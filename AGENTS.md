# AGENTS.md: meta-review-cbt

## Project goal
Write a rigorous critical meta-review of why CBT fails: all the reasons (executive-function demands and ADHD, cognitive component not the active ingredient, inflated effects and measurement, non-response/dropout/relapse/harm, patient and context factors, therapist and delivery factors, an under-tested theory of change), each graded against meta-analytic evidence. The executive-function/ADHD argument (from the owner's blog draft and a shared Google Doc) is the deepest case study, one reason among ten, not the whole scope. For submission to a psychology journal. Draft 3 widens the scope. The human owner decides what is sent to whom. Nothing is sent to a co-author, reviewer or journal without the owner's explicit yes.

## Folder map
- `latex/`: paper. `main.tex` + `sections/NN-name.tex` (17 sections; order is the `\input` list in `main.tex`). Build: `cd latex && latexmk -pdf main.tex` (or `tectonic main.tex`). Format: `elsarticle` for *Clinical Psychology Review*.
- `deep-research/`: `protocol.md` (search strategy), `sources/*.md` (per-topic notes: one line per source with key numbers and a VERIFIED/PARTIAL flag), `references.bib` (single bibliography), `VERIFICATION.md` (log).
- `experiments/`: analyses of published data. Each run gets a dated entry in `experiments/LOG.md` (question, data source with DOI, code path, result, caveats).
- `review/`: `venue.md`, `claim_evidence_map.md`, `open_questions.md`, `CHANGELOG.md`.

## Hard rules
1. **Never invent a reference.** Add an entry to `references.bib` only after resolving its DOI through Crossref (`https://api.crossref.org/works/<doi>`) and checking that title, authors and year match what you intend to cite. If a DOI does not exist, drop the claim or write `\citegap{what is missing}`.
2. **Numbers from sources, not memory.** Quote effect sizes, sample sizes and percentages only after reading the abstract or full text. Record them in `deep-research/sources/`.
3. **Be fair to CBT.** The review grades reasons it is said to fail, and CBT keeps a moderate average effect in almost every analysis. Many limits (dropout, relapse, comorbidity, harm under-reporting) belong to all psychological treatment: say so. Report evidence against it, and keep the "strongest objections" section honest.
4. **Public repo: no personal data.** No health details about the author or anyone else; no private emails or names beyond co-authors. The paper's author statement is the only place for personal facts, and it carries none.
5. **Do not overstate popular sources.** Books, talks and blogs (e.g. Brewer) are cited as claims, not as evidence.
6. **Push straight to `main`** (owner's standing instruction, 2026-10-21: always push to main, no branch or pull request). Commit small and often. Compile the PDF before every commit; `\citegap` marks must not be silently deleted, only replaced by a verified citation.
7. **Log analyses.** Any number computed here is reproducible from a script in `experiments/` and an entry in `LOG.md`.

## Style
Plain, precise academic prose. First-person plural. Short paragraphs. Define terms once. No hype, no moralising, no medical advice.

## Rules carried over from the evidence-screen track (origin/main)
- Scope: a critical meta-review of why CBT can fail across conditions; ADHD and executive function are a case study, not the whole project.
- Preserve the original blog and Google Docs export in sources/ and use their questions to guide the argument. Do not manufacture evidence or omit contradictory findings.
- Brando explicitly instructed on 10-21-2026: always push verified project updates to main. This replaces the earlier init-branch-only workflow for this repository.
- Run make test and make paper, inspect the fresh PDF and exact staged diff before committing. Commit the current main.pdf with semantic manuscript changes.
- Preserve search receipts and distinguish abstract screening, full-text review, indirect evidence, and unresolved access. Do not claim an exhaustive review prematurely.
- Two tracks share this repo: the Draft 3 paper in `latex/`, `deep-research/`, `review/`, and the evidence-screen track at the root (`main.tex`, `sections/`, `protocol.md`, `evidence-map.md`, `sources/`, `data/`, `scripts/`, `tests/`). Neither was dropped in the merge; reconcile them deliberately, not by deleting one.
