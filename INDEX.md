# INDEX — Navigation Map for the Pitching Research Corpus

**Compiled 2026-08-17.** Companion to [`FINDINGS.md`](FINDINGS.md), the flat registry of 244 verified findings.
Population scope: **elite throwers, 85 mph floor** — elite HS prospect (showcase / D1-committed / draft-followed) -> NCAA D1 -> MiLB -> MLB, chasing 90-95+. Mission is **performance development**, not injury prevention; stress costs are tagged and the work moves on.

**How to use this corpus, in order:**
1. **`FINDINGS.md`** — search here first. Every finding, one entry, greppable by `TOPIC`, `EVIDENCE`, `CAUSALITY`, `POPULATION`.
2. **This file** — to find which source document to open and to see what is settled vs contested.
3. **`library/*.md`** — the full argument, with citations and caveats.
4. **`daily/*.md`** — dated snapshots. **NOT current reference** (see Known Corrections).

---

## 1. The corpus, file by file

| File | Size | Last updated | What is in it | Questions it answers |
|---|---|---|---|---|
| **`library/velocity-development.md`** | 1,144 lines / 153 KB — **largest** | 2026-08-13 | What adds mph to an 85+ arm and how to train it. Physical-quality correlates; the complete verified weighted-implement intervention table; where velocity comes from mechanically; program design; the ceiling; a named fabrication list | "Will this add velocity?" "What should he test on a force plate?" "How much can an 88 mph arm realistically gain?" "Do weighted balls work?" "What is the aging curve?" |
| **`library/stuff-and-command.md`** | 1,258 lines / 134 KB | 2026-08-13 | Pitch physics (spin, Magnus, seam-shifted wake, extension, VAA); per-pitch design tables computed from Statcast; arsenal construction and stuff models; command as an angular problem; motor learning; command training | "What should this pitch look like?" "Is spin trainable?" "Why doesn't he command it?" "Is external focus real?" "How long before I can believe a command win?" |
| **`library/anatomy-physiology.md`** | 811 lines / 96 KB | 2026-08-12 | The kinetic chain ground-up; the physiology of a high-intent pitch and outing; the adapted tissue state of the elite thrower; injury mechanisms at tissue tolerance; recovery physiology; coach-facing referral tables | "What is actually resisting valgus load?" "Is this scan normal for a pro?" "What is dead arm?" "How do I structure the week between starts?" "When do I refer?" |
| **`library/coaching-translation.md`** | 679 lines / 75 KB | 2026-08-13 | Science -> cue -> drill -> what failure looks like on video. Four standing rules; the cue ledger with stress costs; the foot-plant-to-MER deep dive; effort dosing; arm slot; command and variability; constraint heuristics; video protocol; retired cues | "What do I actually SAY to him?" "What drill makes this happen without a cue?" "What am I looking for at 240 fps?" "Which cues have been retired and why?" |
| **`library/biomechanics.md`** | 716 lines / 64 KB | 2026-08-12 | Six phases and timing landmarks; ASMI professional kinematic and kinetic norms; the kinematic sequence; velocity-vs-torque conflicts; measurement technology | "What are the pro norms?" "How long is each phase?" "What raises torque without raising velocity?" "What can I measure with what I own?" |
| **`library/open-disputes.md`** | 461 lines / 58 KB | 2026-08-13 | Sixteen unresolved arguments among the anatomist, the biomechanist and the coach, each with both sides, the strongest evidence, and what would settle it. Plus the standing methodological disputes | "Is this settled?" "What would I have to run to find out?" "Where do the three specialists actually disagree?" |
| **`library/idea-scouting.md`** | 413 lines / 45 KB | 2026-08-13 | Two field sweeps of what the industry is arguing about right now, each item labelled PROMISING / UNPROVEN / DEBUNKED / MARKETING. Content-farm blocklist and hazard classes | "Is this new thing real?" "What is the industry selling this month?" "What did we look for and NOT find?" |
| **`src/core/biomech/references.ts`** | 830 lines | — | ~30 structured citations with `EvidenceGrade`, `Population`, `Causality`, caveats and dated `corrected` records. Kinematic and kinetic norm bands, the four "free reductions," the velocity-torque conflict table, and the `MARKERS_NOT_LEVERS` list | "What grade and causality does this citation carry in code?" "Which variables must never be rendered as coachable?" |
| **`daily/2026-08-12-biomechanics.md`** | 74 lines | 2026-08-12 | Day 1 biomechanics brief | Quick orientation only |
| **`daily/2026-08-12-anatomy.md`** | 55 lines | 2026-08-12 | Day 1 anatomy brief | Quick orientation only |
| **`daily/2026-08-12-coach.md`** | 137 lines | 2026-08-12 | Day 1 field sweep, the foot-plant interrogation, cross-examination, three challenges each to the anatomist and biomechanist | The Day-1 disagreements, verbatim |
| **`daily/2026-08-13-velocity.md`** | 122 lines | 2026-08-13 | Day 2 velocity brief | **CONTAINS UNCORRECTED PRE-CORRECTION TEXT** — see Known Corrections |
| **`daily/2026-08-13-stuff-command.md`** | 90 lines | 2026-08-13 | Day 2 stuff/command brief | **CONTAINS THE REVERSED CHANGEUP FRAMING** — see Known Corrections |
| **`daily/2026-08-13-coach.md`** | 518 lines / 67 KB | 2026-08-13 | The single most important document in the corpus for epistemics: the full correction log, the outstanding-verification list, the core-coiling scouting, and the analysis of what six corrections in one day implies | "What did we get wrong and why?" "What is still unverified?" "How should verification work?" |
| **`research/README.md`** | 75 lines | — | Program scope, the three-agent team, how a research day works, ground rules | "What is this program and what is out of scope?" |

**Total corpus:** ~6,500 lines of research across 7 library files, 6 daily briefs, and one structured citation module.

---

## 2. Topic -> file / finding lookup

### Velocity development
| Sub-topic | Primary file | Findings |
|---|---|---|
| Physical-quality correlates (mass, impulse, RSI, power) | `velocity-development.md` §2 | F-001 to F-009, F-018 to F-022 |
| Anthropometry and the non-trainable share | `velocity-development.md` §2.3, §6.1 | F-010, F-011, F-012, F-078 |
| The published nulls (grip, RFD, mobility, core endurance, jump height, per-kg) | `velocity-development.md` §2.1, §2.4, §2.5 | F-004, F-005, F-013, F-014, F-015, F-016 |
| Weighted implements | `velocity-development.md` §3.1-3.3; `open-disputes.md` #8 | F-024 to F-032, F-222, F-227 |
| Non-implement interventions that worked | `velocity-development.md` §3.4 | F-033, F-034, F-037 |
| The "keep lifting" question | `velocity-development.md` §5.5; `open-disputes.md` #14 | F-036, F-039, F-083 |
| Program design, blocks, autoregulation | `velocity-development.md` §5 | F-084, F-085, F-086 |
| The ceiling, aging, base rates | `velocity-development.md` §5.6, §6 | F-072 to F-081 |
| Realistic expectation-setting with an athlete | `daily/2026-08-13-coach.md` §2 | F-072, F-080, F-243 |

### Stuff and pitch design
| Sub-topic | Primary file | Findings |
|---|---|---|
| Spin, Magnus, efficiency, gyro | `stuff-and-command.md` §2.1-2.2 | F-142 to F-146 |
| Seam-shifted wake | `stuff-and-command.md` §2.3 | F-147, F-148, F-149 |
| Extension and perceived velocity | `stuff-and-command.md` §2.4 | F-150 |
| Vertical approach angle | `stuff-and-command.md` §2.5 | F-151, F-152 |
| Per-pitch design targets and league baselines | `stuff-and-command.md` §3 | F-154 to F-160 |
| Arsenal construction and tunneling | `stuff-and-command.md` §4.1-4.2 | F-161, F-163, F-164 |
| Stuff models and their limits | `stuff-and-command.md` §4.3-4.5 | F-165 to F-168, F-233 |
| Spin-efficiency trainability | `idea-scouting.md` Sweep 2 #5; `open-disputes.md` #15 | F-153, F-235 |

### Command
| Sub-topic | Primary file | Findings |
|---|---|---|
| The angular framing (30 cm per degree) | `stuff-and-command.md` §5 | F-171, F-172, F-174 |
| Release-point variability debunking | `stuff-and-command.md` §6 | F-175 |
| Mechanical signature of plus command | `stuff-and-command.md` §7 | F-176, F-177, F-178 |
| Repeatability vs adjustability | `stuff-and-command.md` §8 | F-109, F-179, F-180, F-181 |
| Measuring command / the intent problem | `stuff-and-command.md` §9 | F-182, F-183, F-184 |
| Training command | `stuff-and-command.md` §11; `coaching-translation.md` §11 | F-173, F-185, F-186 |
| Value of command vs stuff | `stuff-and-command.md` §1 | F-169, F-170 |

### Mechanics and kinematics
| Sub-topic | Primary file | Findings |
|---|---|---|
| Phases, landmarks, durations | `biomechanics.md` §2 | F-087, F-088 |
| Professional norms (kinematic and kinetic) | `biomechanics.md` §3-4 | F-089, F-090, F-091, F-092, F-098 |
| Stride length — the worked marker-vs-lever example | `velocity-development.md` §4.4; `open-disputes.md` #13 | F-043 to F-048 |
| Levers you pay for, with exchange rates | `velocity-development.md` §4.5 | F-050 to F-054, F-099 |
| The "free" torque reductions | `biomechanics.md` §6.4; `open-disputes.md` #1 | F-100, F-101 |
| Ground reaction force and the lead-leg block | `biomechanics.md` §4.6; `velocity-development.md` §4.6 | F-060, F-061, F-062, F-063 |
| Energy flow and power accounting | `velocity-development.md` §4.1-4.2 | F-064 to F-068 |
| The kinematic sequence | `biomechanics.md` §5; `open-disputes.md` #11 | F-105 to F-111 |
| Arm slot | `coaching-translation.md` §5; `open-disputes.md` #10 | F-070, F-071, F-104 |
| Efficiency (velocity per unit torque) | `biomechanics.md` §4.5; `open-disputes.md` #3 | F-093, F-094, F-103 |

### Anatomy and tissue
| Sub-topic | Primary file | Findings |
|---|---|---|
| The kinetic chain, structure by structure | `anatomy-physiology.md` §2 | F-112, F-113, F-114 |
| UCL load-sharing and the failure-load question | `anatomy-physiology.md` §1.3, §5.1; `biomechanics.md` §4.4 | F-097, F-113, F-121, F-141 |
| Humeral retrotorsion, GIRD, total rotational motion | `anatomy-physiology.md` §4.1-4.3 | F-115, F-116, F-117, F-118 |
| Imaging baselines in asymptomatic throwers | `anatomy-physiology.md` §4.6 | F-120, F-121 |
| Scapula, laxity, dyskinesis | `anatomy-physiology.md` §2.7, §4.4-4.5 | F-119, F-122, F-123 |
| Elite-specific injuries (oblique, lat/teres, TOS) | `anatomy-physiology.md` §2.5-2.6, §5.5 | F-124, F-129, F-130 |
| Fatigue mechanisms | `anatomy-physiology.md` §3.2-3.3 | F-125 to F-129, F-131 |

### Training transfer and program design
| Sub-topic | Primary file | Findings |
|---|---|---|
| What has an intervention study, and what does not | `velocity-development.md` §3, §7 | F-023, F-033 to F-038 |
| Effort-level dosing | `coaching-translation.md` §4; `open-disputes.md` #6 | F-211 |
| Constraint design | `coaching-translation.md` §7 | F-212 |
| Concurrent training and conditioning | `velocity-development.md` §5.3; `anatomy-physiology.md` §3.1 | F-042, F-132 |
| Transfer lag and time course | `velocity-development.md` §5.2 | F-084, F-085 |
| Detecting whether anything worked | `coaching-translation.md` §11.13 | F-186, F-243 |

### Skill acquisition and motor learning
| Sub-topic | Primary file | Findings |
|---|---|---|
| Acquisition vs learning | `stuff-and-command.md` §10.1 | F-187, F-188 |
| Attentional focus and OPTIMAL theory | `stuff-and-command.md` §10.2 | F-189, F-190, F-191 |
| Contextual interference, variable practice, differential learning | `stuff-and-command.md` §10.3-10.4 | F-193, F-194 |
| Constraints-led approach | `stuff-and-command.md` §10.5 | F-195 |
| Feedback and the guidance hypothesis | `stuff-and-command.md` §10.6 | F-192 |
| Transfer, specificity, representative design | `stuff-and-command.md` §10.7 | F-197 |
| Speed-accuracy in overarm throwing | `stuff-and-command.md` §10.8 | F-196 |
| Dosage, spacing, sleep | `stuff-and-command.md` §10.9 | F-198 |

### Measurement and technology
| Sub-topic | Primary file | Findings |
|---|---|---|
| Markerless capture accuracy | `biomechanics.md` §7.2 | F-199, F-200, F-201 |
| IMU sleeves and the "Stress" metric | `biomechanics.md` §7.3 | F-202 |
| Filter and sampling frequency | `coaching-translation.md` §8 | F-203 |
| Video protocol and what 2D can claim | `biomechanics.md` §7.6 | F-204, F-205 |
| Ball/pitch tracking systems | `biomechanics.md` §7.4 | F-206 |
| Force plates | `biomechanics.md` §7.5; `open-disputes.md` #4 | F-207 |
| Lab vs game velocity | `biomechanics.md` §0 | F-208 |
| What to buy, in order | `biomechanics.md` §7.6 | F-209 |
| Datasets and how to cite them | `velocity-development.md` §8 | F-210, F-221 |

### Workload
| Sub-topic | Primary file | Findings |
|---|---|---|
| Total high-intent volume as the exposure variable | `anatomy-physiology.md` §1.6, §3.4 | F-136 |
| Long toss as mound-equivalent load | `idea-scouting.md` Sweep 1 #2 | F-137 |
| ACWR and its contested thresholds | `anatomy-physiology.md` §3.4 | F-136 |
| The showcase hazard | `anatomy-physiology.md` §3.4, §6.5 | F-136, F-214 |
| Recovery, collagen balance, the between-start map | `anatomy-physiology.md` §6 | F-133, F-138, F-139, F-140, F-214 |
| Autoregulation and in-season | `velocity-development.md` §5.4; `anatomy-physiology.md` §6.4 | F-082, F-083, F-086, F-123 |

---

## 3. Settled versus contested

### What this corpus treats as ESTABLISHED
These are replicated across independent studies, or are undisputed basic mechanics or physics. Coach off these.

- **Velocity is not the injury risk factor; torque is** — velocity did not differ between UCL-surgery and healthy groups in 305 MiLB pitchers followed 4.5 years (F-095).
- **But within one athlete, velocity and torque are locked** at R2 = 0.957, while between athletes the association nearly vanishes at R2 = 0.076 (F-094).
- **The exchange rate varies ~28% across elite arms at the same velocity** (F-093).
- **Foot contact is where the delivery is decided** — arm cocking is 100-150 ms, acceleration 30-50 ms (F-088).
- **Absolute output predicts velocity; relative output and jump height do not** — mass r = 0.58, lean mass r = 0.52, CMJ impulse r = 0.71, jump height r = 0.07 NS, power-per-kg r = 0.19 NS (F-001 to F-005).
- **Height dominates every velocity model that includes it** — 81.2% of variable importance in n = 322 D1 (F-010).
- **Explanatory power collapses with selection** — 93% of velocity variance in HS, 54% in professionals, 29% in the largest in-game D1 model (F-055, F-056).
- **The published velocity-training effect shrinks toward zero as baseline rises** (F-025).
- **In-season velocity RISES ~0.6 mph; it does not decay** (F-082).
- **Command is an ANGULAR problem** — ~30 cm of plate location per 1 degree of release angle, versus 1 cm per 1 cm of release position. This is trigonometry (F-171).
- **Release-point variability does not predict walks** (R2 = 0.011, n = 344 MLB) — it is a deception variable (F-175).
- **The textbook kinematic sequence is essentially never observed**, across three independent samples (F-105, F-106).
- **The one supported sequence fault is trunk-before-pelvis** (F-107).
- **"Abnormal" imaging is the baseline in asymptomatic elite throwers**, and does not predict injury-list placement (F-120, F-121).
- **Fatigue neurally inhibits the infraspinatus**, and command degrades before velocity (F-125, F-127).
- **Acquisition is not learning** (F-187).
- **The guidance hypothesis is falsified** (F-192).
- **Torque is not comparable across labs**, and sampling/filter frequency is the mechanism (F-091, F-203).
- **Lab velocity is 5-8 mph below game velocity** (F-208).
- **Markerless kinematics are good; markerless kinetics are not** (F-199).
- **Motus/PULSE "Stress" is not elbow varus torque** (F-202).

### What is CONTESTED — the sixteen open disputes
Full argument, both sides, and what would settle each, in `library/open-disputes.md`.

| # | Dispute | Status |
|---|---|---|
| 1 | Are the four "free" torque reductions actually modifiable in an 85+ arm without velocity loss? | NARROWED — coach's answer: start with shoulder abduction at FC and only there |
| 2 | Is elbow flexion at FC an independent variable, or just "arm path" wearing a number? | OPEN — coach refuses to cue it; settled by a mediation analysis in the ASMI dataset |
| 3 | Can mechanics decouple velocity from varus torque WITHIN an individual? | OPEN — **the central question of the program**; nobody has demonstrated a within-athlete curve shift |
| 4 | Force plates versus modeled torque — what to buy and what to believe | NARROWED — buy them, but directly measured is not the same as important, and the meaningful quantity has no elite norms |
| 5 | Is there a dugout-measurable posterior-cuff activation marker that fires before command drifts? | OPEN — coach argues the request may be malformed, since the deficit is central |
| 6 | Does "vary your effort" reduce load, or mostly reduce velocity? | OPEN — three datasets disagree on whether kinematics are preserved at submaximal effort |
| 7 | Is the lead-leg block worth coaching given that it RAISES torque? | OPEN — described as the most tractable dispute on the list |
| 8 | Weighted implements in a mature 85+ arm | OPEN — the field is settling a deceleration/cumulative-load question with a concentric-phase study |
| 9 | Does "the block whips the hips" deserve FULL retirement? | NARROWED — cue is dead; whether pelvis rotation after foot plant is irrelevant or merely uniform is unresolved |
| 10 | Lower arm slot — universal recommendation or individual? | NARROWED — a same-handed weapon that reshapes the whole arsenal, not a universal upgrade |
| 11 | The kinematic sequence | **CONCEDED by the coach, 2026-08-12** — replicated in two larger independent samples |
| 12 | Does the velocity-optimal delivery cost command? | OPEN — added 2026-08-13, revisited same day; drifting toward "the trade may be a mirage" |
| 13 | Is stride length a velocity LEVER, or only a CORRELATE? | OPEN — added 2026-08-13; two independent failed manipulations, one showing harm |
| 14 | Is "keep lifting = floor protection" a real asymmetry or a design artifact? | **LARGELY RESOLVED in the coach's favour, 2026-08-13** — the underlying physiological question stays open |
| 15 | Is spin efficiency trainable, and does the industry price the cost honestly? | OPEN — added 2026-08-13; ~65% fixed over three years, and the one documented mover bought a delivery change |
| 16 | Does release-angle precision have any coachable channel? | OPEN — added 2026-08-13; true, geometric, and possibly inert as an instruction |

**Standing methodological disputes** (not attributable to one agent): torque values are not comparable across labs; lab velocity is not game velocity so all published kinetics are probably a floor; 60% of normalized elbow torque variance is unexplained by kinematics; every professional norms table is survivorship-selected; verifying a citation is not verifying a claim; and "one experiment, many papers" (the Buffalo stride cohort appears across at least seven publications).

---

## 4. Known corrections — applied 2026-08-13. Do not re-import.

Six corrections landed in one day. **None was a fabrication.** Every one was a real source, correctly cited, read slightly wrong — and **all six erred in the same direction, toward more confidence than the source supported.** Full analysis in `daily/2026-08-13-coach.md` §9 and §11; registry entry F-240.

| # | Was | Is | Reverses a conclusion? | Finding |
|---|---|---|---|---|
| **1** | "Stride length toward >=80% BH is the best mechanical lever" / "nobody has lengthened a professional's stride" | **Two independent groups manipulated stride length. Neither found a gain and one found lengthening made pitchers SLOWER.** Marker, not lever. Demoted from recommendation #2; cue retired; the "~1-1.5 mph sitting there" line deleted | **YES** | F-043, F-044, F-045 |
| **2** | "Velocity showed virtually no correlation with changeup whiff rate" — which collapsed absolute velocity and velocity separation and **inverted the source** | The source's main argued chain is **velocity GAP -> hitters out front -> whiffs**, called strong. What has no relationship is **ABSOLUTE** changeup velocity. The two nulls in that article are single unquantified sentences, not "published nulls" | **YES** | F-159, F-232 |
| **3** | Driveline >=88 mph cohort **+1.35 mph** | **+0.65 mph** (89.6 -> 90.3, n = 58, mean age 23, mean 67 days), verified two ways. Also: "58 high-level athletes," not explicitly professionals; byline Neiswender, closing credit Aucoin | **YES — and it makes the ceiling HARSHER** | F-072 |
| **4** | "There is not a single published controlled training study whose sample mean is at or above 85 mph. Not one." | **Two clear the floor.** Ake 2016 baseline is 87.25 / 86.80 mph (the corpus had recorded it as "not reported") — still null. And Lee/Choi/Jeon 2026 is the **first positive controlled result above 85** | Partially — the structural argument survives, the absolutism does not | F-023, F-024, F-034, F-226 |
| **5** | "n = 1,163 pitcher-seasons," mean **-1.15 mph** | **Pitcher x pitch-type x consecutive-season PAIRS** — one pitcher can contribute two rows, and the rows are not independent. And **the -1.15 mean is internally inconsistent with the source's own distribution** — probable source error | Caveat, not reversal | F-073 |
| **6** | Gdovin 2025 called a **"removal experiment"** / "natural-experiment removal design," and named the **#1 highest-confidence recommendation** | It is *"Limiting Access to Resistance Training Equipment During the Off-Season"* — an **uncontrolled 8-week pre-post with NO control group.** PMID, n = 12 and p < .001 are all correct; the **mph magnitude is paywalled and was never obtained.** Recommendation #1 re-justified on the correlational case and demoted below #2b; label moved EMERGING -> WEAK | **YES** | F-039 |

**Plus two label fixes:** first author on PMID 34240663 is **Manzi**, not Dowling. And **both Kusafuka 2025 coefficients were mis-described** — r = 0.54 is not an autocorrelation value and r = 0.73 is not a "staying-in-the-same-state" probability; both are correlations *between* a per-pitcher correction statistic and that pitcher's azimuth release-angle SD. The direction of the coaching claim survives; the labels did not.

**Also corrected earlier the same day:** Bloebaum's uncontrolled-manifold synergy index (rho = 0.22, p < 10^-47, 43,650 pitches / 2,052 pitchers) is an association with **PITCH VELOCITY, not command.** `idea-scouting.md` #3 and `coaching-translation.md` §6 both carried it in a command context; both were corrected (F-109).

**Verified clean and marked so, to avoid re-checking:** Kusafuka 2020 (PMID 33345028, 30 cm per 1 degree for both elevation and azimuth); Wakamiya 2024 (PMC11608975, n = 344 MLB starters, BB/9 R2 = 0.011, K/9 0.345, HR/9 0.072); Dowling 2022 (PMID 36479467, n = 157, 39.1 +/- 1.7 vs 38.4 +/- 2.1 m/s, P = .029, torque P = .311); Ludwig/Brill/Wyner (arXiv:2508.19184, 1 inch of fastball xCTRL ~ 0.3 FIP, Gausman 7.05 in, inter-season r = 0.65).

> ### THE OPERATING RULES THAT CAME OUT OF THIS
> **(A)** Verifying a citation is not verifying a claim. Ask two further questions: *does the source support THIS sentence, or a weaker one?* and *what was the ACTUAL DESIGN, and is there a control group?* **Never infer a design from a p-value.**
> **(B)** Secondary sources are not the hazard — our own prose is. The corruption happens in the compression from paper -> table row -> recommendation. **Any claim promoted to a numbered recommendation gets re-read against the primary source before it ships.**
> **(C)** The same scrutiny applies to disconfirming evidence. The coach presented one 19-athlete cohort as multiple independent studies, in the direction he was already arguing, on the same day he accused colleagues of the same error.
> **(D)** Sample sizes are verified on the paper's own page — never from a search summary, an abstract aggregator, or another paper's citation of it.

### Two live re-import vectors

1. **The daily briefs were never corrected.** `daily/2026-08-13-velocity.md` still asserts "not one study at 85+," "+1.35 mph," "mean -1.15 mph," the Gdovin removal framing, and stride length as one of "the two free mechanical levers." `daily/2026-08-13-stuff-command.md` still carries the reversed changeup framing. **These are dated snapshots, not current reference.** (F-241)
2. **Internal inconsistencies not yet resolved** — five figures appear at different values in different files, including the interval-throwing throw count (238,611 vs 111,196), the OpenBiomechanics metric count (81 vs 76), the 2008/2026 league-average velocities, and shoulder IR velocity (5,456-6,149 deg/s from the ASMI table vs "7,000-7,500 deg/s" in the anatomy file, the latter explicitly flagged as unverified). (F-231)

### Outstanding verification backlog
Named in `daily/2026-08-13-coach.md` §9b and registered as F-242. **Do not treat any claim as vetted merely because it survived 2026-08-13.** Priority order: (1) two items pre-flagged as HIGH fabrication risk that never reached a verifier — the only items still carrying an active fabrication flag; (2) the Bloebaum SportRxiv 871 sample size, which has an actively circulating phantom n; (3) the Gdovin mph magnitude, since the corpus quotes a p-value with no effect size. Also outstanding: Bloebaum 919 effect sizes; the Smith/Smith/Bowman 2017 SABR stride manipulation (grey literature, never independently verified); the Nevada/Reno (Buck) thesis outcomes; and the Baseball America college-to-pro cohort.

---

## 5. Coverage gaps — what this corpus does NOT yet cover

### Gaps in the literature itself (searched for, confirmed absent)
- **No controlled velocity trial in PROFESSIONAL pitchers with velocity as an outcome.** Two controlled samples clear 85 mph; neither is professional (F-023).
- **No mass-gain or lean-mass intervention in pitchers with a velocity outcome** — despite mass being the strongest correlate in the entire literature (F-001, F-002).
- **No RSI-training intervention with a velocity outcome** (F-006).
- **No intervention trial on any of the four "free" torque reductions** (F-100).
- **No transfer-lag measurement anywhere** — baseball, handball, any throwing sport (F-084).
- **No periodization comparison in pitchers** with a velocity outcome; no detraining/retraining velocity data (F-038).
- **No controlled mechanics-coaching intervention with a velocity outcome at 85+** (F-038).
- **No longitudinal stride-lengthening intervention.** The only near-miss is an unpublished 2026 Nevada/Reno master's thesis with no velocity outcome and no control group (F-046, F-242).
- **No velocity-ceiling model** and **no heritability estimate for throwing velocity** (F-079).
- **No IMTP-versus-velocity study** in college or professional pitchers (F-021).
- **No spin-efficiency intervention trial with a delayed retention test** — anywhere (F-235).
- **No bullpen-to-game command transfer study in baseball** — described as the largest hole in the applied command literature (F-197).
- **No dose-response curve for throwing-accuracy practice volume** (F-198).
- **No elite braking-impulse norms in %BW-s** — the mechanically meaningful GRF quantity. Searched across three sweeps; this gap is starting to look permanent (F-207).
- **No dugout-deployable posterior-cuff activation test** (F-131).
- **No published accuracy validation of computer-vision seam/axis extraction against Hawk-Eye** (F-149).
- **No end-of-2025 league-wide kick-change evaluation** — Statcast does not classify it separately, so public tracking is currently impossible (F-160).
- **No within-pitcher variance published for seam orientation at release**, so SSW pitch-to-pitch stability is unknown (F-149).
- **No empirical test of within-outing release-speed SD against vertical miss** — the corpus's own cheapest high-value study, computable in an afternoon (F-173).
- **No verifiable quantitative HAA-to-whiff study** (F-152).
- **The dose-response of high-intent throwing on net collagen balance in the UCL specifically** — the 36-72 h window comes from patellar tendon and Achilles work in non-throwers (F-133).

### Topics the corpus has not researched at all
- **Pitchability, sequencing and in-game usage.** The README names it as a research priority; nothing in the corpus covers pitch sequencing decisions, count leverage, times-through-the-order, or attacking specific hitters. Stuff models explicitly do not price sequencing (F-168).
- **Hitter perception and reaction.** Referenced obliquely (attack angle, deception, the 150 ms tunnel-point argument) but never studied directly.
- **Catchers, framing and the pitcher-catcher system**, despite framing contaminating command measurement (F-182).
- **Psychology beyond motor learning** — competitive anxiety, routines, focus under fatigue, the mental side of an outing.
- **Return-to-throw after injury**, deliberately out of scope, though the interval-throwing modeling paper is logged (F-137).
- **Youth and developmental pitching**, deliberately out of scope by the 85 mph floor.
- **Nutrition, hydration and supplementation** beyond a single protein/fueling entry (F-140).
- **Female or softball populations.**
- **Non-fastball workload accounting** — whether a slider-heavy outing loads differently from a fastball-heavy one at equal pitch count.
- **Environmental effects** beyond the Reynolds-number note (altitude, temperature, humidity, ball construction year to year).
- **The economics of development** — beyond one WAR/FV conversion, nothing on what a velocity or command gain is actually worth to an athlete's contract.
- **Sample-level data.** The corpus has no primary dataset of its own; every number is from published literature, industry grey literature, or Statcast queries.

### Structural gaps in the corpus's own method
- **Only two research days exist** (2026-08-12 and 2026-08-13). Everything here is two cycles deep.
- **Verification is incomplete and known to be incomplete** (F-242).
- **The daily briefs are not maintained** and contain superseded claims (F-241).
- **Nothing in the corpus has been tested against a real athlete.** Every protocol is inference from published data.

---

## 6. If you only read five things

1. **F-094** — between-pitcher and within-pitcher associations diverge wildly. Every cross-athlete comparison in this corpus is suspect by default.
2. **F-043 / F-044 / F-045** — the stride-length sequence, the worked example of a cross-sectional finding read as a lever, and what happened when two independent groups actually moved it.
3. **F-072** — +0.65 mph. The number to say to an 88 mph athlete on day one.
4. **F-171** — command is an angular problem, and 1 degree is a foot.
5. **F-240** — six corrections in one day, none a fabrication, all in the same direction. The epistemic finding that should govern how the next cycle reads anything.
