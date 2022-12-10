"""Mini-projet ToDoList - squelette de départ

Ce mini-projet en terminale NSI consiste à créer une application web dynamique
gérant une liste de tâches à faire
"""

# Librairie(s) utilisée(s)
import sqlite3
import Tache


# La classe
class Bdd:
    """Classe pour faire le lien entre la base de données SQLite et le programme"""

    # TODO : ajoutez le code nécessaire à la classe Bdd
    def __init__(self):
        """
        Base de donnée vla gaming pour le projet todolist
        """
        self.cnx = sqlite3.connect("bdd/todo.sqlite", check_same_thread=False)
        self.cnx.row_factory = sqlite3.Row
        self.cursor = self.cnx.cursor()

    def getTaches(self, filtre=True):
        data = (self.cursor.execute("""
        SELECT *
        FROM Taches
        WHERE idEtat != 3
        """).fetchall()
                if filtre else
                self.cursor.execute("""
        SELECT *
        FROM Taches
        """).fetchall())
        return [Tache.Tache(*i, self) for i in data]

    def getCategories(self):
        return self.cursor.execute("""
                SELECT nom
                FROM Categorie
                """).fetchall()

    def getEtats(self):
        return self.cursor.execute("""
        SELECT nom
        FROM Etat
        """).fetchall()

    def getPriorites(self):
        return self.cursor.execute("""
        SELECT nom
        FROM Priorite
        """).fetchall()

    def newTache(self, nom, description, idCategorie, idEtat, idPriorite, dateLimite):
        try:
            self.cursor.execute("""
            INSERT INTO Taches (nom, description, idCategorie, idEtat, idPriorite, dateLimite)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (nom, description, idCategorie, idEtat, idPriorite, dateLimite))
            self.cnx.commit()

        except sqlite3.Error as erreur:
            print("Erreur =>", erreur)

    def updateTache(self, idTache, data: dict):
        """
        Met a jour la tache avec l'id idTache, avec les données data.

        data est un dictionnaire avec la clé représantant le nom de l'attribut et la valeur,
        la valeur de l'attribut
        """
        try:
            set_params = ",".join([f"{k}=:{k}" for k in data.keys()])
            command = f"UPDATE Taches SET {set_params} WHERE idTache = :idt"
            data["idt"] = idTache
            self.cnx.execute(command, data)
            self.cnx.commit()

        except sqlite3.Error as erreur:
            print("Erreur =>", erreur)

    def deleteTache(self, idTache):
        try:
            self.cnx.execute("""
            DELETE FROM Taches
            WHERE idTache = ?
            """, (idTache,))
        except sqlite3.Error as erreur:
            print("Erreur =>", erreur)


# Mise au point de la classe Bdd seule
if __name__ == "__main__":
    # TODO : ajoutez le code pour tester et mettre au point votre classe Bdd
    test = Bdd()
    print(test.getTaches())
    print(test.getTaches(filtre=False))
    # test.newTache("suuuus", "bruh", 2, 1, 1, "2500/10/20")
    # test.updateTache(3, {"dateLimite": "2050/09/15"})
