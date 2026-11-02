# Owned-artifact portfolio — Ravi Netravali / Tri Dao (Gambit and the Princeton rollout / serving stack)

Entry-ticket questions for the advisor conversation. Each question is owner-only because of a named data field or
configuration; "not published" is the strongest statement made about the owner. Stage 8, monthly.

## 2026-W44

**Artifact state (fetched 2026-11-02).** Gambit, "Thought-Level Beam Search for Reasoning" (2608.08020 v2, 2026-08-11;
COLM 2026; Yang, Luo, Zhao, Dao, Netravali). Code: `Dao-AILab/Gambit`, a vLLM v0.11.1 fork ("Compiling vLLM can take a long
time (sometimes several hours)"). Mechanism: capacity $C = 256$ active traces; after a warm-up $w = 12{,}000$ tokens,
every $\Delta = 200$ tokens a tournament prunes the bottom-$K$ and branches the top-$K$ ($K = 16$) by a 2-layer MLP
hidden-state scorer firing at `"\n\n"` boundaries; hard floor $\delta = 0.1$; score-weighted majority vote
$a^\ast = \arg\max_a \sum_{i: a_i = a} \bar s_i$. Logged structures: `TraceTree` (parent/child, score histories,
completion status), `SchedulingPolicy.GAMBIT` (prunes when the KV cache nears saturation), ghost traces (evicted but
logically active — "Scheduler View" versus "Tree View"). Hardware: "a single 275 GB NVIDIA B300 GPU". Results: up to
+6.7 points on HMMT-24 over pruning baselines, > 2xtrace-completion throughput, up to 68.5% fewer tokens than parallel
sampling; latency decomposition 99.03% GPU compute, 0.97% overhead; Phi-4 median unique tokens 5.2K (Gambit) versus
14.5K (SC) and 7.7K (STEP). Ablation (Fig. 10): "performance varies smoothly" over $K \in \{4,8,16,32\}$,
$\Delta \in \{100,200,400\}$, $w \in \{8K,12K,16K\}$; "infrequent updates ($\Delta = 400$) delay corrective selection".
No limitations section; the paper's own open sentences: "naively over-committing to a single prefix easily leads to
confident but incorrect trajectories"; A.2 "STEP is fundamentally bottlenecked by its inability to actively replenish the
trace pool." Related Princeton stack from the owners' arXiv listing: Slipstream (2605.08580, compaction validation),
Aragog (2511.20975, routing for agentic workflows), SAW-INT4 (2604.19157, KV-cache quantization).

**Q1 (strongest; candidate C-W44-OWN-3; orphan, L3).** *Is the tournament decided at warm-up? Rank persistence and the
one-shot control.* Owner-only: the `TraceTree` score histories of the published runs, the eviction log, the per-model
scorers, the B300. First measurement: Spearman $\rho_1$ between first-check and last-check scores per problem and the share
$\sigma$ of final traces whose lineage was top-half at the first check — zero GPU-hours, one day; then the control the
paper lacks: one swap of size $C/2$ at $w$, no further tournaments, same capacity, scorer, vote; three models xAIME-25 and
HMMT-24, three seeds about 65 B300-hours. Surprise — ours: $\rho_1 \ge 0.7$ and one-shot within 1 point on at least 4 of 6 cells;
theirs: "dynamically concentrates compute"; belief-changing: a one-shot fork at $w$ (an existing prefix-fork API) replaces
the tournament scheduler, or the persistence curve's decay sets $\Delta$ and the history-aware scorer (A.1) is the live
direction. Adoption: Gambit defaults, STEP/DeepConf successors, vLLM and SGLang parallel-thinking paths. Density: 0
strict; nearest MARS 2606.12935 (switch probabilities for stopping), 2609.38829 (vote correlation caps effective sample
size), Adapter Thickets 2610.00991 (Narasimhan: "A vote can only overturn mistakes that its voters do not share"). Not
published by the owner.

**Q2 (CL-W43-12).** *Ghost traces on 80 GB:* ghost share of the logical pool over the run on an H100 at $C = 256$, and
accuracy against STEP; about 10 H100-hours per model. Surprise: > 30% ghost after 20k tokens on the 8B model and accuracy at
STEP's level — the gain is conditional on KV bytes per trace.

**Q3 (orphan; campus bridge).** *Effective number of independent votes:* $n_{\mathrm{eff}} = N/(1 + (N-1)\bar r)$ from
sibling answer agreement in the logged trees, and a matched-lineage SC control; zero GPU-hours for the statistic, about 20
GPU-hours for the control. Surprise: $n_{\mathrm{eff}} \le 40$ of 256 and matched lineages close half the margin.

**Q4 (orphan).** *Prefix recomputation after eviction:* computed prefill tokens versus reported "unique tokens" when a
branched-from parent was a ghost; two counters, about 10 GPU-hours. Surprise: computed exceeds unique by at least 20% on the 8B model
under memory pressure.

**Entry ticket (Q1).** Your trace trees can answer whether the tournament is decided at warm-up: if the traces that win
the final vote were already top-ranked at the first check, one swap at $w$ does the whole job. The obvious design, ablate
$\Delta$, fails because a longer interval changes utilization and selection together, which is why Fig. 10 reads as
smooth. The identifiable design is the rank-persistence curve from your logs (zero GPU-hours) and a one-shot control — a
single swap of size $C/2$ at warm-up with the same capacity, scorer and vote — three seeds on three models xtwo benchmarks
(about 65 B300-hours). Pre-registered: we expect persistence above 0.7 and the one-shot arm within a point; your paper
reads the gain as dynamic reallocation. Do you want it, and is anyone doing it?

Solo entry point before asking: Gambit at $C = 32$ on Qwen3-4B on one 80 GB GPU with logging on, the persistence curve at
small scale (about 20 GPU-hours plus the fork build). Records: `C-W44-OWN-3`.
