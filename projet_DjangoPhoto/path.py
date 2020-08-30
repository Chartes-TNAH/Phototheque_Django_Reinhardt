import os

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
print(chemin_actuel)

templates = os.path.join(chemin_actuel, "app", "templates")
print(templates)

chemin_db = os.path.join(chemin_actuel, "db_DjangoPhoto.sqlite")
