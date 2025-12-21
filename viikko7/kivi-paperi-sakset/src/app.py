"""Flask web-sovellus kivi-paperi-sakset pelille."""
import secrets
import pickle
import base64

from flask import Flask, render_template, request, session, redirect, url_for
from pelitehdas import luo_peli
from tuomari import Tuomari

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

VOITTOJEN_TAVOITE = 3

@app.route('/')
def index():
    """Näyttää sovelluksen etusivun."""
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    """Aloittaa uuden pelin valitulla pelimuodolla."""
    session.clear()  # Tyhjennetään vanha pelitilanne
    valinta = request.form.get('valinta')
    peli = luo_peli(valinta)

    if not peli:
        return redirect(url_for('index'))

    session['valinta'] = valinta
    session['ekan_pisteet'] = 0
    session['tokan_pisteet'] = 0
    session['tasapelit'] = 0

    # Serialisoidaan peli-instanssi sessioniin
    session['peli_data'] = base64.b64encode(pickle.dumps(peli)).decode('utf-8')

    return redirect(url_for('pelaa'))

@app.route('/pelaa')
def pelaa():
    """Näyttää pelisivun jossa tehdään siirtoja."""
    if 'valinta' not in session:
        return redirect(url_for('index'))

    # Tarkista onko peli jo päättynyt
    ekan_pisteet = session.get('ekan_pisteet', 0)
    tokan_pisteet = session.get('tokan_pisteet', 0)

    if ekan_pisteet >= VOITTOJEN_TAVOITE or tokan_pisteet >= VOITTOJEN_TAVOITE:
        return redirect(url_for('loppu'))

    return render_template('pelaa.html',
                         valinta=session['valinta'],
                         ekan_pisteet=ekan_pisteet,
                         tokan_pisteet=tokan_pisteet,
                         tasapelit=session.get('tasapelit', 0),
                         voittojen_tavoite=VOITTOJEN_TAVOITE)

@app.route('/siirto', methods=['POST'])
def siirto():
    """Käsittelee pelaajien siirrot ja päivittää pelitilanteen."""
    if 'valinta' not in session:
        return redirect(url_for('index'))

    ekan_siirto = request.form.get('siirto')
    valinta = session['valinta']

    # Tarkista että siirto on validi
    if ekan_siirto not in ['k', 'p', 's']:
        return redirect(url_for('loppu'))

    # Hae peli-instanssi sessionista
    peli_data = session.get('peli_data')
    if not peli_data:
        return redirect(url_for('index'))

    peli = pickle.loads(base64.b64decode(peli_data))

    # Hae toisen pelaajan siirto
    tokan_siirto = None
    if valinta == 'a':
        # Pelaaja vs pelaaja - odotamme toista siirtoa
        tokan_siirto = request.form.get('tokan_siirto')
        if not tokan_siirto or tokan_siirto not in ['k', 'p', 's']:
            return redirect(url_for('loppu'))
    else:
        # Käytetään pelin _toisen_siirto metodia tekoälylle
        tokan_siirto = peli._toisen_siirto(ekan_siirto)

    # Tallenna päivitetty peli takaisin sessioniin
    session['peli_data'] = base64.b64encode(pickle.dumps(peli)).decode('utf-8')

    # Päivitä pisteet
    tuomari = Tuomari()
    tuomari.ekan_pisteet = session.get('ekan_pisteet', 0)
    tuomari.tokan_pisteet = session.get('tokan_pisteet', 0)
    tuomari.tasapelit = session.get('tasapelit', 0)

    tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)

    session['ekan_pisteet'] = tuomari.ekan_pisteet
    session['tokan_pisteet'] = tuomari.tokan_pisteet
    session['tasapelit'] = tuomari.tasapelit
    session['viimeisin_ekan_siirto'] = ekan_siirto
    session['viimeisin_tokan_siirto'] = tokan_siirto

    # Tarkista onko peli päättynyt
    if tuomari.ekan_pisteet >= VOITTOJEN_TAVOITE or tuomari.tokan_pisteet >= VOITTOJEN_TAVOITE:
        return redirect(url_for('loppu'))

    return redirect(url_for('tulos'))

@app.route('/tulos')
def tulos():
    """Näyttää kierroksen tuloksen."""
    if 'valinta' not in session:
        return redirect(url_for('index'))

    return render_template('tulos.html',
                         valinta=session['valinta'],
                         ekan_siirto=session.get('viimeisin_ekan_siirto'),
                         tokan_siirto=session.get('viimeisin_tokan_siirto'),
                         ekan_pisteet=session.get('ekan_pisteet', 0),
                         tokan_pisteet=session.get('tokan_pisteet', 0),
                         tasapelit=session.get('tasapelit', 0),
                         voittojen_tavoite=VOITTOJEN_TAVOITE)

@app.route('/loppu')
def loppu():
    """Näyttää pelin lopputuloksen."""
    ekan_pisteet = session.get('ekan_pisteet', 0)
    tokan_pisteet = session.get('tokan_pisteet', 0)
    tasapelit = session.get('tasapelit', 0)
    session.clear()

    return render_template('loppu.html',
                         ekan_pisteet=ekan_pisteet,
                         tokan_pisteet=tokan_pisteet,
                         tasapelit=tasapelit)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
