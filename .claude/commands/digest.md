Write the weekly digest for ISO week $ARGUMENTS.

Read `prompts/10_digest.md` and `config/generation.yaml`. Build every section from the files in `data/` (seeds,
cards, candidates, crossfield log, pressure records, reports, checklist), never from memory of the run. Write
`data/digests/$ARGUMENTS.md` (≤ 600 words, tables over prose). Append the week's counts to `ledger/scoreboard.jsonl`.
Then commit and push (CLAUDE.md rule 10). Reply with the digest's first table and the ≤ 3 decisions only Jacob can make.
