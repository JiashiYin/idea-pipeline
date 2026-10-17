# Pressure points — agentic benchmarks and leaderboards (2026-W41)

Harvest date 2026-10-09. Every number below was fetched on that date from the source named in the row; dates in
parentheses are the source's own dates. Records: `data/pressure/2026-W41/benchmarks.jsonl` (71 lines). Terms:
*pass@1* = share of tasks solved in one run; *pass@k* = solved in at least one of k runs (optimistic);
*pass^k* = solved in all k runs (pessimistic, a reliability measure); *scaffold/harness* = the fixed code around
the model that decides tools, retries and prompts.

## 1. Benchmark table

| Benchmark | Top score (date) | Human / expert ceiling | Reliability metric shown | Cost reported? | Entries | Main validity issue | Source |
|---|---|---|---|---|---|---|---|
| SWE-bench Verified | Official table not fetchable (JS; GitHub API 403). Aggregator of self-reports: Claude Opus 5 96% (2026-10-09); uniform mini-swe-agent-v2 chart tops at 75.6% (Opus 4.6) | none on page | none (pass@1 only); 2602.07150: single-run spread 2.2–6.0 pp, SD >1.5 pp at temp 0 | plots only, no column | 82 aggregator rows: 76 self-reports, 0 owner/independent | memorization: 3x better file localization than on fresh repos (2512.10218); self-report vs uniform-harness gap ~20 pts | swebench.com; benchlm.ai; arXiv 2602.07150, 2512.10218 |
| SWE-bench Pro (public) | Muse Spark 1.1 61.50 ±3.10 (no entry dates) | none reported | 95% CI only | no $; capped (50 turns) and uncapped (250 turns) runs mixed | 25 | top-2 gap 2.4 pts inside ±3.1–3.6 CIs; held-out 858 tasks never published; contamination resistance asserted via licence | labs.scale.com |
| SWE-rebench | Fable 5 [high] 64.5 ±1.41, pass@5 78.4 (window 2026-05-15→07-01) | none | pass@5 (no pass^k) | yes: $/problem ($0.41–$4.40), tokens, cached share 85–96% | 117 rows, rows 18–117 N/A | small rolling population; pass@5 reorders top (GLM-5.2 81.1); cost depends on caching convention | swe-rebench.com |
| Terminal-Bench 2.0 | NexAU-AHE / GPT-5.5 84.7 ±2.1 (2026-05-14); paper said "<65%" (2026-01-17) | author-estimated expert time only (48.6% <1 h, 47.3% 1 h–1 day) | ± (95% CI per paper) | leaderboard: none; paper: "$1 to $100" per run, up to 100M tokens/task | 142 (team-verified) | top-5 within 2.5 pts, 3 of 5 same model; scaffold chosen to maximize; version 4.0 page already live | tbench.ai; arXiv 2601.11868 |
| τ²-bench / τ³ | τ²: Qwen3.5-397B-A17B pass^1 87.9%; τ³-Banking: Qwen 3.8 Max 55.2% (Jul 2026) | none | pass^1 only displayed (pass^2–4 columns exist but not visible) | no | τ³-Banking 27; τ² "⋯" | 50+ airline/retail tasks fixed Feb 2026; grader version <1.0.1 not comparable; one frozen user sim (gpt-5.2); 4 native scaffolds shift reward up to 0.267 (2609.09218) | taubench.com; github tau2-bench; HAL reliability |
| hyper-τ-bench (τ^τ) | Claude Opus 5 / Claude Code 23.9% held-out (2026-09-08) | engineer-built reference agents 95–100%; same model with engineer context 82.2% | none | cost is a scored budget: 3.0x/1.3x over → 0; survivors use 0.45x | n/a | cheating attempts in 17–42% of runs; <80 of ~1,700 spec files read | sierra.ai blog |
| BrowseComp | GPT-5.6 Sol Ultra 92.2% self-reported, 4 parallel agents; Mythos 5 multi-agent 93.3% listed but not reconciled (page 2026-09-04) | not on page | none | none for top 10; ~$0.50/query only for search-API rows | 100 (aggregator) | all top-10 self-reported, mixed single/multi-agent and graders | leaderboard.steel.dev (aggregator) |
| GAIA | official HF table: fetch-failed; HAL: 74.5% at $178.20 (Sept 2025) | not fetched | none | HAL: yes | HAL paused Sept 2025 | 3 scaffold data leaks + every .xlsx task failing (HAL reliability) | hal.cs.princeton.edu |
| Gaia2 | CLI board: Claude Opus 4.6 57.0% (2026-04-13); vanilla: GPT-5 42.1 (2025-09-09) | none | none | none | 7 CLI; 16 vanilla | all self-reported; Time split 0.8–5.0% for every model; Noise and A2A splits dropped on CLI board | meta-agents-research-environments-leaderboard.hf.space; arXiv 2602.11964 |
| OSWorld-Verified → 2.0 | Verified: Opus 4.8 83.5% vs human 72.36%; 2.0: Opus 4.8 20.6% binary / 54.8% partial at 500 steps (2026-07-15) | 2.0: human median 1.6 h, no human success rate | none (single runs) | 2.0 paper: ~$72.4 and ~$35.8 per task | not shown | agents beat the human figure on v1; binary completion → 0 on longest tasks; residential proxy, pauses, simulated user | osworld-v1.xlang.ai; arXiv 2606.29537 |
| METR time horizons | Claude Mythos Preview p50 1044.8 min [508.9, 3304.3] (2026-04-07); doubling 128.7 d [104.4, 158.0] | human task times "likely overestimate" | p80 horizon: 4–10x shorter than p50 (Opus 4.6: 718.8 vs 69.9 min) | no $; ~1,000 runs, 1–2 weeks | 27 model points | newest p50 exceeds the 16 h reliability limit of the suite; three current models unmeasured | metr.org YAML v1.1 |
| HAL | SWE-bench Verified Mini 72.0% at $463.90; CORE-Bench "solved" 77.8% (95.5% manual) | n/a | none (single runs, $40k total) | yes (Pareto) | 26,597 rollouts, 9 benchmarks; paused | 21 of 36 reasoning-effort increases → equal/lower accuracy; shortcuts (gold answers on HF/arXiv); endpoint weight swaps | hal.cs.princeton.edu; arXiv 2510.11977 |
| HAL Reliability Tracker | accuracy top Gemini 3.5 Flash 80.0%; reliability top Claude Opus 4.5 0.87 (models to Jan 2026) | n/a | outcome consistency (2p̂−1)², Traj-D/S, calibration | no | 15 agents, 2–3 benchmarks | estimator bug (K/(K−1)) zeroed non-unanimous tasks; Opus 4.8 absent | hal.cs.princeton.edu/reliability |
| Toolathlon | GLM 5.3 Flash 78.4 ±1.9 pass@1 (2026-08-30) | none | pass@3 and pass^3 for 5 of 7 rows; gap 15–24 pts | no | 7 shown | pass^3 missing for the newest/top rows; turns 19.9–45.3 vs "≈20" typical | toolathlon.xyz |
| BFCL v4 | table not in page text (2026-04-12) | n/a | none | yes: whole-benchmark $ and latency | n/a | unweighted category average; no variance | gorilla.cs.berkeley.edu |
| MLE-bench | Famou-Agent 2.0 64.44 ±1.18 (2026-02-23); AIDE 7.56 (2024-10) | Kaggle medal thresholds | SEM over ≥3 seeds; incomplete seeds padded with failures | no $ (24 h, 36 vCPU, A10 per run) | 7 main + extras; closed 2026-04-24 | known label leaks kept "to avoid invalidating the leaderboard" | github.com/openai/mle-bench |
| Vending-Bench 2 | GPT-6 Astra $15,514.70 ±$1,074 | modeled "good strategy" ≈$63k/yr; no human run | ± undefined; runs/model unstated | chart only; 60–100M output tokens/run | 69 | fixed 69k-token trimming policy; "no ceiling" vs $63k reference | andonlabs.com |
| ARC-AGI-3 | table not in page text | "100% human-solvable"; score = efficiency vs humans | n/a | display cutoff $10,000/run | n/a | nothing auditable from page | arcprize.org |
| OpenHands Index | Opus 4.7 top (2026-05-11), numbers in charts only | n/a | none | named axis, no numbers in text | n/a | unverifiable trend claim | openhands.dev blog |

Fetch failures (recorded, not retried beyond once): swebench.com Verified table (two URL forms, JS-rendered);
GitHub API `SWE-bench/experiments` (HTTP 403, not routed around); tbench.ai/leaderboard (4.0 page, empty table);
GAIA HF space (did not load); os-world.github.io/osworld-2 (error); appworld.dev/leaderboard (error) and appworld.dev
(redirect stub); webarena.dev (project index only); arcprize.org/leaderboard and BFCL tables (not in page text);
taubench.com/leaderboard τ² tab (only τ³-Banking rendered). Not attempted for time: PaperBench, SWE-Lancer, HLE
agentic configs, SWE-bench Live, AgentBench suites.

## 2. Observations by heuristic

**H1 Dropped metrics / dropped versions.** τ-bench's leaderboard shows pass^1 only although the benchmark's
framing is "the passk reliability metric" (taubench.com). Gaia2's newer CLI board drops the Noise and Agent-to-Agent
splits that scored lowest on the vanilla board (35.4, 17.9). Terminal-Bench 2.0's leaderboard has no cost column;
the empty 4.0 board adds COST and TOKENS. MLE-bench closed submissions 2026-04-24 at 64%. HAL paused in Sept 2025.
SWE-rebench carries 100 rows with no metrics. METR has no horizon for Claude Opus 4.7, Grok 4.3, GPT-5.5.
Toolathlon's two newest top entries omit pass^3.

**H2 Saturation with unreliability.** 2602.07150: 60,000 SWE-bench Verified trajectories, single-run spread 2.2–6.0
pp, SD >1.5 pp at temperature 0, pass@k–pass^k gap up to 24.9 pp. SWE-bench Pro top two inside their CIs.
Terminal-Bench 2.0 top five within 2.5 pts with ±2.1–2.8. Toolathlon pass^3 15–24 pts under pass@3. METR p80
horizons 4–10x shorter than p50, CIs spanning 6–11x. HAL tracker: "reliability is not improving at nearly the same
rate" as accuracy. OSWorld 2.0: partial score 54.8% vs binary 20.6%, binary → 0 on longest tasks.

**H3 Expert-gap anomalies.** hyper-τ-bench: 23.9% alone vs 82.2% with engineer context vs 95–100% reference agents
on identical held-out tasks. OSWorld-Verified: agents (83.5%) above the human figure (72.36%) — ceiling was a floor.
Gaia2 Time split 0.8–5.0% beside Execution 79–83%. Vending-Bench 2 best ≈25% of the modeled good strategy. No
measured human success rate on SWE-bench Pro, Terminal-Bench 2.0, OSWorld 2.0 (time only), Toolathlon, Vending-Bench.

**H4 Workarounds as evidence.** Temperature 0 (does not give determinism, sometimes raises variance — 2602.07150).
HAL's hand-curated 26-task "clean" airline subset. Max-over-scaffolds reporting (Terminal-Bench). τ-bench's four
native scaffolds shift reward up to 0.267 (2609.09218). SWE-bench Pro's capped/uncapped mix. MLE-bench keeps known
leaks to preserve comparability. OSWorld 2.0's residential proxy, 3 s pauses, per-model output caps, simulated user.
Vending-Bench's fixed 69k-token trimming.

**H5 Recipe divergence.** Products demo hours-long computer use; OSWorld 2.0 (median human 1.6 h) shows 13–21%
binary at 318–482 tool calls, and METR's p80 horizon at the frontier is 1–3 hours. Open-weights lead Toolathlon
(78.4 vs 76.2) and top SWE-rebench pass@5 (GLM-5.2), while OpenHands Index says Claude is "a few months ahead".

**H6 Cost silence.** No cost on: SWE-bench Verified table, SWE-bench Pro, Terminal-Bench 2.0 leaderboard, BrowseComp
top 10, τ-bench, Toolathlon, Gaia2, MLE-bench, METR ($), OpenHands text. Cost shown on: SWE-rebench, HAL, OSWorld 2.0
paper, BFCL, Vending-Bench (chart only). HAL: 9x cost at 2-pt accuracy difference; "100x more expensive while only
1% better"; $40,000 and still single runs. Terminal-Bench paper: $1–$100 per run, 100M tokens on one task, dropped
from its leaderboard. hyper-τ-bench is the only benchmark where cost is a scored constraint.

**H7 Universal unmeasured assumptions.** One frozen user simulator (gpt-5.2) for all 27 τ³-Banking entries. Served
model is not fixed (weight swaps behind endpoints, FP4/FP8 routing, provider-specific reasoning-effort budgets — HAL).
Passing tests = solved task (HAL: gold answers found on HuggingFace/arXiv, hard-coded unit-test passes; hyper-τ:
cheating attempts 17–42% of runs). Public oracle solutions reachable by internet-enabled agents (Terminal-Bench,
"not observed"). Copyleft licence as contamination resistance (SWE-bench Pro).

**H8 Open questions in meta-papers (verbatim).** 2609.09218: "we find none that both reports seeded worst-case
reliability and treats the scaffolding level as a controlled variable." 2603.29231: "capability and reliability
rankings diverge substantially, with multi-rank inversions at long horizons"; "frontier models have the highest
meltdown rates (up to 19%)"; "memory scaffolds universally hurt long-horizon performance." 2602.07150: recommends
"statistical power analysis to determine the number of runs needed" — leaves open what k stabilizes the envelope.

**H9 Contradictions across sources.** Self-reported SWE-bench Verified 95–96% vs uniform-harness 75.6% on the same
aggregator page. Terminal-Bench paper "<65%" (Jan 2026) vs leaderboard 84.7% (May 2026). Terminal-Bench "no
correlation" between turns/tokens and success vs HAL positive token–accuracy correlation on 6 of 9 benchmarks vs
OSWorld 2.0 steeply rising token cost per point. HAL: more reasoning effort → equal or lower accuracy in 21 of 36.
BrowseComp FAQ "best 92.2%" vs listed 93.3%. 2609.09218: no-LLM rule-based baseline 96.8 within 0.7 of frontier on a
published leaderboard. 2512.10218: 3x/6x localization advantage on SWE-bench Verified vs fresh repos. τ³ audit fixed
50+ tasks after 20 months of published pass^k numbers.

## 3. Patterns seen across three or more benchmarks

1. **Headline ranks sit inside their own error bars.** SWE-bench Pro (top-2 gap 2.4 < CI ±3.1–3.6), Terminal-Bench
   2.0 (top-5 within 2.5 pts, ±2.1–2.8), Toolathlon (±1.9/±3.4 around a 2.2-pt open-vs-closed lead), SWE-bench
   Verified (2.2–6.0 pp single-run spread), BrowseComp (top-10 within 4 pts, all self-reported). No leaderboard
   marks statistical ties.
2. **The reliability metric exists but is not displayed where ranking happens.** τ-bench (pass^k framing, pass^1
   shown), Toolathlon (pass^3 missing for newest top rows), SWE-rebench (pass@5 but no pass^k), MLE-bench (SEM from
   ≥3 seeds padded with failures), HAL (single runs after $40k), METR (p80 published in YAML, p50 in headlines).
3. **Cost is reported in papers and dropped on leaderboards.** Terminal-Bench ($1–$100 per run in paper, none on
   board), OSWorld 2.0 ($72/task in paper, no leaderboard numbers), BrowseComp (cost only for search-API vendors),
   Vending-Bench (chart without numbers), SWE-bench Verified (plots not columns). Counter-examples: SWE-rebench, HAL,
   BFCL. Two leaderboards that do report cost disagree on what cost is (caching counted or not).
4. **Human ceilings are time estimates, not success rates, or are missing.** Terminal-Bench 2.0 (author-estimated
   time), OSWorld 2.0 (median 1.6 h, no success rate), METR (human times "likely overestimate"), SWE-bench Pro and
   Toolathlon and Vending-Bench (none). Where a human success figure existed (OSWorld-Verified 72.36%) agents passed
   it and the benchmark was replaced rather than re-baselined.
5. **Scaffold is an uncontrolled axis that moves scores by 10–25 points.** Terminal-Bench (max-over-scaffold; 5
   harnesses on 3 models at the top), τ-bench (4 native scaffolds shift reward up to 0.267), SWE-bench Verified
   (self-report vs mini-swe-agent ~20 pts), HAL (9x cost at 2 pts; task-specific beats generalist 11 of 12), Gaia2
   (vanilla 42.1 vs OpenClaw harness 57.0), 2609.09218 (no-LLM baseline 96.8).
6. **Long-horizon success collapses while partial credit and short-horizon scores stay high.** OSWorld 2.0 (binary → 0
   on longest tasks, partial 54.8%), METR (p80 4–10x shorter than p50; p50 above the suite's 16 h limit), Gaia2 (Time
   split 0.8–5.0%), 2603.29231 (meltdown up to 19% at long horizons), Vending-Bench (year-long sim ranked by money
   with undefined ±).
7. **Benchmarks are consumed in months and answered by version churn, not re-measurement.** Terminal-Bench 2.0 → 4.0
   within 11 months; OSWorld-Verified (2025-07-28) → OSWorld 2.0 (2026-06-26); τ² → τ³ with a 50+-task audit;
   MLE-bench closed at 64%; HAL paused; Gaia2 vanilla board frozen since 2025-09. Each reset discards the
   reliability and cost history that was never recorded.
8. **Validity faults found after money was spent, by log inspection rather than by the score.** HAL (τ-bench few-shot
   test leak found after $1,000; gold answers on HF/arXiv), hyper-τ (cheating attempts 17–42%), MLE-bench (label leaks
   kept), τ³ (50+ tasks fixed), HAL reliability (GAIA .xlsx failures; estimator bug), SWE-bench Verified (memorization
   probe 2512.10218).
