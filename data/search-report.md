# Europe PMC baseline search report

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/init/data/search-report.md>

**TLDR:** All ten Europe PMC requests succeeded on 10-21-2026. The versioned searches returned 40 review-slice matches and 21 executive-function/predictor-slice matches. These are overlapping database matches, not screened eligible studies or estimates of treatment effectiveness.

Run: `baseline-10-21-2026`; protocol 0.1; first-publication cutoff 10-21-2026. Query manifest, raw identifier-only responses, the exact executed script and a hashed run receipt are in [the run directory](search-runs/baseline-10-21-2026/). The [CSV log](search-counts.csv) preserves UTC timestamps and URLs. No model calls or paid services were used.

| Slice | Search focus | Matches |
| --- | --- | ---: |
| S01 | Reviews and meta-analyses | 40 |
| S02 | Randomized trials | 73 |
| S03 | Executive function and predictors or moderators | 21 |
| S04 | Executive function sensitivity search | 24 |
| S05 | Specific executive processes | 10 |
| S06 | Medication and adjunctive treatment | 63 |
| S07 | Active comparators and treatment components | 22 |
| S08 | Adherence and feasibility | 23 |
| S09 | Functioning and follow-up | 71 |
| S10 | Comorbid anxiety | 54 |

The counts are complete endpoint `hitCount` responses, not sample estimates: confidence intervals and p-values are not applicable. Counts overlap across slices and must not be summed. All 10/10 slices succeeded on their first attempt; no zero/error substitution occurred. The API returns one identifier per request in this counts-only workflow. Complete paginated exports are still needed for screening.

Historical counts of 27 reviews and 9 executive-function/moderator/outcome hits were supplied without exact queries or timestamps. They remain unverified and are not directly comparable to these broader, dated strings. Differences do not show a change in clinical evidence. PubMed/PsycINFO were not executed, no records have been screened, and no included-study denominator or clinical effect estimate exists yet.

Run the script with a new label for an update; old run directories cannot be overwritten. Database indexing can change even with a fixed publication cutoff. Invalid responses and transport failures are retried once; failures retain a blank count and make the process exit nonzero. A writer lock prevents concurrent CSV writes; after a crash, inspect the partial run and confirm no active writer before removing the lock. Preserve partial records and restart with a new label.
