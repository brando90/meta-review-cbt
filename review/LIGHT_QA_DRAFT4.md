# Draft 4 light review and resolution record

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/review/LIGHT_QA_DRAFT4.md>

**TLDR:** One requested Claude Fable/max review found zero critical and five major issues in the frozen revision. The coordinator addressed those findings, rechecked four baseline abstracts, and passed the deterministic checks without a second model review. The result is a feedback draft, not a submission-ready systematic review.

Date: 11-08-2026. Fixed review base: `2f3ad20`.

## Review contract and coverage

- **Builder/coordinator:** Pi using the exposed `gpt-6-astra` model; builder reasoning effort was not exposed.
- **Reviewer:** authenticated Claude Code subscription, actual response model `claude-fable-5-1`, explicit and observed effort `max`. One opposite-company light-review round; no application programming interface (API) key fallback or model substitution.
- **Ownership:** the reviewer could read the working tree and reading copies and write only its private findings/checkpoint. The coordinator alone edited the manuscript and handles Git and delivery.
- **Frozen input:** 41 file hashes, all matched by the reviewer. The review covered the revision against the base, the three plans/source notes, scripts and receipts, and selected rendered pages.
- **Source coverage:** the reviewer reported checking all 31 cited candidates in the initial 39-candidate inventory against abstracts, with relevant full-text checks for load-bearing claims. The inventory contains eight uncited candidates; the review's prose list named only seven of those eight. This small enumeration error does not change the cited-source coverage.
- **Independent execution:** reviewer reran the consistency checker and rebuilt a scratch PDF successfully, leaving the manuscript unchanged.
- **Limits:** not a fresh content review of all 458 bibliography entries, not independent duplicate screening, and not a test of systematic search completeness. Cached bibliographic records were used, not a fresh live resolution of every DOI.

The raw report, native-session evidence, frozen manifest and worker checkpoint are retained privately under ignored `latex/_build/qa/`. The completed report was written at 17:17 PST; its session was then closed after the handoff. No second reviewer or automatic re-review was run.

## Original reviewer verdict versus coordinator resolution

```text
Original frozen-input verdict: FAIL
Critical issues: 0
Major issues: 5
Reviewer-applied fixes: 0
Structural checks: PASS
Post-fix model verdict: NOT RUN (one-round contract)
Coordinator disposition: fixes applied; deterministic checks pass; ready for feedback
```

The original FAIL is not relabelled as a post-fix model PASS. The following resolutions are the coordinator's, supported by source checks, tests and PDF inspection.

### Major findings

| ID | Finding | Resolution and verification |
|---|---|---|
| M1 | Private first-name breadcrumb in a new public checkpoint | Replaced with a neutral contact-receipt reference; renamed the private receipt without losing its contents. Neutralised the inherited companion README heading as well. Private routing and receipts remain outside Git. |
| M2 | Ten-reason table stranded after the references | Changed the float from `[ht]` to `[!tp]`. Final table is on page **6**, near the taxonomy, rather than page 62 after the reference list; final references begin on page **31**. Inspected the rendered table: all ten rows are present and legible. |
| M3 | Introduction contradicted the revised component verdict | Introduction now describes mixed, often underpowered component evidence, names evidence selection and the evolutionary/clinical analyses, and calls the agenda testable hypotheses. Executive demand alone is not presented as proof of clinical moderation. |
| M4 | Johnco timing result reported one-sidedly | Manuscript, both relevant plans, source notes, claim map and blog paragraph retain the small, non-significant anxiety difference **favouring behavioural experiments**, plus greater expectancy change and a shorter session. The coordinator reread the actual abstract; the one-week follow-up and elevated-anxiety sample remain explicit. |
| M5 | COBRA workforce difference omitted from the component inference | Restored behavioural activation by junior mental health workers versus CBT by psychological therapists. Rechecked the full-text procedures: this is a package-and-workforce comparison, not an isolated restructuring contrast. The prespecified non-inferiority result and its interval remain unchanged. |

### Minor findings

| ID | Resolution |
|---|---|
| m1 | Moved the R7/R8 reading verdict above the new clinical-formulation subsection, so it no longer appears to summarise only that subsection. |
| m2 | Method now points to historical DOI/abstract checks and preserves partial-verification flags without pretending the present pass rechecked every old source. |
| m3 | Added a bounded quantitative abstract result: 16 depression component studies/22 comparisons, full versus reduced packages `g=.21`, 95% confidence interval `[.03,.39]`; methodological limitations remain explicit. |
| m4 | Added weakening observations for P2 and P4; all five hypotheses now have a stated weakening condition. |
| m5 | Restored Baldwin's citation after reading its abstract again. The therapist-level result is scoped to one sample of 331 patients and 80 therapists, not a universal location of the alliance effect. |
| m6 | Reduced repeated timing summaries and expectancy-change caveats through cross-references; removed repeated alliance/therapist effect estimates from the mechanisms section. Essential boundaries remain in the abstract and conclusion. A full journal copy-edit is still separate work. |
| m7 | Explicitly labelled early reframing as a plausible **clinical hypothesis**, not a demonstrated timing mechanism. |
| m8 | Reworded attribution as “a practicing clinician's perspective, shared informally with the author.” It identifies neither the clinician nor a patient; the classification stays informal and unvalidated. |
| m9 | Ignored the generated `latex/main.spl`. Preserved the original bias prompt unchanged at its local path but excluded it from publication through an exact ignore rule; no raw context was deleted. |
| m10 | Receipt exporter now requires an explicit reading inventory and rejects unknown candidates and changed recorded copies. Citation-gap markers are distinguished from bibliography keys. The checker recognises valid explicit BibTeX `and others` truncation only when the recorded author prefix matches. Seven offline tests cover these cases. These remain consistency guards, not proof of reading or scientific truth. |

### Inherited limitations and additional fixes

- **i1 — equivalence language:** rechecked Carlbring, Burlingame and Pittig abstracts. Carlbring now has its estimate and interval, not an unqualified equivalence claim; Burlingame is described as a small average difference for matched comparisons. Pittig's abstract explicitly reports **formal equivalence**, so this was not merely an undetected difference: the manuscript attributes that report to the authors, but the margin was not independently checked from full text. Removed unqualified “parity” in the alternatives discussion. See [source boundaries](../deep-research/sources/clinical-engagement.md).
- **i2 — review label:** changed the title from “Critical Meta-Review” to “Critical Review” to avoid implying a systematic review of reviews.
- **i3 — repeated alliance estimate:** replaced the duplicate with a cross-reference to the delivery section.
- **i4 — inherited private-name heading:** neutralised without changing the immutable imported source files.
- **i5 — LaTeX warnings:** explicit author metadata removed the hyperref warnings. A 2.61-point output-box warning and underfull bibliography boxes remain; inspected pages show no clipping or missing text. The misleading “Preprint submitted to” footer is replaced by “Draft 4: for feedback, not submitted.”
- **i6 — spelling convention:** mixed British/American conventions inherited from earlier sections remain a submission copy-editing task; no claim is changed by them. Spell-checking retained proper names rather than “correcting” them.

## Final deterministic verification

| Check | Observed result |
|---|---|
| `make test` | PASS: six companion unit tests, seven receipt/citation unit tests; both consistency checkers pass. |
| Companion audit validation | Four source hashes, 16 bibliography records, 16 cited keys, ten search receipts. |
| Revision checker | 458 bibliography entries; 265 unique cited keys; 20 labels; zero undefined citations/references and zero citation-gap markers. |
| Final source inventory | 43 identities: 23 evolutionary, eight bias, twelve clinical/delivery. Forty-two abstracts read; ten also have relevant full-text passages read; one metadata-only candidate excluded. |
| `make screen` | PASS. Its eight-page PDF has the same extracted text as the baseline; generated-only binary noise was excluded from this revision. |
| `make paper` | PASS: 63 pages, 411,639 bytes. |
| PDF checks | Table on page 6; references start on page 31; feedback footer present; no `??` markers or embedded files. Selected title, table, revised-text, declarations and reference pages visually inspected. |
| Source formatting | Edited LaTeX sections pass the one-sentence-per-line check; introduction reflow was verified whitespace-only. |
| Code/whitespace | Python compilation and `git diff --check` pass. |

Final PDF SHA-256:

```text
a413a808d10fb7ffc38709bbb0cea0f72bccbdc7f52813adeab98af0f4909754
```

The initial review checked 39 candidates. The four additional existing citations were checked by the coordinator during fixes; their provenance and abstract-only status are included in the clinical manifest/receipts. No new participant data or pooled treatment effect was generated.

## Release, feedback and remaining scope

- **Publication and feedback delivery:** pending the final staged audit and push; private delivery receipts will record the Sent copy and attachment hash, not whether the recipient read the paper.
- **Blog:** the separately owned post already includes the clinician-derived goals/engagement/timing section; this task preserves a source-linked alternative paragraph without overwriting or duplicating that work.
- **Google companion:** synchronization pending. Available connector/command-line routes and a bounded read-only browser attempt did not establish a writable route; no Google document was modified.
- **Submission:** not ready. The review is targeted, not independently double-screened or preregistered; no formal risk-of-bias assessment covers every included review. Official venue requirements, author verification and submission preparation remain separate work.

**TLDR-end:** [meta-review-cbt: Draft 4 light review] The single model-review round is complete and its major findings have been addressed with source-grounded fixes and deterministic verification. Use the checked PDF for feedback without treating this record as journal acceptance or full-bibliography validation.
