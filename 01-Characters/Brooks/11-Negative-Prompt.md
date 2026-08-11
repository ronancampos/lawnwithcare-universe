---
title: Brooks Negative Prompt
character: Brooks
universe: Lawn With Care Universe
document: Negative Prompt
version: 1.1.0
status: CONTROLLED
author: Ronan Campos
creative_direction: OpenAI ChatGPT
last_update: 2026-08-11
---

# Brooks

# Negative Prompt

## Purpose

Consolidates known AI generation failure modes and prohibited visual directions for Brooks into one reusable reference. First compiled from `13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/06-Visual-Prompts.md` and `Assets/References/Audits/Brooks-Visual-Canon-Audit-v1.0.md`, so future episodes don't have to reconstruct this list from scratch.

This is a production tool, not canon. If a rule here and `14-Canon.md` / `15-Design-Rules.md` disagree, the canon/design-rules documents win — update this file to match.

---

## Do Not Generate

- Military, tactical, police, cowboy or superhero styling.
- Beard, mustache, stubble or added hairstyle. Brooks' face canon requires "no visible hairstyle when hat is worn" (Visual Canon Audit, Face: APPROVED).
- Freckles on Brooks — freckles are Sprout's trait (`Sprout/11-Negative-Prompt.md`), never his; a shared reference-image context can bleed this across characters.
- A necktie or any neckwear — not part of the approved wardrobe (`06-Wardrobe.md`); has appeared as an AI invention when the jacket is described without explicitly ruling it out.
- Circular replacement badge or generic ranger badge.
- Invented Brooks insignia, or an additional maple-leaf chest pin — explicitly marked `NOT CANON` in the Visual Canon Audit. This includes the "Pin – Maple Leaf (Right Chest)" shown on `Assets/Icons/Brooks-Insignia-Icons-Sheet-v1.0.png`: that sheet was never corrected after the audit rejected the pin, so do not treat it as a generation reference.
- Extra Lawn With Care leaves, or a redrawn/reconstructed Lawn With Care logo.
- Authoritarian posture: standing over a child, lecture pose, finger-wagging.
- Brooks pointing directly at a clue before the child protagonist has found it.
- Brooks holding a tool that canonically belongs to his scene partner (e.g. Sprout's magnifying loupe).
- Watermarks or panel borders, unless a specific production step explicitly calls for them.
- AI-rendered final dialogue, captions or logos baked into artwork.

## Known Recurring Failure Modes

(from the Visual Canon Audit)

**Logo drift** — leaf count, frame geometry, typography, spacing, colors. **Suspected root cause (found 2026-08-11, S00E02 production):** prompts wrote this mark as literal `[L]` text. Square brackets around a letter read to the model as a design instruction — "draw a bracketed L" — rather than as shorthand for the official icon asset (a leaf shape above a serif L inside an open-top frame; see `00-Franchise/Brand/Logos/04-icon-dark.png`). Always spell out "the official Lawn With Care icon" in prose instead of typing `[L]`, and describe its actual construction. See `13-Episodes/Season-00-Pilots/S00E02-Why-Does-the-Ground-Need-to-Breathe/03-Codex-Draft-Generation-Brief.md` ("Icon wording fix") for the corrected phrasing this produced.

**Badge drift** — shield shape, circular badge, text, maple-leaf size, border treatment.

**Prop invention** — plausible but unapproved equipment (e.g. weather meter, pruning shears, measuring tape appearing without separate canon confirmation).

**Character drift** — face width, eye size, body proportions, hat dimensions, boot style.

## Reject If

(generalized from S00E01's per-panel "Reject If" lists for reuse across episodes)

- The scene/environment is inconsistent with the episode's locked environment reference.
- Brooks leads or announces a discovery instead of the child protagonist.
- Brooks' badges or wardrobe drift from the Master Model Sheet.
- AI-generated text appears anywhere in the image (except deliberate, legible educational labels inside a Discovery Frame diagram, e.g. soil-type callouts — approved exception, S00E02 P05, 2026-08-11; garbled or unintended text is still a reject).

---

## Related Documents

- `14-Canon.md` — "Brooks Prohibited Drift"
- `15-Design-Rules.md`
- `Assets/References/Audits/Brooks-Visual-Canon-Audit-v1.0.md`

---

Status: CONTROLLED v1.0 — update whenever a new recurring failure mode is identified in production.
