---
depends_on:
- 03-Story-Blueprint.md
- 04-Script.md
- 05-Panel-Breakdown.md
- 06-Visual-Prompts.md
- 08-Retrospective-Notes.md
document: Codex Draft Generation Brief
episode: 01
last_update: 2026-08-10
season: 00
status: READY FOR EXECUTION
supersedes: 09-Codex-Draft-Generation.md v2.3 (Round 5, official-icon-compositing approach -- overcomplicated, see Round 6)
title: S00E01 --- Why Is It Sleeping So Long?
universe: Lawn With Care Universe
version: 2.4.0
---

# S00E01 --- Why Is It Sleeping So Long?

## ROUND 6 --- Simplify: Just Match the Master Model Sheet (2026-08-10)

Round 5 overcomplicated this. The actual ask is simple: **Brooks
should look like `Brooks-Master-Model-Sheet-v1.0.png` --- all its
approved characteristics, including the hat icon, chest icon, and
sleeve badge as shown there.** Stop trying to omit, simplify, or
"correct" those marks against a separate official brand file --- that
was solving a problem the owner didn't have. Matching the Master
Model Sheet faithfully *is* the goal.

**What went wrong operationally:** Round 5's regeneration used
`Brooks-Unbranded-Story-Reference-v1.0.png` (Round 4's blank-hat
asset) as one of the Brooks `-r` references, alongside the new
official icon file. A reference image with a completely blank hat and
jacket overpowers any text instruction, so the result came out with
no marks at all --- worse than any previous round.

**That file has been deleted.** Do not generate or use any
"unbranded"/"story reference" variant of Brooks going forward. There
is exactly one approved Brooks reference for wardrobe/branding
purposes: `Brooks-Master-Model-Sheet-v1.0.png`.

### Regenerate P02--P08

Use each panel's Round 2 prompt (P04 keeps Round 3's "no speaker
label in the bubble" fix) with this one change --- replace whatever
"plain hat/chest, no branding" language is currently in the prompt
with:

```
Brooks' campaign hat, left chest, and left sleeve show the Lawn With Care [L] icon and Yard Ranger Canada badge exactly as they appear on the supplied Brooks Master Model Sheet reference -- match that reference faithfully, do not omit, simplify, or alter these elements.
```

Brooks reference flags for every panel that includes him: **only**

```bash
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png"
```

Do not add the `00-Franchise/Brand/Logos/04-icon-dark.png` file or
any other Brooks-related reference alongside it --- one clear,
approved reference, matched faithfully, is more reliable than
multiple references arguing with each other, which is what caused
every inconsistency so far across Rounds 1--5.

(Separately, and not urgent: the exact pixel-perfect official `[L]`
artwork vs. the Master Model Sheet's own approximation of it, and the
fact that the Yard Ranger badge has no standalone official asset, are
still true --- see the Visual Canon Audit if that distinction ever
matters for a different production need. It doesn't block this
episode's panels, which just need to match the approved sheet.)

---

## ROUND 5 --- Correction: Brooks Should Carry His Marks, Accurately (2026-08-10)

Round 4 (below) assumed the fix was to remove Brooks' branding from
the reference entirely. **That was the wrong direction.** The project
owner clarified: Brooks should show his canon marks --- the goal is
*accuracy*, not *absence*. Do not generate or use
`Brooks-Unbranded-Story-Reference-v1.0.png` from Round 4. Full
reasoning:
`01-Characters/Brooks/Assets/References/Audits/Brooks-Visual-Canon-Audit-v1.0.md`,
Finding A (corrected).

**What's actually true:**

- The Lawn With Care `[L]` icon **has** an official source asset ---
  `00-Franchise/Brand/Logos/04-icon-dark.png` --- single leaf, open-top
  square frame, specific serif "L". No generation prompt so far has
  referenced this file directly; every draft has been the model's own
  guess from a text description, which is why it's come out close but
  never exact (wrong leaf count, closed frame, wrong lettering).
- The Yard Ranger Canada badge (maple leaf, sleeve) has **no official
  asset anywhere in the repo** --- only a text description. There is
  nothing exact to copy. This is a real canon gap, not a generation
  bug, and needs an owner decision (see below) before it can be
  "fixed" in any strict sense.

**Two-part corrected fix:**

### Part 1 --- Better draft fidelity for the `[L]` icon

Add the official icon as a direct reference image, so the model has
real artwork to approximate instead of a text description alone. For
any panel showing Brooks' hat or chest clearly, add this flag:

```bash
-r "00-Franchise/Brand/Logos/04-icon-dark.png"
```

And replace the old "hat front and left chest completely plain..."
language in each prompt with:

```
Brooks' campaign hat and left chest each carry the Lawn With Care [L] icon exactly as shown in the supplied official icon reference: one leaf shape above an open-top square frame with a serif "L" inside. Match that reference's proportions and geometry as closely as possible -- do not invent a different frame shape, leaf count, or lettering style. Leave his right sleeve/shoulder area plain for now (no Yard Ranger badge yet -- that asset doesn't exist officially and is being decided separately).
```

This will not be pixel-perfect (no AI generation is, which is why the
Brand README says AI reproductions are never authoritative) but
should track the real design much more closely than freehand
guessing did across every round so far.

### Part 2 --- Pixel-exact fix for anything promoted toward Final

New tool: `05-AI/Scripts/composite_logo.py`. For a panel where the
`[L]` icon needs to be exactly correct (not just close), generate the
panel with that area left plain (or accept Part 1's approximation),
then stamp the real asset on top:

```bash
python3 05-AI/Scripts/composite_logo.py \
  "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P0X-Draft.png" \
  "00-Franchise/Brand/Logos/04-icon-dark.png" \
  -o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P0X-Draft.png" \
  -x <left-pixel> -y <top-pixel> -w <width-pixel>
```

`-x/-y/-w` must be read off the actual generated image (open it, find
where the hat/chest icon area sits, in pixels, on the 1080×1350
canvas) --- there's no auto-detection, since a wrong guess would be
worse than the current approximation. Do this per panel, since
Brooks' position/scale differs panel to panel.

### The Yard Ranger badge decision (owner input needed)

No official asset exists to composite. Options, in order of recommended preference:

1. **Commission/approve an official badge asset now** (a real
   creative decision, out of scope for an AI agent to make silently)
   --- then treat it exactly like the `[L]` icon above.
2. **Leave the badge off entirely** until an asset exists --- cleanest
   short-term choice, avoids repeating an unresolvable drift issue on
   every panel.
3. **Accept the AI's approximation for now**, explicitly logged as
   `NON-CANON / PROPOSED` per `14-Canon.md`'s Badge Rule, understanding
   it cannot be corrected until Option 1 happens.

This brief defaults to **Option 2** for the prompt text above (badge
area left plain) until the owner picks 1 or 3.

---

## ROUND 4 --- Fix the Reference, Not Just the Prompt (2026-08-10, SUPERSEDED --- wrong direction, see Round 5 above)

Round 3 fixed P04's speaker-prefix bug, but the logo/badge (Finding
A) came back on Brooks in that same regeneration, even with the exact
"completely plain, no branding" instruction that worked in Round 2.
Root cause (full detail in
`01-Characters/Brooks/Assets/References/Audits/Brooks-Visual-Canon-Audit-v1.0.md`,
Finding A):

**`Brooks-Master-Model-Sheet-v1.0.png` --- the reference image every
prompt supplies via `-r` --- itself shows the Lawn With Care `[L]`
icon and the Yard Ranger Canada badge across all 5 views.** That's
correct for the sheet's own job (documenting Brooks' full identity,
badges included --- they're legitimately part of his design per
`06-Wardrobe.md`/`14-Canon.md`). But it directly fights this
episode's separate, deliberate decision (`06-Visual-Prompts.md`,
"Logo and Brand Lock") to keep S00E01's panels unbranded. A text
instruction cannot reliably out-vote a reference image that shows the
opposite thing five times over, which is exactly why results were
inconsistent panel to panel and round to round.

**Fix: stop fighting the reference. Give it one that agrees with the
text instead.**

### Step A --- Generate an unbranded story-panel reference

This new asset does not replace or redesign the Master Model Sheet ---
it's a supplementary reference for the specific, already-documented
case where a story calls for no visible branding (an "approved
story-specific wardrobe" exception per `14-Canon.md`). Anchor it to
the Master Model Sheet for everything except the branding.

```bash
python3 05-AI/Scripts/generate_image.py \
"Create a production reference image of Ranger Brooks for the Lawn With Care Universe, matching the supplied Master Model Sheet exactly in face, proportions, expression, forest-green campaign hat and jacket silhouette, dark outdoor boots, and notebook/pencil -- front view, standing, calm approachable pose, same bright clean-outline flat-cel storybook illustration style.

The ONE difference from the reference: his hat front, left chest, and left sleeve must be completely plain, unmarked forest-green/olive fabric -- no [L] icon, no letter, no emblem, no patch, no shield, no maple leaf, no text, no logo of any kind anywhere on the uniform. Everything else (face, body, proportions, colors, boots, notebook, pencil) must match the supplied reference exactly.

This is a production continuity reference for episodes where branding is intentionally omitted, not a redesign of the character. No text labels, no background clutter -- plain neutral background, single front-view figure." \
-o "01-Characters/Brooks/Assets/References/Brooks-Unbranded-Story-Reference-v1.0.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png"
```

**Review before continuing:** face/proportions/colors still match
Brooks exactly? Hat, chest, and sleeve genuinely blank, not just
faded or hard to see? If not, regenerate Step A before touching any
panel --- every panel below depends on it.

### Step B --- Regenerate P02--P08 against the new reference

Not just P04 this time. Since the root cause was systemic (the same
conflicting reference was used for every Brooks panel), full
reliability means switching all 7 Brooks-containing panels to the new
unbranded reference, not patching the one panel that happened to
expose the problem. P01 doesn't need this (no characters).

For each of P02 through P08: take that panel's exact prompt from
Round 2 (below, or Round 3 for P04's speaker-label fix, which stays
in effect), and replace only the Brooks reference flag:

```diff
- -r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
+ -r "01-Characters/Brooks/Assets/References/Brooks-Unbranded-Story-Reference-v1.0.png" \
```

Keep every other `-r` flag (Sprout sheet, Relationship scale sheet,
environment reference) and the full prompt text unchanged, including
the existing "hat front and left chest completely plain... no name
tag, no shoulder patch" language --- it's correct, it just needed a
reference that doesn't contradict it. For P04 specifically, use
Round 3's version of the prompt (the one with the "no speaker label
inside the bubble" instruction) with this same reference swap.

If this round is reliable, every one of P02--P08 should come out
branding-free without needing a second attempt --- that consistency
(not just "no badge on any single panel") is the actual test of
whether the root cause is fixed.

---

## ROUND 3 --- Targeted Fix (P04 only, 2026-08-10, superseded by Round 4 above for the badge issue --- kept for its correct speaker-label fix)

Round 2 (below) resolved Findings A, C, D and left only one new,
isolated issue: **P04's dialogue bubbles render the speaker's name
inline as part of the text** --- "Brooks: Maybe. But let's not guess
yet. What do you notice?" and "Sprout: The outside looks brown and
dry." --- instead of just the line itself, which is how every other
panel in both rounds correctly did it. See
`08-Retrospective-Notes.md`, "Draft Round 2 Review," Finding E.

Composition, poses, color, and the "no logo" fix all held up
correctly in P04 --- **only regenerate P04**, nothing else. Use the
exact same prompt as Round 2's Step 4 below, with one addition: an
explicit instruction that the bubbles must contain only the spoken
line, no speaker label.

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, continuing directly from the previous panel with exact continuity: same shrub, same damage pattern, same lighting and wardrobe. Bright, clean-outline, flat-to-soft-cel storybook style, matching the rest of the set. No photorealism, no anime, no manga, no generic 3D redesign.

COLOR AND LIGHT: crisp blue sky, clear cool high-clarity daylight, not golden or hazy.

Characters, matched exactly to the supplied reference sheets:

RANGER BROOKS -- adult male naturalist mentor, bald under his hat, no beard, forest-green ranger uniform, campaign hat, dark outdoor boots, notebook and pencil, approximately 188 cm tall. Hat front and left chest completely plain forest-green fabric -- no icon, letter, emblem, patch, or text, no name tag, no shoulder patch.

SPROUT -- curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe, approximately 130-135 cm tall.

Use an intimate medium two-shot beside the shrub. Brooks is crouched or kneeling naturally beside Sprout so that he is near her conversational eye level -- his greater height should still read believably through his proportions even while lowered. He has a calm, open, encouraging expression; his notebook may rest in one hand (if it shows any writing, keep it to simple, plain doodles or lines, not invented logos or slogans); if he gestures, it refers generally to the plant and never points directly at any specific bud. Sprout is focused and thoughtful, comparing parts of the shrub, her loupe ready in her hand, attention moving between Brooks and the plant. The composition should visually communicate shared investigation, not a lecture. Keep the brown/tan exposed foliage visible, scale/needle texture, no holes.

Reserve two separated clean dialogue areas in the upper composition: a larger one near Brooks for two lines, a smaller one near Sprout for her shorter response. Render exactly, attributed correctly by bubble position and tail ONLY -- the bubble text itself must contain ONLY the spoken line, with NO speaker name, NO colon, and NO label of any kind inside the bubble: Brooks: \"Maybe. But let's not guess yet. What do you notice?\" and Sprout: \"The outside looks brown and dry.\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: rendering any speaker name, label, or colon inside a speech bubble -- bubbles must contain the spoken line only, Brooks standing over Sprout, a lecture pose, Brooks holding Sprout's loupe, Brooks revealing or pointing at the bud, incorrect relative scale, warm golden/sepia color grading, any branding/logo/patch/name tag on Brooks, garbled or illegible text, bubbles overlapping either character's face." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P04-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v4.0.png"
```

After regenerating, check specifically: do the two bubbles contain
*only* "Maybe. But let's not guess yet. What do you notice?" and "The
outside looks brown and dry." with no "Brooks:" / "Sprout:" prefix
anywhere? If the prefix reappears, the fastest fix is a text-only
correction pass (crop/paint out just the prefix) rather than another
full regeneration, since the rest of the panel is already correct.

Everything below (Round 2, v2.0) is kept as the historical record of
what already succeeded for P01--P03 and P05--P08 --- do not regenerate
those unless something new is found.

---

## 09 --- Codex Draft Generation Brief --- ROUND 2 (Corrective)

## Purpose

Round 1 (`Assets/Drafts/S00E01-P01` through `P08`, plus
`S00E01-Environment-Shrub-Reference-v3.0.png`) produced excellent
character consistency and dialogue rendering, but review in
`08-Retrospective-Notes.md` ("Draft Round 1 Review") found four
findings that block promoting anything to `Assets/Final/`:

-   **Finding A (critical):** an invented Lawn With Care logo /
    Yard Ranger badge / name tag on Brooks in P02, P03, P04, P05, P06,
    P08 --- despite every Round 1 prompt explicitly forbidding it.
-   **Finding B:** an art-style seam --- P01 (and the environment
    reference) render painterly/textured/no-outline, while P02--P08
    render as bold-outline flat-cel cartoon. Standardizing on the
    P02--P08 style (7 of 8 panels already agree).
-   **Finding C:** the P05 Discovery Frame inset shows leaf shapes
    with holes that read as insect damage, contradicting
    `02-Learning-Objective.md`'s "no obvious disease or animal damage
    that would create a competing explanation."
-   **Finding D:** the whole set reads as a warm autumnal palette
    with low clarity, instead of the bright, cool, clear early-spring
    tone specified in every Environment Lock. This traces back to the
    environment reference, which every panel is anchored to.

This document is the Round 2 corrective brief. It **reuses the same
composition, poses, camera, and locked dialogue from Round 1** ---
those were reviewed as strong --- and changes only: art style
consistency, color/lighting direction, the no-logo instruction
(strengthened), and the P05 foliage description.

As with Round 1, every prompt below is **fully self-contained** ---
repeat everything a single generation call needs, since it has no
memory of anything outside itself.

If a prompt here and `06-Visual-Prompts.md` ever disagree on staging,
poses, or dialogue, `06-Visual-Prompts.md` is the authority for those
elements. This document is the authority for the corrective art
direction described above (style, color, logo, foliage) until that
correction is folded back into `06-Visual-Prompts.md` v2.1.

---

## Shared Corrections --- Apply to Every Prompt Below

These four blocks are already written into each step's prompt text.
Listed here once so the reasoning is visible in one place; do not
strip them out when adapting a prompt.

**Style (fixes Finding B):** one consistent bright, clean-outline,
flat-to-soft-cel storybook illustration style for every single image
in the set, including the environment reference --- no painterly,
textured, or outline-free technique anywhere.

**Color / light (fixes Finding D):** crisp blue sky, fresh cool green,
clear high-clarity daylight. Not overcast, hazy, sepia, or golden. The
lawn reads pale green transitioning out of dormancy, not tan/gold
autumn. Only the shrub's damaged foliage carries warm brown/tan/rust
--- everything else stays fresh and cool, so that contrast is
legible instead of the whole image reading as one warm autumnal
scene.

**No logo (fixes Finding A, strengthened from Round 1):** Brooks' hat
front and left chest are completely plain forest-green fabric --- no
icon, letter, emblem, patch, shape, logo, or text anywhere on him,
including no name tag and no shoulder patch.

**Foliage (fixes Finding C):** small, dense, overlapping scale/needle
evergreen texture everywhere on the shrub, healthy or damaged --- never
broad flat leaves, never holes or bite marks. Damage reads only
through color change.

---

## Execution Path

Same as Round 1: **use Codex's own native image-generation tool**
(Gemini API remains unavailable --- no active subscription). See
Round 1's original "Execution Path" reasoning if you need the local
Draw Things fallback (`05-AI/Scripts/generate_image_local.py`);
it's unchanged and not repeated here.

Reference assets (unchanged from Round 1, still required):

-   `01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png`
-   `01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png`
-   `01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png`

Output directory (same as Round 1 --- these files supersede the Round
1 drafts):
`13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/`

**Text is still included in every prompt**, per `06-Visual-Prompts.md`
v2.0's "Text Rule" --- Round 1 proved this works well (Test 05 passed),
so keep doing it exactly the same way.

---

## Step 0 --- Regenerate the Environment / Shrub Reference (v4.0)

Anchor to v3.0 for shrub silhouette and yard layout, but correct
style and color.

```bash
python3 05-AI/Scripts/generate_image.py \
"Create a clean production reference sheet (no characters, no text, no logo) for the environment and mystery plant of the Lawn With Care Universe episode S00E01.

STYLE: a bright, clean-outline, flat-to-soft-cel children's storybook illustration style -- the same technique as the character panels in this series, NOT a painterly or textured technique. No photorealism, no anime, no manga, no generic 3D redesign.

COLOR AND LIGHT: crisp blue sky with soft white clouds, clear high-clarity early-spring daylight, cool and fresh -- not overcast, not hazy, not sepia or golden-toned. The lawn reads pale green transitioning out of dormancy, not tan or gold like autumn.

Show a modest residential backyard in southern Alberta in early spring, caught between winter and spring, matching the layout of the supplied reference image: a simple wooden board fence along at least two visible sides; a stepping-stone path curving diagonally through the yard; a section of house siding visible at one edge. Small, clearly bounded patches of leftover snow only in shaded corners -- never a snow-covered yard. Damp, dark, recently-thawed soil along garden bed edges with a few flattened weathered fall leaves. One or two bare deciduous saplings with faint bud swelling near the fence.

Feature one hardy evergreen shrub, matching the supplied reference image's silhouette and branch structure exactly, positioned along the fence line about a third of the way into the yard. Its foliage --- both damaged and healthy --- must be small, dense, overlapping scale/needle texture (like cedar or juniper), never broad flat leaves, and never showing holes or bite marks. Show localized brown/tan winter-damaged foliage on its more exposed side, and a clearly visible healthier, greener, more sheltered side on the same shrub, so both conditions read together. The damaged foliage's warm brown/tan tone should stand out as the one warm note in an otherwise fresh, cool-toned scene. Include one specific key branch with a small, subtle viable bud.

No characters. No text. No labels. No logo. No magical effects. This is a production continuity reference, not a story panel." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v4.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v3.0.png"
```

**Review before continuing:** bright and clear, not golden/hazy? Same
shrub silhouette as v3.0? Both damaged and healthy shrub sides
visible? Foliage reads as scale/needle texture with no holes? If not,
regenerate Step 0 before touching P01--P08.

Reference variable used below: `$ENV_REF` =
`13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v4.0.png`

---

## Step 1 --- P01: The Yard Wakes Up

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio. Bright, clean-outline, flat-to-soft-cel storybook style -- the same technique used throughout this series, not a painterly or textured technique. No photorealism, no anime, no manga, no generic 3D redesign.

COLOR AND LIGHT: crisp blue sky with soft white clouds, clear high-clarity early-spring daylight, cool and fresh, not overcast/hazy/sepia/golden. The lawn reads pale green transitioning out of dormancy, not a tan/gold autumn field.

A wide, environment-led establishing shot of a modest residential backyard in southern Alberta, caught exactly between winter and spring -- no character focus yet. Simple wooden board fence along at least two visible sides, a stepping-stone path curving diagonally through the space, a section of house siding visible at one edge, matching the supplied environment reference exactly. Include one or two small, clearly bounded patches of leftover snow tucked into shaded corners without making the yard read as snow-covered. Damp, recently-thawed dark soil along garden bed edges with a few flattened weathered fall leaves. One or two bare deciduous saplings with faint bud swelling near the fence. The mystery evergreen shrub (matching the supplied environment reference exactly, including its localized brown/tan winter damage against otherwise scale/needle-textured healthy green foliage) is visible along the fence line, roughly a third of the way into the yard -- readable but not the emphasized subject; keep it modest in the frame, smaller than in the reference sheet's close-up insets.

Do not include Brooks or Sprout in this panel.

Reserve clean negative space in the lower third for a short caption in a simple, friendly hand-lettered banner style: \"Early spring in the yard.\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: a fully green/summer lawn, a snow-covered yard, warm golden/sepia color grading, a painterly or textured rendering technique, the shrub dominating the composition, any character figures, garbled or illegible text." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P01-Draft.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v4.0.png"
```

---

## Step 2 --- P02: Something Is Growing

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, continuing directly from the previous panel: same yard, same early-spring morning, same fence and path, same shrub visible in the background. Bright, clean-outline, flat-to-soft-cel storybook style, matching P01 exactly. No photorealism, no anime, no manga, no generic 3D redesign.

COLOR AND LIGHT: crisp blue sky, clear cool high-clarity daylight, fresh pale-green lawn -- not golden, hazy, or autumnal anywhere in the frame except the shrub's damaged foliage.

Characters, matched exactly to the supplied reference sheets:

RANGER BROOKS -- adult male naturalist mentor, calm warm expression, bald under his hat with no visible hair and no beard, forest-green ranger uniform, campaign hat (forest green with a gold band), dark outdoor boots, may carry a small notebook and pencil, approximately 188 cm tall, rounded approachable proportions. His hat front and left chest are completely plain forest-green fabric -- no icon, letter, emblem, patch, shape, logo, or text anywhere on him, no name tag, no shoulder patch. Never military, tactical, police, cowboy, or superhero styling.

SPROUT -- a curious 9-year-old girl, golden curly blonde hair, light-green eyes, light freckles, green fabric headband, cream short-sleeve field shirt, olive-green shorts, brown outdoor boots, wears her Discovery Band across her chest, carries a magnifying loupe, approximately 130-135 cm tall, energetic natural child body language.

Use a medium composition at a child-friendly eye level, noticeably closer than a wide establishing shot. Sprout is the visual lead, crouched naturally in the foreground, delighted as she closely observes fresh green shoots (or an emerging bulb) pushing up through damp, dark soil near the path. Her loupe is visible but not necessarily in use. Brooks is present farther back or to one side with lower visual emphasis, watching Sprout with a calm, warm expression, notebook optionally in hand -- he is not leading the discovery. Keep the shrub from the environment reference recognizable, softly out of focus, in the background.

Maintain Brooks' and Sprout's canonical relative height.

Reserve clean negative space in the upper-left or upper-center for a speech bubble (same tailed speech-bubble style throughout the set), and render this exact line there, attributed to Sprout: \"Brooks! Look! Everything's waking up!\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: a lush summer lawn, warm golden/sepia color grading, any branding/logo/patch/name tag on Brooks, Brooks pointing out the discovery, Sprout looking older or younger than a 9-year-old, garbled or illegible text, the dialogue text covering Brooks' face." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P02-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v4.0.png"
```

---

## Step 3 --- P03: The Exception

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, continuing directly from the previous panel with exact continuity: same yard, same early-spring day, same lighting, same Brooks and Sprout clothing, same evergreen shrub. Bright, clean-outline, flat-to-soft-cel storybook style, matching the rest of the set. No photorealism, no anime, no manga, no generic 3D redesign.

COLOR AND LIGHT: crisp blue sky, clear cool high-clarity daylight -- not golden or hazy anywhere except the shrub's own damaged foliage.

Characters, matched exactly to the supplied reference sheets:

RANGER BROOKS -- adult male naturalist mentor, bald under his hat, no beard, forest-green ranger uniform, campaign hat, dark outdoor boots, approximately 188 cm tall. Hat front and left chest completely plain forest-green fabric -- no icon, letter, emblem, patch, or text anywhere, no name tag, no shoulder patch.

SPROUT -- curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe, approximately 130-135 cm tall.

Sprout has moved to the evergreen shrub (matching the supplied environment reference exactly: scale/needle foliage texture, no holes or bite marks anywhere). Use a medium shot, closer than the previous panel. The shrub occupies a substantial portion of the composition. Show localized winter-damaged foliage concentrated on the more exposed portion, while preserving recognizable woody structure and less-damaged, greener areas -- concerning but not a completely dead featureless mass. Mulch or bare soil at the shrub's base.

Sprout is closest to the shrub and is the visual focus. Her expression has shifted from delight to puzzled concern. She studies the damaged foliage carefully, leaning or crouching toward it, gently gesturing toward it without touching or breaking anything. Brooks is approaching or standing behind/beside her with secondary visual weight -- he does not point at anything and does not inspect the bud yet.

Maintain Brooks' and Sprout's canonical relative height.

Reserve clean negative space in the upper-right (or another open area opposite Sprout) for a two-line speech bubble, and render this exact text there, attributed to Sprout: \"Except this one... Why is it sleeping so long?\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: a horror-like fully dead plant, disease spots, insect holes or bite marks, animal chewing, a broken trunk, warm golden/sepia color grading, any branding/logo/patch/name tag on Brooks, Brooks already examining the bud, garbled or illegible text." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P03-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v4.0.png"
```

---

## Step 4 --- P04: What Do You Notice?

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, continuing directly from the previous panel with exact continuity: same shrub, same damage pattern, same lighting and wardrobe. Bright, clean-outline, flat-to-soft-cel storybook style, matching the rest of the set. No photorealism, no anime, no manga, no generic 3D redesign.

COLOR AND LIGHT: crisp blue sky, clear cool high-clarity daylight, not golden or hazy.

Characters, matched exactly to the supplied reference sheets:

RANGER BROOKS -- adult male naturalist mentor, bald under his hat, no beard, forest-green ranger uniform, campaign hat, dark outdoor boots, notebook and pencil, approximately 188 cm tall. Hat front and left chest completely plain forest-green fabric -- no icon, letter, emblem, patch, or text, no name tag, no shoulder patch.

SPROUT -- curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe, approximately 130-135 cm tall.

Use an intimate medium two-shot beside the shrub. Brooks is crouched or kneeling naturally beside Sprout so that he is near her conversational eye level -- his greater height should still read believably through his proportions even while lowered. He has a calm, open, encouraging expression; his notebook may rest in one hand (if it shows any writing, keep it to simple, plain doodles or lines, not invented logos or slogans); if he gestures, it refers generally to the plant and never points directly at any specific bud. Sprout is focused and thoughtful, comparing parts of the shrub, her loupe ready in her hand, attention moving between Brooks and the plant. The composition should visually communicate shared investigation, not a lecture. Keep the brown/tan exposed foliage visible, scale/needle texture, no holes.

Reserve two separated clean dialogue areas in the upper composition: a larger one near Brooks for two lines, a smaller one near Sprout for her shorter response. Render exactly, attributed correctly: Brooks: \"Maybe. But let's not guess yet. What do you notice?\" and Sprout: \"The outside looks brown and dry.\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: Brooks standing over Sprout, a lecture pose, Brooks holding Sprout's loupe, Brooks revealing or pointing at the bud, incorrect relative scale, warm golden/sepia color grading, any branding/logo/patch/name tag on Brooks, garbled or illegible text, bubbles overlapping either character's face." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P04-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v4.0.png"
```

---

## Step 5 --- P05: Look Closer

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, continuing with strict continuity from the previous panels -- this is the episode's closest investigation moment. Bright, clean-outline, flat-to-soft-cel storybook style, matching the rest of the set. No photorealism, no anime, no manga, no generic 3D redesign.

COLOR AND LIGHT: crisp, clear, cool daylight, not golden or hazy.

Characters, matched exactly to the supplied reference sheets:

SPROUT -- curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe.

RANGER BROOKS -- adult male naturalist mentor, bald under his hat, no beard, forest-green ranger uniform, campaign hat, dark outdoor boots. Hat front and left chest completely plain forest-green fabric -- no icon, letter, emblem, patch, or text, no name tag, no shoulder patch.

Sprout dominates the composition. She leans naturally toward the same key branch of the evergreen shrub (matching the supplied environment reference) and uses her magnifying loupe to inspect the damaged foliage and nearby buds. Her face shows intense curiosity and concentration, shifting toward the first hint of noticing something unexpected. Brooks remains visible behind or beside her, calm and patient, observing without pointing at the answer. Show the same brown/tan damaged foliage surrounding the key branch.

CRITICAL --- foliage texture: every part of the shrub, in both the main image and the close-up inset, must be small, dense, overlapping scale/needle evergreen texture (like cedar or juniper) -- never broad flat leaf shapes, and never showing holes, bite marks, or perforations of any kind. Damage must read only as a color change from green to brown/tan, never as physical damage to the foliage shape. This is important: previous attempts at this panel produced foliage that looked insect-eaten, which is scientifically wrong for this story.

Include a subtle, organic Discovery Frame -- a soft circular or hand-drawn-style inset, like a magnifying-glass view, not a technological device -- showing an enlarged detail of the branch: intact scale/needle foliage (damaged brown, undamaged green, no holes) around a small, plausible viable bud. No HUD, scanner, hologram, neon interface, or futuristic graphics. The bud should not glow, sparkle, or appear magical.

Use minimal dialogue space; reserve a small clean area for two very short reaction words, in the same tailed speech-bubble style as the rest of the set, and render, attributed to Sprout: \"Hmm... Wait...\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: leaf holes or bite marks anywhere, broad flat leaf shapes, a glowing or oversized bud, futuristic interface elements, an oversized loupe hiding Sprout's face, Brooks pointing out the clue, warm golden/sepia color grading, any branding/logo/patch/name tag on Brooks, shrub continuity drift, garbled or illegible text." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P05-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v4.0.png"
```

---

## Step 6 --- P06: This Bud Is Alive!

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, continuing with strict continuity from the previous panels. Bright, clean-outline, flat-to-soft-cel storybook style, matching the rest of the set. No photorealism, no anime, no manga, no generic 3D redesign.

COLOR AND LIGHT: crisp, clear, cool daylight, not golden or hazy.

Characters, matched exactly to the supplied reference sheets: RANGER BROOKS (adult male naturalist mentor, bald under his hat, no beard, forest-green ranger uniform, campaign hat, dark outdoor boots -- hat front and left chest completely plain forest-green fabric, no icon/letter/emblem/patch/text anywhere, no name tag, no shoulder patch) and SPROUT (curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe).

Use a close-medium discovery/reaction composition beside the same evergreen shrub (scale/needle foliage, no holes anywhere). Sprout has just recognized a small viable bud -- she is delighted and surprised, the genuine expression of a child who found evidence herself. Her loupe remains visible; she may gesture carefully toward the key bud-bearing branch. The viable bud must now be clearly readable while remaining botanically plausible; surrounding brown/tan winter-damaged foliage stays visible for contrast -- do not make the whole branch green. Brooks reacts to Sprout's discovery rather than taking control: he leans in slightly with a warm, proud, encouraging smile, his notebook secondary. Sprout holds the strongest narrative and visual position.

Reserve the dominant clean dialogue area for Sprout and a smaller secondary area for Brooks, in the same tailed speech-bubble style as the rest of the set, and render exactly: Sprout: \"Brooks! This bud is still alive!\" and Brooks: \"Good eye, Sprout.\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: Brooks discovering or pointing out the bud first, the plant appearing healed, an enormous bud, magical glow or sparkles, leaf holes or bite marks, warm golden/sepia color grading, any branding/logo/patch/name tag on Brooks, an exaggerated victory pose, character drift, garbled or illegible text." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P06-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v4.0.png"
```

---

## Step 7 --- P07: Understanding Winter Injury

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio -- the episode's dedicated science-explanation panel, continuing with strict continuity from the previous panels but pulled back to a wider framing than the last two. Bright, clean-outline, flat-to-soft-cel storybook style, matching the rest of the set. No photorealism, no anime, no manga, no generic 3D redesign.

COLOR AND LIGHT: crisp blue sky, clear cool high-clarity daylight, not golden or hazy anywhere except the shrub's own damaged side.

Characters, matched exactly to the supplied reference sheets: RANGER BROOKS (adult male naturalist mentor, bald under his hat, no beard, forest-green ranger uniform, campaign hat, dark outdoor boots, notebook -- hat front and left chest completely plain forest-green fabric, no icon/letter/emblem/patch/text anywhere, no name tag, no shoulder patch -- this must match every other panel in the set exactly, plain in all of them) and SPROUT (curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe).

Use a medium two-shot, positioned so more of the whole evergreen shrub is visible at once than in the previous panel: both the damaged, exposed side established earlier, and a healthier, more sheltered side of the same plant (both in matching scale/needle texture, no holes anywhere). This visual contrast is the point of the panel -- frame the shrub so both conditions read clearly together. Brooks makes a gentle explanatory gesture toward the whole shrub, not just the bud, with a calm, thoughtful expression; his notebook may be open. Sprout remains engaged, looking between Brooks and the plant, not a passive listener. Preserve the same fence, light direction and seasonal cues established since P01; a little more of the yard's depth may show again here.

Reserve generous, clearly separated dialogue-safe space for a three-line exchange, in the same tailed speech-bubble style as the rest of the set, and render: Brooks: \"Winter can dry out exposed parts, even when some of the plant is still alive.\" Sprout: \"So it's not all dead?\" Brooks: \"Not all of it. That's why we look closely.\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: only the damaged side of the shrub being visible, Brooks in a lecture pose, the shrub reading as fully healthy, leaf holes or bite marks, warm golden/sepia color grading, any branding/logo/patch/name tag on Brooks, the three lines crowded into one bubble or overlapping shrub detail." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P07-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v4.0.png"
```

---

## Step 8 --- P08: Look Before You Decide

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio -- the episode's closing panel, continuing with exact continuity from the entire episode, pulled back further than the previous panel toward a medium-wide composition that echoes the opening environment shot without literally repeating it. Bright, clean-outline, flat-to-soft-cel storybook style, matching the rest of the set. No photorealism, no anime, no manga, no generic 3D redesign.

COLOR AND LIGHT: crisp blue sky, clear cool high-clarity daylight, not golden or hazy.

Characters, matched exactly to the supplied reference sheets: RANGER BROOKS (adult male naturalist mentor, bald under his hat, no beard, forest-green ranger uniform, campaign hat, dark outdoor boots -- hat front and left chest completely plain forest-green fabric, no icon/letter/emblem/patch/text anywhere, no name tag, no shoulder patch) and SPROUT (curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe, relaxed in her hand).

Return to a medium-wide composition beside the same evergreen shrub (matching the environment reference, scale/needle foliage, no holes), with enough of the yard visible again -- fence, a hint of the stepping-stone path -- to echo the opening panel. The emotional energy is calmer than the discovery and explanation panels. Brooks remains near Sprout rather than in a dominant standing authority pose, making a gentle gesture toward the shrub with a warm, thoughtful expression. Sprout looks at the plant with new understanding, engaged and active rather than passive. The shrub must still visibly contain the same brown/tan winter-damaged foliage established earlier -- no instant recovery, no pruning happening, no removed shrub.

Reserve generous clean negative space for two short separated dialogue lines plus a closing caption, visually distinct from the character dialogue (same tailed speech-bubble style for dialogue as the rest of the set; the caption as a separate banner/ribbon treatment, as established in this panel already working well). Render: Sprout: \"So we shouldn't give up on it yet.\" Brooks: \"Exactly. Let's watch what grows before we decide what to cut.\" And, as the distinct closing caption: \"LOOK CLOSER BEFORE YOU DECIDE.\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: a suddenly healthy/green shrub, pruning already happening, the plant removed, Brooks lecturing from above, Sprout looking passive, warm golden/sepia color grading, any branding/logo/patch/name tag on Brooks, a location or weather change, the caption styled identically to the character speech bubbles, garbled or illegible text." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P08-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v4.0.png"
```

---

## After Generation --- Review Before Anything Is "Final"

Same checklist as Round 1 (`06-Visual-Prompts.md`, "Visual Approval
Checklist"), plus explicitly re-check Findings A--D:

-   [ ] **Finding A:** zero branding/logo/patch/name-tag on Brooks in
    all 8 panels (not just most of them --- P07 was the one exception
    last time, make sure it's not an exception this time by being the
    only compliant one).
-   [ ] **Finding B:** all 9 images (reference + 8 panels) share one
    consistent illustration style --- no painterly/textured outlier.
-   [ ] **Finding C:** no leaf holes/bite marks anywhere, especially
    inside the P05 Discovery Frame inset.
-   [ ] **Finding D:** the set reads as bright, clear, cool
    early-spring --- not autumnal/golden/hazy.
-   [ ] Everything that passed Round 1 review still holds: dialogue
    accuracy and placement, character/scale consistency, no magical
    plant recovery, P07 shows both shrub sides together.

Report back per panel, same format as Round 1: what passed, what
still needs another pass, and why. Do not move anything to
`Assets/Final/` without this review --- see
`07-Production-Checklist.md`.

---

Status: **READY FOR EXECUTION --- v2.4 (Round 6: match the Master Model Sheet faithfully, single reference, no omission/correction instructions)**
