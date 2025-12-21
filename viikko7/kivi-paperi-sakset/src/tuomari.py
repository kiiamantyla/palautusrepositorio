"""Tuomari-luokka pistelaskentaan."""

# Luokka pitää kirjaa ensimmäisen ja toisen pelaajan pisteistä sekä tasapelien määrästä.
class Tuomari:
    """Tuomari laskee pelin pisteet ja tilanteet."""
    def __init__(self):
        """Alustaa tuomarin."""
        self.ekan_pisteet = 0
        self.tokan_pisteet = 0
        self.tasapelit = 0

    def kirjaa_siirto(self, ekan_siirto, tokan_siirto):
        """Kirjaa pelaajien siirrot ja päivittää pisteet.

        Args:
            ekan_siirto: Ensimmäisen pelaajan siirto.
            tokan_siirto: Toisen pelaajan siirto.
        """
        if self._tasapeli(ekan_siirto, tokan_siirto):
            self.tasapelit = self.tasapelit + 1
        elif self._eka_voittaa(ekan_siirto, tokan_siirto):
            self.ekan_pisteet = self.ekan_pisteet + 1
        else:
            self.tokan_pisteet = self.tokan_pisteet + 1

    def __str__(self):
        """Palauttaa pelien tilanteen merkkijonona.

        Returns:
            Pelitilanne ja tasapelien määrä merkkijonona.
        """
        return (f"Pelitilanne: {self.ekan_pisteet} - {self.tokan_pisteet}\n"
                f"Tasapelit: {self.tasapelit}")

    # sisäinen metodi, jolla tarkastetaan tuliko tasapeli
    def _tasapeli(self, eka, toka):
        if eka == toka:
            return True

        return False

    # sisäinen metodi joka tarkastaa voittaako eka pelaaja tokan
    def _eka_voittaa(self, eka, toka):
        if eka == "k" and toka == "s":
            return True
        if eka == "s" and toka == "p":
            return True
        if eka == "p" and toka == "k":
            return True

        return False
