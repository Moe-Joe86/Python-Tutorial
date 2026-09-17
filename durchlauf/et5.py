# Etappe 5: Der Vorposten und das Depot
# Namen: durchgehend deutsch, ohne Umlaute
# Klasse als Zahl gespeichert
# Entscheidung 1 (versiegelter Weg): Der Weg zur Landeplattform fehlt einfach (Empfehlung des Guides uebernommen)
# Entscheidung 2 (Bestand im Depot): kein Bestand, WAREN ist ein reiner Preiskatalog
# Kennung statt Anzeigename im Inventar/Vorfeld (Entscheidung aus Etappe 4), ANZEIGENAMEN uebersetzt beim Anzeigen
# umsehen/gehe/depot/kaufe/verkaufe kosten keine Runde - der Guide legt das nirgends fest (siehe BERICHT.md)

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
rekruten_verfuegbar = 0
wellen_bis_evakuierung = 20

print(f"Kernintegritaet: {kern_integritaet}%")
print(f"Trefferpunkte: {trefferpunkte}")
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

# --- Die Karte ---

sektoren = {
    "nordtor": {
        "beschreibung": "Das Nordtor. Hier bist du gelandet.",
        "integritaet": 100,
        "nachbarn": {"sueden": "kern"},
    },
    "osttor": {
        "beschreibung": "Das Osttor. Der Tunnel Richtung Osten ist verschuettet.",
        "integritaet": 100,
        "nachbarn": {"westen": "kern"},
    },
    "kern": {
        "beschreibung": "Der Reaktorkern. Er haelt die Kuppel.",
        "nachbarn": {"norden": "nordtor", "osten": "osttor", "westen": "depot"},
    },
    "depot": {
        "beschreibung": "Das Depot. Hier wird gekauft und verkauft.",
        "integritaet": 100,
        "nachbarn": {"osten": "kern", "sueden": "werkstatt"},
    },
    "werkstatt": {
        "beschreibung": "Die Werkstatt. Ab Etappe 13 wird hier gebaut.",
        "integritaet": 100,
        "nachbarn": {"norden": "depot"},
    },
    "landeplattform": {
        "beschreibung": "Die Landeplattform. Hier soll in Etappe 17 das Evakuierungsschiff landen.",
        "integritaet": 100,
        "nachbarn": {},
    },
}
# Kein Sektor hat "osten"/"westen" als nachbarn Richtung landeplattform - der Weg fehlt einfach
# (Entscheidung 1, empfohlene Variante). Die Landeplattform ist dadurch unerreichbar.
aktueller_sektor = "nordtor"

WAREN = {"medkit": 40, "munition": 15, "panzerplatte": 90}
STAPELBAR = {"medkit": False, "munition": True, "panzerplatte": False}
VERKAUFSWERTE = {"chitinpanzer": 5, "organ": 12}
ANZEIGENAMEN = {
    "medkit": "Medkit",
    "munition": "Munition",
    "panzerplatte": "Panzerplatte",
    "chitinpanzer": "Chitinpanzer",
    "organ": "Organ",
    "datenkern": "Datenkern der Brut",
    "vaporium": "Vaporium",
}

vorrat = {"vaporium": 0, "munition": 40, "chitinpanzer": 0, "organ": 0}
MAGAZIN_GROESSE = 8
geladen = MAGAZIN_GROESSE
nachladen_noetig = False

STUFENTABELLE = {0: 1, 100: 2, 300: 3, 600: 4, 1000: 5}

erfahrung = 0
runde = 1
spiel_laeuft = True

inventar = []
vorfeld = []
FELDER = 10

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
            menge_text = ""
            if len(teile) > 2:
                menge_text = teile[2]

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

                anteil_magazin = geladen / MAGAZIN_GROESSE
                voll_magazin = int(anteil_magazin * 10)
                leer_magazin = 10 - voll_magazin
                balken_magazin = "#" * voll_magazin + "." * leer_magazin

                stufe = 1
                for schwelle in STUFENTABELLE:
                    if erfahrung >= schwelle:
                        if STUFENTABELLE[schwelle] > stufe:
                            stufe = STUFENTABELLE[schwelle]

                print(f"Kern     [{balken_kern}] {anteil_kern:.0%}")
                print(f"Marine   [{balken_marine}] {anteil_marine:.0%}")
                print(f"Magazin  [{balken_magazin}] {anteil_magazin:.0%}")
                print(f"Munition im Vorrat: {vorrat['munition']}")
                print(f"Vaporium: {vorrat['vaporium']}")
                print(f"Erfahrung: {erfahrung} (Stufe {stufe})")

            elif befehl == "feuern":
                if geladen > 0:
                    geladen -= 1
                    if len(gegner) > 0:
                        gegner.pop(0)
                    erfahrung += 10
                    print(f"Geschossen. Geladen: {geladen}, Gegner uebrig: {len(gegner)}")
                    if geladen == 0:
                        nachladen_noetig = True
                else:
                    print("Magazin leer. Erst nachladen.")
                rundenkosten = True

            elif befehl == "nachladen":
                platz = MAGAZIN_GROESSE - geladen
                nachschub = vorrat["munition"]
                verschoben = platz
                if nachschub < platz:
                    verschoben = nachschub
                if verschoben == 0:
                    print("Kein Nachschub im Vorrat. Erst im Depot kaufen.")
                else:
                    geladen += verschoben
                    vorrat["munition"] -= verschoben
                    nachladen_noetig = False
                    print(f"Nachgeladen. Magazin: {geladen}, Vorrat: {vorrat['munition']}")
                rundenkosten = True

            elif befehl == "beenden":
                print("Welle wird abgebrochen.")
                welle_beendet = True

            elif befehl == "inventar":
                if len(inventar) == 0:
                    print("Das Inventar ist leer.")
                else:
                    namen = []
                    for ding in inventar:
                        namen.append(ANZEIGENAMEN.get(ding, ding))
                    print(f"Inventar: {', '.join(namen)}")

            elif befehl == "nimm":
                if ziel == "":
                    print("Nimm was?")
                elif ziel not in vorfeld:
                    print(f"{ANZEIGENAMEN.get(ziel, ziel)} liegt hier nicht.")
                elif len(inventar) >= 10:
                    print("Das Inventar ist voll.")
                else:
                    vorfeld.remove(ziel)
                    inventar.append(ziel)
                    print(f"{ANZEIGENAMEN.get(ziel, ziel)} aufgenommen.")

            elif befehl == "ablege":
                if ziel == "":
                    print("Ablegen was?")
                elif ziel not in inventar:
                    print(f"Du traegst kein {ANZEIGENAMEN.get(ziel, ziel)}.")
                else:
                    inventar.remove(ziel)
                    vorfeld.append(ziel)
                    print(f"{ANZEIGENAMEN.get(ziel, ziel)} abgelegt.")

            elif befehl == "umsehen":
                sektor = sektoren[aktueller_sektor]
                print(sektor["beschreibung"])
                if "integritaet" in sektor:
                    print(f"Zustand der Wand: {sektor['integritaet']}%")
                else:
                    print(f"Anlagenzustand: {kern_integritaet}%")
                richtungen = []
                for richtung in sektor["nachbarn"]:
                    richtungen.append(richtung)
                print(f"Richtungen: {', '.join(richtungen)}")

            elif befehl == "gehe":
                sektor = sektoren[aktueller_sektor]
                if ziel == "":
                    print("Gehe wohin?")
                elif ziel not in sektor["nachbarn"]:
                    richtungen = []
                    for richtung in sektor["nachbarn"]:
                        richtungen.append(richtung)
                    print(f"Dort geht es nicht lang. Moeglich: {', '.join(richtungen)}")
                else:
                    aktueller_sektor = sektor["nachbarn"][ziel]
                    neuer_sektor = sektoren[aktueller_sektor]
                    print(neuer_sektor["beschreibung"])

            elif befehl == "depot":
                if aktueller_sektor != "depot":
                    print("Das Depot ist im Sektor 'depot'.")
                else:
                    for ware in WAREN:
                        print(f"{ANZEIGENAMEN.get(ware, ware)}: {WAREN[ware]} Vaporium")

            elif befehl == "kaufe":
                if aktueller_sektor != "depot":
                    print("Das Depot ist im Sektor 'depot'.")
                elif ziel == "":
                    print("Kaufe was?")
                elif ziel not in WAREN:
                    print(f"{ziel} gibt es hier nicht zu kaufen.")
                else:
                    menge = 1
                    if STAPELBAR.get(ziel, False):
                        if menge_text != "":
                            menge = int(menge_text)
                    gesamtpreis = WAREN[ziel] * menge
                    if menge <= 0:
                        print("Ungueltige Menge.")
                    elif gesamtpreis > vorrat["vaporium"]:
                        print("Das Vaporium reicht nicht.")
                    elif not STAPELBAR.get(ziel, False) and len(inventar) >= 10:
                        print("Das Inventar ist voll.")
                    else:
                        vorrat["vaporium"] -= gesamtpreis
                        if STAPELBAR.get(ziel, False):
                            vorrat[ziel] = vorrat.get(ziel, 0) + menge
                        else:
                            inventar.append(ziel)
                        print(f"{ANZEIGENAMEN.get(ziel, ziel)} gekauft. Vaporium uebrig: {vorrat['vaporium']}")

            elif befehl == "verkaufe":
                if aktueller_sektor != "depot":
                    print("Das Depot ist im Sektor 'depot'.")
                elif ziel == "":
                    print("Verkaufe was?")
                elif ziel not in VERKAUFSWERTE:
                    print(f"{ziel} kauft die Forschung nicht an.")
                else:
                    menge = 1
                    if menge_text != "":
                        menge = int(menge_text)
                    vorhanden = vorrat.get(ziel, 0)
                    if menge <= 0:
                        print("Ungueltige Menge.")
                    elif menge > vorhanden:
                        print(f"Du hast nicht so viel {ANZEIGENAMEN.get(ziel, ziel)}.")
                    else:
                        erloes = VERKAUFSWERTE[ziel] * menge
                        vorrat[ziel] -= menge
                        vorrat["vaporium"] += erloes
                        print(f"Verkauft fuer {erloes} Vaporium.")

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
                vorrat["chitinpanzer"] = vorrat.get("chitinpanzer", 0) + 1
                vorrat["organ"] = vorrat.get("organ", 0) + 1
                vorfeld.append("datenkern")
                print("Die Brut hat Material hinterlassen, und im Vorfeld liegt etwas.")
                break

n_marker = "N"
if aktueller_sektor == "nordtor":
    n_marker = "[N]"
o_marker = "O"
if aktueller_sektor == "osttor":
    o_marker = "[O]"
k_marker = "K"
if aktueller_sektor == "kern":
    k_marker = "[K]"
d_marker = "D"
if aktueller_sektor == "depot":
    d_marker = "[D]"
w_marker = "W"
if aktueller_sektor == "werkstatt":
    w_marker = "[W]"

grundriss = f"""
  {n_marker}---{k_marker}---{o_marker}
        |
       {d_marker}   {w_marker}
"""
print(grundriss)

print("Programmende.")
