from .capteur_base import CapteurBase
import random


class CapteurMouvement(CapteurBase):
    def __init__(self):
        super().__init__(nom="Mouvement", type_capteur="actif")

    def lire_mesure(self):
        return random.choice([0, 1])
