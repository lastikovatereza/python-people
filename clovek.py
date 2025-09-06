from abc import ABC, abstractmethod


class Clovek(ABC):

    def __init__(self, jmeno, vek):
        self.jmeno = jmeno
        self._vek = vek

    @property
    def get_jmeno(self):
        return f"Mr./Mrs. {self.jmeno}"     # getter


    def get_vek(self):
        return self._vek                # kalsicky getter


    def set_vek(self, novy_vek):
        if novy_vek > 0 and novy_vek < 100:
            self._vek = novy_vek                # klasicky setter
        else:
            print("Nový věk neleží v povoleném rozmezí.")

        # propojení getteru a setteru pomocí property "vek"
    @property
    def vek(self):
        return self.get_vek()

    @vek.setter
    def vek(self, novy_vek):
        self.set_vek(novy_vek)

    @abstractmethod
    def chodit(self):
        print("Prošel jsem 4 kilometry.")

    @abstractmethod
    def pozdrav(self, pozdrav = "Ahoj"):
        print(f"Ahoj, jsem {self.jmeno} a je mi {self._vek}.")

    def __str__(self):
        return f"Jmenuji se {self.jmeno} a je mi {self._vek}."