# Only one or two numbers per scene are worth measuring, and which ones can be computed in simulation before any robot time: the value of calibrating each physical parameter under a material prior is concentrated in task-specific parameters, and for most tabletop tasks it is below the cost of measuring, so a material-prior database plus randomization is the right default and targeted calibration the exception.

`CL-W45-J01` · lane **L5** · status **open** · rank — · position both · refreshed 2026-11-03

## Status

Open claim. The claim survived its concept-level kill search (2026-11-03); no probe has run its own kill search yet — probe design comes after the kill search (rule 17). Failing gate: none at concept level; probe design owed after the full-text reads (rule 17); Gate 2B flagged. Next action: see First steps.

## The claim

- **Headline:** Only one or two numbers per scene are worth measuring, and which ones can be computed in simulation before any robot time: the value of calibrating each physical parameter under a material prior is concentrated in task-specific parameters, and for most tabletop tasks it is below the cost of measuring, so a material-prior database plus randomization is the right default and targeted calibration the exception.
- **Current belief (the field's):** Two camps, neither with a per-parameter number. Measure: 2606.22062 (sim-to-sim pendulum, two parameters: 'a small number of identification rollouts closed most of the transfer gap ... broad randomization that contained the true system still did not substitute for measurement'), Phys2Real 2510.11689 (VLM prior + online estimate beats DR 100 vs 79 and 57 vs 23 on CoM-offset pushing), ForceTwin 2609.21751 (probed mechanisms 87 vs 60 over a VLM prior), 2503.01255 (static joint friction left out of DR broke transfer). Randomize: Digital Cousins 2410.07408 (twins 'cannot produce cross-domain generalization'), co-training recipe 2503.24361 (+38 percent 'even with notable differences between the simulation and real-world data'), MetaGenSim 2610.19479 (optimises the generation distribution and 'matches expert manual alignment' with no alignment), InternData-A1 2511.16651 (synthetic-only pre-training matches the pi dataset), AutoRSR 2610.20336 (73-87 percent real success from randomized synthetic episodes). Pipelines that calibrate choose the parameters by VLM semantics (2601.08454: 'the minimal subset of missing physical parameters required for the simulation task'). In a 75-paper agent x real2sim2real list (2026-07-19 to 10-16) one paper (D-World) has an agent revise physical parameters on a real robot; about 16 identify parameters without an agent (deformables, tactile, actuators); about 24 are geometry only. Industry assigns, it does not measure (NVIDIA SimReady blog: friction 'assumed 0.8 / 0.6 ... not calibrated against physical measurements').
- **If true:** Real-to-sim pipelines run a simulated pre-flight check - the per-parameter value table under the scene's material prior - and spend robot time only on the one or two parameters above their measurement cost; a material-prior database becomes a first-class artefact; evaluation twins keep full calibration (where the sim must predict this scene) and training data keeps breadth (cousins); the collaborators' prior is confirmed for most tasks and bounded for the CoM / mechanism / static-friction class.
- **If false:** Either the value is spread across many parameters (then the only question is the budget split of 2606.22062 and 'targeted' is empty), or targeted calibration never beats a widened prior at any budget (then randomization is right everywhere and the result is a confirmation table), or a per-parameter value rule is already in print at full-text reading.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Who asked in print: 2606.22062 ('first measure the parameters they can and reserve randomization for the uncertainty that remains' - which ones is left open), MetaGenSim ('manual parameter alignment by domain experts' named as the cost), AdaptSim ('matching dynamics ... may not lead to policies that perform well'). Who pays: every real-to-sim pipeline deciding how to spend robot time (75 papers in 13 weeks), sim-ready asset vendors who assign friction by assumption (NVIDIA SimReady blog), Jacob's collaborators who hold the prior this claim tests.
- **Impact ceiling:** **floor**: A clean sim-to-sim study with the decision rule and a six-task value table, cited by pipelines that need a reason to skip or target calibration (CoRL / RSS paper). p = 0.5 (judgment).; **middle**: The pre-flight check is adopted as a script by one or two agentic real-to-sim pipelines or an asset vendor; the value table becomes the standard citation for 'randomization suffices here'. p = 0.25 (judgment).; **ceiling**: A law - the transfer gap's variance is low-rank in physical parameters across manipulation tasks - that reorganises calibrate-versus-randomize the way 2606.22062 began to, cited by both camps. p = 0.08 (judgment).
- **Relevance:** Collaborators: direct (their prior, tested). Industry: direct (asset vendors' assumed parameters; pipeline robot time). Jacob's edge: load-bearing - variance decompositions and Sobol indices from the dependence thread (CL-W44-J01), numerics, no robot. Narasimhan route: zero. Systems route: zero. Lane L5 program: it is the 'twin for evaluation, cousin for training' finding made measurable. Robotics-flavoured, the same objection Jacob raised about L5 on 2026-10-29 applies.
- **Kill probe:** P-W45-J01-a: 40-60 GPU-h, $80-180, 3 weeks, no robot; dead if the value is spread (top parameter under 35 percent in most tasks) or if a per-parameter rule is in print at full-text reading.
- **Density and ownership:** Concept half occupied (task-oriented exploration RSS 2020; AdaptSim 2023; MetaGenSim 2026-10); budget question asked on a pendulum (2606.22062, June 2026); the per-parameter value, its concentration and a cost-side rule unfound - arXiv abstract conjunction with Sobol / variance-based sensitivity / value of information returns 0. Princeton IRoM (Majumdar; AdaptSim, SureSim, near-optimal stopping) owns the adjacent lineages - natural reviewer or collaborator, on campus (MAE). Report: data/reports/2026-W45-kill-CL-W45-J01.md.
- **Why now:** Material priors exist as artefacts (SimReady Central authored physics; PhysX-Mobility annotations; VLM-inferred parameter distributions in Phys2Real and DEXTERA, 2025-26); parameter-conditioned policies make 'the value of knowing theta_k' a conditioning experiment; the agentic real-to-sim wave (75 papers, Jul-Oct 2026) made 'what to calibrate' a live cost; 2606.22062 asked the budget question in June and left the per-parameter question open in its own words.
- **Register, and what it is not:** Measurement with a decision rule (a pre-flight check for real-to-sim pipelines); lab-adjacent; solo-feasible in simulation. It is not a calibration method, not a new randomization scheme, not a VLM, not a claim about any engine; it does not say calibration is useless (the CoM / mechanism class is where it is predicted to pay).

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | premise checked against the 75-paper list and the vendor texts: calibration is assigned-not-measured in industry and a minority practice in the agentic wave; the collaborators' 'heavily adopted' is not supported, so the claim is a test of their prior, not a correction of the field's practice |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: cheapest probe 40-60 GPU-h, no robot, under one GPU-week |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route B (a ruler with a stated expected reading on both sides): the field's stated knowledge is 'measure what you can' (2606.22062) and 'task-relevant parameters exist' (RSS 2020); the concentration and the cost-side rule are not stated anywhere found - Gate 2B is the red team's first objection and is flagged |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | consequence named: pipelines spend robot time on one or two parameters; material-prior databases become artefacts; evaluation twins and training cousins separate |
| G4 | mechanism and consequence | mechanism: EVPI_k under the prior; Sobol proxy; mask-conditioned estimator (see the kill report, section 7) |
| G5 | durability; lab-adjacent | any engine; two engines required so the numbers are not one contact model's |
| G6 | ownership, density, race window; position clause | concept-level kill search (first pass) survived: exact shape unoccupied (Q3 = 0); adjacent concept occupied by 2006.01952 and 2302.04903 with a stated one-line difference; full texts owed |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W45-J01-a | Tasks (MuJoCo Playground / ManiSkill / Genesis): CoM-offset T-block push (Phys2Real's class), box pick-and-place, sprin… | Pre-registered: dead if the top parameter carries under 35 percent of total value in most tasks (no concentration); dead if total value exceeds 5 success points on every task (prior + DR never suffices - the collaborators' half is false) A… | open - survived the concept-level kill search (first pass, 2026-11-03); design owed after the full texts of 2606.22062, 2006.01952 and 2302.04903 are read (rule 17) | not run (no candidate record yet) |
| P-W45-J01-b | A hidden-parameter twin stands in for the robot (as in 2606.22062). At identification budgets B in {0, 2, 5, 10, 20} ro… | Pre-registered: dead if V beats neither A nor C at any budget on any task. Expected (judgment): on the CoM and drawer tasks V matches C at B = 2-5 where C needs 10-20; on pick-and-place all three arms tie within the seed interval. Cost 20-… | open - runs only if P-W45-J01-a finds concentration | not run (no candidate record yet) |

## Kill search

### Concept level (CL-W45-J01) — survived (concept, first pass) (2026-11-03)
No fetched source computes or publishes the per-parameter value of measuring under a material prior, its concentration, or a rule with the measurement cost on the other side (arXiv conjunction with Sobol / variance-based sensitivity / value of information / EVPI and sim-to-real: 0 hits). The concept 'identify task-relevant parameters' is in print (2006.01952 RSS 2020, implicit in a regret objective; AdaptSim 2302.04903, distribution adaptation) and the budget question was answered on a two-parameter pendulum (2606.22062). Gate 2B flagged: the red team will ask whether 'friction and mass matter most' is folklore; the answer must be the pre-registered concentration number, not the sentence.
Full record: [`data/reports/2026-W45-kill-CL-W45-J01.md`](../../../data/reports/2026-W45-kill-CL-W45-J01.md).
**Occupied by:** concept of task-relevant identification: 2006.01952, 2302.04903; budget question on a toy: 2606.22062; exact shape (per-parameter value under a material prior, concentration, cost rule, sim-to-sim, manipulation): none found
**Why not done before:** Enabling pieces landed in 2025-26 (material priors as artefacts; parameter-conditioned policies; the agentic calibration wave made the choice a cost); the question sits between system-identification (identifiability), randomization (ranges) and pipeline builders (VLM picks). Not a 'no reason' case.
Closest neighbors (one-sentence trick; one-line difference):
- `2606.22062` How Should a Simulation-to-Reality Transfer Budget Be Spent? (2026-06-20) — Sim-to-sim pendulum with two hidden parameters: sweep identification rollouts against randomization width; a few rollouts close most of the gap and randomization containing the truth does not substitute. *Difference:* Two parameters, one toy; no per-parameter value, no material prior, no cost rule; leaves structural mismatch and 'which parameters' open in its own text.
- `2006.01952` Learning Active Task-Oriented Exploration Policies for Bridging the Sim-to-Real Gap (RSS… — Learn an exploration policy that minimises downstream task regret so it probes the parameters the task cost is sensitive to, then hand the estimates to a model-based optimizer. *Difference:* Relevance implicit in a learned policy, never reported per parameter; compared only to task-agnostic exploration, never to randomization.
- `2302.04903` AdaptSim: Task-Driven Simulation Adaptation for Sim-to-Real Transfer (Princeton IRoM) — Meta-learn a policy that adjusts the simulation parameter distribution from a few real rollouts to maximise task performance rather than dynamics match. *Difference:* Adapts the whole distribution with real data; no decomposition by parameter; no measure-or-not decision.
- `2610.19479` Active Generative Simulation / MetaGenSim (2026-10-14) — Meta-learn a rater over the simulator's generation distribution to maximise real success without manual parameter alignment. *Difference:* Generation-side, real rollouts in the loop, learned rater; not a measurement of what calibration is worth.
- `2510.11689` Phys2Real (2025-10) — VLM-inferred prior distributions over physical parameters fused with online estimates; policies conditioned on the parameters; beats DR on CoM-offset pushing. *Difference:* Picks the parameter (CoM) by hand; the 'calibration wins' datum, no rule for when randomization suffices.
*Search degraded:* ['s2 skipped (no key)', 'full texts of 2606.22062, 2006.01952, 2302.04903 unread (abstracts and one PDF summary)', 'GitHub complaint stream skipped', 'no conference-export index']

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **P-W45-J01-a** (Sunday run), or run `/kill P-W45-J01-a` in a session.
2. If it survives: `/redteam P-W45-J01-a`, then the probe as pre-registered — Pre-registered: dead if the top parameter carries under 35 percent of total value in most tasks (no concentration); dead if total value exceeds 5 success points on every task (prior + DR never suffices - the collaborators' half is false) AND is spread (nothing to target); dead as a headline if a per-parameter value rule is found at full-text reading. Expected (judgment): total value under 5 point…
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-03 — claim open: captured from Jacob's real-to-sim questions (2026-11-03) with a concept-level kill search run in the same session (first pass, abstract-level, 73 abstracts + 8 pages; report data/reports/2026-W45-kill-CL-W45-J01.md): survived - exact shape unoccupied, concept half occupied by RSS 2020 / AdaptSim with a stated difference; Gate 2B flagged; probe design owed after the full-text reads (rule 17); red…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W45-J01`, version 1)
- `P-W45-J01-a`: seed or import record (no candidate yet)
- `P-W45-J01-b`: seed or import record (no candidate yet)
