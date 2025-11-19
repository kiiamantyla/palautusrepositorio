import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viite_mock = Mock()
        self.varasto_mock = Mock()
        self.viite_mock.uusi.return_value = 42
        
        # tehdään toteutus saldo-metodille
        def saldo(tuote_id):
            saldot = {1: 10, 2: 5, 3: 0}
            return saldot.get(tuote_id, 0)

        # tehdään toteutus hae_tuote-metodille
        def hae_tuote(tuote_id):
            tuotteet = {
                1: Tuote(1, "maito", 5),
                2: Tuote(2, "leipä", 3),
                3: Tuote(3, "voi", 4)
            }
            return tuotteet.get(tuote_id)
        
        self.varasto_mock.saldo.side_effect = saldo
        self.varasto_mock.hae_tuote.side_effect = hae_tuote
        
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viite_mock)
        
    def test_aloita_asiointi_nollaa_ostokset(self):
        # ensimmäinen ostos
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)

        
        # aloitetaan uusi asiointi
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 3)
    
    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()

    def test_yksi_tuote_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
        
    def test_kaksi_eri_tuotetta_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 8)
        
    def test_kaksi_samaa_tuotetta_oikeilla_parametreilla(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 10)
        
    def test_tuote_loppu_varastosta(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)  # tuote 3 on loppu
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
        
    def test_uusi_viite_jokaiseen_maksuun(self):
        self.viite_mock.uusi.side_effect = [101, 102, 103]
        
        # ensimmäinen maksu
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "11111")
        self.assertEqual(self.viite_mock.uusi.call_count, 1)
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 101, "11111", "33333-44455", 5)
        
        # toinen maksu
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "22222")
        self.assertEqual(self.viite_mock.uusi.call_count, 2)
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 102, "22222", "33333-44455", 3)
        
        # kolmas maksu
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "33333")
        self.assertEqual(self.viite_mock.uusi.call_count, 3)
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 103, "33333", "33333-44455", 5)
        
    