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
    """Gère l'accueil des utilisateurs"""
    print(taches)
    for i in taches:
        print(i.getCategorie())

    # Rendu de la vue
    return render_template("accueil.html")


@app.route("/afficher")
def afficher():
    return render_template('afficher.html', taches=database.getTaches(), categories=database.getCategories())


@app.route('/nouvelle-tache')
def new_task_page():
    return render_template('nouvelle-tache.html', categories=database.getCategories(),
                           priorites=database.getPriorites())


@app.route('/nouvelle-tache-req', methods=["POST"])
def new_task():
    rep = request.form
    ret = database.newTache(rep["nom"], rep["description"], int(rep["categorie"]),
                            1, int(rep["priorite"]), rep["dateLimite"])
    if ret is None:
        flash("La tache a été créer avec succès !")
    else:
        flash("Uh Oh! Une erreur s'est produite lors de la création de la tache!")
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
    ret = database.updateTache(int(idTache), rep)
    if ret is None:
        flash("Tache modifiée avec succès !")
        return redirect('/afficher')
    else:
        flash("Uh Oh ! Une erreur s'est produite dans la modification de la tache !")
        return redirect(url_for('modifier_tache'))


@app.route("/priorites")
def affichage_priorites():
    return render_template('priorites.html', priorites=database.getEtats())


@app.route("/categories")
def affichage_categories():
    categories = database.getCategories()
    return render_template('categories.html', categories=categories,
                           nbtaches=[database.getNombreTacheCategorie(i + 1) for i in range(len(categories))])


@app.route("/modifier-categorie/<idCategorie>", methods=["POST"])
def modifier_categorie(idCategorie):
    rep = request.form
    print(rep)
    database.updateCategorie(int(idCategorie), rep["nom"])
    flash("Nom de la categorie changer avec succès !")
    return redirect("/categories")


@app.route("/nouvelle-categorie", methods=["POST"])
def nouvelle_categorie():
    rep = request.form
    ret = database.newCategorie(rep["nom"])
    if ret is None:
        flash("Catégorie ajoutée avec succès !")
        return redirect(url_for('affichage_categories'))
    else:
        flash("Uh Oh ! Une erreur s'est produite lors de la création de la catégorie")
        return redirect(url_for('affichage_categories'))


@app.route("/etats")
def affichage_etats():
    return render_template('etats.html', etats=database.getEtats())


@app.route('/supprimer/<idTache>')
def supprimer(idTache):
    database.deleteTache(int(idTache))
    flash("La tache a été supprimer avec succès !")
    return redirect("/afficher")


@app.route('/supprimer-categorie/<idCategorie>')
def supprimerCategorie(idCategorie):
    ret = database.deleteCategorie(int(idCategorie))
    if ret is None:
        flash("Catégorie supprimée avec succès !")
        return redirect(url_for('affichage_categories'))
    else:
        flash("Uh Oh ! Une erreur s'est produite lors de la suppression de la catégorie")
        return redirect(url_for('affichage_categories'))


@app.route('/termine-tache/<idTache>')
def termineTache(idTache):
    database.modifyTacheStatus(int(idTache), 2)
    flash("La tache a été terminé avec succès !")
    return redirect("/afficher")


@app.route('/archive-tache/<idTache>')
def archiveTache(idTache):
    database.modifyTacheStatus(int(idTache), 3)
    flash("La tache a été archivé avec succès !")
    return redirect("/afficher")


@app.route('/statistiques')
def stats():
    return render_template('statistiques.html')


@app.route('/get-stats', methods=['GET'])
def get_statistiques():
    etats = database.getEtats()
    categories = database.getCategories()
    message = {"categories": categories, "nbCategorie": [database.getNombreTacheCategorie(i + 1) for i in range(len(
        categories))], "etats": etats, "nbEtat": [database.getNombreTacheEtat(i + 1) for i in range(len(
        etats))]}
    return jsonify(message)


# TODO : ajoutez de nouvelles routes associées à des fonctions "contrôleur" Python


# Lancement du serveur
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)
