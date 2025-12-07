from .capteur_base import CapteurBase
import random


class CapteurTemperature(CapteurBase):
    def __init__(self):
        super().__init__(nom="Température", type_capteur="passif")

    def lire_mesure(self):
        return round(random.uniform(18, 30), 2)
