# Model-written adversarial audits do not bound what an optimiser extracts from a simulator: in agent-built simulators that passed three audit rounds, a 600-episode search against the verifier makes at least one in twenty verified successes physically invalid.

`CL-W44-05` · lane **L5** · status **killed** · rank None · position solo · refreshed 2026-11-03

## Status

Killed — see the kill section. Failing gate: Gate 6 not yet established (kill search owed). Grade on paper: open pending kill search; one scorecarded probe under one GPU-week; proper-shaped. Next action: see First steps.

## The claim

- **Headline:** Model-written adversarial audits do not bound what an optimiser extracts from a simulator: in agent-built simulators that passed three audit rounds, a 600-episode search against the verifier makes at least one in twenty verified successes physically invalid.
- **Current belief (the field's):** Gym-Anything for Robotics (2610.40565, 2026-10-29; card and candidate C-W44-15 fetched 2026-11-01): the pipeline's adversarial auditor 'found a real defect in about three quarters of our simulations' (sec. 6.4) and the paper warns that 'any such exploit could otherwise become learned behavior' (sec. 3) with no reference-based or optimiser-based check of any simulation; the released solution policies succeed on '96.7% of 2,048 gift-box states' (sec. 6.3) under the agent-chosen settings of Table 6; Policy-Aware Simulator Learning (2605.29032): optimisers 'inevitably exploit minor model inaccuracies'; the same shape in RL environment QA — Fable 5.1 card (L07): environments 'were QA'd against older, less capable models which were not able to find certain hacks'; the field's working belief is that three rounds of model audit certify a simulator for use
- **If true:** Every agent-built-simulator pipeline adds an optimiser arm to its audit loop and an invariant audit (mass, energy, penetration) on verified successes; groups about to train RL on such corpora run the admission test first; the L5 meta-benchmark's exploitability instrument X(B) gets a corpus with no robot; the result transfers to RL environment QA (audits at capability c certify nothing at c' > c)
- **If false:** The optimiser finds nothing the auditor missed on all four simulations: three model-audit rounds are sufficient on this corpus, the optimiser arm is cosmetic, and the invariant audit becomes a free column — a reassuring measurement the pipeline's authors cite

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
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | pass: premise numbers fetched and dated (25 simulators; three audit rounds; 'about three quarters' defect rate; Table 6 settings; 96.7% of 2,048 states); the quantity $\epsilon_{\mathrm{opt}} - \epsilon_{\mathrm{honest}}$ (share of verifier successes violating an invariant, optimiser arm minus released-policy arm) is random given the optimiser's seed and the initial-state draw; the simulator is deterministic given the action sequence except GPU-batch repeat spread, which is read as the floor before any violation counts (checklist 2026-10-20); the verifier (state-based) and the auditor (an LLM… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: C-W44-15 is scorecarded at ~100 GPU-h, $250, 10 d with a pre-registered kill; both outcomes informative (a null is the audit's sufficiency on this corpus) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: benchmark paper (2610.40565 sec. 3 and 6.4), meta-paper (2605.29032), system card (L07: the same audit-at-capability-c shape in RL environment QA; pressure #1) — three source types; route B: audit recall as a ruler with a pre-registered surprise (expected: violations the auditor missed on two of four simulations including one recorded defect-free, with interpenetration the majority class; the field assumes three audit rounds suffice; belief-changing if a defect-free simulation flips) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | one community at the floor (builders of agent-written simulators and groups training on them: an optimiser arm in the audit loop, an admission test); two if the recall result carries to RL environment QA (pressure #1's L07) and three if the L5 meta-benchmark adopts it as the no-robot corpus for X(B); proper-shaped, golden only through the environment-QA transfer |
| G4 | mechanism and consequence | pass: mechanism — an LLM auditor searches by reasoning over code and reports, an optimiser searches the state-action space the verifier scores, and the verifier rewards outcomes the physics never checks, so an optimiser climbs onto violations the auditor never enumerates; consequence — an optimiser arm and an invariant audit on successes if epsilon separates, model audits certified as sufficient on this corpus if it does not |
| G5 | durability; lab-adjacent | pass: a ruler for any agent-built simulator and any state-based verifier; the Gym-Anything corpus is one instance; durable as both auditors and optimisers improve (the gap is structural, not a capability snapshot) |
| G6 | ownership, density, race window; position clause | open: density unmeasured (kill search owed; the J03/J04 kill search of 2026-10-24 covered exploit AND simulator AND policy (13 all-time) and adversarial/worst-case AND simulator (60) and is the seed); incumbents: the card paper's adversarial auditor; IcFuzz 2608.06088 (fuzzes Isaac Sim for crashes, not physics); SAPU 2305.17110 (interpenetration exploited and filtered, the precedent); PolySim and ROBOGATE (cross-simulator gaps, no audit-recall axis); why now: the first released corpus of agent-written simulators with per-simulation audit reports and shared audit memory (2026-10-29); race: the… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W44-15 | Optimise against the verifier: what a budgeted search finds that three adversarial audit rounds did not | Four simulations, honest arm 200 states plus 100 held out, CMA-ES 600 episodes each, invariant audit on successes, rubric labelling; about 100 GPU-hours, about $250, 10 days; dead if $\epsilon_{\mathrm{opt}} - \epsilon_{\mathrm{honest}} <… | proposed | — |

## Kill search

### Concept level (CL-W44-05) — killed (2026-11-02)
Gate 2B: the headline's first clause equals the field's stated knowledge (Baker 2019 is the card paper's own citation for it; SPOTA 2019 defined the quantity; 2605.29032 calls exploitation inevitable; 2608.23875 collects 26 anecdotes); the claim's 'field assumes three audit rounds suffice' is not a stated belief anywhere in the fetched set (every owner disclaims sufficiency); the RL-environment-QA transfer in if_true is 2610.15924's measured and released result (31.9% residual; protocol adopted by Terminal Bench). The physics-corpus measurement with invariant-decided validity and audit recall is not occupied and survives weakly as a narrowed measurement claim.
Full record: [`data/reports/2026-W44-kill-CL-W44-05.md`](../../../data/reports/2026-W44-kill-CL-W44-05.md).
**Occupied by:** 2610.15924 (the headline's generic clause and its RL-environment-QA transfer: model-written audit residual against stronger attackers measured at 31.9%, protocol released and adopted by Terminal Bench), with 2606.16062, 2605.20744, 2608.22103, 2609.16816 in the same register; the physics premise by 1909.07528 (the card paper's own citation), 1803.03453, 1907.04685, 1912.06321, 2305.17110, 2605.29…
**Why not done before:** An enabling piece landed four days ago: the first released corpus of model-written physics simulators with per-simulation audit reports, shared audit memory, recorded attempts and released code policies (2610.40565, 2026-10-29). The robotics pipelines (Gym-Anything, Code2Worlds-2, FATE, DiagGen, WorldSolver) audit by a reading model or a pre-optimisation simulator critic because they run no RL; the agent-environment community that owns the attacker-in-the-loop protocol (2610.15924 and kin) does not touch physics. Race flag: the Gym-Anything authors, whose stated purpose (RL on the 175 training environments) surfaces every exploit as a by-product.
Closest neighbors (one-sentence trick; one-line difference):
- `2610.40565` Gym-Anything for Robotics: Scaling physical simulations with digital agents — A coding agent writes each simulation's physics; four same-model auditors, one adversarial, re-run its checks and hunt legal-action exploits for three rounds; 25 simulations and 200 verifier-scored tasks ship with recorded attempts and released code policies. *Difference:* Occupies the corpus, the auditor and the defect rate; runs no optimiser and no RL, states no residual estimate, has no limitations section; its criterion (j) and its citation of Baker 2020 are the claim's premise in the authors' own words.
- `2610.15924` Scalable Weak-to-Strong Verifier Hardening for Agent Environments — Sandbox the verifier, let a weaker model's hacker search for reward without solving the task and a fixer patch the verifier, validate patches by replaying legitimate solutions, then attack with stronger models and report the residual. *Difference:* Occupies the headline's generic clause and its RL-environment-QA transfer: a model-written audit's recall against a stronger attacker, measured (31.9% of 295 exploitable tasks still exploitable), released, adopted by Terminal Bench; attacker is a language mod…
- `1909.07528` Emergent Tool Use From Multi-Agent Autocurricula — Train hiders and seekers by self-play in a MuJoCo arena; six strategy phases emerge, including box surfing and physics exploits. *Difference:* The card paper's own citation for the exploit premise ('agents exploiting inaccuracies of the physics simulations to their advantage'); names environment generation without such behaviours as future work; pre-window, no audit, no rate.
- `2605.29032` Theoretical Foundations and Effective Algorithms for Policy-Aware Simulator Learning — Learn a simulator as a minimax game against an adversarial policy rewarded by the critic's one-step error, because powerful RL optimisers inevitably exploit minor model inaccuracies. *Difference:* The optimiser-as-auditor mechanism for learned models with a true environment to score against; no engineered simulator, no written pre-release audit to score recall against.
- `2610.41857` When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot B… — Record every physics step of benchmark rollouts, flag an object that gains speed at a contact faster than the robot or gravity account for, replay bit for bit, rerun with one engine parameter changed. *Difference:* Occupies the per-rollout invariant flag the probe would reimplement; frozen policies on hand-built benchmarks; no optimiser, no agent-written simulator; the probe cites its flag.
**Narrowest surviving headline:** On a RoboWorld simulation whose three-round robustness audit recorded no remaining defect, a 600-episode CMA-ES over the released code policy's parameters against the state-based verifier reaches verified successes that violate a physical invariant the honest policy never violates at a share epsilon_opt - epsilon_honest >= 0.05, in a defect class the audit report does not name — and a model-written attacker with execution at the same budget reaches the same class or does not. (Exploitation defined per 2605.15960; quantity per SPOTA; invariant flag per SimuGuard; recall protocol per 2610.15924…
*Search degraded:* ['s2']

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

- 2026-11-01 — claim killed: concept-level kill search (data/reports/2026-W44-kill-CL-W44-05.md): killed (weak) — Gate 2B: the headline's first clause equals the field's stated knowledge (Baker 2019 is the card paper's own citation for it; SPOTA 2019 defined the quantity; 2605.29032 calls exploitation inevitable; 2608.23875 collects 26 anecdotes); the claim's 'field assumes three audit rounds suffice' is not a stated belief…
- 2026-11-02 — claim open: written bottom-up by the W44 claims run from the orphan C-W44-15 (scout card 2610.40565; three W44 probes — C-W44-14, 15, 16 — on the scout theme 'agent-built simulators', one of them orphan); one new L5 claim this week (cap respected); concept-level kill search owed (seed: the 2026-10-24 J03/J04 kill search's queries and neighbours)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-05`, version 2)
- probe `C-W44-15`: `data/candidates/2026-W44.jsonl`
