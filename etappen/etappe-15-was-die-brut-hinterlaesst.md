# Etappe 15 — Was die Brut hinterlässt

*v1.1.1 · 2026-09-16*

> **Block 2: Einheiten und Zeit** · Etappe 15 von 30 · [← Etappe 14](etappe-14-das-vorfeld.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 16 →](etappe-16-bug-jagd-ii.md)

**Neue Syntax heute:** Fast keine. Das Set-Muster *merken → abfragen* (`add()` … `in`) · die Umkehrtabelle *Sache → Voraussetzung* · eine Suchschleife, die `None` zurückgibt · 👀 der Begriff *Kopplung* als Zeichnung

⚠️ **Das ist die erste Etappe, die fast nichts Neues lehrt — und trotzdem einen Stern trägt.** Alle Werkzeuge kennst du: Sets seit Etappe 6, Dictionaries seit Etappe 5, Klassen seit Etappe 9, Koordinaten seit gestern. **Was heute neu ist, ist keine Zeile Python, sondern die Frage, wie vier Systeme miteinander reden, ohne aneinander festzuwachsen.**

**Zeitaufwand:** 4–5 Sitzungen à 20–30 Minuten. Rund 38 Minuten Lesestoff — **eine Portion**, aber mit einem sauberen Schnitt nach Auftragsschritt 8.

**Voraussetzung:** Etappe 14 abgeschlossen, mindestens 14a und 14b. Du brauchst das Raster, die Koordinaten und die Zonen. *(Ohne 14c geht alles; die Barrikade spielt heute keine Rolle.)*

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Fundstücke auf Feldern · `erkenntnisse` als Set · Analysieren · Wirkung auf Depot und Schaden · die Umkehrtabelle | Ein Ereignis verändert den Zustand **dauerhaft** · warum ein Set und kein Dictionary aus Booleans · warum die Wirkung nicht beim Fund wohnt | Der Begriff *Kopplung* — als Zeichnung, nicht als Reparatur |

---

## Worum es geht

Dein Spiel vergisst alles.

Eine Welle endet, die nächste beginnt, und außer ein paar Zahlen ist nichts übrig. Du hast in Etappe 4 einen **Datenkern** eingebaut, der sich untersuchen lässt und eine Zahlenfolge ausgibt, die nichts bedeutet. Der Guide von damals hat dir versprochen, dass sie irgendwann etwas bedeutet.

> **Heute bedeutet sie etwas.**

Ab heute hinterlassen gefallene Gegner nicht nur Vaporium, sondern **Spuren**: eine Chitinprobe mit einer Naht, wo keine sein sollte. Einen halb geschmolzenen Datenkern mit einer Bestellnummer darauf. Sporen, die Chitin in einer zweiten Schicht tragen — von etwas, das noch nicht gekommen ist.

Und jede dieser Spuren lässt sich **auswerten**. Was dabei herauskommt, verschwindet nicht mehr:

- Wer die Chitinprobe analysiert hat, **macht gegen Kriecher mehr Schaden** — für immer, in jeder Welle.
- Wer den Datenkern ausgewertet hat, **bekommt im Depot etwas angeboten, das vorher nicht im Sortiment war.**
- Wer die Sporen kennt, **weiß, was in Welle zwölf kommt** — und kann vorbauen.

**Das ist der Moment, in dem aus vier Bausteinen ein Spiel wird.** Bisher hatte dein Programm ein Kampfsystem, eine Wirtschaft, eine Karte und ein Bestiarium — vier Dinge, die nebeneinanderher liefen. Heute fangen sie an, miteinander zu reden.

**Und technisch sind es vier Zeilen:**

```python
erkenntnisse = set()
erkenntnisse.add("chitinprobe")

if "chitinprobe" in erkenntnisse:
    ...
```

> **Etwas passiert einmal. Daraus entsteht Wissen. Das Wissen gehört danach nicht mehr zum Ereignis, sondern zum Spielzustand — und völlig andere Systeme können es abfragen, ohne je von dem Ereignis gehört zu haben.**

`set()` und `.add()` sind nur die Python-Umsetzung davon. **Der schwierige Teil ist nicht, die vier Zeilen hinzuschreiben — sondern zu entscheiden, wo das `if` steht.** Genau darum geht es heute.

*(Und deshalb heißt die Etappe, wie sie heißt: Das Bleibende ist nicht das Fundstück. Es ist die Erkenntnis.)*

---

## Der lange Bogen — was heute fällig wird

- **Der Datenkern aus Etappe 4** wird eingelöst. Elf Etappen lang hat er dagesessen und eine Zahlenfolge ausgegeben, die niemand erklärt hat. *(Falls du die Kür damals ausgelassen hast: kein Problem — du baust ihn heute, dann eben rückwärts.)*
- **`GEGNERTYPEN` und `gesehene_gegnertypen` aus Etappe 6.** Erkenntnisse hängen sich an **vorhandene** Einträge; sie erfinden keine neuen. Und die Anzeige im Bestiarium verändert sich, ohne dass du das Bestiarium anfasst.
- **Die Erstbegegnung aus Etappe 6** — der lange Text beim ersten Mal — bekommt heute eine zweite Stufe: Wer den Typ *analysiert* hat, liest mehr als wer ihn nur gesehen hat.
- **Die Zonen aus Etappe 14b** entscheiden mit, was du überhaupt einsammeln kannst. Die erste Stelle, an der die Zone nicht nur Bewegung begrenzt, sondern etwas einbringt.
- **Die Aufräumphase aus Etappe 12** liefert das Material: Wer in diesem Tick gefallen ist, hinterlässt etwas — und *wo* er gefallen ist, weißt du seit gestern.
- **Der Kopplungs-Begriff aus Etappe 12 und 13** wird heute zum ersten Mal **sichtbar**. Nicht als Warnung im Text, sondern als Zeichnung auf einem Blatt Papier, das du aufhebst.

---

## Eine Design-Entscheidung, die du jetzt treffen musst

### Wo wohnt eine Erkenntnis? ⭐⭐

Drei Orte kommen in Frage, und sie klingen alle vernünftig:

| | Beim Fundstück | Beim Gegnertyp | Zentral beim Spieler |
|---|---|---|---|
| Wie | `fundstueck.analysiert = True` | `GEGNERTYPEN["kriecher"]["bekannt"] = True` | `welt.erkenntnisse` als Set |
| Was passiert, wenn du das Fundstück ablegst? | **Die Erkenntnis ist weg** | — | — |
| Was passiert bei zwei Chitinproben? | **Zwei Wahrheiten** | — | — |
| Wo steht, was der Spieler weiß? | verteilt auf alle Fundstücke | im Katalog, der eigentlich fest ist | **an einer Stelle** |
| In Etappe 19 speichern | jedes Fundstück einzeln | den halben Katalog | **eine Menge Wörter** |

**Der Plan legt sich auf die dritte Spalte fest**, und die Begründung ist dieselbe Besitzfrage wie seit Etappe 9:

> **Eine Erkenntnis gehört nicht dem Ding, aus dem sie stammt. Sie gehört dem, der sie hat.**

Ein analysiertes Chitinstück kannst du wegwerfen — du weißt trotzdem, wo die Naht sitzt. **Einmal gewonnen, bleibt die Erkenntnis im Spielwissen, auch wenn das Fundstück verschwindet.** Ein Modell, das das nicht abbildet, produziert Unsinn: Wer die Probe ablegt, würde dümmer.

⚠️ **Die zweite Spalte ist die verführerischste und die schlimmste.** `GEGNERTYPEN` ist dein **Katalog** — er beschreibt, was es in diesem Spiel gibt, und er ist seit Etappe 6 unveränderlich. Schreibst du dort den Spielstand hinein, vermischst du zwei Dinge, die Etappe 6 ausdrücklich getrennt hat: *was existiert* und *was ich kenne*. **Die Trennung `GEGNERTYPEN` ↔ `gesehene_gegnertypen` ist genau diese Trennung. Dein neues Set ist die dritte Menge in derselben Familie.**

**Schreib deine Entscheidung in `GELERNT.md`.** In Etappe 18 kommt sie zurück, wenn Fähigkeiten Voraussetzungen bekommen.

---

## Die Konzepte

Alle Beispiele laufen **außerhalb** deines Spiels. Heute in einer Kfz-Werkstatt.

### 1. Merken und später abfragen ⭐⭐

```python
class Werkstatt:
    def __init__(self):
        self.befunde = set()

    def pruefe_bremsen(self, wagen):
        if wagen.belagstaerke < 3:
            self.befunde.add("bremsen_kritisch")
```

Und irgendwo ganz woanders, Stunden später:

```python
if "bremsen_kritisch" in self.befunde:
    print("Achtung: Probefahrt nur auf dem Hof.")
```

**Drei Dinge daran sind wichtiger, als sie aussehen:**

- **`add()` doppelt schadet nicht.** Prüfst du die Bremsen dreimal, steht der Befund trotzdem einmal drin. Bei einer Liste hättest du ihn dreimal und müsstest vorher fragen.
- **Die beiden Stellen wissen nichts voneinander.** Die Prüfung kennt die Probefahrt nicht, die Probefahrt kennt die Prüfung nicht. Beide kennen nur das Wort `"bremsen_kritisch"`.
- **Das Wort ist der ganze Vertrag.** Es gibt keinen Compiler, der dich warnt, wenn du an einer Stelle `"bremsen_kritisch"` schreibst und an der anderen `"bremse_kritisch"`.

⚠️ **Der letzte Punkt ist die einzige echte Gefahr dieses Musters, und sie ist still.** Ein Tippfehler im Wort erzeugt keinen Fehler — er erzeugt eine Erkenntnis, die nie abgefragt wird, und eine Abfrage, die nie zutrifft. **Nichts stürzt ab, und das Spiel tut einfach nicht das, was es soll.**

**Der Schutz dagegen kostet dich heute nichts, und er braucht eine genaue Formulierung:**

> **Es gibt genau eine Stelle, die festlegt, welche Erkenntnisse es gibt und wie sie heißen. Andere Tabellen dürfen auf eine Kennung *verweisen* — sie dürfen keine neue erfinden.**

⚠️ **Das ist nicht dasselbe wie „der String steht nur einmal im Quelltext".** Deine Schwachpunkt-Tabelle wird `"schwachpunkt_kriecher"` ebenfalls enthalten, und das ist richtig so — sie *verweist* darauf. Der Fehler wäre, dort ein Wort zu benutzen, das in der Fundtabelle nicht vorkommt. **Ein Verweis ohne Ziel fällt nicht auf.**

**Die praktische Regel daraus:** Wenn du in einer zweiten Tabelle ein Erkenntnis-Wort hinschreibst, schlag es vorher in der ersten nach. Und wenn dir das zu mühsam wird, ist das ein Signal — siehe Konzept 4b.

*(In Etappe 21b tauschst du die Wörter gegen ein `Enum`, und dann meckert Python bei einem Verweis ins Leere. Heute ist die Disziplin der Ersatz dafür.)*

### 2. Warum ein Set und kein Dictionary aus Booleans ⭐

Das hier wäre der naheliegende Gegenvorschlag:

```python
befunde = {"bremsen_kritisch": True, "oel_alt": False}
```

**Sieh dir an, was `True` dir eigentlich sagt.**

Nichts. Es sagt *„dieser Befund liegt vor"* — und dass er vorliegt, sagt schon der Umstand, dass er überhaupt dasteht. **`False` ist eine umständliche Schreibweise für „nicht dabei".** Du hast einen Schlüssel angelegt, um zu vermerken, dass es nichts zu vermerken gibt.

> **Ein Dictionary lohnt sich, wenn du zu einem Schlüssel noch etwas wissen willst. Bei einer Erkenntnis willst du genau eine Sache wissen: ob sie da ist. Dafür ist die Menge der vorhandenen Erkenntnisse die richtige Struktur.**

| Frage | Passende Struktur |
|---|---|
| Gehört etwas zu einer Menge? | **Set** |
| Gehört etwas dazu — **und** was gehört dazu? | **Dictionary** |

**Die Gegenprobe macht die Grenze scharf.** Sobald du wissen willst, *wann* der Befund entstand, *wer* ihn erhoben hat oder *wie sicher* er ist, wird das Set falsch und ein Dictionary richtig — dann hast du nämlich echte Angaben und nicht nur `True`.

*(Dasselbe gilt für `freigeschaltet` und `gesehene_gegnertypen` aus Etappe 6. Drei Mengen, dieselbe Überlegung — und keine davon trägt einen Wert.)*

⚠️ **Es gibt noch ein zweites, kleineres Argument, und es ist nicht das Hauptargument:** Ein Dictionary aus Booleans kennt drei Lagen statt zwei — `True`, `False` und *Schlüssel fehlt*, was beim Lesen einen `KeyError` gibt. **Das lässt sich mit `.get(name, False)` abfangen**, ist also eher Buchhaltung als Grund. Der Grund ist der Absatz darüber.

### 3. Drei Dinge, die man leicht verwechselt

| Was | Wo es lebt | Wann es verschwindet |
|---|---|---|
| **Das Fundstück** | auf einem Feld im Vorfeld | wenn es aufgesammelt wird |
| **Der Besitz** | im Inventar | wenn du es ablegst oder verbrauchst |
| **Die Erkenntnis** | in `welt.erkenntnisse` | **nie** |

**Drei Stufen, drei Orte, und der Übergang zwischen zwei und drei ist eine Handlung des Spielers** — er muss analysieren. Wer die Probe einsteckt und nie auswertet, hat einen Gegenstand und kein Wissen.

*(Das ist die Sorte Unterscheidung, die Spiele gut macht und die man im Code leicht einebnet: Wer beim Aufheben sofort die Erkenntnis setzt, hat Stufe zwei und drei zusammengelegt — und dem Spieler eine Entscheidung genommen.)*

### 4. Wo die Wirkung wohnt — die Umkehrtabelle ⭐⭐

**Das ist das Konzept, um das es heute eigentlich geht.** Der naheliegende Weg sieht so aus:

```python
def berechne_rechnung(wagen, werkstatt):
    preis = 100
    if "bremsen_kritisch" in werkstatt.befunde:
        preis = preis + 80
    if "oel_alt" in werkstatt.befunde:
        preis = preis + 40
    if "achse_verzogen" in werkstatt.befunde:
        preis = preis + 250
    return preis
```

**Das funktioniert, und es ist eine Falle mit Zeitzünder.** Jeder neue Befund kostet dich eine Zeile **in dieser Funktion**. Nach zehn Befunden hast du zehn `if`-Zweige, und wenn du einen elften einbaust, musst du die Funktion anfassen, die mit Befunden eigentlich gar nichts zu tun hat.

**Der andere Weg dreht die Frage um:**

```python
ZUSCHLAEGE = {
    "bremsen_kritisch": 80,
    "oel_alt": 40,
    "achse_verzogen": 250,
}

def berechne_rechnung(wagen, werkstatt):
    preis = 100
    for befund in ZUSCHLAEGE:
        if befund in werkstatt.befunde:
            preis = preis + ZUSCHLAEGE[befund]
    return preis
```

**Der elfte Befund ist jetzt eine Zeile in der Tabelle und null Zeilen in der Funktion.**

> **Statt in der Logik aufzuzählen, was es alles gibt, schreibst du es in eine Tabelle — und die Logik liest sie.**

⚠️ **Und jetzt die Variante, die du in deinem Spiel brauchst**, weil die Frage anders herum gestellt wird. Du willst nicht wissen *„was kostet welcher Befund"*, sondern *„hat dieser eine Wagen einen Schwachpunkt, den ich kenne?"*. Dann steht in der Tabelle nicht der Zuschlag, sondern die **Voraussetzung**:

```python
SCHWACHPUNKTE = {"golf": "achse_verzogen", "transporter": "bremsen_kritisch"}

def rabatt(modell, befunde):
    noetig = SCHWACHPUNKTE.get(modell)
    if noetig is not None and noetig in befunde:
        return 20
    return 0
```

**Lies die Tabelle als Satz:** *Für einen Golf brauchst du den Befund `achse_verzogen`.* Ein Modell, das nicht in der Tabelle steht, bekommt `None` — und `is None` aus Etappe 10 fängt das ab, ohne dass irgendwo ein `KeyError` entsteht.

**Diese sechs Zeilen sind der Grund, warum Auftragsschritt 12 heute überhaupt machbar ist.** Merk sie dir.

### 4b. Drei Tabellen, die zusammengehören — und heute nebeneinander bleiben

Am Ende des Abends hast du mehrere Tabellen, die alle dieselben Kennungen benutzen: die Fundtabelle, die Schwachpunkte, die Depotfreigaben, vielleicht die Beute pro Gegnertyp.

**Und du wirst denken: Das gehört doch zusammen.** Es gehört zusammen.

> **Heute sollst du das *bemerken*, nicht auflösen.** Mehrere Tabellen mit demselben Schlüsselsatz sind ein bekanntes Muster — und der Zeitpunkt, sie zusammenzuführen, ist Etappe 22, wenn alle Zahlen des Spiels zu Daten werden.

**Wer sie heute zusammenbaut, löst ein Problem, das er noch nicht kennt.** Schreib stattdessen in `GELERNT.md`, welche Tabellen du hast und was ihnen gemeinsam ist. Das ist die Vorarbeit, und sie kostet zwei Minuten.

### 5. Das erste finden, das passt

Eine Suche über eine Sammlung, die ein Ergebnis oder nichts liefert:

```python
def finde_auftrag(auftraege, kennzeichen):
    for a in auftraege:
        if a.kennzeichen == kennzeichen:
            return a
    return None
```

**Du kennst jede Zeile davon** — die Schleife aus Etappe 4, das vorzeitige `return` aus Etappe 7, `None` aus Etappe 10. Neu ist nur, dass sie zusammen ein Muster ergeben, das du ab heute ständig brauchst.

**Zwei Dinge, die dabei zählen:**

- **`return` mitten in der Schleife beendet Schleife und Funktion sofort.** Das ist der Grund, warum diese Form „das *erste* Passende" liefert und nicht das letzte.
- **Das `return None` am Ende steht dort absichtlich.** Ohne es gäbe Python auch `None` zurück — aber dann steht es nirgends, und der nächste Leser muss den ganzen Körper durchgehen, um es zu wissen.

⚠️ **Und die Pflicht beim Aufrufer:** Jede Funktion, die `None` zurückgeben *kann*, muss beim Aufrufer geprüft werden. Wer das vergisst, bekommt `AttributeError: 'NoneType' object has no attribute ...` — **eine Zeile später und an einer anderen Stelle als der eigentliche Fehler.** Genau darum geht es in der Leseübung heute.

### 6. Fundstücke liegen irgendwo

Seit gestern hat alles in deinem Vorfeld eine Koordinate — auch das, was ein Gegner fallen lässt.

**Und jetzt die Frage, die du dir stellen musst, bevor du die Klasse tippst:** Dein Inventar enthält seit Etappe 11 **`Item`-Objekte**, keine Strings. Ein Fundstück landet im Inventar. **Also ist ein Fundstück ein Item.**

```python
class Fundstueck(Item):
    def __init__(self, kennung, name, x, y):
        super().__init__(kennung, name)
        self.x = x
        self.y = y
```

**Eine Unterklasse, die ein Attribut mitbringt** — genau die Form aus Etappe 11, Konzept 7. Und damit funktioniert alles, was du dort gebaut hast, unverändert weiter: Die Inventarsuche vergleicht `.kennung`, die Anzeige zeigt `.name`.

⚠️ **Es erbt ausdrücklich nicht von `Einheit`.** Ein Fundstück tickt nicht, hat keine Trefferpunkte und handelt nicht. **Die Frage „wovon erbt das?" beantwortet sich daran, wer es benutzt** — das Inventar, nicht der Tick.

⚠️ **Und ein Schönheitsfehler, den du kennen sollst:** Liegt das Fundstück im Inventar, bedeuten `x` und `y` nichts mehr. Sie stehen da und lügen. **Das ist heute in Ordnung** — die Alternative wäre eine zweite Klasse und ein Umwandeln beim Einsammeln, und das kostet mehr, als es hier einbringt. *(Notier es als offenen Posten. In Etappe 23b bekommst du Werkzeuge, mit denen sich das billig sauber machen lässt.)*

⚠️ **Und was hier ausdrücklich nicht hineingehört: die Wirkung.** Kein `fundstueck.analysiere()`, das den Schaden erhöht. Warum, steht in Konzept 4 — und noch deutlicher in der Kopplungszeichnung weiter unten.

### 7. Der Einzug — einsammeln, was übrig ist

Ein Gegner fällt bei `(7, 3)`. Sein Fundstück liegt bei `(7, 3)`. **Wie kommt es in dein Inventar?**

**Zwei Wege, und du entscheidest:**

| | Beim Fallen sofort ins Inventar | Es liegt, bis jemand es holt |
|---|---|---|
| Aufwand | null | eine Einsammelphase |
| Nutzt das Raster | gar nicht | ja |
| Spielerisch | Beute ist garantiert | **Beute hängt davon ab, wo dein Trupp stand** |
| Zone aus 14b | ohne Wirkung | **entscheidet mit** |

**Der Plan empfiehlt den zweiten Weg**, und zwar aus einem Grund, der nichts mit Python zu tun hat: Er macht die Zonen aus Etappe 14b zum ersten Mal zu einer **Entscheidung mit zwei Seiten.** Bisher war eine enge Zone einfach sicherer. Ab heute heißt eine enge Zone auch: Du siehst weniger von dem, was da draußen liegt.

**Die einfachste Form davon**, und sie reicht völlig — aber sie braucht drei genaue Angaben, sonst entsteht die Regel zufällig aus deinem Code:

> **Ein Fundstück wird eingesammelt, wenn seine Koordinate in der Zone mindestens eines Marines liegt, der noch steht.**

| Frage | Antwort |
|---|---|
| Reicht **eine** Zone, oder müssen es alle sein? | **eine** — die Zonen überlappen sich nicht, jede Stelle gehört höchstens einem |
| Sammelt ein **ausgefallener** Marine? | **nein** — er liegt selbst da draußen. `status` prüfen, wie seit Etappe 13 |
| **Wann** wird gesammelt? | siehe unten |

⚠️ **Und der Zeitpunkt ist keine Nebensache, sondern eine Phase in deiner Reihenfolge.** Fundstücke entstehen in der **Aufräumphase** aus Etappe 12 — dort fällt der Gegner. Eingesammelt wird **nach** der letzten Aufräumphase der Welle und **vor** dem Beginn der nächsten:

```
… Tick: Zähler → Trupp → Gegner → Aufräumen (hier entstehen Fundstücke)
Welle vorbei
→ Einsammeln
→ nächste Welle
```

**Steht das Einsammeln an der falschen Stelle, fehlt dir die Beute des letzten Ticks** — genau die vom letzten Gegner, also der interessantesten. **Trag die Phase in deine Reihenfolge-Notiz aus Etappe 12 ein.** In Etappe 16 ist das ein Beweismittel.

*(Kein Herumlaufen, kein Aufheben per Befehl, kein Tragelimit. Der Trupp geht nach der Welle raus und sammelt ein, was er erreichen konnte. Eine Schleife, zwei Prüfungen, fertig.)*

### 8. Vorwissen — eine Erkenntnis, die nur Text ändert

Nicht jede Erkenntnis muss eine Zahl verändern. **Die nützlichste Sorte verändert gar nichts am Spiel — nur, was der Spieler weiß:**

> *„Die Sporen tragen Chitin in einer zweiten Schicht. Was hier schlüpft, bringt Panzerung mit."*

Danach steht in deiner Wellenvorschau nicht mehr nur die Nummer, sondern ein Hinweis darauf, was kommt. **Nichts am Kampf ändert sich. Alles am Vorbereiten.**

**Das ist die billigste Wirkung im ganzen Spiel und oft die beste**, weil sie eine Entscheidung erzeugt, ohne eine Zahl anzufassen: Kaufst du jetzt panzerbrechende Munition oder sparst du weiter?

*(In Etappe 17a wird der Wellengenerator daraus richtig Kapital schlagen — wenn die Wellen nicht mehr fest sind, ist Vorwissen plötzlich wertvoll statt nett.)*

### 9. Erweitern, ohne zu zerstören ⭐⭐

**Das ist der Test dieser Etappe, und er ist der ehrlichste im ganzen Plan**, weil du ihn nicht bestehen *musst* — du sollst nur wissen, wie er ausgeht.

> **Bau einen vierten Fund ein. Zähl, wie viele Stellen du dafür anfassen musst.**

**Wenn es eine ist** — eine neue Zeile in deiner Tabelle — dann ist deine Struktur in Ordnung, und du hast etwas geschafft, das die meisten Programme nicht schaffen.

**Wenn es fünf sind** — Tabelle, Schadensfunktion, Depotfunktion, Analysebefehl, Anzeige —, dann ist das **eine Erkenntnis über deinen Code, nicht über dein Können.** Schreib die Zahl auf. In Etappe 22 machst du denselben Test noch einmal, und der Unterschied zwischen beiden Zahlen ist der eigentliche Fortschritt.

⚠️ **Und lass sie nicht künstlich klein werden.** Der Test ist nur etwas wert, wenn du ihn ehrlich machst — also den vierten Fund wirklich einbaust und wirklich zählst, statt zu schätzen, wie es ausgehen würde.

---

## Dein Auftrag

Nach **jedem** Schritt ausführen und eine Welle spielen.

---

### 1. Leg die Fundtabelle an

Ein Dictionary, oben in der Datei, mit **allen** Angaben zu einem Fund an einer Stelle:

| Schlüssel | Was drinsteht |
|---|---|
| Kennung, z. B. `"chitinprobe"` | ein Dictionary mit: |
| `"erkenntnis"` | das Wort, das ins Set kommt |
| `"text"` | was beim Analysieren ausgegeben wird — **schreib ihn wirklich** |

**Drei Funde reichen.** Der vierte kommt in Schritt 13, und das ist Absicht.

⚠️ **Das ist die eine Stelle, an der jedes Erkenntnis-Wort steht.** Ab hier tippst du keines mehr ab, sondern holst es aus dieser Tabelle. Konzept 1 sagt, warum.

**So prüfst du es:** `print(FUNDE["chitinprobe"]["erkenntnis"])` in einer Wegwerf-Datei.

---

### 2. Bau die Klasse `Fundstueck`

Nach Konzept 6: **erbt von `Item`** aus Etappe 11, bringt `x` und `y` mit, ruft `super().__init__()` zuerst auf. Kein Verhalten. Ein `__repr__` lohnt sich.

⚠️ **Sie erbt nicht von `Einheit`.** Ein Fundstück tickt nicht, hat keine Trefferpunkte und handelt nicht. Wer es in den `trupp` legt, bekommt beim nächsten Tick einen `AttributeError` — und zwar zu Recht.

**So prüfst du es:** Ein `Fundstueck` erzeugen und ins Inventar legen. Deine Inventaranzeige aus Etappe 11 zeigt es an, ohne dass du sie angefasst hast — **das ist der Beweis, dass es ein `Item` ist.**

---

### 3. Lass Gefallene etwas hinterlassen

- Eine Tabelle **Gegnertyp → Fundkennung**. Nicht jeder Typ muss etwas hinterlassen.
- In deiner Aufräumphase aus Etappe 12: Wer gerade gefallen ist, legt an **seiner** Koordinate ein `Fundstueck` in `welt.fundstuecke`.
- `.get()` für den Typ, `is None` für „hinterlässt nichts" — dann brauchst du keine Sonderbehandlung.

**So prüfst du es:** Eine Welle spielen, danach `print(welt.fundstuecke)`. Die Koordinaten müssen dort liegen, wo Gegner gefallen sind — nicht am Spawnpunkt.

---

### 4. Zeig die Fundstücke im Vorfeld an

Eine Zeile in `zeichne_vorfeld()` aus Etappe 14: ein eigenes Zeichen für ein Fundstück.

⚠️ **Reihenfolge beachten.** Male die Fundstücke **vor** den Einheiten, sonst verdeckt ein Fundstück deinen Marine. *(Und ja: Steht eine Einheit darauf, siehst du das Fundstück nicht mehr. Das ist derselbe Fall wie zwei Einheiten auf einem Feld aus Etappe 14 — bekannt und in Ordnung.)*

---

### 5. Bau die Einsammelphase

Nach Konzept 7 — **nach der letzten Aufräumphase der Welle, vor dem Beginn der nächsten.** Trag die Phase in deine Reihenfolge-Notiz aus Etappe 12 ein.

- Über `welt.fundstuecke` laufen.
- Liegt eines in der Zone eines Marines, der **nicht** auf `"tot"` steht: ins Inventar, aus der Liste entfernen.
- **Sammeln, dann entfernen** — der Griff aus Etappe 12, Konzept 11.
- Eine Meldung, was eingesammelt wurde, und **eine zweite, wie viel liegen blieb.**

⚠️ **Die zweite Meldung ist wichtiger als die erste.** *„Drei Fundstücke außerhalb deiner Zonen zurückgelassen"* ist der Satz, der deine Zonen zu einer echten Entscheidung macht. Ohne ihn merkt der Spieler nie, dass er etwas verpasst.

**So prüfst du es:** Eine Zone absichtlich winzig machen und eine Welle spielen. Es bleibt etwas liegen, und du erfährst davon.

---

### 6. Leg `welt.erkenntnisse` an

Ein leeres Set in `Welt.__init__`. Eine Zeile.

---

### 7. ⭐ Bau den Befehl `analysiere <kennung>`

Die Prüfkette, in dieser Reihenfolge — **erst alle Prüfungen, dann verändern**, wie seit Etappe 5:

```
Steht die Kennung in FUNDE?        →  nein: „Davon weißt du nichts."
Ist die Erkenntnis schon da?       →  ja:   „Das hast du bereits ausgewertet."
Hast du es im Inventar?            →  nein: „Das hast du nicht dabei."
── ab hier wird verändert ──
Erkenntnis ins Set
Text aus der Tabelle ausgeben
```

⚠️ **Die Reihenfolge der mittleren beiden ist nicht beliebig, und der Grund wird erst bei der nächsten Frage sichtbar.** Verbrauchst du das Fundstück beim Analysieren, ist es beim zweiten Versuch weg — dann würde eine Inventarprüfung an erster Stelle *„das hast du nicht dabei"* melden, obwohl die richtige Antwort *„das weißt du schon"* lautet. **So herum funktioniert die Kette in beiden Fällen.**

⚠️ **Die ersten beiden Meldungen müssen verschieden sein**, und zwar aus demselben Grund wie beim `bestiarium` in Etappe 6: *„gibt es nicht"* meint den Katalog, *„hast du nicht"* meint deinen Besitz. **Wer beide zusammenlegt, sagt dem Spieler, ein Gegenstand existiere nicht, den er nur nicht dabei hat.**

**Entscheide außerdem: Wird das Fundstück beim Analysieren verbraucht?** Beides ist vertretbar, und die Kette oben trägt beide.

*(Ein Argument für „ja", das du kennen solltest: Sonst füllt sich dein Inventar mit Dingen, deren einzige Aufgabe erledigt ist — Verwaltung ohne Zweck. Ein Argument für „nein": Ein Ausstellungsstück im Inventar ist ein Andenken, und das kostet nichts.)*

**So prüfst du es:** Vier Aufrufe — ein erfundenes Wort, ein echtes ohne Besitz, ein echtes mit Besitz, dasselbe noch einmal. **Vier verschiedene Ausgaben.**

---

### 8. Commit

Commit: `Etappe 15a: Fundstücke und Erkenntnisse`

> **⏸ Guter Schnitt.** Dein Spiel merkt sich etwas über eine Welle hinaus. Ab Schritt 9 fängt das Gemerkte an zu wirken — und das ist der schwierigere Teil.

---

### 9. ⭐⭐ Lass die Erkenntnis den Schaden verändern

Nach Konzept 4, mit der **Umkehrtabelle**:

- Eine Tabelle **Gegnertyp → nötige Erkenntnis**.
- In deiner `berechne_schaden()` aus Etappe 7: Nachschlagen mit `.get()`, prüfen mit `is not None` und `in`, Zuschlag draufrechnen.
- **Keine `if`-Kette mit Erkenntnis-Namen in der Funktion.** Das ist der ganze Punkt.

⚠️ **`berechne_schaden()` ist seit Etappe 7 deine sauberste Funktion.** Sie bekommt Werte und gibt eine Zahl zurück. **Gib ihr nicht die ganze Welt** — nur das Set. Ein Parameter mehr, und die Reinheit bleibt erhalten. *(Das ist die Kopplungsfrage aus Etappe 12 und 13, hier zum ersten Mal mit einer billigen Antwort.)*

**So prüfst du es:** Denselben Gegnertyp einmal vor und einmal nach dem Analysieren beschießen. **Die Zahl muss sich ändern — und bei einem anderen Typ nicht.**

---

### 10. Lass die Erkenntnis das Depot verändern

- Eine Tabelle **Ware → nötige Erkenntnis**.
- Im Depot: Waren ohne Eintrag sind immer da. Waren mit Eintrag nur, wenn die Erkenntnis vorliegt.
- **Sowohl die Anzeige als auch der Kauf** müssen das berücksichtigen.

⚠️ **Die zweite Hälfte wird vergessen, und sie ist die wichtige.** Wer nur die Anzeige filtert, kann eine unsichtbare Ware trotzdem kaufen, wenn er den Namen errät. **Prüf beides**, und probier es absichtlich aus.

**So prüfst du es:** Die neue Ware vor dem Analysieren kaufen wollen — abgewiesen. Danach — sie steht in der Liste und lässt sich kaufen.

---

### 11. Lass die Erkenntnis das Bestiarium verändern

- Wer einen Typ **analysiert** hat, liest im `bestiarium <kennung>` eine Zeile mehr als jemand, der ihn nur gesehen hat.
- **Fass die Logik von Etappe 6 nicht an.** Häng eine Zeile an, mehr nicht.

*(Damit hat dein Bestiarium drei Stufen: nie gesehen, gesehen, verstanden. Das ist Erzählung, die dich nichts kostet.)*

---

### 12. Bau das Vorwissen ein

Nach Konzept 8: Wer die Sporen ausgewertet hat, sieht in der Ankündigung der nächsten Welle einen Hinweis auf den Typ, der kommt.

*(Deine Wellentypen stehen seit Etappe 6 in einer `if`/`elif`-Kette. Du liest sie nur — du änderst sie nicht.)*

---

### 13. ⭐⭐ Der Test: bau einen vierten Fund ein

**Und zwar wirklich, nicht gedanklich.**

⚠️ **Der vierte Fund muss eine Wirkungsart benutzen, die es schon gibt** — noch ein Schadensbonus, noch eine Depotware, noch ein Vorwissen. **Sonst misst der Test etwas anderes, als er soll.** Ein Fund, der die Marines schneller macht, braucht zwangsläufig neue Logik; daran ist deine Struktur nicht schuld.

> **Neue Daten hinzufügen und eine neue Art von Verhalten hinzufügen sind zwei verschiedene Dinge.** Der Test fragt nur nach dem ersten.

**Zähl, wie viele Stellen du anfassen musstest, und schreib die Zahl in `GELERNT.md`.**

Danach, ehrlich beantwortet: **Welche dieser Stellen hättest du nicht anfassen müssen, wenn du es anders gebaut hättest?**

⚠️ **Wenn die Zahl hoch ist, reiß heute nichts ein.** Notier, was du ändern würdest, und lass es stehen. Etappe 22 ist der Ort dafür, und dort ist es eine Stunde Arbeit statt eines Abends.

---

### 14. Prüf, dass das Alte noch läuft, und commit

- Kaufen, nachladen, Sektor wechseln, Fähigkeit, Bestiarium, Turmbau, Räumen: alles wie vorher?
- Beide Verlustbedingungen?
- Ein voller Wellendurchgang ohne Absturz?

Commit: `Etappe 15b: Erkenntnisse wirken`

---

## ⭐ Die Kopplungszeichnung — fünf Minuten, ein Blatt Papier

**Das ist kein Auftragsschritt, sondern der bleibendste Teil dieser Etappe.** Du reparierst nichts. Du siehst nur hin.

Heute sind vier Systeme zusammengetroffen, die bisher nichts voneinander wussten. **Zeichne die Pfeile:**

```
Fundstück   →  Erkenntnis
Erkenntnis  →  Depot?
Erkenntnis  →  Schadensberechnung?
Erkenntnis  →  Bestiarium?
Erkenntnis  →  Wellenvorschau?
```

**Und dann die eigentliche Frage — und sie ist nicht die naheliegende.**

„Wo laufen die meisten Pfeile zusammen?" wäre zu billig. **Viele Pfeile aus einem zentralen Zustand heraus sind völlig in Ordnung**, solange sie nur *lesen*. Dein Set weiß über niemanden etwas; jeder darf hineinschauen.

> **Gefährlich wird es, wenn ein Pfeil zurückgeht.**

```
Fundstück  →  Erkenntnisse  →  Depot
     ↑                           │
     └───────────────────────────┘        ← das ist die Kopplung
```

**Frag dich also:** Zeigt irgendwo ein Pfeil in beide Richtungen? Und: **Was wäre problematisch, wenn das Fundstück selbst das Depot kennen müsste?**

🚨 **Nur bemerken, nichts reparieren.** Wenn irgendwo eine Zeile entstanden ist wie

```python
fundstueck.analysiere(welt.depot.sortiment, welt.trupp[0].schaden)
```

dann weiß diese eine Zeile sehr viel über sehr viele Teile deines Spiels. **Sie funktioniert.** Sie ist nur schwer zu ändern, weil jede dieser Ebenen sie brechen kann — und weil du sie nicht testen kannst, ohne ein halbes Spiel aufzubauen.

> **Der Begriff heißt Kopplung. Du kennst ihn seit Etappe 12, heute siehst du ihn zum ersten Mal als Bild.**

**Heb die Zeichnung auf.** Fotografier sie, leg sie ins Repo, schreib sie in `GELERNT.md` ab — egal wie. **In Etappe 23b machst du sie ein zweites Mal und vergleichst.** Das ist der einzige Grund, warum sie heute entsteht.

*(Und falls dein Bild langweilig aussieht — alle Pfeile gehen von einem Set aus, sonst nichts —: Das ist kein Versagen, sondern das beste mögliche Ergebnis. Ein Set weiß über niemanden etwas.)*

---

## Was NICHT in diese Etappe gehört

**Keine Reparatur der Kopplung.** Zeichnen, aufheben, weitergehen. Etappe 23b.

**Kein `Enum` für die Erkenntnis-Wörter.** Strings in einer Tabelle. Etappe 21b.

**Keine gewichtete Beute.** Ein Kriecher lässt immer dasselbe fallen. Dass seltene Dinge selten sein sollen, ist die offene Frage aus Etappe 4 — und sie wird in **Etappe 17a** beantwortet.

**Keine Erkenntnisse, die Fähigkeiten freischalten.** Voraussetzungen für Fähigkeiten sind Etappe 18, und sie benutzen genau dieses Set.

**Kein Herumlaufen, um Beute zu holen.** Einsammeln passiert am Wellenende, automatisch, nach Zone.

**Kein Tragelimit, kein Gewicht, kein Rucksack.** Dein Inventar ist eine Liste und bleibt es.

**Keine `dataclass`.** `Fundstueck` wird ausgeschrieben. Etappe 23b.

**Keine automatisierten Tests.** Schritt 13 ist ein Erweiterungs-**Experiment** von Hand, kein Test im technischen Sinn. Gewissheit über „erweitern ohne zu zerstören" gibt es erst in Etappe 26.

---

## Selbsttest

- [ ] Jedes Erkenntnis-Wort, das irgendwo verwendet wird, **existiert in der Fundtabelle** — kein Verweis ins Leere.
- [ ] Ein Fundstück ist ein `Item` und lässt sich mit `nimm` und `ablege` behandeln wie alles seit Etappe 11.
- [ ] Ein Fundstück in der Zone eines **ausgefallenen** Marines wird nicht eingesammelt.
- [ ] Das Einsammeln steht **nach** der letzten Aufräumphase — die Beute des letzten Gegners fehlt nicht.
- [ ] Ein Fundstück liegt dort, wo der Gegner gefallen ist, nicht am Spawnpunkt.
- [ ] Was außerhalb aller Zonen liegt, wird **nicht** eingesammelt — und du erfährst davon.
- [ ] `analysiere` hat vier verschiedene Ausgaben für vier verschiedene Lagen.
- [ ] Zweimal dasselbe analysieren ändert nichts und meldet es.
- [ ] Derselbe Gegnertyp nimmt nach dem Analysieren mehr Schaden, ein anderer nicht.
- [ ] Die neue Depotware lässt sich vorher **weder sehen noch kaufen** — beides geprüft.
- [ ] `berechne_schaden()` bekommt weiterhin keine ganze Welt.
- [ ] In `berechne_schaden()` steht kein einziges Erkenntnis-Wort.
- [ ] Ein Fundstück steht nicht im `trupp`.
- [ ] Der vierte Fund benutzt eine **vorhandene** Wirkungsart, und die Zahl aus Schritt 13 steht in `GELERNT.md`.
- [ ] Die Kopplungszeichnung existiert und ist aufgehoben.
- [ ] Beide Commits sind gesetzt.

---

## Lernziele

In `GELERNT.md`, ohne nachzuschlagen.

1. **Wo speicherst du eine Erkenntnis — beim Fundstück, beim Gegnertyp oder zentral? Was spricht wofür?**
2. Was passiert mit deinem Wissen, wenn du das analysierte Fundstück wegwirfst — und was sagt das über den richtigen Speicherort?
3. Warum ist „Erkenntnis vorhanden" ein Set und kein Dictionary aus Booleans? Nenn den Fall, den es beim Dictionary zusätzlich gibt.
4. Wie findest du in einer Liste von Objekten das erste, das eine Bedingung erfüllt — und was gibst du zurück, wenn keines passt?
5. **Warum steht die Zuordnung „Gegnertyp → nötige Erkenntnis" in einer Tabelle und nicht als `if`-Kette in der Schadensfunktion?**
6. **Kannst du einen Kriecher gesehen haben, ohne seinen Schwachpunkt zu kennen? Warum braucht das Spiel dafür zwei verschiedene Informationen — und wozu die dritte, `GEGNERTYPEN`?**
7. Was passiert, wenn du ein Erkenntnis-Wort an einer Stelle falsch schreibst — und warum ist das schlimmer als ein Absturz?
8. Welche drei Stufen durchläuft ein Fund, bis er wirkt?
9. Wie viele Stellen hat der vierte Fund gekostet — und welche davon waren vermeidbar?
10. Bei welchem Kästchen deiner Zeichnung laufen die meisten Pfeile zusammen?

**Frage 5 ist die wichtigste.** Sie ist der Unterschied zwischen einem Spiel, das man erweitern kann, und einem, das man umbauen muss.

**Frage 7 ist die, die dich am ehesten trifft.** Tippfehler in Strings sind die häufigste stille Fehlerquelle dieses Musters.

---

## Leseübung — Stufe 2 (15 Minuten)

**Du tippst nichts ab und führst nichts aus.** Auf Papier verfolgen.

```python
def dringendster_fall(akten):
    dringendster = akten[0]
    for akte in akten:
        if akte["tage"] > dringendster["tage"]:
            dringendster = akte
    return dringendster


def naechster_termin(akten, raum):
    for akte in akten:
        if akte["raum"] == raum:
            return akte["termin"]


akten = [
    {"name": "Behring", "tage": 4, "raum": "b", "termin": "09:00"},
    {"name": "Cordes",  "tage": 9, "raum": "a", "termin": "11:30"},
    {"name": "Adler",   "tage": 9, "raum": "b", "termin": "14:00"},
]

print(dringendster_fall(akten)["name"])
print(naechster_termin(akten, "a"))
print(naechster_termin(akten, "c"))
print(naechster_termin(akten, "c").split(":")[0])
```

**Die fünf Fragen:**

1. Was kommt rein?
2. Was passiert?
3. Was verändert sich — und woran?
4. Was kommt raus?
5. Welche anderen Funktionen werden aufgerufen?

**Und die vier, die zu dieser Etappe gehören:**

6. **Schreib die vier `print`-Ausgaben hin** — oder, wo es keine gibt, was stattdessen passiert.
7. **Unter welcher Bedingung stürzt `dringendster_fall()` ab?** Die Funktion nimmt etwas stillschweigend an. Was?
8. **Cordes und Adler haben beide neun Tage. Wer kommt zurück, und warum?** *(Dieselbe Frage wie die Achsenwahl in Etappe 14.)*
9. `naechster_termin()` hat kein `return` am Ende. **Was gibt sie zurück, wenn kein Raum passt — und in welcher Zeile merkst du es?**

⚠️ **Frage 9 ist der Kern.** Der Fehler passiert in der vorletzten Zeile, sichtbar wird er in der letzten. **Das ist genau die Entfernung, die eine Fehlersuche teuer macht** — und der Grund, warum Konzept 5 verlangt, `None` beim Aufrufer zu prüfen.

---

## Transferaufgabe (15 Minuten)

**Außerhalb des Spiels.** Ein Impfpass, kein Vorposten.

1. Ein Set `geimpft`, anfangs leer.
2. Eine Tabelle **Reiseziel → nötige Impfung**, drei Einträge. Ein viertes Ziel braucht keine.
3. Eine Funktion `darf_reisen(ziel, geimpft)`, die `True` oder `False` zurückgibt — nach dem Muster aus Konzept 4.
4. Vier Aufrufe, deren Ergebnis du **vorher aufschreibst**: ein Ziel mit Impfung, eines ohne, das Ziel ohne Anforderung, und ein Ziel, das gar nicht in der Tabelle steht.

**Und dann der eigentliche Teil:**

5. **Füg ein fünftes Reiseziel hinzu.** Wie viele Zeilen musstest du anfassen?
6. **Bau dieselbe Funktion noch einmal als `if`-Kette**, ohne Tabelle. Füg wieder ein Ziel hinzu und zähl erneut.

**Schritt 6 ist der Kern.** Es ist Konzept 4 an einem Beispiel, das in zehn Minuten fertig ist — und der Zahlenunterschied ist das ganze Argument.

---

## Kaputtmachen

**Vor jedem Experiment aufschreiben, was passieren wird.** Die ersten drei gehören dazu, die letzten zwei sind Kür.

**1. ⭐⭐ Vertipp dich absichtlich in einem Erkenntnis-Wort.** Schreib beim `add()` `"schwachpunkt_kricher"` und lass die Abfrage richtig. Spiel eine Welle, analysiere, schieß. **Was passiert — und woran hättest du es gemerkt?** Das ist ein Typ-3-Fehler in Reinform: kein Absturz, keine Meldung, und die Erkenntnis wirkt einfach nicht.

**2. ⭐ Leg Erkenntnis und Besitz zusammen.** Setz die Erkenntnis schon beim Aufsammeln, nicht beim Analysieren. Spiel eine Welle. **Was hast du dem Spieler damit weggenommen?** *(Die Antwort ist keine technische.)*

**3. Filtere nur die Anzeige.** Nimm die Prüfung aus dem Kaufvorgang heraus und lass sie in der Liste. Versuch, die versteckte Ware mit ihrem Namen zu kaufen. **Das ist kein erfundenes Szenario** — es ist eine der häufigsten echten Sicherheitslücken überhaupt, in klein.

---

Die folgenden zwei sind Kür.

**4. Analysiere etwas, das du nicht hast.** Nimm die Inventarprüfung aus Schritt 7 heraus. Kannst du jetzt jede Erkenntnis bekommen, ohne je einen Gegner erlegt zu haben?

**5. Mach alle Zonen winzig.** Setz jede Truppzone auf ein einziges Feld und spiel drei Wellen. Wie viel bleibt liegen — und würdest du als Spieler die Zonen danach anders setzen?

---

**Experiment 1 und 3 sind das Paar.** Beide stürzen nicht ab, beide sehen nach funktionierendem Code aus, und beide machen das Spiel kaputt — das eine, weil eine Regel nie greift, das andere, weil sie sich umgehen lässt.

Alles in `GELERNT.md` und ins Fehlertagebuch aus Etappe 8: **woran du es erkannt hättest.**

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| Die Erkenntnis wirkt nicht | Tippfehler im Wort — an einer der beiden Stellen | Konzept 1 — jedes Wort **einmal** in der Tabelle |
| `KeyError: 'chitinprobe'` | Direkter Zugriff statt `.get()` auf einen Typ ohne Beute | Schritt 3 — `.get()` und `is None` |
| `AttributeError: 'NoneType' object has no attribute ...` | Der Rückgabewert einer Suche wurde nicht geprüft | Konzept 5 — jede Suche kann `None` liefern |
| Fundstücke liegen alle am selben Ort | Die Koordinate des Gefallenen wurde nicht mitgegeben | Schritt 3 — `g.x`, `g.y`, nicht der Spawnpunkt |
| Beim zweiten Analysieren kommt der Text noch einmal | Die Prüfung „schon vorhanden" fehlt | Schritt 7 — dritte Zeile der Kette |
| Die versteckte Ware lässt sich kaufen | Nur die Anzeige filtert, der Kauf nicht | Schritt 10 — beide Stellen |
| Jeder neue Fund kostet fünf Änderungen | Die Wirkung steht als `if`-Kette in der Logik | Konzept 4 — Umkehrtabelle |
| Das Fundstück verschwindet beim Zeichnen | Es wird nach den Einheiten gemalt und überdeckt | Schritt 4 — Reihenfolge |
| `AttributeError: 'Fundstueck' object has no attribute 'update'` | Es liegt im `trupp` | Schritt 2 — es ist keine Einheit |
| Nach dem Einsammeln ist die Hälfte noch da | Entfernen während der Schleife | Etappe 12, Konzept 11 |

**Der Debugging-Reflex dieser Etappe: „Steht das Wort wirklich zweimal gleich da?"**

Etappe 12 fragte *in welchem Tick*, 13 *wie oft*, 14 *wo*. Heute ist die Frage die banalste und die häufigste:

```python
print(welt.erkenntnisse)
```

**Eine Zeile, und du siehst, was tatsächlich im Set steht** — statt dessen, was du glaubst, hineingeschrieben zu haben. Bei Mustern, die über Wörter laufen, ist das der schnellste Weg zur Wahrheit.

---

## Ein Blick nach vorne

**Etappe 16 ist die Bug-Jagd II** — und die Kandidaten von heute sind erstklassig, weil keiner von ihnen abstürzt.

**Etappe 17a baut den Wellengenerator.** Dann sind die Wellen nicht mehr fest, und dein Vorwissen aus Konzept 8 wird von einer netten Zeile zu einem echten Vorteil. **Dort wird auch die Frage aus Etappe 4 beantwortet**, warum ein Datenkern genauso oft fällt wie ein Chitinpanzer.

**Etappe 17b lässt einen Sektor fallen** — und welcher es ist, hängt unter anderem davon ab, was du weißt.

**Etappe 18 gibt Fähigkeiten Voraussetzungen**, und die werden gegen genau dieses Set geprüft. Dein `erkenntnisse` wird dort zum zentralen Gedächtnis des Spielstands.

**Etappe 19 speichert es.** Ein Set überlebt den Weg durch JSON nicht — das steht seit Etappe 6 als Schuld im Bogen, und dein wichtigstes Gedächtnis ist genau so eines.

**Etappe 21b gibt Gegnern Widerstände**, und die Schwachpunkt-Tabelle von heute wird Teil der Kampfformel.

**Etappe 22 macht den Test aus Schritt 13 noch einmal.** Die Zahl, die du heute aufschreibst, ist die Vergleichszahl.

**Etappe 23b zeichnet die Kopplung ein zweites Mal** — und dann hast du Werkzeuge, die heute noch fehlen.

---

## Abschluss

**In `GELERNT.md`:**

- ⭐ Meine Entscheidung: Wo wohnt eine Erkenntnis, und warum nicht bei `GEGNERTYPEN`?
- ⭐⭐ **Die Zahl aus Schritt 13** — und welche der Stellen vermeidbar waren.
- Meine Entscheidung: Wird das Fundstück beim Analysieren verbraucht?
- Die Kopplungszeichnung, oder wo sie liegt.
- Was hat mich überrascht? *(Kandidaten: dass ein Tippfehler nichts anzeigt · dass die Zone plötzlich zwei Seiten hat · wie wenig Code eine Verzahnung braucht.)*
- Offener Posten, falls du ihn hast: Was fehlt den Erkenntnissen noch, damit sie sich lohnen?

**Vor dem Commit:** Beide Verlustbedingungen geprüft? `berechne_schaden()` noch ohne Welt? Kein `breakpoint()` drin?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest.

**Gib jedem Fund eine Zeile im Inventar, die sagt, ob er ausgewertet ist.** Zwei Zeichen hinter dem Namen. Dann sieht der Spieler auf einen Blick, was noch Arbeit ist — und du siehst beim Debuggen dasselbe.

**Bau einen Fund, der nichts bewirkt.** Ein Fragment ohne Wirkung, das sich analysieren lässt und nur einen Satz ausgibt. **Das ist derselbe Trick wie der Datenkern in Etappe 4** — und es ist der billigste Weg, ein Spiel größer wirken zu lassen, als es ist. Löse ihn irgendwann auf. Oder nie.

**Zähl, wie viele Wörter in deinem Set landen können.** Wenn es mehr als zehn sind, schreib sie untereinander und sieh dir an, ob du für alle eine Tabelle hast oder für manche eine `if`-Kette. **Das ist der Test aus Schritt 13, nur billiger.**

**Such in fremdem Code nach `set()` und `.add(`.** Du wirst genau dieses Muster finden — Flags, Berechtigungen, gesehene IDs, erledigte Aufgaben. Jetzt weißt du, warum es ein Set ist und kein Dictionary.

---

> **Nächste Etappe:** [Etappe 16 — Bug-Jagd II](etappe-16-bug-jagd-ii.md) · vier Fehler, die nicht abstürzen, und du hast sie alle selbst gebaut
