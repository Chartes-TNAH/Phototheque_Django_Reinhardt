from flask import url_for, flash
from flask_login import login_user, current_user, logout_user
from djangophoto.constantes import DOSSIER_UPLOAD
import os
import datetime

from sqlalchemy import Column, Integer, String

from .. app import db
#On importe l'objet SQLAlchemy du module flask_sqlachemy

#On crée une classe par table ; une ligne par colonne
class Orientation_img(db.Model):
    orientation_type = db.Column(db.String(64), unique=True, nullable=False, primary_key=True)

class Tag_img(db.Model):
    tag_mot = db.Column(db.String(64), unique=True, nullable=False, primary_key=True)

#On crée une classe par table ; une ligne par colonne
class Authorship(db.Model):
    __tablename__ = "authorship"
    authorship_id = db.Column(db.Integer, nullable=True, primary_key=True, autoincrement=True)
    authorship_user_id = db.Column(db.Integer, db.ForeignKey(user.user_id))
    authorship_image_id = db.Column(db.Integer, db.ForeignKey(image.id))
    authorship_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)


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
    tag = db.Column(db.String(64), db.ForeignKey('tag_img.tag_mot'), nullable=False)
    orientation = db.Column(db.String(64), db.ForeignKey('orientation_img.orientation_type'), nullable=False)
    image_valid = db.Column(db.String(2))
    img_user_id = db.Column(db.Integer)
    
    def get_id(self):
        return(self.id)


    @staticmethod
    def add_img(titre, description, sens, date, nom_photographe, source, clef, downloadlink):
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
        
        errors = []
        if not titre:
            errors.append("Veuillez renseigner un titre pour cette image.")
        if not description:
            errors.append("Veuillez renseigner une description pour cette image.")
        if not sens:
            errors.append("Veuillez renseigner une orientation pour cette image.")
        if not date:
            errors.append("Veuillez renseigner une date pour cette image, si elle est inconnue, indiquer: n.d.")
        if not nom_photographe:
            errors.append("Veuillez renseigner un nom du photographe pour cette image, si le nom est inconnu, indiquer: n.n.")
        if not source:
             errors.append("Veuillez renseigner un propriétaire  pour cette image.")
        if not clef:
            errors.append("Veuillez renseigner une mot-clef pour cette image.")
        if not downloadlink:
             errors.append("Aucun lien de téléchargement pour cette image, si aucun lien, indiquer : n.l.")             
    
        if len(errors) > 0:
            return False, errors        

        new_image = Image(
        titre=titre,
        description=description,
        orientation=sens,
        date=date,
        nom_photographe=nom_photographe,
        source=source,
        tag=clef,
        chemin="<img src='" + downloadlink + "' width=100% >",
        img_user_id=current_user.user_id
        )

        # on ajoute une nouvelle entrée dans la table document avec les champs correspondant aux paramètres du modèle

        try:
            # On essaie d'ajouter une image à la BDD
            db.session.add(new_image)
            new_authorship=Authorship(
            authorship_user_id=current_user.user_id,
            auhtorship_image_id=new_image.id
            )
            db.session.add(new_authorship)
            db.session.commit()
            return True, new_image
            
        except Exception as erreur:
            return False, [str(erreur)]

    @staticmethod
    def delete_img(id):
        """
        Fonction qui supprime la notice d'une image, ses données et le fichier image
        :param id: id de l'image (int)
        :return: Booléen
        """
        deleteImg = Image.query.get(id)
        nom_fichier = DOSSIER_UPLOAD + deleteImg.chemin [21:-14]

        if os.path.exists(nom_fichier):
            os.remove(nom_fichier)
        else:
            flash("Fichier inexistant : " + str(nom_fichier))

        try:
            db.session.delete(deleteImg)
            db.session.commit()
            return True

        except Exception as erreur:
            return False, [str(erreur)]
            


    @staticmethod
    def update_img(id, titre, description, sens, date, nom_photographe, source, clef):
        """
        Fonction qui permet de modifier la description de l'image dans la BDD
        :param id: id de l'image (str)
        :param titre: titre donné à l'image (str)
        :param description: courte présentation sur l'image (str)
        :param orientation: "portait", "paysage" (str)
        :param date: date de la photographie (str)
        :param nom_photographe: nom du photographe (str)
        :param source: Nom du propriétaire de l'image (str)
        :param tag: liste des mots-clefs (str)
        :return:
        """
        
        errors = []
        if not titre:
            errors.append("Veuillez renseigner un titre pour cette image.")
        if not description:
            errors.append("Veuillez renseigner une description pour cette image.")
        if not sens:
            errors.append("Veuillez renseigner une orientation pour cette image.")
        if not date:
            errors.append("Veuillez renseigner une date pour cette image, si elle est inconnue, indiquer: n.d.")
        if not nom_photographe:
            errors.append("Veuillez renseigner un nom du photographe pour cette image, si le nom est inconnu, indiquer: n.n.")
        if not source:
             errors.append("Veuillez renseigner un propriétaire  pour cette image.")
        if not clef:
            errors.append("Veuillez renseigner une mot-clef pour cette image.")

        if len(errors) > 0:
            return False, errors

        update_img = Image.query.get(id)    

        if update_img.titre == titre \
           and update_img.description == description \
           and update_img.date == date \
           and update_img.orientation == sens \
           and update_img.nom_photographe == nom_photographe \
           and update_img.source == source \
           and update_img.tag == clef:
           errors.append("Aucune modification n'a été réalisée")

        if len(errors) > 0:
            return False, errors
        
        else:
            update_img.titre=titre
            update_img.description=description
            update_img.date=date
            update_img.orientation=sens
            update_img.nom_photographe=nom_photographe
            update_img.source=source
            update_img.tag=clef

        try:
            db.session.add(update_img)
            db.session.commit()
            return True, update_img

        except Exception as erreur:
            return False, [str(erreur)]
