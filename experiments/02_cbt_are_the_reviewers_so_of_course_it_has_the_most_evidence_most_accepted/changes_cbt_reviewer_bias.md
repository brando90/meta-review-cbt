# Evidence volume, allegiance and reviewer bias: manuscript revision plan

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/experiments/02_cbt_are_the_reviewers_so_of_course_it_has_the_most_evidence_most_accepted/changes_cbt_reviewer_bias.md>

**TLDR:** Include the evidence-selection critique in the main text, but distinguish demonstrated publication bias and researcher allegiance from the unverified claim that CBT-oriented reviewers suppress alternatives. More studies do not establish comparative superiority or identify an active component; neither bias nor the absence of a detected difference establishes that all therapies are equivalent.

Date: 11-08-2026. Target: `latex/sections/07-evidence.tex`, with a short counterweight in `16-objections.tex`. This is a targeted revision plan, not a new systematic review. Implemented in Draft 4; see the [single-review resolution record](../../review/LIGHT_QA_DRAFT4.md).

## 1. Scope of the claim

The motivating question is whether the prominence of cognitive behavioral therapy (CBT) partly reflects how evidence is produced, submitted, selected and interpreted. This is a legitimate methodological question. The stronger explanation—CBT has the largest evidence base *because* most reviewers favour CBT—requires evidence about reviewer composition and decisions, not just a count of trials or a researcher-allegiance correlation.

Separate five claims:

| Claim | Decision |
|---|---|
| A large evidence base alone proves superiority to every credible alternative. | Reject the inference. Comparative efficacy needs appropriate head-to-head evidence and its uncertainty. Evidence volume can still increase confidence when the studies are rigorous. |
| Researcher allegiance is associated with reported comparative outcomes. | Supported across psychotherapy research. Describe allegiance as investigators' preference for a treatment, not reviewers' orientation. |
| Published psychotherapy trials can overstate effects because results are selectively available. | Supported in the checked depression literature; do not generalize a single numerical correction to every disorder or CBT trial. |
| Peer reviewers can favour positive results. | Direct experimental support exists outside psychotherapy; retain the domain boundary. |
| CBT-oriented reviewers are the reason alternatives receive less acceptance. | Not established by the sources read here. Keep as a hypothesis requiring a different study design, not as a reported result. |

## 2. Verified evidence, including the inconvenient parts

Detailed notes and source levels: [`deep-research/sources/evidence-selection.md`](../../deep-research/sources/evidence-selection.md). DOI metadata were checked through Crossref. Numbers below come from the cited abstract or full text, not search summaries.

### Researcher allegiance

- **Munder et al. (2013)**, [10.1016/j.cpr.2013.02.002](https://doi.org/10.1016/j.cpr.2013.02.002), **abstract read**: 30 meta-analyses; mean allegiance–outcome association `r = .262`, with primary-study overlap controlled. The abstract reports `p = .002` and heterogeneity `I² = 28.98%`; it does not provide a confidence interval. Use the qualitative association in the paper rather than a headline estimate without its interval. This association is not itself a randomized demonstration of bias; actual efficacy, expertise, implementation and study design may contribute.
- **Zimmerman & Marcus (2024)**, [10.1002/cpp.2974](https://doi.org/10.1002/cpp.2974), **abstract read**: a quasi-experimental analysis compared 19 pairs of studies with the same treatments/disorder but opposing allegiances; 10 pairs showed patterns consistent with allegiance bias. This strengthens the concern but does not quantify reviewer bias or establish a universal causal correction. Keep in the evidence notes; it need not enlarge the main-text bibliography.
- **Tolin (2010)**, [10.1016/j.cpr.2010.05.003](https://doi.org/10.1016/j.cpr.2010.05.003), **abstract read**: 26 studies, 1,981 participants. CBT exceeded psychodynamic therapy, not interpersonal or supportive therapies; the abstract reports a CBT advantage after adjustment for investigators' self-reported allegiance. Retain as counterevidence to “all apparent advantages disappear after bias adjustment.” Do not turn this older, heterogeneous synthesis into universal CBT superiority.

### Publication selection

- **Driessen et al. (2015)**, [10.1371/journal.pone.0137864](https://doi.org/10.1371/journal.pone.0137864), **full-text methods, results, Table 2, reasons for non-publication and discussion read**: 13 of 55 initiated National Institutes of Health-funded grants/trials did not lead to publication (23.6%; source-reported binomial 95% interval 13–37%). In the control comparisons, adding six unpublished studies to 20 published studies changed Hedges' standardized mean difference from `g = 0.52 [0.37, 0.68]` to `0.39 [0.08, 0.70]`. The reported 25% decrease is a point-estimate change; the between-publication-status comparison was not conventionally significant (`Q = 3.34`, one degree of freedom, `p = .07`). Psychological treatment remained efficacious in the pooled control comparison.
- **Important correction to the reviewer explanation:** of the 13 unpublished studies in Driessen, **two were known to have been submitted and rejected, six were never submitted, and submission status was unclear for five**. Non-publication cannot be equated with rejection by CBT reviewers. This finding belongs in the manuscript, not only in these notes.
- **Cuijpers et al. (2010)**, [10.1192/bjp.bp.109.066001](https://doi.org/10.1192/bjp.bp.109.066001), **abstract read**: 117 trials, 175 comparisons; a statistical adjustment changed an effect estimate from 0.67 to 0.42 with 51 imputed studies. These were **imputed**, not 51 discovered unpublished trials. Prefer Driessen's recovered-study evidence in the new main paragraph and retain this distinction in the notes.

### Peer review and the “gold standard” debate

- **Emerson et al. (2010)**, [10.1001/archinternmed.2010.406](https://doi.org/10.1001/archinternmed.2010.406), **abstract read**: randomly assigned orthopaedic-journal reviewers evaluated positive or no-difference versions of a fabricated trial; 210 of 238 returned reviews. Publication recommendations favoured the positive version (97.3% versus 80.0%). This is direct evidence of positive-outcome bias in that setting, **not evidence of CBT reviewers rejecting psychotherapy alternatives**. The paper can state the directional result without exporting its rate to psychotherapy.
- **Leichsenring et al. (2018)**, [10.3389/fpsyt.2018.00159](https://doi.org/10.3389/fpsyt.2018.00159), **abstract and full-text argument read**: a critical position on “gold standard” language and psychotherapy pluralism. Treat it as an argument supported by underlying literature, not an independent empirical estimate of reviewer suppression. No need to multiply opinion citations in the manuscript.
- **Mahoney (1977)**, [10.1007/BF01173636](https://doi.org/10.1007/BF01173636): title/authors/year verified, but the Crossref/Europe PMC requests supplied no abstract, and the publisher article/PDF routes returned challenge pages. **Not content-verified; do not cite its purported findings.** A famous title or secondary quotation is not an adequate replacement.

## 3. Main-text placement and wording

Add a subsection titled **“Evidence volume, allegiance and reviewer selection”** in `07-evidence.tex`, after the existing control/bias discussion and before temporal trends. It belongs in the main evidence argument because it limits the interpretation of the whole review, not in an appendix as a rhetorical aside.

Its sequence:

1. Distinguish evidence volume, comparative efficacy and component causality.
2. Introduce researcher allegiance with its observational limitation.
3. Retain Tolin's counterevidence and the existing disorder-specific CBT advantages.
4. Explain why the Driessen non-submission findings do not establish editorial gatekeeping.
5. Cite the peer-review experiment with its orthopaedic scope explicitly stated.
6. State that CBT-specific reviewer preference is unresolved and name the direct evidence needed.

Revise the existing Driessen sentence to include the grant/trial denominator, point estimates and intervals instead of treating the 25% decrease as a universal correction. Avoid repeating the entire numerical result in the new subsection.

Add one objection in `16-objections.tex`: selection and allegiance concerns do not invalidate efficacy evidence, apply to rival therapies as well, and do not prove equivalence. Keep package efficacy separate from the causal contribution of cognitive restructuring.

## 4. How to test the reviewer hypothesis

A direct test would require reviewer orientation measured independently of their decisions, comparable manuscript quality, and either randomized manuscript content/labels or a credible adjustment strategy. Submission and editorial records are needed to distinguish non-submission, desk rejection, review recommendations and final editorial decisions. Author preference, treatment credibility, therapist competence, control choice and result direction are distinct variables.

Possible safeguards to recommend, rather than claim as completed here: prospective registration, complete results reporting, appropriate active comparators, transparent component definitions, balanced expertise, independent replication and review procedures that reduce selection by outcome. These safeguards should apply to all therapeutic orientations.

## 5. Integration and acceptance criteria

- Do not add a new established failure category; qualify the existing bias reason and evidence-quality discussion.
- Keep the raw context files intact; do not reproduce private correspondence, names of private sources or transcripts.
- Add only cited and content-checked references to the central bibliography; keep excluded/unused candidates explicit in the notes.
- Include this entire addition in the **same single requested Claude Fable/max light review** as the evolutionary and clinical additions; fix findings and rebuild before publication.
- Commit the plans, evidence records, sources and fresh manuscript PDF, then push directly to `main` after fetch and verification.

**TLDR-end:** [meta-review-cbt: evidence-selection revision] Include the documented selection and allegiance problems without claiming an unmeasured CBT-reviewer conspiracy. The strongest supported argument concerns how much confidence particular comparisons warrant, not whether every positive CBT result is invalid.
