# Skydio Careers — Job Posting Formatting Consistency Report

Source: https://www.skydio.com/careers — 118 open job postings analyzed (snapshot fetched 2026-06-05). Only the **pre-compensation** body of each posting (everything inside the `prose` content container up to but not including the `Compensation:` paragraph) was evaluated.

All Skydio job posting bodies are rendered through the same `prose block-content` CSS wrapper, so font family, base font size, line height, text color and alignment are controlled centrally and are visually identical across postings. The observable formatting inconsistencies therefore come from the **HTML/markup choices made by the content authors** when each posting was written. This report enumerates those authoring inconsistencies — they are the things that actually show up as visual differences (e.g. a bold label rendered as a `<p><strong>` vs. an `<h3>` will render at different sizes/weights), as well as the items that *don't* affect rendering but indicate inconsistent authoring discipline.

---

## 1. Executive summary

Six recurring inconsistencies were found across the 118 postings. They are listed below in roughly decreasing user-visible impact:

| # | Inconsistency | Where it occurs | User-visible impact |
| --- | --- | --- | --- |
| A | Section headings rendered with mixed markup (`<p><strong>…:</strong></p>` vs. real `<h1>`-`<h6>`) | 18 / 118 postings use real headings | **High** – heading tags render at a different size/weight than bold paragraphs |
| B | Inconsistent / missing standard section labels (About the role / How you'll make an impact / What makes you a good fit) | see §3 | **High** – readers expect the same three sections in the same order |
| C | Inline `style=` attributes and custom class names inside the body | 0 postings carry inline styles; 10 carry extra classes | **Medium** – overrides the design-system styling for one posting |
| D | Bullet items mix sentence-style punctuation (some end in '.', others don't) and mix leading bold/non-bold patterns | 79 postings have at least one bullet ending in '.', 22 use leading-bold bullets | **Medium** – list rhythm varies |
| E | Use of `<br>`, empty paragraphs, nested lists, and ordered lists where bullets would be more consistent | 45 have `<br>`, 60 have empty `<p>`, 5 have nested lists, 0 use `<ol>` | **Low–Medium** – extra vertical whitespace |
| F | Stray non-breaking spaces / em-dashes in some postings | 11 postings contain `&nbsp;`; 22 use em-dashes | **Low** – author-tool artefacts |

Average pre-compensation body length is ~3,622 characters (median 3,534). The shortest posting is **1,706** chars (*Senior Autonomy Engineer - Controls *(San Mateo, California, United States)**); the longest is **6,124** chars (*Senior Director, Product Management, Drone as First Responder (DFR) *(San Mateo, California, United States)**). Length itself is not necessarily a defect, but the outliers in section 6 are worth a content review.

---

## 2. Finding A — Mixed markup for section headings

Skydio's CSS styles the `prose` container so that **real `<h1>`-`<h6>` elements render at a larger size and a different weight** than a `<p><strong>...</strong></p>` bold paragraph. The vast majority of postings (100 / 118) use the *bold paragraph* style for their section labels (e.g. `About the role:`, `How you'll make an impact:`, `What makes you a good fit:`). The following **18 postings break this convention** by using actual heading tags — they will appear visually *larger and heavier* than the rest of the postings, which is the most obvious eye-catching inconsistency on the site:

| Job title | Heading tags found in the body |
| --- | --- |
| Aviation Compliance Lead *(San Mateo, California, United States)* | `<h2>` ×3 |
| Communications Manager *(US Remote)* | `<h2>` ×3 |
| Engineering Program Manager *(San Mateo, California, United States)* | `<h2>` ×3, `<h3>` ×5 |
| Full Stack Product Counsel *(San Mateo, California, United States)* | `<h3>` ×4 |
| GTM Engineer, Pre-Sales *(US CA San Mateo)* | `<h2>` ×4, `<h3>` ×7 |
| Logistics Operations Specialist, HQ *(San Mateo, California, United States)* | `<h2>` ×3, `<h3>` ×3 |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) *(Zurich, Switzerland)* | `<h3>` ×3 |
| Revenue Operations Analyst, CPQ *(San Mateo, California, United States)* | `<h2>` ×5 |
| Senior Business Operations Manager *(San Mateo, California, United States)* | `<h3>` ×3 |
| Senior Buyer *(Hayward, California, United States)* | `<h2>` ×2 |
| Senior Technical Support Representative - Japan *(Tokyo, Japan)* | `<h1>` ×3 |
| Senior Wireless Software Engineer, National Security *(San Mateo, California, United States)* | `<h2>` ×6 |
| Software Engineer - Autonomy Infrastructure, Systems and Tools *(San Mateo, California, United States)* | `<h2>` ×5 |
| Software Engineer - Autonomy Infrastructure, Systems and Tools *(Zurich, Switzerland)* | `<h2>` ×5 |
| Software Engineer - Cloud Simulation & Full-Stack *(San Mateo, California, United States)* | `<h2>` ×5 |
| Software Engineer - Cloud Simulation & Full-Stack *(Zurich, Switzerland)* | `<h2>` ×5 |
| Software Engineer - Simulation & Robotics Engineer *(San Mateo, California, United States)* | `<h3>` ×5 |
| Software Engineer - Simulation & Robotics Engineer *(Zurich, Switzerland)* | `<h3>` ×5 |

**Fix:** Strip any `<h1>`/`<h2>`/`<h3>` elements from the job body and replace them with the standard `<p><strong>Label:</strong></p>` form.

---

## 3. Finding B — Missing or renamed standard section labels

The Skydio house template uses three canonical bold-paragraph section labels, in order:

1. `About the role:`
2. `How you'll make an impact:`
3. `What makes you a good fit:`

Below is how often each of these labels (and close variants) appears across the 118 postings. The variant tables group together every label that shares the leading word with the canonical phrasing — so for example `About the Team:` is listed under `About the role:` because it competes for the same template slot. Case differences and straight-quote vs. smart-quote apostrophes (`'` vs. `’`) are shown explicitly because they appear in the page source as different strings even though they look almost identical:

### `About the role:` — used in 106 of 118 postings

| Variant used | # postings |
| --- | --- |
| `About the role:` | 55 |
| `About the Role:` | 35 |
| `About the Team:` | 10 |
| `About the team:` | 6 |

### `How you'll make an impact:` — used in 89 of 118 postings

| Variant used | # postings |
| --- | --- |
| `How you'll make an impact:` | 43 |
| `How You’ll Make an Impact:` | 23 |
| `How you’ll make an impact:` | 18 |
| `How you will make an impact:` | 4 |
| `How You'll Make an Impact:` | 1 |

### `What makes you a good fit:` — used in 110 of 118 postings

| Variant used | # postings |
| --- | --- |
| `What makes you a good fit:` | 57 |
| `What Makes You a Good Fit:` | 23 |
| `What would make you a good fit:` | 7 |
| `What makes you a strong fit:` | 6 |
| `What You’ll Do:` | 6 |
| `What would make you a strong fit:` | 2 |
| `What makes this internship different:` | 1 |
| `What Makes You a Great Fit:` | 1 |
| `What Success Looks Like:` | 1 |
| `What Would Make You a Good Fit:` | 1 |
| `What You'll Work On:` | 1 |
| `What Makes You A Good Fit:` | 1 |
| `What you’ll drive (scope):` | 1 |
| `What you’ll bring:` | 1 |
| `What you will do:` | 1 |

#### Postings missing one or more of the standard sections (48 / 118)

| Job title | Missing standard section(s) |
| --- | --- |
| Autonomy Engineer - Deep Learning Infrastructure *(San Mateo, California, United States)* | `About the role:`, `How you'll make an impact:` |
| Autonomy Engineer - Deep Learning Infrastructure *(Zurich, Switzerland)* | `About the role:`, `How you'll make an impact:` |
| Autonomy Engineer - Deep Learning Model Acceleration *(San Mateo, California, United States)* | `About the role:`, `How you'll make an impact:` |
| Autonomy Engineer - Deep Learning Model Acceleration *(Zurich, Switzerland)* | `About the role:`, `How you'll make an impact:` |
| Autonomy Engineer - Planning and Controls *(Zurich, Switzerland)* | `How you'll make an impact:` |
| Autonomy Software Engineer *(San Mateo, California, United States)* | `About the role:`, `How you'll make an impact:` |
| Customer Success Manager, Commercial *(US Remote)* | `What makes you a good fit:` |
| Customer Success Manager, DFR Mid-Market - Northeast *(US Remote)* | `What makes you a good fit:` |
| Director of Product Management, Drone as First Responder (DFR) *(San Mateo, California, United States)* | `About the role:`, `How you'll make an impact:` |
| Director, Global Supply Management - Mechanicals *(San Mateo, California, United States)* | `How you'll make an impact:` |
| Director, Growth Marketing - Commercial *(San Mateo, California, United States)* | `How you'll make an impact:` |
| Electrical Engineer (Sustaining/Validation) *(San Mateo, California, United States)* | `How you'll make an impact:` |
| Electrical Engineer (all levels) *(San Mateo, California, United States)* | `How you'll make an impact:` |
| Equipment and Inventory Specialist (Part Time) *(San Mateo, California, United States)* | `About the role:`, `How you'll make an impact:`, `What makes you a good fit:` |
| Field Service Technician *(US CA San Mateo)* | `About the role:`, `How you'll make an impact:` |
| GTM Enablement Associate *(San Mateo, California, United States)* | `About the role:` |
| IT Technician (Help Desk - Linux Focus) *(Hayward, California, United States)* | `About the role:`, `How you'll make an impact:`, `What makes you a good fit:` |
| Lead Staff Electrical Engineer *(San Mateo, California, United States)* | `About the role:` |
| Logistics Operations Specialist, HQ *(San Mateo, California, United States)* | `About the role:`, `How you'll make an impact:`, `What makes you a good fit:` |
| Mission Success Operations Manager *(US Remote)* | `What makes you a good fit:` |
| PCB Layout Engineer *(San Mateo, California, United States)* | `How you'll make an impact:` |
| Product Design Engineer (All Levels) *(San Mateo, California, United States)* | `About the role:` |
| Product Support Engineer *(San Mateo, California, United States)* | `About the role:`, `How you'll make an impact:`, `What makes you a good fit:` |
| Program Manager, Commercial Programs *(US AR Remote)* | `About the role:`, `How you'll make an impact:` |
| Revenue Operations Analyst, CPQ *(San Mateo, California, United States)* | `How you'll make an impact:` |
| Senior Autonomy Engineer - Deep Learning *(San Mateo, California, United States)* | `About the role:` |
| Senior Autonomy Engineer - Deep Learning *(Zurich, Switzerland)* | `About the role:` |
| Senior Director, Product Management, Drone as First Responder (DFR) *(San Mateo, California, United States)* | `About the role:`, `How you'll make an impact:` |
| Senior Engineering Manager, Infrastructure *(San Mateo, California, United States)* | `About the role:` |
| Senior Hardware Test and Reliability Engineer *(San Mateo, California, United States)* | `What makes you a good fit:` |
| Senior Manager, Training *(US Remote)* | `What makes you a good fit:` |
| Senior Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | `About the role:` |
| Senior Software Engineer,  Infrastructure *(San Mateo, California, United States)* | `About the role:` |
| Senior Technical Recruiter *(San Mateo, California, United States)* | `About the role:` |
| Senior Technical Recruiter - Hardware Operations *(San Mateo, California, United States)* | `About the role:`, `How you'll make an impact:` |
| Software Engineer - Autonomy Infrastructure, Systems and Tools *(San Mateo, California, United States)* | `How you'll make an impact:` |
| Software Engineer - Autonomy Infrastructure, Systems and Tools *(Zurich, Switzerland)* | `How you'll make an impact:` |
| Software Engineer - Cloud Simulation & Full-Stack *(San Mateo, California, United States)* | `How you'll make an impact:` |
| Software Engineer - Cloud Simulation & Full-Stack *(Zurich, Switzerland)* | `How you'll make an impact:` |
| Software Engineer - Infrastructure *(San Mateo, California, United States)* | `About the role:` |
| Software Engineer - Simulation & Robotics Engineer *(San Mateo, California, United States)* | `How you'll make an impact:` |
| Software Engineer - Simulation & Robotics Engineer *(Zurich, Switzerland)* | `How you'll make an impact:` |
| Software Engineer Intern Fall 2026/Winter 2027 *(San Mateo, California, United States)* | `About the role:`, `How you'll make an impact:` |
| Staff Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | `About the role:` |
| Staff Software Engineer, Full Stack *(San Mateo, California, United States)* | `About the role:` |
| Supply Chain Intern *(San Mateo, California, United States)* | `How you'll make an impact:` |
| Systems Integration and Test Engineer (Mid to Senior Level) *(San Mateo, California, United States)* | `What makes you a good fit:` |
| Workplace Experience Coordinator Part-Time *(Zurich, Switzerland)* | `About the role:`, `What makes you a good fit:` |

**Fix:** Standardise the three labels exactly as listed above. In particular, replace variants like `What you'll do`, `Responsibilities`, `Qualifications`, `Requirements`, `Who you are`, etc. with the canonical phrasing, and add the missing sections.

---

## 4. Finding C — Inline `style=` attributes and stray CSS classes

Every posting body should rely on the centrally-defined `prose` styling. Inline `style=` attributes and custom class names introduced inside a specific posting will override the design-system rules and create one-off visual deviations (different colors, sizes, weights, etc.).

### Postings with inline `style=` attributes (0)

_None._

### Postings with stray CSS classes inside the body (10)

| Job title | # | Example class(es) |
| --- | --- | --- |
| Autonomy Engineer - Deep Learning Infrastructure *(San Mateo, California, United States)* | 4 | `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">` |
| Autonomy Engineer - Deep Learning Model Acceleration *(San Mateo, California, United States)* | 4 | `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">` |
| Autonomy Software Engineer *(San Mateo, California, United States)* | 4 | `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">` |
| Engineering Manager - Autonomy *(San Mateo, California, United States)* | 4 | `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">` |
| Senior Software Engineer - Embedded *(San Mateo, California, United States)* | 4 | `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">` |
| Senior Technical Recruiter *(San Mateo, California, United States)* | 4 | `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">` |
| Senior Technical Recruiter - Hardware Operations *(San Mateo, California, United States)* | 4 | `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">` |
| Software Engineer - Embedded *(San Mateo, California, United States)* | 4 | `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">` |
| Staff Software Engineer - Embedded *(San Mateo, California, United States)* | 4 | `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">` |
| Staff Technical Recruiter *(San Mateo, California, United States)* | 4 | `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">`; `<a class="c-link c-link--underline">` |

**Fix:** Strip all inline `style=` attributes and remove non-`prose` class names from the rich-text content of each posting. Visual tweaks (extra spacing, color highlights, etc.) should be implemented as global rules in the design system, not as per-posting overrides.

---

## 5. Finding D — Inconsistent bullet-list formatting

Most postings use unordered lists whose items are short fragments without a trailing period and without leading bold text. The following postings deviate from that convention:

### Bullet items ending in `.` (79 postings)

| Job title | Items ending in '.' |
| --- | --- |
| Logistics Operations Specialist, HQ *(San Mateo, California, United States)* | 38 / 38 |
| Software Engineer - Cloud Simulation & Full-Stack *(Zurich, Switzerland)* | 26 / 26 |
| Software Engineer - Cloud Simulation & Full-Stack *(San Mateo, California, United States)* | 26 / 26 |
| Senior Wireless Software Engineer, National Security *(San Mateo, California, United States)* | 25 / 25 |
| Public Safety Strategist (West Coast, Midwest, or Pacific North West) *(US Remote)* | 24 / 28 |
| Engineering Program Manager *(San Mateo, California, United States)* | 23 / 23 |
| Product Support Engineer *(San Mateo, California, United States)* | 22 / 22 |
| Software Engineer - Simulation & Robotics Engineer *(Zurich, Switzerland)* | 20 / 20 |
| Software Engineer - Simulation & Robotics Engineer *(San Mateo, California, United States)* | 20 / 20 |
| Senior Software Engineer,  Data Platform *(San Mateo, California, United States)* | 20 / 20 |
| Field Support Representative - New York *(US NY Remote)* | 20 / 22 |
| Senior Customer Support Representative - India *(Bangalore, India)* | 20 / 22 |
| Field Support Representative (Southwest, Remote) *(US Remote)* | 19 / 21 |
| Software Engineer - Autonomy Infrastructure, Systems and Tools *(Zurich, Switzerland)* | 18 / 20 |
| Software Engineer - Autonomy Infrastructure, Systems and Tools *(San Mateo, California, United States)* | 18 / 20 |
| Senior Engineering Manager, Infrastructure *(San Mateo, California, United States)* | 18 / 18 |
| Field Support Representative *(US Remote)* | 18 / 18 |
| CSM Manager - Public Safety (Major Markets) *(US Remote)* | 18 / 18 |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) *(Zurich, Switzerland)* | 17 / 17 |
| Senior Autonomy Engineer, Data Curation *(San Mateo, California, United States)* | 17 / 17 |
| Senior Technical Support Representative - Japan *(Tokyo, Japan)* | 17 / 20 |
| Senior Buyer *(Hayward, California, United States)* | 17 / 22 |
| Senior Materials Program Manager *(San Mateo, California, United States)* | 17 / 17 |
| Product Design Engineer (All Levels) *(San Mateo, California, United States)* | 16 / 16 |
| Staff Software Engineer, Full Stack *(San Mateo, California, United States)* | 16 / 16 |
| Mission Success Operations Manager *(US Remote)* | 16 / 17 |
| Senior Manager, Training *(US Remote)* | 16 / 17 |
| Staff Global Supply Manager,  Mechanicals *(San Mateo, California, United States)* | 16 / 17 |
| Senior Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | 15 / 15 |
| Staff Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | 15 / 15 |

_…and 49 more._

### Bullet items with leading bold sub-label (22 postings)

Pattern: a list item that starts with `<strong>Sub-label:</strong>` followed by descriptive text. Most postings don't use this pattern; those that do will look 'denser' than the rest.

| Job title | Items with leading bold |
| --- | --- |
| Revenue Operations Analyst, CPQ *(San Mateo, California, United States)* | 16 / 25 |
| Senior Wireless Software Engineer, National Security *(San Mateo, California, United States)* | 10 / 25 |
| Senior Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | 9 / 15 |
| Staff Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | 9 / 15 |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) *(Zurich, Switzerland)* | 8 / 17 |
| Software Engineer - Simulation & Robotics Engineer *(Zurich, Switzerland)* | 6 / 20 |
| Software Engineer - Simulation & Robotics Engineer *(San Mateo, California, United States)* | 6 / 20 |
| Hardware Operations Program Manager *(Hayward, California, United States)* | 6 / 12 |
| Software Engineer - Cloud Simulation & Full-Stack *(Zurich, Switzerland)* | 5 / 26 |
| Software Engineer - Cloud Simulation & Full-Stack *(San Mateo, California, United States)* | 5 / 26 |
| Software Engineer - Autonomy Infrastructure, Systems and Tools *(Zurich, Switzerland)* | 4 / 20 |
| Software Engineer - Autonomy Infrastructure, Systems and Tools *(San Mateo, California, United States)* | 4 / 20 |
| Senior Engineering Manager, Infrastructure *(San Mateo, California, United States)* | 4 / 18 |
| Senior Technical Recruiter *(San Mateo, California, United States)* | 2 / 14 |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision *(Zurich, Switzerland)* | 1 / 9 |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision *(San Mateo, California, United States)* | 1 / 9 |
| Manager, Technical Support *(San Mateo, California, United States)* | 1 / 22 |
| Director, Growth Marketing - Commercial *(San Mateo, California, United States)* | 1 / 23 |
| Senior Technical Recruiter - Hardware Operations *(San Mateo, California, United States)* | 1 / 13 |
| Program Manager, Commercial Programs *(US AR Remote)* | 1 / 21 |
| Program Manager, DFR *(US NY Remote)* | 1 / 16 |
| Public Safety Strategist (West Coast, Midwest, or Pacific North West) *(US Remote)* | 1 / 28 |

### Numbered lists (`<ol>`) in the body (0 postings)

_None._

### Nested lists inside list items (5 postings)

| Job title | # of nested lists |
| --- | --- |
| IT Technician (Help Desk - Linux Focus) *(Hayward, California, United States)* | 4 |
| Mission Success Operations Manager *(US Remote)* | 1 |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision *(San Mateo, California, United States)* | 1 |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision *(Zurich, Switzerland)* | 1 |
| Public Safety Strategist (West Coast, Midwest, or Pacific North West) *(US Remote)* | 2 |

**Fix:** Pick one bullet style and apply it everywhere. The most common Skydio pattern is *unordered, sentence fragment, no terminal period, no leading bold*. Convert numbered lists and nested lists into a flat bulleted list where possible.

---

## 6. Finding E — Stray `<br>`, empty paragraphs, and outlier lengths

### Postings with `<br>` line-break tags (45)

| Job title | # of <br> |
| --- | --- |
| IT Technician (Help Desk - Linux Focus) *(Hayward, California, United States)* | 18 |
| Autonomy Engineer - Deep Learning Infrastructure *(San Mateo, California, United States)* | 16 |
| Director, Growth Marketing - Commercial *(San Mateo, California, United States)* | 16 |
| Autonomy Engineer - Deep Learning Infrastructure *(Zurich, Switzerland)* | 12 |
| Autonomy Engineer - Deep Learning Model Acceleration *(Zurich, Switzerland)* | 12 |
| Autonomy Engineer - Deep Learning Model Acceleration *(San Mateo, California, United States)* | 12 |
| Director of Product Management, Drone as First Responder (DFR) *(San Mateo, California, United States)* | 12 |
| Field Service Technician *(US CA San Mateo)* | 12 |
| Autonomy Software Engineer *(San Mateo, California, United States)* | 8 |
| Senior Director, Product Management, Drone as First Responder (DFR) *(San Mateo, California, United States)* | 8 |
| Software Engineer Intern Fall 2026/Winter 2027 *(San Mateo, California, United States)* | 8 |
| Senior Technical Recruiter - Hardware Operations *(San Mateo, California, United States)* | 8 |
| Revenue Operations Analyst, CPQ *(San Mateo, California, United States)* | 8 |
| Senior Autonomy Engineer - Deep Learning *(Zurich, Switzerland)* | 6 |
| GTM Engineer, Pre-Sales *(US CA San Mateo)* | 6 |
| Supply Chain Intern *(San Mateo, California, United States)* | 6 |
| Autonomy Engineer - Planning and Controls *(Zurich, Switzerland)* | 4 |
| Senior Autonomy Engineer - Deep Learning *(San Mateo, California, United States)* | 4 |
| Electrical Engineer (all levels) *(San Mateo, California, United States)* | 4 |
| PCB Layout Engineer *(San Mateo, California, United States)* | 4 |
| Senior Wireless Software Engineer, National Security *(San Mateo, California, United States)* | 4 |
| Product Support Engineer *(San Mateo, California, United States)* | 4 |
| Senior Technical Support Representative - Japan *(Tokyo, Japan)* | 4 |
| Senior Technical Recruiter *(San Mateo, California, United States)* | 4 |
| Senior Manager, Training *(US Remote)* | 4 |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Finland) *(Tampere, Finland)* | 4 |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Germany) *(Germany)* | 4 |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland) *(Zurich, Switzerland)* | 4 |
| GTM Enablement Associate *(San Mateo, California, United States)* | 4 |
| Autonomy Engineer - Deep Learning *(Zurich, Switzerland)* | 2 |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 *(Zurich, Switzerland)* | 2 |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 *(San Mateo, California, United States)* | 2 |
| Engineering Manager - Autonomy *(San Mateo, California, United States)* | 2 |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision *(Zurich, Switzerland)* | 2 |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision *(San Mateo, California, United States)* | 2 |
| Electrical Engineer (Sustaining/Validation) *(San Mateo, California, United States)* | 2 |
| Lead Staff Electrical Engineer *(San Mateo, California, United States)* | 2 |
| Product Design Engineer (All Levels) *(San Mateo, California, United States)* | 2 |
| Senior Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | 2 |
| Staff Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | 2 |
| Senior Software Engineer,  Data Platform *(San Mateo, California, United States)* | 2 |
| Senior Software Engineer, Full Stack *(San Mateo, California, United States)* | 2 |
| Workplace Experience Coordinator Part-Time *(Zurich, Switzerland)* | 2 |
| Aviation Compliance Lead *(San Mateo, California, United States)* | 2 |
| Staff Global Supply Manager,  Mechanicals *(San Mateo, California, United States)* | 2 |

### Postings with empty `<p>` paragraphs (60)

| Job title | # of empty <p> |
| --- | --- |
| Full Stack Product Counsel *(San Mateo, California, United States)* | 8 |
| Senior Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | 6 |
| Staff Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | 6 |
| Senior Software Engineer, Frontend *(San Mateo, California, United States)* | 5 |
| Staff Software Engineer, Frontend *(San Mateo, California, United States)* | 5 |
| Customer Success Manager, DFR Mid-Market - Northeast *(US Remote)* | 5 |
| Deployment Engineer - Southeast *(US Remote)* | 5 |
| Program Manager, Commercial Programs *(US AR Remote)* | 5 |
| Senior Autonomy Engineer, Data Curation *(San Mateo, California, United States)* | 4 |
| Senior Wireless Software Engineer, National Security *(San Mateo, California, United States)* | 4 |
| Senior/Staff Embedded Software Engineer – Camera Systems *(San Mateo, California, United States)* | 4 |
| Sr/Staff Embedded Software Engineer - Camera Systems *(Tampere, Finland)* | 4 |
| Field Support Representative - New York *(US NY Remote)* | 4 |
| Field Support Representative (Southwest, Remote) *(US Remote)* | 4 |
| Logistics Operations Specialist, HQ *(San Mateo, California, United States)* | 4 |
| CSM Manager - Public Safety (Major Markets) *(US Remote)* | 4 |
| Customer Success Manager, Commercial *(US Remote)* | 4 |
| Autonomy Engineer - ML & DL Infrastructure *(Zurich, Switzerland)* | 3 |
| Autonomy Engineer - ML & DL Infrastructure *(San Mateo, California, United States)* | 3 |
| Wireless Software Engineer *(San Mateo, California, United States)* | 3 |
| Engineering Program Manager *(San Mateo, California, United States)* | 3 |
| Senior Software Engineer - Mobile Platform *(San Mateo, California, United States)* | 3 |
| Software Engineer Intern Fall 2026/Winter 2027 *(San Mateo, California, United States)* | 3 |
| Production Planner, Nightshift *(Hayward, California, United States)* | 3 |
| Senior Buyer *(Hayward, California, United States)* | 3 |
| Senior Materials Program Manager *(San Mateo, California, United States)* | 3 |
| Communications Manager *(US Remote)* | 3 |
| Director, Growth Marketing - Commercial *(San Mateo, California, United States)* | 3 |
| Program Manager, DFR *(US NY Remote)* | 3 |
| Order Management Analyst *(US CA San Mateo)* | 3 |
| Director, Global Supply Management - Mechanicals *(San Mateo, California, United States)* | 3 |
| Hardware Operations Program Manager *(Hayward, California, United States)* | 3 |
| Senior Business Operations Manager *(San Mateo, California, United States)* | 3 |
| Software Engineer - Cloud Simulation & Full-Stack *(Zurich, Switzerland)* | 2 |
| Software Engineer - Cloud Simulation & Full-Stack *(San Mateo, California, United States)* | 2 |
| Software Engineer - Simulation & Robotics Engineer *(San Mateo, California, United States)* | 2 |
| Lead Staff Electrical Engineer *(San Mateo, California, United States)* | 2 |
| Senior RF Design Engineer *(San Mateo, California, United States)* | 2 |
| Product Support Engineer *(San Mateo, California, United States)* | 2 |
| IT Technician (Help Desk - Linux Focus) *(Hayward, California, United States)* | 2 |
| Manager, Logistics *(Hayward, California, United States)* | 2 |
| Manufacturing Execution System Analyst *(Hayward, California, United States)* | 2 |
| GTM Engineer, Pre-Sales *(US CA San Mateo)* | 2 |
| Revenue Operations Analyst, CPQ *(San Mateo, California, United States)* | 2 |
| Senior Revenue Operations Manager *(San Mateo, California, United States)* | 2 |
| Autonomy Engineer - Deep Learning Infrastructure *(San Mateo, California, United States)* | 1 |
| Senior Autonomy Engineer - Deep Learning *(San Mateo, California, United States)* | 1 |
| Software Engineer - Autonomy Infrastructure, Systems and Tools *(Zurich, Switzerland)* | 1 |
| Software Engineer - Autonomy Infrastructure, Systems and Tools *(San Mateo, California, United States)* | 1 |
| Software Engineer - Simulation & Robotics Engineer *(Zurich, Switzerland)* | 1 |
| Middleware Software Engineer Intern - Fall 2026 *(San Mateo, California, United States)* | 1 |
| Senior Customer Support Representative - India *(Bangalore, India)* | 1 |
| Senior Technical Support Representative - Japan *(Tokyo, Japan)* | 1 |
| Workplace Experience Coordinator Part-Time *(Zurich, Switzerland)* | 1 |
| Aviation Compliance Lead *(San Mateo, California, United States)* | 1 |
| Senior Manager, Training *(US Remote)* | 1 |
| GTM Enablement Associate *(San Mateo, California, United States)* | 1 |
| Equipment and Inventory Specialist (Part Time) *(San Mateo, California, United States)* | 1 |
| Staff Global Supply Manager,  Mechanicals *(San Mateo, California, United States)* | 1 |
| Supplier Quality Engineer, Sustaining *(Taiwan)* | 1 |

### Length outliers

**Shortest pre-compensation bodies (may be missing standard sections):**

| Job title | Chars |
| --- | --- |
| Senior Autonomy Engineer - Controls *(San Mateo, California, United States)* | 1,706 |
| Electrical Engineer (all levels) *(San Mateo, California, United States)* | 1,718 |
| Autonomy Engineer - Fixed Wing Planning & Controls *(San Mateo, California, United States)* | 1,790 |
| Electrical Engineer (Sustaining/Validation) *(San Mateo, California, United States)* | 2,083 |
| Senior Autonomy Engineer - Deep Learning *(San Mateo, California, United States)* | 2,184 |
| Lead Staff Electrical Engineer *(San Mateo, California, United States)* | 2,187 |
| Manufacturing Execution System Analyst *(Hayward, California, United States)* | 2,262 |
| Software Engineer, Full Stack *(San Mateo, California, United States)* | 2,272 |

**Longest pre-compensation bodies (may have extra/duplicate content):**

| Job title | Chars |
| --- | --- |
| Senior Director, Product Management, Drone as First Responder (DFR) *(San Mateo, California, United States)* | 6,124 |
| Director of Product Management, Drone as First Responder (DFR) *(San Mateo, California, United States)* | 6,117 |
| Staff Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | 5,745 |
| Senior Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | 5,634 |
| Senior Wireless Software Engineer, National Security *(San Mateo, California, United States)* | 5,610 |
| Manager, Technical Support *(San Mateo, California, United States)* | 5,408 |
| Field Support Representative - New York *(US NY Remote)* | 5,401 |
| GTM Engineer, Pre-Sales *(US CA San Mateo)* | 5,396 |

**Fix:** Remove `<br>` tags and empty paragraphs (the `prose` CSS already supplies vertical rhythm between block elements). Review the shortest postings to make sure they have the three standard sections.

---

## 7. Finding F — Non-breaking spaces and em-dashes

These don't change the rendered font but they often originate from copy-paste out of Word / Google Docs and are worth normalising for consistency.

### Postings containing `&nbsp;` (11)

| Job title | # nbsp |
| --- | --- |
| Field Support Representative (Southwest, Remote) *(US Remote)* | 7 |
| Senior Wireless Systems Performance Engineer *(San Mateo, California, United States)* | 2 |
| Autonomy Engineer - Deep Learning *(San Mateo, California, United States)* | 1 |
| Autonomy Engineer - Deep Learning *(Zurich, Switzerland)* | 1 |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 *(Zurich, Switzerland)* | 1 |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 *(San Mateo, California, United States)* | 1 |
| Autonomy Engineer Intern Fall 2026 *(San Mateo, California, United States)* | 1 |
| Autonomy Engineer Intern Fall 2026 *(Zurich, Switzerland)* | 1 |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision *(Zurich, Switzerland)* | 1 |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision *(San Mateo, California, United States)* | 1 |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) *(Zurich, Switzerland)* | 1 |

### Postings using em-dash `—` (22)

| Job title | # em-dash |
| --- | --- |
| GTM Engineer, Pre-Sales *(US CA San Mateo)* | 15 |
| Senior Software Engineer,  Data Platform *(San Mateo, California, United States)* | 14 |
| Senior Software Engineer - Mobile Platform *(San Mateo, California, United States)* | 8 |
| Senior Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | 6 |
| Staff Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | 6 |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) *(Zurich, Switzerland)* | 3 |
| Senior Software Engineer, Full Stack *(San Mateo, California, United States)* | 3 |
| Staff Software Engineer, Full Stack *(San Mateo, California, United States)* | 2 |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Finland) *(Tampere, Finland)* | 2 |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Germany) *(Germany)* | 2 |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland) *(Zurich, Switzerland)* | 2 |
| Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM *(US Remote)* | 2 |
| Enterprise Account Manager, US Army *(US Remote)* | 2 |
| Software Engineer - Cloud Simulation & Full-Stack *(Zurich, Switzerland)* | 1 |
| Software Engineer - Cloud Simulation & Full-Stack *(San Mateo, California, United States)* | 1 |
| Software Engineer - Simulation & Robotics Engineer *(Zurich, Switzerland)* | 1 |
| Software Engineer - Simulation & Robotics Engineer *(San Mateo, California, United States)* | 1 |
| Senior Wireless Software Engineer, National Security *(San Mateo, California, United States)* | 1 |
| Field Support Representative - New York *(US NY Remote)* | 1 |
| Director, Growth Marketing - Commercial *(San Mateo, California, United States)* | 1 |
| Workplace Experience Coordinator Part-Time *(Zurich, Switzerland)* | 1 |
| Director, Global Supply Management - Mechanicals *(San Mateo, California, United States)* | 1 |

---

## 8. Appendix — Per-posting fingerprint (titles A–Z)

For each posting, the following table lists the standard Skydio section labels found, the markup used, and any deviations. Use this to quickly verify changes against the report.

| Title | Department | Section labels found | Deviation flags |
| --- | --- | --- | --- |
| Autonomy Engineer - Deep Learning *(San Mateo, California, United States)* | Autonomy | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | nbsp |
| Autonomy Engineer - Deep Learning *(Zurich, Switzerland)* | Autonomy | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | <br>, nbsp |
| Autonomy Engineer - Deep Learning Infrastructure *(San Mateo, California, United States)* | Autonomy | `What makes you a good fit:` | **extra-class**, <br>, empty-p |
| Autonomy Engineer - Deep Learning Infrastructure *(Zurich, Switzerland)* | Autonomy | `What makes you a good fit:` | <br> |
| Autonomy Engineer - Deep Learning Model Acceleration *(Zurich, Switzerland)* | Autonomy | `What makes you a good fit:` | <br> |
| Autonomy Engineer - Deep Learning Model Acceleration *(San Mateo, California, United States)* | Autonomy | `What makes you a good fit:` | **extra-class**, <br> |
| Autonomy Engineer - Fixed Wing Planning & Controls *(San Mateo, California, United States)* | Autonomy | `About the Role:`; `How You'll Make an Impact:`; `What Makes You a Good Fit:` | bullet-w-period |
| Autonomy Engineer - ML & DL Infrastructure *(Zurich, Switzerland)* | Autonomy | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | empty-p, bullet-w-period |
| Autonomy Engineer - ML & DL Infrastructure *(San Mateo, California, United States)* | Autonomy | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | empty-p, bullet-w-period |
| Autonomy Engineer - Planning and Controls *(Zurich, Switzerland)* | Autonomy | `About the role:`; `What makes you a good fit:` | <br> |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 *(Zurich, Switzerland)* | Autonomy | `About the role:`; `How you'll make an impact:`; `What makes you a strong fit:` | <br>, nbsp |
| Autonomy Engineer Intern - Computer Vision/Deep Learning Fall 2026 *(San Mateo, California, United States)* | Autonomy | `About the role:`; `How you'll make an impact:`; `What makes you a strong fit:` | <br>, nbsp |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) *(Zurich, Switzerland)* | Autonomy | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | bullet-w-period |
| Autonomy Engineer Intern - Deep Learning (Computational Photography) *(San Mateo, California, United States)* | Autonomy | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | bullet-w-period |
| Autonomy Engineer Intern Fall 2026 *(San Mateo, California, United States)* | Autonomy | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | nbsp |
| Autonomy Engineer Intern Fall 2026 *(Zurich, Switzerland)* | Autonomy | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | nbsp |
| Autonomy Software Engineer *(San Mateo, California, United States)* | Autonomy | `What makes you a good fit:` | **extra-class**, <br> |
| Aviation Compliance Lead *(San Mateo, California, United States)* | Policy & Regulatory Affairs | `About the Role`; `How You’ll Make an Impact`; `What Makes You a Good Fit` | **real-heading**, <br>, empty-p, bullet-w-period |
| Communications Manager *(US Remote)* | Marketing | `About the role`; `How you'll make an impact`; `What makes you a good fit` | **real-heading**, empty-p |
| CSM Manager - Public Safety (Major Markets) *(US Remote)* | Professional Services and Training | `About the Team:`; `About the role:`; `How you’ll make an impact:`; `What makes you a good fit:` | empty-p, bullet-w-period |
| Customer Success Manager, Commercial *(US Remote)* | Professional Services and Training | `About the Team:`; `About the role:`; `How you’ll make an impact:` | empty-p, bullet-w-period |
| Customer Success Manager, DFR Majors - Southeast *(US Remote)* | Professional Services and Training | `About the Team:`; `About the role:`; `How you’ll make an impact:`; `What makes you a good fit:` | bullet-w-period |
| Customer Success Manager, DFR Mid-Market - Northeast *(US Remote)* | Professional Services and Training | `About the Team:`; `About the role:`; `How you’ll make an impact:` | empty-p, bullet-w-period |
| Deployment Engineer - Southeast *(US Remote)* | Professional Services and Training | `About the Team:`; `About the role:`; `How you’ll make an impact:`; `What makes you a good fit:`; `Nice to have:` | empty-p, bullet-w-period |
| Director of Product Management, Drone as First Responder (DFR) *(San Mateo, California, United States)* | Product | `What makes you a good fit:`; `Bonus points for:` | <br> |
| Director, Global Supply Management - Mechanicals *(San Mateo, California, United States)* | Supply Chain & Logistics | `About the role:`; `What you will do:`; `Desired Qualifications:` | empty-p, em-dash |
| Director, Growth Marketing - Commercial *(San Mateo, California, United States)* | Marketing | `About the role:`; `Key Responsibilities:`; `What Success Looks Like:`; `What Would Make You a Good Fit:` | <br>, empty-p, bullet-w-period, bullet-leading-bold, em-dash |
| Electrical Engineer (all levels) *(San Mateo, California, United States)* | Hardware | `About the role:`; `What makes you a good fit:` | <br>, bullet-w-period |
| Electrical Engineer (Sustaining/Validation) *(San Mateo, California, United States)* | Hardware | `About the role:`; `What makes you a good fit:` | <br>, bullet-w-period |
| Engineering Manager - Autonomy *(San Mateo, California, United States)* | Autonomy | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | **extra-class**, <br> |
| Engineering Program Manager *(San Mateo, California, United States)* | Hardware | `About the role`; `How you'll make an impact`; `Program Leadership & Execution`; `Cross-Functional Engineering Integration`; `Supplier & Manufacturing Engagement`; `What makes you a good fit`; `Minimum Qualifications`; `Preferred Qualifications` | **real-heading**, empty-p, bullet-w-period |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Finland) *(Tampere, Finland)* | Sales | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | <br>, em-dash |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Germany) *(Germany)* | Sales | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | <br>, em-dash |
| Enterprise Account Manager (MoD/ MoI) – EMEA (Switzerland) *(Zurich, Switzerland)* | Sales | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | <br>, em-dash |
| Enterprise Account Manager,  US Navy, US Marine Corps, and IC/SOCOM *(US Remote)* | Sales | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | em-dash |
| Enterprise Account Manager, US Army *(US Remote)* | Sales | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | em-dash |
| Equipment and Inventory Specialist (Part Time) *(San Mateo, California, United States)* | Solutions Engineering | _none_ | empty-p, bullet-w-period |
| Field Service Technician *(US CA San Mateo)* | Customer Support | `What would make you a good fit:`; `Nice to have:` | <br>, bullet-w-period |
| Field Support Representative *(US Remote)* | Customer Support | `About the team:`; `About the role:`; `How you’ll make an impact:`; `What makes you a good fit:` | bullet-w-period |
| Field Support Representative (Southwest, Remote) *(US Remote)* | Customer Support | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | empty-p, bullet-w-period, nbsp |
| Field Support Representative - New York *(US NY Remote)* | Customer Support | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | empty-p, bullet-w-period, em-dash |
| Full Stack Product Counsel *(San Mateo, California, United States)* | Legal | `About the Team`; `About the Role`; `How You’ll Make an Impact`; `What Makes You a Great Fit` | **real-heading**, empty-p |
| GTM Enablement Associate *(San Mateo, California, United States)* | Sales | `How you'll make an impact:`; `What makes you a good fit:`; `Preferred Qualifications:` | <br>, empty-p |
| GTM Engineer, Pre-Sales *(US CA San Mateo)* | Sales | `About the Role:`; `How You’ll Make an Impact:`; `Find the right problems to solve`; `Build things that scale`; `Drive adoption, not just delivery`; `What Makes You a Good Fit:`; `You understand how GTM teams work`; `You're a builder with AI fluency`; `You build for scale, not just for now`; `You've got the right instincts`; `Nice To Haves` | **real-heading**, <br>, empty-p, bullet-w-period, em-dash |
| Hardware Operations Program Manager *(Hayward, California, United States)* | Supply Chain & Logistics | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | empty-p, bullet-w-period, bullet-leading-bold |
| IT Technician (Help Desk - Linux Focus) *(Hayward, California, United States)* | IT | _none_ | <br>, empty-p, nested-list, bullet-w-period |
| Lead Staff Electrical Engineer *(San Mateo, California, United States)* | Hardware | `How you'll make an impact:`; `What makes you a good fit:` | <br>, empty-p, bullet-w-period |
| Logistics Operations Specialist, HQ *(San Mateo, California, United States)* | People & Recruiting | `Key Responsibilities`; `1. Logistics Operations & Shipping (≈60%)`; `2. Logistics Coordination & Process Improvement (≈25%)`; `3. Workplace Operations Support (≈15%)`; `Required Qualifications`; `Preferred Qualifications` | **real-heading**, empty-p, bullet-w-period |
| Manager, Logistics *(Hayward, California, United States)* | Manufacturing | `About the role:`; `How you will make an impact:`; `What makes you a good fit:` | empty-p, bullet-w-period |
| Manager, Technical Support *(San Mateo, California, United States)* | Customer Support | `About the team:`; `About the role:`; `How you’ll make an impact:`; `What makes you a good fit:` | bullet-w-period, bullet-leading-bold |
| Manufacturing Execution System Analyst *(Hayward, California, United States)* | Manufacturing Engineering | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | empty-p, bullet-w-period |
| Middleware Software Engineer Intern - Fall 2026 *(San Mateo, California, United States)* | Software | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | empty-p, bullet-w-period |
| Mission Success Operations Manager *(US Remote)* | Professional Services and Training | `About the Team:`; `About the role:`; `How you’ll make an impact:` | nested-list, bullet-w-period |
| Order Management Analyst *(US CA San Mateo)* | Sales | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | empty-p, bullet-w-period |
| PCB Layout Engineer *(San Mateo, California, United States)* | Hardware | `About the role:`; `What makes you a good fit:` | <br>, bullet-w-period |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision *(Zurich, Switzerland)* | Autonomy | `About the role:`; `How you'll make an impact:`; `What makes you a strong fit:` | <br>, nested-list, bullet-leading-bold, nbsp |
| PhD Autonomy Engineer Intern - Deep Learning or Computer Vision *(San Mateo, California, United States)* | Autonomy | `About the role:`; `How you'll make an impact:`; `What makes you a strong fit:` | <br>, nested-list, bullet-leading-bold, nbsp |
| PhD Autonomy Engineer Intern - Planning & Controls (Reinforcement Learning) *(Zurich, Switzerland)* | Autonomy | `About the role:`; `How you'll make an impact:`; `What makes this internship different:`; `What makes you a strong fit:`; `Nice-to-Haves:` | **real-heading**, bullet-w-period, bullet-leading-bold, nbsp, em-dash |
| Product Design Engineer (All Levels) *(San Mateo, California, United States)* | Hardware | `How you'll make an impact:`; `What makes you a good fit:` | <br>, bullet-w-period |
| Product Support Engineer *(San Mateo, California, United States)* | Customer Support | _none_ | <br>, empty-p, bullet-w-period |
| Production Planner, Nightshift *(Hayward, California, United States)* | Manufacturing | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | empty-p, bullet-w-period |
| Program Manager, Commercial Programs *(US AR Remote)* | Professional Services and Training | `What You'll Work On:`; `Requirements:`; `Preferred Qualifications:` | empty-p, bullet-w-period, bullet-leading-bold |
| Program Manager, DFR *(US NY Remote)* | Professional Services and Training | `About the role:`; `How you'll make an impact:`; `What Makes You A Good Fit:` | empty-p, bullet-w-period, bullet-leading-bold |
| Public Safety Strategist (West Coast, Midwest, or Pacific North West) *(US Remote)* | Sales | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | nested-list, bullet-w-period, bullet-leading-bold |
| Revenue Operations Analyst, CPQ *(San Mateo, California, United States)* | Sales | `About the Role:`; `What you’ll drive (scope):`; `Day-to-day responsibilities:`; `Tech stack you’ll work with:`; `What you’ll bring:`; `Reporting & Working Model:` | **real-heading**, <br>, empty-p, bullet-w-period, bullet-leading-bold |
| RF Design Engineer *(San Mateo, California, United States)* | Connectivity | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | bullet-w-period |
| Senior Autonomy Engineer - Controls *(San Mateo, California, United States)* | Autonomy | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | — |
| Senior Autonomy Engineer - Deep Learning *(Zurich, Switzerland)* | Autonomy | `How you'll make an impact:`; `What makes you a good fit:` | <br> |
| Senior Autonomy Engineer - Deep Learning *(San Mateo, California, United States)* | Autonomy | `How you'll make an impact:`; `What makes you a good fit:` | <br>, empty-p |
| Senior Autonomy Engineer, Data Curation *(San Mateo, California, United States)* | Autonomy | `About the Role:`; `How you'll make an impact:`; `What makes you a good fit:`; `Nice to have:` | empty-p, bullet-w-period |
| Senior Business Operations Manager *(San Mateo, California, United States)* | Supply Chain & Logistics | `About the Role:`; `How you'll make an impact:`; `Strategic Sourcing:`; `Cost Management`; `Strategy & Operations`; `What makes you a good fit:` | **real-heading**, empty-p |
| Senior Buyer *(Hayward, California, United States)* | Manufacturing | `About the role:`; `How you will make an impact:`; `What makes you a strong fit:` | **real-heading**, empty-p, bullet-w-period |
| Senior Customer Support Representative - India *(Bangalore, India)* | Customer Support | `About the role:`; `How you’ll make an impact:`; `What would make you a good fit:` | empty-p, bullet-w-period |
| Senior Director, Product Management, Drone as First Responder (DFR) *(San Mateo, California, United States)* | Product | `What makes you a good fit:`; `Bonus points for:` | <br> |
| Senior Engineering Manager, Infrastructure *(San Mateo, California, United States)* | Software | `How you'll make an impact:`; `What makes you a good fit:` | bullet-w-period, bullet-leading-bold |
| Senior Hardware Test and Reliability Engineer *(San Mateo, California, United States)* | Hardware | `About the role:`; `How you will make an impact:`; `Useful skills and experience:` | — |
| Senior Manager, Training *(US Remote)* | Professional Services and Training | `About the role:`; `How you'll make an impact:`; `Desired qualifications:` | <br>, empty-p, bullet-w-period |
| Senior Materials Program Manager *(San Mateo, California, United States)* | Manufacturing | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | empty-p, bullet-w-period |
| Senior NPI Product Quality Engineer *(San Mateo, California, United States)* | Manufacturing | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | — |
| Senior Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | Product | `How you'll make an impact:`; `What would make you a strong fit:` | <br>, empty-p, bullet-w-period, bullet-leading-bold, em-dash |
| Senior Revenue Operations Manager *(San Mateo, California, United States)* | Sales | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:`; `Preferred Qualifications:` | empty-p |
| Senior RF Design Engineer *(San Mateo, California, United States)* | Hardware | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | empty-p, bullet-w-period |
| Senior Software Engineer - Embedded *(San Mateo, California, United States)* | Software | `About the team:`; `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | **extra-class**, bullet-w-period |
| Senior Software Engineer - Mobile Platform *(San Mateo, California, United States)* | Software | `About the Role:`; `About the Team:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:`; `Nice To Haves:` | empty-p, em-dash |
| Senior Software Engineer - Security *(San Mateo, California, United States)* | Security | `About the Role:`; `How you’ll make an impact:`; `What makes you a good fit:`; `Nice to have:` | — |
| Senior Software Engineer,  Data Platform *(San Mateo, California, United States)* | Software | `About the role:`; `Examples of what you’ll help build:`; `How you'll make an impact:`; `What would make you a good fit:` | <br>, bullet-w-period, em-dash |
| Senior Software Engineer,  Infrastructure *(San Mateo, California, United States)* | Software | `How you'll make an impact:`; `What makes you a good fit:`; `Bonus points:` | bullet-w-period |
| Senior Software Engineer, Frontend *(San Mateo, California, United States)* | Software | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:`; `Bonus Points:` | empty-p, bullet-w-period |
| Senior Software Engineer, Full Stack *(San Mateo, California, United States)* | Software | `About the role:`; `How you’ll make an impact:`; `What would make you a good fit:`; `Bonus points for:` | <br>, bullet-w-period, em-dash |
| Senior Technical Recruiter *(San Mateo, California, United States)* | People & Recruiting | `How you'll make an impact:`; `What makes you a good fit:` | **extra-class**, <br>, bullet-leading-bold |
| Senior Technical Recruiter - Hardware Operations *(San Mateo, California, United States)* | People & Recruiting | `What makes you a good fit:` | **extra-class**, <br>, bullet-leading-bold |
| Senior Technical Support Representative - Japan *(Tokyo, Japan)* | Customer Support | `About the role:`; `How you’ll make an impact:`; `What would make you a good fit:` | **real-heading**, <br>, empty-p, bullet-w-period |
| Senior Wireless Software Engineer, National Security *(San Mateo, California, United States)* | Software | `About the team`; `About the role`; `Work location`; `How you’ll make an impact`; `What makes you a good fit`; `Even better` | **real-heading**, <br>, empty-p, bullet-w-period, bullet-leading-bold, em-dash |
| Senior Wireless Systems Performance Engineer *(San Mateo, California, United States)* | Connectivity | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | bullet-w-period, nbsp |
| Senior/Staff Embedded Software Engineer – Camera Systems *(San Mateo, California, United States)* | Software | `About the Role:`; `About the Team:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | empty-p, bullet-w-period |
| Software Engineer - Autonomy Infrastructure, Systems and Tools *(Zurich, Switzerland)* | Autonomy | `About the Role:`; `Areas of Responsibility:`; `What You’ll Do:`; `Qualifications:`; `Bonus Experience:` | **real-heading**, empty-p, bullet-w-period, bullet-leading-bold |
| Software Engineer - Autonomy Infrastructure, Systems and Tools *(San Mateo, California, United States)* | Autonomy | `About the Role:`; `Areas of Responsibility:`; `What You’ll Do:`; `Qualifications:`; `Bonus Experience:` | **real-heading**, empty-p, bullet-w-period, bullet-leading-bold |
| Software Engineer - Cloud Simulation & Full-Stack *(Zurich, Switzerland)* | Autonomy | `About the Role:`; `Areas of Responsibility:`; `What You’ll Do:`; `Qualifications:`; `Bonus Experience:` | **real-heading**, empty-p, bullet-w-period, bullet-leading-bold, em-dash |
| Software Engineer - Cloud Simulation & Full-Stack *(San Mateo, California, United States)* | Autonomy | `About the Role:`; `Areas of Responsibility:`; `What You’ll Do:`; `Qualifications:`; `Bonus Experience:` | **real-heading**, empty-p, bullet-w-period, bullet-leading-bold, em-dash |
| Software Engineer - Embedded *(San Mateo, California, United States)* | Software | `About the team:`; `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | **extra-class**, bullet-w-period |
| Software Engineer - Infrastructure *(San Mateo, California, United States)* | Software | `How you'll make an impact:`; `What makes you a good fit:`; `Bonus points:` | bullet-w-period |
| Software Engineer - Simulation & Robotics Engineer *(Zurich, Switzerland)* | Autonomy | `About the Role:`; `Areas of Responsibility:`; `What You’ll Do:`; `Qualifications:`; `Bonus Experience:` | **real-heading**, empty-p, bullet-w-period, bullet-leading-bold, em-dash |
| Software Engineer - Simulation & Robotics Engineer *(San Mateo, California, United States)* | Autonomy | `About the Role:`; `Areas of Responsibility:`; `What You’ll Do:`; `Qualifications:`; `Bonus Experience:` | **real-heading**, empty-p, bullet-w-period, bullet-leading-bold, em-dash |
| Software Engineer Intern Fall 2026/Winter 2027 *(San Mateo, California, United States)* | Software | `What makes you a good fit:` | <br>, empty-p, bullet-w-period |
| Software Engineer, Full Stack *(San Mateo, California, United States)* | Software | `About the role:`; `How you’ll make an impact:`; `What would make you a good fit:`; `Bonus Points:` | bullet-w-period |
| Sr/Staff Embedded Software Engineer - Camera Systems *(Tampere, Finland)* | Software | `About the Role:`; `About the Team:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | empty-p, bullet-w-period |
| Staff Global Supply Manager,  Mechanicals *(San Mateo, California, United States)* | Supply Chain & Logistics | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | <br>, empty-p, bullet-w-period |
| Staff Product Manager, Platform & Infrastructure *(San Mateo, California, United States)* | Product | `How you'll make an impact:`; `What would make you a strong fit:` | <br>, empty-p, bullet-w-period, bullet-leading-bold, em-dash |
| Staff Software Engineer - Embedded *(San Mateo, California, United States)* | Software | `About the team:`; `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | **extra-class**, bullet-w-period |
| Staff Software Engineer - Security *(San Mateo, California, United States)* | Security | `About the Role:`; `How you’ll make an impact:`; `What makes you a good fit:`; `Nice to have:` | — |
| Staff Software Engineer, Frontend *(San Mateo, California, United States)* | Software | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:`; `Bonus Points:` | empty-p, bullet-w-period |
| Staff Software Engineer, Full Stack *(San Mateo, California, United States)* | Software | `How you’ll make an impact:`; `What would make you a good fit:`; `Bonus points for:` | bullet-w-period, em-dash |
| Staff Technical Recruiter *(San Mateo, California, United States)* | People & Recruiting | `About the role:`; `How you’ll make an impact:`; `What makes you a good fit:` | **extra-class**, bullet-w-period |
| Supplier Quality Engineer, Sustaining *(Taiwan)* | Supply Chain & Logistics | `About the role:`; `How you'll make an impact:`; `What makes you a good fit:` | empty-p, bullet-w-period |
| Supply Chain Intern *(San Mateo, California, United States)* | Supply Chain & Logistics | `About the role:`; `What makes you a good fit:` | <br>, bullet-w-period |
| Systems Integration and Test Engineer (Mid to Senior Level) *(San Mateo, California, United States)* | Hardware | `About the role:`; `How you will make an impact:`; `Useful skills and experience:` | bullet-w-period |
| Wireless Software Engineer *(San Mateo, California, United States)* | Connectivity | `About the Role:`; `How You’ll Make an Impact:`; `What Makes You a Good Fit:` | empty-p, bullet-w-period |
| Workplace Experience Coordinator Part-Time *(Zurich, Switzerland)* | People & Recruiting | `How you’ll make an impact:` | <br>, empty-p, em-dash |

---

## 9. Recommendations for the team

1. **Lock the section-label template.** Every posting body should be exactly:

   ```
   <p>Intro paragraph(s) about Skydio.</p>
   <p><strong>About the role:</strong></p>
   <p>Role description…</p>
   <p><strong>How you'll make an impact:</strong></p>
   <ul><li>…</li>…</ul>
   <p><strong>What makes you a good fit:</strong></p>
   <ul><li>…</li>…</ul>
   <p><strong>Compensation:</strong> …</p>
   ```

2. **Remove real `<h1>`-`<h6>` tags from posting bodies.** Convert any existing heading-tagged section labels to the `<p><strong>` pattern so the labels render at the body font size and weight defined by the design system.
3. **Strip inline `style=` and custom class attributes** from all rich-text content. Visual treatments should live in the global stylesheet for `.prose`.
4. **Adopt one bullet convention:** unordered list, sentence fragment, no trailing period, no leading bold. Update copy where the patterns diverge.
5. **Replace `<br>` tags and empty `<p>` blocks** with the natural vertical rhythm of `<p>`/`<ul>` siblings.
6. **Normalise unicode:** strip non-breaking spaces (`&nbsp;`) and convert em-dashes (`—`) to plain hyphens or en-dashes per style guide.
7. **Lint at publish time.** Add an automated check in the recruiting tool that, before a posting goes live, verifies: (a) all three standard section labels are present and exactly spelled; (b) no inline styles, extra classes, `<br>`, empty `<p>`, `<ol>`, nested lists, or real headings are present; (c) list items conform to the bullet style. The script in this repository (`/workspace/scripts/analyze_jobs.py`) can be the basis for that check.
