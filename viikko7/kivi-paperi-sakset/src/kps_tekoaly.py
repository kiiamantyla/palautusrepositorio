"""Pelaaja vs. Tekoäly -peli."""
from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):
    """Pelaaja pelaa yksinkertaista tekoälyä vastaan."""
    def __init__(self):
        """Alustaa pelin tekoälyllä."""
        self._tekoaly = Tekoaly()

    def _toisen_siirto(self, _):
        """Hakee tekoälyn siirron.

        Args:
            _: Ensimmäisen pelaajan siirto (ei käytetä).

        Returns:
            Tekoälyn siirto.
        """
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
