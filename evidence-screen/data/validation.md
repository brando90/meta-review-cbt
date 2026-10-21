# Validation of the cross-condition scope update

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/evidence-screen/data/validation.md>

**TLDR:** The current eight-page PDF builds cleanly. Six deterministic tests and the offline source/citation/search/screening consistency checks pass. These checks validate artifacts, not clinical conclusions.

- Date: 10-21-2026.
- `make test`: six search/failure-handling tests pass; four original source hashes, sixteen bibliography records and ten immutable search receipts verified.
- The 21-record screening ledger has unique source/ID pairs, reasons and source locations; five candidate full texts remain unresolved.
- `make paper`: latexmk/BibTeX completes; final log has zero warnings, undefined citations/references, or overfull/underfull boxes.
- All eight rendered pages inspected, including author-year citations and bibliography. Author-name parsing was corrected before the final build.
- Changed prose passes the sentence-per-line check; `git diff --check` passes.
- PDF SHA-256, bytes and measured checks are in [build receipt](build-receipt.json).
- No cross-condition systematic-search completeness, independent second screening, or new pooled clinical estimate is claimed.
