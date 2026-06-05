"""Build the human-readable formatting consistency report.

Reads /workspace/report/jobs_formatting.json and produces:
  * /workspace/report/REPORT.md   – human-shareable report
  * /workspace/report/findings.json – machine-readable summary
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

DATA = Path("/workspace/report/jobs_formatting.json")
REPORT = Path("/workspace/report/REPORT.md")
FINDINGS = Path("/workspace/report/findings.json")


def md_table(rows: list[list[str]], headers: list[str]) -> str:
    out = ["| " + " | ".join(headers) + " |",
           "| " + " | ".join("---" for _ in headers) + " |"]
    for r in rows:
        out.append("| " + " | ".join(str(x) for x in r) + " |")
    return "\n".join(out)


def main() -> None:
    jobs = json.loads(DATA.read_text())

    # =============== aggregate metrics ===============

    # 1) Section label patterns
    # Capture the *normalized* set of section labels used per posting.
    section_label_freq: Counter = Counter()
    section_label_markup_examples: dict[str, list[str]] = defaultdict(list)
    label_set_per_job: dict[str, list[str]] = {}

    # Markup forms used for section labels per job
    section_label_markup_per_job: dict[str, list[str]] = {}

    # 2) Inline styles / custom classes presence
    jobs_with_inline_styles: list[tuple[str, list[dict]]] = []
    jobs_with_extra_classes: list[tuple[str, list[dict]]] = []

    # 3) Use of real headings inside body
    jobs_with_real_headings: list[tuple[str, dict]] = []

    # 4) Bullet items style
    jobs_with_trailing_period_items: list[tuple[str, int, int]] = []
    jobs_with_leading_bold_items: list[tuple[str, int, int]] = []
    jobs_with_nested_lists: list[tuple[str, int]] = []
    jobs_with_ol: list[tuple[str, int]] = []

    # 5) Special characters
    jobs_with_nbsp: list[tuple[str, int]] = []
    jobs_with_em_dash: list[tuple[str, int]] = []

    # 6) Empty paragraphs / stray <br>
    jobs_with_empty_paragraphs: list[tuple[str, int]] = []
    jobs_with_br: list[tuple[str, int]] = []

    # 7) Body length
    body_lengths: list[tuple[str, int]] = []

    # 8) Presence vs absence of standard sections
    # Standard sections we'd expect (case-insensitive label match)
    STANDARD_LABELS = [
        "About the role",
        "How you'll make an impact",
        "What makes you a good fit",
    ]

    # 9) Block tag sequence shape
    shape_per_job: dict[str, str] = {}
    shape_counter: Counter = Counter()

    # 10) Section heading text variations
    # Many postings have a header like "How you'll make an impact:"
    # but variants are common; track them.
    label_variants: dict[str, Counter] = defaultdict(Counter)

    def display_title(j: dict) -> str:
        meta = j.get("meta") or ""
        # meta looks like "San Mateo, California, United States - Full-time"
        loc = meta.split(" - ")[0].strip() if meta else ""
        if loc:
            return f"{j['title']} *({loc})*"
        return j["title"]

    for j in jobs:
        a = j["analysis"]
        title = display_title(j)

        labels = [s["label"].rstrip(":").strip() for s in a["section_labels"]]
        markups = [s["markup"] for s in a["section_labels"]]
        label_set_per_job[title] = labels
        section_label_markup_per_job[title] = markups
        for lbl in labels:
            section_label_freq[lbl] += 1
        for lbl, mk in zip(labels, markups):
            section_label_markup_examples.setdefault(lbl, []).append(title)

        # Identify variants of standard labels
        for std in STANDARD_LABELS:
            for lbl in labels:
                if lbl.lower().startswith(std.lower().split(" ")[0]):
                    label_variants[std][lbl] += 1

        if a["inline_styles"]:
            jobs_with_inline_styles.append((title, a["inline_styles"]))
        if a["custom_classes"]:
            jobs_with_extra_classes.append((title, a["custom_classes"]))

        hc = a["heading_counts"]
        if hc:
            jobs_with_real_headings.append((title, hc))

        lif = a["list_item_features"]
        total = lif["items_total"]
        if total:
            tp = lif["items_with_trailing_period"]
            if tp > 0:
                jobs_with_trailing_period_items.append((title, tp, total))
            lb = lif["items_with_leading_strong"]
            if lb > 0:
                jobs_with_leading_bold_items.append((title, lb, total))
            if lif["items_with_nested_list"] > 0:
                jobs_with_nested_lists.append((title, lif["items_with_nested_list"]))
        if a["counts"]["ol"] > 0:
            jobs_with_ol.append((title, a["counts"]["ol"]))

        cf = a["char_features"]
        if cf.get("non_ascii_chars", 0) - cf.get("smart_quotes", 0) - cf.get("em_dashes", 0) - cf.get("en_dashes", 0) - cf.get("ellipsis_char", 0) > 0:
            pass  # other non-ascii (apostrophes, accents) – fine
        if a["counts"]["non_breaking_space"] > 0:
            jobs_with_nbsp.append((title, a["counts"]["non_breaking_space"]))
        if cf["em_dashes"] > 0:
            jobs_with_em_dash.append((title, cf["em_dashes"]))

        if a["counts"]["empty_paragraphs"] > 0:
            jobs_with_empty_paragraphs.append((title, a["counts"]["empty_paragraphs"]))
        if a["counts"]["br"] > 0:
            jobs_with_br.append((title, a["counts"]["br"]))

        body_lengths.append((title, a["text_len"]))

        # block tag sequence "shape" – simplified
        shape = " ".join(a["block_tag_sequence"])
        shape_per_job[title] = shape
        shape_counter[shape] += 1

    # Compute stats on body length
    lens = [n for _, n in body_lengths]
    median_len = sorted(lens)[len(lens) // 2] if lens else 0
    avg_len = int(sum(lens) / len(lens)) if lens else 0
    shortest = sorted(body_lengths, key=lambda x: x[1])[:8]
    longest = sorted(body_lengths, key=lambda x: -x[1])[:8]

    # Total counts
    total = len(jobs)

    # ============ build markdown report ============
    md: list[str] = []
    md.append("# Skydio Careers — Job Posting Formatting Consistency Report")
    md.append("")
    md.append(
        f"Source: https://www.skydio.com/careers — {total} open job postings analyzed "
        "(snapshot fetched 2026-06-05). Only the **pre-compensation** body of each "
        "posting (everything inside the `prose` content container up to but not "
        "including the `Compensation:` paragraph) was evaluated."
    )
    md.append("")
    md.append(
        "All Skydio job posting bodies are rendered through the same `prose "
        "block-content` CSS wrapper, so font family, base font size, line height, "
        "text color and alignment are controlled centrally and are visually "
        "identical across postings. The observable formatting inconsistencies "
        "therefore come from the **HTML/markup choices made by the content "
        "authors** when each posting was written. This report enumerates those "
        "authoring inconsistencies — they are the things that actually show up as "
        "visual differences (e.g. a bold label rendered as a `<p><strong>` vs. an "
        "`<h3>` will render at different sizes/weights), as well as the items that "
        "*don't* affect rendering but indicate inconsistent authoring discipline."
    )
    md.append("")
    md.append("---")
    md.append("")

    # -------- Summary table --------
    md.append("## 1. Executive summary")
    md.append("")
    md.append(
        "Six recurring inconsistencies were found across the 118 postings. They "
        "are listed below in roughly decreasing user-visible impact:"
    )
    md.append("")
    md.append(md_table([
        ["A", "Section headings rendered with mixed markup (`<p><strong>…:</strong></p>` vs. real `<h1>`-`<h6>`)", f"{len(jobs_with_real_headings)} / {total} postings use real headings",  "**High** – heading tags render at a different size/weight than bold paragraphs"],
        ["B", "Inconsistent / missing standard section labels (About the role / How you'll make an impact / What makes you a good fit)", f"see §3", "**High** – readers expect the same three sections in the same order"],
        ["C", "Inline `style=` attributes and custom class names inside the body", f"{len(jobs_with_inline_styles)} postings carry inline styles; {len(jobs_with_extra_classes)} carry extra classes", "**Medium** – overrides the design-system styling for one posting"],
        ["D", "Bullet items mix sentence-style punctuation (some end in '.', others don't) and mix leading bold/non-bold patterns", f"{len(jobs_with_trailing_period_items)} postings have at least one bullet ending in '.', {len(jobs_with_leading_bold_items)} use leading-bold bullets", "**Medium** – list rhythm varies"],
        ["E", "Use of `<br>`, empty paragraphs, nested lists, and ordered lists where bullets would be more consistent", f"{len(jobs_with_br)} have `<br>`, {len(jobs_with_empty_paragraphs)} have empty `<p>`, {len(jobs_with_nested_lists)} have nested lists, {len(jobs_with_ol)} use `<ol>`", "**Low–Medium** – extra vertical whitespace"],
        ["F", "Stray non-breaking spaces / em-dashes in some postings", f"{len(jobs_with_nbsp)} postings contain `&nbsp;`; {len(jobs_with_em_dash)} use em-dashes", "**Low** – author-tool artefacts"],
    ], ["#", "Inconsistency", "Where it occurs", "User-visible impact"]))
    md.append("")
    md.append(
        f"Average pre-compensation body length is ~{avg_len:,} characters "
        f"(median {median_len:,}). The shortest posting is **{shortest[0][1]:,}** "
        f"chars (*{shortest[0][0]}*); the longest is **{longest[0][1]:,}** chars "
        f"(*{longest[0][0]}*). Length itself is not necessarily a defect, but the "
        "outliers in section 6 are worth a content review."
    )
    md.append("")
    md.append("---")
    md.append("")

    # -------- Section A – heading markup --------
    md.append("## 2. Finding A — Mixed markup for section headings")
    md.append("")
    md.append(
        "Skydio's CSS styles the `prose` container so that **real `<h1>`-`<h6>` "
        "elements render at a larger size and a different weight** than a "
        "`<p><strong>...</strong></p>` bold paragraph. The vast majority of "
        f"postings ({total - len(jobs_with_real_headings)} / {total}) use the "
        "*bold paragraph* style for their section labels (e.g. `About the role:`, "
        "`How you'll make an impact:`, `What makes you a good fit:`). The "
        f"following **{len(jobs_with_real_headings)} postings break this "
        "convention** by using actual heading tags — they will appear visually "
        "*larger and heavier* than the rest of the postings, which is the most "
        "obvious eye-catching inconsistency on the site:"
    )
    md.append("")
    if jobs_with_real_headings:
        rows = []
        for title, hc in sorted(jobs_with_real_headings):
            rows.append([title, ", ".join(f"`<{t}>` ×{n}" for t, n in sorted(hc.items()))])
        md.append(md_table(rows, ["Job title", "Heading tags found in the body"]))
    else:
        md.append("_None found._")
    md.append("")
    md.append("**Fix:** Strip any `<h1>`/`<h2>`/`<h3>` elements from the job body and "
             "replace them with the standard `<p><strong>Label:</strong></p>` form.")
    md.append("")
    md.append("---")
    md.append("")

    # -------- Section B – standard sections --------
    md.append("## 3. Finding B — Missing or renamed standard section labels")
    md.append("")
    md.append(
        "The Skydio house template uses three canonical bold-paragraph section "
        "labels, in order:"
    )
    md.append("")
    md.append("1. `About the role:`")
    md.append("2. `How you'll make an impact:`")
    md.append("3. `What makes you a good fit:`")
    md.append("")
    md.append(
        "Below is how often each of these labels (and close variants) appears "
        "across the 118 postings. The variant tables group together every "
        "label that shares the leading word with the canonical phrasing — so "
        "for example `About the Team:` is listed under `About the role:` "
        "because it competes for the same template slot. Case differences and "
        "straight-quote vs. smart-quote apostrophes (`'` vs. `’`) are shown "
        "explicitly because they appear in the page source as different "
        "strings even though they look almost identical:"
    )
    md.append("")

    # For each STANDARD label, find variants
    for std in STANDARD_LABELS:
        variants = label_variants.get(std, Counter())
        present = sum(variants.values())
        md.append(f"### `{std}:` — used in {present} of {total} postings")
        if variants:
            rows = []
            for variant, n in variants.most_common():
                rows.append([f"`{variant}:`", n])
            md.append("")
            md.append(md_table(rows, ["Variant used", "# postings"]))
        else:
            md.append("_Not found in any posting._")
        md.append("")

    # Jobs that are missing one or more of the standard labels
    missing_standard: list[tuple[str, list[str]]] = []
    for j in jobs:
        labels_lower = [s["label"].rstrip(":").strip().lower() for s in j["analysis"]["section_labels"]]
        missing = []
        for std in STANDARD_LABELS:
            stem = std.lower().split(" ")[0]
            if not any(l.startswith(stem) for l in labels_lower):
                missing.append(std)
        if missing:
            missing_standard.append((display_title(j), missing))

    md.append(f"#### Postings missing one or more of the standard sections "
             f"({len(missing_standard)} / {total})")
    md.append("")
    if missing_standard:
        rows = [[t, ", ".join(f"`{m}:`" for m in miss)] for t, miss in sorted(missing_standard)]
        md.append(md_table(rows, ["Job title", "Missing standard section(s)"]))
    else:
        md.append("_All postings have all three standard sections._")
    md.append("")
    md.append(
        "**Fix:** Standardise the three labels exactly as listed above. In "
        "particular, replace variants like `What you'll do`, `Responsibilities`, "
        "`Qualifications`, `Requirements`, `Who you are`, etc. with the canonical "
        "phrasing, and add the missing sections."
    )
    md.append("")
    md.append("---")
    md.append("")

    # -------- Section C – inline styles & extra classes --------
    md.append("## 4. Finding C — Inline `style=` attributes and stray CSS classes")
    md.append("")
    md.append(
        "Every posting body should rely on the centrally-defined `prose` styling. "
        "Inline `style=` attributes and custom class names introduced inside a "
        "specific posting will override the design-system rules and create "
        "one-off visual deviations (different colors, sizes, weights, etc.)."
    )
    md.append("")
    md.append(f"### Postings with inline `style=` attributes ({len(jobs_with_inline_styles)})")
    md.append("")
    if jobs_with_inline_styles:
        rows = []
        for title, styles in sorted(jobs_with_inline_styles):
            sample = "; ".join(
                f"`<{s['tag']} style=\"{(s['style'][:80] + '…') if len(s['style'])>80 else s['style']}\">`"
                for s in styles[:3]
            )
            rows.append([title, len(styles), sample])
        md.append(md_table(rows, ["Job title", "#", "Example inline style(s)"]))
    else:
        md.append("_None._")
    md.append("")

    md.append(f"### Postings with stray CSS classes inside the body ({len(jobs_with_extra_classes)})")
    md.append("")
    if jobs_with_extra_classes:
        rows = []
        for title, classes in sorted(jobs_with_extra_classes):
            sample = "; ".join(
                f"`<{c['tag']} class=\"{c['class']}\">`" for c in classes[:3]
            )
            rows.append([title, len(classes), sample])
        md.append(md_table(rows, ["Job title", "#", "Example class(es)"]))
    else:
        md.append("_None._")
    md.append("")
    md.append(
        "**Fix:** Strip all inline `style=` attributes and remove non-`prose` "
        "class names from the rich-text content of each posting. Visual tweaks "
        "(extra spacing, color highlights, etc.) should be implemented as global "
        "rules in the design system, not as per-posting overrides."
    )
    md.append("")
    md.append("---")
    md.append("")

    # -------- Section D – bullet list inconsistencies --------
    md.append("## 5. Finding D — Inconsistent bullet-list formatting")
    md.append("")
    md.append(
        "Most postings use unordered lists whose items are short fragments "
        "without a trailing period and without leading bold text. The following "
        "postings deviate from that convention:"
    )
    md.append("")

    md.append(f"### Bullet items ending in `.` ({len(jobs_with_trailing_period_items)} postings)")
    md.append("")
    if jobs_with_trailing_period_items:
        rows = [[t, f"{n} / {tot}"] for t, n, tot in sorted(jobs_with_trailing_period_items, key=lambda x: -x[1])[:30]]
        md.append(md_table(rows, ["Job title", "Items ending in '.'"]))
        if len(jobs_with_trailing_period_items) > 30:
            md.append("")
            md.append(f"_…and {len(jobs_with_trailing_period_items)-30} more._")
    else:
        md.append("_None._")
    md.append("")

    md.append(f"### Bullet items with leading bold sub-label ({len(jobs_with_leading_bold_items)} postings)")
    md.append("")
    md.append(
        "Pattern: a list item that starts with `<strong>Sub-label:</strong>` "
        "followed by descriptive text. Most postings don't use this pattern; "
        "those that do will look 'denser' than the rest."
    )
    md.append("")
    if jobs_with_leading_bold_items:
        rows = [[t, f"{n} / {tot}"] for t, n, tot in sorted(jobs_with_leading_bold_items, key=lambda x: -x[1])[:30]]
        md.append(md_table(rows, ["Job title", "Items with leading bold"]))
        if len(jobs_with_leading_bold_items) > 30:
            md.append("")
            md.append(f"_…and {len(jobs_with_leading_bold_items)-30} more._")
    else:
        md.append("_None._")
    md.append("")

    md.append(f"### Numbered lists (`<ol>`) in the body ({len(jobs_with_ol)} postings)")
    md.append("")
    if jobs_with_ol:
        rows = [[t, n] for t, n in sorted(jobs_with_ol)]
        md.append(md_table(rows, ["Job title", "# of <ol> blocks"]))
    else:
        md.append("_None._")
    md.append("")

    md.append(f"### Nested lists inside list items ({len(jobs_with_nested_lists)} postings)")
    md.append("")
    if jobs_with_nested_lists:
        rows = [[t, n] for t, n in sorted(jobs_with_nested_lists)]
        md.append(md_table(rows, ["Job title", "# of nested lists"]))
    else:
        md.append("_None._")
    md.append("")
    md.append(
        "**Fix:** Pick one bullet style and apply it everywhere. The most common "
        "Skydio pattern is *unordered, sentence fragment, no terminal period, no "
        "leading bold*. Convert numbered lists and nested lists into a flat "
        "bulleted list where possible."
    )
    md.append("")
    md.append("---")
    md.append("")

    # -------- Section E – empty paragraphs / <br> --------
    md.append("## 6. Finding E — Stray `<br>`, empty paragraphs, and outlier lengths")
    md.append("")

    md.append(f"### Postings with `<br>` line-break tags ({len(jobs_with_br)})")
    md.append("")
    if jobs_with_br:
        rows = [[t, n] for t, n in sorted(jobs_with_br, key=lambda x: -x[1])]
        md.append(md_table(rows, ["Job title", "# of <br>"]))
    else:
        md.append("_None._")
    md.append("")

    md.append(f"### Postings with empty `<p>` paragraphs ({len(jobs_with_empty_paragraphs)})")
    md.append("")
    if jobs_with_empty_paragraphs:
        rows = [[t, n] for t, n in sorted(jobs_with_empty_paragraphs, key=lambda x: -x[1])]
        md.append(md_table(rows, ["Job title", "# of empty <p>"]))
    else:
        md.append("_None._")
    md.append("")

    md.append("### Length outliers")
    md.append("")
    md.append("**Shortest pre-compensation bodies (may be missing standard sections):**")
    md.append("")
    md.append(md_table([[t, f"{n:,}"] for t, n in shortest], ["Job title", "Chars"]))
    md.append("")
    md.append("**Longest pre-compensation bodies (may have extra/duplicate content):**")
    md.append("")
    md.append(md_table([[t, f"{n:,}"] for t, n in longest], ["Job title", "Chars"]))
    md.append("")
    md.append(
        "**Fix:** Remove `<br>` tags and empty paragraphs (the `prose` CSS "
        "already supplies vertical rhythm between block elements). Review the "
        "shortest postings to make sure they have the three standard sections."
    )
    md.append("")
    md.append("---")
    md.append("")

    # -------- Section F – special characters --------
    md.append("## 7. Finding F — Non-breaking spaces and em-dashes")
    md.append("")
    md.append(
        "These don't change the rendered font but they often originate from "
        "copy-paste out of Word / Google Docs and are worth normalising for "
        "consistency."
    )
    md.append("")

    md.append(f"### Postings containing `&nbsp;` ({len(jobs_with_nbsp)})")
    md.append("")
    if jobs_with_nbsp:
        rows = [[t, n] for t, n in sorted(jobs_with_nbsp, key=lambda x: -x[1])]
        md.append(md_table(rows, ["Job title", "# nbsp"]))
    else:
        md.append("_None._")
    md.append("")

    md.append(f"### Postings using em-dash `—` ({len(jobs_with_em_dash)})")
    md.append("")
    if jobs_with_em_dash:
        rows = [[t, n] for t, n in sorted(jobs_with_em_dash, key=lambda x: -x[1])]
        md.append(md_table(rows, ["Job title", "# em-dash"]))
    else:
        md.append("_None._")
    md.append("")
    md.append("---")
    md.append("")

    # -------- Per-posting appendix --------
    md.append("## 8. Appendix — Per-posting fingerprint (titles A–Z)")
    md.append("")
    md.append(
        "For each posting, the following table lists the standard Skydio "
        "section labels found, the markup used, and any deviations. "
        "Use this to quickly verify changes against the report."
    )
    md.append("")
    rows = []
    for j in sorted(jobs, key=lambda x: x["title"].lower()):
        a = j["analysis"]
        j_title = display_title(j)
        labels = [s["label"] for s in a["section_labels"]]
        labels_str = "; ".join(f"`{l}`" for l in labels) or "_none_"

        flags = []
        if a["heading_counts"]:
            flags.append("**real-heading**")
        if a["inline_styles"]:
            flags.append("**inline-style**")
        if a["custom_classes"]:
            flags.append("**extra-class**")
        if a["counts"]["br"]:
            flags.append("<br>")
        if a["counts"]["empty_paragraphs"]:
            flags.append("empty-p")
        if a["counts"]["ol"]:
            flags.append("<ol>")
        if a["list_item_features"]["items_with_nested_list"]:
            flags.append("nested-list")
        if a["list_item_features"]["items_with_trailing_period"]:
            flags.append("bullet-w-period")
        if a["list_item_features"]["items_with_leading_strong"]:
            flags.append("bullet-leading-bold")
        if a["counts"]["non_breaking_space"]:
            flags.append("nbsp")
        if a["char_features"]["em_dashes"]:
            flags.append("em-dash")
        flags_str = ", ".join(flags) or "—"

        rows.append([j_title, j["department"] or "—", labels_str, flags_str])
    md.append(md_table(rows, ["Title", "Department", "Section labels found", "Deviation flags"]))
    md.append("")

    # -------- Recommendations --------
    md.append("---")
    md.append("")
    md.append("## 9. Recommendations for the team")
    md.append("")
    md.append("1. **Lock the section-label template.** Every posting body should be "
             "exactly:\n\n"
             "   ```\n"
             "   <p>Intro paragraph(s) about Skydio.</p>\n"
             "   <p><strong>About the role:</strong></p>\n"
             "   <p>Role description…</p>\n"
             "   <p><strong>How you'll make an impact:</strong></p>\n"
             "   <ul><li>…</li>…</ul>\n"
             "   <p><strong>What makes you a good fit:</strong></p>\n"
             "   <ul><li>…</li>…</ul>\n"
             "   <p><strong>Compensation:</strong> …</p>\n"
             "   ```\n")
    md.append("2. **Remove real `<h1>`-`<h6>` tags from posting bodies.** Convert any "
             "existing heading-tagged section labels to the `<p><strong>` pattern so "
             "the labels render at the body font size and weight defined by the "
             "design system.")
    md.append("3. **Strip inline `style=` and custom class attributes** from all "
             "rich-text content. Visual treatments should live in the global "
             "stylesheet for `.prose`.")
    md.append("4. **Adopt one bullet convention:** unordered list, sentence fragment, "
             "no trailing period, no leading bold. Update copy where the patterns "
             "diverge.")
    md.append("5. **Replace `<br>` tags and empty `<p>` blocks** with the natural "
             "vertical rhythm of `<p>`/`<ul>` siblings.")
    md.append("6. **Normalise unicode:** strip non-breaking spaces (`&nbsp;`) and "
             "convert em-dashes (`—`) to plain hyphens or en-dashes per style guide.")
    md.append("7. **Lint at publish time.** Add an automated check in the recruiting "
             "tool that, before a posting goes live, verifies: (a) all three standard "
             "section labels are present and exactly spelled; (b) no inline styles, "
             "extra classes, `<br>`, empty `<p>`, `<ol>`, nested lists, or real "
             "headings are present; (c) list items conform to the bullet style. The "
             "script in this repository (`/workspace/scripts/analyze_jobs.py`) can be "
             "the basis for that check.")
    md.append("")

    REPORT.write_text("\n".join(md))
    print(f"Wrote report ({REPORT.stat().st_size} bytes) -> {REPORT}")

    # Write machine-readable findings too
    FINDINGS.write_text(json.dumps({
        "total_jobs": total,
        "real_headings_used_in": [t for t, _ in jobs_with_real_headings],
        "inline_styles_used_in": [t for t, _ in jobs_with_inline_styles],
        "extra_classes_used_in": [t for t, _ in jobs_with_extra_classes],
        "trailing_period_bullets_in": [t for t, _, _ in jobs_with_trailing_period_items],
        "leading_bold_bullets_in": [t for t, _, _ in jobs_with_leading_bold_items],
        "ordered_lists_used_in": [t for t, _ in jobs_with_ol],
        "nested_lists_used_in": [t for t, _ in jobs_with_nested_lists],
        "br_tags_used_in": [t for t, _ in jobs_with_br],
        "empty_paragraphs_in": [t for t, _ in jobs_with_empty_paragraphs],
        "nbsp_used_in": [t for t, _ in jobs_with_nbsp],
        "em_dashes_used_in": [t for t, _ in jobs_with_em_dash],
        "missing_standard_sections": [
            {"title": t, "missing": miss} for t, miss in missing_standard
        ],
        "label_variants_per_standard": {
            std: dict(c.most_common()) for std, c in label_variants.items()
        },
        "median_body_chars": median_len,
        "avg_body_chars": avg_len,
        "shortest_postings": shortest,
        "longest_postings": longest,
    }, indent=2))
    print(f"Wrote findings -> {FINDINGS}")


if __name__ == "__main__":
    main()
