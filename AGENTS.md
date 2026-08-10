---
project: Lawn With Care Universe
document: Agent Instructions
version: 1.0.0
status: ACTIVE
last_update: 2026-08-09
---

# AGENTS.md

## Purpose

This file defines how coding agents, repository agents and AI-assisted development tools must work inside the Lawn With Care Universe repository.

The goal is to preserve:

- canon;
- visual consistency;
- brand integrity;
- repository structure;
- production discipline;
- traceability of changes.

Agents may assist with implementation.

Agents do not have authority to redefine the franchise.

---

# 1. Core Principle

**Execute approved decisions. Do not invent canon.**

The repository contains creative canon, visual references, production rules, story systems, brand assets and AI workflow documentation.

When uncertainty exists:

**preserve existing material and report the ambiguity.**

Do not silently resolve creative uncertainty.

---

# 2. Repository Authority

The repository is the source of truth for the Lawn With Care Universe.

Before changing a file:

1. read the relevant local documentation;
2. identify related canon documents;
3. identify dependencies and references;
4. preserve established terminology;
5. avoid creating conflicting rules.

Do not rely on assumptions when repository documentation already exists.

---

# 3. Canon Authority

Agents must distinguish between:

- CANON;
- APPROVED PRODUCTION REFERENCE;
- CONTROLLED;
- OPTIONAL / STORY-SPECIFIC;
- IN REVIEW;
- NON-CANON / EXPLORATION.

Never promote an element to CANON merely because it appears in:

- an AI-generated image;
- a draft;
- a prompt;
- a concept sheet;
- an experimental file;
- a temporary production asset.

Canon changes require explicit approval.

---

# 4. Canon Change Rule

Do not modify canon-defining content unless the task explicitly requests a canon update.

Examples include:

- character identity;
- character age;
- personality;
- relationships;
- visual identity;
- official wardrobe;
- core props;
- badge systems;
- franchise philosophy;
- world rules;
- story rules.

If a requested change appears to affect canon but approval is unclear:

**stop and report the conflict.**

Do not guess.

---

# 5. Character Authority

Each character may have:

- Identity;
- Visual DNA;
- Character Guide;
- Expressions;
- Poses;
- Model Sheet;
- Wardrobe;
- Props;
- Dialogue;
- Animation;
- Prompt Master;
- Negative Prompt;
- Voice;
- Relationships;
- Canon;
- Design Rules;
- Asset folders.

Agents must preserve this hierarchy.

Do not merge specialized documents unless explicitly requested.

---

# 6. Master Visual Reference Rule

When a character has an approved Master Model Sheet, it is the primary visual implementation reference.

For Ranger Brooks:

`01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png`

For Sprout:

`01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png`

Generated visual assets must not override these references.

If a generated asset conflicts with the Master Model Sheet:

**the generated asset is wrong unless a canon revision explicitly says otherwise.**

---

# 7. Brooks Canon Controls

Ranger Brooks core visual identity includes:

- campaign hat;
- forest-green field uniform;
- official Lawn With Care `[L]` brand identifier;
- Yard Ranger Canada badge;
- dark outdoor boots;
- notebook;
- pencil;
- calm and approachable visual language.

Brooks must not drift into:

- military styling;
- tactical styling;
- superhero styling;
- authoritarian posture;
- aggressive visual language.

Refer to Brooks' written canon before making character-level changes.

---

# 8. Sprout Canon Controls

Sprout core visual identity includes:

- approximately 9 years old;
- approximately 130–135 cm tall;
- golden curly blonde hair;
- light-green eyes;
- freckles;
- green headband;
- cream field shirt;
- olive-green shorts;
- brown outdoor boots;
- Discovery Band;
- magnifying loupe;
- curious, warm and capable visual language.

Do not change:

- age presentation;
- core proportions;
- hair identity;
- Discovery Band identity;
- signature prop;
- core outfit

without explicit approval.

---

# 9. Brooks + Sprout Relationship Canon

Primary relationship reference:

`01-Characters/Relationships/Brooks-Sprout/Relationship-Canon.md`

Shared visual reference:

`Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png`

Core rule:

**Brooks guides. Sprout discovers.**

Brooks must not dominate every discovery.

Sprout must retain agency.

Their relationship should communicate:

- trust;
- curiosity;
- mutual respect;
- learning;
- shared exploration;
- care.

---

# 10. Official Brand Assets

Official Lawn With Care brand assets are stored under:

`00-Franchise/Brand/`

These files are authoritative.

Do not recreate or redraw official logos.

Do not alter:

- leaf count;
- typography;
- frame geometry;
- spacing;
- colors;
- proportions;
- slogan construction.

Cropping excess empty border space may be acceptable.

Changing internal artwork is not.

---

# 11. Brand Reproduction Rule

AI-generated logos are not official brand assets.

When exact branding is required:

1. use the official source asset;
2. preserve its geometry;
3. composite it into final artwork when necessary;
4. verify placement and scale.

Never treat an AI approximation as authoritative.

---

# 12. Asset Naming Convention

Prefer:

`Character-Asset-Type-vX.Y.ext`

Examples:

`Brooks-Master-Model-Sheet-v1.0.png`

`Brooks-Expression-Sheet-v1.0.png`

`Sprout-Color-Sheet-v1.0.png`

`Brooks-Sprout-Relationship-Scale-Sheet-v1.0.png`

Avoid:

- spaces in filenames;
- ambiguous names;
- duplicate extensions;
- generic names such as `final.png`;
- inconsistent capitalization.

Use hyphens for filename separation.

---

# 13. Directory Naming

Prefer predictable, stable directories.

Examples:

`Model-Sheets/`

`Expressions/`

`Poses/`

`Wardrobe/`

`Props/`

`Color/`

`Icons/`

`Materials/`

`References/`

`Audits/`

Do not rename established directories without explicit reason.

Do not introduce alternate folders for the same asset category.

---

# 14. Repository Structure Rule

Preserve the existing top-level architecture.

Major folders include:

- `00-Franchise/`
- `01-Characters/`
- `02-World/`
- `03-Storytelling/`
- `04-Art/`
- `05-AI/`
- `06-Studio/`
- `07-Marketing/`
- `08-Comics/`
- `09-Assets/`
- `10-References/`
- `11-Templates/`
- `12-Lore/`
- `13-Episodes/`

Do not reorganize major sections automatically.

Structural migrations require explicit approval.

---

# 15. Markdown Rules

When editing `.md` files:

- preserve front matter;
- preserve document status;
- preserve terminology;
- preserve heading hierarchy;
- avoid unnecessary rewrites;
- avoid replacing a strong existing document when a targeted amendment is enough.

Prefer surgical edits over full rewrites.

---

# 16. Versioning Rules

Use semantic-style versioning when appropriate.

Examples:

`v1.0`

`v1.1`

`v2.0`

Minor revision:

- controlled clarification;
- correction;
- non-destructive expansion.

Major revision:

- material redesign;
- canon-level change;
- structural change.

Do not overwrite historical versioned assets merely to replace them with a new generation.

---

# 17. Git Branch Rule

Primary production branch:

`production/v0.2.0`

Before making changes:

```bash
git status