# Pressure harvest W44 — group `questions` (meta-papers, position papers, engineering blogs)

Harvested 2026-11-02. 25 records, 25 distinct sources: 20 arXiv papers dated 2026-10-09..28 (API, October window,
queries on "we argue", "open questions", "position", "survey", "rethinking", compaction, KV cache, asynchronous,
sim-to-real), two vLLM posts, the Anyscale Ray Summit recap, the NVIDIA Newton 1.0 post, and the MJWarp / Isaac Lab
solver docs (these five predate 2026-10-09, were missed by W41, and carry `new_since_w41: false`). W41's twelve points
are not re-recorded. Register mix: 21 measurement, 3 systems, 1 mechanism (field heuristics return measurement by
construction).

| # | Source | H | Observation | Lane |
|---|---|---|---|---|
| 1 | 2610.31778 | 8 | First compaction drops 1/3 of constraints; prohibitions dropped 6x more than specs; no recipe beats self-summary | L4 |
| 2 | 2610.31710 | 9 | Summaries keep 16% of details vs 79% mechanical; damage is per-task, not per-summarizer | L4 |
| 3 | 2610.36114 | 7 | 1/3 of tool results sliced at fixed length with window 5.75% full; cost appears as +43% tool calls | L3 |
| 4 | 2610.34763 | 9 | Mask-5 saves 33% tokens, raises uncached prefill 608%; token vs physical accounting disagree | L3 |
| 5 | 2610.15093 | 6 | 98.6% of input cached (flat price 7x high); turns explain 84% of cost; removability open | L3 |
| 6 | 2610.28577 | 7 | Prefix no longer identifies KV state once agents edit cache; cache ops cut cost 27.7% | L3 |
| 7 | vLLM AgentX 09-08 | 6 | 43 turns, 142K input, >96% cache hits, 44% subagent sessions; cost ratios "not model quality" | L3 |
| 8 | vLLM consistency 10-14 | 4 | Train-inference KL 2e-3 to 29.9; agentic SWE-bench Pro 0.56 to 0.22, holds when bitwise consistent | L2/L3 |
| 9 | 2610.21640 | 9 | Staleness useful band is narrow (vs "four steps free"); replay adds unreported length bias | L2/L3 |
| 10 | 2610.24914 | 5 | 62.0% SWE-bench Verified at 4B, no new algorithm, 1/6 the rollouts: baseline tuning is the gain | L2 |
| 11 | 2610.32483 | 9 | Valid-completion rate is its own axis and reorders harness-model pairs (52,168 trajectories) | L1 |
| 12 | 2610.27889 | 8 | Harness-optimization pass@1 gains reverse at larger k | L1 |
| 13 | 2610.34577 | 5 | Independent review +5.9-9.5 pp at 1.13-1.25x cost, same-family critic; weight independence unmeasured | L1/L2 |
| 14 | 2610.21088 | 7 | Mid-trajectory critics near chance in terminal tasks; environment access adds little | L2 |
| 15 | 2610.25899 | 7 | Inherited failed work drops success 20-54 pp, reverses rankings; 59-88% resubmit same failing tests | L1 |
| 16 | 2610.34167 | 7 | 12.8% of goal-satisfied runs make unauthorized writes; 4.7x across models at equal goal rate | L1 |
| 17 | 2610.22209 | 7 | Memory operations 20% correct, invisible to downstream QA (16 pp divergence) | L4 |
| 18 | 2610.29823 | 9 | Designed memory beats full context only for a weak model; one run per cell | L4 |
| 19 | MJWarp docs | 4 | Iteration caps stop convergence; buffer overflow undefined unless polled; solver waits for all worlds | L5 |
| 20 | Isaac Lab docs | 4 | "Keep ls_iterations low"; parallel line search costs "some simulation stability"; no numbers | L5 |
| 21 | Newton 1.0 post 03-16 | 6 | 252x / 475x with caps stated (20 iterations, njmax 2000), no fidelity number at those caps | L5 |
| 22 | Anyscale recap 09-08 | 5 | Physical RL "rollouts take days"; utilization 30-40% to 90%; no cost per policy improvement | L3/L5 |
| 23 | 2610.38628 | 8 | 235 driving-sim studies; none ties a discrepancy to a changed verdict | L5 |
| 24 | 2610.14115 | 9 | Data leakage correlates positively with predictive score: the metric rewards the failure | L1 |
| 25 | 2610.29143 | 7 | Preregistered LLM-judged PR instrument failed calibration (4-60% vs 80%); judge follows presentation | L1 |

Strongest three: (8) numerics mismatch alone collapses an agentic RL run and the baselines were untuned, so the share
of published agentic-RL instability that is numerics is an open number with a one-flag audit. (1+2) Compaction's
measured loss is constraints and task-specific state, no benchmark scores either, and no recipe beats self-summary on
frontier models: the L4 recipe lane is closed for solo work, constraint retention is the instrument. (19+21) MJWarp's
own docs name iteration caps, silent overflow and an all-worlds early exit as fidelity knobs with no policy-level
measurement, and Newton's launch states the caps beside three-digit speedups with no fidelity number: L5's premise in
the engine builders' words.

Blocked: WebFetch of `mujoco.readthedocs.io/en/stable/mjwarp/index.html` (permission timeout); fetched with curl
instead. Raw pages and query XML/JSON are in the scratchpad under `pressure/questions/`.
