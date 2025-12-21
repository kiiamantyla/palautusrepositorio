import pytest
from app import app as flask_app


@pytest.fixture
def app():
    flask_app.config['TESTING'] = True
    flask_app.config['SECRET_KEY'] = 'test-secret-key'
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


class TestFlaskApp:
    def test_index_page_loads(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert b'Kivi, Paperi, Sakset' in response.data

    def test_index_has_game_options(self, client):
        response = client.get('/')
        assert b'Ihmist' in response.data  # "Ihmistä vastaan"
        assert b'Teko' in response.data     # "Tekoälyä vastaan"

    def test_start_pelaaja_vs_pelaaja(self, client):
        response = client.post('/start', data={'valinta': 'a'}, follow_redirects=False)
        assert response.status_code == 302
        assert '/pelaa' in response.location

    def test_start_tekoaly(self, client):
        response = client.post('/start', data={'valinta': 'b'}, follow_redirects=False)
        assert response.status_code == 302
        assert '/pelaa' in response.location

    def test_start_parempi_tekoaly(self, client):
        response = client.post('/start', data={'valinta': 'c'}, follow_redirects=False)
        assert response.status_code == 302
        assert '/pelaa' in response.location

    def test_start_invalid_choice_redirects_to_index(self, client):
        response = client.post('/start', data={'valinta': 'x'}, follow_redirects=False)
        assert response.status_code == 302
        assert '/' in response.location

    def test_pelaa_page_requires_session(self, client):
        response = client.get('/pelaa', follow_redirects=False)
        assert response.status_code == 302

    def test_pelaa_page_with_session(self, client):
        # Aloita peli ensin
        client.post('/start', data={'valinta': 'b'})
        response = client.get('/pelaa')
        assert response.status_code == 200

    def test_siirto_against_ai(self, client):
        # Aloita peli tekoälyä vastaan
        client.post('/start', data={'valinta': 'b'})
        response = client.post('/siirto', data={'siirto': 'k'}, follow_redirects=False)
        assert response.status_code == 302
        assert '/tulos' in response.location

    def test_siirto_invalid_redirects_to_loppu(self, client):
        client.post('/start', data={'valinta': 'b'})
        response = client.post('/siirto', data={'siirto': 'x'}, follow_redirects=False)
        assert response.status_code == 302
        assert '/loppu' in response.location

    def test_tulos_page(self, client):
        # Aloita peli ja tee siirto
        client.post('/start', data={'valinta': 'b'})
        client.post('/siirto', data={'siirto': 'k'})
        response = client.get('/tulos')
        assert response.status_code == 200
        assert b'Kierroksen tulos' in response.data

    def test_loppu_page(self, client):
        client.post('/start', data={'valinta': 'b'})
        response = client.get('/loppu')
        assert response.status_code == 200
        assert b'Kiitos' in response.data

    def test_full_game_flow(self, client):
        # Aloita peli
        response = client.post('/start', data={'valinta': 'b'}, follow_redirects=True)
        assert response.status_code == 200

        # Pelaa kierros
        response = client.post('/siirto', data={'siirto': 'k'}, follow_redirects=True)
        assert response.status_code == 200

        # Pelaa toinen kierros
        client.get('/pelaa')
        response = client.post('/siirto', data={'siirto': 'p'}, follow_redirects=True)
        assert response.status_code == 200

        # Lopeta peli
        response = client.get('/loppu')
        assert response.status_code == 200

    def test_score_tracking(self, client):
        with client.session_transaction() as session:
            session['valinta'] = 'b'
            session['ekan_pisteet'] = 2
            session['tokan_pisteet'] = 1
            session['tasapelit'] = 1

        response = client.get('/pelaa')
        assert b'2' in response.data  # ekan pisteet
        assert b'1' in response.data  # tokan pisteet tai tasapelit

    def test_pvp_both_moves_required(self, client):
        client.post('/start', data={'valinta': 'a'})
        response = client.post('/siirto', data={
            'siirto': 'k',
            'tokan_siirto': 'p'
        }, follow_redirects=False)
        assert response.status_code == 302
        assert '/tulos' in response.location

    def test_parannettu_tekoaly_uses_memory(self, client):
        client.post('/start', data={'valinta': 'c'})

        # Pelaa useita kierroksia
        for _ in range(3):
            client.post('/siirto', data={'siirto': 'k'})
            client.get('/pelaa')

        # Varmista että session sisältää peli-instanssin
        with client.session_transaction() as session:
            assert 'peli_data' in session
            assert len(session['peli_data']) > 0

    def test_game_ends_at_three_wins(self, client):
        # Aloita peli
        client.post('/start', data={'valinta': 'b'})

        # Tekoäly 'b' pelaa sekvenssin: p, s, k, p, s, k...
        # Voittavat siirrot: s (voittaa p), k (voittaa s), p (voittaa k),
        # s (voittaa p),k (voittaa s)
        moves = ['s', 'k', 'p', 's', 'k']

        for i, move in enumerate(moves):
            response = client.post('/siirto', data={'siirto': move}, follow_redirects=False)
            if i < 2:  # Ensimmäiset 2 voittoa ohjataan tulos-sivulle
                assert '/tulos' in response.location
                client.get('/pelaa')  # Siirry takaisin pelaamaan
            else:  # Viides voitto ohjaa loppu-sivulle
                assert '/loppu' in response.location

    def test_pelaa_redirects_to_loppu_if_game_finished(self, client):
        # Aloita peli ja aseta toinen pelaaja jo voittaneeksi
        client.post('/start', data={'valinta': 'b'})

        with client.session_transaction() as session:
            session['ekan_pisteet'] = 3
            session['tokan_pisteet'] = 2

        # Yritä mennä pelaa-sivulle
        response = client.get('/pelaa', follow_redirects=False)

        # Pitäisi ohjata loppu-sivulle
        assert response.status_code == 302
        assert '/loppu' in response.location

    def test_voittojen_tavoite_shown_in_pelaa(self, client):
        client.post('/start', data={'valinta': 'b'})
        response = client.get('/pelaa')
        assert b'Tavoite' in response.data
        assert b'3' in response.data

    def test_full_game_to_three_wins(self, client):
        # Simuloi täysi peli 3 voittoon
        client.post('/start', data={'valinta': 'b'})

        # Pelaa riittävästi kierroksia että joku voittaa
        # Tekoäly tekee sekvenssin p, s, k, p, s, k...
        # Pelataan paperi joka kerta -> voittaa kiven, häviää saksille, tasapeli paperin kanssa
        max_rounds = 20
        for i in range(max_rounds):
            response = client.post('/siirto', data={'siirto': 'p'}, follow_redirects=False)
            if '/loppu' in response.location:
                break
            if '/tulos' in response.location:
                client.get('/pelaa')

        # Varmista että päädyttiin loppu-sivulle
        final_response = client.get(response.location, follow_redirects=True)
        assert b'Kiitos' in final_response.data
