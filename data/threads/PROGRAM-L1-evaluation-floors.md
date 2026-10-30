# Program note — L1, "the noise floor of agent evaluation" (proposed 2026-10-30, after Jacob asked for a champion outside L5)

Status of the whole portfolio on 2026-10-30: no claim in any lane has a probe that survived both gates. L5 received the
most attention (two long sessions, a program note, a collaborator write-up) and all three of its survivors died in red
team; the L1–L4 claims have simply never had their kill searches — the weekly budget went to the top-ranked L5 probe and
to two L3/L4 probes that died. "No champion other than the simulator" is therefore "no champion yet, and the core-ML
claims are untested, not dead."

## The candidate program (core LLM evaluation; Princeton-local consumers)

One mechanism, three cheap measurements, mirroring L5's resolution-floor claim in the LLM world:
**the noise floor of agent evaluation is larger than the effects leaderboards and horizon curves report.**

| Claim | Headline (short) | Cheapest probe | Consumers |
| --- | --- | --- | --- |
| `CL-W43-14` | Leaderboard cost/effort effects come from single runs whose spread exceeds the differences ranked (HAL's cost table: one run per cell in all 6,204 cells; HAL's own text admits single runs) | $0 variance decomposition of released HAL logs; then a 4-effort × 60-task replication (~$300–600) | HAL (Princeton), every leaderboard, anyone citing an effort effect |
| `CL-W43-04` | The falling hazard in time-horizon curves is between-task frailty, not within-task degradation — hold the task fixed and the per-minute hazard is flat (METR's logistic-in-log-time is the gamma-frailty curve unnamed) | $0 frailty refit of METR-Horizon-v1.1 runs, 3 days | METR, forecasters, policy readers of horizon curves |
| `CL-W43-J01` | Temperature-0 run-to-run variance is the serving stack's batch arithmetic, not the agent, and grows with trajectory length | 20–60 GPU-h: default vs batch-invariant decoding, 10 repeats × 100 tasks | benchmark owners reporting T = 0 numbers |
| (`CL-W44-J01`) | Training-side cousin: agentic-RL environments are luck-dominated at the group sizes used | 20–40 GPU-h luck table | training teams (recipe half already in print) |

Why this and not another lane: measurement register with a standards consequence (what a leaderboard must report);
community-wide consumers; durable (a procedure, not a test set); lab-adjacent (measurement of labs' numbers); the
consumers sit on campus and on the Narasimhan route (τ-bench is the natural testbed); Jacob's edge (identities,
variance decompositions, GPU numerics) is load-bearing; every probe is under $600 or under one GPU-week.

## The other core-ML candidates, honestly

- `CL-W43-11` (L3): an agent served under KV-cache eviction is not the agent its transcript describes, and a trainer
  recomputing log-probabilities from text does not reproduce the sampled policy. Sharp, MLsys-core, on the systems route
  (Lloyd / Netravali / Dao); probe C-W43-25 (teacher-forced KL by turn offset) needs the released AKV engine. Second
  champion candidate; kill search owed.
- `CL-W43-10` (L1): scaffolds steer by presence, not content (same-length block from the wrong source moves yield as
  much). Cheap placebo design; kill-search risk from the in-context-learning precedent that random labels work (to fetch).
- `CL-W43-03` (L1) and `CL-W43-05` (L4): plausible, costlier ($1,000+), denser; `CL-W43-13` (L2): dense and lab-contested.

## What runs next

The week's three kill searches go to `CL-W43-04`, `CL-W43-14` and `CL-W43-11` instead of the rank order (which would spend
them on L5 again). Jacob steers this with marks in the `## Jacob` sections: `promote` on 04, 14, 11 (and J01); `park:
robotics route, revisit with a lab` on the L5 claims if he wants them out of the ranking. If two of the three survive, the
program is a champion candidate and gets its red teams; if none does, L1 is as dead as L5's first generation and the
honest next move is the claims stage's top-down pass on L2/L3 with the taste file.
