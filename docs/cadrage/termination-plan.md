# Plan de fin d'activité et de cessation des services de confiance
## (*Termination Plan* conforme à l'article 24.2.e du règlement eIDAS et à l'ETSI EN 319 401 § 7.12)

**Association « Open Trusted Service Provider Initiative » (OTSPI)**  
*Approuvé par le Bureau et le Comité des Politiques de Confiance (CPC).*

---

## 1. Contexte, objet et cadre légal

Conformément à l'**article 24 paragraphe 2 point e) du Règlement (UE) n° 910/2014 (eIDAS)** et à la clause 7.12 de la norme **ETSI EN 319 401**, tout prestataire de services de confiance qualifié doit maintenir un plan à jour garantissant la continuité ou la cessation ordonnée de ses activités en cas de liquidation, de faillite ou d'arrêt programmé de service.

Le présent document formalise le **Plan de Fin d'Activité (*Termination Plan*)** d'OTSPI. Il a pour but de :
1. Préserver la validité probatoire des preuves cryptographiques (horodatages, certificats, cachets) délivrées pendant leur durée d'opposabilité légale ;
2. Garantir le maintien de l'accès public aux informations de révocation (annuaires CRL et validateurs OCSP) ;
3. Organiser le transfert sécurisé et l'archivage pérenne des journaux d'audit sur une durée de **dix (10) à trente (30) ans** ;
4. Mettre en œuvre la garantie financière sanctuarisée prévue à l'**Article 12 bis des Statuts**.

---

## 2. Déclenchement du plan de fin d'activité

Le plan de fin d'activité est déclenché dans les cas suivants :
- Décision volontaire de cessation de service votée par l'Assemblée Générale Extraordinaire (Article 10 et 11 des Statuts) ;
- Révocation définitive de qualification ou retrait de l'accréditation par l'autorité nationale de contrôle (ANSSI) ;
- Dissolution statutaire ou liquidation judiciaire de l'association.

---

## 3. Procédure opérationnelle de notification et délais

Dès la décision ou le constat de cessation d'activité :

### 3.1. Notification aux autorités de contrôle (J0 à J+5)
- L'autorité nationale de contrôle compétente (**ANSSI**) et l'organisme d'évaluation de la conformité accrédité (**CAB**) sont formellement notifiés par écrit au moins **trois (3) mois avant la date effective d'arrêt de service** (sauf cas de force majeure).
- Le plan opérationnel détaillé de terminaison est soumis pour avis à l'ANSSI.

### 3.2. Notification publique aux abonnés et tiers utilisateurs (J0 à J+15)
- Information publique publiée sur le site officiel (`otspi.org`), via les canaux d'alerte API et par notification directe aux utilisateurs enregistrés ;
- Indication claire de la date limite d'émission des certificats et horodatages nouveaux ;
- Rappel des modalités d'accès pérenne aux services de vérification et de révocation.

---

## 4. Révocation des autorités et révocation des certificats

1. **Arrêt immédiat des nouvelles émissions** : Dès la date d'effet de la fin de service, aucune nouvelle clé ou certificat ne peut être émis.
2. **Génération d'une CRL finale complète** :  
   Une liste de révocation finale (*Final CRL*) couvrant l'ensemble des certificats émis non expirés est générée au sein du HSM qualifié sous double contrôle (*Dual Control*), signée et publiée.
3. **Révocation des certificats d'autorités subordonnées** : Les certificats intermédiaires sont révoqués avec le motif approprié (*cessationOfOperation*).
4. **Destruction contrôlée ou mise sous séquestre des clés privées racines** :  
   - Les clés privées actives sont révoquées puis détruites de manière irréversible selon les protocoles certifiés du HSM (zéroïsation / *zeroization* cryptographique) en présence d'un huissier de justice / commissaire de justice et de l'Auditeur Interne.
   - Un Procès-Verbal de destruction de clés est dressé et transmis à l'ANSSI.

---

## 5. Maintien des annuaires de révocation et validateurs (CRL / OCSP)

Même après l'arrêt d'émission, l'accès public aux données d'état de révocation doit être assuré pour toute la durée de validité résiduelle des certificats émis :
1. **Périmètre temporel** : Les listes de révocation finales (CRL) et validateurs d'état restent consultables publiquement pendant au moins **dix (10) ans** suivant la cessation de l'activité.
2. **Transfert d'hébergement** :  
   Les répertoires statiques de CRL et les enregistrements OCSP pré-signés sont transférés vers une infrastructure d'archivage publique ou un tiers hébergeur souverain accrédité désigné par convention.

---

## 6. Archivage probatoire à long terme des journaux d'audit (10 à 30 ans)

Conformément à l'ETSI EN 319 401 et aux exigences réglementaires de conservation de la preuve électronique :
1. **Données à archiver** :
   - Tous les journaux d'audit de sécurité, traces d'accès et logs d'événements techniques ;
   - Les dossiers d'identification des Officiers d'Autorité et des abonnés ;
   - L'ensemble des certificats émis, demandes de certificats et requêtes d'horodatage ;
   - Les procès-verbaux de cérémonies de clés et rapports d'audits de conformité.
2. **Durée de conservation** : Les archives probatoires sont conservées pour une durée minimale de **dix (10) ans**, et jusqu'à **trente (30) ans** pour les services d'horodatage qualifié et d'archivage probatoire.
3. **Tiers Séquestre d'Archives** :  
   Les données sont scellées, chiffrées et versées auprès d'un **tiers archiveur qualifié eIDAS (PSCo qualifié de conservation)** ou d'une institution publique d'archivage désignée (Archives Nationales / Caisse des Dépôts).

---

## 7. Convention de séquestre financier et fonds de garantie (article 12 bis des statuts)

Pour garantir que la fin d'activité ne sera pas compromise par une défaillance financière :
1. **Sanctuarisation du Fonds de Réserve Opérationnelle** :  
   Le fonds de réserve constitué au bilan d'OTSPI (Article 12 bis des Statuts) est dédié en **priorité absolue et préalable** au financement intégral :
   - Des frais d'hébergement et de bande passante des CRL/OCSP sur 10 ans ;
   - Du coût du séquestre d'archives probatoires auprès du tiers désigné ;
   - Des notifications légales et formalités administratives.
2. **Modalités de protection contre l'insolvabilité** :  
   Ce fonds est déposé sous forme de **compte séquestre bloqué avec affectation spéciale**, ou garanti par une **caution bancaire autonome à première demande** insaisissable par les créanciers ordinaires.
3. **Liquidation résiduelle (Article 13 des Statuts)** :  
   Ce n'est qu'après exécution complète et certifiée de l'ensemble des obligations de cessation d'activité que le liquidateur peut procéder à la dévolution de l'actif net subsistant vers l'organisme d'intérêt général successeur.
