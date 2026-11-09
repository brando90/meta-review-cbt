# Evidence extensions and proposed analyses

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/experiments/README.md>

**TLDR:** These folders contain the Draft 4 revision plans and Draft 4.1 clinical-feedback follow-up, with source-reading records and reproducible checks. They do not contain new participant experiments or newly pooled treatment effects; the proposed analyses below have not been run.

## Completed evidence extensions — 11-08-2026

| Folder | Deliverable |
|---|---|
| [`01_1st_principles_evolutionary_argument_against_cbt/`](01_1st_principles_evolutionary_argument_against_cbt/) | Evolutionary-learning plan, 23 candidate records, shared retrieval/export/check scripts and the main revision checkpoint. |
| [`02_cbt_are_the_reviewers_so_of_course_it_has_the_most_evidence_most_accepted/`](02_cbt_are_the_reviewers_so_of_course_it_has_the_most_evidence_most_accepted/) | Evidence-selection plan and eight candidate records, separating allegiance/publication selection from unestablished reviewer suppression. |
| [`03_clinical_goals_engagement_and_timing/`](03_clinical_goals_engagement_and_timing/) | Clinical-perspective plan, source-linked blog paragraph, [clinical-feedback refinements](03_clinical_goals_engagement_and_timing/clinical_feedback_revision.md) and fourteen candidate records: eight initial sources, four baseline citations revisited during fixes, and two checked for the follow-up. |

The original 39-candidate revision had one independent Claude Fable/max review. The coordinator applied its fixes and performed the four additional abstract checks without a second model-review round. See the [review and resolution record](../review/LIGHT_QA_DRAFT4.md), [verification log](../deep-research/VERIFICATION.md) and [activity log](LOG.md).

Draft 4.1 adds two abstract checks and relevant Craske author-manuscript passages: the current total is 45 identities, 44 read abstracts, eleven full-text passage sets and one metadata-only exclusion. Public receipts record bibliographic identities and declared reading levels; reading copies and private artifacts stay outside Git. Rerunning retrieval or a consistency checker does not establish that a source was read or that a scientific inference is true.

## Proposed analyses — not run

1. **Effect-size drift:** extract published effect sizes and publication years, then fit a meta-regression with control type as a covariate.
2. **Moderator scan:** tabulate published executive-function or attention-deficit/hyperactivity-disorder moderator results and assess their consistency.
3. **Power check:** calculate sample sizes for a justified executive-function interaction in a component trial, with a prespecified target effect and assumptions.

Any future analysis needs a script, source identifiers, explicit assumptions, uncertainty and a dated entry in `LOG.md`. The current revision uses existing published findings only.

**TLDR-end:** [meta-review-cbt: evidence extensions] The three revision plans and source records are implemented. Proposed statistical analyses remain proposals, not reported results.
