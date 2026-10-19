# Idea pipeline — operating manual for Claude Code sessions

This repository is a weekly machine that turns new papers, complaints and cross-field imports into a
small number of pre-argued research candidates for one researcher (Jacob). You are the operator. Jacob's
time is the scarce resource: everything you produce must be high-signal, short, plain, and end with at
most three decisions only he can make.

## The one rule that governs everything

`config/themes.yaml` is the law: lanes (L1–L5) plus the positioning spec (2026-10-17; the proposal is
`config/themes.proposed.yaml` until Jacob renames it). A seed, card or candidate that does not serve a lane is
dropped at triage with one line of reason. Do not widen the lanes yourself; propose a change as a decision.

`config/standards.md` is the second law (2026-10-16): the gates an idea must pass to be called golden,
proper, parked or a thought. Every grading stage names the gate that failed. The bar is all-or-nothing; a
week with zero golden ideas is normal, and the kill record and parked list are that week's output.

## Stages and the files they produce

| Stage | Command | Cadence | Reads | Writes |
| --- | --- | --- | --- | --- |
| 0 Fetch | `/fetch` → `bash scripts/run_week.sh` | weekly | `config/sources.yaml` | `data/seeds/<week>.jsonl`, `data/runs/` |
| 1 Triage | `/triage <week>` | weekly | seeds, lanes | `status`, lane fits, `source` on every seed |
| 2 Card | `/card <arxiv-id>` | weekly, ≤8 | one seed | `data/cards/<id>.json`; limitations → complaint seeds |
| 3 Mutate | `/mutate <id>` | weekly | one card | candidates in `data/candidates/<week>.jsonl` |
| 4 Kill | `/kill <candidate-id>` | ≤3/week | one candidate | kill record; `killed` / `parked` / `survived-kill` |
| 5 Red team | `/redteam <candidate-id>` | as needed | survivor | objection log |
| 6 Report | `/report <candidate-id>` | ≤2/week | survivor | `data/reports/<candidate-id>.md` |
| 6b Pressure | `/pressure <week>` | monthly | system cards, leaderboards, meta-papers, blogs | `data/pressure/<week>/*.jsonl`, `data/reports/<week>-pressure-points.md` |
| 7 Cross-field | `/crossfield <week>` | weekly, 4 | `config/fields.yaml`, `data/crossfield/log.jsonl` | import seeds; the log |
| 8 Owned artifact | `/owned <week>` | monthly | `config/labs.yaml`, parked items | lab-position candidates; `data/owned/<group>.md` |
| 9 Definitive | `/definitive <week>` | monthly | density files, kill reports | lab-position comparison specs |
| 11 Claims | `/claims <week>` | weekly, after mutate | candidates, imports, pressure points | `data/claims/claims.jsonl` — the headline layer; probes attach to claims |
| 10 Digest | `/digest <week>` | weekly, last | all of `data/` | `data/digests/<week>.md`, `ledger/scoreboard.jsonl` |
| — Capture | `/capture <idea>` | ad hoc | conversation | one seed with `source: chat` |
| — Week | `/week <week>` | Sunday | everything above | the whole cycle; what the scheduled task runs |

Run them in order. Never skip Kill before Report. Never write a Report for a candidate that has not
survived a kill search done this week.

## Rules of conduct

1. **Findings go in files, not in chat.** Chat is for one-line status and for the ≤3 decisions.
2. **One-sentence plain trick, always.** Every paper you mention anywhere gets one sentence that strips the
   framing and names the mechanism, plain enough to say in a talk. No paper is referred to by name alone.
3. **Never state a neighbor from memory.** Fetch the abstract (arXiv API or page) before you write about
   it. Conference exports (NeurIPS/ICML/ICLR `Downloads` pages) count as literature; abstracts-only entries
   are marked `abstract-only`.
4. **Equations when a method is explained in depth.** Define every symbol. Prose paraphrases of math are
   not acceptable in cards or reports.
5. **Dated, append-only.** Every record carries a `history` list of `(date, status, note)`. Nothing is
   deleted; superseded entries are marked.
6. **Budget.** A week is: ≤ 40 seeds triaged, ≤ 8 cards, ≤ 20 candidates, ≤ 3 kill searches, ≤ 2 reports.
   If the fetch returns more, triage harder. Quality beats coverage.
7. **Hedging words are banned in reports**: "may", "could potentially", "it is possible that". Say what the
   evidence supports and name the uncertainty with a number or a missing experiment.
8. **No new jargon without a gloss** on first use in any file Jacob reads (cards, reports, ledger).
9. **Every proposal carries the scorecard** (Jacob, 2026-10-14), in chat and in files, before anything else is
   said about it: target value (who asked for it in print, who pays); impact ceiling as three scenarios
   (floor / middle / ceiling) each with what it requires and a stated rough probability; relevance (to each
   advisor route, to industry, to Jacob's own edge; where it is zero); kill probe (the cheapest step that could
   kill it, its cost in dollars and GPU-hours, its criterion, its time); density and ownership (who else, and
   what they have said in their own text); why now (the enabling piece and its date); register and what it is
   not. An idea without a scorecard is a thought, not a proposal.
10. **Commit and push at the end of every run** (2026-10-17). The repo `JiashiYin/idea-pipeline` is the only
    durable home; a cloud session's container is reclaimed and a run that is not pushed did not happen. Commit
    message: `<week>: <stage> — <one line>`; attribution lines as the session requires.
11. **Source and position on everything** (2026-10-17). Every seed carries `source` (watch | complaint |
    pressure | import | owned | definitive | chat); every candidate carries `position` (solo | lab) and its
    verdict per position (standards.md, position clause). The monthly scoreboard is per source.
12. **Portfolio rule.** At least three live seeds in three different lanes at all times. A week may not end on a
    single live thread; if it would, the digest says so and the next generator run is owed before any kill search.
13. **Chat ideas are captured, not debated.** An idea raised in conversation gets `/capture` and a scorecard
    skeleton; it is a thought until its kill search runs. The operator does not elaborate inside the current
    thread for more than one reply without filing it.
14. **One operator per week, pull before you run** (2026-10-18). The Sunday scheduled task owns the weekly cycle
    (`/week`) for the current ISO week; Jacob's PC and web sessions run the marked kill searches, red teams,
    reports and `/capture`, never a second `/week` for the same week. Every session starts with
    `git pull --rebase origin main` and ends with a push; shakedown or experimental output goes on a branch
    (`shakedown-<week>`), not on `main`, so two operators never race on the same files.
15. **Claims over probes** (Jacob, 2026-10-19). The generators produce probes — a control a paper skipped, a
    ruler for one effect — and probes alone read as footnotes. Every candidate names the claim it tests
    (`claim_id`) or is an orphan; the digest ranks claims, then probes; the kill searches run automatically on
    the top probes, claim by claim (`config/generation.yaml`: `auto_kill_monday: true`, `kill_budget_per_week`).
    What is pitched, pursued and called golden is a claim.

## Definitions

**Trick card** (one per kept seed): the paper reduced to what it does.
- `trick`: one plain sentence, mechanism only.
- `framing_stripped`: what the paper calls it vs what it is.
- `load_bearing_assumption`: the assumption that, if false, voids the result.
- `weakest_component`: the part a critic attacks first (a learned probe, a heuristic threshold, a
  single benchmark, an unmatched baseline).
- `regime`: model size, task family, horizon, pass-rate band where it was tested.
- `information_asymmetry`: what information is missing at the stage the method operates in but exists
  at another stage (training vs inference, forward vs hindsight, policy vs environment). This field is
  where ideas come from; fill it with care.
- `occupies`: what is now published and cannot be claimed.

**Mutation operators** (apply each to a card; keep only candidates that serve a theme):
1. Replace the learned or heuristic component with a principled quantity that exists at training time.
2. Move the method to the regime where the missing information exists (inference → training, forward →
   hindsight, policy-only → environment-aware).
3. Change the unit being allocated (tokens → steps → forks → environments → tasks).
4. Turn the mechanism into a measurement instrument (a ruler), and ask what it would grade.
5. Run the compute-matched or dose-matched comparison the paper did not run.
6. Import the other field's standard answer to this problem shape (statistics, control, physics,
   market microstructure, operations research); explain the import in plain words.
7. Invert the role of a signal: a loss weight becomes a sampler decision, a sampler decision becomes a
   measurement, a mechanism becomes a control arm.

**Kill search** (per candidate, before any report): adjacent-territory search with named neighbors and a
one-line difference for each; a "why has this not been done" answer — "an enabling piece landed recently"
is good, "no reason" is a red flag; the cheapest killing experiment and its cost; the result that kills
it. A candidate with no killing experiment under one GPU-week is parked, not reported.

**Red team**: three personas, each must produce objections grounded in fetched evidence, not opinion:
the systems reviewer, the RL-theory reviewer, the professor who dismisses it in ten minutes. Run the
checklist in `prompts/checklist.md`. Iterate generator ↔ red team until the red team has no unanswered
objection or the candidate dies. Every objection and its answer goes in the objection log, conceded ones
included.

**Report** (`schemas/report.md`): eight sections, fixed order, the last one is "Decisions only Jacob can
make", capped at three. Anything that confuses a reader outside section 8 is a protocol bug: fix the
report, then add the confusion to `prompts/checklist.md` so it does not recur.

## Lab map

`config/labs.yaml` is tiered: campus, problem-setters, infra-builders, measurers, reviewers. It grows by
citation expansion from the cards you keep (`scripts/expand_labs.py`), never by listing famous names.
Monthly: promote groups that keep reappearing; mark `verified` only after you have opened a page that
confirms the role.

## What Jacob sees

`ledger/LEDGER.md` (regenerated by `scripts/ledger.py render`) and the reports. He prunes cards and
candidates on Sundays by editing `status` fields; his edits win over yours. If a record has
`status: jacob-dropped`, never revive it without a new reason in `history`.

## What is code and what is an agent

Only `scripts/fetch_arxiv.py` and `scripts/run_week.sh` are code. Every other stage is an agent run from a
slash command in `.claude/commands/`, reading its prompt in `prompts/`. The ledger renderer and the GitHub
complaint fetcher are specified, not built; until they exist the agent does their job by hand and says so.

## Weekly cadence

Sunday: the scheduled cloud task (or Jacob) runs `/week <week>` — fetch, triage, cards, imports, mutate,
(monthly: pressure, owned, definitive), claims, the automatic kill searches on the top probes, the digest,
commit and push. Jacob's hour: read `data/digests/<week>.md`, mark `status: jacob-dropped` or `promote` on
claims and records; his marks win over the automatic ranking.

## Environment notes

- arXiv API: HTTPS, 3-second pause between calls (their policy). Works everywhere.
- Semantic Scholar: free tier is rate-limited; set `S2_API_KEY` for real use; scripts back off and skip
  without it.
- GitHub API: set `GITHUB_TOKEN` or run on a machine with `gh auth`; without either the complaint stream
  is skipped with a note.
- Web pages for conference exports: fetch with the web tools when the shell cannot.
- Reachable from the shell (checked 2026-10-10): `export.arxiv.org/api/query` over HTTPS (http redirects
  301), `huggingface.co/api/...` and dataset files, `raw.githubusercontent.com`. Not reachable: `api.github.com`
  (403 without the session's repo access). `arxiv.org/abs` pages rate-limit (429) after a few fetches in one
  session; use the API with `id_list=` for abstracts and reserve page fetches for full-text limitation sections.
- HAL trajectory zips are encrypted with a password printed in the harness source; decrypt with your own code
  in the scratchpad, never by running the repository's scripts.
