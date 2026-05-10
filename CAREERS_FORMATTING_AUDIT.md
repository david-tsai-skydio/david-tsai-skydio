# Skydio Careers Page — Job Posting Formatting Audit

**Source:** https://www.skydio.com/careers
**Postings analyzed:** 112 (every open posting listed on the careers index)
**Scope:** content of each posting from the start of the job description through the end of the "What makes you a good fit" / qualifications section, stopping immediately before the "Compensation" block. The 7 postings that have no "Compensation" block (mostly EU/Asia and intern roles) were analyzed in full.
**Method:** raw HTML for every posting was downloaded and the markup of the description container (`<div class="prose block-content">`) was diffed across all postings. Because every posting renders inside the same `.prose` CSS scope, all visible font sizes, weights, colors, line-heights and alignment are inherited from the same stylesheet — so the *visible* differences come almost entirely from the underlying HTML markup that the recruiter or recruiting coordinator pasted into Ashby. The findings below describe the markup-level inconsistencies and what they look like to a candidate on the page.

## 1. Executive Summary

| Area | Result |
| --- | --- |
| Inline font-size overrides | 0 / 112 — clean |
| Inline color overrides | 0 / 112 — clean |
| Inline `style="..."` attributes | 0 / 112 — clean |
| Inline `<font>` tags | 0 / 112 — clean |
| Bullet-list item structure (`<li><p>...</p></li>`) | 112 / 112 — uniform |
| Canonical opening paragraph ("Skydio is the leading US drone company…") | 112 / 112 — uniform |
| **Section heading element used** (`<p><strong>` vs `<h1>` / `<h2>` / `<h3>`) | **4 different elements in use across 14 postings — the largest visible inconsistency** |
| **Casing of section labels** (e.g. "About the role" vs "About the Role") | **mixed across the catalog** |
| **Apostrophe character in "How You'll Make an Impact"** | 53 straight + 44 curly — visually identical, but inconsistent at the character level |
| **Stray `<br>` tags inside paragraphs** | **47 / 112** — uneven vertical spacing |
| Intro paragraph hyperlinks present | 53 / 112 (current) + 12 / 112 (old set) + 47 / 112 (none) |
| Postings with `<em>` (italic) sprinkled in body text | 3 / 112 |
| Postings missing one of the canonical sections | ~15 (alt-template postings) |

**Bottom line:** the careers page itself is well-templated — every posting starts with the same intro paragraph, every bullet list is structured the same way, and there are no rogue inline font sizes/colors. Visible inconsistencies are almost entirely caused by *which HTML element a recruiter chose for section headings*, *which casing they typed*, *which copy of the intro paragraph they pasted (with or without the four solution links)*, and *whether they pressed Shift-Enter (`<br>`) instead of Enter (`<p>`) when adding line breaks*. A handful of postings clearly come from a different copy-template (Hardware "Areas of Responsibility" template vs. the standard "About the role / How you'll make an impact / What makes you a good fit" template).

## 2. Detected Inconsistencies (with severity)

### 2.1 Section headings rendered with different HTML elements ⚠️ HIGH

98 of the 112 postings use the *paragraph + bold* convention for section headings: `<p><strong>About the Role:</strong></p>`. With the site's default body type-scale this renders at roughly **16 px / 600 weight**, the same height as a regular paragraph. Fourteen postings instead use real heading elements, which the site's stylesheet renders much larger (`h1` ≈ 36 px, `h2` ≈ 28–30 px, `h3` ≈ 22–24 px depending on viewport). Anyone scrolling between two postings in adjacent browser tabs sees a jarring jump in heading size:

| Heading element used inside the description | # postings | Effective size relative to body |
| --- | --- | --- |
| `<p><strong>…</strong></p>` (norm) | 98 | ≈ 16 px / bold (same as paragraph) |
| `<h3>…</h3>` | 4 | ≈ 22–24 px / bold |
| `<h2>…</h2>` | 9 | ≈ 28–30 px / bold |
| `<h1>…</h1>` | 1 | ≈ 36 px / bold (same size as the JOB TITLE at top of page!) |

Specific outliers:

* **`<h1>` (single posting — the most extreme outlier)**
  * `Senior Technical Support Representative – Japan` (Customer Support, Tokyo) — every section title ("About the role:", "How you'll make an impact:", "What would make you a good fit:") is rendered with `<h1>`, so each label appears at the same visual weight as the job-title hero. Looks broken.
* **`<h2>` (9 postings):**
  * Autonomy: `Software Engineer - Autonomy Infrastructure, Systems and Tools` (San Mateo & Zurich), `Software Engineer - Cloud Simulation & Full-Stack` (San Mateo & Zurich)
  * Manufacturing: `Senior Buyer` (Hayward)
  * Marketing: `Communications Manager` (US Remote)
  * Policy & Regulatory Affairs: `Aviation Compliance Lead` (San Mateo), `Aviation Regulatory Program Manager` (US Remote)
  * Professional Services and Training: `Deployment Coordinator` (US Remote)
  * Sales: `Revenue Operations Engineer, Quoting Systems` (San Mateo)
* **`<h3>` (4 postings):**
  * Autonomy: `Software Engineer - Simulation & Robotics Engineer` (San Mateo & Zurich), `PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning)` (Zurich)
  * Facilities: `Project Manager, Workplace` (San Mateo)
  * Marketing: `Field Marketing Event Manager` (San Mateo)

### 2.2 Casing inconsistencies in section labels ⚠️ MEDIUM

Even within the dominant `<p><strong>` template, the wording / casing of the same three section headings drifts:

| Section | Variants found (count) |
| --- | --- |
| About the role | "About the role" (~50), "About the Role" (~33 — incl. h2/h3), "About The Role" (1) |
| How you'll make an impact | "How you'll make an impact" (27 — straight `'`), "How you'll make an impact" (13 — curly `'`), "How You'll Make an Impact" (20 + 1 — title-case curly), "How you will make an impact" (3) |
| What makes you a good fit | "What makes you a good fit" (57), "What Makes You a Good Fit" (22), "What Makes You A Good Fit" (3), "What would make you a good fit" (6), "What Would Make You a Good Fit" (2), "What makes you a strong fit" (2) |

The split between sentence-case and Title-Case is roughly 60/40 across the catalog. The straight-vs-curly apostrophe inconsistency is invisible to the eye but breaks anchor-link slugs, search, and CSS first-letter targeting — and shows that two different copy templates are in circulation.

### 2.3 Stray `<br>` tags inside paragraphs ⚠️ MEDIUM

65 postings have **zero** `<br>` tags (the clean default). The remaining 47 use 1–8 `<br>` tags. A `<br>` inside a `<p>` produces a single-line break — i.e. **less vertical space than a paragraph break**, so paragraphs in those postings sit visibly closer together than in the rest of the catalog.

Distribution of `<br>` count per posting:

```
  0 br : 65 postings (clean)
  1 br : 18 postings
  2 br : 15 postings
  3 br :  3 postings
  4 br :  5 postings
  5 br :  1 posting
  6 br :  3 postings
  8 br :  2 postings  <- worst offenders
```

The 8-`<br>` postings are: `Autonomy Engineer - Deep Learning Infrastructure` (San Mateo) and `Director, Growth Marketing - Commercial`. Their description body uses single-line breaks where every other posting uses paragraph breaks, making the spacing noticeably tighter.

### 2.4 Intro paragraph: link set is inconsistent ⚠️ MEDIUM

All 112 postings open with the *same* intro paragraph ("Skydio is the leading US drone company and the world leader in autonomous flight…"). However, three different versions of the paragraph are in circulation:

| Version | # postings | Behavior |
| --- | --- | --- |
| Current — links "utility inspectors", "first responders", "soldiers in battlefield scenarios", "beyond" → energy-and-utilities / public-safety / national-security/tactical-isr / solutions | 53 | Four blue underlined links |
| Older — same anchor text, but the third link points to `/solutions/defense` (a now-redirecting URL) | 12 | Four blue underlined links, one stale |
| No-links version | 47 | Plain text — the same words appear without underline/blue color |

Side-by-side, 47 postings appear text-only at the top while 65 have brightly colored hyperlinks — the most visible top-of-page inconsistency on the careers site.

### 2.5 Wholly different content templates ⚠️ MEDIUM

Six Autonomy postings (and one Sales posting) use a different recruiter template entirely. Instead of the canonical *About the Role / How you'll make an impact / What makes you a good fit* trio, they use:

* **`<h2>` "Areas of Responsibility / What You'll Do / Qualifications / Bonus Experience" template** (4 postings, all Autonomy):
  * `Software Engineer - Autonomy Infrastructure, Systems and Tools` (San Mateo & Zurich)
  * `Software Engineer - Cloud Simulation & Full-Stack` (San Mateo & Zurich)
* **`<h3>` "Areas of Responsibility / What You'll Do / Qualifications / Bonus Experience" template** (2 postings):
  * `Software Engineer - Simulation & Robotics Engineer` (San Mateo & Zurich)
* **`<h2>` "What you'll drive (scope) / Day-to-day responsibilities / Tech stack you'll work with / What you'll bring / Reporting & Working Model" template** (1 posting):
  * `Revenue Operations Engineer, Quoting Systems` (Sales, San Mateo)
* **`<h3>` "Customer Summit Planning & Execution / Field Marketing & Trade Show Support / Relationship Building & Internal Collaboration / Required Experience / Preferred Skills & Experience / Interpersonal & Professional Skills / Physical & Travel Requirements" template** (1 posting):
  * `Field Marketing Event Manager` (Marketing, San Mateo) — uses 7 sub-headings, more than any other posting.
* **`<h3>` "About the Role / How You'll Operate" template** (1 posting):
  * `Project Manager, Workplace` (Facilities, San Mateo) — replaces "How you'll make an impact" with "How You'll Operate" and never declares a "What makes you a good fit" section at all.
* **`<h2>` "How you will make an impact / What makes you a strong fit" template** (1 posting):
  * `Senior Buyer` (Manufacturing, Hayward) — has no "About the role" section at all; the description launches straight into bullet points.
* **`<h3>` "How you'll make an impact / What makes this internship different / What makes you a strong fit" template** (1 posting):
  * `PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning)` (Zurich) — adds an "internship different" section no other internship uses.

### 2.6 Optional "About the Team" section is unevenly applied ⚠️ LOW

13 of 112 postings include an extra "About the Team" / "About the team" header (between the intro and "About the Role"). The 13 are concentrated in Software / Embedded / Cloud / Mobile teams. Other roles on the same teams omit it. This produces an extra section break in those 13 listings that does not appear in equivalent listings.

### 2.7 Run-on / mis-applied bold tags ⚠️ LOW (but visible)

* **`Senior Brand Designer (Contract)`** (Marketing) — the entire opening paragraph (234 characters: *"We're looking for an experienced Senior Brand Designer to help shape how Skydio shows up in the world…"*) is wrapped in a single `<strong>` tag. It renders as a wall of bold text, which no other posting does.
* **5 postings have stacked bold-paragraph headers** (two `<p><strong>...</strong></p>` blocks back-to-back with no body text between them, often because a "Work Location" or "This role must be based in…" notice was added as its own bold block right next to the next section header):
  * `Workplace Experience Coordinator Part-Time` (People & Recruiting, Zurich)
  * `Success Systems Specialist` (Professional Services and Training, US Remote)
  * `Enterprise Account Manager (MoD/MoI) – EMEA (Finland)` (Sales)
  * `Enterprise Account Manager (MoD/MoI) – EMEA (Germany)` (Sales)
  * `Enterprise Account Manager (MoD/MoI) – EMEA (Switzerland)` (Sales)
* **17 postings have a trailing space inside `<strong>...</strong>`** (e.g. `<strong>About the Role: </strong>` instead of `<strong>About the Role:</strong>`). Visually invisible most of the time, but if anyone ever links one of those headings or applies an underline style, the underline/colour bleeds into the trailing space.

### 2.8 Italics (`<em>`) used in only 3 postings ⚠️ LOW

No posting uses italics for emphasis except:
* `Electric Motor / Propulsion Engineer` (Hardware) — 1 italic phrase
* `Senior NPI Product Quality Engineer` (Manufacturing) — 1 italic phrase
* `Director, Growth Marketing - Commercial` (Marketing) — 1 italic phrase

Three is so few that italics functionally read as a typo when they appear.

### 2.9 Length distribution (sanity check) ✅

Pre-compensation length ranges from **~1,950 characters** (`Autonomy Engineer Intern Fall 2026`, `Senior Autonomy Engineer - Controls`) to **~6,800 characters** (`Success Systems Specialist`). Median ~3,900. Paragraph count ranges 14–41, median 24. The longest postings (`Success Systems Specialist`, `Deployment Engineer - Southeast`, `Director, Growth Marketing - Commercial`, `Field Marketing Event Manager`, `Senior Brand Designer (Contract)`) are 2× the catalog median. Length itself isn't a formatting bug, but the longest postings are the same ones that drift hardest from the standard template (2.1 / 2.5 / 2.7 above).

## 3. Recommendations (in order of impact)

1. **Pick one section-heading element and convert all 112 postings to it.** The current 4-way split (`<h1>` / `<h2>` / `<h3>` / `<p><strong>`) is the single most visible inconsistency. Recommended target: keep the existing `<p><strong>About the Role:</strong></p>` convention used by 87 % of postings; it matches the body type scale and avoids the "headline as big as the page title" problem on the Tokyo Senior Tech Support posting. Alternatively, if the team prefers real headings, standardize on `<h3>` and override `.prose h3` size in CSS so it lands at ~18 px.
2. **Lock down the canonical section names and casing.** Pick exactly one of:
   * "About the Role"
   * "How You'll Make an Impact" (use one apostrophe — recommend curly `'` to match marketing copy)
   * "What Makes You a Good Fit"
   …and have recruiters paste from a single, governed boilerplate. Today the catalog has 4 spellings of "About the role", 6 spellings of "How you'll make an impact" (split between straight and curly apostrophes), and 6 spellings of "What makes you a good fit".
3. **Replace the 47 link-less intro paragraphs with the linked version, and update the 12 stale `/solutions/defense` links** to `/solutions/national-security/tactical-isr`. This restores brand consistency and removes a stale URL.
4. **Strip all `<br>` tags** from the 47 postings that use them. Replace with proper paragraph breaks so vertical rhythm matches the other 65 postings. The two 8-`<br>` outliers (`Autonomy Engineer - Deep Learning Infrastructure` San Mateo, `Director, Growth Marketing - Commercial`) should be reformatted first.
5. **Migrate the 7 alt-template postings to the standard template.** Map "Areas of Responsibility" → "How You'll Make an Impact"; map "Qualifications" / "Bonus Experience" → "What Makes You a Good Fit" + "Bonus Points"; merge "What you'll drive (scope)" + "Day-to-day responsibilities" + "Tech stack you'll work with" into "How You'll Make an Impact"; promote "How You'll Operate" / "What makes this internship different" into the canonical 3-section structure.
6. **Fix the four most visible single-posting bugs** before anything else (these are the listings most likely to be flagged by candidates):
   * `Senior Technical Support Representative – Japan` — remove `<h1>` headings.
   * `Senior Brand Designer (Contract)` — un-bold the opening paragraph.
   * `Field Marketing Event Manager` — collapse 7 `<h3>` sub-headings into the canonical 3.
   * `Senior Buyer` — add an "About the Role" section so the page doesn't open straight into bullets.
7. **Decide whether "About the Team" is part of the standard template.** Either include it on every Software/Embedded posting or remove it from the 13 that currently have it. Right now its presence depends on which recruiter cloned which posting.
8. **Stop using `<em>` for emphasis** in those 3 postings, or commit to italics as a documented style and apply it consistently. Today it reads as a copy-paste artifact.
9. **Trim trailing spaces inside `<strong>` tags** on the 17 postings that have them. Easy regex pass on the Ashby content store.
10. **Add a recruiter-facing template lint** in Ashby (or a pre-publish checklist) that enforces: canonical intro paragraph, no `<h1>/<h2>/<h3>` inside the description, standard 3 section headers in standard casing, no `<br>` inside `<p>`, no inline `style=""` attributes. The first 9 fixes will hold only if step 10 is in place.

## 4. Appendix — full per-posting flag table

Flags: `USES_H1` / `USES_H2` / `USES_H3` = description uses real heading elements (renders much larger than the norm); `BR=N` = N stray `<br>` tags inside paragraphs; `HAS_EM` = uses italic emphasis; `NO_INTRO_LINKS` = the four solution links are missing from the intro paragraph; `OLD_INTRO_LINKS` = intro uses the stale `/solutions/defense` URL; `NO_ABOUT_ROLE_HEADER` / `NO_IMPACT_HEADER` / `NO_FIT_HEADER` = the canonical section header is missing or renamed; `HAS_ABOUT_TEAM` = optional "About the Team" section is included; `NO_COMP_BLOCK` = posting has no Compensation block (whole posting was analyzed); `CASING:"X"` = section label uses a non-default casing.

| Department | Title | Location | Flags |
| --- | --- | --- | --- |
| Autonomy | [Autonomy Engineer - Deep Learning](https://www.skydio.com/jobs/cc83824e-a1cd-4bc7-9206-7264da9fbd61) | San Mateo, CA - Full-time | NO_INTRO_LINKS |
| Autonomy | [Autonomy Engineer - Deep Learning](https://www.skydio.com/jobs/ae12de71-0010-49d3-b171-c0b257e3b6c1) | Zurich, Switzerland - Full-time | BR=1, OLD_INTRO_LINKS |
| Autonomy | [Autonomy Engineer - Deep Learning Infrastructure](https://www.skydio.com/jobs/dcb04687-9b4f-425d-8c37-1111cf3ccf3d) | San Mateo, CA - Full-time | BR=8, OLD_INTRO_LINKS, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Autonomy | [Autonomy Engineer - Deep Learning Infrastructure](https://www.skydio.com/jobs/c051266c-3e00-4906-abd0-21f18db56b3f) | Zurich, Switzerland - Full-time | BR=6, NO_INTRO_LINKS, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Autonomy | [Autonomy Engineer - Deep Learning Model Acceleration](https://www.skydio.com/jobs/cd6d8410-419b-4713-8d4d-7eb72b134d5a) | San Mateo, CA - Full-time | BR=6, OLD_INTRO_LINKS, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Autonomy | [Autonomy Engineer - Deep Learning Model Acceleration](https://www.skydio.com/jobs/5892ea83-ad5a-480a-bd9f-2409bb0b644e) | Zurich, Switzerland - Full-time | BR=6, NO_INTRO_LINKS, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Autonomy | [Autonomy Engineer - Fixed Wing Planning & Controls](https://www.skydio.com/jobs/20754382-05e7-4cb6-a0f9-0daf9338ba78) | San Mateo, CA - Full-time | NO_INTRO_LINKS, CASING:"About the Role" |
| Autonomy | [Autonomy Engineer - ML & DL Infrastructure](https://www.skydio.com/jobs/b6be08f7-89c0-48dd-b427-f587f23dbf34) | San Mateo, CA - Full-time | CASING:"About the Role" |
| Autonomy | [Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026](https://www.skydio.com/jobs/c84945f0-b8e0-4272-b636-265d6611a8eb) | San Mateo, CA - Intern | BR=1, NO_FIT_HEADER |
| Autonomy | [Autonomy Engineer Intern - Deep Learning (Computational Photography)](https://www.skydio.com/jobs/d13e3179-e646-4873-84a6-d492a692bc25) | San Mateo, CA - Intern | NO_COMP_BLOCK |
| Autonomy | [Autonomy Engineer Intern - Deep Learning (Computational Photography)](https://www.skydio.com/jobs/6280ab1d-147d-4f39-8618-a216c18ce0f9) | Zurich, Switzerland - Intern | NO_COMP_BLOCK |
| Autonomy | [Autonomy Engineer Intern Fall 2026](https://www.skydio.com/jobs/17f6173b-c96f-4b02-a6b5-da0a91ad95e5) | San Mateo, CA - Intern | standard |
| Autonomy | [Autonomy Software Engineer](https://www.skydio.com/jobs/a48fe41b-030b-4f11-bf25-df7446151854) | San Mateo, CA - Full-time | BR=4, OLD_INTRO_LINKS, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Autonomy | [Engineering Manager - Autonomy](https://www.skydio.com/jobs/849ae77c-5ca2-42b5-812b-8b3ad4524a89) | San Mateo, CA - Full-time | BR=1, OLD_INTRO_LINKS |
| Autonomy | [PhD Autonomy Engineer Intern - Deep Learning or Computer Vision](https://www.skydio.com/jobs/8d3979a8-c791-4825-8cf4-9b25479b9519) | San Mateo, CA - Intern | BR=1, NO_INTRO_LINKS, NO_FIT_HEADER |
| Autonomy | [PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning)](https://www.skydio.com/jobs/f8225008-00b5-415e-9a48-c9b6eba9363c) | Zurich, Switzerland - Intern | USES_H3, OLD_INTRO_LINKS, NO_FIT_HEADER |
| Autonomy | [Senior Autonomy Engineer - Controls](https://www.skydio.com/jobs/58b4cdf6-5630-4dd0-aab3-a1ed4d599466) | San Mateo, CA - Full-time | NO_INTRO_LINKS, CASING:"About the Role" |
| Autonomy | [Senior Autonomy Engineer - Data Curation](https://www.skydio.com/jobs/562c2e8f-c366-4149-945e-0f42f4264b5f) | San Mateo, CA - Full-time | NO_INTRO_LINKS, CASING:"About the Role" |
| Autonomy | [Senior Autonomy Engineer - Deep Learning](https://www.skydio.com/jobs/a6421d3e-fdd0-48d6-8d8f-3fd605cdf09f) | San Mateo, CA - Full-time | BR=2, NO_INTRO_LINKS, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Autonomy | [Senior Autonomy Engineer - Deep Learning](https://www.skydio.com/jobs/a6973c57-132a-4a0d-b130-02d2bdaecd2a) | Zurich, Switzerland - Full-time | BR=3, NO_INTRO_LINKS, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Autonomy | [Software Engineer - Autonomy Infrastructure, Systems and Tools](https://www.skydio.com/jobs/9e42a7af-6369-4036-ae6f-6626ee3a4fb3) | San Mateo, CA - Full-time | USES_H2, NO_INTRO_LINKS, NO_IMPACT_HEADER, NO_FIT_HEADER, CASING:"About the Role" |
| Autonomy | [Software Engineer - Autonomy Infrastructure, Systems and Tools](https://www.skydio.com/jobs/9fc135c5-7a87-410d-8323-e0f918585ebc) | Zurich, Switzerland - Full-time | USES_H2, NO_INTRO_LINKS, NO_IMPACT_HEADER, NO_FIT_HEADER, CASING:"About the Role" |
| Autonomy | [Software Engineer - Cloud Simulation & Full-Stack](https://www.skydio.com/jobs/7d7dfadc-c6fd-4958-8d59-004a91bff55e) | San Mateo, CA - Full-time | USES_H2, NO_INTRO_LINKS, NO_IMPACT_HEADER, NO_FIT_HEADER, CASING:"About the Role" |
| Autonomy | [Software Engineer - Cloud Simulation & Full-Stack](https://www.skydio.com/jobs/948bddb5-4679-4c7c-bf57-960a0fd1a7ed) | Zurich, Switzerland - Full-time | USES_H2, NO_INTRO_LINKS, NO_IMPACT_HEADER, NO_FIT_HEADER, CASING:"About the Role" |
| Autonomy | [Software Engineer - Simulation & Robotics Engineer](https://www.skydio.com/jobs/7a8f3e6c-d576-41af-a81e-bf4fe20da12a) | San Mateo, CA - Full-time | USES_H3, NO_INTRO_LINKS, NO_IMPACT_HEADER, NO_FIT_HEADER, CASING:"About the Role" |
| Autonomy | [Software Engineer - Simulation & Robotics Engineer](https://www.skydio.com/jobs/abd4addb-2d11-4207-b3a2-446a09121e39) | Zurich, Switzerland - Full-time | USES_H3, NO_INTRO_LINKS, NO_IMPACT_HEADER, NO_FIT_HEADER, CASING:"About the Role" |
| Connectivity | [RF Design Engineer](https://www.skydio.com/jobs/f72f1fa5-d3d6-459e-8722-a94ce92ad1c8) | San Mateo, CA - Full-time | CASING:"About the Role" |
| Connectivity | [Senior Wireless Systems Performance Engineer](https://www.skydio.com/jobs/f1ecf164-714c-4f1a-b672-d763f5724c03) | San Mateo, CA - Full-time | standard |
| Connectivity | [Wireless Hardware Engineer Intern](https://www.skydio.com/jobs/5e1057a4-214f-4783-b676-c1315cfa81ea) | San Mateo, CA - Intern | BR=5, NO_IMPACT_HEADER, NO_COMP_BLOCK |
| Connectivity | [Wireless Software Engineer](https://www.skydio.com/jobs/04fde92b-6a2b-4638-adc2-e8fa91cc1a49) | San Mateo, CA - Full-time | standard |
| Customer Support | [Field Support Representative](https://www.skydio.com/jobs/b053b0e2-005c-4e77-95f3-26c7354e6095) | US Remote - Full-time | HAS_ABOUT_TEAM |
| Customer Support | [Field Support Representative (Southwest, Remote)](https://www.skydio.com/jobs/9b93e7c2-e5d5-48b2-a2d2-8df71e0d8357) | US Remote - Full-time | NO_IMPACT_HEADER |
| Customer Support | [Product Support Engineer](https://www.skydio.com/jobs/a4f131a0-4dde-46ce-85a1-c83fc3e0f21e) | San Mateo, CA - Full-time | BR=2, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Customer Support | [Product Support Engineer Intern](https://www.skydio.com/jobs/8df0689e-a489-4c72-a1f7-09dfe59745b8) | San Mateo, CA - Intern | BR=2, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Customer Support | [Senior Customer Support Representative - India](https://www.skydio.com/jobs/bb7a9c5c-8dbb-4a2f-9d7d-db9ab1f707b0) | Bangalore, India - Full-time | NO_IMPACT_HEADER |
| Customer Support | [Senior Technical Support Representative - Japan](https://www.skydio.com/jobs/f714e85f-31df-494e-bac4-1dd61d4d6066) | Tokyo, Japan - Full-time | USES_H1, BR=2, NO_COMP_BLOCK |
| Customer Support | [Technical Support Specialist - West Coast](https://www.skydio.com/jobs/3ac81a34-b7fe-4142-9d29-12bcc1376182) | US Remote - Full-time | NO_INTRO_LINKS, NO_IMPACT_HEADER, HAS_ABOUT_TEAM |
| Facilities | [Project Manager, Workplace](https://www.skydio.com/jobs/ca17c12d-18df-48dc-83a3-e0d8e06aa451) | San Mateo, CA - Full-time | USES_H3, NO_IMPACT_HEADER, NO_FIT_HEADER, CASING:"About the Role" |
| Hardware | [Electric Motor / Propulsion Engineer](https://www.skydio.com/jobs/847c1abe-b3b6-4e97-bc0e-e3f46437287a) | San Mateo, CA - Full-time | BR=1, HAS_EM, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Hardware | [Electrical Engineer (Sustaining/Validation)](https://www.skydio.com/jobs/8e50c7da-2868-4383-af1f-920584d537fc) | San Mateo, CA - Full-time | BR=1, NO_IMPACT_HEADER |
| Hardware | [Electrical Engineer (all levels)](https://www.skydio.com/jobs/f0c26a3c-d999-4dc2-8812-b3835f633ded) | San Mateo, CA - Full-time | BR=2, NO_IMPACT_HEADER |
| Hardware | [Hardware Technician](https://www.skydio.com/jobs/6d5e666b-a0b7-45d4-a4de-45aef141ce10) | San Mateo, CA - Full-time | NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Hardware | [Hardware Test and Reliability Intern](https://www.skydio.com/jobs/4a1441bf-6979-46d0-a466-d9b8fd0a9762) | San Mateo, CA - Intern | standard |
| Hardware | [Lead Staff Electrical Engineer (F10 Program)](https://www.skydio.com/jobs/1bbcf144-7057-4a6e-9d51-4924bfda52b9) | San Mateo, CA - Full-time | BR=1, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Hardware | [PCB Layout Engineer](https://www.skydio.com/jobs/eb2f4124-9bd6-49f9-9636-03152c573f7d) | San Mateo, CA - Full-time | BR=2, NO_IMPACT_HEADER |
| Hardware | [Product Design Engineer (All Levels)](https://www.skydio.com/jobs/3f02ead1-8efe-4e3f-9c75-625e74ab57d1) | San Mateo, CA - Full-time | BR=1, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Hardware | [Senior Hardware Test and Reliability Engineer](https://www.skydio.com/jobs/c0e49670-51ca-461c-b0e2-4a06df01f692) | San Mateo, CA - Full-time | NO_INTRO_LINKS, NO_FIT_HEADER |
| Hardware | [Systems Integration and Test Engineer (Mid to Senior Level)](https://www.skydio.com/jobs/a1a60b27-53a8-455e-b467-712e01c532dc) | San Mateo, CA - Full-time | BR=1, NO_INTRO_LINKS, NO_FIT_HEADER |
| Manufacturing | [Head of Warehouse & Logistics Operations](https://www.skydio.com/jobs/0c1e9360-09dc-4c73-85bc-51aa72afd3ad) | US CA Production - Full-time | BR=1, NO_IMPACT_HEADER |
| Manufacturing | [Manufacturing Quality Supervisor](https://www.skydio.com/jobs/e0c94b6c-e08e-499b-aa62-b010993a9200) | Hayward, CA - Full-time | NO_INTRO_LINKS |
| Manufacturing | [Production Manager, PM Shift](https://www.skydio.com/jobs/7836de07-b630-438b-8db5-37a9ee618009) | Hayward, CA - Full-time | CASING:"About the Role" |
| Manufacturing | [Production Supervisor](https://www.skydio.com/jobs/90771bb1-f860-4b49-90ef-3a15bcd1fada) | Hayward, CA - Full-time | BR=2, NO_IMPACT_HEADER |
| Manufacturing | [RMA & Repair Program Manager](https://www.skydio.com/jobs/dab69dc5-1547-40f3-9e45-09d713403349) | Hayward, CA - Full-time | NO_INTRO_LINKS |
| Manufacturing | [Senior Buyer](https://www.skydio.com/jobs/5d32766d-990a-4c4c-a8c6-5e934dd8bd38) | Hayward, CA - Full-time | USES_H2, NO_FIT_HEADER |
| Manufacturing | [Senior NPI Product Quality Engineer](https://www.skydio.com/jobs/178a7e84-562e-40db-9abd-94bbf29159ca) | San Mateo, CA - Full-time | HAS_EM, NO_INTRO_LINKS |
| Marketing | [Communications Manager](https://www.skydio.com/jobs/50567d8d-2903-494f-8e08-7c8ca734dc3a) | US Remote - Full-time | USES_H2 |
| Marketing | [Director, Growth Marketing - Commercial](https://www.skydio.com/jobs/00d0bdc5-89ad-4182-8512-ab0a028953f6) | San Mateo, CA - Full-time | BR=8, HAS_EM, NO_IMPACT_HEADER |
| Marketing | [Field Marketing Event Manager](https://www.skydio.com/jobs/6451be14-d388-4ad1-a4ce-97c36d130c71) | San Mateo, CA - Full-time | USES_H3, CASING:"About the Role" |
| Marketing | [Program Leader, Law Enforcement & Public Safety Training](https://www.skydio.com/jobs/cedc0320-0238-4fc0-89b9-8d580ada556d) | San Mateo, CA - Full-time | NO_IMPACT_HEADER, CASING:"About the Role" |
| Marketing | [Senior Brand Designer (Contract)](https://www.skydio.com/jobs/5ae7e25f-7da3-4523-a8be-8866aa89e8df) | San Mateo, CA - Full-time | BR=2, NO_INTRO_LINKS, NO_IMPACT_HEADER, CASING:"About the Role" |
| People & Recruiting | [Senior Business Recruiter](https://www.skydio.com/jobs/8f1b5980-5318-4728-afd1-36abbb2e8d55) | San Mateo, CA - Full-time | NO_FIT_HEADER |
| People & Recruiting | [Senior People Analytics Analyst](https://www.skydio.com/jobs/0703aaa0-9fcb-4b22-ad8c-b53e74151a72) | San Mateo, CA - Full-time | NO_FIT_HEADER, CASING:"About The Role" |
| People & Recruiting | [Senior Technical Recruiter](https://www.skydio.com/jobs/16b0647d-a470-4917-9bb9-a95967828edc) | San Mateo, CA - Full-time | BR=2, OLD_INTRO_LINKS, NO_ABOUT_ROLE_HEADER |
| People & Recruiting | [Senior Technical Recruiter - Hardware Operations](https://www.skydio.com/jobs/737c02d2-f03f-4716-a0c8-e14a0307f8cb) | San Mateo, CA - Full-time | BR=4, OLD_INTRO_LINKS, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| People & Recruiting | [Staff Technical Recruiter](https://www.skydio.com/jobs/c3a4256a-4525-443c-81d0-6f69e7c24805) | San Mateo, CA - Full-time | OLD_INTRO_LINKS |
| People & Recruiting | [Workplace Experience Coordinator Part-Time](https://www.skydio.com/jobs/d023afe5-f19f-42f7-a1dd-aa94a361b86f) | Zurich, Switzerland - Part-time | BR=1, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER, NO_FIT_HEADER, NO_COMP_BLOCK |
| Policy & Regulatory Affairs | [Aviation Compliance Lead](https://www.skydio.com/jobs/b9f9047b-1555-4978-9bff-70eae58a6b17) | San Mateo, CA - Full-time | USES_H2, BR=1, NO_INTRO_LINKS, CASING:"About the Role" |
| Policy & Regulatory Affairs | [Aviation Regulatory Program Manager](https://www.skydio.com/jobs/d73ae64d-5877-4ab6-ad42-0224702f3fba) | US Remote - Full-time | USES_H2, NO_INTRO_LINKS, CASING:"About the Role" |
| Product | [Director of Product Management, Drone as First Responder (DFR)](https://www.skydio.com/jobs/129a5bad-ca1d-4eda-843b-96f4581f3c43) | San Mateo, CA - Full-time | BR=4, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Product | [Senior Product Manager, Platform & Infrastructure](https://www.skydio.com/jobs/8d67884d-58f4-41a7-8740-ab65d3c03fa8) | San Mateo, CA - Full-time | BR=1, NO_ABOUT_ROLE_HEADER, NO_FIT_HEADER |
| Product | [Senior Staff Product Manager, Drone Hardware Platforms & Sensors](https://www.skydio.com/jobs/9cfecc93-4d5f-4ce4-ae40-cb3ff4783559) | San Mateo, CA - Full-time | BR=2, NO_FIT_HEADER, CASING:"About the Role" |
| Product | [Staff Product Manager, Cameras & Sensors](https://www.skydio.com/jobs/21f27933-a8cb-421f-997f-9d865d372833) | San Mateo, CA - Full-time | NO_ABOUT_ROLE_HEADER |
| Product | [Staff Product Manager, Platform & Infrastructure](https://www.skydio.com/jobs/dbd737b2-beed-4917-9948-dde4250929a8) | San Mateo, CA - Full-time | BR=1, NO_ABOUT_ROLE_HEADER, NO_FIT_HEADER |
| Professional Services and Training | [Customer Success Manager, DFR Majors - Northeast](https://www.skydio.com/jobs/23721f25-7d5f-45fa-a5fe-d58f9680e1ef) | US Remote - Full-time | NO_INTRO_LINKS, NO_IMPACT_HEADER, HAS_ABOUT_TEAM |
| Professional Services and Training | [Deployment Coordinator](https://www.skydio.com/jobs/3d4cd6a4-ce4c-4df6-9002-93019d93784e) | US Remote - Full-time | USES_H2, CASING:"About the Role" |
| Professional Services and Training | [Deployment Engineer - Southeast](https://www.skydio.com/jobs/6138ba1c-c048-407d-9ea2-7b51a3d38756) | US Remote - Full-time | NO_ABOUT_ROLE_HEADER, HAS_ABOUT_TEAM |
| Professional Services and Training | [Mission Success Operations Manager](https://www.skydio.com/jobs/501a3067-e906-4354-b211-ac70db6accf4) | US Remote - Full-time | NO_INTRO_LINKS, HAS_ABOUT_TEAM |
| Professional Services and Training | [Program Manager, Major Deployments (Hawaii)](https://www.skydio.com/jobs/b194dcda-7ff0-4d44-9785-16895a44727f) | San Mateo, CA - Full-time | standard |
| Professional Services and Training | [Program Manager, Major Deployments (Mid Atlantic)](https://www.skydio.com/jobs/c2651b2d-14c5-4bf7-9a35-90b3c939af10) | US Remote - Full-time | NO_INTRO_LINKS |
| Professional Services and Training | [Program Manager, Major Deployments (South East)](https://www.skydio.com/jobs/28bb232f-54c4-486b-9bdb-c7855d04661d) | US Remote - Full-time | NO_INTRO_LINKS |
| Professional Services and Training | [Success Systems Specialist](https://www.skydio.com/jobs/8de95d05-a601-47e2-8a13-5ba4d7ad428a) | US Remote - Full-time | NO_INTRO_LINKS, CASING:"About the Role" |
| Sales | [Enterprise Account Manager (MoD/ MoI) – EMEA (Finland)](https://www.skydio.com/jobs/d6f731e8-c530-4123-8b52-0e7cab164887) | Tampere, Finland - Full-time | BR=2, NO_INTRO_LINKS, CASING:"About the Role" |
| Sales | [Enterprise Account Manager (MoD/ MoI) – EMEA (Germany)](https://www.skydio.com/jobs/12e9a494-9a89-457c-9dc7-2ef9ccdba17c) | Germany - Full-time | BR=2, NO_INTRO_LINKS, CASING:"About the Role" |
| Sales | [Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland)](https://www.skydio.com/jobs/1d4977a2-c2e7-44ad-820b-253ff8355800) | Zurich, Switzerland - Full-time | BR=2, NO_INTRO_LINKS, CASING:"About the Role" |
| Sales | [Enterprise Account Manager, US Army](https://www.skydio.com/jobs/19559b4c-ed09-41eb-b1aa-f000a855b8fe) | US Remote - Full-time | NO_INTRO_LINKS, CASING:"About the Role" |
| Sales | [Enterprise Account Manager, US Navy, US Marine Corps, and IC/SOCOM](https://www.skydio.com/jobs/e69362bc-5891-486e-be75-6bf25187ccf5) | US Remote - Full-time | NO_INTRO_LINKS, CASING:"About the Role" |
| Sales | [GTM Data Engineer Intern](https://www.skydio.com/jobs/b90b9b3b-e326-4fb6-85bd-fe52bec5f180) | San Mateo, CA - Intern | BR=3, NO_INTRO_LINKS, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER, NO_FIT_HEADER |
| Sales | [GTM Enablement Associate](https://www.skydio.com/jobs/2b3fea3b-e1b5-4497-9607-e9864019b0e7) | San Mateo, CA - Full-time | BR=2, NO_INTRO_LINKS, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Sales | [Revenue Operations Engineer, Quoting Systems](https://www.skydio.com/jobs/02d54431-2747-417d-8234-e72c316fed87) | San Mateo, CA - Full-time | USES_H2, BR=4, NO_INTRO_LINKS, NO_IMPACT_HEADER, NO_FIT_HEADER, CASING:"About the Role" |
| Sales | [Sales Planning Analyst Intern](https://www.skydio.com/jobs/712900e5-ff75-4e07-8f88-626d4f8ab653) | San Mateo, CA - Intern | BR=1, NO_INTRO_LINKS, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Sales | [Senior Revenue Operations Manager](https://www.skydio.com/jobs/05e9f029-3a9d-4956-a4c8-e0bc786dd86a) | San Mateo, CA - Full-time | NO_INTRO_LINKS, CASING:"About the Role" |
| Security | [Senior Software Engineer - Security](https://www.skydio.com/jobs/bcd3d614-178c-4349-afd4-76476211b7fe) | San Mateo, CA - Full-time | CASING:"About the Role" |
| Software | [Senior Software Engineer - Embedded](https://www.skydio.com/jobs/67a7d89f-9c4e-4f60-bdf1-a60b8addd8ae) | San Mateo, CA - Full-time | OLD_INTRO_LINKS, HAS_ABOUT_TEAM |
| Software | [Senior Software Engineer - Mobile Platform](https://www.skydio.com/jobs/e8cb16b0-d2f0-4cb4-a1a1-0f43d195cc9a) | San Mateo, CA - Full-time | HAS_ABOUT_TEAM, CASING:"About the Role" |
| Software | [Senior Software Engineer, Data Platform](https://www.skydio.com/jobs/aeaa130d-3e8b-42c5-a805-46f056e62fda) | San Mateo, CA - Full-time | BR=1, NO_IMPACT_HEADER |
| Software | [Senior Software Engineer, Frontend](https://www.skydio.com/jobs/86cfc7bb-001c-4c1c-b680-160265535a96) | San Mateo, CA - Full-time | NO_INTRO_LINKS, CASING:"About the Role" |
| Software | [Senior Software Engineer, Full Stack](https://www.skydio.com/jobs/5655fbe3-66b0-4951-afdc-3b67f71e6938) | San Mateo, CA - Full-time | BR=1, NO_INTRO_LINKS |
| Software | [Senior Software Engineer, Infrastructure](https://www.skydio.com/jobs/0f71bdbb-a645-49f6-8890-dd5c052772c3) | San Mateo, CA - Full-time | NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER, HAS_ABOUT_TEAM |
| Software | [Senior/Staff Embedded Software Engineer – Camera Systems](https://www.skydio.com/jobs/71033170-d9d0-474b-b712-a11e4f11c146) | San Mateo, CA - Full-time | HAS_ABOUT_TEAM, CASING:"About the Role" |
| Software | [Software Engineer - Embedded](https://www.skydio.com/jobs/ef9f7dd2-5a88-49b4-a507-d5fc9cad565a) | San Mateo, CA - Full-time | OLD_INTRO_LINKS, HAS_ABOUT_TEAM |
| Software | [Software Engineer - Infrastructure](https://www.skydio.com/jobs/cb958101-ede8-4f50-bf30-b3272d33f25f) | San Mateo, CA - Full-time | NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER, HAS_ABOUT_TEAM |
| Software | [Software Engineer Intern Fall 2026/Winter 2027](https://www.skydio.com/jobs/f6320e9b-4eed-408d-8d37-d509fb0406ee) | US CA San Mateo - Intern | BR=4, NO_ABOUT_ROLE_HEADER, NO_IMPACT_HEADER |
| Software | [Software Engineer, Full Stack](https://www.skydio.com/jobs/f0020863-db72-480f-916d-375986f86031) | San Mateo, CA - Full-time | NO_INTRO_LINKS |
| Software | [Sr/Staff Embedded Software Engineer - Camera Systems](https://www.skydio.com/jobs/898a9c77-cc20-4ed6-a050-f68e5c15d5c8) | Tampere, Finland - Full-time | HAS_ABOUT_TEAM, CASING:"About the Role" |
| Software | [Staff Software Engineer - Embedded](https://www.skydio.com/jobs/b3b2dea9-63bb-4adb-ba29-69bd8f7a18eb) | San Mateo, CA - Full-time | OLD_INTRO_LINKS, HAS_ABOUT_TEAM |
| Software | [Staff Software Engineer, Frontend](https://www.skydio.com/jobs/54654035-a78a-4e5b-9ebf-ae4067e5a246) | San Mateo, CA - Full-time | NO_INTRO_LINKS |
| Software | [Staff Software Engineer, Full Stack](https://www.skydio.com/jobs/379b23ea-14ff-4602-9b79-52d00bb96fda) | San Mateo, CA - Full-time | NO_INTRO_LINKS, NO_ABOUT_ROLE_HEADER |
| Supply Chain & Logistics | [Hardware Operations Program Manager](https://www.skydio.com/jobs/55b393cf-124c-46f8-bd83-8c62e3ce628b) | Hayward, CA - Full-time | NO_INTRO_LINKS, NO_FIT_HEADER |
| Supply Chain & Logistics | [Senior Supplier Quality Engineer](https://www.skydio.com/jobs/b0fb285d-0619-42ee-ad24-d549479deb84) | San Mateo, CA - Full-time | BR=2, NO_IMPACT_HEADER |
| Supply Chain & Logistics | [Staff Global Supply Manager, Mechanicals](https://www.skydio.com/jobs/2ffe6453-4a2f-4dfb-94f8-882f731a11ae) | San Mateo, CA - Full-time | BR=1, NO_INTRO_LINKS, NO_IMPACT_HEADER |
| Supply Chain & Logistics | [Supplier Quality Engineer, Sustaining](https://www.skydio.com/jobs/4c4874bf-02da-4ccc-8918-2cca08feaf21) | Taiwan - Full-time | NO_COMP_BLOCK |
| Supply Chain & Logistics | [Supply Chain Intern](https://www.skydio.com/jobs/2d21f482-3224-4906-a1bb-6a64436774cb) | San Mateo, CA - Intern | BR=3, NO_INTRO_LINKS, NO_IMPACT_HEADER, NO_COMP_BLOCK |

---

*Audit generated automatically from the live careers page on 2026-05-10. All 112 postings listed on https://www.skydio.com/careers were fetched, and the markup of each posting's description block was diffed against the dominant template. This report intentionally focuses only on pre-compensation content; the Compensation block, EEO statement, E-Verify notice, and Ashby application form below it were excluded from the analysis as instructed.*