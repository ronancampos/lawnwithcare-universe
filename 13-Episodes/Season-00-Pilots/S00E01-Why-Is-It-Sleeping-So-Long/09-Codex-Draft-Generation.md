---
depends_on:
- 03-Story-Blueprint.md
- 04-Script.md
- 05-Panel-Breakdown.md
- 06-Visual-Prompts.md
document: Codex Draft Generation Brief
episode: 01
last_update: 2026-08-10
season: 00
status: READY FOR EXECUTION
title: S00E01 --- Why Is It Sleeping So Long?
universe: Lawn With Care Universe
version: 1.0.0
---

# S00E01 --- Why Is It Sleeping So Long?

## 09 --- Codex Draft Generation Brief

## Purpose

This is a self-contained execution brief for an AI coding agent (Codex)
to generate the **eight draft panel images** of the S00E01 pilot
(v2.0, eight-panel revision) and save them to
`Assets/Drafts/`, plus regenerate the environment reference they
depend on.

Unlike `06-Visual-Prompts.md` (the human-readable production
document, which assumes the reader has the whole document's context),
every prompt below is **fully self-contained**: each one repeats every
character/environment/shrub lock it needs, because each generation
call is a single, independent request with no memory of anything
outside it.

Treat this as the working document. If a prompt here and
`06-Visual-Prompts.md` ever disagree, `06-Visual-Prompts.md` is the
authority --- fix this file to match it, not the other way around.

---

## Before Running Anything

1.  Confirm you're on branch `production/v0.2.0` and `git status` is
    clean or has only expected changes.
2.  Confirm `GEMINI_API_KEY` is set (`.env`, not `.env.example`). The
    primary script (`05-AI/Scripts/generate_image.py`) calls Gemini
    2.5 Flash Image ("Nano Banana") and needs it.
3.  Confirm these reference assets exist before starting (all already
    in the repo):
    -   `01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png`
    -   `01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png`
    -   `01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png`
    -   `13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v2.0.png`
4.  Run every command from the repository root.
5.  Output directory for this brief:
    `13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/`
    (create it if missing --- the script does this automatically via
    `-o`).

**No AI-rendered Lawn With Care logo anywhere.** Every prompt below
ends with an explicit instruction not to render it. Do not remove
that line.

**Text is intentionally included in every panel prompt.** Per
`06-Visual-Prompts.md` v2.0's "Text Rule," dialogue is locked and
meant to appear in the first draft. Treat whatever text the model
renders as a placement/legibility check, not guaranteed final
typography --- a correction pass happens later, outside this brief.

---

## Alternative: Local / Free Generation

If no Gemini API key is available, `05-AI/Scripts/generate_image_local.py`
works with a local Draw Things install (Settings → Advanced → API
Server → Server Online, HTTP, port 7859) instead. It only accepts
**one** reference image via `-r` (single img2img anchor, not
multi-reference conditioning), so character consistency will be
weaker than the Gemini path below. If using it:

-   drop the extra `-r` flags in each command below to just one
    (prefer the environment reference for shrub continuity, since
    character drift is easier to spot and re-prompt for than
    environment drift);
-   pass `-n` with the relevant "Avoid" text from each panel below as
    the negative prompt;
-   default output is square (`--width 1024 --height 1024`); override
    to a 4:5-compatible size, e.g. `--width 864 --height 1080`, and
    crop/pad to exactly 1080×1350 in a later step, since this script
    does not produce 1080×1350 directly.

Everything else in this brief assumes the Gemini path.

---

## Step 0 --- Regenerate the Environment / Shrub Reference

The existing `S00E01-Environment-Shrub-Reference-v2.0.png` was built
for the six-panel structure and does not yet show: the fence + path +
leftover-snow layout needed for P01/P08, or the shrub's healthier,
sheltered side needed for P07. Regenerate it as v3.0, anchored to the
old version so the shrub doesn't get reinvented.

```bash
python3 05-AI/Scripts/generate_image.py \
"Create a clean production reference sheet (no characters, no text, no logo) for the environment and mystery plant of the Lawn With Care Universe episode S00E01, in a children's educational illustrated storybook aesthetic -- organic shapes, clean readable silhouettes, flat-to-soft dimensional color, no photorealism, no anime, no manga, no generic 3D animation redesign.

Show a modest residential backyard in southern Alberta in early spring, caught between winter and spring. Include: a simple wooden board fence along at least two visible sides; a stepping-stone path curving diagonally through the yard; a section of house siding visible at one edge. Muted dormant lawn with faint early green re-emerging near the path. Small, clearly bounded patches of leftover snow only in shaded corners -- the north side of the shrub, the base of the fence -- never a snow-covered yard. Damp, dark, recently-thawed soil along garden bed edges with a few flattened weathered fall leaves. One or two bare deciduous saplings with faint bud swelling near the fence. Soft, pale, slightly overcast early-morning sky with thin horizontal cloud bands; a single consistent light direction producing long soft cool shadows.

Feature one hardy evergreen shrub, positioned along the fence line about a third of the way into the yard, as the primary continuity subject. It must keep the same stable, memorable silhouette and woody branch structure as the reference image provided. Show localized brown/tan winter-damaged foliage concentrated on its more exposed side, and -- new for this version -- make sure a healthier, greener, more sheltered side of the same shrub is also clearly visible in frame, so both conditions can be seen together. Include one specific key branch with a small, subtle viable bud that can later be investigated closely. No fungal lesions, insect damage, broken trunk, or dramatic fantasy decay.

No characters. No text. No labels. No logo. No magical effects. This is a production continuity reference, not a story panel." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v3.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v2.0.png"
```

**Review before continuing:** does the shrub silhouette clearly match
v2.0? Is a healthier/sheltered side now visible alongside the damaged
side? Is there a fence + path + at least one leftover-snow patch? If
not, regenerate this step before touching P01--P08 -- every later
panel references this file.

Reference variable used below: `$ENV_REF` =
`13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v3.0.png`

---

## Step 1 --- P01: The Yard Wakes Up

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio. Organic shapes, clean readable silhouettes, flat-to-soft dimensional color, warm nature-focused detail, mobile-first composition. No photorealism, no anime, no manga, no generic 3D animation redesign.

A wide, environment-led establishing shot of a modest residential backyard in southern Alberta, caught exactly between winter and spring -- no character focus yet. Show a simple wooden board fence along at least two visible sides, a stepping-stone path curving diagonally through the space, and a section of house siding visible at one edge. Muted dormant lawn with faint early green beginning to show through near the path. Include one or two small, clearly bounded patches of leftover snow tucked into shaded corners without making the yard read as snow-covered. Damp, recently-thawed dark soil along garden bed edges, with a few flattened weathered fall leaves near the shrub base and fence line. One or two bare deciduous saplings with faint bud swelling near the fence. The mystery evergreen shrub (matching the supplied environment reference exactly, including its localized brown/tan winter damage) is visible along the fence line, roughly a third of the way into the yard -- readable but not yet the emphasized subject. Soft, pale, slightly overcast sky with thin horizontal cloud bands; light from one clear direction producing long, soft, cool shadows consistent with early morning.

Do not include Brooks or Sprout in this panel -- this shot is about the yard itself.

Reserve clean negative space in the lower third for a short caption. If you can render clean legible text, add this caption there in a simple, friendly typeface: \"Early spring in the yard.\" If not, leave that space empty and uncluttered.

Do not render the Lawn With Care logo anywhere in this image.

Avoid: a fully green/summer lawn, a snow-covered yard, the shrub dominating the composition, any character figures, any garbled or illegible text." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P01-Draft.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v3.0.png"
```

---

## Step 2 --- P02: Something Is Growing

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, continuing directly from the previous panel: same yard, same early-spring morning, same fence and path, same shrub visible in the background. Organic shapes, clean readable silhouettes, flat-to-soft dimensional color, no photorealism, no anime, no manga, no generic 3D redesign.

Characters, matched exactly to the supplied reference sheets:

RANGER BROOKS -- adult male naturalist mentor, calm warm expression, bald under his hat with no visible hair and no beard, forest-green ranger uniform, campaign hat (forest green with a gold band), approved chest badge and Yard Ranger Canada shoulder badge, dark outdoor boots, may carry a small notebook and pencil, approximately 188 cm tall, rounded approachable proportions. Never military, tactical, police, cowboy, or superhero styling.

SPROUT -- a curious 9-year-old girl, golden curly blonde hair, light-green eyes, light freckles, green fabric headband, cream short-sleeve field shirt, olive-green shorts, brown outdoor boots, wears her Discovery Band across her chest, carries a magnifying loupe, approximately 130-135 cm tall, energetic natural child body language.

Use a medium composition at a child-friendly eye level, noticeably closer than a wide establishing shot. Sprout is the visual lead, crouched naturally in the foreground, delighted as she closely observes fresh green shoots (or an emerging bulb) pushing up through damp, dark soil near the path. A few flattened fall leaves are visible nearby. Her loupe is visible but not necessarily in use. Brooks is present farther back or to one side with lower visual emphasis, watching Sprout with a calm, warm expression, notebook optionally in hand -- he is not leading the discovery. Keep the shrub from the environment reference recognizable, softly out of focus, in the background.

Maintain Brooks' and Sprout's canonical relative height (Brooks much taller).

Reserve clean negative space in the upper-left or upper-center for a speech bubble, and render this exact line there in a simple, friendly hand-lettered style, attributed to Sprout: \"Brooks! Look! Everything's waking up!\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: a lush summer lawn, giant flowers, Brooks pointing out the discovery, heavy branding, Sprout looking older or younger than a 9-year-old, any garbled or illegible text, the dialogue text covering Brooks' face." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P02-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v3.0.png"
```

---

## Step 3 --- P03: The Exception

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, continuing directly from the previous panel: same yard, same early-spring day, same lighting, same Brooks and Sprout clothing, same evergreen shrub. Organic shapes, clean readable silhouettes, flat-to-soft dimensional color, no photorealism, no anime, no manga, no generic 3D redesign.

Characters, matched exactly to the supplied reference sheets:

RANGER BROOKS -- adult male naturalist mentor, bald under his hat, no beard, forest-green ranger uniform, campaign hat, approved chest and shoulder badges, dark outdoor boots, approximately 188 cm tall.

SPROUT -- curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe, approximately 130-135 cm tall.

Sprout has moved to the evergreen shrub (matching the supplied environment reference exactly, same silhouette and damage pattern). Use a medium shot, closer than the previous panel. The shrub occupies a substantial portion of the composition. Show localized winter-damaged evergreen foliage: believable brown/tan dry-looking foliage concentrated on the more exposed portion of the shrub, while preserving recognizable woody structure and less-damaged areas -- concerning but not a completely dead featureless mass. Mulch or bare soil at the shrub's base.

Sprout is closest to the shrub and is the visual focus. Her expression has shifted from delight to puzzled concern. She studies the damaged foliage carefully, leaning or crouching toward it, gently gesturing toward it without touching or breaking anything. Brooks is approaching or standing behind/beside her with secondary visual weight -- he does not point at anything and does not inspect the bud yet.

Maintain Brooks' and Sprout's canonical relative height.

Reserve clean negative space in the upper-right (or another open area opposite Sprout) for a two-line speech bubble, and render this exact text there, attributed to Sprout: \"Except this one... Why is it sleeping so long?\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: a horror-like fully dead plant, disease spots, insects, animal chewing, a broken trunk or mechanical damage, Brooks already examining the bud, any garbled or illegible text." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P03-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v3.0.png"
```

---

## Step 4 --- P04: What Do You Notice?

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, continuing directly from the previous panel with exact continuity: same shrub, same damage pattern, same lighting and wardrobe. Organic shapes, clean readable silhouettes, flat-to-soft dimensional color, no photorealism, no anime, no manga, no generic 3D redesign.

Characters, matched exactly to the supplied reference sheets:

RANGER BROOKS -- adult male naturalist mentor, bald under his hat, no beard, forest-green ranger uniform, campaign hat, approved chest and shoulder badges, dark outdoor boots, notebook and pencil, approximately 188 cm tall.

SPROUT -- curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe, approximately 130-135 cm tall.

Use an intimate medium two-shot beside the shrub. Brooks is crouched or kneeling naturally beside Sprout so that he is near her conversational eye level -- his greater height should still read believably through his proportions even while lowered. He has a calm, open, encouraging expression; his notebook may rest in one hand; if he gestures, it refers generally to the plant and never points directly at any specific bud. Sprout is focused and thoughtful, comparing parts of the shrub, her loupe ready in her hand, attention moving between Brooks and the plant. The composition should visually communicate shared investigation, not a lecture -- Brooks guides, Sprout investigates. Keep the brown/tan exposed foliage visible.

Reserve two separated clean dialogue areas in the upper composition: a larger one near Brooks for two lines, a smaller one near Sprout for her shorter response. Render exactly, attributed correctly: Brooks: \"Maybe. But let's not guess yet. What do you notice?\" and Sprout: \"The outside looks brown and dry.\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: Brooks standing over Sprout, a lecture pose or finger-wagging, Brooks holding Sprout's loupe, Brooks revealing or pointing at the bud, incorrect relative scale, wardrobe or badge changes, garbled or illegible text, bubbles overlapping either character's face." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P04-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v3.0.png"
```

---

## Step 5 --- P05: Look Closer

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, continuing with strict continuity from the previous panels -- this is the episode's closest investigation moment. Organic shapes, clean readable silhouettes, flat-to-soft dimensional color, no photorealism, no anime, no manga, no generic 3D redesign.

Characters, matched exactly to the supplied reference sheets:

SPROUT -- curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe.

RANGER BROOKS -- adult male naturalist mentor, bald under his hat, no beard, forest-green ranger uniform, campaign hat, approved badges, dark outdoor boots.

Sprout dominates the composition. She leans naturally toward the same key branch of the evergreen shrub (matching the supplied environment reference) and uses her magnifying loupe to inspect the damaged foliage and nearby buds. Her face shows intense curiosity and concentration, shifting toward the first hint of noticing something unexpected. Brooks remains visible behind or beside her, calm and patient, observing without pointing at the answer. Show the same brown/tan damaged foliage surrounding the key branch.

Include a subtle, organic Discovery Frame -- a soft circular or hand-drawn-style inset, like a magnifying-glass view, not a technological device -- showing an enlarged detail of the branch: damaged foliage around a small, plausible viable bud. No HUD, scanner, hologram, neon interface, or futuristic graphics. The bud should not glow, sparkle, or appear magical.

Use minimal dialogue space; reserve a small clean area for two very short reaction words and render, attributed to Sprout: \"Hmm... Wait...\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: a glowing or oversized bud, futuristic interface elements, an oversized loupe hiding Sprout's face, Brooks pointing out the clue, the plant looking greener than established, shrub continuity drift, garbled or illegible text, text covering the Discovery Frame or the bud." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P05-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v3.0.png"
```

---

## Step 6 --- P06: This Bud Is Alive!

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, continuing with strict continuity from the previous panels. Organic shapes, clean readable silhouettes, flat-to-soft dimensional color, no photorealism, no anime, no manga, no generic 3D redesign.

Characters, matched exactly to the supplied reference sheets: RANGER BROOKS (adult male naturalist mentor, bald under his hat, no beard, forest-green ranger uniform, campaign hat, approved badges, dark outdoor boots) and SPROUT (curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe).

Use a close-medium discovery/reaction composition beside the same evergreen shrub. Sprout has just recognized a small viable bud -- she is delighted and surprised, the genuine expression of a child who found evidence herself. Her loupe remains visible; she may gesture carefully toward the key bud-bearing branch. The viable bud must now be clearly readable while remaining botanically plausible; surrounding brown/tan winter-damaged foliage stays visible for contrast -- do not make the whole branch green. Brooks reacts to Sprout's discovery rather than taking control: he leans in slightly with a warm, proud, encouraging smile, his notebook secondary. Sprout holds the strongest narrative and visual position.

Reserve the dominant clean dialogue area for Sprout and a smaller secondary area for Brooks, and render exactly: Sprout: \"Brooks! This bud is still alive!\" and Brooks: \"Good eye, Sprout.\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: Brooks discovering or pointing out the bud first, the plant appearing healed, an enormous bud, magical glow or sparkles, an exaggerated victory pose, character drift, garbled or illegible text." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P06-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v3.0.png"
```

---

## Step 7 --- P07: Understanding Winter Injury

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio -- the episode's dedicated science-explanation panel, continuing with strict continuity from the previous panels but pulled back to a wider framing than the last two. Organic shapes, clean readable silhouettes, flat-to-soft dimensional color, no photorealism, no anime, no manga, no generic 3D redesign.

Characters, matched exactly to the supplied reference sheets: RANGER BROOKS (adult male naturalist mentor, bald under his hat, no beard, forest-green ranger uniform, campaign hat, approved badges, dark outdoor boots, notebook) and SPROUT (curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe).

Use a medium two-shot, positioned so more of the whole evergreen shrub is visible at once than in the previous panel: both the damaged, exposed side established earlier, and a healthier, more sheltered side of the same shrub (matching the supplied environment reference, which shows both). This visual contrast is the entire point of the panel -- frame the shrub so both conditions read clearly together. Brooks makes a gentle explanatory gesture toward the whole shrub, not just one branch, with a calm, thoughtful expression; his notebook may be open. Sprout remains engaged, looking between Brooks and the plant, not a passive listener. Preserve the same fence and light direction established since the opening panel; a little more of the yard's depth may show again here.

Reserve generous, clearly separated dialogue space for a three-line exchange, and render exactly: Brooks: \"Winter can dry out exposed parts, even when some of the plant is still alive.\" Sprout: \"So it's not all dead?\" Brooks: \"Not all of it. That's why we look closely.\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: showing only the damaged side of the shrub, Brooks in a standing lecture pose, the shrub reading as fully healthy, the three lines crowded into one bubble or overlapping shrub detail, garbled or illegible text." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P07-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v3.0.png"
```

---

## Step 8 --- P08: Look Before You Decide

```bash
python3 05-AI/Scripts/generate_image.py \
"Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio -- the episode's closing panel, continuing with exact continuity from the entire episode, pulled back further than the previous panel toward a medium-wide composition that echoes the opening environment shot without literally repeating it. Organic shapes, clean readable silhouettes, flat-to-soft dimensional color, no photorealism, no anime, no manga, no generic 3D redesign.

Characters, matched exactly to the supplied reference sheets: RANGER BROOKS (adult male naturalist mentor, bald under his hat, no beard, forest-green ranger uniform, campaign hat, approved badges, dark outdoor boots) and SPROUT (curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe, relaxed in her hand).

Return to a medium-wide composition beside the same evergreen shrub (matching the environment reference), with enough of the yard visible again -- fence, a hint of the stepping-stone path -- to echo the opening panel. The emotional energy is calmer than the discovery and explanation panels. Brooks remains near Sprout rather than in a dominant standing authority pose, making a gentle gesture toward the shrub with a warm, thoughtful expression. Sprout looks at the plant with new understanding, engaged and active rather than passive. The shrub must still visibly contain the same brown/tan winter-damaged foliage established earlier -- no instant recovery, no pruning happening, no removed shrub.

Reserve generous clean negative space for two short separated dialogue lines plus a closing caption, visually distinct from character dialogue. Render exactly: Sprout: \"So we shouldn't give up on it yet.\" Brooks: \"Exactly. Let's watch what grows before we decide what to cut.\" And, as a distinct caption styled differently from the speech bubbles (e.g. a simple banner or title-card treatment): \"LOOK CLOSER BEFORE YOU DECIDE.\"

Do not render the Lawn With Care logo anywhere in this image.

Avoid: a suddenly healthy/green shrub, pruning already happening, the plant removed, Brooks lecturing from above, Sprout looking passive, a location or weather change, the caption styled identically to the character speech bubbles, garbled or illegible text." \
-o "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/Drafts/S00E01-P08-Draft.png" \
-r "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
-r "01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png" \
-r "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v3.0.png"
```

---

## After Generation --- Review Before Anything Is "Final"

Every file lands in `Assets/Drafts/` as `PROPOSED / UNVERIFIED` (per
`AGENTS.md` §48) --- generation is not approval. For each of the 8
files, check against `06-Visual-Prompts.md`'s "Visual Approval
Checklist":

-   Brooks: face (bald under hat, no visible hair), hat, badges,
    wardrobe, proportions.
-   Sprout: face, age read, hair, headband, wardrobe, Discovery Band,
    loupe, proportions.
-   Relationship: relative scale, Sprout's visual agency, Brooks not
    dominating.
-   Episode continuity: same shrub/fence/path/snow placement across
    all 8, compatible lighting.
-   Science: damage plausible, viable bud plausible, no magical
    recovery, P07 shows both shrub sides together.
-   Dialogue: rendered text matches `04-Script.md` exactly, no
    spelling/rendering errors, correct placement, P08's caption reads
    as visually distinct from dialogue.

Report back per panel: which passed as-is, which need a regeneration
(and why), and which only need a text-correction pass rather than a
full re-render. Do not move anything out of `Assets/Drafts/` into
`Assets/Final/` without that review --- see `07-Production-Checklist.md`.

---

Status: **READY FOR EXECUTION --- v1.0**
