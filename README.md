# Association OTSPI — Organisation, Gouvernance & Redevabilité Publique
## « Open Trusted Service Provider Initiative »

[![Site Web](https://img.shields.io/badge/Portail_Web-about.otspi.org-blue?style=flat-square)](https://about.otspi.org)
[![Structure](https://img.shields.io/badge/Structure-Intérêt_Général_&_Gestion_Désintéressée-purple?style=flat-square)](#)
[![Normes](https://img.shields.io/badge/Normes-eIDAS_2.0_|_ETSI_|_WebTrust-blue?style=flat-square)](#)
[![Gouvernance](https://img.shields.io/badge/Gouvernance-Ségrégation_des_Devoirs-green?style=flat-square)](#)
[![Redevabilité](https://img.shields.io/badge/Redevabilité-100%25_Publique-orange?style=flat-square)](#)
[![Licence](https://img.shields.io/badge/Licence-CC--BY--4.0-lightgrey?style=flat-square)](LICENSE)

Ce dépôt centralise l'ensemble des documents juridiques, administratifs, réglementaires et de conformité de l'association **« Open Trusted Service Provider Initiative » (OTSPI)**, régie par la loi du 1er juillet 1901, conforme aux critères de l'**intérêt général** (articles 200 et 238 bis du CGI) et aux exigences des **prestataires de services de confiance qualifiés (eIDAS / ETSI / WebTrust)**.

> 🌐 **Portail officiel en ligne : [about.otspi.org](https://about.otspi.org)**  
> Retrouvez l'intégralité des statuts, du règlement intérieur et du socle de conformité présentés sous forme d'un site interactif avec recherche plein texte et liens d'édition directe.

---

## 🏛️ Mission d'Intérêt Général et Confiance Numérique

L'association **OTSPI** a pour vocation d'intérêt général de lever les barrières économiques, techniques, administratives et éducatives à la sécurité, à la confidentialité et à la confiance numérique dans les communications électroniques mondiales.

À l'instar du modèle d'infrastructure d'intérêt général développé par l'**ISRG (*Let's Encrypt*)** pour le chiffrement du Web :
- Nous concevons, opérons et pérennisons des **infrastructures critiques de confiance numérique ouvertes, souveraines, transparentes et universellement accessibles** (horodatage électronique qualifié, scellement, signature numérique, archivage probatoire, gestion des identités) conformes aux règlements européens **eIDAS / eIDAS 2.0** et aux standards internationaux **ETSI** et **WebTrust** ;
- La gouvernance est strictement **désintéressée** (bénévolat strict des dirigeants, inaliénabilité des logiciels libres et des marques, absence de distribution d'actifs) ;
- Un **Fonds de réserve et de garantie opérationnelle** sanctuarisé (Article 12 bis des Statuts) finance l'exécution du plan de fin d'activité (*Termination Plan*, maintien des CRL/OCSP pendant 10 ans), et l'actif net subsistant est dévolu à un organisme d'intérêt général similaire.

---

## ⚖️ Architecture de Gouvernance et Ségrégation des Fonctions

La gouvernance d'OTSPI applique une séparation stricte des devoirs conformément aux normes ETSI EN 319 401 et WebTrust :

1. **Direction Opérationnelle (*Executive Management*)** :  
   Assurée par le **Bureau** issu du **Conseil d'Administration** (Président, Trésorier, Secrétaire Général). Il porte la responsabilité juridique et financière, assure la mise en œuvre de la politique de sécurité et les relations institutionnelles.
2. **Comité des Politiques de Confiance (CPC / PMA)** :  
   Organe collégial technique indépendant garant de la rigueur cryptographique et normative. Il approuve les CP/CPS et politiques de service, valide les protocoles de cérémonies de clés, supervise l'habilitation des Officiers d'Autorité et nomme le Responsable de la Sécurité des Systèmes d'Information (RSSI / CISO). L'appartenance au Bureau est strictement incompatible avec le CPC.
3. **Officiers d'Autorité & Gardiens de Clés (*Key Custodians*)** :  
   Opérateurs habilités assurant sous contrôle à quatre yeux (*Dual Control*) les cérémonies de clés et disposant d'un pouvoir autonome de **révocation d'urgence** sans délai.

---

## 📁 Panoplie Documentaire Complète

```
├── docs/                              # Contenu du portail about.otspi.org
│   ├── index.md                       # Page d'accueil (bandeau dans overrides/home.html)
│   ├── livre-blanc/                   # Livre blanc (FR, fait foi) et historique des versions
│   ├── white-paper/                   # Traduction anglaise du livre blanc
│   ├── statuts/
│   │   └── statuts-association.md     # Projet de statuts, soumis à l'AG constitutive (non encore adopté)
│   ├── reglement-interieur/
│   │   └── reglement-interieur.md     # RI : cursus Officiers, MFA FIPS/ANSSI, Key Custodians, dépenses
│   ├── gouvernance/
│   │   ├── charte-ethique.md          # Charte d'éthique, de déontologie et de transparence publique
│   │   └── comite-technique.md        # Articulation CPC (PMA), TSC (ingénierie logicielle) et RFC
│   ├── administratif/                 # PV d'AG constitutive (modèle), rescrit fiscal, guide préfecture…
│   ├── cadrage/                       # Socle d'audit TSP / PKI : CP/CPS, PSSI, fin d'activité, OID, devis
│   ├── adhesion/
│   │   └── bulletin-adhesion.md       # Formulaires d'adhésion (sympathisants, titulaires, bienfaiteurs)
│   ├── reunions/                      # Registre des réunions, transparence des hébergements (FR / EN)
│   ├── assets/                        # Logos, police Inter (OFL), image de partage
│   ├── stylesheets/                   # Charte du portail (extra.css), impression et PDF (print.css)
│   └── javascripts/                   # Accessibilité, mesure d'audience sans cookie
├── overrides/                         # Gabarits Material : accueil, 404, métadonnées de partage
├── hooks/page_lang.py                 # Langue de la balise <html> selon la page
├── scripts/                           # Outils : voir ci-dessous
├── data/qtsp-count.json               # Décompte des QTSP cité par le livre blanc (annexe C)
├── deploy/o2switch/                   # Configuration Apache (.htaccess) et notes de déploiement
├── .github/workflows/                 # Déploiement, vérification des PR, contrôles périodiques
├── mkdocs.yml                         # Configuration Material for MkDocs
└── LICENSE                            # Creative Commons Attribution 4.0 International
```

---

## 🛠️ Outils et contribution

Le portail est construit avec [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/). Toute pull request vers `main` est vérifiée par `.github/workflows/check-pr.yml` (construction stricte, accessibilité, PDF) ; la fusion déclenche le déploiement (`deploy-o2switch.yml`), qui repasse les mêmes contrôles. Les deux workflows partagent l'action `.github/actions/build-portal`.

**Construire et prévisualiser le site**

```sh
pip install -r requirements.txt
mkdocs serve                  # http://127.0.0.1:8000, rechargé à chaque modification
mkdocs build --strict         # échoue sur tout lien ou ancre interne cassé
```

**Scripts** (`scripts/`)

| Script | Rôle | Prérequis |
|---|---|---|
| `export_pdf.py` | PDF balisés du livre blanc (FR, EN), du projet de statuts, du règlement intérieur et de la charte, dans `site/` | `pip install -r requirements-pdf.txt` (WeasyPrint, Pango) |
| `check_pdf_ua.sh` | Validation PDF/UA-1 de ces PDF avec veraPDF (téléchargé et vérifié au premier lancement) | Java |
| `check_a11y.js` | Accessibilité WCAG 2 AA (pa11y, moteur axe) de toutes les pages du site construit | Node.js, `npm install --no-save pa11y@9`, Chrome |
| `build_diagrams.py` | Régénère les schémas SVG du livre blanc et l'organigramme de l'accueil | — |
| `build_og_image.py` | Régénère l'image de partage par défaut (`docs/assets/og/og-portail.png`) | Chrome |
| `zenodo_draft.py` | Brouillon Zenodo du livre blanc à la publication d'une release (`release.yml`) ; le DOI n'est attribué qu'à la publication manuelle sur Zenodo | secret `ZENODO_TOKEN` |
| `count_qtsp.py` | Décompte des QTSP des listes de confiance de l'EEE (`data/qtsp-count.json`) | — |
| `check_links.py` | Liens externes cassés (contrôle mensuel) | — |
| `check_sites.sh` | Codes HTTP, redirections et certificats des sites OTSPI (contrôle quotidien) | curl, openssl |

Chaîne complète, comme en CI :

```sh
mkdocs build --strict
python scripts/export_pdf.py
bash scripts/check_pdf_ua.sh
npm install --no-save pa11y@9 && node scripts/check_a11y.js site
```

Les schémas et l'image de partage sont générés puis versionnés : après modification de leur source, relancer le script correspondant et commiter le résultat.

---

## 📬 Contact

- **Contact unique (Adhésions, Questions générales, Sécurité)** : `contact@otspi.org`  
  *(Pour le signalement de vulnérabilités / CVD : mentionner `[Sécurité]` en objet ou utiliser les [GitHub Private Security Advisories](https://github.com/otspi/organisation/security/advisories))*
- **Portail web** : [about.otspi.org](https://about.otspi.org)
