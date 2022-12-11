BEGIN TRANSACTION;
DROP TABLE IF EXISTS Taches;
CREATE TABLE IF NOT EXISTS Taches (
	idTache	INTEGER PRIMARY KEY ,
	nom	TEXT NOT NULL CHECK(length(nom)<=50),
	description TEXT NOT NULL,
	idCategorie	INTEGER,
	idEtat	INTEGER,
	idPriorite	INTEGER,
	dateLimite	TEXT NOT NULL,
	dateFin	TEXT,
	status INTEGER,
	FOREIGN KEY(idCategorie) REFERENCES Categorie(idCategorie),
	FOREIGN KEY(idEtat) REFERENCES Etat(idEtat),
	FOREIGN KEY(idPriorite) REFERENCES Priorite(idPriorite)
);
DROP TABLE IF EXISTS Priorite;
CREATE TABLE IF NOT EXISTS Priorite (
	idPriorite	INTEGER PRIMARY KEY ,
	nom	TEXT NOT NULL
);
DROP TABLE IF EXISTS Categorie;
CREATE TABLE IF NOT EXISTS Categorie (
	idCategorie	INTEGER PRIMARY KEY ,
	nom	TEXT NOT NULL
);
DROP TABLE IF EXISTS Etat;
CREATE TABLE IF NOT EXISTS Etat (
	idEtat	INTEGER PRIMARY KEY ,
	nom	TEXT NOT NULL
);
INSERT INTO Priorite VALUES (1,'basse');
INSERT INTO Priorite VALUES (2,'moyenne');
INSERT INTO Priorite VALUES (3,'haute');
INSERT INTO Categorie VALUES (1,'Travail');
INSERT INTO Categorie VALUES (2,'Maison');
INSERT INTO Etat VALUES (1,'En cours');
INSERT INTO Etat VALUES (2,'Terminée');
INSERT INTO Etat VALUES (3,'Archivée');

INSERT INTO Taches VALUES (1,'Finir le projet todolist','123',1,1,3,'2023/10/05','',0);
INSERT INTO Taches VALUES (2,'bruh','456',2,1,2,'2025/12/28','',0);
INSERT INTO Taches VALUES (3,'suuuus','789',2,1,1,'2500/10/20',NULL,0);

COMMIT;