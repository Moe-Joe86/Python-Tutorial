# Etappe 14 — Das Vorfeld

*v1.1.1 · 2026-09-16*

> **Block 2: Einheiten und Zeit** · Etappe 14 von 30 · [← Etappe 13](etappe-13-bauzeit-und-abklingzeit.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 15 →](etappe-15-was-die-brut-hinterlaesst.md)

**Neue Syntax heute:** Eine Liste, deren Einträge Listen sind · `raster[y][x]` lesend und schreibend · die Doppelschleife über zwei `range(len(...))` · `abs()` · die Randprüfung · ein Set aus Tuples · 👀 `enumerate()` und die drei Schleifenformen

**Zeitaufwand:** 14a: 4–5 Sitzungen · 14b: 4–5 Sitzungen · 14c: 2 Sitzungen, à 20–30 Minuten. Rund 43 Minuten Lesestoff, verteilt auf drei Portionen — lies jeweils nur die, an der du sitzt.

⚠️ **Das ist die am stärksten geteilte Etappe des Plans, und der Grund ist inhaltlich, nicht mengenmäßig.** 14a ist reine Python-Arbeit an einer Datenstruktur — du lernst verschachtelte Listen und sonst nichts. 14b baut darauf Spielmechanik. **Wer beides an einem Abend mischt, lernt weder das eine noch das andere**, weil bei jedem Fehler unklar bleibt, ob die Datenstruktur oder die Spielregel schuld ist.

**Voraussetzung:** Etappe 13 abgeschlossen, Selbsttest grün. Dein Tick läuft, Zähler laufen herunter, deine Gegner sind Objekte mit einer `entfernung`. **Genau diese `entfernung` ist es, die heute stirbt.**

**Die drei Portionen:**

| | Was passiert | Was danach anders ist |
|---|---|---|
| **14a** | Aus einer Zeile wird ein Feld | Deine Gegner haben `(x, y)` statt einer Zahl, und du siehst, wo sie stehen |
| **14b** | Auf dem Feld wird gerechnet | Reichweite deckt Felder ab, und dein Trupp läuft los |
| **14c** | Ein Gegenstand steht im Weg | Du triffst zum ersten Mal eine **räumliche** Entscheidung |

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **14a** | Das Raster · `vorfeld[y][x]` · Randprüfung · Gegnerbewegung · `zeichne_vorfeld()` | Warum hier ein Raster passt und bei den Sektoren ein Dictionary · Koordinate gegen Feldinhalt | `enumerate()` und die drei Schleifenformen |
| **14b** | `abs()` · Abstand · Reichweite als Set von Tuples · Zone · Trupp-KI Stufe 2 | Warum ein Set und keine Liste · warum Abstand und Bewegung zusammenpassen müssen | — |
| **14c** | Barrikade als Ware, auf ein Feld gesetzt | Dieselbe Prüfung zum dritten Mal | — |

⚠️ **14c ist Kür**, und sie hat zwei Stufen. **Schritt 17 und 18** — kaufen und hinstellen — lehren nichts Neues; sie zeigen, dass du eine Prüfkette schon beherrschst. **Schritt 19** — zerstörbare Barrikaden — ist etwas anderes: Dort steckt eine echte Datenmodellierungsentscheidung, und der darf entfallen. Wenn 14b sich zieht, lass 14c ganz weg.

---

## Worum es geht

Seit Etappe 3c hat dein Spiel eine Anmarschbahn. Sie ist **eine Zeile**:

```
[ . . K . . . @ ]
```

Ein Gegner ist eine Zahl — `entfernung = 4` —, und diese Zahl sinkt, bis sie null ist. Das hat elf Etappen lang getragen und ist erstaunlich weit gekommen: Wellen, Objekte, ein Tick, ein Turm.

**Aber es gibt genau eine Frage, die diese Zahl nicht beantworten kann:**

> **Wo steht er?**

Nicht *wie weit weg*, sondern **wo**. Und daran hängt alles, was ein Taktikspiel ausmacht: Zwei Gegner können gleich weit weg sein und trotzdem an völlig verschiedenen Stellen stehen. Ein Marine kann einen davon decken und den anderen nicht. Eine Wand kann dazwischen sein. Ein Weg kann sich verlegen lassen.

**Heute bekommt dein Vorfeld eine zweite Dimension.** Aus der Zeile wird ein Feld:

```
#######
#.....#
#.##..#
#..K..#
#S...@#
#######
```

Und aus `entfernung = 4` wird `(3, 3)`.

**Das ist derselbe Schritt, den du in Etappe 5 mit den Sektoren gemacht hast** — aus einem Ort wurden viele —, nur eine Ebene tiefer. Und der einzige wirklich neue Python-Gedanke **in 14a** ist klein: **eine Liste, deren Einträge selbst Listen sind.** *(14b bringt dann mehr — Abstandsrechnung, Mengen von Koordinaten, eine Suche. Aber nicht heute.)*

Alles andere kannst du längst. Du zeichnest seit Etappe 4 mit `.join()`, du läufst seit Etappe 3 mit `range()`, du kennst Tuples seit Etappe 6, Sets seit Etappe 6, und seit Etappe 10 weißt du, was passiert, wenn zwei Namen auf dasselbe Objekt zeigen. **Heute treffen sich diese fünf Dinge an einer Stelle.**

---

## Der lange Bogen — was heute fällig wird

- **Die größte Schuld des ganzen Plans wird eingelöst:** *„Aus einer Zeile werden viele."* Sie steht seit Etappe 4 offen, und der Guide von damals hat dir gesagt, dass es so kommt.
- **Das Tuple aus Etappe 6** war ein Werkzeug ohne Zweck. In Etappe 10 bekam dein Marine ein `self.position = (0, 0)`, ausdrücklich ohne Bewegung. **Heute ist es endlich das, wofür es gemacht ist.**
- **Das Set aus Etappe 6** zahlt sich in 14b zum ersten Mal richtig aus — bei einer Frage, die mit einer Liste umständlich und mit einem Set trivial ist.
- **`range(len(...))` aus Etappe 4** — die Regel lautete: *nur bei echtem Indexbedarf.* Heute ist der Bedarf echt, zum ersten Mal.
- **`[["."] * 5] * 5`** bringt den Fehler aus Etappe 4 und 10 in seiner gemeinsten Form zurück: *zwei Namen, ein Objekt* — nur dass es diesmal fünf Namen sind und du es erst beim Zeichnen merkst.
- **`zeichne_bahn()` aus Etappe 7b** wird zu `zeichne_vorfeld()`. Die Schicht, die du damals gezogen hast, hält — du tauschst eine Funktion aus, nicht das Spiel.
- **Die Design-Entscheidung aus Etappe 3c** — *ist die Bahn der Zustand oder nur sein Bild?* — wird heute endgültig fällig. Wer sie damals falsch beantwortet hat, merkt es heute.

---

## Zwei Riegel, bevor du anfängst

### ⚠️ Riegel 1: Heute gibt es keine Wegfindung

Kein A\*, kein Dijkstra, keine Breitensuche. **Deine Gegner gehen den direkten Weg** — einen Schritt pro Tick, in Richtung Tor. Steht eine Wand davor, bleiben sie stehen.

**Der Reflex „Wände plus Bewegung, also brauche ich jetzt Wegfindung" ist verständlich und die teuerste Abzweigung in diesem ganzen Plan.** Wegfindung ist ein schönes Thema. Sie ist Informatik statt Python, sie kostet dich zwei Wochen, und sie kostet sie dir an genau der Stelle, an der du gerade verschachtelte Listen lernen wolltest.

**Notier sie in `GELERNT.md` als Idee für nach Etappe 27.** Dann gehört das Spiel dir, du hast Tests, und es ist ein wunderbares Wochenendprojekt.

*(Und der billige Ausweg ist vollkommen legitim: Bau keine Wände dorthin, wo sie jemanden festsetzen. Ein Vorfeld, das den direkten Weg offen lässt, braucht keine Wegfindung.)*

### ⚠️ Riegel 2: Das Raster hält Gelände, keine Einheiten

Diese Entscheidung ist so wichtig, dass sie vor die Konzepte gehört.

> **Im Raster stehen Wände, offene Felder, das Tor und der Spawnpunkt. Einheiten stehen nicht darin. Sie haben eigene Koordinaten.**

Die Versuchung ist groß, den Gegner ins Raster zu schreiben — `vorfeld[y][x] = "K"` — und fertig. **Das rächt sich innerhalb einer Etappe**, und zwar dreifach:

| | Gegner im Raster | Gegner mit eigenen Koordinaten |
|---|---|---|
| Zwei Gegner auf einem Feld | geht nicht | geht |
| Was steht unter dem Gegner? | verloren — das Feld hieß mal `.` | steht noch im Raster |
| Trefferpunkte des Gegners | wo? Ein `"K"` hat keine | im Objekt, wo sie seit Etappe 11 sind |

**Das ist die Design-Entscheidung aus Etappe 3c, zum dritten Mal:** *Positionen sind der Zustand, das Zeichen ist nur sein Bild.* Du hast sie damals getroffen, in Etappe 12 hat sie den Tick getragen, und heute trägt sie das Raster.

---

# Teil 14a — Das Raster

## Die Konzepte — Teil 14a

Alle Beispiele laufen **außerhalb** deines Spiels. Heute in einem Parkhaus.

*(Zwei Wörter, damit sie nicht durcheinandergeraten: **Raster** ist die Datenstruktur allgemein — eine Liste von Listen. **`vorfeld`** ist dein konkretes Raster im Spiel. In den Beispielen unten heißt es `ebene`, weil ein Parkhaus kein Vorfeld hat.)*

### 1. Eine Liste, deren Einträge Listen sind ⭐

Du kennst Listen seit Etappe 4. Das hier ist nichts Neues, sondern dasselbe zweimal:

```python
ebene = [
    ["frei", "belegt", "frei"],
    ["belegt", "belegt", "frei"],
    ["frei", "frei", "frei"],
]
```

`ebene` ist eine Liste mit **drei** Einträgen. Jeder dieser Einträge ist selbst eine Liste mit drei Einträgen.

**Prüf das nach, statt es zu glauben:**

```python
print(len(ebene))        # 3   — drei Reihen
print(ebene[0])          # ['frei', 'belegt', 'frei']   — eine ganze Reihe
print(len(ebene[0]))     # 3   — drei Plätze in dieser Reihe
```

> **`ebene[0]` ist keine Zelle. Es ist eine ganze Zeile.** Das ist der Gedanke, an dem sich alles Weitere entscheidet.

### 2. `raster[y][x]` — Zeile vor Spalte ⭐⭐

Wenn `ebene[0]` eine ganze Zeile ist, dann ist `ebene[0][2]` der dritte Platz in dieser Zeile:

```python
print(ebene[1][2])       # 'frei'
ebene[1][2] = "belegt"
```

**Zwei Klammern hintereinander: Erst die Zeile, dann die Spalte.** Von außen nach innen, genau wie bei `d[a][b]` in deinem Sektoren-Dictionary seit Etappe 5.

⚠️ **Und jetzt die Stelle, an der jeder mindestens einmal stolpert.** Wir sind es gewohnt, Koordinaten als *x, y* zu sagen — erst waagerecht, dann senkrecht. Eine Liste von Listen ist andersherum aufgebaut: erst die Zeile, also **y**, dann die Spalte, also **x**.

```python
ebene[y][x]      # richtig
ebene[x][y]      # läuft oft trotzdem — und liefert das falsche Feld
```

**Das Gemeine daran:** Bei einem quadratischen Raster stürzt die falsche Reihenfolge **nicht ab**. Sie liefert einfach ein anderes Feld. Dein Gegner steht dann gespiegelt an der Diagonalen, und du suchst den Fehler in der Bewegungslogik.

> **Deshalb steht es hier so groß: `raster[y][x]`. Schreib es dir an den Bildschirmrand.**

*(Ein Trost: Es gibt keinen tiefen Grund dafür. Es ist reine Folge davon, dass die äußere Liste die Zeilen hält. Wer das Raster als Liste von Spalten baut, hat `raster[x][y]` — und niemand tut das, weil man ein Raster zeilenweise hinschreibt und zeilenweise ausgibt.)*

### 3. Das Raster bauen — und die Falle dabei ⭐

Für ein kleines, festes Gelände schreibst du es einfach hin, so wie oben. **Das ist kein Provisorium**, sondern die richtige Lösung für eine Karte, die im Code steht. *(In Etappe 25 wandert sie in eine Datei.)*

Willst du es **erzeugen**, etwa weil es fünfzehn mal fünfzehn groß ist, dann so:

```python
ebene = []
for y in range(3):
    zeile = []
    for x in range(3):
        zeile.append("frei")
    ebene.append(zeile)
```

Umständlich? Ja. **Und jetzt die Abkürzung, die alle zuerst probieren:**

```python
ebene = [["frei"] * 3] * 3       # ⚠️
ebene[0][0] = "belegt"
```

**Sag voraus, bevor du weiterliest:** Wie viele Plätze stehen danach auf `"belegt"`?

**Drei.** Alle drei Zeilen zeigen dasselbe an:

```
['belegt', 'frei', 'frei']
['belegt', 'frei', 'frei']
['belegt', 'frei', 'frei']
```

> **`* 3` legt keine drei Listen an. Es legt eine Liste an und schreibt sie dreimal hin.** Drei Namen, ein Objekt — der Fehler aus Etappe 4 und Etappe 10, in seiner unangenehmsten Form.

⚠️ **Das Innere ist übrigens harmlos.** `["frei"] * 3` erzeugt drei Strings nebeneinander, und Strings lassen sich nicht ändern — da kann nichts geteilt kaputtgehen. **Die äußere Vervielfachung ist das Problem**, weil Listen *mutable* sind. Genau die Unterscheidung aus Etappe 6, an einem Fall, der weh tut.

**Der Reflex dazu kennst du seit Etappe 10:**

```
(Pdb) p ebene[0] is ebene[1]     → True bedeutet: dieselbe Zeile, nicht zwei gleiche
```

### 4. Die Doppelschleife

Über ein Raster läuft man mit zwei Schleifen ineinander — die äußere über die Zeilen, die innere über die Spalten:

```python
for y in range(len(ebene)):
    for x in range(len(ebene[y])):
        print(y, x, ebene[y][x])
```

**Drei Dinge, die dabei zählen:**

- Die äußere Schleifenvariable heißt `y`, weil sie die Zeile wählt. Die innere heißt `x`. **Nennst du sie `i` und `j`, verwechselst du sie innerhalb einer Woche.**
- `len(ebene[y])` statt `len(ebene[0])` — fragt die Zeile, in der du gerade bist. Bei einem rechteckigen Raster ist das dasselbe; bei einem, das es versehentlich nicht mehr ist, findest du den Fehler dadurch.
- **Hier ist der Indexbedarf zum ersten Mal echt.** Etappe 4 hat dir gesagt, `range(len(...))` nur zu nehmen, wenn du die Stelle wirklich brauchst. Beim Raster brauchst du sie: `(x, y)` **ist** die Information.

👀 **Die drei Schleifenformen — zwei Minuten, kein Umbau.** Diese drei machen einen erheblichen Teil aller Schleifen aus, die dir je in fremdem Python begegnen. Sag dir zu jeder einen Satz, was in den Schleifenvariablen steht:

```python
for zeile in ebene:                      # ?
for y, zeile in enumerate(ebene):        # ?
for name, wert in daten.items():         # ?
```

`enumerate()` gibt dir Stelle **und** Wert auf einmal. Beim Raster ist `range(len(...))` völlig in Ordnung, und du schreibst heute nichts um — **aber wer die drei Formen verwechselt, liest ein fremdes Programm falsch, ohne es zu merken.**

### 5. Die Randprüfung — und der stille Fehler dahinter ⭐⭐

Etwas bewegt sich auf ein Feld zu. Liegt dieses Feld überhaupt auf dem Raster?

Die Prüfung ist unspektakulär:

```python
def liegt_drauf(ebene, x, y):
    if y < 0 or y >= len(ebene):
        return False
    if x < 0 or x >= len(ebene[y]):
        return False
    return True
```

**Und jetzt der Grund, warum sie nicht optional ist.** Was passiert ohne sie?

```python
ebene = [
    ["#", "#", "#"],
    ["#", ".", "#"],
    ["#", "X", "#"],
]
print(ebene[1][-1])
```

**Sag voraus.** Ein Index von `-1` müsste doch ein Fehler sein?

**Er ist keiner.** Es kommt `"#"` heraus — **der letzte Eintrag der Zeile.** Etappe 4 hat dir `liste[-1]` beigebracht, um bequem an das letzte Element zu kommen. Genau diese Bequemlichkeit schlägt hier zu:

> **Ein Gegner, der bei `x = -1` landet, stürzt nicht ab. Er taucht am rechten Rand wieder auf.**

Das ist einer der schönsten Typ-3-Fehler der Sprache: kein Traceback, keine Meldung, und dein Gegner ist auf der anderen Seite der Karte. **Am oberen Rand knallt es dagegen** — `y >= len(ebene)` gibt einen `IndexError`. Dieselbe Sorte Fehler, zwei völlig verschiedene Symptome, je nachdem, in welche Richtung du danebengreifst.

⚠️ **`>= len(...)`, nicht `> len(...)`.** Bei drei Zeilen sind die gültigen Indizes `0`, `1`, `2` — `3` ist schon zu viel. Das ist die Index-ab-null-Regel aus Etappe 3a, an der Stelle, an der sie das dritte Mal beißt.

### 6. Koordinate ist nicht Feldinhalt

Zwei Dinge, die man leicht in einen Topf wirft:

| | Was es ist | Wo es wohnt |
|---|---|---|
| `(3, 4)` | eine **Adresse** | im Objekt, das dort steht |
| `"#"` | was an dieser Adresse **liegt** | im Raster |

Ein Gegner *hat* eine Koordinate. Er *ist* kein Rasterfeld. Das Raster weiß nicht, dass er da ist — und genau deshalb kann unter ihm ein `.` liegen, das nach seinem Tod wieder sichtbar wird.

*(Das ist die Einlösung aus Etappe 5: „Richtung ≠ Ziel ≠ Standort" — drei Werte, die man leicht verwechselt. Heute kommt ein vierter dazu: der Feldinhalt.)*

### 7. Raster oder Dictionary? Die Modellierungsfrage ⭐

Deine Sektoren aus Etappe 5 sind ein Dictionary. Dein Vorfeld wird ein Raster. **Beide sind Karten. Warum zwei verschiedene Strukturen?**

| | Sektoren (Etappe 5) | Vorfeld (heute) |
|---|---|---|
| Wie viele? | eine Handvoll | Dutzende bis Hunderte Felder |
| Wie benannt? | `"nordtor"` — jedes hat Charakter | `(4, 2)` — reine Adresse |
| Was macht man damit? | nachschlagen, was dort ist | rechnen: Abstände, Wege, Reichweiten |
| Passende Struktur | **Dictionary** | **Raster** |

> **Wenige benannte Dinge mit Eigenschaften → Dictionary. Viele gleichartige Zellen, auf denen gerechnet wird → Raster.**

**Die Gegenprobe macht es deutlich.** Wer das Vorfeld als Dictionary baut — `{"4,2": "#"}` —, kann keinen Abstand ausrechnen, ohne den Schlüssel wieder zu zerlegen. Wer die Sektoren als Raster baut, hat ein Feld namens `(0, 3)`, dem man nicht ansieht, dass es das Depot ist.

**Zu wissen, wann welche Struktur passt, trennt Anfänger von Fortgeschrittenen** — und du hast ab heute beide im selben Programm und kannst sie vergleichen. Das ist eine seltene Gelegenheit; die meisten lernen nur eine und halten sie für die Lösung.

### 8. Gezeichnet wird eine Kopie ⭐

Das Raster hält Gelände, die Einheiten stehen woanders (Riegel 2). Zum Zeichnen müssen beide zusammenkommen — **aber nicht im Raster**:

```python
def zeichne(ebene, autos):
    bild = []
    for zeile in ebene:
        bild.append(zeile.copy())
    for a in autos:
        bild[a.y][a.x] = "A"
    for zeile in bild:
        print("".join(zeile))
```

**Drei Zeilen, die zusammengehören, und jede hat einen Grund:**

- `bild = []` und dann Zeile für Zeile — ein frisches Bild, jedes Mal. Das ist die Regel aus Etappe 3c: *die Bahn wird neu erzeugt, nicht verändert.*
- **`zeile.copy()`, nicht `zeile`.** Ohne die Kopie schreibst du das `"A"` in dein echtes Gelände, und beim nächsten Zeichnen steht es immer noch da. Ein Auto, das eine Spur aus Autos hinterlässt.
- `"".join(zeile)` — seit Etappe 4, unverändert.

⚠️ **Und der Grund, warum eine Kopie der äußeren Liste nicht reicht.** `ebene.copy()` legt eine neue äußere Liste an — die **Zeilen darin sind aber dieselben Objekte.** Du müsstest also trotzdem jede Zeile einzeln kopieren. Das ist derselbe Gedanke wie bei `* 3` in Konzept 3, von der anderen Seite. *(Der Fachbegriff für dieses „nur die oberste Ebene" ist **flache Kopie**. Mehr brauchst du davon heute nicht.)*

---

## Dein Auftrag — Teil 14a

⚠️ **Heute gibt es keinen `diff`-Beweis.** Das Verhalten ändert sich absichtlich und sichtbar — die Anmarschbahn verschwindet. `befehle.txt` bleibt trotzdem nützlich: als schneller Durchlauf, der zeigt, dass nichts abstürzt.

Nach **jedem** Schritt ausführen und einen Tick auslösen.

---

### 1. Leg das Vorfeld in der Welt an

- Attribut `vorfeld` in `Welt.__init__`, als Liste von Listen, **hingeschrieben** wie in Konzept 1.
- Größe: klein anfangen. **Sieben Spalten, sechs Zeilen reichen.**
- Zeichen: `#` Wand, `.` frei, `@` dein Tor, `S` der Spawnpunkt der Brut.
- Zweites Attribut `tor` als Tuple `(x, y)` — die Koordinate deines Tors.
- Rundherum eine geschlossene Wand aus `#`.

⚠️ **Lass zwischen `S` und `@` einen Weg frei, auf dem niemand hängenbleibt.** Riegel 1 — es gibt keine Wegfindung, und ein Gegner vor einer Wand bleibt einfach stehen.

**So prüfst du es:** In einer Wegwerf-Datei `print(len(welt.vorfeld))` und `print(len(welt.vorfeld[0]))`. Sechs und sieben. Und `print(welt.vorfeld[0])` gibt eine **ganze Zeile** aus, kein einzelnes Zeichen.

---

### 2. Bau `welt.ist_auf_dem_raster(x, y)`

Nach Konzept 5. Gibt `True` oder `False` zurück, verändert nichts.

**So prüfst du es:** Vier Aufrufe, deren Antwort du vorher aufschreibst — ein Feld mittendrin, `(-1, 2)`, `(0, -1)`, und ein Feld genau einen Schritt hinter dem rechten Rand. **Alle vier müssen so ausgehen, wie du es aufgeschrieben hast.**

---

### 3. Bau `welt.ist_frei(x, y)`

- Liegt die Koordinate nicht auf dem Raster: `False`.
- Sonst: `True`, wenn dort **keine** Wand steht.

⚠️ **Erst die Randprüfung, dann der Zugriff.** Andersherum greifst du auf ein Feld zu, bevor du weißt, ob es existiert — und bei `x = -1` bekommst du still das falsche.

**So prüfst du es:** `ist_frei` auf ein Wandfeld, auf ein freies Feld und auf `(-1, 1)`. Dreimal die erwartete Antwort.

---

### 4. ⭐⭐ Zieh `entfernung` um: aus einer Zahl werden zwei

**Das ist der Auftragsschritt dieser Portion.** Rechne mit einem halben Abend.

- `Gegner.__init__` bekommt `x` und `y` statt `entfernung`.
- Ein neuer Gegner entsteht auf dem Spawnpunkt.
- **Fahndung, wie seit Etappe 5:** Such alle Stellen, an denen `entfernung` vorkommt, zähl sie und schreib die Zahl auf. Es sind mehr, als du denkst — Bewegung, Zielsuche, Reichweitenprüfung des Turms und der Kameraden, die Anmarschbahn, vermutlich die Statusanzeige.
- Arbeite eine Stelle nach der anderen ab.

⚠️ **Das Spiel ist zwischendurch kaputt, und das ist normal.** Ein `AttributeError: 'Gegner' object has no attribute 'entfernung'` ist der freundliche Fall — er zeigt dir die nächste Stelle. Arbeite dich an ihnen entlang.

**So prüfst du es:** Kein `AttributeError` mehr. Das Wort `entfernung` kommt in deinem Code nicht mehr vor — such danach.

---

### 5. Lass die Gegner einen Schritt gehen

In `Gegner.update()`, anstelle des bisherigen `entfernung -= 1`:

- Steht der Gegner schon auf dem Tor: Schaden auf `kern_integritaet`, wie bisher.
- Sonst: **ein** Schritt in Richtung Tor.
- Die Richtung entscheidest du pro Achse mit einem Vergleich — größer, kleiner, gleich. *(Drei Zeilen. Es gibt in Python einen kürzeren Weg, ihn kennst du noch nicht, und du brauchst ihn nicht.)*
- **Nur wenn das Zielfeld frei ist**, wird der Schritt gemacht. Sonst bleibt er stehen.

⚠️ **„Frei" heißt heute: keine Wand.** `ist_frei()` fragt das Raster, und im Raster stehen keine Einheiten (Riegel 2) — **also können zwei Gegner auf demselben Feld landen.** Das ist Absicht und kein Versehen: Eine Kollisionsprüfung zwischen Einheiten wäre ein eigenes System, und sie würde heute nur dafür sorgen, dass sich Gegner gegenseitig blockieren.

**Die Folge fürs Bild:** Beim Zeichnen gewinnt, wer zuletzt gemalt wird. Zwei Gegner auf einem Feld sehen aus wie einer. **Merk dir das, wenn du beim Debuggen einen Gegner vermisst** — er ist vielleicht nicht weg, sondern verdeckt. *(Wer das später anders will, prüft beim Bewegen zusätzlich die Positionen der anderen Einheiten. Eine Zeile mehr, ein anderes Spiel.)*

⚠️ **Ein Schritt pro Tick, nicht zwei.** Läufst du in x **und** y gleichzeitig, bewegt sich ein Gegner diagonal und ist doppelt so schnell wie einer, der geradeaus läuft. **Entscheide dich für eine Achse pro Tick** — nimm die, bei der der Abstand größer ist.

⚠️ **Und jetzt der Fall, den man beim Hinschreiben übersieht: Was, wenn beide gleich groß sind?** Von `(2, 2)` nach `(5, 5)` sind es dreimal x und dreimal y. *„Nimm die größere"* sagt dazu nichts.

**Du brauchst eine feste Regel für den Gleichstand** — zum Beispiel *„bei Gleichstand immer zuerst x"*. Welche du nimmst, ist egal. **Dass du sie kennst, ist es nicht.** Ohne bewusste Entscheidung entsteht die Regel trotzdem — aus der Reihenfolge deiner `if`-Zweige, zufällig und ungeschrieben. Dein Programm verhält sich dann völlig gleichbleibend, **nur weiß niemand, wie.** Und wenn du in Etappe 16 eine Situation auf Papier nachrechnest, sagst du einen Weg voraus und bekommst einen anderen — **ohne dass irgendwo ein Fehler wäre.** Das sind die teuersten Fehlersuchen.

> ⭐ **Schreib beides in `GELERNT.md`: eine Achse pro Tick — und welche bei Gleichstand.**

*(In 14b muss die Abstandsrechnung zu dieser Entscheidung passen.)*

**So prüfst du es:** Einen Gegner setzen, fünfmal ticken, nach jedem Tick `print(g.x, g.y)`. Er nähert sich Feld für Feld. Setz ihn dann direkt vor eine Wand — er bleibt stehen, und nichts stürzt ab.

---

### 6. Bau `zeichne_vorfeld()`

Nach Konzept 8, in deiner Zeichenschicht aus Etappe 7b.

- Kopie anlegen, **Zeile für Zeile**.
- Trupp und Gegner hineinmalen — unterschiedliche Zeichen.
- Jede Zeile mit `.join()` ausgeben.
- **Die Funktion bekommt Werte und gibt aus. Sie verändert nichts.** Die Reinheitsregel aus 7b gilt unverändert.

**So prüfst du es:** Zweimal hintereinander zeichnen, ohne dass etwas tickt. **Beide Bilder müssen identisch sein.** Sind im zweiten mehr Zeichen als im ersten, hast du die Kopie vergessen und malst in dein echtes Gelände.

---

### 7. Wirf die Anmarschbahn weg

`zeichne_bahn()` aus Etappe 7b wird nicht mehr aufgerufen. **Lösch die Funktion**, nicht auskommentieren.

*(Sie hat elf Etappen gehalten und ist heute erledigt. Das ist kein Verlust, sondern der Normalfall: Code, der seinen Zweck erfüllt hat, wird entfernt. Git erinnert sich für dich.)*

---

### 8. Zähl die Fahndung aus und commit

In `GELERNT.md`: Wie viele Stellen hat Schritt 4 gekostet?

Commit: `Etappe 14a: Aus einer Zeile wird ein Feld`

> **⏸ Guter Schnitt.** Du siehst zum ersten Mal, wo etwas steht. 14b ist ein eigener Abend — und dort fängt der Trupp an zu laufen.

---

# Teil 14b — Reichweite und Bewegung

## Worum es geht

Das Raster steht. Es wird noch nicht benutzt — dein Turm feuert weiterhin auf „den Nächsten", ohne zu fragen, ob er hinreicht, und dein Trupp steht seit Etappe 12 unbeweglich im Vorposten.

**Ab heute wird gerechnet.** Und es sind nur zwei Rechnungen:

> **Wie weit ist das? — und welche Felder gehören dazu?**

Die erste ist eine Zeile. Die zweite ist eine Doppelschleife, die ein Set füllt. Beides zusammen macht aus deinem Vorfeld zum ersten Mal ein Schlachtfeld statt einer Zeichnung.

---

## Die Konzepte — Teil 14b

### 9. Abstand — und warum er zur Bewegung passen muss ⭐

Zwei Punkte, wie weit auseinander? Die Differenz allein reicht nicht, weil sie negativ sein kann:

```python
dx = 2 - 5        # -3
```

Dafür gibt es `abs()` — **den Betrag**, also die Zahl ohne Vorzeichen:

```python
print(abs(-3))    # 3
print(abs(3))     # 3
print(abs(0))     # 0
```

Damit ist der Abstand zweier Felder:

```python
def abstand(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)
```

**Waagerechte Differenz plus senkrechte Differenz.** Von `(1, 1)` nach `(4, 3)` sind das `3 + 2 = 5`.

⚠️ **Und damit gleich die Grenze festnageln, bevor sie irgendwo im Code entsteht:**

> **„In Reichweite 3" heißt: Abstand 0, 1, 2 oder 3. Abstand 4 ist draußen.**

Also `<=`, nicht `<`. Das klingt nach Haarspalterei und ist eine echte Spielregel: Bei `<` ist deine Reichweite in Wahrheit um eins kleiner als die Zahl, die du hingeschrieben hast. **Beides läuft, nur eines stimmt mit deiner Zahl überein.** Die Zählersemantik aus Etappe 13, an einer anderen Zahl.

⚠️ **Und jetzt der Punkt, der wichtiger ist als die Formel:** Diese Rechnung ist eine von mehreren, und sie ist nur dann richtig, wenn sie zu deiner Bewegung passt.

| Rechnung | Von `(0,0)` nach `(3,3)` | Passt zu einer Bewegung, die… | Form der Reichweite |
|---|---|---|---|
| `abs(dx) + abs(dy)` | **6** | pro Tick **eine** Achse geht | Raute |
| größere der beiden | 3 | pro Tick **beide** Achsen geht (diagonal) | Quadrat |
| Luftlinie | ~4,2 | sich frei bewegt | Kreis |

**Nimm die erste**, weil dein Gegner in Schritt 5 genau so läuft: eine Achse pro Tick. Dann bedeutet dein Abstand etwas Handfestes:

> **Der Abstand ist die Anzahl der Ticks, die jemand bis dorthin braucht.**

Das ist kein Schönheitsargument. Es heißt, dass *„Abstand 3"* und *„in drei Ticks da"* dasselbe sind — und damit kannst du im Kopf rechnen, wenn du in Etappe 16 einen Fehler suchst.

⚠️ **Wählst du eine andere Rechnung, musst du die Bewegung mitändern.** Zwei verschiedene Vorstellungen davon, was „nah" heißt, sind eine Fehlerquelle, die man nicht sieht: Der Turm feuert, der Gegner braucht aber noch zwei Ticks — oder umgekehrt.

*(Die drei Rechnungen haben Namen — Manhattan, Tschebyschow, Euklid. Du brauchst sie nicht. Falls sie dir in fremdem Code begegnen: Es sind genau diese drei Zeilen.)*

### 10. Reichweite als Menge von Feldern ⭐

Welche Felder deckt ein Turm auf `(2, 3)` mit Reichweite 2 ab? Die Antwort ist eine Doppelschleife über das Raster und ein Abstandsvergleich:

```python
def felder_in_reichweite(ebene, x, y, r):
    felder = set()
    for py in range(len(ebene)):
        for px in range(len(ebene[py])):
            if abstand(x, y, px, py) <= r:
                felder.add((px, py))
    return felder
```

**Zwei Dinge daran sind neu, und beide zahlen eine Schuld aus Etappe 6:**

**Erstens: Das Ergebnis ist ein Set, keine Liste.** Der Unterschied trägt hier zum ersten Mal richtig:

| | Liste | Set |
|---|---|---|
| Ein Feld doppelt drin | möglich — du müsstest prüfen | **unmöglich, ohne dass du etwas tust** |
| *Liegt der Gegner im Feuerbereich?* | durchlaufen, Stück für Stück | `in` — eine Abfrage |
| Zwei Türme, gemeinsame Abdeckung | von Hand zusammenführen | *(Etappe 6, Konzept 10 — die Mengenoperationen)* |

Die zweite Zeile ist die, die du heute spürst:

```python
if (gegner.x, gegner.y) in feuerbereich:
```

**Eine Zeile, egal wie groß der Bereich ist.** Genau dafür gibt es Sets, und genau darauf hat Etappe 6 acht Etappen lang gewartet.

**Zweitens: Was im Set liegt, sind Tuples.** Das geht nicht zufällig:

> **Ein Tuple darf in ein Set, eine Liste nicht.** Der Grund steht in Etappe 6: Ein Set muss seine Einträge wiederfinden können, und dafür dürfen sie sich nicht hinterher ändern. Ein Tuple kann sich nicht ändern — eine Liste schon.

Probier `felder.add([1, 2])` einmal aus. Der `TypeError` sagt *unhashable*, und das Wort bedeutet genau diesen Gedanken.

⚠️ **Und eine Klammer, die man vergisst:** `felder.add((px, py))` hat zwei Klammerpaare — eines für den Aufruf, eines für das Tuple. Mit einem Paar bekommst du `TypeError: add() takes exactly one argument (2 given)`. Die Meldung ist freundlich; man muss sie nur einmal gesehen haben.

### 11. Die Zone — dieselbe Prüfung, andere Grenzen ⭐

Dein Trupp soll laufen, aber nicht wegrennen. **Jeder Marine hält einen Bereich.**

```python
def in_zone(x, y, zone):
    x0, y0, x1, y1 = zone
    if x < x0 or x > x1:
        return False
    if y < y0 or y > y1:
        return False
    return True
```

**Sieh dir das neben der Randprüfung aus Konzept 5 an.** Es ist dieselbe Form: zwei Vergleiche pro Achse, `False` bei Verletzung. Nur die Grenzen kommen woandersher — dort aus `len()`, hier aus der Zone.

> **„Liegt das noch auf dem Raster?" und „darf der da hin?" sind dieselbe Frage mit verschiedenen Zahlen.** Wer das einmal sieht, schreibt die dritte solche Prüfung in zwei Minuten.

**Die erste Zeile ist eine Wiederbegegnung:** `x0, y0, x1, y1 = zone` ist Tuple-Unpacking aus Etappe 6, Konzept 9 — vier Werte auf einmal aus einem Tuple herausholen.

⚠️ **Warum die Zone Spielmechanik ist und keine Spielerei:** Ohne sie rennt dir der ganze Trupp hinter einem einzelnen Krabbler her, während am anderen Tor die Wand fällt. **Die Zone ist der Grund, warum deine Kameraden nützlich bleiben, wenn die Wellen größer werden** — und in Etappe 21b ist sie eine der ersten Stellschrauben beim Balancing.

### 12. Trupp-KI Stufe 2 — zwei Regeln, keine dritte

In Etappe 12 hatten deine Kameraden **eine** Regel: *Ist ein Ziel in Reichweite, feuere.* Heute kommt genau eine dazu:

1. Such den **nächsten** Gegner.
2. Bist du außer Reichweite, geh **ein** Feld auf ihn zu — aber nur innerhalb deiner Zone und nur auf ein freies Feld.

**Die Suche nach dem Nächsten ist derselbe Schleifenaufbau wie in Etappe 11a und 12** — durchlaufen, Abstand ausrechnen, das beste Ergebnis merken. Neu ist nur, dass „am nächsten" jetzt eine Rechnung ist statt eines Attributs.

⚠️ **Mehr bekommt die KI heute nicht.** Kein Ausweichen, kein Zurückziehen, kein Fokusfeuer, keine Absprache. Das sind reizvolle Probleme, sie kosten je einen Abend, **und keines davon lehrt dich Python.** In `GELERNT.md` notieren und weitergehen.

---

## Dein Auftrag — Teil 14b

---

### 9. Bau `welt.abstand(x1, y1, x2, y2)`

Nach Konzept 9. Eine Zeile Rumpf.

⚠️ **Sie muss zu deiner Bewegungsentscheidung aus Schritt 5 passen.** Hast du dort „eine Achse pro Tick" gebaut, ist es die Summe der Beträge.

**So prüfst du es:** Drei Aufrufe, deren Ergebnis du vorher aufschreibst — darunter einer, bei dem der zweite Punkt links **oberhalb** des ersten liegt, also beide Differenzen negativ sind. Das Ergebnis muss positiv sein.

---

### 10. Stell die Zielsuche auf den Abstand um

Deine `naechster_gegner()` aus Etappe 12 vergleicht noch `entfernung`. Sie bekommt jetzt zwei Parameter — von wo aus gesucht wird — und vergleicht Abstände.

⚠️ **Die Methode braucht einen Startpunkt, weil „am nächsten" ab heute vom Standort abhängt.** Für den Turm ist das ein anderer Gegner als für einen Kameraden am anderen Ende. In Etappe 12 gab es diesen Unterschied nicht.

**So prüfst du es:** Zwei Gegner setzen, die Suche von zwei verschiedenen Punkten aus aufrufen. **Zwei verschiedene Antworten.**

---

### 11. Bau `welt.felder_in_reichweite(x, y, r)`

Nach Konzept 10. Gibt ein Set von Tuples zurück.

**So prüfst du es:** Für einen kleinen Radius das Ergebnis ausgeben und die Felder **von Hand nachzählen**. Bei `r = 1` sind es fünf: das Feld selbst und die vier Nachbarn. Kommen neun heraus, rechnest du diagonal — und das passt dann nicht zu deiner Bewegung.

---

### 12. Gib Turm und Kameraden Standort und Reichweite

- Jede Einheit, die feuert, bekommt `x` und `y` in `__init__`, und eine `reichweite`.
- Der Turm steht an einem festen Feld im Vorposten.
- Die Kameraden starten verteilt, nicht alle auf demselben Feld.

⚠️ **Der Turm aus Etappe 13 wird dabei nicht neu gebaut.** Er bekommt zwei Attribute dazu — das ist alles. Seine Bauzeit, sein `welt.turm`, sein Platz im `trupp` bleiben, wie sie sind.

---

### 13. Stell das Feuern auf Reichweite um

In `update()` von Turm und Kameraden: Ziel suchen, Abstand prüfen, nur bei `<=` feuern.

⚠️ **`<=` und nicht `<`.** Bei Reichweite 3 soll ein Gegner in Abstand 3 noch getroffen werden. Das ist die Sorte Entscheidung, die durchläuft und trotzdem falsch sein kann — **schreib sie auf**, wie die Zählersemantik in Etappe 13.

**So prüfst du es:** Einen Gegner genau auf Abstand `reichweite` setzen — er wird beschossen. Ein Feld weiter — nicht mehr.

---

### 14. ⭐ Lass die Kameraden laufen

In `Marine.update()`, wenn kein Ziel in Reichweite ist:

- Ein Feld in Richtung des nächsten Gegners.
- **Nur wenn das Feld frei ist** (Schritt 3).
- **Nur wenn es in der eigenen Zone liegt** (Konzept 11).
- Sonst: stehen bleiben.

Jeder Marine bekommt dafür ein Attribut `zone` als Tuple aus vier Zahlen.

⚠️ **Die Reihenfolge der drei Prüfungen ist egal, das Vorhandensein nicht.** Fehlt die Zonenprüfung, läuft dir der Trupp davon. Fehlt die Freiprüfung, laufen deine Marines durch Wände — und das siehst du erst, wenn einer mitten in einem `#` steht.

**So prüfst du es:** Einen Gegner weit weg setzen und zusehen. Die Kameraden nähern sich und bleiben an ihrer Zonengrenze stehen. Setz die Zone einmal absichtlich auf ein einziges Feld — dann darf sich niemand bewegen.

---

### 15. *(Kür)* Die Sensorabdeckung

**Nur wenn 14b sich nicht zieht.** Sonst überspringen — sie kann jederzeit nachkommen.

- `welt.erkundete_felder` als Set, anfangs die Umgebung des Vorpostens.
- Jeden Tick um die Reichweite jeder eigenen Einheit erweitern — `set` kennt dafür `.add()` in einer Schleife.
- `zeichne_vorfeld()` malt alles, was nicht darin liegt, als `?`.

**⭐ Die Design-Entscheidung dazu, falls du es baust:** Was heißt „erkundet"? **Einmal gesehen und für immer bekannt** — ein Set, das wächst — oder **nur solange ein Sensor hinschaut** — ein Set, das jeden Tick neu entsteht? Beides ist vertretbar. **Aber nur das erste musst du speichern, und das merkst du in Etappe 19.** Schreib auf, welches du gewählt hast.

---

### 16. Commit

Commit: `Etappe 14b: Reichweite und Bewegung`

> **⏸ Guter Schnitt.** 14c ist Kür und lehrt nichts Neues. Wenn dir der Kopf raucht, hör hier auf.

---

# Teil 14c — Die Barrikade *(Kür)*

## Worum es geht

Sobald es Felder gibt, gibt es etwas, das man auf sie stellen kann.

**Die Barrikade ist eine Ware aus dem Depot** — gekauft für Vaporium, wie alles seit Etappe 5. Neu ist nur, dass man sie **irgendwohin** stellt.

> **Der Reiz liegt nicht im Blockieren, sondern im Umlenken.**

Ein Gegner, der geradeaus nicht weiterkommt, weicht aus — und läuft dabei durch die Zone eines Marines oder in den Feuerbereich des Turms. **Damit triffst du zum ersten Mal eine räumliche Entscheidung statt einer Zahlenentscheidung.** Bisher hieß eine Entscheidung *mehr Munition oder mehr Medkits*. Jetzt heißt sie *hierhin oder dorthin*.

### 13. Dieselbe Prüfung, zum dritten Mal

**Und genau deshalb steht die Barrikade hier und nicht in einer eigenen Etappe:**

| Frage | Woher die Grenzen kommen |
|---|---|
| Liegt das Feld auf dem Raster? | `len()` — Konzept 5 |
| Darf der Marine dahin? | die Zone — Konzept 11 |
| Ist das Feld frei? | das Raster — Schritt 3 |

**Drei Fragen, eine Form.** Die Barrikade kostet dich keine neue Technik. Sie zeigt dir, dass du eine bereits beherrschst — und das ist ein gutes Gefühl an einem Abend nach 14b.

⚠️ **Eine Barrikade ist kein Geschütz.** Sie schießt nicht, sie hat keine Stufen, sie tickt nicht. **Sie steht im Weg und hält ein paar Treffer aus.** Wer ihr Schaden gibt, baut Tower Defense — und das ist ausdrücklich nicht dieses Spiel.

---

## Dein Auftrag — Teil 14c

### 17. Nimm die Barrikade ins Depot auf

Eine Ware wie jede andere seit Etappe 5. Preis, Eintrag im Katalog, fertig. **Keine neue Mechanik.**

---

### 18. Bau den Befehl `stelle x y`

- Die Prüfkette, in dieser Reihenfolge: Hast du eine? Liegt das Feld auf dem Raster? Ist es frei? Steht dort niemand?
- **Erst alle Prüfungen, dann verändern** — die Regel aus Etappe 5, unverändert.
- Dann: `vorfeld[y][x]` auf dein Barrikadenzeichen setzen und eine aus dem Inventar entfernen.

⚠️ **Die Eingabe kommt als Text.** `stelle 3 4` liefert dir `"3"` und `"4"` — Strings, keine Zahlen. Umwandeln mit `int()`, wie seit Etappe 1. Und was passiert bei `stelle drei vier`? Das ist ein Fehlerfall wie jeder andere seit Etappe 4.

**So prüfst du es:** Auf eine Wand stellen — abgewiesen. Neben das Raster — abgewiesen. Auf ein freies Feld — sie steht da, und die Anzahl im Inventar ist um eins gesunken. Bei einem abgewiesenen Versuch bleibt das Inventar unverändert.

---

### 19. *(Optional innerhalb der Kür)* Lass sie kaputtgehen

⚠️ **Dieser Schritt ist der einzige der Portion, der etwas Neues verlangt** — eine Entscheidung darüber, wo Trefferpunkte für etwas wohnen, das kein Objekt ist. **Unzerstörbare Barrikaden sind ein vollkommen brauchbares Spielelement.** Wenn du hier aufhören willst, hör auf und notier es.


- Ein Gegner, der vor einer Barrikade steht, greift sie an statt stehenzubleiben.
- Barrikaden brauchen dafür Trefferpunkte — **als eigenes kleines Objekt oder als Zahl in einem Dictionary, das die Welt führt.** Deine Entscheidung; schreib sie auf.
- Bei null wird das Feld wieder `.`.

*(Das ist die Stelle, an der 14c doch etwas kostet. Wenn du es heute nicht willst: Lass Barrikaden unzerstörbar und notier es als offenen Posten. Ein unzerstörbares Hindernis ist ein vollkommen brauchbares Spielelement.)*

---

### 20. Beobachte das Umlenken und commit

Stell eine Barrikade so, dass ein Gegner durch die Zone eines Kameraden laufen muss. **Sieh eine ganze Welle zu und schreib in `GELERNT.md`, ob es funktioniert hat.**

Commit: `Etappe 14c: Die Barrikade`

---

## Was NICHT in diese Etappe gehört

**Keine Wegfindung.** Riegel 1. Kein A\*, kein Dijkstra, keine Breitensuche — notiert für nach Etappe 27.

**Keine Einheiten im Raster.** Riegel 2. Das Raster hält Gelände.

**Kein Sichtlinien-Check.** Ob eine Wand zwischen Turm und Ziel steht, wird heute nicht geprüft. Dein Turm schießt durch Mauern, und das bleibt vorerst so.

**Keine Zielauswahl nach Priorität.** „Der Nächste" genügt weiterhin. Strategien sind Etappe 23a, zusammen mit `min(..., key=...)`.

**Keine Comprehensions.** Die Doppelschleife in Konzept 10 lässt sich in einer Zeile schreiben. Das ist Etappe 23a, und der Vergleich mit der ausgeschriebenen Fassung ist dort der halbe Lernstoff.

**Kein `enumerate()` im eigenen Code.** Erkennen, nicht umbauen.

**Keine Karte aus einer Datei.** Das Vorfeld steht heute im Code. Etappe 25.

**Keine Fähigkeiten, die das Raster nutzen.** Minen und Fallen wollen Felder — Etappe 18.

---

## Selbsttest

**14a**
- [ ] `welt.vorfeld[0]` gibt eine ganze Zeile aus, nicht ein Zeichen.
- [ ] `welt.vorfeld[0] is welt.vorfeld[1]` ergibt `False`. *(Sonst hast du `* 5` benutzt.)*
- [ ] `ist_auf_dem_raster(-1, 2)` ergibt `False` — und nicht still das letzte Feld der Zeile.
- [ ] Das Wort `entfernung` kommt in deinem Code nicht mehr vor.
- [ ] Ein Gegner bewegt sich **ein** Feld pro Tick, nicht zwei.
- [ ] Ein Gegner vor einer Wand bleibt stehen, ohne Absturz.
- [ ] **Bei gleichem x- und y-Abstand nimmt die Bewegung immer dieselbe Achse zuerst** — und die Regel steht in `GELERNT.md`.
- [ ] Zweimal zeichnen ohne Tick ergibt **zweimal dasselbe Bild**.
- [ ] `zeichne_bahn()` ist gelöscht, nicht auskommentiert.

**14b**
- [ ] `abstand()` liefert bei zwei negativen Differenzen eine positive Zahl.
- [ ] Die Abstandsrechnung passt zur Bewegung — und du kannst sagen, warum.
- [ ] `felder_in_reichweite(x, y, 1)` liefert **fünf** Felder.
- [ ] Die Zielsuche von zwei verschiedenen Punkten liefert zwei verschiedene Antworten.
- [ ] Ein Gegner genau auf Abstand `reichweite` wird noch beschossen — **einer auf `reichweite + 1` nicht.**
- [ ] Kameraden laufen auf ein Ziel zu und bleiben an der Zonengrenze stehen.
- [ ] Kein Marine steht jemals in einem `#`.

**14c** *(falls gebaut)*
- [ ] Ein abgewiesener `stelle`-Versuch kostet keine Barrikade.
- [ ] Eine Barrikade lenkt einen Gegner sichtbar um.

---

## Lernziele

In `GELERNT.md`, ohne nachzuschlagen.

1. **Bei `vorfeld[y][x]` — welcher Index ist Zeile, welcher Spalte? Warum verwechselt das jeder mindestens einmal?**
2. Was ist `vorfeld[0]` — ein Zeichen oder etwas anderes?
3. Warum legt `[["."] * 5] * 5` **nicht** fünf Zeilen an? Woran erkennst du es im Debugger?
4. Wie prüfst du, ob eine Koordinate auf dem Raster liegt — und **warum stürzt es ohne diese Prüfung nach links nicht ab, nach unten aber schon?**
5. Warum ist ein Set für abgedeckte Felder besser als eine Liste? Zwei Gründe.
6. Warum kann ein Tuple ein Set-Element sein, eine Liste aber nicht?
7. Was steht bei den drei Schleifenformen jeweils in den Schleifenvariablen?
8. Wann passt ein Raster, wann ein Dictionary? Nenn je ein Beispiel aus **deinem** Spiel.
9. Warum muss die Abstandsrechnung zur Art der Bewegung passen?
10. **Was tut deine Bewegung bei gleichem x- und y-Abstand — und warum genügt es nicht, dass sie sich gleichbleibend verhält?**
11. Warum wird beim Zeichnen eine Kopie angelegt — und warum reicht es nicht, die äußere Liste zu kopieren?

**Frage 4 ist die wichtigste.** Sie ist ein Typ-3-Fehler, der wie Teleportation aussieht.

**Frage 8 ist die, die dich am weitesten bringt.** Sie ist keine Python-Frage, sondern eine Modellierungsfrage — und die gelten über jede Sprache hinweg.

---

## Leseübung — Stufe 2 (15 Minuten)

**Du tippst nichts ab und führst nichts aus.** Auf Papier verfolgen.

```python
def nachbarn(raster, x, y):
    gefunden = []
    for dy in range(-1, 2):
        for dx in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            nx = x + dx
            ny = y + dy
            if ny < 0 or ny >= len(raster):
                continue
            if nx < 0 or nx >= len(raster[ny]):
                continue
            if raster[ny][nx] == ".":
                gefunden.append((nx, ny))
    return gefunden


gelaende = [
    ["#", ".", "#", "."],
    [".", ".", ".", "#"],
    ["#", ".", "#", "."],
]

print(nachbarn(gelaende, 1, 1))
print(nachbarn(gelaende, 0, 0))
```

**Die fünf Fragen:**

1. Was kommt rein?
2. Was passiert?
3. Was verändert sich — und woran?
4. Was kommt raus?
5. Welche anderen Funktionen werden aufgerufen?

**Und die drei, die zu dieser Etappe gehören:**

6. **Schreib beide Ergebnislisten vollständig hin**, mit allen Tuples, in der Reihenfolge, in der sie entstehen.
7. Die Schleifen laufen über `range(-1, 2)`. **Welche drei Werte sind das, und wozu ist das gut?**
8. Was tut die erste `continue`-Zeile, und was ginge ohne sie schief?

👀 **`continue` kennst du aus Etappe 3a als Zeichen, das du erkennen, aber nicht benutzen sollst.** Hier siehst du, wofür es gemacht ist: *überspring diesen Durchlauf, mach beim nächsten weiter*. **Du baust heute nichts damit** — deine eigenen Prüfungen kommen mit `if` aus.

---

## Transferaufgabe (15 Minuten)

**Außerhalb des Spiels.** Ein Zahlenraster, kein Vorfeld.

1. Bau ein 3×3-Raster aus Zahlen, hingeschrieben.
2. Berechne die Summe der **zweiten Zeile**. *(Eine Schleife.)*
3. Berechne die Summe der **zweiten Spalte**. *(Auch eine Schleife — aber eine andere.)*
4. **Sag vorher, welche der beiden schwieriger zu schreiben ist, und ob du recht hattest.**

**Und dann der eigentliche Teil:**

5. Bau ein Raster, dessen Zeilen **verschieden lang** sind.
6. Lass deine Spaltensumme darüberlaufen. **Was passiert, und welcher Fehler ist das?**
7. Schreib die Zeile hin, die es verhindert hätte.

**Schritt 6 ist der Kern.** Es ist derselbe Grund, warum Konzept 4 `len(ebene[y])` sagt und nicht `len(ebene[0])`.

---

## Kaputtmachen

**Vor jedem Experiment aufschreiben, was passieren wird.** Die ersten vier gehören dazu, die letzten zwei sind Kür.

**1. ⭐⭐ Vertausch `x` und `y`.** Schreib in `zeichne_vorfeld()` einmal `bild[m.x][m.y]`. **Stürzt es ab?** Bei einem quadratischen Raster nicht — deine Einheiten stehen nur an der Diagonalen gespiegelt. Mach das Raster dann ungleich hoch und breit und probier es noch einmal. **Zwei völlig verschiedene Symptome, ein Fehler.**

**2. ⭐⭐ Bau das Raster mit `[["."] * 5] * 5`** und setz ein einzelnes Feld. Zeichne. **Zähl die veränderten Felder.** Dann im Debugger: `p vorfeld[0] is vorfeld[1]`.

**3. ⭐ Lass die Randprüfung weg** und schick einen Gegner auf `x = -1`. Wo taucht er auf? Schick dann einen auf `y = -1` **und** einen über den unteren Rand hinaus. **Drei Versuche, drei verschiedene Ausgänge** — schreib alle drei auf.

**4. Vergiss die Kopie beim Zeichnen.** Nimm `zeile` statt `zeile.copy()`. Zeichne dreimal hintereinander, ohne zu ticken. Was wächst?

---

Die folgenden zwei sind Kür.

**5. Setz die Reichweitenprüfung auf `<` statt `<=`.** Das läuft durch, und ein Gegner wird ein Feld zu spät beschossen. **Genau diese Sorte Fehler beschäftigt dich in Etappe 16** — und sie ist der Grund, warum Schritt 13 verlangt, die Entscheidung aufzuschreiben.

**6. Nimm die Zonenprüfung heraus.** Setz einen einzelnen Gegner in die entfernteste Ecke und sieh einer Welle zu. Wie lange dauert es, bis der Vorposten unbewacht ist?

---

**Experiment 1 und 2 sind das Paar.** Beide stürzen bei einem quadratischen Raster nicht ab und liefern etwas Falsches. **Bau dein Vorfeld deshalb ungleich hoch und breit** — sieben mal sechs statt sechs mal sechs. Das kostet nichts und macht aus zwei stillen Fehlern zwei laute.

Alles in `GELERNT.md` und ins Fehlertagebuch aus Etappe 8: **woran du es erkannt hättest.**

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `IndexError: list index out of range` | Index zu groß — `>= len(...)` fehlt, oder `>` statt `>=` benutzt | Konzept 5 |
| Ein Gegner taucht auf der anderen Kartenseite auf | Negativer Index — `liste[-1]` greift von hinten | Konzept 5 — es stürzt nicht ab |
| Alle Zeilen ändern sich gleichzeitig | Das Raster mit `* n` gebaut | Konzept 3 — `p a[0] is a[1]` |
| Einheiten stehen gespiegelt | `[x][y]` statt `[y][x]` | Konzept 2 — bei quadratischem Raster stürzt es nicht ab |
| `TypeError: 'int' object is not subscriptable` | Eine Klammer zu viel — `vorfeld[y][x][0]` | Die Zeile zählen: zwei Klammerpaare |
| Das Bild wird mit jedem Zeichnen voller | Die Kopie fehlt, du malst ins Gelände | Konzept 8 — `zeile.copy()` |
| `TypeError: unhashable type: 'list'` | Eine Liste soll in ein Set | Konzept 10 — Tuple nehmen |
| `TypeError: add() takes exactly one argument (2 given)` | `felder.add(x, y)` statt `felder.add((x, y))` | Konzept 10 — zwei Klammerpaare |
| `AttributeError: 'Gegner' object has no attribute 'entfernung'` | Eine Zugriffsstelle wurde bei der Fahndung übersehen | Schritt 4 — freundlicher Fall, zeigt dir die Stelle |
| Gegner sind doppelt so schnell wie erwartet | Beide Achsen in einem Tick | Schritt 5 — eine Achse pro Tick |
| Marines stehen in Wänden | Die Freiprüfung fehlt beim Bewegen | Schritt 14 |
| Der Trupp rennt davon | Die Zonenprüfung fehlt | Konzept 11 |
| Der Turm feuert ein Feld zu früh oder zu spät | `<` gegen `<=` | Schritt 13 — hast du es aufgeschrieben? |
| Reichweite 1 liefert neun Felder | Diagonal gerechnet, Bewegung geht aber geradeaus | Konzept 9 — die Formen müssen zusammenpassen |

**Der Debugging-Reflex dieser Etappe: „Male es auf."**

Etappe 12 fragte *in welchem Tick*, Etappe 13 *wie oft*. Heute ist die Frage **wo** — und die beantwortet keine Zahl so gut wie ein Bild:

```python
if welt.zeit == 12:
    welt.zeichne_vorfeld()
    breakpoint()
```

**Zeichnen und anhalten, in dieser Reihenfolge.** Du siehst das Feld vor dir und kannst im Debugger mit `p gegner[0].x, gegner[0].y` nachfragen, ob die Zahlen zum Bild passen. **Wenn sie es nicht tun, weißt du sofort, dass der Fehler im Zeichnen sitzt und nicht in der Bewegung** — zwei völlig verschiedene Stellen.

---

## Ein Blick nach vorne

**Etappe 15 sammelt auf, was die Brut hinterlässt** — und das liegt ab heute auf Feldern.

**Etappe 16 ist die Bug-Jagd II**, und die Kandidaten dieser Etappe sind erstklassig: `<` gegen `<=`, ein vertauschtes Indexpaar, ein Off-by-one am Rand. **Keiner davon stürzt ab.**

**Etappe 18 gibt den Fähigkeiten Wirkung**, und einige davon brauchen Felder: Minen liegen irgendwo, der mobile Turm des Engineer steht irgendwo.

**Etappe 19 speichert das Vorfeld** — und dort lernst du, dass Sets und Tuples den Weg durch JSON nicht überleben. Deine `erkundete_felder` und jede Koordinate werden auf dem Weg in die Datei zu etwas anderem. Die Schuld steht seit Etappe 6 offen.

**Etappe 21a rechnet, wer im Feuerbereich liegt.** Dein Set von heute ist genau die Antwort.

**Etappe 23a schreibt die Doppelschleife aus Konzept 10 in einer Zeile** — als Comprehension. Der Vergleich mit deiner heutigen Fassung ist dort der halbe Lernstoff, und deshalb wird sie heute ausgeschrieben.

**Etappe 25 holt das Vorfeld aus einer Datei**, statt es im Code zu haben. Dann kannst du Karten bauen, ohne Python anzufassen.

**Etappe 29 zeichnet genau dieses Raster grafisch.** Das Format, in dem Pygame Tilemaps erwartet, ist eine Liste von Listen — **deine ist es schon.** Kein Umbau, nur eine andere Zeichenfunktion. Das ist der Zahltag für Riegel 2 und für die Schicht aus Etappe 7b.

---

## Abschluss

**In `GELERNT.md`:**

- ⭐ **`vorfeld[y][x]`** — schreib die Reihenfolge hin und einen Satz dazu, woran du merkst, dass du sie vertauscht hast.
- ⭐ Meine Bewegungsentscheidung: eine Achse pro Tick oder beide? **Welche Achse bei Gleichstand?** Und passt meine Abstandsrechnung dazu?
- ⭐ Meine Entscheidung: `<` oder `<=` bei der Reichweite?
- Wie viele Stellen hat die `entfernung`-Fahndung gekostet?
- Raster oder Dictionary — je ein Beispiel aus meinem Spiel und warum.
- Notiert für nach Etappe 27: Wegfindung.
- Notiert für später: Ausweichen, Zurückziehen, Fokusfeuer, Sichtlinien.
- Was hat mich überrascht? *(Kandidaten: dass ein negativer Index nicht abstürzt · dass `* 5` fünfmal dasselbe erzeugt · wie viel ein Bild beim Fehlersuchen hilft.)*

**Vor dem Commit:** `zeichne_bahn()` gelöscht? Kein `entfernung` mehr im Code? Kein `breakpoint()` drin?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest.

**Mach dein Vorfeld groß.** Fünfzehn mal zwölf. Dann merkst du, ob deine Doppelschleifen wirklich mit `len()` arbeiten oder ob irgendwo eine feste `5` steht.

**Zeichne die Reichweite mit.** Male alle Felder aus `felder_in_reichweite()` deines Turms als `+`, wenn dort nichts anderes steht. **Du siehst zum ersten Mal, was dein Turm eigentlich abdeckt** — und wirst vermutlich sofort die Zahl ändern wollen.

**Bau ein zweites Vorfeld.** Ein anderes Raster mit anderen Wänden, umschaltbar über einen Testbefehl. Wenn dein Code das aushält, ohne dass du etwas anderes anfasst, ist deine Trennung von Daten und Logik in Ordnung — **und Etappe 25 wird ein leichter Abend.**

**Such in fremdem Spielcode nach `[y][x]`.** Du wirst beide Reihenfolgen finden, und manche Projekte streiten darüber in Kommentaren. Jetzt kannst du lesen, wer welche gewählt hat und woran man es erkennt.

---

> **Nächste Etappe:** [Etappe 15 — Was die Brut hinterlässt](etappe-15-was-die-brut-hinterlaesst.md) · Beute liegt ab jetzt irgendwo, und du zeichnest deine Kopplung zum ersten Mal auf Papier
