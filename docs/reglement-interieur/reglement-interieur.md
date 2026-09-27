---
pdf: otspi-reglement-interieur.pdf
template: legal.html
hide:
  - navigation
legal:
  kicker: Règlement intérieur
  status: Projet
  titles: 2
---

# Règlement Intérieur de l'Association OTSPI
## « Open Trusted Service Provider Initiative »

*Adopté par le Conseil d'Administration après avis conforme du Comité des Politiques de Confiance (CPC), en application de l'Article 14 des Statuts.*  
*Conforme aux critères d'intérêt général (CGI art. 200 & 238 bis), aux principes directeurs d'utilité publique, aux exigences ETSI EN 319 401 / WebTrust et à la politique de redevabilité publique intégrale (Public Accountability).*

---

## Préambule

Le présent Règlement Intérieur opérationnalise les principes généraux fixés dans les Statuts de l'Association **« Open Trusted Service Provider Initiative » (OTSPI)**. Il définit les règles précises relatives :

- À la qualification des membres, à la vérification d'identité civile et à la gestion des équipements cryptographiques matériels ;
- Au cursus d'habilitation, au serment éthique et au régime des Officiers d'Autorité et des Gardiens de clés (*Key Custodians*) ;
- À la ségrégation stricte des devoirs entre la direction opérationnelle (Bureau) et l'autorité normative (CPC / PMA) ;
- Aux règles financières, barèmes de cotisation, procédures de relance et plafonds d'engagement de dépenses ;
- Aux impératifs de transparence publique, de protection des données personnelles (RGPD) et de divulgation coordonnée de vulnérabilités (CVD).

---

## Titre I — Membres, Identités Civiles et Authentification Matérielle

### Article 1 — Collèges et catégories de membres
Conformément à l'Article 5 des Statuts, l'association comprend :

1. **Membres sympathisants** : Personnes physiques ou morales soutenant les buts de l'association, à jour de cotisation. Ils disposent d'une voix consultative et exercent la faculté de refus collective prévue aux Articles 9 et 11 des Statuts.
2. **Membres titulaires** : Personnes physiques ou personnes morales dûment représentées participant de manière substantielle et active à la gouvernance, à la conformité ou aux opérations critiques. Ils disposent d'une voix délibérative pleine et entière.
3. **Membres bienfaiteurs** : Personnes morales apportant une contribution annuelle significative supérieure à cinq mille euros (5 000 € / an) sous forme de dons financiers, de mécénat matériel (serveurs, HSMs) ou de prise en charge locative. Ce statut honorifique n'ouvre aucun droit de vote (ni délibératif ni consultatif) afin de garantir la stricte neutralité et l'indépendance de l'infrastructure.
4. **Membres d'honneur** : Personnalités ayant rendu des services signalés à l'association, dispensées de cotisation sur décision du Conseil d'Administration.

### Article 2 — Vérification formelle de l'identité civile des membres titulaires
Conformément à l'Article 5 quater des Statuts, aucune voix délibérative ne peut être exercée sous statut pseudonyme ou anonyme :

1. **Procédure de contrôle d'identité préalable** :
   - Tout candidat personne physique au statut titulaire (ou tout représentant physique désigné par une personne morale membre titulaire) doit présenter une pièce d'identité officielle en cours de validité (carte nationale d'identité, passeport ou titre de séjour émis par un État souverain).
   - La vérification est effectuée soit en présentiel par un membre du Bureau ou un Officier d'Autorité, soit par un moyen de vérification d'identité à distance conforme au référentiel d'exigences PVID (Prestataire de Vérification d'Identité à Distance) de l'ANSSI ou équivalent eIDAS de niveau substantiel ou élevé.
2. **Conservation et purge des données d'identité** :  
   Les copies des pièces justificatives d'identité sont chiffrées et conservées dans un espace à accès strictement restreint sous la responsabilité du Secrétaire Général pendant la seule durée du mandat de titulaire, aux fins de justification de la régularité des scrutins devant les auditeurs et autorités de contrôle.

### Article 3 — Standard technique d'authentification matérielle et dotation
1. **Exigence d'authentification multifacteur (MFA) matérielle** :  
   L'accès aux plateformes de vote délibératif, aux systèmes de communication chiffrée interne et aux consoles d'administration requiert impérativement un mécanisme d'authentification matérielle FIDO2 / WebAuthn ou jeton cryptographique certifié au minimum :
   - **FIPS 140-2 / 140-3 Niveau 2** (ou supérieur) ;
   - Ou bénéficiant d'une **Certification de Sécurité de Premier Niveau (CSPN)** délivrée par l'ANSSI.
2. **Dotation matérielle par l'association (Article 5 quater.3 des Statuts)** :  
   L'association remet à chaque membre titulaire et Officier d'Autorité une clé de sécurité matérielle préconfigurée.
   - Ces équipements demeurent la propriété inaliénable de l'association ;
   - Un registre d'inventaire contradictoire (identifiant du jeton, numéro de série, date de remise, accusé de réception signé) est tenu par le RSSI ;
   - En cas de perte, vol ou dysfonctionnement, le titulaire a l'obligation d'en notifier sans délai le RSSI. Les certificats et accès associés sont immédiatement révoqués et une clé de remplacement est configurée.
3. **Prohibition des procurations physiques** :  
   En application de l'Article 9 bis des Statuts, les délégations de vote et procurations entre personnes physiques sont strictement nulles. Seule une personne morale peut mandater un représentant physique unique muni d'une clé matérielle configurée et enregistrée.

### Article 4 — Déchéance pour défaut d'assiduité (Article 5 ter des Statuts)
1. Tout membre titulaire absent à deux (2) sessions consécutives de l'Assemblée Générale Ordinaire sans avoir pris part aux votes (par vote électronique préalable ou en direct) perd automatiquement sa qualité de membre titulaire et bascule dans le collège des sympathisants.
2. Le Secrétaire Général notifie formellement le basculement à l'intéressé sous quinze (15) jours ouvrés.
3. Pour les personnes morales, la déchéance ne s'applique qu'après l'expiration du délai de préavis de **soixante (60) jours calendaires** imparti à la personne morale pour désigner un nouveau délégué physique habilité.

---

## Titre II — Rôles de Confiance, Officiers d'Autorité et Gardiens de Clés

### Article 5 — Cursus d'évaluation et habilitation des Officiers d'Autorité
L'Officier d'Autorité exerce un rôle de confiance critique au sens des normes ETSI EN 319 401 et WebTrust.

1. **Critères d'éligibilité** :
   - Être membre titulaire ou contributeur de l'association depuis au moins six (6) mois (sauf durant la phase d'amorçage de 24 mois visée à l'Article 5 bis.3 des Statuts) ;
   - Avoir une identité civile vérifiée et un casier judiciaire vierge (bulletin n°3 ou équivalent international de moins de 3 mois) ;
   - Justifier de compétences avérées en sécurité des systèmes d'information, administration PKI, cryptographie à clé publique et environnement Linux sécurisé.
2. **Cursus d'épreuves et habilitation sous le contrôle du CPC** :
   - Le candidat suit un cursus pratique supervisé par le CPC comprenant :
     * La maîtrise intégrale de la CP/CPS et des protocoles de cérémonies de clés ;
     * Une épreuve pratique en bac à sable (manipulation de HSM, partitionnement cryptographique, application des règles de dual-control, simulation d'incident critique) ;
     * Une épreuve théorique de conformité sur les référentiels eIDAS, ETSI et WebTrust.
   - À l'issue des épreuves, le CPC délibère et prononce, le cas échéant, l'habilitation technique formelle.
3. **Serment déontologique et engagement éthique** :  
   Avant toute prise de fonction opérationnelle, l'Officier d'Autorité prête serment et signe la **Déclaration d'Engagement Déontologique de Confiance**, par laquelle il s'engage solennellement à :
   - Préserver le secret absolu des fragments de clés et informations confidentielles dont il a connaissance ;
   - Appliquer rigoureusement les procédures sans jamais contourner les règles de double contrôle (*Dual Control*) ;
   - Exécuter sans délai toute révocation d'urgence nécessaire à la protection de la confiance publique (Article 8 ter des Statuts).
4. **Formation continue et maintien de qualification** :  
   Les Officiers d'Autorité participent obligatoirement à un exercice pratique de simulation de crise ou à un audit interne de compétences au moins une fois par an.

### Article 6 — Récusation, suspension technique et destitution d'un Officier d'Autorité
1. **Suspension conservatoire d'urgence (Article 6.3 des Statuts)** :  
   En cas d'anomalie de sécurité, de suspicion de compromission de clé, de négligence matérielle ou d'incident d'exploitation, le RSSI, le Président ou un membre du CPC peut prononcer la **suspension conservatoire immédiate** des privilèges d'accès physiques et logiques de l'Officier d'Autorité concerné. Cette mesure conservatoire n'emporte aucune sanction disciplinaire préalable et préserve les droits de la défense.
2. **Procédure contradictoire** : Le CPC instruit l'incident sous quinze (15) jours et entend l'intéressé. Le CPC peut :
   - Prononcer la levée de la suspension après vérification technique ;
   - Prescrire une formation de remise à niveau ;
   - Retirer définitivement l'habilitation d'Officier d'Autorité.
3. **Protection statutaire (Article 6.6 des Statuts)** : Le retrait de l'habilitation technique n'emporte pas exclusion disciplinaire de l'association, celle-ci ne pouvant être prononcée que dans le respect des majorités qualifiées prévues à l'Article 8 bis.

### Article 7 — Protocole des Gardiens de Clés (*Key Custodians*)
1. **Rôle et attribution des fragments de clés** :  
   Les clés privées racines ou autorités majeures font l'objet d'un secret partagé selon un schéma cryptographique vérifiable (schéma de Shamir à seuil $k$-parmi-$n$, validé par le CPC). Les fragments de secrets (*key shares*) sont confiés à des Gardiens de clés (*Key Custodians*) distincts et indépendants.
2. **Conservation physique des secrets** :
   - Chaque fragment est inscrit sur un support physique sécurisé (carte à puce cryptographique ou papier inaltérable) scellé sous **enveloppe inviolable numérotée à témoin d'effraction (*Tamper-Evident Envelope*)** ;
   - L'enveloppe est déposée dans un coffre-fort individuel sécurisé ignifuge, dont la localisation géographique est déclarée au RSSI ;
   - Il est formellement interdit à un gardien de secret de communiquer, numériser, photographier ou dupliquer son fragment sous quelque forme que ce soit.
3. **Inventaire contradictoire et restitution** :
   - Le RSSI et l'Auditeur Interne procèdent à un audit physique contradictoire annuel de l'intégrité des scellés de chaque gardien de clé ;
   - En cas de démission, de vacance ou de fin de mandat d'un gardien de secret, la restitution ou destruction contrôlée du fragment s'effectue obligatoirement en présence d'au moins deux témoins désignés par le CPC et fait l'objet d'un Procès-Verbal officiel de restitution.

---

## Titre III — Ségrégation des Fonctions et Fonctionnement du CPC

### Article 8 — Étanchéité de gouvernance et incompatibilités
Conformément à l'Article 8 bis des Statuts :

1. **Incompatibilité absolue** : Les fonctions de membre du Bureau (Président, Trésorier, Secrétaire Général) sont strictement incompatibles avec celles de membre du Comité des Politiques de Confiance (CPC) et avec celles d'Auditeur Interne indépendant.
2. **Rôle des administrateurs du CA** : Les membres du Conseil d'Administration n'exerçant pas de fonction exécutive au Bureau peuvent siéger au CPC, sous réserve de s'abstenir lors de tout vote du Conseil d'Administration portant sur la ratification ou le contrôle des décisions du CPC.
3. **Désignation du RSSI (CISO)** : Le RSSI est nommé par le CPC pour un mandat d'un (1) an renouvelable. Il rapporte techniquement au CPC et fonctionnellement au Bureau.

---

## Titre IV — Finances, Cotisations, Recouvrement et Plafonds de Dépenses

### Article 9 — Barème des cotisations annuelles et justification
1. **Principe de couverture de l'assurance et contributions** :  
   - Pour les personnes physiques, les cotisations n'ont pas vocation à financer l'infrastructure technique (qui relève des dons et du mécénat), mais à **couvrir strictement les coûts d'assurance (RC Pro et Protection Juridique)** et de gestion administrative individuelle. La contribution majeure des membres titulaires résulte de leur investissement bénévole en temps, compétences techniques et responsabilités opérationnelles.
   - Pour les personnes morales, la cotisation contribue aux frais de gouvernance, aux audits de conformité réglementaire et au fonctionnement institutionnel.
2. **Barème annuel** (exigible au 1er janvier ou à l'adhésion) :
   - **Membres sympathisants (personnes physiques)** : **15 € / an** (tarif solidaire / réduit : **5 € / an** pour étudiants et demandeurs d'emploi) ;
   - **Membres titulaires (personnes physiques)** : **10 € / an** ;
   - **Personnes morales sympathisantes** : **500 € / an** ;
   - **Personnes morales titulaires** : **2 500 € / an** ;
   - **Membres bienfaiteurs (personnes morales)** : Statut octroyé pour une contribution annuelle significative **supérieure à 5 000 € / an** (en dons financiers, dons de matériels ou prise en charge de locations/hébergement). Ce statut n'ouvre aucun droit de vote.
3. **Mécénat et dons complémentaires** :  
   Tout versement excédant ces montants statutaires constitue un don d'intérêt général ouvrant droit à la réduction d'impôt (articles 200 et 238 bis du CGI).

### Article 10 — Procédure de relance et échéancier de non-paiement (Article 6.2 des Statuts)
1. **Calendrier de relance** :
   - **Échéance (J0)** : Envoi de l'avis d'appel de cotisation par voie électronique ;
   - **Premier rappel (J+30)** : Rappel amiable par courriel en cas de non-paiement ;
   - **Deuxième rappel (J+45)** : Relance avec avertissement sur la suspension des droits de vote ;
   - **Mise en demeure formelle (J+60)** : Notification formelle par lettre recommandée électronique (LRE) ou courriel certifié accordant un **délai ultime de trente (30) jours calendaires**.
2. **Conséquences à l'expiration du préavis de 30 jours (J+90)** :
   - *Membres ordinaires* : Radiation automatique d'office de l'association ;
   - *Régime dérogatoire de sécurité (Article 6.2 des Statuts)* : Pour les administrateurs, membres du CPC, Officiers d'Autorité et Gardiens de secrets, aucune radiation automatique n'est prononcée. Leurs habilitations et actes techniques demeurent pleinement valides et opposables. Seul l'exercice personnel du droit de vote en AG est suspendu jusqu'à régularisation.

### Article 11 — Plafonds d'engagement de dépenses autonomes du Bureau
Afin de concilier réactivité opérationnelle et contrôle budgétaire de l'Assemblée et du Conseil d'Administration :

1. **Dépenses courantes autonomes du Bureau** : Le Président et le Trésorier peuvent engager conjointement les dépenses d'exploitation courante (abonnements d'infrastructure d'hébergement, télécoms, petit matériel, frais de mission justifiés) dans la limite d'un plafond de **cinq mille euros (5 000 €) hors taxes par opération**, dans le cadre du budget annuel voté.
2. **Autorisation préalable obligatoire du Conseil d'Administration** : Requiert une délibération préalable du Conseil d'Administration :
   - Tout investissement matériel unitaire ou contrat de prestation excédant **cinq mille euros (5 000 €) HT** ;
   - Tout contrat de bail ou engagement financier pluriannuel récurrent d'un montant annuel supérieur à **dix mille euros (10 000 €) HT** ;
   - La souscription de tout emprunt ou ligne de crédit (sous réserve de l'approbation de l'AG conformément à l'Article 10 des Statuts).

---

## Titre V — Redevabilité Publique, RGPD et Divulgation Responsable (CVD)

### Article 12 — Principe de publication intégrale des travaux
En application de l'Article 2 des Statuts, l'ensemble des délibérations, budgets prévisionnels, comptes annuels certifiés, rapports moraux, résolutions normatives du CPC et rapports d'audit de conformité (ETSI, eIDAS, WebTrust) sont publiés en libre accès sur le dépôt public de l'organisation.

### Article 13 — Caviardage RGPD
Avant toute mise en ligne, les coordonnées privées (adresses postales personnelles, numéros de téléphone et e-mails privés) des membres et votants sont systématiquement expurgées. Seuls les dirigeants légaux mentionnés au registre préfectoral apparaissent avec leur identité civile officielle.

### Article 14 — Divulgation coordonnée de vulnérabilités (*Coordinated Vulnerability Disclosure — CVD*)
1. Tout signalement de vulnérabilité technique reçu sur `contact@otspi.org` (avec mention `[Sécurité]` en objet) ou via les outils de divulgation sécurisée de la plateforme de développement est placé sous embargo temporaire de confidentialité.
2. La période d'embargo n'excède pas quatre-vingt-dix (90) jours, sauf accord mutuel motivé par la complexité de déploiement d'un correctif matériel ou cryptographique.
3. À l'issue du déploiement en production, un avis de sécurité public (*Security Advisory*) avec CVE est publié en toute transparence.

---

## Titre VI — Droit d'Évocation à Cinq (5) Membres

### Article 15 — Mise en œuvre du droit d'évocation
1. Conformément à l'**Article 14 alinéa 3 des Statuts**, toute modification du présent Règlement Intérieur arrêtée par le Conseil d'Administration est notifiée aux membres par voie électronique.
2. Dès cette notification, la demande conjointe formulée par au moins **cinq (5) membres** à jour de leurs obligations (titulaires ou sympathisants) oblige le Conseil d'Administration à convoquer une **Assemblée Générale sous un délai maximal de trente (30) jours calendaires** pour statuer souverainement sur le texte contesté.
3. La demande d'évocation suspend l'application de la clause contestée jusqu'au vote souverain de l'Assemblée Générale.
