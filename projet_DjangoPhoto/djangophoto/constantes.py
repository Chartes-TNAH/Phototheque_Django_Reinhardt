from warnings import warn

# Déclaration de toutes les constantes à utiliser dans le projet
# Convention : les constantes portent des noms en majuscule

RESULTATS_PAR_PAGE = 6
# variable qui définit le nombre de résultats par page (utilisée pour l'index et la recherche simple)
DOSSIER_UPLOAD = "./djangophoto/static/img/"

SECRET_KEY = "JE SUIS UN SECRET !"
# variable utilisée comme clé cryptographique, qui permet de générer des signatures ou tokens

if SECRET_KEY == "JE SUIS UN SECRET !":
    warn("Le secret par défaut n'a pas été changé, vous devriez le faire", Warning)


