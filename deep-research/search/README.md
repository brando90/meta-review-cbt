# Search yield log

`europepmc_counts.py` runs the review's ten search strings against Europe PMC and prints the hit count for each (title/abstract fields; review-type filter where marked). `counts-YYYY-MM-DD.tsv` holds the output of each run, including the exact query.

**What this is.** The yield of a reproducible search, the first step toward the PRISMA-style umbrella search listed in `review/open_questions.md`. No screening has been done on these hits.

**What this is not.** The roughly 300 sources in `sources/` were found by targeted search and reference-list chasing, not by screening these hit lists. The counts show how much literature sits behind each slice (for example 27 reviews on CBT for adult ADHD against 1,309 hits for anxiety CBT reviews), and where the argument's key question is nearly empty: 9 hits for ADHD + executive function + CBT + moderator/outcome, 42 for executive function as a moderator of psychotherapy outcome.

| Run | Note |
|---|---|
| 2026-10-21 | First run. Europe PMC treats `"cognitive behavio*"` as a literal phrase, so the first attempt returned zeros for the CBT/ADHD slices; the final strings spell out the four CBT variants. Counts change daily. |

**Next step.** Screen D2 (27 reviews) and E1 (9) by title/abstract against the inclusion criteria in `../protocol.md`, record include/exclude with reasons, and compare with the 300 already in `sources/` to see what the targeted search missed.
