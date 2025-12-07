from statistics import mean
from pymongo import MongoClient


class AnalyseManager:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="consommation_energie"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["mesures"]

    def lire_toutes_les_mesures(self):
        return list(self.collection.find())

    def moyenne_par_capteur(self):
        mesures = self.lire_toutes_les_mesures()
        groupes = {}

        for m in mesures:
            cap = m["capteur"]
            val = m["valeur"]
            groupes.setdefault(cap, []).append(val)

        moyennes = {cap: mean(vals) for cap, vals in groupes.items()}
        return moyennes

    def detecter_anomalies(self, seuils):
        """
        seuils = dictionnaire, ex :
        {
            "Température": (0, 35),
            "CO2": (300, 1000)
        }
        """
        anomalies = []
        mesures = self.lire_toutes_les_mesures()

        for m in mesures:
            cap = m["capteur"]
            val = m["valeur"]

            if cap not in seuils:
                continue  # aucun seuil défini

            bas, haut = seuils[cap]

            if not (bas <= val <= haut):
                anomalies.append({
                    "capteur": cap,
                    "valeur": val,
                    "date": m["date"]
                })

        return anomalies
