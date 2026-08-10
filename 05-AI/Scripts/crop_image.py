"""
Crop a single-character (or single-region) operational reference out of
a larger contact sheet / turnaround / model sheet, so it can be used as
clean image-generation conditioning without competing depictions of
other characters or conflicting annotations bleeding into the prompt.

Master Model Sheets, relationship sheets, and environment "contact
sheets" are great for humans (they document proportions, palettes,
turnarounds, size comparisons side by side) but bad as direct -r inputs
to a generator: every figure/annotation on the sheet is an equally
strong signal, so a sheet with five poses of a character can behave
like five different, slightly-inconsistent references at once.

Usage:
    python3 crop_image.py SHEET.png -o CROP.png -x 280 -y 190 -w 520 -h 640

    -x/-y: top-left corner of the crop, in pixels, on the source image.
    -w/-h: crop width/height, in pixels.
    As with composite_logo.py, there's no auto-detection -- read the
    coordinates off the actual source image first (e.g. open it and use
    your viewer's pixel readout), since a wrong guess silently produces
    a bad reference that's worse than not cropping at all.
"""

import argparse
from pathlib import Path

from PIL import Image


def main():
    parser = argparse.ArgumentParser(description="Crop an operational reference out of a larger sheet.")
    parser.add_argument("source", help="Source sheet/turnaround/contact-sheet PNG.")
    parser.add_argument("-o", "--output", required=True, help="Output PNG path.")
    parser.add_argument("-x", type=int, required=True, help="Left position in pixels on the source image.")
    parser.add_argument("-y", type=int, required=True, help="Top position in pixels on the source image.")
    parser.add_argument("-w", "--width", type=int, required=True, help="Crop width in pixels.")
    parser.add_argument("-H", "--height", type=int, required=True, help="Crop height in pixels.")
    args = parser.parse_args()

    source = Image.open(args.source).convert("RGBA")
    box = (args.x, args.y, args.x + args.width, args.y + args.height)
    crop = source.crop(box)

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    crop.convert("RGB").save(out_path)
    print(f"Saved: {out_path} (cropped {args.width}x{args.height} from {args.x},{args.y})")


if __name__ == "__main__":
    main()
