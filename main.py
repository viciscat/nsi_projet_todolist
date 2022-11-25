"""Mini-projet ToDoList - squelette de départ

Ce mini-projet en terminale NSI consiste à créer une application web dynamique
gérant une liste de tâches à faire
"""

# Librairie(s) utilisée(s)
from flask import *
import bdd

class Tache:
    def __init__(self):
        # TODO: Faire la class! Si pas d'idée de méthodes, juste faire un dico
        pass

# Création des objets Flask et Bdd
app = Flask(__name__)
database = bdd.Bdd()

taches = []



# Les routes associées aux fonctions
@app.route("/")
def accueillir():
    """Gère l'accueil des utilisateurs"""

    # Rendu de la vue
    return render_template("accueil.html")

# TODO : ajoutez de nouvelles routes associées à des fonctions "contrôleur" Python


# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)