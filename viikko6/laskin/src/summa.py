class Summa:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovelluslogiikka = sovelluslogiikka
        self._lue_syote = lue_syote
        self._edellinen_arvo = 0

    def suorita(self):
        self._edellinen_arvo = self._sovelluslogiikka.arvo()
        try:
            luku = int(self._lue_syote())
            self._sovelluslogiikka.plus(luku)
        except:
            pass

    def kumoa(self):
        self._sovelluslogiikka.aseta_arvo(self._edellinen_arvo)