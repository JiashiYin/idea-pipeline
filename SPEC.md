# Idea pipeline — system specification

Version 0.1 · 2026-10-01 · for a Claude Code session to build from, in Jacob's workspace.

This document specifies a research-idea discovery machine for one researcher. It is written so that a
coding agent can build it without further design conversation. Where a choice is open, the default is
stated and marked **(default)**; the builder takes the default and lists the choice in `DECISIONS.md`.

---

## 1. Purpose and the two bottlenecks it is built around

The machine turns a weekly stream of new papers, practitioner complaints and cross-field imports into a
small number of **pre-argued** research candidates that serve one or two named themes.

It is designed around two facts about its user:

1. **His review time is the scarce resource.** Every artifact he reads must be short, plain, and end with
   at most three decisions only he can make. Argument happens inside the machine (generator ↔ red team),
   not in his inbox.
2. **He is new to the field.** The map of who matters is not an input he can supply; the machine builds it
   by citation expansion from what it keeps, and maintains it.

A third fact about the field: the public auto-research systems (see `LANDSCAPE.md`) show that idea *volume*
is cheap and that broader exploration did not produce better papers. The scarce goods are differentiated
seeds, fast and well-sourced kills, and positioning against neighbors. The machine spends its compute there.

### Non-goals

- It does not write papers or run training experiments end to end. It stops at a report with a killing
  experiment specified. (A later module, §12, hooks an experiment harness.)
- It does not browse social feeds. X/Rednote are a low-weight manual input, not a stream.
- It does not optimize for novelty scores. It optimizes for candidates that survive a sourced kill search
  and a three-persona red team, and that Jacob approves.

---

## 2. Architecture at a glance

```
                     config/themes.yaml  (the law: 1–2 theme sentences + keywords)
                              │
   ┌──────────── streams ─────┼───────────────┐
   │ adjacent-lab  (arXiv API by author/paper │
   │ import        (cross-field queries)      │   fetchers (scripts, cached, rate-limited)
   │ complaint     (GitHub issues, limitations│
   │                sections, workshop CFPs)   │
   └──────────────┬────────────────────────── ┘
                  ▼
            data/seeds/<week>.jsonl ── triage (cheap model, parallel) ──► kept / dropped
                  ▼
            data/cards/<id>.json  (trick cards; strong model; parallel per seed)
                  ▼
            mutation operators ──► data/candidates/<week>.jsonl
                  ▼
            kill search (sourced: arXiv, Semantic Scholar, conference exports) ──► killed / survived
                  ▼
            red team (3 personas × checklist) ⇄ generator  ──► objection log
                  ▼
            data/reports/<cid>.md  (8 sections; §8 = ≤3 decisions)
                  ▼
            ledger/LEDGER.md  (regenerated) ──► Jacob prunes on Sundays (status edits win)
                  │
            config/labs.yaml ◄── monthly citation expansion from kept cards
```

Everything is files in a git repository. Every record is append-only with a `history` list. Every stage
is idempotent and resumable. Stages fan out in parallel over records with Claude Code subagents.

---

## 3. Data model

All records are JSON (one per line in `.jsonl` for collections, one file per record for cards and
reports). Identity is content-addressed: arXiv id for papers, `sha1(theme_id + card_id + operator +
normalized_text)[:12]` for candidates. Re-running a stage on an existing id updates `history`, never
duplicates.

### 3.1 Seed (`data/seeds/<ISO-week>.jsonl`)

```json
{"id":"2609.20004","source":"arxiv","stream":"adjacent-lab|import|complaint|manual",
 "title":"...","authors":["..."],"abstract":"...","categories":["cs.LG"],"published":"2026-09-17",
 "url":"https://arxiv.org/abs/2609.20004","matched_queries":["q_fork"],
 "status":"new|kept|dropped|jacob-dropped","triage_reason":"one line",
 "history":[{"date":"2026-10-01","status":"new","note":"fetched"}]}
```

Complaints (GitHub issues, limitations sections) use `"source":"github|paper-limitations|cfp"` and
`"id":"gh:<owner>/<repo>#<n>"`.

### 3.2 Trick card (`data/cards/<id>.json`) — schema in `schemas/card.schema.json`

Fields: `id, title, trick, framing_stripped, load_bearing_assumption, weakest_component, regime,
information_asymmetry, occupies, neighbors[], theme_fit{theme_id, score 0–3, why}, evidence_level
(full-text|abstract-only), history[]`.

`trick` is one plain sentence, mechanism only, presentable in a talk. `information_asymmetry` is the
field ideas come from: what information is missing at the stage the method operates in but exists at
another stage.

### 3.3 Candidate (`data/candidates/<ISO-week>.jsonl`) — schema in `schemas/candidate.schema.json`

Fields: `cid, theme_id, from_card, operator (1–7), statement (≤3 sentences), claim, why_now,
killing_experiment{design, cost_gpu_hours, kills_if}, kill_search{date, neighbors[{id,title,trick,
difference}], verdict}, redteam{objections[{persona, objection, evidence, answer, status}]}, status
(proposed|kill-searched|killed|survived-kill|red-teamed|reported|approved|parked|jacob-dropped),
report_path, history[]`.

### 3.4 Report (`data/reports/<cid>.md`) — skeleton in `schemas/report.md`

Eight fixed sections. Section 8 is "Decisions only Jacob can make", capped at three items. Everything a
reader could be confused by outside section 8 is a protocol bug (fix → add to checklist).

### 3.5 Lab map (`config/labs.yaml`)

Tiers: `campus, problem_setters, infra_builders, measurers, reviewers`. Entry: `name, role, why,
seed_papers[], people[], status (unverified|verified), last_seen_week, appearances`. Grown by
`scripts/expand_labs.py` (citations/references of kept cards → author/affiliation counts); promoted when
`appearances ≥ 3` across distinct weeks; `verified` only after a page confirming the role was opened.

### 3.6 Metrics (`data/metrics/<ISO-week>.json`)

Per week: seeds fetched, kept, cards, candidates, kill searches, killed, survived, reports, decisions
asked, decisions answered, Jacob edits, tokens by stage and model, wall time by stage. Rolling: kill rate,
median time-to-kill, candidates per report, reports per approval, approvals per experiment started.

---

## 4. Stages

Each stage: input → output, the prompt file, the model tier, the parallelism, the acceptance test.

| # | Stage | Input → Output | Prompt | Model tier | Parallel over | Acceptance |
|---|---|---|---|---|---|---|
| 0 | Fetch | sources → seeds, complaints | — (scripts) | — | queries | file written; counts logged; zero duplicates vs `data/seen_ids.txt` |
| 1 | Triage | seeds → kept/dropped + reason | `prompts/00_triage.md` | cheap | seeds (batches of 10) | every seed has a status and one-line reason; keep rate 10–30% |
| 2 | Card | kept seed → card | `prompts/01_trick_card.md` | strong | seeds | schema-valid; `trick` ≤ 35 words; `evidence_level` set; abstract fetched not recalled |
| 3 | Mutate | card → candidates | `prompts/02_mutate.md` | strong | cards | ≤ 4 candidates per card; each names theme and operator; dedupe by `cid` |
| 4 | Kill | candidate → kill record | `prompts/03_kill.md` | strong + tools | candidates | ≥ 5 neighbors with one-line difference; sources include ≥ 1 conference export when the venue season allows; killing experiment ≤ 1 GPU-week or `parked` |
| 5 | Red team | survivor → objection log | `prompts/04_redteam.md` | strong | personas | ≥ 2 rounds; no unanswered objection or status `killed`; checklist fully ticked |
| 6 | Report | red-teamed → report | `prompts/05_report.md` | strong | — | 8 sections; §8 ≤ 3 items; no banned hedges; every neighbor has a trick sentence |
| 7 | Ledger | all → `LEDGER.md` | — (script) | — | — | renders; newest first; status counts match jsonl |
| 8 | Lab map | kept cards → labs.yaml deltas | — (script) + review | cheap | papers | S2 or arXiv-author fallback; proposals never auto-promote |

**Weekly budget (default):** ≤ 40 seeds triaged, ≤ 8 cards, ≤ 20 candidates, ≤ 3 kill searches, ≤ 2
reports. The orchestrator enforces budgets; exceeding one is a logged event, not an exception.

**Model routing (default):** triage and lab-map proposals on the cheapest model; cards, mutation, kill,
red team and report on the strongest available. Record model and token counts per record in `history`.

---

## 5. Prompts and protocols (the IP of this system)

The prompts in `prompts/` are the substance; the code is plumbing. They encode:

- **Trick-card discipline**: strip framing; name the mechanism; name the weakest component; fill
  `information_asymmetry` (this one field produced the fork-placement idea).
- **Seven mutation operators** (`CLAUDE.md` §Definitions). Each candidate names its operator.
- **Kill search protocol**: adjacent-territory table with a one-line difference per neighbor; conference
  exports count; "why has this not been done" with the enabling-piece test; cheapest killing experiment.
- **Red team protocol**: three personas (systems reviewer, RL-theory reviewer, the professor who dismisses
  it in ten minutes), each grounded in fetched evidence; the checklist in `prompts/checklist.md`, mined
  from the fork-placement project (unbiased gradient, compute- and dose-matching, placement rule stated,
  privileged information in the loss, placebo and shuffled controls, measurability/positivity, regime
  stated, neighbors from exports, why-now, what kills it).
- **Report skeleton**: trick → claim and information asymmetry → neighbor table → why now → killing
  experiment → objection log → confidence and what would change it → ≤ 3 decisions.

The builder does not rewrite these prompts. Improvements come from the protocol-bug rule: when a report
confuses Jacob, the confusion is added to the checklist and the prompt is patched, with a dated note.

---

## 6. Scalability requirements

The machine must go from 40 seeds/week to 400 without redesign, and from one theme to five.

1. **Idempotent, resumable stages.** Every stage reads records by status and writes by id; a crashed run
   is re-run with no duplicates. Stage runs are logged to `data/runs/<timestamp>.json`.
2. **Parallel fan-out.** Stages 1–5 run over independent records; the orchestrator dispatches batches to
   Claude Code subagents (or to a worker pool when run outside Claude Code) with a concurrency cap from
   `config/pipeline.yaml` (**default** 4). Red-team personas run as parallel subagents and merge.
3. **Caching.** Every fetched abstract, citation list and page is cached under `data/cache/<sha1(url)>`
   with a 30-day TTL; fetchers consult the cache first. The kill search for a candidate reuses the
   caches of its card's neighbors.
4. **Rate limits as first-class.** arXiv: 1 request per 3 s. Semantic Scholar: key-dependent; exponential
   backoff; skip after 3 failures with a logged `degraded: s2`. GitHub: token-dependent; skip with a note.
   Degraded modes never block the week; they mark the affected records `evidence_level: degraded`.
5. **Dedupe across weeks.** `data/seen_ids.txt` for seeds; candidate `cid` is content-addressed; a candidate
   that reappears from a different card is linked (`also_from[]`), not duplicated.
6. **Model routing and cost accounting.** Model tier per stage from `config/pipeline.yaml`; tokens and
   wall time recorded per record; weekly metrics rolled up. A weekly token budget triggers triage
   tightening (raise `theme_fit` threshold) before any stage is skipped.
7. **Themes as a dimension.** All records carry `theme_id`; the ledger renders per theme; budgets are per
   theme. Adding a theme is a config edit.
8. **Human edits win.** Any field Jacob edits by hand in a record (detected by a `human_edit` marker or a
   git author check) is never overwritten; the machine appends to `history` instead.
9. **Scheduling.** A weekly run (fetch → triage → cards → mutate → kill) is schedulable from a cron or a
   Claude Code scheduled task; red team and report run on demand or on a second scheduled slot. The run
   must complete in under 2 hours of wall time at the default budget.
10. **Experiment hook.** A `survived-kill` candidate with `killing_experiment.cost_gpu_hours ≤ 24` can be
    handed to the experiment harness (§12) with a single command; the pipeline records the handoff.

---

## 7. Repository layout (target)

```
idea-pipeline/
  CLAUDE.md                # operating manual for the Claude Code operator (exists)
  SPEC.md                  # this file
  LANDSCAPE.md             # public auto-research systems: what we borrow, what we don't
  BUILD_BRIEF.md           # the first prompt to the builder session
  DECISIONS.md             # builder's log of defaults taken and deviations (created by builder)
  README.md
  config/
    themes.yaml            # the law (exists; Jacob edits)
    sources.yaml           # streams and queries (exists)
    labs.yaml              # tiered lab map, tier 0 seeded (exists)
    pipeline.yaml          # budgets, concurrency, model tiers, TTLs (builder creates from §4, §6)
  schemas/
    card.schema.json       # (exists)
    candidate.schema.json  # (exists)
    report.md              # (exists)
  prompts/
    00_triage.md 01_trick_card.md 02_mutate.md 03_kill.md 04_redteam.md 05_report.md checklist.md  (exist)
  scripts/
    fetch_arxiv.py         # reference implementation, tested (exists)
    fetch_github.py        # complaint stream (builder)
    fetch_exports.py       # conference Downloads pages → title/abstract index (builder)
    expand_labs.py         # Semantic Scholar / arXiv-author expansion (builder)
    ledger.py              # render + status transitions + metrics (builder)
    orchestrate.py         # stage runner: budgets, parallel dispatch, resumability (builder)
    run_week.sh            # fetch → triage → cards → mutate → kill, then print next steps (builder)
  .claude/commands/        # /week /triage /card /mutate /kill /redteam /report (exist, thin)
  data/                    # seeds cards candidates reports killed complaints labmap cache runs metrics
  ledger/LEDGER.md         # regenerated
  tests/                   # §10
```

---

## 8. Interfaces

**Slash commands** (Claude Code): `/week` runs stage 0 and prints the triage queue; `/triage <week>`;
`/card <id>`; `/mutate <id>`; `/kill <cid>`; `/redteam <cid>`; `/report <cid>`. Each command reads its
prompt file and the relevant records, writes files, and prints one status line.

**CLI** (outside Claude Code): `python scripts/orchestrate.py --stage {fetch,triage,card,mutate,kill,
redteam,report,ledger,labs} [--week W] [--id ID] [--budget-override k=v]`.

**Scheduled task**: `scripts/run_week.sh` is safe to run unattended; it never asks questions; it writes
`data/runs/<ts>.json` and exits non-zero only on a repository-integrity failure.

---

## 9. Security and sandboxing

Fetchers only read public APIs and pages. No code from papers is executed by the pipeline. The experiment
harness (§12) runs in a container with no network except package registries. Tokens (`S2_API_KEY`,
`GITHUB_TOKEN`) come from the environment, never from files in the repo.

---

## 10. Acceptance tests (builder must make these pass)

1. `pytest tests/` includes: schema validation of all bundled example records; `cid` determinism; dedupe
   across two synthetic weeks; ledger render from the bundled data; budget enforcement (21st candidate in
   a week is logged and parked, not written as active).
2. `scripts/fetch_arxiv.py --days 7 --dry-run` prints queries; `--days 7` writes a seeds file with ≥ 1
   record and a `data/runs` entry; a second identical run writes zero new seeds.
3. `/triage 2026-W40` on the bundled seeds produces statuses for every record; keep rate within 10–60%
   (the bundled seeds are curated, so the rate is high).
4. `/card 2609.20004` reproduces a card schema-equal to the bundled example in all fields except free text.
5. `/kill` on the bundled fork candidate reaches `survived-kill` with ≥ 5 neighbors and a killing
   experiment ≤ 24 GPU-hours (the known answer: the nested-fork correlation test).
6. `python scripts/ledger.py render` produces `ledger/LEDGER.md` with per-theme sections and status counts
   equal to the jsonl counts.
7. A full `run_week.sh` on bundled data completes under 30 minutes with the default concurrency.

---

## 11. Build order (milestones)

- **M1 — plumbing (day 1):** `pipeline.yaml`, `orchestrate.py` skeleton with statuses/history/budgets,
  `ledger.py render`, tests 1 and 6. No model calls.
- **M2 — fetch (day 1–2):** `fetch_arxiv.py` integrated with cache and seen-ids; `fetch_github.py`,
  `fetch_exports.py` with degraded modes; test 2.
- **M3 — judgment stages (day 2–3):** triage, card, mutate wired to the prompts with parallel dispatch;
  tests 3–4.
- **M4 — kill and red team (day 3–4):** sourced kill search with cache reuse; three-persona red team with
  merge; report writer; test 5.
- **M5 — lab map and metrics (day 4–5):** `expand_labs.py`, promotion rules, weekly metrics, `/week`
  end-to-end; test 7; first real week run.
- **M6 — scheduling and experiment hook (later):** scheduled weekly run; §12 handoff.

The builder keeps `DECISIONS.md` current and stops to ask only the questions listed in `BUILD_BRIEF.md`.

---

## 12. Experiment harness hook (specified, not built in v0.1)

Borrowed from `karpathy/autoresearch` (see `LANDSCAPE.md`): a killing experiment is a directory with one
agent-editable file, a fixed wall-clock budget, a single metric, and an append-only results log. The
pipeline hands a `survived-kill` candidate to `experiments/<cid>/` with `program.md` (the killing
experiment and its kill condition), `run.py` (the editable surface), `prepare.py` (fixed), and
`results.tsv`. The agent iterates within the budget; the pipeline reads `results.tsv` and sets the
candidate's status to `confirmed` or `killed-by-experiment`. The probe protocol for the fork project is
the first instance.

---

## 13. What success looks like after eight weeks

Per theme: ~150 seeds triaged, ~40 cards, ~100 candidates, ~20 kill searches, ~8 reports, 2–3 approvals,
1 experiment started; a lab map with ≥ 30 verified groups across tiers; a checklist that has grown by the
confusions it prevented; and Jacob spending under two hours a week on it.
