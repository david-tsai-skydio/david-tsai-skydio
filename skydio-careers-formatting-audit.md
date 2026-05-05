# Skydio Careers Page — Job Posting Formatting Audit

**Source:** [https://www.skydio.com/careers](https://www.skydio.com/careers)
**Audit date:** 2026-05-05
**Scope:** All job postings linked from the careers page, analyzed from the page header through the body content immediately preceding each posting's `Compensation:` block. The compensation block and everything below it (benefits, EEO statement, "Apply for this job" form) is intentionally excluded.
**Postings analyzed:** 118 individual job pages (every link found under `/jobs/<id>` on the careers index)

---

## 1. How a Skydio job posting is supposed to look

By looking at the markup the careers site uses, every posting follows the same skeleton — the differences described in this report are deviations from that skeleton.

| Element | Markup | Computed type style |
|---|---|---|
| Posting title (e.g. "Senior Software Engineer, Full Stack") | `<h1 class="type-h2">` | 28-48 px, weight 500 |
| Location / type sub-line (e.g. "San Mateo, California, United States - Full-time") | `<p class="type-body-2">` | 16-18 px, weight 400 |
| Body description container | `<div class="prose block-content">` | — |
| Standard intro paragraph ("Skydio is the leading US drone company…") | `<p>` | 14-16 px, weight 400 |
| Section heading (e.g. "About the role:") | `<p><strong>…</strong></p>` | 14-16 px, weight 700 |
| Bullet item | `<ul><li><p>…</p></li></ul>` | 14-16 px, weight 400 |

**All 118 postings share the wrapper styles** — title is always `type-h2`, location is always `type-body-2`, and the body always lives inside `.prose.block-content`. No posting uses inline `style="…"` attributes, no posting uses `<ol>` numbered lists, every posting wraps each `<li>` content in a `<p>`, and every posting begins with the same boilerplate "Skydio is the leading US drone company…" paragraph.

So the wrapper-level typography is consistent. **The inconsistencies are concentrated in the body of the description**, in five specific buckets:

1. **Heading hierarchy** — using `<h1>`, `<h2>`, or `<h3>` for section titles instead of the standard `<p><strong>…</strong></p>`. This is by far the most visually disruptive issue because it changes font size by 50-200% and changes the surrounding line spacing.
2. **Casing of section labels** — sentence case ("About the role:") vs. title case ("About the Role:") vs. all-caps stand-outs ("PLEASE NOTE:" with `<u>`).
3. **Punctuation of section labels** — colon inside `<strong>` vs. colon outside vs. no colon at all, sometimes mixed within a single posting.
4. **Whitespace artifacts** — empty `<p></p>` paragraphs, stray `<br />` tags inside list items, and multiple `<br />` tags used in place of paragraph breaks. These produce uneven vertical spacing.
5. **Run-together text** — paragraphs that should be separated have been pasted together, leaving a single dense block where the next bold section heading is mid-sentence.

A secondary issue is that other emphasis styles — `<u>` (underline) and `<em>` (italic) — appear in only ~7 postings combined and are inconsistent stand-outs.

---

## 2. Aggregate findings

| Inconsistency | # postings affected | Notes |
|---|---:|---|
| Title (`<h1 class="type-h2">`) | 0 / 118 | Consistent ✓ |
| Location subtitle (`<p class="type-body-2">`) | 0 / 118 | Consistent ✓ — but the wording is verbose ("California, United States" instead of "CA"); see Section 5. |
| Body wrapper (`.prose.block-content`) | 0 / 118 | Consistent ✓ |
| Inline `style="…"` attributes | 0 / 118 | Consistent ✓ |
| Ordered `<ol>` lists | 0 / 118 | Consistent ✓ — all bullets use `<ul>`. |
| Bullet structure (`<li><p>…</p></li>`) | 0 / 118 | Consistent ✓ |
| Standard "Skydio is the leading US drone…" intro | 118 / 118 verbatim | Consistent ✓ |
| **Section heading uses `<h1>` in body** | **1** | "Senior Technical Support Representative – Japan" |
| **Section heading uses `<h2>` in body** | **11** | Renders ~22-32 px, vs. ~14-16 px for the standard `<strong>` heading. |
| **Section heading uses `<h3>` in body** | **6** | Renders ~18-28 px. |
| **Run-together blocks** (no paragraph break separating "About the role" from the next section) | **30** | Single most common defect; sometimes the bold heading literally appears in the middle of a sentence. |
| **Stray empty `<p></p>` paragraphs** | **51** | Adds 1-3 extra blank lines of vertical space in unintended places. |
| **Multiple inline `<br />` tags** (≥4 in body) | **9** | Used to fake paragraph breaks; produces tighter or larger gaps than real `<p>`. |
| **`<br />` at end of `<li><p>…</p></li>`** | **6 postings, 13 bullets** | Some bullets get a trailing blank line, others don't, in the same list. |
| **Mixed colon styles** within one posting | **22** | E.g. "About the Role:" + "How you'll make an impact" + "What makes you a good fit" all in one posting. |
| **Sentence case vs. title case** for the same standard heading | Spread across whole site | "About the role:" appears 49×, "About the Role:" 29×; "How you'll make an impact:" 42×, "How You'll Make an Impact:" 22×; "What makes you a good fit:" 65×, "What Makes You a Good Fit:" 28×. |
| Underline `<u>` used inside body | 6 | Only 6 postings — and 4 of them use it for "PLEASE NOTE:" while the other 2 use it on regular phrases (e.g. "public API"). |
| Italic `<em>` used inside body | 4 | Only 4 postings — examples include "Ability to be in our San Mateo, CA office 3 days per week" and "Please note:". |
| Job-title duplicates (same role, different IDs) | 8 pairs (110 unique titles, 118 postings) | E.g. "Software Engineer - Cloud Simulation & Full-Stack" exists twice with different bodies. |
| "leading US drone" vs. "leading U.S." in intro | 118 vs. 0 in extracted bodies (1 occurrence elsewhere on careers page is in the hero, not a posting body) | Consistent across all postings ✓ |

> **Bottom line:** Wrapper templates are consistent. The body content (which is the part candidates actually read) has formatting drift in **69 of 118 postings (≈58 %)**.

---

## 3. The standard, by example

These two postings represent the cleanest version of the format and should be used as the template:

- **Software Engineer, Full Stack** (`/jobs/4c4874bf-02da-4ccc-8918-2cca08feaf21/`) — exactly four `<p><strong>…</strong></p>` headings ("About the role:", "How you'll make an impact:", "What makes you a good fit:", "Bonus points for:"), no stray `<br/>`, no empty `<p>`, no `<u>`/`<em>`, no `<h*>` tags.
- **Sr/Staff Embedded Software Engineer - Camera Systems (Tampere)** (`/jobs/898a9c77-cc20-4ed6-a050-f68e5c15d5c8/`) — same template, sentence-case headings.

---

## 4. Postings flagged as outliers (sorted by severity)

The full per-job list is in Appendix A. The most disruptive cases are called out here.

### 4.1 — Severe: heading-hierarchy outliers
These postings use `<h1>`, `<h2>` or `<h3>` for section labels, so the section labels render two-to-five times larger than in any other posting and break the visual rhythm of the page.

| Posting | Symptom |
|---|---|
| **Senior Technical Support Representative – Japan** | Uses `<h1>` for "About the role:", "How you'll make an impact:", "What would make you a good fit:". These render at ~28-48 px — same size as the page title at the top. Unique to this posting. |
| **Revenue Operations Engineer, Quoting Systems** | Uses `<h2>` for all section labels ("What you'll drive (scope):", "Day-to-day responsibilities:", "Tech stack you'll work with:", "What you'll bring:", "Reporting & Working Model:"). |
| **Deployment Coordinator** | Uses `<h2>` for "About the Role", "How You'll Make an Impact", "What Makes You a Good Fit", "Why This Role is Unique". |
| **Communications Manager** | Uses `<h2>` for "About the role", "How you'll make an impact", "What makes you a good fit". |
| **Senior Buyer** | Uses `<h2>` for "How you will make an impact:" and "What makes you a strong fit:". |
| **Software Engineer - Cloud Simulation & Full-Stack** (×2 postings) | Uses `<h2>` for "About the Role:", "Areas of Responsibility:", "What You'll Do:", "Qualifications:", "Bonus Experience:". |
| **Software Engineer - Autonomy Infrastructure, Systems and Tools** (×2 postings) | Uses `<h2>` for the same five-label structure as Cloud Simulation. |
| **Senior Manager, Deployment Operations** | Uses `<h2>` for the top-level sections **and** `<h3>` for sub-sections like "Strategic Project Leadership (40%)". The mix of two heading levels makes the page look like a different design system than every other posting. |
| **Aviation Compliance Lead**, **Aviation Regulatory Program Manager** | Use `<h2>` for "About the Role", "How You'll Make an Impact", "What Makes You a Good Fit". |
| **Field Marketing Event Manager** | Uses `<h3>` (with bold inside) for sub-sections like "Customer Summit Planning & Execution". |
| **Software Engineer - Simulation & Robotics Engineer** (×2 postings) | Uses `<h3>` for the standard five labels. |
| **Project Manager, Workplace** | Uses `<h3>` for "About the Role" and "How You'll Operate". |
| **PhD Autonomy Engineer Intern – Planning & Controls (Reinforcement Learning)** | Uses `<h3>` for sub-headings inside the "How you'll make an impact" section. |

> **Specific issue:** Section labels in these postings are 22-48 px depending on the heading level, while the same labels in 100/118 other postings render at 14-16 px (paragraph weight 700). The neighboring vertical spacing also differs because the prose stylesheet adds extra margin around `<h*>` elements.

### 4.2 — Severe: paragraphs merged into one (no paragraph break)
The author pasted prose without preserving paragraph breaks, so the next bold heading appears mid-sentence. The visible result is a wall of text that is impossible to skim.

| Posting | What's collapsed |
|---|---|
| **Senior Product Manager, Platform & Infrastructure** | The intro paragraph and 6 separate "Customer & sales engagement / Own the platform roadmap / Productize / Drive compliance / Release & expectation management / Compliance enablement / Evangelize & enable" sub-bullets are all one giant paragraph (≈2,000 chars). |
| **Staff Product Manager, Platform & Infrastructure** | Identical defect to the above. |
| **Senior Manager, Deployment Operations** | "Location:", "Travel Requirements:", "How You'll Make an Impact", and four percentage-weighted sub-sections are merged into a 2,054-char block. |
| **Hardware Operations Program Manager** | All 7 responsibility bullets are one merged paragraph followed by "What makes you a good fit:". |
| **Senior People Analytics Analyst** | "Reporting & Dashboarding…", "Workday and Data Integrity…", "People Analytics & Insight Generation…", "Strategic Communication…" merged; same thing happens again later for the qualifications. |
| **GTM Data Engineer Intern** | Three separate run-on blocks. |
| **Director of Product Management, Drone as First Responder (DFR)** | The intro, the "Location:" disclaimer, and the start of "How you'll make an impact:" are merged. |
| **Lead Staff Electrical Engineer (F10 Program)** | Intro merged with "How you'll make an impact:". |
| **Senior Software Engineer, Infrastructure** | "About the team:" and "About the role:" are concatenated with no break. |
| **Software Engineer - Infrastructure** | Same defect — pulled from the same source as the Senior version. |
| **Autonomy Engineer - Deep Learning Infrastructure** (×2) | "About the role:" intro merged with the next paragraph and with "How you'll make an impact:". |
| **Autonomy Engineer - Deep Learning Model Acceleration** (×2) | Same defect as Deep Learning Infrastructure. |
| **Senior Autonomy Engineer - Deep Learning** (×2 postings, US + Zurich) | Intro merged with "How you'll make an impact:". |
| **Autonomy Software Engineer** | Intro merged with "How you'll make an impact:". |
| **GTM Enablement Associate** | Five paragraphs collapsed into one. |
| **Sales Planning Analyst Intern** | Intro paragraphs merged with "How You'll Make an Impact:". |
| **Senior Technical Recruiter - Hardware Operations** | "About the role:", a "PLEASE NOTE" sentence, and "How you'll make an impact:" all merged. |
| **Electric Motor / Propulsion Engineer**, **Hardware Technician**, **Product Design Engineer (All Levels)**, **Product Support Engineer**, **Product Support Engineer Intern**, **Senior Brand Designer (Contract)**, **Technical Support Specialist - West Coast**, **Workplace Experience Coordinator Part-Time** | Each has the intro paragraph fused to the next section header. |
| **Revenue Operations Engineer, Quoting Systems**, **PhD Autonomy Engineer Intern – Planning & Controls** | Run-together blocks in addition to the heading-tag misuse described above. |

### 4.3 — Moderate: stray empty paragraphs
Empty `<p></p>` tags add an extra blank line. Most postings have 0; the worst offenders below have 3-6.

| # blank `<p>` | Posting |
|---:|---|
| 6 | Senior Product Manager, Platform & Infrastructure |
| 6 | Staff Product Manager, Platform & Infrastructure |
| 5 | Deployment Engineer - Southeast |
| 5 | Senior Manager, Deployment Operations |
| 4 | Deployment Coordinator |
| 4 | Senior Autonomy Engineer - Data Curation |
| 4 | Senior/Staff Embedded Software Engineer – Camera Systems |
| 4 | Sr/Staff Embedded Software Engineer - Camera Systems |
| 3 | Manufacturing Business Process Intern, Program Manager — Major Deployments (Hawaii / Mid Atlantic / South East), Communications Manager, Hardware Operations Program Manager, Senior Brand Designer (Contract), Senior Buyer, Hardware Technician, Production Manager PM Shift, Product Support Engineer Intern, Senior Software Engineer - Mobile Platform |
| 2 | 17 additional postings (see Appendix A). |

### 4.4 — Moderate: stray `<br />` tags
- **Director, Growth Marketing - Commercial** has 8 `<br />` tags in its body, including 7 `<br />` placed at the very end of `<li><p>…</p></li>` items — so 7 bullets get a trailing blank line while the rest don't.
- **Autonomy Engineer - Deep Learning Infrastructure** (one variant) has 8 `<br />` tags being used in lieu of paragraph breaks.
- **Director of Product Management, DFR**, **Senior Technical Recruiter - Hardware Operations**, **Autonomy Software Engineer**, **Autonomy Engineer - Deep Learning Model Acceleration** (×2), **Revenue Operations Engineer, Quoting Systems**, **GTM Data Engineer Intern** all use 4-6 `<br />` tags.

### 4.5 — Moderate: mixed header punctuation within a single posting
22 postings mix two or three colon styles for sibling headings:

| Posting | "About:", "About:", "About" | Punctuation styles used |
|---|---|---|
| Director, Growth Marketing - Commercial | mixed | 4 with colon-inside-`<strong>`, 1 with no colon ("Additional Desired Experience and Skills") |
| Project Manager, Workplace | mixed | 1 with colon-inside, 5 with no colon |
| Workplace Experience Coordinator Part-Time | mixed | 1 with colon-inside, 4 with no colon |
| Success Systems Specialist | mixed | 4 with colon-inside, 4 with no colon |
| Senior People Analytics Analyst | mixed | 2 with colon-inside, 2 with no colon |
| Staff Product Manager, Cameras & Sensors | mixed | 1 with colon-inside, 2 with no colon |
| Senior Software Engineer, Frontend | mixed | 4 with colon-inside, 1 with **colon outside** `<strong>` |
| Senior Software Engineer, Full Stack | mixed | 4 with colon-inside, 1 with colon outside |
| Staff Software Engineer, Full Stack | mixed | 3 with colon-inside, 1 with colon outside |
| Senior Brand Designer (Contract) | mixed | 3 with colon-inside, 1 with no colon |
| Manufacturing Business Process Intern | mixed | 3 with colon-inside, 1 with no colon |
| Mission Success Operations Manager | mixed | 3 with colon-inside, 1 with no colon |
| Senior Software Engineer, Data Platform | mixed | 3 with colon-inside, 1 with no colon |
| Senior Staff Product Manager, Drone Hardware Platforms & Sensors | mixed | 2 with colon-inside, 1 with no colon |
| Enterprise Account Manager (MoD/MoI) – EMEA (Germany) | mixed | 3 / 1 |
| Enterprise Account Manager (MoD/MoI) – EMEA (Switzerland) | mixed | 3 / 1 |
| Enterprise Account Manager (MoD/MoI) – EMEA (Finland) | mixed | 3 / 1 |
| Solutions Engineer – Government & National Security – Germany | mixed | 3 / 1 |
| Solutions Engineer – Government & National Security – Switzerland | mixed | 3 / 1 |
| Solutions Engineer – Government & National Security – Finland | mixed | 3 / 1 |
| Senior Product Manager, Platform & Infrastructure | mixed | 2 / 1 |
| Staff Product Manager, Platform & Infrastructure | mixed | 2 / 1 |

The colon-outside-`<strong>` variant is the most visible because the colon then renders in regular weight next to the bold label (e.g. **About the Role**:).

### 4.6 — Site-wide: title case vs. sentence case
Across the whole careers page, the same labels appear in two casings:

| Standard label | Sentence case count | Title case count |
|---|---:|---:|
| About the role / About the Role | 49 | 29 |
| How you'll make an impact / How You'll Make an Impact | 42 | 22 |
| What makes you a good fit / What Makes You a Good Fit | 65 | 28 |
| Bonus points for / Bonus Points / Nice to have / Nice To Haves | mixed; at least four label variants observed | — |

There is also one typo: **Senior People Analytics Analyst** has "What Makes Your a Good Fit:" (note "Your", not "You").

### 4.7 — Outliers in emphasis styling
- `<u>` (underline) appears in only **6 postings**:
  - "PLEASE NOTE:" — Senior Technical Recruiter, Senior Technical Recruiter – Hardware Operations, Staff Technical Recruiter
  - "Please Note:" — Senior NPI Product Quality Engineer (also wrapped in `<em>`)
  - "Skydio F10 Program" — Lead Staff Electrical Engineer (F10 Program)
  - "public API" — Senior Software Engineer, Full Stack
  Underlining body text is unconventional in this site (no other posting does it), and it visually conflicts with hyperlinks because every link in `.prose` is also underlined.
- `<em>` (italic) appears in only **4 postings**:
  - **Director, Growth Marketing - Commercial** — italicises the entire bold sentence "Ability to be in our San Mateo, CA office 3 days per week" (no other posting italicises the office-attendance requirement).
  - **Manufacturing Business Process Intern** — italicises three numbered project labels.
  - **Senior NPI Product Quality Engineer** — italicises an underlined "Please Note:" (italic + bold + underline triple-stack).
  - **Electric Motor / Propulsion Engineer** — italicises "Please note:".

### 4.8 — Other small inconsistencies
- **Two pairs of postings have run-on text where the location/team intro is fused into a section heading:** Director of Product Management, DFR puts "Location: This position is based onsite 5 days/week at our HQ in San Mateo, CA, with ~50% travel. We offer relocation assistance if needed." inline immediately before "How you'll make an impact:", with no paragraph break.
- **Trailing whitespace in title strings:** "Senior Software Engineer,  Infrastructure", "Senior Software Engineer,  Data Platform", "Staff Global Supply Manager,  Mechanicals" all contain a double space after the comma. This affects the page `<title>` tag, the `<h1>`, and the index list on the careers page.
- **Eight job titles appear twice with different IDs and slightly different bodies** — e.g. "Software Engineer - Cloud Simulation & Full-Stack", "Software Engineer - Simulation & Robotics Engineer", "Software Engineer - Autonomy Infrastructure, Systems and Tools", "Senior Autonomy Engineer - Deep Learning", "Autonomy Engineer - Deep Learning Infrastructure", "Autonomy Engineer - Deep Learning Model Acceleration", "Sr/Staff Embedded Software Engineer - Camera Systems"/"Senior/Staff Embedded Software Engineer – Camera Systems" (the latter pair also disagree on `Sr/Staff` vs `Senior/Staff` and on hyphen vs. en-dash).

---

## 5. Recommendations

These are ordered by impact-to-effort ratio.

### 5.1 — Adopt and enforce a single template
Document a canonical posting structure and have every recruiter / hiring manager paste into that template. The recommended skeleton:

```html
<p>Skydio is the leading US drone company …</p>          <!-- standard intro, never edited -->

<p><strong>About the role:</strong></p>
<p>…</p>

<p><strong>How you'll make an impact:</strong></p>
<ul><li><p>…</p></li></ul>

<p><strong>What makes you a good fit:</strong></p>
<ul><li><p>…</p></li></ul>

<p><strong>Bonus points for:</strong></p>           <!-- optional -->
<ul><li><p>…</p></li></ul>

<p><strong>Compensation:</strong></p>
…
```

Specifically:
- **Section labels are `<p><strong>…</strong></p>` only.** Never `<h1>`, `<h2>`, or `<h3>`.
- **Sentence case** for every standard label: "About the role:", "How you'll make an impact:", "What makes you a good fit:", "Bonus points for:".
- **Colon goes inside the `<strong>`** so the colon is bold ("About the role:"), not after it.
- **No `<u>` or `<em>`** in body text. If a paragraph needs emphasis, use `<strong>` only. "PLEASE NOTE" / "Please Note:" should become "Please note:" in regular weight, or "**Please note:**" in bold — never underlined.

### 5.2 — Fix the heading-hierarchy outliers (high priority)
The 17 postings listed in Section 4.1 should be re-saved with `<p><strong>…</strong></p>` headings. These are the most visually obvious outliers and the fix is mechanical (it can be done in the CMS without re-writing copy):

```
<h1>About the role:</h1>          →  <p><strong>About the role:</strong></p>
<h2>About the Role:</h2>          →  <p><strong>About the role:</strong></p>
<h3>About the Role:</h3>          →  <p><strong>About the role:</strong></p>
```

For postings that legitimately have **sub-sections** (e.g. Senior Manager, Deployment Operations and Field Marketing Event Manager have grouped responsibilities like "Strategic Project Leadership (40%)"), use a nested `<ul>` or a bold inline label, not `<h3>`.

### 5.3 — Fix run-together text (high priority)
The 30 postings in Section 4.2 each need real paragraph breaks inserted between the intro, "About the role" body, location disclaimer, and "How you'll make an impact" heading. The Senior/Staff Platform & Infrastructure pair and the Senior Manager, Deployment Operations posting are the worst — those are 1,400-2,000-character single paragraphs.

Root cause is almost always pasting from Google Docs or Notion into the CMS without "Paste as plain text". Adding a documented "always paste with Cmd+Shift+V then re-add formatting" step in the recruiter onboarding checklist would prevent recurrences.

### 5.4 — Strip empty paragraphs and stray `<br />` tags (medium priority)
- Run a one-time pass through the CMS to delete `<p></p>` from the 51 postings flagged in Section 4.3.
- Remove `<br />` tags that appear at the end of `<li><p>…</p></li>` items (Director, Growth Marketing - Commercial; Revenue Operations Engineer, Quoting Systems; GTM Data Engineer Intern; Engineering Manager - Autonomy; Aviation Compliance Lead; Senior Manager, Deployment Operations).
- Replace `<br /><br />` chains with real `<p>` elements (Director, Growth Marketing - Commercial; Director of Product Management, DFR; Autonomy Engineer - Deep Learning Infrastructure/Model Acceleration; Autonomy Software Engineer; Senior Technical Recruiter - Hardware Operations).

### 5.5 — Standardise the casing and punctuation of standard labels (medium priority)
Site-wide find-and-replace:

| Replace | With |
|---|---|
| `About the Role:` / `About The Role` / `About the Role` | `About the role:` |
| `How You'll Make an Impact:` / `How you'll make an impact` (no colon) / `How you will make an impact:` | `How you'll make an impact:` |
| `What Makes You a Good Fit:` / `What Makes You A Good Fit:` / `What makes you a good fit` (no colon) / `What would make you a good fit:` / `What Makes Your a Good Fit:` (typo) | `What makes you a good fit:` |
| `Bonus Points:` / `Nice to have:` / `Nice To Haves:` / `Preferred Qualifications:` (when used as the bonus section) | `Bonus points for:` |

### 5.6 — Fix double-spaces in titles (low priority but visible)
Titles "Senior Software Engineer,  Infrastructure", "Senior Software Engineer,  Data Platform", and "Staff Global Supply Manager,  Mechanicals" contain two consecutive spaces after the comma. Trim to one space — these appear in the page `<title>`, `<h1>`, and the index list, so the typo is visible in three places and is also indexed by Google.

### 5.7 — Reconcile duplicate roles (process-level)
There are 8 cases where the same role title exists twice with different IDs. In several cases the two versions disagree on:
- title casing of headings (one is sentence case, the other title case),
- presence of `<h2>` headings (one uses them, the other does not),
- punctuation (e.g. "Sr/Staff" vs. "Senior/Staff", `-` vs. `–`).

Either merge duplicates into a single posting with location toggles, or sync the body content so the two versions only differ in the location field.

### 5.8 — Shorten the location string (optional)
Every posting renders its location as e.g. "San Mateo, California, United States - Full-time". This is visually long and pushes the body further down on mobile. Most companies use "San Mateo, CA · Full-time" or "San Mateo, CA — Full-time". This is a one-line CSS / template change because all 118 postings already use the same `type-body-2` element.

### 5.9 — Add a CI/lint step
A 50-line script in the CMS publish hook can prevent regressions:
- Reject postings that contain `<h1>`, `<h2>`, or `<h3>` inside the body.
- Reject `<u>` and `<em>` inside the body (or whitelist a known set of phrases).
- Warn on `<p></p>`, on `<br />` adjacent to `</li>`, and on consecutive `<br /><br />`.
- Warn on standard-label text that is not in the canonical casing.
- Warn when the standard "Skydio is the leading US drone…" intro is missing.

---

## Appendix A — Per-posting issue list

The full list of 69 postings with at least one formatting issue, sorted by severity, is below. Each issue is described in the bucket it falls under (heading-tag misuse, run-together text, empty paragraphs, stray `<br/>`, mixed punctuation, underline / italic styling).

> Note: The two-postings-with-the-same-title cases listed below are distinct job-page IDs, so each one is included separately.

### Director, Growth Marketing - Commercial
- 2 stray empty `<p></p>` paragraphs producing extra vertical whitespace
- Inconsistent header punctuation within posting: 4 with colon inside `<strong>`, 1 with no colon
- 7 bullets end with stray `<br />` tag, producing inconsistent inter-bullet spacing
- High count of inline `<br />` tags (8) used in lieu of paragraph breaks
- Uses italic styling: "Ability to be in our San Mateo, CA office 3 days per week"

### Revenue Operations Engineer, Quoting Systems
- Uses `<h2>` inside body (renders ~22-32 px, much larger than peer postings)
- Has 1 run-on block where multiple paragraphs were merged into one
- 2 stray empty paragraphs
- 3 bullets end with stray `<br />` tag
- High count of inline `<br />` tags (4)

### Senior Manager, Deployment Operations
- Uses `<h2>` inside body
- Uses `<h3>` inside body (sub-headings)
- 1 run-on block (intro + Location + Travel Requirements + 4 percentage-weighted sub-sections all merged)
- 5 stray empty paragraphs

### Senior Product Manager, Platform & Infrastructure
- 2 run-on blocks (one ~1,400 chars, another ~2,000 chars)
- 6 stray empty paragraphs
- Inconsistent header punctuation: 2 colon-inside, 1 no-colon

### Staff Product Manager, Platform & Infrastructure
- 2 run-on blocks (mirrors Senior PM Platform & Infrastructure)
- 6 stray empty paragraphs
- Inconsistent header punctuation: 2 colon-inside, 1 no-colon

### Software Engineer - Cloud Simulation & Full-Stack (San Mateo)
- Uses `<h2>` inside body
- 2 stray empty paragraphs

### Software Engineer - Cloud Simulation & Full-Stack (Zurich)
- Uses `<h2>` inside body
- 2 stray empty paragraphs

### Software Engineer - Simulation & Robotics Engineer (Zurich)
- Uses `<h3>` inside body
- 2 stray empty paragraphs

### Software Engineer - Simulation & Robotics Engineer (San Mateo)
- Uses `<h3>` inside body
- 2 stray empty paragraphs

### Software Engineer - Autonomy Infrastructure, Systems and Tools (San Mateo)
- Uses `<h2>` inside body

### Software Engineer - Autonomy Infrastructure, Systems and Tools (Zurich)
- Uses `<h2>` inside body

### Senior Technical Support Representative – Japan
- Uses `<h1>` inside body (renders ~28-48 px — same as the page title; unique to this posting)

### Communications Manager
- Uses `<h2>` inside body
- 3 stray empty paragraphs

### Deployment Coordinator
- Uses `<h2>` inside body
- 4 stray empty paragraphs

### Senior Buyer
- Uses `<h2>` inside body
- 3 stray empty paragraphs

### Aviation Compliance Lead
- Uses `<h2>` inside body
- 1 bullet ends with stray `<br />`

### Aviation Regulatory Program Manager
- Uses `<h2>` inside body
- 2 stray empty paragraphs

### Field Marketing Event Manager
- Uses `<h3>` inside body

### Project Manager, Workplace
- Uses `<h3>` inside body
- Inconsistent header punctuation: 1 colon-inside, 5 no-colon

### PhD Autonomy Engineer Intern – Planning & Controls (Reinforcement Learning)
- Uses `<h3>` inside body
- 1 run-on block

### Manufacturing Business Process Intern
- 3 stray empty paragraphs
- Inconsistent header punctuation: 3 colon-inside, 1 no-colon
- Uses italic styling on three numbered project labels

### Lead Staff Electrical Engineer (F10 Program)
- 1 run-on block
- 2 stray empty paragraphs
- Uses underline styling: "Skydio F10 Program"

### Senior NPI Product Quality Engineer
- Uses underline styling: "Please Note:"
- Uses italic styling on the same "Please Note:" (italic + bold + underline triple-stack)

### Senior Technical Recruiter
- Uses underline styling: "PLEASE NOTE:"

### Senior Technical Recruiter - Hardware Operations
- 1 run-on block
- High count of inline `<br />` tags (4)
- Uses underline styling: "PLEASE NOTE:"

### Staff Technical Recruiter
- Uses underline styling: "PLEASE NOTE:"

### Senior Software Engineer, Full Stack
- Inconsistent header punctuation: 4 colon-inside, 1 colon-outside
- Uses underline styling: "public API"

### Staff Software Engineer, Full Stack
- Inconsistent header punctuation: 3 colon-inside, 1 colon-outside

### Senior Software Engineer, Frontend
- Inconsistent header punctuation: 4 colon-inside, 1 colon-outside

### Senior Software Engineer, Data Platform
- Inconsistent header punctuation: 3 colon-inside, 1 no-colon

### Director of Product Management, Drone as First Responder (DFR)
- 1 run-on block (intro + Location disclaimer + start of "How you'll make an impact:")
- High count of inline `<br />` tags (4)

### Senior People Analytics Analyst
- 2 run-on blocks
- Inconsistent header punctuation: 2 colon-inside, 2 no-colon
- Typo: "What Makes Your a Good Fit:" (should be "Your" → "You")

### GTM Data Engineer Intern
- 3 run-on blocks
- 2 stray empty paragraphs
- 2 bullets end with stray `<br />`

### GTM Enablement Associate
- 1 run-on block

### Sales Planning Analyst Intern
- 1 run-on block

### Senior Brand Designer (Contract)
- 1 run-on block
- 3 stray empty paragraphs
- Inconsistent header punctuation: 3 colon-inside, 1 no-colon

### Workplace Experience Coordinator Part-Time
- 1 run-on block
- Inconsistent header punctuation: 1 colon-inside, 4 no-colon

### Hardware Operations Program Manager
- 1 run-on block
- 3 stray empty paragraphs

### Hardware Technician
- 1 run-on block
- 3 stray empty paragraphs

### Electric Motor / Propulsion Engineer
- 1 run-on block
- Uses italic styling: "Please note:"

### Product Design Engineer (All Levels)
- 1 run-on block

### Product Support Engineer
- 1 run-on block
- 2 stray empty paragraphs

### Product Support Engineer Intern
- 1 run-on block
- 3 stray empty paragraphs

### Technical Support Specialist - West Coast
- 1 run-on block

### Autonomy Engineer - Deep Learning Infrastructure (Zurich variant)
- 1 run-on block
- High count of inline `<br />` tags (6)

### Autonomy Engineer - Deep Learning Infrastructure (San Mateo variant)
- High count of inline `<br />` tags (8)

### Autonomy Engineer - Deep Learning Model Acceleration (Zurich)
- 1 run-on block
- High count of inline `<br />` tags (6)

### Autonomy Engineer - Deep Learning Model Acceleration (San Mateo)
- 1 run-on block
- High count of inline `<br />` tags (6)

### Senior Autonomy Engineer - Deep Learning (Zurich)
- 1 run-on block

### Senior Autonomy Engineer - Deep Learning (San Mateo)
- 1 run-on block

### Autonomy Software Engineer
- 1 run-on block
- High count of inline `<br />` tags (4)

### Senior Software Engineer, Infrastructure
- 1 run-on block (About the team + About the role merged)

### Software Engineer - Infrastructure
- 1 run-on block (mirrors the Senior version)

### Senior Staff Product Manager, Drone Hardware Platforms & Sensors
- Inconsistent header punctuation: 2 colon-inside, 1 no-colon

### Staff Product Manager, Cameras & Sensors
- Inconsistent header punctuation: 1 colon-inside, 2 no-colon

### Mission Success Operations Manager
- Inconsistent header punctuation: 3 colon-inside, 1 no-colon

### Success Systems Specialist
- Inconsistent header punctuation: 4 colon-inside, 4 no-colon

### Enterprise Account Manager (MoD/MoI) – EMEA (Germany)
- Inconsistent header punctuation: 3 colon-inside, 1 no-colon

### Enterprise Account Manager (MoD/MoI) – EMEA (Switzerland)
- Inconsistent header punctuation: 3 colon-inside, 1 no-colon

### Enterprise Account Manager (MoD/MoI) – EMEA (Finland)
- Inconsistent header punctuation: 3 colon-inside, 1 no-colon

### Solutions Engineer – Government & National Security – Germany
- Inconsistent header punctuation: 3 colon-inside, 1 no-colon

### Solutions Engineer – Government & National Security – Switzerland
- Inconsistent header punctuation: 3 colon-inside, 1 no-colon

### Solutions Engineer – Government & National Security – Finland
- Inconsistent header punctuation: 3 colon-inside, 1 no-colon

### Senior Revenue Operations Manager
- 2 stray empty paragraphs

### Senior Autonomy Engineer - Data Curation
- 4 stray empty paragraphs

### Senior/Staff Embedded Software Engineer – Camera Systems
- 4 stray empty paragraphs

### Sr/Staff Embedded Software Engineer - Camera Systems
- 4 stray empty paragraphs

### Senior Software Engineer - Mobile Platform
- 3 stray empty paragraphs

### Field Support Representative (Southwest, Remote)
- 2 stray empty paragraphs

### Engineering Manager - Autonomy
- 1 bullet ends with stray `<br />`

### Production Manager, PM Shift
- 3 stray empty paragraphs

### Program Manager, Major Deployments (Hawaii)
- 3 stray empty paragraphs

### Program Manager, Major Deployments (Mid Atlantic)
- 3 stray empty paragraphs

### Program Manager, Major Deployments (South East)
- 3 stray empty paragraphs

### Deployment Engineer - Southeast
- 1 run-on block
- 5 stray empty paragraphs

---

## Appendix B — Postings with no formatting issues found

The remaining **49 of 118 postings** matched the canonical template (sentence-case `<p><strong>…</strong></p>` headings, no `<h*>` tags in body, no stray `<br/>` or empty `<p>`, no `<u>`/`<em>`, no run-together blocks). Examples:

- Software Engineer, Full Stack
- Sr/Staff Embedded Software Engineer - Camera Systems (Tampere, Finland posting)
- Wireless Software Engineer
- RF Design Engineer
- Senior Wireless Systems Performance Engineer
- Electrical Engineer Intern
- PCB Layout Engineer
- Senior Customer Support Representative - India
- Senior Software Engineer - Embedded
- Software Engineer - Embedded
- Staff Software Engineer - Embedded
- Senior Software Engineer - Security
- Field Support Representative
- Customer Success Manager, DFR Majors - Northeast
- Mission Success Operations Manager (re-check: only header-punctuation issue)
- Workplace Project Manager (Workplace Experience Coordinator Zurich)
- Senior Director, Product Marketing
- Director, Growth Marketing - Commercial — *not in this list; has issues, see Appendix A*

(See `/tmp/jobs_data.json` in the audit data set for the full machine-readable list of all 118 postings with their parsed structure.)
