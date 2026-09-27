# Portail sur o2switch

Ce dossier décrit l'hébergement du portail `about.otspi.org` chez o2switch (société française, droit de l'Union), à la place de GitHub Pages (société américaine).

## Ce qui est en place

- `htaccess` : redirection HTTPS, domaine canonique, page 404, en-têtes de sécurité, compression et durées de cache. Il est copié à la racine du site au déploiement.
- `.github/workflows/deploy-o2switch.yml` : construit et contrôle le site avec l'action commune `.github/actions/build-portal` (construction stricte, accessibilité, export et validation PDF/UA-1 des PDF, mêmes contrôles que les pull requests), ajoute le `.htaccess`, puis envoie tout en FTPS (TLS obligatoire, certificat vérifié).
- Un compte FTP dédié, cantonné au seul répertoire du site. Il est renseigné dans les secrets `O2_FTP_USERNAME` et `O2_FTP_PASSWORD` du dépôt ; l'hôte est dans la variable `O2_FTP_HOST`.

## Bascule (faite le 26 septembre 2026)

1. Lancer le workflow « Déploiement du portail sur o2switch (FTPS) » à la main, puis contrôler le site en forçant la résolution : `curl --resolve about.otspi.org:443:<IP> -k https://about.otspi.org/`.
2. Basculer le DNS (zone `otspi.org`) : remplacer l'enregistrement `about` (CNAME vers `otspi.github.io`) par un enregistrement A vers l'adresse de l'hébergement.
3. Émettre le certificat Let's Encrypt dans le cPanel, puis vérifier la redirection, les en-têtes et les PDF.
4. Ajouter `push` au déclenchement de `deploy-o2switch.yml`.
5. Retirer GitHub Pages : supprimer `docs/CNAME` et `.github/workflows/deploy-pages.yml`, puis désactiver Pages dans les paramètres du dépôt.

## Précautions

- `mirror --delete` supprime les fichiers distants absents de `site/` (sauf `.ftpquota` et `cgi-bin/`, exclus) : le compte FTP ne doit donner accès qu'au répertoire du portail.
- Les adresses `https://about.otspi.org/...` doivent rester valides : le site est identique, seul l'hébergeur change.
