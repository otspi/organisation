#!/usr/bin/env python3
"""Génère les PDF de référence du portail à partir du site MkDocs construit : le livre blanc (français et
anglais), le projet de statuts, le règlement intérieur et la charte d'éthique.

Le site est servi localement puis imprimé ; la mise en page est portée par docs/stylesheets/print.css.
Le livre blanc porte sa page de garde et son sommaire dans sa source ; pour les textes juridiques, qu'on ne
modifie pas pour les besoins de l'impression, le script les ajoute au HTML avant l'impression (WeasyPrint).
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
import datetime
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
from html import escape
from pathlib import Path

CHROME_CANDIDATES = ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser")
ROOT = Path(__file__).resolve().parent.parent

# Pages exportées : répertoire de la page dans le site construit → PDF. Les textes juridiques reçoivent une
# page de garde (cover) et un sommaire des titres de niveau `section` ; `source` date la version.
DOCUMENTS = {
    "livre-blanc/": {"pdf": "otspi-livre-blanc.pdf"},
    "white-paper/": {"pdf": "otspi-white-paper.pdf"},
    "statuts/statuts-association/": {
        "pdf": "otspi-projet-de-statuts.pdf",
        "source": "docs/statuts/statuts-association.md",
        "section": 3,
        "cover": {
            "kicker": "Projet de statuts",
            "title": "Statuts de l'association Open Trusted Service Provider Initiative (OTSPI)",
            "status": "Projet soumis à l'assemblée générale constitutive, non encore adopté",
            "footer": "OTSPI — Projet de statuts, non adopté · CC-BY-4.0",
        },
    },
    "reglement-interieur/reglement-interieur/": {
        "pdf": "otspi-reglement-interieur.pdf",
        "source": "docs/reglement-interieur/reglement-interieur.md",
        "section": 2,
        "cover": {
            "kicker": "Règlement intérieur",
            "title": "Règlement intérieur de l'association Open Trusted Service Provider Initiative (OTSPI)",
            "status": "Projet, en application de l'article 14 du projet de statuts",
            "footer": "OTSPI — Règlement intérieur, projet · CC-BY-4.0",
        },
    },
    "gouvernance/charte-ethique/": {
        "pdf": "otspi-charte-ethique.pdf",
        "source": "docs/gouvernance/charte-ethique.md",
        "section": 2,
        "cover": {
            "kicker": "Charte",
            "title": "Charte d'éthique, de déontologie et de transparence publique",
            "status": "Association en cours de constitution",
            "footer": "OTSPI — Charte d'éthique · CC-BY-4.0",
        },
    },
}

MONTHS = ("janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre",
          "novembre", "décembre")


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


def version_date(source):
    """Date du dernier commit du fichier source, en toutes lettres (date du jour à défaut)."""
    result = subprocess.run(["git", "log", "-1", "--format=%cs", "--", source], cwd=ROOT, capture_output=True, text=True)
    day = datetime.date.fromisoformat(result.stdout.strip()) if result.stdout.strip() else datetime.date.today()
    return f"{day.day} {MONTHS[day.month - 1]} {day.year}"


def plain(fragment):
    """Texte brut d'un fragment HTML de titre, sans le lien permanent « ¶ »."""
    return re.sub(r"<[^>]+>", "", re.sub(r'<a class="headerlink".*?</a>', "", fragment, flags=re.S)).strip()


def add_cover(html, doc):
    """Ajoute une page de garde et un sommaire paginé à un texte juridique, sans toucher à sa source.

    La page de garde précède le titre de niveau 1 ; le sommaire suit ce titre (et son sous-titre), pour que
    le premier titre du PDF reste de niveau 1. Les titres de section et de sous-section reçoivent les
    classes doc-section et doc-sub, qui règlent l'en-tête courant et les signets (voir print.css).
    """
    cover, level = doc["cover"], doc["section"]
    start = html.index("<h1")
    head_end = html.index("</h1>", start) + len("</h1>")
    subtitle = re.match(r"\s*<h2\b.*?</h2>", html[head_end:], re.S)
    if subtitle:
        head_end += subtitle.end()

    body = html[head_end:]
    entries = [(m.group(1), plain(m.group(2))) for m in re.finditer(rf'<h{level} id="([^"]+)"[^>]*>(.*?)</h{level}>', body, re.S)]
    body = re.sub(rf'<h{level} id="', f'<h{level} class="doc-section" id="', body)
    body = re.sub(rf'<h{level + 1} id="', f'<h{level + 1} class="doc-sub" id="', body)

    page = (
        f'<div class="wp-cover doc-cover" data-footer="{escape(cover["footer"])}">'
        '<p><img alt="OTSPI" class="wp-cover-logo" src="/assets/logo-vertical-dark.svg"></p>'
        f'<p class="wp-cover-kicker">{escape(cover["kicker"])}</p>'
        f'<p class="wp-cover-title">{escape(cover["title"])}</p>'
        f'<p class="wp-cover-meta">Open Trusted Service Provider Initiative (OTSPI)<br>{escape(cover["status"])}'
        f'<br>Version du {version_date(doc["source"])}</p>'
        '<p class="wp-cover-license">Licence Creative Commons Attribution 4.0 International · contact@otspi.org</p>'
        "</div>"
    )
    toc = '<div class="wp-toc"><h2>Sommaire</h2><ul>' + "".join(
        f'<li><a href="#{anchor}">{escape(text)}</a></li>' for anchor, text in entries) + "</ul></div>"
    return html[:start] + page + html[start:head_end] + toc + body


def print_weasyprint(url, output, doc):
    """Imprime une page en PDF/UA-1 avec WeasyPrint ; renvoie None en cas de succès, sinon un message."""
    try:
        import weasyprint
    except ImportError:
        return "WeasyPrint n'est pas installé (pip install -r requirements-pdf.txt)"
    override = weasyprint.CSS(filename=str(Path(__file__).resolve().parent / "pdf-weasyprint.css"))
    try:
        with urllib.request.urlopen(url) as response:
            html = hoist_link_wrappers(svg_to_img(response.read().decode("utf-8")))
        if "cover" in doc:
            html = add_cover(html, doc)
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
        for page_path, doc in DOCUMENTS.items():
            pdf_name = doc["pdf"]
            if not (site / page_path / "index.html").is_file():
                sys.exit(f"Page introuvable : {site / page_path / 'index.html'} (lancer avec --build)")
            output = site / page_path / pdf_name
            output.unlink(missing_ok=True)
            url = f"http://127.0.0.1:{httpd.server_address[1]}/{page_path}"
            if args.engine == "chrome":
                result = print_pdf(url, output)
                error = result.stderr if result.returncode != 0 else None
            else:
                error = print_weasyprint(url, output, doc)
            if error or not output.is_file() or output.stat().st_size == 0:
                sys.stderr.write((error or "") + "\n")
                sys.exit(f"Échec de la génération du PDF : {pdf_name}")
            print(f"PDF généré : {output} ({output.stat().st_size // 1024} Kio)")
    finally:
        httpd.shutdown()


if __name__ == "__main__":
    main()
