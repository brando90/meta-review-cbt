# Changelog

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/evidence-screen/CHANGELOG.md>

**TLDR:** Project initialized on branch `init`; the original author material, protocol, measured search receipts and first manuscript are now versioned. This is not a completed systematic review.

## 10-25-2026 — D2 and E1 abstract screen

- Reran slices D2 (27) and E1 (9) with abstracts; counts reproduced. Receipts and raw responses in `data/search-runs/d2-e1-2026-10-25/`, triage in `data/d2-e1-screen-2026-10-25.md`. No study tests baseline executive function as a moderator of CBT; nine review candidates found, not yet added to the manuscript.

## 10-24-2026 — R7 autism targeted search

- Ran four Europe PMC slices (A1-A4) on autism and ADHD with CBT; receipts, raw responses and script in `data/search-runs/r7-autism-2026-10-24/`. Triage note: `data/r7-autism-search-2026-10-24.md`. No direct cognitive or executive-function moderator test in autistic adults; Ng-Cordell 2025 (ADHD not a moderator of CBT for anxiety in autistic children, N = 167) is the closest direct analogue. Manuscript unchanged; three candidates await full-text checks.

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

## 10-23-2026
- Checked open-access status of the five unresolved S03 records (Europe PMC, Unpaywall): all closed. Receipt in `data/s03-fulltext-access-2026-10-23.md`; no screening decision changed; `open-questions.md` row 1 updated.
