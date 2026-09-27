# Organisation technique et Comité des politiques de confiance (CPC)

**Association « Open Trusted Service Provider Initiative » (OTSPI)**

---

## 1. Architecture de la gouvernance technique

La gouvernance technique de l'association repose sur une séparation stricte des rôles entre l'autorité normative cryptographique et les comités d'ingénierie logicielle et opérationnelle :

```
┌────────────────────────────────────────────────────────┐
│             Assemblée Générale & Statuts               │
└──────────────────────────┬─────────────────────────────┘
                           │
         ┌─────────────────┴─────────────────┐
         ▼                                   ▼
┌──────────────────────────┐       ┌──────────────────────────┐
│  Conseil d'Administration │       │   Comité des Politiques  │
│         & Bureau         │       │    de Confiance (CPC)    │
│  (Direction Opérationnelle│       │(PMA - Autorité Normative)│
│    Executive Management) │       │   [Article 8 bis]        │
└────────────┬─────────────┘       └─────────────┬────────────┘
             │                                   │
             ▼                                   ▼
┌──────────────────────────┐       ┌──────────────────────────┐
│ Comité Technique & Dév.  │◄──────┤ Politiques CP/CPS, TSP,  │
│   (TSC / Projets Open)   │ Avis  │ Habilitations Officiers, │
│  Ingénierie, RFCs, CI/CD │ Conforme│ Désignation du RSSI    │
└──────────────────────────┘       └──────────────────────────┘
```

---

## 2. Le Comité des politiques de confiance (CPC / PMA)

Conformément à l'**Article 8 bis des Statuts**, le CPC est l'organe collégial indépendant faisant office d'**Autorité de Gestion des Politiques (*Policy Management Authority - PMA*)** :
- **Garantie d'indépendance** : Strictement dissocié de la direction exécutive (incompatibilité absolue avec le Bureau) ;
- **Compétences exclusives** :
  - Élaboration, approbation et révision des Politiques de Certification et des Pratiques (CP/CPS, TSP) ;
  - Approbation préalable des protocoles de cérémonies de clés et déploiements HSM ;
  - Cursus d'évaluation, d'examen et d'habilitation des Officiers d'Autorité ;
  - Désignation formelle du Responsable de la Sécurité des Systèmes d'Information (RSSI / CISO) pour un mandat d'un an renouvelable ;
- **Mandat et renouvellement** : Mandat de 6 ans renouvelable par tiers tous les 2 ans, avec prise de fonction différée calée sur la clôture des cycles d'audit réglementaires.

---

## 3. Le Comité de pilotage technique (TSC — Technical Steering Committee)

Le **TSC** rassemble les ingénieurs, mainteneurs de code et experts en systèmes distribués assurant le développement et l'exploitation quotidienne des briques logicielles libres :
- **Ingénierie logicielle** : Développement des composants d'horodatage qualifié (TSA), PKI, protocoles d'émission et de validation (RFC 3161, ACME, REST/JSON, CMP, OCSP) ;
- **Maintien des dépôts open source** : Revues de code, tests automatisés, intégration continue (CI/CD) ;
- **Processus de décision par RFC (*Request for Comments*)** :
  1. *Élaboration* : Soumission d'une proposition ouverte (RFC) sur les dépôts de l'association ;
  2. *Débat public* : Consultation ouverte de 14 jours minimum ;
  3. *Vérification de conformité* : Validation que la RFC respecte les exigences du CPC et des référentiels ETSI / eIDAS ;
  4. *Adoption* : Consensus technique au sein de l'équipe d'ingénierie.

---

## 4. Politique de sécurité et signalement de vulnérabilités

La sécurité de l'infrastructure de confiance est assurée sous la coordination directe du RSSI et du CPC :
- **Signalement confidentiel** :  
  📧 **contact@otspi.org** (avec la mention `[Sécurité]` en objet ou via les GitHub Private Security Advisories) avec chiffrement PGP.
- **Protocole CVD (Coordinated Vulnerability Disclosure)** :
  - Accusé de réception sous 48 heures ouvrées ;
  - Traitement sous embargo temporaire de confidentialité ;
  - Déploiement du correctif puis publication conjointe d'un *Security Advisory* transparent (avec numéro CVE).

---

## 5. Environnements et qualification

Les services opèrent sur deux environnements strictement cloisonnés :
1. **Environnement Bac à Sable (Staging / Test)** :
   - Endpoints publics dédiés aux intégrations partenaires et tests communautaires ;
   - Fonctionnalités identiques à la production mais avec certificats de test non qualifiés.
2. **Environnement de Production Qualifiée (eIDAS / ETSI Production)** :
   - Modules matériels de sécurité (HSM) certifiés CC EAL4+ / QSCD en datacenters hautement sécurisés (SecNumCloud / ISO 27001) ;
   - Clés opérées sous contrôle strict à quatre yeux (*Dual Control*) et cérémonies formelles approuvées par le CPC ;
   - Certificats qualifiés inscrits sur la liste de confiance européenne (EU Trusted List / TSL).
