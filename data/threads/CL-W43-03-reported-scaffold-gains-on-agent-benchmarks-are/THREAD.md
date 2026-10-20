# Reported scaffold gains on agent benchmarks are mostly reasoning-effort and restart effects, not scaffold design.

`CL-W43-03` · lane **L1** · status **open** · rank 6 · position both · refreshed 2026-10-20

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established; Gate 1 borderline on dollars. Grade on paper: open, ungraded past Gate 5 until the kill search. Next action: see First steps.

## The claim

- **Headline:** Reported scaffold gains on agent benchmarks are mostly reasoning-effort and restart effects, not scaffold design.
- **Current belief (the field's):** Scaffold papers attribute gains to their design; 2610.22289 §9.3: 'Further analysis is needed to determine their relative contributions'; HAL: higher effort can reduce scores
- **If true:** Scaffold papers must run the effort-notch and fresh-restart control arms; leaderboards separate scaffold from effort
- **If false:** Scaffold design carries independent value beyond effort — a measured answer to an open question

## Scorecard (from the cheapest probe's record)

- **Target value:** Asked in print: 2610.22289 Sec. 9.2 (difficulty reports 'may prompt additional reasoning'; mechanism unresolved) and Sec. 4.3 ('instructions request these behaviors rather than enforcing them'); checklist item 'shuffled control for any targeting or placement claim'. Who pays: anyone shipping 'ask when unsure' or stop-and-report behaviors in coding agents (Codex, Claude Code style harnesses) and ARC Prize entrants choosing controller cadence.
- **Impact ceiling:** **floor**: A note that timed returns match triggered returns on ARC-AGI-3 at GPT-5.5 high, cited by scaffold papers as the control they must run. Requires step 2 only. Judgment p 0.45.; **middle**: A placement-value ruler for self-reported uncertainty in agents, with the first measurement showing it is near zero on games and reported on one more benchmark (Terminal-Bench 2.1, about $1.5k more). Judgment p 0.25.; **ceiling**: A positive result (triggered >> timed) establishing that frontier agents place their own 'stuck' signal well, making the unread report a usable signal for controllers and a measurable metacognition quantity across models. Requires two models and three benchmarks. Judgment p 0.1.
- **Relevance:** Narasimhan (tau-family): moderate, attribution of a scaffold gain, same shape as the tau-bench who-moved question. HAL: direct, scaffold-sensitivity measurement. Evaluators (ARC Prize): direct. Industry: moderate (controller cadence is a product knob). Jacob's edge: physics supplies the shuffled-control habit; computer engineering relevance is zero.
- **Kill probe:** Timed-return arm, 3 reps x 25 games at GPT-5.5 high plus 3 fresh Stop-and-report reps, about $1,000, 0 GPU-hours, 4 days; dead if the Stop-and-report gain does not reproduce or the schedule cannot be matched.
- **Density and ownership:** Occupied: forced continuation by appending 'Wait' (s1, 2501.19393, pre-window) for reasoning traces, not agents; stop/restart placement in distillation (2609.14636); self-reflection controllers (Reflexion 2303.11366, pre-window); the Stop-and-report result itself. arXiv API 2026-10-19: return-control placebo query = 3 total, 1 in window, off target; periodic reminder/interrupt AND agent AND coding/terminal/game = 12 total, none a matched-schedule control (closest: 2610.01160 versioned execution for interruptible agents, a systems design). This week's seeds: Probe-and-Resume 2610.21088 (evaluation probes, not return control), Empty Commitments 2610.01045 (promises, not returns). Kill search owed with the two closest papers' limitation text quoted.
- **Why now:** Code, instruction text and 48 runs with return events public since 2026-10-15; the enforced schedule is a client-side change the environment-agnostic contract allows without touching the agent.
- **Register, and what it is not:** Measurement (attribution of a scaffold gain by a shuffled control). It is not a new return policy, not an uncertainty estimator, and not a benchmark.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe C-W43-12 (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: scaffold paper (2610.22289 sec. 9.3: further analysis needed on relative contributions), leaderboard (HAL: higher effort can reduce scores on 21 of 36 benchmarks), meta-paper (2607.12227: matched feedback and inference budgets) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: scaffold papers (run effort-notch and restart arms), leaderboards (separate scaffold from effort columns), harness builders (default effort setting) |
| G4 | mechanism and consequence | pass: mechanism — scaffolds inject tokens and fresh contexts, both of which the effort knob and a restart also inject; consequence — matched-spend reporting, or the scaffold keeps its organisational credit |
| G5 | durability; lab-adjacent | pass as a protocol, flagged as a number: the effort knob persists across generations; ARC-AGI-3 is a static set consumed in months |
| G6 | ownership, density, race window; position clause | open: kill search owed on C-W43-12 and C-W43-11 (limitation text of 2607.12227 and 2609.15309 unread); ownership risk — the same author owns the stack and names the question in sec. 9.3; re-open test is asking him |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-12 | Timed returns as the shuffled control for Stop-and-report | Timed-return arm, 3 reps x 25 games at GPT-5.5 high plus 3 fresh Stop-and-report reps, about $1,000, 0 GPU-hours, 4 days; dead if the Stop-and-report gain does not reproduce or the schedule cannot be matched. | proposed | — |
| C-W43-11 | Effort notch and fresh restart as control arms for scaffold gains | Restart-controller arm at GPT-5.5 xhigh capped at 45.5 M normalized tokens, 3 reps x 25 games, about $1,600 of the $2,200, 0 GPU-hours, 6 days; dead if RHAE < 53.2 in all reps and truncation curves separate on B <= 9 M. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W43-12** (Sunday run), or run `/kill C-W43-12` in a session.
2. If it survives: `/redteam C-W43-12`, then the probe as pre-registered — Timed-return arm, 3 reps x 25 games at GPT-5.5 high plus 3 fresh Stop-and-report reps, about $1,000, 0 GPU-hours, 4 days; dead if the Stop-and-report gain does not reproduce or the schedule cannot be matched.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-19 — claim open: seeded 2026-10-19 so the W43 probes hang under claims; grade and rewrite in the next /claims run
- 2026-10-20 — claim open: graded: C-W43-06 and C-W43-07 detached (they test sibling claims, now orphans); cheapest attached probe is C-W43-12; kill search owed; dollar-equivalent of a GPU-week raised as a decision

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-03`, version 2)
- probe `C-W43-12`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-11`: `data/candidates/2026-W43.jsonl`
