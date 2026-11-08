#!/usr/bin/env python3
"""Make web-sized copies of the original photos in photos/ for the site.

Crops each chosen photo to the shape it is shown at, saves a large and a
small JPEG in assets/img/, and drops all metadata (including any GPS data).

    python3 tools/photos.py
"""
from pathlib import Path
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent.parent
SRC, OUT = ROOT / "photos", ROOT / "assets" / "img"

# Cropped photos used outside the gallery.
# output name: (source file, aspect w/h, vertical focus 0=top..1=bottom, horizontal focus)
PHOTOS = {
    "table-round":   ("WhatsApp Image 2026-11-08 at 7.58.22 AM26.jpeg", 4 / 5, 0.5, 0.5),
}

# Events page gallery, in display order. Each becomes event-NN.jpg (1200px) and event-NN-sm.jpg (600px).
GALLERY = [
    "WhatsApp Image 2026-11-08 at 7.58.20 AM12.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.22 AM26.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.20 AM13.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.21 AM09.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.24 AM.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.22 AM07.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.23 AM04.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.19 AM14.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.23 AM.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.21 AM11.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.21 AM10.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.23 AM02.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.22 AM08.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.23 AM05.jpeg",
    "WhatsApp Image 2026-11-08 at 7.58.23 AM03.jpeg",
]
SIZES = {"": 1600, "-sm": 800}


def crop(im, aspect, fy, fx):
    w, h = im.size
    if w / h > aspect:            # too wide: trim sides
        nw = round(h * aspect)
        x = round((w - nw) * fx)
        return im.crop((x, 0, x + nw, h))
    nh = round(w / aspect)        # too tall: trim top/bottom
    y = round((h - nh) * fy)
    return im.crop((0, y, w, y + nh))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    for name, (src, aspect, fy, fx) in PHOTOS.items():
        im = ImageOps.exif_transpose(Image.open(SRC / src)).convert("RGB")
        im = crop(im, aspect, fy, fx)
        for suffix, width in SIZES.items():
            if aspect < 1:            # portrait photos are shown in a narrow column
                width = {"": 1000, "-sm": 600}[suffix]
            out = im.copy()
            if out.width > width:
                out = out.resize((width, round(width / aspect)), Image.LANCZOS)
            path = OUT / f"{name}{suffix}.jpg"
            out.save(path, "JPEG", quality=78, optimize=True, progressive=True)
            print(f"{path.relative_to(ROOT)}  {out.width}x{out.height}  {path.stat().st_size // 1024} KB")

    for i, src in enumerate(GALLERY, 1):
        im = ImageOps.exif_transpose(Image.open(SRC / src)).convert("RGB")
        for suffix, width in {"": 1200, "-sm": 600}.items():
            out = im.copy()
            out.thumbnail((width, width * 2), Image.LANCZOS)
            path = OUT / f"event-{i:02d}{suffix}.jpg"
            out.save(path, "JPEG", quality=78, optimize=True, progressive=True)
        print(f"event-{i:02d}  {im.width}x{im.height}")


if __name__ == "__main__":
    main()
