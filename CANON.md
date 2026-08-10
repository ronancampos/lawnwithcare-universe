---
title: Lawn With Care Universe — Canon Index
document: Canon
version: 1.0.0
status: CANON
author: Ronan Campos
last_update: 2026-08-10
---

# Canon Index

## Purpose

This file is the entry point required by `PROJECT_CONTEXT.md`'s Authority Hierarchy (level 6, "Canon") and by `CLAUDE.md` / `GEMINI.md`'s required reading list.

It does not restate canon. It points to the documents that define it, organized by authority level, so no collaborator has to search the repository to find the authoritative source for a given decision.

If this index and a linked document ever disagree, the linked document wins — update this index instead of trusting it blindly.

---

## 1. Franchise-level canon

- Vision — `00-Franchise/Vision.md`
- Manifesto — `00-Franchise/Manifesto.md`
- Brand DNA — `00-Franchise/Brand-DNA.md`
- Franchise DNA — `00-Franchise/Franchise-DNA.md`
- Universe Principles — `Universe-Principles.md`
- Architecture — `00-Franchise/Architecture.md`
- Art Direction — `00-Franchise/Art-Direction.md`
- Official brand assets — `00-Franchise/Brand/`

## 2. Character canon

### Brooks

- Identity — `01-Characters/Brooks/00-Identity.md`
- Canon — `01-Characters/Brooks/14-Canon.md`
- Design Rules — `01-Characters/Brooks/15-Design-Rules.md`
- Wardrobe — `01-Characters/Brooks/06-Wardrobe.md`
- Model Sheet spec — `01-Characters/Brooks/05-Model-Sheet.md`
- Prompt Master — `01-Characters/Brooks/10-Prompt-Master.md`
- Dialogue / Voice / Negative Prompt / Relationships — `01-Characters/Brooks/08-Dialogue.md`, `12-Voice.md`, `11-Negative-Prompt.md`, `13-Relationships.md`
- Visual Canon Audit — `01-Characters/Brooks/Assets/References/Audits/Brooks-Visual-Canon-Audit-v1.0.md`
- Master Model Sheet — `01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png`

### Sprout

- Identity — `01-Characters/Sprout/00-Identity.md`
- Canon — `01-Characters/Sprout/14-Canon.md`
- Dialogue / Voice / Negative Prompt / Relationships — `01-Characters/Sprout/08-Dialogue.md`, `12-Voice.md`, `11-Negative-Prompt.md`, `13-Relationships.md`
- Master Model Sheet — `01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png`
- **Gap:** Sprout does not yet have a written `05-Model-Sheet.md`, `06-Wardrobe.md`, `10-Prompt-Master.md`, `15-Design-Rules.md`, or Visual Canon Audit, even though the matching visual asset sheets already exist under `01-Characters/Sprout/Assets/`. Treat those visual assets as approved production references, but do not assume a written rule exists until one of these files is created.

### Brooks + Sprout

- Relationship Canon — `01-Characters/Relationships/Brooks-Sprout/Relationship-Canon.md`
- Relationship / Scale Sheet — `01-Characters/Relationships/Brooks-Sprout/Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png`

## 3. World canon

- World Bible — `02-World/00-World-Bible.md`
- Yard Rangers — `02-World/02-Yard-Rangers.md`
- Discovery System — `02-World/03-Discovery-System.md`
- Discovery Badges — `02-World/04-Badges.md`
- Field Equipment — `02-World/05-Field-Equipment.md`
- **Gap:** `02-World/01-Locations.md` is empty.

## 4. Storytelling canon

- Storytelling DNA (emotional structure / narrative rhythm) — `Storytelling-DNA.md`
- Story Bible — `03-Storytelling/00-Story-Bible.md`
- Episode Structure — `03-Storytelling/01-Episode-Structure.md`
- Writers' Room Guide — `03-Storytelling/10-Writer-Room-Guide.md`
- **Gap:** `03-Storytelling/02-Dialogue.md` through `09-Season-Structure.md` (Dialogue, Humor, Educational Framework, Pacing, Discovery Moments, Narration, Panel Language, Season Structure) are empty. This matches the ~25% Storytelling completion tracked in `PROJECT_STATUS.md`.

## 5. Production / operating rules

- `AGENTS.md` — repository agent operating manual; governs how AI and coding agents work in this repository (canon-change policy, git safety, approval boundaries)
- Episode pipeline (per episode) — `13-Episodes/<Season>/<Episode>/01-Concept.md` through the episode's final production documents

## 6. Publishing / marketing

- `07-Marketing/01-Instagram-Guidelines.md` — account setup, caption voice and formula, hashtag strategy, publishing checklist. `APPROVED` operational guidance, not franchise canon; must stay consistent with `Storytelling-DNA.md`'s tone.

---

## Known gaps — do not silently fill

The following are empty by omission, not by accident, and are tracked for a future "Deferred Consolidation" pass referenced in `PROJECT_CONTEXT.md`:

- Root `STYLEGUIDE.md`, `TODO.md`
- `00-Franchise/Canon-Rules.md`, `Color-System.md`, `Shape-Language.md`, `Timeline.md`
- `02-World/01-Locations.md`
- `03-Storytelling/02-Dialogue.md` through `09-Season-Structure.md`, `CHANGELOG.md`, `README.md`

If a task depends on one of these, treat the subject as **NOT DEFINED** and propose an option explicitly — do not infer a plausible answer and proceed as if it were canon.

---

Status: CANON v1.0 — index only, does not itself define new canon.
