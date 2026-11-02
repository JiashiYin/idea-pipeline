# A non-rigid-body robotics test suite assembled by porting and collecting the incumbents' tasks, plus frontier-model-synthesised scenes, will become the suite people report when they train policies.

`CL-W43-J06` · lane **L5** · status **open** · rank 8 · position solo · refreshed 2026-11-02

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 2 (no stated pressure, no ruler); Gate 4; Gate 5. Grade on paper: open as graded on 2026-11-02 so that the verdict is on the record: fails Gate 2, 4 and 5 as a product; alive only as the scene set for the ruler (J04) and the acceleration oracle (J05); the kill search, not this stage, parks or kills it. Next action: see First steps.

## The claim

- **Headline:** A non-rigid-body robotics test suite assembled by porting and collecting the incumbents' tasks, plus frontier-model-synthesised scenes, will become the suite people report when they train policies.
- **Current belief (the field's):** The non-rigid session (2026-10-23) found general deformable suites crowded and arriving monthly (SoftGym, DaXBench, GarmentLab, RoboVerse garment support, MoDeSuite, WireCraft, SoftVTBench, DLO-Lab, DeformX, RGBench, the 2023 cloth sim-to-real benchmark, GAUGE's 22 task families across textiles, cables and volumetric deformables); RoboVerse 2504.18904 is already the unified-platform aggregator across simulators; frontier-model scene synthesis is itself crowded (EmbodiedGen V2 2607.07459, Code2Worlds-2 2610.17651, Gen2Physics 2608.23869, SimuScene 2606.03994, phi-Scene 2606.21596, Artisan 2610.13947), and synthesised soft-body scenes carry no measured material behaviour - that session's conclusion was that the opening is ground truth from reality, not more synthetic scenes.
- **If true:** The suite becomes the default soft-body evaluation; policies report on it.
- **If false:** A convenience aggregator that duplicates RoboVerse and GAUGE; adoption requires a new reason to report (a finding, a standard, a consortium) that a union of existing tasks does not supply.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Who asked: nobody in print asks for another soft-body suite; people ask for real material data (GAUGE's framing) and for a reason to trust one engine over another.
- **Impact ceiling:** **floor**: A convenience aggregator with ported scenes. p = 0.6 (judgment).; **middle**: Becomes the default soft-body suite. p = 0.1 (judgment) - RoboVerse, GAUGE and consortium suites compete.; **ceiling**: Negligible without a finding attached.
- **Relevance:** L5 as a means (the scene set the ruler needs); as a product, low; porting labour is the whole cost.
- **Kill probe:** P-W43-J06-a, $0, two days.
- **Density and ownership:** Dense; see current_belief.
- **Why now:** None specific; scene synthesis tools make assembly cheaper for everyone, which lowers the barrier for competitors too.
- **Register, and what it is not:** Infrastructure. Worth doing only as the scene set for the ruler and the acceleration oracle, not as the paper.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | pass: premise numbers fetched (2610.40565: 76% blind-comparison win rate for agent-written solvers; GAUGE 2608.05948 'no uniformly faithful physics engine'); the plain trick exists (port and collect the incumbents' tasks plus synthesised scenes into one suite) |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass on paper: P-W43-J06-a ($0, 2 d overlap table) and C-W44-16 (~10 GPU-h) are under one GPU-week with pre-registered kills |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | fails both routes: no fetched source asks for another soft-body suite (the record's own target_value: 'nobody in print asks'); no ruler with a pre-registered surprise — the suite is infrastructure, and C-W44-16's surprise belongs to the fidelity question (J03/J04), not to adoption |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | one community at best (soft-body robot-RL authors); the must-change action is 'report on this suite', which RoboVerse, GAUGE, DaXBench and GarmentLab already compete for |
| G4 | mechanism and consequence | fails: the headline states an outcome (adoption) without a mechanism; the only mechanism offered is convenience |
| G5 | durability; lab-adjacent | fails: a static suite is consumed in months (standards.md Gate 5); scene synthesis lowers the barrier for every competitor |
| G6 | ownership, density, race window; position clause | dense (fourteen incumbents listed in current_belief); why now: none specific |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W43-J06-a | Overlap table: proposed suite tasks versus the incumbents' task lists; adoption evidence for existing aggregators (cita… | Dead as a contribution if over 70% of the proposed tasks exist in incumbents and no incumbent aggregator shows adoption growth; alive only as the scene set on which the ruler runs (ported by the agent transpiler, which is the systems contr… | thought | not run (no candidate record yet) |
| C-W44-16 | Score the agent's cloth and tissue against measured reality: GAUGE's trajectory error on agent-written solvers | Three GAUGE families ported to the agent's cloth, tissue and rigid stacks after a 10% port validation on Newton; about 10 GPU-hours, about $50, 12 days of mostly porting; dead if the agent solver's error lies within the Isaac / Genesis / N… | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **P-W43-J06-a** (Sunday run), or run `/kill P-W43-J06-a` in a session.
2. If it survives: `/redteam P-W43-J06-a`, then the probe as pre-registered — Dead as a contribution if over 70% of the proposed tasks exist in incumbents and no incumbent aggregator shows adoption growth; alive only as the scene set on which the ruler runs (ported by the agent transpiler, which is the systems contribution).
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- Agree with collaborators that the suite is a means (scene set for the ruler and the acceleration oracle), not the deliverable?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-25 — claim thought: captured from the collaborators' proposal; density from the non-rigid session and this week's fetches
- 2026-11-01 — claim open: ranked 8 after the W44 kill searches: Gate 2/4/5 open; one scorecarded probe (C-W44-16)
- 2026-11-02 — claim open: pressure #5 (2026-11-02): the LIBERO forks (B24: five forks in ten days, 17-42 point drops) are the field's answer to 'another suite' — perturbation axes on an existing suite, not a new one; records R24, R25 routed here
- 2026-11-02 — claim open: claims (W44 weekly run, 2026-11-02): C-W44-16 (scout card 2610.40565 x GAUGE) attached — it tests the synthesised-scenes premise, not adoption; graded against gates 0-6; status thought -> open so the grading is on the record (fails Gate 2, 4, 5 as a product); rank 16 (last); not killed or parked here — the kill search decides

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-J06`, version 3)
- `P-W43-J06-a`: seed or import record (no candidate yet)
- probe `C-W44-16`: `data/candidates/2026-W44.jsonl`
