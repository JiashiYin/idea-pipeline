#!/usr/bin/env bash
# Stage 0: fetch the arXiv watch and import streams into this ISO week's seeds file and print the run summary.
# The complaint (GitHub issues) and citation (Semantic Scholar) streams are agent-driven until their fetchers exist;
# the week command handles them. Idempotent: a second run adds zero seeds.
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
DAYS="${1:-7}"
python3 scripts/fetch_arxiv.py --days "$DAYS"
RUN="$(ls -t data/runs/*.json 2>/dev/null | head -1 || true)"
if [ -n "$RUN" ]; then
  python3 - "$RUN" <<'PY'
import json, sys
r = json.load(open(sys.argv[1]))
print("run:", sys.argv[1])
for k in ("week", "seeds_fetched", "seeds_new", "queries_failed"):
    if k in r: print(f"  {k}: {r[k]}")
PY
fi
WEEK="$(python3 -c 'import datetime as d; y,w,_=d.date.today().isocalendar(); print(f"{y}-W{w:02d}")')"
if [ -f "data/seeds/$WEEK.jsonl" ]; then
  echo "seeds in data/seeds/$WEEK.jsonl: $(wc -l < "data/seeds/$WEEK.jsonl")"
fi
