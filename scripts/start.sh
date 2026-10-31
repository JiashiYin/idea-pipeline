#!/usr/bin/env bash
# Start of a working session on Jacob's PC: get onto main, pull, show whether a run is live, show marks waiting, show the index.
# Usage: bash scripts/start.sh
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$ROOT"
WEEK="$(TZ=America/New_York date +%G-W%V)"
CARRY=""
if [ -n "$(git status --porcelain)" ]; then
  echo "You have uncommitted changes; committing them first so the pull can rebase cleanly:"
  git add -A && git commit -q -m "$WEEK: Jacob — local edits before pull" && CARRY="$(git rev-parse HEAD)" && echo "  committed $CARRY."
fi
BRANCH="$(git branch --show-current)"
if [ "$BRANCH" != "main" ]; then
  echo "You are on branch '$BRANCH', not main. Switching to main; your local edits come along."
  git checkout -q main
  git pull --rebase origin main
  if [ -n "$CARRY" ]; then
    git cherry-pick -q "$CARRY" && echo "  carried your edits ($CARRY) onto main." || { echo "  could not carry $CARRY automatically (conflict). Run: git cherry-pick --abort; then ask Claude or redo the edits on main."; git cherry-pick --abort || true; }
  fi
else
  git pull --rebase origin main
fi
echo
if [ -f data/runs/ACTIVE.json ]; then
  echo "A run holds the lock (stale after 3 h): $(cat data/runs/ACTIVE.json)"; echo
fi
python3 scripts/threads.py --inbox
echo
echo "Threads index: data/threads/README.md  ·  user guide: README.md  ·  branch: $(git branch --show-current)"
sed -n '/^| Rank/,/^$/p' data/threads/README.md | cut -c1-140
