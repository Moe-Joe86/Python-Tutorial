# Das Syntaxregister — welches Werkzeug ab wann zur Verfügung steht

*v1.4.0 · 2026-09-07*

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
| `and` / `or` geben Werte zurück, nicht `True`/`False` | 7 | 👀 |

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

---

## Etappe 5 — Der Vorposten und das Depot

| Werkzeug | Konzept | Stufe |
|---|---|---|
| `{"schluessel": wert}` — Dictionary | 1 | 🔨 |
| `d["schluessel"]` — lesen | 2 | 🔨 |
| `d["schluessel"] = wert` — anlegen und überschreiben | 2 | 🔨 |
| `KeyError` | 2 | 🧠 |
| `.get(key)` und `.get(key, ersatz)` | 3 | 🔨 |
| `in` prüft beim Dictionary den Schlüssel | 4 | 🔨 |
| `in d.values()` | 4 | 👀 |
| `d[a][b]` — verschachtelter Zugriff | 5 | 🔨 |
| `f"{d['schluessel']}"` — Zugriff im f-String, innen die andere Anführungssorte | 2b | 🔨 |
| Gleiche Anführungszeichen innen wie außen sind erst ab Python 3.12 erlaubt | 2b | 🧠 |
| `python3 --version` | 2b | 🔨 |
| `for name in d` — läuft über die Schlüssel | 6 | 🔨 |
| `.items()` | 6 | 🔨 |
| `.keys()` und `.values()` | 6 | 👀 |
| `del d[key]` | 6 (als Gegenbeispiel gezeigt) | 🧠 |
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
| `&` `\|` `-` — Mengenoperationen | 10 | 👀 |
| Sets und Tuples lassen sich nicht als JSON speichern | 14 | 👀 |
| `.pop(i)` — entfernt über die Stelle und gibt zurück | **0** | 🔨 |
| `del liste[i]` | **0** | 🔨 |
| `remove` / `pop` / `del` unterscheiden | **0** | 🧠 |
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
| `return a, b` — zwei Werte zurückgeben | 14 | 🔨 |
| `assert` | 15 | 👀 |
| `UnboundLocalError` — Zuweisung im Körper macht den Namen im ganzen Körper lokal | 5 | 🧠 |
| Seiteneffekt gegen Rückgabewert | 5 | 🧠 |
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

*(Diese Etappe führt keine Spielsyntax ein — alles hier sind Werkzeuge zur Fehlersuche. Das Traceback-Lesen steht bereits bei Etappe 1 auf 🧠 und wird hier nur aktiv geübt, deshalb kein neuer Eintrag. `git diff` und `git log --oneline` gehören in den Git-Faden des Bogens, nicht in dieses Register.)*

---

## Offene Lücken

Werkzeuge, die eine Aufgabe braucht und die kein Guide erklärt. **Jede solche Zeile blockiert einen Lernenden, der keine zweite Quelle hat.**

> **Für die Etappen 1 bis 8: keine.** Alle Werkzeuge, die ein Auftragsschritt dort verlangt, sind vorher erklärt.

**Diese Tabelle bleibt trotzdem stehen**, weil sie beim Schreiben jeder weiteren Etappe wieder gebraucht wird. Findest du eine Lücke, trag sie hier ein — mit der Etappe, die sie braucht, und der Etappe, in die die Erklärung gehört.

| Werkzeug | Gebraucht in | Muss erklärt werden in |
|---|---|---|
| *(zurzeit leer)* | | |

**Eine geschlossene Lücke zur Erinnerung:** Der Dictionary-Zugriff im f-String fehlte in Etappe 5 bis v1.3.0 — der Auftrag verlangte ihn (Schritt 9, Statusanzeige auf `vorrat` umstellen), kein Konzept erklärte ihn. Aufgefallen ist das **nicht beim Review, sondern beim Bauen**. Die Lehre daraus: Ein Werkzeug kann fehlen, obwohl beide Einzelteile registriert sind — f-Strings seit Etappe 1, Dictionaries seit Etappe 5. **Prüf beim Schreiben nicht nur die Werkzeuge, sondern auch ihre Kombinationen.**

**Zur Erinnerung, wie es dazu kam:** Elf solcher Lücken waren im Bestand, und keine davon war Nachlässigkeit im Einzelfall. Sie entstanden, weil die Guides nach *Ideen* gegliedert sind und `+=`, `%`, `//`, `liste[i] =` und `.pop()` zu klein für eine eigene Idee und zu neu zum Voraussetzen waren. Genau dagegen gibt es diese Datei.

---

## Pflege

**Wenn eine Etappe geschrieben oder überarbeitet wird:** Jeden Auftragsschritt tatsächlich selbst lösen, jedes benötigte Werkzeug notieren, gegen dieses Register prüfen. Drei mögliche Ausgänge — steht mit Etappe ≤ N drin (in Ordnung), fehlt und gehört hierher (erklären und eintragen), gehört in eine spätere Etappe (Aufgabe umbauen).

**Außerhalb von Codeblöcken mitprüfen:** Stolpersteine-Tabelle, Kaputtmach-Experimente, Selbsttest, Klammerbemerkungen. Dort ist historisch das meiste durchgerutscht.

**Wenn ein Werkzeug von 👀 auf 🔨 hochgestuft wird:** Eintrag ändern, nicht doppeln, und die Kopfzeile der betroffenen Etappe nachziehen.

**Wenn eine Lücke geschlossen ist:** Die Zeile in der Etappentabelle bekommt ihre Konzeptnummer, und der Eintrag verschwindet aus „Offene Lücken".

**Die Kopfzeile „Neue Syntax heute" jedes Guides muss deckungsgleich sein** mit dem, was diese Etappe hier neu einträgt. Sie ist die Zusage an den Lernenden, dass er nichts anderes braucht.
