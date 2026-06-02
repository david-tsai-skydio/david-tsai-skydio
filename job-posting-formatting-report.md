# Skydio Careers — Job Posting Formatting Consistency Report

**Source:** [https://www.skydio.com/careers](https://www.skydio.com/careers)
**Postings analyzed:** 115 (every posting linked from the careers index)
**Scope:** All content above the `Compensation:` block (intro + section
headings + body bullets). Compensation, EEO/E-Verify boilerplate, and the
embedded Ashby application form were intentionally excluded.
**Method:** All 115 job pages were fetched and the contents of
`<div class="prose block-content">` were programmatically parsed and compared
(tag usage, inline styles, heading text, capitalization, punctuation,
whitespace, structure).

---

## 1. Executive summary

The page-level chrome (page title `<h1 class="type-h2">`, the location line
`<p class="type-body-2">`) is **fully consistent** across all 115 postings —
the inconsistencies all live inside the description body that recruiters /
hiring managers paste into the Ashby/CMS editor.

The "norm" is a 3-section template authored as bold paragraphs:

```html
<p><strong>About the Role:</strong></p>
<p>…intro paragraph…</p>
<p><strong>How You'll Make an Impact:</strong></p>
<ul><li><p>bullet</p></li>…</ul>
<p><strong>What Makes You a Good Fit:</strong></p>
<ul><li><p>bullet</p></li>…</ul>
<p><strong>Compensation:</strong></p>   ← cut-off point
```

Out of 115 postings, only ~30 follow this template cleanly. The remaining 85
deviate in at least one of the following ways: capitalization, punctuation,
heading element type (`<h1>` / `<h2>` / `<h3>` vs. bold paragraph), missing
sections, mid-paragraph bolding, stray `<br>` tags, empty paragraphs,
non-breaking spaces, smart vs. straight apostrophes, or an entire
template-swap to `<h2>/<h3>` headings.

The most visually disruptive issues are:

1. **Heading hierarchy is not unified.** 95 postings use `<p><strong>…</strong></p>`,
   18 use real `<h2>/<h3>`, and 1 uses `<h1>`. The `<h1>` posting renders the
   section labels at the same size as the page's job-title — a clear visual
   bug.
2. **Section labels render in two different styles** — Title Case
   ("About the Role:") on ~50 postings and sentence case ("About the role:")
   on ~64 postings.
3. **16 postings have no recognizable section headings at all** — a giant
   wall-of-text was pasted as a single paragraph.
4. **57 postings contain mid-paragraph bold or run-together text**, where a
   section heading is concatenated to the end of the previous paragraph
   instead of standing on its own line.

Detailed counts and per-posting breakdowns follow.

---

## 2. The "norm" / canonical template

| Element | Canonical form | Postings that match |
|---|---|---|
| Page title | `<h1 class="type-h2">{title}</h1>` | 115 / 115 ✅ |
| Location line | `<p class="type-body-2">{Location} - {Type}</p>` | 115 / 115 ✅ |
| Section heading | `<p><strong>About the Role:</strong></p>` (Title Case + colon) | ~30 / 115 |
| Body bullets | `<ul><li><p>…</p></li></ul>` | 114 / 115 ✅ |
| Inline styles | none (theme handles all sizing) | 114 / 115 ✅ |

Only one posting injects an inline style attribute and zero use inline
font-size, font-weight, font-family, or color declarations — so visual
inconsistency is **driven by structure and text choices, not by ad-hoc CSS.**

---

## 3. Inconsistency findings

### 3.1 Heading hierarchy / element type

| Element used for section labels | # postings |
|---|---|
| `<p><strong>…</strong></p>` (the canonical pattern) | 95 |
| `<h2>` | 12 |
| `<h3>` | 4 |
| Mixed `<h2>` + `<h3>` (sub-sections) | 3 |
| `<h1>` (renders same size as job title) | 1 |
| No section headings at all (single blob of text) | 16 |

Postings to flag:

- **`<h1>` misuse** — `Senior Technical Support Representative - Japan`
  uses `<h1>` for "About the role:", "How you'll make an impact:" and "What
  would make you a good fit:". These render at the same visual weight as
  the page title.
- **`<h2>` template variant** (12) — these section headings are visibly
  larger and more spaced than the bold-paragraph variant used everywhere
  else. Examples:
  `Aviation Compliance Lead`, `Aviation Regulatory Program Manager`,
  `Communications Manager`, `Senior Buyer`, `Senior Wireless Software Engineer, National Security`,
  `Software Engineer - Autonomy Infrastructure, Systems and Tools` (×2 listings),
  `Software Engineer - Cloud Simulation & Full-Stack` (×2 listings),
  `Revenue Operations Engineer, Quoting Systems`.
- **`<h3>` template variant** (4) —
  `Full Stack Product Counsel`, `PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning)`,
  `Senior Business Operations Manager`,
  `Software Engineer - Simulation & Robotics Engineer` (×2 listings).
- **Mixed `<h2>` + `<h3>`** —
  `GTM Engineer, Pre-Sales`, `Hardware Engineering Program Manager`,
  `Logistics Operations Specialist, HQ`. These are the only postings using
  multi-level section nesting; the rest of the careers site has no such
  visual pattern.
- **No headings at all (16)** — the description was pasted as one or two
  giant paragraphs:
  `Software Engineer - Simulation & Robotics Engineer` (×2),
  `Software Engineer - Autonomy Infrastructure, Systems and Tools` (×2),
  `Software Engineer - Cloud Simulation & Full-Stack` (×2),
  `Communications Manager`, `Product Support Engineer`,
  `Logistics Operations Specialist, HQ`, `Hardware Engineering Program Manager`,
  `Aviation Compliance Lead`, `GTM Engineer, Pre-Sales`,
  `Full Stack Product Counsel`, `Aviation Regulatory Program Manager`,
  `Senior Wireless Software Engineer, National Security`,
  `Senior Technical Support Representative - Japan`.

### 3.2 Heading capitalization (Title Case vs. sentence case)

The same conceptual sections are split almost evenly between two styles:

| Canonical section | Title-Case variants | Sentence-case variants |
|---|---|---|
| About the Role | `"About the Role:"` (23) / `"About The Role"` (1) | `"About the role:"` (48) / `"About the role"` (2) |
| How You'll Make an Impact | `"How You'll Make an Impact:"` (18) / `"How You'll Make an Impact"` (1) / `"How You'll Make an Impact:"` (18) | `"How you'll make an impact:"` (26) / `"How you'll make an impact:"` (10) |
| What Makes You a Good Fit | `"What Makes You a Good Fit:"` (18) / `"What Makes You A Good Fit:"` (1) / `"What Makes You a Good Fit"` (1) | `"What makes you a good fit:"` (49) / `"What makes you a good fit"` (2) |
| About the Team | `"About the Team:"` (9) | `"About the team:"` (5) |

Within a single posting, capitalization is internally consistent, but
across postings users see two distinct visual styles depending on which
recruiter authored the role. Net result: **the careers index feels like
two different companies wrote it.**

### 3.3 Missing or trailing punctuation

- 19 postings are missing the trailing colon on at least one section
  heading. Examples:
  `Customer Success Manager, Commercial` ("What makes you a good fit"),
  `Customer Success Manager, DFR Majors - Southeast` ("Requirements"),
  `Customer Success Manager, DFR Mid-Market - Northeast` ("Requirements",
  "Experience & Skills"), `Mission Success Operations Manager`
  ("What makes you a good fit"), `IT Technician (Help Desk - Linux Focus)`
  ("About the Role", "What Makes You a Good Fit", "Nice to Have"),
  `Program Manager, Commercial Programs` ("About the Role"),
  `Senior Software Engineer, Data Platform` ("Why Join Us?" — a `?` not `:`),
  `Workplace Experience Coordinator Part-Time`
  ("Workplace Experience & Office Operations", "People Operations & HR
  Coordination", "Qualifications", "Work Environment").
- 11 postings have a trailing space *inside* the `<strong>` tag, e.g.
  `<strong>About the role: </strong>` instead of
  `<strong>About the role:</strong>`. While usually invisible, this leaks
  whitespace before the next word when the heading is run inline. Found in:
  `Autonomy Engineer - Fixed Wing Planning & Controls`,
  `Senior Revenue Operations Manager`, `Lead Staff Electrical Engineer`,
  `Program Manager, Commercial Programs`, `Manager, Technical Support`,
  `GTM Enablement Associate`, `Senior Engineering Manager, Infrastructure`,
  `Software Engineer - Autonomy Infrastructure, Systems and Tools`,
  `Customer Success Manager, DFR Mid-Market - Northeast`,
  `Senior Business Operations Manager`,
  `Senior Wireless Software Engineer, National Security` (`" RF data links"`).
- 6 postings put a non-breaking space (`\u00A0`) inside the heading:
  `Director of Product Management, Drone as First Responder (DFR)`,
  `Senior Director, Product Management, Drone as First Responder (DFR)`,
  `Senior Software Engineer - Embedded`,
  `Staff Software Engineer - Embedded`,
  `Software Engineer - Embedded`. These were almost certainly pasted from
  Google Docs / Word.

### 3.4 Apostrophe style ("you'll" vs. "you'll")

- Curly apostrophe (`’`, U+2019) in section labels: **52 postings**.
- Straight ASCII apostrophe (`'`, U+0027): **33 postings**.
- Two postings mix BOTH styles within the same description:
  `Senior Product Manager, Platform & Infrastructure`,
  `Staff Product Manager, Platform & Infrastructure`.

This is the textual equivalent of using two different fonts — it looks
fine in isolation but obviously inconsistent in side-by-side comparisons
(and search/copy-paste behavior also differs between the two glyphs).

### 3.5 Mid-paragraph bold / merged blocks

**57 of 115 postings** have at least one paragraph that mixes bold "heading"
text with running prose, instead of putting the heading on its own line.
Typical patterns:

- `<strong>About the role: </strong>Skydio is the leading…` — the heading
  is glued to the very first sentence (e.g., `Lead Staff Electrical Engineer`,
  `Director of Product Management, Drone as First Responder (DFR)`,
  `Senior Director, Product Management, Drone as First Responder (DFR)`,
  `Senior Engineering Manager, Infrastructure`,
  `Senior Software Engineer - Embedded`, `Staff Software Engineer - Embedded`,
  `Software Engineer - Embedded`, `GTM Enablement Associate`,
  `Senior People Analytics Analyst`,
  `Director, Growth Marketing - Commercial`,
  `Manager, Technical Support`).
- `<strong>About the role:</strong><br/><br/>` — a heading followed by
  manually inserted `<br>` line breaks instead of a paragraph break (e.g.,
  `Autonomy Engineer - Deep Learning Infrastructure`,
  `Autonomy Engineer - Deep Learning Model Acceleration`).
- A whole sub-list pasted as one paragraph with `<strong>Term:</strong>`
  embedded in the middle (e.g., `Revenue Operations Engineer, Quoting Systems`,
  `Senior Product Manager, Platform & Infrastructure`,
  `Staff Product Manager, Platform & Infrastructure`,
  `Senior Software Engineer, Data Platform`).

The visual symptom: line spacing collapses, bullet points disappear, and
the section labels appear to "float" inside body text instead of acting
as headings.

### 3.6 Stray block-level whitespace

| Issue | Postings |
|---|---|
| Empty `<p></p>` (extra vertical gap) | **57** (1–5 empty paragraphs each) |
| `<br>` tags inside the body (manual line breaks) | **48** (1–9 brs each) |
| Both empty paragraphs **and** `<br>` tags | 25+ |

Top offenders for empty paragraphs:
`Customer Success Manager, DFR Mid-Market - Northeast` (5),
`Program Manager, Commercial Programs` (5),
`Staff Software Engineer, Frontend` (5),
`Deployment Engineer - Southeast` (5),
`Senior/Staff Embedded Software Engineer – Camera Systems` (4),
`Customer Success Manager, Commercial` (4).

Top offenders for `<br>` tags:
`IT Technician (Help Desk - Linux Focus)` (9),
`Director, Growth Marketing - Commercial` (8),
`Autonomy Engineer - Deep Learning Infrastructure` (8),
`Autonomy Engineer - Deep Learning Model Acceleration` (6),
`Systems Integration and Test Engineer (Mid to Senior Level)` (5),
`Software Engineer Intern Fall 2026/Winter 2027` (4),
`Autonomy Software Engineer` (4).

The combined effect is unpredictable line-height: some postings have
tight ~1× line spacing, others have ~1.5×, and a few have noticeable
double-spaces between the title block and the first paragraph.

### 3.7 Wall-of-text paragraphs

30 postings contain at least one paragraph longer than 600 characters
(i.e. >100 words on a single visual line block). The longest examples:

| Length (chars) | Posting |
|---|---|
| 1,341 | `Field Support Representative (Southwest, Remote)` |
| 1,334 | `Manager, Technical Support` |
| 1,075 | `Product Support Engineer` |
| 1,051 | `Systems Integration and Test Engineer (Mid to Senior Level)` |
| 1,044 | `Autonomy Engineer - Deep Learning Infrastructure` |
| 1,036 | `Full Stack Product Counsel` |
| 1,035 | `Aviation Compliance Lead` |
|   960 | `Senior Manager, Training` |
|   943 | `Senior Customer Support Representative - India` |
|   941 | `Senior Technical Support Representative - Japan` |

These are postings where bullet content has been collapsed into prose
with no list formatting, producing a noticeably denser visual block
than the rest of the careers page.

### 3.8 Inline styling and "off-template" formatting

- **Inline `style` attribute** found in only 1 posting:
  `Manager, Logistics` —
  `style="min-height:1.2em;margin-top:0;margin-bottom:0"` (an empty
  paragraph forced to render). No font-size, font-weight, font-family,
  color, or background-color overrides exist anywhere — every other
  posting relies on the global `prose` typography theme.
- **Underline tags** (`<u>`) appear 8 times across 1 posting:
  `Senior NPI Product Quality Engineer` uses `<em><strong><u>Please Note:</u></strong></em>`
  for an onsite-presence callout. Underlines are unique to this posting
  and visually conflict with hyperlinks.
- **Italic / `<em>` tags** appear in only 2 spots site-wide
  (1 of them is the underline-italic combo above). Effectively no
  posting uses italics for emphasis.

### 3.9 Title-text issues (page `<h1>`)

Four postings have a double-space after a comma in the page title — these
render with a visibly wider gap than other titles:

- `Senior Software Engineer,  Infrastructure`
- `Senior Software Engineer,  Data Platform`
- `Staff Global Supply Manager,  Mechanicals`
- `Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM`

### 3.10 Spelling / copy-edit issues surfaced during the scan

- `Senior People Analytics Analyst` → "**What Makes Your a Good Fit:**"
  (typo: "Your" should be "You"). This is also one of the postings that
  uses real `<h2>` for "About The Role" but a bold-paragraph heading
  for the rest, so it has a heading-hierarchy issue *and* a typo.

### 3.11 Optional-section naming

The fourth ("nice-to-have") section uses 6 different labels across the
~12 postings that include it:

- `Bonus points:` (2)
- `Bonus points for:` (4)
- `Bonus Points:` (3)
- `Nice to have:` (2)
- `Nice to Have` (1, no colon)
- `Even better` (1, no colon — `Senior Wireless Software Engineer, National Security`)
- `Nice-to-Haves:` (1)
- `Additional Desired Experience and Skills` (1, no colon —
  `Director, Growth Marketing - Commercial`)
- `Nice To Haves` (1, no colon — `GTM Engineer, Pre-Sales`)

### 3.12 "Location" callouts inside the body

The `Location:` line is supposed to live in the canonical
`<p class="type-body-2">` row beneath the title. Instead, **15+ postings**
duplicate or relocate it inside the description body as a bold paragraph
or as a `<strong>` glued to the start of "About the role:". Typical
examples:

- `Senior Revenue Operations Manager` — "**Location:** SF/Bay area - hybrid 3 days in office"
- `Manager, Technical Support` — multi-paragraph "**Location:** This is an office or remote-based position…"
- `Customer Success Manager, DFR Mid-Market - Northeast` — "**Location Preference:** …"
- `Public Safety Strategist (West Coast, Midwest, or Pacific North West)` —
  bold "West Coast, Midwest, or Pacific North West" with no label
- `Director of Product Management, Drone as First Responder (DFR)` and
  `Senior Director, Product Management, Drone as First Responder (DFR)`
  bake the location into the same paragraph as "About the role:"
- `Hardware Engineering Program Manager`, `GTM Enablement Associate`,
  `Aviation Compliance Lead`, etc. all introduce a "Location" sub-line
  in different visual styles.

Some postings include this duplication; others rely solely on the row
above the body. The reader sees two different layouts.

---

## 4. Per-posting "stand-out" list (most divergent from norm)

Ranked by number of distinct issues from the canonical template:

| Posting | Issues |
|---|---|
| `Senior Technical Support Representative - Japan` | Uses `<h1>` for section labels, no template structure, has wall-of-text paragraphs (941 chars). |
| `Logistics Operations Specialist, HQ` | Mixes `<h2>`/`<h3>`, sub-section nesting, no canonical template. |
| `Hardware Engineering Program Manager` | Mixes `<h2>`/`<h3>`, sub-section nesting (Minimum/Preferred Qualifications under "What makes you a good fit"). |
| `GTM Engineer, Pre-Sales` | Mixes `<h2>`/`<h3>`, adds extra "Nice To Haves" section without colon. |
| `Senior People Analytics Analyst` | Typo in section label ("Your" → "You"), runs `<h2>` for one heading and bold paragraphs for others, missing colons. |
| `Senior Wireless Software Engineer, National Security` | All-`<h2>` template, leading space inside a `<strong>` (`" RF data links"`), unusual extra sections ("Even better", "Work location"). |
| `Senior Product Manager, Platform & Infrastructure` / `Staff Product Manager, Platform & Infrastructure` | Both apostrophe styles on the same posting; one giant 5,600-char merged paragraph; headings hidden mid-paragraph. |
| `Customer Success Manager, DFR Mid-Market - Northeast` | 5 empty paragraphs, "Requirements" without colon, "Location Preference:" injected. |
| `Program Manager, Commercial Programs` | 5 empty paragraphs, "About the Role" missing colon, mis-uses bold for "PMP certification" requirement line. |
| `Director, Growth Marketing - Commercial` | 8 `<br>` tags, missing-colon headings, "Additional Desired Experience and Skills" instead of "What makes you a good fit". |
| `Director of Product Management, Drone as First Responder (DFR)` / `Senior Director, Product Management, Drone as First Responder (DFR)` | Heading concatenated with body via `<strong>About the role:\u00A0</strong>…`, multiple non-breaking spaces. |
| `Manager, Logistics` | Only posting with an inline `style` attribute. |
| `Senior NPI Product Quality Engineer` | Only posting using `<em><strong><u>` triple-styling for emphasis. |
| `Revenue Operations Engineer, Quoting Systems` | All `<h2>` headings, embeds an entire bulleted list as bold-marker paragraph instead of `<ul>`. |
| `Software Engineer - Cloud Simulation & Full-Stack` (×2 listings) / `Software Engineer - Autonomy Infrastructure, Systems and Tools` (×2 listings) / `Software Engineer - Simulation & Robotics Engineer` (×2 listings) | All-`<h2>`/`<h3>` headings; extra "Areas of Responsibility" and "Bonus Experience" sections; non-canonical template. |
| `Senior Software Engineer - Embedded` / `Staff Software Engineer - Embedded` / `Software Engineer - Embedded` | Section labels glued to body with `\u00A0`; merged heading-paragraph blocks. |
| `Autonomy Engineer - Deep Learning Infrastructure` / `Autonomy Engineer - Deep Learning Model Acceleration` | 6–8 `<br>` tags, no real section breaks, single 1,000+ char paragraph. |

---

## 5. Recommendations for standardizing the formatting

### 5.1 Adopt and enforce one heading style

Pick **one** of the two existing patterns and migrate everything to it:

- **Option A (recommended):** keep the bold-paragraph pattern
  `<p><strong>Section Title:</strong></p>` because 95/115 postings already
  use it and the careers theme already styles it correctly. Rewrite the
  ~20 postings using `<h1>/<h2>/<h3>`.
- **Option B:** use real `<h2>` semantics for accessibility and a11y;
  this is better for screen-readers but requires updating ~95 postings
  and matching the page CSS to render `<h2>` at the same visual size as
  the current bold paragraph.

Either way, **lock the choice in a CMS template** (Ashby supports
required structured fields) so recruiters cannot paste raw HTML/Word
formatting.

### 5.2 Lock down section labels to a canonical phrasing

Create a fixed list of allowed section labels and reject anything else:

- `About the Role:`
- `About the Team:` (optional, only when relevant)
- `How You'll Make an Impact:`
- `What Makes You a Good Fit:`
- `Bonus Points:` (optional)
- `Compensation:` (this is the cut-off and is already enforced)

Mandate Title-Case + trailing colon for all section labels and pick
**one apostrophe style** (recommend the curly `’` — used by 52 postings
and matches the rest of the marketing site copy). A simple linter or
CMS-side regex catch can be added.

### 5.3 Strip pasted-from-Word artifacts on save

A copy-paste sanitizer should:

- collapse runs of `&nbsp;`/U+00A0 to a single regular space (fixes 6 postings),
- delete trailing whitespace inside `<strong>` (fixes 11 postings),
- delete double spaces inside titles (fixes 4 page titles),
- remove empty `<p></p>` and `<br>` tags inside list bodies (fixes 57+48 postings),
- forbid `<u>` and inline `style="font-…"`/`style="color:…"`/inline
  `style="*"` attributes (only 1 posting currently has any inline style,
  so enforcement is cheap),
- forbid mid-paragraph `<strong>` followed by running prose — flag the
  57 affected postings and split them into proper heading + paragraph.

### 5.4 Force list structure for "How You'll Make an Impact" and
        "What Makes You a Good Fit"

Sixteen postings have no `<ul>` at all and 30 have at least one
600+ char paragraph. CMS validation should require those two sections
to be a `<ul>`/`<li>` list (3+ items). This single rule eliminates
the largest visual divergence between postings.

### 5.5 Move the "Location:" callout to a structured field

The duplicated "Location:" / "Location Preference:" lines that 15+
postings inject into the body should be modelled as a structured field
under the page title (similar to the existing
`San Mateo, California, United States – Full-time` row). When the
location is unusually nuanced (hybrid schedules, multi-region
flexibility), the row should flex to two lines instead of being
re-pasted as a bolded paragraph in the body.

### 5.6 Copy-edit pass

- Fix typo on `Senior People Analytics Analyst` —
  "What Makes Your a Good Fit" → "What Makes You a Good Fit".
- Remove double-spaces from the four page titles listed in §3.9.
- Standardize the optional "nice-to-have" section to one label
  (recommend `Bonus Points:`).

### 5.7 Add a CI / pre-publish check

A small script (the same one that produced this report) can run on
every job-board sync. It should fail the publish if a posting:

1. Uses any heading element other than the chosen one,
2. Has a section label outside the allow-list,
3. Contains `&nbsp;`, `<br>`, empty `<p></p>`, `<u>`, or inline `style`,
4. Has a paragraph longer than 600 chars in the bullet sections, or
5. Mixes apostrophe styles within a single description.

Running that check today would have flagged **roughly 85 of 115 postings**
— close to ~74% of the live careers page is currently off-template in
at least one of the ways above.

---

## Appendix A — Data files

- `job-posting-formatting-report.md` — this report.
- (analysis pipeline artifacts kept locally, not committed) — raw HTML,
  per-posting JSON summaries, and `analyze.py` / `analyze2.py` extraction
  scripts. Available on request if the team wants to reproduce or extend
  the linting.

## Appendix B — Distribution sketch (counts at a glance)

```
Total postings analysed:                   115
Postings 100% on-template (canonical):    ~30
Posters using a different heading element: 19
Postings without recognizable headings:    16
Postings with mid-paragraph bold:          57
Postings with empty <p></p>:               57
Postings with <br> tags inside body:       48
Postings with curly apostrophe headings:   52
Postings with straight apostrophe headings:33
Postings with U+00A0 in body text:         29
Postings with paragraphs > 600 chars:      30
Postings with section heading missing colon:19
Postings using <h1> for section labels:     1
Postings using inline style attributes:     1
Page titles with double-space artifacts:    4
Confirmed typos in section labels:          1
```
