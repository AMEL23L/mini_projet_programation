from capteurs import (
    CapteurTemperature,
    CapteurLumiere,
    CapteurHumidite,
    CapteurSon,
    CapteurMouvement,
    CapteurCO2,
    CapteurEau,
)
from stockage.mongo_manager import MongoManager
from analyse.analyseur import AnalyseManager


def main():
    capteurs = [
        CapteurTemperature(),
        CapteurLumiere(),
        CapteurHumidite(),
        CapteurSon(),
        CapteurMouvement(),
        CapteurCO2(),
        CapteurEau(),
    ]
    mongo = MongoManager()

    for capteur in capteurs:
        valeur = capteur.lire_mesure()
        print(f"{capteur.nom} ({capteur.type}) → {valeur}")
        mongo.sauvegarder_mesure(capteur.nom, valeur)


if __name__ == "__main__":
    main()

analyse = AnalyseManager()

print("\n--- Moyennes ---")
moyennes = analyse.moyenne_par_capteur()

for cap, moy in moyennes.items():
    print(f"{cap} → {moy}")

print("\n--- Anomalies détectées ---")
seuils = {
    "Température": (0, 35),
    "CO2": (300, 1000),
    "Humidité": (20, 70),
    "Lumière": (0, 1000),
    "Bruit": (0, 85),
    "Débit d'eau": (0, 10),
}

anomalies = analyse.detecter_anomalies(seuils)

for a in anomalies:
    print(f"⚠ Anomalie : {a['capteur']} = {a['valeur']} ({a['date']})")
