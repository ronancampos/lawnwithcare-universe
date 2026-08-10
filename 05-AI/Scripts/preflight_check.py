"""
Preflight checks for an image-generation call, run BEFORE spending an
API call on it. Catches the exact failure classes that caused repeated
rework on S00E01: stale/contradictory prompt language, more than one
reference image containing the same character, and accidental
overwrite of an approved output.

This does not call any generation API. It only inspects the prompt
text and the reference file list you're about to pass to
generate_image.py / generate_image_local.py.

Usage:
    python3 preflight_check.py --mode DRAFT_MATCH_MASTER \\
      --prompt-file prompt.txt \\
      --ref 01-Characters/Brooks/Assets/Model-Sheets/Brooks-Master-Model-Sheet-v1.0.png \\
      --ref 01-Characters/Sprout/Assets/Model-Sheets/Sprout-Master-Model-Sheet-v1.0.png \\
      --output 13-Episodes/.../Assets/Drafts/S00E01-P04-Draft.png

Exits non-zero (and prints every problem found) if any check fails.
"""

import argparse
import sys
from pathlib import Path

# Phrases that must NOT appear in a DRAFT_MATCH_MASTER prompt -- these
# are exactly the "hide the branding" instructions that fought the
# Master Model Sheet reference across Rounds 2-5 of S00E01.
FORBIDDEN_IN_DRAFT_MATCH_MASTER = [
    "completely plain",
    "unbranded",
    "do not render the lawn with care logo",
    "no icon, letter, emblem",
    "no branding",
]

# Phrases that signal someone is trying to free-hand the exact logo in
# a mode that should instead reserve the area for compositing.
FORBIDDEN_IN_FINAL_BRAND_EXACT = [
    "reproduce the lawn with care [l] icon",
    "draw the lawn with care logo",
    "render the [l] icon exactly",
]

# Reference filename fragments that identify "this image contains
# Brooks" / "this image contains Sprout", used for the single-character
# -r rule. Extend this list if new multi-character sheets are added.
BROOKS_MARKERS = ["brooks-master-model-sheet", "relationship-scale-sheet", "brooks-unbranded"]
SPROUT_MARKERS = ["sprout-master-model-sheet", "relationship-scale-sheet"]


def check_prompt_language(prompt: str, mode: str) -> list[str]:
    problems = []
    lowered = prompt.lower()
    forbidden = FORBIDDEN_IN_DRAFT_MATCH_MASTER if mode == "DRAFT_MATCH_MASTER" else FORBIDDEN_IN_FINAL_BRAND_EXACT
    for phrase in forbidden:
        if phrase in lowered:
            problems.append(f'Prompt contains "{phrase}", which contradicts mode {mode}.')
    return problems


def check_reference_files(refs: list[str]) -> list[str]:
    problems = []
    for ref in refs:
        if not Path(ref).is_file():
            problems.append(f"Reference file does not exist: {ref}")
    return problems


def check_single_character_rule(refs: list[str]) -> list[str]:
    problems = []
    lowered_refs = [r.lower() for r in refs]

    def count_matches(markers):
        return sum(1 for r in lowered_refs for m in markers if m in r)

    brooks_count = count_matches(BROOKS_MARKERS)
    sprout_count = count_matches(SPROUT_MARKERS)
    if brooks_count > 1:
        problems.append(
            f"{brooks_count} reference images contain a Brooks depiction "
            "(expected at most 1) -- competing references cause drift."
        )
    if sprout_count > 1:
        problems.append(
            f"{sprout_count} reference images contain a Sprout depiction "
            "(expected at most 1) -- competing references cause drift."
        )
    return problems


def check_output_collision(output: str) -> list[str]:
    if output and Path(output).is_file():
        return [f"Output path already exists and will be overwritten: {output} (confirm this is intended)"]
    return []


def main():
    parser = argparse.ArgumentParser(description="Preflight-check a generation prompt before spending an API call.")
    parser.add_argument("--mode", choices=["DRAFT_MATCH_MASTER", "FINAL_BRAND_EXACT"], required=True)
    parser.add_argument("--prompt-file", help="Path to a text file containing the exact prompt.")
    parser.add_argument("--prompt", help="Inline prompt text (alternative to --prompt-file).")
    parser.add_argument("--ref", action="append", default=[], help="Reference image path (repeatable).")
    parser.add_argument("--output", help="Intended output path, to check for accidental overwrite.")
    args = parser.parse_args()

    if not args.prompt_file and not args.prompt:
        sys.exit("Provide --prompt-file or --prompt.")
    prompt_text = Path(args.prompt_file).read_text() if args.prompt_file else args.prompt

    problems = []
    problems += check_prompt_language(prompt_text, args.mode)
    problems += check_reference_files(args.ref)
    problems += check_single_character_rule(args.ref)
    problems += check_output_collision(args.output)

    if problems:
        print("PREFLIGHT FAILED:")
        for p in problems:
            print(f"  - {p}")
        sys.exit(1)

    print(f"PREFLIGHT OK ({args.mode}, {len(args.ref)} reference(s) checked).")


if __name__ == "__main__":
    main()
