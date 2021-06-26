from flask import render_template, request, flash, redirect

#La fonction request permet d'afficher les requêtes

#On importe la variable app qui instancie l'application
from djangophoto.app import app, login
#On déclare les tables de la BDD
from djangophoto.modeles.donnees import Orientation_img
from djangophoto.modeles.donnees import Tag_img
from djangophoto.modeles.donnees import Image
from djangophoto.modeles.donnees import Authorship
from djangophoto.modeles.utilisateurs import User
from flask_login import login_user, current_user, logout_user
from djangophoto.utils import lenTitle, lenDesc, extension_ok
from werkzeug import secure_filename
from djangophoto.constantes import DOSSIER_UPLOAD

#On importe flask :
#- render_template permet de relier les templates aux URLS
#- url_for permet de construire les URLS vers les fonctions et les pages HTML
from flask import render_template, url_for
from flask import Flask
#On importe SQLAlchemy ainsi que l'opérateur or_ 
#qui sert dans la fonction de requête pour la recherche plein texte 
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, text, func
# on importe or_, text et func de la librairie sqlalchemy
from .. app import db
from datetime import date

#On souhaite avoir 5 résultats par page lors de la recherche
RESULTATS_PAR_PAGES = 5

#On définit les différentes routes 
#page d'accueil
@app.route("/")
def accueil():
        return render_template("pages/accueil.html")

#page Galerie
@app.route("/galerie")
def galerie():
 #   cheminImages = Image.query.filter(Image.image_valid=="y").all
 #   développement futur pour la validation des images par l'administrateur.()
    cheminImages = Image.query.all()
    return render_template("pages/galerie.html", Images=cheminImages)
#Permet de faire apparaitre l'ensemble des images dans la page Galerie

#page de la liste des contributions
@app.route("/liste")
def liste():
    contribute = User.query.group_by(User.user_nom).order_by(User.user_nom).all()
#    for i_liste in contribute:
#        contribute.nombre = db.session.query(func.count(Image.id)).filter(Image.img_user_id == contribute.user_id).as_scalar()
    flash(contribute)
    return render_template("pages/liste.html", contribute=contribute)

#page Galerie
@app.route("/galerie_contribute")
def galerie_contribute():
 #   cheminImages = Image.query.filter(Image.image_valid=="y").all
 #   développement futur pour la validation des images par l'administrateur.()
    cheminImages = Image.query.all()
    return render_template("pages/galerie_contribute.html", Images=cheminImages)
#Permet de faire apparaitre l'ensemble des images dans la page Galerie


#page de la biographie de Django Reinhardt
@app.route("/biographie")
def biographie():
		return render_template("pages/biographie.html") 
		
#page de l'ajout d'image
@app.route("/importer")
def edit_image():
    orientation_img = Orientation_img.query.all()
    tag_img = Tag_img.query.all()
    return render_template("pages/edit_image.html", orientation_img=orientation_img, tag_img=tag_img) 

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    # # # VALEURS RENSEIGNÉES PAR L'UTILISATEUR

    # # # LISTE DE TOUS LES LIENS VERS LES IMAGES DÉJÀ EXISTANTES SUR LE SERVEUR
    img_links = Image.query.with_entities(Image.chemin)
    img_links = [link[0] for link in img_links.all()]

    orientation_img = Orientation_img.query.all()
    tag_img = Tag_img.query.all()
    # # # IMPORT DE FICHIER
    if request.method == 'POST':
        f = request.files['file']
        # dans f, on stocke le fichier uploadé
        if f:  # on vérifie qu'un fichier a bien été envoyé
            if extension_ok(f.filename):  # on vérifie que son extension est valide
                nom = secure_filename(f.filename) # on stocke le nom de fichier dans nom
                downloadlink = url_for('static', filename = "img/" + nom)

                # on stocke le lien de stockage sur le serveur du fichier uploadé
                if downloadlink in img_links:
                    # Si le document est déjà présent sur le serveur
                    return redirect(url_for('oups'))
                else:
                    status, new_image = Image.add_img(
                        titre = request.form.get("titre", None),
                        description = request.form.get("description", None),
                        sens = request.form.get("sens", None),
                        date = request.form.get("date", None),
                        nom_photographe = request.form.get("author", None),
                        source = request.form.get("source", None),
                        clef = request.form.get("clef", None),
                        downloadlink = downloadlink
                        )
                    # on ajoute l'image à la BDD
                    if status is True:
                        f.save(DOSSIER_UPLOAD + nom) # on l'enregistre dans le dossier img                        
                        flash("Votre image a bien été ajoutée à la base de donnée ! Merci de votre contribution, vous pouvez modifier ses données si nécessaire.", "success")
                        droit_modif = True
                        return render_template("pages/imgs.html", img = new_image, id=new_image.id, droit_modif=droit_modif, orientation_img=orientation_img, tag_img=tag_img)
                    else:
                        flash("L'ajout d'une nouvelle oeuvre a échoué pour les raisons suivantes : " + ", ".join(new_image), "error")
                        return render_template("pages/edit_image.html", orientation_img=orientation_img, tag_img=tag_img)
            else:
                flash(u'Ce fichier ne porte pas une extension autorisée !', 'error')
        else:
            flash(u'Vous avez oublié le fichier !', 'error')

    return render_template("pages/edit_image.html", orientation_img=orientation_img, tag_img=tag_img) 



@app.route("/upped")
def upped():
    """
    Route pour la page à afficher après avoir importé un nouvelle image dans la BDD

    
    unique_img = Image.query.get(id)
    droit_modif = True
    if status is True:
        flash("Modification réussie !", "success")
        return render_template("pages/imgs.html", img = unique_img, id=id, droit_modif=droit_modif, orientation_img=orientation_img, tag_img=tag_img)
    """
    return render_template("pages/upped.html")

@app.route("/oups/")
def oups():
    """
    Route pour la page à afficher si le fichier à importer est déjà sur le serveur

    """

    return render_template("pages/oups.html")


#page à propos
@app.route("/a_propos")
def a_propos():
		return render_template("pages/a_propos.html")

#page de la modification des légendes de l'image
@app.route("/update_img/<int:id>", methods=["POST", "GET"])
def update_img(id):
    """ 
    Route permettant de modifier les données d'une image
    :param id: ID de l'image
    :return: redirection ou template Imgs.html
    :rtype: template
    """
    orientation_img = Orientation_img.query.all()
    tag_img = Tag_img.query.all()

    if request.method == "GET":
        updateImg = Image.query.get(id)
        
        return render_template("pages/update-image.html", updateImg=updateImg, orientation_img=orientation_img, tag_img=tag_img)    

    else:
        status, data = Image.update_img(
            id=id,
            titre = request.form.get("titre", None),
            description = request.form.get("description", None),
            sens = request.form.get("sens", None),
            date = request.form.get("date", None),
            nom_photographe = request.form.get("author", None),
            source = request.form.get("source", None),
            clef = request.form.get("clef", None)
            )
        unique_img = Image.query.get(id)
        droit_modif = True

        if status is True:
            flash("Modification réussie !", "success")
            return render_template("pages/imgs.html", img = unique_img, id=id, droit_modif=droit_modif, orientation_img=orientation_img, tag_img=tag_img)
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ", ".join(data), "danger")
            updateImg = Image.query.get(id)
            return render_template("pages/update-image.html", updateImg=updateImg, orientation_img=orientation_img, tag_img=tag_img)


    unique_img = Image.query.get(id)

    return render_template("pages/update-image.html", img = unique_img, id=id, orientation_img=orientation_img, tag_img=tag_img)


#page de la suppression de l'image
@app.route("/delete_img/<int:id>")
def delete_img(id):
    """ 
    Route pour supprimer une image et ses données dans la base
    :param _id : ID de l'image
    :return: redirection ou template galerie.html
    :rtype: template
    """
    deleteImg = Image.query.get(id)
    
    
    status = Image.delete_img(
    id=deleteImg.id
        )

    if status is True:        
        cheminImages = Image.query.all()
        return render_template("pages/galerie.html", Images=cheminImages)

    else:
        flash("La suppresion a échoué...", "error")
        cheminImages = Image.query.all()
        return render_template("pages/galerie.html", Images=cheminImages)

    


# Définition de la route vers chaque image grâce à leur identifiant (int)
@app.route("/imgs/<int:id>")
def img(id):
    unique_img = Image.query.get(id)
    droit_modif = False
    if current_user.is_authenticated is True:

        if ((current_user.user_type == 'admin')
            or (Image.img_user_id == current_user.user_id)
            ):
            droit_modif = True
    return render_template("pages/imgs.html", img = unique_img, id=id, droit_modif=droit_modif)


#On définit la route pour la recherche plein-texte
@app.route("/recherche")
def recherche():
    motclef = request.args.get("keyword", None)
    page = request.args.get("page",1)

    if isinstance(page, str) and page.isdigit():
        page = int(page)
    else:
        page = 1 

#Création d'une liste vide pour les résultats
    resultats = []
    titre = "Recherche"

    if motclef:
    # Si on a un mot-clé, on requête toutes les tables de notre base de données pour vérifier s'il y a des correspondances
    # Le résultat de cette requête est stocké dans la liste resultats = []
        resultats = Image.query.filter(
            or_(
                Image.date.like("%{}%".format(motclef)),
                Image.orientation.like("%{}%".format(motclef)),
                Image.description.like("%{}%".format(motclef)),
                Image.tag.like("%{}%".format(motclef)),
                Image.titre.like("%{}%".format(motclef)),
                Image.nom_photographe.like("%{}%".format(motclef)),
                Image.source.like("%{}%".format(motclef)),
            )
        ).paginate(page=page, per_page=RESULTATS_PAR_PAGES)
        titre = "Résultats pour votre recherche '"+ motclef + "'"
        # On affiche une phrase de titre qui indiquera les résultats de la recherche en fonction du mot-clé rentré par l'utilisateur
        # Cette variable titre sera réutilisée dans la page recherche.html
    return render_template("pages/recherche.html", resultats=resultats, titre=titre, keyword=motclef)
    # On retourne la page recherhce.html, et on indique à quoi correspondent les variables resultats, titre et keyword,
    # qui seront appelées ensuite au sein des pages html

@app.route("/inscription", methods=["GET", "POST"])
def inscription():
	   
    #Route gérant les inscriptions
    #
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST":
        statut, donnees = User.creer(
            login=request.form.get("login", None),
            email=request.form.get("email", None),
            nom=request.form.get("nom", None),
            prenom=request.form.get("prenom", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if statut is True:
            flash("Enregistrement effectué. Identifiez-vous maintenant", "success")
            return redirect("/")
        else:
            flash("Les erreurs suivantes ont été rencontrées : " + ",".join(donnees), "error")
            return render_template("pages/inscription.html")
    else:
        return render_template("pages/inscription.html")
   

@app.route("/connexion", methods=["POST", "GET"])
def connexion():
    """ Route gérant les connexions
    """
    if current_user.is_authenticated is True:
        flash("Vous êtes déjà connecté-e", "info")
        return redirect("/")
    # Si on est en POST, cela veut dire que le formulaire a été envoyé
    if request.method == "POST":
        utilisateur = User.identification(
            login=request.form.get("login", None),
            motdepasse=request.form.get("motdepasse", None)
        )
        if utilisateur:
            flash("Connexion effectuée", "success")
            login_user(utilisateur)
            return redirect("/")
        else:
            flash("Les identifiants n'ont pas été reconnus", "error")

    return render_template("pages/connexion.html")
login.login_view = 'connexion'


@app.route("/deconnexion", methods=["POST", "GET"])
def deconnexion():
    if current_user.is_authenticated is True:
        logout_user()
    flash("Vous êtes déconnecté-e", "info")
    return redirect("/")

#page de l'erreur 404 lorsque la page demandée est introuvable
#template "error/404"
@app.errorhandler(404)
def page_not_found(error):
    return render_template("error/404.html"), 404
