import pytest
from tuomari import Tuomari


class TestTuomari:
    def test_alussa_pisteet_nolla(self):
        tuomari = Tuomari()
        assert tuomari.ekan_pisteet == 0
        assert tuomari.tokan_pisteet == 0
        assert tuomari.tasapelit == 0

    def test_tasapeli_kirjataan_oikein(self):
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("k", "k")
        assert tuomari.tasapelit == 1
        assert tuomari.ekan_pisteet == 0
        assert tuomari.tokan_pisteet == 0

    def test_eka_voittaa_kivi_sakset(self):
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("k", "s")
        assert tuomari.ekan_pisteet == 1
        assert tuomari.tokan_pisteet == 0
        assert tuomari.tasapelit == 0

    def test_eka_voittaa_sakset_paperi(self):
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("s", "p")
        assert tuomari.ekan_pisteet == 1
        assert tuomari.tokan_pisteet == 0

    def test_eka_voittaa_paperi_kivi(self):
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("p", "k")
        assert tuomari.ekan_pisteet == 1
        assert tuomari.tokan_pisteet == 0

    def test_toka_voittaa_kivi_sakset(self):
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("s", "k")
        assert tuomari.ekan_pisteet == 0
        assert tuomari.tokan_pisteet == 1

    def test_toka_voittaa_paperi_sakset(self):
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("p", "s")
        assert tuomari.tokan_pisteet == 1
        assert tuomari.ekan_pisteet == 0

    def test_toka_voittaa_kivi_paperi(self):
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("k", "p")
        assert tuomari.tokan_pisteet == 1
        assert tuomari.ekan_pisteet == 0

    def test_monta_kierrosta(self):
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("k", "s")  # eka voittaa
        tuomari.kirjaa_siirto("p", "p")  # tasapeli
        tuomari.kirjaa_siirto("s", "k")  # toka voittaa

        assert tuomari.ekan_pisteet == 1
        assert tuomari.tokan_pisteet == 1
        assert tuomari.tasapelit == 1

    def test_str_toimii(self):
        tuomari = Tuomari()
        tuomari.kirjaa_siirto("k", "s")
        output = str(tuomari)
        assert "1" in output
        assert "0" in output
