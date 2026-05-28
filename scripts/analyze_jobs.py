#!/usr/bin/env python3
"""Analyze formatting consistency of Skydio job postings (pre-compensation block).

For each job posting we:
  1. Extract the title.
  2. Locate the job body: <div class="prose block-content"> ... </div>.
  3. Truncate everything from the "Compensation Range" block onward.
  4. Collect formatting signals: heading style, bold-as-heading patterns,
     list types, paragraph structure, intro paragraph wording, emoji use,
     trailing punctuation in headings, inline color styles, etc.
"""
from __future__ import annotations

import json
import os
import re
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JOBS_DIR = Path(os.environ.get("SKYDIO_JOBS_DIR", "/tmp/skydio_jobs"))
OUTPUT_JSON = REPO_ROOT / "data/job-formatting-analysis.json"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

PROSE_RE = re.compile(
    r'<div class="prose block-content">(?P<body>.*?)</div>\s*</article>',
    re.S,
)
# Fallback: just first <div class="prose block-content">...</div> (non greedy across nested divs is fine since
# the body itself usually has no nested divs except inner spans).
PROSE_FALLBACK_RE = re.compile(
    r'<div class="prose block-content">(?P<body>.*?)</div>\s*(?:<aside|<section|<footer|</article|</main|</body)',
    re.S,
)

TITLE_RE = re.compile(r"<title>(.*?)\s*\|\s*Skydio</title>", re.S)
LOC_TYPE_RE = re.compile(
    r'<p class="type-body-2">\s*(?P<loc>[^<]+?)\s*-\s*(?P<type>Full-time|Part-time|Intern|Contract)\s*</p>',
    re.I,
)

# Patterns used to chop the body at the start of the compensation block.
COMP_PATTERNS = [
    re.compile(r"<p[^>]*>\s*<strong>\s*Compensation\b[^<]*</strong>", re.I),
    re.compile(r"<p[^>]*>\s*<b>\s*Compensation\b[^<]*</b>", re.I),
    re.compile(r"<h[1-6][^>]*>\s*Compensation\b", re.I),
    re.compile(r"<strong>\s*Compensation Range\b", re.I),
    re.compile(r"<strong>\s*Compensation\s*</strong>", re.I),
    re.compile(r"<strong>\s*Salary\b", re.I),
    re.compile(r"<p[^>]*>\s*<strong>\s*Pay Range\b", re.I),
    re.compile(r"<p[^>]*>\s*<strong>[^<]*\bSalary Range\b[^<]*</strong>", re.I),
]

# Patterns matching the closing boilerplate (EEO + LinkedIn slug).  We truncate
# at these too so we are comparing apples to apples for jobs that omit
# compensation entirely.  We also record which one triggered the cut.
FOOTER_PATTERNS = [
    ("li_slug", re.compile(r"#LI-[A-Z0-9]+", re.I)),
    ("eeo_diversity", re.compile(r"At Skydio we believe that diversity drives innovation", re.I)),
    ("eeo_qualified", re.compile(r"Qualified applicants will receive consideration for employment", re.I)),
    ("e_verify", re.compile(r"For positions located in the United States of America, Skydio", re.I)),
]


def strip_tags(html: str) -> str:
    text = re.sub(r"<[^>]+>", " ", html)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def truncate_at_compensation(body: str) -> tuple[str, bool, str]:
    """Return (body_pre_comp, found_compensation_block, cut_signal).

    cut_signal is one of: 'compensation', 'li_slug', 'eeo_diversity',
    'eeo_qualified', 'e_verify', or 'none' (body returned as-is).
    """
    cuts: list[tuple[int, str, bool]] = []  # (offset, label, is_comp)
    for pat in COMP_PATTERNS:
        m = pat.search(body)
        if m:
            cuts.append((m.start(), "compensation", True))
    for label, pat in FOOTER_PATTERNS:
        m = pat.search(body)
        if m:
            cuts.append((m.start(), label, False))
    if not cuts:
        return body, False, "none"
    cuts.sort(key=lambda x: x[0])
    earliest_offset, label, is_comp = cuts[0]
    # found_compensation_block is True only if a compensation pattern exists
    # *anywhere* in the body (even if footer came first - unlikely)
    has_comp = any(is_c for _, _, is_c in cuts)
    return body[:earliest_offset], has_comp, label


# ---------------------------------------------------------------------------
# HTML feature extractor
# ---------------------------------------------------------------------------


class FeatureExtractor(HTMLParser):
    """Walk the body HTML and record formatting features."""

    HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.tag_stack: list[tuple[str, dict]] = []
        self.tag_counts: Counter[str] = Counter()
        self.heading_texts: list[tuple[str, str]] = []  # (tag, text)
        self.bold_paragraphs: list[str] = []  # text of <p> whose ENTIRE content is bold (used as a pseudo-heading)
        self.bold_inline_count = 0  # <strong> appearing mid-paragraph
        self.list_types: Counter[str] = Counter()  # ul / ol
        self.nested_list_count = 0
        self.li_with_p_count = 0
        self.li_plain_count = 0
        self.paragraph_count = 0
        self.empty_paragraph_count = 0
        self.link_count = 0
        self.style_attrs: list[str] = []
        self.color_styles: list[str] = []
        self.font_size_styles: list[str] = []
        self.font_family_styles: list[str] = []
        self.inline_classes: Counter[str] = Counter()
        self.italic_count = 0
        self.underline_count = 0
        self.br_count = 0
        self.hr_count = 0
        self.image_count = 0
        self.emoji_pseudo_headings: list[str] = []
        self.first_paragraph_text: str | None = None
        self._buffer: list[str] = []
        self._current_p_only_strong = None  # tracks if a <p> contains only <strong>
        self._inside_p = False
        self._p_text = []
        self._p_has_only_strong_child = True
        self._p_saw_strong = False
        self._p_saw_other_content = False
        self._inside_li = False
        self._li_has_p = False
        self._inside_strong_in_p = False
        self.headings_with_trailing_punct: list[str] = []
        self.section_headers: list[str] = []  # all "pseudo headings" (bold-only paragraphs + real headings)

    def handle_starttag(self, tag, attrs):
        attr_d = dict(attrs)
        self.tag_counts[tag] += 1
        self.tag_stack.append((tag, attr_d))

        style = attr_d.get("style", "")
        if style:
            self.style_attrs.append(style)
            if "color" in style.lower():
                self.color_styles.append(style)
            if re.search(r"font-size", style, re.I):
                self.font_size_styles.append(style)
            if re.search(r"font-family", style, re.I):
                self.font_family_styles.append(style)

        cls = attr_d.get("class", "")
        if cls:
            for c in cls.split():
                self.inline_classes[c] += 1

        if tag == "a":
            self.link_count += 1
        elif tag == "br":
            self.br_count += 1
        elif tag == "hr":
            self.hr_count += 1
        elif tag == "img":
            self.image_count += 1
        elif tag in ("em", "i"):
            self.italic_count += 1
        elif tag == "u":
            self.underline_count += 1
        elif tag in ("ul", "ol"):
            # is this nested inside a <li>?
            ancestor_tags = [t for t, _ in self.tag_stack[:-1]]
            if "li" in ancestor_tags:
                self.nested_list_count += 1
            self.list_types[tag] += 1
        elif tag == "li":
            self._inside_li = True
            self._li_has_p = False
        elif tag == "p":
            # a <p> nested inside a <li> doesn't count as a top-level paragraph
            ancestor_tags = [t for t, _ in self.tag_stack[:-1]]
            if "li" in ancestor_tags:
                self._li_has_p = True
            else:
                self.paragraph_count += 1
                self._inside_p = True
                self._p_text = []
                self._p_saw_strong = False
                self._p_saw_other_content = False
        elif tag in ("strong", "b"):
            if self._inside_p:
                self._p_saw_strong = True
                self._inside_strong_in_p = True
            else:
                # bold outside paragraph (e.g. inside <li>) - ignore for now
                pass
        elif tag in self.HEADING_TAGS:
            self._buffer = []

    def handle_endtag(self, tag):
        # pop matching tag from stack
        for i in range(len(self.tag_stack) - 1, -1, -1):
            if self.tag_stack[i][0] == tag:
                del self.tag_stack[i:]
                break

        if tag == "p" and self._inside_p:
            text = " ".join(self._p_text).strip()
            text = re.sub(r"\s+", " ", text)
            if not text:
                self.empty_paragraph_count += 1
            if self._p_saw_strong and not self._p_saw_other_content and text:
                # paragraph whose visible text was entirely inside <strong> - acts as pseudo-heading
                self.bold_paragraphs.append(text)
                self.section_headers.append(text)
            elif self._p_saw_strong:
                self.bold_inline_count += 1
            if self.first_paragraph_text is None and text:
                self.first_paragraph_text = text
            self._inside_p = False
            self._p_text = []
            self._p_saw_strong = False
            self._p_saw_other_content = False
        elif tag == "li" and self._inside_li:
            if self._li_has_p:
                self.li_with_p_count += 1
            else:
                self.li_plain_count += 1
            self._inside_li = False
            self._li_has_p = False
        elif tag in ("strong", "b") and self._inside_strong_in_p:
            self._inside_strong_in_p = False
        elif tag in self.HEADING_TAGS:
            text = " ".join(self._buffer).strip()
            self.heading_texts.append((tag, text))
            self.section_headers.append(text)
            self._buffer = []

    def handle_data(self, data):
        if self._inside_p:
            self._p_text.append(data)
            if self._inside_strong_in_p:
                pass
            else:
                if data.strip():
                    self._p_saw_other_content = True
        # capture heading text via buffer
        if self.tag_stack and self.tag_stack[-1][0] in self.HEADING_TAGS:
            self._buffer.append(data)


# ---------------------------------------------------------------------------
# Per-job analysis
# ---------------------------------------------------------------------------

EMOJI_RE = re.compile(
    "["
    "\U0001F300-\U0001FAFF"
    "\u2600-\u27BF"
    "\U0001F1E6-\U0001F1FF"
    "]"
)
INTRO_SIGNATURE = "Skydio is the leading"  # canonical intro paragraph opener


def analyze_job(html_path: Path) -> dict:
    html = html_path.read_text(errors="replace")

    title_m = TITLE_RE.search(html)
    title = title_m.group(1).strip() if title_m else html_path.stem

    loc_m = LOC_TYPE_RE.search(html)
    location = loc_m.group("loc").strip() if loc_m else ""
    employment_type = loc_m.group("type").strip() if loc_m else ""

    prose_m = PROSE_RE.search(html) or PROSE_FALLBACK_RE.search(html)
    if not prose_m:
        # last resort - find by class and read until two closing divs
        idx = html.find('<div class="prose block-content">')
        body = html[idx:idx + 60000] if idx != -1 else ""
    else:
        body = prose_m.group("body")

    pre_comp, found_comp, cut_signal = truncate_at_compensation(body)

    extractor = FeatureExtractor()
    extractor.feed(pre_comp)

    plain_text = strip_tags(pre_comp)
    word_count = len(plain_text.split())
    char_count = len(plain_text)

    # Detect headings ending in a colon (a stylistic choice)
    bold_p_with_colon = sum(1 for t in extractor.bold_paragraphs if t.rstrip().endswith(":"))
    bold_p_without_colon = len(extractor.bold_paragraphs) - bold_p_with_colon

    # Section headers normalization
    canon_sections = [re.sub(r"[:\s]+$", "", h).strip().lower() for h in extractor.section_headers]

    has_intro = bool(extractor.first_paragraph_text and INTRO_SIGNATURE.lower() in extractor.first_paragraph_text.lower())
    intro_paragraph = extractor.first_paragraph_text or ""

    emoji_in_body = bool(EMOJI_RE.search(plain_text))

    inline_color_count = len(extractor.color_styles)
    inline_font_size_count = len(extractor.font_size_styles)
    inline_font_family_count = len(extractor.font_family_styles)
    inline_style_count = len(extractor.style_attrs)

    # Heading hierarchy summary
    heading_tag_counts = Counter(t for t, _ in extractor.heading_texts)

    # Common section labels (canonicalised)
    common_sections_present = set()
    for h in canon_sections:
        for key in (
            "about the role",
            "about the team",
            "about you",
            "about this role",
            "how you",
            "how you'll make an impact",
            "what makes you a good fit",
            "what makes your a good fit",  # typo seen in sample
            "what you'll do",
            "what you'll bring",
            "what you'll need",
            "what we're looking for",
            "responsibilities",
            "qualifications",
            "preferred qualifications",
            "nice to have",
            "nice to haves",
            "bonus points",
            "requirements",
            "requirement",
            "skills",
            "minimum qualifications",
            "benefits",
            "what's in it for you",
            "who you are",
        ):
            if key in h:
                common_sections_present.add(key)

    return {
        "id": html_path.stem,
        "title": title,
        "location": location,
        "type": employment_type,
        "url": f"https://www.skydio.com/jobs/{html_path.stem}",
        "found_compensation_block": found_comp,
        "cut_signal": cut_signal,
        "word_count": word_count,
        "char_count": char_count,
        "has_canonical_intro": has_intro,
        "intro_first_sentence": intro_paragraph.split(". ")[0][:200] if intro_paragraph else "",
        "intro_length": len(intro_paragraph),
        "headings_real": [{"tag": t, "text": txt} for t, txt in extractor.heading_texts],
        "heading_tag_counts": dict(heading_tag_counts),
        "bold_pseudo_headings": extractor.bold_paragraphs,
        "bold_pseudo_heading_count": len(extractor.bold_paragraphs),
        "bold_pseudo_headings_with_colon": bold_p_with_colon,
        "bold_pseudo_headings_without_colon": bold_p_without_colon,
        "bold_inline_in_paragraph_count": extractor.bold_inline_count,
        "paragraph_count": extractor.paragraph_count,
        "empty_paragraph_count": extractor.empty_paragraph_count,
        "list_ul_count": extractor.list_types.get("ul", 0),
        "list_ol_count": extractor.list_types.get("ol", 0),
        "list_li_total": extractor.tag_counts.get("li", 0),
        "list_li_with_inner_p": extractor.li_with_p_count,
        "list_li_plain": extractor.li_plain_count,
        "nested_list_count": extractor.nested_list_count,
        "link_count": extractor.link_count,
        "italic_count": extractor.italic_count,
        "underline_count": extractor.underline_count,
        "br_count": extractor.br_count,
        "hr_count": extractor.hr_count,
        "image_count": extractor.image_count,
        "inline_style_attr_count": inline_style_count,
        "inline_color_style_count": inline_color_count,
        "inline_font_size_style_count": inline_font_size_count,
        "inline_font_family_style_count": inline_font_family_count,
        "inline_styles_sample": extractor.style_attrs[:5],
        "color_styles_sample": extractor.color_styles[:5],
        "font_size_styles_sample": extractor.font_size_styles[:5],
        "font_family_styles_sample": extractor.font_family_styles[:5],
        "inline_classes": dict(extractor.inline_classes.most_common(10)),
        "emoji_in_body": emoji_in_body,
        "common_section_labels": sorted(common_sections_present),
        "all_section_headers_canon": canon_sections,
    }


def main() -> None:
    files = sorted(JOBS_DIR.glob("*.html"))
    results = []
    for f in files:
        try:
            results.append(analyze_job(f))
        except Exception as exc:  # pragma: no cover - defensive
            print(f"FAILED {f.name}: {exc}")
    OUTPUT_JSON.write_text(json.dumps(results, indent=2))
    print(f"Wrote {len(results)} job analyses to {OUTPUT_JSON}")
    # Quick stats
    missing_comp = [r for r in results if not r["found_compensation_block"]]
    print(f"Jobs missing compensation block detection: {len(missing_comp)}")
    for r in missing_comp[:10]:
        print(f"  - {r['title']} ({r['id']})")


if __name__ == "__main__":
    main()
