#!/usr/bin/env bash
# SPDX-License-Identifier: EUPL-1.2
# Valide au format PDF/UA-1 les PDF du portail générés dans ./site avec veraPDF.
# Retourne un code d'erreur si un PDF n'est pas conforme.
#
# veraPDF (licence GPLv3 et MPL 2.0) est téléchargé en version épinglée, vérifié par empreinte SHA-256,
# puis installé dans VERAPDF_HOME (par défaut ~/.cache/verapdf). Java est requis.
#
# Usage :
#     bash scripts/check_pdf_ua.sh [fichier.pdf ...]

set -euo pipefail

VERSION="1.30.2"
URL="https://software.verapdf.org/releases/1.30/verapdf-greenfield-${VERSION}-installer.zip"
SHA256="6cc6341cb1af644044054b81f00a6590a7918abb18f762243de115258bcad838"
HOME_DIR="${VERAPDF_HOME:-$HOME/.cache/verapdf}"

if [ ! -x "$HOME_DIR/verapdf" ]; then
  work="$(mktemp -d)"
  trap 'rm -rf "$work"' EXIT
  curl -fsSL -o "$work/installer.zip" "$URL"
  echo "$SHA256  $work/installer.zip" | sha256sum -c - >/dev/null
  unzip -q "$work/installer.zip" -d "$work"
  cat > "$work/auto.xml" <<XML
<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<AutomatedInstallation langpack="eng">
<com.izforge.izpack.panels.htmlhello.HTMLHelloPanel id="welcome"/>
<com.izforge.izpack.panels.target.TargetPanel id="install_dir"><installpath>$HOME_DIR</installpath></com.izforge.izpack.panels.target.TargetPanel>
<com.izforge.izpack.panels.packs.PacksPanel id="sdk_pack_select"><pack index="0" name="veraPDF Runtime" selected="true"/><pack index="1" name="veraPDF Mac and *nix Scripts" selected="true"/><pack index="2" name="veraPDF Validation model" selected="true"/><pack index="3" name="veraPDF Documentation" selected="false"/><pack index="4" name="veraPDF Sample Plugins" selected="false"/></com.izforge.izpack.panels.packs.PacksPanel>
<com.izforge.izpack.panels.install.InstallPanel id="install"/>
<com.izforge.izpack.panels.finish.FinishPanel id="finish"/>
</AutomatedInstallation>
XML
  java -jar "$work"/verapdf-greenfield-*/verapdf-izpack-installer-*.jar "$work/auto.xml" >/dev/null 2>&1
fi

if [ "$#" -gt 0 ]; then
  files=("$@")
else
  files=(site/livre-blanc/otspi-livre-blanc.pdf site/white-paper/otspi-white-paper.pdf
         site/statuts/statuts-association/otspi-projet-de-statuts.pdf
         site/reglement-interieur/reglement-interieur/otspi-reglement-interieur.pdf
         site/gouvernance/charte-ethique/otspi-charte-ethique.pdf)
fi

status=0
for file in "${files[@]}"; do
  if "$HOME_DIR/verapdf" --flavour ua1 --format text "$file" 2>/dev/null | grep -q '^PASS'; then
    echo "PDF/UA-1 conforme : $file"
  else
    echo "PDF/UA-1 NON conforme : $file"
    "$HOME_DIR/verapdf" --flavour ua1 --format text --verbose "$file" 2>/dev/null | head -20 || true
    status=1
  fi
done
exit "$status"
