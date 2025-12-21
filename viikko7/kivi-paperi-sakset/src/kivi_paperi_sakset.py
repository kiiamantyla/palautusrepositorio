"""Kivi-paperi-sakset pelin perusluokka."""
from tuomari import Tuomari

class KiviPaperiSakset:
    """Abstrakti perusluokka kivi-paperi-sakset pelille."""
    def pelaa(self):
        """Pelaa peliä kunnes jompikumpi antaa virheellisen siirron."""
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        """Kysyy ensimmäisen pelaajan siirron.

        Returns:
            Ensimmäisen pelaajan syöttämä siirto.
        """
        return input("Ensimmäisen pelaajan siirto: ")

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        """Määrittää toisen pelaajan/tekoälyn siirron.

        Args:
            ensimmaisen_siirto: Ensimmäisen pelaajan siirto.

        Returns:
            Toisen pelaajan/tekoälyn siirto.
        """
        raise NotImplementedError

    def _onko_ok_siirto(self, siirto):
        """Tarkistaa onko siirto kelvollinen (k, p tai s).

        Args:
            siirto: Siirto tarkistettavaksi.

        Returns:
            True jos siirto on kelvollinen, muuten False.
        """
        return siirto in ["k", "p", "s"]
