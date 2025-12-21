"""Komentoriviohjelma kivi-paperi-sakset pelille."""
from pelitehdas import luo_peli

def main():
    """Pääohjelma."""
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        valinta = input()

        peli = luo_peli(valinta)
        if peli:
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            peli.pelaa()


if __name__ == "__main__":
    main()
