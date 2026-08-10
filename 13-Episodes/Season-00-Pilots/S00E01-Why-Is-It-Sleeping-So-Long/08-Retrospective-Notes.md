---
depends_on:
- 03-Story-Blueprint.md
- 05-Panel-Breakdown.md
- 06-Visual-Prompts.md
document: Retrospective Notes
episode: 01
last_update: 2026-08-10
season: 00
status: IN PROGRESS
title: S00E01 --- Why Is It Sleeping So Long?
universe: Lawn With Care Universe
version: 0.1.0
---

# S00E01 --- Why Is It Sleeping So Long?

## 08 --- Retrospective Notes

## Purpose

`03-Story-Blueprint.md` ("Pilot Experiment Notes") asks explicitly: if Panel 06 becomes overloaded with dialogue, document that finding for the Season 00 retrospective before the six-panel carousel format is locked for future episodes. This document is that retrospective, started while S00E01 is still in production so findings aren't lost before final review.

This is a living document. Update it as each open question below gets resolved, then change status from `IN PROGRESS` to `COMPLETE` before starting S00E02.

---

## Test 01 --- Separate Panel Generation

**Question:** Can six independently generated 4:5 images maintain enough continuity to feel like one episode?

**Finding so far:** Yes, with iteration. `S00E01-P01` through `P06` all have a `v2.0` revision alongside the original, meaning at least one full continuity-correction pass was needed. Worth tracking going forward: how many regeneration passes per panel, and which elements needed correcting (see Test 07).

## Test 02 --- Character Consistency

**Question:** Can Brooks and Sprout remain visually stable across separate generations?

**Finding so far:** Largely yes across the reviewed panels (P01, P04, P06). One open discrepancy: Brooks' hair reads as visible under the campaign hat in some panels, which conflicts with the approved Face rule in the Brooks Visual Canon Audit ("no visible hairstyle when hat is worn"). Logged as a separate finding in `Assets/References/Audits/Brooks-Visual-Canon-Audit-v1.0.md` — resolve before calling P04/P06 final.

## Test 03 --- Relationship Canon

**Question:** Can Brooks guide while Sprout retains discovery ownership?

**Finding so far:** Yes, in the panels reviewed — Sprout is closest to the shrub and the loupe in P04, and owns the reaction beat in P05 per the script. Brooks kneels to her level in P06 rather than standing over her.

## Test 04 --- Visual Science

**Question:** Can the plant evidence be shown clearly enough that the image contributes to learning?

**Finding so far:** The Discovery Frame inset in P04 clearly isolates the damaged foliage vs. the viable bud — this is the strongest visual-science moment in the episode and matches the Learning Objective's evidence logic.

## Test 05 --- Mobile Dialogue

**Question:** How much dialogue can fit without competing with the artwork?

**Status:** Open. This requires the actual lettered/composited panels (in `Assets/Panels/Lettered/`, currently empty except `.gitkeep`) to evaluate — clean art alone can't confirm text fit. P06 remains the panel most likely to be overloaded (`04-Script.md` flags it as "the primary density test"); check it first once lettering begins.

## Test 06 --- Discovery Frame

**Question:** Does a close-observation device improve comprehension?

**Finding so far:** Yes, based on the P04 clean artwork — the inset frame around the bud is legible and reads as an organic magnification device rather than a HUD/scanner, matching the "no futuristic interface" constraint.

## Test 07 --- Production Corrections

**Question:** Which elements create the most regeneration or compositing work?

**Status:** Open. Every panel has a `v2.0` file, which means something was corrected at least once across the board, but the specific reason per panel isn't recorded anywhere. Recommendation: going forward, note the reason for each regeneration (e.g. "badge drift," "Brooks led the discovery," "shrub silhouette changed") directly in this section so the pattern is visible before S00E02.

---

## Panel 06 Dialogue-Density Verdict

**Not yet determined.** The clean P06-v2.0 artwork reserves generous open sky/negative space, which is a good sign, but per `03-Story-Blueprint.md`'s own instruction this can only be confirmed once the approved dialogue (`04-Script.md`, P06 — three short lines plus a closing caption) is actually composited onto the image. Revisit this section once a lettered P06 exists.

---

## Six-Panel Format --- Preliminary Recommendation

**Too early to conclude.** Hold the format decision for S00E02 until Test 05 and Test 07 above have real data (post-lettering). If P06 turns out to require shrinking the three-line exchange plus caption to fit, that is itself the signal the Story Blueprint asked to watch for — the fix should be splitting the beat across an extra panel, not shrinking typography (per the Blueprint's explicit instruction).

---

## Next Steps

1. Complete lettering for at least P06 (the highest-risk panel) and re-evaluate Test 05.
2. Resolve the Brooks hair/hat discrepancy (regenerate or document as an approved exception).
3. Fill in Test 07 regeneration reasons retroactively if still recoverable from production history.
4. Flip status to `COMPLETE` and fold the verdict into `PROJECT_STATUS.md` before starting S00E02.

---

Status: **IN PROGRESS --- v0.1**
