# Skydio Careers Page — Job Posting Formatting Audit

**Source:** [https://www.skydio.com/careers](https://www.skydio.com/careers) (job content fetched from the Ashby job-board API that powers the page).
**Date of capture:** 2026‑05‑20
**Postings analyzed:** 107 (all listings visible on the page)
**Scope:** Only the content *before* the `Compensation:` block of each posting (intro paragraph, "About the role", "How you'll make an impact", "What makes you a good fit", etc.). Compensation and the boilerplate legal/EEO text that follows it are excluded.

> The careers page renders postings as HTML from Ashby. All visible font-size, font-weight, color, line-spacing and alignment differences originate from the **HTML tags** the recruiter pasted into each posting (Ashby applies the page CSS to those tags). So when this report says "uses `<h2>`," what the visitor sees is a heading rendered at the much larger `<h2>` size set by the careers stylesheet — not a styling difference invented by this report.

---

## 1 — Headline findings (TL;DR)

1. **The single biggest visual inconsistency** is that **16 of 107 postings use real HTML heading tags (`<h1>`, `<h2>`, `<h3>`) for section titles**, while the rest use the standard pattern of **bold paragraphs** (`<p><strong>…</strong></p>`). Because the careers stylesheet renders headings much larger than body text, those 16 postings stand out with section titles that look 1.3–2× the size of every other posting. Four of the 16 mix both styles in the same posting, which compounds the effect.
2. **Section-title casing is a free-for-all.** "About the role", "About the Role", and "About The Role" all coexist for the same section, as do "What makes you a good fit" / "What Makes You a Good Fit" / "What Makes You A Good Fit" — and one posting even has a typo: **"What Makes Your a Good Fit"**.
3. **Trailing-colon punctuation on section labels is mixed.** 261 bold headings end with `:`, 35 do not — the same section is written with and without a colon across the catalog.
4. **9 postings have a "run-on" bold heading** where what should be a body paragraph got pasted *inside* a `<strong>` tag, producing a 200–910-character wall of bold text where the reader expects a short label.
5. **Spacing model is split between two paradigms.** 44 postings insert empty `<p>` spacer paragraphs and 43 use raw `<br>` line breaks — sometimes both — instead of relying on default paragraph spacing the way the majority do.
6. **Emphasis is applied inconsistently.** "Please note" is variously bold + underlined (`<strong><u>PLEASE NOTE:</u></strong>`), italic (`<em>Please note:</em>`), or plain across different postings.
7. **16 job *titles* contain whitespace defects** (leading/trailing spaces or double spaces) which show up verbatim in the listing.
8. **The Compensation block itself has 3 structural variants:** the standard `<p><strong>Compensation:</strong>…</p>` (99 postings), an `<h2><strong>Compensation:</strong></h2>` wrapper with the body inside a `<ul><li>` (1 posting — *Aviation Compliance Lead*), an extra empty `<div>` spacer before the paragraph (*Manager, Logistics*), and 6 postings that omit the dedicated Compensation paragraph entirely.

---

## 2 — What "consistent" looks like (the de facto template)

The vast majority of postings follow this exact structure:

| Element | Standard | % of postings |
| --- | --- | --- |
| Intro paragraph | `<p style="min-height:1.5em">Skydio is the leading US drone company and the world leader in autonomous flight, the key technology for the future of drones and aerial mobility …</p>` | **107 / 107 (100%)** |
| Section labels | Bold paragraph: `<p><strong>About the role:</strong></p>` | 95 / 107 (89%) — but 4 of those also mix in real `<h2>`/`<h3>` |
| Body copy | Standard `<p style="min-height:1.5em">` paragraphs | 107 / 107 (100%) |
| Bulleted lists | `<ul style="min-height:1.5em"><li><p>…</p></li></ul>` | 106 / 107 (99%) |
| Section ordering | Intro → About the role → How you'll make an impact → What makes you a good fit → Compensation | ~64 / 107 (60%) |
| Compensation header | `<p><strong>Compensation:</strong> …</p>` | 99 / 107 (93%) |
| In-paragraph CSS | Inline `style="min-height:1.5em"` only | 107 / 107 (100%) — no rogue inline `color`, `font-size`, `font-weight`, or `text-align` declarations anywhere |

**So when we talk about "outliers" below, the baseline is: bold-paragraph section labels in sentence case ("About the role:") followed by paragraphs and bullet lists, with no manual font sizing.**

---

## 3 — Postings that stand out from the norm

### 3.1 Postings that use real HTML headings instead of bold-paragraph labels (16 / 107)

These render with section titles that are visibly **larger and heavier** than the same sections in every other posting. They are the most obvious "looks different" outliers on the careers page.

| # | Posting (title — location) | Heading tag(s) used | Notes |
| - | --- | --- | --- |
| 1 | **Senior Technical Support Representative – Japan** (Tokyo) | `<h1>` ×3 | Uses page-title-sized `<h1>` for "About the role", "How you'll make an impact", "What would make you a good fit". This is the single largest-typography outlier on the site. |
| 2 | **Revenue Operations Engineer, Quoting Systems** (San Mateo) | `<h2>` ×5 | Five sections all rendered at H2 size. |
| 3 | **Aviation Compliance Lead** (San Mateo) | `<h2>` ×3 | Also wraps the Compensation block in `<h2>` + `<ul><li>` (see §3.6). |
| 4 | **Aviation Regulatory Program Manager** (US Remote) | `<h2>` ×3 | |
| 5 | **Communications Manager** (US Remote) | `<h2>` ×3 | |
| 6 | **Senior Buyer** (Hayward) | `<h2>` ×2 | Only two of the standard sections present, both at H2 size. |
| 7 | **Software Engineer – Cloud Simulation & Full-Stack** (Zurich) | `<h2>` ×5 | Duplicate-pair posting (see #10). |
| 8 | **Software Engineer – Cloud Simulation & Full-Stack** (San Mateo) | `<h2>` ×5 | Duplicate-pair posting. |
| 9 | **Software Engineer – Autonomy Infrastructure, Systems and Tools** (Zurich) | `<h2>` ×5 | |
| 10 | **Software Engineer – Autonomy Infrastructure, Systems and Tools** (San Mateo) | `<h2>` ×5 | |
| 11 | **Software Engineer – Simulation & Robotics Engineer** (Zurich) | `<h3>` ×5 | Same template family as #7–#10 but at `<h3>` instead of `<h2>` — internally inconsistent within the same role family. |
| 12 | **Software Engineer – Simulation & Robotics Engineer** (San Mateo) | `<h3>` ×5 | |
| 13 | **PhD Autonomy Engineer Intern — Planning & Controls (RL)** (Zurich) | `<h3>` ×3 | |
| 14 | **Full Stack Product Counsel** (San Mateo) | `<h3>` ×4 | Also has the most empty-paragraph spacers (see §3.5). |
| 15 | **Senior Business Operations Manager** (San Mateo) | `<h3>` ×3 | Uses `<h3>` as sub-headings ("Strategic Sourcing", "Cost Management", "Strategy & Operations") rather than the standard 3-section template. |
| 16 | **Hardware Engineering Program Manager** (San Mateo) | `<h2>` ×3 + `<h3>` ×5 | **Mixes two heading levels** — top-level sections are `<h2>` and sub-sections are `<h3>`. The only posting that does multi-level heading nesting. |

> *Issue:* Each of these displays section labels at a font-size and font-weight different from the surrounding 91 postings. "Senior Technical Support Representative – Japan" is the most extreme — `<h1>` is the same size as the page's own page-title. *Within the same role family* (the four "Software Engineer – Cloud Simulation / Autonomy Infrastructure" postings) the same content is rendered at both `<h2>` and `<h3>` sizes across geographies — clearly unintentional drift.

### 3.2 Casing & punctuation inconsistencies in section titles

The same logical heading is written several different ways across the catalog:

| Section | Variants observed (count) |
| --- | --- |
| **About the role** | `About the role:` (46) · `About the role` (2) · `About the Role:` (26) · `About the Role` (4) · `About The Role:` (1) |
| **How you'll make an impact** | `How you'll make an impact:` (34) · `How you'll make an impact` (2) · `How you'll make an impact:` (14) · `How You'll Make an Impact:` (18) · `How You'll Make an Impact` (3) · `How You'll Make an Impact:` (1) · `How you will make an impact` (3) |
| **What makes you a good fit** | `What makes you a good fit:` (51) · `What makes you a good fit` (3) · `What Makes You a Good Fit:` (16) · `What Makes You a Good Fit` (3) · `What Makes You A Good Fit:` (3) · `What Would Make You a Good Fit:` (2) · `What makes you a strong fit:` (2) · `What would make you a strong fit:` (2) · `Useful skills and experience:` (2) |
| **About the team** | `About the team:` (6) · `About the Team:` (6) · `About the Team` (1) |
| **Qualifications** | `Qualifications:` (6) · `Qualifications` (1) |
| **Preferred Qualifications** | `Preferred Qualifications:` (2) · `Preferred Qualifications` (2) |
| **Nice to have** | `Bonus Points:` (3) · `Bonus points:` (3) · `Nice to have:` (2) · `Nice to Have:` (1) · `Nice-to-Haves:` (1) |
| **What you'll do** | `What you'll do:` (1) · `What You'll Do:` (6) · `What you will do:` (1) |
| **Apostrophe style** | "you'll" (straight) vs "you'll" (curly) are both in use within the same section name |

**Trailing-colon punctuation:** of 296 bold-paragraph headings inspected, **261 end in `:` and 35 do not** — the same section is written with and without a trailing colon across postings.

### 3.3 Run-on / oversized bold headings (9 postings)

In these postings, what looks visually like a giant wall of bold text is actually a body paragraph that was accidentally pasted *inside* a `<strong>` tag, often concatenated with the next heading. They render as 200–910 characters of bold body copy where the reader expects a short label like "About the role:".

| Posting | Length of run-on heading | Likely correct content |
| --- | --- | --- |
| **Director of Product Management, DFR** | 910 chars | The entire "About the role" paragraph + "Location" + "How you'll make an impact" are jammed into a single `<strong>` |
| **Autonomy Engineer – Deep Learning Model Acceleration** (San Mateo) | 835 chars | Same pattern |
| **Autonomy Engineer – Deep Learning Model Acceleration** (Zurich) | 831 chars | Same pattern |
| **Autonomy Engineer – Deep Learning Infrastructure** (San Mateo / Zurich) | 831 chars each | Same pattern |
| **Autonomy Software Engineer** (San Mateo) | 580 chars | About-the-role body inside `<strong>` |
| **Senior Brand Designer (Contract)** | 234 chars | Intro sentence wrapped in `<strong>` instead of being a paragraph |
| **Senior Technical Recruiter – Hardware Operations** | 217 chars | First sentence of "How you'll make an impact" wrapped in `<strong>` |
| **Senior Director, Product Management, DFR** | 166 chars | A "Location" line bolded together with the next section header |
| **Manager, Technical Support** | 85 chars | Bonus-points bullet got promoted to a bold paragraph |

### 3.4 Typo

* **Senior People Analytics Analyst (San Mateo)** — section label reads **"What Makes Your a Good Fit:"** ("Your" should be "You"). The wrong word appears twice in that posting's pre-comp content.

### 3.5 Spacing inconsistencies

Two parallel mechanisms are in use for vertical spacing — postings should pick one and stick with it.

* **Empty `<p style="min-height:1.5em">` paragraphs as spacers — 44 / 107 postings.** Top offenders:
  * Full Stack Product Counsel: **8 empty paragraphs**
  * Staff Product Manager, Platform & Infrastructure: 5
  * Senior Product Manager, Platform & Infrastructure: 5
  * Deployment Engineer – Southeast: 4
  * Senior Software Engineer – Mobile Platform: 3
  * Director, Growth Marketing – Commercial: 3
  * Senior/Staff Embedded Software Engineer – Camera Systems (San Mateo & Tampere): 3 each
* **Raw `<br>` line breaks — 43 / 107 postings.** Top offenders:
  * Autonomy Engineer – Deep Learning Infrastructure (Zurich): **8 `<br>`**
  * Director, Growth Marketing – Commercial: **8 `<br>`**
  * IT Technician (Help Desk – Linux Focus): **8 `<br>`**
  * Autonomy Engineer – Deep Learning Infrastructure (San Mateo): 6
  * Autonomy Engineer – Deep Learning Model Acceleration (San Mateo & Zurich): 6 each
* **Manager, Logistics** inserts an empty `<div style="min-height:1.2em;margin-top:0;margin-bottom:0"> </div>` immediately before the Compensation paragraph — the only posting using `<div>` for spacing.

### 3.6 Compensation-block boundary anomalies (relevant because they affect what is "pre-compensation")

| Posting | Anomaly |
| --- | --- |
| **Aviation Compliance Lead** | Compensation header is `<h2><strong>Compensation:</strong></h2>` *and* its body sits inside a `<ul><li>…</li></ul>` — visually it renders with a large H2 heading *and* a bullet marker before the salary paragraph. |
| **Manager, Logistics** | Inserts an empty `<div>…</div>` spacer immediately before the `<p>` containing Compensation. |
| **Full Stack Product Counsel** | The word "Compensation" appears mid-paragraph (no dedicated heading at all) — the salary information is buried inside an existing body paragraph. |
| **Workplace Experience Coordinator Part-Time (Zurich)** | No Compensation paragraph at all. |
| **Supplier Quality Engineer, Sustaining (Taiwan)** | No Compensation paragraph at all. |
| **Senior Technical Support Representative – Japan (Tokyo)** | No Compensation paragraph at all. (Acceptable for non-US roles where state law doesn't require it, but inconsistent with other non-US listings that *do* include one.) |
| **Autonomy Engineer Intern – Deep Learning (Computational Photography) (Zurich)** | No Compensation paragraph. |
| **Autonomy Engineer Intern – Deep Learning (Computational Photography) (San Mateo)** | No Compensation paragraph. |

### 3.7 Emphasis (bold / italic / underline) inconsistencies

* **Underline `<u>` in pre-comp content — 7 / 107 postings.** Most are wrapping the phrase "PLEASE NOTE:" together with a `<strong>`:
  * `<strong><u>PLEASE NOTE:</u></strong>` appears in 3 postings ("Staff Technical Recruiter", "Senior Technical Recruiter", "Senior Technical Recruiter — Hardware Operations").
  * `<u>Please Note:</u>` (no bold, mixed case) appears in 1 posting.
  * **Full Stack Product Counsel** underlines its *own job title* ("Full Stack Product Counsel") in the intro paragraph — nowhere else in the catalog does a posting underline the role title.
  * **Lead Staff Electrical Engineer (F10 Program)** underlines "Skydio F10 Program".
  * **Senior Software Engineer, Full Stack** underlines "public API".
* **Italic `<em>` in pre-comp content — 3 / 107 postings.**
  * `<em>Please note:</em>` in **Electric Motor / Propulsion Engineer** and **Senior NPI Product Quality Engineer**.
  * `<em>Ability to be in our San Mateo, CA office 3 days per week</em>` in **Director, Growth Marketing – Commercial**.
* **Net effect:** the same "Please note" / hybrid-policy callout is sometimes bold-underlined-all-caps, sometimes italic-sentence-case, and sometimes nothing at all.

### 3.8 Structural / list-vs-prose outliers

* **Director, Global Supply Management — Mechanicals (San Mateo)** is the **only posting (1 / 107) with zero bullet list items** in its pre-comp content — the role is conveyed entirely in long prose paragraphs, which makes it visually denser than every other posting on the page.
* **Senior Business Operations Manager (San Mateo)** is the only posting that uses **third-level sub-headings** ("Strategic Sourcing", "Cost Management", "Strategy & Operations") *as if* they were standard sections — but they are `<h3>` rather than bold paragraphs, so they appear larger than other postings' top-level sections.
* **Hardware Engineering Program Manager** is the only posting that combines `<h2>` and `<h3>` heading levels.

### 3.9 Missing standard sections

Out of the implied template "About the role → How you'll make an impact → What makes you a good fit":

* **39 / 107 postings do not have an "About the role" label** (in any casing). For most of these, the role description was simply written as the second paragraph without being introduced by a heading.
* **34 / 107 postings have no "How you'll make an impact" / "What you'll do" / "Responsibilities" heading** — their responsibilities list is presented without a heading.
* **30 / 107 postings have no "What makes you a good fit" / "Qualifications" heading** — the qualifications list also goes unlabeled.

(Full lists are in the appendix; the postings that hit *all three* are most exposed.)

### 3.10 Job-title text defects (16 / 107)

These appear as the visible posting title and contain stray whitespace:

* Leading space: ` Senior Software Engineer,  Infrastructure`, ` Electrical Engineer (Sustaining/Validation)`, ` Software Engineer - Infrastructure`
* Trailing space: `Electrical Engineer (all levels) `, `Senior Software Engineer - Embedded `, `Autonomy Engineer - ML & DL Infrastructure `, `Senior Autonomy Engineer - Controls `, `Success Systems Specialist `, `Senior Software Engineer - Mobile Platform `, `Field Support Representative `, `Manager, Logistics `, `Senior Software Engineer,  Data Platform `
* Double space inside title: `Senior Software Engineer,  Data Platform `, `Staff Global Supply Manager,  Mechanicals`, ` Senior Software Engineer,  Infrastructure`, `Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM`

---

## 4 — Per-posting "looks different" scoreboard

These postings have the **most cumulative formatting deviations** from the de facto template and should be reviewed first.

| Posting | Reasons it stands out |
| --- | --- |
| **Senior Technical Support Representative – Japan** (Tokyo) | Uses `<h1>` for sections (largest typography on the site); no Compensation paragraph |
| **Aviation Compliance Lead** (San Mateo) | Uses `<h2>` section headings; Compensation also wrapped in `<h2>` + `<ul><li>` |
| **Hardware Engineering Program Manager** (San Mateo) | Mixes `<h2>` and `<h3>` heading levels (only posting to nest) |
| **Full Stack Product Counsel** (San Mateo) | `<h3>` headings; 8 empty-`<p>` spacers (most in catalog); underlines its own job title; Compensation is inlined into body rather than its own paragraph |
| **Director of Product Management, DFR** (San Mateo) | 910-character run-on bold "heading"; 4 stray `<br>`; missing "About the role" label |
| **Autonomy Engineer – Deep Learning (Infrastructure & Model Acceleration)** family (4 postings) | Run-on bold headings (~830 chars); 6–8 `<br>` each; missing "About the role" label; identical formatting bug across the four — likely copy-pasted |
| **Director, Growth Marketing – Commercial** (San Mateo) | 8 `<br>` + 3 empty `<p>` (uses both spacing paradigms simultaneously); italic emphasis where every other posting uses bold |
| **Senior People Analytics Analyst** (San Mateo) | Typo "What Makes Your a Good Fit:" (appears twice) |
| **Software Engineer – Simulation & Robotics Engineer** (San Mateo & Zurich) | `<h3>` headings while sister postings (Cloud Simulation, Autonomy Infrastructure) use `<h2>` — same template, two different heading sizes |
| **Director, Global Supply Management — Mechanicals** (San Mateo) | The only posting with **no bullet lists at all** — pure prose, visually much denser than every neighbor |
| **Senior Business Operations Manager** (San Mateo) | Sub-section headings done as `<h3>` instead of the standard pattern |
| **Manager, Logistics ** (US CA Production) | Empty `<div>` spacer before Compensation; trailing whitespace in title |
| **Senior Technical Recruiter** / **Senior Technical Recruiter – Hardware Operations** / **Staff Technical Recruiter** | All-caps `<strong><u>PLEASE NOTE:</u></strong>` callout absent from the rest of the catalog |
| **IT Technician (Help Desk – Linux Focus)** (Hayward) | 8 stray `<br>` — among the most in the catalog |

---

## 5 — Recommendations (actionable)

### 5.1 Establish a canonical template
Adopt the following as the single approved structure for every posting (pre-compensation):

```
<p>Skydio is the leading US drone company …</p>                <!-- standardized intro paragraph -->
<p><strong>About the role:</strong></p>
<p>…role description…</p>

<p><strong>How you'll make an impact:</strong></p>
<ul><li><p>…</p></li>…</ul>

<p><strong>What makes you a good fit:</strong></p>
<ul><li><p>…</p></li>…</ul>

<p><strong>Compensation:</strong> …</p>
```

Codify two rules in writing:
* **Section titles are bold paragraphs (`<p><strong>…</strong></p>`), never `<h1>`, `<h2>`, `<h3>`.** Eliminating heading tags removes the single biggest visible inconsistency on the page (the 16 oversized-heading postings).
* **All section titles use sentence case, a straight apostrophe, and a trailing colon:**
  `About the role:` · `How you'll make an impact:` · `What makes you a good fit:` · `Compensation:`

### 5.2 Run a one-time cleanup pass on the 16 postings using `<h1>`/`<h2>`/`<h3>`
Replace each `<h1>…</h1>`, `<h2>…</h2>`, `<h3>…</h3>` with `<p><strong>…</strong></p>`. Special handling for:
* **Aviation Compliance Lead** — also unwrap the Compensation `<ul><li>` so the salary copy is in a plain paragraph.
* **Senior Technical Support Representative – Japan** — replace `<h1>` (page-title-size) immediately.
* **Hardware Engineering Program Manager** — collapse the `<h3>` sub-headings into bullet lead-ins or short bolded list-item prefixes; do not introduce a new heading hierarchy.

### 5.3 Fix the 9 run-on bold "headings"
For each posting in §3.3, manually unwrap the `<strong>` tag so the section label is *only* the short label ("About the role:") and the body copy becomes regular paragraphs. The Autonomy Engineer (DL) family of four can be fixed with a single template edit.

### 5.4 Fix the typo and the title whitespace
* Edit **Senior People Analytics Analyst**: change both occurrences of "What Makes Your a Good Fit" to **"What makes you a good fit:"**.
* Trim leading/trailing whitespace and collapse double spaces in the 16 job titles listed in §3.10.

### 5.5 Pick one spacing model and stop mixing
Recommend using paragraph-level spacing only (the careers stylesheet already provides margin between `<p>` blocks).
* **Remove all `<br>` tags from the 43 postings in §3.5**, especially Autonomy Engineer – DL Infrastructure (Zurich), Director Growth Marketing – Commercial, and IT Technician (Linux Focus) which each have 8.
* **Remove the empty `<p>` spacer paragraphs** from the 44 postings — they exist almost exclusively to add extra vertical air that the global stylesheet would otherwise handle.
* **Remove the empty `<div>` spacer** in Manager, Logistics.

### 5.6 Standardize the "Please note" callout
Pick one of the three current styles and use it everywhere. Recommended: `<p><strong>Please note:</strong> …</p>` (bold only, sentence case, no underline, no italic, no all-caps). This affects ~10 postings (3 with `PLEASE NOTE:`, 3 with italic `Please note:`, others).

### 5.7 Standardize the Compensation block
* Always present Compensation as `<p><strong>Compensation:</strong> …</p>` — never `<h2>`, never inside a `<ul>`, never inline mid-paragraph, never preceded by an empty `<div>`/`<p>` spacer.
* For non-US roles that genuinely don't publish a salary range, still include the boilerplate `<p><strong>Compensation:</strong> Compensation will be discussed during the recruiting process …</p>` paragraph so the heading-by-heading visual rhythm is identical across postings.

### 5.8 Decide once whether the three standard section labels are required
Currently 39 postings lack "About the role:", 34 lack a responsibilities heading, and 30 lack a qualifications heading. Either:
* Make them mandatory and back-fill the missing labels, **or**
* Officially permit an unlabeled lead paragraph and document it in the style guide — but apply the choice catalog-wide so the page reads consistently.

### 5.9 Add a CI check (optional but high-leverage)
Because the content is fetched from a public API (`https://api.ashbyhq.com/posting-api/job-board/skydio?includeCompensation=true`) a simple lint script (~200 lines of Python, similar to what produced this report) could be run nightly to fail when a posting:
* contains any `<h[1-6]>` tag,
* contains `<br>`,
* contains an empty `<p>` or `<div>`,
* uses `<u>` outside a known allow-list,
* uses inline `style="color:…"`, `style="font-size:…"`, `style="font-weight:…"`, or `style="text-align:…"`,
* has a section label not in the canonical set,
* has a title with leading/trailing/double spaces,
* omits the Compensation paragraph.

A nightly Slack notification on regressions would prevent the next round of drift.

---

## Appendix A — Full list of postings missing each standard section heading

**Missing "About the role" label (39 postings):**
Senior Technical Recruiter – Hardware Operations · Senior Technical Recruiter · Senior Director, Product Management, DFR · Director of Product Management, DFR · Electric Motor / Propulsion Engineer · Senior Autonomy Engineer – Deep Learning (San Mateo) · Senior Autonomy Engineer – Deep Learning (Zurich) · Autonomy Engineer – Deep Learning Infrastructure (×2) · Autonomy Engineer – Deep Learning Model Acceleration (×2) · Autonomy Software Engineer · Full Stack Product Counsel · Staff Product Manager, Platform & Infrastructure · Product Design Engineer (All Levels) · Staff Software Engineer, Full Stack · GTM Data Engineer Intern · Sales Planning Analyst Intern · Product Support Engineer · Senior Technical Support Representative – Japan · Aviation Compliance Lead · Software Engineer – Cloud Simulation & Full-Stack (×2) · Software Engineer – Simulation & Robotics Engineer (×2) · Software Engineer – Autonomy Infrastructure, Systems and Tools (×2) · Senior Software Engineer, Infrastructure · Aviation Regulatory Program Manager · GTM Enablement Associate · Communications Manager · Workplace Experience Coordinator Part-Time · Senior Product Manager, Platform & Infrastructure · Hardware Engineering Program Manager · Product Support Engineer Intern · Hardware Technician · Software Engineer – Infrastructure · Lead Staff Electrical Engineer (F10 Program) · Software Engineer Intern Fall 2026/Winter 2027

**Missing any responsibilities heading (34 postings):** See per-posting JSON for the full list — top offenders include the Software Engineer – Cloud Simulation / Simulation & Robotics / Autonomy Infrastructure family (6 postings), the Autonomy Engineer – Deep Learning family (4 postings), and the four DFR Product Manager postings.

**Missing any qualifications heading (30 postings):** Includes the same simulation/infrastructure SWE family, both DFR Director postings, Director Growth Marketing – Commercial, Director Global Supply Management – Mechanicals, both PM postings, several intern roles.

## Appendix B — Methodology

1. Fetched the live job board JSON: `GET https://api.ashbyhq.com/posting-api/job-board/skydio?includeCompensation=true` (this is the same payload the careers page uses to render the listings).
2. For each of the 107 postings, isolated the `descriptionHtml` content **up to (but not including) the first block element whose text begins with the word "Compensation"** (`<p>`, `<h1>`–`<h6>`, `<ul>`, `<ol>`, `<li>`, or `<div>` — to catch the various wrappers that occur in the catalog).
3. Catalogued for each posting: every HTML tag used, every `style="…"` declaration (separated into `color`, `font-size`, `font-weight`, `text-align`, and other), every real heading (`<h1>`–`<h6>`) and every bold-paragraph "heading" pattern, list-item count, empty-paragraph count, `<br>` count, and underline / italic usages.
4. Compared per-posting catalogs against the catalog-wide mode to identify outliers.
5. Manually spot-checked the outliers above (Aviation Compliance Lead, Hardware Engineering Program Manager, Senior Technical Support Representative – Japan, etc.) against their live URLs on `skydio.com/careers` to confirm the rendered effect.

No inline `color`, `font-size`, `font-weight`, or `text-align` declarations were found in any posting — all visible font-size/weight/alignment differences come from the use (or misuse) of structural HTML tags (`<h1>`–`<h6>`, `<strong>`, `<em>`, `<u>`), not from per-posting CSS overrides.
