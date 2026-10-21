# Program note — L5, the simulator thread (shaped 2026-10-21 with Jacob)

A lane-level note, above the per-claim threads it links. The claims are graded one by one; this page says what they add
up to, which shape was chosen and why, and what the operator's judgment is. Rewritten when the shape changes; dated.

## The question Jacob asked

Is this work a **systems stack** (an iteration-level scheduler for batched contact solvers) or a **measurement** of
physical simulators used to train agents? He leans measurement and benchmarking, with several results at once — a
surprising measurement about exploitation among them.

## The shape chosen: one instrument, three headlines, the systems piece as a consequence

**The instrument — the simulator-budget 2×2.** Train a policy at the shipped solver budget and at the converged budget
under the full training protocol (domain randomization, kicks, noise), at matched wall-clock; evaluate every policy in
both engines with paired draws. Write J_e(π) for the return of policy π evaluated in engine e. The exploit is the
interaction term:

  X = [J_conv(π_conv) − J_conv(π_cap)] − [J_cap(π_conv) − J_cap(π_cap)]

(what the converged engine takes away from the cap-trained policy beyond what it takes from any policy). Alongside it:
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
