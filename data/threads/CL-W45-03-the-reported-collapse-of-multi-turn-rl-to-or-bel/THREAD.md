# The reported collapse of multi-turn RL to or below its base model at a quarter of the turn cap is a budget-prompt effect, not a budget dependence of what RL learned: on FrozenLake with the prompt's budget line held at $T_{\max}$ (the full cap) and success read at one attempt, the RL model stays above the base model at 25% of the cap.

`CL-W45-03` · lane **L2** · status **open** · rank 9 · position both · refreshed 2026-11-09

## Status

Open claim. The claim survived its concept-level kill search (2026-11-08); no probe has run its own kill search yet — probe design comes after the kill search (rule 17). Failing gate: none hard; Gate 4 mechanism rewrite owed (why GRPO-Full and not GiGPO/PPO-Full); Gate 6 race flag (authors' v2); 2026-11-01 conjunction lesson (two one-quantifier claims). Next action: see First steps.

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

### Concept level (CL-W45-03) — survived (2026-11-08)
No occupant of the announced-vs-held control on a fixed-cap RL checkpoint and the paper never runs it (Gate 0/2B question answered no); survival is weak because the paper's own GiGPO/PPO cells show the announced prompt is not sufficient for collapse and AdaTurn Table 1 shows a silent-cap collapse of a budget-blind RL agent (judgment probability of the expected result 0.55 -> 0.25), the headline bundles a prompt term and a coverage term (split into CL-W45-03a/b), and the race is with three groups holding the stack.
**Why not done before:** an enabling piece landed: the card paper (2026-11-04) with its prompt verbatim and evaluator code (2026-10-30, no checkpoints); the budget-aware line (AdaTurn, AnySearch, On the Clock, 2610.28409, BudgetMix) varies the cap and never the counter's visibility on a fixed-cap RL checkpoint; three limitation sentences (2604.14877 App. J, 2610.28409 sec. 7, 2611.06483 App. D.1) each ask for one piece of the run; the owners could run it in a day and the step-0 letter is the re-open test
Closest neighbors (one-sentence trick; one-line difference):
- `2611.06483` What Does Multi-Turn Reinforcement Learning Really Improve in LLM Agents? — Sweep the turn cap at eight samples per task with the cap and remaining turns announced in the prompt and read RL-over-base against the cap. *Difference:* the claim's object: runs no held-prompt arm and no K=1 sweep; its own Figs. 15-16 (GiGPO-Full, PPO-Full keep their FrozenLake lead at 25% under the same announced protocol) bound the prompt term from above
- `2604.14877` Does RL Expand the Capability Boundary of LLM Agents? A PASS@(k,T) Analysis — Run 64 separate rollouts per (problem, depth T) with a prompt that never mentions T and read the RL-vs-base pass curve on a (k,T) grid. *Difference:* the silent-cap sweep in print, other domain: Table 2 RL-minus-base is about -3 at k=1 and +4 at k=64 at both T=1 and T=5 (no collapse, task saturates at T*=2); no announced arm, no counter-trained policy
- `2607.14547` AdaTurn: Budget-Aware Test-Time Scaling for Active Visual Perception Agents — Condition a visual-search agent on the allowed turns, sample the cap in training, and train the final-turn boundary as a forced answer. *Difference:* the silent-cap collapse of a budget-blind RL agent with the mechanism named (catastrophic truncation): Mini-o3 at 4 vs 32 turns loses 56-95% of its lead over the base and reverses on MME-RealWorld (Table 1, Avg@32); base row is one-pass, no fixed announced-ca…
- `2610.28409` Rewards for Budget-Aware Multi-Turn Agents That Adapt to Arbitrary Test-Time Constraints — Train one Dr. GRPO policy across sampled budgets with total and remaining budget in the prompt and compare eleven overspend penalties. *Difference:* its task-reward-only baseline is also budget-prompted and budget-sampled; Limitations concede no prompt-component ablation; no fixed-cap arm, no base-vs-RL sweep
- `2610.10833` On the Clock: Towards Punctual and Productive Time-Budgeted AI Agents — Give small agents a wall-clock budget by prompt, clock hooks, enforcement or GRPO and measure adherence and productive use. *Difference:* has a No Budget control vs budget-in-prompt for untrained agents in seconds (prompt term near zero for the base); no RL policy at an unseen cap, no per-turn counter

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
- 2026-11-08 — claim open: concept-level kill search (/home/claude/idea-pipeline/data/reports/2026-W45-kill-CL-W45-03.md): survived (weak) — No occupant of the announced-vs-held control on a fixed-cap RL checkpoint and the paper never runs it (Gate 0/2B question answered no); survival is weak because the paper's own GiGPO/PPO cells show the announced prompt is not sufficient for collapse and AdaTurn Table 1 shows a silent-…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W45-03`, version 2)
- probe `C-W45-06`: `data/candidates/2026-W45.jsonl`
