Write the report for candidate $ARGUMENTS.

Read `prompts/05_report.md` and `schemas/report.md`. The candidate must have status `red-teamed`; otherwise stop and
say so. Write `data/reports/$ARGUMENTS.md`, set `report_path` and `status: reported`, append history. Re-read the
report as Jacob; fix anything that needs a second read; add the confusion to `prompts/checklist.md` under Readability
with today's date. Print only section 8.
