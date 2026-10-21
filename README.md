# meta-review-cbt

A critical review of **cognitive restructuring in CBT for anxiety**, asking whether the "argue with your thoughts" component depends on executive function that anxiety (and, in some people, ADHD) impairs, and what the evidence says about where CBT's active ingredients are.

**Status:** Draft 1 (built from an informal blog post, upgraded and fully cited). Draft 2 (deep literature pass) in progress. Nothing here has been sent to a journal or a reviewer.

> Working title: *Reasoning Your Way Out of Anxiety? A Critical Review of Cognitive Restructuring, Executive Function and Adult ADHD*

## Thesis in three lines
1. Cognitive restructuring is, mechanically, an executive-function task (working memory, inhibition, shifting).
2. Acute stress and anxiety impair the prefrontal systems that support those functions; ADHD often starts with executive weaknesses.
3. CBT works on average (moderate effects, about half respond), but its *cognitive* mechanism is under-tested and the best-supported active ingredients look behavioural (exposure, skills, practice). No adequately powered study yet tests executive function as a moderator in working-age adults with ADHD and anxiety.

## Repo map
| Folder | What is in it |
|---|---|
| `latex/` | The paper (`main.tex`, one file per section in `sections/`), Elsevier `elsarticle` format for *Clinical Psychology Review*. |
| `deep-research/` | Search protocol, per-topic source notes, the **verified** bibliography (`references.bib`) and the verification log. |
| `experiments/` | Any re-analysis of published meta-analytic data (effect-size trends, moderator meta-regression). Every analysis is logged. |
| `review/` | The detailed review: venue recommendation, claim-by-claim evidence map, open questions and the draft changelog. |
| `AGENTS.md`, `CLAUDE.md` | Rules for AI coding agents working in this repo (citations must be verified; no personal data). |

## Build the paper
```bash
cd latex
latexmk -pdf main.tex      # or: tectonic main.tex
```
`main.pdf` is committed for convenience. The bibliography is `deep-research/references.bib`.

## Ground rules
- Every reference must resolve (DOI through Crossref) and match the claim it supports. Unsourced claims are marked `\citegap{...}` and shown in red.
- Numbers come from the abstract or full text, never from memory.
- This repo is public. No personal health information about any person, ever.
- This is a theoretical review by a non-clinician, not medical advice.

## Venue
Primary target: *Clinical Psychology Review*. Fallbacks: *Perspectives on Psychological Science*, *Psychological Medicine*. See `review/venue.md`.
