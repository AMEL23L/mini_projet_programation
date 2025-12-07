from .capteur_base import CapteurBase
import random


class CapteurEau(CapteurBase):
    def __init__(self):
        super().__init__(nom="Débit d'eau", type_capteur="passif")

    def lire_mesure(self):
        return round(random.uniform(0.5, 10.0), 2)
