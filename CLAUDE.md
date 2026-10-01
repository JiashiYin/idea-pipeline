# Idea pipeline — operating manual for Claude Code sessions

This repository is a weekly machine that turns new papers, complaints and cross-field imports into a
small number of pre-argued research candidates for one researcher (Jacob). You are the operator. Jacob's
time is the scarce resource: everything you produce must be high-signal, short, plain, and end with at
most three decisions only he can make.

## The one rule that governs everything

`config/themes.yaml` is the law. A seed, card or candidate that does not serve a theme is dropped at
triage with one line of reason. Do not widen the themes yourself; propose a change as a decision.

## Stages and the files they produce

| Stage | Command | Reads | Writes |
| --- | --- | --- | --- |
| 0 Fetch | `scripts/run_week.sh` | `config/sources.yaml` | `data/seeds/<week>.jsonl`, `data/complaints/<week>.jsonl` |
| 1 Triage | `/triage <week>` | seeds | `status: kept|dropped` + one-line reason per seed |
| 2 Card | `/card <arxiv-id>` | one seed | `data/cards/<id>.json` (schema: `schemas/card.schema.json`) |
| 3 Mutate | `/mutate <id>` | one card | candidates appended to `data/candidates/<week>.jsonl` |
| 4 Kill | `/kill <candidate-id>` | one candidate | kill record inside the candidate; status `killed` or `survived-kill` |
| 5 Red team | `/redteam <candidate-id>` | survivor | objection log inside the candidate |
| 6 Report | `/report <candidate-id>` | survivor | `data/reports/<candidate-id>.md` (skeleton: `schemas/report.md`) |
| 7 Ledger | `python scripts/ledger.py render` | all jsonl | `ledger/LEDGER.md` |

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

## Environment notes

- arXiv API: HTTPS, 3-second pause between calls (their policy). Works everywhere.
- Semantic Scholar: free tier is rate-limited; set `S2_API_KEY` for real use; scripts back off and skip
  without it.
- GitHub API: set `GITHUB_TOKEN` or run on a machine with `gh auth`; without either the complaint stream
  is skipped with a note.
- Web pages for conference exports: fetch with the web tools when the shell cannot.
