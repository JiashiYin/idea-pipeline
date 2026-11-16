# On Genie Sim Benchmark, the unpublished physics time step and contact-offset settings move a released policy's simulated task Score by more than the platform's claimed real-to-sim discrepancy of 10 points on at least 3 of 8 contact-rich tasks.

`CL-W46-07` · lane **L5** · status **open** · rank 8 · position both · refreshed 2026-11-16

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: none at filing; Gate 6 not yet established (kill search owed); Gate 2B flagged. Next action: see First steps.

## The claim

- **Headline:** On Genie Sim Benchmark, the unpublished physics time step and contact-offset settings move a released policy's simulated task Score by more than the platform's claimed real-to-sim discrepancy of 10 points on at least 3 of 8 contact-rich tasks.
- **Current belief (the field's):** Genie Sim README (github.com/AgibotTech/genie_sim, fetched 2026-11-15): 'Discrepancy between simulation and real-world test results is less than 10%', with no engine, time step, iteration count or contact setting named; 2611.15020 sec. II-C (card, full text): 'Simulation evaluation uses a fixed Genie Sim experimental branch' — the task-layer engine and setting are not in the text, while the object layer names '1 ms steps', 'CPU TGS, 32/1 solver iterations' and shows one engine swap at identical parameters moving error 25.50 to 524.61 mm (App. D.3); SIMPLER 2405.05941 (card neighbour): validity from matching 'the simulator's controller and camera image'; X2Real 2609.27449 (abstract fetched 2026-11-15): 'calibrates simulation visual and physical properties ... achieving a 0.84 linear correlation'. The real-to-sim evaluation community treats visuals, controller and assets as the validity axes and the numerics as fixed infrastructure; the sim-to-sim community holds the opposite datum for RL trackers (2610.32277, abstract fetched 2026-11-15: 'the first sim-to-sim gap we saw came from the harness, a missing floor and a wrong timestep').
- **If true:** A real-to-sim validity number is conditional on (engine, step, iterations, contact offset): validity tables and leaderboards (RoboColiseum, X2Real, SIMPLER-family, REALM) print the setting and a one-at-a-time sensitivity row beside the correlation; engine builders' defaults stop being certified by proxy; the lane's 'silent numerics' question gets its first answer on a validated benchmark, with the repeat floor (CL-W43-09) measured on the way.
- **If false:** Within shipped ranges the numerics are a second-order term for real-trained VLA evaluation at Score granularity: the sim-to-sim time-step datum does not transfer to this register, evaluation-twin builders are entitled to treat numerics as fixed infrastructure, with a citation, and the lane confines its numerics question to training (where the policy can exploit the setting) and to deformables; the repeat-floor table survives as CL-W43-09's datum.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: 2611.15020 names 1 ms / TGS 32/1 / solref-solimp and a 25.50 -> 524.61 mm engine swing at the object layer (App. D.3) and reports the task layer from an unnamed setting (sec. II-C); the README's 'less than 10%'; 2609.37771: 'success criteria and simulation settings do not fully capture how acceleration affects task execution'; 2610.32277's 'wrong timestep' datum. Who pays: RoboColiseum and Genie Sim (what to publish with a board), every evaluation-twin builder (X2Real, R2S-Eval, SIMPLER, REALM) choosing what to calibrate, engine builders (NVIDIA Isaac / Newton) whose defaults are being certified by proxy, and reviewers reading a real-to-sim correlation.
- **Impact ceiling:** **floor**: A sensitivity table for one shipped validated benchmark (8 tasks x 4 knobs, with repeat floor), cited by the Genie Sim paper's v2 and by the next validity table as the reason to print the setting. Requires steps 0-3. Judgment p 0.5.; **middle**: A reporting rule — engine, step, iterations, contact offset and a one-at-a-time sensitivity row beside every real-to-sim correlation — adopted by one benchmark (RoboColiseum or X2Real) and asked for by reviewers; the repeat-floor column becomes CL-W43-09's shipped datum. Requires a second benchmark (X2Real on Isaac Lab-Arena) at about 60 GPU-h more. Judgment p 0.3.; **ceiling**: The numerics-sensitivity row is a standard column of simulated robot evaluation, and the lane's V&V triad (verification of the numerics, validation against real, model-form disagreement) is adopted as the frame for validity papers. Requires three benchmarks and an engine owner's endorsement. Judgment p 0.1.
- **Relevance:** Robotics and learning faculty: direct (what a validated benchmark certifies). Engine builders (NVIDIA Isaac / Newton, Genesis): direct (their defaults are the knobs). Industry (AgiBot, RoboColiseum, evaluation-twin vendors): direct. HAL / evaluators: indirect, as the benchmark-validity shape. Narasimhan route: zero. Systems route (Lloyd / Netravali / Tri Dao): zero. Jacob's edge: load-bearing — time step, iteration count and contact offset are discretisation and convergence choices; the GPU/CPU repeatability floor is computer engineering; no mechanical engineering is involved.
- **Kill probe:** Steps 0-3: about 130 GPU-h if the policies must be built (50-70 if baseline weights cover the tasks), about $400 on cloud GPUs or $0 on owned ones, 14 days; dead if fewer than 2 of 8 tasks move by more than $\max(f_t, 1.96\,\mathrm{SE}, 0.04)$ under every knob, or at step 0 if the runtime exposes no setting.
- **Density and ownership:** Exact shape (a validated real-to-sim benchmark re-scored under its own numerics, shift read against its published validity number): 0 found — the 10-hit real-to-sim x numerics conjunction (API, 2026-11-15) holds no such paper by title. Coarser shapes occupied: one-at-a-time knob attribution for sim-trained RL (2610.32277 Table 2: 'solver iterations ... less than 0.006 rad', time step decisive); one-parameter reruns of benchmark rollouts (SimuGuard: collision constant decisive, 89% -> 98%); benchmark settings reversing VLA rankings (2609.37771: checkers and masses, 'bug fixes can reverse method rankings'); cross-platform VLA validity (2606.10366). Pre-window precedents: Erez-Tassa-Todorov ICRA 2015 (speed vs accuracy per engine), Kadian 2019 (sim-trained agents exploit the simulator, correlation 0.18). Owners: Genie Sim / AgiBot have the policies and the real column; the 2610.32277 autho…
- **Why now:** 2611.15020 (2026-11-11); Genie Sim v3.5.0 benchmark release (2026-11-02) with task-selected runtimes; RoboColiseum boards (2026-06); 2610.32277 (2026-10-23); SimuGuard (2026-10-30); X2Real (2026-09). Flag: the paper's own policies are unreleased, so the shift is measured on a rebuilt policy.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Premise numbers fetched and dated: README '<10%' (claimed, 2026-11-15), paper MAE 0.0405 and r 0.9686 (reported, Table B1), object-layer 25.50 -> 524.61 mm (reported, App. D.3), 2610.32277 Table 2 (reported). Conditioning set written: fixed policy and sampling seed, fixed layouts, one engine build, setting levels named in the headline; the Score shift is a property of (policy, layouts, setting pair, engine build), not of the protocol; GPU non-determinism measured as a floor, not assumed. The headline's quantifiers (10 points; 3 of 8) are pre-registered numbers. One defect: the paper's own pol… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass: cheapest probe under one GPU-week (about 130 GPU-h worst case), kill written before the run (fewer than 2 of 8 tasks move above max(floor, 1.96 SE, 0.04)); both outcomes informative — the null is the first datum that the sim-to-sim time-step result does not transfer to real-trained policy evaluation, and it carries the repeat-floor table. |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route A: three source types quote the strain — the paper's own split (numerics named in one layer, absent in the other) and its App. D.3 swing; the README's unqualified '<10%'; 2609.37771's 'simulation settings do not fully capture' and 2610.32277's 'wrong timestep'. Route B: the ruler (numerics sensitivity of a validity number) has a pre-registered surprise — expected: time step and contact offset move at least 3 of 8 tasks by more than 10 points, solver iterations none; the real-to-sim community assumes numerics are fixed infrastructure (no table reports them); belief-changing either way. G… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | Consumers with actions: benchmark operators (print the setting and a sensitivity row with each board — RoboColiseum, X2Real), evaluation-twin builders (add numerics to what they calibrate or cite the null), engine builders (defaults certified or not), reviewers (ask for the setting). Community-wide if true (every validity table changes a column); one community if false. Golden-shaped on breadth, proper on the null. |
| G4 | mechanism and consequence | Mechanism: contact-rich stages (grasp, fold, stack, handover) resolve impulses over a few steps, so the step size and contact offset change which grasps hold and which stacks topple; the policy is real-trained and does not adapt, so the Score shift is the simulator's alone; solver iterations are expected flat because at these step sizes the constraint solve converges within the shipped count (2610.32277 Table 2, SimuGuard). Consequence written both ways: shift above the claimed discrepancy -> print the setting and the sensitivity row, treat validity as setting-conditional; shift inside the fl… |
| G5 | durability; lab-adjacent | Durable: the sensitivity row applies to any engine, benchmark and policy generation; the specific numbers expire with Genie Sim's next release, the rule does not. Lab-adjacent: a measurement of shipped artifacts by engine builders and benchmark operators, not a frontier lab's core problem. |
| G6 | ownership, density, race window; position clause | Unmeasured: kill search owed (rule 17). Density this run: real-to-sim x numerics conjunction 10 hits total, none on the shape by title (API, 2026-11-15); known coarser occupants fetched: 2610.32277 (one-at-a-time knobs, sim-trained RL, no real column), SimuGuard (one-parameter reruns, artefact share), 2609.37771 (checkers and masses reverse rankings), 2606.10366 (cross-platform VLA validity). Pre-window: Erez-Tassa-Todorov 2015, Kadian 2019. Race: Genie Sim / AgiBot own the policies and the real column; the 2610.32277 authors own the harness method; the Gym-Anything / SimuGuard groups own rer… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W46-18 | The setting the validation never named: re-scoring Genie Sim Benchmark tasks under the physics time step, solver iterat… | Steps 0-3: about 130 GPU-h if the policies must be built (50-70 if baseline weights cover the tasks), about $400 on cloud GPUs or $0 on owned ones, 14 days; dead if fewer than 2 of 8 tasks move by more than $\max(f_t, 1.96\,\mathrm{SE}, 0.… | proposed | — |
| C-W46-20 | The engine swing at the task layer: the same Genie Sim task and policy on the PhysX and Newton runtimes the platform sh… | Steps 0-2: about 90 GPU-h with the policy build (about 30 if shared with C-W46-18), about $270 or $0 on owned GPUs, 10 days; dead if every two-runtime task's swing is inside the floor or the real-sim gap; parked at step 0 if fewer than 3 t… | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W46-18** (Sunday run), or run `/kill C-W46-18` in a session.
2. If it survives: `/redteam C-W46-18`, then the probe as pre-registered — Steps 0-3: about 130 GPU-h if the policies must be built (50-70 if baseline weights cover the tasks), about $400 on cloud GPUs or $0 on owned ones, 14 days; dead if fewer than 2 of 8 tasks move by more than $\max(f_t, 1.96\,\mathrm{SE}, 0.04)$ under every knob, or at step 0 if the runtime exposes no setting.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-15 — claim open: born W46 claims stage, origin top-down (L5 lane sentence read against card 2611.15020 and the Genie Sim README fetched 2026-11-15); probes C-W46-18 (cheapest) and C-W46-20 attached; concept-level kill search owed (rule 17); Gate 2B flagged; the per-pair interval column from the same card is CL-W43-02's refuted ruler and was not filed; the failure-stage disagreement column is a lab-only thought (r…
- 2026-11-15 — claim open: claims (W46, 2026-11-15): ranked 8: born W46: L5 numerics-vs-validity claim; probe 50-130 GPU-h with policies rebuilt (nothing released); Gate 2B flagged (magnitude against a shipped validity claim is the content); concept-level kill search runs this week (rule 17)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W46-07`, version 1)
- probe `C-W46-18`: `data/candidates/2026-W46.jsonl`
- probe `C-W46-20`: `data/candidates/2026-W46.jsonl`
