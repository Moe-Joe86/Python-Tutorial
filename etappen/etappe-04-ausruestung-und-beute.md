# Etappe 4 — Ausrüstung und Beute

> **Block 1: Fundament** · Etappe 4 von 30 · [← Etappe 3](etappe-03-die-wellenschleife.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 5 →](etappe-05-vorposten-und-depot.md)

**Boot.dev:** Listen, `append()`, `remove()`, `len()`, Indexing
**Zeitaufwand:** 3–5 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 3c abgeschlossen, Selbsttest grün

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Inventar, Gegnerliste, `.split()`, die Anmarschbahn | Warum `append()` nichts zurückgibt · zwei Namen, ein Objekt | Der Begriff *mutable* |

---

## Worum es geht

Dein Vorposten hält seit Etappe 3. Er hält gegen eine Zahl.

Sieh dir an, was in deinem Programm gerade einen Gegner darstellt: eine Variable, in der steht, wie viele noch übrig sind. Du feuerst, sie wird kleiner. Das funktioniert — und es hat eine Grenze, die du sofort spürst, sobald du eine ganz normale Frage stellst:

> *Welcher* Gegner ist am nächsten dran?

Das kannst du nicht beantworten. Nicht weil dir Python fehlt, sondern weil in deinem Programm gar keine einzelnen Gegner existieren. Es gibt eine Anzahl. Eine Anzahl hat keine Position, keinen Zustand und keine Reihenfolge. Man kann sie hochzählen und runterzählen, mehr nicht.

Dasselbe von der anderen Seite: Nach einer Welle liegt Zeug im Vorfeld. Schrott, ein Munitionskasten, irgendein Ding von der Brut. Mit Einzelvariablen könntest du das aufheben — `hat_schrott = True`, `hat_kasten = True` — und beim dritten Fundstück merkst du, dass du eine Variable pro möglichem Gegenstand brauchst und beim vierten wieder den Code anfassen musst.

**Beides ist dasselbe Problem, und es hat einen Namen, unter dem diese ganze Etappe steht:**

> **Dinge statt Zahlen.**

Du hast Einzelwerte, wo du eine Sammlung brauchst. Genau dafür gibt es Listen, und heute lernst du sie an zwei Stellen gleichzeitig — an deinem Inventar und an deinen Gegnern.

**Und jetzt der Satz, der über den Rest der Etappe entscheidet: Was ist ein Gegner heute eigentlich?**

Noch kein Objekt. Objekte kommen in Etappe 11. Heute ist ein Gegner nur **eine Zahl — die Stelle, an der er steht:**

```python
gegner = [7, 4]
```

Zwei Gegner. Einer auf Feld 7, einer auf Feld 4. Mehr weiß dein Programm über sie nicht, und mehr braucht es heute nicht.

**Diese Liste ist der Spielzustand.** Sie zu ändern heißt, dass sich im Spiel etwas ändert. Alles andere ist Anzeige.

Und weil du die Gegner jetzt einzeln hast, kannst du sie zum ersten Mal **zeigen**:

```
S..K...K....@
```

Das ist die Anmarschbahn. Links kommt die Brut heraus, rechts steht dein Tor, dazwischen laufen zwei Krabbler. **Sie wird aus `gegner` erzeugt und ist selbst kein Zustand** — das `"K"` steht nirgends in deinen Daten, nur in der Ausgabe.

Es ist eine Liste, mehr nicht — und trotzdem der Abend, an dem dein Spiel aufhört, eine Zahlenkolonne zu sein.

**Merk dir den Weg, den diese eine Liste im Rest des Plans nimmt.** Sie ist der Faden, an dem die nächsten fünfzehn Etappen hängen:

```
Etappe 3    gegner_anzahl = 3                  eine Zahl
Etappe 4    gegner = [7, 4, 2]                 Positionen
Etappe 11   gegner = [Gegner(...), ...]        Objekte mit HP und Typ
Etappe 12   jedes Objekt tickt                 eigener Zustand über Zeit
Etappe 14a  Positionen werden (x, y)           auf einem Raster
Etappe 19   dieser Zustand wird gespeichert
```

Jeder Schritt ersetzt nur, *was in der Liste steht* — nie, dass es eine Liste ist.

---

## Der lange Bogen

| Was du heute anlegst | Wo es wieder auftaucht |
|---|---|
| Die Gegnerliste der laufenden Welle | **12** — sie wird zu `self.einheiten`, über die der Tick läuft |
| „Eine Liste nicht verändern, während man über sie läuft" | **12** — als echtes Problem; **16** — als Kandidat der Bug-Jagd |
| Zwei Namen können auf dasselbe Objekt zeigen | **10** — zwei Marines teilen sich versehentlich ein Inventar; **14a** — `[["."] * 5] * 5` |
| `inventar` als Liste von Strings | **11** — wird zur Liste von `Item`-Objekten |
| Kennung ↔ Anzeigename eines Gegenstands | **11** — `item.id` und `item.name`; **25** — die Kennung wird JSON-Schlüssel |
| Obergrenze von zehn Gegenständen | **20** — „Inventar voll" wird ein sauber abgefangener Fall |
| `remove()` scheitert an einem fehlenden Element | **20** — daraus wird `try` / `except` |
| Index ab 0, `len()` | **14a** — `vorfeld[y][x]` und `range(len(vorfeld))` |
| `in` bei einer Liste | **6** — Gegenüberstellung Liste / Set / Dictionary |
| **Die Frage: Menge oder mehrere Dinge?** (Munition bleibt eine Zahl) | **6** — dieselbe Frage für vier Strukturen; **25** — welche Inhalte werden JSON |
| `for` über eine Liste statt über `range()` | **12** — der Tick läuft über die Einheitenliste; **14a** — dieselbe Schleife über ein Raster |
| Zwei identische Gegenstände sind nicht unterscheidbar | **11** — genau deshalb werden aus Strings Objekte |
| `.split()` für Zwei-Wort-Befehle | **5** — `kaufe medkit`; **7a** — `verarbeite_befehl()` |
| Schrott als Währung | **5** — der Kaufvorgang; **22** — Kosten in Bauplänen |
| Der Datenkern der Brut (heute nutzlos) | **15** — er wird zur ersten Erkenntnis |
| **Die Anmarschbahn als eine Zeile** ⭐ | **14a** — aus einer Zeile wird ein Raster; **7b** — sie wandert in `zeichne_bahn()` |
| Position eines Gegners ↔ Zeichen an dieser Stelle | **14a** — Position als Tuple, Zeichen aus dem Raster |
| Die Darstellung als Debugging-Werkzeug | **8** — Fehler sehen statt sie zu lesen; **16** — Reihenfolgefehler im Tick |
| Bauen in drei Schritten statt einem | **8** — genau dieses Halbieren ist das Suchverfahren |

**Sieben Schulden werden heute eingelöst — mehr als in jeder Etappe zuvor.** Das ist kein Zufall: Etappe 4 ist der Punkt, an dem das Fundament aus 1 bis 3 zum ersten Mal zusammenläuft.

| Aus Etappe | Was versprochen wurde | Wo es heute passiert |
|---|---|---|
| **1** | „Ein Name zeigt auf einen Wert" statt „eine Variable ist ein Behälter" | Konzept 9 — zwei Namen, ein Objekt |
| **2** | Truthy und Falsy, besonders die `0` | Konzept 11 — die leere Liste ist falsy |
| **2** | `.strip()` auf Eingaben | Konzept 12 — beim Zerlegen von `nimm  schrott` |
| **3a** | `range()` zählt ab 0, die zweite Zahl ist nicht dabei | Konzept 3 — derselbe Grund, warum der erste Index 0 ist |
| **3b** | `.lower()` auf der Eingabe | Konzept 12 — dieselbe Kette, jetzt mit `.split()` |
| **3b** | Die einwortige Befehlssprache, bewusst gewählt | Konzept 12 — heute wird sie umgebaut, und du merkst, was das kostet |
| **3c** | Der Balken als erste Anzeige | Konzept 14 — die Anmarschbahn kommt daneben |

Die sechste Zeile ist die interessanteste. In Etappe 3b hast du dich für einwortige Befehle entschieden und es stand dabei, dass Etappe 4 den Umbau erzwingt. Heute ist es so weit. Achte darauf, wie sich das anfühlt — es kostet dich zehn Minuten, und in Etappe 25 wirst du dieselbe Sorte Entscheidung noch einmal treffen, dann für ein ganzes Content-System.

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

Zwei Fragen. Beide haben mehr als eine vertretbare Antwort, und beide haben Folgen, die du erst in einigen Monaten siehst. Schreib deine Wahl **und die Begründung** in `GELERNT.md`.

### Entscheidung 1 — Kennung oder Anzeigename?

Was steht in deiner Liste?

| | Kennung | Anzeigename |
|---|---|---|
| Sieht so aus | `"munitionskasten"` | `"Munitionskasten (halbvoll)"` |
| Der Spieler tippt | genau das | irgendetwas anderes, du musst übersetzen |
| Beim Vergleichen | ein direkter Vergleich | Groß-/Kleinschreibung, Leerzeichen, Klammern |
| Beim Anzeigen | sieht karg aus | sieht gut aus |

**Die Frage dahinter ist größer als sie wirkt:** Ist ein Gegenstand *ein Wort* oder *ein Ding mit einem Namen*? Wenn du dich für die Kennung entscheidest, brauchst du irgendwo eine zweite Stelle, an der steht, wie eine Kennung schön heißt — und diese zweite Stelle wird in Etappe 5 dein Depot und in Etappe 25 eine JSON-Datei. Wenn du dich für den Anzeigenamen entscheidest, sparst du dir das heute und zahlst es in Etappe 11, wenn aus Strings Objekte werden.

Es gibt hier keine Antwort, die ich dir vorsagen könnte. Es gibt nur die Antwort, die du in vier Monaten wiedererkennst.

### Entscheidung 2 — Wo *ist* ein Gegner? ⭐

Das ist die wichtigere der beiden, und sie ist unauffällig genug, dass die meisten sie treffen, ohne sie zu bemerken.

Ein Gegner steht auf Feld 7 der Anmarschbahn. Wo steht das im Programm?

| | Die Bahn ist die Wahrheit | Die Bahn ist nur ein Bild |
|---|---|---|
| Was in der Liste steht | Zeichen: `[".", ".", "K", ".", "K", "@"]` | Positionen: `[2, 4]` |
| Bewegen heißt | Zeichen von Feld 7 nach Feld 8 verschieben | die Zahl um eins erhöhen |
| „Wo steht Gegner 2?" | die ganze Bahn absuchen | direkt ablesen |
| Zwei Gegner auf einem Feld | unmöglich | möglich, und du musst entscheiden, was du zeichnest |
| Ein Gegner bekommt Trefferpunkte | geht nicht — ein Zeichen hat keine | eine zweite Zahl daneben, später ein Objekt |

**Der zweite Weg ist der, den dieser Plan meint, und ab hier bin ich deutlicher als sonst:**

> **Deine Gegnerliste enthält Zustandsdaten — heute Positionszahlen. Das `"K"` gehört ausschließlich in die Darstellung und kommt in `gegner` nicht vor.**

Der Grund steht in einem Satz:

> **Ein Zustand und seine Darstellung sind zwei Dinge. Wer sie zu einem macht, kann sie später nicht trennen.**

In Etappe 14a wird aus der Zeile ein Raster, in Etappe 12 tickt jeder Gegner, in Etappe 19 wird sein Zustand gespeichert. Ein Gegner, der nur als Zeichen in einer Anzeigezeile existiert, hat nichts, was man ticken oder speichern könnte.

**Bau trotzdem, was du für richtig hältst.** Wenn du Weg 1 nimmst, notier es — dann wissen wir in Etappe 14a, dass dort ein Umbau ansteht, und du weißt, dass er nicht dein Fehler war, sondern der Preis einer Entscheidung.

---

## Die Konzepte

Alle Beispiele hier laufen absichtlich **außerhalb** deines Spiels. Tipp sie in eine Wegwerf-Datei, wenn du sie ausprobieren willst — was in `spiel.py` entsteht, schreibst du selbst.

**Und eine Bitte für diese Etappe im Besonderen:** Listen sind das erste Thema, bei dem du die Antwort selbst finden *kannst*. Wenn du hier gleich liest „diese Methode hängt etwas an" — probier es vorher. Eine Liste ist ein Objekt, und ein Objekt kann man fragen, was es kann:

```python
dir([])          # alles, was eine Liste kann
help([].append)  # was eine bestimmte Methode tut
```

Dreißig Sekunden, und du hast dieselbe Information selbst geholt statt sie gelesen zu haben. Der Unterschied klingt nach nichts und ist der ganze Punkt dieses Projekts: Eine Erklärung *wiederzuerkennen* fühlt sich an wie sie zu *wissen*, und der Unterschied fällt erst auf, wenn niemand da ist, den man fragen kann.

### 1. Eine Liste ist eine geordnete Sammlung

```python
werkzeuge = ["hammer", "zange", "feile"]
```

Drei Dinge, ein Name, **eine feste Reihenfolge**. Das letzte Wort ist der Unterschied zu allem, was in Etappe 6 noch kommt: Eine Liste merkt sich, was zuerst kam. `["hammer", "zange"]` und `["zange", "hammer"]` sind nicht dasselbe.

Eine leere Liste schreibt man `[]`. Sie ist ein völlig normaler Wert — genauso wie `0` eine normale Zahl ist und nicht „keine Zahl".

### 2. Nicht alles wird eine Liste ⚠️

Bevor du irgendetwas umbaust: **Eine Liste ist nicht die bessere Variable.** Sie ist die richtige Struktur für eine bestimmte Sorte Problem, und heute ist die Versuchung groß, alles hineinzuwerfen, was mehr als einmal vorkommt.

Sieh dir an, was in deinem Programm steht, und beantworte für jeden Wert eine einzige Frage:

> **Kann ich die einzelnen Dinge unterscheiden — oder interessiert mich nur, wie viele es sind?**

| Wert | Was es ist | Struktur |
|---|---|---|
| Kernintegrität | eine Menge | Zahl |
| **Munition** | **eine Menge** | **Zahl — bleibt eine Zahl** |
| Schrott | eine Menge | Zahl |
| Gegner der Welle | mehrere unterscheidbare Dinge | Liste |
| Was du bei dir trägst | mehrere unterscheidbare Dinge | Liste |

**Munition ist der Fall, an dem sich das entscheidet.** Vierzig Schuss als Liste aus vierzig gleichen Einträgen wäre technisch möglich, und es wäre falsch: Du kannst diese vierzig Dinge nicht auseinanderhalten, du willst nichts an einem einzelnen davon tun, und die einzige Frage, die du je stellst, lautet „wie viele noch?". Genau das ist eine Zahl.

**Warum das hier so viel Gewicht bekommt und nicht in einem Nebensatz steht:** *„Welche Struktur beschreibt dieses Problem?"* ist die Frage, um die es in Etappe 6 vollständig geht und die dich bis Etappe 25 begleitet. Heute triffst du sie zum ersten Mal — und zwar als Frage, die man auch falsch beantworten kann. Wer nach dieser Etappe alles zu Listen macht, hat Listen gelernt und Modellieren verlernt.

Ein Sonderfall, der dir gleich begegnen wird: **Was ist Schrott im Inventar?**

Er ist eine Menge — und trotzdem landet er heute in der Liste, weil du noch nichts anderes hast. **Ja, du wirst zweimal `"schrott"` untereinander stehen haben. Das ist Absicht, und es ist keine gute Mengenverwaltung.**

Bei zwei Stück ist das komisch, bei fünfzig lächerlich. Sag es dir laut, wenn es passiert — dann verstehst du in Etappe 5 in der ersten Minute, wozu die dritte Struktur da ist.

### 3. Der Index fängt bei 0 an — und du weißt schon, warum

```python
werkzeuge[0]     # "hammer"
werkzeuge[1]     # "zange"
werkzeuge[2]     # "feile"
```

In Etappe 3a hast du gesehen, dass `range(5)` die Zahlen 0, 1, 2, 3, 4 liefert — fünf Stück, aber die 5 ist nicht dabei. Das ist dieselbe Zählweise. Python zählt nicht *„das erste, das zweite"*, sondern *„null Schritte vom Anfang, ein Schritt vom Anfang"*.

**Der praktische Nutzen dieser Sichtweise:** `range(len(werkzeuge))` liefert genau die gültigen Indizes und keinen darüber hinaus. Das ist kein Zufall, sondern derselbe Gedanke zweimal. In Etappe 14a läuft dein gesamtes Raster über diese Konstruktion.

⚠️ **Das heißt aber nicht, dass du normalerweise so über Listen laufen solltest.** Wenn du nur die Elemente brauchst, ist `for ding in liste:` die passende Form — kürzer, lesbarer, und du kannst dich nicht verzählen. `range(len(...))` brauchst du dann, wenn du wirklich mit **Indizes** arbeitest: wenn du die Position kennen musst oder einen Eintrag an einer bestimmten Stelle ersetzt.

Der Reflex `for i in range(len(inventar)): print(inventar[i])` ist einer der häufigsten Anfänger-Umwege überhaupt. Wenn du ihn bei dir siehst, frag: *Brauche ich hier die Nummer, oder nur das Ding?*

### 4. `len()`, der Blick von hinten — und der `IndexError`

```python
len(werkzeuge)      # 3
werkzeuge[-1]       # "feile"  — das letzte
werkzeuge[-2]       # "zange"  — das vorletzte
```

`werkzeuge[len(werkzeuge) - 1]` ist dasselbe wie `werkzeuge[-1]`, nur umständlicher. Beim Lesen fremden Codes wirst du beide Formen sehen.

**Eine Frage, die du dir stellen solltest, bevor du weiterliest:** Was ist `werkzeuge[len(werkzeuge)]`? Sag es dir laut, bevor du es ausprobierst.

**Der ehrlichste Fehler dieser Etappe wartet direkt daneben:**

```
IndexError: list index out of range
```

Er heißt: Du hast nach einer Stelle gefragt, die es nicht gibt. Bei drei Einträgen sind 0, 1 und 2 gültig — und 3 ist es nicht, obwohl es sich nach „der dritte" anfühlt.

**Merk dir diesen Fehler als angenehm.** Er stürzt sofort ab und sagt genau, was los ist. Es gibt in dieser Etappe zwei Fehler, die das nicht tun, und die kosten dich mehr Zeit.

### 5. Etwas hinzufügen — und die Falle dabei ⭐

```python
werkzeuge.append("saege")
```

Das verändert die Liste, die es schon gibt. Es entsteht **keine neue Liste**. Und jetzt der Punkt, an dem fast jeder einmal eine halbe Stunde verliert:

```python
werkzeuge = werkzeuge.append("bohrer")     # ← was passiert hier?
```

Sag deine Vorhersage auf, bevor du es ausprobierst. Danach: `print(werkzeuge)`.

**Und was dabei genau passiert, ist die Hälfte der Lektion:** Die Liste wird tatsächlich erweitert — `append()` tut brav seine Arbeit. Nur gibt es danach nichts zurück, und dieses Nichts (`None`) landet in `werkzeuge`. **Die Liste ist nicht zerstört. Der Name zeigt nur nicht mehr auf sie.** Genau der Satz aus Etappe 1, diesmal mit Folgen.

**Die Regel dahinter ist größer als dieses eine Beispiel.** Es gibt in Python zwei Sorten von Operationen: solche, die ein Objekt **verändern**, und solche, die einen **neuen Wert liefern**. `append()` gehört zur ersten Sorte und gibt deshalb nichts Sinnvolles zurück. Wer das verwechselt, schreibt eine Zeile, die völlig richtig aussieht.

Diese Unterscheidung begleitet dich bis zum Ende des Plans. In Etappe 7b bekommt sie den Namen, der in echtem Code benutzt wird: *Nebenwirkung* gegen *Rückgabewert*.

### 6. Etwas entfernen — laut und nach dem ersten Treffer

```python
werkzeuge.remove("zange")
```

Zwei Eigenschaften, die man kennen muss:

**Es entfernt das erste Vorkommen, nicht alle.** Stehen zwei `"zange"` drin, ist danach noch eine da.

Und daran hängt eine Frage, die heute noch harmlos aussieht: Du trägst zwei Medkits. Du benutzt eines. **Welches?** Die ehrliche Antwort lautet heute: egal, sie sind identisch — es steht zweimal dasselbe Wort in der Liste, und zwischen zwei gleichen Wörtern gibt es nichts zu unterscheiden.

Behalt diese Frage. Sobald zwei Medkits *nicht* mehr identisch sind — eines halb verbraucht, eines abgelaufen —, hört die Antwort auf zu funktionieren, und dann brauchst du etwas, das mehr ist als ein Wort. Das ist Etappe 11, und du hast gerade selbst den Grund dafür gefunden. Das wird dir bei Schrott begegnen, sobald du mehrere Stücke davon hast — und es ist der erste Hinweis darauf, dass Listen für *Mengen* das falsche Werkzeug sind. In Etappe 5 löst ein Dictionary das.

**Und es scheitert laut**, wenn nichts zu entfernen ist:

```
ValueError: list.remove(x): x not in list
```

Heute prüfst du vorher, ob etwas drin ist. In Etappe 20 lernst du die andere Bauweise — es versuchen und den Fehler auffangen — und dann auch, wann welche von beiden die richtige ist.

### 7. `in` fragt, ob etwas drin ist

```python
if "feile" in werkzeuge:
```

Sieht selbstverständlich aus und ist es nicht ganz: Python geht dafür die Liste von vorne durch, bis es etwas findet. Bei fünf Einträgen egal, bei fünfhunderttausend nicht. In Etappe 6 lernst du Strukturen kennen, die für die Frage „ist das drin?" besser geeignet sind — und dann verstehst du, warum es überhaupt mehr als eine Sammlungsart gibt.

### 8. `for` läuft auch durch Dinge ⭐

In Etappe 3 hast du `for` mit Zahlen benutzt:

```python
for i in range(3):
```

Und jetzt der Punkt, der wichtiger ist, als er aussieht:

```python
for werkzeug in werkzeuge:
    print(werkzeug)
```

**Es ist dieselbe `for`-Schleife.** Sie hat sich nicht geändert, sie kann das schon immer. Was sich geändert hat, ist das, worüber sie läuft.

> **`for` interessiert sich nicht dafür, ob rechts Zahlen aus `range()` stehen oder Dinge in einer Liste. Es läuft durch das, was man ihm gibt.**

Damit hast du zum ersten Mal beide Hälften zusammen: In Etappe 3 hattest du eine Schleife und einzelne Werte. Heute hast du eine Schleife und eine Sammlung — und ab jetzt heißt „mach das mit allen" nicht mehr, dass du weißt, wie viele es sind.

**Die Schleifenvariable ist übrigens nur ein Name für den aktuellen Eintrag.** Ihr etwas **zuzuweisen** ändert die Liste nicht:

```python
for ding in werkzeuge:
    ding = "kaugummi"          # die Liste bleibt, wie sie war
```

Der Name zeigt danach woanders hin — die Liste merkt davon nichts. Das ist derselbe Gedanke wie in Konzept 5, und du probierst ihn im Kaputtmach-Teil aus.

*(Die Feinheit dazu, für später: Wenn ein Listeneintrag selbst ein veränderbares Objekt ist, kannst du ihn über die Schleifenvariable sehr wohl verändern — `ding.append(...)` fasst das Objekt an, auf das beide zeigen. Bei Strings und Zahlen geht das nicht, deshalb spielt es heute noch keine Rolle. Ab Etappe 11, wenn deine Liste Objekte enthält, schon.)*

👀 **Beim Lesen fremden Codes** wirst du zwei weitere Formen sehen: `for k, v in daten.items():` und `for i, x in enumerate(dinge):`. Die erste kommt in Etappe 5, die zweite in 14a. Heute genügt es, sie einmal gesehen zu haben und zu wissen, dass es Varianten derselben Sache sind.

### 9. Zwei Namen, ein Objekt ⭐ — die Einlösung aus Etappe 1

In Etappe 1 stand ein Satz, der damals nach Wortklauberei aussah: **Ein Name ist kein Behälter, sondern ein Zeiger auf einen Wert.** Heute wird er zu einem Verhalten, das man sehen kann.

```python
a = [1, 2]
b = a
b.append(3)
print(a)          # Was steht hier? Warum?

x = "hallo"
y = x
y += " welt"
print(x)          # Und hier? Warum anders?
```

**Erst vorhersagen. Beide Zeilen. Dann ausführen.**

Der Unterschied liegt nicht bei `a` und `b`, sondern beim Typ des Werts.

**Bei der Liste:** `append()` fasst genau das Objekt an, auf das beide Namen zeigen. Ein Objekt, zwei Namen, eine Änderung — beide sehen sie.

**Beim String:** `y += " welt"` kann `"hallo"` gar nicht anfassen, weil Strings sich nicht verändern lassen. Also entsteht ein **neuer** String, und `y` zeigt fortan darauf. **Das alte `"hallo"` bleibt unangetastet — und `x` zeigt immer noch darauf.**

Merk dir die zwei Bilder nebeneinander, sie sind wichtiger als das Fachwort:

```
Liste:   ein Objekt  →  wird verändert   →  beide Namen sehen es
String:  ein Objekt  →  bleibt, wie es war  →  ein neuer Wert, ein Name zieht um
```

👀 **Der Fachbegriff, und mehr braucht es heute nicht:** Veränderbare Objekte heißen *mutable*, unveränderbare *immutable*. Listen sind mutable, Strings und Zahlen sind immutable. Ein Satz, dann weiter.

Wenn du wirklich eine zweite, eigenständige Liste brauchst:

```python
b = a.copy()
```

**Warum das hier so viel Platz bekommt:** Das ist die Ursache einer ganzen Familie von Fehlern, die sich anfühlen wie Spuk — irgendwo ändert sich etwas, das niemand angefasst hat. Du triffst diese Familie in Etappe 10 wieder (zwei Marines, ein Inventar), in Etappe 14a (ein Raster, in dem alle Zeilen gleichzeitig kippen) und in Etappe 16 als Kandidat für die Bug-Jagd. Heute ist die einzige Gelegenheit, sie in Ruhe an vier Zeilen anzusehen.

### 10. Zwei Listen, ein Gegenstand wandert

Etwas von A nach B zu bewegen sind in deinem heutigen Listenmodell **zwei Handgriffe**: bei A entfernen, bei B hinzufügen. Es gibt keine eingebaute Listenmethode, die beides auf einmal tut.

*(Eine selbstgeschriebene Funktion kann das später sehr wohl — genau darum geht es in Etappe 7a. Sie besteht dann aus denselben zwei Handgriffen, nur an einer Stelle statt an fünf.)*

Und daraus folgt die Frage, die diese Etappe interessant macht: **Was, wenn der zweite Handgriff nicht klappt?** Dein Inventar ist voll, der Gegenstand ist aber schon aus dem Vorfeld verschwunden. Dann hast du ihn gelöscht statt bewegt.

Die Lösung ist unspektakulär und die Denkweise dahinter nicht: **Prüfe zuerst, ob der Umzug möglich ist. Erst danach fass irgendetwas an.** Das ist der Kerngedanke von Etappe 20 und der Grund, warum Datenbanken Transaktionen haben. Du brauchst heute keinen der beiden Begriffe — nur einmal den Fall gebaut zu haben, in dem etwas verlorengeht.

### 11. Die leere Liste ist falsy — die Einlösung aus Etappe 2

In Etappe 2 stand: Es gibt Werte, die als „falsch" gelten, ohne `False` zu sein — und `0` ist einer davon.

Die leere Liste ist der nächste:

```python
if werkzeuge:
    print("Da ist etwas drin.")
```

Das ist gleichbedeutend mit `if len(werkzeuge) > 0:` und in echtem Python die übliche Form. Beide sind richtig; die kurze wirst du häufiger lesen.

⚠️ **Und hier die Falle, die dazu gehört** — sie ist wichtig genug, dass sie einen eigenen Faden im Lehrplan hat:

```python
if munition:        # heißt: munition ist nicht 0
```

Solange `0` „leer" bedeutet, ist das genau richtig. Sobald `0` ein *gültiger Wert* ist, den man von „nicht gesetzt" unterscheiden muss, ist es falsch — und der Fehler zeigt sich nie sofort. Merk dir die Frage, die dazu gehört und die du ab heute stellst: **Kann diese Variable legitim `0` sein?** In Etappe 10 kommt der Gegenbegriff dazu, in Etappe 18 die Falle in voller Größe.

### 12. `.split()` — aus einer Zeile werden Wörter

```python
"nimm schrott".split()        # ["nimm", "schrott"]
```

Ohne Argument trennt `.split()` an Leerzeichen und wirft überzählige weg. `"nimm   schrott"` mit drei Leerzeichen liefert dasselbe Ergebnis — was dir einen Teil der Arbeit abnimmt, die du sonst `.strip()` überlassen müsstest.

**Und jetzt wird die Entscheidung aus Etappe 3b fällig.** Damals hast du einwortige Befehle gebaut und es stand dabei, dass heute der Umbau kommt. Er kommt jetzt: Aus einer Zeile werden ein Verb und ein Ziel, aus `if befehl == "status"` wird ein Vergleich mit dem ersten Wort.

Drei Dinge, über die dabei jeder stolpert — such dir die Antworten selbst, sie stehen alle in einem `print()`:

1. Was liefert `"".split()`? Und was macht dein Programm dann bei einer leeren Eingabe?
2. Der Spieler tippt nur `nimm`. Wie viele Elemente hat die Liste, und was passiert bei `teile[1]`?
3. Der Spieler tippt `NIMM Schrott`. Wo genau in deiner Kette gehört `.lower()` hin — vor oder nach dem Zerlegen? Macht das einen Unterschied?
4. Tipp das hier in die Konsole und sieh nach, was herauskommt:

   ```python
   "  NIMM   Schrott  ".strip().lower().split()
   ```

   Lies die Kette von links nach rechts und sag vorher, was nach jedem Schritt dasteht. **Das ist die Eingabezeile, die dein Spiel von hier bis Etappe 25 benutzt** — drei Methoden hintereinander, jede gibt einen neuen Wert zurück, auf dem die nächste arbeitet.

**Ehrlich eingeordnet:** Der Umbau selbst ist in zehn Minuten erledigt. Der Wert liegt nicht darin, sondern in dem, was du dabei fühlst — eine Entscheidung von vor zwei Wochen kostet dich heute Arbeit. Das ist die billigste Version dieser Erfahrung, die dieser Plan zu bieten hat. In Etappe 25 machst du dieselbe Sorte Entscheidung noch einmal, dann für dein ganzes Content-System, und dann ist sie nicht mehr billig.

### 13. Die Falle: eine Liste verändern, während man über sie läuft ⭐

Das ist der berühmteste Anfängerfehler dieser Etappe und der einzige, der **nicht abstürzt**.

```python
zahlen = [1, 2, 3, 4, 5, 6]
for z in zahlen:
    if z % 2 == 0:
        zahlen.remove(z)
print(zahlen)          # Vorhersage aufschreiben. Dann ausführen.
```

Wenn dein Ergebnis nicht das ist, was du erwartet hast: Das ist der Punkt. Python merkt sich beim Durchlaufen, an welcher **Stelle** es gerade ist. Entfernst du etwas, rutscht alles dahinter eine Position nach vorn — und der nächste Schritt landet eine Stelle zu weit.

**Das ist ein Fehler vom Typ 3: Er läuft durch und liefert das Falsche.** Keine Fehlermeldung, kein Traceback, nichts. Nur ein Ergebnis, das man für richtig hält, weil nichts dagegen spricht.

Die übliche Antwort darauf heißt: **erst sammeln, dann entfernen.** Ein Durchlauf stellt fest, was weg soll; danach wird entfernt. Wie du das baust, ist deine Aufgabe — du hast alles dafür.

**Und jetzt der Grund, warum das ausgerechnet in dieser Etappe steht:** In einer Textausgabe siehst du diesen Fehler nicht. Auf der Anmarschbahn siehst du ihn sofort — ein Gegner springt zwei Felder weit oder einer verschwindet, den du nie getroffen hast. In Etappe 12 kommt er als echtes Problem zurück, wenn Einheiten während des Ticks fallen. Wer ihn heute einmal *gesehen* hat, erkennt ihn dort in zwei Minuten.

### 14. Die Anmarschbahn — Zustand und Bild sind zwei Dinge

Die Darstellung ist eine Liste fester Länge mit einem Zeichen pro Feld:

```python
# fremdes Beispiel: acht Parkbuchten, in zweien steht ein Auto
buchten = [".", ".", "A", ".", ".", "A", ".", "."]
```

Mehr Datenstruktur ist das nicht. Was daraus eine Anzeige macht, sind zwei Schritte, und beide sollst du selbst finden:

1. **Von den Zuständen zum Bild.** Du hast `gegner = [7, 4]` — zwei Zahlen. Du brauchst eine Liste aus Punkten, in der an den Stellen 7 und 4 ein Zeichen steht. Ein Weg beginnt mit einer Liste aus lauter Punkten in der richtigen Länge — schau dir an, was `["."] * 8` liefert.

   **Und die Bahn wird jede Runde neu gebaut, nicht verändert.** Das klingt nach Verschwendung und ist die einfachere Bauweise: Du musst nie ein altes `K` wieder wegräumen.
2. **Von der Liste zur Zeile.** Du hast eine Liste aus Zeichen und willst eine einzige Zeile. Das geht mit einer Schleife, die aneinanderhängt — und es geht mit einer eingebauten String-Methode, die genau das tut. **Such sie:** `dir("")` zeigt dir alles, was ein String kann, `help("".join)` erklärt eines davon. Nimm dir zwei Minuten für die Suche, bevor du die Schleife baust.

Punkt 2 ist keine Schikane. *Woher weiß ich, was dieses Objekt kann?* ist eine der Fähigkeiten, um die es in diesem ganzen Projekt geht, und `dir()` und `help()` sind die zwei Werkzeuge dafür. In Etappe 27 stehst du vor einem fremden Repo und hast genau diese beiden.

**Der Riegel dazu:** Zehn Minuten, ganz am Schluss, wenn alles andere läuft. Bahnbreite, Rahmenzeichen und hübschere Symbole sind ein Rabbit Hole von derselben Sorte wie das Balancing, und sie fühlen sich genauso nach Arbeit an.

### 15. Der Bauplan: drei Schritte, nicht einer ⭐

Die wichtigste Anweisung dieser Etappe ist keine über Python.

Bau die Anmarschbahn in drei getrennten Schritten, und lass nach **jedem** das Programm laufen:

| Schritt | Was neu ist | Was du siehst |
|---|---|---|
| 1 | **Eine** Position, die pro Runde um eins wächst | Ein Zeichen bewegt sich. Sonst nichts. |
| 2 | Mehrere Positionen in einer Liste | Mehrere Zeichen bewegen sich. |
| 3 | Die Bahn wird aus den Positionen erzeugt | Dasselbe Bild — aber jetzt aus Daten |
| 4 | Getroffene Positionen verschwinden | Und hier schnappt die Falle aus Konzept 13 zu. |

**Der Grund ist rein praktisch.** Wenn du alle vier auf einmal baust und danach etwas nicht stimmt, hast du vier Verdächtige und keinen Anhaltspunkt. Wenn du sie einzeln baust, weißt du immer, welcher Schritt es war — der letzte.

Das ist kein Anfängertrick, sondern das Suchverfahren, das dir in Etappe 8 als **Halbieren statt Durchsuchen** wiederbegegnet, und in Etappe 14a baust du das Raster nach genau demselben Muster.

**Schritt 1 ist außerdem der Moment, um den es heute geht.** Ein einzelnes Zeichen, das sich über den Bildschirm bewegt, weil dein Code es bewegt. Das ist zehn Minuten Arbeit, und es ist der erste Abend, an dem dein Programm etwas *tut*, statt etwas auszugeben.

---

## Dein Auftrag

Nach jedem Schritt ausführen. Nach den Schritten 4, 7 und 9 ist ein Commit sinnvoll, auch wenn erst am Ende der offizielle steht.

1. **Das Inventar als leere Liste anlegen** und den Befehl `inventar` bauen, der zeigt, was drin ist — inklusive des Falls, dass nichts drin ist. Der Unterschied zwischen „leer" und „gar nicht vorhanden" soll für den Spieler sichtbar sein.
2. **Die Befehlskette auf zwei Wörter umbauen.** Eingabe zerlegen, mit dem ersten Wort vergleichen. Die bestehenden Einwort-Befehle aus Etappe 3b müssen danach **unverändert funktionieren** — prüf das ausdrücklich, bevor du weitergehst. Das ist die erste Erweiterung dieses Projekts, die etwas Bestehendes anfasst.
3. **Eine Liste mit dem, was im Vorfeld liegt.** Vier Fundstücke reichen: Schrott, ein Munitionskasten, eine Panzerplatte, ein Datenkern der Brut. Der Datenkern tut heute nichts. Das ist Absicht.
4. **`nimm <ding>` und `ablege <ding>`** — ein Gegenstand wandert zwischen den beiden Listen. Denk an Konzept 10: erst prüfen, ob der Umzug möglich ist, dann bewegen.
5. **Die Obergrenze von zehn Gegenständen** mit einer verständlichen Meldung. Der Gegenstand bleibt dabei liegen, wo er lag.
> **Wenn du hier teilen willst, teil hier.** Nach Schritt 6 steht ein funktionierendes Inventar, und das ist ein sauberer Schnitt mit eigenem Commit (`Etappe 4: Das Inventar ist eine Liste`). Der Lehrplan teilt diese Etappe nicht offiziell — aber die Regel *„Etappen dürfen halbiert werden"* gilt, und dies ist die Stelle, an der es ohne Bruch geht. Die Schritte 7 bis 10 sind ein eigener Abend.

6. **Was passiert bei `nimm hubschrauber`?** Und bei `nimm` ohne zweites Wort? Beides soll den Spieler nicht abstürzen lassen. Noch ohne `try`/`except` — das ist Etappe 20.
7. **Ersetz `gegner_anzahl` durch eine Liste von Positionen.**

   Zu Wellenbeginn entsteht eine Liste mit einer Positionszahl pro Gegner — wie viele, sagt deine Formel aus 3c. Wo sie starten, entscheidest du: alle am Spawnpunkt, oder verteilt.

   Danach gibt es **keine Variable mehr, die zählt, wie viele Gegner übrig sind.** Die Anzahl liest du mit `len(gegner)` aus der Liste ab — überall, auch in deiner `while`-Bedingung.

   Deine Kampflogik aus 3c muss danach dasselbe tun wie vorher: `feuern` entfernt einen Gegner aus der Liste, statt eine Zahl zu senken.
8. **Die Falle bauen und sehen.** Entferne getroffene Gegner absichtlich mitten im Durchlauf. Schreib auf, was du erwartest, führ es aus, vergleiche. Erst danach bau es richtig.
9. **Die Anmarschbahn, in vier Schritten.** Konzept 15 erklärt, warum einzeln und nicht auf einmal. Nach **jedem** Schritt ausführen:

   **9.1 — Ein Gegner bewegt sich.** Setz `gegner = [7]`. Erhöh die Zahl am Ende jeder Runde um eins und zeichne die Bahn neu. Du siehst ein `K`, das nach rechts wandert. Mehr nicht — noch kein Feuern, noch kein Entfernen.

   **9.2 — Mehrere bewegen sich.** `gegner = [7, 4, 9]`. Alle rücken pro Runde ein Feld vor. Dafür brauchst du eine Schleife, die **jede Position** verändert — und hier wirst du merken, dass das Ändern einer Schleifenvariablen nicht reicht (Konzept 8).

   **9.3 — Die Bahn kommt aus den Positionen.** Bau die Darstellung nach Konzept 14: leere Bahn erzeugen, Zeichen an die richtigen Stellen setzen, zu einer Zeile zusammenfügen. **Die Gegnerliste bleibt unangetastet** — die Bahn wird jede Runde neu gebaut.

   **9.4 — Getroffene verschwinden.** Jetzt entfernt `feuern` eine Position aus der Liste. **Und hier schnappt die Falle aus Konzept 13 zu**, wenn du beim Entfernen über die Liste läufst.

   Zehn Minuten gelten für die Optik in 9.3, nicht für alle vier Schritte.
10. **Der Rückwärtsgang:** Spiel eine ganze Welle durch, so wie du es nach Etappe 3c getan hast. Der Balken, das Nachladen, das Wellenende — funktioniert alles noch? Wenn nicht, hast du nicht erweitert, sondern umgebaut.

---

## Was NICHT in diese Etappe gehört

- ❌ **Gegenstände als Objekte mit Eigenschaften** (Gewicht, Schaden, Haltbarkeit) → Etappe 11
- ❌ **Mengen und Stapel** („3× Schrott" statt dreimal `"schrott"`) → Etappe 5, mit einem Dictionary
- ❌ **Kaufen, Verkaufen, ein Depot** → Etappe 5
- ❌ **Gegner mit eigenen Trefferpunkten und Typen** → Etappe 11 und 17a
- ❌ **`try` / `except` beim Entfernen** → Etappe 20
- ❌ **Ein zweidimensionales Vorfeld** → Etappe 14a
- ❌ **Zeichenfunktionen, die als eigene Schicht leben** → Etappe 7b
- ❌ **Wegfindung, Ausweichen, Gegner, die um etwas herumlaufen** → notieren, frühestens nach 27
- ❌ **Balancing** (wie viel Schrott, wie viele Gegner) → notieren, Etappe 21a

**Der verlockendste Punkt ist der erste, und das Gefühl dahinter ist völlig richtig.** Es *stimmt*, dass ein Munitionskasten mehr ist als das Wort `"munitionskasten"` — er hat einen Inhalt, ein Gewicht, vielleicht einen Zustand. Und du wirst heute mehrfach an eine Stelle kommen, an der ein String zu wenig ist.

Bau es trotzdem nicht. Nicht weil es falsch wäre, sondern wegen der Reihenfolge: **Der Grund, warum eine Klasse besser ist als ein String, ist der Schmerz, den ein String macht.** Wer heute Objekte baut, lernt in Etappe 11 die Syntax und hält sie für Zeremonie. Wer heute mit Strings arbeitet und dabei dreimal denkt „hier fehlt was", weiß in Etappe 11 in der ersten Minute, wozu Klassen da sind.

Notier diese Momente. Jedes Mal, wenn dir heute ein String zu dünn vorkommt, schreib eine Zeile in `GELERNT.md`. Diese Liste ist deine Vorbereitung auf Etappe 11 — und sie ist überzeugender als alles, was in einem Guide stehen kann.

---

## Selbsttest

Prüft den Zustand deines Programms, nicht dein Gefühl. Führ jeden Punkt tatsächlich aus.

- [ ] `inventar` bei leerem Inventar sagt etwas anderes als bei vollem — und stürzt nicht ab
- [ ] `nimm schrott` funktioniert, `NIMM  Schrott` mit Großbuchstaben und zwei Leerzeichen auch
- [ ] `nimm` allein tippen führt nicht zum Absturz
- [ ] `nimm hubschrauber` sagt, dass hier so etwas nicht liegt
- [ ] Ein genommener Gegenstand liegt danach **nicht mehr** im Vorfeld — und `nimm` desselben Dings ein zweites Mal meldet, dass da nichts mehr ist
- [ ] `ablege schrott` legt ihn zurück; danach kannst du ihn erneut nehmen
- [ ] Beim elften Gegenstand kommt eine Meldung, und der Gegenstand bleibt liegen, wo er lag
- [ ] Alle Befehle aus Etappe 3b (`feuern`, `status`, `nachladen`, `beenden`) tun genau das, was sie vorher taten
- [ ] In `gegner` stehen **Zahlen, keine Zeichen** — such nach `"K"` in deiner Gegnerliste; es darf dort nicht vorkommen
- [ ] Zu Wellenbeginn steht die richtige Anzahl Gegner in der Liste — nachgezählt, nicht angenommen
- [ ] Die Bahn wird jede Runde neu erzeugt und nicht verändert — ein alter Gegner hinterlässt kein Zeichen
- [ ] Fällt ein Gegner, verschwindet er aus der Liste, und die übrigen bewegen sich normal weiter
- [ ] Über eine ganze Welle hinweg wird **kein** Gegner übersprungen (auf der Bahn nachzählen)
- [ ] Die Bahn ist bei jeder Runde gleich lang — Spawnpunkt links, Tor rechts, dazwischen der Rest
- [ ] Eine komplette Welle lässt sich von Anfang bis Ende spielen, ohne dass etwas abstürzt
- [ ] ⭐ **Such in `spiel.py` nach der alten Gegnerzahl.** Es gibt sie nirgends mehr — keine Variable, die zählt, wie viele Gegner übrig sind. Die Liste *ist* der Zustand, die Anzahl liest du mit `len()` daraus ab. Damit ist der Satz eingelöst, den du nach Etappe 3 in `GELERNT.md` geschrieben hast: *„Gegner sind heute eine Zahl. Ab Etappe 4 eine Liste."*
- [ ] Munition ist dabei **keine** Liste geworden und steht immer noch als Zahl da

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten. Dein Mentor fragt sie ab, und das Erklären ist der Lernvorgang — nicht die Prüfung.

1. Warum ist der erste Index 0? Was hat das mit `range()` aus Etappe 3a zu tun?
2. Was macht `liste[-1]`, und wie schreibt man dasselbe umständlich?
3. Was passiert bei `liste[99]`, wenn drei Einträge drin sind — und warum ist dieser Fehler ein *angenehmer*?
4. **Was verändert `append()` — die Liste selbst, oder gibt es eine neue zurück? Was steht danach in `x`, wenn du `x = x.append(3)` schreibst?**
5. Was ist der Unterschied zwischen `b = a` und `b = a.copy()`? An welchem der beiden Beispiele aus Konzept 9 sieht man ihn, und warum am anderen nicht?
6. Was heißt *mutable*? Nenn je zwei Beispiele. *(Ein Satz genügt — das ist eine 👀-Frage.)*
7. Warum überspringt eine Schleife Einträge, wenn man während des Durchlaufs entfernt? Und warum ist das ein Fehler vom Typ 3?
8. Wie kommst du von „dieser Gegner steht auf Feld 4" zu „an Stelle 4 der Bahn steht ein `K`" — und warum sind das zwei getrennte Dinge?
8b. Was genau steht heute in `gegner`, und was steht dort ausdrücklich **nicht**?
9. Was liefert `"nimm".split()`, und was passiert danach bei einem Zugriff auf das zweite Element?
10. Warum ist `if inventar:` dasselbe wie `if len(inventar) > 0:` — und bei welcher Art von Variable wäre dieselbe Kurzform gefährlich?
11. **Warum ist Munition keine Liste geworden, das Inventar aber schon?** Nenn die Frage, mit der du das entscheidest.
12. Was hat sich an `for` geändert, seit du es in Etappe 3 benutzt hast — und was nicht?

**Frage 8 ist die wichtigste.** Die anderen neun sind Werkzeugwissen, und Werkzeugwissen holt man nach. Frage 8 ist eine Frage über *Modellierung*: Sie unterscheidet den Zustand deiner Welt von seiner Darstellung. Wenn diese Trennung heute sitzt, sind Etappe 12 (der Tick), Etappe 14a (das Raster), Etappe 19 (Speichern) und Etappe 28 (Pygame) Erweiterungen. Wenn sie nicht sitzt, sind es Umbauten.

---

## Transferaufgabe (10 Minuten)

**Außerhalb des Spiels**, in einer Wegwerf-Datei. Wenn du Listen nur im Kontext deines Inventars bedienen kannst, kannst du keine Listen.

Eine Liste mit drei Namen. Dann der Reihe nach:

1. Gib den zweiten aus.
2. Gib den letzten aus — **ohne** `len()` zu benutzen.
3. Häng einen vierten an.
4. Entferne den ersten.
5. Gib die Länge aus.

Und jetzt der eigentliche Punkt der Aufgabe:

6. Weis die Liste einer zweiten Variablen zu.
7. Entferne über die **zweite** Variable jemanden.
8. Gib die **erste** aus. **Vorher aufschreiben, was du erwartest.**
9. Mach dasselbe noch einmal, aber mit `.copy()` bei Schritt 6. Was ist jetzt anders?

Wenn die Schritte 8 und 9 dich nicht überrascht haben, hast du Konzept 9 verstanden. Wenn doch: gut — genau dafür ist die Aufgabe da, und du hast dir gerade Wochen Fehlersuche gespart.

---

## Kaputtmachen

**Vor jedem Experiment aufschreiben, was passieren wird.** Ein Satz reicht. Das ist der ganze Trick — ohne Vorhersage ist Ausführen nur Zuschauen.

1. **`remove()` mit etwas, das nicht drin ist.** Lies die Fehlermeldung ganz. Welches Wort darin sagt dir, was Python erwartet hätte?
2. **`inventar = inventar.append("medkit")`** und danach `print(inventar)`. Führ danach irgendeinen Befehl aus, der das Inventar benutzt. Wo genau knallt es — an der Zeile, die den Fehler verursacht hat, oder woanders?
3. **Greif auf `liste[len(liste)]` zu.** Warum ist das immer einer zu viel?
4. **Ändere eine Liste über einen zweiten Namen** und gib die erste aus. Mach dasselbe mit einem String. Erklär den Unterschied in einem Satz.
5. ⭐ **Entferne Gegner mitten im Durchlauf**, während die Anmarschbahn läuft. **Das ist der Typ-3-Fehler dieser Etappe:** Es gibt keine Fehlermeldung, keinen Traceback, nichts Rotes. Nur eine Bahn, auf der etwas nicht stimmt. Zähl die Gegner vor und nach der Runde und vergleiche mit dem, was du siehst.
6. **Zeichne die Bahn, bevor die Gegner sich bewegen, statt danach.** Was ändert sich für den Spieler? Und was verrät dir das darüber, an welcher Stelle deiner Schleife die Anzeige stehen sollte?
7. **Setz die Bahnlänge auf 5**, während ein Gegner auf Feld 9 steht. Was passiert — und was *sollte* passieren?
8. **Bau Munition testweise als Liste** aus vierzig gleichen Einträgen. Lass das Spiel eine Welle laufen. Was wird umständlicher? Danach zurückbauen — das ist der Sinn der Übung. **Eine Struktur zu verstehen heißt auch, sie einmal am falschen Problem benutzt zu haben.**
9. **Ändere die Schleifenvariable** in einem `for`-Durchlauf über deine Beute (`ding = "kaugummi"`) und gib die Liste danach aus. Was hast du geändert — den Eintrag oder nur den Namen?

10. **Versuch, alle Gegner mit derselben Methode zu bewegen:** `for pos in gegner: pos += 1`. Gib `gegner` danach aus. **Nichts hat sich bewegt** — und das ist derselbe Grund wie in Experiment 9. Wie musst du es stattdessen bauen, wenn du die Liste wirklich ändern willst?

Experiment 5 ist das wichtigste dieser Etappe. Experiment 6 ist das unterschätzteste: Es ist deine erste Begegnung mit der Frage, in welcher **Reihenfolge** Dinge innerhalb einer Runde passieren. In Etappe 16 wird daraus eine eigene Bug-Jagd.

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `IndexError: list index out of range` | Zugriff auf eine Stelle, die es nicht gibt | Die Stelle, an der du rechnest, *welchen* Index du willst — nicht die Zeile mit den eckigen Klammern |
| `ValueError: list.remove(x): x not in list` | Entfernt wird etwas, das nicht drin ist | Wurde es vorher schon entfernt? Steht dort eine andere Schreibweise? |
| `AttributeError: 'NoneType' object has no attribute 'append'` | Irgendwo steht `liste = liste.append(...)` | Such nach `= ` und `.append` in derselben Zeile |
| `TypeError: object of type 'NoneType' has no len()` | Dasselbe, nur später bemerkt | Dieselbe Suche |
| `TypeError: 'str' object does not support item assignment` | Du behandelst die Bahn als String statt als Liste | Ein String lässt sich nicht an einer Stelle ändern. Eine Liste schon. |
| `IndexError` beim Befehl mit nur einem Wort | `.split()` liefert eine Liste mit einem Element | Prüf die Länge, bevor du auf das zweite zugreifst |
| Kein Fehler, aber Gegner werden übersprungen | Entfernen während des Durchlaufs | Konzept 13 |
| Kein Fehler, aber ein Gegenstand ist doppelt da | Beim Umzug hinzugefügt, aber nicht entfernt | Konzept 10 |
| Kein Fehler, aber ein Gegenstand ist weg | Beim Umzug entfernt, aber nicht hinzugefügt — weil die Prüfung dazwischen scheiterte | Konzept 10 |
| Die Bahn wird jede Runde länger | Sie wird nicht neu gebaut, sondern erweitert | Wo entsteht die Bahn — innerhalb oder außerhalb der Runde? Das ist die Frage aus Etappe 3b |

**Der Debugging-Reflex dieser Etappe: „Was steht da gerade wirklich drin?"**

In Etappe 1 war es *welchen Typ hat dieser Wert?*, in Etappe 2 *welcher Zweig läuft?*, in Etappe 3 *wie oft läuft das?*. Heute:

```python
print("### VOR ", liste, len(liste))
# ... die Zeile, um die es geht ...
print("### NACH", liste, len(liste))
```

Zwei Zeilen, und sie beantworten die Hälfte aller Fragen dieser Etappe. Die Länge gehört ausdrücklich dazu: Bei einer Liste, die neun Einträge haben sollte und acht hat, siehst du das an der Zahl sofort und am Inhalt erst nach dem Nachzählen.

Alle vier Reflexe folgen demselben Grundsatz, und er ist der eigentliche Ertrag von Block 1: **Nachsehen schlägt Vermuten.** In Etappe 8 löst der Debugger diese `print()`-Zeilen ab. Der Reflex bleibt.

---

## Ein Blick nach vorne

**Etappe 5** braucht `.split()` sofort wieder, für `kaufe medkit`. Und dort merkst du, warum eine Liste für Mengen das falsche Werkzeug ist: Drei Stück Schrott dreimal einzeln einzutragen ist die Sorte Lösung, die bei fünfzig Stück lächerlich wird. Ein Dictionary löst das.

**Etappe 6** stellt Liste, Dictionary, Set und Tuple nebeneinander — und beantwortet die Frage aus Konzept 2 für alle vier auf einmal. Dann verstehst du rückwirkend, welche Eigenschaft einer Liste du heute eigentlich benutzt hast — und an welchen zwei Stellen sie dir im Weg war.

**Etappe 7b** holt das Zeichnen der Bahn aus deiner Spiellogik heraus. Ab dann liefert eine Zeichenfunktion Zeilen und gibt sie nicht selbst aus. Das klingt nach einer Feinheit und ist der Grund, warum in Etappe 14a Raster und Statusspalte nebeneinander passen.

**Etappe 8** ist die Bug-Jagd, und deine Anmarschbahn ist dort Werkzeug, nicht Zierde: Ein Fehler, den man sieht, ist ein Fehler, den man findet.

**Etappe 10** bringt Konzept 9 zurück, dann an eigenen Objekten: Zwei Marines teilen sich versehentlich dasselbe Inventar. Wer heute verstanden hat, warum `b = a` keine Kopie ist, erkennt das in zwei Minuten.

**Etappe 11** macht aus deiner Liste von Strings eine Liste von Objekten. Deine Notizzettel aus dem „Was NICHT"-Abschnitt sind dort die Begründung.

**Etappe 12** ist der Punkt, an dem deine Gegnerliste zur `self.einheiten`-Liste der Welt wird, über die der Tick läuft. Und dort ist „nicht entfernen, während man darüber läuft" kein Übungsfall mehr, sondern dein Spiel.

**Etappe 14a** löst die Schuld ein, die du heute anlegst: Aus einer Zeile werden viele. Der einzige neue Gedanke ist die zweite Ebene — eine Liste, deren Elemente selbst Listen sind. Zeichnen kannst du dann längst.

**Etappe 15** löst den Datenkern ein, der heute nichts tut.

**Etappe 20** verwandelt drei Stellen von heute in echte Fehlerbehandlung: das volle Inventar, das nicht vorhandene Element und den Befehl ohne zweites Wort.

---

## Abschluss

**In `GELERNT.md`** — das Format aus dem Lehrplan, und diesmal gehören zwei Entscheidungen hinein:

- Was habe ich gebaut?
- Was habe ich verstanden?
- Was hat mich überrascht? *(Kandidaten: `x = x.append(...)`, die verschwindenden Gegner, `b = a`)*
- Welchen Fehler habe ich gemacht — und **wie habe ich ihn gefunden?**
- **Entscheidung 1:** Kennung oder Anzeigename — und warum?
- **Entscheidung 2:** Ist die Bahn die Wahrheit oder nur ein Bild — und warum?
- Die Notizliste: an welchen Stellen war ein String heute zu dünn?

**Commit:**

```bash
git add .
git commit -m "Etappe 4: Ausrüstung, Beute und die Anmarschbahn"
git push
```

Wenn du zwischendurch schon committet hast: gut. Vier kleine Commits sind besser als einer, der zwei Abende umfasst.

---

## Wenn du mehr willst

Erst bei grünem Selbsttest. Alles hier ist freiwillig und nichts davon wird später vorausgesetzt.

**Beute per Nummer nehmen.** Zeig, was im Vorfeld liegt, als nummerierte Liste (1, 2, 3) und lass `nimm 2` funktionieren. Das ist zwei Zeilen Arbeit und macht den Index körperlich: Der Spieler tippt 2, dein Programm braucht Stelle 1. Diese Verschiebung um genau eins ist derselbe Off-by-One, der dir in Etappe 8 als eigene Fehlerkategorie begegnet — und hier merkst du zum ersten Mal, dass die Zählweise des Menschen und die der Maschine nicht dieselbe ist.

**`ablege` ohne Ziel** legt den zuletzt aufgenommenen Gegenstand ab. Zwei Zeichen Code (`[-1]`), und du merkst sofort, dass eine Liste eine Reihenfolge hat und ein Haufen nicht.

**Ein Gegenstand, der nicht tragbar ist** — eine umgestürzte Stützstrebe, ein festgeschweißtes Panel. `nimm` scheitert daran mit einer eigenen Meldung. Das ist der erste Gegenstand, der eine *Eigenschaft* hat, und die Frage, wo diese Eigenschaft eigentlich stehen soll, ist genau die Frage von Etappe 11. Heute darf die Antwort noch hässlich sein.

**Die Bahn zeigt die Blickrichtung.** Statt `K` für alle: ein anderes Zeichen für einen Gegner, der gerade angreift, ein weiteres für einen, der fällt. Kostet nichts und macht das Bild lesbar.

**Der Datenkern lässt sich untersuchen.** `untersuche datenkern` gibt eine einzige Zeile aus — eine Zahlenfolge, ein Fragment einer Kennung, etwas, das nach einer Nachricht aussieht und keine ist. Du erklärst nichts. Der Spieler auch nicht.

Das ist der beste Zusatz dieser Etappe, und zwar aus einem Grund, der nichts mit Python zu tun hat: Es ist die erste Stelle, an der dein Spiel etwas zeigt, das es nicht auflöst. In Etappe 15 löst du es auf. Bis dahin steht die Zeile da und arbeitet für dich.

---

> **Nächste Etappe:** [Etappe 5 — Der Vorposten und das Depot](etappe-05-vorposten-und-depot.md) · Dictionaries, verschachtelte Dictionaries, `.keys()` / `.values()` / `.items()`
