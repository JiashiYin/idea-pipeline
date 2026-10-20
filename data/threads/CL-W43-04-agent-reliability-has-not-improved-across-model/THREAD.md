# Agent reliability has not improved across model generations once per-task difficulty is held fixed.

`CL-W43-04` · lane **L1** · status **open** · position solo · refreshed 2026-10-19

## Status

Open claim, ungraded or partly graded; nothing under it has survived a kill search yet. Failing gate: none recorded. Next action: see First steps.

## The claim

- **Headline:** Agent reliability has not improved across model generations once per-task difficulty is held fixed.
- **Current belief (the field's):** Headline accuracy rises every generation; HAL's tracker says 'reliability shows only small improvements over time while accuracy steadily climbs' on 15 agents
- **If true:** Labs report pass^k or a frailty-adjusted reliability alongside accuracy; the time-horizon curve gets a reliability companion
- **If false:** Reliability does improve once difficulty is fixed — METR's own numbers would be reinterpreted

## Scorecard (from the cheapest probe's record; the claim-level scorecard is written by `/claims`)

- **Target value:** —
- **Impact ceiling:** —
- **Relevance:** —
- **Kill probe:** —
- **Density and ownership:** —
- **Why now:** —
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | untested |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| X-W42-S7F9 | X-W42-S7F9 (frailty refit of METR's 27,119 runs; $0, 3 days) | — | — | not found in records |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml).

## Red team

Not run. A red team runs only on a probe that survived its kill search.

## First steps if pursued

1. Read the kill-search record of **X-W42-S7F9** when it lands; if killed, read what killed it before anything else.
2. If it survived: run its probe exactly as pre-registered — —
3. Write the result into the probe's record and this thread's Log; the claim's status moves only on evidence.
4. Only then: red team (`/redteam <probe>`), then the next probe under this claim by cost.

## Decisions for Jacob

- (none pending)

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-10-19 — open: seeded 2026-10-19 so the W43 probes hang under claims; grade and rewrite in the next /claims run

## Records

- claim record: `data/claims/claims.jsonl` (id CL-W43-04)
- probe `X-W42-S7F9`: `data/candidates/*.jsonl`
