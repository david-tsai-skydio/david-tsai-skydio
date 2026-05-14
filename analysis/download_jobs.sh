#!/bin/bash
mkdir -p jobs
while IFS= read -r url; do
  id=$(echo "$url" | grep -oE '[a-f0-9-]{36}' | head -1)
  if [ ! -s "jobs/$id.html" ]; then
    curl -sL "https://www.skydio.com$url" -o "jobs/$id.html"
  fi
done < job_urls.txt
