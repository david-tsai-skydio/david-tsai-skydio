# Skydio Careers — Job-Posting Formatting Audit

**Source:** [https://www.skydio.com/careers](https://www.skydio.com/careers)
**Postings audited:** 111 (every live posting on the page)
**Scope:** The visible content of each posting from the page title through to — **but not including** — the `Compensation:` block. Everything after `Compensation:` (salary band, benefits, EEO language, etc.) was intentionally ignored, per the request.
**Date of capture:** 2026-05-16

> The Skydio careers site is built on Astro with a Sanity CMS back-end. Job-description bodies are rendered into a single shared wrapper (`<div class="prose block-content">`) whose CSS controls all *typography*: font family, font sizes, line-height, colors, weights, and alignment. Because the CSS is shared, **no posting actually uses a different pixel size, font family, or color** — but the *semantic HTML each posting authors* is wildly inconsistent, and that HTML directly drives the visible heading hierarchy, vertical rhythm, bolding, and line spacing the reader sees. This report focuses on those authored differences, because they are the only thing recruiters/hiring managers can fix in the CMS.

---

## 1. Executive summary

| Dimension | Norm (≈80% of postings) | Outliers | Severity |
|---|---|---|---|
| Section-heading **tag** | `<p><strong>Label:</strong></p>` (fake heading) — 92 / 111 | 7 use `<h2>`, 3 use `<h3>`, **1 uses `<h1>`**, 5 use a *mix* of real headings + bold paragraphs, 3 have **no section headings at all** | High |
| Section-heading **label text** | `About the role:` / `How you'll make an impact:` / `What makes you a good fit:` | 16+ casing/wording variants, **1 typo** (`What Makes Your a Good Fit`), multiple bespoke labels (e.g. `Key Responsibilities`, `What Success Looks Like`, `Working Style`) | High |
| Section-heading **trailing colon** | Colon at the end (88 / 111) | 8 postings mix colon and no-colon within the same posting; 1 has none at all | Low–Medium |
| Apostrophe character | Straight `'` (34) **vs** curly `’` (35) — basically a coin-flip | 2 postings mix both characters *within the same posting* | Low |
| Bullet-list trailing **punctuation** | Inconsistent across the site (25 all-period, 36 no-period) | **49 / 111 postings (44%) mix the two styles inside the same bullet list** | Medium |
| Use of `<br>` inside the body | Most postings use only `<p>` and `<ul>` (64 / 111) | **47 postings emit raw `<br>` tags**, 20 of those stack `<br><br>` to fake vertical spacing | Medium |
| Empty paragraphs (`<p></p>`) used as spacers | None expected | **53 postings contain one or more empty `<p>` tags** (up to 8 in a single posting) — produces uneven blank gaps | Medium |
| Italic (`<em>`) / underline (`<u>`) | None expected | 9 postings use `<em>` or `<u>` — most underline body text, which on the web reads as a broken hyperlink | Medium |
| Inline `style="…"` attribute | None expected | 1 posting (Manager, Logistics) leaks a Word/Docs paste with `style="min-height:1.2em;margin-top:0;margin-bottom:0"` | Low |
| Job-title double spaces | None | **4 titles have a `,␣␣` double space** that renders as a wider gap | Low |
| Intro paragraph (the “Skydio is the leading US drone company…” boilerplate) | Present, identical wording | All 111 postings match — this is the one place the site is fully consistent | ✅ |
| Word count of pre-comp body | ~470 words (median) | Range **229 → 786 words** (3.4×) — primarily a content choice, but very short bodies look visually thin next to long ones on the same listing page | Informational |

**Bottom line:** the careers site’s *CSS* is consistent, but the *authored HTML* is not. The visible inconsistencies a reader sees — different heading sizes, mismatched section labels, uneven blank gaps between paragraphs, underlined or italicized words, mixed punctuation in bullet lists — all come from CMS authors using different building blocks. Standardising on a single template will fix every issue in §3 without touching engineering.

---

## 2. How each posting is built (technical baseline)

Every posting page on www.skydio.com renders the pre-compensation block inside the same DOM:

```html
<h1 class="type-h2">{Job title}</h1>
<p class="type-body-2"> {City, Country} - {Employment type} </p>
<div class="prose block-content">
  …authored body HTML…
</div>
```

This means:

- **Font family, base font-size, color, line-height, and alignment are identical across all 111 postings** — they are governed by `.prose.block-content` and its child selectors in the site stylesheet, not by anything inside the post body.
- The *page title* (`<h1>`) is styled by `.type-h2` and the *location line* by `.type-body-2`. Those two never vary.
- All visible variation in the body is therefore a function of **which HTML tags the author chose** inside the `prose` container. The CSS for `.prose` styles `<h2>`, `<h3>`, `<p>`, `<strong>`, `<ul>/<li>` differently — so swapping a `<p><strong>` for an `<h2>` *does* visibly enlarge and add space around that line. That is the mechanism behind nearly every issue called out below.

---

## 3. Formatting issues — observations, examples, and recommendations

### 3.1 Section-heading hierarchy is completely inconsistent (highest impact)

There are five different ways postings render the “About the role / How you’ll make an impact / What makes you a good fit” section labels:

| Pattern | # of postings | What it looks like to the reader |
|---|---:|---|
| `<p><strong>Label:</strong></p>` (bold paragraph) | **92** | Same font size as body text, just bold. No extra space above the label. |
| `<h2>Label</h2>` (real heading) | 7 | **Markedly larger** font (≈ same size as the job title), with extra top/bottom margin. |
| `<h2>` + `<p><strong>` mixed in the same posting | 2 | First section is a large heading, later sections are bold paragraphs — visibly broken hierarchy. |
| `<h3>` only | 3 | Slightly larger than body text, with extra margin. |
| `<h3>` + `<p><strong>` mixed | 3 | Same broken-hierarchy problem as above. |
| `<h1>` (!) | **1** | Renders at the same scale as the page title itself. |
| No section headings at all | 3 | The whole role description is a wall of paragraphs. |

**Specific outliers to fix first**

- **`<h1>` outlier (renders at job-title size inside the body):**
  - *Senior Technical Support Representative — Japan* (Tokyo, Japan) — uses `<h1>About the role:</h1>`, `<h1>How you’ll make an impact:</h1>`, `<h1>What would make you a good fit:</h1>`.

- **`<h2>`-only postings (visually bigger headings than the rest of the site):**
  - Software Engineer — Autonomy Infrastructure, Systems and Tools (San Mateo & Zurich, 2 postings)
  - Software Engineer — Cloud Simulation & Full-Stack (San Mateo & Zurich, 2 postings)
  - Communications Manager (US Remote)
  - Aviation Compliance Lead (San Mateo)
  - Aviation Regulatory Program Manager (US Remote)

- **`<h3>` (and `<h3>` + bold-paragraph mixed) postings:**
  - PhD Autonomy Engineer Intern — Planning & Controls (Reinforcement Learning), Zurich
  - Software Engineer — Simulation & Robotics Engineer (San Mateo & Zurich)
  - Full Stack Product Counsel (San Mateo)
  - Field Marketing Event Manager (San Mateo)
  - Senior Business Operations Manager (San Mateo)

- **Mixed real-heading + bold-paragraph within the same posting (broken hierarchy):**
  - Senior Buyer (Hayward)
  - Revenue Operations Engineer, Quoting Systems (San Mateo)

- **No section headings at all (wall of text):**
  - Product Support Engineer (San Mateo)
  - Product Support Engineer Intern (San Mateo)
  - Technical Support Specialist — West Coast (US Remote)

**Recommendation:** pick one tag — recommended `<h2>` (semantic, accessible, screen-reader friendly) — and use it everywhere. Update the CMS template / rich-text style guide and apply the same heading tag to every posting. Remove the lone `<h1>` immediately, as it duplicates the role title’s visual weight.

---

### 3.2 Section-heading labels: 16 wording / casing variants for what should be 3 labels

What the writer types is also inconsistent. The same three “canonical” section labels appear in this many shapes (counts include all postings that use that exact string):

| Label as authored | Count |
|---|---:|
| `About the role` | 49 |
| `About the Role` | 23 |
| `About The Role` | 1 |
| `About the team` | 5 |
| `About the Team` | 6 |
| `How you'll make an impact` (straight apostrophe) | 34 |
| `How you’ll make an impact` (curly apostrophe) | 13 |
| `How You’ll Make an Impact` | 20 |
| `How You'll Make an Impact` | 1 |
| `How you will make an impact` | 3 |
| `What makes you a good fit` | 56 |
| `What Makes You a Good Fit` | 19 |
| `What Makes You A Good Fit` | 3 |
| `What Makes Your a Good Fit` | **1 (typo — “Your” instead of “You”)** |
| `What would make you a good fit` | 5 |
| `What makes you a strong fit` / `What would make you a strong fit` | 4 (combined) |
| `What Would Make You a Good Fit` | 2 |

Plus a long tail of bespoke labels used by single postings: `Key Responsibilities`, `What You’ll Do`, `What you'll do`, `What Success Looks Like`, `Working Style`, `Examples of what you'll help build`, `Why Join Us?`, `Preferred Qualifications`, `Bonus points`, `Bonus Points`, `Bonus points for`, `Nice to have`, `Nice To Haves`, `Nice-to-Haves`, `Additional Desired Experience and Skills`, `Useful skills and experience`, `Workplace Experience & Office Operations`, `People Operations & HR Coordination`, etc.

**Notable callouts**

- **Typo to fix immediately:** *Senior People Analytics Analyst* (San Mateo) has the heading `What Makes Your a Good Fit`.
- **A “heading” that is actually a sentence:** *Workplace Experience Coordinator Part-Time* (Zurich) styles the line `This role must be based in Switzerland, Germany, or Finland.` as a bold paragraph (i.e., the template’s heading slot). It reads like a heading but is body content.
- **A “heading” that is the whole intro paragraph:** *Senior Brand Designer (Contract)* puts its entire opening sentence (`We’re looking for an experienced Senior Brand Designer…`) inside `<p><strong>…</strong></p>`. The bold pulls the eye in a way no other posting does.

**Recommendation:** Standardise to exactly three required section headings, sentence-case, straight apostrophe, no trailing colon (the colon is redundant when a heading style is used). Suggested canonical wording:

1. **About the role**
2. **How you’ll make an impact**
3. **What makes you a good fit**

Reserve `Bonus points`, `Nice to have`, `Preferred qualifications`, etc. for an optional fourth section and write *one* approved label for each.

---

### 3.3 Trailing colon on section labels

- 88 postings: `Label:` (with colon)
- 1 posting: `Label` (no colon at all)
- **8 postings mix colon and no-colon in the same job description** — visually obvious because one section heading looks complete and the next looks truncated.

**Recommendation:** pick one (recommended: *no* colon, because the heading style already signals the role of the line). Apply consistently.

---

### 3.4 Straight vs. curly apostrophe in headings (`'` vs `’`)

| Apostrophe style in section headings | # of postings |
|---|---:|
| Straight `'` only | 34 |
| Curly `’` only | 35 |
| **Both styles in the same posting** | 2 |

This is the kind of inconsistency a reader will not consciously notice but a designer will. The two characters render with slightly different widths and weights in the site’s body font.

**Recommendation:** enable “smart quotes” in the CMS editor (curly `’`) and convert all existing postings in one batch find-and-replace.

---

### 3.5 Bullet-list trailing punctuation

| Pattern of bullet endings within a posting | # of postings |
|---|---:|
| All bullets end with a period | 25 |
| No bullets end with a period | 36 |
| **Bullets mix period / no-period in the same list** | **49** |

Almost half of all postings have visibly inconsistent bullets — i.e. some lines end with `.` and the very next line does not. This is the single most common *visible* defect in the body copy.

**Recommendation:** writing style — pick one and add it to the editorial guide. Recommended: **no period** when bullets are fragments (the dominant Skydio voice), period when bullets are complete sentences. Then sweep all 49 mixed postings.

---

### 3.6 Vertical rhythm: `<br>` tags and empty `<p></p>` paragraphs

The shared CSS already gives paragraphs and list items a consistent top/bottom margin. When authors insert `<br>` tags — and especially `<br><br>` stacks — to “add a blank line”, the spacing no longer matches the rest of the site and the cadence visibly differs between postings.

- **47 / 111 postings (42%)** contain at least one `<br>` inside the pre-compensation body.
- **20 / 47** of those stack two or more `<br>` tags in a row to fake a paragraph break. Examples:

  - Autonomy Engineer — Deep Learning Infrastructure (Zurich & San Mateo)
  - Autonomy Engineer — Deep Learning Model Acceleration (Zurich & San Mateo)
  - Autonomy Software Engineer (San Mateo)
  - Senior Autonomy Engineer — Deep Learning (San Mateo & Zurich)
  - Director of Product Management, DFR (San Mateo)
  - IT Technician (Help Desk — Linux Focus) (Hayward) — **8 `<br>` tags**
  - Director, Growth Marketing — Commercial (San Mateo) — **8 `<br>` tags**
  - Senior Technical Support Representative — Japan (Tokyo)
  - Software Engineer Intern Fall 2026/Winter 2027 (US CA San Mateo)
  - PCB Layout Engineer, Electrical Engineer (all levels), Wireless Hardware Engineer Intern (all San Mateo)
  - Production Supervisor, Senior Buyer (Hayward)
  - Senior Supplier Quality Engineer, Senior Brand Designer, Supply Chain Intern (San Mateo)
  - Enterprise Account Manager (MoD/MoI) — EMEA (Finland, Germany, Switzerland) — all 3 postings.

- **53 / 111 postings** contain one or more *empty* `<p></p>` paragraphs (literal blank paragraphs the CMS still pushes through). Worst offenders:

  - Full Stack Product Counsel (San Mateo) — 8 empty paragraphs
  - Senior Product Manager, Platform & Infrastructure (San Mateo) — 6
  - Staff Product Manager, Platform & Infrastructure (San Mateo) — 6
  - Deployment Engineer — Southeast (US Remote) — 5
  - Senior/Staff Embedded Software Engineer – Camera Systems (San Mateo) — 4
  - Sr/Staff Embedded Software Engineer - Camera Systems (Tampere) — 4
  - Director of Product Management, DFR (San Mateo) — 4
  - Senior Autonomy Engineer — Data Curation (San Mateo) — 4

The visible symptom: side by side, two postings will have noticeably different vertical white space between the intro paragraph and the first section heading.

**Recommendation:** add a CMS pre-publish lint that strips empty paragraphs and converts inline `<br>` tags to real paragraph breaks. Run it once over the back-catalog. Going forward, train authors to press *Enter* (new paragraph) rather than *Shift-Enter* (line break).

---

### 3.7 Use of italic (`<em>`) and underline (`<u>`)

The site’s body style does not use italics or underlines anywhere else. Underlined body text is especially problematic because users associate underlines with hyperlinks.

| Posting | `<em>` | `<u>` |
|---|:-:|:-:|
| Electric Motor / Propulsion Engineer (San Mateo) | ✅ | – |
| Lead Staff Electrical Engineer (F10 Program) (San Mateo) | – | ✅ |
| Senior Software Engineer, Full Stack (San Mateo) | – | ✅ |
| Full Stack Product Counsel (San Mateo) | – | ✅ |
| Senior NPI Product Quality Engineer (San Mateo) | ✅ | ✅ |
| Director, Growth Marketing — Commercial (San Mateo) | ✅ | – |
| Senior Technical Recruiter (San Mateo) | – | ✅ |
| Senior Technical Recruiter — Hardware Operations (San Mateo) | – | ✅ |
| Staff Technical Recruiter (San Mateo) | – | ✅ |

**Recommendation:** remove underlines from all 6 postings (use bold or a real heading instead). Strip italics from non-section content unless there is an editorial reason (book titles, foreign terms).

---

### 3.8 Inline `style="…"` attributes leaking into the CMS

Only one offender, but it is a tell that the author pasted from Google Docs or Word:

- **Manager, Logistics** (US CA Production) — contains `style="min-height:1.2em;margin-top:0;margin-bottom:0"` on a paragraph. This overrides the site’s consistent paragraph spacing for that one element.

**Recommendation:** strip inline styles on publish. Add a “paste as plain text” editor option (or filter) in the CMS.

---

### 3.9 Job-title double-space defect

Four titles in the listing render with a noticeable extra gap because there are two spaces after the comma:

- `Senior Software Engineer,␣␣Infrastructure`
- `Senior Software Engineer,␣␣Data Platform`
- `Enterprise Account Manager,␣␣US Navy, US Marine Corps, and IC/SOCOM`
- `Staff Global Supply Manager,␣␣Mechanicals`

**Recommendation:** trivial copy fix in the CMS — collapse any run of consecutive spaces in the title field on save.

---

### 3.10 Pre-compensation body length

Not strictly a *formatting* issue, but worth flagging because on the listing/landing pages two postings side by side can look visibly imbalanced if one is 3× the length of the other.

- Median pre-comp body length: **~470 words**.
- Shortest: *Supply Chain Intern* (229 words), *Electrical Engineer (all levels)* (244), *Senior Autonomy Engineer — Controls* (245), *Software Engineer, Full Stack* (254), *Autonomy Engineer — Fixed Wing Planning & Controls* (260).
- Longest: *Staff Product Manager, Platform & Infrastructure* (786), *Manager, Technical Support* (780), *Full Stack Product Counsel* (771), *Senior Product Manager, Platform & Infrastructure* (767), *Senior Software Engineer, Data Platform* (731).

**Recommendation:** set soft length guidelines in the editorial guide (e.g. 350–550 words for the role description). Trim outliers above ~700, expand the four 229–260-word stubs to at least give all three standard sections.

---

## 4. What is *already* consistent (do not change)

These dimensions are uniform across all 111 postings and should be preserved:

- **Page-title styling** (`<h1>` with the `.type-h2` class) — same font, size, weight, color, and alignment on every page.
- **Location/employment line** (`<p>` with the `.type-body-2` class) — same on every page.
- **Boilerplate intro paragraph.** All 111 postings start with the exact same paragraph (`“Skydio is the leading US drone company and the world leader in autonomous flight…”`).
- **Body font family, base font size, body color, line height, alignment, and link styling** — controlled by `.prose.block-content` and identical everywhere.
- **No posting uses a non-standard color, font face, or pixel size** in inline CSS. Every visible difference traces to a different *tag* or *string*, not a different *style*.

---

## 5. Prioritized action list

| Priority | Action | Effort | Where |
|:--:|---|---|---|
| **P0** | Replace `<h1>` in the Tokyo *Senior Technical Support Representative* posting with the standard tag (recommended `<h2>`). It currently renders at the same size as the job title. | 1 edit | CMS |
| **P0** | Fix the typo `What Makes Your a Good Fit` on *Senior People Analytics Analyst*. | 1 edit | CMS |
| **P0** | Collapse double-spaces in the 4 affected job titles. | 4 edits | CMS |
| **P0** | Strip the inline `style="min-height:1.2em…"` from *Manager, Logistics*. | 1 edit | CMS |
| **P1** | Pick **one** section-heading tag (`<h2>` recommended) and convert all 111 postings to use it. Drop the colon, use sentence case, use the curly apostrophe (`’`). | ≈ 111 edits, scriptable | CMS / data migration |
| **P1** | Sweep the 49 postings that mix period / no-period bullet endings; pick a single bullet style and apply. | 49 edits | CMS |
| **P1** | Add the three *no-section-headings* postings (Product Support Engineer, Product Support Engineer Intern, Technical Support Specialist – West Coast) into the standard template. | 3 edits | CMS |
| **P2** | Remove `<u>` underlines from the 6 postings that use them and `<em>` from the 3 postings that use them (or justify each case editorially). | 9 edits | CMS |
| **P2** | Strip the 53 stray empty `<p></p>` paragraphs and convert the 47 postings’ in-paragraph `<br>` tags into real paragraph breaks (worst offenders: 8 `<br>` in *IT Technician (Help Desk – Linux Focus)* and *Director, Growth Marketing — Commercial*; 8 empty paragraphs in *Full Stack Product Counsel*). Scriptable. | ≈ 60 postings, scriptable | CMS / data migration |
| **P2** | Reconcile the long-tail section labels into one canonical list (`About the role`, `How you’ll make an impact`, `What makes you a good fit`, optional `Bonus points`). | ≈ 30 postings | CMS |
| **P3** | Trim the 5 longest postings (>700 words) and expand the 5 shortest (<260 words) so the page feels balanced. | 10 postings | Recruiting / hiring managers |
| **P3** | Add a CMS publish-time linter that flags: inline `style=` attributes, `<br>` tags, empty `<p>` tags, `<h1>` in the body, straight apostrophes, double-spaces, and missing/typo’d section headings. Prevents the back-catalog issues from recurring. | One-time engineering | CMS / build pipeline |

---

## 6. Appendix — per-posting characteristic table

The full per-posting characteristic table (all 111 postings) is included as a sibling Markdown file: [`job-posting-formatting-audit-per-posting.md`](./job-posting-formatting-audit-per-posting.md). Columns:

- **Title / Location** — exactly as shown on the listing.
- **Words** — word count of the pre-`Compensation` body.
- **Section heading style** — `p>strong`, `h2`, `h3`, `h1`, combinations (e.g. `h2+p>strong`), or `none`.
- **Has `<br>`** — number of `<br>` tags in the body (0 = clean).
- **Empty `<p>`** — number of empty paragraphs in the body (0 = clean).
- **Italic/Underline** — `em` / `u` flags and any inline `style="…"` count.
- **Bullet end-punctuation** — `period` (all end with `.`), `none` (none end with `.`), `mixed` (mixed within the same posting), or `–` (no bullets).
- **Section labels used** — verbatim list of the headings the author wrote.

---

## 7. Method & reproducibility

- All 111 posting pages were downloaded from `https://www.skydio.com/jobs/{id}/?gh_jid={id}` on **2026-05-16**.
- The pre-compensation block was extracted as everything inside the `<div class="prose block-content">` up to the first occurrence of `<strong>Compensation`, `<h2>Compensation`, `<h3>Compensation`, or `<p>Compensation:` (whichever came first).
- Counts in §1 and §3 were produced by parsing the resulting HTML fragments and tallying the relevant tag/text patterns. Because the entire site shares one CSS bundle, no per-posting computed-style inspection was needed — typography differences are 1-to-1 with the authored HTML differences reported here.
- If this audit is rerun later, the same scripts will produce a comparable report; the categories in §3 are stable across re-runs.
