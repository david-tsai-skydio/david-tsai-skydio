# Skydio Careers Page – Job Posting Formatting Audit

**Source:** `https://www.skydio.com/careers` plus all linked job‑detail pages
**Postings analyzed:** **112** (every open req visible on the page)
**Audit window:** content from the start of each posting up to (but **not including**) the *Compensation* block
**Audit date:** 2026‑05‑09

---

## 1. Executive summary

Skydio's careers page links to 112 individual job postings, all rendered through a shared `.prose` content style on `skydio.com/jobs/<uuid>`. The intended template is consistent and clean — but only **23 of 112 postings (≈21%) follow it without deviation**. The other **89 postings (≈79%) carry at least one formatting inconsistency** in the pre‑compensation content.

The five most prevalent issues are:

| # | Issue | Postings affected |
|---|-------|------------------:|
| 1 | Section heading wording deviates from the most common labels (e.g., `About the Role` vs `About the role`, 9 different "Bonus / Nice‑to‑have" labels, …) | **73** |
| 2 | Empty `<p></p>` paragraphs used as vertical spacers (creates inconsistent vertical rhythm) | **51** |
| 3 | Mixed bold styles within one posting (whole‑paragraph bold *and* inline bold prefix used together) | **35** |
| 4 | "Glued" headings — section titles fused into the same `<p><strong>…</strong></p>` block as their body copy (rendered as one continuous bold paragraph) | **34** |
| 5 | `<br><br>` used as paragraph separator inside one `<p>` instead of separate paragraphs | **21** |

There is also a smaller but visually loud cluster of **16 postings that use real `<h1>/<h2>/<h3>` heading tags inside the prose**. In Skydio's CSS those tags render **22 – 32 px at medium weight (500)**, while every other posting renders section titles at the body size (~16 – 18 px) at bold weight (700) — so those 16 postings literally have larger, lighter section titles than everyone else.

Almost all defects are content‑authoring artifacts (paste‑in markup from Word/Notion/Greenhouse), not CSS. None of the 112 postings carry inline `style="…"` overrides, so every visible formatting difference traces back to a fixable HTML structure or text choice.

---

## 2. Methodology

1. Downloaded the careers index and parsed out 112 unique job‑detail URLs (`/jobs/<uuid>/?gh_jid=<uuid>`).
2. Fetched the rendered HTML for every posting.
3. Extracted each posting's `<div class="prose block-content">` body and truncated it at the first occurrence of any of: `<strong>Compensation`, `<strong>Compensation Range`, `<strong>Pay Range`, `<strong>Salary Range`, `<strong>Pay Transparency`, `<strong>Compensation and Benefits`. (5 international/intern postings have no compensation block; their content was kept whole — they end at the EEO statement.)
4. For each posting, computed: heading element used (`<h2>` / `<h3>` / `<p><strong>`), heading text, casing, trailing punctuation, apostrophe glyph, list usage, empty paragraphs, `<br>` spacers, and unusual inline tags (`<u>`, `<b>`, `<i>`, inline `style="…"`).
5. Cross‑referenced findings against Skydio's published `.prose` CSS to translate "uses `<h2>`" / "uses `<p><strong>`" / "uses `<u>`" into the actual rendered font‑size / weight / decoration.

---

## 3. The intended ("canonical") template

23 postings render exactly as the design system intends. They look like this:

```text
[H1 job title @ type-h2 style]
[Location/employment‑type line @ type-body-2]

— intro paragraph: "Skydio is the leading US drone company…"   (regular body)
— <p><strong>About the role:</strong></p>                       (bold body)
— body paragraph(s) of role context
— <p><strong>How you'll make an impact:</strong></p>           (bold body)
— <ul><li>… </li></ul>
— <p><strong>What makes you a good fit:</strong></p>           (bold body)
— <ul><li>… </li></ul>
— <p><strong>Compensation:</strong> …</p>      ← cut‑off point
```

Key visual properties of the canonical template:

| Element                | Tag               | Font size            | Weight | Notes |
|------------------------|-------------------|----------------------|-------:|-------|
| Job title              | `<h1 class="type-h2">` | 22 – 32 px (clamp) | 500 | Outside the prose |
| Location line          | `<p class="type-body-2">` | ~14 – 16 px      | 400 | Outside the prose |
| Section heading        | `<p><strong>…:</strong></p>` | ~16 – 18 px (body) | **700 (strong)** | Inherits paragraph size, bold via `<strong>` |
| Body paragraph         | `<p>`             | ~16 – 18 px (body)   | 400 | |
| Bulleted item          | `<ul><li><p>…</p></li></ul>` | body         | 400 | `block-content ul li{padding:0 1em}` and `+li{margin-top:.5em}` |
| Block spacing          | (CSS only)        | —                    | —      | `block-content > * + * { margin-top: 1em }` — i.e., *no manual blank paragraphs are needed* |

Reference Skydio CSS values (extracted from the live page):

```text
.prose h1 → font-size: clamp(1.75rem, .7273rem + 2.8409vw, 3rem)   (~28–48 px, weight 500)
.prose h2 → font-size: clamp(1.375rem, .8636rem + 1.4205vw, 2rem)  (~22–32 px, weight 500)
.prose h3 → font-size: clamp(1.125rem, .6136rem + 1.4205vw, 1.75rem) (~18–28 px, weight 500)
.prose h4–h6 → progressively smaller, all weight 500
block-content > * + * { margin-top: 1em }
```

This is critical context for the findings below: **every time a posting drops an `<h2>`/`<h3>`/`<h1>` into the prose, the section title visually balloons and de‑bolds versus the canonical bold‑body style.**

---

## 4. Findings — formatting inconsistencies

### Finding 4.1 — Heading element type is not consistent

| Heading style | Postings | Rendered impact |
|---|---:|---|
| `<p><strong>` whole‑paragraph only (canonical) — bold body | **64** | Section titles are 16 – 18 px, weight 700 |
| Mixes whole‑paragraph bold with inline bold prefixes (`<p><strong>X:</strong> body…</p>`) | **32** | The prefix variant has no visible block break before the body, producing a tighter, jagged rhythm versus canonical |
| Uses real `<h2>` inside the prose (with or without other styles) | **10** | Section titles render at **22 – 32 px, weight 500** — visibly larger and *less bold* than peers |
| Uses real `<h3>` | **5** | Section titles render at **18 – 28 px, weight 500** — also larger/lighter than peers |
| Uses real `<h1>` (only one posting) | **1** | Section titles render at **28 – 48 px** — same size as the page's job title |

**Postings that use heading tags (visually different from peers):**

* **`<h1>` (extreme outlier):** Senior Technical Support Representative – Japan
* **`<h2>`:** Aviation Compliance Lead; Aviation Regulatory Program Manager; Communications Manager; Deployment Coordinator; Revenue Operations Engineer, Quoting Systems; Senior Buyer; Software Engineer – Autonomy Infrastructure, Systems and Tools (San Mateo + Zurich); Software Engineer – Cloud Simulation & Full‑Stack (San Mateo + Zurich)
* **`<h3>`:** Field Marketing Event Manager; PhD Autonomy Engineer Intern – Planning & Controls (Reinforcement Learning); Project Manager, Workplace; Software Engineer – Simulation & Robotics Engineer (San Mateo + Zurich)

> Issue example: "**Senior Buyer**" displays *How you will make an impact* at ~26 px medium weight, while the next posting on the listing — *Senior NPI Product Quality Engineer* — displays the same heading at ~16 px bold. Side by side, the headings appear to be from two different brands.

---

### Finding 4.2 — Heading wording / casing is not consistent

The same canonical sections appear under many different labels.

**"About the role" variants (same intended section):**

| Label | Count |
|---|---:|
| `About the role` | 49 |
| `About the Role` | 33 |
| `About The Role` | 1 |
| `About the team` | 5 |
| `About the Team` | 6 |

So the most common section heading on the careers page exists in **5 capitalisation variants**.

**"How you'll make an impact" variants:**

| Label | Count |
|---|---:|
| `How you'll make an impact` *(straight apostrophe, sentence case)* | 27 |
| `How you'll make an impact` *(curly apostrophe, sentence case)* | 13 |
| `How You'll Make an Impact` *(curly, title case)* | 20 |
| `How You'll Make an Impact` *(straight, title case)* | 1 |
| `How you will make an impact` | 3 |

Across all postings, **43 use a straight ASCII apostrophe and 44 use a curly Unicode apostrophe** in their headings. **13 postings mix both glyphs in the same posting**, which means within a single page a reader sees `How you'll make an impact` next to `What makes you a good fit` with two different apostrophe shapes.

**"What makes you a good fit" variants:**

| Label | Count |
|---|---:|
| `What makes you a good fit` | 56 |
| `What Makes You a Good Fit` | 22 |
| `What Makes You A Good Fit` | 3 |
| `What would make you a good fit` | 6 |
| `What Would Make You a Good Fit` | 2 |
| `What makes you a strong fit` | 4 |
| `What would make you a strong fit` | 2 |
| `Qualifications` | 7 |
| `Requirements` | 1 |
| `Useful skills and experience` | 2 |

**"Bonus / Nice‑to‑have" variants:** **9 distinct labels** covering the same concept:

| Label | Count |
|---|---:|
| `Bonus Experience` | 6 |
| `Bonus points for` | 4 |
| `Bonus Points` | 3 |
| `Bonus points` | 2 |
| `Nice to have` | 2 |
| `Nice To Haves` | 2 |
| `Nice‑to‑have` | 1 |
| `Preferred Qualifications` | 2 |
| `Preferred Skills & Experience` | 1 |

---

### Finding 4.3 — Trailing punctuation on headings is not consistent

| Pattern within a single posting | Postings |
|---|---:|
| Every heading ends with `:` (canonical) | 85 |
| Mix of `:` and no punctuation | 17 |
| Every heading has no trailing punctuation | 6 |
| Mix of `.` and `:` | 4 |

Within a single posting (e.g., *Senior Software Engineer, Full Stack*) you can see *How you'll make an impact:* followed by *What would make you a good fit* (no colon) followed by *Work Location*.

---

### Finding 4.4 — Bold‑style mixing inside the same posting

35 postings combine two different bold conventions:

* **Whole‑paragraph bold heading:** `<p><strong>Section name:</strong></p>` → produces a clear blank‑line separation before the next paragraph (canonical look).
* **Inline bold prefix:** `<p><strong>Section name:</strong> Body text continues on the same line…</p>` → visually no blank line; the section title sits on the same baseline as its body copy.

When these two styles appear in the same posting, the *visual cadence* of the page is jagged — some sections feel like real headings, others feel like in‑paragraph emphasis.

A representative example from the audit: *Director of Product Management, Drone as First Responder (DFR)* uses **whole‑paragraph bold** for *Bonus points for* but **inline bold prefix** for *About the role:* — so the reader sees one heading appear like a heading and another appear like an inline label.

---

### Finding 4.5 — "Glued" headings (paragraph‑break bug)

**34 postings** contain a `<p><strong>…</strong></p>` block whose bold text is **>120 characters long**, which means the section heading and the body paragraph(s) that should follow it have been concatenated into one giant bold block. This is almost always a paste‑in error where a `</p><p>` was lost or replaced with a `<br>` (see 4.6).

Real example (rendered on the page as one bold paragraph that is 5 sentences long, all bold):

> **About the role:Learning a semantic and geometric understanding of the world from visual data is the core of our autonomy system… As a deep learning infrastructure engineer, you will be responsible for building and scaling the infrastructure that supports Skydio's Deep Learning (DL) and AI efforts… How you'll make an impact**

Postings affected (34):
*Autonomy Engineer – Deep Learning Infrastructure (Zurich); Autonomy Engineer – Deep Learning Model Acceleration (Zurich + San Mateo); Autonomy Software Engineer; Customer Success Manager, DFR Majors – Northeast; Deployment Engineer – Southeast; Director of Product Management, DFR; Electric Motor / Propulsion Engineer; Field Support Representative (Southwest, Remote); GTM Data Engineer Intern; GTM Enablement Associate; Hardware Operations Program Manager; Hardware Technician; Lead Staff Electrical Engineer (F10 Program); PhD Autonomy Engineer Intern – Planning & Controls (Reinforcement Learning); Product Design Engineer (All Levels); Product Support Engineer; Product Support Engineer Intern; Program Leader, Law Enforcement & Public Safety Training; Revenue Operations Engineer, Quoting Systems; Sales Planning Analyst Intern; Senior Autonomy Engineer – Deep Learning (San Mateo + Zurich); Senior Brand Designer (Contract); Senior Customer Support Representative – India; Senior People Analytics Analyst; Senior Product Manager, Platform & Infrastructure; Senior Software Engineer, Infrastructure; Senior Technical Recruiter – Hardware Operations; Software Engineer – Infrastructure; Software Engineer Intern Fall 2026/Winter 2027; Staff Product Manager, Platform & Infrastructure; Technical Support Specialist – West Coast; Workplace Experience Coordinator Part‑Time.*

---

### Finding 4.6 — `<br><br>` used as paragraph separator inside a `<p>`

21 postings use `<br /><br />` to fake paragraph breaks inside one `<p>` instead of closing and re‑opening the paragraph. Combined with Finding 4.5, this is the primary reason headings become "glued" to their body copy. CSS sets `block-content > * + * { margin-top: 1em }` — but this rule only fires *between* block elements. `<br>` runs do **not** trigger that spacing, so blocks built with `<br><br>` collapse to half the vertical rhythm of canonical postings.

Postings affected (21):
*Autonomy Engineer – Deep Learning Infrastructure (Zurich + San Mateo); Autonomy Engineer – Deep Learning Model Acceleration (Zurich + San Mateo); Autonomy Software Engineer; Director of Product Management, DFR; Electrical Engineer (all levels); PCB Layout Engineer; Product Support Engineer; Product Support Engineer Intern; Production Supervisor; Senior Autonomy Engineer – Deep Learning (San Mateo + Zurich); Senior Brand Designer (Contract); Senior Staff Product Manager, Drone Hardware Platforms & Sensors; Senior Supplier Quality Engineer; Senior Technical Recruiter – Hardware Operations; Senior Technical Support Representative – Japan; Software Engineer Intern Fall 2026/Winter 2027; Supply Chain Intern; Wireless Hardware Engineer Intern.*

---

### Finding 4.7 — Empty `<p>` paragraphs used as vertical spacers

51 postings include 1 – 6 empty `<p></p>` blocks. The CSS already adds `margin-top: 1em` between every adjacent block, so these empty paragraphs **double the gap** between sections, producing visibly inconsistent vertical rhythm against the 61 postings that don't use them.

| Empty paragraphs in posting | Postings |
|---:|---:|
| 0 | 61 |
| 1 | 19 |
| 2 | 13 |
| 3 | 12 |
| 4 | 4 |
| 5 | 1 |
| 6 | 2 |

The two postings with **6 empty paragraphs** — *Senior Product Manager, Platform & Infrastructure* and *Staff Product Manager, Platform & Infrastructure* — render with roughly twice the inter‑section whitespace of the canonical template.

---

### Finding 4.8 — `<u>` (underline) used as emphasis

6 postings use `<u>` to underline body words. The Skydio prose CSS reserves underline as the link‑hover indicator (`block-content a:not(.button):hover { text-decoration: underline }`), so underlined non‑link text reads as a misclick‑bait broken link.

Affected: *Lead Staff Electrical Engineer (F10 Program); Senior NPI Product Quality Engineer; Senior Software Engineer, Full Stack; Senior Technical Recruiter; Senior Technical Recruiter – Hardware Operations; Staff Technical Recruiter.*

(There are no `<b>`, `<i>`, `<font>`, or inline `style="…"` attributes anywhere in the corpus — those are clean.)

---

### Finding 4.9 — Custom / non‑canonical section structures

Beyond label variations (4.2), several postings use entirely different section frameworks. These postings stand out as visually distinct because they have *more* sections than peers and use real heading tags:

* **Field Marketing Event Manager** — 7 `<h3>` sections: *Customer Summit Planning & Execution / Field Marketing & Trade Show Support / Relationship Building & Internal Collaboration / Required Experience / Preferred Skills & Experience / Interpersonal & Professional Skills / Physical & Travel Requirements*. This is visually a completely different document from the rest of the page.
* **Director, Growth Marketing – Commercial** — 4 bold sections: *Key Responsibilities / What Success Looks Like / What Would Make You a Good Fit / Additional Desired Experience and Skills*.
* **Project Manager, Workplace** — 1 `<h3>` (*How You'll Operate*) plus 6 specialty bold sub‑headings (*Bring Skydio's HQ and vision to life*, *Translate technical needs into physical environments*, etc.).
* **Software Engineer – Autonomy Infrastructure / Cloud Simulation / Simulation & Robotics** (6 postings, San Mateo + Zurich) — share a custom `<h2>`/`<h3>` template with sections *Areas of Responsibility / What You'll Do / Bonus Experience*.
* **Success Systems Specialist** — 5 unique bold sections (*Why This Role Matters Now / Build Automation & Intelligence into Mission Success / Customer Digital Experience / Cross‑Functional Architecture & Governance / Scalability & Cost Avoidance*).
* **Revenue Operations Engineer, Quoting Systems** — 5 `<h2>` sections (*What you'll drive (scope) / Day‑to‑day responsibilities / Tech stack you'll work with / What you'll bring / Reporting & Working Model*).

---

### Finding 4.10 — Section ordering varies

Across the canonical sections (intro → about_role → impact → qualifications → nice_to_have), the audit observed **18 distinct section orderings**:

| Ordering | Postings |
|---|---:|
| about_role → impact → qualifications  *(canonical)* | 45 |
| impact → qualifications  *(no "About the role")* | 15 |
| about_role → qualifications  *(no impact section)* | 9 |
| about_role → impact  *(no qualifications)* | 8 |
| about_role → responsibilities → qualifications → nice_to_have | 6 |
| about_role → impact → qualifications → nice_to_have | 5 |
| impact → qualifications → nice_to_have | 5 |
| (other 11 orderings, ≤ 4 each) | 19 |

A reader scanning multiple postings on the same job family (e.g., comparing Autonomy roles) will not find the same information in the same order.

---

### Finding 4.11 — Job‑title typos (`<h1>` content)

4 postings have **double whitespace** in the page title:

* `Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM`
* `Senior Software Engineer,  Data Platform`
* `Senior Software Engineer,  Infrastructure`
* `Staff Global Supply Manager,  Mechanicals`

This isn't a CSS issue but it shows up in the rendered title and in the careers index list.

---

### Finding 4.12 — Length is highly variable

| Statistic | Pre‑comp text length (chars) |
|---|---:|
| Min | 1,655 (*Supply Chain Intern*) |
| Median | 3,216 |
| Mean | 3,312 |
| Max | 5,739 (*Staff Product Manager, Platform & Infrastructure*) |

The longest five postings are **3.5×** longer than the shortest five. Both PM Platform & Infrastructure postings (Senior + Staff) are over 5,500 characters and are the same outliers that have 6 empty‑paragraph spacers and the "glued heading" bug — they're effectively the worst‑formatted postings on the careers page.

---

## 5. Postings that stand out the most (top 18 hot spots)

Sorted by number of independent formatting flags. These are where editing effort should be focused first.

| # | Title | Location | Flags |
|---:|---|---|---|
| 1 | Revenue Operations Engineer, Quoting Systems | San Mateo, CA | empty‑p×2, uses `<h2>`, mixed casing, mixed trailing punct, glued heading, mixed bold styles |
| 2 | Software Engineer Intern Fall 2026/Winter 2027 | US CA San Mateo | `<br><br>`‑paragraphs, empty‑p×1, mixed trailing punct, glued heading, mixed bold styles, mixed apostrophes |
| 3 | GTM Enablement Associate | San Mateo, CA | empty‑p×1, mixed casing, glued heading, mixed bold styles, mixed apostrophes |
| 4 | Product Support Engineer | San Mateo, CA | `<br><br>`‑paragraphs, empty‑p×2, glued heading, mixed bold styles, mixed apostrophes |
| 5 | Product Support Engineer Intern | San Mateo, CA | `<br><br>`‑paragraphs, empty‑p×3, glued heading, mixed bold styles, mixed apostrophes |
| 6 | Senior Brand Designer (Contract) | San Mateo, CA | `<br><br>`‑paragraphs, empty‑p×3, mixed trailing punct (`.` and `:`), glued heading, mixed apostrophes |
| 7 | Senior Product Manager, Platform & Infrastructure | San Mateo, CA | empty‑p×6, mixed trailing punct, glued heading, mixed bold styles, mixed apostrophes |
| 8 | Staff Product Manager, Platform & Infrastructure | San Mateo, CA | empty‑p×6, mixed trailing punct, glued heading, mixed bold styles, mixed apostrophes |
| 9 | Director of Product Management, DFR | San Mateo, CA | `<br><br>`‑paragraphs, glued heading, mixed bold styles, mixed apostrophes |
| 10 | GTM Data Engineer Intern | San Mateo, CA | empty‑p×2, glued heading, mixed bold styles, mixed apostrophes |
| 11 | Lead Staff Electrical Engineer (F10 Program) | San Mateo, CA | empty‑p×2, `<u>` underline, glued heading, mixed bold styles |
| 12 | Project Manager, Workplace | San Mateo, CA | empty‑p×1, uses `<h3>`, mixed trailing punct, mixed bold styles |
| 13 | Senior Autonomy Engineer – Deep Learning | San Mateo, CA | `<br><br>`‑paragraphs, empty‑p×1, glued heading, mixed bold styles |
| 14 | Senior People Analytics Analyst | San Mateo, CA | mixed casing, mixed trailing punct, glued heading, mixed bold styles |
| 15 | Senior Software Engineer, Full Stack | San Mateo, CA | `<u>` underline, mixed casing, mixed trailing punct, mixed bold styles |
| 16 | Senior Software Engineer, Infrastructure | San Mateo, CA | glued heading, mixed bold styles, **double‑space in title**, mixed apostrophes |
| 17 | Senior Technical Recruiter – Hardware Operations | San Mateo, CA | `<br><br>`‑paragraphs, `<u>` underline, glued heading, mixed apostrophes |
| 18 | Workplace Experience Coordinator Part‑Time | Zurich | empty‑p×1, mixed casing, mixed trailing punct, glued heading |

The complete per‑posting flag spreadsheet is checked in alongside this report (`skydio-careers-formatting-audit-per-posting.csv`).

---

## 6. Recommendations (in priority order)

### 6.1 Fix the rendering bugs first (highest visual impact)
1. **Replace every `<br><br>` paragraph break with proper `</p><p>` tags** in the 21 affected postings (Finding 4.6). This single fix also resolves most of the 30 "glued heading" cases (4.5).
2. **Delete every empty `<p></p>` block** in the 49 affected postings (4.7). The `block-content > * + * { margin-top: 1em }` rule already provides the right vertical rhythm.
3. **Replace `<u>` with either a link, `<em>`, or plain text** in the 6 affected postings (4.8). Underline reads as "broken link" on this site.

### 6.2 Standardize heading markup
4. **Always use `<p><strong>Section name:</strong></p>` for section headings**, not `<h2>` / `<h3>` / `<h1>`. Migrate the 16 postings flagged in 4.1 — particularly the Software Engineer family of 6 postings (Autonomy Infra, Cloud Sim, Simulation & Robotics) which currently use `<h2>`/`<h3>`. Either change those headings or, if larger headings are desired by Recruiting, **promote that style to the canonical template** and migrate all 96 other postings in the opposite direction. Pick one.
5. **Pick one bold style** — whole‑paragraph bold (`<p><strong>X:</strong></p>` followed by a separate `<p>`) — and stop using inline bold prefixes (`<p><strong>X:</strong> body…</p>`) for section headings. This eliminates the 40 mixed‑bold‑style postings (4.4).

### 6.3 Standardize heading text
6. **Adopt one canonical label per section** and search/replace across all 112 postings. Recommended labels (matching the most common variant):
   * Intro → unchanged ("Skydio is the leading US drone company…")
   * `About the role:` (sentence case, colon)
   * `How you'll make an impact:` (sentence case, **straight ASCII apostrophe**, colon)
   * `What makes you a good fit:` (sentence case, colon)
   * `Bonus points:` (sentence case, colon) — retire *Bonus Experience / Bonus Points / Nice to Haves / Nice‑to‑have / Preferred Qualifications / Useful skills and experience*.
7. **Choose a single apostrophe style** — recommend straight ASCII (`'`) since 43 postings use it and it's safer for copy/paste — and find/replace all 44 curly variants in headings. Resolves the 15 mixed‑apostrophe postings (4.2).
8. **Always end section headings with a colon** (the dominant convention, 85/112 postings). Resolves Finding 4.3.

### 6.4 Standardize section sequence
9. **Enforce the canonical order:** *intro → About the role → How you'll make an impact → What makes you a good fit → (optional Bonus points) → Compensation*. The 67 postings that currently deviate (4.10) should be reordered.
10. **Retire the bespoke templates** in *Field Marketing Event Manager*, *Director, Growth Marketing – Commercial*, *Project Manager, Workplace*, *Success Systems Specialist*, *Revenue Operations Engineer, Quoting Systems*, the 6 SWE postings, and *Workplace Experience Coordinator Part‑Time* (4.9). If hiring managers truly need extra sub‑sections, add them as additional `<p><strong>…:</strong></p>` blocks **inside** the canonical sections, not as alternative templates.

### 6.5 Hygiene
11. **Fix the 4 double‑space typos** in job titles (4.11): *Enterprise Account Manager, US Navy / US Marine Corps / IC‑SOCOM*; *Senior Software Engineer, Data Platform*; *Senior Software Engineer, Infrastructure*; *Staff Global Supply Manager, Mechanicals*.
12. **Add a length sanity check** in the publishing workflow. The two PM Platform & Infrastructure postings at ~5,700 chars are 78% longer than the median posting — almost certainly because they were drafted in a long Word document and pasted in unedited.
13. **Add a pre‑publish lint** (it could literally be the Python script used to produce this report) that runs on every job posting at publish time and blocks the publish if any of the rules above are violated. The same script can produce a weekly drift report after launch.

### 6.6 Process
14. **Standardize on a single rich‑text source** (e.g., Greenhouse's editor, never copy‑paste from Word/Notion). Most of the bugs in 4.5 / 4.6 / 4.7 / 4.8 are paste‑in artifacts.
15. **Document the canonical template** (Section 3 above can be the basis) inside the recruiting playbook so hiring managers don't reach for `<h2>` or "Bonus Experience" by default.

---

## Appendix — Per‑posting flags

The full table of all 112 postings, their exact flag list, and the source URL is in `skydio-careers-formatting-audit-per-posting.csv` (alongside this report).
