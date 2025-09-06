from clovek import Clovek
from utils import Jazyky


class Programator(Clovek):

    def __init__(self, jmeno, vek, jazyk: Jazyky.CSHARP.value):
        self.jazyk = jazyk
        super().__init__(jmeno, vek)

    def pozdrav(self, pozdrav = None):
        if pozdrav == None:
            print("Hello World.")
        else:
            super().pozdrav(pozdrav)

    def chodit(self):
        print("Prošel jsem 5 kilometrů.")
