import pytest
from produkte import Produkt

# Test: Gültiges Produkt erzeugen
def test_valides_produkt():
    p = Produkt("MacBook", 1450, 100)
    assert p.name == "MacBook"
    assert p.preis == 1450
    assert p.menge == 100
    assert p.ist_aktiv() == True

# Test: Name darf nicht leer sein
def test_leerer_name():
    with pytest.raises(Exception) as e:
        Produkt("", 1450, 100)
    assert "Name darf nicht leer" in str(e.value)

# Test: Preis darf nicht negativ sein
def test_negativer_preis():
    with pytest.raises(Exception) as e:
        Produkt("Monitor", -5, 10)
    assert "Preis darf nicht negativ" in str(e.value)

# Test: Menge darf nicht negativ sein
def test_negative_menge():
    with pytest.raises(Exception) as e:
        Produkt("USB Stick", 5, -1)
    assert "Menge darf nicht negativ" in str(e.value)

# Test: kaufen reduziert Menge, deaktiviert bei 0
def test_kauf_bis_leer():
    p = Produkt("Tastatur", 50, 1)
    kosten = p.kaufen(1)
    assert kosten == 50
    assert p.menge == 0
    assert p.ist_aktiv() == False

# Test: Kauf über Lagerbestand
def test_kauf_zu_viel():
    p = Produkt("HDMI-Kabel", 20, 2)
    with pytest.raises(Exception) as e:
        p.kaufen(5)
    assert "Nicht genug auf Lager" in str(e.value)

# Test: Produkt ist deaktiviert → darf nicht kaufen
def test_kauf_inaktives_produkt():
    p = Produkt("USB Stick", 5, 1)
    p.deaktiviere()
    with pytest.raises(Exception) as e:
        p.kaufen(1)
    assert "nicht aktiv" in str(e.value)
