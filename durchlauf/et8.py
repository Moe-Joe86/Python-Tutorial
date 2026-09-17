# Etappe 8: Die Bug-Jagd I
# Etappe 8 fuehrt kein neues Spielfeature ein (Debugger, Fehlertagebuch, Bug-Jagd als Uebung).
# Der Code ist identisch zu et7.py - breakpoint()/###-Debugzeilen aus der Uebung sind vor dem
# Commit wieder entfernt, injizierte Testfehler zurueckgebaut. Siehe durchlauf/FEHLERTAGEBUCH.md
# und BERICHT.md fuer die tatsaechlich durchgefuehrte Bug-Jagd.
# Namen: durchgehend deutsch, ohne Umlaute
# Design-Entscheidung "Wie kommt Zustand in Funktionen": alles als Parameter, kein global (siehe GELERNT.md)
# GROSS geschriebene Konstanten (WAREN, AUSBAUTEN, GEGNERTYPEN, ...) werden NICHT als Parameter durchgereicht -
# sie aendern sich zur Laufzeit nie, anders als vorrat/inventar/sektoren usw. (eigene Interpretation, siehe BERICHT.md)
# Beweis (befehle.txt -> vorher.txt/nachher.txt, diff) wurde separat gefuehrt, siehe BERICHT.md

KLASSEN = ("soldat", "heavy", "engineer", "medic")

WAREN = {"medkit": 40, "munition": 15, "panzerplatte": 90}
STAPELBAR = {"munition"}
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
AUSBAUTEN = {"zielhilfe": 60, "grossmagazin": 80, "schnellfeuer": 120}
GEGNERTYPEN = {
    "kriecher": {
        "lang": "Ein Kriecher huscht auf vier Gliedmassen ueber den Fels, den Kopf tief gehalten. Er greift an, sobald er in Reichweite ist, und weicht sonst nichts aus.",
        "kurz": "Ein Kriecher.",
    },
    "speier": {
        "lang": "Ein Speier bleibt auf Distanz und spuckt Aetzsaeure in kurzen Stoessen. Sein Panzer ist duenner als der eines Kriechers.",
        "kurz": "Ein Speier.",
    },
    "panzerbrut": {
        "lang": "Panzerbrut bewegt sich langsam, gedeckt von dicken Chitinplatten. Was sie an Tempo verliert, macht sie an Zaehigkeit wett.",
        "kurz": "Panzerbrut.",
    },
}
TYP_ZEICHEN = {"kriecher": "k", "speier": "S", "panzerbrut": "P"}
STUFENTABELLE = {0: 1, 100: 2, 300: 3, 600: 4, 1000: 5}
FELDER = 10


# --- Zeichenfunktionen (7b): bekommen fertige Werte, rechnen nichts, entscheiden nichts ---

def zeichne_kopf():
    """Gibt den festen ASCII-Kopf aus. Braucht nichts, rechnet nichts."""
    kopf = """
  /------------\\
 |  VORPOSTEN   |
 ----------------
"""
    print(kopf)


def zeichne_balken(wert, maximum, beschriftung):
    """Zeichnet einen Balken der Breite 10 fuer wert/maximum. Gibt nichts zurueck, nur Ausgabe."""
    anteil = wert / maximum
    voll = int(anteil * 10)
    leer = 10 - voll
    balken = "#" * voll + "." * leer
    print(f"{beschriftung:<8} [{balken}] {anteil:.0%}")


def zeichne_bahn(gegner, gegner_typen):
    """Zeichnet die Anmarschbahn aus den Positionen und Typen. Veraendert keine der beiden Listen."""
    bahn_felder = ["."] * FELDER
    for i in range(len(gegner)):
        pos = gegner[i]
        if 0 <= pos < FELDER:
            bahn_felder[pos] = TYP_ZEICHEN[gegner_typen[i]]
    bahn = "S" + "".join(bahn_felder) + "@"
    print(bahn)


def zeichne_grundriss(aktueller_sektor):
    """Zeichnet den statischen Grundriss, mit dem aktuellen Sektor markiert."""
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


def zeige_status(kern_integritaet, trefferpunkte, geladen, magazin_groesse, vorrat, erfahrung,
                  freigeschaltet=None, ausfuehrlich=False):
    """Gibt den Statusblock aus: drei Balken, Munition im Vorrat, Vaporium, Erfahrung und Stufe.
    Bei ausfuehrlich=True zusaetzlich die freigeschalteten Ausbauten."""
    zeichne_balken(kern_integritaet, 100, "Kern")
    zeichne_balken(trefferpunkte, 100, "Marine")
    zeichne_balken(geladen, magazin_groesse, "Magazin")
    print(f"Munition im Vorrat: {vorrat['munition']}")
    print(f"Vaporium: {vorrat['vaporium']}")

    stufe = 1
    for schwelle in STUFENTABELLE:
        if erfahrung >= schwelle:
            if STUFENTABELLE[schwelle] > stufe:
                stufe = STUFENTABELLE[schwelle]
    print(f"Erfahrung: {erfahrung} (Stufe {stufe})")

    if ausfuehrlich:
        if freigeschaltet is None or len(freigeschaltet) == 0:
            print("Freigeschaltete Ausbauten: keine")
        else:
            print(f"Freigeschaltete Ausbauten: {', '.join(freigeschaltet)}")


# --- Logikfunktionen (7a/7b): rechnen und entscheiden, geben zurueck statt auszugeben ---

def berechne_schaden(schaden_klasse):
    """Gibt den Schadenswert der Klasse zurueck. Hat noch keinen Verbraucher (siehe Etappe 3c/11)."""
    ergebnis = schaden_klasse
    assert ergebnis >= 0
    return ergebnis


def kaufe(ziel, menge_text, aktueller_sektor, vorrat, inventar):
    """Kauft eine Ware aus WAREN. Meldet den Ausgang, veraendert vorrat/inventar direkt."""
    if aktueller_sektor != "depot":
        print("Das Depot ist im Sektor 'depot'.")
        return
    if ziel == "":
        print("Kaufe was?")
        return
    if ziel not in WAREN:
        print(f"{ziel} gibt es hier nicht zu kaufen.")
        return

    menge = 1
    if ziel in STAPELBAR and menge_text != "":
        menge = int(menge_text)
    gesamtpreis = WAREN[ziel] * menge

    if menge <= 0:
        print("Ungueltige Menge.")
        return
    if gesamtpreis > vorrat["vaporium"]:
        print("Das Vaporium reicht nicht.")
        return
    if ziel not in STAPELBAR and len(inventar) >= 10:
        print("Das Inventar ist voll.")
        return

    vorrat["vaporium"] -= gesamtpreis
    if ziel in STAPELBAR:
        vorrat[ziel] = vorrat.get(ziel, 0) + menge
    else:
        inventar.append(ziel)
    print(f"{ANZEIGENAMEN.get(ziel, ziel)} gekauft. Vaporium uebrig: {vorrat['vaporium']}")


def verkaufe(ziel, menge_text, aktueller_sektor, vorrat):
    """Verkauft Material aus VERKAUFSWERTE. Meldet den Ausgang, veraendert vorrat direkt."""
    if aktueller_sektor != "depot":
        print("Das Depot ist im Sektor 'depot'.")
        return
    if ziel == "":
        print("Verkaufe was?")
        return
    if ziel not in VERKAUFSWERTE:
        print(f"{ziel} kauft die Forschung nicht an.")
        return

    menge = 1
    if menge_text != "":
        menge = int(menge_text)
    vorhanden = vorrat.get(ziel, 0)

    if menge <= 0:
        print("Ungueltige Menge.")
        return
    if menge > vorhanden:
        print(f"Du hast nicht so viel {ANZEIGENAMEN.get(ziel, ziel)}.")
        return

    erloes = VERKAUFSWERTE[ziel] * menge
    vorrat[ziel] -= menge
    vorrat["vaporium"] += erloes
    print(f"Verkauft fuer {erloes} Vaporium.")


def schalte_frei(kennung, aktueller_sektor, vorrat, freigeschaltet, magazin_groesse):
    """Schaltet einen Ausbau frei. Gibt magazin_groesse zurueck (unveraendert oder neu bei Grossmagazin)."""
    if aktueller_sektor != "depot":
        print("Ausbauten gibt es nur im Depot.")
        return magazin_groesse
    if kennung == "":
        print("Schalte frei was?")
        return magazin_groesse
    if kennung not in AUSBAUTEN:
        print(f"{kennung} gibt es nicht.")
        return magazin_groesse
    if kennung in freigeschaltet:
        print(f"{kennung} ist bereits freigeschaltet.")
        return magazin_groesse
    if AUSBAUTEN[kennung] > vorrat["vaporium"]:
        print("Das Vaporium reicht nicht.")
        return magazin_groesse

    vorrat["vaporium"] -= AUSBAUTEN[kennung]
    freigeschaltet.add(kennung)
    if kennung == "grossmagazin":
        magazin_groesse = 60
    print(f"{kennung} freigeschaltet.")
    return magazin_groesse


def wechsle_sektor(richtung, aktueller_sektor, sektoren):
    """Gibt den neuen Sektornamen zurueck. Setzt aktueller_sektor NICHT selbst."""
    sektor = sektoren[aktueller_sektor]
    if richtung == "":
        print("Gehe wohin?")
        return aktueller_sektor
    if richtung not in sektor["nachbarn"]:
        richtungen = []
        for r in sektor["nachbarn"]:
            richtungen.append(r)
        print(f"Dort geht es nicht lang. Moeglich: {', '.join(richtungen)}")
        return aktueller_sektor

    neuer_sektor = sektor["nachbarn"][richtung]
    print(sektoren[neuer_sektor]["beschreibung"])
    return neuer_sektor


def verarbeite_befehl(eingabe, aktueller_sektor, geladen, magazin_groesse, nachladen_noetig, erfahrung,
                       kern_integritaet, trefferpunkte, gegner, gegner_typen, sektoren, vorrat, inventar,
                       vorfeld, freigeschaltet, gesehene_gegnertypen, schaden_klasse):
    """
    Verarbeitet eine Eingabezeile. Veraendert gegner/gegner_typen/vorrat/inventar/vorfeld/freigeschaltet
    direkt (mutable). Gibt zurueck, in dieser Reihenfolge:
    aktueller_sektor, geladen, magazin_groesse, nachladen_noetig, erfahrung, rundenkosten, welle_beendet, eingabe_leer
    """
    teile = eingabe.strip().lower().split()

    if len(teile) == 0:
        print("Bitte gib etwas ein.")
        return aktueller_sektor, geladen, magazin_groesse, nachladen_noetig, erfahrung, False, False, True

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
        ausfuehrlich = ziel == "ausfuehrlich"
        zeige_status(kern_integritaet, trefferpunkte, geladen, magazin_groesse, vorrat, erfahrung,
                     freigeschaltet, ausfuehrlich)

    elif befehl == "feuern":
        schuesse = 1
        if "schnellfeuer" in freigeschaltet:
            schuesse = 2
        abgegeben = 0
        for i in range(schuesse):
            if geladen > 0 and len(gegner) > 0:
                geladen -= 1
                vorderste_position = max(gegner)
                stelle = gegner.index(vorderste_position)
                gefallener_typ = gegner_typen[stelle]
                del gegner[stelle]
                del gegner_typen[stelle]
                berechne_schaden(schaden_klasse)  # bekommt nur einen Ort - Ausgabe bleibt unveraendert (siehe BERICHT.md)
                erfahrung += 10
                abgegeben += 1
                print(f"Treffer: {gefallener_typ}. Geladen: {geladen}, Gegner uebrig: {len(gegner)}")
        if abgegeben == 0:
            print("Magazin leer oder kein Ziel mehr. Erst nachladen.")
        if geladen == 0:
            nachladen_noetig = True
        rundenkosten = True

    elif befehl == "nachladen":
        platz = magazin_groesse - geladen
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
            print("Anlagenzustand: siehe status")
        richtungen = []
        for richtung in sektor["nachbarn"]:
            richtungen.append(richtung)
        print(f"Richtungen: {', '.join(richtungen)}")

    elif befehl == "gehe":
        aktueller_sektor = wechsle_sektor(ziel, aktueller_sektor, sektoren)

    elif befehl == "depot":
        if aktueller_sektor != "depot":
            print("Das Depot ist im Sektor 'depot'.")
        else:
            for ware in WAREN:
                print(f"{ANZEIGENAMEN.get(ware, ware)}: {WAREN[ware]} Vaporium")

    elif befehl == "kaufe":
        kaufe(ziel, menge_text, aktueller_sektor, vorrat, inventar)

    elif befehl == "verkaufe":
        verkaufe(ziel, menge_text, aktueller_sektor, vorrat)

    elif befehl == "ausbauten":
        if aktueller_sektor != "depot":
            print("Ausbauten gibt es nur im Depot.")
        else:
            for ausbau in AUSBAUTEN:
                status_text = "noch nicht freigeschaltet"
                if ausbau in freigeschaltet:
                    status_text = "bereits freigeschaltet"
                print(f"{ausbau}: {AUSBAUTEN[ausbau]} Vaporium ({status_text})")

    elif befehl == "schalte":
        if ziel != "frei":
            print("Meintest du 'schalte frei <kennung>'?")
        else:
            magazin_groesse = schalte_frei(menge_text, aktueller_sektor, vorrat, freigeschaltet, magazin_groesse)

    elif befehl == "bestiarium":
        if ziel == "":
            if len(gesehene_gegnertypen) == 0:
                print("Noch keine Daten.")
            for typ in gesehene_gegnertypen:
                print(f"{typ}: {GEGNERTYPEN[typ]['kurz']}")
            print(f"{len(gesehene_gegnertypen)} von {len(GEGNERTYPEN)} Typen erfasst.")
        elif ziel not in GEGNERTYPEN:
            print("Diesen Typ gibt es nicht.")
        elif ziel not in gesehene_gegnertypen:
            print("Ueber diesen Typ liegen dir keine Daten vor.")
        else:
            print(GEGNERTYPEN[ziel]["lang"])

    else:
        print("Unbekannter Befehl.")

    return aktueller_sektor, geladen, magazin_groesse, nachladen_noetig, erfahrung, rundenkosten, welle_beendet, False


# --- Hauptprogramm ---

zeichne_kopf()

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
if klasse < 1 or klasse > len(KLASSEN):
    print("Diese Klasse gibt es nicht.")
elif klasse == 1:
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

if klasse_gueltig:
    print(f"Klasse:        {KLASSEN[klasse - 1]}")
    print(f"Trefferpunkte: {trefferpunkte}")
    print(f"Schaden:       {schaden}")
    print(f"Panzerung:     {panzerung}")

print("Auf dem Radar bewegt sich etwas, das dort nicht hingehoert.")
funk_antwort = input("Melden? (ja/nein) ").strip()
meldung_abgesetzt = funk_antwort == "ja"
print(f"Meldung abgesetzt: {meldung_abgesetzt}")

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
aktueller_sektor = "nordtor"

vorrat = {"vaporium": 0, "munition": 40, "chitinpanzer": 0, "organ": 0}
magazin_groesse = 40
geladen = magazin_groesse
nachladen_noetig = False

gesehene_gegnertypen = set()
freigeschaltet = set()

erfahrung = 0
runde = 1
spiel_laeuft = True

inventar = []
vorfeld = []

for welle in range(1, wellen_bis_evakuierung + 1):
    if not spiel_laeuft:
        break

    print(f"--- Welle {welle} von {wellen_bis_evakuierung} ---")

    if welle <= 3:
        wellen_typen = {"kriecher"}
    elif welle <= 7:
        wellen_typen = {"kriecher", "speier"}
    else:
        wellen_typen = {"kriecher", "speier", "panzerbrut"}

    for typ in wellen_typen:
        if typ not in gesehene_gegnertypen:
            print(GEGNERTYPEN[typ]["lang"])
        else:
            print(GEGNERTYPEN[typ]["kurz"])
    for typ in wellen_typen:
        gesehene_gegnertypen.add(typ)

    gegner = []
    gegner_typen = []
    for i in range(welle):
        gegner.append(0)
        if welle <= 3:
            gegner_typen.append("kriecher")
        elif welle <= 7:
            if i == 0:
                gegner_typen.append("speier")
            else:
                gegner_typen.append("kriecher")
        else:
            if i == 0:
                gegner_typen.append("panzerbrut")
            elif i == 1:
                gegner_typen.append("speier")
            else:
                gegner_typen.append("kriecher")

    while True:
        eingabe = input(f"Welle {welle}, Runde {runde} > ")

        (aktueller_sektor, geladen, magazin_groesse, nachladen_noetig, erfahrung,
         rundenkosten, welle_beendet, eingabe_leer) = verarbeite_befehl(
            eingabe, aktueller_sektor, geladen, magazin_groesse, nachladen_noetig, erfahrung,
            kern_integritaet, trefferpunkte, gegner, gegner_typen, sektoren, vorrat, inventar,
            vorfeld, freigeschaltet, gesehene_gegnertypen, schaden,
        )

        if welle_beendet:
            break

        if not eingabe_leer:
            if rundenkosten:
                runde += 1
                if len(gegner) > 0:
                    for i in range(len(gegner)):
                        gegner[i] += 1
                    kern_integritaet -= 5
                    trefferpunkte -= 2
                    print("Die Brut schlaegt zurueck.")

            zeichne_bahn(gegner, gegner_typen)

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

zeichne_grundriss(aktueller_sektor)
print("Programmende.")
