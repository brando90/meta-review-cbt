# Protocol: critical meta-review of CBT across conditions

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/evidence-screen/protocol.md>

**TLDR:** Version 0.2 (10-21-2026) restores the broader scope requested by the author: reasons CBT can fail across conditions, with systematic-review evidence and explicit gaps. This is an unregistered protocol amendment, not a completed review. The original ADHD search receipts remain intact as a case study.

## Scope amendment: primary review

The ADHD-only initial scope was narrower than the author's blog and intended project. This amendment precedes broad systematic screening and preserves the prior queries and counts rather than relabeling them as comprehensive evidence.

| Element | Broader definition |
| --- | --- |
| Population | Adults across mental-health conditions; other clinical uses such as insomnia and chronic pain remain eligible in separate strata. Separate diagnoses, settings, severity, comorbidity and age groups; do not extrapolate automatically to children. |
| Intervention | CBT packages and identifiable components, including cognitive restructuring, exposure, behavioral activation and compensatory skills. Code what was delivered rather than assuming all treatments labeled CBT are identical. |
| Comparator | Waitlist, usual care, pill/psychological placebo, active psychotherapy, medication, and component-removal contrasts, analyzed separately. |
| Outcomes | Symptoms, response, remission, functioning, quality of life, sustained benefit/relapse, deterioration/adverse events, dropout, burden and access; treatment-specific predictors, moderators and mechanisms. |

Primary questions: Where is benefit absent, small, uncertain, short-lived or poorly transferable? Does restructuring add benefit beyond behavioral components? How do control choice, publication bias, measurement and missing data affect conclusions? Who does not respond, and what alternatives have direct comparative support?

Include systematic reviews/meta-analyses with explicit selection methods and extractable CBT findings. Supplement with component trials, direct moderator studies, adverse-effect studies and mechanistic research, labeled by evidence type. Exclude irrelevant interventions, inseparable mixed interventions, unsystematic efficacy claims and duplicate reports without new information. Narrative and laboratory work can motivate hypotheses but cannot establish clinical ineffectiveness. Retain evidence favorable to CBT and contrary to the critique. Map overlapping reviews to primary studies, use AMSTAR 2, and extract estimates with reported uncertainty rather than pooling incompatible endpoints.

Search Europe PMC, PubMed and PsycINFO across: (1) cross-condition reviews, (2) anxiety, (3) depression, (4) trauma/obsessive-compulsive conditions, (5) other conditions, (6) components/mechanisms, (7) comparator/bias, (8) nonresponse/harms/burden, (9) durability/functioning, and (10) moderators/alternatives. Broad searches and translated syntax are pending, not represented by the ADHD-only counts below. The initial broad evidence map uses explicitly identified seed sources from the original drafts and targeted retrieval; it is not an exhaustive search.

The following operational definitions and ten frozen queries govern the retained **ADHD executive-function case study**, not eligibility for the broader review.

## ADHD case-study PICO and estimands

| Element | Definition |
| --- | --- |
| Population | Adults aged 18 or older with diagnosed ADHD; mixed-age studies only if adult results can be extracted separately. Record diagnostic method, comorbid anxiety/depression, medication and baseline severity. |
| Intervention | Structured CBT for adult ADHD, including skills-based, metacognitive and multicomponent programs explicitly described as CBT. Record delivery format, dose, therapist support, cognitive restructuring, organization/planning and homework separately. |
| Comparator | Waitlist/usual care, active psychological comparator, or pharmacotherapy alone for adjunctive CBT. Analyze each class separately; distinguish medication-balanced and medication-imbalanced contrasts. |
| Outcomes | ADHD symptoms and daily functioning at treatment end and longest reported follow-up; baseline executive-function associations and treatment-by-baseline-executive-function interactions. Secondary: quality of life, anxiety, adherence, dropout, adverse events and executive function measured as an outcome. |

Primary question: **Does the effect of CBT relative to its comparator vary with baseline executive function?** Secondary questions: Does baseline executive function predict later outcome regardless of treatment, and what do systematic reviews establish about CBT benefits under each comparator?

A predictor is a prognostic association; a moderator changes the treatment contrast. A statistically significant association in one arm and a nonsignificant association in another is not evidence of an interaction. Improvement in executive function during CBT is neither baseline moderation nor, by itself, a mediation analysis. These distinctions follow [Kraemer et al. (2002)](https://doi.org/10.1001/archpsyc.59.10.877). Extract the actual analysis rather than relying on authors' labels.

The executive-demand hypothesis predicts smaller CBT benefits at lower baseline executive function, particularly for cognitive restructuring; compensatory-skills accounts could predict greater benefit instead. Record both directions, confidence intervals and null findings. Do not select studies according to agreement with the author's blog.

## ADHD case-study evidence streams and eligibility

**A: Meta-review.** Include systematic reviews and meta-analyses with an explicit search and selection method and extractable adult-ADHD CBT results, irrespective of publication year or direction. Narrative reviews, editorials and non-systematic theoretical reviews supply context only. Map each review's primary studies to avoid treating overlapping reviews as independent replications.

**B: Supplementary original studies.** Include adult-ADHD CBT trials and prospective treatment cohorts measuring executive function before treatment and relating it to a later clinical/functional outcome, or presenting an extractable treatment interaction. Randomized comparisons inform causal treatment-effect moderation; nonrandomized or single-arm results remain prognostic evidence with their limitations. Studies measuring executive function only after treatment or only as an outcome enter the outcome/context inventory, not the baseline moderator synthesis. Prespecified and exploratory interactions are separate.

Exclude from primary synthesis: exclusively pediatric samples; mixed samples without separate adult-ADHD data; no ADHD diagnosis; no relevant CBT intervention; no extractable relevant results; duplicate reports without new information. Link companion reports rather than discarding useful follow-up data. Abstracts, dissertations and preprints may be retained provisionally but are labeled by publication status and assessed for extractability; unavailable full text is *awaiting retrieval*, not evidence of no effect. Apply no language exclusion at search; seek translation and disclose unresolved cases. Exclude publications first published after 10-21-2026 from this baseline version. Contextual older-adult anxiety studies must not be silently generalized to ADHD.

## ADHD case-study databases and ten search slices

Europe PMC is the implemented baseline search. PubMed and PsycINFO (Ovid) are planned complementary searches, not yet executed. Search database inception through 10-21-2026 where fields permit; log exact platform, date, limits, query, count and export. The executable source of truth is [search/queries.json](search/queries.json), containing **ten complete search strings per database**. The Europe PMC strings are also reproduced below, not shorthand placeholders. PubMed uses title/abstract and publication-type/date fields; Ovid translations require syntax validation against the institution's PsycINFO interface before use. Record any revision as a new protocol/query version, without replacing baseline receipts.

The core combines ADHD synonyms, adult terms and CBT spelling variants. Slices overlap deliberately; counts cannot be added to obtain unique records. S01 retrieves reviews, S02 trials, S03 baseline/executive-function candidate associations, S04 a broader executive-function sensitivity set, S05 named cognitive processes, S06 medication, S07 components/comparators, S08 adherence, S09 functioning/follow-up, and S10 anxiety. Title/abstract filters can miss relevant studies, so reference checking and broader sensitivity retrieval are required before claiming completeness.

<!-- BEGIN GENERATED EUROPE PMC QUERIES -->
### S01 — Reviews and meta-analyses

```text
(TITLE_ABS:ADHD OR TITLE_ABS:"attention deficit hyperactivity disorder" OR TITLE_ABS:"attention-deficit/hyperactivity disorder" OR TITLE_ABS:"attention deficit disorder") AND (TITLE_ABS:adult*) AND (TITLE_ABS:"cognitive behavioral therap*" OR TITLE_ABS:"cognitive behavioural therap*" OR TITLE_ABS:"cognitive behavior therap*" OR TITLE_ABS:"cognitive behaviour therap*" OR TITLE_ABS:CBT) AND ((TITLE_ABS:review OR TITLE_ABS:"systematic review" OR TITLE_ABS:"meta-analysis" OR TITLE_ABS:"meta analysis") OR PUB_TYPE:review OR PUB_TYPE:"meta-analysis") AND FIRST_PDATE:[1900-01-01 TO 2026-10-21]
```

### S02 — Randomized trials

```text
(TITLE_ABS:ADHD OR TITLE_ABS:"attention deficit hyperactivity disorder" OR TITLE_ABS:"attention-deficit/hyperactivity disorder" OR TITLE_ABS:"attention deficit disorder") AND (TITLE_ABS:adult*) AND (TITLE_ABS:"cognitive behavioral therap*" OR TITLE_ABS:"cognitive behavioural therap*" OR TITLE_ABS:"cognitive behavior therap*" OR TITLE_ABS:"cognitive behaviour therap*" OR TITLE_ABS:CBT) AND (TITLE_ABS:random* OR TITLE_ABS:trial OR TITLE_ABS:RCT) AND FIRST_PDATE:[1900-01-01 TO 2026-10-21]
```

### S03 — Executive function and predictors or moderators

```text
(TITLE_ABS:ADHD OR TITLE_ABS:"attention deficit hyperactivity disorder" OR TITLE_ABS:"attention-deficit/hyperactivity disorder" OR TITLE_ABS:"attention deficit disorder") AND (TITLE_ABS:adult*) AND (TITLE_ABS:"cognitive behavioral therap*" OR TITLE_ABS:"cognitive behavioural therap*" OR TITLE_ABS:"cognitive behavior therap*" OR TITLE_ABS:"cognitive behaviour therap*" OR TITLE_ABS:CBT) AND (TITLE_ABS:"executive function*" OR TITLE_ABS:"cognitive control" OR TITLE_ABS:"cognitive flexibil*" OR TITLE_ABS:"working memory" OR TITLE_ABS:inhibit* OR TITLE_ABS:"set shifting" OR TITLE_ABS:"set-shifting" OR TITLE_ABS:planning) AND (TITLE_ABS:moderat* OR TITLE_ABS:predict* OR TITLE_ABS:outcome* OR TITLE_ABS:response OR TITLE_ABS:baseline) AND FIRST_PDATE:[1900-01-01 TO 2026-10-21]
```

### S04 — Executive function sensitivity search

```text
(TITLE_ABS:ADHD OR TITLE_ABS:"attention deficit hyperactivity disorder" OR TITLE_ABS:"attention-deficit/hyperactivity disorder" OR TITLE_ABS:"attention deficit disorder") AND (TITLE_ABS:adult*) AND (TITLE_ABS:"cognitive behavioral therap*" OR TITLE_ABS:"cognitive behavioural therap*" OR TITLE_ABS:"cognitive behavior therap*" OR TITLE_ABS:"cognitive behaviour therap*" OR TITLE_ABS:CBT) AND (TITLE_ABS:"executive function*" OR TITLE_ABS:"cognitive control" OR TITLE_ABS:"cognitive flexibil*" OR TITLE_ABS:"working memory" OR TITLE_ABS:inhibit* OR TITLE_ABS:"set shifting" OR TITLE_ABS:"set-shifting" OR TITLE_ABS:planning) AND FIRST_PDATE:[1900-01-01 TO 2026-10-21]
```

### S05 — Specific executive processes

```text
(TITLE_ABS:ADHD OR TITLE_ABS:"attention deficit hyperactivity disorder" OR TITLE_ABS:"attention-deficit/hyperactivity disorder" OR TITLE_ABS:"attention deficit disorder") AND (TITLE_ABS:adult*) AND (TITLE_ABS:"cognitive behavioral therap*" OR TITLE_ABS:"cognitive behavioural therap*" OR TITLE_ABS:"cognitive behavior therap*" OR TITLE_ABS:"cognitive behaviour therap*" OR TITLE_ABS:CBT) AND (TITLE_ABS:"working memory" OR TITLE_ABS:inhibit* OR TITLE_ABS:"cognitive flexibil*" OR TITLE_ABS:"set shifting" OR TITLE_ABS:"set-shifting" OR TITLE_ABS:planning) AND FIRST_PDATE:[1900-01-01 TO 2026-10-21]
```

### S06 — Medication and adjunctive treatment

```text
(TITLE_ABS:ADHD OR TITLE_ABS:"attention deficit hyperactivity disorder" OR TITLE_ABS:"attention-deficit/hyperactivity disorder" OR TITLE_ABS:"attention deficit disorder") AND (TITLE_ABS:adult*) AND (TITLE_ABS:"cognitive behavioral therap*" OR TITLE_ABS:"cognitive behavioural therap*" OR TITLE_ABS:"cognitive behavior therap*" OR TITLE_ABS:"cognitive behaviour therap*" OR TITLE_ABS:CBT) AND (TITLE_ABS:medicat* OR TITLE_ABS:pharmacotherap* OR TITLE_ABS:adjunct* OR TITLE_ABS:"add-on" OR TITLE_ABS:stimulant*) AND FIRST_PDATE:[1900-01-01 TO 2026-10-21]
```

### S07 — Active comparators and treatment components

```text
(TITLE_ABS:ADHD OR TITLE_ABS:"attention deficit hyperactivity disorder" OR TITLE_ABS:"attention-deficit/hyperactivity disorder" OR TITLE_ABS:"attention deficit disorder") AND (TITLE_ABS:adult*) AND (TITLE_ABS:"cognitive behavioral therap*" OR TITLE_ABS:"cognitive behavioural therap*" OR TITLE_ABS:"cognitive behavior therap*" OR TITLE_ABS:"cognitive behaviour therap*" OR TITLE_ABS:CBT) AND (TITLE_ABS:"active control" OR TITLE_ABS:relaxation OR TITLE_ABS:psychoeducation OR TITLE_ABS:dismantl* OR TITLE_ABS:component* OR TITLE_ABS:"cognitive restructur*") AND FIRST_PDATE:[1900-01-01 TO 2026-10-21]
```

### S08 — Adherence and feasibility

```text
(TITLE_ABS:ADHD OR TITLE_ABS:"attention deficit hyperactivity disorder" OR TITLE_ABS:"attention-deficit/hyperactivity disorder" OR TITLE_ABS:"attention deficit disorder") AND (TITLE_ABS:adult*) AND (TITLE_ABS:"cognitive behavioral therap*" OR TITLE_ABS:"cognitive behavioural therap*" OR TITLE_ABS:"cognitive behavior therap*" OR TITLE_ABS:"cognitive behaviour therap*" OR TITLE_ABS:CBT) AND (TITLE_ABS:homework OR TITLE_ABS:adherence OR TITLE_ABS:engagement OR TITLE_ABS:dropout OR TITLE_ABS:"drop-out" OR TITLE_ABS:attrition OR TITLE_ABS:feasibility) AND FIRST_PDATE:[1900-01-01 TO 2026-10-21]
```

### S09 — Functioning and follow-up

```text
(TITLE_ABS:ADHD OR TITLE_ABS:"attention deficit hyperactivity disorder" OR TITLE_ABS:"attention-deficit/hyperactivity disorder" OR TITLE_ABS:"attention deficit disorder") AND (TITLE_ABS:adult*) AND (TITLE_ABS:"cognitive behavioral therap*" OR TITLE_ABS:"cognitive behavioural therap*" OR TITLE_ABS:"cognitive behavior therap*" OR TITLE_ABS:"cognitive behaviour therap*" OR TITLE_ABS:CBT) AND (TITLE_ABS:functioning OR TITLE_ABS:"quality of life" OR TITLE_ABS:"long-term" OR TITLE_ABS:"follow-up" OR TITLE_ABS:occupational) AND FIRST_PDATE:[1900-01-01 TO 2026-10-21]
```

### S10 — Comorbid anxiety

```text
(TITLE_ABS:ADHD OR TITLE_ABS:"attention deficit hyperactivity disorder" OR TITLE_ABS:"attention-deficit/hyperactivity disorder" OR TITLE_ABS:"attention deficit disorder") AND (TITLE_ABS:adult*) AND (TITLE_ABS:"cognitive behavioral therap*" OR TITLE_ABS:"cognitive behavioural therap*" OR TITLE_ABS:"cognitive behavior therap*" OR TITLE_ABS:"cognitive behaviour therap*" OR TITLE_ABS:CBT) AND (TITLE_ABS:anxiety OR TITLE_ABS:anxious OR TITLE_ABS:comorbid*) AND FIRST_PDATE:[1900-01-01 TO 2026-10-21]
```
<!-- END GENERATED EUROPE PMC QUERIES -->

The script retrieves **counts plus one identifier per slice**, not complete screening exports. Before screening, export every matching record with pagination, deduplicate across slices/databases and preserve export provenance. Record citation chasing of included reviews/trials separately. Compare S03 with S04 and cited-study recovery to assess missed predictor terminology. The historical 27-review and 9-hit notes cannot establish search sensitivity without their original strings and dates.

## Screening and extraction plan

1. Freeze dated exports and assign record IDs. Deduplicate first on digital object identifier (DOI), then PubMed ID (PMID), then normalized title/year with manual confirmation. Retain all source-database IDs and review-to-study relationships.
2. Two independent reviewers pilot up to 50 records (all if fewer), reconcile eligibility rules and record amendments before full screening. Reviewer names and a third adjudicator are not yet assigned; no two-person screening is claimed.
3. Independently screen titles/abstracts, then full texts. Record include/exclude/uncertain decisions, full-text exclusion reasons and disagreements. Resolve by discussion, then adjudication. Report counts in a Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) flow after screening, not now.
4. Extract into the versioned templates in `data/`. A second reviewer checks all clinical estimates, moderator/predictor classifications and study identifiers. Separate multiple reports from distinct samples.
5. Record sample size and outcome-specific denominator, diagnosis, age, medication, comparator, intervention components, executive-function instrument/domain, baseline timing, rater/blinding, outcome/time point, interaction specification, covariate adjustment, missing data, attrition, effect estimate and 95% confidence interval, exact reported p-value/test, and prespecification/multiplicity. Never invent missing uncertainty; label it unavailable and seek the source.

## Appraisal and synthesis

Assess reviews using [AMSTAR 2](https://doi.org/10.1136/bmj.j4008), retaining domain judgments rather than an invented summed score. For original studies, record randomization/allocation, deviations, missingness, outcome measurement and selective reporting with support from full texts. Final choice of a design-specific risk-of-bias instrument is an amendment to make before extraction. Check whether baseline executive function is measured by performance tasks or self-report, and whether it overlaps conceptually with the outcome.

Start with a structured evidence map. Keep review-level estimates separate from de-duplicated primary-study estimates. Tabulate active versus passive controls, adjunctive versus stand-alone CBT, blinded versus unblinded ratings and post-treatment versus follow-up outcomes. Do not pool already-overlapping meta-analyses. Show review overlap and study coverage explicitly.

Any future pooled moderator analysis requires at least two independent studies with a compatible executive-function construct, treatment contrast, outcome/time point and interaction estimand; this is a minimum for consideration, not a guarantee of reliable inference. A statistical analysis amendment must specify scale harmonization, model, dependence handling and heterogeneity before fitting. Single-arm prognostic slopes must never be pooled with randomized treatment interactions. Unavailable subgroup data cannot be inferred from aggregate executive-function improvement. Report intervals, study/participant denominators and limitations; small or nonsignificant estimates do not establish equivalence. Separate exploratory from confirmatory findings and preserve null results.

Reporting will follow [PRISMA 2020](https://doi.org/10.1136/bmj.n71) and [PRISMA-S](https://doi.org/10.1186/s13643-020-01542-z). A protocol is not evidence that those standards have already been fulfilled. Full-text citation verification, registration, reviewer assignment and screening remain open.

## Provenance, deviations and conflicts

The author is motivated by skepticism about executive demands in cognitive restructuring. The archived blog and critical review are author sources, not screened data or a predetermined conclusion. Keep contradictory evidence and distinguish CBT components from packages. Archive original search receipts; append reruns rather than overwriting them. Record protocol deviations in `CHANGELOG.md` with date, reason and stage. No participant-level clinical data are collected in this project initialization.
