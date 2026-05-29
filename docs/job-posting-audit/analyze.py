"""
Skydio careers — job posting formatting audit.

Pulls every published job from the Ashby posting API behind
https://www.skydio.com/careers, truncates each description at the
"Compensation" block, and reports per-job formatting characteristics so
inconsistencies can be reviewed.

Re-run with:  python3 analyze.py
"""

from __future__ import annotations

import csv
import json
import re
import urllib.request
from collections import Counter
from pathlib import Path

API_URL = "https://api.ashbyhq.com/posting-api/job-board/skydio?includeCompensation=true"
OUT_DIR = Path(__file__).parent
RAW_PATH = OUT_DIR / "jobs_api.json"
CSV_PATH = OUT_DIR / "per_job_findings.csv"


def fetch_jobs() -> list[dict]:
    req = urllib.request.Request(
        API_URL,
        headers={"User-Agent": "Mozilla/5.0 (compatible; skydio-job-audit/1.0)"},
    )
    with urllib.request.urlopen(req) as resp:
        payload = json.load(resp)
    RAW_PATH.write_text(json.dumps(payload, indent=2))
    return payload["jobs"]


def truncate_before_compensation(description_html: str) -> str:
    """Return the HTML up to (and not including) the Compensation block."""
    # Most postings open the compensation block with <strong>Compensation
    cut = re.search(r"<[^>]*>\s*<strong>\s*Compensation", description_html, re.IGNORECASE)
    if not cut:
        cut = re.search(r"<strong>\s*Compensation", description_html, re.IGNORECASE)
    return description_html[: cut.start()] if cut else description_html


def analyze(jobs: list[dict]) -> list[dict]:
    rows: list[dict] = []
    for job in jobs:
        pre = truncate_before_compensation(job.get("descriptionHtml", ""))

        h1 = len(re.findall(r"<h1\b", pre))
        h2 = len(re.findall(r"<h2\b", pre))
        h3 = len(re.findall(r"<h3\b", pre))
        h4 = len(re.findall(r"<h4\b", pre))
        strong = len(re.findall(r"<strong\b", pre))
        em = len(re.findall(r"<em\b", pre))
        u = len(re.findall(r"<u\b", pre))
        br = len(re.findall(r"<br\b", pre))
        empty_p = len(re.findall(r"<p[^>]*>\s*</p>", pre))
        multi_br = bool(re.search(r"<br[^>]*>\s*<br", pre))
        div = len(re.findall(r"<div\b", pre))
        # Inline styles that deviate from the canonical "min-height:1.5em"
        odd_styles = [
            m.group(1)
            for m in re.finditer(r'style="([^"]*)"', pre)
            if m.group(1) != "min-height:1.5em"
        ]
        has_strong_p = bool(re.search(r"<p[^>]*>\s*<strong>[^<]+</strong>\s*</p>", pre))

        if h1 or h2 or h3 or h4:
            mode = "mixed" if has_strong_p else "heading-tags"
        elif has_strong_p:
            mode = "p-strong (norm)"
        else:
            mode = "inline (no headers)"

        title = job["title"]
        rows.append(
            {
                "title": title,
                "team": job.get("team") or "",
                "location": job.get("location") or "",
                "mode": mode,
                "h1": h1, "h2": h2, "h3": h3, "h4": h4,
                "strong": strong, "em": em, "u": u,
                "br": br, "multi_br": int(multi_br),
                "empty_p": empty_p,
                "odd_styles": "; ".join(odd_styles),
                "div": div,
                "title_whitespace_issue": int(title != title.strip() or "  " in title),
            }
        )
    return rows


def summarize(rows: list[dict]) -> None:
    modes = Counter(r["mode"] for r in rows)
    print("Heading mode per job:")
    for mode, count in modes.most_common():
        print(f"  {count:>4}  {mode}")


def main() -> None:
    jobs = fetch_jobs()
    rows = analyze(jobs)
    rows.sort(key=lambda r: (r["team"], r["title"]))

    with CSV_PATH.open("w", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {CSV_PATH.relative_to(OUT_DIR.parent)}")
    summarize(rows)


if __name__ == "__main__":
    main()
