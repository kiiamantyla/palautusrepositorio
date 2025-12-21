import pytest
from pelitehdas import luo_peli
from kps_pvp import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly


class TestPelitehdas:
    def test_luo_pelaaja_vs_pelaaja(self):
        peli = luo_peli("a")
        assert isinstance(peli, KPSPelaajaVsPelaaja)

    def test_luo_tekoaly_peli(self):
        peli = luo_peli("b")
        assert isinstance(peli, KPSTekoaly)

    def test_luo_parempi_tekoaly_peli(self):
        peli = luo_peli("c")
        assert isinstance(peli, KPSParempiTekoaly)

    def test_virheellinen_valinta_palauttaa_none(self):
        peli = luo_peli("x")
        assert peli is None

    def test_tyhja_valinta_palauttaa_none(self):
        peli = luo_peli("")
        assert peli is None
