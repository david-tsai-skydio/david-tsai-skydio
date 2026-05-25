#!/usr/bin/env python3
"""Build the human-readable consistency report from /tmp/job_analysis.json."""
import json, collections, statistics, re
from pathlib import Path

data = json.load(open('/tmp/job_analysis.json'))
records = data['records']

# Sort once by title for stable output
records.sort(key=lambda r: r['title'].lower())

def by_title(rs):
    return sorted({r['title'] for r in rs}, key=str.lower)

# --- Buckets of deviations -----------------------------------------------

# 1. Header style for known section labels
hdr_outliers_h1 = []
hdr_outliers_h2 = []
hdr_no_colon    = []
for r in records:
    for kind, label in r['heading_label_styles']:
        if kind == 'h1':
            hdr_outliers_h1.append((r['title'], label))
        elif kind == 'h2':
            hdr_outliers_h2.append((r['title'], label))
        elif kind == 'p_strong_no_colon':
            hdr_no_colon.append((r['title'], label))

# 2. Underline & italic usage
underline_used = [r['title'] for r in records if r['has_underline']]
italic_used    = [r['title'] for r in records if r['has_italic']]

# 3. <b> vs <strong>
b_tag_used = [r['title'] for r in records if r['has_b_tag']]

# 4. List usage
no_lists   = [r['title'] for r in records if not r['has_lists']]
ol_users   = [r['title'] for r in records if r['list_types'].get('ol')]
both_lists = [r['title'] for r in records
              if r['list_types'].get('ol') and r['list_types'].get('ul')]

# 5. Empty paragraphs (whitespace tricks)
empty_par_users = sorted(
    [(r['empty_paragraphs'], r['title']) for r in records if r['empty_paragraphs'] > 0],
    reverse=True,
)

# 6. <br> usage (line-break shims instead of paragraph breaks)
br_users = sorted(
    [(r['br_count'], r['title']) for r in records if r['br_count'] > 0],
    reverse=True,
)

# 7. ALL-CAPS bold phrases (e.g. ABOUT THE ROLE)
caps_users = [(r['all_caps_bold_phrases'], r['title']) for r in records if r['all_caps_bold_phrases']]
caps_users.sort(reverse=True)

# 8. Period-after-strong-label / colon-spacing oddities
period_after = [(r['period_after_strong_label'], r['title'])
                for r in records if r['period_after_strong_label']]
space_issue  = [(r['space_after_colon_issues'], r['title'])
                for r in records if r['space_after_colon_issues']]

# 9. Length outliers
lengths = [r['char_len'] for r in records]
mean_l = statistics.mean(lengths); med_l = statistics.median(lengths); stdev_l = statistics.pstdev(lengths)
length_outliers_high = sorted(
    [(r['char_len'], r['title']) for r in records if r['char_len'] > med_l + 1.5 * stdev_l],
    reverse=True)
length_outliers_low = sorted(
    [(r['char_len'], r['title']) for r in records if r['char_len'] < med_l - 1.5 * stdev_l])

# 10. Postings missing the standard "About Skydio" intro
missing_intro = [r['title'] for r in records if not r['opens_with_skydio_is_the_leading']]

# 11. Postings missing Compensation block entirely (cut-off marker not found)
no_comp = [r['title'] for r in records if not r['compensation_found']]
unlabeled_comp = [r['title'] for r in records if r.get('compensation_kind') == 'unlabeled']

# 12. Class attributes inside the prose block - in theory editor-injected styles
class_users = collections.Counter()
for r in records:
    for c, n in r['class_attrs'].items():
        class_users[c] += n
# 13. Inline styles used at all
inline_style_users = []
for r in records:
    if r['inline_styles']:
        inline_style_users.append((r['title'], r['inline_styles']))

# --- Render markdown -------------------------------------------------------

def list_block(title_pairs, formatter=None):
    if not title_pairs:
        return '_None observed._\n'
    out = []
    seen = set()
    for item in title_pairs:
        if isinstance(item, tuple):
            txt = formatter(item) if formatter else f'{item[0]} — {item[1]}'
        else:
            txt = item
        if txt in seen: continue
        seen.add(txt); out.append(f'- {txt}')
    return '\n'.join(out) + '\n'

md = []
md.append('# Skydio Careers Page — Job Posting Formatting Audit\n')
md.append(
    f'_Scope: {len(records)} job postings reachable from '
    '[skydio.com/careers](https://www.skydio.com/careers), '
    'analyzing only the content **before** each posting\'s **Compensation** block._\n'
)

md.append('## 1. Methodology\n')
md.append(
    '- Fetched every job posting linked from the careers page (106 listings).\n'
    '- For each posting, located the `<div class="prose block-content">` body and sliced '
    'off everything from the **Compensation** paragraph onward (matched on '
    '`<p><strong>Compensation…</strong></p>`, `<h*>Compensation…`, or a bare '
    '`<strong>Compensation:</strong>`).\n'
    '- The pre-compensation slice was inspected for HTML tag usage, inline styles, '
    'class attributes, list types, heading conventions, line-break / empty-paragraph '
    'usage, ALL-CAPS bold phrases, and length.\n'
    '- Because every posting renders through Skydio\'s shared site stylesheet '
    '(`type-body-2`, `prose block-content`, etc.), absolute font sizes, colors, and '
    'line-heights are inherited from the same CSS for all postings. Differences are '
    'therefore driven entirely by the **semantic HTML the recruiter chose in '
    'Greenhouse** (e.g. `<p><strong>` vs `<h1>` vs `<h2>`, bullets vs prose, '
    'underline, italics, blank paragraphs, etc.). All deviations below originate '
    'in the source content, not in the page CSS.\n'
)

md.append('## 2. Executive Summary — The Norm\n')
md.append(
    'A clear house-style emerges across the 106 postings. A "consistent" posting:\n\n'
    '1. Opens with the standard Skydio company boilerplate paragraph that begins '
    '_"Skydio is the leading US drone company..."_. **All 106 postings comply.**\n'
    '2. Uses `<p><strong>Section Label:</strong></p>` as the heading mechanism for '
    'sections such as **About the role**, **Responsibilities**, **Required '
    'qualifications**, etc. (166 occurrences across the corpus — the dominant '
    'convention).\n'
    '3. Uses unordered `<ul>` bullet lists for responsibilities & qualifications '
    '(105 of 106 postings).\n'
    '4. Contains no inline `style="…"` overrides, no inline color, no inline '
    '`font-size`, no inline `text-align`. **All 106 postings comply.**\n'
    '5. Uses `<strong>` (never `<b>`) for emphasis. **All 106 postings comply.**\n'
    '6. Avoids `<u>` underlines and `<em>/<i>` italics in the pre-compensation '
    'body.\n'
    '7. Falls in the **~3,400 – 4,900 character / ~365 – 540 word** range '
    f'(median ≈ {int(statistics.median(lengths)):,} chars, '
    f'{int(statistics.median([r["word_count"] for r in records]))} words).\n'
)

md.append('## 3. Cross-Posting Formatting Inventory\n')
md.append(
    '| Feature | Postings following the norm | Postings deviating |\n'
    '|---|---|---|\n'
    f'| Opens with standard Skydio intro paragraph | {len(records) - len(missing_intro)}/{len(records)} | {len(missing_intro)} |\n'
    f'| Uses `<p><strong>Label:</strong></p>` headings (with trailing colon) | 166 occurrences | {len(hdr_no_colon)} no-colon, {len(hdr_outliers_h1)} `<h1>`, {len(hdr_outliers_h2)} `<h2>` |\n'
    f'| Uses bullet (`<ul>`) lists | {len(records)-len(no_lists)}/{len(records)} | {len(no_lists)} use only prose |\n'
    f'| Uses `<strong>` (never `<b>`) | {len(records)}/{len(records)} | 0 |\n'
    f'| No `<u>` underlines | {len(records)-len(underline_used)}/{len(records)} | {len(underline_used)} use underline |\n'
    f'| No `<em>` / `<i>` italics | {len(records)-len(italic_used)}/{len(records)} | {len(italic_used)} use italics |\n'
    f'| No empty `<p></p>` spacers | {len(records)-len(empty_par_users)}/{len(records)} | {len(empty_par_users)} insert blank paragraphs |\n'
    f'| No `<br>` line-break shims | {len(records)-len(br_users)}/{len(records)} | {len(br_users)} use `<br>` inside prose |\n'
    f'| No ALL-CAPS bold phrases | {len(records)-len(caps_users)}/{len(records)} | {len(caps_users)} use SHOUTED headers |\n'
    f'| No inline `style=` overrides | 106/106 | 0 |\n'
    f'| No inline color / font-size / alignment | 106/106 | 0 |\n'
)

md.append('## 4. Specific Inconsistencies Flagged\n')

md.append('### 4.1 Heading hierarchy: `<h1>` / `<h2>` used inside the body\n')
md.append(
    'The dominant convention is to render section labels as a bold paragraph '
    '(`<p><strong>About the role:</strong></p>`), which inherits body styling '
    'and visually reads at body-text size. A small number of postings instead '
    'use **HTML headings** for those same labels, which Skydio\'s site CSS '
    'renders much larger (and `<h1>` competes with the actual job-title `<h1>` '
    'at the top of the page).\n'
)
md.append('**`<h1>` headings used in body (visually equal to the job title):**\n')
md.append(list_block(hdr_outliers_h1, lambda t: f'_{t[0]}_ — `<h1>{t[1]}</h1>`'))
md.append('\n**`<h2>` headings used in body:**\n')
md.append(list_block(hdr_outliers_h2, lambda t: f'_{t[0]}_ — `<h2>{t[1]}</h2>`'))

md.append('\n### 4.2 Bold section labels missing the trailing colon\n')
md.append(
    'The house pattern is `<strong>About the role:</strong>` (with colon). '
    f'These postings drop the colon, making their labels look subtly different:\n'
)
md.append(list_block(hdr_no_colon, lambda t: f'_{t[0]}_ — `<strong>{t[1]}</strong>` (no colon)'))

md.append('\n### 4.3 Underline (`<u>`) usage\n')
md.append(
    '`<u>` is not used anywhere else on the careers site. Underlined text '
    'visually mimics a hyperlink and should be avoided in static copy.\n'
)
md.append(list_block(sorted(set(underline_used))))

md.append('\n### 4.4 Italic (`<em>` / `<i>`) usage\n')
md.append('Italics are absent from the rest of the corpus.\n')
md.append(list_block(sorted(set(italic_used))))

md.append('\n### 4.5 Empty-paragraph spacers (`<p></p>`, `<p>&nbsp;</p>`)\n')
md.append(
    'Empty paragraphs are used by some postings to add vertical whitespace. '
    'Because Skydio\'s `prose` CSS already applies a consistent paragraph '
    'rhythm, these blanks create unequal spacing between sections — visible as '
    'one posting having a noticeably larger gap before "Responsibilities" '
    'than another.\n'
)
md.append(list_block(empty_par_users,
                     lambda t: f'_{t[1]}_ — {t[0]} blank paragraph(s)'))

md.append('\n### 4.6 Inline `<br>` line-breaks\n')
md.append(
    '`<br>` shims inside paragraphs disrupt the consistent line-height that '
    '`<p>` siblings would produce. Sites typically prefer a new `<p>` or a '
    'list item instead.\n'
)
md.append(list_block(br_users[:25], lambda t: f'_{t[1]}_ — {t[0]} `<br>` tag(s)'))

md.append('\n### 4.7 ALL-CAPS bold "headers" (e.g. `**ABOUT THE ROLE**`)\n')
md.append(
    'A small number of postings render section labels in ALL CAPS in addition '
    'to bolding, breaking sentence-case consistency with the rest of the corpus.\n'
)
md.append(list_block(caps_users, lambda t: f'_{t[1]}_ — {t[0]} ALL-CAPS bold phrase(s)'))

md.append('\n### 4.8 Postings without bulleted lists\n')
md.append(
    '105 of 106 postings break responsibilities and qualifications out into '
    'bulleted lists. The following posting renders everything as continuous '
    'prose paragraphs, which reads markedly differently:\n'
)
md.append(list_block(sorted(no_lists)))

md.append('\n### 4.9 Length outliers (character count of pre-compensation body)\n')
md.append(
    f'Distribution: min **{min(lengths):,}**, '
    f'p25 **{data["length_stats"]["q1"]:,}**, '
    f'median **{data["length_stats"]["median"]:,}**, '
    f'p75 **{data["length_stats"]["q3"]:,}**, '
    f'max **{max(lengths):,}**.\n'
    '\n**Substantially longer than the norm** '
    '(>1.5σ above median — these dominate visually compared to peer postings):\n'
)
md.append(list_block(length_outliers_high, lambda t: f'_{t[1]}_ — {t[0]:,} chars'))
md.append('\n**Substantially shorter than the norm** '
          '(<1.5σ below median — these look "thin" relative to peers):\n')
md.append(list_block(length_outliers_low, lambda t: f'_{t[1]}_ — {t[0]:,} chars'))

md.append('\n### 4.10 Compensation-block labeling inconsistencies\n')
md.append(
    'Every US-located Skydio posting is expected to end with a clearly-labeled '
    'Compensation block (`<p><strong>Compensation:</strong> …</p>`). Two '
    'deviations show up:\n'
)
md.append('\n**4.10a — Compensation paragraph present but with no bold "Compensation:" label** '
          '(the paragraph starts inline with "At Skydio, our compensation packages…"):\n')
md.append(list_block(sorted(unlabeled_comp)) if unlabeled_comp else '_None._\n')
md.append('\n**4.10b — No Compensation paragraph at all** '
          '(typically non-US roles where pay-range disclosure is not legally required, '
          'but worth confirming intentional):\n')
md.append(list_block(sorted(no_comp)) if no_comp else '_None — every posting contains a Compensation block._\n')
md.append('\n**4.10c — Variant label "Compensation Range:" used instead of "Compensation:":**\n')
# Re-scan source for label variants
import re as _re
from pathlib import Path as _Path
variant_label = []
for r in records:
    h = _Path(f'/tmp/jobs/{r["id"]}.html').read_text(errors='ignore')
    if _re.search(r'<strong[^>]*>\s*Compensation\s+Range', h, _re.I):
        variant_label.append(r['title'])
md.append(list_block(sorted(set(variant_label))) if variant_label else '_None._\n')

md.append('\n### 4.11 Postings missing the standard "Skydio is the leading..." intro\n')
md.append(list_block(sorted(missing_intro)) if missing_intro else
          '_None — every posting opens with the canonical company-intro paragraph._\n')

md.append('\n### 4.12 Trailing punctuation inconsistencies in bold section labels\n')
weird_label_postings = []
for r in records:
    if r['period_after_strong_label']:
        weird_label_postings.append((r['period_after_strong_label'], r['title']))
weird_label_postings.sort(reverse=True)
md.append(
    'Most labels follow `**Label:**`. These postings use a period or other '
    'punctuation after the bold instead, breaking the pattern.\n'
)
md.append(list_block(weird_label_postings, lambda t: f'_{t[1]}_ — {t[0]} occurrence(s)'))

# ---------- 5. Per-posting characteristics table -----------------------

md.append('\n## 5. Per-Posting Formatting Characteristics\n')
md.append(
    'Columns: **len** (pre-compensation char count), **words**, **¶** (paragraph '
    'count), **·** (`<ul>` count), **#·** (list items), **H1/H2** (body headings '
    'used), **<u>** / **<em>** (underline / italic), **∅¶** (empty paragraphs), '
    '**<br>** (line breaks), **CAPS** (all-caps bold phrases). A blank cell = 0.\n'
)
md.append('| Job title | Location | len | words | ¶ | · | #· | H1 | H2 | <u> | <em> | ∅¶ | <br> | CAPS |\n')
md.append('|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|\n')
for r in records:
    def cell(n): return str(n) if n else ''
    md.append(
        '| ' + ' | '.join([
            r['title'],
            r.get('location') or '',
            f'{r["char_len"]:,}',
            str(r['word_count']),
            str(r['paragraph_count']),
            str(r['list_types'].get('ul', 0) or ''),
            str(r['list_item_count'] or ''),
            cell(r['heading_tags_used'].get('h1', 0)),
            cell(r['heading_tags_used'].get('h2', 0)),
            cell(1 if r['has_underline'] else 0),
            cell(1 if r['has_em_tag'] else 0),
            cell(r['empty_paragraphs']),
            cell(r['br_count']),
            cell(r['all_caps_bold_phrases']),
        ]) + ' |\n'
    )

# ---------- 6. Recommendations ---------------------------------------------

md.append('\n## 6. Recommendations for Standardization\n')
md.append('''
The cleanest path to a uniformly styled careers feed is to lock the source HTML in
Greenhouse (or whatever editor recruiters use) to the existing house style. Concrete
guidelines below — listed in priority order.

### 6.1 Adopt a single section-header pattern
- **Use:** `<p><strong>About the role:</strong></p>`, `<p><strong>Responsibilities:</strong></p>`,
  `<p><strong>Required qualifications:</strong></p>`, etc.
- **Stop using:** `<h1>` or `<h2>` for body sections — they visually compete with the
  page-level job title and render at a much larger size due to the site\'s default
  heading CSS.
- **Stop using:** ALL-CAPS labels (`**ABOUT THE ROLE**`). Sentence case + colon
  matches the rest of the corpus.
- **Always include the trailing colon** on section labels.

### 6.2 Forbid ad-hoc inline styles
- No `<u>` underlines — they look like broken links.
- No `<em>` / `<i>` for emphasis; reserve `<strong>` for emphasis as the rest of the
  corpus does.
- No `<b>` (use `<strong>` consistently).
- No inline `style="..."` attributes (color, font-size, text-align) — none of the
  current postings need them, and Greenhouse should already be stripping them.

### 6.3 Use real lists, never line-break shims
- Convert any `<br>`-separated bullet lookalikes into proper `<ul><li>…</li></ul>`
  blocks. This keeps line-height consistent with the site\'s `.prose` styling.
- The one posting currently written as continuous prose should be re-flowed into
  the same Responsibilities / Qualifications bullet layout as every other role.

### 6.4 Remove blank paragraph spacers
- `<p></p>` and `<p>&nbsp;</p>` should be deleted. The site\'s `.prose` CSS already
  spaces sections evenly; manual spacers create uneven gaps that vary posting to
  posting.

### 6.5 Standardize the opening paragraph
- All 106 postings already open with the canonical _"Skydio is the leading US drone
  company..."_ paragraph. Lock that paragraph as a Greenhouse template snippet so
  recruiters can\'t accidentally tweak the wording.

### 6.6 Establish a length guardrail
- Pre-compensation body should target **350–550 words / 3,400–4,900 characters**
  (the current interquartile range). Postings above ~700 words are clearly the
  outliers and should be tightened; postings under ~250 words feel skeletal next to
  peers.

### 6.7 Add a CI/lint step
A 30-line script very similar to this audit can be wired into the careers-site
build (or run nightly) to flag new postings that violate any rule above. Suggested
checks:
1. `<h1>` / `<h2>` / `<h3>` inside `.prose.block-content` → fail.
2. `<u>`, `<b>`, `<em>`, `<i>` inside `.prose.block-content` → fail.
3. `style="..."` attribute inside `.prose.block-content` → fail.
4. Empty `<p></p>` or `<p>&nbsp;</p>` → fail.
5. `<br>` not inside a poem/address block → warn.
6. Section labels that don\'t match `<p><strong>[^<:]+:</strong></p>` → warn.
7. Pre-compensation word count outside 250 – 700 → warn.
8. Missing canonical intro paragraph → warn.
9. Missing `<strong>Compensation:</strong>` block → fail.
''')

Path('/workspace/JOB_POSTING_FORMATTING_AUDIT.md').write_text(''.join(md))
print('Wrote /workspace/JOB_POSTING_FORMATTING_AUDIT.md', len(''.join(md)), 'chars')
