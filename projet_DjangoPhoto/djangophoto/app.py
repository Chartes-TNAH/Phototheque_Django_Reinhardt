#import des packages
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os
from .constantes import SECRET_KEY

#Stockage des chemins courants
chemin_actuel = os.path.dirname(os.path.abspath(__file__))
#Stockage des chemins vers les "templates"
templates = os.path.join(chemin_actuel, "templates")
#Stockage des chemins vers les "static"
statics = os.path.join(chemin_actuel, "static")

#On paramètre l'application web
app = Flask( 
    "Application",
    template_folder=templates,
    static_folder=statics
)

# On configure le secret
app.config['SECRET_KEY'] = SECRET_KEY
#On configure la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./db_DjangoPhoto.sqlite'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#On initie l'extension
db = SQLAlchemy(app)

# On met en place la gestion d'utilisateur-rice-s
login = LoginManager(app)

import djangophoto.routes
