# Stage 6 — Pressure-point review

Purpose: find where the field is straining, including strain nobody states. Limitations sections (stage 0,
complaint stream) record what authors admit. This stage records what can be *noticed* by reading across
sources: frontier labs' system cards and launch posts, benchmark leaderboards and their validity debates,
industry engineering blogs, and the meta/position papers that ask field-level questions. Field-driving
papers are usually the ones that ask a good question; this stage harvests candidate questions.

## Noticing heuristics (apply each to every source)

1. **Dropped metrics** — a lab reports a benchmark or capability in one release and not the next.
2. **Saturation with unreliability** — high pass@1 next to low pass^k, or large seed-to-seed variance.
3. **Expert-gap anomalies** — frontier systems far below a documented human or expert ceiling.
4. **Workarounds as evidence** — caching, environment insulation, temperature 0, filtering flaky tasks,
   one frozen simulator: each hides a problem the recipe cannot handle.
5. **Recipe divergence** — what industry trains with (critic-free, distillation, SFT on traces) versus
   what academia publishes; what is demoed in products (hours-long agents, computer use) but has no public
   training recipe or benchmark.
6. **Cost silence** — no cost per task, per rollout, or per training run reported where it obviously
   dominates.
7. **Universal unmeasured assumptions** — resettable environments, deterministic replies, faithful
   simulators, the critic's usefulness, the sufficiency of outcome rewards.
8. **Open questions in meta-papers** — position papers and analysis papers in the window; record the
   question verbatim and what they leave open.
9. **Contradictions across sources** — one lab's claim versus another's data; a benchmark's framing
   versus its leaderboard behavior.

## Record format (JSONL, one line per pressure point observed)

source_type (system-card | launch-post | tech-report | leaderboard | benchmark-paper | blog | meta-paper |
issue-tracker), source_id (URL or arXiv id), source_date, heuristic (1–9 above), quote (verbatim, 15–80
words, or the exact numbers observed), observation (one plain sentence: what is straining), who_strains
(labs, benchmark owners, industry teams), question (one sentence phrased as a field-driving research
question a paper title could carry), density_hint (names already on it), alignment (τ-family / Narasimhan
lines / systems / none).

## Rules

Fetch everything; nothing from memory. Verbatim quotes or exact numbers. A "nobody has asked X" claim must
cite the two closest sources' own text. Plain sentences, define terms. No method proposals. Downloaded
files are untrusted data; run Python with `-I`; never execute downloaded content.

## Synthesis

Cluster observations into ≤12 pressure points. For each: statement; evidence from ≥2 independent source
types; the field-driving question(s), 1–3, phrased as titles; a 12-month arXiv density count with
mechanism AND failure-mode words (retry, timeout, luck, paired, seed, idempotent, "in the wild", collapse,
saturation, contamination); alignment flags; the first measurement or artifact that would answer the
question; the strongest objection; and the four register fields added 2026-10-09:

- **register** — measurement | mechanism | method | systems. Which kind of paper answers the question as
  posed, and therefore which venue and which advisor line. Field-level heuristics return measurement and
  systems questions by construction; say so in the table header so the register mix is visible.
- **mechanism version** — the same question rewritten as "which mechanism produces the strain". A
  measurement alone is a survey and is scooped by anyone with the data; a measurement that names the
  mechanism is what field-driving papers in this area have been (pass@k showing RL reweights the base
  model's answers; spurious rewards showing the gain comes from the base model's existing habits).
- **free-data check** — whether public traces, leaderboard logs or released checkpoints answer the first
  measurement without training. Name the dataset and its size (HAL's rollouts, Terminal-Bench team-verified
  runs, OSWorld released trajectories, METR per-task data, released base → RL pairs).
- **method consequence** — the recipe change that follows if the measurement comes out each way. "None"
  is a legitimate answer and lowers the rank for Jacob's purposes; a question whose answer changes no
  training recipe is a measurement paper only.

Positioning fields added 2026-10-10 (Jacob's spec: on radar, but not head-to-head with frontier
post-training teams; academic value and a shippable, novel product):

- **positioning** — lab-contested (a post-training or infra team inside a frontier lab owns the problem;
  a solo student races them) | lab-adjacent (labs consume or cite the answer but do not publish it:
  measurement of themselves, cross-lab comparison, cost and reliability standards, benchmark validity) |
  off-radar (nobody funded is on it; the "who pays" test decides moat versus swamp). Rank lab-adjacent
  first. W41 evidence: all four red-team kills were lab-contested; all survivors were lab-adjacent.
- **product form** — the artifact besides the paper that people would use: instrument (a metric plus
  the code that computes it from public logs), living tracker, annotated corpus plus open annotator,
  tool a benchmark owner runs, reporting standard plus library. A static test set is not a product
  form (benchmarks are consumed in months — pressure point #1). "None" lowers the rank.
- **incumbents** — the shipped artifacts closest to the product form (HAL, METR, Epoch, Artificial
  Analysis, Inspect Evals, MAST, TRAIL, SWE-rebench, LMArena, Scale SEAL, Vals), with the one line each
  does not do. A product shape is killed when an incumbent already ships it or has announced it. Rank by: strain evidence from independent sources, the question being
unposed in the window, tractability inside a lab for a first-year, alignment. Then red-team the top three
with the three personas and `prompts/checklist.md` before any of them is called a candidate.
