"""Offline tests for the FuzzingPaper catalog filter."""

from __future__ import annotations

import csv
import contextlib
import importlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


TOOLS_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(TOOLS_DIR))
filter_papers = importlib.import_module("filter_papers")


class CatalogParserTests(unittest.TestCase):
    def test_publication_list_parses_and_resolves_relative_links(self):
        markdown = """# All Papers
- **SP 2025**
  - [Parser (with details)](papers/a_(b).pdf)
  - [Project](https://example.test/project)
  - [Code](https://example.test/code)
  - [Slides](slides.pdf)
  - [Reading Note](notes.md)
  - ![chart](chart.png)
  - [same page](#section)
"""
        papers = filter_papers.parse_catalog(markdown, "https://papers.test/catalog/index.md")
        self.assertEqual(len(papers), 2)
        self.assertEqual(papers[0].title, "Parser (with details)")
        self.assertEqual(papers[0].urls, ["https://papers.test/catalog/papers/a_(b).pdf"])
        self.assertEqual(papers[1].title, "Project")
        self.assertEqual(papers[1].urls, ["https://example.test/project"])
        self.assertEqual(papers[0].categories, ["SP 2025"])

    def test_section_format_and_abstract_variants(self):
        markdown = """# Greybox Fuzzing
### Example: Stateful Fuzzing (USENIX Security 2024)
* [Paper](../paper.pdf)
**Abstract:** First line
  continued line.

# Compilers
### Another Paper (PLDI 2023)
* [Paper](https://example.test/another)
Abstract: A short summary.
"""
        papers = filter_papers.parse_catalog(markdown, "https://papers.test/list.md")
        self.assertEqual([p.title for p in papers], [
            "Example: Stateful Fuzzing (USENIX Security 2024)",
            "Another Paper (PLDI 2023)",
        ])
        self.assertEqual(papers[0].categories, ["Greybox Fuzzing"])
        self.assertEqual(papers[0].urls, ["https://papers.test/paper.pdf"])
        self.assertIn("First line", papers[0].abstract)
        self.assertIn("continued line.", papers[0].abstract)
        self.assertEqual(papers[1].categories, ["Compilers"])
        self.assertEqual(papers[1].abstract, "A short summary.")

    def test_deduplicates_normalized_title_and_merges_metadata(self):
        markdown = """- **SP 2025**
  - [Shared Paper (SP 2025)](one.pdf)
  - [Shared Paper (SP 2025)](two.pdf)
# Systems
### Shared Paper (CCS 2024)
* [Paper2](https://example.test/three)
Abstract: Merged abstract.
"""
        papers = filter_papers.parse_catalog(markdown, "https://papers.test/index.md")
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0].title, "Shared Paper (SP 2025)")
        self.assertEqual(papers[0].urls, [
            "https://papers.test/one.pdf", "https://papers.test/two.pdf",
            "https://example.test/three",
        ])
        self.assertEqual(papers[0].categories, ["SP 2025", "Systems"])
        self.assertIn("Merged abstract.", papers[0].abstract)

    def test_real_abstract_label_without_link_preserves_section(self):
        markdown = """# Static Analysis
### Paper Without Link (CCS 2024)
**Abstract**: This paper has no linked resource.
"""
        papers = filter_papers.parse_catalog(markdown, "https://papers.test/list.md")
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0].title, "Paper Without Link (CCS 2024)")
        self.assertEqual(papers[0].urls, [])
        self.assertEqual(papers[0].abstract, "This paper has no linked resource.")

    def test_distinct_titles_with_same_url_remain_separate(self):
        markdown = """- **SP 2025**
  - [First Paper](https://example.test/shared)
  - [Second Paper](https://example.test/shared)
"""
        papers = filter_papers.parse_catalog(markdown, "https://papers.test/list.md")
        self.assertEqual([paper.title for paper in papers], ["First Paper", "Second Paper"])
        self.assertEqual(papers[0].urls, papers[1].urls)

    def test_code_fence_links_are_ignored(self):
        markdown = """# Fuzzing
### Real Paper (SP 2025)
* [Paper](real.pdf)
```markdown
* [Example Paper](fake.pdf)
```
"""
        papers = filter_papers.parse_catalog(markdown, "https://papers.test/list.md")
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0].title, "Real Paper (SP 2025)")
        self.assertEqual(papers[0].urls, ["https://papers.test/real.pdf"])


class MatchingAndHtmlTests(unittest.TestCase):
    def test_keyword_word_boundaries_casefold_and_substring_mode(self):
        text = "API api randomApi DOM domain"
        self.assertEqual(filter_papers.keyword_matches(text, ["api", "dom"]), ["api", "dom"])
        self.assertEqual(filter_papers.keyword_matches("capital random", ["api", "dom"]), [])
        self.assertEqual(
            filter_papers.keyword_matches(text, ["api"], mode="substring"), ["api"]
        )

    def test_visible_text_decodes_entities_and_skips_hidden_elements(self):
        html = """<html><body>Hello&nbsp;<b>world &amp; friends</b>
<script>bad()</script><style>.bad{}</style><noscript>off</noscript>
<template>hidden</template><svg><text>vector</text></svg></body></html>"""
        visible = filter_papers.visible_text(html)
        self.assertIn("Hello", visible)
        self.assertIn("world & friends", visible)
        for hidden in ("bad()", "off", "hidden", "vector"):
            self.assertNotIn(hidden, visible)


class FetchTests(unittest.TestCase):
    def test_fetches_html_successfully_with_bounded_read(self):
        response = _Response(b"<html><body>Page text</body></html>", "text/html; charset=utf-8")
        with patch.object(filter_papers, "urlopen", return_value=response) as urlopen:
            result = filter_papers.fetch_page("https://example.test/page", timeout=7, max_bytes=128)
        self.assertEqual(result.status, "ok")
        self.assertIn("Page text", result.text)
        urlopen.assert_called_once()

    def test_pdf_detected_by_type_or_signature(self):
        for content_type, body in (("application/pdf", b"not needed"),
                                   ("application/octet-stream", b"%PDF-1.7 data")):
            response = _Response(body, content_type)
            with self.subTest(content_type=content_type), patch.object(filter_papers, "urlopen", return_value=response):
                self.assertEqual(
                    filter_papers.fetch_page("https://example.test/file", max_bytes=128).status,
                    "skipped_pdf",
                )

    def test_fetch_classifies_other_content_types_and_errors(self):
        response = _Response(b"image bytes", "image/png")
        with patch.object(filter_papers, "urlopen", return_value=response):
            self.assertEqual(filter_papers.fetch_page("https://example.test/image").status, "skipped_type")
        with patch.object(filter_papers, "urlopen", side_effect=OSError("offline")):
            result = filter_papers.fetch_page("https://example.test/page")
        self.assertEqual(result.status, "error")
        self.assertTrue(result.error)

    def test_size_limit_is_reported_as_error(self):
        response = _Response(b"x" * 12, "text/plain")
        with patch.object(filter_papers, "urlopen", return_value=response):
            result = filter_papers.fetch_page("https://example.test/large", max_bytes=10)
        self.assertEqual(result.status, "error")
        self.assertIn("exceeds 10 bytes", result.error)


class SearchTests(unittest.TestCase):
    def test_external_page_match_and_shared_url_is_fetched_once(self):
        papers = [
            filter_papers.Paper("Alpha", ["https://example.test/shared"]),
            filter_papers.Paper("Beta", ["https://example.test/shared"]),
        ]
        page = filter_papers.PageResult("https://example.test/shared", "ok", "contains UNIQUEWORD")
        with patch.object(filter_papers, "fetch_page", return_value=page) as fetch:
            results = list(filter_papers.search(papers, ["uniqueword"], fetch=True, delay=0))
        self.assertEqual(fetch.call_count, 1)
        self.assertEqual(results[0]["matched_fields"], ["pages"])
        self.assertEqual(results[1]["matched_fields"], ["pages"])

    def test_failed_external_page_keeps_title_match(self):
        paper = filter_papers.Paper("Target Keyword", ["https://example.test/fail"])
        failed = filter_papers.PageResult(paper.urls[0], "error", error="offline")
        with patch.object(filter_papers, "fetch_page", return_value=failed):
            result = list(filter_papers.search([paper], ["target"], fetch=True, delay=0))[0]
        self.assertEqual(result["matched_fields"], ["title"])
        self.assertEqual(result["pages"][0]["status"], "error")


class CliTests(unittest.TestCase):
    def test_json_cli_exports_matching_papers_offline(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "papers.md"
            output = root / "papers.json"
            source.write_text("- **SP 2025**\n  - [API Fuzzing](https://example.test/api)\n", encoding="utf-8")
            with contextlib.redirect_stderr(io.StringIO()):
                status = filter_papers.main([
                    str(source), "-k", "api", "--format", "json", "-o", str(output),
                    "--base-url", "https://papers.test/catalog.md",
                ])
            self.assertEqual(status, 0)
            exported = json.loads(output.read_text(encoding="utf-8"))
            self.assertEqual(exported[0]["title"], "API Fuzzing")

    def test_csv_cli_writes_header_and_missing_source_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "papers.md"
            output = root / "papers.csv"
            source.write_text("- **SP 2025**\n  - [Fuzzer](paper.pdf)\n", encoding="utf-8")
            with contextlib.redirect_stderr(io.StringIO()):
                status = filter_papers.main([str(source), "-k", "fuzzer", "--format", "csv", "-o", str(output)])
            self.assertEqual(status, 0)
            with output.open(encoding="utf-8", newline="") as stream:
                rows = list(csv.DictReader(stream))
            self.assertEqual(rows[0]["title"], "Fuzzer")
            with contextlib.redirect_stderr(io.StringIO()):
                self.assertNotEqual(filter_papers.main([str(root / "missing.md"), "-k", "fuzz"]), 0)

    def test_empty_keyword_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "papers.md"
            source.write_text("", encoding="utf-8")
            with contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit) as error:
                filter_papers.main([str(source), "-k", "   "])
            self.assertEqual(error.exception.code, 2)

    def test_include_unmatched_exports_fetch_errors_in_csv_and_json(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "papers.md"
            source.write_text(
                "- **SP 2025**\n  - [Unmatched Paper](https://example.test/page)\n",
                encoding="utf-8",
            )
            failed = filter_papers.PageResult("https://example.test/page", "error", error="offline")
            for format_name in ("csv", "json"):
                output = root / f"papers.{format_name}"
                with self.subTest(format=format_name):
                    with patch.object(filter_papers, "fetch_page", return_value=failed):
                        with contextlib.redirect_stderr(io.StringIO()):
                            status = filter_papers.main([
                                str(source), "-k", "absent", "--fetch-pages", "--include-unmatched",
                                "--format", format_name, "-o", str(output),
                            ])
                self.assertEqual(status, 1)
                if format_name == "json":
                    data = json.loads(output.read_text(encoding="utf-8"))
                    self.assertEqual(data[0]["pages"][0]["status"], "error")
                    self.assertEqual(data[0]["title"], "Unmatched Paper")
                else:
                    with output.open(encoding="utf-8", newline="") as stream:
                        rows = list(csv.DictReader(stream))
                    self.assertIn('"status": "error"', rows[0]["pages"])
                    self.assertEqual(rows[0]["title"], "Unmatched Paper")


class _Response:
    def __init__(self, body, content_type):
        from email.message import Message

        self._body = body
        self._position = 0
        self.headers = Message()
        self.headers["Content-Type"] = content_type

    def __enter__(self):
        return self

    def __exit__(self, *args):
        return False

    def read(self, size=-1):
        if size < 0:
            size = len(self._body) - self._position
        chunk = self._body[self._position:self._position + size]
        self._position += len(chunk)
        return chunk

    def geturl(self):
        return "https://example.test/page"


if __name__ == "__main__":
    unittest.main()
