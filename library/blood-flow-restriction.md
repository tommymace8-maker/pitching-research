# Blood Flow Restriction Training and the 85+ Arm

**Opened 2026-10-08.** Findings **F-615 → F-627**. Disputes **#63, #64**.
⚠️ **OPENED IN THE NINTH CONSECUTIVE FULLY EGRESS-BLOCKED CYCLE (F-615). ZERO PRIMARY TEXTS WERE OPENED. Every literature claim in this file is SNIPPET-ONLY and is a LEAD, not a finding. Everything in §2, §4 and §5 is arithmetic and is source-independent.**

---

## 1. What the whole topic actually is

BFR is **low-load resistance exercise performed with a pneumatic tourniquet on the proximal limb**, typically at 20–30% of 1RM and 40–80% of limb occlusion pressure. The standard rationale: local hypoxia and metabolite accumulation force recruitment of high-threshold motor units at a load far below what normally recruits them, so you get a hypertrophy signal without the joint and tissue load of heavy lifting.

**For a pitcher that rationale is attractive for one reason only: load sparing.** It is not a velocity argument and has never been one. §5 is where that matters.

**The entire baseball evidence base is three items:**

| Study | Design | n | Outcome | Result |
|---|---|---|---|---|
| Lambert 2023, JSES (PMID 36933646) | **RCT**, 8 wk, offseason, D-IA pitchers | **28** (15 vs 13) | shoulder lean mass, isometric strength, endurance, kinematics | BFR > control on lean mass and IR90 strength |
| Brumitt 2020, IJSPP 15(8) | **RCT**, 8 wk | **46** healthy adults | cuff strength, supraspinatus tendon thickness | **NULL between groups** |
| WVU ETD 7522 (2020) | uncontrolled retrospective season | **4** D1 starters | **fastball velocity (TrackMan)** | uninterpretable; protocol deviations |

**That is 78 participants, of whom 32 were pitchers, and exactly one study measured ball velocity (n = 4, uncontrolled).**

---

## 2. The power arithmetic, which settles more than the studies do

All figures α = .05 two-tailed, two equal-ish arms, derived in-cycle.

**Minimum detectable between-group effect:**

| Study | n per arm | d at 80% power | d at 50% power |
|---|---|---|---|
| Lambert 2023 | 15 / 13 | **1.062** | 0.743 |
| Brumitt 2020 | 23 / 23 | **0.826** | 0.578 |

**Lambert's published effect sizes are ES = 1.0 to 1.4.** Its floor is d ≈ 1.06. **A study reporting effects at its own detection floor is reporting the only effects it could have declared — i.e. the largest ones. Assume the true effect is smaller than published (F-616).**

**Brumitt's null is an underpowered null** by this corpus's own standing rule (F-439): it could not have seen anything below d = 0.83. ⚠️ **And it has been retitled in a published synopsis as "Rotator cuff strength is NOT augmented by blood flow restriction training" — a 46-person detection floor presented as an absence, in a title.**

**So the two studies do not disagree (F-618).** A single true effect of d ≈ 0.5 predicts both: Brumitt reports NS (power ≈ 36%), Lambert can only declare significance on the inflated tail.

**What would settle it:**

| true d | per arm | total |
|---|---|---|
| 0.30 | 175 | **350** |
| 0.40 | 99 | **198** |
| 0.50 | 63 | **126** |
| 0.60 | 44 | 88 |

The existing literature has **74 randomised participants**.

### 2b. Lambert's effect size, recomputed (F-617)

Reported: BFR **+227 ± 60 g** vs control **+75 ± 37 g** shoulder lean mass, P = .018, "ES = 1.0."

- The ± are **standard errors**, proved by self-consistency: read as SDs the same numbers give t = 8.18, p = 1.2 × 10⁻⁸, irreconcilable with the paper's own P = .018. Read as SEs: t = 2.16, df = 26, p = 0.040. Implied SDs 232 g and 133 g.
- **"ES = 1.0" is 227/232 = 0.98 — a WITHIN-GROUP effect size.** In an RCT that is not the treatment effect; the control group changed too.
- **The between-group treatment effect is 152 g, pooled d = 0.79.**

**Scale check: 152 grams of regional lean tissue in one shoulder over 8 weeks — about a third of a pound.** This corpus holds **no within-athlete mass→velocity slope of any kind** (F-504), so there is no licensed conversion to mph, and the order of magnitude says not to look for one. ⚠️ **Open: regional DXA lean-soft-tissue least-significant-change may be of the same order as 152 g. Whether this effect clears its own instrument is unresolved and needs the paper.**

---

## 3. The anatomy objection, which is the strongest thing in the topic (F-620)

**A BFR cuff goes on the proximal upper arm. The rotator cuff originates on the scapula. All four muscles are entirely upstream of the tourniquet and are never occluded.**

So the standard mechanism — local hypoxia drives high-threshold recruitment *in the restricted muscle* — **cannot be the mechanism for cuff adaptation.** The literature names the problem rather than solving it: Hedt et al. (2022) call it **"the paradox of proximal performance"** and rate their own evidence **Level V, expert opinion**, concluding further research is needed to characterise proximal responses. The candidate mechanisms offered — metabolic stress sensing, metabolite spillover, mechanotransduction via cell swelling, systemic hormonal response — are all hypotheses, none demonstrated for a non-occluded muscle.

**⭐ THE FREE TEST NOBODY HAS RUN: measure the NON-THROWING shoulder.** A systemic mechanism must act on the untrained shoulder too; a local one cannot. Lambert used DXA, which images both shoulders by default — **the discriminating data may already exist inside that trial's own scans.** This is the cheapest decisive measurement in the topic and it requires no new subjects.

---

## 4. What BFR actually buys, in the populations that have been studied (F-621)

| Outcome | LL-BFR vs high-load | Source |
|---|---|---|
| **Strength, untrained males** | **INFERIOR, SMD −0.33 [−0.49, −0.18], p < .0001** | *Life* 14:1442 (2024) |
| **Strength, >60 y** | INFERIOR, SMD −0.23 [−0.41, −0.05]; earlier review −0.42 [−0.70, −0.14] | PMID 36556004 |
| **Hypertrophy** | **EQUIVALENT, SMD 0.046, p = 0.14** (4.12% vs 5.8% raw) | *PeerJ* 12:e17195 |
| **Trained athletes** | **NO POOLED ESTIMATE EXISTS** | — |

**Baseball players in any meta-analysis: zero. Velocity outcomes: zero.**

**⭐ THE SENTENCE FOR THE WEIGHT ROOM: BFR buys roughly the hypertrophy of heavy lifting at a fraction of the load, and it buys LESS STRENGTH.** For a pitcher that trade is the wrong way round — the channel the velocity literature keeps implicating is force and RFD, not cross-sectional area. **So BFR belongs where heavy loading is unavailable: in-season congestion, a tweaked elbow, post-op, a travel week. Not as an addition to an offseason that can already lift heavy.**

⚠️ **Note the direction of the sample mismatch: untrained people gain from almost anything, so these are UPPER BOUNDS for an 85+ arm.** And Check #2 passes unusually well here — these are genuine randomised interventions, rare in a registry running ~30:1 cross-sectional. The failure is Check #3: the numbers measure 1RM and fibre CSA, and the sentence people want is about mph.

---

## 5. The detection wall, and why it is the most useful output of the cycle

### 5a. The dispersion nobody had extracted (F-622)

F-072 has been quoted for two months for its **+0.65 mph** mean in 88+ arms. Its **dispersion** was never taken out, and the published tails determine it:

- n = 58, entry ≥ 88 mph, mean +0.65 mph, **41.95% gained ≥ 1 mph, 18.39% lost > 1 mph**
- P(X < −1) = 0.1839 → z = −0.90 → **SD = (−1 − 0.65)/(−0.90) = 1.83 mph**
- **Independent back-check on the opposite tail:** z = (1 − 0.65)/1.83 = 0.191 → **42.4% predicted vs 41.95% observed.**

**A two-point fit that closes to half a percentage point.** The change distribution is near-normal and **SD ≈ 1.8 mph**.

> **Say this to an 88 mph arm alongside the +0.65: the spread is about ±1.8 mph, nearly three times the average gain.** One athlete's +3 mph proves nothing about a program; one athlete's −2 mph proves nothing against it.

### 5b. What that SD costs any velocity trial (F-623)

| Effect to detect | per arm | **total pitchers** |
|---|---|---|
| 0.50 mph | 211 | **422** |
| 0.65 mph (F-072's whole mean) | 125 | **250** |
| 1.00 mph | 53 | **106** |
| 1.50 mph | 24 | 48 |

**A D1 staff is 12–18 arms. An SEC season fields on the order of 200 pitchers across fourteen programs.** Detecting half a mile per hour needs **more pitchers than the conference has.**

**⭐ THE DECISION RULE, AND IT GENERALISES PAST BFR: a college program cannot validate ANY velocity intervention on its own athletes. "Did it work for us?" is not an answerable question and should not be asked.** What a program can ask is whether an intervention is **cheap, safe and mechanistically sound**, and accept the velocity effect as unmeasurable.

**This is the same wall F-506 hit for nutrition and F-476 hit for imagery — now reached from a third direction.** It is starting to look like a property of the sport rather than a feature of three topics.

⚠️ **Corollary warning: any facility claiming to have MEASURED a sub-mph velocity benefit on a roster-sized sample is reporting noise. The arithmetic forbids the claim regardless of the intervention.**

---

## 6. The provenance problem (F-626)

**Every positive proximal-BFR result traces to one group.** Houston Methodist / Lambert–Hedt–McCulloch: the D1 RCT, an AJSM "case for proximal benefit" (2021), the Level V paradox review (2022), an ORS 2023 presentation, and the institution's promotional blog — **five outputs, one underlying RCT.** The one independent randomised trial (Brumitt, George Fox) is **null**. Three of the forthcoming overhead-throwing BFR registrations located today share a single institution, date and ethics family (F-625).

**The exact parallel is already in this registry: F-194 downgraded Differential Learning for a single-lab plus publication-bias problem. Same test, same verdict — and here the independent replication exists and is null.** Grade proximal BFR **EMERGING**, not settled.

---

## 7. 🚨 The re-import vector this cycle caught (F-619)

**The sponsor's own blog reports an outcome its own peer-reviewed paper does not publish.**

| | Press release (Houston Methodist, Nov 2023) | Paper (PMID 36933646) |
|---|---|---|
| Duration | **six weeks** | **eight weeks** |
| Velocity | **"improvements in… fastball velocity and spin rate"** | **not reported; "velocity" is a keyword only** |
| Magnitude | **none given** | **none exists** |
| Mechanics | not mentioned | **only the CONTROL group changed** |

**DO NOT IMPORT "BFR RAISED FASTBALL VELOCITY."** No magnitude, no sample statistic, no peer-reviewed home.

**This is a NEW vector class for the corpus.** Not a content farm (F-274), not a university release restating an uncontrolled thesis (F-275), but **a sponsor's release adding an outcome its own paper did not publish** — the hardest kind to catch, because the institution has genuine standing and a real RCT behind it. **The tell was the 6-vs-8-week duration mismatch, which cost one extra search.**

**And note the paper's own move: it converts the BFR group's FAILURE to change mechanics into "possibly maintaining pitching mechanics."** A null sold as an outcome.

---

## 8. What to actually do with an 85+ arm

**The honest position: BFR is not a velocity tool, and nothing in this topic should change what a healthy 85+ pitcher does in an offseason that can already lift heavy.**

Where it has a defensible use:

1. **In-season load sparing.** The channel BFR genuinely matches heavy lifting on is hypertrophy (§4), at a fraction of the joint load. Mid-season, when heavy lower-body work competes with outings, that trade is real. ⚠️ Graded PROMISING, population-mismatched.
2. **A congested or compromised week** — tweaked elbow, travel, post-op. This is BFR's rehab home and the evidence is strongest there.
3. **NOT inside 48 h of an outing.** A 2023 *Sports Med* review warns inappropriate BFR "could significantly impair neuromuscular performance by generating considerable fatigue." Fatiguing stimulus, unmeasured acute cost, no demonstrated acute benefit.

**THE MEASURABLE CHECK — and read it honestly.** You cannot check velocity (§5b: 106 pitchers for 1 mph). What you CAN check is the thing BFR actually claims:

> **Isometric cuff strength (IR/ER at 0° and 90°) by handheld dynamometer, both shoulders, every 4 weeks.** Expect ~5 kg of between-day noise per athlete; you need **3 pre and 3 post measurements per athlete** to see a 2 kg change. **Track the NON-THROWING shoulder too — that is §3's free mechanism test, and nobody has published it.**

**On video, the failure looks like:** nothing. There is no mechanical signature of BFR, which is part of why it is hard to evaluate and easy to sell.

---

## 9. Open items and the cheapest unrun work

1. **🚨 THE CHEAPEST DECISIVE MEASUREMENT IN THE TOPIC — the contralateral shoulder (§3).** Systemic vs local mechanism, settled by a measurement Lambert's own DXA scans may already contain. **No new subjects.**
2. **Lambert 2023's full text is UNREAD and holds four things:** whether ball velocity was measured at all (the keyword suggests it was), the DXA regional precision / least-significant-change, the trial's mean fastball velocity (Check #1 is currently unanswerable), and whether the P = .018 is covariate-adjusted.
3. **No adequately powered proximal-BFR RCT exists** — n ≈ 198 for d = 0.4 (§2).
4. **No BFR study in any population has a velocity outcome** except an uncontrolled n = 4 thesis (F-624).
5. **The training-stress confound is unaddressed** — lower stress markers may mean less stress, not better recovery (F-627, Dispute #64).
6. **No BFR trial has reported pitch location, command or accuracy.** Dispute #27's **tenth venue**, holding without exception.
7. **The Riphah fast-bowler trial (NCT07440810) is complete, retrospectively registered, and measures strength/girth/power — not ball speed** (F-625). Its publication is the next external evidence in overhead throwing.

---

## 10. SEE ALSO

`strength-training-velocity.md` (the heavy-load channel BFR substitutes for) · `velocity-development.md` (F-072, F-622) · `null-audit.md` (F-439, the detection-floor rule applied here to a positive) · `nutrition-body-mass.md` (F-504, F-506 — the same detection wall) · `cold-water-immersion.md` (F-611, the same post-outing gap) · `open-disputes.md` #63, #64
