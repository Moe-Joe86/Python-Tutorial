# Etappe 4: Ausrüstung und Beute
# Namen der Variablen: durchgehend deutsch, ohne Umlaute
# Klasse wird als Zahl gespeichert
# Befehle jetzt Verb + Ziel (zwei Woerter), Design-Entscheidung aus Etappe 3 eingeloest
# Entscheidung 1: Kennung statt Anzeigename (z.B. "chitinpanzer", nicht "Chitinpanzer (rissig)")
# Entscheidung 2: Die Bahn ist nur ein Bild - gegner ist die Wahrheit (Liste von Positionszahlen)
# nimm/ablege kosten keine Runde - der Guide sagt dazu nichts, das ist meine eigene Wahl (siehe BERICHT.md)
# continue wird nicht benutzt (laut Etappe 3 Konzept 7 nur zum Erkennen, nicht zum Bauen)

kopf = """
  /------------\\
 |  VORPOSTEN   |
 ----------------
"""
print(kopf)

name = input("Wie heisst du, Marine? ")
print(f"Willkommen, {name}.")

kern_integritaet = 100
trefferpunkte = 100
munition = 40
vaporium = 0
rekruten_verfuegbar = 0
wellen_bis_evakuierung = 20

print(f"Kernintegritaet: {kern_integritaet}%")
print(f"Trefferpunkte: {trefferpunkte}")
print(f"Munition: {munition} Schuss")
print(f"Vaporium: {vaporium}")
print(f"Rekruten verfuegbar: {rekruten_verfuegbar}")
print(f"Wellen bis Evakuierung: {wellen_bis_evakuierung}")

letzte_meldung = "Hier Aussenposten Sieben. Bitte um Bestaetigung, over."
print(f"Aufgezeichnete Durchsage: {letzte_meldung}")

print("Waehle deine Klasse:")
print("1 Soldat")
print("2 Heavy")
print("3 Engineer")
print("4 Medic")
klassenwahl_text = input("Klasse (1-4): ").strip()
klasse = int(klassenwahl_text)

klasse_gueltig = False
if klasse == 1:
    trefferpunkte = 100
    schaden = 10
    panzerung = 5
    klassengeraet = "Sturmgewehr"
    klasse_gueltig = True
elif klasse == 2:
    trefferpunkte = 140
    schaden = 14
    panzerung = 10
    klassengeraet = "Schweres MG"
    klasse_gueltig = True
elif klasse == 3:
    trefferpunkte = 90
    schaden = 7
    panzerung = 4
    klassengeraet = "Multiwerkzeug"
    klasse_gueltig = True
elif klasse == 4:
    trefferpunkte = 80
    schaden = 6
    panzerung = 3
    klassengeraet = "Bio-Injektor"
    klasse_gueltig = True
else:
    print("Diese Klasse gibt es nicht.")

if klasse_gueltig:
    print(f"Klasse:        {klasse}")
    print(f"Trefferpunkte: {trefferpunkte}")
    print(f"Schaden:       {schaden}")
    print(f"Panzerung:     {panzerung}")

print("Auf dem Radar bewegt sich etwas, das dort nicht hingehoert.")
funk_antwort = input("Melden? (ja/nein) ").strip()
meldung_abgesetzt = funk_antwort == "ja"
print(f"Meldung abgesetzt: {meldung_abgesetzt}")

nachladen_noetig = False
erfahrung = 0
runde = 1
spiel_laeuft = True

inventar = []
vorfeld = []
FELDER = 10
BEUTE_PRO_WELLE = ["chitinpanzer", "organ", "datenkern"]

for welle in range(1, wellen_bis_evakuierung + 1):
    if not spiel_laeuft:
        break

    print(f"--- Welle {welle} von {wellen_bis_evakuierung} ---")

    gegner = []
    for i in range(welle):
        gegner.append(0)

    while True:
        eingabe = input(f"Welle {welle}, Runde {runde} > ").strip().lower()
        teile = eingabe.split()

        if len(teile) == 0:
            print("Bitte gib etwas ein.")
        else:
            befehl = teile[0]
            ziel = ""
            if len(teile) > 1:
                ziel = teile[1]

            rundenkosten = False
            welle_beendet = False

            if befehl == "status":
                anteil_kern = kern_integritaet / 100
                voll_kern = int(anteil_kern * 10)
                leer_kern = 10 - voll_kern
                balken_kern = "#" * voll_kern + "." * leer_kern

                anteil_marine = trefferpunkte / 100
                voll_marine = int(anteil_marine * 10)
                leer_marine = 10 - voll_marine
                balken_marine = "#" * voll_marine + "." * leer_marine

                anteil_munition = munition / 40
                voll_munition = int(anteil_munition * 10)
                leer_munition = 10 - voll_munition
                balken_munition = "#" * voll_munition + "." * leer_munition

                print(f"Kern     [{balken_kern}] {anteil_kern:.0%}")
                print(f"Marine   [{balken_marine}] {anteil_marine:.0%}")
                print(f"Munition [{balken_munition}] {anteil_munition:.0%}")
                print(f"Erfahrung: {erfahrung}")

            elif befehl == "feuern":
                if munition > 0 and not nachladen_noetig:
                    munition -= 1
                    if len(gegner) > 0:
                        gegner.pop(0)
                    erfahrung += 10
                    print(f"Geschossen. Munition uebrig: {munition}, Gegner uebrig: {len(gegner)}")
                    if munition == 0:
                        nachladen_noetig = True
                else:
                    print("Keine Munition mehr. Erst nachladen.")
                rundenkosten = True

            elif befehl == "nachladen":
                munition = 40
                nachladen_noetig = False
                print("Nachgeladen.")
                rundenkosten = True

            elif befehl == "beenden":
                print("Welle wird abgebrochen.")
                welle_beendet = True

            elif befehl == "inventar":
                if len(inventar) == 0:
                    print("Das Inventar ist leer.")
                else:
                    print(f"Inventar: {', '.join(inventar)}")

            elif befehl == "nimm":
                if ziel == "":
                    print("Nimm was?")
                elif ziel not in vorfeld:
                    print(f"{ziel} liegt hier nicht.")
                elif len(inventar) >= 10:
                    print("Das Inventar ist voll.")
                else:
                    vorfeld.remove(ziel)
                    inventar.append(ziel)
                    print(f"{ziel} aufgenommen.")

            elif befehl == "ablege":
                if ziel == "":
                    print("Ablegen was?")
                elif ziel not in inventar:
                    print(f"Du traegst kein {ziel}.")
                else:
                    inventar.remove(ziel)
                    vorfeld.append(ziel)
                    print(f"{ziel} abgelegt.")

            else:
                print("Unbekannter Befehl.")

            if welle_beendet:
                break

            if rundenkosten:
                runde += 1
                if len(gegner) > 0:
                    for i in range(len(gegner)):
                        gegner[i] += 1
                    kern_integritaet -= 5
                    trefferpunkte -= 2
                    print("Die Brut schlaegt zurueck.")

            bahn_felder = ["."] * FELDER
            for pos in gegner:
                if 0 <= pos < FELDER:
                    bahn_felder[pos] = "K"
            bahn = "S" + "".join(bahn_felder) + "@"
            print(bahn)

            if kern_integritaet <= 0:
                print("Die Kernintegritaet ist auf 0 gefallen. Der Vorposten ist verloren.")
                spiel_laeuft = False
                break

            if trefferpunkte <= 0:
                print("Du bist gefallen. Der Lauf ist zu Ende.")
                spiel_laeuft = False
                break

            if len(gegner) == 0:
                print("Welle geschafft.")
                for beute in BEUTE_PRO_WELLE:
                    vorfeld.append(beute)
                print("Im Vorfeld liegt jetzt etwas.")
                break

print("Programmende.")
