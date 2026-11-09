# Draft 4.1: clinical-feedback refinements implemented

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/experiments/03_clinical_goals_engagement_and_timing/clinical_feedback_revision.md>

**TLDR:** Draft 4.1 distinguishes intellectual understanding from emotional and behavioural change, communication format from mechanism, and final-phase cognitive consolidation from a universal treatment sequence. The feedback motivates these distinctions; published evidence supplies the bounded claims, not proof of brief strategic therapy's efficacy or cognitive restructuring's irrelevance.

Date: 11-08-2026. Baseline: `cdd8a727c4e0a069642f8de84007c7b421ad6539`. Canonical manuscript: [`latex/main.pdf`](../../latex/main.pdf).

## Scope and provenance

This follow-up revisits existing informal clinical input. The manuscript retains the attribution “a practicing clinician's perspective, shared informally with the author,” with no clinician identity, private correspondence, personal health information or raw transcript published. Original input and access receipts remain in ignored private storage.

All ten proposed reasons cognitive behavioral therapy (CBT) may fail remain in the taxonomy. Executive function and adult attention-deficit/hyperactivity disorder (ADHD) remain the deepest case study. This is a targeted critical review, not a completed systematic review, new participant experiment or newly pooled treatment-effect analysis. The separately maintained blog was not changed.

## Disposition of the clinical points

| Clinical point | Revision or existing coverage | Evidence boundary |
|---|---|---|
| Intellectual understanding may coexist with threat and avoidance | Added a formulation paragraph in `13-patients.tex`; added separate measures in `17-agenda.tex` | A clinical question, not a prevalence estimate, diagnosis or proof of a separate non-cognitive system |
| Experience can support subsequent understanding | Retained the learning hypothesis and added the communication-format distinction in `15-mechanism.tex` | Experience-based language does not establish an exclusively subcortical mechanism |
| Verbal delivery need not mean reasoning alone; action can change expectations | Added a dedicated paragraph in `15-mechanism.tex` and linked the existing behavioural-experiment comparison | Format does not identify a causal mechanism; the verbal-reframing claim remains a clinical proposal |
| Johnco's component comparison | Retained the balanced result in `08-ingredients.tex` and the timing discussion; reread its abstract | Both expectation-addressing approaches exceeded exposure without explicit expectancy processing. The anxiety difference favouring behavioural experiments was small and non-significant; follow-up was one week, not a demonstration of durable superiority |
| Behavioural activation in the COBRA trial | Existing `08-ingredients.tex` account retained | Non-inferiority applies to the specified depression outcome and margin; packages and workforces differ, so this is not an isolated cognitive-component or neural-mechanism test |
| A corrective experience need not destroy earlier threat learning | Added the competing-learning account in `15-mechanism.tex`; inspected relevant Craske author-manuscript passages | Describes an inhibitory-learning framework, not an exclusive established mechanism of all psychotherapy |
| Introduce a change, attend to feedback and adapt | Existing `14-delivery.tex` coverage retained | Evidence for a structured feedback intervention does not validate every informal therapeutic probe or the precise early-reframing hypothesis |
| Thought control can backfire | Added the suppression meta-analysis and an explicit distinction from restructuring in `15-mechanism.tex` | Suppression rebound is not evidence that cognitive restructuring causes rebound |
| Cognitive consolidation can follow experiential change, with earlier reframing also possible | Added the proposed final-phase sequence in `14-delivery.tex` and follow-up measurement in `17-agenda.tex` | Consolidation after one exposure and consolidation near the end of therapy are different timing questions; neither universal sequence is established by the cited trials |
| Whether manualisation is generally superior | Replaced the broad sentence in `14-delivery.tex` with the direct/indirect evidence split | None of six direct comparisons supported superiority, but three of eight indirect meta-analyses did; retain both, without inferring equivalence |
| Package efficacy does not identify the component responsible | Existing component and mechanism discussions retained | Behavioural procedures can alter expectancies; effective components do not directly validate brief strategic therapy as a package |
| Improvement, common factors, placebo comparisons and harms | Existing `07-evidence.tex`, `12-nonresponse.tex` and `15-mechanism.tex` coverage retained | These sources were not comprehensively rechecked in this follow-up; the manuscript retains efficacy counterevidence and uncertain harm attribution |
| Emotional intensity is not therapeutic success by itself | Made explicit in `15-mechanism.tex` and `17-agenda.tex` | Measure avoidance, functioning and persistence outside sessions, not only a compelling experience or explanation |
| Historical exposure antecedents and a specific acceptance-integrated exposure example | Not added | No primary historical source or specific integrated-treatment study was checked for those details in this follow-up; they are not necessary to the distinction between procedure and mechanism |

Historical mechanism and delivery notes were also aligned with these interpretation limits. The previously checked alliance and format abstracts were reread before removing residual universal-equivalence and therapist-level causal wording from those notes; this does not expand their prior reading inventory or revalidate every historical source.

## Source checks and reproducibility

- **Two existing references newly recorded in this targeted inventory:** Abramowitz et al. (2001), [10.1016/s0272-7358(00)00057-x](https://doi.org/10.1016/s0272-7358(00)00057-x), and Truijens et al. (2019), [10.1002/jclp.22712](https://doi.org/10.1002/jclp.22712). Crossref identities checked and abstracts read; no full-text reading claimed. Both were already in the 458-entry bibliography. Abramowitz is newly cited in the manuscript.
- **One reading-level extension:** Craske et al. (2014), [10.1016/j.brat.2014.04.006](https://doi.org/10.1016/j.brat.2014.04.006). Read the author-manuscript discussion of inhibitory learning, expressed fear versus learning, expectancy violation and consolidation. The text was obtained through the National Center for Biotechnology Information (NCBI) BioC service after the XML route failed and public HTML returned a browser challenge. This is relevant-passage reading, not a full-paper or final-publisher-PDF check.
- **Version qualification:** the BioC document identifies the DOI, title and authors and labels the copy an author manuscript. Its title metadata reports 2015; Crossref dates the journal publication to July 2014. The bibliography keeps the journal year.
- **Counterevidence preserved:** Craske's recommendation to move cognitive questioning after exposure is a framework-based recommendation, not a universal result. Johnco and Krause remain the relevant later timing constraints.
- **Current combined inventory:** 45 candidate identities; 44 abstracts read, comprising 33 abstract-only and eleven with relevant full-text passages; one metadata-only excluded candidate. This is not fresh verification of all 458 bibliography entries.

The source URL, raw-response hash and extraction description for Craske are in the evolutionary folder's `sources/metadata_receipts.json`; the reading-copy hash is in `sources/reading_receipts.json`. Its BioC text extraction is reproducible from the repository root after saving the identified response in the ignored reading-copy folder:

```python
import json
from pathlib import Path
cache = Path("experiments/01_1st_principles_evolutionary_argument_against_cbt/_build/sources")
raw = cache / "craske2014maximizing.feedback.bioc.json"
document = json.loads(raw.read_text())[0]["documents"][0]
assert document["id"] == "4114726"
assert document["passages"][0]["infons"]["article-id_doi"] == "10.1016/j.brat.2014.04.006"
text = "\n\n".join(p["text"] for p in document["passages"] if p.get("text")) + "\n"
(cache / "craske2014maximizing.fulltext.txt").write_text(text)
```

The two additional abstracts were retrieved with the existing `retrieve_one` function in [`retrieve_sources.py`](../01_1st_principles_evolutionary_argument_against_cbt/scripts/retrieve_sources.py). Their explicit reading decisions were then added to the shared exporter. Running that exporter or the consistency checker does not establish that a source has been read.

## Publication

Published directly to `main` in [`a116b916d50b10919ce95f7449ea4d7334a51c89`](https://github.com/brando90/meta-review-cbt/commit/a116b916d50b10919ce95f7449ea4d7334a51c89). The remote revision and pinned PDF were verified on 11-08-2026 at 20:00 PST; downloaded PDF bytes match the checked local artifact.

[Immutable Draft 4.1 PDF](https://github.com/brando90/meta-review-cbt/blob/a116b916d50b10919ce95f7449ea4d7334a51c89/latex/main.pdf). This revision has not been emailed to a collaborator; the earlier Draft 4 delivery record remains unchanged.

## Verification and remaining limits

- `make test`: thirteen unit tests pass; companion source/receipt checks pass.
- Manuscript consistency: 458 bibliography entries, 266 cited keys, 20 labels and 45 source records; zero undefined citations/references and zero citation gaps.
- `make paper`: successful 64-page build, 414,929 bytes. SHA-256: `8805e2b644dd3255f392fc9ee89c2df006e9ca8781df1a8da652f4476006781a`.
- The title page says **“Draft 4.1: for feedback, not submitted.”** The ten-reason table remains on page 6; references begin on page 32. No `??` markers or embedded files were found.
- The build retains a 2.61108-point output-box warning and underfull bibliography boxes; these are not undefined references or build failures. Selected-page rendering checks are recorded privately with the build receipts.
- The clinical sequence remains a hypothesis. Emotional responding, intellectual understanding, avoidance and functioning need distinct measurements and follow-up before a sequence can be judged effective.
- Google companion synchronization remains pending; the exact unapplied update is saved locally. Submission preparation and any further collaborator sending remain separate work.

**TLDR-end:** [meta-review-cbt: clinical-feedback revision] Draft 4.1 implements the clinical refinements without overclaiming mechanisms or treatment superiority. The manuscript, source notes and reading receipts distinguish supported findings from clinical proposals and retain counterevidence.
