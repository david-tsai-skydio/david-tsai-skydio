#!/usr/bin/env bash
# Download every job posting from https://www.skydio.com/careers and stash the
# raw HTML under $OUT (default: /tmp/skydio_jobs).  The careers landing page is
# server-rendered Astro and references each posting as /jobs/<uuid>.  We harvest
# those UUIDs from the listing page, then fetch each posting page.
set -euo pipefail

UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"
OUT="${SKYDIO_JOBS_DIR:-/tmp/skydio_jobs}"
mkdir -p "$OUT"

curl -fsSL "https://www.skydio.com/careers" -A "$UA" -o "$OUT/_careers.html"

grep -oE 'jobs/[a-f0-9-]{36}' "$OUT/_careers.html" | sort -u > "$OUT/_ids.txt"
total=$(wc -l < "$OUT/_ids.txt")
echo "Found $total unique job postings"

count=0
while read -r path; do
  id="${path##jobs/}"
  [ -s "$OUT/$id.html" ] && continue
  curl -fsSL "https://www.skydio.com/$path" -A "$UA" -o "$OUT/$id.html"
  count=$((count+1))
  [ $((count % 10)) -eq 0 ] && echo "  downloaded $count..."
done < "$OUT/_ids.txt"
echo "Done. $(ls "$OUT"/*.html | wc -l) HTML files in $OUT"
