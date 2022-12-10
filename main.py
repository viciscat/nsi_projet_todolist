"""Mini-projet ToDoList - squelette de départ

Ce mini-projet en terminale NSI consiste à créer une application web dynamique
gérant une liste de tâches à faire
"""

# Librairie(s) utilisée(s)

from flask import *
import bdd


# Création des objets Flask et Bdd
app = Flask(__name__)
app.secret_key = b"1r9)G^A3vTfX4qtwsV#M+Rjjd@JR$+Wa.nt8dz.jhZ_j3M8-(zzkkL^Z5Y3cm2R"
database = bdd.Bdd()

taches = database.getTaches()


# Les routes associées aux fonctions
@app.route("/")
def accueillir():
    flash("Bienvenue sur L'application ToDoList")
    """Gère l'accueil des utilisateurs"""
    print(taches)
    for i in taches:
        print(i.getCategorie())

    # Rendu de la vue
    return render_template("accueil.html")

@app.route("/afficher")
def afficher():
    return render_template('afficher.html', taches=database.getTaches())

@app.route('/nouvelle-tache')
def new_task():
    return render_template('nouvelle_tache.html', taches=database.getTaches())

@app.route('/modifier-tache')
def modifier_tache():
    return render_template('modifier-tache.html', taches=database.getTaches())

@app.route("/priorites")
def affichage_priorites():
    return render_template('priorites.html', priorites=database.getEtats())

@app.route("/categories")
def affichage_categories():
    return render_template('categories.html', categories=database.getCategories())

@app.route("/etats")
def affichage_etats():
    return render_template('etats.html', etats=database.getEtats())


@app.route('/supprimer/<idTache>')
def supprimer(idTache):
    pass


# TODO : ajoutez de nouvelles routes associées à des fonctions "contrôleur" Python


# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)

