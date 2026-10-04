# THE BETWEEN-START WEEK — days of rest, the side session, and the next start

**Created 2026-10-04 (Cycle 34). Findings F-575 → F-587. Disputes #57, #58.**

> ⚠️ **FIFTH CONSECUTIVE FULLY EGRESS-BLOCKED CYCLE. ZERO primary texts opened. Every citation in this file is SNIPPET-ONLY except the sections marked DERIVED, which are arithmetic.** `WebFetch` returned `EGRESS_BLOCKED` on `ncbi.nlm.nih.gov` and on `ijspt.scholasticahq.com` — both listed WORKING in the standing brief. `curl` returned `CONNECT tunnel failed, 403` on `example.com`, `pmc.ncbi.nlm.nih.gov`, `sportrxiv.org` and `frontiersin.org`.

---

## 1. The one-paragraph version

**The calendar is not a lever and the load is.** Four extra days of rest is worth about **0.06 ERA** (F-576); the rolling 5- and 10-game pitch load carries **2× and 3.1×** the per-pitch weight of the last outing (F-575). The only place rest visibly moves a physical output is the **reliever** — **−0.5 mph back-to-back, −1.5 mph on three straight** — and that is a marker produced by manager selection, not an effect (F-577, Dispute #57). **What the pitcher throws between starts has never been manipulated with a next-start outcome by anyone, anywhere (F-580)**, which means this corpus's own day-by-day template (F-214) is reasoning cited to itself (F-587). The single best-designed intervention in the area measured a dynamometer rather than a pitcher (F-581) — the same design error caught at a different literature the day before (F-582). And at the scale a schedule change plausibly buys, **one pitcher cannot detect it in one season** (F-586).

---

## 2. The evidence table — what exists, and what it measured

| Question | Best evidence | Design | Outcome measured | Verdict |
|---|---|---|---|---|
| Does an extra rest day improve the next start? | Bradbury & Forman 2012, MLB SP 1988–2009 | Observational panel | Next-game ERA | **≈ 0.015 ERA/day, n.s. NULL** |
| Does cumulative load hurt the next start? | same | Observational panel | Next-game ERA | **Yes; 2–3× the last game's weight** |
| Does rest move reliever velocity? | THT, ~300k PITCHf/x | Observational, usage-pattern | Fastball mph | **−0.5 / −1.5 mph. MARKER (Dispute #57)** |
| Does a side session help the next start? | **nothing exists** | — | — | **GAP (F-580)** |
| Does the side session volume/intent matter? | **nothing exists** | — | — | **GAP (F-580)** |
| Does post-outing recovery work? | JSCR 2026, PMID 42172289, n=16 | **INTERVENTION, within-subject** | **Isokinetic torque + soreness** | **Ice yes, percussion no — ON THE WRONG OUTCOME (F-581)** |
| How much softer is a pen than a game? | **nothing exists** | — | — | **GAP — one afternoon of radar logging (F-579)** |
| What is the post-24h recovery curve? | **nothing exists, incl. commercially** | — | — | **GAP by the vendor's own admission (F-585)** |

**Read the right-hand two columns together. That is the whole topic: of eight questions a coach actually has, five have no evidence at all, one has evidence on the wrong outcome, and the two with real evidence both return approximately zero.**

---

## 3. The population mismatch nobody flags

Today's findings are unusual for this corpus in that the **velocity** population is right — MLB starters and relievers sit well above the 85 floor. **The CALENDAR population is wrong, and it is wrong in the direction that matters.**

- **MLB:** five-day rotation, one high-intent exposure, club controls the schedule.
- **NCAA:** **seven-day weekend cycle.** A Friday starter has two extra days every week, and may also be used in relief on Sunday.
- **Showcase/draft-followed HS:** no cycle at all — Friday for the school, Sunday for the travel team, a pro-day workout on a Tuesday.

**Every rest-day estimate in this file was computed on a 5-day cycle and is being read against a 7-day one.** The direction of the error is at least knowable: if more rest buys ~nothing in MLB, the extra two days in college buy, at most, ~nothing as well. **The null transfers more safely than a positive would have.** But the college-specific question — *does the extra Sunday availability cost the Friday start?* — is not the same question and has no answer here.

---

## 4. DERIVED — the detection table, and why one pitcher cannot answer this

Paired comparison, α = .05 two-tailed, 80% power: **n ≈ 7.85/d².** At the corpus's carried assumption **SD ≈ 1.0 mph** between sessions:

| Effect | d | Paired starts needed |
|---|---|---|
| 0.5 mph | 0.50 | **≈ 32** |
| 0.75 mph | 0.75 | **≈ 14** |
| 1.0 mph | 1.00 | **≈ 8** |

**A college starter makes ~15–17 starts a season.**

**THE ONLY DESIGN THAT FITS A PROGRAM:** staff-level, **6 starters × 15 starts ≈ 90 paired observations**, with the protocol **alternated week to week per pitcher, assigned in February.** Never a first-half/second-half split — in-season velocity drift is large and would swallow the effect whole.

**FOR COMMAND:** F-186's bar — **~200 tracked pitches to claim a 2-inch gain.** At 10 declared pitches per side, **20 side sessions ≈ most of a season.**

⚠️ **THE SD = 1.0 mph IS AN ASSUMPTION THE CORPUS HAS CARRIED, NOT A MEASUREMENT.** No start-to-start fastball-velocity SD has been published for an 85+ population. **One query against a program's own radar log retires it. If it comes back at 1.4, every number above roughly doubles and the staff-level design fails too.**

---

## 5. What the Marlins did, and the one sentence in the reporting that matters

**Bill Hezel, Marlins director of pitching (ex-Driveline, ex-Angels, ex-Phillies consultant).** The traditional between-start bullpen is gone, replaced by a **"pitch design session" with a hitter in the box**, each carrying **a written prescription** (two-strike putaways; sweeper spin; fastballs at the bottom of the zone). Some starters take the scheduled side as **a real relief appearance.** Rationale, quoted: *"if we can train close to the game and make it more game-like, that's probably a better training environment."*

**This is the first organisation-scale action on F-197 (no bullpen-to-game transfer evidence exists).** It is also, per the same reporting, a **dose increase**: *a hitter in the box brings out adrenaline that often prompts pitchers to throw harder than they otherwise should between starts*, and pitchers have told their agents they feel judged.

> **THE CORPUS'S READING: take the PRESCRIPTION, leave the HITTER.** The transferable idea is that the side session has a written objective before it starts rather than being thirty pitches of ambient mound time. That is F-185's declare-the-target rule applied to Tuesday — **free, already established, and claiming nothing new.** The hitter is what converts a recovery-week exposure into a near-game one (F-584), and the Marlins' reporting does not say they accounted for it.

---

## 6. 🚨 The fabrication (F-578) — and the new failure mode behind it

Three independent queries returned, as settled fact, that **the NCAA imposed a 110-pitch cap and a mandatory rest-day table in 2018.** All three trace to **one commercial SEO page selling a tally counter.** Every other rules hit across the same sweeps was a state high-school association. No `ncaa.org`. No news coverage. A live forum thread asking *"Should college baseball have pitch count rules"* — which cannot exist if the rule does. The quoted table is the **shape of an NFHS state table with the numbers raised.**

**THE FAILURE MODE HAS CHANGED, and this is the durable lesson.** The risk used to be a content farm you might stumble onto. The risk now is **a content farm that has become the only indexed answer to a question**, leaving the summariser nothing to disagree with. **A claim corroborated only by restatement is not corroborated — and three independent queries returning the same single source is restatement, not corroboration.**

**This is also the only verification in the file that does not need the network: an NCAA D1 pitching coach can settle it from memory.**

---

## 7. What to actually do this week with an 85+ arm

1. **Write the side session down before he throws it.** One declared objective (pitch type + intended finish location), one pitch count, one intent cap. Score miss distance in inches on the declared pitch. *(F-185, F-356, F-583 — established rule, new venue.)*
2. **Stop buying back days you did not lose.** Four extra rest days ≈ 0.06 ERA. Manage the rolling 10-outing pitch total instead. *(F-575, F-576.)*
3. **Treat a hard side as game pitches.** Not as "a pen." *(F-584, F-137.)*
4. **Pull the radar log and compute start-to-start velocity SD.** Free, one query, retires a bracket the corpus has carried for weeks. *(F-586.)*
5. **Settle F-578 from inside the building.**
6. **Do not announce that any of this worked** before the sample in §4 exists. *(F-586.)*

---

## 8. Gaps this topic leaves open

1. **No manipulation of between-start throwing with a next-start outcome, anywhere.** (F-580)
2. **No measured bullpen-vs-game velocity/intent gap.** (F-579) — *one afternoon with a radar gun.*
3. **No post-24-hour arm-recovery curve**, in the literature or in the largest commercial dataset. (F-585)
4. **No within-reliever version of the back-to-back velocity drop.** (Dispute #57) — *one Statcast query.*
5. **No effort-gradient study in the 85–100% range in an 85+ sample.** (Dispute #58) — the only part of the curve a between-start decision lives on.
6. **No SEM/MDC in hand for any between-start arm-strength monitor**, which makes the monitoring recommendation currently unfalsifiable. (F-585) — *egress-blocked, PMID 40904715.*
7. **No college-specific (7-day cycle) rest or workload estimate at all.** (§3)
8. **Unknown whether the JSCR 2026 ice/percussion trial measured ball velocity and did not report it.** (F-581) — *an F-466-class catch if so.*
