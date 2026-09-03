# PITCHABILITY, SEQUENCING AND HITTER ANTICIPATION

**Created 2026-09-02.** Fills the coverage gap `INDEX.md` §5 listed as a README research priority with nothing written on it.
Population scope: **elite throwers, 85 mph floor.** Mission is performance development.

> ## ⚠️ VERIFICATION STATUS OF THIS ENTIRE FILE
> **Every claim below is SNIPPET-LEVEL. Nothing was read at source.** The 2026-09-02 cycle ran with all direct egress blocked — `WebFetch` and `curl` returned 403 for every domain attempted, including every domain the run brief lists as working. `WebSearch` was the only channel.
> **By this corpus's own rule these are leads, not findings.** The 2026-08-19 precedent — a snippet-only cycle that required the 2026-08-20 pass to fix two misreads — sets the expected error rate. Verification order is in F-258. **Re-read this banner before quoting anything here to an athlete.**

---

## 1. The question has three parts and the industry collapses them

This is the organizing distinction of the whole topic. Keep them apart:

| | Question | Verdict | Grade | Causality |
|---|---|---|---|---|
| **ORDER** | Does pitch *n−1* change the outcome of pitch *n*? ("Set him up with the fastball to get him with the slider.") | **NOT SUPPORTED** | WEAK / contested | INTERVENTION (null) + CROSS_SECTIONAL |
| **PREDICTABILITY** | Does the hitter's ability to *anticipate* pitch *n* change its outcome, regardless of what preceded it? | **SUPPORTED on the hitter side; magnitude small; TRAINABILITY UNTESTED** | EMERGING | INTERVENTION (hitter-side only) |
| **MIX** | Does the overall usage distribution — arsenal breadth, best-pitch usage rate — change outcomes? | **MOST SUPPORTED, LEAST COACHED** | EMERGING | CROSS_SECTIONAL |

**Coaching folklore is built almost entirely on ORDER, which is the sub-question with the weakest support.** The evidence, such as it is, sits on MIX and PREDICTABILITY.

---

## 2. The two experimental manipulations — and they disagree (F-251, F-252)

Sequencing research is overwhelmingly observational for an obvious reason: you cannot randomize a major-league pitch call. **Two laboratory studies actually manipulated the sequence.** They reached opposite conclusions, and there are no others.

### 2.1 Kashiwabara et al., PLOS ONE 2020 — order null, foreknowledge positive

PLOS ONE 15(3):e0230385; PMID 32182276; PMC7077830.

| | |
|---|---|
| Subjects | **n = 26 high-school hitters.** `SAMPLE MISMATCH — DIRECTIONAL ONLY` |
| Apparatus | Pitching machine |
| Pitches | FB **34.3 ± 1.3 m/s = 76.7 ± 2.9 mph**; CB **25.4 ± 1.0 m/s = 56.8 mph**; slowball **25.5 ± 0.9 m/s = 57.0 mph** |
| Conditions | *Continuity* — same type 5× consecutively (15 trials); *Random* — type not conveyed (30 trials); *Open* — next type conveyed in advance (20 trials) |
| Outcome | **Timing error** = difference between measured ball–bat impact location relative to the batter's body and optimal impact location |
| **Result 1** | **The (n−1)th pitch type did NOT affect impact timing. p = 0.338** |
| **Result 2** | **Timing error lower in Open than Random. p < 0.001** |

**Read the pair together.** Telling the hitter what was coming helped him a lot. Telling him *by means of the previous pitch* helped him not at all. **The channel that sequencing folklore assumes exists did not carry information in this experiment.** What carried information was simply *knowing*.

**The authors' own stated mechanisms for increasing a hitter's timing error:** two or more pitch types; **reduced fluctuation of the pitching motion**; **similar early ball trajectory between different pitch types**. **Order is absent from that list — and every item on it is something a pitcher can actually change.**

**Four limits, all of which must travel with the number.** A pitching machine has no delivery, so the expectancy channel was tested stripped of arm-slot and torso cues — clean isolation, poor generalization. Timing error is not an outcome. A 57 mph breaking ball against a 77 mph fastball is a ~20 mph gap, wider than an elite arsenal's, which may make late identification easy and suppress any sequence effect. And these are HS hitters, while §2.2 reports the expectancy machinery *strengthens* with playing level.

### 2.2 Gray 2002 — order positive, n = 6

Psychological Science 13(6):542–547 (PMID 12430839); companion in J Exp Psychol HPP 28(5):1131–1148 (PMID 12421060).

**n = 6 experienced college hitters**, VR batting task. A **two-state Markov expectancy model**: the batter switches between expectancy states under transition rules; the probability he expects a given pitch is computed **from the types of the previous three pitches**, and predicts swing accuracy. Reported: good model fit; **significant effects of the previous 3 pitches and of the pitch count on accuracy**; **model parameters highly correlated with playing level**.

**The biomechanist's standing objection:** n = 6. A free-parameter model fit to six subjects will fit almost anything; "good fit" is not a hypothesis test, and a correlation with playing level across six people has about four degrees of freedom. **Neither study is strong. They are simply the only two that exist.**

### 2.3 The four available reconciliations, most plausible first

1. **DEPTH OF HISTORY.** Gray modeled a state built from **three** prior pitches; Kashiwabara tested **one**. An expectancy that takes three pitches to load is invisible to a lag-1 test. **Most likely explanation, and directly testable.**
2. **SKILL LEVEL.** Gray's own parameters-correlate-with-level result implies the machinery grows with skill — which would make an HS null uninformative about the hitters an SEC pitcher faces. **This possibility alone forbids quoting the null as settled to a college pitcher.**
3. **Outcome measure** — swing accuracy vs impact-location timing error.
4. **Apparatus** — rendered pitcher with delivery cues vs machine with none.

---

## 3. The large-N observational record (F-253, F-254, F-255)

### 3.1 12.4 million pitches: no association with outcomes

arXiv:2601.11904, published **Journal of the Korean Physical Society** (DOI 10.1007/s40042-026-01641-5). **~12.4M Statcast records, 2008–2025.** Macroscale: **Shannon entropy** and **inverse Simpson** index of motif usage vs **ERA and wins**. Microscale: **hit vs out frequencies across motifs**.

Authors' abstract language: diversity "exhibits **less decisive association** with conventional performance measures such as ERA or wins"; "**the most highly ranked motifs do not contribute to discriminating between HIT and OUT outcomes**," indicating "inherent limitations in using motif-based diversity measures alone." What they *do* find: motif usage is stable and non-random, following **Zipf's law**.

**No effect size was retrievable.** Do not quote this as "r = 0" — quoting a hedge harder than the authors wrote it is the failure mode of F-240.

**The coach's objection, conceded in part:** ERA and wins aggregated to a season would wash out an effect that lives in 0-2 against a specific hitter, and wins is nearly meaningless at pitcher level. **The part that survives:** the microscale arm is at motif level, not season level, and still found no hit/out discrimination.

### 3.2 Pitchers over-alternate, and repetition is not punished

**Kovash & Levitt 2009** (NBER WP 15347), **>3,000,000 pitches**: pitchers throw **too many fastballs** and show **negative serial correlation** in pitch calling — **they alternate more than randomization would produce.** Back-of-envelope: **"as many as two additional victories a year."**

**The critique is as important as the paper.** Birnbaum (*Sabermetric Research*, Sept 2009) and others: the correct equilibrium test is to adjust until OPS-after-fastball equals OPS-after-non-fastball, and **the paper did not make that comparison** — it evaluated **only pitches that ended the at-bat**, a biased subset. **OPS was reportedly computed incorrectly, undervaluing walks**, which would inflate the apparent value of breaking pitches — exactly the direction needed to produce the headline. **Quote the over-alternation half. Do not quote "two wins."**

**FanGraphs Community Research**, *"The Effects of Repeating Pitches on Pitcher Success Rate,"* **2023 Trackman**: throwing the same pitch twice **outperforms the average sequencing result in every area except fastball whiffs**; each pitch type is about as effective in isolation as when thrown one to three times in a row. No n, no controls.

**The confound running the other way, uncontrolled everywhere:** pitchers repeat a pitch when it is working and when the count allows. **Selection makes repetition look good.** So the honest position is that the folklore is unsupported — **not** that repetition is a positive strategy.

### 3.3 The size of the prize: ~0.23 bits

**Brennan (Baseball Prospectus):** mean information given up through sequencing **~0.23 bits, range 0.15–0.35 bits**; pitchers get **more predictable the further they fall behind in the count**.

**Arithmetic (computed here):** with four pitch types maximum uncertainty is 2 bits, so **~0.23 bits is roughly a tenth of the hitter's uncertainty.**

**Next-pitch prediction models** — numbers from *different* studies, **not poolable**: binary FB vs non-FB **~71%**; 3-class **61.3%**; per-pitcher, **42 of 70** beat baseline on binary, **12 of 70** on 3-class. **Discard the XGBoost claim of 93.3% / macro-F1 0.873 — 30 points above every other result, almost certainly leakage.** Feature importance consistently ranks **previous pitch type** among the top predictors.

**Where the exploitable signal lives: overall tendencies and count behaviour — not any individual clever two-pitch combination.** That is the argument for auditing usage by count over arguing about order.

---

## 4. Times through the order — the familiarity mechanism is shakier than assumed (F-256)

This matters because the TTO penalty is the **only large-scale natural experiment on hitter familiarity**, and familiarity is the mechanism sequencing folklore depends on.

**The received view — Lichtman** (SABR / BP, data **2002–2012**, BIS pitch types via FanGraphs): mostly-fastball pitchers **lose 47 points of wOBA** by the third time through; low-fastball-frequency pitchers **lose only 18**. Interpretation: **familiarity, not fatigue.**

**The challenge — Brill, Deshpande & Wyner** (JQAS 2023, DOI 10.1515/jqas-2022-0116, arXiv:2210.06724): after adjusting for **batter quality, pitcher quality, handedness and home-field advantage**, there is **little evidence of a strong discontinuity** between times through the order; existing methods **cannot disentangle continuous within-game evolution from discontinuities**; the third time through **should not be treated as a special cutoff.**

**State it precisely or it will be misreported.** Brill et al. do **not** say pitchers fail to decline over a game. They say **the jump at each new time through is not well supported** — and that distinction carries the mechanism: **familiarity predicts a discontinuity** (the hitter's information resets upward each plate appearance) while **fatigue predicts a smooth decline.** No discontinuity ⇒ the cleanest published evidence for familiarity weakens, and so does the strongest argument that "he's already seen it" is large.

**Not resolved. Both can be true:** no clean discontinuity overall, plus a real conditional advantage for arsenal breadth. **Brill et al. did not test the breadth interaction.** → `open-disputes.md` #18.

**Standing on the authors:** the corpus already carries Ludwig/Brill/Wyner (arXiv:2508.19184, xCTRL) as verified-clean. Same group, same posture of distrusting effects that survive only without confounder adjustment — the posture this program adopted for itself (F-240).

---

## 5. What is being sold, and what it is worth

| Item | Who | Verdict |
|---|---|---|
| **"A pitcher with average stuff and elite sequencing beats elite stuff with linear sequencing"** — attributed to the 12.4M-pitch paper | atsstats.com (new); mkdcbaseball.com (**already blocklisted, Sweep 1**) | **DEBUNKED / MARKETING.** The paper found the **opposite**. Correct n, reversed conclusion. **Blocklist both. See §7.** |
| **Driveline "Paint Mixer"** + **"buyback effect"** (secondary pitches making primaries better) | Driveline | **UNPROVEN.** Premise — usage over order — is the one thing today's evidence supports; **no outcome validation found.** This is the F-163 tunneling pattern with a different noun. |
| **"Throw your best pitch more"** (e.g. Clay Holmes, **sinker→sinker 365 times in 2025**) | industry trend | **PROMISING.** Consistent with over-alternation (§3.2) and with repetition not being punished. |
| **Carry more distinct shapes** (Colorado 2026: four-seam usage **40.9% → 29.1%**; Senzatela **57% → 37%**; cutter+sweeper, four-seam+sinker pairings; more viable primaries per arsenal since 2021) | industry trend | **PROMISING — and not actually in conflict with the row above.** Both are moves *away* from a balanced, alternating, predictable mix, which is the error all three evidence lines flag. |
| **"Setup" and "knockout" pitches exist in the sequence clusters** | Prasad, MIT Sloan 2021; ~3.5–3.6M pitches 2015–2019; Sequence Graph Transform + GMM clustering | **UNPROVEN, FLAGGED.** A description of structure, not a demonstration of effect. **F-163 is the cautionary tale: a full metric suite published with zero outcome validation, later tested at r = 0.07.** Do not let "setup pitch" acquire evidential status by repetition. |
| **Game-theoretic optimal sequencing** — Stackelberg and "decision point" equilibria, **with a pitcher command/accuracy model as an input** | Melville, Melville, Dawson, Nieves-Rivera, Archibald & Grisman; MIT Sloan 2023; BYU thesis #9910 | **PROMISING as a framework, UNPROVEN as a result.** No outcome validation retrievable. **The command-as-input feature is the right idea** — a sequencing recommendation that ignores whether the pitcher can execute the location is a recommendation for a different pitcher (cf. F-171, xCTRL). |

---

## 6. Translation — the one deployable action (F-255, F-257)

**Audit predictability by COUNT, not sequence by sequence.**

**What I tell the pitcher:** *"Nobody is beating you because of what you threw last pitch. They're beating you because in 2-0 and 3-1 you throw the fastball almost every time, and everyone in this league already knows it."*

**The work — a 20-minute data audit, then a constraint bullpen:**
1. Pull a full season of Trackman logs. Tabulate **pitch-type usage by count** (12 buckets) × batter handedness.
2. Flag buckets where one pitch exceeds **~80%**. Brennan's result — predictability rises as the pitcher falls behind — says look hardest at **1-0, 2-0, 2-1, 3-1**.
3. Bullpen with the **catcher calling from a randomization card**, constraining him to his second-best pitch in the two leakiest counts, ≥8 reps each. This is a **constraints-led manipulation** (F-195, F-212), not a cue.
4. Separately, and with the most experimental support behind it: **film from centre field at 240 fps and compare the first 15 frames after release across pitch types.** Kashiwabara's authors name **delivery consistency** and **matched early trajectory** as the timing-error mechanisms — and unlike order, those are things a pitcher can change.

**On video the failure looks like:** a visible glove-side or head-position difference between fastball and changeup **in the frames before release** (a tell — no sequencing recovers from it); **early trajectories separating before ~150 ms**; or a single count cell over 85%.

**How you know it worked — and the sample size to see it:**
- **A usage rate is a proportion.** Pinning one to **±10 percentage points at 95% confidence takes ~96 pitches IN THAT COUNT BUCKET.** A college starter throws ~1,000–1,400 pitches a season across 12 buckets, so **only the five or six most common counts give usable estimates, and only over a full season.** One bullpen tells you nothing; one month tells you nothing. **Say this to the athlete before starting or the intervention dies from an impatient read.**
- **The tell check is fast:** frame-by-frame on 20 fastballs vs 20 changeups. A systematic postural difference across 20 reps is real.
- **Do not promise a run-value or ERA change.** Outcome-level command effects need ~200+ tracked pitches to detect even when large, and sequencing effects are small.

**What NOT to do on this evidence:** do not build a philosophy around specific two-pitch combinations; do not tell him to avoid repeating a pitch; do not buy a pitch-calling product on the strength of "setup pitches exist in the data"; and do not repeat "elite sequencing beats elite stuff" to anyone — that sentence is a content farm inverting a paper that found the opposite.

---

## 7. ⚠️ A NEW HAZARD CLASS: DIRECTIONAL INVERSION OF A REAL SOURCE (F-258)

**atsstats.com** (new to the blocklist) and **mkdcbaseball.com** (**already blocklisted since Sweep 1, 2026-08-12 — a repeat offender**) cite the motifs paper — **correct title, correct 12.4-million figure, real journal** — for the claim that "the effectiveness of a pitch is defined by the pitches preceding it" and that elite sequencing beats elite stuff. **The paper reports the reverse.**

**This is not a fabrication and not an AI hallucination.** The citation is real; the direction is flipped. **It defeats citation-checking by construction** — anyone who verified the PMID/DOI, the title and the n would have passed it.

It is structurally identical to **correction #2 of 2026-08-13** (the changeup framing, which also inverted its source) and is exactly what **operating rule (A)** exists to catch: *does the source support THIS sentence, a weaker one, or the opposite one?*

**Countermeasure: check the abstract's own verbs, not the identifier.** Added to the blocklist.

---

## 8. What does not exist (F-257) — and why the whole literature may be aimed wrong

Absence search 2026-09-02, **against search indexes only** (egress blocked), so weaker than the F-250 absence:

- **No sequence manipulation with professional or D1 hitters.** The two that exist are n = 26 HS and n = 6 college-in-VR.
- **No sequencing analysis controlling for pitcher quality.** Every observational result is contaminated by "good pitchers do X."
- **No outcome validation of any commercial sequencing product.**
- **No study of pitch sequencing at the college level at all.**
- **No test of whether a pitcher can be trained to be less predictable.**
- **No year-over-year stability estimate for per-count pitch-type entropy.**
- **No within-pitcher analysis** of outing run value against that outing's entropy with pitcher fixed effects.

**The last two are computable from public data in an afternoon, and the first of them can kill the topic.**

**And here is the structural indictment.** **F-094 — within-athlete R² = 0.957 vs between-athlete R² = 0.076** for velocity and torque — says between-pitcher associations are close to uninformative about within-athlete levers. **Every sequencing result above, positive or null, is between-pitcher.** Add the standing restriction-of-range problem (Luera 2020, r = .17–.29 in an all-hard-throwing sample) and the elite-population effects are probably smaller than the published numbers.

**Two questions, in order:**
1. **Is per-count pitch-type entropy even stable year over year within a pitcher?** If not, it is noise and the subject collapses.
2. **Do pitchers do better in their own higher-entropy outings?**

**Until (1) is answered, "be less predictable" is a marker-shaped instruction and must not be sold as a lever** — the same error as stride length (F-043) and extension (F-250).

---

---

# ADDENDUM — 2026-09-03

**The 2026-09-03 cycle selected this topic from `INDEX.md` §5 and only discovered it was already covered after the research pass was complete** — because that cycle cloned `main`, and this file lives on an unmerged branch `main` cannot see. **That is registered as F-259 and it is the most consequential thing the cycle produced.** What follows is the residue: four items the 09-02 sweep did not reach, and one conflict between the two cycles.

## A1. ⚠️ Citation conflict on the PLOS ONE manipulation (F-260)

**The two cycles agree on every identifier, every number and every result of the study in §2.1 — and disagree on its authors.**

| | 2026-09-02 (§2.1) | 2026-09-03 |
|---|---|---|
| Authors | **"Kashiwabara et al."** | **Kidokoro S, Matsuzaki Y, Akagi R** |
| Provenance | search summary | search summary naming a **Shibaura Institute of Technology institutional-repository page**, listing all three with given names |

Everything else matches: PLOS ONE **15(3):e0230385**, PMID **32182276**, n = 26 HS hitters, FB 34.3 ± 1.3 m/s, Continuity 15 / Random 30 / Open 20.

**Neither cycle opened the paper. PLOS ONE is fully open access — this is a one-click fix the moment egress returns, and it is the first thing to resolve.** Both names are recorded and dated; **neither has been overwritten.** The 09-03 provenance is the stronger one, but the 09-02 reading of this paper was otherwise more complete — it retrieved **p = 0.338** and **p < 0.001**, which the 09-03 pass did not.

**Why this matters out of proportion to its size:** it is this corpus's most-repeated lesson at the smallest possible scale. A PMID, a DOI, a sample size and two p-values, all agreed on by two independent passes — **with the author line still in dispute.**

## A2. The minimax leg of §3.2 has been reversed twice in 2024 (F-261)

§3.2 records Kovash & Levitt's over-alternation result as contested. **It is now stronger than contested: two independent 2024 analyses report that payoff equality and the absence of serial correlation HOLD for the majority of players.** Their deviations are elsewhere — batters swing less than theory predicts; pitchers throw inside the zone more than expected.

- ScienceDirect PII **S2773161824000168**, *"Professionals do play Minimax: Revisiting the Nash equilibrium in Major League Baseball"* (2024) — **authors and journal unretrievable.**
- **White DR & Smith BO (2024)**, *"Changing It Up: Determining the Nash Equilibria for Major League Baseball Pitchers,"* American Behavioral Scientist, **DOI 10.1177/00027642241235829.**

⚠️ **Attribution risk between the two is logged and unresolved.** Now **Dispute #19**.

**What this does and does not touch.** It undercuts *"he alternates too much."* **It does not touch the count audit in §6**, which rests on Brennan's ~0.23 bits and the count-behaviour result — *usage in a given count*, not serial dependence between adjacent pitches. **Different quantities; only one has been reversed.**

**The portable idea, worth taking regardless of who wins: move the question from pitch TYPE to pitch LOCATION.** A pitcher who throws three pitch types and puts all of them in the same third of the zone is more predictable than his mix suggests. **Add a location-by-count row to the §6 audit.**

## A3. The seven-class predictability baseline, and two more sample sizes for §6 (F-262)

**Sidle & Tran (2018)**, Journal of Sports Analytics, DOI 10.3233/JSA-170171. **~1,340,000 pitches, 287 pitchers** with ≥500 pitches in both 2014 and 2015. **Seven-class naive baseline accuracy 54.38%.** Random forests > LDA > SVM. Top features again include **the previous pitch**, alongside pitcher/batter history, pitcher/count history and game score.

⚠️ **Not poolable with §3.3's binary ~71% or 3-class 61.3%** — different label sets, different papers. Quote each with its class count.

**Two sample sizes to sit alongside §6's ±10 pp figure** (which answers *how precisely can I estimate a usage rate*; these answer *how big a change can I detect*):

| Question | Requirement |
|---|---|
| Detect a **70% → 55%** shift in one count's fastball usage, 80% power, α = .05 | **≈ 83 pitches in that count** |
| Detect a lag-1 **serial correlation r = 0.10**, 80% power | **≈ 790 pitches** — a starter's full season |

## A4. The TTOP framing to adopt, and the test that would settle §4 (F-263)

**"The third time through the order" is a BIN BOUNDARY.** Every pre-2023 analysis binned plate appearances by time-through and compared bin means — **a design that cannot distinguish a step from a slope**, because a slope binned into three buckets produces three different bucket means. That *is* Brill/Deshpande/Wyner's stated critique.

**This corpus has been burned by exactly this shape once, in space rather than time:** stride length, a real cross-sectional pattern read as a mechanism that would survive intervention (F-043). F-094 is the general warning. **This is F-043 in the time domain.**

**The test nobody has run, and it is cheap.** F-125 and F-127 hold that under fatigue **command degrades before velocity** and fatigue **neurally inhibits the infraspinatus**. So a fatigue-driven TTOP should appear in **location quality, smoothly, ahead of any outcome signal** — and a familiarity-driven one should not. Computable from public pitch-level data with no new collection. **The cheapest high-value study the 09-03 cycle identified.**

**One thing blocks pricing the fatigue side at all:** the within-start velocity decline in mph is **unknown to this corpus** (F-266). The circulating "3–5 mph by the sixth" is a commercial-blog claim about an **88 mph** pitcher — the same 88 mph strawman F-072 already catches facilities using for training *gains*, now recycled as a within-start *loss*. **Do not quote it, and do not quote a counter-number: there isn't one.**

## A5. The sentence for the athlete

> **"Nothing happens to you when the lineup flips. There's no bell. You get tired on a pitch-count clock, and the clock doesn't care what inning it is."**

Both camps agree the batter gets better across a game. The dispute is about **why**, and therefore about what to do — **fatigue is trainable and familiarity is not.**

---

*Sources for this file: `daily/2026-09-02-sequencing.md`, `daily/2026-09-03-report.md`. Findings F-251 to F-258 (09-02) and F-259 to F-266 (09-03). Disputes #17, #18, #19. **Nothing here was read at source — see the banner at the top.***
