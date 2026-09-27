# Politique de sécurité des systèmes d'information (PSSI)
## Conforme aux normes ISO/IEC 27001 et ETSI EN 319 401

**Association « Open Trusted Service Provider Initiative » (OTSPI)**  
*Approuvée par le Bureau (Executive Management) et le Comité des Politiques de Confiance (CPC).*

---

## 1. Objectifs, périmètre et engagement de la direction

### 1.1. Objectifs de la PSSI
La présente Politique de Sécurité des Systèmes d'Information (PSSI) a pour objet de garantir :
- La **disponibilité, l'intégrité, la confidentialité et la traçabilité** des infrastructures de confiance numérique opérées par OTSPI ;
- La conformité stricte aux exigences du **Règlement (UE) n° 910/2014 (eIDAS)** et **eIDAS 2.0 (UE 2024/1183)** ;
- L'alignement sur le standard international **ISO/IEC 27001:2022** et la norme européenne **ETSI EN 319 401** (exigences générales pour les prestataires de services de confiance).

### 1.2. Périmètre d'application
La PSSI s'applique à :
- L'ensemble des systèmes d'information, réseaux, serveurs, conteneurs et modules matériels HSM ;
- Tous les administrateurs, membres du Bureau, membres du CPC, Officiers d'Autorité, Gardiens de clés et salariés ou prestataires intervenant sur l'infrastructure.

### 1.3. Engagement de la direction opérationnelle
Le Bureau de l'association (*Executive Management* au sens de l'ETSI EN 319 401) s'engage à allouer les ressources humaines, matérielles et financières nécessaires à l'application et au contrôle continu de cette politique.

---

## 2. Organisation de la sécurité et rôles clés

Conformément à la séparation stricte des fonctions imposée par l'ETSI et WebTrust :

### 2.1. Le responsable de la sécurité des systèmes d'information (RSSI / CISO)
- **Nomination et indépendance** : Nommé par le Comité des Politiques de Confiance (CPC) pour un mandat d'un (1) an renouvelable (Article 8 bis.3 des Statuts).
- **Missions** :
  * Piloter le Système de Management de la Sécurité de l'Information (SMSI) ;
  * Mener l'analyse de risques annuelle (méthode EBIOS RM / ISO 27005) ;
  * Superviser la gestion des incidents et coordonner la divulgation des vulnérabilités (CVD) ;
  * Disposer d'une ligne de reporting direct auprès du Bureau et du CPC, en totale indépendance des équipes d'exploitation courante.

### 2.2. L'auditeur interne indépendant
- Désigné en concertation entre le CPC et le Conseil d'Administration.
- Ne peut exercer aucune fonction au sein du Bureau, ni aucune tâche opérationnelle d'administration système ou d'Officier d'Autorité.
- Réalise des audits de conformité semestriels et supervise l'audit contradictoire des scellés des Gardiens de clés.

### 2.3. Les équipes d'exploitation et d'ingénierie
- Chargées de l'administration système, du déploiement des briques logicielles libres (TSA, PKI, validateurs) et de la maintenance opérationnelle.
- Opèrent sous le principe du moindre privilège (*Least Privilege*) et ne possèdent aucun accès direct aux clés privées racines en clair.

### 2.4. Les officiers d'autorité et gardiens de clés
- Rôles de confiance soumis à habilitation préalable par le CPC, assermentation éthique et vérification d'identité (Articles 5 et 7 du Règlement Intérieur).

---

## 3. Gestion des actifs et contrôles d'accès

### 3.1. Classification des informations
Les actifs d'information sont classifiés en 4 niveaux :
1. **Public** : Spécifications RFC, codes sources open source, statuts, CP/CPS, certificats publics, CRL/OCSP, rapports d'audit.
2. **Usage Interne** : Procédures de travail, délibérations administratives non nominatives.
3. **Confidentiel / RGPD** : Données personnelles des membres et votants, identités civiles vérifiées, journaux d'accès techniques.
4. **Secret Cryptographique (Inaliénable)** : Clés privées racines et intermédiaires, secrets partagés de Shamir, codes d'activation HSM.

### 3.2. Contrôle d'accès logique et authentification forte
- Tout accès d'administration requiert une authentification multifacteur (MFA) matérielle certifiée **FIPS 140-2/3 Niveau 2+** ou **ANSSI CSPN** (Article 3 du Règlement Intérieur).
- Accès distant via bastion d'administration sécurisé avec tunnels chiffrés (SSH avec clés matérielles FIDO2 / certificats de session éphémères).
- Révocation automatique immédiate des comptes et privilèges en cas de départ ou suspension d'un intervenant.

---

## 4. Sécurité physique et opérationnelle

### 4.1. Hébergement des infrastructures
- Les modules matériels de sécurité (HSM) et serveurs d'autorité sont implantés dans des centres de données hautement sécurisés situés dans l'Union Européenne, qualifiés SecNumCloud ou certifiés ISO 27001.
- Cloisonnement réseau strict (*air-gap* pour les autorités racines hors ligne, VLANs isolés et DMZ hautement filtrée pour les services de publication).

### 4.2. Gestion des changements et durcissement système
- Application systématique du principe de *Security by Design* et *Infrastructure as Code* vérifiable.
- Tout déploiement fait l'objet d'une revue de code par les pairs et d'une validation d'intégrité (signatures cryptographiques des commits et des conteneurs).
- Systèmes d'exploitation durcis (noyaux durcis, désactivation des services inutiles, contrôle d'intégrité des fichiers).

---

## 5. Gestion des incidents de sécurité et continuité d'activité

### 5.1. Détection et journalisation (*Logging & Monitoring*)
- Journalisation centralisée et horodatée des événements de sécurité sur un serveur de logs dédié en écriture seule (WORM / *Write Once Read Many*) ;
- Les journaux d'audit de sécurité sont conservés de manière chiffrée pendant une durée minimale de **dix (10) ans** conformément à l'ETSI EN 319 401.

### 5.2. Gestion des incidents de sécurité
1. **Classification** : Tout événement anormal est qualifié sous 1 heure par le RSSI (incident mineur, majeur ou critique).
2. **Notification réglementaire obligatoire** :  
   Conformément à l'article 19 du Règlement eIDAS, toute faille de sécurité ou atteinte à l'intégrité ayant un impact significatif sur les services de confiance est **notifiée à l'autorité de contrôle compétente (ANSSI) sous 24 heures**.
3. **Révocation d'urgence** : En cas de suspicion de compromission de clé privée, les Officiers d'Autorité appliquent sans délai la procédure de révocation d'urgence (Article 8 ter des Statuts).

### 5.3. Continuité d'activité et reprise après sinistre (PCA / PRA)
- Des procédures documentées de reprise après sinistre (*Disaster Recovery Plan - DRP*) sont maintenues et testées au moins une fois par an.
- Les sauvegardes chiffrées des bases de données et des partitions HSM sont répliquées de manière asynchrone sur un site distant géographiquement séparé.

---

## 6. Révision et amélioration continue

La présente PSSI fait l'objet d'une revue annuelle obligatoire par le RSSI, le Bureau et le CPC, ainsi qu'à la suite de tout incident majeur ou évolution réglementaire substantielle.
