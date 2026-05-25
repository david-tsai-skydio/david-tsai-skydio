#!/usr/bin/env python3
"""Analyze formatting characteristics of Skydio job postings up to the Compensation block."""
import os, re, json, collections, html as html_mod
from pathlib import Path

JOBS_DIR = Path('/tmp/jobs')

# ---------- 1. Per-posting extraction ----------

TITLE_RE = re.compile(r'<h1 class="type-h2">([^<]+)</h1>')
LOC_RE = re.compile(r'<h1 class="type-h2">[^<]+</h1>\s*<p class="type-body-2">\s*([^<]+?)\s*</p>', re.S)
# The job description sits inside <div class="prose block-content"> ... </div> immediately following.
PROSE_RE = re.compile(
    r'<div class="prose block-content">\s*(.*?)\s*</div>\s*</stack-l>',
    re.S,
)

# Patterns for the compensation cut-off. Several variants observed.
COMP_PATTERNS_LABELED = [  # explicit "Compensation" / "Compensation Range" label
    re.compile(r'<p[^>]*>\s*(?:<br[^>]*>\s*)?<strong[^>]*>\s*Compensation\b', re.I),
    re.compile(r'<p[^>]*>\s*<b[^>]*>\s*Compensation\b', re.I),
    re.compile(r'<h[1-6][^>]*>\s*Compensation\b', re.I),
    re.compile(r'<strong[^>]*>\s*Compensation(?:\s+Range)?\s*:?\s*</strong>', re.I),
]
# Fallback: postings where the compensation paragraph has no bold label and just
# starts with "At Skydio, our compensation packages…".
COMP_PATTERNS_UNLABELED = [
    re.compile(r'<p[^>]*>\s*At Skydio, our compensation packages\b', re.I),
    re.compile(r'<p[^>]*>\s*The (?:annual|hourly) base salary range\b', re.I),
]

def find_compensation_split(prose_html: str, allow_fallback: bool = True):
    earliest = None
    for p in COMP_PATTERNS_LABELED:
        m = p.search(prose_html)
        if m and (earliest is None or m.start() < earliest):
            earliest = m.start()
    if earliest is not None:
        return earliest, 'labeled'
    if allow_fallback:
        for p in COMP_PATTERNS_UNLABELED:
            m = p.search(prose_html)
            if m and (earliest is None or m.start() < earliest):
                earliest = m.start()
        if earliest is not None:
            return earliest, 'unlabeled'
    return None, None

def get_title_location_and_pre(html_text: str):
    title_m = TITLE_RE.search(html_text)
    title = html_mod.unescape(title_m.group(1)).strip() if title_m else None
    loc_m = LOC_RE.search(html_text)
    location = ' '.join(html_mod.unescape(loc_m.group(1)).split()) if loc_m else None
    prose_m = PROSE_RE.search(html_text)
    if not prose_m:
        return title, location, None, None
    prose = prose_m.group(1)
    split, kind = find_compensation_split(prose)
    pre = prose[:split] if split is not None else prose
    return title, location, pre, prose, kind

# ---------- 2. Formatting characterizations ----------

TAG_RE = re.compile(r'<(/?)([a-zA-Z][a-zA-Z0-9]*)([^>]*)>')
STYLE_ATTR_RE = re.compile(r'\bstyle\s*=\s*"([^"]*)"', re.I)
CLASS_ATTR_RE = re.compile(r'\bclass\s*=\s*"([^"]*)"', re.I)

# Common section labels - we want to detect heading conventions
SECTION_LABELS = [
    'about skydio', 'about the role', 'about the team', 'about the job',
    'about us', 'about you', 'about the company',
    'responsibilities', 'requirements', 'qualifications',
    'what you', 'how you', 'why you', 'why skydio',
    'minimum qualifications', 'preferred qualifications',
    'nice to have', 'bonus', 'benefits', "what you'll do",
    'who you are', 'what we offer', 'a day in the life',
    'role overview', 'role responsibilities', 'role qualifications',
    'key responsibilities', 'job description',
]
HEADING_HINT_RE = re.compile(r'(' + '|'.join(re.escape(s) for s in SECTION_LABELS) + r')', re.I)

def text_of(html_text: str) -> str:
    return html_mod.unescape(re.sub(r'<[^>]+>', '', html_text))

def analyze_pre(pre: str):
    """Return a dict of formatting characteristics."""
    info = {
        'char_len': len(pre),
        'word_count': len(text_of(pre).split()),
        'tag_counts': collections.Counter(),
        'heading_tags_used': collections.Counter(),
        'inline_styles': [],
        'class_attrs': collections.Counter(),
        'colon_strong_labels': [],       # like "<p><strong>About the role:</strong></p>"
        'heading_label_styles': [],      # how each known section label is wrapped
        'has_lists': False,
        'list_types': collections.Counter(),
        'list_item_count': 0,
        'br_count': 0,
        'empty_paragraphs': 0,
        'paragraph_count': 0,
        'orphan_text': False,
        'has_color_style': False,
        'has_font_size_style': False,
        'has_inline_align': False,
        'has_underline': False,
        'has_italic': False,
        'has_em_tag': False,
        'has_b_tag': False,
        'starts_with_about_skydio_boilerplate': False,
        'opens_with_skydio_is_the_leading': False,
        'links': 0,
        'images': 0,
        'all_caps_bold_phrases': 0,
        'mixed_list_in_paragraph': 0,
        'trailing_colons_after_strong': 0,
        'period_after_strong_label': 0,
        'space_after_colon_issues': 0,
    }
    # tag census
    for m in TAG_RE.finditer(pre):
        closing, tag, attrs = m.groups()
        tag = tag.lower()
        if closing:
            continue
        info['tag_counts'][tag] += 1
        if re.fullmatch(r'h[1-6]', tag):
            info['heading_tags_used'][tag] += 1
        if tag in ('ul','ol'):
            info['has_lists'] = True
            info['list_types'][tag] += 1
        if tag == 'li':
            info['list_item_count'] += 1
        if tag == 'br':
            info['br_count'] += 1
        if tag == 'p':
            info['paragraph_count'] += 1
        if tag == 'a':
            info['links'] += 1
        if tag == 'img':
            info['images'] += 1
        if tag == 'u':
            info['has_underline'] = True
        if tag in ('i','em'):
            info['has_italic'] = True
        if tag == 'em':
            info['has_em_tag'] = True
        if tag == 'b':
            info['has_b_tag'] = True
        # attributes
        sm = STYLE_ATTR_RE.search(attrs)
        if sm:
            style = sm.group(1).lower()
            info['inline_styles'].append((tag, sm.group(1).strip()))
            if 'color' in style and 'background' not in style:
                info['has_color_style'] = True
            if 'font-size' in style:
                info['has_font_size_style'] = True
            if 'text-align' in style:
                info['has_inline_align'] = True
        cm = CLASS_ATTR_RE.search(attrs)
        if cm:
            for c in cm.group(1).split():
                info['class_attrs'][c] += 1

    # Empty paragraphs (spacing tricks)
    info['empty_paragraphs'] = len(re.findall(r'<p[^>]*>\s*(?:&nbsp;|\u00a0|<br\s*/?>)?\s*</p>', pre, re.I))

    # Boilerplate intro check
    plain = text_of(pre).strip()
    info['opens_with_skydio_is_the_leading'] = plain.lower().startswith('skydio is the leading')

    # Section heading wrappers: look at how each known label is wrapped
    # Pattern: <p[^>]*>\s*<strong>About the role:?</strong>\s*</p>
    label_wrap_patterns = {
        'p_strong_with_colon':    re.compile(r'<p[^>]*>\s*<strong[^>]*>\s*([^<:]+):\s*</strong>\s*</p>', re.I),
        'p_strong_no_colon':      re.compile(r'<p[^>]*>\s*<strong[^>]*>\s*([^<:]+?)\s*</strong>\s*</p>', re.I),
        'p_b_with_colon':         re.compile(r'<p[^>]*>\s*<b[^>]*>\s*([^<:]+):\s*</b>\s*</p>', re.I),
        'h1': re.compile(r'<h1[^>]*>\s*([^<]+?)\s*</h1>', re.I),
        'h2': re.compile(r'<h2[^>]*>\s*([^<]+?)\s*</h2>', re.I),
        'h3': re.compile(r'<h3[^>]*>\s*([^<]+?)\s*</h3>', re.I),
        'h4': re.compile(r'<h4[^>]*>\s*([^<]+?)\s*</h4>', re.I),
        'h5': re.compile(r'<h5[^>]*>\s*([^<]+?)\s*</h5>', re.I),
        'h6': re.compile(r'<h6[^>]*>\s*([^<]+?)\s*</h6>', re.I),
    }
    for kind, pat in label_wrap_patterns.items():
        for lm in pat.finditer(pre):
            label_text = lm.group(1).strip()
            if HEADING_HINT_RE.search(label_text):
                info['heading_label_styles'].append((kind, label_text))

    # Inline-bold labels at the start of a sentence inside a paragraph, e.g.
    # <p><strong>Role:</strong> some text...</p>  (these *don't* sit alone)
    for inline in re.finditer(r'<p[^>]*>\s*<strong[^>]*>\s*([^<:]{2,60}):\s*</strong>\s*([^<])', pre):
        info['trailing_colons_after_strong'] += 1
    for inline in re.finditer(r'<strong[^>]*>\s*([^<:]{2,60})\.\s*</strong>', pre):
        info['period_after_strong_label'] += 1
    # "About the role: text" (no space after colon)
    for inline in re.finditer(r'</strong>:[^\s<]', pre):
        info['space_after_colon_issues'] += 1

    # ALL CAPS BOLD phrases
    for m in re.finditer(r'<strong[^>]*>\s*([A-Z][A-Z\s&/\-]{3,})\s*</strong>', pre):
        info['all_caps_bold_phrases'] += 1

    return info


# ---------- 3. Run over all postings ----------

records = []
missing = []
for f in sorted(JOBS_DIR.glob('*.html')):
    html_text = f.read_text(errors='ignore')
    title, location, pre, full, comp_kind = get_title_location_and_pre(html_text)
    if not title or pre is None:
        missing.append(f.name)
        continue
    info = analyze_pre(pre)
    records.append({
        'id': f.stem,
        'title': title,
        'location': location,
        'pre_present': True,
        'compensation_kind': comp_kind,  # 'labeled' | 'unlabeled' | None
        'compensation_found': comp_kind is not None,
        **info,
    })

print(f'Analyzed: {len(records)}    Missing/unparsable: {len(missing)}')
if missing:
    print('Missing files:', missing[:5], '...')

# ---------- 4. Compute norms and flag deviations ----------

def majority(values):
    c = collections.Counter(values)
    return c.most_common(1)[0]  # (val, count)

# Tag-use distribution
features = [
    ('has_lists', 'no/has lists'),
    ('has_color_style', 'inline color style'),
    ('has_font_size_style', 'inline font-size style'),
    ('has_inline_align', 'inline text-align'),
    ('has_underline', '<u> tag used'),
    ('has_italic', 'italic styling'),
    ('has_b_tag', '<b> tag used'),
    ('opens_with_skydio_is_the_leading', 'opens with Skydio boilerplate'),
]
norms = {}
for feat, _ in features:
    norms[feat] = collections.Counter(r[feat] for r in records).most_common()

heading_pattern_by_post = []
for r in records:
    # Determine dominant heading style used for known section labels in this posting
    styles_used = collections.Counter(k for k, _ in r['heading_label_styles'])
    heading_pattern_by_post.append((r['id'], r['title'], styles_used))

# Global popularity of heading-label wrappers
all_label_styles = collections.Counter()
for _, _, sc in heading_pattern_by_post:
    for k, n in sc.items():
        all_label_styles[k] += n

# Lengths
lengths = [r['char_len'] for r in records]
words = [r['word_count'] for r in records]

def quartiles(xs):
    s = sorted(xs)
    n = len(s)
    if n == 0:
        return (0, 0, 0, 0, 0)
    def pct(p):
        i = int(round(p * (n-1)))
        return s[i]
    return (s[0], pct(0.25), pct(0.5), pct(0.75), s[-1])

print('len min/q1/med/q3/max:', quartiles(lengths))
print('word min/q1/med/q3/max:', quartiles(words))
print('heading-label styles used globally:', all_label_styles)
print('feature norms:')
for k, c in norms.items():
    print(' ', k, '->', c)

# Save raw records for the report-building step
out = {
    'records': records,
    'norms': {k: v for k, v in norms.items()},
    'heading_label_styles_global': dict(all_label_styles),
    'length_stats': dict(zip(
        ['min','q1','median','q3','max'], quartiles(lengths))),
    'word_stats': dict(zip(
        ['min','q1','median','q3','max'], quartiles(words))),
    'missing': missing,
}
# Counters aren't JSON-serializable; convert
def normalize(o):
    if isinstance(o, collections.Counter):
        return dict(o)
    if isinstance(o, dict):
        return {k: normalize(v) for k, v in o.items()}
    if isinstance(o, list):
        return [normalize(x) for x in o]
    if isinstance(o, tuple):
        return [normalize(x) for x in o]
    return o
with open('/tmp/job_analysis.json','w') as f:
    json.dump(normalize(out), f, indent=2)
print('Wrote /tmp/job_analysis.json')
