# Skydio Careers — Job Posting Formatting Consistency Audit

**Source:** https://www.skydio.com/careers (and 106 individual `/jobs/<uuid>/` pages)
**Date crawled:** 2026-05-22  
**Scope:** All content rendered above (and not including) the *Compensation* block of each job posting — i.e. the job-title header, location/employment-type line, the boilerplate company intro paragraph, and all role-specific sections (About the role, How you’ll make an impact, What makes you a good fit, etc.).
**Jobs analyzed:** 106

---

## 1. TL;DR (for the team)

Visually the postings all use the same global CSS shell (the job title is rendered with the `type-h2` class, the location line with `type-body-2`, and the body sits inside a `prose block-content` container) so **the *theme* is uniform**. The inconsistencies are happening inside the rich-text body that recruiters paste from Greenhouse / Word / Notion. They fall into 5 buckets:

| # | Inconsistency | Postings affected | Visual symptom |
|---|---|---|---|
| 1 | Section headings authored as **`<h1>`, `<h2>`, or `<h3>`** instead of the standard **bold paragraph** (`<p><strong>…</strong></p>`) | 16 of 106 | Section titles are **noticeably larger / heavier** (browser-default heading sizes) than the rest of the postings |
| 2 | Three different versions of the **standard intro paragraph** ("Skydio is the leading US drone company…") | 35 + 18 vs canonical 53 | Subtle punctuation/sentence-structure drift only, but it propagates a *second* visual difference (see row 3) |
| 3 | The 18-posting intro variant ships boilerplate links with the CSS class **`c-link c-link--underline`** instead of the default unstyled anchors | 12 | The four "utility inspectors / first responders / soldiers / beyond" links appear **underlined**, while the rest of the posts render them as plain colored links |
| 4 | Section-heading **wording & capitalization drift** (e.g. *About the role:* vs *About the Role:*, *How you’ll make an impact:* (curly ’) vs *How you'll make an impact:* (straight ')) | every posting | The strings look identical at a glance but cause grep/SEO/screen-reader inconsistencies — and one outright typo: **"What Makes Your a Good Fit:"** |
| 5 | Editor-artifact junk: trailing `<br/>` after bullet text (extra blank line), empty `<p></p>` placeholders, stray `<div style="min-height:1.2em…">`, **non-breaking spaces (`&nbsp;`)**, **`<u>` underline tags**, and italic/bold-mixed section labels | 50+, 28, 1, 7, 1 | Random extra vertical gaps; underlined snippets that look like links; one section title rendered as *italic + bold* |

Bottom line: **at least 96 of the 106 postings (≈91 %) have at least one formatting deviation from the most-common pattern, and 10 are clean.** The two structural outliers most likely to be noticed by candidates are:
* `Senior Technical Support Representative – Japan` — uses **`<h1>` tags for in-body section headings**, which renders each section title as a *page-title-sized* line.
* `Hardware Engineering Program Manager` — only posting that **also uses `<h2>` + `<h3>` together** to introduce sub-sections inside *How you’ll make an impact*; sub-section names get visibly larger headings than peers do.

---

## 2. The "canonical" Skydio job posting

The most common shape (followed by ~85 % of postings to varying degrees) is:

1. Job title (rendered with `type-h2`)
2. Location – employment-type line (`type-body-2`)
3. **Boilerplate intro paragraph** — one `<p>` containing 4 inline links to skydio.com solutions pages
4. `<p><strong>About the role:</strong></p>` followed by 1-3 narrative paragraphs
5. `<p><strong>How you’ll make an impact:</strong></p>` followed by a `<ul>` bullet list
6. `<p><strong>What makes you a good fit:</strong></p>` followed by a `<ul>` bullet list
7. (optional) `<p><strong>Bonus points:</strong></p>` + bullet list
8. `<p><strong>Compensation:</strong></p>` — *not in scope for this report*

All section titles are authored as **bold paragraphs, not heading tags**, end with a **trailing colon**, and use **sentence case** ("About the role:" — only first word capitalized).

---

## 3. Detailed findings

### 3.1 Font size / weight — section-heading style inconsistency *(highest impact)*

Because the body sits inside the generic `.prose` container, browser/Skydio default styles render `<h2>`, `<h3>` and `<p><strong>` very differently:

| Authoring pattern | Roughly rendered font size | Postings using it |
|---|---|---|
| `<h1>…</h1>` (invalid inside a page body) | ~32 px | **1** |
| `<h2>…</h2>` | ~24 px | **9** |
| `<h3>…</h3>` | ~18 px | **5** |
| `<h2>` + `<h3>` mixed | mix | **1** |
| `<p><strong>…</strong></p>` (canonical) | ~16 px (= body) | **88** |
| No section headings detected at all | n/a | **2** |

Concrete outliers:

* **Hardware Engineering Program Manager** *(San Mateo, California, United States - Full-time)* — `mixed-h2-h3` — heading tags found: `['h2', 'h2', 'h3', 'h3', 'h3', 'h2', 'h3', 'h3']`
* **Product Support Engineer** *(San Mateo, California, United States - Full-time)* — `none-detected` — heading tags found: `[]`
* **Product Support Engineer Intern** *(San Mateo, California, United States - Intern)* — `none-detected` — heading tags found: `[]`
* **Senior Technical Support Representative - Japan** *(Tokyo, Japan - Full-time)* — `uses-h1-h2` — heading tags found: `['h1', 'h1', 'h1']`
* **Aviation Compliance Lead** *(San Mateo, California, United States - Full-time)* — `uses-h2` — heading tags found: `['h2', 'h2', 'h2']`
* **Aviation Regulatory Program Manager** *(US Remote - Full-time)* — `uses-h2` — heading tags found: `['h2', 'h2', 'h2']`
* **Communications Manager** *(US Remote - Full-time)* — `uses-h2` — heading tags found: `['h2', 'h2', 'h2']`
* **Revenue Operations Engineer, Quoting Systems** *(San Mateo, California, United States - Full-time)* — `uses-h2` — heading tags found: `['h2', 'h2', 'h2', 'h2', 'h2']`
* **Senior Buyer** *(Hayward, California, United States - Full-time)* — `uses-h2` — heading tags found: `['h2', 'h2']`
* **Software Engineer - Autonomy Infrastructure, Systems and Tools** *(San Mateo, California, United States - Full-time)* — `uses-h2` — heading tags found: `['h2', 'h2', 'h2', 'h2', 'h2']`
* **Software Engineer - Autonomy Infrastructure, Systems and Tools** *(Zurich, Switzerland - Full-time)* — `uses-h2` — heading tags found: `['h2', 'h2', 'h2', 'h2', 'h2']`
* **Software Engineer - Cloud Simulation &amp; Full-Stack** *(San Mateo, California, United States - Full-time)* — `uses-h2` — heading tags found: `['h2', 'h2', 'h2', 'h2', 'h2']`
* **Software Engineer - Cloud Simulation &amp; Full-Stack** *(Zurich, Switzerland - Full-time)* — `uses-h2` — heading tags found: `['h2', 'h2', 'h2', 'h2', 'h2']`
* **Full Stack Product Counsel** *(San Mateo, California, United States - Full-time)* — `uses-h3` — heading tags found: `['h3', 'h3', 'h3', 'h3']`
* **PhD Autonomy Engineer Intern - Planning &amp; Controls (Reinforcement Learning)** *(Zurich, Switzerland - Intern)* — `uses-h3` — heading tags found: `['h3', 'h3', 'h3']`
* **Senior Business Operations Manager** *(San Mateo, California, United States - Full-time)* — `uses-h3` — heading tags found: `['h3', 'h3', 'h3']`
* **Software Engineer - Simulation &amp; Robotics Engineer** *(San Mateo, California, United States - Full-time)* — `uses-h3` — heading tags found: `['h3', 'h3', 'h3', 'h3', 'h3']`
* **Software Engineer - Simulation &amp; Robotics Engineer** *(Zurich, Switzerland - Full-time)* — `uses-h3` — heading tags found: `['h3', 'h3', 'h3', 'h3', 'h3']`

> **Recommendation:** standardize on `<p><strong>Section title:</strong></p>` for top-level sections. If sub-sections are needed (only one posting currently uses them), introduce a *single* convention — e.g. `<p><em>Sub-section</em></p>` — rather than mixing heading levels into a body that has no h1.

### 3.2 Boilerplate intro paragraph — three competing versions

Every posting starts with the same Skydio company-blurb paragraph, but the exact wording diverges in three ways:

| Variant | Count | Differing phrase |
|---|---|---|
| **v1 (canonical)** | 53 | "…drone users, **from** utility inspectors to first responders, soldiers in battlefield scenarios**,** and beyond." |
| **v2** | 35 | Same wording but **missing the Oxford-style comma** before "and beyond" → "…scenarios and beyond." |
| **v3** | 18 | Sentence is split: "…drone users**.** **From** utility inspectors to first responders, soldiers in battlefield scenarios and beyond." |

Crucially the **v3 variant also carries different link markup**: `<a class="c-link c-link--underline" rel="noopener" …>`. The other variants emit `<a rel="noopener noreferrer nofollow" …>` (no class). So **the four solutions links in those 12 postings are visually underlined** while the same links in the other 94 postings are not.

The 12 postings using **v3 intro + underlined-link class** (the visibly different cohort):

* Autonomy Engineer - Deep Learning *(San Mateo)*
* Autonomy Engineer - Deep Learning Infrastructure *(San Mateo)*
* Autonomy Engineer - Deep Learning Model Acceleration *(San Mateo)*
* Autonomy Software Engineer *(San Mateo)*
* Engineering Manager - Autonomy *(San Mateo)*
* PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) *(Zurich)*
* Senior Software Engineer - Embedded *(San Mateo)*
* Senior Technical Recruiter *(San Mateo)*
* Senior Technical Recruiter - Hardware Operations *(San Mateo)*
* Software Engineer - Embedded *(San Mateo)*
* Staff Software Engineer - Embedded *(San Mateo)*
* Staff Technical Recruiter *(San Mateo)*

The remaining 6 postings use the v3 wording but with default (non-underlined) link markup — so they only drift on the *text* of the intro, not the styling:

* Autonomy Engineer - Deep Learning *(Zurich)*
* Autonomy Engineer - Deep Learning Infrastructure *(Zurich)*
* Autonomy Engineer - Deep Learning Model Acceleration *(Zurich)*
* Senior Autonomy Engineer - Deep Learning *(San Mateo)*
* Senior Autonomy Engineer - Deep Learning *(Zurich)*
* Senior Brand Designer (Contract) *(San Mateo)*

> **Recommendation:** lock the boilerplate intro to one canonical paragraph and one anchor-tag pattern. Add it as a Greenhouse template snippet so recruiters cannot paste alternate versions.

### 3.3 Section-heading wording & capitalization drift

Even within postings that all use bold-paragraph section titles, the **same heading is written ≥4 different ways**:

**"About the role" (66 instances):**
* `About the role:` — 45 ✅ majority
* `About the Role:` — 21 (Title-Case variant)
* `About the Role` — 1 (no colon)
* `About The Role` — 1 (Title-Case + no colon)

**"How you’ll make an impact" (69 instances):**
* `How you'll make an impact:` (straight apostrophe) — 32 ✅ majority
* `How You’ll Make an Impact:` (curly apostrophe, Title-Case) — 19
* `How you’ll make an impact:` (curly apostrophe, sentence case) — 13
* `How you will make an impact:` — 3
* `How You'll Make an Impact:` — 1
* `How you'll make an impact` — 1 (no colon)

**"What makes you a good fit" (86 instances):**
* `What makes you a good fit:` — 51 ✅ majority
* `What Makes You a Good Fit:` — 17
* `What would make you a good fit:` — 6
* `What Would Make You a Good Fit:` — 2
* `What makes you a strong fit:` — 2
* `What would make you a strong fit:` — 2
* `What Makes You A Good Fit:` — 2 (note: "A" capitalized)
* `What makes you a good fit` — 2 (no colon)
* `What Makes You a Good Fit` — 1 (no colon)
* `What Makes Your a Good Fit:` — 1  **← typo: "Your" should be "You"**

Section-title typo lives in **`Senior People Analytics Analyst`** (San Mateo).

> **Recommendation:** pick a house style — recommended: sentence case, straight apostrophe, trailing colon — and reject any other variant in copy-edit.

### 3.4 Postings with mixed colon / no-colon section labels (internal inconsistency)

These postings mix headings that end with a colon and headings that do not, in the *same* job — which renders as a noticeable rhythm break:

* **Director, Growth Marketing - Commercial** *(San Mateo, California, United States - Full-time)* — section headers mix trailing colons and no-colon: ['Ability to be in our San Mateo, CA office 3 days per week', 'Additional Desired Experience and Skills']
* **Success Systems Specialist** *(US Remote - Full-time)* — section headers mix trailing colons and no-colon: ['Build Automation & Intelligence into Mission Success', 'Customer Digital Experience', 'Cross-Functional Architecture & Governance', 'Scalability & Cost Avoidance']
* **Workplace Experience Coordinator Part-Time** *(Zurich, Switzerland - Part-time)* — section headers mix trailing colons and no-colon: ['Workplace Experience & Office Operations', 'People Operations & HR Coordination', 'Qualifications', 'Work Environment']
* **Enterprise Account Manager (MoD/ MoI) – EMEA (Finland)** *(Tampere, Finland - Full-time)* — section headers mix trailing colons and no-colon: ['This role must be based in Switzerland, Germany, or Finland.']
* **Enterprise Account Manager (MoD/ MoI) – EMEA (Germany)** *(Germany - Full-time)* — section headers mix trailing colons and no-colon: ['This role must be based in Switzerland, Germany, or Finland.']
* **Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland)** *(Zurich, Switzerland - Full-time)* — section headers mix trailing colons and no-colon: ['This role must be based in Switzerland, Germany, or Finland.']
* **Mission Success Operations Manager** *(US Remote - Full-time)* — section headers mix trailing colons and no-colon: ['What makes you a good fit']
* **Senior People Analytics Analyst** *(San Mateo, California, United States - Full-time)* — section headers mix trailing colons and no-colon: ['About The Role']
* **Senior Software Engineer,  Data Platform** *(San Mateo, California, United States - Full-time)* — section headers mix trailing colons and no-colon: ['Why Join Us?']

### 3.5 Stray `<u>` (underline) tags in body text

HTML `<u>` is being used by 7 postings for emphasis. Visually this underlines text the same way an anchor does, which can confuse readers ("is that a link?"). Concrete uses:

| Posting | What is underlined |
|---|---|
| Senior Technical Recruiter | `PLEASE NOTE:` |
| Senior Technical Recruiter – Hardware Operations | `PLEASE NOTE:` |
| Staff Technical Recruiter | `PLEASE NOTE:` |
| Senior NPI Product Quality Engineer | `Please Note:` (also wrapped in italics) |
| Lead Staff Electrical Engineer (F10 Program) | `Skydio F10 Program` (product-name emphasis) |
| Senior Software Engineer, Full Stack | `public API` |
| Full Stack Product Counsel | `Full Stack Product Counsel` (the *job title* repeated and underlined in the intro) |

> **Recommendation:** retire `<u>` altogether in postings. Use bold (`<strong>`) for emphasis; reserve underline for actual links.

### 3.6 List-item line-spacing artifacts

5 postings include trailing `<br/>` tags at the end of bullet items, which inserts an empty line between bullets and makes the list look loosely double-spaced compared to other postings:

| Posting | # bullets with stray `<br/>` |
|---|---|
| Director, Growth Marketing - Commercial | 7 |
| Revenue Operations Engineer, Quoting Systems | 3 |
| GTM Data Engineer Intern | 2 |
| Aviation Compliance Lead | 1 |
| Engineering Manager - Autonomy | 1 |

### 3.7 Empty `<p>` elements and `&nbsp;` whitespace artifacts

* **50 postings (≈47 %)** contain at least one literally empty `<p></p>` element from copy-paste, which renders as an extra paragraph of vertical whitespace.
* **28 postings** contain `&nbsp;` (non-breaking space) characters in body copy. These slip in from Word/Google Docs and break responsive line-wrap rules.
* **`Manager, Logistics`** contains a stray `<div style="min-height:1.2em;margin-top:0;margin-bottom:0">` — an editor placeholder that renders as an extra blank line at the end of the qualifications list.

> **Recommendation:** add a "strip empty `<p>`/`<div>`/`&nbsp;`" pre-publish lint step on whatever ATS/CMS Skydio uses to pipe postings into the careers site.

### 3.8 Italic / bold mixed section heading (single posting)

* **`Director, Growth Marketing – Commercial`** is the only posting where a section label is wrapped in both `<em>` and `<strong>`. The phrase **"*Ability to be in our San Mateo, CA office 3 days per week*"** renders bold + italic, while every other San Mateo "in-office requirement" line in the corpus renders as plain or bold-only text. The same posting also has 7 of the 14 corpus-wide trailing-`<br/>` artifacts and adds two non-standard section labels: *"What Success Looks Like:"* and *"Additional Desired Experience and Skills"* (the latter is the only top-level section in the entire corpus that omits the trailing colon).

### 3.9 Postings that do not have a Compensation block at all

5 postings have no Compensation block — all international roles where Skydio is not legally required to list a salary range. **The body simply ends at the EEO statement.** That is fine on its own, but these postings still drift in formatting from the US-norm:

| Posting | Location | Notable extra issue |
|---|---|---|
| Supplier Quality Engineer, Sustaining | Taiwan | uses sentence-case `About the role:` (consistent with the norm) but only 3 `<strong>` blocks — minimal structure |
| Autonomy Engineer Intern – Deep Learning (Computational Photography) | San Mateo, CA | run-on intro paragraph (no `<br>` between "Skydio is…" and "About the role:") |
| Autonomy Engineer Intern – Deep Learning (Computational Photography) | Zurich / Tampere | same run-on intro as above |
| Workplace Experience Coordinator Part-Time | Zurich | drops colon on **every** section header (`About the Role`, `Workplace Experience & Office Operations`, `People Operations & HR Coordination`, `Qualifications`, `Work Environment`) — a fully different style |
| Senior Technical Support Representative – Japan | Tokyo | **uses `<h1>` for in-body section headings** — biggest single visual outlier in the entire careers site |

---

## 4. Outlier postings — ranked by total formatting flags

| # of flags | Posting | Location | Issues |
|---|---|---|---|
| 5 | Director, Growth Marketing - Commercial | San Mateo, California, United States - Full-time | trailing <br/> at end of 7 list item(s); section headers mix trailing colons and no-colon: ['Ability to be in our San Mateo, CA office 3 days per week', 'Additional Desired Experience and Skills']; contains empty <p></p> element(s); uses italics in body (1x): ['Ability to be in our San Mateo, CA office 3 days per week']; section heading wrapped in both <em> AND <strong> (italic + bold) |
| 4 | Autonomy Engineer - Deep Learning Infrastructure | San Mateo, California, United States - Full-time | uses "v3" intro variant ("drone users. From utility..."); uses CSS class "c-link c-link--underline" on boilerplate links (visually underlines them); contains empty <p></p> element(s); contains &nbsp; / non-breaking spaces (2) |
| 4 | Aviation Compliance Lead | San Mateo, California, United States - Full-time | uses <h2> tags for sections (vs bold-paragraph norm); trailing <br/> at end of 1 list item(s); uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 4 | PhD Autonomy Engineer Intern - Planning &amp; Controls (Reinforcement Learning) | Zurich, Switzerland - Intern | uses <h3> with no <h2> (section level skipped); uses "v3" intro variant ("drone users. From utility..."); uses CSS class "c-link c-link--underline" on boilerplate links (visually underlines them); contains &nbsp; / non-breaking spaces (1) |
| 4 | Senior Technical Recruiter | San Mateo, California, United States - Full-time | contains <u> underline tag (1x); uses "v3" intro variant ("drone users. From utility..."); uses CSS class "c-link c-link--underline" on boilerplate links (visually underlines them); contains &nbsp; / non-breaking spaces (1) |
| 4 | Senior Technical Recruiter - Hardware Operations | San Mateo, California, United States - Full-time | contains <u> underline tag (1x); uses "v3" intro variant ("drone users. From utility..."); uses CSS class "c-link c-link--underline" on boilerplate links (visually underlines them); contains &nbsp; / non-breaking spaces (1) |
| 4 | Staff Technical Recruiter | San Mateo, California, United States - Full-time | contains <u> underline tag (1x); uses "v3" intro variant ("drone users. From utility..."); uses CSS class "c-link c-link--underline" on boilerplate links (visually underlines them); contains &nbsp; / non-breaking spaces (1) |
| 3 | Autonomy Engineer - Deep Learning | Zurich, Switzerland - Full-time | uses "v3" intro variant ("drone users. From utility..."); uses CSS class "c-link c-link--underline" on boilerplate links (visually underlines them); contains &nbsp; / non-breaking spaces (1) |
| 3 | Aviation Regulatory Program Manager | US Remote - Full-time | uses <h2> tags for sections (vs bold-paragraph norm); uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 3 | Engineering Manager - Autonomy | San Mateo, California, United States - Full-time | trailing <br/> at end of 1 list item(s); uses "v3" intro variant ("drone users. From utility..."); uses CSS class "c-link c-link--underline" on boilerplate links (visually underlines them) |
| 3 | Full Stack Product Counsel | San Mateo, California, United States - Full-time | uses <h3> with no <h2> (section level skipped); contains <u> underline tag (1x); contains empty <p></p> element(s) |
| 3 | GTM Data Engineer Intern | San Mateo, California, United States - Intern | trailing <br/> at end of 2 list item(s); uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 3 | GTM Enablement Associate | San Mateo, California, United States - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s); contains &nbsp; / non-breaking spaces (1) |
| 3 | Hardware Engineering Program Manager | San Mateo, California, United States - Full-time | uses <h2> tags for sections (vs bold-paragraph norm); uses both <h2> and <h3> (mixed with bold-paragraph norm); contains empty <p></p> element(s) |
| 3 | Lead Staff Electrical Engineer (F10 Program) | San Mateo, California, United States - Full-time | contains <u> underline tag (1x); contains empty <p></p> element(s); contains &nbsp; / non-breaking spaces (2) |
| 3 | Manager, Logistics | US CA Production - Full-time | contains stray <div style="..."> spacer; contains empty <p></p> element(s); contains &nbsp; / non-breaking spaces (1) |
| 3 | Revenue Operations Engineer, Quoting Systems | San Mateo, California, United States - Full-time | trailing <br/> at end of 3 list item(s); uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 3 | Senior Autonomy Engineer - Deep Learning | San Mateo, California, United States - Full-time | uses "v3" intro variant ("drone users. From utility..."); contains empty <p></p> element(s); contains &nbsp; / non-breaking spaces (1) |
| 3 | Senior NPI Product Quality Engineer | San Mateo, California, United States - Full-time | contains <u> underline tag (1x); uses "v2" intro variant (missing Oxford-style comma after "scenarios"); uses italics in body (1x): ['Please Note:'] |
| 3 | Senior Software Engineer - Embedded | San Mateo, California, United States - Full-time | uses "v3" intro variant ("drone users. From utility..."); uses CSS class "c-link c-link--underline" on boilerplate links (visually underlines them); contains &nbsp; / non-breaking spaces (3) |
| 3 | Senior Technical Support Representative - Japan | Tokyo, Japan - Full-time | uses <h1> inside body (invalid heading hierarchy); contains empty <p></p> element(s); no "Compensation" block at all (pre-compensation analysis covers whole body) |
| 3 | Software Engineer - Autonomy Infrastructure, Systems and Tools | San Mateo, California, United States - Full-time | uses <h2> tags for sections (vs bold-paragraph norm); uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 3 | Software Engineer - Autonomy Infrastructure, Systems and Tools | Zurich, Switzerland - Full-time | uses <h2> tags for sections (vs bold-paragraph norm); uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 3 | Software Engineer - Cloud Simulation &amp; Full-Stack | San Mateo, California, United States - Full-time | uses <h2> tags for sections (vs bold-paragraph norm); uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 3 | Software Engineer - Cloud Simulation &amp; Full-Stack | Zurich, Switzerland - Full-time | uses <h2> tags for sections (vs bold-paragraph norm); uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 3 | Software Engineer - Embedded | San Mateo, California, United States - Full-time | uses "v3" intro variant ("drone users. From utility..."); uses CSS class "c-link c-link--underline" on boilerplate links (visually underlines them); contains &nbsp; / non-breaking spaces (3) |
| 3 | Software Engineer - Simulation &amp; Robotics Engineer | San Mateo, California, United States - Full-time | uses <h3> with no <h2> (section level skipped); uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 3 | Software Engineer - Simulation &amp; Robotics Engineer | Zurich, Switzerland - Full-time | uses <h3> with no <h2> (section level skipped); uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 3 | Staff Software Engineer - Embedded | San Mateo, California, United States - Full-time | uses "v3" intro variant ("drone users. From utility..."); uses CSS class "c-link c-link--underline" on boilerplate links (visually underlines them); contains &nbsp; / non-breaking spaces (3) |
| 3 | Success Systems Specialist | US Remote - Full-time | section headers mix trailing colons and no-colon: ['Build Automation & Intelligence into Mission Success', 'Customer Digital Experience', 'Cross-Functional Architecture & Governance', 'Scalability & Cost Avoidance']; uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 3 | Workplace Experience Coordinator Part-Time | Zurich, Switzerland - Part-time | section headers mix trailing colons and no-colon: ['Workplace Experience & Office Operations', 'People Operations & HR Coordination', 'Qualifications', 'Work Environment']; contains empty <p></p> element(s); no "Compensation" block at all (pre-compensation analysis covers whole body) |
| 2 | Autonomy Engineer - Deep Learning | San Mateo, California, United States - Full-time | uses "v3" intro variant ("drone users. From utility..."); contains &nbsp; / non-breaking spaces (1) |
| 2 | Autonomy Engineer - Deep Learning Model Acceleration | San Mateo, California, United States - Full-time | uses "v3" intro variant ("drone users. From utility..."); uses CSS class "c-link c-link--underline" on boilerplate links (visually underlines them) |
| 2 | Autonomy Software Engineer | San Mateo, California, United States - Full-time | uses "v3" intro variant ("drone users. From utility..."); uses CSS class "c-link c-link--underline" on boilerplate links (visually underlines them) |
| 2 | Communications Manager | US Remote - Full-time | uses <h2> tags for sections (vs bold-paragraph norm); contains empty <p></p> element(s) |
| 2 | Customer Success Manager, DFR Majors - Northeast | US Remote - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains &nbsp; / non-breaking spaces (6) |
| 2 | Enterprise Account Manager (MoD/ MoI) – EMEA (Finland) | Tampere, Finland - Full-time | section headers mix trailing colons and no-colon: ['This role must be based in Switzerland, Germany, or Finland.']; uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 2 | Enterprise Account Manager (MoD/ MoI) – EMEA (Germany) | Germany - Full-time | section headers mix trailing colons and no-colon: ['This role must be based in Switzerland, Germany, or Finland.']; uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 2 | Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland) | Zurich, Switzerland - Full-time | section headers mix trailing colons and no-colon: ['This role must be based in Switzerland, Germany, or Finland.']; uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 2 | Field Support Representative (Southwest, Remote) | US Remote - Full-time | contains empty <p></p> element(s); contains &nbsp; / non-breaking spaces (13) |
| 2 | Hardware Operations Program Manager | Hayward, California, United States - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 2 | Mission Success Operations Manager | US Remote - Full-time | section headers mix trailing colons and no-colon: ['What makes you a good fit']; uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 2 | PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | San Mateo, California, United States - Intern | uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains &nbsp; / non-breaking spaces (1) |
| 2 | Program Manager, Major Deployments (Mid Atlantic) | US Remote - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 2 | Sales Planning Analyst Intern | San Mateo, California, United States - Intern | uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 2 | Senior Autonomy Engineer - Deep Learning | Zurich, Switzerland - Full-time | uses "v3" intro variant ("drone users. From utility..."); contains &nbsp; / non-breaking spaces (1) |
| 2 | Senior Brand Designer (Contract) | San Mateo, California, United States - Full-time | uses "v3" intro variant ("drone users. From utility..."); contains empty <p></p> element(s) |
| 2 | Senior Business Operations Manager | San Mateo, California, United States - Full-time | uses <h3> with no <h2> (section level skipped); contains empty <p></p> element(s) |
| 2 | Senior Revenue Operations Manager | San Mateo, California, United States - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 2 | Senior Software Engineer, Full Stack | San Mateo, California, United States - Full-time | contains <u> underline tag (1x); uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 2 | Staff Global Supply Manager,  Mechanicals | San Mateo, California, United States - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains empty <p></p> element(s) |
| 2 | Supplier Quality Engineer, Sustaining | Taiwan - Full-time | contains empty <p></p> element(s); no "Compensation" block at all (pre-compensation analysis covers whole body) |
| 2 | Technical Support Specialist - West Coast | US Remote - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios"); contains &nbsp; / non-breaking spaces (5) |
| 1 | Autonomy Engineer - Deep Learning Infrastructure | Zurich, Switzerland - Full-time | uses "v3" intro variant ("drone users. From utility...") |
| 1 | Autonomy Engineer - Deep Learning Model Acceleration | Zurich, Switzerland - Full-time | uses "v3" intro variant ("drone users. From utility...") |
| 1 | Autonomy Engineer - Fixed Wing Planning &amp; Controls | San Mateo, California, United States - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 1 | Autonomy Engineer - ML &amp; DL Infrastructure | San Mateo, California, United States - Full-time | contains empty <p></p> element(s) |
| 1 | Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | San Mateo, California, United States - Intern | contains &nbsp; / non-breaking spaces (1) |
| 1 | Autonomy Engineer Intern - Deep Learning (Computational Photography) | Zurich, Switzerland or Tampere, Finland - Intern | no "Compensation" block at all (pre-compensation analysis covers whole body) |
| 1 | Autonomy Engineer Intern - Deep Learning (Computational Photography) | San Mateo, California, United States - Intern | no "Compensation" block at all (pre-compensation analysis covers whole body) |
| 1 | Autonomy Engineer Intern Fall 2026 | San Mateo, California, United States - Intern | contains &nbsp; / non-breaking spaces (1) |
| 1 | Deployment Engineer - Southeast | US Remote - Full-time | contains empty <p></p> element(s) |
| 1 | Director of Product Management, Drone as First Responder (DFR) | San Mateo, California, United States - Full-time | contains &nbsp; / non-breaking spaces (5) |
| 1 | Director, Global Supply Management - Mechanicals | San Mateo, California, United States - Full-time | contains empty <p></p> element(s) |
| 1 | Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM | US Remote - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 1 | Hardware Technician | San Mateo, California, United States - Full-time | contains empty <p></p> element(s) |
| 1 | Head of Warehouse &amp; Logistics Operations | US CA Production - Full-time | contains empty <p></p> element(s) |
| 1 | IT Technician (Help Desk - Linux Focus) | Hayward, California, United States - Full-time | contains empty <p></p> element(s) |
| 1 | Middleware Software Engineer Intern - Fall 2026 | US CA San Mateo - Intern | contains &nbsp; / non-breaking spaces (2) |
| 1 | PCB Layout Engineer | San Mateo, California, United States - Full-time | contains &nbsp; / non-breaking spaces (2) |
| 1 | Product Design Engineer (All Levels) | San Mateo, California, United States - Full-time | contains &nbsp; / non-breaking spaces (1) |
| 1 | Product Support Engineer | San Mateo, California, United States - Full-time | contains empty <p></p> element(s) |
| 1 | Product Support Engineer Intern | San Mateo, California, United States - Intern | contains empty <p></p> element(s) |
| 1 | Production Manager, PM Shift | Hayward, California, United States - Full-time | contains empty <p></p> element(s) |
| 1 | Program Manager, Major Deployments (Hawaii) | San Mateo, California, United States - Full-time | contains empty <p></p> element(s) |
| 1 | Senior Autonomy Engineer - Controls | San Mateo, California, United States - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 1 | Senior Buyer | Hayward, California, United States - Full-time | contains empty <p></p> element(s) |
| 1 | Senior Customer Support Representative - India | Bangalore, India - Full-time | contains empty <p></p> element(s) |
| 1 | Senior Director, Product Management, Drone as First Responder (DFR) | San Mateo, California, United States - Full-time | contains &nbsp; / non-breaking spaces (5) |
| 1 | Senior Hardware Test and Reliability Engineer | San Mateo, California, United States - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 1 | Senior People Analytics Analyst | San Mateo, California, United States - Full-time | section headers mix trailing colons and no-colon: ['About The Role'] |
| 1 | Senior Product Manager, Platform &amp; Infrastructure | San Mateo, California, United States - Full-time | contains empty <p></p> element(s) |
| 1 | Senior RF Design Engineer | San Mateo, California, United States - Full-time | contains empty <p></p> element(s) |
| 1 | Senior Software Engineer - Mobile Platform | San Mateo, California, United States - Full-time | contains empty <p></p> element(s) |
| 1 | Senior Software Engineer,  Data Platform | San Mateo, California, United States - Full-time | section headers mix trailing colons and no-colon: ['Why Join Us?'] |
| 1 | Senior Software Engineer, Frontend | San Mateo, California, United States - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 1 | Senior Wireless Systems Performance Engineer | San Mateo, California, United States - Full-time | contains &nbsp; / non-breaking spaces (4) |
| 1 | Senior/Staff Embedded Software Engineer – Camera Systems | San Mateo, California, United States - Full-time | contains empty <p></p> element(s) |
| 1 | Software Engineer Intern Fall 2026/Winter 2027 | US CA San Mateo - Intern | contains empty <p></p> element(s) |
| 1 | Sr/Staff Embedded Software Engineer - Camera Systems | Tampere, Finland - Full-time | contains empty <p></p> element(s) |
| 1 | Staff Product Manager, Platform &amp; Infrastructure | San Mateo, California, United States - Full-time | contains empty <p></p> element(s) |
| 1 | Staff Software Engineer, Frontend | San Mateo, California, United States - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 1 | Staff Software Engineer, Full Stack | San Mateo, California, United States - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 1 | Supply Chain Intern | San Mateo, California, United States - Intern | uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 1 | Systems Integration and Test Engineer (Mid to Senior Level) | San Mateo, California, United States - Full-time | uses "v2" intro variant (missing Oxford-style comma after "scenarios") |
| 1 | Wireless Software Engineer | San Mateo, California, United States - Full-time | contains &nbsp; / non-breaking spaces (1) |

### Clean postings (no flags raised)

10 postings raise no flags and can serve as the *reference templates* for the team:

* Electrical Engineer (Sustaining/Validation) *(San Mateo, California, United States - Full-time)*
* Electrical Engineer (all levels) *(San Mateo, California, United States - Full-time)*
* Enterprise Account Manager, US Army *(US Remote - Full-time)*
* Field Support Representative *(US Remote - Full-time)*
* Manager, Technical Support *(US CA San Mateo - Full-time)*
* RF Design Engineer *(San Mateo, California, United States - Full-time)*
* Senior Software Engineer - Security *(San Mateo, California, United States - Full-time)*
* Senior Software Engineer,  Infrastructure *(San Mateo, California, United States - Full-time)*
* Software Engineer - Infrastructure *(San Mateo, California, United States - Full-time)*
* Software Engineer, Full Stack *(San Mateo, California, United States - Full-time)*

---

## 5. Recommendations (concrete, actionable)

### 5.1 Lock the boilerplate
* Save the canonical "Skydio is the leading US drone company…" paragraph as a Greenhouse "snippet" / Job Board insert template.
* Audit all 35 v2 postings to add back the missing Oxford-style comma after "battlefield scenarios".
* Re-import the 12 v3 postings using the canonical snippet so the four solutions links stop rendering with the `c-link c-link--underline` class.

### 5.2 Standardize section-heading authoring
* Mandate **`<p><strong>Title:</strong></p>`** for every top-level section.
* **Forbid** `<h1>`, `<h2>`, `<h3>` inside job-posting bodies. Remediate: 
  * `Senior Technical Support Representative – Japan` (h1)
  * `Aviation Compliance Lead`, `Aviation Regulatory Program Manager`, `Communications Manager`, `Senior Buyer`, `Software Engineer – Cloud Simulation & Full-Stack` (×2), `Software Engineer – Autonomy Infrastructure, Systems and Tools` (×2), `Revenue Operations Engineer, Quoting Systems` (h2)
  * `Senior Business Operations Manager`, `Software Engineer – Simulation & Robotics Engineer` (×2), `Full Stack Product Counsel`, `PhD Autonomy Engineer Intern – Planning & Controls` (h3)
  * `Hardware Engineering Program Manager` (h2 + h3 mixed)

### 5.3 Standardize section-heading wording
* House style: **sentence case + straight apostrophe + trailing colon**.
  * `About the role:`
  * `How you'll make an impact:`
  * `What makes you a good fit:`
  * (optional) `Bonus points:`
* Fix the typo in **`Senior People Analytics Analyst`** — `What Makes Your a Good Fit:` → `What makes you a good fit:`.
* Normalize curly vs straight apostrophes (`’` → `'`) across all 33 affected postings.

### 5.4 Strip editor artifacts
Pre-publish lint should remove:
* trailing `<br>` and `<br/>` inside `<li>` items (5 postings)
* empty `<p></p>` and `<p>&nbsp;</p>` (50 postings)
* `<div style="min-height:…">` placeholders (1 posting)
* `<u>` underline tags (7 postings) — replace with `<strong>` where emphasis is genuinely needed
* `&nbsp;` characters (28 postings) — convert to ordinary spaces unless deliberately preserving non-breaking behavior

### 5.5 International / no-compensation postings
* Adopt the same boilerplate + section template as US roles. The five no-comp postings (Taiwan, Zurich, Zurich/Tampere, Tokyo) currently each drift in different directions.
* Specifically rewrite `Senior Technical Support Representative – Japan` (h1 sections) and `Workplace Experience Coordinator Part-Time` (no-colon headings everywhere) — they are the most visible international outliers.

### 5.6 One posting needing line-by-line copy-edit
* `Director, Growth Marketing – Commercial` — single posting that triggers 5 different categories of flag. Worth a full re-author.

---

## Appendix A — Per-posting flag log

Full machine-readable data lives in [`data/per_job.json`](data/per_job.json) (one record per posting, including all flags, section-heading texts and link to the live job page).

---

*Generated by automated audit of the 106 job postings listed on https://www.skydio.com/careers as of 2026-05-22. Methodology: each individual `/jobs/<uuid>/` page was downloaded, the body content between the `<h1 class="type-h2">` job title and the `<p><strong>Compensation:</strong></p>` block was extracted, and tag/heading/text patterns were compared across the corpus to surface deviations from the majority pattern.*