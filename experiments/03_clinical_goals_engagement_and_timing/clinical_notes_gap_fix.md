# Draft 4.2: clinician-note gap fix

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/experiments/03_clinical_goals_engagement_and_timing/clinical_notes_gap_fix.md>

**TLDR:** A second pass over ten informal voice notes from a practicing clinician found six points that Draft 4.1 did not carry. Draft 4.2 adds them in `latex/sections/15-mechanism.tex` as clinical opinion, not evidence, with three source-checked counterpoints. No clinician identity or raw transcript is published.

Date: 11-09-2026. Canonical manuscript: [`latex/main.pdf`](../../latex/main.pdf).

## Coverage of the notes

| Clinical point | Draft 4.1 | Draft 4.2 |
|---|---|---|
| Goal is a changed relationship to the feeling, not always a different feeling | Covered (`13-patients.tex`) | No change |
| Resistance and patient types (four-way split) | Covered as formulation questions, not a validated classification | No change; kept out as a classification |
| Prescription, communication, relationship, timing, feedback | Covered (`13-patients.tex`, `14-delivery.tex`) | No change |
| Verbal is not the same as cognitive | Partly covered (format is not a mechanism) | Extended in the new top-down/strategic paragraph |
| Top-down versus strategic restructuring; metaphor, aphorism, paradox, corrective experience; respond to the logic of the problem | Missing (strategic therapy named once, no contrast) | Added |
| Attempted solutions (talking as relief, avoidance) and questions that lead the patient to state the maintaining loop | Missing | Added |
| Control paradox, including the panic example and the written logbook | Partly (thought-suppression rebound only) | Added, with the interoceptive-exposure caveat |
| Metaphor must fit the patient; listening is the key technique | Missing | Added |

## Source checks

All three are abstract-only readings, with Crossref identity checks (title, authors, year, journal, DOI).

- Braun et al. (2015), [10.1016/j.brat.2015.05.004](https://doi.org/10.1016/j.brat.2015.05.004): 55 adults in cognitive therapy for depression; within-patient Socratic questioning in sessions 1 to 3 predicted next-session symptom change (1.51-point BDI-II decrease per standard deviation), after controlling for alliance. Observational. Used for the guided-discovery caveat.
- Jackson et al. (2018), [10.1037/ccp0000313](https://doi.org/10.1037/ccp0000313): randomized trial, 60 women with binge eating disorder and obesity; brief strategic therapy favoured over CBT at one year. One trial, one population.
- Jansson-Fröjmark et al. (2022), [10.1111/jsr.13464](https://doi.org/10.1111/jsr.13464): meta-analysis of 10 trials of paradoxical intention for insomnia; large effects against passive and moderate against active comparators; authors ask for stronger studies.

Targeted Europe PMC searches (11-09-2026) for a direct comparison of top-down and strategic restructuring, for strategic-therapy trials and for paradoxical-intervention syntheses did not identify a study of that contrast. They were not exhaustive.

## Not claimed

No evidence is claimed for the clinician's mechanisms. The panic example does not separate strategic therapy from CBT, because interoceptive exposure is a CBT procedure. The resemblance of leading questions to guided discovery is the authors' reading, not the clinician's. The four-type split remains unvalidated.

## Verification run

`check_revision.py` and `test_verification_receipts.py` pass (461 bibliography entries, no undefined citations). The PDF was built with tectonic (`latexmk` cannot find `elsarticle` on this machine); an unchanged-source tectonic build gives the same 64 pages as the committed Draft 4.1 PDF, and this build is 67 pages.
