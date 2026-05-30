"""
Analyze Skydio job postings for visual / formatting consistency
in the content that appears BEFORE the Compensation block.

Data source: https://api.ashbyhq.com/posting-api/job-board/skydio
"""

import json, re, os, html as html_lib
from collections import Counter, defaultdict

DATA_FILE = '/tmp/jobs.json'
OUT_DIR = '/workspace/analysis'
os.makedirs(OUT_DIR, exist_ok=True)

with open(DATA_FILE) as f:
    data = json.load(f)
jobs = data['jobs']

# ---------------------------------------------------------------------------
# 1. Truncate each posting at the start of the Compensation block.
#    We try multiple markers because formatting of the Compensation header
#    is itself inconsistent across postings (see report).
# ---------------------------------------------------------------------------

COMP_PATTERNS = [
    # explicit Compensation heading wrapped in <strong> / <b>
    re.compile(r'<p[^>]*>\s*<(?:strong|b)>\s*Compensation', re.I),
    # heading-style Compensation
    re.compile(r'<h[1-6][^>]*>\s*Compensation', re.I),
    # generic "At Skydio our compensation packages" sentence start (some postings)
    re.compile(r'<p[^>]*>\s*Compensation\b', re.I),
    # boiler-plate fallback used by a handful of postings ("Compensation will vary")
    re.compile(r'Compensation will vary based on', re.I),
    re.compile(r'Compensation for certain positions', re.I),
]

def truncate_to_pre_comp(html):
    """Return the HTML up to the start of the compensation block."""
    cut = len(html)
    for pat in COMP_PATTERNS:
        m = pat.search(html)
        if m and m.start() < cut:
            cut = m.start()
    return html[:cut]

# ---------------------------------------------------------------------------
# 2. Extract formatting characteristics from a piece of HTML.
# ---------------------------------------------------------------------------

TAG_RE   = re.compile(r'<(/?)([a-zA-Z0-9]+)([^>]*)>')
STYLE_RE = re.compile(r'style\s*=\s*"([^"]*)"', re.I)
FONT_FAM_RE = re.compile(r'font-family\s*:\s*([^;"]+)', re.I)
FONT_SIZE_RE = re.compile(r'font-size\s*:\s*([^;"]+)', re.I)
COLOR_RE     = re.compile(r'(?<!background-)color\s*:\s*([^;"]+)', re.I)
BG_COLOR_RE  = re.compile(r'background-color\s*:\s*([^;"]+)', re.I)
TEXT_ALIGN_RE = re.compile(r'text-align\s*:\s*([^;"]+)', re.I)
LINE_HEIGHT_RE = re.compile(r'line-height\s*:\s*([^;"]+)', re.I)

def text_of(html):
    text = re.sub(r'<[^>]+>', ' ', html)
    text = html_lib.unescape(text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

def analyze(html):
    """Return a dict of formatting metrics for a snippet of HTML."""
    h = html

    # Heading tag usage
    h_tags = Counter()
    for m in re.finditer(r'<(h[1-6])\b', h, re.I):
        h_tags[m.group(1).lower()] += 1

    # Other tag usage
    tags = Counter()
    for m in TAG_RE.finditer(h):
        closing, name, _ = m.groups()
        if closing:
            continue
        tags[name.lower()] += 1

    # Inline styles
    font_families = Counter()
    font_sizes    = Counter()
    colors        = Counter()
    bg_colors     = Counter()
    text_aligns   = Counter()
    line_heights  = Counter()
    for s in STYLE_RE.findall(h):
        for ff in FONT_FAM_RE.findall(s):
            font_families[ff.strip()] += 1
        for fs in FONT_SIZE_RE.findall(s):
            font_sizes[fs.strip()] += 1
        for c in COLOR_RE.findall(s):
            colors[c.strip().lower()] += 1
        for bc in BG_COLOR_RE.findall(s):
            bg_colors[bc.strip().lower()] += 1
        for ta in TEXT_ALIGN_RE.findall(s):
            text_aligns[ta.strip().lower()] += 1
        for lh in LINE_HEIGHT_RE.findall(s):
            line_heights[lh.strip()] += 1

    # Bold/strong patterns: count <strong>, <b>, and <p><strong>...</strong></p>
    # used as a pseudo-heading.
    strong_count = len(re.findall(r'<strong\b', h, re.I))
    b_count      = len(re.findall(r'<b\b(?!r)', h, re.I))
    em_count     = len(re.findall(r'<em\b', h, re.I))
    i_count      = len(re.findall(r'<i\b(?!nput|frame|mg)', h, re.I))
    u_count      = len(re.findall(r'<u\b(?!l)', h, re.I))

    # Pseudo-headings: a paragraph whose entire visible content is wrapped
    # in <strong> or <b> (a common substitute for an actual heading tag).
    pseudo_headings = []
    for m in re.finditer(
        r'<p[^>]*>\s*(?:<(?:strong|b)>)([^<]{1,120})(?:</(?:strong|b)>)\s*</p>',
        h, re.I):
        pseudo_headings.append(m.group(1).strip())
    # Also <p>**Label:**</p>
    for m in re.finditer(
        r'<p[^>]*>\s*<(?:strong|b)>([^<]{1,120}:)</(?:strong|b)>\s*</p>',
        h, re.I):
        pseudo_headings.append(m.group(1).strip())

    # Section headers, however expressed (real <h?> or pseudo).
    section_headings = []
    for m in re.finditer(r'<(h[1-6])\b[^>]*>(.*?)</\1>', h, re.I | re.S):
        section_headings.append((m.group(1).lower(), text_of(m.group(2))[:80]))
    for ph in pseudo_headings:
        section_headings.append(('pseudo', ph[:80]))

    # Lists
    ul = len(re.findall(r'<ul\b', h, re.I))
    ol = len(re.findall(r'<ol\b', h, re.I))
    li = len(re.findall(r'<li\b', h, re.I))

    # Paragraphs
    p_count   = len(re.findall(r'<p\b', h, re.I))
    br_count  = len(re.findall(r'<br\b', h, re.I))

    # Empty/whitespace paragraphs (used as spacers)
    empty_p   = len(re.findall(r'<p[^>]*>\s*(?:&nbsp;|\xa0)?\s*</p>', h, re.I))

    # min-height usage (Ashby default)
    min_height_p = len(re.findall(r'<p[^>]*style="min-height:1\.5em"', h, re.I))

    # Trailing-colon vs no-colon section label style
    colon_labels = sum(1 for x in pseudo_headings if x.rstrip().endswith(':'))
    nocolon_labels = sum(1 for x in pseudo_headings
                         if not x.rstrip().endswith(':'))

    return {
        'length_chars': len(h),
        'word_count':   len(text_of(h).split()),
        'h_tags':       dict(h_tags),
        'tags':         dict(tags),
        'font_families':dict(font_families),
        'font_sizes':   dict(font_sizes),
        'colors':       dict(colors),
        'bg_colors':    dict(bg_colors),
        'text_aligns':  dict(text_aligns),
        'line_heights': dict(line_heights),
        'strong_count': strong_count,
        'b_count':      b_count,
        'em_count':     em_count,
        'i_count':      i_count,
        'u_count':      u_count,
        'pseudo_headings': pseudo_headings,
        'section_headings': section_headings,
        'ul': ul, 'ol': ol, 'li': li,
        'p_count': p_count, 'br_count': br_count,
        'empty_p': empty_p,
        'min_height_p': min_height_p,
        'colon_labels': colon_labels,
        'nocolon_labels': nocolon_labels,
    }

# ---------------------------------------------------------------------------
# 3. Run analysis over every job posting.
# ---------------------------------------------------------------------------

results = []
for j in jobs:
    html = j['descriptionHtml']
    pre  = truncate_to_pre_comp(html)
    info = analyze(pre)
    info['id']        = j['id']
    info['title']     = j['title']
    info['team']      = j.get('team')
    info['department']= j.get('department')
    info['location']  = j.get('location')
    info['url']       = j.get('jobUrl')
    info['pre_html']  = pre
    results.append(info)

with open(os.path.join(OUT_DIR, 'per_job_metrics.json'), 'w') as f:
    # strip pre_html for slimmer file
    slim = [{k:v for k,v in r.items() if k!='pre_html'} for r in results]
    json.dump(slim, f, indent=2)

print('Analyzed', len(results), 'jobs')
print('Wrote per_job_metrics.json')

# ---------------------------------------------------------------------------
# 4. Aggregate / cross-posting comparison.
# ---------------------------------------------------------------------------

def field_counter(field, list_field=False):
    c = Counter()
    for r in results:
        v = r[field]
        if isinstance(v, dict):
            for k, n in v.items():
                c[k] += n
        elif list_field:
            for x in v:
                c[x] += 1
        else:
            c[v] += 1
    return c

print('\n=== Font sizes used (inline style) ===')
print(field_counter('font_sizes'))
print('\n=== Font families used (inline style) ===')
print(field_counter('font_families'))
print('\n=== Text colors used (inline style) ===')
print(field_counter('colors'))
print('\n=== Background colors used (inline style) ===')
print(field_counter('bg_colors'))
print('\n=== Text alignments used (inline style) ===')
print(field_counter('text_aligns'))
print('\n=== Line-heights used (inline style) ===')
print(field_counter('line_heights'))
print('\n=== Heading tags used ===')
print(field_counter('h_tags'))

# How many jobs have any real <h?> tag at all?
h_users = [r for r in results if r['h_tags']]
no_h = [r for r in results if not r['h_tags']]
print(f"\nJobs using >=1 real <h?> tag: {len(h_users)}")
print(f"Jobs using NO real heading tag (all pseudo): {len(no_h)}")

# Pseudo-headings: how many jobs use them, and at what counts?
psh_users = [r for r in results if r['pseudo_headings']]
print(f"\nJobs using >=1 pseudo (bold-only) heading: {len(psh_users)}")

# Mixed: jobs using BOTH real and pseudo headings (inconsistent within posting).
mixed = [r for r in results if r['h_tags'] and r['pseudo_headings']]
print(f"Jobs mixing real <h?> AND pseudo headings: {len(mixed)}")

# Distribution of italic / underline / em / b usage
print('\n=== Inline emphasis counts (jobs using any) ===')
print('  <strong>:', sum(1 for r in results if r['strong_count']))
print('  <b>     :', sum(1 for r in results if r['b_count']))
print('  <em>    :', sum(1 for r in results if r['em_count']))
print('  <i>     :', sum(1 for r in results if r['i_count']))
print('  <u>     :', sum(1 for r in results if r['u_count']))

# Length distribution
lens = sorted(r['word_count'] for r in results)
n = len(lens)
print(f"\nPre-compensation word count: min={lens[0]} p25={lens[n//4]} median={lens[n//2]} p75={lens[3*n//4]} max={lens[-1]}")

# Save outliers
