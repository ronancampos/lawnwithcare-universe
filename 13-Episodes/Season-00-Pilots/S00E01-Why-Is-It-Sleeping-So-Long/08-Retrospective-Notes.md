---
depends_on:
- 03-Story-Blueprint.md
- 05-Panel-Breakdown.md
- 06-Visual-Prompts.md
document: Retrospective Notes
episode: 01
last_update: 2026-08-10
season: 00
status: FIRST DEFINITIVE CUT APPROVED
title: S00E01 --- Why Is It Sleeping So Long?
universe: Lawn With Care Universe
version: 1.0.0
---

# S00E01 --- Why Is It Sleeping So Long?

## 08 --- Retrospective Notes

## Purpose

`03-Story-Blueprint.md` v1.0 ("Pilot Experiment Notes") asked explicitly: if Panel 06 becomes overloaded with dialogue, document that finding for the Season 00 retrospective before the six-panel carousel format is locked for future episodes. This document is that retrospective, started while S00E01 was still in production so findings weren't lost before final review.

This is a living document. Update it as each open question below gets resolved, then change status from `IN PROGRESS` to `COMPLETE` before starting S00E02.

---

## Resolution (2026-08-10) --- Six Panels → Eight Panels

Before Test 05 could be confirmed against real lettered artwork, production direction moved to expand the format from six to eight panels and lock dialogue at script stage. This is a direct, if earlier-than-planned, answer to the open question this document was tracking: **the old Panel 06 was overloaded** (three lines of dialogue plus a closing caption on top of carrying the science explanation), and the fix applied is exactly what the "Preliminary Recommendation" below already anticipated --- **split the beat across an extra panel rather than shrinking typography.**

Concretely: old Panel 06 (UNDERSTAND + CARE + CLOSE) is now two panels --- new P07 (UNDERSTAND, 3 lines) and new P08 (CARE + CLOSE, 2 lines + caption) --- and a new dedicated environment-establishing panel (new P01) was added at the open. See `03-Story-Blueprint.md` v2.0 for the full architecture and its "Artwork Migration Note," and `06-Visual-Prompts.md` v2.0 for the companion change: dialogue is now included in every panel's first-draft prompt instead of added in a separate lettering pass.

This supersedes the "Too early to conclude" verdict below for the *structural* question (whether to split). It does **not** yet resolve Test 05 itself --- that still needs confirmation against real eight-panel draft artwork, which does not exist yet. The six-panel findings below are kept as historical record, not deleted, since they're still valid evidence about what worked in the original structure.

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

## Six-Panel Format --- Preliminary Recommendation (superseded, kept for record)

*Original note, 2026-08-10, superseded same day by the Resolution above:* "Too early to conclude. Hold the format decision for S00E02 until Test 05 and Test 07 above have real data (post-lettering). If P06 turns out to require shrinking the three-line exchange plus caption to fit, that is itself the signal the Story Blueprint asked to watch for — the fix should be splitting the beat across an extra panel, not shrinking typography." Production direction acted on this reasoning ahead of having the post-lettering data, based on inspection of the dialogue load alone. Test 05 still needs real confirmation against the new eight-panel drafts.

---

## Draft Round 1 Review --- Eight-Panel Set (2026-08-10)

The eight-panel draft set (`Assets/Drafts/S00E01-P01` through `P08`,
plus `S00E01-Environment-Shrub-Reference-v3.0.png`) was generated via
Codex's native image tool (Gemini path unavailable --- no active
subscription) per `09-Codex-Draft-Generation.md`. This closes part of
Test 01 (continuity held up well) and Test 05/06 below, and opens
four new findings that block moving anything to `Assets/Final/`.

**This resolves Test 05 (Mobile Dialogue):** dialogue fit and
attribution are excellent in all 8 panels --- crisp, correctly
positioned, matches `04-Script.md` exactly, and P08's closing caption
reads as visually distinct from character dialogue (banner
treatment). No panel needed shrinking. Mark Test 05 **CLOSED ---
PASS**.

**Test 02 (Character Consistency) update:** face/proportion/scale
consistency across independent generations is strong --- the best
result yet in this production. However, it surfaces a **new**
finding, more serious than the earlier hair/hat one:

### Finding A --- Invented Lawn With Care logo / Yard Ranger badge (CRITICAL)

Every prompt in `09-Codex-Draft-Generation.md` explicitly says "Do
not render the Lawn With Care logo anywhere in this image." The model
rendered one anyway on Brooks in P02, P03, P04, P05, P06 and P08: a
square "L" icon on his hat and chest, a "YARD" shield with a maple
leaf on his sleeve, and in P06/P08 a "BROOKS" name tag. None of this
is official artwork --- it's an AI invention, exactly the "Logo
Drift / Badge Drift" failure mode `Brooks-Visual-Canon-Audit-v1.0.md`
already warned about, and the maple-leaf chest pin specifically is
already on record there as `NOT CANON`. **P07 is the one panel where
Brooks has no visible branding at all** --- so the instruction *can*
be followed, just not reliably, which also makes this a wardrobe
continuity problem (P07 doesn't match P02--P06/P08). Logged in full
in `Assets/References/Audits/Brooks-Visual-Canon-Audit-v1.0.md`.

### Finding B --- Art style seam between P01 and P02--P08

The environment reference and P01 render in a painterly, textured,
no-outline storybook style. From P02 onward (once characters appear)
the style shifts to bold-outline, flat-cel cartoon rendering. The
shift is consistent *within* P02--P08, so the fix is to bring P01 (and
the environment reference) in line with the P02--P08 house style
(recommended, since 7 of 8 panels already agree) rather than the
reverse.

### Finding C --- P05 Discovery Frame foliage reads as insect-damaged

The close-up inset in P05 shows broad leaf shapes with small holes
that look like insect feeding damage, inconsistent with the
scale/needle foliage used everywhere else and in direct conflict with
`02-Learning-Objective.md`'s "Scientific Accuracy Gate for Artwork" ---
"no obvious disease or animal damage that would create a competing
explanation." Needs regeneration with foliage texture matching the
rest of the shrub and no perforations.

### Finding D --- Color palette reads autumnal, not spring; low clarity

Owner feedback (2026-08-10): the whole set leans warm gold/brown/amber
--- closer to a fall palette than "early spring, cool, awakening" as
specified in every panel's Environment Lock, and the images feel low
on clarity/brightness generally. This affects all 9 images (reference
+ 8 panels), since the environment reference anchors the palette for
every panel that follows it. Needs a corrected color/lighting
direction: crisper sky blue, fresher green, cooler clear daylight,
higher overall clarity, with the shrub's brown/tan damage kept as a
deliberate, isolated contrast rather than the ambient tone of the
whole scene.

**Verdict:** do not promote any Round 1 file to `Assets/Final/`. A
Round 2 corrective pass is needed, addressing Findings A--D together
(regenerating the environment reference first, since B and D both
trace back to it, then all 8 panels against the corrected reference
and corrected prompts). See `09-Codex-Draft-Generation.md` v2.0 for
the Round 2 brief.

---

## Draft Round 2 Review --- Corrective Pass (2026-08-10)

`S00E01-Environment-Shrub-Reference-v4.0.png` and all 8 panels were
regenerated per `09-Codex-Draft-Generation.md` v2.0.

-   **Finding A (logo/badge) --- RESOLVED.** Zero instances of the
    invented logo, badge, or name tag across all 8 panels, including
    P07 (which was already clean in Round 1 and stayed clean here ---
    consistency achieved).
-   **Finding B (style seam) --- PARTIALLY RESOLVED.** Color/light now
    matches across the whole set. P01 and the v4.0 environment
    reference still render slightly softer/more painterly (less
    defined outline work) than the crisper cartoon-outline technique
    used consistently in P02--P08. Closer than Round 1, but a
    side-by-side scroll would still show the seam. Low priority --- not
    blocking.
-   **Finding C (P05 insect-hole leaves) --- RESOLVED.** The Discovery
    Frame inset now shows clean scale/needle foliage with no
    perforations.
-   **Finding D (autumnal palette / low clarity) --- RESOLVED.** Bright
    blue sky, fresh green lawn, and clear daylight across the whole
    set; the shrub's brown/tan damage now reads as a deliberate,
    isolated contrast rather than the scene's overall tone.
-   The inconsistent P05 bubble style from Round 1 is also gone ---
    every panel now uses the same tailed speech-bubble style, and
    P08's caption remains a distinct banner treatment.

### Finding E --- P04 renders speaker names inline in the dialogue text (new)

P04's two bubbles read "Brooks: Maybe. But let's not guess yet. What
do you notice?" and "Sprout: The outside looks brown and dry." ---
the speaker name is baked into the rendered text itself. No other
panel in either round does this; bubble position/tail already
identifies the speaker per `06-Visual-Prompts.md`'s bubble-planning
notes. Composition, poses, and everything else in P04 are strong ---
this reads as an isolated text-rendering slip, not a reason to
regenerate the whole panel.

**Verdict:** 7 of 8 panels (P01--P03, P05--P08) plus the environment
reference are in good shape --- Findings A, C, D resolved, B
downgraded to low-priority polish. Only **P04** needs another pass,
targeted specifically at Finding E. See
`09-Codex-Draft-Generation.md` v2.1 for the targeted Round 3 brief
(P04 only).

---

## Draft Round 3 Review --- P04 Targeted Fix (2026-08-10)

P04 was regenerated per `09-Codex-Draft-Generation.md` v2.1. Finding
E (speaker-name prefix inside the bubble text) is **RESOLVED** ---
both bubbles now contain only the spoken line.

**However, the logo/badge from Finding A reappeared on Brooks in this
regenerated P04**, even though the same "completely plain, no
branding" instruction that worked in Round 2 was used again. This
inconsistency prompted a root-cause investigation (owner question:
"precisa mudar algo nas referências do projeto?").

**Root cause found:** `Brooks-Master-Model-Sheet-v1.0.png` --- the
reference image supplied via `-r` in every single panel prompt ---
itself shows the Lawn With Care `[L]` icon and the Yard Ranger Canada
badge prominently, across all 5 views. The text instruction ("no
branding") and the reference image (badges everywhere) directly
conflict on every generation call; which one "wins" is inconsistent
rather than a true fix. Full reasoning and resolution path logged in
`Assets/References/Audits/Brooks-Visual-Canon-Audit-v1.0.md` under
Finding A.

**Resolution path chosen:** generate a supplementary unbranded
reference variant (`Brooks-Unbranded-Story-Reference-v1.0.png`) for
use in place of the Master Model Sheet specifically when a story
calls for no visible branding --- matching `14-Canon.md`'s own
allowance for an "approved story-specific wardrobe" exception. This
removes the conflict at its source instead of relying on text
instructions to overpower a contradicting reference image on every
call. See `09-Codex-Draft-Generation.md` v2.2 for the brief:
generating the new reference, then regenerating P02--P08 against it
for full consistency (not just P04 again).

---

## Next Steps

1. ~~Generate the eight-panel draft set~~ --- done, see Draft Round 1
   Review above.
2. ~~Evaluate Test 05~~ --- done, **PASS**.
3. ~~Run the Round 2 corrective pass~~ --- done, see Draft Round 2
   Review above. Findings A, C, D resolved.
4. Run the Round 3 targeted fix for P04 only (Finding E) ---
   `09-Codex-Draft-Generation.md` v2.1.
5. Optional polish: bring P01 / the environment reference fully in
   line with the P02--P08 outline style (Finding B) --- not blocking,
   revisit if there's time before final export.
6. Resolve the original Brooks hair/hat discrepancy (Test 02, first
   finding) --- re-check against the Round 2/3 art; not observed as a
   problem in this pass but wasn't specifically targeted either.
7. Fill in Test 07 regeneration reasons for the eight-panel set as
   they occur, rather than retroactively.
8. Flip status to `COMPLETE` and fold the verdict into
   `PROJECT_STATUS.md` before starting S00E02.

---

## Correction (2026-08-10) --- Round 4's Direction Was Wrong

Round 4 above proposed generating an unbranded Brooks reference,
assuming the episode should hide his marks. The project owner
corrected this: Brooks should show his canon marks, accurately --- the
issue was never "too much branding," it was "the branding is an AI
guess instead of the real artwork." Investigated further and found:
the Lawn With Care `[L]` icon has a real official asset
(`00-Franchise/Brand/Logos/04-icon-dark.png`) that no prompt had ever
referenced directly; the Yard Ranger Canada sleeve badge has **no**
official asset anywhere in the repo, which is a genuine canon gap, not
a generation bug. Full corrected plan --- referencing the real icon
file for better draft fidelity, plus a new `composite_logo.py` tool
for pixel-exact final compositing --- is in
`09-Codex-Draft-Generation.md` v2.3 ("ROUND 5"). See
`Assets/References/Audits/Brooks-Visual-Canon-Audit-v1.0.md`, Finding
A, for the full corrected diagnosis. Round 4's unbranded reference
should not be generated or used.

---

## Draft Round 6 Review --- Resolved (2026-08-10)

Round 5's plan (above) was itself overcomplicated. The owner clarified
the real goal: Brooks should simply match
`Brooks-Master-Model-Sheet-v1.0.png` faithfully --- marks included ---
using it as the *only* Brooks reference. The intermediate attempt
(Round 5, reusing Round 4's leftover unbranded reference alongside the
official icon file) produced panels with no marks at all, because a
blank-hat reference image overpowers any text instruction --- same
lesson as the original root cause, just re-triggered. That file
(`Brooks-Unbranded-Story-Reference-v1.0.png`) has been deleted.

P02--P08 were regenerated per `09-Codex-Draft-Generation.md` v2.4
("ROUND 6"), using only the Master Model Sheet as the Brooks
reference and an instruction to match it faithfully rather than omit
or correct anything. **Result: consistent across all 7 panels** ---
`[L]` icon on hat and chest, Yard Ranger badge on the sleeve, in every
one of them. **Finding A is closed.** Only residual item: P03's sleeve
badge text rendered garbled/illegible --- a one-panel text-rendering
slip, optional cleanup, not blocking.

**Lesson for future episodes:** when a reference image and a text
instruction disagree, the reference wins, unreliably. Don't fight a
reference with contradicting text --- pick the reference that already
shows what you want and describe it as "match this faithfully," which
is exactly what finally worked here after several rounds of the
opposite approach.

---

## Pipeline Audit and Overhaul (2026-08-10)

With the Round 6 fix working, the owner asked for a critical review of
the whole image-generation pipeline to reduce rework on future
episodes. An audit (run via Codex, ~10 minutes, no files changed
during the audit itself) found the rework across Rounds 1--6 wasn't
caused by under-detailed prompts --- it was caused by three structural
problems:

1. **No single resolved prompt per panel.** `09-Codex-Draft-Generation.md`
   had accumulated six rounds of patches; the "correct" instruction
   lived in a note at the top while the actual executable prompt
   blocks below it still contained the superseded "completely plain,
   no branding" language from Rounds 2--5 (confirmed: 11+ occurrences
   found via `grep` after the audit). Two people running "the same"
   document could get opposite results depending which block they
   copied.
2. **Reference images with competing or ambiguous roles.** Verified
   directly: `Sprout-Master-Model-Sheet-v1.0.png` contains a second
   depiction of Brooks and annotates Sprout at a non-canonical 112 cm
   (operational canon is 130--135 cm). `Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png`
   contains roughly 15 independently-generated Brooks/Sprout
   vignettes --- each one a separate opportunity for drift --- despite
   being treated as one reference. Any generation call that included
   these alongside the Master Model Sheets was effectively showing the
   model multiple different "Brooks" and "Sprout" references at once.
3. **No reproducible process.** Attempts overwrote each other in
   place with no record of what prompt or reference set produced a
   given result, no preflight check for known failure language, and no
   automated technical QA before human review.

**Fixes applied:**

- `09-Codex-Draft-Generation.md` rewritten from scratch as v3.0: one
  fully-resolved prompt per panel, built from named locked blocks
  (`BROOKS_LOCK`, `SPROUT_LOCK`, `RELATIONSHIP_LOCK`, etc.) defined
  once and never duplicated with drift. All six rounds of prior patch
  history removed from the file (still available in git history and
  in this document).
- `06-Visual-Prompts.md`'s "Logo and Brand Lock" rewritten to declare
  two explicit modes --- `DRAFT_MATCH_MASTER` (reproduce the Master
  Model Sheet faithfully, marks included --- active for S00E01) and
  `FINAL_BRAND_EXACT` (reserve the area, composite the real asset) ---
  so the branding question can't silently flip again.
- `Relationship-Canon.md` updated: the Relationship Scale Sheet is now
  documented as QA/staging reference only, never a generation input.
- Sprout's 112 cm / embedded-Brooks defect logged in
  `01-Characters/Sprout/14-Canon.md` ("Known Reference Asset Issue")
  rather than silently corrected --- it's an approved asset, so fixing
  it is the owner's call.
- P04's script had a dangling reference ("Maybe. But let's not guess
  yet." with nothing in P03 for "Maybe" to answer, introduced when the
  six-panel structure split into eight) --- fixed in `04-Script.md`,
  `03-Story-Blueprint.md`, and `05-Panel-Breakdown.md`.
- Two new tools in `05-AI/Scripts/`: `preflight_check.py` (catches
  stale branding language, competing character references, and
  accidental output overwrite before a generation call runs ---
  verified against both the exact failure patterns from this episode)
  and `crop_image.py` (produces single-purpose operational crops from
  multi-figure contact sheets, for future use per the "Future
  Optimization" list in `09-Codex-Draft-Generation.md`).

**Not yet done** (logged as P1/P2 in the audit, tracked in
`09-Codex-Draft-Generation.md`'s "Future Optimization" section):
operational environment-reference crops, deterministic (non-generative)
lettering, a generation manifest with reference-file hashes, automated
technical QA (dimensions/format/naming), and immutable per-attempt
file naming instead of in-place overwrite.

**Governing lesson, worth carrying into every future episode:** when a
reference image and a text instruction disagree, the reference wins,
unreliably. Don't fight a reference with contradicting text --- pick
or build a reference that already shows what you want, and describe
it as "match this faithfully."

---

## First Definitive Cut Approved (2026-08-10)

Owner reviewed the corrected 8-panel set and approved it as S00E01's
first definitive story. All 8 panels promoted from `Assets/Drafts/`
to `Assets/Final/S00E01-P01.png` through `S00E01-P08.png`. Tagged in
git as a production milestone (see repository tags).

Known open item, explicitly accepted as non-blocking: P03's sleeve
badge text renders slightly illegibly. Everything else --- character
consistency, dialogue accuracy, spring color palette, scientific
accuracy of the shrub, Brooks' marks matching his Master Model Sheet
--- passed review across all 8 panels.

**Not yet done, deliberately deferred past this milestone:** social
export/cropping for the actual Instagram post, and the "Future
Optimization" list in `09-Codex-Draft-Generation.md` (operational
reference crops, deterministic lettering, generation manifest,
automated technical QA, immutable attempt naming). None of these
block calling this set the episode's first definitive cut --- they
improve the *next* episode's production speed.

---

## Addendum (2026-08-11) --- Reference Authority Hierarchy

Found during S00E02 production (`03-Codex-Draft-Generation-Brief.md`, P02), while chasing a recurring Brooks insignia problem (tie invented, freckles bled over from Sprout, maple-leaf badge duplicated onto the chest). Recorded here because it is a structural rule for every future episode's reference/prompt setup, not just this one panel.

**Finding:** the strongest results came from giving each reference image one job instead of asking it to prove everything at once:

- `*-Master-Model-Sheet-v1.0.png` --- governs character identity: face, proportions, silhouette, wardrobe, and *placement* of marks (which panel of the uniform they sit on).
- `00-Franchise/Brand/Logos/04-icon-dark.png` (or `05-icon-light.png`) --- governs the official `[L]` icon's *exact geometry* only (open-top frame, single two-lobed leaf, serif letter), which the Master Model Sheet itself only approximates.
- Prompt text --- governs pose, composition, and narrative only. It should not try to carry the full visual definition of a brand mark in words.

This is a refinement of, not a reversal of, the S00E01 finding under "Reference Roles" below (Test 07): giving the model two *competing* full references for the same character caused drift; giving it two references that each own a clearly different, non-overlapping aspect of the same character did not.

**Wording fix that made this reliable:** earlier prompts (S00E01 and early S00E02 drafts) wrote the icon as literal `[L]` in the generation prompt text. Square brackets around a letter read to the model as a literal design instruction rather than shorthand for the approved icon asset, which is the likely root cause of the "Logo drift" failure mode tracked in `Brooks-Visual-Canon-Audit-v1.0.md`. `[L]` remains fine as informal shorthand in conversation and internal documentation, but generation-prompt text must spell out "the official Lawn With Care icon" and describe its actual construction instead.

**Operational caveat (do not skip this when generating by hand in a chat UI):** naming a reference file's path in the prompt text does not cause an image generator to see that file. This repository's scripted pipeline (`05-AI/Scripts/generate_image.py` / `preflight_check.py --ref ...`) already attaches reference images as real inputs to the generation call, so this has never been a problem there. It only matters when a human is pasting a prompt directly into a chat UI (e.g. ChatGPT web) instead of running the script --- in that case, every reference this section lists (Master Model Sheet(s), environment reference, and now optionally the brand icon file) must be physically attached/uploaded to that generation turn every time. Mentioning the path in words is silently ignored, not enforced.

**Superseded (2026-08-11, S00E03):** the two-reference pattern above worked once (S00E02 P02.1) but the project owner reconfirmed on S00E03 P03 that it is not the standing rule --- the Master Model Sheet alone remains the default single Brooks reference, matching this document's own "Draft Round 4/5" and "Final resolution" findings further up. When the icon drifts, fix it by strengthening the prompt's text description first, not by adding the brand-asset file back in. See `01-Characters/Brooks/Assets/References/Audits/Brooks-Visual-Canon-Audit-v1.0.md`, "Standing Rule Reconfirmed."

See `13-Episodes/Season-00-Pilots/S00E02-Why-Does-the-Ground-Need-to-Breathe/03-Codex-Draft-Generation-Brief.md` ("REFERENCE_ROLES", "BROOKS_LOCK") for this pattern applied, and `01-Characters/Brooks/11-Negative-Prompt.md` for the character-side failure-mode entry.

---

## Addendum (2026-08-11) --- Crop Before Approving, and Two Other S00E02 Production Lessons

Found across full S00E02 production (all 8 panels). Recorded here, not just in S00E02's own documents, because all three apply to every future episode's review pass, not just this one.

**1. Full-panel viewing at normal size misses real defects that a close crop catches.** Two genuine bugs in S00E02 were invisible on first look at the full 4:5 panel and only became clear after cropping the specific region with `05-AI/Scripts/crop_image.py`: a third arm/extra hand on Sprout (holding the magnifying loupe while both her actual hands were already occupied), and faint freckles on Brooks' face. Going forward, treat cropping Brooks' face and both characters' hands as a required step of the review pass, not something to reach for only when a problem is already suspected.

**2. A wording fix that works most of the time is not a wording fix that always works.** The "no freckles" instruction for Brooks held clean for 5 consecutive panels, then failed twice in a row even with progressively stronger wording, then held clean again with no wording change from the failed attempts. Treat this kind of fix as reducing failure rate, not eliminating it --- keep reviewing every panel rather than trusting a prompt-language fix to be permanent once it's worked a few times. See `01-Characters/Brooks/Assets/References/Audits/Brooks-Visual-Canon-Audit-v1.0.md` ("Freckles on Brooks Are Intermittent, Not Solved") for the full record.

**3. When generating by hand in a long chat session, verify the saved filename matches the panel actually shown.** Several S00E02 panels came back saved one panel number ahead of what was actually pictured (e.g. a P06 regeneration saved as `P07.1.png`), apparently from the chat session's own turn-counting rather than the episode's panel numbering. The image content was correct each time; only the filename drifted. Check the picture against the panel brief before trusting the filename, especially several regenerations into a single panel.

---

Status: **FIRST DEFINITIVE CUT APPROVED --- v1.0 (all 8 panels promoted to Assets/Final/; pipeline overhaul complete; remaining items are deferred polish/tooling, not blockers)**
