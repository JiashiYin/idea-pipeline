Triage the seeds for ISO week $ARGUMENTS.

Read `config/themes.yaml`, then `prompts/00_triage.md`, then `data/seeds/$ARGUMENTS.jsonl`. Process in batches of 10,
dispatching batches to parallel subagents when more than 20 seeds are new. Write `status`, `theme_fit` and
`triage_reason` back into each record and append a history entry `{date, status, note: "triage"}`. Print one line:
kept / dropped counts and the kept ids.
