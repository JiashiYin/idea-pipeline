# Taste — what made an idea alive in the live sessions, and what killed the rest

Read before `/claims`, `/mutate`, `/capture`, `/discuss` and any sprint that generates. This file is the memory the
unattended runs lack: the judgment that came out of Jacob's live discussions with the operator (Oct 2026), written so
that a fresh session reasons the way those sessions did instead of filling templates. Every rule here was paid for by a
killed idea. Added to, never rewritten; dated.

## 1. What a claim is for

A claim is a sentence about the world, not about our method: "engines trade physics for speed and policies exploit
it", "temperature-0 variance is the serving stack's arithmetic", "scaffold gains are effort and restarts". If the
sentence names our instrument instead of a fact, it is a probe wearing a claim's clothes. If a stranger would not
repeat it at lunch, it is not clear yet. If it needs a second sentence, it is two claims or none.

## 2. Where the live ideas came from (2026-10-08 → 10-20)

- **A conservation law or identity that reorganises a messy quantity.** The per-turn variance split began as
  $\mathrm{Var}[R] = p(1-p) = \sum_k \mathbb{E}[D_k^2]$, with $p$ the task's root success probability and $D_k$ the change
  in the value process $V(h_k) = \mathbb{E}[R \mid h_k]$ at move $k$. Signal versus headroom at a compaction node:
  $C(h) = \mathrm{Var}_\sigma[V(h,\sigma)]$ (how much the summary $\sigma$ moves the value) against
  $H(h) = V_{\mathrm{full}} - \mathbb{E}_\sigma V$ (what the best summary leaves on the table). An identity a
  stranger can check on a napkin outranks a pipeline diagram.
- **An identifiability question asked before any method.** "Random *given what*?" "Whose temperature?" "A seed is
  not a state of the world." The strongest moves were finding that a quantity people report is a property of the
  protocol, not of the thing: temperature-0 "determinism" that is batch arithmetic; a luck term that is identically
  zero in a deterministic sandbox; a group whose identical rewards give zero advantages by construction.
- **The field's own words as the pressure point.** A meta-paper declining an axis because convergence is
  non-monotone; a model file annotated "modified for performance"; a lab post that proves reproducibility and stops
  before evaluation. The gap is what they wrote down and did not do.
- **Measurement with a recipe consequence, lab-adjacent.** A ruler that grades shipped artifacts first — a leaderboard
  column, a default cap, a reported variance — and tells a named consumer which of two recipes to use. Not a new
  simulator, not a new estimator evaluated on one benchmark, not a frontier recipe fight from a solo position.
- **Cross-field imports said plainly.** Kalman innovations to whiten an audit residual; gauge repeatability and
  reproducibility for engines; attenuation and chance agreement for real-to-sim agreement; survival hazards for agent
  horizons. The import earns its place only when the mapping is written in two plain sentences and names the source
  field's term.
- **Three scenarios with probabilities, the cheapest killing step, the pre-registered surprise.** Always, before
  anything else is said.

## 3. What killed ideas, in the order it happened

- **Framing chosen for an audience** (an "RSI flavour" added to a compaction agent so it would attract readers): the
  mechanism did not need the frame, the frame did not survive the kill search, and the time was lost. Framing is not a
  claim. (2026-10-14)
- **A premise that was our own error**: "raw history is a ceiling" for a compaction agent; the Reflector at
  temperature 0 made the measured signal a protocol artifact; signal starvation posed and answered in print. The kill
  search found three papers each closing one door. Premise hygiene is Gate 0 for a reason. (2026-10-16)
- **Probes that are footnotes**: a control one paper skipped, an audit of one critic. True, useful, not news. The
  claims layer exists because seventeen such probes read as nothing. (2026-10-19)
- **A degenerate null**: a shuffle that any monotone curve beats; a placebo that cannot fire on an all-failed set. If
  the null is beaten by linear decay, the test measures nothing. (C-W43-01, 2026-10-20)
- **An estimator that does not estimate the named quantity**: $\rho_{L5}$ counted reward on threshold-crossing steps when the
  return gap is a signed, value-weighted sum of one-step errors; the 2×2 train-in-each / test-in-both matrix was the
  estimator and was cheaper. Write the quantity's definition, then ask whether the probe computes it. (C-W43-15)
- **A "surprise" that equals the field's stated knowledge**: the per-state convergence law was the engine manual's own
  description; "mostly the agent" was the benchmark owners' assumption. A ruler whose expected reading matches what
  everyone already believes is a service, not a paper (Gate 2B). (C-W43-15; τ-bench split, 2026-10-14)
- **Vocabulary blind spots in the kill search**: Probe-and-Resume (critics at chance early in a trajectory) was in
  print five days before our search and was missed because the lane's queries said "credit assignment, process reward"
  and the paper said "critic, intermediate states, continuation pass rate". Search in the neighbours' words, not ours.
- **"Most" and "silent" in a headline** without a table: the first three real tables made "most" false (29–37%). A
  quantifier is a pre-registered number or it is not in the sentence. (C-W43-13)
- **Research-tool landscapes mistaken for kill searches**: a tool said "wide open"; the arXiv count said 39 papers and
  a benchmark the week before. Density is measured on the day of writing, by us.

## 4. Jacob's stated taste (apply, do not argue)

Headlines over scopes; the plain one-sentence trick for every paper; equations with every symbol when depth is
needed, written in LaTeX (`$...$`, `$$...$$`) and never in Unicode math (Jacob, 2026-10-24: Unicode math is hard to
read), each display equation short and self-contained; no hedging words; the scorecard every time; cross-field connections he may lack the background to see, said
plainly; on radar but not head-to-head with frontier labs; academic value plus a shippable artifact (an instrument,
a standard, a definitive comparison); measurement and benchmark work is where the heavy hitters are; a result rather
than a reading is the point of the first year. His background is computer engineering and theoretical physics —
numerics, GPUs, identities, limits — and never anything else.

## 5. How to generate so the distribution is his and not the cards'

Two passes, always, and the record says which produced each claim (`origin`):
- **Top-down (`origin: top-down`)**: for each live lane and each scout theme, before looking at any probe, write the
  one sentence that would be news if true — from the lane sentence, this month's pressure points, the field's own
  stated assumptions, and §2 above. Then look for probes, existing or new. A claim with no probe is a thought and is
  queued for `/sprint generate`.
- **Bottom-up (`origin: bottom-up`)**: from cards through the mutation operators to probes, then lift three probes
  on one theme into a claim. Operators are prompts for thinking, not templates: no candidate is written whose
  headline would not be news.
- **Chat (`origin: chat`)**: what Jacob and the operator found in a live session, captured within one reply.
The scoreboard reports survival through kill search and red team by origin, so the generator that earns its keep is
visible and the one that does not is cut.
