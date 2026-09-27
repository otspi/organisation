# Documents de cadrage stratégique et socle de conformité initial (TSP / PKI)

**Association « Open Trusted Service Provider Initiative » (OTSPI)**

Ce dossier rassemble l'ensemble des documents de cadrage stratégique, réglementaire et technique constituant le **socle d'audit initial** d'OTSPI, soumis à l'approbation conjointe du **Comité des Politiques de Confiance (CPC / PMA)** et du **Bureau (Executive Management)** avant toute cérémonie de clé.

---

## Le socle de conformité initial (corpus d'audit)

1. **[Cadre Général des Politiques de Certification et Pratiques (CP/CPS)](cp-cps-cadre.md)** :
   - Document maître conforme à la **RFC 3647**, à l'**ETSI EN 319 401**, à l'**ETSI EN 319 411-1 / 411-2** et aux exigences **WebTrust / CA/Browser Forum** ;
   - Régit l'ensemble du cycle de vie des clés et certificats (génération en HSM qualifié, profils d'émission, algorithmes cryptographiques autorisés, procédures de révocation d'urgence sous 24h/1h).

2. **[Politique de Sécurité des Systèmes d'Information (PSSI)](pssi.md)** :
   - Conforme aux standards internationaux **ISO/IEC 27001:2022** et européens **ETSI EN 319 401** ;
   - Définit l'organisation de la sécurité, le rôle indépendant du RSSI (CISO) nommé par le CPC, le statut de l'Auditeur Interne indépendant, le contrôle d'accès avec authentification matérielle FIPS/ANSSI, et la procédure de notification des incidents de sécurité (ANSSI sous 24h).

3. **[Plan de Fin d'Activité et Cessation de Service (*Termination Plan*)](termination-plan.md)** :
   - Conforme à l'**article 24.2.e du Règlement eIDAS** et à la clause 7.12 de l'**ETSI EN 319 401** ;
   - Organise le maintien de la disponibilité publique des annuaires de révocation (CRL / OCSP) pendant au moins 10 ans ;
   - Fixe le protocole d'archivage probatoire des journaux d'audit sur 10 à 30 ans auprès d'un tiers séquestre qualifié ;
   - Met en œuvre le **fonds de réserve opérationnelle sanctuarisé** (Article 12 bis des Statuts).

4. **[Arc d'identifiants d'objet (OID) et numéro d'entreprise IANA](oid-arc.md)** :
   - Plan d'obtention d'un numéro d'entreprise auprès de l'IANA, au nom de l'association ;
   - Allocation de l'arc, séparation du test et de la production, et plan de remplacement de l'OID de test dans le moteur.

---

## Documents complémentaires de cadrage

- **[Livre blanc](../livre-blanc/index.md)** : vision et modèle d'intérêt général à but non lucratif inspiré de l'ISRG / Let's Encrypt appliqué aux services qualifiés eIDAS.
- **[Manifeste pour une identité numérique libre et ouverte](https://www.otspi.org/manifeste.html)** : dix principes ouverts à la signature des personnes et des organisations.
- **Politique d'Horodatage (*Time-Stamping Policy - TSP*)** : Profils d'horodatage qualifié conformes à l'ETSI EN 319 421 / 422 et RFC 3161.
- **Feuille de Route Institutionnelle et Technique (*Roadmap*)** : Calendrier d'évaluation de la conformité (CAB), intégration EUDI Wallet (eIDAS 2.0) et préparation aux algorithmes post-quantiques.

---

## Principes d'auditabilité et de sécurité

- Tous les documents de cadrage normatifs sont publics et consultables en libre accès dans le cadre de la redevabilité publique intégrale ;
- Les seules exceptions concernent les secrets cryptographiques matériels (clés sous séquestre HSM) et les embargos temporaires de sécurité sur les vulnérabilités non corrigées (*Coordinated Vulnerability Disclosure*).
