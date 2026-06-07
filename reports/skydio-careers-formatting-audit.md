# Skydio Careers — Job Posting Formatting Consistency Audit

**Source:** [https://www.skydio.com/careers](https://www.skydio.com/careers) (Ashby-hosted job pages embedded under `skydio.com/jobs/<id>/`)
**Audit date:** 2026-06-07
**Scope:** Content of each job posting from the start of the description through the last bullet before the **Compensation** block (i.e. the diversity / EEO / compensation boilerplate is excluded).
**Sample size:** 25 postings across every represented department (Autonomy, Connectivity, Hardware, Product, Security, Software, Customer Support, Manufacturing, Marketing, People & Recruiting, Professional Services, Sales, Solutions Engineering, Supply Chain, Legal).

---

## 1. How the postings are styled

All job pages are rendered by the same Ashby embed and share one stylesheet (`/assets/css/ashby.css`). That means font family, base font size, line-height, link color, body color and bullet styling are physically identical across every posting. **Visible inconsistencies in font size, weight, color or spacing therefore come entirely from differences in the underlying HTML structure of each description** (which Ashby renders verbatim).

The relevant HTML primitives in use across the sample are:

| Pattern | What it renders as | Frequency in sample |
|---|---|---|
| `<p><strong>Section title:</strong></p>` ("pseudo‑header") | Bold paragraph at body size (~16 px), small bottom margin | **Used by 20 / 25 postings** — the de‑facto house style |
| `<h2><strong>Section title:</strong></h2>` | Browser/Ashby H2: ~24‑28 px, extra bold, much larger margin | 3 postings |
| `<h3><strong>Section title</strong></h3>` | H3: ~20‑22 px, large margin | 1 posting |
| `<ul><li><p>…</p></li></ul>` | Bulleted list with extra paragraph spacing per item | All postings |
| `<br/>` inside `<p>` | Forces a line break / extra vertical space | 0–8 per posting (see below) |
| `<em>` / `<u>` | Italic / underline | Only 2 postings |
| Inline `<strong>` inside body text or bullets | Mid‑sentence bolding | 1–26 per posting (see below) |

The very fact that **5 of the 25 postings reach for real `<h2>`/`<h3>` tags** is the single largest visual inconsistency — those postings have section labels that are dramatically larger and bolder than the rest of the careers page.

---

## 2. Posting‑by‑posting formatting profile

Columns: P = paragraphs, UL = bullet lists, LI = list items, BR = `<br>` count, H2/H3 = real heading tags inside description, **PH** = pseudo‑headers (`<p><strong>…</strong></p>`), **inS** = inline `<strong>` runs (a proxy for body bolding), Style = inline `style` attrs, EM/U = italic/underline tags, `#LI` = trailing internal cross‑posting tag.

| # | Job posting | P | UL | LI | BR | H2 | H3 | PH | inS | EM | U | `#LI` |
|---:|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| 1 | Autonomy Engineer – Deep Learning | 22 | 2 | 14 | 1 | 0 | 0 | 3 | 3 | 0 | 0 | ✅ |
| 2 | Senior Autonomy Engineer – Deep Learning | 19 | 2 | 13 | 3 | 0 | 0 | 2 | 3 | 0 | 0 | ✅ |
| 3 | Software Engineer – Cloud Simulation & Full‑Stack | 33 | 4 | 26 | 0 | **5** | 0 | **0** | **26** | 0 | 0 | ✅ |
| 4 | Wireless Software Engineer | 21 | 3 | 12 | 0 | 0 | 0 | 3 | 3 | 0 | 0 | — |
| 5 | Electrical Engineer (all levels) | 18 | 2 | 13 | 2 | 0 | 0 | 2 | 3 | 0 | 0 | — |
| 6 | PCB Layout Engineer | 17 | 2 | 12 | 2 | 0 | 0 | 2 | 3 | 0 | 0 | — |
| 7 | Senior RF Design Engineer | 35 | 3 | 25 | 0 | 0 | 0 | 3 | 3 | 0 | 0 | — |
| 8 | Senior Product Manager, Platform & Infrastructure | 30 | 2 | 15 | 1 | 0 | 0 | 3 | **14** | 0 | 0 | — |
| 9 | Staff Software Engineer – Security | 24 | 3 | 17 | 0 | 0 | 0 | 4 | 5 | 0 | 0 | — |
| 10 | Senior Software Engineer – Embedded | 24 | 3 | 17 | 0 | 0 | 0 | 4 | 4 | 0 | 0 | — |
| 11 | Software Engineer, Full Stack | 22 | 3 | 13 | 0 | 0 | 0 | 4 | 5 | 0 | 0 | — |
| 12 | Software Engineer Intern Fall 2026 | 20 | 3 | 12 | 4 | 0 | 0 | 1 | 3 | 0 | 0 | — |
| 13 | Field Support Representative | 26 | 2 | 18 | 0 | 0 | 0 | 4 | 4 | 0 | 0 | — |
| 14 | Senior Customer Support Representative – India | 30 | 3 | 22 | 0 | 0 | 0 | 3 | 4 | 0 | 0 | — |
| 15 | Senior NPI Product Quality Engineer | 26 | 2 | 19 | 0 | 0 | 0 | 3 | 3 | **1** | **1** | — |
| 16 | Director, Growth Marketing – Commercial | 34 | **6** | 23 | **8** | 0 | 0 | **5** | 6 | **1** | 0 | — |
| 17 | Senior Technical Recruiter | 9 | 1 | 5 | 0 | 0 | 0 | 1 | 1 | 0 | 0 | — |
| 18 | Customer Success Manager, Commercial | 32 | 2 | 20 | 0 | 0 | 0 | 4 | 4 | 0 | 0 | — |
| 19 | Enterprise Account Manager, US Army | 27 | 2 | 20 | 0 | 0 | 0 | 3 | 3 | 0 | 0 | — |
| 20 | GTM Engineer, Pre‑Sales | 35 | **8** | 28 | 3 | **4** | **7** | **0** | 4 | 0 | 0 | — |
| 21 | Senior Solutions Engineer – North East | 21 | 2 | 13 | 1 | 0 | 0 | 2 | 4 | 0 | 0 | — |
| 22 | Hardware Operations Program Manager | 21 | 2 | 12 | 0 | 0 | 0 | 3 | 9 | 0 | 0 | — |
| 23 | Senior Buyer | 30 | 2 | 22 | 0 | **2** | 0 | 1 | 3 | 0 | 0 | — |
| 24 | Senior Manager, Training | 25 | 2 | 17 | 2 | 0 | 0 | 1 | 3 | 0 | 0 | — |
| 25 | Full Stack Product Counsel | 23 | 2 | 15 | 0 | 0 | **4** | **0** | 4 | 0 | 0 | — |

Cells flagged **in bold** are the values that deviate from the rest of the cohort.

---

## 3. What stands out as different from the norm

### 3.1 Five postings use real heading tags instead of the house pseudo‑header

The dominant pattern is a bold paragraph (`<p><strong>About the role:</strong></p>`). The exceptions render section labels at a much larger size and weight, breaking visual consistency the moment you open the page:

| Posting | What it does instead | Visual effect |
|---|---|---|
| **GTM Engineer, Pre‑Sales** | `<h2><strong>About the Role:</strong></h2>` for top sections + `<h3>` for every sub‑topic (e.g. "Find the right problems to solve", "Build things that scale") | Section titles roughly 1.5× larger, sub‑headers also far larger than other postings' body text |
| **Software Engineer – Cloud Simulation & Full‑Stack** | `<h2><strong>About the Role:</strong></h2>`, `<h2><strong>What You'll Do:</strong></h2>`, `<h2><strong>Bonus Experience:</strong></h2>` | Headings are oversized vs. peer SWE postings |
| **Senior Buyer** | Mixes one pseudo‑header (`About the role:`) with two `<h2><strong>How you will make an impact:</strong></h2>` headings | Visually inconsistent *within the same posting* |
| **Full Stack Product Counsel** | Uses `<h3><strong>About the Team</strong></h3>`, `<h3><strong>About the Role</strong></h3>` etc. — and uses **no `<p><strong>` headers at all** | Headers are larger than peers but smaller than the H2 postings — a third visual scale |
| **GTM Engineer, Pre‑Sales** (again) | Also uses `<h3>` for *sub‑sections* under each H2 (e.g. "You're a builder with AI fluency") | Introduces a 4‑level visual hierarchy not present anywhere else |

### 3.2 Heavy `<br>` usage in one marketing posting

`<br/>` is rare in this sample (0–3 in almost every posting), but **Director, Growth Marketing – Commercial uses 8 `<br/>` tags**. The result is extra blank space in the middle of paragraphs that you do not see elsewhere. **Software Engineer Intern Fall 2026** also uses 4 `<br/>` tags — about 4× the median.

### 3.3 Mid‑sentence bolding is wildly uneven

The number of inline `<strong>` runs that are not section headers ranges from 1 to 26 across the sample.

* **Software Engineer – Cloud Simulation & Full‑Stack** has **26** inline `<strong>` runs — every bullet contains 1–3 bolded terms (e.g. "**3D or visualization technologies**", "**Temporal**", "**Three.js or WebGL**"). No other posting bolds keywords inside bullets like this.
* **Senior Product Manager, Platform & Infrastructure** has **14** — also far above the median (≈4). It bolds product names, locations and qualifiers throughout the description.
* **Hardware Operations Program Manager** has **9** — moderately high.
* The other 22 postings sit between 1 and 6.

The visual effect is that two postings look "noisy" with many bolded words while the rest read as clean body text.

### 3.4 The only italics and the only underline in the sample

* **Senior NPI Product Quality Engineer** is the only posting in the sample that uses `<u>` (underline), and it does so wrapped in both `<em>` and `<strong>`: `<em><strong><u>Please Note:</u></strong></em>`. That single line renders as italic + bold + underlined — three emphasis modes stacked. No other posting uses this style anywhere.
* **Director, Growth Marketing – Commercial** uses `<em><strong>Ability to be in our San Mateo, CA office 3 days per week</strong></em>` as the final bullet of a list — italic + bold. No other posting italicises a bullet.

### 3.5 Boilerplate “cross‑posting” tag is present in only 3 postings

`#LI-SM1` (LinkedIn campaign tag) appears at the end of the body in:

* Autonomy Engineer – Deep Learning
* Senior Autonomy Engineer – Deep Learning
* Software Engineer – Cloud Simulation & Full‑Stack

It is missing from the other 22. This is a content/operations leak rather than a styling issue, but it is visible to candidates.

---

## 4. Section labels: capitalisation, punctuation, wording

Even among the postings that use the standard pseudo‑header pattern, the **labels themselves are not standardised**. The "About / How / What" trio appears in at least six variants:

### 4.1 Capitalisation drift

| Variant | Used by |
|---|---|
| `About the role:` (sentence case) — *the de‑facto house style* | 14 postings |
| `About the Role:` (title case) | Enterprise Account Manager US Army, Senior RF Design Engineer, Staff Software Engineer – Security, Wireless Software Engineer, GTM Engineer Pre‑Sales (in H2), Cloud Sim (in H2), Full Stack Product Counsel (in H3) |
| `About the team:` vs `About the Team:` | Field Support Representative uses lowercase, Customer Success Manager Commercial uses Title Case, Full Stack Product Counsel uses Title Case |

Same drift on "How you'll make an impact":

| Variant | Used by |
|---|---|
| `How you'll make an impact:` (sentence case, **straight** apostrophe) | Autonomy Engineer DL, Senior Autonomy Engineer DL, Hardware Ops PM, Senior NPI PQE, Senior PM Platform, Senior SWE Embedded, Senior Technical Recruiter |
| `How you'll make an impact:` (sentence case, **curly** apostrophe `’`) | Customer Success Manager, Field Support Rep, Senior Customer Support India, Software Engineer Full Stack, Staff SWE Security |
| `How You'll Make an Impact:` (Title Case, curly) | Enterprise Account Manager US Army, Senior RF Design Engineer, Wireless Software Engineer |

### 4.2 The "good fit" section is the most fragmented

The same concept ("required/preferred qualifications") appears under at least **six different labels** in the sample:

* `What makes you a good fit:` — the most common form
* `What Makes You a Good Fit:` — Title Case variant
* `What would make you a good fit:` — Senior Customer Support India, Software Engineer Full Stack
* `What would make you a strong fit:` — Senior PM Platform & Infrastructure
* `What makes you a strong fit:` — Senior Buyer
* `What Makes You a Great Fit` — Full Stack Product Counsel (and missing trailing colon)
* `What Would Make You a Good Fit:` — Director Growth Marketing

### 4.3 Trailing colons are inconsistent

The convention appears to be "section header ends with a colon", but it is not enforced:

* Missing colon: `What makes you a good fit` (Customer Success Manager, Commercial), `Additional Desired Experience and Skills` (Director Growth Marketing), `Nice To Haves` (GTM Engineer), all four sections of Full Stack Product Counsel, the `Location` opener of Senior PM Platform & Infrastructure.
* Present colon: every other posting.

### 4.4 Invisible whitespace inside header text

**Senior Software Engineer – Embedded** has a non‑breaking space (`\xa0`) embedded inside the strong tag itself: `<strong>About the team:\xa0</strong>` and `<strong>About the role:\xa0</strong>`. Visually it adds an extra trailing space after the colon that no other posting has, and it would also defeat naive string matching on the section name.

### 4.5 "Bonus" sections — three labels for the same idea

* `Bonus Points:` — Software Engineer, Full Stack
* `Nice to have:` — Staff Software Engineer – Security
* `Nice To Haves` (no colon) — GTM Engineer, Pre‑Sales
* `Bonus Experience:` — Software Engineer – Cloud Simulation & Full‑Stack

### 4.6 Non‑standard top‑level sections

A few postings drop the standard 3‑part structure entirely:

* **Director, Growth Marketing – Commercial** uses a unique 5‑part outline: *About the role / Key Responsibilities / What Success Looks Like / What Would Make You a Good Fit / Additional Desired Experience and Skills*.
* **Senior Product Manager, Platform & Infrastructure** opens with a section literally titled `Location` (no colon) before any "About the role" — the only posting where the first bold header is about geography.

---

## 5. Bullet hygiene

All postings use Ashby's native bulleted list (`<ul><li><p>…</p></li></ul>`). Visual issues within the lists:

* **Terminal punctuation is mixed.** Within the same posting bullets frequently mix periods and no‑periods (e.g. Senior Buyer ends technical bullets with periods but a five‑item "soft skills" group at the very end with no periods at all). No posting in the sample is internally 100 % consistent on this.
* **Bullet length varies dramatically between postings.** Median bullet length runs ~75 chars for engineering postings vs. 130+ chars for some Sales/Operations postings, which produces visually denser bullet blocks for the latter.
* **GTM Engineer, Pre‑Sales** is the only posting in the sample whose bullets are broken into 7 separate small lists under sub‑headings rather than 2–3 long lists.

No `<ol>` (numbered list) is used anywhere in the sample.

---

## 6. Headline issues, ranked by visibility

1. **Heading hierarchy mismatch (visible on first scroll)** – 5 of 25 postings use real `<h2>`/`<h3>` tags instead of the bold‑paragraph house style, producing section titles that are visibly larger and bolder.
2. **Inline bolding overload** – Cloud Sim and Senior PM Platform & Infrastructure read as noticeably "bolder" than every other posting because they bold individual keywords within bullets.
3. **Inconsistent section names** – the same section appears under six labels across the site, with mixed capitalisation, mixed punctuation, and curly vs. straight apostrophes.
4. **Excess vertical whitespace** – Director, Growth Marketing – Commercial inserts 8 `<br>` tags, producing larger gaps than any other posting.
5. **Stray italic + underline** – Senior NPI Product Quality Engineer's triple‑emphasised "Please Note" is the only italic+underline in the sample and stands out as an anomaly.
6. **Leftover internal tags** – `#LI-SM1` left in body text of 3 Autonomy/SWE postings.
7. **Hidden whitespace inside headers** – Senior SWE – Embedded leaks `\xa0` characters into its section headers.

---

## 7. Recommendations for standardisation

### 7.1 Lock down a single section template

Adopt a canonical 3‑part structure that the recruiting team can copy/paste:

```
About the role:
  <intro paragraph(s)>

How you'll make an impact:
  <bulleted responsibilities>

What makes you a good fit:
  <bulleted requirements>

Nice to have:    ← optional, used only when needed
  <bulleted preferred>
```

Specifically agree on:

* **Sentence case** for every section title (`About the role:`, not `About the Role:`).
* **Straight ASCII apostrophe** for `you'll` (and configure the rich text editor to disable smart quotes for this field, or paste from a plain‑text source).
* **Trailing colon** on every section title.
* **One word** for the "preferred" section across all postings — pick `Nice to have:` and retire `Bonus Points`, `Bonus Experience`, `Nice To Haves`, `Additional Desired Experience and Skills`.
* **One word** for the "requirements" section across all postings — pick `What makes you a good fit:` and retire `What would make you a good fit`, `What Makes You a Great Fit`, `What makes you a strong fit`, `What would make you a strong fit`.

### 7.2 Forbid heading tags inside descriptions

Ashby's rich‑text editor lets recruiters apply `Heading 2` / `Heading 3`. That produces the oversized H2/H3 titles seen on GTM, Cloud Sim, Senior Buyer and Full Stack Product Counsel.

* Update the recruiting style guide to **use only Bold for section titles** (which produces `<p><strong>…</strong></p>`).
* Fix the four affected postings: GTM Engineer Pre‑Sales, Software Engineer – Cloud Simulation & Full‑Stack, Senior Buyer, Full Stack Product Counsel.
* If sub‑sections are really needed (as in GTM), use bold + sentence case at the start of the bullet group rather than a heading tag.

### 7.3 Reserve inline bolding for true emphasis (or eliminate it)

* Set a soft cap of ≤2 inline `<strong>` runs per bullet list.
* Re‑edit the two outliers — **Software Engineer – Cloud Simulation & Full‑Stack** (26 inline strongs) and **Senior Product Manager, Platform & Infrastructure** (14 inline strongs) — to remove keyword‑highlighting bolding so they match the rest of the site.

### 7.4 Strip stray HTML primitives

* **No `<br>` for spacing** — Ashby already gives paragraphs adequate bottom margin. Audit the Director, Growth Marketing – Commercial posting (8 `<br>` tags) and the Software Engineer Intern posting (4 `<br>` tags) and remove them.
* **No `<em>` and no `<u>`** in the standard description body. Remove the italic+underline on Senior NPI Product Quality Engineer and the italic+bold final bullet on Director, Growth Marketing – Commercial.
* **No non‑breaking spaces** inside section titles. Clean the `\xa0` characters from Senior Software Engineer – Embedded's `About the team:` and `About the role:` headers.

### 7.5 Operational hygiene

* Strip internal `#LI-XX` cross‑posting tags from the public body — currently leaking on Autonomy Engineer – Deep Learning, Senior Autonomy Engineer – Deep Learning, and Software Engineer – Cloud Simulation & Full‑Stack.
* Standardise bullet terminal punctuation: pick "end every bullet with a period" or "no terminal periods on bullets" and apply consistently.
* Add a lightweight pre‑publish lint that flags: any `<h1>`–`<h6>` in the description, any `<br>`, any `<em>`/`<u>`, any non‑breaking space, and any pseudo‑header that doesn't appear on an allow‑list of approved section names.

### 7.6 Quick‑fix priority list

If only a handful of postings can be updated this week, the highest‑impact fixes (in order) are:

1. **GTM Engineer, Pre‑Sales** — remove all `<h2>`/`<h3>` tags; convert to bold paragraphs. Largest visual divergence in the cohort.
2. **Software Engineer – Cloud Simulation & Full‑Stack** — remove `<h2>` headings; remove the 20+ keyword‑bolds inside bullets; remove `#LI-SM1`.
3. **Full Stack Product Counsel** — convert `<h3>` section titles to bold paragraphs.
4. **Senior Buyer** — replace the two `<h2>` section titles with bold paragraphs so the posting is internally consistent.
5. **Director, Growth Marketing – Commercial** — remove the 8 `<br>` tags and the italic+bold last bullet; rename non‑standard sections to the canonical labels.
6. **Senior Product Manager, Platform & Infrastructure** — open with `About the role:` instead of `Location`; remove ~10 of the 14 mid‑paragraph bolds.
7. **Senior NPI Product Quality Engineer** — remove the italic/underline on "Please Note".
8. **Senior Software Engineer – Embedded** — strip non‑breaking spaces inside `About the team:` / `About the role:` headers.
9. **All postings** — pick a single canonical apostrophe (straight or curly) and rewrite the 25 `you'll` / `you'll` instances to match. Pick sentence case vs. Title Case for section titles and rewrite the ~7 Title‑Case offenders to match.

---

## Appendix A — Methodology

* The careers index at `https://www.skydio.com/careers` was scraped to enumerate all 110+ open req URLs.
* 25 reqs were sampled to give at least one example from every department visible on the index.
* Each posting was fetched via plain HTTP and the description HTML extracted from the page (the description is rendered server‑side, not via JavaScript).
* The description was truncated at the first occurrence of any of: `Compensation`, `salary range`, `Pay Range`, `Total Rewards`, `Qualified applicants will receive consideration`, `At Skydio we believe that diversity drives innovation`, `Skydio is an equal opportunity`. Everything after these markers (compensation block, diversity statement, EEO notices) was excluded from analysis as instructed.
* All structural counts in §2 were measured directly from the HTML; capitalisation and punctuation findings in §4 come from textual comparison of the extracted section titles across the sample.
* All visual claims (e.g. "H2 renders ~24‑28 px") are based on the shared Ashby stylesheet (`/assets/css/ashby.css`) that styles every posting identically.

## Appendix B — Sample of 25 postings analysed

Autonomy Engineer – Deep Learning · Senior Autonomy Engineer – Deep Learning · Software Engineer – Cloud Simulation & Full‑Stack · Wireless Software Engineer · Electrical Engineer (all levels) · PCB Layout Engineer · Senior RF Design Engineer · Senior Product Manager, Platform & Infrastructure · Staff Software Engineer – Security · Senior Software Engineer – Embedded · Software Engineer, Full Stack · Software Engineer Intern Fall 2026 · Field Support Representative · Senior Customer Support Representative – India · Senior NPI Product Quality Engineer · Director, Growth Marketing – Commercial · Senior Technical Recruiter · Customer Success Manager, Commercial · Enterprise Account Manager, US Army · GTM Engineer, Pre‑Sales · Senior Solutions Engineer – North East · Hardware Operations Program Manager · Senior Buyer · Senior Manager, Training · Full Stack Product Counsel.
