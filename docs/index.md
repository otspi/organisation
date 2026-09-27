---
title: "OTSPI — Open Trusted Service Provider Initiative"
description: "Portail officiel de gouvernance, statuts, conformité et documentation d'intérêt général pour la confiance numérique européenne."
template: home.html
hide:
  - navigation
  - toc
---

<!-- Le bandeau d'accueil (titre, accroche, boutons) est dans overrides/home.html -->

<div class="otspi-features" markdown>

<div class="otspi-feature" markdown>
:material-bank-outline:{ .otspi-feature__icon }

<p class="otspi-feature__title">100 % intérêt général</p>

Gestion désintéressée, bénévolat strict des dirigeants, inaliénabilité des logiciels libres et des marques.
</div>

<div class="otspi-feature" markdown>
:material-certificate-outline:{ .otspi-feature__icon }

<p class="otspi-feature__title">eIDAS 2.0 et ETSI</p>

Services de confiance qualifiés : horodatage, signature, scellement et archivage probatoire sous audit CAB.
</div>

<div class="otspi-feature" markdown>
:material-scale-balance:{ .otspi-feature__icon }

<p class="otspi-feature__title">Séparation des devoirs</p>

Indépendance absolue du Comité des Politiques de Confiance (CPC) vis-à-vis du Bureau exécutif.
</div>

<div class="otspi-feature" markdown>
:material-magnify-scan:{ .otspi-feature__icon }

<p class="otspi-feature__title">Redevabilité intégrale</p>

Transparence totale des PV, budgets prévisionnels, rapports d'audit et politiques de certification (CP/CPS).
</div>

</div>

## Explorer la documentation et les textes fondateurs

<div class="grid cards otspi-docs" markdown>

-   :material-scale-balance:{ .lg .middle } __Statuts et gouvernance__

    ---

    Le projet de statuts constitutifs, soumis au vote de l'assemblée générale constitutive, fondé sur l'intérêt général (CGI art. 200 & 238 bis), la gestion désintéressée et la séparation stricte des devoirs.

    [:octicons-arrow-right-24: Consulter le projet de statuts](statuts/statuts-association.md)  
    [:octicons-arrow-right-24: Charte d'éthique et de déontologie](gouvernance/charte-ethique.md)  
    [:octicons-arrow-right-24: Organisation technique et CPC](gouvernance/comite-technique.md)

-   :material-book-open-page-variant:{ .lg .middle } __Règlement intérieur__

    ---

    Fonctionnement opérationnel : cursus d'habilitation des Officiers d'Autorité, clés matérielles FIPS/ANSSI et règles de fonctionnement de l'association.

    [:octicons-arrow-right-24: Règlement intérieur](reglement-interieur/reglement-interieur.md)

-   :material-certificate:{ .lg .middle } __Socle de conformité (TSP / PKI)__

    ---

    Le référentiel d'audit initial conforme aux normes eIDAS, ETSI et WebTrust : Cadre CP/CPS (RFC 3647), Politique de Sécurité (PSSI) et Fin d'Activité.

    [:octicons-arrow-right-24: Cadre général CP/CPS](cadrage/cp-cps-cadre.md)  
    [:octicons-arrow-right-24: Politique de sécurité (PSSI ISO 27001)](cadrage/pssi.md)  
    [:octicons-arrow-right-24: Plan de fin d'activité (Termination Plan)](cadrage/termination-plan.md)

-   :material-file-document-outline:{ .lg .middle } __Démarches légales et fiscales__

    ---

    Dossier juridique complet : Procès-Verbal de l'AG Constitutive, demande formelle de rescrit fiscal mécénat DGFIP et guide d'immatriculation.

    [:octicons-arrow-right-24: Procès-verbal constitutif (modèle)](administratif/pv-ag-constitutive-modele.md)  
    [:octicons-arrow-right-24: Dossier de rescrit fiscal DGFIP](administratif/rescrit-fiscal-mecenat.md)  
    [:octicons-arrow-right-24: Guide préfecture (RNA, SIRET)](administratif/declaration-prefecture.md)

</div>

## La confiance numérique comme bien commun

L'association **« Open Trusted Service Provider Initiative » (OTSPI)**, en cours de constitution, a pour but d'intérêt général de lever les barrières économiques, techniques, administratives et éducatives à la sécurité, à la confidentialité et à la confiance numérique dans les communications électroniques mondiales.

À l'instar du modèle d'infrastructure d'intérêt général développé par l'**ISRG (*Let's Encrypt*)** pour le chiffrement du Web :

* **Infrastructures ouvertes et universelles** : Nous concevons, opérons et pérennisons des services de confiance qualifiés (horodatage électronique qualifié, scellement, signature numérique, archivage probatoire, gestion des identités) conformes aux règlements européens **eIDAS / eIDAS 2.0** et aux standards internationaux **ETSI** et **WebTrust**.
* **Gestion strictement désintéressée** : Bénévolat strict des dirigeants, inaliénabilité des dépôts logiciels libres et des marques, absence de distribution d'actifs et réinvestissement intégral des excédents dans la mission d'intérêt général.
* **Garantie de continuité opérationnelle** : Un fonds de réserve sanctuarisé garantit l'exécution intégrale du plan de fin d'activité (*Termination Plan*, maintien des listes de révocation CRL/OCSP pendant au moins 10 ans).

## Architecture de gouvernance et ségrégation des fonctions

La gouvernance d'OTSPI applique une séparation stricte des devoirs conformément aux normes ETSI EN 319 401 et WebTrust :

<!-- diagram:governance:start -->
<figure class="wp-diagram" markdown="0">
<svg class="wp-svg wp-svg--wide" viewBox="0 0 940 490" role="img" aria-labelledby="home-g-t home-g-d" xmlns="http://www.w3.org/2000/svg"><title id="home-g-t">Organisation de la gouvernance d&#x27;OTSPI</title><desc id="home-g-d">L&#x27;assemblée générale élit le conseil d&#x27;administration, qui désigne le bureau (direction opérationnelle) ; le bureau assure les relations avec les autorités de contrôle et les auditeurs. L&#x27;assemblée générale confirme aussi les nominations au comité des politiques de confiance (CPC), autorité normative indépendante du bureau, qui désigne le RSSI pour un an, habilite et contrôle les officiers d&#x27;autorité et rend un avis conforme sur les travaux du comité technique ; le bureau fournit à ce comité ses moyens.</desc><defs><marker id="arr-home-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path class="dg-arrow" d="M0 0 L10 5 L0 10 z"/></marker><marker id="arc-home-g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path class="dg-arrow-cross" d="M0 0 L10 5 L0 10 z"/></marker></defs><rect class="dg-group" x="10" y="196" width="300" height="284" rx="10"/><text class="dg-glabel" x="26" y="466">DIRECTION OPÉRATIONNELLE</text><rect class="dg-group" x="330" y="196" width="600" height="284" rx="10"/><text class="dg-glabel" x="346" y="466">AUTORITÉ NORMATIVE INDÉPENDANTE</text><path class="dg-edge" d="M330 42 C220 42 160 56 160 108" marker-end="url(#arr-home-g)"/><path class="dg-cross" d="M570 42 C650 42 630 150 630 228" marker-end="url(#arc-home-g)"/><text class="dg-label" x="646" y="140">confirmation des nominations</text><path class="dg-edge" d="M160 174 L160 228" marker-end="url(#arr-home-g)"/><path class="dg-edge" d="M160 294 L160 364" marker-end="url(#arr-home-g)"/><path class="dg-edge" d="M290 262 C360 262 410 318 420 364" marker-end="url(#arr-home-g)"/><path class="dg-edge" d="M630 294 C630 330 435 330 435 364" marker-end="url(#arr-home-g)"/><path class="dg-edge" d="M630 294 L631 364" marker-end="url(#arr-home-g)"/><path class="dg-edge" d="M630 294 C630 330 827 330 827 364" marker-end="url(#arr-home-g)"/><rect class="dg-root" x="330" y="10" width="240" height="64" rx="8"/><text class="dg-t" x="450.0" y="37" text-anchor="middle">Assemblée générale</text><text class="dg-s" x="450.0" y="58" text-anchor="middle">titulaires et sympathisants</text><rect class="dg-box" x="40" y="110" width="240" height="64" rx="8"/><text class="dg-t" x="160.0" y="137" text-anchor="middle">Conseil d&#x27;administration</text><text class="dg-s" x="160.0" y="158" text-anchor="middle">2 à 9 membres</text><rect class="dg-box" x="30" y="230" width="260" height="64" rx="8"/><text class="dg-t" x="160.0" y="257" text-anchor="middle">Bureau</text><text class="dg-s" x="160.0" y="278" text-anchor="middle">présidence · trésorerie · secrétariat</text><rect class="dg-box" x="30" y="366" width="260" height="64" rx="8"/><text class="dg-t" x="160.0" y="393" text-anchor="middle">Autorités de contrôle</text><text class="dg-s" x="160.0" y="414" text-anchor="middle">et auditeurs (CAB)</text><rect class="dg-root" x="500" y="230" width="260" height="64" rx="8"/><text class="dg-t" x="630.0" y="257" text-anchor="middle">Comité des politiques de confiance</text><text class="dg-s" x="630.0" y="278" text-anchor="middle">CPC / PMA</text><rect class="dg-box" x="342" y="366" width="186" height="64" rx="8"/><text class="dg-t" x="435.0" y="393" text-anchor="middle">Comité technique (TSC)</text><text class="dg-s" x="435.0" y="414" text-anchor="middle">avis CPC · moyens du Bureau</text><rect class="dg-box" x="538" y="366" width="186" height="64" rx="8"/><text class="dg-t" x="631.0" y="393" text-anchor="middle">RSSI / CISO</text><text class="dg-s" x="631.0" y="414" text-anchor="middle">désigné par le CPC, 1 an</text><rect class="dg-box" x="734" y="366" width="186" height="64" rx="8"/><text class="dg-t" x="827.0" y="393" text-anchor="middle">Officiers d&#x27;autorité</text><text class="dg-s" x="827.0" y="414" text-anchor="middle">et gardiens de clés</text></svg>
</figure>
<!-- diagram:governance:end -->

1. **Direction Opérationnelle (*Executive Management*)** : Assurée par le Bureau issu du Conseil d'Administration. Il porte la responsabilité juridique et financière, alloue les ressources de sécurité et assure les relations de gouvernance.
2. **Comité des Politiques de Confiance (CPC / PMA)** : Organe collégial indépendant garant de la rigueur cryptographique et normative. Il approuve les CP/CPS, valide les cérémonies de clés, supervise l'habilitation des Officiers d'Autorité et désigne le RSSI. **L'appartenance au Bureau est strictement incompatible avec le CPC.**
3. **Officiers d'Autorité & Gardiens de Clés (*Key Custodians*)** : Opérateurs habilités assurant sous contrôle à quatre yeux (*Dual Control*) les cérémonies de clés et disposant d'un pouvoir autonome de **révocation d'urgence** sans délai.

## Redevabilité publique intégrale (*Public Accountability*)

OTSPI applique un principe de **transparence radicale et d'auditabilité publique** :

- Ordres du jour, débats et comptes-rendus publics des réunions (CA, Bureau, Assemblées Générales, comités techniques) ;
- Budgets prévisionnels, comptes annuels certifiés, rapports moraux et rapports d'évaluation d'audit (ETSI / eIDAS / WebTrust) ;
- Dépôt public de l'ensemble des sources et des documents de gouvernance sur [GitHub : `otspi/organisation`](https://github.com/otspi/organisation).

!!! note "Réserves de protection légitimes"
    Conformément à notre projet de statuts, les seules exceptions à la publication intégrale concernent la **protection des données personnelles (RGPD)** de nos membres et votants (données nominatives caviardées), les **secrets cryptographiques matériels** (clés protégées sous HSM) et l'**embargo temporaire de sécurité** lors du traitement coordonné de vulnérabilités critiques (*Coordinated Vulnerability Disclosure — CVD*).

## Contact et adresses officielles

- **Contact unique (Informations, Partenariats, Sécurité)** : `contact@otspi.org`  
  *(Pour le signalement de vulnérabilités / CVD : indiquer `[Sécurité]` en objet ou utiliser les [GitHub Private Security Advisories](https://github.com/otspi/organisation/security/advisories))*
- **Dépôt Git de gouvernance** : [github.com/otspi/organisation](https://github.com/otspi/organisation)
- **Portail d'information** : [about.otspi.org](https://about.otspi.org)
