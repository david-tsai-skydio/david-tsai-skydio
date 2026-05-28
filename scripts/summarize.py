#!/usr/bin/env python3
"""Aggregate analyses across all jobs and print key inconsistency signals."""
import json
from collections import Counter, defaultdict
from pathlib import Path
import html as html_mod

data = json.loads(Path(__file__).resolve().parent.parent.joinpath(
    "data/job-formatting-analysis.json"
).read_text())
N = len(data)


def header(s):
    print(f"\n{'='*78}\n{s}\n{'='*78}")


header(f"Corpus stats ({N} jobs)")
print(f"Jobs with detected compensation block: {sum(1 for d in data if d['found_compensation_block'])}")
print(f"Jobs WITHOUT compensation block:        {sum(1 for d in data if not d['found_compensation_block'])}")
print(f"Cut-signal distribution: {Counter(d['cut_signal'] for d in data)}")
print(f"Jobs with canonical intro paragraph:    {sum(1 for d in data if d['has_canonical_intro'])}")
print(f"Jobs WITHOUT canonical intro paragraph: {sum(1 for d in data if not d['has_canonical_intro'])}")

header("Intro paragraph variants (jobs without canonical 'Skydio is the leading' opener)")
non_canon = [d for d in data if not d["has_canonical_intro"]]
seen = set()
for d in non_canon:
    snip = d["intro_first_sentence"][:140]
    if snip in seen:
        continue
    seen.add(snip)
    print(f"  - [{d['title'][:60]}] {snip!r}")

header("Real heading tag use (h1-h6) — should be zero (these jobs use bold paragraphs instead)")
all_real_headings = Counter()
jobs_with_real_headings = []
for d in data:
    for tag, cnt in d["heading_tag_counts"].items():
        all_real_headings[tag] += cnt
    if d["heading_tag_counts"]:
        jobs_with_real_headings.append(d)
print(f"Aggregate heading tag counts: {dict(all_real_headings)}")
print(f"Jobs using <h1>-<h6>: {len(jobs_with_real_headings)}")
for d in jobs_with_real_headings[:20]:
    print(f"  - {d['title']}: {d['heading_tag_counts']}")

header("Inline style attributes (color / font-size / font-family / generic)")
print(f"Jobs with ANY inline style attribute:  {sum(1 for d in data if d['inline_style_attr_count'])}")
print(f"Jobs with inline color: {sum(1 for d in data if d['inline_color_style_count'])}")
print(f"Jobs with inline font-size: {sum(1 for d in data if d['inline_font_size_style_count'])}")
print(f"Jobs with inline font-family: {sum(1 for d in data if d['inline_font_family_style_count'])}")
for d in data:
    if d["inline_style_attr_count"]:
        print(f"  - {d['title']}: {d['inline_style_attr_count']} inline styles, sample={d['inline_styles_sample']}")

header("Italic / underline / <br> / <hr> / image usage")
print(f"Jobs with any italic (<em>/<i>): {sum(1 for d in data if d['italic_count'])}")
print(f"Jobs with any underline (<u>):   {sum(1 for d in data if d['underline_count'])}")
print(f"Jobs with any <br>:              {sum(1 for d in data if d['br_count'])}")
print(f"Jobs with any <hr>:              {sum(1 for d in data if d['hr_count'])}")
print(f"Jobs with any <img>:             {sum(1 for d in data if d['image_count'])}")
print(f"Jobs with emoji:                 {sum(1 for d in data if d['emoji_in_body'])}")
print()
for d in data:
    flags = []
    if d['italic_count']: flags.append(f"italic={d['italic_count']}")
    if d['underline_count']: flags.append(f"underline={d['underline_count']}")
    if d['br_count']: flags.append(f"br={d['br_count']}")
    if d['hr_count']: flags.append(f"hr={d['hr_count']}")
    if d['image_count']: flags.append(f"img={d['image_count']}")
    if d['emoji_in_body']: flags.append("emoji=yes")
    if flags:
        print(f"  - {d['title']}: {', '.join(flags)}")

header("List structure (Greenhouse-style <ul><li><p>... vs plain <li>)")
li_with_p_only = []
li_plain_only = []
li_mixed = []
no_lists = []
for d in data:
    if d['list_li_total'] == 0:
        no_lists.append(d)
    elif d['list_li_with_inner_p'] and not d['list_li_plain']:
        li_with_p_only.append(d)
    elif d['list_li_plain'] and not d['list_li_with_inner_p']:
        li_plain_only.append(d)
    else:
        li_mixed.append(d)
print(f"Jobs with NO bullet list at all:        {len(no_lists)}")
for d in no_lists:
    print(f"     - {d['title']}")
print(f"Jobs using ONLY <li><p>...</p></li>:    {len(li_with_p_only)}")
print(f"Jobs using ONLY plain <li>...</li>:     {len(li_plain_only)}")
for d in li_plain_only[:20]:
    print(f"     - {d['title']}")
print(f"Jobs MIXING both <li> styles:           {len(li_mixed)}")
for d in li_mixed[:30]:
    print(f"     - {d['title']}: plain={d['list_li_plain']}, with_p={d['list_li_with_inner_p']}")

header("Ordered list usage (<ol>) — most jobs should use <ul>")
for d in data:
    if d['list_ol_count']:
        print(f"  - {d['title']}: ol={d['list_ol_count']}")

header("Bold pseudo-heading conventions")
all_section_labels = Counter()
for d in data:
    for h in d['all_section_headers_canon']:
        if h:
            all_section_labels[h] += 1
print("Top 30 normalised section headings across all jobs:")
for label, cnt in all_section_labels.most_common(30):
    print(f"  {cnt:4d}  {label}")

header("Section heading style (does the bold-heading line end with a colon?)")
def colon_style(d):
    w = d['bold_pseudo_headings_with_colon']
    wo = d['bold_pseudo_headings_without_colon']
    if w == 0 and wo == 0:
        return "none"
    if w and wo:
        return "mixed"
    if w:
        return "all-colon"
    return "no-colon"
style_counts = Counter(colon_style(d) for d in data)
print(f"Colon-style distribution across jobs: {dict(style_counts)}")
for d in data:
    if colon_style(d) == "mixed":
        wo_examples = [h for h in d['bold_pseudo_headings'] if not h.rstrip().endswith(":")]
        w_examples = [h for h in d['bold_pseudo_headings'] if h.rstrip().endswith(":")]
        print(f"  MIXED: {d['title']}")
        print(f"     colon:    {w_examples[:3]}")
        print(f"     no-colon: {wo_examples[:3]}")

header("Pseudo-heading punctuation/case oddities (lines using non-standard casing)")
def looks_title_case(s):
    s = s.rstrip(":")
    words = s.split()
    if not words:
        return True
    # Title-case = most non-stopword words start with capital
    skip = {"a","an","and","or","of","the","to","in","on","for","with","at","by","from","as"}
    cap = 0
    total = 0
    for i, w in enumerate(words):
        wt = w.strip(",.")
        if not wt:
            continue
        total += 1
        if i == 0 or wt.lower() not in skip:
            if wt[0:1].isupper():
                cap += 1
    return total > 0 and cap / total >= 0.7

for d in data:
    weird = [h for h in d['bold_pseudo_headings']
             if h and not looks_title_case(h) and len(h.split()) >= 2]
    if weird:
        for w in weird[:3]:
            print(f"  - {d['title']}: {w!r}")

header("Outlier: section labels seen in only ONE job (potential typos / one-offs)")
single_use = [(label, cnt) for label, cnt in all_section_labels.items() if cnt == 1]
print(f"Single-use section labels: {len(single_use)}")
for label, cnt in sorted(single_use):
    print(f"  - {label!r}")

header("Length outliers (word_count of pre-comp body)")
word_counts = [(d['word_count'], d['title']) for d in data]
word_counts.sort()
print("Shortest 10:")
for wc, t in word_counts[:10]:
    print(f"  {wc:5d}  {t}")
print("Longest 10:")
for wc, t in word_counts[-10:]:
    print(f"  {wc:5d}  {t}")

header("Jobs with NO compensation block (the 22 outliers)")
for d in data:
    if not d['found_compensation_block']:
        print(f"  - {d['title']} — {d['url']}")

header("Inline classes detected in body (should typically be empty)")
class_global = Counter()
jobs_with_classes = []
for d in data:
    if d['inline_classes']:
        jobs_with_classes.append(d)
        for c, n in d['inline_classes'].items():
            class_global[c] += n
print(f"Aggregate body classes: {dict(class_global.most_common(20))}")
for d in jobs_with_classes[:10]:
    print(f"  - {d['title']}: {d['inline_classes']}")

header("Paragraph counts (a job uses headings via bold-only paragraphs)")
print("Pseudo-heading counts distribution:")
counts = Counter(d['bold_pseudo_heading_count'] for d in data)
for k in sorted(counts):
    print(f"  count={k}: {counts[k]} jobs")
