---
depends_on:
- 01-Concept-and-Learning-Objective.md
- 02-Story-Blueprint-and-Script.md
document: Codex Draft Generation Brief
episode: 02
last_update: 2026-08-11
season: 00
status: FIRST DEFINITIVE CUT APPROVED
title: S00E02 --- Why Does the Ground Need to Breathe?
universe: Lawn With Care Universe
version: 1.3.0
---

# S00E02 --- Why Does the Ground Need to Breathe?

## 03 --- Codex Draft Generation Brief

## What This Document Is

A single, self-contained, fully-resolved set of generation prompts,
built the same way as S00E01's (see
`13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/09-Codex-Draft-Generation.md`
v3.0 for the full rationale): one resolved prompt per panel, locked
character/style blocks reused verbatim from the proven S00E01 set, no
historical patches.

**Mode:** `DRAFT_MATCH_MASTER` for all panels --- Brooks' marks are
reproduced faithfully from his Master Model Sheet, exactly as
established for S00E01.

---

## Locked Blocks (identical to S00E01 --- reused, not redefined)

### REFERENCE_ROLES

Each reference has exactly one job. Do not let two references compete
to define the same thing --- that combination is what caused drift in
S00E01 (see `S00E01/08-Retrospective-Notes.md`, "Reference Authority
Hierarchy").

| Reference file | Governs | Notes |
|---|---|---|
| `01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png` | Brooks' identity: face, proportions, silhouette, wardrobe, mark *placement*. | Required. |
| `01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png` | Sprout | Ignore the "Size Comparison" panel (112 cm defect) --- see `01-Characters/Sprout/14-Canon.md`. Required. |
| `13-Episodes/Season-00-Pilots/S00E02-Why-Does-the-Ground-Need-to-Breathe/Assets/References/S00E02-Environment-Reference-v1.0.png` | Yard layout, worn-path/healthy-lawn contrast | Generate this first (Step 0 below) before any panel. Required. |
| `00-Franchise/Brand/Logos/04-icon-dark.png` (or `05-icon-light.png`) | The official Lawn With Care icon's *exact geometry only* (frame, leaf, letterform) --- not Brooks' identity. | Optional but recommended (confirmed working 2026-08-11, S00E02 P02.1). Only add this alongside the "Icon wording fix" note in `BROOKS_LOCK` below --- without it, this reference competes with the Master Model Sheet's own approximation instead of clarifying it. |

**Do not use:** the Relationship Scale Sheet (QA-only, never a
generation input --- see `Relationship-Canon.md`) or the Brooks
Insignia & Icons Sheet (`01-Characters/Brooks/Assets/Icons/`) ---
it depicts a maple-leaf chest pin the Visual Canon Audit already
rejected as `NOT CANON`; see `Brooks-Visual-Canon-Audit-v1.0.md`.

**If generating by hand in a chat UI (not the `generate_image.py`
script):** every reference marked "Required" or included as
"Optional" above must be physically attached/uploaded to that
generation turn. Writing the file path in the prompt text does not
make the generator see the file --- this is silently ignored, not
enforced.

### STYLE_AND_LIGHT_LOCK

Bright, clean-outline, flat-to-soft-cel children's storybook
illustration style, consistent across every image in the set. Crisp
blue sky, soft white clouds, clear high-clarity daylight. No
photorealism, no anime, no manga, no generic 3D redesign.

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
relocated from its Master Model Sheet position. No name tag. Never
military, tactical, police, cowboy, or superhero styling.

**Icon wording fix (added 2026-08-11):** always write "the official
Lawn With Care icon" in prompt text and, when the brand icon file is
attached as a reference (see `REFERENCE_ROLES`), let that image
define its construction. Never type `[L]` in generation-prompt text
--- the bracket notation is fine as informal shorthand in conversation
or documentation, but inside a prompt it reads as an instruction to
draw a literal letter L in brackets, which is the suspected cause of
the "Logo drift" failure mode logged in
`Brooks-Visual-Canon-Audit-v1.0.md`.

### SPROUT_LOCK

SPROUT: curious 9-year-old girl, approximately 130--135 cm tall
(operational canon height). Golden curly blonde hair, light-green
eyes, light freckles, green fabric headband, cream short-sleeve field
shirt, olive-green shorts, brown outdoor boots, Discovery Band across
her chest, magnifying loupe. Match
`Sprout-Master-Model-Sheet-v1.0.png`'s face, hair, and outfit
faithfully. Exactly two arms, two hands, normal human anatomy --- never
a third arm or an extra hand.

**Both-hands-occupied rule (added 2026-08-11, after S00E02 P06):**
whenever a panel's action needs both of Sprout's hands doing something
other than holding it (e.g. one hand touching soil, one hand
gesturing), the magnifying loupe hangs from its cord on the Discovery
Band instead of being held --- do not leave it "holdable" in a pose
that has no free hand for it. A generator asked to keep the loupe
in-hand while also occupying both hands with other actions has
invented a third arm to do it (`S00E02-p06.png`, corrected in
`S00E02-P06.1`). Also: any bare-soil touch point described as
"healthy lawn soil" or similar must sit within the single worn path
already established by the episode's environment reference --- never a
second, separate bare patch elsewhere in the grass.

### RELATIONSHIP_LOCK

Brooks noticeably taller than Sprout whenever both are in frame.
Brooks guides, Sprout discovers: Sprout holds the strongest
visual/narrative position during investigation beats; Brooks lowers
himself to her conversational eye level rather than looming.

### LETTERING_SPEC

Dialogue text is included directly in the prompt and rendered as part
of the draft, one consistent tailed-speech-bubble style throughout,
closing caption (P08) as a distinct banner. **Bubble text contains
ONLY the spoken line --- no speaker name, no colon, no label.** Verify
rendered text against `02-Story-Blueprint-and-Script.md` exactly.

---

## New for This Episode --- YARD_AND_SOIL_STATE

A well-loved residential backyard, late spring, warm clear daylight. A
worn path/patch cuts across one section of the lawn --- visibly thin,
pale grass with some bare soil showing where feet cross it repeatedly
--- contrasted with thick, healthy, deep-green grass everywhere else in
the yard. The worn strip should read as a clear, deliberate desire
path (a natural walking line, e.g. between a gate and a play area),
not a random dead patch --- the shape should imply repeated footsteps.
No disease spots, no pest damage, no dead/brown grass elsewhere in the
yard --- the healthy grass must read as genuinely thriving, so the
contrast is legible.

---

## Preflight

Run before every generation call, same as S00E01:

```bash
python3 05-AI/Scripts/preflight_check.py \
  --mode DRAFT_MATCH_MASTER \
  --prompt-file <panel prompt text file> \
  --ref "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
  --ref "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
  --ref "13-Episodes/Season-00-Pilots/S00E02-Why-Does-the-Ground-Need-to-Breathe/Assets/References/S00E02-Environment-Reference-v1.0.png" \
  --output "<intended output path>"
```

---

## Step 0 --- Environment Reference

```text
Create a clean production reference sheet (no characters, no text, no logo) for the environment of the Lawn With Care Universe episode S00E02, in a bright, clean-outline, flat-to-soft-cel children's storybook illustration style. Crisp blue sky, clear high-clarity daylight.

Show a well-loved residential backyard in late spring. A worn path/patch cuts diagonally across one section of the lawn -- clearly a repeated walking line between two points (e.g. a gate and a play area) -- with thin, pale grass and some bare soil showing where feet cross it most. Everywhere else in the yard, the grass is thick, healthy, and deep green -- genuinely thriving, no disease, no pests, no other brown patches, so the contrast with the worn strip is the only visual anomaly. Include a simple wooden fence, a section of house siding at one edge, and soft natural yard landscaping.

No characters. No text. No labels. No logo. This is a production continuity reference, not a story panel.
```

**Output:** `Assets/References/S00E02-Environment-Reference-v1.0.png`

**Review before continuing:** is the worn strip legible as a distinct desire-path shape, not a random blob? Does the surrounding lawn read as genuinely healthy (not just "less brown")?

---

## P01 --- The Yard, Two Ways

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border. Bright, clean-outline, flat-to-soft-cel storybook style. Crisp blue sky, clear high-clarity daylight, not overcast or hazy. No photorealism, no anime, no manga, no generic 3D redesign.

A wide, environment-led establishing shot of a well-loved residential backyard in late spring -- no characters emphasized. A worn path/patch cuts diagonally across one section of the lawn, matching the supplied environment reference exactly: thin pale grass, some bare soil, a clear repeated-walking-line shape. Everywhere else, the grass is thick and healthy. Simple wooden fence, house siding visible at one edge.

Reserve clean negative space for a short caption in a simple hand-lettered banner style: "The paths we love most are the ones we walk without noticing."

Avoid: the worn patch looking like a random dead spot rather than a walking path, the healthy grass looking anything less than thriving, warm golden/sepia color grading, any character figures, garbled text.
```

**Output:** `Assets/Drafts/S00E02-P01-Draft.png`
**References:** Environment Reference v1.0 only.

---

## P02 --- Everything Else Is Thriving

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing directly from the previous panel: same yard, same daylight. Bright, clean-outline, flat-to-soft-cel storybook style, matching P01. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: adult male naturalist mentor, calm warm expression, bald under his hat with no visible hair, no beard, no mustache, no stubble, and no freckles, approximately 188 cm tall. Forest-green ranger jacket over a plain collared shirt (no tie, no neckwear), campaign hat (forest green, gold band), dark outdoor boots, may carry his notebook and pencil. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon on the hat front above the gold band, the same icon once more on his own anatomical left chest only, and the Yard Ranger maple-leaf badge (shield shape, white field, red maple leaf, dark-green border, small "YARD" wordmark) only on his own anatomical left sleeve --- never the chest. Each mark exactly once, never mirrored, duplicated, or clustered together. No name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, light freckles, green fabric headband, cream short-sleeve field shirt, olive-green shorts, brown outdoor boots, Discovery Band across her chest, magnifying loupe. Match Sprout-Master-Model-Sheet-v1.0.png's face, hair, and outfit faithfully.

Sprout is the visual lead, crouched delighted in the thick, healthy section of the lawn, running a hand through the deep-green grass. Brooks is present farther back or to one side, secondary, watching with a calm warm expression. Brooks is noticeably taller than Sprout.

Reserve clean negative space for a tailed speech bubble containing ONLY this line, no speaker label: "Brooks, look how thick the grass is over here!" (spoken by Sprout).

Avoid: warm golden/sepia grading, more than one Brooks-like or Sprout-like figure, garbled text, a speaker name/colon inside the bubble, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E02-P02-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P03 --- The Thin Strip

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing directly from the previous panel with exact continuity. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve --- never the chest. Each mark exactly once, no name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe.

Sprout has moved to the worn path, standing or crouching, puzzled concerned expression looking down at the thin, patchy grass and bare soil. Brooks approaching or standing behind/beside her, secondary weight, not yet explaining anything.

Reserve clean negative space for a tailed speech bubble containing ONLY this two-line text, no speaker label: "But over here it's... kind of sad. Why won't it grow like the rest?" (spoken by Sprout).

Avoid: the worn patch looking diseased or pest-damaged rather than compacted/worn, warm golden/sepia grading, Brooks already explaining, garbled text, a speaker name/colon inside the bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E02-P03-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P04 --- What Do You Notice About the Ground?

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing with exact continuity. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall, notebook and pencil. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve --- never the chest. Each mark exactly once, no name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe.

Brooks kneels frame-left at Sprout's conversational eye level beside the worn strip, calm open expression, notebook in one hand, gesturing generally toward the ground (not pointing at a specific answer). Sprout kneels frame-right, thoughtful, looking at the ground rather than the grass. Medium two-shot, cropped near the knees.

Reserve two separated clean dialogue areas. Render exactly, each bubble containing ONLY the line with no speaker label: a larger bubble near Brooks with "Let's find out. What do you notice about the ground itself?" and a smaller bubble near Sprout with "It feels harder. Like a sidewalk almost."

Avoid: Brooks standing over Sprout, a lecture pose, warm golden/sepia grading, garbled text, a speaker name/colon inside a bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E02-P04-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P05 --- Look Closer

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing with strict continuity -- the closest investigation moment. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

SPROUT: curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve --- never the chest.

Close-up on Sprout pressing one finger down into the worn, compacted soil, meeting visible resistance -- the soil surface does not yield. Brooks visible behind or beside her, calm and patient, watching without pointing at the answer.

Include a subtle, organic Discovery Frame -- a soft circular hand-drawn-style inset -- showing an enlarged side-by-side comparison: the compacted soil (dense, hard, no visible gaps) next to a small sample of the healthy lawn's soil (crumbly, with visible small air pockets). No HUD, scanner, or futuristic graphics.

Reserve a small clean bubble area containing ONLY this text, no speaker label: "Whoa... my finger won't even go in." (spoken by Sprout).

Avoid: futuristic interface elements, warm golden/sepia grading, Brooks pointing out the answer, garbled text, a speaker name/colon inside the bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E02-P05-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P06 --- It's a Totally Different Ground

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing with strict continuity. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve --- never the chest. No name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe.

Sprout delighted and surprised, one hand pressed into soft healthy lawn soil, the other gesturing back toward the compacted worn strip -- testing both, discovering the contrast herself. Her expression shifts partway through from delight to a quieter, more thoughtful recognition, as if she's just realized something personal, not just factual. Brooks reacts warmly, leaning in slightly, watching her have the realization rather than supplying it.

Reserve the dominant clean bubble area for Sprout, containing ONLY this text (rendered as two small sequential bubbles from her, not one crowded paragraph), no speaker label: "Brooks! Over here it's soft -- but this part is packed down solid!" then "...Wait. This is my path. The one I take to the swing every day."

Avoid: Brooks discovering or announcing it first, warm golden/sepia grading, an exaggerated pose, garbled text, a speaker name/colon inside the bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E02-P06-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## P07 --- Understanding Compaction

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border -- the dedicated science-explanation panel, pulled back to a wider framing than the last two. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall, notebook. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve --- never the chest -- must match every other panel in the set exactly. No name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe.

Brooks kneels frame-left at Sprout's conversational eye level. Sprout kneels frame-right, engaged, looking between Brooks and the ground. Medium two-shot, cropped near the knees, positioned so both the worn strip and a visible edge of the healthy lawn are in frame together -- the visual contrast is the point of this panel. Brooks makes a gentle explanatory gesture toward the worn strip.

Reserve generous, clearly separated dialogue space for a three-line exchange, each bubble containing ONLY the spoken line, no speaker label: Brooks: "That's compaction. When soil gets packed too tight, there's no room left for air or water to reach the roots." Sprout: "Like when everyone's squeezed onto the same bench, and I can't breathe deep?" Brooks: "Exactly like that. Even a path we love needs room to breathe too."

Avoid: only the worn strip visible without the healthy lawn contrast, Brooks in a lecture pose, warm golden/sepia grading, the three lines crowded into one bubble, a speaker name/colon inside any bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E02-P07-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

**Panel-specific QA:** both the worn strip AND healthy lawn must be visible together --- this panel's whole scientific point, same requirement pattern as S00E01's P07.

---

## P08 --- Give It Room

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border -- the closing panel, pulled back further toward a medium-wide composition that echoes the opening environment shot. Bright, clean-outline, flat-to-soft-cel storybook style. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: bald under his hat, no beard, no mustache, no stubble, no freckles, no tie, approximately 188 cm tall. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the official Lawn With Care icon on the hat front, the same icon once more on his own anatomical left chest only, Yard Ranger badge (shield shape, red maple leaf) only on his own anatomical left sleeve --- never the chest. No name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe relaxed in her hand.

Medium-wide composition beside the worn strip, with enough of the yard visible again to echo the opening panel. Calmer emotional energy. Brooks near Sprout, gentle gesture toward the ground, warm thoughtful expression -- perhaps gesturing at the idea of small holes/openings in the soil rather than performing an action. Sprout engaged, looking at the ground with new understanding. The worn strip still visibly thin and compacted -- no instant recovery, no equipment/tool being actively used yet.

Reserve generous clean negative space for two short separated dialogue bubbles plus a closing caption, visually distinct from each other: two tailed speech bubbles each containing ONLY the spoken line, no speaker label -- Sprout: "So we give it room. Maybe I'll take the long way to the swing sometimes." Brooks: "That would help. And a few holes poked through the soil let the air find its way back down to the roots." -- and, styled as a separate banner/ribbon treatment: "GIVE THE GROUND ROOM TO BREATHE."

Avoid: the worn strip suddenly looking fully recovered, active pruning/tool-use already happening, Brooks lecturing from above, warm golden/sepia grading, the caption styled identically to the speech bubbles, a speaker name/colon inside any bubble, more than one Brooks-like or Sprout-like figure, Brooks wearing a tie, Brooks with freckles/facial hair/visible hair, any mark on Brooks's chest besides the single official Lawn With Care icon, the maple-leaf badge appearing anywhere but the sleeve.
```

**Output:** `Assets/Drafts/S00E02-P08-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v1.0.

---

## After Generation --- Review

Same `QA_ASSERTIONS` approach as S00E01: check every panel for character/mark consistency, dialogue accuracy, environment continuity, and style. Report per panel: pass, needs regeneration (why), or needs only a text-compositing correction. Do not move anything to `Assets/Final/` without this review.

**Crop before approving (added 2026-08-11, after full S00E02 production):**
full-panel viewing at normal size missed two real defects this
episode that only became visible on a close crop --- a third arm/extra
hand on Sprout (`S00E02-P06.png`) and faint freckles on Brooks'
face (`S00E02-P07.png`, `S00E02-P07.1.png`). Both were confirmed using
`05-AI/Scripts/crop_image.py` to zoom into the specific region (hands,
face, chest/sleeve marks) before making a pass/fail call. Treat this
as a required review step, not an optional one: crop Brooks' face and
both characters' hands on every panel before approving, even when the
full image looks fine at a glance.

**Freckles on Brooks are an intermittent risk, not a solved problem
(added 2026-08-11):** the "no freckles" wording fix held clean across
P02.1--P06, then reappeared on P07 through two regeneration attempts
with progressively stronger wording, then did not reappear on P08 with
the same wording as the failed P07 attempts. This means the fix
reduces the failure rate but does not guarantee it --- keep checking
every panel at close crop rather than assuming the wording alone has
solved it. See `Brooks-Visual-Canon-Audit-v1.0.md` for the tracked
finding.

**Watch output filenames when generating by hand across a long chat
session (added 2026-08-11):** multiple S00E02 panels came back saved
one panel number ahead of what was actually generated (P06 content
saved as `P07.1`/`P07.2`; P07 content saved as `P08.1`). The image
content was correct each time --- only the filename drifted, likely
from the chat session's own internal turn-counting rather than the
episode's panel numbering. Verify the filename matches the panel
actually shown before treating it as that panel's draft.

---

# Status

**FIRST DEFINITIVE CUT APPROVED --- v1.3 (all 8 panels generated, reviewed, and promoted to `Assets/Final/`, 2026-08-11; P07 has one documented non-blocking imperfection, see `07-Production-Checklist.md`)**
