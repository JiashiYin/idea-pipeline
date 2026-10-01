Generate candidates from card $ARGUMENTS.

Read `prompts/02_mutate.md`, `config/themes.yaml` and `data/cards/$ARGUMENTS.json`. Write at most 4 candidates to
this week's `data/candidates/<week>.jsonl` with status `proposed`; compute `cid` as specified in
`schemas/candidate.schema.json` (or call `python scripts/orchestrate.py cid` when it exists) and skip any cid already
present anywhere in `data/candidates/`. Print one line per candidate: cid, operator, claim.
