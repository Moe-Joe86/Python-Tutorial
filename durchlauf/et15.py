# Etappe 15: Was die Brut hinterlaesst (15a Fundstuecke/Erkenntnisse, 15b Wirkung)
#
# 15a: Gefallene Gegner hinterlassen an ihrer Koordinate ein Fundstueck (Item-Unterklasse,
# erbt NICHT von Einheit - tickt nicht). Einsammeln passiert in einer eigenen Phase NACH
# der letzten Aufraeumphase einer Welle, VOR der naechsten (Konzept 7) - nicht beim Fallen
# selbst, damit die Zonen aus 14b eine echte zweite Bedeutung bekommen (was liegt bleibt,
# bleibt liegen). welt.erkenntnisse ist ein Set (Konzept 2: ein Dictionary aus Booleans
# waere nur eine umstaendliche Schreibweise fuer "nicht dabei").
#
# Design-Entscheidung "Wo wohnt eine Erkenntnis?" (siehe GELERNT.md): zentral bei
# welt.erkenntnisse, nicht am Fundstueck und nicht in GEGNERTYPEN - genau die Trennung
# "was existiert" (GEGNERTYPEN) vs. "was ich kenne" (gesehene_gegnertypen), jetzt ein
# drittes Mal (erkenntnisse).
#
# Eigene Entscheidung: Fundstuecke werden beim Analysieren NICHT verbraucht (Andenken im
# Inventar, kostet nichts) - Prüfkette trotzdem in der vom Guide empfohlenen Reihenfolge
# (Erkenntnis-Check vor Besitz-Check), falls das je geaendert wird.
#
# 15b: Umkehrtabelle SCHWACHPUNKTE (Gegnertyp -> noetige Erkenntnis) statt if-Kette in
# berechne_schaden() (Konzept 4) - berechne_schaden() bekommt damit endlich einen
# "Verbraucher" (seit Etappe 3c/9 als offen vermerkt). DEPOT_VORAUSSETZUNG (Ware ->
# noetige Erkenntnis) blendet eine Ware in Anzeige UND Kauf gleichermassen aus/ein.
# Vorwissen: sporen_analysiert kuendigt panzerbrut einen Zug vorher an.
#
# Auftragsschritt 13 (vierter Fund, gleiche Wirkungsart): "pheromonspur" fuer speier,
# vier reine Tabellen-Stellen (GEGNERTYP_FUND, FUNDE, ANZEIGENAMEN, SCHWACHPUNKTE), keine
# Funktion angefasst - siehe GELERNT.md fuer die genaue Zaehlung und den Bezug zu
# Konzept 4b (mehrere Tabellen mit denselben Kennungen, bewusst nicht zusammengefuehrt).
#
# Kopplungszeichnung: siehe GELERNT.md (Textform statt Papier/Foto).
#
# Aus Etappe 14 unveraendert: Raster, x/y, Zonen, Bewegung. Aus 13b unveraendert: Zaehler-
# Muster, Basisturm, welt.raeume_frei(). Eigene Entscheidung aus Etappe 11/12: Einheit.
# gesteuert=False als generischer Default, keine isinstance-Pruefung fuer Ausfall/Respawn.

WAREN = {"medkit": 40, "munition": 15, "panzerplatte": 90, "schwerpanzerplatte": 150}
STAPELBAR = {"munition"}
VERKAUFSWERTE = {"chitinpanzer": 5, "organ": 12}
ANZEIGENAMEN = {
    "medkit": "Medkit",
    "munition": "Munition",
    "panzerplatte": "Panzerplatte",
    "schwerpanzerplatte": "Schwerpanzerplatte",
    "chitinpanzer": "Chitinpanzer",
    "organ": "Organ",
    "datenkern": "Datenkern der Brut",
    "vaporium": "Vaporium",
    "chitinprobe": "Chitinprobe",
    "sporenprobe": "Sporenprobe",
    "datenkernfragment": "Datenkernfragment",
    "pheromonspur": "Pheromonspur",
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
REICHWEITE = 5
SCHADENSBONUS_SCHWACHPUNKT = 5

# Auftragsschritt 1: die eine Stelle, die festlegt, welche Erkenntnisse es gibt (Konzept 1).
# Andere Tabellen verweisen auf diese Woerter, erfinden aber keine neuen.
FUNDE = {
    "chitinprobe": {
        "erkenntnis": "chitin_analysiert",
        "text": "Die Chitinprobe hat eine Naht, wo keine sein sollte - keine natuerliche "
                "Panzerung, sondern etwas Gewachsenes mit einem Fehler. Ein Schuss trifft "
                "diese Naht jetzt zuverlaessiger.",
    },
    "sporenprobe": {
        "erkenntnis": "sporen_analysiert",
        "text": "Die Sporen tragen Chitin in einer zweiten Schicht. Was hier schluepft, "
                "bringt Panzerung mit.",
    },
    "datenkernfragment": {
        "erkenntnis": "datenkern_ausgewertet",
        "text": "Der Datenkern traegt eine Bestellnummer der Forschungsabteilung. Offenbar "
                "gibt es einen Lieferanten, den das Depot bisher nicht kannte.",
    },
    # Auftragsschritt 13, vierter Fund - gleiche Wirkungsart wie chitinprobe (Schadensbonus).
    "pheromonspur": {
        "erkenntnis": "pheromon_analysiert",
        "text": "Die Pheromonspur zeigt, wie ein Speier vor dem Spucken kurz innehaelt - "
                "ein Sturmgewehr trifft in diesem Moment zuverlaessiger.",
    },
}
# Gegnertyp -> Liste von Fundkennungen. Nicht jeder Typ muss etwas hinterlassen
# (Auftragsschritt 3); ein Typ darf auch mehrere Fundarten hinterlassen (Auftragsschritt 13,
# vierter Fund: speier hinterlaesst seitdem zwei statt einer).
GEGNERTYP_FUND = {
    "kriecher": ["chitinprobe"],
    "speier": ["sporenprobe", "pheromonspur"],
    "panzerbrut": ["datenkernfragment"],
}
# Umkehrtabelle (Konzept 4): Gegnertyp -> noetige Erkenntnis fuer den Schadensbonus.
SCHWACHPUNKTE = {
    "kriecher": "chitin_analysiert",
    "speier": "pheromon_analysiert",
}
# Ware -> noetige Erkenntnis. Ohne Eintrag: immer da (Auftragsschritt 10).
DEPOT_VORAUSSETZUNG = {
    "schwerpanzerplatte": "datenkern_ausgewertet",
}

# Auftragsschritt 2: alle sieben Zaehlerzahlen an einer Stelle, auch die fuer 13b.
ABKLINGZEIT = 6
RESPAWNZEIT = 5
AUSFALLZEIT = 4
TURM_BAUZEIT = 8
TURM_KOSTEN = 100
NACHLADEZEIT = 2
MAGAZIN_GROESSE = 3
# Eigene Ergaenzung (Auftragsschritt 19 verlangt nur "einen Wert deiner Wahl", keine
# eigene GROSS-Konstante) - der Konvention aus Etappe 1 folgend trotzdem als Konstante:
RAEUMZEIT = 4


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
    if kennung in ("panzerplatte", "schwerpanzerplatte"):
        return Panzerung(kennung, name, schutzwert=10)
    return Item(kennung, name)


class Fundstueck(Item):
    """Ein Fund an einer Koordinate - erbt von Item (landet im Inventar), NICHT von Einheit
    (tickt nicht, hat keine Trefferpunkte, handelt nicht). x/y bedeuten nichts mehr, sobald
    es im Inventar liegt - ein bekannter, in Kauf genommener Schoenheitsfehler (Konzept 6)."""

    def __init__(self, kennung, name, x, y):
        super().__init__(kennung, name)
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Fundstueck(kennung={self.kennung!r}, name={self.name!r}, x={self.x}, y={self.y})"


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


# --- 11b/12b/13: Einheit als gemeinsame Basis von Marine, Gegner und Basisturm ---

class Einheit:
    """Alles, was Trefferpunkte hat, Schaden austeilen kann, im Tick handelt und
    ausfallen/wieder aufstehen kann."""

    def __init__(self, name, trefferpunkte, schaden):
        self.name = name
        self.trefferpunkte = trefferpunkte
        self.max_trefferpunkte = trefferpunkte
        self.schaden = schaden
        self.status = "aktiv"
        self.abschuesse = 0
        self.ausfallzeit = 0
        self.gesteuert = False  # Default; Marine ueberschreibt in __init__.

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

    def zaehler_runter(self, welt):
        """Zaehlt ausfallzeit herunter (generisch fuer jede Einheit, die ausgefallen sein
        kann) und steht bei 0 wieder auf: aktiv, volle Trefferpunkte, Meldung."""
        if self.ausfallzeit > 0:
            self.ausfallzeit -= 1
            if self.ausfallzeit == 0:
                self.status = "aktiv"
                self.trefferpunkte = self.max_trefferpunkte
                welt.melde(f"{self.name} ist wieder einsatzbereit.")

    def __repr__(self):
        return (f"{type(self).__name__}(name={self.name!r}, trefferpunkte={self.trefferpunkte}, "
                f"status={self.status!r})")


class Gegner(Einheit):
    """Ein Gegner der Brut. typ aus Etappe 6 ist der name aus Einheit (Etappe 11).
    entfernung (eine Zahl) ist seit 14a x/y (eine Koordinate) - Konzept-4-Fahndung,
    32 Fundstellen (siehe GELERNT.md)."""

    def __init__(self, name, trefferpunkte, schaden, x, y):
        super().__init__(name, trefferpunkte, schaden)
        self.x = x
        self.y = y

    def update(self, welt):
        """Tot? Nichts tun. Am Tor? Den Kern treffen. Sonst: ein Schritt Richtung Tor,
        eine Achse (Auftragsschritt 5), nur auf ein freies Feld - sonst stehenbleiben."""
        if self.status == "tot":
            return
        tor_x, tor_y = welt.tor
        if (self.x, self.y) == welt.tor:
            welt.kern_integritaet -= self.schaden
            return

        dx = tor_x - self.x
        dy = tor_y - self.y
        neu_x, neu_y = self.x, self.y
        if abs(dx) >= abs(dy):  # Gleichstand: zuerst x (eigene Festlegung)
            neu_x = self.x + (1 if dx > 0 else -1)
        else:
            neu_y = self.y + (1 if dy > 0 else -1)

        if welt.ist_frei(neu_x, neu_y):
            self.x, self.y = neu_x, neu_y

    def __repr__(self):
        return (f"Gegner(name={self.name!r}, trefferpunkte={self.trefferpunkte}, "
                f"x={self.x}, y={self.y}, status={self.status!r})")


class Marine(Einheit):
    """Basis fuer alle vier Klassen: Ausruestung, Vorrat, Standort, Fortschritt."""

    def __init__(self, name, trefferpunkte, schaden, panzerung, klassengeraet, sektor, vorrat,
                 geladen, gesteuert=False):
        super().__init__(name, trefferpunkte, schaden)
        self.gesteuert = gesteuert
        self.panzerung = panzerung
        self.klassengeraet = klassengeraet
        self.sektor = sektor
        self.vorrat = vorrat
        self.inventar = Inventar(10)
        self.ausruestung = Ausruestung()
        # self.position aus Etappe 10 ("noch ohne Bewegung") entfaellt - seit 14b sind x/y/
        # reichweite/zone die echten, bewegten Koordinaten (Auftragsschritt 12). Startwerte
        # hier nur als Platzhalter; das Hauptprogramm setzt die tatsaechliche Aufstellung.
        self.x = 0
        self.y = 0
        self.reichweite = REICHWEITE
        self.zone = None
        self.magazin_groesse = 40  # eigenes Magazin des Helden, seit Etappe 5/6 unveraendert
        self.geladen = geladen
        self.nachladen_noetig = False
        self.erfahrung = 0
        self.level = 1
        self.abklingzeit = 0
        self.magazin = MAGAZIN_GROESSE  # nur fuer Kameraden relevant (Auftragsschritt 15)
        self.nachladezeit = 0

    def __repr__(self):
        return (f"{type(self).__name__}(name={self.name!r}, "
                f"trefferpunkte={self.trefferpunkte}, sektor={self.sektor!r}, level={self.level}, "
                f"x={self.x}, y={self.y}, inventar={self.inventar!r})")

    def faehigkeit_einsetzen(self, welt):
        """Prueft die Abklingzeit (gehoert in die Oberklasse, Auftragsschritt 6). Gibt
        zurueck, ob die Unterklasse jetzt ihre eigene Meldung ausgeben und die Abklingzeit
        setzen darf - True, wenn frei; False, wenn noch gesperrt (dann meldet diese
        Methode selbst die Restzeit)."""
        if self.abklingzeit > 0:
            welt.melde(f"{self.name}: Faehigkeit noch {self.abklingzeit} Takte gesperrt.")
            return False
        self.abklingzeit = ABKLINGZEIT
        return True

    def zaehler_runter(self, welt):
        """Ausfallzeit generisch von Einheit, plus die Marine-eigenen Zaehler: Abklingzeit
        und das Kameraden-Magazin."""
        super().zaehler_runter(welt)

        if self.abklingzeit > 0:
            self.abklingzeit -= 1
            if self.abklingzeit == 0:
                welt.melde(f"{self.name}: Faehigkeit wieder einsatzbereit.")

        if self.nachladezeit > 0:
            self.nachladezeit -= 1
            if self.nachladezeit == 0:
                self.magazin = MAGAZIN_GROESSE

    def update(self, welt):
        """Der gesteuerte Marine wartet auf input() und tut im Tick nichts. Die drei
        Kameraden (Trupp-KI Stufe 2, Konzept 12): Ziel in Reichweite? Feuern. Sonst: ein
        Schritt darauf zu, wenn frei und innerhalb der eigenen Zone."""
        if self.gesteuert:
            return
        if self.status == "tot":
            return

        ziel = welt.naechster_gegner(self.x, self.y)
        if ziel is None:
            return

        if welt.abstand(self.x, self.y, ziel.x, ziel.y) <= self.reichweite:
            if self.magazin <= 0 or self.nachladezeit > 0:
                return
            ueberlebt = ziel.nimm_schaden(self.berechne_schaden(welt.erkenntnisse, ziel.name))
            if not ueberlebt:
                self.abschuesse += 1
            self.magazin -= 1
            if self.magazin == 0:
                self.nachladezeit = NACHLADEZEIT
            print(f"{self.name} feuert automatisch auf {ziel.name}.")
            return

        dx = ziel.x - self.x
        dy = ziel.y - self.y
        neu_x, neu_y = self.x, self.y
        if abs(dx) >= abs(dy):  # Gleichstand: zuerst x - dieselbe Regel wie beim Gegner
            neu_x = self.x + (1 if dx > 0 else -1)
        else:
            neu_y = self.y + (1 if dy > 0 else -1)

        if welt.ist_frei(neu_x, neu_y) and _in_zone(neu_x, neu_y, self.zone):
            self.x, self.y = neu_x, neu_y

    def zeige_status(self, kern_integritaet, freigeschaltet=None, ausfuehrlich=False):
        """Gibt den Statusblock aus: drei Balken, Munition im Vorrat, Vaporium, Erfahrung,
        Stufe und Abklingzeit."""
        zeichne_balken(kern_integritaet, 100, "Kern")
        zeichne_balken(self.trefferpunkte, self.max_trefferpunkte, "Marine")
        zeichne_balken(self.geladen, self.magazin_groesse, "Magazin")
        print(f"Munition im Vorrat: {self.vorrat['munition']}")
        print(f"Vaporium: {self.vorrat['vaporium']}")
        print(f"Erfahrung: {self.erfahrung} (Stufe {self.level})")
        if self.abklingzeit > 0:
            print(f"Faehigkeit: noch {self.abklingzeit} Takte gesperrt")
        else:
            print("Faehigkeit: bereit")

        if ausfuehrlich:
            if freigeschaltet is None or len(freigeschaltet) == 0:
                print("Freigeschaltete Ausbauten: keine")
            else:
                print(f"Freigeschaltete Ausbauten: {', '.join(freigeschaltet)}")

    def berechne_schaden(self, erkenntnisse, ziel_typ):
        """Gibt den Schadenswert zurueck, mit Zuschlag bei bekanntem Schwachpunkt (Konzept 4,
        Umkehrtabelle SCHWACHPUNKTE) - endlich ein echter Verbraucher (seit Etappe 3c/9
        offen). Bekommt bewusst nicht die ganze Welt, nur das Set und den Typ-Namen."""
        ergebnis = self.schaden
        noetig = SCHWACHPUNKTE.get(ziel_typ)
        if noetig is not None and noetig in erkenntnisse:
            ergebnis += SCHADENSBONUS_SCHWACHPUNKT
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

    def kaufe(self, ziel, menge_text, erkenntnisse):
        """Kauft eine Ware aus WAREN. Meldet den Ausgang, veraendert vorrat/inventar direkt.
        Waren mit Eintrag in DEPOT_VORAUSSETZUNG nur mit der noetigen Erkenntnis (Auftrags-
        schritt 10) - dieselbe Meldung wie "gibt es nicht", sonst verraet die Meldung
        selbst schon, dass es die Ware gibt."""
        if self.sektor != "depot":
            print("Das Depot ist im Sektor 'depot'.")
            return
        if ziel == "":
            print("Kaufe was?")
            return
        voraussetzung = DEPOT_VORAUSSETZUNG.get(ziel)
        gesperrt = voraussetzung is not None and voraussetzung not in erkenntnisse
        if ziel not in WAREN or gesperrt:
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
                          geladen=40, gesteuert=gesteuert)

    def faehigkeit_einsetzen(self, welt):
        if not super().faehigkeit_einsetzen(welt):
            return
        welt.melde(f"{self.name} feuert einen Unterlauf-Granatwerfer ab. (Fläche, noch ohne Wirkung.)")


class Heavy(Marine):
    def __init__(self, name, sektor, vorrat, gesteuert=False):
        super().__init__(name, trefferpunkte=140, schaden=14, panzerung=10,
                          klassengeraet="Schweres MG", sektor=sektor, vorrat=vorrat,
                          geladen=40, gesteuert=gesteuert)

    def faehigkeit_einsetzen(self, welt):
        if not super().faehigkeit_einsetzen(welt):
            return
        welt.melde(f"{self.name} setzt Durchschlag ein. (Trifft mehrere Ziele in einer Reihe, noch ohne Wirkung.)")


class Engineer(Marine):
    def __init__(self, name, sektor, vorrat, gesteuert=False):
        super().__init__(name, trefferpunkte=90, schaden=7, panzerung=4,
                          klassengeraet="Multiwerkzeug", sektor=sektor, vorrat=vorrat,
                          geladen=40, gesteuert=gesteuert)

    def faehigkeit_einsetzen(self, welt):
        if not super().faehigkeit_einsetzen(welt):
            return
        welt.melde(f"{self.name} beginnt den Bau eines Geschuetzturms. (Noch ohne Wirkung.)")


class Medic(Marine):
    def __init__(self, name, sektor, vorrat, gesteuert=False):
        super().__init__(name, trefferpunkte=80, schaden=6, panzerung=3,
                          klassengeraet="Bio-Injektor", sektor=sektor, vorrat=vorrat,
                          geladen=40, gesteuert=gesteuert)

    def faehigkeit_einsetzen(self, welt):
        if not super().faehigkeit_einsetzen(welt):
            return
        welt.melde(f"{self.name} setzt den Bio-Injektor ein. (Heilung, noch ohne Wirkung.)")


class Basisturm(Einheit):
    """Ein Gebaeude, kein Marine - steht trotzdem in welt.trupp (Konzept 9). Genau einer,
    unabhaengig von der Klassenwahl (siehe Kopfkommentar/BERICHT.md)."""

    def __init__(self, x, y):
        super().__init__("Basisturm", trefferpunkte=150, schaden=8)
        self.bauzeit = TURM_BAUZEIT
        self.x = x
        self.y = y
        self.reichweite = REICHWEITE

    def update(self, welt):
        if self.bauzeit > 0:
            return
        if self.status == "tot":
            return
        ziel = welt.naechster_gegner(self.x, self.y)
        if ziel is None:
            return
        if welt.abstand(self.x, self.y, ziel.x, ziel.y) > self.reichweite:
            return
        ueberlebt = ziel.nimm_schaden(self.schaden)
        if not ueberlebt:
            self.abschuesse += 1
        print(f"{self.name} feuert auf {ziel.name}.")

    def zaehler_runter(self, welt):
        super().zaehler_runter(welt)
        if self.bauzeit > 0:
            self.bauzeit -= 1
            if self.bauzeit == 0:
                welt.melde("Der Basisturm ist einsatzbereit.")


# --- 12a/13: Die Welt ---

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
        self.turm = None
        self.raeumzeit = 0
        # 14a: Vorfeld als Liste von Listen (welt.vorfeld[y][x]). Sieben Spalten, sechs
        # Zeilen, hingeschrieben (Konzept 3) - Rand aus Wand, ein freier Weg von S nach @
        # auf Zeile 3 (Riegel 1: keine Wegfindung noetig).
        self.vorfeld = [
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", ".", "#"],
            ["#", ".", ".", ".", ".", ".", "#"],
            ["#", "S", ".", ".", ".", "@", "#"],
            ["#", ".", ".", ".", ".", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#"],
        ]
        self.tor = (5, 3)
        self.spawn = (1, 3)
        self.fundstuecke = []
        self.erkenntnisse = set()

    def __repr__(self):
        return (f"Welt(zeit={self.zeit}, welle={self.welle}, "
                f"kern_integritaet={self.kern_integritaet}, gegner={len(self.gegner)})")

    def melde(self, text):
        """Der einzige Ort, an dem Zaehler-Meldungen erscheinen (Auftragsschritt 1)."""
        print(text)

    def ist_auf_dem_raster(self, x, y):
        """Konzept 5: liegt die Koordinate ueberhaupt im Vorfeld?"""
        if y < 0 or y >= len(self.vorfeld):
            return False
        if x < 0 or x >= len(self.vorfeld[y]):
            return False
        return True

    def ist_frei(self, x, y):
        """Erst die Randpruefung, dann der Zugriff (sonst liest x=-1 still das letzte
        Feld der Zeile). Frei heisst: keine Wand - Einheiten stehen nicht im Raster
        (Riegel 2), also blockieren sie sich hier nicht gegenseitig."""
        if not self.ist_auf_dem_raster(x, y):
            return False
        return self.vorfeld[y][x] != "#"

    def abstand(self, x1, y1, x2, y2):
        """Manhattan-Distanz - passt zur Ein-Achse-pro-Tick-Bewegung (Konzept 9):
        Abstand == Anzahl Ticks bis dahin."""
        return abs(x2 - x1) + abs(y2 - y1)

    def felder_in_reichweite(self, x, y, r):
        """Set aus (x,y)-Tupeln aller Felder im Vorfeld mit Abstand <= r (Konzept 10)."""
        felder = set()
        for py in range(len(self.vorfeld)):
            for px in range(len(self.vorfeld[py])):
                if self.abstand(x, y, px, py) <= r:
                    felder.add((px, py))
        return felder

    def naechster_gegner(self, x, y):
        """Der aktive Gegner mit dem kleinsten Abstand zu (x,y) - "am naechsten" haengt
        seit 14b vom Standort des Suchenden ab (Auftragsschritt 10). None, wenn keiner
        mehr aktiv ist."""
        naechster = None
        bester_abstand = None
        for g in self.gegner:
            if g.status == "tot":
                continue
            a = self.abstand(x, y, g.x, g.y)
            if naechster is None or a < bester_abstand:
                naechster = g
                bester_abstand = a
        return naechster

    def raeume_auf(self):
        """Entfernt alle toten Gegner aus welt.gegner (Sammeln, dann entfernen - Konzept
        11). Wer gerade gefallen ist, hinterlaesst an SEINER Koordinate ein Fundstueck
        (Auftragsschritt 3), falls sein Typ in GEGNERTYP_FUND steht. Setzt danach bei toten
        Trupp-Mitgliedern ohne laufenden Zaehler die Ausfallzeit - RESPAWNZEIT fuer den
        Gesteuerten, sonst AUSFALLZEIT (Konzept 7)."""
        gefallene = []
        for g in self.gegner:
            if g.status == "tot":
                gefallene.append(g)
        for g in gefallene:
            self.gegner.remove(g)
            for kennung in GEGNERTYP_FUND.get(g.name, []):
                name = ANZEIGENAMEN.get(kennung, kennung)
                self.fundstuecke.append(Fundstueck(kennung, name, g.x, g.y))

        for kamerad in self.trupp:
            if kamerad.status == "tot" and kamerad.ausfallzeit == 0:
                if kamerad.gesteuert:
                    kamerad.ausfallzeit = RESPAWNZEIT
                else:
                    kamerad.ausfallzeit = AUSFALLZEIT

        return len(gefallene)

    def raeume_frei(self):
        """Oeffnet den Osttunnel. Eigene Entscheidung aus Etappe 5 ('der Weg fehlt
        einfach') - der Eintrag wird neu erzeugt, kein del noetig."""
        self.sektoren["osttor"]["nachbarn"]["osten"] = "landeplattform"
        self.melde("Der Osttunnel ist frei. Die Landeplattform ist erreichbar.")

    def sammle_fundstuecke_ein(self):
        """Nach der letzten Aufraeumphase einer Welle, vor der naechsten (Konzept 7).
        Ein Fundstueck wird eingesammelt, wenn seine Koordinate in der Zone MINDESTENS
        EINES noch stehenden Marines liegt (Auftragsschritt 5) - Zonen ueberlappen sich
        nicht, also reicht eine. Sammeln, dann entfernen (Konzept 11)."""
        eingesammelt = []
        liegengeblieben = []
        for fund in self.fundstuecke:
            gesammelt = False
            for kamerad in self.trupp:
                if kamerad.status == "tot":
                    continue
                if _in_zone(fund.x, fund.y, kamerad.zone):
                    if kamerad.inventar.hinzufuegen(fund):
                        eingesammelt.append(fund)
                        gesammelt = True
                    break
            if not gesammelt:
                liegengeblieben.append(fund)
        for fund in eingesammelt:
            self.fundstuecke.remove(fund)

        if len(eingesammelt) > 0:
            namen = [f.name for f in eingesammelt]
            self.melde(f"Eingesammelt: {', '.join(namen)}.")
        if len(liegengeblieben) > 0:
            self.melde(f"{len(liegengeblieben)} Fundstueck(e) ausserhalb der Zonen "
                       f"zurueckgelassen.")

    def tick(self):
        """Fuenf Phasen: Zeit, Zaehler, Trupp, Gegner, Aufraeumen. Reihenfolge Trupp-vor-
        Gegner heisst: Ein Gegner, den der Trupp in Phase 3 toetet, schlaegt in Phase 4
        desselben Ticks nicht mehr zu - siehe GELERNT.md (Etappe 12/13)."""
        self.zeit += 1

        for kamerad in self.trupp:
            kamerad.zaehler_runter(self)
        if self.raeumzeit > 0:
            self.raeumzeit -= 1
            if self.raeumzeit == 0:
                self.raeume_frei()

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


def zeichne_vorfeld(vorfeld, trupp, gegner, fundstuecke):
    """Loest zeichne_bahn() aus Etappe 7b ab (Auftragsschritt 7, geloescht statt
    auskommentiert). Kopie Zeile fuer Zeile (Konzept 8) - malt nicht ins echte Gelaende.
    Fundstuecke VOR den Einheiten gemalt (Auftragsschritt 4), sonst verdeckt eine Einheit
    das Fundstueck. Veraendert nichts, gibt nur aus."""
    bild = []
    for zeile in vorfeld:
        bild.append(zeile.copy())
    for fund in fundstuecke:
        bild[fund.y][fund.x] = "f"
    for kamerad in trupp:
        if kamerad.status != "tot":
            bild[kamerad.y][kamerad.x] = "M"
    for g in gegner:
        if g.status != "tot":
            bild[g.y][g.x] = TYP_ZEICHEN[g.name]
    for zeile in bild:
        print("".join(zeile))


def _in_zone(x, y, zone):
    """Konzept 11: dieselbe Form wie die Randpruefung, nur mit den Grenzen der Zone statt
    des Rasters. zone ist None -> keine Einschraenkung (fuer Einheiten ohne Zone, z. B.
    den Turm, der sich ohnehin nicht bewegt)."""
    if zone is None:
        return True
    x0, y0, x1, y1 = zone
    if x < x0 or x > x1:
        return False
    if y < y0 or y > y1:
        return False
    return True


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

    if marine.status == "tot":
        # Auftragsschritt 14: JEDER Befehl wird abgewiesen, der Tick laeuft trotzdem -
        # sonst sperrt man sich ein (Kaputtmachen 4, ausprobiert und bestaetigt).
        welt.melde(f"Du bist ausgefallen. Noch {marine.ausfallzeit} Takte bis zum Aufstehen.")
        return True, False, False

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
            zustand = kamerad.status
            if kamerad.status == "tot":
                zustand = f"ausgefallen, noch {kamerad.ausfallzeit} Takte"
            print(f"  {kamerad.name} - {type(kamerad).__name__} - {kamerad.trefferpunkte} TP"
                  f" - {zustand} - {kamerad.abschuesse} Abschuesse{markierung}")

    elif befehl == "feuern":
        schuesse = 1
        if "schnellfeuer" in freigeschaltet:
            schuesse = 2
        abgegeben = 0
        for i in range(schuesse):
            if marine.geladen > 0 and len(welt.gegner) > 0:
                marine.geladen -= 1
                # Eigene Entscheidung (naechster_gegner braucht seit 14b einen Startpunkt):
                # der Held zielt wie die Kameraden auf den ihm naechsten Gegner, nicht mehr
                # bedingungslos auf den torneesten - siehe GELERNT.md/BERICHT.md.
                vorderster = welt.naechster_gegner(marine.x, marine.y)
                if vorderster is not None:
                    welt.gegner.remove(vorderster)
                    # weiterhin ein Ein-Schuss-Kill seit Etappe 6 - der Rueckgabewert wird
                    # nicht auf den Treffer angewendet (siehe BERICHT.md, bekannte, seit
                    # Etappe 12 dokumentierte Asymmetrie Held/Kameraden). Trotzdem echt
                    # aufgerufen, damit ein bekannter Schwachpunkt bei "status" sichtbar
                    # bliebe, falls berechne_schaden() spaeter eine zweite Wirkung bekommt.
                    marine.berechne_schaden(welt.erkenntnisse, vorderster.name)
                    marine.erfahrung += 10
                    alte_stufe = marine.level
                    marine.berechne_stufe()
                    if marine.level > alte_stufe:
                        welt.melde(f"{marine.name} steigt auf Stufe {marine.level} auf!")
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
        marine.faehigkeit_einsetzen(welt)

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
        elif ziel not in welt.bodenfunde:
            print(f"{ANZEIGENAMEN.get(ziel, ziel)} liegt hier nicht.")
        elif not marine.inventar.hinzufuegen(erzeuge_item(ziel)):
            print("Das Inventar ist voll.")
        else:
            welt.bodenfunde.remove(ziel)
            print(f"{ANZEIGENAMEN.get(ziel, ziel)} aufgenommen.")

    elif befehl == "ablege":
        if ziel == "":
            print("Ablegen was?")
        elif not marine.inventar.enthaelt(ziel):
            print(f"Du traegst kein {ANZEIGENAMEN.get(ziel, ziel)}.")
        else:
            marine.inventar.entfernen(ziel)
            welt.bodenfunde.append(ziel)
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
                voraussetzung = DEPOT_VORAUSSETZUNG.get(ware)
                if voraussetzung is not None and voraussetzung not in welt.erkenntnisse:
                    continue
                print(f"{ANZEIGENAMEN.get(ware, ware)}: {WAREN[ware]} Vaporium")

    elif befehl == "kaufe":
        marine.kaufe(ziel, menge_text, welt.erkenntnisse)

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
            # Auftragsschritt 11: dritte Stufe "verstanden" - Logik von Etappe 6
            # unangetastet, nur eine Zeile angehaengt.
            schwachpunkt = SCHWACHPUNKTE.get(ziel)
            if schwachpunkt is not None and schwachpunkt in welt.erkenntnisse:
                print(f"Schwachpunkt bekannt: +{SCHADENSBONUS_SCHWACHPUNKT} Schaden gegen diesen Typ.")

    elif befehl == "analysiere":
        if ziel == "":
            print("Analysiere was?")
        elif ziel not in FUNDE:
            print("Davon weisst du nichts.")
        elif FUNDE[ziel]["erkenntnis"] in welt.erkenntnisse:
            print("Das hast du bereits ausgewertet.")
        elif not marine.inventar.enthaelt(ziel):
            print("Das hast du nicht dabei.")
        else:
            welt.erkenntnisse.add(FUNDE[ziel]["erkenntnis"])
            print(FUNDE[ziel]["text"])

    elif befehl == "baue":
        if ziel != "turm":
            print("Meintest du 'baue turm'?")
        elif marine.sektor != "werkstatt":
            print("Bauauftraege gibt es nur in der Werkstatt.")
        elif welt.turm is not None:
            print("Es steht bereits ein Basisturm.")
        elif TURM_KOSTEN > marine.vorrat["vaporium"]:
            print("Das Vaporium reicht nicht.")
        else:
            marine.vorrat["vaporium"] -= TURM_KOSTEN
            turm = Basisturm(4, 2)  # fester Platz im Vorposten (Auftragsschritt 12)
            welt.turm = turm
            welt.trupp.append(turm)
            print(f"Der Basisturm ist in Auftrag gegeben. Fertig in {TURM_BAUZEIT} Takten.")

    elif befehl == "raeume":
        if marine.sektor != "osttor":
            print("Freiraeumen geht nur am Osttor.")
        elif "osten" in welt.sektoren["osttor"]["nachbarn"]:
            print("Der Tunnel ist schon frei.")
        elif welt.raeumzeit > 0:
            print(f"Wird schon geraeumt. Noch {welt.raeumzeit} Takte.")
        else:
            welt.raeumzeit = RAEUMZEIT
            print(f"Freiraeumen begonnen. Fertig in {RAEUMZEIT} Takten.")

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
        "beschreibung": "Die Werkstatt. Hier wird der Basisturm in Auftrag gegeben.",
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
    marine.x, marine.y = (2, 1)
    # Zonen (Konzept 11): das Vorfeld ist 7x6, Rand ist Wand (x:1-5, y:1-4 begehbar).
    # Aufgeteilt in drei ueberlappungsfreie Streifen entlang y, damit sich der Trupp beim
    # Verteidigen nicht auf ein Feld draengt.
    marine.zone = (1, 1, 5, 1)

    # Die drei Kameraden: die anderen Klassen kommen automatisch dazu, mit eigenem Vorrat,
    # an unterschiedlichen Startpunkten und mit unterschiedlichen Zonen (Auftragsschritt 12/14).
    KAMERADEN_AUFSTELLUNG = [((2, 2), (1, 2, 5, 2)), ((2, 3), (1, 3, 5, 3)), ((2, 4), (1, 4, 5, 4))]
    aufstellung_index = 0
    for zahl, Klassenbauplan in KLASSEN_NACH_ZAHL.items():
        if Klassenbauplan is not GewaehlteKlasse:
            kamerad_name = f"Rekrut {Klassenbauplan.__name__}"
            kamerad_vorrat = {"vaporium": 0, "munition": 40, "chitinpanzer": 0, "organ": 0}
            kamerad = Klassenbauplan(kamerad_name, "nordtor", kamerad_vorrat, gesteuert=False)
            (kamerad.x, kamerad.y), kamerad.zone = KAMERADEN_AUFSTELLUNG[aufstellung_index]
            aufstellung_index += 1
            welt.trupp.append(kamerad)

    gesehene_gegnertypen = set()
    freigeschaltet = set()
    welt.bodenfunde = []

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

        # Konzept 8, Vorwissen: aendert nur den Text, nie eine Zahl. Die if/elif-Kette,
        # die festlegt, wann panzerbrut dazukommt, wird nur gelesen (welle == 7 -> Welle 8
        # bringt panzerbrut), nicht angefasst.
        if "sporen_analysiert" in welt.erkenntnisse and welle == 7:
            welt.melde("Die Pheromonspur wird staerker. Naechste Welle: gepanzerte Brut.")

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
            spawn_x, spawn_y = welt.spawn
            welt.gegner.append(Gegner(gegner_typ, trefferpunkte=20, schaden=5, x=spawn_x, y=spawn_y))

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

                zeichne_vorfeld(welt.vorfeld, welt.trupp, welt.gegner, welt.fundstuecke)

                if welt.kern_integritaet <= 0:
                    print("Die Kernintegritaet ist auf 0 gefallen. Der Vorposten ist verloren.")
                    welt.laeuft = False
                    break

                if len(welt.gegner) == 0:
                    print("Welle geschafft.")
                    marine.vorrat["chitinpanzer"] = marine.vorrat.get("chitinpanzer", 0) + 1
                    marine.vorrat["organ"] = marine.vorrat.get("organ", 0) + 1
                    welt.bodenfunde.append("datenkern")
                    print("Die Brut hat Material hinterlassen, und im Vorfeld liegt etwas.")
                    # Konzept 7: NACH der letzten Aufraeumphase dieser Welle, VOR der
                    # naechsten - sonst fehlt die Beute des letzten Gegners.
                    welt.sammle_fundstuecke_ein()
                    break

    zeichne_grundriss(marine.sektor)

print("Programmende.")
