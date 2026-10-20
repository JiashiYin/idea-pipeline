Apply Jacob's marks and answer his questions from the `## Jacob` sections of the thread notes.

`git pull --rebase origin main`, then `python scripts/threads.py --inbox`. For each thread listed: a mark (`promote`,
`jacob-dropped`, `park: <reason>`) is applied to the claim record and, where it names one, the probe record, as a new
status with a dated history entry (append-only; a claim record is updated by appending a new version record with
`supersedes`); a question is answered with evidence in a dated history line on the claim record so it appears in the
thread's Log — fetch before you answer, never from memory; a correction is applied to the record it concerns. Then
`python scripts/threads.py --mark-applied <ids>` and `python scripts/threads.py`, commit (`<week>: inbox — <one line>`)
and push. Print one line per thread: id, what was applied or answered.
