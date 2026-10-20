# Stage 13 — Sprint (on-demand, in Claude Code, whenever Jacob has hours)

Purpose: the machine is not only Sunday's. A sprint is an intensive session that advances the pipeline on demand —
one thread to its next gate, a fresh generation pass, a scout pass, or Jacob's inbox — with the same rules, the same
records and the same quality as the scheduled run, and without racing it.

## Modes

- `/sprint <claim-id>` — advance one thread as far as the evidence allows tonight: whatever step is owed next in its
  `THREAD.md` First steps. Owed steps, in order: kill search of the cheapest unsearched probe (`/kill`) → red team
  of a survivor (`/redteam`) → report (`/report`) → the probe itself: a pre-registered run plan with commands, data,
  cost, and the kill criterion written before anything runs; code for the probe goes in `probes/<probe-id>/` with a
  README that states the pre-registration. Stop at the first verdict that closes the thread. Refresh the note after
  every step.
- `/sprint generate` — an extra generation pass on the backlog: trick cards for kept seeds without cards (newest and
  scouts first, within the card budget), `/mutate` on cards with a non-empty `information_asymmetry`, then `/claims`
  for the week so every new probe hangs under a headline or is flagged orphan. No fetch; the backlog is enough.
- `/sprint scout` — fetch the scout stream alone (`python scripts/fetch_arxiv.py --only scout_hf_daily` is not
  supported; run `bash scripts/run_week.sh 3` to refresh the last three days, which is idempotent), triage the new
  scouts on the headline test, write a card for the best one, and say whether any theme now has three scouts.
- `/sprint inbox` — apply Jacob's marks and answer his questions (same as `/inbox`), then refresh the notes.
- `/sprint kill` — run the kill searches that are owed and within budget (claim rank order), nothing else.

## Sync protocol (two operators, one repository)

1. `git pull --rebase origin main` first. Read `data/runs/ACTIVE.json`: if it exists and `started` is under 3 hours
   old, another operator is live — never touch the records in its `scope`; pick another mode or thread, or wait.
   The scheduled runs own Sunday 20:50–23:30 New York time; one-off scheduled runs announce themselves in the lock.
2. Write your own lock: `data/runs/ACTIVE.json` = `{"operator": "sprint <mode> (Jacob's PC)", "started": "<UTC ISO>",
   "scope": [ids you will touch]}`; commit and push it before the first stage.
3. One stage, one commit, one push (`<week>: sprint — <one line>`). Small commits make rebases trivial.
4. A rebase conflict in a `.jsonl` file is resolved by keeping both sides' lines (the files are append-only; the last
   record per id wins) and re-running `python scripts/threads.py`. A conflict in a `.md` note is resolved by
   regenerating the note (`python scripts/threads.py <id>`), since notes are views of the records.
5. Remove the lock in the final commit. If the session dies, the lock expires on its own after 3 hours.
6. Never run `/week` in a sprint (rule 14). A sprint may call any other stage command.

## Conduct

Everything in `CLAUDE.md` holds: scorecard before any proposal, fetched neighbors only, one-sentence tricks,
equations with every symbol defined, status moves only on evidence, ≤ 3 decisions in the final message. Chat is for
one-line status; findings go in the records and the thread notes. Start by printing the thread's six-line brief (or
the backlog counts), end by printing what moved — id, from → to, the gate or verdict — and the decisions.
