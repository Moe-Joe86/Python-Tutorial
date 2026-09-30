# Das Syntaxregister — welches Werkzeug ab wann zur Verfügung steht

*v1.28.0 · 2026-09-30*

> Verbindlicher Anhang zum [Lehrplan](Vorposten_Lehrplan.md). Diese Datei ist die einzige Quelle der Wahrheit darüber, was ein Lernender an einem bestimmten Punkt kennt.

---

## Wozu es diese Datei gibt

Dieses Tutorial setzt keine zweite Lernquelle voraus. Kein Kurs, kein Buch, keine Plattform. Wer Terminal und Editor bedienen kann, muss allein durchkommen.

Diese Zusage hat eine harte Folge: **Jedes Zeichen, jedes Schlüsselwort und jeder Aufruf, den eine Aufgabe braucht, muss vorher erklärt worden sein.** Nicht erwähnt — erklärt, mit Syntax und Beispiel.

Das klingt selbstverständlich und ist der Punkt, an dem Tutorials reihenweise scheitern. Nicht bei den großen Themen — Listen, Schleifen und Klassen bekommt jeder unter. Es scheitert am Kleinen: `+=` ist zu unscheinbar für einen eigenen Abschnitt und zu neu, um vorausgesetzt zu werden. Genau solche Zeichen fallen durch, und der Lernende sitzt vor einer Aufgabe, die er mit dem Gezeigten nicht lösen kann.

Diese Datei ist die Buchführung dagegen. Sie hat drei Adressaten:

**Den Lernenden.** Wenn ein Auftragsschritt ein Werkzeug verlangt, das hier nicht steht, ist das kein Wissenslücke — es ist ein Fehler im Guide. Melde ihn.

**Den Mentor.** Bevor eine KI erklärt oder Hinweise gibt, schlägt sie hier nach. Was hier steht, darf sie voraussetzen. Was nicht hier steht, erklärt sie direkt statt sokratisch — man kann nichts herleiten, das man nie gesehen hat.

**Den Autor.** Vor jeder neuen Etappe: Auftragsschritte selbst lösen, benötigte Werkzeuge auflisten, gegen dieses Register prüfen. Was fehlt, wird entweder erklärt oder die Aufgabe wird umgebaut.

**Regel:** Wer ein Werkzeug in einer Etappe einführt, trägt es hier ein. Ohne Ausnahme. Ein Werkzeug, das nicht im Register steht, existiert für den Lernenden nicht.

---

## Wie man die Tabellen liest

**Spalte „Konzept"** nennt den nummerierten Abschnitt des Etappen-Guides, in dem das Werkzeug erklärt wird. Steht dort `⚠️`, ist das Werkzeug in dieser Etappe **nötig, aber nicht erklärt** — eine offene Lücke. Die Sammelliste dazu steht am Ende.

**Spalte „Stufe"** trägt dieselbe Bedeutung wie in den Guides:

| | Heißt |
|---|---|
| 🔨 | Der Lernende baut damit. Aufgaben dürfen es verlangen. |
| 🧠 | Er versteht das Verhalten, ohne es aktiv einzusetzen. |
| 👀 | Er erkennt es in fremdem Code und kann es in einem Satz erklären. **Keine Aufgabe darf es verlangen.** |

---

## Etappe 0 — Das Repo

Kein Python. Terminal, Git, virtuelle Umgebung, `pip`. Steht im Lehrplan, nicht hier.

---

## Etappe 1 — Der Abwurf

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `#` — Kommentar | 10 | 🔨 |
| `=` — Zuweisung | 2 | 🔨 |
| Die Typen `str`, `int`, `float`, `bool` | 3 | 🔨 |
| `type()` | 3 | 🔨 |
| `'...'` und `"..."` | 4 | 🔨 |
| `"""..."""` — mehrzeiliger String | 4 | 🔨 |
| `+` — Strings aneinanderhängen | 3 | 🔨 |
| `f"...{name}..."` — f-String | 5 | 🔨 |
| Ausdruck in `{}` (`{offen * 2}`) | 5 | 🔨 |
| `print()` | 6 | 🔨 |
| `input()` | 7 | 🔨 |
| `int()`, `float()`, `str()` — Umwandlung | 8 | 🔨 |
| Traceback von unten nach oben lesen | 12 | 🧠 |
| Grundrechenarten `+` `-` `*` an Zahlen, Punkt vor Strich | 3b | 🔨 |
| Rechnen ohne Zuweisung ändert nichts | 3b | 🧠 |
| `trefferpunkte` als zweiter Gesundheitswert neben `kern_integritaet` | Auftrag 3 | 🔨 |
| GROSS geschriebene Namen für feste Werte (Verabredung, keine Sprachregel) | 10 | 🧠 |

---

## Etappe 2 — Der erste Kontakt

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `if`, Doppelpunkt, Einrückung als Bedeutung | 1 | 🔨 |
| `==` | 2 | 🔨 |
| `!=` `<` `>` `<=` `>=` | 3 | 🔨 |
| `elif` | 4 | 🔨 |
| `else` | 5 | 🔨 |
| `True` / `False` | 6 | 🔨 |
| Vergleichsergebnis in einer Variablen speichern | 6 | 🔨 |
| `and` `or` `not` | 7 | 🔨 |
| Klammern in verknüpften Bedingungen | 8 | 🔨 |
| Truthy / Falsy, besonders `0` | 9 | 🧠 |
| `.strip()` | 10 | 🔨 |
| Punkt-Schreibweise `wert.methode()` | 10 | 👀 |
| `print()`-Marker zur Zweigverfolgung | 12 | 🔨 |
| `and` / `or` geben Werte zurück, nicht `True`/`False` — **in 18b als Lesestoff wiederholt** (Etappe 18, Konzept 12), bleibt 👀 | 7 | 👀 |

---

## Etappe 3 — Die Wellenschleife

### 3a — Die Schleife

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `while` | 1 | 🔨 |
| `+=` `-=` `*=` | 1b | 🔨 |
| `NameError`, wenn der Zähler vor der Schleife fehlt | 1b | 🧠 |
| `+=` bei Strings hängt an, statt zu addieren | 1b | 🧠 |
| `for x in range(...)` | 2 | 🔨 |
| `range(a)`, `range(a, b)`, `range(a, b, c)` | 2 | 🔨 |
| Verschachtelte Schleifen, zwei Einrückungsebenen | 4 | 🔨 |
| `break` | 6 | 🔨 |
| `continue` | 7 | 👀 |
| `_` als Wegwerfname | 7 | 👀 |
| `Strg + C` als Notausgang | 1 | 🔨 |

### 3b — Die Befehle

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `.lower()` | 8 | 🔨 |
| Zustandsvariable als Schleifenbedingung (`while laeuft:`) | 11 | 🔨 |
| `while True:` mit `break` | **6b (3a)** | 🔨 |

### 3c — Kampf und Anzeige

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `"#" * 7` — Text mal Zahl | 14 | 🔨 |
| `erfahrung` als Zähler ohne Wirkung | Auftrag 15b | 🔨 |
| `/` — Division | 13b | 🔨 |
| `f"{anteil:.0%}"` — Formatangabe im f-String | 14 | 👀 |
| `round()` gegen `int()` | 13b | 🔨 |
| `//` Ganzzahldivision | 13b | 🔨 |
| `%` Modulo (heute ungebraucht, neben `//` eingeführt) | 13b | 🧠 |
| `/` liefert immer eine Kommazahl | 13b | 🧠 |

---

## Etappe 4 — Ausrüstung und Beute

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `[...]` und `[]` — Liste | 1 | 🔨 |
| `liste[0]` — Index lesen | 3 | 🔨 |
| `range(len(liste))` | 3 | 🔨 |
| `liste[-1]`, `liste[-2]` | 4 | 🔨 |
| `len()` | 4 | 🔨 |
| `IndexError` | 4 | 🧠 |
| `.append()` und dass es `None` zurückgibt | 5 | 🔨 |
| `.remove()` und `ValueError` | 6 | 🔨 |
| `in` bei einer Liste | 7 | 🔨 |
| `for ding in liste` | 8 | 🔨 |
| Zuweisung an die Schleifenvariable ändert die Liste nicht | 8 | 🧠 |
| Slicing `liste[a:b]` | 8b | 👀 |
| `b = a` — zwei Namen, ein Objekt | 9 | 🧠 |
| `.copy()` | 9 | 🔨 |
| `if liste:` — leere Liste ist falsy | 11 | 🔨 |
| `.split()` | 12 | 🔨 |
| Methodenkette `.strip().lower().split()` | 12 | 🔨 |
| `["."] * 8` — Liste mal Zahl | 14 (knapp, als Selbstversuch) | 🔨 |
| `for k, v in d.items()` | 8 (Vorschau, gehört zu 5) | 👀 |
| `for i, x in enumerate(...)` | 8 (Vorschau, gehört zu 14a) | 👀 |
| `liste[i] = wert` — Index schreiben | **3b** | 🔨 |
| `for i in range(len(...))` mit Zuweisung — alle Einträge ändern | **3b** | 🔨 |
| Ersetzen ändert die Länge der Liste nicht | **3b** | 🧠 |

| `", ".join(liste)` — Trennzeichen ruft auf, Liste in die Klammern | 14 | 🔨 |
| `AttributeError` bei vertauschter Reihenfolge | 14 | 🧠 |
| `print(dir(x))` und `help(x.methode)` — Ausgabe lesen, Dunder überspringen | Vorspann | 🔨 |
| `BAHNLAENGE` als fester Wert, GROSS geschrieben — der erste im eigenen Code | Auftrag 9 | 🔨 |
| *(Kür)* `import random` — nur als Gebrauchsanweisung, erklärt wird er in **24**. **Ab 17a im Auftrag** (Etappe 17, Konzept 1) | Kür | 🔨 |
| *(Kür)* `random.choice(liste)` — ein zufälliger Eintrag, **gleichverteilt**. **Ab 17a im Auftrag** (Etappe 17, Konzept 2) | Kür | 🔨 |
| ⚠️ Gewichte (`random.choices` mit `weights=`) gehören **nicht** hierher — Zahltag ist **17a** | — | ⛔ |

---

## Etappe 5 — Der Vorposten und das Depot

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `{"schluessel": wert}` — Dictionary | 1 | 🔨 |
| `d["schluessel"]` — lesen | 2 | 🔨 |
| `d["schluessel"] = wert` — anlegen und überschreiben | 2 | 🔨 |
| `KeyError` | 2 | 🧠 |
| `.get(key)` und `.get(key, ersatz)` | 3 | 🔨 |
| `.get(kennung, kennung)` — Rückfall auf den Schlüssel selbst | 9, Auftrag 7b | 🔨 |
| `in` prüft beim Dictionary den Schlüssel | 4 | 🔨 |
| `in d.values()` | 4 | 👀 |
| `d[a][b]` — verschachtelter Zugriff | 5 | 🔨 |
| `f"{d['schluessel']}"` — Zugriff im f-String, innen die andere Anführungssorte | 2b | 🔨 |
| Gleiche Anführungszeichen innen wie außen sind erst ab Python 3.12 erlaubt | 2b | 🧠 |
| `python3 --version` | 2b | 🔨 |
| `for name in d` — läuft über die Schlüssel | 6 | 🔨 |
| `.items()` | 6 | 🔨 |
| `.keys()` und `.values()` | 6 | 👀 |
| `del d[key]` | 6 (als Gegenbeispiel gezeigt), **hochgestuft in 13** (Konzept 10) | 🔨 |
| `RuntimeError` beim Ändern der Größe während der Iteration | 6 | 🧠 |
| Schlüssel müssen hashbar sein, `TypeError: unhashable type` | 7 | 👀 |
| `d[key] -= n` | 10 | 🔨 |
| Zahlen als Schlüssel (`{1: "…", 2: "…"}`) — kein Index | 15 | 🔨 |

---

## Etappe 6 — Liste, Dictionary, Set, Tuple

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `{a, b, c}` — Set | 2 | 🔨 |
| `set()` — das leere Set, und warum nicht `{}` | 2 | 🔨 |
| `set([...])` — Set aus einer Liste | 2 | 🔨 |
| `.add()` | 3 | 🔨 |
| `.discard()` gegen `.remove()` beim Set | 3 | 🔨 |
| `in` beim Set | 6 | 🔨 |
| `(a, b)` — Tuple | 7 | 🔨 |
| `TypeError: 'tuple' object does not support item assignment` | 7 | 🧠 |
| `(5,)` — die Komma-Falle | 8 | 🔨 |
| Tuple-Unpacking `a, b = t` und `for a, b in ...` | 9 | 🔨 |
| `&` `\|` — Mengenoperationen | 10 | 👀 |
| `a - b` — Differenzmenge. **Hochgestuft in 18b** (Etappe 18, Konzept 10) | 10 | 👀 → 🔨 |
| Sets und Tuples lassen sich nicht als JSON speichern — **in 19a auf 🧠 hochgestuft** (Etappe 19, Konzept 5) | 14 | 👀 → 🧠 |
| `.index(wert)` — von einem Wert zu seiner Stelle | **0** | 🔨 |
| `ValueError: x is not in list` | **0** | 🧠 |
| `.pop(i)` — entfernt über die Stelle und gibt zurück | **0** | 🔨 |
| `del liste[i]` | **0** | 🔨 |
| `remove` / `pop` / `del` unterscheiden — und `.index()` als Brücke vom Wert zur Stelle | **0** | 🧠 |
| Eine Liste über den Index aufbauen (`i` als Positionsangabe) | **0** | 🔨 |

---

## Etappe 7 — Aufräumen

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `def name(parameter):` | 1 | 🔨 |
| Parameter gegen Argument | 2 | 🧠 |
| `return` | 3 | 🔨 |
| `return` beendet die Funktion sofort | 4 | 🧠 |
| Scope — lokal gegen global | 5 | 🧠 |
| `global` | 5 | 👀 |
| Standardargument `def f(x, y=0)` | 6 | 🔨 |
| Docstring als erster String im Funktionskörper | 9 | 🔨 |
| `return a, b` — zwei Werte zurückgeben | **5b** (in v1.5.0 aus 7b nach 7a verschoben) | 🔨 |
| `assert` — **in 20c auf 🔨 hochgestuft** (Etappe 20, Konzept 12) | 15 | 👀 → 🔨 |
| `UnboundLocalError` — Zuweisung im Körper macht den Namen im ganzen Körper lokal | 5 | 🧠 |
| Seiteneffekt gegen Rückgabewert | 5 | 🧠 |
| `cd` und `ls` (Windows: `dir`) — das Terminal muss im Projektordner stehen | 11 | 🔨 |
| `python: can't open file '...'` ist ein **Ortsfehler**, kein Python-Fehler | 11 | 🧠 |
| `> datei` legt die Datei an und **überschreibt** sie vollständig; sie leitet **nur** normale Ausgaben um | 11 | 🧠 |
| **Wohin `def`-Zeilen gehören** — über das Hauptprogramm, weil `def` vor dem Aufruf gelaufen sein muss | 1 | 🔨 |
| `NameError`, wenn die `def`-Zeile unter dem Aufruf steht | 1 | 🧠 |
| **Mutable gegen immutable als Rückgabefrage** — was sich von innen ändert und was durch `return` heraus muss | 5b | 🧠 |
| `return a, b, c` und `a, b, c = f(...)` beim Aufruf — **Reihenfolge wird nicht geprüft** | 5b | 🔨 |
| `TypeError: cannot unpack non-sequence NoneType` — ein Zweig ohne `return` | 5b | 🧠 |
| Blockweises Aus- und Einrücken beim Verschieben in einen Funktionskörper | Auftrag 2 | 🔨 |
| Das Format von `befehle.txt` — eine Zeile pro `input()`, in der Reihenfolge der Fragen; leere Zeile = leere Eingabe | 11b | 🔨 |
| `EOFError: EOF when reading a line` — die Eingabedatei ist zu Ende; **erwartbar**, weil das Spiel keinen Befehl zum Beenden hat | 11b | 🧠 |
| Zwei Ausgabekanäle: Fehler landen **nicht** in der Ausgabedatei, `2>` leitet sie um — nur erkennen | 11b | 👀 |
| Umgeleitete Eingaben erscheinen nicht in der Ausgabedatei, und `input()`-Texte enden ohne Zeilenumbruch | 11b | 🧠 |
| `<` und `>` im Terminal — Eingabe und Ausgabe umleiten | 11 | 🔨 |

*(Konzept 14 benutzt `//` und `%` im Beispiel. Beide kommen aus Etappe 3c, Konzept 13b.)*

---

## Etappe 8 — Die Bug-Jagd I

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `f"{wert!r}"` — die `!r`-Form im f-String | 5 | 🔨 |
| `repr()` als Funktion | 5 | 👀 |
| `breakpoint()` — hält an und öffnet den Debugger | 6 | 🔨 |
| `p name` im Debugger — druckt, und zwar in der repr-Form | 6 | 🔨 |
| `n` `s` `r` `c` `l` `q` — die Debugger-Schrittbefehle | 6 | 🔨 |
| `if bedingung: breakpoint()` — der bedingte Breakpoint | 7 | 🔨 |
| Grafischer Debugger: *Step Over/Into/Out* = `n`/`s`/`r` | 6 | 👀 |

*(Diese Etappe führt keine Spielsyntax ein — alles hier sind Werkzeuge zur Fehlersuche. Das Traceback-Lesen steht bereits bei Etappe 1 auf 🧠 und wird hier nur aktiv geübt, deshalb kein neuer Eintrag. `git diff` und `git log --oneline` gehören in den Git-Faden des Bogens, nicht in dieses Register. Ausnahme ist `git checkout` in Etappe 16, weil dort ein Auftragsschritt ihn verlangt.)*

---

## Etappe 9 — Alles wird zum Objekt

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `class Name:` — der Bauplan | 2 | 🔨 |
| `def __init__(self, ...)` — richtet das neu erzeugte Objekt ein | 2 | 🔨 |
| `self` als erster Parameter jeder Methode | 3 | 🔨 |
| `self.attribut = wert` — Wert am Objekt festmachen | 2 | 🔨 |
| `objekt = Klasse(...)` — ein Objekt erzeugen | 2 | 🔨 |
| `objekt.attribut` lesen und schreiben | 6 | 🔨 |
| `def methode(self):` und `objekt.methode()` | 5 | 🔨 |
| `objekt.attribut["schluessel"]` — Punkt und Klammer hintereinander | 6 | 🔨 |
| `def __repr__(self)` — die Entwicklerdarstellung, mit `return` | 9 | 🔨 |
| `repr(objekt)` löst `__repr__` aus (aus Etappe 8, jetzt an eigenen Klassen) | 10 | 🔨 |
| `TypeError: … takes 0 positional arguments` — `self` vergessen | 4 | 🧠 |
| `AttributeError: object has no attribute` | 6 | 🧠 |
| Fehlendes `self.` erzeugt still eine lokale Variable — Typ 3 | 4 | 🧠 |
| `__str__` und der Rückfall von `print()` auf `__repr__` | 11 | 👀 |
| Dunder-Methoden als Begriff — Python löst sie über normale Syntax aus | 10 | 👀 |
| `RecursionError`, wenn `__repr__` sich selbst einsetzt | Kaputtmachen | 👀 |

*(`dir()` und `help()` stehen seit Etappe 4 auf 🔨 und werden hier nur an eigenen Klassen wiederholt — kein neuer Eintrag. Vererbung, `super()` und weitere Dunder gehören zu **11**.)*

---

## Etappe 10 — Komposition

| Werkzeug | Konzept | Stufe |
|---|---|---|
| Ein Objekt als Attribut eines anderen (`self.regal = Regal(3)`) | 2 | 🔨 |
| `objekt.inneres.attribut` — zwei Punkte hintereinander | 2 | 🔨 |
| `None` als bewusster Leerwert | 4 | 🔨 |
| `is None` und `is not None` | 4, 9 | 🔨 |
| Ein Dictionary mit festen Schlüsseln und `None` als Startwert (Slots) | 9 | 🔨 |
| Ein Tuple als Position (`self.position = (0, 0)`) — **ohne Bewegung** | 10 | 🔨 |
| `.copy()` als Schutz vor geteilten Objekten (aus Etappe 4) | 8 | 🔨 |
| `def __init__(self, x=None)` statt `=[]` — der veränderbare Standardwert | 7 | 🔨 |
| **Objektidentität: zwei Namen, ein Objekt** | 6 | 🧠 |
| `None` ≠ `0` — beide falsy, verschiedene Bedeutung | 4 | 🧠 |
| `__repr__` der inneren Klasse trägt die des äußeren Objekts | 11 | 🧠 |
| `a is b` als Nachweis, dass zwei Namen auf dasselbe Objekt zeigen | 5, 6 | 🔨 |
| `is` gegen `==` als Regel für Vergleiche — Ding gegen Wert | 5 | 👀 |
| Komposition („hat ein") als Begriff, gegen Vererbung („ist ein") | 1 | 👀 |
| `TypeError: 'tuple' object does not support item assignment` | Kaputtmachen | 👀 |

*(Vererbung, `super()` und Objekte statt Strings im Inventar gehören zu **11**. `@property` wird in **11** als 👀 gezeigt und nirgends gebaut.)*

---

## Etappe 11 — Vererbung

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `class Kind(Eltern):` — Vererbung | 6 | 🔨 |
| `super().__init__(...)` — als erste Zeile der `__init__` | 7 | 🔨 |
| `super().methode()` in einer überschriebenen Methode | 8 | 🔨 |
| Eine Methode überschreiben (gleicher Name in der Unterklasse) | 8 | 🔨 |
| Eine Schleife über gemischte Objekte, ein Methodenaufruf | 8 | 🔨 |
| `.remove(objekt)` an einer Liste von Objekten — entfernt genau dieses | 2 | 🔨 |
| `for obj in liste: obj.attribut -= 1` verändert die Objekte | 3 | 🔨 |
| Eine Klasse als Wert: ein Dictionary Eingabe/Kennung → Klasse, Aufruf aus dem Dictionary, statt einer `if`/`elif`-Kette | 11b | 🔨 |
| Begriffe: Ober-/Basis-/Elternklasse, Unter-/abgeleitete/Kindklasse | 6 | 🧠 |
| `AttributeError` bei fehlendem `super().__init__()` — Absturzstelle ≠ Fehlerstelle | 7 | 🧠 |
| ⚠️ Methode ohne Klammern im `if` ist **immer wahr** — stiller Typ 3 | 14 | 🧠 |
| `type(self).__name__` — Klassenname im `__repr__` der Oberklasse oder als Anzeige | 11 | 🔨 |
| `__len__`, `__contains__`, `__iter__` — **keine Implementierungsaufgabe** | 13 | 👀 |
| `@property` — Methode ohne Klammern aufrufen | 14 | 👀 |
| `TypeError: 'bool' object is not callable` — Klammern bei `@property` | 14 | 👀 |

*(`min(..., key=...)` gehört zu **23a** und wird in 11a ausdrücklich vertagt — dort baut der Lernende die Schleife von Hand. Mehrfachvererbung kommt im ganzen Plan nicht vor.)*

---

## Etappe 12 — Der Tick

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `Welt` als Besitzer allen Zustands, den es pro Spiel einmal gibt | 1 | 🔨 |
| Ein Objekt als Parameter statt sechs Einzelwerte (`f(name, hafen)`) | 3 | 🔨 |
| Ein Objekt steht in einer Liste **und** unter eigenem Namen (`self.held`) | 4 | 🔨 |
| `self` als Argument weitergeben (`einheit.update(self)`) | 8 | 🔨 |
| Derselbe Parameter heißt drinnen `self` und draußen anders | 8 | 🧠 |
| Ein Methodenkörper, der nur aus einem Docstring besteht | 7 | 🔨 |
| `return` ohne Wert — sofort aussteigen, der Aufrufer bekommt `None` | 9 | 🔨 |
| `self.status = "tot"` — Zustand als String am Objekt | 12 | 🔨 |
| Sammeln und danach entfernen — zwei Schleifen statt einer | 11 | 🔨 |
| Entfernen beim Iterieren überspringt jeden zweiten Eintrag, **ohne Absturz** | 11 | 🧠 |
| `TypeError: … missing 1 required positional argument` beim vergessenen Argument | Stolpersteine | 🧠 |
| `REICHWEITE` als fester Wert, GROSS geschrieben | Auftrag 13 | 🔨 |
| `abschuesse` als Zähler am Objekt (Gedächtnis ohne Wirkung) | Auftrag 18 | 🔨 |
| `pass` als leerer Rumpf — statt des Docstrings, gleichwertig | 7 | 👀 |
| Der Begriff **Kopplung** — ein Ding, das alles kennt | 3 | 👀 |
| Der Begriff **Zustandsautomat** | 12 | 👀 |
| Die Tick-Reihenfolge als Entscheidung, nicht als Gegebenheit | 13 | 👀 |

*(`.copy()` aus Etappe 4 wird in Konzept 11 als zweiter Weg gezeigt und bleibt gültig — kein neuer Eintrag. `min(..., key=...)` wird in Konzept 10 ausdrücklich auf **23a** vertagt; die Zielsuche läuft als Schleife von Hand. `continue` bleibt 👀 — die Zielsuche in Auftrag 11 kommt mit einem verschachtelten `if` aus.)*

---

## Etappe 13 — Bauzeit und Abklingzeit

| Werkzeug | Konzept | Stufe |
|---|---|---|
| **Das Zähler-Muster** — `if z > 0:` · `z -= 1` · `if z == 0:` melden | 1 | 🔨 |
| Die Meldung **innerhalb** des `> 0`-Blocks macht aus einem Zustand ein Ereignis | 2 | 🧠 |
| Ein Zähler als Attribut an dem Objekt, dem er gehört | Design-Entscheidung | 🔨 |
| `welt.melde(text)` — ein Ort, an dem entschieden wird, wie Meldungen erscheinen | 5 | 🔨 |
| Einen Wert merken, neu berechnen, vergleichen — den Übergang erkennen | 4 | 🔨 |
| `d[a][b] = wert` — **schreibend** in ein verschachteltes Dictionary; fehlender innerer Schlüssel entsteht | 10 | 🔨 |
| `del d[key]` — jetzt aktiv, nicht mehr nur als Gegenbeispiel (aus **5** hochgestuft). **Nur nötig, wenn der versiegelte Weg in Etappe 5 als *markiert* gebaut wurde** | 10 | 🔨 |
| `KeyError` auch beim `del` eines fehlenden Schlüssels | 10 | 🧠 |
| Ein zweites Attribut für den Startwert (Trefferpunkte beim Aufstehen) | 8 | 🔨 |
| Ein Objekt unter eigenem Namen an der Welt als „höchstens einer" (`welt.turm`) | 9 | 🔨 |
| Ein Attribut (`gesteuert`) entscheidet den Startwert — **kein** Objektvergleich mit `is` | 7 | 🔨 |
| **Die Bedeutung einer Zählerzahl schriftlich festlegen** (Off-by-one vor dem Bauen) | Auftrag 7 | 🔨 |
| Eine Prüfkette mit Ortsbedingung und Kosten (aus **5** und **6**), erweitert um „steht schon eines?" | Auftrag 17 | 🔨 |
| Eine eigene Tick-Phase für Zähler, vor dem Handeln | Auftrag 4 | 🔨 |
| Invariante (prüfbar) und Merksatz (nicht prüfbar) unterscheiden — beide aufschreiben, keines prüfen | Auftrag 10 | 🧠 |
| Der Begriff **Scheduler** — die Welt führt Termine statt Zähler im Objekt | Design-Entscheidung | 👀 |
| Entscheidung **Tick-Zeit statt Echtzeit** — `time.time()` wird benannt, nicht benutzt | Design-Entscheidung | 👀 |

*(`is` als Vergleich zwischen Objekten bleibt 👀 — der Identitätsnachweis `a is b` aus Etappe 10 ist davon unberührt. Konzept 7 rät im Auftrag ausdrücklich davon ab und nennt das Attribut als gedeckten Weg. `assert` bleibt 👀 aus 7b: Schritt 9 lässt die Invariante aufschreiben, nicht prüfen. Die Stufenberechnung stammt aus 9a und wird nicht neu eingeführt — Schritt 8 legt nur zwei Zeilen darum.)*

---

## Etappe 14 — Das Vorfeld

| Werkzeug | Konzept | Stufe |
|---|---|---|
| **Eine Liste, deren Einträge Listen sind** — als Literal hingeschrieben | 1 | 🔨 |
| `raster[y][x]` — **Zeile vor Spalte**, lesend und schreibend | 2 | 🔨 |
| `raster[x][y]` stürzt bei quadratischem Raster **nicht** ab, liefert aber das falsche Feld | 2 | 🧠 |
| Ein Raster über zwei verschachtelte Schleifen aufbauen (`zeile = []`, `append`) | 3 | 🔨 |
| `[["."] * n] * n` erzeugt **eine** Zeile, n-mal verlinkt — aus **4** und **10** | 3 | 🧠 |
| Die Doppelschleife `for y in range(len(r))` / `for x in range(len(r[y]))` | 4 | 🔨 |
| `len(r[y])` statt `len(r[0])` — die Zeile fragen, in der man steht | 4 | 🧠 |
| **Die Randprüfung** — `< 0` und `>= len(...)`, beide Achsen, vor jedem Zugriff | 5 | 🔨 |
| Ein negativer Index greift **still** von hinten; über den unteren Rand knallt es | 5 | 🧠 |
| Eine flache Kopie eines Rasters: **jede Zeile einzeln** mit `.copy()` | 8 | 🔨 |
| `abs()` — der Betrag | 9 | 🔨 |
| Abstand als `abs(dx) + abs(dy)` — und dass die Form zur Bewegung passen muss | 9 | 🧠 |
| **Ein Set aus Tuples** (`felder.add((x, y))`) — Einlösung aus **6** | 10 | 🔨 |
| `TypeError: unhashable type: 'list'` — warum eine Liste nicht ins Set darf | 10 | 🧠 |
| `TypeError: add() takes exactly one argument (2 given)` — ein Klammerpaar fehlt | 10 | 🧠 |
| `(x, y) in menge` als Bereichsabfrage | 10 | 🔨 |
| Die Zonenprüfung — dieselbe Form wie die Randprüfung, andere Grenzen | 11 | 🔨 |
| Tuple-Unpacking aus einem Attribut (`x0, y0, x1, y1 = zone`) — aus **6** | 11 | 🔨 |
| Entscheidung `<` gegen `<=` bei Reichweite **schriftlich** festlegen (Konzept 9 legt fest: Abstand `<= r` ist drin) | 9, Auftrag 13 | 🔨 |
| 👀 `enumerate()` und die drei Schleifenformen — **kein Umbau** | 4 | 👀 |

*(`continue` bleibt 👀 und kommt nur in der Leseübung vor, mit ausdrücklichem Bauverbot. `min(..., key=...)` und Comprehensions werden in Konzept 10 und unter „Was NICHT" auf **23a** vertagt — die Doppelschleife wird heute ausgeschrieben. Der Bedingungsausdruck `a if c else b` und verkettete Vergleiche (`a <= x <= b`) werden bewusst **nicht** eingeführt; die Aufträge kommen mit `if`/`return` aus.)*

---

## Etappe 15 — Was die Brut hinterlässt

⚠️ **Fast keine neue Sprache.** Diese Etappe kombiniert Registriertes zu Mustern. Was hier steht, sind Bauformen, keine neuen Schlüsselwörter.

| Werkzeug | Konzept | Stufe |
|---|---|---|
| **Das Set-Muster: `add()` … später `in`** — merken und abfragen an getrennten Stellen | 1 | 🔨 |
| Ein falsch geschriebenes Flag-Wort erzeugt **keinen** Fehler — stiller Typ 3 | 1 | 🧠 |
| Set statt Dictionary aus Booleans — zwei Zustände statt drei | 2 | 🧠 |
| **Die Umkehrtabelle: Sache → Voraussetzung**, nachgeschlagen mit `.get()` + `is not None` + `in` | 4 | 🔨 |
| Eine Tabelle iterieren statt in der Logik aufzuzählen (`for k in TABELLE`) | 4 | 🔨 |
| **Suchschleife mit `return` in der Schleife und `return None` am Ende** — „das erste, das passt" | 5 | 🔨 |
| Jede Funktion, die `None` liefern kann, muss beim **Aufrufer** geprüft werden | 5 | 🧠 |
| `Fundstueck(Item)` — eine Unterklasse, die nur Attribute mitbringt (aus **11**); das Inventar behandelt sie unverändert | 6 | 🔨 |
| Prüfkette mit **verschiedenen** Meldungen für Katalog und Besitz (aus **6**) | Auftrag 7 | 🔨 |
| **Eine Quelle definiert die Flag-Wörter**, andere Tabellen verweisen nur darauf — ein Verweis ins Leere fällt nicht auf | 1, Auftrag 1 | 🔨 |
| 👀 **Kopplung als Zeichnung** — Pfeile auf Papier, nichts wird repariert | Kopplungszeichnung | 👀 |

*(Über ein Set wird **nicht** iteriert — jede Abfrage ist ein `in`. Die Reihenfolge eines Sets ist nirgends zugesagt, und der Guide braucht sie nicht. `dataclass` wird in Konzept 6 auf **23b** vertagt, `Enum` in Konzept 1 auf **21b**, gewichtete Beute auf **17a**.)*

---

## Etappe 16 — Bug-Jagd II

⚠️ **Keine neue Sprache — nicht eine Zeile.** Diese Etappe führt Verfahren ein, keine Werkzeuge. Sie steht hier, damit das Register lückenlos bleibt.

| Werkzeug | Konzept | Stufe |
|---|---|---|
| **Die Tick-Tabelle von Hand** — Phase mal Einheit, **vor** dem Ausführen | 3 | 🔨 |
| **Reihenfolgefehler als eigene Ursachenklasse** — die Schritte stimmen, ihre Anordnung entspricht nicht der Spielregel; **meistens** Typ 3, bei Zugriff auf Entferntes auch Typ 1 | 1 | 🧠 |
| Der Dreizeiler Beobachtung → Hypothese → Experiment als **Pflicht** (aus **8**) | 4 | 🔨 |
| **Die Rückwärtsprobe:** Änderung zurücknehmen — ist der Fehler wieder da? | 4 | 🔨 |
| **Zwei Familien, drei Notizen**: Off-by-one (13 Zeitsemantik, 14b Grenzwert) gegen **Tie-Break** (14a Gleichstand) — verschiedene Suchverfahren | 5 | 🧠 |
| Bisektion über die **Git-Historie** statt über den Code (aus **8**) | 7 | 🔨 |
| `git checkout <hash>` — einen alten Stand ansehen, nichts darauf committen; `git checkout main` (oder `master`) — zurück | 7 | 🔨 |
| **Verweis ins Leere** zwischen zwei Tabellen — beide für sich fehlerfrei (aus **15**) | 8 | 🧠 |
| „Wann hätte ich es gemerkt, wenn es funktioniert hätte?" — fehlende Wirkung ist schwerer zu bemerken als falsche | 6 | 🧠 |
| Die Leseleiter **auf eigenen Code** angewandt | Leseübung | 🔨 |

*(`git bisect` wird unter „Was NICHT" ausdrücklich ausgeschlossen — halbiert wird von Hand. `Enum` gegen Verweise ins Leere bleibt **21b**, Tests bleiben **26**.)*

---

## Etappe 17 — Der Wellengenerator

### 17a — Zufall

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `import random` als erste Zeile von `spiel.py` — Gebrauchsanweisung, erklärt in **24** *(Eintrag aus der Kür von 4, ab hier Auftrag)* | 1 | 🔨 |
| Eine eigene Datei `random.py` verdeckt das Modul — `AttributeError: … module 'random' has no attribute …`, mit oder ohne *partially initialized* | 1 | 🧠 |
| `random.randint(a, b)` — **beide Enden eingeschlossen**, anders als `range()` | 2 | 🔨 |
| `random.choice(liste)` *(Eintrag aus der Kür von 4, ab hier Auftrag)* · `IndexError` bei leerer Liste | 2 | 🔨 |
| `random.random()` — Kommazahl ab 0, immer unter 1; `< 0.3` als Prozentchance | 2 | 🧠 |
| Gewicht gegen Wahrscheinlichkeit — Anteil = Gewicht durch Summe | 3 | 🧠 |
| **Gewichtete Auswahl von Hand** — summieren, von 1 bis zur Summe würfeln, die Strecke ablaufen (`return` in der Schleife, `return None` am Ende) | 3 | 🔨 |
| Wurfbereich und Vergleichsgrenze gehören zusammen — eine falsche Grenze verschiebt still die Anteile | 3 | 🧠 |
| `ValueError: empty range …` bei `randint(1, 0)` — Summe vor dem Würfeln prüfen | 3 | 🧠 |
| Zufall prüfen durch Zählen: `d[k] = d.get(k, 0) + 1` über viele Züge | 4 | 🔨 |
| `if not d:` — ein leeres Dictionary ist falsy wie eine leere Liste | 5 | 🔨 |
| **Das Budget-Muster** — das Bezahlbare in jeder Runde neu bauen, ziehen, bezahlen; Ende bei *nichts mehr bezahlbar* | 5 | 🔨 |
| `random.choices(liste, weights=[...])[0]` — liefert eine **Liste** | 7 | 👀 |

### 17b — Der Seed

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `random.seed(n)` — **einmal**, vor dem ersten Zufallsaufruf | 10 | 🔨 |
| Ein fester Wert als Schalter: `SEED = None` heißt *selbst ziehen* | 10 | 🔨 |
| Derselbe Seed und dieselben Eingaben ergeben denselben Lauf; jeder Zufallsaufruf verbraucht die nächste Zahl der Folge | 11 | 🧠 |
| Die Reihenfolge eines Sets aus Strings kann sich zwischen zwei Programmstarts ändern — der Seed ändert daran nichts | 11 | 🧠 |
| Der Debugger liest aus derselben Eingabe wie `input()` — bedingte Breakpoints nie zusammen mit `<` | 12 | 🧠 |

### 17c — Zwischen den Wellen

| Werkzeug | Konzept | Stufe |
|---|---|---|
| Ein Standardargument an einer **bestehenden** Methode nachrüsten — alte Aufrufe bleiben gültig (aus **7**, Konzept 6) · Weg B; Weg A ist eine zweite Methode `notiere()` | 13 | 🔨 |
| **Einzelne `if` füllen einen Topf, eine `elif`-Kette führt das Gezogene aus** (aus **2**, Konzept 4) | 14 | 🔨 |
| Das Zähler-Muster mit einer anderen Uhr — einmal pro Wellenende statt pro Takt (aus **13**) | 16 | 🔨 |

*(Der Beweislauf mit `<`, `>` und `diff` stammt aus Etappe 7, der bedingte Breakpoint aus Etappe 8, „merken, neu berechnen, vergleichen" aus Etappe 13 — kein neuer Eintrag. Die Stimmen im Wellenbericht sind Methoden überschreiben aus Etappe 11, Konzept 8 — ebenfalls kein neuer Eintrag. Die Leseübung gehört zu 17b und benutzt `for _ in range(...)`; `_` steht seit 3a auf 👀 und wird nicht gebaut. `random.shuffle` und `random.sample` kommen im Plan nicht vor.)*

---

## Etappe 18 — Fähigkeiten, Skillpunkte, Statuseffekte

### 18a — Statuseffekte

| Werkzeug | Konzept | Stufe |
|---|---|---|
| **Ein Dictionary *Name → Restdauer* herunterzählen** — Werte ändern beim Durchlaufen, Abgelaufenes erst sammeln, danach mit `del` löschen (aus **5**, **12** und **13**) | 2 | 🔨 |
| **Ein abgeleiteter Wert als Methode** (`aktueller_schaden()`) — der Grundwert wird nie „vorübergehend" verändert | 4 | 🔨 |
| **Eine Tabelle, die beschreibt, *was* ein Effekt tut** (Dauer, Schaden pro Takt, was halbiert wird) — der Code fragt die Spalten, nicht die Namen | 5 | 🔨 |
| `return` in der Fassung der Oberklasse beendet **nur diese Fassung** — `super().methode()` kehrt zurück, die Fassung der Unterklasse läuft weiter | Auftrag 4 | 🧠 |

### 18b — Skillpunkte und Voraussetzungen

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `a - b` — **die Differenzmenge**, aktiv gebaut *(Eintrag aus Etappe 6 hochgestuft)* | 10 | 🔨 |
| **Ein leeres Set ist falsy** — `if fehlt:` fragt „fehlt überhaupt etwas?" | 10 | 🔨 |
| **Ein Set als Wert in einem Dictionary** (`"braucht": {"grundkurs"}`) — leer ist `set()`, nicht `{}` | 9 | 🔨 |
| **Eine Prüfkette, die einen Grund oder `None` liefert** — jeder Zweig ein `return` mit Text, am Ende `return None`; der Aufrufer fragt `is None` | 11 | 🔨 |
| **Die `or`-Falle bei `0`** — `wert or ersatz` ersetzt auch eine gültige `0` | 12 | 🧠 |

### 18c — Fähigkeiten wirken

| Werkzeug | Konzept | Stufe |
|---|---|---|
| **Die Oberklasse ruft `self.methode()` auf, und die Fassung der Unterklasse läuft** — der Ablauf steht oben, die Wirkung unten; `return super().methode(...)` als Rückfallebene | 14 | 🔨 |
| **Ein fehlendes `return` liefert `None`, und `None` sieht aus wie `False`** — stiller Typ 3 | 14 | 🧠 |

*(Kein neuer Eintrag, weil nur Registriertes kombiniert wird: das Abklingzeiten-Dictionary in 18c ist das Muster aus 18a; `RuntimeError` beim Größenändern stammt aus **5**; die Zeitsemantik-Tabelle aus **13**; die Reichweitenmenge, `abstand()` und die Randprüfung aus **14**; die Umkehrtabelle und die Suchschleife mit `return None` aus **15**; der Beweislauf mit festem Seed und `diff` aus **17b**; `and`/`or` als Rückgabewerte bleiben 👀 aus **2** und werden in Konzept 12 nur wieder gelesen. Dass die Reihenfolge einer Differenzmenge nicht zugesagt ist, folgt aus **17b** — die Ausgabe läuft deshalb über `FUNDE`. `max()` und `sorted()` werden nicht gebraucht; das beste Ziel wird wie in **12** von Hand gesucht. `//=` wird nicht eingeführt: halbiert wird mit `wert = wert // 2`. Die Mine ist eine eigene Klasse ohne `Einheit` als Oberklasse — `class` aus **9**. Die `elif`-Ketten in `wirke()` und in der Kameraden-KI sind gewollt und sterben in **23a**.)*

---

## Etappe 19 — Speichern und Laden

### 19a — Dateien und JSON

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `import json` und `from pathlib import Path` — Gebrauchsanweisung, erklärt in **24**; `from … import …` holt einen einzelnen Namen, der danach ohne Kastennamen dasteht | 2 | 🔨 |
| `Path("ordner") / "datei.json"` — ein Pfad, `/` hängt ein Stück an; links muss ein Pfad stehen | 3 | 🔨 |
| `.exists()` und `.mkdir(exist_ok=True)` — ein Argument mit Namen an einem fremden Werkzeug (Form aus **17c**) | 3 | 🔨 |
| Ein relativer Pfad meint den Ordner, in dem das Terminal steht (aus **7**, Konzept 11) | 3 | 🧠 |
| `with open(pfad, "w", encoding="utf-8") as f:` und dasselbe mit `"r"` — `with` schließt die Datei von selbst; `"w"` überschreibt vollständig | 4 | 🔨 |
| `json.dump(daten, f, ensure_ascii=False, indent=2)` und `json.load(f)` | 4 | 🔨 |
| Die sechs Dinge, die JSON kennt; Tuple → Liste, Set → `TypeError`, Zahlenschlüssel → Text, `None` ↔ `null` | 5 | 🧠 |
| `[3, 2] == (3, 2)` ist `False` — eine geladene Liste ist nie gleich einem Tuple | 5 | 🧠 |
| `FileNotFoundError`, `FileExistsError`, `TypeError: Object of type … is not JSON serializable`, `JSONDecodeError` lesen | 3, 4, 5, Auftrag 7 | 🧠 |
| `sorted(sammlung)` — gibt eine neue, sortierte Liste zurück; ohne `key=` (das ist **23a**) | 6 | 🔨 |

### 19b — Objekte werden Daten

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `tuple(liste)` — der Rückweg zum Tuple, wie `set(liste)` aus **6** | 12 | 🔨 |
| **Eine Methode, die ein Objekt als Dictionary beschreibt, und ihr Gegenstück, das ein erzeugtes Objekt daraus überschreibt** — in der Unterklasse mit `super()` zuerst (aus **11**) | 8 | 🔨 |
| **Ein Verweis als Stelle in einer Liste** — `.index()` beim Speichern, `liste[stelle]` beim Laden, erst alle Objekte, dann die Verweise, Prüfung mit `is` (aus **6** und **10**) | 10 | 🔨 |
| Das Erzeugen ist die eine Stelle, an der nach dem Typ gefragt werden muss — dort ist eine Kette über Klassennamen erlaubt | 9 | 🧠 |

### 19c — Das Spiel überlebt das Beenden

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `pfad.unlink()` — löscht eine Datei; vorher mit `.exists()` fragen | Auftrag 23 | 🔨 |
| Was ein Seed nach dem Laden kann und was nicht — neu säen beim Speichern | Design-Entscheidung | 🧠 |
| Ein Wert, der für einen Übergang gemerkt wird, ist Zustand — auch wenn er sich herleiten lässt | 13 | 🧠 |
| Ein halb geschriebener Spielstand — `"w"` leert beim Öffnen | 15 | 🧠 |
| Atomares Schreiben: in eine andere Datei schreiben, dann umbenennen | 15 | 👀 |

*(Kein neuer Eintrag, weil nur Registriertes kombiniert wird: das Standardargument für den Pfad (**7**), `.copy()` am Dictionary (dieselbe Methode wie an der Liste, **4**, **10**), `set(liste)` (**6**), `type(self).__name__` und die Klasse als Wert (**11**), `random.randint` und `random.seed` (**17**), der Beweislauf mit `<`, `>` und `diff` (**7**, **17b**), `input()`-Zweige und `is None` (**2**, **10**). `pickle` und `random.getstate()` werden nur genannt, nicht gezeigt — keine Zeile Code. `Path.replace()` steht allein unter „Wenn du mehr willst" und wird dort erklärt. `try`/`except` bleibt **20**.)*

---

## Etappe 20 — Wenn der Spieler Unsinn eingibt

### 20a — Fangen

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `try:` / `except Fehlerklasse:` — bei einem Fehler springt Python in den `except`, der Rest des `try` läuft nicht | 2 | 🔨 |
| `except Fehlerklasse as e:` — die Nachricht steckt in `e`; bei `KeyError` ist sie der Schlüssel mit Anführungszeichen | 4 | 🔨 |
| Mehrere `except` untereinander — der erste passende gewinnt | 6 | 🔨 |
| `except json.JSONDecodeError:` — eine Fehlerklasse aus einem Werkzeugkasten | 6 | 🔨 |
| Eng fangen: nur die erwartete Fehlerklasse, nur um die eine Zeile, die scheitern darf | 3 | 🧠 |
| `except Exception` und nacktes `except:` machen aus Typ 1 einen Typ 3; nacktes `except:` fängt sogar `Strg + C` | 3 | 🧠 |
| Prüfen oder fangen? — prüfen, wenn die Frage einfach ist; fangen, wenn man es nur durch Versuchen erfährt; danach oft noch ein `if` | 5 | 🧠 |
| Fehlerklassen haben Oberklassen — `JSONDecodeError` ist ein `ValueError`, `Exception` ist die Oberklasse fast aller | 6 | 👀 |

### 20b — Werfen

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `class SpielFehler(Exception):` mit einem Docstring als Körper — eine eigene Fehlerklasse (aus **11** und **12**) | 7 | 🔨 |
| `raise SpielFehler("…")` — die Funktion endet sofort, der Fehler fliegt | 7 | 🔨 |
| `else:` beim `try` — läuft nur, wenn kein Fehler aufgetreten ist | 10 | 🔨 |
| Ein Fehler wandert die Aufrufkette hinauf bis zum ersten passenden `except`; die Stufen dazwischen enden sofort (aus **7a**, **8**) | 8 | 🧠 |
| `return Fehler(...)` statt `raise` — gibt ein Objekt zurück, nichts fliegt; stiller Typ 3 | 7 | 🧠 |
| Grund-oder-`None` gegen Exception — fragen gegen verlangen | 9 | 🧠 |
| Wem gehört ein Fehler — Spieler, Welt, Entwickler | 11 | 🧠 |

### 20c — Prüfen und trennen

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `assert bedingung, "Text"` *(Eintrag aus Etappe 7 hochgestuft)* | 12 | 🔨 |
| Ein `AssertionError` wird nie gefangen; `python -O` schaltet Behauptungen ab — deshalb prüft `assert` nie Eingaben | 12 | 🧠 |
| `finally` — und wann es nicht läuft | 15 | 👀 |
| `raise` ohne Fehler dahinter, in einem `except` — weiterwerfen | 15 | 👀 |
| `logging` und seine Stufen `debug`, `info`, `warning`, `error` | 14 | 👀 |

*(Kein neuer Eintrag, weil nur Registriertes kombiniert wird: der Schalter `DEBUG` ist ein fester Wert mit `if` (Form aus **17b**, `SEED`), `welt.debug()` eine Methode wie `melde()` (**13**), die Tabellen- und Zustandsprüfungen sind Schleifen mit `in` (**4**, **6**), die Munitions-Invariante ist *merken, neu berechnen, vergleichen* (**13**). `len()` vor dem Zugriff auf das zweite Wort stammt aus **4**. `continue` bleibt 👀 aus **3a** — die kleine Schleife aus Konzept 2 kommt ohne aus. Keine Familie eigener Fehlerklassen; `logging` bleibt bis **24** unbenutzt.)*

---

## Offene Lücken

Werkzeuge, die eine Aufgabe braucht und die kein Guide erklärt. **Jede solche Zeile blockiert einen Lernenden, der keine zweite Quelle hat.**

> **Für die Etappen 1 bis 20: keine.** Alle Werkzeuge, die ein Auftragsschritt dort verlangt, sind vorher erklärt.

**Diese Tabelle bleibt trotzdem stehen**, weil sie beim Schreiben jeder weiteren Etappe wieder gebraucht wird. Findest du eine Lücke, trag sie hier ein — mit der Etappe, die sie braucht, und der Etappe, in die die Erklärung gehört.

| Werkzeug | Gebraucht in | Muss erklärt werden in |
|---|---|---|
| *(zurzeit leer)* | | |

**Eine dritte geschlossene Lücke, gefunden beim Durchsehen von Etappe 7:** `.clear()` bei einer Liste. Konzept 5 verlangte in einem „probier das aus"-Schritt `k.clear()` — erklärt war die Methode nirgends. Sie *stand* in Etappe 4, aber nur als eines von 81 Wörtern in der abgedruckten `dir([])`-Ausgabe, und **eine Nennung in einer Werkzeugliste ist keine Einführung**. Der Schritt arbeitet jetzt mit `.append()`, das seit Etappe 4 auf 🔨 steht; `.clear()` kommt im ganzen Plan nicht mehr vor. **Die Lehre: Was `dir()` ausspuckt, gilt nicht als eingeführt.**

**Eine zweite geschlossene Lücke, gefunden beim Schreiben von Etappe 12:** Das **nackte `return`** ohne Wert. Etappe 7 erklärt `return name` und `return None`, nie `return` allein — und die Auftragsschritte 12 und 13 der Etappe 12 verlangen genau die Form („Status `"tot"`? Sofort `return`."). Erklärt wird sie jetzt in Etappe 12, Konzept 9. **Dasselbe Muster wie unten: Beide Einzelteile waren registriert, die Schreibweise selbst nicht.**

**Eine geschlossene Lücke zur Erinnerung:** Der Dictionary-Zugriff im f-String fehlte in Etappe 5 bis v1.3.0 — der Auftrag verlangte ihn (Schritt 9, Statusanzeige auf `vorrat` umstellen), kein Konzept erklärte ihn. Aufgefallen ist das **nicht beim Review, sondern beim Bauen**. Die Lehre daraus: Ein Werkzeug kann fehlen, obwohl beide Einzelteile registriert sind — f-Strings seit Etappe 1, Dictionaries seit Etappe 5. **Prüf beim Schreiben nicht nur die Werkzeuge, sondern auch ihre Kombinationen.**

**Zur Erinnerung, wie es dazu kam:** Elf solcher Lücken waren im Bestand, und keine davon war Nachlässigkeit im Einzelfall. Sie entstanden, weil die Guides nach *Ideen* gegliedert sind und `+=`, `%`, `//`, `liste[i] =` und `.pop()` zu klein für eine eigene Idee und zu neu zum Voraussetzen waren. Genau dagegen gibt es diese Datei.

---

## Pflege

**Wenn eine Etappe geschrieben oder überarbeitet wird:** Jeden Auftragsschritt tatsächlich selbst lösen, jedes benötigte Werkzeug notieren, gegen dieses Register prüfen. Drei mögliche Ausgänge — steht mit Etappe ≤ N drin (in Ordnung), fehlt und gehört hierher (erklären und eintragen), gehört in eine spätere Etappe (Aufgabe umbauen).

**Außerhalb von Codeblöcken mitprüfen:** Stolpersteine-Tabelle, Kaputtmach-Experimente, Selbsttest, Klammerbemerkungen. Dort ist historisch das meiste durchgerutscht.

**Wenn ein Werkzeug von 👀 auf 🔨 hochgestuft wird:** Eintrag ändern, nicht doppeln, und die Kopfzeile der betroffenen Etappe nachziehen.

**Wenn eine Lücke geschlossen ist:** Die Zeile in der Etappentabelle bekommt ihre Konzeptnummer, und der Eintrag verschwindet aus „Offene Lücken".

**Die Kopfzeile „Neue Syntax heute" jedes Guides muss deckungsgleich sein** mit dem, was diese Etappe hier neu einträgt. Sie ist die Zusage an den Lernenden, dass er nichts anderes braucht.
