# On Terminal-Bench 3.0 to 4.0, with the model fixed and the harness pinned, the 19 repaired tasks carry more than half of the kept-task delta after the recalibration delta on the 47 untouched tasks is subtracted (DiD repair share > 0.5, task-cluster bootstrap), and the model ordering on the 19 repaired tasks departs from the ordering on the 47 untouched tasks beyond a difficulty-matched random-subset ceiling.

`CL-W44-02` · lane **L1** · status **refuted** · rank None · position solo · refreshed 2026-11-02

## Status

A probe came out against the claim. Failing gate: Gate 1 data gate open (per-trial 3.0 results); Gate 5 one benchmark. Grade on paper: open pending kill search; two zero-dollar probes, one scorecarded; consumer breadth one community unless labs move. Next action: see First steps.

## The claim

- **Headline:** On Terminal-Bench 3.0 to 4.0, with the model fixed and the harness pinned, the 19 repaired tasks carry more than half of the kept-task delta after the recalibration delta on the 47 untouched tasks is subtracted (DiD repair share > 0.5, task-cluster bootstrap), and the model ordering on the 19 repaired tasks departs from the ordering on the 47 untouched tasks beyond a difficulty-matched random-subset ceiling.
- **Current belief (the field's):** Terminal-Bench 4.0 release note (B04, 2026-08-28): 'All tasks in TB 4.0 are now set to a flat agent timeout of 8 hours [...] We removed 8 tasks [...] We fixed 19 tasks [...] These represent breaking changes that require re-running trials' — the changes are listed, not scored; SWE-Bench Pro V2 (B07, 2026-10-16): 'repaired or retired 480 of the 731 tasks: 23 contracted engineers spent 404 hours [...] 69 tasks had instructions that contradicted the tests grading them', with the board at '99.4 +/- 0.4' three weeks after relaunch (B08); Cognition FrontierCode 2.0 (L18, 2026-10-27): 'In 80% of FrontierCode 2.0 tasks, the reference solution differs from the upstream PR, up from 60% in FrontierCode 1.0', six of eight models reordered; Gemini 4 Argon model card (L12): 'computed with improved evaluations and thus are not directly comparable'; Vals (B12): 'Because the task set is entirely different, scores are not comparable across versions' — the owners say 'not comparable' with no number, and launch tables read the version delta as model progress
- **If true:** Every continuous benchmark publishes a repair delta per release and the ordering on the unchanged subset; labs report old-version and new-version scores as separate columns; aggregators stop drawing trend lines across refreshes; a version refresh is labelled equatable, linkable or new construct
- **If false:** The delta is uniform across repaired and untouched tasks and the link is population-invariant: the versions measure the same thing, churn costs only history, and the output is a link table (a service) plus the withdrawal of the churn premise

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Asked in print: the Terminal-Bench team's position post (B05) proposes semantic versioning 'with no number for how large the broken fraction is'; tau-bench's maintainers write 'results produced with tau2-bench < 1.0.1 are not comparable with >= 1.0.1' with no number (import S5xF2); Vals and Argon declare non-comparability (B12, L12). Who pays: benchmark owners refreshing versions (Terminal-Bench, Scale, Cognition, Sierra, Nebius), labs whose cited numbers sit on retired versions, aggregators plotting trends.
- **Impact ceiling:** **floor**: A repair-share table for two version pairs and a link table with the population-invariance verdict; cited when a refresh is announced. Requires the two $0 probes. p = 0.55 (judgment).; **middle**: Repair share above one half on at least one pair with the ordering preserved on untouched tasks, or non-invariance by scaffold family beyond 2x the floor: one benchmark owner ships the repair delta and verdict label per release. Requires an owner willing to ship the table. p = 0.3 (judgment).; **ceiling**: Repair delta and untouched-subset ordering become the reporting rule for continuous benchmarks and launch tables carry two columns per refresh. Requires the middle result on two owners plus a lab adopting the columns. p = 0.1 (judgment).
- **Relevance:** L1 direct (benchmark validity and churn; the tau-family boards are among the stalled trackers). Narasimhan route: tau-bench version pairs are one of the three. HAL route: paused tracker, the obvious host. Industry: labs' launch tables. Jacob's edge: the linear links and variance ratios are hand-checkable statistics; no numerics or GPU content. zero_where: L2, L3, L5; the systems route.
- **Kill probe:** import S5xF2 ($0, 11 d; dead if REMSD < 1.5x floor under both groupings on every qualifying pair) and P-W44-02-repair ($0, 14 d; dead if the repair share is under one half on both public pairs).
- **Density and ownership:** P2a = 1, P2b = 7 in the 12-month window, none decomposes a version delta; equating and population invariance for agent benchmarks in no fetched source; the two closest (2607.26191; B05) pose adjacent questions and stop; incumbents list, re-run or aggregate, none decomposes; the owners are the race.
- **Why now:** Public paired per-task files for both versions of FrontierCode (2026-10-27) and Terminal-Bench 4.0's 330-trial payload (2026-10-23) make the decomposition a desk job for the first time; three trackers stopped in 2026, so the question of what a version delta measures has no incumbent answer.
- **Register, and what it is not:** Measurement (a version-delta decomposition and an equating verdict) with a reporting-rule consequence. It is not a new benchmark, not a contamination study, not a horizon refit.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | pass: every premise number is fetched, dated and carries its denominator (B04 8 removed, 19 fixed; B07 480 of 731; B08 99.4 +/- 0.4 on 642 tasks; L18 80% vs 60%); the quantity is defined on paired per-task outcomes for the same model-harness-effort entry, random given fixed harness and effort with one run per cell on the boards, so the split-half floor of one version (import S5xF2) is the null and CL-W43-14's single-run spread enters as that floor; plain trick: score the changelog, then re-rank on what did not change |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: import S5xF2 is $0 with a scorecard and a pre-registered kill; P-W44-02-repair is $0 and two weeks; both outcomes informative (a link table and the withdrawal of the churn premise is the footnote result) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: leaderboard (B04, B08, B12), blog (B05), benchmark paper (B07, L18), model card (L12), tech-report (B16) — five source types, ten records; the pressure report ranks this strain second of twelve |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass at one community with a community-wide reach if labs change launch tables: benchmark owners (repair delta per release; verdict label), evaluators (Vals, Artificial Analysis: two columns), aggregators (no cross-refresh trend), harness builders (a scaffold-dependent link means the refresh changed what harness features are worth); the pressure report's objection is that the owners already write 'not comparable', so the must-change population is the evaluators unless the number moves labs |
| G4 | mechanism and consequence | pass: mechanism — a version bump moves the mean through four separable per-task channels (resource headroom, timeout removal, task removal, verifier fixes), each an indicator on a paired matrix, so the delta decomposes exactly; consequence — a published repair delta and an untouched-subset ordering per release if the share is large, churn costs only history if it is uniform |
| G5 | durability; lab-adjacent | pass as a protocol (every refresh of every continuous benchmark); the specific pairs are consumed; not head-to-head with any lab |
| G6 | ownership, density, race window; position clause | survived concept-level kill search (weak: one version pair of one benchmark whose owner holds the data; closest ABA 2605.26079 re-grades, never re-runs); race window 0.35/week adjacent vs 3 weeks to result |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W44-02-repair | For each version pair $(v, v')$ and each model-harness-effort entry run on both, pair per-task outcomes and write the d… | Pre-registered: dead if the repair share is under one half on both public pairs (TB 3.0 to 4.0; FrontierCode 1.1 to 2.0) with a task-cluster bootstrap interval excluding 0.5; the ordering clause is dead if the untouched-subset Spearman is… | thought | not run (no candidate record yet) |

Also under this claim (no scorecard yet): import:2026-W44-S5xF2 (population invariance of the old-to-new score link by scaffold and model family on Terminal-Bench 2.x to 4, tau-bench 1.0.0 to 1.0.1, SW…

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

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

- 2026-11-01 — claim open: pressure red team (point #2): candidate-worthy, narrowed to proper — 1 killing objection (the $0 probe was unfunded: Harbor Hub registers one leaderboard, the tbench.ai 3.0 URL serves the 4.0 payload with aggregate-only rows, SWE-Pro V1 has no per-task grades, FrontierCode 2.0 is a new task set with rho = 0.83) conceded and re-costed; headline narrowed to Terminal-Bench 3.0 -> 4.0 under one pinne…
- 2026-11-01 — claim open: concept-level kill search (data/reports/2026-W44-kill-CL-W44-02.md): survived-kill (weak) — No neighbour occupies the shipped-version-pair decomposition or the repaired-versus-untouched ordering test; the filter-level mechanism is occupied in the same benchmark family (ABA 2605.26079 on TB2/Verified with the maintainers' PR as ground truth; text-to-SQL 2601.08778; UTBoost) and the field's stated…
- 2026-11-01 — claim refuted: design red team of C-W44-19 ran step 0/1 on the Hub payloads: the ordering clause is refuted on the shipped 4.0 board (rho_RU = 0.902 >= matched ceiling 0.839) and the headline is a conjunction; the first clause (repair share) is unresolved on the free record (in-band DiD +0.109 to +0.133, intervals above zero) and moves to CL-W44-11 as a thought; import S5xF2 (ordering clause across version pair…
- 2026-11-02 — claim open: written top-down by the W44 claims run from pressure #2 (B04, B07, B08, L18, L12, B12, B16 quoted); import S5xF2 attached as the ordering-clause probe (scorecarded, $0); P-W44-02-repair written as the first-clause probe ($0); L1 open claims before this run: 4 (CL-W43-03, 04, 10, 14); this is the first of two new L1 claims this week; concept-level kill search owed (must quote 2607.26191 and the Te…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-02`, version 4)
- `P-W44-02-repair`: seed or import record (no candidate yet)
