Run stage 6 (pressure-point review) for the given ISO week. Read `prompts/06_pressure.md` first.

Launch three harvest agents in parallel — (a) frontier-lab system cards, launch posts and technical reports
from the last 12 months; (b) agentic benchmarks and leaderboards with their validity debates; (c) meta and
position papers plus industry engineering blogs that ask field-level questions — each writing
`data/pressure/<week>/<group>.jsonl` in the record format of the prompt. Then run one synthesis agent to
write `data/reports/<week>-pressure-points.md`, then one red-team agent on the top three to write
`data/reports/<week>-pressure-redteam.md`. Append the week's checklist lessons to `prompts/checklist.md`.
Reply to Jacob with the ranked pressure points, the questions they suggest, and the red-team verdicts —
nothing is called a candidate before the red team.
