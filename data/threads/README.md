# Threads — one folder per claim, one note per folder

Refreshed 2026-10-20. Each `THREAD.md` is regenerated from the records by `python scripts/threads.py`; your
`## Jacob` section is preserved verbatim. Read a note top to bottom: Status, the claim, scorecard, gates, probes,
kill search, red team, first steps, decisions — then write in your section. Ranked by the claims stage.
Lost? The user guide is [`README.md`](../../README.md) at the repository root.

> **A run is in progress** (scheduled red-team run, started 2026-10-20T06:02:25Z UTC) on: C-W43-15, C-W43-13, C-W43-01, CL-W43-01, CL-W43-02, CL-W43-06. Leave those records alone until it pushes.

| Rank | Lane | Claim | Status | Headline | Probes (survived) | Cheapest | Failing gate | Folder |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | L5 | CL-W43-01 | open | GPU physics engines trade physics for speed through solver iteration caps, and RL policies trained in them exploit the difference. | 4 (0) | C-W43-17 | G1 (no live probe of the exploit clause) and headline defec… | [`CL-W43-01-gpu-physics-engines-trade-physics-for-speed-thro`](./CL-W43-01-gpu-physics-engines-trade-physics-for-speed-thro/THREAD.md) |
| 2 | L1 | CL-W43-02 | open | Most published real-to-sim validity claims rest on policy pairs their own real-world sample cannot resolve. | 1 (1) | C-W43-13 | none on paper; survival is by scope and statistic, not by t… | [`CL-W43-02-most-published-real-to-sim-validity-claims-rest`](./CL-W43-02-most-published-real-to-sim-validity-claims-rest/THREAD.md) |
| 3 | L1 | CL-W43-04 | open | The falling hazard in agent time-horizon curves is between-task frailty, not within-task degradation: hold the task fixed and the per-minute hazard is flat. | 1 (0) | X-2026-W42-S7F9 | Gate 6 not yet established; Gate 1 blocked on paperwork (no… | [`CL-W43-04-the-falling-hazard-in-agent-time-horizon-curves`](./CL-W43-04-the-falling-hazard-in-agent-time-horizon-curves/THREAD.md) |
| 4 | L2 | CL-W43-06 | open | Published step-credit critics for long-horizon agents do not beat their own shuffled control in the first two thirds of a trajectory. | 2 (1) | C-W43-01 | none on paper; Gate 3 at one community; red team owed | [`CL-W43-06-published-step-credit-critics-for-long-horizon-a`](./CL-W43-06-published-step-credit-critics-for-long-horizon-a/THREAD.md) |
| 5 | L4 | CL-W43-05 | open | Compaction summaries fail by unsourced persistence — claims no observation supports — not by length. | 3 (0) | C-W43-09 | Gate 6 race window (golden); Gate 5 durability graded weak;… | [`CL-W43-05-compaction-summaries-fail-by-unsourced-persisten`](./CL-W43-05-compaction-summaries-fail-by-unsourced-persisten/THREAD.md) |
| 6 | L1 | CL-W43-03 | open | Reported scaffold gains on agent benchmarks are mostly reasoning-effort and restart effects, not scaffold design. | 2 (0) | C-W43-12 | Gate 6 not yet established; Gate 1 borderline on dollars | [`CL-W43-03-reported-scaffold-gains-on-agent-benchmarks-are`](./CL-W43-03-reported-scaffold-gains-on-agent-benchmarks-are/THREAD.md) |
| 7 | L3 | CL-W43-07 | open | Whether prefill-decode disaggregation pays for an agent workload is set by the measured temporal overlap of prefill with decode, not by turn count. | 1 (0) | C-W43-05 | Gate 6 not yet established | [`CL-W43-07-whether-prefill-decode-disaggregation-pays-for-a`](./CL-W43-07-whether-prefill-decode-disaggregation-pays-for-a/THREAD.md) |
| 8 | L3 | CL-W43-08 | open | At the concurrency of asynchronous agentic RL, a backlog-threshold rule captures as much of the hindsight-optimal prefill-decode role-switching headroom as a d… | 1 (0) | C-W43-04 | Gate 6 not yet established | [`CL-W43-08-at-the-concurrency-of-asynchronous-agentic-rl-a`](./CL-W43-08-at-the-concurrency-of-asynchronous-agentic-rl-a/THREAD.md) |
| 9 | L5 | CL-W43-09 | open | GPU physics engines cannot resolve the policy-return differences that robot-RL papers report as improvements: engine-only repeatability and batch-position vari… | 0 (0) | import:2026-W43-S4xF9 | Gate 6 not yet established; Gate 1 blocked on paperwork (no… | [`CL-W43-09-gpu-physics-engines-cannot-resolve-the-policy-re`](./CL-W43-09-gpu-physics-engines-cannot-resolve-the-policy-re/THREAD.md) |

## Orphan probes (no claim yet)

Probes without a headline are footnotes until a claim is written over them (three on one theme = a missing claim).

- `C-W43-02` (L1; failure localization on capped runs) — headline-worthy: failure-localization labels and restart gains on capped runs measure the clock, not the agent; L1 at its two-new-claims-per-week limit (three seeded 10-19), so written next week
- `C-W43-06` (L1; scaffold-model interaction) — tests whether unscaffolded behaviour predicts the sign of a scaffold effect
- `C-W43-07` (L1; scaffold-model interaction) — tests prompt-form versus content for one scaffold's harm
- *Flag:* two L1 orphans on scaffold-model interaction; a third makes a missing claim (prompts/11_claims.md rule)
