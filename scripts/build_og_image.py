#!/usr/bin/env python3
# SPDX-License-Identifier: EUPL-1.2
"""Génère l'image de partage par défaut du portail (Open Graph, 1200 × 630 px) avec Chrome headless.

Elle sert aux pages sans image propre (voir overrides/main.html) ; les pages du livre blanc gardent
la leur. Mise en page aux couleurs de la couverture du livre blanc, police Inter du portail.

Usage :
    python3 scripts/build_og_image.py      # écrit docs/assets/og/og-portail.png

La variable d'environnement CHROME permet d'imposer le binaire du navigateur.
"""

import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "docs/assets/og/og-portail.png"
FONTS = ROOT / "docs/assets/fonts/inter"
LOGO = ROOT / "docs/assets/logo-vertical-dark.svg"

HTML = """<!doctype html>
<html lang="fr"><head><meta charset="utf-8"><style>
@font-face {{ font-family: Inter; font-weight: 400; src: url("{fonts}/inter-latin-400-normal.woff2"); }}
@font-face {{ font-family: Inter; font-weight: 700; src: url("{fonts}/inter-latin-700-normal.woff2"); }}
@font-face {{ font-family: Inter; font-weight: 800; src: url("{fonts}/inter-latin-800-normal.woff2"); }}
html, body {{ margin: 0; width: 1200px; height: 630px; overflow: hidden; }}
body {{ display: flex; align-items: center; gap: 56px; box-sizing: border-box; padding: 0 80px;
        background: #0b1120; color: #f8fafc; font-family: Inter, sans-serif; }}
img {{ flex: none; width: 300px; height: 300px; }}
.kicker {{ margin: 0 0 22px; color: #38bdf8; font-size: 22px; font-weight: 700; letter-spacing: 0.2em;
           text-transform: uppercase; }}
h1 {{ margin: 0; font-size: 60px; font-weight: 800; line-height: 1.08; letter-spacing: -0.02em; }}
.bar {{ width: 96px; height: 7px; margin: 30px 0 28px; background: #fbbf24; }}
.lead {{ margin: 0; color: #cbd5e1; font-size: 26px; line-height: 1.45; }}
.url {{ margin: 26px 0 0; color: #94a3b8; font-size: 22px; }}
</style></head><body>
<img src="{logo}" alt="">
<div>
  <p class="kicker">Portail de l'association</p>
  <h1>Open Trusted Service Provider Initiative</h1>
  <div class="bar"></div>
  <p class="lead">Statuts, gouvernance, livre blanc et socle de conformité des services de confiance eIDAS 2.0</p>
  <p class="url">about.otspi.org</p>
</div>
</body></html>
"""


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for candidate in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser"):
        path = shutil.which(candidate)
        if path:
            return path
    sys.exit("Chrome ou Chromium introuvable : définir la variable d'environnement CHROME.")


def main():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as work:
        page = Path(work) / "og.html"
        page.write_text(HTML.format(fonts=FONTS.as_uri(), logo=LOGO.as_uri()), encoding="utf-8")
        subprocess.run(
            [find_chrome(), "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--user-data-dir={work}/profile",
             "--window-size=1200,630", "--virtual-time-budget=3000", f"--screenshot={OUTPUT}", page.as_uri()],
            check=True, capture_output=True, timeout=120,
        )
    print(f"Image générée : {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
