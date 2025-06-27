from produkte import Produkt

from store import Laden

def start(laden):
    while True:
        print("\nWas möchtest du tun?")
        print("1. Alle Produkte im Laden anzeigen")
        print("2. Gesamtmenge im Laden anzeigen")
        print("3. Eine Bestellung aufgeben")
        print("4. Beenden")

        wahl = input("Deine Auswahl (1-4): ")

        if wahl == "1":
            for p in laden.alle_aktiven_produkte():
                print(p.anzeigen())

        elif wahl == "2":
            print(f"Gesamtmenge im Laden: {laden.gesamte_menge()}")

        elif wahl == "3":
            produkte = laden.alle_aktiven_produkte()
            bestellung = []
            for index, produkt in enumerate(produkte):
                print(f"{index + 1}. {produkt.anzeigen()}")
            print("Gib die Nummer und Menge ein (z.B. '1 2' für Produkt 1, Menge 2). Leere Eingabe zum Beenden.")
            while True:
                eingabe = input(">> ")
                if eingabe == "":
                    break
                try:
                    nr, menge = map(int, eingabe.split())
                    bestellung.append((produkte[nr - 1], menge))
                except:
                    print("Ungültige Eingabe. Bitte erneut versuchen.")

            try:
                gesamtpreis = laden.bestellung(bestellung)
                print(f"Bestellung erfolgreich! Gesamtpreis: {gesamtpreis}€")
            except Exception as e:
                print(f"Fehler: {e}")

        elif wahl == "4":
            print("Programm beendet.")
            break

        else:
            print("Ungültige Eingabe. Bitte 1–4 wählen.")

# Initiale Produktliste & Laden starten
if __name__ == "__main__":
    produktliste = [
        Produkt("MacBook Air M2", 1450, 100),
        Produkt("Bose QuietComfort Earbuds", 250, 500),
        Produkt("Google Pixel 7", 500, 250)
    ]
    laden = Laden(produktliste)
    start(laden)
