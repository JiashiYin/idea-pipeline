# On one 8-GPU node, self-GRPO on-policy distillation's reported $50\times$ FLOP saving over GRPO (on-policy distillation: training a student on its own rollouts under a frozen teacher's per-token supervision; FLOPs: floating-point operations) is less than half as large in node-hours (under $25\times$), because the $G = 1$ setting ($G$ rollouts per prompt) buys its FLOPs with eight times the optimizer steps on a decode-bound machine where a batch of 64 and a batch of 512 sequences take nearly the same time to generate.

`CL-W45-06` · lane **L3** · status **open** · rank 4 · position both · refreshed 2026-11-09

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established; Gate 2B flagged (direction stated in print). Next action: see First steps.

## The claim

- **Headline:** On one 8-GPU node, self-GRPO on-policy distillation's reported $50\times$ FLOP saving over GRPO (on-policy distillation: training a student on its own rollouts under a frozen teacher's per-token supervision; FLOPs: floating-point operations) is less than half as large in node-hours (under $25\times$), because the $G = 1$ setting ($G$ rollouts per prompt) buys its FLOPs with eight times the optimizer steps on a decode-bound machine where a batch of 64 and a batch of 512 sequences take nearly the same time to generate.
- **Current belief (the field's):** 2611.08453 App. A (card quote): 'Wall-clock and GPU-hours entangle the training objective with implementation and hardware; FLOPs is the only implementation-invariant compute metric'; abstract (fetched 2026-11-09): 'when the teacher is the student's own GRPO checkpoint, OPD recovers that checkpoint's accuracy on math with $50\times$ fewer distillation FLOPs than GRPO needs to reach the same accuracy'; App. I concedes the direction, not the size: the $G = 1$ setting 'takes longer in wall-clock time because it runs more optimizer steps'. The field reads the $50\times$ as a cost ratio a consumer would see (the Thinking Machines post's '7-10x fewer gradient steps => 50-100x compute efficiency').
- **If true:** FLOP-based efficiency claims for RL and distillation recipes state the batch shape and give node-hours beside FLOPs; the $G = 1$ recipe is retired for single-node users; the lane gets its datum that RL post-training cost on a node is sequential decode steps, not FLOPs, and a two-term cost model (decode steps plus FLOPs) predicts wall-clock across recipes and batch shapes.
- **If false:** The FLOP ledger survives the clock within a factor of two (ratio at or above 25 with $t_{\mathrm{step}}$ flat in batch): the ledger is vindicated as a cost proxy for this pair and the lane stops asking for wall-clock here; the residue is the first node-hour table for the pair, which the paper asks the field for and does not give.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the paper's own App. I sentence and its request for FLOP reporting; its audit finding that of 406 OPD preprints 'none evaluate their claimed advantage over outcome-reward methods like GRPO in terms of FLOPs' while the three that claim a compute win report GPU-hours or wall-clock (sec. 2, App. A); REOPOLD 2603.11137 'reports GPU-hours, wall-clock, optimizer steps, and rollouts' (card neighbour). Who pays: every team choosing between GRPO and distillation from its own checkpoints on a fixed node budget, and the multi-domain 'specialize, then consolidate' recipe whose 42% saving is also a FLOP number.
- **Impact ceiling:** **floor**: A replication note with the node-hour table and the $t_{\mathrm{step}}(B)$ curve, cited by the paper's v2 and by the next OPD-efficiency paper. Requires steps 0-2. Judgment p 0.55.; **middle**: A reporting rule (FLOPs with batch shape and node-hours side by side) taken up by one RL framework's benchmark page and by the paper's authors; the multi-domain consolidation pair timed the same way at about 150 GPU-h more. Judgment p 0.3.; **ceiling**: A two-term cost model for RL post-training on a node (sequential decode steps plus FLOPs) that predicts wall-clock across recipes and batch shapes, adopted by the systems lane as the unit in which recipe efficiency is quoted. Requires two more nodes and three more recipes. Judgment p 0.1.
- **Relevance:** Narasimhan route: indirect (post-training efficiency). Systems route (Lloyd, Netravali, Tri Dao): direct — decode-bound RL cost is their subject. Industry: direct for anyone sizing a distillation run. Jacob's edge: the latency model, the timing instrumentation and the GPU memory accounting are computer engineering; statistics for the crossing-time bands; theoretical physics zero.
- **Kill probe:** Steps 0-2: about 130 GPU-h on one 8-GPU node, $0 on owned GPUs, 7 days; dead if GRPO's node-hours to 33.9% are at least 25 times OPD-$G=1$'s.
- **Density and ownership:** Closest: 2611.08453 (the pair, FLOPs only); REOPOLD 2603.11137 (wall-clock for a different OPD objective, matched steps); ZPPO 2606.18216 (OPD slower in wall-clock, external teacher); SCOPE 2604.10688 ($G = 8$ vs $G = 1$ mismatch). Pre-window precedents: Pope et al. 2022 (memory-bound decode, latency flat in batch), the Thinking Machines OPD post (2025). Density role words: wall-clock, GPU-hours, node-hours, throughput, decode-bound, batch size, optimizer steps, rollouts per step, self-distillation, GRPO checkpoint. Nobody owns the timing table; the paper's authors have the node.
- **Why now:** 2611.08453 (2026-11-05): FLOP-only comparison and its App. I admission; verl 0.8 native OPD; public models and data; the 50x is being quoted.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | mechanism written first: a batch of $B$ sequences decodes in about $L_{\max} \cdot t_{\mathrm{step}}(B)$ seconds ($L_{\max}$ the longest response in the batch, $t_{\mathrm{step}}(B)$ the per-token latency of one decode step, nearly flat in $B$ until the KV-cache memory limit), while the FLOP ledger charges $10 N_s$ per generated token ($N_s$ the student's parameter count), linear in $B$; one seed per arm as in the paper (every curve there is a single run), crossing times reported as a band (first crossing of 33.9 minus 1 and plus 1) with a seed replicate of the cheapest arm if the band spans… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: about 130 GPU-h on one node, under one GPU-week; kill written: GRPO's node-hours to the 33.9% band at least 25 times OPD-$G=1$'s with step 0 showing $t_{\mathrm{step}}$ flat in $B$ |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route A: the paper's own App. I and Limitations ask the field for FLOP reporting while conceding wall-clock runs longer; REOPOLD 2603.11137 reports GPU-hours and wall-clock; the Thinking Machines post 'reports no method-separated GPU-hours or wall clock' (the paper's bibliography note) — three source types. Route B flag: the direction is in print and the magnitude is the content, so Gate 2B is the red team's first objection |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | consumers with actions: teams sizing a distillation run on a fixed node budget (choose $G$ by the node's $t_{\mathrm{step}}$ curve), recipe authors (report node-hours with batch shape), RL framework benchmark pages (a two-term cost model as the unit). One community (post-training efficiency) with a systems consumer — proper-shaped |
| G4 | mechanism and consequence | mechanism: decode is memory-bound so per-step time is nearly flat in batch (Pope et al. 2022); consequence: FLOP ratios overstate node-hour ratios by about the step-count ratio, or the ledger stands |
| G5 | durability; lab-adjacent | the two-term cost model is durable across recipes and nodes (the curve predicts another node's ratio); the 50x number expires with the next recipe; lab-adjacent (cost accounting of a published comparison) |
| G6 | ownership, density, race window; position clause | unmeasured: kill search owed (role words: wall-clock, GPU-hours, node-hours, throughput, decode-bound, batch size, optimizer steps, rollouts per step, self-distillation, GRPO checkpoint). Nearest: REOPOLD 2603.11137 (wall-clock for a different OPD objective at matched steps), ZPPO 2606.18216 (fetched 2026-11-09: a teacher-in-prompt method that 'outperforms off/on-policy distillation and GRPO'; its wall-clock table must be read), SCOPE 2604.10688 (the $G = 8$ vs $G = 1$ mismatch); pre-window: Pope et al. 2022 (memory-bound decode, latency flat in batch), the Thinking Machines OPD post (2025).… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W45-08 | The 50x on a clock: self-GRPO distillation against GRPO in node-hours, where rollouts inside a batch are nearly free an… | Steps 0-2: about 130 GPU-h on one 8-GPU node, $0 on owned GPUs, 7 days; dead if GRPO's node-hours to 33.9% are at least 25 times OPD-$G=1$'s. | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W45-08** (Sunday run), or run `/kill C-W45-08` in a session.
2. If it survives: `/redteam C-W45-08`, then the probe as pre-registered — Steps 0-2: about 130 GPU-h on one 8-GPU node, $0 on owned GPUs, 7 days; dead if GRPO's node-hours to 33.9% are at least 25 times OPD-$G=1$'s.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-08 — claim open: filed (claims, W45) by lifting C-W45-08 into L3 (the lane sentence names cost structure); headline quantifier ('less than half as large, under 25x') is the probe's kill; C-W45-09 (judge dollars, ORSD) left orphan at L2's cap; concept-level kill search owed (rule 17); ranked 15
- 2026-11-08 — claim open: re-ranked after the W45 kill searches: rank 4: born this week; kill search owed; Gate 2B flagged at filing

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W45-06`, version 2)
- probe `C-W45-08`: `data/candidates/2026-W45.jsonl`
