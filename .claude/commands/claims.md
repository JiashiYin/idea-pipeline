Run stage 11 (claims — the headline layer) for ISO week $ARGUMENTS.

Read `prompts/11_claims.md`, `config/themes.yaml`, `config/standards.md`, `data/claims/claims.jsonl`, this week's
candidates and import seeds, and the latest pressure-points report. Attach every new candidate to a claim or mark it
orphan; write new claims (<= 2 per lane, >= 1 open per live lane) in the record format; grade each against the gates,
naming the failing gate; rank. Append to `data/claims/claims.jsonl` (append-only; status changes as new records with
history). Print one line per open claim: id, lane, headline, number of probes, cheapest probe cost, failing gate if any.
