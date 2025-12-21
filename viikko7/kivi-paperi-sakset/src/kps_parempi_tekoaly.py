"""Pelaaja vs. Parannettu Tekoäly -peli."""
from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly(KiviPaperiSakset):
    """Pelaaja pelaa parannettua tekoälyä vastaan joka oppii pelaajan siirroista."""
    def __init__(self):
        """Alustaa pelin parannetulla tekoälyllä."""
        self._tekoaly = TekoalyParannettu(10)

    def _toisen_siirto(self, ensimmaisen_siirto):
        """Antaa parannetun tekoälyn siirron.

        Args:
            ensimmaisen_siirto: Ensimmäisen pelaajan siirto jota käytetään oppimiseen.

        Returns:
            Tekoälyn siirto.
        """
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto
