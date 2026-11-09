# On a RoboWorld simulation whose three-round robustness audit recorded no remaining defect, a 600-episode CMA-ES over the released code policy's parameters against the state-based verifier reaches verified successes that violate a physical invariant the honest policy never violates at a share epsilon_opt - epsilon_honest >= 0.05, in a defect class the audit report does not name — and a model-written attacker with execution at the same budget reaches the same class or does not. (Exploitation defined per 2605.15960; quantity per SPOTA; invariant flag per SimuGuard; recall protocol per 2610.15924 transposed to physics; all cited, not claimed.)

`CL-W44-09` · lane **L5** · status **open** · rank 11 · position both · refreshed 2026-11-09

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established (kill search owed next week). Next action: see First steps.

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
| C-W44-15 | Optimise against the verifier: what a budgeted search finds that three adversarial audit rounds did not | Four simulations, honest arm 200 states plus 100 held out, CMA-ES 600 episodes each, invariant audit on successes, rubric labelling; about 100 GPU-hours, about $250, 10 days; dead if $\epsilon_{\mathrm{opt}} - \epsilon_{\mathrm{honest}} <… | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W44-15** (Sunday run), or run `/kill C-W44-15` in a session.
2. If it survives: `/redteam C-W44-15`, then the probe as pre-registered — Four simulations, honest arm 200 states plus 100 held out, CMA-ES 600 episodes each, invariant audit on successes, rubric labelling; about 100 GPU-hours, about $250, 10 days; dead if $\epsilon_{\mathrm{opt}} - \epsilon_{\mathrm{honest}} < 0.05$ with the band including zero on all four.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-01 — claim open: filed as the narrowest surviving headline of CL-W44-05 (killed at concept level the same day); its own concept-level kill search is owed next week (W44 budget of 12 spent) before any probe is designed (rule 17)
- 2026-11-01 — claim open: ranked 4 after the W44 kill searches: 100 GPU-h at the budget edge; four-day-old corpus; null is the surprise
- 2026-11-08 — claim open: claims (W45, 2026-11-08): rank 4 -> 11; ranked 11 (was 4): one agent-built simulator and one optimiser; narrower consumers than the eight claims placed above it; kill search still owed

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-09`, version 3)
- probe `C-W44-15`: `data/candidates/2026-W44.jsonl`
