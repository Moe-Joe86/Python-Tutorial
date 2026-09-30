# Etappe 12 — Der Tick

*v1.1.2 · 2026-09-16*

> **Block 2: Einheiten und Zeit** · Etappe 12 von 30 · [← Etappe 11](etappe-11-vererbung.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 13 →](etappe-13-bauzeit-und-abklingzeit.md)

**Neue Syntax heute:** `self` als Argument weitergeben (`einheit.update(self)`) · ein Methodenkörper, der nur aus einem Docstring besteht · Status als String am Objekt · `return` ohne Wert · Sammeln und danach entfernen · 👀 `pass` · 👀 der Begriff *Zustandsautomat* · 👀 der Begriff *Kopplung*

⚠️ **Diese Liste ist kurz, und das ist kein Versehen.** Etappe 12 bringt fast keine neue Sprache. Sie bringt eine neue **Bauform**, gebaut aus Werkzeugen, die du seit Etappe 3 hast. Das ist der Grund, warum sie im Lehrplan einen Stern trägt: Ab hier hängt alles Weitere daran.

**Zeitaufwand:** 12a: 3–4 Sitzungen · 12b: 4–5 Sitzungen, à 20–30 Minuten. Rund 45 Minuten davon sind Lesestoff, gut zwanzig je Portion — lies jeweils nur die, an der du sitzt. **Rechne damit, dass allein Auftragsschritt 13 einen halben Abend kostet**; das ist die Stelle, an der dein Spiel zum ersten Mal von selbst etwas tut.

**Voraussetzung:** Etappe 11 abgeschlossen, Selbsttest grün. Vier Marines stehen nebeneinander, deine Gegner sind Objekte, `Einheit` ist die gemeinsame Basis. Ohne diese drei geht heute nichts.

**Die zwei Portionen:**

| | Was passiert | Was danach anders ist |
|---|---|---|
| **12a** | Alles Lose bekommt einen Besitzer: die `Welt` | Deine Funktionen werden kürzer, dein Spiel verhält sich identisch |
| **12b** | Die Welt tickt, und drei Kameraden fangen an zu handeln | Zeit vergeht auch, wenn du nichts tust |

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **12a** | `Welt` als Objekt · loser Zustand zieht um · `self.held` neben `self.trupp` | Pro Figur gegen pro Spiel — die Antwort aus Etappe 9 auf dem Prüfstand | Kopplung: warum kurze Parameterlisten einen Preis haben |
| **12b** | `tick()` · `update()` an jeder Einheit · `return` ohne Wert · Trupp-KI Stufe 1 · sammeln und danach entfernen | Gesteuert gegen autonom · warum die Reihenfolge im Tick zählt | `pass` · Zustandsautomat · die Tick-Reihenfolge als Entscheidung |

---

## Worum es geht

Dein Spiel hat seit Etappe 3 eine Schleife. Aber es hat keine **Zeit**.

Zwischen zwei Eingaben passiert bei dir nichts. Du tippst `feuern`, ein Gegner verliert Trefferpunkte, du tippst `status`, du tippst wieder `feuern`. Die Welt steht still und wartet auf dich, unendlich lange. Du könntest aufstehen, Kaffee kochen, zurückkommen — der Kriecher steht auf demselben Feld.

> **Heute hört das auf. Ab heute kostet dich jede Handlung eine Einheit Zeit, und in dieser Zeit tun alle anderen etwas.**

*(Handlung, nicht Eingabe. Die Unterscheidung stammt aus Etappe 3b — Auskunft kostet nichts —, und sie wird in Konzept 14 fällig.)*

Das ist der Motor, den dieses Spiel braucht und den ein rundenbasiertes Rätselspiel nicht bräuchte. Ohne ihn rücken keine Gegner vor, laufen keine Abklingzeiten ab (Etappe 13), baut sich kein Geschütz auf, kommt kein Nachschub. **Alles, was die Etappen 13 bis 22 dazubauen, hängt sich an genau eine Methode, die du heute schreibst.**

Und der Tick braucht einen Ort, an dem er wohnt. Den gibt es noch nicht.

**Sieh dir dazu die Kopfzeile einer deiner Funktionen aus Etappe 7 an.** Bei dir steht dort vermutlich etwas in dieser Größenordnung:

```python
def verarbeite_befehl(befehl, marine, gegner, kern_integritaet, welle, sektoren, runde):
```

Sieben Parameter. Etappe 7, Konzept 7 hat dir gesagt, dass das ein Signal ist. Du hast es trotzdem so gebaut, und das war richtig — sichtbar und unbequem ist besser als bequem und unsichtbar. **Heute kommt die Auflösung, auf die du seit fünf Etappen wartest.**

Denn was da in der Klammer steht, ist gar keine Ansammlung von sieben Dingen. Es ist **ein** Ding, das noch keinen Namen hat:

> **Alles, was pro Spiel genau einmal existiert, gehört zusammen. Das zusammen ist die Welt.**

---

## Der lange Bogen — was heute fällig wird

Diese Etappe zahlt mehr zurück als jede andere im Block. Sechs Schulden auf einmal:

- **Die Design-Entscheidung aus Etappe 9** — *gäbe es diesen Wert pro Figur oder pro Spiel?* — wird heute geprüft. Du hast damals eine Antwort in `GELERNT.md` geschrieben. **Hol sie heraus, bevor du anfängst.** Wenn sie trug, ist 12a ein ruhiger Abend. Wenn nicht, merkst du es heute — und das ist der günstigste Zeitpunkt dafür.
- **`kern_integritaet` bekommt ihr Zuhause.** Seit Etappe 1 liegt sie lose herum, seit Etappe 5 ist der Kern zusätzlich ein Ort auf der Karte. Beides bleibt: Die Zahl gehört der Welt, der Sektor gehört der Karte.
- **Der Rundenzähler aus Etappe 3b wird zu `self.zeit`** — und damit zum ersten Mal ein Wert, den andere Teile des Spiels lesen.
- **„Eine Liste nicht verändern, während man über sie läuft"** aus Etappe 4 war ein Übungsfall mit einer Anmarschbahn. Heute ist es dein Spiel, und der Fehler überspringt Gegner, die dich gerade angreifen.
- **Die Frage aus Etappe 3b** — *welcher Befehl kostet eine Runde?* — kommt in ihrer erwachsenen Form zurück: **Welche Spieleraktion löst einen Tick aus?** Damals ein `if`, heute eine Entscheidung mit Folgen.
- **Die `Einheit`-Basisklasse aus Etappe 11** zeigt heute, wozu sie da war. Eine Schleife, ein Aufruf, und jedes Objekt tut das Seine — Marines, Gegner, ab Etappe 13 auch der Basisturm.

---

## Eine Design-Entscheidung, die du jetzt treffen musst

### Eine Einheitenliste oder zwei? ⭐

Der Tick soll über alles laufen, was handelt. Es liegt nahe, dafür **eine** Liste zu bauen — `einheiten` — und Marines wie Gegner hineinzulegen. Eine Schleife, fertig.

**Das hat einen Preis, und der fällt an einer Stelle an, an der du ihn nicht erwartest.**

| | Eine Liste `einheiten` | Zwei Listen `trupp` und `gegner` |
|---|---|---|
| Der Tick | eine Schleife | zwei Schleifen |
| Die Anmarschbahn zeichnen | braucht eine Abfrage, **was** ein Eintrag ist | läuft unverändert weiter |
| Ein Ziel für den Trupp suchen | dieselbe Abfrage nochmal | unverändert |
| Reihenfolge Trupp ↔ Gegner | ergibt sich aus der Einfügereihenfolge, unsichtbar | **steht sichtbar im Tick** |

**Der Plan legt sich auf zwei Listen fest**, und zwar aus einem Grund, der direkt aus der letzten Etappe kommt:

> **Eine Liste, die alles enthält, zwingt dich an jeder zweiten Stelle wieder zu der Frage, die Etappe 11 gerade abgeschafft hat: *Was bist du eigentlich?***

Deine Anmarschbahn braucht Gegner mit einer Entfernung. Deine Marines haben keine Entfernung — sie stehen im Vorposten. Mit einer gemeinsamen Liste müsstest du beim Zeichnen aussortieren, und aussortieren heißt fragen.

**Die zweite Zeile von unten ist der eigentliche Gewinn.** Mit zwei Schleifen im Tick steht schwarz auf weiß in deinem Code, wer zuerst dran ist. Das brauchst du heute noch nicht — aber in Etappe 16 suchst du einen Fehler, dessen ganze Ursache genau diese Reihenfolge ist.

⚠️ **Was das *nicht* heißt:** Die beiden Listen sind keine parallelen Sammlungen wie `gegner` und `gegner_typen` aus Etappe 6. Die mussten gleich lang bleiben und über den Index zusammenpassen. Diese hier haben nichts miteinander zu tun — sie enthalten verschiedene Dinge, in verschiedener Anzahl. **Zwei Listen sind nur dann ein Fehler, wenn sie sich einen Index teilen.**

*(Der Basisturm aus Etappe 13 kommt in den `trupp`. Er ist kein Marine, aber er steht auf deiner Seite und tickt wie alle anderen — das ist der Punkt an der `Einheit`-Basis.)*

**Schreib deine Entscheidung in `GELERNT.md`**, auch wenn du dem Plan folgst. In Etappe 22 kommt die Frage zurück.

---

# Teil 12a — Die Welt bekommt ein Zuhause

## Vor dem Umbau: drei Fragen ⭐

| Frage | Antwort |
|---|---|
| **Was bleibt gleich?** | Jede Zahl, jede Meldung, jedes Verhalten. Der Spieler merkt nichts. |
| **Was ändert sich nur in der Darstellung?** | Nichts. |
| **Was ändert sich wirklich am Datenmodell?** | Nichts wird neu erfunden. Werte, die nebeneinander lagen, bekommen einen gemeinsamen Besitzer. |

**Das ist der vierte reine Umbau des Plans**, nach 7, 9 und 10. Also gilt wieder: `befehle.txt`, `diff`, und jede Abweichung ist ein Fehler.

⚠️ **Und heute ist der Beweis wichtiger als je zuvor.** Du fasst in 12a fast jede Zeile deines Spiels an. Das ist genau die Sorte Umbau, bei der man am Ende nicht mehr weiß, ob eine Zahl schon vorher falsch war.

---

## Die Konzepte — Teil 12a

Alle Beispiele laufen **außerhalb** deines Spiels. Heute in einem Hafen.

### 1. Die Welt ist ein Objekt wie jedes andere ⭐

Technisch ist daran nichts Neues. Es ist eine Klasse aus Etappe 9, die Objekte enthält wie in Etappe 10:

```python
class Hafen:
    def __init__(self):
        self.tag = 0
        self.wetter = "klar"
        self.liegeplaetze = 12
        self.schiffe = []
        self.kran_defekt = False
```

Kein neues Schlüsselwort, keine neue Schreibweise. **Was neu ist, ist die Frage, nach der du entscheidest, was hineingehört** — und die kennst du seit Etappe 9:

> **Gäbe es diesen Wert pro Figur oder pro Spiel?**

Ein Schiff hat einen eigenen Tiefgang, einen eigenen Namen, eine eigene Ladung. Den **Tag** gibt es einmal. Das **Wetter** gibt es einmal. Die Zahl der **Liegeplätze** gibt es einmal. Alles, was es einmal gibt, wohnt im Hafen.

**Die Gegenprobe ist genauso wichtig, und sie fällt Anfängern schwerer:**

```python
class Hafen:
    def __init__(self):
        self.tag = 0
        self.ladung = []        # ⚠️ falsch — wessen Ladung?
```

`ladung` gehört einem Schiff. Zwei Schiffe hätten zwei verschiedene Ladungen. Sobald du sie in den Hafen legst, hast du sie für alle zusammengelegt, und du merkst es erst, wenn das zweite Schiff einläuft.

> **Die Welt ist kein Abstellraum für alles, was gerade keinen Platz hat.** Sie ist der Besitzer genau der Werte, die es pro Spiel einmal gibt.

### 2. Der Umbau selbst ist eine Fahndung

Du kennst das Verfahren aus Etappe 5 und 11. Ein Name wandert, und du suchst jede Stelle, die ihn benutzt:

| Vorher | Nachher |
|---|---|
| `kern_integritaet` | `welt.kern_integritaet` |
| `gegner` | `welt.gegner` |
| `welle` | `welt.welle` |

**Und innerhalb der Welt-Methoden heißt derselbe Wert `self.kern_integritaet`** — genau wie bei deinem Marine seit Etappe 9. Von außen `welt.`, von innen `self.`, dasselbe Objekt.

⚠️ **Die Fahndung ist heute größer als bei jedem bisherigen Umbau.** Zähl die Treffer vorher und schreib die Zahl auf. Wer hier auf gut Glück sucht, findet den letzten vergessenen Zugriff drei Abende später in Etappe 13.

### 3. Sieben Parameter werden einer — und das kostet etwas 👀

Hier ist der Gewinn, auf den du seit Etappe 7 wartest:

```python
def loesche_schiff(name, schiffe, liegeplaetze, tag, wetter, kran_defekt):
    ...

def loesche_schiff(name, hafen):
    ...
```

Aus sechs Parametern werden zwei. Jede Aufrufstelle wird kürzer. Und wenn du morgen einen siebten Wert brauchst, musst du **keine einzige Funktionssignatur ändern** — er steht schon im Hafen.

**🚨 KI-Code-Warnsignal — nur bemerken, nichts reparieren:**

Genau hier hast du etwas eingetauscht, und du solltest wissen, was:

| | Lange Parameterliste | Ein Welt-Objekt |
|---|---|---|
| Man sieht der Funktion an, was sie anfasst | **ja** | **nein** |
| Neuer Wert nötig | jede Signatur ändern | nichts ändern |
| Diese Funktion allein testen | mühsam, aber möglich | man braucht eine ganze Welt |

Die dritte Zeile ist die, die später wehtut. **Das hat einen Namen: Kopplung.** Eine Funktion, die die ganze Welt bekommt, kann alles anfassen — und niemand sieht ihr an, was sie tatsächlich anfasst.

⚠️ **Für dein Spiel ist es heute trotzdem richtig so.** Die Alternative wäre, jeder Funktion genau die drei Werte zu geben, die sie braucht, und das ist bei einem Spiel dieser Größe mehr Buchhaltung als Nutzen. **Merk dir nur die Frage — *muss dieses Ding wirklich alles kennen?*** Sie ist eine der nützlichsten, die du an fremdem Code stellen kannst, und du stellst sie in Etappe 15 an einer Zeichnung deines eigenen Codes wieder.

### 4. Zwei Namen, ein Objekt — diesmal als Werkzeug 🧠

In Etappe 10 war das eine Fehlerquelle: Zwei Marines teilten sich ein Inventar, und niemand merkte es.

**Heute nutzt du dasselbe Verhalten absichtlich.** Der Hafen hat eine Liste aller Schiffe — und eines davon ist das Flaggschiff, auf das er ständig zugreifen muss:

```python
class Hafen:
    def __init__(self, flaggschiff):
        self.schiffe = []
        self.schiffe.append(flaggschiff)
        self.flaggschiff = flaggschiff      # derselbe Kasten, zweiter Pfeil darauf
```

```python
hafen.flaggschiff.ladung = 40
print(hafen.schiffe[0].ladung)      # 40 — es ist dasselbe Schiff
```

**Zwei Namen zeigen auf ein Objekt, und das ist hier genau richtig.** Das Flaggschiff steht in der Liste, weil es ein Schiff ist wie jedes andere. Und es hat zusätzlich einen kurzen Namen, weil der Hafen es oft braucht.

⚠️ **Die Falle daneben:** Legst du stattdessen ein **zweites** Schiff-Objekt mit demselben Namen an, hast du zwei Flaggschiffe. Beide heißen gleich, beide sehen gleich aus, und Ladung, die du dem einen gibst, fehlt beim anderen. Prüf es mit dem Reflex aus Etappe 10:

```
(Pdb) p hafen.flaggschiff is hafen.schiffe[0]     → muss True sein
```

### 5. Was zuerst entsteht

Eine Frage, die dich beim Bauen aufhält, wenn du sie nicht vorher geklärt hast: **Der Hafen braucht das Flaggschiff, um zu entstehen. Das Flaggschiff braucht keinen Hafen.** Also entsteht es zuerst und wird übergeben:

```python
flaggschiff = Schiff("Nordstern")
hafen = Hafen(flaggschiff)
```

Nicht umgekehrt. **Wenn zwei Dinge einander brauchen, entsteht immer zuerst das, das ohne das andere auskommt.** Merk dir das Gefühl — in Etappe 24 wird daraus ein echtes Problem, wenn zwei Dateien einander importieren wollen.

---

## Dein Auftrag — Teil 12a

### 1. Zieh den Beweis

```bash
python spiel.py < befehle.txt > vorher.txt
```

Ergänz `befehle.txt` um alles, was seit Etappe 11 dazugekommen ist — mindestens `faehigkeit` und einen Blick auf den Trupp. **Ohne diese Datei fängst du nicht an.**

---

### 2. Hol deine Antwort aus Etappe 9 heraus

Lies in `GELERNT.md` nach, welche Werte du damals als „gehört der Welt" eingeordnet hast, und welche dir schwergefallen sind.

**Schreib daneben, was du heute sagen würdest.** Zwei Sätze. Das dauert fünf Minuten und ist der Grund, warum du die Antwort damals aufgeschrieben hast.

---

### 3. Bau die Klasse `Welt`

Ein Parameter: der gesteuerte Marine. Diese Attribute:

| Attribut | Startwert | Woher es kommt |
|---|---|---|
| `zeit` | `0` | neu — der Rundenzähler aus 3b in seiner endgültigen Form |
| `welle` | `1` | war die Schleifenvariable |
| `kern_integritaet` | `100` | lag seit Etappe 1 lose herum |
| `sektoren` | deine Karte aus Etappe 5 | war eine lose Variable |
| `gegner` | `[]` | war eine lose Liste |
| `trupp` | `[]` | war eine lose Liste aus Etappe 11 |
| `held` | der übergebene Marine | neu — Konzept 4 |
| `laeuft` | `True` | falls du in 3b die Zustandsvariable gebaut hast |

Der übergebene Marine wird **auch** an `trupp` angehängt. Er steht in der Liste *und* unter `held` — ein Objekt, zwei Namen.

**So prüfst du es:** In einer Wegwerf-Datei eine Welt erzeugen und `welt.held is welt.trupp[0]` drucken. Muss `True` ergeben.

---

### 4. Zieh die losen Variablen um

- Jede Variable aus der Tabelle in Schritt 3 verschwindet aus dem Hauptprogramm.
- Sie wird **gelöscht**, nicht auskommentiert.
- Die Wellenschleife bleibt, wo sie ist. Sie setzt am Anfang jeder Welle nur noch `welt.welle`.

⚠️ **Diese Werte bleiben, wo sie sind:** `trefferpunkte`, `vorrat`, `erfahrung`, `inventar`, `sektor` und `standort` gehören dem Marine, seit Etappe 9. Wer sie heute in die Welt zieht, macht die Entscheidung von damals rückgängig, ohne es zu merken.

**So prüfst du es:** Das Spiel startet nicht mehr. Ein `NameError` ist der freundliche Fall — er zeigt dir die nächste Stelle.

---

### 5. Zieh alle Zugriffsstellen nach

Die Fahndung, viertes Mal.

- Zähl die Treffer **vorher** und schreib die Zahl auf.
- Arbeite eine Variable vollständig ab, bevor du die nächste anfängst.
- Nach jeder einzelnen ausführen.

**So prüfst du es:** Kein `NameError`, kein `AttributeError`. Das Spiel läuft durch.

---

### 6. Kürz die Parameterlisten

- Jede Funktion, die bisher drei oder mehr Weltwerte einzeln bekam, bekommt jetzt `welt`.
- **Funktionen, die nur den Marine brauchen, bekommen weiterhin nur den Marine.** Nicht alles bekommt alles.
- Die Zeichenfunktionen aus Etappe 7b bleiben rein: Sie bekommen Werte, keine Welt.

⚠️ **Der letzte Punkt ist die Stelle, an der man heute Schaden anrichtet.** Eine Zeichenfunktion, die eine ganze Welt bekommt, kann darin etwas ändern — und damit ist die Reinheit weg, die du in 7b geprüft hast. Zeichnen bekommt Zahlen und Listen, sonst nichts.

**So prüfst du es:** Such nach der längsten Parameterliste, die noch übrig ist. Wenn dort noch `kern_integritaet` **und** `welle` **und** `gegner` nebeneinanderstehen, hast du eine Funktion übersehen.

---

### 7. Gib der Welt ein `__repr__`

Eine Zeile, die Zeit, Welle, Kernintegrität und die Anzahl der Gegner zeigt.

**Warum jetzt und nicht später:** Ab 12b hältst du das Programm im Debugger an und willst in *einer* Zeile sehen, wo du bist. `print(welt)` ist ab morgen dein wichtigster Debug-Befehl.

**So prüfst du es:** `print(welt)` ergibt eine lesbare Zeile ohne Speicheradresse.

---

### 8. Beweis und Commit

```bash
python spiel.py < befehle.txt > nachher.txt
diff vorher.txt nachher.txt
```

**Kein Unterschied.** Wenn doch: Der Unterschied ist ein Fehler, keine Verbesserung.

Commit: `Etappe 12a: Loser Zustand wird zur Welt`

> **⏸ Guter Schnitt.** Dein Spiel verhält sich exakt wie gestern und hat trotzdem eine andere Architektur. 12b ist ein eigener Abend — und dort ändert sich endlich etwas für den Spieler.

---

# Teil 12b — Der Tick

## Worum es geht

Deine Welt hat ein Attribut `zeit`, und es steht auf `0` und bleibt dort. Heute gibst du ihr die Methode, die es bewegt — und daran hängt sich alles andere.

> **Ein Tick ist ein Zeitschritt. Er passiert einmal, er passiert überall gleichzeitig, und danach ist die Welt einen Schritt weiter.**

Das Wort „gleichzeitig" ist dabei eine Lüge, und es lohnt sich, sie sofort zu durchschauen: **Dein Computer tut nichts gleichzeitig.** Er arbeitet eine Reihenfolge ab. Erst der Zähler, dann der Trupp, dann die Gegner, dann das Aufräumen — oder eben anders herum. Für den Spieler sieht beides nach einem Augenblick aus. Für dein Programm ist es der Unterschied zwischen einem Gegner, der noch schlägt, und einem, der vorher gefallen ist.

**Und heute fangen drei Marines an, ohne dich zu handeln.** Das ist der Moment, in dem aus einer Anwendung ein Spiel wird.

---

## Die Konzepte — Teil 12b

Weiter im Hafen.

### 6. Die Tick-Methode ⭐

Sie gehört der Welt, nicht den Dingen darin:

```python
class Hafen:
    def tick(self):
        self.tag += 1
        for s in self.schiffe:
            s.update(self)
```

Zwei Zeilen Rumpf, und sie tragen den Rest des Projekts.

**Warum tickt der Hafen und nicht jedes Schiff für sich?** Weil jemand die Reihenfolge bestimmen muss und weil jemand danach aufräumen muss. Ein Schiff, das sich selbst tickt, weiß nicht, ob die anderen schon dran waren. **Der Tick ist die einzige Stelle im Programm, die den Überblick über einen Zeitschritt hat** — und deshalb darf es genau eine geben.

⚠️ **`self.tag += 1` steht bewusst zuerst.** Sobald in Etappe 13 Zähler mitlaufen, ist die Frage „welchen Tag haben wir, während die Schiffe handeln?" eine echte. Beantworte sie heute, indem du die Zeile oben hinschreibst — und schreib auf, dass du es so entschieden hast.

### 7. `update()` an jeder Einheit — und die Basis tut nichts ⭐

Jede Klasse, die ticken soll, bekommt eine Methode desselben Namens. Die gemeinsame Basis bekommt eine, die nichts tut:

```python
class Schiff:
    def update(self, hafen):
        """Ein Schiff ohne eigenes Verhalten tut in einem Tick nichts."""
```

**Das ist ein vollständiger Methodenkörper.** Ein Docstring allein genügt Python als Rumpf — du kennst ihn seit Etappe 7, Konzept 9.

👀 **Was du stattdessen in fremdem Code sehen wirst:** dort steht meist `pass`. Das ist ein Platzhalter, der nichts tut und nur da ist, weil Python nach einem Doppelpunkt etwas eingerücktes verlangt. Beide Fassungen sind gleichwertig; die mit Docstring sagt zusätzlich, *warum* hier nichts steht.

**Und jetzt der Punkt, für den du Etappe 11 gebaut hast:**

```python
for s in self.schiffe:
    s.update(self)
```

Ein Frachter fährt, ein Schlepper schleppt, ein Wrack liegt herum — **und nirgends steht eine Abfrage, welches Schiff das gerade ist.** Jedes Objekt weiß es selbst. Das ist dieselbe Schleife wie bei der Fahrzeugflotte in Etappe 11, nur dass sie jetzt einmal pro Zeitschritt läuft statt einmal im ganzen Programm.

### 8. `self` als Argument weitergeben ⭐

Diese Zeile ist die einzige wirklich neue Schreibweise der Etappe:

```python
s.update(self)
```

**Lies sie langsam.** `self` ist, von innen gesehen, der Name des Objekts, in dessen Methode du gerade stehst — das kennst du seit Etappe 9. Neu ist, dass du ihn **weiterreichst**: Der Hafen übergibt sich selbst an das Schiff.

**Warum muss er das?** Weil das Schiff sonst nichts sehen kann außer sich selbst. Ein Schlepper, der einem anderen Schiff helfen soll, muss wissen, welche Schiffe es gibt. Ein Frachter, der anlegen will, muss die freien Liegeplätze kennen. Beides steht im Hafen.

**Im Schiff kommt das als ganz normaler Parameter an:**

```python
class Schlepper(Schiff):
    def update(self, hafen):
        if hafen.wetter == "sturm":
            return
        hafen.liegeplaetze -= 1
```

⚠️ **Zwei Namen für dasselbe Ding, und das verwirrt am Anfang zuverlässig:** Im Hafen heißt es `self`, im Schiff heißt es `hafen`. Es ist **dasselbe Objekt** — der Parametername ist nur der Name, unter dem das Schiff es kennt. Genau wie bei jeder anderen Funktion seit Etappe 7.

*(Und ja: Damit kennt jedes Schiff den ganzen Hafen. Das ist die Kopplung aus Konzept 3, jetzt an der Stelle, an der sie wirklich anfällt. Heute ist das richtig so. Die Frage stellst du in Etappe 15 wieder.)*

### 9. Gesteuert gegen autonom ⭐⭐

**Das ist der Begriff, um den es in dieser Etappe eigentlich geht**, und du kannst ihn an vier fast identischen Objekten sehen:

> **Eine gesteuerte Einheit wartet auf einen Befehl. Eine autonome Einheit entscheidet im Tick selbst.**

Deine vier Marines sind derselbe Typ. Sie haben dieselben Attribute, dieselben Methoden, dieselbe Basisklasse. **Sie unterscheiden sich in genau einem Attribut** — dem, das du in Etappe 11 gesetzt hast —, und dieses eine Attribut entscheidet, woher ihr nächster Befehl kommt:

| | Woher der Befehl kommt | Wann er kommt |
|---|---|---|
| Der Held | `input()` | wenn du tippst |
| Die drei Kameraden | die eigene `update()` | in jedem Tick |

**Deshalb steigt die `update()` des Helden sofort wieder aus.** Im Hafen sieht das so aus:

```python
class Frachter(Schiff):
    def update(self, hafen):
        if self.wird_gelotst:
            return
        self.position += 1
```

**Und hier steht ein `return` ohne Wert dahinter**, das du so noch nicht gesehen hast. In Etappe 7, Konzept 4 stand immer etwas dahinter — `return name`, `return None`. Ein `return` allein tut dasselbe wie `return None`, nur ohne es hinzuschreiben: **Es verlässt die Methode sofort, und der Aufrufer bekommt `None`.**

Nimm es überall dort, wo dich nur das Aussteigen interessiert und niemand auf einen Rückgabewert wartet. Genau das ist bei `update()` der Fall — der Tick ruft auf und sieht sich das Ergebnis nie an. Der gelotste Frachter tut im Tick also nichts, weil ein Mensch für ihn entscheidet.

⚠️ **Das sieht aus wie eine Typabfrage, ist aber keine.** Du fragst nicht *„welche Klasse bist du?"*, sondern *„hast du gerade jemanden, der dich steuert?"*. Der Unterschied ist nicht kosmetisch: Wenn du in Etappe 13 ausfällst und ein Kamerad übernimmt, ändert sich ein Attribut — und keine Klasse.

### 10. Die Trupp-KI in ihrer dümmsten Form

Die drei Kameraden tun ab heute genau **eine** Sache:

> **Wenn ein Ziel in Reichweite ist, feuere darauf.**

Kein Laufen, keine Zielauswahl nach Priorität, keine Fähigkeiten, kein Rückzug. **Das ist Absicht und keine Sparmaßnahme.** Laufen können sie nicht, weil es vor Etappe 14a keine Positionen gibt, auf denen man laufen könnte. Zielauswahl kommt in 23a, Fähigkeiten in 18.

**Was du für diese eine Regel brauchst, ist ein Ziel.** Und hier kommt die Schleife zurück, die du in Etappe 11a von Hand gebaut hast, weil `min()` an Objekten nicht mehr trägt:

```python
def naechstes_wrack(self):
    naechstes = None
    for s in self.schiffe:
        if s.status == "gesunken":
            if naechstes is None:
                naechstes = s
            elif ...:                  # ← diese Zeile gehört dir
                naechstes = s
    return naechstes
```

**Die offene Zeile ist die ganze Aufgabe.** Zwei Schiffe liegen auf dem Grund, `naechstes` hält gerade eines davon, und `s` ist das andere. **Welcher Vergleich muss wahr sein, damit `s` das bessere Ziel ist?** Schreib ihn hin, bevor du weiterliest — und prüf ihn an einem Fall, in dem beide dieselbe Tiefe haben.

**Drei Dinge, auf die es dabei ankommt:**

- Sie steht als Methode **im Hafen**, nicht im Schlepper. Die Suche braucht die ganze Liste, und die gehört dem Hafen. Sonst müsste jedes Schiff sie noch einmal schreiben.
- Sie gibt `None` zurück, wenn es nichts gibt. **Der Aufrufer muss das prüfen** — `is None` aus Etappe 10.
- Sie überspringt, was nicht in Frage kommt, mit einem `if` statt einer zweiten Liste.

⚠️ **Die Null-Falle, in ihrer heutigen Ausgabe:** `if ziel:` sieht kürzer aus als `if ziel is not None:` — und es funktioniert, solange ein Ziel immer wahrheitswertig wahr ist. Bleib bei `is None`. Du weißt seit Etappe 10, warum.

### 11. Sammeln und danach entfernen ⭐

Das hier ist der Fehler aus Etappe 4, und heute ist er kein Übungsfall mehr.

**Er sieht harmlos aus:**

```python
for s in self.schiffe:
    if s.status == "gesunken":
        self.schiffe.remove(s)      # ⚠️
```

**Sag voraus, bevor du weiterliest:** Vier Schiffe, alle vier gesunken. Wie viele sind nach dieser Schleife noch in der Liste?

Die Antwort ist **zwei**. Die Schleife merkt sich eine Stelle in der Liste, und wenn du einen Eintrag entfernst, rutscht alles dahinter eine Stelle nach vorn — an die Stelle, die gerade schon abgearbeitet wurde. **Jeder zweite Eintrag wird übersprungen.**

> ⚠️ **Und es stürzt nicht ab.** Kein Fehler, keine Meldung, keine rote Zeile. Das ist ein Typ-3-Fehler, und in deinem Spiel heißt er: Ein gefallener Gegner steht noch auf der Bahn, oder ein lebender verschwindet.

**Der Ausweg hat zwei Formen, und beide kennst du:**

```python
# Weg 1: über eine Kopie laufen, am Original ändern
for s in self.schiffe.copy():
    if s.status == "gesunken":
        self.schiffe.remove(s)

# Weg 2: erst sammeln, dann entfernen
weg = []
for s in self.schiffe:
    if s.status == "gesunken":
        weg.append(s)
for s in weg:
    self.schiffe.remove(s)
```

**Nimm heute Weg 2**, obwohl er länger ist. Der Grund ist nicht Geschmack:

- Weg 2 ist eine **eigene Phase im Tick**. Du kannst sie ans Ende stellen, und damit ist entschieden, dass niemand mitten im Tick verschwindet.
- Weg 2 gibt dir eine Liste `weg` in der Hand. Ab Etappe 15 willst du wissen, *was* in diesem Tick gefallen ist — bei Weg 1 ist diese Information weg.

*(`.copy()` bleibt trotzdem richtig und nützlich, überall dort, wo du keine zweite Phase brauchst. Zwei Werkzeuge für zwei Lagen.)*

### 12. Status als String — und ein Begriff dazu 👀

Damit die Aufräumphase weiß, wen sie entfernen soll, muss eine gefallene Einheit markiert sein. Zwei Zeilen genügen:

```python
if self.tiefgang <= 0:
    self.status = "gesunken"
```

**Das Entfernen und das Sterben sind ab jetzt zwei verschiedene Dinge**, und das ist der eigentliche Gewinn. Ein Schiff, das in diesem Tick gesunken ist, liegt noch in der Liste — aber jedes `update()` sieht am Status, dass es nichts mehr tut. **Ohne diese Trennung würde ein Gegner, den dein Kamerad zu Beginn des Ticks erledigt hat, am Ende desselben Ticks noch einmal zuschlagen.**

👀 **Der Begriff dazu, ein Satz, keine Aufgabe:** Ein Objekt, das eine feste Menge benannter Zustände hat und zwischen ihnen nach Regeln wechselt, heißt **Zustandsautomat**. Dein Gegner ist einer — er kennt `"aktiv"` und `"tot"`, und der Übergang hat genau eine Bedingung. Mehr musst du dazu heute nicht können.

⚠️ **Strings als Zustände sind eine Übergangslösung**, und du wirst den Grund selbst finden: Ein Tippfehler in `"aktvi"` erzeugt keinen Fehler, sondern einen Zustand, in dem nichts mehr passt. Etappe 21b löst das ab. Heute sind es zwei Wörter, und zwei Wörter verträgt jeder.

### 13. 👀 Die Tick-Reihenfolge ist eine Entscheidung

Dein Tick hat Phasen. Bei einer Reihenfolge wie dieser —

```
1. Zeit erhöhen
2. Trupp handelt
3. Gegner handeln
4. Gefallene entfernen
```

— stirbt ein Gegner, den dein Trupp in Phase 2 erledigt, **bevor** er in Phase 3 zuschlagen kann. Dreh 2 und 3 um, und derselbe Gegner trifft dich noch, bevor er fällt.

**Beide Fassungen sind vertretbar. Keine ist ein Fehler.** Die eine belohnt Verteidigung, die andere macht jeden Gegner gefährlicher.

> **Du musst heute keine gute Reihenfolge entwerfen. Du musst nur aufschreiben, welche du gebaut hast.**

Der Grund steht in Etappe 16: Dort schreibst du einen Tick von Hand mit und stellst fest, dass ein Gegner ein Feld weiter vorne stirbt, als du erwartet hast. Nichts stürzt dabei ab. **Wenn du dann nachschlagen kannst, welche Reihenfolge du gewählt hattest, ist der Fehler in zehn Minuten gefunden. Wenn nicht, in zwei Stunden.** Das ist der ganze Grund für Auftragsschritt 16.

### 14. Welcher Befehl löst einen Tick aus?

In Etappe 3b hast du entschieden, welche Befehle eine Runde kosten: Auskunft kostet nichts, Handlung schon. **Dieselbe Entscheidung, heute mit Zähnen.**

Damals kostete dich eine falsche Antwort einen Rundenzähler, der zu schnell lief. Heute kostet sie dir das Gleichgewicht des ganzen Spiels: Wer `status` tippen kann, ohne dass die Gegner vorrücken, kann vor jedem Schuss beliebig lange nachdenken. Wer einen Tippfehler macht und dafür einen Tick bezahlt, wird für Tippfehler bestraft.

| Eingabe | Tick? | Warum |
|---|---|---|
| `feuern`, `nachladen`, `gehe norden` | **ja** | Handlung |
| `status`, `inventar`, `umsehen` | **nein** | Auskunft |
| `hdsjkfh` (ungültig) | **du entscheidest** | siehe unten |

**Die dritte Zeile ist die interessante**, und sie hat keine richtige Antwort. Kostet Unsinn keinen Tick, ist die Eingabe ein kostenloser Zeitstopp. Kostet er einen, bestraft das Vertipper. Entscheide dich, schreib es auf — und probier im Kaputtmachen aus, was die andere Fassung tut.

---

## Dein Auftrag — Teil 12b

### 9. Gib `Einheit` eine `update()`-Methode, die nichts tut

- Parameter: `self` und `welt`.
- Körper: ein Docstring, der sagt, warum hier nichts steht.

**So prüfst du es:** In einer Wegwerf-Datei eine `Einheit` erzeugen und `update()` aufrufen. Kein Fehler, keine Ausgabe.

---

### 10. Ergänz `nimm_schaden()` um den Status

- `Einheit` bekommt in `__init__` das Attribut `status` mit dem Startwert `"aktiv"`.
- Fallen die Trefferpunkte auf `0` oder darunter, setzt `nimm_schaden()` sie auf `0` und den Status auf `"tot"`.
- Der Rückgabewert bleibt, wie er in Etappe 11 war.

⚠️ **Trefferpunkte auf `0` festnageln, nicht ins Negative laufen lassen.** Sonst zeigt deine Balkenanzeige aus Etappe 3c irgendwann einen Balken mit negativer Länge, und du suchst den Fehler dort statt hier.

**So prüfst du es:** Eine Einheit mit 10 Trefferpunkten 20 Schaden nehmen lassen. `trefferpunkte` ist `0`, `status` ist `"tot"`.

---

### 11. Bau `welt.naechster_gegner()`

- Eine Methode der `Welt`, die den aktiven Gegner mit der kleinsten Entfernung zurückgibt.
- Gibt `None` zurück, wenn es keinen gibt.
- Gegner mit Status `"tot"` kommen nicht in Frage.

*(Das ist die Schleife aus Etappe 11a, Konzept 4 — mit einer zusätzlichen Bedingung. `min(..., key=...)` kommt in Etappe 23a; heute baust du sie von Hand.)*

**So prüfst du es:** Drei Gegner in verschiedenen Entfernungen, einer davon `"tot"` und am nächsten. Die Methode muss den zweitnächsten liefern. Danach alle auf `"tot"` setzen: `None`.

---

### 12. Gib `Gegner` seine `update()`

Die Regel, die bei dir bisher irgendwo in der Rundenschleife stand, zieht in die Klasse um:

- Status `"tot"`? Sofort `return`.
- Entfernung größer als `0`? Um eins verringern, dann `return`.
- Sonst: Schaden auf `welt.kern_integritaet`.

**So prüfst du es:** Eine Welt mit einem Gegner in Entfernung 2 bauen und dreimal `update()` aufrufen. Beim dritten Mal sinkt die Kernintegrität.

---

### 13. ⭐ Gib `Marine` seine `update()`

**Das ist der Auftragsschritt dieser Etappe.** Rechne mit einem halben Abend.

⚠️ **Und hier ist eine Zwischenstufe, an der du aufhören darfst.** Bau zuerst die Fassung **ohne** Reichweitenprüfung: Der Kamerad feuert auf das, was `welt.naechster_gegner()` liefert, egal wie weit weg es ist. Die läuft, sie ist testbar, und sie ist ein sauberer Stand zum Committen.

**Wenn du an dieser Stufe für heute Schluss machst, ist das kein Rückstand.** Der Plan ist ein Vorschlag, kein Vertrag — und eine Zwischenstufe, die läuft, ist mehr wert als eine vollständige, die um Mitternacht halb fertig liegenbleibt. `REICHWEITE` kommt dann morgen dazu und kostet vier Zeilen.

- `gesteuert`? Sofort `return` — der Held wartet auf `input()`.
- Status `"tot"`? Sofort `return`.
- Ziel über `welt.naechster_gegner()` holen. `None`? `return`.
- Entfernung des Ziels kleiner oder gleich `REICHWEITE`? Dann `nimm_schaden()` mit dem eigenen Schaden, und eine Meldung ausgeben.

Leg `REICHWEITE` als festen Wert oben in der Datei an, groß geschrieben, Startwert `5`. *(Die Schreibweise ist die Verabredung aus Etappe 1.)*

⚠️ **Feuern kostet die Kameraden heute keine Munition.** Das ist eine bewusste Auslassung — ein Vorrat pro Kamerad wäre ein eigenes Thema, und es steht in Etappe 13, wo Zähler an Objekten drankommen. Notier es in `GELERNT.md` als offenen Posten.

**So prüfst du es:** Starte das Spiel und tipp `status`, ohne zu feuern. Sobald der erste Gegner nah genug ist, verliert er Trefferpunkte, ohne dass du etwas getan hast. **Das ist der Moment, für den du Etappe 11 gebaut hast.**

---

### 14. Bau `welt.tick()`

Vier Phasen, in dieser Reihenfolge:

1. `self.zeit += 1`
2. Über `self.trupp` laufen, bei jedem `update(self)` aufrufen
3. Über `self.gegner` laufen, ebenso
4. Aufräumen (Schritt 15)

**So prüfst du es:** In einer Wegwerf-Datei eine Welt mit drei Gegnern bauen und fünfmal `tick()` aufrufen. Druck nach jedem Tick `print(welt)` — dafür hast du das `__repr__` in Schritt 7 gebaut.

---

### 15. Bau die Aufräumphase

- Eine eigene Methode der Welt.
- Erst eine Liste `gefallene` füllen, dann in einer **zweiten** Schleife aus `self.gegner` entfernen.
- Die Methode gibt zurück, wie viele es waren.

⚠️ **Nicht in einer Schleife entfernen.** Konzept 11 — und dieser Schritt ist der Grund, warum es dort steht.

**So prüfst du es:** Vier Gegner, alle auf `"tot"`, einmal aufräumen. `len(welt.gegner)` muss `0` sein. Wenn `2` dasteht, hast du den Fehler aus Konzept 11 gebaut — sieh ihn dir an, bevor du ihn reparierst.

---

### 16. Häng den Tick an den Befehl

- Nach jedem Befehl, der Zeit kostet, ruft die Hauptschleife `welt.tick()` auf — **genau einmal.**
- Deine Entscheidung aus Etappe 3b, welche Befehle Zeit kosten, bleibt gültig.
- Entscheide neu, was bei einer **ungültigen** Eingabe passiert, und schreib die Entscheidung auf.

⚠️ **Genau einmal.** Wenn das alte Vorrücken der Gegner bei dir noch in der Rundenschleife steht, hast du es jetzt doppelt: einmal dort, einmal im Tick. **Lösch die alte Stelle.** Das ist der wahrscheinlichste Fehler dieser Etappe.

**So prüfst du es:** Tipp zehnmal `status`. Die Gegner dürfen sich keinen Schritt bewegt haben. Dann zehnmal `nachladen`: Sie müssen zehn Schritte näher sein.

---

### 17. ⭐ Schreib die Tick-Reihenfolge auf

In `GELERNT.md`, als nummerierte Liste, mit einem Satz dazu: **Was wäre anders, wenn Phase 2 und 3 vertauscht wären?**

**Das ist der Auftragsschritt mit der längsten Wirkung.** Er kostet fünf Minuten und spart dir in Etappe 16 zwei Stunden.

---

### 18. Gib den Einheiten ein Gedächtnis

- Jede `Einheit` bekommt in `__init__` das Attribut `abschuesse` mit Startwert `0`.
- Wer ein Ziel zur Strecke bringt, erhöht es um eins.
- Die Statusanzeige zeigt es beim Trupp mit an.

**Billig gebaut, große Wirkung:** Nach zehn Wellen steht in deiner Statuszeile, dass Rekrut Vasquez elf Kriecher erledigt hat, und plötzlich ist Vasquez keine Zeile mehr, sondern jemand. Etappe 17 baut darauf Meldungen auf.

**So prüfst du es:** Spiel drei Wellen ohne selbst zu feuern. Mindestens ein Kamerad hat eine Zahl größer als `0`.

---

### 19. Prüf, dass das Alte noch läuft

Ohne `diff`, denn das Verhalten hat sich absichtlich geändert. Von Hand:

- Kaufen, nachladen, Sektor wechseln, Fähigkeit einsetzen — alles wie vorher?
- Sinkt die Kernintegrität, wenn ein Gegner ankommt?
- Endet das Spiel noch, wenn sie auf `0` fällt — **und ebenso, wenn deine eigenen Trefferpunkte auf `0` fallen?**

⚠️ **Die letzte Frage ist die, die übersehen wird.** Du hast seit Etappe 1 zwei Verlustbedingungen. Prüf beide, jedes Mal.

---

### 20. Aufräumen und Commit

Keine auskommentierte alte Bewegungslogik, kein vergessenes `breakpoint()`.

Commit: `Etappe 12b: Der Vorposten tickt`

---

## Was NICHT in diese Etappe gehört

**Keine Abklingzeiten, keine Bauzeiten, keine Zähler an Objekten.** Das ist Etappe 13, und es ist das Erste, was der Tick tragen wird.

**Keine Bewegung der Kameraden.** Sie feuern oder sie feuern nicht. Laufen braucht Positionen, und die kommen in Etappe 14a.

**Keine Zielauswahl nach Priorität.** „Der Nächste" genügt. Strategien sind 23a.

**Keine Fähigkeiten im Tick.** Die Kameraden setzen heute keine ein. Etappe 18.

**Kein `Enum` für die Zustände.** Zwei Strings genügen. Etappe 21b.

**Keine Echtzeit.** Der Tick läuft, wenn du einen Befehl gibst, nicht wenn eine Sekunde vergeht. Etappe 28.

**Keine Reparatur der Kopplung.** `update(self, welt)` bleibt, wie es ist. Bemerken, nicht beheben.

**Keine dritte Liste `einheiten`.** Die Design-Entscheidung ist gefallen.

---

## Selbsttest

**12a**
- [ ] Keine der Variablen aus der Tabelle in Schritt 3 existiert noch lose — auch nicht auskommentiert.
- [ ] `welt.held is welt.trupp[0]` ergibt `True`.
- [ ] `diff vorher.txt nachher.txt` nach 12a zeigt **keinen** Unterschied.
- [ ] Keine Funktion bekommt mehr `kern_integritaet`, `welle` und `gegner` einzeln.
- [ ] Die Zeichenfunktionen aus 7b bekommen weiterhin keine Welt.
- [ ] `trefferpunkte` und `vorrat` gehören immer noch dem Marine.

**12b**
- [ ] Zehnmal `status` bewegt keinen Gegner. Zehnmal `nachladen` bewegt sie zehn Schritte.
- [ ] Ein Kamerad erledigt einen Gegner, ohne dass du etwas tust.
- [ ] Vier tote Gegner verschwinden bei einem Aufräumen **alle vier**.
- [ ] Ein Gegner, der in der Trupp-Phase eines Ticks fällt, schlägt in der Gegner-Phase **desselben** Ticks nicht mehr zu.
- [ ] Nirgends fragt der Code, welche Klasse eine Einheit hat.
- [ ] Beide Verlustbedingungen beenden das Spiel.
- [ ] Die Tick-Reihenfolge steht in `GELERNT.md`.
- [ ] Beide Commits sind gesetzt.

---

## Lernziele

In `GELERNT.md`, ohne nachzuschlagen.

1. Warum tickt die Welt und nicht jede Einheit für sich?
2. Was bedeutet `self` in der Zeile `einheit.update(self)` — und wie heißt dasselbe Objekt auf der anderen Seite?
3. Warum bekommt `update()` die ganze Welt übergeben, und was ist der Preis dafür?
4. **Was passiert, wenn du beim Iterieren über eine Liste Einträge daraus entfernst — und warum merkst du es nicht sofort?**
5. Was unterscheidet eine gesteuerte von einer autonomen Einheit? Ein Satz.
6. Wozu ist `status = "tot"` gut, wenn die Einheit am Ende des Ticks ohnehin entfernt wird?
7. Was ist ein Zustandsautomat, und wo steckt einer in deinem Gegner? *(Ein Satz reicht.)*
8. Welche Reihenfolge hat dein Tick, und was wäre bei der umgekehrten anders?
9. Warum steht `naechster_gegner()` in der `Welt` und nicht im `Marine`?
10. Welche Werte gehören der Welt, welche dem Marine — und an welcher Frage hast du das entschieden?

**Frage 4 ist die wichtigste.** Sie ist der Fehler, der in Etappe 16 auf dich wartet.

**Frage 8 ist die, die du am ehesten für unwichtig hältst.** Sie ist es nicht.

---

## Leseübung — Stufe 2 (15 Minuten) ⭐

**Ab heute steigt die Leseleiter auf Stufe 2.** Stufe 1 fragte *was passiert hier?*. Stufe 2 fragt:

> **Was verändert sich — und wer verändert es?**

**Die Regel bleibt: Du tippst nichts ab und führst nichts aus.** Auf Papier verfolgen. Wer den Code laufen lässt, lässt das Programm die Frage beantworten statt sich selbst.

```python
class Pflanze:
    def __init__(self, name, hoehe, wasser):
        self.name = name
        self.hoehe = hoehe
        self.wasser = wasser
        self.status = "lebt"

    def update(self, haus):
        if self.wasser <= 0:
            self.status = "vertrocknet"
            return
        self.wasser -= 1
        self.hoehe += 1
        if self.hoehe >= haus.decke:
            haus.geerntet.append(self.name)
            self.status = "geerntet"


class Gewaechshaus:
    def __init__(self, decke):
        self.tag = 0
        self.decke = decke
        self.beet = []
        self.geerntet = []

    def tick(self):
        self.tag += 1
        for p in self.beet:
            p.update(self)
        weg = []
        for p in self.beet:
            if p.status != "lebt":
                weg.append(p)
        for p in weg:
            self.beet.remove(p)


haus = Gewaechshaus(12)
haus.beet.append(Pflanze("Basilikum", 9, 4))
haus.beet.append(Pflanze("Minze", 6, 1))
haus.beet.append(Pflanze("Thymian", 11, 0))
```

**Die fünf Fragen:**

1. Was kommt rein?
2. Was passiert?
3. Was verändert sich — und woran?
4. Was kommt raus?
5. Welche anderen Objekte oder Funktionen werden dabei aufgerufen?

**Und die drei, die zu dieser Etappe gehören:**

6. **Was steht nach dem dritten `tick()` in `haus.beet` und in `haus.geerntet`?** Schreib beide Listen vollständig hin, mit allen Werten.
7. Thymian ist 11 hoch, die Decke liegt bei 12. **Warum wird er nie geerntet?** Die Antwort steht in `update()`, nicht in `tick()` — es geht um die Reihenfolge **innerhalb** einer Methode.
8. Wer setzt `status` — und wer liest ihn? Sind das dieselben zwei Klassen?

*(Frage 7 ist genau die Fehlerklasse, die dich in Etappe 16 erwartet. Sie ist hier kein Fehler, sondern eine Entscheidung — aber sie sieht identisch aus.)*

---

## Transferaufgabe (15 Minuten)

**Außerhalb des Spiels.** Eine Uhr, kein Vorposten.

1. Klasse `Uhr` mit `stunde` und `minute`, beide Startwert `0`.
2. Methode `tick()`: erhöht die Minute um eins. Bei `60` springt sie auf `0` und die Stunde um eins weiter. Bei `24` Stunden springt auch die Stunde auf `0`.
3. Ein `__repr__`, das `07:05` zeigt und nicht `7:5`. *(Ein f-String und ein `if` genügen — die Formatangabe, die das in einem Zug könnte, kommt später.)*
4. Ruf `tick()` 1500-mal auf und druck das Ergebnis. Rechne vorher aus, was dastehen muss.

**Und dann der eigentliche Teil:**

5. **Bau einen Wecker.** Die Uhr bekommt `weckzeit` als Tuple `(7, 0)` und gibt einmal eine Meldung aus, wenn sie diese Zeit erreicht.
6. **Sag voraus**, was bei 1500 Ticks passiert, wenn du die Prüfung *vor* das Erhöhen der Minute setzt statt danach. Führ es dann aus.

**Schritt 6 ist der Kern.** Es ist dieselbe Frage wie in Konzept 13, an einem Beispiel, bei dem du die richtige Antwort nachrechnen kannst.

---

## Kaputtmachen

**Vor jedem Experiment aufschreiben, was passieren wird.** Die ersten vier gehören dazu, die letzten zwei sind Kür.

**1. ⭐ Ruf `tick()` zweimal pro Befehl auf.** Dann gar nicht. Dann nur nach gültigen Befehlen. **Und dann die eigentliche Frage:** Kannst du dir mit Unsinn-Eingaben unendlich Zeit erkaufen? Spiel eine Welle so durch. **Das ist ein Typ-3-Fehler, der wie eine Spielmechanik aussieht** — und genau deshalb bleibt er in echten Spielen manchmal jahrelang drin.

**2. ⭐ Entferne beim Iterieren.** Bau die Aufräumphase absichtlich zu einer einzigen Schleife um. Setz vier Gegner auf `"tot"` und räum auf. Zähl, wie viele übrig bleiben, **bevor** du nachsiehst. Danach: Wie viele bleiben bei fünf? Bei sechs? Findest du die Regel?

**3. Lass den Status weg.** Nimm die Prüfung `if self.status == "tot": return` aus `Gegner.update()` heraus. Sorg dafür, dass ein Kamerad einen Gegner erledigt, der noch nicht am Zug war. **Was macht der tote Gegner danach?**

**4. Dreh die Tick-Phasen um.** Lass die Gegner vor dem Trupp handeln. Spiel drei Wellen. Wie viel Kernintegrität hast du am Ende — und ist das Spiel dadurch besser oder schlechter geworden?

---

Die folgenden zwei sind Kür.

**5. Vergiss das Argument.** Schreib `einheit.update()` statt `einheit.update(self)`. Lies den `TypeError` genau: Welche Zahl nennt er, und warum ist sie um eins höher, als du erwartet hättest? *(Etappe 9, Konzept 4 — derselbe Mechanismus, andere Richtung.)*

**6. Tick den Helden mit.** Nimm die `gesteuert`-Prüfung aus `Marine.update()` heraus. Was tut dein Held jetzt bei jedem Befehl — und woran merkst du es zuerst?

---

**Experiment 1 und 4 sind das Paar.** Beide ändern nicht eine einzige Regel des Spiels, sondern nur, *wann* etwas passiert — und beide ändern das Spielgefühl vollständig. Wer das einmal gesehen hat, versteht, warum Etappe 16 eine ganze Sitzung auf Reihenfolgefehler verwendet.

Alles in `GELERNT.md` und ins Fehlertagebuch aus Etappe 8: **woran du es erkannt hättest.**

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `NameError: name 'kern_integritaet' is not defined` | Eine Zugriffsstelle wurde in 12a übersehen | Schritt 5 — die Fahndung ist unvollständig |
| `AttributeError: 'Welt' object has no attribute 'gegner'` | Tippfehler im Attributnamen oder in `__init__` vergessen | Schritt 3 — die Tabelle durchgehen |
| `TypeError: update() missing 1 required positional argument` | `einheit.update()` ohne `self` | Konzept 8 — der Tick übergibt die Welt |
| `TypeError: update() takes 1 positional argument but 2 were given` | Die Methode hat `welt` nicht in der Parameterliste | Die Signatur muss `(self, welt)` lauten |
| Die Gegner rücken doppelt so schnell vor | Das alte Vorrücken steht noch in der Rundenschleife | Schritt 16 — die alte Stelle löschen |
| Jeder zweite tote Gegner bleibt liegen | Entfernen während der Schleife | Konzept 11 — zwei Schleifen statt einer |
| Ein gefallener Gegner schlägt noch zu | Kein `status`-Check am Anfang von `update()` | Schritt 12, erste Zeile |
| Der Held handelt von selbst | `gesteuert`-Prüfung fehlt oder greift nicht | Schritt 13 — steht das Attribut wirklich auf `True`? |
| Die Kameraden feuern nie | `naechster_gegner()` gibt `None` oder die Reichweite ist zu klein | Schritt 11 einzeln testen, dann `REICHWEITE` |
| `AttributeError: 'NoneType' object has no attribute 'entfernung'` | Der Rückgabewert von `naechster_gegner()` wurde nicht geprüft | Konzept 10 — `is None` vor dem Zugriff |
| Alle vier Marines haben dieselben Abschüsse | Ein geteiltes Objekt | Etappe 10, Konzept 6 — `is` prüfen |
| Der Balken hat negative Länge | Trefferpunkte laufen ins Negative | Schritt 10 — auf `0` festnageln |

**Der Debugging-Reflex dieser Etappe: „In welchem Tick war das?"**

Etappe 9 fragte *wem gehört dieser Wert*, Etappe 10 *sind das überhaupt zwei Dinge*. Heute kommt die Zeitfrage dazu — und der bedingte Breakpoint aus Etappe 8, Konzept 7, ist genau dafür gebaut:

```python
if self.zeit == 40:
    breakpoint()
```

**Das ist die schärfste Kombination, die du bisher hast.** Statt vierzig Ticks lang `print`-Zeilen zu lesen, hältst du genau bei dem an, der schiefgeht, und siehst dir mit `p welt` an, wo du stehst. Genau dafür hast du das `__repr__` in Schritt 7 gebaut.

---

## Ein Blick nach vorne

**Etappe 13 hängt sich als Erstes an den Tick.** Abklingzeiten, die Bauzeit des Basisturms, Nachladen und dein eigener Ausfall mit Respawn-Zähler — alle sind dasselbe Muster: ein Zähler, der pro Tick um eins sinkt. Dein `tick()` von heute bekommt eine Phase dazu, und mehr passiert dort nicht.

**Etappe 14a macht aus `entfernung` ein `(x, y)`** — und deine `update()`-Methoden sind die Stellen, die das merken. In 14b lernen die Kameraden laufen, und aus „in Reichweite" wird eine Rechnung.

**Etappe 15 zeichnet deine Kopplung auf Papier.** Fünf Minuten, nichts wird repariert. Du wirst sehen, wie viele Pfeile bei der `Welt` zusammenlaufen.

**Etappe 16 ist die Bug-Jagd II**, und die Reihenfolge deines Ticks ist dort der Hauptverdächtige. Deine Notiz aus Schritt 17 ist das Beweismittel.

**Etappe 17 gibt deinen Einheiten eine Stimme.** Die Abschusszahlen von heute werden zu Meldungen zwischen den Wellen.

**Etappe 19 speichert die Welt** — und dann zeigt sich, dass `self.zeit` und halb abgelaufene Zähler zum Spielstand gehören, sonst springt beim Laden die Zeit zurück.

**Etappe 21b tauscht deine Zustandsstrings gegen ein `Enum`** — und du wirst dich an den ersten Tippfehler in `"tot"` erinnern.

**Etappe 28 ruft den Tick sechzigmal pro Sekunde auf**, statt einmal pro Befehl. Dann ist aus derselben Methode Echtzeit geworden, ohne dass sich eine Zeile darin ändert. **Das ist der Grund, warum sie heute so gebaut wird.**

---

## Abschluss

**In `GELERNT.md`:**

- Wie viele Zugriffsstellen musste ich in 12a anfassen?
- ⭐ **Meine Antwort aus Etappe 9 — hat sie getragen?** Welchen Wert habe ich anders eingeordnet, als ich damals dachte?
- ⭐⭐ **Die Tick-Reihenfolge**, nummeriert, mit dem Satz zur Umkehrung.
- Meine Entscheidung: Kostet eine ungültige Eingabe einen Tick? Warum?
- Was hat mich überrascht? *(Kandidaten: dass ein Kamerad ohne mich feuert · dass jeder zweite tote Gegner liegen bleibt · wie kurz die Funktionssignaturen geworden sind.)*
- Offener Posten: Die Kameraden feuern ohne Munition.

**Vor dem Commit:** Beide Verlustbedingungen geprüft? Das alte Vorrücken gelöscht? Kein `breakpoint()` mehr drin?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest.

**Zähl, wie viele Parameter du in 12a eingespart hast.** Addier die Parameterlisten aller Funktionen vorher und nachher. Die Zahl ist das ehrlichste Argument für diesen Umbau.

**Gib der Welt eine Methode `lebende_gegner()`**, die zählt, wie viele Gegner nicht `"tot"` sind. Eine Schleife, vier Zeilen — und deine Wellenende-Prüfung wird dadurch lesbar.

**Lass den Tick sich selbst protokollieren.** Eine Zeile pro Phase, mit `### PHASE 2` davor, wie der Reflex aus Etappe 3. Spiel eine Welle, lies das Protokoll, und lösch die Zeilen wieder. Du siehst zum ersten Mal, was in einem einzigen Zeitschritt tatsächlich passiert — und in Etappe 16 machst du genau das noch einmal, dann von Hand auf Papier.

**Such in fremdem Spielcode nach `def update(`.** Du wirst es in fast jedem finden, und es bekommt fast immer irgendeine Form von Welt übergeben. Jetzt weißt du, warum — und welche Frage du daran stellen kannst.

---

> **Nächste Etappe:** [Etappe 13 — Bauzeit und Abklingzeit](etappe-13-bauzeit-und-abklingzeit.md) · dasselbe Zähler-Muster fünfmal, ein Turm im Vorposten, und dein eigener Ausfall ist nicht mehr das Ende
