# Advanced — Vom Spiel zum System

**Ein Aufbaukurs in 10 Etappen. Dein Dorf hört auf, auf dich zu warten.**

> **Voraussetzung: Etappe 27 des Haupttutorials.** Nicht Etappe 20, nicht „ich hab das meiste". Dieser Kurs setzt Klassen, Module, Tests, Fehlerbehandlung und die Debugging-Methodik als selbstverständlich voraus — und er wird an Stellen unangenehm, an denen dir das Fundament fehlen würde.

---

## Was das hier ist

Dein Spiel ist ein **einzelner Ablauf, der auf `input()` wartet**. Es passiert immer genau eine Sache zur Zeit. Wenn nichts eingegeben wird, passiert nichts. Das Programm gehört dir allein, und wenn es abstürzt, ist niemand außer dir betroffen.

Die meiste Software, die dich umgibt, ist anders gebaut:

- Es laufen **mehrere Dinge gleichzeitig** — etwas wird angezeigt, während im Hintergrund gerechnet wird.
- Es gibt **fremde Prozesse**, die man startet, überwacht und wieder beendet.
- Es gibt **Ressourcen, um die gestritten wird** — Dinge, die nur einer gleichzeitig benutzen kann.
- Es gibt **Datenströme** statt fertiger Ergebnisse — Antworten kommen stückweise.
- Es gibt **ein Netzwerk**, und über ein Netzwerk kann alles langsam sein, scheitern oder schweigen.
- Es gibt **austauschbare Teile** hinter einer gemeinsamen Schnittstelle.
- Und es gibt **Dinge, die beim Testen nicht da sind**.

Nichts davon lernt man an einem Textadventure, das brav wartet. **Deshalb hört dein Dorf in diesem Kurs auf zu warten.**

---

## Das Vehikel: dasselbe Dorf

Kein neues Projekt. Du baust dein bestehendes Spiel um — und jede Etappe erzeugt das Problem, das die nächste löst.

**Am Ende dieses Kurses ist dein Spiel:**

- Eine Welt, deren Zeit **wirklich** vergeht. Der magische Samen aus Etappe 13 wächst in drei echten Minuten, nicht in 180 Befehlen. Wer zu lange über einer Entscheidung brütet, kommt zu spät.
- Ein Programm, das ein **zweites Programm startet und überwacht** — ein Sprachmodell, das den drei Überlebenden Antworten gibt, die niemand vorgeschrieben hat.
- Ein System mit **austauschbaren Teilen**: Dialoge aus einer JSON-Datei oder aus dem Modell, dieselbe Schnittstelle, ein Schalter in der Konfiguration.
- Und etwas, das man **testen kann, ohne dass das Modell läuft**.

Das ist strukturell dieselbe Art von Programm wie ein Sprachassistent, ein Spieleserver oder eine Robotersteuerung. Nur dass du es an etwas lernst, das du bereits verstehst.

---

## Ehrliche Einschränkungen

Zwei Dinge vorweg, damit du weißt, worauf du dich einlässt.

**Das hier ist nicht mehr didaktisch geglättet.** Im Haupttutorial hat jede Etappe genau das Werkzeug bekommen, das sie brauchte, in genau der richtigen Reihenfolge. Hier greifen die Themen ineinander, es gibt Rückgriffe und Vorgriffe, und manches lernst du erst richtig, wenn du es zum zweiten Mal brauchst. So sieht echtes Lernen an einem echten System aus.

**Nicht alles lässt sich am Dorf zeigen.** Zwei Themen aus der Systemwelt passen schlecht oder gar nicht:

| Thema | Passt es? |
|---|---|
| **numpy** — Zahlenfelder, Vektorrechnung | Nur mit Mühe. Es gibt einen Weg (Wegfindung in der Mine), aber er ist konstruiert. Als **A10** markiert und ausdrücklich optional. |
| **Hardwaresteuerung** — Roboter, Sensoren, Motoren | Gar nicht. Das braucht ein eigenes Vehikel. Was du hier lernst — Nebenläufigkeit, Prozessgrenzen, Fehlertoleranz, austauschbare Teile — ist die Hälfte davon; die andere Hälfte lernt man nur an echter Hardware. |

Ich sage das lieber deutlich, als dir ein Dorf zu bauen, das so tut, als wäre es ein Roboter.

---

## Der neue Fehlertyp

Im Haupttutorial hast du drei Sorten Fehler kennengelernt: sofortiger Absturz, gelegentlicher Absturz, und die schlimmste — läuft durch, liefert das Falsche.

**Ab Etappe A1 kommt ein vierter dazu:**

> **Typ 4: Der Fehler tritt nur manchmal auf, hängt vom Zeitverhalten ab, und verschwindet, sobald du ein `print()` einbaust.**

Das ist eine **Race Condition**, und sie ist unangenehmer als alles bisher — weil deine bewährten Werkzeuge sie stören. Ein Breakpoint hält einen Programmfaden an und verändert genau das, was du untersuchen willst.

Deshalb dreht sich hier die Reihenfolge um: **erst denken, dann messen.** Und deshalb ist Logging (A2) in diesem Kurs keine Kür, sondern die Voraussetzung dafür, überhaupt etwas zu sehen.

---

## Die Etappen

### A1 — Der Tick löst sich vom Spieler ⭐⭐

**Threads, `queue.Queue`, `threading.Lock`, `threading.Event`**

Die zentrale Etappe. Bisher rief dein Spiel `world.tick()` bei jedem Befehl. Jetzt bekommt die Welt einen eigenen Programmfaden, der unabhängig weiterläuft.

```python
def welt_schleife(world, stopp: threading.Event):
    while not stopp.is_set():
        world.tick()
        time.sleep(1.0)          # ein Tick pro Sekunde
```

Und damit hast du dir sofort ein Problem gebaut: **Zwei Fäden fassen dieselben Daten an.** Der Spieler hebt einen Gegenstand auf, während der Tick die Ortsliste durchläuft. Das ist die Race Condition, und du wirst sie erleben.

- **`Lock`** schützt den Weltzustand — nur einer darf gleichzeitig hinein.
- **`Queue`** übergibt Ereignisse vom Tick-Faden an die Anzeige, ohne dass sich beide ins Gehege kommen.
- **`Event`** ist das Signal „bitte aufhören" von außen.

**Was dein Spiel dadurch gewinnt:** Zeitdruck. Der Verschwundene aus Etappe 17 verschwindet jetzt, während du überlegst.

**Was du über den GIL wissen musst, kurz und ehrlich:** Python führt in einem Prozess immer nur ein Stück Python-Code gleichzeitig aus. Threads helfen dir deshalb **beim Warten** — auf Eingaben, auf Dateien, auf das Netz. Sie helfen dir **nicht**, Rechenarbeit zu beschleunigen. Faustregel: *Warten → Threads. Rechnen → eigener Prozess.*

**Transferaufgabe:** Zwei Threads erhöhen dieselbe Zählvariable eine Million Mal. Erwartet: 2.000.000. Lass es fünfmal laufen. **Wenn dich das Ergebnis nicht kurz erschreckt, hast du es nicht verstanden.** Dann setz ein `Lock` darum.

**Kaputtmachen:** Ersetz die Queue durch eine gemeinsame Liste. Vergiss `daemon=True` und versuch, mit Strg+C zu beenden. Lass beim Erzeuger das Schlusszeichen weg.

---

### A2 — Sehen, was passiert: Logging und Konfiguration

**`logging`, `tomllib`, Umgebungsvariablen**

A1 hat dein wichtigstes Werkzeug zerstört. `print()` aus zwei Fäden erzeugt ineinandergeschobene Zeilen, und du weißt nicht mehr, wer was gesagt hat.

```python
import logging
log = logging.getLogger(__name__)

log.debug("Tick %d: %s bewegt sich nach %s", self.zeit, npc.name, ziel)
log.warning("Tick brauchte %.2fs — zu lang", dauer)
log.exception("Ereignis fehlgeschlagen")     # inklusive Traceback
```

Der Unterschied zu `print`: Stufen, Herkunft, Zeitstempel, **Fadenname** — und die Möglichkeit, alles in eine Datei zu schreiben, ohne eine Zeile Code zu ändern. Bei einem nebenläufigen System ist ein Log kein Komfort, sondern das einzige Fenster nach innen.

**Konfiguration:** Alles, was du zum Ausprobieren ständig änderst — Tickdauer, Wachstumszeiten, Ereigniswahrscheinlichkeiten — gehört in eine `config.toml`, nicht in den Code. `tomllib` ist seit Python 3.11 in der Standardbibliothek.

**Warum das hier steht und nicht später:** Ohne Logging bist du in A3 bis A8 blind.

---

### A3 — Sauber besitzen und sauber beenden

**Eigene Kontextmanager, `__enter__`/`__exit__`, `KeyboardInterrupt`**

Seit A1 besitzt dein Programm etwas, das nicht Speicher ist: einen laufenden Faden. Und damit wird das Beenden zur eigenen Aufgabe.

Zwei Probleme, die du jetzt hast:

**Die Pause.** Während der Spieler in einem Dialog steckt, soll die Welt stillstehen. Das ist ein eigener Kontextmanager:

```python
with world.pausiert():
    fuehre_dialog(npc)
# hier läuft die Zeit wieder
```

**Das Ende.** Was passiert bei Strg+C? Ein `KeyboardInterrupt` — eine ganz normale Exception. Dein Spiel soll darauf den Tick-Faden stoppen, den Spielstand sichern und sich verabschieden. Nicht einen Traceback ausspucken und einen laufenden Faden zurücklassen.

Dazu: **Zeit richtig messen.** `time.time()` ist die Uhrzeit und kann springen. Für Dauern und Takte nimmt man `time.monotonic()`, eine Uhr, die nur vorwärts läuft.

**Kaputtmachen:** Gib in `__exit__` `True` zurück und beobachte, dass Fehler spurlos verschwinden — der bequemste Weg, sich einen Typ-3-Fehler einzubauen.

---

### A4 — Ströme statt Ergebnisse

**Generatoren, `yield`, das Iterator-Protokoll**

Dein Tick erzeugt Ereignisse. Bisher sammelst du sie in einer Liste und gibst sie am Ende aus. Aber eine Welt, die läuft, hat kein Ende.

```python
def ereignisse(self):
    while True:
        for e in self.tick():
            yield e              # kein return: das hier ist ein Generator
```

**Der Unterschied, auf den alles ankommt:** Eine Funktion mit `return` rechnet fertig und gibt dir das Ergebnis. Eine Funktion mit `yield` gibt dir eine **Bezugsquelle**. Der Code läuft erst, wenn du das nächste Stück abholst, und pausiert danach mitten in der Funktion — mit allen lokalen Variablen an Ort und Stelle.

Zweiter Einsatz im Spiel: Text, der sich aufbaut. Eine lange Ortsbeschreibung, die satzweise erscheint, statt auf einmal.

**Der wichtigste Fallstrick:** Einen Generator kann man **nur einmal** durchlaufen. Beim zweiten `for` ist er leer — ohne Fehlermeldung. Ein lupenreiner Typ-3-Fehler.

---

### A5 — Austauschbare Teile ⭐

**Duck Typing, `ABC`, `Protocol`, Abhängigkeiten hineinreichen**

Deine Dialoge kommen aus JSON-Dateien (Etappe 25). Gleich sollen sie wahlweise aus einem Sprachmodell kommen. Der Rest des Spiels darf davon nichts wissen.

```python
from abc import ABC, abstractmethod

class Dialogquelle(ABC):
    @abstractmethod
    def antwort(self, npc: str, frage: str) -> str: ...

class AusDatei(Dialogquelle): ...
class AusModell(Dialogquelle): ...
```

**Drei Ebenen, in aufsteigender Formalität:** Duck Typing (es reicht, dass die Methode da ist), `ABC` mit `@abstractmethod` (Vererbung erzwingt die Umsetzung), `Protocol` (beschreibt eine Schnittstelle, ohne dass geerbt werden muss).

**Und hier bekommst du endlich die Antwort auf die Frage aus Etappe 13.** Damals hast du gefragt, warum die Pflanze die ganze Welt kennen muss. Antwort: Sie muss nicht. Sie braucht ein Objekt, das `oeffne_weg` kann. Wer ihr das gibt, entscheidet die aufrufende Stelle. Das heißt **Dependency Injection** — ein einschüchternder Name für *„gib dem Objekt seine Werkzeuge von außen, statt dass es sie sich selbst besorgt"*.

Der Gewinn ist nicht Eleganz, sondern Testbarkeit. Wovon A6 handelt.

**Erweitern ohne zu zerstören — die Prüfung dieser Etappe:** Füge eine dritte Dialogquelle hinzu und ändere dabei **keine Zeile** im übrigen Spiel.

---

### A6 — Testen, wenn das Echte nicht da ist

**Fakes, Mocks, `monkeypatch`, testbare Zeit und testbarer Zufall**

Du kannst dein Spiel nicht testen, indem bei jedem Test ein Sprachmodell antwortet. Und du kannst einen Tick-Faden nicht testen, indem du zwei Sekunden wartest.

**Zwei Werkzeuge, und der Unterschied ist wichtiger, als er aussieht:**

- **Fake** — eine echte, einfache Umsetzung deiner Schnittstelle aus A5. `FakeDialog` gibt immer denselben Satz zurück. Sauber, lesbar, dein Standardwerkzeug.
- **Mock** — ein Aufzeichnungsobjekt, das prüft, *ob und wie* etwas aufgerufen wurde. Für Fragen wie: *Wurde der Tick-Faden wirklich gestoppt, als der Spieler beendet hat?*

**Und hier zahlt A5 zurück:** Wenn deine Welt ihre Dialogquelle übergeben bekommt, ist der Test drei Zeilen. Wenn sie sie selbst erzeugt, brauchst du Mock-Trickserei. **Schwer testbarer Code ist fast immer ein Hinweis auf zu enge Kopplung** — der Test ist die Rückmeldung, nicht das Problem.

Dazu: Zufall testbar machen (fester Seed — die Zusage aus Etappe 17), Zeit testbar machen (die Uhr als Abhängigkeit statt `time.monotonic()` mitten im Code), und wie man nebenläufigen Code testet, ohne dass er mal durchläuft und mal nicht.

---

### A7 — Ein zweites Programm starten ⭐

**`subprocess`, Prozessgrenzen, Lebenszyklus, Health-Check**

Jetzt wird es ernst: Dein Spiel startet ein Sprachmodell als eigenes Programm, wartet, bis es bereit ist, benutzt es und beendet es wieder.

```python
proc = subprocess.Popen(
    [sys.executable, "modell_server.py", "--port", "8080"],
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True,
)
```

**Fang mit einer Attrappe an.** Schreib erst ein zweites Python-Skript, das ein paar Sekunden schläft und dann festen Text zurückgibt. Erst wenn der ganze Ablauf steht — starten, warten, benutzen, beenden —, tauschst du es gegen ein echtes Modell. Sonst rätst du bei jedem Fehler, ob es an dir, am Modell oder am Speicher lag.

**Die Themen:**
- `run()` (starten und warten) gegen `Popen()` (starten und weiterarbeiten)
- Warum `shell=True` fast immer die falsche Antwort ist
- **Der Klassiker: Wenn du die Ausgabe des Kindprozesses nicht abholst, blockiert er irgendwann.** Ein eigener Thread liest mit und schreibt ins Log — dein Wissen aus A1 und A2 zusammen.
- Warten, bis der Dienst wirklich bereit ist: **nicht `sleep(10)`**, sondern in einer Schleife nachfragen, mit Zeitlimit. Das heißt Health-Check.
- Beenden in drei Stufen: höflich (`terminate`), warten, notfalls hart (`kill`)

**Die eigentliche Erkenntnis:** Das ist die härteste Grenze in deinem System. Innerhalb eines Prozesses teilst du Objekte. Über eine Prozessgrenze passt nur, worauf sich beide Seiten geeinigt haben — Text, Bytes, JSON. Derselbe Gedanke wie in Etappe 19, aber diesmal spürst du ihn.

**Kaputtmachen:** Beende dein Spiel, ohne den Subprozess zu stoppen. Schau mit `ps` nach, was noch läuft. Starte dann neu und lies „Adresse bereits belegt". Diesen Ablauf wirst du wiedererkennen.

---

### A8 — Über das Netz reden

**`requests` / `httpx`, Statuscodes, Zeitlimits, Wiederholungen**

Dein Spiel redet mit seinem Modellserver über HTTP.

```python
antwort = requests.post(
    "http://127.0.0.1:8080/dialog",
    json={"npc": "versorgerin", "frage": frage},
    timeout=30,          # NIEMALS weglassen
)
antwort.raise_for_status()
```

**Die Themen:** Statuscodes in Gruppen (2xx gut, 4xx *du* hast Mist gebaut, 5xx *die andere Seite*). `timeout` — die eine Zeile, deren Fehlen ein Programm für immer hängen lässt. Wiederholungen mit wachsender Wartezeit, und wann Wiederholen falsch ist. `localhost` gegen `0.0.0.0` und warum dein Dorf-Dashboard vom Handy aus nicht erreichbar ist, wenn du das verwechselst.

**Die Denkgewohnheit, die hier entsteht:** Bei jeder Zeile, die eine Prozess- oder Netzgrenze überquert, fragst du: *Was, wenn das dreißig Sekunden dauert? Was, wenn nie eine Antwort kommt? Was, wenn Unsinn zurückkommt?* Bei einem lokalen Funktionsaufruf ist diese Frage unnötig. Hier ist sie Pflicht.

**Und die Anwendung, die Spaß macht:** Ein kleines Dashboard im Browser, das zeigt, wo die drei Überlebenden gerade sind und wie viel Zeit vergangen ist. Zwanzig Zeilen mit Flask oder Gradio.

---

### A9 — `async` und `await`

*Optional. Ehrlich gesagt der schwächste Fit dieses Kurses — aber du wirst es lesen müssen.*

Threads sind nicht der einzige Weg. Viele moderne Bibliotheken arbeiten mit `async`, und wenn du in A8 ein Dashboard gebaut hast, bist du ihm schon begegnet.

**Das Modell in einem Satz:** Ein einzelner Faden springt zwischen vielen Aufgaben hin und her — aber **nur an den Stellen, die mit `await` markiert sind.**

Daraus folgt die wichtigste praktische Regel: Eine langsame, nicht-async Operation in einer async-Funktion legt alles lahm. `time.sleep(5)` in einer Coroutine blockiert das ganze Programm, `await asyncio.sleep(5)` nicht. Genau daran scheitern die meisten Oberflächen, die beim Arbeiten einfrieren.

| Situation | Werkzeug |
|---|---|
| Die Bibliothek erwartet es | `async` |
| Blockierende Aufrufe, die du nicht ändern kannst | Thread |
| Reine Rechenlast in Python | eigener Prozess |
| Deine eigene Wahl | Threads sind meist einfacher zu debuggen |

**Für dein Dorf brauchst du es nicht.** Aber `asyncio.to_thread(blockierende_funktion, arg)` solltest du gesehen haben — die Brücke zwischen beiden Welten steht in echten Projekten überall.

---

### A10 — numpy

*Optional, und der einzige konstruierte Teil dieses Kurses.*

Ich habe lange überlegt, ob das hier hineingehört. Ein Textadventure braucht keine Vektorrechnung, und ich will dir kein Thema andrehen, indem ich einen Anlass erfinde.

**Es gibt genau einen ehrlichen Anlass:** Wenn deine Mine aus Etappe 14 groß wird und NPCs sich darin bewegen sollen, brauchst du Wegfindung. Eine Distanzkarte über ein Raster ist genau die Sorte Rechnung, für die numpy gebaut ist — Rechnen auf ganzen Feldern statt in Schleifen.

```python
import numpy as np

raster = np.array(karte)        # dein Minenraster aus Etappe 14
begehbar = raster != "#"        # eine Zeile, kein for
```

**Die Themen, falls du es machst:** `shape` und `dtype` — die zwei Fragen, die du bei jedem Array zuerst stellst. Vektorisierung: Rechnen ohne `for`, und warum das nicht nur kürzer, sondern hundertfach schneller ist. Und **Views gegen Kopien** — ein Slice teilt sich oft den Speicher mit dem Original. Wenn dir das bekannt vorkommt: Es ist Etappe 4, nur schärfer.

**Wenn dich Wegfindung nicht reizt, lass die Etappe aus.** Sie ist der einzige Teil dieses Kurses, dessen Anlass ich mir zusammensuchen musste.

---

## Was danach kommt

Nach A8 ist dein Dorf strukturell dieselbe Art von Programm wie ein Sprachassistent, ein Spieleserver oder eine Gerätesteuerung: nebenläufig, mit einem fremden Prozess, einer Netzschnittstelle, austauschbaren Teilen und einem Log, das erklärt, was passiert ist.

**Was dann noch fehlt, lernt man nur an echter Hardware:** Geräte, die nicht antworten. Latenz, die man hört. Bewegungen, die man glätten muss. Ein Not-Aus, der wirklich funktionieren muss. Dafür braucht es ein anderes Vehikel als ein Dorf — aber nicht mehr diese Grundlagen.

---

## Arbeitsweise

**Dieselbe wie im Haupttutorial.** `MENTOR.md` gilt unverändert: kein fertiger Code, Hinweis-Leiter, Lernziele werden abgefragt, die Bug-Jagd läuft weiter — und zwar mit einem Fehlertyp mehr.

**Zwei Dinge ändern sich:**

**Die Etappen sind größer.** Rechne mit sechs bis zehn Sitzungen statt vier bis sechs. A1 allein kann zwei Wochen dauern, und das ist in Ordnung.

**Der Bogen läuft weiter.** Auch hier gilt: Vorausverweise gehören in `BOGEN.md`, nicht ins Gedächtnis. Trag sie mit dem Präfix `A` ein, damit die Nummern sich nicht mit dem Haupttutorial beißen.

**Und arbeite auf einem Branch.** A1 verändert die Grundstruktur deines Spiels. Wenn es schiefgeht, willst du zu einem Dorf zurückkehren können, das funktioniert.

---

## Warum das Dorf und kein neues Projekt

Man könnte für diesen Kurs ein frisches, kleines Projekt anlegen — sauberer, weniger Altlasten, schnellere Fortschritte.

**Es wäre trotzdem schlechter.** Der Wert dieses Kurses entsteht daraus, dass du ein System umbaust, das du bereits vollständig verstehst. Wenn in A1 die Race Condition zuschlägt, weißt du genau, welche Datenstruktur betroffen ist und warum — weil du sie geschrieben hast. In einem fremden Beispielprojekt wäre es nur eine weitere unverständliche Fehlermeldung.

Das ist derselbe Grund, aus dem das Haupttutorial ein Spiel baut statt Übungsaufgaben zu lösen: **Man lernt Architektur nur an einem System, das einem etwas bedeutet.**
