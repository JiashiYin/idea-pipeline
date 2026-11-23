# A user simulator's error enters an agent leaderboard as two separable terms, an impact shift every agent receives and an agent-by-simulator interaction, and on the tau2-bench voice board the interaction alone moves the five agents run under both the gpt-4.1 and the gpt-5.5 user simulator by -10 to +16 points around a +7 mean and reorders them (Kendall $\tau$ 0.20-0.60) while the fidelity indices of 2611.24892 measure only the shift.

`CL-W47-02` · lane **L1** · status **killed** · rank — · position solo · refreshed 2026-11-22

## Status

Killed — see the kill section. Failing gate: G2B (surprise equals the stated knowledge of the two nearest communities); G4 and G6 fail behind it. Grade on paper: killed at the concept-level kill search. Next action: see First steps.

## The claim

- **Headline:** A user simulator's error enters an agent leaderboard as two separable terms, an impact shift every agent receives and an agent-by-simulator interaction, and on the tau2-bench voice board the interaction alone moves the five agents run under both the gpt-4.1 and the gpt-5.5 user simulator by -10 to +16 points around a +7 mean and reorders them (Kendall $\tau$ 0.20-0.60) while the fidelity indices of 2611.24892 measure only the shift.
- **Current belief (the field's):** 2611.24892 (card, full text) grades simulators by a geometric mean of utility, fidelity and detectability levels and reads Table 4 as a result ('no simulator leads at all levels'; 'SimulatorArena highest ranking agreement, the profile-based Sonnet 5 highest fidelity'), reporting the leaderboard response to only 2 of its 10 injected faults ('all three miss agent favoritism although it shifts agent ranks', Table 6: $\tau$ shift 0.04-0.06). Sim2Real 2603.11245 (card neighbour, abstract): simulators are 'excessively cooperative and uniform, an "easy mode" that inflates agent success above the human baseline' — a population shift, the impact term. Lost in Simulation 2601.17087 (import, abstract): a 9-point range across user LLMs, never agent-matched. The tau2-bench 1.x text board mixes gpt-4.1 and gpt-5.2 user simulators across rows (import, fetched board).
- **If true:** User-simulator fidelity suites report the agent-by-simulator interaction (a matched per-task odds ratio summed over tasks) beside the fidelity index, because the fidelity index is blind to the term that reorders agents; tau2-bench-style boards print the simulator model per row and a cross-simulator SE (4-6 points per agent at one trial, which no board prints); the 'easy mode' finding is reclassified as impact, harmless to a ranking.
- **If false:** If the rank-moving share $\rho < 0.3$ once a within-simulator rerun floor exists: a simulator swap is a shift plus noise, fidelity indices suffice for leaderboards, and the record is a footnote fixing the tau2 voice board's single-trial SE. If the interaction is large but the voice floor cannot be obtained: parked on the floor.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: the card's lane fit, 'nothing converts a fidelity index for the tau2-bench or SimulatorArena simulators into points of leaderboard error'; the paper motivates its utility level with 'Lost in Simulation documents discrepancies between agent success rates measured with simulated and real users' (sec. 2) and prints the agent-score response for two faults only. Who pays: leaderboard operators running simulated users (the paper's own affiliation, Arena; the $\tau$-bench family; HAL's $\tau$-bench cells with a pinned gpt-4o user), simulator builders choosing between the faithful backbone and the agreeing one (Table 4's sign disagreement), and anyone reading a fidelity index as an error bar on a leaderboard.
- **Impact ceiling:** **floor**: The ten-fault displacement table with intervals, cited by the paper's v2 and the next fidelity suite. Requires steps 0-1. Judgment 0.55.; **middle**: A reporting convention — order and level displacement per fault beside every fidelity index — adopted by one suite or one simulator-driven leaderboard. Requires step 2 and a second agent set. Judgment 0.25.; **ceiling**: Simulator-driven leaderboards publish a simulator error bar in rank units from an injection panel, and fidelity suites stop reporting composites. Requires a second backbone, a second agent set and an operator's adoption. Judgment 0.1.
- **Relevance:** Narasimhan route ($\tau$-family): direct — the $\tau^2$-bench recipe is one of the six simulators compared and its fidelity index (82 / 74) has no leaderboard conversion. HAL: indirect (its $\tau$-bench cells pin gpt-4o as the user; the question applies, the replays do not). Evaluators and benchmark-validity work: direct. Industry: moderate (arena operators). Jacob's edge: the affine-invariance identity and the split of $\Delta_p(a)$ into a common offset plus an agent term are napkin algebra; GPUs and physics zero.
- **Kill probe:** Steps 0-1: $0, 0 GPU-h, 5 days on the paper's replays; dead if two of the three detected faults reorder ($\tau_p \leq 0.78$, upper bound under 0.89); parked if the replays cannot be had within 30 days.
- **Density and ownership:** Occupant of the mechanism: the card paper (ten faults, paired replays on gpt-5.6-terra, nine agents), which prints the agent-score response for two faults and the fidelity response for ten. Nearest, from the card: Sim2Real 2603.11245 ('easy mode' on $\tau$-bench with 451 humans; population rates, no per-fault order statement); Lost in Simulation 2601.17087 (success-rate gap; abstract not fetched); SimulatorArena (agreement with human judgments; number of assistants not in the card); SWE-Together 2606.29957 (scores agents by repository correctness and corrective turns). Inference, no fetch this week: no paper reports a per-fault order displacement of an agent leaderboard; density is measured at the kill search in the neighbours' words — 'simulator-derived ranking', 'rank correlation', 'leaderboard agreement', 'robustness of evaluation', 'perturbation', 'user simulator', 'judge', 'satisfa…
- **Why now:** 2611.24892 v1, 18 Nov 2026: the replays exist for the first time; its Table 4 sign disagreement is unexplained in its own text. Flag: the enabling piece is data held by others, and the probe is a sketch until the release is located.
- **Register, and what it is not:** Measurement with a reporting consequence (order and level displacement per fault beside every fidelity index). It is not a new fidelity metric, not the paper's injection protocol on another benchmark, not a claim that simulators are unreliable (Sim2Real and Lost in Simulation own that), and not a verdict on which simulator is best.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Pass on paper: premise numbers fetched (per-agent shifts airline +10.0/-4.0/+10.0/+8.0/+8.0, retail +3.5/+5.3/+14.9/+7.9/+2.6, telecom +3.5/+12.3/-10.1/+15.8/+15.8 from results.json per cell on s3://sierra-tau-bench-public; Kendall $\tau$ 0.60/0.20/0.60; within-simulator rerun discordance 0.196 from the gpt-5 4-trial text release, so a single-trial 114-task shift has SE about 4.2). Conditioning set: the user simulator is a fixed treatment at temperature 0.0 by the harness (read from the harness source, checklist 2026-11-08), so the interaction is a property of the (agent, simulator) pair unde… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass: step 1 is $0 and two days on downloaded files; step 2 under 20 GPU-h. Kill written. Both outcomes informative (the first cross-simulator SE for a tau2 board either way). |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route B (ruler): 'simulator fidelity' split into impact and interaction with the DIF machinery, identifiable from released per-task vectors (tau2 ships them; HAL does not — stated). Surprise three ways: expected $\rho$ in [0.3, 0.7) (judgment 0.45); field assumes a population shift ('easy mode') measured by fidelity indices; belief-changing $\rho \geq 0.7$ in two domains (0.25) or $\rho < 0.3$ once a floor exists (0.30, kills it). Flag for the kill search: the benchmark owners' protocol sections (checklist 2026-11-01) — tau2-bench's own paper and 2611.24892 sec. 5 must be grepped for 'interac… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | One community with adjacent consumers: user-simulator meta-evaluation authors (report the interaction), benchmark owners (simulator model per row, cross-simulator SE), agent developers choosing a simulator for development (a shift is harmless, an interaction is not), the attribution instrument of the L1 lane. Proper-shaped. |
| G4 | mechanism and consequence | Mechanism: $\mathrm{logit}\,p_{aig} = \theta_a - b_i + \lambda_g + \delta_{ig} + \gamma_{ag} + \epsilon_{aig}$; a leaderboard column under $g$ averages over $i$, so $\lambda_g$ and $\delta_{ig}$ cancel in differences between agents and only $\gamma_{ag}$ and the residual move the order; a population fidelity index is a function of the margins and carries no $\gamma$. Consequences per outcome written above. |
| G5 | durability; lab-adjacent | Durable: the decomposition applies to any agent-simulator matrix; flag — tau2-bench board composition changes, and the voice board's judge is part of the reward. |
| G6 | ownership, density, race window; position clause | Import's density: field words x simulator words 14 hits (0 on point); sim-vs-real-user words 57 (8 on point, none decomposes); 2601.17087 and 2609.00482 (family DIF on static suites) closest. Kill search owed in the owners' words (agent favoritism, simulator bias, user-model sensitivity, cross-simulator, matched). Why now: the tau2 voice board shipped same-agent pairs under two simulators (November 2026) and 2611.24892's paired replays. Race: user-simulator papers about one a week; window judged adequate for the $0 step. |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W47-04 | Level or order: what each injected user-simulator fault does to the agent leaderboard the fidelity suites were built to… | Steps 0-1: $0, 0 GPU-h, 5 days on the paper's replays; dead if two of the three detected faults reorder ($\tau_p \leq 0.78$, upper bound under 0.89); parked if the replays cannot be had within 30 days. | killed | — |
| C-W47-05 | Nine agents cannot order six simulators: the resolution of the leaderboard-agreement score in user-simulator meta-evalu… | Steps 0-1: $0, 0 GPU-h, 3 days; dead if the top two simulators' intervals do not overlap with outranking probability above 0.95, or if Table 4 already carries separating intervals. | parked | — |

Also under this claim (no scorecard yet): import:2026-W47-S1xF2 (step 1 $0, 2 d on the five paired tau2 voice submissions and the gpt-5 4-trial text release; step 2 about 20 GPU-h, about $350, 9 d tota…

## Kill search

### Concept level (CL-W47-02) — killed (2026-11-22)
The two-term reading (order displacement vs scale shift of a simulator swap, each invisible to the other's check, against a seed-rerun floor) is 2609.00982's stated acceptance criteria and reporting rule; the identity is 2608.22432's double-centering; GAUGE ran 25 agents x 2 simulators on tau2 retail and read it as a shift; the seed's conclusion already reports per-agent effects beside fidelity.
Full record: [`/home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-02.md`](../../..//home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-02.md).
**Occupied by:** 2609.00982 (concept: two terms with a floor on a simulator swap); 2608.22432 (identity: evaluator-by-system interaction by double-centering, shift cancels); 2609.27787 (structure: system-by-instrument term sets the single-instrument ceiling); 2609.12191 GAUGE App. D (the tau2 25x2 grid, ordering preserved); 2611.24892 conclusion (if_true equals the seed's fix)
**Why not done before:** It was done in the two adjacent facets (judge language; trained-vs-prompted companion simulator) and on tau2-bench with 25 agents by GAUGE, read as a shift; for the voice pairs specifically, no reason found: the vendors read the gpt-5.5 rows as capability statements and only #729's timing review has asked about comparability.
Closest neighbors (one-sentence trick; one-line difference):
- `2609.00982` Disclosure-Gated User Simulation for Companion-Agent Evaluation — Swap the user simulator under twelve fixed systems, re-run the reference under a new seed for a noise floor and band, and read each replacement as largest rank displacement plus per-system score change. *Difference:* none at the concept level: has the two terms, the floor, the blindness of each check to the other term, a pure-shift swap and a pure-reorder swap, and the reporting rule; lacks DIF vocabulary, a per-task odds ratio and a verifiable-reward benchmark (vocabular…
- `2608.22432` Rank Reversal in Multilingual LLM Judges: A Label-Free Double-Centering Calibrator — Write an evaluator-by-system score matrix as task difficulty plus system skill plus an evaluator-by-system interaction and recover the interaction by double-centering the cell means. *Difference:* owns the identity (two-way ANOVA under sum-to-zero contrasts; the shared shift cancels; the three-way term is the named risk); the group is the judge's language, a post-hoc scorer, not an in-loop party
- `2609.27787` Ask Which, Not How Good: Sizing Benchmarks Scored by an LLM — Decompose 373,019 judgments into system, item, judge and interaction components and show the system-by-judge term is the one more items cannot average away. *Difference:* the structural statement behind the claim's mechanism in G-theory form, with measured floors; judge facet, not simulator
- `2609.12191` GAUGE: When Not to Trust LLM-as-a-Judge in User-Simulated Evaluation of Task-Oriented Age… — Run 25 agents on tau2-bench retail and airline under a persona-driven simulator and a judge, test whether the judged ranking tracks verifiable reward, and re-run the whole grid under a second-provider simulator. *Difference:* holds the claim's design on the claim's benchmark at 25 agents x 2 simulators x 114 tasks (App. D) and reads it as a shift ('the harsher simulator surfacing more task failures'; 'The ordering persists'); reports no between-agent spread of the displacement; ma…
- `2611.24892` the seed: user-simulator meta-evaluation suite — Grade six simulators by ranking agreement, population fidelity and trace fidelity, inject ten faults, and show fidelity suites miss the agent-selective ones. *Difference:* already reads agent-selective faults as rank movers invisible to trace diagnostics and reports 'per-agent effects' beside fidelity (conclusion); the claim adds a natural swap and a floor to a paper that owns the frame
*Search degraded:* ['s2 (skipped by rule)', '2609.38043 arxiv.org/html served a stub (3,574 words); abstract-only', 'conference exports not built']

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- C-W47-05 is parked — Steps 0-1: $0, 0 GPU-h, 3 days; dead if the top two simulators' intervals do not overlap with outranking probability above 0.95, or if Table 4 already carries separating intervals.: fund it, or leave it parked?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-22 — claim open: born W47 claims stage (bottom-up): import S1xF2's $0 voice-board computation plus two card probes; concept-level kill search scheduled this run
- 2026-11-22 — claim killed: concept-level kill search (/home/claude/idea-pipeline/data/reports/2026-W47-kill-CL-W47-02.md): killed — gate G2B (surprise equals the stated knowledge of the two nearest communities); G4 and G6 fail behind it; The two-term reading (order displacement vs scale shift of a simulator swap, each invisible to the other's check, against a seed-rerun floor) is 2609.00982's stated acceptance criteria and…
- 2026-11-22 — C-W47-04 killed: W47 concept-level kill search of CL-W47-02: probe verdict killed. its claim is the seed's conclusion sentence ('substantial changes in selected agents' scores and ranks can coexist with weak responses from the available trace diagnostics'; 'We therefore report fidelity, per-agent effects and agreement ... together'), and the 351 sessions and paired replays have no release location in the paper
- 2026-11-22 — C-W47-05 parked: W47 concept-level kill search of CL-W47-02: probe verdict parked. footnote, not a probe: at n = 9 one swapped pair moves tau by 0.056 and the null SD is 0.266, so Table 4's 0.44-0.67 spread is under one null SD; Table 4 carries no intervals (HTML checked); the sizing question for instrument-scored comparisons is owned by 2609.27787; re-open trigger the sessions' release, cost one day, outcome a f…

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W47-02`, version 2)
- probe `C-W47-04`: `data/candidates/2026-W47.jsonl`
- probe `C-W47-05`: `data/candidates/2026-W47.jsonl`
