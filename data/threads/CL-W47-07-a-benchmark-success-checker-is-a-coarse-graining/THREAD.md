# A benchmark success checker is a coarse-graining of the simulator state read at a persistence window of zero, and the physics settings that matter to the recorded success bit are the ones whose excess flip rate over the repeat floor does not decay as the window grows: on RoboTwin 2.0's flip-concentrated tasks the time-step and transient operators are irrelevant by a one-second window ($\psi_h(1\,\mathrm{s}) < 1$ pp on 7 of 10 tasks) while the contact-offset (air-gap) operator stays flat, and RoboDyna's 85 latency flips of 700 are mostly the episodes' sensitivity to any perturbation, with fewer than half surviving a same-arm repeat and a one-physics-step delay.

`CL-W47-07` · lane **L5** · status **open** · rank — · position both · refreshed 2026-11-22

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: none at concept level; Gate 6 open until the kill search. Next action: see First steps.

## The claim

- **Headline:** A benchmark success checker is a coarse-graining of the simulator state read at a persistence window of zero, and the physics settings that matter to the recorded success bit are the ones whose excess flip rate over the repeat floor does not decay as the window grows: on RoboTwin 2.0's flip-concentrated tasks the time-step and transient operators are irrelevant by a one-second window ($\psi_h(1\,\mathrm{s}) < 1$ pp on 7 of 10 tasks) while the contact-offset (air-gap) operator stays flat, and RoboDyna's 85 latency flips of 700 are mostly the episodes' sensitivity to any perturbation, with fewer than half surviving a same-arm repeat and a one-physics-step delay.
- **Current belief (the field's):** 2611.25179 (card, full text) treats the checker's readout as a code object: 61 defects, 'approximately two-thirds were rejected during visual review', rates re-scored on the authors' own re-rolls (RoboTwin -2.7 to -3.9 pp, 3.1-5.6% of episodes flipped, 'the rankings stayed the same on all three benchmarks'), with transient success (3/61, 60 ms), a first-physics-step gripper phantom and 'a contact point that the simulator reports across an air gap of up to 2 cm' (App. E) found only in executed physics, and the identifiability sentence 'A policy that goes on to release is therefore credited early, and a policy that stops there is credited for a task it did not finish. The recorded episode is the same in both cases' (App. C); it never varies a physics setting or measures a repeat floor. 2611.26969 (card, full text): 'This paired evaluation isolates the effect of inference latency on task performance' (sec. II-C); 85 / 63 / 34 of 700 matched pairs flip (12.1 / 9.0 / 4.9%) while the mean moves at most 0.03 (Table II), with no sync-sync replicate and no delay sweep.
- **If true:** Checker repairs and physics-setting sensitivities are reported at a named persistence window, and a benchmark's validity table carries the window scan beside the setting line (the reporting consequence CL-W46-07's red team asked for); 'latency sensitivity' and 'checker defect' flip counts are reported as excess over a repeat floor; the per-step audit of the L5 lane gains its readout scale.
- **If false:** If every $\psi_j$ is within 1 pp of the repeat floor or every $\psi_j$ is flat in the window: the checker is lumpable at the shipped readout and the settings are irrelevant to the bit — the ruler is a service. If the repeat floor itself is 3-6% at every window: SimAudit's 3.1-5.6% and RoboDyna's 4.9-12.1% are one floor measured twice, and both papers' flip counts are noise — a result that changes two benchmarks' reporting but not by this mechanism.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: 2611.26969's own protocol statement (sec. II-C) and its confound admission ('asynchronous performance reflects both action capability and execution timing', sec. IV-B); its mean-vs-flip contrast (0.03 vs 12%); the card's missing-null complaint; the lane's standing question of what a paired count measures (CL-W43-09's floor, CL-W43-J01). Who pays: RoboDyna's owners (what to report), the asynchronous-VLA line (DynamicVLA, Reflex, real-time chunking) that will be scored on paired protocols, evaluation-twin builders who compare policies under latency, and anyone reading a per-episode flip count as a policy property.
- **Impact ceiling:** **floor**: A dose-response table with the repeat floor and the lost / gained split for one policy on RoboDyna, cited by its v2 and by the next latency-aware benchmark as the reason to replicate the control arm. Requires steps 0-3. Judgment p 0.6.; **middle**: A reporting rule, same-arm repeat plus a fixed minimal-delay arm beside every cross-arm flip count, adopted by one dynamic-manipulation benchmark, and $\xi(d)$ at a fixed $d$ used as the latency-robustness number in one asynchronous-VLA paper. Requires the second policy (X-VLA) and the optional horizon arm. Judgment p 0.25.; **ceiling**: Paired-episode flip counts in simulated robot evaluation are read against a replicate floor as a matter of course, and latency is reported as a fixed simulated dose rather than a measured wall clock. Requires two benchmarks and one benchmark owner's adoption. Judgment p 0.08.
- **Relevance:** L1 (attribution of outcome variance to who moved: policy noise, simulator, protocol): direct. L5 (simulator sensitivity to a timing perturbation; the protocol knob of CL-W46-07 in a second benchmark, here as a measured dose rather than a calibration cell): direct as a neighbour. Robotics and learning faculty: direct. Asynchronous-VLA and real-time-control industry: direct. Engine builders: indirect (SAPIEN / PhysX determinism is read, not measured). Narasimhan route: zero. Systems route: zero (latency is imposed, not served). Jacob's edge: pure-error replication and sensitive dependence on one-step perturbations are design-of-experiments and dynamical-systems reasoning he can check; no robot.
- **Kill probe:** Steps 0-3: 40-65 GPU-h (up to 115 with a fine-tune), $100-350, 9 days; dead if both controls stay under 0.3 of the 27-step count and the dose curve rises.
- **Density and ownership:** Occupant of the number: 2611.26969 (85 / 63 / 34 of 700, no replicate, no sweep). Occupant of the knob: ReflexBench 2608.14379 (configurable latency under sync and async; card abstract: no paired count or replicate stated) and DynamicVLA's DOM benchmark 2601.22153 (asynchronous, 'partial' on paired evaluation in RoboDyna's Table I). Lane precedents: CL-W43-09 (killed 2026-11-15, Gate 2B: GPUSimBench owns the engine-repeatability premise and magnitudes for GPU-batched engines; per-episode noise is inside the reported seed interval) — not repeated: here the floor is the null for one paper's paired count, the engine is single-environment CPU PhysX, the noise is the policy's, and the if-false branch is a dose curve, not a floor table; CL-W46-07 / C-W46-18 (open): the Genie Sim inference-pause flag as a calibration cell — not repeated: RoboDyna's knob is the headline, and this probe adds the…
- **Why now:** 2611.26969 (2026-11-20); 2608.14379 Reflex (2026-08) for the fixed-delay knob; checklist 2026-11-15 (timing knobs before any latency arm); taste.md 2026-10-20 (degenerate null). Flag: artifact-enabled.
- **Register, and what it is not:** Measurement of what a reported paired count measures, with a reporting consequence (replicate and minimal-delay arms; $\xi(d)$ at fixed $d$). It is not a new latency-aware policy, not RoboDyna's protocol on another benchmark, not real-time chunking, and not a claim about which policy is more latency-robust.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Pass on paper: premise numbers fetched with denominators (61 defects, 568 proposed states, 183 verdict matches; 3.1-5.6% of about 1,050 episodes per policy flipped on RoboTwin; 85/63/34 of 700 pairs; mean shift at most 0.03) from both cards' full text. Conditioning set written in the import: the repeat null (two runs at the shipped setting, same seeds) is the floor; the excess flip rate is a property of the (setting, checker window) pair under the shipped policy; number format and the engine's step are read from the released config at step 0 (RoboTwin's step is not stated in 2611.25179 — flag… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass: C-W47-14 at 40-65 GPU-h and the import at about 85 GPU-h are both under one GPU-week; kills written; both outcomes informative (the first repeat floor for a manipulation benchmark's success bit either way). |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route B (ruler): 'checker defect' and 'latency sensitivity' made measurable as excess flip rates over a repeat floor at a named window. Surprise three ways: expected — step and transient operators irrelevant by 1 s but not at $\tau = 0$, air-gap group flat, latency relevant on moving scenes, fewer than half of RoboDyna's flips survive the controls (judgment 0.45); field assumes — numerics a detail at every window, RoboDyna's null = 0 (0.30); belief-changing — the repeat floor is itself 3-6% so both papers' counts are one floor (0.25). Flag for the kill search: the sim-to-sim harness community… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | One community with adjacent consumers: benchmark owners (window scan in the validity table), checker-audit authors (floor-corrected counts), dynamic-manipulation evaluators (replicate and minimal-delay arms), engine teams (which settings are relevant to a bit). Proper-shaped; golden only with every manipulation benchmark adopting the window line. |
| G4 | mechanism and consequence | Mechanism: a first-hit readout ($\tau = 0$) credits transient microstates inside the success block (a stack falling at 60 ms, a gripper bit one step after the open command), so settings that perturb short-time dynamics (step, latency) flip the bit only at short windows; a contact reported across an air gap is a steady microstate, so its flips persist at every window — the physics notion of relevant versus irrelevant operators. Consequences per outcome written above. |
| G5 | durability; lab-adjacent | Durable: the window scan applies to any checker and any engine; flag — RoboTwin and RoboDyna are 2026 benchmarks; the ruler, not the numbers, is what survives. |
| G6 | ownership, density, race window; position clause | Import's density (four API calls, none degraded): field words x checker words 7 (0 on point); role words 16 (2 on point: 2611.25179, 2609.37771, neither scans the window or measures a floor); RL-abstraction x verifier 18 (0); success-detector community 33 (0 varying a setting against a code checker). Kill search owed in the sim-to-sim and evaluation-determinism words. Why now: SimAudit's released checkers and counterexamples (2026-11-20) and RoboDyna's paired protocol (2026-11-21). Race: L5 checker papers are new; window judged adequate. |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W47-14 | Two controls RoboDyna did not run: the same-arm repeat and the one-physics-step delay against its 85 latency flips | Steps 0-3: 40-65 GPU-h (up to 115 with a fine-tune), $100-350, 9 days; dead if both controls stay under 0.3 of the 27-step count and the dose curve rises. | proposed | — |

Also under this claim (no scorecard yet): import:2026-W47-S4xF11 (about 85 GPU-h, about $250, 10 d: RoboTwin 2.0, SimAudit's released checkers, two released policies, 10 tasks x 40 seeds x 5 arms = 4,0…

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W47-14** (Sunday run), or run `/kill C-W47-14` in a session.
2. If it survives: `/redteam C-W47-14`, then the probe as pre-registered — Steps 0-3: 40-65 GPU-h (up to 115 with a fine-tune), $100-350, 9 days; dead if both controls stay under 0.3 of the 27-step count and the dose curve rises.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-22 — claim open: born W47 claims stage (top-down from the L5 lane sentence applied to the scorer): import S4xF11 and the RoboDyna controls probe; concept-level kill search scheduled this run

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W47-07`, version 1)
- probe `C-W47-14`: `data/candidates/2026-W47.jsonl`
