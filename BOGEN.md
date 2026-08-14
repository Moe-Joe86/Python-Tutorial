# Der Bogen — Register aller Vorausverweise

> Verbindlicher Anhang zum [Lehrplan](RPG_Lehrplan.md). Diese Datei ist die einzige Quelle der Wahrheit für alles, was eine frühe Etappe verspricht und eine späte einlösen muss.

---

## Wozu es diese Datei gibt

Der Lehrplan verspricht ständig etwas: *„Diese Variable brauchst du in Etappe 17."* — *„Das Raster wird in Etappe 28 zur Tilemap."* Diese Versprechen sind der Grund, warum sich das Projekt wie ein Bogen anfühlt und nicht wie 29 Übungsaufgaben.

Aber sie sind auch eine Schuld. Wenn Etappe 17 kommt und dort nichts eingelöst wird, war das Versprechen eine Behauptung.

Diese Datei ist die Buchführung darüber. Sie hat drei Adressaten:

**Dich.** Wenn du bei Etappe 12 sitzt und dich fragst, warum du in Etappe 6 ein Set statt einer Liste genommen hast, steht die Antwort hier.

**Mich.** Ich habe kein verlässliches Langzeitgedächtnis über Monate. Wenn du bei Etappe 17 ankommst, weiß ich nicht mehr zuverlässig, was ich in Etappe 2 versprochen habe — ich würde es rekonstruieren, und Rekonstruktion ist Raten mit gutem Ruf. Verweis mich bei jeder späten Etappe auf diese Datei, dann rate ich nicht.

**Jeden, der den Guide liest.** Das Register macht sichtbar, dass die Struktur Absicht ist.

**Regel:** Wer einen neuen Vorausverweis in eine Etappe schreibt, trägt ihn hier ein. Ohne Ausnahme. Ein Verweis, der nicht im Register steht, existiert nicht.

---

## Teil A — Was gepflanzt wird

Chronologisch nach Etappe. Spalte „Status": `offen` = noch nicht eingelöst, `eingelöst` = erledigt und geprüft.

### Etappe 1 — Der erste Morgen

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `geruch` als Variable statt als Satz | **17** — Rückblende: „Du erinnerst dich an den Geruch von Brot…" | offen |
| Weitere Sinnesvariablen (Geräusch, Licht, Temperatur) | **17** — Material für weitere Rückblenden | offen |
| Prinzip: Weltzustand speichern, nicht nur ausgeben | **12** — der gesamte Tick beruht darauf | offen |
| „Name zeigt auf Wert" statt „Behälter" | **4** — Aliasing: `b = a` und beide ändern sich | offen |
| `=` als „bekommt den Wert" lesen | **2** — Abgrenzung zu `==` | offen |
| `tageszeit` (angelegt, ungenutzt) | **2** — erste Bedingung auf Weltzustand | offen |
| Sprachentscheidung Variablennamen (de/en) | durchgehend — Konsistenz bis 29 | offen |
| `int()` kann mit `ValueError` scheitern | **20** — echte Fehlerbehandlung | offen |

### Etappe 2 — Die erste Begegnung

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `vertrauen = True/False` | **18** — wird zum Vertrauens- und Flag-System | offen |
| Verknüpfte Bedingungen (`and`/`or`/`not`) | **18** — Dialoge prüfen mehrere Flags | offen |
| `.lower()` / `.strip()` auf Eingaben | **3** — Befehle; **5** — `gehe norden`; **7** — `verarbeite_befehl()` | offen |
| Punkt-Schreibweise (`wert.methode()`) | **9** — `npc.speak()` bei Objekten | offen |
| Der `else`-Zweig für Unerwartetes | **20** — `try`/`except` statt Auffangbecken | offen |
| Die Wahl Erzählen ↔ Schweigen | **17** — wirkt mit, wer als Nächstes verschwindet | offen |
| **Wer** den Spieler findet (Design-Entscheidung) | **18** — diese Figur ist die Bezugsfigur | offen |
| Die gefundene Figur selbst | **12** — bekommt Tagesablauf und Gedächtnis | offen |
| `elif` ≠ mehrere `if` | **17** — mehrere Ereignisse treffen gleichzeitig zu | offen |
| Truthy/Falsy-Liste | **4** — `if inventar:`; **18** — als Gefahr bei `0` | offen |
| `and`/`or` geben mehr zurück als `True`/`False` | **18** — Kurzschlussauswertung | offen |
| `print()`-Debugging als Reflex | **8** — der Debugger als bessere Variante | offen |
| Optional: Name der Figur in einer Variable | **9** — wird zu `npc.name` | offen |
| Optional: Spieler kann lügen | **18** — Symmetrie zum unzuverlässigen Fremden | offen |

### Etappe 3 — Die Game-Loop

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `range()` | **14** — Schleifen über das Minenraster | offen |
| `range()` zählt ab 0 | **4** — derselbe Grund, warum der erste Listenindex 0 ist | offen |
| Befehlsverarbeitung (`umsehen`, `reden`) | **7** — wandert in `verarbeite_befehl()` | offen |
| Die Hauptschleife selbst | **12** — jeder Durchlauf löst einen Tick aus | offen |
| Die Loop-Struktur | **27** — wird zur Pygame-Loop mit 60 fps | offen |
| Zähler mit `+=` | **12** — wird zu `self.zeit += 1`, der Weltzeit | offen |
| Eingabe-Wiederholung bei ungültiger Antwort | **20** — wird zu `try`/`except`-Validierung | offen |
| Befehl `beenden` | **19** — dort wird vor dem Beenden gespeichert | offen |
| `else`-Zweig für unbekannte Befehle | **5** — wächst mit jedem neuen Befehl mit | offen |
| Lange `elif`-Kette (bewusst ertragen) | **5** — Dictionary löst sie ab | offen |
| Design-Entscheidung Befehlssprache | **4** `nimm brot`; **5** `gehe norden`; **25** Befehle als Content | offen |
| `_` als Schleifenvariable (nur zum Erkennen) | **23** — pythonische Schreibweisen | offen |
| Optional: Zähler verändert die Erzählung | **12** — Reaktion auf verstrichene Zeit statt auf Eingabe | offen |

### Etappe 4 — Das Inventar

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| Mutable vs. immutable | **10** — geteiltes `Inventory()`-Objekt; **14** — `[["."] * 5] * 5` | offen |
| `inventar` als Liste von Strings | **11** — wird zur Liste von `Item`-Objekten | offen |
| Der Schlüssel, der zu keiner Tür passt | **14** — Zugang zur Mine | offen |
| Obergrenze 10 Gegenstände | **20** — „Inventar voll" als abgefangener Fall | offen |
| Index ab 0 | **14** — `karte[y][x]` im Minenraster | offen |
| `len()` | **14** — `range(len(karte))` | offen |
| `in` bei einer Liste | **6** — Gegenüberstellung Liste / Set / Dictionary | offen |
| `remove()` scheitert an fehlendem Element | **20** — wird zu `try` / `except` | offen |
| `.split()` für Zwei-Wort-Befehle | **5** — `gehe norden`; **7** — `verarbeite_befehl()` | offen |
| Kennung ↔ Anzeigename eines Gegenstands | **11** — `item.id` / `item.name`; **25** — JSON-Schlüssel | offen |
| Liste nie verändern, während man darüber läuft | **12** — NPC beim Iterieren entfernen | offen |
| `.copy()` als bewusste Kopie | **10** — die Alternative zum geteilten Objekt | offen |
| Mengen lassen sich mit Listen schlecht führen | **5** — Dictionary löst das | offen |
| Optional: `untersuche <ding>` | **15** — Funde in der Mine sind Wissen, nicht Ausrüstung | offen |
| Erkenntnis: Code beruht auf unausgesprochenen Annahmen über Eingaben | **7** — Aufräumen macht sie sichtbar; **20** — Validierung löst sie auf | offen |

### Etappe 5 — Die Karte

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `orte` als Dictionary | **13** — wird zur Laufzeit verändert | offen |
| Trennung Daten ↔ Code | **25** — Inhalt wandert komplett nach `content/` | offen |
| Verschlossener Mineneingang | **14** — die Mine öffnet sich | offen |
| Die Wiese | **13** — dort wird gepflanzt | offen |
| `in` prüft beim Dict den **Schlüssel** | **6** — Gegenüberstellung Liste/Set/Dict | offen |
| Verschachtelte Struktur (Dict im Dict) | **19** — genau diese Form ist JSON; **25** — Content-Format | offen |
| Schlüssel müssen immutable sein | **6** — warum ein Set keine Listen aufnimmt | offen |
| `aktueller_ort` als Zustandsvariable | **10** — wird zu `player.ort`; **19** — Teil des Speicherstands | offen |
| `.get()` für sicheren Zugriff | **20** — die leichtere Alternative zu `try` / `except` | offen |
| `.items()` zum Iterieren | **12** — über alle NPCs laufen | offen |
| Zuweisung ändert die Karte zur Laufzeit | **13** — `world.oeffne_weg()` ist genau diese Zeile | offen |
| Gegenstände gehören zum Ort | **13** — Pflanzen gehören zur Wiese, nicht zum Spieler | offen |
| Dictionary nicht ändern, während man iteriert | **12** — dasselbe bei NPCs | offen |
| Entscheidung: gesperrter Weg fehlt oder ist markiert | **13** — bestimmt, wie `oeffne_weg()` gebaut wird | offen |
| Dictionary als Nachschlagetabelle (Kennung → Name, Mengen) | **11** — `item.name`; **22** — Rezeptmengen | offen |
| Ortsbeschreibung beim ersten Besuch länger | **6** — das Set löst das sauber | offen |
| Fehlerklasse „inkonsistente Daten" (Ausgang zeigt ins Leere) | **25** — bei externem Content die häufigste Fehlerart | offen |

### Etappe 6 — Liste, Dictionary, Set, Tuple

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| Set für besuchte Orte | **14** — `besuchte_felder`; **18** — `flags` | offen |
| Tuple für Koordinaten | **10** — `self.position`; **14** — `(x, y)` in der Mine | offen |
| Sets lassen sich nicht als JSON speichern | **19** — Design-Entscheidung beim Speichern | offen |

### Etappe 7 — Aufräumen

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| Funktionen als Bausteine | **9** — werden zu Methoden | offen |
| „Was muss immer gelten?" (Testdenken) | **26** — dieselben Fragen als `pytest` | offen |
| `berechne_schaden()` | **21** — wird zur echten Kampfformel | offen |
| Verhalten bleibt gleich nach Umbau | **27** — derselbe Beweis bei Pygame | offen |

### Etappe 9 — Alles wird zum Objekt

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `Player`-Klasse | **10** — bekommt Inventar und Ausrüstung | offen |
| Leseübungen beginnen | **23** — Code aus echten Vibe-Coding-Projekten | offen |

### Etappe 10 — Komposition

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `None` als „bewusst nichts" | **19** — wird zu `null` in JSON | offen |
| Ausrüstungs-Slots | **21** — Waffe und Rüstung im Kampf | offen |
| `self.position` als Tuple | **14** — Bewegung im Raster | offen |
| Komposition als Standardwerkzeug | **11** — Gegenprobe: brauchen wir Vererbung? | offen |

### Etappe 11 — Vererbung

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `Item` → `Weapon`/`Tool`/`Seed`/`Consumable` | **13** — `Seed` wird gepflanzt; **21** — `Weapon` im Kampf; **22** — Rezepte | offen |
| `Entity` → `Player`/`Villager`/`Monster` | **12** — `Villager.update()`; **21** — `Monster` in der Mine | offen |
| `Item` als Klasse | **23** — wird zur `dataclass` | offen |
| Die schriftliche Design-Frage | **24** — dieselbe Denkweise bei Modulen | offen |

### Etappe 12 — Der Tick ⭐

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `World.tick()` | **13** — Pflanzen; **17** — Ereignisse; **22** — Crafting | offen |
| NPC-Tagesabläufe | **17** — „wo war wer, als es passierte" | offen |
| NPC-Gedächtnis („ich hab dich gesehen") | **17** — Grundlage der Verdachtslogik | offen |
| `self.zeit` als Zähler | **19** — wird mitgespeichert; **27** — wird zur Bildrate | offen |

### Etappe 13 — Der magische Samen ⭐

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `wachstum_noetig` in Ticks | **27** — 180 Ticks = 3 Minuten bei 60 fps | offen |
| `world.oeffne_weg()` — Karte zur Laufzeit ändern | **19** — der veränderte Zustand muss mitgespeichert werden | offen |
| Halb gewachsene Pflanzen | **19** — Serialisierung mit Zwischenzustand | offen |
| Die Kopplungsfrage (Pflanze kennt Welt) | **offen und erwünscht** — dein erster echter Umweg | offen |
| Ein Samen | **22** — mehrere Sorten mit Wirkungen | offen |

### Etappe 14 — Die Mine ⭐

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| 2D-Raster als Liste von Listen | **28** — exakt das Format für Pygame-Tilemaps | offen |
| `besuchte_felder` als Set | **19** — Set → JSON ist nicht trivial | offen |
| Die Mine als Ort | **21** — hier findet Kampf statt, nicht im Dorf | offen |
| `enumerate()` (nur zum Wiedererkennen) | **23** — pythonische Schreibweisen | offen |

### Etappe 15 — Was in der Mine liegt

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| Funde setzen Flags | **17** — Funde beeinflussen, wer verschwindet | offen |
| Funde ändern Dialoge | **18** — vollständige Dialogprüfung | offen |
| Erstes „erweitern ohne zu zerstören" | **26** — Tests machen daraus eine Gewissheit | offen |

### Etappe 17 — Und dann sind es zwei ⭐

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| Ereignisliste mit Wahrscheinlichkeiten | **22** — Wachstum läuft über denselben Takt | offen |
| Fester Seed beim Testen | **26** — reproduzierbare Tests | offen |
| Ereignisse als Daten | **25** — wandern nach `content/` | offen |

### Etappe 18 — Vertrauen

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| `flags` als zentrales Set | **19** — muss serialisiert werden | offen |
| Vertrauenswerte pro NPC | **19** — Teil des Speicherstands | offen |
| Dialoge als Struktur | **25** — wandern nach `content/` | offen |

### Etappe 19–22

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **19:** JSON-Denkweise (Objekt ≠ Daten) | **25** — Content-Format beruht darauf | offen |
| **19:** `pathlib` | **25** — `content/`-Verzeichnis laden | offen |
| **21:** `Enum` für Spielzustände | **27** — Pygame braucht sie für Modi | offen |
| **21:** Erster Branch | **24** — Branches systematisch | offen |
| **22:** Rezepte als Daten | **25** — wandern nach `content/` | offen |

### Etappe 23–26

| Was angelegt wird | Wo es eingelöst wird | Status |
|---|---|---|
| **23:** Lesekompetenz für fremden Code | **das eigentliche Ziel des Projekts** | offen |
| **24:** Modulstruktur | **27** — Pygame kommt als eigenes Modul dazu | offen |
| **25:** Content in JSON | **die Prämisse löst ihre Schuld ein** — Rückkehrer ohne Code | offen |
| **26:** Tests | **27–29** — Beweis, dass Grafik die Logik nicht bricht | offen |

---

## Teil B — Was eine späte Etappe erwartet

Umgekehrte Richtung. Vor jeder dieser Etappen prüfen, ob die Voraussetzung wirklich dasteht — sonst fehlt die Pointe.

| Etappe | Erwartet aus | Was da sein muss |
|---|---|---|
| **4** (Inventar) | 1, 2, 3 | „Name zeigt auf Wert", Truthy-Liste, `range()`-Zählung ab 0, Befehlsschleife |
| **5** (Karte) | 3, 4 | `.split()` für `gehe norden`, Gegenstände pro Ort |
| **10** (Komposition) | **4** | Mutable vs. immutable — sonst ist das geteilte Inventory unerklärlich |
| **11** (Vererbung) | 4 | Kennung ↔ Anzeigename wird zu `item.id` / `item.name` |
| **12** (Tick) | 1, 2, 3, 4, 6, 9, 11 | Weltzustand in Variablen, **die Hauptschleife**, „nicht iterierend entfernen", drei NPCs als `Villager`-Objekte |
| **6** (Datenstrukturen) | 4, 5 | Mutable/immutable, `in` beim Dictionary, besuchte Orte als Problem |
| **13** (Samen) | 5, 11, 12 | `orte`-Dictionary veränderbar, **Entscheidung zu gesperrten Wegen**, `Seed`-Klasse, laufender Tick |
| **14** (Mine) | 3, 4, 6, 10 | `range()`, verschachtelte Listen, Set, Tuple-Position |
| **17** (Verschwinden) | **1**, 2, 12, 15 | **`geruch` und die Sinnesvariablen vom ersten Morgen**, `vertrauen`, NPC-Gedächtnis, Minenfunde |
| **18** (Vertrauen) | 2, 6, 15 | `vertrauen`, Set-Verständnis, Flags aus Funden |
| **19** (Speichern) | 6, 10, 12, 13 | Sets, `None`, `self.zeit`, halb gewachsene Pflanzen |
| **20** (Fehlerbehandlung) | 2, 3, 4 | `else`-Zweige, Eingabe-Wiederholung, Inventar-Obergrenze |
| **21** (Kampf) | 7, 10, 11, 14 | `berechne_schaden()`, Slots, `Weapon`/`Monster`, die Mine |
| **25** (Content) | 5, 11, 17, 18, 22 | Alle Inhalte müssen sauber von der Logik getrennt sein |
| **26** (Tests) | 7, 15, 19, 22 | Die „was muss immer gelten"-Fragen von Etappe 7 |
| **27** (Pygame) | 3, 12, 13, 24 | Loop, Tick, `wachstum_noetig = 180`, Modulstruktur |
| **28** (Tilemap) | 14 | Das Raster im unveränderten Format |

**Die kritischste Zeile ist Etappe 17.** Sie ist der einzige Punkt, an dem etwas aus Etappe 1 direkt eingelöst wird — über vier Monate hinweg. Wenn du dort ankommst und die Rückblende nicht schreibst, war der ganze erste Tag umsonst begründet.

---

## Teil C — Durchgehende Fäden

Kein einzelner Verweis, sondern etwas, das über den ganzen Plan läuft.

**Erweitern ohne zu zerstören** — Etappe 7 (erstes Refactoring) → 15 (vierter Fund ohne Dialogänderung) → 19 (Pflanzen mitspeichern) → 22 (Rezept ohne Logikänderung) → 26 (Tests machen daraus Gewissheit).

**Die Bug-Jagd** — Etappe 8 (erste Runde) → 16 (subtilere Fehler) → 26 (umgekehrt: erst Test, dann Fix). Dazwischen unregelmäßig und unangekündigt.

**Die drei Fehlertypen** — eingeführt im Lehrplan, benannt in Etappe 1 (fehlendes `f`), Etappe 2 (falsche Einrückung), Etappe 20 (`except:` verwandelt Typ 1 in Typ 3), Etappe 21 (`"kamfp"` gegen `GameState.KAMFP`).

**Git** — Etappe 0 (Minimalset) → 21 (erster Branch mit echtem Zweck) → 24 (Branches, Merges, Konflikte).

**Schreiben → Lesen** — Etappe 9 (erste Leseübung) → alle Etappen ab dort → 23 (Code aus echten Vibe-Coding-Projekten). Das ist der eigentliche Zweck des Projekts.

**Die Prämisse** — Etappe 2 (drei NPCs sind überschaubar) → 12 (Leere macht Bewegung sichtbar) → 17 (einer von dreien verschwindet) → 18 (Kombinatorik bleibt beherrschbar) → 25 (Rückkehrer als JSON, ohne Code).

---

## Teil D — Pflege

**Wenn ein Verweis eingelöst ist:** Status auf `eingelöst` setzen und das Datum dazuschreiben. Die Liste der offenen Posten ist damit immer aktuell.

**Wenn du von der Vorgabe abweichst:** Eintrag anpassen, nicht löschen. Wenn du in Etappe 6 doch keine Sets nimmst, muss Etappe 14 und 18 das wissen. Eine Zeile hier erspart dir eine Stunde Verwirrung dort.

**Wenn ein Umweg entsteht:** Eintragen. Der Kopplungs-Umweg bei Etappe 13 steht bereits drin. Weitere kommen — ab Etappe 17 ist das der Normalfall und nicht die Ausnahme.

**Wenn du mit mir arbeitest:** Verweis mich bei jeder Etappe ab 12 auf diese Datei. Nicht aus Misstrauen — ich habe über Monate kein verlässliches Gedächtnis, und eine plausible Rekonstruktion ist schlimmer als ein Nachschlagen.
