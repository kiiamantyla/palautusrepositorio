"""Yksinkertainen tekoäly joka pelaa sekvenssin p, s, k, p, s, k..."""

class Tekoaly:
    """Yksinkertainen tekoäly."""
    def __init__(self):
        """Alustaa tekoälyn."""
        self._siirto = 0

    def anna_siirto(self):
        """Palauttaa seuraavan siirron (k/p/s).

        Returns:
            Seuraava siirto ('k', 'p' tai 's').
        """
        self._siirto = self._siirto + 1
        self._siirto = self._siirto % 3

        if self._siirto == 0:
            return "k"
        if self._siirto == 1:
            return "p"
        return "s"

    def aseta_siirto(self, siirto):
        """Asettaa pelaajan siirron. Tämä tekoäly ei käytä tätä tietoa.

        Args:
            siirto: Pelaajan siirto.
        """
        # ei tehdä mitään
