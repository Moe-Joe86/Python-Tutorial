# Etappe 4 — Das Inventar

> **Block 1: Fundament** · Etappe 4 von 29 · [← Etappe 3](etappe-03-die-game-loop.md) · [Lehrplan](../RPG_Lehrplan.md) · [Etappe 5 →](etappe-05-die-karte.md)

**Boot.dev:** Listen, `append()`, `remove()`, `len()`, Indexing
**Zeitaufwand:** 4–6 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 3 abgeschlossen, Selbsttest grün

---

## Worum es geht

Bisher hat dein Spieler nichts. Er sieht sich um, er redet, er geht wieder von vorn — aber die Welt hinterlässt keine Spuren bei ihm.

Heute bekommt er zum ersten Mal etwas in die Hand. Ein halb gegessenes Brot. Einen umgestoßenen Stuhl, den er nicht mitnehmen kann. Und einen Schlüssel, der zu keiner Tür im Dorf passt.

**Der Schlüssel ist wichtig.** Er ist kein Rätsel und kein Puzzle — er ist eine Frage, die dein Spiel dem Spieler stellt und erst in Etappe 14 beantwortet. Ein Gegenstand, der auf etwas außerhalb des sichtbaren Bereichs verweist, ist eines der billigsten und wirksamsten Mittel, die es gibt.

Technisch lernst du die **Liste** kennen — die Datenstruktur, die du von heute bis Etappe 29 am häufigsten benutzen wirst.

**Und du lernst etwas, das größer ist als diese Etappe.** In der Mitte dieses Guides steht ein Abschnitt über *mutable und immutable*. Er sieht harmlos aus, ist vier Codezeilen lang, und er erklärt die Mehrheit aller Bugs, die Anfänger nicht verstehen. Wenn du heute nur eine Sache wirklich begreifst, dann diese.

---

## Der lange Bogen

| Was du heute baust | Wo es wieder auftaucht |
|---|---|
| `inventar` als Liste von Strings | **Etappe 11** — wird zur Liste von `Item`-Objekten |
| **Mutable vs. immutable** | **Etappe 10** — zwei Spieler teilen versehentlich ein Inventar; **Etappe 14** — `[["."] * 5] * 5` |
| Index ab 0 | **Etappe 14** — `karte[y][x]` im Minenraster |
| `len()` | **Etappe 14** — `range(len(karte))` |
| `in` zum Prüfen | **Etappe 6** — die Gegenüberstellung Liste / Set / Dictionary |
| Obergrenze von 10 Gegenständen | **Etappe 20** — „Inventar voll" als sauber abgefangener Fall |
| `remove()` scheitert an fehlenden Elementen | **Etappe 20** — dort wird daraus `try` / `except` |
| Zwei-Wort-Befehle mit `.split()` | **Etappe 5** — `gehe norden`; **Etappe 7** — `verarbeite_befehl()` |
| Kennung ↔ Anzeigename eines Gegenstands | **Etappe 11** — `item.id` und `item.name`; **Etappe 25** — der JSON-Schlüssel |
| Der Schlüssel, der nirgends passt | **Etappe 14** — er öffnet die Mine |

**Drei Schulden werden heute eingelöst:**

Aus **Etappe 1** — dort stand, eine Variable sei kein Behälter, sondern ein Schild, das auf einen Wert zeigt. Heute merkst du zum ersten Mal, warum das kein Wortspiel war.

Aus **Etappe 2** — die Truthy-Liste. Heute schreibst du `if inventar:` statt `if len(inventar) > 0:` und verstehst, warum das erlaubt ist.

Aus **Etappe 3** — dort hast du entschieden, wie deine Befehlssprache aussieht, aber Zwei-Wort-Befehle noch nicht bauen können. Heute bekommst du das Werkzeug.

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

**Wie heißt ein Gegenstand — für den Spieler und für deinen Code?**

Der Spieler soll lesen: *„Auf dem Tisch liegt ein halb gegessenes Brot."*
Der Spieler soll tippen: `nimm brot`
Dein Code muss beides zusammenbringen.

Wenn du den Gegenstand als `"ein halb gegessenes Brot"` in der Liste speicherst, findet ihn niemand. Wenn du ihn als `"brot"` speicherst, ist deine Ausgabe kahl.

**Es gibt zwei saubere Wege:**

*Kurze Kennung, langer Text bei der Ausgabe.* Du speicherst `"brot"` und schreibst den schönen Satz von Hand, wenn du den Ort beschreibst. Einfach, und für ein Dutzend Gegenstände völlig ausreichend.

*Zwei Angaben pro Gegenstand.* Kennung und Anzeigename getrennt. Das ist sauberer — aber du brauchst dafür ein Werkzeug, das du noch nicht hast. Es kommt in Etappe 5.

**Meine Empfehlung: heute die kurze Kennung.** Nicht als Notlösung, sondern weil du in Etappe 11 sowieso umbaust: Dort wird aus jedem Gegenstand ein Objekt mit `item.id` und `item.name`, und in Etappe 25 wird die Kennung zum Schlüssel in einer JSON-Datei. Die Trennung, die du heute im Kopf machst, wird später im Code sichtbar.

**Praktischer Hinweis dazu:** Halte Kennungen klein geschrieben und ohne Umlaute — `schluessel`, nicht `Schlüssel`. Der Spieler tippt keine Umlaute, wenn er es eilig hat, und dein `.lower()` aus Etappe 3 hilft dir bei `ü` nicht.

**Zweite Frage, kürzer:** Was passiert, wenn das Inventar voll ist? Nimmst du den Gegenstand nicht auf, oder tauschst du? Heute reicht eine Meldung — aber entscheide bewusst, denn in Etappe 20 wird dieser Fall nochmal aufgegriffen.

---

## Die Konzepte

### 1. Die Liste

Eine Liste ist eine **geordnete Sammlung von Werten in einer einzigen Variable**.

```python
inventar = ["brot", "schluessel"]
leer = []
```

Die eckigen Klammern machen die Liste. Die Reihenfolge bleibt erhalten — was du zuerst hineinlegst, steht vorn.

Bisher brauchtest du für jeden Wert eine eigene Variable. Bei drei Gegenständen ginge das noch. Bei zehn hättest du zehn Variablen und keine Möglichkeit, „zeig mir alles" zu sagen. **Genau dafür gibt es Listen.**

Eine Liste darf alles enthalten — Strings, Zahlen, Wahrheitswerte, gemischt. In deinem Inventar sind es heute Strings. In Etappe 11 werden es Objekte.

### 2. Index — die Zählung beginnt bei 0

```python
inventar = ["brot", "schluessel", "lampe"]

inventar[0]    # "brot"
inventar[1]    # "schluessel"
inventar[2]    # "lampe"
```

Die eckigen Klammern hinter dem Namen heißen: „gib mir das Element an dieser Position".

**Und hier zahlt Etappe 3.** Du hast dich damals gewundert, warum `range(3)` die Zahlen 0, 1, 2 liefert und nicht 1, 2, 3. Das ist der Grund: Es passt exakt auf die Positionen einer Liste mit drei Einträgen. `range()` und Listen-Indizes sind aufeinander abgestimmt — das ist kein Zufall, sondern Design.

**Negative Indizes zählen von hinten:**

```python
inventar[-1]   # "lampe"   — das letzte Element
inventar[-2]   # "schluessel"
```

`[-1]` ist die übliche Art, an das letzte Element zu kommen, ohne vorher die Länge auszurechnen. Du wirst es ständig sehen.

**Was bei einem Index passiert, den es nicht gibt:**

```python
inventar[99]   # IndexError: list index out of range
```

Das ist ein Absturz, ein Fehler vom Typ 1 — unangenehm, aber ehrlich. Der Fehler sagt dir genau, was los ist. In Etappe 20 lernst du, ihn abzufangen. Heute reicht es, ihn einmal gesehen zu haben.

**Achtung, häufige Falle:** Bei drei Einträgen ist der letzte gültige Index **2**, nicht 3. Die Länge und der höchste Index sind nie dieselbe Zahl. Das erwischt jeden mindestens einmal.

### 3. `len()` — wie viele sind es?

```python
len(inventar)     # 3
len("Dorf")       # 4 — funktioniert auch bei Strings
```

`len()` liefert die Anzahl der Elemente. Zusammen mit `range()` bekommst du damit jeden Index:

```python
for i in range(len(inventar)):
    print(i, inventar[i])
```

**Das ist genau die Form, die in Etappe 14 dein Minenraster durchläuft** — dort dann zweimal ineinander. Merk dir das Muster.

Meistens brauchst du den Index aber gar nicht:

```python
for gegenstand in inventar:
    print(gegenstand)
```

Das ist kürzer und lesbarer. **Benutz die zweite Form, wann immer du kannst.** Die erste nur, wenn du die Position wirklich brauchst.

### 4. `append()` und `remove()` — und was sie zurückgeben

```python
inventar.append("lampe")     # hängt hinten an
inventar.remove("brot")      # entfernt das erste Vorkommen
```

Die Punkt-Schreibweise kennst du aus Etappe 2 von `.lower()` und `.strip()`. Dieselbe Idee: „ruf diese Funktion auf diesem Wert auf".

**Aber es gibt einen entscheidenden Unterschied, und der ist die halbe Etappe:**

```python
name = "kolja"
grossgeschrieben = name.upper()     # .upper() GIBT etwas ZURÜCK
                                    # name selbst bleibt "kolja"

inventar.append("lampe")            # .append() VERÄNDERT die Liste
                                    # und gibt nichts zurück
```

Schreibst du `inventar = inventar.append("lampe")`, ist deine Liste danach **weg**. `append()` gibt `None` zurück, und du hast dir `None` in die Variable geschrieben. Das ist ein sehr häufiger Anfängerfehler, und er steht unten in den Experimenten.

**Merksatz für heute:** `.append()` und `.remove()` verändern die Liste selbst. Du schreibst sie als eigene Zeile, nie mit einem `=` davor.

**Und der Gegenpol dazu:**

```python
inventar.append("lampe")              # VERÄNDERT die vorhandene Liste
neues = inventar + ["lampe"]          # ERZEUGT eine neue Liste
```

Beide führen zu einer Liste mit Lampe. Aber der erste Weg verändert das, was schon da ist; der zweite legt etwas Neues an und lässt das Alte unberührt.

Das ist derselbe Unterschied wie bei `.append()` und `.upper()` — nur von der anderen Seite betrachtet. Merk ihn dir: **verändern** und **neu erzeugen** sind zwei verschiedene Dinge, und Python macht beides, ohne dich zu warnen, welches du gerade tust. In Abschnitt 7 wird daraus der wichtigste Punkt dieser Etappe.

**`remove()` hat eine Tücke:** Es entfernt nur das *erste* Vorkommen. Und wenn das Element gar nicht in der Liste ist, stürzt es ab:

```python
inventar.remove("axt")    # ValueError: list.remove(x): x not in list
```

Deshalb prüfst du vorher — womit wir beim nächsten Punkt sind.

### 5. `in` — ist das drin?

```python
if "schluessel" in inventar:
    print("Du hast den Schlüssel.")

if "axt" not in inventar:
    print("Dir fehlt eine Axt.")
```

Kurz, lesbar, und die Absicherung vor jedem `remove()`.

**Für später wichtig:** `in` verhält sich bei Listen, Sets und Dictionaries unterschiedlich — bei einem Dictionary sucht es im *Schlüssel*, nicht im Wert. Das ist Etappe 6. Heute reicht: Bei einer Liste sucht `in` im Inhalt.

### 6. `if inventar:` — die Schuld aus Etappe 2

In Etappe 2 hast du die Truthy-Liste gelernt: `False`, `0`, `""`, `[]`, `{}` und `None` gelten als falsch. **Die leere Liste war dabei.**

Das heißt:

```python
if len(inventar) > 0:     # funktioniert
if inventar:              # dasselbe, aber besser lesbar
```

Beide sind richtig. Die zweite ist die pythonische Form und liest sich fast wie ein Satz: *wenn Inventar…*

**Und die Kehrseite:**

```python
if not inventar:
    print("Du trägst nichts bei dir.")
```

Benutz das heute für die Ausgabe des leeren Inventars. Es ist eine Kleinigkeit — aber es ist der Moment, in dem ein abstraktes Konzept aus Etappe 2 zu etwas Nützlichem wird.

**Wenn du es dir sichtbar machen willst:**

```python
print(bool([]))              # False
print(bool(["brot"]))        # True
```

`bool()` zeigt dir, was Python in einer Bedingung aus einem Wert macht. Du brauchst die Funktion im Spiel nicht — aber sie beantwortet die Frage „gilt das jetzt als wahr?" ohne Raten, so wie `type()` in Etappe 1 die Frage nach dem Datentyp beantwortet hat.

### 7. Mutable und immutable — der wichtigste Abschnitt dieser Etappe

Lies das hier langsam. Es sind vier Zeilen Code und die Erklärung für die meisten unverständlichen Bugs, die dir in den nächsten Monaten begegnen.

**Erster Block — probier ihn aus, bevor du weiterliest:**

```python
a = [1, 2]
b = a
b.append(3)
print(a)      # Was steht hier?
```

Ausgegeben wird `[1, 2, 3]`. Du hast `b` verändert, und `a` hat sich mitverändert.

**Zweiter Block:**

```python
x = "hallo"
y = x
y += " welt"
print(x)      # Und hier?
```

Ausgegeben wird `hallo`. Unverändert. Obwohl es doch dasselbe Muster war.

**Warum der Unterschied?**

Erinnerst du dich an Etappe 1? Dort stand: *Eine Variable ist kein Behälter, sondern ein Schild, das auf einen Wert zeigt.* Damals wirkte das wie Haarspalterei. Hier ist die Einlösung.

`b = a` legt keine Kopie an. Es hängt ein **zweites Schild an denselben Wert**. Es gibt weiterhin nur eine Liste, aber zwei Namen dafür. Änderst du sie über den einen Namen, siehst du die Änderung auch über den anderen — es ist ja dieselbe Liste.

Beim String passiert etwas anderes: **Strings lassen sich gar nicht verändern.** `y += " welt"` ändert nicht den bestehenden String, sondern erzeugt einen neuen und hängt das Schild `y` daran um. Das Schild `x` zeigt noch auf den alten Wert.

**Die Begriffe dafür:**

> **mutable** — veränderbar. Listen, Dictionaries, Sets.
> **immutable** — unveränderbar. Strings, Zahlen, Booleans, Tuples.

Bei immutablen Werten kann dir das nie passieren. Bei mutablen ständig.

**Warum das für dich konkret wichtig ist:**

In **Etappe 10** baust du zwei Spieler, und beide bekommen versehentlich dasselbe Inventar-Objekt. Der eine hebt ein Brot auf, der andere hat es plötzlich auch. Das ist einer der berühmtesten Python-Stolpersteine überhaupt — und du wirst ihn nur verstehen, wenn du diesen Abschnitt verstanden hast.

In **Etappe 14** erzeugst du dein Minenraster mit `[["."] * 5] * 5`, änderst ein einziges Feld, und plötzlich hat sich eine ganze Spalte verändert. Derselbe Grund.

**Wenn du wirklich eine Kopie willst:**

```python
b = a.copy()      # oder: b = list(a)
```

Merk dir, dass es das gibt. Brauchen wirst du es heute noch nicht.

### 8. `.split()` — Zwei-Wort-Befehle, die Schuld aus Etappe 3

In Etappe 3 hast du entschieden, wie deine Befehlssprache aussieht, aber `nimm brot` noch nicht verarbeiten können. Hier ist das Werkzeug — und es passt genau in diese Etappe, denn **`.split()` liefert eine Liste**.

```python
eingabe = "nimm brot"
teile = eingabe.split()      # ["nimm", "brot"]

teile[0]     # "nimm"   — das Verb
teile[1]     # "brot"   — das Ziel
```

`.split()` zerlegt einen String an den Leerzeichen. Mehrere Leerzeichen hintereinander sind kein Problem, und führende oder abschließende verschwinden — dein `.strip()` aus Etappe 3 wird dadurch fast überflüssig, schadet aber nicht.

**Die Falle, die dich sicher erwischt:**

```python
eingabe = "inventar"
teile = eingabe.split()      # ["inventar"] — nur EIN Element
teile[1]                     # IndexError!
```

Gibt der Spieler nur ein Wort ein, existiert `teile[1]` nicht. Du musst also prüfen, bevor du darauf zugreifst — mit `len(teile)`. Das ist der erste Ort, an dem du `len()` produktiv brauchst, und ein guter.

**Ehrlich eingeordnet:** Diese Lösung trägt bis Etappe 7. Sie kommt an Grenzen, sobald du `nimm den rostigen schlüssel` erlauben willst — drei Wörter, und `teile[1]` ist „den". Das ist kein Problem für heute; die meisten Textadventures der Achtzigerjahre haben genau so funktioniert.

### 9. Slicing — nur zum Wiedererkennen

```python
inventar[0:2]     # die ersten beiden
inventar[:3]      # von vorn bis Position 3 (ausschließlich)
inventar[2:]      # ab Position 2 bis zum Ende
```

Ein Doppelpunkt in den Klammern gibt dir einen **Ausschnitt** statt eines einzelnen Elements. Die obere Grenze ist ausgeschlossen — dasselbe Prinzip wie bei `range()`.

Du brauchst das heute nicht. Aber du wirst es in fremdem Code sehen, und dann soll es nicht rätselhaft sein.

---

## Dein Auftrag

Schrittweise, nach jedem Schritt ausführen.

**Schritt 1 — Die beiden Listen**
Vor der Hauptschleife: ein leeres `inventar`. Und eine zweite Liste mit dem, was am Ort herumliegt — mindestens `brot`, `stuhl` und `schluessel`.

Zwei Listen, weil ein Gegenstand von der einen in die andere wandert. Das ist der ganze Mechanismus.

**Schritt 2 — Der Befehl `inventar`**
Zeigt an, was der Spieler trägt. Bei leerem Inventar eine eigene Meldung — mit `if not inventar:`, nicht mit `len()`.

Gib die Gegenstände mit einer `for`-Schleife aus. Deine erste Schleife über eine Liste statt über `range()`.

**Schritt 3 — Die Eingabe zerlegen**
`.split()` direkt nach `.lower().strip()`. Das erste Wort ist der Befehl, das zweite das Ziel.

**Wichtig:** Deine bestehenden Ein-Wort-Befehle aus Etappe 3 müssen weiter funktionieren. `umsehen`, `reden` und `beenden` haben kein zweites Wort — dein Code darf nicht abstürzen, wenn `teile[1]` nicht existiert.

Das ist die zweite Übung im übergreifenden Prinzip: **Neues hinzufügen, ohne Bestehendes kaputtzumachen.** Prüf danach alle drei alten Befehle durch.

**Schritt 4 — `nimm <ding>`**
Vier Fälle, und alle vier gehören dazu:

- Der Gegenstand liegt hier → aus der Ortsliste entfernen, ins Inventar legen
- Der Gegenstand liegt nicht hier → freundliche Meldung
- Das Inventar ist voll → deine Entscheidung von oben
- Es wurde kein Gegenstand genannt (`nimm` allein) → nachfragen

Der vierte Fall wirkt kleinlich. Genau daran stürzen Programme ab.

**Schritt 5 — Die Obergrenze**
Maximal 10 Gegenstände. Prüf mit `len()`, bevor du etwas hinzufügst.

Kommentier, dass dieser Fall in Etappe 20 nochmal aufgegriffen wird.

**Schritt 6 — `ablege <ding>`**
Der umgekehrte Weg: aus dem Inventar entfernen, in die Ortsliste legen.

**Und hier eine Auflage:** Prüf mit `in`, ob der Gegenstand überhaupt im Inventar ist, *bevor* du `remove()` aufrufst. Probier vorher einmal aus, was ohne die Prüfung passiert — der `ValueError` gehört zu den Fehlern, die du gesehen haben solltest.

**Schritt 7 — Der Stuhl, den man nicht nehmen kann**
Nicht alles ist tragbar. Ein umgestoßener Stuhl bleibt liegen.

Du brauchst dafür heute keine neue Technik — eine zweite Liste mit dem, was fest ist, und eine Prüfung mit `in`. Aber es ist erzählerisch wichtig: Eine Welt, in der man alles einsammeln kann, fühlt sich wie ein Lager an. Eine Welt, in der manches liegen bleibt, fühlt sich wie ein Ort an.

**Schritt 8 — Der Schlüssel**
Wenn der Spieler ihn aufnimmt, bekommt er einen Satz dazu. Er passt zu keiner Tür im Dorf — und der Spieler soll sich fragen, wozu dann.

Setz einen Kommentar: In Etappe 14 öffnet er die Mine. Das ist der erste Faden, den du über zehn Etappen spannst.

---

## Was NICHT in diese Etappe gehört

- ❌ Mehrere Orte, an denen unterschiedliche Dinge liegen → **Etappe 5**
- ❌ Gegenstände mit Eigenschaften (Gewicht, Schaden, Haltbarkeit) → **Etappe 11**
- ❌ Ausrüstungs-Slots — Waffe in der Hand, Helm auf dem Kopf → **Etappe 10**
- ❌ Ein Set für schon gesehene Gegenstände → **Etappe 6**
- ❌ Funktionen wie `zeige_inventar()` → **Etappe 7**
- ❌ `try` / `except` beim `remove()` → **Etappe 20**
- ❌ Crafting, Gegenstände kombinieren → **Etappe 22**

**Besonders verlockend werden die Eigenschaften sein.** Sobald ein Gegenstand mehr als einen Namen hat — ein Gewicht, eine Beschreibung — willst du etwas anderes als eine Liste von Strings. Das Gefühl ist völlig richtig, und es ist genau der Grund, warum es Etappe 5 und Etappe 11 gibt.

Heute bleibt es bei Strings. Die Beschränkung zu spüren ist der Sinn der Übung.

---

## Selbsttest

- [ ] `inventar` beginnt leer und existiert vor der Hauptschleife
- [ ] `nimm brot` legt das Brot ins Inventar und entfernt es vom Ort
- [ ] `nimm brot` ein zweites Mal meldet, dass hier nichts mehr liegt
- [ ] `ablege brot` funktioniert und legt es zurück
- [ ] `inventar` zeigt die Gegenstände einzeln an
- [ ] Ein leeres Inventar hat eine eigene Meldung, geprüft mit `if not inventar:`
- [ ] Der Stuhl kann nicht aufgenommen werden
- [ ] Mehr als 10 Gegenstände sind nicht möglich
- [ ] `nimm` ohne zweites Wort stürzt nicht ab
- [ ] `umsehen`, `reden` und `beenden` aus Etappe 3 funktionieren unverändert
- [ ] Vor jedem `remove()` steht eine Prüfung mit `in`
- [ ] Nirgends steht `inventar = inventar.append(...)`
- [ ] Du hast die beiden Blöcke aus dem Abschnitt „mutable und immutable" ausgeführt
- [ ] Ein Kommentar verweist auf Etappe 14 (Schlüssel) und auf Etappe 20 (volles Inventar)

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten:

1. **Warum ist der erste Index 0?** Und was hat das mit `range()` aus Etappe 3 zu tun?
2. **Was macht `liste[-1]`?** Wann ist das praktischer als `liste[len(liste) - 1]`?
3. **Was passiert bei `liste[99]`, wenn die Liste 3 Einträge hat?** Wie heißt der Fehler?
4. **Was verändert `append()` — die Liste selbst, oder gibt es eine neue zurück?** Was passiert bei `inventar = inventar.append("brot")`?
5. **Erklär den Unterschied zwischen den beiden Blöcken:**
   ```python
   a = [1, 2];    b = a;   b.append(3);      print(a)
   x = "hallo";   y = x;   y += " welt";     print(x)
   ```
   Warum verhalten sie sich unterschiedlich?
6. **Was heißt mutable und immutable?** Nenn je zwei Typen.
7. **Was macht `.split()` und was gibt es zurück?** Was passiert bei einem Ein-Wort-Befehl?
8. **Warum ist `if inventar:` erlaubt?** Welche Regel aus Etappe 2 steckt dahinter?
9. **Was ist der Unterschied zwischen `for g in inventar:` und `for i in range(len(inventar)):`?** Die entscheidende Frage dabei: Willst du das *Element* oder seine *Position*?
10. **Was ist der Unterschied zwischen `inventar.append("x")` und `inventar + ["x"]`?**

**Frage 5 ist die wichtigste des ganzen ersten Blocks.** Wenn du sie sauber beantworten kannst, hast du etwas verstanden, das viele Programmierer erst nach Jahren wirklich begreifen. Wenn nicht: ausführen, verändern, nochmal ausführen. Erklärungen helfen hier weniger als Beobachtung.

---

## Transferaufgabe (10–15 Minuten)

**Neue Datei, außerhalb des Spiels.** `uebung_04.py`.

**Teil 1 — Die Grundlagen**

> Leg eine Liste mit drei Dorfbewohnern an.
> Gib den zweiten aus. Dann den letzten — ohne `len()` zu benutzen.
> Häng einen vierten an. Entferne den ersten.
> Gib nach jedem Schritt die ganze Liste und ihre Länge aus.

Nichts davon ist schwer. Der Zweck ist, dass du die vier Operationen einmal außerhalb deines Inventars gemacht hast. Wer Listen nur im Kontext des eigenen Spiels bedienen kann, kann keine Listen.

**Teil 2 — Das Experiment, auf das es ankommt**

> Weise deine Bewohnerliste einer zweiten Variable zu.
> Entferne über die **zweite** Variable jemanden.
> Gib danach die **erste** aus.

Schreib auf, was du erwartest, bevor du es ausführst. Dann führ es aus.

Danach dasselbe noch einmal — aber diesmal mit `.copy()` bei der Zuweisung. Was ist jetzt anders?

Das sind sechs Zeilen Code und die wichtigste Beobachtung dieser Etappe.

---

## Kaputtmachen

Nach jedem Experiment rückgängig machen.

**Experiment 1 — Der Rückgabewert von `append()`**
```python
inventar = ["brot"]
inventar = inventar.append("lampe")
print(inventar)
```
Kein Absturz. Aber was steht in `inventar`? Warum? Das ist Fehler vom Typ 3 in Reinform — und einer der häufigsten überhaupt.

**Experiment 2 — `remove()` mit etwas, das nicht drin ist**
Nimm die `in`-Prüfung heraus und lege etwas ab, das du gar nicht hast. Lies den `ValueError`. In Etappe 20 fängst du ihn ab; heute sollst du wissen, wovor du dich schützt.

**Experiment 3 — Der Index, der einen zu weit geht**
```python
inventar = ["brot", "schluessel", "lampe"]
print(inventar[3])
```
Drei Einträge, Index 3. Warum knallt es? Wie heißt der höchste gültige Index?

**Experiment 4 — Ein Wort zu wenig**
Tipp `nimm` ohne Gegenstand, nachdem du die `len(teile)`-Prüfung entfernt hast. Der `IndexError` kommt aus deinem eigenen Befehlsparser — genau der Fall, den Schritt 4 abfangen sollte.

**Experiment 5 — Die geteilte Liste**
```python
inventar = ["brot"]
rucksack = inventar
rucksack.append("lampe")
print(inventar)
```
Zwei Namen, eine Liste. **Bau das in dein Spiel ein und beobachte es dort**, nicht nur im Testskript. In Etappe 10 passiert dir das mit zwei Spielern, und dann ist es schwerer zu sehen.

**Experiment 6 — Einen zu weit, diesmal in der Schleife**
```python
inventar = ["brot", "schluessel", "lampe"]
for i in range(len(inventar) + 1):
    print(inventar[i])
```
Drei Ausgaben, dann ein Absturz. Nimm das `+ 1` weg und führ es nochmal aus.

Das ist derselbe Fehler wie Experiment 3, aber versteckt in einer Schleife — und genau so wird er dir in freier Wildbahn begegnen. Hier siehst du die Kette in einem Stück: **Länge → gültige Indizes → `range()`.** In Etappe 14 hängt dein ganzes Minenraster daran.

**Experiment 7 — Die versteckte Annahme**
Dein `nimm brot` funktioniert. Tipp jetzt der Reihe nach:

```text
nimm
nimm brot kuchen
nimm    brot
```

Der erste Fall stürzt ab, wenn du die `len(teile)`-Prüfung entfernst — das ist bekannt. Interessanter ist der zweite: Was landet in `teile[1]`, und was passiert mit „kuchen"?

**Das ist die eigentliche Lektion dieser Etappe, und sie ist größer als Listen:**

> Code funktioniert oft nicht, weil er allgemein richtig ist, sondern weil die Eingaben bisher zufällig genau so aussahen, wie der Programmierer sie erwartet hat.

Schreib in `GELERNT.md` einen Satz, der so anfängt: *„Meine Befehlsverarbeitung nimmt momentan an, dass …"* Du musst diese Annahmen heute nicht auflösen. Du sollst wissen, dass du welche gemacht hast. In Etappe 7 räumst du auf, in Etappe 20 fängst du ab.

**Experiment 8 — Während der Schleife entfernen**
```python
inventar = ["brot", "schluessel", "lampe"]
for gegenstand in inventar:
    inventar.remove(gegenstand)
print(inventar)
```
Erwartest du eine leere Liste? Führ es aus. Das Ergebnis überrascht fast jeden.

Erklärung in einem Satz: Die Schleife merkt sich eine Position, während die Liste unter ihr kürzer wird. **Verändere nie eine Liste, über die du gerade läufst.** Diese Regel kommt in Etappe 12 wieder, wenn du NPCs entfernst.

---

## Häufige Stolpersteine

| Fehlermeldung / Symptom | Was dahintersteckt | Wo du suchst |
|---|---|---|
| `IndexError: list index out of range` | Index zu groß, oder zweites Wort fehlt | Höchster Index ist `len() - 1`; `len(teile)` prüfen |
| `ValueError: list.remove(x): x not in list` | `remove()` ohne vorherige Prüfung | Ein `if ... in ...` davorsetzen |
| `AttributeError: 'NoneType' object has no attribute 'append'` | Vorher `liste = liste.append(...)` geschrieben | Die Zeile mit dem `=` vor `.append()` |
| Die Liste ist plötzlich `None` | Dasselbe — `append()` gibt nichts zurück | `.append()` ohne Zuweisung schreiben |
| Zwei Listen ändern sich gemeinsam | Zuweisung statt Kopie | `.copy()` — oder war es Absicht? |
| Beim Löschen in der Schleife bleibt etwas übrig | Liste wird während der Iteration verändert | Über eine Kopie laufen |
| `nimm brot` funktioniert nicht | `.split()` fehlt oder Vergleich mit ganzer Eingabe | Was steht wirklich in `teile[0]`? |
| Der Gegenstand ist doppelt da | Vom Ort entfernen vergessen | Beide Listen ausgeben |
| `TypeError: 'in <string>' requires string as left operand` | `in` auf etwas angewandt, das keine Liste ist | Was ist der Typ? `type()` benutzen |

**Der Debugging-Reflex dieser Etappe:** Wenn Gegenstände sich merkwürdig verhalten, gib **beide Listen** aus, nicht nur eine.

```python
print(f"DEBUG: hier={gegenstaende_hier}  inventar={inventar}")
```

Fast jeder Inventar-Fehler ist ein Gegenstand, der in beiden oder in keiner Liste steht. Das siehst du nur, wenn du beide gleichzeitig anschaust.

---

## Ein Blick nach vorne

Heute ist dein Inventar eine Liste von Wörtern:

```python
inventar = ["brot", "schluessel"]
```

In **Etappe 5** bekommt jeder Ort seine eigenen Gegenstände, und der Schlüssel liegt nicht mehr da, wo du stehst.

In **Etappe 6** lernst du, dass ein *Set* besser wäre für „was habe ich schon gesehen" — weil dort nichts doppelt sein kann.

In **Etappe 11** wird daraus:

```python
inventar = [Weapon("Schwert", schaden=5), Tool("Hacke", haltbarkeit=20)]
```

Jeder Gegenstand ist dann ein Objekt mit eigenen Eigenschaften. Dein `nimm`-Befehl wird sich kaum ändern — die Liste bleibt eine Liste. Nur ihr Inhalt wird reicher.

In **Etappe 22** werden Gegenstände zu Zutaten, aus denen sich andere Gegenstände bauen lassen.

Und in **Etappe 25** stehen sie gar nicht mehr im Code, sondern in einer JSON-Datei, die du bearbeiten kannst, ohne zu programmieren.

Du legst heute die Struktur an, in der all das stattfinden wird.

---

## Abschluss

**`GELERNT.md`:**
Zwei bis drei Sätze. Zusätzlich diesmal:

- Deine Entscheidung zur Benennung von Gegenständen (Kennung und Anzeigename)
- Was passiert, wenn das Inventar voll ist
- Und in eigenen Worten: der Unterschied zwischen den beiden Blöcken aus Lernziel 5

Der letzte Punkt ist der wichtigste Eintrag, den du bisher geschrieben hast. Du wirst in Etappe 10 darauf zurückblättern.

**Commit:**
```bash
git add .
git commit -m "Etappe 4: Das Inventar"
git push
```

---

## Wenn du mehr willst

Optional, erst bei grünem Selbsttest.

**Nummerierte Ausgabe.** Statt einer schlichten Aufzählung eine nummerierte Liste. Du brauchst dafür den Index — entweder mit `range(len(...))` oder mit `enumerate()`, das du in Etappe 14 sowieso kennenlernst. Achte auf die Zählung: Der Spieler will `1.` sehen, nicht `0.`.

**Gegenstände zählen.** Zwei Brote statt eines. Das geht mit einer Liste, in der `"brot"` zweimal steht — und `.count("brot")` sagt dir, wie oft. Es geht *nicht* gut mit einer Liste, wenn du Mengen ändern willst. Merk dir das Problem für Etappe 5, wo du das passende Werkzeug bekommst.

**Ein `untersuche <ding>`-Befehl.** Beschreibt einen Gegenstand genauer, wenn er im Inventar oder am Ort ist. Erzählerisch das Beste, was du heute einbauen kannst: Der Schlüssel bekommt eine Beschreibung, die eine Frage aufwirft — Rost, eine Gravur, eine Form, die zu keinem Schloss im Dorf passt.

**Der Stuhl, der etwas verbirgt.** Wer den umgestoßenen Stuhl untersucht, findet darunter etwas. Das braucht nur ein `if` und ein `append()` — aber es lehrt den Spieler etwas Wichtiges über deine Welt: dass Hinsehen sich lohnt. Wenn du das einmal einlöst, untersucht er ab da alles.

---

> **Nächste Etappe:** [Etappe 5 — Die Karte](etappe-05-die-karte.md) · Dictionaries, verschachtelte Dictionaries, `keys()` / `values()` / `items()`
> Dort bekommt dein Dorf zum ersten Mal eine Ausdehnung. Und du siehst zum ersten Mal, wie sich Daten vom Code lösen.
