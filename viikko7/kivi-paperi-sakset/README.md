# Kivi-Paperi-Sakset - Web-sovellus

Flask-pohjainen web-sovellus klassiseen kivi-paperi-sakset peliin.

**Peli jatkuu kunnes toinen pelaaja on saavuttanut 5 voittoa!**

## Asennus

```bash
poetry install
```

## Sovelluksen käynnistäminen

```bash
cd src
poetry run python app.py
```

Sovellus käynnistyy osoitteessa http://127.0.0.1:5000

## Pelimuodot

- **Pelaaja vs. Pelaaja**: Kaksi ihmispelaajaa pelaa toisiaan vastaan
- **Pelaaja vs. Tekoäly**: Pelaa yksinkertaista tekoälyä vastaan
- **Pelaaja vs. Parannettu Tekoäly**: Pelaa tekoälyä vastaan joka oppii siirroistasi

## Testit

Sovellukselle on tehty kattavat automaattiset testit pytest-kirjastolla.

### Testien ajaminen

```bash
poetry run pytest
```

### Testit verbose-tilassa

```bash
poetry run pytest -v
```

### Testitilastot

Projektissa on yhteensä **42 testiä** jotka kattavat:

- **Flask-sovelluksen testit** (20 testiä): 
  - Reittien toiminta
  - Session hallinta
  - Pelitilan ylläpito
  - Kaikki pelimuodot
  - 5 voiton sääntö
  
- **Tuomarin testit** (10 testiä):
  - Pisteiden laskenta
  - Voittajan määritys
  - Tasapelitilanteet

- **Pelitehtaan testit** (5 testiä):
  - Eri pelityyppien luominen
  - Virheellisten valintojen käsittely

- **Tekoälyjen testit** (7 testiä):
  - Yksinkertaisen tekoälyn logiikka
  - Parannetun tekoälyn oppimiskyky
  - Muistin hallinta

## Projektirakenne

```
src/
├── app.py                      # Flask web-sovellus
├── index.py                    # Alkuperäinen CLI-sovellus
├── pelitehdas.py              # Pelien luonti (Factory pattern)
├── kivi_paperi_sakset.py      # Pelin peruslogiikka
├── kps_pvp.py                 # Pelaaja vs. Pelaaja
├── kps_tekoaly.py             # Pelaaja vs. Tekoäly
├── kps_parempi_tekoaly.py     # Pelaaja vs. Parannettu Tekoäly
├── tekoaly.py                 # Yksinkertainen tekoäly
├── tekoaly_parannettu.py      # Oppiva tekoäly
├── tuomari.py                 # Pisteiden laskenta
├── templates/                 # HTML-sivupohjat
│   ├── index.html
│   ├── pelaa.html
│   ├── tulos.html
│   └── loppu.html
└── tests/                     # Automaattiset testit
    ├── test_app.py
    ├── test_pelitehdas.py
    ├── test_tekoaly.py
    ├── test_tekoaly_parannettu.py
    └── test_tuomari.py
```

## Teknologiat

- **Python 3.12**
- **Flask** - Web-framework
- **pytest** - Testauskirjasto
- **pytest-flask** - Flask-testaustyökalut
- **Poetry** - Riippuvuuksien hallinta
