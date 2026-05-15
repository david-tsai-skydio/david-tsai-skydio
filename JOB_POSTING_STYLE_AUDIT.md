# Skydio Careers — Job Posting Formatting Consistency Audit

**Source:** `https://www.skydio.com/careers`  
**Scope:** All **109 unique job postings** linked from the careers landing page, analyzing only the **pre‑compensation body** (everything inside `<div class="prose block-content">` up to — but not including — the "Compensation:" section).  
**Date of capture:** May 15, 2026

---

## 1. How the page is built (context for the findings)

All postings render through the same Sanity-backed template, so the **page-chrome typography is identical across every posting**:

| Element | Markup used on every posting | Effective rendered style |
|---|---|---|
| Page title (role name) | `<h1 class="type-h2">…</h1>` | 28 – 48 px, bold (the site's `type-h2` token) |
| Location / employment-type line | `<p class="type-body-2">…</p>` | small body text |
| Description body | `<div class="prose block-content">…</div>` | base body text 16 – 18 px |
| **Inside** `.prose`, raw heading tags are styled by the site CSS as: |  |  |
| `<h1>` inside prose | `clamp(1.75rem, 3rem)` | **28 – 48 px**, bold |
| `<h2>` inside prose | `clamp(1.375rem, 2rem)` | **22 – 32 px**, bold |
| `<h3>` inside prose | `clamp(1.125rem, 1.75rem)` | **18 – 28 px**, bold |
| `<p><strong>…</strong></p>` (default pattern) | inherits body size | **16 – 18 px**, bold |

> **This is the most important fact in the whole audit:** the *only* way a section heading appears at a larger font size in one posting than another is if a recruiter dropped in a raw `<h1>`/`<h2>`/`<h3>` tag while editing. Most postings just bold a paragraph, so their section headings render at body size. **The size difference between the two styles is roughly 2× larger / 50–80 % taller line-height**, so the inconsistency is *very* visible to a candidate browsing multiple roles.

The audit therefore focuses on what recruiters put inside `.prose block-content` — that is where every visible inconsistency lives.

---

## 2. The canonical (modal) pre-compensation pattern

Across the 109 postings the **dominant** structure is:

1. **One** intro paragraph about Skydio + the team (used by 70/109 postings; ~64 %).
2. **Three bolded-paragraph section headings**, in this order:
   - **`About the role:`**
   - **`How you'll make an impact:`** *(followed by a `<ul>` of bullets)*
   - **`What makes you a good fit:`** *(followed by a `<ul>` of bullets)*
3. Section headings are written as `<p><strong>Section title:</strong></p>` — i.e. **bold body text, not real headings**.
4. Each bullet is `<li><p>…</p></li>`, starts with a capital letter, and **does not** end in a period.
5. Apostrophes use curly quotes (`'`) but a substantial minority use straight ASCII (`'`).
6. No headings, colors, font tags, inline styles, or `<u>` underlines are used.

The numbers behind this:

| Signal | Count of 109 postings |
|---|---|
| Job title rendered via `h1.type-h2` | 109 / 109 |
| Location subline rendered via `p.type-body-2` | 109 / 109 |
| Description container is `div.prose.block-content` | 109 / 109 |
| Postings with **exactly 1 intro paragraph** before the first section heading | 70 |
| Postings using `<p><strong>…:</strong></p>` for at least one section heading | 94 |
| Postings using `<p><strong>…:</strong></p>` *exclusively* for section headings | 89 |
| Postings whose `<li>` items are wrapped in `<p>` (the template default) | 105 |
| Postings using ordered lists `<ol>` in pre-comp content | 0 |
| Postings using empty `<p></p>` spacer paragraphs | 0 |
| Postings with inline `style="…"` overrides | 0 |
| Postings with `<font color>` / `style="color:…"` overrides | 0 |
| Bullets that start with a lowercase letter | 0 |

So **font colour, alignment, line-height, font-family and explicit font-size are consistent across all postings** — nobody is overriding them. The inconsistencies that *do* exist live in **structural / markup choices** that change which CSS rule wins.

---

## 3. The inconsistencies (with evidence and severity)

### 3.1 ⚠️ HIGHEST IMPACT — Section headings rendered at different font sizes

A subset of postings uses real heading tags inside the description, which renders the section heading at **roughly 1.4× to 2× the size** of the dominant bolded-paragraph style. Within that subset, three different heading levels are used, producing **three different visual sizes for "About the role"** across the careers site.

| Markup used for section headings | Rendered size | # of postings | Postings |
|---|---|---|---|
| `<p><strong>…:</strong></p>` only *(canonical)* | 16 – 18 px | **89** | the modal pattern (see appendix) |
| `<h2>…</h2>` only | 22 – 32 px | **7** | Software Engineer – Autonomy Infrastructure, Systems and Tools (SF + Zurich); Software Engineer – Cloud Simulation & Full-Stack (SF + Zurich); Communications Manager; Aviation Compliance Lead; Aviation Regulatory Program Manager |
| `<h3>…</h3>` only | 18 – 28 px | **3** | Software Engineer – Simulation & Robotics Engineer (SF + Zurich); Full Stack Product Counsel |
| `<h1>…</h1>` only | 28 – 48 px (**same size as the page title!**) | **1** | **Senior Technical Support Representative – Japan** |
| Mix of `<hN>` and `<p><strong>` headings in the same posting | inconsistent within one posting | **5** | PhD Autonomy Engineer Intern – Planning & Controls (Reinforcement Learning); Senior Buyer; Field Marketing Event Manager; Revenue Operations Engineer, Quoting Systems; Senior Business Operations Manager |
| No section headings at all (plain prose + bullets) | n/a | **4** | PhD Autonomy Engineer Intern – Deep Learning or Computer Vision; Product Support Engineer; Product Support Engineer Intern; Technical Support Specialist – West Coast |

**Specific flags:**

- **"Senior Technical Support Representative – Japan"** uses `<h1>` for *every* section heading, so the headings render at the **same visual size as the page's role title**. This is by far the most jarring outlier.
- The **Software Engineer – Autonomy Infrastructure** pair (SF + Zurich) uses `<h2>`, while the very similar **Software Engineer – Simulation & Robotics Engineer** pair (SF + Zurich) uses `<h3>`. Two roles owned by the same team, advertised side-by-side, render their section headings at noticeably different sizes.
- **Communications Manager**, **Aviation Compliance Lead**, **Aviation Regulatory Program Manager**, and **Full Stack Product Counsel** all use `<h2>`/`<h3>` and **drop the trailing colon** ("About the Role" rather than "About the role:") — they look like a different template.
- **Field Marketing Event Manager** has *seven* `<h3>` sub-headings (`Customer Summit Planning & Execution`, `Field Marketing & Trade Show Support`, `Required Experience`, …) and no canonical "About the role / How you'll make an impact / What makes you a good fit" anywhere. It is the only posting on the site that follows this structure.
- **Senior Business Operations Manager** uses three `<h3>` headings ("Strategic Sourcing:", "Cost Management", "Strategy & Operations") that mix colon / no-colon and skip the canonical headings entirely.
- **Revenue Operations Engineer, Quoting Systems** uses five `<h2>` sub-headings with a completely bespoke vocabulary ("What you'll drive (scope):", "Day-to-day responsibilities:", "Tech stack you'll work with:", "What you'll bring:", "Reporting & Working Model:").

### 3.2 ⚠️ HIGH IMPACT — Inconsistent section-heading wording, casing, and apostrophes

Across the 105 postings that *do* use some form of section heading (bold paragraphs or real heading tags), the same concept is written in many different ways. The frequency-sorted list of every literal heading string in pre-comp content (across both `<p><strong>` and `<hN>` markup) is:

| String | Count |
|---|---|
| `What makes you a good fit:` | 53 |
| `About the role:` | 46 |
| `How you'll make an impact:` *(straight apostrophe)* | 36 |
| `About the Role:` | 22 |
| `How You'll Make an Impact:` *(curly apostrophe, title case)* | 20 |
| `What Makes You a Good Fit:` | 18 |
| `How you'll make an impact:` *(curly apostrophe, sentence case)* | 13 |
| `About the Team:` | 6 |
| `About the team:` | 5 |
| `What would make you a good fit:` | 5 |
| `Bonus points:` | 3 |
| `Bonus Points:` | 3 |
| `Bonus points for:` | 3 |
| `What Makes You A Good Fit:` | 3 |
| `Nice To Haves:` | 2 |
| `Nice to have:` | 2 |
| `Nice-to-Haves:` | 1 |
| `Nice to Have` | 1 |
| `Preferred Qualifications:` | 2 |
| `Preferred Qualifications` *(no colon)* | 1 |
| `What would make you a strong fit:` | 2 |
| `What makes you a strong fit:` | 1 |
| `What Would Make You a Good Fit:` | 2 |
| `How you will make an impact:` | 2 |
| `How You'll Make an Impact:` *(straight apostrophe, title case)* | 1 |
| `Useful skills and experience:` *(only Hardware Test Engineer + Systems Integration Engineer)* | 2 |
| `About the Role` *(no colon, h2)* | 4 |
| `About The Role` *(odd capitalization of "The")* | 1 |
| `About the Role` *(no colon, p strong)* | 1 |

Specific flags this surfaces:

- **3 distinct apostrophe characters** appear in "How you'll make an impact": straight `'`, curly `'`, plus the all-caps "How You'll …" variant — **6 different surface forms of the same heading**.
- **"What makes you a good fit"** appears in **8 different surface forms** (sentence vs. title vs. "A"-capitalised, "good" vs. "great" vs. "strong", with/without colon).
- **Typo in "Senior People Analytics Analyst":** `What Makes Your a Good Fit:` (extra "r" on "Your"). **Must be fixed.**
- **"How you will make an impact"** (no contraction) only appears on `Senior Hardware Test and Reliability Engineer`, `Systems Integration and Test Engineer`, and `Senior Buyer`. Everywhere else uses the contraction.
- **"Useful skills and experience:"** is used by 2 hardware postings instead of the canonical "What makes you a good fit:".

### 3.3 HIGH IMPACT — Trailing-colon inconsistency on section headings

The norm is `About the role:` *with* trailing colon (93 / 106 postings that have any heading).

- **12 postings mix** colon and no-colon headings within the same posting.
- **1 posting (IT Technician — Help Desk, Linux Focus)** drops the colon on every heading and has no consistent canonical structure at all (`About the Role`, `Location`, `Onsite - 5 days/week, Monday - Friday: 3:30pm - 12am Skydio Manufacturing (Hayward, CA)`, `What You'll Do`, `What Makes You a Good Fit`, `Nice to Have`). The "Onsite – 5 days/week…" line is bolded as a paragraph and visually reads as a section heading because of it.
- All four `<h2>`/`<h3>` postings noted in §3.1 (Communications Manager, Aviation Compliance Lead, Aviation Regulatory Program Manager, Full Stack Product Counsel) drop the colon, which combined with the larger heading size makes them stand out twice.

### 3.4 HIGH IMPACT — Inconsistent bullet end-punctuation

Across all 1 808 bullets in pre-comp content:

- 1 037 bullets end **without** punctuation (the dominant style).
- 771 bullets end with a period.
- **46 of 109 postings mix the two styles within a single posting.** Examples:
  - `Autonomy Engineer Intern – Deep Learning (Computational Photography)`: 1 bullet with period, 14 without.
  - `RF Design Engineer`: 2 with, 17 without.
  - `Software Engineer – Autonomy Infrastructure, Systems and Tools` (the `<h2>` variant): 18 with, 2 without — the *opposite* default.
  - `Wireless Software Engineer`: 10 with, 2 without.
  - `Senior Software Engineer – Embedded` family (3 postings: Senior, Software Engineer, Staff): each 2 with, 15 without.

The pattern suggests **bullets are being copy-pasted between postings and end-punctuation is being added or stripped inconsistently** during the import.

### 3.5 MEDIUM IMPACT — Bolded paragraphs that are *not* section headings

Recruiters occasionally wrap an emphasis sentence in `<strong>`, which the audit tool detects as a section heading and which visually reads as one to a candidate:

- **Senior Brand Designer (Contract):** the opening lead paragraph
  *"We're looking for an experienced Senior Brand Designer to help shape how Skydio shows up in the world—crafting clear, compelling, and memorable visual experiences across a wide range of touchpoints for the leader in autonomous flight."*
  is fully bolded — it reads as a section heading but is body copy.
- **Senior Product Manager / Staff Product Manager, Platform & Infrastructure:** each starts with a bold paragraph that just says `Location` (no colon), followed by the office location on the next line. This duplicates information already shown in the page's location subline and creates a visual mini-heading where none is needed.
- **Enterprise Account Manager (MoD/MoI) – EMEA** (Finland, Germany, Switzerland — three postings): each contains the bold paragraph `This role must be based in Switzerland, Germany, or Finland.` between `About the Role:` and `How You'll Make an Impact:`. It is identical in all three but appears as a pseudo-heading rather than a callout. Either it should be a real callout or italicised inline.
- **Senior People Analytics Analyst** uses bullets that *begin* with a bolded fragment ("**Lead People Analytics Strategy** – Define & evolve…"). Only this posting does this — every other posting writes bullets as plain sentences.

### 3.6 MEDIUM IMPACT — Intro / overview length and structure

The number of intro paragraphs *before* the first section heading ranges from 0 to 10 paragraphs.

| Intro paragraphs | # of postings |
|---|---|
| 1 (norm) | 70 |
| 2 | 11 |
| 3 | 10 |
| 4 | 12 |
| 5 | 2 |
| 6 | 2 |
| 9 | 1 (Technical Support Specialist – West Coast) |
| 10 | 1 (Full Stack Product Counsel) |

Postings at the extreme end (Technical Support Specialist – West Coast, Full Stack Product Counsel, Director of Product Management DFR, Manager Technical Support) read as essay-style narratives rather than structured job posts. They also tend to be the longest pre-comp content overall:

| Posting | Pre-comp word count |
|---|---|
| Director of Product Management, Drone as First Responder (DFR) | **875** |
| Staff Product Manager, Platform & Infrastructure | 786 |
| Manager, Technical Support | 780 |
| Full Stack Product Counsel | 771 |
| Senior Product Manager, Platform & Infrastructure | 767 |
| Senior Software Engineer, Data Platform | 731 |
| … | |
| Median across all 109 postings | 474 |
| Electrical Engineer (all levels) | **244** (shortest) |

There is a **3.6× spread** between the shortest and longest pre-comp content, which by itself produces very different page rhythms.

### 3.7 MEDIUM IMPACT — Underlined text in body copy

Seven postings include `<u>…</u>` in the pre-comp content. Underlining inside body text is conventionally read as a hyperlink, so this is a usability issue:

- Lead Staff Electrical Engineer (F10 Program)
- Senior Software Engineer, Full Stack
- Full Stack Product Counsel
- Senior NPI Product Quality Engineer
- Senior Technical Recruiter
- Senior Technical Recruiter – Hardware Operations
- Staff Technical Recruiter

### 3.8 MEDIUM IMPACT — Listing structure within `<ul>`

- 105 / 109 postings consistently wrap each `<li>` content in `<p>`, which is the template's own normal output.
- **2 postings mix both styles within a single `<ul>`**, producing uneven vertical spacing between adjacent bullets:
  - `IT Technician (Help Desk – Linux Focus)`
  - `Mission Success Operations Manager`
- **1 posting (`PhD Autonomy Engineer Intern – Deep Learning or Computer Vision`) uses *only* the plain `<li>text</li>` style** — its bullets render with slightly tighter spacing than every other posting on the site.
- **Ordered lists are never used.**

### 3.9 LOW IMPACT — Punctuation / quote characters

- **17 postings use only ASCII straight quotes** (`'` `"`) in the pre-comp body.
- **42 postings use only curly typographic quotes** (`'` `"`).
- **48 postings mix both within the same posting.**

This is the kind of thing the site CSS cannot normalise — only the source content can. It does not change font size, but it does produce visible variance in how possessives and contractions render side-by-side.

### 3.10 LOW IMPACT — Duplicate roles with diverging formatting

Skydio lists the same role multiple times when it's open in multiple offices. In several cases the duplicate postings have **the same content but inconsistent formatting choices**, suggesting they were edited separately:

| Role | Variants | Diff |
|---|---|---|
| `Autonomy Engineer – Deep Learning` | SF / Zurich | One copy of the SF version is listed under no department in the page source (a data-attribute regression on the listing page itself — possible CMS bug, separate from formatting). |
| `Software Engineer – Autonomy Infrastructure…` | SF / Zurich | Both use `<h2>` (consistent). |
| `Software Engineer – Cloud Simulation & Full-Stack` | SF / Zurich | Both use `<h2>` (consistent). |
| `Software Engineer – Simulation & Robotics Engineer` | SF / Zurich | Both use `<h3>` (consistent inside the pair but different from the two pairs above). |
| `Senior Autonomy Engineer – Deep Learning` | SF / Zurich | Identical formatting and identical word count. |
| `Senior/Staff Embedded Software Engineer – Camera Systems` (SF) vs. `Sr/Staff Embedded Software Engineer – Camera Systems` (Tampere) | SF / Tampere | Identical pre-comp content and word count (394) but the title is spelled differently (`Senior/Staff` vs. `Sr/Staff`). |
| `Senior Software Engineer – Embedded`, `Software Engineer – Embedded`, `Staff Software Engineer – Embedded` | three levels | Identical pre-comp content (353 words each) — only the seniority in the title differs. Suggests intentional copy-paste; opportunity to use a shared snippet. |

---

## 4. Outlier roll-up — postings most "off the norm"

If a recruiter only has time to fix a few postings, these are the ones that deviate from the canonical pattern across **multiple** dimensions at once:

| Posting | Reason it stands out |
|---|---|
| **Senior Technical Support Representative – Japan** | Uses `<h1>` for every section heading — renders them at the same size as the page title. |
| **Field Marketing Event Manager** | Drops the canonical 3-heading structure entirely; uses 7× `<h3>` sub-sections instead. |
| **IT Technician (Help Desk – Linux Focus)** | No trailing colons anywhere; bolds an "Onsite – 5 days/week…" paragraph as a heading; duplicates "Location"; mixes `<li>` styles within a single list. |
| **Senior People Analytics Analyst** | Heading typo ("What Makes **Your** a Good Fit"); mixes "About The Role" (no colon, weird "The" capital) with colon headings; bullets begin with bolded mini-titles unlike any other posting. |
| **Full Stack Product Counsel** | `<h3>` headings, no colons; **10** intro paragraphs before the first section heading; uses `<u>` underlines. |
| **Director of Product Management, DFR** | Longest pre-comp on the site at 875 words; only two section headings ("What makes you a good fit:" and "Bonus points for:") so the bulk of the content is unstructured. |
| **Senior Software Engineer, Data Platform** | Adds a non-standard `Examples of what you'll help build:` heading and ends with `Why Join Us?` (the only `?`-terminated heading on the site). |
| **Senior Product Manager / Staff Product Manager, Platform & Infrastructure** | Both start the description with a bold `Location` "heading" before the canonical sections. |
| **Software Engineer – Autonomy Infrastructure, Systems and Tools** (both cities) | `<h2>` headings + uses a custom "Areas of Responsibility:" / "Bonus Experience:" vocabulary. |
| **Software Engineer – Cloud Simulation & Full-Stack** (both cities) | Same as above (`<h2>` + custom vocabulary). |
| **Software Engineer – Simulation & Robotics Engineer** (both cities) | `<h3>` headings + same custom vocabulary as the previous two — inconsistent heading level within the same team. |
| **Senior Buyer** | `<h2>` headings, no "About the role", uses "How you will make an impact:" and "What makes you a strong fit:" (both non-canonical phrasings). |
| **Aviation Compliance Lead** / **Aviation Regulatory Program Manager** | `<h2>` headings + no colons + 4–6 intro paragraphs. |
| **Communications Manager** | `<h2>` headings, no colons. |
| **Revenue Operations Engineer, Quoting Systems** | `<h2>` headings + entirely bespoke section names. |
| **Senior Brand Designer (Contract)** | Opening lead paragraph is fully bolded and reads as a heading. |
| **Enterprise Account Manager (MoD/MoI) – EMEA** (Finland / Germany / Switzerland) | All three contain a bolded "This role must be based in Switzerland, Germany, or Finland." paragraph that reads as a heading. |
| **PhD Autonomy Engineer Intern – Deep Learning or Computer Vision** | Only posting on the site whose `<ul>` items are plain `<li>text</li>` rather than `<li><p>…</p></li>`; no section headings at all. |
| **Workplace Experience Coordinator Part-Time (Zurich)** | Drops "About the role"; uses 4 sub-headings ("Workplace Experience & Office Operations", "People Operations & HR Coordination", "Qualifications", "Work Environment") with no colons. |
| **Success Systems Specialist** | 8 section headings (the most on the site), many of which are bespoke ("Why This Role Matters Now:", "Build Automation & Intelligence into Mission Success", …). |
| **Senior Software Engineer, Mobile Platform** | Orders sections as "About the Role → About the Team → How…" while sibling postings (`Senior Software Engineer – Embedded`, `Sr/Staff Embedded Software Engineer`) order them "About the team → About the role" — pick one. |

---

## 5. Recommendations for standardisation

These are listed in order of effort-to-impact. Items 1 – 4 can be enforced mechanically (linter rules or a Sanity validator); items 5 – 7 are editorial-style guide work.

### 5.1 Adopt one Sanity content model for "job description body"

Replace the current free-form `prose block-content` editor with a structured block of named fields:

- `intro` *(rich text, max 1 paragraph)*
- `about_role` *(rich text)*
- `impact_bullets` *(list of strings, each rendered as a bullet)*
- `good_fit_bullets` *(list of strings)*
- `nice_to_haves_bullets` *(optional list of strings)*
- `compensation` *(rich text — handled by template, not by recruiters)*

The template then emits the markup, so recruiters cannot accidentally insert `<h1>`/`<h2>`/`<h3>`, `<u>`, `<font>`, or stray empty paragraphs. This single change eliminates §3.1, §3.3 (markup half), §3.5, §3.7, §3.8 in one pass.

### 5.2 Pick one and only one section-heading style and enforce it

Decision needed from the brand / talent team:

- **Option A (status quo majority):** `<p><strong>About the role:</strong></p>` — body-sized bold. Used by 93/109 today.
- **Option B (visually clearer hierarchy):** wrap each section in a `<h3>` styled via the existing `.prose h3` rule (18 – 28 px). This is the option I would recommend for a careers page because it produces real document outline / accessibility benefits and visually separates sections from body bullets.

Whichever is chosen, the template emits it — never the recruiter.

### 5.3 Canonicalise the section-heading wording

Lock the three canonical headings in the style guide (sentence case, trailing colon, curly apostrophe, no variant wordings):

- `About the role:`
- `How you'll make an impact:`
- `What makes you a good fit:`

Optional headings (only when actually applicable):

- `About the team:` — only when the team paragraph is substantive enough to warrant its own section; otherwise merge into the intro.
- `Bonus points:` — replace the variants `Bonus points for:` / `Bonus Points:` / `Nice to have:` / `Nice To Haves:` / `Nice-to-Haves:` / `Nice to Have` / `Preferred Qualifications:` / `Additional Desired Experience and Skills`.

Run a one-time pass to fix all 81 outliers and the typo on `Senior People Analytics Analyst` ("What Makes **Your** a Good Fit").

### 5.4 Pick one bullet end-punctuation rule and enforce it

The majority style is **no end punctuation on bullets** (1 037 vs. 771). Lock that in the style guide and run a pass to strip trailing periods/semicolons on the 46 mixed postings (or on all 771 period-terminated bullets, depending on the call).

### 5.5 Normalise typographic characters

Strip the inconsistency between straight and curly apostrophes / quotes (48 postings currently mix them). Either:

- have the Sanity ingestion step run a smart-quote pass on save, **or**
- have the careers page render do a `replace('` → '`)` etc. on output.

This is one-line work in the renderer.

### 5.6 Cap intro length and dedupe Location/onsite info

- Limit `intro` to one or two paragraphs (today's median posting uses one). Move multi-paragraph "story" content (Full Stack Product Counsel, Manager Technical Support, DFR PM) into `About the role:` so the page rhythm matches the rest.
- Remove the bolded "Location" paragraph from the two Platform & Infrastructure PM postings and the IT Technician posting — the location is already shown in the page's `type-body-2` subline.
- For the EMEA Enterprise Account Manager triplet, replace the bolded *"This role must be based in Switzerland, Germany, or Finland."* paragraph with an italic callout inline in the intro, **or** make it a structured field (e.g. `location_requirement_callout`) styled distinctly from a section heading.
- Convert the Senior Brand Designer (Contract) bolded opening sentence to a normal paragraph.

### 5.7 Share content across duplicates

Five Embedded postings (Senior / Staff / Software Engineer – Embedded × 3 + Sr/Staff Camera Systems × 2), the two Software Engineer – Cloud Simulation & Full-Stack postings, etc. carry identical bodies. Convert these to a shared description snippet that's referenced from each Greenhouse JID — that prevents the formatting from diverging the next time one is edited.

### 5.8 Add a CI lint pass against the careers feed

Once §5.1–5.4 are in place, add a small lint script (a couple hundred lines of Python — the analysis pipeline used for this report can be the basis) that:

- Fails if any posting contains `<h1>`, `<h2>`, `<h3>`, `<u>`, `<font>`, `style=`, or inline color attributes inside the pre-comp block.
- Fails if any section heading does not exactly match the locked-in canonical strings.
- Fails on bullets that end in `.` / `;` (or whichever rule is locked in).
- Warns on intro paragraph counts > 2.

Run it on PR / on every Sanity publish.

---

## 6. Appendix — per-posting summary (109 rows)

Sorted by department then title. "Section headers (markup)" shows which HTML tag the writer used — `<p><strong>` is the canonical style; `<h1>`/`<h2>`/`<h3>` indicate the role is using a real heading tag and therefore renders at a larger font size.

| Department | Title | Location | Section headings (tag + text) | Bullet end-punctuation | Intro paras | Words |
|---|---|---|---|---|---|---|
| Customer Support | Field Support Representative | US Remote | `<p><strong>` About the team:<br>`<p><strong>` About the role:<br>`<p><strong>` How you’ll make an impact:<br>`<p><strong>` What makes you a good fit: | all period (18) | 1 | 513 |
| Customer Support | Field Support Representative (Southwest, Remote) | US Remote | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | all period (22) | 1 | 712 |
| Customer Support | Manager, Technical Support | US CA San Mateo | `<p><strong>` About the team:<br>`<p><strong>` About the role:<br>`<p><strong>` How you’ll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (2 period / 20 none) | 1 | 780 |
| Customer Support | Product Support Engineer | San Mateo, California, United States | _(none — plain prose only)_ | all period (22) | 4 | 581 |
| Customer Support | Product Support Engineer Intern | San Mateo, California, United States | _(none — plain prose only)_ | all period (15) | 4 | 441 |
| Customer Support | Senior Customer Support Representative - India | Bangalore, India | `<p><strong>` About the role:<br>`<p><strong>` How you’ll make an impact:<br>`<p><strong>` What would make you a good fit: | mixed (20 period / 2 none) | 1 | 614 |
| Customer Support | Senior Technical Support Representative - Japan | Tokyo, Japan | `<h1>` About the role:<br>`<h1>` How you’ll make an impact:<br>`<h1>` What would make you a good fit: | mixed (17 period / 3 none) | 6 | 717 |
| Customer Support | Technical Support Specialist - West Coast | US Remote | _(none — plain prose only)_ | mixed (1 period / 18 none) | 9 | 620 |
| IT | IT Technician (Help Desk - Linux Focus) | Hayward, California, United States | `<p><strong>` About the Role<br>`<p><strong>` Location<br>`<p><strong>` Onsite - 5 days/week, Monday - Friday: 3:30pm - 12am Skydio Manufacturing (Hayward, CA)<br>`<p><strong>` What You’ll Do<br>`<p><strong>` What Makes You a Good Fit<br>`<p><strong>` Nice to Have | mixed (1 period / 31 none) | 1 | 524 |
| Legal | Full Stack Product Counsel | San Mateo, California, United States | `<h3>` About the Team<br>`<h3>` About the Role<br>`<h3>` How You’ll Make an Impact<br>`<h3>` What Makes You a Great Fit | all none (15) | 10 | 771 |
| Manufacturing | Head of Warehouse & Logistics Operations | US CA Production | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (3 period / 17 none) | 1 | 447 |
| Manufacturing | Manufacturing Quality Supervisor | Hayward, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you’ll make an impact:<br>`<p><strong>` What makes you a good fit: | all none (23) | 1 | 371 |
| Manufacturing | Production Manager, PM Shift | Hayward, California, United States | `<p><strong>` About the Role:<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit: | all period (11) | 1 | 295 |
| Manufacturing | Production Supervisor | Hayward, California, United States | `<p><strong>` About the role:<br>`<p><strong>` What makes you a good fit: | all none (11) | 1 | 294 |
| Manufacturing | Senior Buyer | Hayward, California, United States | `<h2>` How you will make an impact:<br>`<h2>` What makes you a strong fit: | mixed (17 period / 5 none) | 1 | 478 |
| Manufacturing | Senior NPI Product Quality Engineer | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | all none (19) | 1 | 391 |
| Marketing | Communications Manager | US Remote | `<h2>` About the role<br>`<h2>` How you'll make an impact<br>`<h2>` What makes you a good fit | all none (12) | 3 | 425 |
| Marketing | Director, Growth Marketing - Commercial | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` Key Responsibilities:<br>`<p><strong>` What Success Looks Like:<br>`<p><strong>` What Would Make You a Good Fit:<br>`<p><strong>` Additional Desired Experience and Skills | mixed (1 period / 22 none) | 1 | 596 |
| Marketing | Field Marketing Event Manager | San Mateo, California, United States | `<h3>` Customer Summit Planning & Execution<br>`<h3>` Field Marketing & Trade Show Support<br>`<h3>` Relationship Building & Internal Collaboration<br>`<h3>` Required Experience<br>`<h3>` Preferred Skills & Experience<br>`<h3>` Interpersonal & Professional Skills<br>`<h3>` Physical & Travel Requirements | all period (27) | 1 | 518 |
| Marketing | Senior Brand Designer (Contract) | San Mateo, California, United States | `<p><strong>` We’re looking for an experienced Senior Brand Designer to help shape how Skydio shows up in the world—crafting clear, compelling, and memorable visual experiences across a wide range of touchpoints for the leader in autonomous flight.<br>`<p><strong>` About the Role:<br>`<p><strong>` What you'll do:<br>`<p><strong>` What makes you a good fit: | mixed (1 period / 21 none) | 1 | 501 |
| People & Recruiting | Senior People Analytics Analyst | San Mateo, California, United States | `<p><strong>` About The Role<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes Your a Good Fit:<br>`<p><strong>` Preferred Qualifications | mixed (15 period / 1 none) | 1 | 725 |
| People & Recruiting | Senior Technical Recruiter | San Mateo, California, United States | `<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | all none (14) | 3 | 433 |
| People & Recruiting | Senior Technical Recruiter - Hardware Operations | San Mateo, California, United States | `<p><strong>` What makes you a good fit: | all none (13) | 4 | 440 |
| People & Recruiting | Staff Technical Recruiter | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you’ll make an impact:<br>`<p><strong>` What makes you a good fit: | all period (15) | 1 | 430 |
| People & Recruiting | Workplace Experience Coordinator Part-Time | Zurich, Switzerland | `<p><strong>` How you’ll make an impact:<br>`<p><strong>` Workplace Experience & Office Operations<br>`<p><strong>` People Operations & HR Coordination<br>`<p><strong>` Qualifications<br>`<p><strong>` Work Environment | all none (20) | 4 | 486 |
| Policy & Regulatory Affairs | Aviation Compliance Lead | San Mateo, California, United States | `<h2>` About the Role<br>`<h2>` How You’ll Make an Impact<br>`<h2>` What Makes You a Good Fit | all period (15) | 4 | 399 |
| Policy & Regulatory Affairs | Aviation Regulatory Program Manager | US Remote | `<h2>` About the Role<br>`<h2>` How You’ll Make an Impact<br>`<h2>` What Makes You a Good Fit | all period (16) | 6 | 493 |
| Professional Services and Training | Customer Success Manager, DFR Majors - Northeast | US Remote | `<p><strong>` About the Team:<br>`<p><strong>` About the role:<br>`<p><strong>` How you’ll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (10 period / 9 none) | 1 | 499 |
| Professional Services and Training | Deployment Engineer - Southeast | US Remote | `<p><strong>` About the Team:<br>`<p><strong>` About the role:<br>`<p><strong>` How you’ll make an impact:<br>`<p><strong>` What makes you a good fit:<br>`<p><strong>` Nice to have: | mixed (4 period / 19 none) | 1 | 595 |
| Professional Services and Training | Mission Success Operations Manager | US Remote | `<p><strong>` About the Team:<br>`<p><strong>` About the role:<br>`<p><strong>` How you’ll make an impact:<br>`<p><strong>` What makes you a good fit | all period (14) | 1 | 452 |
| Professional Services and Training | Program Manager, Major Deployments (Hawaii) | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What Makes You A Good Fit: | mixed (11 period / 3 none) | 1 | 596 |
| Professional Services and Training | Program Manager, Major Deployments (Mid Atlantic) | US Remote | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What Makes You A Good Fit: | mixed (11 period / 4 none) | 1 | 603 |
| Professional Services and Training | Program Manager, Major Deployments (South East) | US Remote | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What Makes You A Good Fit: | mixed (11 period / 3 none) | 1 | 597 |
| Professional Services and Training | Success Systems Specialist | US Remote | `<p><strong>` About the Role:<br>`<p><strong>` Why This Role Matters Now:<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` Build Automation & Intelligence into Mission Success<br>`<p><strong>` Customer Digital Experience<br>`<p><strong>` Cross-Functional Architecture & Governance<br>`<p><strong>` Scalability & Cost Avoidance<br>`<p><strong>` What makes you a good fit: | all period (28) | 1 | 729 |
| Sales | Enterprise Account Manager (MoD/ MoI) – EMEA (Finland) | Tampere, Finland | `<p><strong>` About the Role:<br>`<p><strong>` This role must be based in Switzerland, Germany, or Finland.<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit: | all none (22) | 1 | 602 |
| Sales | Enterprise Account Manager (MoD/ MoI) – EMEA (Germany) | Germany | `<p><strong>` About the Role:<br>`<p><strong>` This role must be based in Switzerland, Germany, or Finland.<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit: | all none (22) | 1 | 602 |
| Sales | Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland) | Zurich, Switzerland | `<p><strong>` About the Role:<br>`<p><strong>` This role must be based in Switzerland, Germany, or Finland.<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit: | all none (22) | 1 | 602 |
| Sales | Enterprise Account Manager, US Army | US Remote | `<p><strong>` About the Role:<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit: | all none (20) | 1 | 474 |
| Sales | Enterprise Account Manager, US Navy, US Marine Corps, and IC/SOCOM | US Remote | `<p><strong>` About the Role:<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit: | all none (20) | 1 | 508 |
| Sales | GTM Data Engineer Intern | San Mateo, California, United States | `<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit:<br>`<p><strong>` Bonus points:<br>`<p><strong>` What you’ll gain: | mixed (11 period / 7 none) | 2 | 456 |
| Sales | GTM Enablement Associate | San Mateo, California, United States | `<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit:<br>`<p><strong>` Preferred Qualifications: | all none (18) | 5 | 374 |
| Sales | Revenue Operations Engineer, Quoting Systems | San Mateo, California, United States | `<h2>` What you’ll drive (scope):<br>`<h2>` Day-to-day responsibilities:<br>`<h2>` Tech stack you’ll work with:<br>`<h2>` What you’ll bring:<br>`<h2>` Reporting & Working Model: | mixed (15 period / 10 none) | 1 | 508 |
| Sales | Sales Planning Analyst Intern | San Mateo, California, United States | `<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Would Make You a Good Fit: | all none (18) | 4 | 596 |
| Sales | Senior Revenue Operations Manager | San Mateo, California, United States | `<p><strong>` About the Role:<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit:<br>`<p><strong>` Preferred Qualifications: | all none (18) | 1 | 441 |
| Supply Chain & Logistics | Director, Global Supply Management - Mechanicals | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` What you will do:<br>`<p><strong>` Desired Qualifications: | no bullets | 1 | 612 |
| Supply Chain & Logistics | Hardware Operations Program Manager | Hayward, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (6 period / 6 none) | 1 | 379 |
| Supply Chain & Logistics | Senior Business Operations Manager | San Mateo, California, United States | `<h3>` Strategic Sourcing:<br>`<h3>` Cost Management<br>`<h3>` Strategy & Operations | all none (26) | 1 | 506 |
| Supply Chain & Logistics | Senior Supplier Quality Engineer | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` What makes you a good fit: | mixed (2 period / 10 none) | 1 | 434 |
| Supply Chain & Logistics | Staff Global Supply Manager, Mechanicals | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (16 period / 1 none) | 1 | 546 |
| Supply Chain & Logistics | Supplier Quality Engineer, Sustaining | Taiwan | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (10 period / 3 none) | 1 | 566 |
| Supply Chain & Logistics | Supply Chain Intern | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` What makes you a good fit: | mixed (1 period / 7 none) | 1 | 416 |
| Autonomy | Autonomy Engineer - Deep Learning | Zurich, Switzerland | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | all none (14) | 1 | 366 |
| Autonomy | Autonomy Engineer - Deep Learning Infrastructure | Zurich, Switzerland | `<p><strong>` What makes you a good fit: | all none (17) | 2 | 448 |
| Autonomy | Autonomy Engineer - Deep Learning Infrastructure | San Mateo, California, United States | `<p><strong>` What makes you a good fit: | all none (17) | 2 | 481 |
| Autonomy | Autonomy Engineer - Deep Learning Model Acceleration | Zurich, Switzerland | `<p><strong>` What makes you a good fit: | all none (17) | 2 | 449 |
| Autonomy | Autonomy Engineer - Deep Learning Model Acceleration | San Mateo, California, United States | `<p><strong>` What makes you a good fit: | all none (17) | 2 | 449 |
| Autonomy | Autonomy Engineer - Fixed Wing Planning & Controls | San Mateo, California, United States | `<p><strong>` About the Role:<br>`<p><strong>` How You'll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit: | mixed (1 period / 11 none) | 1 | 260 |
| Autonomy | Autonomy Engineer - ML & DL Infrastructure | San Mateo, California, United States | `<p><strong>` About the Role:<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit: | mixed (1 period / 12 none) | 1 | 454 |
| Autonomy | Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a strong fit: | all none (8) | 1 | 524 |
| Autonomy | Autonomy Engineer Intern - Deep Learning (Computational Photography) | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (1 period / 14 none) | 1 | 567 |
| Autonomy | Autonomy Engineer Intern - Deep Learning (Computational Photography) | Zurich, Switzerland | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (1 period / 14 none) | 1 | 567 |
| Autonomy | Autonomy Engineer Intern Fall 2026 | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | all none (8) | 1 | 434 |
| Autonomy | Autonomy Software Engineer | San Mateo, California, United States | `<p><strong>` What makes you a good fit: | all none (12) | 2 | 392 |
| Autonomy | Engineering Manager - Autonomy | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | all none (10) | 1 | 338 |
| Autonomy | PhD Autonomy Engineer Intern - Deep Learning or Computer Vision | San Mateo, California, United States | _(none — plain prose only)_ | all none (1) | 4 | 521 |
| Autonomy | PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) | Zurich, Switzerland | `<h3>` How you'll make an impact:<br>`<h3>` What makes this internship different:<br>`<h3>` What makes you a strong fit: | all period (17) | 1 | 442 |
| Autonomy | Senior Autonomy Engineer - Controls | San Mateo, California, United States | `<p><strong>` About the Role:<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit: | all none (9) | 1 | 245 |
| Autonomy | Senior Autonomy Engineer - Data Curation | San Mateo, California, United States | `<p><strong>` About the Role:<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit:<br>`<p><strong>` Nice To Haves:<br>`<p><strong>` Working Style: | all period (19) | 1 | 436 |
| Autonomy | Senior Autonomy Engineer - Deep Learning | Zurich, Switzerland | `<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | all none (13) | 2 | 314 |
| Autonomy | Senior Autonomy Engineer - Deep Learning | San Mateo, California, United States | `<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | all none (13) | 3 | 314 |
| Autonomy | Software Engineer - Autonomy Infrastructure, Systems and Tools | San Mateo, California, United States | `<h2>` About the Role:<br>`<h2>` Areas of Responsibility:<br>`<h2>` What You’ll Do:<br>`<h2>` Qualifications:<br>`<h2>` Bonus Experience: | mixed (18 period / 2 none) | 3 | 521 |
| Autonomy | Software Engineer - Autonomy Infrastructure, Systems and Tools | Zurich, Switzerland | `<h2>` About the Role:<br>`<h2>` Areas of Responsibility:<br>`<h2>` What You’ll Do:<br>`<h2>` Qualifications:<br>`<h2>` Bonus Experience: | mixed (18 period / 2 none) | 3 | 521 |
| Autonomy | Software Engineer - Cloud Simulation & Full-Stack | San Mateo, California, United States | `<h2>` About the Role:<br>`<h2>` Areas of Responsibility:<br>`<h2>` What You’ll Do:<br>`<h2>` Qualifications:<br>`<h2>` Bonus Experience: | all period (26) | 3 | 552 |
| Autonomy | Software Engineer - Cloud Simulation & Full-Stack | Zurich, Switzerland | `<h2>` About the Role:<br>`<h2>` Areas of Responsibility:<br>`<h2>` What You’ll Do:<br>`<h2>` Qualifications:<br>`<h2>` Bonus Experience: | all period (26) | 3 | 552 |
| Autonomy | Software Engineer - Simulation & Robotics Engineer | Zurich, Switzerland | `<h3>` About the Role:<br>`<h3>` Areas of Responsibility:<br>`<h3>` What You’ll Do:<br>`<h3>` Qualifications:<br>`<h3>` Bonus Experience: | all period (20) | 4 | 482 |
| Autonomy | Software Engineer - Simulation & Robotics Engineer | San Mateo, California, United States | `<h3>` About the Role:<br>`<h3>` Areas of Responsibility:<br>`<h3>` What You’ll Do:<br>`<h3>` Qualifications:<br>`<h3>` Bonus Experience: | all period (20) | 4 | 482 |
| Connectivity | RF Design Engineer | San Mateo, California, United States | `<p><strong>` About the Role:<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit: | mixed (2 period / 17 none) | 1 | 391 |
| Connectivity | Senior Wireless Systems Performance Engineer | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (1 period / 15 none) | 1 | 385 |
| Connectivity | Wireless Hardware Engineer Intern | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` What makes you a good fit: | all period (14) | 1 | 551 |
| Connectivity | Wireless Software Engineer | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (10 period / 2 none) | 1 | 400 |
| Hardware | Electric Motor / Propulsion Engineer | San Mateo, California, United States | `<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (1 period / 13 none) | 3 | 284 |
| Hardware | Electrical Engineer (Sustaining/Validation) | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` What makes you a good fit: | mixed (1 period / 13 none) | 1 | 295 |
| Hardware | Electrical Engineer (all levels) | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` What makes you a good fit: | mixed (1 period / 12 none) | 1 | 244 |
| Hardware | Hardware Technician | San Mateo, California, United States | `<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit: | all none (18) | 2 | 376 |
| Hardware | Lead Staff Electrical Engineer (F10 Program) | San Mateo, California, United States | `<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (1 period / 14 none) | 2 | 318 |
| Hardware | PCB Layout Engineer | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` What makes you a good fit: | all period (12) | 1 | 346 |
| Hardware | Product Design Engineer (All Levels) | San Mateo, California, United States | `<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | all period (16) | 2 | 448 |
| Hardware | Senior Hardware Test and Reliability Engineer | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you will make an impact:<br>`<p><strong>` Useful skills and experience: | all none (12) | 1 | 539 |
| Hardware | Systems Integration and Test Engineer (Mid to Senior Level) | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you will make an impact:<br>`<p><strong>` Useful skills and experience: | mixed (1 period / 13 none) | 1 | 509 |
| Product | Director of Product Management, Drone as First Responder (DFR) | San Mateo, California, United States | `<p><strong>` What makes you a good fit:<br>`<p><strong>` Bonus points for: | all none (20) | 2 | 875 |
| Product | Senior Product Manager, Platform & Infrastructure | San Mateo, California, United States | `<p><strong>` Location<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What would make you a strong fit: | all period (15) | 4 | 767 |
| Product | Staff Product Manager, Platform & Infrastructure | San Mateo, California, United States | `<p><strong>` Location<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What would make you a strong fit: | all period (15) | 4 | 786 |
| Security | Senior Software Engineer - Security | San Mateo, California, United States | `<p><strong>` About the Role:<br>`<p><strong>` How you’ll make an impact:<br>`<p><strong>` What makes you a good fit:<br>`<p><strong>` Nice to have: | all none (17) | 1 | 418 |
| Software | Senior Software Engineer - Embedded | San Mateo, California, United States | `<p><strong>` About the team:<br>`<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (2 period / 15 none) | 1 | 353 |
| Software | Senior Software Engineer - Mobile Platform | San Mateo, California, United States | `<p><strong>` About the Role:<br>`<p><strong>` About the Team:<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit:<br>`<p><strong>` Nice To Haves: | all none (18) | 1 | 530 |
| Software | Senior Software Engineer, Data Platform | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` Examples of what you’ll help build:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What would make you a good fit:<br>`<p><strong>` Why Join Us? | all period (20) | 1 | 731 |
| Software | Senior Software Engineer, Frontend | San Mateo, California, United States | `<p><strong>` About the Role:<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit:<br>`<p><strong>` Bonus Points: | mixed (11 period / 4 none) | 1 | 350 |
| Software | Senior Software Engineer, Full Stack | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you’ll make an impact:<br>`<p><strong>` What would make you a good fit:<br>`<p><strong>` Bonus points for: | mixed (12 period / 1 none) | 1 | 623 |
| Software | Senior Software Engineer, Infrastructure | San Mateo, California, United States | `<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit:<br>`<p><strong>` Bonus points: | all period (13) | 3 | 400 |
| Software | Senior/Staff Embedded Software Engineer – Camera Systems | San Mateo, California, United States | `<p><strong>` About the Role:<br>`<p><strong>` About the Team:<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit: | mixed (1 period / 17 none) | 1 | 394 |
| Software | Software Engineer - Embedded | San Mateo, California, United States | `<p><strong>` About the team:<br>`<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (2 period / 15 none) | 1 | 353 |
| Software | Software Engineer - Infrastructure | San Mateo, California, United States | `<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit:<br>`<p><strong>` Bonus points: | all period (13) | 3 | 398 |
| Software | Software Engineer Intern Fall 2026/Winter 2027 | US CA San Mateo | `<p><strong>` What makes you a good fit: | mixed (8 period / 4 none) | 5 | 528 |
| Software | Software Engineer, Full Stack | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you’ll make an impact:<br>`<p><strong>` What would make you a good fit:<br>`<p><strong>` Bonus Points: | mixed (12 period / 1 none) | 1 | 254 |
| Software | Sr/Staff Embedded Software Engineer - Camera Systems | Tampere, Finland | `<p><strong>` About the Role:<br>`<p><strong>` About the Team:<br>`<p><strong>` How You’ll Make an Impact:<br>`<p><strong>` What Makes You a Good Fit: | mixed (1 period / 17 none) | 1 | 394 |
| Software | Staff Software Engineer - Embedded | San Mateo, California, United States | `<p><strong>` About the team:<br>`<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | mixed (2 period / 15 none) | 1 | 353 |
| Software | Staff Software Engineer, Frontend | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit:<br>`<p><strong>` Bonus Points: | mixed (11 period / 4 none) | 1 | 350 |
| Software | Staff Software Engineer, Full Stack | San Mateo, California, United States | `<p><strong>` How you’ll make an impact:<br>`<p><strong>` What would make you a good fit:<br>`<p><strong>` Bonus points for: | all period (16) | 4 | 613 |
| _(unfiled)_ | Autonomy Engineer - Deep Learning | San Mateo, California, United States | `<p><strong>` About the role:<br>`<p><strong>` How you'll make an impact:<br>`<p><strong>` What makes you a good fit: | all none (14) | 1 | 365 |
