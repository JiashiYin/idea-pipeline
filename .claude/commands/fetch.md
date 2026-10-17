Run the weekly fetch and queue the triage.

1. Run `bash scripts/run_week.sh` (or, before the orchestrator exists, `python scripts/fetch_arxiv.py --days 7`).
2. Read `data/runs/` for the newest run record and report counts in one line: seeds fetched, new, per query.
3. Print the list of new seed ids and titles for this ISO week, then stop. Do not triage in this command.
