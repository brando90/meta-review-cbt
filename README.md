# meta-review-cbt

A critical meta-review of **why CBT fails**: ten reasons (executive-function demands and ADHD, a cognitive component that may not be the active ingredient, inflated effects and measurement, non-response, dropout and relapse, under-recorded harm, patient and context factors, therapist and delivery factors, an under-tested theory of change), each graded against meta-analytic evidence. The executive-function/ADHD argument, which started the project as a blog post, is the deepest case study.

**Status:** Draft 3 (2026-10-21): 17-section paper (`elsarticle` preprint format) with a graded map of ten reasons CBT fails, built on about 440 DOI-verified sources. Draft 1 (blog-based) and Draft 2 (executive-function focus) are in the history of `main`. Nothing here has been sent to a journal or a reviewer.

> Working title: *Why Does CBT Fail? A Critical Meta-Review of Non-Response, Weak Mechanism Evidence and Delivery Limits, with Executive Function and Adult ADHD as a Test Case*

## Thesis in five lines
1. CBT works on average (moderate effects), but fewer than half of patients respond in several analyses, about 16% drop out before and 26% during treatment, and 29% relapse within a year after cognitive therapy ends.
2. Headline effects shrink with active controls, bias adjustment and quality; outcome measures are heterogeneous and harms are rarely recorded.
3. Most documented limits (dropout, comorbidity, relapse, therapist variability) are shared with other treatments; the CBT-specific gaps are mostly missing studies (autism, ADHD plus anxiety, minority groups, causal tests of competence).
4. The cognitive mechanism is under-tested; the best-supported active ingredients look behavioural (exposure, skills, practice).
5. Deepest case study: cognitive restructuring is an executive-function task, anxiety impairs the prefrontal systems behind it and ADHD often starts with executive weaknesses, but no adequately powered study tests executive function as a moderator in working-age adults with ADHD and anxiety.

## Repo map
| Folder | What is in it |
|---|---|
| `latex/` | The paper (`main.tex`, one file per section in `sections/`, 17 sections), Elsevier `elsarticle` format for *Clinical Psychology Review*. |
| `deep-research/` | Search protocol, per-topic source notes (eight slices), the **verified** bibliography (`references.bib`) and the verification log. |
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
- Commit and push straight to `main` (owner's standing instruction).
- Every reference must resolve (DOI through Crossref) and match the claim it supports. Unsourced claims are marked `\citegap{...}` and shown in red.
- Numbers come from the abstract or full text, never from memory.
- This repo is public. No personal health information about any person, ever.
- This is a theoretical review by a non-clinician, not medical advice.

## Venue
Primary target: *Clinical Psychology Review*. Fallbacks: *Perspectives on Psychological Science*, *Psychological Medicine*. See `review/venue.md`.
