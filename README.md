# ceves-site-web-version-1

## Programmes à installer

* [Python 3.7+](https://www.python.org/downloads/)
* [Git](https://git-scm.com/)
* Éditeur de code (exemple Atom, Sublime)

Pour Python, il faut assurer que les environment variables pour `python` et `pip` sont bien configurés (pour Windows, il faut taper "Environment Variables" dans start bar)

## Démarrage du site web

**Cloner le site web**
Dans un Terminal (par exemple cmd):
Pour cloner le GitHub du site web:
```
git clone https://github.com/wat3rfall/ceves-site-web-version-1.git
```
Pour se glisser dans la branche `dev/main`:
```
git checkout dev/main
```

**Installation des dépendances**
```
pip3 install -r requirements.txt
```

**Démarrage du site web**
```
python app.py
```

**Accès au site web via localhost**
Tapez dans le bar URL d'un browser (exemple Google Chrome):
```
http://localhost:5000
```
Vous devriez voir un message d'accueil!

## Description du repository

**Dossiers**

**src**: dossier avec du code Python

**static**: dossier avec le contenu statique

**-css**: dossier avec les fichiers CSS

**-img**: dossier avec des images

**templates**: dossier avec les pages HTML

**Fichiers**

*app.py*: fichier Python principal

*README.md*: fichier avec des renseignements sur le projet

*requirements.txt*: fichier avec les dépendances

## Commandes Git

Quelques commandes de base utiles

Télécharger le site web
`git clone https://github.com/wat3rfall/ceves-site-web-version-1.git`

Vérifier la nature d'une branche git
`git status`

Créer une nouvelle branche
`git branch <nom de ta nouvelle branche>`

Changer de branche
`git checkout <nom de la branche à changer>`

Ajouter des fichiers modifiés
`git add .` pour tous les fichiers modifés
`git add <nom de fichier ou dossier>` pour certains fichiers modifiés

Sauvegarder les fichiers modifiés (avec commit)
`git commit -m <message de commit>`

Pousser des modifications à une branche particulière
`git push <nom de branche>`

Et sur GitHub, on peut faire:
* des *pull request* pour des requêtes de fusionner des branches
