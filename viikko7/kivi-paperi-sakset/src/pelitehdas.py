"""Pelitehdas luo eri tyyppisiä peli-instansseja."""
from kps_pvp import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def luo_peli(valinta):
    """Luo peli-instanssin valinnan perusteella.

    Args:
        valinta: 'a' = pelaaja vs pelaaja, 'b' = tekoäly, 'c' = parannettu tekoäly

    Returns:
        Peli-instanssi tai None jos valinta on virheellinen.
    """
    if valinta == "a":
        return KPSPelaajaVsPelaaja()
    if valinta == "b":
        return KPSTekoaly()
    if valinta == "c":
        return KPSParempiTekoaly()
    return None
