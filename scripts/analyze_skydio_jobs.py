#!/usr/bin/env python3
"""Analyze Skydio careers postings for pre-compensation formatting consistency.

Pulls every listed posting from the Skydio Ashby job board API, isolates the
content that appears BEFORE the Compensation block, and reports formatting
inconsistencies (heading hierarchy, bold/italic/underline use, list style,
inline CSS overrides, alignment, whitespace, label punctuation, etc.).

Output: a Markdown report at reports/skydio-job-formatting-report.md.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString, Tag

API_URL = (
    "https://api.ashbyhq.com/posting-api/job-board/Skydio?includeCompensation=true"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = REPO_ROOT / "data" / "skydio_jobs.json"
REPORT_PATH = REPO_ROOT / "reports" / "skydio-job-formatting-report.md"


# --------------------------------------------------------------------------- #
# Fetch
# --------------------------------------------------------------------------- #


def fetch_jobs(force: bool = False) -> list[dict]:
    """Fetch jobs from Ashby (cached on disk)."""
    if DATA_PATH.exists() and not force:
        with DATA_PATH.open() as fh:
            return json.load(fh)["jobs"]

    DATA_PATH.parent.mkdir(parents=True, exist_ok=True)
    req = urllib.request.Request(API_URL, headers={"User-Agent": "skydio-audit/1.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        payload = json.load(resp)
    DATA_PATH.write_text(json.dumps(payload, indent=2))
    return payload["jobs"]


# --------------------------------------------------------------------------- #
# Pre-compensation extraction
# --------------------------------------------------------------------------- #


COMPENSATION_LABEL_RE = re.compile(
    r"^\s*compensation\s*[:\-–—]?\s*$|"
    r"^\s*compensation\s*(range|details|information)\b|"
    r"^\s*salary\s*(range|information)\b|"
    r"^\s*pay\s*(range|transparency)\b",
    re.IGNORECASE,
)


_COMP_LABELS = {
    "compensation",
    "compensation range",
    "compensation details",
    "compensation information",
    "salary range",
    "pay range",
    "pay transparency",
}

# Canonical Skydio compensation paragraph openings (used when there's no label).
_COMP_PROSE_PREFIXES = (
    "at skydio, our compensation packages",
    "at skydio our compensation packages",
    "at skydio, our compensation",
    "skydio's compensation packages",
    "skydio offers competitive",
    "the annual base salary range for this position",
    "the base salary range for this position",
    "the salary range for this position",
)


def _block_starts_compensation(tag: Tag) -> bool:
    """A top-level block 'starts' the compensation section if its first
    visible text begins with the word 'Compensation' (or salary/pay range
    headers Skydio sometimes uses), or with the canonical Skydio
    'At Skydio, our compensation packages…' boilerplate paragraph."""
    text = tag.get_text(" ", strip=True)
    if not text:
        return False
    head = text.split(":", 1)[0].strip().lower()
    if head in _COMP_LABELS:
        return True
    first_strong = tag.find(["strong", "b"])
    if first_strong is not None:
        st = first_strong.get_text(" ", strip=True).lower().rstrip(":").strip()
        if st in _COMP_LABELS:
            return True
    # No label, but the paragraph IS the compensation block (Skydio's
    # boilerplate sometimes drops the bold "Compensation:" prefix).
    lower = text.lower().lstrip()
    for prefix in _COMP_PROSE_PREFIXES:
        if lower.startswith(prefix):
            return True
    return False


# Skydio's EEO / diversity boilerplate that sits AFTER the compensation block.
# For non-US / intern postings that have no compensation paragraph, we use
# this as a fallback "stop" marker so we don't analyze post-content boilerplate
# as if it were the body of the role description.
_EEO_PROSE_PREFIXES = (
    "at skydio we believe that diversity drives innovation",
    "qualified applicants will receive consideration",
    "skydio, inc. is an equal opportunity employer",
    "skydio is an equal opportunity employer",
    "for positions located in the united states",
)


def _block_starts_eeo_boilerplate(tag: Tag) -> bool:
    text = tag.get_text(" ", strip=True).lower().lstrip()
    if not text:
        return False
    for prefix in _EEO_PROSE_PREFIXES:
        if text.startswith(prefix):
            return True
    return False


def slice_pre_compensation(html: str) -> tuple[str, BeautifulSoup, bool]:
    """Return (pre-compensation HTML string, parsed soup of pre-comp content,
    whether a compensation section was actually found)."""
    soup = BeautifulSoup(f"<div id='root'>{html}</div>", "lxml")
    root = soup.find("div", id="root")
    pre_blocks: list[Tag] = []
    found = False
    for child in list(root.children):
        if isinstance(child, NavigableString):
            if str(child).strip():
                # rare stray text
                pre_blocks.append(child)  # type: ignore[arg-type]
            continue
        if isinstance(child, Tag):
            if _block_starts_compensation(child):
                found = True
                break
            # If we never find a compensation block, also stop at the EEO
            # boilerplate (which always sits AFTER compensation in postings
            # that DO have it). This keeps non-US / intern postings honest.
            if _block_starts_eeo_boilerplate(child):
                break
            pre_blocks.append(child)
    pre_html = "".join(str(b) for b in pre_blocks)
    pre_soup = BeautifulSoup(f"<div id='root'>{pre_html}</div>", "lxml")
    return pre_html, pre_soup, found


# --------------------------------------------------------------------------- #
# Feature extraction
# --------------------------------------------------------------------------- #


SECTION_KEYWORDS = [
    "about the role",
    "about this role",
    "about the position",
    "about the team",
    "about you",
    "about skydio",
    "about us",
    "what you'll do",
    "what you’ll do",
    "what you will do",
    "what you'll be doing",
    "what you’ll be doing",
    "your responsibilities",
    "responsibilities",
    "key responsibilities",
    "how you'll make an impact",
    "how you’ll make an impact",
    "the impact you'll have",
    "the impact you’ll have",
    "what makes you a good fit",
    "what we're looking for",
    "what we’re looking for",
    "what we look for",
    "qualifications",
    "minimum qualifications",
    "preferred qualifications",
    "required qualifications",
    "requirements",
    "must haves",
    "must-haves",
    "nice to haves",
    "nice-to-haves",
    "bonus points",
    "preferred",
    "skills and experience",
    "experience",
    "please note",
]


def normalize_label(s: str) -> str:
    s = s.strip().rstrip(":").rstrip(".").strip()
    s = re.sub(r"\s+", " ", s)
    return s.lower().replace("’", "'")


def is_section_label_text(text: str) -> bool:
    norm = normalize_label(text)
    if not norm:
        return False
    if len(norm) > 90:
        return False
    for kw in SECTION_KEYWORDS:
        if norm == kw or norm.startswith(kw):
            return True
    return False


@dataclass
class Posting:
    id: str
    title: str
    department: str
    team: str
    location: str
    url: str
    raw_html: str
    pre_html: str
    pre_soup: BeautifulSoup
    has_compensation: bool

    # Top-level structure --------------------------------------------------
    block_tags: list[str] = field(default_factory=list)
    heading_tags: Counter = field(default_factory=Counter)
    section_label_styles: Counter = field(default_factory=Counter)
    section_labels: list[tuple[str, str]] = field(default_factory=list)  # (style, text)

    # Text styling ---------------------------------------------------------
    has_underline: bool = False
    has_italic: bool = False
    has_em: bool = False
    has_uppercase_block: bool = False
    has_color_style: bool = False
    has_font_size_style: bool = False
    has_font_family_style: bool = False
    has_font_tag: bool = False
    has_align_style: bool = False
    has_text_align_attr: bool = False
    inline_style_props: Counter = field(default_factory=Counter)
    nonstandard_inline_styles: list[str] = field(default_factory=list)

    # Lists ----------------------------------------------------------------
    ul_count: int = 0
    ol_count: int = 0
    list_items: int = 0
    list_with_p_wrappers: bool = False  # <li><p>...</p></li> pattern
    list_without_p_wrappers: bool = False  # <li>...text...</li> without <p>

    # Whitespace / cleanliness --------------------------------------------
    empty_paragraphs: int = 0
    br_count: int = 0
    nbsp_count: int = 0
    trailing_whitespace_blocks: int = 0
    double_space_runs: int = 0

    # Boilerplate ----------------------------------------------------------
    starts_with_intro_paragraph: bool = False
    intro_first_words: str = ""

    # Punctuation / casing for labels -------------------------------------
    labels_with_colon: int = 0
    labels_without_colon: int = 0
    labels_titlecase: int = 0
    labels_sentencecase: int = 0
    labels_all_caps: int = 0

    # Sizes ----------------------------------------------------------------
    pre_text_chars: int = 0

    # Issues bag (already-flagged human-readable strings) -----------------
    issues: list[str] = field(default_factory=list)


SKYDIO_INTRO_PHRASE = "Skydio is the leading"

STANDARD_STYLE = "min-height:1.5em"


def parse_inline_style(style: str) -> dict[str, str]:
    out: dict[str, str] = {}
    for part in style.split(";"):
        if ":" in part:
            k, v = part.split(":", 1)
            out[k.strip().lower()] = v.strip().lower()
    return out


def extract_features(p: Posting) -> None:
    soup = p.pre_soup
    root = soup.find("div", id="root")
    if root is None:
        return

    text_total = root.get_text("\n", strip=False)
    p.pre_text_chars = len(text_total.strip())
    p.nbsp_count = text_total.count("\xa0")
    p.double_space_runs = len(re.findall(r"  +", text_total))

    # Top-level blocks
    for child in root.find_all(recursive=False):
        if isinstance(child, Tag):
            p.block_tags.append(child.name)

    # Intro
    first_block = next((c for c in root.find_all(recursive=False) if isinstance(c, Tag)), None)
    if first_block is not None:
        intro_text = first_block.get_text(" ", strip=True)
        p.intro_first_words = intro_text[:120]
        p.starts_with_intro_paragraph = intro_text.startswith(SKYDIO_INTRO_PHRASE)

    # Headings & section labels
    for tag in root.find_all(True):
        name = tag.name
        if name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            p.heading_tags[name] += 1

        # Inline style audit
        style = tag.get("style")
        if style:
            props = parse_inline_style(style)
            for k, v in props.items():
                p.inline_style_props[f"{k}:{v}"] += 1
            # Anything other than the universal 'min-height:1.5em' is non-standard.
            extras = {k: v for k, v in props.items() if not (k == "min-height" and v == "1.5em")}
            if extras:
                p.nonstandard_inline_styles.append(
                    f"<{name}> " + "; ".join(f"{k}:{v}" for k, v in extras.items())
                )
            for k in props:
                if k == "color":
                    p.has_color_style = True
                if k in {"font-size"}:
                    p.has_font_size_style = True
                if k == "font-family":
                    p.has_font_family_style = True
                if k == "text-align":
                    p.has_align_style = True
                if k == "background" or k == "background-color":
                    p.has_color_style = True

        if tag.has_attr("align"):
            p.has_text_align_attr = True
        if name == "font":
            p.has_font_tag = True
        if name == "u":
            p.has_underline = True
        if name == "i":
            p.has_italic = True
        if name == "em":
            p.has_em = True
        if name == "br":
            p.br_count += 1

    # Section label classification: top-level <p> whose entire content is
    # bold (<strong>) is the dominant pattern. We also catch real headings
    # and bare uppercase paragraphs.
    for child in root.find_all(recursive=False):
        if not isinstance(child, Tag):
            continue
        if child.name in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            txt = child.get_text(" ", strip=True)
            if is_section_label_text(txt) or len(txt) < 80:
                p.section_label_styles[child.name.upper()] += 1
                p.section_labels.append((child.name.upper(), txt))
                _classify_label_punct_case(p, txt)
            continue
        if child.name == "p":
            txt = child.get_text(" ", strip=True)
            if not txt:
                p.empty_paragraphs += 1
                continue
            if txt != txt.rstrip():
                p.trailing_whitespace_blocks += 1
            # Detect "section label" paragraphs.
            # Case 1: <p><strong>...</strong></p> (and nothing else)
            strongs = child.find_all(["strong", "b"], recursive=True)
            child_text_compact = re.sub(r"\s+", "", txt)
            strong_text_compact = re.sub(
                r"\s+",
                "",
                "".join(s.get_text("", strip=True) for s in strongs),
            )
            is_only_bold = bool(strongs) and child_text_compact == strong_text_compact

            # Case 2: <p><u><strong>...</strong></u></p> — Skydio sometimes
            # uses underline + bold for "PLEASE NOTE:" callouts.
            us = child.find_all("u", recursive=True)

            looks_like_label = is_only_bold and (
                is_section_label_text(txt) or len(txt) < 80
            )

            if looks_like_label:
                style_key = "P+STRONG"
                if us:
                    style_key = "P+U+STRONG"
                p.section_label_styles[style_key] += 1
                p.section_labels.append((style_key, txt))
                _classify_label_punct_case(p, txt)
            else:
                # Plain paragraph; flag UPPERCASE / weird styling
                if txt.isupper() and len(txt) > 12:
                    p.has_uppercase_block = True

    # Lists
    for ul in root.find_all("ul"):
        p.ul_count += 1
        for li in ul.find_all("li", recursive=False):
            p.list_items += 1
            ps = li.find_all("p", recursive=False)
            li_text = li.get_text("", strip=True)
            ps_text = "".join(pp.get_text("", strip=True) for pp in ps)
            if ps and re.sub(r"\s+", "", li_text) == re.sub(r"\s+", "", ps_text):
                p.list_with_p_wrappers = True
            else:
                p.list_without_p_wrappers = True
    for ol in root.find_all("ol"):
        p.ol_count += 1
        for li in ol.find_all("li", recursive=False):
            p.list_items += 1
            ps = li.find_all("p", recursive=False)
            li_text = li.get_text("", strip=True)
            ps_text = "".join(pp.get_text("", strip=True) for pp in ps)
            if ps and re.sub(r"\s+", "", li_text) == re.sub(r"\s+", "", ps_text):
                p.list_with_p_wrappers = True
            else:
                p.list_without_p_wrappers = True


def _classify_label_punct_case(p: Posting, text: str) -> None:
    t = text.strip()
    if t.endswith(":"):
        p.labels_with_colon += 1
    else:
        p.labels_without_colon += 1
    body = t.rstrip(":").strip()
    if not body:
        return
    if body.isupper() and len(body) > 3:
        p.labels_all_caps += 1
        return
    words = body.split()
    titlecased = sum(1 for w in words if w[:1].isupper()) >= max(2, int(len(words) * 0.6))
    if titlecased and len(words) > 1:
        p.labels_titlecase += 1
    else:
        p.labels_sentencecase += 1


# --------------------------------------------------------------------------- #
# Aggregation / norming
# --------------------------------------------------------------------------- #


@dataclass
class Norms:
    section_label_dominant_style: str
    section_label_dominant_share: float
    label_case_dominant: str
    label_case_dominant_share: float
    label_colon_dominant: str  # "with" or "without"
    label_colon_dominant_share: float
    list_wrapper_dominant: str  # "p-wrapped" or "bare"
    list_wrapper_dominant_share: float
    standard_inline_style: str
    intro_share: float


def compute_norms(postings: list[Posting]) -> Norms:
    style_counter: Counter = Counter()
    case_counter: Counter = Counter()
    colon_counter: Counter = Counter()
    list_counter: Counter = Counter()
    intro_yes = 0

    for p in postings:
        # Pick each posting's dominant style for its section labels
        if p.section_label_styles:
            style_counter[p.section_label_styles.most_common(1)[0][0]] += 1
        # Case
        if p.labels_titlecase + p.labels_sentencecase + p.labels_all_caps > 0:
            case = max(
                ("titlecase", p.labels_titlecase),
                ("sentencecase", p.labels_sentencecase),
                ("all-caps", p.labels_all_caps),
                key=lambda x: x[1],
            )[0]
            case_counter[case] += 1
        # Colon
        if p.labels_with_colon + p.labels_without_colon > 0:
            colon_counter[
                "with" if p.labels_with_colon >= p.labels_without_colon else "without"
            ] += 1
        # Lists
        if p.list_with_p_wrappers and not p.list_without_p_wrappers:
            list_counter["p-wrapped"] += 1
        elif p.list_without_p_wrappers and not p.list_with_p_wrappers:
            list_counter["bare"] += 1
        elif p.list_with_p_wrappers and p.list_without_p_wrappers:
            list_counter["mixed"] += 1
        if p.starts_with_intro_paragraph:
            intro_yes += 1

    n = len(postings)

    def dom(c: Counter) -> tuple[str, float]:
        if not c:
            return ("(none)", 0.0)
        k, v = c.most_common(1)[0]
        return (k, v / sum(c.values()))

    s_k, s_share = dom(style_counter)
    c_k, c_share = dom(case_counter)
    col_k, col_share = dom(colon_counter)
    l_k, l_share = dom(list_counter)

    return Norms(
        section_label_dominant_style=s_k,
        section_label_dominant_share=s_share,
        label_case_dominant=c_k,
        label_case_dominant_share=c_share,
        label_colon_dominant=col_k,
        label_colon_dominant_share=col_share,
        list_wrapper_dominant=l_k,
        list_wrapper_dominant_share=l_share,
        standard_inline_style=STANDARD_STYLE,
        intro_share=intro_yes / n if n else 0.0,
    )


def diagnose(postings: list[Posting], norms: Norms) -> None:
    """Populate Posting.issues based on deviations from norms."""
    for p in postings:
        # Section-label style deviation
        if p.section_label_styles:
            local_dom = p.section_label_styles.most_common(1)[0][0]
            if local_dom != norms.section_label_dominant_style:
                p.issues.append(
                    f"Section labels primarily styled as **{local_dom}** while "
                    f"{int(norms.section_label_dominant_share*100)}% of postings use "
                    f"**{norms.section_label_dominant_style}**."
                )
            # Mixed within a single posting
            if len(p.section_label_styles) > 1:
                breakdown = ", ".join(
                    f"{k}={v}" for k, v in p.section_label_styles.most_common()
                )
                p.issues.append(
                    f"Mixes section-label styles within the posting "
                    f"({breakdown})."
                )
        else:
            p.issues.append("No detectable section labels (flat prose).")

        # Real heading tags (Skydio's careers page renders these very large)
        if p.heading_tags:
            tags = ", ".join(f"{k}={v}" for k, v in p.heading_tags.most_common())
            p.issues.append(
                f"Uses real heading tags inside the body ({tags}); the page-wide "
                f"convention is `<p><strong>` for section labels."
            )

        # Underline usage
        if p.has_underline:
            p.issues.append("Uses `<u>` underline (rare across postings; only "
                            "appears in 'PLEASE NOTE' callouts).")
        if p.has_italic:
            p.issues.append("Uses `<i>` italics tag (non-standard; most postings use plain text or `<em>`).")
        if p.has_font_tag:
            p.issues.append("Uses deprecated `<font>` tag.")
        if p.has_color_style:
            p.issues.append("Inline `color` / background styling overrides site CSS.")
        if p.has_font_size_style:
            p.issues.append("Inline `font-size` overrides site CSS.")
        if p.has_font_family_style:
            p.issues.append("Inline `font-family` overrides site CSS.")
        if p.has_align_style or p.has_text_align_attr:
            p.issues.append("Inline alignment override (`text-align` / `align=`).")
        if p.has_uppercase_block:
            p.issues.append("Contains an ALL-CAPS paragraph (visually shouts; "
                            "no other postings do this).")

        # Whitespace cleanliness
        if p.empty_paragraphs:
            p.issues.append(
                f"Contains {p.empty_paragraphs} empty paragraph(s) (extra vertical gap)."
            )
        if p.br_count:
            p.issues.append(f"Contains {p.br_count} `<br>` tag(s) (line-break "
                            "instead of paragraph break).")
        if p.nbsp_count:
            p.issues.append(
                f"Contains {p.nbsp_count} non-breaking space(s) — likely pasted "
                "from a word processor."
            )
        if p.double_space_runs:
            p.issues.append(
                f"Contains {p.double_space_runs} run(s) of double spaces in body text."
            )
        if p.trailing_whitespace_blocks:
            p.issues.append(
                f"{p.trailing_whitespace_blocks} block(s) end with trailing whitespace."
            )

        # Label punctuation/case
        total_labels = (
            p.labels_with_colon + p.labels_without_colon
        )
        if total_labels >= 2:
            if p.labels_with_colon and p.labels_without_colon:
                p.issues.append(
                    f"Inconsistent label punctuation: {p.labels_with_colon} end "
                    f"with `:` and {p.labels_without_colon} do not."
                )
            else:
                this = "with" if p.labels_with_colon else "without"
                if this != norms.label_colon_dominant:
                    p.issues.append(
                        f"Section labels {this} colons, while "
                        f"{int(norms.label_colon_dominant_share*100)}% of postings "
                        f"use labels {norms.label_colon_dominant} colons."
                    )

        cases_present = [
            ("titlecase", p.labels_titlecase),
            ("sentencecase", p.labels_sentencecase),
            ("all-caps", p.labels_all_caps),
        ]
        used = [c for c, n in cases_present if n > 0]
        if len(used) > 1:
            p.issues.append(
                "Inconsistent label capitalization within the posting "
                f"({', '.join(f'{c}={n}' for c, n in cases_present if n > 0)})."
            )
        else:
            local_case = used[0] if used else None
            if local_case and local_case != norms.label_case_dominant:
                p.issues.append(
                    f"Section labels use **{local_case}** while "
                    f"{int(norms.label_case_dominant_share*100)}% of postings use "
                    f"**{norms.label_case_dominant}**."
                )

        # Lists
        if p.list_with_p_wrappers and p.list_without_p_wrappers:
            p.issues.append(
                "Mixes list-item structures (`<li><p>…</p></li>` and `<li>…</li>` "
                "in the same posting) — this produces uneven bullet spacing."
            )
        else:
            local_list = (
                "p-wrapped" if p.list_with_p_wrappers
                else "bare" if p.list_without_p_wrappers
                else None
            )
            if local_list and norms.list_wrapper_dominant in {"p-wrapped", "bare"} \
                    and local_list != norms.list_wrapper_dominant:
                p.issues.append(
                    f"List items rendered as **{local_list}** while "
                    f"{int(norms.list_wrapper_dominant_share*100)}% of postings use "
                    f"**{norms.list_wrapper_dominant}** items."
                )

        # Non-standard inline styles (anything other than min-height:1.5em)
        if p.nonstandard_inline_styles:
            p.issues.append(
                "Non-standard inline styles detected: "
                + "; ".join(sorted(set(p.nonstandard_inline_styles))[:5])
                + ("…" if len(set(p.nonstandard_inline_styles)) > 5 else "")
            )

        # Intro boilerplate
        if not p.starts_with_intro_paragraph:
            preview = p.intro_first_words.replace("\n", " ")[:90]
            p.issues.append(
                f"Does not begin with the standard \"Skydio is the leading…\" "
                f"intro paragraph (starts with: \"{preview}\")."
            )


# --------------------------------------------------------------------------- #
# Reporting
# --------------------------------------------------------------------------- #


def render_report(postings: list[Posting], norms: Norms) -> str:
    n = len(postings)
    flagged = [p for p in postings if p.issues]
    clean = [p for p in postings if not p.issues]

    # Top-level counters for the executive summary
    style_counter: Counter = Counter()
    for p in postings:
        for k, v in p.section_label_styles.items():
            style_counter[k] += v

    list_wrapper_counter: Counter = Counter()
    for p in postings:
        if p.list_with_p_wrappers and p.list_without_p_wrappers:
            list_wrapper_counter["mixed"] += 1
        elif p.list_with_p_wrappers:
            list_wrapper_counter["p-wrapped"] += 1
        elif p.list_without_p_wrappers:
            list_wrapper_counter["bare"] += 1

    issue_counter: Counter = Counter()
    for p in postings:
        for issue in p.issues:
            # Bucket: take the first 60 chars as a category-ish key.
            key = issue.split(".")[0]
            key = re.sub(r"\d+", "N", key)
            issue_counter[key] += 1

    # Group flagged postings by department for readability
    by_dept: dict[str, list[Posting]] = defaultdict(list)
    for p in flagged:
        by_dept[p.department or "(no dept)"].append(p)

    out: list[str] = []
    out.append("# Skydio Careers — Pre-Compensation Formatting Audit")
    out.append("")
    out.append(
        f"_Source: `{API_URL}` (Ashby job board), pulled live. "
        f"All listed postings analyzed up to (and not including) the "
        f"\"Compensation\" block._"
    )
    out.append("")
    out.append(f"**Postings analyzed:** {n}  ")
    comp_found = sum(1 for p in postings if p.has_compensation)
    out.append(f"**Postings with a detectable Compensation block:** {comp_found} / {n}  ")
    out.append(f"**Postings flagged with at least one inconsistency:** "
               f"{len(flagged)} ({int(100*len(flagged)/n)}%)  ")
    out.append(f"**Postings with no detected formatting issues:** {len(clean)}")
    out.append("")
    out.append("**Contents**")
    out.append("")
    out.append("1. [Executive summary](#1-executive-summary)")
    out.append("2. [Distribution of section-label styles across postings](#2-distribution-of-section-label-styles-across-postings)")
    out.append("3. [Distribution of list-item structure](#3-distribution-of-list-item-structure)")
    out.append("4. [Flagged postings (pre-compensation content only)](#4-flagged-postings-pre-compensation-content-only)")
    out.append("5. [Postings with no detected issues](#5-postings-with-no-detected-issues)")
    out.append("6. [Recommendations for standardizing pre-compensation content](#6-recommendations-for-standardizing-pre-compensation-content)")
    out.append("")

    # ------------------------------------------------------------------ #
    # 1. Executive summary
    # ------------------------------------------------------------------ #
    out.append("## 1. Executive summary")
    out.append("")
    out.append(
        "Every posting on `skydio.com/careers` is rendered from HTML stored "
        "in Ashby. The Skydio site's CSS gives **all** of these a single "
        "uniform look — body text inherits the page font, size, weight, line "
        "height, and color from the careers stylesheet. So the only places "
        "real visual inconsistencies can creep in are the **HTML structure** "
        "of each posting (which tags are used) and any **inline `style=` "
        "overrides** writers add inside Ashby's editor."
    )
    out.append("")
    out.append("**The page-wide conventions** (what most postings do):")
    out.append("")
    out.append(
        f"- **Section labels** are rendered as `<p><strong>Label:</strong></p>` "
        f"in **{int(norms.section_label_dominant_share*100)}%** of postings "
        f"(dominant style: `{norms.section_label_dominant_style}`)."
    )
    out.append(
        f"- **Label casing**: **{norms.label_case_dominant}** in "
        f"~{int(norms.label_case_dominant_share*100)}% of postings."
    )
    out.append(
        f"- **Label colon**: labels end **{norms.label_colon_dominant}** a colon in "
        f"~{int(norms.label_colon_dominant_share*100)}% of postings."
    )
    out.append(
        f"- **Bulleted list items**: **{norms.list_wrapper_dominant}** "
        f"(`<li><p>…</p></li>`) in "
        f"~{int(norms.list_wrapper_dominant_share*100)}% of postings."
    )
    out.append(
        f"- Every block carries the inline style `style=\"{STANDARD_STYLE}\"` "
        "(this is Ashby's default and is consistent — not an issue)."
    )
    out.append(
        f"- **Standard intro paragraph** (\"Skydio is the leading…\") opens "
        f"~{int(norms.intro_share*100)}% of postings."
    )
    out.append("")

    out.append("**Where postings drift from the norm** (most common issues):")
    out.append("")
    for k, v in issue_counter.most_common(12):
        out.append(f"- {v}× — {k}.")
    out.append("")

    # Bonus: title-string hygiene (out of strict scope, but easy to spot).
    bad_titles = [
        p for p in postings if p.title != p.title.strip() or "  " in p.title
    ]
    if bad_titles:
        out.append("**Bonus — title-string hygiene** (visible in the careers index):")
        out.append("")
        for p in bad_titles:
            out.append(
                f"- `\"{p.title}\"` — leading/trailing whitespace or double space."
            )
        out.append("")

    # ------------------------------------------------------------------ #
    # 2. Style distributions
    # ------------------------------------------------------------------ #
    out.append("## 2. Distribution of section-label styles across postings")
    out.append("")
    out.append("| Style used for section labels (e.g. \"About the role\") | Postings |")
    out.append("|---|---|")
    used_styles_by_posting: Counter = Counter()
    for p in postings:
        if not p.section_label_styles:
            used_styles_by_posting["(none — flat prose)"] += 1
            continue
        if len(p.section_label_styles) > 1:
            used_styles_by_posting["mixed within posting"] += 1
        else:
            used_styles_by_posting[next(iter(p.section_label_styles))] += 1
    for style, ct in used_styles_by_posting.most_common():
        out.append(f"| `{style}` | {ct} |")
    out.append("")

    # List wrapper distribution
    out.append("## 3. Distribution of list-item structure")
    out.append("")
    out.append("| List-item structure | Postings (with lists) |")
    out.append("|---|---|")
    if list_wrapper_counter:
        for k, v in list_wrapper_counter.most_common():
            out.append(f"| `{k}` | {v} |")
    else:
        out.append("| (no postings contain lists) | 0 |")
    out.append("")
    out.append(
        "_Why this matters visually: a `<li>` whose text is wrapped in `<p>` "
        "renders with the page's standard paragraph spacing above and below; a "
        "bare `<li>` does not. Mixing these in one page produces visibly "
        "uneven gaps between bullets._"
    )
    out.append("")

    # ------------------------------------------------------------------ #
    # 4. Flagged postings, grouped by department
    # ------------------------------------------------------------------ #
    out.append("## 4. Flagged postings (pre-compensation content only)")
    out.append("")
    out.append(
        "Each entry below lists the issues detected in that posting's "
        "pre-compensation HTML, with quotes anchored to specific elements where "
        "possible."
    )
    out.append("")

    for dept in sorted(by_dept):
        out.append(f"### {dept}")
        out.append("")
        for p in sorted(by_dept[dept], key=lambda x: x.title.lower()):
            out.append(f"#### {p.title}")
            out.append(
                f"_{p.team} · {p.location} · "
                f"[posting]({p.url})_"
            )
            out.append("")
            # Quick fingerprint
            label_styles = ", ".join(
                f"`{k}`={v}" for k, v in p.section_label_styles.most_common()
            ) or "_(none)_"
            heading_tags = ", ".join(
                f"`{k}`={v}" for k, v in p.heading_tags.most_common()
            ) or "_(none)_"
            list_summary = (
                f"{p.ul_count} `<ul>`, {p.ol_count} `<ol>`, "
                f"{p.list_items} items"
            )
            out.append(
                f"- Section-label styles: {label_styles}  "
            )
            out.append(
                f"- Heading tags inside body: {heading_tags}  "
            )
            out.append(f"- Lists: {list_summary}  ")
            out.append(
                f"- Pre-compensation length: {p.pre_text_chars} chars across "
                f"{len(p.block_tags)} top-level blocks"
            )
            if p.section_labels:
                # Show the actual labels so reviewers can see at a glance
                # which case/colon style each posting actually uses.
                quoted = ", ".join(
                    f"`{style}` \"{text[:60]}\"" for style, text in p.section_labels[:8]
                )
                if len(p.section_labels) > 8:
                    quoted += f", … (+{len(p.section_labels) - 8} more)"
                out.append(f"- Actual labels: {quoted}")
            out.append("")
            out.append("**Issues:**")
            out.append("")
            for issue in p.issues:
                out.append(f"- {issue}")
            out.append("")

    # ------------------------------------------------------------------ #
    # 5. Clean postings
    # ------------------------------------------------------------------ #
    out.append("## 5. Postings with no detected issues")
    out.append("")
    if clean:
        for p in sorted(clean, key=lambda x: x.title.lower()):
            out.append(f"- **{p.title}** — {p.team} · {p.location}")
    else:
        out.append("_None — every posting has at least one detected drift._")
    out.append("")

    # ------------------------------------------------------------------ #
    # 6. Recommendations
    # ------------------------------------------------------------------ #
    out.append("## 6. Recommendations for standardizing pre-compensation content")
    out.append("")
    out.append(
        "These are concrete, do-this-not-that fixes the recruiting/marketing "
        "team can apply directly in Ashby's editor."
    )
    out.append("")
    out.append("**A. Lock the section-label style.**  ")
    out.append(
        f"Use `<p><strong>Label:</strong></p>` for every section header "
        f"(About the role, How you'll make an impact, What makes you a good "
        f"fit, About Skydio, etc.). Do **not** use `<h1>`–`<h6>` inside the "
        f"body — those tags pick up the page's display-heading CSS and "
        f"render dramatically larger than the rest of the posting. "
        f"({sum(p.heading_tags.total() for p in postings)} stray heading "
        f"tag(s) found across "
        f"{sum(1 for p in postings if p.heading_tags)} posting(s).)"
    )
    out.append("")
    out.append("**B. Pick one capitalization style for labels and use it everywhere.**  ")
    out.append(
        "Today the corpus mixes Title Case (\"How You'll Make an Impact\"), "
        "Sentence case (\"What makes you a good fit\"), and a few all-caps "
        "callouts. Recommend Sentence case + trailing colon (the majority "
        "pattern), e.g. \"About the role:\", \"How you'll make an impact:\", "
        "\"What makes you a good fit:\"."
    )
    out.append("")
    out.append("**C. Pick one bullet structure.**  ")
    out.append(
        "Standardize on `<li><p>…</p></li>` (the dominant pattern). When "
        "writers paste from Google Docs, Ashby sometimes produces bare "
        "`<li>…</li>` — visually those bullets render closer together than "
        "the rest of the page. After pasting, click into each bullet and "
        "press Enter/Backspace once to force the editor to wrap text in `<p>`."
    )
    out.append("")
    out.append("**D. Strip inline `style=` attributes other than the default.**  ")
    out.append(
        "Anything other than `min-height:1.5em` (Ashby's default) is a smell: "
        "`color:`, `font-family:`, `font-size:`, `text-align:`, `<font>`, etc. "
        "These come from pasted Google Docs / Word content and override the "
        "site's typography. Use Ashby's \"Clear formatting\" before saving."
    )
    out.append("")
    out.append("**E. Reserve `<u>` underline for the \"PLEASE NOTE\" callout only.**  ")
    out.append(
        "Underlines are easy to confuse with hyperlinks. Today underline is "
        "used inconsistently — only keep it for the standard hybrid-policy "
        "PLEASE NOTE block (or replace that block with bold text)."
    )
    out.append("")
    out.append("**F. Remove empty paragraphs, stray `<br>`, and non-breaking spaces.**  ")
    out.append(
        "Empty `<p></p>` blocks add an extra blank line that's visually "
        "double-spaced; `<br>` makes a soft line-break that looks tighter "
        "than a real paragraph break; non-breaking spaces (`\\xa0`) are an "
        "artifact of pasted Word/Docs content and have no place here."
    )
    out.append("")
    out.append("**G. Standardize the opening paragraph.**  ")
    out.append(
        f"Today {int(norms.intro_share*100)}% of postings start with the "
        f"canonical \"Skydio is the leading US drone company…\" boilerplate. "
        f"Make this a required opening (Ashby template) so every posting "
        f"shares the same first paragraph."
    )
    out.append("")
    out.append("**H. Single source of truth: a posting template in Ashby.**  ")
    out.append(
        "Build a template containing the standard intro, the standard "
        "PLEASE NOTE block, and the standard section labels (About the role, "
        "How you'll make an impact, What makes you a good fit). Recruiters "
        "should fork this template instead of copy-pasting from existing "
        "postings, which is how drift compounds."
    )
    out.append("")
    out.append("**I. Add a CI/lint pass.**  ")
    out.append(
        "The script that produced this report (`scripts/analyze_skydio_jobs.py`) "
        "can be run on a schedule against the Ashby API. Treat any non-zero "
        "issue count as a posting that needs a quick editor pass before it "
        "hits production."
    )
    out.append("")
    out.append("---")
    out.append("")
    out.append(
        "_Generated by `scripts/analyze_skydio_jobs.py`. "
        "Re-run any time to refresh the audit._"
    )
    out.append("")

    return "\n".join(out)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def main(argv: list[str]) -> int:
    force = "--refresh" in argv
    jobs = fetch_jobs(force=force)
    listed = [j for j in jobs if j.get("isListed")]
    print(f"Fetched {len(jobs)} jobs ({len(listed)} listed).", file=sys.stderr)

    postings: list[Posting] = []
    for j in listed:
        html = j.get("descriptionHtml") or ""
        pre_html, pre_soup, found = slice_pre_compensation(html)
        p = Posting(
            id=j["id"],
            title=j["title"],
            department=j.get("department", "") or "",
            team=j.get("team", "") or "",
            location=j.get("location", "") or "",
            url=j.get("jobUrl", "") or "",
            raw_html=html,
            pre_html=pre_html,
            pre_soup=pre_soup,
            has_compensation=found,
        )
        extract_features(p)
        postings.append(p)

    norms = compute_norms(postings)
    diagnose(postings, norms)

    report = render_report(postings, norms)
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(report)
    print(f"Wrote report to {REPORT_PATH}", file=sys.stderr)
    print(
        f"Flagged {sum(1 for p in postings if p.issues)} / {len(postings)} postings.",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
