# Evolutionary learning: evidence-backed manuscript revision plan

**Doc link:** <https://github.com/brando90/meta-review-cbt/blob/main/experiments/01_1st_principles_evolutionary_argument_against_cbt/changes_to_paper_based_on_my_evolutionary_argument.md>

**TLDR:** Retain the evolutionary argument as motivation for testing learning and practice, not as a proof that older brain systems or behavioural therapies outperform cognitive techniques. The defensible thesis is that verbal understanding need not be sufficient for durable change, while experience, instructions and cognitive processing can interact; a universal “experience first, cognition only consolidates” sequence is contradicted by relevant evidence.

Date: 11-08-2026. Target: the critical theoretical review in `latex/`, retaining all ten reasons and the executive-function/attention-deficit/hyperactivity disorder case study. Implemented in Draft 4. The plan is retained below; completion evidence is in the [changelog](../../review/CHANGELOG.md) and [single-review resolution record](../../review/LIGHT_QA_DRAFT4.md).

## Request and boundaries

The original request was to write a scientifically referenced plan, implement it in the paper, and perform one light Claude Fable/max quality-assurance review. Truth takes priority over supporting the proposed argument. The original instruction-only file is preserved locally under ignored `_build/original_plan_request.txt`; identifying attribution is not reproduced here. Existing raw blog-context files remain unchanged. No private anecdotes or transcripts enter the manuscript or new public notes.

This is a targeted literature extension, not a systematic review or a new experiment. The companion in `evidence-screen/` remains an audit trail, not the submission manuscript. Do not infer clinical efficacy from neuronal mechanisms, animal experiments, phylogenetic age, or a therapy's branding.

## 1. The argument we can defend

1. Learning about consequences is not dependent on uniquely human verbal reasoning. Operant conditioning has been demonstrated in *Aplysia*; comparative work documents ancient vertebrate basal-ganglia organization.
2. This does **not** divide the brain into an old effective system and a new ineffective system. Prefrontal subdivisions have different evolutionary histories, and goal-directed and habitual control interact.
3. The clinically relevant question is whether a treatment changes the processes maintaining the target problem, at a tolerable cognitive cost, in contexts where the new response must work.
4. Practice may change behaviour and expectancies without explicit cognitive restructuring. Conversely, instructions and cognitive restructuring can influence learning, and rehearsal does not establish that habit formation is the operative mechanism.
5. Therefore, test component content, practice, timing and executive demand directly. Evolutionary conservation motivates such tests but cannot supply their results.

**Scoped hypothesis:** For persistent avoidance under high executive demand, structured behavioural practice may produce more durable functional change than cognitive restructuring without comparable practice. This is a hypothesis about a specified population, contrast and outcome—not an established finding or a prescription for everyone.

**Rejected stronger claim:** Behaviour changes only after feelings change, or cognition can only consolidate change produced by experience. Acceptance-based work targets acting in accordance with values despite difficult feelings, and instructed-learning and exposure-timing studies contradict an exclusively experience-first account.

## 2. Claim-by-claim evidence and inference limits

Reading levels below mean the abstract or the named full-text passages were actually read. All cited identities were checked against DOI-resolved Crossref metadata; retrieval alone is not content verification. Detailed source notes: [`deep-research/sources/evolutionary-learning.md`](../../deep-research/sources/evolutionary-learning.md).

| Proposed premise | Checked source and reading level | Manuscript decision |
|---|---|---|
| Operant learning predates human verbal reasoning. | Brembs et al. (2002), [10.1126/science.1069434](https://doi.org/10.1126/science.1069434), abstract: operant reward learning and cellular changes in *Aplysia*. | Retain as comparative evidence. Do not claim homology of every circuit or date the origin of all reinforcement learning. |
| Relevant action-selection circuitry is ancient. | Grillner & Robertson (2016), [10.1016/j.cub.2016.06.041](https://doi.org/10.1016/j.cub.2016.06.041), abstract: conserved lamprey/mammalian basal-ganglia organization. | Retain without converting evolutionary age into treatment superiority. |
| Prefrontal cortex is a recent, uniquely human addition. | Preuss & Wise (2022; online 2021), [10.1038/s41386-021-01076-5](https://doi.org/10.1038/s41386-021-01076-5), full-text abstract, evolutionary fundamentals and cortical organization. | Reject. Distinguish shared mammalian regions from later primate specializations. |
| There are just two learning systems: rewards and repetition. | Dolan & Dayan (2013), [10.1016/j.neuron.2013.09.007](https://doi.org/10.1016/j.neuron.2013.09.007), full-text definitions and system interactions; Wood & Rünger (2016), [10.1146/annurev-psych-122414-033417](https://doi.org/10.1146/annurev-psych-122414-033417), abstract. | Replace the exhaustive two-system taxonomy. Separate instrumental learning, Pavlovian learning, habitual control and deliberate goal pursuit. Repetition is a training condition, not a separate mechanism by definition. |
| Repetition necessarily creates an inflexible habit. | de Wit et al. (2018), [10.1037/xge0000402](https://doi.org/10.1037/xge0000402), abstract: five failed attempts to induce human habits by overtraining. | Reject necessity. Treat automaticity and outcome-insensitivity as different measurements. |
| Reward equals conscious pleasure; pleasure alone changes behaviour. | Berridge & Robinson (2016), [10.1037/amp0000059](https://doi.org/10.1037/amp0000059), abstract: wanting and liking are dissociable. | Reject equivalence. Do not describe dopamine simply as a pleasure signal. |
| Cognition cannot change reward learning without experience. | Li et al. (2011), [10.1073/pnas.1014938108](https://doi.org/10.1073/pnas.1014938108), abstract: instructed probabilities improved task performance; Doll et al. (2009), [10.1016/j.brainres.2009.07.007](https://doi.org/10.1016/j.brainres.2009.07.007), abstract: misleading instructions biased choices despite contrary experience. | Retain explicit counterevidence. These are laboratory findings, not proof of clinical cognitive-restructuring efficacy. |
| Reward revaluation is a demonstrated general alternative to CBT. | Ludwig et al. (2020), [10.1177/1745691620931460](https://doi.org/10.1177/1745691620931460), theoretical abstract; Taylor et al. (2021), [10.1556/2006.2021.00020](https://doi.org/10.1556/2006.2021.00020), full-text methods/results/limitations. | Present as an emerging hypothesis. Taylor has no control group; its larger naturalistic sample did not show the predicted decrease in observed eating behaviour across tool uses. It does not establish superiority to CBT or efficacy for anxiety. |
| Behavioural activation demonstrates that cognitive restructuring is never useful. | Jacobson et al. (1996), [10.1037/0022-006X.64.2.295](https://doi.org/10.1037/0022-006X.64.2.295), abstract; Richards et al. (2016), [10.1016/S0140-6736(16)31140-0](https://doi.org/10.1016/S0140-6736(16)31140-0), abstract and full-text primary outcome. | Retain narrower evidence: no detected advantage in the former; prespecified non-inferiority in the latter. Richards compares behavioural activation delivered by junior mental health workers with CBT delivered by psychological therapists, not a component alone. Neither trial proves universal equivalence or identifies a neural mechanism. |
| Exposure isolates non-cognitive change. | Hofmann (2008), [10.1016/j.cpr.2007.04.009](https://doi.org/10.1016/j.cpr.2007.04.009), abstract; Craske et al. (2014), [10.1016/j.brat.2014.04.006](https://doi.org/10.1016/j.brat.2014.04.006), abstract. | Correct the false opposition between expectancy violation and belief change. Distinguish a treatment procedure from its proposed mediator. |
| Restructuring must come after exposure. | Krause et al. (2022), [10.1177/01454455221075754](https://doi.org/10.1177/01454455221075754), full-text methods/results: no detected outcome difference between sequences, one-month follow-up; Johnco et al. (2025), [10.1037/ccp0000953](https://doi.org/10.1037/ccp0000953), abstract: restructuring before exposure and behavioural experiments both beat exposure without explicit expectancy processing, one-week follow-up. | Reject universal ordering. Preserve short follow-up, differing cognitive content in Krause, and elevated-anxiety rather than diagnosed-disorder sampling in Johnco. Retain Johnco's small, non-significant anxiety difference favouring behavioural experiments, with greater expectancy change and a shorter session. |
| Null component findings prove absence of a cognitive contribution. | Cuijpers et al. (2019; online 2017), [10.1080/10503307.2017.1395922](https://doi.org/10.1080/10503307.2017.1395922), abstract; Šipka et al. (2025), [10.1159/000542425](https://doi.org/10.1159/000542425), full-text components and outcomes. | Preserve power limits and the positive pooled component contrast. For Šipka, distinguish post-treatment benefits from non-significant follow-up contrasts and note that exposure included explicit expectancy processing. |

## 3. Terminology to keep consistent

- **Cognitive behavioral therapy (CBT):** the broad treatment family; not a synonym for cognitive restructuring.
- **Cognitive restructuring:** explicitly examining and revising interpretations or beliefs.
- **Instrumental learning:** learning relations between actions and their consequences.
- **Pavlovian learning:** learning predictive relations between events; not interchangeable with instrumental learning.
- **Habitual control:** in outcome-devaluation paradigms, responding relatively insensitive to a changed outcome value. Repeated action or low perceived effort alone does not establish it.
- **Behavioural practice:** performing target actions in relevant contexts; not automatically proof of habit formation or a non-cognitive mechanism.
- **Expectancy change:** a change in a prediction about an outcome; can follow discussion, instruction or experience.
- **Acceptance:** allowing difficult internal experiences without unnecessary attempts to eliminate them; not resignation or a claim that treatment should never reduce symptoms.

## 4. Concrete manuscript changes

| File | Change |
|---|---|
| `latex/sections/02-method.tex` | State all-ten-reasons scope; record the targeted November extension and its non-exhaustive nature; distinguish metadata from content checks. |
| `latex/sections/08-ingredients.tex` | Repair the existing inference “practice works, therefore the active ingredient is habit”; report the behavioural-activation non-inferiority margin/interval and component-study uncertainty. |
| `latex/sections/09-alternatives.tex` | Add reward-revaluation proposal with the uncontrolled-data limitation and negative naturalistic result; avoid implying mindfulness removes executive demands. |
| `latex/sections/15-mechanism.tex` | Add a main-text evolutionary-learning subsection; explain the evidence-to-hypothesis boundary and instructed-learning counterevidence; repair expectancy-versus-belief wording. |
| `latex/sections/16-objections.tex` | Update practice/exposure objections; explicitly acknowledge age does not rank therapies, cognitive timing evidence, and alliance/acceptance counterweights. |
| `latex/sections/17-agenda.tex` | Add falsifiable practice and sequencing predictions, with functional outcomes and prespecified contrasts; keep the conclusion narrower than the hypothesis. |
| `latex/main.tex` | Keep a review-draft designation; align the abstract with the qualified component claim and theoretical-review status, without turning the paper into an evolutionary-only essay. |
| `deep-research/references.bib` and source records | Add only cited, identity-checked entries; fix the Cuijpers component-review issue year while retaining the stable key. |

The reviewer-bias extension belongs in the evidence-quality argument, and the clinical perspective belongs in patient/context and delivery discussions; see the separate plans in the neighbouring experiment folders. None is an eleventh established reason for treatment failure.

## 5. What would test or weaken the hypothesis?

A proposed comparison would randomize a specified clinical population to cognitive restructuring without assigned behavioural practice, structured behavioural practice, or their combination, with comparable therapist contact and credible rationales. Ethical acceptability and adequate treatment provision would need independent clinical review before any actual study. No study is launched here.

Predefine the behavioural target, symptom and functional outcomes, follow-up, executive-function measure, adherence measures, primary contrast, clinically meaningful effect/non-inferiority margin and power calculation. Measure actual practice, expectancies and valued action rather than assuming the assigned label identifies the active process. A null result without adequate precision cannot establish equivalence.

The practice-priority claim would be weakened by a precise absence of its predicted advantage in the specified high-demand population. Added benefit from restructuring would reject the claim that it is dispensable in that setting. A timing experiment must keep cognitive content and contact comparable; existing timing studies already rule out treating experience-first ordering as a universal clinical law. Measuring mediation does not establish causation without temporal and causal assumptions.

## 6. Verification and publication sequence

1. Implement these revisions and the linked bias/clinical plans; preserve the original context inputs.
2. Run `make test`, `make screen`, `make paper`, citation checks, sentence-per-line checks and PDF text/render inspection. Keep the rebuilt `latex/main.pdf` with the source change.
3. Run **one** subscription-authenticated Claude `claude-fable-5-1` review at `max` effort covering all three additions, their citations, fairness, privacy and manuscript coherence. Resolve findings and rerun deterministic checks; no automatic second review.
4. Inspect the exact staged diff and privacy/secret checks; fetch, integrate any concurrent upstream work, commit and push directly to `main`.
5. Deliver the verified review draft to the explicitly authorized collaborator using privately verified routing. Do not describe this as journal submission or systematic-review completion.

**TLDR-end:** [meta-review-cbt: evolutionary-learning revision] Use evolutionary evidence to motivate component and learning questions, not to declare cognition ineffective. The manuscript must retain contradictory evidence, operational definitions and a testable, scoped hypothesis.
