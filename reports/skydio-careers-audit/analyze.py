#!/usr/bin/env python3
"""
Extract the pre-compensation portion of each Skydio job posting and
characterize formatting features.

We focus on what writers control inside the rich-text body
(the <div class="prose block-content">...</div> region):
  - Use of headings vs. <p><strong>...</strong></p>
  - Section header punctuation/casing
  - Bulleted-list structure (<li><p>..</p></li> vs <li>..</li>)
  - Stray <br>, &nbsp;, smart quotes
  - Inline style="..." attributes (color, font-size, font-family)
  - Empty paragraphs / <p>&nbsp;</p>
  - Whitespace around the title
  - Whether the boilerplate Skydio intro paragraph is present

The Skydio site renders all of these inside a `prose` Tailwind block, so the
visual rendering (font sizes, line-heights, alignment) is uniform when writers
use the same markup. Inconsistencies in markup are therefore the proximate
cause of any visual inconsistencies users see.
"""
import os, re, json, html as html_mod, collections

RAW_DIR = "/tmp/jobs/raw"
INDEX = json.load(open("/tmp/jobs/index.json"))

PROSE_RE = re.compile(
    r'<div class="prose block-content">(.*?)</div>\s*</stack-l>',
    re.S,
)
TITLE_RE = re.compile(r'<h1 class="type-h2">(.*?)</h1>', re.S)
TITLE_LOC_RE = re.compile(r'<p class="type-body-2">\s*(.*?)\s*</p>', re.S)


# Patterns we recognize as the *start* of the compensation/legal block.
# Recruiters use a few different phrasings; we cut at whichever appears first.
COMPENSATION_MARKERS = [
    r'<strong>Compensation\b',
    r'<strong>Compensation\s*&\s*Benefits',
    r'<strong>Compensation\s*and\s*Benefits',
    r'<p>\s*<strong>Compensation\b',
    r'<b>Compensation\b',
    r'<h[1-6][^>]*>\s*Compensation\b',
    # Some posts dive straight into a salary-range sentence prefixed with
    # "At Skydio, our compensation packages..." with no explicit header.
    r'At Skydio, our compensation packages',
    r'The annual base salary range',
]
COMPENSATION_RE = re.compile("|".join(COMPENSATION_MARKERS), re.I)


def strip_tags(s: str) -> str:
    s = re.sub(r'<[^>]+>', '', s)
    s = html_mod.unescape(s)
    return re.sub(r'\s+', ' ', s).strip()


def split_at_compensation(prose_html: str):
    m = COMPENSATION_RE.search(prose_html)
    if not m:
        return prose_html, None
    # Walk backwards to the start of the enclosing <p> or <h*> if present
    start = m.start()
    # Look back for the nearest opening tag that starts the block
    snippet = prose_html[:start]
    last_p = snippet.rfind('<p')
    last_h = max(snippet.rfind('<h2'), snippet.rfind('<h3'),
                 snippet.rfind('<h4'), snippet.rfind('<h5'),
                 snippet.rfind('<h6'))
    cut = max(last_p, last_h)
    if cut == -1:
        cut = start
    return prose_html[:cut], prose_html[cut:]


SECTION_HEADER_PATTERNS = [
    # <p><strong>About the role:</strong></p>  (the dominant style)
    (re.compile(r'<p>\s*<strong>(.{2,120}?)</strong>\s*</p>', re.S), "p_strong"),
    (re.compile(r'<p>\s*<b>(.{2,120}?)</b>\s*</p>', re.S), "p_b"),
    # <h2><strong>About the role:</strong></h2> -- the alternate/outlier style
    (re.compile(r'<h2[^>]*>\s*(?:<strong>)?\s*(.{2,120}?)\s*(?:</strong>)?\s*</h2>', re.S), "h2"),
    (re.compile(r'<h3[^>]*>\s*(?:<strong>)?\s*(.{2,120}?)\s*(?:</strong>)?\s*</h3>', re.S), "h3"),
    (re.compile(r'<h4[^>]*>\s*(?:<strong>)?\s*(.{2,120}?)\s*(?:</strong>)?\s*</h4>', re.S), "h4"),
    (re.compile(r'<h5[^>]*>\s*(?:<strong>)?\s*(.{2,120}?)\s*(?:</strong>)?\s*</h5>', re.S), "h5"),
    (re.compile(r'<h6[^>]*>\s*(?:<strong>)?\s*(.{2,120}?)\s*(?:</strong>)?\s*</h6>', re.S), "h6"),
]


def find_section_headers(html: str):
    """Return list of (header_text, kind) preserving document order."""
    found = []
    seen_spans = []
    # Process header tags first so we don't double count their inner <strong> as p_strong
    ordered = sorted(SECTION_HEADER_PATTERNS,
                     key=lambda x: 0 if x[1].startswith('h') else 1)
    for pat, kind in ordered:
        for m in pat.finditer(html):
            # Skip overlap with already-claimed spans
            if any(s <= m.start() < e for s, e in seen_spans):
                continue
            text = strip_tags(m.group(1))
            if not text:
                continue
            found.append((m.start(), text, kind))
            seen_spans.append((m.start(), m.end()))
    found.sort(key=lambda t: t[0])
    return [(t, k) for _, t, k in found]


SKYDIO_INTRO_SIG = "Skydio is the leading"


def analyze(prose_html: str):
    pre_html, post_html = split_at_compensation(prose_html)

    headers = find_section_headers(pre_html)
    header_kinds = collections.Counter(k for _, k in headers)
    header_texts = [t for t, _ in headers]

    # Bullet-list structure
    list_items = re.findall(r'<li\b[^>]*>(.*?)</li>', pre_html, re.S)
    li_with_p = sum(1 for li in list_items if re.match(r'\s*<p\b', li))
    li_plain = len(list_items) - li_with_p
    # Bullet items that begin with a bolded lead-in (e.g. "<strong>Design...</strong> rest")
    li_bold_leadin = sum(
        1 for li in list_items
        if re.match(r'\s*(?:<p\b[^>]*>\s*)?<strong>', li)
    )
    # Bullet items containing a link
    li_with_link = sum(1 for li in list_items if '<a ' in li)

    # Heuristic indicators
    intro_present = SKYDIO_INTRO_SIG in pre_html

    issues = {
        "br_tags": len(re.findall(r'<br\s*/?>', pre_html)),
        "nbsp": pre_html.count('&nbsp;') + pre_html.count('\u00a0'),
        "smart_quotes": (
            pre_html.count('\u2019') + pre_html.count('\u2018')
            + pre_html.count('\u201c') + pre_html.count('\u201d')
        ),
        "inline_style": len(re.findall(r'\sstyle="[^"]*"', pre_html)),
        "inline_color": len(re.findall(r'color\s*:', pre_html, re.I)),
        "inline_font_size": len(re.findall(r'font-size\s*:', pre_html, re.I)),
        "inline_font_family": len(re.findall(r'font-family\s*:', pre_html, re.I)),
        "empty_paragraphs": len(re.findall(
            r'<p>\s*(?:&nbsp;|\u00a0|\s)*\s*</p>', pre_html)),
        "all_caps_headers": sum(
            1 for t, _ in headers
            if len(re.sub(r'[^A-Za-z]', '', t)) >= 3
            and t == t.upper()
            and t.upper() != t.lower()
        ),
        "headers_no_colon": sum(
            1 for t, _ in headers if not t.rstrip().endswith(':')
        ),
        "headers_with_colon": sum(
            1 for t, _ in headers if t.rstrip().endswith(':')
        ),
        "uses_hr": len(re.findall(r'<hr\b', pre_html)),
        "uses_em": len(re.findall(r'<em\b', pre_html)),
        "uses_u": len(re.findall(r'<u\b', pre_html)),
        "uses_underline_style": len(re.findall(
            r'text-decoration\s*:\s*underline', pre_html, re.I)),
        "uses_h_tag": header_kinds.get("h2", 0) + header_kinds.get("h3", 0)
                      + header_kinds.get("h4", 0) + header_kinds.get("h5", 0)
                      + header_kinds.get("h6", 0),
        "uses_p_strong_header": header_kinds.get("p_strong", 0),
        "uses_p_b_header": header_kinds.get("p_b", 0),
        "li_with_p": li_with_p,
        "li_plain": li_plain,
        "li_bold_leadin": li_bold_leadin,
        "li_with_link": li_with_link,
        "n_list_items": len(list_items),
        "n_paragraphs": len(re.findall(r'<p[\s>]', pre_html)),
        "n_lists": len(re.findall(r'<ul[\s>]', pre_html))
                   + len(re.findall(r'<ol[\s>]', pre_html)),
        "intro_present": intro_present,
        "pre_chars": len(strip_tags(pre_html)),
        "headers": header_texts,
        "header_kinds": dict(header_kinds),
    }
    return issues, pre_html, post_html


results = []
for j in INDEX:
    fname = os.path.join(RAW_DIR, f"{j['uuid']}.html")
    if not os.path.exists(fname):
        continue
    full = open(fname).read()
    title_m = TITLE_RE.search(full)
    title_in_page = strip_tags(title_m.group(1)) if title_m else j["title"]
    title_raw = title_m.group(1) if title_m else j["title"]
    title_has_trailing_ws = bool(re.search(r'\s$', title_in_page)) \
                            or title_in_page != title_in_page.strip()
    # Trailing whitespace inside the H1 text node
    title_inner_trailing = title_raw.endswith(' ') or title_raw.endswith('\t') \
                           or title_raw.endswith('\n ')

    prose_m = PROSE_RE.search(full)
    if not prose_m:
        # fallback
        m = re.search(r'<div class="prose block-content">(.*)', full, re.S)
        if m:
            chunk = m.group(1)
            # cut at next </div> closing the prose block (best effort)
            depth = 1
            i = 0
            while i < len(chunk) and depth > 0:
                if chunk[i:i+5] == '<div ' or chunk[i:i+4] == '<div>':
                    depth += 1
                elif chunk[i:i+6] == '</div>':
                    depth -= 1
                    if depth == 0:
                        break
                i += 1
            prose_html = chunk[:i]
        else:
            print("MISSING PROSE:", j["uuid"])
            continue
    else:
        prose_html = prose_m.group(1)

    issues, pre_html, post_html = analyze(prose_html)
    issues["uuid"] = j["uuid"]
    issues["title"] = title_in_page.strip()
    issues["title_in_h1_raw"] = title_raw
    issues["title_inner_trailing_ws"] = title_inner_trailing
    issues["loc"] = j["loc"]
    issues["had_compensation_marker"] = post_html is not None
    results.append(issues)

with open('/tmp/jobs/analysis.json', 'w') as f:
    json.dump(results, f, indent=2)
print("Analyzed", len(results), "jobs")
