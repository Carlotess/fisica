#!/usr/bin/env python3
"""Amplía (y opcionalmente recorta) la figura de un problema de física.

Uso:
    python ampliar.py imagen.png
    python ampliar.py imagen.png --crop x0 y0 x1 y1
    python ampliar.py imagen.png --crop x0 y0 x1 y1 --ancho 1800 --out zoom.png

Por defecto escala la imagen (o el recorte) hasta ~1600 px de ancho con
LANCZOS y aplica un leve realce de nitidez y contraste para que se vean
mejor los extremos de las cuerdas y los ejes de las poleas.
Imprime el tamaño original para poder elegir coordenadas de recorte.
"""
import argparse
import os
import sys

try:
    from PIL import Image, ImageEnhance, ImageFilter
except ImportError:
    sys.exit("Falta Pillow: pip install pillow --break-system-packages")


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("imagen")
    p.add_argument("--crop", nargs=4, type=int, metavar=("X0", "Y0", "X1", "Y1"),
                   help="recorte en píxeles de la imagen original")
    p.add_argument("--ancho", type=int, default=1600,
                   help="ancho final aproximado en px (default 1600)")
    p.add_argument("--out", help="ruta de salida (default: <nombre>_ampliada.png)")
    a = p.parse_args()

    im = Image.open(a.imagen).convert("RGB")
    print(f"Tamaño original: {im.size[0]} x {im.size[1]} px")

    if a.crop:
        im = im.crop(tuple(a.crop))
        print(f"Recorte: {a.crop} -> {im.size[0]} x {im.size[1]} px")

    factor = max(1.0, a.ancho / im.size[0])
    nuevo = (round(im.size[0] * factor), round(im.size[1] * factor))
    im = im.resize(nuevo, Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=2, percent=120, threshold=2))
    im = ImageEnhance.Contrast(im).enhance(1.2)

    base, _ = os.path.splitext(a.imagen)
    sufijo = "_recorte" if a.crop else "_ampliada"
    out = a.out or os.path.join(os.getcwd(), os.path.basename(base) + sufijo + ".png")
    im.save(out)
    print(f"Guardada: {out} ({nuevo[0]} x {nuevo[1]} px, x{factor:.1f})")


if __name__ == "__main__":
    main()
