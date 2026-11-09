# On a RoboWorld simulation whose three-round robustness audit recorded no remaining defect, a 600-episode CMA-ES over the released code policy's parameters against the state-based verifier reaches verified successes that violate a physical invariant the honest policy never violates at a share epsilon_opt - epsilon_honest >= 0.05, in a defect class the audit report does not name — and a model-written attacker with execution at the same budget reaches the same class or does not. (Exploitation defined per 2605.15960; quantity per SPOTA; invariant flag per SimuGuard; recall protocol per 2610.15924 transposed to physics; all cited, not claimed.)

`CL-W44-09` · lane **L5** · status **killed** · rank None · position both · refreshed 2026-11-09

## Status

Killed — see the kill section. Failing gate: Gate 1 (both outcomes informative; probe runnable on shipped artefacts), with Gate 6 occupancy of the second clause (2609.20752) and Gate 2B on the first clause (owners' own disclaimers). Next action: see First steps.

## The claim

- **Headline:** On a RoboWorld simulation whose three-round robustness audit recorded no remaining defect, a 600-episode CMA-ES over the released code policy's parameters against the state-based verifier reaches verified successes that violate a physical invariant the honest policy never violates at a share epsilon_opt - epsilon_honest >= 0.05, in a defect class the audit report does not name — and a model-written attacker with execution at the same budget reaches the same class or does not. (Exploitation defined per 2605.15960; quantity per SPOTA; invariant flag per SimuGuard; recall protocol per 2610.15924 transposed to physics; all cited, not claimed.)
- **Current belief (the field's):** Scalable Weak-to-Strong Verifier Hardening 2610.15924 (limitation, grep-verified in the kill report): 'Hardening is bounded by the hacker's search capability and budget ... cannot ensure that all exploit routes are discovered'
- **If true:** Agent-built simulator pipelines add an optimiser-in-the-loop check with invariant-decided validity before shipping environments; the audit's recall gets a number
- **If false:** A null on a recorded-defect-free simulation is itself the belief-changing result (the field expects the optimiser to win) — informative either way

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the card paper's sec. 3 warning and its sec. 6.4 defect rate; 2605.29032's statement that optimisers 'inevitably exploit minor model inaccuracies'; themes.yaml L5 names 'simulator overoptimization' and 'what policies exploit' as the lane's question and SAPU (2305.17110) as the precedent where interpenetration was exploited and had to be filtered. Who pays: groups about to train RL on the 175 environments; the Gym-Anything authors (an optimiser-in-the-loop fourth auditor); benchmark users who read the verifier's success bit as physical competence.
- **Impact ceiling:** **floor**: A four-row table of invalid-success shares under optimisation with the auditor's recall, on the first agent-written corpus; cited by the next creation-audit paper when it adds an optimiser auditor. Requires steps 0 to 3. Judgment p 0.5.; **middle**: Recall below 0.5 on audited-clean simulations: the creation-audit loop gains a budgeted-optimiser auditor, the invariant-violation share becomes the reported exploitability number for soft-body simulators, and CL-W43-J03's optimiser-side instrument has its first corpus result. Requires the probe plus the auditor's code released. Judgment p 0.3.; **ceiling**: The optimiser audit becomes a standard column on agent-built and hand-built soft-body benchmarks (RGBench, GAUGE, BEHAVIOR-1K descendants), with the auditor's recall as the number that grades LLM audits; requires the audit on all 25 simulations plus one incumbent suite, about 500 GPU-hours. Judgment p 0.15.
- **Relevance:** Robotics and learning faculty: direct. Engine builders: moderate, the exploits are in agent-written solvers more than in their kernels. L1 (benchmark validity): direct, a verifier's success bit versus physical validity. L2: zero (no training dynamics). Systems route: zero. Industry: anyone deploying creation-audit loops. Jacob's edge: high on the invariants (mass, energy, penetration are conservation checks), moderate on the optimiser (off-the-shelf CMA-ES), zero on LLM-audit design.
- **Kill probe:** Four simulations, honest arm 200 states plus 100 held out, CMA-ES 600 episodes each, invariant audit on successes, rubric labelling; about 100 GPU-hours, about $250, 10 days; dead if $\epsilon_{\mathrm{opt}} - \epsilon_{\mathrm{honest}} < 0.05$ with the band including zero on all four.
- **Density and ownership:** From fetched abstracts: 2605.29032 (Policy-Aware Simulator Learning) proves the worst-case policy is dual to RL on the critic's one-step error and measures it on learned models in continuous control, not on engineered simulators and not against a written audit; from themes.yaml: SAPU (2305.17110) documents interpenetration exploitation in Isaac and filters it, no optimiser audit; from the card: the adversarial auditor is the paper's own pre-optimisation exploit search with its recall unestimated. Occupied by the card: the auditor design, the defect rate, the memory file. CL-W43-J03 (thought) names the budgeted-optimiser violation as its predictor; CL-W44-J02 (thought) rests on the premise that checks miss exploits; neither has a corpus result and this probe serves both without being either. Race flag: the Gym-Anything team and the 2605.29032 group; density to be counted at the kill sear…
- **Why now:** Card paper 2026-10-29 (written per-simulation audit findings; released solution programs as optimiser seeds); 2605.29032 (2026-05) for the duality framing. The optimiser is old; the flag is recorded.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: ~100 GPU-h (at the budget edge) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route B: the ruler is the audit's recall against an optimiser; the field's stated assumption is that no audit bounds an optimiser (the null is the surprise) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | unmeasured: own kill search owed; corpus four days old; 0 in-window hits on the exact shape |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W44-15 | Optimise against the verifier: what a budgeted search finds that three adversarial audit rounds did not | Four simulations, honest arm 200 states plus 100 held out, CMA-ES 600 episodes each, invariant audit on successes, rubric labelling; about 100 GPU-hours, about $250, 10 days; dead if $\epsilon_{\mathrm{opt}} - \epsilon_{\mathrm{honest}} <… | killed | — |

## Kill search

### Concept level (CL-W44-09) — killed (2026-11-08)
Gate 1: neither outcome is informative (the positive equals the owners' stated belief — hack prompt 'it does not establish that the environment cannot break'; the null is a search-space artefact of a 10–40-parameter code-policy perturbation), and the probe's named artefacts (released code policies, per-round audit reports) are not in the release; Gate 6: the second clause's mechanism is occupied by 2609.20752 and the third arm is the release's own executing hack auditor, so the parent's reading-vs-execution gap never existed.
**Occupied by:** second clause's mechanism (LLM attacker with execution vs numerical optimiser at matched simulation budget): 2609.20752 LLM-Falsifier; the executing model attacker itself: 2610.40565's released hack auditor (hack_prompt.md: 'Actually run the environment and try them'); optimiser-recall-against-adversarial-testers in the game register: 2607.07498 RAID; the physics-law oracle under search: 2307.108…
**Why not done before:** the mechanism comparison was done in September 2026 by the CPS falsification community (2609.20752); the robotics corpus shipped 2026-10-29 with an executing LLM attacker built in but without the code policies the probe parametrises or the per-round audit reports it scores against; for the only group positioned to run it (the Gym-Anything authors) it is an appendix row. Not 'no reason found'; not an open question either.
Closest neighbors (one-sentence trick; one-line difference):
- `2610.40565 + release gym-anything/robotics` Gym-Anything for Robotics: Scaling physical simulations with digital agents (RoboWorld) — A coding agent writes each simulation's physics; four auditors (qualitative, evidence, infrastructure, hack) check it over three rounds, the hack auditor running legal actions that produce NaNs, blow-ups or impossible motion and saving a reproduction; task au… *Difference:* occupies the executing model attacker (the claim's third arm is `gar audit --auditor hack` re-run); ships no code policies (paper's are two gift-box tasks), no per-round audit reports, no shared memory; runs no numerical optimiser or RL; its own prompt and re…
- `2609.20752` Large Language Models as Falsifiers for Cyber-Physical Systems (LLM-Falsifier) — Put an LLM in the falsification loop with variable names, output trajectories and the critical-time witness of the STL robustness, and compare with CMA-ES-class tools by simulations-to-counterexample. *Difference:* occupies the second clause's mechanism: LLM-with-execution vs numerical optimisers at matched simulation budget, 14 of 21 ARCH-COMP specifications won, failure condition named; target is a controller's specification, not simulator physics; hand-built Simulink…
- `2607.07498` Reward-Adaptive Iterative Discovery: Automated Game Testing for NHL26 (RAID) — Train RL scorers sequentially, masking reward near earlier agents' strategies, so the population enumerates diverse goalie-AI exploits for an expert to review. *Difference:* the game register's optimiser-recall-against-human-testers result (6 found strategies matched playtesters' exploits); qualitative, no rate, no physics oracle
- `2307.10818` PHYFU: Fuzzing Modern Physics Simulation Engines — Mutate initial states and assert that forward and backward simulation respect basic physical laws; feedback-driven scheduling. *Difference:* the physics-law oracle under search as a tool (5K error-triggering inputs, four engines); fuzzes states not policies against a verifier; hand-built engines; pre-window
- `2507.22099` Runtime Failure Hunting for Physics Engine Based Software Systems (PhysiXFails) — Collect physics failures in engine-based software, build a manifestation taxonomy and benchmark detectors. *Difference:* owns the defect-class taxonomy the probe would hand-write; no search, no verifier, no agent-written simulators

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- (none pending)

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-01 — claim open: filed as the narrowest surviving headline of CL-W44-05 (killed at concept level the same day); its own concept-level kill search is owed next week (W44 budget of 12 spent) before any probe is designed (rule 17)
- 2026-11-01 — claim open: ranked 4 after the W44 kill searches: 100 GPU-h at the budget edge; four-day-old corpus; null is the surprise
- 2026-11-08 — claim open: claims (W45, 2026-11-08): rank 4 -> 11; ranked 11 (was 4): one agent-built simulator and one optimiser; narrower consumers than the eight claims placed above it; kill search still owed
- 2026-11-08 — claim killed: concept-level kill search (/home/claude/idea-pipeline/data/reports/2026-W45-kill-CL-W44-09.md): killed — Gate 1: neither outcome is informative (the positive equals the owners' stated belief — hack prompt 'it does not establish that the environment cannot break'; the null is a search-space artefact of a 10–40-parameter code-policy perturbation), and the probe's named artefacts (released code poli…
- 2026-11-08 — C-W44-15 killed: W45 concept-level kill search of CL-W44-09 (data/reports/2026-W45-kill-CL-W44-09.md): killed-with-claim — search space (released code policy parameters), step 0 (25 audit reports + shared memory) and recall denominator are not in the release; inverted pre-registration rests on an uninterpretable null; third arm is the released hack auditor

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-09`, version 4)
- probe `C-W44-15`: `data/candidates/2026-W44.jsonl`
