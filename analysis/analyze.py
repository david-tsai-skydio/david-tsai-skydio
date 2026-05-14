#!/usr/bin/env python3
"""Analyze formatting consistency across Skydio job postings.

For each posting we:
  1. Pull the job title and location chip.
  2. Extract the <div class="prose block-content"> body.
  3. Truncate at the first "Compensation" / "compensation" heading.
  4. Inspect the surviving HTML for formatting signals (heading tags used,
     inline styles, emphasis patterns, list structures, section-heading
     patterns, font/color overrides, etc.).
"""
from __future__ import annotations

import json
import os
import re
from collections import Counter, defaultdict
from glob import glob

from bs4 import BeautifulSoup, NavigableString, Tag

JOB_DIR = os.path.join(os.path.dirname(__file__), "jobs")

COMP_MARKERS = re.compile(
    r"^\s*(compensation(?:\s+range)?|pay\s*range|salary(?:\s*range)?|"
    r"base\s*pay(?:\s*range)?|at\s+skydio,?\s+our\s+compensation)\b",
    re.IGNORECASE,
)


def find_compensation_node(prose: Tag) -> Tag | None:
    """Return the first descendant whose text starts the compensation block.

    Two common forms in Skydio postings:
      1. <p><strong>Compensation:</strong></p> followed by detail paragraphs.
      2. <p><strong>Compensation:</strong> At Skydio, our compensation ... </p>
         — a single long paragraph that *starts* with the heading.
    """
    for el in prose.find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "div"]):
        txt = el.get_text(" ", strip=True)
        if not txt:
            continue
        if COMP_MARKERS.match(txt):
            # Heading-like usage: the paragraph either is short, or begins with
            # a bolded label such as "Compensation:" / "Salary Range:" /
            # "Pay Range:" before the body text.
            stripped_short = txt[:200].strip()
            looks_label = bool(
                re.match(
                    r"^(compensation(?:\s+range)?|pay\s*range|salary(?:\s*range)?|"
                    r"base\s*pay(?:\s*range)?)\s*:",
                    stripped_short,
                    re.IGNORECASE,
                )
            )
            looks_boilerplate = stripped_short.lower().startswith(
                "at skydio, our compensation"
            ) or stripped_short.lower().startswith(
                "at skydio our compensation"
            )
            if looks_label or looks_boilerplate or len(txt) < 200:
                return el
    return None


def truncate_before(prose: Tag, marker: Tag) -> Tag:
    """Return a copy of prose with all content from marker onward removed."""
    soup = BeautifulSoup(str(prose), "lxml")
    new_prose = soup.find("div", class_="prose") or soup
    # Walk children top-level - if marker is a child, drop from there
    target_text = marker.get_text(" ", strip=True)
    children = list(new_prose.children)
    found = False
    for c in children:
        if isinstance(c, Tag):
            if c.get_text(" ", strip=True) == target_text or COMP_MARKERS.match(
                c.get_text(" ", strip=True) or ""
            ):
                found = True
            if found:
                c.decompose()
    return new_prose


def get_title_and_meta(soup: BeautifulSoup) -> tuple[str, str]:
    h = soup.find("h1", class_=re.compile("type-h2"))
    if not h:
        h = soup.find("h1")
    title = h.get_text(strip=True) if h else ""
    # Location/employment chip <p class="type-body-2"> right after h1.
    meta = ""
    if h:
        sib = h.find_next_sibling()
        if sib and sib.name == "p":
            meta = sib.get_text(" ", strip=True)
    return title, meta


def looks_like_section_heading(p: Tag) -> bool:
    """Heuristic: a <p> is acting as a section heading if its only meaningful
    contents are wrapped in <strong>/<b>, the text ends with ':' or is short,
    and isn't part of a list item."""
    if p.parent and p.parent.name in {"li"}:
        return False
    text = p.get_text(" ", strip=True)
    if not text or len(text) > 120:
        return False
    # Strip leading bullets if any.
    children = [c for c in p.children if not (isinstance(c, NavigableString) and not c.strip())]
    if not children:
        return False
    # Whole text must be inside a single strong/b (allowing nested em/u).
    if all(isinstance(c, Tag) and c.name in {"strong", "b"} for c in children):
        return True
    # Also allow <p><strong>... :</strong> trailing whitespace</p>
    if len(children) == 1 and isinstance(children[0], Tag) and children[0].name in {"strong", "b"}:
        return True
    # A <p> whose text fully matches its <strong> descendant text.
    strongs = p.find_all(["strong", "b"])
    if strongs:
        strong_text = " ".join(s.get_text(" ", strip=True) for s in strongs).strip()
        if strong_text == text:
            return True
    return False


def style_signature(prose: Tag) -> dict:
    """Collect structural / formatting signals about the prose region."""
    tag_counts: Counter[str] = Counter()
    inline_styles: list[str] = []
    inline_style_tags: Counter[str] = Counter()
    font_tags = 0
    span_with_style = 0
    headings_used: Counter[str] = Counter()
    heading_text_samples: dict[str, list[str]] = defaultdict(list)
    section_headings: list[str] = []
    section_heading_uses_colon = 0
    section_heading_all_caps = 0
    section_heading_title_case = 0
    bold_inside_li = 0
    italic_inside_li = 0
    underline_inside_li = 0
    nested_p_in_li = 0
    plain_text_li = 0
    ul_count = 0
    ol_count = 0
    bullet_glyph_lines = 0
    br_count = 0
    nbsp_count = 0
    em_dash_uses = 0
    en_dash_uses = 0
    has_horizontal_rule = False
    quirky_quotes = 0
    h_levels_in_body: Counter[str] = Counter()
    explicit_color = 0
    explicit_font_size = 0
    explicit_font_family = 0
    explicit_line_height = 0
    explicit_alignment = 0
    classes_seen: Counter[str] = Counter()
    list_after_heading_pattern: Counter[str] = Counter()

    body_text = prose.get_text("\n")
    nbsp_count = body_text.count("\u00a0")
    em_dash_uses = body_text.count("—")
    en_dash_uses = body_text.count("–")
    quirky_quotes = sum(body_text.count(ch) for ch in ("“", "”", "‘", "’"))

    for tag in prose.find_all(True):
        tag_counts[tag.name] += 1
        if tag.has_attr("style"):
            style = tag["style"]
            inline_styles.append(style)
            inline_style_tags[tag.name] += 1
            lower = style.lower()
            if "color" in lower:
                explicit_color += 1
            if "font-size" in lower:
                explicit_font_size += 1
            if "font-family" in lower:
                explicit_font_family += 1
            if "line-height" in lower:
                explicit_line_height += 1
            if "text-align" in lower or "align" in lower:
                explicit_alignment += 1
        if tag.has_attr("class"):
            for c in tag["class"]:
                classes_seen[c] += 1
        if tag.name == "font":
            font_tags += 1
        if tag.name == "span" and tag.has_attr("style"):
            span_with_style += 1
        if tag.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            headings_used[tag.name] += 1
            heading_text_samples[tag.name].append(tag.get_text(" ", strip=True))
            h_levels_in_body[tag.name] += 1
        if tag.name == "hr":
            has_horizontal_rule = True
        if tag.name == "ul":
            ul_count += 1
        if tag.name == "ol":
            ol_count += 1
        if tag.name == "br":
            br_count += 1
        if tag.name == "li":
            sub_p = tag.find_all("p", recursive=False)
            if sub_p:
                nested_p_in_li += 1
            else:
                plain_text_li += 1
            if tag.find(["strong", "b"]):
                bold_inside_li += 1
            if tag.find(["em", "i"]):
                italic_inside_li += 1
            if tag.find("u"):
                underline_inside_li += 1
        if tag.name == "p":
            txt = tag.get_text(" ", strip=True)
            if txt.startswith(("•", "●", "○", "·", "-", "*")) and len(txt) < 200:
                bullet_glyph_lines += 1
            if looks_like_section_heading(tag):
                clean = txt.strip()
                section_headings.append(clean)
                if clean.endswith(":"):
                    section_heading_uses_colon += 1
                bare = clean.rstrip(":").strip()
                if bare and bare == bare.upper():
                    section_heading_all_caps += 1
                elif bare and bare[:1].isupper() and bare not in {bare.lower(), bare.upper()}:
                    section_heading_title_case += 1
                # Look at next sibling pattern.
                nxt = tag.find_next_sibling()
                if isinstance(nxt, Tag):
                    list_after_heading_pattern[nxt.name] += 1

    # Section-heading style breakdown: does <strong>/<h*>/<u> get used?
    bold_section_headings = len(section_headings)
    real_heading_sections = sum(headings_used[h] for h in headings_used)

    return {
        "tag_counts": tag_counts,
        "inline_style_count": len(inline_styles),
        "inline_style_tag_breakdown": inline_style_tags,
        "font_tags": font_tags,
        "span_with_style": span_with_style,
        "headings_used": dict(headings_used),
        "heading_text_samples": {k: v[:5] for k, v in heading_text_samples.items()},
        "section_headings": section_headings,
        "bold_section_headings": bold_section_headings,
        "real_heading_sections": real_heading_sections,
        "section_heading_uses_colon": section_heading_uses_colon,
        "section_heading_all_caps": section_heading_all_caps,
        "section_heading_title_case": section_heading_title_case,
        "bold_inside_li": bold_inside_li,
        "italic_inside_li": italic_inside_li,
        "underline_inside_li": underline_inside_li,
        "nested_p_in_li": nested_p_in_li,
        "plain_text_li": plain_text_li,
        "ul_count": ul_count,
        "ol_count": ol_count,
        "br_count": br_count,
        "nbsp_count": nbsp_count,
        "em_dash_uses": em_dash_uses,
        "en_dash_uses": en_dash_uses,
        "has_horizontal_rule": has_horizontal_rule,
        "quirky_quotes": quirky_quotes,
        "bullet_glyph_lines": bullet_glyph_lines,
        "explicit_color": explicit_color,
        "explicit_font_size": explicit_font_size,
        "explicit_font_family": explicit_font_family,
        "explicit_line_height": explicit_line_height,
        "explicit_alignment": explicit_alignment,
        "classes_in_body": dict(classes_seen),
        "list_after_heading_pattern": dict(list_after_heading_pattern),
        "inline_styles_raw": inline_styles,
    }


def analyze_file(path: str) -> dict | None:
    with open(path, "r", encoding="utf-8") as fh:
        html = fh.read()
    soup = BeautifulSoup(html, "lxml")
    title, meta = get_title_and_meta(soup)
    prose = soup.find("div", class_=re.compile(r"\bprose\b"))
    if not prose:
        return None
    comp = find_compensation_node(prose)
    truncated_prose = prose
    if comp is not None:
        # Build a fresh prose containing only siblings before the compensation heading.
        wrapper = BeautifulSoup("<div class='prose'></div>", "lxml").find("div")
        for child in list(prose.children):
            if isinstance(child, Tag):
                ctxt = child.get_text(" ", strip=True)
                if COMP_MARKERS.match(ctxt or ""):
                    break
                wrapper.append(BeautifulSoup(str(child), "lxml").contents[0] if BeautifulSoup(str(child), "lxml").contents else None)
            else:
                if str(child).strip():
                    wrapper.append(str(child))
        truncated_prose = wrapper

    sig = style_signature(truncated_prose)
    sig["title"] = title
    sig["meta"] = meta
    sig["file"] = os.path.basename(path)
    sig["had_compensation_marker"] = comp is not None
    sig["body_char_len"] = len(truncated_prose.get_text(" ", strip=True))
    return sig


def main() -> None:
    results = []
    files = sorted(glob(os.path.join(JOB_DIR, "*.html")))
    for f in files:
        try:
            r = analyze_file(f)
            if r is not None:
                results.append(r)
        except Exception as e:
            print("ERR", f, e)
    print(f"Analyzed {len(results)} job postings")
    out_path = os.path.join(os.path.dirname(__file__), "results.json")
    # Counters aren't JSON-serializable directly
    def _clean(obj):
        if isinstance(obj, Counter):
            return dict(obj)
        if isinstance(obj, dict):
            return {k: _clean(v) for k, v in obj.items()}
        if isinstance(obj, list):
            return [_clean(v) for v in obj]
        return obj

    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(_clean(results), fh, indent=2, ensure_ascii=False)
    print("Wrote", out_path)


if __name__ == "__main__":
    main()
