---
depends_on:
- 01-Concept-and-Learning-Objective.md
- 02-Story-Blueprint-and-Script.md
document: Codex Draft Generation Brief
episode: 03
last_update: 2026-08-11
season: 00
status: READY FOR EXECUTION
title: S00E03 --- Too Much Love Can Drown a Root
universe: Lawn With Care Universe
version: 1.2.0
---

# S00E03 --- Too Much Love Can Drown a Root

## 03 --- Codex Draft Generation Brief

## What This Document Is

Same structure as S00E01 v3.0 and S00E02's brief: one fully-resolved
prompt per panel, locked character/style blocks reused verbatim, no
historical patches. **Mode:** `DRAFT_MATCH_MASTER` for all panels.

---

## Locked Blocks (identical to S00E01/S00E02 --- reused, not redefined)

### REFERENCE_ROLES

Each reference has exactly one job. Do not let two references compete
to define the same thing --- see `S00E01/08-Retrospective-Notes.md`,
"Reference Authority Hierarchy," and `S00E02`'s brief, where this was
validated across a full 8-panel set.

| Reference file | Governs | Notes |
|---|---|---|
| `01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png` | Brooks' identity: face, proportions, silhouette, wardrobe, mark *placement*. | Required. |
| `01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png` | Sprout | Ignore the "Size Comparison" panel (112 cm defect). Required. |
| `13-Episodes/Season-00-Pilots/S00E03-Too-Much-Love-Can-Drown-a-Root/Assets/References/S00E03-Environment-Reference-v1.0.png` | Garden bed layout, plant state | Generate first (Step 0). Required. |

**Do not use:** `00-Franchise/Brand/Logos/04-icon-dark.png`/`05-icon-light.png` as a generation reference (reconfirmed 2026-08-11, S00E03 P03) --- the Master Model Sheet is the only Brooks reference, full stop. This matches the S00E01 Visual Canon Audit's final resolution: match the Master Model Sheet faithfully, marks included, with no competing official-asset reference fighting it. When the icon drifts (e.g. losing its letterform, changing frame shape), fix it with more explicit prompt wording describing the icon's construction, not by adding a second reference image.

**Do not use:** the Relationship Scale Sheet, or the Brooks Insignia &
Icons Sheet (`01-Characters/Brooks/Assets/Icons/`) --- it depicts a
maple-leaf chest pin the Visual Canon Audit already rejected as `NOT
CANON`; see `Brooks-Visual-Canon-Audit-v1.0.md`.

**If generating by hand in a chat UI (not the `generate_image.py`
script):** every reference marked "Required" or included as
"Optional" above must be physically attached/uploaded to that
generation turn. Writing the file path in the prompt text does not
make the generator see the file. Also verify the saved output
filename matches the panel actually shown before trusting it --- S00E02
had several regenerations save under the wrong panel number.

### STYLE_AND_LIGHT_LOCK

Bright, clean-outline, flat-to-soft-cel children's storybook
illustration style. **This episode's light is softly overcast** ---
still clear and readable, not hazy or dim, but without the crisp blue
sky used in S00E01/S00E02 --- matching the original draft's "overcast
soft daylight" setting and giving the set its own subtle visual
identity distinct from the other pilots. No photorealism, no anime, no
manga, no generic 3D redesign.

### BROOKS_LOCK

RANGER BROOKS: adult male naturalist mentor, calm warm expression,
approximately 188 cm tall, rounded approachable proportions. Bald
under his hat: no visible hair, no beard, no mustache, no stubble, no
freckles (freckles are Sprout's trait only), clean skin. Forest-green
ranger jacket over a plain collared shirt (no tie, no neckwear),
campaign hat (forest green, gold band), dark outdoor boots, may carry
his notebook and pencil.

Match `Brooks-Master-Model-Sheet-v1.0.png` faithfully for face,
proportions, uniform, and where each mark sits. Exactly three marks
total, nowhere else:

1. The official Lawn With Care icon, centered on the hat front above
   the gold band.
2. The same official Lawn With Care icon, once more, on his own
   anatomical left chest only --- no second chest mark, no pin, no
   additional badge anywhere on the chest or torso.
3. The Yard Ranger Canada badge (shield shape, white/light field, red
   maple leaf, restrained dark-green border, small "YARD" wordmark)
   on his own anatomical left sleeve only --- never the chest.

Each mark exactly once, never mirrored, duplicated, resized, or
relocated from its Master Model Sheet position. No name tag.

**Icon wording fix (carried over from S00E02, 2026-08-11):** always
write "the official Lawn With Care icon" in prompt text; never type
`[L]` in generation-prompt text --- the bracket notation reads as an
instruction to draw a literal letter L in brackets rather than
shorthand for the approved icon asset, and is the suspected root
cause of "Logo drift." See `Brooks-Visual-Canon-Audit-v1.0.md`.

**Icon construction, winning wording (found 2026-08-11, S00E03 P03,
after 3 regeneration rounds):** spelling out "the official Lawn With
Care icon" alone is not enough to prevent drift --- it took this exact
level of detail to get a clean, correctly colored, correctly
constructed result. Use this phrasing (or equivalent) wherever the
icon is described in a panel prompt:

> The official Lawn With Care icon, reproduced like an embroidered
> patch, built from exactly three parts: (1) a frame made of only
> three lines --- left vertical, right vertical, bottom horizontal, no
> top line, the top is open; the frame lines are GREEN, never gold or
> yellow. (2) a single two-lobed green leaf sitting in that open gap
> at the top, its base plugging the opening. (3) a bold WHITE letter
> "L" centered below the leaf. Two colors only: green and white ---
> never a single monochrome gold/tan icon.

Round 1 (plain "[L] icon" wording) produced a closed gold-monochrome
square with no visible letter. Round 2 (spelled-out but generic
wording) fixed the letter and got the two-color contrast partly right
but the frame stayed closed and gold. Round 3 (the wording above,
explicit about line-by-line frame construction and banning gold)
produced the accepted result. Each panel below has been updated to use
this wording.

**Known risk, not fully solved (carried over from S00E02):** the
"no freckles" instruction reduces but does not eliminate the risk ---
it failed on 2 of 8 S00E02 panels despite being present the whole
time. Crop Brooks' face at close zoom before approving any panel; see
"After Generation --- Review" below.

### SPROUT_LOCK

SPROUT: curious 9-year-old girl, approximately 130--135 cm tall.
Golden curly blonde hair, light-green eyes, light freckles, green
fabric headband, cream short-sleeve field shirt, olive-green shorts,
brown outdoor boots, Discovery Band across her chest, magnifying
loupe. Match `Sprout-Master-Model-Sheet-v1.0.png`'s face, hair, and
outfit faithfully. **This episode:** she also carries a small
watering can (muted green, no brand markings) in the early panels.
Exactly two arms and two hands, normal human anatomy --- never a third
arm or extra hand.

**Both-hands-occupied rule (carried over from S00E02, 2026-08-11):**
whenever a panel's action needs both of Sprout's hands doing something
other than holding a prop (soil, gesture, watering can down), any prop
not currently in use (loupe, watering can) must be explicitly placed
down or hung from the Discovery Band rather than left ambiguously
"holdable" --- a generator asked to keep a prop in-hand while also
occupying both hands with other actions has invented a third arm to do
it before (`S00E02-P06`, see `01-Characters/Sprout/11-Negative-Prompt.md`).

### RELATIONSHIP_LOCK

Brooks noticeably taller than Sprout whenever both are in frame.
Brooks guides, Sprout discovers. In this episode specifically, Brooks'
first move is to validate Sprout's question rather than correct her ---
this should read in his body language as taking her seriously, not as
gentle amusement.

### LETTERING_SPEC

Dialogue included directly in the prompt, one consistent tailed-bubble
style, closing caption (P08) as a distinct banner. **Bubble text
contains ONLY the spoken line --- no speaker name, no colon, no label.**

---

## New for This Episode --- GARDEN_STATE

A home garden bed near a porch, southern-Alberta-plausible residential
setting, soft overcast daylight (bright enough to read clearly, not
gloomy). One small plant sits visibly droopy, with yellowed lower
leaves, in dark soil that reads as clearly damp/wet --- not dry or
cracked. The soil's saturation should be visually legible (dark,
glossy-damp appearance, perhaps a faint sheen) without looking like
standing water or mud. No disease spots or pest damage --- the visual
story is specifically about water, not a competing explanation.

---

## Preflight

```bash
python3 05-AI/Scripts/preflight_check.py \
  --mode DRAFT_MATCH_MASTER \
  --prompt-file <panel prompt text file> \
  --ref "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
  --ref "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
  --ref "13-Episodes/Season-00-Pilots/S00E03-Too-Much-Love-Can-Drown-a-Root/Assets/References/S00E03-Environment-Reference-v1.0.png" \
  --output "<intended output path>"
```

---

## Step 0 --- Environment Reference

```text
Create a clean production reference sheet (no characters, no text, no logo) for the environment of the Lawn With Care Universe episode S00E03, in a bright, clean-outline, flat-to-soft-cel children's storybook illustration style. Soft overcast daylight -- clear and readable, not hazy or gloomy.

Show a home garden bed near a porch in a residential yard. One small plant sits visibly droopy, with some yellowed lower leaves, in dark soil that reads clearly as damp/saturated -- a faint sheen, no cracking, no dryness. No standing water or mud, just clearly wet dark soil. No disease spots, no pest damage, no other struggling plants nearby -- the visual story is specifically about this one overwatered plant. Include a hint of porch structure at one edge and simple garden landscaping.

No characters. No text. No labels. No logo. This is a production continuity reference, not a story panel.
```

**Output:** `Assets/References/S00E03-Environment-Reference-v1.0.png`

**Review before continuing:** does the soil read as clearly wet/saturated (not just "dark")? Is the plant's droop/yellowing visible without looking diseased or pest-damaged?

---

## P01 --- A Garden Bed by the Porch

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border. Bright, clean-outline, flat-to-soft-cel storybook style. Soft overcast daylight, clear and readable, not hazy or gloomy. No photorealism, no anime, no manga, no generic 3D redesign.

A wide establishing shot of a home garden bed near a porch -- no characters emphasized. One small plant sits visibly droopy with yellowed lower leaves, in dark, clearly damp soil, matching the supplied environment reference exactly. Simple porch structure at one edge, soft garden landscaping.

Reserve clean negative space for a short caption in a simple hand-lettered banner style: "Some things wilt not from too little care, but too much."

Avoid: the soil looking dry or cracked, the plant looking diseased or pest-damaged rather than overwatered, any character figures, garbled text.
```

**Output:** `Assets/Drafts/S00E03-P01-Draft.png`
**References:** Environment Reference v1.0 only.

---

## P02 --- I Water It Every Day

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing directly from the previous panel: same garden bed, same soft overcast daylight. Bright, clean-outline, flat-to-soft-cel storybook style, matching P01. No photorealism, no anime, no manga, no generic 3D redesign.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, light freckles, green fabric headband, cream short-sleeve field shirt, olive-green shorts, brown outdoor boots, Discovery Band across her chest, magnifying loupe, carrying a small muted-green watering can with no brand markings. Match Sprout-Master-Model-Sheet-v1.0.png's face, hair, and outfit faithfully.

Sprout kneeling beside the droopy plant, watering can in one hand, other hand gently touching a yellowed leaf, confused and a little worried expression -- she has clearly been caring for it faithfully and doesn't understand why it still looks unwell.

Reserve clean negative space for a tailed speech bubble containing ONLY this two-line text, no speaker label: "I gave it water every single day. Why is it still sad? Can you love a plant too much?" (spoken by Sprout).

Avoid: warm inconsistent color grading, Brooks appearing in this panel, garbled text, a speaker name/colon inside the bubble, more than one Sprout-like figure.
```

**Output:** `Assets/Drafts/S00E03-P02-Draft.png`
**References:** Sprout Master Model Sheet, Environment Reference v1.0.

---

## P03 --- You Can

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing directly from the previous panel with exact continuity. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: adult male naturalist mentor, bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall, notebook and pencil. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon (a three-line open-top frame in GREEN -- left, right, and bottom edges only, no top line -- with a green two-lobed leaf plugging the open top gap, and a bold WHITE letter L centered below it; never gold, never a closed four-sided square) on the hat front above the gold band, the same icon once more on his own anatomical left chest only, Yard Ranger maple-leaf badge (shield shape, red maple leaf) only on his own anatomical left sleeve -- never the chest. Each mark exactly once, no name tag.

SPROUT: curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, watering can set nearby.

Brooks kneels beside Sprout at the garden bed, at her conversational eye level, warm and taking her question seriously -- gentle, engaged expression, not amused or dismissive. Sprout looks up at him, genuinely wanting to know.

Reserve clean negative space for a tailed speech bubble containing ONLY this text, no speaker label: "You can. Roots don't just drink water -- they breathe through the tiny spaces around them." (spoken by Brooks).

Avoid: Brooks looking amused or condescending, warm golden/sepia grading, garbled text, a speaker name/colon inside the bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E03-P03-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P04 --- What the Soil Shows

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing with exact continuity. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon (a three-line open-top frame in GREEN -- left, right, and bottom edges only, no top line -- with a green two-lobed leaf plugging the open top gap, and a bold WHITE letter L centered below it; never gold, never a closed four-sided square) on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve -- never the chest. No name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band.

Medium shot: Brooks kneeling, gently pressing one hand into the damp soil to show Sprout how saturated it is, notebook open nearby. Sprout crouches beside him, watching closely, attentive.

Reserve clean negative space for a tailed speech bubble containing ONLY this text, no speaker label: "Too much water fills up all that space, and there's no air left for the roots at all." (spoken by Brooks).

Avoid: Brooks standing over Sprout, warm golden/sepia grading, garbled text, a speaker name/colon inside the bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E03-P04-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P05 --- Look Closer

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing with strict continuity -- the closest investigation moment. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

SPROUT: curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon (a three-line open-top frame in GREEN -- left, right, and bottom edges only, no top line -- with a green two-lobed leaf plugging the open top gap, and a bold WHITE letter L centered below it; never gold, never a closed four-sided square) on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve -- never the chest.

Close-up on Sprout's own fingers pressing into the damp soil, feeling the saturation herself -- concentrated, curious expression. Brooks visible behind or beside her, patient, watching without pointing at the answer.

Include a subtle, organic Discovery Frame -- a soft circular hand-drawn-style inset -- showing a simple cross-section idea: water filling the small spaces around a root, contrasted with a small comparison of what healthy, airy moist soil looks like around a root. No HUD, scanner, or futuristic graphics.

Reserve a small clean bubble area containing ONLY this text, no speaker label: "It's really squishy... like a sponge." (spoken by Sprout).

Avoid: futuristic interface elements, warm golden/sepia grading, Brooks pointing out the answer, garbled text, a speaker name/colon inside the bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E03-P05-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P06 --- It's Not Thirsty

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing with strict continuity. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon (a three-line open-top frame in GREEN -- left, right, and bottom edges only, no top line -- with a green two-lobed leaf plugging the open top gap, and a bold WHITE letter L centered below it; never gold, never a closed four-sided square) on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve -- never the chest. No name tag.

Sprout sitting back slightly, wide-eyed realization, looking at her damp fingers and then at the plant -- the reversal of her assumption is dawning on her. Brooks watching her reaction warmly, not supplying the realization for her.

Reserve a clean bubble area containing ONLY this text, no speaker label: "So it's not thirsty at all... it's drowning?" (spoken by Sprout).

Avoid: Brooks announcing the realization first, warm golden/sepia grading, garbled text, a speaker name/colon inside the bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E03-P06-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P07 --- Real Care Checks First

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border -- the dedicated understanding panel, pulled back to a wider framing than the last two. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall, notebook. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon (a three-line open-top frame in GREEN -- left, right, and bottom edges only, no top line -- with a green two-lobed leaf plugging the open top gap, and a bold WHITE letter L centered below it; never gold, never a closed four-sided square) on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve -- never the chest -- must match every other panel in the set exactly. No name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band.

Brooks kneels frame-left at Sprout's conversational eye level. Sprout kneels frame-right, engaged, thoughtful. Medium two-shot, cropped near the knees, the garden bed and plant visible between them.

Reserve generous, clearly separated dialogue space for a three-line exchange, each bubble containing ONLY the spoken line, no speaker label: Brooks: "Exactly. Even love needs to leave room to breathe." Sprout: "Like when someone hugs me so tight I can't move my arms?" Brooks: "Exactly like that."

Avoid: Brooks in a lecture pose, warm golden/sepia grading, the three lines crowded into one bubble, a speaker name/colon inside any bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E03-P07-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P08 --- Check Before You Water

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border -- the closing panel, pulled back further toward a medium-wide composition that echoes the opening environment shot. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon (a three-line open-top frame in GREEN -- left, right, and bottom edges only, no top line -- with a green two-lobed leaf plugging the open top gap, and a bold WHITE letter L centered below it; never gold, never a closed four-sided square) on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve -- never the chest. No name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, watering can set aside further away.

Medium-wide composition beside the garden bed, calmer emotional energy. Sprout kneeling calmly, watering can set aside, resting her fingers near the base of the plant instead of reaching for water. Brooks standing or kneeling beside her, watching with a warm, proud smile. The plant is still visibly droopy -- no instant recovery shown.

Reserve generous clean negative space for two short separated dialogue bubbles plus a closing caption, visually distinct from each other: two tailed speech bubbles each containing ONLY the spoken line, no speaker label -- Sprout: "So we check first. Every time." Brooks: "Every time. Not because we love it less -- because we're paying attention." -- and, styled as a separate banner/ribbon treatment: "LOVE NEEDS ROOM TO BREATHE."

Avoid: the plant suddenly looking recovered, Brooks lecturing from above, warm golden/sepia grading, the caption styled identically to the speech bubbles, a speaker name/colon inside any bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E03-P08-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## After Generation --- Review

Same review approach as S00E01/S00E02: check every panel against
character/mark consistency, dialogue accuracy, environment continuity,
style. Report per panel: pass, needs regeneration (why), or needs only
a text-compositing correction.

**Crop before approving (carried over from S00E02):** full-panel
viewing at normal size missed a third-arm anatomy error and faint
freckles on Brooks in S00E02 --- both were only visible on a close crop.
Use `05-AI/Scripts/crop_image.py` to zoom into Brooks' face and both
characters' hands on every panel before approving, not just when a
problem is already suspected.

---

# Status

**READY FOR EXECUTION --- v1.1 (2026-08-11: BROOKS_LOCK, SPROUT_LOCK, REFERENCE_ROLES and every panel's Avoid list updated to carry forward all S00E02 production lessons before generation begins)**
