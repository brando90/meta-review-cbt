# Draft 4 revision checkpoint

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/experiments/01_1st_principles_evolutionary_argument_against_cbt/CKPT_evolutionary_revision.md>

**TLDR:** The evolutionary-learning, evidence-selection and clinical-perspective revisions are implemented. The single requested Fable/max review and coordinator fixes are complete, and the final build and deterministic checks pass. The staged audit, publication and feedback delivery remain pending.

Created: 11-08-2026 16:07 PST
Last updated: 11-08-2026 17:44 PST

## Goal
- Revise the all-ten-reasons critical review; retain executive function and adult attention-deficit/hyperactivity disorder as the deepest case study. Truth outranks persuasion.
- Publish the checked manuscript and evidence records directly to `main`, then deliver the PDF for authorized collaborator feedback. Private routing stays outside Git.
## What ran
- Completed all three plans, manuscript integration and source notes against base `2f3ad20`.
- Initial source inventory: 39 candidates. Four existing delivery/alliance references were rechecked after review, yielding 43 identities, 42 abstracts and ten sets of relevant full-text passages; one metadata-only candidate remains excluded.
- One Claude `claude-fable-5-1` / `max` review completed on 11-08-2026; the reviewer checked the frozen 41-file manifest and did not edit the manuscript.
- Contact verification remains in ignored `_build/contact-verification.json` (mode 0600). The original context files remain intact.
## Results
- Reviewer verdict on the frozen input: FAIL, zero critical and five major findings; no second model review was requested or run.
- Edits address privacy wording, taxonomy-table placement, the stale introduction, the direction of the Johnco result and the COBRA workforce comparison. Final PDF inspection confirms the table on page 6 and the explicit feedback-draft footer.
- All thirteen unit tests pass (six companion, seven receipt/citation); the source checker reports 458 bibliography entries, 265 cited keys and 43 source records, with no undefined citations or references.
- Final manuscript: 63 pages, 411,639 bytes; its hash and full resolution record are in `review/LIGHT_QA_DRAFT4.md`. Origin was fetched and remains at base `2f3ad20`; no upstream integration is needed.
## Stuck / blocked
- No manuscript blocker. Abstract-only reading levels and the targeted search limits are explicit. Google companion synchronization is pending; no Google document was modified.
## Next steps
- [p 10/10] Inspect the exact staged changes and commit/push directly to `main`.
- [p 9/10] Deliver the checked PDF, verify the Sent copy and attachment, and update completion records.
## Brando to-do
- None for the authorized revision and delivery. Submission preparation is separate from feedback readiness.

## Log
- 11-08-2026 16:07 PST — Began the authorized revision and preserved the original review base.
- 11-08-2026 16:36 PST — Added evidence-selection and clinical-perspective work; resolved feedback routing privately.
- 11-08-2026 17:17 PST — Single model review completed with five major findings.
- 11-08-2026 17:28 PST — Applied manuscript fixes and rechecked four baseline abstracts.
- 11-08-2026 17:44 PST — Final build, visual inspection, source consistency checks, thirteen tests and spell-check pass; staged audit and delivery pending.
