#!/bin/bash
id="$1"; url="$2"
if [ ! -s "jobs/$id.html" ]; then
  curl -sL "https://www.skydio.com$url" -o "jobs/$id.html"
fi
