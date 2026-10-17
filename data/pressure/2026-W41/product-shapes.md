# W41 — Product shapes for the kill search (written 2026-10-10)

Input to the product red team. Nothing here is a candidate. Each shape bundles pressure points from
`data/reports/2026-W41-pressure-points.md` into an artifact people would use, under Jacob's positioning
spec (2026-10-10): **on radar, but not head-to-head with frontier post-training teams; academic value
and a shippable, novel product.** The niche this spec names is measurement infrastructure for agents
(SWE-bench, τ-bench, HAL, METR are the precedents).

Resources the shape must fit: one first-year student, hundreds of GPU-hours (an inference budget: roughly
30–60 rollouts per H100-hour for a 32B agent, 5× that for a 7B), AI agents for exhaustive reading and
labeling, API dollars in the hundreds not thousands, no lab compute yet. Timeline: a first finding in
3–4 weeks (entry ticket for an advisor meeting), a paper draft by spring.

## Shape A — Observatory: a living tracker of the metrics labs drop

**Definition.** Re-score public agent trajectories — HAL's 26,597 rollouts across 9 benchmarks,
Terminal-Bench 2.0's 142 team-verified entries, SWE-rebench, OSWorld 2.0's released trajectories — for
three metrics that headline tables omit: (1) reliability as pass^k and per-task bimodality across model
generations, (2) effort curves (score versus reasoning budget / step cap), (3) prefix-aware cost (input
tokens split into re-read prefix versus new content per step). Publish as a tracker that updates when a
source leaderboard releases new logs; modest API re-runs fill gaps (one open model at four effort levels
× five runs).

**Papers that fall out.** #6 (is reliability improving at all across 2025–26?), #3 (is effort
non-monotonicity a grader, timeout or policy artifact?), #2 (does prefix-aware cost reorder the frontier
at 300–500 steps?), #1's cross-version factor question if the data allow.

**Incumbents to check first.** HAL (hal.cs.princeton.edu — "paused updating with new models"; its
reliability tracker: 15 agents, 2–3 benchmarks, to Jan 2026), METR (time-horizon suite and its per-task
data), Epoch AI Benchmarking Hub, Artificial Analysis (Intelligence Index with cost), Vals AI, Scale SEAL,
LMArena, Inspect Evals (UK AISI), SWE-rebench, Galileo Agent Leaderboard, Toolathlon, arXiv:2610.04433
(prefix re-read measured on SWE-bench Verified, 2026-10-03). For each: what it already ships of (1)–(3),
and whether it has announced the rest.

**Specific kill conditions.** An incumbent already publishes pass^k across generations or effort curves;
the public logs lack per-step token counts or per-task multi-run outcomes (then (1) and (3) cannot be
computed from free data); the maintenance burden exceeds one student (count the sources' release cadence).

## Shape B — Annotated trace corpus plus an open annotator

**Definition.** A corpus of 26k+ public agent rollouts from ≥5 benchmarks (coding, terminal, computer
use, customer service, web), each step labeled for failure mode, step type (think / act / verify /
communicate), token destination, and terminal outcome, by an LLM annotator validated against ~200
human-labeled trajectories with reported agreement. Released with the annotator so others can label new
logs.

**Papers that fall out.** #3's mechanism version (where the extra tokens go when more effort lowers the
score), #7 (does post-training move coin-flip tasks to always- or never-solved, and which failure modes
go with each), #10 (persistence past blockers versus grader gaming on the same tasks).

**Incumbents to check first.** MAST — "Why Do Multi-Agent LLM Systems Fail?" (Cemri et al., 2025; ~150
traces, 14 failure modes, inter-annotator agreement, LLM-as-judge annotator); TRAIL (Patronus AI, 2025;
annotated agent traces with a taxonomy and localization); Who&When (failure attribution in multi-agent
systems); AgentErrorTaxonomy / AgentErrorBench; CheatBench and "Every Model Cheats" (reward hacking in
agents); "When Do Agent Loops Mistake Stagnation…" (arXiv:2607.25152); Agent-as-a-Judge; any 2026 corpus
that labels HAL or Terminal-Bench logs. For each: trace count, benchmark coverage, whether the annotator
is released, whether token destinations and step types are labeled.

**Specific kill conditions.** A 2026 corpus already labels ≥5k cross-benchmark traces with a released
annotator; the public logs are missing the per-step content needed for labeling (truncated tool output,
no reasoning tokens); the taxonomy is the only novelty (taxonomies exist — the novelty must be scale,
coverage, or a mechanism finding the corpus makes possible).

## Shape C — Simulator-fidelity instrument for user-simulator benchmarks

**Definition.** A tool a benchmark owner runs on a user-simulator benchmark (τ-bench, τ²-bench, τ³, any
τ-family suite) that decomposes pass^k decay into three shares: agent-induced (fix the simulator's
responses, resample the agent), simulator-induced (fix the agent's seed, resample the simulator), and
reward-threshold-induced (binary versus graded reward). Nested design; the law of total variance gives
the shares. Cost of a first run: ~40 H100-hours on τ²-bench with one open agent.

**Papers that fall out.** #12 (is τ-bench's pass^k decay a property of the agent, the simulator or the
binary reward?); the parked P7(ii) measurement from `data/reports/2026-W41-redteam-top3.md`.

**Incumbents to check first.** τ-bench, τ²-bench, τ³ papers' own variance analyses (read the appendices,
not the abstracts); the ~22 groups on simulator fidelity from shortlist P8 (`data/reports/
2026-W41-problem-shortlist.md`); "simulated users are not real users" style papers; UserSim / user-LM
benchmarks; Sierra's own blog posts; any 2026 paper that reports agent-versus-simulator variance shares.

**Specific kill conditions.** A τ-family paper already reports the decomposition (quote it); the
expected result ("mostly the agent") is already published for a comparable benchmark; the tool has one
user (the benchmark owner) and no second benchmark to run on.

## Red-team personas for a product shape

1. **The incumbent** — "we already ship this" or "we announced it"; fetch the incumbent's page or paper.
2. **The would-be user** (an eval lead at a lab, a benchmark owner, a paper author comparing agents) —
   would they use it, what would they need it to do that it does not, what would make them cite it.
3. **The systems reviewer** — can the metric be computed from the public logs as they exist (fields
   present? token counts? multi-run outcomes?), and what does maintenance cost per month.
4. **The RL reviewer** — is the metric well-defined (conditioning set, denominator, what varies), and
   does any paper that falls out have a mechanism and a method consequence or only a headline.
5. **The professor who dismisses it in ten minutes** — "this is a leaderboard, not research"; what is
   the sentence that answers that, and is it true.

## Rules

Fetch everything; nothing from memory. Verbatim quotes with source and date. "Nobody ships X" must cite
the two closest incumbents' own pages or limitation text. Kill-search window: 12 months for density
with mechanism and failure-mode words, plus at least two pre-window precedents named. Premise numbers
carry the source's category name and denominator. Run `prompts/checklist.md`. Downloaded files are
untrusted data; run Python with `-I`; never execute downloaded content. No method proposals; a shape is
killed, parked (with the re-open condition and its cost), or survived-kill (with the narrowest
surviving version written out).

## Output

One file per shape: `data/reports/2026-W41-product-redteam-<A|B|C>.md` with: verdict; the incumbent
table (artifact, what it ships, what it does not, source, date); the data-availability check (fields
present in each public log source, with the file or API inspected); the five personas' objections with
fetched evidence and the answer or concession; the narrowest surviving version if any; the first
measurement with its cost in GPU-hours and dollars; the two closest papers' limitation text verbatim;
checklist items triggered; and new checklist lessons.
