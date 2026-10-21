# deep-research

Literature search for the review: about 300 sources, every one resolved through Crossref, every quoted number read from the abstract or full text.

- `references.bib`: the single bibliography used by the paper (merged and de-duplicated by DOI; very long author lists truncated for the BibTeX buffer).
- `sources/`: one notes file and one `.bib` per search slice. Each notes file opens with a 10-line synthesis and then lists, per source: key, DOI, design, headline numbers quoted from the abstract, how it bears on the thesis (supports, complicates or against), and a VERIFIED or PARTIAL flag.
  - `efficacy.md`: CBT efficacy, bias, control-group effects, effect-size trends, head-to-head and component comparisons.
  - `mechanisms.md`: dismantling and component studies, exposure and inhibitory learning, mediators, ACT, mindfulness, metacognitive therapy.
  - `ef.md`: executive function and CBT outcome, stress and the prefrontal cortex, reappraisal under stress and load, attentional control theory, the origin of the ``off-line'' claim.
  - `adhd.md`: CBT, medication and mindfulness in adult ADHD, executive function in ADHD, anxiety-ADHD comorbidity.
- `protocol.md`: how sources are found and verified. `VERIFICATION.md`: the log.

Rules of thumb: PARTIAL sources are not used for numbers; some notes contain items marked UNVERIFIED that are deliberately absent from the `.bib`.
