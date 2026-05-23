#!/usr/bin/env python3
"""Analyze formatting of Skydio job postings (pre-Compensation content).

The Skydio careers site renders every posting inside a single
`<div class="prose block-content">` container.  All visible typography
(font sizes, weights, line-heights, colours, alignment) is driven by
CSS classes applied to the *semantic HTML tags* the recruiter inserted
in the rich-text editor — `<h1..h6>`, `<p>`, `<strong>`, `<em>`,
`<u>`, `<ul>`, `<ol>`, `<li>`, `<br>`, etc.

That means visual inconsistencies between two postings almost always
trace back to one (or more) of:

  1.  A different *tag* being used for the same logical element
      (e.g. a section heading written as `<h2>` in one posting and
      `<p><strong>...</strong></p>` in another – they render at
      different font sizes / weights / line-heights).
  2.  A different *text style* for the same kind of label
      (e.g. `<strong>Compensation:</strong>` vs.
      `<strong><em>Compensation Range</em></strong>:`).
  3.  Extra whitespace inserted as empty paragraphs / `<br>` tags
      (visible as inconsistent line-spacing).
  4.  Inconsistent casing of section labels
      ("What you'll do" vs. "What You'll Do" vs. "WHAT YOU'LL DO").

For every posting we extract the rich-text HTML, truncate it at the
first "Compensation" block (we tolerate the label being inside any
combination of `<strong>/<em>/<u>` with or without a trailing colon
and with the colon either inside or outside the formatting tags), and
then record:

  * top-level child tags (h2 vs. p, etc.)
  * exact text of every section label found, and its capitalisation
  * extra empty paragraphs / spacer blocks
  * <br> tags used as paragraph breaks (inside <p> and inside <li>)
  * italics, underline, bold-italic, all-caps headings
  * use of headings (h1..h6) anywhere in the prose
  * the intro paragraph (boilerplate check)
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup, NavigableString, Tag


JOBS_DIR = Path("/tmp/jobs")
URLS_FILE = Path("/workspace/data/job_urls.txt")
OUT_JSON = Path("/workspace/data/job_analysis.json")


# Matches the *visible text* of the Compensation label, allowing for
# "Compensation", "Compensation:" or "Compensation Range" (with optional
# trailing colon) and surrounding whitespace.
COMP_LABEL_RE = re.compile(r"^\s*compensation(\s+range)?\s*:?\s*$", re.I)
# Matches the same labels when followed inline by salary text
COMP_INLINE_RE = re.compile(r"^\s*compensation(\s+range)?\s*:?\s", re.I)


def load_jobs() -> list[tuple[str, str]]:
    out = []
    with URLS_FILE.open() as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 2:
                out.append((parts[0], parts[1]))
    return out


def looks_like_comp_label(tag: Tag) -> tuple[bool, str]:
    """Return (matches, raw_label_html) for the tag if it looks like the
    Compensation heading – either as a standalone paragraph/heading or
    as an inline `<strong>Compensation:</strong> ...` prefix at the
    start of a paragraph."""
    text = tag.get_text(" ", strip=True)
    if not text:
        return False, ""
    if COMP_LABEL_RE.match(text):
        return True, str(tag)
    if not COMP_INLINE_RE.match(text):
        return False, ""
    # inline: look at the first <strong>/<b> inside the tag – if it
    # starts the paragraph and matches the compensation pattern, treat
    # as a heading.
    first_strong = tag.find(["strong", "b"])
    if first_strong is None:
        return False, ""
    strong_text = first_strong.get_text(" ", strip=True)
    if COMP_LABEL_RE.match(strong_text + ":") or COMP_LABEL_RE.match(strong_text):
        # ensure it really is at the very start of the paragraph
        first_text = "".join(
            t for t in tag.strings
        ).lstrip()
        if first_text.lower().startswith(strong_text.lower().rstrip(":")):
            return True, str(first_strong)
    return False, ""


def classify_comp_label(label_html: str) -> str:
    """Classify how the Compensation heading was authored."""
    if not label_html:
        return "missing"
    # remove tags but keep order
    soup = BeautifulSoup(label_html, "lxml")
    txt = soup.get_text(" ", strip=True)
    tags = [t.name for t in soup.find_all(True)]
    # Normalise into a short signature
    sig = f"{'strong' if any(t in {'strong','b'} for t in tags) else 'plain'}|"
    sig += f"{'em' if any(t in {'em','i'} for t in tags) else ''}|"
    sig += f"{'u' if 'u' in tags else ''}|"
    sig += f"{'colon-in' if txt.rstrip().endswith(':') else 'colon-out'}|"
    sig += "range" if "range" in txt.lower() else "no-range"
    return sig


def parse_job(html: str) -> dict[str, Any]:
    soup = BeautifulSoup(html, "lxml")

    title_tag = soup.find("h1", class_="type-h2")
    title = title_tag.get_text(strip=True) if title_tag else ""
    title_class = title_tag.get("class", []) if title_tag else []

    location = ""
    location_class: list[str] = []
    if title_tag:
        sib = title_tag.find_next_sibling()
        if sib:
            location = sib.get_text(" ", strip=True)
            location_class = sib.get("class", [])

    prose = soup.find("div", class_="prose")
    if prose is None:
        return {"title": title, "location": location, "error": "no prose block found"}

    pre_nodes: list[Tag] = []
    comp_label_html = ""
    found_comp = False
    for child in list(prose.children):
        if isinstance(child, NavigableString):
            continue
        matched, label_html = looks_like_comp_label(child)
        if matched:
            comp_label_html = label_html
            found_comp = True
            break
        pre_nodes.append(child)

    pre_html = "".join(str(n) for n in pre_nodes)
    pre_soup = BeautifulSoup(f"<div>{pre_html}</div>", "lxml")
    pre_root = pre_soup.div

    tag_counts: Counter[str] = Counter()
    for el in pre_root.find_all(True):
        tag_counts[el.name] += 1

    top_level: list[str] = []
    for child in pre_root.children:
        if isinstance(child, NavigableString):
            continue
        top_level.append(child.name)
    top_counts = Counter(top_level)

    # Section labels: bolded short phrases ending with a colon that make
    # up an entire paragraph/heading, or that begin a paragraph.
    section_labels: list[dict[str, Any]] = []
    seen_labels = set()
    for el in pre_root.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6"]):
        # If it IS a heading tag, record its text as a label.
        if el.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            txt = el.get_text(" ", strip=True)
            if not txt:
                continue
            section_labels.append({
                "text": txt,
                "container": el.name,
                "inner_tags": sorted({c.name for c in el.find_all(True)}),
            })
            seen_labels.add(id(el))
            continue
        # Paragraphs: look for a leading <strong>/<b>
        first_child = next(
            (c for c in el.children if not (isinstance(c, NavigableString) and not c.strip())),
            None,
        )
        if not isinstance(first_child, Tag):
            continue
        if first_child.name not in {"strong", "b"} and not (
            first_child.name in {"em", "i", "u"} and first_child.find(["strong", "b"])
        ):
            continue
        # Inner-most strong text
        strong_el = first_child if first_child.name in {"strong", "b"} else first_child.find(["strong", "b"])
        if strong_el is None:
            continue
        s_txt = strong_el.get_text(" ", strip=True)
        if not s_txt or len(s_txt) > 100:
            continue
        # Determine whether it ends with a colon, and whether the paragraph
        # is "label only" (no following text)
        p_txt = el.get_text(" ", strip=True)
        label_only = (p_txt.rstrip(":") == s_txt.rstrip(":"))
        # heuristic: only treat as section label if either it's label-only,
        # or s_txt ends with ":"
        if not label_only and not s_txt.endswith(":"):
            continue
        section_labels.append({
            "text": s_txt.rstrip(":").strip(),
            "container": el.name,
            "inner_tags": sorted({c.name for c in first_child.find_all(True)} | {first_child.name}),
            "label_only_paragraph": label_only,
            "colon_inside_strong": s_txt.endswith(":"),
        })

    # Top-level heading tags used inside the prose
    headings = [(h.name, h.get_text(" ", strip=True)) for h in pre_root.find_all(re.compile(r"^h[1-6]$"))]

    # Intro paragraph
    intro_paragraph = ""
    for child in pre_root.children:
        if isinstance(child, NavigableString):
            continue
        if child.name == "p":
            intro_paragraph = child.get_text(" ", strip=True)
            break
        if child.name in {"ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6"}:
            break
    skydio_intro = intro_paragraph.lower().startswith("skydio is the leading")

    # <br> usage
    br_in_li = sum(1 for li in pre_root.find_all("li") if li.find("br"))
    li_total = len(pre_root.find_all("li"))
    br_in_p = sum(1 for p in pre_root.find_all("p") if p.find("br") and p.get_text(strip=True))
    total_br = len(pre_root.find_all("br"))

    # Empty / spacer paragraphs
    spacer_p = 0
    for p in pre_root.find_all("p"):
        inner = "".join(str(c) for c in p.children).strip()
        if (
            inner == ""
            or inner in {"<br/>", "<br>", "<br />", "&nbsp;"}
            or re.fullmatch(r"(?:<br\s*/?>|\s|&nbsp;)+", inner)
        ):
            spacer_p += 1

    italic_count = len(pre_root.find_all(["em", "i"]))
    underline_count = len(pre_root.find_all("u"))

    bold_italic = 0
    for strong in pre_root.find_all(["strong", "b"]):
        if strong.find(["em", "i"]) or (strong.parent and strong.parent.name in {"em", "i"}):
            bold_italic += 1

    # Casing
    def cap_style(s: str) -> str:
        words = re.findall(r"[A-Za-z][A-Za-z'’/&-]*", s)
        if not words:
            return "other"
        if all(w.isupper() for w in words):
            return "ALL_CAPS"
        if all(w[0].isupper() for w in words):
            return "Title_Case"
        if words[0][0].isupper():
            # other words begin lowercase or are stop words
            stop = {"a", "an", "the", "and", "or", "of", "in", "to", "for", "as", "on"}
            if all(w[0].islower() or w.lower() in stop for w in words[1:]):
                return "Sentence_case"
        return "Mixed"

    label_styles = Counter(cap_style(l["text"]) for l in section_labels)

    nested_lists = sum(1 for ul in pre_root.find_all(["ul", "ol"]) if ul.find(["ul", "ol"]))
    ordered_lists = len(pre_root.find_all("ol"))

    has_about_role = any(
        re.search(r"\babout (the )?role\b", l["text"], re.I) for l in section_labels
    )
    has_responsibilities = any(
        re.search(r"responsib|what you.?ll do|areas of responsibility", l["text"], re.I)
        for l in section_labels
    )
    has_qualifications = any(
        re.search(
            r"qualif|requirements|what (we'?re looking|you('?ll)? need|would make you|makes you|you bring)",
            l["text"],
            re.I,
        )
        for l in section_labels
    )
    has_nice_to_have = any(
        re.search(
            r"nice to have|bonus|preferred|additional desired|good to have",
            l["text"],
            re.I,
        )
        for l in section_labels
    )

    pre_text = pre_root.get_text(" ", strip=True)
    word_count = len(pre_text.split())

    # Detect non-standard intro extensions: paragraphs between the
    # Skydio intro and the first section heading.
    intro_extra_paragraphs = 0
    saw_intro = False
    for child in pre_root.children:
        if isinstance(child, NavigableString):
            continue
        if child.name == "p":
            txt = child.get_text(" ", strip=True).lower()
            if not saw_intro:
                saw_intro = True
                continue
            # paragraph after the intro but before any section label
            first_child = next(
                (c for c in child.children if not (isinstance(c, NavigableString) and not c.strip())),
                None,
            )
            if isinstance(first_child, Tag) and first_child.name in {"strong", "b"}:
                break
            if not txt:
                continue
            intro_extra_paragraphs += 1
        elif child.name in {"ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6"}:
            break

    # Compensation label classification
    comp_signature = classify_comp_label(comp_label_html)

    return {
        "title": title,
        "title_class": title_class,
        "location": location,
        "location_class": location_class,
        "found_compensation_block": found_comp,
        "compensation_label_signature": comp_signature,
        "compensation_label_html": comp_label_html[:200],
        "pre_word_count": word_count,
        "tag_counts": dict(tag_counts),
        "top_level_children": dict(top_counts),
        "section_labels": section_labels,
        "label_styles": dict(label_styles),
        "headings": headings,
        "intro_paragraph_preview": intro_paragraph[:160],
        "intro_is_skydio_boilerplate": skydio_intro,
        "intro_extra_paragraphs": intro_extra_paragraphs,
        "br_in_li_count": br_in_li,
        "br_in_p_count": br_in_p,
        "total_br_count": total_br,
        "li_total": li_total,
        "spacer_p_count": spacer_p,
        "italic_count": italic_count,
        "underline_count": underline_count,
        "bold_italic_count": bold_italic,
        "nested_lists": nested_lists,
        "ordered_lists": ordered_lists,
        "inline_headings_count": len(headings),
        "has_about_role": has_about_role,
        "has_responsibilities": has_responsibilities,
        "has_qualifications": has_qualifications,
        "has_nice_to_have": has_nice_to_have,
    }


def main() -> None:
    results: dict[str, Any] = {}
    for job_id, url in load_jobs():
        path = JOBS_DIR / f"{job_id}.html"
        if not path.exists():
            print(f"missing html for {job_id}", file=sys.stderr)
            continue
        html = path.read_text(errors="replace")
        try:
            info = parse_job(html)
        except Exception as e:  # noqa: BLE001
            info = {"error": f"{type(e).__name__}: {e}"}
        info["job_id"] = job_id
        info["url"] = url
        results[job_id] = info

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(results, indent=2, default=str))
    print(f"wrote {OUT_JSON} ({len(results)} jobs)")


if __name__ == "__main__":
    main()
