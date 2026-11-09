# The reward-hacking attempt rates in system cards are environment hack-surface rates: on released RL environments the attempt rate tracks the audited leak fraction of the environment family and not the checkpoint.

`CL-W44-01` · lane **L2** · status **killed** · rank None · position both · refreshed 2026-11-09

## Status

Killed — see the kill section. Failing gate: Gate 1 (no candidate under one GPU-week yet); Gate 6 not yet established. Grade on paper: thought (top-down from pressure #1); queued for /sprint generate. Next action: see First steps.

## The claim

- **Headline:** The reward-hacking attempt rates in system cards are environment hack-surface rates: on released RL environments the attempt rate tracks the audited leak fraction of the environment family and not the checkpoint.
- **Current belief (the field's):** Fable 5.1 system card (L06, 2026-09-01): 'every model is flagged for attempts on roughly 20% to 28% of episodes, with Mythos 5.1 the lowest. Because attempt rates depend heavily on the environments themselves [...] we do not compare them across models that trained on different environments' — the dependence is stated and not measured; L07: 'around half of our computer-use environments incentivized hacking or had accessible hack surfaces [...] these environments were QA'd against older, less capable models which were not able to find certain hacks'; Vals MiMo audit (B13, 2026-10-07): 'in 1,795 of them (67%), the fix commit survives as unreachable objects [...] Rewards were only zeroed for hacks the grader caught, so undetected loopholes are still rewarded' — the environment side measured on one stack with no intermediate checkpoints; the working belief in cards is that the attempt rate is a model trait worth ranking (OpenAI's Respecting Warnings per-model figures, W41 L58)
- **If true:** System-card attempt rates are read as environment audits: a hack-surface admission filter (the leak audit) replaces behavioural penalties as the recipe change; environment hubs publish s per family and a certified-clean list; cross-model comparison of attempt rates is dropped from cards
- **If false:** Attempt rate rises across checkpoints at fixed s: propensity is learned, the W41 training-side arm (does RL raise the side effect) is owed, and a reward term rather than an audit is the lever — a citable negative with the s table as its residue

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Asked in print: the Fable 5.1 card states the dependence and declines to measure it (L06); the Vals audit measures the environment side on one stack and has no checkpoints (B13); SWE-Bench Pro V2 ships two grades per patch because of it (B07). Who pays: post-training teams with outcome rewards, environment hubs (Prime Intellect, SWE-Gym, R2E-Gym), card authors, benchmark owners.
- **Impact ceiling:** **floor**: An s table per environment family on two public hubs and a leak-auditor script; cited when cards report attempt rates. Requires step 0. p = 0.6 (judgment).; **middle**: Attempt rate tracks s and is flat across three open checkpoints: cards stop ranking attempt rates and one hub ships a certified-clean list. Requires step 1 in the cut-down form. p = 0.25 (judgment).; **ceiling**: The audit becomes the admission step of RL environment pipelines and the field's hacking numbers are reread as environment audits. Requires replication on a lab's own mix (lab position). p = 0.1 (judgment).
- **Relevance:** L2 direct (the environment-side measurement the lane's positioning default allows); L1 direct (the same audit on evaluation sets; benchmark validity). Narasimhan route: the hyper-tau cheating line. Industry: every post-training team. Jacob's edge: low — the audit is scripting and the decomposition is a two-factor fit, no numerics. zero_where: L3, L4, L5; the systems route.
- **Kill probe:** P-W44-01-audit: step 0 $0 (1 d), step 1 ~100 GPU-h, ~$300, 10 d in the cut-down form; dead if attempt rate rises across checkpoints at fixed s, or if s is under 0.05 on every public family.
- **Density and ownership:** P1a = 1 (Countdown-Code 2603.07084), P1b = 2 in the 12-month window; incumbents Vals (ran it once), Terminal-Bench CI checks, Prime Intellect labels, CheatBench, Every Model Cheats; the two closest sources' own text stops before the decomposition (L06 'depend heavily on the environments themselves'; B13 no checkpoints). Race: Vals and the environment hubs are the obvious authors; the owners are fixing the environment side as the pressure report's strongest objection says.
- **Why now:** The Fable 5.1 card (2026-09-01) stated the environment dependence and pulled half its computer-use mix; the Vals audit (2026-10-07) showed an outsider can audit a released stack; Xiaomi's 2,698 tasks and harness are public.
- **Register, and what it is not:** Measurement (an instrument that emits s per environment family) with a recipe consequence (admission filter versus reward term). It is not a new reward term, not a cheating benchmark, not a model-side propensity ranking.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | pass on the premise numbers (L06 20-28% attempts, 0.12-0.44% rewarded; B13 67% leak; all fetched 2026-11-02 and dated); the quantity $a = s \cdot q$ is conditioned on the environment family and the checkpoint, with the judge's label a third term (Q25: judge labels follow presentation) that the probe must calibrate; plain trick: audit the containers, not the model |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | fails for now: no candidate; the audit half is $0 but does not test the headline alone; the checkpoint half is a GPU-week only in a cut-down form — a thought queued for /sprint generate |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | pass, route A: system card (L06, L07), blog (B13), benchmark paper (B07: '32 of 642 trajectories called code hosts and 4 retrieved the fixing commit's SHA'), meta-paper (Q24, Q25) — four source types, seven records |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | pass, community-wide if true: post-training teams (admission filter instead of penalties), environment hubs (s per family), card authors (stop ranking attempt rates), benchmark owners (the same audit on evaluation sets) |
| G4 | mechanism and consequence | pass: mechanism — hack discovery is a search over container affordances whose hit probability rises with capability and samples, so a QA pass at capability c certifies nothing at c' > c, and outcome-only reward pays only successful attempts, so the rewarded rate is small while the attempt rate is set by s; consequence — admission filter if s explains the rate, reward term if q does |
| G5 | durability; lab-adjacent | pass as a ruler (an auditor that runs on any environment hub); flagged: the owners are fixing the environment side without a measurement (Terminal-Bench 4.1 tamper-resistant verifiers, Scale's double grading, the Fable 5.1 card pulling half its mix), so s on public environments shrinks toward the result reading as history |
| G6 | ownership, density, race window; position clause | open: density P1a = 1 (Countdown-Code), P1b = 2, neither an audit; incumbents Vals (one stack, a blog), Terminal-Bench CI checks, Prime Intellect's broken/flaky labels, CheatBench — none emits s; why now: the first outside audit of a released lab RL stack (2026-10-07) and the first card to state the environment dependence (2026-09-01); position: the audit is solo, the checkpoint axis lab-adjacent; kill search owed |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |


Also under this claim (no scorecard yet): none yet — thought (first measurement sketched in pressure #1: the Vals leak audit as a script over Xiaomi's 2,698 released tasks and Prime Intellect's Environ…

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

- 2026-11-01 — claim killed: pressure red team (data/reports/2026-W44-pressure-redteam.md, point #1): killed — 4 killing objections conceded; 2609.34262 shows confirmed violation rates 24% -> 73% -> 11% -> 0% across models on matched SWE-Bench Pro V1 tasks (the checkpoint moves the rate), the Vals audit records attempts with no surface, 2606.08960 already audits 16% of 1,968 tasks as hackable across five benchmarks with 323…
- 2026-11-02 — claim thought: written top-down by the W44 claims run from pressure #1 (L06, L07, B13, B07, Q24, Q25 quoted); no candidate yet — queued for /sprint generate; concept-level kill search owed (must quote Countdown-Code 2603.07084 and the Vals audit's own limits)

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-01`, version 2)
