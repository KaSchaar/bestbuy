from produkte import Produkt

class Laden:
    def __init__(self, produkte):
        self.produkte = produkte

    def produkt_hinzufuegen(self, produkt):
        self.produkte.append(produkt)

    def produkt_entfernen(self, produkt):
        if produkt in self.produkte:
            self.produkte.remove(produkt)

    def gesamte_menge(self):
        gesamt = 0
        for p in self.produkte:
            gesamt += p.gib_menge()
        return gesamt

    def alle_aktiven_produkte(self):
        aktive = []
        for p in self.produkte:
            if p.ist_aktiv():
                aktive.append(p)
        return aktive

    def bestellung(self, einkaufsliste):
        gesamtpreis = 0
        for produkt, menge in einkaufsliste:
            gesamtpreis += produkt.kaufen(menge)
        return gesamtpreis


if __name__ == "__main__":
    produkt_liste = [
        Produkt("MacBook Air M2", 1450, 100),
        Produkt("Bose QuietComfort Earbuds", 250, 500),
        Produkt("Google Pixel 7", 500, 250)
    ]

    laden = Laden(produkt_liste)
    produkte = laden.alle_aktiven_produkte()
    print(laden.gesamte_menge())
    print(laden.bestellung([(produkte[0], 1), (produkte[1], 2)]))
