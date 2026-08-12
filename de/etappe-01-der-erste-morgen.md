# Etappe 1 — Der erste Morgen

> **Block 1: Fundament** · Etappe 1 von 29 · [← Lehrplan](../RPG_Lehrplan.md) · [Etappe 2 →](etappe-02-die-erste-begegnung.md)

**Boot.dev:** Variablen, Strings, f-Strings, `print()`, `input()`
**Zeitaufwand:** 2–4 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 0 (Repo steht, virtuelle Umgebung läuft)

---

## Worum es geht

Am Ende dieser Etappe existiert dein Spiel. Es ist noch keine Schleife, kein Inventar, keine Entscheidung — es läuft einmal von oben nach unten durch und ist dann fertig. Das ist in Ordnung. Wichtig ist: Ab heute gibt es eine Datei, die du jeden Tag ein Stück größer machst.

Inhaltlich baust du den Morgen, an dem das Dorf leer ist. Der Spieler wacht auf, nimmt seine Umgebung wahr, ruft — und bekommt keine Antwort.

**Ehrlich eingeordnet:** Als Programmier-Übung ist das dünn. Es sind ein paar Variablen und ein paar Ausgaben. Der eigentliche Wert liegt woanders: Du gewöhnst dir von der ersten Zeile an eine Denkweise an, die die meisten Anfänger nie entwickeln — **Weltzustand wird gespeichert, nicht nur ausgegeben.**

Der Unterschied sieht so aus:

```python
# Die Gewohnheit, die du NICHT willst:
print("Es riecht nach frischem Brot.")

# Die Gewohnheit, die du willst:
geruch = "frischem Brot"
print(f"Es riecht nach {geruch}.")
```

Beide Zeilen erzeugen dieselbe Ausgabe. Aber in der zweiten Fassung *weiß dein Programm noch*, wonach es gerochen hat. In Etappe 17 wirst du darauf zurückgreifen, wenn der zweite Bewohner verschwindet:

> *„Du erinnerst dich an den Geruch von Brot an diesem ersten Morgen. Jetzt riecht es nach kaltem Rauch."*

Diese Rückblende ist nur möglich, weil du heute eine Variable angelegt hast statt einen Satz auszugeben. Merk dir das Muster — es ist die halbe Miete für alles, was noch kommt.

---

## Die Konzepte

### 1. Variablen

Eine Variable ist ein **Name, der auf einen Wert zeigt**.

```python
kaffeesorte = "Espresso"
tassen = 3
```

Die meisten Einführungen erklären das mit einem Kasten: „Eine Variable ist ein Behälter, in dem ein Wert liegt." Das ist bequem, aber ungenau — und die Ungenauigkeit fällt dir in Etappe 4 auf die Füße, wenn du dich fragst, warum das Ändern einer Liste plötzlich zwei Variablen betrifft.

Die genauere Vorstellung: **Der Wert existiert irgendwo im Speicher, und der Name ist ein Schild, das darauf zeigt.** Zwei Namen können auf denselben Wert zeigen. Merk dir diese Formulierung, auch wenn sie heute noch keinen Unterschied macht.

**Das `=` ist keine Gleichheit.** Es ist eine Zuweisung. Lies `tassen = 3` nicht als „tassen gleich 3", sondern als **„tassen bekommt den Wert 3"**. Diese Lesegewohnheit erspart dir in Etappe 2 Verwirrung, wenn `==` dazukommt.

**Namensregeln:** Buchstaben, Ziffern und Unterstriche; keine Ziffer am Anfang; keine Leerzeichen. Python-Konvention ist `kleinbuchstaben_mit_unterstrich` (snake_case), nicht `kleinBuchstabenMitHöckern`.

**Eine Entscheidung, die du jetzt treffen solltest:** Deutsche oder englische Variablennamen? Die Python-Welt schreibt englisch, aber dein Spiel ist deutsch, und für ein Lernprojekt ist Deutsch völlig legitim. Was nicht funktioniert, ist Mischmasch — `player_name` neben `tageszeit` neben `hasKey`. Entscheide dich jetzt und zieh es durch. Umbenennen ist später lästig.

### 2. Datentypen

Jeder Wert in Python hat einen Typ. Für heute reichen vier:

| Typ | Was es ist | Beispiel |
|---|---|---|
| `str` | Text (*string*) | `"Espresso"` |
| `int` | Ganzzahl | `3` |
| `float` | Kommazahl | `2.5` |
| `bool` | Wahrheitswert | `True` / `False` |

**Der wichtigste Unterschied für heute:** `"12"` und `12` sind nicht dasselbe. Das erste ist Text, der zufällig aus Ziffern besteht. Das zweite ist eine Zahl.

```python
"12" + "12"    # ergibt "1212"  — Texte werden aneinandergehängt
12 + 12        # ergibt 24      — Zahlen werden addiert
```

**Dein Werkzeug zum Nachschauen:** `type()` sagt dir, womit du es zu tun hast.

```python
print(type(tassen))
```

Benutz das heute mindestens dreimal. Nicht weil du es im fertigen Spiel brauchst, sondern weil es die Frage „was ist das eigentlich gerade?" zur Gewohnheit macht — und diese Frage wird dir noch hunderte Male Zeit sparen.

### 3. `print()`

Gibt etwas auf dem Bildschirm aus. Mehrere Werte werden durch Komma getrennt und mit Leerzeichen verbunden:

```python
print("Tassen heute:", tassen)
```

`print()` ohne Argumente erzeugt eine Leerzeile. Das ist dein wichtigstes Gestaltungsmittel in einem Textspiel — Absätze sind Rhythmus.

### 4. f-Strings

Text und Variablen zusammenbringen kannst du auf mehrere Arten. Die moderne und lesbare ist der **f-String**: ein `f` direkt vor dem öffnenden Anführungszeichen, Variablen in geschweiften Klammern.

```python
name = "Kolja"
alter = 34
print(f"{name} ist {alter} Jahre alt.")
```

Ohne das `f` passiert etwas, das du einmal gesehen haben solltest:

```python
print("{name} ist {alter} Jahre alt.")
# Ausgabe: {name} ist {alter} Jahre alt.
```

Python interessiert sich dann nicht für die Klammern — es sind einfach Zeichen im Text. Genau das ist übrigens ein Fehler vom Typ 3 aus der Bug-Jagd: kein Absturz, keine Fehlermeldung, einfach das Falsche.

In den Klammern darf auch gerechnet werden:

```python
print(f"Morgen sind es {tassen + 1} Tassen.")
```

**Die Alternative, die du kennen, aber nicht benutzen solltest:**

```python
print(name + " ist " + str(alter) + " Jahre alt.")
```

Das funktioniert, ist aber schwerer zu lesen, und du musst Zahlen von Hand in Text umwandeln. Du wirst diese Schreibweise in älterem Code sehen — deshalb solltest du sie erkennen. Schreiben tust du f-Strings.

### 5. `input()`

Hält das Programm an und wartet auf eine Eingabe. Der Text in den Klammern wird vorher angezeigt:

```python
antwort = input("Wie heißt du? ")
```

**Und jetzt die wichtigste Einzelheit dieser gesamten Etappe:**

> **`input()` gibt IMMER einen String zurück. Immer. Auch wenn der Benutzer eine Zahl eintippt.**

Das ist der häufigste Anfängerfehler in Python, und du wirst ihn heute in der Transferaufgabe selbst produzieren. Das ist Absicht.

### 6. Typumwandlung

Wenn du mit einer Eingabe rechnen willst, musst du sie umwandeln:

```python
eingabe = input("Wie viele Tassen? ")   # "3" — ein String
zahl = int(eingabe)                      # 3   — eine Zahl
```

`int()` macht aus Text eine Ganzzahl, `float()` eine Kommazahl, `str()` aus allem Text.

`int("3")` funktioniert. `int("drei")` stürzt ab mit einem `ValueError`. Damit wirst du dich in Etappe 20 richtig beschäftigen — heute reicht es zu wissen, dass es passieren kann.

### 7. Kommentare

Alles hinter `#` ignoriert Python:

```python
# Der Geruch wird in Etappe 17 nochmal gebraucht
geruch = "frischem Brot"
```

Kommentiere **warum**, nicht **was**. `# setzt geruch auf frischem Brot` ist wertlos — das steht da schon.

---

## Dein Auftrag

Bau das in dieser Reihenfolge. Nach jedem Schritt einmal ausführen. Nicht alles auf einmal schreiben und dann hoffen.

**Schritt 1 — Die Datei existiert**
Leg `spiel.py` im Repo an. Ein einziges `print()` mit irgendeinem Text. Ausführen (`python spiel.py` im Terminal oder der Run-Button in VS Code). Wenn Text erscheint, funktioniert deine gesamte Werkzeugkette. Das ist mehr wert, als es aussieht.

**Schritt 2 — Der Weltzustand**
Leg mindestens vier Variablen an: Tageszeit, Wetter, Geruch, Dorfname. Gib sie noch nicht aus — definier sie erstmal nur. Sie stehen gesammelt am Anfang der Datei.

Setz einen Kommentar darüber, dass diese Werte später wieder gebraucht werden.

**Schritt 3 — Der Spieler bekommt einen Namen**
Frag nach dem Namen und speichere ihn in einer Variable. Prüf mit `type()`, was du bekommen hast.

**Schritt 4 — Der Morgen**
Beschreib den Morgen in mehreren `print()`-Zeilen. Mindestens drei davon müssen f-Strings sein, die deine Variablen aus Schritt 2 benutzen.

Und hier schreibst du als Autor, nicht als Programmierer: **Du darfst nirgends hinschreiben, dass das Dorf leer ist.** Zeig es. Kalte Herdstelle, offene Tür, ein Frühstück, das jemand nicht zu Ende gegessen hat. Der Leser soll es begreifen, bevor du es sagst.

**Schritt 5 — Der Ruf**
Der Spieler ruft. Niemand antwortet. Nutz Leerzeilen, um die Stille hörbar zu machen — `print()` ohne Argumente.

Das ist das Ende von Etappe 1. Das Programm läuft durch und beendet sich.

---

## Was NICHT in diese Etappe gehört

Der Reiz wird groß sein, sofort weiterzubauen. Widersteh ihm — jedes dieser Dinge hat seine eigene Etappe, und du baust es dann mit dem passenden Werkzeug statt mit Krücken:

- ❌ Abfragen mit `if` → Etappe 2
- ❌ Eine Schleife, die auf Befehle wartet → Etappe 3
- ❌ Ein Inventar → Etappe 4
- ❌ Mehrere Orte → Etappe 5
- ❌ Funktionen → Etappe 7

Wenn dir Ideen kommen: `GELERNT.md` hat unten Platz für eine Ideenliste. Aufschreiben, weiterarbeiten.

---

## Selbsttest

Bevor du committest — läuft alles davon?

- [ ] `python spiel.py` läuft ohne Fehlermeldung durch
- [ ] Das Programm fragt nach dem Namen und wartet
- [ ] Der eingegebene Name taucht später im Text auf
- [ ] Mindestens vier Variablen für Weltzustand sind definiert
- [ ] Mindestens drei f-Strings sind im Einsatz
- [ ] Kein einziger String wird mit `+` zusammengeklebt
- [ ] Nirgends steht wörtlich, dass das Dorf leer ist — der Text zeigt es
- [ ] Du hast `type()` mindestens dreimal benutzt und wieder entfernt
- [ ] Mindestens ein Kommentar erklärt ein *Warum*

---

## Lernziele

Diese Fragen musst du **ohne Nachschlagen und in eigenen Worten** beantworten können. Nicht auswendig — erklärt.

1. **Was ist der Unterschied zwischen einer Variable und ihrem Wert?**
2. **Was genau macht das `f` vor dem Anführungszeichen?** Und was passiert ohne?
3. **Warum ist `alter = "12"` etwas anderes als `alter = 12`?** Nenn eine Operation, die bei einem funktioniert und beim anderen etwas anderes tut.
4. **Was gibt `input()` zurück — und in welchem Datentyp?** Auch wenn der Benutzer `42` eintippt?
5. **Warum legen wir `geruch` als Variable an, statt den Satz direkt auszugeben?**

Wenn du bei einer Frage ins Stocken gerätst, ist das kein Versagen — das ist genau der Zweck der Liste. Schreib die Frage auf, probier sie im Code aus, frag mich.

---

## Transferaufgabe (5–10 Minuten)

**Neue Datei, außerhalb des Spiels.** Nenn sie `uebung_01.py` oder wirf sie danach weg — sie gehört nicht ins Spiel.

> Frag nach dem Geburtsjahr und gib das ungefähre Alter aus.

Der ganze Zweck steckt in einem einzigen Punkt: Was musst du mit dem Rückgabewert von `input()` tun, bevor du damit rechnen kannst?

**Mach es absichtlich zuerst falsch.** Rechne direkt mit dem, was `input()` liefert. Lies die Fehlermeldung. Erst dann repariere es.

Warum das wichtig ist: Du sollst diesen Fehler nicht vermeiden, sondern **wiedererkennen**. In vier Wochen wirst du ihn nochmal machen, und dann brauchst du keine zehn Minuten, sondern zehn Sekunden.

---

## Kaputtmachen

Dein Spiel läuft. Jetzt zerstör es gezielt und schau zu. Nach jedem Experiment: rückgängig machen.

**Experiment 1 — Das `f` weglassen**
Entferne bei einem f-String das `f`. Was wird ausgegeben? Warum gibt es keine Fehlermeldung? Was sagt dir das über Fehler, die nicht abstürzen?

**Experiment 2 — Ein Tippfehler im Namen**
Schreib in einem f-String `{gerch}` statt `{geruch}`. Welche Fehlermeldung kommt? Was bedeutet sie wörtlich?

**Experiment 3 — Die Reihenfolge umdrehen**
Verschieb eine Variablendefinition ans Ende der Datei, nachdem sie schon benutzt wurde. Was passiert? Was lernst du daraus darüber, wie Python eine Datei liest?

**Experiment 4 — Rechnen mit Text**
`print(spielername + 1)`. Lies die Fehlermeldung ganz. Sie sagt dir sehr genau, was schiefgelaufen ist — Fehlermeldungen sind Hilfe, keine Beschimpfung.

**Experiment 5 — Ein Anführungszeichen entfernen**
Lösch bei einem String das schließende Anführungszeichen. `SyntaxError`. Zeigt Python auf die richtige Zeile? (Oft auf die *nächste* — auch das ist eine Lektion.)

---

## Häufige Stolpersteine

| Fehlermeldung | Was sie bedeutet | Wo du suchst |
|---|---|---|
| `NameError: name 'x' is not defined` | Der Name existiert nicht | Tippfehler, oder du benutzt ihn vor der Definition |
| `SyntaxError: unterminated string literal` | Ein Anführungszeichen fehlt | Die genannte Zeile — oder die davor |
| `TypeError: can only concatenate str (not "int") to str` | Text und Zahl mit `+` verbunden | f-String benutzen oder `str()` |
| `ValueError: invalid literal for int()` | `int()` bekam etwas, das keine Zahl ist | Was hat der Benutzer wirklich eingetippt? |
| Klammern erscheinen im Text | Das `f` fehlt | Der betroffene String |

**Wie man eine Fehlermeldung liest:** Von unten nach oben. Die letzte Zeile sagt, *was* schiefging. Die Zeile darüber sagt, *wo*. Alles davor ist der Weg dorthin. Das ist heute noch trivial, weil deine Datei kurz ist — aber die Gewohnheit legst du jetzt an.

---

## Abschluss

**`GELERNT.md` — zwei bis drei Sätze:**
Was war neu? Wo hast du am längsten gehangen? Was hat dich überrascht?

Schreib das ehrlich, auch wenn es banal wirkt. In Woche 12 liest du diesen Eintrag und siehst schwarz auf weiß, wie weit du gekommen bist. An Tagen ohne Motivation ist diese Datei das Beste, was du hast.

**Commit:**
```bash
git add .
git commit -m "Etappe 1: Der erste Morgen"
git push
```

---

## Wenn du mehr willst

Optional. Erst, wenn der Selbsttest komplett grün ist.

**Dramaturgische Pausen.** Text, der auf einmal erscheint, hat keinen Rhythmus. Mit dem `time`-Modul kannst du Pausen einbauen. Du brauchst dafür `import` — das ist neu und steht nicht im Lehrplan. Genau deshalb ist es eine gute Übung im Nachschlagen. Such nach „python time sleep" und bau es ein.

**Mehr Sinne.** Nicht nur Geruch — Geräusch, Temperatur, Licht. Jede zusätzliche Variable ist Material für spätere Rückblenden. Was du heute speicherst, kannst du in Etappe 17 gegen den Spieler verwenden.

**Der Name des Dorfes.** Soll der Spieler ihn eingeben können? Das wäre ein zweites `input()` und kostet dich zwei Minuten. Überleg, ob es dem Spiel guttut — ein Dorf, das der Spieler benannt hat, verliert man ungern.

---

> **Nächste Etappe:** [Etappe 2 — Die erste Begegnung](etappe-02-die-erste-begegnung.md) · `if` / `elif` / `else`, Booleans, `and` / `or` / `not`
