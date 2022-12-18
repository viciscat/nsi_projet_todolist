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
        Base de donnée pour le projet todolist
        """
        self.cnx = sqlite3.connect("bdd/todo.sqlite", check_same_thread=False)
        self.cnx.row_factory = sqlite3.Row
        self.cursor = self.cnx.cursor()

    def getTaches(self, filtre=True):
        """
        Récuperer toutes les taches, si filtre est True, n'inclut pas les taches archivées.
        """
        data = (self.cursor.execute("""
        SELECT *
        FROM Taches
        WHERE idEtat != 3
        ORDER BY dateLimite ASC
        """).fetchall()
                if filtre else
                self.cursor.execute("""
        SELECT *
        FROM Taches
        """).fetchall())
        return [Tache.Tache(*i, database=self) for i in data]

    def getTache(self, id):
        """
        Récupère une tache spécifique avec son ID
        """
        return self.cursor.execute("""
                SELECT *
                FROM Taches
                WHERE idTache = ?
                """, (id,)).fetchall()

    # Ça donne une liste de tuple avec un élément (("truc",), ("machin",), ...) donc on doit faire une petite manip
    def getCategories(self):
        """
        Récupère toutes les catégories
        """
        return [i[0] for i in self.cursor.execute("""SELECT nom FROM Categorie""").fetchall()]

    def getEtats(self):
        """
        Récupère tous les états
        """
        return [i[0] for i in self.cursor.execute("""SELECT nom FROM Etat""").fetchall()]

    def getNombreTacheEtat(self, idEtat):
        """
        Renvoie le nombre de taches qui ont cet état
        """
        try:
            return self.cursor.execute("""
            SELECT COUNT(idTache)
            FROM Taches
            WHERE idEtat = ?
            """, (idEtat,)).fetchall()[0][0]
        except sqlite3.Error as erreur:
            return erreur

    def getPriorites(self):
        """
        Renvoie toutes les priorités
        """
        return [i[0] for i in self.cursor.execute("""SELECT nom FROM Priorite""").fetchall()]

    def updateCategorie(self, idCategorie, nom):
        """
        Permet de changer le nom de la catégorie d'id idCategorie
        """
        try:
            self.cursor.execute("""
            UPDATE Categorie
            SET nom = ?
            WHERE idCategorie = ?
            """, (nom, idCategorie))

            self.cnx.commit()
        except sqlite3.Error as erreur:
            print("Erreur =>", erreur)

    def getNombreTacheCategorie(self, idCategorie):
        """
        Renvoie le nombre de taches qui ont cette catégorie
        """
        try:
            return self.cursor.execute("""
            SELECT COUNT(idTache)
            FROM Taches
            WHERE idCategorie = ?
            """, (idCategorie,)).fetchall()[0][0]
        except sqlite3.Error as erreur:
            return erreur

    def deleteCategorie(self, idCategorie):
        """
        Supprime la catégorie d'ID idCategorie
        """
        try:
            self.cursor.execute("""
            DELETE FROM Categorie
            WHERE idCategorie = ?
            """, (idCategorie,))

            self.cnx.commit()
        except sqlite3.Error as erreur:
            return erreur

    def newCategorie(self, nom):
        """
        Crée une nouvelle catégorie avec un nom
        """
        try:
            self.cursor.execute("""
            INSERT INTO Categorie (nom)
            VALUES (?)
            """, (nom,))
            self.cnx.commit()
        except sqlite3.Error as erreur:
            return erreur

    def newTache(self, nom, description, idCategorie, idEtat, idPriorite, dateLimite):
        """
        Crée une nouvelle tache avec ces paramètres
        """
        try:
            self.cursor.execute("""
            INSERT INTO Taches (nom, description, idCategorie, idEtat, idPriorite, dateLimite)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (nom, description, idCategorie, idEtat, idPriorite, dateLimite))
            self.cnx.commit()

        except sqlite3.Error as erreur:
            return erreur

    def updateTache(self, idTache, data: dict):
        """
        Met à jour la tache avec l'id idTache, avec les données data.

        Data est un dictionnaire avec la clé représantant le nom de l'attribut et la valeur,
        la valeur de l'attribut
        """
        try:
            set_params = ",".join([f"{k}=:{k}" for k in data.keys()])
            command = f"UPDATE Taches SET {set_params} WHERE idTache = :idt"
            data["idt"] = idTache
            self.cnx.execute(command, data)
            self.cnx.commit()

        except sqlite3.Error as erreur:
            return erreur

    def deleteTache(self, idTache):
        """
        Suprrime la tache d'ID idTache
        """
        try:
            self.cnx.execute("""
            DELETE FROM Taches
            WHERE idTache = ?
            """, (idTache,))
            self.cnx.commit()
        except sqlite3.Error as erreur:
            return erreur

    def modifyTacheStatus(self, idTache, status):
        """
        Modifie l'état de la tache d'ID idTache par l'état status
        """
        try:
            self.cnx.execute("""
            UPDATE Taches
            SET idEtat = ?
            WHERE idTache = ?
            """, (status, idTache,))
            self.cnx.commit()
        except sqlite3.Error as erreur:
            print("Erreur =>", erreur)


# Mise au point de la classe Bdd seule
if __name__ == "__main__":
    # TODO : ajoutez le code pour tester et mettre au point votre classe Bdd
    test = Bdd()
    print(test.getTaches())
    print(test.getTaches(filtre=False))
    print(test.getNombreTacheCategorie("hre"))
    # test.newTache("suuuus", "bruh", 2, 1, 1, "2500/10/20")
    # test.updateTache(3, {"dateLimite": "2050/09/15"})
