"""Analyze the pre-compensation content of every Skydio job posting and
record formatting characteristics so we can spot inconsistencies.

For each job we capture:
  * pre-comp HTML length / text length
  * heading levels used (real <h1>-<h6>)
  * section labels (paragraphs whose visible text starts with a bold
    sentence ending in ':') and how they were marked up
  * count of paragraphs, lists, list items, line breaks
  * use of <strong>/<b>/<em>/<i>/<u>
  * any inline `style=` attributes
  * any class attributes other than the bare-minimum 'prose'/'block-content'
  * use of <br>, <hr>, <a>, images, tables, blockquotes
  * use of nested lists or numbered (<ol>) lists
  * stray characters: non-breaking spaces, smart quotes, em-dashes, etc.
  * sequence of block-level tag names (the "shape" of the posting)
"""

from __future__ import annotations

import json
import re
import unicodedata
from collections import Counter
from pathlib import Path

from bs4 import BeautifulSoup, NavigableString, Tag

INDEX = Path("/workspace/report/jobs_index.json")
PAGES_DIR = Path("/workspace/job_pages")
OUT = Path("/workspace/report/jobs_formatting.json")


def split_pre_compensation(prose: Tag) -> list[Tag]:
    """Return the list of direct children of <div class="prose"> that appear
    before (and not including) the paragraph whose visible text begins with
    'Compensation'."""
    kept: list[Tag] = []
    for child in prose.children:
        if isinstance(child, NavigableString):
            continue
        if not isinstance(child, Tag):
            continue
        # If this element's text starts with "Compensation" (case-insensitive,
        # possibly preceded by whitespace), stop.
        text = child.get_text(" ", strip=True)
        if re.match(r"^\s*Compensation\s*:", text, flags=re.IGNORECASE):
            break
        kept.append(child)
    return kept


def is_section_label_paragraph(p: Tag) -> tuple[bool, str | None]:
    """A 'section label' in these postings is typically a <p> whose entire
    visible text is bold and ends with ':' (e.g. 'About the role:')."""
    if p.name != "p":
        return False, None
    text = p.get_text(" ", strip=True)
    if not text or len(text) > 120:
        return False, None
    if not text.endswith(":"):
        return False, None
    # Is the whole paragraph effectively a bold span?
    children = [c for c in p.children if not (isinstance(c, NavigableString) and not c.strip())]
    if len(children) == 1 and isinstance(children[0], Tag) and children[0].name in {"strong", "b"}:
        inner = children[0].get_text(" ", strip=True)
        if inner == text:
            return True, text
    # Or text wrapped in <strong> plus a trailing space (still acceptable)
    strong = p.find(["strong", "b"])
    if strong and strong.get_text(" ", strip=True).rstrip(":") == text.rstrip(":"):
        return True, text
    return False, None


def classify_section_label_markup(p: Tag) -> str:
    """Return a short description of HOW the section label is marked up."""
    children = [c for c in p.children if not (isinstance(c, NavigableString) and not c.strip())]
    parts = []
    for c in children:
        if isinstance(c, NavigableString):
            parts.append("text")
        else:
            parts.append(c.name)
    return "p>" + ",".join(parts)


def analyze_one(prose: Tag) -> dict:
    pre = split_pre_compensation(prose)

    container = BeautifulSoup("<div></div>", "lxml").div
    for el in pre:
        container.append(el.__copy__())

    html = "".join(str(e) for e in pre)
    text = " ".join(e.get_text(" ", strip=True) for e in pre)

    # --- top-level block tag sequence ---
    block_tag_seq = [e.name for e in pre]
    block_tag_counts = dict(Counter(block_tag_seq))

    # --- headings actually used ---
    heading_levels: list[str] = []
    for e in pre:
        for h in e.find_all(re.compile(r"^h[1-6]$")):
            heading_levels.append(h.name)
        if re.match(r"^h[1-6]$", e.name or ""):
            heading_levels.append(e.name)
    heading_counts = dict(Counter(heading_levels))

    # --- section labels ---
    section_labels: list[dict] = []
    for e in pre:
        candidates: list[Tag] = []
        if e.name == "p":
            candidates.append(e)
        else:
            candidates.extend(e.find_all("p"))
        for p in candidates:
            ok, label = is_section_label_paragraph(p)
            if ok:
                section_labels.append({
                    "label": label,
                    "markup": classify_section_label_markup(p),
                })
        # Also count real headings as section labels
        for h in (e.find_all(re.compile(r"^h[1-6]$")) if isinstance(e, Tag) else []):
            section_labels.append({
                "label": h.get_text(" ", strip=True),
                "markup": h.name,
            })
        if re.match(r"^h[1-6]$", e.name or ""):
            section_labels.append({
                "label": e.get_text(" ", strip=True),
                "markup": e.name,
            })

    # --- counts of structural elements ---
    counts = {
        "paragraphs": 0,
        "ul": 0,
        "ol": 0,
        "li": 0,
        "nested_lists": 0,
        "br": 0,
        "hr": 0,
        "anchors": 0,
        "images": 0,
        "tables": 0,
        "blockquotes": 0,
        "strong": 0,
        "b": 0,
        "em": 0,
        "i": 0,
        "u": 0,
        "span_with_style": 0,
        "elements_with_style": 0,
        "elements_with_class": 0,
        "empty_paragraphs": 0,
        "non_breaking_space": text.count("\u00a0"),
    }
    for e in pre:
        for el in e.find_all(True) if isinstance(e, Tag) else []:
            n = el.name
            if n in counts:
                counts[n] = counts[n] + 1 if n in counts and isinstance(counts[n], int) else 1
            if n == "ul":
                counts["ul"] += 1
            if n == "ol":
                counts["ol"] += 1
            if n == "li":
                counts["li"] += 1
            if n == "p":
                counts["paragraphs"] += 1
                if not el.get_text(strip=True):
                    counts["empty_paragraphs"] += 1
            if n == "br":
                counts["br"] += 1
            if n == "hr":
                counts["hr"] += 1
            if n == "a":
                counts["anchors"] += 1
            if n == "img":
                counts["images"] += 1
            if n == "table":
                counts["tables"] += 1
            if n == "blockquote":
                counts["blockquotes"] += 1
            if n == "strong":
                counts["strong"] += 1
            if n == "b":
                counts["b"] += 1
            if n == "em":
                counts["em"] += 1
            if n == "i":
                counts["i"] += 1
            if n == "u":
                counts["u"] += 1
            if n == "span" and el.has_attr("style"):
                counts["span_with_style"] += 1
            if el.has_attr("style"):
                counts["elements_with_style"] += 1
            if el.has_attr("class"):
                counts["elements_with_class"] += 1
            if n in {"ul", "ol"}:
                if el.find(["ul", "ol"]):
                    counts["nested_lists"] += 1
        # also count the top-level element itself
        if e.name == "p":
            counts["paragraphs"] += 1
            if not e.get_text(strip=True):
                counts["empty_paragraphs"] += 1
        if e.name == "ul":
            counts["ul"] += 1
        if e.name == "ol":
            counts["ol"] += 1
        if e.name in {"strong", "b", "em", "i", "u"}:
            counts[e.name] += 1

    # --- styles & classes ---
    inline_styles = []
    custom_classes = []
    for e in pre:
        for el in e.find_all(True) if isinstance(e, Tag) else []:
            if el.has_attr("style"):
                inline_styles.append({"tag": el.name, "style": el["style"]})
            if el.has_attr("class"):
                cls = " ".join(el["class"])
                if cls.strip():
                    custom_classes.append({"tag": el.name, "class": cls})

    # --- characters of interest ---
    char_features = {
        "smart_quotes": sum(text.count(c) for c in ["\u2018", "\u2019", "\u201c", "\u201d"]),
        "em_dashes": text.count("\u2014"),
        "en_dashes": text.count("\u2013"),
        "ellipsis_char": text.count("\u2026"),
        "non_ascii_chars": sum(1 for ch in text if ord(ch) > 127),
    }

    # --- bullet list label vs sentence-style item ---
    # Skim list items: do they end with punctuation? Are some <strong>?
    li_features = {
        "items_total": 0,
        "items_with_trailing_period": 0,
        "items_with_leading_strong": 0,
        "items_with_only_strong": 0,
        "items_empty": 0,
        "items_with_nested_list": 0,
    }
    for e in pre:
        for li in (e.find_all("li") if isinstance(e, Tag) else []):
            li_features["items_total"] += 1
            li_text = li.get_text(" ", strip=True)
            if not li_text:
                li_features["items_empty"] += 1
                continue
            if li_text.endswith("."):
                li_features["items_with_trailing_period"] += 1
            first = li.find(["strong", "b"])
            if first and li_text.startswith(first.get_text(" ", strip=True)):
                li_features["items_with_leading_strong"] += 1
                if first.get_text(" ", strip=True) == li_text:
                    li_features["items_with_only_strong"] += 1
            if li.find(["ul", "ol"]):
                li_features["items_with_nested_list"] += 1

    return {
        "html_len": len(html),
        "text_len": len(text),
        "block_tag_sequence": block_tag_seq,
        "block_tag_counts": block_tag_counts,
        "heading_counts": heading_counts,
        "section_labels": section_labels,
        "counts": counts,
        "inline_styles": inline_styles,
        "custom_classes": custom_classes,
        "char_features": char_features,
        "list_item_features": li_features,
    }


def main() -> None:
    jobs = json.loads(INDEX.read_text())
    results = []
    for j in jobs:
        path = PAGES_DIR / f"{j['job_id']}.html"
        if not path.exists():
            continue
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "lxml")
        prose = soup.find("div", class_="prose")
        if prose is None:
            print(f"WARN no prose for {j['title']}")
            continue
        analysis = analyze_one(prose)
        results.append({
            **j,
            "analysis": analysis,
        })

    OUT.write_text(json.dumps(results, indent=2))
    print(f"Analyzed {len(results)} jobs -> {OUT}")


if __name__ == "__main__":
    main()
