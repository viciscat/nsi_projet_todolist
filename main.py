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
    flash("wowi")
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
def new_task_page():
    return render_template('nouvelle-tache.html', categories=database.getCategories(),
                           priorites=database.getPriorites())


@app.route('/nouvelle-tache-req', methods=["POST"])
def new_task():
    rep = request.form
    database.newTache(rep["nom"], rep["description"], int(rep["categorie"]),
                      1, int(rep["priorite"]), rep["dateLimite"])
    flash("La tache a été créer avec succès !")
    return redirect("/afficher")


@app.route('/modifier-tache/<idTache>')
def modifier_tache_page(idTache):
    return render_template('modifier-tache.html',
                           tache=database.getTache(int(idTache))[0],
                           categories=database.getCategories(),
                           priorites=database.getPriorites())


@app.route('/modifier-tache-req/<idTache>', methods=["POST"])
def modifier_tache(idTache):
    rep = request.form.to_dict()
    rep["description"] = rep["description"].replace("\r\n", "\\r\\n")
    database.updateTache(int(idTache), rep)
    return redirect('/afficher')


@app.route("/priorites")
def affichage_priorites():
    return render_template('priorites.html', priorites=database.getEtats())


@app.route("/categories")
def affichage_categories():
    return render_template('categories.html', categories=database.getCategories())


@app.route("/modifier-categorie/<idCategorie>", methods=["POST"])
def modifier_categorie(idCategorie):
    rep = request.form
    database.updatePriorite(int(idCategorie), rep["nom"])
    flash("Nom de la categorie changer avec succès !")
    return redirect("/categories")


@app.route("/etats")
def affichage_etats():
    return render_template('etats.html', etats=database.getEtats())


@app.route('/supprimer/<idTache>')
def supprimer(idTache):
    database.deleteTache(int(idTache))
    flash("La tache a été supprimer avec succès !")
    return redirect("/afficher")


@app.route('/termine-tache/<idTache>')
def termineTache(idTache):
    database.modifyTacheStatus(int(idTache), 1)
    flash("La tache a été terminé avec succès !")
    return redirect("/afficher")


@app.route('/archive-tache/<idTache>')
def archiveTache(idTache):
    database.modifyTacheStatus(int(idTache), 2)
    flash("La tache a été archivé avec succès !")
    return redirect("/afficher")


# TODO : ajoutez de nouvelles routes associées à des fonctions "contrôleur" Python


# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)
