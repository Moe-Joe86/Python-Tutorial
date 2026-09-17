# Etappe 12: Der Tick (12a Welt als Objekt, 12b Zeit vergeht auch ohne Eingabe)
#
# 12a: Aller loser Zustand (kern_integritaet, sektoren, gegner, trupp, zeit/runde,
# laeuft) zieht in eine neue Klasse Welt. trefferpunkte/vorrat/erfahrung/inventar/
# sektor bleiben beim Marine, wie in Etappe 9 entschieden - siehe GELERNT.md,
# Auftragsschritt 2 (Antwort aus Etappe 9 wurde geprueft, hat getragen).
# Design-Entscheidung "eine Liste oder zwei": zwei Listen (welt.trupp, welt.gegner),
# wie vom Plan vorgegeben - Begruendung in GELERNT.md.
#
# 12b: Welt.tick() in vier Phasen (Zeit, Trupp, Gegner, Aufraeumen). Jede Einheit
# bekommt update(self, welt). Marine.update() ist fuer den gesteuerten Marine ein
# sofortiges return - er wartet auf input(). Die drei Kameraden feuern autonom auf
# welt.naechster_gegner(), wenn er in REICHWEITE ist.
#
# WICHTIG zur eigenen Entfernungs-Konvention (siehe Etappe 11, Kopfkommentar):
# entfernung waechst bei mir von 0 (Spawn) auf FELDER (Tor) - eine STEIGENDE Zahl,
# nicht die im Guide beschriebene sinkende. "naechster_gegner" (die groesste Bedrohung)
# ist deshalb bei mir der Gegner mit der GROESSTEN entfernung, nicht der kleinsten -
# konsistent mit "vorderster" aus der feuern-Logik seit Etappe 11.
#
# Charakterisierungstest fuer 12a (diff gegen et11.py, PYTHONHASHSEED fixiert) und
# manuelle Pruefung fuer 12b. Siehe BERICHT.md.

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
REICHWEITE = 5


# --- 11c: Item-Hierarchie ---

class Item:
    """Ein Einzelstueck. kennung ist, womit verglichen wird; name, was angezeigt wird."""

    def __init__(self, kennung, name):
        self.kennung = kennung
        self.name = name

    def __repr__(self):
        return f"{type(self).__name__}(kennung={self.kennung!r}, name={self.name!r})"


class Waffe(Item):
    def __init__(self, kennung, name, schaden, munitionsart):
        super().__init__(kennung, name)
        self.schaden = schaden
        self.munitionsart = munitionsart

    def __repr__(self):
        return (f"{type(self).__name__}(kennung={self.kennung!r}, name={self.name!r}, "
                f"schaden={self.schaden}, munitionsart={self.munitionsart!r})")


class Panzerung(Item):
    def __init__(self, kennung, name, schutzwert):
        super().__init__(kennung, name)
        self.schutzwert = schutzwert

    def __repr__(self):
        return (f"{type(self).__name__}(kennung={self.kennung!r}, name={self.name!r}, "
                f"schutzwert={self.schutzwert})")


class Modul(Item):
    def __init__(self, kennung, name, wirkt_auf):
        super().__init__(kennung, name)
        self.wirkt_auf = wirkt_auf

    def __repr__(self):
        return (f"{type(self).__name__}(kennung={self.kennung!r}, name={self.name!r}, "
                f"wirkt_auf={self.wirkt_auf!r})")


class Verbrauchsgut(Item):
    def __init__(self, kennung, name, anwendungen):
        super().__init__(kennung, name)
        self.anwendungen = anwendungen

    def __repr__(self):
        return (f"{type(self).__name__}(kennung={self.kennung!r}, name={self.name!r}, "
                f"anwendungen={self.anwendungen})")


def erzeuge_item(kennung):
    """Baut aus einer Kennung das passende Item-Objekt. Kein Katalog-Werkzeug, nur ein Schalter
    zwischen den vier Unterklassen - die Waren-/Preisdaten bleiben in WAREN/ANZEIGENAMEN."""
    name = ANZEIGENAMEN.get(kennung, kennung)
    if kennung == "medkit":
        return Verbrauchsgut(kennung, name, anwendungen=1)
    if kennung == "panzerplatte":
        return Panzerung(kennung, name, schutzwert=10)
    return Item(kennung, name)


class Inventar:
    """Einzelne Item-Objekte bis zu einer festen Kapazitaet. Kennt seine eigene Obergrenze."""

    def __init__(self, plaetze):
        self.plaetze = plaetze
        self.gegenstaende = []

    def hinzufuegen(self, item):
        """Legt ein Item hinein. False, wenn kein Platz mehr ist."""
        if len(self.gegenstaende) >= self.plaetze:
            return False
        self.gegenstaende.append(item)
        return True

    def enthaelt(self, kennung):
        """Prueft per Kennung, nicht per Objekt - der Spieler tippt einen String, kein Item."""
        for item in self.gegenstaende:
            if item.kennung == kennung:
                return True
        return False

    def entfernen(self, kennung):
        """Entfernt das erste Item mit dieser Kennung. False, wenn keines da ist."""
        for item in self.gegenstaende:
            if item.kennung == kennung:
                self.gegenstaende.remove(item)
                return True
        return False

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


# --- 11b/12b: Einheit als gemeinsame Basis von Marine und Gegner ---

class Einheit:
    """Alles, was Trefferpunkte hat, Schaden austeilen kann und im Tick handelt."""

    def __init__(self, name, trefferpunkte, schaden):
        self.name = name
        self.trefferpunkte = trefferpunkte
        self.schaden = schaden
        self.status = "aktiv"
        self.abschuesse = 0

    def nimm_schaden(self, menge):
        """Zieht Trefferpunkte ab, auf 0 festgenagelt. Setzt status auf 'tot' bei 0.
        Gibt zurueck, ob die Einheit noch lebt."""
        self.trefferpunkte -= menge
        if self.trefferpunkte <= 0:
            self.trefferpunkte = 0
            self.status = "tot"
        return self.trefferpunkte > 0

    def update(self, welt):
        """Eine Einheit ohne eigenes Verhalten tut in einem Tick nichts."""

    def __repr__(self):
        return (f"{type(self).__name__}(name={self.name!r}, trefferpunkte={self.trefferpunkte}, "
                f"status={self.status!r})")


class Gegner(Einheit):
    """Ein Gegner der Brut. typ aus Etappe 6 ist jetzt der name aus Einheit (Entscheidung
    Auftragsschritt 9, Etappe 11: zwei Attribute fuer dieselbe Sache waeren zwei Wahrheiten)."""

    def __init__(self, name, trefferpunkte, schaden, entfernung):
        super().__init__(name, trefferpunkte, schaden)
        self.entfernung = entfernung

    def update(self, welt):
        """Tot? Nichts tun. Noch nicht am Tor? Naeherkommen. Am Tor? Den Kern treffen."""
        if self.status == "tot":
            return
        if self.entfernung < FELDER:
            self.entfernung += 1
            return
        welt.kern_integritaet -= self.schaden

    def __repr__(self):
        return (f"Gegner(name={self.name!r}, trefferpunkte={self.trefferpunkte}, "
                f"entfernung={self.entfernung}, status={self.status!r})")


class Marine(Einheit):
    """Basis fuer alle vier Klassen: Ausruestung, Vorrat, Standort, Fortschritt."""

    def __init__(self, name, trefferpunkte, schaden, panzerung, klassengeraet, sektor, vorrat,
                 magazin_groesse, geladen, gesteuert=False):
        super().__init__(name, trefferpunkte, schaden)
        self.panzerung = panzerung
        self.klassengeraet = klassengeraet
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
        self.gesteuert = gesteuert

    def __repr__(self):
        return (f"{type(self).__name__}(name={self.name!r}, "
                f"trefferpunkte={self.trefferpunkte}, sektor={self.sektor!r}, level={self.level}, "
                f"position={self.position}, inventar={self.inventar!r})")

    def faehigkeit_einsetzen(self):
        """Basisfassung: eine Klasse ohne eigene Faehigkeit hat keine. Jede Unterklasse
        ueberschreibt das."""
        print(f"{self.name} hat keine einsetzbare Faehigkeit.")

    def update(self, welt):
        """Der gesteuerte Marine wartet auf input() und tut im Tick nichts. Die drei
        Kameraden feuern autonom auf das naechste Ziel, wenn es in Reichweite ist.
        Kein Munitionsverbrauch heute - offener Posten, siehe GELERNT.md."""
        if self.gesteuert:
            return
        if self.status == "tot":
            return
        ziel = welt.naechster_gegner()
        if ziel is None:
            return
        if self._abstand(ziel) <= REICHWEITE:
            ueberlebt = ziel.nimm_schaden(self.schaden)
            if not ueberlebt:
                self.abschuesse += 1
            print(f"{self.name} feuert automatisch auf {ziel.name}.")

    def _abstand(self, ziel):
        """Wie weit das Ziel noch vom Tor entfernt ist - siehe Kopfkommentar zur
        eigenen (steigenden) entfernung-Konvention."""
        return FELDER - ziel.entfernung

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
            if not self.inventar.hinzufuegen(erzeuge_item(ziel)):
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


class Soldat(Marine):
    def __init__(self, name, sektor, vorrat, gesteuert=False):
        super().__init__(name, trefferpunkte=100, schaden=10, panzerung=5,
                          klassengeraet="Sturmgewehr", sektor=sektor, vorrat=vorrat,
                          magazin_groesse=40, geladen=40, gesteuert=gesteuert)

    def faehigkeit_einsetzen(self):
        print(f"{self.name} feuert einen Unterlauf-Granatwerfer ab. (Fläche, noch ohne Wirkung.)")


class Heavy(Marine):
    def __init__(self, name, sektor, vorrat, gesteuert=False):
        super().__init__(name, trefferpunkte=140, schaden=14, panzerung=10,
                          klassengeraet="Schweres MG", sektor=sektor, vorrat=vorrat,
                          magazin_groesse=40, geladen=40, gesteuert=gesteuert)

    def faehigkeit_einsetzen(self):
        print(f"{self.name} setzt Durchschlag ein. (Trifft mehrere Ziele in einer Reihe, noch ohne Wirkung.)")


class Engineer(Marine):
    def __init__(self, name, sektor, vorrat, gesteuert=False):
        super().__init__(name, trefferpunkte=90, schaden=7, panzerung=4,
                          klassengeraet="Multiwerkzeug", sektor=sektor, vorrat=vorrat,
                          magazin_groesse=40, geladen=40, gesteuert=gesteuert)

    def faehigkeit_einsetzen(self):
        print(f"{self.name} beginnt den Bau eines Geschuetzturms. (Noch ohne Wirkung.)")


class Medic(Marine):
    def __init__(self, name, sektor, vorrat, gesteuert=False):
        super().__init__(name, trefferpunkte=80, schaden=6, panzerung=3,
                          klassengeraet="Bio-Injektor", sektor=sektor, vorrat=vorrat,
                          magazin_groesse=40, geladen=40, gesteuert=gesteuert)

    def faehigkeit_einsetzen(self):
        print(f"{self.name} setzt den Bio-Injektor ein. (Heilung, noch ohne Wirkung.)")


# --- 12a: Die Welt ---

class Welt:
    """Alles, was es pro Spiel genau einmal gibt. Der uebergebene Marine steht
    zusaetzlich unter .held - ein Objekt, zwei Namen (Konzept 4)."""

    def __init__(self, held, sektoren):
        self.zeit = 0
        self.welle = 1
        self.kern_integritaet = 100
        self.sektoren = sektoren
        self.gegner = []
        self.trupp = [held]
        self.held = held
        self.laeuft = True

    def __repr__(self):
        return (f"Welt(zeit={self.zeit}, welle={self.welle}, "
                f"kern_integritaet={self.kern_integritaet}, gegner={len(self.gegner)})")

    def naechster_gegner(self):
        """Der aktive Gegner, der dem Tor am naechsten ist (siehe Kopfkommentar zur
        eigenen, steigenden entfernung-Konvention: das ist die GROESSTE entfernung,
        nicht die kleinste). None, wenn keiner mehr aktiv ist."""
        naechster = None
        for g in self.gegner:
            if g.status == "tot":
                continue
            if naechster is None:
                naechster = g
            elif g.entfernung > naechster.entfernung:
                naechster = g
        return naechster

    def raeume_auf(self):
        """Entfernt alle toten Gegner aus welt.gegner. Sammeln, dann entfernen (Konzept 11) -
        nicht in derselben Schleife, sonst wird jeder zweite uebersprungen."""
        gefallene = []
        for g in self.gegner:
            if g.status == "tot":
                gefallene.append(g)
        for g in gefallene:
            self.gegner.remove(g)
        return len(gefallene)

    def tick(self):
        """Vier Phasen: Zeit, Trupp, Gegner, Aufraeumen. Reihenfolge Trupp-vor-Gegner
        heisst: Ein Gegner, den der Trupp in Phase 2 toetet, schlaegt in Phase 3
        desselben Ticks nicht mehr zu - siehe GELERNT.md."""
        self.zeit += 1
        for kamerad in self.trupp:
            kamerad.update(self)
        for gegner in self.gegner:
            gegner.update(self)
        self.raeume_auf()


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


def zeichne_bahn(gegner):
    """Zeichnet die Anmarschbahn aus den Gegner-Objekten. Veraendert die Liste nicht."""
    bahn_felder = ["."] * FELDER
    for g in gegner:
        if 0 <= g.entfernung < FELDER:
            bahn_felder[g.entfernung] = TYP_ZEICHEN[g.name]
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

def verarbeite_befehl(eingabe, welt, freigeschaltet, gesehene_gegnertypen):
    """
    Verarbeitet eine Eingabezeile fuer den gesteuerten Marine. Veraendert welt/freigeschaltet
    direkt (mutable). Gibt zurueck: tick_noetig, welle_beendet, eingabe_leer
    """
    marine = welt.held
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

    tick_noetig = False
    welle_beendet = False

    if befehl == "status":
        ausfuehrlich = ziel == "ausfuehrlich"
        marine.zeige_status(welt.kern_integritaet, freigeschaltet, ausfuehrlich)
        print("Trupp:")
        for kamerad in welt.trupp:
            markierung = " (du)" if kamerad.gesteuert else ""
            print(f"  {kamerad.name} - {type(kamerad).__name__} - {kamerad.trefferpunkte} TP"
                  f" - {kamerad.abschuesse} Abschuesse{markierung}")

    elif befehl == "feuern":
        schuesse = 1
        if "schnellfeuer" in freigeschaltet:
            schuesse = 2
        abgegeben = 0
        for i in range(schuesse):
            if marine.geladen > 0 and len(welt.gegner) > 0:
                marine.geladen -= 1
                vorderster = welt.naechster_gegner()
                if vorderster is not None:
                    welt.gegner.remove(vorderster)
                    marine.berechne_schaden()  # bekommt nur einen Ort - Ausgabe bleibt unveraendert
                    marine.erfahrung += 10
                    marine.berechne_stufe()
                    marine.abschuesse += 1
                    abgegeben += 1
                    print(f"Treffer: {vorderster.name}. Geladen: {marine.geladen}, "
                          f"Gegner uebrig: {len(welt.gegner)}")
        if abgegeben == 0:
            print("Magazin leer oder kein Ziel mehr. Erst nachladen.")
        if marine.geladen == 0:
            marine.nachladen_noetig = True
        tick_noetig = True

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
        tick_noetig = True

    elif befehl == "beenden":
        print("Welle wird abgebrochen.")
        welle_beendet = True

    elif befehl == "faehigkeit":
        marine.faehigkeit_einsetzen()

    elif befehl == "inventar":
        if len(marine.inventar.gegenstaende) == 0:
            print("Das Inventar ist leer.")
        else:
            namen = []
            for item in marine.inventar.gegenstaende:
                namen.append(item.name)
            print(f"Inventar: {', '.join(namen)}")

    elif befehl == "nimm":
        if ziel == "":
            print("Nimm was?")
        elif ziel not in welt.vorfeld:
            print(f"{ANZEIGENAMEN.get(ziel, ziel)} liegt hier nicht.")
        elif not marine.inventar.hinzufuegen(erzeuge_item(ziel)):
            print("Das Inventar ist voll.")
        else:
            welt.vorfeld.remove(ziel)
            print(f"{ANZEIGENAMEN.get(ziel, ziel)} aufgenommen.")

    elif befehl == "ablege":
        if ziel == "":
            print("Ablegen was?")
        elif not marine.inventar.enthaelt(ziel):
            print(f"Du traegst kein {ANZEIGENAMEN.get(ziel, ziel)}.")
        else:
            marine.inventar.entfernen(ziel)
            welt.vorfeld.append(ziel)
            print(f"{ANZEIGENAMEN.get(ziel, ziel)} abgelegt.")

    elif befehl == "umsehen":
        sektor = welt.sektoren[marine.sektor]
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
        marine.wechsle_sektor(ziel, welt.sektoren)

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
        # Eigene Entscheidung (siehe GELERNT.md): eine ungueltige Eingabe kostet
        # keinen Tick - Tippfehler werden nicht bestraft, "Unbekannter Befehl" ist
        # reine Auskunft ueber die Eingabe, keine gescheiterte Handlung.

    return tick_noetig, welle_beendet, False


# --- Hauptprogramm ---

zeichne_kopf()

name = input("Wie heisst du, Marine? ")
print(f"Willkommen, {name}.")

kern_integritaet_anzeige = 100  # nur fuer die Briefing-Zeile vor Welt/Klassenwahl, siehe GELERNT.md
trefferpunkte_anzeige = 100
rekruten_verfuegbar = 0
wellen_bis_evakuierung = 20

print(f"Kernintegritaet: {kern_integritaet_anzeige}%")
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

KLASSEN_NACH_ZAHL = {1: Soldat, 2: Heavy, 3: Engineer, 4: Medic}

klasse_gueltig = klasse in KLASSEN_NACH_ZAHL
welt = None
if not klasse_gueltig:
    print("Diese Klasse gibt es nicht.")
else:
    eigener_vorrat = {"vaporium": 0, "munition": 40, "chitinpanzer": 0, "organ": 0}
    GewaehlteKlasse = KLASSEN_NACH_ZAHL[klasse]
    marine = GewaehlteKlasse(name, "nordtor", eigener_vorrat, gesteuert=True)

    print(f"Klasse:        {type(marine).__name__}")
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

if klasse_gueltig:
    welt = Welt(marine, sektoren)

    # Die drei Kameraden: die anderen Klassen kommen automatisch dazu, mit eigenem Vorrat.
    for zahl, Klassenbauplan in KLASSEN_NACH_ZAHL.items():
        if Klassenbauplan is not GewaehlteKlasse:
            kamerad_name = f"Rekrut {Klassenbauplan.__name__}"
            kamerad_vorrat = {"vaporium": 0, "munition": 40, "chitinpanzer": 0, "organ": 0}
            welt.trupp.append(Klassenbauplan(kamerad_name, "nordtor", kamerad_vorrat, gesteuert=False))

    gesehene_gegnertypen = set()
    freigeschaltet = set()
    welt.vorfeld = []

    for welle in range(1, wellen_bis_evakuierung + 1):
        if not welt.laeuft:
            break

        welt.welle = welle
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

        welt.gegner = []
        for i in range(welle):
            if welle <= 3:
                gegner_typ = "kriecher"
            elif welle <= 7:
                if i == 0:
                    gegner_typ = "speier"
                else:
                    gegner_typ = "kriecher"
            else:
                if i == 0:
                    gegner_typ = "panzerbrut"
                elif i == 1:
                    gegner_typ = "speier"
                else:
                    gegner_typ = "kriecher"
            welt.gegner.append(Gegner(gegner_typ, trefferpunkte=20, schaden=5, entfernung=0))

        while True:
            eingabe = input(f"Welle {welle}, Runde {welt.zeit} > ")

            tick_noetig, welle_beendet, eingabe_leer = verarbeite_befehl(
                eingabe, welt, freigeschaltet, gesehene_gegnertypen,
            )

            if welle_beendet:
                break

            if not eingabe_leer:
                if tick_noetig:
                    welt.tick()
                    if len(welt.gegner) > 0:
                        print("Die Brut schlaegt zurueck.")

                zeichne_bahn(welt.gegner)

                if welt.kern_integritaet <= 0:
                    print("Die Kernintegritaet ist auf 0 gefallen. Der Vorposten ist verloren.")
                    welt.laeuft = False
                    break

                if marine.trefferpunkte <= 0:
                    print("Du bist gefallen. Der Lauf ist zu Ende.")
                    welt.laeuft = False
                    break

                if len(welt.gegner) == 0:
                    print("Welle geschafft.")
                    marine.vorrat["chitinpanzer"] = marine.vorrat.get("chitinpanzer", 0) + 1
                    marine.vorrat["organ"] = marine.vorrat.get("organ", 0) + 1
                    welt.vorfeld.append("datenkern")
                    print("Die Brut hat Material hinterlassen, und im Vorfeld liegt etwas.")
                    break

    zeichne_grundriss(marine.sektor)

print("Programmende.")
