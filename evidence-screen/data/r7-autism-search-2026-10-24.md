# R7 targeted search: autism and CBT outcome (Europe PMC), 2026-10-24

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/evidence-screen/data/r7-autism-search-2026-10-24.md>

**TLDR:** The autism leg of R7 still rests on thin evidence: only four candidate randomized records for autistic adults, all small, and none tests a baseline cognitive or executive-function moderator. The closest direct test of ADHD as a moderator of CBT for anxiety is in autistic children (Ng-Cordell 2025, N = 167, no moderation). One database, one agent reading titles and abstracts; not a systematic screen.

## Why

`review/open_questions.md` item 7 flagged R7 (autism and other neurodivergence) as resting on two sources (Pérez-Castilla 2026; Weston 2016). This step runs a reproducible count and title/abstract triage to see whether a direct moderator test exists.

## Search (Europe PMC, run 2026-10-24, no date lower limit)

Receipts, raw responses and the script are in `search-runs/r7-autism-2026-10-24/` (`q.py`, `receipt.json`, one JSON per query). Terms: autis* or Asperger*, with the CBT phrases used in slices S01-S10.

| Id | Question | Hits |
| --- | --- | --- |
| A1 | Autism + adult* + CBT + randomized | 4 |
| A2 | Autism + CBT + review/meta-analysis | 32 |
| A3 | Autism + CBT + moderator/predictor/IPD/treatment response | 70 |
| A4 | Adult ADHD + anxiety + CBT + moderator/predictor/comorbid | 22 |

Counts overlap and are not unique records. A1 is narrow because it needs "adult*" and a randomization term in title or abstract; trials that describe themselves differently are missed. No PubMed or PsycINFO run (still pending, open question 8 in the evidence-screen list).

## Triage (single agent, titles and abstracts; abstracts only, no full texts)

| Record | Design | Reading for R7 |
| --- | --- | --- |
| Yang & Chung 2023, doi 10.1007/s10803-022-05617-9 | Pilot RCT, app-based CBT, autistic adolescents and adults 15-35, n = 30, waitlist | Anxiety fell versus waitlist, mostly proxy-reported; small, passive control, no moderator test |
| Russell et al. 2013, doi 10.1002/da.22053 | RCT, CBT for OCD vs anxiety management, ASD, n = 46 (mean age 26.9) | Active comparator; no moderator analysis in abstract |
| Kuroda et al. 2013, doi 10.1186/1745-6215-14-231 | Protocol only, group CBT for emotion regulation in adults with ASD, planned n = 60 | Not a result; check whether the trial reported |
| Murphy et al. 2017, doi 10.1007/s10803-017-3252-8 | Pilot RCT, CBT vs counselling, ages 12-18, n = 36 | Youth; CBT not superior to counselling, which the authors say matches adult findings |
| Roberts & Rankin 2025, doi 10.1177/13591045251314906 | Systematic review, 24 articles, youth 4-18, standard vs adapted CBT | Adapted CBT looked better, but the comparison was not statistically significant. Directly on the "autistic people lack the cognitive resources for CBT" worry, in youth |
| Ng-Cordell et al. 2025, doi 10.1111/jcpp.70010 (from A3) | Secondary analysis of a multisite RCT (standard CBT, autism-adapted CBT, treatment as usual), autistic children with elevated anxiety, N = 167; 62% met ADHD criteria | ADHD did not moderate anxiety response to CBT; CBT predicted lower evaluator-rated ADHD severity. Youth, not adults, but it is the one direct ADHD-as-moderator test of CBT for anxiety found so far |
| Roisenberg et al. 2026, doi 10.1002/aur.70268 | Single-arm modified CBT, 32 autistic adults with social anxiety | Fear extinction during a speech task related to response (59% vs 25% improved, high vs low extinction). A process predictor, not an executive-function moderator, and correlational |

## What changes

- No direct test of executive function or another cognitive baseline as a moderator of CBT in autistic adults was found. The draft's wording that autism evidence is "thin rather than negative" stands.
- Three candidates are worth adding after full-text checks: Ng-Cordell 2025 (ADHD not a moderator, autistic children; into the moderators section), Roberts & Rankin 2025 (youth, adapted vs standard CBT) and Roisenberg 2026 (extinction as a response predictor). Neither is added to the manuscript yet.
- A3 (70 hits, mostly youth predictor and moderator studies) is only skimmed by title. Ng-Cordell 2025 stands out; other youth moderator papers (e.g. on comorbidity and on baseline subgroups) are not yet read. The manuscript sentence "we found no study of ADHD as a moderator of CBT for anxiety in adults" stays true as worded, but the child analogue should be cited next to it.
- A4 returned the 2026 CBT-for-anxiety-in-ADHD meta-analysis (13 RCTs, n = 744) and the 2020 López-Pinar internalizing meta-analysis; both are already cited. Neither tests executive function as a moderator, so the "no ADHD-as-moderator study for anxiety in adults" sentence is unchanged.

## Next

1. Read the full texts of Ng-Cordell 2025, Roberts & Rankin 2025 and Roisenberg 2026, then add them with verified DOIs (all seven DOIs above resolve at Crossref, checked 2026-10-24). Screen the rest of A3.
2. Check whether the Kuroda 2013 protocol has a published results paper.
3. Run the same A1-A3 slices in PubMed (translation is in the protocol style of S01-S10).
