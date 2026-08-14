# Projekt-Lehrplan: Dein Dorf-RPG

**Begleitend zu Boot.dev — Python lernen, indem das Spiel wächst**
*Fassung 4 — final. Ab hier wächst der Plan nur noch durch dein eigenes Projekt.*

---

## Die Prämisse

Du wachst an einem Morgen auf. Das Dorf ist leer. Drei Menschen sind noch da. Alle anderen sind fort — keine Kampfspuren, keine Abschiedsbriefe, nur kalte Herdstellen und ein Frühstück, das jemand nicht mehr zu Ende gegessen hat.

Vor dem Dorf liegt eine Wiese. Weiter draußen der Eingang zu einer alten Mine, die niemand mehr betreten hat.

**Die drei, die geblieben sind** — Namen sind deine Baustelle, ich schlage nur Funktionen vor, weil jede an ein Code-System andockt:

| Rolle | Erzählerisch | Technisch |
|---|---|---|
| **Der Wissende** | Kennt das Dorf, redet nur gegen Gegenleistung | Dialogbaum, Flags |
| **Die Versorgerin** | Hat Werkzeug, Samen, Vorräte | Item-System, Handel, Crafting |
| **Der Fremde** | War erst seit kurzem da. Oder behauptet das | Vertrauenswert, unzuverlässige Information |

Drei Figuren sind auch die klassische Mindestbesetzung für einen Verdacht. Bei zwölf Verdächtigen ist niemand verdächtig; bei dreien ist es jeder. Zurückkehrende Dorfbewohner sind deine Belohnungswährung — du erweiterst den Bestand genau dann, wenn dein Code bereit ist.

---

## Die zwei Fähigkeiten

Es gibt zwei Arten, ein Projekt abzuschließen:

**„Mein Inventar funktioniert."** — Du erinnerst dich an deinen eigenen Code.
**„Ich kann mit Listen umgehen."** — Du beherrschst das Konzept.

Der erste Zustand fühlt sich wie der zweite an. Er ist es nicht.

Und es gibt zwei Fähigkeiten, die ebenfalls nicht dasselbe sind:

**Python schreiben** — du bringst deine Absicht in Code.
**Python lesen** — du verstehst Code, den jemand anders geschrieben hat.

Für dein eigentliches Ziel ist die zweite die wichtigere. Sie wird in keinem Kurs unterrichtet, weil Kurse dich immer schreiben lassen. Deshalb steht sie ab Etappe 9 fest im Plan.

---

## Die Struktur jeder Etappe

1. **Boot.dev** — was du dort lernst
2. **Was du baust** — die Anwendung im Spiel
3. **Lernziele** — was du danach *ohne Hilfe erklären* können musst
4. **Entweder Transferaufgabe oder Leseübung** — 5–15 Minuten
5. **Kaputtmach-Experiment** — absichtlich zerstören und beobachten
6. **Commit**

**Punkt 4 ist ein Entweder-oder, kein Und.** Das ist meine wichtigste Abweichung von den Vorschlägen, die diesen Plan gewachsen haben. Bei 20–30 Minuten am Tag ist die größte Gefahr nicht, zu wenig zu üben — sondern dass der Plan zur Bürokratie wird und du aufhörst. Sechs Pflichtelemente pro Etappe wären genau das. Wähle je nach Etappe, was mehr bringt.

**Transferaufgabe:** Bewusst *außerhalb* des Spiels, in einer Wegwerf-Datei. Wenn du eine Liste nur im Kontext deines Inventars bedienen kannst, kannst du keine Listen. Obergrenze 15 Minuten — sie darf nie zum zweiten Projekt werden.

**Leseübung:** Ich zeige dir fremden Code, du erklärst ihn. Nicht „schreib das", sondern: *Was passiert hier? Was ist dieses Objekt? Wann wird die Methode aufgerufen? Was steht am Ende in der Variable?* Später nehme ich dafür bewusst Code, den ich selbst geschrieben habe — also genau das, womit du beim Vibe Coding konfrontiert bist.

**Kaputtmachen:** Kein Spaßelement. „So schreibt man es" ist Auswendiglernen. „Warum muss es so sein" ist Verstehen. Der einzige verlässliche Weg dorthin führt über die Fehlermeldung.

---

## Das übergreifende Prinzip

> **Neue Funktionalität hinzufügen, ohne bestehende kaputtzumachen.**

Das ist keine Etappe, sondern der Maßstab für alles ab Block 2. Anfänger denken: Programmieren = neuen Code schreiben. In Wirklichkeit besteht der Beruf zum großen Teil daraus, bestehenden Code zu verstehen und vorsichtig zu verändern.

Deshalb tauchen im Plan immer wieder Aufgaben dieser Form auf: *„Füge X hinzu, ohne Y anzufassen."* Wenn das nicht geht, ist das eine Erkenntnis über deinen Code — nicht über dein Können.

---

## Die Bug-Jagd

Fehlerbehandlung und Debugging sind **nicht dasselbe**. `try/except` verhindert Abstürze. Debugging heißt herausfinden, *warum* etwas nicht tut, was es soll.

**Drei Sorten Fehler, nach Schwierigkeit:**

1. Stürzt sofort ab — unangenehm, aber ehrlich
2. Stürzt manchmal ab — schwerer, weil er von Bedingungen abhängt
3. **Stürzt nie ab und liefert einfach das Falsche** — die gefährlichste Sorte

Der dritte Typ ist der wichtigste, weil er eine der schädlichsten Überzeugungen zerstört, die Anfänger haben: *„Wenn Python keinen Fehler anzeigt, ist mein Programm richtig."* Das ist schlicht falsch, und je früher du das körperlich spürst, desto besser.

**Wie wir es machen — bewusst unvorhersehbar.** Wenn du weißt „nach jedem Block versteckt Claude drei Bugs", wird daraus wieder eine Schulaufgabe. Also läuft es zufällig ab. Manchmal bekommst du ein normales Review. Manchmal einen manipulierten Code. Manchmal: „Irgendwo in deinem eigenen Code ist ein Fehler, den du selbst eingebaut hast — such ihn."

**Eine Zusage dazu, damit das nicht ins Rutschen kommt:** Ich behaupte nie, dein Code sei fehlerfrei, wenn ich einen Fehler sehe. Und ich behaupte nie, ich hätte einen Fehler eingebaut, wenn ich es nicht getan habe. Die Unvorhersehbarkeit betrifft nur, *ob* ich manipuliere — nie die Wahrheit über deinen eigenen Code.

**Was du dabei lernst:** Tracebacks von unten nach oben lesen. Den VS-Code-Debugger (Breakpoint, Variablen inspizieren). Gezielte `print()`-Ausgaben statt Herumraten. Und die Unterscheidung, auf die alles ankommt: *Wo es knallt, ist selten, wo es kaputt ist.*

**Warum das für dich besonders zählt:** Wenn dir eines Tages 400 Zeilen vorliegen, die du nicht selbst geschrieben hast, ist „ich kann den Fehler lokalisieren und präzise beschreiben" mehr wert als jedes auswendig gelernte Syntaxdetail.

---

## Git und GitHub — bewusst rationiert

Git ist ein Fass ohne Boden, und es ist kein Python. Wer in Woche 3 Rebase-Strategien liest, lernt in Woche 3 kein Programmieren.

**Minimalset für die ersten Monate:**

```
git init / git status / git add . / git commit -m "..." / git push
git log --oneline        # deine Motivationskurve
```

Drei Dateien im Repo: `README.md` (dein Schaufenster), `GELERNT.md` (zwei Sätze pro Etappe), `.gitignore` (`__pycache__/`, `saves/`, `.venv/`).

**Aufgeschoben bis Etappe 24:** Branches, Pull Requests, Merge-Konflikte, Rebase. Ein Branch ergibt Sinn, wenn du beim Kampfbalancing experimentieren und das Ergebnis wegwerfen willst. Vorher ist es Zeremonie ohne Zweck.

**Ehrlicher Zusatznutzen:** Ein öffentliches Repo mit hunderten Commits über Monate ist ein besserer Nachweis für Durchhaltevermögen als jedes Kurszertifikat.

---

## Arbeitsregeln

**Kein Vibe Coding in diesem Projekt.** Du schreibst jede Zeile selbst. Wenn du feststeckst: „Ich will X, habe Y probiert, es passiert Z — woran könnte es liegen?"

**Etappen dürfen halbiert werden.** Der Plan ist ein Vorschlag, kein Vertrag.

**Umwege haben Vorrang.** Wenn dein eigenes Programm eine Frage erzeugt, ist diese Frage die nächste Lektion — auch wenn sie hier nicht steht.

---

## Zeitrahmen

Bei 20–30 Minuten am Tag, Übungen eingerechnet:

| Block | Etappen | Dauer |
|---|---|---|
| Werkzeug | 0 | 1 Abend |
| Fundament | 1–8 | 7–10 Wochen |
| Objekte und Zeit | 9–16 | 9–12 Wochen |
| Die Welt reagiert | 17–26 | 12–16 Wochen |
| Grafik | 27–29 | offen |

Die Etappen 1–6 sind ausgearbeitet und veranschlagen zusammen 22–31 Sitzungen — die Schätzung für Block 1 ist daran geeicht und nicht geraten.

Der Punkt, an dem es *richtig* Spaß macht, liegt bei Etappe 12–13.

---

# BLOCK 0 — Werkzeug

## Etappe 0 — Das Repo

Ein Abend, kein Python. Repo auf GitHub, lokal klonen, `README.md`, `GELERNT.md`, `.gitignore`, virtuelle Umgebung (`python -m venv .venv`), erster Commit, erster Push.

**Lernziele:** Was ist ein Commit? Warum existiert `.gitignore`? Wozu eine virtuelle Umgebung?

**Commit:** `Etappe 0: Projektstart`

---

# BLOCK 1 — Fundament

*Boot.dev: „Learn to Code in Python", erste Kapitel*

## Etappe 1 — Der erste Morgen

**Boot.dev:** Variablen, Strings, f-Strings, `print()`, `input()`

**Was du baust:**
`spiel.py`. Der Spieler gibt seinen Namen ein. Variablen für Tageszeit, Wetter, Geruch, Dorfname — und mindestens drei f-Strings, die sie in die Beschreibung des Morgens einbauen. Dann ruft er. Niemand antwortet.

Auflage als Autor: Nirgends darf wörtlich stehen, dass das Dorf leer ist. Der Text zeigt es.

`geruch` hebst du auf. In Etappe 17 schreibst du: *„Du erinnerst dich an den Geruch von Brot an diesem ersten Morgen. Jetzt riecht es nach kaltem Rauch."*

**Ehrlich eingeordnet:** Kaum eine Programmier-Übung. Aber sie baut eine Gewohnheit an, die technisch zählt: **Weltzustand wird gespeichert, nicht nur ausgegeben.**

**Lernziele:**
- Unterschied zwischen einer Variable und ihrem Wert?
- Was macht das `f` vor dem String genau?
- Warum ist `alter = "12"` etwas anderes als `alter = 12`?
- Was gibt `input()` zurück — in welchem Datentyp?

**Transferaufgabe (5 Min):** Frage nach dem Geburtsjahr, berechne das Alter. Achte darauf, was mit dem Rückgabewert von `input()` passieren muss.

**Kaputtmachen:** Lass das `f` weg. Rechne mit `input()`, ohne umzuwandeln. `TypeError` wird dein häufigster Fehler der nächsten Monate.

**Commit:** `Etappe 1: Der erste Morgen`

---

## Etappe 2 — Die erste Begegnung

**Boot.dev:** `if` / `elif` / `else`, Vergleiche, Booleans, `and` / `or` / `not`

**Was du baust:**
Einer der drei findet dich. Zwei Antwortmöglichkeiten: Du erzählst, was du gesehen hast — oder du behältst es für dich. `vertrauen = True/False` merkt sich das.

**Und gleich richtig kombinieren.** Nicht nur einzelne Booleans, sondern verknüpfte Bedingungen — genau die Form, die dir in Etappe 18 als vollständiges Flag-System begegnet:

```python
if vertrauen and hat_hinweis and not misstrauisch:
```

**Lernziele:**
- Wann `elif`, wann mehrere separate `if`? (Echter Unterschied, keine Stilfrage.)
- Was ergibt `"5" == 5`? Warum?
- Was ist „truthy"? Welche Werte sind falsch, ohne `False` zu sein?
- Was ergibt `not (a and b)` im Vergleich zu `not a and not b`?

**Transferaufgabe (10 Min):** Türsteher. Frag nach Alter und Gästelisten-Status, entscheide mit **einer** verknüpften Bedingung über den Einlass — nicht mit verschachtelten `if`. (Noch ohne Funktion; die kommt in Etappe 7.)

**Kaputtmachen:** Schreib `if vertrauen = True:`. Der Klassiker, der jeden einmal eine halbe Stunde kostet.

---

## Etappe 3 — Die Game-Loop

**Boot.dev:** `while`, `for`, `range()`, `break`, `continue`

**Was du baust:**
Die Hauptschleife. „Was tust du?" → Befehl lesen (`umsehen`, `reden`, `beenden`) → reagieren → von vorn.

Dazu ein Zähler mit `+=`, der die Runden mitzählt — in Etappe 12 wird daraus `self.zeit += 1`, die Uhr deiner Welt. Und eine Eingabe, die so lange wiederholt wird, bis sie gültig ist: die Schuld aus Etappe 2.

**Warum das zählt:** Ab hier ist es kein Skript mehr, sondern ein Spiel. Es wartet auf dich.

**`range()` gehört hierher, nicht als Nebenbemerkung.** Es ist eine der meistgetippten Funktionen in Python überhaupt, und in Etappe 14 läuft dein gesamtes Minenraster darüber.

**Lernziele:**
- Wann `while`, wann `for`?
- Was ergibt `range(5)` genau — welche Zahlen, und warum ist die letzte nicht dabei?
- Was macht `range(2, 10, 3)`?
- Unterschied `break` ↔ `continue`?
- Wie entsteht eine Endlosschleife — und wie kommst du raus? (`Strg+C`)

**Transferaufgabe (10 Min):** Zahlenraten mit „zu hoch"/„zu niedrig". Danach: gib mit `range()` alle geraden Zahlen von 0 bis 20 aus — einmal mit Schrittweite, einmal mit einer Bedingung. Vergleiche, was lesbarer ist.

**Kaputtmachen:** Entferne das `break`. Verschieb `input()` aus der Schleife heraus.

**Commit:** `Etappe 3: Das Spiel läuft`

---

## Etappe 4 — Das Inventar

**Boot.dev:** Listen, `append()`, `remove()`, `len()`, Indexing

**Was du baust:**
`inventar = []`. Befehle `nimm <ding>` und `inventar`. Maximal 10 Gegenstände.

Dazu `ablege <ding>` und eine zweite Liste mit dem, was am Ort herumliegt — ein Gegenstand wandert von der einen in die andere. Und `.split()`, damit Zwei-Wort-Befehle überhaupt möglich werden; in Etappe 5 trägt dasselbe Werkzeug `gehe norden`.

**Erste Fundstücke:** ein halb gegessenes Brot, ein umgestoßener Stuhl (nicht tragbar), ein Schlüssel, der zu keiner Tür im Dorf passt. Der Schlüssel ist der Köder Richtung Mine.

**Lernziele:**
- Warum ist der erste Index 0?
- Was macht `liste[-1]`?
- Was passiert bei `liste[99]`, wenn die Liste 3 Einträge hat?
- **Was verändert `append()` — die Liste selbst, oder gibt es eine neue zurück?**

Die letzte Frage ist der Einstieg in **mutable vs. immutable** — Ursache vieler Bugs, die man nicht versteht:

```python
a = [1, 2]
b = a
b.append(3)
print(a)      # Was steht hier? Warum?

x = "hallo"
y = x
y += " welt"
print(x)      # Und hier? Warum anders?
```

Wenn du diese beiden Blöcke wirklich verstehst, hast du dir Wochen Fehlersuche gespart.

**Transferaufgabe (10 Min):** Liste mit drei Dorfbewohnern. Gib den zweiten aus, dann den letzten ohne `len()`. Häng einen an, entferne den ersten. Dann der eigentliche Punkt: Weis die Liste einer zweiten Variable zu, entferne über die zweite jemanden und gib die erste aus. (Noch ohne Funktion; die kommt in Etappe 7.)

**Kaputtmachen:** `remove()` mit etwas, das nicht drin ist.

---

## Etappe 5 — Die Karte

**Boot.dev:** Dictionaries, verschachtelte Dictionaries, `keys()` / `values()` / `items()`

**Was du baust:**

```python
orte = {
    "dorfplatz": {
        "beschreibung": "...",
        "ausgaenge": {"norden": "schmiede", "sueden": "wiese"}
    },
    "wiese": {
        "beschreibung": "...",
        "ausgaenge": {"norden": "dorfplatz", "westen": "minenpfad"}
    },
}
```

Fünf bis sechs Orte, plus **Wiese** und **Minenpfad**. Dazu `aktueller_ort` als Zustandsvariable (wird in Etappe 10 zu `player.ort`) und Gegenstände, die zum Ort gehören statt zum Spieler.

Der Mineneingang ist verschlossen — dein erster gesperrter Weg. **Und die Design-Entscheidung dazu trägt bis Etappe 13:** Fehlt der Ausgang einfach, oder existiert er und ist markiert? Eine sichtbare verschlossene Tür ist ein Versprechen; eine fehlende Tür ist nichts. Davon hängt ab, ob `world.oeffne_weg()` später eine Zeile oder ein Umbau ist.

**Warum das zählt:** Erster Moment, in dem *Daten* und *Code* auseinanderfallen. Neue Orte, ohne die Logik anzufassen. Merk dir das Gefühl — es kommt in Etappe 25 in voller Größe zurück.

**Lernziele:**
- Warum ist ein Dictionary hier besser als eine Liste?
- Wie kommst du an einen verschachtelten Wert?
- Was passiert bei einem Schlüssel, den es nicht gibt — und was macht `.get()` anders?
- **Was prüft `"dorfplatz" in orte` — Schlüssel oder Wert?** (Das ist ein Stolperstein, über den fast jeder einmal fällt.)
- Was bekommst du beim Iterieren über ein Dictionary?

**Transferaufgabe (15 Min):** Dictionary mit drei NPCs und Alter. Frag einen Namen per `input()` ab und gib das Alter aus — und reagier sauber, wenn der Name nicht existiert. Probier beide Wege: eckige Klammern und `.get()`. (Noch ohne Funktion; die kommt in Etappe 7.)

**Kaputtmachen:** Mach aus `ausgaenge` eine Liste. Lösch einen Ort, auf den ein Ausgang zeigt.

---

## Etappe 6 — Liste, Dictionary, Set, Tuple

**Boot.dev:** Sets, Tuples, Mengenoperationen

**Was du baust:**
Keine neue Funktion — eine bessere Wahl der Werkzeuge.

```python
besuchte_orte = {"dorfplatz", "wiese"}                    # Set: keine Duplikate, keine Reihenfolge
RICHTUNGEN = ("norden", "sueden", "osten", "westen")      # Tuple: unveränderlich
```

Besuchte Orte werden zum Set. Der Befehl `karte` zeigt, wo du warst — und wie viel vom Dorf noch fehlt. Die erste Beschreibung eines Ortes ist länger als jede spätere.

Das Tuple ist bewusst kein Koordinatenpaar: Koordinaten gibt es erst in Etappe 14. `RICHTUNGEN` hat dafür sofort einen Nutzen — damit unterscheidet dein Spiel „das ist keine Richtung" von „hier ist kein Weg".

**Warum eine eigene Etappe:** Die Unterscheidung ist fundamental, und die meisten Anfänger benutzen jahrelang Listen für alles. Ein Set kann nichts doppelt enthalten und beantwortet „ist X drin?" sofort. Ein Tuple sagt dem Leser: *das ändert sich nicht.*

**Das `in`-Experiment — mach es wirklich:**

```python
"Schwert" in meine_liste    # sucht im Inhalt
"Schwert" in mein_set       # sucht im Inhalt, aber viel schneller
"Schwert" in mein_dict      # sucht im SCHLÜSSEL, nicht im Wert
```

Dreimal dasselbe Wort, dreimal etwas anderes. Genau solche Kleinigkeiten trennen „ich habe es abgeschrieben" von „ich weiß, was da steht".

**Lernziele:**
- Wann Set statt Liste? (Zwei Gründe: Duplikate und Geschwindigkeit bei `in`.)
- Warum kann ein Set keine Listen enthalten, aber Tuples schon?
- Was ist an einem Tuple unveränderlich?
- Warum eignen sich Koordinaten besonders für Tuples?

**Transferaufgabe (10 Min):** Zwei Listen mit Gegenständen. Finde ohne Schleife heraus, welche in beiden vorkommen. (Eine Zeile, wenn du das richtige Werkzeug wählst.)

**Kaputtmachen:** Leg eine Liste in ein Set. Ändere ein Tuple.

---

## Etappe 7 — Aufräumen

**Boot.dev:** Funktionen, Parameter, Rückgabewerte, Scope

**Was du baust:**
Nichts Neues. Du zerlegst die unübersichtliche Datei: `zeige_ort()`, `bewege_spieler()`, `zeige_inventar()`, `verarbeite_befehl()`.

**Warum das zählt:** Refactoring — funktionierenden Code umbauen, ohne sein Verhalten zu ändern. Ungefähr die Hälfte dessen, was Entwickler den ganzen Tag tun. Beim ersten Mal fühlt es sich falsch an („es lief doch!").

**Prüfung:** Nach dem Umbau muss sich das Spiel *exakt* wie vorher verhalten.

**Lernziele:**
- Unterschied `return` ↔ `print`?
- Was ist Scope — warum kennt eine Funktion deine äußeren Variablen nicht?
- Was passiert, wenn eine Funktion kein `return` hat?
- Unterschied Parameter ↔ Argument?

**Transferaufgabe (10 Min):** Funktion `berechne_schaden(angriff, ruestung)`. Danach die entscheidende Frage — noch ohne Testframework: **Was muss immer gelten?** Schaden nie negativ? Rüstung 0 heißt voller Schaden? Schreib drei Fälle auf und prüf sie von Hand. Das ist Testdenken, lange bevor du `pytest` anfasst.

**Kaputtmachen:** Ändere eine Variable in einer Funktion und lies sie draußen aus.

**Commit:** `Etappe 7: Refactoring in Funktionen`

---

## Etappe 8 — Bug-Jagd I ⭐

**Kein neues Boot.dev-Thema. Eine eigenständige Fähigkeit.**

**Was du baust:**
Kein Spielfeature, sondern zwei Dokumente: dein eigenes **Debugging-Protokoll** und ein **Fehlertagebuch** mit der wichtigsten Zeile — *wie gefunden*, nicht *was war*.

Davor die Werkzeuge, in dieser Reihenfolge: die drei Fehlertypen als Denkraster, Tracebacks von unten nach oben lesen, Ursache von Symptom trennen, Halbieren statt Durchsuchen, `print()` mit Präfix und `!r`, und der **Debugger** — Breakpoints, Step Over/Into/Out, Variablen-Ansicht, bedingte Breakpoints. Dazu `git diff` als Suchraum-Verkleinerer.

Erst wenn die Werkzeuge sitzen, kommt die Jagd: Der Mentor gibt manipulierten Code zurück, ohne zu sagen wie viele Fehler und wo. Ab hier läuft sie unregelmäßig weiter — du wirst nicht wissen, wann. **Ohne Mentor** funktioniert die Zeitversatz-Variante: zehn Sabotagen aufschreiben, zwei Tage warten, drei davon blind anwenden.

**Warum das zählt:** Debugging wird in fast keinem Kurs unterrichtet, ist aber die Fähigkeit, die bei fremdem Code als einzige trägt. Und Typ 3 — läuft durch, liefert das Falsche — zerstört die schädlichste Anfängerüberzeugung: *„Wenn Python keinen Fehler zeigt, ist mein Programm richtig."*

**Wichtige Abgrenzung:** Debugging ist nicht Fehlerbehandlung. Das eine heißt herausfinden, *warum* sich das Programm falsch verhält; das andere kommt in Etappe 20.

**Lernziele:**
- Die drei Fehlertypen — und warum Typ 3 der gefährlichste ist?
- In welcher Richtung liest man einen Traceback, und welche Zeile sagt was?
- Warum ist die Absturzstelle selten die Fehlerstelle?
- Wann Debugger, wann `print()`?
- Welche vier Angaben gehören in eine gute Fehlerbeschreibung?
- Warum ist „ich habe etwas geändert und jetzt geht es" ein schlechtes Ergebnis?

**Transferaufgabe (10–15 Min):** Ein fremdes Programm mit einem Typ-3-Fehler — eine Funktion verändert die übergebene Liste, obwohl ihr Docstring das nicht ankündigt. Mit dem Debugger finden, erklären, reparieren. Verbindet mutable Objekte aus Etappe 4 mit „Abhängigkeiten sichtbar machen" aus Etappe 7.

**Kaputtmachen:** Acht Trainingsbugs, selbst eingebaut — einer je Fehlertyp, dazu der fast richtige Vergleich (`>=` statt `>`), das vergessene `return`, der Fehler in den *Daten* statt im Code, und zwei Fehler gleichzeitig.

**Commit:** `Etappe 8: Bug-Jagd bestanden`

Damit ist Block 1 abgeschlossen.

---

# BLOCK 2 — Objekte und Zeit

*Boot.dev: „Learn Object Oriented Programming in Python"*
*Ab hier kommen Leseübungen dazu.*

## Etappe 9 — Alles wird zum Objekt

**Boot.dev:** Klassen, `__init__`, Methoden, Attribute

**Was du baust:**
Klasse `Player` mit `name`, `hp`, `ort`. Deine losen Variablen wandern hinein.

**Lernziele:**
- Was ist `self` — und warum steht es überall?
- Unterschied Klasse ↔ Objekt?
- Wann wird `__init__` aufgerufen?
- Unterschied Attribut ↔ lokale Variable in einer Methode?

**Leseübung (5 Min):** Ich gebe dir etwas in dieser Form:

```python
npc = Villager("Mara")

if npc.trust > 5:
    npc.speak("Ich glaube dir.")
else:
    npc.speak("Ich kenne dich kaum.")
```

Du schreibst nichts. Du beantwortest: Was ist `npc`? Woher kommt `trust`? Was macht der Punkt? Wann läuft `speak()`? Was passiert, wenn `trust` genau 5 ist?

**Kaputtmachen:** Lass `self` bei einer Methode weg. Setz `self.hp` nicht in `__init__` und greif später darauf zu.

---

## Etappe 10 — Komposition

**Boot.dev:** Objekte in Objekten, Komposition

**Was du baust:**
Nicht Vererbung — **Komposition.** Ein Spieler *hat* Dinge:

```python
class Player:
    def __init__(self, name):
        self.name = name
        self.inventar = Inventory()
        self.ausruestung = Equipment()
        self.position = (0, 0)
```

`Equipment` verwaltet die Slots: `{"hand": None, "kopf": None, "koerper": None}`

**Hier lernst du `None` richtig.** `None` heißt „hier ist bewusst nichts" — etwas völlig anderes als `0`, `""` oder `False`. Leerer Slot, kein aktiver Dialog, keine Zielposition: alles `None`. Und `if waffe is None:` — nicht `== None`. Kein Stil, echter Unterschied; frag mich danach.

**Warum Komposition vor Vererbung:** Die meisten Einführungen stürzen sich auf Vererbung, weil sie sich spektakulär anfühlt. In echtem Python ist Komposition häufiger, einfacher zu debuggen, flexibler. Wenn du nur eins von beiden wirklich beherrschst, sollte es dieses sein.

**Lernziele:**
- Unterschied „ist ein" ↔ „hat ein"?
- Warum `is None` statt `== None`?
- Was passiert, wenn zwei Spieler versehentlich dasselbe Inventory-Objekt teilen?

**Transferaufgabe (15 Min):** Klasse `Rucksack` mit Kapazität und `hinzufuegen()`, die `True`/`False` zurückgibt. Klasse `Wanderer`, die einen Rucksack besitzt.

**Kaputtmachen:** Gib `Inventory()` als Standardwert in die Parameterliste (`def __init__(self, inv=Inventory())`). Erzeug zwei Spieler. Beobachte. Einer der berühmtesten Python-Stolpersteine — und du verstehst ihn nur, wenn Etappe 4 saß.

---

## Etappe 11 — Vererbung — und die Frage, ob wir sie brauchen

**Boot.dev:** Vererbung, `super()`, Methoden überschreiben

**Was du baust:**
- `Item` → `Weapon`, `Tool`, `Seed`, `Consumable`
- `Entity` → `Player`, `Villager`, `Monster`

Ein Schwert hat Schaden, ein Werkzeug Haltbarkeit, ein Samen eine Wachstumsdauer — alle haben Name und Gewicht. Echte „ist ein"-Beziehung, einer der Fälle, wo Vererbung wirklich passt.

**Die zweite Aufgabe ist die wichtigere:**

> Zehn Minuten, schriftlich: *Brauchen wir hier Vererbung überhaupt?* Was wäre die Alternative? Was gewinnst du, was verlierst du?

Es gibt keine richtige Antwort, die ich dir vorsagen könnte. Aber die Frage zu stellen ist der Unterschied zwischen jemandem, der Syntax kann, und jemandem, der Entscheidungen trifft.

**Lernziele:**
- Was macht `super().__init__()` genau?
- Was passiert, wenn du es vergisst?
- Was heißt „Methode überschreiben"?
- Wann ist Vererbung die falsche Wahl?

**Transferaufgabe (15 Min):** `Fahrzeug` → `Auto`, `Fahrrad`, jeweils mit `beschreibe()` und `super()`.

**Kaputtmachen:** Lass `super().__init__()` weg. Lies den `AttributeError` und überleg, was er dir eigentlich sagt.

**Commit:** `Etappe 11: Item- und Entity-Hierarchie`

---

## Etappe 12 — DER TICK ⭐

**Boot.dev:** Objekte in Schleifen, Zustandsautomaten

```python
class World:
    def tick(self):
        self.zeit += 1
        for npc in self.npcs:
            npc.update(self)
```

Jeder deiner drei NPCs bekommt einen Tagesablauf. Ein Tick läuft bei jedem Spielerbefehl.

**Der Trick aus deiner Prämisse:** In einem *vollen* Dorf sind NPC-Tagesabläufe Hintergrundrauschen. In einem *leeren* Dorf ist jede Bewegung ein Ereignis. Du gehst zum Brunnen, und der Fremde ist nicht da, wo er vorhin war. Deine kleine Besetzung ist nicht nur einfacher zu bauen — sie macht das System *dramatisch wirksamer*.

**Erweiterung:** NPCs merken sich, wo sie waren. „Ich hab dich vorhin am Minenpfad gesehen." Billig zu bauen, enorme Wirkung. Grundlage für Etappe 17.

**Lernziele:**
- Warum bekommt `update()` die Welt übergeben?
- Was ist ein Zustandsautomat — und wo steckt einer in deinem NPC?
- Was passiert, wenn du beim Iterieren über `self.npcs` einen NPC entfernst?

**Transferaufgabe (10 Min):** Klasse `Uhr` mit `tick()`, die Minuten zählt und bei 60 auf die nächste Stunde springt.

**Kaputtmachen:** Ruf `tick()` zweimal pro Befehl auf. Dann gar nicht.

**Commit:** `Etappe 12: Das Dorf lebt`

---

## Etappe 13 — Der magische Samen ⭐

**Boot.dev:** Objektzustand über Zeit, Weltzustand zur Laufzeit ändern

```python
class Plant:
    def update(self, world):
        self.alter += 1
        if self.alter >= self.wachstum_noetig and not self.reif:
            self.reif = True
            world.oeffne_weg("wiese", "osten", "schlucht")
```

Du pflanzt, machst etwas anderes, kommst zurück — und die Welt hat sich ohne dich verändert. Der einfachste mögliche Beweis, dass dein Tick-System funktioniert.

Und `world.oeffne_weg()` ändert das `ausgaenge`-Dictionary **zur Laufzeit**. Deine Karte aus Etappe 5 war statische Daten. Jetzt ist sie lebendiger Zustand.

**⚠️ Hier ist ein Umweg ausdrücklich erwünscht:**

Irgendwann wirst du fragen: *Warum muss die Pflanze eigentlich die ganze Welt kennen?* Ausgezeichnete Frage, sie hat einen Namen (Kopplung), und sie steht nicht im Lehrplan.

**Stell sie trotzdem.** Ab hier lernst du nicht mehr Python, um eine Übungsaufgabe zu lösen — du lernst Python, weil *dein* Programm ein Problem hat. Das ist die stärkste Form des Lernens, die dieses Projekt zu bieten hat.

**Zur „3 Minuten"-Idee:**

- **Tick-Zeit** — wächst pro Spieleraktion. Passt zum Textspiel: Kaffee kochen ändert nichts.
- **Echtzeit** (`time.time()`) — wächst, während du weg bist. Im Textspiel fühlt sich das falsch an.

**Empfehlung: jetzt Tick-Zeit.** Nicht als Kompromiss — in Etappe 27 läuft die Loop mit 60 Bildern pro Sekunde. Dann *ist* ein Tick eine Zeiteinheit, und `wachstum_noetig = 180` sind exakt deine drei Minuten. Ohne eine Zeile neue Wachstumslogik.

**Commit:** `Etappe 13: Die Wiese wächst`

---

## Etappe 14 — Die Mine ⭐

**Boot.dev:** Verschachtelte Listen, 2D-Raster, `range()` über Koordinaten

```python
karte = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", ".", ".", "@", "#"],
    ["#", "#", "#", "#", "#"],
]
```

Position als Tuple `(x, y)`. Bewegung prüft, ob das Zielfeld begehbar ist. Nebel des Krieges: `besuchte_felder` ist ein Set — genau der Fall aus Etappe 6.

**Hier zahlt `range()` aus Etappe 3:**

```python
for y in range(len(karte)):
    for x in range(len(karte[y])):
```

**Kleiner Zusatz, der dir beim Lesen fremden Codes hilft:** Wenn du Index *und* Wert brauchst, ist `enumerate()` die übliche Alternative — `for y, zeile in enumerate(karte):`. Beim 2D-Raster ist `range(len(...))` völlig in Ordnung; du solltest nur beide Formen wiedererkennen.

**Warum eine eigene Etappe:** Bewusst eine *andere* Datenstruktur als das Dorf. Handgeschriebene Orte im Dictionary passen zu einem Dorf mit Charakter. Ein Raster passt zu einem Dungeon, der groß, verzweigt und potenziell zufällig erzeugt ist. Zu wissen, wann welche Struktur passt, trennt Anfänger von Fortgeschrittenen.

**Der spätere Zahltag:** Genau dieses Raster ist das Format, in dem Pygame Tilemaps zeichnet. Deine Mine wird in Etappe 28 zur ersten grafischen Karte — ohne Umbau.

**Lernziele:**
- Bei `karte[y][x]` — welcher Index ist Zeile, welcher Spalte? Warum verwechselt das jeder mindestens einmal?
- Wie prüfst du, ob eine Koordinate überhaupt auf der Karte liegt?
- Warum ist ein Set für besuchte Felder besser als eine Liste?

**Transferaufgabe (15 Min):** 3×3-Raster aus Zahlen. Funktion für die Summe einer Zeile, dann eine für eine Spalte.

**Kaputtmachen:** Vertausch `x` und `y`. Erzeug das Raster mit `[["."] * 5] * 5` und ändere ein Feld — das hängt direkt mit Etappe 4 zusammen.

**Commit:** `Etappe 14: Die Mine`

---

## Etappe 15 — Was in der Mine liegt

**Boot.dev:** Suchen in Datenstrukturen, Zustandsverwaltung

Fundstücke, die Wissen sind, nicht Ausrüstung: ein Fetzen Stoff, ein Grubenbuch mit fehlenden Seiten, Kratzspuren, die nicht von Werkzeug stammen. Jeder Fund setzt ein Flag. Manche Funde ändern, was die NPCs sagen — wenn du den Stofffetzen findest, erkennt die Versorgerin ihn. Vielleicht.

**Erste echte Verzahnung** von Ort, Gegenstand und Dialog. Deine Systeme reden miteinander.

**Erweitern ohne zu zerstören:** Füge einen vierten Fundgegenstand hinzu, **ohne** die Dialoglogik anzufassen. Wenn das nicht geht, ist das eine Erkenntnis über deinen Code — nicht über dein Können.

---

## Etappe 16 — Bug-Jagd II

Gleiches Ritual, größeres System, subtilere Fehler: ein NPC, der sich falsch bewegt; ein Flag, das zu früh gesetzt wird; ein Objekt, das versehentlich geteilt wird.

**Zusatzaufgabe:** Nimm einen der Fehler und schreib in `GELERNT.md`, *wie du vorgegangen bist* — nicht, was der Fehler war.

---

# BLOCK 3 — Die Welt reagiert

*Ab hier wird der Plan bewusst gröber. Das ist Absicht: Dein Spiel wird Fragen erzeugen, die heute niemand kennt, und die haben Vorrang.*

## Etappe 17 — Und dann sind es zwei ⭐

**Boot.dev:** `random`, gewichtete Wahrscheinlichkeiten, Ereigniswarteschlangen

Ein Ereignissystem: Liste möglicher Ereignisse, jedes mit Bedingungen und Wahrscheinlichkeit pro Tick. Meistens Kleinkram — ein Geräusch aus dem Wald, ein Sturm, ein Licht in einem Fenster, in dem niemand wohnt.

Und dann, wenn du zu langsam warst: **Einer der drei ist am nächsten Morgen weg.** Nicht gescriptet — ausgelöst davon, wie viele Ticks vergangen sind, wem du vertraut hast, was du in der Mine gefunden hast.

**Hier zahlt Etappe 1 aus:**

> *„Du erinnerst dich an den Geruch von Brot an diesem ersten Morgen. Jetzt riecht es nach kaltem Rauch."*

Ein Verschwundener von dreien ist ungleich härter als ein Toter von zwölf — und erzeugt Druck, ohne dass du eine Uhr einblenden musst.

**Lernziele:** Unterschied `random.choice` / `random.random` / `random.randint`? Wie gewichtest du Wahrscheinlichkeiten? Warum ist ein fester Seed beim Testen Gold wert?

**Commit:** `Etappe 17: Ereignissystem`

---

## Etappe 18 — Vertrauen

**Boot.dev:** Zustandsverwaltung, Sets, komplexere Boolean-Logik

Ein zentraler `flags`-Speicher (ein Set — jetzt weißt du, warum). Jeder NPC hat einen Vertrauenswert. Dialoge prüfen beides: Was weißt du? Wem hast du es erzählt? Der Fremde erzählt bei hohem Vertrauen etwas anderes als bei niedrigem. Ob es dann stimmt, ist eine andere Frage.

**Neu: Kurzschlussauswertung.** Deine Bedingungen aus Etappe 2 sind erwachsen geworden, und jetzt lohnt sich die Frage, was `and` und `or` eigentlich *zurückgeben*:

```python
name = npc and npc.name          # None, wenn npc None ist — sonst der Name
ziel = gewaehltes_ziel or standardziel
```

Das ist kein Angeber-Python. Du wirst es in fremdem Code ständig sehen, und es soll dann nicht mystisch wirken.

**Lernziele:** Was gibt `a or b` zurück, wenn `a` truthy ist? Warum wird der rechte Teil manchmal gar nicht ausgewertet? Wo ist das gefährlich (wenn `0` ein gültiger Wert ist)?

**Warum drei NPCs hier ideal sind:** Bei zwölf wird die Kombinatorik unbeherrschbar. Bei dreien kannst du jeden Zustand von Hand durchdenken und wirklich *verstehen*, wie ein Konsequenzsystem funktioniert.

---

## Etappe 19 — Speichern und Laden

**Boot.dev:** Datei-I/O, `json`, `pathlib`

Kompletter Weltzustand in eine Datei und zurück — inklusive halb gewachsener Pflanzen, erkundeter Minenfelder, Vertrauenswerte.

**Die wichtigste Einsicht dieser Etappe — und sie ist präziser, als sie klingt:**

JSON ist **nicht** „Python-Objekte in anderer Form". JSON kennt genau sechs Dinge: Text, Zahl, Wahrheitswert, `null`, Liste, Objekt (≈ Dictionary). Deine `Villager`-Instanz ist nichts davon. Ein Set auch nicht. Ein Tuple auch nicht.

Du musst also selbst **entscheiden, wie sich dein Objekt als solche Daten darstellen lässt** — und wie du es daraus wieder herstellst. Das ist eine Design-Entscheidung, keine Übersetzung.

Diese Unterscheidung ist später bei APIs, Datenbanken und Konfigurationsdateien Gold wert. Wer sie nicht macht, wundert sich jahrelang, warum „das Objekt" nicht ankommt.

**Neu dabei: `pathlib`.** Pfade sind kein String-Basteln:

```python
from pathlib import Path
SAVE_DIR = Path("saves")
SAVE_DIR.mkdir(exist_ok=True)
```

**Erweitern ohne zu zerstören:** Erweitere das Speichern so, dass Pflanzen mitgesichert werden — ohne die bestehende Speicherlogik umzuschreiben.

---

## Etappe 20 — Wenn der Spieler Unsinn eingibt

**Boot.dev:** `try` / `except`, eigene Exceptions, Validierung

Kein Absturz mehr. Unbekannte Befehle, volles Inventar, Bewegung in Fels — alles wird abgefangen und erklärt.

**Wichtige Abgrenzung:** Das hier ist Fehler*behandlung*. Debugging (Etappe 8, 16) ist etwas anderes. Fehlerbehandlung heißt: das Programm bleibt stehen statt abzustürzen. Debugging heißt: du findest heraus, warum es sich falsch verhält. Verwechsle die beiden nie.

**Kaputtmachen:** Fang alles mit `except:` ab. Merke, warum das eine schlechte Idee ist — es verwandelt Fehler vom Typ 1 in Fehler vom Typ 3.

---

## Etappe 21 — Kampf

**Boot.dev:** Mehrere Rückgabewerte, Zufall, Zahlenlogik — plus `Enum`

Schaden mit Waffe und Rüstung, Trefferchance, Ausweichen, Abklingzeiten. Rundenbasiert im Text.

**Wo:** In der Mine, nicht im Dorf. Das Dorf bleibt der Ort für Gespräche und Verdacht, die Mine der Ort für Gefahr. Diese Trennung hält beide Systeme sauber — im Code wie im Gefühl.

**Neu: Zustände sauber modellieren.**

```python
from enum import Enum

class GameState(Enum):
    ERKUNDUNG = 1
    DIALOG = 2
    KAMPF = 3
```

`GameState.KAMFP` knallt sofort. `"kamfp"` schleicht sich durch — genau die Sorte Fehler vom Typ 3.

**Warnung:** Kampfbalancing ist ein Loch, in das man wochenlang fällt. Setz dir ein Zeitlimit. **Und mach das auf einem Branch** — der erste Moment, in dem Branches einen echten Zweck haben.

---

## Etappe 22 — Crafting und Anbau

**Boot.dev:** Datengetriebenes Design, Listen von Dictionaries

```python
rezepte = {
    "fackel": {"zutaten": {"holz": 1, "harz": 1}, "zeit": 2}
}
```

Mehrere Samensorten mit unterschiedlichen Wachstumszeiten und Wirkungen. Ein Samen öffnet eine Brücke, ein anderer lockt etwas an, ein dritter zeigt, was vergraben wurde.

**Fast geschenkt:** Wachstum, NPC-Zeitpläne und Ereignisse laufen alle auf demselben Takt aus Etappe 12.

**Erweitern ohne zu zerstören:** Neues Rezept hinzufügen, ohne eine einzige Zeile Logik zu ändern. Wenn das klappt, hast du datengetriebenes Design verstanden.

---

## Etappe 23 — Python wird pythonisch ⭐

**Boot.dev:** Comprehensions, `dataclass`, Typannotationen

Keine neue Spielfunktion. **Und trotzdem die Etappe, die deinem eigentlichen Ziel am direktesten dient.**

Bis hierher lautete die Frage: *Wie schreibe ich etwas?* Ab hier: *Wie lese ich Code, den jemand anders geschrieben hat?* Das ist dein Übergang von „Claude macht Dinge, die ich nicht verstehe" zu „Claude macht Dinge, die ich nachvollziehen und beurteilen kann."

**Comprehensions:**
```python
namen = [npc.name for npc in self.npcs]
lebende = {npc.name: npc for npc in self.npcs if npc.lebendig}
```
*Warnung:* Eine Ebene, nie verschachtelt. Wenn die Comprehension schwerer zu lesen ist als die Schleife, hast du verloren.

**dataclass:**
```python
from dataclasses import dataclass

@dataclass
class Item:
    name: str
    gewicht: int
    wert: int
```
Die Brücke zwischen „ich verstehe Klassen" und „ich verstehe, wie professioneller Python-Code aussieht".

**Typannotationen:**
```python
def finde_npc(self, name: str) -> Villager | None:
```
**Ehrliche Einordnung:** Python *prüft* das zur Laufzeit nicht. Es ist Dokumentation, die dein Editor lesen kann — keine Typsicherheit. Genau deshalb ist es für dich wichtig: Die Signatur sagt dir sofort, was rein- und rausgeht.

**Nur zur Kenntnis:** `*args` und `**kwargs` bedeuten „beliebig viele weitere Argumente". Du wirst darüber stolpern. Mehr musst du vorerst nicht wissen.

**Leseübung (15 Min):** Ich gebe dir ein Stück Code aus einem unserer alten Vibe-Coding-Projekte. Du erklärst mir, was es tut. Das ist der eigentliche Test dieses ganzen Lehrplans.

---

## Etappe 24 — Das Projekt wird zum Projekt (Code + Git)

**Boot.dev:** Module, Imports, Paketstruktur — passend zum Git- und Linux-Kurs

Aufteilung in mehrere Dateien, zum Beispiel `world.py`, `entities.py`, `items.py`, `events.py`, `mine.py`, `commands.py`, `main.py`.

**Ausdrücklich: Das ist ein Vorschlag, kein Standard.** Deine Struktur darf anders aussehen, solange du **begründen kannst, warum**. Was du hier lernen sollst, ist nicht „professioneller Python-Code hat sieben Dateien mit diesen Namen", sondern:

> Ich teile ein Programm in Module auf, wenn es dadurch verständlicher und wartbarer wird.

Wenn du beim Aufteilen merkst, dass zwei Dateien ständig voneinander importieren, ist das ein Signal — dann gehören sie vielleicht zusammen, oder es fehlt eine dritte.

**Der Git-Teil, den wir aufgeschoben haben:** Branches, Merges, Pull Requests, Merge-Konflikte — und wie man einen absichtlich herbeiführt, um zu sehen, wie er aussieht. Erst jetzt, weil du erst jetzt einen Grund hast.

---

## Etappe 25 — Inhalt raus aus dem Code ⭐

**Boot.dev:** JSON als Content-Format, Laden zur Laufzeit

Alle Dialoge, NPCs, Items, Orte, Ereignisse und Minenebenen wandern nach `content/`. Der Code lädt sie beim Start.

**Warum das für dich besonders zählt:** Ab hier kannst du an deinem Spiel *schreiben*, ohne zu programmieren. Und genau hier kommen die verschwundenen Dorfbewohner zurück: Einen NPC hinzuzufügen ist kein Code mehr, sondern ein JSON-Eintrag. Dein Dorf kann von drei auf zwanzig wachsen, ohne dass du die Spiellogik anfasst. **Das ist der Moment, in dem deine Prämisse ihre Schuld einlöst.**

---

## Etappe 26 — Tests

**Boot.dev:** `pytest`

Jetzt formalisierst du, was du seit Etappe 7 nebenbei gemacht hast. Tests für das, was stillschweigend kaputtgeht: Schadensberechnung, Inventar-Limits, Rezeptprüfung, Speichern/Laden, Wachstumszeiten.

**Und hier schließt sich der Kreis zum übergreifenden Prinzip:** Tests sind das, was „erweitern ohne zu zerstören" von einer Hoffnung in eine Gewissheit verwandelt. Beim ersten Test, der einen Fehler findet, den du nicht bemerkt hattest, verstehst du das körperlich.

**Bug-Jagd III, umgekehrt:** Ich baue einen Fehler ein, und du schreibst zuerst einen Test, der ihn *nachweist*, bevor du ihn behebst.

---

# BLOCK 4 — Grafik

*Erst starten, wenn Block 1–3 stehen. Wirklich.*

## Etappe 27 — Pygame: Das erste Fenster

Fenster, Spielschleife mit Bildrate, ein Rechteck mit Pfeiltasten.

**Entscheidend:** Deine gesamte Logik bleibt unverändert. Pygame ist nur eine neue *Darstellung*. Wenn du sauber gearbeitet hast, fasst du `world.py` fast nicht an. Das ist der Beweis, dass die Architektur stimmt.

**Und hier wird die 3-Minuten-Idee wahr:** Die Loop tickt 60-mal pro Sekunde. `wachstum_noetig = 180` sind exakt drei Minuten Echtzeit.

## Etappe 28 — Kacheln, Sprites, Kamera

Tilemap für Dorf und Mine, animierte Figuren, eine Kamera, die dem Spieler folgt. Deine Minenkarte aus Etappe 14 ist bereits im richtigen Format.

## Etappe 29 — Isometrie

Umrechnung von Karten- auf Bildschirmkoordinaten, Zeichenreihenfolge nach Tiefe. Mathematisch der anspruchsvollste Teil. Zu diesem Zeitpunkt bist du ein anderer Programmierer als heute.

---

## Warum hier Schluss ist

Der Bogen steht: Grundlagen → Datenstrukturen → Funktionen → Debugging → OOP → Komposition → Vererbung → Zeit und Zustand → Dateien → Fehlerbehandlung → Zustandsmodellierung → datengetriebenes Design → modernes Python → Module → Tests → Grafik.

Weitere Themen hineinzupressen würde den Plan verbessern und das Projekt verschlechtern. Ab Etappe 17 ist er bewusst grob — und das ist keine Lücke, sondern die eigentliche Absicht.

Denn wenn du an diesem Punkt sagst:

> *„Ich glaube, meine Datenstruktur ist falsch."*
> *„Warum brauche ich diese Klasse eigentlich?"*
> *„Hier hängt zu viel voneinander ab."*

…dann ist dieses Problem selbst die nächste Lektion. Und dann brauchst du keinen Lehrplan mehr.

---

## Was du am Ende hast

Ein spielbares RPG: ein leeres Dorf, drei Überlebende, eine Mine voller Hinweise, eine Wiese, auf der Dinge wachsen, während du weg bist, Entscheidungen mit Nachhall — und ein Verschwinden, das nicht gescriptet ist, sondern passiert.

Dazu ein öffentliches Repo mit hunderten Commits. Und der eigentliche Punkt: Du wirst fremden Python-Code lesen und beurteilen können, statt ihm zu vertrauen.

---

## So arbeiten wir

Bring mir pro Etappe:
1. Was du bauen willst, in eigenen Worten
2. Deinen Code
3. Was nicht klappt

Ich gebe Hinweise, Erklärungen, Reviews. Wenn du nach fertigem Code fragst, frage ich zurück, was du schon probiert hast.

**Ich nehme die Lernziele ernst.** Wenn du sagst „Etappe 5 ist fertig", frage ich dich die Fragen. Nicht als Prüfung — das Erklären *ist* der Lernvorgang. Du lernst am besten, wenn du etwas selbst machen und wiederholen musst: Die Transferaufgaben sind das Machen, die Lernziele das Wiederholen, die Leseübungen das, was am Ende zählt.

An Tagen ohne Energie: `GELERNT.md` öffnen, die letzten drei Einträge lesen. Das zählt auch.
