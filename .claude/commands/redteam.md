Red-team candidate $ARGUMENTS.

Read `prompts/04_redteam.md` and `prompts/checklist.md`. Run the three personas as parallel subagents, each returning
objections with evidence; merge; run the checklist; let the generator answer; iterate up to 3 rounds. Write the
`redteam` block into the record, set `status`, append history. Print the verdict, the number of objections, and how
many were conceded.
