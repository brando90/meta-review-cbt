# S03: full-text access check for the five unresolved records

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/evidence-screen/data/s03-fulltext-access-2026-10-23.md>

**TLDR:** None of the five unresolved records (S03-08, S03-09, S03-11, S03-12, S03-20) has an open-access full text, so their decisions stay `unresolved_full_text`. The abstracts again show executive function (EF) only as an outcome or profile descriptor, not a baseline-EF-by-treatment test. Resolving them needs institutional access.

Checked 10-23-2026 by one agent. Method: Europe PMC record lookup by PMID (fields `pmcid`, `isOpenAccess`, `inEPMC`, `inPMC`) and Unpaywall lookup by DOI. Abstracts re-read from the Europe PMC record.

| Record | PMID | DOI | Europe PMC / PMC full text | Unpaywall | What the abstract says about baseline EF |
| --- | --- | --- | --- | --- | --- |
| S03-08 | 39798484 | 10.1016/j.psychres.2025.116352 | none | closed | EF is a secondary outcome; mixed models compare groups at each time point. No baseline-EF prediction stated. |
| S03-09 | 41962667 | 10.1016/j.jad.2026.121748 | none | closed | EF differs across emotion-regulation profiles; CBT improves EF in the most dysregulated profile. Profiles are defined from emotion-regulation scales, so this is a profile comparison, not a baseline-EF predictor. |
| S03-11 | 41220055 | 10.1177/10870547251384462 | none | closed | No EF measure named; mediation by organizational/planning change and cognitions; waitlist control. |
| S03-12 | 33615398 | 10.1007/s00406-021-01236-0 | none | closed | EF is a secondary endpoint; group-by-time comparisons only. |
| S03-20 | 28866911 | 10.1177/1087054717725874 | none | closed | EF is a secondary outcome; CBT vs booster vs waitlist. |

## Consequence
- No decision changes. All five stay `unresolved_full_text` / `indirect_profile_unresolved` in `s03-screening.csv`. The abstracts give no sign of a baseline-EF predictor analysis, but an abstract cannot rule one out (supplementary tables and subgroup analyses often hold them).
- Next step for open question 1: obtain the five full texts through a university library and read Statistical Analysis and supplementary tables. Until then, the repo claim stays "no direct test confirmed in retrieved material", never "none exists".
