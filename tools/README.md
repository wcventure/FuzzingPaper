# Filter papers by keyword

`filter_papers.py` extracts entries from this repository's Markdown catalog and
filters their titles and abstracts. Optionally, it also searches the HTML or plain
text at the paper links. Requires Python 3.9 or later; no third-party dependencies.

From the repository root:

```sh
python3 tools/filter_papers.py README.md -k browser -k javascript --format csv -o results.csv
python3 tools/filter_papers.py README.md --keywords-file keywords.txt --format urls -o links.txt
```

Keywords are combined with **OR** and matched without case sensitivity. By default,
word boundaries prevent `api` from matching `capital` or `dom` from matching
`random`. Use `--match substring` for prefixes, plurals, or the original crawler's
substring behavior. There is no stemming or automatic synonym expansion.
Keyword files accept one keyword or phrase per line, ignoring blank lines and
lines starting with `#`. No topic-specific keywords are built in.

You can use another local catalog or a raw/GitHub blob URL:

```sh
python3 tools/filter_papers.py \
  https://raw.githubusercontent.com/wcventure/FuzzingPaper/master/README.md \
  -k 'REST API' -k protocol --format json -o results.json
```

Relative paper links resolve against the source location. Local files produce
`file:` URLs; to export shareable links from a local checkout, add:

```sh
--base-url https://raw.githubusercontent.com/wcventure/FuzzingPaper/master/README.md
```

## Searching external pages

```sh
python3 tools/filter_papers.py README.md -k browser \
  --base-url https://raw.githubusercontent.com/wcventure/FuzzingPaper/master/README.md \
  --fetch-pages --timeout 20 --delay 1 --include-unmatched \
  --format json -o search-report.json
```

This fetches each distinct paper URL once per run, including papers that did not
match the catalog text, to find matches present only on external pages. It searches
visible HTML text, excluding scripts, styles, SVGs and templates. It does not crawl
links within those pages, execute JavaScript, or authenticate with publishers.
Pages containing login screens or navigation may still produce irrelevant matches;
results are candidates for manual review, not evidence of full-text coverage.

Requests are sequential, with a configurable pause between URLs. The timeout is
per socket operation, not a total-run deadline. Pages are limited to 2 MB and the
remote catalog to 10 MB. Failed requests do not discard matches in catalog text
or stop the other articles from being searched. No automatic retries are made.
The Python standard library honors the environment's proxy settings.

PDFs are marked `skipped_pdf`; their binary contents are never searched as text.
Non-HTTP links and unsupported media types are marked `skipped_type`. PDF text
extraction and downloading are outside this utility's scope.

## Output and limitations

- CSV and JSON contain titles, paper URLs, categories, abstracts, matched keywords,
  matched fields (`title`, `abstract`, `pages`), and per-page statuses/errors.
- By default only matching records are exported. `--include-unmatched` retains
  the complete audit trail, including failures for papers with no matches.
- The `urls` format exports unique paper URLs from the selected records. These can
  be publisher landing pages, not necessarily direct PDF links.
- Statistics go to stderr so stdout can be redirected without corrupting output.
- Exit codes: 0 for a completed run (including zero matches), 1 if external
  requests failed (results are still written), 2 for input/configuration errors,
  130 for interruption. Skipped PDFs are reported but do not cause exit code 1.

The parser supports the catalog's two formats: bulleted `[Title](URL)` lists
(optionally grouped by `- **Venue Year**`), and `### Title` sections containing
`[Paper]`, `[Paper1]`, `[Paper2]`, `[PDF]` or `[Link]` links and an `Abstract:` marker.
It handles multiline abstracts, inline HTML, relative URLs and balanced parentheses
in inline destinations. Code fences, images, internal anchors, code repositories,
slides and reading notes are not treated as paper links.

This is a parser for those conventions, not a complete CommonMark implementation:
tables and reference-style links are not supported. A section with an abstract but
no valid paper link is retained with an empty URL list, reported in the summary.
Malformed links are not guessed or repaired. Duplicate titles are merged ignoring
case, whitespace and trailing parenthetical venue/year annotations. This heuristic
can combine versions of a work with the same title. Different titles sharing a URL
remain separate, allowing catalog mistakes to be inspected rather than hidden.

## Tests

```sh
python3 -B -m unittest discover -s tools/tests -v
```

Tests use synthetic catalogs and mocked HTTP responses; they require no internet,
institutional account or publisher access. For a manual integration check, run
against the current README and inspect the exported matches and skipped entries.
