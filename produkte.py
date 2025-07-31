from abc import ABC, abstractmethod

class Produkt:
    def __init__(self, name, preis, menge):
        if not name:
            raise ValueError("Name darf nicht leer sein")
        if preis < 0:
            raise ValueError("Preis darf nicht negativ sein")
        if menge < 0:
            raise ValueError("Menge darf nicht negativ sein")

        self._name = name
        self._preis = preis
        self._menge = menge
        self._aktiv = True
        self._aktion = None

    @property
    def name(self):
        return self._name

    @property
    def preis(self):
        return self._preis

    @preis.setter
    def preis(self, wert):
        if wert < 0:
            raise ValueError("Preis darf nicht negativ sein")
        self._preis = wert

    @property
    def menge(self):
        return self._menge

    @menge.setter
    def menge(self, wert):
        if wert < 0:
            raise ValueError("Ungültige Menge")
        self._menge = wert
        if wert == 0:
            self.deaktiviere()

    def ist_aktiv(self):
        return self._aktiv

    def aktiviere(self):
        self._aktiv = True

    def deaktiviere(self):
        self._aktiv = False

    def setze_aktion(self, aktion):
        self._aktion = aktion

    def gib_aktion(self):
        return self._aktion

    def __str__(self):
        aktionstext = f" (Aktion: {self._aktion.name})" if self._aktion else ""
        return f"{self._name}, Preis: {self._preis}, Menge: {self._menge}{aktionstext}"

    def __gt__(self, anderes):
        return self.preis > anderes.preis

    def __lt__(self, anderes):
        return self.preis < anderes.preis

    def kaufen(self, menge):
        if not self._aktiv:
            raise ValueError("Produkt nicht aktiv")
        if menge <= 0:
            raise ValueError("Menge muss positiv sein")
        if menge > self._menge:
            raise ValueError("Nicht genug auf Lager")
        self._menge -= menge
        if self._menge == 0:
            self.deaktiviere()

        if self._aktion:
            return self._aktion.wende_an(self, menge)
        return menge * self._preis


class NichtlagerProdukt(Produkt):
    def __init__(self, name, preis):
        super().__init__(name, preis, 0)
        self._aktiv = True

    def kaufen(self, menge):
        if not self._aktiv:
            raise ValueError("Produkt nicht aktiv")
        if menge <= 0:
            raise ValueError("Menge muss positiv sein")
        if self._aktion:
            return self._aktion.wende_an(self, menge)
        return menge * self._preis


class BegrenztesProdukt(Produkt):
    def __init__(self, name, preis, menge, max_menge_pro_bestellung):
        super().__init__(name, preis, menge)
        self._max = max_menge_pro_bestellung

    def kaufen(self, menge):
        if menge > self._max:
            raise ValueError("Maximale Bestellmenge überschritten")
        return super().kaufen(menge)


class Aktion(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def wende_an(self, produkt, menge):
        pass


class ProzentRabatt(Aktion):
    def __init__(self, name, prozent):
        super().__init__(name)
        self.prozent = prozent

    def wende_an(self, produkt, menge):
        gesamt = produkt.preis * menge
        rabatt = gesamt * (self.prozent / 100)
        return gesamt - rabatt


class ZweiterHalbpreis(Aktion):
    def __init__(self, name):
        super().__init__(name)

    def wende_an(self, produkt, menge):
        paare = menge // 2
        rest = menge % 2
        return paare * (produkt.preis + produkt.preis / 2) + rest * produkt.preis


class DritterGratis(Aktion):
    def __init__(self, name):
        super().__init__(name)

    def wende_an(self, produkt, menge):
        gratis = menge // 3
        return (menge - gratis) * produkt.preis


class Store:
    def __init__(self, produkte):
        self.produkte = produkte

    def __contains__(self, produkt):
        return produkt in self.produkte

    def __add__(self, anderer_store):
        neue_liste = self.produkte + anderer_store.produkte
        return Store(neue_liste)
