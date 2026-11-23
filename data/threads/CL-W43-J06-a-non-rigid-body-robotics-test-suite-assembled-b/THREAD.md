# A non-rigid-body robotics test suite assembled by porting and collecting the incumbents' tasks, plus frontier-model-synthesised scenes, will become the suite people report when they train policies.

`CL-W43-J06` · lane **L5** · status **killed** · rank None · position solo · refreshed 2026-11-22

## Status

Killed — see the kill section. Failing gate: Gate 6 (RoboVerse 2504.18904 ports incumbents plus AI task generation; ManiLadder 2611.16374 ships 40+ deformable tasks; Alloy 2611.16312 is the enabling piece); Gate 2B; Gate 4. Grade on paper: open as graded on 2026-11-02 so that the verdict is on the record: fails Gate 2, 4 and 5 as a product; alive only as the scene set for the ruler (J04) and the acceleration oracle (J05); the kill search, not this stage, parks or kills it. Next action: see First steps.

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
| G6 | ownership, density, race window; position clause | concept-level kill search 2026-11-15 (data/reports/2026-W46-kill-CL-W43-J06.md): killed; gate failed G6; occupied_by 2504.18904 (mechanism); 2611.16374 (product); 2611.16312 (enabling piece); why not done: It was done: RoboVerse 2025-04-26 (port + synthesise, rigid; non-rigid format declared future work), ManiLadder 2026-11-12 (40+ deformable tasks on Genesis), Alloy 2026-11-12 (one scene for rigid, cloth, cables, liquids, granular, soft bodies; agent interface); fourteen non-rigid suites or data engines in the 12-month window.. Previous: dense (fourteen incumbents listed in current_belief);… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W43-J06-a | Overlap table: proposed suite tasks versus the incumbents' task lists; adoption evidence for existing aggregators (cita… | Dead as a contribution if over 70% of the proposed tasks exist in incumbents and no incumbent aggregator shows adoption growth; alive only as the scene set on which the ruler runs (ported by the agent transpiler, which is the systems contr… | thought | not run (no candidate record yet) |
| C-W44-16 | Score the agent's cloth and tissue against measured reality: GAUGE's trajectory error on agent-written solvers | Three GAUGE families ported to the agent's cloth, tissue and rigid stacks after a 10% port validation on Newton; about 10 GPU-hours, about $50, 12 days of mostly porting; dead if the agent solver's error lies within the Isaac / Genesis / N… | redesign-owed | redesign-owed ([record](../../../data/reports/2026-W46-kill-CL-W43-J06.md)) |

## Kill search

### Concept level (CL-W43-J06) — killed (2026-11-15)
Occupied in three pieces: RoboVerse 2504.18904 ports incumbents and synthesises tasks in one platform with non-rigid support as its stated future work; ManiLadder 2611.16374 (2026-11-12) ships 40+ organised deformable tasks scored on policies and coding agents; Alloy 2611.16312 (2026-11-12) is the multi-material agent-driven engine the claim would build on, with its own published list of where cloth, liquid and soft-solid behaviour departs from measurement; the adoption headline has no mechanism (Gate 4) and equals the occupants' stated programme (Gate 2B).
Full record: [`data/reports/2026-W46-kill-CL-W43-J06.md`](../../../data/reports/2026-W46-kill-CL-W43-J06.md).
**Occupied by:** 2504.18904 (mechanism); 2611.16374 (product); 2611.16312 (enabling piece)
**Why not done before:** It was done: RoboVerse 2025-04-26 (port + synthesise, rigid; non-rigid format declared future work), ManiLadder 2026-11-12 (40+ deformable tasks on Genesis), Alloy 2026-11-12 (one scene for rigid, cloth, cables, liquids, granular, soft bodies; agent interface); fourteen non-rigid suites or data engines in the 12-month window.
Closest neighbors (one-sentence trick; one-line difference):
- `2504.18904` RoboVerse: Towards a Unified Platform, Dataset and Benchmark for Scalable and Generalizab… — Abstract every simulator behind one configuration format, migrate existing benchmarks' tasks, assets and trajectories into it, add LLM task generation and teleoperation, and ship unified imitation and RL benchmarks across simulators. *Difference:* none — occupied (mechanism: port incumbents plus synthesise tasks in one platform; non-rigid format is its stated future work, sec. VII)
- `2611.16374` ManiLadder: Benchmarking Robot Manipulation Through a Categorized and Multi-Difficulty Le… — Build 112 Genesis tasks across rigid and 1D/2D/3D deformable objects and four embodiments, calibrate each task's difficulty by a fixed-data flow-matching policy's success rate, and score policies and coding agents by the highest level they reliably solve. *Difference:* none — occupied (product: 'the first simulation benchmark that contains more than 40 deformable object manipulation tasks within a well-organized structure', with protocols and agentic baselines; designs rather than ports; one engine)
- `2611.16312` Alloy: A Multi-Material Physics Engine for Robot Learning — Route every object in one scene to the solver its material card names (MuJoCo Warp, Newton VBD, Newton MPM, own SPH), couple them inside each control step, grade every parallel world's health, and expose the engine to coding agents over MCP. *Difference:* none — occupied (enabling piece: one engine for rigid, cloth, cables, liquids, granular and soft bodies, agent-driven); ships nine environments and a card library, no ported incumbent task and no suite
- `2610.40565` Gym-Anything for Robotics: Scaling physical simulations with digital agents — Have a coding agent write each simulation's physics, audit it with same-model agents for three rounds, and ship 25 non-rigid-heavy simulations as 200 RL environments with a blind table against the incumbents. *Difference:* took the synthesised half on 2026-11-01 (card occupies); ports no incumbent task; realism evidence is a same-model judgment
- `2608.05948` GAUGE: A Measurement-Grounded Benchmark for Physical Fidelity in Simulation Engines and V… — Record real trajectories for 22 controlled task families across rigid, cable, textile and volumetric materials with calibrated metadata and score Isaac Sim, Genesis and Newton by generalised trajectory error. *Difference:* the validation layer for engines, done; not a policy suite; its 'no uniformly faithful physics engine' is the claim's own material-behaviour premise
*Search degraded:* ['s2', 'conference exports not built', 'complaint stream skipped (no stack named)']

### C-W44-16 — redesign-owed (2026-11-15)
One probe for CL-W43-J03/J04: cross-engine ranking stability of a shipped non-rigid suite (ManiLadder on Genesis versus the same scenes in Alloy/Newton), unoccupied (Q8: 5 hits, none on target). It is a probe and a scene set, not a claim; file with an automatic kill on the first paper that runs a non-rigid suite across two engines.
Full record: [`data/reports/2026-W46-kill-CL-W43-J06.md`](../../../data/reports/2026-W46-kill-CL-W43-J06.md).
Per position — **solo**: not yet kill-searched; **lab**: not yet kill-searched
**Occupied by:** 2504.18904 (mechanism); 2611.16374 (product); 2611.16312 (enabling piece)

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

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
- 2026-11-08 — claim open: claims (W45, 2026-11-08): rank 8 -> 17; ranked 17 (was 8): fails Gate 2 (no stated pressure, no ruler) and Gate 4; kept open at Jacob's capture
- 2026-11-08 — claim open: re-ranked after the W45 kill searches: rank 6: kill search owed; fails Gate 2 as written
- 2026-11-15 — claim open: claims (W46, 2026-11-15): rank 6 -> 13; kill search owed; fails Gate 2 as written; kept open at Jacob's capture
- 2026-11-15 — claim killed: concept-level kill search (data/reports/2026-W46-kill-CL-W43-J06.md): killed — gate G6; Occupied in three pieces: RoboVerse 2504.18904 ports incumbents and synthesises tasks in one platform with non-rigid support as its stated future work; ManiLadder 2611.16374 (2026-11-12) ships 40+ organised deformable tasks scored on policies and coding agents; Alloy 2611.16312 (2026-11-12) is the multi-materi…
- 2026-11-15 — claim killed: failing gate recorded after the W46 kill search: Gate 6 (RoboVerse 2504.18904 ports incumbents plus AI task generation; ManiLadder 2611.16374 ships 40+ deformable tasks; Alloy 2611.16312 is the enabling piece); Gate 2B; Gate 4

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-J06`, version 8)
- `P-W43-J06-a`: seed or import record (no candidate yet)
- probe `C-W44-16`: `data/candidates/2026-W44.jsonl`; kill record `data/reports/2026-W46-kill-CL-W43-J06.md`
