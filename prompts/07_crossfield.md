# Stage 7 — Cross-field import

Purpose: produce seeds that harvesting cannot. Every other generator reads what the lane has already
written and therefore proposes on-radar ideas; this stage carries another field's standard answer into
one of our problem shapes. The one surviving insight of October 2026 (a seed is not a state of the world;
the per-move luck/skill split) was an import from game analysis into variance attribution.

Inputs: `config/fields.yaml` (shapes × fields), `config/themes.yaml` (lanes), `data/crossfield/log.jsonl`
(pairs already done; do not repeat a pair within 6 months), `config/standards.md`.

## Procedure (weekly; 2 shapes × 2 fields = 4 imports)

1. Pick pairs. Prefer the suggested pairs in `fields.yaml` not yet logged; otherwise round-robin. Weight fields
   F1–F5, F9, F11 (Jacob can evaluate them). Record the pick and the reason in the log.
2. For each pair, fetch the field's standard answer from its own literature (textbook chapter, review, or the
   canonical paper — fetched, not recalled; one or two sources, cited). Write it in plain words in three
   sentences a stranger could repeat.
3. Carry it across. Write, in this order:
   - **The import in one sentence**: "In <field>, <problem shape> is solved by <standard answer>; carried into
     <lane>, that says <concrete statement about agents>."
   - **What it predicts**: one measurable statement about agents that would be true if the import holds and
     false otherwise. Pre-register the surprise: our expected result, the field's assumption, the result that
     would change a belief or a ruler (standards Gate 2, route B).
   - **Identifiability check**: random given what; whose temperature; is the imported quantity a property of the
     agent system or of the protocol (standards Gate 0).
   - **The cheapest probe**: cost in GPU-hours or dollars and days; the kill result written now (Gate 1).
   - **Who consumes it**: three consumer classes and the action each would change (Gate 3).
   - **Nearest existing use**: one arXiv API query with the field's own words AND the lane's words; name the two
     closest papers (fetched) and what they did not do. If the import is already made, say so and stop; a
     repeated import is still logged so the pair is not retried.
4. File each import as a seed in `data/seeds/<week>.jsonl` with `stream: import`, `source: import`,
   `shape`, `field`, `lane`, `position: solo|lab|both`, and the six fields above; status `proposed`.
5. Append to `data/crossfield/log.jsonl`: `{week, shape, field, outcome: filed|already-made|no-import, seed_id}`.

## Rules

Fetch the field's answer; never paraphrase a field from memory. Plain words, every term glossed on first use.
No method proposals beyond the import sentence and the probe; the mutate and kill stages do the rest. An import
that only renames a known agent result in the other field's vocabulary is `no-import`; say so. Four imports a
week, no more: quality beats coverage.
