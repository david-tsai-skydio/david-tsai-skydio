#!/usr/bin/env python3
"""
audit_postings.py
=================

Re-runs the Skydio careers-page formatting audit that produced
`JOB_POSTING_STYLE_AUDIT.md`.

It pulls every live posting from the Skydio Ashby job board, trims each
posting's HTML at the first `Compensation` block (so the audit only sees the
recruiter-authored "above the compensation block" content), parses the
remaining HTML, and prints a one-line report per posting plus an overall
summary of inconsistencies.

Usage:
    python3 tools/audit_postings.py                # human-readable summary
    python3 tools/audit_postings.py --json out.json # write feature vectors
    python3 tools/audit_postings.py --check        # exit-code 1 if any flagged

Dependencies:
    pip install requests beautifulsoup4 lxml
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

try:
    import requests
except ImportError:
    print("This script needs `requests` (pip install requests).", file=sys.stderr)
    sys.exit(2)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("This script needs `beautifulsoup4` (pip install beautifulsoup4 lxml).",
          file=sys.stderr)
    sys.exit(2)


ASHBY_URL = "https://api.ashbyhq.com/posting-api/job-board/skydio?includeCompensation=true"

COMP_PATTERNS = [
    re.compile(r'<strong[^>]*>\s*Compensation', re.I),
    re.compile(r'<u[^>]*>\s*Compensation', re.I),
    re.compile(r'<b[^>]*>\s*Compensation', re.I),
    re.compile(r'<h[1-6][^>]*>\s*Compensation', re.I),
    re.compile(r'<em[^>]*>\s*Compensation', re.I),
    re.compile(r'<[a-z][^>]*>\s*Compensation\s*(Range)?\s*[:<]', re.I),
]

STYLE_RE = re.compile(r'([a-zA-Z\-]+)\s*:\s*([^;]+)')

SECTION_LABELS = [
    'About the role', 'About you', 'About the team',
    "How you'll make an impact", 'How you’ll make an impact',
    'How you make an impact', 'What makes you a good fit',
    "What you'll do", 'What you’ll do', 'What you will do',
    'Responsibilities', 'Qualifications', 'Requirements',
    'Required qualifications', 'Preferred qualifications',
    'Nice to have', 'Nice-to-have', 'Bonus points', 'Bonus Points',
    'Preferred', 'Why Skydio', 'Benefits',
    'PLEASE NOTE', 'Please note', 'Note',
]


def trim_pre_compensation(html_doc: str) -> tuple[str, int]:
    """Return (pre_compensation_html, cut_index). cut_index = -1 if not found."""
    best = -1
    for pat in COMP_PATTERNS:
        m = pat.search(html_doc)
        if m and (best == -1 or m.start() < best):
            best = m.start()
    if best == -1:
        return html_doc, -1
    walk = best
    while walk > 0 and html_doc[walk - 1] == '>':
        prev_open = html_doc.rfind('<', 0, walk)
        if prev_open == -1:
            break
        tag_text = html_doc[prev_open:walk]
        if re.match(r'<\s*(p|div|span)\b', tag_text, re.I):
            walk = prev_open
        else:
            break
    return html_doc[:walk], walk


def parse_style(style: str | None) -> dict:
    if not style:
        return {}
    return {k.strip().lower(): v.strip() for k, v in STYLE_RE.findall(style)}


def normalize(s: str) -> str:
    return re.sub(r'\s+', ' ', s).strip()


def analyze_posting(title: str, full_html: str) -> dict:
    pre_html, cut = trim_pre_compensation(full_html)
    soup = BeautifulSoup(pre_html, 'lxml')

    feat = {
        'title': title,
        'pre_comp_chars': len(pre_html),
        'has_compensation_marker': cut != -1,
        'tag_counts': Counter(),
        'heading_levels': Counter(),
        'inline_styles': Counter(),
        'style_values': defaultdict(Counter),
        'section_header_style': set(),
        'list_li_with_p': 0,
        'list_li_plain': 0,
    }

    for el in soup.find_all(True):
        feat['tag_counts'][el.name] += 1
        if el.name in ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'):
            feat['heading_levels'][el.name] += 1
        style = el.get('style')
        if style:
            for k, v in parse_style(style).items():
                feat['inline_styles'][k] += 1
                feat['style_values'][k][v] += 1
        if el.name == 'li':
            inner_p = el.find('p', recursive=False)
            if inner_p is not None:
                feat['list_li_with_p'] += 1
            else:
                feat['list_li_plain'] += 1

    label_re = re.compile(
        r'^(?:' + '|'.join(re.escape(l) for l in SECTION_LABELS) + r')\b', re.I)
    for el in soup.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6']):
        txt = normalize(el.get_text())
        if not txt or not label_re.match(txt):
            continue
        if el.name.startswith('h'):
            feat['section_header_style'].add(f'<{el.name}>')
        else:
            if el.find('strong') or el.find('b'):
                feat['section_header_style'].add('<p><strong>')
            elif el.find('u'):
                feat['section_header_style'].add('<p><u>')
            else:
                feat['section_header_style'].add('<p>')

    feat['tag_counts'] = dict(feat['tag_counts'])
    feat['heading_levels'] = dict(feat['heading_levels'])
    feat['inline_styles'] = dict(feat['inline_styles'])
    feat['style_values'] = {k: dict(v) for k, v in feat['style_values'].items()}
    feat['section_header_style'] = sorted(feat['section_header_style'])
    return feat


def flag_anomalies(feat: dict) -> list[str]:
    flags = []
    if feat['heading_levels']:
        flags.append('uses heading tags')
    if '<p><u>' in feat['section_header_style']:
        flags.append('underline section head')
    if 'em' in feat['tag_counts']:
        flags.append('italic')
    if feat['tag_counts'].get('br', 0) >= 4:
        flags.append(f"{feat['tag_counts'].get('br')}× <br>")
    if 'ul' not in feat['tag_counts'] and 'ol' not in feat['tag_counts']:
        flags.append('no bullet list')
    if any(k != 'min-height' for k in feat['inline_styles']):
        flags.append('custom inline CSS')
    if not feat['has_compensation_marker']:
        flags.append('no compensation block')
    if feat['title'] != feat['title'].strip() or '  ' in feat['title']:
        flags.append('title whitespace')
    return flags


def main():
    p = argparse.ArgumentParser(description=__doc__.split('\n')[1])
    p.add_argument('--json', type=Path,
                   help='Write per-posting feature vectors to this path.')
    p.add_argument('--check', action='store_true',
                   help='Exit code 1 if any posting has anomaly flags.')
    p.add_argument('--input', type=Path,
                   help='Read jobs from this JSON file instead of hitting the '
                        'Ashby API (useful in offline / test runs).')
    args = p.parse_args()

    if args.input:
        data = json.loads(args.input.read_text())
    else:
        r = requests.get(ASHBY_URL, timeout=30)
        r.raise_for_status()
        data = r.json()

    jobs = data['jobs']
    feats = []
    for j in jobs:
        feat = analyze_posting(j['title'], j['descriptionHtml'])
        feat['id'] = j['id']
        feat['department'] = j.get('department')
        feat['location'] = j.get('location')
        feat['flags'] = flag_anomalies(feat)
        feats.append(feat)

    if args.json:
        args.json.write_text(json.dumps(feats, indent=2, ensure_ascii=False))
        print(f'Wrote {len(feats)} records -> {args.json}')

    flagged = [f for f in feats if f['flags']]
    print(f'\n== Skydio careers audit: {len(feats)} postings, '
          f'{len(flagged)} with anomalies ==\n')
    for f in feats:
        flag_str = '; '.join(f['flags']) if f['flags'] else 'ok'
        print(f"  - {f['title'].strip()[:60]:60s} | {flag_str}")

    if args.check and flagged:
        sys.exit(1)


if __name__ == '__main__':
    main()
