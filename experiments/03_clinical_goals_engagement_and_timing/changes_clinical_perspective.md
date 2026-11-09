# Clinical goals, engagement and timing: evidence and integration plan

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/experiments/03_clinical_goals_engagement_and_timing/changes_clinical_perspective.md>

**TLDR:** Acceptance, therapeutic alliance, reactance and feedback have research support, so the useful clinical points are not merely opinion. The proposed four-type classification, its prevalence claims and a universal rule against early cognitive restructuring are not established by the sources checked; retain these boundaries and the evidence that cognition can help.

Date: 11-08-2026. Scope: a short position-paper-style extension to the critical review, plus a matching blog-ready paragraph kept in this experiment folder. No website publication is part of this addition. Private sources are unnamed, and raw transcripts are not copied into tracked files. Implemented in Draft 4; the [review resolution record](../../review/LIGHT_QA_DRAFT4.md) also covers four baseline delivery/alliance citations rechecked during fixes.

## 1. Goal: a different relationship with feelings, not necessarily their elimination

**Research-supported formulation:** Acceptance and commitment therapy (ACT) targets psychological flexibility—responding to the present situation and persisting or changing action in line with values. Acceptance and cognitive defusion address how a person responds to thoughts and feelings, not simply their frequency or intensity.

- Hayes et al. (2006), [10.1016/j.brat.2005.06.006](https://doi.org/10.1016/j.brat.2005.06.006): **abstract and author-manuscript full-text sections on acceptance, defusion and committed action read**. This is a treatment model and developer-authored review, not proof of its unique causal mechanism. The supplied PDF is an author-manuscript version, not a checked final publisher PDF.
- Stockton et al. (2019; online 2018), [10.1017/S1352465818000553](https://doi.org/10.1017/S1352465818000553): **abstract read**. Twelve mediation studies, published between 2006 and 2015, were generally consistent with the psychological-flexibility model, but methodological quality was limited and only a narrow range of proposed processes was studied.

**Do not infer:** that an emotion must disappear before behaviour can change; that all effective treatment works by changing feelings; that mediation establishes a unique causal pathway; or that ACT is evidence against the whole CBT family. ACT is an acceptance-based member of the broader behavioural/CBT tradition. Symptom reduction and better functioning need not be rival treatment goals.

**Placement:** one paragraph in `latex/sections/13-patients.tex`, under a new subsection “Goals, engagement and clinical formulation,” with a cross-reference to the alternatives/mechanism discussion.

## 2. Patient types: keep the clinical questions, not an unsupported taxonomy

The informal clinical perspective distinguishes four situations: needing clear instructions, wanting change but being blocked by fear, resisting perceived control, and difficulty establishing collaborative engagement. Treat these as **formulation questions**, not stable patient types, diagnoses or a validated classification. The fourth situation does not identify a diagnosis and must not be used to equate disengagement with psychosis.

The empirical literature supplies related constructs, not validation of that four-way split:

- **Readiness to change:** Krebs et al. (2018), [10.1002/jclp.22683](https://doi.org/10.1002/jclp.22683), **abstract read**: 76 studies and 25,917 patients; pretreatment readiness was associated with outcome (`d = 0.41`, confidence interval unavailable in the abstract). An association does not establish that a particular stage-matched intervention causes better outcomes.
- **Reactance and directiveness:** Beutler, Edwards & Someah (2018), [10.1002/jclp.22682](https://doi.org/10.1002/jclp.22682), **abstract read**: 13 controlled studies, 1,208 patients; high-reactance patients did better with less directive treatment (`d = .79`, confidence interval unavailable in the abstract). This supports examining the interaction between engagement and delivery, not labelling every disagreement as resistance or blaming the patient.

**Search boundary:** I did not find validation of the exact four-type split in the targeted Europe PMC title/abstract searches recorded in [`sources/targeted_search_receipts.json`](sources/targeted_search_receipts.json), or in the reviewed readiness/reactance sources. The exact typology queries returned no records; the timing/alliance/resistance query returned one unrelated adaptation study. These narrow searches are not exhaustive and cannot establish that no related typology exists anywhere.

**Delete from the scholarly argument:** claims that one type is almost nonexistent or another is the majority. No denominator or population estimate was verified. Do not reproduce stigmatizing diagnostic labels from an uncertain transcription. No raw quotations enter the public repository.

**Placement:** the same patient/context subsection, with the clinical heuristic explicitly introduced as an informal perspective. Cite the evidence for related constructs separately so that citations do not appear to validate the four types.

## 3. Relationship, communication and feedback

- **Alliance:** Flückiger et al. (2018), [10.1037/pst0000172](https://doi.org/10.1037/pst0000172), **abstract and full-text definition/causality discussion read**. Alliance comprises agreement about goals/tasks and a therapeutic bond. The synthesis covered 295 studies and more than 30,000 patients; the face-to-face alliance–outcome association was `r = .278 [.256, .299]` (95% confidence interval). This is an association across modalities, not proof that alliance causes all improvement.
- **Direction of influence:** Flückiger et al. (2020), [10.1037/ccp0000594](https://doi.org/10.1037/ccp0000594), **abstract read**. An individual-participant-data meta-analysis of 17 studies/5,350 participants found reciprocal session-by-session relationships between alliance and symptoms during the first seven sessions. Retain reverse causation and time-varying confounding as limitations of a causal interpretation.
- **Rupture repair:** Eubanks et al. (2018), [10.1037/pst0000185](https://doi.org/10.1037/pst0000185), **abstract read**. Repair–outcome association: `r = .29 [.10, .47]`, 11 studies/1,314 patients. Training/supervision comparison: `r = .11 [-.09, .30]`, six studies/276 trainees or supervisees, not a significant outcome benefit. Do not present the first estimate while hiding the second.
- **Feedback-informed adaptation:** Delgadillo et al. (2018), [10.1016/S2215-0366(18)30162-7](https://doi.org/10.1016/S2215-0366(18)30162-7), **abstract read**. Cluster-randomized trial, 77 participating therapists and 2,233 patients; not-on-track patients had lower symptoms with feedback (`d = .23` for depression and `.19` for anxiety). The corresponding adjusted scale-score differences and intervals are in the source notes. This tests structured outcome feedback, not every possible informal therapeutic “probe.”

**Placement:** expand `latex/sections/14-delivery.tex` without duplicating the existing alliance claim. Add a short paragraph about rupture repair, feedback and the distinction between relational timing and component sequence.

## 4. Timing: a plausible clinical concern, not a universal empirical rule

The proposition that a correct reframe can be unhelpful before the person feels understood is clinically plausible. The evidence above supports attention to alliance and directiveness, but does not directly establish the narrower causal claim “early restructuring causes resistance because alliance is not ready.” I did not find a direct test of that exact interaction in the targeted search and sources checked here.

The available component-sequence trials also cut against an unconditional experience-first rule:

- Krause et al. (2022), [10.1177/01454455221075754](https://doi.org/10.1177/01454455221075754), **full-text methods/results read**: 93 participants with claustrophobic fear; restructuring before versus consolidation after exposure yielded no detected difference in outcomes through one month. Cognitive content as well as sequence differed, so this is not a pure order-only contrast or an equivalence trial.
- Johnco et al. (2025), [10.1037/ccp0000953](https://doi.org/10.1037/ccp0000953), **abstract read**: 249 adults with elevated public-speaking anxiety; both behavioural experiments and restructuring before exposure improved outcomes more than exposure without explicit expectancy processing. The small, non-significant anxiety difference favoured behavioural experiments, which also produced greater expectancy change in a shorter session. Follow-up was one week, not a long-term clinical test.

**Conclusion for the thesis:** communication, alliance and timing may condition how a cognitive technique works; they do not show cognition is useless. “Experience first, cognition consolidates” remains, at most, a scoped hypothesis. Do not assume that all change must first occur in conscious feeling.

## 5. Deliverables and verification

1. Add the short patient/context subsection and delivery paragraph; update objections and the evolutionary subsection consistently.
2. Add only the five genuinely new, cited clinical references to `deep-research/references.bib`; existing Hayes, alliance and feedback references remain canonical.
3. Record reading levels and caveats in [`deep-research/sources/clinical-engagement.md`](../../deep-research/sources/clinical-engagement.md); retain retrieval receipts and public metadata separately from private or copyrighted reading copies.
4. Save a source-linked paragraph in `blog_paragraph.md` using the same evidence/hypothesis distinction; do not publish it to the website.
5. Include all additions in the requested single Claude Fable/max light review, fix findings, rebuild and inspect the PDF, then commit and push to `main`.

**TLDR-end:** [meta-review-cbt: clinical goals and timing] Ground the clinician's useful points in acceptance, alliance, reactance and feedback research. Keep the four-way heuristic non-diagnostic and unvalidated, omit unsupported prevalence claims, and retain the evidence that cognitive techniques can help before experience.
