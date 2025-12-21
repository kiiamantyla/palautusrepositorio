import pytest
from tekoaly_parannettu import TekoalyParannettu


class TestTekoalyParannettu:
    def test_aluksi_palauttaa_kiven(self):
        tekoaly = TekoalyParannettu(10)
        assert tekoaly.anna_siirto() == "k"

    def test_yhden_siirron_jalkeen_palauttaa_kiven(self):
        tekoaly = TekoalyParannettu(10)
        tekoaly.aseta_siirto("k")
        assert tekoaly.anna_siirto() == "k"

    def test_oppii_vastustajan_siirroista(self):
        tekoaly = TekoalyParannettu(10)
        # Annetaan useita kivi-siirtoja
        for _ in range(5):
            tekoaly.aseta_siirto("k")

        # Tekoälyn pitäisi oppia ja antaa paperi (voittaa kiven)
        siirto = tekoaly.anna_siirto()
        assert siirto == "p"

    def test_muisti_tayttyy_oikein(self):
        tekoaly = TekoalyParannettu(3)
        tekoaly.aseta_siirto("k")
        tekoaly.aseta_siirto("p")
        tekoaly.aseta_siirto("s")
        # Muisti täynnä, seuraava siirto korvaa vanhimman
        tekoaly.aseta_siirto("k")
        # Ei pitäisi kaatua
        siirto = tekoaly.anna_siirto()
        assert siirto in ["k", "p", "s"]

    def test_vaihtelevat_siirrot(self):
        tekoaly = TekoalyParannettu(10)
        tekoaly.aseta_siirto("k")
        tekoaly.aseta_siirto("p")
        tekoaly.aseta_siirto("p")
        tekoaly.aseta_siirto("p")

        # Papereita eniten, pitäisi antaa sakset
        siirto = tekoaly.anna_siirto()
        assert siirto == "s"
