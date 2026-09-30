# Der Bogen — Register aller Vorausverweise

*v3.21.0 · 2026-09-30*

> Verbindlicher Anhang zum [Lehrplan](Vorposten_Lehrplan.md). Das Gegenstück dazu ist [`SYNTAX.md`](SYNTAX.md), das Register der Werkzeuge: Der Bogen führt Buch über Versprechen zwischen Etappen, das Syntaxregister darüber, welches Werkzeug ab wann zur Verfügung steht. Diese Datei ist die einzige Quelle der Wahrheit für alles, was eine frühe Etappe verspricht und eine späte einlösen muss.

---

## Wozu es diese Datei gibt

Der Lehrplan verspricht ständig etwas: *„Diese Variable brauchst du in Etappe 17."* — *„Das Raster wird in Etappe 29 zur Tilemap."* Diese Versprechen sind der Grund, warum sich das Projekt wie ein Bogen anfühlt und nicht wie 30 Übungsaufgaben.

Aber sie sind auch eine Schuld. Wenn Etappe 17 kommt und dort nichts eingelöst wird, war das Versprechen eine Behauptung.

Diese Datei ist die Buchführung darüber. Sie hat drei Adressaten:

**Dich.** Wenn du bei Etappe 12 sitzt und dich fragst, warum du in Etappe 6 ein Set statt einer Liste genommen hast, steht die Antwort hier.

**Mich.** Ich habe kein verlässliches Langzeitgedächtnis über Monate. Wenn du bei Etappe 17 ankommst, weiß ich nicht mehr zuverlässig, was ich in Etappe 2 versprochen habe — ich würde es rekonstruieren, und Rekonstruktion ist Raten mit gutem Ruf. Verweis mich bei jeder späten Etappe auf diese Datei, dann rate ich nicht.

**Jeden, der den Guide liest.** Das Register macht sichtbar, dass die Struktur Absicht ist.

**Regel:** Wer einen neuen Vorausverweis in eine Etappe schreibt, trägt ihn hier ein. Ohne Ausnahme. Ein Verweis, der nicht im Register steht, existiert nicht.

**Zur Statusspalte:** `offen` heißt, dass die Ziel-Etappe noch nicht geschrieben ist — kein Rückstand, sondern der Normalfall. Die Spalte füllt sich, während die Guides entstehen.

**Zwei Dinge muss man beim Lesen wissen:**

**1. Vierzehn Etappen sind in Portionen geteilt** — 3, 7, 9, 11, 12, 13, 14, 15, 17, 18, 19, 20, 21, 23. **Sieben davon haben drei Portionen** — 3 (3a Schleife, 3b Befehle, 3c Kampf und Anzeige), 11, 14, 17 (17a Zufall, 17b der Seed, 17c zwischen den Wellen), 18 (18a Statuseffekte, 18b Skillpunkte, 18c Fähigkeiten wirken), 19 (19a Dateien und JSON, 19b Objekte werden Daten, 19c das Spiel überlebt das Beenden) und 20 (20a Fangen, 20b Werfen, 20c Prüfen und trennen) —, die übrigen zwei. Die **Nummern sind unverändert**, deshalb bleibt jeder Verweis in diesem Register gültig. Wo es für die Buchführung einen Unterschied macht, steht die Portion dabei (`7b`, `14a`, `17b`). Ein Verweis auf **7** ohne Buchstaben meint die Etappe als Ganzes.

**2. Es gibt drei Anspruchsstufen** — 🔨 bauen, 🧠 verstehen, 👀 nur erkennen. Das ist für den Bogen keine Kosmetik, sondern ändert, *was eine Schuld überhaupt bedeutet*:

> Eine Schuld auf Stufe 👀 ist eingelöst, wenn der Lernende die Sache **wiedererkennt und in einem Satz erklärt**. Sie verlangt keinen Code. Wer sie behandelt, als müsste etwas gebaut werden, bläht die Ziel-Etappe auf.

Betroffene Einträge sind mit 👀 markiert.

---

## Teil A — Was gepflanzt wird

Chronologisch nach Etappe. Spalte „Status": `offen` = noch nicht eingelöst, `eingelöst` = der Guide der Ziel-Etappe ist geschrieben und löst die Schuld dort tatsächlich ein.

### Etappe 0 — Das Repo

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `pip`, venv, `requirements.txt` | **24** — `pyproject.toml` als Gegenstück; **28** — Pygame installieren | offen |
| Die Paketliste gehört zum Projekt | **24** — Abhängigkeiten deklarieren statt einfrieren | offen |
| `.gitignore` und was nicht ins Repo gehört | **19** — `saves/`; **24** — Build-Artefakte | **teilweise eingelöst** ✓ (19a, Schritt 1 — `saves/`) |
| `GELERNT.md` als Ort für Entscheidungen | durchgehend — jede Design-Entscheidung landet dort | offen |

### Etappe 1 — Der Abwurf

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `letzte_meldung` als Variable statt als Satz | **17** — die Aufzeichnung ist achtzehn Tage alt | **eingelöst** ✓ (17c — der Funkkontakt spielt sie ab) |
| `kern_integritaet` (angelegt, noch ohne Wirkung) | **3a** — Abbruchbedingung, inklusive Knobelstelle ✓; **17** — Vergleich mit dem Startwert | **eingelöst** ✓ (3a; 17c — Wellenbericht in Prozent von `KERN_START`, der Riss kommt nur unter der Hälfte) |
| ⭐ **Zwei Verlustbedingungen nebeneinander** — `kern_integritaet` (die Basis) und `trefferpunkte` (die eigene Figur) | **3a** — beide beenden den Lauf, zwei Prüfungen statt einer; **9a** — `trefferpunkte` wandert in den Marine, `kern_integritaet` bleibt bei der Welt; **13** — der eigene Ausfall bekommt einen Respawn-Zähler | **eingelöst** ✓ (13) |
| **Die Namensfalle dazu:** zwei Gesundheitswerte, die nie verwechselt werden dürfen | **5** — dort steht die Regel für gleichlautende Namen; **16** — Kandidat für die Bug-Jagd | offen |
| `wellen_bis_evakuierung` als feste Zahl | **3a** — `range(1, 21)` ✓; **17** — der Wellengenerator skaliert daran | **eingelöst** ✓ (3a; 17a — die letzte Welle bekommt das doppelte Budget) |
| Prinzip: Weltzustand speichern, nicht nur ausgeben | **12** — der gesamte Tick beruht darauf | **eingelöst** ✓ (12) |
| „Name zeigt auf Wert" statt „Behälter" | **4** — Aliasing: `b = a` und beide ändern sich ✓; **10** — dasselbe an eigenen Objekten, dort als **Objektidentität** benannt ✓ | **eingelöst** ✓ (4, 10) |
| `=` als „bekommt den Wert" lesen | **2** — Abgrenzung zu `==` | offen |
| Die Klassenwahl als Zahl aus `input()` | **2** — bestimmt die Startwerte **der gewählten Klasse**; **11** — wird zur Klassenhierarchie | **eingelöst** ✓ (11b) |
| **Der Dreisatz: `input()` gibt Text → `int()` macht eine Zahl → erst damit wird gerechnet** | **5** — die Mengenabfrage beim Kaufen ✓; **20** — `ValueError` wird abgefangen | **eingelöst** ✓ (5; 20a — `ValueError` gefangen) |
| Regel: *woher* ein Wert kommt, bestimmt, was vor der Benutzung passieren muss | **19** — geladene Daten sind nicht das, was gespeichert wurde; **25** — Content von außen ist nie vertrauenswürdig | **teilweise eingelöst** ✓ (19a, Konzept 5 — *beim Laden ist nichts automatisch das, was du gespeichert hast*) |
| `int()` kann mit `ValueError` scheitern | **20** — echte Fehlerbehandlung | **eingelöst** ✓ (20a, Schritt 2 und 3) |
| Sprachentscheidung Variablennamen (de/en) | durchgehend — Konsistenz bis 30; **23** fremden Code lesen; **25** Namen werden JSON-Schlüssel | offen |
| **Schreibweise: GROSS für feste Werte, klein für veränderlichen Zustand** — heute nur die Regel, im eigenen Code gibt es noch keinen festen Wert | **4** — `BAHNLAENGE` ist der erste ✓; **5** — `WAREN`, `VERKAUFSWERTE`, `STAPELBAR`, `ANZEIGENAMEN` sind die ersten Tabellen ✓; **6** — `KLASSEN`, `AUSBAUTEN`, `GEGNERTYPEN`, `STAPELBAR` als Set ✓; **9** — Klassennamen groß, Objektnamen klein | **teilweise eingelöst** ✓ (4, 5, 6) |
| **Darstellung: fester ASCII-Kopf, mehrzeiliger String** | **3c** — Balken kommen dazu ✓; **7b** — wandert in `zeichne_kopf()` ✓ | **eingelöst** ✓ |
| Autorenregel: die Zahlen zeigen die Lage, nicht der Text | durchgehend — Grund, warum dieses Setting wenig Prosa braucht | offen |

### Etappe 2 — Der erste Kontakt

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `if`/`elif`-Kette für Klassenwerte (bewusst ertragen) | **11** — die Kette stirbt, Klassen übernehmen | **eingelöst** ✓ (11b) |
| `meldung_abgesetzt = True/False` | **17** — wirkt mit, welcher Sektor fällt; **18** — geht im Flag-Set auf | **eingelöst** ✓ (17c — Nachschubgewicht 40 statt 20; in der Kür, Schritt 22, zusätzlich beim Sektorfall; 18b — geht in `welt.flags` auf, reiner Umbau mit `diff`) |
| Verknüpfte Bedingungen (`and`/`or`/`not`) | **18** — Freischaltungen prüfen mehrere Voraussetzungen | **eingelöst** ✓ (18b/18c — die Voraussetzungen werden bewusst **keine** `and`-Zeile, sondern eine Prüfkette mit Grund: Konzept 11 löst damit die Erkenntnis aus 2 ein, dass eine verknüpfte Bedingung nicht sagt, welcher Teil scheiterte; 18a, Schritt 7 holt die Feuerbedingung aus 2 als Vergleich hervor) |
| 👀 Grenze des Booleans: nur zwei Zustände (benannt, nicht ausgebaut) | **12** — Status als String; **21b** — `Enum` für benannte Zustände | **teilweise eingelöst** ✓ (12) |
| Truthy/Falsy — besonders `0` (**eine Regel, nicht die volle Liste**) | **4** — `if inventar:`, die leere Liste ist falsy ✓; **10** — `None` ≠ `0`, beide falsy ✓; **18** — als Gefahr bei Munition und Zählern | **eingelöst** ✓ (4, 10; 18b — die `or`-Falle bei `0`, Konzept 12 und Kaputtmachen) |
| 👀 `and`/`or` geben mehr zurück als `True`/`False` (zwei Zeilen im Terminal, kein Bauauftrag) | **18** — dort als Lesestoff eingelöst; **23b** — in fremdem Code | **teilweise eingelöst** ✓ (18b, Konzept 12 — als Lesestoff, mit Bauverbot) |
| ⚠️ **`trefferpunkte` (Marine) und `kern_integritaet` (Anlage) sind zwei Werte** — beide 100, deshalb die häufigste Verwechslung des Fundaments | **3c** — die Gegner schlagen auf die Anlage, nicht auf den Marine; **11** — jeder der vier Marines bekommt eigene Trefferpunkte; **12** — beide ticken unabhängig | **teilweise eingelöst** ✓ (12) |
| **`klassengeraet`** — ein String pro Klasse (Sturmgewehr, Schweres MG, Multiwerkzeug, Bio-Injektor), der angezeigt und nie abgefragt wird | **18** — wird zur Wurzel der Klassenfähigkeit; **22** — wird zur Spalte `klasse` in der Fähigkeitentabelle. **Sperren: 4 ✓, 5 ✓, 10 (Datei noch ungeschrieben), 13 (Datei noch ungeschrieben)** | **teilweise eingelöst** ✓ (18b — die Spalte `"geraet"` in `FAEHIGKEITEN` wird gegen `klassengeraet` verglichen; ⚠️ **Abweichung:** sie heißt `"geraet"`, nicht `klasse`, weil sie das Gerät nennt und nicht die Python-Klasse — **22** übernimmt sie unter diesem Namen oder benennt sie begründet um) |
| ⚠️ **Das Klassengerät ist Identität, kein Besitz** — steht in keinem Depot, kostet kein Vaporium | **4** — gehört nicht ins Inventar ✓; **5** — die Warentabelle führt es ausdrücklich nicht, mit Begründung ✓; **10** — das Ausrüstungs-Objekt ist etwas anderes und heißt anders | **eingelöst** ✓ (4, 5) |
| **Die Klassentabelle mit markiertem Bezugsfall** (Soldat als Anker, drei Klassen relativ dazu) | **11** — wird zu vier Python-Klassen; **21a** — der Bezugsfall wird balanciert, die anderen relativ nachgezogen; **22** — sind das nicht eigentlich Daten? | **teilweise eingelöst** ✓ (11b) |
| `nachladen_noetig` als echter Boolean, zusammen mit `ziel_in_sicht` in **einer** `and`-Bedingung | **12** — Einheiten bekommen eigene Zustände; **18** — geht in der Voraussetzungsprüfung auf | **eingelöst** ✓ (18a, Schritt 7 — gelöscht; die Frage wird am Magazinstand gestellt) |
| **`ziel_in_sicht`** — bleibt bis 14b immer `True`, in 3c ausdrücklich so benannt | **14b** — bekommt seine Bedeutung: ein Gegner ist in Reichweite; auch der eigene `feuern`-Befehl prüft ab dort die Reichweite ✓ | **eingelöst** ✓ (14b) |
| ⚠️ **Nach der Meldung im `else`-Zweig stürzt die Werteanzeige mit `NameError` ab** — im Guide als Termin benannt, wie `zwei` in Etappe 1 | **3a** — Schritt 2b legt die Klassenwahl in `while True:` mit `break`, eine ungültige Eingabe führt zu einer neuen Frage ✓ | **eingelöst** ✓ (3a) |
| **Das Lagebriefing steht hinter der Klassenwahl**; die Trefferpunkte-Zeile aus Etappe 1 wird ersetzt, nicht verdoppelt | **9a** — dort gibt es den Marine erst nach der Klassenwahl, und das Briefing liest aus ihm | offen |
| **Erkenntnis: eine verknüpfte Bedingung sagt nicht, welcher Teil scheiterte** | **20** — die ganze Etappe über brauchbare Fehlermeldungen | **eingelöst** ✓ (18b — Prüfkette mit Grund; 20b — jeder Grund wird ein eigener `SpielFehler`) |
| `elif` ≠ mehrere `if` | **17** — mehrere Ereignisse treffen gleichzeitig zu | **eingelöst** ✓ (17c — Ereignistopf mit einzelnen `if`, Ausführung mit `elif`; Kaputtmachen 7) |
| Der `else`-Zweig für Unerwartetes | **20** — `try`/`except` statt Auffangbecken | **eingelöst** ✓ (20b — ⚠️ **Präzisierung:** der `else`-Zweig der Befehlskette bleibt und wirft einen `SpielFehler` mit eigenem Satz; `try`/`except` ersetzt ihn nicht, sondern fängt, was er wirft) |
| `.strip()` auf Eingaben — **`.lower()` erst in 3a**, weil hier Zahlen eingegeben werden | **3a** ✓; **4** — mit `.split()` ✓; **7a** — die ganze Aufbereitung wohnt in `verarbeite_befehl()` ✓ | **eingelöst** ✓ |
| 👀 Punkt-Schreibweise (`wert.methode()`) — ein Satz: *gehört zu* | **9a** — `einheit.melde()` bei eigenen Objekten | offen |
| Die vier Klassen als festes Personal (erzählerisch, noch nicht im Code) | **11** — Klassenhierarchie; **22** — die Frage, ob sie Daten sein sollten | **teilweise eingelöst** ✓ (11b) |
| **Nur die gewählte Klasse bekommt Werte** — die `if`/`elif`-Kette wählt genau einen Zweig | **11** — dort entstehen alle vier Objekte gleichzeitig | **eingelöst** ✓ (11b) |
| `print()`-Debugging als Reflex | **8** — der Debugger als bessere Variante | **eingelöst** ✓ |
| Design-Entscheidung: welche Klasse ist der Bezugsfall | **21** — gegen sie wird balanciert | offen |

### Etappe 3 — Die Wellenschleife ⭐  *(3a Schleife · 3b Befehle · 3c Kampf und Anzeige)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **3a:** `for` über die Wellen, `while` über die Runden | **12** — jeder Rundendurchlauf löst einen Tick aus | **eingelöst** ✓ (12) |
| **3a: Die Hauptschleife selbst** | **28** — wird zur Pygame-Loop mit 60 fps | offen |
| **3a:** Zwei Schleifenebenen, also zwei Einrückungstiefen | **14a** — die Doppelschleife über das Raster | **eingelöst** ✓ (14a) |
| **3a:** `range()` | **14a** — Schleifen über das Vorfeldraster | **eingelöst** ✓ (14a) |
| **3a:** `range()` zählt ab 0, die zweite Zahl ist ausgeschlossen | **4** — derselbe Grund, warum der erste Listenindex 0 ist ✓; **8** — Off-by-One als eigene Fehlerkategorie | **eingelöst** ✓ |
| **3a:** `break` beim Wellenende | **20** — die Abbruchbedingungen werden validiert | **entfällt** für 20 — die Abbruchbedingungen werden nicht validiert, sondern bleiben Spielregeln; geprüft wird in 20c nur, was eine Invariante ist |
| ⭐ **3a: Knobelstelle — Abbruch von innen nach außen** (erste Aufgabe ohne gezeigtes Verfahren) | **12** — dieselbe Frage beim Beenden des Ticks; **19** — dort wird vor dem Beenden gespeichert | **teilweise eingelöst** ✓ (19c, Schritt 23 — vor dem Aussteigen wird gespeichert) |
| **3a:** `while True:` mit `break` als Bauform für Schleifen ohne bekannte Länge | **3b** — die zweite Bauform mit Zustandsvariable wird danebengestellt ✓; **12** — die Zustandsvariable trägt ab dort die Hauptschleife | **teilweise eingelöst** ✓ (3b) |
| **3c:** `//` und `%` (heute ungebraucht, neben `/` eingeführt) | **7b** — im Beispiel zu mehreren Rückgabewerten; **14a** — Zeile und Spalte aus einem Index | offen |
| **3a:** `Strg + C` als Notausgang, einmal absichtlich benutzt | **8** — gehört zum Werkzeugkasten der Bug-Jagd | **eingelöst** ✓ |
| 👀 **3a:** `continue` und `_` (im Wegwerf-Skript gesehen, nicht im Spiel gebaut) | **23a** — dieselben Denkfiguren in Comprehensions | offen |
| **3b:** `.lower()` auf der Eingabe — Einlösung aus **2** | **4** — mit `.split()` ✓; **7a** — wohnt in `verarbeite_befehl()` ✓ | **eingelöst** ✓ |
| **3b:** Lange `elif`-Kette der Befehle (bewusst ertragen) | **7a** — wandert in `verarbeite_befehl()` ✓; **23a** — stirbt durch das Befehls-Dictionary | **teilweise eingelöst** ✓ (7a) |
| **3b:** `else`-Zweig für unbekannte Befehle | **5** — wächst um `umsehen`, `gehe`, `depot`, `kaufe` ✓; **20** — wird echte Fehlerbehandlung | **eingelöst** ✓ (5; 20b) |
| **3b: Design-Entscheidung Befehlssprache** (heute einwortig, bewusst) | **4** — der Umbau auf Verb + Ziel findet statt, und er wird als Erfahrung ausgewertet ✓; **5** — `kaufe medkit` und `gehe norden` ✓; **25** — Befehle als Content | **teilweise eingelöst** ✓ (4, 5) |
| **3b:** Befehl `beenden` (Schreibweise als Entscheidung festgelegt) | **19** — dort wird vor dem Beenden gespeichert | **eingelöst** ✓ (19c, Schritt 23) |
| **3b: Design-Entscheidung — welche Befehle kosten eine Runde?** (Auskunft kostet nichts, Handlung schon) | **12** — dieselbe Frage als „welche Spieleraktion löst einen Tick aus?"; **13** — Bauzeit läuft nur bei vergehender Zeit; **21a** — erst dadurch wird Nachladen eine echte Wahl | **teilweise eingelöst** ✓ (12, 13) |
| **3a: Drei Ebenen für Variablen** (vor den Schleifen · pro Welle · pro Runde) ⭐ | **7a** — dort heißt das Verhalten *Scope* ✓; **12** — Weltzustand gehört der Welt | **teilweise eingelöst** ✓ (7a) |
| **3a: Zwei Abbruchbedingungen — `kern_integritaet` *und* `trefferpunkte`** — Einlösung aus **1** und **2** | **13** — nur eine der beiden bekommt einen Respawn-Zähler; ab dort beendet **nur noch der Kern** den Lauf | **eingelöst** ✓ (13) |
| **3a: Entwicklerbefehle sind erlaubt und werden am Ende entfernt** | **3c** — eigener Aufräumschritt; **8** — sie wären sonst Verdächtige bei der Fehlersuche | **eingelöst** ✓ |
| **3c: `nachladen_noetig` bekommt endlich einen Wert** — Einlösung aus **2** | **18** — zwei Werte, die dasselbe sagen, sind eine Fehlerquelle | **eingelöst** ✓ (18a — gelöscht) |
| ⭐ **3c: `erfahrung` — ein Zähler, der beim Kill steigt** (heute nur eine Zahl in der Anzeige, ohne Wirkung) | **5** — die Stufenschwellen kommen als Dictionary dazu; **9a** — wird Attribut des Marine; **13** — „Erfahrung bis zur nächsten Stufe" ist dasselbe Zählermuster wie ein Cooldown; **18** — Stufen zahlen Skillpunkte aus | **eingelöst** ✓ (13; 18b — jede Stufe zahlt einen Skillpunkt, Schritt 13) |
| **3c: Zwei Werte für dieselbe Aussage** (`munition > 0` und `nachladen_noetig`) | **18** — Zustandsverwaltung; **16** — Kandidat für die Bug-Jagd | **eingelöst** ✓ (18a, Schritt 7 und Konzept 4 — abgeleitet statt gespeichert) |
| **3c: Was aus Zustand entsteht, wird beim Anzeigen erzeugt, nicht aufbewahrt** (Balkenlänge) | **4** — dasselbe für die Anmarschbahn ✓; **7b** — die Rechnung wohnt in `zeichne_balken()` ✓; **28** — 60-mal pro Sekunde | **teilweise eingelöst** ✓ (4, 7b) |
| **3b: Wo eine Variable angelegt wird, entscheidet, wann sie neu gesetzt wird** ⭐ | **7a** — dort bekommt das Verhalten den Namen *Scope* ✓; **12** — Weltzustand gehört der Welt | **teilweise eingelöst** ✓ (7a) |
| **3b:** Rundenzähler mit `+=` | **12** — wird zu `self.zeit`, der Weltzeit | **eingelöst** ✓ (12) |
| **3c:** Anzahl Gegner hängt an der Wellennummer (**Formel vom Lernenden selbst gewählt**) | **17a** — wird zum Budget-System | **eingelöst** ✓ (17a) |
| **3c:** Platzhalter-Kampfformel (fester Schaden) | **7a** — wird zu `berechne_schaden()` ✓; **21a** — wird zum System | **teilweise eingelöst** ✓ (7a) |
| **3c:** Nachladen kostet eine Runde, Nachschauen nicht (erste echte Spielentscheidung) | **13** — dasselbe Muster als Bauzeit; **21a** — Teil des Balancings | **teilweise eingelöst** ✓ (13) |
| **3c:** Notizliste „was fühlt sich falsch an" | **21a** — Grundlage des Balancings | offen |
| **3c: Darstellung: Balken statt Zahlen** | **4** — die Anmarschbahn kommt daneben ✓; **7b** — wandert in `zeichne_balken()` | **teilweise eingelöst** ✓ (4) |
| **3c: `trefferpunkte_max`** — der Startwert der gewählten Klasse, gleich nach der Klassenwahl festgehalten; gegen ihn misst der Trefferpunkte-Balken | **9a** — wandert mit den übrigen Marine-Werten; **13** — derselbe Wert trägt den Respawn, kein zweiter Name ✓ | **teilweise eingelöst** ✓ (13) |
| **3c:** Balken zeigt ungültige Werte sichtbar an — **und soll sie nicht begrenzen** | **8** — Typ-3-Fehler an der Darstellung erkennen | **eingelöst** ✓ |
| 👀 **3c:** Formatangabe im f-String (`:.0%`) | **9b** — `__repr__` formatiert Objekte; durchgehend beim Lesen | offen |

### Etappe 4 — Ausrüstung und Beute

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| Mutable vs. immutable | **10** — geteiltes `Inventar()`-Objekt und der veränderbare Standardwert ✓; **14a** — `[["."] * 5] * 5` | **teilweise eingelöst** ✓ (10) |
| **Zwei Namen können auf dasselbe Objekt zeigen** (`b = a`) | **10** — als Objektidentität benannt, mit `is` nachweisbar ✓; **16** — Bug-Kandidat | **teilweise eingelöst** ✓ (10) |
| `.copy()` als bewusste Kopie | **10** — die Alternative zum geteilten Objekt ✓ | **eingelöst** ✓ (10) |
| `inventar` als Liste von Strings | **11** — wird zur Liste von `Item`-Objekten | **eingelöst** ✓ (11c) |
| **Zwei identische Gegenstände sind nicht unterscheidbar** („welches Medkit?") | **11** — genau deshalb werden aus Strings Objekte | **eingelöst** ✓ (11c) |
| Obergrenze 10 Gegenstände | **20** — „Inventar voll" als abgefangener Fall | **eingelöst** ✓ (20b, Schritt 8) |
| Index ab 0 — Einlösung aus **3a** | **14a** — `vorfeld[y][x]`, und `>= len(...)` in der Randprüfung | **eingelöst** ✓ (14a) |
| **Einen Eintrag über den Index ersetzen** (`liste[i] = wert`) | **6** — dasselbe an zwei parallelen Listen, dort mit `.pop(i)` daneben; **14a** — jedes Feld des Rasters wird so gesetzt; **23a** — dieselbe Absicht als List Comprehension | offen |
| `len()` | **14a** — `range(len(vorfeld))`, und `len(r[y])` statt `len(r[0])` | **eingelöst** ✓ (14a) |
| `for` über eine Sammlung statt über `range()` | **12** — der Tick läuft über Trupp und Gegner; **14a** — dieselbe Schleife über ein Raster | **teilweise eingelöst** ✓ (12) |
| ⭐ **Gegner = Positionszahl** — die Liste ist der Zustand, das `"K"` gehört nur in die Darstellung | **11** — aus der Zahl wird ein Objekt mit HP und Typ ✓; **12** — das Objekt tickt ✓; **14a** — aus `entfernung` werden `x` und `y` ✓; **19** — dieser Zustand wird gespeichert | **eingelöst** ✓ (11, 12, 14a; 19b — Gegner stehen mit Position, Trefferpunkten und Effekten im Spielstand) |
| Gegnerliste der laufenden Welle — **keine Zählvariable mehr, `len()` ist die Anzahl** | **12** — wird zu `welt.gegner`. ⚠️ **Abweichung von der ursprünglichen Vorgabe:** Es entsteht **keine** gemeinsame `einheiten`-Liste. Der Tick läuft über `trupp` und `gegner` getrennt, weil eine gemeinsame Liste beim Zeichnen und bei der Zielsuche wieder die Typfrage erzwingen würde, die **11** gerade abgeschafft hat. Die Design-Entscheidung steht im Guide zu 12. | **eingelöst** ✓ (12) |
| **Feste Bahnlänge `BAHNLAENGE = 12`** — ein Gegner auf Feld 11 rückt nicht weiter vor, bleibt vor dem Tor stehen und macht weiter Schaden | **11a** — die Umrechnung von Position in `entfernung` rechnet gegen sie ✓; **12** — das Stehenbleiben bleibt in `Gegner.update()` erhalten ✓; **14a** — auf dem Raster betritt der Gegner das Torfeld selbst und macht dort Schaden ✓ | **eingelöst** ✓ (11a, 12, 14a) |
| **Rundenkosten jedes neuen Befehls** — ab `nimm` und `ablege` entscheidet der Lernende selbst (Auskunft oder Handlung) und notiert es in `GELERNT.md` | **5, 6, 11** — dieselbe Frage bei jedem neuen Befehl ✓; **12** — die Notizen werden zur Antwort, welche Aktion einen Tick auslöst ✓ | **teilweise eingelöst** ✓ (5, 6, 11, 12) |
| **Die Bahn wird jede Runde neu erzeugt, nicht verändert** | **7b** — `zeichne_bahn()` ✓; **14a** — dasselbe für das Raster; **28** — dasselbe 60-mal pro Sekunde | **teilweise eingelöst** ✓ (7b) |
| 👀 **Zuweisen an die Schleifenvariable ändert die Liste nicht** (`for pos in gegner: pos += 1` bewegt nichts) | **11** — ab dort *kann* man den Eintrag über die Schleifenvariable ändern, weil er ein Objekt ist | **eingelöst** ✓ (11a) |
| ⚠️ **`range(len(...))` nur bei echtem Indexbedarf** — sonst `for ding in liste` | **14a** — dort ist der Indexbedarf echt | **eingelöst** ✓ (14a) |
| **Liste nie verändern, während man darüber läuft** (Typ-3-Fehler) | **12** — als echtes Problem beim Tick; **16** — Kandidat für die Bug-Jagd | **teilweise eingelöst** ✓ (12) |
| `in` bei einer Liste | **6** — Gegenüberstellung Liste / Set / Dictionary | offen |
| `remove()` scheitert an fehlendem Element | **20** — wird zu `try` / `except` | **eingelöst** ✓ (20b, Schritt 8 — ⚠️ **Abweichung:** geprüft mit `in`, nicht gefangen; Konzept 5 begründet es) |
| **Umzug zwischen zwei Listen: erst prüfen, dann anfassen** | **20** — der Kerngedanke der Fehlerbehandlung | **eingelöst** ✓ (20b, Schritt 8 — jedes `raise` vor der ersten Veränderung) |
| `.split()` für Zwei-Wort-Befehle | **5** — `kaufe medkit` und `gehe norden` ✓; **7a** — wohnt in `verarbeite_befehl()` ✓ | **eingelöst** ✓ |
| Befehl ohne zweites Wort (`nimm` allein) | **20** — wird sauber abgefangen | **eingelöst** ✓ (20b, Schritt 8) |
| **Design-Entscheidung 1: Kennung oder Anzeigename?** | **5** — das Depot ist die zweite Stelle, und die Entscheidung wird dort ausdrücklich nachgeprüft ✓; **11** — `item.id` / `item.name`; **25** — die Kennung wird JSON-Schlüssel | **teilweise eingelöst** ✓ (5) |
| **Design-Entscheidung 2: Ist die Bahn der Zustand oder nur sein Bild?** ⭐ — **der Plan legt sich hier fest: Positionen sind der Zustand** | **12** — nur ein eigenständiger Zustand lässt sich ticken ✓; **14a** — Riegel 2 macht die Entscheidung endgültig ✓; **19** — nur Zustand wird gespeichert; **28** — nur so bleibt die Logik grafikfähig | **teilweise eingelöst** ✓ (12, 14a; 19a, Konzept 1 — Zustand, Inhalt, Bild: nur Zustand wird gespeichert) |
| **Die Frage „Menge oder mehrere unterscheidbare Dinge?"** (Munition bleibt eine Zahl) | **6** — dieselbe Frage für vier Strukturen; **25** — welche Inhalte werden JSON | offen |
| Vaporium als Währung | **5** — der Kaufvorgang, und Vaporium wandert in den `vorrat` ✓; **22** — Kosten in den Tabellen | **teilweise eingelöst** ✓ (5) |
| Mengen lassen sich mit Listen schlecht führen (mehrmals `"vaporium"`) | **5** — das `vorrat`-Dictionary löst das ✓ | **eingelöst** ✓ |
| Der Datenkern der Brut (heute nutzlos) | **15** — wird zur ersten Erkenntnis | **eingelöst** ✓ (15) |
| ⚠️⭐ **Grundsatz: Aus der Brut fällt nichts, was ein Mensch anlegen kann** — kein Vaporium, keine Munition, keine Panzerplatte. Beute ist Rohstoff plus Rätsel | **5** — die Panzerplatte ist reine Depotware ✓; **17a** — auch seltene Beute bleibt biologisch; **25** — gilt für fremden Content | **teilweise eingelöst** ✓ (5; 17a — die seltensten Einträge in `BEUTE` sind die Funde aus 15, und auch sie sind Brut) |
| **Typspezifische Beute** — heute fällt bei jedem Gegner dasselbe; ein Speier soll später eine **Säuredrüse** hinterlassen, ein Kriecher nicht | **6** — dort entstehen die Gegnertypen, an die sich Beute hängen kann; **17a** — Zahltag: Typen bekommen Gewichte, Beute wird typgebunden | **eingelöst** ✓ (17a — `BEUTE`, die Säuredrüse fällt beim Speier; die Tabelle *Gegnertyp → Fundkennung* aus 15 geht darin auf) |
| 💡 **Seltene Beute als Werkstoff** — ein *perfekt erhaltener* Chitinpanzer, aus dem sich eine **Chitinpanzerplatte** herstellen lässt (besser als die gekaufte Panzerplatte) | **17a** — er setzt Gewichte voraus, vorher gibt es keine Seltenheit. **Das Herstellen selbst braucht die Werkstatt aus 13** — und weil 13 vor 17a liegt, ist die Reihenfolge zu klären, bevor das gebaut wird | **Idee, nicht terminiert** — 17 bietet das Fallen als Kür unter „Wenn du mehr willst" an, das Herstellen bleibt offen |
| ⭐ *(Kür)* Der untersuchbare Datenkern — eine Zeile, die nichts auflöst | **15** — dort wird sie aufgelöst; der Guide fängt den Fall ab, dass die Kür damals entfiel | **eingelöst** ✓ (15) |
| **Darstellung: die Anmarschbahn als eine Zeile** ⭐ | **7b** — wandert in `zeichne_bahn()` ✓; **14a** — `zeichne_bahn()` wird **gelöscht** und durch `zeichne_vorfeld()` ersetzt ✓ | **eingelöst** ✓ (7b, 14a) |
| Gegnerposition ↔ Zeichen an dieser Stelle (zwei Dinge) | **14a** — Riegel 2: das Raster hält Gelände, Einheiten haben eigene Koordinaten | **eingelöst** ✓ (14a) |
| Darstellung als Debugging-Werkzeug | **8** — sichtbare Fehler statt gelesener; **16** — Reihenfolgefehler im Tick | **teilweise eingelöst** ✓ (8) |
| **Reihenfolge: zeichnen vor oder nach dem Bewegen?** (Kaputtmach-Experiment 6) | **16** — daraus wird eine eigene Bug-Jagd; **12** — die Tick-Phasen | **teilweise eingelöst** ✓ (12) |
| **Baureihenfolge: ein Gegner → mehrere → entfernen** (drei Schritte, nicht einer) | **8** — genau dieses Halbieren ist das Suchverfahren; **14a** — dieselbe Staffelung beim Raster | **teilweise eingelöst** ✓ (8) |
| 👀 **`dir()` und `help()` — ein Objekt selbst befragen** (in **4** an `.count()` geübt, ohne dass die Lösung daran hängt) | **9b** — dieselbe Technik an eigenen Klassen; **24** — eine fremde Bibliotheks-API lesen; **27** — die zwei Werkzeuge vor einem fremden Repo | offen |
| `.join()` — Liste zu einer Zeile | **7b** — lebt jetzt in `zeichne_bahn()` ✓; **14a** — jede Rasterzeile entsteht so | **teilweise eingelöst** ✓ (7b) |
| ⭐ *(Kür)* Beute per Nummer nehmen — der Spieler zählt ab 1, Python ab 0 | **8** — Off-by-One als eigene Fehlerkategorie | **eingelöst** ✓ |

### Etappe 5 — Der Vorposten und das Depot

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **Material über `nimm`: Gezähltes in den `vorrat`, Einzelstücke ins Inventar** — entschieden über `kennung in vorrat`, ohne Materialnamen in der Logik | **15** — die Einsammelphase benutzt dieselbe Regel ✓; **17a** — ein neues Material ist nur ein `vorrat`-Eintrag | **eingelöst** ✓ (15; 17a — die Säuredrüse ist drei Dateneinträge, keine Zeile Logik) |
| **Dictionary = Zuordnung Schlüssel → Wert** (zuerst an einem Nicht-Spiel-Beispiel) | **19** — genau diese Form ist JSON; **25** — Content-Format | **teilweise eingelöst** ✓ (19a, Konzept 4 und 5) |
| `sektoren` als verschachteltes Dictionary | **13** — wird zur Laufzeit verändert | **eingelöst** ✓ (13) |
| `WAREN` als flaches Dictionary | **22** — bekommt Kosten, Voraussetzungen, Ausbaustufen | offen |
| Die Wahl flach ↔ verschachtelt als bewusste Entscheidung | **14a** — Dict oder Raster; **19** — Struktur ↔ Dateiformat | **teilweise eingelöst** ✓ (19a — die Karte geht nicht ganz in den Spielstand, nur ihre veränderlichen Teile) |
| Trennung Daten ↔ Code | **25** — Inhalt wandert komplett nach `content/` | offen |
| **Entscheidung: versiegelter Sektor fehlt oder ist markiert** — **empfohlen ist „fehlt"**; bei „markiert" bekommt der Sektor ein zweites flaches Dictionary (Richtung → Grund) und `gehe` drei Fälle statt zwei | **13** — bestimmt, wie `raeume_frei()` gebaut wird (beide Varianten sind im Guide ausgeführt); **18** — Zustand mit Bedingung ist dasselbe Muster | **eingelöst** ✓ (13; 18b — dieselbe Frage *ausblenden oder sichtbar lassen* für Fähigkeiten, die man noch nicht lernen kann) |
| **Entscheidung: ausverkaufte Ware fliegt raus oder bleibt mit Bestand 0** | **22** — bestimmt, wie leicht Ausbaustufen einzubauen sind | offen |
| Die Landeplattform als unerreichbarer Ort | **13** — wird freigeräumt; **17** — dort landet das Evakuierungsschiff | **eingelöst** ✓ (13; 17c — die Siegmeldung nennt die Landeplattform) |
| `aktueller_sektor` als Zustandsvariable | **9** — wird zu `marine.sektor`; **19** — Teil des Speicherstands | **eingelöst** ✓ (19b, Schritt 12 — Teil des Spielstands) |
| `in` prüft beim Dict den **Schlüssel** | **6** — Gegenüberstellung Liste/Set/Dict | offen |
| Verschachtelte Struktur (Dict im Dict) | **19** — genau diese Form ist JSON; **25** — Content-Format | **teilweise eingelöst** ✓ (19a) |
| Schlüssel müssen immutable sein | **6** — warum ein Set keine Listen aufnimmt | offen |
| `.get()` für sicheren Zugriff — **eckige Klammern, wenn Fehlen ein Bug wäre; `.get()`, wenn es der Normalfall ist** | **20** — die leichtere Alternative zu `try` / `except` | **eingelöst** ✓ (20a, Konzept 5 — prüfen oder fangen) |
| Tippfehler **links vom `=`** legt still einen Eintrag an; Tippfehler beim **Lesen** stürzt ab | **8** — Typ-3-Fehler erkennen; **25** — Schlüssel aus fremden Dateien | **teilweise eingelöst** ✓ (8) |
| `.items()` zum Iterieren | **12** — über alle Einheiten laufen | offen |
| Zuweisung ändert die Karte zur Laufzeit | **13** — `welt.raeume_frei()` ist genau diese Zeile | **eingelöst** ✓ (13) |
| Der Kaufvorgang prüft drei Bedingungen | **20** — drei Bedingungen werden drei Exceptions | **eingelöst** ✓ (20b — drei Gründe, drei Sätze, ein `SpielFehler`) |
| **Größe** eines Dictionaries nicht ändern, während man iteriert (Werte ändern ist erlaubt) — Python knallt hier, wo eine Liste still das Falsche tut | **12** — dasselbe bei Einheiten | **eingelöst** ✓ (12) |
| Fehlerklasse „inkonsistente Daten" — **zwei Stufen: Richtung fehlt (wird abgefangen) gegen Zielname fehlt (stürzt trotz Prüfung ab)** | **25** — bei externem Content die häufigste Fehlerart | offen |
| **Invarianten: Welche Bedingungen müssen bei meinen Daten immer stimmen?** (aufgeschrieben, **nicht** geprüft) | **25** — dieselben Sätze gegen fremden Content; **26** — sie werden zu Tests | offen |
| **Richtung ≠ Ziel ≠ Standort** — drei Werte, die man leicht verwechselt | **9** — das Objekt kennt seinen eigenen Standort; **14a** — Koordinate gegen Feldinhalt | offen |
| **Der Kauf als Transaktion: erst alle Prüfungen, dann verändern** — Einlösung aus **4** | **20** — der Kerngedanke der Fehlerbehandlung; **19** — halb geschriebener Spielstand | **eingelöst** ✓ (19a, 19c; 20a, Schritt 3; 20b, Schritt 8) |
| **Der Architekturtest: Daten ändern, Logik nicht anfassen** ⭐ (hinzufügen **und löschen**) | **22** — derselbe Test mit den Tabellen; **25** — derselbe Test mit JSON-Content | offen |
| **Umbenennen bricht Verweise, ohne dass Python warnt** | **24** — dasselbe bei Modulnamen; **25** — bei Content-Schlüsseln; **26** — ein Test würde es finden | offen |
| **Darstellung: statischer Grundriss mit Markierung** (handgezeichnet, **nicht** aus den Daten erzeugt) | **7b** — wandert in `zeichne_grundriss()` ✓; **29** — wird zur Kulisse | **teilweise eingelöst** ✓ (7b) |
| **`vorrat` als Dictionary Name → Anzahl** (Vaporium und Munition verlassen die losen Variablen) | **22** — Kosten werden gegen denselben Vorrat geprüft; **19** — Teil des Speicherstands | **teilweise eingelöst** ✓ (19b — Teil des Spielstands) |
| **Trennung Menge ↔ Einzelstück** (`vorrat` gegen `inventar`) — Einlösung aus **4** | **6** — dieselbe Frage für vier Strukturen; **11** — Einzelstücke werden Objekte | offen |
| **Begriffstrennung Depot / Vorrat / Inventar** (Katalog · Ressourcen · Einzelstücke) | durchgehend — ab hier benutzt der Plan die drei Wörter konsequent; **22** — Tabellen sind ein zweiter Katalog | offen |
| **`STAPELBAR` als zweite flache Tabelle neben `WAREN`** — zwei parallele Dictionaries mit denselben Schlüsseln | **22** — dort werden sie zu **einer** verschachtelten Tabelle zusammengezogen; **25** — als JSON-Objekt pro Ware | offen |
| **Der Kauf kennt keine Warennamen** ⭐ (Preis wird nachgeschlagen statt abgefragt) | **22** — die Tabellen funktionieren nach demselben Prinzip; **23a** — dieselbe Ablösung für die Befehlskette; **25** — Content aus JSON | offen |
| ⭐ **Die Bedingung dafür: Es geht nur ohne Logikänderung, wenn *alles* in den Daten steht, was die Logik fragt** | **22** — dort scheitert es, wenn eine Eigenschaft fehlt; **25** — die Frage an jedes JSON-Feld; **26** — Tests prüfen die Vollständigkeit | offen |
| **Ein Befehl hängt zum ersten Mal vom Ort ab** (`kaufe` nur im Depot) | **13** — `raeume` nur am Osttor; **14b** — Reichweite als Ortsbedingung | **teilweise eingelöst** ✓ (13) |
| `int()` beim Kauf einer Menge — Einlösung aus **1** | **20** — `ValueError` bei `drei` statt `3` wird abgefangen | **eingelöst** ✓ (20a, Schritt 3 — dazu die negative Menge) |
| Der Wirtschaftskreislauf schließt sich (Brut → Material → verkaufen → Vaporium → kaufen → Munition → Brut) | **21a** — Balancing hat ab hier einen Kreislauf zu balancieren | offen |
| ⭐ *(Kür)* Die Werkbank, an der nichts geht | **13** — dort wird der **Basisturm** an ihr in Auftrag gegeben; die Werkstatt bekommt damit ihren ortsgebundenen Befehl. *Entfällt, wenn die Kür entfällt.* | **eingelöst** ✓ (13) |
| ⭐ **`integritaet` pro Sektor** — ein Wert, der sich zur Laufzeit ändert **und** nach dem Laden noch stimmen muss | **11 (Konzept)** — das Beispiel für veränderlichen Laufzeitzustand; **5 (Kür)** — Sektoren nehmen einzeln Schaden, `repariere` hebt sie; **17c (Kür, Schritt 22)** — ein Sektor kann endgültig fallen; **19** — muss in den Spielstand, anders als die Beschreibungen | **teilweise eingelöst** ✓ (19a, Schritt 5 und 8 — die veränderlichen Teile jedes Sektors stehen im Spielstand, die Beschreibung nicht) |
| ⚠️⭐ **Der Kern wechselt die Rolle: von einer Zahl (seit 1) zu einem Ort (ab 5) — und bleibt beides** | **9a** — `kern_integritaet` bleibt draußen, wenn die Werte in den Marine ziehen; **12** — sie bekommt ihr Zuhause in der `Welt`, der Sektor bleibt bei der Karte | **eingelöst** ✓ (9a, 12) |
| ⚠️ **Der Sektor `"kern"` bekommt *keine* eigene `integritaet`** — sonst zwei Zahlen für denselben Reaktor | **5 selbst** — Konzept 0, Auftragsschritt 1 und 3, Selbsttest ✓; **12** — dort wird sichtbar, wem welcher Wert gehört | **eingelöst** ✓ (5) |
| ⭐ **Ungleichmäßige Daten sind der Normalfall** — ein Eintrag mit anderen Schlüsseln als die übrigen, und `.get()` bekommt dadurch seinen ersten echten Anlass | **20** — fehlende Schlüssel werden abgefangen statt umgangen; **25** — bei fremdem Content die Regel, nicht die Ausnahme | **teilweise eingelöst** ✓ (20a, Schritt 4 — `KeyError` beim Laden, mit der Grenze zu **25**) |
| ⭐ **Brut-Material als Beute** (`chitinpanzer`, `organ`) — **kein Vaporium, keine Munition im Vorfeld** | **5** — wird zur gezählten Ressource und über `verkaufe` zu Vaporium ✓; **21a** — der Kreislauf ist die Balancing-Grundlage | **eingelöst** ✓ (5) |
| ⭐ **Der Wirtschaftskreislauf hat vier Stationen** (Material → verkaufen → Vaporium → kaufen) — nicht zwei | **21a** — ein Kreislauf lässt sich balancieren, eine Einbahnstraße nicht; **22** — Kaufpreis und Verkaufswert wandern in **eine** verschachtelte Tabelle | offen |
| ⚠️ **Begriffsfalle: `STAPELBAR` ist eine Angabe für den *Kaufvorgang*, keine Eigenschaft der Welt** — Material wird gestapelt, steht aber nicht in der Tabelle; der Datenkern ist Beute, aber nicht zählbar | **6** — die Frage „gezählt oder einzeln?" für vier Strukturen; **22** — beim Zusammenzug der Tabellen muss die Unterscheidung erhalten bleiben | offen |
| **`int()` beim Verkauf einer Menge** — dieselbe Form wie beim Kauf, drittes Mal | **20** — `ValueError` wird abgefangen | **eingelöst** ✓ (20a, Schritt 3) |
| ⭐ **Nachladen ist eine Verschiebung, keine Quelle** — `geladen` (im Magazin) und `vorrat["munition"]` (im Rucksack) sind zwei Zahlen für zwei Dinge; ihre **Summe steigt beim Nachladen nie** | **12** — dieselbe Trennung von Zustand und Ereignis, systematisch; **20** — die Invariante wird geprüft; **26** — sie wird ein Test | **teilweise eingelöst** ✓ (20c, Schritt 11 — die Invariante als `assert` im Nachladen) |
| ⚠️ **Das Loch, das Etappe 5 selbst aufreißt:** Ab dem Moment, in dem Munition kaufbar wird, ist das alte `nachladen` aus Etappe 3 ein Cheat, der den Wirtschaftskreislauf entwertet | **5 selbst** — Auftragsschritt 12b schließt es ✓ | **eingelöst** ✓ (5) |
| 💡 **Magazingröße je Klasse** — Idee des Lernenden, bewusst vertagt | **21a** — dort ist Balancing erlaubt; vorher eine Zahl ohne Lerninhalt, die Etappe 2 rückwirkend anfasst. *(Nicht zu verwechseln mit dem Großmagazin aus **6**: das hebt `magazin_groesse` für alle Klassen gleich und fasst Etappe 2 nicht an.)* | **Idee, nicht terminiert** |
| ⭐ **`ANZEIGENAMEN` als flache Namenstabelle** — Kennung → schöner Name, nachgeschlagen mit `.get(kennung, kennung)`; sie kennt **auch die unverkäuflichen Dinge** (Datenkern), deshalb steht der Name nicht bei der Ware | **11c** — `Item` trägt Kennung und Name zusammen, die Tabelle entfällt; **22** — alle Tabellen werden eine verschachtelte | offen |
| ⚠️ **Vier flache Tabellen mit fast demselben Schlüsselsatz** (`WAREN`, `VERKAUFSWERTE`, `STAPELBAR`, `ANZEIGENAMEN`) — ein neuer Gegenstand braucht bis zu vier Einträge | **22** — Zahltag: ein Eintrag pro Ding. **Das ist geplante Not**, dieselbe Bauart wie die parallelen Gegnerlisten aus 6 | offen |
| **`VERKAUFSWERTE` als zweite flache Tabelle neben `WAREN`** — die Verkaufslogik kennt keine Materialnamen | **22** — mit `WAREN` und `STAPELBAR` zu einem Eintrag pro Ding zusammengezogen; **25** — als JSON | offen |
| ⭐ *(Kür)* Sektoren nehmen einzeln Schaden | **17c** — ein Sektor kann endgültig fallen. *Entfällt, wenn die Kür entfällt.* | **eingelöst** ✓ (17c — als Kür, Schritt 22) |
| ⭐ **Die Stufentabelle** (`{1: 0, 2: 120, 3: 300}`) — ein Dictionary, das eine Schwelle nachschlägt statt sie abzufragen | **9a** — die Stufe wird beim Marine berechnet; **18** — jede Stufe zahlt einen Skillpunkt; **22** — die Tabelle wandert zu den übrigen Zahlentabellen; **25** — nach `content/` | **teilweise eingelöst** ✓ (18b — jeder Stufenaufstieg zahlt einen Skillpunkt, `level` ist Voraussetzung in `kann_lernen()`) |
| **Die Schwellen bleiben bewusst grob** (glatte Zahlen, kein Feintuning) | **21b** — Balancing bekommt einen eigenen Branch und findet erst dort statt | offen |

### Etappe 6 — Liste, Dictionary, Set, Tuple

**⭐ Hier werden Gegnertypen eingeführt.** Bis Etappe 5 ist ein Gegner eine Positionszahl und alle sehen gleich aus. Ab hier hat jeder einen Typ — als **zweite, parallele Liste** neben den Positionen, über den Index verbunden. Das ist bewusst unbequem und die tragende Begründung für Etappe 11.

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `freigeschaltet` als Set | **18** — wird zum zentralen Flag-Speicher | **eingelöst** ✓ (18b — geht in `welt.flags` auf, zusammen mit `erkenntnisse` und `meldung_abgesetzt`) |
| **Das Set ist die Spielregel, nicht die Prüfung** | **18** — Freischaltungen; **22** — Voraussetzungen | **teilweise eingelöst** ✓ (18b) |
| ⭐ **Ein Set garantiert den Zustand, nicht den Vorgang** — die Prüfung vor dem Abbuchen bleibt nötig | **18** — dieselbe Prüfung mit Voraussetzungen; **20** — aus der Prüfreihenfolge wird Fehlerbehandlung | **teilweise eingelöst** ✓ (18b; 20b — die Prüfreihenfolge wird zu `SpielFehler`n vor der Veränderung) |
| `AUSBAUTEN` als Katalog (Kennung → Preis) — zweiter Katalog nach `WAREN` aus **5** | **18** — Voraussetzungen kommen als Dateneintrag dazu; **22** — Kosten, Bauzeit, Ausbaustufen | **teilweise eingelöst** ✓ (18b — `AUSBAU_VORAUSSETZUNG` als eigene Umkehrtabelle neben dem Katalog; der Zusammenzug ist **22**) |
| `"zielhilfe"` — eine Freischaltung ohne Wirkung | **18** — sie bekommt dort eine Fähigkeit | **eingelöst** ✓ (18b — ⚠️ **Abweichung:** sie wird **keine Fähigkeit**, sondern ein **gekauftes Passiv** — `aktuelle_reichweite()` gibt dem Helden ein Feld mehr. Eine Fähigkeit, die Vaporium freischaltet, bräche Verbot 2 der Machtquellen; ein gekaufter Zahlenwert ist erlaubt. Dazu ist sie die Voraussetzung des Schnellfeuers) |
| ⚠️ **`.index()` als Brücke vom Wert zur Stelle** — ohne es bleiben zwei parallele Listen nicht synchron zu halten; **Lücke, in v1.8.0 geschlossen** | **11** — mit Objekten entfällt der Umweg, Position und Typ sitzen zusammen; **14a** — Index im Raster | **eingelöst** ✓ (6, Konzept 0) |
| `"schnellfeuer"` — zwei Schuss in einer Runde, passiver Ausbau für alle Klassen | **18** — dort ist der **Durchschlag** des Heavy etwas anderes: ein Schuss auf mehrere Ziele in einer Reihe, als Fähigkeit mit Abklingzeit. Die Abgrenzung dort ausdrücklich benennen, sonst liest sie sich wie eine Wiederholung | **eingelöst** ✓ (18b — braucht ab jetzt die Zielhilfe; 18c, Konzept 16 — Abgrenzungstabelle Schnellfeuer gegen Durchschlag, Lernziel 17) |
| ⚠️ **Die Ausbauten aus 6 wirken über Munition und Gegnerzahl, nicht über Schaden** — der Schadenswert aus **2** hat bis **11** keinen Verbraucher, weil ein Gegner mit einem Treffer fällt | **11** — Gegner bekommen eigene Trefferpunkte, ab da wirkt Schaden überhaupt ✓; **21a** — die Formel | **teilweise eingelöst** ✓ (11b) |
| `KLASSEN` als Tuple | **11** — die Klassenhierarchie; **20** — Eingabe validieren | **teilweise eingelöst** ✓ (11b; 20a — die Klassenwahl fängt `ValueError`) |
| Tuple als unveränderliche Liste (`KLASSEN`) — **ohne Koordinaten-Vorgriff** | **10** — `self.position` als Tuple, ohne Wirkung ✓; **14a/b** — `(x, y)` als Set-Eintrag und als `welt.tor` ✓ | **eingelöst** ✓ (10, 14a, 14b) |
| Tuple als Dictionary- und Set-Element | **14b** — Koordinaten in einer Menge | **eingelöst** ✓ (14b) |
| Die Komma-Falle: `(5)` ist kein Tuple, `(5,)` schon | **21a** — Rückgabe zweier Werte; **16** — Kandidat für die Bug-Jagd | offen |
| Tuple-Unpacking (`for a, b in ...`) | **12** — über Einheiten und ihre Zustände laufen | offen |
| 👀 Mengenoperationen (`&`, `\|`, `-`) | **18** — „welche Voraussetzungen fehlen noch?" | **eingelöst** ✓ (18b, Konzept 10 — `-` hochgestuft auf 🔨; `&` und `\|` bleiben 👀) |
| Set für abgedeckte Felder | **14b** — Reichweite von Turm und Kameraden | **eingelöst** ✓ (14b) |
| Sets und Tuples lassen sich nicht als JSON speichern | **19** — Design-Entscheidung beim Speichern | **eingelöst** ✓ (19a, Konzept 5 und 6; 19b, Konzept 12 — `sorted()`, `set()`, `tuple()`) |
| Unterscheidung „kein gültiges Wort" ↔ „hier nicht möglich" | **20** — dieselbe Trennung bei allen Befehlen | **eingelöst** ✓ (20b, Schritt 8 — zwei verschiedene Sätze) |
| „Modellierungsentscheidung" als Begriff | **14a** — Dict oder Raster; **19** — Struktur ↔ Dateiformat | **teilweise eingelöst** ✓ (19a und 19b — zwei Design-Entscheidungen zum Dateiformat und zu Verweisen) |
| **Die Entscheidungshilfe: vier Fragen, feste Reihenfolge** | durchgehend ab hier — jede Strukturwahl bis **25** | offen |

**Gegnertypen — die Einträge dazu:**

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| ⭐ **`GEGNERTYPEN` als verschachteltes Dictionary** (Kennung → langer und kurzer Text) | **15** — Erkenntnisse hängen sich **daneben**, nicht hinein: der Katalog bleibt unverändert, die dritte Menge `erkenntnisse` steht neben `gesehene_gegnertypen` ✓; **17a** — dieselben Einträge bekommen Kosten; **25** — wandert nach `content/` | **teilweise eingelöst** ✓ (15, 17a) |
| ⭐ **`gegner_typen` als zweite Liste parallel zu `gegner`**, über den Index verbunden | **11** — beide Listen kollabieren zu **einer** Liste von Objekten | **eingelöst** ✓ (11a) |
| ⭐ **Der Schmerz paralleler Listen** — beim Entfernen muss an **zwei** Stellen derselbe Index getroffen werden; `remove()` nach Wert trägt nicht mehr | **11** — genau dieser Schmerz ist die Begründung für Objekte; **16** — Kandidat für die Bug-Jagd | **teilweise eingelöst** ✓ (11a) |
| **`.pop(i)` und `del liste[i]` — über die Stelle entfernen statt über den Wert** — Einlösung aus **4** (Index schreiben) | **11** — eine Liste von Objekten braucht denselben Griff; **14a** — Felder des Rasters gezielt leeren | offen |
| **Eine Liste über den Index aufbauen** (die Stelle entscheidet, was hineinkommt) | **14a** — jede Rasterzeile entsteht so; **17a** — der Wellengenerator ersetzt die feste Regel; **23a** — dieselbe Absicht als Comprehension | **teilweise eingelöst** ✓ (17a) |
| Entfernen über den **Index** statt über den Wert (`pop`), rückwärts oder mit gesammelten Indizes | **11** — entfällt, weil ein Objekt eine Sache ist; **12** — dasselbe Problem im Tick | **eingelöst** ✓ (11, 12) |
| `gesehene_gegnertypen` als Set | **15** — `erkenntnisse` ist dieselbe Bauform, dritte Menge derselben Familie ✓; **25** — Gegnertypen kommen aus JSON | **teilweise eingelöst** ✓ (15) |
| Erstbegegnung ausführlicher als jede spätere | **15** — dritte Stufe: nie gesehen ↔ gesehen ↔ analysiert | **eingelöst** ✓ (15) |
| Wellenzusammenstellung als `if`/`elif` über die Wellennummer | **17a** — der Budget-Generator ersetzt die Kette | **eingelöst** ✓ (17a) |
| Die Anmarschbahn zeigt **verschiedene Zeichen je Typ** | **14a** — dieselbe Zuordnung Typ → Zeichen im Raster; **29** — Typ → Kachel | offen |
| `bestiarium` als Auskunftsbefehl, kostet keine Runde — Anwendung aus **3b** | **12** — welche Spieleraktion löst einen Tick aus | **eingelöst** ✓ (12) |
| Unterscheidung „Typ existiert nicht" ↔ „Typ noch nie gesehen" | **20** — dieselbe Trennung als Fehlerbehandlung | **teilweise eingelöst** ✓ (20b — über die Fahndung, falls `bestiarium` ein zweites Wort nimmt) |
| **Invariante zwischen zwei Sammlungen** — jeder Eintrag in `gesehene_gegnertypen` ist Schlüssel in `GEGNERTYPEN` | **20** — daraus wird eine Prüfung; **26** — daraus wird ein Test | **teilweise eingelöst** ✓ (20c, Schritt 11) |
| ⭐ **Die zweistufige Invariante der parallelen Listen** — (1) `len()` beider ist gleich, (2) **für jeden Index beschreiben beide denselben Gegner**. Nur Stufe 1 ist messbar. | **11** — beide entfallen, weil es eine Liste gibt; **20** — Stufe 1 wird eine Prüfung; **26** — ein Test | **eingelöst** ✓ (11a — beide Listen entfallen; 20 hat nichts mehr zu prüfen) |
| ⭐ **Der Index ist die Identität des Gegners** — eine Verbindung, die nirgends geschrieben steht | **11** — die Identität wandert ins Objekt und wird sichtbar | **eingelöst** ✓ (11a) |
| **Das Wellentypen-Set bestimmt nicht die Reihenfolge** — welche Typen erlaubt sind, ist eine andere Frage als welcher Gegner wo entsteht | **17a** — der Generator trifft beide Entscheidungen getrennt | **eingelöst** ✓ (17a — `"ab_welle"` entscheidet, was kommen kann, der Generator, wer entsteht; `wellen_typen` wird aus der Namensliste gebaut) |
| **Drei Mengen, drei Fragen:** `GEGNERTYPEN` (was existiert) · Wellentypen (was kann kommen) · `gesehene_gegnertypen` (was kenne ich) | **17a** — eine vierte kommt dazu: was ist im Budget leistbar; **20** — die Meldungen unterscheiden die Mengen | **teilweise eingelöst** ✓ (17a; 20b — die Absagen nennen, welche Menge fehlt) |
| ⚠️ **Begriffsfalle „Klasse"**: Spielerklasse (Soldat, Heavy …) gegen Python-Klasse | **9a** — dort tauchen beide erstmals gleichzeitig auf; **11** — aus vier Spielerklassen werden vier Python-Klassen | **eingelöst** ✓ (11b) |

### Etappe 7 — Aufräumen  *(7a Funktionen · 7b Trennung)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **7a:** Funktionen als Bausteine | **9a** — werden zu Methoden | offen |
| **7a: Zustand als lange Parameterliste (der Schmerz)** | **9a** — genau das begründet `self` | offen |
| 👀 **7a: `global` als verlockende Abkürzung, bewusst abgelehnt** | **9a** — Klassen lösen das Problem, das `global` nur zudeckt | offen |
| **7a:** `berechne_schaden()` | **21a** — wird zur echten Kampfformel; **26** — erster `parametrize`-Test | offen |
| 👀 **7b:** „Was muss immer gelten?" (Testdenken, **kein** Testeinstieg) | **21a** — drei `assert`-Zeilen zur Schadensformel; **26** — dieselben Fragen als `pytest` | offen |
| 👀 **7b: `assert` als geprüfte Behauptung** — drei Zeilen, dann ist das Thema erledigt | **13** — Zähler-Invarianten; **20** — prüfen ↔ fangen; **26** — `pytest` ist derselbe `assert` im Rahmen | **teilweise eingelöst** ✓ (13; 20c — hochgestuft auf 🔨, Behauptung gegen Behandlung) |
| Lesefrage: „welche Annahmen macht diese Funktion?" | **23** — Lesekriterium bei fremdem Code; **27** — bei einem ganzen Repo | offen |
| Der Verhaltens-Beweis (Charakterisierungstest) | **26** — wird zum automatischen Testlauf | offen |
| **7b: Entscheidung `return` statt `print` in der Logik** | **21a** — zwei Rückgabewerte statt einer Meldung; **26** — nur so ist die Kampffunktion testbar; **28** — nur so bleibt die Logik grafikfähig | offen |
| **7b: Darstellung wird eigene Schicht (`zeichne_*`)** | **14a** — `zeichne_vorfeld()`; **28** — die Schicht wird ausgetauscht, nicht ersetzt | offen |
| Zeichenfunktionen entscheiden nichts | **29** — deshalb genügt hier ein Austausch | offen |
| Zwei Rückgabewerte als Tuple | **21a** — Schaden und Trefferart zusammen | offen |
| Standardwerte für Parameter | **10** — die Falle mit veränderbaren Standardwerten ✓ | **eingelöst** ✓ (10) |
| Docstrings | **23** — bekommen Typannotationen dazu | offen |
| „Eine Funktion, ein Zweck" | **24** — dasselbe Prinzip bei Modulen | offen |
| Klare Funktionsgrenzen zum Prüfen von Eingaben | **20** — an genau diesen Grenzen wird validiert | **eingelöst** ✓ (20a — an den Eingaben, 20b — an den Befehlen) |
| `verarbeite_befehl()` wird selbst zur `elif`-Kette | **23a** — Befehle als Dictionary; **25** — Befehle als Content | offen |
| Refactoring und neue Funktionen nicht mischen | durchgehend — Arbeitsregel ab hier | offen |
| Warnung vor Überabstraktion | **24** — dieselbe Frage bei der Dateiaufteilung | offen |
| Einzelne Funktionen statt ganzer Datei zeigen können | durchgehend — hält den Mentor bei langem Code arbeitsfähig | offen |
| ⭐ **7a: Design-Entscheidung „wie kommt Zustand in die Funktion?"** — Parameter, nicht `global`, nicht Zustands-Dictionary | **9a** — `self` löst dieselbe Frage; die Entscheidung wird dort wieder gelesen | offen |
| **7a: Die Notiz „welche Werte treten immer gemeinsam auf?"** | **9a** — genau diese Werte werden Attribute desselben Objekts | offen |
| **7a: Die Liste der Einfälle, die nicht gebaut wurden** | **21a** — Vorlage fürs Kampfsystem; **23a** — Vorlage fürs Befehls-Dictionary | offen |
| **7a: `return` beendet die Funktion sofort** (frühe Abfahrt statt Verschachtelung) | **20** — Prüfketten mit frühem Ausstieg | **eingelöst** ✓ (20b, Konzept 7 — `raise` beendet sie genauso) |
| **7a:** `befehle.txt` als Eingabedatei | **26** — dieselbe Idee, dann automatisch; **20** — die Chaos-Datei findet Validierungslücken | **teilweise eingelöst** ✓ (20a — die Chaos-Datei) |
| 👀 **7a:** Der Preis des Zerlegens sind Sprünge — mehr Funktionen sind nicht besser | **24** — dieselbe Abwägung bei Dateien | offen |
| **7b:** `zeichne_balken(wert, maximum)` **ersetzt drei fast gleiche Blöcke** (Kern, Trefferpunkte, Munition) | **14a** — dieselbe Funktion für Rasterzeilen; **28** — wird ausgetauscht | offen |
| **7b: Reinheitsprüfung der Zeichenfunktionen** (rechnet nichts, entscheidet nichts, kennt die Welt nicht) | **28** — nur reine Zeichenfunktionen lassen sich austauschen; **29** — Kacheln statt Zeichen | offen |
| **7b:** Die Balkenrechnung wohnt in der Zeichenfunktion — Einlösung aus **3c** | **14a** — dasselbe für das Raster | offen |
| **7b:** Genau **ein** `assert` im Spielcode (`schaden >= 0`) | **13** — Zähler-Invarianten, aufgeschrieben statt geprüft; **26** — wird zum Test | **teilweise eingelöst** ✓ (13) |
| 👀 **7a:** Der Aufrufstapel (Kür) | **8** — genau den liest man in jedem Traceback | **eingelöst** ✓ |

### Etappe 8 — Bug-Jagd I ⭐

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| Die drei Fehlertypen als Denkraster | **20** — `except:` macht aus Typ 1 einen Typ 3; **21** — `"weele"` gegen `Spielzustand.WEELE` | **teilweise eingelöst** ✓ (20a, Konzept 3; 20b, Kaputtmachen 7) |
| Tracebacks von unten nach oben lesen | durchgehend — bis **30** das häufigste Werkzeug | offen |
| Der Debugger (Breakpoints, Step, Variablen) | **9b** — Objektzustand aufklappen; **12** — den Tick beobachten; **14a** — Bewegung im Raster | **teilweise eingelöst** ✓ (12) |
| **Bedingte Breakpoints** | **12** — „halt an, wenn `welle == 7`"; **17b** — zusammen mit dem Seed die schärfste Kombination des Plans | **teilweise eingelöst** ✓ (12; 17b — in der Probedatei, nie zusammen mit `<`) |
| Ursache und Symptom trennen | **16** — der Abstand ist dort nicht in Zeilen, sondern in **Ticks** ✓ | **eingelöst** ✓ (16) |
| **Beobachtung → Hypothese → Experiment** (als Denkform angelegt) | **16** — verbindlicher Dreizeiler, plus die **Rückwärtsprobe** ✓; **27** — dieselbe Form ohne Änderungserlaubnis | **teilweise eingelöst** ✓ (16) |
| Halbieren als Suchverfahren | **24** — welches Modul ist schuld | offen |
| Das schriftliche Debugging-Protokoll | **16** — drei vollständige Einträge, **mindestens einer mit falscher Hypothese** ✓ | **eingelöst** ✓ (16) |
| Das Fehlertagebuch — **eine Zeile aus zwei Teilen: Symptom, dann der Fundweg** | **26** — jeder Eintrag ist ein Testkandidat; das Symptom ist dort das Material, der Fundweg bleibt der Schwerpunkt | offen |
| Einen Fehler präzise beschreiben (vier Punkte) | **23** — dieselbe Fähigkeit bei fremdem Code | offen |
| `git diff` / `git log` als Debugging-Werkzeug | **24** — dort zusammen mit Branches | offen |
| Abgrenzung Debugging ↔ Fehlerbehandlung | **20** — warum nacktes `except:` gefährlich ist | **eingelöst** ✓ (20a, Worum es geht) |
| Fehler in den **Daten** statt im Code | **16** — ⚠️ **Korrektur:** kein manipulierter Speicherstand, den gibt es erst ab **19**. Stattdessen der **Verweis ins Leere** zwischen zwei Tabellen aus **15** — beide Tabellen für sich fehlerfrei ✓; **19** — dort kommt der Speicherstand dazu; **25** — bei externem Content die häufigste Sorte | **teilweise eingelöst** ✓ (16; 19c, Kaputtmachen 11 — der manipulierte Spielstand) |
| **Die Funktion, die ihren eigenen Docstring bricht** (Transferaufgabe: verändert die übergebene Liste, obwohl sie das Gegenteil zusagt) | **15** — Leseübung: `dringendster_fall()` nimmt stillschweigend an, die Liste sei nie leer ✓; **20** — Zusagen an Funktionsgrenzen prüfen | **teilweise eingelöst** ✓ (15; 20c — Behauptungen über Zusagen) |
| Die Darstellung als Fehleranzeiger benutzen | **16** — Phasenausgabe mit `### PHASE n` macht den Tick sichtbar ✓ | **eingelöst** ✓ (16) |
| **Die repr-Form** (`!r` im f-String, und `p` im Debugger zeigt sie von selbst) | **9b** — `__repr__` macht dasselbe für eigene Objekte; ohne heute fehlt dort der Anlass | offen |
| **Der bewusste Verzicht auf `try`/`except`** — ein Absturz beim Entwickeln ist ein Fund, kein Ärgernis | **20** — dort erst die Fehlerbehandlung, samt der Warnung vor nacktem `except:` | **eingelöst** ✓ (20a) |

### Etappe 9 — Alles wird zum Objekt  *(9a Klassen · 9b `__repr__`)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **9a:** Klasse `Marine` | **10** — bekommt Inventar und Ausrüstung ✓; **11** — bekommt vier Unterklassen | **teilweise eingelöst** ✓ (10) |
| **9a:** Klasse `Gegner` | **11** — gemeinsame Basis mit `Marine`; **17a** — wird aus Typen erzeugt | **eingelöst** ✓ (11a, 11b, 17a) |
| **9a:** `self` bündelt den Zustand | **12** — `self.zeit`; durchgehend | **eingelöst** ✓ (12) |
| **9a:** `trefferpunkte`, `erfahrung` und `level` werden Attribute des Marine — Einlösung aus **1** und **3c** | **11** — jede Unterklasse steigt anders; **18** — `level` schaltet Fähigkeiten frei; **19** — Teil des Speicherstands | **teilweise eingelöst** ✓ (18b; 19b/19c — alle drei im Spielstand, und warum `level` trotz Herleitbarkeit: Konzept 13) |
| **9a: `kern_integritaet` bleibt bei der Welt, nicht beim Marine** | **12** — `Welt` ist das Objekt, dem sie gehört; **13** — Basiswerte ticken mit | **teilweise eingelöst** ✓ (12, 13) |
| **9b:** `__repr__` | **12** — zwanzig Einheiten lesbar im Debugger; **8**-Rückgriff | **eingelöst** ✓ (12) |
| **9b:** Doppelte Unterstriche sind Haken für Python | **11** — `__len__`, `__contains__`, `__iter__` (dort 👀) | **eingelöst** ✓ (11c) |
| Erste Leseübung — **Stufe 1 der Leseleiter** | **12** — Stufe 2; **17** — Stufe 3; **23b** — Stufe 4; **27** — die Prüfung | **teilweise eingelöst** ✓ (12; 17b — Stufe 3, die Musikbox) |
| 👀 **9b:** `__str__` ↔ `__repr__` — **nur eines bauen**, das andere erkennen | **23b** — `f"{objekt}"` in fremdem Code | offen |
| **9a: Die Probedatei** — `spiel.py` als `probe.py` kopieren, den Startteil durch Prüfzeilen ersetzen, vor dem Commit löschen; alle späteren Prüfungen „in deiner Probedatei“ verweisen hierher | **24** — Module und `if __name__ == "__main__":` lösen es sauber; dort ein Rückbezug | offen |
| **Frage „woher kommt dieser Name?"** (Datei / Import / `self`) | **11** — Oberklasse als vierte Herkunft ✓, mit `s` im Debugger nachweisbar; **24** — jetzt baust du Module selbst | **teilweise eingelöst** ✓ (11) |

### Etappe 10 — Komposition

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `Inventar` und `Ausruestung` als eigene Objekte | **11** — bekommen Dunder-Methoden; **19** — müssen serialisiert werden | **teilweise eingelöst** ✓ (19b, Schritt 14 — jedes beschreibt sich selbst) |
| **`Ausruestung` ohne Befehl** — die Plätze bleiben im Spiel leer, bewusster Leerlauf (reiner Umbau, `diff` bleibt still). ⚠️ Beim Festlegen des Befehls den Namen gegen `ablege` aus **4** abgrenzen | Ziel-Etappe noch festzulegen | offen |
| Slots mit `None` | **19** — `null` in JSON; **23** — `| None` in Typannotationen | **teilweise eingelöst** ✓ (19b, Konzept 12 — `null` und zurück) |
| **`None` ≠ `0`** (keine Waffe ≠ leere Waffe) | **18** — die `or`-Falle bei `0`; **20** — unterschiedliche Fehlermeldungen | **teilweise eingelöst** ✓ (18b; 20a, Konzept 2 — `None` als *noch keine Zahl*) |
| `is None` statt `== None` | durchgehend — Lesegewohnheit für fremden Code | offen |
| `self.position` als Tuple | **14a** — Position im Raster; ⚠️ **Abweichung:** die Koordinate liegt als **zwei Attribute** `x` und `y` am Objekt, nicht als ein Tuple. Tuples bleiben für Adressen, die weitergereicht und verglichen werden (`welt.tor`, Set-Einträge). Grund: Eine Einheit bewegt sich pro Tick auf einer Achse — mit zwei Zahlen ist ein Schritt eine Zuweisung an eine Achse, mit einem Tuple müsste jedes Mal ein neues gebaut werden. `self.position` wird in 14a/14b ausdrücklich gelöscht, damit es keine zwei Wahrheiten über den Ort gibt | **eingelöst** ✓ (14a) |
| **Objektidentität: zwei Namen, ein Objekt** — Einlösung aus **4**, jetzt an eigenen Klassen | **14a** — `[["."] * 5] * 5`; **16** — Bug-Kandidat; **19** — was beim Laden neu erzeugt wird | **teilweise eingelöst** ✓ (19b — Verweise als Stelle, Prüfung mit `is`, Kaputtmachen 5) |
| Reflex: *„verändern sich zwei Dinge gemeinsam — sind es überhaupt zwei?"* | **16** — Fahndung 6, 7 und 13 ✓ | **eingelöst** ✓ (16) |
| Geteilte Objekte als Fehlerquelle | **16** — Kandidat für die Bug-Jagd | offen |
| Veränderbarer Standardwert in `__init__` | **16** — subtiler, weil er erst beim zweiten Objekt auffällt | offen |
| „hat ein" als Alternative zu „ist ein" | **11** — die Vererbungsfrage braucht diesen Vergleich | **eingelöst** ✓ (11b) |
| **Zwei Behälterklassen mit verschiedenen Regeln** (`Inventar` = Liste mit Obergrenze, `Ausruestung` = feste Rollen) | **11** — das Beispiel, an dem gezeigt wird, wann Vererbung **nicht** passt | **eingelöst** ✓ (11b) |
| **Die Regel wandert zum Ding** — Kapazität steht in `Inventar`, nicht an den Aufrufstellen | **22** — dieselbe Frage für Daten gegen Klassen | offen |
| `.copy()` kopiert nur eine Ebene tief | **19** — beim Speichern verschachtelter Objekte wird das zum Problem | **eingelöst** ✓ (19b, Konzept 12) |
| ⭐ **Die Slot-Invariante: ein Platz existiert immer, leer heißt `None`, nie gelöscht** | **20** — daraus wird eine Prüfung; **26** — daraus wird ein Test | **teilweise eingelöst** ✓ (20c, Schritt 11) |

### Etappe 11 — Vererbung  *(11a Eine Gegnerliste · 11b Vererbung und der Trupp · 11c Item-Hierarchie)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `Einheit` als gemeinsame Basis | **12** — der Tick läuft über alle Einheiten; **13** — Bauzeit und Nachschub teilen ein Muster | **teilweise eingelöst** ✓ (12, 13) |
| Die vier Marine-Klassen | **21a** — unterschiedliche Formeln; **22** — die Frage, ob sie Daten sein sollten | offen |
| **Vier Objekte gleichzeitig — hier entsteht der Trupp** (Einlösung aus **2**) | **12** — drei davon autonom; **14b** — sie bewegen sich; **18** — sie nutzen Fähigkeiten | **teilweise eingelöst** ✓ (12; 18c — alle vier setzen Fähigkeiten ein) |
| ⭐ **Einer ist der gesteuerte Held, drei sind Kameraden** — gleiche Basisklasse, verschiedene Steuerungsquelle | **12** — der Held handelt auf Befehl, die drei im `update()`; **13** — nur der Held hat einen Respawn-Zähler, der das Spiel anhält; **18** — Fähigkeiten hat jeder, aber nur der Held wählt sie | **eingelöst** ✓ (12, 13; 18b/18c — `lerne` gegen `lerne_selbst`, Befehl gegen `will_einsetzen`) |
| ⭐ **Jede Marine-Klasse bekommt ihre eigene Fähigkeit** — das ist ab hier der eigentliche Unterschied zwischen den Unterklassen, nicht mehr nur die Werte | **13** — die Abklingzeit sitzt in der Oberklasse, die Unterklassen rufen sie mit `super()` auf; **18** — Freischaltung über `level`; **22** — die Frage, ob Fähigkeiten Daten sein sollten | **teilweise eingelöst** ✓ (13; 18c — sechs aktive Fähigkeiten und ein Passiv, `wirke()` je Unterklasse) |
| **Der mobile Geschützturm des Engineer** — eine *Fähigkeit*, kein Gebäude, und höchstens einer gleichzeitig | ⚠️ **Korrektur:** Er gehört **nicht** nach 13. Der Klassengerät-Faden sperrt Klassenbindung bis **18**; was 13 baut, ist der **Basisturm** (Gebäude, klassenunabhängig, Werkstatt). **18** — Aufstelldauer und Abklingzeit als echte Klassenfähigkeit; **14b** — Reichweite wie der Trupp | **eingelöst** ✓ (18c — `MobilerTurm(Einheit)` mit Aufstellzeit und Lebensdauer, höchstens einer über `welt.mobiler_turm`, Reichweite wie der Trupp) |
| 👀 **Komposition als dritter Weg** (benannt, nicht gebaut) | **22** — dritte Spalte der Entscheidungstabelle; **10**-Rückgriff | offen |
| **Die schriftliche Frage „brauchen wir Vererbung?"** | **22** — Wiedervorlage mit den Fähigkeitentabellen; **25** — die Antwort zeigt sich in JSON | offen |
| `Item` → `Waffe`, `Panzerung`, `Modul`, `Verbrauchsgut` | **21b** — Schadenstypen; **22** — Ausbaustufen | offen |
| 👀 `__len__`, `__contains__`, `__iter__` — **keine Implementierungsaufgabe** | **23a** — Comprehensions über eigene Objekte | offen |
| 👀 `@property` (`am_leben`) — erkennen, nicht bauen | **12** — Prüfung im Tick; **23b** — Dekoratoren allgemein | offen |
| ⚠️ **Korrektur (v3.7.0):** Truthy ist eine **normale Methode** ohne Klammern (`if e.am_leben:`), **nicht** eine `@property`. Bei einer `@property` sind die Klammern gerade falsch und geben `TypeError`. Etappe 11, Konzept 14 führt alle vier Fälle in einer Tabelle | **16** — Fahndung 8 prüft beide Richtungen | **eingelöst** ✓ (16) |
| `super().__init__()` | **13** — ⚠️ **Abweichung:** es entsteht **keine** Zähler-Basisklasse. Zähler sind Attribute an dem Objekt, dem sie gehören; `Geschuetz` erbt von `Einheit` wie alle anderen. Begründung im Guide zu 13 (Design-Entscheidung); Wiedervorlage in **22** | **eingelöst** ✓ (13) |
| Die `elif`-Kette aus Etappe 2 stirbt hier | — Einlösung | offen |
| **Die Vererbungsfrage schriftlich in `GELERNT.md`** | **22** — Gegenprobe an den Tabellen; **25** — Endprobe beim Verdaten | offen |
| ⭐ **Der Ablauf Entscheidung → Erfahrung → Gegenprobe → Revision** — die Antwort wird mit Datum und Begründung festgehalten, weil man aus dem Gedächtnis immer die heutige Entscheidung rekonstruiert | **22** und **25** — dort wird sie herausgeholt und **vor** dem Urteil gelesen | offen |
| **`Item` trägt Kennung *und* Anzeigename** — die Design-Entscheidung 1 aus Etappe 4 war nie ein Entweder-Oder, sondern ein „noch nicht" | **25** — die Kennung wird JSON-Schlüssel, der Name Content | offen |
| **Der Held ist keine eigene Unterklasse** — nur ein Attribut unterscheidet ihn vom Kameraden | **12** — dort entscheidet dasselbe Attribut, ob `input()` oder `update()` handelt | **eingelöst** ✓ (12) |
| Eine Schleife über Objekte ersetzt die Typabfrage — **niemand fragt mehr, welche Klasse etwas ist** | **12** — der Tick läuft genauso über alle Einheiten; **17a** — Gegner werden aus Typen erzeugt | **teilweise eingelöst** ✓ (12, 17a) |
| **11a: `entfernung` ist der Abstand zum Tor** — die Position aus **4** wird beim Erzeugen umgerechnet (gegen `BAHNLAENGE`), die Bahn rechnet für die Anzeige zurück | **12** — nächster Gegner und `<= REICHWEITE` rechnen mit dieser Richtung ✓; **14a** — wird durch `x`/`y` ersetzt ✓ | **eingelöst** ✓ (12, 14a) |
| **11b: Der Schuss des Helden wirkt über `nimm_schaden()`** — Trefferpunkte je Gegnertyp legt der Lernende fest | **12** — die Kameraden kämpfen nach derselben Regel ✓; **21** — Balancing | **teilweise eingelöst** ✓ (12) |
| **11b: `klasse` neben der Unterklasse** — der Lernende entscheidet, ob der String bleibt oder der Klassenname die Anzeige ist (`type(self).__name__`) | **22** — Gegenprobe an den Tabellen | offen |
| **11b: Der Vorrat gehört dem Helden** — was die Kameraden bekommen, entscheidet der Lernende; sie dürfen nicht auf denselben Vorrat zeigen | **13** — die Kameraden bekommen ein eigenes Magazin, das sich über Zeit füllt ✓ | **eingelöst** ✓ (13) |
| **11c: Wo `Item`s entstehen** — `kaufe`, `nimm`, `ablege`; Dictionary Kennung → Klasse (dasselbe Muster wie die Klassenwahl), `name` aus `ANZEIGENAMEN` | **15** — Fundstücke auf dem Raster; **22** — ein Eintrag pro Ding | offen |
| `min()` auf Objekten trägt nicht mehr — die Schleife wird von Hand gebaut | **23a** — `min(..., key=...)` und Comprehensions lösen es ab | offen |
| ⚠️ **Ein Gegner hat `name`, nicht `typ`** — der Typ *ist* sein Name; zwei Attribute wären zwei Wahrheiten über dieselbe Sache | **6** — `GEGNERTYPEN` wird über `.name` nachgeschlagen; **17a** — Gegner werden aus Typen erzeugt | **eingelöst** ✓ (17a — Generator und `BEUTE` arbeiten mit dem Namen) |
| ⚠️ **Eingebaute Werkzeuge verlieren an Objekten ihren Bezugspunkt** — `min(liste)` und `"medkit" in liste` funktionieren nicht mehr von selbst, weil Python nicht weiß, worauf es schauen soll | **23a** — `key=` und Comprehensions geben ihn zurück; **11c** — bis dahin eine Schleife von Hand ✓ | **teilweise eingelöst** ✓ (11) |

### Etappe 12 — DER TICK ⭐  *(12a Die Welt · 12b Der Tick)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **12b: Ein Gegner am Tor trifft den Kern und eine Einheit des Trupps** — welche, entscheidet der Lernende; Held und Kameraden müssen treffbar bleiben | **13** — Ausfall und Wiedereinstieg setzen Treffer auf den Trupp voraus ✓; **19** — beide Verlustbedingungen bleiben prüfbar | **eingelöst** ✓ (13; 19 — Kern und Trefferpunkte jeder Einheit stehen im Spielstand) |
| `Welt.tick()` und `self.zeit` | **13** — Bauzeiten; **17** — Ereignisse; **18** — Statuseffekte; **22** — alles auf demselben Takt | **teilweise eingelöst** ✓ (13; 17c — Ereignisse **zwischen** den Wellen, nicht im Takt; 18a — Statuseffekte zählen in der Zählerphase) |
| 👀 `update(self, welt)` — Einheiten kennen die Welt (**nur bemerken, nichts reparieren**) | **13** — der Kopplungs-Umweg; **15** — die Kopplungszeichnung ✓; **23b** — Alternativen beim Lesen fremden Codes | **teilweise eingelöst** ✓ (13, 15) |
| Status als String (`gegner.status = "tot"`) — zwei Zeilen, mehr nicht | **21b** — `Enum` löst die Strings ab | offen |
| 👀 Der Begriff **Zustandsautomat** (benannt, nicht ausgebaut) | **21b** — dort bekommt er benannte Werte | offen |
| Sammeln und danach entfernen | — Einlösung aus **4**; **16** — bleibt Bug-Kandidat | offen |
| 👀 **Die Tick-Reihenfolge ist eine Entscheidung** — heute nur aufschreiben, nicht optimieren | **16** — dort wird sie zur Tick-Tabelle und zur eigenen Fehlerklasse | offen |
| Einheiten merken sich, wo sie waren | **17** — Material für Ereignisse und Meldungen | offen — 17c bietet es nur als Kür unter „Wenn du mehr willst" an |
| Ein Tick pro Befehl | **20** — auch bei ungültigem Befehl?; **28** — ein Tick pro Bild | **teilweise eingelöst** ✓ (20b — ein Befehl, der mit `SpielFehler` endet, kostet keine Runde) |
| **Leseleiter Stufe 2** (Ablauf auf Papier verfolgen) | **16** — zum ersten Mal auf **eigenen** Code angewandt, an `tick()` ✓ | **eingelöst** ✓ (16) |
| **Trupp-KI Stufe 1: feuern, wenn in Reichweite** | **14b** — Bewegung kommt dazu; **18** — Fähigkeiten kommen dazu | **eingelöst** ✓ (14b; 18c — Fähigkeiten kommen dazu) |
| Unterscheidung gesteuert ↔ autonom | **13** — autonome Objekte mit Zählern, und `gesteuert` entscheidet die Ausfalldauer; **23a** — Strategien als Funktionen | **teilweise eingelöst** ✓ (13) |
| **Die Einheitenliste nimmt Fremdkörper auf** — Trupp, Engineer-Turret, später Söldner ticken über denselben Weg | **13** — jeder von ihnen bringt einen eigenen Zähler mit; **22** — sie kommen aus Tabellen; **23a** — dieselbe Zielauswahl für alle | **teilweise eingelöst** ✓ (13) |
| ⚠️ **Design-Entscheidung: zwei Listen statt einer** — `welt.trupp` und `welt.gegner`, **keine** gemeinsame `einheiten`-Liste. Der Basisturm aus **13** und die Söldner aus **22** kommen in den `trupp` | **16** — die zwei Schleifen machen die Tick-Reihenfolge im Code sichtbar; **22** — die Frage wird dort wiedervorgelegt | offen |
| `welt.naechster_gegner()` — Zielsuche als Schleife von Hand, `None` bei leerer Liste | **14b** — aus „der Nächste" wird eine Rechnung auf dem Raster; **23a** — `min(..., key=...)` und Strategien lösen sie ab | offen |
| **Die Aufräumphase als eigene Tick-Phase** — sterben und entfernt werden sind zwei Dinge | **15** — die Gefallenen hinterlassen an **ihrer** Koordinate ein Fundstück ✓; **19** — nur Aufgeräumtes wird gespeichert | **teilweise eingelöst** ✓ (15; 19c, Konzept 13 — gespeichert wird nur zwischen zwei Takten, nach dem Aufräumen) |
| `abschuesse` als Zähler am Objekt — Gedächtnis ohne Wirkung | **17** — daraus werden Meldungen zwischen den Wellen | **eingelöst** ✓ (17c — der Wellenbericht mit Stimmen) |
| ⚠️ **Offener Posten: Kameraden feuern ohne Munitionsverbrauch** — bewusst ausgelassen, im Guide benannt | **13** — ein Magazin mit `nachladezeit`, dasselbe Zähler-Muster; ob die Kameraden dafür das Magazin-Attribut des Helden mitbenutzen, entscheidet der Lernende | **eingelöst** ✓ (13) |
| 👀 **Nacktes `return`** — Werkzeuglücke aus **7**, hier geschlossen | — Einlösung | **eingelöst** ✓ (12) |

### Etappe 13 — Bauzeit und Abklingzeit ⭐  *(13a Das Zähler-Muster · 13b Ausfall, Nachschub und das Geschütz)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| ⭐ **Das Zähler-Muster, dreimal am selben Abend** — Abklingzeit einer Fähigkeit · Erfahrung bis zur nächsten Stufe · Respawn nach dem eigenen Ausfall | **22** — alle drei bekommen ihre Werte aus Tabellen; **19** — alle drei müssen gespeichert werden | **teilweise eingelöst** ✓ (19b — alle laufenden Zähler im Spielstand) |
| **Die Abklingzeit als das eigentliche Thema** — eine Fähigkeit ist nicht „verfügbar\" oder „weg\", sondern *in soundso vielen Ticks wieder da* | **18** — jede Fähigkeit bekommt eine; **21b** — die Entscheidung, sie zu balancieren; **28** — aus Ticks werden Sekunden | **teilweise eingelöst** ✓ (18c — jede Fähigkeit hat eine, `abklingzeiten` als Dictionary) |
| **Der eigene Ausfall mit Respawn-Zähler** — Einlösung aus **1** (`trefferpunkte` als zweite Verlustbedingung) | **17c** — was passiert währenddessen mit dem Trupp?; **19** — Teil des Speicherstands | **eingelöst** ✓ (17c; 19b) |
| **Man kommt mit Restmunition zurück, nicht mit voller** — eine bewusste Entscheidung, keine Nebensache | **21b** — Balancing; **19** — der Restbestand muss gespeichert werden | **teilweise eingelöst** ✓ (19b — Magazin und Vorrat im Spielstand) |
| **Der Basisturm mit Bauzeit** — genau einer, klassenunabhängig, in der Werkstatt in Auftrag gegeben; Einlösung der Werkbank-Kür aus **5** | **14b** — steht auf einem Feld und hat Reichweite; **22** — fünf Ausbaustufen desselben Turms; **23a** — Zielauswahl-Strategien | offen |
| ⚠️ **Zwei Türme, die nicht verwechselt werden dürfen** — der Basisturm (Gebäude, ab 13) und der mobile Geschützturm des Engineer (Klassenfähigkeit, ab 18). Im Guide zu 13 steht die Abgrenzungstabelle | **18** — dort entsteht der zweite und die Unterscheidung wird praktisch; **22** — nur der Basisturm bekommt Ausbaustufen | **teilweise eingelöst** ✓ (18c — der mobile Turm entsteht, Konzept 17 grenzt ab) |
| Der Rekrut mit Nachschubzähler — **verschoben nach 22** (siehe die Zeile weiter unten) | **22** — entsteht dort mit den Söldnern; **17c** — kann endgültig verloren gehen; **18** — Statuseffekte wirken auf ihn (**vorbereitet** ✓: Effekte hängen an `Einheit`, der Rekrut erbt sie, sobald er in **22** entsteht) | offen — **17c hat entschieden:** kein endgültiger Verlust vor **22** |
| 👀 **Der Begriff *Scheduler*** — die Alternative zum Zähler im Objekt, benannt und nicht gebaut | **23b** — beim Lesen fremden Codes als gleichwertige Bauart erkennen | offen |
| `welt.raeume_frei()` ändert Daten zur Laufzeit | — Einlösung aus **5**; **19** — der geänderte Zustand muss mitgespeichert werden | **eingelöst** ✓ (19a, Schritt 3, 5, 8 — die Karte, soweit sie sich ändert) |
| **Der Kopplungs-Umweg** (warum kennt das Geschütz die Welt?) | **15** — die Zeichnung macht es sichtbar ✓; **23b** — Callbacks und Strategien als eine Antwort; **24** — Module machen Kopplung schmerzhaft | **teilweise eingelöst** ✓ (15) |
| **Zustand ↔ Ereignis als benannter Begriff** (*soll das gelten oder soll das passieren?*) | **17c** — Ereignisse zwischen den Wellen; **19** — was gespeichert wird ist Zustand; **28** — zeichnen ↔ aufblitzen | **teilweise eingelöst** ✓ (17c; 19c, Konzept 13 — *ein Spielstand ist ein Foto*) |
| Ausgefallener Trupp-Kamerad mit `ausfallzeit` | **17c** — kann er endgültig fallen?; **19** — Teil des Speicherstands | **eingelöst** ✓ (17c; 19b) |
| **Der Unterschied Held ↔ Kamerad wird hier zum ersten Mal spürbar:** fällt ein Kamerad, läuft das Spiel weiter; fällt der Held, wartet es | **28** — in Echtzeit wird daraus eine sichtbare Wartezeit | offen |
| Unterscheidung „ist fertig" ↔ „wurde gerade fertig" | **19** — Speicherformat; **26** — genau hier lauern Off-by-One-Tests | **teilweise eingelöst** ✓ (19c, Konzept 13 — dazu Rest gegen Fortschritt) |
| Entscheidung Tick-Zeit statt Echtzeit | **28** — `bauzeit = 180` sind drei Sekunden | offen |
| ⚠️ **Verschoben: der Rekrut mit Nachschubzähler entsteht nicht in 13, sondern in 22** — ein Rekrut ist eine **gekaufte Stelle**, die neu besetzt wird, und damit etwas anderes als ein Kamerad, der ausfällt und wieder aufsteht. Er braucht Kauf- und Vertragstabellen, und die stehen in 22. Im Guide zu 13 ist die Abgrenzung unter *Was NICHT* benannt | **22** — dort zusammen mit den Söldnern; **17c** — die Frage, ob er endgültig verloren gehen kann, wandert mit | offen — **17c hat entschieden:** kein endgültiger Verlust vor **22** |
| ⭐ **Die Bedeutung einer Zählerzahl wird schriftlich festgelegt** — was heißt `BAUZEIT = 3` für Tick 1, 2, 3? Einlösung des Beobachtbarkeitsfadens; gilt ab dort für alle fünf Zähler | **16** — Fahndung 2, und die Notiz ist dort Beweismittel ✓; **26** — daraus wird ein Test | **teilweise eingelöst** ✓ (16) |
| **Invariante und Merksatz getrennt notiert** — „nie kleiner als `0`" ist prüfbar, „läuft oder ist abgelaufen" ist es nicht | **20** — nur die prüfbare wird zur Prüfung; **26** — nur sie wird zum Test | **teilweise eingelöst** ✓ (20c — nur die prüfbaren werden `assert`) |
| ⭐ **Das Zähler-Muster als benannte Bauform** — dieselben drei Zeilen an fünf Objekten, schriftlich gezählt | **22** — dort fällt die Entscheidung, ob daraus eine gemeinsame Struktur wird; **19** — jeder laufende Zähler gehört in den Spielstand | **teilweise eingelöst** ✓ (19b) |
| `welt.melde(text)` — ein einziger Ort für alle Meldungen aus dem Tick | **17** — wird zur gesammelten Meldungsliste zwischen den Wellen; **28** — trennt Zeichnen von Aufblitzen | **teilweise eingelöst** ✓ (17c — gesammelt wird in `welt.bericht`, über eine zweite Methode `notiere()` oder über `melde(text, sofort=True)`, nach Wahl des Lernenden) |
| **Der Startwert der Trefferpunkte als zweites Attribut** — derselbe Wert wie `trefferpunkte_max` aus **3c**, kein zweiter Name | **19** — muss gespeichert werden; **21b** — wird beim Balancing zur Tabellenzahl | **teilweise eingelöst** ✓ (19a, Konzept 7 — ⚠️ **Präzisierung:** gespeichert wird er nur, wenn er sich im Spiel ändern kann; setzt ihn nur der Konstruktor, stellt der ihn wieder her) |
| ⚠️ **„Eine Strafe darf keine Belohnung sein"** — Rückkehr mit Restmunition, Fehlversuch ohne Abklingzeit | **21b** — dieselbe Prüffrage beim Balancing der Kampfformel | offen |
| **Fällt der Turm, wird `welt.turm` wieder `None`** — die Aufräumphase unterscheidet über ein Attribut, nicht über den Typ (wie `gesteuert` in **12**) | **16** — Bug-Kandidat, wenn die Unterscheidung fehlt; **22** — Ausbaustufen | offen |
| **Abklingzeit in der Oberklasse: woher weiß die Unterklasse vom Abbruch?** — Rückgabewert (**7**) oder überschriebene Meldungsmethode (**11**), der Lernende wählt | **18** — Fähigkeiten mit Kosten und Wirkung bauen darauf auf | **eingelöst** ✓ (18c, Konzept 14 — die Frage wird umgedreht: `setze_ein()` in der Oberklasse prüft, ruft `wirke()` und bezahlt erst danach) |
| **`KAMERAD_MAGAZIN` neben `magazin_groesse`** — zwei Startgrößen, weil Kameraden kostenlos über Zeit nachladen und der Held aus dem Vorrat zahlt; ob es dafür zwei Attribute braucht, fragt Schritt 15 als Reflexionsfrage (gemeinsame Klasse, kein zweiter Name für dieselbe Sache) | **21a** — Magazingröße je Klasse (Idee) | offen |
| **`welt.turm` als „höchstens einer"** — ein Objekt unter eigenem Namen neben der Liste | **14b** — er bekommt Standort und Reichweite; **22** — Ausbaustufen statt zweitem Turm | offen |

### Etappe 14 — Das Vorfeld ⭐  *(14a Raster · 14b Reichweite und Bewegung · 14c Barrikade, Kür)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **14a:** Das Raster als Liste von Listen | **29** — unverändertes Format für die Tilemap; **30** — Grundlage der Isometrie | offen |
| **14a:** Einlösung: aus einer Zeile werden viele | — Einlösung aus **4** | **eingelöst** ✓ (14a) |
| **14a:** `vorfeld[y][x]` — Zeile vor Spalte | **29** — dieselbe Reihenfolge beim Zeichnen | offen |
| **14a:** Randprüfung („liegt die Koordinate drauf?") | **14b** — dieselbe Form als Zonengrenze ✓; **14c** — ein drittes Mal beim Stellen der Barrikade ✓; **20** — wird zu einer abgefangenen Bewegung | **teilweise eingelöst** ✓ (14b, 14c; 20b — wo ein Befehl eine Bewegung verlangt, über die Fahndung) |
| **14a/14b:** Position als zwei Attribute `x` und `y`; Tuples tragen Adressen (`welt.tor`, Reichweite, Zone) — Einlösung aus **6** | **19** — ein Tuple überlebt JSON nicht | **teilweise eingelöst** ✓ (19a, Konzept 5; 19b — die Zone kommt als Liste zurück, `tuple()`) |
| ⚠️ **14a: Wegfindung ausdrücklich ausgeschlossen** (kein A\*, kein Dijkstra) | **nach 27** — als notierte Idee in `GELERNT.md`, nicht im Plan | offen |
| 👀 **14a:** `enumerate()` und die drei Schleifenformen — Erkennen, **kein Umbau** | **23a** — dieselben Formen als Comprehension; durchgehend beim Lesen | offen |
| **14a:** Vergleich Dictionary ↔ Raster als Modellierungsfrage | **25** — welche Inhalte werden JSON, welche bleiben Struktur | offen |
| **14a:** `zeichne_vorfeld()` | **28** — dieselbe Funktion, andere Ausgabe; **29** — dasselbe Raster als Tilemap | offen |
| ⚠️ **14a, Riegel 2: Das Raster hält Gelände, keine Einheiten** — Einheiten haben eigene Koordinaten, gezeichnet wird eine Kopie | **19** — nur Zustand wird gespeichert, das Bild nicht; **29** — Tilemap und Sprites sind dieselbe Trennung | **teilweise eingelöst** ✓ (19a, Konzept 1 — das Gelände ist Inhalt und wird nicht gespeichert) |
| **14a: Die flache Kopie** — jede Zeile einzeln kopieren, sonst malt man ins Gelände | **19** — dasselbe Problem beim Laden; **28** — 60-mal pro Sekunde | **teilweise eingelöst** ✓ (19b, Konzept 12 — was `json.load` liefert, ist frisch gebaut; geteilt wird nur, was man selbst kopiert) |
| ⭐ **14a: Entscheidung „eine Achse pro Tick oder beide?" und „welche Achse bei Gleichstand?"** — beides schriftlich | **14b** — die Abstandsrechnung muss dazu passen ✓; **16** — ⚠️ **kein Off-by-one, sondern ein Tie-Break**: bei zwei gleich langen Wegen ist keiner um eins daneben, es gibt zwei richtige Antworten und der Code wählt eine ✓; **21b** — Gegnertempo als Stellschraube | **teilweise eingelöst** ✓ (16) |
| ⭐ **14b: Entscheidung `<` gegen `<=` bei Reichweite** — schriftlich, nach dem Muster aus **13** | **16** — ausdrücklich als Bug-Kandidat benannt; **21a** — Teil der Trefferrechnung | offen |
| **14b: `abs()`** | **21a** — Schadensformel; durchgehend beim Rechnen mit Koordinaten | offen |
| ⚠️ **14a: Zwei Einheiten dürfen dasselbe Feld belegen** — `ist_frei()` fragt nur das Gelände, das Raster kennt keine Einheiten. Beim Zeichnen gewinnt die zuletzt gemalte | **nicht im Plan** — eine Kollisionsprüfung wäre ein eigenes System; im Guide als bewusste Regel benannt statt als Zufall | offen |
| ⚠️ **14b: Kein Sichtlinien-Check** — der Turm schießt durch Wände, ausdrücklich benannt | **nicht im Plan** — als offener Posten in `GELERNT.md` | offen |
| ⭐ **14c (Kür, Stufe 1): Barrikade kaufen und hinstellen** — lehrt nichts Neues, zeigt die Prüfkette aus **5** zum dritten Mal | **21b** — Preis als Stellschraube. *Entfällt mit der Kür.* | offen |
| ⭐ **14c (Kür, Stufe 2, optional innerhalb der Kür): Die Barrikade** — eine Depotware, die auf ein Feld gestellt wird; **die erste räumliche Entscheidung des Spielers** | **21b** — Preis und Trefferpunkte als Stellschraube. ⚠️ Sie schießt nicht, hat keine Stufen und tickt nicht — wer ihr Schaden gibt, baut Tower Defense. *Entfällt, wenn die Kür entfällt.* | offen |
| **14c (Kür): Entscheidung, ob Barrikaden zerstörbar sind** | **19** — nur zerstörbare haben Trefferpunkte, die gespeichert werden müssen. *Entfällt mit der Kür.* | **teilweise eingelöst** ✓ (19a, Schritt 3 — in der Inventur abgefragt. *Entfällt mit der Kür.*) |
| **14b:** Reichweite als Set von Tuples | **21a** — wer ist im Feuerbereich; **23a** — als Comprehension | offen |
| **14b: Trupp-KI Stufe 2: nächsten Gegner suchen, Zone halten** | **15** — die Zone entscheidet mit, was eingesammelt wird, und bekommt damit zwei Seiten ✓; **18** — Fähigkeiten; **21b** — Balancing-Stellschraube; **23a** — `min`/`sorted` mit `key`, Strategien | **teilweise eingelöst** ✓ (15; 18c — Fähigkeiten über `will_einsetzen`) |
| **14b:** „Nächstes Ziel finden" als Suchalgorithmus | **23a** — `sorted(..., key=lambda ...)`; **26** — testbar mit festen Positionen | offen |
| **14b:** Zonengrenze als Randprüfung | **20** — wird zu einer abgefangenen Bewegung | **entfällt** für 20 — die Zone begrenzt die Kameraden, keinen Befehl des Spielers; ein `SpielFehler` hätte keinen Adressaten (Design-Entscheidung 20b) |
| ⭐ **14b (Kür):** `erkundete_felder` als Set (Sensorabdeckung) — im Guide als Auftragsschritt 15 mit ausdrücklichem „nur wenn 14b sich nicht zieht" | **19** — Set → JSON ist nicht trivial | **teilweise eingelöst** ✓ (19a, Schritt 3 — in der Inventur, Set aus Tuples. *Entfällt mit der Kür.*) |
| ⭐ **14b (Kür): Entscheidung „erkundet" dauerhaft oder nur bei Sicht** | **19** — bestimmt, ob es gespeichert werden muss. *Entfällt, wenn die Kür entfällt.* | **teilweise eingelöst** ✓ (19a — nur die dauerhafte Fassung ist Zustand. *Entfällt mit der Kür.*) |

### Etappe 15 — Was die Brut hinterlässt  *(15a Fundstücke und Erkenntnisse · 15b Erkenntnisse wirken)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **Ein Beute-System statt zwei** — alles, was ein Gegner hinterlässt, liegt als `Fundstueck` in `welt.fundstuecke`; die ortlose Liste aus **4** geht darin auf. Was aus `nimm` und `ablege` wird, entscheidet der Lernende | **16** — Bug-Kandidat, falls die alte Liste weiterlebt; **19** — `welt.fundstuecke` wird gespeichert | **teilweise eingelöst** ✓ (19b — `welt.fundstuecke` im Spielstand) |
| **Eingesammeltes landet immer beim Helden** — die Zone entscheidet nur, ob eingesammelt wird | **18** — Fähigkeiten, die Beute betreffen | **entfällt** für 18 — keine Fähigkeit betrifft Beute. Beute gehört zur Vaporium-Seite der Machtquellen; eine Fähigkeit, die mehr Beute bringt, wäre ein gelernter Zahlenbonus. Die Zeile bleibt ohne Ziel-Etappe stehen |
| **Wer profitiert vom Schadensbonus?** — Held allein oder jeder, der schießt; der Lernende entscheidet | **21a** — die Trefferrechnung wird gemeinsam | offen |
| **Das Set-Muster: merken → später abfragen** (`add()` … `in`) | **18** — derselbe Speicher, größer; **22** — Voraussetzungen prüfen genauso | **teilweise eingelöst** ✓ (18b — `welt.flags`) |
| `erkenntnisse` als Flag-Sammlung | **17c** — beeinflusst, welcher Sektor fällt; **18** — geht im zentralen Set auf | **teilweise eingelöst** ✓ (18b — geht in `welt.flags` auf; 17c nur in der Kür, Schritt 22) |
| Erkenntnisse ändern das Depot-Sortiment | **22** — Voraussetzungen im Ausbaubaum | offen |
| Erkenntnisse ändern Schadensberechnung | **21b** — Schwachpunkte und Widerstände | offen |
| Vorwissen über kommende Wellen | **17a** — der Generator macht das Vorwissen wertvoll | **eingelöst** ✓ (17a — das Vorwissen zeigt die Zusammensetzung der erzeugten Welle) |
| Erstes „erweitern ohne zu zerstören" | **26** — Tests machen daraus eine Gewissheit | offen |
| ⭐ **Die Umkehrtabelle „Sache → Voraussetzung"** — die Wirkung steht in einer Tabelle, nicht als `if`-Kette in der Logik | **18** — Fähigkeiten prüfen ihre Voraussetzungen genauso; **21b** — Widerstände und Schwachpunkte werden Tabellenzeilen; **22** — der Ausbaubaum ist dieselbe Form | **teilweise eingelöst** ✓ (18b — `AUSBAU_VORAUSSETZUNG` und die Spalte `"flags"` in `FAEHIGKEITEN`) |
| **Eine Quelle definiert die Flag-Wörter** — andere Tabellen verweisen, definieren nicht; ein Verweis ins Leere fällt nicht auf | **21b** — `Enum` macht daraus eine echte Prüfung | offen |
| **Drei Stufen: Fundstück ↔ Besitz ↔ Erkenntnis** — der Übergang von 2 zu 3 ist eine Handlung des Spielers | **18** — dieselbe Trennung bei Skillpunkten: haben ↔ ausgeben | **eingelöst** ✓ (18b, Konzept 8 — haben ↔ ausgeben) |
| **`Fundstueck` erbt von `Item`** — Einlösung aus **11**; ⚠️ offener Posten: `x`/`y` bedeuten im Inventar nichts mehr | **23b** — dort lässt sich das billig sauber machen | offen |
| **Fundstücke liegen an Koordinaten, eingesammelt wird nach der letzten Aufräumphase, nur in Zonen lebender Marines** — Einlösung aus **14b** | **19** — liegengebliebene Fundstücke gehören in den Spielstand; **21b** — Zonengröße wird zur Stellschraube mit zwei Seiten | **teilweise eingelöst** ✓ (19b) |
| ⭐ **Der Erweiterungstest: vierter Fund mit *vorhandener* Wirkungsart, Stellen zählen** — neue Daten ≠ neues Verhalten | **22** — derselbe Test noch einmal, die beiden Zahlen werden verglichen; **26** — Tests machen daraus Gewissheit | offen |
| **Drei Tabellen mit demselben Schlüsselsatz — heute bemerkt, nicht zusammengeführt** | **22** — dort werden sie zusammengelegt; die Notiz aus 15 ist die Vorarbeit | offen |
| ⚠️ **Entscheidung: Wird das Fundstück beim Analysieren verbraucht?** | **19** — bestimmt, ob Inventar und Erkenntnisse getrennt gespeichert werden müssen | **eingelöst** ✓ (19b — Inventar und Flags werden getrennt gespeichert, beide Entscheidungen sind damit gedeckt) |
| 👀 **Die Kopplungszeichnung** (wer muss von wem wissen?) — **nur bemerken, nichts reparieren** | **23b** — dieselbe Zeichnung ein zweites Mal, dann als Werkzeug; **27** — die schwächste Stelle liegt zwischen zwei Teilen | offen |

### Etappe 16 — Bug-Jagd II

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **Die Tick-Tabelle von Hand** (Phase für Phase, alle Einheiten nebeneinander) | **17b** — nur mit Seed noch etwas wert, sobald Zufall dazukommt; **27** — dieselbe Geduld, angewandt auf fremden Code | **teilweise eingelöst** ✓ (17b — Beweislauf mit festem Seed) |
| **Beobachtung → Hypothese → Experiment als verbindlicher Dreizeiler** | — Einlösung aus **8**; **26** — erst der Test, dann der Fix; **27** — dieselbe Form ohne Änderungserlaubnis | offen |
| Regel „nur eine Sache auf einmal ändern" | **21b** — Balancing auf einem Branch; **26** — ein Test prüft eine Annahme | offen |
| **Reihenfolgefehler als eigene Ursachenklasse** — Einlösung aus **12**. ⚠️ **Korrektur:** nicht der „vierte Fehlertyp" — Etappe 8 hat drei **Zeit**typen (wann fällt es auf) und die **Ort**frage (Code oder Daten). Die Reihenfolge ist eine dritte Antwort auf die Ortfrage und auf der Zeitachse immer Typ 3 | **17b** — mit Seed reproduzierbar; **28** — die Reihenfolge gilt 60-mal pro Sekunde | **teilweise eingelöst** ✓ (17b) |
| ⭐ **Die Fahndungsliste** — vierzehn Kandidaten aus neun Etappen, jeder mit einem von drei Wörtern versehen | **26** — jeder Fund ist ein Testkandidat; **27** — dieselbe Systematik ohne Änderungserlaubnis | offen |
| **Die Rückwärtsprobe** — Änderung zurücknehmen, kommt der Fehler wieder? | **26** — dort wird daraus „erst der Test, dann der Fix" | offen |
| **„Wann hätte ich es gemerkt, wenn es funktioniert hätte?"** — findet Mechaniken, die sich nicht beobachten lassen | **21b** — was man nicht beobachten kann, kann man nicht balancieren; **26** — und nicht testen | offen |
| **Die entschiedene Tick-Reihenfolge in `GELERNT.md`** | **19** — sie gehört zum Zustand des Spiels; **28** — sie wandert unverändert in die Loop | **teilweise eingelöst** ✓ (19c, Konzept 13 — sie steht im Code, nicht im Spielstand; deshalb nur zwischen zwei Takten speichern) |

### Etappe 17 — Der Wellengenerator ⭐  *(17a Zufall · 17b Der Seed · 17c Zwischen den Wellen)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **17a:** Budget statt Anzahl | **22** — Kosten stehen in denselben Daten; **25** — Wellenrezepte werden JSON | offen |
| ⭐ **17a:** Gewichtete Auswahl **von Hand** (`gewichtete_wahl()`, die Strecke) — `random.choices` nur 👀 | **17c** — Ereignisse benutzen dieselbe Funktion ✓; **25** — Gewichte werden Content | **teilweise eingelöst** ✓ (17c) |
| **17a:** `BEUTE` — typgebundene, gewichtete Beute, `"nichts"` als gewöhnliches Ergebnis, die Funde aus 15 mit kleinen Gewichten — die Antwort auf die Beutefrage aus 4 | **25** — wird Content | offen |
| 🧠 **17b:** Was ein Seed **nicht** festnagelt — Eingaben und die Reihenfolge von Sets | **19** — reicht der Seed, um nach dem Laden denselben Zufall zu bekommen?; **26** | **teilweise eingelöst** ✓ (19c, Design-Entscheidung — neu säen beim Speichern) |
| **17b/17c:** Neue Welt-Attribute `seed` (17b), `letzte_meldung`, `meldung_abgesetzt`, `funk_gehoert`, `generatorausfall`, `bericht` (17c) | **19** — alles außer `bericht` gehört in den Spielstand | **eingelöst** ✓ (19a — ⚠️ **Präzisierung:** ob `bericht` hineingehört, entscheidet der Lernende in der Inventur; gespeichert wird mitten in einer Welle) |
| **17c:** Meldungen sammeln (Weg A `notiere()` oder Weg B `melde(text, sofort=True)`) und der Wellenbericht — jede Marine-Klasse überschreibt `funkspruch()` | **20** — Debug-Zeile und Bericht bekommen getrennte Wege; **28** — zeichnen ↔ aufblitzen | **teilweise eingelöst** ✓ (20c — die Debug-Zeile geht über `welt.debug()` mit Schalter) |
| **17b:** Beweislauf mit `befehle17.txt`, festem Seed und `diff` | **26** — ein wiederholbarer Lauf ist ein Testfall | offen |
| **17c:** Die Reihenfolge der Pause zwischen den Wellen in `GELERNT.md` | **19** — gehört zum Zustand des Spiels, wie die Tick-Reihenfolge | **teilweise eingelöst** ✓ (19c, Schritt 22 — der Wellenstart nach dem Laden) |
| **17a:** Gegnertypen bekommen **Kosten und Gewichte** — die Typen selbst gibt es seit **6** | **23b** — `@dataclass`; **25** — JSON | offen |
| **17b: Fester Seed** ⭐ | **19** — gehört in den Spielstand; **26** — ohne ihn ist der Generator untestbar | **teilweise eingelöst** ✓ (19c — im Spielstand, dazu der Beweislauf) |
| **17b: Der Seed als sichtbare Entwicklerfunktion** (`Seed: 48173` in der Anzeige) | **16**-Rückgriff — ein Bug wird vorführbar statt jagdbar; **19** — wird mitgespeichert; **26** — Testvoraussetzung | **teilweise eingelöst** ✓ (19c — die Debug-Zeile zeigt nach jedem Speichern den neuen Seed) |
| **17c:** Ereignisse als Topf mit Bedingungen (`moegliche_ereignisse()`), ausgeführt in `ereignis()` | **25** — wandern nach `content/` | offen |
| **17c:** Einlösung `letzte_meldung` | — Einlösung aus **1** | **eingelöst** ✓ (17c) |
| ⭐ **17c (Kür):** Der endgültig verlorene Sektor | **19** — muss im Speicherstand stehen; **20** — Bewegung dorthin wird abgefangen. *Entfällt, wenn die Kür entfällt.* | **teilweise eingelöst** ✓ (19a; 20b — `gehe` in einen gefallenen Sektor über die Fahndung. *Entfällt mit der Kür.*) |
| **17c:** Die Zufallsregeln des eigenen Spiels in `GELERNT.md` — ein fester Satz, der Rest vom Lernenden, darunter mindestens eine bewusste Begrenzung des Zufalls | **19** — was muss der Spielstand dafür mitspeichern?; **26** — die Regeln werden Testfälle | **teilweise eingelöst** ✓ (19c — die Regel über das Säen wird neu gefasst) |
| 🧠 **17c: Entwicklerfrage** „Wie viel Zufall ist noch fair?" | `GELERNT.md` — wird in **22** und **26** wieder gelesen | offen |

### Etappe 18 — Fähigkeiten, Skillpunkte, Statuseffekte  *(18a Statuseffekte · 18b Skillpunkte und Voraussetzungen · 18c Fähigkeiten wirken)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **18a: `effekte` an jeder `Einheit`** — Dictionary Name → Restdauer, die Tabelle `EFFEKTE` sagt, was ein Effekt tut (**das Hauptthema**) | **19** — Wörter und Zahlen, überlebt JSON; **22** — Rekruten und Söldner tragen dieselben Effekte; **26** — „Effekt mit Dauer 3 macht dreimal Schaden" als Test | **teilweise eingelöst** ✓ (19b) |
| ⭐ **18a: Die Zeitsemantik-Tabelle für Effekte** — was „Dauer 3" für Held und Kamerad bedeutet, schriftlich | **26** — die Tabelle ist die Vorlage für den Test | offen |
| **18a: Abgeleitete Werte statt gespeicherter** — `aktueller_schaden()`, später `aktuelle_reichweite()` | **21a** — die Trefferrechnung fragt die Methode, nicht das Attribut | offen |
| **18b: `welt.flags` als zentrales Set** — `freigeschaltet`, `erkenntnisse`, `meldung_abgesetzt` in einem; `funk_gehoert` nach Wahl des Lernenden | **19** — Set → JSON ist nicht trivial | **teilweise eingelöst** ✓ (19a — sortiert als Liste, beim Laden wieder ein Set) |
| ⚠️ **18b: Die Invariante „kein Wort in zwei Quellen"** — ein Flag-Wort steht nie zugleich in `FUNDE` und `AUSBAUTEN` (aufgeschrieben, nicht geprüft) | **20** — wird eine Prüfung; **21b** — `Enum` als Alternative; **26** — ein Test | **teilweise eingelöst** ✓ (20c — `pruefe_tabellen()` beim Start) |
| ⭐ **18b: Skillpunkte** — Differenz aus erreichter Stufe und Gelerntem; jede Stufe zahlt einen aus | **19** — gehört in den Spielstand; **22** — Stufenschwellen in die Tabellen | **teilweise eingelöst** ✓ (19b) |
| **18b: `FAEHIGKEITEN` mit `"geraet"`, `"ab_level"`, `"flags"`, `"passiv"`** und `MAX_FAEHIGKEITSSTUFE` | **22** — wird mit `ABKLINGZEITEN` und `SCHWERE_KOSTEN` **eine** Tabelle; die Formeln `10 · s` vielleicht eine Tabelle pro Stufe; **25** — nach `content/` | offen |
| **18b: `kann_lernen()` liefert einen Grund oder `None`** | **20** — ein zweiter Weg, einen Grund zu tragen (Exception); die Frage, welcher Grund dem Spieler gehört | **teilweise eingelöst** ✓ (20b, Konzept 9 — Grund gegen Exception; der Befehl macht aus dem Grund einen Fehler) |
| **18b: Zwei Passive** — Zielhilfe (gekauft) und Standfest (gelernt) | **21a** — die Trefferrechnung fragt die Passiva ab; **22** — stehen in derselben Tabelle | offen |
| 👀 **18b: `and`/`or` geben einen der Werte zurück** — lesen, nicht schreiben | **23b** — dieselbe Form in fremdem Code | offen |
| 🧠 **18b: Die `or`-Falle bei `0`** | **27** — eines der Warnsignale | offen |
| **18c: Schwere Munition** im `vorrat`, Depotware | **19** — Teil des Speicherstands; **21b** — Preis als Stellschraube | **teilweise eingelöst** ✓ (19b) |
| **18c: `treffe(ziel, menge, welt)`** — ein Ort, an dem Schaden, Abschuss und Erfahrung zusammenkommen | **21a** — die Trefferrechnung setzt hier an | offen |
| ⭐ **18c: `setze_ein()` / `wirke()`** — die Oberklasse regelt den Ablauf, die Unterklasse liefert die Wirkung; `elif`-Ketten über die Fähigkeitsnamen | **23a** — die Ketten sterben, Wirkungen werden Funktionen im Dictionary | offen |
| **18c: `abklingzeiten` als Dictionary** Name → Rest | **19** — Teil des Speicherstands; **22** — Werte aus der Tabelle | **teilweise eingelöst** ✓ (19b) |
| **18c: `welt.minen` und `welt.mobiler_turm`** — die Mine zeigt auf ihren Besitzer, der Turm steht im Trupp **und** unter eigenem Namen | **19** — ein Verweis auf ein Objekt ist kein Wort; der Turm muss nach dem Laden wieder *ein* Turm sein | **eingelöst** ✓ (19b — Verweise als Stelle, Prüfung mit `is`) |
| **18c: Die Tick-Reihenfolge mit Minenphase** in `GELERNT.md` | **19** — gehört zum Zustand des Spiels; **28** — wandert in die Loop | **teilweise eingelöst** ✓ (19c, Konzept 13) |
| **18c: `will_einsetzen()` — die Kameraden-KI, zum letzten Mal** | **23a** — Zielauswahl und die doppelte Zielsuche aus Schritt 29 als Funktionen; **nach 27** alles Weitere | offen |
| **18c: Zwei Invarianten** — *jede aktive Fähigkeit steht in `ABKLINGZEITEN` und `SCHWERE_KOSTEN`, kein Passiv* · *`welt.mobiler_turm` und der Trupp zeigen auf dasselbe Objekt oder beide auf keines* (aufgeschrieben, nicht geprüft) | **19** — der Turm wird als Stelle gespeichert ✓; **20** — werden Prüfungen; **22** — die erste verschwindet mit dem Zusammenzug; **26** — Tests | **teilweise eingelöst** ✓ (19b; 20c — beide werden `assert`) |
| **18c: Gleichstandsregel der Heilung** — bei gleicher Lücke gewinnt, wer im Trupp vorne steht | **26** — ein Testfall mit zwei gleich Verletzten; **23a** — Zielauswahl als Funktion | offen |
| **18c: Drei Tabellen mit demselben Schlüsselsatz** (`FAEHIGKEITEN`, `ABKLINGZEITEN`, `SCHWERE_KOSTEN`), notiert | **22** — Zusammenzug | offen |
| 🧠 **Entwicklerfrage** „Wo gehört Zustand hin — Einheit oder Welt?" | **22** — dort wird die Antwort auf die Probe gestellt | offen |

### Etappe 19 — Speichern und Laden  *(19a Dateien und JSON · 19b Objekte werden Daten · 19c Das Spiel überlebt das Beenden)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **19a:** JSON-Denkweise — Zustand, Inhalt, Bild; *gespeichert wird Zustand* | **25** — Content-Format beruht darauf; die Grenze Zustand/Inhalt wird zur Ordnerstruktur | offen |
| ⭐ **19a: Serialisierung als Abbildung — und die Frage, ob sie verlustfrei ist** | **25** — dieselbe Skepsis gegenüber fremden Dateien; **26** — Speichern und Laden als Test | offen |
| **19a:** `pathlib`, `with open`, `json` | **25** — `content/` laden; **24** — Importe verstehen | offen |
| **19a: `SPIELSTAND_VERSION`** — weist fremde Stände ab, rechnet nicht um | **22** — die erste Formatänderung, die Nummer wird erhöht; **25** — Content-Version; **26** — Test für alte Stände | offen |
| ⭐ **19a: Die Zustandsinventur** in `GELERNT.md` — jedes Attribut mit Entscheidung | **21b** — `Enum`-Zustände müssen übersetzt werden; **22** — Rekruten und Tabellen ändern die Inventur; **26** — die Inventur ist die Testliste | offen |
| **19a: Zahlenschlüssel werden Text** | **25** — Inhalte mit Zahlenschlüsseln (Stufentabelle) | offen |
| **19b: `als_daten()` / `aus_daten()` an jeder Klasse** — erst erzeugen, dann überschreiben | **21b** — Status als `Enum` braucht eine Übersetzung; **23b** — `@dataclass` als Vergleich; **25** — Inhalte kommen auf demselben Weg herein | offen |
| ⚠️ **19b: Der Klassenname ist die Kennung im Spielstand** — Umbenennen bricht alte Stände, die Reparatur ist eine Zeile im Dictionary *Klassenname → Klasse* | **22** — beim ersten Umbau prüfen, ob die Versionsnummer steigen muss; **25** — Kennungen werden von Namen getrennt und eindeutig gemacht | offen |
| **19b: Verweise als Stelle, Prüfung mit `is`** | **25** — Verweise über Kennungen, die eindeutig *gemacht* werden (Weg C) | offen |
| **19b: Eine Funktion erzeugt Items aus Kennungen** — Kauf und Laden teilen sie | **22** — ein Eintrag pro Ding; **25** — Kennungen aus Dateien | offen |
| **19c: Zähler als Rest gespeichert, nicht als Fortschritt** — ein laufender Bau behält seinen alten Rest, wenn sich die Bauzeit ändert | **22** — muss Änderungen an Bauzeiten überleben; dort wird die Wahl spürbar | offen |
| **19b:** Die Rundreise mit `diff` | **26** — der erste Test, der speichert, lädt und vergleicht | offen |
| **19c:** Neu säen beim Speichern, Laden mit dem gespeicherten Seed — die Regel über das Säen neu gefasst | **26** — ein gespeicherter Lauf ist ein Testfall | offen |
| ⭐ **19c: Der Beweislauf** mit `befehle19a.txt` und `befehle19b.txt` | **26** — der erste Test über ein ganzes Spiel | offen |
| **19c: Die Startfrage `Spielstand laden?`** — jede Befehlsdatei beginnt mit `n` oder `j` | **20** — ungültige Antworten; **26** — Befehlsdateien als Testeingaben | **teilweise eingelöst** ✓ (19c — jede andere Antwort heißt neues Spiel; 20 hat dort nichts mehr zu fangen) |
| **19c: Die Entscheidung zum Spielende** (Rücksetzpunkt oder löschen) | **21b** — Balancing: wie viel Rücksetzen ist fair? | offen |
| **19c:** `JSONDecodeError`, `KeyError`, fremde Werte beim Laden — heute Abstürze | **20** — abfangen, Meldung für Spieler gegen Entwickler; **25** — drei Stufen von „gültig" | **teilweise eingelöst** ✓ (20a, Schritt 4 — `JSONDecodeError` und `KeyError`; fremde Werte bleiben **25**) |
| 👀 **19c:** Atomares Schreiben (temporäre Datei, dann umbenennen) — **Kür, nicht Pflicht** | **20** — `finally` hilft nicht gegen Stromausfall; **27** — in fremdem Code als Qualitätsmerkmal erkennen | **teilweise eingelöst** ✓ (20c, Konzept 15) |
| 🧠 **19c: Entwicklerfrage** „Was muss ein Spielstand garantieren?" | **22** — beim ersten Erhöhen der Versionsnummer wiedergelesen; **25** — dieselbe Frage für Content | offen |

### Etappe 20 — Wenn der Spieler Unsinn eingibt  *(20a Fangen · 20b Werfen · 20c Prüfen und trennen)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **20a:** 🚨 breites `except` als Warnsignal — Typ 1 wird Typ 3 | **27** — eines der drei Risiken, die du finden sollst | offen |
| **20a: Die Chaos-Datei** `chaos.txt` mit zwei Spalten — Abstürze und stille Falschheiten | **26** — jede Zeile ein Testfall | offen |
| **20a: Prüfen oder fangen** — die Faustregel | **25** — Inhalte von außen: strukturell prüfen statt fangen | offen |
| **20a:** Kaputter Spielstand wird abgefangen — ⚠️ ein falscher **Wert** (`"viel"`) nicht | **25** — drei Stufen von „gültig" | offen |
| 👀 **20a:** Fehlerklassen haben Oberklassen (`JSONDecodeError` ist ein `ValueError`) | **25** — bei Bedarf eine Unterklasse von `SpielFehler`; **27** — Bibliotheken lesen | offen |
| **20b: Genau eine eigene Fehlerklasse** `SpielFehler` und **eine** Stelle, die sie fängt | **24** — bekommt ein eigenes Modul; **25** — Content-Fehler bekommen eine eigene; **26** — ein Test prüft, *dass* ein Fehler fliegt | offen |
| ⭐ **20b: Nur Wege des Spielers werfen** — Kameraden, Tick und Pause fragen vorher | **23a** — Strategien als Funktionen bleiben fehlerfrei; **26** | offen |
| **20b: Grund-oder-`None` gegen Exception** — fragen gegen verlangen | **23b** — Typannotation `str \| None`; **27** — in fremdem Code beide Stile erkennen | offen |
| **20b:** `else` beim `try` — der Tick nur nach Erfolg | **28** — dieselbe Frage in der Spielschleife | offen |
| **20c: Invarianten als `assert`** — Tabellen beim Start, Zustand nach jedem Tick, Munition im Nachladen | **21a** — drei `assert`-Zeilen zur Schadensformel; **22** — Tabellen-Prüfungen ändern sich mit dem Zusammenzug; **26** — Tests | offen |
| **20c: `DEBUG` und `welt.debug()`** — ein Schalter für Entwicklerausgaben | **24** — `logging` ersetzt den Schalter, wenn es Module gibt; **28** — Debug-Anzeige im Fenster | offen |
| 👀 **20c:** `finally` — und die Tabelle, wann es nicht läuft | **28** — Autosave bei Fensterschließung, *falls* du es dann brauchst | offen |
| 👀 **20c:** Logging-Stufen lesen können (`debug`…`error`) | **24**; **27** — fremde Projekte loggen statt zu drucken | offen |
| 🧠 **20: Entwicklerfrage** „Welchen Fehler zeige ich dem Spieler, welchen dem Entwickler?" | **25** — dieselbe Frage für Inhalte, die nicht von dir stammen | offen |

### Etappe 21–22

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **21a:** Trefferrechnung mit zwei Rückgabewerten | — Einlösung aus **6** (Komma-Falle) und **7b** (`return` statt `print`); **26** — erster `parametrize`-Test | offen |
| **21a:** Drei `assert`-Zeilen zur Schadensformel | — Einlösung aus **7b**; **26** — dieselben Zeilen in einer Testdatei | offen |
| **21b:** `Enum` für **die Spielzustände** — eines genügt | — Einlösung aus **12**; **28** — Pygame braucht sie für Modi | offen |
| **21b:** `Enum` ist nicht automatisch besser als ein String | **25** — aus JSON kommen wieder Strings zurück | offen |
| 👀 ⭐ **21b (Kür):** Schadenstypen und Widerstände | **22** — stehen in den Waffendaten; **25** — lassen sich dort billiger nachrüsten als heute | offen |
| **21b:** Erster Branch (Balancing) | **24** — Branches systematisch, Merge oder Verwerfen des Balancing-Branches | offen |
| 🧠 **21b: Entwicklerfrage** „Welche Werte gehören wirklich zum Kampfsystem?" | **22** — Daten oder Verhalten? | offen |
| **22:** Die Zahlentabellen als Daten — **Fähigkeiten, Ausbaustufen des Basisturms, Söldner, Stufenschwellen** | **25** — wandern nach `content/` | offen |
| ⭐ **22: Genau ein Turm in der Basis, dafür mit Ausbaustufen** — die Tabelle beschreibt fünf Stufen desselben Turms, nicht fünf Turmtypen | **25** — Stufen als Content; **21b** — Balancing der Stufen | offen |
| ⚠️ **22: Was ausdrücklich nicht gebaut wird — freies Bauen beliebig vieler Geschütze.** Das Spiel ist ein Hero-Survival, kein Tower Defense; Türme sind eine Beigabe, keine Mechanik | durchgehend — Riegel; **nach 27** als bewusste Erweiterungsoption | offen |
| ⚠️ **22: Basisausbau bewusst zurückgestellt.** Er ist heute kein Teil des Spiels. **Der natürliche Ort wäre 22**, sobald die Ausbaustufen-Tabelle steht — dann ist ein zweites ausbaubares Objekt eine zweite Tabelle und keine neue Mechanik | **nach 27** — falls gewünscht, ohne Umbau am Rest | offen |
| **22: Söldner und Rekruten als Tabelle** — Kosten, Vertragsdauer, Werte, **Nachschubzähler**. ⭐ Die Modellierungsfrage dahinter: **eine gekaufte Stelle, die neu besetzt wird, ist etwas anderes als eine Figur, die ausfällt und wieder aufsteht** | — Einlösung aus **12** (Einheitenliste), **13** (Zähler-Muster) und **11** (`Einheit` als Basis); **25** — Söldnertypen als Content | offen |
| **22:** Voraussetzung als schlichtes Feld (*Stufe 3 braucht Energiezelle*) | **25** — dieselbe Prüfung, Daten von außen | offen |
| **22:** Wiedervorlage der Vererbungsfrage | **25** — die Antwort zeigt sich beim Verdaten | offen |
| 👀 **22:** Komposition als dritte Spalte — **erwähnt, nicht gebaut** | — Einlösung aus **11**; **nach 27** als Umbaumöglichkeit | offen |
| 🧠 **22: Entwicklerfrage** „Was ist Inhalt, was ist Verhalten?" | **25** — die Linie wird zur Ordnerstruktur | offen |

### Etappe 23–26

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **23a:** Befehls-Dictionary (Funktionen als Werte) | — Einlösung aus **3b** und **7a**; **25** — Befehle können Content werden | offen |
| **23a:** Zielauswahl-Strategien als Funktionen | — Einlösung aus **14b** und **18**; **28** — dasselbe Muster bei Eingabe-Callbacks | offen |
| **23a:** Comprehensions | — Einlösung aus **14a** (Schleifenformen) und **14b** (Reichweitenmengen) | offen |
| 👀 **23a:** `*args` / `**kwargs` — erkennen, nie selbst schreiben | **24** — `fremde_funktion(**config)` beim Lesen fremder Bibliotheken | offen |
| **23b:** `@dataclass` und Typannotationen | — Einlösung aus **6** und **17a** (die Gegnertyp-Einträge werden zum Wertetyp); **25** — dieselben Felder als JSON | offen |
| 👀 **23b:** Dekoratoren — die Zeile darunter geht durch die Zeile darüber | — Einlösung aus **11** (`@property`); **26** — `@pytest.mark.parametrize` | offen |
| **23b: Die Kopplungszeichnung zum zweiten Mal** | — Einlösung aus **13** und **15**; **27** — Frage 7 ist eine Kopplungsfrage | offen |
| **23b:** Lesekompetenz für fremden Code, **Leseleiter Stufe 4** | **27** — das eigentliche Ziel des Projekts | offen |
| 🧠 **23b: Entwicklerfrage** „Wer muss wen kennen?" | **24** — zirkuläre Importe beantworten sie schmerzhaft | offen |
| **24:** Modulstruktur | **28** — Pygame kommt als eigenes Modul dazu | offen |
| **24:** Der Satz *„nicht kaputt, nur zu groß"* | **27** — dieselbe Erwartung an fremde Projekte | offen |
| 👀 **24:** `pyproject.toml`, Versionsangaben, semantische Versionierung | **27** — der schnellste Einstieg in ein fremdes Repo | offen |
| **24:** Merge und Konflikt am Balancing-Branch | — Einlösung aus **21b** | offen |
| **24:** Pull Requests **ausdrücklich nicht** — allein ohne Gegenüber | — bewusste Auslassung, kein offener Posten | — |
| **24:** Eine fremde Bibliotheks-API lesen (`set_mode`) | **28** — dieselbe Zeile, jetzt benutzt; **27** — dieselbe Technik am ganzen Repo | offen |
| **24:** Die Komma-Falle im fremden Code wiedererkannt | — Einlösung aus **6** | offen |
| 🧠 **24: Entwicklerfrage** „Wann macht Aufteilung Code besser, wann nur komplizierter?" | **27** — Urteil über fremde Strukturen | offen |
| **25:** Content in JSON | **die Prämisse löst ihre Schuld ein** — dreißig Gegnertypen ohne Code | offen |
| **25: Der Erfolg: neuer Gegnertyp ohne eine Zeile Python** | — Einlösung aus **22**; Beweis für datengetriebenes Design | offen |
| **25: Drei Stufen von „gültig"** (syntaktisch → strukturell → inhaltlich) | — Einlösung aus **8** (Fehler in den Daten) und **19** (Verlust beim Laden); **26** — jede Stufe wird ein Test | offen |
| **25:** Liste der Validierungsfälle | **26** — genau diese Liste wird zur Testdatei | offen |
| 🧠 **25: Entwicklerfrage** „Wem vertraue ich — Code, Daten oder keinem von beiden?" | **27** — dieselbe Frage an fremden Code | offen |
| **26:** Tests | **28–30** — Beweis, dass Grafik die Logik nicht bricht | offen |
| **26:** `pytest` ist derselbe `assert` in einem Rahmen | — Einlösung aus **7b** und **21a** | offen |
| **26:** Der Seed macht den Generator testbar | — Einlösung aus **17b** | offen |
| 🧠 **26: Entwicklerfrage** „Was beweist ein grüner Test eigentlich?" | **27** — „kein einziger Test" als Warnsignal | offen |

## Teil B — Was eine späte Etappe erwartet

Umgekehrte Richtung. Vor jeder dieser Etappen prüfen, ob die Voraussetzung wirklich dasteht — sonst fehlt die Pointe.

| Etappe | Erwartet aus | Was da sein muss |
|---|---|---|
| **3a** (Schleife) | 1, 2 | `wellen_bis_evakuierung`, `kern_integritaet` als Abbruchbedingung |
| **3b** (Befehle) | **3a**, 2 | Eine laufende Schleife · die `if`/`elif`-Kette und `.strip()` |
| **3c** (Kampf, Anzeige) | **3b**, 1 | Eine Befehlskette, in die Wirkung eingehängt wird · `munition`, `kern_integritaet` |
| **4** (Ausrüstung) | 1, 2, **3a**, **3b**, **3c** | „Name zeigt auf Wert", Truthy und die `0`, `.strip()`/`.lower()`, `range()`-Zählung ab 0, **die einwortige Befehlssprache, die hier durch `.split()` abgelöst wird**, die Gegnerzahl aus 3c, die Balkendarstellung |
| **5** (Vorposten) | 3, **4** | `.split()` für `kaufe medkit`, Vaporium als Währung, Beute pro Ort, **die Kennung-oder-Anzeigename-Entscheidung** (das Depot braucht die zweite Stelle), **mehrfach `"chitinpanzer"` in der Liste als erlebtes Problem**, der Datenkern als Einzelstück daneben |
| **6** (Datenstrukturen) | **4**, **5** | Mutable/immutable, `in` bei Liste und Dictionary, doppelte Käufe als Problem, **die Frage „Menge oder mehrere Dinge?" — in 4 einmal gestellt, hier für vier Strukturen beantwortet**, **die Gegnerliste als Positionszahlen und der Kaufvorgang, an den sich `AUSBAUTEN` anlehnt**, **`magazin_groesse` aus 12b — das Großmagazin hebt den Wert, nicht das Nachladen** |
| **7a** (Funktionen) | 3, 4, 5, **6** | Die Platzhalterformel, die gewachsene `elif`-Kette, **die Prüfketten aus 5 und 6**, die Zustandsübersicht aus 5 |
| **7b** (Trennung) | **7a**, 1, 3c, 4, 5, **6** | Funktionen als Bausteine **und** die Zeichenschnipsel aus 1 (Kopf), 3c (Balken), 4 (Bahn), 5 (Grundriss), 6 (Typzeichen) |
| **8** (Bug-Jagd I) | 1, **3a**, **3c**, **4**, 5, **7a**, **7b** | Der `print`-Reflex aus allen Fundament-Etappen · `Strg + C` und die Entwicklerbefehle aus 3a · der nicht kappende Balken aus 3c · die Anmarschbahn als Messgerät aus 4 · der stille Schlüssel-Tippfehler aus 5 · **das dreischrittige Bauen aus 4, aus dem Halbieren wird** · der Aufrufstapel aus 7a · **ein Programm, das aus Funktionen besteht, die man einzeln verdächtigen kann** |
| **9a** (Objekte) | **7a** | Die lange Parameterliste **und die Notiz, welche Werte immer gemeinsam auftreten** — ohne den Schmerz wirkt `self` willkürlich |
| **9b** (`__repr__`) | **9a**, 8 | Klassen **und** der Debugger, sonst fehlt der Anlass |
| **10** (Komposition) | **4**, 9a | Mutable vs. immutable, Aliasing bei Objekten, `__init__` mit Standardwerten |
| **11** (Vererbung) | 2, **4**, **6**, 9a, **10** | **Die `elif`-Kette der Klassenwerte**, Komposition als Vergleichsgrundlage, **die Notizliste „hier war ein String zu dünn" aus Etappe 4 und der Schmerz der zwei parallelen Listen aus Etappe 6** — zusammen sind sie die Begründung für Klassen. *Hier — und nicht in 2 — entsteht der Trupp.* |
| **12** (Tick) | 1, 3a, 4, 6, 9, 11 | Weltzustand in Variablen, **die Hauptschleife**, „nicht iterierend entfernen", `Einheit` als Basis, **vier Marine-Objekte aus 11** |
| **13** (Bauzeit) | **5**, 11, 12 | `sektoren` veränderbar, **Entscheidung zum versiegelten Sektor**, **die Werkstatt als Ort mit ortsgebundenem Befehl**, laufender Tick |
| **14a** (Raster) | 3a, **4**, 5, 6 | `range()`, **die Anmarschbahn als eine Zeile und die Entscheidung, ob sie der Zustand oder sein Bild ist**, `.join()`, das dreischrittige Bauen, Dictionary als Gegenbeispiel, Tuple |
| **14b** (Reichweite, Bewegung) | **14a**, 6, 10, 12, 13 | Das Raster, **Set und Tuple**, `self.position`, Trupp-KI Stufe 1, das Geschütz |
| **15** (Erkenntnisse) | 4, **6**, 12 | Der Datenkern aus 4, **`GEGNERTYPEN` und `gesehene_gegnertypen`** — Erkenntnisse hängen sich an vorhandene Typ-Einträge, sie erfinden keine |
| **16** (Bug-Jagd II) | **8**, 12, 13, 14b | Debugger, Halbieren, das eigene Protokoll, **eine notierte Tick-Reihenfolge aus 12**, mehrere Systeme im selben Tick |
| **17a** (Zufall) | 3a, 4, 5, **6**, 9a, 15 | `range()` über Wellen, **die Gegnertypen und die `if`/`elif`-Wellenkette, die hier durch das Budget ersetzt wird**, `Gegner` als Klasse, Vorwissen aus Erkenntnissen, **die Beutefrage aus 4 und die Fundtabelle aus 15** |
| **17b** (Seed) | **17a**, 7, 8, **16** | `befehle.txt` und `diff`, der bedingte Breakpoint, **das Bedürfnis nach Reproduzierbarkeit aus 16** |
| **17c** (Bericht, Ereignisse) | **17a**, **17b**, **1**, 2, 7, 11, 12, 13 | **`letzte_meldung` vom ersten Tag**, `meldung_abgesetzt`, das Standardargument aus 7, **die vier Marine-Klassen und das Überschreiben aus 11**, Einheiten-Gedächtnis, Zustand gegen Ereignis |
| **18** (Fähigkeiten) | 2, 5, 6, 9a, 10, 11, 13, 14b, 15, 16, **17b** | Verknüpfte Bedingungen, `klassengeraet`, **Set und Mengenoperationen**, `AUSBAUTEN` und die Zielhilfe, die Stufentabelle und `level`, `None` ≠ `0`, **die Zählerphase und der Stufenaufstieg aus 13**, `abstand()` und `felder_in_reichweite()` aus 14, **`FUNDE` und die Erkenntnis-Flags**, die Tick-Reihenfolge aus 16, **`befehle17.txt` und der Schalter `SEED` für zwei reine Umbauten** |
| **19** (Speichern) | 0, 3a, 5, 6, 7, 10, 11, 12, 13, **14a**, 15, 17b, 17c, 18 | `.gitignore` mit `saves/`, `beenden`, die Karte, Sets und Tuples, **das Standardargument und `diff`**, `None` und `is`, **das Dictionary *Kennung → Klasse***, `self.zeit`, halb fertige Zähler, `welt.fundstuecke`, **der Seed und `befehle17.txt`**, Restdauern, `welt.flags`, Minen und mobiler Turm. *`erkundete_felder` nur, wenn die Kür in 14b gebaut wurde.* |
| **20** (Fehlerbehandlung) | 1, 2, 3b, **4**, 5, 7a, 8, 10, 13, 17b, 18b, **19** | **`int()` und `ValueError` aus Etappe 1**, `else`-Zweige, **drei Stellen aus Etappe 4: volles Inventar, `remove()` ohne Element, Befehl ohne zweites Wort**, die drei Kaufbedingungen, Randprüfung |
| **21a** (Rechnung) | 6, **7a**, **7b**, 10, 14b | `berechne_schaden()`, Komma-Falle beim Tuple, `return` statt `print`, Slots, Reichweite |
| **21b** (Zustände, Branch) | **21a**, 12, 11, 0 | Die Zustandsstrings aus 12, Waffenklassen, Git-Minimalset |
| **22** (Tabellen) | **5**, 11, 13, 15, 18 | **Entscheidung zur ausverkauften Ware**, **der Kauf, der keine Warennamen kennt**, die Vererbungsfrage **und die Komposition aus 11**, das Zähler-Muster, Erkenntnisse als Voraussetzung |
| **23a** (Lesen) | 7a, 11, 14a, 14b | Die `elif`-Kette in `verarbeite_befehl()`, Dunder-Methoden, Schleifenformen, Reichweitenmengen, Zielsuche |
| **23b** (Modellieren) | **23a**, 13, 15, 17a | Der Kopplungs-Umweg, **die Zeichnung aus 15**, Gegnertypen als Datensätze |
| **24** (Module) | 0, 7a, 12, **21b** | `requirements.txt`, „eine Funktion, ein Zweck", die gegenseitige Abhängigkeit Welt ↔ Einheiten, **der Balancing-Branch als Merge-Objekt** |
| **25** (Content) | 5, 11, 17a, 18, 19, 21b, 22 | Alle Inhalte müssen sauber von der Logik getrennt sein — **und die Serialisierungs-Skepsis aus 19** |
| **26** (Tests) | **7b**, 8, 13, **17b**, 19, **21a**, 22, 25 | **Die `assert`-Zeilen aus 7b und 21a**, das Fehlertagebuch, Off-by-One bei Zählern, **der feste Seed**, **die Validierungsliste aus 25** |
| **27** (Fremden Code lesen) | 0, 8, **9–23 (die Leseleiter)**, 24 | Debugger, alle vier Lesestufen, das Kopplungsbild, Modulverständnis, **`pyproject.toml` lesen können** |
| **28** (Spielschleife) | 3a, **7b**, 12, 13, 16, 24 | Loop, **`return` statt `print`** und die getrennte Zeichenschicht, Tick, **die entschiedene Tick-Reihenfolge**, `bauzeit = 180`, Module |
| **29** (Tilemap) | 5, 7b, **14a** | Das Raster im unveränderten Format, `zeichne_vorfeld()` als austauschbare Schicht, der Grundriss als Kulisse |
| **30** (Isometrie) | 14a, 29 | Rasterkoordinaten und Zeichenreihenfolge |

**Die kritischste Zeile ist Etappe 17.** Sie ist der einzige Punkt, an dem etwas aus Etappe 1 direkt eingelöst wird — über vier Monate hinweg. Wenn du dort ankommst und die Rückblende nicht schreibst, war der ganze erste Tag umsonst begründet.

**Die drittkritischste ist Etappe 11.** Der Trupp entsteht erst dort — Etappe 2 setzt nur noch die gewählte Klasse. Wer in 11 die vier Objekte nicht tatsächlich nebeneinander erzeugt, hinterlässt drei tote Klassen, und die Etappen 12, 14b, 16, 18 und 23a verlieren ihren Gegenstand.

**Die zweitkritischste ist Etappe 28.** Sie löst keine Erzählschuld ein, sondern eine strukturelle: Wenn die Entscheidung aus Etappe 7 nicht durchgehalten wurde — Logik gibt zurück, Darstellung gibt aus — dann ist Block 4 kein Aufsatz, sondern eine Neuschreibung.

---

## Teil C — Durchgehende Fäden

Kein einzelner Verweis, sondern etwas, das über den ganzen Plan läuft.

**Die Darstellung** — Etappe 1 (fester ASCII-Kopf) → **2 (hält bewusst still: nur mehr Variablen im selben Briefing)** → **3c (Balken beim `status`-Befehl; der Kopf bleibt unangetastet)** → **4 (die Anmarschbahn — eine Zeile, in der man Bewegung sieht; ab hier ist die Anzeige auch Messgerät)** → **5 (der Grundriss mit Markierung — handgezeichnet, nur die Markierung kommt aus den Daten)** → **6 (die Bahn zeigt verschiedene Zeichen je Gegnertyp — die Darstellung liest zum ersten Mal aus zwei Quellen)** → 7b (eigene Zeichenschicht, die nichts entscheidet) → **14a (aus einer Zeile wird ein Raster)** → 28 (dieselbe Schicht, andere Ausgabe) → 29 (Kacheln) → 30 (Isometrie). Der Faden hat zwei Zwecke: Das Spiel ist früh sichtbar, und die Trennung Logik/Darstellung wird eingeübt, lange bevor sie in Etappe 28 zur Bedingung wird.

**Die Leseleiter** ⭐ — vier Stufen mit festen Fragen. Stufe 1 (Benennen): Etappe 9–11, 5–10 Zeilen. Stufe 2 (Verfolgen): 12–16, 15–30 Zeilen — zahlt direkt in 16 bei den Reihenfolgefehlern. Stufe 3 (Zusammenhänge): 17–22, 30–60 Zeilen. Stufe 4 (Beurteilen): ab 23b, echter KI-Code, hier kommt die sechste Frage dazu → **27 (ganzes Repo, Frage 7 ist Frage 6)**. Die Stufen dürfen nicht übersprungen werden: Frage 6 setzt voraus, dass Alternativen bekannt sind.

**Die Null-Falle** — Etappe 2 (truthy/falsy, `0` ist falsy) → **4 (`if inventar:` — die leere Liste ist falsy, und dazu die Frage: *kann diese Variable legitim `0` sein?*)** → 10 (**`None` ≠ `0`**: keine Waffe ≠ leere Waffe) → 14a (Feld 0, Index 0, `x = -1` greift von hinten) → **18b (`x or standard` greift falsch, wenn `0` gültig ist — dort 🧠, als Lesefalle; die Form selbst bleibt 👀)** → 19 (`null` in JSON) → 20 (drei verschiedene Fehlermeldungen statt einer). In diesem Setting ist `0` überall — deshalb ist das der wichtigste der Lesefäden.

**Die drei Schleifenformen** 👀 — angelegt in Etappe 3a (`for x in dinge`) und 5 (`.items()`) → **14a (Erkennungsdrill mit allen dreien, `enumerate()` kommt dazu — zwei Minuten, kein Umbau)** → 23a (dieselben Formen als Comprehension). **Ziel ist Erkennen, nicht Schreiben** — der ganze Faden liegt auf Stufe 👀.

**Namen und ihre Herkunft (Modul-Lesen vor Modul-Bauen)** — Etappe 9 (jede Leseübung fragt: aus dieser Datei, aus einem Import, oder von `self`?) → 11 (Vererbung: ein Name kann aus der Oberklasse kommen) → 23a (Funktionen als Werte — Namen zeigen auf Funktionen) → **24 (jetzt baust du selbst Module; die fremde Bibliothek liest du am selben Tag)** → 27 (Importe als Inhaltsverzeichnis eines fremden Repos). Absicht: Bei Etappe 24 soll `from einheiten import Marine` ein Wiedererkennen sein, kein Rätsel.

**Behauptungen über Zustand** — Etappe 7b (`assert` als 👀-Ausblick, drei Zeilen, **kein** Testeinstieg) → 13 (Zähler-Invarianten) → 20 (Prüfen vorher ↔ Fangen hinterher) → 21a (drei `assert`-Zeilen zur Schadensformel — die erste echte Anwendung) → 25 (die Validierungsliste) → **26 (`pytest` ist derselbe `assert` in einem Rahmen)**. Und als Lesefrage ab 7b durchgehend: *Welche Annahmen macht diese Funktion, und prüft sie eine davon?*

**Wichtig für die Buchführung:** Zwischen 7b und 26 liegen Monate, und in dieser Zeit steht `assert` bewusst still. Wer in 13 oder 20 daraus schon Testarbeit macht, verbrennt Etappe 26 und überlädt die Zwischenetappen. Der Faden ist absichtlich dünn.

**Kopplung als Lesekriterium** — Etappe 12 (👀 `update(self, welt)`: nur bemerken) → 13 (der Umweg: warum kennt das Geschütz die ganze Welt?) → **15 (👀 die Zeichnung zum ersten Mal — fünf Minuten, nichts wird repariert)** → **23b (dieselbe Zeichnung zum zweiten Mal, jetzt als Werkzeug und im Vergleich)** → 24 (zirkulärer Import macht Kopplung schmerzhaft) → 27 (die schwächste Stelle liegt zwischen zwei Teilen, nicht in einem).

Der Faden liegt bis 23b vollständig auf Stufe 👀. Das ist Absicht: Kopplung ist das wichtigste Beurteilungskriterium des ganzen Plans und gleichzeitig das, an dem ein Anfänger am schnellsten hängenbleibt, wenn er es zu früh reparieren soll.

**Der Trupp** ⭐ — **Etappe 11 (hier entsteht er: vier Objekte, sichtbar nebeneinander — einer gesteuert, drei autonom)** → **12 (die drei anderen bekommen `update()`: feuern, wenn in Reichweite)** → 13 (ausgefallener Kamerad folgt dem Zähler-Muster; nur der Held hält das Spiel an) → **14b (nächsten Gegner suchen, Zone halten)** → 16 (sie stehen in der Tick-Tabelle) → 18 (sie nutzen Fähigkeiten — und hört hier auf) → 23a (Zielauswahl-Strategien gelten für Kameraden, Turret und Söldner gleichermaßen). Zweck: Ohne den Trupp sind drei der vier Klassen toter Code, und Vererbung in Etappe 11 bleibt eine Behauptung.

**Der Held ist genau einer** — das ist die Prämisse des Spiels und keine Vereinfachung, die später fällt. Der Spieler steuert eine Figur; die anderen drei kämpfen mit, entscheiden aber selbst. Daran hängt, warum Etappe 11 zwei Steuerungsquellen auf einer Basisklasse braucht und warum Etappe 12 überhaupt zwischen *gesteuert* und *autonom* unterscheidet.

**Das Klassengerät → die Klassenfähigkeit** ⭐ — der Faden, der die Klassenwahl aus Etappe 1 bis zum Ende trägt: **2 (`klassengeraet` als String pro Klasse — angezeigt, nie abgefragt)** → 4 (Sperre: es gehört nicht ins Inventar) → **5 (Sperre: es steht in keiner Warentabelle — das Depot verkauft keine Identität)** → 10 (Sperre: das Ausrüstungs-Objekt für *gekaufte* Teile ist etwas anderes und heißt deshalb anders) → **13 (Sperre eingehalten: die geübte Fähigkeit bleibt erfunden, und der Turm, der dort gebaut wird, ist der klassenunabhängige Basisturm — nicht der Geschützturm des Engineer)** → **18 (Zahltag: Granatwerfer, Durchschlag, Mine und Turm, Heilung und Aura — und die Spalte `"geraet"` in `FAEHIGKEITEN`)** → **22 (wird zur Spalte der gemeinsamen Fähigkeitentabelle)**.

⚠️ **Vier Sperren auf sechzehn Etappen — genauso viele wie beim Erfahrungszähler.** Das ist kein Zufall: Beide Fäden sind sichtbare Werte ohne Wirkung, und beide werden an jeder Etappe, an der sie „fast fertig" aussehen, ausdrücklich stillgelegt.

**Die zwei Machtquellen** ⭐ — die Entwurfsregel, die ab Etappe 5 mitläuft und in 18 geprüft wird: **Erfahrung entscheidet, *was du kannst*; Vaporium entscheidet, *womit du es tust*.** → 5 (Vaporium kauft Verbrauchsgüter, keine Fähigkeiten) → 13 (die Abklingzeit begrenzt den Einsatz, nicht den Zugang) → 14b (die Barrikade ist gekauft, also Vaporium — sie schaltet nichts frei) → **18 (Skillpunkte kaufen Können, schwere Munition bezahlt den Einsatz)** → **22 (in der Fähigkeitentabelle stehen `ab_level` und `kosten` nebeneinander — dort wird die Regel sichtbar oder verletzt)** → 21b (erst dann wird balanciert).

**Die Kosten einer Entscheidung wachsen mit der Zeit** ⭐ — der Faden, der Umbauten erklärbar macht, statt sie wie Strafen aussehen zu lassen: **5, Konzept 9 (Kennung gegen Anzeigename — „die Rechnung für eine Entscheidung")** → **5, Schritt 9 (die Umstellung auf `vorrat` kostet zehn Fundstellen; die Entscheidung aus Etappe 1 war trotzdem richtig)** → **7 (der erste Umbau ohne äußeren Zwang — nur weil er jetzt billiger ist als später; dazu der `diff`-Beweis)** → 9a (die lange Parameterliste aus 7a wird fällig) → 11 (die `if`/`elif`-Kette aus Etappe 2 wird fällig) → 15/24 (dieselbe Umstellung über mehrere Dateien, ein Vielfaches teurer).

⚠️ **Die Regel, die dieser Faden transportiert, muss in jeder Etappe gleich formuliert sein:** *Nicht „triff bessere Entscheidungen", sondern „jede Entscheidung wird einmal fällig, und der Preis wächst mit der Zahl der Stellen, an denen sie steht."* Ein Lernender, der glaubt, er hätte in Etappe 1 anders bauen sollen, hat den Faden falsch verstanden — er **konnte** es dort nicht wissen.

**Die Beutetabelle und der kontrollierte Zufall** ⭐ — der Faden, der eine Anfängerfrage sechzehn Etappen lang offen hält: **4 (Kür: `random.choice` über eine Beutetabelle — gleichverteilt, und der Lernende merkt, dass ein Datenkern nicht so oft fallen darf wie ein Chitinpanzer; die Frage wird ausdrücklich *nicht* beantwortet)** → 6 (Gegnertypen entstehen — dieselbe Struktur, dasselbe Problem) → **17a (Zahltag: gewichtete Auswahl, und die schwierigere Frage dahinter — wie erzeugt man kontrollierte Unvorhersehbarkeit? **Hier wird die Beute außerdem typgebunden** — der Speier hinterlässt die Säuredrüse, und Seltenheit wird überhaupt erst möglich)** → 25 (Gewichte werden Content).

⚠️ **Die Sperre dazu gilt in 4:** `random.choice` darf erklärt werden, Gewichte nicht. Wer sie dort vorwegnimmt, gibt dem Lernenden eine Zeile und nimmt ihm den Gedanken — 17a sagt selbst, der schwierige Teil sei nicht `random`, sondern das Wort davor. Ebenso bleibt `import` dort eine Gebrauchsanweisung; erklärt wird er in **24**.

**Geteilte Objekte** ⭐ — der Faden, der den häufigsten schwer findbaren Fehler in objektorientiertem Python trägt: **4 (Aliasing an einer Liste — `b = a`, beide ändern sich; damals eine Kuriosität)** → **10 (Zahltag: dasselbe an eigenen Objekten, benannt als Objektidentität; drei Gegenmittel — in `__init__` erzeugen, `None` als Standardwert, `.copy()`; dazu der Reflex *„sind das überhaupt zwei Dinge?"* und `is` als Nachweis)** → **14a (`[["."] * 5] * 5` — fünf Namen für dieselbe Zeile, die böseste Form)** → **16 (Hauptkandidat der Bug-Jagd II — der Reflex aus 10 ist das Werkzeug)** → 19 (was beim Laden ein neues Objekt wird und was dasselbe).

⚠️ **Diese Fehlerklasse stürzt nie ab.** Sie gehört durchgehend zu Typ 3 aus Etappe 8 und muss überall so benannt werden.

**Fortschritt der eigenen Figur** ⭐ — der Faden, der das Spiel zu einem Hero-Survival macht: **3c (`erfahrung` steigt beim Kill — eine Zahl, noch ohne Wirkung)** → **5 (die Stufentabelle als Dictionary: ab welcher Erfahrung welche Stufe?)** → **9a (`erfahrung` und `level` werden Attribute des Marine)** → **13 (Erfahrung bis zur nächsten Stufe ist derselbe Zähler wie eine Abklingzeit)** → **18 (jede Stufe zahlt einen Skillpunkt aus; Fähigkeiten haben Voraussetzungen und eigene Stufen)** → 19 (vergebene Punkte gehören in den Spielstand) → 21b (jetzt erst wird balanciert) → **22 (alle Zahlen wandern in Tabellen)** → 25 (und von dort nach `content/`).

**Wichtig für die Buchführung:** Zwischen 3c und 18 hat die Erfahrung fünfzehn Etappen lang **keine Wirkung** — sie ist eine Zahl auf dem Bildschirm. Das ist Absicht und dieselbe Bauweise wie bei `kern_integritaet` in Etappe 1: Der Lernende sieht früh, dass etwas mitgezählt wird, und erlebt später, wozu. Wer in 5 oder 9 schon Fähigkeiten freischaltet, nimmt Etappe 18 ihren Gegenstand.

**Zwei Verlustbedingungen** — **Etappe 1 (beide Werte werden angelegt: `kern_integritaet` und die eigene `trefferpunkte`)** → **3a (beide beenden den Lauf — zwei Prüfungen, nicht eine)** → **5 (der Kern wird zusätzlich ein Ort; ein dritter Wert mit 100 kommt dazu — die `integritaet` eines Sektors —, und der Sektor `"kern"` bekommt ausdrücklich keine eigene)** → 9a (die eine gehört dem Marine, die andere der Welt — und genau daran merkt man, wem ein Wert gehört) → **13 (der eigene Ausfall ist nicht endgültig: Respawn-Zähler)** → 16 (Kandidat für die Bug-Jagd: welcher der beiden Werte war es?) → 19 (beide im Spielstand). Der didaktische Zweck ist der Namensfaden aus Etappe 5: Zwei Gesundheitswerte, die nie verwechselt werden dürfen, sind die beste Übung dafür, dass Namen Bedeutung tragen.

**Warum der Trupp nicht schon in Etappe 2 entsteht:** Eine `if`/`elif`-Kette, die dort alle vier Wertesätze setzt, erzeugt Daten, die das Spiel monatelang nicht benutzt — und verdeckt den eigentlichen Lernstoff von Etappe 2: *eine* Kette wählt *einen* Zweig. Der Faden beginnt deshalb erst dort, wo er auch etwas tut.

**Beobachtbarkeit** — die Frage *woher weißt du, dass es das Richtige tut?* **Etappe 3c (der Balken macht 110 % und negative Werte sofort sichtbar — und soll sie ausdrücklich *nicht* begrenzen)** → 4 (Bahn zeigt übersprungene Einheiten) → 7b (`assert`) → 8 (Debugger) → 9b (`__repr__`) → 13 (Zähler sichtbar machen) → 16 (Tick-Tabelle) → **17b (der Seed, sichtbar in der Debug-Anzeige)** → 19 (Speicherstand als lesbarer Zustand) → 20 (Logging) → **26 (Tests: alle Annahmen auf einmal)**.

**Vorhersagen → Ausführen → Vergleichen → Erklären** — ab Etappe 1 bei jedem Kaputtmach-Experiment. Verdichtet in **16** (Tick-Tabelle gegen Programmlauf) und **27** (fünfhundert Zeilen fremder Code, Ausführen erst nach der Analyse).

**Daten statt Code** ⭐ — der Faden, der zur Prämisse führt: **5** (der Kauf schlägt Preise nach, statt sie abzufragen — eine neue Ware ist eine Zeile in den Daten) → **13** (Bauzeiten stehen bei den Objekten) → **17a** (Gegnertypen als Datensätze) → **22** (Fähigkeiten, Turmstufen und Söldner als Daten, und die Frage *was ist Inhalt, was Verhalten?*) → **23a** (die Befehlskette stirbt durch ein Dictionary) → **25** (alles wandert nach `content/`). Prüffrage, die in **5** zum ersten Mal gestellt wird: **Ändert sich diese Liste? Dann sind es Daten.**

**🚨 KI-Code-Warnsignale** — ab Etappe 8 verteilt: 12 (`update(self, welt)` — warum die ganze Welt?), 15 (die Zeile, die das halbe Spiel kennt), 20 (breites `except`), 22 (`elif`-Kette statt Daten), 23b (Funktion mit acht Parametern), 26 (kein einziger Test), durchgehend die Null-Falle → **27 (drei Risiken finden)**. Alle liegen auf Stufe 👀: bemerken und benennen, nicht beheben.

**Erweitern ohne zu zerstören** — **Etappe 4 (der Befehlsumbau darf die Befehle aus 3b nicht brechen)** → **5 (der `vorrat`-Umbau fasst Statusanzeige, Feuern und Aufsammeln an)** → **6 (die zweite Gegnerliste darf Bewegung, Feuern und Wellenende nicht brechen)** → **7a (der Sonderfall: es darf sich *überhaupt nichts* ändern — und `diff` beweist es)** → 15 (vierter Fund ohne Änderung der Depot-Logik) → 19 (Statuseffekte mitspeichern) → 22 (neuer Geschütztyp ohne Logikänderung) → 25 (Gegnertypen als JSON) → 26 (Tests machen daraus Gewissheit).

**Knobelstellen** ⭐ — Aufgaben, bei denen das Problem gestellt wird, aber nicht das Verfahren: **3a** (Abbruch von innen nach außen) → **4** (`.join()` selbst finden; „erst sammeln, dann entfernen" selbst bauen) → **8** (die Bug-Jagd ist eine einzige große Knobelstelle) → **14b** (Zielsuche und Zonengrenze) → **16** (Reihenfolgefehler finden) → **27** (fremdes Repo). Im Guide ausdrücklich als solche markiert, damit Hängenbleiben nicht als Verständnislücke missdeutet wird — der Mentor gibt dort **Hinweise, keine Lösungen**.

**Von Namen zu Daten** ⭐ — die Architekturlinie des gesamten Tutorials, und der Faden, den man am leichtesten übersieht:

| Etappe | Was ein Name bezeichnet |
|---|---|
| **1** | einen einzelnen Wert |
| **4** | eine Sammlung von Werten |
| **5** | Werte, die über Namen nachgeschlagen werden |
| **9 / 10** | ein Objekt aus Zustand und Verhalten, das aus anderen Objekten besteht |
| **25** | Daten, die nicht einmal im Python-Code stehen müssen |

Jede dieser Etappen soll den Schritt am Ende benennen, nicht nur vollziehen. **Und der wichtigste Satz dabei steht in Etappe 4:** *Objektorientierung ersetzt keine Datenstrukturen — sie gibt ihren Einträgen mehr Bedeutung.*

**Die Gegner** ⭐ — der längste Datenfaden des Plans, und der, an dem sich Modellierung erklärt:

**3** (`gegner_anzahl = 3` — eine Menge) → **4** (`gegner = [7, 4, 2]` — Positionen, alle sehen gleich aus) → **6** (`gegner_typen` als zweite Liste daneben; jeder hat einen Typ, die Bahn zeigt verschiedene Zeichen — **und das Entfernen wird unangenehm**) → **11** (beide Listen kollabieren zu einer Liste von Objekten; der Schmerz endet) → **12** (die Objekte ticken) → **14a** (die Position wird `(x, y)`) → **17a** (die Typen bekommen Kosten, der Generator wählt sie) → **19** (der Zustand wird gespeichert) → **25** (die Typen kommen aus einer Datei).

**Warum die parallelen Listen in 6 gewollt sind:** Vererbung und Objekte in 9–11 sind sonst Zeremonie. Wer erlebt hat, dass ein gefallener Gegner an zwei Stellen mit demselben Index verschwinden muss, versteht in der ersten Minute von Etappe 11, wozu ein Objekt gut ist. **Das ist absichtliches technisches Schuldenmachen mit festem Rückzahlungstermin.**

**Parallele Sammlungen als Muster** — zwei Strukturen, die über den Index oder denselben Schlüssel zusammenhängen: **5** (`WAREN` und `STAPELBAR` — zwei Tabellen, ein Schlüsselsatz) → **6** (`gegner` und `gegner_typen` — zwei Listen, ein Index) → **11 / 22** (beide Male werden sie zu **einer** Struktur zusammengezogen). Gemeinsame Erkenntnis: **Zwei Sammlungen, die immer gleich lang sein müssen, sind eine Sammlung, die noch nicht gebaut wurde.**

**Migrationen — was womit ersetzt wird** ⭐

Der Plan baut mehrfach etwas Funktionierendes um. **Diese Übergänge müssen festgelegt sein, sonst entstehen zwei Wahrheiten über dieselbe Sache:**

| Was | Bis | Ab | Regel |
|---|---|---|---|
| **Gegner** | 3: `gegner_anzahl = 5` | 4: `gegner = [7, 4, 2]` | Die Anzahl verschwindet, `len()` ersetzt sie. **Keine zweite Zählvariable.** |
| **Gegner** | 4: Positionszahlen | 6: `gegner` **plus** `gegner_typen`, über den Index verbunden | Zwei parallele Listen, bewusst unbequem. **`len()` beider muss immer gleich sein.** |
| **Gegner** | 6: zwei parallele Listen | 9/11: `Gegner`-Objekte | **Beide Listen kollabieren zu einer.** Position und Typ werden Attribute desselben Objekts. Das ist der Zahltag für den Schmerz aus 6. |
| **Munition** | 3: `munition = 40` | 5: `vorrat["munition"]` | Die lose Variable verschwindet. **Kein zweiter Speicher.** |
| **Munition** | 5: loses `vorrat` | 9: `marine.vorrat` | Der ganze Vorrat wandert in den Marine — **`marine.munition` wird nicht neu eingeführt.** |
| **Vaporium** | 4: Eintrag in `inventar` | 5: `vorrat["vaporium"]` | **Vaporium ist ab 5 Ressource, kein Gegenstand.** Nie beides gleichzeitig. |
| **Inventar** | 4: Liste von Strings | 11: Liste von `Item`-Objekten | Die Liste bleibt, der Eintrag wird reicher. |
| **Weltzustand** | 1–11: lose Variablen (`kern_integritaet`, `welle`, `gegner`, `trupp`, `sektoren`) | 12: `welt.*` | **Die losen Namen verschwinden.** Kein zweiter Speicher, keine Kopie bleibt zurück. Was pro Figur existiert, bleibt beim Marine. |
| **Gegner entfernen** | 11: sofort bei `remove()` | 12: `status = "tot"`, Entfernen in der Aufräumphase | Sterben und Entferntwerden sind zwei Vorgänge. Niemand verschwindet mitten im Tick. |
| **Die Karte** | 5–12: statische Daten, nur gelesen | 13: Zustand, der sich zur Laufzeit ändert | Ab dem Freiräumen gehört `sektoren` in den Spielstand (**19**) — die Beschreibungen nicht, die stehen im Code. |
| **Ausfall des Helden** | 3a–12: `trefferpunkte <= 0` beendet den Lauf | 13: Respawn-Zähler | **Nur noch `kern_integritaet` beendet das Spiel.** Die zweite Verlustbedingung bleibt, sie kostet ab jetzt Zeit statt allem. |
| **Gegnerposition** | 3c–13: `entfernung`, eine sinkende Zahl | 14a: `x` und `y` auf dem Raster | Das Wort `entfernung` verschwindet vollständig. „Wie weit" wird ab dort **gerechnet** (`welt.abstand`), nicht gespeichert. |
| **Darstellung des Vorfelds** | 3c–13: `zeichne_bahn()`, eine Zeile | 14a: `zeichne_vorfeld()`, ein Raster | Die alte Funktion wird **gelöscht**. Die Schicht aus 7b bleibt unangetastet — nur ihr Inhalt wird getauscht. |
| **Wellenzusammensetzung** | 3c–16: Anzahlformel, `if`/`elif`-Kette, feste Verteilung nach Stelle | 17a: `erzeuge_welle()` aus Budget und den Zahlen in `GEGNERTYPEN` | **Formel, Kette und Verteilung werden gelöscht.** `wellen_typen` bleibt für die Ankündigung und wird aus der Namensliste gebaut. |
| **Funkentscheidung und letzte Meldung** | 1–16: lose `letzte_meldung`, `meldung_abgesetzt` | 17c: `welt.letzte_meldung`, `welt.meldung_abgesetzt` | Was **vor** der Welt entsteht, wird direkt nach ihrem Anlegen übergeben; danach liest niemand mehr die lose Variable. Was **nach** der Welt entsteht, landet direkt im Attribut. |
| **Kern-Startwert** | 1–16: die nackte `100` | 17c: `KERN_START` | Ein Name für den Startwert, weil ab jetzt mit ihm verglichen wird. |
| **Flag-Speicher** | 2/6/15/17c: `meldung_abgesetzt`, `freigeschaltet`, `erkenntnisse` (und nach Wahl `funk_gehoert`) | 18b: `welt.flags` | **Drei Speicher werden einer.** Reiner Umbau, bewiesen mit `diff` bei festem Seed. Kein Wort darf in zwei Quellen stehen. |
| **`nachladen_noetig`** | 2–17 | 18a: gelöscht | Die Frage wird am Magazinstand gestellt. **Kein zweiter Wert für dieselbe Aussage.** |
| **Schaden, den eine Einheit austeilt** | 2–17: `schaden` wird direkt gelesen | 18a: `aktueller_schaden()` | Der Grundwert bleibt unverändert; wer austeilt, fragt die Methode. Effekte verändern nie ein Attribut „vorübergehend". |
| **Schaden anrichten** | 11b–17: `nimm_schaden()` plus Erfahrung und Abschuss an jeder Stelle einzeln | 18c: `treffe(ziel, menge, welt)` | Reiner Umbau vor dem Umbau, bewiesen mit `diff`. Was nur ein Marine bekommt, steht in seiner Fassung von `treffe()`. |
| **Abklingzeit** | 13: eine Zahl `abklingzeit` und die erfundene Übungsfähigkeit | 18c: `abklingzeiten`, Name → Rest | Das Attribut und die feste Zahl `ABKLINGZEIT` verschwinden; die Übungsfähigkeit aus 13 wird durch die echten ersetzt. |
| **Das Spielende** | 1–18: jedes Beenden verliert alles | 19c: `beenden` speichert, der Start fragt | Beim Laden gilt der Seed aus dem Spielstand, nicht `SEED`. Jede Befehlsdatei bekommt eine erste Zeile `n` oder `j`. |
| **Das Säen** | 17b: `random.seed()` genau einmal | 19c: am Anfang, beim Speichern, beim Laden | Nie auf einen alten Anfang zurück — jeder Seed steht im Spielstand oder kommt gleich hinein. |
| **Das Erzeugen von Items** | 11c–18: an jeder Stelle ausgeschrieben | 19b: eine Funktion *Kennung → Item* | Kauf, Einsammeln und Laden benutzen denselben Weg. |
| **Absagen eines Befehls** | 3b–19: `melde()` und `return` an jeder Stelle, oder ein `else`-Zweig | 20b: `raise SpielFehler(...)`, gefangen an **einer** Stelle | Die Meldung und das `return` fallen weg. Ein abgesagter Befehl kostet keine Runde. Kameraden und Tick werfen nie. |
| **Entwicklerausgaben** | 17b–19: `print()` und `###`-Zeilen, die Debug-Zeile über `melde()` | 20c: `welt.debug()` mit Schalter `DEBUG` | Was bleiben soll, geht über den Schalter; der Rest fliegt raus. |
| **Invarianten** | 5–18: aufgeschrieben, nicht geprüft | 20c: `assert` | Nur die prüfbaren; Merksätze bleiben Text. Ein `AssertionError` wird nie gefangen. |
| **Zustandsstrings** | 12: `"tot"` | 21b: `Enum` | Nur die Spielzustände, nicht jeder String im Programm. |

**Und das Ritual dazu, ab Etappe 4 in jedem Guide vor einem Umbau:** *Was bleibt gleich? Was ändert sich nur in der Darstellung? Was ändert sich wirklich am Datenmodell?* Zweck: **Umbauen heißt nicht „alles neu".**

**Invarianten** — Sätze, die immer wahr bleiben müssen: **4** (`len(gegner)` ist die Wahrheit; keine Position außerhalb der Bahn; Munition nie negativ) → **5** (jeder Nachbarname existiert; jeder Sektor hat eine Beschreibung; jeder Sektor **außer dem Kern** hat eine Integrität) → **6** (`len(gegner)` und `len(gegner_typen)` sind immer gleich; jeder gesehene Typ existiert in `GEGNERTYPEN`) → **5** (die Summe aus geladener und gelagerter Munition steigt beim Nachladen nie) → **10** (jeder Ausrüstungsplatz existiert immer; leer heißt `None`, nicht gelöscht) → **13** (Bauzeit kann nicht gleichzeitig laufen und fertig sein) → **17a** (`"kosten"` mindestens 1, `"gewicht"` mindestens 0) → **20** (aus Invarianten werden Prüfungen) → **26** (aus Prüfungen werden Tests). **Bis 20 werden sie nur aufgeschrieben, nicht geprüft** — das ist Absicht, weil `assert` erst in 7b als 👀 auftaucht.

**Refactoring als eigene Tätigkeit** ⭐ — umbauen, ohne das Verhalten zu ändern: **7a** (der erste bewusste Umbau, mit `diff` als Beweis und der Regel *nie Refactoring und neue Features im selben Schritt*) → **9** (Funktionen werden Methoden) → **11** (zwei Listen werden eine) → **22** (Code wird Daten) → **23a** (die `elif`-Kette stirbt) → **24** (eine Datei wird viele). **Der Charakterisierungstest aus 7a ist bei jedem dieser Umbauten das Werkzeug** — in 26 wird er automatisch.

**Die drei Debugging-Reflexe** — je einer pro Fundament-Etappe, alle nach demselben Grundsatz *Nachsehen schlägt Vermuten*: Etappe 1 *welchen Typ hat dieser Wert?* (`print(type(x))`) → Etappe 2 *welcher Zweig läuft?* (`### ZWEIG`) → **Etappe 3 *wie oft läuft das?* (`### RUNDE n`)** → **Etappe 4 *was steht da gerade wirklich drin?* (`### VOR`/`### NACH` mit Inhalt **und** `len()`)** → **Etappe 5 *unter welchem Namen?* (`.keys()`)** → **Etappe 6 *welche Struktur ist das eigentlich?* (`type()` und Inhalt)** → **Etappe 7 *was geht rein, was kommt raus?* (zwei `print` an den Funktionsgrenzen — trennt „rechnet falsch" von „wird falsch gefüttert")** → **8** *„halt an und sieh nach"* (**ein `breakpoint()` löst alle sieben `print`-Reflexe auf einmal ab; der Reflex selbst bleibt**). Gemeinsamer Grundsatz: **Nachsehen schlägt Vermuten.**

**Werkzeuge selbst befragen** 👀 — statt nachzuschlagen: **4** (`dir([])`, `help([].append)`, und `.join()` wird ausdrücklich selbst gesucht) → **5** (`dir({})`, `help({}.get)`; `.keys()` wird zum Debugwerkzeug) → **9b** (dieselbe Technik an eigenen Klassen) → **24** (eine fremde Bibliotheks-API lesen) → **27** (vor einem fremden Repo sind das die zwei Werkzeuge, die man immer hat). Zweck: Eine Erklärung *wiederzuerkennen* fühlt sich an wie sie zu *wissen* — der Unterschied fällt erst auf, wenn niemand da ist, den man fragen kann.

**Die Bug-Jagd** — Etappe 8 (erste Runde, Werkzeuge und Protokoll; **ohne Mentor die Zeitversatz-Variante — die Wartezeit ist der Mechanismus, nicht Zierde, denn wer die Sabotagen selbst geschrieben hat, weiß ohne Abstand, wo sie sitzen. Und in beiden Varianten gilt: kein `git diff` während der Jagd, es verrät alle eingebauten Fehler auf einen Schlag**) → 16 (subtilere Fehler; dort auch **Reihenfolgefehler im Tick** und ein **manipulierter Speicherstand**, sobald Etappe 19 ihn möglich macht) → 26 (umgekehrt: erst Test, dann Fix). Dazwischen unregelmäßig und unangekündigt.

**Das Formular dazu** — *Beobachtung → Hypothese → Experiment*, in 8 als Denkform angelegt, in **16** zum verbindlichen Dreizeiler gemacht, in **27** ohne Änderungserlaubnis angewandt. Es ist das Gegenstück zum Ritual *Vorhersagen → Ausführen → Vergleichen → Erklären*: Das eine gilt für Code, den du neu schreibst, das andere für Code, der sich falsch verhält.

**Die drei Fehlertypen** — eingeführt im Lehrplan, erlebt in Etappe 1 (fehlendes `f`, vergessenes `int()`), Etappe 2 (falsche Einrückung in der Klassenkette), Etappe 3 (Rundenzähler an der falschen Stelle), Etappe 4 (`liste = liste.append(...)`, Gegner beim Iterieren entfernen), Etappe 5 (`vaporium - preis` ohne Zuweisung), **Etappe 4 (eine Liste verändern, während man über sie läuft — der erste Typ-3-Fehler, den der Lernende *sehen* kann, weil die Anmarschbahn ihn zeigt)**, **Etappe 5 (`x - y` statt `x -= y` beim Abbuchen — unendlich Geld ohne jede Meldung; und der Tippfehler im Schlüssel, der still einen neuen Eintrag anlegt)**, Etappe 10 (zwei Marines, ein Inventar), Etappe 11 (eine **normale Methode** ohne Klammern ist immer truthy — bei `@property` ist es umgekehrt), Etappe 14a (`x = -1` greift von hinten), Etappe 14b (`<=` statt `<` bei der Reichweite) → **systematisch benannt und geübt in Etappe 8** → Etappe 12 (Tick zweimal pro Befehl), Etappe 16 (Reihenfolge im Tick), Etappe 20 (`except:` verwandelt Typ 1 in Typ 3), Etappe 21a (Panzerung größer als Schaden heilt den Gegner), Etappe 21b (`"weele"` gegen `Spielzustand.WEELE`), Etappe 25 (`"trefferpunkte": "sehr viel"` ist gültiges JSON).

**Zahlen als Lehrmittel** — dieses Setting rechnet überall, und deshalb ist Typ 3 hier der Normalfall statt der Ausnahme. Ab Etappe 3 zeigt die Balkendarstellung Rechenfehler an, die in einer Zahlenkolonne unsichtbar wären. Ab Etappe 4 zeigt die Anmarschbahn Listenfehler an. Das ist Absicht: Die Darstellung ist Teil des Debugging-Werkzeugkastens.

**Git** — Etappe 0 (Minimalset) → 8 (`git diff`, `git log --oneline` als Suchhilfe) → **16 (`git checkout <hash>` und zurück: alte Stände ansehen für die Bisektion, nichts darauf committen)** → **21b (erster Branch mit echtem Zweck: Balancing)** → 24 (Merges, Konflikte, Rückgängigmachen; der Balancing-Branch ist das Übungsobjekt). **Pull Requests, Rebase und Cherry-Pick stehen nicht im Plan** — sie sind kein offener Posten, sondern eine begründete Auslassung.

**Ein Commit pro Portion**, nicht pro Etappe: Die geteilten Etappen haben einen Zwischen-Commit (`Etappe 14a: …`). Nach sechs Monaten ist `git log --oneline` die ehrlichste Fortschrittsanzeige, die es gibt — und mit 51 statt 30 Einträgen eine dichtere.

**Schreiben → Lesen** — Etappe 7a (Struktur in fremdem Code erkennen) → 9 (erste Leseübung) → 15 (fremde Funktion mit stiller Annahme) → alle Etappen ab dort → 23b (Code aus echten Projekten) → **27 (ein ganzes fremdes Repo, ohne Hilfe)**. Das ist der eigentliche Zweck des Projekts, und Etappe 27 ist seine Einlösung.

**Die Prämisse** — Etappe 1 (vier Klassen, zwanzig Wellen, ein Kern) → 11 (die Klassen werden Code, **alle vier gleichzeitig**) → 13 (der Basisturm macht die Zeit spürbar — **genau einer, und jede Klasse kann ihn bauen**) → 17c (ein Sektor fällt endgültig — Kür) → 22 (die Klassenfrage kommt zurück) → 25 (Vielfalt ohne Code).

**Groß und klein geschriebene Namen** — Etappe 1 (die Regel, ohne eigenen Anwendungsfall) → **5 (die vier Depot-Tabellen sind die ersten festen Werte; `sektoren`, `inventar` und `vorrat` bleiben klein und sind die Gegenprobe)** → **6 (`KLASSEN`, `AUSBAUTEN`, `GEGNERTYPEN` — und `STAPELBAR` behält beim Umbau zum Set seinen Namen, weil sich die Struktur ändert und nicht die Rolle)** → 9 (dieselbe Frage für Klassen- und Objektnamen) → 25 (feste Werte wandern in Dateien und heißen dort anders). Zweck: Wer die Regel erst spät lernt, benennt rückwirkend um — deshalb steht sie in Etappe 1, obwohl sie dort noch nichts zu tun hat.

**Die Balancing-Falle** — benannt im Lehrplan, **im Guide zum ersten Mal akut in 3c (Schaden und Gegneranzahl), mit Fünfzehn-Minuten-Deckel und der Notizliste als Ventil**, Höhepunkt bei 17a (Wellenbudget) und 21b (Kampfformel). Gegenmittel: Zeitlimit, Branch ab 21b, und die Regel „eine langweilige Welle, die läuft, schlägt eine spannende, die abstürzt".

**Die drei Anspruchsstufen** 🔨🧠👀 — kein Verweisfaden, sondern die Regel, nach der alle anderen gelesen werden. Sie steht ab Etappe 3 in fast jedem Etappenkopf. **Für dieses Register heißt sie:** Wer eine 👀-Schuld einlöst, schuldet einen Satz, keine Implementierung. Wer sie zur Bauaufgabe macht, überlädt die Ziel-Etappe.

**🧠 Die Entwicklerfrage** — je eine ab Etappe 17: 17c (wie viel Zufall ist fair?) → 18 (wo gehört Zustand hin?) → 19 (was muss ein Spielstand garantieren?) → 20 (welcher Fehler gehört wem?) → 21b (welche Werte gehören zum Kampfsystem?) → 22 (was ist Inhalt, was Verhalten?) → 23b (wer muss wen kennen?) → 24 (wann hilft Aufteilung?) → 25 (wem vertraue ich?) → 26 (was beweist ein grüner Test?) → **27 (woran erkennst du, dass jemand nachgedacht hat?)**. Alle Antworten stehen in `GELERNT.md` und werden **nicht** korrigiert — sie werden später wiedergelesen. Der Wert liegt im Vergleich zwischen der Antwort von damals und der von heute.

---

## Teil D — Pflege

**Was der Status bedeutet.** Er beschreibt den Zustand des **Tutorials**, nicht deines Codes: `eingelöst` heißt, dass der Guide für die Ziel-Etappe geschrieben ist und diese Schuld dort tatsächlich einlöst. Solange eine Ziel-Etappe noch nicht ausgearbeitet ist, bleibt der Eintrag `offen` — auch wenn die Idee feststeht.

Damit beantwortet die Spalte genau die Frage, die beim Weiterschreiben zählt: *Was muss die nächste Etappe noch abarbeiten?*

**Wenn eine Etappe fertig geschrieben ist:** alle Schulden durchgehen, die auf sie zeigen, und prüfen, ob der Guide sie wirklich einlöst. Was er nicht einlöst, bleibt offen und wandert auf die nächste Ziel-Etappe.

**Wenn du von der Vorgabe abweichst:** Eintrag anpassen, nicht löschen. Wenn du in Etappe 6 doch keine Sets nimmst, müssen 14 und 18 das wissen. Eine Zeile hier erspart dir eine Stunde Verwirrung dort.

**Wenn ein Umweg entsteht:** Eintragen. Der Kopplungs-Umweg bei Etappe 13 steht bereits drin. Weitere kommen — ab Etappe 17 ist das der Normalfall und nicht die Ausnahme.

**Wenn eine Kür entfällt:** Zwei Einträge hängen an optionalen Teilen — die Sensorabdeckung (14b) und der endgültig verlorene Sektor (17c). Wird die Kür nicht gebaut, sind die abhängigen Zeilen in **19** und **20** keine offene Schuld, sondern **entfallen**. Streich sie nicht, sondern setz den Status auf `entfällt` und schreib dazu, warum. Sonst suchst du in vier Monaten nach einer Einlösung, die es nie geben sollte.

**Wenn du eine Etappe selbst teilst:** Das ist ausdrücklich erlaubt (Lehrplan, *Etappen dürfen halbiert werden*). Für den Bogen ändert sich dabei nichts — die Verweise zeigen auf Nummern, nicht auf Portionen. Ergänz höchstens den Buchstaben, wenn es die Buchführung klarer macht.

**Wenn du eine 👀-Schuld doch ausbaust:** Auch das ist erlaubt, aber trag es ein. Wer `__iter__` in Etappe 11 tatsächlich implementiert, hat danach eine Etappe 23a, die eine halbe Sitzung kürzer ist — und eine Etappe 11, die zwei Abende länger war. Beides ist vertretbar; unsichtbar sollte es nicht bleiben.

**Wenn dir eine Werkzeuglücke auffällt:** Ein Auftragsschritt verlangt etwas, das kein Guide erklärt hat — das gehört nicht hierher, sondern in `SYNTAX.md`, Abschnitt *Offene Lücken*. Der Bogen führt Versprechen, das Syntaxregister führt Werkzeuge.

**Wenn du mit mir arbeitest:** Verweis mich bei jeder Etappe ab 12 auf diese Datei. Nicht aus Misstrauen — ich habe über Monate kein verlässliches Gedächtnis, und eine plausible Rekonstruktion ist schlimmer als ein Nachschlagen.
