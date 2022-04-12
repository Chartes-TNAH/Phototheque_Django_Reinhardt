## Phase d'installation

- `git init` inutile
- `MySLQ` inutile?
- Erreur: se déplacer dans `./projetDangoPhoto` et non `~/`

## Lancement

- Le premier lancement ne fonctionne pas: la fonction `secure_filename` ne fonctionne pas car mauvaise version de Werkzeug
	- Bug connu il y a 17 mois: donc pas de tentative de réinstallation avant soumission
	https://stackoverflow.com/questions/61628503/flask-uploads-importerror-cannot-import-name-secure-filename

## Hygiène du code

- Problème d'indentation ici et là (exemple: fichier donnees.py, ligne 77-86)
- 2 fichiers inutiles dans routes (api et generic.py)
- Les noms de variables: éviter les noms commençant par des majuscules pour les instances: il faut réserver cela aux classes
- Les imports dans `routes/__init__.py` sont illogiques ou répétés, proposition de correction:

```python
from djangophoto.app import app, login, db
from djangophoto.modeles.donnees import Orientation_img, Tag_img, Image, Authorship
from djangophoto.modeles.utilisateurs import User
from djangophoto.utils import lenTitle, lenDesc, extension_ok
from djangophoto.constantes import DOSSIER_UPLOAD
```

## Modeles

Note générale:

Une seule table est véritablement modifiable: celle des photos. Il n'y a aucune gestion dynamique des mots clefs, des photographes... Un mot clef n'est pas un mot-clef s'il est "unique": c'est une catégorie.
On regrette donc la très faible utilisation du moteur relationnel et de ses capacités.

### Partie SQL

- La table `Orientation_img` est inutile: elle ne fournit aucune fonctionnalité qu'un champ ne pourrait pas offrir
- La table `Tag_img` n'est pas réellement utilisée, dans la mesure où sa clef primaire est aussi sa seule valeur. Par ailleurs, on attend, pour un système de `tags`, d'avoir une relation N-to-N
- La date en `integer` est probablement une erreur mais pose  problème
- Le champ image_valid n'est jamais utilisé.

### Partie Python

- La fonction get_id ne sert à rien.
- `return` ne prend pas de parenthèse (fonction `get_id()`)

### Mixte

- Il n'est pas normal de sauvegarder un tag HTML là où un chemin aurait suffit (Image.chemin), forçant à des bidouillages (`deleteImg.chemin [21:-14]`)
- Vu la situation, le nom du fichier aurait suffit (083.jpg): sauvegarder le nom complet du fichier pose un problème pour des maintenances futures (changement de dossier par exemple)
- La mise à jour de l'imag ede permet pas de changer l'image
- Où est utilisé paysage vs. portrait ?

## Fonctionnalités

- Pas de pagination
- Pas de possibilité de mise à jour des images
- Moteur de recherche "simple"
- La page `liste` n'utilise pas `Authorship`. Dans cette même page, la fonction `group_by` ne fait pas sens car des personnes peuvent partager le même nom de famille.


## Code

- Les lignes 204-206 ne servent à rien dans `routes/__init__.py` car elles ne peuvent pas être atteintes
- Le carousel n'est pas dynamique: si je supprime les images, il ne marche plus
- Dans le HTML, il reste des liens qui n'utilisent pas `url_for` (biographie.html)
- Vous pourriez simplifier:

```python
            {% for clef in tag_img %}
            {% if clef.tag_mot == updateImg.tag %}
            <option value="{{clef.tag_mot}}" selected>{{clef.tag_mot}}</option>
            {% else %}
            <option value="{{clef.tag_mot}}">{{clef.tag_mot}}</option>
            {% endif %}
            {% endfor %}

```

en 
```python
{% for clef in tag_img %}
	<option value="{{clef.tag_mot}}" {% if clef.tag_mot == updateImg.tag %} selected {%endif}>{{clef.tag_mot}}</option>
{% endfor %}

```
- Votre bouton ligne 87 dans update-image n'est pas dans sa colonne.

# Notes

## Note SQL : 9

Vous ne faites pas vraiment usage des possibilités de SQL et le modèle pose quelques problèmes (y compris quand on voit en base ensuite des valeurs non numériques dans des champs numériques).

## Note python: 7.5

Des progrès, mais encore loin de ce qui était attendu: vous restez à la surface des possibles et ne remplissez pas la feuille de route que nous avions établi, à savoir produire une véritable application qui mette en valeurs vos compétences. 
