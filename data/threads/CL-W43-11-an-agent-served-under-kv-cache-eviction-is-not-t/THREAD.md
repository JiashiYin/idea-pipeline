# An agent served under KV-cache eviction is not the agent its transcript describes: it keeps using tool outputs it can no longer see, and a trainer recomputing log-probabilities from the text does not reproduce the policy it sampled from.

`CL-W43-11` · lane **L3** · status **killed** · rank None · position both · refreshed 2026-11-03

## Status

Killed — see the kill section. Failing gate: Gate 6 not yet established (kill search requested ahead of rank order on 2026-10-30). Grade on paper: open pending kill search; four scorecarded probes under one GPU-week each; champion candidate. Next action: see First steps.

## The claim

- **Headline:** An agent served under KV-cache eviction is not the agent its transcript describes: it keeps using tool outputs it can no longer see, and a trainer recomputing log-probabilities from the text does not reproduce the policy it sampled from.
- **Current belief (the field's):** Agentic-RL stacks and the cache-engineering paper treat the visible token sequence as the policy's input: 2610.28577 names training under cache operations as future work and benchmarks drop/reposition only against threshold summarization, never against the same drop done as text (card 2610.28577, Table 1 and sec. 3.2).
- **If true:** Trainers log the operation sequence, not the token sequence, or forbid eviction during rollouts; the +1.7-point cache-operations margin is re-read as ghost information; off-policy corrections (the engine-trainer mismatch literature) gain a second, larger term.
- **If false:** KV drop equals text drop within 3 points and post-drop divergence is within 2x the numerical baseline: cache operations are a pure cost lever and trainers can keep recomputing from text.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: 2610.28577 writes down the history dependence and names training under it as future work; import S6xF7 names cache engineering as a training-throughput lever once KV residency is shown to bind. Who pays: agentic-RL systems teams that want eviction or compaction inside rollouts without training a different policy than the one that acted; serving teams who must know whether an operation log is a required part of the trajectory record.
- **Impact ceiling:** **floor**: A null: the divergence is within the numerical mismatch band and cache eviction is free for trainers; a citable footnote that unblocks the KV-residency lever inside RL; probability 0.15 (judgment).; **middle**: A ruler with numbers on two models: trainers must reproduce the operation sequence or carry it in importance weights; adopted as a check by one open agentic-RL stack; requires the two models and the trainer-side reproduction demo (one prefill per trajectory on AKV); probability 0.55 (judgment).; **ceiling**: The divergence is shown to change a training outcome: the same rollouts trained with text recompute versus operation-aware recompute diverge in pass rate on one task family (an added ~150 GPU-h training run, lab position preferred); the operation log becomes a standard field of agentic-RL trajectory records; probability 0.2 (judgment).
- **Relevance:** **routes**: L3 systems route: train-serve consistency for RL infrastructure, direct. L2 (Narasimhan, RL groups): the consumer of the result. L4: cache-level compaction as a training problem. L1: none.; **industry**: Direct for any team serving agents with cache editing and training on the trajectories; serving-engine teams (SGLang, vLLM) decide whether to expose the operation log.; **jacobs_edge**: Direct: this is a numerics and identity question (two states with identical tokens and positions, finite-precision re-rotation error, bf16 mismatch as the unit); GPU arithmetic is his ground.; **zero_where**: L5 (robot simulation): zero.
- **Kill probe:** 90 recorded trajectories, three teacher-forced replays each, two open models, ~30 GPU-h, ~$110, 5 days; kills if post-drop divergence stays under 2x the numerical mismatch and the over-threshold token fraction does not move.
- **Density and ownership:** From the card's neighbors only: SideQuest 2602.22603 trains a side branch to issue cache deletions (215 samples) and is the one neighbor where a trained component acts on a modified cache; whether its training reproduced the modified state is the first thing to read. Context Language Models 2609.37725 trains context editing with online RL, but its edits are to text, so text recompute is exact there, which is the contrast case. The other neighbors (TokenPilot, SmoothAgent, Complexity Trap) are text-level and do not face the mismatch. The engine-trainer numerical mismatch and its importance-ratio corrections are a known body of agentic-RL systems work that the kill search must name and quote; nothing is stated about it here from memory beyond its existence as a trainer practice. Queries in the field's words: 'training-inference mismatch', 'importance sampling', 'rollout engine', 'log-prob…
- **Why now:** 2610.28577 (October 2026): the formalization, the future-work sentence and the segment-batch attention that makes teacher-forcing any operation history one prefill; import S6xF7 (2026-10-25): KV residency as the predicted binding station in agentic RL.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: C-W43-25 (~30 GPU-h) and C-W44-09 (~30 GPU-h) both under one GPU-week with pre-registered kills; C-W44-10 adds the gradient-level consequence at ~60 GPU-h |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: a systems paper that names training under cache operations as future work (2610.28577) and the engine-trainer mismatch line that agentic-RL stacks already correct for (card neighbors); route B: the ruler is per-token divergence by turn offset, computable from recorded trajectories; 2026-11-02, pressure #11 names the mechanism's cause and its field-scale consequence: Q08 vLLM 'the high-performance baseline's train-inference KL rose from 2e-3 to 29.9 while reward fell back [...] the consistent run's SWE-bench Pro score holds while the baseline's drops from 0.56 to 0.22'; the pres… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass: RL infrastructure teams (log operations or forbid eviction), serving teams (whether cache ops change the policy), compaction evaluators (ghost information as a confound); after pressure #11, every method paper that reports a delta on an asynchronous stack is a consumer of the train-inference KL column — community-wide if the eviction term is of the order of the sampling noise (C-W44-10's pre-registered expectation) |
| G4 | mechanism and consequence | pass: mechanism — attention entries computed while the tool output was visible carry its information after eviction; consequence — a logging change or an eviction ban in rollouts |
| G5 | durability; lab-adjacent | pass: a property of any KV-cache serving stack; the AKV engine is one instance |
| G6 | ownership, density, race window; position clause | open: density not measured; why now — the released AKV engine and cache-operation API (2026-10); race window unknown; lab-adjacent (systems labs publish this; frontier labs do not); 2026-11-02: InterQ-RL 2610.35303 (October 2026) and CTPO 2605.07331 own the arithmetic-mismatch correction and its sqrt(n) envelope; the Zero-Mismatch Reference 2605.14220 calls mismatch 'a systems-level perturbation that should be treated as a first-order factor'; none of the three separates the eviction (conditioning) term from the arithmetic term — the claim's ground; density P11a = 2 (12-month) |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-25 | Off-policy by cache: how far the served policy under KV eviction departs from its own text | 90 recorded trajectories, three teacher-forced replays each, two open models, ~30 GPU-h, ~$110, 5 days; kills if post-drop divergence stays under 2x the numerical mismatch and the over-threshold token fraction does not move. | killed | — |
| C-W43-24 | Ghost information: KV drop versus the same drop done as text | Step 0 teacher-forced divergence (~10 GPU-h) then two arms x 300 SWE-bench Verified tasks x 2 runs on GPT-OSS-120B (~110 GPU-h, ~$420 at $3.50 per GPU-hour, 10 days); kills if the paired 90% interval for the pass-rate difference lies insid… | parked | — |
| C-W44-09 | Drift or diffusion: the growth law of the prefix log-ratio separates arithmetic mismatch from cache-eviction mismatch | 60 trajectories, five teacher-forced passes each, one 8B model, about 30 GPU-h, about $110, 6 days; dead if $H^{E}$ and $H^{N}$ agree within 0.1 with overlapping bands. | killed | — |
| C-W44-10 | Does the eviction term reach the gradient: text recompute, InterQ-RL weights and operation-aware recompute on the same… | 128 rollouts under eviction, three recompute paths with backprop, one 8B model, about 60 GPU-h, about $220, 9 days; dead if the bias is under a quarter of the sampling noise and unstructured on both batches. | killed | — |

## Kill search

### Concept level (CL-W43-11) — killed (2026-11-01)
Both halves of the headline are published positives in the neighbours' own words — Memento 2604.09852 §6.2.1 (retained KV computed while the evicted block was visible is worth 15.3 AIME24 points; RL trained under physical KV compaction with a matched block-mask trainer) and MemoryWalker 2609.00865 (training on text the agent never saw inflates the train–rollout log-prob gap 26x; a 4D mask from eviction records is gradient-exact) — so the pre-registered surprise equals the field's stated knowledge (Gate 2B); density on the trainer half is 12 papers in 12 months with shipped incumbents (Gate 6).
Full record: [`data/reports/2026-W44-kill-CL-W43-11.md`](../../../data/reports/2026-W44-kill-CL-W43-11.md).
**Occupied by:** 2604.09852 (serving half: restart ablation; trainer practice: block-masked RL) and 2609.00865 (trainer half: measured gap and gradient-exact 4D mask)
**Why not done before:** The exact fix is cheaper than the measurement: with eviction records, one forward under a 4D or block mask reproduces the served conditioning for every token (MemoryWalker Theorem 1; Memento's vLLM fork and trainer, App. A.2.3), so no stack with records needs the size of the bias it removes; black-box stacks are MemoryWalker's SDCC case. Enabling pieces landed in order: ReSum 2025-09, Sparse-RL 2026-01, Memento 2026-04, MemoryWalker 2026-09, AKV 2026-10. The pressure #11 numerics evidence (vLLM post 2026-10-14: KL 2e-3 to 29.9; MoE routing flips) belongs to the arithmetic/routing line (CIS, DLC, R3/PR2/RDC) and the proposed CL-W44-04, not to this claim.
Closest neighbors (one-sentence trick; one-line difference):
- `2604.09852` MEMENTO: Teaching LLMs to Manage Their Own Context — Train a reasoning model to segment its chain of thought into blocks, summarize each, and physically evict the block's KV while keeping the summary's entries computed with the block visible; serve from a vLLM fork with block masking and train with RL under the… *Difference:* none — occupied: §6.2.1 is C-W43-24's same-text cache-kept-vs-rebuilt test (66.1% to 50.8% on AIME24, −15.3 pp); App. A.2.3 trains under physical KV compaction with a matched block-mask trainer (C-W44-10's g_op as default); untrained models, tool outputs and…
- `2609.00865` MemoryWalker: Stop Training Agents on Contexts They Never Saw — Treat a rollout under mid-trajectory context compression as a tree of conditioning branches, show that replaying the final context or the full history both train the wrong distributions, and recover exactness with a K-forward traversal or a packed 4D mask fro… *Difference:* none — occupied on the trainer half: train–rollout log-prob gap 0.366 vs 0.014 floor (26x) on eviction-heavy batches; 4D mask proven gradient-equivalent (Theorem 1); text-level editors on SGLang re-prefill rather than cache-level drops, same dense-attention c…
- `2609.37725` Context Language Models — Let the model edit its context as a file, train the editing with stepwise GRPO, and serve edits with Suffix Cache Reuse that keeps the unchanged suffix's KV computed under the pre-edit context and re-rotates positions. *Difference:* serving-side ghost channel used on purpose at matched accuracy, approximation named (App. B) and capped at K = 6 spans; RL rollouts served without it; cites Memento for the retained-information finding
- `2601.10079` Sparse-RL: Breaking the Memory Wall in LLM Reinforcement Learning via Stable Sparse Rollo… — Run RL rollouts under KV compression and correct the resulting off-policy bias with sparsity-aware rejection sampling and importance reweighting. *Difference:* states the trainer half as its premise (dense old policy vs sparse sampler policy vs learner); single-turn reasoning, no agent loop, no eviction record
- `2605.06850` How to Compress KV Cache in RL Post-Training? Shadow Mask Distillation for Memory-Efficie… — Sampler acts under a sparse context while the learner updates under the dense one; importance reweighting fails, so distill the sparse-context behaviour. *Difference:* same premise and register; names the failure of the correction family C-W44-09/10 would test; single-turn
**Narrowest surviving headline:** None at claim level. Footnote only: on a model never trained for cache compaction, harness-level eviction of old tool outputs (AKV, K = 12) leaves a ghost channel worth Delta pass-rate points over the identical trim done as text on SWE-bench Verified — Memento's restart ablation transplanted to the tool-agent cell both closest papers name as future work; expected sign is Memento's, so it is a service unless Delta is zero.
*Search degraded:* ['s2']

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- Promote as the systems-route champion candidate? Kill search owed; probe needs the released AKV engine.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-25 — claim open: written by the closing-W43 claims run from card 2610.28577's probes; C-W43-22 (pricing) attached to CL-W43-12 instead
- 2026-10-25 — claim open: claims (closing W43, after kills): re-ranked 6 (unchanged) after the kill run
- 2026-10-30 — claim open: nominated as a core-ML champion candidate (Jacob asked for a champion outside L5); kill search requested ahead of rank order; see PROGRAM-L1-evaluation-floors.md
- 2026-11-01 — claim killed: concept-level kill search (data/reports/2026-W44-kill-CL-W43-11.md): killed — Both halves of the headline are published positives in the neighbours' own words — Memento 2604.09852 §6.2.1 (retained KV computed while the evicted block was visible is worth 15.3 AIME24 points; RL trained under physical KV compaction with a matched block-mask trainer) and MemoryWalker 2609.00865 (training on text the…
- 2026-11-01 — C-W43-25 killed: killed with claim CL-W43-11 (concept-level kill search, data/reports/2026-W44-kill-CL-W43-11.md): MemoryWalker §6/Fig. 1 report the train–rollout log-prob gap by eviction density against the no-compression floor; Sparrow's per-token tail statistic is the same ruler in the sparse-attention register; the by-offset curve and the KV-level case are cells, not news.
- 2026-11-01 — C-W43-24 killed: killed with claim CL-W43-11 (concept-level kill search, data/reports/2026-W44-kill-CL-W43-11.md): The one-bit test (same text, cache kept vs rebuilt) is Memento §6.2.1 (−15.3 pp); Leyline ships both arms as modes. Step 0 survives only as an optional footnote attached to CL-W43-12.
- 2026-11-01 — C-W43-24 killed: claim_id CL-W43-11 -> orphan (re-homed after the kill searches)
- 2026-11-01 — C-W43-24 parked: kill note retains it as an orphan probe in footnote register: parked (not killed) with the trigger written
- 2026-11-01 — C-W44-09 killed: killed with claim CL-W43-11 (concept-level kill search, data/reports/2026-W44-kill-CL-W43-11.md): Its consequence (whether a sqrt(n) envelope absorbs the eviction term) is moot when the exact mask costs one forward; 2610.40945 characterizes the arithmetic term as a constant per-token bias removed by centering; the exponent contrast is unpublished and uncalled-for.
- 2026-11-01 — C-W44-10 killed: killed with claim CL-W43-11 (concept-level kill search, data/reports/2026-W44-kill-CL-W43-11.md): g_op is MemoryWalker's packed 4D mask (Theorem 1, gradient-equivalent) and Memento's trainer; the two naive arms are MemoryWalker's Pitfalls A and B (Delta_full about +18.5 nats per matched leaf); the InterQ-RL-weights arm answers a question no trainer with records asks.
- 2026-11-02 — claim open: pressure #11 (2026-11-02): Q08 'train-inference KL rose from 2e-3 to 29.9 while reward fell back [...] drops from 0.56 to 0.22' with 'neither baseline was thoroughly tuned'; L20 DeepSeek 'systematic improvements in the scale, diversity, and verifiability of synthesized data and environments account for essentially all of the observed gains'; the MoE-routing cause of mismatch named; records Q08, Q…
- 2026-11-02 — claim open: claims (W44 weekly run, 2026-11-02): C-W44-09 and C-W44-10 (card 2610.35303) attached — the growth-law and gradient-level probes of the trainer half; rank 6 -> 5

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W43-11`, version 5)
- probe `C-W43-25`: `data/candidates/2026-W43.jsonl`
- probe `C-W43-24`: `data/candidates/2026-W43.jsonl`
- probe `C-W44-09`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-10`: `data/candidates/2026-W44.jsonl`
