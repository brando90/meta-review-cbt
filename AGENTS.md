# AGENTS.md: meta-review-cbt

## Project goal
Write a rigorous critical review of cognitive restructuring in CBT for anxiety (executive-function argument, adult ADHD as a test case) for submission to a psychology journal. Draft 1 exists; draft 2 integrates a deep literature search. The human owner decides what is sent to whom. Nothing is sent to a co-author, reviewer or journal without the owner's explicit yes.

## Folder map
- `latex/`: paper. `main.tex` + `sections/NN-name.tex`. Build: `cd latex && latexmk -pdf main.tex` (or `tectonic main.tex`). Format: `elsarticle` for *Clinical Psychology Review*.
- `deep-research/`: `protocol.md` (search strategy), `sources/*.md` (per-topic notes: one line per source with key numbers and a VERIFIED/PARTIAL flag), `references.bib` (single bibliography), `VERIFICATION.md` (log).
- `experiments/`: analyses of published data. Each run gets a dated entry in `experiments/LOG.md` (question, data source with DOI, code path, result, caveats).
- `review/`: `venue.md`, `claim_evidence_map.md`, `open_questions.md`, `CHANGELOG.md`.

## Hard rules
1. **Never invent a reference.** Add an entry to `references.bib` only after resolving its DOI through Crossref (`https://api.crossref.org/works/<doi>`) and checking that title, authors and year match what you intend to cite. If a DOI does not exist, drop the claim or write `\citegap{what is missing}`.
2. **Numbers from sources, not memory.** Quote effect sizes, sample sizes and percentages only after reading the abstract or full text. Record them in `deep-research/sources/`.
3. **Be fair to CBT.** The review argues a narrow claim. Report evidence against it, and keep the "strongest objections" section honest.
4. **Public repo: no personal data.** No health details about the author or anyone else; no private emails or names beyond co-authors. The paper's author statement is the only place for personal facts, and it carries none.
5. **Do not overstate popular sources.** Books, talks and blogs (e.g. Brewer) are cited as claims, not as evidence.
6. **Do not merge or push to `main` without the owner's yes.** Work on a branch and open a pull request. Compile the PDF before every commit; `\citegap` marks must not be silently deleted, only replaced by a verified citation.
7. **Log analyses.** Any number computed here is reproducible from a script in `experiments/` and an entry in `LOG.md`.

## Style
Plain, precise academic prose. First-person plural. Short paragraphs. Define terms once. No hype, no moralising, no medical advice.
