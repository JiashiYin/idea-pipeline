# Standards — what counts as a golden idea, a proper idea, a parked item, or a thought

The second law, beside `config/themes.yaml`. Jacob edits this file; the machine applies it. Every stage that
grades an idea (kill search, red team, report, pressure synthesis) grades against these gates, in this order,
and says which gate failed. The bar is all-or-nothing by Jacob's choice (2026-10-16): most weeks produce zero
golden ideas, and the pipeline's output on those weeks is the kill record and the parked list.

Version: 2026-10-16. Owner: Jacob Yin.

## Definitions

- **Golden idea** — passes every gate below, including the position clause. Rare by design.
- **Proper idea** — passes Gate 0, Gate 1, Gate 2 (either route), Gate 4 and Gate 6; may fail Gate 3's
  community-wide breadth (one community is enough), Gate 5's durability, or have a short race window. Worth a
  semester inside the right room; not a signature.
- **Parked item** — fails one gate for a reason that can change (position, a release, an unanswered question
  to a specific person). Carries a written re-open trigger and the cost on re-open. The parked list is an
  asset; items are re-checked when their trigger fires, never on a schedule.
- **Thought** — fails Gate 0 or has no kill probe. Not recorded as a candidate.

Nothing is called golden, proper or even a candidate before: a 12-month kill search with mechanism AND role
words; the two closest papers' own limitation text quoted; an independent red team with fetched evidence
(`prompts/checklist.md`). A proposal in chat before those is a thought.

## Gate 0 — Premise hygiene (hard; a thought until it passes)

- Every premise number is fetched, carries the source's category name and denominator, and is dated.
- Every defined quantity has its conditioning set written down: random *given what*. If the environment is
  deterministic after the action, there is no luck term. (The 2026-10-08 error.)
- The quantity is a property of the thing, not of the protocol: name whose sampling temperature it depends
  on; a party at temperature 0 has zero decision variance by construction; a seed is not a state of the world.
  (τ-bench 2026-10-14; ACE/RBC 2026-10-16.)
- Judge and critic, verifier and judge, are different objects; the premise says which one it means.
- One-sentence plain trick exists, mechanism only, sayable in a talk. If it cannot be said, it is not clear yet.

## Gate 1 — Cheap to kill (hard)

- A probe exists costing at most one week and one GPU-week (or the dollar equivalent), whose result would kill
  the idea.
- The kill result is written before the probe runs: "if we observe X, dead." Pre-registration is what stops
  coherence from being mistaken for confirmation.
- Both outcomes are informative: the kill result is at least a footnote someone would cite. A probe whose
  negative outcome teaches nothing is not a probe.
- No probe under a GPU-week → parked, not reported (`CLAUDE.md`, kill search).

## Gate 2 — Pressure, by one of two routes (hard)

**Route A — a stated pressure point.** The idea addresses a strain visible in at least two independent source
types (lab disclosures, benchmarks and leaderboards, meta-papers, engineering blogs, issue trackers), quoted in
their own words (stage 6b records).

**Route B — the ruler route.** The idea makes a fuzzy, widely used notion measurable (reliability, effort, cost,
autonomy, skill versus luck, memory quality) with a definition that is (i) identifiable under the stated
protocol, (ii) computable from data someone named actually has, and (iii) carries a **pre-registered
surprise**: write three results side by side — the result we expect, the result the field assumes, the result
that would change a belief or a ruler. If our expected result equals the field's assumption, the ruler is a
service, not a paper (τ-bench per-turn split: expected "mostly the agent" = the owners' assumption → parked).

## Gate 3 — Consumers and adoption surface (graded; golden needs community-wide)

- Name at least three distinct consumer classes (training teams, benchmark owners, harness builders,
  evaluators, theorists, product teams) and, for each, the **specific action they would change** if the result
  holds: a metric they report, a recipe step, a default, a column on a leaderboard.
- Count the must-change population. **Golden:** a whole community must change something (every compaction paper
  reports X; every leaderboard adds Y; the default recipe changes). **Proper:** one community.
- Register test, symmetric: a method must change someone's training run; a measurement must change a belief or
  a ruler; a systems result must change a deployed stack. "Interesting" is not a consumer.

## Gate 4 — Mechanism and consequence (hard)

- A headline number alone is a survey. The idea states the mechanism (why the number comes out as it does) and
  the consequence (the action that follows each way the result can come out). Example shape: signal versus
  headroom → which recipe to use. Both sentences are written before the first run.

## Gate 5 — Durability (graded; golden needs it)

- Survives the next model generation and the next benchmark refresh. A ruler that applies to any agent is
  durable; a static test set is consumed in months (pressure point #1); a result that depends on one model's
  quirk is not.
- Not head-to-head with a frontier post-training or infrastructure team's core problem: labs will have it in
  production before the paper is reviewed. Lab-adjacent is the target (measurement of labs, cross-lab
  comparison, standards, benchmark validity, definitive controlled comparisons).

## Gate 6 — Ownership, density and timing (hard, position-relative)

- Density: 12-month arXiv API count with mechanism words AND the field's role words (for memory steps:
  curator, reflector, write-time, read-time, gate; for forks: snapshot, branch, sibling, prefix, replay), plus
  at least two pre-window precedents named with their tricks. A research-tool landscape is a harvest, not a
  kill search.
- Incumbents: shipped artifacts count (a leaderboard column is a shipped effort curve). The two closest papers'
  limitation sections are quoted; "they have the stack" is a guess, and the re-open test is asking them.
- Why now: the enabling piece and its date. "No reason" is a flag.
- **Race window:** estimate the lane's publication rate (papers per week in the window) and the time to our
  first result; golden needs window ≥ 2× time-to-result. Three papers a week with a two-week pilot is a coin
  flip, not a plan.
- **Position clause.** Density is relative to position. State the position assumed: *solo* (free public data,
  hundreds of GPU-hours, no artifact) or *lab* (an owned artifact, compute, logs, standing). From the solo
  position, density means a race we cannot win: kill. From a lab position, density with no definitive version
  means a race we can enter: the compute-matched comparison nobody ran (mutation #5) or the owner's measurement
  on the owned artifact. The same idea can be parked solo and golden in a room; the record says which.

## Scorecard (required on every proposal, `CLAUDE.md` rule 9)

Target value (who asked in print, who pays) · impact ceiling as floor / middle / ceiling with what each
requires and a stated rough probability · relevance to each route and to Jacob's edge, including where it is
zero · kill probe with cost, criterion and time · density and ownership with the quotes · why now · register and
what it is not. Probabilities are labelled as judgment.

## Weekly expectation

A week with zero golden ideas is a normal week. The pipeline's score for the week is: kills with fetched
evidence (count, hours each), parked items with written triggers, checklist lessons added, and whether the
watch caught every paper in our lanes before a human colleague mentioned it. A golden idea that passes all
gates goes to a report (`schemas/report.md`) and to the three decisions only Jacob can make.
