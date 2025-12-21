## Päätyikö agentti toimivaan ratkaisuun?
Agentti päätyi toimivaan ratkaisuun.

## Miten varmistuit, että ratkaisu toimii?
Varmistuin ratkaisun toimivuudesta:
- Testasin sovellusta itse pelaamalla erilaisia pelejä sillä
- Ajoin automatisoidut testit ja varmistin että ne menivät läpi ilman virheitä
- Erityisesti testeillä tarkistettiin pelin päättymisehdot

## Oletko ihan varma, että ratkaisu toimii oikein?
Ratkaisu toimii tarkoituksen mukaisesti. On kuitenkin todennäköistä ettei kaikkia reunatapauksia ole testattu.

## Kuinka paljon jouduit antamaan agentille komentoja matkan varrella?
Yllättävän vähällä ohjeistuksella agentti pystyi tekemää toimivan sovelluksen, mutta se ei käyttänyt ollenkaan annettuja toiminnallisuuksia koodissa vaan kopio samankaltaiset toiminnallisuudet app.py tiedostoon.

## Kuinka hyvät agentin tekemät testit olivat?
Testit olivat pääosin hyviä ja selkeitä:
- ne oli nimetty selkeästi
- testasivat melko laajasti pelilogiikkaa
- erityisesti päättymisehdot oli testattu
- muitakin kuin unittest ympäristöä olisi voinut käyttää

## Onko agentin tekemä koodi ymmärrettävää?
Agentin tekemä koodi on pääosin ymmärrettävää, mutta siinä on myös muutamia kohtia mitä piti selväntää.
Hyvää:
- selkeästi jäsennelty koodi
- on looginen
- vastaa testejä hyvin
Epäselvempiä kohtia:
- peli-instanssin serialisointi
- yksityisen metodin käyttö app.pyssä
- syötteiden validoinnissa ei ole virheilmoitusta

## Miten agentti on muuttanut edellisessä tehtävässä tekemääsi koodia?
Agentti ei muuttanut tekemääni koodia muuten kuin pylintin mukaiseksi.
