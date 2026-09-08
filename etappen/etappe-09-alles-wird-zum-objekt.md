# Etappe 9 — Alles wird zum Objekt

*v1.1.0 · 2026-09-07*

> **Block 2: Einheiten und Zeit** · Etappe 9 von 30 · [← Etappe 8](etappe-08-die-bug-jagd.md) · [Lehrplan](../Vorposten_Lehrplan.md) · Etappe 10 →

**Neue Syntax heute:** `class Name:` · `__init__` · `self` · `self.attribut = wert` · `objekt = Klasse(...)` · `objekt.attribut` · `def methode(self):` · `objekt.methode()` · `__repr__` · 👀 `__str__` · 👀 Dunder-Methoden als Begriff

**Zeitaufwand:** 9a: 4–5 Sitzungen · 9b: 2–3 Sitzungen, à 20–30 Minuten. Rund 45 Minuten davon sind Lesestoff, verteilt auf beide Portionen. **Rechne mit einer ganzen Sitzung allein für Auftragsschritt 3** — dort wandern deine losen Variablen in das Objekt, und dabei bricht erfahrungsgemäß erst einmal alles.

**Voraussetzung:** Etappe 8 abgeschlossen, Selbsttest grün. Du brauchst heute beides: die Funktionen aus Etappe 7 **und** den Debugger aus Etappe 8.

**Diese Etappe ist geteilt, und zwar an der Stelle, an der die meisten Anfänger hängenbleiben.** 9a ist `self` — ein Begriff, der nicht schwer ist, aber überall steht, und deshalb einen Abend für sich allein bekommt. 9b ist die Belohnung: Deine Objekte lernen, sich selbst zu zeigen.

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **9a** | `Marine` und `Gegner` als Klassen · `__init__` · Methoden statt Funktionen mit sieben Parametern | Was `self` ist · Klasse gegen Objekt · Attribut gegen lokale Variable · **wem ein Wert gehört** | — |
| **9b** | `__repr__` | Warum das dein Debugging verändert | `__str__` und wann es statt `__repr__` läuft · Dunder als Haken |

---

## Worum es geht

Hol deine Notiz aus Etappe 7 heraus — die aus Auftragsschritt 7, in der stehen sollte: **welche Funktion die längste Parameterliste hat, und welche Werte darin immer gemeinsam auftreten.**

Das ist die wichtigste Vorarbeit, die du für heute geleistet hast. Wenn du sie nicht geschrieben hast, schau jetzt in deinen Code und beantworte die Frage nachträglich. Ohne sie wirkt alles, was heute kommt, wie Zeremonie.

Denn du hast am Ende von Etappe 7 vermutlich etwas in dieser Art dastehen:

```
berechne_schaden(waffe, ziel, panzerung, klasse, boni, munition)
```

Sechs Parameter. Und wenn du ehrlich hinsiehst, treten fünf davon **immer gemeinsam** auf — sie gehören alle demselben Marine. Du reichst sie trotzdem einzeln durch drei Ebenen durch, weil Python bisher nicht wusste, dass sie zusammengehören.

> **Heute lernst du, wie man Python das sagt. Das Werkzeug dafür heißt Klasse, und der Zusammenhalt, den es stiftet, heißt `self`.**

Danach steht dort:

```
marine.berechne_schaden(ziel)
```

Ein Punkt statt sechs Parametern. Und das ist nicht bloß kürzer — es ist eine andere Aussage. Die erste Zeile sagt *„nimm diese sechs zufällig zusammengetragenen Werte"*. Die zweite sagt *„dieser Marine berechnet seinen Schaden"*. Der Code sagt jetzt dasselbe wie das Spiel.

**Und noch etwas ändert sich, das du erst in Etappe 11 und 12 voll spüren wirst.** Bisher gab es in deinem Spiel *einen* Marine, weil mehr gar nicht ging — sechs lose Variablen pro Marine wären bei vier Marines vierundzwanzig lose Variablen. Ab heute ist ein zweiter Marine eine einzige zusätzliche Zeile. Das ist die Tür, hinter der der Trupp wartet.

---

## Der lange Bogen — was heute fällig wird

Etappe 9 ist eine Einlösung, und die Schulden kommen aus mehreren Richtungen. Ich nenne sie, damit du siehst, dass der Schmerz der letzten Etappen Absicht war:

- **Die lange Parameterliste aus 7a** war kein Versehen des Plans, sondern sein Aufbau. Sie begründet `self`. Wer sie nicht hatte, hält Klassen für Bürokratie.
- **Die Design-Entscheidung aus 7a** — Zustand als Parameter, nicht als `global` — wird heute wieder gelesen. `self` löst dieselbe Frage, nur endgültig. Das `global`, das du damals abgelehnt hast, hätte genau das Problem zugedeckt, das heute verschwindet.
- **`trefferpunkte` aus Etappe 1** zieht in den Marine ein. **`kern_integritaet` bleibt draußen** — und genau an diesem Unterschied lernst du heute, wem ein Wert gehört.
- **`erfahrung` aus 3c** — die Zahl, die seit sechs Etappen mitzählt und nichts tut — wird Attribut. Zusammen mit **der Stufentabelle aus Etappe 5** kann dein Marine ab heute seine eigene Stufe ausrechnen. *(Wirkung hat sie weiterhin keine. Das bleibt Etappe 18 vorbehalten.)*
- **`aktueller_sektor` aus Etappe 5** wird zu `marine.sektor`. Das Objekt kennt seinen eigenen Standort.
- **Der `vorrat` aus Etappe 5** wandert vollständig hinein.
- **Die Punkt-Schreibweise aus Etappe 2** — damals ein Satz zum Wiedererkennen, *„gehört zu"* — bekommt heute ihren vollen Sinn. Du hast sie an `.strip()` und `.append()` benutzt, ohne zu wissen, wie so etwas entsteht. Heute baust du selbst welche.
- **Der Debugger aus Etappe 8** bekommt in 9b seinen zweiten Zahn, und **die repr-Form aus Etappe 8** ihre eigentliche Anwendung.

**Eine Schuld wird heute ausdrücklich *nicht* eingelöst:** die zwei parallelen Listen aus Etappe 6. Warum, steht weiter unten in Konzept 8.

---

## Vor dem Umbau: drei Fragen ⭐

Das Ritual seit Etappe 4. Heute ist es besonders nützlich, weil sich viel *anfühlt*, als würde es sich ändern, und wenig es tatsächlich tut:

| Frage | Antwort |
|---|---|
| **Was bleibt gleich?** | Jeder Wert, jede Zahl, jede Meldung, jedes Verhalten. Der Spieler merkt nichts. |
| **Was ändert sich nur in der Darstellung?** | Nichts. Die Anzeige bleibt Zeichen für Zeichen dieselbe. |
| **Was ändert sich wirklich am Datenmodell?** | Die Werte bekommen einen **Besitzer**. `trefferpunkte` heißt ab heute `marine.trefferpunkte` — derselbe Wert, neuer Wohnort. |

**Das ist der zweite reine Umbau des Plans nach Etappe 7** — und wieder gilt: Jede Abweichung im Verhalten ist ein Fehler, nicht ein Nebeneffekt. Deshalb ziehst du heute wieder den Beweis aus Etappe 7a, mit `befehle.txt` und `diff`.

---

## Eine Design-Entscheidung: Wem gehört ein Wert? ⭐

Das ist die eigentliche Denkarbeit dieser Etappe, und sie fällt schwerer als die Syntax.

Du hast zwei Gesundheitswerte, seit Etappe 1, und beide stehen auf 100:

- `trefferpunkte` — deine Figur
- `kern_integritaet` — die Anlage, die du verteidigst

Beide sind Zahlen. Beide sinken. Beide beenden das Spiel, wenn sie null erreichen. Es liegt nahe, beide in den Marine zu stecken, weil sie sich so ähnlich verhalten.

**Tu das nicht.** Frag stattdessen: *Wenn es einen zweiten Marine gäbe — hätte der seinen eigenen Wert davon?*

| | Zweiter Marine hätte davon | Also gehört es |
|---|---|---|
| `trefferpunkte` | **einen eigenen** — jeder Marine hat seine eigene Gesundheit | **in den Marine** |
| `vorrat`, `sektor`, `erfahrung`, `schaden` | jeweils **einen eigenen** | **in den Marine** |
| `kern_integritaet` | **keinen** — die Anlage gibt es genau einmal | **nach draußen** |
| Die Gegnerliste, die Wellennummer | **keinen** — die gehören der Welt | **nach draußen** |

> **Die Frage lautet nicht „ist der Wert wichtig?", sondern „gäbe es ihn pro Figur oder pro Spiel?".**

Was pro Figur existiert, wird Attribut. Was pro Spiel existiert, bleibt vorerst eine lose Variable — bis Etappe 12, wo es ein eigenes Objekt bekommt, dem es gehört: die Welt.

**Schreib deine Antwort und die Begründung in `GELERNT.md`.** Und dazu, welche Werte du dir schwer getan hast einzuordnen. In Etappe 12 liest du das wieder, und dort wird sich zeigen, ob du richtig lagst.

---

## Die Konzepte — Teil 9a

Alle Beispiele laufen **außerhalb** deines Spiels — eine Bäckerei, ein Café, ein Lager. Was in `spiel.py` entsteht, schreibst du selbst.

### 1. Der Bauplan und das Ding ⭐

Zwei Wörter, die man ständig verwechselt, und der Unterschied ist der ganze Kern:

> **Eine Klasse ist ein Bauplan. Ein Objekt ist ein Ding, das nach diesem Bauplan gebaut wurde.**

Ein Bauplan für einen Backofen ist kein Backofen. Man kann darin nicht backen. Aus einem Bauplan lassen sich beliebig viele Öfen bauen, und jeder hat danach seine **eigene** Temperatur.

```python
class Backofen:
    ...
```

Das ist der Bauplan. Er tut nichts, er beschreibt nur. Und jetzt zwei Öfen daraus:

```python
ofen_nord = Backofen("Nord", 180)
ofen_sued = Backofen("Süd", 220)
```

Zwei Objekte, ein Bauplan. `ofen_nord` und `ofen_sued` sind völlig unabhängig — heizt du den einen hoch, bleibt der andere, wo er war. **Genau das ist die Eigenschaft, wegen der ein Trupp aus vier Marines in Etappe 11 überhaupt möglich wird.**

Der Klassenname beginnt üblicherweise mit einem Großbuchstaben, die Objektnamen nicht. Das ist keine Regel, die Python erzwingt, sondern eine Verabredung unter Menschen — und du hältst dich daran, weil jeder fremde Code es so macht.

### 2. `class` und `__init__` — der Bauplan wird geschrieben

```python
class Backofen:
    def __init__(self, name, temperatur):
        self.name = name
        self.temperatur = temperatur
        self.betriebsstunden = 0
```

Vier Dinge stehen hier, die alle neu sind:

**`class Backofen:`** — Doppelpunkt und Einrückung, wie bei `if` und `def`. Alles Eingerückte gehört zum Bauplan.

**`def __init__(self, ...)`** — das ist eine ganz normale Funktionsdefinition, wie du sie aus Etappe 7 kennst. Der Name ist besonders: **Python ruft sie automatisch auf, wenn ein Objekt entsteht.** Du rufst `__init__` nie selbst.

**`self.name = name`** — hier passiert der eigentliche Trick. Rechts steht der Parameter (der verschwindet, wenn die Funktion endet, du weißt das aus Etappe 7, Scope). Links steht `self.name` — und das bleibt. Der Wert wird am Objekt **festgemacht**.

**`self.betriebsstunden = 0`** — nicht jedes Attribut muss von außen kommen. Manche haben schlicht einen Startwert.

**Beim Erzeugen gibst du alles mit, was `__init__` verlangt — außer `self`:**

```python
ofen = Backofen("Nord", 180)
```

`self` steht in der Definition, aber nicht im Aufruf. Warum, kommt gleich.

### 3. `self` — der Zettel mit der eigenen Adresse ⭐

Das ist der Begriff, an dem es hakt, deshalb langsam.

`self` ist ein **ganz normaler erster Parameter**. Nichts Magisches. Python füllt ihn nur automatisch aus, und zwar mit **dem Objekt, an dem gerade gearbeitet wird**.

Wenn du `ofen_nord.heize(20)` schreibst, macht Python daraus sinngemäß: *„führe `heize` aus, und `self` ist `ofen_nord`."* Deshalb steht `self` in der Definition, aber nicht im Aufruf — Python setzt es ein.

Und deshalb funktioniert derselbe Bauplan für beliebig viele Öfen:

```python
    def heize(self, grad):
        self.temperatur += grad
```

Bei `ofen_nord.heize(20)` ist `self` der Nord-Ofen, also steigt dessen Temperatur. Bei `ofen_sued.heize(20)` ist `self` der Süd-Ofen. **Eine Methode, geschrieben für alle, die jedes Mal weiß, an wem sie gerade arbeitet.**

> **Merksatz: `self` heißt „das Ding, an dem ich gerade arbeite".** Wo `self.` steht, ist ein Wert gemeint, der diesem einen Objekt gehört — und nicht dem Nachbarn.

**Der Name `self` ist übrigens frei wählbar** und Python zwingt dich zu nichts. Aber jeder Python-Code der Welt nennt ihn `self`, und wer ihn anders nennt, macht seinen Code für alle anderen fremd. Nimm `self`.

### 4. Attribut oder lokale Variable? 🧠

Innerhalb einer Methode gibt es zwei Sorten von Namen, und sie sehen fast gleich aus:

```python
    def heize(self, grad):
        zielwert = self.temperatur + grad     # lokal — weg nach dem Aufruf
        self.temperatur = zielwert            # Attribut — bleibt am Objekt
```

`zielwert` ist eine **lokale Variable**. Sie existiert, solange die Methode läuft, und verschwindet danach — genau der Scope aus Etappe 7, Konzept 5. Nichts Neues.

`self.temperatur` ist ein **Attribut**. Es gehört dem Objekt und überlebt den Aufruf.

> **Die Faustregel: Was der Zustand des Dings ist, kommt an `self`. Was nur ein Zwischenschritt der Rechnung ist, bleibt lokal.**

Und daraus folgt die häufigste Anfängerfalle dieser Etappe, die du im Kaputtmachen absichtlich auslösen wirst: **Wer das `self.` vergisst, schreibt versehentlich in eine lokale Variable.** Der Code läuft, es knallt nichts — und der Wert ist beim nächsten Aufruf wieder weg. Ein lupenreiner **Typ-3-Fehler**, aus Etappe 8.

### 5. Methoden — Funktionen, die zu etwas gehören

Eine Methode ist eine Funktion, die im Bauplan steht. Fast alles, was du in Etappe 7 gelernt hast, gilt unverändert: Parameter, `return`, Standardargumente, Docstrings, `return` beendet sofort.

Der einzige Unterschied ist der erste Parameter:

```python
class Backofen:
    """Ein Ofen mit Temperatur und Betriebsstunden."""

    def __init__(self, name, temperatur):
        self.name = name
        self.temperatur = temperatur
        self.betriebsstunden = 0

    def heize(self, grad):
        """Erhöht die Temperatur um grad und meldet den neuen Stand."""
        self.temperatur += grad
        print(f"{self.name} jetzt bei {self.temperatur} Grad")

    def ist_betriebsbereit(self):
        """Gibt True zurück, wenn der Ofen heiß genug ist."""
        return self.temperatur >= 200
```

Beachte `ist_betriebsbereit`: Sie hat **nur** `self` und sonst keinen Parameter — weil sie alles, was sie braucht, schon am Objekt vorfindet. **Das ist der Schrumpfvorgang, um den es heute geht.** Vorher hätte sie `temperatur` übergeben bekommen müssen.

Und der Aufruf braucht die Klammern, wie bei jeder Funktion:

```python
ofen = Backofen("Nord", 180)
ofen.heize(30)
print(ofen.ist_betriebsbereit())
print(ofen.temperatur)
```

⚠️ **`ofen.ist_betriebsbereit` ohne Klammern ruft nicht auf** — es zeigt nur auf die Methode selbst, und das ist immer wahrheitswertig „wahr". In einem `if` ist das ein stiller Fehler, der nie knallt. Merk ihn dir; in Etappe 11 kommt seine gefährlichere Verwandte.

### 6. Attribute von außen lesen und schreiben

Der Punkt funktioniert in beide Richtungen:

```python
print(ofen.temperatur)        # lesen
ofen.temperatur = 250         # schreiben
ofen.betriebsstunden += 5     # verändern, wie bei jeder Variablen
```

Und weil ein Attribut jeden beliebigen Wert halten kann, auch ein Dictionary aus Etappe 5:

```python
class Lager:
    def __init__(self, bestand):
        self.bestand = bestand

lager = Lager({"mehl": 4, "hefe": 2})
print(lager.bestand["mehl"])
lager.bestand["hefe"] -= 1
```

**`lager.bestand["mehl"]` — Punkt und eckige Klammer hintereinander.** Erst holt der Punkt das Dictionary aus dem Objekt, dann greift die Klammer den Schlüssel heraus. Das sieht beim ersten Mal überladen aus und ist genau das, was du gleich mit deinem Vorrat brauchst.

### 7. Die Begriffsfalle „Klasse" ⚠️

Ab heute bedeutet das Wort *Klasse* in diesem Projekt zwei verschiedene Dinge, und sie tauchen zum ersten Mal gleichzeitig auf:

| | Was gemeint ist | Beispiel |
|---|---|---|
| **Spielerklasse** | Soldat, Heavy, Engineer, Medic — die Rolle deiner Figur, seit Etappe 1 | ein **Wert**, der in einer Variablen steht |
| **Python-Klasse** | Der Bauplan, den du heute schreibst | `class Marine:` |

**Heute wird die Spielerklasse ein ganz normales Attribut** — `self.klasse = "Engineer"`, ein String wie jeder andere. Sie ist **keine** Python-Klasse.

**In Etappe 11 ändert sich das**, und dann werden aus den vier Spielerklassen tatsächlich vier Python-Klassen. Bis dahin: zwei Wörter, ein Laut, verschiedene Dinge. Wenn du im Selbsttest gefragt wirst, welche Klasse gemeint ist, ist das keine Spitzfindigkeit.

### 8. Zwei Klassen — und warum die Gegnerlisten heute unangetastet bleiben ⭐

Du baust heute **zwei** Klassen: `Marine` und `Gegner`. Aber nur eine davon setzt du wirklich ein.

**`Marine` ersetzt deine losen Variablen vollständig.** Das ist der Umbau.

**`Gegner` schreibst du auf und lässt sie liegen.** Deine zwei parallelen Listen aus Etappe 6 —

```
gegner       = [7, 4, 2]
gegner_typen = ["kriecher", "kriecher", "speier"]
```

— bleiben, wie sie sind. Unbequem, mit dem lästigen Zwang, beim Entfernen an zwei Stellen denselben Index zu treffen.

**Das ist Absicht, aus zwei Gründen.**

Der erste ist die Regel aus Etappe 7a: **nie zwei Umbauten im selben Schritt.** Wer heute gleichzeitig den Marine zerlegt und die Gegnerlisten kollabieren lässt und danach einen Fehler hat, hat zwei Verdächtige. Du kennst das Verfahren dagegen seit Etappe 8 — es heißt Halbieren, und hier wendest du es vorbeugend an.

Der zweite ist die Buchführung: **Der Zusammenbruch der zwei Listen ist der Zahltag von Etappe 11.** Dort stellst du die Frage, was `Marine` und `Gegner` gemeinsam haben, und dort verschwindet der Schmerz aus Etappe 6 — an dem Tag, an dem er etwas beweist.

Wozu die Klasse dann heute? **Damit sie in Etappe 11 neben `Marine` steht und die Frage überhaupt gestellt werden kann.** Zwei Baupläne nebeneinander, die sich verdächtig ähneln, sind ein besseres Argument für Vererbung als jede Erklärung.

*(Und damit du sie einmal angefasst hast, erzeugst du im Auftrag ein paar Gegner-Objekte in einer Wegwerf-Datei. Wegwerfcode ist ausdrücklich erlaubt, wenn etwas erst später richtig gebaut wird.)*

---

## Die Konzepte — Teil 9b

### 9. `__repr__` — das Objekt zeigt, was in ihm steckt ⭐

Bau eine Klasse ohne Weiteres und druck ein Objekt davon aus, und du bekommst das hier:

```
<__main__.Lieferung object at 0x7efc266382c0>
```

**Das ist die nutzloseste Ausgabe der Sprache.** Sie sagt dir die Klasse und eine Speicheradresse — also nichts, was du beim Fehlersuchen gebrauchen könntest. Und ab Etappe 12, wenn zwanzig Einheiten gleichzeitig existieren, bekommst du zwanzig solcher Zeilen und kannst keine von der anderen unterscheiden.

Eine einzige Methode behebt das:

```python
class Lieferung:
    def __init__(self, ziel, kisten):
        self.ziel = ziel
        self.kisten = kisten

    def __repr__(self):
        return f"Lieferung(ziel={self.ziel!r}, kisten={self.kisten})"
```

Jetzt zeigt `print(lieferung)`:

```
Lieferung(ziel='Nord', kisten=3)
```

**Drei Dinge an dieser Methode sind wichtig:**

**Sie gibt `return` einen String zurück, sie druckt nicht.** Das ist die Linie aus Etappe 7b: Wer hier `print` schreibt statt `return`, bekommt eine Methode, die druckt und danach `None` liefert — die Falle aus Etappe 7.

**Das `!r` aus Etappe 8 steht bei jedem String-Attribut.** Deshalb erscheint `ziel='Nord'` mit Anführungszeichen und `kisten=3` ohne. Beim Fehlersuchen siehst du damit sofort, was ein String ist und was eine Zahl — und genau diese Verwechslung war dein allererster Fehler in Etappe 1.

**Die übliche Form ist `Klassenname(attribut=wert, ...)`.** Sie sieht aus wie der Aufruf, mit dem man das Objekt erzeugen würde. Das ist kein Zufall, sondern die Verabredung: Eine `__repr__` soll so eindeutig sein, dass man daraus das Objekt nachbauen könnte.

**Und jetzt der Zahltag für Etappe 8.** Setz ein `breakpoint()` und tipp `p lieferung`:

```
(Pdb) Lieferung(ziel='Nord', kisten=3)
```

`p` zeigt die repr-Form, das hast du in Etappe 8 gelernt. **Ab heute ist diese Form deine eigene.** Der Debugger zeigt dir nicht mehr eine Speicheradresse, sondern den Zustand deines Objekts — und in einer Liste von zwanzig Objekten jede einzelne Zeile lesbar.

### 10. Doppelte Unterstriche sind Haken 🧠

`__init__` und `__repr__` haben etwas gemeinsam, das über den Namen hinausgeht:

> **Du rufst sie nie selbst auf. Python ruft sie auf, in bestimmten Momenten.**

`__init__` läuft, wenn ein Objekt entsteht. `__repr__` läuft, wenn Python das Objekt darstellen soll. Solche Methoden heißen **Dunder-Methoden**, nach *double underscore*, und man kann sie sich als **Haken** vorstellen: Python zieht daran, du hängst etwas dran.

Genau die hast du übrigens in Etappe 4 schon gesehen — als die lange Liste aus `print(dir([]))`, in der dir gesagt wurde, du sollst die Einträge mit den doppelten Unterstrichen überspringen. Jetzt weißt du, was sie sind.

**Mehr davon kommt in Etappe 11.** Heute baust du zwei, und das ist genug.

### 11. 👀 `__str__` und `__repr__` — zwei Darstellungen, nicht eine

| | Gedacht für | Ausgelöst durch |
|---|---|---|
| `__repr__` | **dich**, beim Fehlersuchen — eindeutig und vollständig | `repr(x)`, der Debugger, die Ausgabe einer Liste |
| `__str__` | **den Spieler** — lesbar und kurz | `str(x)`, `print(x)`, `f"{x}"` |

⚠️ **Schreib heute nur `__repr__`.** Wenn `__str__` fehlt, springt Python auf `__repr__` zurück — eines von beiden reicht deshalb vollkommen, und das nützlichere ist `__repr__`.

Dieser Kasten steht hier aus **einem** Grund: Wenn du in fremdem Code auf `f"{einheit}"` triffst und dort ein sauberer Satz erscheint, sollst du nicht rätseln, woher der Text kommt. Er kommt aus einer dieser beiden Methoden, und welche es ist, steht **in der Klasse** — nicht in der f-String-Zeile. Ein Satz, den du sagen kannst, erledigt diese Spalte. Eine zweite Implementierung brauchst du nicht.

### 12. Das eigene Objekt befragen 👀

Die Technik aus Etappe 4 und 5 — `dir()` und `help()`, statt nachzuschlagen — funktioniert an deinen eigenen Klassen genauso:

```python
lieferung = Lieferung("Nord", 3)
print(dir(lieferung))
help(lieferung.melde)
```

`dir()` liefert wieder eine lange Liste, in der die Dunder-Einträge die Mehrheit bilden. **Überspring sie und lies nur die Namen ohne Unterstriche** — das sind genau die Attribute und Methoden, die du selbst geschrieben hast. Bei einem fremden Objekt sind es genau die, die dich interessieren.

`help()` zeigt dir deinen eigenen Docstring aus Etappe 7. Das ist der Moment, in dem sich zeigt, ob du damals brauchbare geschrieben hast.

### 13. Die Leseleiter, Stufe 1 — und eine neue Frage ⭐

Ab heute gehört zu jeder Etappe eine **Leseübung**. Du tippst nichts ab und führst nichts aus — du liest fremden Code und beantwortest Fragen. Das ist nicht Beiwerk, sondern der eigentliche Zweck dieses ganzen Projekts: Am Ende sollst du fremden Code beurteilen können, statt ihn zu glauben.

**Stufe 1 umfasst fünf bis zehn Zeilen, und die Leitfrage ist: *Was passiert hier?*** Die fünf festen Fragen sind immer dieselben, und die Wiederholung ist der Punkt:

> 1. Was kommt rein?
> 2. Was passiert?
> 3. Was verändert sich — und woran?
> 4. Was kommt raus?
> 5. Welche anderen Objekte oder Funktionen werden dabei aufgerufen?

**Und ab heute kommt eine sechste dazu, die zu Objekten gehört:**

> **Woher kommt dieser Name?** Steht er in dieser Datei, kommt er aus einem `import`, oder hängt er an `self`?

Drei völlig verschiedene Herkünfte, die beim Lesen gleich aussehen. Wer sie nicht trennt, hält jeden unbekannten Namen für Magie — und genau das ist der Zustand, aus dem dieses Projekt dich herausholt. **Module baust du erst in Etappe 24; erkennen musst du sie ab jetzt.** In Etappe 11 kommt eine vierte Herkunft dazu.

---

## Dein Auftrag

Durchlaufende Nummerierung über beide Portionen. **Nach jedem einzelnen Schritt ausführen. Nicht nach fünf.**

⚠️ **Das hier ist die vollständige Liste.** Wenn diese Schritte stehen, bist du fertig — auch wenn dir noch drei weitere Dinge einfallen, die man zu Objekten machen könnte. Die gehören in `GELERNT.md`, nicht in den heutigen Abend.

---

### 1. Zieh den Beweis, bevor du irgendetwas anfasst

- Nimm `befehle.txt` aus Etappe 7. Ergänz Zeilen, falls seither Befehle dazugekommen sind.
- Lauf einmal durch und sichere die Ausgabe:

```bash
python spiel.py < befehle.txt > vorher.txt
```

**So prüfst du es:** Öffne `vorher.txt`. Steht dort ein vollständiger Durchlauf? Bricht das Programm vorher ab, fehlt eine Eingabe.

⚠️ **Ohne diese Datei fängst du nicht an.** Sie ist der einzige Beweis, dass dein Umbau nichts kaputt gemacht hat.

---

### 2. Schreib die Klasse `Marine` mit ihrem `__init__`

Leg die Klasse oben in `spiel.py` an, über allem anderen. Sie bekommt diese Attribute:

| Attribut | Woher der Wert kommt | Hinweis |
|---|---|---|
| `name` | Parameter | der Name deiner Figur |
| `klasse` | Parameter | die **Spieler**klasse als String: `"Soldat"`, `"Heavy"`, `"Engineer"`, `"Medic"` |
| `klassengeraet` | Parameter | der String aus Etappe 2: `"Sturmgewehr"`, `"Schweres MG"`, `"Multiwerkzeug"`, `"Bio-Injektor"` |
| `trefferpunkte` | Parameter | dein bisheriger Wert, üblicherweise 100 |
| `panzerung` | Parameter | dein bisheriger Wert |
| `schaden` | Parameter | dein bisheriger Wert |
| `sektor` | Parameter | dein bisheriger `aktueller_sektor` |
| `vorrat` | Parameter | das **ganze** Vorrats-Dictionary aus Etappe 5 |
| `inventar` | Parameter | deine Inventarliste aus Etappe 4 |
| `erfahrung` | Startwert `0` | die Zahl aus 3c |
| `level` | Startwert `1` | |

⚠️ **`klassengeraet` wandert mit, bleibt aber ein toter String.** Es wird angezeigt und nirgends abgefragt — genau wie seit Etappe 2. Die Versuchung, jetzt eine Methode `setze_faehigkeit_ein()` daneben zu stellen, ist groß, weil du gerade gelernt hast, wie man Methoden schreibt. **Das ist Etappe 18**, und dort braucht es Sets, Statuseffekte und Abklingzeiten, die du alle noch nicht hast.

⚠️ **`vorrat` wandert als Ganzes hinein — es gibt kein `self.munition`.** Deine Munition heißt ab heute `marine.vorrat["munition"]`. Ein zweiter Speicher für denselben Wert wäre die sicherste Art, sie auseinanderlaufen zu lassen.

**So prüfst du es:** Erzeug am Ende der Datei testweise ein Objekt und druck zwei Attribute aus. Läuft es?

---

### 3. Ersetz die losen Variablen durch das Objekt

**Das ist der lange Schritt. Plan eine ganze Sitzung dafür ein.**

- Erzeug **ein** Marine-Objekt an der Stelle, an der bisher deine losen Variablen standen — mit denselben Startwerten wie bisher.
- Geh dann durch die Datei und ersetz jede Verwendung: `trefferpunkte` wird `marine.trefferpunkte`, `aktueller_sektor` wird `marine.sektor`, `vorrat["munition"]` wird `marine.vorrat["munition"]`, und so weiter.
- **Lösch die losen Variablen erst, wenn keine Stelle mehr auf sie zeigt.**

**So prüfst du es:** Wenn eine Stelle übersehen ist, bekommst du einen `NameError` — der freundlichste Fehler, den es gibt, weil er dir den Namen und die Zeile nennt. Lauf das Spiel so lange, bis kein `NameError` mehr kommt.

⚠️ **Diese Werte wandern ausdrücklich NICHT hinein:** `kern_integritaet`, deine Gegnerlisten, die Wellennummer, die Sektorenkarte. Sie gehören dem Spiel, nicht der Figur — siehe die Design-Entscheidung oben. Sie bleiben vorerst lose Variablen und bekommen in Etappe 12 ihr eigenes Zuhause.

---

### 4. Mach aus deiner ersten Funktion eine Methode

- Nimm `zeige_status()` aus Etappe 7 und verschieb sie **in** die Klasse, eingerückt wie `__init__`.
- Setz `self` als ersten Parameter.
- **Lösch jeden Parameter, den die Methode jetzt über `self` erreichen kann.** Genau dafür ist heute.
- Pass die Aufrufstelle an: aus `zeige_status(trefferpunkte, vorrat, sektor)` wird `marine.zeige_status()`.

**So prüfst du es:** Führ das Spiel aus und ruf `status` auf. Sieht die Ausgabe **exakt** aus wie vorher?

---

### 5. Verschieb die übrigen Marine-Funktionen

Dasselbe für jede Funktion aus Etappe 7, die überwiegend mit Marine-Werten arbeitet — üblicherweise die Schadensberechnung, das Kaufen, der Sektorwechsel.

**Die Prüffrage bei jeder einzelnen: *Arbeitet diese Funktion hauptsächlich an einem Marine?*** Wenn ja, wird sie Methode. Wenn nein, bleibt sie Funktion.

⚠️ **Nicht jede Funktion wird eine Methode.** Deine Zeichenfunktionen aus 7b zum Beispiel bleiben, wo sie sind — `zeichne_balken(wert, maximum)` gehört keinem Marine, sie zeichnet einen Balken für jeden. Wer sie hineinzieht, macht die Trennung aus 7b wieder kaputt, die Etappe 28 braucht.

Nach **jeder** verschobenen Funktion ausführen.

---

### 6. Bau eine Methode, die die Stufe berechnet

- Hol die Stufentabelle aus Etappe 5 (`{1: 0, 2: 120, 3: 300}` oder deine eigenen Schwellen).
- Schreib eine Methode, die aus `self.erfahrung` die passende Stufe ermittelt und in `self.level` schreibt.
- Ruf sie an der Stelle auf, an der die Erfahrung steigt.

⚠️ **Die Stufe hat weiterhin keine Wirkung** — sie steht in der Anzeige und sonst nirgends. Keine Freischaltungen, keine Boni, keine Fähigkeiten. Das ist Etappe 18, und wer es vorzieht, nimmt ihr den Gegenstand.

**So prüfst du es:** Setz `marine.erfahrung` testweise über die höchste Schwelle, ruf die Methode und druck `marine.level`.

---

### 7. Schreib die Klasse `Gegner`

- Attribute: `trefferpunkte`, `schaden`, `entfernung`, `typ`.
- Nur `__init__`, keine Methoden.
- **Bau sie nicht in dein Spiel ein.** Deine zwei Gegnerlisten bleiben unangetastet — siehe Konzept 8.
- Erzeug in einer **Wegwerf-Datei** drei Gegner-Objekte und druck ihre Attribute aus, damit du die Klasse einmal in der Hand hattest.

**So prüfst du es:** Läuft die Wegwerf-Datei? Steht in `spiel.py` weiterhin die alte Gegnerlogik, unverändert?

---

### 8. Zieh den Beweis

```bash
python spiel.py < befehle.txt > nachher.txt
diff vorher.txt nachher.txt
```

**Es darf kein Unterschied erscheinen.** Wenn doch: Der Unterschied ist ein Fehler, kein Nebeneffekt. Halbieren aus Etappe 8 — welche Funktion hast du zuletzt verschoben?

---

### 9. Räum auf und committe 9a

- Sind alle losen Marine-Variablen weg, oder liegen noch Leichen herum?
- Gibt es irgendwo einen zweiten Speicher für die Munition?
- Keine `###`-Zeilen, kein `breakpoint()`.
- Commit: `Etappe 9a: Alles wird zum Objekt`

---

### 10. Gib `Marine` ein `__repr__`

- Form: `Marine(name='…', klasse='…', trefferpunkte=…, sektor='…', level=…)` — nimm die Attribute, die du beim Fehlersuchen tatsächlich sehen willst, nicht alle.
- **`!r` bei jedem String-Attribut**, keines bei den Zahlen.
- `return`, kein `print`.

**So prüfst du es:** `print(marine)` in einer Wegwerf-Zeile. Steht dort eine lesbare Zeile statt einer Speicheradresse?

---

### 11. Gib `Gegner` ein `__repr__`

Dasselbe für die zweite Klasse. **Druck danach in deiner Wegwerf-Datei eine *Liste* mit drei Gegner-Objekten aus** — `print(meine_gegner)`.

Das ist der Moment, auf den es ankommt: Eine Liste von Objekten ist ohne `__repr__` unlesbar und mit `__repr__` eine saubere Tabelle. **Ab Etappe 12 hast du zwanzig davon gleichzeitig.**

---

### 12. Sieh dir dein Objekt im Debugger an

- Setz ein `breakpoint()` mitten in deine Hauptschleife.
- Tipp `p marine`. Was siehst du jetzt, was du in Etappe 8 nicht gesehen hättest?
- Tipp `p marine.vorrat` und geh mit `n` ein paar Zeilen weiter. Ändert sich etwas?
- **`breakpoint()` danach wieder raus.**

---

### 13. Befrag dein eigenes Objekt

- `print(dir(marine))` — überspring die Dunder-Einträge und lies die übrigen. Stehen dort genau die Attribute und Methoden, die du geschrieben hast?
- `help(marine.zeige_status)` — kommt ein brauchbarer Satz, oder zeigt sich, dass dein Docstring aus Etappe 7 nichts sagt?

---

### 14. Die Leseübung

**Du tippst nichts ab und führst nichts aus.** Lies und beantworte schriftlich:

```python
rekrut = Rekrut("Vasquez", 7)

if rekrut.moral > 5:
    rekrut.melde("Position gehalten.")
else:
    rekrut.melde("Ich brauche Ablösung.")

rekrut.moral -= 3
```

Beantworte die fünf Fragen der Leseleiter, und dazu diese:

- Was ist `rekrut` — Klasse oder Objekt?
- Woher kommt `moral`? Nenn die wahrscheinlichste Stelle.
- Was macht der Punkt in `rekrut.melde(...)`, und was in `rekrut.moral`?
- Wann läuft `melde()` — und wann nicht?
- Was passiert, wenn `moral` genau 5 ist?
- Was steht nach der letzten Zeile in `moral`, und **wo** steht es?
- **Woher kommt der Name `Rekrut`?** Aus dieser Datei, aus einem Import, oder von `self`?

---

### 15. Committe 9b

- Keine `###`-Zeilen, kein `breakpoint()`, keine Wegwerf-Zeilen in `spiel.py`.
- Führ `diff` noch einmal — hat `__repr__` versehentlich etwas an der Ausgabe geändert?
- Commit: `Etappe 9b: Objekte zeigen, was in ihnen steckt`

---

## Was NICHT in diese Etappe gehört

**Keine Vererbung.** Du hast gleich zwei Klassen, die sich ähneln, und es wird dich jucken, eine gemeinsame Oberklasse zu bauen. **Tu es nicht.** Etappe 11 stellt die Frage, *ob* du Vererbung überhaupt brauchst — und diese Frage ist wertlos, wenn du sie vorher unbesehen beantwortet hast.

**Keine vier Marine-Klassen.** Deine Spielerklasse ist heute ein String in einem Attribut. Punkt.

**Kein zweiter Marine, kein Trupp.** Auch der kommt in Etappe 11, und dort ist er die halbe Etappe.

**Keine Objekte in Objekten.** Ein `Inventar`-Objekt statt einer Liste, ein `Waffe`-Objekt im Marine — das ist Etappe 10, und es heißt Komposition.

**Kein `Welt`-Objekt.** `kern_integritaet` und die Gegnerlisten bleiben lose. Etappe 12.

**Keine Wirkung für `level`.** Etappe 18.

**Und die Gegnerlisten bleiben zwei.** Der Zusammenbruch ist Etappe 11 — der Zahltag für einen Schmerz, den du seit Etappe 6 mit dir trägst.

> **Die Regel hinter allen sechs Punkten: Heute wird umgebaut, nicht erweitert.** Das ist dieselbe Regel wie in Etappe 7a, und sie ist der Grund, warum dein `diff` am Ende leer sein muss.

---

## Selbsttest

Prüft einen **Zustand**, nicht dein Selbstbild.

- [ ] `diff vorher.txt nachher.txt` zeigt keinen Unterschied.
- [ ] In `spiel.py` gibt es keine lose Variable mehr, die einem Marine gehört — jede ist ein Attribut.
- [ ] Es gibt **kein** `self.munition`; die Munition steht ausschließlich in `marine.vorrat`.
- [ ] `kern_integritaet` ist **nicht** im Marine gelandet.
- [ ] Mindestens drei Funktionen aus Etappe 7 sind Methoden geworden, und ihre Parameterlisten sind dabei kürzer geworden.
- [ ] Deine Zeichenfunktionen aus 7b sind **keine** Methoden geworden.
- [ ] `print(marine)` zeigt eine lesbare Zeile, keine Speicheradresse.
- [ ] `print()` einer Liste von Gegner-Objekten ist lesbar.
- [ ] Die Gegnerlogik in `spiel.py` arbeitet unverändert mit den zwei Listen aus Etappe 6.
- [ ] Du kannst an einer beliebigen Stelle deines Codes sagen, ob ein Name lokal ist oder an `self` hängt.
- [ ] Beide Commits sind gesetzt.

---

## Lernziele

Als Fragen, in `GELERNT.md` zu beantworten, ohne nachzuschlagen.

1. Was ist der Unterschied zwischen Klasse und Objekt?
2. **Was ist `self` — und warum steht es überall?**
3. Wann wird `__init__` aufgerufen, und von wem?
4. Was ist der Unterschied zwischen einem Attribut und einer lokalen Variablen in einer Methode? Was passiert, wenn du `self.` vergisst?
5. Warum steht `self` in der Definition, aber nicht im Aufruf?
6. Wer ruft `__repr__` auf — und warum rufst *du* es nie selbst?
7. Wann läuft `__str__`, wann `__repr__`, und was passiert, wenn nur eines existiert?
8. Was hat sich an deinen Funktionen aus Etappe 7 geändert, und was nicht?
9. **Woran entscheidest du, ob ein Wert in ein Objekt gehört oder nach draußen?**
10. Was bedeutet das Wort „Klasse" in diesem Projekt — und in welchem der beiden Sinne?
11. Woran erkennst du beim Lesen, ob ein Name aus dieser Datei, aus einem Import oder von `self` kommt?

**Frage 2 ist die wichtigste**, und sie ist erst beantwortet, wenn du ohne das Wort „magisch" auskommst.

**Frage 9 ist die kniffligste** und die einzige, die kein Werkzeugwissen ist. Sie kommt in Etappe 12 wieder, und dort kostet eine falsche Antwort einen Umbau.

---

## Transferaufgabe (10–15 Minuten)

**Außerhalb des Spiels**, in einer Wegwerf-Datei. Eine Bibliothek, kein Vorposten.

1. Schreib eine Klasse `Buch` mit `titel`, `autor`, `seiten` und `ausgeliehen` (Startwert `False`).
2. Gib ihr eine Methode `leihe_aus()`, die `ausgeliehen` auf `True` setzt — **aber nur, wenn es nicht schon ausgeliehen ist.** Sonst gibt sie eine Meldung aus.
3. Gib ihr `__repr__` in der üblichen Form, mit `!r` bei den Strings.
4. Erzeug **zwei** Bücher und leih eines davon aus. Druck danach **beide**.

**Und jetzt der eigentliche Punkt:**

5. **Sag voraus**, was `ausgeliehen` beim zweiten Buch ist, *bevor* du es ausführst. Schreib die Vorhersage auf.
6. **Bau den Fehler ein:** Schreib in `leihe_aus()` `ausgeliehen = True` statt `self.ausgeliehen = True`. Führ aus. **Es knallt nicht.** Was ist stattdessen passiert, und woran hättest du es gemerkt, wenn du es nicht absichtlich eingebaut hättest?
7. Finde ihn mit dem Debugger: `breakpoint()` in der Methode, `p ausgeliehen` und `p self.ausgeliehen` im Vergleich.

**Schritt 6 ist der Kern der Aufgabe.** Er verbindet das vergessene `self.` mit dem Typ-3-Fehler aus Etappe 8 — und er ist der Fehler, den du in den nächsten Monaten am häufigsten machen wirst.

---

## Kaputtmachen

**Vor jedem Experiment aufschreiben, was passieren wird.** Die ersten vier gehören dazu, die letzten zwei sind Kür.

**1. Lass `self` bei einer Methode weg.** Schreib `def zeige_status():` ohne Parameter und ruf `marine.zeige_status()` auf. Lies die Fehlermeldung genau — sie sagt etwas über die Anzahl der Argumente. **Erklär, warum dort von einem Argument die Rede ist, obwohl du keines übergeben hast.**

**2. Greif auf ein Attribut zu, das `__init__` nie gesetzt hat.** Nimm eine Zeile aus `__init__` heraus und lass eine Methode darauf zugreifen. Welcher Fehler kommt, und in welchem Moment?

**3. ⭐ Vergiss das `self.` bei einer Zuweisung.** Schreib in einer Methode `trefferpunkte = 50` statt `self.trefferpunkte = 50`. **Es knallt nicht.** Prüf danach von außen, was in `marine.trefferpunkte` steht.

**Das ist der Typ-3-Fehler dieser Etappe** — der wichtigste. Beantworte, bevor du weiterliest: Wohin ist der Wert 50 gegangen, und wie lange hat er dort gelebt?

**4. Nimm `__repr__` heraus** und druck eine Liste mit drei Objekten. Vergleich die Ausgabe mit der von vorher. **Stell dir vor, das wären zwanzig Gegner in Etappe 12** und du suchtest einen bestimmten davon.

---

Die folgenden zwei sind Kür.

**5. Ruf eine Methode ohne Klammern auf.** `if marine.ist_am_leben:` statt `if marine.ist_am_leben():`. Was gibt der Zweig aus, und zwar bei **jedem** Wert? Warum ist das schlimmer als ein Absturz?

**6. Lass `__repr__` sich selbst aufrufen.** Schreib `return f"Marine({self})"` und druck das Objekt. Lies die Fehlermeldung und erklär in einem Satz, warum sie so lang ist.

---

**Experiment 1 und 3 sind das Paar, auf das es ankommt.** Beide handeln vom vergessenen `self`, und sie zeigen die zwei Gesichter: Einmal knallt es sofort, einmal nie. Wer nur eines macht, lernt die halbe Wahrheit.

Alles in `GELERNT.md` und ins Fehlertagebuch aus Etappe 8, mit dem einen Satz: **woran du es erkannt hättest.**

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `TypeError: … takes 0 positional arguments but 1 was given` | `self` fehlt in der Methodendefinition | Die `def`-Zeile der Methode, nicht die Aufrufstelle |
| `TypeError: __init__() missing 1 required positional argument` | Beim Erzeugen fehlt ein Wert | Die Zeile `Marine(...)` — Anzahl gegen `__init__` zählen |
| `AttributeError: 'Marine' object has no attribute 'x'` | `x` wurde nie in `__init__` gesetzt — oder ist vertippt | `__init__` durchgehen. Vertippt zählt auch |
| `NameError: name 'trefferpunkte' is not defined` | Eine Stelle zeigt noch auf die alte lose Variable | Genau die Zeile, die im Traceback steht — Schritt 3 |
| Die Methode rechnet, aber draußen ändert sich nichts | `self.` bei der Zuweisung vergessen — es entstand eine lokale Variable | Konzept 4. Der Typ-3-Fehler dieser Etappe |
| `print(marine)` zeigt `<__main__.Marine object at 0x…>` | `__repr__` fehlt oder ist falsch eingerückt | Steht sie **in** der Klasse, auf Höhe von `__init__`? |
| `__repr__` gibt `None` aus | `print` statt `return` in der Methode | Konzept 9 — dieselbe Falle wie in Etappe 7 |
| `RecursionError` beim Drucken | `__repr__` benutzt `{self}` und ruft sich selbst | Attribute einsetzen, nicht das Objekt |
| Ein `if` mit einer Methode ist immer wahr | Klammern beim Aufruf vergessen | Konzept 5, Warnkasten |
| Munition läuft auseinander | Zwei Speicher: `marine.vorrat["munition"]` **und** eine lose Variable | Schritt 3 — es darf nur einen geben |
| `IndentationError` direkt nach `class` | Der Körper ist nicht eingerückt | Die Zeile unter `class` |
| Methoden sind versehentlich Funktionen geworden | Zu weit links — eine Ebene zu wenig eingerückt | Alle `def` in der Klasse auf gleicher Höhe |

**Der Debugging-Reflex dieser Etappe: „Wem gehört dieser Wert?"**

Seit Etappe 8 gilt *halt an und sieh nach*. Heute kommt eine Frage dazu, die der Debugger direkt beantwortet:

```
(Pdb) p trefferpunkte        → lokal, oder gar nicht vorhanden
(Pdb) p self.trefferpunkte   → das Attribut am Objekt
```

**Zwei Zeilen, die den häufigsten Fehler dieser Etappe in fünf Sekunden aufklären.** Wenn beide existieren und verschiedene Werte zeigen, hast du dein `self.` irgendwo vergessen.

---

## Ein Blick nach vorne

**Etappe 10 ist Komposition.** Aus `self.inventar = ["medkit"]` wird ein eigenes `Inventar`-Objekt, aus einem Waffennamen ein `Waffe`-Objekt. Ein Marine *hat* Dinge, und diese Dinge sind selbst Objekte. Dort kommt auch die Falle mit den geteilten Objekten: zwei Marines, ein Inventar.

**Etappe 11 ist die große Ernte** — und die Frage, ob du Vererbung überhaupt brauchst. Dort passiert dreierlei gleichzeitig: Deine zwei Gegnerlisten kollabieren endlich zu einer, aus dem einen Marine werden **vier** (drei davon steuert das Spiel selbst — der Trupp), und aus deiner Spielerklasse als String werden vier echte Python-Klassen. **Die `Gegner`-Klasse von heute steht dort neben `Marine`, und die Frage, was die beiden gemeinsam haben, ist der Einstieg.**

**Etappe 12 gibt `kern_integritaet` ihr Zuhause.** Alles, was heute lose geblieben ist, wird zur `Welt` — und deine Antwort auf die Design-Entscheidung von heute wird dort geprüft.

**Etappe 13** macht aus „Erfahrung bis zur nächsten Stufe" und einer Abklingzeit dasselbe Zählermuster. Deine Stufenmethode von heute ist die halbe Vorarbeit.

**Etappe 18 gibt `level` endlich Wirkung** — jede Stufe zahlt einen Skillpunkt aus. Fünfzehn Etappen hat die Erfahrung dann mitgezählt, ohne etwas zu tun. Das war Absicht.

**Etappe 19 speichert deine Objekte.** Was heute Attribut ist, muss dort in eine Datei und wieder heraus. Alles, was du sauber an `self` gehängt hast, macht das leicht.

**Etappe 24** beantwortet die Frage, die du heute beim Lesen gestellt hast — *woher kommt dieser Name?* Dort baust du Module selbst, und `from einheiten import Marine` soll ein Wiedererkennen sein, kein Rätsel.

---

## Abschluss

**In `GELERNT.md`:**

- Was habe ich gebaut? *(Ehrliche Antwort: kein neues Feature. Wieder.)*
- Was habe ich verstanden?
- Was hat mich überrascht? *(Kandidaten: wie kurz die Parameterlisten wurden · dass ein vergessenes `self.` nicht knallt · wie viel `__repr__` im Debugger ausmacht.)*
- Welchen Fehler habe ich gemacht — und **wie habe ich ihn gefunden?**
- ⭐ **Die Design-Entscheidung:** Woran habe ich entschieden, ob ein Wert in den Marine gehört? Welche Werte waren schwer einzuordnen? *(Das liest du in Etappe 12 wieder.)*
- ⭐ **Die Notiz aus Etappe 7 im Rückblick:** Waren es tatsächlich die Werte, die du damals als „immer gemeinsam" notiert hast, die heute Attribute wurden?
- Was hätte ich in Etappe 7 anders gemacht, wenn ich Klassen schon gekannt hätte?

**Vor dem Commit:** `diff` leer? Keine `###`-Zeilen, kein `breakpoint()`? Nur ein Speicher für die Munition?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest. Alles freiwillig.

**Erzeug einen zweiten Marine in einer Wegwerf-Datei.** Nicht im Spiel — nur um zu sehen, dass es geht. Ändere bei einem die Trefferpunkte und druck beide. **Das ist der Beweis für den Satz aus „Worum es geht"**, und es ist ein Vorgeschmack auf Etappe 11.

**Zähl deine Parameter.** Notier vor und nach dieser Etappe, wie viele Parameter deine längste Funktion hatte. Die Differenz ist das, was `self` für dich getan hat — und sie ist überzeugender als jede Erklärung.

**Schreib `__repr__` für eine Klasse aus einer fremden Domäne** und lass jemanden raten, was das Objekt ist, ohne den Code zu sehen. Wenn er es nicht kann, ist deine `__repr__` zu knapp. Das ist die einzige Qualitätsprüfung, die es für diese Methode gibt.

**Lies deine eigenen Docstrings mit `help()`, alle.** Nach Etappe 7 hast du das schon einmal gemacht. Jetzt zeigt sich zusätzlich, welche davon noch von Parametern reden, die es nicht mehr gibt.

---

> **Nächste Etappe:** Etappe 10 — Komposition · Objekte in Objekten, und was passiert, wenn sich zwei Marines ein Inventar teilen
