# In a growing self-evolving lesson store (WikiTrace's insights-only store on ALFWorld's 134 unseen tasks over three passes with a Qwen3-30B-A3B actor), a lesson's per-use harm — the paired drop in success with the lesson retrieved versus withheld — is set by the store it is retrieved with, not by its birth or its own age: mean harm rises by at least 0.05 from a lesson's first use to its eighth-or-later use in the growing store and by under 0.03 in the same store frozen after the first pass.

`CL-W46-04` · lane **L4** · status **open** · rank 7 · position both · refreshed 2026-11-16

## Status

Open claim. Nothing under it has survived a kill search yet. Failing gate: Gate 6 unmeasured (kill search owed); Gate 2B flagged (crowding stated at library level by 2605.19576; the per-lesson shape is the difference). Next action: see First steps.

## The claim

- **Headline:** In a growing self-evolving lesson store (WikiTrace's insights-only store on ALFWorld's 134 unseen tasks over three passes with a Qwen3-30B-A3B actor), a lesson's per-use harm — the paired drop in success with the lesson retrieved versus withheld — is set by the store it is retrieved with, not by its birth or its own age: mean harm rises by at least 0.05 from a lesson's first use to its eighth-or-later use in the growing store and by under 0.03 in the same store frozen after the first pass.
- **Current belief (the field's):** FGSE 2611.14326 abstract (fetched 2026-11-15): lessons are admitted only after 'target-transfer, falsification, and archived-regression probes', reducing 'harmful committed updates to 3.6%' — defects are at birth and a probe battery finds them. WikiTrace 2611.14320 abstract (fetched): degradation happens when the agent 'follows a lesson that is incorrect, or misapplies or misreads a valid one', so the agent 'descends through its links' at every use — harm is a per-use draw. 2610.17544 abstract (fetched): 'A contracted memory saves reasoning steps and errors until its facts change, then quietly answers wrong' — constant within an epoch. TrackRL 2610.25126 abstract (fetched): skills 'becoming redundant after the model internalizes their capabilities ... still others turning harmful', with protected incubation for young skills. Library Drift 2605.19576 abstract (fetched): 'unbounded skill accumulation ... causes retrieval degradation, false-positive injections' — crowding named at library level, measured as pass@1 over 100 rounds, never per skill against its age.
- **If true:** Memory-induced degradation is reported as a curve over use-age with a frailty share, not one rate; admission-gate builders size the probe count from the per-use harm via $1 - (1 - p)^{k}$ and read their residual as leakage, not a defect floor; per-use inspection is restricted to the frailty minority once identified; lifecycle and certificate designers put a store-size term in the null instead of constant-within-epoch; capacity or age bounds become the default retirement design for rule files and auto-memory in coding agents; a lesson's value, like a memory's in CoReMem, is read as a property of the (lesson, store, actor) triple.
- **If false:** If the hazard is flat with strong frailty, burn-in is a frailty screen with a computable probe count and expiry buys nothing — FGSE's design is right and its residual is leakage at its probe count; if the hazard falls after frailty is removed, the first real uses are the admission test and TrackRL's protected incubation has the wrong sign; if it rises at fixed store size, a lesson is degraded by its own age, a reading-drift mechanism no fetched source names; if pooled harm is under 0.02, lesson-grain degradation on ALFWorld is too small for a lifecycle design to matter and the four designs are indistinguishable at benchmark scale — a footnote the admission and inspection papers would cite.

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** In print (abstracts fetched 2026-11-15): WikiTrace 2611.14320 (memory-induced degradation named and reduced); FGSE 2611.14326 ('when an experience-derived behavioral update should be admitted into persistent agent state'; 3.6%); 2610.32578 (a six-week ledger of 118 agent failures under rule files; 'Stale documentation (drift) was the largest failure class (48 of 118)'); TrackRL 2610.25126 (lifecycle management from per-skill counterfactual evidence); Library Drift 2605.19576 (crowding named; 'premature retirement (active harm, $-0.019$)'); 2610.17544. Who pays: builders of self-evolving memory choosing between admission probes, per-use inspection and expiry; teams running rule files and auto-memory in coding agents; evaluators who report one degradation number.
- **Impact ceiling:** **floor**: pooled harm under 0.02 or no shape and no frailty: a footnote giving the per-retrieval harm of lesson-grain memory on ALFWorld and saying the four lifecycle designs are indistinguishable at benchmark scale. Requires step 1. Judgment p 0.35.; **middle**: a shape and a frailty share on one harness with the policy it selects (probe count from the leakage formula, or a capacity / age bound) and FGSE's residual read as leakage: a proper idea; self-evolving papers report degradation by use-age. Requires steps 1-3 with the frozen null passed. Judgment p 0.45.; **ceiling**: the shape replicates across harnesses (AppWorld, a coding harness with repository drift), the leakage formula predicts admission-battery residuals in two papers, and the lesson-lifecycle ruler becomes the column every self-evolving memory paper reports; a lab-adjacent standard. Requires step 4 and one more harness, $400-800. Judgment p 0.2.
- **Relevance:** L4 all routes, Narasimhan's self-evolving interest directly (a measurement with a protocol consequence); L1 through the reliability register (hazards, replicates); L2 only as the counterfactual estimator TrackRL already uses; L3 and L5 zero. Industry: direct (coding-agent products write rules and auto-memory with no retirement policy; 2610.32578 says the stores only grow). Jacob's edge: power-law hazards, mixtures of constant-rate units reading as a falling pooled hazard, the Duane plot and the $1 - (1 - p)^{k}$ screening arithmetic are his to check by hand; the bathtub is his to say in a talk.
- **Kill probe:** Step 1 (about 18 GPU-hours, $60, 6 days) plus step 2 (10 GPU-hours, 2 days): dead if pooled harm is under 0.02 (upper end under 0.04); dead as a ruler if the frozen arm trends or the $(\beta, \gamma)$ fit cannot separate; dead as an import if bins agree within 0.03 and frailty variance includes 0.
- **Density and ownership:** L4 is the densest lane (about 3.4 compaction-agent papers a week by the CL-W45-08 kill search's count); lifecycle papers ran at about two a month in October 2026 (TrackRL, SkillForge 2610.09832, Selm 2610.24630, 2610.32322, 2610.32578, REM 2610.27377, 2610.17544) and two more in November (WikiTrace, FGSE); this run's lifecycle query returned 226 hits with none fitting a per-lesson hazard against use-age. Occupied: lifecycle state machines with incubation and retirement (TrackRL, SkillForge), staleness as a change-point with certificates (2610.17544), crowding at library level (Library Drift), admission probing (FGSE; PACE 2606.08106, the W42 S12xF3 record), the per-lesson with/without contrast (TrackRL; CoReMem; RBC 2610.18427's randomised inclusion of playbook lessons), lessons carrying chance from lucky runs (2610.33029, 256 synthetic worlds), 'presence is not responsibility' for skil…
- **Why now:** WikiTrace and FGSE (2026-11-10); CoReMem (2026-11-12); TrackRL (2026-10-18); 2610.17544 (2026-10-13); 2610.33029 (2026-10-12); the survival vocabulary (Kaplan-Meier in 2610.17544) is already in the lane.
- **Register, and what it is not:** —

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | Quantity defined before the estimator: $\hat\delta_{\ell u} = (c_{\ell u} - a_{\ell u}) / n$ at $n = 4$, signed, averaged by bin (never a binarised induced-failure event, whose false rate at $n = 3$ and $q = 0.5$ is 0.25); conditioning set: fixed task, lesson text, store state at retrieval, actor and sampling, deterministic environment (no luck term; programmatic verifier). Whose temperature: the actor's deployed setting, read from WikiTrace's code before the run (not in the abstract — recorded as unknown until read); the writer's temperature enters the frailty distribution only and is report… |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | Pass: C-W46-09 steps 1-2 at about 28 GPU-hours and $100 in 8 days; kill written at three levels (pooled harm under 0.02; frozen arm trends or the fit cannot separate; bins within 0.03 with frailty variance including 0); both outcomes citable (the negative is the first per-retrieval harm rate of lesson-grain memory with a frozen-store control). |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | Route B: a ruler (hazard by use-age with a frailty share and a crowding exponent) with a pre-registered surprise — expected (judgment 0.4) a rise absorbed by store size against four designs that each presuppose a shape they never measured (burn-in: FGSE; per-use draw: WikiTrace; constant within epoch: 2610.17544; internalisation with protected youth: TrackRL); the ruler's expected reading equals none of their statements. Flag for the kill search: Library Drift states crowding at library level, so if the answer is crowding its authors will say they said so; the difference is per-unit shape, th… |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | Consumers with actions: admission-gate builders (size $k$ from $p$; report predicted leakage), per-use inspection builders (restrict the descent by age or frailty), lifecycle and certificate designers (store-size term in the null; incubation sign from the early hazard), evaluators and rule-file operators (report degradation by use-age; schedule re-tests by shape). One community (self-evolving agent memory) must change what it reports — proper-shaped; community-wide only if the shape replicates across harnesses. |
| G4 | mechanism and consequence | Mechanism: ALFWorld tasks are drawn from a fixed distribution with no fact edits, so between a lesson's first and tenth use only the store around it changes; more co-retrieved lessons mean more conflicts and misapplication (Library Drift's false-positive injections at lesson grain). Consequence per branch written in if_true and if_false: capacity or age bound; frailty screen with a probe count; early uses as the admission test; age-based re-validation; or no lifecycle lever at benchmark scale. |
| G5 | durability; lab-adjacent | Durable as a ruler: the hazard-by-use-age design applies to any lesson store, actor and harness; the specific shape is measured on ALFWorld only until step 4 runs (flag: no fact edits there, so the rising-at-fixed-store branch has judgment probability under 0.1 on this benchmark and the AppWorld arm is where it would show). Lab-adjacent: measurement of shipped memory designs, no recipe. |
| G6 | ownership, density, race window; position clause | Unmeasured: concept-level kill search owed (rule 17). Density: this run's lifecycle query 226 hits, none fitting the per-lesson hazard; the import's Q1 30 and Q2 181 (about 20 lifecycle papers); sub-lane rate about two a month. Nearest: TrackRL (per-skill contrasts; lifecycle states; no age), 2610.17544 (change-point; Kaplan-Meier of retirement delay, not time-to-first-harm), Library Drift (crowding at library level), FGSE (admission residual), WikiTrace (per-use inspection; harness), RBC 2610.18427 (randomised inclusion for curation), 2610.33029 (lessons carry chance), GRSE 2610.27227 (prese… |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W46-09 | A lesson's hazard against its use-age: the paired per-use harm of a self-written lesson by use-age bin, with lesson fra… | Step 1 (about 18 GPU-hours, $60, 6 days) plus step 2 (10 GPU-hours, 2 days): dead if pooled harm is under 0.02 (upper end under 0.04); dead as a ruler if the frozen arm trends or the $(\beta, \gamma)$ fit cannot separate; dead as an import… | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **C-W46-09** (Sunday run), or run `/kill C-W46-09` in a session.
2. If it survives: `/redteam C-W46-09`, then the probe as pre-registered — Step 1 (about 18 GPU-hours, $60, 6 days) plus step 2 (10 GPU-hours, 2 days): dead if pooled harm is under 0.02 (upper end under 0.04); dead as a ruler if the frozen arm trends or the $(\beta, \gamma)$ fit cannot separate; dead as an import if bins agree within 0.03 and frailty variance includes 0.
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- None pending; the machine runs the next kill search on its own. Mark `jacob-dropped` here if the headline is not worth a week of yours.

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-11-15 — claim open: born W46 claims stage, origin bottom-up by lifting import:2026-W46-S12xF9 with the WikiTrace and FGSE seeds and the CoReMem estimator; headline quantifier (at least 0.05 rise against under 0.03 frozen) set at the import's P1; the attribution clause's own death condition written; the CoReMem valuation-noise alternative recorded as a thought (owners can print it; CL-W45-08's shape); concept-level k…
- 2026-11-15 — claim open: claims (W46, 2026-11-15): ranked 7: born W46: 28 GPU-h probe on a released store; Library Drift states crowding at library level (2B flag); concept-level kill search runs this week (rule 17)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W46-04`, version 1)
- probe `C-W46-09`: `data/candidates/2026-W46.jsonl`
