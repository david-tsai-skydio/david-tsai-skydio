#!/usr/bin/env python3
import json
import re
from collections import Counter
from pathlib import Path

data = json.loads(Path(__file__).resolve().parent.parent.joinpath(
    "data/job-formatting-analysis.json"
).read_text())

print("=== Apostrophe style in section headers ===")
straight = curly = 0
straight_jobs = []
curly_jobs = []
mixed_jobs = []
for d in data:
    has_s = False
    has_c = False
    for h in d["bold_pseudo_headings"]:
        if "'" in h:
            has_s = True
        if "\u2019" in h:
            has_c = True
    if has_s and has_c:
        mixed_jobs.append(d["title"])
    elif has_s:
        straight_jobs.append(d["title"])
        straight += 1
    elif has_c:
        curly_jobs.append(d["title"])
        curly += 1
print(f"Jobs using ASCII straight apostrophe only:    {straight}")
print(f"Jobs using Unicode curly apostrophe only:     {curly}")
print(f"Jobs MIXING both in their bold pseudo-headings: {len(mixed_jobs)}")
for t in mixed_jobs:
    print(f"   - {t}")

print("\n=== Double-space typos in title ===")
for d in data:
    if "  " in d["title"]:
        print(f"  - {d['title']!r}  ({d['id']})")

print("\n=== Use of c-link / c-link--underline link classes ===")
with_classes = sum(1 for d in data if d["inline_classes"].get("c-link"))
without_classes = sum(
    1 for d in data
    if d["link_count"] > 0 and not d["inline_classes"].get("c-link")
)
no_links = sum(1 for d in data if d["link_count"] == 0)
print(f"Jobs with links AND c-link class: {with_classes}")
print(f"Jobs with links but NO c-link class: {without_classes}")
print(f"Jobs with no links at all:         {no_links}")

print("\n=== Mixed heading styles (real <h2>/<h3> AND bold pseudo-headings in same job) ===")
for d in data:
    if d["heading_tag_counts"] and d["bold_pseudo_heading_count"] > 0:
        print(f"  - {d['title']}: real={d['heading_tag_counts']}, bold={d['bold_pseudo_heading_count']}")

print("\n=== Jobs that use ONLY real <h*> headings (no bold pseudo-headings) ===")
for d in data:
    if d["heading_tag_counts"] and d["bold_pseudo_heading_count"] == 0:
        print(f"  - {d['title']}: {d['heading_tag_counts']}")

print("\n=== Jobs that use neither real headings NOR bold pseudo-headings ===")
for d in data:
    if not d["heading_tag_counts"] and d["bold_pseudo_heading_count"] == 0:
        print(f"  - {d['title']} ({d['url']})")

print("\n=== Heading-tag level outliers ===")
for d in data:
    if d["heading_tag_counts"].get("h1"):
        print(f"  USES <h1>: {d['title']} - {d['heading_tag_counts']}")

print("\n=== 'About the role' label casing variants ===")
variants = Counter()
for d in data:
    for h in d["bold_pseudo_headings"] + [t for _, t in d["headings_real"]]:
        if h and "about the role" in h.lower():
            variants[h] += 1
for v, c in variants.most_common():
    print(f"  {c:3d}  {v!r}")

print("\n=== 'How you' label variants ===")
variants = Counter()
for d in data:
    for h in d["bold_pseudo_headings"] + [t for _, t in d["headings_real"]]:
        if h and re.match(r"how you", h.lower()):
            variants[h] += 1
for v, c in variants.most_common():
    print(f"  {c:3d}  {v!r}")

print("\n=== 'What makes' label variants ===")
variants = Counter()
for d in data:
    for h in d["bold_pseudo_headings"] + [t for _, t in d["headings_real"]]:
        if h and ("what makes" in h.lower() or "what would make" in h.lower()):
            variants[h] += 1
for v, c in variants.most_common():
    print(f"  {c:3d}  {v!r}")

print("\n=== 'Nice to' label variants ===")
variants = Counter()
for d in data:
    for h in d["bold_pseudo_headings"] + [t for _, t in d["headings_real"]]:
        if h and "nice" in h.lower():
            variants[h] += 1
for v, c in variants.most_common():
    print(f"  {c:3d}  {v!r}")

print("\n=== 'Bonus' label variants ===")
variants = Counter()
for d in data:
    for h in d["bold_pseudo_headings"] + [t for _, t in d["headings_real"]]:
        if h and "bonus" in h.lower():
            variants[h] += 1
for v, c in variants.most_common():
    print(f"  {c:3d}  {v!r}")

print("\n=== <br>-heavy jobs (>=4 <br> tags = noticeable visual irregularity) ===")
br_heavy = [(d['br_count'], d['title']) for d in data if d['br_count'] >= 4]
br_heavy.sort(reverse=True)
for c, t in br_heavy:
    print(f"  br={c}: {t}")

print("\n=== Italic-heavy outlier ===")
for d in data:
    if d['italic_count'] >= 2:
        print(f"  italic={d['italic_count']}: {d['title']}")

print("\n=== Underline usage ===")
for d in data:
    if d['underline_count']:
        print(f"  underline={d['underline_count']}: {d['title']}")
