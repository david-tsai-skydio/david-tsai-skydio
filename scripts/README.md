# Skydio careers — job-posting formatting audit scripts

These scripts produce [`JOB_POSTING_FORMATTING_AUDIT.md`](../JOB_POSTING_FORMATTING_AUDIT.md).

## How to re-run

```bash
mkdir -p /tmp/jobs
# 1. Pull the careers index and extract job IDs
curl -s -L https://www.skydio.com/careers -o /tmp/careers.html
python3 -c "import re; ids=set(re.findall(r'/jobs/([a-f0-9-]{36})/', open('/tmp/careers.html').read())); open('/tmp/job_ids.txt','w').write('\n'.join(sorted(ids)))"

# 2. Download every job posting (parallel)
cd /tmp/jobs && cat /tmp/job_ids.txt | xargs -I{} -P 16 sh -c \
  'test -s "{}.html" || curl -s -L "https://www.skydio.com/jobs/{}/" -o "{}.html"'

# 3. Build the analysis and the report
python3 scripts/analyze.py        # writes /tmp/job_analysis.json
python3 scripts/report_build.py   # writes JOB_POSTING_FORMATTING_AUDIT.md
```

## What is analyzed

For each posting the script slices the body content inside
`<div class="prose block-content">` up to (and **not** including) the
**Compensation** paragraph, then collects per-posting:

- HTML tag census (paragraphs, headings, lists, list items, breaks, links, etc.)
- Use of inline `style="…"`, color, font-size, text-align
- Use of `<u>`, `<em>` / `<i>`, `<b>`, `<strong>`
- Empty `<p></p>` / `<p>&nbsp;</p>` spacers and bare `<br>` tags
- ALL-CAPS bold "shouted" headers
- Section-heading wrapper style (`<p><strong>Label:</strong></p>` vs `<h1>` /
  `<h2>` / no-colon variants)
- Character / word count length
- Whether the posting opens with Skydio's canonical company-intro paragraph
- Whether/how the Compensation block is labeled

`report_build.py` then computes the dominant pattern (the "norm"), flags every
deviating posting, and emits a single markdown report.
