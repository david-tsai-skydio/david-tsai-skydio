# careers-audit — tooling for the Skydio careers formatting audit

This folder contains the data and analyzer that produced
[`../careers-formatting-audit.md`](../careers-formatting-audit.md).

## Contents

| File | What it is |
|------|------------|
| `job_links.txt` | The 113 unique posting URLs found on https://www.skydio.com/careers (one path per line). |
| `analyze_jobs.py` | Parses each posting's HTML, isolates the pre-compensation body, and emits a per-posting fingerprint plus an aggregate report on stdout. |
| `analysis.json` | The full machine-readable fingerprint dataset (one entry per posting). |
| `per_job_issues.csv` | A flat CSV of per-posting issues, ready for spreadsheet triage. |

## Reproducing the analysis

```bash
# 1. Fetch each posting (about 50 MB of HTML).
mkdir -p /tmp/skydio_jobs
curl -sL https://www.skydio.com/careers \
  | grep -oE 'href="(/jobs/[a-f0-9-]+/?\?gh_jid=[a-f0-9-]+)"' \
  | sed -E 's/href="(.*)"/\1/' | sort -u > /tmp/job_links.txt

while IFS= read -r path; do
  id=$(echo "$path" | grep -oE '[a-f0-9-]{36}' | head -1)
  out="/tmp/skydio_jobs/${id}.html"
  [ -s "$out" ] || curl -sS --max-time 30 "https://www.skydio.com${path}" -o "$out"
done < /tmp/job_links.txt

# 2. Run the analyzer.
SKYDIO_JOBS_DIR=/tmp/skydio_jobs SKYDIO_ANALYSIS_OUT=/tmp/analysis.json \
  python3 analyze_jobs.py
```

The script prints the aggregate findings (heading-tag use, capitalization variants,
empty paragraphs, trailing `<br>`s, ALL-CAPS bolds, missing sections, etc.) and
writes the full fingerprint to `$SKYDIO_ANALYSIS_OUT`.

## Notes on truncation

Each posting's body ends with a `Compensation:` block (sometimes inside the
last `<li>` of a bullet list). `truncate_at_compensation()` finds the first
`<strong>Compensation…</strong>` token and walks back to the start of the
containing block-level element (or to the surrounding `<ul>`/`<ol>` if that
token sits inside a list item) so we only analyze the pre-compensation
content as required by the audit scope.
