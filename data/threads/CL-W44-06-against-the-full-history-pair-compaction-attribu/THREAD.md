# Against the full-history pair, compaction-attributable failures are sourced values that lost their binding (stale or look-alike entries) and dropped constraints, not entries nothing supports (under one in ten), and the provenance judge's +8.9 Pass3 is matched by section drop or matched-count random deletion.

`CL-W44-06` · lane **L4** · status **killed** · rank None · position both · refreshed 2026-11-09

## Status

Killed — see the kill section. Failing gate: Gate 2B (surprise equals stated knowledge) and Gate 6 (occupied; race window under 1x). Next action: see First steps.

## The claim

- **Headline:** Against the full-history pair, compaction-attributable failures are sourced values that lost their binding (stale or look-alike entries) and dropped constraints, not entries nothing supports (under one in ten), and the provenance judge's +8.9 Pass3 is matched by section drop or matched-count random deletion.
- **Current belief (the field's):** SJC 2610.20927 abstract: '83% of failed runs trace back to an action that carries out a specific summary entry, most of which no environment output supports'
- **If true:** Compaction papers report failures against the full-history pair as lost bindings and dropped constraints; the provenance gate is matched by random deletion at matched count — the provenance column leaves the recipe
- **If false:** Unsourced entries do cause a measured share of failures beyond random deletion; SJC's gate stands as a mechanism

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print: HSC-Bench sec. 6, 'was the completion record missing, or did the receiver repeat the operation despite having that record? This distinction identifies whether an observed problem concerns the information passed to the receiver or its use during continuation'; Compact-Bench's abstract, 'retaining relevant information alone does not ensure successful continuation'; CL-W43-05's own open gate (red team 2026-10-25: a census with the uncompressed control and a pre-registered matcher is owed). Who pays: compactor and handoff-writer builders choosing between a provenance gate, retention and receiver prompting; compaction evaluators choosing the axis to add; product teams running orchestrator handoffs.
- **Impact ceiling:** **floor**: A three-cell table on one benchmark, one writer, six receivers, cited by the next handoff or compaction evaluation. Requires step 0 or step 2. Judgment p 0.5.; **middle**: The use axis (in view and unused) adopted as a reported column by one compaction benchmark (Compact-Bench or HSC-Bench) and CL-W43-05 re-scoped to iterative compaction. Requires both corpora agreeing. Judgment p 0.3.; **ceiling**: The census on production compaction chains (Compact-Bench's 106 chains) shows the same ordering and 'in view and unused' becomes the standard decomposition for every lossy agent message. Requires the production chains and a second writer. Judgment p 0.1.
- **Relevance:** Narasimhan (self-evolving agents, memory): moderate, the use axis is the measurement his memory work lacks. HAL and evaluators: direct, a column. Systems routes: zero. Industry (orchestrator and compaction teams): direct. Jacob's edge: computer engineering small (the labeler is parsing code); theoretical physics zero.
- **Kill probe:** Step 0 email and step 1 labeler ($0, 5 days plus the wait); fallback step 2 at most $300, 0 GPU-hours, 7 days; dead if the family-clustered lower bound of $\pi_{\mathrm{inv}}$ is above 0.10 for three of six receivers.
- **Density and ownership:** Fetched 2026-11-01: Compact-Bench 2610.31710 (2026-10-22; paired full-history / summary-only continuations, 14 summarizer backbones, 'LLM summaries retain at most 16.0% of recurring details, compared with 79.1% for mechanical extraction'; code and data public) measures retention and has no provenance cell in its abstract; 'Benchmarks Are Surprisingly Compaction-Friendly' 2610.31778 (2026-10-22) measures dropped constraints by number of compactions; 'Questions That Come Later' 2610.27301 (2026-10-19) compares every method with random deletion at the same budget; Slipstream 2605.08580 validates a summary against the agent's actual next steps at write time (a per-summary use signal, not a failure census); Handoff Debt 2606.02875 scores four handoff views by events and tokens; SJC 2610.20927 is the unsourced census by LLM annotation in the iterative regime; TRACE 2610.08722 the human causal…
- **Why now:** HSC-Bench 2026-10-27 (full-history arm for six receivers, typed criteria); Compact-Bench 2026-10-22 (public pairs); the C-W43-23 red team 2026-10-25 (control and matcher specified).
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | added W45: two cards bear on the census — 2611.05650 states the field norm that a transcript label 'cannot distinguish a cause of failure from something that co-occurs with it' (so C-W44-11 is descriptive and the deletion and injection arms C-W44-12 / C-W44-18 carry the claim), and 2611.03289's Proposition 2 says one episode compacted once determines at most one item value (so per-entry attribution needs the paired replay's designed variation); 2611.06545's ledger-adjudicated counts fall on this claim's side for held-out restrictions (59 of 76 overgeneralized vs 17 invented), a census of sent… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: C-W44-11 step 0 is $0 on Compact-Bench's public full-history/summary pairs |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route A: SJC, Compact-Bench, transparent-compact and Governance Decay each state a different noun for the failure; the field disagrees in print |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | one community (compaction papers) must change the control they report — proper-shaped |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | unmeasured: own kill search owed; race window about 1x time-to-result (eight compaction papers in two weeks) |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W44-11 | Where message-attributable handoff failures sit: dropped, in view and unused, or followed from an invented entry — the… | Step 0 email and step 1 labeler ($0, 5 days plus the wait); fallback step 2 at most $300, 0 GPU-hours, 7 days; dead if the family-clustered lower bound of $\pi_{\mathrm{inv}}$ is above 0.10 for three of six receivers. | killed | — |
| C-W45-05 | Whose words are the unsupported entries? Widening the provenance gate's source set to the agent's own earlier turns, an… | Steps 0 and 1 at $0 on the released handoff-audit records and Compact-Bench pairs, 6 days; step 2 at most $250 in the SJC harness, 4 days; 0 GPU-hours; dead if on two of three corpora the lower bound of $u_1$ is above 0.75 and $u_3$ above… | proposed | — |
| C-W43-08 | Does Source-Judged Compaction win by what it deletes or how much? | Four arms x 168 tasks x 3 runs on GPT-5.6 Luna; ~$700 API, 0 GPU-hours; kills if SJC beats both controls by >= 5 Pass3 with std < 3; 10 days including a one-week harness build. | proposed | — |
| C-W44-18 | One wrong bullet in the agent's own summary, the right value in a fresh tool output: which one does the agent act on? | 60 tasks x six cells x three runs in the public SJC harness on GPT, about $500 API, 0 GPU-hours, 12 days; dead if the fresh output displaces the planted value ($u_S, u_F < 0.25$) or if the fabricated value is taken up at under half the rat… | proposed | — |
| C-W44-12 | The provenance gate, judge-free, on a one-shot handoff sheet: delete the unsourced entries at matched tokens | At most $300, 0 GPU-hours, 10 days after the census labeler; dead as a claim if $|\Delta_D| \geq 2$ with interval excluding zero for three of six receivers. | killed | — |
| C-W44-13 | Unsourced entries by write regime: the same writer and budget, iterating on its own summary versus rewriting from the r… | At most $350, 0 GPU-hours, 12 days; dead if the upper bound of $\rho_u$ is below 2 on both corpora. | proposed | — |
| C-W43-21 | Omission of irrecoverable state versus commission of unsourced bullets: which predicts the compaction penalty on the sa… | Steps 1-3 on the TRACE corpus: ~$60 API, 0 GPU-hours, 5 days (10 with the optional cross-benchmark step at ~$300 more); kills if the unsourced count explains at least twice the penalty variance of the omission count or the omission coeffic… | killed | — |
| C-W44-DEF-L4 | Damage versus dose: the compute-matched, dose-matched comparison of compaction recipes under a forced window, with rand… | The 60 GPU-hour pilot above; dead if random deletion is more than 10 points below both recipes on the paired readout. | parked | — |

Also under this claim (no scorecard yet): import:2026-W44-S3xF11 (fast-variable persistence; $0 step)

## Kill search

### Concept level (CL-W44-06) — killed (2026-11-08)
Clause 1 was published with full-history controls by two independent groups within three days of filing (ARCBench 2611.03223; handoff-audit 2611.06545), so the pre-registered surprise equals the field's stated knowledge (Gate 2B) and two occupants sit inside ten days in a lane at 2.6 papers/week (Gate 6); clause 2's only length control in print (2611.06545's count-matched edit) runs against it.
**Occupied by:** 2611.03223 (ARCBench, 2026-11-02) for clause 1 with the full-history control; 2611.06545 (2026-11-04) for the lost-binding/invented split and, against clause 2, the count-matched control edit
**Why not done before:** an enabling piece landed: ARCBench's public harness with full-context baseline and rule-state/behaviour judges (2026-11-02), 2611.06545's released replay records (2026-11-04), 2611.05650's live-vs-restored control specification (2026-11-04); the natural-failure census remains unrun because the needed-value oracle requires a reference solution and a naturalistic corpus pulls the labeler back to a judge (2606.25449; 2611.05650) — and its expected result is now in print twice
Closest neighbors (one-sentence trick; one-line difference):
- `2611.03223` Do Agents Still Follow the Rules? Benchmarking Rule Compliance under Agent Context Compac… — Inside the pi harness, give the agent a rule and a work history, compact it or keep it whole, issue a request the rule forbids, grade the tool call deterministically, then have judges label whether the summary kept the rule and why the agent broke a rule it s… *Difference:* none for clause 1 — occupied: the census with its full-history pair for rules (agent's own 8.9 vs compaction-added 28.9 of 37.8 violation@3; rule retained 70.1% / partially 26.9% / absent 3.0%; retained-rule runs violate 21.1% vs 8.1% full history; reasons ap…
- `2611.06545` When Do Summaries Become Instructions? Unsupported Policy in LLM Agents' Self-Written Han… — Give each synthetic task a permission ledger, flag summary sentences the ledger contradicts, rerun the successor from the same snapshot with the sentence swapped for filler, deleted, replaced by the truth, or with the full history, and count confirmation requ… *Difference:* none for clause 1's split — occupied for policy sentences (59 of 76 held-out restrictions overgeneralized vs 17 invented; 18 of 42 authorizations stale, 21 look-alike); its count-matched control edit is the first length control on deleting unsourced entries a…
- `2611.05650` Attributing Agent Failures to Their History Needs an Executed Counterfactual: Toward a Re… — Before saying an agent failed because of something in its history, freeze the executable state, edit only the history, continue the same agent, and first prove the restored state replays the live run. *Difference:* methodological, neither side of the noun: the claim's census is a transcript label that 'cannot distinguish a cause of failure from something that co-occurs with it'; every same-snapshot probe owes a live-vs-restored control row (byte-identical snapshots dive…
- `2609.38866` When Context Changes: Understanding Update Failures in LLMs — Put several versions of one variable in context, ask for the current one, and show models answer with an old value while probes still recover the new one — attention drifts to the old values. *Difference:* names the mechanism in NLP's word ('stale binding') as a selection failure with the value in view; conversations and logs, no compaction summary, no actions
- `2608.06057` When History Lies: Evaluating and Improving Tool Use under Misleading Multi-Turn Histories — Build paired Original / Polluted / Oracle-state views of a tool-use history and use eleven gold-preserving edits to split failures into decision state, entity binding and interface execution. *Difference:* the three-cell classification with a control, including an explicit entity-binding cell, for polluted histories rather than compaction summaries

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Read the kill section; the claim is closed unless a new probe or a new enabling piece re-opens it (write that in your section).

## Decisions for Jacob

- C-W44-DEF-L4 is parked — lab compute of >= 3500 GPU-hours and a shared harness (one open scaffold with a pluggable compaction hook and the paired-continuation instrument): fund it, or leave it parked?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-11-01 — claim open: filed as the narrowest surviving headline of CL-W43-05 (killed at concept level the same day); its own concept-level kill search is owed next week (W44 budget of 12 spent) before any probe is designed (rule 17)
- 2026-11-01 — claim open: ranked 2 after the W44 kill searches: $0 step on public pairs; the field disagrees in print on the noun; proper-shaped (race ~1x)
- 2026-11-01 — C-W44-DEF-L4 parked: stage 9 definitive-comparison prospecting (W44 monthly run); lab position
- 2026-11-01 — C-W44-DEF-L4 parked: claim CL-W43-05 concept-level kill search (killed): probe effect 'unchanged' — Lab, parked; random-deletion floor is the residue's length control at scale.
- 2026-11-01 — C-W44-DEF-L4 parked: claim_id CL-W43-05 -> CL-W44-06 (re-homed after the kill searches)
- 2026-11-08 — claim open: claims (W45, 2026-11-08): rank 2 -> 4; ranked 4 (was 2): $0 step on public pairs and a field that disagrees in print on the noun; a second probe (C-W45-05) attached this week; moved below CL-W45-05 (community-wide consumers, exact law) and kept above the new L4 claims because it is further along; race window about 1x (eight compaction papers in two weeks)
- 2026-11-08 — claim killed: concept-level kill search (/home/claude/idea-pipeline/data/reports/2026-W45-kill-CL-W44-06.md): killed — Clause 1 was published with full-history controls by two independent groups within three days of filing (ARCBench 2611.03223; handoff-audit 2611.06545), so the pre-registered surprise equals the field's stated knowledge (Gate 2B) and two occupants sit inside ten days in a lane at 2.6 papers/we…
- 2026-11-08 — C-W44-11 killed: W45 concept-level kill search of CL-W44-06 (data/reports/2026-W45-kill-CL-W44-06.md): killed-with-claim — its expected table is ARCBench Table 3 and 2611.06545 Table 5; 2611.05650 makes the census descriptive
- 2026-11-08 — C-W44-12 killed: W45 concept-level kill search of CL-W44-06 (data/reports/2026-W45-kill-CL-W44-06.md): killed-with-claim — 2611.06545's neutral-vs-count-matched edit is this arm on a ledger-adjudicated corpus
- 2026-11-08 — C-W43-21 killed: W45 concept-level kill search of CL-W44-06 (data/reports/2026-W45-kill-CL-W44-06.md): killed-with-claim — merged into C-W44-11; TRACE release carries no summaries
- 2026-11-08 — C-W44-DEF-L4 parked: W45 concept-level kill search of CL-W44-06 (data/reports/2026-W45-kill-CL-W44-06.md): survives — parked unchanged (lab)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-06`, version 4)
- probe `C-W44-11`: `data/candidates/2026-W44.jsonl`
- probe `C-W45-05`: `data/candidates/2026-W45.jsonl`
- probe `C-W43-08`: `data/candidates/2026-W43.jsonl`
- probe `C-W44-18`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-12`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-13`: `data/candidates/2026-W44.jsonl`
- probe `C-W43-21`: `data/candidates/2026-W43.jsonl`
- probe `C-W44-DEF-L4`: `data/candidates/2026-W44.jsonl`
