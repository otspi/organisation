#!/usr/bin/env python3
"""Génère les PDF de référence du livre blanc (français et anglais) à partir du site MkDocs construit.

Le site est servi localement puis imprimé ; la mise en page est portée par docs/stylesheets/print.css.
Deux moteurs sont disponibles :

- weasyprint (par défaut) : PDF balisés, quasi conformes à PDF/UA-1 (voir requirements-pdf.txt) ;
- chrome : Chrome ou Chromium en mode headless, dont le balisage est très incomplet.

Usage :
    python scripts/export_pdf.py                     # utilise le site déjà construit dans ./site
    python scripts/export_pdf.py --build             # construit d'abord le site (mkdocs build --strict)
    python scripts/export_pdf.py --engine chrome

La variable d'environnement CHROME permet d'imposer le binaire du navigateur.
"""

import argparse
import base64
import functools
import http.server
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import urllib.request
from pathlib import Path

CHROME_CANDIDATES = ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser")
# Pages exportées : répertoire de la page dans le site construit → nom du PDF
DOCUMENTS = {
    "livre-blanc/": "otspi-livre-blanc.pdf",
    "white-paper/": "otspi-white-paper.pdf",
}


class QuietHandler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *args):
        pass


def find_chrome():
    if os.environ.get("CHROME"):
        return os.environ["CHROME"]
    for candidate in CHROME_CANDIDATES:
        path = shutil.which(candidate)
        if path:
            return path
    sys.exit("Chrome ou Chromium introuvable : définir la variable d'environnement CHROME.")


def serve(directory):
    handler = functools.partial(QuietHandler, directory=str(directory))
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    return httpd


def print_pdf(url, output):
    """Imprime une page en PDF avec Chrome headless ; renvoie le résultat du processus."""
    with tempfile.TemporaryDirectory() as profile:
        cmd = [
            find_chrome(),
            "--headless=new",
            "--disable-gpu",
            "--no-first-run",
            "--no-default-browser-check",
            f"--user-data-dir={profile}",
            "--no-pdf-header-footer",
            "--generate-pdf-document-outline",
            # Laisse le temps au chargement complet de la page (polices, scripts)
            "--virtual-time-budget=20000",
            "--run-all-compositor-stages-before-draw",
            f"--print-to-pdf={output}",
            url,
        ]
        if os.environ.get("CI"):
            cmd.insert(1, "--no-sandbox")
        return subprocess.run(cmd, capture_output=True, text=True, timeout=180)


# Style des schémas SVG du livre blanc, en couleurs fixes (thème clair) : WeasyPrint rend un SVG en ligne
# comme une image indépendante, qui n'hérite ni des feuilles de style ni des variables CSS de la page.
SVG_STYLE = """
.dg-box{fill:#fff;stroke:#b8bcc4;stroke-width:1.5}
.dg-root{fill:#e8eefc;stroke:#1a3d8f;stroke-width:2}
.dg-future{fill:none;stroke:#6b7280;stroke-width:1.5;stroke-dasharray:6 5}
.dg-t{fill:#1f2937;font-size:12.5px;font-weight:700;font-family:Inter,sans-serif}
.dg-s{fill:#4b5563;font-size:12px;font-family:Inter,sans-serif}
.dg-edge,.dg-cross{fill:none;stroke-width:1.8}
.dg-edge{stroke:#4b5563}
.dg-dash{stroke-dasharray:5 5}
.dg-cross{stroke:#1a3d8f;stroke-dasharray:7 5}
.dg-arrow{fill:#4b5563}
.dg-arrow-cross{fill:#1a3d8f}
.dg-label{fill:#1a3d8f;font-size:12px;font-weight:700;font-family:Inter,sans-serif}
"""


def svg_to_img(html):
    """Remplace chaque schéma SVG en ligne par une image autonome dotée d'un texte alternatif."""

    def convert(match):
        svg = match.group(0)
        title = re.search(r"<title[^>]*>(.*?)</title>", svg, re.S)
        desc = re.search(r"<desc[^>]*>(.*?)</desc>", svg, re.S)
        alt = ". ".join(part.group(1) for part in (title, desc) if part)
        svg = re.sub(r"(<svg\b[^>]*>)", lambda m: m.group(1) + f"<style>{SVG_STYLE}</style>", svg, count=1)
        data = base64.b64encode(svg.encode("utf-8")).decode("ascii")
        return f'<img class="wp-svg" src="data:image/svg+xml;base64,{data}" alt="{alt}">'

    return re.sub(r'<svg class="wp-svg".*?</svg>', convert, html, flags=re.S)


def hoist_link_wrappers(html):
    """Place la mise en forme (em, strong, code) autour du lien plutôt qu'à l'intérieur.

    WeasyPrint ne balise pas comme lien un `<a>` dont tout le contenu est enveloppé dans un élément de
    mise en forme : PDF/UA-1 le refuse (règle 7.18.5). Le rendu visuel reste le même.
    """
    return re.sub(
        r"<a\b([^>]*)>\s*<(em|strong|code)\b([^>]*)>(.*?)</\2>\s*</a>",
        lambda m: f"<{m.group(2)}{m.group(3)}><a{m.group(1)}>{m.group(4)}</a></{m.group(2)}>",
        html,
        flags=re.S,
    )


def print_weasyprint(url, output):
    """Imprime une page en PDF/UA-1 avec WeasyPrint ; renvoie None en cas de succès, sinon un message."""
    try:
        import weasyprint
    except ImportError:
        return "WeasyPrint n'est pas installé (pip install -r requirements-pdf.txt)"
    override = weasyprint.CSS(filename=str(Path(__file__).resolve().parent / "pdf-weasyprint.css"))
    try:
        with urllib.request.urlopen(url) as response:
            html = hoist_link_wrappers(svg_to_img(response.read().decode("utf-8")))
        weasyprint.HTML(string=html, base_url=url).write_pdf(str(output), stylesheets=[override], pdf_variant="pdf/ua-1", pdf_identifier=True)
    except Exception as error:  # noqa: BLE001 - toute erreur de rendu doit faire échouer l'export
        return str(error)
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--engine", choices=("weasyprint", "chrome"), default="weasyprint", help="moteur d'impression")
    parser.add_argument("--site", default="site", type=Path, help="répertoire du site construit")
    parser.add_argument("--build", action="store_true", help="exécuter mkdocs build --strict au préalable")
    args = parser.parse_args()

    site = args.site.resolve()
    if args.build:
        subprocess.run(["mkdocs", "build", "--strict", "--site-dir", str(site)], check=True)

    httpd = serve(site)
    try:
        for page_path, pdf_name in DOCUMENTS.items():
            if not (site / page_path / "index.html").is_file():
                sys.exit(f"Page introuvable : {site / page_path / 'index.html'} (lancer avec --build)")
            output = site / page_path / pdf_name
            output.unlink(missing_ok=True)
            url = f"http://127.0.0.1:{httpd.server_address[1]}/{page_path}"
            if args.engine == "chrome":
                result = print_pdf(url, output)
                error = result.stderr if result.returncode != 0 else None
            else:
                error = print_weasyprint(url, output)
            if error or not output.is_file() or output.stat().st_size == 0:
                sys.stderr.write((error or "") + "\n")
                sys.exit(f"Échec de la génération du PDF : {pdf_name}")
            print(f"PDF généré : {output} ({output.stat().st_size // 1024} Kio)")
    finally:
        httpd.shutdown()


if __name__ == "__main__":
    main()
