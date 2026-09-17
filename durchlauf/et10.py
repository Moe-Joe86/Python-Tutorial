# Etappe 10: Komposition
# Namen: durchgehend deutsch, ohne Umlaute
# Design-Entscheidung "Wem gehoert ein Wert?": trefferpunkte, vorrat, inventar, sektor, erfahrung,
# level -> Marine (ein zweiter Marine haette jeweils einen eigenen). kern_integritaet bleibt
# draussen (die Anlage gibt es nur einmal). geladen/magazin_groesse/nachladen_noetig sind in
# Etappe 5/6 entstanden (nicht im Standard-Attributsatz von Etappe 9) - ein zweiter Marine haette
# aber offensichtlich sein eigenes Magazin, deshalb wandern sie konsequent mit in die Klasse.
# Inventar und Ausruestung sind jetzt eigene Klassen (Komposition), IN Marine.__init__ erzeugt,
# nicht davor und nicht als veraenderbarer Standardwert (Etappe 10, Konzept 6/7).
# Charakterisierungstest (befehle.txt/diff gegen et9.py) wurde durchgefuehrt, siehe BERICHT.md.

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


class Inventar:
    """Einzelne Gegenstaende bis zu einer festen Kapazitaet. Kennt seine eigene Obergrenze."""

    def __init__(self, plaetze):
        self.plaetze = plaetze
        self.gegenstaende = []

    def hinzufuegen(self, gegenstand):
        """Legt einen Gegenstand hinein. False, wenn kein Platz mehr ist."""
        if len(self.gegenstaende) >= self.plaetze:
            return False
        self.gegenstaende.append(gegenstand)
        return True

    def entfernen(self, gegenstand):
        """Entfernt einen Gegenstand. False, wenn er nicht da ist."""
        if gegenstand not in self.gegenstaende:
            return False
        self.gegenstaende.remove(gegenstand)
        return True

    def __repr__(self):
        return f"Inventar({len(self.gegenstaende)}/{self.plaetze}: {self.gegenstaende})"


class Ausruestung:
    """Feste Ausruestungsplaetze. Ein leerer Platz existiert und enthaelt None."""

    def __init__(self):
        self.plaetze = {"waffe": None, "panzerung": None, "modul": None}

    def anlegen(self, platz, teil):
        """Stellt ein Teil auf einen Platz. False, wenn der Platz schon besetzt ist."""
        if self.plaetze[platz] is not None:
            return False
        self.plaetze[platz] = teil
        return True

    def ablegen(self, platz):
        """Nimmt das Teil vom Platz und gibt es zurueck. None, wenn der Platz leer war.
        Der Platz bleibt bestehen (kein del) - er ist danach leer, nicht verschwunden."""
        teil = self.plaetze[platz]
        self.plaetze[platz] = None
        return teil

    def __repr__(self):
        return f"Ausruestung({self.plaetze})"


class Marine:
    """Der vom Spieler gesteuerte Marine: Ausruestung, Vorrat, Standort, Fortschritt."""

    def __init__(self, name, klasse, klassengeraet, trefferpunkte, panzerung, schaden, sektor,
                 vorrat, magazin_groesse, geladen):
        self.name = name
        self.klasse = klasse
        self.klassengeraet = klassengeraet
        self.trefferpunkte = trefferpunkte
        self.panzerung = panzerung
        self.schaden = schaden
        self.sektor = sektor
        self.vorrat = vorrat
        self.inventar = Inventar(10)
        self.ausruestung = Ausruestung()
        self.position = (0, 0)
        self.magazin_groesse = magazin_groesse
        self.geladen = geladen
        self.nachladen_noetig = False
        self.erfahrung = 0
        self.level = 1

    def __repr__(self):
        return (f"Marine(name={self.name!r}, klasse={self.klasse!r}, "
                f"trefferpunkte={self.trefferpunkte}, sektor={self.sektor!r}, level={self.level}, "
                f"position={self.position}, inventar={self.inventar!r})")

    def zeige_status(self, kern_integritaet, freigeschaltet=None, ausfuehrlich=False):
        """Gibt den Statusblock aus: drei Balken, Munition im Vorrat, Vaporium, Erfahrung und Stufe."""
        zeichne_balken(kern_integritaet, 100, "Kern")
        zeichne_balken(self.trefferpunkte, 100, "Marine")
        zeichne_balken(self.geladen, self.magazin_groesse, "Magazin")
        print(f"Munition im Vorrat: {self.vorrat['munition']}")
        print(f"Vaporium: {self.vorrat['vaporium']}")
        print(f"Erfahrung: {self.erfahrung} (Stufe {self.level})")

        if ausfuehrlich:
            if freigeschaltet is None or len(freigeschaltet) == 0:
                print("Freigeschaltete Ausbauten: keine")
            else:
                print(f"Freigeschaltete Ausbauten: {', '.join(freigeschaltet)}")

    def berechne_schaden(self):
        """Gibt den Schadenswert zurueck. Hat noch keinen Verbraucher (siehe Etappe 3c/11)."""
        ergebnis = self.schaden
        assert ergebnis >= 0
        return ergebnis

    def berechne_stufe(self):
        """Ermittelt aus self.erfahrung die aktuelle Stufe und schreibt sie in self.level."""
        stufe = 1
        for schwelle in STUFENTABELLE:
            if self.erfahrung >= schwelle:
                if STUFENTABELLE[schwelle] > stufe:
                    stufe = STUFENTABELLE[schwelle]
        self.level = stufe

    def kaufe(self, ziel, menge_text):
        """Kauft eine Ware aus WAREN. Meldet den Ausgang, veraendert vorrat/inventar direkt."""
        if self.sektor != "depot":
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
        if gesamtpreis > self.vorrat["vaporium"]:
            print("Das Vaporium reicht nicht.")
            return

        if ziel in STAPELBAR:
            self.vorrat["vaporium"] -= gesamtpreis
            self.vorrat[ziel] = self.vorrat.get(ziel, 0) + menge
            print(f"{ANZEIGENAMEN.get(ziel, ziel)} gekauft. Vaporium uebrig: {self.vorrat['vaporium']}")
        else:
            if not self.inventar.hinzufuegen(ziel):
                print("Das Inventar ist voll.")
                return
            self.vorrat["vaporium"] -= gesamtpreis
            print(f"{ANZEIGENAMEN.get(ziel, ziel)} gekauft. Vaporium uebrig: {self.vorrat['vaporium']}")

    def verkaufe(self, ziel, menge_text):
        """Verkauft Material aus VERKAUFSWERTE. Meldet den Ausgang, veraendert vorrat direkt."""
        if self.sektor != "depot":
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
        vorhanden = self.vorrat.get(ziel, 0)

        if menge <= 0:
            print("Ungueltige Menge.")
            return
        if menge > vorhanden:
            print(f"Du hast nicht so viel {ANZEIGENAMEN.get(ziel, ziel)}.")
            return

        erloes = VERKAUFSWERTE[ziel] * menge
        self.vorrat[ziel] -= menge
        self.vorrat["vaporium"] += erloes
        print(f"Verkauft fuer {erloes} Vaporium.")

    def schalte_frei(self, kennung, freigeschaltet):
        """Schaltet einen Ausbau frei. Setzt bei Grossmagazin self.magazin_groesse neu."""
        if self.sektor != "depot":
            print("Ausbauten gibt es nur im Depot.")
            return
        if kennung == "":
            print("Schalte frei was?")
            return
        if kennung not in AUSBAUTEN:
            print(f"{kennung} gibt es nicht.")
            return
        if kennung in freigeschaltet:
            print(f"{kennung} ist bereits freigeschaltet.")
            return
        if AUSBAUTEN[kennung] > self.vorrat["vaporium"]:
            print("Das Vaporium reicht nicht.")
            return

        self.vorrat["vaporium"] -= AUSBAUTEN[kennung]
        freigeschaltet.add(kennung)
        if kennung == "grossmagazin":
            self.magazin_groesse = 60
        print(f"{kennung} freigeschaltet.")

    def wechsle_sektor(self, richtung, sektoren):
        """Setzt self.sektor, wenn die Richtung gueltig ist. Meldet in jedem Fall."""
        sektor = sektoren[self.sektor]
        if richtung == "":
            print("Gehe wohin?")
            return
        if richtung not in sektor["nachbarn"]:
            richtungen = []
            for r in sektor["nachbarn"]:
                richtungen.append(r)
            print(f"Dort geht es nicht lang. Moeglich: {', '.join(richtungen)}")
            return

        self.sektor = sektor["nachbarn"][richtung]
        print(sektoren[self.sektor]["beschreibung"])


class Gegner:
    """Ein Gegner mit Trefferpunkten, Schaden, Entfernung und Typ.
    Wird heute bewusst noch NICHT im Spiel eingesetzt - die zwei parallelen Listen
    aus Etappe 6 bleiben unangetastet (siehe Etappe 9, Konzept 8). Diese Klasse steht
    hier nur bereit, damit Etappe 11 sie neben Marine vergleichen kann."""

    def __init__(self, trefferpunkte, schaden, entfernung, typ):
        self.trefferpunkte = trefferpunkte
        self.schaden = schaden
        self.entfernung = entfernung
        self.typ = typ

    def __repr__(self):
        return (f"Gegner(trefferpunkte={self.trefferpunkte}, schaden={self.schaden}, "
                f"entfernung={self.entfernung}, typ={self.typ!r})")


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


# --- Befehlsverarbeitung ---

def verarbeite_befehl(eingabe, marine, kern_integritaet, gegner, gegner_typen, sektoren,
                       vorfeld, freigeschaltet, gesehene_gegnertypen):
    """
    Verarbeitet eine Eingabezeile. Veraendert marine/gegner/gegner_typen/vorfeld/freigeschaltet
    direkt (mutable). Gibt zurueck: rundenkosten, welle_beendet, eingabe_leer
    """
    teile = eingabe.strip().lower().split()

    if len(teile) == 0:
        print("Bitte gib etwas ein.")
        return False, False, True

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
        marine.zeige_status(kern_integritaet, freigeschaltet, ausfuehrlich)

    elif befehl == "feuern":
        schuesse = 1
        if "schnellfeuer" in freigeschaltet:
            schuesse = 2
        abgegeben = 0
        for i in range(schuesse):
            if marine.geladen > 0 and len(gegner) > 0:
                marine.geladen -= 1
                vorderste_position = max(gegner)
                stelle = gegner.index(vorderste_position)
                gefallener_typ = gegner_typen[stelle]
                del gegner[stelle]
                del gegner_typen[stelle]
                marine.berechne_schaden()  # bekommt nur einen Ort - Ausgabe bleibt unveraendert
                marine.erfahrung += 10
                marine.berechne_stufe()
                abgegeben += 1
                print(f"Treffer: {gefallener_typ}. Geladen: {marine.geladen}, Gegner uebrig: {len(gegner)}")
        if abgegeben == 0:
            print("Magazin leer oder kein Ziel mehr. Erst nachladen.")
        if marine.geladen == 0:
            marine.nachladen_noetig = True
        rundenkosten = True

    elif befehl == "nachladen":
        platz = marine.magazin_groesse - marine.geladen
        nachschub = marine.vorrat["munition"]
        verschoben = platz
        if nachschub < platz:
            verschoben = nachschub
        if verschoben == 0:
            print("Kein Nachschub im Vorrat. Erst im Depot kaufen.")
        else:
            marine.geladen += verschoben
            marine.vorrat["munition"] -= verschoben
            marine.nachladen_noetig = False
            print(f"Nachgeladen. Magazin: {marine.geladen}, Vorrat: {marine.vorrat['munition']}")
        rundenkosten = True

    elif befehl == "beenden":
        print("Welle wird abgebrochen.")
        welle_beendet = True

    elif befehl == "inventar":
        if len(marine.inventar.gegenstaende) == 0:
            print("Das Inventar ist leer.")
        else:
            namen = []
            for ding in marine.inventar.gegenstaende:
                namen.append(ANZEIGENAMEN.get(ding, ding))
            print(f"Inventar: {', '.join(namen)}")

    elif befehl == "nimm":
        if ziel == "":
            print("Nimm was?")
        elif ziel not in vorfeld:
            print(f"{ANZEIGENAMEN.get(ziel, ziel)} liegt hier nicht.")
        elif not marine.inventar.hinzufuegen(ziel):
            print("Das Inventar ist voll.")
        else:
            vorfeld.remove(ziel)
            print(f"{ANZEIGENAMEN.get(ziel, ziel)} aufgenommen.")

    elif befehl == "ablege":
        if ziel == "":
            print("Ablegen was?")
        elif ziel not in marine.inventar.gegenstaende:
            print(f"Du traegst kein {ANZEIGENAMEN.get(ziel, ziel)}.")
        else:
            marine.inventar.entfernen(ziel)
            vorfeld.append(ziel)
            print(f"{ANZEIGENAMEN.get(ziel, ziel)} abgelegt.")

    elif befehl == "umsehen":
        sektor = sektoren[marine.sektor]
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
        marine.wechsle_sektor(ziel, sektoren)

    elif befehl == "depot":
        if marine.sektor != "depot":
            print("Das Depot ist im Sektor 'depot'.")
        else:
            for ware in WAREN:
                print(f"{ANZEIGENAMEN.get(ware, ware)}: {WAREN[ware]} Vaporium")

    elif befehl == "kaufe":
        marine.kaufe(ziel, menge_text)

    elif befehl == "verkaufe":
        marine.verkaufe(ziel, menge_text)

    elif befehl == "ausbauten":
        if marine.sektor != "depot":
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
            marine.schalte_frei(menge_text, freigeschaltet)

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

    return rundenkosten, welle_beendet, False


# --- Hauptprogramm ---

zeichne_kopf()

name = input("Wie heisst du, Marine? ")
print(f"Willkommen, {name}.")

kern_integritaet = 100
trefferpunkte_anzeige = 100  # nur fuer die Briefing-Zeile vor der Klassenwahl, siehe BERICHT.md
rekruten_verfuegbar = 0
wellen_bis_evakuierung = 20

print(f"Kernintegritaet: {kern_integritaet}%")
print(f"Trefferpunkte: {trefferpunkte_anzeige}")
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
    start_trefferpunkte, start_schaden, start_panzerung, start_geraet = 100, 10, 5, "Sturmgewehr"
    klasse_gueltig = True
elif klasse == 2:
    start_trefferpunkte, start_schaden, start_panzerung, start_geraet = 140, 14, 10, "Schweres MG"
    klasse_gueltig = True
elif klasse == 3:
    start_trefferpunkte, start_schaden, start_panzerung, start_geraet = 90, 7, 4, "Multiwerkzeug"
    klasse_gueltig = True
elif klasse == 4:
    start_trefferpunkte, start_schaden, start_panzerung, start_geraet = 80, 6, 3, "Bio-Injektor"
    klasse_gueltig = True

if klasse_gueltig:
    marine = Marine(
        name=name,
        klasse=KLASSEN[klasse - 1],
        klassengeraet=start_geraet,
        trefferpunkte=start_trefferpunkte,
        panzerung=start_panzerung,
        schaden=start_schaden,
        sektor="nordtor",
        vorrat={"vaporium": 0, "munition": 40, "chitinpanzer": 0, "organ": 0},
        magazin_groesse=40,
        geladen=40,
    )
    print(f"Klasse:        {marine.klasse}")
    print(f"Trefferpunkte: {marine.trefferpunkte}")
    print(f"Schaden:       {marine.schaden}")
    print(f"Panzerung:     {marine.panzerung}")

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

gesehene_gegnertypen = set()
freigeschaltet = set()

runde = 1
spiel_laeuft = True

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

        rundenkosten, welle_beendet, eingabe_leer = verarbeite_befehl(
            eingabe, marine, kern_integritaet, gegner, gegner_typen, sektoren,
            vorfeld, freigeschaltet, gesehene_gegnertypen,
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
                    marine.trefferpunkte -= 2
                    print("Die Brut schlaegt zurueck.")

            zeichne_bahn(gegner, gegner_typen)

            if kern_integritaet <= 0:
                print("Die Kernintegritaet ist auf 0 gefallen. Der Vorposten ist verloren.")
                spiel_laeuft = False
                break

            if marine.trefferpunkte <= 0:
                print("Du bist gefallen. Der Lauf ist zu Ende.")
                spiel_laeuft = False
                break

            if len(gegner) == 0:
                print("Welle geschafft.")
                marine.vorrat["chitinpanzer"] = marine.vorrat.get("chitinpanzer", 0) + 1
                marine.vorrat["organ"] = marine.vorrat.get("organ", 0) + 1
                vorfeld.append("datenkern")
                print("Die Brut hat Material hinterlassen, und im Vorfeld liegt etwas.")
                break

zeichne_grundriss(marine.sektor)
print("Programmende.")
