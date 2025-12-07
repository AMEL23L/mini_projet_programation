import pytest  # noqa: F401
from analyse.analyseur import AnalyseManager


class FakeMongo:
    """Simule la collection MongoDB pour les tests."""

    def __init__(self, data):
        self.data = data

    def find(self):
        return self.data


def test_moyenne_par_capteur():
    fake_data = [
        {"capteur": "Température", "valeur": 20},
        {"capteur": "Température", "valeur": 30},
        {"capteur": "CO2", "valeur": 500},
        {"capteur": "CO2", "valeur": 700},
    ]

    analyse = AnalyseManager()
    analyse.collection = FakeMongo(fake_data)

    result = analyse.moyenne_par_capteur()

    assert result["Température"] == 25
    assert result["CO2"] == 600


def test_detecter_anomalies():
    fake_data = [
        {"capteur": "Température", "valeur": 50, "date": "2025-01-01"},
        {"capteur": "CO2", "valeur": 500, "date": "2025-01-01"},
    ]

    seuils = {
        "Température": (0, 35),
        "CO2": (300, 1000),
    }

    analyse = AnalyseManager()
    analyse.collection = FakeMongo(fake_data)

    anomalies = analyse.detecter_anomalies(seuils)

    assert len(anomalies) == 1
    assert anomalies[0]["capteur"] == "Température"
    assert anomalies[0]["valeur"] == 50
