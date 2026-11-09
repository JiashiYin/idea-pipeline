# The verdict that multi-turn RL improves single-step decision quality on fewer than half of states is a ruler choice: on FrozenLake, judged by the base policy's own continuation on the ordinary states the RL policy actually visits, the RL action is the better one on more than half of them.

`CL-W45-04` · lane **L2** · status **killed** · rank None · position both · refreshed 2026-11-09

## Status

Killed — see the kill section. Failing gate: Gate 2B (pre-registered surprise equals the field's stated knowledge); Gate 6 why-now 'no reason found'. Next action: see First steps.

## The claim

- **Headline:** The verdict that multi-turn RL improves single-step decision quality on fewer than half of states is a ruler choice: on FrozenLake, judged by the base policy's own continuation on the ordinary states the RL policy actually visits, the RL action is the better one on more than half of them.
- **Current belief (the field's):** 2611.06483 abstract (fetched 2026-11-09): 'agentic RL does not uniformly elevate single-step decision quality; rather, its strength concentrates in error recovery and long-horizon resilience'; sec. 3.3 (card): 'RL achieves better step-level decision quality on only 46.8% of DeepCoder-MT states and 42.8% of FrozenLake states, with average quality no better than, even slightly below, the base model', graded against 'the exact $Q^{*}$ value of each step-level action under optimal continuation within the remaining interaction budget' on a pool sampled 'equally from base and RL trajectories'.
- **If true:** Every step-quality claim names the continuation policy and the state weights and reports the identity check; the 'RL does not improve per-step actions' story and the remedies built on it (process rewards, step judges) are re-read; the $R_{\mathrm{single}}$ decline on a fixed base-state pool is a visitation shift, not a loss of step quality.
- **If false:** Recovery-after-error is confirmed under the right ruler: more than 70% of the summed advantage sits on post-error histories and the win share stays below 52%; the paper's reading gains the identity it lacked and the next step-grading paper cites the identity check as a method note.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the paper's own hedge — 'Strictly evaluating one-step quality is challenging because reliable process rewards remain difficult to obtain in agentic settings' (sec. 3.3) — and its choice to treat visitation as bias (sec. 3.3, App. B.4); Probe-and-Resume 2610.21088 grades critics against executed continuations (card neighbour context, CL-W43-06). Who pays: anyone grading an RL'd agent step by step (process-reward builders, critic papers, the paper's authors), and the training teams who decide between outcome RL and process supervision on the strength of such readings.
- **Impact ceiling:** **floor**: A method note: the identity check and the two-ruler table on FrozenLake, cited by the paper's v2 and by the next matched-state analysis. Requires step 2. Judgment p 0.5.; **middle**: A reading rule for step-quality claims (name the continuation policy and the state weights; report the identity check) adopted by the step-credit lane's next two papers, plus the DeepCoder-MT extension. Judgment p 0.3.; **ceiling**: The decomposition of multi-turn RL's gain by depth, state stratum and continuation becomes the lane's ruler for 'what RL changed', the training-dynamics $R_{\mathrm{single}}$ reading is retired, and with the sibling budget probe the lane's first live L2 claim stands. Requires a realistic environment and the forward (non-hindsight) critic consumer named in CL-W43-06. Judgment p 0.1.
- **Relevance:** Narasimhan route (what RL teaches agents; EasyPPO's critic): direct. Any RL-theory group: the import is theirs. Industry: step-level evaluation of deployed agents. Jacob's edge: the identity, exact DP and the Monte Carlo estimator are his; theoretical physics only as the habit of writing the conservation law before the measurement; GPUs zero.
- **Kill probe:** Step 2: about 30 GPU-h marginal (130 standalone), $0, 5 days; dead if the RL win share on RL-visited ordinary histories under $Q^{\pi_{\mathrm{B}}}$ stays below 52% with the identity check passing.
- **Density and ownership:** Closest: 2611.06483 (the ruler without the identity); 2610.21088 Probe-and-Resume (continuation grading of critics, not of policies); TRPO (Schulman 2015) and CPI (Kakade and Langford 2002) as pre-window precedents that use the identity for training, never for reading an agent. Density query role words: matched states, step-level action quality, continuation, state visitation, performance difference, advantage decomposition, error recovery. Nobody owns the reading; the paper's authors have the checkpoints and would need a day.
- **Why now:** 2611.06483 (2026-11-04) makes matched-state step grading the headline reading; continuation grading spreading since Oct 2026; the identity is from 2002 and unused by any of them.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | the quantity is written before the estimator — the performance difference lemma (Kakade and Langford 2002) for a finite horizon, discount 1, deterministic environment: $$J(\pi_{\mathrm{RL}}) - J(\pi_{\mathrm{B}}) = \sum_{t=1}^{T_{\max}} \mathbb{E}_{h_t \sim d_t^{\pi_{\mathrm{RL}}},\ a_t \sim \pi_{\mathrm{RL}}(\cdot \mid h_t)} \bigl[ Q^{\pi_{\mathrm{B}}}(h_t, a_t) - V^{\pi_{\mathrm{B}}}(h_t) \bigr],$$ with $J(\pi)$ the success probability of policy $\pi$, $d_t^{\pi}$ the distribution of histories at turn $t$ under $\pi$, $Q^{\pi_{\mathrm{B}}}(h, a)$ the success probability of taking $a$ at $h$… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: about 30 GPU-h marginal on the shared checkpoint; kill written: the RL win share under $Q^{\pi_{\mathrm{B}}}$ on RL-visited ordinary histories below 52% (bootstrap band over 200 histories) with the identity check passing (summed advantage within 3 points of the measured $\mathrm{Pass}@1$ gain) and more than 70% of the sum on post-error histories |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route B: a ruler with an identity behind it and a pre-registered surprise — expected (judgment 0.55) RL wins 60-70% of RL-visited ordinary histories under $Q^{\pi_{\mathrm{B}}}$ against the paper's 42.8% under $Q^{*}$ on the symmetric pool; the field reads matched-state grading under $Q^{*}$ as a property of the policy |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | consumers with actions: step-grading and process-reward authors (name the continuation policy and the state weights), critic papers (the identity check as a method note), training teams choosing between outcome RL and process supervision on the strength of such readings. One community (the step-credit lane) — proper-shaped |
| G4 | mechanism and consequence | mechanism: what GRPO learns on a grid is to stop walking into regions where the base falls into holes, which $Q^{*}$ under optimal continuation barely penalises and $Q^{\pi_{\mathrm{B}}}$ penalises fully; a half-and-half pool graded by a perfect player measures the perfect player's map, not the difference between the two agents; consequence: the reading rule, or the confirmation of recovery |
| G5 | durability; lab-adjacent | durable: the identity applies to any policy pair and any environment; the FrozenLake number expires with the paper's v2; lab-adjacent (a ruler, not a recipe); the authors hold the checkpoints |
| G6 | ownership, density, race window; position clause | unmeasured: kill search owed (role words: matched states, step-level action quality, continuation, state visitation, performance difference, advantage decomposition, error recovery). The arXiv abstract conjunction 'performance difference lemma' AND (language model OR LLM) returned 0 on 2026-11-09 — a density datum, to be re-run in the neighbours' words (checklist 2026-10-25); Probe-and-Resume 2610.21088 grades critics against executed continuations and GiGPO 2505.10978 groups anchor states; pre-window precedents CPI 2002 and TRPO 2015 use the identity for training, never for reading an agent |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W45-07 | Graded by the wrong continuation: multi-turn RL's step quality under the base policy's own value on the states the trai… | Step 2: about 30 GPU-h marginal (130 standalone), $0, 5 days; dead if the RL win share on RL-visited ordinary histories under $Q^{\pi_{\mathrm{B}}}$ stays below 52% with the identity check passing. | killed | — |

## Kill search

### Concept level (CL-W45-04) — killed (2026-11-08)
Gate 2B: the ruler-dependence of step quality is PAV 2410.08146's theorem and mechanism sentence (Lemma F.1 is the performance difference lemma), the state-weight half is stated for LLM RL by 2609.39634, and the expected result ('RL wins on the states it steers into under the base's continuation') is 2611.06483's own reading ('long-horizon execution and error recovery') in other words — the authors would call it a confirmation, not a reversal; why-not-done is 'no reason found'.
**Occupied by:** none for the exact two-ruler table; the headline's premise and mechanism are stated by 2410.08146 (sec. 3.2, Lemma F.1) and its expected result by 2611.06483's own reading (Gate 2B)
**Why not done before:** no reason found — the checkpoint, the base policy and a deterministic grid were in 2611.06483's hands and Monte Carlo Q^{pi_B} is a few thousand short rollouts; the authors wanted the visitation-free question and the process-reward community had already settled the ruler dependence in theory (PAV 2024); the claim's why-now ('the identity is unused by any of them') is false for PAV
Closest neighbors (one-sentence trick; one-line difference):
- `2611.06483` What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents? — Sweep the turn cap at evaluation and grade both policies' sampled actions at matched states by an exact Q* (FrozenLake) or unit tests (DeepCoder-MT); RL wins 42.8-46.8% of ordinary states and 65.7-67.3% of injected-error states. *Difference:* The ruler the claim re-reads: optimal continuation on a pool built equally from base and RL trajectories to remove visitation on purpose; never Q^{pi_B}, never weighted by RL visitation, no identity check. Its own reading ('long-horizon execution and error re…
- `2410.08146` Rewarding Progress: Scaling Automated Process Verifiers for LLM Reasoning — Define a step's process reward as its advantage under a prover policy distinct from the base policy and characterise which provers help. *Difference:* Occupies part (i) of the headline (the step ruler is a continuation-policy choice) and the mechanism sentence (a capable prover 'fails to distinguish steps, resulting in A^mu ~ 0'); states the performance difference lemma as Lemma F.1. Training-signal design…
- `2605.06241` Rethinking RL for LLM Reasoning: It's Sparse Policy Selection, Not Capability Learning — Generate with the base model, substitute the RL model's token wherever it disagrees and let the base continue; the oracle intervention recovers RL's pass@1 touching 1-3% of tokens while a random substitution does not. *Difference:* The claim's instrument in single-turn reasoning (RL's choices graded by the base's continuation at matched prefixes, summed to the gain), with the opposite finding (concentration at a few branch points), on base-visited prefixes under greedy decoding; no agen…
- `2604.14877` Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis — Vary samples k and turns T jointly for a search agent, then swap the retrieval plan and the final reasoning between base and RL to attribute the gain. *Difference:* A coarse two-stage version of grading RL's choices by the base's continuation ('swapping reasoning to pi_RL at fixed pi_base strategy raises EM by 1.3 pp'); reads RL as reweighting toward strategies 'whose downstream reasoning lands on the correct answer'. No…
- `2609.39634` Free Everywhere, Exact on Trees: PPO's Dropped Correction Buys Sample Efficiency Under Ag… — Restore the state-visitation ratio PPO drops, exactly, from per-step policy ratios on history-injective dynamics. *Difference:* States the state-weight half of the lemma for LLM RL in its abstract ('estimate policy improvement under the behavioral policy's state-visitation distribution rather than the improved policy's own'); a training correction, not a diagnosis.

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

- 2026-11-08 — claim open: filed (claims, W45) by lifting C-W45-07; headline quantifier ('more than half') set at the probe's kill (52%); shares the GRPO checkpoint with CL-W45-03's probes, so the two claims' probes run in one sprint; concept-level kill search owed (rule 17); ranked 10
- 2026-11-08 — claim killed: concept-level kill search (/home/claude/idea-pipeline/data/reports/2026-W45-kill-CL-W45-04.md): killed — Gate 2B: the ruler-dependence of step quality is PAV 2410.08146's theorem and mechanism sentence (Lemma F.1 is the performance difference lemma), the state-weight half is stated for LLM RL by 2609.39634, and the expected result ('RL wins on the states it steers into under the base's continuati…
- 2026-11-08 — C-W45-07 killed: W45 concept-level kill search of CL-W45-04 (data/reports/2026-W45-kill-CL-W45-04.md): killed-with-claim; redesign owed if the residue is captured — primary readout becomes the post-error share of the summed base-continuation advantage over natural RL trajectories with a tie rule and a task bootstrap; the win-share table becomes a secondary row; the identity check stays as estimator calibration

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W45-04`, version 2)
- probe `C-W45-07`: `data/candidates/2026-W45.jsonl`
