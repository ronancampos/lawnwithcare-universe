"""
Generate images with Gemini 2.5 Flash Image ("Nano Banana") for the
Lawn With Care Universe.

Usage:
    python3 generate_image.py "prompt text" -o output/path/Brooks-Front-v1.png
    python3 generate_image.py "prompt text" -o out.png -r ref1.png -r ref2.png

Naming convention (06-Studio/04-Asset-Management.md):
    Character-Description-Version.png
"""

import argparse
import os
import sys
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types

MODEL = "gemini-2.5-flash-image"


def main():
    parser = argparse.ArgumentParser(description="Generate an image via Gemini.")
    parser.add_argument("prompt", help="Text prompt describing the image.")
    parser.add_argument("-o", "--output", required=True, help="Output PNG path.")
    parser.add_argument(
        "-r", "--reference", action="append", default=[],
        help="Reference image path (repeatable) for character/style consistency.",
    )
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        sys.exit("GEMINI_API_KEY not set. Add it to .env (see .env.example).")

    client = genai.Client(api_key=api_key)

    contents = [args.prompt]
    for ref_path in args.reference:
        contents.append(
            types.Part.from_bytes(
                data=Path(ref_path).read_bytes(),
                mime_type="image/png",
            )
        )

    response = client.models.generate_content(model=MODEL, contents=contents)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    saved = False
    for part in response.candidates[0].content.parts:
        if part.inline_data:
            out_path.write_bytes(part.inline_data.data)
            saved = True
            print(f"Saved: {out_path}")
        elif part.text:
            print(f"Model note: {part.text}")

    if not saved:
        sys.exit("No image returned. Check the prompt or API response.")


if __name__ == "__main__":
    main()
