# Der Bogen — Register aller Vorausverweise

> Verbindlicher Anhang zum [Lehrplan](Vorposten_Lehrplan.md). Diese Datei ist die einzige Quelle der Wahrheit für alles, was eine frühe Etappe verspricht und eine späte einlösen muss.

---

## Wozu es diese Datei gibt

Der Lehrplan verspricht ständig etwas: *„Diese Variable brauchst du in Etappe 17."* — *„Das Raster wird in Etappe 29 zur Tilemap."* Diese Versprechen sind der Grund, warum sich das Projekt wie ein Bogen anfühlt und nicht wie 30 Übungsaufgaben.

Aber sie sind auch eine Schuld. Wenn Etappe 17 kommt und dort nichts eingelöst wird, war das Versprechen eine Behauptung.

Diese Datei ist die Buchführung darüber. Sie hat drei Adressaten:

**Dich.** Wenn du bei Etappe 12 sitzt und dich fragst, warum du in Etappe 6 ein Set statt einer Liste genommen hast, steht die Antwort hier.

**Mich.** Ich habe kein verlässliches Langzeitgedächtnis über Monate. Wenn du bei Etappe 17 ankommst, weiß ich nicht mehr zuverlässig, was ich in Etappe 2 versprochen habe — ich würde es rekonstruieren, und Rekonstruktion ist Raten mit gutem Ruf. Verweis mich bei jeder späten Etappe auf diese Datei, dann rate ich nicht.

**Jeden, der den Guide liest.** Das Register macht sichtbar, dass die Struktur Absicht ist.

**Regel:** Wer einen neuen Vorausverweis in eine Etappe schreibt, trägt ihn hier ein. Ohne Ausnahme. Ein Verweis, der nicht im Register steht, existiert nicht.

**Zum Stand dieser Fassung:** Sie entstand zusammen mit dem Lehrplan, bevor ein einziger Guide geschrieben war. Deshalb steht überall `offen`. Das ist kein Rückstand, sondern der Ausgangszustand — die Spalte füllt sich, während die Guides entstehen.

**Nachgezogen auf Lehrplan-Fassung 3.** Zwei Dinge haben sich geändert, und beide betreffen dieses Register:

**1. Sieben Etappen sind in Portionen geteilt** — 3, 7, 9, 14, 17, 21, 23. **Etappe 3 hat als einzige drei Portionen** (3a Schleife, 3b Befehle, 3c Kampf und Anzeige), die übrigen zwei. Die **Nummern sind unverändert**, deshalb bleibt jeder Verweis in diesem Register gültig. Wo es für die Buchführung einen Unterschied macht, steht die Portion dabei (`7b`, `14a`, `17b`). Ein Verweis auf **7** ohne Buchstaben meint die Etappe als Ganzes.

**2. Es gibt drei Anspruchsstufen** — 🔨 bauen, 🧠 verstehen, 👀 nur erkennen. Das ist für den Bogen keine Kosmetik, sondern ändert, *was eine Schuld überhaupt bedeutet*:

> Eine Schuld auf Stufe 👀 ist eingelöst, wenn der Lernende die Sache **wiedererkennt und in einem Satz erklärt**. Sie verlangt keinen Code. Wer sie behandelt, als müsste etwas gebaut werden, bläht die Ziel-Etappe auf — genau der Fehler, den Fassung 3 behoben hat.

Betroffene Einträge sind mit 👀 markiert.

---

## Teil A — Was gepflanzt wird

Chronologisch nach Etappe. Spalte „Status": `offen` = noch nicht eingelöst, `eingelöst` = der Guide der Ziel-Etappe ist geschrieben und löst die Schuld dort tatsächlich ein.

### Etappe 0 — Das Repo

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `pip`, venv, `requirements.txt` | **24** — `pyproject.toml` als Gegenstück; **28** — Pygame installieren | offen |
| Die Paketliste gehört zum Projekt | **24** — Abhängigkeiten deklarieren statt einfrieren | offen |
| `.gitignore` und was nicht ins Repo gehört | **19** — `saves/`; **24** — Build-Artefakte | offen |
| `GELERNT.md` als Ort für Entscheidungen | durchgehend — jede Design-Entscheidung landet dort | offen |

### Etappe 1 — Der Abwurf

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `letzte_meldung` als Variable statt als Satz | **17** — die Aufzeichnung ist achtzehn Tage alt | offen |
| `kern_integritaet` (angelegt, noch ohne Wirkung) | **3a** — Abbruchbedingung, inklusive Knobelstelle ✓; **17** — Vergleich mit dem Startwert | **teilweise eingelöst** ✓ (3a) |
| `wellen_bis_evakuierung` als feste Zahl | **3a** — `range(1, 21)` ✓; **17** — der Wellengenerator skaliert daran | **teilweise eingelöst** ✓ (3a) |
| Prinzip: Weltzustand speichern, nicht nur ausgeben | **12** — der gesamte Tick beruht darauf | offen |
| „Name zeigt auf Wert" statt „Behälter" | **4** — Aliasing: `b = a` und beide ändern sich ✓; **10** — dasselbe an eigenen Objekten | **teilweise eingelöst** ✓ (4) |
| `=` als „bekommt den Wert" lesen | **2** — Abgrenzung zu `==` | offen |
| Die Klassenwahl als Zahl aus `input()` | **2** — bestimmt die Startwerte **der gewählten Klasse**; **11** — wird zur Klassenhierarchie | offen |
| **Der Dreisatz: `input()` gibt Text → `int()` macht eine Zahl → erst damit wird gerechnet** | **5** — die Mengenabfrage beim Kaufen ✓; **20** — `ValueError` wird abgefangen | **teilweise eingelöst** ✓ (5) |
| Regel: *woher* ein Wert kommt, bestimmt, was vor der Benutzung passieren muss | **19** — geladene Daten sind nicht das, was gespeichert wurde; **25** — Content von außen ist nie vertrauenswürdig | offen |
| `int()` kann mit `ValueError` scheitern | **20** — echte Fehlerbehandlung | offen |
| Sprachentscheidung Variablennamen (de/en) | durchgehend — Konsistenz bis 30; **23** fremden Code lesen; **25** Namen werden JSON-Schlüssel | offen |
| **Darstellung: fester ASCII-Kopf, mehrzeiliger String** | **3c** — Balken kommen beim `status`-Befehl dazu, der Kopf bleibt unangetastet ✓; **7b** — wandert in eine Zeichenfunktion | **teilweise eingelöst** ✓ (3c) |
| Autorenregel: die Zahlen zeigen die Lage, nicht der Text | durchgehend — Grund, warum dieses Setting wenig Prosa braucht | offen |

### Etappe 2 — Der erste Kontakt

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `if`/`elif`-Kette für Klassenwerte (bewusst ertragen) | **11** — die Kette stirbt, Klassen übernehmen | offen |
| `meldung_abgesetzt = True/False` | **17** — wirkt mit, welcher Sektor fällt; **18** — geht im Flag-Set auf | offen |
| Verknüpfte Bedingungen (`and`/`or`/`not`) | **18** — Freischaltungen prüfen mehrere Voraussetzungen | offen |
| 👀 Grenze des Booleans: nur zwei Zustände (benannt, nicht ausgebaut) | **12** — Status als String; **21b** — `Enum` für benannte Zustände | offen |
| Truthy/Falsy — besonders `0` (**eine Regel, nicht die volle Liste**) | **4** — `if inventar:`, die leere Liste ist falsy ✓; **10** — `None` ≠ `0`; **18** — als Gefahr bei Munition und Zählern | **teilweise eingelöst** ✓ (4) |
| 👀 `and`/`or` geben mehr zurück als `True`/`False` (zwei Zeilen im Terminal, kein Bauauftrag) | **18** — dort als Lesestoff eingelöst; **23b** — in fremdem Code | offen |
| ⚠️ **`trefferpunkte` (Marine) und `kern_integritaet` (Anlage) sind zwei Werte** — beide 100, deshalb die häufigste Verwechslung des Fundaments | **3c** — die Gegner schlagen auf die Anlage, nicht auf den Marine; **11** — jeder der vier Marines bekommt eigene Trefferpunkte; **12** — beide ticken unabhängig | offen |
| **Die Klassentabelle mit markiertem Bezugsfall** (Soldat als Anker, drei Klassen relativ dazu) | **11** — wird zu vier Python-Klassen; **21a** — der Bezugsfall wird balanciert, die anderen relativ nachgezogen; **22** — sind das nicht eigentlich Daten? | offen |
| `nachladen_noetig` / `ziel_in_sicht` als echte Booleans, in **einer** `and`-Bedingung | **12** — Einheiten bekommen eigene Zustände; **18** — gehen in der Voraussetzungsprüfung auf | offen |
| **Erkenntnis: eine verknüpfte Bedingung sagt nicht, welcher Teil scheiterte** | **20** — die ganze Etappe über brauchbare Fehlermeldungen | offen |
| `elif` ≠ mehrere `if` | **17** — mehrere Ereignisse treffen gleichzeitig zu | offen |
| Der `else`-Zweig für Unerwartetes | **20** — `try`/`except` statt Auffangbecken | offen |
| `.strip()` auf Eingaben — **`.lower()` erst in 3a**, weil hier Zahlen eingegeben werden | **3a** — Befehlswörter brauchen `.lower()` ✓; **4** — dieselbe Kette, jetzt mit `.split()` ✓; **7a** — `verarbeite_befehl()` | **teilweise eingelöst** ✓ (3a, 4) |
| 👀 Punkt-Schreibweise (`wert.methode()`) — ein Satz: *gehört zu* | **9a** — `einheit.melde()` bei eigenen Objekten | offen |
| Die vier Klassen als festes Personal (erzählerisch, noch nicht im Code) | **11** — Klassenhierarchie; **22** — die Frage, ob sie Daten sein sollten | offen |
| **Nur die gewählte Klasse bekommt Werte** — die `if`/`elif`-Kette wählt genau einen Zweig | **11** — dort entstehen alle vier Objekte gleichzeitig | offen |
| `print()`-Debugging als Reflex | **8** — der Debugger als bessere Variante | offen |
| Design-Entscheidung: welche Klasse ist der Bezugsfall | **21** — gegen sie wird balanciert | offen |

### Etappe 3 — Die Wellenschleife ⭐  *(3a Schleife · 3b Befehle · 3c Kampf und Anzeige)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **3a:** `for` über die Wellen, `while` über die Runden | **12** — jeder Rundendurchlauf löst einen Tick aus | offen |
| **3a: Die Hauptschleife selbst** | **28** — wird zur Pygame-Loop mit 60 fps | offen |
| **3a:** Zwei Schleifenebenen, also zwei Einrückungstiefen | **14a** — die Doppelschleife über das Raster | offen |
| **3a:** `range()` | **14a** — Schleifen über das Vorfeldraster | offen |
| **3a:** `range()` zählt ab 0, die zweite Zahl ist ausgeschlossen | **4** — derselbe Grund, warum der erste Listenindex 0 ist ✓; **8** — Off-by-One als eigene Fehlerkategorie | **teilweise eingelöst** ✓ (4) |
| **3a:** `break` beim Wellenende | **20** — die Abbruchbedingungen werden validiert | offen |
| ⭐ **3a: Knobelstelle — Abbruch von innen nach außen** (erste Aufgabe ohne gezeigtes Verfahren) | **12** — dieselbe Frage beim Beenden des Ticks; **19** — dort wird vor dem Beenden gespeichert | offen |
| **3a:** `Strg + C` als Notausgang, einmal absichtlich benutzt | **8** — gehört zum Werkzeugkasten der Bug-Jagd | offen |
| 👀 **3a:** `continue` und `_` (im Wegwerf-Skript gesehen, nicht im Spiel gebaut) | **23a** — dieselben Denkfiguren in Comprehensions | offen |
| **3b:** `.lower()` auf der Eingabe — Einlösung aus **2** | **4** — dieselbe Kette, jetzt mit `.split()` ✓; **7a** — `verarbeite_befehl()` | **teilweise eingelöst** ✓ (4) |
| **3b:** Lange `elif`-Kette der Befehle (bewusst ertragen) | **7a** — wandert in `verarbeite_befehl()`; **23a** — stirbt durch das Befehls-Dictionary | offen |
| **3b:** `else`-Zweig für unbekannte Befehle | **5** — wächst um `umsehen`, `gehe`, `depot`, `kaufe` ✓; **20** — wird echte Fehlerbehandlung | **teilweise eingelöst** ✓ (5) |
| **3b: Design-Entscheidung Befehlssprache** (heute einwortig, bewusst) | **4** — der Umbau auf Verb + Ziel findet statt, und er wird als Erfahrung ausgewertet ✓; **5** — `kaufe medkit` und `gehe norden` ✓; **25** — Befehle als Content | **teilweise eingelöst** ✓ (4, 5) |
| **3b:** Befehl `beenden` (Schreibweise als Entscheidung festgelegt) | **19** — dort wird vor dem Beenden gespeichert | offen |
| **3b: Design-Entscheidung — welche Befehle kosten eine Runde?** (Auskunft kostet nichts, Handlung schon) | **12** — dieselbe Frage als „welche Spieleraktion löst einen Tick aus?"; **13** — Bauzeit läuft nur bei vergehender Zeit; **21a** — erst dadurch wird Nachladen eine echte Wahl | offen |
| **3a: Drei Ebenen für Variablen** (vor den Schleifen · pro Welle · pro Runde) ⭐ | **7a** — dort heißt das Verhalten *Scope*; **12** — Weltzustand gehört der Welt; **3c** — die Balkenrechnung gehört ans Anzeigen, nicht an den Start | offen |
| **3a: Die Abbruchbedingung ist `kern_integritaet`, nicht `trefferpunkte`** — Einlösung aus **2** | **13** — dort wird der Ausfall des Marine ein eigenes Thema | offen |
| **3a: Entwicklerbefehle sind erlaubt und werden am Ende entfernt** | **3c** — eigener Aufräumschritt; **8** — sie wären sonst Verdächtige bei der Fehlersuche | offen |
| **3c: `nachladen_noetig` bekommt endlich einen Wert** — Einlösung aus **2** | **18** — zwei Werte, die dasselbe sagen, sind eine Fehlerquelle | offen |
| **3c: Zwei Werte für dieselbe Aussage** (`munition > 0` und `nachladen_noetig`) | **18** — Zustandsverwaltung; **16** — Kandidat für die Bug-Jagd | offen |
| **3c: Was aus Zustand entsteht, wird beim Anzeigen erzeugt, nicht aufbewahrt** (Balkenlänge) | **4** — dasselbe für die Anmarschbahn; **7b** — die Zeichenschicht; **28** — 60-mal pro Sekunde | offen |
| **3b: Wo eine Variable angelegt wird, entscheidet, wann sie neu gesetzt wird** ⭐ | **7a** — dort bekommt das Verhalten den Namen *Scope*; **12** — Weltzustand gehört der Welt | offen |
| **3b:** Rundenzähler mit `+=` | **12** — wird zu `self.zeit`, der Weltzeit | offen |
| **3c:** Anzahl Gegner hängt an der Wellennummer (**Formel vom Lernenden selbst gewählt**) | **17a** — wird zum Budget-System | offen |
| **3c:** Platzhalter-Kampfformel (fester Schaden) | **7a** — wird zu `berechne_schaden()`; **21a** — wird zum System | offen |
| **3c:** Nachladen kostet eine Runde, Nachschauen nicht (erste echte Spielentscheidung) | **13** — dasselbe Muster als Bauzeit; **21a** — Teil des Balancings | offen |
| **3c:** Notizliste „was fühlt sich falsch an" | **21a** — Grundlage des Balancings | offen |
| **3c: Darstellung: Balken statt Zahlen** | **4** — die Anmarschbahn kommt daneben ✓; **7b** — wandert in `zeichne_balken()` | **teilweise eingelöst** ✓ (4) |
| **3c:** Balken zeigt ungültige Werte sichtbar an — **und soll sie nicht begrenzen** | **8** — Typ-3-Fehler an der Darstellung erkennen | offen |
| 👀 **3c:** Formatangabe im f-String (`:.0%`) | **9b** — `__repr__` formatiert Objekte; durchgehend beim Lesen | offen |

### Etappe 4 — Ausrüstung und Beute

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| Mutable vs. immutable | **10** — geteiltes `Inventar()`-Objekt; **14a** — `[["."] * 5] * 5` | offen |
| **Zwei Namen können auf dasselbe Objekt zeigen** (`b = a`) | **10** — dort ausdrücklich als Objektidentität benannt; **16** — Bug-Kandidat | offen |
| `.copy()` als bewusste Kopie | **10** — die Alternative zum geteilten Objekt | offen |
| `inventar` als Liste von Strings | **11** — wird zur Liste von `Item`-Objekten | offen |
| **Zwei identische Gegenstände sind nicht unterscheidbar** („welches Medkit?") | **11** — genau deshalb werden aus Strings Objekte | offen |
| Obergrenze 10 Gegenstände | **20** — „Inventar voll" als abgefangener Fall | offen |
| Index ab 0 — Einlösung aus **3a** | **14a** — `vorfeld[y][x]` im Raster | offen |
| `len()` | **14a** — `range(len(vorfeld))` | offen |
| `for` über eine Sammlung statt über `range()` | **12** — der Tick läuft über die Einheitenliste; **14a** — dieselbe Schleife über ein Raster | offen |
| ⭐ **Gegner = Positionszahl** — die Liste ist der Zustand, das `"K"` gehört nur in die Darstellung | **11** — aus der Zahl wird ein Objekt mit HP und Typ; **12** — das Objekt tickt; **14a** — aus der Zahl wird `(x, y)`; **19** — dieser Zustand wird gespeichert | offen |
| Gegnerliste der laufenden Welle — **keine Zählvariable mehr, `len()` ist die Anzahl** | **12** — wird zur `self.einheiten`-Liste im Tick | offen |
| **Die Bahn wird jede Runde neu erzeugt, nicht verändert** | **7b** — die Zeichenfunktion liefert Zeilen; **14a** — dasselbe für das Raster; **28** — dasselbe 60-mal pro Sekunde | offen |
| 👀 **Zuweisen an die Schleifenvariable ändert die Liste nicht** (`for pos in gegner: pos += 1` bewegt nichts) | **11** — ab dort *kann* man den Eintrag über die Schleifenvariable ändern, weil er ein Objekt ist | offen |
| ⚠️ **`range(len(...))` nur bei echtem Indexbedarf** — sonst `for ding in liste` | **14a** — dort ist der Indexbedarf echt | offen |
| **Liste nie verändern, während man darüber läuft** (Typ-3-Fehler) | **12** — als echtes Problem beim Tick; **16** — Kandidat für die Bug-Jagd | offen |
| `in` bei einer Liste | **6** — Gegenüberstellung Liste / Set / Dictionary | offen |
| `remove()` scheitert an fehlendem Element | **20** — wird zu `try` / `except` | offen |
| **Umzug zwischen zwei Listen: erst prüfen, dann anfassen** | **20** — der Kerngedanke der Fehlerbehandlung | offen |
| `.split()` für Zwei-Wort-Befehle | **5** — `kaufe medkit` und `gehe norden` ✓; **7a** — `verarbeite_befehl()` | **teilweise eingelöst** ✓ (5) |
| Befehl ohne zweites Wort (`nimm` allein) | **20** — wird sauber abgefangen | offen |
| **Design-Entscheidung 1: Kennung oder Anzeigename?** | **5** — das Depot ist die zweite Stelle, und die Entscheidung wird dort ausdrücklich nachgeprüft ✓; **11** — `item.id` / `item.name`; **25** — die Kennung wird JSON-Schlüssel | **teilweise eingelöst** ✓ (5) |
| **Design-Entscheidung 2: Ist die Bahn der Zustand oder nur sein Bild?** ⭐ — **der Plan legt sich hier fest: Positionen sind der Zustand** | **12** — nur ein eigenständiger Zustand lässt sich ticken; **14a** — beim Raster wird die Entscheidung fällig; **19** — nur Zustand wird gespeichert; **28** — nur so bleibt die Logik grafikfähig | offen |
| **Die Frage „Menge oder mehrere unterscheidbare Dinge?"** (Munition bleibt eine Zahl) | **6** — dieselbe Frage für vier Strukturen; **25** — welche Inhalte werden JSON | offen |
| Schrott als Währung | **5** — der Kaufvorgang, und Schrott wandert in den `vorrat` ✓; **22** — Kosten in Bauplänen | **teilweise eingelöst** ✓ (5) |
| Mengen lassen sich mit Listen schlecht führen (mehrmals `"schrott"`) | **5** — das `vorrat`-Dictionary löst das ✓ | **eingelöst** ✓ |
| Der Datenkern der Brut (heute nutzlos) | **15** — wird zur ersten Erkenntnis | offen |
| ⭐ *(Kür)* Der untersuchbare Datenkern — eine Zeile, die nichts auflöst | **15** — dort wird sie aufgelöst. *Entfällt, wenn die Kür entfällt.* | offen |
| **Darstellung: die Anmarschbahn als eine Zeile** ⭐ | **14a** — wird zum Raster aus vielen Zeilen; **7b** — wandert in `zeichne_bahn()` | offen |
| Gegnerposition ↔ Zeichen an dieser Stelle (zwei Dinge) | **14a** — Position als Tuple, Zeichen aus dem Raster | offen |
| Darstellung als Debugging-Werkzeug | **8** — sichtbare Fehler statt gelesener; **16** — Reihenfolgefehler im Tick | offen |
| **Reihenfolge: zeichnen vor oder nach dem Bewegen?** (Kaputtmach-Experiment 6) | **16** — daraus wird eine eigene Bug-Jagd; **12** — die Tick-Phasen | offen |
| **Baureihenfolge: ein Gegner → mehrere → entfernen** (drei Schritte, nicht einer) | **8** — genau dieses Halbieren ist das Suchverfahren; **14a** — dieselbe Staffelung beim Raster | offen |
| 👀 **`dir()` und `help()` — ein Objekt selbst befragen** | **9b** — dieselbe Technik an eigenen Klassen; **24** — eine fremde Bibliotheks-API lesen; **27** — die zwei Werkzeuge vor einem fremden Repo | offen |
| `.join()` selbst gefunden statt vorgesagt | **7b** — die Zeichenfunktion liefert Zeilen; **14a** — jede Rasterzeile entsteht so | offen |
| ⭐ *(Kür)* Beute per Nummer nehmen — der Spieler zählt ab 1, Python ab 0 | **8** — Off-by-One als eigene Fehlerkategorie | offen |

### Etappe 5 — Der Vorposten und das Depot

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **Dictionary = Zuordnung Schlüssel → Wert** (zuerst an einem Nicht-Spiel-Beispiel) | **19** — genau diese Form ist JSON; **25** — Content-Format | offen |
| `sektoren` als verschachteltes Dictionary | **13** — wird zur Laufzeit verändert | offen |
| `waren` als flaches Dictionary | **22** — bekommt Kosten, Voraussetzungen, Ausbaustufen | offen |
| Die Wahl flach ↔ verschachtelt als bewusste Entscheidung | **14a** — Dict oder Raster; **19** — Struktur ↔ Dateiformat | offen |
| Trennung Daten ↔ Code | **25** — Inhalt wandert komplett nach `content/` | offen |
| **Entscheidung: versiegelter Sektor fehlt oder ist markiert** — **empfohlen ist „fehlt"**; bei „markiert" bekommt der Sektor ein zweites flaches Dictionary (Richtung → Grund) und `gehe` drei Fälle statt zwei | **13** — bestimmt, wie `raeume_frei()` gebaut wird; **18** — Zustand mit Bedingung ist dasselbe Muster | offen |
| **Entscheidung: ausverkaufte Ware fliegt raus oder bleibt mit Bestand 0** | **22** — bestimmt, wie leicht Ausbaustufen einzubauen sind | offen |
| Die Landeplattform als unerreichbarer Ort | **13** — wird freigeräumt; **17** — dort landet das Evakuierungsschiff | offen |
| `aktueller_sektor` als Zustandsvariable | **9** — wird zu `marine.sektor`; **19** — Teil des Speicherstands | offen |
| `in` prüft beim Dict den **Schlüssel** | **6** — Gegenüberstellung Liste/Set/Dict | offen |
| Verschachtelte Struktur (Dict im Dict) | **19** — genau diese Form ist JSON; **25** — Content-Format | offen |
| Schlüssel müssen immutable sein | **6** — warum ein Set keine Listen aufnimmt | offen |
| `.get()` für sicheren Zugriff — **eckige Klammern, wenn Fehlen ein Bug wäre; `.get()`, wenn es der Normalfall ist** | **20** — die leichtere Alternative zu `try` / `except` | offen |
| Tippfehler **links vom `=`** legt still einen Eintrag an; Tippfehler beim **Lesen** stürzt ab | **8** — Typ-3-Fehler erkennen; **25** — Schlüssel aus fremden Dateien | offen |
| `.items()` zum Iterieren | **12** — über alle Einheiten laufen | offen |
| Zuweisung ändert die Karte zur Laufzeit | **13** — `welt.raeume_frei()` ist genau diese Zeile | offen |
| Der Kaufvorgang prüft drei Bedingungen | **20** — drei Bedingungen werden drei Exceptions | offen |
| **Größe** eines Dictionaries nicht ändern, während man iteriert (Werte ändern ist erlaubt) — Python knallt hier, wo eine Liste still das Falsche tut | **12** — dasselbe bei Einheiten | offen |
| Fehlerklasse „inkonsistente Daten" — **zwei Stufen: Richtung fehlt (wird abgefangen) gegen Zielname fehlt (stürzt trotz Prüfung ab)** | **25** — bei externem Content die häufigste Fehlerart | offen |
| **Invarianten: Welche Bedingungen müssen bei meinen Daten immer stimmen?** (aufgeschrieben, **nicht** geprüft) | **25** — dieselben Sätze gegen fremden Content; **26** — sie werden zu Tests | offen |
| **Richtung ≠ Ziel ≠ Standort** — drei Werte, die man leicht verwechselt | **9** — das Objekt kennt seinen eigenen Standort; **14a** — Koordinate gegen Feldinhalt | offen |
| **Der Kauf als Transaktion: erst alle Prüfungen, dann verändern** — Einlösung aus **4** | **20** — der Kerngedanke der Fehlerbehandlung; **19** — halb geschriebener Spielstand | offen |
| **Der Architekturtest: Daten ändern, Logik nicht anfassen** ⭐ (hinzufügen **und löschen**) | **22** — derselbe Test mit Bauplänen; **25** — derselbe Test mit JSON-Content | offen |
| **Umbenennen bricht Verweise, ohne dass Python warnt** | **24** — dasselbe bei Modulnamen; **25** — bei Content-Schlüsseln; **26** — ein Test würde es finden | offen |
| **Darstellung: statischer Grundriss mit Markierung** (handgezeichnet, **nicht** aus den Daten erzeugt) | **7b** — wandert in eine Zeichenfunktion; **29** — wird zur Kulisse | offen |
| **`vorrat` als Dictionary Name → Anzahl** (Schrott und Munition verlassen die losen Variablen) | **22** — Kosten werden gegen denselben Vorrat geprüft; **19** — Teil des Speicherstands | offen |
| **Trennung Menge ↔ Einzelstück** (`vorrat` gegen `inventar`) — Einlösung aus **4** | **6** — dieselbe Frage für vier Strukturen; **11** — Einzelstücke werden Objekte | offen |
| **Begriffstrennung Depot / Vorrat / Inventar** (Katalog · Ressourcen · Einzelstücke) | durchgehend — ab hier benutzt der Plan die drei Wörter konsequent; **22** — Baupläne sind ein zweiter Katalog | offen |
| **`stapelbar` als zweite flache Tabelle neben `waren`** — zwei parallele Dictionaries mit denselben Schlüsseln | **22** — dort werden sie zu **einer** verschachtelten Tabelle zusammengezogen; **25** — als JSON-Objekt pro Ware | offen |
| **Der Kauf kennt keine Warennamen** ⭐ (Preis wird nachgeschlagen statt abgefragt) | **22** — Baupläne funktionieren nach demselben Prinzip; **23a** — dieselbe Ablösung für die Befehlskette; **25** — Content aus JSON | offen |
| ⭐ **Die Bedingung dafür: Es geht nur ohne Logikänderung, wenn *alles* in den Daten steht, was die Logik fragt** | **22** — dort scheitert es, wenn eine Eigenschaft fehlt; **25** — die Frage an jedes JSON-Feld; **26** — Tests prüfen die Vollständigkeit | offen |
| **Ein Befehl hängt zum ersten Mal vom Ort ab** (`kaufe` nur im Depot) | **13** — Bauen nur in der Werkstatt; **14b** — Reichweite als Ortsbedingung | offen |
| `int()` beim Kauf einer Menge — Einlösung aus **1** | **20** — `ValueError` bei `drei` statt `3` wird abgefangen | offen |
| Der Wirtschaftskreislauf schließt sich (Gegner → Schrott → Munition → Gegner) | **21a** — Balancing hat ab hier einen Kreislauf zu balancieren | offen |
| ⭐ *(Kür)* Die Werkbank, an der nichts geht | **13** — dort wird an ihr gebaut. *Entfällt, wenn die Kür entfällt.* | offen |
| ⭐ *(Kür)* Sektoren nehmen einzeln Schaden | **17b** — ein Sektor kann endgültig fallen. *Entfällt, wenn die Kür entfällt.* | offen |

### Etappe 6 — Liste, Dictionary, Set, Tuple

**⭐ Hier werden Gegnertypen eingeführt.** Bis Etappe 5 ist ein Gegner eine Positionszahl und alle sehen gleich aus. Ab hier hat jeder einen Typ — als **zweite, parallele Liste** neben den Positionen, über den Index verbunden. Das ist bewusst unbequem und die tragende Begründung für Etappe 11.

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `freigeschaltet` als Set | **18** — wird zum zentralen Flag-Speicher | offen |
| **Das Set ist die Spielregel, nicht die Prüfung** | **18** — Freischaltungen; **22** — Voraussetzungen | offen |
| ⭐ **Ein Set garantiert den Zustand, nicht den Vorgang** — die Prüfung vor dem Abbuchen bleibt nötig | **18** — dieselbe Prüfung mit Voraussetzungen; **20** — aus der Prüfreihenfolge wird Fehlerbehandlung | offen |
| `AUSBAUTEN` als Katalog (Kennung → Preis) — zweiter Katalog nach `waren` aus **5** | **18** — Voraussetzungen kommen als Dateneintrag dazu; **22** — Kosten, Bauzeit, Ausbaustufen | offen |
| `"zielhilfe"` — eine Freischaltung ohne Wirkung | **18** — sie bekommt dort eine Fähigkeit | offen |
| `KLASSEN` als Tuple | **11** — die Klassenhierarchie; **20** — Eingabe validieren | offen |
| Tuple als unveränderliche Liste (`KLASSEN`) — **ohne Koordinaten-Vorgriff** | **10** — `self.position`; **14a** — dort wird `(x, y)` das eigentliche Beispiel | offen |
| Tuple als Dictionary- und Set-Element | **14b** — Koordinaten in einer Menge | offen |
| Die Komma-Falle: `(5)` ist kein Tuple, `(5,)` schon | **21a** — Rückgabe zweier Werte; **16** — Kandidat für die Bug-Jagd | offen |
| Tuple-Unpacking (`for a, b in ...`) | **12** — über Einheiten und ihre Zustände laufen | offen |
| 👀 Mengenoperationen (`&`, `\|`, `-`) | **18** — „welche Voraussetzungen fehlen noch?" | offen |
| Set für abgedeckte Felder | **14b** — Reichweite eines Geschützes | offen |
| Sets und Tuples lassen sich nicht als JSON speichern | **19** — Design-Entscheidung beim Speichern | offen |
| Unterscheidung „kein gültiges Wort" ↔ „hier nicht möglich" | **20** — dieselbe Trennung bei allen Befehlen | offen |
| „Modellierungsentscheidung" als Begriff | **14a** — Dict oder Raster; **19** — Struktur ↔ Dateiformat | offen |
| **Die Entscheidungshilfe: vier Fragen, feste Reihenfolge** | durchgehend ab hier — jede Strukturwahl bis **25** | offen |

**Gegnertypen — die Einträge dazu:**

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| ⭐ **`GEGNERTYPEN` als verschachteltes Dictionary** (Kennung → langer und kurzer Text) | **15** — Erkenntnisse hängen sich an denselben Eintrag; **17a** — dieselben Einträge bekommen Kosten; **25** — wandert nach `content/` | offen |
| ⭐ **`gegner_typen` als zweite Liste parallel zu `gegner`**, über den Index verbunden | **11** — beide Listen kollabieren zu **einer** Liste von Objekten | offen |
| ⭐ **Der Schmerz paralleler Listen** — beim Entfernen muss an **zwei** Stellen derselbe Index getroffen werden; `remove()` nach Wert trägt nicht mehr | **11** — genau dieser Schmerz ist die Begründung für Objekte; **16** — Kandidat für die Bug-Jagd | offen |
| Entfernen über den **Index** statt über den Wert (`pop`), rückwärts oder mit gesammelten Indizes | **11** — entfällt, weil ein Objekt eine Sache ist; **12** — dasselbe Problem im Tick | offen |
| `gesehene_gegnertypen` als Set | **15** — Erkenntnisse bauen darauf auf; **25** — Gegnertypen kommen aus JSON | offen |
| Erstbegegnung ausführlicher als jede spätere | **15** — Erkenntnisse verändern die Anzeige | offen |
| Wellenzusammenstellung als `if`/`elif` über die Wellennummer | **17a** — der Budget-Generator ersetzt die Kette | offen |
| Die Anmarschbahn zeigt **verschiedene Zeichen je Typ** | **14a** — dieselbe Zuordnung Typ → Zeichen im Raster; **29** — Typ → Kachel | offen |
| `bestiarium` als Auskunftsbefehl, kostet keine Runde — Anwendung aus **3b** | **12** — welche Spieleraktion löst einen Tick aus | offen |
| Unterscheidung „Typ existiert nicht" ↔ „Typ noch nie gesehen" | **20** — dieselbe Trennung als Fehlerbehandlung | offen |
| **Invariante zwischen zwei Sammlungen** — jeder Eintrag in `gesehene_gegnertypen` ist Schlüssel in `GEGNERTYPEN`; `len(gegner)` und `len(gegner_typen)` sind immer gleich | **20** — daraus wird eine Prüfung; **26** — daraus wird ein Test | offen |

### Etappe 7 — Aufräumen  *(7a Funktionen · 7b Trennung)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **7a:** Funktionen als Bausteine | **9a** — werden zu Methoden | offen |
| **7a: Zustand als lange Parameterliste (der Schmerz)** | **9a** — genau das begründet `self` | offen |
| 👀 **7a: `global` als verlockende Abkürzung, bewusst abgelehnt** | **9a** — Klassen lösen das Problem, das `global` nur zudeckt | offen |
| **7a:** `berechne_schaden()` | **21a** — wird zur echten Kampfformel; **26** — erster `parametrize`-Test | offen |
| 👀 **7b:** „Was muss immer gelten?" (Testdenken, **kein** Testeinstieg) | **21a** — drei `assert`-Zeilen zur Schadensformel; **26** — dieselben Fragen als `pytest` | offen |
| 👀 **7b: `assert` als geprüfte Behauptung** — drei Zeilen, dann ist das Thema erledigt | **13** — Zähler-Invarianten; **20** — prüfen ↔ fangen; **26** — `pytest` ist derselbe `assert` im Rahmen | offen |
| Lesefrage: „welche Annahmen macht diese Funktion?" | **23** — Lesekriterium bei fremdem Code; **27** — bei einem ganzen Repo | offen |
| Der Verhaltens-Beweis (Charakterisierungstest) | **26** — wird zum automatischen Testlauf | offen |
| **7b: Entscheidung `return` statt `print` in der Logik** | **21a** — zwei Rückgabewerte statt einer Meldung; **26** — nur so ist die Kampffunktion testbar; **28** — nur so bleibt die Logik grafikfähig | offen |
| **7b: Darstellung wird eigene Schicht (`zeichne_*`)** | **14a** — `zeichne_vorfeld()`; **28** — die Schicht wird ausgetauscht, nicht ersetzt | offen |
| Zeichenfunktionen entscheiden nichts | **29** — deshalb genügt hier ein Austausch | offen |
| Zwei Rückgabewerte als Tuple | **21a** — Schaden und Trefferart zusammen | offen |
| Standardwerte für Parameter | **10** — die Falle mit veränderbaren Standardwerten | offen |
| Docstrings | **23** — bekommen Typannotationen dazu | offen |
| „Eine Funktion, ein Zweck" | **24** — dasselbe Prinzip bei Modulen | offen |
| Klare Funktionsgrenzen zum Prüfen von Eingaben | **20** — an genau diesen Grenzen wird validiert | offen |
| `verarbeite_befehl()` wird selbst zur `elif`-Kette | **23a** — Befehle als Dictionary; **25** — Befehle als Content | offen |
| Refactoring und neue Funktionen nicht mischen | durchgehend — Arbeitsregel ab hier | offen |
| Warnung vor Überabstraktion | **24** — dieselbe Frage bei der Dateiaufteilung | offen |
| Einzelne Funktionen statt ganzer Datei zeigen können | durchgehend — hält den Mentor bei langem Code arbeitsfähig | offen |

### Etappe 8 — Bug-Jagd I ⭐

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| Die drei Fehlertypen als Denkraster | **20** — `except:` macht aus Typ 1 einen Typ 3; **21** — `"weele"` gegen `Spielzustand.WEELE` | offen |
| Tracebacks von unten nach oben lesen | durchgehend — bis **30** das häufigste Werkzeug | offen |
| Der Debugger (Breakpoints, Step, Variablen) | **9b** — Objektzustand aufklappen; **12** — den Tick beobachten; **14a** — Bewegung im Raster | offen |
| **Bedingte Breakpoints** | **12** — „halt an, wenn `welle == 7`"; **17b** — zusammen mit dem Seed die schärfste Kombination des Plans | offen |
| Ursache und Symptom trennen | **16** — dort liegen sie weiter auseinander, und dort wird das Formular daraus | offen |
| **Beobachtung → Hypothese → Experiment** (als Denkform angelegt) | **16** — wird zum verbindlichen Dreizeiler; **27** — dieselbe Form ohne Änderungserlaubnis | offen |
| Halbieren als Suchverfahren | **24** — welches Modul ist schuld | offen |
| Das schriftliche Debugging-Protokoll | **16** — wird nachgelesen und geschärft | offen |
| Das Fehlertagebuch | **26** — jeder Eintrag ist ein Testkandidat | offen |
| Einen Fehler präzise beschreiben (vier Punkte) | **23** — dieselbe Fähigkeit bei fremdem Code | offen |
| `git diff` / `git log` als Debugging-Werkzeug | **24** — dort zusammen mit Branches | offen |
| Abgrenzung Debugging ↔ Fehlerbehandlung | **20** — warum nacktes `except:` gefährlich ist | offen |
| Fehler in den **Daten** statt im Code | **16** — manipulierter Speicherstand; **25** — bei externem Content die häufigste Sorte | offen |
| Die Darstellung als Fehleranzeiger benutzen | **16** — Reihenfolgefehler im Tick werden sichtbar | offen |

### Etappe 9 — Alles wird zum Objekt  *(9a Klassen · 9b `__repr__`)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **9a:** Klasse `Marine` | **10** — bekommt Inventar und Ausrüstung; **11** — bekommt vier Unterklassen | offen |
| **9a:** Klasse `Gegner` | **11** — gemeinsame Basis mit `Marine`; **17a** — wird aus Typen erzeugt | offen |
| **9a:** `self` bündelt den Zustand | **12** — `self.zeit`; durchgehend | offen |
| **9b:** `__repr__` | **12** — zwanzig Einheiten lesbar im Debugger; **8**-Rückgriff | offen |
| **9b:** Doppelte Unterstriche sind Haken für Python | **11** — `__len__`, `__contains__`, `__iter__` (dort 👀) | offen |
| Erste Leseübung — **Stufe 1 der Leseleiter** | **12** — Stufe 2; **17** — Stufe 3; **23b** — Stufe 4; **27** — die Prüfung | offen |
| 👀 **9b:** `__str__` ↔ `__repr__` — **nur eines bauen**, das andere erkennen | **23b** — `f"{objekt}"` in fremdem Code | offen |
| **Frage „woher kommt dieser Name?"** (Datei / Import / `self`) | **11** — Oberklasse als vierte Herkunft; **24** — jetzt baust du Module selbst | offen |

### Etappe 10 — Komposition

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `Inventar` und `Ausruestung` als eigene Objekte | **11** — bekommen Dunder-Methoden; **19** — müssen serialisiert werden | offen |
| Slots mit `None` | **19** — `null` in JSON; **23** — `| None` in Typannotationen | offen |
| **`None` ≠ `0`** (keine Waffe ≠ leere Waffe) | **18** — die `or`-Falle bei `0`; **20** — unterschiedliche Fehlermeldungen | offen |
| `is None` statt `== None` | durchgehend — Lesegewohnheit für fremden Code | offen |
| `self.position` als Tuple | **14a** — Position im Raster | offen |
| **Objektidentität: zwei Namen, ein Objekt** — Einlösung aus **4**, jetzt an eigenen Klassen | **14a** — `[["."] * 5] * 5`; **16** — Bug-Kandidat; **19** — was beim Laden neu erzeugt wird | offen |
| Reflex: *„verändern sich zwei Dinge gemeinsam — sind es überhaupt zwei?"* | **16** — genau diese Frage findet den Bug | offen |
| Geteilte Objekte als Fehlerquelle | **16** — Kandidat für die Bug-Jagd | offen |
| Veränderbarer Standardwert in `__init__` | **16** — subtiler, weil er erst beim zweiten Objekt auffällt | offen |
| „hat ein" als Alternative zu „ist ein" | **11** — die Vererbungsfrage braucht diesen Vergleich | offen |

### Etappe 11 — Vererbung

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `Einheit` als gemeinsame Basis | **12** — der Tick läuft über alle Einheiten; **13** — Bauzeit und Nachschub teilen ein Muster | offen |
| Die vier Marine-Klassen | **21a** — unterschiedliche Formeln; **22** — die Frage, ob sie Daten sein sollten | offen |
| **Vier Objekte gleichzeitig — hier entsteht der Trupp** (Einlösung aus **2**) | **12** — drei davon autonom; **14b** — sie bewegen sich; **18** — sie nutzen Fähigkeiten | offen |
| 👀 **Komposition als dritter Weg** (benannt, nicht gebaut) | **22** — dritte Spalte der Entscheidungstabelle; **10**-Rückgriff | offen |
| **Die schriftliche Frage „brauchen wir Vererbung?"** | **22** — Wiedervorlage mit Bauplänen; **25** — die Antwort zeigt sich in JSON | offen |
| `Item` → `Waffe`, `Panzerung`, `Modul`, `Verbrauchsgut` | **21b** — Schadenstypen; **22** — Ausbaustufen | offen |
| 👀 `__len__`, `__contains__`, `__iter__` — **keine Implementierungsaufgabe** | **23a** — Comprehensions über eigene Objekte | offen |
| 👀 `@property` (`am_leben`) — erkennen, nicht bauen | **12** — Prüfung im Tick; **23b** — Dekoratoren allgemein | offen |
| `@property` ohne Klammern ist immer truthy | **16** — genau dieser Typ-3-Fehler | offen |
| `super().__init__()` | **13** — gemeinsame Basis für Zähler-Objekte | offen |
| Die `elif`-Kette aus Etappe 2 stirbt hier | — Einlösung | offen |
| **Die Vererbungsfrage schriftlich in `GELERNT.md`** | **22** — Gegenprobe an Bauplänen; **25** — Endprobe beim Verdaten | offen |

### Etappe 12 — DER TICK ⭐

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `Welt.tick()` und `self.zeit` | **13** — Bauzeiten; **17** — Ereignisse; **18** — Statuseffekte; **22** — alles auf demselben Takt | offen |
| 👀 `update(self, welt)` — Einheiten kennen die Welt (**nur bemerken, nichts reparieren**) | **13** — der Kopplungs-Umweg; **15** — die Kopplungszeichnung; **23b** — Alternativen beim Lesen fremden Codes | offen |
| Status als String (`gegner.status = "tot"`) — zwei Zeilen, mehr nicht | **21b** — `Enum` löst die Strings ab | offen |
| 👀 Der Begriff **Zustandsautomat** (benannt, nicht ausgebaut) | **21b** — dort bekommt er benannte Werte | offen |
| Sammeln und danach entfernen | — Einlösung aus **4**; **16** — bleibt Bug-Kandidat | offen |
| 👀 **Die Tick-Reihenfolge ist eine Entscheidung** — heute nur aufschreiben, nicht optimieren | **16** — dort wird sie zur Tick-Tabelle und zur eigenen Fehlerklasse | offen |
| Einheiten merken sich, wo sie waren | **17** — Material für Ereignisse und Meldungen | offen |
| Ein Tick pro Befehl | **20** — auch bei ungültigem Befehl?; **28** — ein Tick pro Bild | offen |
| **Leseleiter Stufe 2** (Ablauf auf Papier verfolgen) | **16** — genau so findet man Reihenfolgefehler | offen |
| **Trupp-KI Stufe 1: feuern, wenn in Reichweite** | **14b** — Bewegung kommt dazu; **18** — Fähigkeiten kommen dazu | offen |
| Unterscheidung gesteuert ↔ autonom | **13** — autonome Objekte mit Zählern; **23a** — Strategien als Funktionen | offen |

### Etappe 13 — Bauzeit und Nachschub ⭐

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| Das Zähler-Muster (Bauzeit / Nachschub / Räumzeit) | **22** — alle drei kommen aus Bauplänen; **19** — alle drei müssen gespeichert werden | offen |
| `Geschuetz` als Einheit mit Bauzeit | **14b** — steht auf einem Feld und hat Reichweite; **23a** — Zielauswahl-Strategien | offen |
| Der Rekrut mit Nachschubzähler | **17b** — kann endgültig verloren gehen; **18** — Statuseffekte wirken auf ihn | offen |
| 👀 **Der Begriff *Scheduler*** — die Alternative zum Zähler im Objekt, benannt und nicht gebaut | **23b** — beim Lesen fremden Codes als gleichwertige Bauart erkennen | offen |
| `welt.raeume_frei()` ändert Daten zur Laufzeit | — Einlösung aus **5**; **19** — der geänderte Zustand muss mitgespeichert werden | offen |
| **Der Kopplungs-Umweg** (warum kennt das Geschütz die Welt?) | **15** — die Zeichnung macht es sichtbar; **23b** — Callbacks und Strategien als eine Antwort; **24** — Module machen Kopplung schmerzhaft | offen |
| **Zustand ↔ Ereignis als benannter Begriff** (*soll das gelten oder soll das passieren?*) | **17b** — Ereignisse zwischen den Wellen; **19** — was gespeichert wird ist Zustand; **28** — zeichnen ↔ aufblitzen | offen |
| Ausgefallener Trupp-Marine mit `ausfallzeit` | **17b** — kann er endgültig fallen?; **19** — Teil des Speicherstands | offen |
| Unterscheidung „ist fertig" ↔ „wurde gerade fertig" | **19** — Speicherformat; **26** — genau hier lauern Off-by-One-Tests | offen |
| Entscheidung Tick-Zeit statt Echtzeit | **28** — `bauzeit = 180` sind drei Sekunden | offen |

### Etappe 14 — Das Vorfeld ⭐  *(14a Raster · 14b Reichweite und Bewegung)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **14a:** Das Raster als Liste von Listen | **29** — unverändertes Format für die Tilemap; **30** — Grundlage der Isometrie | offen |
| **14a:** Einlösung: aus einer Zeile werden viele | — Einlösung aus **4** | offen |
| **14a:** `vorfeld[y][x]` — Zeile vor Spalte | **29** — dieselbe Reihenfolge beim Zeichnen | offen |
| **14a:** Randprüfung („liegt die Koordinate drauf?") | **14b** — dieselbe Form als Zonengrenze; **20** — wird zu einer abgefangenen Bewegung | offen |
| **14a:** Position als Tuple `(x, y)` — Einlösung aus **6** | **19** — Tuple überlebt JSON nicht | offen |
| ⚠️ **14a: Wegfindung ausdrücklich ausgeschlossen** (kein A\*, kein Dijkstra) | **nach 27** — als notierte Idee in `GELERNT.md`, nicht im Plan | offen |
| 👀 **14a:** `enumerate()` und die drei Schleifenformen — Erkennen, **kein Umbau** | **23a** — dieselben Formen als Comprehension; durchgehend beim Lesen | offen |
| **14a:** Vergleich Dictionary ↔ Raster als Modellierungsfrage | **25** — welche Inhalte werden JSON, welche bleiben Struktur | offen |
| **14a:** `zeichne_vorfeld()` | **28** — dieselbe Funktion, andere Ausgabe | offen |
| **14b:** Reichweite als Set von Tuples | **21a** — wer ist im Feuerbereich; **23a** — als Comprehension | offen |
| **14b: Trupp-KI Stufe 2: nächsten Gegner suchen, Zone halten** | **18** — Fähigkeiten; **23a** — `min`/`sorted` mit `key`, Strategien | offen |
| **14b:** „Nächstes Ziel finden" als Suchalgorithmus | **23a** — `sorted(..., key=lambda ...)`; **26** — testbar mit festen Positionen | offen |
| **14b:** Zonengrenze als Randprüfung | **20** — wird zu einer abgefangenen Bewegung | offen |
| ⭐ **14b (Kür):** `erkundete_felder` als Set (Sensorabdeckung) | **19** — Set → JSON ist nicht trivial | offen |
| ⭐ **14b (Kür): Entscheidung „erkundet" dauerhaft oder nur bei Sicht** | **19** — bestimmt, ob es gespeichert werden muss. *Entfällt, wenn die Kür entfällt.* | offen |

### Etappe 15 — Was die Brut hinterlässt

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **Das Set-Muster: merken → später abfragen** (`add()` … `in`) | **18** — derselbe Speicher, größer; **22** — Voraussetzungen prüfen genauso | offen |
| `erkenntnisse` als Flag-Sammlung | **17b** — beeinflusst, welcher Sektor fällt; **18** — geht im zentralen Set auf | offen |
| Erkenntnisse ändern das Depot-Sortiment | **22** — Voraussetzungen im Ausbaubaum | offen |
| Erkenntnisse ändern Schadensberechnung | **21b** — Schwachpunkte und Widerstände | offen |
| Vorwissen über kommende Wellen | **17a** — der Generator macht das Vorwissen wertvoll | offen |
| Erstes „erweitern ohne zu zerstören" | **26** — Tests machen daraus eine Gewissheit | offen |
| 👀 **Die Kopplungszeichnung** (wer muss von wem wissen?) — **nur bemerken, nichts reparieren** | **23b** — dieselbe Zeichnung ein zweites Mal, dann als Werkzeug; **27** — die schwächste Stelle liegt zwischen zwei Teilen | offen |

### Etappe 16 — Bug-Jagd II

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **Die Tick-Tabelle von Hand** (Phase für Phase, alle Einheiten nebeneinander) | **27** — dieselbe Geduld, angewandt auf fremden Code | offen |
| **Beobachtung → Hypothese → Experiment als verbindlicher Dreizeiler** | — Einlösung aus **8**; **26** — erst der Test, dann der Fix; **27** — dieselbe Form ohne Änderungserlaubnis | offen |
| Regel „nur eine Sache auf einmal ändern" | **21b** — Balancing auf einem Branch; **26** — ein Test prüft eine Annahme | offen |
| **Reihenfolgefehler als vierte Fehlerursache** — Einlösung aus **12** | **17b** — mit Seed reproduzierbar; **28** — die Reihenfolge gilt 60-mal pro Sekunde | offen |
| **Die entschiedene Tick-Reihenfolge in `GELERNT.md`** | **19** — sie gehört zum Zustand des Spiels; **28** — sie wandert unverändert in die Loop | offen |

### Etappe 17 — Der Wellengenerator ⭐  *(17a Zufall · 17b Reproduzierbarkeit und Ereignisse)*

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **17a:** Budget statt Anzahl | **22** — Kosten stehen in denselben Daten; **25** — Wellenrezepte werden JSON | offen |
| 👀 **17a:** Gewichtete Auswahl (`random.choices`) — einbauen erlaubt, Theorie nicht nötig | **17b** — Ereignisse benutzen dieselbe Form; **25** — Gewichte werden Content | offen |
| **17a:** Gegnertypen bekommen **Kosten und Gewichte** — die Typen selbst gibt es seit **6** | **23b** — `@dataclass`; **25** — JSON | offen |
| **17b: Fester Seed** ⭐ | **19** — gehört in den Spielstand; **26** — ohne ihn ist der Generator untestbar | offen |
| **17b: Der Seed als sichtbare Entwicklerfunktion** (`Seed: 48173` in der Anzeige) | **16**-Rückgriff — ein Bug wird vorführbar statt jagdbar; **19** — wird mitgespeichert; **26** — Testvoraussetzung | offen |
| **17b:** Ereignisse als Liste mit Bedingungen | **25** — wandern nach `content/` | offen |
| **17b:** Einlösung `letzte_meldung` | — Einlösung aus **1** | offen |
| ⭐ **17b (Kür):** Der endgültig verlorene Sektor | **19** — muss im Speicherstand stehen; **20** — Bewegung dorthin wird abgefangen. *Entfällt, wenn die Kür entfällt.* | offen |
| 🧠 **17b: Entwicklerfrage** „Wie viel Zufall ist noch fair?" | `GELERNT.md` — wird in **22** und **26** wieder gelesen | offen |

### Etappe 18 — Fähigkeiten und Statuseffekte

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `flags` als zentrales Set | **19** — Set → JSON ist nicht trivial | offen |
| Statuseffekte mit Restdauer (**das Hauptthema**) | **19** — Teil des Speicherstands; **26** — „Effekt läuft ab" als Test | offen |
| 👀 Kurzschluss: `a or b` gibt einen der Werte zurück — **lesen, nicht schreiben** | **23b** — dieselbe Form in fremdem Code | offen |
| Die `or`-Falle bei `0` | — Einlösung aus **2** und **10**; **27** — eines der Warnsignale | offen |
| 🧠 **Entwicklerfrage** „Wo gehört Zustand hin — Einheit oder Welt?" | **22** — dort wird die Antwort auf die Probe gestellt | offen |
| Voraussetzungsprüfung als verknüpfte Bedingung | **22** — Voraussetzungen werden Daten | offen |

### Etappe 19–22

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **19:** JSON-Denkweise (Objekt ≠ Daten) | **25** — Content-Format beruht darauf | offen |
| **19: Serialisierung als Abbildung — und die Frage, ob sie verlustfrei ist** | **25** — dieselbe Skepsis gegenüber fremden Dateien; **26** — Speichern/Laden als Test | offen |
| **19:** Tuple und Set überleben JSON nicht | — Einlösung aus **6** und **14a** | offen |
| **19:** `pathlib` | **25** — `content/`-Verzeichnis laden | offen |
| **19:** `save_version` im Spielstand | **22** — Formatänderung; **25** — Content-Version; **26** — Test für alte Stände | offen |
| **19:** Speicherformat für halb fertige Zähler | **22** — muss Änderungen an Bauzeiten überleben | offen |
| **19:** Der Seed gehört in den Spielstand | — Einlösung aus **17b**; **26** — ein gespeicherter Lauf ist ein Testfall | offen |
| 👀 **19:** Atomares Schreiben (temporäre Datei, dann umbenennen) — **Bonus, nicht Pflicht** | **27** — in fremdem Code als Qualitätsmerkmal erkennen | offen |
| 🧠 **19: Entwicklerfrage** „Was muss ein Spielstand garantieren?" | **25** — dieselbe Frage für Content | offen |
| **20:** 🚨 breites `except` als Warnsignal | **27** — eines der drei Risiken, die du finden sollst | offen |
| **20: Genau eine eigene Exception-Klasse** (`SpielFehler`) | **25** — Content-Fehler bekommen eine eigene; **27** — das Muster in Bibliotheken wiedererkennen | offen |
| 👀 **20:** Exception-**Hierarchien** — erkennen (`except json.JSONDecodeError`), nicht bauen | **25** — bei Bedarf zwei Zeilen mehr | offen |
| 👀 **20:** `finally` — und die vier Schlüsselwörter in einer Zeile | **28** — Autosave bei Fensterschließung, *falls* du es dann brauchst | offen |
| **20:** `finally` schützt vor Programmfehlern, nicht vor `kill -9` | **19**-Rückgriff — deshalb bleibt die temporäre Datei nötig | offen |
| 👀 **20:** Logging-Stufen lesen können (`debug`…`error`) | **27** — fremde Projekte loggen statt zu drucken | offen |
| 🧠 **20: Entwicklerfrage** „Welcher Fehler gehört zum Spieler, welcher zum Entwickler?" | **25** — dieselbe Trennung bei Content-Fehlern | offen |
| **21a:** Trefferrechnung mit zwei Rückgabewerten | — Einlösung aus **6** (Komma-Falle) und **7b** (`return` statt `print`); **26** — erster `parametrize`-Test | offen |
| **21a:** Drei `assert`-Zeilen zur Schadensformel | — Einlösung aus **7b**; **26** — dieselben Zeilen in einer Testdatei | offen |
| **21b:** `Enum` für **die Spielzustände** — eines genügt | — Einlösung aus **12**; **28** — Pygame braucht sie für Modi | offen |
| **21b:** `Enum` ist nicht automatisch besser als ein String | **25** — aus JSON kommen wieder Strings zurück | offen |
| 👀 ⭐ **21b (Kür):** Schadenstypen und Widerstände | **22** — stehen in den Waffendaten; **25** — lassen sich dort billiger nachrüsten als heute | offen |
| **21b:** Erster Branch (Balancing) | **24** — Branches systematisch, Merge oder Verwerfen des Balancing-Branches | offen |
| 🧠 **21b: Entwicklerfrage** „Welche Werte gehören wirklich zum Kampfsystem?" | **22** — Daten oder Verhalten? | offen |
| **22:** Baupläne als Daten | **25** — wandern nach `content/` | offen |
| **22:** Voraussetzung als schlichtes Feld (*Plasmaturm braucht Energiezelle*) | **25** — dieselbe Prüfung, Daten von außen | offen |
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
| **5** (Vorposten) | 3, **4** | `.split()` für `kaufe medkit`, Schrott als Währung, Beute pro Ort, **die Kennung-oder-Anzeigename-Entscheidung** (das Depot braucht die zweite Stelle), **mehrfach `"schrott"` in der Liste als erlebtes Problem** |
| **6** (Datenstrukturen) | **4**, **5** | Mutable/immutable, `in` bei Liste und Dictionary, doppelte Käufe als Problem, **die Frage „Menge oder mehrere Dinge?" — in 4 einmal gestellt, hier für vier Strukturen beantwortet**, **die Gegnerliste als Positionszahlen und der Kaufvorgang, an den sich `AUSBAUTEN` anlehnt** |
| **7a** (Funktionen) | 3, 4, 5, 6 | Die Platzhalterformel, die gewachsene `elif`-Kette |
| **7b** (Trennung) | **7a**, 1, 3b, 4, 5 | Funktionen als Bausteine **und** die Zeichenschnipsel aus 1/3b/4/5 |
| **9a** (Objekte) | **7a** | Die lange Parameterliste — ohne den Schmerz wirkt `self` willkürlich |
| **9b** (`__repr__`) | **9a**, 8 | Klassen **und** der Debugger, sonst fehlt der Anlass |
| **10** (Komposition) | **4**, 9a | Mutable vs. immutable, Aliasing bei Objekten, `__init__` mit Standardwerten |
| **11** (Vererbung) | 2, **4**, **6**, 9a, **10** | **Die `elif`-Kette der Klassenwerte**, Komposition als Vergleichsgrundlage, **die Notizliste „hier war ein String zu dünn" aus Etappe 4 und der Schmerz der zwei parallelen Listen aus Etappe 6** — zusammen sind sie die Begründung für Klassen. *Hier — und nicht in 2 — entsteht der Trupp.* |
| **12** (Tick) | 1, 3a, 4, 6, 9, 11 | Weltzustand in Variablen, **die Hauptschleife**, „nicht iterierend entfernen", `Einheit` als Basis, **vier Marine-Objekte aus 11** |
| **13** (Bauzeit) | **5**, 11, 12 | `sektoren` veränderbar, **Entscheidung zum versiegelten Sektor**, **die Werkstatt als Ort mit ortsgebundenem Befehl**, laufender Tick |
| **14a** (Raster) | 3a, **4**, 5, 6 | `range()`, **die Anmarschbahn als eine Zeile und die Entscheidung, ob sie der Zustand oder sein Bild ist**, `.join()`, das dreischrittige Bauen, Dictionary als Gegenbeispiel, Tuple |
| **14b** (Reichweite, Bewegung) | **14a**, 6, 10, 12, 13 | Das Raster, **Set und Tuple**, `self.position`, Trupp-KI Stufe 1, das Geschütz |
| **15** (Erkenntnisse) | 4, **6**, 12 | Der Datenkern aus 4, **`GEGNERTYPEN` und `gesehene_gegnertypen`** — Erkenntnisse hängen sich an vorhandene Typ-Einträge, sie erfinden keine |
| **16** (Bug-Jagd II) | **8**, 12, 13, 14b | Debugger, Halbieren, das eigene Protokoll, **eine notierte Tick-Reihenfolge aus 12**, mehrere Systeme im selben Tick |
| **17a** (Zufall) | 3a, **6**, 9a, 15 | `range()` über Wellen, **die Gegnertypen und die `if`/`elif`-Wellenkette, die hier durch das Budget ersetzt wird**, `Gegner` als Klasse, Vorwissen aus Erkenntnissen |
| **17b** (Seed, Ereignisse) | **17a**, **1**, 2, 12, 16 | **`letzte_meldung` vom ersten Tag**, `meldung_abgesetzt`, Einheiten-Gedächtnis, **das Bedürfnis nach Reproduzierbarkeit aus 16** |
| **18** (Fähigkeiten) | 2, 6, 10, 15 | Verknüpfte Bedingungen, **Set und Mengenoperationen**, `None` ≠ `0`, Erkenntnis-Flags |
| **19** (Speichern) | 6, 10, 12, 13, **14a**, 17b, 18 | Sets und Tuples, `None`, `self.zeit`, halb fertige Zähler, **der Seed**, Restdauern. *`erkundete_felder` nur, wenn die Kür in 14b gebaut wurde.* |
| **20** (Fehlerbehandlung) | 1, 2, 3b, **4**, 5, 14a | **`int()` und `ValueError` aus Etappe 1**, `else`-Zweige, **drei Stellen aus Etappe 4: volles Inventar, `remove()` ohne Element, Befehl ohne zweites Wort**, die drei Kaufbedingungen, Randprüfung |
| **21a** (Rechnung) | 6, **7a**, **7b**, 10, 14b | `berechne_schaden()`, Komma-Falle beim Tuple, `return` statt `print`, Slots, Reichweite |
| **21b** (Zustände, Branch) | **21a**, 12, 11, 0 | Die Zustandsstrings aus 12, Waffenklassen, Git-Minimalset |
| **22** (Baupläne) | **5**, 11, 13, 15, 18 | **Entscheidung zur ausverkauften Ware**, **der Kauf, der keine Warennamen kennt**, die Vererbungsfrage **und die Komposition aus 11**, das Zähler-Muster, Erkenntnisse als Voraussetzung |
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

**Die drittkritischste ist Etappe 11.** Seit Fassung 3 entsteht der Trupp erst dort — Etappe 2 setzt nur noch die gewählte Klasse. Wer in 11 die vier Objekte nicht tatsächlich nebeneinander erzeugt, hinterlässt drei tote Klassen, und die Etappen 12, 14b, 16, 18 und 23a verlieren ihren Gegenstand.

**Die zweitkritischste ist Etappe 28.** Sie löst keine Erzählschuld ein, sondern eine strukturelle: Wenn die Entscheidung aus Etappe 7 nicht durchgehalten wurde — Logik gibt zurück, Darstellung gibt aus — dann ist Block 4 kein Aufsatz, sondern eine Neuschreibung.

---

## Teil C — Durchgehende Fäden

Kein einzelner Verweis, sondern etwas, das über den ganzen Plan läuft.

**Die Darstellung** — Etappe 1 (fester ASCII-Kopf) → **2 (hält bewusst still: nur mehr Variablen im selben Briefing)** → **3c (Balken beim `status`-Befehl; der Kopf bleibt unangetastet)** → **4 (die Anmarschbahn — eine Zeile, in der man Bewegung sieht; ab hier ist die Anzeige auch Messgerät)** → **5 (der Grundriss mit Markierung — handgezeichnet, nur die Markierung kommt aus den Daten)** → **6 (die Bahn zeigt verschiedene Zeichen je Gegnertyp — die Darstellung liest zum ersten Mal aus zwei Quellen)** → 7b (eigene Zeichenschicht, die nichts entscheidet) → **14a (aus einer Zeile wird ein Raster)** → 28 (dieselbe Schicht, andere Ausgabe) → 29 (Kacheln) → 30 (Isometrie). Der Faden hat zwei Zwecke: Das Spiel ist früh sichtbar, und die Trennung Logik/Darstellung wird eingeübt, lange bevor sie in Etappe 28 zur Bedingung wird.

**Die Leseleiter** ⭐ — vier Stufen mit festen Fragen. Stufe 1 (Benennen): Etappe 9–11, 5–10 Zeilen. Stufe 2 (Verfolgen): 12–16, 15–30 Zeilen — zahlt direkt in 16 bei den Reihenfolgefehlern. Stufe 3 (Zusammenhänge): 17–22, 30–60 Zeilen. Stufe 4 (Beurteilen): ab 23b, echter KI-Code, hier kommt die sechste Frage dazu → **27 (ganzes Repo, Frage 7 ist Frage 6)**. Die Stufen dürfen nicht übersprungen werden: Frage 6 setzt voraus, dass Alternativen bekannt sind.

**Die Null-Falle** — Etappe 2 (truthy/falsy, `0` ist falsy) → **4 (`if inventar:` — die leere Liste ist falsy, und dazu die Frage: *kann diese Variable legitim `0` sein?*)** → 10 (**`None` ≠ `0`**: keine Waffe ≠ leere Waffe) → 14a (Feld 0, Index 0, `x = -1` greift von hinten) → **18 (`x or standard` greift falsch, wenn `0` gültig ist — dort 👀, als Lesefalle)** → 19 (`null` in JSON) → 20 (drei verschiedene Fehlermeldungen statt einer). In diesem Setting ist `0` überall — deshalb ist das der wichtigste der Lesefäden.

**Die drei Schleifenformen** 👀 — angelegt in Etappe 3a (`for x in dinge`) und 5 (`.items()`) → **14a (Erkennungsdrill mit allen dreien, `enumerate()` kommt dazu — zwei Minuten, kein Umbau)** → 23a (dieselben Formen als Comprehension). **Ziel ist Erkennen, nicht Schreiben** — der ganze Faden liegt auf Stufe 👀.

**Namen und ihre Herkunft (Modul-Lesen vor Modul-Bauen)** — Etappe 9 (jede Leseübung fragt: aus dieser Datei, aus einem Import, oder von `self`?) → 11 (Vererbung: ein Name kann aus der Oberklasse kommen) → 23a (Funktionen als Werte — Namen zeigen auf Funktionen) → **24 (jetzt baust du selbst Module; die fremde Bibliothek liest du am selben Tag)** → 27 (Importe als Inhaltsverzeichnis eines fremden Repos). Absicht: Bei Etappe 24 soll `from einheiten import Marine` ein Wiedererkennen sein, kein Rätsel.

**Behauptungen über Zustand** — Etappe 7b (`assert` als 👀-Ausblick, drei Zeilen, **kein** Testeinstieg) → 13 (Zähler-Invarianten) → 20 (Prüfen vorher ↔ Fangen hinterher) → 21a (drei `assert`-Zeilen zur Schadensformel — die erste echte Anwendung) → 25 (die Validierungsliste) → **26 (`pytest` ist derselbe `assert` in einem Rahmen)**. Und als Lesefrage ab 7b durchgehend: *Welche Annahmen macht diese Funktion, und prüft sie eine davon?*

**Wichtig für die Buchführung:** Zwischen 7b und 26 liegen Monate, und in dieser Zeit steht `assert` bewusst still. Wer in 13 oder 20 daraus schon Testarbeit macht, verbrennt Etappe 26 und überlädt die Zwischenetappen. Der Faden ist absichtlich dünn.

**Kopplung als Lesekriterium** — Etappe 12 (👀 `update(self, welt)`: nur bemerken) → 13 (der Umweg: warum kennt das Geschütz die ganze Welt?) → **15 (👀 die Zeichnung zum ersten Mal — fünf Minuten, nichts wird repariert)** → **23b (dieselbe Zeichnung zum zweiten Mal, jetzt als Werkzeug und im Vergleich)** → 24 (zirkulärer Import macht Kopplung schmerzhaft) → 27 (die schwächste Stelle liegt zwischen zwei Teilen, nicht in einem).

Der Faden liegt bis 23b vollständig auf Stufe 👀. Das ist Absicht: Kopplung ist das wichtigste Beurteilungskriterium des ganzen Plans und gleichzeitig das, an dem ein Anfänger am schnellsten hängenbleibt, wenn er es zu früh reparieren soll.

**Der Trupp** ⭐ — **Etappe 11 (hier entsteht er: vier Objekte, sichtbar nebeneinander)** → **12 (die drei anderen bekommen `update()`: feuern, wenn in Reichweite)** → 13 (ausgefallener Marine folgt dem Zähler-Muster) → **14b (nächsten Gegner suchen, Zone halten)** → 16 (sie stehen in der Tick-Tabelle) → 18 (sie nutzen Fähigkeiten — und hört hier auf) → 23a (Zielauswahl-Strategien gelten für Marines *und* Geschütze). Zweck: Ohne den Trupp sind drei der vier Klassen toter Code, und Vererbung in Etappe 11 bleibt eine Behauptung.

**Geändert in Fassung 3:** Der Trupp begann früher in Etappe 2, wo die `if`/`elif`-Kette alle vier Wertesätze setzte. Das erzeugte Daten, die das Spiel monatelang nicht benutzte, und verdeckte den eigentlichen Lernstoff von Etappe 2 — *eine* Kette wählt *einen* Zweig. Der Faden beginnt jetzt erst dort, wo er auch etwas tut.

**Beobachtbarkeit** — die Frage *woher weißt du, dass es das Richtige tut?* **Etappe 3c (der Balken macht 110 % und negative Werte sofort sichtbar — und soll sie ausdrücklich *nicht* begrenzen)** → 4 (Bahn zeigt übersprungene Einheiten) → 7b (`assert`) → 8 (Debugger) → 9b (`__repr__`) → 13 (Zähler sichtbar machen) → 16 (Tick-Tabelle) → **17b (der Seed, sichtbar in der Debug-Anzeige)** → 19 (Speicherstand als lesbarer Zustand) → 20 (Logging) → **26 (Tests: alle Annahmen auf einmal)**.

**Vorhersagen → Ausführen → Vergleichen → Erklären** — ab Etappe 1 bei jedem Kaputtmach-Experiment. Verdichtet in **16** (Tick-Tabelle gegen Programmlauf) und **27** (fünfhundert Zeilen fremder Code, Ausführen erst nach der Analyse).

**Daten statt Code** ⭐ — der Faden, der zur Prämisse führt: **5** (der Kauf schlägt Preise nach, statt sie abzufragen — eine neue Ware ist eine Zeile in den Daten) → **13** (Bauzeiten stehen bei den Objekten) → **17a** (Gegnertypen als Datensätze) → **22** (Baupläne als Daten, und die Frage *was ist Inhalt, was Verhalten?*) → **23a** (die Befehlskette stirbt durch ein Dictionary) → **25** (alles wandert nach `content/`). Prüffrage, die in **5** zum ersten Mal gestellt wird: **Ändert sich diese Liste? Dann sind es Daten.**

**🚨 KI-Code-Warnsignale** — ab Etappe 8 verteilt: 12 (`update(self, welt)` — warum die ganze Welt?), 15 (die Zeile, die das halbe Spiel kennt), 20 (breites `except`), 22 (`elif`-Kette statt Daten), 23b (Funktion mit acht Parametern), 26 (kein einziger Test), durchgehend die Null-Falle → **27 (drei Risiken finden)**. Alle liegen auf Stufe 👀: bemerken und benennen, nicht beheben.

**Erweitern ohne zu zerstören** — **Etappe 4 (der Befehlsumbau darf die Befehle aus 3b nicht brechen)** → **5 (der `vorrat`-Umbau fasst Statusanzeige, Feuern und Aufsammeln an; eigener Rückwärtsgang-Schritt)** → **6 (die zweite Gegnerliste darf Bewegung, Feuern und Wellenende nicht brechen)** → 7a (erstes Refactoring) → 15 (vierter Fund ohne Änderung der Depot-Logik) → 19 (Statuseffekte mitspeichern) → 22 (neuer Geschütztyp ohne Logikänderung) → 25 (Gegnertypen als JSON) → 26 (Tests machen daraus Gewissheit).

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

**Parallele Sammlungen als Muster** — zwei Strukturen, die über den Index oder denselben Schlüssel zusammenhängen: **5** (`waren` und `stapelbar` — zwei Tabellen, ein Schlüsselsatz) → **6** (`gegner` und `gegner_typen` — zwei Listen, ein Index) → **11 / 22** (beide Male werden sie zu **einer** Struktur zusammengezogen). Gemeinsame Erkenntnis: **Zwei Sammlungen, die immer gleich lang sein müssen, sind eine Sammlung, die noch nicht gebaut wurde.**

**Migrationen — was womit ersetzt wird** ⭐

Der Plan baut mehrfach etwas Funktionierendes um. **Diese Übergänge müssen festgelegt sein, sonst entstehen zwei Wahrheiten über dieselbe Sache:**

| Was | Bis | Ab | Regel |
|---|---|---|---|
| **Gegner** | 3: `gegner_anzahl = 5` | 4: `gegner = [7, 4, 2]` | Die Anzahl verschwindet, `len()` ersetzt sie. **Keine zweite Zählvariable.** |
| **Gegner** | 4: Positionszahlen | 6: `gegner` **plus** `gegner_typen`, über den Index verbunden | Zwei parallele Listen, bewusst unbequem. **`len()` beider muss immer gleich sein.** |
| **Gegner** | 6: zwei parallele Listen | 9/11: `Gegner`-Objekte | **Beide Listen kollabieren zu einer.** Position und Typ werden Attribute desselben Objekts. Das ist der Zahltag für den Schmerz aus 6. |
| **Munition** | 3: `munition = 40` | 5: `vorrat["munition"]` | Die lose Variable verschwindet. **Kein zweiter Speicher.** |
| **Munition** | 5: loses `vorrat` | 9: `marine.vorrat` | Der ganze Vorrat wandert in den Marine — **`marine.munition` wird nicht neu eingeführt.** |
| **Schrott** | 4: Eintrag in `inventar` | 5: `vorrat["schrott"]` | **Schrott ist ab 5 Ressource, kein Gegenstand.** Nie beides gleichzeitig. |
| **Inventar** | 4: Liste von Strings | 11: Liste von `Item`-Objekten | Die Liste bleibt, der Eintrag wird reicher. |
| **Zustandsstrings** | 12: `"tot"` | 21b: `Enum` | Nur die Spielzustände, nicht jeder String im Programm. |

**Und das Ritual dazu, ab Etappe 4 in jedem Guide vor einem Umbau:** *Was bleibt gleich? Was ändert sich nur in der Darstellung? Was ändert sich wirklich am Datenmodell?* Zweck: **Umbauen heißt nicht „alles neu".**

**Invarianten** — Sätze, die immer wahr bleiben müssen: **4** (`len(gegner)` ist die Wahrheit; keine Position außerhalb der Bahn; Munition nie negativ) → **5** (jeder Nachbarname existiert; jeder Sektor hat Beschreibung und Integrität) → **6** (`len(gegner)` und `len(gegner_typen)` sind immer gleich; jeder gesehene Typ existiert in `GEGNERTYPEN`) → **13** (Bauzeit kann nicht gleichzeitig laufen und fertig sein) → **20** (aus Invarianten werden Prüfungen) → **26** (aus Prüfungen werden Tests). **Bis 20 werden sie nur aufgeschrieben, nicht geprüft** — das ist Absicht, weil `assert` erst in 7b als 👀 auftaucht.

**Die drei Debugging-Reflexe** — je einer pro Fundament-Etappe, alle nach demselben Grundsatz *Nachsehen schlägt Vermuten*: Etappe 1 *welchen Typ hat dieser Wert?* (`print(type(x))`) → Etappe 2 *welcher Zweig läuft?* (`### ZWEIG`) → **Etappe 3 *wie oft läuft das?* (`### RUNDE n`)** → **Etappe 4 *was steht da gerade wirklich drin?* (`### VOR`/`### NACH` mit Inhalt **und** `len()`)** → **Etappe 5 *unter welchem Namen?* (`.keys()` zeigt Tippfehler in Schlüsseln, die sonst unsichtbar sind)** → **8** (der Debugger löst alle vier `print`-Varianten ab, der Reflex bleibt). Gemeinsamer Grundsatz: **Nachsehen schlägt Vermuten.**

**Werkzeuge selbst befragen** 👀 — statt nachzuschlagen: **4** (`dir([])`, `help([].append)`, und `.join()` wird ausdrücklich selbst gesucht) → **5** (`dir({})`, `help({}.get)`; `.keys()` wird zum Debugwerkzeug) → **9b** (dieselbe Technik an eigenen Klassen) → **24** (eine fremde Bibliotheks-API lesen) → **27** (vor einem fremden Repo sind das die zwei Werkzeuge, die man immer hat). Zweck: Eine Erklärung *wiederzuerkennen* fühlt sich an wie sie zu *wissen* — der Unterschied fällt erst auf, wenn niemand da ist, den man fragen kann.

**Die Bug-Jagd** — Etappe 8 (erste Runde, Werkzeuge und Protokoll) → 16 (subtilere Fehler; dort auch **Reihenfolgefehler im Tick** und ein **manipulierter Speicherstand**, sobald Etappe 19 ihn möglich macht) → 26 (umgekehrt: erst Test, dann Fix). Dazwischen unregelmäßig und unangekündigt.

**Das Formular dazu** — *Beobachtung → Hypothese → Experiment*, in 8 als Denkform angelegt, in **16** zum verbindlichen Dreizeiler gemacht, in **27** ohne Änderungserlaubnis angewandt. Es ist das Gegenstück zum Ritual *Vorhersagen → Ausführen → Vergleichen → Erklären*: Das eine gilt für Code, den du neu schreibst, das andere für Code, der sich falsch verhält.

**Die drei Fehlertypen** — eingeführt im Lehrplan, erlebt in Etappe 1 (fehlendes `f`, vergessenes `int()`), Etappe 2 (falsche Einrückung in der Klassenkette), Etappe 3 (Rundenzähler an der falschen Stelle), Etappe 4 (`liste = liste.append(...)`, Gegner beim Iterieren entfernen), Etappe 5 (`schrott - preis` ohne Zuweisung), **Etappe 4 (eine Liste verändern, während man über sie läuft — der erste Typ-3-Fehler, den der Lernende *sehen* kann, weil die Anmarschbahn ihn zeigt)**, **Etappe 5 (`x - y` statt `x -= y` beim Abbuchen — unendlich Geld ohne jede Meldung; und der Tippfehler im Schlüssel, der still einen neuen Eintrag anlegt)**, Etappe 10 (zwei Marines, ein Inventar), Etappe 11 (`@property` ohne Klammern ist immer truthy), Etappe 14a (`x = -1` greift von hinten), Etappe 14b (`<=` statt `<` bei der Reichweite) → **systematisch benannt und geübt in Etappe 8** → Etappe 12 (Tick zweimal pro Befehl), Etappe 16 (Reihenfolge im Tick), Etappe 20 (`except:` verwandelt Typ 1 in Typ 3), Etappe 21a (Panzerung größer als Schaden heilt den Gegner), Etappe 21b (`"weele"` gegen `Spielzustand.WEELE`), Etappe 25 (`"hp": "sehr viel"` ist gültiges JSON).

**Zahlen als Lehrmittel** — dieses Setting rechnet überall, und deshalb ist Typ 3 hier der Normalfall statt der Ausnahme. Ab Etappe 3 zeigt die Balkendarstellung Rechenfehler an, die in einer Zahlenkolonne unsichtbar wären. Ab Etappe 4 zeigt die Anmarschbahn Listenfehler an. Das ist Absicht: Die Darstellung ist Teil des Debugging-Werkzeugkastens.

**Git** — Etappe 0 (Minimalset) → **21b (erster Branch mit echtem Zweck: Balancing)** → 24 (Merges, Konflikte, Rückgängigmachen; der Balancing-Branch ist das Übungsobjekt). **Pull Requests, Rebase und Cherry-Pick stehen nicht im Plan** — sie sind kein offener Posten, sondern eine begründete Auslassung.

**Ein Commit pro Portion**, nicht pro Etappe: Die geteilten Etappen haben einen Zwischen-Commit (`Etappe 14a: …`). Nach sechs Monaten ist `git log --oneline` die ehrlichste Fortschrittsanzeige, die es gibt — und mit 37 statt 30 Einträgen eine dichtere.

**Schreiben → Lesen** — Etappe 7a (Struktur in fremdem Code erkennen) → 9 (erste Leseübung) → 15 (fremde Funktion mit stiller Annahme) → alle Etappen ab dort → 23b (Code aus echten Projekten) → **27 (ein ganzes fremdes Repo, ohne Hilfe)**. Das ist der eigentliche Zweck des Projekts, und Etappe 27 ist seine Einlösung.

**Die Prämisse** — Etappe 1 (vier Klassen, zwanzig Wellen, ein Kern) → 11 (die Klassen werden Code, **alle vier gleichzeitig**) → 13 (das erste Geschütz macht die Zeit spürbar) → 17b (ein Sektor fällt endgültig — Kür) → 22 (die Klassenfrage kommt zurück) → 25 (Vielfalt ohne Code).

**Die Balancing-Falle** — benannt im Lehrplan, **im Guide zum ersten Mal akut in 3c (Schaden und Gegneranzahl), mit Fünfzehn-Minuten-Deckel und der Notizliste als Ventil**, Höhepunkt bei 17a (Wellenbudget) und 21b (Kampfformel). Gegenmittel: Zeitlimit, Branch ab 21b, und die Regel „eine langweilige Welle, die läuft, schlägt eine spannende, die abstürzt".

**Die drei Anspruchsstufen** 🔨🧠👀 — kein Verweisfaden, sondern die Regel, nach der alle anderen gelesen werden. Sie steht ab Etappe 3 in fast jedem Etappenkopf. **Für dieses Register heißt sie:** Wer eine 👀-Schuld einlöst, schuldet einen Satz, keine Implementierung. Wer sie zur Bauaufgabe macht, überlädt die Ziel-Etappe — und genau daran war Fassung 2 an sieben Stellen gescheitert.

**🧠 Die Entwicklerfrage** — je eine ab Etappe 17: 17b (wie viel Zufall ist fair?) → 18 (wo gehört Zustand hin?) → 19 (was muss ein Spielstand garantieren?) → 20 (welcher Fehler gehört wem?) → 21b (welche Werte gehören zum Kampfsystem?) → 22 (was ist Inhalt, was Verhalten?) → 23b (wer muss wen kennen?) → 24 (wann hilft Aufteilung?) → 25 (wem vertraue ich?) → 26 (was beweist ein grüner Test?) → **27 (woran erkennst du, dass jemand nachgedacht hat?)**. Alle Antworten stehen in `GELERNT.md` und werden **nicht** korrigiert — sie werden später wiedergelesen. Der Wert liegt im Vergleich zwischen der Antwort von damals und der von heute.

---

## Teil D — Pflege

**Was der Status bedeutet.** Er beschreibt den Zustand des **Tutorials**, nicht deines Codes: `eingelöst` heißt, dass der Guide für die Ziel-Etappe geschrieben ist und diese Schuld dort tatsächlich einlöst. Solange eine Ziel-Etappe noch nicht ausgearbeitet ist, bleibt der Eintrag `offen` — auch wenn die Idee feststeht.

Damit beantwortet die Spalte genau die Frage, die beim Weiterschreiben zählt: *Was muss die nächste Etappe noch abarbeiten?*

**Wenn eine Etappe fertig geschrieben ist:** alle Schulden durchgehen, die auf sie zeigen, und prüfen, ob der Guide sie wirklich einlöst. Was er nicht einlöst, bleibt offen und wandert auf die nächste Ziel-Etappe.

**Wenn du von der Vorgabe abweichst:** Eintrag anpassen, nicht löschen. Wenn du in Etappe 6 doch keine Sets nimmst, müssen 14 und 18 das wissen. Eine Zeile hier erspart dir eine Stunde Verwirrung dort.

**Wenn ein Umweg entsteht:** Eintragen. Der Kopplungs-Umweg bei Etappe 13 steht bereits drin. Weitere kommen — ab Etappe 17 ist das der Normalfall und nicht die Ausnahme.

**Wenn eine Kür entfällt:** Zwei Einträge hängen an optionalen Teilen — die Sensorabdeckung (14b) und der endgültig verlorene Sektor (17b). Wird die Kür nicht gebaut, sind die abhängigen Zeilen in **19** und **20** keine offene Schuld, sondern **entfallen**. Streich sie nicht, sondern setz den Status auf `entfällt` und schreib dazu, warum. Sonst suchst du in vier Monaten nach einer Einlösung, die es nie geben sollte.

**Wenn du eine Etappe selbst teilst:** Das ist ausdrücklich erlaubt (Lehrplan, *Etappen dürfen halbiert werden*). Für den Bogen ändert sich dabei nichts — die Verweise zeigen auf Nummern, nicht auf Portionen. Ergänz höchstens den Buchstaben, wenn es die Buchführung klarer macht.

**Wenn du eine 👀-Schuld doch ausbaust:** Auch das ist erlaubt, aber trag es ein. Wer `__iter__` in Etappe 11 tatsächlich implementiert, hat danach eine Etappe 23a, die eine halbe Sitzung kürzer ist — und eine Etappe 11, die zwei Abende länger war. Beides ist vertretbar; unsichtbar sollte es nicht bleiben.

**Zur Fassung dieser Datei:** Sie ist auf Lehrplan-Fassung 3 nachgezogen. Keine Etappennummer hat sich geändert, deshalb bleibt jeder ältere Verweis gültig. Neu sind: die Portionsangaben (`14a`), die Stufenmarkierung 👀, ein eigener Abschnitt für **Etappe 16** (den es vorher nicht gab), die Verlagerung des Trupps von 2 nach 11 und die Einträge zu den Entwicklerfragen.

**Zur Herkunft dieser Datei:** Sie ist die Portierung des Bogens aus dem Dorf-RPG-Lehrplan. Die Etappennummern und Python-Themen sind identisch geblieben; getauscht wurden nur die Vehikel. Wo ein Eintrag im alten Bogen an Dialogen, NPCs oder der Mine hing, hängt er hier an Fähigkeiten, Einheiten und dem Vorfeld. Neu hinzugekommen ist der Faden **Darstellung** — im RPG gab es ihn nicht, weil dort bis Etappe 28 nichts zu sehen war.

**Wenn du mit mir arbeitest:** Verweis mich bei jeder Etappe ab 12 auf diese Datei. Nicht aus Misstrauen — ich habe über Monate kein verlässliches Gedächtnis, und eine plausible Rekonstruktion ist schlimmer als ein Nachschlagen.
