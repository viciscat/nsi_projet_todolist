class Tache:
    def __init__(self, idTache, nom, description, idCategorie, idEtat, idPriorite, dateLimite, dateFin, database):
        self.idTache = idTache
        self.nom = nom
        self.description = description
        self.idCategorie = idCategorie
        self.idEtat = idEtat
        self.idPriorite = idPriorite
        self.dateLimite = dateLimite
        self.dateFin = dateFin
        self.database = database

    def getCategorie(self):
        return self.database.getCategories()[self.idCategorie-1]

    def getPriorite(self):
        return self.database.getPriorites()[self.idPriorite-1]

    def getEtat(self):
        return self.database.getEtats()[self.idEtat-1]
