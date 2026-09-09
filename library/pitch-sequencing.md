# Pitch Sequencing — the transition matrix

**Opened 2026-09-09.** Companion to `pitch-mix-sequencing.md` (the marginal distribution), `count-leverage.md` (where a pitch is worth something) and `times-through-order.md` (when to stop). Findings **F-294 → F-303**.

> ### ⚠️ RUN CONDITION — READ BEFORE USING ANYTHING IN THIS FILE
> **Written in the SIXTH consecutive fully egress-blocked cycle (F-294). No primary source was opened.** Everything in §1–§6 is **closed-form arithmetic and simulation, re-derivable in thirty lines, dependent on no source.** Everything in §7 is **snippet-level or existence-level and is quarantined.** The one empirical input inherited from elsewhere — the per-pitch run-value SD — is F-270's, is itself unverified, and is bracketed throughout.
>
> **This file states RATIOS and DETECTION THRESHOLDS with confidence and ABSOLUTE RUN VALUES with none.** Every run figure scales linearly with the anticipation slope $D$, which is unmeasured anywhere (Dispute #19).

---

## 1. What object is actually being chosen

The corpus already holds three of the four pieces of the in-game decision. This is the fourth.

| Piece | Object | File |
|---|---|---|
| Mix | the marginal distribution $p_i$ — a **vector** | `pitch-mix-sequencing.md` |
| Count | leverage weights across ball-strike states | `count-leverage.md` |
| Outing | when to stop | `times-through-order.md` |
| **Sequence** | $P(\text{next}=j \mid \text{prev}=i)$ — a **matrix** | **this file** |

**That vector-to-matrix step is the whole file.** It multiplies the parameters by $k$ and leaves the season at 1,600 pitches.

**Free parameters in the decision:**

| arsenal $k$ | mix | 1st-order sequence | sequence × 12 counts | 2nd-order |
|---|---|---|---|---|
| 3 | 2 | 6 | 72 | 18 |
| **4** | **3** | **12** | **144** | **48** |
| 5 | 4 | 20 | 240 | 100 |

**Pitches per cell, 1,600-pitch NCAA starter season:**

| conditioning | $k=3$ | $k=4$ |
|---|---|---|
| pitch type only (mix) | 3 cells / **533** | 4 / **400** |
| previous pitch | 9 / **178** | 16 / **100** |
| previous pitch × batter hand | 18 / **89** | 32 / **50** |
| previous pitch × count (12) | 108 / **15** | 192 / **8** |

---

## 2. The detection asymmetry — and it runs between the two PARTIES (F-295)

Two different questions about the same pitcher, requiring two different statistics.

**Question A — "does he have a tendency?"** A frequency. One-sample proportion test, $\alpha = .05$ two-sided, 80% power, observations **of the conditioning event**:

| baseline $p_0$ | +5pp | +10pp | +15pp | **+20pp** | +30pp |
|---|---|---|---|---|---|
| 0.35 | 726 | 183 | 82 | **46** | 20 |
| 0.40 | 761 | 191 | 85 | **47** | 20 |
| 0.50 | 783 | 194 | 85 | **47** | 19 |

**Question B — "did changing it help?"** A run value. Two-sample per group, SD from F-270:

| true gap | SD .20 | SD .25 | SD .30 |
|---|---|---|---|
| 0.5 R/100 | 25,116 | 39,244 | 56,512 |
| 1.0 | 6,279 | 9,811 | 14,128 |
| 2.0 | 1,570 | 2,453 | 3,532 |
| 5.0 | 251 | 392 | 565 |

**The same +20-point effect, priced both ways:**

| $D$ (R/100) | implied gap | opponent needs | **you need** | ratio |
|---|---|---|---|---|
| 1 | 0.20 R/100 | 47 | 245,277/group | 5,208× |
| 2 | 0.40 | 47 | 61,319 | 1,302× |
| 4 | 0.80 | 47 | 15,330 | 326× |
| 8 | 1.60 | 47 | 3,832 | 81× |

> **A 1,600-pitch season is comfortably enough for the first question and roughly 1/2,000th of enough for the second.**

**This is F-257 and F-289's input-vs-outcome asymmetry with a new feature: it is asymmetric between the PARTIES.** The opponent is measuring a bounded-variance proportion; you would be measuring a run-value difference of order 0.002–0.016 runs against an SD of 0.20–0.30. **The signal-to-noise ratios differ by orders of magnitude before any test is chosen** — which is why the direction survives every convention change even though the ratio itself does not.

⚠️ **Say the direction, never the ratio.** The 81×–5,208× span is convention-dependent and scales entirely with the unmeasured $D$. Same discipline as F-269's magnitude table and F-278's λ table.

**The prescription: build the report your opponent is building.** You have the same log and better access. You are only disadvantaged if you insist on asking the harder question.

---

## 3. The granularity trap (F-297)

Simulate a pitcher with **no tendencies at all** — true conditional probability 0.40 in every cell — and ask how big the largest apparent tendency looks.

| conditioning | cells | n/cell | SD | **E[largest deviation]** | P(≥1 sig. at .05) |
|---|---|---|---|---|---|
| prev pitch, $k=3$ | 9 | 178 | 3.7pp | **+5.4pp** | 37% |
| prev pitch, $k=4$ | 16 | 100 | 4.9pp | **+8.6pp** | 56% |
| prev × hand, $k=3$ | 18 | 89 | 5.2pp | **+9.4pp** | 60% |
| prev × hand, $k=4$ | 32 | 50 | 6.9pp | **+14.3pp** | 81% |
| prev × count, $k=3$ | 108 | 15 | 12.6pp | **+32.2pp** | 99.6% |
| **prev × count, $k=4$** | **192** | **8** | **17.3pp** | **+47.3pp** | **100%** |

**The honest budget** (≥47 obs/cell): 9 ✓ · 16 ✓ · 32 ✓ barely · 48 ✗ · 108 ✗ · 192 ✗ (fails by 3–6×).

**Bonferroni-corrected, to detect a TRUE +20-point tendency:** $m=9$ needs 78/cell (has 178 ✓) · $m=16$ needs 86 (has 100 ✓) · $m=32$ needs 96 (has 50 ✗) · $m=192$ needs 121 (has 8 ✗).

> **Previous-pitch × handedness is the finest cut a college season can honestly support, and only uncorrected.**

**This disarms the opposing report too.** Their fine-grained sheet on your pitcher is subject to the identical arithmetic.

---

## 4. The count-composition confound, and why the fix is unaffordable (F-298)

"The pitch after a fastball" is not a random subset. The previous pitch's strike rate determines which counts follow it; count drives usage. **So an apparent sequence effect can be pure composition with zero true sequence dependence:**

$$\text{apparent gap} = \Delta(\text{strike rate}) \times \Delta(\text{usage between count states})$$

| Δ strike | Δusage .20 | .25 | .30 | .35 | .40 |
|---|---|---|---|---|---|
| 5pp | 1.0 | 1.2 | 1.5 | 1.7 | 2.0 |
| 10pp | 2.0 | 2.5 | 3.0 | 3.5 | 4.0 |
| 15pp | 3.0 | 3.8 | 4.5 | 5.2 | 6.0 |
| 20pp | 4.0 | 5.0 | 6.0 | 7.0 | **8.0** |

**1–8 points, free.**

**Two honest observations:**

1. **This is NOT F-287.** There the lineup-slot bias was **2.5× the effect**, fatal, and *grew more confident with more data*. Here it is 1–8 points against a ~20-point detection floor — **below what a season can resolve.** It matters for **interpretation**, not detection: **attribute any apparent sequence effect under ~10 points to count composition before attributing it to the pitcher.** The corpus should not inflate a real confound into a crisis because the last one was a crisis.
2. **The fix is not free, and that IS new.** F-287's fix cost nothing (compare slots 1–4 vs 1–4). This one requires comparing **within count**, taking cells from $k^2$ to $12k^2$: $k=3$ → 9 to 108 cells (n 178 → 15); $k=4$ → 16 to 192 (n 100 → 8). **Both fail §3's budget by 3–6×.**

> **THE BIND: the confound is real, the correction is textbook, and the correction costs more sample than the season contains. You can have an unconfounded estimate or an adequately-powered one. Not both.**

---

## 5. The equilibrium argument — an observed sequence effect is a MISTAKE, not a lever (F-299)

Apply F-268's stationarity condition to sequences rather than pitch types. If hitter anticipation responds to **conditional** frequencies as it does to marginal ones, then at an interior optimum **every sequence actually used has equal marginal value.**

**So a run-value gap between two sequences in game data is one of three things:**

1. **Noise** — overwhelmingly most likely (§2: 3,832–245,277 pitches per group vs a 1,600-pitch whole-arsenal season).
2. **Composition** — count context in disguise (§4).
3. **A genuine disequilibrium** — real, exploitable, and rarest.

**"His slider plays better after a fastball, so throw more sliders after fastballs" is F-269's error transplanted from the marginal distribution to the transition matrix** — which makes it the stride-length error (F-043/F-044/F-045) in its **third venue**.

### 5.1 Why this is not purely academic: the adaptation channel

**Equilibrium requires the adapting party to observe enough to adapt.** A college hitter faces a given conference starter roughly twice a season — **about eight plate appearances.** He cannot personally equilibrate.

**Adaptation therefore runs through the ADVANCE REPORT, not the hitter's experience** — so the equilibrium argument's force is proportional to the **opposing program's analytics capability.**

| opponent | posture |
|---|---|
| high-analytics conference weekend | **assume the report exists.** Audit and break your top one or two tendencies — this is where §6's runs live |
| low-analytics midweek | the tendency is not being read. **Spend the time elsewhere** |

⚠️ **State this as a question to your own analyst — "does their staff run transition matrices?" — never as a fact about a named opponent.** The SEC/midweek split is an illustration, not a measurement (Dispute #22, §6.3 of the daily brief).

---

## 6. The predictability tax (F-296)

Excess cost per pitch in the affected cell $= D(q-p)/100$ runs. **Runs per 1,600-pitch NCAA season:**

| cell share | tendency | $D=1$ | $D=2$ | $D=4$ | $D=8$ |
|---|---|---|---|---|---|
| 0.15 | +20pp | 0.48 | 0.96 | 1.92 | 3.84 |
| **0.25** | **+20pp** | **0.80** | **1.60** | **3.20** | **6.40** |
| 0.35 | +30pp | 1.68 | 3.36 | 6.72 | 13.44 |

**Where it ranks against everything else the corpus has priced:**

| question | per college season |
|---|---|
| the 0-2 waste pitch (F-280) | ~0.2 runs |
| times through the order, entire question (F-288) | ~1 run |
| **an exploited 20-point sequencing tendency** | **0.8 – 6.4 runs** |
| a 5-point mix error (F-272) | 0.08 – 0.64 |
| a 30-point mix error (F-272) | 2.9 – 23 |

⚠️ **Three stacked upper bounds:** $D$ is unmeasured; it assumes the hitter has the report **and can use it** (F-251/F-252 — advance knowledge is a *prior*, not an in-flight read); and it assumes the tendency is real (§3 says most are not). **The ordering is the usable output. The cell values are not.**

**The anatomist's note (F-299):** a sequencing change is the **only lever in this corpus with zero tissue cost** — unlike velocity (F-094), the lead-leg block (F-062), weighted implements or arm slot. **Unless the fix moves the arsenal 15 points toward breaking balls**, which leaves the free regime into non-fastball workload accounting, an uncovered gap.

---

## 7. ⚠️ QUARANTINE — everything external

**No page was opened. Nothing below is verified substance.**

| Item | Status |
|---|---|
| **Kovash & Levitt 2009, NBER w15347** — "Professionals Do Not Play Minimax." Reported: 3M+ pitches, too many fastballs, **negative serial correlation**, "as many as two additional victories a year" | **EXISTENCE VERIFIED** (NBER, SSRN, Semantic Scholar, NBER Digest). **SUBSTANCE SNIPPET-ONLY. DO NOT QUOTE THE TWO-WINS FIGURE** |
| **"Professionals do play Minimax" 2024, *Sports Economics Review*, S2773161824000168** — a **direct published rebuttal**, found in the same search. Analyses **both** players, and pitch **location** not **type** | **EXISTENCE VERIFIED, SUBSTANCE SNIPPET-ONLY.** Imported as a **pair** with the above or not at all |
| **Walker & Wooders 2001, AER 91(5):1521–1538** — tennis serve frequencies at equilibrium, **serial correlation in the choices** | **EXISTENCE VERIFIED.** ⚠️ Itself contested by a published **Comment**, AER 2007 97(1):517–523 |
| **arXiv 2601.11904** — pitch-pattern motifs, ~12.4M pitches; reportedly **non-random structure with limited association with performance** | **UNREAD. QUEUE HEAD FOR THIS TOPIC** — it would test §5 directly |
| arXiv 2606.17345 · arXiv 2609.03810 · Sloan directed-graph sequencing | **UNREAD**, queued since 2026-09-06/07 |
| arXiv 2607.29041 · SABR two-pitch sequences · *Sports* 2015 3(1) 40 · "A Game Theoretical Approach to Optimal Pitch Sequencing" | **UNREAD, NEW** |
| Next-pitch prediction accuracy: ~70% binary FB/non-FB; 66.62% multi-class; 59%; 80.88% k-NN | **SNIPPET-ONLY, MIXED SOURCES.** ⚠️ The reported **"311% improvement over naive"** is a **ratio artefact** — only possible when the naive baseline was near zero. **Do not repeat it** |
| "Humans are bad at randomising" | ⚠️ **Appeared in a search SUMMARY and in NO SNIPPET.** F-284/F-293 rule applies. The corpus holds **no verified citation** and will not manufacture one |

**What the prediction-accuracy numbers do NOT mean:** a ~70% binary model against a ~55–60% marginal baseline bounds the **total** exploitable conditional information from **all** features — count, batter, score, previous pitch. **The previous-pitch share alone is smaller**, which makes §6's +20pp scenario an upper bound. **And prediction is not exploitation:** a model with unlimited time and full Statcast is not a hitter with 150 ms (F-251, F-252).

---

## 8. THE TRANSITION-MATRIX AUDIT — what to actually do

**One afternoon of analyst time per pitcher. No new instrumentation, no athlete time, data you already own.**

1. Pull last season's pitch log for one 85+ starter. **Exclude the first pitch of every plate appearance.**
2. Build **one** table: previous pitch type × current pitch type, **split by batter handedness and nothing else.** (18 cells at ~89 for $k=3$; 32 at ~50 for $k=4$.) **Do not condition on count.**
3. Print the pitcher's **marginal** usage beside each row. **The row is the tendency; the marginal is the null.**
4. Flag a cell only if **all three**: ≥47 observations · deviation ≥15 points (10 is composition, §4) · it is not the single most extreme cell — **or** you have accepted the 56–81% false-positive rate out loud.
5. **The free extra, and run it FIRST:** the **repeat rate** for the primary and secondary pitch — $P(\text{SL} \mid \text{prev} = \text{SL})$ vs the marginal SL rate. **Below the marginal is the over-alternation signature** (F-300). ~42–47 same-pitch observations. **One number per pitch type, and it tests the only claim in this topic with a mechanism behind it.**
6. **What "working" looks like — and it is NOT run values.** Re-run in-season at ≥47/cell. **Success = the flagged tendency has moved toward the marginal.** You will never know whether it scored runs.

**The script, third application of F-273's:**

> *"We're changing this on principle, not on evidence. If your ERA is better in April I won't credit it and if it's worse I won't blame it. Neither reading would be real."*

**Do not:**
- ❌ build a count-conditioned sequencing report (**100% guaranteed** to produce a fake tendency; expected largest ≈ **47 points**);
- ❌ compare run values between sequences (3,832–245,277 per group);
- ❌ tell the pitcher about a tendency found in the most extreme of sixteen cells.

⚠️ **Steps 1–5 are a MEASUREMENT protocol and assume nothing about changing the athlete. Only step 6 assumes transfer** — and **F-197 records that no bullpen-to-game transfer study exists in baseball.** This is the third consecutive cycle whose single executable recommendation rests on it (Dispute #20a). **The audit is worth running even if transfer is zero**, because it tells you what the opposing report says about your pitcher, which is a fact about the world regardless.

---

## 9. What this file does not contain

- **No estimate of $D$.** Six cycles have needed it; none could get it.
- **No verified empirical sequence effect from anywhere.** Everything external is §7.
- **Nothing on attacking SPECIFIC hitters** — batter-specific planning remains entirely uncovered.
- **No second-order (two-pitch-back) analysis.** §1's table shows why: 48 parameters for a four-pitch arm.
- **No treatment of location sequencing**, which the 2024 rebuttal says is the right unit. **If that paper is correct, this entire file analyses the wrong object** — a limitation stated because it is the single most likely way this file is wrong.
