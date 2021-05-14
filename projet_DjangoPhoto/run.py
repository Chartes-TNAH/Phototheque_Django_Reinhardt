from djangophoto.app import app
# du fichier app.py dans le dossier djangophoto j'importe la fonction config_app


if __name__ == '__main__':
    app.run(debug=True)
    # app.run() lance l'application
# le mode debug permet de lancer un débogueur pendant le développement de l'application
