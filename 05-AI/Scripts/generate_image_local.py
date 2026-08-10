"""
Generate images locally and for free via Draw Things' HTTP API
(Automatic1111-compatible txt2img endpoint), running on this Mac.

Requires Draw Things open with Settings > Advanced > API Server:
    Server Online: on
    Protocol: HTTP
    Port: 7859 (default used below)

Usage:
    python3 generate_image_local.py "prompt text" -o output/path/Brooks-Front-v1.png
    python3 generate_image_local.py "prompt" -o out.png -n "custom negative prompt"

    # img2img, using an existing reference image as a visual anchor:
    python3 generate_image_local.py "prompt" -o out.png -r reference.png -d 0.6
"""

import argparse
import base64
import io
import sys
from pathlib import Path

import requests
from PIL import Image

DEFAULT_NEGATIVE = (
    "photorealistic, anime, manga, cel shading, comic book ink style, "
    "harsh lighting, dramatic horror lighting, superhero pose, "
    "exaggerated perspective, aggressive gesture, crossed arms, scary expression"
)


def main():
    parser = argparse.ArgumentParser(description="Generate an image via local Draw Things API.")
    parser.add_argument("prompt", help="Text prompt describing the image.")
    parser.add_argument("-o", "--output", required=True, help="Output PNG path.")
    parser.add_argument("-n", "--negative", default=DEFAULT_NEGATIVE, help="Negative prompt.")
    parser.add_argument("-p", "--port", type=int, default=7859, help="Draw Things API port.")
    parser.add_argument("--width", type=int, default=1024)
    parser.add_argument("--height", type=int, default=1024)
    parser.add_argument("--steps", type=int, default=30)
    parser.add_argument("--seed", type=int, default=-1, help="-1 for random.")
    parser.add_argument(
        "-r", "--reference", help="Reference image path for img2img (character continuity)."
    )
    parser.add_argument(
        "-d", "--denoise", type=float, default=0.6,
        help="img2img denoising strength 0-1. Lower = closer to reference, "
             "higher = more freedom to follow the prompt. Default 0.6.",
    )
    args = parser.parse_args()

    payload = {
        "prompt": args.prompt,
        "negative_prompt": args.negative,
        "width": args.width,
        "height": args.height,
        "steps": args.steps,
        "seed": args.seed,
    }

    if args.reference:
        url = f"http://127.0.0.1:{args.port}/sdapi/v1/img2img"

        ref_img = Image.open(args.reference).convert("RGB")
        target_long_side = max(args.width, args.height)
        scale = target_long_side / max(ref_img.size)
        new_w = round(ref_img.width * scale / 8) * 8
        new_h = round(ref_img.height * scale / 8) * 8
        ref_img = ref_img.resize((new_w, new_h), Image.LANCZOS)

        buf = io.BytesIO()
        ref_img.save(buf, format="PNG")
        ref_b64 = base64.b64encode(buf.getvalue()).decode("utf-8")

        payload["init_images"] = [ref_b64]
        payload["denoising_strength"] = args.denoise
        payload["width"] = new_w
        payload["height"] = new_h
    else:
        url = f"http://127.0.0.1:{args.port}/sdapi/v1/txt2img"

    try:
        response = requests.post(url, json=payload, timeout=300)
        response.raise_for_status()
    except requests.exceptions.ConnectionError:
        sys.exit(
            f"Could not reach Draw Things at {url}. "
            "Is the app open with Server Online enabled?"
        )
    except requests.exceptions.HTTPError as e:
        sys.exit(f"Draw Things returned an error: {e}\n{response.text}")

    data = response.json()
    images = data.get("images", [])
    if not images:
        sys.exit(f"No image returned. Response: {data}")

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_bytes(base64.b64decode(images[0]))
    print(f"Saved: {out_path}")


if __name__ == "__main__":
    main()
