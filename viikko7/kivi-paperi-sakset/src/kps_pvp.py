"""Pelaaja vs. Pelaaja -peli."""
from kivi_paperi_sakset import KiviPaperiSakset


class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    """Kaksi ihmispelaajaa pelaa toisiaan vastaan."""
    def _toisen_siirto(self, _):
        """Kysyy toisen pelaajan siirron.

        Args:
            _: Ensimmäisen pelaajan siirto (ei käytetä).

        Returns:
            Toisen pelaajan syöttämä siirto.
        """
        return input("Toisen pelaajan siirto: ")
