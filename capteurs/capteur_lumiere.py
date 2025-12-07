from .capteur_base import CapteurBase
import random


class CapteurLumiere(CapteurBase):
    def __init__(self):
        super().__init__(nom="Lumière", type_capteur="passif")

    def lire_mesure(self):
        return random.randint(100, 900)
