# Changelog

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/evidence-screen/CHANGELOG.md>

**TLDR:** Project initialized on branch `init`; the original author material, protocol, measured search receipts and first manuscript are now versioned. This is not a completed systematic review.

## 10-21-2026 — Initial project, protocol 0.1

- Imported the exact blog Markdown, Google document text export and original 29-page deep-research Draft 2 PDF with extracted text and source hashes.
- Defined the adult-ADHD meta-review and supplementary baseline executive-function predictor/moderator study stream. Preserved the skeptical motivation without selecting studies by outcome direction.
- Added ten versioned search slices with Europe PMC, PubMed and PsycINFO/Ovid translations, PICO, eligibility and independent-screening plan. PubMed and PsycINFO execution and reviewer assignment remain pending.
- Implemented a credential-free Europe PMC count search with dry run, immutable run receipts, exact script snapshot, append-only CSV log, single-writer lock, one retry and explicit failures.
- Retrieved all ten Europe PMC count responses successfully: S01 reviews 40 matches; S03 executive-function/predictor candidates 21 matches. Other counts and limitations are in `data/search-report.md`. Historical 27/9 notes remain unverified.
- Added a cited abstract and introduction, the complete LaTeX section structure, ten independently retrieved bibliography records, a claim/scope evidence ledger, empty extraction templates and reproducible build commands.
- Added deterministic failure-handling and artifact-consistency checks. Compile and visual-verification details are recorded in `data/validation.md` after the build.

## Protocol deviations

At initialization (version 0.1), screening had not started. Version 0.2 broadens the scope at the author’s request and records a preliminary single-agent case-study screen; independent two-reviewer screening remains pending. Initial search wording and receipts are preserved.

## 10-21-2026 — Scope correction and publication on main

- Merged initialization PR #1 so the blog, review, README and manuscript are visible on the default branch.
- Restored the cross-condition critical scope from the author's blog/Google Docs draft; ADHD is one case study.
- Recorded direct-to-main publication instructions, protocol amendment 0.2, evidence map and preliminary 21-record screen.
- Preserved original sources and frozen ADHD search receipts; no broad-search completeness claim.
