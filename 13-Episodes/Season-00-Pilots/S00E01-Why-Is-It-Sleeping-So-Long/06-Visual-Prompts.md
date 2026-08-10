---
depends_on:
- 01-Concept.md
- 02-Learning-Objective.md
- 03-Story-Blueprint.md
- 04-Script.md
- 05-Panel-Breakdown.md
document: Visual Prompts
episode: 01
last_update: 2026-08-10
season: 00
status: READY FOR VISUAL TESTING
supersedes: 06-Visual-Prompts.md v1.0 (six-panel, clean-art-only workflow)
title: S00E01 --- Why Is It Sleeping So Long?
universe: Lawn With Care Universe
version: 2.0.0
---

# S00E01 --- Why Is It Sleeping So Long?

## 06 --- Visual Prompts

## Purpose

This document contains the production prompts for the eight
independent visual panels of S00E01.

Each panel is generated separately.

Primary output:

-   1080 × 1350 px
-   4:5 portrait
-   one image per panel
-   **dialogue from `04-Script.md` included in the first-draft
    generation prompt** (see "Text Rule" below --- this is a change
    from v1.0)
-   consistent characters, environment, shrub and lighting across the
    full carousel

The prompts are implementation instructions. They do not override
character canon, Master Model Sheets, Relationship Canon, official
brand assets or the approved episode documents.

------------------------------------------------------------------------

# Text Rule --- Updated for v2.0

**v1.0 rule (superseded):** generate clean art only, with no text of
any kind, and add all dialogue in a separate compositing pass after
final art approval.

**v2.0 rule (current):** the dialogue is locked at script stage
(`04-Script.md`) and is now written into each panel's draft prompt
below, positioned in the panel's designated dialogue-safe area. This
means the first draft of every panel should already show the
approved dialogue, not placeholder art waiting for text.

**Why this changed:** the production owner wants dialogue visible
from the first draft rather than deferred to a later, separate step,
so the panel can be judged as a whole -- art and words together -- from
the earliest review point.

**What did not change:** AI-rendered text inside generated images is
still unreliable (this was the reason for the old rule, and that
underlying fact hasn't changed). So:

1.  Include the exact dialogue text and its speaker in the prompt, as
    written below.
2.  Treat whatever text the model renders in the draft as a
    **placement and legibility check** -- does the composition leave
    room for this much text in this position? -- not as guaranteed
    final typography.
3.  Before export, run a **correction pass**: verify the rendered
    text against `04-Script.md` exactly (wording, spelling, speaker
    attribution) and fix any rendering errors through controlled
    compositing rather than trusting a second AI attempt to get it
    right.
4.  If a model instance cannot render legible text at all, generate
    the panel with the dialogue area left visually reserved (per the
    dialogue-safe notes below) and overlay the locked text
    immediately as part of that same draft pass -- the point is that
    the *draft you review* has the words in it, however they got
    there.

Reject a draft outright if the baked-in text materially changes the
composition in a way this document doesn't call for (e.g. crowding
out the bud, covering a face) -- fix via layout, not by shrinking
typography.

------------------------------------------------------------------------

# Reference Priority

For every panel, use the following authority order:

1.  Approved Brooks Master Model Sheet
2.  Approved Sprout Master Model Sheet
3.  Approved Brooks + Sprout Relationship/Scale reference
4.  Approved Brooks Design Rules / Canon / Negative Prompt
5.  Approved Sprout Design Rules / Canon / Negative Prompt
6.  Episode environment/shrub/yard reference
7.  `05-Panel-Breakdown.md`
8.  Locked dialogue (`04-Script.md`)
9.  Panel-specific prompt below

If generated artwork conflicts with a higher-level reference, reject
or correct the generated artwork. Do not change canon to accommodate
a generation error.

------------------------------------------------------------------------

# GLOBAL VISUAL LOCK

Apply this lock to P01--P08.

## Art Direction

Children's educational illustrated storybook/comic aesthetic. Use:
organic shapes; clean readable silhouettes; warm character appeal;
controlled flat-to-soft dimensional color; expressive but natural
poses; friendly visual storytelling; nature-focused environmental
detail; clear mobile-first composition. Avoid photorealism,
hyper-detailed cinematic realism, and generic 3D animation styling
that changes the approved character designs. Preserve the established
Lawn With Care Universe visual language from the canonical reference
assets.

## Brooks Lock

Match the approved Brooks Master Model Sheet exactly. Preserve:
canonical facial structure; canonical skin tone; **bald under the
hat, no added hairstyle, no visible hair when the hat is worn** (this
is an explicit open finding from the current pilot art -- hold this
line strictly); no beard; warm approachable expression; approved
campaign hat and hat insignia/badge configuration; forest-green
ranger clothing; approved chest insignia/badge configuration; dark
outdoor boots; canonical body proportions; notebook and pencil when
specified; approximately 188 cm standing height. Full list of
prohibited directions: `01-Characters/Brooks/11-Negative-Prompt.md`.

## Sprout Lock

Match the approved Sprout Master Model Sheet exactly. Preserve:
approximately 9-year-old appearance; canonical child proportions;
golden curly blonde hair; light-green eyes; freckles; green headband;
cream field shirt; olive-green shorts; brown outdoor boots; approved
Discovery Band; approved magnifying loupe design; energetic but
natural child body language. Full list of prohibited directions:
`01-Characters/Sprout/11-Negative-Prompt.md`.

## Relationship Lock

Brooks standing height ≈ 188 cm; Sprout height ≈ 130--135 cm; preserve
canonical relative scale; Brooks should not dominate every
composition; Sprout may occupy the strongest visual position during
investigation; Brooks lowers himself toward Sprout's conversational
level when appropriate; body language communicates trust and shared
discovery. Core relationship: **BROOKS GUIDES. SPROUT DISCOVERS.**

## Environment Lock

All eight panels occur in the same residential yard during one
continuous early-spring morning, plausible for Calgary / southern
Alberta without requiring identifiable landmarks. Preserve: same
fence line and stepping-stone path (established in P01); same
evergreen shrub; same nearby hardscape; same general background
vegetation; same early-spring seasonal state; same approximate time
of day; compatible soft daylight; consistent light direction; the
same leftover-snow patch positions established in P01. The yard is
not lush summer. Use restrained early-spring cues: muted grass
transitioning out of dormancy, damp or recently thawed soil, small
emerging growth, dormant vegetation mixed with subtle new life, cool
overcast atmosphere.

## Shrub Lock

One consistent hardy evergreen shrub. Stable overall silhouette;
plausible woody structure; localized brown/tan winter-damaged
foliage, more visible on an exposed portion; remaining viable
structure; one key bud-bearing branch used for the discovery; from
Panel 07 onward, a clearly readable healthier/sheltered side visible
in the same frame as the damaged side; no magical recovery between
panels. Do not depict fungal lesions, insect infestation, animal
chewing, broken trunk, mechanical damage, total featureless death, or
dramatic fantasy decay.

## Logo and Brand Lock

Do not ask the image generator to reproduce the Lawn With Care logo.
Composite the official source asset afterward if required. Never
generate or approximate extra leaves, altered open-frame geometry,
substitute typography, circular logo versions, or invented Lawn With
Care symbols. Overt branding is not required inside the generated
scene for this episode.

------------------------------------------------------------------------

# P01 --- The Yard Wakes Up

## Output

`S00E01-P01-Draft.png`

1080 × 1350 px, portrait 4:5.

## Prompt

Create a single portrait children's educational story illustration for
the Lawn With Care Universe: a wide, environment-led establishing
shot of a modest residential backyard in southern Alberta, caught
exactly between winter and spring.

Show a simple wooden board fence along at least two visible sides, a
stepping-stone path curving diagonally through the space, and a
section of the house's siding visible at one edge. The lawn is muted
and dormant with faint early green beginning to show through,
especially near the path. Include one or two small, clearly bounded
patches of leftover snow tucked into shaded corners -- the north side
of a shrub, the base of the fence -- without making the yard read as
snow-covered. Ground should show damp, recently-thawed dark soil
along garden bed edges, with a few flattened, weathered leaves left
over from fall near the shrub base and fence line. Include one or two
bare deciduous saplings with faint bud swelling near the fence. The
mystery evergreen shrub (with subtle localized brown/tan winter
damage) should be visible along the fence line, roughly a third of
the way into the yard, readable but not yet emphasized as the
subject. Sky should be soft, pale, and slightly overcast, with thin
horizontal cloud bands; light should come from one clear direction,
producing long, soft, cool shadows consistent with early morning.

Brooks and Sprout may appear as small, unposed figures entering the
frame from the path, or may be omitted entirely -- this panel's focus
is the yard itself, not the characters.

If a caption is desired for this panel, reserve clean negative space
in the lower third for the short line: *"Early spring in the yard."*
Render this caption text plainly and legibly if the model supports
it; otherwise leave the space reserved.

No speech bubbles. No generated logo.

## Visual Priority

1.  the season/setting itself
2.  yard layout (fence, path, house edge)
3.  the shrub's position, established but not emphasized
4.  leftover-snow placement
5.  optional caption

## Reject If

-   the yard looks like summer or is snow-covered;
-   the shrub already dominates the composition;
-   characters (if included) are posed or expressive;
-   AI-generated text appears anywhere other than the reserved caption
    area, if used.

------------------------------------------------------------------------

# P02 --- Something Is Growing

## Output

`S00E01-P02-Draft.png`

1080 × 1350 px, portrait 4:5.

## Prompt

Create the next independent portrait story illustration, maintaining
exact visual continuity with P01: same yard, same early-spring
morning, same lighting, same fence and path, same shrub visible in
the background.

Use a medium composition at a child-friendly eye level, noticeably
closer than P01. Sprout is the visual lead, crouched naturally in the
foreground or near-middle ground, delighted as she closely observes
fresh green shoots (or an emerging bulb) pushing up through damp,
dark soil near the path. A few flattened fall leaves are visible
nearby. Her canonical magnifying loupe is visible but not necessarily
in use. Brooks is present farther back or to one side with lower
visual emphasis, watching Sprout's investigation with a calm, warm
expression, notebook optionally in hand -- not leading the discovery.

Maintain the canonical Brooks/Sprout scale. Keep the shrub from P01
recognizable, softly out of focus, in the background for continuity
without making it the subject.

Reserve clean negative space in the upper-left or upper-center for
one short speech bubble, and render this exact line inside that
bubble: **Sprout: "Brooks! Look! Everything's waking up!"**

No generated logo.

## Visual Priority

1.  Sprout's wonder
2.  the specific new-growth clue
3.  early-spring yard continuity from P01
4.  Brooks as supportive secondary presence
5.  Sprout's dialogue

## Reject If

-   the yard looks like summer;
-   Brooks leads the discovery;
-   Sprout looks older/younger than canon;
-   character clothing changes;
-   Brooks badges drift;
-   the dialogue text is missing, misplaced over a face, or doesn't
    match the script wording.

------------------------------------------------------------------------

# P03 --- The Exception

## Output

`S00E01-P03-Draft.png`

1080 × 1350 px, portrait 4:5.

## Prompt

Create the third independent portrait illustration, maintaining exact
continuity with P01--P02: same yard, same early-spring day, same
lighting, same Brooks and Sprout clothing, same evergreen shrub.

Sprout has moved to the evergreen shrub. Use a medium shot, closer
than P02. The shrub occupies a substantial portion of the
composition. Show localized winter-damaged evergreen foliage:
believable brown/tan dry-looking foliage concentrated on a more
exposed portion of the shrub, while preserving recognizable woody
structure and less-damaged areas. The plant should look concerning
but not like a completely dead featureless mass. Mulch or bare soil
is visible at the shrub's base, consistent with P01--P02.

Sprout is closest to the shrub and is the visual focus. Her expression
has shifted from delight to puzzled concern. She studies the damaged
foliage carefully, leaning or crouching toward it, gently gesturing
toward it without pulling or breaking anything. Brooks is approaching
or standing behind/beside her with secondary visual weight -- he does
not point at the answer and does not inspect the key bud yet.

Maintain the exact shrub silhouette and damage pattern for use in
subsequent panels.

Reserve clean negative space in the upper-right (or another natural
open area, opposite Sprout's position) and render Sprout's two lines
there, as a short two-line exchange: **Sprout: "Except this one...
Why is it sleeping so long?"**

No generated logo.

## Visual Priority

1.  Sprout notices something wrong
2.  localized brown/tan foliage
3.  visual contrast with the hopeful signs from P02
4.  Brooks remains secondary
5.  Sprout's dialogue

## Reject If

-   the entire shrub becomes uniformly dead;
-   obvious disease or pest symptoms appear;
-   the plant changes species/look from P01;
-   Brooks discovers the clue;
-   dialogue text is missing or doesn't match the script.

------------------------------------------------------------------------

# P04 --- What Do You Notice?

## Output

`S00E01-P04-Draft.png`

1080 × 1350 px, portrait 4:5.

## Prompt

Create the fourth independent portrait illustration with exact
continuity from P01--P03.

Same early-spring yard, same shrub, identical damage pattern, same
lighting and wardrobe. Use an intimate medium two-shot beside the
shrub.

Brooks is crouched or kneeling naturally beside Sprout so that he is
near her conversational eye level. Preserve the fact that Brooks is
much taller when standing through believable body proportions. Brooks
has a calm, open, encouraging expression -- posture communicates
curiosity and respect rather than authority. His canonical notebook
may rest naturally in one hand. If he gestures, it refers generally
to observing the plant and never directly reveals the key viable bud.

Sprout is focused and thoughtful, comparing parts of the shrub. Her
magnifying loupe is ready in her hand. Her attention moves between
Brooks and the plant.

The composition must visually communicate shared investigation:
Brooks guides; Sprout investigates. Keep the brown/tan exposed
foliage visible.

Reserve two separated clean dialogue-safe areas in the upper
composition: a larger one near Brooks for his two lines, and a
smaller one near Sprout for her response. Render: **Brooks: "Maybe.
But let's not guess yet. What do you notice?"** and **Sprout: "The
outside looks brown and dry."**

No generated logo.

## Visual Priority

1.  respectful Brooks/Sprout interaction
2.  shared investigation
3.  shrub evidence
4.  loupe ready for next step
5.  the Brooks/Sprout dialogue exchange

## Reject If

-   Brooks stands towering over Sprout;
-   Brooks points directly at the viable bud;
-   Brooks holds Sprout's loupe;
-   the pose resembles a lecture;
-   relative scale is wrong;
-   badges or wardrobe change;
-   dialogue text is missing, garbled, or misattributed.

------------------------------------------------------------------------

# P05 --- Look Closer

## Output

`S00E01-P05-Draft.png`

1080 × 1350 px, portrait 4:5.

## Prompt

Create the fifth independent portrait illustration with strict
continuity from the previous panels. This is the episode's closest
investigation moment.

Sprout dominates the composition. She leans naturally toward the same
key branch of the evergreen shrub and uses her canonical magnifying
loupe to inspect the damaged foliage and nearby bud area. Her face
shows intense curiosity and concentration, followed by the first hint
that she has noticed something unexpected.

Brooks remains visible behind or beside her, calm and patient,
observing Sprout's investigation without pointing to or revealing the
answer. Show the same brown/tan damaged foliage surrounding the key
branch.

Include a subtle, organic Discovery Frame or magnified observation
inset that visually connects to Sprout's loupe. Inside the enlarged
detail, show damaged foliage and a small, plausible viable bud. The
Discovery Frame must feel like a gentle children's educational
illustration device, not technology -- no HUD, scanner, hologram, neon
interface or futuristic graphics. The viable bud should be visible
enough for an attentive viewer to notice but should not glow, sparkle
or appear magical.

Use minimal dialogue-safe space, since the artwork carries this beat.
Reserve a small clean area for two very short reaction beats and
render: **Sprout: "Hmm... Wait..."**

No generated logo.

## Visual Priority

1.  Sprout's eyes and concentration
2.  loupe
3.  key bud area
4.  Discovery Frame
5.  Brooks quietly supporting
6.  minimal reaction text

## Reject If

-   the bud glows;
-   a futuristic interface appears;
-   an oversized loupe hides Sprout;
-   Brooks points out the clue;
-   the plant suddenly becomes greener;
-   shrub continuity changes;
-   dialogue text overwhelms the investigation moment.

------------------------------------------------------------------------

# P06 --- This Bud Is Alive!

## Output

`S00E01-P06-Draft.png`

1080 × 1350 px, portrait 4:5.

## Prompt

Create the sixth independent portrait illustration with strict
continuity from P01--P05.

Use a close-medium discovery/reaction composition beside the same
evergreen shrub. Sprout has just recognized the viable bud -- she is
delighted and surprised, with the expression of a child who has
genuinely discovered evidence herself. Her canonical magnifying loupe
remains visible. She may gesture carefully toward the key bud-bearing
branch.

The small viable bud must now be clearly readable to the viewer while
remaining botanically plausible. Surrounding brown/tan winter-damaged
foliage remains visible, creating a clear contrast. Do not make the
entire branch green.

Brooks reacts to Sprout's discovery rather than taking control -- he
leans in slightly with a warm, proud, encouraging smile, body
language communicating "you found it." His notebook remains
secondary.

Sprout should hold the strongest narrative and visual position.
Reserve the dominant clean dialogue area for Sprout and a smaller
secondary area for Brooks, and render: **Sprout: "Brooks! This bud is
still alive!"** and **Brooks: "Good eye, Sprout."**

No generated logo.

## Visual Priority

1.  Sprout owns the discovery
2.  viable bud
3.  surrounding damaged foliage
4.  Brooks' supportive reaction
5.  the discovery/response dialogue

## Reject If

-   Brooks discovers or points out the bud first;
-   the plant appears healed;
-   the bud is enormous;
-   magical glow/sparkles appear;
-   the celebration pose is exaggerated;
-   character drift occurs;
-   dialogue text is missing or misattributed.

------------------------------------------------------------------------

# P07 --- Understanding Winter Injury

## Output

`S00E01-P07-Draft.png`

1080 × 1350 px, portrait 4:5.

## Prompt

Create the seventh independent portrait illustration with strict
continuity from the entire episode so far. This is the episode's
dedicated science-explanation panel -- give it noticeably more
breathing room than P06.

Pull back to a medium two-shot, wider than P05/P06, positioned so
that more of the whole evergreen shrub is visible at once: both the
damaged, exposed side established since P03, and a healthier, more
sheltered side of the same plant. This visual contrast is the point
of the panel -- frame the shrub so both conditions read clearly
without needing to be explained by text alone.

Brooks makes a gentle explanatory gesture toward the whole shrub, not
just the bud, with a calm, thoughtful expression; his notebook may be
open. Sprout remains engaged, looking between Brooks and the plant,
not a passive listener. Preserve the same fence, light direction and
seasonal cues established since P01; a little more of the yard's
depth may show again here, consistent with the camera easing back out
toward the episode's close.

Reserve generous, clearly separated dialogue-safe space for a
three-line exchange, and render: **Brooks: "Winter can dry out
exposed parts, even when some of the plant is still alive."**
**Sprout: "So it's not all dead?"** **Brooks: "Not all of it. That's
why we look closely."**

No generated logo.

## Visual Priority

1.  both the damaged and healthier sides of the shrub, visible
    together
2.  Brooks' explanatory gesture
3.  Sprout's engaged attention
4.  the three-line exchange, clearly separated

## Reject If

-   only the damaged side of the shrub is visible (the panel loses
    its visual argument);
-   Brooks stands in a lecture pose;
-   the shrub reads as fully healthy;
-   the three lines are crowded into one bubble or overlap the shrub
    detail.

------------------------------------------------------------------------

# P08 --- Look Before You Decide

## Output

`S00E01-P08-Draft.png`

1080 × 1350 px, portrait 4:5.

## Prompt

Create the eighth and final independent portrait illustration with
exact continuity from the entire episode.

Return to a medium-wide composition beside the same evergreen shrub,
pulling back further than P07 so enough of the yard (fence, a hint of
the stepping-stone path) is visible again to echo P01's opening
image, without literally repeating it. The emotional energy is calmer
than P06/P07.

Brooks and Sprout are together near the plant. Brooks remains near
Sprout rather than using a dominant standing authority pose, making a
gentle gesture toward the shrub with a warm, thoughtful expression.
Sprout looks at the plant with new understanding, her loupe relaxed
in her hand, remaining engaged and active rather than becoming a
passive listener.

The shrub must still visibly contain the same brown/tan
winter-damaged foliage established since P03. Do not show instant
recovery. The viable area discovered earlier remains subtle within
the plant, not spotlighted. Do not depict either character cutting
the plant.

Reserve generous clean negative space for the episode's second-largest
dialogue load: two short separated lines plus a closing caption,
visually distinct from the character dialogue. Render: **Sprout: "So
we shouldn't give up on it yet."** **Brooks: "Exactly. Let's watch
what grows before we decide what to cut."** and, as a distinct closing
caption: **"LOOK CLOSER BEFORE YOU DECIDE."**

No generated logo.

## Visual Priority

1.  Brooks + Sprout shared understanding
2.  the same damaged shrub, unrecovered
3.  a calm care decision
4.  the yard echoing P01
5.  the closing dialogue and caption

## Reject If

-   the shrub is suddenly healthy/green;
-   pruning is already happening;
-   the plant is removed;
-   Brooks lectures from above;
-   Sprout becomes passive;
-   the scene changes location/weather;
-   the closing caption is styled identically to character dialogue
    (it should read as distinct).

------------------------------------------------------------------------

# Global Negative Constraints

Apply across all eight generations: no photorealism; no anime
redesign; no generic 3D movie redesign; no military/police/cowboy/
superhero Brooks; no beard or added hair on Brooks; no circular
replacement badge; no invented Brooks insignia; no extra Lawn With
Care leaves or reconstructed logo; no altered Sprout hair identity; no
older-teenage or toddler Sprout; no generic scout uniform; no
redesigned Discovery Band; no invented permanent badges; no magical
plant effects; no glowing bud; no talking plant; no summer-green
environment; no sudden snowstorm between panels; no watermarks; no
panel borders unless explicitly added in post-production. See
`01-Characters/Brooks/11-Negative-Prompt.md` and
`01-Characters/Sprout/11-Negative-Prompt.md` for the full, maintained
lists.

------------------------------------------------------------------------

# Generation Order

``` text
ENVIRONMENT / YARD / SHRUB REFERENCE (recommended: regenerate/extend
  to also show the healthier shrub side needed for P07, and lock the
  P01/P08 fence + path + leftover-snow layout)
↓
P01 → P02 → P03 → P04 → P05 → P06 → P07 → P08
```

Do not generate all panels independently without reviewing continuity
between them. After each panel: compare Brooks to the Master Model
Sheet; compare Sprout to the Master Model Sheet; compare their scale;
compare shrub/environment continuity; verify the rendered dialogue
matches `04-Script.md` exactly; reject visible canon drift or text
errors; only then proceed.

------------------------------------------------------------------------

# Production Workflow --- Updated for v2.0

``` text
CANON REFERENCES
+
ENVIRONMENT/YARD/SHRUB REFERENCE
+
PANEL BREAKDOWN
+
LOCKED DIALOGUE (04-Script.md)
+
PANEL PROMPT (with dialogue included)
↓
DRAFT GENERATION (art + dialogue together)
↓
VISUAL CANON REVIEW
↓
DIALOGUE ACCURACY REVIEW (wording, spelling, placement)
↓
CONTINUITY REVIEW
↓
APPROVE / REGENERATE / CORRECT TEXT VIA COMPOSITING
↓
MOBILE READABILITY CHECK
↓
FINAL 1080 × 1350 EXPORT
```

The old six-panel workflow separated "clean art" from "lettering" as
two distant stages. This workflow keeps them together from the first
draft, with a correction step still available if the model's
text rendering is unreliable.

------------------------------------------------------------------------

# File Organization

``` text
Assets/
├── References/
├── Drafts/
├── Panels/
│   ├── Clean/        (legacy v1.0 six-panel art; superseded, keep for reference)
│   └── Lettered/      → now: Draft/ (art + baked-in dialogue from first pass)
└── Final/             (post correction-pass exports)
```

------------------------------------------------------------------------

# Visual Approval Checklist

For every generated panel:

## Brooks

-   [ ] Face matches canonical reference (including: bald under the
    hat, no visible hair).
-   [ ] Hat matches canonical reference.
-   [ ] Hat insignia is correct.
-   [ ] Chest insignia is correct.
-   [ ] Wardrobe is correct.
-   [ ] Body proportions are correct.
-   [ ] No invented visual elements.

## Sprout

-   [ ] Face matches canonical reference.
-   [ ] Age reads correctly.
-   [ ] Hair is correct.
-   [ ] Headband is correct.
-   [ ] Wardrobe is correct.
-   [ ] Discovery Band is correct.
-   [ ] Loupe is correct.
-   [ ] Body proportions are correct.

## Relationship

-   [ ] Relative scale is believable.
-   [ ] Sprout has visual agency.
-   [ ] Brooks does not dominate unnecessarily.
-   [ ] Body language supports shared discovery.

## Episode Continuity

-   [ ] Same shrub, same fence/path, same leftover-snow placement.
-   [ ] Same yard, same season.
-   [ ] Compatible lighting.
-   [ ] No unexplained environmental changes.

## Science

-   [ ] Damage looks plausible.
-   [ ] Viable bud is plausible.
-   [ ] Plant does not magically recover.
-   [ ] No competing disease/pest narrative appears.
-   [ ] P07 shows both damaged and healthier shrub areas together.

## Dialogue

-   [ ] Rendered text matches `04-Script.md` wording exactly.
-   [ ] No spelling/rendering errors.
-   [ ] Text is positioned in the planned dialogue-safe area, not
    covering a face or the key clue.
-   [ ] Closing caption (P08) reads as visually distinct from
    character dialogue.

## Production

-   [ ] Portrait 4:5 composition.
-   [ ] No incorrect generated logo.
-   [ ] Panel works independently.
-   [ ] Panel connects visually to the carousel.

------------------------------------------------------------------------

# Next Step

Regenerate or extend the environment/shrub reference to cover the
fence + path + leftover-snow layout (for P01/P08) and the
healthier-side shrub view (for P07), then generate P01--P08 in order.
None of the existing v1.0 six-panel clean art satisfies this
structure directly -- see `03-Story-Blueprint.md`, "Artwork Migration
Note."

------------------------------------------------------------------------

# Status

**READY FOR VISUAL TESTING --- v2.0 (eight-panel revision, dialogue
included in first drafts)**
