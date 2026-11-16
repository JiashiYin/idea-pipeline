# On one 8-GPU node, self-GRPO on-policy distillation's reported $50\times$ FLOP saving over GRPO (on-policy distillation: training a student on its own rollouts under a frozen teacher's per-token supervision; FLOPs: floating-point operations) is less than half as large in node-hours (under $25\times$), because the $G = 1$ setting ($G$ rollouts per prompt) buys its FLOPs with eight times the optimizer steps on a decode-bound machine where a batch of 64 and a batch of 512 sequences take nearly the same time to generate.

`CL-W45-06` · lane **L3** · status **killed** · rank None · position both · refreshed 2026-11-16

## Status

Killed — see the kill section. Failing gate: Gate 2B (2608.29296 owns the two-term cost model and the decision rule); Gate 6 (occupied 2026-08-29); Gate 0 (decode is not flat in batch past 1-2K tokens at 4B: the two-term Roofline gives a ratio of 15-25, on the claim's own kill line). Next action: see First steps.

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
| G6 | ownership, density, race window; position clause | concept-level kill search 2026-11-15 (data/reports/2026-W46-kill-CL-W45-06.md): killed; gate failed G2B; occupied_by 2608.29296; why not done: Done for the mechanism and model (2608.29296, GRPO on fixed hardware); the pair's clock is unpublished because the card paper chose FLOPs on principle (App. A) and wrote the wall-clock fact as a sentence (App. I); its authors hold the node and logs.. Previous: unmeasured: kill search owed (role words: wall-clock, GPU-hours, node-hours, throughput, decode-bound, batch size, optimizer steps, rollouts per step, self-distillation, GRPO checkpoint). Nearest… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W45-08 | The 50x on a clock: self-GRPO distillation against GRPO in node-hours, where rollouts inside a batch are nearly free an… | Steps 0-2: about 130 GPU-h on one 8-GPU node, $0 on owned GPUs, 7 days; dead if GRPO's node-hours to 33.9% are at least 25 times OPD-$G=1$'s. | killed | killed ([record](../../../data/reports/2026-W46-kill-CL-W45-06.md)) |

## Kill search

### Concept level (CL-W45-06) — killed (2026-11-15)
The surprise (a FLOP saving bought by a smaller per-step rollout batch does not appear on the clock because decode is memory-bound; a two-term decode-plus-FLOPs cost model predicts wall-clock) is the stated thesis, eq. 4, Roofline appendix and measured GRPO sweep of 2608.29296 (2026-08-29); the direction is conceded in the card paper's App. I and the FLOPs-vs-GPU-hours gap is stated by the source of the 50x; the headline's 'nearly the same time' omits the KV-cache read, linear in batch, so the predicted node-hour ratio (15-25) sits on the claim's own kill line and the probe fits a coefficient, not a belief.
Full record: [`data/reports/2026-W46-kill-CL-W45-06.md`](../../../data/reports/2026-W46-kill-CL-W45-06.md).
**Occupied by:** 2608.29296
**Why not done before:** Done for the mechanism and model (2608.29296, GRPO on fixed hardware); the pair's clock is unpublished because the card paper chose FLOPs on principle (App. A) and wrote the wall-clock fact as a sentence (App. I); its authors hold the node and logs.
Closest neighbors (one-sentence trick; one-line difference):
- `2608.29296` When Do Larger Batches Help Scale LLM Reinforcement Learning? — Split time-to-target into samples-to-target (made batch-invariant by square-root learning-rate scaling) times generation throughput (sublinear in batch because low-concurrency decode is memory-bandwidth-bound while training FLOPs grow linearly), and raise the… *Difference:* none — occupied: eq. 4 is the two-term cost model, sec. 4.1 measures it for GRPO and PPO on fixed hardware (4x responses: 2.93x and 1.74x time), App. A's Roofline carries the KV term; not done there: OPD, a self-teacher, the 2611.08453 pair
- `2611.08453` Unpacking the Compute Efficiency of Strong-to-Weak OPD against GRPO — Lay a parameter-count FLOP ledger under accuracy curves; only the student's own GRPO checkpoint is recovered cheaply (6x at G=8, 50x at G=1). *Difference:* occupies the pair in FLOPs; concedes the direction in App. I ('It takes longer in wall-clock time because it runs more optimizer steps'); reports no wall-clock, GPU-hours or memory for any pair
- `2510.00977` It Takes Two: Your GRPO Is Secretly DPO — Replace 16 rollouts per prompt by 2 and raise the prompt batch so each step still holds 512 rollouts; performance is kept at 97.6%. *Difference:* a published rollouts-vs-clock divergence for GRPO group-size reduction ('12.5% of its total rollouts and 21.0% of its training time'), at matched per-step batch; its App. D.2 takes the FLOPs-first stance
- `2603.11137` Scaling Reasoning Efficiently via Relaxed On-Policy Distillation (REOPOLD) — Apply teacher credit only where, how strongly and when token-level signals warrant it, for a 12x sample-efficiency gain over sampled-token OPD. *Difference:* the per-step wall-clock breakdown of an OPD step on one 8-GPU node is in print (Fig. 15: generation 77.3%, teacher 8.2% at 8,192 tokens); external teacher, matched 300 steps, no self-teacher clock
- `2610.18853` Two Clocks: Why Larger Rollout Batches Learn Slower but Fail on Schedule in RLVR — Under a local quadratic model, larger rollout batches with square-root learning-rate scaling preserve drift per sample but not progress, so sample efficiency degrades past a critical batch. *Difference:* the sample side of the same tradeoff; no clock
*Search degraded:* ['s2', 'conference-exports-not-built', 'arxiv-Q9-rate-exceeded', 'arxiv-Q10-rate-exceeded', 'webfetch-blocked-thinkingmachines-url (fetched with curl instead)']

### C-W45-08 — killed (2026-11-15)
A footnote, not a claim: the node-hour row for the 2611.08453 pair on its node (predicted GRPO/OPD-G=1 ratio 15-25 by eq. 4 of 2608.29296 from the measured t_step(B)), best obtained by asking the authors for the wall-clock number behind their App. I sentence; filed as a watch item with an automatic close on the first published timing of the pair.
Full record: [`data/reports/2026-W46-kill-CL-W45-06.md`](../../../data/reports/2026-W46-kill-CL-W45-06.md).
Per position — **solo**: not yet kill-searched; **lab**: not yet kill-searched
**Occupied by:** 2608.29296

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

- 2026-11-08 — claim open: filed (claims, W45) by lifting C-W45-08 into L3 (the lane sentence names cost structure); headline quantifier ('less than half as large, under 25x') is the probe's kill; C-W45-09 (judge dollars, ORSD) left orphan at L2's cap; concept-level kill search owed (rule 17); ranked 15
- 2026-11-08 — claim open: re-ranked after the W45 kill searches: rank 4: born this week; kill search owed; Gate 2B flagged at filing
- 2026-11-15 — claim open: claims (W46, 2026-11-15): rank 4 -> 11; kill search owed; Gate 2B flagged at filing
- 2026-11-15 — claim killed: concept-level kill search (data/reports/2026-W46-kill-CL-W45-06.md): killed — gate G2B; The surprise (a FLOP saving bought by a smaller per-step rollout batch does not appear on the clock because decode is memory-bound; a two-term decode-plus-FLOPs cost model predicts wall-clock) is the stated thesis, eq. 4, Roofline appendix and measured GRPO sweep of 2608.29296 (2026-08-29); the direction is co…
- 2026-11-15 — claim killed: failing gate recorded after the W46 kill search: Gate 2B (2608.29296 owns the two-term cost model and the decision rule); Gate 6 (occupied 2026-08-29); Gate 0 (decode is not flat in batch past 1-2K tokens at 4B: the two-term Roofline gives a ratio o
- 2026-11-15 — C-W45-08 killed: claim-level kill search of CL-W45-06 (data/reports/2026-W46-kill-CL-W45-06.md): killed — killed with the claim: step 0 is the occupant's profile, the kill line sits inside the occupant model's predicted band, and the pre-registered 'r flat' mechanism check fails by the KV-cache term; a 50 GPU-h timing row remains as a footnote/watch item, not a probe

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W45-06`, version 5)
- probe `C-W45-08`: `data/candidates/2026-W45.jsonl`; kill record `data/reports/2026-W46-kill-CL-W45-06.md`
