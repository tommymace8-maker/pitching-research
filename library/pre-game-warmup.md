# THE PRE-OUTING WARM-UP — the bullpen before the first inning

**Opened 2026-09-20 (Cycle 18).** Findings **F-413 → F-424**. Companion: `daily/2026-09-20-report.md`.
**Six primary texts read in full.** Sister file: `library/between-inning-break.md`, which covers the *between-innings* warm-up and should not be confused with this one.

**Population as always: elite, 85 mph floor.** Every velocity in the primary literature on this topic is below that floor and is flagged.

---

## 0. The one-paragraph state of the topic

Three physiological channels are offered for the pre-game routine — **stretching**, **ball-weight priming**, **post-activation performance enhancement**. All three have been checked at the source and all three are nulls, two of them genuinely manipulated. The fourth channel, **motor calibration**, has never been measured in throwing by anybody. Meanwhile the only well-measured property of the pre-game bullpen is its **size**: 27.2 ± 9.4 pitches, and ~45% of a season's total pitches are thrown outside the pitch count, a proportion invariant from high school to a professional organisation. **The routine is large, variable by a factor of two, and untested.**

---

## 1. What a warm-up can do to tissue, and on what clock

| Channel | Mechanism | Time course | Reaches a pitch? |
|---|---|---|---|
| Muscle temperature | Q₁₀ on cross-bridge cycling; reduced viscous resistance | rise over 5–15 min; decay τ ~300–1800 s | Reaches **lower-body power**. F-004 / F-358 / F-359 say that does not reach a fastball here. |
| Phosphagen readiness | PCr availability | half-time 20–30 s (F-132) | **Irrelevant pre-game.** A rested pitcher is saturated. Only bites within an outing. |
| Post-activation potentiation | myosin RLC phosphorylation, Ca²⁺ sensitivity | peak 3–10 min, coexists with fatigue | **F-415: did not beat a general warm-up in three RCTs.** |
| Motor calibration | not a tissue property — a skill property | unknown | **The only channel nobody has falsified, and the only one nobody has measured.** |

**The structural point:** the first three are capacity channels. This population is not capacity-limited at the margin in ways a 30-minute routine can move, and restriction of range (Luera 2020, n = 149 pros, r = .17–.29) says an acute capacity nudge has *less* room in an 85+ arm, not more. **A null at 75 mph is conservative for 92 mph, provided the mechanism is capacity.** It says nothing if the mechanism is skill — which is why the surviving hypothesis is a command hypothesis, and why that relocation is itself contested (Dispute #33).

---

## 2. The evidence, ranked by how much it is worth

| # | Study | Design | n | Sample's actual velocity | Verdict |
|---|---|---|---|---|---|
| 1 | **Shin & Choi 2018** (PMC6028211) | within-subject, 3 warm-up ball weights → max-effort RB | 12 | **75.1 mph** | **MANIPULATED NULL, 0.52 mph wide, F = 0.138, p = 0.871. Manipulation verified at the muscle by EMG.** |
| 2 | **Rappelt 2024** (PMC11350113) | 3 randomised crossover RCTs, 6 conditioning activities, **general-warm-up anchor** | 66 | n/a (jump height) | **MANIPULATED NULL. No condition effect or interaction anywhere. Best jump of the day was at PRE.** |
| 3 | **Zaremski 2018** (PMC5894908) | observational count, trained independent observers | 115 outings / 13,769 pitches | HS varsity | **DESCRIPTIVE. Pre-game bullpen 27.2 ± 9.4. 42.4% hidden.** |
| 4 | **Erickson 2023** (PMC10102946) | observational count, team staff | 137 pitchers, full season | professional org | **DESCRIPTIVE. 45.4 ± 13.3% hidden. Injury null, p = .15.** |
| 5 | **Krzysztofik 2021** (PMC7844331) | meta-analysis, 11 studies | 174 | n/a (bench-press throw) | **ES = 0.33 — but it is a PRE-POST pool with no warm-up control. F-415 decomposes it.** |
| 6 | **Williams 2013** (PMC4590899) | randomised counterbalanced crossover | 27 | **61.4 mph peak** | **NULL on an unusable population. Its only significant result is below its gun's ±1.0 mph error.** |
| 7 | **Stastny 2023** (PMC10044369) | crossover, 3 conditioning activities | 13 | n/a (seated MB chest pass) | **CONSTRUCT MISMATCH. Not a throwing study.** |
| — | **Haag 2010** (JSCR 24(2):452–457, PMID 20072054) | crossover, NCAA D-III **pitchers** | unknown | **unknown** | ⚠️ **SNIPPET-ONLY, EGRESS-BLOCKED. The only on-population study on this topic and this corpus has not read it. Verification queue.** |

### 2.1 The one result worth memorising

**Shin & Choi's warm-up throws differed by 22 mph across conditions (LB 75.2 mph, OB 53.4 mph, p < 0.001) and the subsequent max-effort fastball differed by 0.52 mph (p = 0.871).** The EMG confirms the arm genuinely did something different in each condition. **The sensation is real and it is not the mechanism.**

### 2.2 The methodological lesson worth more than any of the numbers

**Krzysztofik's ES = 0.33 is a within-condition pre-post difference.** *"Meta-analyses of standardized mean effect size (ES) between pre-CA mean and post-CA mean from individual studies were conducted."* There is no arm that simply kept warming up. **Rappelt's three trials are exactly the decomposition of that quantity, and when the general-warm-up anchor is inserted, the effect goes away.** This is the same structural error as F-358's re-warm-up meta-analysis: an intervention arriving with the strongest credential in sports science, measuring the wrong contrast.

---

## 3. The thermal derivation for the pre-game gap (F-419)

Corpus model (F-356, `between-inning-break.md` §2): exponential decay calibrated so **ΔT(900 s) = 1.5 °C**, converted at **~3% lower-body power per 1 °C**.
A = 1.5/(1 − e^(−900/τ)) → **1.579 (τ=300), 1.931 (τ=600), 3.812 (τ=1800)**.

| Elapsed | τ=300 | τ=600 | τ=1800 | Range | ≈ power @3%/°C |
|---|---|---|---|---|---|
| **120 s** (inning break) | 0.52 | 0.35 | 0.25 | 0.20–0.52 °C | 0.6–1.6% |
| **480 s** | 1.26 | 1.06 | 0.89 | 0.89–1.26 °C | 2.7–3.8% |
| **600 s** | 1.37 | 1.22 | 1.08 | 1.08–1.37 °C | 3.2–4.1% |
| **1200 s** | 1.55 | 1.67 | 1.86 | 1.55–1.86 °C | 4.7–5.6% |

**Interval scale:** MLB 2025 nine-inning games average **2:38**; across ~17.5 half-innings that is ~**9.0 min per half-inning including its ~2:05 break**. The visiting starter's bullpen-to-first-pitch gap therefore exceeds the home starter's by roughly one half-inning.

⚠️ **Three caveats, all conceded within cycle.**
1. **The τ bracket is a guess and the curves CROSS between 600 s and 1200 s** — τ=1800 gives the smallest ΔT at 600 s and the largest at 1200 s. The range width reflects ignorance of τ, not measurement error. (Cross-examination ③, partially conceded.)
2. **The 8 warm-up pitches on the game mound are themselves a re-warm-up**, and F-362 found warm-up timing inside a break barely matters. The derived 3–4% is an upper bound on an upper bound. (**Dispute #34.**)
3. **Do not convert lower-body power into mph.** The corpus has forbidden that conversion since F-357, and F-004 / F-358 / F-359 are why.

**Conclusion: the pre-game gap is 2–4× the inning break on this channel, and the corpus's verdict on the inning break was "the margin is not close." Four times not-close is still not close.**

---

## 4. What to do — and the precise limit of what is licensed

### The recommendation, worded to survive the marker/lever rule
**Do not ADD pre-game work in pursuit of velocity.** That is a null-supported prohibition on addition, which is what F-415 and F-413 license.
**This corpus does NOT license "cut the pen."** Nobody has manipulated bullpen volume downward, there is a real floor, and the removal experiment has never been run. (Cross-examination ⑤, conceded.)

### The cue that survives
*"Your pen is done when you've located your three pitches, not when you've hit a number."*

### The audit (F-421) — one line per outing
Record per starter per outing: **(a) pre-game bullpen pitch count, (b) first-inning first-fastball velocity, (c) first-inning strike%, (d) first-inning location SD if TrackMan is running.**

**Detection.** Two-sample, α = .05, 80% power, n per group = **15.7 σ²/Δ²**, at within-pitcher release-speed SD **σ = 1.0 mph** (F-289):

| Δ to detect | Outings per bucket | Total |
|---|---|---|
| 1.0 mph | 16 | 32 |
| 0.75 mph | 28 | 56 |
| 0.5 mph | 63 | 126 |

A 14-arm staff at ~15 outings each ≈ **210 outings a season** → **a median split detects 0.5 mph inside one season at staff level**, and 1.0 mph inside one starter's two seasons. For command, ~15–20 first-inning pitches per outing means **~12 outings per bucket** reaches the corpus's ~200-tracked-pitch threshold. **Command is the cheaper measurement, and it is the channel still alive.**

**Two confounds, designed around, not ignored:**
- **Endogeneity.** Bullpen volume is not random — a pitcher who feels bad throws more, which biases the naive regression *toward manufacturing a negative result*. Use the residual of pen count after regressing on pitcher identity and days' rest, or restrict to outings where volume varied for scheduling reasons.
- **Lineup composition.** First-inning *outcomes* are contaminated by facing slots 1–3 with certainty (F-287, F-424). **Velocity and location SD are immune; ERA and strike% are not.**

### The bonus instrument (F-420)
For visiting starts only, regress first-inning velocity and location SD on the **pitch count of the top of the first**. Within-pitcher; the predictor depends on the opposing pitcher and your own offence, not on him.
**The two hypotheses make opposite predictions: thermal moves velocity and not scatter; calibration moves scatter and not velocity; F-004's transfer null predicts neither moves.**
⚠️ Use pitch count rather than runs or elapsed time (a long scoreless half-inning carries the time cost without the lead), and carry runs scored as a covariate — F-365 says pressure raises peak output in elite college players, which would push against the thermal prediction. **Do not substitute home-vs-away**: that is confounded with travel, sleep (F-410), crowd and umpire.

---

## 5. What is not known

1. **No measured pitch-location outcome as a function of warm-up state, anywhere.** Six papers this cycle, six velocity-or-count outcomes, zero accuracy outcomes. This is the topic's largest hole and it is larger than the sleep topic's.
2. **No dose-response study of warm-up throw NUMBER** in baseball, handball or tennis (F-423). The handball literature standardises at "8–10 free-ball throws" and treats it as a nuisance constant.
3. **No published distribution of the college bullpen-to-first-pitch interval.** §3 is bracketed for this reason. It is a stopwatch and a season.
4. **Haag 2010 is unread** — the only on-population acute study in the topic.
5. **Nobody knows whether 27 is the right number**, or whether 18 and 37 produce different first innings.

---

## 6. Fabrication watch

🚨 **"Statcast data shows pitchers who complete a full bullpen warm up average 0.8 mph higher velocity in the first inning compared to those who abbreviate their prep."** — **F-422. Do not import.** Public Statcast is 12 Hawk-Eye cameras per park covering the field of play; there is no public bullpen tracking and no variable encoding warm-up completeness. **Both published bullpen-volume studies had to count by hand** — Zaremski used human observers, Erickson used the Phillies' own staff. If the data were in Statcast, neither would have needed to.

Also logged: **Driveline's "prime the nervous system with medicine ball rotational scoop tosses"** — the named mechanism is PAPE and F-415/F-416 are this corpus's answer (UNPROVEN, and note the recommendation is *low-volume*, which is accidentally the right practical advice reached through the wrong mechanism). **"Dynamic warm-ups improve vertical jump 3–5%"** — probably true and beside the point (F-358 trap); note that Rappelt's PRE measurement *is* the post-dynamic-warm-up measurement and it was the best jump of the day. **Coaching-consensus "15–20 pitches in the pen"** — FOLKLORE, and it disagrees with the only measurement (27.2) by ~40%.

---

## 7. Cross-links

- `library/between-inning-break.md` — the *between-innings* warm-up. F-351→F-364. The thermal model in §3 is borrowed from its §2.
- `library/velocity-development.md` — F-004, the jump-height transfer null that kills the thermal channel here and has now killed four channels in six cycles.
- **F-287 / F-424** — lineup composition bias, which is why the outcome variables in §4 are velocity and location SD.
- **Dispute #33** — whether relocating a velocity null into a command claim is a finding or a house style. Open, and this file's §1 conclusion is one of the two data points.
- **Dispute #34** — whether the 8-pitch mound warm-up erases the pre-game thermal gap.
