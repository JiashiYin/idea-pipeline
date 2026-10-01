# Stage 6 — Report

You are writing the report for a red-teamed candidate, following `schemas/report.md` exactly: eight
sections, fixed order, section 8 is the only part Jacob must think about and is capped at three items.
Strong model.

Style rules (violations are protocol bugs):
- Plain words. Any term a first-year PhD student new to the field might not know gets a gloss on first use.
- Every paper named gets its one-sentence trick, mechanism only. No paper is a bare name.
- Equations where a method is explained: every symbol defined, no prose paraphrase of math.
- Banned: "may", "could potentially", "it is possible that", "novel", "framework", "leverage".
  State what the evidence supports and give the uncertainty a number or a missing experiment.
- Sentences under 25 words where possible. Paragraphs ≤ 3 sentences. Bullets only for parallel items.
- The report must be readable in under ten minutes. If it is longer than two pages, cut sections 3 and 6
  to tables.

Section 8, "Decisions only Jacob can make": at most three. Each is a question with the options and what
each option costs or forecloses. Not "should we proceed" — that is the report's job to argue. Typical
legitimate decisions: which of two themes this serves; whether to spend the killing experiment's GPU-hours
now or after another result; whether to contact a named person.

After writing, re-read as Jacob: anything you had to re-read twice outside section 8 is a bug. Fix it,
then add the confusion to `prompts/checklist.md` under "Readability" with today's date.
