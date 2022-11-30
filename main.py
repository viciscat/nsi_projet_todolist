"""Mini-projet ToDoList - squelette de départ

Ce mini-projet en terminale NSI consiste à créer une application web dynamique
gérant une liste de tâches à faire
"""

# Librairie(s) utilisée(s)
from flask import *
import bdd


class Tache:
    def __init__(self, idTache, nom, description, idCategorie, idEtat, idPriorite, dateLimite, dateFin):
        # TODO: Faire la class! Si pas d'idée de méthodes, juste faire un dico
        self.idTache = idTache
        self.nom = nom
        self.description = description
        self.idCategorie = idCategorie
        self.idEtat = idEtat
        self.idPriorite = idPriorite
        self.dateLimite = dateLimite
        self.dateFin = dateFin


# Création des objets Flask et Bdd
app = Flask(__name__)
database = bdd.Bdd()

taches = [Tache(*i) for i in database.getTaches()]


# Les routes associées aux fonctions
@app.route("/")
def accueillir():
    """Gère l'accueil des utilisateurs"""
    print(taches)

    # Rendu de la vue
    return render_template("accueil.html")


# TODO : ajoutez de nouvelles routes associées à des fonctions "contrôleur" Python


# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)

