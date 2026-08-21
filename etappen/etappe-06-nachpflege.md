# Nachpflege zu Etappe 6

Zwei Dateien. Beide sind nötig, damit die Etappe fertig ist.

---

## A — BOGEN.md

### A1. Teil A, Etappe 6 — diese Zeilen an die bestehende Tabelle anhängen

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `AUSBAUTEN` als Katalog (Kennung → Preis) | **18** — Voraussetzungen kommen als Dateneintrag dazu; **22** — Kosten, Bauzeit, Ausbaustufen | offen |
| ⭐ **Ein Set garantiert den Zustand, nicht den Vorgang** — die Prüfung vor dem Abbuchen bleibt nötig | **18** — dieselbe Prüfung, dann mit Voraussetzungen; **20** — aus der Prüfreihenfolge wird Fehlerbehandlung | offen |
| `"zielhilfe"` — eine Freischaltung ohne Wirkung | **18** — sie bekommt dort eine Fähigkeit | offen |
| `GEGNERTYPEN` als verschachteltes Dictionary (langer und kurzer Text) | **15** — Erkenntnisse hängen sich an denselben Eintrag; **25** — wandert nach `content/` | offen |
| Wellenzusammenstellung als `if`/`elif` über die Wellennummer | **17a** — der Budget-Generator ersetzt die Kette | offen |
| **Entscheidung: Typ bei der Welle oder beim einzelnen Gegner** — empfohlen ist „bei der Welle" | **11** — dort wandert der Typ ins Gegnerobjekt; **17a** — der Generator entscheidet pro Gegner | offen |
| `bestiarium` als Auskunftsbefehl, kostet keine Runde — Anwendung aus **3b** | **12** — welche Spieleraktion löst einen Tick aus | offen |
| **Invariante zwischen zwei Sammlungen** (jeder Set-Eintrag existiert als Dictionary-Schlüssel) | **20** — daraus wird eine Prüfung; **26** — daraus wird ein Test | offen |
| **Umbau: `stapelbar` wird zum Set `STAPELBAR`** — Änderung an **5** | **22** — die Eigenschaft geht in die verschachtelte Warentabelle über | offen |
| **Der Preis dieses Umbaus: „nicht im Set" heißt stillschweigend „nein"** | **20** — fehlende Angaben werden zum abgefangenen Fall | offen |
| Der Debugging-Reflex „welche Struktur ist das eigentlich?" (`type()` **und** Inhalt) | **8** — der Debugger löst alle fünf `print`-Reflexe ab | offen |
| 👀 `sorted()` auf einem Set liefert eine Liste | **23a** — `lambda` als Sortierschlüssel | offen |
| ⭐ *(Kür)* Ein Gegnertyp im Bestiarium, der in keiner Welle vorkommt | **17a** — der Generator entscheidet, ab wann er anrückt. *Entfällt, wenn die Kür entfällt.* | offen |

### A2. Teil A — Status von fünf Schulden ändern

| Etappe | Zeile beginnt mit | Neuer Status |
|---|---|---|
| 4 | `` `in` bei einer Liste `` | **eingelöst** ✓ |
| 4 | **Die Frage „Menge oder mehrere unterscheidbare Dinge?"** | **teilweise eingelöst** ✓ (6) |
| 5 | `` `in` prüft beim Dict den **Schlüssel** `` | **eingelöst** ✓ |
| 5 | Schlüssel müssen immutable sein | **eingelöst** ✓ |
| 5 | **Trennung Menge ↔ Einzelstück** | **teilweise eingelöst** ✓ (6) |

### A3. Teil A, Etappe 5 — eine Zeile anpassen

Die Zeile zu `stapelbar` bekommt einen Zusatz in der ersten Spalte:

> **`stapelbar` als zweite flache Tabelle neben `waren`** — zwei parallele Dictionaries mit denselben Schlüsseln. **Ab Etappe 6 ein Set (`STAPELBAR`) statt einer Tabelle aus Wahrheitswerten.**

Ziel und Status bleiben.

### A4. Teil B — sechs Zeilen ergänzen

| Zeile | Ergänzung in „Erwartet aus" / „Was da sein muss" |
|---|---|
| **6** | Erwartet zusätzlich: `.items()`, die Kauf-Prüfreihenfolge aus 5, **`stapelbar` als Umbauobjekt** |
| **11** | Erwartet zusätzlich **6**: `KLASSEN` als Liste der verfügbaren Klassen |
| **15** | Erwartet zusätzlich: **`GEGNERTYPEN` mit langem und kurzem Text** |
| **17a** | Erwartet zusätzlich **6**: die Wellen-Typen-Kette, die hier stirbt |
| **18** | Was da sein muss zusätzlich: **`freigeschaltet`, `AUSBAUTEN`, die zweite Sorte Nein** |
| **20** | Erwartet zusätzlich **6**: `KLASSEN` als Prüfmenge, **„kein gültiges Wort" ↔ „hier nicht möglich"** |

### A5. Teil C — fünf Fäden nachziehen

**Umbautabelle** — neue Zeile:

| Was | Bis | Ab | Regel |
|---|---|---|---|
| **Stapelbarkeit** | 5: Dictionary Name → Wahrheitswert | 6: Set `STAPELBAR` | Die `False`-Einträge fallen weg — sie sind ab jetzt die, die **fehlen**. |

**Invarianten** — Etappe 6 einfügen: … → **5** → **6** (erste Invariante, die zwei Sammlungen verbindet: jeder Set-Eintrag existiert als Dictionary-Schlüssel) → **13** → **20** → **26**.

**Die Debugging-Reflexe** — Etappe 6 anhängen: … → Etappe 5 *unter welchem Namen?* → **Etappe 6 *welche Struktur ist das eigentlich?* (`type()` und Inhalt in einer Zeile — ab hier sehen sich `{}`, `{"a"}`, `(5)` und `(5,)` zum Verwechseln ähnlich)** → **8**.

**Werkzeuge selbst befragen** 👀 — Etappe 6 einfügen: … → 5 (`dir({})`) → **6 (`dir(set())`, und der Vergleich, was ein Set *nicht* kann)** → 9b → …

**Die drei Fehlertypen** — Etappe 6 ergänzen: **Etappe 6 (dreimal abgebucht, Set trotzdem korrekt — die Struktur ist sauber und das Spiel kaputt; zwei Gegner auf einem Feld werden im Positions-Set zu einem)**.

---

## B — Vorposten_Lehrplan.md

Der Abschnitt „## Etappe 6" wird vollständig ersetzt. Drei Gründe, alle drei aus dem Kurzcheck:

1. Er enthält zwei Zeilen fertigen Spielcode (`KLASSEN = …`, `freigeschaltet = {…}`).
2. `freigeschaltet` startet dort mit zwei bereits freigeschalteten Einträgen — im Guide wird beides gekauft.
3. Der Satz *„Mit einem Set ist es strukturell unmöglich"* stimmt nur für den Zustand, nicht für den Vorgang. In dieser Form baut man den Kauf, der zweimal abbucht.

**Ersatztext:**

---

## Etappe 6 — Liste, Dictionary, Set, Tuple

**Boot.dev:** Sets, Tuples, Mengenoperationen

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| `KLASSEN` als Tuple, zwei Sets, Freischaltungen, Bestiarium | Warum ein Set eine Regel *ist* statt sie zu prüfen — und was es trotzdem nicht garantiert | Mengenoperationen · Laufzeit von `in` · Sets und Tuples in JSON |

**Was du baust:**
Keine neue Spielmechanik, eine bessere Wahl der Werkzeuge — und zwei kleine Systeme, die ohne Sets nicht sauber gingen.

**`KLASSEN` als Tuple.** Eine feste Aufzählung, die sich nie ändert. Damit unterscheidet dein Programm „das ist keine Klasse" von „diese Klasse hast du nicht gewählt" — und die ungültige Klassenzahl aus Etappe 1 bekommt endlich eine Stelle, die sie abweist.

**Das Tuple bleibt heute bei `KLASSEN`, und das hat einen Grund.** Die übliche Tuple-Begründung lautet „gut für Koordinaten" — nur hat dein Spiel noch keine, und über etwas zu reden, das man nicht braucht, erzeugt keine Einsicht, sondern eine offene Frage. Ab Etappe 14a sind Koordinaten das schönste Beispiel dafür.

**`freigeschaltet` als Set.** Ein Katalog von Ausbauten wird im Depot gekauft; was gekauft ist, landet im Set. **Das Set ist hier keine Optimierung, sondern eine Spielregel:** Eine Ausbaute zweimal zu besitzen ergibt keinen Sinn, und mit einem Set kann dieser Zustand gar nicht erst entstehen. Die Regel steht nicht mehr in einer `if`-Zeile, die man an der nächsten Stelle vergessen kann — sie steht in der Struktur. Das ist der Unterschied zwischen „ich habe es abgefangen" und „es kann nicht passieren".

**Und die Hälfte, die dazugehört:** Ein Set garantiert den **Zustand**, nicht den **Vorgang**. Es verhindert den doppelten Eintrag, nicht die doppelte Abbuchung. Die Prüfung „habe ich das schon?" verschwindet also nicht, sie wechselt die Aufgabe — vorher hat sie die Daten geschützt, jetzt schützt sie den Kaufablauf. Wer nur die erste Hälfte lernt, baut den Kauf, der dreimal Schrott nimmt und dabei völlig korrekte Daten hinterlässt.

**`gesehene_gegnertypen` als Set.** Der Befehl `bestiarium` zeigt, was dir bisher begegnet ist — und damit auch, wie viel du noch nicht kennst. Die erste Begegnung mit einem Typ bekommt eine ausführlichere Beschreibung als jede spätere. Das ist die erste Sache im Programm, die sich etwas über Wellen hinweg merkt: Alle anderen Variablen beschreiben den Zustand, dieses Set beschreibt die Geschichte.

**Die Modellierungsentscheidung dazu:** Woher weiß dein Programm, welcher Typ anrückt? Ein Gegner ist bis Etappe 11 nur eine Position. Der Typ kann bei der **Welle** liegen (empfohlen, zwanzig Minuten) oder beim **einzelnen Gegner** (ein bis zwei Abende, und man baut mit den Mitteln von Etappe 6 etwas, das Etappe 11 richtig löst). Der Begriff *Modellierungsentscheidung* wird hier eingeführt und kommt in 14a und 19 wieder.

**Der Umbau der Etappe** ist die Einlösung eines Versprechens aus Etappe 5: Die Stapelbarkeitstabelle ist ein Dictionary aus lauter Wahrheitswerten — also ein Set, das sich als Dictionary verkleidet hat. Der Umbau ist für den Spieler unsichtbar und hat trotzdem einen Preis, den der Guide benennt: „nicht im Set" heißt danach stillschweigend „nein".

**Zwei Sorten Nein.** „Dieses Wort kenne ich nicht" und „dieses Wort kenne ich, hier geht es nur nicht" sind verschiedene Meldungen, und der Unterschied ist der zwischen zwei Mengen: dem Katalog und dem Zustand. In Etappe 20 wird daraus ein Prinzip für jeden Befehl, in Etappe 18 die häufigste Meldung des Spiels.

**Mengenoperationen 👀** — Differenz, Schnitt und Vereinigung beantworten mit einem Zeichen, wofür man sonst eine Schleife schreibt. Heute nur wiedererkennen. In Etappe 18 lautet die Frage *„welche Voraussetzungen fehlen mir noch?"*, und die Antwort ist eine Differenzmenge.

**Die Etappe endet mit einer Entscheidungshilfe** — vier Fragen in dieser Reihenfolge, und die Reihenfolge ist Teil der Regel:

> **1. Schlage ich etwas unter einem Namen nach?** → Dictionary
> **2. Sollen Duplikate unmöglich sein und die Reihenfolge egal?** → Set
> **3. Soll sich das nach dem Anlegen nicht mehr ändern?** → Tuple
> **4. Sonst** → Liste

Damit werden auch die drei Fragen beantwortet, die Etappe 5 offen gelassen hat: *Ist es schon enthalten? Darf es doppelt vorkommen? Ist die Reihenfolge Teil der Bedeutung?* Und dazu die Gegenprobe, die wichtiger ist als die Liste: **Wo wäre ein Set falsch?** Im Inventar — zwei Medkits sind zwei Medkits, und ein Set würde das zweite stillschweigend schlucken.

**Das `in`-Experiment — mach es wirklich:** Dasselbe Wort an einer Liste, einem Set und einem Dictionary. Dreimal etwas anderes: Suche im Inhalt, schnelle Suche im Inhalt, Suche im **Schlüssel**. Dazu eine Messung an drei Millionen Einträgen, damit der Geschwindigkeitsunterschied nicht geglaubt, sondern gesehen wird — und die ehrliche Einordnung dazu: Bei zehn Inventareinträgen ist er bedeutungslos.

**Lernziele:**
- Wann Set statt Liste? (Zwei Gründe: Duplikate und Geschwindigkeit bei `in`.)
- Was garantiert ein Set — und was garantiert es ausdrücklich nicht?
- Warum kann ein Set keine Listen enthalten, aber Tuples schon?
- Was ist an einem Tuple unveränderlich, und was nicht?
- Was unterscheidet `(5)` von `(5,)`?
- Was liefert `.items()` für jeden Eintrag — und seit wann benutzt du damit Tuples?
- Die vier Fragen der Entscheidungshilfe, in der richtigen Reihenfolge.
- Wo wäre ein Set im eigenen Spiel die falsche Wahl?
- Die zwei Sorten Nein, an einem eigenen Beispiel.

**Transferaufgabe (10 Min):** Zwei Listen mit Ausrüstungsteilen. Finde ohne Schleife heraus, welche in beiden vorkommen, und welche nur in der ersten. (Je eine Zeile, wenn du das richtige Werkzeug wählst.) Zum Schluss dieselbe Ausgabe dreimal in einem neu gestarteten Programm — bleibt die Reihenfolge gleich?

**Kaputtmachen:** Ein Set mit `{}` statt `set()` anlegen und `.add()` aufrufen. Ein Tuple ändern. `(5)` und `(5,)` mit `type()` befragen. Die „schon freigeschaltet?"-Prüfung weglassen und dreimal dieselbe Ausbaute kaufen — der Typ-3-Fehler der Etappe, bei dem die Daten hinterher makellos aussehen. Und die Anmarschbahn einmal über ein Set aus besetzten Feldern bauen, dann zwei Gegner auf dasselbe Feld stellen.

**Commit:** `Etappe 6: Die richtige Datenstruktur`

---

**Nicht ändern:** Blocktabelle und Portionszahlen. Etappe 6 bleibt eine Portion, das Fundament bleibt bei elf.
