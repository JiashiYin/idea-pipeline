#!/usr/bin/env bash
# End of a working session on Jacob's PC: refresh the notes, commit everything, push; rebase once if the remote moved.
# Usage: bash scripts/done.sh "what you did"     (the week label is added for you)
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"; cd "$ROOT"
MSG="${1:-Jacob marks}"
WEEK="$(TZ=America/New_York date +%G-W%V)"
python3 scripts/threads.py >/dev/null || true
git add -A
git diff --cached --quiet || git commit -q -m "$WEEK: Jacob — $MSG"
if ! git push -q origin main 2>/dev/null; then
  echo "remote moved; rebasing once"
  git pull --rebase origin main || { echo "conflict: in a .jsonl keep both sides' lines, in a THREAD.md regenerate (python scripts/threads.py), then: git add -A && git rebase --continue && git push"; exit 1; }
  git push -q origin main
fi
echo "pushed: $(git log --oneline -1)"
