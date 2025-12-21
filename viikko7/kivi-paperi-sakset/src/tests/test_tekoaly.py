import pytest
from tekoaly import Tekoaly


class TestTekoaly:
    def test_anna_siirto_palauttaa_kps(self):
        tekoaly = Tekoaly()
        # Ensimmäinen siirto on p (koska _siirto alkaa 0:sta, kasvatetaan 1:ksi)
        assert tekoaly.anna_siirto() == "p"
        # Toinen siirto on s
        assert tekoaly.anna_siirto() == "s"
        # Kolmas siirto on k (modulo 3 antaa 0)
        assert tekoaly.anna_siirto() == "k"
        # Neljäs siirto taas p
        assert tekoaly.anna_siirto() == "p"

    def test_aseta_siirto_ei_tee_mitaan(self):
        tekoaly = Tekoaly()
        tekoaly.aseta_siirto("k")
        # Pitäisi silti palauttaa sama sekvenssi
        assert tekoaly.anna_siirto() == "p"
        assert tekoaly.anna_siirto() == "s"
