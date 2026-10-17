# Stage 8 — Owned-artifact prospecting (position-aware generation)

Purpose: build the lab-position portfolio before Jacob is in a lab, and the entry-ticket questions for the
advisor conversations. An owned artifact (a benchmark, a harness, a leaderboard's logs, a serving stack, a
model series) generates questions only its owner can answer cheaply; from the solo position those questions
are parked, from the owner's position they are a two-week measurement. The per-turn τ-bench attribution
question came from this logic by accident; this stage does it on purpose, monthly.

Inputs: `config/labs.yaml` (tiers: campus, problem-setters, infra-builders, measurers), `config/themes.yaml`,
`config/standards.md`, the pressure records in `data/pressure/`, the parked items in `data/candidates/`.

## Procedure (monthly; one artifact per target group, ≤ 6 artifacts)

1. For each target group (campus tier first: Narasimhan — τ-family, hyper-τ, Odysseus/EasyPPO stacks; Narayanan
   — HAL; Netravali / Lloyd / Tri Dao — rollout and serving stacks; then problem-setters and measurers), name
   the artifact and fetch its current state: latest version, release cadence, what its logs contain (field
   names), what its papers' limitation sections say is uncharacterized (quote verbatim).
2. List the questions only the owner can answer cheaply. For each: the question as a paper title; the data
   field or configuration that makes it owner-only (API simulator config, unreleased logs, repeated trials
   the leaderboard does not run, serving stack); the first measurement and its cost *for the owner*; the
   pre-registered surprise (ours, theirs, the belief-changing result); the adoption surface.
3. Check that nobody outside has already done it from public data (arXiv API, role words), and that the owner
   has not published it (their own papers and blog, fetched).
4. Write the entry-ticket version: the one-paragraph question Jacob could put to the owner in person, in the
   form "your artifact can answer X; the obvious design fails because Y; the identifiable design is Z; do you
   want it, and is anyone doing it?" — a finding or an argument, never a pitch.
5. File each as a candidate in `data/candidates/<week>.jsonl` with `source: owned`, `position: lab`,
   `owner`, `artifact`, `status: parked`, `reopen_trigger: "access to <artifact> or a stated need from <owner>"`,
   and the entry-ticket paragraph. Append to `data/owned/<group>.md` so the portfolio per group accumulates.

## Rules

Fetch; verbatim quotes; the owner's own limitation text decides what is open. Never claim an owner has not
done something internally — write "not published" and the re-open test is asking. Three to five questions per
artifact; the portfolio for a group should fit on one page, because that page is what Jacob walks in with.
