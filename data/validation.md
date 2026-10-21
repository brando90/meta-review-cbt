# Initialization validation

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/init/data/validation.md>

**TLDR:** The six-page manuscript compiles cleanly with both documented commands; all six search tests and the artifact-consistency checks pass. Search results are measured counts, while screening and clinical synthesis remain pending.

Verified on 10-21-2026:

| Check | Observed result |
| --- | --- |
| `python3 -m unittest discover -s tests -v` | 6/6 tests passed: zero versus failure, malformed responses, one retry, immutable runs, dry run, log schema, writer lock and safe configuration. |
| `python3 scripts/check_project.py` | 4/4 source hashes, 10 bibliography records, 10 cited keys and 10 search receipts verified; protocol queries and results tables agree. |
| `make paper` | latexmk completed; six pages, bibliography resolved. |
| `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` | Direct root build completed; six pages. |
| Final LaTeX log | 0 warnings, 0 undefined citations, 0 undefined references, 0 overfull/underfull boxes. Intermediate first-pass citation warnings were resolved by BibTeX and reruns. |
| Render inspection | All six manuscript pages rendered with Poppler and visually inspected for text, table and reference layout. |
| Europe PMC | 10/10 live count requests succeeded on their first attempt; exact queries, response hashes and executed script archived. |
| Google companion | Body read back and project folder verified; permission metadata confirms anyone-with-link reader access. |

The [machine-readable build receipt](build-receipt.json) records the delivered PDF hash and size. TeX toolchain: latexmk 4.83, pdfTeX 1.40.26 / TeX Live 2024. PDF metadata/timestamps can vary between rebuilds, so a future byte-identical PDF is not promised; source, bibliography and counts remain versioned.

The current citation ledger records the material actually checked, primarily metadata and abstracts. Full-text eligibility, bias judgments, clinical effect extraction and two-person screening have not been completed. The imported critical review is preserved as author material and its full reference set has not been independently validated.

Google companion: <https://docs.google.com/document/d/1f_iB6s4OG7D26Bns6782IGMuWA_GMTC_bEekB4_fERI/edit>.
