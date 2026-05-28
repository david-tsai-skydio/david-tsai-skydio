#!/usr/bin/env python3
"""Generate a per-job CSV summary of formatting attributes."""
import csv
import json
from pathlib import Path

data = json.loads(Path(__file__).resolve().parent.parent.joinpath(
    "data/job-formatting-analysis.json"
).read_text())

fields = [
    "title",
    "location",
    "type",
    "url",
    "word_count",
    "found_compensation_block",
    "cut_signal",
    "uses_real_headings",
    "real_heading_tag_breakdown",
    "uses_bold_pseudo_headings",
    "bold_pseudo_heading_count",
    "heading_colon_style",
    "paragraph_count",
    "ul_count",
    "ol_count",
    "li_total",
    "br_count",
    "italic_count",
    "underline_count",
    "link_count",
    "uses_c_link_class",
    "inline_style_count",
    "emoji_in_body",
    "section_labels",
]


def colon_style(d):
    w = d["bold_pseudo_headings_with_colon"]
    wo = d["bold_pseudo_headings_without_colon"]
    if w == 0 and wo == 0:
        return "n/a"
    if w and wo:
        return "mixed"
    if w:
        return "all-colon"
    return "no-colon"


outpath = Path("/workspace/data/job-formatting-by-posting.csv")
outpath.parent.mkdir(parents=True, exist_ok=True)
with outpath.open("w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for d in sorted(data, key=lambda x: x["title"].lower()):
        w.writerow({
            "title": d["title"].replace("&amp;", "&"),
            "location": d["location"],
            "type": d["type"],
            "url": d["url"],
            "word_count": d["word_count"],
            "found_compensation_block": d["found_compensation_block"],
            "cut_signal": d["cut_signal"],
            "uses_real_headings": bool(d["heading_tag_counts"]),
            "real_heading_tag_breakdown": ";".join(f"{k}={v}" for k, v in sorted(d["heading_tag_counts"].items())),
            "uses_bold_pseudo_headings": d["bold_pseudo_heading_count"] > 0,
            "bold_pseudo_heading_count": d["bold_pseudo_heading_count"],
            "heading_colon_style": colon_style(d),
            "paragraph_count": d["paragraph_count"],
            "ul_count": d["list_ul_count"],
            "ol_count": d["list_ol_count"],
            "li_total": d["list_li_total"],
            "br_count": d["br_count"],
            "italic_count": d["italic_count"],
            "underline_count": d["underline_count"],
            "link_count": d["link_count"],
            "uses_c_link_class": bool(d["inline_classes"].get("c-link")),
            "inline_style_count": d["inline_style_attr_count"],
            "emoji_in_body": d["emoji_in_body"],
            "section_labels": " | ".join(
                sorted({h.replace("\u2019", "'") for h in d["bold_pseudo_headings"]} |
                       {t for _, t in d["headings_real"] if t})
            ),
        })
print(f"Wrote {outpath}")
