# Cadre général des politiques de certification et pratiques (CP/CPS)
## Conforme à la RFC 3647, ETSI EN 319 401, ETSI EN 319 411-1 / 411-2 et WebTrust

**Association « Open Trusted Service Provider Initiative » (OTSPI)**  
*Document soumis à l'approbation du Comité des Politiques de Confiance (CPC) et du Bureau avant toute cérémonie de clé.*

---

## 1. Introduction

### 1.1. Vue d'ensemble
Le présent document définit les Politiques de Certification (*Certificate Policy - CP*) et la Déclaration des Pratiques de Certification (*Certification Practice Statement - CPS*) pour l'ensemble des infrastructures à clés publiques (PKI), services d'horodatage qualifié (TSA) et services de confiance opérés par l'association **« Open Trusted Service Provider Initiative » (OTSPI)**.

### 1.2. Dénomination du document et identification
- **Titre** : Cadre Général CP/CPS d'OTSPI
- **OID Racine** : `1.3.6.1.4.1.XXXXX` (Attribution IANA OTSPI)
- **Applicabilité** : Certificats racines, autorités de certification subordonnées, certificats d'horodatage qualifié (RFC 3161), certificats de cachet et de signature conformes au Règlement (UE) n° 910/2014 (eIDAS) et eIDAS 2.0 (UE 2024/1183).

### 1.3. Participants à la PKI
- **Autorité de Gestion des Politiques (PMA)** : Le **Comité des Politiques de Confiance (CPC)** d'OTSPI (Article 8 bis des Statuts), garant exclusif de la conformité normative et de l'intégrité cryptographique.
- **Direction Opérationnelle (*Executive Management*)** : Le **Bureau** de l'association (Président, Trésorier, Secrétaire Général).
- **Officiers d'Autorité** : Opérateurs habilités par le CPC assurant sous double contrôle (*Dual Control*) les cérémonies de clés et les opérations de révocation d'urgence.
- **Gardiens de clés (*Key Custodians*)** : Détenteurs des fragments de secrets des clés racines partagées selon le schéma de Shamir à seuil.
- **Utilisateurs / Tiers de confiance (*Relying Parties*)** : Toute entité, citoyen ou système validant les preuves cryptographiques ou certificats émis par OTSPI.

---

## 2. Répertoires de publication et référentiels

### 2.1. Répertoires publics
OTSPI maintient un répertoire accessible publiquement, de façon continue (24h/24, 7j/7), neutre et gratuite, contenant :
- Les certificats des autorités racines et intermédiaires ;
- Les listes de révocation de certificats (CRL) à jour et signées ;
- Les répondeurs en ligne du protocole d'état de certificat (OCSP) ;
- Les versions approuvées de la CP/CPS, du Règlement Intérieur et de la PSSI.

### 2.2. Disponibilité et SLA
La disponibilité des services de publication de révocation (CRL/OCSP) fait l'objet d'un engagement de haute disponibilité (au minimum 99,9 % de temps de fonctionnement, hors maintenance programmée approuvée par le CPC).

---

## 3. Identification et authentification (I&A)

### 3.1. Enregistrement initial
- **Officiers d'Autorité et Gardiens de clés** : Identification civile formelle en présence physique ou par PVID qualifié, vérification du casier judiciaire, serment déontologique (Article 5 du Règlement Intérieur).
- **Entités et abonnés de certificats** : Vérification des identités civiles et représentations morales conformément aux normes ETSI EN 319 411-1/2 et aux exigences du profil de certificat applicable.

### 3.2. Clés et jetons matériels
Tous les accès administratifs et d'émission requièrent des clés matérielles FIDO2/WebAuthn certifiées FIPS 140-2/3 Niveau 2+ ou ANSSI CSPN (Article 3 du Règlement Intérieur).

---

## 4. Exigences opérationnelles du cycle de vie des certificats

### 4.1. Demande et émission de certificats
Toute demande de certificat suit un processus automatisé ou validé par un Officier d'Autorité selon le profil d'usage. L'émission est signée exclusivement au sein d'un module matériel de sécurité (HSM) qualifié.

### 4.2. Révocation des certificats
- **Motifs de révocation** : Suspicion ou constat avéré de compromission de clé privée, changement des informations du sujet, fin d'activité de l'entité, cessation de service.
- **Délégation et révocation d'urgence** : En application de l'**Article 8 ter alinéa 2 des Statuts**, les Officiers d'Autorité disposent des pleins pouvoirs pour ordonner et exécuter sans délai la révocation d'un certificat en cas d'urgence opérationnelle ou de compromission, sans délibération préalable du Bureau ou du CA.
- **Délais de traitement** : Révocation publiée sous **24 heures** maximum pour une clé de certificat final, et sous **1 heure** en cas de compromission critique avérée d'une autorité intermédiaire.

---

## 5. Contrôles de sécurité physique, environnementale et procédurale

### 5.1. Sécurité physique des sites d'hébergement
Les composants serveurs et modules HSM sont hébergés au sein de datacenters certifiés ISO/IEC 27001 et qualifiés SecNumCloud (ou équivalent européen souverain), situés exclusivement sur le territoire de l'Union Européenne :
- Contrôle d'accès biométrique et par badge renforcé ;
- Vidéosurveillance continue 24/7 avec rétention des enregistrements pendant au moins un (1) an ;
- Protection incendie gaz inerte, redondance électrique N+1 et climatisation secourue.

### 5.2. Contrôle à quatre yeux (*Dual Control*) et séparation des devoirs
Toute opération sur les HSM ou sur les clés racines (génération, sauvegarde, restauration) requiert la présence physique ou logique simultanée d'au moins **deux (2) Officiers d'Autorité habilités** détenant des fragments de secrets ou jetons d'activation distincts (Article 5 alinéa 2 du Règlement Intérieur).

---

## 6. Contrôles techniques de sécurité et cycle de vie des clés

### 6.1. Modules matériels de sécurité (HSM)
- Les clés privées racines et intermédiaires sont générées et stockées exclusivement au sein de modules HSM certifiés **Common Criteria EAL 4+ (profil de protection EN 419 221-5)** ou **FIPS 140-2 / 140-3 Niveau 3**.
- Les clés privées ne quittent jamais le périmètre cryptographique du HSM en clair.

### 6.2. Algorithmes cryptographiques et tailles de clés
Conformément aux référentiels ETSI TS 119 312 et aux recommandations de l'ANSSI :
- **Autorités Racines (Root CA)** : RSA 4096 bits ou courbes elliptiques (ECDSA P-384 / Ed25519) avec fonction de hachage SHA-384 / SHA-512.
- **Autorités Intermédiaires et Horodatage (TSA)** : RSA 3072 bits minimum ou ECDSA P-256 / P-384 avec fonction de hachage SHA-256 minimum.
- **Feuille de route post-quantique** : Préparation des profils de transition hybrides (algorithmes post-quantiques normalisés NIST / ANSSI).

### 6.3. Cérémonies de clés cryptographiques (*Key Generation Ceremonies*)
- Toute génération de clé racine fait l'objet d'un protocole scripté préalablement approuvé par le CPC.
- La cérémonie se déroule en présence d'un auditeur interne ou témoin indépendant assermenté.
- Un Procès-Verbal de Cérémonie de Clés complet est rédigé, signé par l'ensemble des participants et rendu public (hors fragments secrets).

---

## 7. Profils de certificats, de CRL et d'horodatage

1. **Profils X.509 v3** : Conformes aux normes IETF RFC 5280 et profils ETSI EN 319 412 (parties 1 à 5).
2. **Profils d'horodatage qualifié** : Conformes à la RFC 3161 et ETSI EN 319 421 / 422.
3. **Profils CRL v2** : Émission périodique (au moins toutes les 24 heures pour les intermédiaires, et à chaque révocation immédiate) signée par l'autorité émettrice.

---

## 8. Audit de conformité et évaluation

1. **Audits internes périodiques** : Réalisés sous la responsabilité de l'Auditeur Interne indépendant nommé en coordination avec le CPC.
2. **Audits externes d'accréditation** : Conduits au moins tous les deux (2) ans (avec audits de surveillance annuels) par un organisme d'évaluation de la conformité (*Conformity Assessment Body - CAB*) accrédité selon la norme ISO/IEC 17065 et ETSI EN 319 403 / 403-1.
3. **Publication des rapports d'audit** : Les attestations d'audit (*Audit Attestations*) sont publiées dans le cadre de la redevabilité publique intégrale.

---

## 9. Dispositions légales, responsabilités et droit applicable

1. **Inaliénabilité des clés et séquestre** : Les clés privées sont insaisissables et sous séquestre technique exclusif (Article 8 ter des Statuts).
2. **Garanties financières et RC Pro** : Couverture par le fonds de réserve opérationnelle (Article 12 bis des Statuts) et police d'assurance responsabilité civile professionnelle souscrite par l'association.
3. **Droit applicable et juridiction** : Les présentes pratiques sont régies par le droit français et les règlements de l'Union Européenne. Les juridictions compétentes du ressort de la Cour d'Appel de Lyon sont seules compétentes.
