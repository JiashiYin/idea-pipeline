# Penalising or filtering physics violations in simulation teaches robot policies to exploit the simulator where the checks cannot see; routing those gradients into sacrificial parameters and ablating them before deployment transfers better than penalties or filtering - and the ablation drop is the policy's exploit share.

`CL-W44-J02` · lane **L5** · status **thought** · rank — · position solo · refreshed 2026-10-30

## Status

A thought from `/capture`: not yet graded against the gates; its kill search has not run. Failing gate: none recorded. Next action: see First steps.

## The claim

- **Headline:** Penalising or filtering physics violations in simulation teaches robot policies to exploit the simulator where the checks cannot see; routing those gradients into sacrificial parameters and ablating them before deployment transfers better than penalties or filtering - and the ablation drop is the policy's exploit share.
- **Current belief (the field's):** GRAFT 2610.17062 (fetched 2026-10-30, abstract): with a misspecified reward and a monitor that makes systematic errors, filtering or penalising flagged samples fails - the model learns to hack in undetected ways; constraining the flagged samples' gradient updates to a sacrificial set of new adapter parameters keeps the monitor out of the reward (so misbehaviour is not hidden) and ablating those parameters removes the behaviour while keeping target-task gains; shown on 135M-8B models in RL and by distilling hacking trajectories into Qwen3-32B. Gradient routing 2410.04332 (fetched): data-dependent gradient masks localise capabilities even from a limited, ad-hoc subset of the data (absorption). The robotics field's answers to simulator exploits are penalties and constraints - action-Jacobian penalty 2602.18312 (policies exploit unachievable high-frequency actuation), Lipschitz-constrained policies 2504.08246, SAPU 2305.17110 (drop episodes over 1 mm interpenetration, down-weight the rest), and domain randomisation (Peng 2017) - i.e. exactly the 'penalise or filter' arm GRAFT argues drives hacking underground when the monitor is imperfect. No application of gradient routing to robot policies or simulators in the fetched set (7 abstract hits for 'gradient routing', none robotic).
- **If true:** The ruler's physics checks become a training ingredient without becoming a reward: sim-to-real pipelines add routed sacrificial parameters beside domain randomisation; benchmarks report an exploit-ablated score beside the raw score; the ablation drop is a causal, policy-internal estimate of realised exploitation that needs no converged reference engine (so it exists for soft bodies).
- **If false:** Either exploits and skills share representations in continuous control so ablation removes skill too (then routing is for discrete agents only), or penalties do not drive hidden exploitation in physics (then SAPU-style filtering is fine and GRAFT's premise does not carry).

## Scorecard (from the cheapest probe's record, or the claim's skeleton for a thought)

- **Target value:** Who asked in print: GRAFT states the failure of penalise-or-filter under an imperfect monitor and demonstrates it only on LLM RL; SAPU documents interpenetration exploitation and answers with filtering; the action-Jacobian and Lipschitz papers answer with penalties. Who pays: every sim-to-real pipeline that currently shapes rewards against artifacts; benchmark owners who want an exploit-ablated score.
- **Impact ceiling:** **floor**: A controlled study on two tasks showing whether penalties drive hidden exploitation in physics and whether routing localises it - citable either way. p = 0.6 (judgment).; **middle**: Routed sacrificial parameters with a physics monitor become a standard ingredient beside domain randomisation, and the ablation drop is adopted as the exploit-share measurement for soft-body tasks where no converged reference exists. p = 0.2 (judgment).; **ceiling**: Exploit-ablated scores become a reported column for simulator-trained policies and the method ships in a training framework. p = 0.1 (judgment).
- **Relevance:** L5 direct; L2 (training dynamics) direct - it is an RL-safety method imported into robotics; robotics faculty route high; systems route zero; Narasimhan route zero; Jacob's edge: the monitor is our ruler (numerics), the routing is a gradient-masking implementation (GPU/JAX). Core-ML flavour: yes - alignment-style method, robotics-grade test.
- **Kill probe:** P-W44-J02-a: 10-30 GPU-h, $50-100, two weeks; dead if nothing exploit-specific is localised or routing does not beat DR and penalties on transfer.
- **Density and ownership:** Gradient routing in robotics or simulators: none found (7 abstract hits, 2 real papers, both non-robotic). Penalty/constraint answers to exploits: 2602.18312, 2504.08246, SAPU. Race flag: the GRAFT authors (an obvious next domain), and any sim-to-real group that reads GRAFT this month.
- **Why now:** GRAFT is eighteen days old; the ruler supplies the imperfect monitor it assumes; MJX and Playground make the 2 x 4 x 2 arm grid a two-week job.
- **Register, and what it is not:** A recipe with a measurement attached (the ablation drop); not a new simulator, not a new RL algorithm - an import of a two-week-old alignment method into robot learning.

## Gates (config/standards.md)

| Gate | Test | Verdict |
| --- | --- | --- |
| G0 | premise hygiene (conditioning set, whose temperature, fetched numbers) | untested |
| G1 | cheap to kill (cheapest probe under one GPU-week, kill result pre-registered) | carried by the cheapest probe P-W44-J02-b (see Probes for its cost and verdict) |
| G2 | pressure (stated strain, or ruler with pre-registered surprise) | untested |
| G3 | consumers (three classes, the action each changes; community-wide for golden) | untested |
| G4 | mechanism and consequence | untested |
| G5 | durability; lab-adjacent | untested |
| G6 | ownership, density, race window; position clause | untested |

## Probes under this claim

| Probe | What | Kill probe (cost, criterion) | Status | Kill-search verdict |
| --- | --- | --- | --- | --- |
| P-W44-J02-a | Implement step-level gradient routing in the PPO update (two parameter groups; flagged steps' loss terms update only th… | Pre-registered: dead if the ablation drop in the converged engine equals the drop in the training engine on both tasks (nothing exploit-specific was localised), or if the routed-and-ablated policy transfers no better than DR alone and no b… | thought | not run (no candidate record yet) |
| P-W44-J02-b | GRAFT's own regime ported to simulation robotics: the policy is an open-weights code-writing model (Qwen3-8B or -32B cl… | Pre-registered: dead if ablating the adapter costs as much in the trusted engines as in the training engine (nothing exploit-specific localised), or if routing transfers no better than the penalty and filter arms. Expected (judgment): the… | thought (Jacob's preferred shape, 2026-10-30: no real robot; code-as-policy LLM agent; avoids the small-MLP representation question) | not run (no candidate record yet) |

## Kill search

Not run yet. Kill searches run automatically on the top probes, claim by claim (config/generation.yaml); `/kill <probe>` runs one by hand.

## Red team

Not run. A red team (three personas, fetched evidence; `/redteam <probe>`) runs only on a probe that survived its kill search; nothing is called proper before it.

## First steps if pursued

1. Wait for the automatic kill search on **P-W44-J02-b** (Sunday run), or run `/kill P-W44-J02-b` in a session.
2. If it survives: `/redteam P-W44-J02-b`, then the probe as pre-registered — Pre-registered: dead if ablating the adapter costs as much in the trusted engines as in the training engine (nothing exploit-specific localised), or if routing transfers no better than the penalty and filter arms. Expected (judgment): the frontier model's code-as-policy trajectories contain a measurable exploit fraction on contact-rich tasks (penetration-assisted grasps, solver-error-assisted ins…
3. Write results into the records and this Log; status moves only on evidence.

## Decisions for Jacob

- Run P-W44-J02-a as the L5 thread's next experiment (two weeks, $50-100), in place of or beside the 2x2?

## Jacob

<!-- Yours. Preserved verbatim on every refresh. Write marks here: `promote`, `jacob-dropped`, `park: <reason>`,
     a question, a correction. The operator applies marks to the records and answers questions in the Log. -->

- status mark: (none)
- notes:

## Log

- 2026-10-30 — claim thought: captured from Jacob's question about GRAFT 2610.17062; density checked (no robotics application); kill search owed
- 2026-10-30 — claim thought: Jacob 2026-10-30: no real robot; prefer a code-as-policy frontier-model-based agent in simulation; asked whether a prior catalogue of hacks is needed. Variant b written: GRAFT's own LLM regime (RL or distillation into an open student) with the ruler as the imperfect monitor and a trusted-simulator ladder as the deployment test; no hack catalogue required

## Records

- claim record: `data/claims/claims.jsonl` (id `CL-W44-J02`, version 2)
- `P-W44-J02-a`: seed or import record (no candidate yet)
- `P-W44-J02-b`: seed or import record (no candidate yet)
