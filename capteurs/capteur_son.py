from .capteur_base import CapteurBase
import random


class CapteurSon(CapteurBase):
    def __init__(self):
        super().__init__(nom="Bruit", type_capteur="actif")

    def lire_mesure(self):
        return random.randint(20, 120)
