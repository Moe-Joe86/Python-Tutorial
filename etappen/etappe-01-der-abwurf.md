# Etappe 1 — Der Abwurf

> **Block 1: Fundament** · Etappe 1 von 30 · [← Etappe 0](../Vorposten_Lehrplan.md#etappe-0--das-repo) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 2 →](etappe-02-der-erste-kontakt.md)

**Boot.dev:** Variablen, Strings, f-Strings, `print()`, `input()`, Typumwandlung
**Zeitaufwand:** 2–3 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 0 abgeschlossen — Repo steht, venv läuft, ein Commit ist gemacht

---

## Worum es geht

Heute entsteht `spiel.py`. Es fragt nach einem Namen, lässt eine von vier Klassen wählen, zeigt die Lage auf dem Vorposten und setzt einen Funkspruch ab, den niemand beantwortet.

Als Programmierübung ist das mager, und ich sage das lieber selbst, als dir eine Bedeutung vorzuspielen, die diese Etappe nicht hat. Du wirst heute keine Entscheidung treffen, keine Schleife bauen, nichts berechnen. Du legst Werte an und gibst sie aus.

**Der Wert liegt woanders**, und er ist echt: Du baust dir heute eine Gewohnheit an, die die nächsten neunundzwanzig Etappen trägt.

> **Weltzustand wird gespeichert, nicht nur ausgegeben.**

Der Unterschied klingt nach nichts. Er ist der Grund, warum manche Anfängerprojekte in Etappe 12 gegen eine Wand laufen und andere nicht. Wenn du heute `print("Kernintegrität: 100%")` schreibst, existiert diese 100 nirgends — sie ist Text, sie steht in keiner Variable, niemand kann sie verändern. Wenn du stattdessen `kern_integritaet = 100` schreibst und den Wert danach in die Ausgabe einsetzt, existiert er. Und alles, was dein Spiel je tun wird — Schaden nehmen, Wellen zählen, Zustände speichern —, besteht daraus, solche Werte zu verändern.

Das ist die ganze Etappe. Alles andere ist Syntax.

---

## Der lange Bogen

| Was heute entsteht | Wo es wieder auftaucht |
|---|---|
| `kern_integritaet` | **3** — Abbruchbedingung der Wellenschleife · **17** — Vergleich mit dem Startwert |
| `wellen_bis_evakuierung` | **3** — `range(1, 21)` · **17** — der Wellengenerator skaliert daran |
| `letzte_meldung` | **17** — die Rückblende, vier Monate später |
| Die Klassenwahl als Zahl aus `input()` | **2** — bestimmt die Startwerte · **11** — wird zur Klassenhierarchie |
| „Name zeigt auf Wert" statt „Behälter" | **4** — warum zwei Namen dieselbe Liste verändern |
| `=` als „bekommt den Wert" | **2** — die Abgrenzung zu `==` |
| `int()` kann scheitern | **20** — echte Fehlerbehandlung mit `try` / `except` |
| Prinzip: Zustand speichern | **12** — der gesamte Tick beruht darauf |
| Der ASCII-Kopf als mehrzeiliger String | **3** — Balken kommen dazu · **7** — wandert in eine Zeichenfunktion · **29** — wird zur Kulisse |
| Die Sprachentscheidung bei Variablennamen | durchgehend bis **30** · **25** — die Namen werden JSON-Schlüssel |

**Eine dieser Zeilen ist besonders.** `letzte_meldung` wird heute angelegt und **vier Monate lang nicht benutzt**. In Etappe 17 zitierst du sie zurück: *„Die Aufzeichnung läuft immer noch. Sie ist von vor achtzehn Tagen."* Das ist der längste Spannungsbogen des ganzen Projekts, und er beginnt mit einer Zuweisung, die heute nutzlos aussieht.

Schreib sie trotzdem hin. Und schreib in `GELERNT.md`, was drinsteht — sonst erfindest du sie im November neu, und dann war es keine Rückblende, sondern ein Einfall.

Schulden aus früheren Etappen gibt es heute keine. Etappe 1 ist der Anfang des Bogens; sie pflanzt nur.

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

Zwei Fragen. Beide sehen aus wie Geschmack und sind es nicht.

**Erstens: In welcher Sprache heißen deine Variablen?**

`kern_integritaet` oder `core_integrity`. Beides ist vertretbar. Was nicht vertretbar ist: heute das eine, in Etappe 14 das andere. Ein Programm mit `gegner_liste` neben `enemy_count` ist mühsam zu lesen, und du wirst es zwanzig Wochen lang lesen.

Zwei Dinge, die du wissen solltest, bevor du wählst: Python selbst ist englisch (`print`, `len`, `input`) — bei deutschen Namen steht also immer beides nebeneinander. Und in Etappe 25 werden deine Variablennamen zu Schlüsseln in JSON-Dateien. Deutsche Umlaute darin sind erlaubt, aber unangenehm; `integritaet` statt `integrität` ist die übliche Lösung.

Meine Empfehlung, falls du keine hast: durchgehend deutsch, ohne Umlaute. Der Grund ist nicht technisch — es ist deine Muttersprache, und in den ersten Wochen zählt jede Kleinigkeit, die dir das Lesen des eigenen Codes erleichtert. Aber entscheide selbst, und dann bleib dabei.

**Zweitens: Wie speicherst du die gewählte Klasse?**

Der Spieler tippt eine Zahl. Aber was steht danach in deiner Variable?

- **Die Zahl** (`klasse = 2`) — kurz, aber `if klasse == 2:` sagt in Etappe 2 niemandem, was gemeint ist. Auch dir nicht, in drei Wochen.
- **Der Name** (`klasse = "heavy"`) — eine Umwandlung mehr heute, dafür liest sich `if klasse == "heavy":` von selbst.

Das ist keine Kleinigkeit. In Etappe 2 baust du auf dieser Variable eine Verzweigung auf, in Etappe 11 wird daraus eine Klassenhierarchie. Wer die Zahl behält, schreibt in Etappe 11 eine Übersetzungstabelle, die er heute hätte sparen können.

Beide Entscheidungen kommen in `GELERNT.md`. Nicht als Notiz, sondern als Satz mit Begründung — du wirst ihn wieder brauchen.

---

## Die Konzepte

### 1. Was eine Variable wirklich ist

Fast jede Einführung sagt: *Eine Variable ist ein Behälter für einen Wert.* Das Bild ist bequem und es ist falsch, und du wirst in Etappe 4 vier Stunden mit einem Fehler verbringen, den nur dieses Bild ermöglicht.

Das richtige Bild: **Ein Name zeigt auf einen Wert.**

```python
preis = 3
kosten = preis
```

Es gibt hier keine zwei Kisten mit je einer 3 darin. Es gibt eine 3, und zwei Namen zeigen darauf. Bei Zahlen merkst du den Unterschied nie. Bei Listen — Etappe 4 — merkst du ihn sofort und schmerzhaft.

Merk dir die Formulierung. Wenn du in vier Wochen fragst „warum hat sich meine andere Liste auch geändert?", ist dieser Absatz die Antwort.

### 2. `=` heißt „bekommt den Wert"

```python
tassen = 3
```

Lies das nicht als „tassen ist gleich 3". Lies es als: **tassen bekommt den Wert 3.** Es ist ein Befehl, keine Feststellung. Die Zeile tut etwas.

Das klingt pedantisch, bis du in Etappe 2 zum ersten Mal `if x = 3:` schreibst und dich fragst, warum Python schimpft. Dort gibt es nämlich ein zweites Zeichen — `==` — und *das* ist die Feststellung. Ein Zeichen Unterschied, zwei völlig verschiedene Dinge.

### 3. Die vier Datentypen, die heute zählen

| Typ | Was es ist | Beispiel |
|---|---|---|
| `str` | Text | `"Vasquez"`, `"40"` |
| `int` | Ganzzahl | `40`, `-3` |
| `float` | Kommazahl | `0.75` |
| `bool` | Wahrheitswert | `True`, `False` |

`bool` brauchst du heute noch nicht — er kommt in Etappe 2. Die anderen drei brauchst du sofort.

**Der wichtigste Satz dieser Etappe:** `"40"` und `40` sind nicht dasselbe. Das erste ist Text, der zufällig aus Ziffern besteht. Das zweite ist eine Zahl.

```python
"40" + "5"     # "405"    — Text wird aneinandergehängt
40 + 5         # 45       — Zahlen werden addiert
"40" + 5       # TypeError — Python weiß nicht, was du willst
```

**Und du musst nie raten, welcher Typ gerade vorliegt.** Python sagt es dir:

```python
print(type(40))       # <class 'int'>
print(type("40"))     # <class 'str'>
print(type(0.75))     # <class 'float'>
```

Lies die Ausgabe als *„das ist ein `int`"* — der Rest (`<class ...>`) ist Beiwerk.

`print(type(x))` ist die nützlichste Zeile dieser Etappe. Sie kostet dich fünf Sekunden und beantwortet die Frage, aus der heute fast jeder Fehler entsteht. In Abschnitt 8 machen wir daraus einen Reflex.

### 4. Strings, und wie man mehrere Zeilen schreibt

Anführungszeichen: `'einfach'` oder `"doppelt"`, Python ist beides recht. Nimm eine Sorte und bleib dabei.

Für mehrere Zeilen gibt es drei Anführungszeichen:

```python
speisekarte = """
  Brot .......... 2
  Suppe ......... 4
"""
```

Alles zwischen den dreifachen Anführungszeichen kommt so heraus, wie es dasteht — inklusive Zeilenumbrüchen und Leerzeichen. Genau das brauchst du heute für den Kopf deines Spiels.

**Vorsicht bei der Einrückung:** Innerhalb eines dreifachen Strings zählt jedes Leerzeichen. Was in deinem Editor ordentlich eingerückt aussieht, ist im String enthalten und wird mit ausgegeben.

### 5. f-Strings — Werte in Text einsetzen

```python
kunde = "Meier"
offen = 12

print(f"Herr {kunde} schuldet noch {offen} Euro.")
```

Das `f` vor dem Anführungszeichen schaltet die geschweiften Klammern scharf. Ohne das `f` sind `{kunde}` und `{offen}` einfach Zeichen — Python gibt sie wörtlich aus, mit Klammern, und wundert sich nicht.

Das ist ein Fehler, der **nicht abstürzt**. Er läuft durch und liefert Unsinn. Merk dir das Gefühl; im Lehrplan heißt diese Sorte *Fehler vom Typ 3*, und sie ist die gefährlichste, die es gibt.

In den Klammern darf auch gerechnet werden:

```python
print(f"Das macht {offen * 2} Euro mit Zuschlag.")
```

### 6. `print()` — und was es nicht tut

`print()` schreibt etwas auf den Bildschirm. Mehr nicht. Es speichert nichts, es verändert nichts, es gibt nichts zurück, mit dem du weiterarbeiten könntest.

Das ist genau der Punkt aus dem ersten Abschnitt: Was du nur druckst, ist weg. Was in einer Variable steht, bleibt.

Ab Etappe 7 wird daraus eine harte Regel — Logik rechnet, Darstellung druckt —, und in Etappe 28 entscheidet sie darüber, ob dein Spiel eine Oberfläche bekommen kann oder neu geschrieben werden muss. Heute reicht es, den Unterschied zu kennen.

### 7. `input()` gibt **immer** Text zurück

```python
antwort = input("Wie viele Brötchen? ")
```

Egal was der Mensch tippt — `7`, `sieben`, gar nichts — in `antwort` steht ein `str`. Immer. Ohne Ausnahme. Auch dann, wenn es aussieht wie eine Zahl.

Das ist die Quelle des häufigsten Anfängerfehlers überhaupt:

```python
anzahl = input("Wie viele? ")
print(anzahl * 3)          # bei Eingabe 7 kommt "777" heraus
```

Kein Absturz. Wieder ein Fehler vom Typ 3. Der Text wird verdreifacht statt der Zahl.

### 8. Typumwandlung — und wo sie scheitert

```python
int("7")        # 7
int("7 ")       # 7      — Leerzeichen am Rand sind Python egal
int("sieben")   # ValueError
int("7.5")      # ValueError — auch das nicht
float("7.5")    # 7.5
str(7)          # "7"
```

`int()` nimmt Text und macht daraus eine Ganzzahl — **wenn es geht.** Wenn nicht, stürzt dein Programm ab mit `ValueError: invalid literal for int() with base 10: 'sieben'`.

**Und jetzt der Reflex, der dich durch die nächsten Monate trägt: `print(type(x))`.**

Eine Umwandlung ist eine Behauptung — *„das hier ist jetzt eine Zahl"*. Behauptungen prüft man. Und zwar so:

```python
antwort = input("Wie viele? ")
print(type(antwort))          # <class 'str'>   — immer, ausnahmslos

zahl = int(antwort)
print(type(zahl))             # <class 'int'>   — jetzt kann man rechnen
```

Zwei Zeilen, die du wieder löschst, sobald du die Antwort hast. **Genau dafür sind sie da.** Das ist kein Anfängerkrückstock, den man später ablegt — es ist die schnellste Methode, die Python für diese Frage anbietet, und erfahrene Entwickler tippen sie täglich.

**Mach das heute mindestens dreimal:**

1. Direkt nach jedem `input()` in deinem Programm.
2. Direkt nach jedem `int()`.
3. Bei einer deiner Lagevariablen, bevor du sie ausgibst — nur um zu sehen, dass dort tatsächlich `int` steht und nicht versehentlich `str`.

Wenn du in vier Wochen vor einem `TypeError` sitzt und nicht weißt warum, ist diese Zeile die Antwort. Und in Etappe 25, wenn Werte aus JSON-Dateien kommen und plötzlich Text sind, wo du Zahlen erwartet hast, ist sie es wieder.

**Ein Hinweis zur Schreibweise:** `type(x)` allein gibt nichts aus — es *liefert* den Typ zurück. Sichtbar wird er erst durch `print()` drumherum. Dasselbe Muster wie bei `int()`: Die Funktion liefert etwas, und du musst etwas damit tun.

Der Absturz bei `int("sieben")` ist heute übrigens völlig in Ordnung. Ein Absturz ist ein ehrlicher Fehler: Er zeigt dir sofort, wo das Problem sitzt. In Etappe 20 lernst du, ihn abzufangen; bis dahin darf dein Programm ruhig abstürzen, wenn jemand Unsinn eingibt. Du bist der einzige Spieler.

### 9. Zustand speichern statt ausgeben

Der Kern der Etappe, jetzt konkret. Zwei Wege, dieselbe Ausgabe:

```python
# Weg A
print("Auf Lager: 12 Brote")

# Weg B
lager = 12
print(f"Auf Lager: {lager} Brote")
```

Auf dem Bildschirm steht dasselbe. Im Programm ist der Unterschied gewaltig: Nur bei B existiert die 12 als Wert. Nur bei B kannst du morgen `lager = lager - 1` schreiben.

**Deine Regel für heute:** Jede Zahl und jede Tatsache über die Welt bekommt eine Variable. Auch die, die du heute nur einmal ausgibst. Auch `letzte_meldung`, die vier Monate lang nichts tut.

### 10. Namen, die etwas sagen

`k = 100` ist schneller getippt als `kern_integritaet = 100` und in drei Wochen wertlos. Python erlaubt dir Buchstaben, Ziffern und Unterstriche; Ziffern nicht am Anfang. Üblich ist `kleinbuchstaben_mit_unterstrichen`.

**Und Kommentare.** Alles hinter `#` ignoriert Python:

```python
lager = 12      # Stand vom Morgen, wird abends neu gezählt
```

Ein guter Kommentar erklärt **warum**, nicht was. `lager = 12  # setzt lager auf 12` ist Lärm. Die Zeile oben ist nützlich.

### 11. Der Kopf: ein Bild aus Zeichen

Am Ende der Etappe, nicht am Anfang. **Das Ziel in einem Satz: ein dreifacher String mit einer groben Skizze der Kuppel, darunter die Lagewerte per f-String.** Nichts weiter — kein Rahmen aus Sonderzeichen, keine Farben, keine halbe Stunde Feinschliff.

Und weil „mach eine Skizze der Kuppel" für jemanden, der heute zum ersten Mal `print()` benutzt hat, keine brauchbare Anweisung ist, hier ganz konkret, was gemeint ist.

**Es ist ein einziger dreifacher String, in dem du Zeichen so anordnest, dass sie ein Bild ergeben.** Mehr Technik steckt nicht dahinter — du kannst das seit Abschnitt 4.

Nimm dieses Beispiel aus einem völlig anderen Spiel als Muster, damit die *Form* klar ist:

```python
kneipe = """
==============================
      Z U M   A N K E R
==============================
   [][]   [][]   [][]
    ()     ()     ()
------------------------------
"""

print(kneipe)
```

Das ist alles. Gleichheitszeichen als Linien, Klammern als Hocker, Leerzeichen zum Ausrichten. Niemand muss darin einen Tresen erkennen — man muss erkennen, dass jemand einen gemeint hat.

**Welche Zeichen sich eignen:**

| Zeichen | Wofür |
|---|---|
| `=` `-` `_` | waagerechte Linien, Böden, Trennlinien |
| `\|` | senkrechte Wände |
| `/` `\\` | Schrägen, Dächer, Kuppelrundung |
| `.` `:` | Boden, Staub, leerer Raum |
| `#` `[]` | feste Masse, Blöcke, Anlagen |
| `*` `+` | Lichter, Antennen, Markierungen |

**So gehst du vor — fünf Minuten, wörtlich:**

1. **Zeichne es zuerst außerhalb von Python.** Neue leere Datei im Editor, oder ein Blatt Papier. Ohne `print`, ohne Anführungszeichen, ohne Python. Nur Zeichen.
2. **Vier bis acht Zeilen, nicht mehr.** Eine Kuppel ist eine Schräge, eine waagerechte Linie darunter, ein Boden. Das reicht.
3. **Kopier das Ergebnis zwischen `"""` und `"""`** und gib es mit `print()` aus.
4. **Führ es aus und schau, ob es verrutscht ist.** Falls ja: Abschnitt 4, Absatz „Vorsicht bei der Einrückung". Der dreifache String nimmt jedes Leerzeichen wörtlich — auch die, die dein Editor zur Einrückung eingefügt hat. Die Zeilen im String müssen ganz links anfangen, auch wenn das im Code seltsam aussieht.
5. **Darunter, als eigenes `print()`, die Lagewerte per f-String.** Der Kopf ist Kulisse und bleibt immer gleich. Die Zahlen darunter kommen aus Variablen und ändern sich später.

**Falls dir partout nichts einfällt:** Drei Zeilen genügen vollkommen.

```
  /------------\
 |  VORPOSTEN   |
 ----------------
```

Ehrlich — das ist ausreichend, und es ist besser als nichts, weil es der Anfang eines Fadens ist und nicht sein Höhepunkt.

**Die Zehn-Minuten-Regel gilt hier streng.** Die Darstellung ist der **letzte** Schritt der Etappe, und sie ist fertig, wenn man sie erkennt. Kein Rahmen aus Sonderzeichen, keine Farben, kein Feinschliff. Wer hier eine Stunde verbringt, hat einen netten Abend gehabt und kein Python gelernt — und in Etappe 29 wird ohnehin ein Bild daraus, das dein Kunstwerk ersetzt.

**Was das Ganze soll:** Ab Etappe 3 wachsen Balken hinein, ab Etappe 4 die Anmarschbahn, ab Etappe 14 ein ganzes Raster. In Etappe 7 wandert das alles in eine eigene Zeichenfunktion, und in Etappe 28 wird die Funktion ausgetauscht statt umgeschrieben. Deine drei Zeilen heute sind die erste davon.

### 12. Wie du dein Programm startest — und die erste Fehlermeldung liest

Im Terminal, im Projektordner, mit aktiver venv:

```
python spiel.py
```

Wenn etwas schiefgeht, kommt ein **Traceback** — mehrere Zeilen, die aussehen wie ein Unfallbericht. Zwei Regeln dazu, die ab heute gelten und bis Etappe 30 nicht mehr aufhören:

1. **Lies von unten nach oben.** Die letzte Zeile nennt die Fehlerart und den Grund. Das ist fast immer die einzige Zeile, die du brauchst.
2. **Die vorletzte Zeile nennt Datei und Zeilennummer.** Dort schaust du nach.

`SyntaxError` heißt: Python hat den Satzbau nicht verstanden — meist ein fehlendes Anführungszeichen oder eine fehlende Klammer, oft eine Zeile **über** der genannten. `NameError` heißt: Du benutzt einen Namen, den es nicht gibt — meist ein Tippfehler.

---

## Dein Auftrag

Nach jedem Schritt ausführen. Nicht alles schreiben und dann testen — das ist die teuerste Angewohnheit, die man sich im ersten Monat zulegen kann.

1. **Leg `spiel.py` an** und gib eine einzige Zeile aus. Führ es aus. Damit ist bewiesen, dass venv, Ordner und Editor zusammenpassen.

2. **Frag den Namen ab** und begrüße den Spieler mit einem f-String, der den Namen enthält. Setz danach einmal `print(type(name))` darunter und schau nach, was `input()` geliefert hat. Dann lösch die Zeile wieder.

3. **Leg die Lagewerte an.** Diese fünf, mit genau diesen Startwerten:

   | Variable | Wert | Was sie bedeutet |
   |---|---|---|
   | `kern_integritaet` | `100` | Prozent. Fällt sie auf 0, ist das Spiel vorbei. |
   | `munition` | `40` | Schuss. Wenig — das ist Absicht. |
   | `schrott` | `0` | Deine Währung. Du hast noch nichts eingesammelt. |
   | `rekruten_verfuegbar` | `0` | Niemand da, der ein Tor halten könnte. |
   | `wellen_bis_evakuierung` | `20` | So lange musst du durchhalten. |

   **Die Werte sind nicht beliebig, und du sollst sie heute genau so übernehmen.** Sie sind aufeinander abgestimmt: 100 ist ein Prozentwert, an dem sich ab Etappe 3 ein Balken ablesen lässt. 20 Wellen werden in Etappe 3 zu `range(1, 21)`. Und 40 Schuss bei 20 Wellen ist die Zahl, aus der die ganze Atmosphäre entsteht — das rechnet sich der Spieler selbst aus.

   Später darfst du an allen fünf drehen. Heute nicht: Du hast noch kein Spiel, an dem du merken würdest, ob eine Änderung es besser oder unspielbar macht.

   **Alles Zahlen, keine Texte.** Kein `munition = "40"`. Noch keine Ausgabe.

4. **Baue das Lagebriefing** aus mindestens drei f-Strings, die diese Variablen einsetzen. Nirgends darf eine Zahl direkt im Text stehen — `print("Munition: 40")` ist genau das, was diese Etappe verhindern will.

5. **Leg `letzte_meldung` an** und gib sie als aufgezeichnete Durchsage aus. Ein Satz oder zwei, in einer Variable, in deinen eigenen Worten. Sie tut heute nichts weiter — und wird in Etappe 17 zitiert, deshalb kommt der Wortlaut in `GELERNT.md`.

6. **Bau die Klassenwahl.** Vier Klassen (Soldat, Heavy, Engineer, Medic), nummeriert 1 bis 4. Eingabe mit `input()`, Umwandlung mit `int()`, Speicherung nach deiner Design-Entscheidung von oben. Gib zur Bestätigung aus, was gewählt wurde.

   Setz auch hier einmal `print(type(...))` vor und nach dem `int()` und sieh dir den Unterschied an. Erst dann löschen.

7. **Bau den Funkspruch.** Lass den Spieler sich melden und gib als Antwort dieselbe Durchsage aus wie in Schritt 5 — **dieselbe Variable**, nicht derselbe Text noch einmal getippt. Schreib keinen Kommentar dazu; die Wiederholung wirkt von allein.

8. **Prüf die Autorenregel:** Lies deine gesamte Ausgabe durch. Steht irgendwo, dass die Lage schlecht ist? Dann streich es. Die Zahlen machen das.

9. **Zum Schluss, zehn Minuten: der ASCII-Kopf.** Konzept 11 beschreibt das Vorgehen Schritt für Schritt — hier nur die Reihenfolge:

   - Zeichne vier bis acht Zeilen **außerhalb von Python**, in einer leeren Datei oder auf Papier.
   - Kopier sie zwischen dreifache Anführungszeichen, ganz links beginnend.
   - Gib den String mit `print()` aus, **ganz oben im Programm**, vor der Begrüßung.
   - Führ aus. Verrutscht? Dann ist es Einrückung — Zeilen im String nach ganz links.
   - Darunter, als eigenes `print()`, die Lagewerte aus Schritt 4.

   Wenn nach zehn Minuten irgendetwas dasteht, das man als Bauwerk erkennt, ist der Schritt erledigt. Drei Zeilen reichen. Stell den Wecker.

10. **Führ das ganze Programm dreimal aus** — einmal mit einer gültigen Klassenzahl, einmal mit `9`, einmal mit `zwei`. Notier dir, was jeweils passiert. Zwei der drei Fälle sind heute noch kaputt, und das ist Absicht.

---

## Was NICHT in diese Etappe gehört

- ❌ **Prüfen, ob die Eingabe gültig ist** → Etappe 2 (`if`) und Etappe 20 (`try`/`except`)
- ❌ **Wiederholt fragen, bis die Antwort stimmt** → Etappe 3 (Schleifen)
- ❌ **Unterschiedliche Startwerte je Klasse** → Etappe 2
- ❌ **Ein Inventar** → Etappe 4
- ❌ **Funktionen** → Etappe 7
- ❌ **Klassen im Python-Sinn** (`class Marine:`) → Etappe 9 und 11
- ❌ **Gegner, Wellen, Kampf** → Etappe 3

**Der verlockendste Punkt ist der erste.** Nach Schritt 10 hast du gesehen, dass `zwei` dein Programm zum Absturz bringt, und der Reflex „das fange ich schnell ab" ist der Reflex eines guten Programmierers. Das Gefühl ist richtig. Die Zeitplanung nicht.

Denn du hast heute kein Werkzeug dafür. Eine Prüfung braucht `if` — das ist Etappe 2, sie kommt in ein paar Tagen. Eine Wiederholung braucht eine Schleife — Etappe 3. Ein sauberes Abfangen braucht `try` — Etappe 20. Wer das heute mit angelesenem Code löst, hat drei Werkzeuge halb verstanden statt eines ganz, und Etappe 2 verliert ihren Anlass.

Lass es abstürzen. Schreib in `GELERNT.md`: *„Ungültige Eingabe stürzt ab — wird in Etappe 2 behandelt."* Das ist kein Mangel, das ist ein Termin.

---

## Selbsttest

Prüft den Zustand des Programms, nicht dein Selbstbild. Alles muss beobachtbar sein.

- [ ] `python spiel.py` läuft von Anfang bis Ende ohne Fehler durch, wenn du eine gültige Klassenzahl eingibst
- [ ] Der eingegebene Name taucht in der Ausgabe auf
- [ ] Keine einzige Lagezahl steht wörtlich im ausgegebenen Text — alle kommen aus Variablen
- [ ] Wenn du `kern_integritaet` im Code auf `40` änderst und neu startest, ändert sich die Ausgabe an **allen** Stellen
- [ ] Die gewählte Klasse wird bestätigt und steht danach in einer Variable
- [ ] `letzte_meldung` existiert als Variable und wird zweimal ausgegeben — bei der Durchsage und beim Funkspruch
- [ ] Alle fünf Lagewerte existieren als Variablen mit den vorgegebenen Startwerten
- [ ] `print(type(munition))` meldet `int`, nicht `str`
- [ ] Der ASCII-Kopf erscheint ganz oben, ist mindestens drei Zeilen hoch und nicht verrutscht
- [ ] Bei Eingabe `zwei` erscheint ein `ValueError` — und du kannst zeigen, welche Zeile ihn ausgelöst hat
- [ ] Nirgends in der Ausgabe steht in Worten, dass die Lage aussichtslos ist
- [ ] `GELERNT.md` enthält beide Design-Entscheidungen mit Begründung

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten. Dein Mentor fragt sie ab, bevor er „fertig" akzeptiert.

1. Was ist der Unterschied zwischen einer Variable und ihrem Wert?
2. Warum ist „Name zeigt auf Wert" ein besseres Bild als „Behälter"?
3. Was macht das `f` vor einem String genau — und was passiert, wenn es fehlt?
4. Warum ist `munition = "40"` etwas anderes als `munition = 40`?
5. Was gibt `input()` zurück, in welchem Datentyp — und gilt das immer?
6. Was passiert bei `int("drei")`, was bei `int("3 ")`, was bei `int("3.5")`?
7. Wozu ein dreifaches Anführungszeichen?
8. **Warum reicht es nicht, eine Zahl einfach auszugeben?**
9. In welcher Richtung liest man einen Traceback, und was steht in der letzten Zeile?
10. Wie findest du heraus, welchen Typ ein Wert gerade hat — und warum reicht `type(x)` allein nicht?

**Frage 8 ist die wichtigste.** Die anderen acht sind Syntax — die schlägt man notfalls nach, und in vier Wochen sitzen sie ohnehin. Frage 8 ist das Prinzip, auf dem die Etappen 3, 12, 13 und 19 stehen. Wer sie nur mit „damit man sie später ändern kann" beantwortet, hat sie halb verstanden; sag dazu, *was* dein Programm mit einem gespeicherten Wert tun kann, das es mit einem gedruckten nicht kann.

---

## Transferaufgabe (5 Minuten)

**Ausdrücklich außerhalb des Spiels.** Neue Datei, `uebung.py`, wird nicht committet — trag sie in `.gitignore` ein oder lösch sie danach.

Frag nach dem Geburtsjahr und gib das Alter aus.

Das ist alles. Vier Zeilen. Der Punkt ist nicht die Rechnung, sondern die eine Stelle, an der es hakt: `input()` liefert Text, und mit Text kann man nicht subtrahieren. Wenn du den `TypeError` siehst, bevor du ihn behebst, hat die Aufgabe funktioniert.

Wer eine Liste nur im eigenen Inventar bedienen kann, kann keine Listen — dasselbe gilt für Typumwandlung. Deshalb sind die Transferaufgaben in diesem Tutorial immer woanders.

---

## Kaputtmachen

Nummerierte Experimente. **Schreib bei jedem zuerst auf, was du erwartest**, dann führ es aus. Der Unterschied zwischen Erwartung und Ergebnis ist der eigentliche Lerngewinn; ohne die Notiz ist es nur Herumklicken.

1. **Lass bei einem f-String das `f` weg.** Was steht auf dem Bildschirm? Stürzt es ab?
2. **Lass ein Anführungszeichen weg.** Lies die Fehlermeldung. Zeigt sie auf die richtige Zeile?
3. **Benutze eine Variable, bevor du sie anlegst** — schreib die `print`-Zeile über die Zuweisung. Welcher Fehler kommt?
4. **Vertipp dich absichtlich bei einem Variablennamen** in der Ausgabe (`kern_integritat`). Was ist das für ein Fehler, und woran hättest du ihn ohne Absturz erkannt?
5. **Rechne mit `input()`, ohne umzuwandeln.** Frag nach einer Zahl und multiplizier sie mit 3. Bei Eingabe `7`: Was kommt heraus?
6. **Gib bei der Klassenwahl `zwei` ein.** Welche Fehlerart? Welche Zeile?
7. **Gib bei der Klassenwahl `9` ein.** Und jetzt der wichtige Teil: **Es stürzt nicht ab.** Dein Programm läuft durch und behauptet, du spielst eine Klasse, die es nicht gibt.

8. **Setz `print(type(...))` an fünf verschiedene Stellen** — hinter `input()`, hinter `int()`, bei einer Lagevariable, bei einem f-String-Ergebnis, bei `letzte_meldung`. Sag **vorher** bei jeder Stelle, was herauskommen wird. Wie viele hast du richtig geraten?

**Experiment 5 und 7 sind die eigentlichen.** Beide laufen fehlerfrei durch und liefern Unsinn — bei 5 steht `777` statt `21`, bei 7 spielst du eine Klasse, die nicht existiert. Das ist der **Fehler vom Typ 3**, und er ist der gefährlichste, weil er die schädlichste Anfängerüberzeugung bestätigt: *„Wenn Python nicht meckert, stimmt mein Programm."* Das ist falsch, und je früher du es körperlich spürst, desto besser. Notier beide in `GELERNT.md`.

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `TypeError: can only concatenate str (not "int") to str` | Text und Zahl mit `+` verbunden | Die genannte Zeile — meist fehlt ein f-String oder ein `str()` |
| `ValueError: invalid literal for int() with base 10: 'zwei'` | `int()` auf etwas, das keine Zahl ist | Die `int(input(...))`-Zeile; heute noch erwartet |
| `NameError: name 'kern_integritat' is not defined` | Tippfehler im Namen, oder Variable erst später angelegt | Namen buchstabenweise vergleichen |
| `SyntaxError: unterminated string literal` | Fehlendes Anführungszeichen | Genannte Zeile **und die darüber** |
| `{kunde}` erscheint wörtlich in der Ausgabe | `f` vergessen | Die betroffene `print`-Zeile |
| Die Ausgabe ist eingerückt, obwohl sie es nicht sein soll | Einrückung im dreifachen String | Der `"""`-Block |
| Zahl ändert sich im Code, aber nicht in der Ausgabe | Die Zahl steht wörtlich im Text statt in `{}` | Alle `print`-Zeilen durchgehen |
| `IndentationError: unexpected indent` | Führendes Leerzeichen vor einer Zeile | Genannte Zeile ganz nach links |
| Der ASCII-Kopf ist nach rechts verschoben oder ausgefranst | Einrückung innerhalb des dreifachen Strings | Alle Zeilen im `"""`-Block ganz nach links |
| `type(x)` gibt nichts aus | `print()` fehlt drumherum — `type()` liefert nur | Die Zeile: `print(type(x))` |

**Dein Debugging-Reflex für diese Etappe** — die eine Frage, die hier am schnellsten zum Ziel führt:

> **Welchen Typ hat dieser Wert gerade wirklich?**

Nicht raten. Nachsehen: `print(type(antwort))` an die fragliche Stelle. Fast jeder Fehler dieser Etappe ist ein Typfehler in Verkleidung — und diese eine Zeile beantwortet ihn in fünf Sekunden. Merk dir den Reflex; er trägt bis Etappe 25, wenn Daten aus JSON-Dateien kommen und plötzlich Text sind, wo du Zahlen erwartet hast.

---

## Ein Blick nach vorne

**Etappe 2** gibt deiner Klassenwahl Folgen. Die Zahl, die heute nur bestätigt wird, bestimmt dort Panzerung, Schaden und Trefferpunkte — und du lernst `if`, das Werkzeug, das dir heute an drei Stellen gefehlt hat.

**Etappe 3** macht aus dem Skript ein Spiel. `wellen_bis_evakuierung` wird zu `range(1, 21)`, `kern_integritaet` zur Abbruchbedingung. Ab dort wartet dein Programm auf dich, statt einmal durchzulaufen.

**Etappe 12** ist der Punkt, an dem sich das heutige Prinzip auszahlt oder rächt. Der Tick verändert bei jedem Spielerbefehl den Weltzustand. Alles, was du heute nur gedruckt hast, musst du dort nachrüsten.

**Etappe 17** zitiert `letzte_meldung`. Das ist ungefähr vier Monate entfernt.

Und **Etappe 29** zeichnet deinen ASCII-Kopf als Kulisse. Die Skizze von heute ist die erste Zeile dieses Fadens.

---

## Abschluss

**In `GELERNT.md`** — zwei bis vier Sätze, immer inklusive der Design-Entscheidungen:

- Was neu war: Variablen als Namen, die auf Werte zeigen; f-Strings; `input()` gibt immer Text
- Was gehakt hat (ehrlich, mit der Fehlermeldung)
- **Entscheidung 1:** Sprache der Variablennamen — welche, und warum
- **Entscheidung 2:** Klasse als Zahl oder als Name — welche, und warum
- Der Wortlaut von `letzte_meldung` (du brauchst ihn in Etappe 17)
- Die beiden Typ-3-Fehler aus dem Kaputtmachen
- Der Reflex `print(type(x))` — notier ihn ausdrücklich, du brauchst ihn spätestens in Etappe 4

**Dann committen:**

```
git add .
git commit -m "Etappe 1: Der Abwurf"
git push
```

Das ist dein zweiter Commit. In vier Monaten steht hier eine Liste, die länger ist als jedes Zertifikat.

---

## Wenn du mehr willst

Erst bei grünem Selbsttest. Alles hier ist optional und darf weggelassen werden.

- **Mehr Sinnesvariablen.** Neben `letzte_meldung` noch Temperatur in der Kuppel, ein Geräusch von draußen, der Stand der Notbeleuchtung. Alles Variablen, alle heute ungenutzt — Etappe 17 nimmt sie dankend.
- **Die Zeit seit dem letzten Kontakt** als Variable in Tagen, eingesetzt per f-String. Kostet eine Zeile und macht die Durchsage deutlich unangenehmer.
- **Rechne im f-String.** Zeig die Munition zusätzlich als „reicht für ungefähr N Wellen", ausgerechnet direkt in den geschweiften Klammern. Erste Berührung damit, dass in `{}` mehr stehen darf als ein Name.
- **Formatier eine Zahl.** `f"{anteil:.0%}"` macht aus `0.72` die Ausgabe `72%`. Du brauchst das in Etappe 3 für die Balken — heute ist es ein Vorgeschmack, kein Pflichtstoff.
- **Schreib den Funkspruch zweimal.** Einmal beim Start als automatische Durchsage, einmal als Antwort auf den Ruf des Spielers — mit derselben Variable. Dass zweimal exakt dasselbe kommt, ist die ganze Aussage. **Das ist die beste Erweiterung dieser Liste**, weil sie nichts kostet und erzählerisch mehr trägt als jeder Absatz, den du schreiben könntest.

---

> **Nächste Etappe:** [Etappe 2 — Der erste Kontakt](etappe-02-der-erste-kontakt.md) · `if` / `elif` / `else`, Vergleiche, Booleans, `and` / `or` / `not`
