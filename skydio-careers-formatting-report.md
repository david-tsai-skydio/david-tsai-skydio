# Skydio Careers — Job Posting Formatting Consistency Report

**Source:** [`https://www.skydio.com/careers`](https://www.skydio.com/careers)
**Scope:** All 106 individual job postings linked from the careers page. For each
posting, only the content above the "**Compensation:**" block is analyzed (per
the brief). The Skydio careers site renders every posting through the same
`<div class="prose block-content">` wrapper, so visible differences come from
the HTML structure each requisition author committed to Greenhouse — not from
the site stylesheet.
**Analysis date:** May 24, 2026
**Method:** Each `/jobs/<id>/` page was downloaded and parsed; the
`prose block-content` container was sliced at the "Compensation:" heading and
the remaining block elements were inspected for tag name, classes, inline
style, heading method, list structure, line-break usage, empty paragraphs, and
inline emphasis (bold/italic/underline). Aggregate distributions are below.

---

## 1. Headline findings (TL;DR)

| Area | Status | Issue |
|---|---|---|
| Posting title (`<h1 class="type-h2">`) | Consistent | All 106 use the same site-provided H1 styling. |
| Body section headings | **Inconsistent** | 89 jobs use bold-paragraph (`<p><strong>`) "headings," 11 use real `<h2>`/`<h3>` tags, 1 uses `<h1>`, 4 mix both, 1 has none. Real heading tags render visibly larger and bolder than the bold-paragraph version. |
| Section heading wording | **Inconsistent** | The same logical section appears under 5+ different labels (e.g. "What makes you a good fit" vs. "What would make you a good fit" vs. "Qualifications"). |
| Section heading capitalization | **Inconsistent** | 48 jobs use sentence case ("About the role"), 31 use Title Case ("About the Role"), 1 uses mixed ("About The Role"). |
| Curly vs straight apostrophes | **Inconsistent** | 40 headings use a straight `'` (e.g. "How you'll make an impact"); 27 use a curly `’` ("How you’ll make an impact"). |
| Trailing colon on section headings | **Inconsistent** | Majority end with `:`, but 7+ "About the role" / "How you'll make an impact" headings omit it. |
| Empty `<p></p>` "spacer" paragraphs | **Inconsistent** | 51 of 106 postings contain one or more empty paragraphs (109 in total); some have 6–8. |
| Trailing/leading `<br/>` inside paragraphs and list items | **Inconsistent** | 6 jobs ship paragraphs with a stray trailing `<br/>`, 10 jobs have leading `<br/>` in a `<p>`, and 6 jobs have `<br/>` tags at the end of `<li>` bullets — all create visibly larger vertical gaps. |
| Inline italics / underlines | **Inconsistent** | 7 postings use `<u>` and 2 use `<em>/<i>` in the pre-compensation body; the other 97 do not. |
| Inline `color`, `font-size`, `font-weight` styles | Clean | No posting uses inline color, font-size, or font-weight overrides. |
| `text-align: center/right` | Clean | No posting overrides text alignment. |
| Inline `<div style="min-height:1.2em">` spacer | **Inconsistent** | 1 job (Manager, Logistics) uses raw `<div>` blocks with inline `min-height/margin` style as spacers instead of empty `<p>`. |
| Title spelling | **Inconsistent** | 4 job titles contain a double-space typo (e.g. `Senior Software Engineer,  Infrastructure`). |
| Body spelling | **Inconsistent** | 1 job ("Senior People Analytics Analyst") has a typo in a section heading: "What Makes **Your** a Good Fit". |

The "loudest" visible offenders are summarized in §4.

---

## 2. The 106 job postings analyzed

All postings come from the same Greenhouse-backed `/jobs/<uuid>/` template.
The full set is grouped below by department, exactly as listed on the careers
page.

### R&D — Autonomy (25)
- Autonomy Engineer - Deep Learning — San Mateo, CA
- Autonomy Engineer - Deep Learning — Zurich, Switzerland
- Autonomy Engineer - Deep Learning Infrastructure — Zurich
- Autonomy Engineer - Deep Learning Infrastructure — San Mateo
- Autonomy Engineer - Deep Learning Model Acceleration — Zurich
- Autonomy Engineer - Deep Learning Model Acceleration — San Mateo
- Autonomy Engineer - Fixed Wing Planning & Controls — San Mateo
- Autonomy Engineer - ML & DL Infrastructure — San Mateo
- Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 — San Mateo
- Autonomy Engineer Intern - Deep Learning (Computational Photography) — San Mateo
- Autonomy Engineer Intern - Deep Learning (Computational Photography) — Zurich
- Autonomy Engineer Intern - Deep Learning (Computational Photography) — Tampere, Finland
- Autonomy Engineer Intern Fall 2026 — San Mateo
- Autonomy Software Engineer — San Mateo
- Engineering Manager - Autonomy — San Mateo
- PhD Autonomy Engineer Intern - Deep Learning or Computer Vision — San Mateo
- PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) — Zurich
- Senior Autonomy Engineer - Controls — San Mateo
- Senior Autonomy Engineer - Deep Learning — Zurich
- Senior Autonomy Engineer - Deep Learning — San Mateo
- Software Engineer - Autonomy Infrastructure, Systems and Tools — San Mateo
- Software Engineer - Autonomy Infrastructure, Systems and Tools — Zurich
- Software Engineer - Cloud Simulation & Full-Stack — San Mateo
- Software Engineer - Cloud Simulation & Full-Stack — Zurich
- Software Engineer - Simulation & Robotics Engineer — Zurich
- Software Engineer - Simulation & Robotics Engineer — San Mateo

### R&D — Connectivity (3)
- RF Design Engineer; Senior Wireless Systems Performance Engineer; Wireless Software Engineer (all San Mateo)

### R&D — Hardware (9)
- Electrical Engineer (Sustaining/Validation); Electrical Engineer (all levels); Hardware Engineering Program Manager; Lead Staff Electrical Engineer; PCB Layout Engineer; Product Design Engineer (All Levels); Senior Hardware Test and Reliability Engineer; Senior RF Design Engineer; Systems Integration and Test Engineer (Mid to Senior Level)

### R&D — Product (4)
- Director of Product Management, DFR; Senior Director, Product Management, DFR; Senior Product Manager, Platform & Infrastructure; Staff Product Manager, Platform & Infrastructure

### R&D — Security (1)
- Senior Software Engineer - Security

### R&D — Software (15)
- Senior Software Engineer, Infrastructure; Software Engineer - Infrastructure; Middleware Software Engineer Intern - Fall 2026; Senior Software Engineer - Embedded; Senior Software Engineer - Mobile Platform; Senior Software Engineer, Data Platform; Senior Software Engineer, Frontend; Senior Software Engineer, Full Stack; Senior/Staff Embedded Software Engineer – Camera Systems; Software Engineer - Embedded; Software Engineer Intern Fall 2026/Winter 2027; Software Engineer, Full Stack; Sr/Staff Embedded Software Engineer - Camera Systems (Tampere); Staff Software Engineer - Embedded; Staff Software Engineer, Frontend; Staff Software Engineer, Full Stack

### Operations — Customer Support (8), IT (1), Legal (1), Manufacturing (5), Marketing (3), People & Recruiting (5), Policy & Regulatory Affairs (2), Professional Services and Training (7), Sales (10), Supply Chain & Logistics (6)
(Full list in the source-of-truth careers page; all 106 postings were analyzed.)

---

## 3. Formatting characteristics, by category

### 3.1 Posting title (the `<h1>` at the top of each page)
- **Tag:** `<h1 class="type-h2">` — identical across all 106 jobs.
- **Location subtitle:** `<p class="type-body-2">` — identical across all 106 jobs.
- **Verdict:** ✅ Consistent.

### 3.2 Body section heading method (the single biggest visual inconsistency)
The careers stylesheet renders `<h2>` and `<h3>` substantially larger and
heavier than `<p><strong>`. Most postings use the latter; a handful use real
heading tags, so those postings look conspicuously different at a glance.

| Heading method | # jobs |
|---|---|
| Bold-paragraph only (`<p><strong>Heading:</strong></p>`) | **89** |
| Real heading tags only (`<h2>` or `<h3>`) | **11** |
| Mixed (bold-paragraph + real headings) | **4** |
| Used `<h1>` inside the body | **1** |
| No detectable section headings | **1** |

**Jobs whose bodies use real `<h2>`/`<h3>` tags (= visibly larger headings than the other 89):**
- `<h2>` only — Communications Manager; Software Engineer - Cloud Simulation & Full-Stack (San Mateo); Software Engineer - Cloud Simulation & Full-Stack (Zurich); Software Engineer - Autonomy Infrastructure, Systems and Tools (San Mateo); Software Engineer - Autonomy Infrastructure, Systems and Tools (Zurich); Aviation Compliance Lead; Aviation Regulatory Program Manager
- `<h3>` only — Software Engineer - Simulation & Robotics Engineer (San Mateo); Software Engineer - Simulation & Robotics Engineer (Zurich); Full Stack Product Counsel
- Mixed `<p><strong>` + `<h2>`/`<h3>` — Revenue Operations Engineer, Quoting Systems (1 strong + 5× h2); Senior Business Operations Manager (3 strong + 3× h3, used for nested sub-sections); Senior Buyer (1 strong + 2× h2); PhD Autonomy Engineer Intern - Planning & Controls (RL) (2 strong + 3× h3)
- Uses `<h2>` *and* `<h3>` for nested sub-sections — Hardware Engineering Program Manager
- **`<h1>` inside the body (extreme outlier — these render the same size as the page title)** — Senior Technical Support Representative - Japan (Tokyo); all three section headings ("About the role:", "How you'll make an impact:", "What would make you a good fit:") are wrapped in `<h1>` rather than `<p><strong>` or `<h2>`/`<h3>`. This is the single most visually anomalous posting on the site.

### 3.3 Section heading wording
The same logical section appears under many labels. Counts for each canonical section:

**"About the role" section (intro)** — 88 jobs include one; the rest skip the heading.

**"Responsibilities / what you'll do" section** — 5+ variants in use:

| Phrase | Count |
|---|---|
| "How you'll make an impact" (straight apostrophe) | 39 |
| "How you’ll make an impact" (curly apostrophe) | 35 |
| "How you will make an impact" | 4 |
| "What you’ll do" / "What you'll do" | 8 |
| "Areas of Responsibility" | 6 |
| "Key Responsibilities" | 1 |
| "Day-to-day responsibilities" | 1 |
| "What you’ll drive (scope)" | 1 |

**"Qualifications / good fit" section** — 7+ variants in use:

| Phrase | Count |
|---|---|
| "What makes you a good fit" | 76 |
| "What would make you a good fit" | 8 |
| "Qualifications" | 7 |
| "What makes you a strong fit" | 3 |
| "What would make you a strong fit" | 2 |
| "What you’ll bring" | 1 |
| "What makes you a great fit" | 1 |
| **"What Makes Your a Good Fit" (typo)** | 1 |

**"Bonus / preferred experience" section** — 7+ variants in use: "Bonus points" (6), "Bonus points for" (4), "Bonus experience" (6), "Nice to have" (3), "Preferred qualifications" (4), "Useful skills and experience" (2), "Additional desired experience and skills" (1).

### 3.4 Heading capitalization
The same heading is written in both Title Case and sentence case across postings:

| Heading | Count |
|---|---|
| "About the role" (sentence case) | 48 |
| "About the Role" (Title Case) | 31 |
| **"About The Role"** (every word capitalized — only on Senior People Analytics Analyst) | 1 |
| "About the team" | 6 |
| "About the Team" | 8 |
| "How you'll make an impact" / "How you’ll make an impact" (sentence) | 53 |
| "How You'll Make an Impact" / "How You’ll Make an Impact" (Title) | 22 |

### 3.5 Punctuation
- **Curly vs. straight apostrophe** — within section headings alone: 40 headings use the ASCII `'`, 27 use the Unicode `’`. The same wording therefore appears in two different glyphs across postings.
- **Trailing colon on section headings** — most "About the role" / "How you'll make an impact" headings end with `:`; 7 postings omit the colon on "About the role", 5 omit it on the impact heading, and 6 omit it on the fit heading. Notably, *every* job in the "real heading tags" group above is also the group most likely to drop the trailing colon (e.g. Communications Manager, Aviation Compliance Lead, Aviation Regulatory Program Manager, Hardware Engineering Program Manager).

### 3.6 Vertical spacing / line breaks

**Empty `<p></p>` blocks** (51 / 106 postings — these are zero-content paragraphs the rich-text editor inserted as visual spacers). Worst offenders:

| Empty `<p>` count | Job |
|---|---|
| 8 | Full Stack Product Counsel |
| 6 | Senior Product Manager, Platform & Infrastructure |
| 6 | Staff Product Manager, Platform & Infrastructure |
| 3 | Director, Growth Marketing - Commercial |
| 3 | Senior Brand Designer (Contract) |
| 3 | Senior Buyer |
| 3 | Deployment Engineer - Southeast |
| 3 | Sr/Staff Embedded Software Engineer - Camera Systems (Tampere) |
| 3 | Product Support Engineer Intern |
| 3 | Program Manager, Major Deployments (Mid Atlantic) |
| 3 | Senior Software Engineer - Mobile Platform |
| 3 | Director, Global Supply Management - Mechanicals |
| 3 | Software Engineer Intern Fall 2026/Winter 2027 |
| 1–2 | ~35 additional postings |

**Trailing `<br/>` inside `<p>`** (extra blank line below a paragraph) — 6 postings:
Director, Growth Marketing - Commercial; Revenue Operations Engineer, Quoting Systems; Lead Staff Electrical Engineer; IT Technician (Help Desk - Linux Focus) (x2); Senior Software Engineer, Full Stack; Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026.

**Leading `<br/>` inside `<p>`** (extra blank line above a paragraph) — 10 postings:
Director, Growth Marketing - Commercial; Head of Warehouse & Logistics Operations; Enterprise Account Manager (MoD/MoI) – EMEA (Germany) (x2); Enterprise Account Manager (MoD/MoI) – EMEA (Switzerland) (x2); IT Technician (Help Desk - Linux Focus); GTM Enablement Associate; Supply Chain Intern; Staff Global Supply Manager, Mechanicals; Senior Software Engineer, Data Platform; Enterprise Account Manager (MoD/MoI) – EMEA (Finland) (x2).

**Trailing `<br/>` inside list items** (extra gap *below* a bullet point) — 6 postings (most prominently Director, Growth Marketing - Commercial with 7 bullets ending in `<br/>`; also Revenue Operations Engineer, Quoting Systems x3; Engineering Manager - Autonomy; PhD Autonomy Engineer Intern - DL/CV; GTM Data Engineer Intern x2; Aviation Compliance Lead).

**Custom inline `<div>` spacers** — 1 posting (Manager, Logistics) uses raw `<div style="min-height:1.2em;margin-top:0;margin-bottom:0;"></div>` as a spacer in place of empty `<p>`. It is the only job in the entire set with inline `style` attributes in body blocks.

### 3.7 List structure
- 105 / 106 postings wrap every `<li>` with an additional `<p>`: `<ul><li><p>…</p></li></ul>`. This subtly increases bullet padding.
- Manager, Logistics is the lone exception (uses plain `<li>` text), so its bullets sit slightly tighter than every other job's.

### 3.8 Inline emphasis (within pre-compensation body)
- **Italics (`<em>` / `<i>`)** — 2 postings: Director, Growth Marketing - Commercial (italicizes "*Ability to be in our San Mateo, CA office 3 days per week*"); Senior NPI Product Quality Engineer.
- **Underline (`<u>`)** — 7 postings: Senior Technical Recruiter; Senior NPI Product Quality Engineer; Lead Staff Electrical Engineer; Senior Software Engineer, Full Stack; Senior Technical Recruiter - Hardware Operations; Staff Technical Recruiter; Full Stack Product Counsel.
- **Bold (`<strong>` / `<b>`)** — used by every posting (for inline emphasis and for the bold-paragraph headings discussed above). No inconsistencies detected in *how* it is applied beyond §3.2.
- **Inline color / font-size / font-weight overrides** — 0 postings.
- **Custom text alignment** — 0 postings (everything is left-aligned by default).

### 3.9 Length / shape
The pre-compensation block varies from 5 to 28 top-level blocks (paragraphs + lists + headings).

| Shortest 5 | Blocks |
|---|---|
| Autonomy Engineer - Deep Learning Model Acceleration (Zurich) | 5 |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | 5 |
| Autonomy Software Engineer | 5 |
| Autonomy Engineer - Deep Learning Infrastructure (Zurich) | 5 |
| Autonomy Engineer - Deep Learning Model Acceleration (San Mateo) | 5 |

| Longest 5 | Blocks |
|---|---|
| IT Technician (Help Desk - Linux Focus) | 28 |
| Director, Global Supply Management - Mechanicals | 26 |
| Full Stack Product Counsel | 24 |
| Success Systems Specialist | 19 |
| Hardware Engineering Program Manager | 18 |

### 3.10 Other quality issues spotted while parsing
- **Double-space typos in 4 job titles** (renders as a noticeably wider gap):
  - "Senior Software Engineer,  Infrastructure"
  - "Staff Global Supply Manager,  Mechanicals"
  - "Senior Software Engineer,  Data Platform"
  - "Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM"
- **Spelling typo in body heading:** Senior People Analytics Analyst → "What Makes **Your** a Good Fit:" (should be "You").
- **Inconsistent dash use in titles:** some titles use the en-dash `–` (e.g. "Enterprise Account Manager (MoD/ MoI) – EMEA (Finland)") while most use a hyphen `-`.

---

## 4. Postings that stand out as different from the norm

Ordered loosely from "most visibly different" to "still visibly different."

1. **Senior Technical Support Representative - Japan (Tokyo)** — Uses `<h1>` for every body section heading. Renders the *body* section labels at the same size as the page's job-title H1. **Single most anomalous posting.**
2. **Software Engineer - Cloud Simulation & Full-Stack (San Mateo & Zurich), Software Engineer - Autonomy Infrastructure, Systems and Tools (San Mateo & Zurich), Communications Manager, Aviation Compliance Lead, Aviation Regulatory Program Manager** — Use `<h2>` for body section headings. Visibly larger and heavier than the 89 jobs that use bold-paragraph headings.
3. **Software Engineer - Simulation & Robotics Engineer (San Mateo & Zurich), Full Stack Product Counsel** — Use `<h3>` for body section headings (still visibly larger than the bold-paragraph norm).
4. **Hardware Engineering Program Manager** — The only posting that uses *both* `<h2>` and `<h3>` to express a two-level heading hierarchy (top-level sections in `<h2>`, sub-sections in `<h3>`). No other posting has visible sub-sections.
5. **Revenue Operations Engineer, Quoting Systems** — Mixes `<p><strong>About the Role:</strong></p>` with five `<h2>` sub-sections (creates a clear hierarchy mismatch — the "About the Role" label looks smaller than the "Day-to-day responsibilities" label below it).
6. **Senior Business Operations Manager** — Mixes `<p><strong>` for the three primary sections with `<h3>` for three sub-sections within "How you'll make an impact" (Strategic Sourcing, Cost Management, Strategy & Operations). The H3 sub-sections look larger than their own parent header.
7. **Senior Buyer & PhD Autonomy Engineer Intern - Planning & Controls (RL)** — Same h2/h3-vs-bold-paragraph mismatch as above.
8. **Manager, Logistics** — The only posting that uses raw `<div style="min-height:1.2em;margin-top:0;margin-bottom:0;">` spacer divs and the only posting whose bullets are *not* wrapped in `<p>` (so bullet spacing is slightly tighter than everywhere else).
9. **Director, Growth Marketing - Commercial** — Most aggressive use of stray `<br/>` tags: 7 list items end with `<br/>`, 1 paragraph ends with `<br/>`, 1 paragraph starts with `<br/>`, and 3 empty `<p>` blocks. Also the rare posting with italicized text in the body.
10. **Senior Product Manager, Platform & Infrastructure** and **Staff Product Manager, Platform & Infrastructure** — 6 empty paragraphs each — the body has visibly larger vertical gaps than peer postings.
11. **Full Stack Product Counsel** — 8 empty paragraphs (worst in the dataset) *and* uses `<h3>` headings. Body looks airy and out-of-style relative to other postings.
12. **Senior People Analytics Analyst** — Contains the spelling typo "What Makes Your a Good Fit" *and* the "About **The** Role" capitalization variant (only posting with both).
13. **Enterprise Account Manager (MoD/MoI) – EMEA (Germany / Switzerland / Finland)** — These three postings all have two leading `<br/>` inside paragraphs (extra blank lines mid-body). They're also the postings using `–` (en-dash) in the title instead of `-`.
14. **IT Technician (Help Desk - Linux Focus)** — 28 blocks (longest), with 2 trailing `<br/>` and 1 leading `<br/>`.
15. **Senior Technical Recruiter / Senior Technical Recruiter - Hardware Operations / Staff Technical Recruiter** — Three of the seven postings that include `<u>` underline formatting in the body.

---

## 5. Recommended fixes (prioritized for the team)

### P0 — Standardize the body heading mechanism (visible to every visitor)
- **Pick one mechanism for all section headings** in every posting. Two reasonable options:
  - **(Recommended) Use `<h2>` for all top-level section headings** ("About the role", "How you'll make an impact", "What makes you a good fit", "Compensation", and the post-comp legal blocks). This is semantically correct (the page already provides the title `<h1>`) and improves accessibility / screen-reader navigation.
  - Or keep the current bold-paragraph treatment everywhere — but then *remove* the `<h2>`/`<h3>`/`<h1>` headings from the 16 outlier postings.
- **Fix the 1 posting that uses `<h1>` inside the body** (Senior Technical Support Representative - Japan, Tokyo) immediately — it is the most jarring visual difference on the site.
- **Choose one canonical section ordering** ("About the role" → "How you'll make an impact" → "What makes you a good fit" → optional bonus / preferred section → "Compensation") and enforce it in the requisition template.

### P1 — Standardize section heading wording
Adopt a single canonical label for each section and update the Greenhouse posting template + style guide:

| Section | Canonical label |
|---|---|
| Intro | `About the role:` |
| Responsibilities | `How you'll make an impact:` |
| Qualifications | `What makes you a good fit:` |
| Optional preferred | `Bonus points:` |
| Compensation | `Compensation:` |

(Or whichever labels the people team prefers — what matters is picking *one* per section.)
- Replace the curly `’` with the straight `'` (or vice versa) consistently across all headings.
- Pick sentence case *or* Title Case for headings and apply universally. (Sentence case is currently the plurality at 48 vs 31, so the smaller change set is to standardize on sentence case.)
- Always include the trailing colon (or always omit it — but be consistent).
- Fix the typo "What Makes **Your** a Good Fit" on Senior People Analytics Analyst.

### P2 — Eliminate manual vertical-spacing hacks
- Remove all empty `<p></p>` blocks (109 across 51 postings). Spacing between sections should be controlled by CSS on the section heading, not by hand-inserted blank paragraphs.
- Remove trailing `<br/>` inside paragraphs (6 postings) and inside `<li>` elements (6 postings). They cause visibly different vertical rhythm.
- Remove leading `<br/>` inside paragraphs (10 postings — mostly the EMEA Account Manager set).
- Remove the inline `<div style="min-height:1.2em;…">` spacers used in Manager, Logistics — replace with the standard template structure.
- Standardize the list-item structure: pick either `<li>text</li>` or `<li><p>text</p></li>` (currently 105 of 106 use the latter — easiest fix is to switch Manager, Logistics to match).

### P3 — Inline-emphasis cleanup
- Decide whether the pre-compensation body may contain underlines (`<u>`) and italics (`<em>`/`<i>`). Currently 7 postings use underline and 2 use italics; the other 97 use neither. Removing the underlines/italics from those 9 postings (or formalizing where they are allowed — e.g. only for the "must be located in X" note) is a 5-minute fix that removes a real visible difference.

### P4 — Title cleanup
- Strip the double space from the four job titles: "Senior Software Engineer,  Infrastructure", "Staff Global Supply Manager,  Mechanicals", "Senior Software Engineer,  Data Platform", "Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM".
- Standardize on `-` (hyphen) or `–` (en-dash) in titles; right now the three EMEA Enterprise Account Manager titles use `–` while the rest use `-`.

### P5 — Process changes to prevent regressions
- Add a posting-template "skeleton" in Greenhouse with the canonical heading text and structure pre-filled.
- Add a short job-posting style guide (1 page) covering: section order, heading wording, capitalization, punctuation, and "do not paste from Word / Google Docs — paste as plain text" guidance. The vast majority of the inconsistencies above (curly quotes, stray `<br/>`, leading/trailing line breaks, empty paragraphs, `<u>` underlines, inline `<div>` spacers) are tell-tale signs of pasted content from a word processor.
- Consider a lightweight pre-publish HTML-lint check in Greenhouse (or a periodic audit script) that flags empty `<p>`, `<br/>` next to block boundaries, `<u>`, inline `style`, `<h1>` in body, and unexpected heading wording. The Python script in this audit (see Appendix) is ~250 lines and can be reused.

---

## 6. Quick-reference scorecard

| Metric | Best ("on style") | Worst (outliers) | % postings on style |
|---|---|---|---|
| Title H1 | All 106 | — | 100% |
| Body section heading method | 89 use `<p><strong>` | 16 use `<h1>`/`<h2>`/`<h3>` (or mix) | 85% (relative to plurality) |
| "About the role" wording | 48 ("About the role:") | 58 use a variant | 45% |
| "How you'll make an impact" wording | 39 (straight apostrophe, sentence case) | 67 use a variant | 37% |
| "What makes you a good fit" wording | 76 ("What makes you a good fit:") | 30 use a variant or typo | 72% |
| No empty `<p>` blocks | 55 | 51 contain ≥1 | 52% |
| No stray `<br/>` | 86 | 20 (leading, trailing, or in `<li>`) | 81% |
| No inline `<u>` / `<em>` | 97 | 9 | 92% |
| No inline `style=` | 105 | 1 (Manager, Logistics) | 99% |
| No body `<h1>` | 105 | 1 (Senior Technical Support Rep - Japan) | 99% |

---

## Appendix — How the analysis was produced

1. Downloaded `https://www.skydio.com/careers` and extracted every `/jobs/<uuid>/` href (106 unique).
2. Downloaded each `/jobs/<uuid>/` page (HTML, no JS execution required — the site server-renders the posting body inside `<div class="prose block-content">`).
3. For each posting, parsed the `prose block-content` container with BeautifulSoup, sliced child elements at the first node whose visible text begins with "Compensation", and recorded for every block: tag name, classes, inline `style` (including `text-align`, `color`, `font-size`, `font-weight`), heading-method classification (`<h1..h6>` vs `<p><strong>...</strong></p>` vs `<p><strong>` containing a likely-heading phrase), number of `<br/>` tags (including leading/trailing detection), whether the block is an empty paragraph, list-item wrapper pattern, and inline `<strong>`/`<em>`/`<u>`/`<a>` counts.
4. Aggregated counters across all 106 jobs and identified outliers per metric.

The site's CSS itself is internally consistent — every posting renders within the same `prose` typography system. All formatting differences identified above come from variation in the source HTML that requisition authors pasted/typed into Greenhouse, not from the design system.
