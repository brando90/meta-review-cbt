# CBT for adult ADHD: executive function and treatment outcomes

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/init/README.md>

**TLDR:** This project asks whether baseline executive function predicts or moderates outcomes of cognitive behavioral therapy (CBT) for adults with attention-deficit/hyperactivity disorder (ADHD). It preserves the author's skeptical blog and prior critical review, and adds a prospective meta-review protocol, reproducible searches and a cited manuscript draft; it does not yet report a completed systematic review.

## Question and scope

Does CBT improve adult ADHD symptoms and functioning relative to specified comparators, and does baseline executive function identify who benefits less or more? The motivating concern is that cognitive restructuring may require the very capacities some participants struggle to use. That concern is a hypothesis to test, not an inclusion criterion or a foregone conclusion.

The review will separate:

- **Predictor:** baseline executive function is associated with later outcome, possibly across treatments.
- **Moderator:** the effect of CBT versus a comparator differs with baseline executive function, tested as a treatment-by-baseline interaction.
- **Mediator or outcome:** executive function changes during treatment; such change alone does not establish baseline moderation.
- **Component versus package:** evidence about cognitive restructuring alone does not establish whether a multicomponent CBT program works.

Primary synthesis: systematic reviews and meta-analyses of CBT for adult ADHD. Supplementary synthesis: original adult-ADHD studies with baseline executive-function measures and treatment-outcome analyses. Non-ADHD anxiety and laboratory studies inform context only. See [protocol](protocol.md) for eligibility, ten search slices, assessment and screening plans.

## Existing material

The [source archive](sources/README.md) contains the actual blog draft and the 29-page deep-research Draft 2, including its searchable text. Their arguments and citations are not silently relabeled as verified findings. The current [manuscript](main.pdf) and [citation evidence](data/citation-evidence.csv) distinguish retrieved support from questions still to be answered.

## Reproduce

Requirements: Python 3.10+ (standard library only), TeX Live with `latexmk`, `pdflatex`, BibTeX, `natbib`, `booktabs`, `geometry`, `hyperref` and `microtype`; Poppler for optional PDF inspection.

```sh
python3 scripts/search_europe_pmc.py --dry-run
python3 scripts/search_europe_pmc.py --run-label update-10-21-2026
python3 -m unittest discover -s tests -v
make paper
```

`make paper` runs latexmk in `_build/` and refreshes `main.pdf`. Direct `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` also works. Searches require internet access, no credentials or model calls. Each run saves an immutable query manifest and response files, and appends to `data/search-counts.csv`; failures have blank counts, never zero. Details and measured counts are in [search report](data/search-report.md).

## Status and interpretation

This is a protocol and first manuscript draft, not a registered protocol, full-text screening result, pooled analysis or treatment recommendation. Europe PMC retrieval counts measure indexed search matches, not eligible reviews or evidence that CBT succeeds or fails. The previously reported counts of **27 reviews** and **9 executive-function/moderator/outcome hits** lack exact queries and timestamps and remain unverified historical notes. Current counts use the versioned queries in `search/queries.json` and must not be forced to match those numbers.

PubMed and PsycINFO searches are planned, not claimed as executed. PsycINFO translations target Ovid and require an available institutional session plus syntax validation. Database overlap must be deduplicated before screening. The two-reviewer plan remains pending reviewer assignment.

## Files and next steps

- `main.tex`, `sections/`, `references.bib`, `main.pdf`: current manuscript and compiled reading copy.
- `protocol.md`, `search/queries.json`: dated protocol and ten database-specific query translations.
- `scripts/search_europe_pmc.py`, `tests/`: count retrieval, provenance and failure handling.
- `data/`: measured search counts, query receipts, citation verification and empty screening/extraction templates.
- `sources/`: original requested blog and deep-research review, with provenance.
- `open-questions.md`, `CHANGELOG.md`: unresolved methodological choices and history.

Next work is full record export, deduplication, independent screening and extraction under the protocol. Preserve null and contradictory findings. Do not infer equivalence or no effect from a nonsignificant result. Changes are on branch `init` for review; `main` is not modified.
