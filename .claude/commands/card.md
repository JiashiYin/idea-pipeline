Write the trick card for seed $ARGUMENTS.

Read `prompts/01_trick_card.md` and `schemas/card.schema.json`. Fetch the abstract from
`https://export.arxiv.org/api/query?id_list=$ARGUMENTS` and the full text from `https://arxiv.org/html/$ARGUMENTS`
when it exists. Write `data/cards/$ARGUMENTS.json`, schema-valid, with `evidence_level` set honestly. Append any
`limitations_as_complaints` as complaint seeds to this week's seeds file with `stream: paper-limitations`.
Print the `trick` sentence and nothing else.
