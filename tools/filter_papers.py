#!/usr/bin/env python3
"""Extract and filter papers from a Markdown catalog (Python 3.9+, standard library)."""

import argparse
import csv
import io
import json
import math
import re
import sys
import time
from dataclasses import asdict, dataclass, field
from html.parser import HTMLParser
from http.client import HTTPException
from pathlib import Path
from urllib.error import URLError
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen


class TextParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []
        self.hidden = []

    def handle_starttag(self, tag, attrs):
        if tag in {'script', 'style', 'noscript', 'template', 'svg'}:
            self.hidden.append(tag)
        if tag in {'p', 'div', 'br', 'li', 'section', 'h1', 'h2', 'h3'}:
            self.parts.append(' ')

    def handle_startendtag(self, tag, attrs):
        self.parts.append(' ')

    def handle_endtag(self, tag):
        if self.hidden and tag == self.hidden[-1]:
            self.hidden.pop()
        if tag in {'p', 'div', 'li', 'section', 'h1', 'h2', 'h3'}:
            self.parts.append(' ')

    def handle_data(self, data):
        if not self.hidden:
            self.parts.append(data)


def visible_text(html):
    parser = TextParser()
    parser.feed(html)
    return ' '.join(''.join(parser.parts).split())


def markdown_links(text):
    """Inline links with balanced parentheses; reference-style links are not supported."""
    pattern = re.compile(r'(?<!!)\[((?:\\.|[^\]\\])*)\]\(')
    for match in pattern.finditer(text):
        start = pos = match.end()
        depth = 1
        while pos < len(text) and depth:
            if text[pos] == '\\':
                pos += 2
                continue
            if text[pos] == '(':
                depth += 1
            elif text[pos] == ')':
                depth -= 1
            pos += 1
        if depth:
            continue
        destination = text[start:pos - 1].strip()
        if destination.startswith('<'):
            destination = destination[1:].split('>', 1)[0]
        else:
            destination = destination.split()[0] if destination else ''
        yield match.group(1), re.sub(r'\\([()])', r'\1', destination)


def plain_markdown(text):
    text = re.sub(r'!?\[([^\]]+)\]\([^\n]*?\)', r'\1', text)
    return visible_text(text).replace('**', '').replace('`', '').strip()


@dataclass
class Paper:
    title: str
    urls: list = field(default_factory=list)
    categories: list = field(default_factory=list)
    abstract: str = ''


def title_key(title):
    title = re.sub(r'\s*\([^()]*(?:19|20)\d{2}[^()]*\)\s*$', '', title)
    return ' '.join(title.casefold().split())


def parse_catalog(markdown, base_url):
    papers = []
    current = None
    category = group = ''
    abstract_lines = []
    in_abstract = False
    fence = None
    resource = re.compile(r'^(?:paper\d*|pdf|link|code.*|slides?.*|video.*|reading.*|demo|poc)$', re.I)
    paper_label = re.compile(r'^(?:paper\d*|pdf|link)$', re.I)

    def finish():
        if current:
            current.abstract = plain_markdown(' '.join(abstract_lines))
            if current.urls or current.abstract:
                papers.append(current)

    for line in markdown.splitlines():
        stripped = line.strip()
        fence_match = re.match(r'^(`{3,}|~{3,})', stripped)
        if fence_match:
            marker = fence_match.group(1)[0]
            fence = None if fence == marker else marker if fence is None else fence
            continue
        if fence:
            continue
        heading = re.match(r'^(#{1,6})\s+(.+?)\s*#*$', stripped)
        if heading:
            finish()
            current, abstract_lines, in_abstract = None, [], False
            level, title = len(heading.group(1)), plain_markdown(heading.group(2))
            if level <= 2:
                category, group = title, ''
            elif level == 3:
                current = Paper(title, categories=[category] if category else [])
            continue
        grouping = re.match(r'^[-*+]\s+\*\*(.+?)\*\*\s*$', stripped)
        if grouping and current is None:
            group = plain_markdown(grouping.group(1))
            continue
        abstract = re.match(r'^\*{0,2}Abstract\*{0,2}\s*:\*{0,2}\s*(.*)', stripped, re.I)
        if current and abstract:
            in_abstract = True
            abstract_lines.append(abstract.group(1))
            continue
        if current and in_abstract:
            abstract_lines.append(stripped)
            continue
        if not re.match(r'^[-*+]\s', stripped):
            continue
        for label, destination in markdown_links(stripped):
            if not destination or destination.startswith('#'):
                continue
            url = urljoin(base_url, destination)
            if urlparse(url).scheme not in ('http', 'https', 'file'):
                continue
            label = plain_markdown(label)
            if current:
                if paper_label.fullmatch(label) and url not in current.urls:
                    current.urls.append(url)
            elif not resource.fullmatch(label):
                papers.append(Paper(label, [url], [group or category] if group or category else []))
    finish()
    merged = {}
    for paper in papers:
        key = title_key(paper.title)
        if key not in merged:
            merged[key] = paper
            continue
        target = merged[key]
        target.urls = list(dict.fromkeys(target.urls + paper.urls))
        target.categories = list(dict.fromkeys(target.categories + paper.categories))
        if paper.abstract and paper.abstract not in target.abstract:
            target.abstract = ' '.join(filter(None, [target.abstract, paper.abstract]))
    return list(merged.values())


def keyword_matches(text, keywords, mode='word'):
    text = text.casefold()
    return [keyword for keyword in keywords if (
        keyword.casefold() in text if mode == 'substring'
        else re.search(r'(?<!\w)' + re.escape(keyword.casefold()) + r'(?!\w)', text)
    )]


@dataclass
class PageResult:
    url: str
    status: str
    text: str = ''
    error: str = ''


def fetch_page(url, timeout=20, max_bytes=2_000_000):
    if urlparse(url).scheme not in ('http', 'https'):
        return PageResult(url, 'skipped_type', error='Only HTTP(S) pages are fetched')
    try:
        request = Request(url, headers={'User-Agent': 'FuzzingPaperFilter/1.0'})
        with urlopen(request, timeout=timeout) as response:
            kind = response.headers.get_content_type()
            if kind == 'application/pdf':
                return PageResult(url, 'skipped_pdf')
            data = response.read(max_bytes + 1)
            if data.lstrip().startswith(b'%PDF-'):
                return PageResult(url, 'skipped_pdf')
            if len(data) > max_bytes:
                return PageResult(url, 'error', error=f'Response exceeds {max_bytes} bytes')
            if kind not in ('text/html', 'application/xhtml+xml', 'text/plain'):
                return PageResult(url, 'skipped_type', error=f'Unsupported content type: {kind}')
            encoding = response.headers.get_content_charset() or 'utf-8'
            text = data.decode(encoding, errors='replace')
            return PageResult(url, 'ok', visible_text(text) if kind != 'text/plain' else text)
    except (URLError, OSError, HTTPException, ValueError, LookupError) as exc:
        return PageResult(url, 'error', error=str(exc))


def read_source(source, timeout):
    parsed = urlparse(source)
    if parsed.scheme in ('http', 'https'):
        if parsed.hostname == 'github.com' and '/blob/' in parsed.path:
            source = 'https://raw.githubusercontent.com/' + parsed.path.lstrip('/').replace('/blob/', '/', 1)
        request = Request(source, headers={'User-Agent': 'FuzzingPaperFilter/1.0'})
        with urlopen(request, timeout=timeout) as response:
            data = response.read(10_000_001)
            if len(data) > 10_000_000:
                raise ValueError('Catalog exceeds 10 MB')
            return data.decode('utf-8-sig'), response.geturl()
    path = Path(source).resolve()
    return path.read_text(encoding='utf-8-sig'), path.as_uri()


def search(papers, keywords, mode='word', fetch=False, timeout=20, delay=1):
    cache = {}
    for paper in papers:
        fields = {'title': paper.title, 'abstract': paper.abstract}
        pages = []
        if fetch:
            for url in paper.urls:
                if url not in cache:
                    if cache:
                        time.sleep(delay)
                    cache[url] = fetch_page(url, timeout)
                page = cache[url]
                pages.append({k: v for k, v in asdict(page).items() if k != 'text'})
                if page.status == 'ok':
                    fields['pages'] = fields.get('pages', '') + '\n' + page.text
        matches = {name: keyword_matches(text, keywords, mode) for name, text in fields.items()}
        yield {**asdict(paper),
               'matched_keywords': [k for k in keywords if any(k in hit for hit in matches.values())],
               'matched_fields': [name for name, hit in matches.items() if hit], 'pages': pages}


def serialize(records, format):
    if format == 'json':
        return json.dumps(records, ensure_ascii=False, indent=2) + '\n'
    if format == 'urls':
        urls = list(dict.fromkeys(url for row in records for url in row['urls']))
        return '\n'.join(urls) + ('\n' if urls else '')
    stream = io.StringIO(newline='')
    fields = ['title', 'urls', 'categories', 'abstract', 'matched_keywords', 'matched_fields', 'pages']
    writer = csv.DictWriter(stream, fieldnames=fields)
    writer.writeheader()
    for record in records:
        writer.writerow({key: json.dumps(value, ensure_ascii=False) if isinstance(value, list) else value
                         for key, value in record.items()})
    return stream.getvalue()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', help='Local Markdown file or raw/GitHub blob URL')
    parser.add_argument('-k', '--keyword', action='append', default=[])
    parser.add_argument('--keywords-file', type=Path, help='One keyword/phrase per line; # comments allowed')
    parser.add_argument('--base-url', help='Resolve relative paper links against this URL')
    parser.add_argument('--match', choices=['word', 'substring'], default='word')
    parser.add_argument('--fetch-pages', action='store_true', help='Also search external HTML/text pages')
    parser.add_argument('--include-unmatched', action='store_true', help='Include every paper and fetch status')
    parser.add_argument('--timeout', type=float, default=20)
    parser.add_argument('--delay', type=float, default=1)
    parser.add_argument('--format', choices=['csv', 'json', 'urls'], default='csv')
    parser.add_argument('-o', '--output', type=Path, help='Default: stdout')
    args = parser.parse_args(argv)
    if not math.isfinite(args.timeout) or args.timeout <= 0 or not math.isfinite(args.delay) or args.delay < 0:
        parser.error('timeout must be positive and delay must be nonnegative (finite seconds)')
    try:
        keywords = list(args.keyword)
        if args.keywords_file:
            keywords.extend(line.strip() for line in args.keywords_file.read_text(encoding='utf-8-sig').splitlines()
                            if line.strip() and not line.lstrip().startswith('#'))
        keywords = list({k.strip().casefold(): k.strip() for k in keywords if k.strip()}.values())
        if not keywords:
            parser.error('provide at least one nonempty --keyword or --keywords-file')
        markdown, source_base = read_source(args.source, args.timeout)
        papers = parse_catalog(markdown, args.base_url or source_base)
        if not papers:
            raise ValueError('No paper entries found; check the source and supported Markdown format')
        results = list(search(papers, keywords, args.match, args.fetch_pages, args.timeout, args.delay))
        matched = [r for r in results if r['matched_keywords']]
        exported = results if args.include_unmatched else matched
        output = serialize(exported, args.format)
        if args.output:
            if urlparse(args.source).scheme not in ('http', 'https') and args.output.resolve() == Path(args.source).resolve():
                raise ValueError('Output must not overwrite the input catalog')
            args.output.write_text(output, encoding='utf-8')
        else:
            sys.stdout.write(output)
        statuses = {(p['url'], p['status']) for r in results for p in r['pages']}
        failures = sum(status == 'error' for _, status in statuses)
        skipped = sum(status.startswith('skipped') for _, status in statuses)
        missing_links = sum(not paper.urls for paper in papers)
        print(f'{len(papers)} papers; {len(matched)} matches; {failures} page errors; '
              f'{skipped} skipped pages; {missing_links} entries without paper links.', file=sys.stderr)
        if failures or skipped:
            print('External search is incomplete. Use --include-unmatched --format json to inspect statuses.', file=sys.stderr)
        return 1 if failures else 0
    except (OSError, ValueError, HTTPException) as exc:
        print(f'Error: {exc}', file=sys.stderr)
        return 2


if __name__ == '__main__':
    try:
        sys.exit(main())
    except KeyboardInterrupt:
        print('Interrupted.', file=sys.stderr)
        sys.exit(130)
