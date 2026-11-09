# The reported collapse of multi-turn RL to or below its base model at a quarter of the turn cap is a budget-prompt effect, not a budget dependence of what RL learned: on FrozenLake with the prompt's budget line held at $T_{\max}$ (the full cap) and success read at one attempt, the RL model stays above the base model at 25% of the cap.

`CL-W45-03` · lane **L2** · status **open** · rank 9 · position both · refreshed 2026-11-09

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established; race flag (authors' v2). Next action: see First steps.

## The claim

- **Headline:** The reported collapse of multi-turn RL to or below its base model at a quarter of the turn cap is a budget-prompt effect, not a budget dependence of what RL learned: on FrozenLake with the prompt's budget line held at $T_{\max}$ (the full cap) and success read at one attempt, the RL model stays above the base model at 25% of the cap.
- **Current belief (the field's):** 2611.06483 abstract (fetched 2026-11-09): 'we show that trajectory-level RL advantages depend on sufficient turn budgets, diminishing significantly when budgets tighten'; sec. 3.2 (card): 'These results suggest that the gains of agentic RL depend on a sufficient interaction budget'; App. B.3: 'We conjecture that agent RL primarily strengthens long-horizon capabilities whose benefits emerge when sufficient interaction budget is available'. The protocol: 'The budget is specified in the system prompt before generation begins' (App. B.1) and 'we fix the sampling breadth at $k=8$ and vary the maximum interaction turns $T$' (sec. 3.2).
- **If true:** Budget sweeps hold the prompt and report $\mathrm{Pass}@(1,T)$ (success at one attempt under cap $T$) beside $\mathrm{Pass}@(8,T)$; the deployment-risk warning reverses (an RL agent under a silent cap is fine, under an announced unfamiliar cap it is not); BudgetMix's +7.5 points at 25% is read as partly prompt-distribution matching, which a one-line prompt-mixing control also buys; the Pass@(k,T) family (2604.14877) reports the no-counter curve.
- **If false:** The sweep is a true budget dependence: the RL model's full-cap successes concentrate beyond the 25% cut; the fix belongs in training (budget sampling or a turns-used term) and the next probe is the training 2x2 the card names (BudgetMix vs a turns-used reward vs budget-blind RL); the orphan import S8xF4's terminal-value reading becomes the live alternative mechanism.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the paper's own protocol sentences (above) and its admission that the two readings are entangled by design ('Full-Budget and BudgetMix RL use identical training settings; their only difference is the distribution of budgets', App. A.2); 2604.14877 introduced $\mathrm{Pass}@(k,T)$ 'to characterize multi-turn capability boundaries' (as quoted by the card). Who pays: anyone evaluating an RL-trained agent under a turn or step cap (BFCL, Terminal-Bench, tool-call limits), teams about to adopt BudgetMix, and the Pass@(k,T) authors whose metric is being read as a policy property.
- **Impact ceiling:** **floor**: A replication note with the 2x2 protocol on FrozenLake, cited by the paper's v2 and by the next budget-sweep paper. Requires steps 1-2. Judgment p 0.5.; **middle**: A protocol rule ('budget sweeps hold the prompt and report $K = 1$') adopted by the Pass@(k,T) family and one agent-RL framework's evaluation script, with the DeepCoder-MT extension (the environment with the largest reversal and a 100% structural bound) at about 100 GPU-h more. Judgment p 0.3.; **ceiling**: The three-term reading of a budget sweep (prompt term, coverage term, turns-used term) becomes how the lane reads 'what RL changed', and together with the sibling step-quality ruler founds the lane's first live L2 claim. Requires the sibling probe and one realistic environment. Judgment p 0.1.
- **Relevance:** Narasimhan route (Odysseus, EasyPPO train and evaluate multi-turn agents): direct. L1 evaluators (budget and effort axes): direct, the instrument is an evaluation protocol. Industry: direct for anyone deploying RL agents under step caps. Jacob's edge: the truncation identity and the without-replacement estimator are statistics; the environment rebuild is computer engineering; theoretical physics zero.
- **Kill probe:** Steps 1-2 above: about 110 GPU-h, $0 on owned GPUs, 10 days; dead if the held-prompt $K = 1$ gap at 25% is at or below zero with the band excluding half the full-cap lead.
- **Density and ownership:** Closest: the paper itself (runs neither control); 2604.14877 (sweeps $T$; its prompt handling and $k$ must be read before costing); budget-in-prompt work is single-turn (Token-Budget-Aware LLM Reasoning 2412.18547: a stated token budget changes reasoning length). Nobody owns the control; the paper's authors could run it in a day on their checkpoints, so the race is with their v2 — the step-0 letter is also the re-open test. Role words for the density query: budget-aware prompt, turn budget, interaction budget, remaining turns, anytime, truncation, Pass@(k,T), horizon cap.
- **Why now:** 2611.06483 (2026-11-04) and its BudgetMix recipe; Pass@(k,T) sweeps standard since April 2026; the paper ships the prompt verbatim and no checkpoints.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | FrozenLake transitions are deterministic ('known deterministic transition dynamics', App. B.4), so there is no luck term after the action; the quantity $p_T(x) = \Pr_{\tau \sim \pi(\cdot \mid x, T_{\max})}[R(\tau) = 1,\ \ell(\tau) \leq T]$ ($x$ the task, $R \in \{0,1\}$ the terminal verifier, $\ell(\tau)$ the turns the trajectory used) is a property of the (policy, prompt, cap) triple and the headline names all three; whose temperature: the $K = 8$ coverage term belongs to the sampled policy at 0.6, and the base is flatter than the RL model (card: cumulative log-likelihood ratio about 228 vs… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: S8xF9 at about 50 GPU-h (one GRPO training run is unavoidable: 'Model weights ... are not bundled', README); kill written: at 25% of cap $|\Delta_{\mathrm{RL}}| < 3$ points with the interval excluding $-5$ and the RL-minus-base deficit mostly wrong commits (S8xF9), or the held-prompt $K = 1$ gap at 25% at or below zero with its band excluding half the full-cap lead (C-W45-06) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route B: the ruler is the paper's own sweep with the prompt held, read at $K = 1$, with a pre-registered surprise — expected (judgment 0.55): the announced $K = 8$ reading reproduces the paper and the held $K = 1$ reading leaves RL above base at 25%; the field reads the sweep as a property of the policy (2604.14877 and the card's sec. 3.2 sentence) |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | consumers with actions: multi-turn RL evaluators (hold the prompt; report $\mathrm{Pass}@(1,T)$ with the cap drawn as a censoring line), BudgetMix adopters (run the prompt-mixing control), deployers under step caps (drop the counter rather than retrain), RL framework maintainers (log termination type and turn per rollout). Population: everyone evaluating RL'd agents under a turn cap — one community (agent-RL evaluation), proper-shaped |
| G4 | mechanism and consequence | mechanism: a tight-budget evaluation under the paper's protocol is a prompt the RL model never trained on and a cut it was never scored under, at once, while the base model saw neither prompt; the eight-try coverage bonus of the flatter base adds a second term; consequence: prompt-held $K = 1$ sweeps become the reading rule, or the training 2x2 runs |
| G5 | durability; lab-adjacent | a reading rule for any budget sweep (durable while Pass@(k,T) sweeps are the lane's standard); the FrozenLake number itself expires with the paper's v2; lab-adjacent (a control, not a recipe); race flag: the paper's authors can run it in a day on their checkpoints |
| G6 | ownership, density, race window; position clause | unmeasured: kill search owed (role words: budget-aware prompt, turn budget, interaction budget, remaining turns, anytime, truncation, censoring, competing risks, Pass@(k,T), horizon cap). Nearest: 2604.14877 (fetched 2026-11-09: 'PASS@(k,T), a two-dimensional metric that jointly varies sampling budget k and interaction depth T'; its prompt handling unread), DAPRO 2605.06605 and HARP 2610.07362 (cap as censoring for evaluation-budget allocation, one event type), AnySearch 2609.00813 and On the Clock 2610.10833 (budget-aware training — the time-awareness route), 2412.18547 (budget in the prompt… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W45-06 | Whose budget? The tight-turn collapse of multi-turn RL read with the prompt held fixed and one attempt instead of eight | Steps 1-2 above: about 110 GPU-h, $0 on owned GPUs, 10 days; dead if the held-prompt $K = 1$ gap at 25% is at or below zero with the band excluding half the full-cap lead. | proposed | — |

Also under this claim (no scorecard yet): import:2026-W45-S8xF9 (one Full-budget GRPO run on FrozenLake plus inference, about 50 GPU-h, $150-250 at spot rates, 10 d: the prompt gap $\Delta_\pi(T)$ betw…

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **import:2026-W45-S8xF9** (Sunday run), or run `/kill import:2026-W45-S8xF9` in a session.
2. If it survives: `/redteam import:2026-W45-S8xF9`, then the probe as pre-registered — —
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-08 — claim open: filed (claims, W45) by lifting C-W45-06 and import S8xF9 (cheapest); the shared three-clause headline_test of C-W45-06/07/08 split into three one-quantifier claims (checklist 2026-11-01); headline quantifier (RL above base at 25% under the held prompt at K = 1) is the probes' kill; import S8xF4 left orphan as the competing training-side mechanism; L2's first open claim since CL-W43-06 was parked;…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W45-03`, version 1)
- probe `C-W45-06`: `data/candidates/2026-W45.jsonl`
