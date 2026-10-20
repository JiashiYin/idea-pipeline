# GPU physics engines trade physics for speed through solver iteration caps, and RL policies trained in them exploit the difference.

`CL-W43-01` · lane **L5** · status **open** · position both · refreshed 2026-10-19

## Status

Open claim, ungraded or partly graded; nothing under it has survived a kill search yet. Failing gate: none recorded. Next action: see First steps.

## The claim

- **Headline:** GPU physics engines trade physics for speed through solver iteration caps, and RL policies trained in them exploit the difference.
- **Current belief (the field's):** Engine defaults (MJX/Warp capped Newton; Playground iterations=1 for Go1) are treated as adequate; 2610.17221 declines the solver axis because 'convergence is non-monotone in the outer-iteration count'
- **If true:** Every GPU-RL robotics paper must report its solver settings and a fidelity check; engine builders expose a per-step fidelity flag; the audit becomes a standard column
- **If false:** Caps are harmless at the states policies visit — a reassuring measurement engine teams would still cite

## Scorecard (from the cheapest probe's record; the claim-level scorecard is written by `/claims`)

- **Target value:** Asked in print: 2610.17221 declines the SIMPLEC solver axis because 'convergence is non-monotone in the outer-iteration count' and its recipe needs a known law (card, method and limitations); the MuJoCo XML reference asserts warm-start accuracy without a number; Playground ships iterations=1 (go1_mjx_feetonly.xml). Who pays: every group choosing `iterations` in MJX/Warp/Newton, and engine teams choosing defaults.
- **Impact ceiling:** **floor**: A measured dose-response table (e vs K, e vs substep) for four Playground tasks and two policies; an engineering note others cite when choosing caps. Requires the 10 GPU-hour probe. p = 0.85 (judgment).; **middle**: The law is per state and contact-driven; a per-state fidelity tag built from n_t and the residual becomes the stated missing ingredient for fidelity scheduling in GPU RL, and the exploit heatmap shows return concentrated on cap-hit steps. Requires the bimodal result on at least two tasks. p = 0.4 (judgment).; **ceiling**: Playground or Warp adds a per-task iteration audit or changes a default; the result is the measurement half of the lane's 'iteration caps silently trade physics for speed' paper, with the scheduler as the systems half. Requires rho_L5 separation on Go1 and a real-impact validation (lane kill test 3). p = 0.1 (judgment).
- **Relevance:** Robotics and learning faculty: a measurement with a recipe consequence, direct. Systems route: the per-world rho_t and cap-hit distribution is exactly the input the iteration-level scheduler needs (lane kill test 2). Engine builders: consumers of the audit. Industry: every GPU-simulator RL shop. Jacob's edge: convergence order and numerics (theoretical physics), GPU batch behavior (computer engineering), both load-bearing. Zero for L1-L4 routes and for any LLM-agent consumer.
- **Kill probe:** Re-step 200k visited states at 8 caps and 4 substeps in MJX, fit per-state geometric law, compute rho_L5 for coarse and converged Go1 policies; 10 GPU-hours, about $30, 5 days; dead if a single-rho fit holds on >= 90% of contact steps everywhere, or if e(K_default) < kappa on >= 99% of steps and rho_L5 does not separate the two policies.
- **Density and ownership:** —
- **Why now:** Capped Newton became the production path (MJX 2023, Warp 2025); Playground shipped iterations=1 for Go1 in Feb 2025; Warp exposes solver_niter per world (read 2026-10-19); 2610.17221 (Oct 2026) states the recipe that needs the law.
- **Register, and what it is not:** Measurement (a dose-response law along visited states) with a ruler consequence (what it grades first: the shipped `iterations` values in Playground model files and Isaac Lab's solver iteration defaults). It is not a new simulator, not a contact model, not a method, not a benchmark suite.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | untested — cheapest probe listed: C-W43-15 |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| C-W43-15 | Convergence law of the capped contact solve along policy-visited states | Re-step 200k visited states at 8 caps and 4 substeps in MJX, fit per-state geometric law, compute rho_L5 for coarse and converged Go1 policies; 10 GPU-hours, about $30, 5 days; dead if a single-rho fit holds on >= 90% of | proposed | — |
| C-W43-17 | The solver's own stopping statistic as a free per-step fidelity flag | Record the Newton gradient norm at the cap on the 200k visited states in CPU MuJoCo and correlate with d_t; 6 GPU-hours (5 shared with the convergence-law candidate) plus CPU, about $20, 3 days; dead if raw Spearman < 0. | proposed | — |
| C-W43-14 | Does the real winner survive the engine's speed knobs? | Pilot: 2 tasks x 3 policies x 5 iteration settings x 3 batch seeds x 100 episodes with d_t against the finest setting; ~15 GPU-hours, $0 on public assets, 5 days; dead if absolute rates move < 5 points everywhere and no  | proposed | — |
| C-W43-16 | Compute-matched fidelity mixture versus fixed solver cap in GPU RL | 30 PPO runs at equal solver-iteration budget across 5 arms, 2 tasks, 3 seeds, evaluated under the converged engine with the per-step audit; 50 GPU-hours, about $150, 7 days; dead if the mixture is no better than fixed K= | proposed | — |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml).

## Red team

Not run. A red team runs only on a probe that survived its kill search.

## First steps if pursued

1. Read the kill-search record of **C-W43-15** when it lands; if killed, read what killed it before anything else.
2. If it survived: run its probe exactly as pre-registered — Re-step 200k visited states at 8 caps and 4 substeps in MJX, fit per-state geometric law, compute rho_L5 for coarse and converged Go1 policies; 10 GPU-hours, about $30, 5 days; dead if a single-rho fit holds on >= 90% of contact steps everywhere, or if e(K_default) < kappa on >= 99% of steps and rho
3. Write the result into the probe's record and this thread's Log; the claim's status moves only on evidence.
4. Only then: red team (`/redteam <probe>`), then the next probe under this claim by cost.

## Decisions for Jacob

- (none pending)

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:


## Log

- 2026-10-19 — open: seeded 2026-10-19 so the W43 probes hang under claims; grade and rewrite in the next /claims run

## Records

- claim record: `data/claims/claims.jsonl` (id CL-W43-01)
- probe `C-W43-15`: `data/candidates/*.jsonl`
- probe `C-W43-17`: `data/candidates/*.jsonl`
- probe `C-W43-14`: `data/candidates/*.jsonl`
- probe `C-W43-16`: `data/candidates/*.jsonl`
