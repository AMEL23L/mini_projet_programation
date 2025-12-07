from .capteur_base import CapteurBase
import random


class CapteurCO2(CapteurBase):
    def __init__(self):
        super().__init__(nom="CO2", type_capteur="passif")

    def lire_mesure(self):
        return random.randint(300, 2000)
