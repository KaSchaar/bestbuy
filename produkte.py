class Produkt:
    def __init__(self, name, preis, menge):
        if name == "":
            raise Exception("Name darf nicht leer sein")
        if preis < 0:
            raise Exception("Preis darf nicht negativ sein")
        if menge < 0:
            raise Exception("Menge darf nicht negativ sein")

        self.name = name
        self.preis = preis
        self.menge = menge
        self.aktiv = True

    def gib_menge(self):
        return self.menge

    def setze_menge(self, menge):
        if menge < 0:
            raise Exception("Ungültige Menge")
        self.menge = menge
        if menge == 0:
            self.deaktiviere()

    def ist_aktiv(self):
        return self.aktiv

    def aktiviere(self):
        self.aktiv = True

    def deaktiviere(self):
        self.aktiv = False

    def anzeigen(self):
        return f"{self.name}, Preis: {self.preis}, Menge: {self.menge}"

    def kaufen(self, menge):
        if not self.aktiv:
            raise Exception("Produkt nicht aktiv")
        if menge <= 0:
            raise Exception("Menge muss positiv sein")
        if menge > self.menge:
            raise Exception("Nicht genug auf Lager")
        self.menge -= menge
        if self.menge == 0:
            self.deaktiviere()
        return menge * self.preis
