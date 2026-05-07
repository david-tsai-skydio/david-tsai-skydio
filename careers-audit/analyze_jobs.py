#!/usr/bin/env python3
"""Analyze formatting consistency of Skydio job postings (pre-compensation only)."""
import os
import re
import json
import glob
import html
from collections import Counter, defaultdict

JOBS_DIR = os.environ.get("SKYDIO_JOBS_DIR", "/tmp/skydio_jobs")
OUT_JSON = os.environ.get("SKYDIO_ANALYSIS_OUT", "/tmp/analysis.json")

# Compensation cut-off markers (case-insensitive). We stop at the first one we see.
COMPENSATION_MARKERS = [
    r"\bcompensation\b\s*[:.]?",
    r"compensation\s*range",
    r"compensation\s*&\s*benefits",
    r"compensation\s*and\s*benefits",
    r"salary\s*range",
    r"pay\s*range",
    r"base\s*salary",
    r"the\s*annual\s*base\s*salary\s*range",
]
COMP_RE = re.compile("|".join(COMPENSATION_MARKERS), re.I)


def extract_job_post(html_text: str) -> str:
    m = re.search(
        r'<skydio-module class="[^"]*job-post[^"]*"[^>]*>(.*?)</skydio-module>',
        html_text,
        re.S,
    )
    return m.group(1) if m else ""


def split_title_loc_body(jp_html: str):
    title_m = re.search(r'<h1[^>]*class="[^"]*"[^>]*>(.*?)</h1>', jp_html, re.S)
    title = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", title_m.group(1)))).strip() if title_m else ""

    loc_m = re.search(r'<p class="type-body-2">(.*?)</p>', jp_html, re.S)
    loc = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", loc_m.group(1)))).strip() if loc_m else ""

    body_m = re.search(r'<div class="prose block-content">(.*?)</div>\s*</stack-l>', jp_html, re.S)
    body = body_m.group(1) if body_m else ""

    return title, loc, body


def truncate_at_compensation(body_html: str) -> str:
    """Return only the body up to (and not including) the compensation block.

    The body in these postings uses one of the following section-heading patterns:
        <p><strong>Compensation:</strong></p>
        <p><strong>Compensation:</strong> ... (inline)</p>
        <h2><strong>Compensation</strong></h2>
        <ul><li><p><strong>Compensation:</strong> ...</p></li>...</ul>
        <p><strong>Compensation:</strong></p><ul><li><p>At Skydio, our compensation packages...</p></li></ul>

    The very first <strong>...Compensation...</strong> token within a block-level element
    is treated as the section boundary. We then walk backwards to the most recent
    block-level opening tag so that we don't leave dangling fragments.
    """
    # Match a <strong> (or <b>) whose visible text starts with "Compensation"
    # (allowing a trailing colon, dash, or whitespace).
    strong_pat = re.compile(
        r"<(?:strong|b)[^>]*>\s*compensation[\s:&\-—]*(?:</(?:strong|b)>|<)",
        re.I,
    )
    m = strong_pat.search(body_html)
    if not m:
        return body_html

    # Walk back to the start of the containing block-level element so we cut cleanly.
    idx = m.start()
    upto = body_html[:idx]
    block_starts = []
    for tag in ("<p>", "<p ", "<ul>", "<ul ", "<ol>", "<ol ", "<li>", "<li ",
                "<h1", "<h2", "<h3", "<h4", "<h5", "<h6"):
        i = upto.rfind(tag)
        if i != -1:
            block_starts.append(i)
    if not block_starts:
        return body_html[:idx]
    cut = max(block_starts)

    # If the cut lands inside a list item, walk further back to the start of <ul>/<ol>
    # so we don't leave open list tags.
    tail = body_html[cut:idx]
    if "<li" in tail and "<ul" not in tail and "<ol" not in tail:
        list_starts = [upto.rfind("<ul>"), upto.rfind("<ul "),
                       upto.rfind("<ol>"), upto.rfind("<ol ")]
        list_starts = [x for x in list_starts if x != -1]
        if list_starts:
            cut = max(list_starts)

    return body_html[:cut]


# --- Feature extraction -----------------------------------------------------

INTRO_PHRASE = "Skydio is the leading US drone company"
INTRO_PHRASE_2 = "Skydio is the leading U.S. drone company"


def features(body_html: str) -> dict:
    f = {}
    text_only = re.sub(r"<[^>]+>", " ", body_html)
    text_only = html.unescape(re.sub(r"\s+", " ", text_only)).strip()
    f["char_len"] = len(text_only)
    f["word_count"] = len(text_only.split())

    # Element counts
    f["count_p"] = len(re.findall(r"<p[\s>]", body_html))
    f["count_p_empty"] = len(re.findall(r"<p>\s*</p>|<p>\s*<br\s*/?>\s*</p>", body_html))
    f["count_strong"] = len(re.findall(r"<strong[\s>]", body_html))
    f["count_b"] = len(re.findall(r"<b[\s>]", body_html))
    f["count_em"] = len(re.findall(r"<em[\s>]", body_html))
    f["count_i"] = len(re.findall(r"<i[\s>]", body_html))
    f["count_u"] = len(re.findall(r"<u[\s>]", body_html))
    f["count_h1"] = len(re.findall(r"<h1[\s>]", body_html))
    f["count_h2"] = len(re.findall(r"<h2[\s>]", body_html))
    f["count_h3"] = len(re.findall(r"<h3[\s>]", body_html))
    f["count_h4"] = len(re.findall(r"<h4[\s>]", body_html))
    f["count_h5"] = len(re.findall(r"<h5[\s>]", body_html))
    f["count_h6"] = len(re.findall(r"<h6[\s>]", body_html))
    f["count_ul"] = len(re.findall(r"<ul[\s>]", body_html))
    f["count_ol"] = len(re.findall(r"<ol[\s>]", body_html))
    f["count_li"] = len(re.findall(r"<li[\s>]", body_html))
    f["count_br"] = len(re.findall(r"<br\s*/?>", body_html))
    f["count_inline_style"] = len(re.findall(r'style="[^"]+"', body_html))
    f["count_font_face"] = len(re.findall(r"font-family", body_html, re.I))
    f["count_font_size"] = len(re.findall(r"font-size", body_html, re.I))
    f["count_color"] = len(re.findall(r"color\s*:", body_html, re.I))
    f["count_class_attr"] = len(re.findall(r' class="', body_html))
    f["count_div"] = len(re.findall(r"<div[\s>]", body_html))
    f["count_span"] = len(re.findall(r"<span[\s>]", body_html))
    f["count_table"] = len(re.findall(r"<table[\s>]", body_html))

    # Bullet style: <li><p>...</p></li> vs <li>...</li>
    f["count_li_p"] = len(re.findall(r"<li>\s*<p>", body_html))
    f["count_li_no_p"] = len(re.findall(r"<li>(?!\s*<p>)", body_html))

    # All-caps usage in strong
    strong_text = [
        re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()
        for s in re.findall(r"<strong[^>]*>(.*?)</strong>", body_html, re.S)
    ]
    f["strong_phrases"] = strong_text
    f["count_strong_allcaps"] = sum(
        1 for s in strong_text if s and s.upper() == s and any(c.isalpha() for c in s)
    )

    # Trailing colon on bold "headings" (those that are the only content of a <p>)
    section_headings = re.findall(
        r"<p>\s*<strong>(.*?)</strong>\s*</p>", body_html, re.S
    )
    section_headings = [
        re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", "", s))).strip()
        for s in section_headings
    ]
    section_headings = [s for s in section_headings if s]
    f["section_headings"] = section_headings
    f["count_section_headings"] = len(section_headings)
    f["count_section_with_colon"] = sum(1 for s in section_headings if s.endswith(":"))
    f["count_section_no_colon"] = sum(1 for s in section_headings if not s.endswith(":"))

    # Has the standard Skydio intro paragraph?
    f["has_skydio_intro"] = (
        INTRO_PHRASE in text_only or INTRO_PHRASE_2 in text_only
    )

    # Detect "About the role" header presence and exact wording
    about_role = None
    for s in section_headings:
        if re.search(r"about\s+the\s+role", s, re.I):
            about_role = s
            break
    f["about_role_heading"] = about_role

    # Italic-emphasized paragraphs
    f["count_em_strong_combo"] = len(re.findall(r"<em>\s*<strong>", body_html))

    # Internal whitespace anomalies
    f["count_double_space"] = len(re.findall(r"  +", text_only))
    f["count_trailing_br_in_p"] = len(re.findall(r"<br\s*/?>\s*</p>", body_html))
    f["count_trailing_br_in_li_p"] = len(re.findall(r"<br\s*/?>\s*</p>\s*</li>", body_html))

    # Hashtags / signoffs (LI tags etc.)
    f["count_hash_signoff"] = len(re.findall(r"#LI-[A-Za-z0-9]+", body_html))

    # Emoji presence
    f["has_emoji"] = bool(re.search(r"[\U0001F300-\U0001FAFF\u2600-\u27BF]", body_html))

    # Curly quotes
    f["count_curly_quotes"] = len(re.findall(r"[\u2018\u2019\u201C\u201D]", text_only))
    f["count_straight_quotes"] = len(re.findall(r"[\"']", text_only))

    return f


def main():
    rows = []
    for path in sorted(glob.glob(os.path.join(JOBS_DIR, "*.html"))):
        job_id = os.path.splitext(os.path.basename(path))[0]
        with open(path, encoding="utf-8") as fp:
            txt = fp.read()
        jp = extract_job_post(txt)
        if not jp:
            continue
        title, loc, body = split_title_loc_body(jp)
        pre_comp = truncate_at_compensation(body)
        feats = features(pre_comp)
        rows.append({
            "id": job_id,
            "title": title,
            "location": loc,
            "features": feats,
        })

    with open(OUT_JSON, "w") as fp:
        json.dump(rows, fp, indent=2, default=str)

    # ---- Aggregate ---------------------------------------------------------
    print(f"Analyzed {len(rows)} job postings.\n")

    # Section heading patterns
    heading_counter = Counter()
    headings_by_job = {}
    for r in rows:
        for h in r["features"]["section_headings"]:
            heading_counter[h] += 1
        headings_by_job[r["id"]] = r["features"]["section_headings"]

    print("=== Top 30 section headings (verbatim) ===")
    for h, c in heading_counter.most_common(30):
        print(f"  {c:3d}  {h!r}")

    # Count colon vs no colon
    total_h = sum(r["features"]["count_section_headings"] for r in rows)
    total_c = sum(r["features"]["count_section_with_colon"] for r in rows)
    print(f"\nSection-style bold headings: {total_h} total, {total_c} end with ':' "
          f"({total_c / max(1,total_h):.0%}), {total_h - total_c} do not.")

    # Jobs with no Skydio intro paragraph
    no_intro = [r for r in rows if not r["features"]["has_skydio_intro"]]
    print(f"\nJobs WITHOUT the standard 'Skydio is the leading US drone company' intro: {len(no_intro)}")
    for r in no_intro[:30]:
        print(f"  - {r['title']}")

    # H1/H2/H3 inside body (should be zero)
    using_h_tags = [
        r for r in rows
        if any(r["features"][k] > 0 for k in ("count_h1","count_h2","count_h3","count_h4","count_h5","count_h6"))
    ]
    print(f"\nJobs using <h1>-<h6> inside body: {len(using_h_tags)}")
    for r in using_h_tags:
        f = r["features"]
        sig = ",".join(f"{k.replace('count_','')}={f[k]}" for k in ("count_h1","count_h2","count_h3","count_h4","count_h5","count_h6") if f[k])
        print(f"  - {r['title']}: {sig}")

    # Use of <b> instead of <strong>
    using_b = [r for r in rows if r["features"]["count_b"] > 0]
    print(f"\nJobs using <b> tag: {len(using_b)}")
    for r in using_b:
        print(f"  - {r['title']}: {r['features']['count_b']}")

    # Inline styles / fonts / colors / sizes
    inline = [r for r in rows if r["features"]["count_inline_style"] > 0]
    print(f"\nJobs with inline style attributes in body: {len(inline)}")
    for r in inline[:20]:
        print(f"  - {r['title']}: count_inline_style={r['features']['count_inline_style']}")

    fonts = [r for r in rows if r["features"]["count_font_face"] or r["features"]["count_font_size"]]
    print(f"\nJobs with font-family/font-size declarations: {len(fonts)}")
    for r in fonts:
        print(f"  - {r['title']}")

    colors = [r for r in rows if r["features"]["count_color"] > 0]
    print(f"\nJobs with explicit color declarations: {len(colors)}")
    for r in colors:
        print(f"  - {r['title']}")

    # Bullet sub-style (<li><p>)
    li_with_p = sum(1 for r in rows if r["features"]["count_li_p"] > 0)
    li_without_p = sum(1 for r in rows if r["features"]["count_li_no_p"] > 0 and r["features"]["count_li_p"] == 0)
    li_mixed = sum(1 for r in rows if r["features"]["count_li_p"] > 0 and r["features"]["count_li_no_p"] > 0)
    print(f"\nList item style:\n  uses <li><p> exclusively: {li_with_p - li_mixed}\n  uses bare <li> exclusively: {li_without_p}\n  mixed within same posting: {li_mixed}")
    print("  (mixed jobs):")
    for r in rows:
        if r["features"]["count_li_p"] > 0 and r["features"]["count_li_no_p"] > 0:
            print(f"    - {r['title']}: <li><p>={r['features']['count_li_p']}, bare <li>={r['features']['count_li_no_p']}")

    # Trailing <br> inside <p>
    br_in_p = [r for r in rows if r["features"]["count_trailing_br_in_p"] > 0]
    print(f"\nJobs with trailing <br> inside <p> (creates inconsistent vertical rhythm): {len(br_in_p)}")
    for r in br_in_p[:30]:
        print(f"  - {r['title']}: {r['features']['count_trailing_br_in_p']}")

    # Empty paragraphs
    empty = [r for r in rows if r["features"]["count_p_empty"] > 0]
    print(f"\nJobs with empty <p></p> filler paragraphs: {len(empty)}")
    for r in empty[:30]:
        print(f"  - {r['title']}: {r['features']['count_p_empty']}")

    # All-caps strong
    allcaps = [r for r in rows if r["features"]["count_strong_allcaps"] > 0]
    print(f"\nJobs using ALL-CAPS bolded headings: {len(allcaps)}")
    for r in allcaps:
        cs = [s for s in r["features"]["strong_phrases"] if s and s.upper() == s and any(c.isalpha() for c in s)]
        print(f"  - {r['title']}: {cs}")

    # Length outliers
    lens = [r["features"]["word_count"] for r in rows]
    avg = sum(lens) / len(lens)
    print(f"\nWord-count stats (pre-compensation): min={min(lens)}, max={max(lens)}, avg={avg:.0f}")
    short = sorted(rows, key=lambda r: r["features"]["word_count"])[:5]
    long = sorted(rows, key=lambda r: -r["features"]["word_count"])[:5]
    print("  shortest 5:")
    for r in short:
        print(f"    {r['features']['word_count']:5d}  {r['title']}")
    print("  longest 5:")
    for r in long:
        print(f"    {r['features']['word_count']:5d}  {r['title']}")

    # Postings whose title-level "About the role" wording differs
    about = Counter(r["features"]["about_role_heading"] for r in rows)
    print(f"\n'About the role' heading wording variants:")
    for k, v in about.most_common():
        print(f"  {v:3d}  {k!r}")

    # Postings missing "About the role" heading
    missing_about = [r for r in rows if not r["features"]["about_role_heading"]]
    print(f"\nJobs missing 'About the role' bold heading: {len(missing_about)}")
    for r in missing_about[:30]:
        print(f"  - {r['title']} :: section headings = {r['features']['section_headings']}")

    # Hash signoff variations
    sig = Counter()
    for r in rows:
        if r["features"]["count_hash_signoff"]:
            sig["has signoff"] += 1
        else:
            sig["missing signoff"] += 1
    print(f"\n#LI-* signoffs: {dict(sig)}")

    # Curly vs straight quotes
    curly = sum(r["features"]["count_curly_quotes"] for r in rows)
    straight = sum(r["features"]["count_straight_quotes"] for r in rows)
    print(f"\nCurly quotes: {curly}, Straight quotes: {straight}")

    return rows


if __name__ == "__main__":
    rows = main()
