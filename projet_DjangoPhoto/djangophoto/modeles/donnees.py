from sqlalchemy import Column, Integer, String
from ..app import db
#On importe l'objet SQLAlchemy du module flask_sqlachemy

#On crée une classe par table ; une ligne par colonne
class Image(db.Model):
    __tablename__="image"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titre = db.Column(db.String(64))
    chemin = db.Column(db.String(64), index=True, unique=True)
    date = db.Column(db.Integer)
    nom_photographe = db.Column(db.String(64))
    description = db.Column(db.String(64))
    source = db.Column(db.String(64))
    tag = db.Column(db.String(64))
    orientation = db.Column(db.String(64))
    image_valid = db.Column(db.String(2))
    
    def get_id(self):
        return(self.image_id)


    @staticmethod
    def add_img(titre, description, orientation, date, nom_photographe, source, tag, downloadlink):
        """
        Fonction qui permet d'ajouter un nouveau document dans la BDD
        :param titre: titre donné à l'image (str)
        :param description: courte présentation sur l'image (str)
        :param orientation: "portait", "paysage" (str)
        :param date: date de la photographie (str)
        :param nom_photographe: nom du photographe (str)
        :param source: Nom du propriétaire de l'image (str)
        :param tag: liste des mots-clefs (str)
        :param downloadLink: lien de téléchargement de l'image (str)
        :return:
        """
        erreurs = []
        if not titre:
            erreurs.append("Veuillez renseigner un titre pour cette image.")
        if not description:
            erreurs.append("Veuillez renseigner une description pour cette image.")
        if not orientation:
            erreurs.append("Veuillez renseigner une orientation pour cette image.")
        if not date:
            erreurs.append("Veuillez renseigner une date pour cette image.")
        if not nom_photographe:
            erreurs.append("Veuillez renseigner un nom de photographe pour cette image.")
        if not source:
             erreurs.append("Veuillez renseigner un propriétaire  pour cette image.")
        if not tag:
            erreurs.append("Veuillez renseigner une mot-clef pour cette image.")
        if not downloadlink:
             erreurs.append("Aucun lien de téléchargement pour cette image.")             
             

        image = Image(titre=titre,
                        description=description,
                        orientation=orientation,
                        date=date,
                        nom_photographe=nom_photographe,
                        source=source,
                        tag=tag,
                        chemin=downloadlink)
        # on ajoute une nouvelle entrée dans la table document avec les champs correspondant aux paramètres du modèle

        try:
            # On essaie d'ajouter une image à la BDD
            db.session.add(image)
            db.session.commit()

            return image
        except Exception as erreur:
            return False, [str(erreur)]


