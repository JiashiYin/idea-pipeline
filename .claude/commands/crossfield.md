Run stage 7 (cross-field import) for ISO week $ARGUMENTS.

Read `prompts/07_crossfield.md`, `config/fields.yaml`, `config/themes.yaml`, `config/standards.md` and
`data/crossfield/log.jsonl`. Pick 2 shapes × 2 fields not logged in the last 6 months (prefer the suggested pairs;
weight F1–F5, F9, F11). Run the four imports as parallel subagents, each fetching the field's standard answer from
its own literature and the two closest agent papers from the arXiv API, each returning the six fields the prompt
specifies. File each as a seed in `data/seeds/$ARGUMENTS.jsonl` with `stream: import`, `source: import`, and append
to `data/crossfield/log.jsonl`. Print one line per import: shape × field → filed | already-made | no-import, and
the import sentence.
