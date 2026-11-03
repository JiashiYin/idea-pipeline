# Against the full-history pair, compaction-attributable failures are sourced values that lost their binding (stale or look-alike entries) and dropped constraints, not entries nothing supports (under one in ten), and the provenance judge's +8.9 Pass3 is matched by section drop or matched-count random deletion.

`CL-W44-06` · lane **L4** · status **open** · rank 2 · position both · refreshed 2026-11-03

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 not yet established (kill search owed next week). Next action: see First steps.

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
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | pass: C-W44-11 step 0 is $0 on Compact-Bench's public full-history/summary pairs |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | route A: SJC, Compact-Bench, transparent-compact and Governance Decay each state a different noun for the failure; the field disagrees in print |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | one community (compaction papers) must change the control they report — proper-shaped |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | unmeasured: own kill search owed; race window about 1x time-to-result (eight compaction papers in two weeks) |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W44-11 | Where message-attributable handoff failures sit: dropped, in view and unused, or followed from an invented entry — the… | Step 0 email and step 1 labeler ($0, 5 days plus the wait); fallback step 2 at most $300, 0 GPU-hours, 7 days; dead if the family-clustered lower bound of $\pi_{\mathrm{inv}}$ is above 0.10 for three of six receivers. | proposed | — |
| C-W43-08 | Does Source-Judged Compaction win by what it deletes or how much? | Four arms x 168 tasks x 3 runs on GPT-5.6 Luna; ~$700 API, 0 GPU-hours; kills if SJC beats both controls by >= 5 Pass3 with std < 3; 10 days including a one-week harness build. | proposed | — |
| C-W44-18 | One wrong bullet in the agent's own summary, the right value in a fresh tool output: which one does the agent act on? | 60 tasks x six cells x three runs in the public SJC harness on GPT, about $500 API, 0 GPU-hours, 12 days; dead if the fresh output displaces the planted value ($u_S, u_F < 0.25$) or if the fabricated value is taken up at under half the rat… | proposed | — |
| C-W44-12 | The provenance gate, judge-free, on a one-shot handoff sheet: delete the unsourced entries at matched tokens | At most $300, 0 GPU-hours, 10 days after the census labeler; dead as a claim if $|\Delta_D| \geq 2$ with interval excluding zero for three of six receivers. | proposed | — |
| C-W44-13 | Unsourced entries by write regime: the same writer and budget, iterating on its own summary versus rewriting from the r… | At most $350, 0 GPU-hours, 12 days; dead if the upper bound of $\rho_u$ is below 2 on both corpora. | proposed | — |
| C-W43-21 | Omission of irrecoverable state versus commission of unsourced bullets: which predicts the compaction penalty on the sa… | Steps 1-3 on the TRACE corpus: ~$60 API, 0 GPU-hours, 5 days (10 with the optional cross-benchmark step at ~$300 more); kills if the unsourced count explains at least twice the penalty variance of the omission count or the omission coeffic… | proposed | — |
| C-W44-DEF-L4 | Damage versus dose: the compute-matched, dose-matched comparison of compaction recipes under a forced window, with rand… | The 60 GPU-hour pilot above; dead if random deletion is more than 10 points below both recipes on the paired readout. | parked | — |

Also under this claim (no scorecard yet): import:2026-W44-S3xF11 (fast-variable persistence; $0 step)

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W44-11** (Sunday run), or run `/kill C-W44-11` in a session.
2. If it survives: `/redteam C-W44-11`, then the probe as pre-registered — Step 0 email and step 1 labeler ($0, 5 days plus the wait); fallback step 2 at most $300, 0 GPU-hours, 7 days; dead if the family-clustered lower bound of $\pi_{\mathrm{inv}}$ is above 0.10 for three of six receivers.
3. Write results into the records and this Log; status moves only on evidence.

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

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-06`, version 2)
- probe `C-W44-11`: `data/candidates/2026-W44.jsonl`
- probe `C-W43-08`: `data/candidates/2026-W43.jsonl`
- probe `C-W44-18`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-12`: `data/candidates/2026-W44.jsonl`
- probe `C-W44-13`: `data/candidates/2026-W44.jsonl`
- probe `C-W43-21`: `data/candidates/2026-W43.jsonl`
- probe `C-W44-DEF-L4`: `data/candidates/2026-W44.jsonl`
