##mainmodul
import random

# lista amiből a random_elem választ, bővíthetö
elemek = ["alma", "banán", "tej", "kenyér", "sajt", "vaj", "paradicsom", "hagyma", "kalács"]

# Bevásárlólista kezelése
class BevasarloLista:
    def __init__(self):
        self.lista = []

    def hozzaad(self, elem):
        if elem and elem not in self.lista:
            self.lista.append(elem)
            return True
        return False

    def torol(self, elem):
        if elem in self.lista:
            self.lista.remove(elem)
            return True
        return False

    def listaz(self):
        return self.lista

    def random_elem(self):
        return random.choice(elemek)

