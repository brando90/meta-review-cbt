# Search and verification protocol

**Question.** Does the cognitive-restructuring component of CBT for anxiety depend on executive function that anxiety and ADHD impair, and where do CBT's active ingredients lie?

**Sources searched.** PubMed / Europe PMC, Crossref, Google Scholar, publisher pages, Cochrane Library, reference lists of the key meta-analyses. Date of search is recorded in each notes file. Today's coverage runs to October 2026.

**Inclusion (priority order).** Meta-analyses and umbrella reviews; RCTs and component (dismantling) trials; mechanistic neuroscience reviews (stress and prefrontal function); studies of executive function as a moderator of psychotherapy outcome; ADHD treatment trials and meta-analyses; the strongest critiques and defences of CBT.

**Verification (every source).**
1. Resolve the DOI through Crossref; title, authors and year must match.
2. Read the abstract (Europe PMC or PubMed) before quoting any number.
3. Record the entry in `sources/<slice>.md` with a VERIFIED (abstract or full text read) or PARTIAL (secondary source only) flag.
4. Only VERIFIED or explicitly flagged PARTIAL sources enter `references.bib`.

**Search yield (reproducible).** `search/europepmc_counts.py` runs ten Europe PMC strings and logs hit counts per slice (`search/counts-*.tsv`). Screening of those hits is not done yet.

**Known limitations.** Search is targeted rather than a PRISMA-complete systematic search; a PRISMA-style umbrella search is listed as a future step in `review/open_questions.md`.
