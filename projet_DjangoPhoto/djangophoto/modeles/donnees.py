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
