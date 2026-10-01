# Build brief — paste this as the first message to the Claude Code session in the workspace

You are building the research-idea pipeline specified in this repository. Read, in this order:
`SPEC.md`, `CLAUDE.md`, `LANDSCAPE.md`, then everything in `config/`, `schemas/`, `prompts/`, and the
worked examples in `data/`. Do not redesign; build what is specified, take every **(default)** stated in
`SPEC.md`, and log each default you took and each deviation you had to make in `DECISIONS.md` with a
one-line reason.

## What to build, in order

Milestones M1 → M5 from `SPEC.md` §11. Each milestone ends with its acceptance tests (`SPEC.md` §10)
passing and a one-line status in `DECISIONS.md`. Do not start M3 before M1 and M2 tests pass.

## Constraints you must respect

1. The prompts in `prompts/` and the schemas in `schemas/` are the substance of this system. You may fix a
   typo or a broken reference; you may not change their content. If a prompt cannot be executed as written,
   stop and ask (question 3 below).
2. Every record is append-only with a `history` list; nothing is deleted; human edits win (SPEC §6.8).
3. Stages are idempotent and resumable; a second run on the same inputs writes zero new records.
4. Parallelism uses Claude Code subagents when run inside Claude Code and a worker pool otherwise; the
   concurrency cap comes from `config/pipeline.yaml`.
5. Rate limits and degraded modes are implemented as specified; a missing API key never blocks a week.
6. Python 3.11, standard library plus `pyyaml` and `pytest` only, unless `DECISIONS.md` records why
   another dependency was unavoidable.
7. Keep the shell-facing surface small: `scripts/orchestrate.py`, `scripts/run_week.sh`, and the slash
   commands in `.claude/commands/`. Everything else is a module.

## Reference implementation already present

`scripts/fetch_arxiv.py` works against the live arXiv API and writes schema-valid seeds; integrate it,
do not rewrite it. The bundled `data/seeds/2026-W40.jsonl`, the three cards in `data/cards/` and the
fork candidate in `data/candidates/2026-W40.jsonl` are the fixtures for the tests.

## The only questions you may stop to ask

1. Which model identifiers to use for the "cheap" and "strong" tiers in `config/pipeline.yaml`.
2. Whether `S2_API_KEY` and `GITHUB_TOKEN` are available in this environment.
3. A prompt in `prompts/` that cannot be executed as written (quote the line).

Anything else: take the default, log it, continue.

## Definition of done for v0.1

- `pytest tests/` green.
- `scripts/run_week.sh` completes on the bundled data in under 30 minutes and writes `ledger/LEDGER.md`.
- A first live week has been run: `data/seeds/<this-week>.jsonl` exists with real arXiv records, triage
  statuses are set, at least two cards and one kill search exist for the current week, and
  `ledger/LEDGER.md` shows them.
- `DECISIONS.md` lists every default taken.

Report back with: the test summary, the live week's counts (seeds / kept / cards / candidates / killed /
survived), and the three decisions from the week's best report — nothing else.
