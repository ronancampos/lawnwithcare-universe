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
supersedes: 09-Codex-Draft-Generation.md v2.4 and all prior Rounds 1--6
title: S00E01 --- Why Is It Sleeping So Long?
universe: Lawn With Care Universe
version: 3.0.0
---

# S00E01 --- Why Is It Sleeping So Long?

## 09 --- Codex Draft Generation Brief

## What This Document Is

A single, internally consistent, fully-resolved set of generation
prompts for S00E01's 8 panels. No history, no "use Round 2 but
replace this phrase" instructions, no alternate modes to choose
between mid-panel. If you find a contradiction anywhere in this
document, that is a bug in the document --- report it, don't silently
resolve it by picking one side.

**Why this replaces the previous six rounds:** an audit (2026-08-10,
run via Codex, summarized in `08-Retrospective-Notes.md`) found that
S00E01's rework wasn't caused by under-specified prompts. It was
caused by (1) contradictory instructions coexisting in the same
document, (2) reference images with ambiguous or competing roles, and
(3) no reproducible, auditable process. All three are fixed below.
Full incident history remains in `08-Retrospective-Notes.md` and git
history --- it is not repeated here.

---

## Locked Blocks

These blocks are the single source of truth for every panel below.
Each panel's full prompt is these blocks assembled with that panel's
delta --- if you ever need to hand-edit a panel prompt, edit the block
here first, then regenerate every panel's composed prompt from it.
Never edit one panel's copy of a block without updating this section.

### MODE

**`DRAFT_MATCH_MASTER`** for all 8 panels in this set. Brooks'
approved marks (per his Master Model Sheet) are reproduced faithfully
--- this is not the "hide all branding" mode used in earlier, now-
superseded rounds. See `06-Visual-Prompts.md`, "Logo and Brand Lock,"
for the full two-mode policy (`DRAFT_MATCH_MASTER` vs
`FINAL_BRAND_EXACT`) if a different asset ever needs the other mode.

### OUTPUT_LOCK

1080 × 1350 px, 4:5 portrait, full-bleed single illustration. The
artwork fills the entire canvas edge to edge --- no padding, no
border, no visible canvas edge, no additional panel frame, no
contact-sheet layout. One scene, one image.

### REFERENCE_ROLES

| Reference file | Governs | Notes |
|---|---|---|
| `01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png` | Brooks: face, body, uniform, marks | The **only** Brooks reference. Never combine with any other image containing a Brooks depiction. |
| `01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png` | Sprout: face, hair, outfit | Ignore this sheet's "Size Comparison" panel --- it shows Sprout at a non-canonical 112 cm and includes a second Brooks depiction. Operational height comes from `SPROUT_LOCK` text below, not this panel. |
| `13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v4.0.png` | Yard layout, shrub silhouette and damage pattern | This is a contact sheet (hero view + detail insets + palette swatches). Treat the large hero view as the composition authority; treat the insets only as texture/damage-pattern reference. **Known optimization not yet executed:** cropping this into per-panel-group operational references (see "Future Optimization" below) would reduce conditioning noise; the full sheet works but is not ideal. |
| `01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png` | Nothing --- **do not use as a generation reference.** | QA/staging reference only (see `Relationship-Canon.md`, "Visual Reference"). Contains ~15 independently-generated Brooks/Sprout vignettes, i.e. multiple competing character depictions. Scale and eye-line rules are already encoded as text in `RELATIONSHIP_LOCK` below. |
| `00-Franchise/Brand/Logos/04-icon-dark.png` | Nothing in `DRAFT_MATCH_MASTER` mode --- **do not use.** | Reserved for `FINAL_BRAND_EXACT` compositing only, via `composite_logo.py`. Adding it alongside the Master Model Sheet creates two competing `[L]` depictions, which is what produced blank/inconsistent results in an earlier round. |

**Rule of thumb, stated generally:** count how many reference images
contain a given character, not how many files you intended as "the"
reference for them. If the count is more than one, the model is
seeing competing versions of that character. `preflight_check.py`
checks this automatically --- see "Preflight" below.

### STYLE_AND_LIGHT_LOCK

Bright, clean-outline, flat-to-soft-cel children's storybook
illustration style, consistent across every image in the set
including the environment reference. Crisp blue sky, soft white
clouds, clear high-clarity cool early-spring daylight --- never
overcast, hazy, sepia, or golden-toned. The lawn reads pale-to-fresh
green transitioning out of dormancy, never tan/gold like autumn. No
photorealism, no anime, no manga, no generic 3D redesign.

### BROOKS_LOCK

RANGER BROOKS: adult male naturalist mentor, calm warm expression,
bald under his hat with no visible hair and no beard, approximately
188 cm tall, rounded approachable proportions. Forest-green ranger
jacket, campaign hat (forest green, gold band), dark outdoor boots,
may carry his notebook and pencil. Match
`Brooks-Master-Model-Sheet-v1.0.png` faithfully, including its marks:
the Lawn With Care `[L]` icon appears centered on the hat front above
the gold band, and a second `[L]` icon appears on Brooks's own
**anatomical left chest** (the side nearer his own left hand --- not
the viewer's left when he's facing forward); the Yard Ranger Canada
badge (maple leaf) appears only on Brooks's own **anatomical left
sleeve/shoulder**. Each mark appears exactly once, in exactly one of
these three locations --- never mirrored, never duplicated, never
relocated to the wrong side. If his left sleeve isn't visible in a
given composition, the badge is simply, naturally not visible --- do
not move it elsewhere to compensate. No name tag anywhere. Never
military, tactical, police, cowboy, or superhero styling.

### SPROUT_LOCK

SPROUT: curious 9-year-old girl, approximately 130--135 cm tall (the
operational canon height --- ignore the 112 cm figure that appears on
one non-canonical annotation of the Sprout reference sheet). Golden
curly blonde hair, light-green eyes, light freckles, green fabric
headband, cream short-sleeve field shirt, olive-green shorts, brown
outdoor boots, Discovery Band across her chest, magnifying loupe.
Energetic but natural child body language. Match
`Sprout-Master-Model-Sheet-v1.0.png`'s face, hair, and outfit
faithfully.

### RELATIONSHIP_LOCK

Brooks stands roughly 188 cm; Sprout stands roughly 130--135 cm ---
Brooks is noticeably, believably taller whenever both are in frame.
Brooks guides, Sprout discovers: Sprout holds the strongest
visual/narrative position during investigation beats; Brooks lowers
himself toward her conversational eye level during shared dialogue
rather than looming over her. Body language communicates trust and
shared discovery, never authority.

### YARD_AND_SHRUB_STATE

Setting: a modest residential backyard in southern Alberta, early
spring, caught between winter and spring. Simple wooden board fence
along at least two sides, a stepping-stone path, a section of house
siding visible in wide shots. Small, clearly bounded patches of
leftover snow only in shaded corners --- never a snow-covered yard.
Damp dark soil along bed edges, a few weathered fall leaves, one or
two bare deciduous saplings with faint bud swelling. The mystery
evergreen shrub sits along the fence line: small, dense, overlapping
scale/needle foliage (like cedar or juniper) throughout --- never
broad flat leaves, never holes or bite marks anywhere, in the main
image or in any close-up inset. Localized brown/tan winter-damaged
foliage on its more exposed side; a healthier, greener, more
sheltered side elsewhere on the same shrub; one key bud-bearing
branch with a small viable bud.

### LETTERING_SPEC

Dialogue text is included directly in the prompt and rendered as part
of the draft (per `06-Visual-Prompts.md`'s "Text Rule"), in one
consistent tailed-speech-bubble style throughout the set; the P08
closing caption is styled as a distinct banner, not a speech bubble.
**Bubble text must contain ONLY the spoken line --- no speaker name, no
colon, no label of any kind inside the bubble.** Speaker identity
comes from bubble position and tail direction alone. Treat rendered
text as a placement/legibility check: verify wording against
`04-Script.md` exactly and fix via compositing if needed, rather than
regenerating the whole panel for a text-only error.

### QA_ASSERTIONS (apply to every panel, in addition to panel-specific ones below)

- [ ] Exactly 1080×1350, full-bleed, no border/frame/contact-sheet layout.
- [ ] Brooks bald under hat; exactly one `[L]` on hat, exactly one `[L]`
      on his anatomical left chest; Yard Ranger badge present only if
      his left sleeve is in frame, on that sleeve only; no name tag;
      nothing mirrored or duplicated.
- [ ] Sprout reads as ~9 years old; hair, headband, outfit, Discovery
      Band, loupe all correct.
- [ ] Relative scale correct (Brooks visibly taller); Sprout has
      visual agency appropriate to the beat.
- [ ] Yard/shrub continuity holds against the previous panel (fence,
      path, snow placement, shrub silhouette and damage pattern).
- [ ] Rendered dialogue text matches `04-Script.md` exactly, no
      speaker-label artifacts, correctly positioned.
- [ ] Style and color match `STYLE_AND_LIGHT_LOCK` (no autumnal cast).

---

## Preflight (run before every generation call)

```bash
python3 05-AI/Scripts/preflight_check.py \
  --mode DRAFT_MATCH_MASTER \
  --prompt-file <path to a text file with the panel's full composed prompt> \
  --ref "01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png" \
  --ref "01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png" \
  --ref "13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/Assets/References/S00E01-Environment-Shrub-Reference-v4.0.png" \
  --output "<intended output path>"
```

This catches: stale "plain/unbranded/do not render the logo" language
left over from a copy-paste of an old round; more than one reference
image containing Brooks or Sprout; and accidental overwrite of an
existing file. Fix any reported problem before spending a generation
call on it.

---

## Attempt Naming (don't overwrite silently)

When iterating on a panel, keep every attempt instead of overwriting
in place, so a regression can be compared against what worked before:

```text
S00E01-P04-Draft-a01.png   (first attempt)
S00E01-P04-Draft-a02.png   (second attempt, after a fix)
```

Promote the approved attempt to `S00E01-P04-Draft.png` (no suffix)
only after it passes the QA assertions above. This is a process
recommendation, not yet automated --- see "Future Optimization" below.

---

## Generation Order

```text
P01 → P02 → P03 → P04 → P05 → P06 → P07 → P08
```

(The environment/shrub reference, v4.0, already exists and does not
need regenerating for this set --- reuse it as-is per
`REFERENCE_ROLES` above.)

---

# PANEL PROMPTS

Each block below is the fully composed prompt --- `STYLE_AND_LIGHT_LOCK`
+ `BROOKS_LOCK`/`SPROUT_LOCK`/`RELATIONSHIP_LOCK` as needed +
`YARD_AND_SHRUB_STATE` + that panel's delta (camera, action, dialogue)
--- ready to paste as-is. Do not add or remove branding language
per-panel; if `BROOKS_LOCK` ever changes, regenerate these from the
block above rather than hand-editing each one differently.

---

## P01 --- The Yard Wakes Up

**Delta:** wide, environment-led establishing shot, no characters.
Caption only, no speech bubble.

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border. Bright, clean-outline, flat-to-soft-cel storybook style. Crisp blue sky, soft white clouds, clear high-clarity cool early-spring daylight -- not overcast, hazy, sepia, or golden. No photorealism, no anime, no manga, no generic 3D redesign.

A wide, environment-led establishing shot of a modest residential backyard in southern Alberta, caught exactly between winter and spring -- no characters in this panel. Simple wooden board fence along at least two visible sides, a stepping-stone path curving diagonally through the space, a section of house siding visible at one edge, matching the supplied environment reference. Small, clearly bounded patches of leftover snow tucked into shaded corners -- never a snow-covered yard. Damp, recently-thawed dark soil along garden bed edges with a few flattened weathered fall leaves. One or two bare deciduous saplings with faint bud swelling near the fence. The mystery evergreen shrub (matching the supplied environment reference exactly: small, dense scale/needle foliage, localized brown/tan winter damage, no holes or bite marks anywhere) is visible along the fence line, roughly a third of the way into the yard -- readable but modest in the frame, not yet the subject.

Reserve clean negative space in the lower third for a short caption in a simple, friendly hand-lettered banner style (not a speech bubble): "Early spring in the yard."

Avoid: a fully green/summer lawn, a snow-covered yard, warm golden/sepia color grading, a painterly or textured technique different from the rest of the series, the shrub dominating the composition, any character figures, garbled or illegible text.
```

**Output:** `Assets/Drafts/S00E01-P01-Draft.png`
**References:** `S00E01-Environment-Shrub-Reference-v4.0.png` only.

**Panel-specific QA:** no characters present; caption text exact; shrub modest, not dominant.

---

## P02 --- Something Is Growing

**Delta:** medium shot, Sprout crouched over new growth, Brooks secondary. One Sprout line.

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing directly from the previous panel: same yard, same early-spring morning, same fence and path, same shrub visible in the background. Bright, clean-outline, flat-to-soft-cel storybook style, matching P01 exactly. Crisp blue sky, clear cool high-clarity daylight, fresh pale-green lawn -- not golden, hazy, or autumnal anywhere except the shrub's own damaged foliage. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: adult male naturalist mentor, calm warm expression, bald under his hat with no visible hair and no beard, approximately 188 cm tall, rounded approachable proportions. Forest-green ranger jacket, campaign hat (forest green, gold band), dark outdoor boots, may carry his notebook and pencil. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: the Lawn With Care [L] icon centered on the hat front above the gold band, and a second [L] icon on Brooks's own anatomical left chest; the Yard Ranger Canada maple-leaf badge only on his own anatomical left sleeve, if that sleeve is visible in this composition. Each mark exactly once, never mirrored or duplicated. No name tag. Never military, tactical, police, cowboy, or superhero styling.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, light freckles, green fabric headband, cream short-sleeve field shirt, olive-green shorts, brown outdoor boots, Discovery Band across her chest, magnifying loupe. Match Sprout-Master-Model-Sheet-v1.0.png's face, hair, and outfit faithfully.

Sprout is the visual lead, crouched naturally in the foreground, delighted as she closely observes fresh green shoots (or an emerging bulb) pushing up through damp, dark soil near the path. Her loupe is visible but not necessarily in use. Brooks is present farther back or to one side with lower visual emphasis, watching Sprout with a calm, warm expression, notebook optionally in hand -- he is not leading the discovery. Keep the shrub from the environment reference recognizable, softly out of focus, in the background. Brooks is noticeably taller than Sprout.

Reserve clean negative space in the upper-left or upper-center for a tailed speech bubble containing ONLY this line, no speaker label: "Brooks! Look! Everything's waking up!" (spoken by Sprout, shown by bubble position/tail).

Avoid: a lush summer lawn, warm golden/sepia grading, Brooks pointing out the discovery, Sprout looking older or younger than 9, garbled text, any speaker name/colon inside the bubble, more than one Brooks-like figure.
```

**Output:** `Assets/Drafts/S00E01-P02-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v4.0.

---

## P03 --- The Exception

**Delta:** medium shot, Sprout at the shrub, puzzled. Two-line Sprout bubble.

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing directly from the previous panel with exact continuity: same yard, same early-spring day, same lighting, same Brooks and Sprout clothing, same evergreen shrub. Bright, clean-outline, flat-to-soft-cel storybook style, matching the rest of the set. Crisp blue sky, clear cool high-clarity daylight, not golden or hazy anywhere except the shrub's own damaged foliage. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: adult male naturalist mentor, bald under his hat, no beard, approximately 188 cm tall. Forest-green ranger jacket, campaign hat, dark outdoor boots. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: [L] icon on hat front above the gold band, second [L] icon on his own anatomical left chest, Yard Ranger maple-leaf badge only on his own anatomical left sleeve if visible. Each mark exactly once, never mirrored or duplicated. No name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe.

Sprout has moved to the evergreen shrub, which occupies a substantial part of the composition: small, dense scale/needle foliage throughout, localized brown/tan winter damage concentrated on the more exposed portion, healthier greener structure elsewhere, no holes or bite marks anywhere -- concerning but not a completely dead featureless mass. Mulch or bare soil at the shrub's base.

Sprout is closest to the shrub, the visual focus, expression shifted from delight to puzzled concern, leaning or crouching toward the damaged foliage, gently gesturing toward it without touching or breaking anything. Brooks is approaching or standing behind/beside her with secondary visual weight -- he does not point at the answer and does not inspect the bud yet.

Reserve clean negative space in the upper-right (or another open area opposite Sprout) for a tailed speech bubble containing ONLY this two-line text, no speaker label: "Except this one... Why is it sleeping so long?" (spoken by Sprout).

Avoid: a horror-like fully dead plant, disease spots, insect holes or bite marks, animal chewing, a broken trunk, warm golden/sepia grading, Brooks already examining the bud, garbled text, any speaker name/colon inside the bubble, more than one Brooks-like figure.
```

**Output:** `Assets/Drafts/S00E01-P03-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v4.0.

**Panel-specific QA:** watch this one closely for badge-text legibility --- a prior attempt rendered the sleeve badge's text garbled here specifically.

---

## P04 --- What Do You Notice?

**Delta:** intimate two-shot, Brooks kneels to Sprout's level. Three-line exchange. Script fixed 2026-08-10 --- opens with "Let's not guess yet," not "Maybe," which had nothing in P03 to respond to.

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing directly from the previous panel with exact continuity: same shrub, same damage pattern, same lighting and wardrobe. Bright, clean-outline, flat-to-soft-cel storybook style, matching the rest of the set. Crisp blue sky, clear cool high-clarity daylight, not golden or hazy. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: adult male naturalist mentor, bald under his hat, no beard, approximately 188 cm tall, notebook and pencil. Forest-green ranger jacket, campaign hat, dark outdoor boots. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: [L] icon on hat front above the gold band, second [L] icon on his own anatomical left chest, Yard Ranger maple-leaf badge only on his own anatomical left sleeve if visible. Each mark exactly once, never mirrored or duplicated. No name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe.

Brooks kneels frame-left at Sprout's conversational eye level -- his greater height still reads believably through his proportions even while lowered. Calm, open, encouraging expression; notebook rests in one hand (if it shows writing, keep it to simple plain doodles or lines, never invented logos or slogans); if he gestures, it refers generally to the plant and never points directly at any specific bud. Sprout kneels frame-right, focused and thoughtful, actively comparing parts of the shrub with her loupe ready in hand, attention moving between Brooks and the plant. Medium two-shot, cropped near the knees. The composition visually communicates shared investigation, not a lecture. Keep the brown/tan exposed scale/needle foliage visible, no holes.

Reserve two separated clean dialogue areas in the upper composition. Render exactly, each bubble containing ONLY the line with no speaker label: a larger bubble near Brooks with "Let's not guess yet. What do you notice?" and a smaller bubble near Sprout with "The outside looks brown and dry."

Avoid: Brooks standing over Sprout, a lecture pose, Brooks holding Sprout's loupe, Brooks revealing or pointing at the bud, incorrect relative scale, warm golden/sepia grading, garbled text, any speaker name/colon inside a bubble, bubbles overlapping either character's face, more than one Brooks-like figure.
```

**Output:** `Assets/Drafts/S00E01-P04-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v4.0.

**Panel-specific QA:** this is the panel that previously rendered "Brooks:"/"Sprout:" inside the bubbles --- double-check bubble text contains only the spoken line.

---

## P05 --- Look Closer

**Delta:** close investigation shot, Discovery Frame inset. Minimal reaction text.

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing with strict continuity from the previous panels -- the episode's closest investigation moment. Bright, clean-outline, flat-to-soft-cel storybook style, matching the rest of the set. Crisp, clear, cool daylight, not golden or hazy. No photorealism, no anime, no manga, no generic 3D redesign.

SPROUT: curious 9-year-old girl, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe.

RANGER BROOKS: adult male naturalist mentor, bald under his hat, no beard. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: [L] icon on hat front, second [L] on his own anatomical left chest, Yard Ranger badge only on his own anatomical left sleeve if visible. Each mark exactly once.

Sprout dominates the composition, leaning toward the same key branch of the evergreen shrub and using her loupe to inspect the damaged foliage and nearby buds, face shifting from concentration to the first hint of noticing something. Brooks remains visible behind or beside her, calm and patient, observing without pointing at the answer.

CRITICAL foliage texture, in both the main image and the close-up inset: small, dense, overlapping scale/needle evergreen texture throughout (like cedar or juniper) -- never broad flat leaf shapes, and never any holes, bite marks, or perforations anywhere. Damage reads only as a color change from green to brown/tan, never as physical damage to the foliage shape. (A previous attempt at this exact panel produced insect-eaten-looking foliage in the inset -- this must not recur.)

Include a subtle, organic Discovery Frame -- a soft circular hand-drawn-style inset, like a magnifying-glass view, not a technological device -- showing an enlarged detail of the branch: intact scale/needle foliage (damaged brown, undamaged green, no holes) around a small, plausible viable bud, no glow or sparkle. No HUD, scanner, hologram, or futuristic graphics.

Reserve a small clean tailed-speech-bubble area for a short reaction containing ONLY this text, no speaker label: "Hmm... Wait..." (spoken by Sprout).

Avoid: leaf holes or bite marks anywhere, broad flat leaf shapes, a glowing or oversized bud, futuristic interface elements, an oversized loupe hiding Sprout's face, Brooks pointing out the clue, warm golden/sepia grading, garbled text, a speaker name/colon inside the bubble, more than one Brooks-like figure.
```

**Output:** `Assets/Drafts/S00E01-P05-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v4.0.

---

## P06 --- This Bud Is Alive!

**Delta:** close-medium discovery/reaction shot. Two-line exchange.

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border, continuing with strict continuity from the previous panels. Bright, clean-outline, flat-to-soft-cel storybook style, matching the rest of the set. Crisp, clear, cool daylight, not golden or hazy. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: adult male naturalist mentor, bald under his hat, no beard, approximately 188 cm tall. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: [L] icon on hat front, second [L] on his own anatomical left chest, Yard Ranger badge only on his own anatomical left sleeve if visible. Each mark exactly once, no name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe.

Close-medium discovery/reaction composition beside the same evergreen shrub (small dense scale/needle foliage, no holes anywhere). Sprout has just recognized a small viable bud -- delighted, genuine surprise, the expression of a child who found evidence herself. Loupe visible; she may gesture carefully toward the key bud-bearing branch. The viable bud is now clearly readable while remaining botanically plausible; surrounding brown/tan winter-damaged foliage stays visible for contrast -- do not make the whole branch green. Brooks reacts to Sprout's discovery rather than taking control: leans in slightly, warm proud encouraging smile, notebook secondary. Sprout holds the strongest narrative and visual position.

Reserve the dominant clean bubble area for Sprout and a smaller secondary bubble for Brooks, each containing ONLY the spoken line, no speaker label: Sprout's bubble: "Brooks! This bud is still alive!" Brooks's bubble: "Good eye, Sprout."

Avoid: Brooks discovering or pointing out the bud first, the plant appearing healed, an enormous bud, magical glow or sparkles, leaf holes or bite marks, warm golden/sepia grading, an exaggerated victory pose, garbled text, a speaker name/colon inside either bubble, more than one Brooks-like figure.
```

**Output:** `Assets/Drafts/S00E01-P06-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v4.0.

---

## P07 --- Understanding Winter Injury

**Delta:** wider two-shot showing both damaged and healthy sides of the shrub together. Three-line exchange. Positive blocking (not just "avoid a lecture pose").

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border -- the episode's dedicated science-explanation panel, continuing with strict continuity from the previous panels but pulled back to a wider framing than the last two. Bright, clean-outline, flat-to-soft-cel storybook style, matching the rest of the set. Crisp blue sky, clear cool high-clarity daylight, not golden or hazy anywhere except the shrub's own damaged side. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: adult male naturalist mentor, bald under his hat, no beard, approximately 188 cm tall, notebook. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: [L] icon on hat front, second [L] on his own anatomical left chest, Yard Ranger badge only on his own anatomical left sleeve if visible -- this must match every other panel in the set exactly, present in all of them the same way. No name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe.

Brooks kneels frame-left at Sprout's conversational eye level. Sprout kneels frame-right and actively compares both sides of the shrub, looking between Brooks and the plant, engaged rather than a passive listener. Medium two-shot, cropped near the knees, positioned so more of the whole evergreen shrub is visible than in the previous panel: both the damaged, exposed side established earlier, and a healthier, more sheltered side of the same plant, both in matching scale/needle texture with no holes anywhere. This visual contrast -- damaged vs. healthy, side by side on one shrub -- is the entire point of the panel; frame it so both read clearly together. Brooks makes a gentle explanatory gesture toward the whole shrub, not just one branch, calm and thoughtful. Preserve the same fence, light direction, and seasonal cues established since P01.

Reserve generous, clearly separated dialogue-safe space for a three-line exchange, each bubble containing ONLY the spoken line, no speaker label: Brooks: "Winter can dry out exposed parts, even when some of the plant is still alive." Sprout: "So it's not all dead?" Brooks: "Not all of it. That's why we look closely."

Avoid: only the damaged side of the shrub being visible, Brooks standing in a lecture pose, the shrub reading as fully healthy, leaf holes or bite marks, warm golden/sepia grading, the three lines crowded into one bubble or overlapping shrub detail, a speaker name/colon inside any bubble, more than one Brooks-like figure.
```

**Output:** `Assets/Drafts/S00E01-P07-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v4.0.

**Panel-specific QA:** both damaged AND healthy sides of the shrub must be visible together --- this is the panel's whole scientific point.

---

## P08 --- Look Before You Decide

**Delta:** medium-wide closing shot, echoing P01. Two-line exchange plus a distinct closing caption.

```text
Portrait children's educational storybook illustration for the Lawn With Care Universe, 4:5 aspect ratio, full-bleed, no border -- the episode's closing panel, continuing with exact continuity from the entire episode, pulled back further than the previous panel toward a medium-wide composition that echoes the opening environment shot without literally repeating it. Bright, clean-outline, flat-to-soft-cel storybook style, matching the rest of the set. Crisp blue sky, clear cool high-clarity daylight, not golden or hazy. No photorealism, no anime, no manga, no generic 3D redesign.

RANGER BROOKS: adult male naturalist mentor, bald under his hat, no beard, approximately 188 cm tall. Match Brooks-Master-Model-Sheet-v1.0.png faithfully, including its marks: [L] icon on hat front, second [L] on his own anatomical left chest, Yard Ranger badge only on his own anatomical left sleeve if visible. Each mark exactly once, no name tag.

SPROUT: curious 9-year-old girl, approximately 130-135 cm tall, golden curly blonde hair, light-green eyes, freckles, green headband, cream field shirt, olive-green shorts, brown outdoor boots, Discovery Band, magnifying loupe relaxed in her hand.

Medium-wide composition beside the same evergreen shrub, with enough of the yard visible again -- fence, a hint of the stepping-stone path -- to echo the opening panel. Calmer emotional energy than the discovery and explanation panels. Brooks stands or kneels near Sprout rather than in a dominant standing authority pose, gentle gesture toward the shrub, warm thoughtful expression. Sprout looks at the plant with new understanding, engaged and active rather than passive. The shrub still visibly contains the same brown/tan winter-damaged foliage established earlier -- no instant recovery, no pruning happening, no removed shrub.

Reserve generous clean negative space for two short separated dialogue bubbles plus a closing caption, visually distinct from each other: two tailed speech bubbles (same style as the rest of the set) each containing ONLY the spoken line, no speaker label -- Sprout: "So we shouldn't give up on it yet." Brooks: "Exactly. Let's watch what grows before we decide what to cut." -- and, styled as a separate banner/ribbon treatment (not a speech bubble): "LOOK CLOSER BEFORE YOU DECIDE."

Avoid: a suddenly healthy/green shrub, pruning already happening, the plant removed, Brooks lecturing from above, Sprout looking passive, warm golden/sepia grading, a location or weather change, the caption styled identically to the speech bubbles, a speaker name/colon inside any bubble, more than one Brooks-like figure.
```

**Output:** `Assets/Drafts/S00E01-P08-Draft.png`
**References:** Brooks Master Model Sheet, Sprout Master Model Sheet, Environment Reference v4.0.

---

# After Generation --- Review

Check every panel against its `QA_ASSERTIONS` (shared list above, plus
any panel-specific note). Report per panel: pass as-is, needs a
regeneration (and why), or needs only a text-compositing correction.
Do not move anything to `Assets/Final/` without this review --- see
`07-Production-Checklist.md`.

---

# Future Optimization (not yet executed, P1/P2 --- see `08-Retrospective-Notes.md` for the full priority table)

- **Operational environment crops:** derive single-purpose crops from
  `S00E01-Environment-Shrub-Reference-v4.0.png` using
  `05-AI/Scripts/crop_image.py` --- full yard (for P01/P02/P08), shrub +
  damage map (P03/P04), key branch + bud (P05/P06), whole shrub both
  sides (P07) --- instead of feeding the full contact sheet to every
  panel.
- **Deterministic lettering:** move dialogue insertion out of
  generation entirely (reserve bubble areas in the art, composite
  exact text from `04-Script.md` afterward) once a lettering tool
  exists, rather than relying on the generator to render text
  correctly, which is still fundamentally unreliable even though it's
  worked well so far in this set.
- **Generation manifest:** log prompt text, reference file hashes,
  model, attempt number, and rejection reason per generation call, so
  rounds are comparable and diagnosable without reconstructing history
  from chat logs.
- **Automated technical QA:** a script that checks decodable PNG, RGB,
  exact 1080×1350, full-bleed (no border), and correct file naming
  across the whole P01--P08 set before human visual review.
- **Sprout Master Model Sheet fix:** the sheet's "Size Comparison"
  panel shows Sprout at 112 cm (not the 130--135 cm operational canon)
  and includes a second Brooks depiction. This doesn't block current
  generation (the text lock overrides it, and the front-view figure
  used for face/hair/outfit is unaffected) but is a real defect in an
  approved reference asset --- flagged for the project owner, not
  silently fixed. See `01-Characters/Sprout/Assets/References/Audits/`
  (create if it doesn't exist yet --- Sprout doesn't have a Visual
  Canon Audit the way Brooks does).

---

# Status

**READY FOR EXECUTION --- v3.0 (single resolved prompt per panel, no
historical patches, explicit reference roles, DRAFT_MATCH_MASTER mode
declared)**
