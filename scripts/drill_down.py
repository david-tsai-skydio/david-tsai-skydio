#!/usr/bin/env python3
"""Deeper inconsistency drill-down."""
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROWS = json.loads(Path("/tmp/jobs/parsed/analysis.json").read_text())

def short(t, n=70):
    return t if len(t) <= n else t[:n-1] + "…"

print("="*90)
print(f"TOTAL POSTINGS ANALYZED: {len(ROWS)}")
print("="*90)

# 1. Heading style: which posts use real <h*> tags
print("\n--- 1. SECTION HEADING STYLE ---")
heading_modes = Counter()
for r in ROWS:
    if r.get("headings_via_h_tag", 0) > 0:
        heading_modes["uses <h*> tags"] += 1
    elif r.get("headings_via_bold_p", 0) > 0:
        heading_modes["only <p><strong> pseudo-headings"] += 1
    else:
        heading_modes["no visible section headings"] += 1
print(heading_modes)

print("\nPostings that use real <h*> headings (outliers):")
for r in ROWS:
    if r.get("headings_via_h_tag", 0) > 0:
        tags = [h[0] for h in r["headings"] if h[2] == "heading"]
        print(f"  - [{','.join(sorted(set(tags)))}] {short(r['title'])}  -- {r['location']}")

# 2. Which heading tags used
print("\n--- 2. HEADING TAG DISTRIBUTION ---")
tag_counter = Counter()
for r in ROWS:
    for h in r.get("headings", []):
        if h[2] == "heading":
            tag_counter[h[0]] += 1
print(tag_counter)

# 3. Posts with inline styles
print("\n--- 3. INLINE STYLE OUTLIERS ---")
for r in ROWS:
    if r.get("n_inline_style", 0) > 0 or r.get("n_inline_font_size", 0) > 0 \
       or r.get("n_inline_font_weight", 0) > 0 or r.get("n_inline_color", 0) > 0:
        print(f"  - {short(r['title'])} -- inline_style={r['n_inline_style']} "
              f"font_size={r['n_inline_font_size']} "
              f"font_weight={r['n_inline_font_weight']} ")

# 4. Bold-vs-strong mix
print("\n--- 4. BOLD MARKUP: <strong> vs <b> ---")
both = []
only_b = []
only_s = []
neither = []
for r in ROWS:
    nb, ns = r.get("n_b", 0), r.get("n_strong", 0)
    if nb and ns: both.append(r)
    elif nb: only_b.append(r)
    elif ns: only_s.append(r)
    else: neither.append(r)
print(f"  uses both <b> & <strong>: {len(both)}")
print(f"  uses <b> only:           {len(only_b)}")
print(f"  uses <strong> only:      {len(only_s)}")
print(f"  uses neither:            {len(neither)}")
if only_b:
    print("  Posts using <b> (instead of <strong>):")
    for r in only_b: print(f"    - {short(r['title'])}")
if both:
    print("  Posts mixing <b> and <strong>:")
    for r in both: print(f"    - {short(r['title'])} (b={r['n_b']}, strong={r['n_strong']})")

# 5. List-item structure
print("\n--- 5. LIST ITEM PATTERN ---")
li_with_p = sum(1 for r in ROWS if r.get("n_li", 0) > 0 and r["n_li"] == r["n_li_with_p"])
li_mixed = [r for r in ROWS if r.get("n_li", 0) > 0 and 0 < r["n_li_with_p"] < r["n_li"]]
li_bare = [r for r in ROWS if r.get("n_li", 0) > 0 and r["n_li_with_p"] == 0]
no_li = [r for r in ROWS if r.get("n_li", 0) == 0]
print(f"  all <li> wrapped in <p>: {li_with_p}")
print(f"  all <li> bare (no inner <p>): {len(li_bare)}")
print(f"  mixed pattern within same posting: {len(li_mixed)}")
print(f"  no list items at all: {len(no_li)}")
for r in li_bare:
    print(f"    BARE LI: {short(r['title'])}  (li={r['n_li']}, li_with_p={r['n_li_with_p']})")
for r in li_mixed:
    print(f"    MIXED  : {short(r['title'])}  (li={r['n_li']}, li_with_p={r['n_li_with_p']})")
for r in no_li:
    print(f"    NO LI  : {short(r['title'])}")

# 6. Empty paragraphs / nbsp
print("\n--- 6. EMPTY PARAGRAPHS / NBSP ---")
empties = [r for r in ROWS if r.get("n_empty_p", 0) > 0]
print(f"  Postings with empty <p>: {len(empties)}")
for r in empties:
    print(f"    - {short(r['title'])} (empty_p={r['n_empty_p']})")
nbsps = [r for r in ROWS if r.get("n_nbsp", 0) > 0]
print(f"  Postings with &nbsp;: {len(nbsps)}")
for r in nbsps[:20]:
    print(f"    - {short(r['title'])} (nbsp={r['n_nbsp']})")

# 7. <br> usage
print("\n--- 7. <br> USAGE ---")
brs = [r for r in ROWS if r.get("n_br", 0) > 0]
print(f"  Postings with <br>: {len(brs)}")
for r in brs:
    print(f"    - {short(r['title'])} (br={r['n_br']})")

# 8. Trailing-colon vs no-colon section headers
print("\n--- 8. SECTION HEADER PUNCTUATION ---")
colon = sum(r.get("ends_with_colon_bold", 0) for r in ROWS)
nocolon = sum(r.get("ends_no_colon_bold", 0) for r in ROWS)
print(f"  bold paragraphs ending with ':'   : {colon}")
print(f"  bold paragraphs without trailing ':': {nocolon}")

# Per posting punctuation consistency
mixed_punct = []
for r in ROWS:
    c, nc = r.get("ends_with_colon_bold", 0), r.get("ends_no_colon_bold", 0)
    if c > 0 and nc > 0:
        mixed_punct.append((r["title"], c, nc))
print(f"  Postings that mix colon/no-colon in their own bold headings: {len(mixed_punct)}")
for t, c, nc in mixed_punct[:30]:
    print(f"    - {short(t)} (with_colon={c}, no_colon={nc})")

# 9. Section heading vocabulary
print("\n--- 9. SECTION HEADING VOCABULARY (top 30) ---")
phrase_counter = Counter()
for r in ROWS:
    for h in r.get("headings", []):
        phrase_counter[h[1].lower().strip(' :')] += 1
for p, n in phrase_counter.most_common(35):
    print(f"  {n:4d}  {p}")

# 10. Smart vs straight quotes
print("\n--- 10. SMART vs STRAIGHT QUOTES ---")
both_q = sum(1 for r in ROWS if r.get("n_smart_apostrophe",0) > 0 and r.get("n_straight_apostrophe",0) > 0)
smart_only = sum(1 for r in ROWS if r.get("n_smart_apostrophe",0) > 0 and r.get("n_straight_apostrophe",0) == 0)
straight_only = sum(1 for r in ROWS if r.get("n_smart_apostrophe",0) == 0 and r.get("n_straight_apostrophe",0) > 0)
print(f"  smart only: {smart_only}")
print(f"  straight only: {straight_only}")
print(f"  mixed within same posting: {both_q}")

# 11. Hyperlinks
print("\n--- 11. HYPERLINKS ---")
links = [r for r in ROWS if r.get("n_a", 0) > 0]
print(f"  Postings with <a> links: {len(links)}")
for r in links:
    print(f"    - {short(r['title'])} (a={r['n_a']})")

# 12. Length distribution
print("\n--- 12. PROSE LENGTH ---")
lens = sorted([(r["text_count"], r["title"]) for r in ROWS])
print(f"  shortest 5:")
for tc, t in lens[:5]:
    print(f"    {tc:6d} chars  {short(t)}")
print(f"  longest 5:")
for tc, t in lens[-5:]:
    print(f"    {tc:6d} chars  {short(t)}")

# 13. Per-posting summary CSV-like
out_path = Path("/tmp/jobs/parsed/summary_table.txt")
with out_path.open("w") as f:
    f.write(f"{'TITLE':<70} {'LOC':<35} HTAG  PSTRONG  LI/LIp   BR  NBSP  STYLES\n")
    for r in sorted(ROWS, key=lambda x: x['title']):
        f.write(f"{short(r['title'], 68):<70} {short(r.get('location','')[:34], 34):<35} "
                f"{r.get('headings_via_h_tag',0):>4}  {r.get('headings_via_bold_p',0):>6}  "
                f"{r.get('n_li',0):>3}/{r.get('n_li_with_p',0):<3}  "
                f"{r.get('n_br',0):>3}  {r.get('n_nbsp',0):>4}  {r.get('n_inline_style',0):>5}\n")
print(f"\nSummary table written to {out_path}")
