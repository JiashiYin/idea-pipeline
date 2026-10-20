Refresh the thread note(s) for $ARGUMENTS (a claim id, or `all`).

Read `prompts/12_thread.md`. First read the `## Jacob` section of each affected `data/threads/*/THREAD.md` and apply
any marks to the records (history entry), answering questions in the Log. Then run `python scripts/threads.py
$ARGUMENTS` (omit the argument for all) and enrich the kill-search, red-team, first-steps and decisions content by
writing it into the records, then regenerate once more. Commit and push. Print one line per thread: id, status,
cheapest probe, failing gate, and whether a Jacob mark was applied.
