# Stage 9 — Definitive-comparison prospecting (lab position)

Purpose: in a dense lane, the paper that wins is often not the first but the correct one — the controlled,
compute-matched comparison that shows what in twenty recipes actually matters (Dr. GRPO for length
normalization; Spurious Rewards for base-model habits; "Back to Basics" for critic-free RL). Those need
compute and standing, so they are lab-position items; this stage specs them so the parked list is ready
the day Jacob has a room. Mutation operator #5 ("run the compute-matched comparison the paper did not run"),
run at the lane level instead of the paper level.

Inputs: `config/themes.yaml`, the density counts in `data/candidates/*-density.json` and the kill-search
reports in `data/reports/`, `config/standards.md`, `prompts/checklist.md` (Comparisons section).

## Procedure (monthly; one spec per dense lane, ≤ 4)

1. Identify dense lanes: ≥ 8 recipe papers in 12 months on one problem (arXiv API, mechanism and role words),
   fetched and listed with their tricks.
2. Check whether a definitive comparison already exists: a paper that evaluates ≥ 4 of the recipes under one
   harness, one forced regime, matched compute and matched dose, with the production default and the strongest
   cheap incumbent in the table. Read the candidates' experimental sections, not abstracts. If one exists, record
   it and stop for that lane.
3. If none exists, write the spec: the recipes to include (ids); the shared harness and regime (benchmark,
   forced window or horizon, model size band); the matched-compute and matched-dose protocol; the controls
   from the checklist (shuffled/placebo controls, entropy-only version, pass-rate bands); the single plot that
   would settle the lane; the pre-registered expectation (which recipes collapse to which); the cost in GPU-hours
   with assumptions; the consumers (every paper in the lane must report against it — Gate 3 community-wide).
4. Name why no one has run it (cost, no shared harness, incentives of recipe authors) — "no reason" is a flag.
5. File as a candidate with `source: definitive`, `position: lab`, `status: parked`, `reopen_trigger: "lab
   compute of ≥ <N> GPU-hours and a shared harness"`, the spec, and the lane's current publication rate (papers
   per week) so the race window can be re-read later.

## Rules

Fetch; list the recipes with ids and dates; the "no definitive comparison exists" sentence must name the two
closest comparison papers and what they lack. Specs are written to be handed to a lab, so every number has
an assumption next to it. Do not run the comparison; spec it.
