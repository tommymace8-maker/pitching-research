# INDEX — Navigation Map for the Pitching Research Corpus

**Compiled 2026-08-17. Updated 2026-09-11.** Companion to [`FINDINGS.md`](FINDINGS.md), the flat registry of **314** findings (**F-304→F-314 added 2026-09-11** — catcher framing and the contamination of a command number; all derivation plus one rules fact, one queue-head lead and one new laundering channel — see §7; F-294→F-303 added 2026-09-09, sequencing arithmetic plus a PARTIAL RETRACTION of this program's own fabrication verdict — see §7; F-285→F-293 added 2026-09-08, arithmetic plus one citation correction; F-277→F-284 added 2026-09-07, all source-independent arithmetic; F-268→F-276 added 2026-09-06; F-260→F-266 added 2026-09-05; F-251→F-259 added 2026-09-04; **F-255, F-256 and F-258 are UNVERIFIED leads in quarantine — see §7**).

> ### 🚨 EGRESS HAS NOW FAILED **SEVEN TIMES IN A ROW** (2026-09-04, -05, -06, -07, -08, -09, -11) — AND A CYCLE WAS MISSED ENTIRELY (2026-09-10)
> **Zero primary sources opened across seven consecutive cycles, and eight calendar days.** `WebSearch` works; `WebFetch` and raw `curl` do not. **NEW 2026-09-11: `WebFetch` was tested INDEPENDENTLY of curl and returns its own explicit `{"error_type":"EGRESS_BLOCKED"}` naming the domain** — previous cycles inferred this from curl's behaviour; it is now directly confirmed, and both channels fail for the same reason. The proxy names the cause itself: `connect_rejected (organization policy)`, for **every** host including **`en.wikipedia.org` used as a control**. **This is an empty network allowlist in the remote execution environment. It is not an outage, not a paywall, and not a proxy fault — IT REQUIRES A HUMAN TO CHANGE** (F-277, F-285, F-304).
> **⚠️ THERE IS NO `daily/2026-09-10-report.md`.** The sequence runs 09-04 → 09-09, then jumps to 09-11. Recorded because **a missing brief is otherwise indistinguishable from a brief that found nothing** (F-304).
> **The standing brief's WORKING-domain list has been wrong SEVEN times and should be DELETED from the prompt, not amended.**
> **PROBE EGRESS BEFORE CHOOSING A TOPIC.** Added after cycle 4; followed on 2026-09-08, -09 and -11; costs ninety seconds and determines the whole shape of the cycle. **KEEP IT.** If egress is down, pick a gap that arithmetic can close (F-266, F-278, F-286, F-295, F-307).
> **⚠️ THE UNREAD VERIFICATION QUEUE NOW STANDS AT 26 ITEMS. Seven consecutive arithmetic-only cycles have produced ~60 findings, essentially all internally consistent and NONE checked against data.** That is the condition F-259 warns about, and **the next cycle with working egress should spend itself entirely on the queue rather than opening a new topic.** Queue head, **REORDERED 2026-09-11: arXiv `2609.03786` (KBO umpire count-bias, F-312)** — it would touch THREE areas in one page (a confound ~4× larger than the catcher term on every called-strike command metric; a third answer to Dispute #20b; the strongest live objection to F-283) — then arXiv `2601.11904` (pitch-pattern motifs, F-299/F-303), then *Scientific Reports* s41598-025-28142-y (peer-reviewed KBO/ABS), then Brill/Deshpande/Wyner (F-290, F-292), then the Kovash & Levitt minimax pair (F-302).
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
| **`library/open-disputes.md`** | 461 lines / 58 KB | **2026-09-07** | **Twenty** unresolved arguments among the anatomist, the biomechanist and the coach, each with both sides, the strongest evidence, and what would settle it. Plus the standing methodological disputes | "Is this settled?" "What would I have to run to find out?" "Where do the three specialists actually disagree?" |
| **`library/hitter-perception.md`** | **NEW 2026-09-04** | 2026-09-04 | **The hitter's decision clock.** Flight time with drag; where the ball is at the commit instant; the linear-vs-quadratic argument that reconciles F-163 with F-159/F-232; the detection asymmetry; a quarantined 7-item verification queue | "How long does he actually have?" "Why does tunneling correlate at 0.07 while velocity gap works?" "What do I tell a pitcher about his changeup, and how would I know it worked?" **⚠️ §1–4 are arithmetic and durable; §5 is unread and quarantined** |
| **`library/environment-air-density.md`** | **NEW 2026-09-05** | 2026-09-05 | **Altitude, temperature and humidity as constraints on pitch shape.** Density by venue (Swayze → Air Force Academy); movement scales with density to within 0.1 pp, invariant to Cd and C_L; the altitude asymmetry; the humidity folklore debunked in sign *and* size; the per-pitch-vs-per-sensor detection split | "How much movement does he lose in Denver?" "Does humid air really make it bite?" "Is his February-to-May IVB drop real?" "What do I tell him before an altitude series?" **All computed in-cycle — no source was opened; ratios are claimed, absolute inches are not** |
| **`library/pitch-mix-sequencing.md`** | **NEW 2026-09-06** | 2026-09-06 | **The arithmetic of pitch usage.** The optimality condition (marginal, not average, run value); why the more-used pitch should look *better*; the run-value noise floor that ends individual-level mix inference; the quadratically flat objective; "commit or cut" for the fourth pitch; the missing anticipation slope $D$ and how to estimate it | "How often should he throw it?" "His slider grades better — throw more sliders?" "How would I know a mix change worked?" "Keep the 6% changeup or kill it?" **All derived in-cycle — no source was opened; one empirical input is approximate and bracketed** |
| **`library/count-leverage.md`** | **NEW 2026-09-07** | 2026-09-07 | **Where a pitch is actually worth something, by ball-strike count.** The identity that makes relative leverage computable with no data (walk and strikeout run values cancel); the λ table and the three specifications it was attacked with; why total leverage is dominated by 0-0 and not by 3-2; 0-2 as the lowest-leverage count in baseball; why a count-specific effect can never be seen in game data; the ABS challenge as the same problem | "Which pitches actually matter?" "Is the 0-2 waste-pitch argument worth having?" "Does 'get ahead' hold up?" "How would I train and measure a full count?" "When should he burn an ABS challenge?" **All derived in-cycle — no source opened; ONE bracketed empirical input (the walk-minus-strikeout run gap)** |
| **`library/times-through-order.md`** | **NEW 2026-09-08** | 2026-09-08 | **Times through the order, and the within-outing decline.** Why one pitcher's own TTOP needs 790 seasons; the lineup-slot composition bias that makes 56% of a scorebook split an artefact; the pull decision as a talent-gap comparison with a ~20-wOBA-point break-even; the whole question priced at ~1 run a season; the input-vs-outcome detection asymmetry; a citation correction to F-258 | "Does my guy fall off the third time through?" "What is my scorebook actually showing me?" "Should I pull him?" "What can I see inside one outing?" **All computed in-cycle — no source opened; ONE bracketed snippet-level input (~10 wOBA pts per time through)** |
| **`library/pitch-sequencing.md`** | **NEW 2026-09-09** | 2026-09-09 | **The transition matrix — what to throw NEXT.** Why sequencing is a MATRIX where mix is a vector; the two-party detection asymmetry (your opponent can measure this and you cannot); the granularity trap (a count-conditioned report shows a 47-point tendency that does not exist); the count-composition confound and why its textbook fix is unaffordable; the equilibrium argument; the transition-matrix audit | "Does he tip his sequence?" "What do I do with the analyst's split sheet?" "Is 'slider plays better after the heater' real?" "How would I know a sequencing change worked?" **All computed in-cycle — no source opened; every RUN figure scales with the unmeasured $D$, every DETECTION threshold does not** |
| **`library/catcher-framing-command-measurement.md`** | **NEW 2026-09-11** | 2026-09-11 | **The zone edge, and what contaminates a command number.** The ball-CENTRE called zone (+33% area); the physical framing lever as plate-to-glove travel drop (2.0 in FB → 3.7 in CB); the shift×density result and why umpire precision CANCELS; what framing is worth and the backward check saying the whole MLB spread is HALF AN INCH; ⚠️ **the catcher term equals a one-season command gain**; the free fix; the ABS stress test F-283 survived | "How much of his command number is actually him?" "Is framing worth anything at my level?" "Should he ever challenge on 0-2?" "What do I measure command with instead?" **All derived in-cycle — no source opened; THREE unverified empirical inputs, each bracketed where used** |
| **`daily/2026-09-11-report.md`** | **NEW** | 2026-09-11 | Cycle 10 brief. **SEVENTH consecutive fully-blocked cycle**, and the first MISSED cycle (no 09-10). Opens catcher framing; sizes a contaminant of the corpus's own command metrics; resolves F-283's ABS conditional; catches a **new laundering channel aimed at the credibility check itself** | "Why is my strike percentage a two-person statistic?" "Is ABS at my level yet?" "How do you launder a source's own marketing into a credibility rating?" |
| **`daily/2026-09-09-report.md`** | | 2026-09-09 | Cycle 9 brief. **SIXTH consecutive fully-blocked cycle.** Opens sequencing; issues the corpus's **first correction in the SKEPTICAL direction** (F-303); finds the industry is not publicly arguing about this at all | "Who can actually measure sequencing?" "Why is my opponent's report better than mine?" "When is a defensive rule too defensive?" |
| **`daily/2026-09-08-report.md`** | **NEW** | 2026-09-08 | Cycle 8 brief. **FIFTH consecutive fully-blocked cycle.** Opens times-through-the-order; corrects F-258's citation *and* its practical meaning; kills a field fatigue-metric claim on arithmetic alone | "What is a third-time-through split worth?" "Why is my own scorebook the least trustworthy thing in the dugout?" |
| **`daily/2026-09-07-report.md`** | | 2026-09-07 | Cycle 7 brief. **FOURTH consecutive fully-blocked cycle.** Opens count leverage; catches a new content farm **and a search summariser emitting an unprompted fabricated magnitude** | "What is a pitch worth in this count?" "How is the fabrication problem getting worse?" |
| **`daily/2026-09-06-report.md`** | | 2026-09-06 | Cycle 6 brief. **THIRD consecutive fully-blocked cycle — escalated.** Opens the pitchability gap; catches a live content-farm cluster and a press-release laundering | "What can a blocked cycle produce?" "What is currently fabricating pitching research?" |
| **`daily/2026-09-05-report.md`** | | 2026-09-05 | Cycle 5 brief. **Second consecutive fully-blocked cycle** — chose a topic physics could close | "What can a blocked cycle actually produce?" |
| **`daily/2026-09-04-report.md`** | | 2026-09-04 | Cycle 4 brief. **Ran with all egress blocked** — the run-condition banner is the first thing in it | "What happened on the blocked day, and what is safe to use from it?" |
| **`library/idea-scouting.md`** | 413 lines / 45 KB | **2026-09-07** | **Four** field sweeps of what the industry is arguing about right now, each item labelled PROMISING / UNPROVEN / DEBUNKED / MARKETING. Content-farm blocklist and hazard classes | "Is this new thing real?" "What is the industry selling this month?" "What did we look for and NOT find?" |
| **`src/core/biomech/references.ts`** | 830 lines | — | ~30 structured citations with `EvidenceGrade`, `Population`, `Causality`, caveats and dated `corrected` records. Kinematic and kinetic norm bands, the four "free reductions," the velocity-torque conflict table, and the `MARKERS_NOT_LEVERS` list | "What grade and causality does this citation carry in code?" "Which variables must never be rendered as coachable?" |
| **`daily/2026-08-12-biomechanics.md`** | 74 lines | 2026-08-12 | Day 1 biomechanics brief | Quick orientation only |
| **`daily/2026-08-12-anatomy.md`** | 55 lines | 2026-08-12 | Day 1 anatomy brief | Quick orientation only |
| **`daily/2026-08-12-coach.md`** | 137 lines | 2026-08-12 | Day 1 field sweep, the foot-plant interrogation, cross-examination, three challenges each to the anatomist and biomechanist | The Day-1 disagreements, verbatim |
| **`daily/2026-08-13-velocity.md`** | 122 lines | 2026-08-13 | Day 2 velocity brief | **CONTAINS UNCORRECTED PRE-CORRECTION TEXT** — see Known Corrections |
| **`daily/2026-08-13-stuff-command.md`** | 90 lines | 2026-08-13 | Day 2 stuff/command brief | **CONTAINS THE REVERSED CHANGEUP FRAMING** — see Known Corrections |
| **`daily/2026-08-13-coach.md`** | 518 lines / 67 KB | 2026-08-13 | The single most important document in the corpus for epistemics: the full correction log, the outstanding-verification list, the core-coiling scouting, and the analysis of what six corrections in one day implies | "What did we get wrong and why?" "What is still unverified?" "How should verification work?" |
| **`research/README.md`** | 75 lines | — | Program scope, the three-agent team, how a research day works, ground rules | "What is this program and what is out of scope?" |

**Total corpus:** ~8,900 lines of research across **14** library files, **11** daily briefs, and one structured citation module. **314 registered findings.**

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

### Hitter perception and the deception budget — **added 2026-09-04**
| Sub-topic | Primary file | Findings |
|---|---|---|
| Flight time with drag; plate speed; the hitter's budget | `hitter-perception.md` §2.2 | F-251 |
| The commit instant — where the ball is when the decision is made | `hitter-perception.md` §2.3 | F-252 |
| Why tunneling fails and velocity gap works — linear vs quadratic | `hitter-perception.md` §3; `open-disputes.md` #17 | F-254 |
| The BP tunnel-point arithmetic inconsistency | `hitter-perception.md` §3.4 | F-253 |
| The detection asymmetry (cheap input check, unaffordable outcome check) | `hitter-perception.md` §4.2 | F-257 |
| The changeup arm-speed tell | `hitter-perception.md` §4.3 | F-256 |
| **Quarantined leads — occlusion, TTOP, sequencing** | `hitter-perception.md` §5 | F-255, F-258, F-259 |

### Environment — air density, altitude, temperature, humidity — **added 2026-09-05**
| Sub-topic | Primary file | Findings |
|---|---|---|
| Density by venue; movement ∝ density, invariant to Cd and C_L | `environment-air-density.md` §2.1, §3.1 | F-260 |
| The altitude asymmetry — 21% of movement for 4 ms | `environment-air-density.md` §3.2 | F-261 |
| Humidity folklore — wrong in sign, negligible in size | `environment-air-density.md` §2.4, §4.5 | F-262 |
| Temperature as the in-season variable (≈0.03 in/°F) | `environment-air-density.md` §2.3, §4.6 | F-263 |
| Invisible per pitch (0.26 SD), detectable in 6–8 | `environment-air-density.md` §3.3 | F-264 |
| Reynolds-equivalence — F-148's note confirmed | `environment-air-density.md` §5; `open-disputes.md` #18 | F-265, F-148 |

### Pitch mix, sequencing and usage — **added 2026-09-06**

| Question | Go to |
|---|---|
| How often should he throw a given pitch? | `library/pitch-mix-sequencing.md` §1 — **F-268**. The optimum equalises **marginal** run value ($v_i + p_i v_i'$), not average. Equal run values across an arsenal is NOT the optimality condition |
| "His slider grades out better — throw more sliders?" | **F-269.** No. At a true optimum the **more-used** pitch should show the **better** average run value. This is the stride-length error (F-043/F-044/F-045) transplanted into analytics |
| Is ESPN's Nash Score usable? | **F-271.** Framing right, test broken twice: wrong quantity equalised, and its 0.2 R/100 threshold is **4–9× smaller than the SE of its own inputs** |
| How would I know a mix change worked? | **F-270, F-273.** You would not, ever. Single-pitch run-value SD ≈ 0.21–0.25 runs; detecting the benefit of a 20 pp fix needs 60,000+ pitches. **Verify compliance (usage %, ±2.5 pts at 400 pitches), never outcome** |
| How much does a wrong mix actually cost? | **F-272.** Quadratically flat. 5 pp off ≈ 0.1–0.6 runs/season (ignore it). 30 pp off ≈ 3–23 runs (fix it). **The middle does not exist** |
| Keep the 6%-usage fourth pitch or kill it? | **F-276.** "Commit or cut" — sprinkling is the one usage level the model says is provably wrong. **February decision, not June.** Cheap check: ~100 of each, release-angle SD vs the fastball's |
| What is the missing number? | **F-276 / Dispute #19.** The anticipation slope $D$. Unmeasured anywhere. `library/pitch-mix-sequencing.md` §6 gives the panel-regression design; **Statcast already holds the data** |
| Is tunnelling a sequencing tool? | **F-166 — NO.** Retired as a training target. And **F-172**: no public stuff model prices sequencing at all |

### Count leverage — which pitches are worth something — **added 2026-09-07**

| Question | Go to |
|---|---|
| How much is a pitch worth in this count? | `library/count-leverage.md` §1 — **F-278.** Relative leverage follows from ONE parameter; the walk and strikeout run values **cancel exactly**, so no run-expectancy table is needed. λ(3-2) ≈ 4.7, λ(0-0) = 1.00, λ(0-2) ≈ 0.26 |
| Can I quote the table? | **F-278 — ONLY THE EXTREMES.** 3-2 highest and 0-2 lowest survive every specification; the 3-2/0-2 gap spans **4.9×–18.2×** and the middle of the table reshuffles freely. **Say the direction, never a middle cell.** Same discipline as F-269 |
| Which count carries the most total leverage? | **F-279 — 0-0, at ~24%**, not 3-2 at ~12%. Per-pitch leverage and aggregate leverage peak in **different counts**. The first pass of this model got it backwards and the error is recorded on purpose |
| Is the 0-2 waste-pitch argument worth having? | **F-280 — barely.** 0-2 is 9.7% of pitches and 2.1% of leverage; a +5-point gain there is worth ~0.2 runs a season. Both outcomes at 0-2 are cheap |
| Does "get ahead" hold up? | **F-281 — yes, but not for the usual reason.** Ahead counts are 33.8% of pitches and 15.2% of leverage. The value is banked **at the transition**, not spent in the count you occupy |
| How would I know a count-targeted change worked? | **F-282 — never in games.** ~43 full counts a season; a +10-point 3-2 gain needs **≈17 seasons** of game data. **Manufacture the count in the pen**: 25/bullpen × 3/week × 12 weeks = 900 pitches detects ~9 points |
| When should he burn an ABS challenge? | **F-283 — never on 0-2.** The count term dominates the EV because λ spans 5–18× while overturn probability does not. **All ABS empirics are snippet-only and unverified** |
| Does the manufactured count transfer? | **UNKNOWN — Dispute #20a, and the corpus's most load-bearing unanswered applied question.** F-197: no bullpen-to-game command transfer study exists in baseball |

### Times through the order, and the within-outing decline — **added 2026-09-08**

| Question | Go to |
|---|---|
| Does *my* guy fall off the third time through? | `library/times-through-order.md` §2 — **F-286. You will never know.** Per-PA wOBA SD = 0.531, so the league-average effect needs **44,200 PA per group ≈ 790 college seasons**; an effect **5× the league average** still needs **32 seasons**. Third in the series after F-273 (60,000 pitches) and F-282 (17 seasons), and the most extreme yet |
| What is my scorebook actually showing me? | **F-287 — 56% lineup slot.** The 1st and 2nd times through are complete passes through all nine slots; the 3rd is **truncated at the top of the order**. That is **+0.025 wOBA of pure artefact against a reported real effect of 0.010** — the bias is **2.5× the effect**. ⚠️ **Bias-in-expectation, not noise: more starts make it MORE confident, not less.** Free fix: compare **slots 1–4 vs slots 1–4** |
| Should I pull him the third time through? | **F-288 — wrong question.** It is a talent-gap comparison: leave him in whenever his penalty is smaller than the fresh arm's deficit. **Break-even ≈ a 20-wOBA-point gap**, and in a college pen arm #6 is usually further behind than that |
| What is the whole question worth? | **F-288 — ~1 run per college season**, and only against an *equal-talent* fresh arm. Same order as F-280 (0-2 counts, ~0.2 runs). **Real, confirmed, and too small to spend a coaching week on.** The leverage is in bullpen depth, not in the penalty |
| What can I actually see inside one outing? | **F-289 — a 1.0 mph velocity drop, in ~16 fastballs per bucket.** Against 790 seasons for an outcome change: **~10,000 starts between them.** Decide on inputs, never outcomes. ⚠️ But F-127 puts velocity **last** in the fatigue sequence — the cheapest instrument watches the latest signal |
| Is the reported penalty stepped or continuous? | **F-290 — reportedly CONTINUOUS, and F-258 recorded the opposite practical meaning.** Also corrects the citation: **Brill, DESHPANDE & Wyner, JQAS 2023**, not "Brill & Wyner 2022." **Still quarantined — snippet-only** |
| Familiarity or fatigue? | **UNKNOWN — Dispute #21.** The two have **opposite training answers** (arsenal in February vs capacity in the fall). The identifying design needs no new instrumentation. **Whether it has already been run is unknown — deliberately NOT recorded as a gap** |
| Is a "velocity drops are a flawed fatigue signal" claim credible? | **F-291 — UNPROVEN.** A 1.5 mph inning-to-inning drop is **3.4–6.6 SD** of measurement noise, so a reported 41% "false-alarm" rate cannot be instrument error. **Do not repeat the 41%** |

### Sequencing — the transition matrix, what to throw NEXT — **added 2026-09-09**

| Question | Go to |
|---|---|
| How is sequencing different from mix? | `library/pitch-sequencing.md` §1 — **F-297.** Mix is a **vector** ($k-1$ free parameters); sequencing is a **matrix** ($k(k-1)$; **144** if you condition on count for a 4-pitch arm). **The parameters multiply by $k$ and the season stays at 1,600 pitches** |
| Can I tell whether my guy tips his sequence? | **F-295 — YES, cheaply.** A 20-point tendency is established in **~47 observations of the conditioning event**; a season supplies 178 per previous-pitch cell ($k=3$) or 100 ($k=4$) |
| Can I tell whether fixing it helped? | **F-295 — NO, ever.** That needs **3,832–245,277 pitches per group.** Fourth in the series after F-273 (60,000), F-282 (17 seasons) and F-286 (790 seasons) |
| So who is better positioned — me or the opponent? | **F-295 — THE OPPONENT, by 81×–5,208×.** ⚠️ **The direction is the finding; the ratio is not** (Dispute #22). The prescription is the inversion: **build the report your opponent is building.** You have the same log and better access |
| The analyst circled one cell on a sixteen-cell sheet | **F-297 — ask how many cells were on the sheet.** On a pitcher with **NO tendencies at all**, the largest looks **+8.6 points** at 16 cells (56% chance of a "significant" one) and **+47.3 points** at 192 count-conditioned cells (**100%**). **Previous-pitch × handedness is the finest cut a college season supports** |
| Is a small sequence split real? | **F-298 — under ~10 points, assume count composition.** The previous pitch's strike rate sets which counts follow, and count drives usage: **1–8 points of apparent effect with ZERO true sequence dependence.** ⚠️ **Unlike F-287 the fix is NOT free** — comparing within count takes 9 cells to 108, failing the budget by 3–6×. **You can have an unconfounded estimate or a powered one, not both** |
| "His slider plays better after the heater — throw more?" | **F-299 — NO.** F-269's error transplanted from the marginal distribution to the transition matrix, which makes it **the stride-length error (F-043/F-044/F-045) in its THIRD venue.** At an interior optimum every used sequence has equal marginal value |
| Then why bother at all? | **F-299 — because equilibrium needs an ADAPTING opponent.** A college hitter sees a conference starter ~8 PA a season and cannot equilibrate; adaptation runs through the **advance report**. So the posture is **opponent-dependent** — ⚠️ a question for your own analyst, never a claim about a named opponent |
| What is it worth? | **F-296 — 0.8–6.4 runs per college season** for an exploited 20-point tendency. Above times-through-the-order (~1 run, F-288), below a gross mix error (F-272). ⚠️ **Three stacked upper bounds; the ORDERING is usable, the cells are not** |
| The one thing to actually run | **F-300 + `pitch-sequencing.md` §8 — the REPEAT RATE.** $P(\text{SL} \mid \text{prev}=\text{SL})$ vs the marginal. Below marginal = the over-alternation signature. **~42–47 observations, twenty minutes, and it tests the only mechanism in the topic** |
| Is the minimax literature usable? | **F-302 — NOT YET, and not singly.** Kovash & Levitt (NBER w15347) arrived **with a published 2024 rebuttal attached** that changes the unit from pitch TYPE to pitch LOCATION. **Import the pair or neither. Do not quote the "two additional victories" figure** |

### Catcher framing, the zone edge, and command-metric contamination — **added 2026-09-11**

| Question | Go to |
|---|---|
| How big is the zone I'm actually throwing to? | `library/catcher-framing-command-measurement.md` §1 — **F-305.** The **ball-CENTRE** called zone is **19.90 × 24.50 in**, +33% area over the rulebook rectangle, perimeter **88.8 in**. Every framing argument and every called-strike command metric lives on that perimeter. ⚠️ **Never a cue** |
| What can a catcher physically do? | **F-306.** The umpire judges the ball **where it is caught**, ~1.5–2.0 ft past the plate, and it keeps dropping: **2.0 in (4-seam), 2.4 (sinker), 2.8 (SL), 3.7 (CB); horizontal only 0.9 in.** Lever ∝ tan(VAA) ⇒ framing is **vertical- and bottom-of-zone-dominant**, derived without reading anyone. ⚠️ **MARKER, NOT LEVER** |
| Does it matter whether tonight's umpire is tight? | **F-307 — SECOND-ORDER.** Converted calls = **δ · f₀**, and the umpire's precision σ_u **cancels exactly**. Portable form: **~7 calls per 100 taken pitches per inch.** ⚠️ Say "about 7," never "7.38" (Dispute #23) |
| What is a catcher worth? | **F-308 — ~8 runs per college season for half an inch**, the largest single item this corpus has priced (vs ~1 R for TTOP, ~0.2 R for 0-2). **Backward check: the entire MLB best-to-worst framing spread implies only 0.35–0.70 in** against a ~2-in available lever. ⚠️ **Ordering usable, cells not.** A roster decision, not a pitching one |
| **How much of his command number is him?** | **F-309 — ROUGHLY HALF, at the scale that matters.** A realistic one-season command gain = **4.52 pts**; changing catchers (δ=0.5 in) = **3.69 pts**. **Ratio 0.82.** Only 15% of the *large cross-sectional* gap — it is the **small within-athlete** change where contamination equals signal (the F-094 pattern again). ⚠️ **BIAS, NOT NOISE** — assignment isn't random, so more data makes it MORE confident. Second worked example after F-287 |
| So what do I measure instead? | **F-310 — TRACKED LOCATION, and it's FREE.** Zone rate / edge rate / miss distance are framing-immune by construction and use 100% of the sample. **Contrast F-298**, where the unconfounded estimator cost 3–6× and failed the budget. ⚠️ Clean ≠ fast: **2.4 starter-seasons**. ⚠️ Within-pitcher at similar usage only (Dispute #23b) |
| Is ABS at my level? | **F-311 — YES.** SEC ran the challenge system in the **2026 conference tournament**; NCAA approved **all three divisions from 2027**. **The pitcher is one of three who may challenge.** F-283's conditional resolved. ⚠️ Multi-outlet but snippet-only |
| Should he ever challenge on 0-2? | **F-313 — NO, and the rule now survives its best attack.** The count-dependent umpire zone (F-312) is the strongest argument *for* 0-2; it needs an **18.2×** overturn edge and can supply at most **1.86×**. **Margin ~9.8×** |
| What is the new queue head? | **F-312 — arXiv `2609.03786`.** Reportedly **−17.17 pp** called strikes on 0-2, ~zero under ABS. If real, **count composition outranks the catcher** as the dominant command-metric confound. ⚠️ **SNIPPET-ONLY — do not quote either number** |

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

### What is CONTESTED — the twenty-two open disputes
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
| 17 | Is deception priced in positional separation at the commit instant, or must it be priced in optical expansion? | NARROWED — added 2026-09-04; the "factor of six" ratio was **withdrawn** the same cycle, the linear-vs-quadratic **ordering** was defended |
| 18 | Does the air-density movement ratio extend to seam-shifted-wake pitches, or only to clean Magnus pitches? | OPEN — added 2026-09-05; biomechanist conceded the model has no SSW term. **Cleanest for the pitches it matters least for**; settleable from existing Hawk-Eye data. **Revisited 2026-09-06: unmoved, and BLOCKED ON EGRESS rather than on reasoning** |
| 20 | Does a MANUFACTURED count train the real count — and is the strike probability *q* a property of the count or a move in a game? | OPEN — added 2026-09-07. **Two objections to the same model.** **(a) Transfer: CONCEDED IN FULL by the coach** — the cycle's only executable recommendation rests on F-197, a transfer study that does not exist; he keeps it because the alternative is 17 seasons, and states the contingency. **(b) Equilibrium: partially defended** — *q* is a choice in a two-player game, not a coin; the count-varying-*q* run moved no count more than 2 places, but a genuine game solution was never attempted. A third challenge — that a 4.9–18.2× quantity is a direction and not a table row — was **conceded in full** |
| 19 | Is the "more-used pitch should look better" wedge a finding, or a model wearing a finding's clothes? | NARROWED — added 2026-09-06. Biomechanist **conceded the F-269 magnitude table** (never quote the cells) and **kept the Nash Score critique**, one half of which (threshold below its own SE) needs no model at all. Coach accepts that half unreservedly, holds the other as "probably right, not yet demonstrated." Settled by the §6 panel regression |

| 23 | Is the framing-contamination result a finding, or a Gaussian pitch-location model wearing a finding's clothes? | NARROWED ON THE SPOT — added 2026-09-11. Anatomist **CONCEDED the f₀ VALUE** (a model output calibrated to remembered league rates in a cycle that read nothing — say "about 7 per 100 per inch," never 7.38) and the biomechanist **DEFENDED THE STRUCTURE** on three specifics: the σ_u cancellation is an **identity**; the 0.82 ratio is more robust than either half because numerator and denominator share the same boundary density and partially cancel; and the **bias-not-noise** argument depends on no magnitude at all, only on catcher assignment being non-random. **#23b IS GENUINELY OPEN:** if usage drifts WITH command, zone rate is contaminated even within-pitcher and F-310's "free fix" is not free. Settled by three queries against any program's own pitch log |
| 22 | Is the sequencing detection asymmetry a finding, or two different statistical tests wearing a finding's clothes? | NARROWED — added 2026-09-09. Biomechanist **CONCEDED the ratio** (the 81×–5,208× span is convention-dependent and scales entirely with the unmeasured $D$ — say the direction, never the number, as with F-269 and F-278) and **DEFENDED the direction**, which comes from the quantities rather than the tests: a proportion's variance is bounded at 0.25 while per-pitch run value has SD 0.20–0.30 against effects of order 0.002–0.016 runs. Two sub-disputes: **#22b** the scouting-capability conditional, defended as *bounding* not *establishing* — it needs only that opponent analytics capability is non-uniform, and the SEC/midweek split is an ILLUSTRATION, not a measurement; **#22c** whether the F-284 retraction re-imported what the rule excluded, **conceded in part and narrowed on the spot**. Settled for all three by measuring $D$ — or, for #22c, by opening one arXiv page |

| 21 | Is the third-time-through decline FAMILIARITY or FATIGUE? | OPEN — added 2026-09-08, and **the most expensive open question in the file**: the two have OPPOSITE training answers (arsenal, bought in February vs capacity, bought in the fall), so a program that guesses wrong spends an off-season on the wrong problem. The anatomist's challenge to the coach — *you cannot hold a smooth fatigue mechanism AND a lineup-turn heuristic* — was **CONCEDED IN FULL**, and the coach's recommendation was rewritten in pitch count. Settled by regressing outcome on pitch count AND a TTO indicator, exploiting that the third pass arrives anywhere from pitch 62 to 95. **No new instrumentation. Whether it has already been run is UNKNOWN and is deliberately not recorded as a gap** |

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

### Re-import vectors — one closed 2026-08-17, three live

**🚨 ADDED 2026-09-06 — two ACTIVE, CURRENTLY-INDEXED laundering channels, caught in a single field sweep. Both will be quoted back to this program by athletes, parents and staff.**

- **`accio.com/biz-sportshealth/` — a content-farm cluster fabricating ASMI, NCAA and Little League citations (F-274).** At least five templated near-identical articles spanning youth baseball, collegiate softball and softball science, asserting the *same* invented finding with the numbers barely changed. The fabricated figures, recorded so a future search surfaces the debunking: *"2026 ASMI data … ≥30% slot-consistency improvement over 8 weeks gained 1.2 mph"*; *"2026 NCAA biomechanics data … 1–2 mph within 4 weeks"*; *"22% improvement in strike-zone command … Little League Medical & Safety Advisory Committee, 2026"*; *"±3° release-arm angle variation directly compromises vertical accuracy."* **No sample size appears anywhere.** **NEVER CITE accio.com.** ⚠️ **The laundering mechanism, observed live:** a search summariser reported one farm claim as *"also corroborated in another source"* — where the other source was **a second page from the same farm.** **Two fabrications citing each other read as independent replication to any summariser and any hurried human. This is how a fabrication enters a corpus without anyone lying to you.** ⚠️ **Collateral damage:** arm-slot consistency is a *real* topic with real corpus material (F-135, F-171, F-176); the farm has attached invented magnitudes to a legitimate idea, which is far harder to filter than an invented topic would be.
- **The Nevada/Reno stride-length press release (F-275).** *Nevada Today*, May 2026, states an optimal stride length of **"roughly 80% to 87% of a pitcher's height"** with a two-sided injury penalty. The underlying study is already registered at **F-046/F-242 as an unpublished master's thesis with no velocity outcome and no control group.** **Nothing about the evidence changed — only the packaging.** A cross-sectional observation has become a prescription, which is THE ONE RULE's worked example (F-043/F-044/F-045: stride length moved experimentally twice, no gain, one loss). **A press release is a higher-credibility laundering channel than a content farm**, because it carries a real institution's name and a real study behind it. Compare F-274: **the farm invents a study; the press release over-reads a real one — and the second is harder to catch. This corpus has already been caught by it once (F-240).**

**Carried forward from earlier cycles:**


1. ~~**The daily briefs were never corrected.**~~ **CLOSED 2026-08-17 — back-correction applied in place.** `daily/2026-08-13-velocity.md` asserted "not one study at 85+," "+1.35 mph," "mean -1.15 mph," the Gdovin removal framing, and stride length as one of "the two free mechanical levers"; `daily/2026-08-13-stuff-command.md` carried the reversed changeup framing. **Every affected brief now carries a ⚠ banner at the top listing which of its claims were later corrected, plus an inline `⚠ CORRECTED 2026-08-17` notice immediately after each superseded assertion**, giving the current number, the design, and the library file and F-ID. **The original text was NOT deleted or rewritten** — these remain dated historical records, and the trail of what the program believed and when is intact (which matters, because that trail is the evidence for F-240). Annotated — 16 inline notices across 5 files: `2026-08-13-velocity.md` (10 notices), `2026-08-13-coach.md` (3 — its §2.2 script, the Kusafuka r = 0.73 label, and its §5 changeup row, which contradicted its own §9), `2026-08-13-stuff-command.md` (1), `2026-08-12-biomechanics.md` (1 — stride length as the "clean win"), `2026-08-12-coach.md` (1 — Bloebaum rho = 0.22 in a command context, F-109). `2026-08-12-anatomy.md` was checked and left untouched. **They are still dated snapshots, not current reference — read the library files for current state.** (F-241)
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
- **No published within-pitcher pitch-to-pitch SD of induced vertical break for an 85+ arm** — added 2026-09-05. The corpus does not hold this number, which is why F-264's detection table is bracketed across SD = 1.0/1.5/2.0 in rather than exact. **Computable from any program's own TrackMan in an afternoon**, and a prerequisite for reading any movement change anywhere (F-264).
- **No test of whether seam-shifted-wake movement scales with air density or non-monotonically with Reynolds number** — added 2026-09-05. Settleable from existing Hawk-Eye data by comparing one pitcher's sinker/sweeper movement at a sea-level and a high-altitude park against the density ratio. No new instrumentation required (Dispute #18, F-260).

### Topics the corpus has not researched at all
- ~~**Pitchability, sequencing and in-game usage.**~~ **PARTIALLY OPENED 2026-09-06** — `library/pitch-mix-sequencing.md`, F-268→F-273, F-276. **The USAGE half is now covered and is source-independent arithmetic**: the optimality condition, why the more-used pitch should look better, the run-value noise floor, the flat objective, and "commit or cut." **Three limits: (a) opened in a fully blocked cycle, so nothing was verified at source and the one empirical input (per-pitch run-value SD) is approximate and bracketed; (b) every magnitude scales with the anticipation slope $D$, which is UNMEASURED anywhere — the direction is safe to say, the numbers are not (Dispute #19); (c) it covers WHAT MIX, not WHAT NEXT PITCH.** **COUNT LEVERAGE CLOSED 2026-09-07** — `library/count-leverage.md`, F-278→F-283, all derivation. **TIMES THROUGH THE ORDER CLOSED 2026-09-08** — `library/times-through-order.md`, F-286→F-292. **The DECISION half is now covered and is source-independent arithmetic**: the individual-detection wall (790 seasons), the lineup-slot composition bias (56% of a scorebook split), the talent-gap decision rule, the ~1-run price of the whole question, and the input-vs-outcome asymmetry. **Two limits: (a) opened in a fifth consecutive blocked cycle, so the one empirical input (~10 wOBA pts per time through) is snippet-only and bracketed; (b) the MECHANISM — familiarity vs fatigue — is unresolved and its two answers point at opposite off-seasons (Dispute #21).** **SEQUENCING CLOSED 2026-09-09** — `library/pitch-sequencing.md`, F-294→F-303. **The NEXT-PITCH half is now covered and is source-independent arithmetic**: the vector-to-matrix parameter explosion, the two-party detection asymmetry, the granularity trap, the count-composition confound and its unaffordable fix, the equilibrium argument, and the transition-matrix audit. **Three limits: (a) opened in a sixth consecutive blocked cycle, so nothing was verified at source; (b) every RUN figure scales with the unmeasured $D$ while every DETECTION threshold does not — quote the second, never the first; (c) the 2024 minimax rebuttal argues the right unit is pitch LOCATION, not pitch TYPE, and if it is correct the whole file analyses the wrong object (F-302).** **Still entirely uncovered: attacking SPECIFIC hitters, and second-order (two-pitch-back) sequencing.** Stuff models still do not price any of it (F-168, F-172).
- **The anticipation slope $D$ itself — how much a pitch's effectiveness decays per point of usage share.** Added 2026-09-06. Every public sequencing metric implicitly assumes a value and none states one. **The estimation design needs no new instrumentation and Statcast already holds the data** (`library/pitch-mix-sequencing.md` §6). Currently the cheapest unanswered question in the corpus.
- **No bullpen-to-game command transfer study — now the corpus's most load-bearing applied gap.** Escalated 2026-09-07: the only executable recommendation the count-leverage cycle produced (the manufactured full-count block, F-282) rests entirely on an assumption F-197 says nobody has tested. Needs no new instrumentation (Dispute #20a).
- **No published count-frequency distribution or run-expectancy $(W-K)$ retrieved.** Added 2026-09-07. Both are single Statcast queries and both would convert F-279's bracketed pitch shares and F-280's bracketed run values into actual numbers. **Blocked, not absent** (F-277).
- **No game-theoretic solution of the ball-strike count.** Added 2026-09-07. Every count model in public circulation, this corpus's included, treats strike probability as exogenous when it is a move in a two-player game (Dispute #20b).
- **The crossover usage $p_c$ where execution-dose stops outrunning hitter anticipation.** Added 2026-09-06. Below it, "commit or cut" is correct and small doses are provably wrong; above it, ordinary equalisation applies. Nothing in the corpus bounds it (F-276).
- ~~**Hitter perception and reaction.**~~ **PARTIALLY OPENED 2026-09-04** — `library/hitter-perception.md`, F-251→F-259. **But opened in a fully egress-blocked cycle, so the GEOMETRY is covered and the PERCEPTUAL LITERATURE is not.** The clock, the commit instant, and the linear-vs-quadratic channel argument are arithmetic and durable. Everything about what hitters actually *see* — occlusion timings, advance-cue use, expert-novice differences — remains a 7-item unread queue (F-259). **Treat this topic as one-third covered.**
- ~~**Catchers, framing and the pitcher-catcher system.**~~ **PARTIALLY OPENED 2026-09-11** — `library/catcher-framing-command-measurement.md`, F-305→F-314. **The MEASUREMENT-CONTAMINATION half is now covered and is source-independent derivation**: the ball-centre zone, the plate-to-glove framing lever, the shift×density cancellation, the run valuation and its backward check, the catcher-equals-command-gain result, and the free fix. **Three limits: (a) opened in a SEVENTH consecutive blocked cycle, so nothing was verified at source and three empirical inputs are bracketed (the F-270 run table, the ±15–20 R framing anchor, the 1.5–2.0 ft catch distance); (b) f₀ is a MODEL OUTPUT calibrated to remembered league rates — the direction is safe, the cells are not (Dispute #23); (c) it covers the pitcher-facing MEASUREMENT question, NOT receiving technique, catcher development, pitch-calling, or the pitcher-catcher relationship.** ⚠️ **And it may already be outranked: if F-312's −17.17 pp count effect is real, COUNT COMPOSITION is a ~4× larger confound on the same metric.**
- **No measured pitch-location distribution for an 85+ arm — added 2026-09-11.** F-307's f₀ is calibrated to remembered league zone/swing rates because the corpus holds no location scatter for its own population. **One query against any program's TrackMan: the share of taken pitches within ±1 in of the called-zone line.** Fourth entry in the pattern of F-264, F-289 and the transition matrix: **already in every program's own data and nobody has published it** (F-307, Dispute #23).
- **No published boundary-band called-strike rate split by catcher — added 2026-09-11.** The single measurement that would settle F-309's contamination term. **~2,500 taken pitches per catcher detects a 0.5-in difference** (F-310).
- **Whether usage drifts WITH command — added 2026-09-11.** If it does, zone rate is contaminated even within-pitcher and F-310's free fix is less free than it looks. Nothing in the corpus bounds the usage-command coupling (Dispute #23b).
- **Receiving technique, catcher development and pitch-calling** — still entirely uncovered, and deliberately so: F-306 bounds what is geometrically *available* and says nothing about whether it can be *harvested*.
- **Psychology beyond motor learning** — competitive anxiety, routines, focus under fatigue, the mental side of an outing.
- **Return-to-throw after injury**, deliberately out of scope, though the interval-throwing modeling paper is logged (F-137).
- **Youth and developmental pitching**, deliberately out of scope by the 85 mph floor.
- **Nutrition, hydration and supplementation** beyond a single protein/fueling entry (F-140).
- **Female or softball populations.**
- **Non-fastball workload accounting** — whether a slider-heavy outing loads differently from a fastball-heavy one at equal pitch count.
- ~~**Environmental effects** beyond the Reynolds-number note (altitude, temperature, humidity, ball construction year to year).~~ **THREE OF FOUR CLOSED 2026-09-05** — `library/environment-air-density.md`, F-260→F-265. Altitude, temperature and humidity are now covered and are **source-independent arithmetic**, so unlike most of the corpus they carry no citation risk. **Two limits: (a) no empirical/Statcast validation was possible, so these are model predictions with one unread snippet-level corroboration; (b) the model has NO seam-shifted-wake term, so the clean density ratio is established for four-seams and 12-6 curveballs and is of unknown quality for sinkers and sweepers (Dispute #18).** **`ball construction year to year` remains entirely uncovered.**
- **Whether the familiarity-vs-fatigue decomposition of the within-game decline has ever been run.** Added 2026-09-08. The design is a two-term regression on any public Statcast panel and needs no new instrumentation (Dispute #21). **This is deliberately recorded as UNKNOWN rather than as a gap** — the corpus has been burned once already asserting an absence it had not searched properly (Known Correction #4), and no page was opened this cycle.
- **No within-outing fastball velocity SD published for an 85+ arm.** Added 2026-09-08. F-289's detection table is bracketed across SD = 0.8/1.0/1.2 mph rather than exact for the same reason F-264's is. **It is already in every program's radar log and nobody has published it.**
- **No published lineup-slot talent profile for college baseball.** Added 2026-09-08. F-287's +0.025 wOBA composition bias uses an illustrative profile; the SIGN is structural but the MAGNITUDE would be exact with one query.
- **No published transition matrix for any pitcher, with or without confidence intervals.** Added 2026-09-09. F-295 identifies this as **the only quantity in the entire sequencing topic a college program can measure within a season**, and nobody publishes it. **It is one query against a pitch log every program already owns.**
- **No published repeat rate (serial correlation) for an 85+ arm.** Added 2026-09-09. F-300's over-alternation signature is testable in **~42–47 same-pitch observations and twenty minutes of analyst time**, and it tests the only claim in sequencing with a mechanism behind it. Third entry in the pattern F-264 and F-289 established: **already in every program's own data and nobody has published it.**
- **No estimate of the anticipation slope $D$ — now blocking THREE topic areas.** Escalated 2026-09-09. It scales the magnitudes in mix (F-272), the predictability tax (F-296) and the detection asymmetry (F-295), and every quantitative disagreement in Dispute #22 reduces to it. **Unambiguously the corpus's most load-bearing unmeasured parameter.**
- **The economics of development** — beyond one WAR/FV conversion, nothing on what a velocity or command gain is actually worth to an athlete's contract.
- **Sample-level data.** The corpus has no primary dataset of its own; every number is from published literature, industry grey literature, or Statcast queries.

### Structural gaps in the corpus's own method
- **Nine research days exist** (2026-08-12, 2026-08-13, 2026-08-20 verification pass, 2026-09-04 through 2026-09-09). Most of the corpus is still only two cycles deep.
- **🚨 ADDED 2026-09-04, ESCALATED EVERY CYCLE SINCE — FOUR CONSECUTIVE CYCLES HAVE RUN WITH NO SOURCE ACCESS (F-277).** On 2026-09-07 `en.wikipedia.org` was denied as a control alongside every journal host, confirming a policy denial at the gateway rather than anything topic- or paywall-related. **The diagnosis changed on 2026-09-06 and it matters:** raw `curl` now fails to open a socket at all (HTTP `000`, including to `en.wikipedia.org` as a control) while the agent proxy reports `enabled: true` with **zero relay failures**. That is **an empty network allowlist in the remote execution environment, not an outage and not a proxy fault — it requires a human to change.** The brief's WORKING-domain list has been wrong three times and should be **deleted from the standing prompt**, not amended: three cycles have each burned their opening minutes rediscovering the same fact. **Probe egress before choosing a topic; if it is down, pick a gap that arithmetic can close.** Full record: F-259, F-266, **F-267**.
- **⚠️ The unread verification queue is now 15 items (+3 on 2026-09-07: arXiv 2603.04874 pre-release anticipation — the item most likely to resolve F-256; arXiv 2606.17345 counterfactual sequencing; and the MLB ABS challenge data). It and is the corpus's largest structural liability.** F-259's 7 remain entirely untouched after three cycles; +2 from 2026-09-05 (Nathan's Denver page; Purple Row's altitude series); +3 from 2026-09-06 (arXiv 2609.03810 *Unified Pitch Graphs*; the ESPN Nash Score article; **the per-pitch run-value SD underpinning F-270**). **A program that can compute but never read will slowly fill with internally-consistent unvalidated arithmetic** — and the corpus has now run **four consecutive arithmetic-only cycles**. The 2026-09-05 and 2026-09-06 findings are honest, but they are all model, and **nothing has checked a model against data in four cycles.**
- **⚠️ ADDED 2026-09-06 — the field sweep is now the corpus's highest-risk input, because WebSearch is the only working channel and it returns summaries rather than pages.** Two live laundering vectors were caught in one cycle: a **content farm** inventing ASMI/NCAA/Little League citations (**F-274**), and a **university press release** restating an uncontrolled thesis as a prescription (**F-275**). The farm case included a search summariser reporting one farm page as "corroborated by another source" that was **a second page from the same farm**. **Two fabrications citing each other read as replication.** Treat every snippet as a lead, never a magnitude.
- **Verification is incomplete and known to be incomplete** (F-242).
- **The daily briefs are not maintained** and contain superseded claims — **now annotated in place with dated correction notices (2026-08-17), but not rewritten.** Read them as history, not reference (F-241).
- **Nothing in the corpus has been tested against a real athlete.** Every protocol is inference from published data.

---

## 6. If you only read five things

1. **F-094** — between-pitcher and within-pitcher associations diverge wildly. Every cross-athlete comparison in this corpus is suspect by default.
2. **F-043 / F-044 / F-045** — the stride-length sequence, the worked example of a cross-sectional finding read as a lever, and what happened when two independent groups actually moved it.
3. **F-072** — +0.65 mph. The number to say to an 88 mph athlete on day one.
4. **F-171** — command is an angular problem, and 1 degree is a foot.
5. **F-240** — six corrections in one day, none a fabrication, all in the same direction. The epistemic finding that should govern how the next cycle reads anything.

**Two more worth adding since 2026-09-06:**
6. **F-273** — the mix decision cannot be learned from the athlete it is made about. Estimate the parameter league-wide, apply it as a prior, verify **compliance** and never **outcome**. The general form of F-257, two orders of magnitude more extreme.
7. **F-274** — two fabrications citing each other read as replication. The laundering mechanism, caught live, with a currently-indexed example.

**And two more since 2026-09-07:**
8. **F-279** — per-pitch leverage and total leverage peak in **different counts**, and the first pass of that model got it backwards inside an hour. The corpus's own worked example of a per-unit truth read as an aggregate truth, committed by this program rather than found in someone else's.
9. **F-284** — the fabrication is now coming from the **summariser**, not the page: a real author, a real year, an invented number. With `WebSearch` as the only working channel (F-277), this is the failure mode most likely to enter the corpus next.

**And two more since 2026-09-08:**
10. **F-287** — **more data makes this error more confident, not less.** The lineup-slot composition bias is 2.5× the effect it contaminates, and it is bias-in-expectation rather than noise, so every instinct a coach has about "wait for a bigger sample" makes it worse. The corpus's first worked example of a bias that *does not* shrink.
11. **F-290** — the fifth time this program has caught itself **compressing a nuanced result into a verdict that inverted its practical meaning.** Not a wrong number and not a bad source: a one-line summary that turned "the decline is continuous, not stepped" into "the decline isn't real." Every previous instance happened in the same paper → table-row step (F-240).

**And two more since 2026-09-09:**
12. **F-295** — **the opponent can measure your pitcher's sequencing and you cannot**, by 81×–5,208×. The corpus's input-vs-outcome asymmetry (F-257, F-289) acquires a genuinely new feature: it is asymmetric **between the two parties**, not merely between two measurements of one thing. The strategic inversion it forces — *build the report your opponent is building* — is the most directly usable thing produced in six blocked cycles. ⚠️ **Say the direction, never the ratio** (Dispute #22).
13. **F-303** — **the first correction this program has ever issued in the SKEPTICAL direction.** Every previous one ran toward more confidence than the source supported (F-240, Known Corrections #1–#6). This one withdraws a *fabrication* verdict. **A defensive rule has a false-positive rate, and it suppresses true findings INVISIBLY** — a suppressed true finding leaves no trace to audit, whereas an imported false one eventually collides with something. **A corpus that only ever audits its credulity will never find these.**

**And two more since 2026-09-11:**
14. **F-309** — **your strike percentage is a two-person statistic.** At the scale of a realistic one-season command gain the catcher term (3.69 pts) is 0.82× the command term (4.52 pts), and because catcher assignment is not random it is **bias, not noise** — the corpus's second worked example, after F-287, of an error that gets *more* confident with more data. It is only 15% of the *large cross-sectional* gap: **the contamination lives precisely where development lives, in the small within-athlete change.** The F-094 between-vs-within pattern arriving in a third venue.
15. **F-307** — **the umpire's precision cancels.** Converted calls = δ · f₀ regardless of σ_u, because a sloppier umpire converts more pitches near the line and fewer far from it in exactly compensating amounts. The corpus's cleanest instance of a result that **survives not knowing the thing nobody knows** — and a template for what a blocked cycle should be hunting for.

---

## 7. ⚠️ QUARANTINE — findings that are NOT findings yet (added 2026-09-04)

The 2026-09-04 cycle ran with **all outbound HTTPS denied (403 on every host)** and could open **no primary source**. It deliberately produced **no source-verified literature finding.** Three registry entries from that cycle are **leads in quarantine** and must not be quoted, compressed, or promoted until someone reads the paper:

| F-ID | What it is | Status |
|---|---|---|
| **F-255** | Higuchi et al. 2016 occlusion study (PLOS ONE, PMID 26848742) — reportedly, occluding the final 150 ms does not change mean contact location | **UNVERIFIED — SNIPPET-ONLY. Read this first.** Would independently corroborate F-254 by a wholly different method |
| **F-256** | "A slowed arm gives the changeup away" | **FOLKLORE with a plausible mechanism.** Universally repeated, never measured. Legitimate to *check on video*; not legitimate to state as known |
| **F-258** | Brill & Wyner 2022 Bayesian TTOP re-analysis | **UNVERIFIED — SNIPPET-ONLY.** Do not change a third-time-through decision on it |

**The rest of that cycle (F-251, F-252, F-253, F-254, F-257) is arithmetic** — closed-form drag integration and power calculations, computed in-cycle, dependent on no source. Those are safe. **F-252 carries one unverified external input**, a ~150 ms swing duration, and its sensitivity band is stated wherever it is used.

**⚠️ ADDED 2026-09-06 — the quarantine now extends to the pitch-mix work, in a specific and limited way.** The 2026-09-06 cycle (F-267, third consecutive block) produced nine findings. **Six are derivation** — F-268, F-269, F-272, F-273, F-276 and the power arithmetic of F-270 — and depend on no source. **Three carry a flag:**

| F-ID | What needs watching | Status |
|---|---|---|
| **F-270** | The **per-pitch run-value distribution** (SD ≈ 0.214 runs) was reconstructed from memory with no page open | **ONE UNVERIFIED EMPIRICAL INPUT.** Bracketed ±40% and the conclusion survives — overturning it needs the SD wrong by ~30×, not 40%. **Still: verify against a Statcast run-value table when egress returns, and issue a dated correction to the tables if it lands outside 0.20–0.30, even though the conclusion holds** |
| **F-269** | The **magnitude table** of how far apart run values "should" sit | **MODEL OUTPUT, NOT A FINDING — the coach's challenge was upheld (Dispute #19). Say the DIRECTION, never the cell values.** Scales entirely with the unmeasured $D$ |
| **F-271** | ESPN's Nash Score description | **SNIPPET-ONLY — the article was never opened.** The arithmetic objection (threshold below its own SE) is sound regardless; the *description of the metric* is not verified |

**⚠️ ADDED 2026-09-07 — the 2026-09-07 cycle (F-277, fourth consecutive block) produced eight findings. SIX ARE PURE DERIVATION** — F-278, F-279, F-281, F-282 and the decision rule of F-283 depend on no source and are re-derivable in twenty lines. **Two carry a flag:**

| F-ID | What needs watching | Status |
|---|---|---|
| **F-280** | The **walk-minus-strikeout run gap $(W-K)$** was reconstructed from memory with no page open | **ONE UNVERIFIED EMPIRICAL INPUT**, bracketed 0.55–0.62 runs. **Every absolute run figure scales linearly with it; no RATIO in the file depends on it.** Verify against a run-expectancy table when egress returns and issue a dated correction if it lands outside the bracket. Same posture as F-270 |
| **F-283** | Every **ABS challenge empirical figure** (overturn rates, the pitcher-participation gap, per-player records) | **SNIPPET-ONLY — no article was opened.** The decision rule is sound arithmetic regardless; the empirical picture is a reason to look, not a measurement. **Do not repeat these numbers to anyone before a page is opened** |

**And a rule change, not just a flag (F-284).** The 2026-09-07 sweep caught the **search summariser itself** emitting an unprompted, uncorroborated magnitude ("Park et al., 2026 … 12.4 million Statcast pitches") attached to what appears to be a real author and a real year. This is an escalation from F-274, where the fabrication at least lived on a findable page. **NEW STANDING RULE: in a blocked cycle, a magnitude that appears only in a search SUMMARY and never inside a quoted snippet is treated as FABRICATED until a page is opened.** Blocklist additions: **`afroliterarymagazine.com`** (fabricated ASMI velocity claim), alongside **`accio.com`** (F-274).

**⚠️ ADDED 2026-09-08 — the 2026-09-08 cycle (F-285, fifth consecutive block) produced nine findings. SIX ARE PURE DERIVATION** — F-286, F-287, F-288, F-289, the arithmetic objection inside F-291, and the composition analysis are closed-form and re-derivable in thirty lines. **Three carry a flag:**

| F-ID | What needs watching | Status |
|---|---|---|
| **F-286 / F-288** | The **~10 wOBA points per time through the order** was taken from search snippets describing Brill, Deshpande & Wyner (JQAS 2023) | **ONE UNVERIFIED EMPIRICAL INPUT.** F-286's *conclusion* is immune — it survives the effect size being wrong by a factor of 25. **F-288's magnitudes are NOT immune: the 20-point break-even and the ~1-run season price scale linearly with it.** Verify when egress returns and issue a dated correction. Same posture as F-270 and F-280 |
| **F-290** | The **substance** of the TTOP paper (continuous vs stepped, the discontinuity posteriors, the design) | **SNIPPET-ONLY — no page opened. F-258 STAYS IN QUARANTINE.** The *citation* correction (Deshpande omitted; JQAS 2023 not 2022) IS established, corroborated by the second author's own publications page |
| **F-291 / F-293** | Every reported figure from `sportsnaut.com` and `medium.com/@ParadigmPDS` | **SNIPPET-ONLY, pages unfetchable.** The arithmetic objection in F-291 stands without them. **Do not repeat the 41% false-alarm rate or the "two-thirds of college arms" figure** |

**And a second extension to the F-284 rule (F-293).** The 2026-09-08 sweep caught the search summariser rendering a bolded heading, *"Modern Information Asymmetry (2026)"*, and asserting that *"a 2026 hitter has already reviewed pitch sequencing data on the dugout iPad between at-bats."* **No snippet contains this.** F-284 was an invented magnitude; this is invented **narrative**, complete with a prop — softer, and therefore more likely to be absorbed, because nobody fact-checks a scene. **RULE EXTENDED: in a blocked cycle, treat as fabricated not only an unquoted magnitude but any concrete factual DETAIL appearing in a summary and in no snippet.**

**⚠️ ADDED 2026-09-09 — the 2026-09-09 cycle (F-294, sixth consecutive block) produced ten findings. SIX ARE PURE DERIVATION** — F-295, F-296, F-297, F-298, F-299 and the arithmetic inside F-303 are closed-form power calculations and simulation, re-derivable in thirty lines. **Four carry a flag:**

| F-ID | What needs watching | Status |
|---|---|---|
| **F-296** | Every **absolute run figure** in the predictability tax | **SCALES LINEARLY WITH THE UNMEASURED $D$**, and rests on two further assumptions — that the hitter has the report AND can use it (against F-251/F-252, advance knowledge is a *prior*, not an in-flight read), and that the tendency is real (F-297 says most are not). **Three stacked upper bounds. The ORDERING against F-280/F-288/F-272 is the usable output; the cell values are not.** Same posture as F-269 |
| **F-299** | That hitter anticipation responds to **CONDITIONAL** frequencies the way it responds to marginal ones | **AN ASSUMPTION, DEMONSTRATED NOWHERE.** The stationarity mathematics is inherited and sound; this bridge to it is not. If it fails, the equilibrium argument does not apply to sequences at all |
| **F-300 / F-302** | Every reported figure from Kovash & Levitt, the 2024 *Sports Economics Review* rebuttal, and Walker & Wooders | **EXISTENCE VERIFIED across multiple independent institutional hosts; SUBSTANCE SNIPPET-ONLY, no page opened.** **DO NOT REPEAT THE "TWO ADDITIONAL VICTORIES" FIGURE** — a working-paper number the snippet itself calls back-of-the-envelope, with a published rebuttal. **Import the pair or neither** |
| **F-301** | Next-pitch prediction accuracies (~70% binary, 66.62%, 59%, 80.88%) | **SNIPPET-ONLY, MIXED SOURCES.** The reported **"311% improvement over naive" is a ratio artefact** — arithmetically possible only when the naive baseline was near zero — and **must not be repeated.** Note also these bound the exploitable information from ALL features, not from the previous pitch alone |

**And a correction running the OTHER WAY (F-303), which is a first.** The 2026-09-09 sweep found that a magnitude F-284 classified as **FABRICATED** two cycles ago — *"12.4 million Statcast pitches"* — reappeared from a different query attached to a specific arXiv identifier (`2601.11904`) and passes an independent arithmetic check: 2,430 games × 18 seasons (2008–2025) at 285 pitches/game = **12.47 M**, within 0.6%. **The verdict is downgraded to UNVERIFIED WITH A CANDIDATE SOURCE.** ⚠️ **NOT withdrawn:** the F-284 operating rule itself, the "Park et al." attribution, or F-284's item (1). **The anatomist's challenge — that the retraction used a lower bar than the verdict — was CONCEDED IN PART and narrowed the retraction on the spot (Dispute #22c).** What is withdrawn is only the *positive* claim that no such number exists in any source.

**⚠️ ADDED 2026-09-11 — the 2026-09-11 cycle (F-304, seventh consecutive block) produced eleven findings. SIX ARE PURE DERIVATION** — F-305, F-306, F-307, F-309, F-310 and F-313 are rule geometry, flight geometry and closed-form probability, re-derivable in forty lines and dependent on no source. **Five carry a flag:**

| F-ID | What needs watching | Status |
|---|---|---|
| **F-307 / F-309** | **f₀ = 7.38% of taken pitches per inch**, and with it every magnitude in the head-to-head | **MODEL OUTPUT, NOT A MEASUREMENT.** Calibrated to a 2-D Gaussian (σ_p = 10 in) and remembered league rates (47% swing / 68% in-zone / 28% chase) in a cycle that read nothing. **Say "about 7 per 100 per inch," never "7.38"** (Dispute #23). **What does NOT depend on it:** the σ_u cancellation (an identity) and the bias-not-noise argument (which needs only non-random assignment). Same posture as F-269 |
| **F-308** | The **±15–20 R/season MLB framing spread** used in the backward check, and the **1.5–2.0 ft catch distance** in F-306 | **TWO UNVERIFIED EMPIRICAL INPUTS**, both reconstructed/assumed with no page open. Every run cell scales linearly with the first; every drop figure with the second. **The ORDERING against F-280/F-288/F-296 is the output; the cells are not.** Also inherits F-270's own flagged run-value SD |
| **F-311** | Every **ABS specific** — dates, three challenges per team, who may challenge, the 2027 division scope | **SNIPPET-ONLY, NO PAGE OPENED**, though existence is corroborated across genuinely independent outlets (ESPN, Baseball America, Annenberg, an Ole Miss local outlet). **Verify with compliance and umpiring contacts before acting.** The *existence* of SEC ABS play is solid; the mechanics are not |
| **F-312** | **−17.17 pp (0-2) and +6.61 pp (3-0)** from arXiv 2609.03786 | **EXISTENCE VERIFIED across independent arXiv paths; SUBSTANCE SNIPPET-ONLY. DO NOT QUOTE EITHER NUMBER.** ⚠️ **Named hazard:** "0-2 tightens, 3-0 widens" is long-asserted American baseball folklore, so a confabulated confirmation would be easy to produce and hard to doubt, and two-decimal precision is exactly F-284's texture. **NEW QUEUE HEAD anyway**, because it would touch three areas in one page |
| **F-314** | The **calledthird.com figures** (51.7% / 33.0% / 18.7-pt gap) | **UNVERIFIED, from a source whose only credibility signal is SELF-GENERATED.** Recorded **against interest**: the 18.7-pt gap backs into 0.75–1.1 in, encouragingly close to F-308's independent 0.35–0.70 in — **and that convergence is explicitly NOT claimed as corroboration.** Two unverified numbers agreeing is the F-274 pattern |

**And a third extension to the F-284/F-293 rule (F-314) — this one aimed at the defence itself.** Asked whether an unfamiliar site was credible, the search summariser returned four numbered methodological endorsements ("two independent models ... verify each other's code line by line," "pre-registered," "a public queue") **whose every cited link was a page on the site being assessed.** No independent assessment appeared anywhere. F-274 was a farm inventing a study; F-275 a press release over-reading a real one; F-284 an invented magnitude; F-293 an invented narrative. **THIS ONE DEFEATS THE CHECK THIS PROGRAM RUNS ON EVERY NEW SOURCE: a site that describes itself as rigorous will be reported back to you as rigorous. RULE: a credibility answer whose cited links all point at the source being assessed is not an assessment — ask who CITES it, and treat absence of independent citation as the answer.**

> **The standing rule this adds (F-259): a cycle that cannot read papers must not write table rows.** The corruption this corpus keeps catching happens in the compression from paper → table row → recommendation (F-240). A blocked cycle is that compression with the paper removed entirely — the highest-risk condition this program can run in. **The correct output of a blocked cycle is arithmetic, a quarantined queue, and an explicit statement that nothing was verified.**
