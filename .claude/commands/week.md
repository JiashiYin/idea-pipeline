Run the full weekly cycle for ISO week $ARGUMENTS (Sunday run; also what the scheduled task executes).
The week label is the ISO week of today's date in America/New_York, never UTC: a Sunday-evening run belongs to the
week that is ending. If $ARGUMENTS is empty, compute it that way.

Read `CLAUDE.md`, `config/themes.yaml`, `config/standards.md`, `config/generation.yaml` first. Then, in order:
0. `git pull --rebase origin main`. If `data/runs/ACTIVE.json` exists and is under 3 hours old, another operator (a
   sprint) is live: do not touch the records in its scope this run and say so in the digest. Write your own lock
   (`{"operator": "weekly run", "started": "<UTC ISO>", "scope": []}`), commit and push it. Then
   `python scripts/threads.py --inbox`: apply every mark Jacob left (`promote`, `jacob-dropped`, `park: <reason>`) to the
   records with a dated history entry, answer his questions in the Log, `--mark-applied` each. His marks win.
1. `/fetch` — `bash scripts/run_week.sh` (arXiv watch and import streams; complaint stream if GitHub access exists).
1b. Banter and inbox (2026-10-30): read `data/inbox/links.md`; for each line fetch the paper's abstract (arXiv API) or
   note it as an idea for `/capture`; then run four to six web searches for arXiv papers argued about this week on the
   Alignment Forum, LessWrong, Hacker News, r/MachineLearning and Zhihu (a Chinese query: 论文 反直觉 OR 出人意料
   强化学习 OR 智能体 OR 仿真 site:zhihu.com), extract arXiv ids, fetch their abstracts, and add them to this week's
   seeds as stream `scout`, source `banter` (inbox lines: source `jacob-banter`). Move processed inbox lines to
   `data/inbox/processed.md` with the verdict. Read at most 15 banter abstracts.
2. `/triage $ARGUMENTS` — against the lanes, with the scout rule (lanes are priorities, not walls: off-lane seeds that
   pass the headline test are kept as L0 scouts, at most `scout_quota_per_week`); record `source` and lane fits on every seed.
3. `/card <id>` for each kept seed, up to 8, newest first; append limitations as complaint seeds.
4. `/crossfield $ARGUMENTS` — 4 imports.
5. `/mutate <id>` for the cards whose `information_asymmetry` field is non-empty, up to 20 candidates total.
6. Monthly only (first run of the month): `/pressure $ARGUMENTS`, `/owned $ARGUMENTS`, `/definitive $ARGUMENTS`.
6b. `/claims $ARGUMENTS` — attach every candidate to a claim or mark it orphan; write and rank claims (top-down pass first).
6c. Concept-level kill searches (`design_after_kill`): one `/kill` per claim that has none yet — promoted claims first, then
   rank order, up to `kill_budget_per_week` — run as parallel subagents, each following prompts/03_kill.md with the
   neighbours' own vocabulary; record the verdict on the claim (killed / parked / survived) with the two closest papers'
   limitation text.
6d. Probe design for survivors only: rewrite or write the cheapest probe with the neighbours in hand (scorecard, pre-registered
   kill, cost), then its probe-level `/kill` if the design changed what is being claimed.
7. (superseded by 6c–6d; kept for records that predate 2026-10-30)
7b. If `auto_redteam` is true in `config/generation.yaml` (it is): `/redteam` on every probe that survived a kill search
   and has no `redteam` block yet, up to `redteam_budget_per_week`, claim rank order; a probe Jacob marked
   `jacob-dropped` is skipped. Record the verdict on the probe and its effect on the claim.
8. `python scripts/threads.py` — refresh every thread note and the threads index (read Jacob's sections first and apply marks).
9. `/digest $ARGUMENTS` — one page, each claim linked to its thread folder, scouts and any proposed lane; remove the
   lock; commit and push.
Budget: ≤ 40 seeds triaged, ≤ 8 cards, ≤ 20 candidates, ≤ 3 kill searches. Stop and write the digest if a stage
fails; a degraded week with a digest beats a complete week without one.
