from .capteur_base import CapteurBase
import random


class CapteurHumidite(CapteurBase):
    def __init__(self):
        super().__init__(nom="Humidité", type_capteur="passif")

    def lire_mesure(self):
        return round(random.uniform(30, 70), 2)
