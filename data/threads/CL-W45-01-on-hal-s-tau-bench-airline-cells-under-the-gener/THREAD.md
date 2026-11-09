# On HAL's tau-bench airline cells under the Generalist scaffold, more than one in five of the task-level disagreements between two archived runs of the same model is a trigger flip (the grader ran in one run and not in the other), not the agent solving the task in one run and failing in the other, so the replicate disagreement and pass^k (the chance that all $k$ runs of a task pass) those cells report measure the instrument's trigger before they measure the agent.

`CL-W45-01` · lane **L1** · status **open** · rank 6 · position both · refreshed 2026-11-09

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established (kill search owed); Gate 3 one community. Next action: see First steps.

## The claim

- **Headline:** On HAL's tau-bench airline cells under the Generalist scaffold, more than one in five of the task-level disagreements between two archived runs of the same model is a trigger flip (the grader ran in one run and not in the other), not the agent solving the task in one run and failing in the other, so the replicate disagreement and pass^k (the chance that all $k$ runs of a task pass) those cells report measure the instrument's trigger before they measure the agent.
- **Current belief (the field's):** HAL 2602.16666 sec. 4 (as recorded on CL-W44-07): 'We set the temperature to zero so that any observed variance is attributable to non-sampling sources of stochasticity [17] (e.g., floating-point non-associativity, batch-size variation from concurrent server load, non-deterministic kernel scheduling...)'. 2611.04399 reads the ungraded half as a level shift (card quote): 'On this leaderboard the difference between the two scaffolds was a difference in whether the grader ran'. 2609.37315 abstract (fetched 2026-11-09): 'a defect beneath a score is present on every rerun', which predicts the same tasks go ungraded in both runs.
- **If true:** Benchmark owners that grade on an ending event (tau-bench, tau2-bench, HAL's airline cells) report pass^k with the grading rate and split replicate disagreement into trigger flips and outcome flips; the remedy for the Generalist's deficit is a grading rule that fires on agent exit (or a resume step), not the paper's reporting column alone; 2611.04399's per-model 'bias' directions are re-read as means of a noisy indicator; CL-W44-07's 'second sampling party' clause gets its measurement-event mechanism.
- **If false:** The ungraded set is a stable property of the task under that scaffold (Jaccard overlap $J \geq 0.75$), the replicate disagreement HAL reports is agent and serving behaviour as HAL assumes, 2611.04399's level-shift reading stands and the graded-fraction column ('accuracy 0.30, graded 51%') is the whole fix — a footnote the owners can cite.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: 2611.04399 sec. 3.2 'A model's cell holds one or two runs of about 41 records each, so the per-model gaps that end within a few points of zero are not resolved by these data'; HAL 2602.16666 sec. 4 attributes temperature-0 variance to the serving stack; HAL 2510.11977 'we were forced to rely on single runs without statistical validation'; tau-bench's pass^k is sold as the consistency metric (2406.12045). Who pays: HAL (its paused reliability tracker and its three correction notes on this paper's disclosures), the tau-bench and tau2-bench owners (the stop-token ending rule has 'no maintainer reply' as of 2026-11-03), and every leaderboard that reports pass^k on a user-simulator benchmark.
- **Impact ceiling:** **floor**: A note on HAL's airline cells giving $\tau$, $J$ and $D_{\mathrm{pub}}/D_{\mathrm{all}}$ per cell, cited by HAL's correction notes and by the next version of 2611.04399. Requires steps 0-1. Judgment p 0.55.; **middle**: A reporting rule for user-simulator benchmarks (replicate disagreement split into trigger and outcome flips; pass^k reported with the grading rate) adopted by HAL or tau2-bench, plus the measured deflation of pass^k by the trigger for one scaffold. Requires step 2 for at least five cells and one pass^k recomputation. Judgment p 0.3.; **ceiling**: The L1 program's instrument-versus-noise axis started: the published run-to-run spread of a leaderboard cell decomposed into instrument-trigger, agent-outcome and (with CL-W44-07's deterministic arm) serving terms on one benchmark, changing what 'reliability' means on multi-party benchmarks. Requires CL-W44-07's probe to run beside this and one more benchmark with a termination-gated grader. Judg…
- **Relevance:** HAL (Narayanan): direct — their archives, their replicate protocol, their correction notes. Narasimhan (tau-family): direct — the ending rule and pass^k are theirs. Evaluators: direct. Industry: moderate (any customer-service agent evaluation with a simulated user grades on an ending event). Jacob's edge: the exact decomposition of a disagreement indicator into disjoint sets is napkin-checkable; GPU numerics and theoretical physics zero (file parsing and API calls only).
- **Kill probe:** Steps 0-1: $0, 0 GPU-h, 5 days on the decrypted archives; dead if $J \geq 0.75$ and $\tau \leq 0.2$ pooled over Generalist two-run cells (bootstrap upper bound under 0.35). Step 2 adds about $150 of API spend if fewer than three such cells exist.
- **Density and ownership:** Occupied by the card: the graded-fraction finding, the alignment rule, the offline re-grade and the pooled 0.30 to 0.43 shift. Neighbours from the card and the CL-W43-14 and CL-W43-J01 kill reports: 2602.07150 (60,000 SWE-bench trajectories; single-run pass@1 moves 2.2-6.0 points; trajectories diverge early — the run term, no grader term), 2610.11678 TRACE (re-grade versus re-run on tau2-bench; 'Identical reruns flip 15-36% of task outcomes' — the flip rate without a trigger split), 2605.12131 Rollout Cards (none of 50 repositories report failed, errored or skipped runs; a drop manifest — the reporting rule, not the trigger), 2605.08545 (tau-bench airline log analysis; pass^5 under-elicited by nearly 50%), 2507.02825 (ABC; 'TAU-bench counts empty responses as successful'), 2609.37315 ('a defect beneath a score is present on every rerun' — the rival reading), 2602.16666 (HAL's temperatur…
- **Why now:** 2611.04399 released 2026-11-03 with code; HAL confirmed its three disclosures (dated 2026-10-05) and left the archives unchanged, so the paired runs are frozen; CL-W44-07 (open, rank 3) needs a mechanism for its 'second sampling party' clause and this is the cheapest one. Flag: the decomposition identity is elementary; the enabling piece is the released grader-action classifier.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | quantities defined on the probe record: published disagreement $D_{\mathrm{pub}} = \frac{1}{n}\sum_i \mathbb{1}[r_{i1} \neq r_{i2}]$ over $n = 41$ tasks with stored rewards $r_{ir} \in \{0,1\}$; trigger share $\tau$ = disagreements with $G_{i1} \neq G_{i2}$ over all disagreements, $G_{ir} \in \{0,1\}$ the grading indicator (a function of the stored record: an injected gold copy or a positive reward); $J$ the Jaccard overlap of the two ungraded sets; $D_{\mathrm{all}}$ the disagreement after offline re-grading. Conditioning set: the archive's recorded sampling setting, read at step 0 — if abov… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: C-W45-01 steps 0-1 at $0 and 0 GPU-h, 5 days; kill written: $J \geq 0.75$ and $\tau \leq 0.2$ (bootstrap upper bound under 0.35) pooled over Generalist two-run cells, so that $D_{\mathrm{pub}}/D_{\mathrm{all}} \leq 1.1$; also dead if step 0 finds the ungraded episodes carry a terminating event the paper's rule missed |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route B: the ruler (trigger share $\tau$ of replicate disagreement) is identifiable from the archive, computable from data HAL holds, with a pre-registered surprise — expected (judgment 0.5) $\tau \geq 0.4$ and $J \in [0.3, 0.6]$ on Generalist cells, $\tau \approx 0$ on Tool-Calling cells (graded 98%); the field assumes $\tau \approx 0$ (HAL's serving attribution; 2609.37315's 'present on every rerun') |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | three consumer classes with actions: benchmark owners (grade on agent exit; publish the grading rate beside pass^k), leaderboard operators (split replicate disagreement into trigger and outcome flips), auditors who re-grade from logs (resume the second party before grading — the orphan C-W45-02's question). Population: every leaderboard that reports pass^k on a user-simulator benchmark — one community; proper-shaped unless termination-gated graders prove common on other benchmark families |
| G4 | mechanism and consequence | mechanism: the Generalist closes conversations unsolicited and the stop token that triggers grading is the user simulator's reply, so whether a measurement is taken depends on a second party's sampled turn; consequence: if $\tau$ is high, pass^k on such scaffolds is deflated by the trigger's reliability (one ungraded run zeroes a task's pass^k) and the fix is protocol; if low, the fix is the reporting column |
| G5 | durability; lab-adjacent | durable as a ruler for any termination-gated grader (tau-family, any simulated-user benchmark); the HAL airline numbers themselves expire with the next archive; not head-to-head with a lab |
| G6 | ownership, density, race window; position clause | unmeasured: own concept-level kill search owed (role words: termination, episode end, stop token, ungraded, errored runs, skipped runs, drop manifest, consistency, pass^k, user simulator, early exit). Nearest fetched: TRACE 2610.11678 (2026-11-09: 'Identical reruns flip 15-36% of task outcomes' — the flip rate with no trigger split), Rollout Cards 2605.12131 (skipped runs as a reporting rule), 2605.08545 (tau-bench airline log analysis), 2609.37315 (the rival reading). Enabling piece: 2611.04399's released grader-action classifier (2026-11-03). Race: the HAL team can compute this in a day on… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W45-01 | Did the grader run twice? The trigger-flip share of run-to-run disagreement on HAL's tau-bench airline cells | Steps 0-1: $0, 0 GPU-h, 5 days on the decrypted archives; dead if $J \geq 0.75$ and $\tau \leq 0.2$ pooled over Generalist two-run cells (bootstrap upper bound under 0.35). Step 2 adds about $150 of API spend if fewer than three such cells… | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W45-01** (Sunday run), or run `/kill C-W45-01` in a session.
2. If it survives: `/redteam C-W45-01`, then the probe as pre-registered — Steps 0-1: $0, 0 GPU-h, 5 days on the decrypted archives; dead if $J \geq 0.75$ and $\tau \leq 0.2$ pooled over Generalist two-run cells (bootstrap upper bound under 0.35). Step 2 adds about $150 of API spend if fewer than three such cells exist.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-08 — claim open: filed (claims, W45) by lifting C-W45-01; the L1 top-down pass converged on the same sentence; headline quantifier set at the probe's pre-registered kill (one in five) with the expected reading (two in five) in the scorecard (checklist 2026-10-25); concept-level kill search owed before any probe is elaborated (rule 17); C-W45-02 left orphan at L1's two-claim cap and runs in the same step-0 session…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W45-01`, version 1)
- probe `C-W45-01`: `data/candidates/2026-W45.jsonl`
