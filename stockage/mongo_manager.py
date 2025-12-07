# Apporter la gestion de la base de données MongoDB pour stocker les mesures de consommation d'énergie
from pymongo import MongoClient
# Importer datetime pour gérer les horodatages
from datetime import datetime


# Définir la classe MongoManager pour gérer les opérations de la base de données MongoDB
class MongoManager:
    # Initialisation de la connexion à la base de données MongoDB
    def __init__(self, uri="mongodb://localhost:27017/", db_name="consommation_energie"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["mesures"]

    # Méthode pour sauvegarder les mesures dans la base de données
    def sauvegarder_mesure(self, capteur, valeur):
        document = {
            "capteur": capteur,
            "valeur": valeur,
            "date": datetime.now()
        }
        self.collection.insert_one(document)
        print(f"Mesure sauvegardée : {document}")
