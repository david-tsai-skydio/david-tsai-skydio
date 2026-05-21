# Skydio Careers — Job Posting Style Consistency Report

**Source:** [https://www.skydio.com/careers](https://www.skydio.com/careers)
**Scope:** All 105 unique job postings linked from the Skydio careers page, analyzing the body content (title + description) up to — and **not including** — the "Compensation at Skydio" block.
**Date generated:** May 21, 2026 (UTC)
**Total postings analyzed:** 105

---

## 1. Executive summary

The Skydio careers site renders every job posting through the same Astro/Sanity template (`type-h2` for the title, `type-body-2` for the location line, `prose block-content` for the description). Because all postings share the same global stylesheet, the *visual* font family, base font size, base line-height, default text color, alignment, and link color are **consistent across all 105 postings** by construction.

The inconsistencies are therefore not in the global CSS — they are in the **HTML/structural markup the recruiting team pastes into the description editor**. Different authors and different paste sources produce different DOM that the same CSS then styles differently. The largest visible inconsistencies are:

- **Section headings rendered at two different sizes.** 16 of 105 postings use real `<h1>`/`<h2>`/`<h3>` tags for section headers; the other 89 use a bold paragraph (`<p><strong>...</strong></p>`) as a pseudo-heading. The two styles render at clearly different font sizes and weights.
- **Inconsistent vertical spacing** between sections — 50 postings contain empty `<p></p>` elements and 42 postings contain `<br>` tags, both of which produce extra blank lines that don't appear in the rest of the corpus.
- **Inconsistent section-header punctuation** — 13 postings mix headers that end in a colon (`About the role:`) with headers that don't (`How you'll make an impact`) within the same posting.
- **A handful of structural outliers** — one posting uses literal `•` characters instead of `<ul><li>` lists, one carries a stray Word/Docs spacer `<div style="…">`, and one posting promotes section labels all the way to `<h1>`.
- **Inconsistent typography of apostrophes** — 43 postings mix straight `'` and curly `'` within the same description.

**Bottom line:** only **29 of 105** postings (~28 %) are fully clean against the most-common (modal) pattern. The remaining **76 (~72 %)** show at least one structural inconsistency that produces a visible difference in heading size, weight, or line spacing.

---

## 2. Methodology

For each posting we downloaded the rendered HTML and extracted the `div.prose.block-content` block that wraps the description. We then **truncated each prose block at the first occurrence of "Compensation"** (in any tag form), so all analysis below is of the *pre-compensation* content only.

We then computed, per posting:

- Element counts: `<p>`, `<ul>`, `<ol>`, `<li>`, `<li><p>` wrapping, `<strong>`, `<b>`, `<em>`, `<i>`, `<u>`, `<br>`, `<hr>`, `<a>`, `<h1>`–`<h6>`, `<blockquote>`, `<span>`.
- Inline style usage: `style="…"`, `font-size`, `font-weight`, `color`.
- "Pseudo-heading" usage: a `<p>` whose entire content is a single `<strong>`/`<b>`.
- Section-header text and trailing-colon pattern.
- Empty paragraphs (`<p></p>`, `<p>&nbsp;</p>`), non-breaking spaces, smart vs straight quotes, em/en-dash usage.
- Literal bullet glyphs in paragraph text (`•`, `●`, `▪`, etc.).

The full per-posting metrics are saved alongside this report (see [`data/analysis.json`](data/analysis.json) and [`data/per_posting.json`](data/per_posting.json)).

---

## 3. What "the norm" looks like

The single most common Skydio job-posting template — used by ~85 % of postings — has this DOM shape:

```html
<h1 class="type-h2">{Job title}</h1>
<p class="type-body-2">{City, State, Country} - {Full-time | Intern | Part-time}</p>

<div class="prose block-content">
  <p>Skydio is the leading US drone company and the world leader in autonomous flight … and beyond.</p>
  <p><strong>About the role:</strong></p>
  <p>{1–3 paragraphs of role context}</p>
  <p><strong>How you'll make an impact:</strong></p>
  <ul>
    <li><p>{impact bullet}</p></li>
    …
  </ul>
  <p><strong>What makes you a good fit:</strong></p>
  <ul>
    <li><p>{requirements bullet}</p></li>
    …
  </ul>
  <!-- compensation block follows -->
</div>
```

Key properties of the norm:

| Aspect | Norm |
|---|---|
| Title element | `<h1 class="type-h2">` (consistent — set by template, not author) |
| Location line | `<p class="type-body-2">` (consistent — set by template) |
| Opening paragraph | The "Skydio is the leading US drone company…" boilerplate — present in **all 105 postings (100%)** |
| Section headings | `<p><strong>Section Name:</strong></p>` — used by **89 of 105 (85%)** postings |
| Section header punctuation | Ends in `:` — used in **248 of 272** bold-paragraph headings (91%) |
| Section-header phrasing | `About the role` (78), `How you'll make an impact` (55 combined), `What makes you a good fit` (76) |
| Body paragraphs | Plain `<p>` |
| Bullet lists | `<ul><li><p>…</p></li></ul>` — used in **104 of 105 (99%)** |
| Bold markup tag | `<strong>` — used by **all 105 (100%)** (no `<b>` anywhere — this is consistent) |
| Italic / underline | Not used (consistent — 0 postings) |
| Inline `style=` attribute | Not used (consistent — only **1 outlier**) |
| Inline `color`, `font-size`, `font-weight` overrides | Not used (consistent — 0 postings) |

Because the global CSS for `.prose` is the same across all postings, postings that follow the norm above render with identical font sizes, weights, line spacing, alignment, and link color.

---

## 4. The 16 outliers — postings that visually stand out the most

These postings use real heading tags (`<h1>`/`<h2>`/`<h3>`) instead of the bold-paragraph pseudo-headings used by the rest of the site. Because the `.prose` stylesheet sizes these tags noticeably larger and bolder than a paragraph, **a candidate browsing multiple roles will immediately perceive these as "different design."**

| # | Posting | Location | Heading tags used | Why it stands out |
|---|---|---|---|---|
| 1 | Aviation Compliance Lead | San Mateo, CA | `<h2>` × 3 | Section headers are visually 1 size larger / heavier than the norm |
| 2 | Aviation Regulatory Program Manager | US Remote | `<h2>` × 3 | Same as above |
| 3 | Communications Manager | US Remote | `<h2>` × 3 | Same as above |
| 4 | Full Stack Product Counsel | San Mateo, CA | `<h3>` × 4 | Same as above |
| 5 | Hardware Engineering Program Manager | San Mateo, CA | `<h2>` × 3 + `<h3>` × 5 | **Most extreme outlier** — also introduces a secondary heading level (`<h3>`) inside each `<h2>` section, creating a multi-level hierarchy that no other posting uses |
| 6 | PhD Autonomy Engineer Intern – Planning & Controls (Reinforcement Learning) | Zurich | `<h3>` × 3 (mixed with `<p><strong>` × 2) | Mixes both heading styles within the same posting |
| 7 | Revenue Operations Engineer, Quoting Systems | San Mateo, CA | `<h2>` × 5 (mixed with `<p><strong>` × 2) | Mixes both styles; also includes `<br>` and empty `<p>` |
| 8 | Senior Business Operations Manager | San Mateo, CA | `<h3>` × 3 (mixed with `<p><strong>` × 3) | Mixes both styles |
| 9 | Senior Buyer | Hayward, CA | `<h2>` × 2 (mixed with `<p><strong>` × 1) | Mixes both styles |
| 10 | **Senior Technical Support Representative – Japan** | Tokyo | `<h1>` × 3 | **Worst single outlier** — uses `<h1>` (page-title size) for section headers, making them larger than every other posting *and* duplicating the H1 used by the job title itself |
| 11 | Software Engineer – Autonomy Infrastructure, Systems and Tools | San Mateo, CA | `<h2>` × 5 | Standalone outlier |
| 12 | Software Engineer – Autonomy Infrastructure, Systems and Tools | Zurich | `<h2>` × 5 | Standalone outlier |
| 13 | Software Engineer – Cloud Simulation & Full-Stack | San Mateo, CA | `<h2>` × 5 | Standalone outlier |
| 14 | Software Engineer – Cloud Simulation & Full-Stack | Zurich | `<h2>` × 5 | Standalone outlier |
| 15 | Software Engineer – Simulation & Robotics Engineer | San Mateo, CA | `<h3>` × 5 | Standalone outlier |
| 16 | Software Engineer – Simulation & Robotics Engineer | Zurich | `<h3>` × 5 | Standalone outlier |

> **Pattern:** the Software Engineering family of postings appears to have been authored as a batch using a different template than the rest of the engineering family.

### Other notable structural outliers

| Posting | Issue | Severity |
|---|---|---|
| **Director, Global Supply Management – Mechanicals** | The only posting in the corpus that uses literal `•` characters inside `<p>` tags instead of `<ul><li>` lists (16 bullet glyphs across two "lists"). Bullets render with no hanging indent, no spacing, no `disc` marker style. | **High** — visually unique |
| **Manager, Logistics** | Contains a stray `<div style="min-height:1.2em;margin-top:0;margin-bottom:0">` left over from a Google Docs / Word paste. It's the **only** inline `style=` attribute in the entire corpus. Renders as an extra blank line. | Medium |
| **Senior Technical Support Representative – Japan** | Also uses `<h1>` for in-body section headers (see above). | High |
| **Field Support Representative (Southwest, Remote)** | Contains **13** `&nbsp;` non-breaking spaces — by far the most in the corpus (norm is 0). Suggests heavy Word-paste residue. | Low–Medium |
| **Director, Growth Marketing – Commercial** & **IT Technician (Help Desk – Linux Focus)** | Both contain **8 `<br>` tags** (corpus norm is 0). `<br>` is used in lieu of paragraph breaks, producing tighter vertical spacing than the surrounding `<p>` blocks. | Medium |
| **Senior Product Manager, Platform & Infrastructure** & **Staff Product Manager, Platform & Infrastructure** | Each contains **6 empty `<p></p>`** elements — the most in the corpus — producing visibly larger gaps between sections than every other posting. | Medium |

---

## 5. Detailed inconsistency findings

### 5.1 Section-heading style (largest visible inconsistency)

| Style | # postings | % | Visual rendering |
|---|---|---|---|
| `<p><strong>Heading:</strong></p>` only (pseudo-heading) | 89 | 84.8 % | Body-size text, bold — about 16 px in this template |
| Real `<h1>`/`<h2>`/`<h3>` tags | 16 | 15.2 % | Larger, heavier — `<h2>` and `<h3>` in `.prose` render notably bigger than body bold |
| — of which mix `h*` and `<p><strong>` in same posting | 4 | 3.8 % | **Two different heading sizes inside the same posting** |

Heading tags used across the 16 outliers: `<h2>` × 39 occurrences, `<h3>` × 25, `<h1>` × 3.

### 5.2 Bullet-list structure

| Pattern | # postings |
|---|---|
| All `<li>` items wrapped in `<p>` (`<li><p>…</p></li>`) | 104 |
| No `<ul>`/`<ol>` lists at all — uses literal `•` characters | 1 (Director, Global Supply Management – Mechanicals) |
| Bare `<li>` items (no inner `<p>`) | 0 |
| Mixed `<li>` and `<li><p>` in same posting | 0 |

The wrapper `<p>` inside every `<li>` adds the prose paragraph's top/bottom margin to each bullet, which is why Skydio bullets render with extra vertical spacing compared with a plain unordered list — this is consistent and not a defect, but worth noting if the team prefers tighter bullets.

### 5.3 `<br>` (line-break) usage

42 of 105 postings (40 %) contain `<br>` tags; 63 don't. Where `<br>` is used, it almost always replaces a paragraph break, causing those line-breaks to render tighter than the paragraph spacing in the rest of the document.

Worst offenders: Director, Growth Marketing – Commercial (8), IT Technician (8), Autonomy Engineer – Deep Learning Infrastructure SF (8), Autonomy Engineer – Deep Learning Model Acceleration (×2) and Autonomy Engineer – Deep Learning Infrastructure Zurich (6 each), Autonomy Software Engineer (4), Software Engineer Intern Fall 2026/Winter 2027 (4), Senior Technical Recruiter – Hardware Operations (4), Revenue Operations Engineer, Quoting Systems (4), GTM Data Engineer Intern (3).

### 5.4 Empty paragraphs (`<p></p>` or `<p>&nbsp;</p>`)

50 of 105 postings (48 %) contain at least one empty paragraph. These render as a blank line and are the primary cause of inconsistent vertical spacing between sections.

| Empty `<p>` count | # postings |
|---|---|
| 0 | 55 |
| 1 | 11 |
| 2 | 14 |
| 3 | 15 |
| 4 | 3 |
| 5 | 1 |
| 6 | 2 (Senior PM Platform & Infrastructure; Staff PM Platform & Infrastructure) |

### 5.5 `&nbsp;` non-breaking spaces

27 of 105 postings contain `&nbsp;` characters that were not authored intentionally — they almost always come from pasting out of Word, Google Docs, or Pages. Worst case: **Field Support Representative (Southwest, Remote) — 13 nbsp**; Director of Product Management, DFR — 5; Senior Director, DFR — 5; Customer Success Manager, DFR Majors – Northeast — 6; Technical Support Specialist – West Coast — 5.

### 5.6 Section-header punctuation: trailing colon vs. no colon

The corpus contains 272 bold-paragraph headings overall. 248 end in `:` (91 %), 24 do not (9 %). The inconsistency surfaces *within individual postings*:

13 postings mix both forms in their own bold headings:

- Director, Growth Marketing – Commercial (4 with `:`, 1 without)
- Senior People Analytics Analyst (2 / 2)
- Enterprise Account Manager (MoD/MoI) – EMEA — Finland, Germany, Switzerland (3 / 1 each — same template re-used)
- Manager, Technical Support (4 / 1)
- Mission Success Operations Manager (3 / 1)
- Senior Brand Designer (Contract) (3 / 1)
- Senior Product Manager, Platform & Infrastructure (2 / 1)
- Senior Software Engineer, Data Platform (3 / 1)
- Staff Product Manager, Platform & Infrastructure (2 / 1)
- Success Systems Specialist (4 / 4 — even split, **worst case**)
- **Workplace Experience Coordinator Part-Time (1 with `:`, 4 without)** — inverted from the corpus norm

### 5.7 Section-header phrasing inconsistency

The same conceptual section appears under many different titles across the corpus, e.g.:

| Concept | Variants observed | Counts |
|---|---|---|
| Impact / responsibilities | "How you'll make an impact" / "How you'll make an impact" (curly vs straight apostrophe) / "How you will make an impact" / "Your impact" / "Responsibilities" / "Key responsibilities" / "Areas of responsibility" / "Day-to-day responsibilities" | 27 / 28 / 4 / 1 / 1 / 1 / 6 / 1 |
| Qualifications | "What makes you a good fit" / "What would make you a good fit" / "What makes you a strong fit" / "Qualifications" / "Preferred Qualifications" / "Minimum Qualifications" / "Nice to have" / "Bonus experience" / "Bonus points" / "Bonus points for" / "Useful skills and experience" | 76 / 8 / 4 / 7 / 3 / 1 / 3 / 6 / 5 / 4 / 2 |

This is technically a copy/content issue, not a "formatting" issue per the strict definition, but it contributes to the perception that each posting is a one-off and not part of a consistent system.

### 5.8 Apostrophe consistency (smart `'` vs straight `'`)

| Pattern | # postings |
|---|---|
| Smart apostrophe (`'`) only | 44 |
| Straight apostrophe (`'`) only | 16 |
| **Mixed within the same posting** | **43** |
| Neither (no apostrophes) | 2 |

43 of 105 postings (41 %) display visibly different apostrophe glyphs in adjacent words — e.g. "How you'll make an impact" in a heading and "you'll" in a bullet just below.

### 5.9 Bold markup tag (consistent — no action needed)

All 105 postings use `<strong>`. **0** use `<b>`. **0** mix the two. ✅

### 5.10 Inline style overrides (essentially consistent)

`font-size` overrides: **0**
`font-weight` overrides: **0**
`color` overrides: **0**
Any `style="…"` attribute at all: **1** (Manager, Logistics — the stray Google Docs spacer div)

### 5.11 Text alignment

No postings use `text-align`, `align`, or any alignment-related class. All text is left-aligned by the global `.prose` style. ✅ Consistent.

### 5.12 Hyperlink styling

All `<a>` links use the same attribute set: `target="_blank" rel="noopener noreferrer nofollow"`, no inline color or styling. They render via the same `.prose a` rule everywhere. 65 of 105 postings include the standard 4-link block (utility inspectors / first responders / soldiers / beyond) in the boilerplate opener; 40 use the unlinked variant of the same boilerplate. This is a content/template difference rather than a styling one, but it is visible because hyperlinks have a distinct color.

### 5.13 Prose length distribution

Pre-compensation prose text length ranges from **1,643 characters** (Supply Chain Intern) to **5,713 characters** (Staff Product Manager, Platform & Infrastructure). Median ≈ 2,800 characters. This is a content scope question rather than a formatting one but worth noting if the team wants comparable density across roles.

---

## 6. Per-posting characteristics — full table

Columns:

- **Heading style**: `p>strong (N)` = N pseudo-heading paragraphs; `h-tags (N)` = N real `<h*>` headings; `mixed` = both styles.
- **Bullets**: `ul/li` = proper unordered list; **`inline •`** = literal bullet glyphs in `<p>`.
- **`<br>`**, **`empty <p>`**, **`nbsp`**: counts of each artifact.
- **Flags**: short summary of issues vs the corpus norm. A `—` means the posting matches the norm on every dimension above.

| Posting | Location | Heading style | Bullets | <br> | empty <p> | nbsp | Flags |
|---|---|---|---|---|---|---|---|
| Autonomy Engineer - Deep Learning | Zurich, Switzerland | p>strong (3) | ul/li |  |  | 1 | — |
| Autonomy Engineer - Deep Learning | San Mateo, California, United States | p>strong (3) | ul/li |  |  | 1 | — |
| Autonomy Engineer - Deep Learning Infrastructure | Zurich, Switzerland | p>strong (2) | ul/li | 6 |  |  | uses 6 <br> |
| Autonomy Engineer - Deep Learning Infrastructure | San Mateo, California, United States | p>strong (1) | ul/li | 8 | 1 | 2 | uses 8 <br>, 1 empty <p> |
| Autonomy Engineer - Deep Learning Model Acceleration | Zurich, Switzerland | p>strong (2) | ul/li | 6 |  |  | uses 6 <br> |
| Autonomy Engineer - Deep Learning Model Acceleration | San Mateo, California, United States | p>strong (2) | ul/li | 6 |  |  | uses 6 <br> |
| Autonomy Engineer - Fixed Wing Planning & Controls | San Mateo, California, United States | p>strong (3) | ul/li |  |  |  | — |
| Autonomy Engineer - ML & DL Infrastructure | San Mateo, California, United States | p>strong (3) | ul/li |  | 3 |  | 3 empty <p> |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | San Mateo, California, United States | p>strong (3) | ul/li | 1 |  | 1 | uses 1 <br> |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | Zurich, Switzerland or Tampere, Finland | p>strong (3) | ul/li |  |  |  | — |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) | San Mateo, California, United States | p>strong (3) | ul/li |  |  |  | — |
| Autonomy Engineer Intern Fall 2026 | San Mateo, California, United States | p>strong (3) | ul/li |  |  | 1 | — |
| Autonomy Software Engineer | San Mateo, California, United States | p>strong (2) | ul/li | 4 |  |  | uses 4 <br> |
| **Aviation Compliance Lead** | San Mateo, California, United States | **h-tags (3)** | ul/li | 1 | 1 |  | **uses real heading tags (h2)**, uses 1 <br>, 1 empty <p> |
| **Aviation Regulatory Program Manager** | US Remote | **h-tags (3)** | ul/li |  | 2 |  | **uses real heading tags (h2)**, 2 empty <p> |
| **Communications Manager** | US Remote | **h-tags (3)** | ul/li |  | 3 |  | **uses real heading tags (h2)**, 3 empty <p> |
| Customer Success Manager, DFR Majors - Northeast | US Remote | p>strong (4) | ul/li |  |  | 6 | — |
| Deployment Engineer - Southeast | US Remote | p>strong (5) | ul/li |  | 5 |  | 5 empty <p> |
| Director of Product Management, Drone as First Responder (DFR) | San Mateo, California, United States | p>strong (3) | ul/li | 4 |  | 5 | uses 4 <br> |
| **Director, Global Supply Management - Mechanicals** | San Mateo, California, United States | p>strong (3) | **inline `•`** |  | 3 |  | **no `<ul>` bullets; uses inline '•' chars**, 3 empty <p> |
| Director, Growth Marketing - Commercial | San Mateo, California, United States | p>strong (5) | ul/li | 8 | 2 |  | uses 8 <br>, 2 empty <p>, mixes ':' / no ':' in section headers (4 vs 1) |
| Electrical Engineer (all levels) | San Mateo, California, United States | p>strong (2) | ul/li | 2 |  |  | uses 2 <br> |
| Electrical Engineer (Sustaining/Validation) | San Mateo, California, United States | p>strong (2) | ul/li | 1 |  |  | uses 1 <br> |
| Engineering Manager - Autonomy | San Mateo, California, United States | p>strong (3) | ul/li | 1 |  |  | uses 1 <br> |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Finland) | Tampere, Finland | p>strong (4) | ul/li | 2 |  |  | uses 2 <br>, mixes ':' / no ':' in section headers (3 vs 1) |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Germany) | Germany | p>strong (4) | ul/li | 2 |  |  | uses 2 <br>, mixes ':' / no ':' in section headers (3 vs 1) |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland) | Zurich, Switzerland | p>strong (4) | ul/li | 2 |  |  | uses 2 <br>, mixes ':' / no ':' in section headers (3 vs 1) |
| Enterprise Account Manager, US Army | US Remote | p>strong (3) | ul/li |  |  |  | — |
| Enterprise Account Manager, US Navy, US Marine Corps, and IC/SOCOM | US Remote | p>strong (3) | ul/li |  |  |  | — |
| Field Support Representative | US Remote | p>strong (4) | ul/li |  |  |  | — |
| Field Support Representative (Southwest, Remote) | US Remote | p>strong (3) | ul/li |  | 2 | **13** | 2 empty <p> |
| **Full Stack Product Counsel** | San Mateo, California, United States | **h-tags (4)** | ul/li |  | 3 |  | **uses real heading tags (h3)**, 3 empty <p> |
| GTM Data Engineer Intern | San Mateo, California, United States | p>strong (4) | ul/li | 3 | 2 |  | uses 3 <br>, 2 empty <p> |
| GTM Enablement Associate | San Mateo, California, United States | p>strong (3) | ul/li | 2 | 1 | 1 | uses 2 <br>, 1 empty <p> |
| **Hardware Engineering Program Manager** | San Mateo, California, United States | **h-tags (8 — h2+h3)** | ul/li |  | 3 |  | **uses real heading tags (h2,h3) — only posting with two heading levels**, 3 empty <p> |
| Hardware Operations Program Manager | Hayward, California, United States | p>strong (3) | ul/li |  | 3 |  | 3 empty <p> |
| Hardware Technician | San Mateo, California, United States | p>strong (2) | ul/li |  | 3 |  | 3 empty <p> |
| Head of Warehouse & Logistics Operations | US CA Production | p>strong (2) | ul/li | 1 | 2 |  | uses 1 <br>, 2 empty <p> |
| IT Technician (Help Desk - Linux Focus) | Hayward, California, United States | p>strong (5) | ul/li | 8 | 2 |  | uses 8 <br>, 2 empty <p> |
| Lead Staff Electrical Engineer (F10 Program) | San Mateo, California, United States | p>strong (2) | ul/li | 1 | 2 | 2 | uses 1 <br>, 2 empty <p> |
| **Manager, Logistics** | US CA Production | p>strong (3) | ul/li |  | 2 | 1 | **inline `style=` attribute (only posting in corpus)**, 2 empty <p> |
| Manager, Technical Support | US CA San Mateo | p>strong (5) | ul/li |  |  |  | mixes ':' / no ':' in section headers (4 vs 1) |
| Mission Success Operations Manager | US Remote | p>strong (4) | ul/li |  |  |  | mixes ':' / no ':' in section headers (3 vs 1) |
| PCB Layout Engineer | San Mateo, California, United States | p>strong (2) | ul/li | 2 |  | 2 | uses 2 <br> |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | San Mateo, California, United States | p>strong (3) | ul/li | 1 |  | 1 | uses 1 <br> |
| **PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning)** | Zurich, Switzerland | **mixed (h*=3, p>strong=2)** | ul/li |  |  | 1 | **uses real heading tags (h3) and bold-paragraph headings in the same posting** |
| Product Design Engineer (All Levels) | San Mateo, California, United States | p>strong (2) | ul/li | 1 |  | 1 | uses 1 <br> |
| Product Support Engineer | San Mateo, California, United States | p>strong (2) | ul/li | 2 | 2 |  | uses 2 <br>, 2 empty <p> |
| Product Support Engineer Intern | San Mateo, California, United States | p>strong (2) | ul/li | 2 | 3 |  | uses 2 <br>, 3 empty <p> |
| Production Manager, PM Shift | Hayward, California, United States | p>strong (3) | ul/li |  | 3 |  | 3 empty <p> |
| Program Manager, Major Deployments (Hawaii) | San Mateo, California, United States | p>strong (3) | ul/li |  | 3 |  | 3 empty <p> |
| Program Manager, Major Deployments (Mid Atlantic) | US Remote | p>strong (3) | ul/li |  | 3 |  | 3 empty <p> |
| **Revenue Operations Engineer, Quoting Systems** | San Mateo, California, United States | **mixed (h*=5, p>strong=2)** | ul/li | 4 | 2 |  | **uses real heading tags (h2)**, uses 4 <br>, 2 empty <p> |
| RF Design Engineer | San Mateo, California, United States | p>strong (3) | ul/li |  |  |  | — |
| Sales Planning Analyst Intern | San Mateo, California, United States | p>strong (2) | ul/li | 1 | 1 |  | uses 1 <br>, 1 empty <p> |
| Senior Autonomy Engineer - Controls | San Mateo, California, United States | p>strong (3) | ul/li |  |  |  | — |
| Senior Autonomy Engineer - Deep Learning | San Mateo, California, United States | p>strong (2) | ul/li | 2 | 1 | 1 | uses 2 <br>, 1 empty <p> |
| Senior Autonomy Engineer - Deep Learning | Zurich, Switzerland | p>strong (2) | ul/li | 2 |  | 1 | uses 2 <br> |
| Senior Brand Designer (Contract) | San Mateo, California, United States | p>strong (4) | ul/li | 2 | 3 |  | uses 2 <br>, 3 empty <p>, mixes ':' / no ':' in section headers (3 vs 1) |
| **Senior Business Operations Manager** | San Mateo, California, United States | **mixed (h*=3, p>strong=3)** | ul/li |  | 3 |  | **uses real heading tags (h3)**, 3 empty <p> |
| **Senior Buyer** | Hayward, California, United States | **mixed (h*=2, p>strong=1)** | ul/li |  | 3 |  | **uses real heading tags (h2)**, 3 empty <p> |
| Senior Customer Support Representative - India | Bangalore, India | p>strong (3) | ul/li |  | 1 |  | 1 empty <p> |
| Senior Director, Product Management, Drone as First Responder (DFR) | San Mateo, California, United States | p>strong (3) | ul/li | 2 |  | 5 | uses 2 <br> |
| Senior Hardware Test and Reliability Engineer | San Mateo, California, United States | p>strong (3) | ul/li |  |  |  | — |
| Senior NPI Product Quality Engineer | San Mateo, California, United States | p>strong (3) | ul/li |  |  |  | — |
| Senior People Analytics Analyst | San Mateo, California, United States | p>strong (4) | ul/li |  |  |  | mixes ':' / no ':' in section headers (2 vs 2) |
| Senior Product Manager, Platform & Infrastructure | San Mateo, California, United States | p>strong (3) | ul/li | 1 | **6** |  | uses 1 <br>, **6 empty <p>**, mixes ':' / no ':' in section headers (2 vs 1) |
| Senior Revenue Operations Manager | San Mateo, California, United States | p>strong (4) | ul/li |  | 2 |  | 2 empty <p> |
| Senior RF Design Engineer | San Mateo, California, United States | p>strong (3) | ul/li |  | 2 |  | 2 empty <p> |
| Senior Software Engineer - Embedded | San Mateo, California, United States | p>strong (4) | ul/li |  |  | 3 | — |
| Senior Software Engineer - Mobile Platform | San Mateo, California, United States | p>strong (5) | ul/li |  | 3 |  | 3 empty <p> |
| Senior Software Engineer - Security | San Mateo, California, United States | p>strong (4) | ul/li |  |  |  | — |
| Senior Software Engineer, Data Platform | San Mateo, California, United States | p>strong (4) | ul/li | 1 |  |  | uses 1 <br>, mixes ':' / no ':' in section headers (3 vs 1) |
| Senior Software Engineer, Frontend | San Mateo, California, United States | p>strong (5) | ul/li |  |  |  | — |
| Senior Software Engineer, Full Stack | San Mateo, California, United States | p>strong (5) | ul/li | 1 |  |  | uses 1 <br> |
| Senior Software Engineer, Infrastructure | San Mateo, California, United States | p>strong (3) | ul/li |  |  |  | — |
| Senior Technical Recruiter | San Mateo, California, United States | p>strong (2) | ul/li | 2 |  | 1 | uses 2 <br> |
| Senior Technical Recruiter - Hardware Operations | San Mateo, California, United States | p>strong (2) | ul/li | 4 |  | 1 | uses 4 <br> |
| **Senior Technical Support Representative - Japan** | Tokyo, Japan | **h-tags (3 — `<h1>`!)** | ul/li | 2 | 1 |  | **uses `<h1>` for section headers — the only posting in the corpus that does this**, uses 2 <br>, 1 empty <p> |
| Senior Wireless Systems Performance Engineer | San Mateo, California, United States | p>strong (3) | ul/li |  |  | 4 | — |
| Senior/Staff Embedded Software Engineer – Camera Systems | San Mateo, California, United States | p>strong (4) | ul/li |  | 4 |  | 4 empty <p> |
| **Software Engineer - Autonomy Infrastructure, Systems and Tools** | San Mateo, California, United States | **h-tags (5)** | ul/li |  | 1 |  | **uses real heading tags (h2)**, 1 empty <p> |
| **Software Engineer - Autonomy Infrastructure, Systems and Tools** | Zurich, Switzerland | **h-tags (5)** | ul/li |  | 1 |  | **uses real heading tags (h2)**, 1 empty <p> |
| **Software Engineer - Cloud Simulation & Full-Stack** | San Mateo, California, United States | **h-tags (5)** | ul/li |  | 2 |  | **uses real heading tags (h2)**, 2 empty <p> |
| **Software Engineer - Cloud Simulation & Full-Stack** | Zurich, Switzerland | **h-tags (5)** | ul/li |  | 2 |  | **uses real heading tags (h2)**, 2 empty <p> |
| Software Engineer - Embedded | San Mateo, California, United States | p>strong (4) | ul/li |  |  | 3 | — |
| Software Engineer - Infrastructure | San Mateo, California, United States | p>strong (3) | ul/li |  |  |  | — |
| **Software Engineer - Simulation & Robotics Engineer** | San Mateo, California, United States | **h-tags (5)** | ul/li |  | 2 |  | **uses real heading tags (h3)**, 2 empty <p> |
| **Software Engineer - Simulation & Robotics Engineer** | Zurich, Switzerland | **h-tags (5)** | ul/li |  | 2 |  | **uses real heading tags (h3)**, 2 empty <p> |
| Software Engineer Intern Fall 2026/Winter 2027 | US CA San Mateo | p>strong (2) | ul/li | 4 | 1 |  | uses 4 <br>, 1 empty <p> |
| Software Engineer, Full Stack | San Mateo, California, United States | p>strong (5) | ul/li |  |  |  | — |
| Sr/Staff Embedded Software Engineer - Camera Systems | Tampere, Finland | p>strong (4) | ul/li |  | 4 |  | 4 empty <p> |
| Staff Global Supply Manager, Mechanicals | San Mateo, California, United States | p>strong (2) | ul/li | 1 | 1 |  | uses 1 <br>, 1 empty <p> |
| Staff Product Manager, Platform & Infrastructure | San Mateo, California, United States | p>strong (3) | ul/li | 1 | **6** |  | uses 1 <br>, **6 empty <p>**, mixes ':' / no ':' in section headers (2 vs 1) |
| Staff Software Engineer - Embedded | San Mateo, California, United States | p>strong (4) | ul/li |  |  | 3 | — |
| Staff Software Engineer, Frontend | San Mateo, California, United States | p>strong (4) | ul/li |  |  |  | — |
| Staff Software Engineer, Full Stack | San Mateo, California, United States | p>strong (4) | ul/li |  |  |  | — |
| Staff Technical Recruiter | San Mateo, California, United States | p>strong (3) | ul/li |  |  | 1 | — |
| Success Systems Specialist | US Remote | p>strong (8) | ul/li |  | 1 |  | 1 empty <p>, **mixes ':' / no ':' in section headers (4 vs 4 — worst case)** |
| Supplier Quality Engineer, Sustaining | Taiwan | p>strong (3) | ul/li |  | 1 |  | 1 empty <p> |
| Supply Chain Intern | San Mateo, California, United States | p>strong (2) | ul/li | 2 |  |  | uses 2 <br> |
| Systems Integration and Test Engineer (Mid to Senior Level) | San Mateo, California, United States | p>strong (3) | ul/li |  |  |  | — |
| Technical Support Specialist - West Coast | US Remote | p>strong (4) | ul/li |  |  | 5 | — |
| Wireless Software Engineer | San Mateo, California, United States | p>strong (3) | ul/li |  |  | 1 | — |
| Workplace Experience Coordinator Part-Time | Zurich, Switzerland | p>strong (5) | ul/li | 1 | 1 |  | uses 1 <br>, 1 empty <p>, mixes ':' / no ':' in section headers (**1 with `:`, 4 without** — inverted from norm) |

**Postings with no flagged inconsistencies (29 of 105):** Autonomy Engineer - Deep Learning (×2), Autonomy Engineer - Fixed Wing Planning & Controls, Autonomy Engineer Intern - Deep Learning (Computational Photography) (×2), Autonomy Engineer Intern Fall 2026, Customer Success Manager DFR Majors - Northeast, Enterprise Account Manager US Army, Enterprise Account Manager US Navy/USMC/IC-SOCOM, Field Support Representative, RF Design Engineer, Senior Autonomy Engineer - Controls, Senior Hardware Test and Reliability Engineer, Senior NPI Product Quality Engineer, Senior Software Engineer - Embedded, Senior Software Engineer - Security, Senior Software Engineer, Frontend, Senior Software Engineer, Infrastructure, Senior Wireless Systems Performance Engineer, Software Engineer - Embedded, Software Engineer - Infrastructure, Software Engineer, Full Stack, Staff Software Engineer - Embedded, Staff Software Engineer, Frontend, Staff Software Engineer, Full Stack, Staff Technical Recruiter, Systems Integration and Test Engineer (Mid to Senior Level), Technical Support Specialist - West Coast, Wireless Software Engineer.

---

## 7. Specific issues to fix (actionable list)

Ranked roughly by visual impact:

1. **Reformat the 16 postings that use `<h1>`/`<h2>`/`<h3>` tags into the standard `<p><strong>Heading:</strong></p>` pattern.** This is the largest visible inconsistency on the site. Affected postings: Aviation Compliance Lead; Aviation Regulatory Program Manager; Communications Manager; Full Stack Product Counsel; Hardware Engineering Program Manager; PhD Autonomy Engineer Intern - Planning & Controls; Revenue Operations Engineer, Quoting Systems; Senior Business Operations Manager; Senior Buyer; **Senior Technical Support Representative - Japan (highest priority — uses `<h1>`)**; the four Software Engineer - Autonomy Infrastructure / Cloud Simulation roles; and the two Software Engineer - Simulation & Robotics Engineer roles.

2. **Remove the inline `style="min-height:1.2em;…"` div from "Manager, Logistics".** It's the only inline style anywhere on the site and produces an extra blank line.

3. **Rebuild the bullet section in "Director, Global Supply Management - Mechanicals" as a real `<ul><li>` list.** Currently it uses 16 literal `•` characters in paragraphs, making the bullets look visually different (no indent, no marker color, no hang) from every other posting.

4. **Strip empty `<p></p>` elements from 50 postings.** Priority targets (6 empty paragraphs each): Senior Product Manager, Platform & Infrastructure and Staff Product Manager, Platform & Infrastructure. Next tier (5): Deployment Engineer - Southeast.

5. **Replace `<br>` line-breaks with paragraph breaks in 42 postings.** Priority targets (8 each): Director, Growth Marketing - Commercial; IT Technician (Help Desk - Linux Focus); Autonomy Engineer - Deep Learning Infrastructure (SF).

6. **Standardize section-header punctuation** — pick either always-colon or never-colon as the house style and apply it. Since 91 % of the corpus already uses trailing colons, *always-colon* is the lower-friction choice.  
   At minimum, fix the 13 postings that mix both forms within themselves, and explicitly the inverted one: **Workplace Experience Coordinator Part-Time** (1 with colon, 4 without).

7. **Strip `&nbsp;` non-breaking spaces** introduced by Word/Docs paste. 27 postings affected; worst is Field Support Representative (Southwest, Remote) with 13.

8. **Pick one apostrophe style (curly `'` recommended, since 87 of 103 quoted postings already use it)** and normalize. 43 postings currently mix straight and curly in the same description.

9. **Standardize section-header vocabulary.** Pick one canonical name per section (recommended: "About the role", "How you'll make an impact", "What makes you a good fit") and remove the long tail of one-off variants ("Areas of responsibility", "Day-to-day responsibilities", "Useful skills and experience", "Bonus experience", "Bonus points for…", etc.).

---

## 8. Recommendations for standardizing going forward

### 8.1 Publish a Skydio job-posting style template

Make a copy of the modal HTML in section 3 the official template that every recruiter starts from. Store it in the recruiting wiki / Notion as both Markdown *and* the rendered HTML that the Sanity-backed CMS will accept. Authors should never need to invent the markup themselves.

### 8.2 Enforce one heading style

Pick **one** of:

- **Option A (matches today's majority — recommended):** Use `<p><strong>Heading:</strong></p>` for in-body section headers. Pro: no template change needed and 89 of 105 postings already comply. Con: section headers are not semantic headings, which is mildly worse for screen readers and SEO.
- **Option B (semantic — recommended if a small CMS-side change is on the table):** Update the `.prose` CSS so that `h2` and `h3` inside `.prose` render at the same visual weight/size as `<p><strong>`, and switch everything to `<h2>`/`<h3>`. This preserves accessibility and produces identical visual output. Then migrate the 89 bold-paragraph postings.

Either choice is fine — what matters is that one of them is enforced consistently.

### 8.3 Tighten the editor / CMS

If postings are authored in a rich-text editor that backs the Sanity store, configure it to:

- Strip `<br>` on paste (convert to paragraph breaks).
- Strip empty paragraphs on save.
- Strip `&nbsp;` and `style=` attributes on paste.
- Force one heading style (per 8.2).
- Auto-normalize quotes/apostrophes to one form on save (Sanity has a `transform` hook for this).

Most modern CMS editors (Sanity Studio with `portableText` + a sanitizer) support this with a small custom plugin.

### 8.4 Add a pre-publish lint

A small CI check that compares any newly authored posting against the rules in section 7 (no `<h*>` outside the page-level `h1`, no `<br>` inside `.prose`, no empty `<p>`, no inline `style=`, no literal `•` in `<p>`, no mixed apostrophes, no mixed colon/no-colon section headers) would prevent regressions and surface every issue in this report as a build failure rather than a live page.

### 8.5 Author-facing checklist

Add a short pre-publish checklist to the posting workflow:

- [ ] Standard opening paragraph present?
- [ ] Section headers use the exact wording: *About the role / How you'll make an impact / What makes you a good fit*?
- [ ] All section headers end with `:`?
- [ ] All bullets are real list items (no `•` glyphs typed into paragraphs)?
- [ ] No empty paragraphs left between sections?
- [ ] Posting was authored directly in the CMS (not pasted from Google Docs / Word)?

---

## 9. Caveats

- This analysis is based on the **rendered HTML** of each posting, not the underlying Sanity / CMS source. The mappings between the source DSL and the rendered HTML are not visible from outside, so individual fixes need to be made in whatever editor the recruiting team uses.
- "Pre-compensation" was determined by cutting each posting at the first occurrence of the word *Compensation* inside a heading or bold paragraph. A small number of postings may also have role-specific compensation language earlier in the body — those edge cases are noted as outliers, not as corpus norms.
- All postings were fetched once on May 21, 2026; the site is updated frequently, so a re-run is recommended before any large fix-up campaign.

---

## Appendix — files produced alongside this report

- `data/analysis.json` — full per-posting structural metrics (JSON)
- `data/per_posting.json` — per-posting issue summary (JSON)
- `data/prose_excerpts/<job-id>.html` — each posting's prose, truncated at the compensation block (raw HTML, for spot-checking)
- `scripts/parse_jobs.py` — the extraction script
- `scripts/drill_down.py` — the inconsistency-drill-down script
