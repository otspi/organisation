#!/usr/bin/env python3
# SPDX-License-Identifier: EUPL-1.2
"""Prépare sur Zenodo un dépôt en brouillon du livre blanc (PDF français et anglais) pour une version donnée.

Le dépôt reste un brouillon : le DOI n'est attribué, définitivement, que lorsqu'une personne relit puis
publie le dépôt depuis Zenodo. Les métadonnées viennent de .zenodo.json ; la version et la date de
publication sont ajoutées. Appelé par .github/workflows/release.yml à la publication d'une release.

Variables d'environnement :
    ZENODO_TOKEN           jeton personnel Zenodo (portées deposit:write et deposit:actions) ;
    ZENODO_URL             https://zenodo.org par défaut (https://sandbox.zenodo.org pour un essai) ;
    ZENODO_DEPOSITION_ID   identifiant d'un dépôt déjà publié : le brouillon en devient une nouvelle
                           version (même DOI de concept) au lieu d'un dépôt distinct.

Usage :
    python3 scripts/zenodo_draft.py --version 0.9 fichier.pdf [...]
    python3 scripts/zenodo_draft.py --version 0.9 --dry-run fichier.pdf [...]   # affiche sans envoyer

Aucune dépendance en dehors de la bibliothèque standard.
"""

import argparse
import datetime
import json
import os
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def api(method, url, token, payload=None, data=None, content_type="application/json"):
    body = json.dumps(payload).encode("utf-8") if payload is not None else data
    request = urllib.request.Request(url, data=body, method=method)
    request.add_header("Authorization", f"Bearer {token}")
    if body is not None:
        request.add_header("Content-Type", content_type)
    with urllib.request.urlopen(request, timeout=300) as response:
        raw = response.read()
    return json.loads(raw) if raw else None


def metadata(version):
    meta = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))
    meta["version"] = version
    meta["publication_date"] = datetime.date.today().isoformat()
    return meta


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--version", required=True, help="numéro de version (par exemple 0.9)")
    parser.add_argument("--dry-run", action="store_true", help="afficher les métadonnées et les fichiers sans rien envoyer")
    parser.add_argument("files", nargs="+", type=Path, help="fichiers à déposer")
    args = parser.parse_args()

    missing = [str(f) for f in args.files if not f.is_file()]
    if missing:
        sys.exit(f"Fichiers introuvables : {', '.join(missing)}")
    meta = metadata(args.version)
    if args.dry_run:
        print(json.dumps({"metadata": meta, "files": [f.name for f in args.files]}, ensure_ascii=False, indent=2))
        return

    token = os.environ.get("ZENODO_TOKEN")
    if not token:
        sys.exit("ZENODO_TOKEN n'est pas défini.")
    base = os.environ.get("ZENODO_URL", "https://zenodo.org").rstrip("/")
    previous = os.environ.get("ZENODO_DEPOSITION_ID")

    if previous:
        # Nouvelle version d'un dépôt publié : Zenodo recopie ses fichiers, qu'on remplace
        created = api("POST", f"{base}/api/deposit/depositions/{previous}/actions/newversion", token)
        draft = api("GET", created["links"]["latest_draft"], token)
        for old in draft.get("files", []):
            api("DELETE", old["links"]["self"], token)
    else:
        draft = api("POST", f"{base}/api/deposit/depositions", token, payload={})

    for path in args.files:
        api("PUT", f'{draft["links"]["bucket"]}/{path.name}', token, data=path.read_bytes(), content_type="application/octet-stream")
    draft = api("PUT", f'{base}/api/deposit/depositions/{draft["id"]}', token, payload={"metadata": meta})

    link = draft["links"]["html"]
    print(f"Brouillon Zenodo prêt (non publié, aucun DOI attribué) : {link}")
    summary = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary:
        with open(summary, "a", encoding="utf-8") as out:
            out.write(f"Brouillon Zenodo de la version {args.version} : {link}\n\n"
                      "À relire puis publier depuis Zenodo pour attribuer le DOI.\n")


if __name__ == "__main__":
    main()
