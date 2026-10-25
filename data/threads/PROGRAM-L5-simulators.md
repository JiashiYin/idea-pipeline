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
