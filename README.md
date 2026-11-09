# meta-review-cbt

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/README.md>

**TLDR:** Draft 4.1 (11-08-2026) incorporates clinical feedback into the critical review of ten proposed reasons cognitive behavioral therapy (CBT) may fail, with executive function and adult attention-deficit/hyperactivity disorder (ADHD) as the deepest case study. It distinguishes intellectual understanding, emotional responding and everyday behaviour without claiming a universal therapeutic sequence, systematic completeness or submission readiness.

**Paper:** [Draft 4.1 PDF](latex/main.pdf) · [clinical-feedback changes](experiments/03_clinical_goals_engagement_and_timing/clinical_feedback_revision.md) · [earlier Draft 4 review record](review/LIGHT_QA_DRAFT4.md) · [claim–evidence map](review/claim_evidence_map.md) · [source-verification log](deep-research/VERIFICATION.md)

> *Why Does CBT Fail? A Critical Review of Ten Proposed Explanations, with Executive Function and Adult ADHD as a Test Case*

## Scope and conclusions

The review retains ten reasons: executive demands, uncertain cognitive-component contributions, biased effect estimates, non-response and dropout, relapse, harms, patient factors, context, delivery, and under-tested mechanisms. The executive-function argument is one case study, not the entire review.

1. CBT works on average, while non-response, relapse and delivery/access limitations remain important; many limitations are shared with other therapies.
2. Package efficacy does not identify a causal component. Component findings are mixed, often underpowered and sensitive to disorder, comparator and follow-up.
3. Evolutionarily conserved learning motivates a hypothesis about practice and action, not a ranking of treatments. Instructions and cognitive processing can help before experience.
4. Researcher allegiance and publication selection warrant scrutiny. The sources checked do not establish that CBT-oriented reviewers suppress alternatives or that all therapies are equivalent.
5. Acceptance, alliance, reactance and structured feedback connect clinical goals and engagement to research. They do not validate the informal four-type classification, its prevalence claims or the exact early-reframing hypothesis.

The [current blog post](https://github.com/brando90/brandomiranda/blob/55b7edf3c920e658998e41fd6b8408acd054a6c9/_posts/2026-11-08-why-cbt-doesnt-make-sense-to-me.md) is a separate, independently maintained artifact. The [original imported blog draft](evidence-screen/sources/blog-original.md) remains unchanged.

## Revision plans

- [Evolutionary learning: defensible claims and counterevidence](experiments/01_1st_principles_evolutionary_argument_against_cbt/changes_to_paper_based_on_my_evolutionary_argument.md)
- [Evidence volume, allegiance and reviewer selection](experiments/02_cbt_are_the_reviewers_so_of_course_it_has_the_most_evidence_most_accepted/changes_cbt_reviewer_bias.md)
- [Clinical goals, engagement and timing](experiments/03_clinical_goals_engagement_and_timing/changes_clinical_perspective.md), plus a [source-linked blog paragraph](experiments/03_clinical_goals_engagement_and_timing/blog_paragraph.md)

The current source inventory contains 45 candidate identities: the initial 39, four existing citations rechecked during Draft 4 fixes, and two existing references checked for the clinical-feedback follow-up. Abstracts were read for 44; eleven also had relevant full-text passages read, including the newly inspected Craske author-manuscript passages. One metadata-only candidate is excluded. These checks are **not** a fresh content verification of all 458 bibliography entries. Identifier resolution, retrieval, reading and consistency tests are different activities.

## Repository map

| Folder | Role |
|---|---|
| `latex/` | Canonical manuscript, section files and committed PDF; `elsarticle` format. |
| `deep-research/` | Search protocol, topic notes, bibliography and historical/current verification records. |
| `experiments/` | Revision plans, candidate manifests, public metadata/reading receipts and reproducible checks; no new participant experiment or pooled treatment estimate. |
| `review/` | Review/fix record, venue notes, claim–evidence map and changelog. |
| `evidence-screen/` | Companion audit trail for the ADHD case study: protocol, search receipts, 21-record screen, scripts and tests; **not a second submission manuscript**. |
| `AGENTS.md`, `CLAUDE.md` | Shared project instructions for coding agents. |

## Build and check

From the repository root:

```bash
make paper   # Build latex/main.pdf.
make screen  # Build the evidence-screen companion.
make test    # Six companion tests, seven revision tests, and consistency checks.
```

The canonical bibliography is `deep-research/references.bib`. The revision checks validate citations, labels, source-record consistency and available cached-file hashes; they do not establish scientific truth or prove that a source was read. Copyrighted reading copies and private contact/mail receipts remain in ignored `_build/` directories.

## Ground rules and readiness

- Commit and push directly to `main`, following the owner's standing instruction; inspect changes and preserve concurrent work.
- Resolve bibliographic identities and check source content before making claims. Missing support remains explicit rather than fabricated.
- Quote numbers from inspected abstracts or full-text passages, with their denominators, uncertainty and scope.
- Keep personal health information, clinician identities, private correspondence and raw transcripts out of the public manuscript artifacts.
- This is a theoretical review by a non-clinician, not medical advice.
- Feedback readiness is distinct from submission readiness. No journal submission has been made. The provisional target is *Clinical Psychology Review*; official venue requirements and submission preparation remain to be confirmed separately ([venue notes](review/venue.md)).

## Evidence-screen companion

The companion preserves protocol 0.2, ten Europe PMC search receipts, a 21-record executive-function screen and a short developing report. Its narrow screen does not cover all CBT evidence.

- [Companion PDF](evidence-screen/main.pdf), [protocol](evidence-screen/protocol.md), [evidence and gaps](evidence-screen/evidence-map.md), [open questions](evidence-screen/open-questions.md)
- [Imported-source record](evidence-screen/sources/README.md), [prior 29-page review](evidence-screen/sources/deep-research-draft-2.pdf), [companion changelog](evidence-screen/CHANGELOG.md)
- The broader historical search-count log lives separately in [`deep-research/search/`](deep-research/search/).

**TLDR-end:** [meta-review-cbt: clinical-feedback revision] Draft 4.1 incorporates the clinical refinements with explicit source and interpretation limits. Read the current PDF alongside its change record; the earlier Draft 4 review remains a separate historical record.
