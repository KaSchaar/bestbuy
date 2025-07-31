import pytest
from produkte import (
    Produkt, NichtlagerProdukt, BegrenztesProdukt,
    ProzentRabatt, ZweiterHalbpreis, DritterGratis, Store
)

# Basis-Tests für Produkt
def test_produkt_erstellung_valide():
    p = Produkt("MacBook", 1450, 10)
    assert p.name == "MacBook"
    assert p.preis == 1450
    assert p.menge == 10
    assert p.ist_aktiv()

def test_produkt_leerer_name():
    with pytest.raises(ValueError):
        Produkt("", 1000, 1)

def test_produkt_negativer_preis():
    with pytest.raises(ValueError):
        Produkt("Test", -1, 1)

def test_produkt_negativer_lagerbestand():
    with pytest.raises(ValueError):
        Produkt("Test", 100, -5)

def test_produkt_kauf_normal():
    p = Produkt("Monitor", 300, 5)
    betrag = p.kaufen(2)
    assert betrag == 600
    assert p.menge == 3

def test_produkt_kauf_mehr_als_lager():
    p = Produkt("Kabel", 10, 3)
    with pytest.raises(ValueError):
        p.kaufen(4)

def test_produkt_inaktiv_nach_kauf():
    p = Produkt("Maus", 20, 1)
    p.kaufen(1)
    assert not p.ist_aktiv()

# NichtlagerProdukt
def test_nichtlagerprodukt_kauf():
    p = NichtlagerProdukt("Windows Lizenz", 100)
    betrag = p.kaufen(3)
    assert betrag == 300
    assert p.menge == 0
    assert p.ist_aktiv()

# BegrenztesProdukt
def test_begrenztes_produkt():
    p = BegrenztesProdukt("Versand", 10, 100, max_menge_pro_bestellung=1)
    with pytest.raises(ValueError):
        p.kaufen(2)

# Rabattaktionen
def test_prozent_rabatt():
    p = Produkt("Smartphone", 1000, 10)
    aktion = ProzentRabatt("20% Rabatt", 20)
    p.setze_aktion(aktion)
    betrag = p.kaufen(2)
    assert betrag == 1600

def test_zweiter_halbpreis():
    p = Produkt("Kopfhörer", 100, 10)
    aktion = ZweiterHalbpreis("2. zum halben Preis")
    p.setze_aktion(aktion)
    betrag = p.kaufen(3)
    # 2 Produkte: 1x 100 + 1x 50, 3. wieder 100 = 250
    assert betrag == 250

def test_dritter_gratis():
    p = Produkt("Tastatur", 80, 6)
    aktion = DritterGratis("3. gratis")
    p.setze_aktion(aktion)
    betrag = p.kaufen(6)
    # 6 Produkte → 2 gratis → 4x80 = 320
    assert betrag == 320

# Magic Methoden
def test_str_ausgabe():
    p = Produkt("Mac", 1200, 1)
    assert str(p) == "Mac, Preis: 1200, Menge: 1"

def test_vergleich_gt_lt():
    a = Produkt("A", 500, 5)
    b = Produkt("B", 600, 5)
    assert b > a
    assert a < b

# Store Funktionen
def test_store_contains_und_add():
    a = Produkt("A", 100, 1)
    b = Produkt("B", 200, 2)
    store1 = Store([a])
    store2 = Store([b])
    store3 = store1 + store2
    assert a in store3
    assert b in store3
    assert a not in store2
