# Owned-artifact portfolio — engine builders for L5: NVIDIA Newton / MuJoCo Warp (Google DeepMind + NVIDIA)

Entry-ticket questions for the engine-builder conversation. Each question is owner-only because of a named data field or
configuration; "not published" is the strongest statement made about the owner. Stage 8, monthly.

## 2026-W44

**Artifact state (fetched 2026-11-02).** MuJoCo Warp `3.17.0` on main ("maintained by Google DeepMind and NVIDIA as part
of the Newton project"); Newton `1.7.0` released 2026-10-14, monthly minor releases since `1.1.0` (2026-04-13), `1.8.0.dev0`
on main. Shipped solver defaults: Newton's `SolverMuJoCo` custom attributes `iterations` default 100, `ls_iterations`
default 50 ("MuJoCo's default"); the nightly G1 model ships `<option iterations="10" ls_iterations="20" timestep="0.005"
integrator="implicitfast">`, "derived from mjlab", and its benchmark entries set `"override": "opt.warn_overflow=
~ITERATIONS|~LS_ITERATIONS"` (the cap-hit warning off). Per-world Data fields: `solver_niter (nworld,)`, `overflow
(nworld,)` with `ITERATIONS: solver iteration limit reached`, `LS_ITERATIONS: linesearch iteration limit reached`;
`types.py` comment "`# unsupported: OVERRIDE, FWDINV, ISLAND, DIAGEXACT`" (the forward/inverse consistency certificate is
not on the GPU engine). Solver loop (`solver.py`): `wp.capture_while(nsolving, …)` — "it counts the number of worlds that
are not converged, it becomes 0 when all worlds are converged"; `_solve_done` marks a world done on
`alpha == 0 or 0 < improvement < tol or gradient < tol or model_improvement < tol`, or at the cap, where it sets the
overflow bit and (if not silenced) prints "solver iterations limit reached - please increase iterations". Nightly suite
(`google-deepmind.github.io/mujoco_warp/nightly/`, RTX 6000 Ada 48 GB): 18 scenes, per-night JSONL `{commit, timestamp,
jit_duration, run_time, steps_per_second, converged_worlds, model_memory, data_memory, total_memory, ncon_mean, ncon_p95,
nefc_mean, nefc_p95, solver_niter_mean, solver_niter_p95, step, step.forward.solve, …}`; `run.py` invokes
`mjwarp-testspeed --measure_solver=true --measure_alloc=true --event_trace=true`, which collects `d.solver_niter` for every
world and step and reports mean / p95 only. Latest entries (2026-09-03 on the fetched page): unitree_g1_flat 8192 worlds,
2.55M steps/s, niter mean 3.01 / p95 5, solve 205 of 390 ns per step; g1_hfield 1.68M, 3.24 / 6, 218 of 590; three_humanoids
1.09M, 2.67 / 5, 626 of 915; aloha_clutter 2048 worlds, 2.68 / 6; aloha_cloth 32 worlds, 34.3 / 62; franka 1.02 / 1.
Tuning page, verbatim: "Reducing MJWarp's settings `Option.iterations` and/or `Option.ls_iterations` limits may improve
performance and should be secondary considerations"; "Reducing these limits too much may prevent the constraint solver from
converging and can lead to inaccurate or unstable simulation"; "With MJWarp, in contrast, once all worlds have converged
the solver can early exit and avoid unnecessary computation. As a result, the values of these settings have comparatively
less impact on performance." Newton changelog: a `deterministic` constructor argument on `SolverMuJoCo` and others ("the
default inherits `wp.config.deterministic`"), repeated non-determinism fixes in contact ordering.

**Q1 (strongest; candidate C-W44-OWN-4; claim CL-W43-01, L5 kill test #2).** *How much of the batched Newton solve is
waiting for the slowest world.* Owner-only: the per-world `solver_niter` arrays the nightly collects but does not publish,
the silenced `overflow & ITERATIONS` bits, the replay controls, and the loop itself. First measurement: the wait share
$W = 1 - \frac{\sum_s \sum_w n_{s,w}}{\sum_s N \max_w n_{s,w}}$ ($n_{s,w}$ iterations of world $w$ at step $s$, $N$ worlds),
the per-step histogram and cap-hit share across the 18 scenes — about 1 GPU-hour, one day; then a compacted launch over the
unconverged-world list, checked bit-for-bit, timed on g1_hfield and three_humanoids — one engineer-week. Surprise — ours:
$W \ge 0.4$ on g1_hfield and aloha_clutter, cap 10 hit by 0.5–3% of worlds per step, solve time -30% (at least 10% of step time);
theirs: early exit read batch-wide, "comparatively less impact"; belief-changing: two nightly columns and a Newton change,
or the scheduler retired on this engine and attention moved to contact-rich manipulation. Adoption: the nightly page,
Newton's SolverMuJoCo, mjlab / Isaac Lab / Playground configs. Density (arXiv API, role words): 0 on every straggler /
iteration-cap / RL-transfer query; nearest GPUSimBench 2607.13059, GPUPhysBench 2609.35639, mjlab 2601.22074, ComFree-Sim
2603.12185. Not published by the owner.

**Q2 (CL-W43-01).** *Which worlds hit the cap, and what is their physics?* Export the exit certificate per world beside
`solver_niter`; relate capped steps on G1 to contacts and impact phase; re-simulate them at cap 100. about 2 GPU-hours.
Surprise: capped steps cluster at impacts and carry most of the cap-10-versus-100 one-step error, in < 5% of steps.

**Q3 (CL-W43-J03).** *Forward-inverse consistency on the GPU* (`FWDINV` unsupported): a batched residual published per
scene on the nightly; engineer-days. Surprise: the residual tracks the cap-hit share and nothing in throughput.

**Q4 (CL-W43-09; owner-cheap).** *The batch-nondeterminism floor per scene:* identical seeds twice, `deterministic` on
and off, per-world divergence after 1,000 steps and the throughput cost; about 1 GPU-hour. Surprise: determinism costs < 10%
on locomotion and the divergence without it exceeds reported policy gains.

**Q5 (CL-W43-01; solo-doable).** *The nightly history as a physics-regression log:* 250 nights x18 scenes of
`solver_niter_mean` / p95 against commit, from the public JSONL (fetched); half a day. Surprise: a commit that shifted a
contact-rich scene's iteration count by > 20% with no fidelity note.

**Entry ticket (Q1).** Your nightly already records how many Newton iterations each of the 8,192 worlds needed per step
and publishes the mean and p95; it can answer how much of `step.forward.solve` is launched work on worlds that had already
converged, because the loop runs until the last world is done. The obvious design, lower the iteration cap and time it,
fails because it changes the physics and the waiting at once, which is why the docs can say the setting has little effect.
The identifiable design is the wait share from the recorded per-world counts, the cap-hit share from the overflow bit your
G1 entries silence, and a compacted launch over the unconverged-world list checked bit-for-bit against the current loop:
about one GPU-hour for the numbers, a week for the prototype. Pre-registered: we expect a wait share above 0.4 on
g1_hfield and aloha_clutter and a 30% cut in solve time; the docs read early exit as batch-wide. Do you want it, and is
anyone doing it?

Solo entry point before asking: Q5 from the public JSONL, and a per-world histogram on any NVIDIA GPU (about 1 GPU-hour),
which bounds $W$. Records: `C-W44-OWN-4`.
