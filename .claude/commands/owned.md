Run stage 8 (owned-artifact prospecting) for ISO week $ARGUMENTS.

Read `prompts/08_owned_artifact.md`, `config/labs.yaml`, `config/themes.yaml`, `config/standards.md` and the parked
items in `data/candidates/`. One subagent per target group (campus tier first; ≤ 6 artifacts), each fetching the
artifact's current state and its papers' limitation text, listing 3–5 owner-only questions with the entry-ticket
paragraph. File each as a candidate with `source: owned`, `position: lab`, `status: parked` and a `reopen_trigger`;
append the group's page to `data/owned/<group>.md`. Print one line per artifact: owner, artifact, number of
questions, the strongest entry-ticket sentence.
