# THE REGISTRY-WIDE NULL AUDIT
### What this corpus's "don't bother" verdicts are actually made of

**Created 2026-09-30.** Closes the structural item `INDEX.md` has carried as its **top priority since 2026-09-22** and which went unrun for eight days.
**Findings produced:** F-464 → F-477.
**Companion to** `library/jump-transfer-audit.md` (which audits one topic's nulls) — this file audits **the whole registry**.

> **THE ONE-LINE RESULT:** the n ≥ 97 rule works, catches 31 findings, and **would have missed both of the two biggest errors found today.**

---

## 1. Why this matters to a pitching coach and not only to a statistician

Every registered NULL in this corpus is a channel it has told Tommy **not to train**. Jump height. Power-to-bodyweight. Grip strength. Trunk mobility. Weighted implements. Stride length. Each one is a training block somebody did not run because this vault said the evidence was against it.

A null that is wrong does not merely misstate the literature. **It closes a door.** The audit exists because closing a door on a detection floor is the most expensive mistake a development program can make — it is invisible, it never produces a failed experiment, and it compounds every season.

---

## 2. THE TAXONOMY — three ways a registered null fails (F-471)

The audit's main product is not a list. It is the discovery that **"underpowered" is only one of three failure modes**, and the corpus had a procedure for that one only.

| Type | What went wrong | Caught by power arithmetic? | How you actually catch it | Confirmed count |
|---|---|---|---|---|
| **A — UNDERPOWERED** | Right variable, right contrast, sample too small to detect a meaningful effect | ✅ **Yes** — F-439's n ≥ 97 / MDE | Compute `r_crit` or MDE from n | **31 of 38** null-bearing findings with an extractable n |
| **B — MISSING COMPARISON** | Adequate power, but **the study never ran the contrast the corpus attributes to it** | ❌ **No** | Read the DESIGN section; enumerate conditions; check each against the claim's wording | **1 confirmed (F-044)** |
| **C — WRONG OUTCOME** | Well-powered analysis on **a different dependent variable** than the claim names | ❌ **No** | Find the sentence in the source; check its **object noun** | **1 confirmed (F-013)** |

**The order of operations is now:**
1. **What was the dependent variable?**
2. **Which contrasts were actually run?**
3. *Then* compute power.

Power is the **third** check. The corpus escalated it to a top structural item for eight days without noticing that the two errors sitting underneath it were not power errors at all (F-470).

> ⚠️ **Types B and C are F-382 with the direction reversed.** F-382 caught a peer-reviewed clinical review miscarrying a citation (wrong leg, wrong variable, wrong population). Types B and C are **this corpus doing the same thing to its own sources.** Every fabrication defence that has caught 16 fabrications — does the journal exist, are the authors real, is the PMID right, is the number correctly transcribed — **passes cleanly on both of today's errors.**

---

## 3. THE TYPE A TABLE — detection floors across the registry (F-464)

Registry parsed at **463 findings**. Null-language sweep over title + CLAIM + EVIDENCE + CAUSALITY returned **57 candidates**, of which **36 carry an explicit NULL/REFUTED tag** and **38 have an extractable `n`**. **31 of those 38 (82%) fail the n ≥ 97 threshold.**

### Correlational nulls — α = .05 two-tailed

| Finding | n | `r_crit` | R² floor | 95% CI on reported r | Max R² compatible | Verdict |
|---|---|---|---|---|---|---|
| **F-004** jump height → velocity | 33 | 0.344 | 11.8% | r = .07 → [−0.280, +0.404] | **16.3%** | FAIL *(already regraded, F-438)* |
| **F-005** relative power → velocity | 33 | 0.344 | 11.8% | r = .19 → [−0.164, +0.501] | **25.1%** | **FAIL — newly flagged** |
| **F-013** grip → *(see §4)* | 87 | 0.211 | 4.4% | [−0.211, +0.211] | 4.4% | **Type C, not Type A** |
| **F-015** trunk rotation ROM → velocity | 30 | 0.361 | 13.0% | r = .131 → [−0.241, +0.469] | **22.0%** | **FAIL — newly flagged** |
| **F-431** finger strength → spin | 21 | 0.433 | 18.7% | [−0.432, +0.432] | 18.6% | **FAIL — newly flagged** |
| F-043 stride → velocity *(positive)* | 315 | 0.111 | 1.2% | — | — | PASSES |
| F-175 release SD → walks | 344 | 0.106 | 1.1% | — | — | PASSES |
| F-400 sleep → skill | 959 | 0.063 | 0.4% | — | — | PASSES |

**F-005 is the newly consequential one.** It is the basis of the corpus's "test and train ABSOLUTE impulse, never per-kilogram" instruction (F-003). That instruction may well be right — but **r = 0.19 at n = 33 is compatible with relative power explaining up to 25% of velocity variance.** The *comparison* F-005 actually makes (relative r = .19 vs absolute r = .43–.44, **in the same 33 pitchers**) is a better-powered inference than a bare null, because a within-sample comparison of two correlations does not carry the same detection floor. **The comparison survives; the bare null does not.**

### Paired / within-subject nulls — MDE at 80% power

| Finding | n | MDE (Cohen's *d*) | ≈ mph at within-subject SD 1.5 |
|---|---|---|---|
| **F-413** warm-up ball weight | 12 | **0.889** | 1.33 mph |
| **F-035** wearable resistance | 17 | 0.724 | 1.09 mph |
| **F-415** PAPE vs general warm-up | 18 | 0.701 | 1.05 mph |
| **F-386** command within outing | 18 | 0.701 | — |
| **F-044** stride ±25% | 19 | 0.680 | 1.02 mph |
| **F-045 / F-468** stride ±20% | 20 | 0.660 | 0.99 mph |
| **F-391** caffeine crossover | 20 | 0.660 | 0.99 mph |

**Read this table as: none of these studies could have detected a 1 mph effect.** A 1 mph gain is worth a training block to an 88 mph arm. **Every one of these nulls is compatible with a change this program would happily pay for.**

### Two-group intervention nulls

- **F-024** (weighted implements, SEC D1, 35 vs 21): **MDE d = 0.787.** At a pooled velocity SD of ~2.0 mph, **this study could not have detected anything smaller than ~1.6 mph.** It is described in the registry as "the highest-velocity controlled sample that exists, and it is null." It is the highest-velocity controlled sample that exists, and **it is uninformative below 1.6 mph.**
- **F-026** (Driveline, n = 17, **no control group**): no MDE is worth printing. **A single-arm pre/post has no counterfactual at any n.**

### The one null that nearly clears

**F-013 at n = 87** has `r_crit` = 0.211 — the best-powered correlational null in the registry, bounding a correlation inside roughly ±0.21. Under the ±0.20 convention it fails by a hair. **In practice a null that bounds R² below 4.4% is usable.** It is not the power that disqualifies it (§4).

---

## 4. TYPE C, WORKED — the grip-strength null (F-465, F-466)

**F-013 as written:** *"No significant univariate association exists between any grip-strength variable and **ball velocity** in D1 pitchers."* Graded **ESTABLISHED**, **CONFIDENCE: high**, described as *"the closest sample-to-target match of any cross-sectional study in the corpus."*

**The paper** (Barrack et al. 2024, PMC11590131, read in full 2026-09-30) is titled *"Investigating the Influence of Modifiable Physical Measures on the **Elbow Varus Torque – Ball Velocity Relationship**."* Its dependent variable is **elbow varus torque**. Ball velocity is a **covariate**. Its only grip sentence:

> *"No grip strength variables were significantly associated with **EVT** in univariate analysis."*

**The population was right. The sample size was right. The PMID was right. The dependent variable was wrong.**

- n = 87 NCAA D1, **mean ball velocity 37.87 ± 1.55 m/s = 84.83 ± 3.47 mph** — genuinely the best population match in the registry.
- **57 modifiable variables** entered univariately against EVT. **No multiplicity correction stated.**
- The paper's a-priori power statement: **R² ≥ 0.16 with 5 predictors, minimum n = 80** — powered for a large effect *on EVT*. Velocity was never the target.

**And the null concealed a positive result (F-466).** Grip strength **symmetry** entered the final model as a predictor of **increased** EVT: **+0.27 N·m per +1 N of asymmetry, 95% CI [0.07, 0.48], P = .008**, controlling for velocity. Individual-arm grip strength entered neither the univariate nor the final model. The authors themselves: *"The relevance of grip strength on the nondominant arm is unclear, making interpretation difficult."*

> **Treat F-466 with suspicion proportional to its provenance:** it survived a backward elimination from a 27-variable pool reduced from 57, its CI's lower bound is 0.07, and an asymmetry term entering a model when neither of its components does is more likely an artifact of the reduction than a tissue fact. **It is a screen, not a program, and emphatically not a reason to train the glove hand.**

### Downstream damage
`library/ball-hand-friction.md` answers *"Should I buy grip trainers?"* with **"No — grip strength is null."** That answer rested on F-013. It now rests only on **F-431** — n = 21, a **77.9 mph** sample, `r_crit` = 0.433. **The recommendation survives on weak grounds; the certainty does not.**

---

## 5. TYPE B, WORKED — the stride-length crossover (F-467 → F-470)

### 5.1 What F-044 said, and what the study did

**F-044 as written:** *"pitchers threw at **±25% of self-selected stride** and hand and ball velocity were **equivalent across conditions**."*

**The Buffalo crossover ran two game conditions: over-stride and under-stride.** Desired stride was measured **in warm-up** and never pitched as a condition. Verified twice, independently, this cycle:

1. **Crotin & Ramsey 2021** (PMC8486408 — the *same* n = 19 cohort, read in full) names it as a limitation:
   > *"The disadvantage of this methodological design was the inability for comparing desired stride length data with the ± 25% stride conditions."*
   > *"Responses seen between stride length extremes also cannot infer changes occurring from desired stride length, which is a goal of future study."*
2. **Matsuda et al. 2025** (PMC12011807, read in full) cites it as its reference 13:
   > *"there was no significant difference in ball velocity **between the over-stride length and under-stride length conditions**."*

Reported stride values: **OS 1.40 ± 0.15 m (0.76 %BH); US 0.95 ± 0.14 m (0.52 %BH); desired 1.24 ± 0.17 m.**

### 5.2 It is not a power problem (F-470)

| n | Power to detect *d* = 0.79 |
|---|---|
| 12 | 70.3% |
| 15 | 81.2% |
| **19 (Buffalo)** | **90.2%** |
| 20 | 91.8% |
| 25 | 96.6% |

**The Buffalo study had 90% power to detect the effect that F-045 found. It had the power and lacked the condition.** Applying the n ≥ 97 rule here returns "underpowered, discount it" — the wrong diagnosis, which would have left the real error in place.

### 5.3 The midpoint, supplied (F-468)

**Matsuda et al. 2025, every figure read at source.** n = 20 college pitchers (age 19.9 ± 1.1, **173.2 ± 5.8 cm, 71.8 ± 6.4 kg**), ±20% conditions.

| Condition | Stride (m) | Stride (%BH) | Ball velocity (m/s) | vs NS |
|---|---|---|---|---|
| Under-stride | 1.08 ± 0.13 | 62.52 ± 6.99 | **32.48 ± 1.72** | −1.42 (**p = 0.03, d = 0.78**) |
| **Normal** | 1.35 ± 0.12 | **78.20 ± 5.70** | **33.90 ± 1.86** | — |
| Over-stride | 1.56 ± 0.13 | 89.86 ± 6.58 | **32.48 ± 1.70** | −1.42 (**p = 0.03, d = 0.79**) |

**One-way ANOVA p < 0.01, η² = 0.36 (large). US vs OS: p = 1.00, d < 0.01.**
**The penalty is 1.42 m/s = 3.18 mph in both directions, identical to two decimal places.**
**Power check: MDE at n = 20 is d = 0.660; observed d = 0.79 → 91.8% achieved power. Adequately powered for what it found — rare in this registry.**

### 5.4 The synthesis (F-469)

**The two studies do not conflict. They are one curve seen twice.**

- Both found **the two extremes indistinguishable from each other.**
- Only one had the middle point, and it sits **3.2 mph above both.**

Stride length is an **inverted U with a sharp vertex at the self-selected value.** The corpus's practical instruction — *don't move his stride* — is **unchanged and better supported**. The reason has inverted: not *"stride doesn't matter,"* but *"**it matters, symmetrically, and he is already at the top of the curve.**"*

⚠️ **F-048 is untouched by this correction.** "A shorter stride cut heart rate 11.1 bpm at no velocity cost" is an **OS-vs-US comparison** — the comparison that study *can* make. Stride as a **stamina** trade survives intact.

### 5.5 The mechanism, and the hole in it (F-472)

Matsuda's actual purpose was energy flow, and the result is sharper than the velocity finding:

- **Total energy outflow, lower torso → trunk, summed across stride + arm-cocking phases: p = 0.59, η² = 0.02 (negligible).**
- Meanwhile the inputs moved hard: lower-torso energy at SFC **OS > US, d = 1.23**; at MER **US > NS, d = 1.65**; stride-hip negative work **US < OS, d = 2.66**; trunk-joint positive work **OS > US, d = 2.85**.

**Stride length changed the TIMING of energy delivery to the trunk. It did not change the TOTAL.** The authors: *"implying difficulties in explaining ball velocity only by the lower extremity mechanics."*

> ⚠️ **DO NOT CLOSE THIS LOOP ON THE PAPER'S BEHALF.** If total trunk inflow was invariant, **this model does not explain why NS was 3.2 mph faster.** The velocity effect is real and its mechanism is unaccounted for. Candidates this corpus cannot currently separate: a sequencing effect that summed work integrates away; a distal (trunk→arm) transfer difference nobody measured; or §5.6.

### 5.6 🚨 The confound under every stride study ever run (F-473)

**In every instructed-stride design, the normal condition is the only one in which the pitcher is not executing a conscious instruction.**

NS beat both extremes by an *identical* margin. That symmetry is equally well explained by:
- **(a)** the optimum is in the middle, **or**
- **(b)** both instructed conditions cost the same attentional tax.

The corpus already holds the machinery for (b): **F-192 (guidance hypothesis, k = 75, N = 2,228 — PASSES n ≥ 97)** and the external-focus literature both say directing attention to the body degrades skilled output.

**No stride study in existence contains a sham-instruction condition** — a trial where the pitcher is told to hit a stride target *equal to his own normal stride*. **It costs one extra condition and separates the two explanations completely.** Filed as **Dispute #40**.

**What this changes:** you may say *"instructing a stride change costs about 3 mph acutely."* You may **not** say *"his current stride is mechanically optimal."*

**And the deeper gap: every stride manipulation in existence is ACUTE.** Nobody has moved a pitcher's habitual stride across a training block and re-measured.

---

## 6. THE FIELD ITEM THIS CYCLE VERIFIED — grip as a fatigue instrument (F-474, F-475)

**Tremblay et al. 2025** (PMC11877241, *BMJ Open Sport Exerc Med*, read in full), simulated 75-pitch outing, 5 blocks of 15, Rapsodo 2.0, turf mound.

| Measure | Pre | Block 5 | Change | Test |
|---|---|---|---|---|
| **Grip, dominant (kg)** | 55.67 ± 12.32 | 48.62 ± 12.25 | **−12.66%** | F(5) = 10.246, **p < 0.001**, ηp² = 0.299 |
| **Grip, NON-dominant (kg)** | 53.81 ± 12.08 | 49.94 ± 11.86 | **−7.19%** | p = 0.073 *(linear trend p = 0.029)* |
| **Velocity (km/h)** | 119.87 ± 8.00 | 118.75 ± 6.90 | **−0.93%** | F(4) = 3.701, p = 0.039, ηp² = 0.142 |
| Soreness, forearm flexors (0–10) | 1.65 ± 1.16 | 4.19 ± 2.02 | +25.4% | p = 0.005 |
| Pressure pain threshold | — | — | nothing significant anywhere | flexors p = 0.060 |

### 6.1 The headline
**Grip falls ~14× more than radar velocity.** Velocity was **not monotonic** — block 2 (120.35) exceeded block 1 (119.87) before declining. Converges with **Crotin & Ramsey 2021**, read the same cycle: **−1.9 kg / 45.1 kg = −4.2% across 80 pitches, p = 0.017, d = 0.28.** Two independent samples, two countries, same direction.

### 6.2 🚨 The unintended control, and the discount (F-475)
**The non-dominant arm also lost grip — 7.19% — and it threw zero pitches.** It held a glove and performed **six maximal 3-second isometric grip efforts**, exactly as the dominant arm did.

The authors offer **cross-education** and **glove weight**. The parsimonious alternative — **a repeated maximal isometric test is itself fatiguing** — is never considered, and **there is no no-pitch control session** to separate them.

> **Throwing-attributable grip decline ≈ 12.66 − 7.19 = 5.5 percentage points, not 12.66.**
> **Corrected responsiveness ratio ≈ 5.9 : 1, not 13.6 : 1.**

Still substantial. Still better than radar, which is provably unresponsive (and **F-082**: in-season velocity *rises*). **But a program using dominant-hand grip loss as a pull threshold is over-reading it by roughly 2×.**

### 6.3 What it is and is not
The authors state the limit themselves:
> *"This study did not directly evaluate the effects of a gradual decline in grip strength, and we were, therefore, unable to evaluate the relationship between the decrease in grip strength, muscle soreness perception and pitch count."*

**Nothing links grip decline to any outcome you care about.** It is a **responsive instrument with no validated criterion.** There is no evidence anywhere for a grip-loss number that should remove a pitcher from a game.

### 6.4 ⚠️ Population
**n = 30 recruited / 26 analysed, age 21.43 ± 8.86, RANGE 13–50, mean velocity 119.87 km/h = 74.5 mph.** A sample containing children and middle-aged men, ten mph below this corpus's floor, pitch count chosen from a **13U federation guideline**, indoors, to a nine-pocket net. **SAMPLE MISMATCH — directional only. No magnitude here is a norm.**

### 6.5 The free upgrade
**Test both hands and track the DIFFERENCE, not the dominant value.** The non-dominant arm is a within-session control for everything that is not throwing — test reactivity, time, arousal, hydration — and it costs three extra seconds. **Neither published study made it the primary outcome.**

---

## 7. WHAT A D1 PROGRAM CAN DO WITH THIS, THIS WEEK

| Claim | Marker or lever? | What to do | Detection |
|---|---|---|---|
| Stride is at a sharp self-selected optimum | **LEVER, manipulated — but acute and off-population** | **Nothing.** Measure %BH, don't target it | %BH from 2 camera frames, 1st vs last inning, ~25 pitches/bin — detects **DRIFT**, which is the only actionable stride quantity |
| Grip strength → velocity | **UNTESTED** (was: null) | Don't promise mph; don't rule it out either | No study exists to cite |
| Grip asymmetry → elbow torque | **MARKER**, one selected model | Screen only, one line | — |
| Grip as fatigue monitor | **Responsive instrument, no criterion** | **Both hands, track the gap** | Bilateral Jamar, pre / post outing |
| "Stride to 80–85% of body height" | **FOLKLORE as a prescription** | Ignore as a target | — |

---

## 8. WHAT THIS AUDIT DID NOT DO

**The honest accounting, because it is the point of the file.**

- **The audit is begun, not finished.** Type A is now **mechanised** — the script runs against `FINDINGS.md` alone and needs no egress. **Types B and C need a paper read each, and there are ~55 null-bearing candidates to go.**
- **Two papers were read at source this cycle and BOTH contained a Type B or Type C error in the corpus's own entry.** That is **2-for-2 on a deliberately selected pair** — it is the strongest available argument that the rest are unchecked, and it is **emphatically not a population estimate.**
- **The 57-candidate sweep is regex-based.** It has false positives (positive findings caught by null-language, e.g. F-043, F-049, F-095, F-400) and certainly false negatives. **It is a floor on the count, not a census.**
- **No `1 − β` recomputation sweep was run.** F-463's rule — recompute every printed power figure — was applied to the four papers read this cycle (only Barrack printed one, an a-priori target, correctly labelled). **The registry-wide `1 − β` sweep remains unrun.**
- **F-044's original source (Ramsey, Crotin & White 2014, *Hum Mov Sci*, PMID 25457417) is STILL UNREAD.** Elsevier; absent from the PMC OA bucket. The correction rests on **two independent secondary descriptions**, one of them by the same research group about its own design. That is strong but it is not the paper.

---

## 9. RETRIEVAL NOTES (2026-09-30)

**Probe order per F-462, run before topic selection:**

| Host | Status |
|---|---|
| `pmc-oa-opendata.s3.amazonaws.com` | **200 — SERVING** |
| `storage.googleapis.com/arxiv-dataset` | **200 — SERVING** |
| `openalex.s3.amazonaws.com` | **200 — SERVING** |
| `ncaaorg.s3.amazonaws.com` | **200 — SERVING** |
| `biorxiv-src-monthly.s3.amazonaws.com` | 403 (requester-pays — the bucket answers) |
| `en.wikipedia.org` *(control)* | **000 — REFUSED** |
| `doi.org`, `frontiersin.org`, `thieme-connect.com`, `digitalscholar.lsuhsc.edu` | **000 — REFUSED** (`connect_rejected`) |

**FOUR PRIMARY TEXTS READ IN FULL:** PMC11590131 (Barrack 2024), PMC8486408 (Crotin & Ramsey 2021), PMC12011807 (Matsuda 2025), PMC11877241 (Tremblay 2025).

⚠️ **Guessing PMCIDs does not work and was abandoned within one call.** The pattern that works is unchanged and stated in F-351: **WebSearch for the PMCID, then `?list-type=2&prefix=PMC<id>` for the key list, then GET the `.txt`.** Note that **`prefix=PMC<id>` works and `prefix=oa_comm/txt/all/PMC<id>` returns zero keys** — the bucket is flat, keyed `PMC<id>.<ver>/`.

⚠️ **`scipy` and `numpy` are absent from the base image and install cleanly via `pip install scipy numpy`** (~40 s). `scipy.stats.nct.cdf` **returns NaN at large noncentrality** and will crash a `brentq` solve — guard every power computation with a NaN check and bisect rather than root-find.

⚠️ **One search-summary hazard logged:** a sweep on grip strength returned *"grip strength correlated with **exit velocity** but didn't add predictive value beyond height and weight — a marker, not a driver."* **That is a HITTING result** and would read as a pitching result to anyone skimming. It is not used anywhere in this file.
