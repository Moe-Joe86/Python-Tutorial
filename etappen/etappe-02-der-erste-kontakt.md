# Etappe 2 — Der erste Kontakt

> **Block 1: Fundament** · Etappe 2 von 30 · [← Etappe 1](etappe-01-der-abwurf.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 3 →](etappe-03-die-wellenschleife.md)

**Boot.dev:** `if` / `elif` / `else`, Vergleiche, Booleans, `and` / `or` / `not`
**Zeitaufwand:** 3 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 1 abgeschlossen — `spiel.py` läuft, Klassenwahl wird eingelesen und bestätigt

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| `if` / `elif` / `else` · `==` `!=` `<` `>` · `True` / `False` · `and` `or` `not` · Einrückung · `.strip()` | `elif` ist nicht dasselbe wie mehrere `if` · warum `0` falsy ist und was das anrichtet | Der Punkt in `wert.methode()` · dass `and`/`or` Werte zurückgeben · wo ein Boolean aufhört |

**Die linke Spalte ist überschaubar, und das ist Absicht.** Alles, was rechts steht, brauchst du heute nicht zu beherrschen — ein Satz dazu genügt. Wer versucht, Truthy/Falsy und Kurzschlussauswertung gleichzeitig mit `if` zu lernen, lernt beides halb.

---

## Worum es geht

Bis gestern lief dein Programm von oben nach unten durch. Jede Zeile einmal, immer dieselbe Reihenfolge, egal was der Spieler eingibt. Es war eine Durchsage.

Heute bekommt es eine Gabelung.

> **Ein Programm mit `if` trifft Entscheidungen. Ab heute kann dein Code zweimal etwas anderes tun, obwohl er einmal geschrieben ist.**

Das ist der größte Einzelsprung der ersten fünf Etappen, und er hat zwei Anwendungen, die zusammengehören.

**Erstens: Die Klassenwahl aus Etappe 1 bekommt Folgen.** Gestern hast du gespeichert, was der Spieler gewählt hat, und es bestätigt. Heute bestimmt diese Wahl Panzerung, Schaden, Trefferpunkte und Startausrüstung. Der Heavy hält aus, was den Medic umwirft. Ab heute ist die Klassenwahl eine Entscheidung und keine Kosmetik.

**Und zwar für genau eine Figur.**

> **Heute gibt es in deinem Python-Code eine einzige Spielerfigur.** Die vier Klassen sind vier mögliche Ausprägungen dieser einen Figur — nicht vier Figuren.

Das ist wichtig, weil in der Prämisse vier Marines gleichzeitig auf dem Feld stehen. Im Code kommen die anderen drei erst in Etappe 11 dazu, wenn du Klassen hast, in denen sie wohnen können.

Wer heute vier Wertesätze anlegt, erzeugt Daten, die das Spiel monatelang nicht anfasst — und verdeckt dabei genau das, was diese Etappe zeigen soll: **Eine `if`/`elif`-Kette wählt einen Zweig aus. Einen.**

**Zweitens: Der erste Schuss.** Ob du feuern kannst, hängt an mehreren Dingen gleichzeitig — Munition, Nachladezustand, ob überhaupt ein Ziel da ist. Das ist die erste Stelle, an der eine Bedingung aus mehreren Teilen besteht, und die Form, in der du das schreibst, entscheidet darüber, ob dein Code in Etappe 18 noch lesbar ist.

Und ganz nebenbei löst du eine Schuld ein, die Etappe 1 offen gelassen hat: Als du dort `9` eingegeben hast, hat dein Programm behauptet, du spielst eine Klasse, die es nicht gibt. Heute hast du das Werkzeug dagegen.

---

## Der lange Bogen

**Lies diesen Abschnitt einmal und vergiss ihn dann.** Er ist Buchführung, keine Hausaufgabe — du musst dir nichts davon merken, um heute weiterzukommen.

**Was Etappe 1 offen gelassen hat und heute beglichen wird:**

- `=` heißt „bekommt den Wert" — heute kommt `==` dazu, die Feststellung neben dem Befehl.
- Die Klassenwahl war eine gespeicherte Zahl ohne Wirkung — ab heute bestimmt sie deine Werte.
- Eingabe `9` lief stillschweigend durch — der `else`-Zweig fängt sie ab.

**Was heute entsteht und später wieder auftaucht** — die drei, auf die es ankommt:

| Was entsteht | Wo es wiederkommt |
|---|---|
| **Die `if`/`elif`-Kette für die Klassenwerte** | **11** — sie stirbt, vier Python-Klassen übernehmen |
| **Die verknüpfte Bedingung mit `and`** | **18** — daraus wird ein System aus Freischaltungen |
| **Die Null-Falle** (`0` ist falsy) | **4**, **10**, **18** — sie kommt dreimal in neuer Verkleidung |

*(Kleinkram wie `meldung_abgesetzt`, `.strip()` oder die Punkt-Schreibweise steht vollständig in `BOGEN.md`. Dort gehört er hin, nicht in deinen Kopf.)*

**Die erste Zeile ist die auffälligste.** Du baust heute eine `if`/`elif`-Kette, von der im Lehrplan steht, dass sie hässlich wird — und sie soll trotzdem so gebaut werden. Wer die Kette nicht erlebt hat, hält Vererbung in Etappe 11 später für Zeremonie. **Der Schmerz ist der Lehrstoff.**

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

**Welche Klasse ist dein Bezugsfall?**

Du legst heute vier Sätze Startwerte fest. Vier Zahlenpaare aus der Luft gegriffen, und jedes fühlt sich beliebig an. Genau deshalb brauchst du einen Anker:

> Eine der vier Klassen ist die Normale. Sie bekommt runde, langweilige Werte. Die anderen drei werden **gegen sie** beschrieben.

Der Soldat bietet sich an — er ist im Lehrplan als ausgewogen angelegt.

**Damit du nicht vier Zahlenpaare erfinden musst, hier ein vollständiger Satz zum Übernehmen.** Er ist nicht heilig, aber er ist stimmig, und du sollst heute deine Zeit nicht mit Balancing verbringen:

| Klasse | Trefferpunkte | Schaden | Panzerung | Startausrüstung |
|---|---|---|---|---|
| **Soldat** ← Bezugsfall | 100 | 10 | 5 | Sturmgewehr |
| Heavy | 140 | 14 | 10 | Schweres MG |
| Engineer | 90 | 7 | 4 | Reparaturwerkzeug |
| Medic | 80 | 6 | 3 | Medkit |

⚠️ **Und jetzt die Falle, in die hier fast jeder tappt — sie kostet später Stunden.**

Der Soldat hat **100 Trefferpunkte**. Die Kernintegrität aus Etappe 1 steht bei **100 Prozent**. Dieselbe Zahl, und beides klingt nach „Leben".

**Es sind zwei völlig verschiedene Dinge:**

| Variable | Gehört zu | Woher | Fällt sie auf 0 |
|---|---|---|---|
| `trefferpunkte` | **deinem Marine** | heute, aus der Tabelle | dein Marine fällt aus |
| `kern_integritaet` | **der Anlage** | Etappe 1 | das Spiel ist verloren |

Wer beides in eine Variable schreibt, hat ein Spiel, in dem der Soldat stirbt, sobald die Anlage getroffen wird — und in Etappe 11, wenn *jeder* der vier Marines eigene Trefferpunkte hat, ist der Umbau ungleich teurer als heute.

**Nenn sie deshalb nicht beide `health`.** Der englische Sammelbegriff verführt genau dazu, weil er auf beides passt. Nimm zwei Namen, die sagen, wem der Wert gehört.

*(In Etappe 3c schlagen die Gegner auf die Anlage, nicht auf dich. Dann brauchst du die Trennung ohnehin.)*

**Lies die Tabelle spaltenweise, nicht zeilenweise.** Der Heavy hat nicht „140 TP", sondern *vierzig Prozent mehr als der Soldat*. Der Medic hat nicht „6 Schaden", sondern *deutlich weniger, dafür kann er heilen*. Genau so sollst du sie in `GELERNT.md` notieren — als Verhältnisse, nicht als Zahlen. Denn wenn du in Etappe 21a die Schadensformel baust, änderst du den Bezugsfall und rechnest die anderen drei relativ nach. Mit absoluten Zahlen wäre das jedes Mal von vorn.

Und wenn dir andere Werte besser gefallen: nimm sie. Nur behalt den Bezugsfall bei runden Zahlen — er ist der Anker, an dem du später misst.

**Warum das jetzt zählt und nicht in Etappe 21a:** Ohne Bezugsfall balancierst du vier Klassen gegen nichts. Mit Bezugsfall balancierst du drei gegen eine — und wenn du in Etappe 21 die Schadensformel änderst, musst du nur eine Klasse nachrechnen und die anderen relativ dazu anpassen. Das ist der Unterschied zwischen einer halben Stunde und einem Abend.

Schreib die vier Klassen als Tabelle in `GELERNT.md`, mit dem Bezugsfall markiert. Du wirst diese Tabelle in Etappe 11 wieder brauchen, wenn aus ihr vier Python-Klassen werden — und in Etappe 21a, wenn die Schadensformel entsteht.

*(Eine zweite Frage taucht heute vielleicht auf: Wäre ein Wörterbuch nicht besser als vier `elif`-Zweige? Ja, wäre es. Warum du es trotzdem nicht tust, steht weiter unten unter „Was NICHT".)*

---

## Die Konzepte

### 1. `if` — und warum die Einrückung Syntax ist

```python
if temperatur > 30:
    print("Zu warm für den Ofen.")
    print("Teig geht zu schnell auf.")
print("Bäckerei geöffnet.")
```

Die ersten beiden `print`-Zeilen gehören zum `if`, die dritte nicht. Der einzige Unterschied sind vier Leerzeichen.

In vielen Sprachen sind Einrückungen Kosmetik. **In Python sind sie Bedeutung.** Wer eine Zeile falsch einrückt, ändert das Programm — und meistens ohne Fehlermeldung. Das ist der Grund, warum ein falsch eingerückter `elif`-Zweig weiter unten als Kaputtmach-Experiment steht.

Nimm vier Leerzeichen, immer. Dein Editor macht das automatisch; misch niemals Tabs und Leerzeichen.

Und **der Doppelpunkt am Zeilenende** gehört dazu. Wer ihn vergisst, bekommt `SyntaxError: expected ':'` — freundlicherweise mit der richtigen Zeilennummer.

### 2. `==` gegen `=` — die Schuld aus Etappe 1

Gestern hast du gelernt: `=` heißt *bekommt den Wert*. Es ist ein Befehl.

Heute kommt das Gegenstück:

```python
kunden = 3      # Befehl:      kunden bekommt den Wert 3
kunden == 3     # Frage:       ist kunden gleich 3?  →  True
```

Ein Zeichen Unterschied, zwei völlig verschiedene Dinge. Das eine tut etwas, das andere stellt etwas fest.

Wenn du `if kunden = 3:` schreibst, sagt Python:

```
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
```

Freundlicher geht es kaum, und trotzdem kostet dieser Fehler jeden einmal eine halbe Stunde — weil man beim Lesen des eigenen Codes den Unterschied schlicht übersieht. Merk dir das Gegenmittel: Beim Suchen dieses Fehlers liest du die Zeile **laut** vor. „Wenn kunden bekommt den Wert drei" klingt falsch. „Wenn kunden gleich drei ist" klingt richtig.

### 3. Vergleichen — und der Typ hinter dem Vergleich

| Operator | Bedeutung |
|---|---|
| `==` | gleich |
| `!=` | ungleich |
| `<` `>` | kleiner, größer |
| `<=` `>=` | kleiner-gleich, größer-gleich |

Und jetzt die Falle, die direkt an Etappe 1 anschließt:

```python
"5" == 5        # False
```

Kein Fehler, keine Warnung, einfach `False`. Text ist nie gleich Zahl, auch wenn beide gleich aussehen. Python vergleicht nicht nur den Inhalt, sondern auch den Typ.

Genau hier zahlt dein `int()` aus Etappe 1. Ohne die Umwandlung wäre deine ganze Klassenwahl heute wirkungslos: `klasse == 2` wäre immer `False`, jeder Zweig würde übersprungen, und der `else`-Zweig würde behaupten, die Eingabe sei ungültig. **Das Programm liefe fehlerfrei durch und wäre komplett falsch** — Fehler vom Typ 3, und diesmal einer, der eine ganze Etappe unbrauchbar macht.

Bei `<` und `>` ist Python strenger: `"5" < 5` ist ein `TypeError`. Ein Absturz, also die freundlichere Variante.

### 4. `elif` ist nicht dasselbe wie mehrere `if`

Das ist der wichtigste Absatz dieser Etappe, und er wird fast überall als Stilfrage behandelt. Er ist keine.

```python
# Variante A — eine Kette
if punkte > 90:
    note = "sehr gut"
elif punkte > 80:
    note = "gut"
elif punkte > 70:
    note = "befriedigend"

# Variante B — drei einzelne Prüfungen
if punkte > 90:
    note = "sehr gut"
if punkte > 80:
    note = "gut"
if punkte > 70:
    note = "befriedigend"
```

Bei `punkte = 95` liefert A **„sehr gut"** und B **„befriedigend"**.

Der Grund: Eine `if`/`elif`-Kette ist **eine** Entscheidung mit mehreren Ausgängen. Sobald ein Zweig zutrifft, sind alle anderen erledigt — Python schaut gar nicht mehr hin. Drei einzelne `if` sind dagegen **drei** Entscheidungen, die nacheinander getroffen werden, und die letzte überschreibt die vorherigen.

**Die Frage, die du dir stellst:** *Schließen sich diese Fälle gegenseitig aus?* Eine Klasse kann nicht gleichzeitig Medic und Heavy sein — Kette. Ein Gegner kann gleichzeitig brennen und verlangsamt sein — einzelne `if`.

Diese Unterscheidung kommt in Etappe 17 zurück, wenn mehrere Ereignisse gleichzeitig zutreffen können. Wer dort eine Kette baut, verliert Ereignisse und merkt es nicht.

### 5. `else` — das Auffangbecken

```python
if klasse == "medic":
    ...
elif klasse == "heavy":
    ...
else:
    print("Diese Klasse gibt es nicht.")
```

**`else` läuft, wenn kein Zweig davor zugetroffen hat.** Es hat selbst keine Bedingung — deshalb steht es immer ganz am Ende.

Genau dafür brauchst du es heute: Eingabe `9` trifft auf keinen der vier Zweige, landet im `else` und wird als ungültige Klassennummer gemeldet. Damit ist die Schuld aus Etappe 1 beglichen, wo dieselbe `9` stillschweigend durchlief.

*(Dass `else` auf Dauer zu grob ist — es kann nicht unterscheiden, warum etwas danebenging — merkst du selbst in Auftragsschritt 7. Das saubere Werkzeug dafür ist Etappe 20.)*

### 6. Booleans — der dritte Datentyp

`True` und `False`. Groß geschrieben, ohne Anführungszeichen. `"True"` mit Anführungszeichen ist Text und etwas völlig anderes.

Ein Vergleich *erzeugt* einen Boolean:

```python
offen = kunden > 0      # in offen steht jetzt True oder False
```

Das ist eine Zeile, die viele Anfänger nie schreiben, weil sie nicht merken, dass sie erlaubt ist. Sie ist der Kern von `meldung_abgesetzt`: Ein Boolean ist ein Gedächtnis für eine Ja/Nein-Tatsache, und du kannst ihn wegspeichern und später wieder abfragen.

Und wenn du einen Boolean hast, brauchst du ihn nicht nochmal zu vergleichen:

```python
if offen == True:      # umständlich
if offen:              # so schreibt man das
```

### 7. `and`, `or`, `not` — mehrere Bedingungen in einer Zeile

| | Wahr, wenn |
|---|---|
| `a and b` | beide wahr sind |
| `a or b` | mindestens eines wahr ist |
| `not a` | `a` falsch ist |

Und jetzt der eigentliche Punkt. Zwei Wege zum selben Ergebnis:

```python
# fremdes Beispiel — Turm
if hat_ticket:
    if not gesperrt:
        if alter >= 18:
            print("Einlass.")

# dasselbe — eine Zeile
if hat_ticket and not gesperrt and alter >= 18:
    print("Einlass.")
```

Beide funktionieren. Nur eines davon kannst du in vier Monaten noch lesen.

**Der Turm ist die natürliche Schreibweise für Anfänger**, weil er dem Denken folgt: erst das, dann das, dann das. Er hat zwei Probleme. Er wächst nach rechts, bis er nicht mehr auf den Bildschirm passt. Und er verschleiert, dass es hier um **eine** Frage geht („darf der rein?") und nicht um drei.

Nimm die verknüpfte Form. Sie ist die, die dir in Etappe 18 als vollständiges Freischaltsystem wiederbegegnet — dort prüfst du vier Voraussetzungen gleichzeitig, und ein vierstöckiger Turm wäre dort unbenutzbar.

👀 **Eine Merkwürdigkeit am Rande, nur zum Erkennen.** Probier das einmal im Terminal aus:

```python
print(True and "hallo")     # hallo
print(0 or "ersatz")        # ersatz
```

`and` und `or` liefern **nicht** `True` oder `False`, sondern einen der beiden Werte, die du hineingesteckt hast. In einem `if` fällt das nie auf, weil dort ohnehin nur „wahr oder nicht" zählt.

**Du brauchst das heute nicht, und du sollst es heute nicht benutzen.** Es steht hier, damit es dich nicht überrascht, wenn du in fremdem Code eine Zeile wie `ziel = gewaehltes or standard` liest. In Etappe 18 kommt es wieder — und dort zusammen mit der Falle, die daraus entsteht, wenn `0` ein gültiger Wert ist. Ein Satz dazu reicht heute vollkommen.

### 8. Rangfolge und Klammern

Python liest `and` vor `or`. Das heißt, `a or b and c` bedeutet in Wirklichkeit `a or (b and c)` — und das ist selten das, was jemand gemeint hat.

**Merk dir nicht die Regel, merk dir das Gegenmittel:**

> Sobald `and` und `or` in derselben Zeile stehen, setz Klammern. Auch wenn sie technisch überflüssig wären.

```python
if (klasse == "heavy" or klasse == "soldat") and munition > 0:
```

Einmal getippt, und du musst nie wieder darüber nachdenken, in welcher Reihenfolge Python das gelesen hat. Ohne Klammern bedeutet diese Zeile etwas anderes — probier es im Kaputtmach-Teil aus.

### 9. Truthy und Falsy — hier beginnt die Null-Falle

Python lässt in einem `if` nicht nur Booleans zu, sondern jeden Wert. Und behandelt dabei ein paar Werte als falsch, obwohl sie nicht `False` sind — vor allem **die Null**:

```python
if munition:        # bedeutet: wenn munition nicht 0 ist
    schiessen()
```

Das ist bequem, funktioniert hier sogar, und es ist trotzdem der Anfang eines Fehlers, der dich später erwischt. Denn `0` heißt nicht immer „nichts da":

> Panzerung 0 ist eine echte Panzerung. Abklingzeit 0 heißt „bereit". Feld 0 ist ein echtes Feld.

Bei `munition` passt die Abkürzung zufällig. Bei `panzerung` wäre sie falsch — und beide sehen im Code identisch aus.

**Deine Regel für heute, mehr brauchst du nicht:**

> Wenn du „mehr als nichts" meinst, schreib es hin: `if munition > 0:`

Diese Sorte Fehler heißt im Lehrplan **Null-Falle** und begleitet dich bis Etappe 19. Heute genügt es, sie einmal gesehen zu haben — im Kaputtmach-Teil führst du sie selbst vor.

### 10. `.strip()` — und was der Punkt bedeutet

Der Spieler tippt ` 2` mit einem Leerzeichen davor. Für Python ist das nicht `"2"`, und `int(" 2")` geht zwar gut, aber der Reflex lohnt sich trotzdem:

```python
eingabe = input("Klasse: ").strip()
```

`.strip()` entfernt Leerzeichen am Anfang und Ende. Eine Zeile, ein Ärgernis weniger.

👀 **Wichtiger als die Methode ist der Punkt davor.** `eingabe.strip()` heißt: *ruf die Fähigkeit `strip` auf, die zu diesem Text gehört*. Es ist keine Funktion, der du etwas übergibst — der Wert selbst kann etwas.

Das ist deine erste Begegnung mit einer Schreibweise, die ab Etappe 9 dein ganzes Programm trägt: `marine.feuern()`, `gegner.schaden_nehmen()`, `welt.tick()`. Der Punkt heißt immer dasselbe: **gehört zu**. Ein Satz dazu reicht heute.

**Und ein Detail, das gleich in Auftragsschritt 1 zuschlägt:** `.strip()` verändert `eingabe` nicht, sondern *gibt einen neuen Text zurück*. Wer `eingabe.strip()` schreibt, ohne das Ergebnis zuzuweisen, hat nichts getan — genau wie bei `int()` gestern.

*(`.lower()` — Großschreibung angleichen — brauchst du erst, wenn der Spieler Wörter statt Zahlen tippt. Das ist Etappe 3a mit den Befehlen.)*

### 11. Wo der Boolean aufhört

`meldung_abgesetzt` ist ein guter Boolean: Du hast gefunkt oder nicht, dazwischen gibt es nichts.

👀 **Merk dir nur, wo die Grenze liegt.** Ein Boolean kennt zwei Zustände. Sobald etwas drei haben kann — „am Leben / gefallen / wird ersetzt" —, ist er das falsche Werkzeug, und drei Booleans nebeneinander sind die falsche Rettung.

Heute betrifft dich das nicht. In Etappe 12 nimmst du dafür Strings, in Etappe 21b `Enum`. Ein Satz, weitergehen.

### 12. `print()`-Debugging — dein Werkzeug für heute

Du hast noch keinen Debugger; der kommt in Etappe 8. Was du hast, ist `print()` an der richtigen Stelle.

**Die Technik, die bei Verzweigungen fast immer trifft:** Setz in jeden Zweig eine Zeile mit einem Erkennungswort.

```python
if punkte > 90:
    print("### ZWEIG A")
    ...
elif punkte > 80:
    print("### ZWEIG B")
    ...
```

Jetzt siehst du beim Ausführen, welcher Zweig **wirklich** läuft — statt zu vermuten, welcher laufen sollte. In neun von zehn Fällen ist genau das die Antwort auf „warum passiert das nicht?".

Die drei Rauten sind kein Spaß: Sie machen die Zeilen später mit einer Suche wiederfindbar. Und sie müssen alle raus, bevor du committest.

---

## Dein Auftrag

Nach jedem Schritt ausführen. Und ab heute: **nach jedem Schritt mit mehreren verschiedenen Eingaben ausführen.** Ein Programm mit Verzweigungen ist erst getestet, wenn jeder Zweig einmal gelaufen ist.

**1. Räum die Eingabe auf.**

Die Klassenwahl aus Etappe 1 bekommt `.strip()`, bevor `int()` darauf losgeht. Führ es aus und tippe absichtlich ` 2` mit einem Leerzeichen davor.

**2. Bau die `if`/`elif`-Kette.** Das ist der Kern der Etappe, deshalb hier genau, was herauskommen soll:

> Nach der Eingabe soll dein Programm **genau einen** dieser fünf Fälle ausführen:
>
> | Eingabe | Klasse | `trefferpunkte` | `schaden` | `panzerung` | `ausruestung` |
> |---|---|---|---|---|---|
> | `1` | Soldat | 100 | 10 | 5 | `"Sturmgewehr"` |
> | `2` | Heavy | 140 | 14 | 10 | `"Schweres MG"` |
> | `3` | Engineer | 90 | 7 | 4 | `"Reparaturwerkzeug"` |
> | `4` | Medic | 80 | 6 | 3 | `"Medkit"` |
> | alles andere | — | — | — | — | Fehlermeldung |
>
> **Nach der Kette stehen in diesen vier Variablen die Werte genau einer Klasse.** Es gibt keine `heavy_trefferpunkte` und kein `medic_schaden` — nur `trefferpunkte`, `schaden`, `panzerung`, `ausruestung`, jeweils einmal.

Vier Zweige mit `if` und `elif`, jeder setzt vier Variablen. Ja, das sind vier fast identische Blöcke. Ja, das darf sich falsch anfühlen — warum, steht unten unter „Was NICHT".

**3. Setz den `else`-Zweig.** Die fünfte Zeile der Tabelle: Ungültige Eingabe wird gemeldet, statt stillschweigend durchzulaufen. Damit ist die Schuld aus Etappe 1 beglichen. Testeingabe: `9`.

**4. Zeig die Werte an — und heute ist das ausdrücklich keine Bastelarbeit.**

Dein Lagebriefing aus Etappe 1 bekommt vier Zeilen dazu, in genau derselben Form wie die vorhandenen:

```
Klasse:        Heavy
Trefferpunkte: 140
Schaden:       14
Panzerung:     10
```

Dieselben f-Strings, dieselbe `print()`-Technik, nur mehr Variablen darin. **Der ASCII-Kopf von gestern wird heute nicht angefasst** — er bleibt, wie er ist, und die neuen Zeilen kommen darunter zum übrigen Briefing.

Das ist Absicht: Die Darstellung wächst nur, wenn das jeweilige Python-Thema das Werkzeug dafür mitbringt. Heute lernst du Verzweigungen. Der nächste sichtbare Schritt ist Etappe 3b, wo aus Zahlen Balken werden.

**5. Führ alle fünf Fälle durch** — `1`, `2`, `3`, `4` und `9`. Notier dir, welche Werte jeweils herauskommen. Wenn zwei Eingaben dieselben Werte liefern, hast du einen Fehler gefunden, bevor er dich gefunden hat.

**6. Bau den ersten Schuss.**

Leg zwei neue Booleans an:

```python
nachladen_noetig = False
ziel_in_sicht = True
```

`munition` gibt es seit Etappe 1 mit dem Startwert `40`.

**Schreib die Feuerbedingung als eine Zeile mit `and`** — nicht als drei verschachtelte `if`. Gefeuert wird, wenn alle drei Bedingungen stimmen: Munition vorhanden, kein Nachladen nötig, Ziel in Sicht.

Senk bei Erfolg `munition` um 1. Gib sonst eine Meldung aus.

Mehr nicht — kein Zielsystem, kein Schaden am Gegner, kein Nachladebefehl. Das kommt in Etappe 3.

**7. Bau die Funkentscheidung.** Beschreib beim ersten Kontakt etwas Ungewöhnliches und frag den Spieler, ob er es meldet. Speicher seine Antwort in einem Boolean namens `meldung_abgesetzt`.

Er wird heute nicht weiter benutzt. In Etappe 17b entscheidet er mit, welcher Sektor fällt.

**8. Mach den Ehrlichkeitstest.** Setz `munition = 0`, führ aus und feuere. Lies die Meldung: Sagt sie dir, dass die *Munition* leer ist — oder nur „Feuern nicht möglich"?

Wenn Letzteres: Das ist kein Fehler, sondern die Eigenschaft einer verknüpften Bedingung. Sie liefert ein Gesamtergebnis, keine Begründung. Schreib den Satz in `GELERNT.md`; in Etappe 20 wird eine ganze Etappe daraus.

---

## Was NICHT in diese Etappe gehört

- ❌ **Wiederholt fragen, bis die Eingabe stimmt** → Etappe 3a (Schleifen)
- ❌ **Eine Liste für die Startausrüstung** → Etappe 4
- ❌ **Ein Wörterbuch für die Klassenwerte** → siehe unten
- ❌ **`try` / `except` für die Eingabe `zwei`** → Etappe 20
- ❌ **Funktionen, damit die Kette kürzer wird** → Etappe 7
- ❌ **`match` / `case`** → kommt in diesem Lehrplan gar nicht vor; `if`/`elif` ist die Form, die du in fremdem Code lesen musst
- ❌ **Gegner, die zurückschießen** → Etappe 3 und 12

**Der dritte Punkt ist der wichtigste, und er wird dir wehtun.**

Irgendwann während dieser Etappe wirst du auf deine `elif`-Kette schauen und denken: *Das sind vier fast identische Blöcke. Da müsste doch eine Tabelle reichen.*

**Der Gedanke ist völlig richtig.** Ein Wörterbuch wäre kürzer, wäre erweiterbar, und du würdest eine neue Klasse mit einer Zeile hinzufügen statt mit fünf. Das ist Etappe 5, und dort machst du genau das mit dem Depot.

Warum trotzdem nicht heute: Diese Kette hat eine Aufgabe, die über das Funktionieren hinausgeht. In Etappe 11 löst du sie durch vier Python-Klassen ab, und diese Ablösung ist der Moment, in dem Vererbung aufhört, Zeremonie zu sein. Damit das funktioniert, musst du die Kette **gehabt** haben — hässlich, wiederholt, mit vier fast gleichen Blöcken. Wer sie in Etappe 2 durch ein elegantes Wörterbuch ersetzt, kommt in Etappe 11 an und fragt: *Wozu jetzt noch Klassen? Es lief doch.*

Ertrag sie. Und schreib in `GELERNT.md`: *„Die elif-Kette stört mich. Wird in Etappe 11 abgelöst."* Dann ist es ein Termin und kein Mangel.

---

## Selbsttest

Beobachtbare Zustände, keine Selbsteinschätzung.

- [ ] Alle vier Klassen ergeben unterschiedliche Werte — du kannst sie einzeln vorführen
- [ ] `trefferpunkte` und `kern_integritaet` sind **zwei** Variablen — änderst du eine im Code, ändert sich die Ausgabe der anderen nicht
- [ ] Nach der Kette steht in `trefferpunkte` **ein** Wert, nicht vier — es gibt keine Variablen für die nicht gewählten Klassen
- [ ] Der ASCII-Kopf aus Etappe 1 erscheint unverändert, die Klassenwerte stehen darunter im Briefing
- [ ] Eingabe `9` erzeugt eine verständliche Meldung statt einer erfundenen Klasse
- [ ] Eingabe mit Leerzeichen davor funktioniert trotzdem
- [ ] Du kannst zeigen, welche Zeile deines Codes bei welcher Eingabe läuft
- [ ] Die Feuer-Bedingung steht in **einer** Zeile, nicht als verschachtelter Turm
- [ ] Bei `munition = 0` wird nicht gefeuert, und es gibt eine Meldung
- [ ] `meldung_abgesetzt` enthält nach der Entscheidung `True` oder `False` — nicht `"True"`
- [ ] Änderst du in einem Zweig `==` testweise zu `!=`, kannst du vorhersagen, was bei welcher Eingabe passiert — und es trifft ein
- [ ] Alle `### ZWEIG`-Debugzeilen sind vor dem Commit entfernt
- [ ] `GELERNT.md` enthält die Klassentabelle mit markiertem Bezugsfall

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten.

1. Wann `elif`, wann mehrere separate `if`? Nenn je ein Beispiel aus deinem Spiel.
2. Was ergibt `"5" == 5`? Warum stürzt es nicht ab?
3. Was ist „truthy"? Welche Werte sind falsch, ohne `False` zu sein?
4. **Warum ist `if munition:` gefährlich, wenn `0` ein gültiger Wert sein kann?**
5. Warum reicht ein Boolean nicht, um „Munition" darzustellen?
6. Was bedeutet der Punkt in `eingabe.strip()`?
7. Was passiert, wenn du `eingabe.strip()` schreibst, ohne das Ergebnis zuzuweisen?
8. Wann läuft der `else`-Zweig?
9. Warum setzt deine Kette nur die Werte **einer** Klasse und nicht aller vier?

**Frage 1 und 4 sind die wichtigen.**

Frage 1, weil `elif` gegen mehrere `if` der einzige Punkt dieser Etappe ist, den man wirklich falsch machen kann, ohne es zu merken.

Frage 4, weil sie der Anfang eines Fadens ist, der bis Etappe 19 läuft. Wer mit „weil `0` falsy ist" antwortet, hat die Syntax verstanden — sag dazu, welche Variable in **deinem** Spiel legitim `0` sein kann und was dann schiefgeht.

**Und wenn du bei einer Frage ins Grübeln kommst: probier sie aus.** Vier Zeilen im Terminal beantworten mehr als zehn Minuten Nachdenken. Das ist keine Schummelei, sondern eine Methode — sie heißt später Experiment und ab Etappe 26 Test.

---

## Transferaufgabe (10 Minuten)

**Außerhalb des Spiels**, in `uebung.py`.

Ein Türsteher. Frag nach Alter und danach, ob jemand auf der Gästeliste steht. Entscheide über den Einlass mit **einer** verknüpften Bedingung — nicht mit verschachtelten `if`.

Die Regel: Rein kommt, wer mindestens 18 ist. Oder wer auf der Gästeliste steht, unabhängig vom Alter. Aber niemand unter 16, egal was.

Diese dritte Zeile ist der Punkt der Aufgabe. Sie zwingt dich, `and` und `or` in einer Zeile zu mischen — und damit zu den Klammern aus Konzept 8.

**Vorgehen:** Schreib die Bedingung erst ohne Klammern hin. Teste sie mit einem 15-Jährigen, der auf der Gästeliste steht. Setz dann die Klammern und teste denselben Fall noch einmal.

*(Noch ohne Funktion; die kommt in Etappe 7.)*

---

## Kaputtmachen

Erst aufschreiben, was du erwartest. Dann ausführen. Fünf Experimente, und drei davon laufen ohne jede Fehlermeldung falsch — das sind die eigentlichen.

1. **Schreib `if klasse = 2:`** — ein Gleichheitszeichen statt zwei. Was sagt Python, und schlägt es die Lösung vor?

2. **Nimm die `int()`-Umwandlung aus Etappe 1 weg** und lass die Klassenwahl laufen. Gib `2` ein. Welcher Zweig greift? *(Kein Absturz. Das ist das Problem.)*

3. **Bau die Kette aus vier einzelnen `if` statt `if`/`elif`.** Gib `1` ein. Welche Klassenwerte stehen am Ende in deinen Variablen?

4. **Rück einen `elif`-Zweig eine Ebene zu tief ein.** Führ alle vier Klassen durch. Welche bekommt jetzt welche Werte? Stürzt es ab?

5. **Setz `munition = 0`** und prüf mit `if munition:` statt `if munition > 0:` — noch richtig? Und jetzt dasselbe mit `panzerung = 0` und `if panzerung:`. Dieselbe Schreibweise, unterschiedliches Ergebnis.

**Warum 2, 3 und 5 die wichtigen sind:**

- **2** vergleicht Text mit Zahl. Kein Zweig trifft, `else` greift, und dein Programm behauptet, `2` sei ungültig. Die ganze Etappe wirkungslos — ohne eine einzige Fehlermeldung.
- **3** setzt am Ende immer die Werte des letzten Zweigs. Dein Spieler ist immer Medic, egal was er wählt.
- **5** ist die Null-Falle in ihrer reinsten Form: Bei `munition` funktioniert die Abkürzung zufällig, bei `panzerung` nicht.

Alle drei in `GELERNT.md`, mit einem Satz dazu, **woran du sie erkannt hättest**. Nicht was der Fehler war — wie man ihn bemerkt.

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `SyntaxError: expected ':'` | Doppelpunkt am `if`-Ende vergessen | Genannte Zeile |
| `SyntaxError: ... Maybe you meant '=='` | `=` statt `==` im `if` | Genannte Zeile, laut vorlesen |
| `IndentationError: expected an indented block` | Nach dem `if` nicht eingerückt | Zeile darunter |
| Immer derselbe Zweig läuft | Vergleich zwischen Text und Zahl | Die `int()`-Umwandlung aus Etappe 1 |
| Marine und Anlage verlieren gleichzeitig Leben | Beide Werte stecken in derselben Variablen | Zwei getrennte Namen, siehe Warnung oben |
| Kein Zweig läuft, `else` greift immer | Text wird mit Zahl verglichen, oder Leerzeichen in der Eingabe | `int()` aus Etappe 1, dann `.strip()` |
| Werte stimmen bei einer Klasse, bei anderen nicht | Einrückung eines Zweigs | `### ZWEIG`-Zeilen setzen |
| Bedingung mit `and`/`or` verhält sich unerwartet | Rangfolge | Klammern setzen |
| `if offen == "True":` läuft nie | Boolean mit Text verglichen | Anführungszeichen weg |
| Meldung erscheint doppelt | `elif` mit `if` verwechselt | Alle Zweige der Kette durchgehen |

**Dein Debugging-Reflex für diese Etappe:**

> **Welcher Zweig läuft gerade wirklich?**

Nicht welcher laufen *sollte* — das weißt du, du hast ihn geschrieben. Setz in jeden Zweig eine `### ZWEIG`-Zeile und führ aus.

Das ist derselbe Reflex wie in Etappe 1, nur eine Ebene höher: Dort hast du gefragt *welchen Typ hat dieser Wert*, heute fragst du *welchen Weg nimmt das Programm*. Beide beruhen auf demselben Grundsatz, und der trägt bis Etappe 30: **Nachsehen schlägt Vermuten.** In Etappe 8 bekommst du dafür ein besseres Werkzeug als `print()`. Der Reflex bleibt derselbe.

---

## Ein Blick nach vorne

**Etappe 3a** macht aus dem Skript ein Spiel. Deine Verzweigungen wandern in eine Schleife, und die ungültige Eingabe führt nicht mehr zum Programmende, sondern zu einer neuen Frage. Ab dort wartet dein Programm auf dich.

**Etappe 11** tötet deine `elif`-Kette. Aus den vier Klassen werden vier Python-Klassen — und der Vergleich zwischen vorher und nachher ist der Grund, warum du die Kette heute erträgst.

*(Was `meldung_abgesetzt` und die Null-Falle später anrichten, steht im Bogen. Du musst es heute nicht wissen.)*

---

## Abschluss

**In `GELERNT.md`:**

- Was neu war: Verzweigungen, Booleans, verknüpfte Bedingungen
- Was gehakt hat, mit Fehlermeldung
- **Die Klassentabelle** mit markiertem Bezugsfall (du brauchst sie in Etappe 11 und 21a)
- Der Satz zur `elif`-Kette: *stört mich, wird in Etappe 11 abgelöst*
- Die drei stillen Fehler aus dem Kaputtmachen — mit **woran du sie erkannt hättest**
- Der Satz aus Auftragsschritt 8: *eine verknüpfte Bedingung sagt nicht, welcher Teil gescheitert ist*

**Dann committen:**

```
git add .
git commit -m "Etappe 2: Der erste Kontakt"
git push
```

Vorher: Sind alle `### ZWEIG`-Zeilen raus?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest. Alle drei sind optional.

- **Eine Klassen-Fähigkeit als Boolean.** Der Medic kann heilen, der Engineer kann bauen — `kann_heilen`, `kann_bauen`. Heute nur gesetzt, nicht benutzt. In Etappe 11 werden Methoden daraus.
- **Eine zweite Bedingung beim Feuern.** Etwa Überhitzung: nach drei Schüssen ohne Pause geht nichts mehr. Zwingt dich zu einem Zähler neben den Booleans.
- **Zeig an, welche Bedingung gescheitert ist.** Statt „Feuern nicht möglich" die Angabe, woran es lag. **Das ist die beste Erweiterung hier** — sie ist mehr Arbeit, als sie aussieht, und genau das ist die Lektion: Eine verknüpfte Bedingung liefert ein Gesamtergebnis, keine Begründung.

---

> **Nächste Etappe:** [Etappe 3 — Die Wellenschleife](etappe-03-die-wellenschleife.md) · `while`, `for`, `range()`, `break`, `continue`
