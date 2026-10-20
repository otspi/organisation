# Arc d'identifiants d'objet (OID) d'OTSPI

## Plan d'obtention d'un numéro d'entreprise IANA et d'allocation de l'arc

!!! note "Statut du document"
    Document de cadrage, version 0.2, en cours d'examen par le Comité des Politiques de Confiance (CPC). La demande auprès de l'IANA a été déposée le 25 septembre 2026 au nom de l'initiative (demande n° PHTU-RTZ-60K). **Le numéro d'entreprise 67027 a été attribué** (constaté le 5 octobre 2026) ; l'arc d'OTSPI est donc `1.3.6.1.4.1.67027`. Le titulaire enregistré reste l'initiative : il doit être transféré à l'association (§2).

---

## 1. Pourquoi un arc d'OID propre

Les jetons d'horodatage, les certificats et les politiques d'OTSPI portent des **identifiants d'objet (OID)**. Ces identifiants sont gravés dans des preuves qui doivent rester vérifiables pendant des décennies : ils ne peuvent ni changer, ni être réutilisés, ni appartenir à un tiers.

Le service de staging utilise aujourd'hui l'OID de test `1.3.6.1.4.1.99999.1.1.1`. Ce choix était acceptable pour un banc d'essai, mais il ne peut pas être conservé :

- le numéro d'entreprise `99999` n'est pas réservé à l'usage de test. Le registre IANA des numéros d'entreprise (*Private Enterprise Numbers*, PEN), mis à jour le 24 septembre 2026, en est au numéro 66 956 et les attribue dans l'ordre : **le numéro 99999 sera un jour attribué à une autre organisation**, qui deviendrait alors titulaire légitime de l'arc que nous utilisons ;
- un OID de politique doit relever d'un arc **dont OTSPI est titulaire**, conformément à l'ETSI EN 319 401 et à l'ETSI EN 319 421 (identification de la politique d'horodatage).

## 2. Titulaire de l'attribution : l'association, pas une personne

L'IANA accepte les attributions au nom d'une organisation ou d'une personne physique. Pour OTSPI, le titulaire doit être **l'association**, pour deux raisons :

- l'arc d'OID fait partie des actifs immatériels inaliénables du projet (article 13 du projet de statuts) et ne doit pas dépendre d'une personne ;
- une attribution personnelle créerait une dépendance à un individu pour un identifiant destiné à durer plus longtemps que ses fondateurs.

**Calendrier recommandé.**

| Situation | Démarche |
|---|---|
| Association déclarée en préfecture (numéro RNA obtenu) | Déposer la demande au nom de l'association. **Voie à privilégier.** |
| Déclaration pas encore effectuée | Déposer la demande au nom de l'initiative (« Open Trusted Service Provider Initiative (OTSPI) »), avec une adresse de contact de rôle, puis faire mettre à jour le titulaire auprès de l'IANA dès la déclaration de l'association. |

La demande est **gratuite** ; l'IANA envoie un e-mail de confirmation à l'adresse indiquée et, sans complément d'information à fournir, l'attribution intervient dans les sept jours suivant la réponse.

## 3. Informations de la demande

Le formulaire IANA comporte une section *Assignee* et une section *Contact*. Les informations du registre sont **publiques** : elles doivent donc être limitées à celles qui peuvent l'être.

| Champ | Valeur prévue |
|---|---|
| Organisation | Open Trusted Service Provider Initiative (saisi sans le sigle) |
| Adresse et pays | 254 rue Vendôme, 69003 Lyon, France (adresse de domiciliation du siège) |
| Contact (nom) | Un intitulé de rôle plutôt qu'un nom de personne : « OTSPI Registry Contact » |
| Contact (e-mail) | `contact@otspi.org` (adresse de rôle, non nominative) |
| Téléphone, fax | Non renseignés (facultatifs) |

L'adresse de contact doit rester relevable à long terme : elle servira à la confirmation initiale et à toute mise à jour ultérieure de l'attribution.

## 4. Allocation de l'arc

Notation : `<PEN>` désigne le numéro d'entreprise d'OTSPI, **67027**, sous l'arc `1.3.6.1.4.1.<PEN>` (soit `1.3.6.1.4.1.67027`).

| Arc | Usage |
|---|---|
| `<PEN>.1` | Politiques de service (production) |
| `<PEN>.1.1` | Politiques d'horodatage (TSA) ; `<PEN>.1.1.1` : première politique d'horodatage |
| `<PEN>.1.2` | Politiques de cachet et de signature (réservé) |
| `<PEN>.1.3` | Politiques de certificats TLS (réservé) |
| `<PEN>.2` | Politiques de certification (CP/CPS) |
| `<PEN>.2.9` | Politiques de certification **internes** au système (certificats du lien entre console et autorité, jamais délivrés au public) |
| `<PEN>.3` | Extensions et attributs |
| `<PEN>.3.1` | Extension de CRL listant les numéros de série émis (usage interne au moteur) |
| `<PEN>.9` | **Test et staging**, qui reproduit à l'identique la structure ci-dessus (ex. `<PEN>.9.1.1.1`) |

Règles de gestion :

1. **Séparation stricte du test et de la production.** Un jeton émis par le staging ne doit jamais pouvoir être pris pour un jeton de production : le staging utilise uniquement l'arc `<PEN>.9`.
2. **Immuabilité.** Un OID publié n'est jamais réutilisé ni modifié ; une évolution de politique donne un nouvel OID (dernier arc incrémenté).
3. **Registre public.** Chaque attribution est consignée dans un registre publié dans le dépôt de gouvernance, avec sa date, son objet et le document de référence.
4. **Approbation par le CPC.** Toute nouvelle branche de l'arc est approuvée par le CPC, comme les politiques de certification et de service dont il a la charge (article 8 bis du projet de statuts).
5. **Conformité à la politique de référence.** La Politique d'Horodatage d'OTSPI déclare sa conformité à la politique *Best Practices Time-Stamp Policy* de l'ETSI EN 319 421 (OID `0.4.0.2023.1.1`). La forme exacte de cette déclaration (OID propre référençant la BTSP, ou reprise directe de l'OID de l'ETSI) est à arrêter avec l'organisme d'évaluation de la conformité lors de la phase 2.

## 4 bis. Registre des attributions

Registre des identifiants effectivement alloués (règle 3). Une ligne n'est ajoutée qu'après approbation du CPC ; la colonne « Statut » le dit.

| OID | Objet | Document de référence | Date | Statut |
|---|---|---|---|---|
| `1.3.6.1.4.1.67027` | Numéro d'entreprise IANA d'OTSPI (titulaire : l'initiative, à transférer à l'association) | Demande IANA PHTU-RTZ-60K du 25 septembre 2026 | 2026-10-05 (constat) | Attribué |
| `1.3.6.1.4.1.67027.9.1.1.1` | Politique d'horodatage de **test** et de staging | Ce document, §5 | 2026-10-05 | Posé dans le moteur ; à approuver par le CPC |
| `1.3.6.1.4.1.67027.2.9.1` | Politique de certification interne : certificat client de la console | Moteur, `docs/CA.md` | 2026-10-05 | **Proposé**, en attente du CPC |
| `1.3.6.1.4.1.67027.2.9.2` | Politique de certification interne : certificat serveur de l'autorité | Moteur, `docs/CA.md` | 2026-10-05 | **Proposé**, en attente du CPC |
| `1.3.6.1.4.1.67027.3.1` | Extension de CRL : numéros de série émis | Moteur, constat O-1 de l'audit du 25 septembre 2026 | 2026-10-05 | **Proposé**, en attente du CPC |

Les trois OID internes ont remplacé des valeurs provisoires placées sous le numéro `0` (`1.3.6.1.4.1.0.1.1` à `.3`), qui n'appartenaient à personne. Elles n'ont jamais figuré dans un certificat ou une CRL délivrés à un tiers.

## 5. Plan de remplacement dans le code

Le remplacement est essentiellement une affaire de **configuration** : l'OID de politique du moteur est lu dans la variable d'environnement `OPENEIDAS_POLICY_OID`. Il faut néanmoins traiter **toutes** les occurrences de la valeur de test, aujourd'hui au nombre de 18 dans le dépôt du moteur :

| Élément | Fichier |
|---|---|
| Valeur par défaut de la configuration et test associé | `crates/oe-config/src/lib.rs` |
| Tests d'intégration et de bout en bout | `crates/oe-crosstsa/tests/`, `crates/oe-httpapi/tests/`, `crates/oe-tsa-core/tests/`, `crates/oe-tsa-core/src/lib.rs` |
| Déploiement | `deploy/helm/open-eidas/values.yaml`, `docker-compose.yml` |
| Documentation | `docs/API.md`, `docs/ARCHITECTURE.md`, `docs/CPS.md` |

État au 5 octobre 2026 : le remplacement des 18 occurrences de la valeur de test par `<PEN>.9.1.1.1`, et des trois OID provisoires internes, est préparé dans une modification du dépôt du moteur (script `scripts/set-oid-arc.sh`), en attente de revue et de fusion. Le staging doit aussi recevoir la nouvelle valeur de `OPENEIDAS_POLICY_OID`, et les certificats internes déjà émis doivent être réémis (ils portent l'ancien OID provisoire).

Séquence :

1. Obtenir le numéro d'entreprise et l'enregistrer dans le registre d'OID.
2. Remplacer la valeur de test par `<PEN>.9.1.1.1` (arc de **test**) partout, y compris dans la configuration du staging.
3. Ne renseigner l'OID de production `<PEN>.1.1.1` qu'au moment de la mise en service du service qualifié, après approbation de la Politique d'Horodatage par le CPC.
4. Faire échouer la mise en production si l'OID configuré appartient à l'arc de test (garde-fou à prévoir dans le moteur).

Les jetons déjà émis par le staging sous l'ancien OID n'ont aucune valeur juridique et n'ont pas à être migrés.

## 6. Prochaines étapes

- [ ] Décision du CPC sur le titulaire de l'attribution (association ou initiative)
- [x] Dépôt de la demande auprès de l'IANA (25 septembre 2026)
- [x] Attribution du numéro d'entreprise **67027** (constatée le 5 octobre 2026)
- [ ] Mise à jour du titulaire au nom de l'association après sa déclaration
- [ ] Approbation par le CPC de l'allocation des OID internes (`2.9.x`, `3.1`) et de l'OID de test
- [x] Registre d'OID : première version au §4 bis (à publier après approbation du CPC)
- [ ] Remplacement de l'OID de test dans le moteur (préparé) et le staging
- [ ] Garde-fou de mise en production
