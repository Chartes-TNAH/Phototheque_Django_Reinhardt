# La Photothèque Django Reinhardt
Est une application web réalisée dans le cadre des enseignements (``CSS``, ``HTML``, ``Python`` et ``SQL``) pour le Master 2 en Technologies numériques appliquées à l'histoire, promotion 2019-2020, à l'Ecole nationale des chartes.

## Présentation du projet 
L'application vise à présenter un corpus composé d'une vingtaine de photographies de Django Reinhardt retraçant la vie du guitariste.
A partir d'une base de données ``SQLite``, le projet est développé en ``Python 3`` et utilise ``Bootstrap`` pour la mise en forme graphique.

* Une galerie globale du corpus permet donc le renvoi à partir du titre de chaque photographie sur une notice décrivant le document et présentant également le nom du photographe et sa source.
* La recherche s'effectue par mots-clefs (famille, portrait, musicien, quintette), par nom du photographe, par date, par l'orientation de l'image (portrait/paysage), ou en accès direct via la Galerie.
* Une biographie de l'auteur est proposée avec des liens vers des sources.
* Avec la création d'un compte, l'utilisateur peut enrichir la photothèque en créant une notice et téléchargeant une image. Après être connecté, l'utilisateur pourra modifier sa notice ou supprimer son image. L'utilisateur ne peut modifier que les images de son compte.

## Son installation
### :penguin: Linux 
* installer ``Python3`` et ``MySQL``
* créer un environnement virtuel dédié à l'application avec la commande ``python3 -m venv env``
* Initier le dossier créé en repository local grâce à la commande ``git init``
* Cloner le repository `Phototheque_Django_Reinhardt` : ``git clone https://github.com/Chartes-TNAH/Phototheque_Django_Reinhardt``
* Activer l'environnement virtuel avec la commande ``source env/bin/activate``
* Installer les packages nécessaires avec ``pip install -r requirements.txt``
* Se place dans `~/projet_DjangoPhoto` et lancer l'application avec la commande ``python3 run.py``

