#!/usr/bin/env bash
# Start of a working session on Jacob's PC: pull, show whether a run is live, show marks waiting, show the threads index.
# Usage: bash scripts/start.sh
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$ROOT"
if [ -n "$(git status --porcelain)" ]; then
  echo "You have uncommitted changes; committing them first so the pull can rebase cleanly:"
  git add -A && git commit -q -m "$(TZ=America/New_York date +%G-W%V): Jacob — local edits before pull" && echo "  committed."
fi
git pull --rebase origin main
echo
if [ -f data/runs/ACTIVE.json ]; then
  echo "A run holds the lock (stale after 3 h): $(cat data/runs/ACTIVE.json)"; echo
fi
python3 scripts/threads.py --inbox
echo
echo "Threads index: data/threads/README.md  ·  user guide: README.md"
sed -n '/^| Rank/,/^$/p' data/threads/README.md | cut -c1-140
