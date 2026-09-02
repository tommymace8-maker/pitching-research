# 2026-09-02 — PITCH SEQUENCING, PREDICTABILITY AND HITTER ANTICIPATION

**Topic selected because it is the largest named coverage gap in the corpus.** `INDEX.md` §5 lists "Pitchability, sequencing and in-game usage" as a README research priority with **nothing** written on it, and F-163 (tunneling is over-sold) left the sequencing question dangling: if tunnels are not the mechanism, what is?

**Population scope:** elite, 85 mph floor. Off-population samples flagged `SAMPLE MISMATCH — directional only`.

---

## ⚠️ RUN CONDITION — READ THIS BEFORE YOU READ ANYTHING ELSE

**ALL DIRECT EGRESS WAS BLOCKED FOR THIS ENTIRE CYCLE. ZERO SOURCES WERE READ AT SOURCE.**

`WebFetch` and raw `curl` both returned `EGRESS_BLOCKED` / `CONNECT tunnel failed, response 403` for **every domain attempted**, including every domain the run brief lists as working:

| Domain attempted | Result |
|---|---|
| `tangotiger.net` (Kovash & Levitt PDF) | BLOCKED |
| `www.nber.org` | BLOCKED |
| `journals.sagepub.com` | BLOCKED *(listed as WORKING in the brief)* |
| `www.frontiersin.org` | BLOCKED *(listed as WORKING)* |
| `pmc.ncbi.nlm.nih.gov` | BLOCKED *(listed as WORKING)* |
| `www.ncbi.nlm.nih.gov/pmc` | BLOCKED *(listed as WORKING)* |
| `arxiv.org` | BLOCKED |
| `papers.ssrn.com`, `asu.elsevierpure.com` | BLOCKED |
| `example.com` (control, via curl) | BLOCKED |

`WebSearch` worked. Nothing else did. **The egress allowlist in the run brief is stale.**

**Consequence, stated in the program's own language: every number in this brief is SNIPPET-LEVEL. Not one is a finding. They are all leads.** This is precisely the condition under which the 2026-08-19 extension cycle ran, and that cycle required the 2026-08-20 verification pass to fix two misreads. **Assume the same failure rate here.** A verification pass is queued as F-258 and is the first item of tomorrow's work.

Where a snippet quoted a study's own abstract language closely enough to reproduce p-values, units and trial counts, I say so — that raises confidence that the *number* was transcribed correctly. It does nothing for whether the *sentence* around it is right, which is the error mode this program actually suffers from (F-240).

---

## 0. The question, posed properly

Coaches sequence. Every college staff in the country has a pitch-calling philosophy. The corpus has **never asked whether any of it survives contact with evidence**, and it inherited a warning from the tunneling work: an entire metric suite (Baseball Prospectus 2017) shipped with **no outcome validation at all**, and when someone finally tested it against run values the correlation was r = 0.07 (F-163).

So: **is the ORDER of pitches a lever, a marker, or neither?**

Three sub-questions, kept separate on purpose, because the industry collapses them:

1. **ORDER** — does pitch *n−1* change the outcome of pitch *n*? ("Set him up with the fastball to get him with the slider.")
2. **PREDICTABILITY** — does the hitter's ability to *anticipate* pitch *n* change its outcome, regardless of what preceded it?
3. **MIX** — does the overall usage distribution (arsenal breadth, best-pitch usage rate) change outcomes?

**These have different answers, and the folklore is built entirely on (1), which is the one with the weakest support.**

---

## 1. THE ONLY EXPERIMENTAL MANIPULATIONS THAT EXIST — and they disagree

This is the whole reason this topic is worth a day. Sequencing research is overwhelmingly observational, for an obvious reason: you cannot randomize a major-league pitch call. But **two laboratory studies actually manipulated the sequence and measured hitter performance.** They reached opposite conclusions.

### 1a. Kashiwabara et al. (PLOS ONE, 2020) — sequence null, advance-information positive

*"Does the combination of different pitches and the absence of pitch type information influence timing control during batting in baseball?"* PLOS ONE 15(3):e0230385; PMID 32182276; PMC7077830.

**Design — and this is a real manipulation, not an observation:**
- **n = 26 high-school baseball players.** `SAMPLE MISMATCH — DIRECTIONAL ONLY.` These are hitters, not pitchers, so the 85 mph floor does not apply the same way — but their skill level bounds how much anticipation machinery is available, and HS hitters are not SEC hitters.
- Pitching machine. **Fastball 34.3 ± 1.3 m/s = 76.7 ± 2.9 mph.** Curveball 25.4 ± 1.0 m/s = **56.8 mph.** Slowball 25.5 ± 0.9 m/s = **57.0 mph.**
- **Three conditions:** *Continuity* (same pitch type five times consecutively, 15 trials); *Random* (pitch type not conveyed, 30 trials); *Open* (next pitch type told to the hitter in advance, 20 trials).
- Outcome: **timing error**, computed from the difference between measured impact location (ball position relative to the batter's body at ball–bat impact) and optimal impact location.

**Results:**
- **The (n−1)th pitch type did NOT affect impact timing. p = 0.338.**
- **Timing errors were lower in Open than in Random. p < 0.001.**

**Read that pair carefully, because it is the finding of the day.** Telling the hitter what is coming helped him a great deal. Telling him *by means of the previous pitch* helped him not at all. **The information channel that sequencing folklore assumes exists — "the last pitch sets up the next one" — did not carry information in this experiment.** What carried information was simply *knowing*.

**The authors' own stated implication** (snippet-level, close paraphrase of their conclusion): having **two or more pitch types**, **reducing fluctuation of the pitching motion**, and **similar early ball trajectory between different pitch types** are what increase a hitter's timing errors. **Note what is absent from that list: the order.**

**What the biomechanist says about this study before anyone quotes it.**
- A **pitching machine has no delivery.** There are no arm-slot, hand, or torso cues to read. This *strengthens* the sequence null in one direction — the sequence channel was tested in isolation, unpolluted — and *weakens* the generalization in another: against a real pitcher, expectancy may be built from delivery cues that a machine cannot provide, and the sequence may interact with those.
- **Timing error is not an outcome.** Nobody measured whiffs, exit velocity, or run value. A timing effect too small to move impact location could still move contact quality.
- **A 57 mph "curveball" against a 77 mph fastball is a 20 mph gap** — far larger than an elite arsenal's typical fastball-to-breaking-ball gap. Large gaps make pitch type easy to identify late, which may *suppress* the sequence effect by making anticipation unnecessary.
- **n = 26, and "Continuity" is a strange operationalization of sequencing** — five of the same pitch in a row is not what a coach means by a sequence.

`CAUSALITY: INTERVENTION (hitter-side; sequence manipulated).`
`VERIFICATION: SNIPPET-LEVEL. Not read at source. PLOS ONE is open access and this is the single highest-priority verification target in the corpus right now.`

### 1b. Gray (2002) — sequence POSITIVE, and it is the older, smaller study

Two companion papers, same author, same year:
- Gray R. (2002). *"Markov at the Bat": A Model of Cognitive Processing in Baseball Batters.* **Psychological Science 13(6):542–547.** PMID 12430839.
- Gray R. (2002). *Behavior of College Baseball Players in a Virtual Batting Task.* **Journal of Experimental Psychology: Human Perception and Performance 28(5):1131–1148.** PMID 12421060.

**Design:** VR batting simulation. **n = 6 experienced college baseball players** (Psych Science paper). A **two-state Markov expectancy model** — the batter switches between expectancy states under a set of transition rules; the probability he expects a given pitch is computed **from the types of the previous three pitches**, and that probability predicts swing accuracy.

**Results (snippet-level):** the model **fit the hitters' performance well**; **the history of the previous three pitches and the pitch count both had significant effects on accuracy**; and **estimated model parameters correlated highly with playing level.**

**This is a direct contradiction of 1a on the central question.** Gray found previous-3-pitch history moved swing accuracy. Kashiwabara found previous-1-pitch type did not move timing error.

**Reconciliations that are actually available, in order of plausibility:**
1. **Depth of history.** Gray modeled *three* prior pitches building an expectancy *state*; Kashiwabara tested *one* prior pitch. An expectancy that takes three pitches to build is invisible to a lag-1 test. **This is the most likely reconciliation and it is testable.**
2. **Skill level.** n = 6 college vs n = 26 high school. Gray's own result — parameters correlate with playing level — says **the expectancy machinery gets stronger with skill.** If so, the HS null is uninformative about SEC hitters, which is exactly the population Tommy's pitchers face. **This possibility alone forbids quoting the PLOS null to a college pitcher as settled.**
3. **Outcome measure.** Swing accuracy (Gray) vs impact-location timing error (Kashiwabara).
4. **Apparatus.** VR with a rendered pitcher (delivery cues present) vs machine (absent).

**And what the biomechanist says about Gray:** **n = 6.** A two-state Markov model with free parameters fit to six subjects will fit almost anything; "good fit" is not a hypothesis test, and "highly correlated with playing level" across six people is a correlation with roughly four degrees of freedom. **Neither of these studies is strong. They are simply the only two that exist.**

`CAUSALITY: INTERVENTION (hitter-side, simulated).`
`VERIFICATION: SNIPPET-LEVEL. Sample size and design descriptions come from search summaries only — and note operating rule (D): this corpus has already been burned by a search summary manufacturing a phantom n (F-242).`

---

## 2. THE LARGE-N OBSERVATIONAL RECORD — and it converges on "order does not carry much"

### 2a. 12.4 million pitches: sequence diversity is not associated with performance

**"Structure of Pitch-Pattern Motifs in Major League Baseball."** arXiv:2601.11904; published in the **Journal of the Korean Physical Society** (Springer, DOI 10.1007/s40042-026-01641-5).

- **~12.4 million Statcast pitch records, 2008–2025 MLB regular seasons.** This is, by a wide margin, the largest sequencing dataset ever analyzed in public.
- Macroscale: **Shannon entropy** and **inverse Simpson index** of motif usage, tested against **ERA and wins**. Microscale: **hit vs out frequencies across pitch-pattern motifs.**

**The authors' own conclusion, close to verbatim from the abstract:** motif-based sequence diversity at pitcher level, as quantified by Shannon entropy, **"exhibits less decisive association with conventional performance measures such as ERA or wins"**; and **"the most highly ranked motifs do not contribute to discriminating between HIT and OUT outcomes,"** indicating **"inherent limitations in using motif-based diversity measures alone as independent variables for predicting seasonal pitching performance."** What they *do* find is that motif usage is **stable and non-random, following Zipf's law**.

**So: at n = 12.4 million, sequence diversity did not predict ERA or wins, and the most common motifs did not separate hits from outs.** The structure is real and highly organized. It just did not attach to outcomes.

**Caveats the biomechanist insists on:**
- **No effect sizes were retrievable.** "Less decisive association" is the authors' phrase, not a coefficient. **Do not quote this as "r = 0" or "no association."** It is a qualitative null in an abstract.
- **This is a physics-journal paper doing statistical mechanics on baseball**, not a baseball-analytics paper. Zipf's law is the headline; outcomes are secondary.
- **Season-level aggregation destroys the effect if the effect is situational.** A sequence that works in an 0-2 count against a lefty could be real and still vanish in a pitcher's annual entropy.
- **ERA and wins are terrible dependent variables** — noisy, defense-dependent, and in the case of wins, nearly meaningless at pitcher level.

`CAUSALITY: CROSS_SECTIONAL. EVIDENCE: EMERGING at best — enormous n, weak outcome variables, no retrievable effect size.`

### 2b. Repeating a pitch is not punished

**FanGraphs Community Research**, *"The Effects of Repeating Pitches on Pitcher Success Rate."* **2023 Trackman data.**

Reported result (snippet-level): **throwing the same pitch twice outperforms the average results of sequencing in every area except fastball whiffs**, and **each pitch type is about as effective in isolation as when thrown one to three times in a row.**

**This is the empirical demolition of "never throw the same pitch twice."** It is grey literature, no sample size retrieved, no control for pitcher quality or count — but the direction agrees with 2a and with 1a.

**The confound the coach has to hold in his head, and it runs the other way:** pitchers repeat a pitch *when it is working and when the count allows it*. Selection makes repetition look good. **Nobody in this literature has controlled for that.**

### 2c. Kovash & Levitt (2009) — pitchers alternate TOO MUCH, and the paper has a serious critique attached

**Kovash K. & Levitt S.D. (2009). *Professionals Do Not Play Minimax: Evidence from Major League Baseball and the National Football League.* NBER Working Paper No. 15347.**

- **>3,000,000 pitches** (plus ~125,000 NFL play calls).
- Two claims: **(i) pitchers throw too many fastballs**; **(ii) there is negative serial correlation in pitch calling** — pitchers **alternate pitch types more than randomization would produce**, making them predictable to an opponent who notices.
- Back-of-envelope: correcting these errors is worth **"as many as two additional victories a year"** to a franchise.

**THE CRITIQUE IS AS IMPORTANT AS THE PAPER, AND THE CORPUS SHOULD CARRY BOTH.** Phil Birnbaum (*Sabermetric Research*, Sept 2009) and others argued:
- The equilibrium test is right in principle — **adjust until OPS-after-fastball equals OPS-after-non-fastball** — but **the paper did not make that comparison**; it evaluated only **pitches that ended the at-bat**, which is a biased subset.
- **OPS was reportedly computed incorrectly, undervaluing walks**, which would **inflate the apparent effectiveness of breaking pitches** — the exact direction needed to generate the "too many fastballs" conclusion.
- Game theory cannot deliver the correct proportion without assumptions that are probably wrong.

**Verdict: the SERIAL-CORRELATION result (over-alternation) is the durable half; the "throw fewer fastballs" half is contested and its magnitude should not be quoted.** Note that the over-alternation finding **agrees with 2b**: pitchers under-repeat, and repeating is not punished.

`VERIFICATION: SNIPPET-LEVEL, and the PDF host (tangotiger.net) and NBER were both blocked. The critique is also snippet-level.`

### 2d. How predictable is the next pitch, actually?

Bounding the size of the prize. Published/grey ML attempts at next-pitch prediction (snippet-level, multiple sources, **numbers come from different studies and must not be pooled**):
- **Binary fastball vs non-fastball: ~71% accuracy** in one wearable-sensor study; **3-class (fastball / offspeed / breaking): 61.3%.**
- In a per-pitcher study, **42 of 70 pitchers were predicted better than their own baseline on the binary task; only 12 of 70 on the 3-class task.**
- One XGBoost report claims **93.3% accuracy, macro-F1 0.873** on multi-class — **this is an outlier by 30 points and almost certainly reflects leakage or a per-pitcher/high-base-rate setup. Do not quote it.**
- **Feature importance consistently ranks previous pitch type among the top predictors**, alongside release speed and spin rate.

**Patrick Brennan / Baseball Prospectus** put a number on the information: **the mean information given up through sequencing is ~0.23 bits, range 0.15–0.35 bits**, and **pitchers get more predictable the further they fall behind in the count.**

**The anatomist-physiologist's translation of 0.23 bits:** with four pitch types, maximum uncertainty is 2 bits. Giving up ~0.23 bits means **the sequence resolves roughly a tenth of the hitter's uncertainty.** Real, small, and — crucially — **it says the exploitable signal lives in the pitcher's overall tendencies and count behavior, not in any individual clever two-pitch combination.**

---

## 3. TIMES THROUGH THE ORDER — the familiarity story is weaker than the corpus would have assumed

This matters for sequencing because the TTO penalty is the **only large-scale natural experiment on hitter familiarity** — and familiarity is the mechanism sequencing folklore depends on.

**The received view (Lichtman, SABR / Baseball Prospectus, data 2002–2012, Baseball Info Solutions pitch types via FanGraphs):** the TTO penalty is **familiarity, not fatigue**, and **arsenal breadth mitigates it**: pitchers who throw **mostly fastballs lose 47 points of wOBA** by the third time through, while those with **much lower fastball frequency lose only 18 points.**

**The challenge (Brill R., Deshpande S.K. & Wyner A.J., *A Bayesian analysis of the time through the order penalty in baseball*, Journal of Quantitative Analysis in Sports, 2023; arXiv:2210.06724):** after adjusting for confounders — **batter and pitcher quality, handedness, home-field advantage** — there is **little evidence of a strong discontinuity in pitcher performance between times through the order.** The authors argue existing methods **cannot disentangle continuous within-game decline from discontinuous jumps at each new time through**, and conclude that **the start of the third time through should not be treated as a special cutoff for pulling a starter.**

**This is the sharpest methodological point of the day, so state it precisely:** Brill et al. do **not** claim pitchers do not get worse as the game goes on. They claim **the jump at each new time through the order is not well supported.** That distinction is the whole ballgame, because **familiarity predicts a discontinuity** (the hitter's information resets upward each plate appearance) while **fatigue predicts a smooth decline.** If the discontinuity is not there, **the cleanest published evidence for the familiarity mechanism weakens** — and with it the strongest argument that "he's seen it already" is a large effect.

**Standing on this author:** the corpus already carries Ludwig/Brill/Wyner (arXiv:2508.19184) on xCTRL as verified-clean (INDEX §4). **Same group, same statistical posture — skeptical of effects that survive only without confounder adjustment.** That is the posture this program has adopted for itself.

**Not resolved.** Lichtman's arsenal-breadth split (47 vs 18) is a *conditional* effect and Brill et al. did not test it. **Both can be true:** no clean discontinuity overall, and a real breadth advantage. **Goes to open disputes.**

---

## 4. FIELD SWEEP — Sweep 3

### 4a. ⚠️ A CONTENT FARM HAS INVERTED THE 12.4-MILLION-PITCH PAPER. THIS IS THE CATCH OF THE DAY.

Two sites — **atsstats.com** (a sports-betting stats site) and **mkdcbaseball.com** ("Pitch Arsenal & Design Guide 2026") — are circulating this:

> "A pitcher with average stuff and elite sequencing outperforms a pitcher with elite stuff and linear sequencing."
> "Recent academic research analyzing 12.4 million Statcast pitches identifies pitch sequences as a language-like structure where the effectiveness of a pitch is defined by the pitches preceding it."

**The paper they are citing found the OPPOSITE.** The motifs paper's own abstract says sequence diversity has "less decisive association" with ERA or wins and that top motifs "do not contribute to discriminating between HIT and OUT outcomes." **The 12.4-million-pitch figure is correct; the conclusion attached to it is reversed.**

**VERDICT: DEBUNKED / MARKETING.** Add `atsstats.com` to the blocklist. **`mkdcbaseball.com` is already on it** — blocklisted in Sweep 1 (2026-08-12), which makes it a named repeat offender. Worth noting what that means: **the blocklist worked as a warning and the claim still reached this cycle anyway, through a search summary that did not name its source domain.** A blocklist filters what you read; it does not filter what a search engine paraphrases at you.

**And note the hazard class, because it is a new one for this corpus and it is not an AI hallucination.** The citation is real, the n is real, the paper is real — **and the direction is flipped.** This is *structurally identical* to correction #2 of 2026-08-13 (the changeup framing, which also inverted its source) and it is exactly what operating rule (A) exists to catch. **Anyone who checked the citation would have passed it.** Call it **DIRECTIONAL INVERSION OF A REAL SOURCE**, and it is now the most dangerous class this program faces, because it defeats citation-checking.

### 4b. Driveline "Paint Mixer" and the "buyback effect" — UNPROVEN

Driveline markets a **Paint Mixer** framework generating pitch-usage recommendations from **Arsenal+** plus other metrics, with two stated goals: **break familiar patterns hitters learn over time**, and exploit a **"buyback effect"** in which certain secondary pitches make a pitcher's primary offerings more effective.

**VERDICT: UNPROVEN.** The premise is the one thing today's evidence *does* support — usage and predictability over sequence order. But **no outcome validation of the Paint Mixer or of the "buyback effect" was found in this sweep.** This is the tunneling pattern (F-163) with a different noun: a named proprietary framework, plausible mechanism, no published test against run values. **Treat "buyback" as a hypothesis until someone publishes a number.**

### 4c. "Throw your best pitch more" vs the 2026 counter-move — GENUINELY CONTESTED, and PROMISING

- The best-pitch-more trend, exemplified: **Clay Holmes threw sinker-followed-by-sinker 365 times in the 2025 season.**
- Running against it, **Colorado in 2026 cut four-seam usage from 40.9% to 29.1%**; **Antonio Senzatela went from 57% four-seams to 37%**, redistributing into other fastball shapes. Staffs report pairing **cutters with sweepers** and **four-seams with sinkers** to change eye level.
- Also reported: **since 2021, an increase in the number of viable primary pitches per arsenal**, four-seam usage down, cutter usage up.

**VERDICT: PROMISING, and note the two trends are not actually in conflict.** "Throw your best pitch more" and "carry more distinct shapes" are both moves *away* from a balanced, alternating, predictable mix — which is the one thing Kovash & Levitt, the FanGraphs repeat study, and Brennan's entropy work all independently flag as the actual error. **The industry is converging on usage, not order. The corpus should follow.**

### 4d. Prasad (MIT Sloan, 2021) — descriptive, no outcome validation

*Decoding MLB Pitch Sequencing Strategies via Directed Graph Embeddings.* **~3.5–3.6 million pitches, 2015–2019.** Uses **Sequence Graph Transform** embeddings plus **Gaussian Mixture Model** clustering. Findings: at-bats cluster into a finite set of universal patterns; **a pitcher's sequencing strategy is distinct from his arsenal**; pitchers adjust sequence usage dynamically in-game; and the clusters contain apparent **"setup" and "knockout" pitches.**

**VERDICT: UNPROVEN — and flagged.** "Setup and knockout pitches exist in the clusters" is a **description of structure, not a demonstration of effect.** F-163 is the cautionary tale: a full metric suite published with zero outcome validation, later tested at r = 0.07. **This paper is at the same stage. Do not let "setup pitch" acquire evidential status by repetition.**

### 4e. Melville et al. (MIT Sloan, 2023) — the only normative model, and it needs command as an input

*A Game Theoretical Approach to Optimal Pitch Sequencing.* Authors: **William Melville, Jesse Melville, Theo Dawson, Delma Nieves-Rivera, Christopher Archibald, David Grisman** (BYU; also a BYU thesis, ScholarsArchive #9910).

Models the pitcher–batter matchup as a **zero-sum game**, solves for equilibrium, and proposes the **Stackelberg equilibrium** and a newly defined **"decision point equilibrium"** as sequencing strategies. Notably, it includes **a model of pitcher command/accuracy — the probability of actually hitting the target — as an input to the recommendation.**

**VERDICT: PROMISING as a framework, UNPROVEN as a result.** No outcome validation was retrievable. **But the command-as-input feature is the right idea and it connects directly to the corpus's own command work (F-171, xCTRL).** A sequencing recommendation that ignores whether the pitcher can execute the location is a recommendation for a different pitcher.

### 4f. Things I looked for and did NOT find (Sweep 3)

- **No study anywhere manipulating pitch sequence with PROFESSIONAL or D1 hitters.** The two manipulations are n = 26 HS and n = 6 college-in-VR.
- **No pitch-sequencing analysis controlling for pitcher quality** as a confound. Every observational result in this brief is contaminated by "good pitchers do X."
- **No published outcome validation of ANY commercial sequencing product** — not Paint Mixer, not any pitch-calling app.
- **No study of pitch sequencing at the college level at all.** Everything is MLB Statcast or laboratory.
- **No test of whether a pitcher can be TRAINED to be less predictable**, or whether measured predictability is stable within a pitcher across seasons. **This is the single biggest hole and it is entirely computable from existing data.**
- **No within-pitcher analysis** of whether *the same pitcher* does better in his high-entropy games than his low-entropy games. **This is the design that would answer the question, and nobody has run it.**

---

## 5. CROSS-EXAMINATION

### Challenge 1 — COACH → BIOMECHANIST
**Claim challenged:** "12.4 million pitches found no association between sequence diversity and performance, therefore sequencing does not matter."
**Why I doubt it:** the dependent variables were **ERA and wins, aggregated to a season.** I have never in my life called a pitch to lower someone's seasonal ERA. If sequencing works, it works in **0-2 against a specific hitter**, and a season-level entropy statistic would wash that out completely even if the effect were large.
**What would settle it:** run the analysis at pitch level with **run value or delta-win-expectancy** as the outcome, pitcher fixed effects, and count/batter-hand controls. Until then this is a null on a badly chosen outcome.
**BIOMECHANIST'S RESPONSE — CONCEDED, with a boundary.** The aggregation criticism is correct and I will not defend ERA/wins as endpoints. **But the microscale arm of that same paper compared hit and out frequencies at the MOTIF level and still found the top motifs did not discriminate** — that is pitch-level, not season-level, and it survives the objection. **Revised claim: sequence ORDER has not been shown to move outcomes at either the season or the motif level; whether it moves them in specific counts against specific hitters is untested and remains open.**

### Challenge 2 — BIOMECHANIST → COACH
**Claim challenged:** the coach's proposed takeaway that "unpredictability is the lever."
**Why I doubt it:** the corpus has been here before. **Unpredictability is measured as an OBSERVED distribution across a season** — that is a between-pitcher cross-sectional statistic wearing the clothes of an instruction, and it is the exact shape of stride length (F-043) and extension (F-250). **Nobody has ever manipulated a pitcher's predictability and measured what happened.** The one intervention-grade support is a **null on order** plus a **positive on advance information given verbally to a hitter** — which is not the same thing as a pitcher becoming less predictable.
**What would settle it:** a within-pitcher design — compute per-count pitch-type entropy per outing, regress outing run value on it with pitcher fixed effects. If pitchers do better in their own higher-entropy outings, the lever survives its first real test.
**COACH'S RESPONSE — PARTIALLY CONCEDED, and this is the correct challenge.** I accept that **"be less predictable" is currently a marker-shaped instruction and must not be sold as a lever.** I defend one narrower thing: **the Open-vs-Random contrast in Kashiwabara is a genuine experimental manipulation of the hitter's information state, and it was significant at p < 0.001.** That establishes **the information channel is worth something** — it does not establish that a pitcher can move his own position on it. **Those are two different claims and I will keep them separate.** The honest statement: *predictability is a variable with demonstrated hitter-side consequence and no demonstrated pitcher-side trainability.*

### Challenge 3 — ANATOMIST-PHYSIOLOGIST → COACH
**Claim challenged:** that sequencing deserves a training block at all.
**Why I doubt it:** look at what the hitter's nervous system actually has time to do. The corpus already holds that **the final third of the trajectory contributes nothing** because required angular eye velocity exceeds physiological limits, and that the usable tunnel point is **~150 ms** (F-163). Swing initiation is committed roughly **150–175 ms before contact.** So the hitter's *anticipatory* state is set **before release**, and the only thing that can update it is what the pitcher does *in his delivery and in the first ~150 ms of flight* — **not what he threw ninety seconds ago.** The mechanism you are proposing has to survive an interference interval containing an entire between-pitch reset. **The physiology favours the null.**
**COACH'S RESPONSE — DEFENDED, and this is where the anatomist overreaches.** Anticipation is not a perceptual process running inside 150 ms; **it is a prior that is loaded before the pitch and biases the whole swing decision.** Gray's Markov model is precisely a model of a state that persists *across* pitches — that is what a Markov state *is*. And the between-pitch interval is not a reset; it is **the only time the hitter has to think.** The anatomist's argument correctly kills *within-flight* sequencing effects and says nothing about *between-pitch* expectancy.
**ANATOMIST — CONCEDES the distinction, holds the magnitude.** Fair: the prior is loaded pre-pitch and I conflated two timescales. **I maintain that the effect size must be small**, because whatever the prior is, it has to compete with 150 ms of high-quality visual information about an object the hitter is staring at. **And the largest dataset ever assembled agrees with me on magnitude.**

### Challenge 4 — BIOMECHANIST → ANATOMIST
**Claim challenged:** "the physiology favours the null."
**Why I doubt it:** that is a mechanism argument used to predict an effect size, which is the move this corpus has repeatedly caught being wrong. **60% of normalized elbow torque variance is unexplained by kinematics** (standing methodological dispute) — mechanism reasoning has an unimpressive record here. Physiology tells you a channel is *narrow*; it does not tell you it is *empty*, and **p < 0.001 on the Open condition says it is not empty.**
**ANATOMIST — CONCEDED.** I was predicting a magnitude from a mechanism. Restated as a bounded claim: **the anticipatory channel is real and its bandwidth is limited by the fact that the hitter also gets 150 ms of direct evidence. That bounds the effect; it does not zero it.**

**NO MANUFACTURED CONSENSUS.** What survives all four exchanges is narrower than any single agent started with, and two disputes go to `open-disputes.md` unresolved (#17, #18).

---

## 6. WHAT ACTUALLY SURVIVES — the three-tier answer

| Sub-question | Verdict | Grade | Causality |
|---|---|---|---|
| **ORDER** — does pitch *n−1* change pitch *n*? | **NOT SUPPORTED.** One experimental null (p = 0.338), one 12.4M-pitch observational null, one grey-lit finding that repeating is not punished, one large-n finding that pitchers already over-alternate. Against: one n = 6 VR study using a 3-pitch history. | WEAK / contested | INTERVENTION (null) + CROSS_SECTIONAL |
| **PREDICTABILITY** — does anticipation change outcomes? | **SUPPORTED on the hitter side** (Open vs Random, p < 0.001). **Magnitude small in the field** (~0.23 bits given up; ~71% binary predictability at best). **TRAINABILITY COMPLETELY UNTESTED.** | EMERGING | INTERVENTION (hitter-side only) |
| **MIX** — does usage distribution matter? | **MOST SUPPORTED, LEAST COACHED.** Arsenal breadth mitigates TTO (47 vs 18 wOBA pts, contested); pitchers over-alternate and throw too many fastballs (contested magnitude); the industry is moving here on its own. | EMERGING | CROSS_SECTIONAL |

**The headline for the vault: the sequencing conversation is aimed at the weakest of its three sub-questions.** Coaches argue about order. The evidence, such as it is, sits on mix and predictability.

---

## 7. TRANSLATION — what to actually do this week with an 85+ arm

The coach's four questions were put to the other two agents above. Here is what comes out the other side, in the required form.

### THE ONE THING: audit predictability by count, not by sequence.

**So what I tell the pitcher is:** *"Nobody is beating you because of what you threw last pitch. They're beating you because in 2-0 and 3-1 you throw the fastball almost every time, and everyone in this league already knows it."*

**The drill is:** not a drill — a **20-minute data audit**, then a constraint bullpen.
1. Pull his last full season of Trackman/TrackMan-equivalent logs. Tabulate **pitch-type usage by count** (12 count buckets) and by batter handedness.
2. Find the buckets where his usage exceeds **~80% on one pitch**. Those are the leaks. Brennan's finding — predictability rises as the pitcher falls behind — says look hardest at **1-0, 2-0, 2-1, 3-1**.
3. Build a bullpen where the **catcher calls from a randomization card** constraining him to throw his second-best pitch in his two leakiest counts, at least 8 reps each. This is a **constraints-led manipulation** (F-195, F-212), not a cue.
4. Separately, and this is the part with the most experimental support: **film the delivery from centre field at 240 fps and compare the first 15 frames after release across pitch types.** Kashiwabara's authors name **"reducing fluctuation of the pitching motion"** and **"similar early trajectory between pitch types"** as the timing-error mechanisms — **and those, unlike order, are things a pitcher can actually change.**

**On video the failure looks like:** (a) a visible **difference in glove-side action or head position** between fastball and changeup in the frames *before* release — the hitter reads it, and no sequencing can recover from a tell; (b) **early trajectories that separate before 150 ms** — if the two pitches are already on different lines out of the hand, arsenal breadth is doing nothing for you; (c) in the count table, a **single cell over 85%**.

**And here's how we know it's working:**
- **The predictability metric:** per-count pitch-type usage, recomputed after the block. **A pitch-type usage rate is a proportion, so precision is governed by binomial arithmetic: to pin a usage rate to ±10 percentage points at 95% confidence you need ~96 pitches IN THAT COUNT BUCKET.** A college starter throws roughly 1,000–1,400 pitches a season spread across 12 buckets — **so you get usable estimates for the five or six most common counts only, and only over a full season.** One bullpen tells you nothing. **One month tells you nothing.** Say this out loud to the athlete before you start, or the intervention dies from an impatient read.
- **The tell check:** frame-by-frame comparison of 20 fastballs and 20 changeups. This one is fast — a systematic postural difference visible in 20 reps is a real tell.
- **The outcome check you should NOT promise:** run value. Per the corpus's own standing rules on command detection, outcome-level changes need on the order of **200+ tracked pitches** to see even a large effect, and sequencing effects are small. **Do not tell an athlete his ERA will move.**

**What NOT to do, on today's evidence:** do not build a sequencing philosophy around specific two-pitch combinations; do not tell him to avoid repeating a pitch; do not buy a pitch-calling product on the strength of "setup pitches exist in the data"; and do not quote "elite sequencing beats elite stuff" to anyone — **that sentence is a content farm inverting a paper that found the opposite.**

---

## 8. TOMORROW — three questions handed forward

1. **VERIFICATION PASS FIRST, before any new topic.** The blocked-egress condition means today produced leads, not findings. Priority order: **(a) PLOS ONE 15(3):e0230385 / PMC7077830** — confirm n = 26, the HS level, p = 0.338 on the (n−1) pitch, p < 0.001 on Open vs Random, and whether "timing error" is what this brief says it is; **(b) arXiv:2601.11904 / JKPS** — get an actual effect size for the entropy-vs-ERA relationship, since "less decisive association" is currently doing far too much work; **(c) Gray 2002** — confirm n = 6 and whether "significant effects of the previous 3 pitches" is a hypothesis test or a model-fit statement.
2. **Can a pitcher's predictability be moved, and is it even stable?** Compute per-count pitch-type entropy for MLB pitchers with 2+ seasons and report **year-over-year correlation**. If predictability is not stable within a pitcher, it is noise and this whole topic collapses. **This is computable in an afternoon from public data and nobody has published it** — same category as the release-speed-SD study the corpus already flagged as its cheapest high-value question (F-173).
3. **Does the within-pitcher design rescue sequencing?** Regress per-outing run value on that outing's per-count entropy **with pitcher fixed effects.** Between-pitcher nulls are exactly what F-094 warns are uninformative about within-athlete levers — **the corpus's own central methodological finding says the existing sequencing literature has been asking the question in the wrong direction.**

---

*Prepared 2026-09-02. Three agents: anatomy-physiology, biomechanist, pitching-coach. **Zero sources read at source — all claims snippet-level. See the run-condition banner at the top.** New findings F-251 to F-258. New disputes #17, #18. New library file `library/pitchability-sequencing.md`.*
