# At the settings they ship, physics engines differ in what a budgeted optimiser can extract from them by more than their fidelity scores differ, and their speed claims reorder once speed is quoted at a fixed accuracy.

`CL-W43-J04` · lane **L5** · status **thought** · rank — · position solo · refreshed 2026-10-24

## Status

A thought from `/capture`: not yet graded against the gates; its kill search has not run. Failing gate: none recorded. Next action: see First steps.

## The claim

- **Headline:** At the settings they ship, physics engines differ in what a budgeted optimiser can extract from them by more than their fidelity scores differ, and their speed claims reorder once speed is quoted at a fixed accuracy.
- **Current belief (the field's):** Engine speed is reported at the engine's own settings and fidelity on chosen motions (GPUSimBench 2607.13059, fetched: scalability and distributional fidelity at fixed settings, soft bodies excluded; RGBench 2511.06434, fetched: 20 percent lower error at 3x the speed on garments). Exploitation of simulators is folklore with a standard answer, domain randomization (Peng 2017, fetched in the C-W43-15 red team), and no engine reports an exploitability number. IcFuzz 2608.06088 (fetched) fuzzes Isaac Sim for crashes, not for physics violations.
- **If true:** Engine comparisons quote exploits per GPU-hour and time-to-accuracy; the speed leaderboard reorders; synthetic-data generators choose engines by exploitability for their task class.
- **If false:** All engines break at once or none does (the ruler cannot separate engines - its functionals are the problem), or exploitability ranks engines exactly as fidelity does (nothing new) - either is a usable finding about the ruler, not about the engines.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Who asked in print: launch claims nobody can compare (Genesis 10-80x vs Stone Tao's 3-10x slower on manipulation; Newton's 475x is rigid-body), GPUSimBench naming the speed-fidelity-determinism trade as 'largely unexamined' (fetched). Who pays: anyone budgeting synthetic data or choosing an engine for a task class.
- **Impact ceiling:** **floor**: X(B) curves and time-to-accuracy for three engines on two tasks; the first comparable numbers. p = 0.65 (judgment).; **middle**: Engine comparisons adopt exploits-per-GPU-hour and time-to-accuracy; one engine changes a default or ships a regression test on the ruler. p = 0.2 (judgment).; **ceiling**: The ruler is the per-release card for engines (with claim A behind it). p = 0.1 (judgment).
- **Relevance:** L5 direct; L3/systems route (GPU performance at matched accuracy, batch effects); robotics faculty via engine choice; Jacob's edge load-bearing. Zero for LLM-agent consumers.
- **Kill probe:** P-W43-J04-a: 10-30 GPU-h, $30-100, two weeks; dead on no separation or on ranking equal to fidelity.
- **Density and ownership:** To be measured at the kill search; fetched neighbours as in CL-W43-J03; GPUSimBench owns speed-and-determinism for rigid GPU engines and excluded soft bodies - the obvious race.
- **Why now:** GPU soft-body engines (Genesis, Isaac deformables, Newton) shipped with uncheckable speed claims in 2025-26; GPUSimBench (Jul 2026) measured rigid bodies and stopped; differentiable cloth engines make the adversary a gradient.
- **Register, and what it is not:** Measurement with a standards consequence (how to quote speed and robustness). Not a new engine, not a scene suite.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe P-W43-J04-a (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W43-J04-a | GAUGE's three engines (Isaac Sim, Genesis, Newton) plus MuJoCo/MJX, on one GAUGE cloth or cable task family and one rig… | Pre-registered: dead if every engine's X(5 GPU-h) exceeds a gross violation (all break instantly) or none exceeds the batch-permutation floor (none breaks) - no separation; dead as a headline if the X ranking equals the fidelity ranking an… | thought | not run (no candidate record yet) |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **P-W43-J04-a** (Sunday run), or run `/kill P-W43-J04-a` in a session.
2. If it survives: `/redteam P-W43-J04-a`, then the probe as pre-registered — Pre-registered: dead if every engine's X(5 GPU-h) exceeds a gross violation (all break instantly) or none exceeds the batch-permutation floor (none breaks) - no separation; dead as a headline if the X ranking equals the fidelity ranking and the speed ranking is unchanged at fixed accuracy. Expected (judgment): separation of 3-10x in X at B = 2 GPU-h between the fastest and the most conservative e…
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- First domain for the ruler: cloth (fidelity worst, real data exists, GPUSimBench stopped there) or rigid contact (Part I's assets exist)? Recommendation: both, one task each, because the generality claim needs two material classes.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-23 — claim thought: captured 2026-10-23 from the non-rigid session's headline, with the ruler under it; kill search owed
- 2026-10-24 — claim thought: Jacob's critiques answered (program note addendum): incumbents inspected, functionals are self-consistency against the declared model, adversary = calibrated optimiser portfolio on an auxiliary MDP, both capacity and realised exploitation reported
- 2026-10-24 — claim thought: kill search (concept-level): survived-kill, weak; the fidelity side is GAUGE's (2608.05948) and the engine set becomes GAUGE's three plus MuJoCo; the exploitability term is defined against its three literatures

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-J04`, version 3)
- `P-W43-J04-a`: seed or import record (no candidate yet)
