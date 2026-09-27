#!/usr/bin/env python3
# SPDX-License-Identifier: EUPL-1.2
"""Génère les deux schémas du livre blanc (hiérarchie qualifiée, hiérarchies TLS) en SVG intégré,
en français et en anglais, et les insère entre les marqueurs des pages du livre blanc.

Les schémas n'utilisent aucun script : ils remplacent des blocs Mermaid, dont la bibliothèque
(environ 950 Ko, chargée depuis un service tiers) ralentissait fortement la page.
Les couleurs proviennent des variables du thème (clair et sombre) : voir docs/stylesheets/extra.css.

Usage :
    python3 scripts/build_diagrams.py
"""

from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

TEXT = {
    "fr": {
        "h_title": "Hiérarchie de certification qualifiée d'OTSPI",
        "h_desc": "L'AC racine OTSPI, hors ligne et sous quorum, certifie l'AC intermédiaire d'horodatage, qui certifie les unités d'horodatage TSU-1 (site A) et TSU-2 (site B). Elle certifiera aussi de futures AC qualifiées de cachet, de signature et d'attestations.",
        "root": ("AC racine OTSPI", "hors ligne · air-gap · quorum M-de-N"),
        "inter": ("AC intermédiaire Horodatage", "hors ligne ou en ligne restreinte"),
        "future": ("AC qualifiées futures", "cachet · signature · attestations"),
        "tsu1": ("Unité d'horodatage TSU-1", "HSM en ligne — site A"),
        "tsu2": ("Unité d'horodatage TSU-2", "HSM en ligne — site B"),
        "t_title": "Hiérarchies de certification TLS d'OTSPI",
        "t_desc": "Deux racines distinctes : une racine WebTrust pour les magasins des navigateurs, une racine QWAC inscrite sur la liste de confiance européenne. La racine WebTrust certifie une sous-AC DV, qui émet des certificats serveur DV par ACME instantané. Une sous-AC hybride OV / QWAC, à clé unique, est certifiée par la racine WebTrust et, par signature croisée, par la racine QWAC ; elle émet des certificats OV / QWAC.",
        "rw": ("Racine WebTrust", "magasins OS et navigateurs"),
        "rq": ("Racine QWAC", "liste de confiance européenne"),
        "dv": ("Sous-AC DV", "WebTrust uniquement · HSM standard"),
        "hy": ("Sous-AC hybride OV / QWAC", "une clé · deux certificats d'AC"),
        "cdv": ("Certificats serveur DV", "usage Web · ACME instantané"),
        "cov": ("Certificats serveur OV / QWAC", "DSP2, eIDAS · ACME avec liaison de compte"),
        "cross": "signature croisée",
    },
    "en": {
        "h_title": "OTSPI qualified certification hierarchy",
        "h_desc": "The offline OTSPI root CA, under a quorum, certifies the time-stamping intermediate CA, which certifies time-stamping units TSU-1 (site A) and TSU-2 (site B). It will also certify future qualified CAs for seals, signatures and attestations.",
        "root": ("OTSPI root CA", "offline · air-gapped · M-of-N quorum"),
        "inter": ("Time-stamping intermediate CA", "offline or restricted online"),
        "future": ("Future qualified CAs", "seal · signature · attestations"),
        "tsu1": ("Time-stamping unit TSU-1", "online HSM — site A"),
        "tsu2": ("Time-stamping unit TSU-2", "online HSM — site B"),
        "t_title": "OTSPI TLS certification hierarchies",
        "t_desc": "Two separate roots: a WebTrust root for browser stores, and a QWAC root listed on the European trusted list. The WebTrust root certifies a DV sub-CA, which issues DV server certificates through instant ACME. A hybrid OV / QWAC sub-CA, holding a single key, is certified by the WebTrust root and, through cross-signing, by the QWAC root; it issues OV / QWAC certificates.",
        "rw": ("WebTrust root", "OS and browser stores"),
        "rq": ("QWAC root", "European trusted list"),
        "dv": ("DV sub-CA", "WebTrust only · standard HSM"),
        "hy": ("Hybrid OV / QWAC sub-CA", "one key · two CA certificates"),
        "cdv": ("DV server certificates", "general Web use · instant ACME"),
        "cov": ("OV / QWAC server certificates", "PSD2, eIDAS · ACME with account binding"),
        "cross": "cross-signing",
    },
}


def box(x, y, w, h, texts, cls):
    title, sub = texts
    cx = x + w / 2
    return (f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/>'
            f'<text class="dg-t" x="{cx}" y="{y + 27}" text-anchor="middle">{escape(title)}</text>'
            f'<text class="dg-s" x="{cx}" y="{y + 48}" text-anchor="middle">{escape(sub)}</text>')


def defs(uid):
    return (f'<defs><marker id="arr-{uid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path class="dg-arrow" d="M0 0 L10 5 L0 10 z"/></marker>'
            f'<marker id="arc-{uid}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">'
            f'<path class="dg-arrow-cross" d="M0 0 L10 5 L0 10 z"/></marker></defs>')


def hierarchy(t, uid):
    parts = [
        f'<svg class="wp-svg" viewBox="0 0 760 350" role="img" aria-labelledby="{uid}-t {uid}-d" xmlns="http://www.w3.org/2000/svg">',
        f'<title id="{uid}-t">{escape(t["h_title"])}</title><desc id="{uid}-d">{escape(t["h_desc"])}</desc>',
        defs(uid),
        f'<path class="dg-edge" d="M380 74 C380 104 190 100 190 128" marker-end="url(#arr-{uid})"/>',
        f'<path class="dg-edge dg-dash" d="M380 74 C380 104 570 100 570 128" marker-end="url(#arr-{uid})"/>',
        f'<path class="dg-edge" d="M190 198 C190 228 100 224 100 256" marker-end="url(#arr-{uid})"/>',
        f'<path class="dg-edge" d="M190 198 C190 228 290 224 290 256" marker-end="url(#arr-{uid})"/>',
        box(230, 10, 300, 64, t["root"], "dg-root"),
        box(60, 130, 260, 68, t["inter"], "dg-box"),
        box(440, 130, 260, 68, t["future"], "dg-future"),
        box(10, 258, 180, 68, t["tsu1"], "dg-box"),
        box(200, 258, 180, 68, t["tsu2"], "dg-box"),
        '</svg>',
    ]
    return "".join(parts)


def tls(t, uid):
    parts = [
        f'<svg class="wp-svg" viewBox="0 0 760 390" role="img" aria-labelledby="{uid}-t {uid}-d" xmlns="http://www.w3.org/2000/svg">',
        f'<title id="{uid}-t">{escape(t["t_title"])}</title><desc id="{uid}-d">{escape(t["t_desc"])}</desc>',
        defs(uid),
        f'<path class="dg-edge" d="M200 74 L200 140" marker-end="url(#arr-{uid})"/>',
        f'<path class="dg-edge" d="M300 74 C300 108 500 104 500 138" marker-end="url(#arr-{uid})"/>',
        f'<path class="dg-cross" d="M600 74 L600 138" marker-end="url(#arc-{uid})"/>',
        f'<text class="dg-label" x="610" y="112">{escape(t["cross"])}</text>',
        f'<path class="dg-edge" d="M200 212 L200 288" marker-end="url(#arr-{uid})"/>',
        f'<path class="dg-edge" d="M560 212 L560 288" marker-end="url(#arr-{uid})"/>',
        box(60, 10, 280, 64, t["rw"], "dg-root"),
        box(420, 10, 280, 64, t["rq"], "dg-root"),
        box(60, 142, 280, 70, t["dv"], "dg-box"),
        box(420, 142, 280, 70, t["hy"], "dg-box"),
        box(60, 290, 280, 70, t["cdv"], "dg-box"),
        box(420, 290, 280, 70, t["cov"], "dg-box"),
        '</svg>',
    ]
    return "".join(parts)


def figure(svg, number, title):
    """Enveloppe un schéma dans une figure légendée et numérotée, ancrée sur #figure-N pour les renvois."""
    return (f'<figure class="wp-diagram" id="figure-{number}" markdown="0">\n{svg}\n'
            f'<figcaption><span class="wp-fig-num">Figure {number}</span> — {escape(title)}</figcaption>\n</figure>')


def replace_block(text, name, block):
    start, end = f"<!-- diagram:{name}:start -->", f"<!-- diagram:{name}:end -->"
    i, j = text.index(start), text.index(end)
    return text[: i + len(start)] + "\n" + block + "\n" + text[j:]


def main():
    for lang, path in (("fr", "docs/livre-blanc/index.md"), ("en", "docs/white-paper/index.md")):
        page = ROOT / path
        text = page.read_text(encoding="utf-8")
        text = replace_block(text, "hierarchy", figure(hierarchy(TEXT[lang], f"{lang}-h"), 1, TEXT[lang]["h_title"]))
        text = replace_block(text, "tls", figure(tls(TEXT[lang], f"{lang}-t"), 2, TEXT[lang]["t_title"]))
        page.write_text(text, encoding="utf-8")
        print(f"{path} : schémas régénérés")


if __name__ == "__main__":
    main()
