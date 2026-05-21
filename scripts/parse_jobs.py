#!/usr/bin/env python3
"""Extract and analyze pre-compensation formatting from Skydio job postings."""

import os
import re
import json
import html
from collections import Counter, defaultdict
from pathlib import Path

HTML_DIR = Path("/tmp/jobs/html")
OUT_DIR = Path("/tmp/jobs/parsed")
OUT_DIR.mkdir(exist_ok=True)

# --- Helpers ---------------------------------------------------------------

JOB_POST_RE = re.compile(
    r'<div\s+class="container container--small content-grid job-post[^"]*"[^>]*>(.*?)</div>\s*</section>',
    re.DOTALL,
)
# fallback - we find the container start, then walk forward to end of <section>
TITLE_RE = re.compile(r'<h1[^>]*class="type-h2"[^>]*>(.*?)</h1>', re.DOTALL)
LOC_RE = re.compile(r'<p[^>]*class="type-body-2"[^>]*>(.*?)</p>', re.DOTALL)
PROSE_RE = re.compile(
    r'<div\s+class="prose block-content"[^>]*>(.*)',
    re.DOTALL,
)

TAG_RE = re.compile(r'<[^>]+>')
SPACES_RE = re.compile(r'\s+')


def strip_tags(s: str) -> str:
    return SPACES_RE.sub(" ", TAG_RE.sub("", s)).strip()


def extract_prose(html_text: str):
    # Get title
    t_m = TITLE_RE.search(html_text)
    title = html.unescape(strip_tags(t_m.group(1))) if t_m else "?"

    # Get location/type line
    loc_m = LOC_RE.search(html_text)
    loc = html.unescape(strip_tags(loc_m.group(1))) if loc_m else "?"

    # Find prose block
    p_m = PROSE_RE.search(html_text)
    if not p_m:
        return title, loc, None
    rest = p_m.group(1)
    # Walk forward and find matching closing div for the prose block.
    # We do a balanced parse for <div>.
    depth = 1
    i = 0
    while i < len(rest):
        nxt = rest.find("<", i)
        if nxt < 0:
            break
        if rest.startswith("<div", nxt) and (rest[nxt + 4] in " >"):
            depth += 1
            i = nxt + 4
        elif rest.startswith("</div", nxt):
            depth -= 1
            i = nxt + 5
            if depth == 0:
                break
        else:
            i = nxt + 1
    prose_html = rest[: i - len("</div")] if depth == 0 else rest
    return title, loc, prose_html


def truncate_at_compensation(prose: str) -> str:
    """Cut off the prose at the first 'compensation' heading/mention.

    We look for indicators like 'Compensation' as bold text or heading,
    or 'Compensation at Skydio', 'Compensation:', etc.
    """
    if not prose:
        return prose
    # Find earliest occurrence of any case of the word inside a tag boundary.
    candidates = []
    # Find all positions of /compensation/i
    for m in re.finditer(r'compensation', prose, re.IGNORECASE):
        # Heuristic: prefer when it's inside <strong>, <b>, <h*>, or shortly preceded by a tag open.
        start = m.start()
        ctx_before = prose[max(0, start - 40):start].lower()
        if any(t in ctx_before for t in ['<strong>', '<b>', '<h1', '<h2', '<h3', '<h4', '<h5', '<h6',
                                         '<p>compensation', '<p><strong>compensation']):
            candidates.append(start)
    if candidates:
        cut = min(candidates)
    else:
        # fall back: just first occurrence
        first = prose.lower().find('compensation')
        cut = first if first >= 0 else len(prose)

    # Back up to the nearest tag start so we don't cut mid-element awkwardly.
    # Find the most recent '<' before `cut`.
    back = prose.rfind('<', 0, cut)
    # Walk back to the opening tag of the wrapping block (p, h*, ul, ol, div).
    # Simpler: search backwards for one of '<p', '<h', '<ul', '<ol', '<div'
    # and take the earliest among them.
    block_tags = ['<p', '<h1', '<h2', '<h3', '<h4', '<h5', '<h6', '<ul', '<ol', '<div', '<section']
    best = -1
    for t in block_tags:
        idx = prose.rfind(t, 0, cut)
        if idx > best:
            best = idx
    if best > 0:
        return prose[:best]
    return prose[:cut]


# --- Analysis --------------------------------------------------------------

# Patterns of interest
SECTION_HEADING_PATTERNS = [
    "about the role",
    "the role",
    "about you",
    "about the team",
    "the team",
    "what you'll do",
    "what you will do",
    "what you’ll do",
    "how you'll make an impact",
    "how you’ll make an impact",
    "your impact",
    "responsibilities",
    "key responsibilities",
    "what makes you a good fit",
    "what we're looking for",
    "what we’re looking for",
    "qualifications",
    "required qualifications",
    "preferred qualifications",
    "must have",
    "nice to have",
    "bonus points",
    "minimum qualifications",
    "preferred",
    "skills",
    "requirements",
    "about skydio",
    "why skydio",
    "benefits",
    "what we offer",
]


def get_section_headings(prose: str):
    """Return list of (tag, text, is_bold_paragraph) for visible section headers."""
    headings = []
    # h1-h6
    for m in re.finditer(r'<(h[1-6])[^>]*>(.*?)</\1>', prose, re.IGNORECASE | re.DOTALL):
        headings.append((m.group(1).lower(), strip_tags(m.group(2)).strip(), "heading"))
    # <p><strong>Heading</strong></p>  (only-strong paragraph)
    for m in re.finditer(r'<p[^>]*>\s*<(strong|b)[^>]*>(.*?)</\1>\s*:?\s*</p>',
                          prose, re.IGNORECASE | re.DOTALL):
        text = strip_tags(m.group(2)).strip(' :')
        headings.append(("p>strong", text, "bold-p"))
    # <p>X</p> where the entire content is bold
    for m in re.finditer(r'<p[^>]*><(strong|b)[^>]*>(.*?)</\1></p>',
                          prose, re.IGNORECASE | re.DOTALL):
        pass  # already covered above mostly
    return headings


def analyze_one(prose: str) -> dict:
    a = {
        "char_count": len(prose),
        "text_count": len(strip_tags(prose)),
        "n_p": len(re.findall(r'<p\b', prose, re.IGNORECASE)),
        "n_ul": len(re.findall(r'<ul\b', prose, re.IGNORECASE)),
        "n_ol": len(re.findall(r'<ol\b', prose, re.IGNORECASE)),
        "n_li": len(re.findall(r'<li\b', prose, re.IGNORECASE)),
        "n_li_with_p": len(re.findall(r'<li[^>]*>\s*<p\b', prose, re.IGNORECASE)),
        "n_strong": len(re.findall(r'<strong\b', prose, re.IGNORECASE)),
        "n_b": len(re.findall(r'<\s*b\b(?!r|ody|lockquote)', prose, re.IGNORECASE)),
        "n_em": len(re.findall(r'<em\b', prose, re.IGNORECASE)),
        "n_i_tag": len(re.findall(r'<i\s|<i>', prose, re.IGNORECASE)),
        "n_u_tag": len(re.findall(r'<u\b', prose, re.IGNORECASE)),
        "n_br": len(re.findall(r'<br\b', prose, re.IGNORECASE)),
        "n_hr": len(re.findall(r'<hr\b', prose, re.IGNORECASE)),
        "n_a": len(re.findall(r'<a\b', prose, re.IGNORECASE)),
        "n_h1": len(re.findall(r'<h1\b', prose, re.IGNORECASE)),
        "n_h2": len(re.findall(r'<h2\b', prose, re.IGNORECASE)),
        "n_h3": len(re.findall(r'<h3\b', prose, re.IGNORECASE)),
        "n_h4": len(re.findall(r'<h4\b', prose, re.IGNORECASE)),
        "n_h5": len(re.findall(r'<h5\b', prose, re.IGNORECASE)),
        "n_h6": len(re.findall(r'<h6\b', prose, re.IGNORECASE)),
        "n_blockquote": len(re.findall(r'<blockquote\b', prose, re.IGNORECASE)),
        "n_div_inline_color": len(re.findall(r'style="[^"]*color\s*:', prose, re.IGNORECASE)),
        "n_inline_font_size": len(re.findall(r'style="[^"]*font-size\s*:', prose, re.IGNORECASE)),
        "n_inline_font_weight": len(re.findall(r'style="[^"]*font-weight\s*:', prose, re.IGNORECASE)),
        "n_inline_style": len(re.findall(r'\sstyle="', prose, re.IGNORECASE)),
        "n_span": len(re.findall(r'<span\b', prose, re.IGNORECASE)),
        "n_class_attrs": len(re.findall(r'\sclass="', prose, re.IGNORECASE)),
        "n_smart_apostrophe": prose.count('’'),
        "n_straight_apostrophe": prose.count("'"),
        "n_smart_dquote": prose.count('“') + prose.count('”'),
        "n_em_dash": prose.count('—'),
        "n_en_dash": prose.count('–'),
        "n_empty_p": len(re.findall(r'<p[^>]*>\s*(?:&nbsp;|\u00a0|\s)*</p>', prose, re.IGNORECASE)),
        "n_nbsp": prose.count('&nbsp;') + prose.count('\u00a0'),
        "ends_with_colon_bold": len(re.findall(
            r'<p[^>]*>\s*<(?:strong|b)[^>]*>[^<]*:\s*</(?:strong|b)>\s*</p>',
            prose, re.IGNORECASE)),
        "ends_no_colon_bold": len(re.findall(
            r'<p[^>]*>\s*<(?:strong|b)[^>]*>[^<:]*</(?:strong|b)>\s*</p>',
            prose, re.IGNORECASE)),
    }
    a["headings"] = get_section_headings(prose)
    a["heading_tags"] = sorted({h[0] for h in a["headings"]})
    a["heading_text"] = [h[1] for h in a["headings"]]
    a["headings_via_h_tag"] = sum(1 for h in a["headings"] if h[2] == "heading")
    a["headings_via_bold_p"] = sum(1 for h in a["headings"] if h[2] == "bold-p")
    return a


def main():
    rows = []
    for f in sorted(HTML_DIR.glob("*.html")):
        with open(f, encoding="utf-8") as fh:
            html_text = fh.read()
        title, loc, prose = extract_prose(html_text)
        if not prose:
            rows.append({"id": f.stem, "title": title, "location": loc, "error": "no-prose"})
            continue
        cut = truncate_at_compensation(prose)
        analysis = analyze_one(cut)
        analysis.update({
            "id": f.stem,
            "title": html.unescape(title),
            "location": html.unescape(loc),
        })
        rows.append(analysis)
        # save trimmed prose for human inspection
        with open(OUT_DIR / f"{f.stem}.html", "w", encoding="utf-8") as out:
            out.write(cut)

    with open(OUT_DIR / "analysis.json", "w", encoding="utf-8") as out:
        json.dump(rows, out, indent=2, ensure_ascii=False)

    print(f"Wrote {len(rows)} job analyses to {OUT_DIR/'analysis.json'}")
    # Quick summary
    has_h = [r for r in rows if r.get("headings_via_h_tag", 0) > 0]
    bold_only = [r for r in rows if r.get("headings_via_bold_p", 0) > 0
                 and r.get("headings_via_h_tag", 0) == 0]
    print(f"Postings with <h*> headings used: {len(has_h)}")
    print(f"Postings using bold-paragraph pseudo-headings only: {len(bold_only)}")
    print(f"Postings with inline style attrs: "
          f"{sum(1 for r in rows if r.get('n_inline_style', 0) > 0)}")
    print(f"Postings with <hr>: {sum(1 for r in rows if r.get('n_hr', 0) > 0)}")
    print(f"Postings using <li><p>: {sum(1 for r in rows if r.get('n_li_with_p', 0) > 0)}")
    print(f"Postings with <li> (no inner <p>): "
          f"{sum(1 for r in rows if r.get('n_li', 0) > r.get('n_li_with_p', 0))}")


if __name__ == "__main__":
    main()
