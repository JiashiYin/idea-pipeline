# Program note — L5, the simulator thread (Part I shaped 2026-10-21; Part II, the meta-benchmark, 2026-10-23)

A lane-level note, above the per-claim threads it links. The claims are graded one by one; this page says what they add
up to, which shape was chosen and why, and what the operator's judgment is. Rewritten when the shape changes; dated.

## The question Jacob asked

Is this work a **systems stack** (an iteration-level scheduler for batched contact solvers) or a **measurement** of
physical simulators used to train agents? He leans measurement and benchmarking, with several results at once — a
surprising measurement about exploitation among them.

## The shape chosen: one instrument, three headlines, the systems piece as a consequence

**The instrument — the simulator-budget 2×2.** Train a policy at the shipped solver budget and at the converged budget
under the full training protocol (domain randomization, kicks, noise), at matched wall-clock; evaluate every policy in
both engines with paired draws. Write $J_e(\pi)$ for the return of policy $\pi$ evaluated in engine $e$, with
$e \in \{\mathrm{cap}, \mathrm{conv}\}$ (the shipped budget and the converged one) and $\pi_{\mathrm{cap}}, \pi_{\mathrm{conv}}$
the policies trained in each. The exploit is the interaction term

$$
X = \big[J_{\mathrm{conv}}(\pi_{\mathrm{conv}}) - J_{\mathrm{conv}}(\pi_{\mathrm{cap}})\big]
  - \big[J_{\mathrm{cap}}(\pi_{\mathrm{conv}}) - J_{\mathrm{cap}}(\pi_{\mathrm{cap}})\big],
$$

what the converged engine takes away from the cap-trained policy beyond what it takes from any policy. Alongside it:
the solver's own certificate per step (gradient norm at the cap, `nchange`) as the fidelity column; sim2sim across
engines (the field's standard exploit test, shipped by Playground and Humanoid-Gym) as the transfer proxy; hardware as
the ceiling arm. This replaces ρ_L5, which the red team showed does not estimate exploitation (it counts reward on
threshold-crossing steps; the return gap is a signed, value-weighted sum of one-step errors).

**H1 — exploitation by task class** ([`CL-W43-01`](./CL-W43-01-gpu-physics-engines-trade-physics-for-speed-thro/THREAD.md),
proposed rewrite recorded in its decisions). *Policies owe little of their return to solver shortcuts in locomotion and
a measurable share in contact-rich manipulation — so part of manipulation's sim-to-real gap is a numerics gap that
budget buys back, not a modeling gap.* Priors from fetched sources: flat-ground locomotion is insensitive to solver
choice (2304.06372 §IV-D); shipped cap-1 Go1 policies transfer to hardware (Playground); interpenetration is exploited
in contact-rich assembly (SAPU 2305.17110); the Leap failures were attributed by the authors to hardware flex and
geometry. Expected (judgment): X ≈ 0 on Go1, X > 0 on Leap. Probe `P-W43-01-2x2`, 4–10 GPU-h, $20–50, one week; dead if
X sits inside the seed interval of zero on both tasks.

**H2 — fidelity is a dose** ([`CL-W43-J02`](./CL-W43-J02-a-gpu-simulator-s-physics-budget-is-a-dose-tran/THREAD.md), thought).
*Transferable return follows one dose-response curve in solver budget per task class, so fidelity can be scheduled like
a learning rate.* Rides on H1's data with two more budgets; the recipe test is C-W43-16 (50 GPU-h). This is where the
lane's systems piece lives now — the iteration-level scheduler is the consequence if the curve is clean, not a product
on its own. From a solo position the scheduler is head-to-head with engine teams; from a lab position it is a paper.

**H3 — the resolution floor** ([`CL-W43-09`](./CL-W43-09-gpu-physics-engines-cannot-resolve-the-policy-re/THREAD.md)).
*Engine-only repeatability and batch-position variance exceed a stated share of the policy-return differences papers
report as improvements.* First step costs $0: a table of 20 papers' reported gains, their seed intervals, and the
engine divergence GPUSimBench measured — the quantifier is measured before it is written (the lesson of CL-W43-02's
refutation). Twin of [`CL-W43-J01`](./CL-W43-J01-the-run-to-run-variance-that-agent-benchmarks-re/THREAD.md) in L1:
the same mechanism (floating-point reduction order under GPU batching) in the LLM serving stack. Together they are one
cross-lane sentence — *the measurement floor of the stack is often larger than the effects papers report* — which is
the kind of headline that travels.

**Deliverables if the program holds:** a measurement paper (H1 + H3, the first with a controlled surprise, the second
with a table nobody has made); a standards artifact — what a GPU-RL paper must report: solver budget, certificate
statistics, engine repeatability, a sim2sim check; and the shippable tool: the audit column (`solver_niter`, `fwdinv`,
residual logging) plus the 2×2 harness, a few hundred lines on top of MuJoCo/MJX.

## Judgment

- **Measurement over stack**, for three reasons that are about position, not taste: a scheduler competes with the
  engine teams (Warp/Newton, Isaac, Genesis) who can ship it in a release; a measurement grades their shipped
  artifacts and every GPU-RL paper is its consumer; and the measurement is solo-feasible this month (public tasks,
  minutes-scale training, tens of GPU-hours) while the stack needs an owned engine.
- **Not a benchmark suite.** Comparing engines on scenes is occupied (GPUSimBench, GPUPhysBench, 2304.06372) and a
  static suite is consumed in months. The lane's own ground is *along the states a policy visits, tied to return and
  transfer* — an instrument applied to shipped policies, not a scene collection.
- **The surprise has to be quantitative.** "Policies exploit simulators" is 2017 folklore with a standard answer
  (domain randomization), and PolySim measured the cross-engine version in-window. What nobody has is the
  knob-isolated, wall-clock-matched share, and its contrast across task classes. If X ≈ 0 everywhere, the result is the
  reassuring number engine teams cite — floor scenario, still citable, not golden.
- **Rough probabilities (judgment):** floor 0.6 (citable numbers + tool), middle 0.25 (task-class defaults change;
  "report your solver budget" becomes a reviewer ask), ceiling 0.1 (manipulation's gap shown partly numerical and
  recoverable by budget; H2's schedule adopted). Relevance: robotics and learning faculty direct; engine teams direct;
  systems route only through H2; Narasimhan route zero. Jacob's edge — numerics, convergence, GPU batching — is
  load-bearing in all three.
- **Why now:** GPU engines made a retrain a matter of minutes (Playground, Feb 2025), so a 2×2 with several budgets is
  a one-day job; the engine teams' own measurers (GPUSimBench, Jul 2026) have arrived at the distribution level and
  stopped there.
- **Open question for Jacob:** "agent-driven accelerated simulators" — if this means GPU-accelerated engines used to
  train agents, it is this program; if it means LLM agents that generate or configure simulations, the natural claim
  is an audit of generated model files for speed-first numerics defaults, and it is a scout until stated.

## What runs next

1. `P-W43-09-lit` — the $0 table (two days, no GPU); it decides whether H3 is a headline or a footnote.
2. `P-W43-01-2x2` — Go1 and Leap, 4–10 GPU-h; kill search first (automatic or `/sprint CL-W43-01`), then the run.
3. H2's two extra budgets ride on step 2.


---

# Part II — the meta-benchmark (2026-10-23, from Jacob's five points and the non-rigid session of 2026-10-23)

Jacob's position: domain-specific simulators and sim-generated datasets are consortium-scale and not an academic target;
the academic target is one level up — a system that benchmarks the simulators and datasets themselves. Low capital,
high ceiling if engine and dataset releases report it; quantities of interest: fidelity, robustness to hacking,
speed–accuracy, affinity to parallel hardware; AI agents involved meaningfully or not at all; the main fear is
ad-hoc metrics (fixed exploit lists, pass-through checks, engine quirks, dimensionful thresholds, one task class) that
cap the claim. The non-rigid session had already reached three axes — fidelity, hacking, speed — and the combined line
"grade engines by their worst exploitable error, and quote speed only at a fixed accuracy", with imports from fuzzing,
metamorphic testing, the method of manufactured solutions, LINPACK/HPCG and MLPerf.

## Red team of the five points (honest)

1. **"Meta-benchmark" is not empty ground.** Fetched this week: GPUSimBench 2607.13059 (trick: run GPU simulators on the
   same inclined-plane and scaling scenes, compare outcome distributions to real ones, and measure how identical
   worlds diverge across batch slots and runs; excludes soft bodies); GPUPhysBench 2609.35639 (trick: give coding agents
   50 GPU-physics tasks and score pass rate and speed against expert code); RGBench 2511.06434 (trick: 6,000 garment
   meshes, a new cloth simulator, and a protocol that scores simulated garment dynamics against measured real ones);
   PBD-R 2603.14634 (trick: fix position-based dynamics with a momentum-conservation constraint and ship a
   solver-agnostic benchmark with analytical solutions); IcFuzz 2608.06088 (fuzzes Isaac Sim with stage-guided
   mutations — crashes, not physics); Policy-Aware Simulator Learning 2605.29032 (trick: train a learned simulator as a
   minimax game against an adversarial policy, with the worst-case policy dual to RL on the critic's one-step error);
   plus the earlier contact-solver comparison 2304.06372, Acosta RA-L 2022 and the 2024 cloth sim-to-real benchmark.
   Each measures one axis with its own protocol. What none has: one ruler across axes, evaluation along the states
   trained policies visit, an adaptive (optimizer-defined) exploitability, and a test of whether any of these metrics
   predicts transfer. That combination is the ground; "a benchmark of simulators" alone is a follow-up.
2. **Capital is low in GPUs and high in adoption.** The hidden cost of a benchmark is ports (every engine has its own
   scene format and its settings mean different things), version drift, and maintenance. A leaderboard Jacob maintains
   dies with his attention; a `pip install` test suite that engine teams run in CI survives. The ceiling is reached only
   if a third party (reviewers, leaderboard owners) demands the number — which needs a demonstrated consequence
   (Part II claim A below), not a suite.
3. **Obsolescence works differently here, and partly the same.** LLM test sets die by saturation and contamination
   because the subject learns the test. Engines do not learn, but (i) a reference engine used as truth is surpassed,
   (ii) scene suites go stale as task classes move (rigid → soft → fluid), (iii) engine teams tune to the suite
   (Goodhart), and (iv) the *policies* trained in engines do learn, so a fixed exploit list saturates exactly like a
   test set. What survives: procedures anchored to invariances and conservation (true forever), to reality (measured
   data), to convergence limits (Richardson, manufactured solutions), and to adversarial search with a stated budget
   (adaptive). What dies: fixed scenes graded against one engine, fixed exploit lists, thresholds in metres.
4. **Quantities, ranked by consumer value (judgment):** predictivity of transfer (does the simulator rank policies as
   reality does — the only number a robot-RL author needs) > exploitability (worst-case physical violation under a
   budgeted optimizer) > fidelity at matched speed (the MLPerf rule: time to a fixed accuracy) > resolution and
   determinism (gauge R&R, batch invariance — CL-W43-09) > hardware affinity (scaling, memory — GPUSimBench's ground)
   > portability cost (how hard a scene is to port; measurable with an agent). Add for differentiable engines:
   gradient fidelity. Add for randomization: whether the DR envelope covers reality's parameter posterior.
5. **AI agents, honestly.** Three roles are structural, one is decoration. Structural: (a) the adversary — exploitability
   is *defined* by an optimizer with a budget (RL, CEM, or gradients in differentiable engines); no learner, no metric;
   (b) the porting labor — a coding agent that translates a scene across engine formats (MJCF, USD, URDF, Genesis API)
   and proves equivalence with the metamorphic tests below; this is the benchmark's scalability bottleneck and a
   genuine MLsys contribution (GPUPhysBench and WorldSolver 2610.08720 show agents already write physics code);
   (c) test generation — agent-driven fuzzing for physics violations rather than crashes (IcFuzz is the crash version).
   Decoration: an LLM judging physical plausibility from trajectories or video; unvalidated, and a different target.
   The project is AI/MLsys-aligned through (a)–(c) and through its consumers (policies, synthetic data, world models),
   not by making the LLM the physicist.
6. **The ad-hoc fear is the right fear, and it has a known cure: the oracle problem.** Software testing faced "how do
   you test a program whose correct output you do not know" and answered with metamorphic relations, differential
   testing and property-based testing; computational science answered the same question with verification and
   validation (solving the equations right vs solving the right equations) and uncertainty quantification. The ruler
   below is those answers applied along the states policies visit.

## The ruler — four design rules, five functionals, two measures

**Rules.** R1 *dimensionless*: every quantity is normalised by the scene's own scales — an energy scale $E_0$ (actuator
work budget per step, or $m g \ell_0$), a length $\ell_0$ (smallest feature or contact radius), a force $F_0$ (weight of
the manipulated body); a threshold is a fraction, never a metre. R2 *oracle-free where possible, reality-anchored where
not*: no reference engine is truth. R3 *adaptive*: worst case under optimisation with a stated budget, reported as a
curve, never as a list. R4 *consumer-validated*: a functional is admitted into the ruler only after it predicts a
consumer outcome in a pre-registered test.

**Functionals along a trajectory $(x_t, u_t)$.** Let $E_t$ be the scene's mechanical energy (kinetic + potential +
elastic), $\Delta E_t = E_{t+1} - E_t$, $W_t^{\mathrm{act}}$ the actuator work in step $t$, and $W_t^{\mathrm{ext}}$ the
work of prescribed or kinematic bodies.

- Energy from nothing (work–energy bookkeeping; dissipation can only remove energy):

$$
\varepsilon^{E}_t = \frac{\max\!\big(0,\; \Delta E_t - W_t^{\mathrm{act}} - W_t^{\mathrm{ext}}\big)}{E_0}
$$

  Catches box-surfing, twitch-to-speed, penetration springs. Needs only energies and actuator torques, which every
  engine exposes; for soft bodies the elastic term needs the material model and nodal positions (a design task; PBD
  engines have no energy, which is itself a finding).
- Complementarity residual (non-penetration and friction cone), for contacts $i$ with gap $g_i$, normal force
  $\lambda_i$, tangential force $f_i$ and friction coefficient $\mu$:

$$
\varepsilon^{C}_t = \sum_i \left[ \frac{\max(0, -g_i)}{\ell_0}\,\frac{\lambda_i}{F_0}
  + \frac{\max\!\big(0,\; |f_i| - \mu \lambda_i\big)}{F_0} \right]
$$

  (the NCP violation of 2304.06372, made dimensionless and taken along visited states).
- Metamorphic defects, for a transformation $T$ in {translate, rotate, mirror, rescale units, permute bodies or batch
  slots, halve $\Delta t$ with doubled substeps}, where physics demands $S(Tx) = T\,S(x)$ for the step map $S$:

$$
\varepsilon^{M}_T = \frac{\lVert S(Tx) - T\,S(x) \rVert}{\ell_0}
$$

  Oracle-free. The batch-slot permutation defect is GPUSimBench's nondeterminism and CL-W43-09's floor.
- Convergence (verification), from three resolutions $h, 2h, 4h$ of the shipped setting ($\Delta t$ or solver budget),
  with $x_h$ the trajectory computed at resolution $h$:

$$
\hat p = \frac{\log\big(\lVert x_{2h} - x_{4h} \rVert / \lVert x_h - x_{2h} \rVert\big)}{\log 2},
\qquad
\varepsilon^{R} = \frac{\lVert x_h - x_{2h} \rVert}{(2^{\hat p} - 1)\,\ell_0}
$$

  Richardson's estimate of the discretisation error at the shipped setting; the order degrades at impacts, which is
  reported, not hidden. This is the "law" half of Part I done the standard way.
- Validation (reality-anchored): on public paired sim/real data, trajectory discrepancy at matched protocol, or
  outcome-level rank agreement κ with chance correction (CL-W43-02's instrument, which survives that claim's refutation).

**Two measures.** Write $\varepsilon_t$ for the sum of the functionals at step $t$ and $\tau$ for a trajectory. Fidelity
is their mean over motions a fixed protocol chose (demonstrations, trained policies $\pi_{\mathrm{ref}}$):

$$
F(S) = \mathbb{E}_{\tau \sim \pi_{\mathrm{ref}}}\Big[\sum_t \varepsilon_t\Big]
$$

Exploitability is their worst case over motions an optimiser chose, within the set $\Pi_B$ of policies reachable with
a budget $B$ of GPU-hours:

$$
X(S; B) = \max_{\pi \in \Pi_B} \; \mathbb{E}_{\tau \sim \pi}\Big[\sum_t \varepsilon_t\Big]
$$

reported as the curve of $X$ against $B$ — exploits per GPU-hour, the way fuzzers report crashes per CPU-hour. Reinforcement learning lives under the second measure. The
return-weighted version (how much task return is reachable only through violations) is what the 2×2 of Part I
estimates with a reference engine; the oracle-free version weights return by $\varepsilon_t$ along the trajectory and
must use the energy and complementarity functionals, not a count — the $\rho_{L5}$ lesson.

**Speed** is quoted only at a fixed accuracy (time to $\varepsilon^{R}$ or the validation error below a target), and **hardware affinity** is scaling,
memory, batch-permutation defect and the resolution floor.

## Claims this adds (thoughts until their kill searches run)

- **A — predictivity** (`CL-W43-J03`): *the fidelity scores engines report do not predict whether policies transfer;
  worst-case exploitable error under a fixed optimiser budget does.* The consequence that makes the ruler mandatory.
- **B — exploitability at matched speed** (`CL-W43-J04`): *at the settings they ship, physics engines differ in what a
  budgeted optimiser can extract from them by more than their fidelity scores differ, and speed claims reorder when
  quoted at a fixed accuracy.* The headline the non-rigid session reached, now with a ruler under it.
- Part I's H1 (exploitation by task class) and H3 (resolution floor) are instances of the same ruler on rigid contact.

## Judgment

Measurement, procedure-based, two material classes from the start (one rigid-contact task where Part I's assets exist;
one cloth task where fidelity is worst, real data exists — the 2024 cloth benchmark, RGBench — and GPUSimBench stopped).
The golden version needs claim A; without it the program is a proper idea for one community (simulator builders). The
agent layer is (a)–(c) above and nothing else. Risks named: adoption capital; limited real paired data (tens of
policy–sim–real triples in the public tables, enough for a first correlation, not for fine claims); the elastic-energy
term for soft bodies; adversarial search cost on non-differentiable engines (budget-normalise, start where gradients
exist); race flags on the GPUSimBench team (soft-body extension is the obvious next paper), NVIDIA (Newton validation)
and the Policy-Aware Simulator Learning group (the adversarial framing for learned simulators).


## Addendum 2026-10-24 — Jacob's critiques and the answers

**Incumbents, inspected (PDFs fetched 2026-10-24).** GPUSimBench 2607.13059: authors from Shanghai AI Laboratory, Nanyang
Technological University, Nanjing University (LAMDA) and two Moscow institutes; cs.RO, IEEE format. One real-matched
scene (a steel ball rolls down an incline into a cube array; final cube positions compared with a physical apparatus
at the distribution level), plus scalability scenes (free-falling cube arrays) and the run-to-run / inter-environment
nondeterminism measurement. Jacob's reading — one scene, a headline-claiming benchmark — is fair on scope; its one
durable datum is the nondeterminism measurement. GPUPhysBench 2609.35639: Georgia Institute of Technology (Bo Zhu's
group — a credible simulation lab); 50 tasks for *coding agents*, graded against "expert-optimized" references that
the paper says were produced by translating upstream code to CUDA with a model and then hand-optimising. It is not
an incumbent for a measurement of simulators at all; it is evidence that agents write physics code. Consequence for
us: both occupy *title space* ("benchmark" + "GPU simulators"), which bears on how a reviewer reads novelty, not on
substance — one more reason the headline must be a finding, never "a benchmark".

**Should we hand-pick quirks?** Not as the core; yes as a dated regression corpus appended to the suite, the way fuzzers
keep a crash corpus beside their property checks. The functionals are not quirks: they are conservation laws and the
engine's own constraint residuals. One correction to Part II that Jacob's objection forces: the complementarity
residual must be computed against the engine's *declared* contact model. MuJoCo's soft constraints permit penetration
by design, so penetration per se is not a violation there; the violation is inconsistency with the engine's own force
law at its shipped setting. The functionals measure *self-consistency* (verification), not conformity to an external
ideal.

**"Responsible makers already attend to these."** True at converged settings on simple scenes, and that near-zero
reading is itself a profile worth printing. The violations live elsewhere: (i) at shipped speed settings — a Newton
solve capped at one iteration is unconverged by construction, and the 2023 contact-solver comparison measured
non-converged PGS and NCP violations; (ii) at batch scale — GPUSimBench's divergence of identical worlds is a
permutation-symmetry violation in shipped engines; (iii) in soft bodies and self-collision — position-based engines
have no energy (PBD-R 2603.14634 had to add momentum conservation); (iv) under adversarial optimisation — SAPU's
interpenetration exploit in assembly (success 85–88% falling under 40% under strict evaluation). Each method is anchored
to one invariant and leaks on others: PBD exact on constraints, wrong on momentum and energy; capped Newton good on
energy, wrong on constraints; soft contact exact on its own law, soft on penetration. The ruler's value is printing all
the leaks on one scale — the profile — not catching a blatant bug.

**The adversary.** Jacob is right that a pass over a priori exploits persuades nobody. Exploitability is defined as the
optimal value of an auxiliary decision problem, approximated by a *portfolio* of optimisers under a budget, calibrated
on settings where exploits are known to exist:

- State $s_t$: the engine state. Action $a_t$: within the task's own actuator limits (no superhuman torques). Reward:
  $r_t = \varepsilon_t$, the violation sum of Part II. Horizon $H$: the task's. Nothing about the exploit is given.
- Optimisers at budget $B$ GPU-hours: sampling MPC / CEM over action sequences (engine-agnostic, GPU-parallel, no
  training — the natural fit for batched engines); PPO or SAC for long-horizon exploits; gradient ascent through the
  engine where it is differentiable (MJX, Warp, DaXBench). $X(S;B)$ is the best over the portfolio, the way fuzzing
  papers report the best of several fuzzers.
- Calibration: the portfolio must rediscover, unprompted, exploits known to exist — penetration exploits at one Newton
  iteration, cloth self-intersection with self-collision off, box-surfing — before any new reading is believed.
- Two readings, both reported: *capacity* (the adversary's $X$) and *realised* exploitation (violations along
  task-trained policies' own rollouts, and the 2×2 interaction where retraining is cheap). Capacity is the worst case;
  realised is what practitioners get.
- Every discovered exploit is kept as a trajectory with its violation profile — the dated regression corpus.

**The ceiling numbers.** The 0.6 / 0.25 / 0.1 beside floor / middle / ceiling are the operator's subjective
probabilities, labelled judgment per the scorecard rule, that an executed project reaches at least that scenario. They
are not calibrated estimates; they exist to force the three scenarios to be written with what each requires, and to be
moved by evidence (a kill search, a pilot).

**The two findings, elaborated.** Yes: the benchmark is the instrument; the paper's contributions are the findings.

*A. Does physics-prior violation predict bad transfer?* Units are (policy, simulator, task) triples with a measured real
success and a sim success — the public tables already in our records (R2S-Eval $n=20$, SimFoundry $n=25$, Kaedim's five
tasks, SIMPLER's policies). For each: fidelity $F$ along that policy's own sim rollouts; exploitability $X(B)$ of that
simulator–task; the 2×2 interaction where retraining is cheap. Outcome: the real–sim gap. Pre-registered three results:
expected (judgment) — $F$ weak, $X$ moderate; the field's assumption — fidelity suffices; belief-changing — $F$ near
zero correlation with transfer (the fidelity numbers engines report are uninformative) and $X$ strong. Stated limit:
the real–sim gap includes perception; this analysis measures the physics-attributable part, and a null is informative.

*B. Speed–fidelity becomes speed–exploitability.* Engines × settings grid; for each, wall-clock per step at batch $N$,
$F$ on fixed scenes, $X(B)$. Plot speed against $F$ (today's frontier) and against $X$; pre-registered: at least one
engine on the speed–fidelity frontier drops off the speed–exploitability frontier (its speed was bought with exploitable
shortcuts), or none does (then exploitability is fidelity in disguise — also a finding). Speed is also re-quoted at a
fixed accuracy (time to $\varepsilon^{R}$ below target), the MLPerf rule.


## Kill search of the concepts (2026-10-24) — `data/reports/2026-W43-kill-CL-W43-J03-J04.md`

Jacob's null hypothesis ("none of the framing or proxies is novel") tested with eight arXiv queries, five web searches
and twelve fetched abstracts. Verdicts: the **proxies are not novel** — NCP violation is the solver literature's own test
(2304.06372), metamorphic testing is routine for CPS and driving simulators, Richardson is textbook — and are recorded as
instrument, not claim. **Exploitability is an occupied word** (best-response value in game theory; model exploitation and
the simulation lemma in MBRL; preference reversal, 2605.15960; the adversarial objective for learned simulators,
2605.29032); the unoccupied piece is the oracle-free conservation-law reward applied by a calibrated budgeted optimiser
portfolio to engineered engines — a mechanism difference, so `CL-W43-J04` survives weakly. **The fidelity axis is
occupied by GAUGE** 2608.05948 (Aug 2026: 22 real-grounded task families across rigid, cable, textile and volumetric
materials; Isaac Sim, Genesis, Newton scored by trajectory error) — far stronger than GPUSimBench; the ruler's
validation layer uses GAUGE's numbers rather than competing. **Trace-free prediction of transfer has a precedent**,
RoboGauge 2602.00678 (Jan 2026: sim-to-sim robustness metrics predict a policy's transferability without hardware), and
Kadian 2019 (1912.06321) is the single-artifact datum that an engine exploit ruined predictivity (SRCC 0.18 → 0.844
after tuning). Not found: a simulator-level number tested as a predictor of transfer, or any test of whether GAUGE-type
fidelity predicts it. `CL-W43-J03` survives on that gap, **redesigned as a horse race** of trace-free predictors — GAUGE
fidelity, sim-to-sim robustness, Richardson error, $X(B)$ — against the public real outcomes, with power bounded by tens
of triples. **No hardware is required** for either claim; persuasion comes from adversary calibration and from predicting
public real outcomes; the hardware confirmation is owed from a lab position and the paper says so.


## Collaborator write-up (2026-10-24)

A self-contained document for collaborators, without this repository's vocabulary: "Grading the Simulators: A Meta-Benchmark for Physics Engines in Robot Learning" — https://claude.ai/artifact/GBSdR9Yz9X51d1X3ZXiwxJ (summary, incumbents, novelty verdicts, the ruler with formulas, the adversary, Findings A and B, agent roles, durability, risks, first steps, references).


---

# Part III — the collaborators' proposed pivot (2026-10-25)

Collaborators propose steering away from a benchmark of simulators toward (1) agent-driven acceleration of simulators as a
deployed stack, on the claim that simulators predate agents and are so poorly optimised that frontier coding agents can
deliver 10–100× by generic means (kernel fusion and the like), and (2) an aggregated non-rigid test suite ported from
incumbents plus frontier-model-synthesised scenes, hoped to become what people report. Both captured as `CL-W43-J05`
and `CL-W43-J06` (thoughts) with scorecards and $300 / $0 probes.

**On (1), evidence first.** Three independent 2025–26 measurements contradict the generic claim: GPUPhysBench (agents 100%
correct but ≥ 0.9× expert speed on only 22–36% of tasks; global solves 0.23–0.25×; collision detection < 0.5×; largest gaps
exactly in collision detection, constraint solving and iterative solvers — the hot paths of engines); KernelBench-Verified
(June 2026: best frontier model 0.88× geometric mean against PyTorch once TF32 baselines and hidden tests are used; the
1.43× of the old protocol was reward hacking); Sakana's AI CUDA Engineer (Feb 2025: claimed 100×, measured 3× slower,
evaluation exploited, walked back). What is true in the claim: agents now write correct GPU physics code; CPU-era
soft-body codebases (SOFA, Bullet soft bodies, old FleX) are far from the GPU frontier, and porting them gives 10–100× —
but that is the GPU-port gain the engine teams already harvested, and the result must beat Genesis/Newton/Warp on the
same scene to count. The structural danger: an agent rewarded for speed cuts physics (iterations, tolerances, collisions)
unless the correctness oracle forbids it — the ruler is that oracle, which is why the acceleration claim cannot be
evaluated without it. "Distrust of agents" is not the gap GPUPhysBench found; capability on irregular workloads is.

**On (2).** Dense and arriving monthly (SoftGym, DaXBench, GarmentLab, RoboVerse, MoDeSuite, WireCraft, SoftVTBench,
DLO-Lab, DeformX, RGBench, the 2023 cloth benchmark, GAUGE); RoboVerse already aggregates across simulators; scene
synthesis is crowded (EmbodiedGen V2, Code2Worlds-2, Gen2Physics, SimuScene, φ-Scene, Artisan) and synthesised soft-body
scenes carry no measured material behaviour. Adoption needs a reason to report that a union of existing tasks does not
supply. Worth doing only as the scene set the ruler and the acceleration oracle both need — ported by the agent
transpiler, which is the shared systems piece — not as the paper.

**Synthesis offered to the collaborators:** "agent-accelerated simulation, verified" — their deployed optimisation stack,
with speed quoted only at fixed accuracy and unchanged exploitability (the ruler as oracle), and the measurement paper
"what frontier agents can and cannot accelerate in physics engines under a physics oracle" (GPUPhysBench as baseline).
The two findings of Part II remain the headline science; the suite is their scene set.


---

# Part IV — the ruler as a training ingredient without becoming a reward (2026-10-30)

Jacob asked whether GRAFT — *Gradient Routing Localizes and Removes Unintended Behaviors in RL* (2610.17062, 12 Oct 2026;
trick: when a misspecified reward produces unintended behaviour and the monitor that flags it makes systematic errors,
do not penalise or filter flagged samples — that teaches the model to hack where the monitor cannot see — but route the
flagged samples' gradients into a sacrificial set of adapter parameters and ablate them at deployment) carries over to
simulator RL. It does, structurally: the imperfect monitor is our physics-violation ruler; penalise-or-filter is what the
robotics field does today (interpenetration filtering in SAPU, action-smoothness and Lipschitz penalties, domain
randomisation); ablation at deployment is sim-to-real transfer without fixing the simulator; and the in-engine return
lost by ablating the sacrificial branch is a *causal, policy-internal exploit share* that needs no converged reference —
so it exists for soft bodies, where the 2×2 does not. Captured as `CL-W44-J02` with a two-week, $50–100 probe on Leap and
Go1 (plain / penalty / filter / routed × DR, evaluated in the training engine, the converged engine and a second
engine, branch on and off). No application of gradient routing to robot policies or simulators exists in the fetched set.
Pre-registered death: nothing exploit-specific localised (ablation drop equal in training and converged engines), or no
transfer gain over DR and penalties.


---

# Part V — real-to-sim data synthesis with VLMs: seven questions, one claim (2026-11-03)

Jacob and a colleague raised seven questions about VLM-driven real-to-sim data-synthesis pipelines (Astra-era 3D
modelling). Evidence: 73 arXiv abstracts fetched by API, 8 pages (two maintained GitHub lists, the NVIDIA SimReady blog,
the Moonlake asset-evaluation post, a buyer's QA checklist, two AgiBot posts), one PDF (RSS 2020). Every paper below
carries its one-sentence trick in `data/reports/2026-W45-kill-CL-W45-J01.md` or here. One claim captured: `CL-W45-J01`.

## 1. "Per-scene physical calibration by a VLM-driven real robot is heavily adopted lately" — not supported

The maintained list `YanjieZe/agent-real2sim2real` holds 75 papers dated 2026-07-19 to 2026-10-16 (13 weeks). In the
27 "agent × real2sim2real" papers, **one** (D-World 2610.17114: LLM agents revise states and physical parameters after each
real action chunk on a dual-arm robot) clearly has an agent calibrate physics on a real robot; RoboSimStudio 2610.18835
(humans or coding agents edit solver, contact model and parameters against observed behaviour, in Newton) is a partial
fit. Of the 48 non-agent papers, about 16 identify physical parameters from real data without an agent — mostly
deformables, tactile sensors and actuators (ForceTwin, RealSimLoop, PneuTac, BoxTwin, Contact-UAN) — and about 24 are
geometry- or asset-only. The 30 public Astra demos (`zjwzcx/Awesome-Astra-Embodied-AI`) are zero-shot control (19),
real-to-sim *replay* (5) and RL-environment building (5); one caption mentions physical parameters.

What *is* adopted is assignment, not measurement: NVIDIA's SimReady pipeline (Oct 2026 blog, Astra as the frontier
model) sets friction to "assumed static 0.8, dynamic 0.6", mass "estimated from STEP geometry volumes", and says outright
"these parameters were not calibrated against physical YuMi measurements" and the tests "did not establish agreement with
real-world robot dynamics". The papers that do calibrate with a robot — 2601.08454 (a VLM names "the minimal subset of
missing physical parameters required for the simulation task" and a behaviour tree acquires them by contact), RigPI
2606.25212 (VLM-seeded differentiable identification of inertia and friction), Phys2Real 2510.11689 (VLM prior
distributions fused with online estimates), Vid2Sid 2602.19359 (a VLM diagnoses sim–real video mismatch and proposes
parameter updates) — chose tasks where a parameter is known to matter. Why it *looks* prevalent: the demos are vivid, and
the evaluation side of the field (next section) does calibrate, for a different reason.

## 2. Is calibration worth it against a material-prior database plus randomization?

The evidence splits by **task sensitivity**, which is the claim.

For measuring: 2606.22062 (June 2026, sim-to-sim pendulum, two hidden parameters) — "a small number of identification
rollouts closed most of the transfer gap ... broad randomization that contained the true system still did not substitute
for measurement"; Phys2Real — 100% vs 79% and 57% vs 23% over a DR baseline on CoM-offset pushing; ForceTwin — probed
door mechanisms give 87% goal completion against 60% from a VLM prior; 2503.01255 — leaving static joint friction out of
randomization broke transfer, and identification found "unexpectedly high friction-torque ratios".

For the prior plus breadth: Digital Cousins 2410.07408 — twins "are expensive to generate and cannot produce
cross-domain generalization"; the co-training recipe 2503.24361 — +38% real success "even with notable differences
between the simulation and real-world data"; MetaGenSim 2610.19479 — optimising the *generation distribution* "matches
expert manual alignment" with no alignment; InternData-A1 2511.16651 — synthetic-only pre-training matches the π
dataset; AutoRSR 2610.20336 — 73–87% real success from 1K randomized synthetic episodes per task; SIMPLER 2405.05941 —
sim–real correlation for evaluation "without needing to craft full-fidelity digital twins".

Reading, stated plainly: **twin for evaluation, cousin for training.** When the simulator must predict *this* scene's
outcome — policy evaluation (R2S-Eval 2609.03276, X2Real 2609.27449 with a 0.84 sim–real correlation after calibrating
visuals and physics, PolaRiS 2512.16881, RobotArena∞ 2510.23571, SureSim 2510.04354) and replay — per-scene calibration
is the point. When the simulator is a data source for training, breadth over the prior beats fidelity to one scene,
*except* where one parameter the prior cannot pin down flips the task outcome (centre of mass, spring mechanisms,
static joint friction, deformable stiffness). Nobody has measured which parameters those are, task by task, or how
concentrated the value is — that is `CL-W45-J01` (section 8).

## 3. Can sim-to-sim replace the real world for training or evaluating a VLM data synthesizer?

For the *physics* half, yes, and the field already does it: 2606.22062 used a hidden-parameter twin as the robot; TUCO
2610.05407 and the co-training mechanism study 2604.13645 evaluate sim-to-sim; Vid2Sid validates parameter recovery
sim2sim ("mean relative error under 13% vs 28–98%"). Two conditions. (i) The target must differ from the source in the
*structural* ways reality differs — contact model, actuator response, deformables — so cross-engine (MuJoCo → Newton or
IPC, rigid → soft) rather than same-engine with perturbed constants; otherwise the synthesizer learns one engine's
idiosyncrasies. This is exactly the engine-disagreement instrument of Part II. (ii) One real anchor per task family is
still owed to show the sim-to-sim ordering of synthesizers matches the real ordering (GAUGE's reality anchoring). For the
*appearance* half, no: the visual gap is what real-to-sim exists to close, and a synthesizer trained sim-to-sim learns no
camera.

## 4. Evaluating a data synthesizer: the transfer score is a two-sample test on coin flips

The common metric — fine-tune a VLA on the batch, measure real success, compare — is a difference of two binomial
proportions. With $n$ trials per arm and success $p$, the standard error of each arm is $\sqrt{p(1-p)/n}$: at $p = 0.5$
and $n = 50$ it is 7 points, the standard error of the *difference* is 10 points, and a 15-point gain is not
distinguishable from zero. The one study that got clean conclusions on what drives sim-to-real for VLAs (2603.22876)
ran over 10,000 real trials. Jacob's concern is correct and quantified; it is also stated knowledge in the evaluation
literature, so it is a finding here, not a claim (the W44 run killed the L1 "noise floor" set for the same reason).

The fixes exist in print and should be used, not reinvented: paired initial conditions across arms (common random
numbers — our luck/skill thread); SureSim 2510.04354 (Princeton IRoM: prediction-powered inference that uses many
simulated trials and a few paired real trials to bound real success, "saves 20–25% of hardware evaluation effort");
sequential comparison with near-optimal stopping 2503.10966 (same lab); CDF lower bounds from few rollouts 2405.05439;
VLM pairwise preference instead of binary success (R2S-Eval), which recovers the information binary success throws
away; a calibrated twin for *ranking* synthesizers (X2Real's 0.84).

## 5. Evaluating a batch of synthetic data: the principled metric exists, and the territory is dense

The right quantity is the batch's value to the consumer on the real target distribution — and that is what influence
functions estimate without a deployment per batch: CUPID 2506.19121 (Stanford/TRI: influence of each demonstration on
closed-loop return from a set of evaluation rollouts), QoQ 2603.09056 (influence on validation-demo loss), ATHENA
2606.16208 (billion-parameter VLAs, 313× faster influence), and **TUCO 2610.05407 (Oct 2026), which does exactly the
sim-demo-for-co-training case**: influence of each simulated demonstration on target-domain scoring rollouts,
decomposed into trajectory utility and set coverage. Learner-free proxies also exist: mutual information between states
and actions 2502.08623, signature-kernel entropy for diversity (FAKTUAL 2603.11634), power-spectral smoothness
2605.01544, state criticality under adversarial perturbation (SCRIM 2610.17709), self-supervised progress and
deduplication (SCIZOR 2505.22626), reusable-primitive structure (SIEVE 2607.06442). Eight metric papers in eighteen
months from Stanford, UT Austin, TRI and others: a new metric here is a race, not a gap.

A learner-free *absolute* quality number does not exist in principle — data value is relative to what is being learned
(Re-Mix 2408.14037: the best mixture depends on the training setup). What is unmeasured is **validity**: whether the
influence or proxy ranking of synthetic *batches* matches their transfer ranking. That is a meta-evaluation worth a probe
inside this program (it needs real transfer numbers or a calibrated-twin target), not a headline on its own.

## 6. How industry evaluates: assets by authoring checks, demonstrations by labels; transfer rarely

Asset vendors grade *assets*, not transfer. Moonlake's post (vendor blog, ten articulated assets) scores 22 metrics —
collision-proxy error, joints with explicit limits, friction authored rather than left at simulator default (Moonlake
36.8% of joints, Astra 58.1%), exported mass against the product reference, a button-press test — and states that the
metrics are "only a proxy for whether an asset improves robot learning", with correlation to training outcomes as future
work. NVIDIA's SimReady Foundation validation checks units, geometry, materials, rigid bodies, joints and drives, and the
blog says real-dynamics agreement was not established. Lightwheel assets serve as references in the Artisan benchmark
2610.13947 (spatial fidelity, physical plausibility, downstream task performance, overall quality).

Demonstration-data buyers and sellers grade *batches* by manifests (task, site, object, operator, outcome), calibration
versions, timestamp alignment, action semantics, success and failure labels, acceptance yield; AgiBot World keeps failed
episodes and labels `error_cause` and `restorable` rather than discarding them, and reports downstream policy gains
(GO-1) rather than QA metrics. The one buyer's checklist that recommends downstream validation says a batch without it
is "technically qualified, not performance-proven". So the industrial metric is structural QA plus labels; transfer is
measured rarely, late, and with the noise of section 4.

## 7. Training a scaled open VLM for sim-ready synthesis — the harness outlives the weights

Against: Agentic Real2Sim 2607.19190 reports that an *open-weight VLM backend at a small fraction of the cost of frontier
models* attains a comparable conversion success rate — the capability sits in the agentic harness, which survives a
model swap, not in the weights, which do not. The lane is already occupied by groups with data and compute:
3D-Generalist 2507.06484 (VLMs as policies that craft layout, materials, lighting and assets, trained by self-improvement;
Stanford, 2025), PhysX-Anything 2511.13648 (a VLM-based physical 3D generative model with a 193× token reduction and the
PhysX-Mobility dataset), SpatialLM 2506.07491, STABLE 2605.16137 (fine-tuned LLM plus a physics corrector). RECONSPATIAL
2611.02026 (1 Nov 2026) locates where frontier VLMs fail: metric accuracy — GPT-6 Astra scores 81.4% on relative structure
and 58.7% on metric scale; "relational consistency alone does not ensure metric accuracy". Metric errors are physical
errors: mass estimated from volume scales as $L^3$, so a 10% scale error is a 33% mass error, and penetration and support
failures follow (SimuScene 2606.03994 and φ-Scene 2606.21596 exist because of them). Jacob's durability concern is
supported; what survives a model generation is the verifier (SimReady validation, Moonlake's metrics, Artisan's
benchmark, RECONSPATIAL), the physics-in-the-loop check (SimuScene uses the engine "as a diagnostic measurement tool"),
and the data or prior (PhysX-Mobility, ABO masses). Recommendation: do not train the synthesizer; build what it is graded
by — the Part II position, again.

## 8. The claim this adds — `CL-W45-J01`

**Headline.** Only one or two numbers per scene are worth measuring, and which ones can be computed in simulation before
any robot time: the value of calibrating each physical parameter under a material prior is concentrated in task-specific
parameters, and for most tabletop tasks it is below the cost of measuring, so a material-prior database plus
randomization is the right default and targeted calibration the exception.

**Quantity.** Scene parameters $\theta = (\theta_1, \dots, \theta_d)$ with material prior $p(\theta)$; a policy $\pi$; success
$J(\pi, \theta)$ when deployed in a world with parameters $\theta$. The value of measuring parameter $k$ is the expected
value of perfect information (decision theory's term; Raiffa and Schlaifer 1961),

$$\mathrm{EVPI}_k = \mathbb{E}_{\theta_k}\Big[\max_\pi \mathbb{E}_{\theta_{-k} \mid \theta_k} J(\pi, \theta)\Big] - \max_\pi \mathbb{E}_{\theta} J(\pi, \theta),$$

with $\theta_{-k}$ all other parameters: the success gained by specialising the policy to the measured value, averaged
over what the measurement could return. Measure $k$ only if $\mathrm{EVPI}_k$ exceeds its measurement cost $c_k$ in robot
time. The cheap necessary condition is the Sobol index of the randomized policy's success,

$$S_k = \frac{\mathrm{Var}_{\theta_k}\big(\mathbb{E}[J(\pi_{\mathrm{DR}}, \theta) \mid \theta_k]\big)}{\mathrm{Var}_{\theta}\, J(\pi_{\mathrm{DR}}, \theta)},$$

the share of the randomized policy's scene-to-scene success variation that parameter $k$ explains; a parameter with
$S_k \approx 0$ cannot be worth measuring. This is the dependence toolkit of `CL-W44-J01` pointed at physical parameters.

**Estimator without retraining per parameter.** One policy per task conditioned on a masked parameter vector,
$\pi_u(a \mid s, \hat\theta)$, trained under the prior with random masks (a masked entry is replaced by its prior mean), so
every conditioning pattern is in-distribution. Then $\widehat{\mathrm{EVPI}}_k = J_k - J_0$, where $J_k$ is the success with
only $\theta_k$ revealed and $J_0$ with nothing revealed; $J_{\mathrm{all}} - J_0$ is the total; concentration is the top
parameter's share of the total.

**Pre-registered surprise, two-sided.** Total value under 5 success points on pick-and-place and peg insertion (the
collaborators' prior holds); 15–40 points on CoM-offset pushing and a spring-loaded drawer (the Phys2Real / ForceTwin
class); the top parameter above 60% of the total in at least five of six tasks. Dead if the value is spread (top under
35% in most tasks), if targeted calibration beats neither a widened prior nor full calibration at any budget, or if a
per-parameter value rule is found at full-text reading of 2606.22062, Liang–Saxena–Kroemer (RSS 2020) and AdaptSim.

**Kill search (concept, first pass, same day).** Survived: the concept "identify task-relevant parameters" is in print
(RSS 2020, implicit in a regret objective; AdaptSim 2302.04903, distribution adaptation; MetaGenSim, generation side); the
budget question was answered on a two-parameter pendulum (2606.22062) and left "which parameters" and structural
mismatch open in its own words; the per-parameter value, its concentration and a cost-side rule are unfound — the arXiv
conjunction (Sobol OR variance-based sensitivity OR value of information OR EVPI) AND (sim-to-real OR domain
randomization OR system identification) AND robot returns 0. Gate 2B flagged: the red team will say "friction and mass
matter most" is folklore; the answer is the pre-registered number, not the sentence. Princeton IRoM (Majumdar: AdaptSim,
SureSim, near-optimal stopping) owns the adjacent lineages — natural reviewer or collaborator, on campus.

**Scorecard** in the claim record and thread. Cost of the first probe: 40–60 GPU-h, $80–180, three weeks, no robot; the
lab position adds one real anchor (Phys2Real's public T-block task or a collaborator scene) — the one place the
collaborators' robot time is worth spending on this question. Relevance: collaborators and asset vendors direct; Jacob's
edge (variance decompositions, no robot) load-bearing; both advisor routes zero — robotics-flavoured, as Jacob said of
L5 on 2026-10-29.

## Judgment

The real-to-sim data-synthesis territory has three dense regions (scene and asset generation; data-value metrics;
evaluation statistics), each owned by groups with robots or compute, and one measurable gap at the join of the
calibrate-versus-randomize debate, which the agentic wave is spending robot time on without a rule. `CL-W45-J01` is that
gap. It is a measurement with a decision rule in the Part II register, solo-feasible in simulation, and its expected
result vindicates the collaborators' prior on most tasks while bounding it — a result either camp can use. It is not core
ML.
