Run the kill search for candidate $ARGUMENTS.

Read `prompts/03_kill.md`. Locate the candidate in `data/candidates/`. Search arXiv (API), Semantic Scholar (skip with
a degraded note if unavailable), the local conference-export index (`data/exports/` if built), and the complaint
stream. Every neighbor must come from a fetched abstract or page; record ids/URLs. Write the `kill_search` block into
the record, set `status` to the verdict, append a history entry. Print the verdict and its one-line reason.
