class CapteurBase:
    def __init__(self, nom, type_capteur):
        self.nom = nom
        self.type = type_capteur  # actif ou passif

    def lire_mesure(self):
        raise NotImplementedError(
            "La méthode lire_mesure() doit être redéfinie dans chaque capteur spécifique."
        )
