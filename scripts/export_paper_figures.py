#!/usr/bin/env python3
"""Export tightly cropped figures from the GCPR camera-ready paper.

Requires Poppler (pdftoppm) and ImageMagick (convert). Coordinates are in PDF
points, measured on static/pdfs/mess-gcpr2026.pdf; they exclude page headers,
body text, and captions, which the website supplies as accessible HTML.
Run from any directory: python3 scripts/export_paper_figures.py
"""
from pathlib import Path
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / 'static/pdfs/mess-gcpr2026.pdf'
DPI = 600
# Name, one-based page, and crop rectangle (left, top, right, bottom).
FIGURES = [
    ('coverfigure', 2, (130, 110, 485, 220)),
    ('method', 5, (130, 110, 485, 309)),
    ('aginpaint', 9, (193, 110, 303, 176)),
    ('gcalign', 9, (313, 110, 422, 176)),
    ('comparison', 11, (130, 110, 485, 413)),
    ('lod3', 12, (150, 110, 470, 251)),
]


def main():
    with tempfile.TemporaryDirectory(prefix='mess-paper-figures-') as tmp:
        for name, page, (left, top, right, bottom) in FIGURES:
            x, y, end_x, end_y = [round(v * DPI / 72) for v in (left, top, right, bottom)]
            prefix = Path(tmp) / name
            subprocess.run([
                'pdftoppm', '-f', str(page), '-l', str(page), '-singlefile',
                '-r', str(DPI), '-x', str(x), '-y', str(y),
                '-W', str(end_x - x), '-H', str(end_y - y), '-png',
                str(PAPER), str(prefix),
            ], check=True)
            destination = ROOT / f'static/images/{name}.png'
            subprocess.run([
                'convert', str(prefix.with_suffix('.png')), '-fuzz', '1%',
                '-trim', '+repage', '-resize', '2400x2400>',
                '-bordercolor', 'white', '-border', '6', '-strip',
                str(destination),
            ], check=True)
            print(destination.relative_to(ROOT))


if __name__ == '__main__':
    main()
