---
title: S00E02 Production Checklist
episode: S00E02
status: FIRST DEFINITIVE CUT APPROVED
last_update: 2026-08-11
---

# Production Checklist

**Legend:** a checked box means the pipeline stage's document is
complete --- not that the project owner has given final creative
sign-off.

- [x] Concept & Learning Objective complete --- `01-Concept-and-Learning-Objective.md`, status `SCIENCE LOCK`
- [x] Story Blueprint & Script complete --- `02-Story-Blueprint-and-Script.md`, status `SCRIPT LOCK`
- [x] Codex Draft Generation Brief complete --- `03-Codex-Draft-Generation-Brief.md`, status `READY FOR EXECUTION`
- [ ] Environment reference generated as its own file (`Assets/References/S00E02-Environment-Reference-v1.0.png`) --- never saved separately; production went straight to panel generation, using P01 as the de facto environment lock instead. Not blocking so far, but do this properly before a S00E03 brief copies the same shortcut.
- [x] Draft assets generated --- P01 through P08 (`Assets/Drafts/`).
- [x] Draft assets reviewed against QA assertions --- P01--P08 (see per-panel notes below).
- [x] Final assets approved and promoted to `Assets/Final/` --- **all 8 panels promoted 2026-08-11.**
- [ ] Social assets prepared per `07-Marketing/01-Instagram-Guidelines.md` --- caption drafted (`Assets/Social/S00E02-Instagram-Caption.md`, status `DRAFT`); panel export/crop for the actual post still pending

## Promoted-to-Final Notes (2026-08-11)

| Panel | Source draft | Status |
|---|---|---|
| P01 | `S00E02-p01.png` | Clean pass. |
| P02 | `S00E02-p02.png` (corrected version --- tie/freckles/chest-pin removed, badge isolated to sleeve) | Clean pass after 1 regeneration. |
| P03 | `S00E02-p03.png` | Clean pass. |
| P04 | `S00E02-P04.png` | Clean pass. |
| P05 | `S00E02-P05.png` | Passed with one accepted, documented exception: Discovery Frame carries unrequested but legible "COMPACTED SOIL" / "HEALTHY LAWN SOIL" labels --- owner-approved, see `01-Characters/Brooks/11-Negative-Prompt.md` and `01-Characters/Sprout/11-Negative-Prompt.md`. |
| P06 | `S00E02-P06.3.png` | Clean pass after 3 regenerations. Fixed in order: a third arm/extra hand holding the loupe (anatomy error), the "healthy soil" hand landing on a disconnected second bare patch instead of the established path, then Sprout's gaze pointing away from her own discovery instead of down at it. |
| P07 | `S00E02-P07.1.png` | **Accepted with a known, documented imperfection:** faint freckle-like texture on Brooks' cheek, visible on close crop, survived two regeneration attempts (`S00E02-P07.png`, `S00E02-P07.1.png`) despite explicit "no freckles" instructions reinforced both times. Composition, dialogue, marks placement, and the required worn-strip/healthy-lawn contrast are all otherwise correct. Precedent: S00E01 accepted P03's illegible sleeve-badge text the same way (`S00E01/08-Retrospective-Notes.md`, "First Definitive Cut Approved"). If the owner wants zero-tolerance instead, this needs a fourth regeneration attempt or a compositing/inpainting fix rather than another plain prompt retry, since two text-only retries already failed to fully suppress it. |
| P08 | `S00E02-P08.2.png` | Clean pass, no regenerations needed beyond the owner's own first two local iterations. Brooks' face re-checked closely given the P07 freckle history --- clean this time. |

---

Related: `13-Episodes/Season-00-Pilots/S00E01-Why-Is-It-Sleeping-So-Long/08-Retrospective-Notes.md` documents the pipeline lessons this episode's Codex brief already applies (single resolved prompt per panel, explicit reference roles, `DRAFT_MATCH_MASTER` mode).
