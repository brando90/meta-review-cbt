# Why CBT can fail: a critical meta-review across conditions

**Doc link:** <https://github.com/brando90/meta-review-cbt>

**TLDR:** This project develops the strongest evidence-backed critique of cognitive behavioral therapy (CBT): when it fails, whom it fails, which claimed mechanisms remain unproven, and how study design can exaggerate apparent benefit. Its scope spans conditions; adult attention-deficit/hyperactivity disorder (ADHD) and executive function are one case study.

## Start with the original argument

- [Read the original blog draft: Why CBT Doesn't Make Sense to Me](sources/blog-original.md).
- [Read the Google Docs blog draft](https://docs.google.com/document/d/1-3ynnqjyrLw-rwftcR6Rpa1h7bhbhCDThq4cZlmU0bI/edit).
- [Read the prior 29-page critical review](sources/deep-research-draft-2.pdf).
- [Read the developing paper](main.pdf) and [evidence and gaps](evidence-map.md).

The blog asks why reasoning through distress should work when stress makes executive control harder. It also questions whether cognitive restructuring deserves credit for benefits delivered by exposure, behavioral activation, practice or support. These questions drive this project, along with nonresponse, comparator choice, bias, durability, treatment burden and alternatives. The preserved drafts include the author's strongest objections and the strongest counterarguments.

## The review's argument

We are building a critical case against overclaiming CBT, including its rationale, effectiveness, fit and implementation. Each proposed reason for failure must be linked to evidence at the right level: a treatment package, a component, a condition, a population or an individual outcome. Evidence of benefit and evidence contradicting the critique stay in the review. A null comparison does not establish equivalence; uncertainty about a mechanism does not establish that the treatment never helps.

The primary scope is adults across mental-health conditions, including anxiety, depression, trauma-related conditions, obsessive-compulsive disorder, eating disorders, psychosis, bipolar disorder and ADHD. Reviews of other clinical uses, including insomnia and chronic pain, are eligible in separate condition strata. Pediatric evidence requires a separately labeled extension. No single pooled verdict across unlike conditions is planned.

[Protocol 0.2](protocol.md) corrects the initial ADHD-only framing. The existing ten searches and the [21-record executive-function screen](data/s03-screening.md) are retained as an ADHD case study. They are **not** a search of all CBT evidence. Broader coverage and unresolved full texts are explicitly tracked.

## Reproduce

Requirements: Python 3.10+ (standard library only), TeX Live with `latexmk`, `pdflatex`, BibTeX, `natbib`, `booktabs`, `geometry`, `hyperref` and `microtype`; Poppler for optional PDF inspection.

```sh
python3 scripts/search_europe_pmc.py --dry-run
python3 scripts/search_europe_pmc.py --run-label update-10-21-2026
python3 -m unittest discover -s tests -v
make paper
```

`make paper` runs latexmk in `_build/` and refreshes `main.pdf`. Direct `latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex` also works. Searches require internet access, no credentials or model calls. Each run saves an immutable query manifest and response files, and appends to `data/search-counts.csv`; failures have blank counts, never zero. Details and measured counts are in [search report](data/search-report.md).

## Status and publication

The repository is populated on **main**. The original initialization pull request was merged; subsequent verified updates go directly to main at the author's explicit request on 10-21-2026. See [CHANGELOG](CHANGELOG.md).

The broader critical review is in development. The [evidence map](evidence-map.md) is a cited starting synthesis, not a completed exhaustive systematic review. The [screening report](data/s03-screening.md) distinguishes preliminary exclusions, indirect evidence and unresolved full texts. PubMed and PsycINFO systematic searches and independent second-reviewer screening remain pending.

The [Google project summary](https://docs.google.com/document/d/1f_iB6s4OG7D26Bns6782IGMuWA_GMTC_bEekB4_fERI/edit) records current scope and findings. [Source provenance](sources/README.md), [citation evidence](data/citation-evidence.csv), [search receipts](data/search-report.md), [validation](data/validation.md) and [open questions](open-questions.md) make the evidence status inspectable.
