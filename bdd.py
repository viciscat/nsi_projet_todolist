"""Mini-projet ToDoList - squelette de départ

Ce mini-projet en terminale NSI consiste à créer une application web dynamique
gérant une liste de tâches à faire
"""

# Librairie(s) utilisée(s)
import sqlite3


# La classe
class Bdd:
    """Classe pour faire le lien entre la base de données SQLite et le programme"""
    # TODO : ajoutez le code nécessaire à la classe Bdd
    def __init__(self):
        """
        Base de donnée vla gaming pour le projet todolist
        """
        self.cnx = sqlite3.connect("bdd/todo.sqlite")
        self.cursor = self.cnx.cursor()

    def getTaches(self):
        return self.cursor.execute("""
        SELECT *
        FROM Taches
        """).fetchall()

    def newTache(self, nom, idCategorie, idEtat, idPriorite, dateLimite):
        try:
            self.cursor.execute("""
            INSERT INTO Taches (nom, idCategorie, idEtat, idPriorite, dateLimite)
            VALUES (?, ?, ?, ?, ?)
            """, (nom, idCategorie, idEtat, idPriorite, dateLimite))
            self.cnx.commit()

        except sqlite3.Error as erreur:
            print("Erreur =>", erreur)

    def updateTache(self, idTache, kwargs):
        pass



# Mise au point de la classe Bdd seule
if __name__ == "__main__":
    # TODO : ajoutez le code pour tester et mettre au point votre classe Bdd
    test = Bdd()
    print(test.getTaches())
    # test.newTache("suuuus", 2, 1, 1, "2500/10/20")
