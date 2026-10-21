# Weightlifting derivatives, "triple extension" and complex/contrast training as velocity levers

**Opened 2026-10-21.** Findings **F-787 → F-800**. Disputes **#90, #91**.
Companion to `lower-body-power-transfer.md` (2026-10-20), which covered sprinting, sled and jump
training; this file covers the barbell half — Olympic lifts and their derivatives — plus the
complex/contrast sequencing literature and the coaching cue the whole package is sold on.

⚠️ **PROVENANCE WARNING FOR THIS ENTIRE FILE. Nineteenth consecutive fully egress-blocked cycle
(F-787). Not one primary text was opened. Every magnitude below is SNIPPET-GRADE.** The control
probe (`example.com` → `getaddrinfo ENOTFOUND`), 10/10 DNS failures and a 403 CONNECT against a
self-reporting-healthy proxy are on the record in F-787. Read every number here as a lead.
The source-independent material — F-790's interval arithmetic, F-791's chain audit, F-799's
detection table — does not depend on that and is as good as it will get.

---

## 1. Why this topic was opened

INDEX flagged it twice as **"the widest remaining hole"** (2026-10-18, re-flagged 2026-10-20).
Pre-cycle greps across 786 findings: `triple extension` **0**, `complex training` **0**,
`contrast training` **1**, `trap bar` **0**, `clean pull` **0**, `Olympic` **6** (all of them
gap-statements, never an object). The 2026-10-20 cycle established the baseball half of the gap
(F-776) and explicitly left this half open.

## 2. The terminal gap, and it is documented rather than inferred

**F-788.** Zero weightlifting, Olympic-lift, derivative, complex or contrast training trials with a
throwing outcome, in any population.

The contrast/complex half is the stronger claim because **the field's own systematic review says so
in print**: Petruzela, Papla & Stastny (2023), *J Hum Kinet* 87:189–200 — already in this registry
at F-765 — states it could not find studies with training focusing on intensity contrast (PAPE),
complex and ballistic methods, and recommends they be tested. That matters methodologically:
**Correction #13 falsified F-038's gap claim by re-searching.** A gap claim sourced to somebody
else's published search is harder to overturn that way.

The one partial exception is an older Spanish-language handball report of static-dynamic contrast
training beating maximal-strength-plus-peak-power at **p = 0.033**, with design, n and baseline
velocity all unretrievable. **UNVERIFIED. Do not cite.**

## 3. What the pooled evidence actually says — and what it is an outcome for

**F-789.** Morris SJ, Oliver JL, Pedley JS, Haff GG, Lloyd RS (2022), *Sports Medicine*
52(7):1533–1554, DOI 10.1007/s40279-021-01627-2, PMID 35025093, PMC9213388. 16 studies, 427
participants, Hedges' *g*, random effects.

| Comparison | Outcome | *g* | 95% CI | k | p |
|---|---|---|---|---|---|
| WL vs traditional RT | load lifted | 1.35 | 0.20 – 2.51 | 4 | 0.02 |
| WL vs traditional RT | CMJ height | 0.95 | 0.04 – 1.87 | 9 | < 0.01 |
| WL vs traditional RT | linear sprint | 1.04 | −0.03 – 2.39 | 4 | 0.13 **NS** |
| WL vs traditional RT | change of direction | 1.21 | −1.41 – 3.83 | 2 | 0.36 **NS** |
| WL vs plyometrics | CMJ height | 0.31 | — | 6 | 0.09 **NS** |
| WL vs plyometrics | strength | 0.69 | — | 4 | 0.20 **NS** |

**Zero throwing outcomes anywhere in it.**

**F-790 — the interval arithmetic, and it is the part to keep.** Widths: **5.24** *g* units (k = 2),
**2.42** and **2.31** (k = 4), **1.83** (k = 9). Width falls monotonically as k rises and the two
largest point estimates sit on the two widest intervals — the small-study-bias signature, not a
dose-response. **The only significant transfer outcome has a lower bound of *g* = 0.04**, i.e. the
data are compatible with no difference from ordinary lifting.

**Portable rule: at k ≤ 4 a pooled interval in a training meta-analysis is typically wider than the
effect it reports. Ask for the interval and the k before you believe a point estimate.**

## 4. ⭐⭐ The structural result — the chain's second step was never measured

**F-791.** The NSCA's own position statement (Comfort P et al. 2023, *JSCR* 37(6):1163–1190) grounds
weightlifting's transfer claim in **biomechanical similarity to jumping and sprinting** — hip, knee
and ankle extension shared with the pulls and the jerk drive.

For a pitcher that is a two-step chain:

1. **weightlifting → jump / sprint.** Best estimate *g* = 0.95 on CMJ height (F-789), lower bound 0.04.
2. **jump / sprint → ball velocity.** **This is the step that does not exist.**
   - CMJ **height** vs fastball velocity: **r = 0.07, n = 33 NCAA D1** (F-004).
   - CMJ **impulse** vs velocity: r = 0.71 (F-003) — but **J = m·√(2gh)** (F-005), so the correlating
     term is body mass, which is F-001 restated.
   - Sprint: **zero sled or resisted-sprint trials with a throwing outcome in baseball** (F-776);
     "sprint momentum predicts ball speed" is **p = m·v** with the mass partial unreported (F-783).

Granting step 1 in full and multiplying through an r = 0.07 step 2 leaves essentially nothing at the
ball. **This kills the transfer ARGUMENT, not the exercise.** The honest position is the one Dispute
#88 reached about sprinting: keep the work for athleticism and loading tolerance, drop the velocity
claim.

⭐ **FOURTH ARRIVAL in nine days of the candidate sixth structural sweep (flagged 2026-10-13):
which registered magnitudes are expressed only in a proximal test never linked to ball velocity in
an 85+ arm?** After tendon stiffness, the rotational med-ball throw and sprint momentum. **Promote
it to a standing sweep.**

## 5. ⭐⭐ The pre-post artefact, quantified by a review that prints both numbers

**F-792.** Fredriksen & van den Tillaar (2024), *Sports Medicine – Open*,
DOI 10.1186/s40798-024-00785-7, PMC11550301. 17 studies. Already registered at F-782 for its
taxonomy; **this result is new**:

> **All resistance-band and forearm-loading studies raised throwing velocity, by roughly 3.7% to
> 26% — and only HALF found a significantly higher increase than the control group.**

**100% pre-post positive → 50% controlled positive.** F-779's sweep had four registry instances
(F-416, F-754, F-769, F-037) all pointing the same way. This is the first to quantify the survival
rate, and it gives the sweep a prior it lacked: **the expected shrinkage on an uncontrolled training
magnitude is roughly a coin flip between "some of it" and "none of it."**

## 6. Complex and contrast training — the sequencing literature

**F-793.** Cormier P, Freitas TT, Rubio-Arias JÁ, Alcaraz PE (2020), *JSCR* 34(5):1461–1479,
DOI 10.1519/JSC.0000000000003493. 27 articles.

- **1RM: described explicitly as improvements FROM BASELINE — +23.4% (complex), +23.7% (contrast).**
- Vertical jump: complex SMD 0.85 [0.45, 1.25]; contrast 0.50 [0.19, 0.81].
- Sprint: complex −0.94 [−1.33, −0.54] in one retrieved version, **−0.69 [−1.02, −0.36] in another**.
- Change of direction: complex −0.83 [−1.08, −0.59], and the abstract states **there was no control
  group for contrast.**
- Stated conclusion: complex "potentially slightly greater."
- **Zero throwing outcomes.**

The "complex beats contrast" conclusion compares **two sets of within-arm pre-post effect sizes from
different studies.** It is Dispute #80's defect found in the wild. A +23% 1RM gain in team-sport
athletes is a training-age effect that a third arm doing neither would also have got.

**F-794 — the best-designed trial, with a magnitude that cannot be real.** Xu et al. (2026), *JSCR*
40(8), DOI 10.1519/JSC.0000000000005451, PMID 42223132. n = 45 national-level male track and field,
24 weeks, three arms, 3-D force plate. **Jump height with arm swing: complex +30.9%, contrast
+17.1%, control +5.2%.** Push-off time without arm swing: contrast −6.1%. Eccentric strength
reported as 43.1% of jump-height variance. **Zero throwing outcomes.**

A national-level male athlete's arm-swing CMJ is of the order of 50–60 cm. **+30.9% is +15 to +19 cm
in 24 weeks in an already-selected athlete.** ⭐ **And the control arm moved +5.2%. In an elite
population a control group should not move; when it does, suspect the test first** — and "jump
height with arm swing" is the most learnable, least reliable jump variant in common use. The
between-arm contrast inherits that uncertainty rather than escaping it. **Do not quote +30.9%.**

## 7. The derivative question is a loading question

**F-795.** Suchomel TJ, McKeever SM, Comfort P (2020), *JSCR* — n = 27 resistance-trained men,
10 weeks, CATCH / PULL / OL. The force- and velocity-overload group produced the greatest
improvements in each examined characteristic. **But a Comfort et al. load-matched 8-week comparison
found no differences in strength, squat jump or CMJ between catching and pulling derivatives at the
same relative loads.** A 2022 follow-up (*JSSM* 21:504–516) has pulling positive and catching
trivial.

**The pulling-over-catching inference is confounded with load.** At ≈ 9 per arm the 2020 trial can
only detect very large effects — and here that power objection applies against a **positive**, which
should worry a coach more than it does against a null. **Programming answer: pick the derivative your
athletes can perform well at the load you want.**

**Fourth time this registry has decomposed a modality claim into a dose claim** (after F-764's
inertia dial and F-711's relative load).

## 8. 🚨 The trial of Olympic lifting in throwers that never measured a throw

**F-796.** Pálinkás et al. (2025), *J Funct Morphol Kinesiol* 10(2):187, DOI 10.3390/jfmk10020187,
PMC12194710. **n = 27 after attrition (control 8, heavy squat 7, Olympic weightlifting 12), young
female handball players, described by the authors as less skilled.**

- Both intervention groups improved 5RM back squat and CMJ height; the control group did not.
- Theoretical maximal force ≈ unchanged (+2% each); FV imbalance −14% in the weightlifting arm only.
- **The force–velocity profile did not change significantly in either group.**
- **NO THROWING OUTCOME OF ANY KIND.**

**Dispute #27's fourteenth venue, and its sharpest form yet: it is no longer only accuracy that goes
unmeasured, but the sport's own primary skill.** Somebody randomised handball players to Olympic
lifting, tested them, published it, and never asked them to throw a ball. This is F-782's
exercise-selection thesis in one object.

⭐ **And the authors handed the topic its manipulation check, as a limitation:** the Olympic
weightlifting exercises were intended to be performed with maximal velocity, but **the realization
of this during training was limited by the players' technical proficiency.**

## 9. "Triple extension" / 3X — the cue, and the citation that refutes it

**F-797. VERDICT: MARKETING.** `triple extension` returned **0 hits** in 786 findings before this
cycle. The claims, from `topvelocity.net` / `.org` (vendor pages, not opened):

1. Triple extension = drive-leg ankle, knee and hip extension, "as your body drives itself off the
   ground when jumping."
2. A prescribed order — knee, then ankle, then hip, just before front-foot strike.
3. Drive-leg force becomes hip-to-shoulder separation, credited with most of a pitcher's velocity.
4. "The hang clean's second pull produces over four times the power output of a squat."

**Nobody has ever manipulated drive-leg extension magnitude, order or timing against any outcome, in
any population.** And the support cited for (3) is **this registry's own F-003** (Sakurai, Qiao,
Szymanski & Crotin 2024, *JSCR* 38(7):1288–1294, PMID 38900174), whose claim line reads that
**pelvis and trunk pitching kinematics do NOT correlate with any CMJ variable** — the mechanism the
cue exists to serve. The correlation that does hold, impulse r = 0.71, is mass (F-005; height alone
r = 0.07, F-004).

⭐ **Third instance of the absolute-mass-weighted-output confound sold as a lever**, after the
rotational med-ball throw (F-751, Dispute #84) and sprint momentum (F-783). **In all three the
decisive test is the same partial correlation controlling for body mass.**

## 10. ⭐⭐ The reading rule, fourth arrival — and its first in-the-wild failure

**F-798.** F-762's portable rule: **when a training tool is named for a mechanism, treat the
mechanism as unverified until a manipulation check is shown.**

| Arrival | Named mechanism | Status of the check |
|---|---|---|
| F-571 / F-721 | modality mechanism assumed | never checked |
| F-762 / F-763 | flywheel "eccentric overload" | **does not necessarily occur**; field inferred force from power and velocity |
| F-764 | the inertia dial | the setting that delivers the mechanism removes the velocity |
| **F-798, today** | **"force and velocity overload" in weightlifting derivatives** | **absent in F-795's trial; FAILED in F-796, reported by the authors as a limitation** |

**Technical proficiency gates the stimulus.** A pitcher who cannot clean well does not get a weaker
version of the velocity overload — by Pálinkás's account he may not get it at all, while still paying
the coaching minutes and the recovery cost. **That is a stronger argument against Olympic lifting on
a mid-season college staff than anything in the transfer literature, because it does not require
transfer to be false.**

## 11. ⭐⭐ What to actually do — the bar-velocity manipulation check

**F-799.**

**The trial you cannot run.** From F-623 (SD of offseason velocity change = 1.83 mph, F-622;
α = .05 two-tailed, 80% power, two arms):

| Effect to detect | Per arm | Total pitchers |
|---|---|---|
| 1.00 mph | 53 | **106** |
| 0.65 mph | 125 | **250** |
| 0.50 mph | 211 | **422** |

Fourteen pitchers cannot see a 1 mph modality effect. **Fifth arrival of the detection wall**
(F-506, F-476, F-623, F-681).

**The check you can run.** Per pitcher, per programmed derivative: **mean concentric barbell velocity
on every working set, 3 sets, 3 sessions, one week.** One linear position transducer or a bar-velocity
app. **Zero additional athlete time** — logged during work already being done.

**Decision rule.** The exercise is prescribed as a velocity overload. If an athlete's mean concentric
velocity on the prescribed load sits below the band the exercise is supposed to occupy, **the named
stimulus is not being delivered to that athlete.** ⚠️ Set the band from your own device's norms;
this corpus holds no derivative velocity norms and could fetch none (F-787).

**Second free output:** between-session velocity variability per athlete — the weight-room analogue
of the ICC = 0.36 reliability objection that blocked Dispute #89 (F-781).

**What you tell the pitcher:** *"We're not changing the lift. We're putting a sensor on the bar for a
week, because this exercise is prescribed for speed and I want to know whether you're actually
hitting speed. If you're not, we'll change the load, the exercise, or both — and that's a coaching
problem, not a you problem."*

**On video the failure looks like:** a pull that looks heavy and finishes slow — a grind through the
second pull rather than a snap. The number tells you before your eye does.

**How you know it worked:** the check has a result either way. In band → the stimulus is real and the
only open question is transfer, which your roster cannot answer, so F-791's position stands. Below
band → you found a program defect in a week, for free, and nothing about transfer had to be true.

⚠️ **DO NOT pair this with a velocity test and read the mph.** You need 53 pitchers per arm to see a
mile per hour. Any mph change on 14 arms is F-082's rising baseline plus noise.

## 12. Field sweep

**F-800.** Seven searches; **no new 2026 claim from any side.**

| Item | Standing | Verdict |
|---|---|---|
| Cressey: doesn't use Olympic lifts with pitchers; plane specificity | high | the position is defensible; **the stated reason is not** (see next) |
| 5toolsportsscience.org (2019): the coaches making the plane-specificity objection trap-bar deadlift, **the same plane as a power clean** | medium (blog) | ⭐ **PROMISING as an argument, UNPROVEN as physiology** — it does not make the clean work, it makes the stated reason for rejecting it wrong |
| MLB strength coach implementing Olympic lifts, claiming speed and fewer shoulder injuries | low, anecdotal | **UNPROVEN** |
| TopVelocity 3X / triple extension | commercial | **MARKETING** (F-797) |
| Shared across pro, anti and middle: the lifts need skilled instruction, hard to find in baseball | high (consensus) | **PROMISING**, and it converges with F-798 from the other direction |
| Driveline / Tread / Kinetic Pro on lower-body lifting | — | **nothing surfaced this cycle** |

**In seven searches not one source on any side cited a trial, because per F-788 there is none to
cite.** A ten-year-old argument with no data is this topic's normal state, not a search failure.

The one genuinely 2026 baseball object returned — Burke et al., *JSCR* ahead of print, PMID 42423608,
longitudinal CMJ and workload against fastball velocity and consistency — **is already registered and
still unread.** It remains the most load-bearing unread object for the jump channel.

## 13. What would move this topic

1. **Any trial.** Three arms (weightlifting derivatives / matched-volume traditional lifting /
   nothing), one college staff, 8–12 weeks, mound velocity measured. Nothing structural prevents it;
   F-799 says no single program can power it.
2. **The partial correlation controlling for body mass** — the same regression that settles
   Disputes #84 and #85's accounting half and F-783. **One regression, three topics.**
3. **Morris 2022's full forest plots**, to confirm whether the k ≤ 4 estimates carry the small-study
   signature F-790 infers from interval widths alone.
4. **A derivative velocity-norm band from any peer-reviewed source**, which would convert F-799's
   decision rule from device-dependent to citable.
5. **Burke et al. 2026 (PMID 42423608)** read in full — the only longitudinal within-athlete
   jump-to-velocity object in existence.
