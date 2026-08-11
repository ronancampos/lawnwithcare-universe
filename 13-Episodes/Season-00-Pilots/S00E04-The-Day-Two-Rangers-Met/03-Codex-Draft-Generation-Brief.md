---
depends_on:
- 01-Concept-and-Narrative-Objective.md
- 02-Story-Blueprint-and-Script.md
document: Codex Draft Generation Brief
episode: 04
last_update: 2026-08-11
season: 00
status: READY FOR EXECUTION (PROPOSED EPISODE — NOT YET CANON)
title: S00E04 --- The Day Two Rangers Met
universe: Lawn With Care Universe
version: 1.1.0
---

# S00E04 --- The Day Two Rangers Met

## 03 --- Codex Draft Generation Brief

## What This Document Is

Same structure as S00E01/S00E02/S00E03: one fully-resolved prompt per
panel, locked blocks reused, no historical patches. **This episode is
`PROPOSED`, not canon** --- see `README.md` before treating any
resulting artwork as more than a production test. **Mode:**
`DRAFT_MATCH_MASTER` for all panels.

---

## Locked Blocks (mostly identical to S00E01--S00E03 --- one
## deliberate exception noted in SPROUT_LOCK below)

### REFERENCE_ROLES

Each reference has exactly one job. Do not let two references compete
to define the same thing --- see `S00E01/08-Retrospective-Notes.md`,
"Reference Authority Hierarchy."

| Reference file | Governs | Notes |
|---|---|---|
| `01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png` | Brooks | The only Brooks reference, unchanged from other episodes. Required. |
| `01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png` | Sprout's face/hair/proportions only | Ignore the "Size Comparison" panel (112 cm defect). **Do not copy the loupe or Discovery Band from this reference in P01--P06** --- see SPROUT_LOCK below; they are added back only from P07 onward. Required. |
| `13-Episodes/Season-00-Pilots/S00E04-The-Day-Two-Rangers-Met/Assets/References/S00E04-Environment-Reference-v1.0.png` | Front yard / flower bed layout | Generate first (Step 0). Required. |

**Do not use:** the Relationship Scale Sheet, the official brand logo
file (`00-Franchise/Brand/Logos/`), or the Brooks Insignia & Icons
Sheet (`01-Characters/Brooks/Assets/Icons/`) --- the Master Model
Sheet is the only Brooks reference, full stop (reconfirmed
2026-08-11, S00E03); the Icons Sheet depicts a maple-leaf chest pin
the Visual Canon Audit already rejected as `NOT CANON`.

**If generating by hand in a chat UI:** every "Required" reference
above must be physically attached/uploaded to that generation turn ---
naming the file path in the prompt text does not make the generator
see it. Also verify the saved output filename matches the panel
actually shown before trusting it.

### STYLE_AND_LIGHT_LOCK

Bright, clean-outline, flat-to-soft-cel children's storybook
illustration style. **Early morning light** --- soft, warm, low-angle,
quieter and more intimate than the other episodes' midday brightness,
matching this episode's more personal register. No photorealism, no
anime, no manga, no generic 3D redesign.

### BROOKS_LOCK

Same identity as S00E01--S00E03, updated with the production fixes
found across those episodes (tie/freckle exclusions, spelled-out icon
wording, the proven icon-construction phrasing from S00E03).

RANGER BROOKS: adult male naturalist mentor, calm warm expression,
approximately 188 cm tall, rounded approachable proportions. Bald
under his hat: no visible hair, no beard, no mustache, no stubble, no
freckles (freckles are Sprout's trait only), clean skin. Forest-green
ranger jacket over a plain collared shirt (no tie, no neckwear),
campaign hat (forest green, gold band), dark outdoor boots.

Match `Brooks-Master-Model-Sheet-v1.0.png` faithfully for face,
proportions, uniform, and where each mark sits. Exactly three marks
total, nowhere else:

1. The official Lawn With Care icon (a three-line open-top frame in
   GREEN --- left, right, and bottom edges only, no top line --- with a
   green two-lobed leaf plugging the open top gap, and a bold WHITE
   letter L centered below it; never gold, never a closed four-sided
   square) on the hat front above the gold band.
2. The same icon, once more, on his own anatomical left chest only ---
   no second chest mark, no pin, no additional badge on the chest or
   torso.
3. The Yard Ranger Canada badge (shield shape, white/light field, red
   maple leaf, restrained dark-green border, small "YARD" wordmark) on
   his own anatomical left sleeve only --- never the chest.

Each mark exactly once, never mirrored, duplicated, resized, or
relocated. No name tag. **This episode:** in the closing panels he
extends a small magnifying loupe toward Sprout --- otherwise
unchanged.

### SPROUT_LOCK --- Episode-Specific Variant

SPROUT: curious 9-year-old girl, approximately 130--135 cm tall ---
same canonical age, proportions, and face as every other episode, NOT
younger or differently designed. Golden curly blonde hair, light-green
eyes, light freckles, green fabric headband, cream short-sleeve field
shirt, olive-green shorts, brown outdoor boots. Match
`Sprout-Master-Model-Sheet-v1.0.png`'s face, hair, and outfit
faithfully **except**:

- **P01--P06: no magnifying loupe, no Discovery Band.** This is a
  deliberate, temporary, narratively-justified omission for this
  origin episode only --- do not treat it as her new default design.
- **P07--P08: she receives and then holds the magnifying loupe** (a
  small handheld magnifying glass, simple design, no ornamentation).
  Still no Discovery Band --- that begins after this episode, not
  during it.

Exactly two arms and two hands, normal human anatomy --- never a third
arm or extra hand. Whenever a panel needs both of Sprout's hands doing
something other than holding a prop, any prop not currently in use
must be explicitly set down rather than left ambiguously "holdable" ---
a generator asked to keep a prop in-hand while both hands are occupied
elsewhere has invented a third arm to do it before (`S00E02-P06`).

### RELATIONSHIP_LOCK

Brooks noticeably taller than Sprout whenever both are in frame.
**This episode inverts the usual dynamic slightly:** for the first
half (P01--P02), Sprout is alone --- there is no "Brooks guides, Sprout
discovers" interaction yet, because they haven't met. From P03 onward,
Brooks' entire role is validation, not instruction --- he confirms what
Sprout already noticed rather than teaching her something new.

### LETTERING_SPEC

Dialogue included directly in the prompt, one consistent tailed-bubble
style, closing caption (P08) as a distinct banner. **Bubble text
contains ONLY the spoken line --- no speaker name, no colon, no label.**

---

## New for This Episode --- YARD_STATE

A quiet residential front yard, early morning, soft warm low-angle
light. A small flower bed near the sidewalk holds one visibly wilted,
drooping flower among otherwise healthy plants --- subtle, easy to walk
past without noticing, not dramatic or alarming. A sidewalk runs along
the yard's edge, useful for Brooks' distant approach in P01. The
overall mood is quiet and unhurried, distinct from the more
"discovery-adventure" energy of S00E01--S00E03.

---

## Preflight

```bash
python3 05-AI/Scripts/preflight_check.py \
  --mode DRAFT_MATCH_MASTER \
  --prompt-file <panel prompt text file> \
  --ref "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
  --ref "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
  --ref "13-Episodes/Season-00-Pilots/S00E04-The-Day-Two-Rangers-Met/Assets/References/S00E04-Environment-Reference-v1.0.png" \
  --output "<intended output path>"
```

Note: `preflight_check.py`'s single-Brooks/single-Sprout reference
rule still applies normally here --- the loupe/Band omission is a
prompt-text instruction, not a reference-file change, so the tool's
checks are unaffected.

---

## Step 0 --- Environment Reference

```text
Create a clean production reference sheet (no characters, no text, no logo) for the environment of the Lawn With Care Universe episode S00E04, in a bright, clean-outline, flat-to-soft-cel children's storybook illustration style. Soft, warm, early-morning low-angle light -- quiet and gentle, not the crisp midday brightness of other episodes in this series.

Show a quiet residential front yard with a sidewalk running along its edge. A small flower bed near the sidewalk holds mostly healthy plants, with one visibly wilted, drooping flower among them -- subtle enough that someone could easily walk past without noticing it, not dramatic or alarming. Include simple house architecture at one edge.

No characters. No text. No labels. No logo. This is a production continuity reference, not a story panel.
```

**Output:** `Assets/References/S00E04-Environment-Reference-v1.0.png`

**Review before continuing:** does the wilted flower read as subtle/easy-to-miss rather than dramatic? Does the light feel quieter/warmer than the other episodes' references?

---

## P01 --- A Quiet Front Yard

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border. Bright, clean-outline, flat-to-soft-cel storybook style. Soft, warm, early-morning low-angle light. No photorealism, no anime, no manga, no generic 3D redesign.

A wide establishing shot of a quiet residential front yard, early morning. SPROUT (curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, light freckles, green fabric headband, cream short-sleeve field shirt, olive-green shorts, brown outdoor boots, matching Sprout-Master-Model-Sheet-v1.0.png's face, hair, and outfit faithfully -- NO magnifying loupe, NO Discovery Band, she doesn't have them yet in this story) stands alone at the edge of the yard, looking uncertainly toward a small flower bed nearby, matching the supplied environment reference. In the far distance down the sidewalk, RANGER BROOKS (adult male naturalist mentor, bald under his hat, no beard, no tie, forest-green ranger uniform, campaign hat, matching Brooks-Master-Model-Sheet-v1.0.png faithfully including his hat and chest official Lawn With Care icons -- green open-top frame, green leaf, white letter L, never gold or closed) is visible approaching, small in the frame, not yet close enough to interact.

Reserve clean negative space for a short caption in a simple hand-lettered banner style: "Before the Discovery Band. Before the loupe."

Avoid: Sprout carrying a magnifying loupe or wearing a Discovery Band, Brooks already close/interacting, warm golden/sepia grading that looks like a different time of day than soft early morning, garbled text, more than one Sprout-like or Brooks-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair.
```

**Output:** `Assets/Drafts/S00E04-P01-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P02 --- Does Anybody Else See This?

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing directly from the previous panel: same yard, same early-morning light. Bright, clean-outline, flat-to-soft-cel storybook style, matching P01. No photorealism, no anime, no manga, no generic 3D redesign.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, light freckles, green fabric headband, cream short-sleeve field shirt, olive-green shorts, brown outdoor boots. Match Sprout-Master-Model-Sheet-v1.0.png's face, hair, and outfit faithfully. NO magnifying loupe, NO Discovery Band -- she doesn't have them yet.

Close-up: Sprout crouching alone beside the small flower bed, gently touching a drooping petal with one finger, looking around as if checking whether anyone else has noticed it too -- a little unsure, quietly curious expression, not sad.

Reserve clean negative space for a tailed speech bubble containing ONLY this two-line text, no speaker label: "Does anybody else see this? Or am I the only one who noticed it was sad?" (spoken by Sprout).

Avoid: a magnifying loupe or Discovery Band appearing on Sprout, Brooks appearing in this panel, warm golden/sepia grading, garbled text, a speaker name/colon inside the bubble, more than one Sprout-like figure.
```

**Output:** `Assets/Drafts/S00E04-P02-Draft.png`
**References:** Sprout Master Model Sheet, Environment Reference v1.0.

---

## P03 --- I See It Too

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing directly from the previous panel with exact continuity. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: adult male naturalist mentor, calm warm expression, bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall. Forest-green ranger jacket over a plain collared shirt, campaign hat, dark outdoor boots, notebook and pencil. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon (a three-line open-top frame in GREEN -- left, right, and bottom edges only, no top line -- with a green two-lobed leaf plugging the open top gap, and a bold WHITE letter L centered below it; never gold, never a closed four-sided square) on the hat front above the gold band, the same icon once more on his own anatomical left chest only, Yard Ranger maple-leaf badge (shield shape, red maple leaf) only on his own anatomical left sleeve -- never the chest. Each mark exactly once, no name tag.

SPROUT: curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots. NO magnifying loupe, NO Discovery Band yet.

Brooks kneels down beside Sprout at the flower bed, lowering himself fully to her eye level -- his first action is to get low, not speak from standing height. Warm, genuinely interested expression. Sprout looks up at him, a little shy but interested, not afraid.

Reserve clean negative space for a tailed speech bubble containing ONLY this two-line text, no speaker label: "I see it too. Good eye -- most people walk right past a flower like this without ever looking down." (spoken by Brooks).

Avoid: Brooks standing over her rather than kneeling, a magnifying loupe or Discovery Band appearing on Sprout, warm golden/sepia grading, garbled text, a speaker name/colon inside the bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E04-P03-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P04 --- Somebody Should Notice

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing with exact continuity. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, light freckles, green fabric headband, cream short-sleeve field shirt, olive-green shorts, brown outdoor boots. NO magnifying loupe, NO Discovery Band yet.

Close-up: Sprout standing a little taller than before, looking down at the flower bed with a small, surprised smile just beginning to form -- the first flicker of pride at having noticed something that mattered. Soft warm morning light.

Reserve clean negative space for a tailed speech bubble containing ONLY this text, no speaker label: "I just thought... somebody should notice before it's too late to help." (spoken by Sprout).

Avoid: a magnifying loupe or Discovery Band appearing on Sprout, Brooks dominating the frame, warm golden/sepia grading beyond the intended soft morning light, garbled text, a speaker name/colon inside the bubble, more than one Sprout-like figure.
```

**Output:** `Assets/Drafts/S00E04-P04-Draft.png`
**References:** Sprout Master Model Sheet, Environment Reference v1.0.

---

## P05 --- That's Exactly What a Ranger Does

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing with strict continuity. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall, notebook and pencil. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon (a three-line open-top frame in GREEN -- left, right, and bottom edges only, no top line -- with a green two-lobed leaf plugging the open top gap, and a bold WHITE letter L centered below it; never gold, never a closed four-sided square) on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve -- never the chest. No name tag.

SPROUT: curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots. NO magnifying loupe, NO Discovery Band yet.

Medium shot: Brooks looking at Sprout with a gentle, moved expression, as if he's just recognized something important in her -- pencil paused above the notebook. Sprout listening closely, quiet and attentive.

Reserve clean negative space for a tailed speech bubble containing ONLY this two-line text, no speaker label: "...That's exactly what a Ranger does. Noticing before it's too late -- that's the whole job." (spoken by Brooks).

Avoid: a magnifying loupe or Discovery Band appearing on Sprout, warm golden/sepia grading, garbled text, a speaker name/colon inside the bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E04-P05-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P06 --- You Already Know How

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing with strict continuity -- same intimate framing as the previous panel, a beat later. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon (a three-line open-top frame in GREEN -- left, right, and bottom edges only, no top line -- with a green two-lobed leaf plugging the open top gap, and a bold WHITE letter L centered below it; never gold, never a closed four-sided square) on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve -- never the chest. No name tag.

SPROUT: curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots. NO magnifying loupe, NO Discovery Band yet.

Close two-shot, Brooks' expression softening further, warm and sincere. Sprout listening closely, quietly taking the words in.

Reserve clean negative space for a tailed speech bubble containing ONLY this text, no speaker label: "You already know how to do the hardest part." (spoken by Brooks).

Avoid: a magnifying loupe or Discovery Band appearing on Sprout, warm golden/sepia grading, garbled text, a speaker name/colon inside the bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E04-P06-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P07 --- The Loupe

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border -- the episode's symbolic gift moment. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon (a three-line open-top frame in GREEN -- left, right, and bottom edges only, no top line -- with a green two-lobed leaf plugging the open top gap, and a bold WHITE letter L centered below it; never gold, never a closed four-sided square) on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve -- never the chest. Notebook now closed, held at his side; his other hand extends a small, simple handheld magnifying glass toward Sprout. Warm, proud smile.

SPROUT: curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots. Still NO Discovery Band (that begins after this episode). Reaching up with both hands to receive the magnifying glass, bright delighted wide-eyed expression -- this is the first time she holds it.

Medium-wide shot, quiet front yard, warm morning light. Brooks handing Sprout the magnifying glass; she reaches up eagerly.

Reserve clean negative space for a tailed speech bubble containing ONLY this two-line text, no speaker label: "Every Ranger starts somewhere. Here -- start noticing with this." (spoken by Brooks).

Avoid: Sprout already holding the loupe as if she's had it before, a Discovery Band appearing, warm golden/sepia grading, garbled text, a speaker name/colon inside the bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E04-P07-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P08 --- Let's Find Out

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border -- the closing panel. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon (a three-line open-top frame in GREEN -- left, right, and bottom edges only, no top line -- with a green two-lobed leaf plugging the open top gap, and a bold WHITE letter L centered below it; never gold, never a closed four-sided square) on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve -- never the chest. Warm, settled smile.

SPROUT: curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, now holding her new magnifying glass and looking through it at the flower bed for the first time -- delighted, focused. Still no Discovery Band.

Medium-wide shot, quiet front yard, warm settled morning light, calmer energy than the previous panel. Sprout looking through the loupe at the flower bed; Brooks beside her, watching warmly. This composition should visually echo the partnership shown in every other produced episode -- the visual beginning of it.

Reserve generous clean negative space for a speech bubble plus a closing caption, visually distinct from each other: a tailed speech bubble containing ONLY the spoken line, no speaker label -- Sprout: "Let's find out what else I've been missing." -- and, styled as a separate banner/ribbon treatment: "EVERY RANGER STARTS BY NOTICING."

Avoid: a Discovery Band appearing, warm golden/sepia grading, the caption styled identically to the speech bubble, a speaker name/colon inside the bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E04-P08-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## After Generation --- Review

Same review approach as the other episodes, plus one addition specific
to this episode: confirm P01--P06 show no loupe/Band on Sprout, and
P07--P08 correctly show the loupe (still no Band). Do not treat any
resulting artwork as canon-final --- flag for the owner's explicit
approval per `README.md`, "Canon Status," before this episode's
backstory is treated as official.

**Crop before approving (carried over from S00E02/S00E03):**
full-panel viewing at normal size has missed real defects in every
episode so far --- a third-arm anatomy error, faint freckles on Brooks,
and a wrong icon frame/color, all only visible on close crop. Use
`05-AI/Scripts/crop_image.py` to zoom into Brooks' face, his hat/chest
icons, and both characters' hands on every panel before approving.

---

# Status

**READY FOR EXECUTION --- v1.1 (PROPOSED EPISODE --- NOT YET CANON; 2026-08-11: BROOKS_LOCK, SPROUT_LOCK, REFERENCE_ROLES and every panel updated to carry forward all S00E02/S00E03 production lessons before generation begins)**
