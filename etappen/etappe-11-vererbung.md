# Etappe 11 — Vererbung, und die Frage, ob wir sie brauchen

*v1.1.0 · 2026-09-08*

> **Block 2: Einheiten und Zeit** · Etappe 11 von 30 · [← Etappe 10](etappe-10-komposition.md) · [Lehrplan](../Vorposten_Lehrplan.md) · Etappe 12 →

**Neue Syntax heute:** `class Kind(Eltern):` · `super().__init__(...)` · Methoden überschreiben · 👀 `__len__`, `__contains__`, `__iter__` · 👀 `@property` · 👀 `type(self).__name__`

**Zeitaufwand:** 11a: 3–4 Sitzungen · 11b: 5–6 Sitzungen · 11c: 3–4 Sitzungen, à 20–30 Minuten. Rund 35 Minuten Lesestoff, verteilt auf drei Portionen — die Zeit steckt hier im Bauen, nicht im Lesen. **Das ist die größte Etappe des Blocks** — und sie ist geteilt, weil sie drei Schulden auf einmal zurückzahlt.

**Voraussetzung:** Etappe 10 abgeschlossen, Selbsttest grün. Du brauchst heute alles: Klassen aus 9, Komposition aus 10, den Debugger aus 8.

**Die drei Portionen und was jede abschließt:**

| | Was passiert | Woher die Schuld kommt |
|---|---|---|
| **11a** | Deine zwei Gegnerlisten werden **eine** | Etappe 6 — seit fünf Etappen |
| **11b** | Vererbung, und **der Trupp entsteht** | Etappe 2 — seit neun Etappen |
| **11c** | Items werden Objekte, und du **entscheidest schriftlich** | Etappe 4 — seit sieben Etappen |

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **11a** | Eine Liste von `Gegner`-Objekten statt zweier paralleler Listen | Warum die beiden Fehlerarten aus Etappe 6 jetzt unmöglich sind | — |
| **11b** | `Einheit` als Basis · `super()` · `faehigkeit_einsetzen()` überschreiben · vier Marine-Klassen | „ist ein" gegen „hat ein" · Held und Kamerad auf einer Basisklasse | `type(self).__name__` |
| **11c** | `Item`-Hierarchie · **die Vererbungsfrage schriftlich** | Wann Vererbung *nicht* passt | `__len__`, `__contains__`, `__iter__`, `@property` |

---

# Teil 11a — Eine Liste statt zwei

## Worum es geht

Seit Etappe 6 schleppst du das hier mit dir herum:

```python
gegner       = [7, 4, 2]
gegner_typen = ["kriecher", "kriecher", "speier"]
```

Zwei Listen, die über den Index zusammenhängen. Der Gegner an Stelle 0 hat Entfernung 7 **und** ist ein Kriecher — aber dass diese beiden Dinge zusammengehören, steht **nirgends im Code**. Es steht in deinem Kopf.

Du hast dafür bezahlt, und zwar an zwei Stellen:

- **Beim Entfernen** musst du an zwei Listen denselben Index treffen. `remove()` nach Wert trägt nicht mehr, weil zwei Gegner dieselbe Entfernung haben können.
- **Beim Hinzufügen** musst du an beide denken. Vergisst du eine, sind sie verschieden lang — und ab da beschreibt jeder Index den falschen Gegner.

> **Heute wird daraus eine Liste, und der Eintrag weiß selbst, was er ist.**

```python
gegner = [Gegner("kriecher", 7), Gegner("kriecher", 4), Gegner("speier", 2)]
```

**Die `Gegner`-Klasse hast du in Etappe 9a schon geschrieben** und dann liegen gelassen. Heute setzt du sie ein. Das war kein Leerlauf, sondern Vorbereitung: In 11b steht sie neben `Marine`, und die Frage, was die beiden gemeinsam haben, ist der Einstieg in die Vererbung.

⚠️ **Und dieser Teil ist ein reiner Umbau.** Der Spieler merkt nichts. Also gilt wieder: `befehle.txt`, `diff`, und jede Abweichung ist ein Fehler.

---

## Vor dem Umbau: drei Fragen ⭐

| Frage | Antwort |
|---|---|
| **Was bleibt gleich?** | Jede Zahl, jede Meldung. Die Anmarschbahn sieht Zeichen für Zeichen gleich aus. |
| **Was ändert sich nur in der Darstellung?** | Nichts. |
| **Was ändert sich wirklich am Datenmodell?** | Aus zwei Listen wird eine. **Die Liste bleibt eine Liste** — nur was ein Eintrag *ist*, wird reicher. |

**Die letzte Zeile ist die Migrationsregel dieses Projekts**, und sie ist der Grund, warum dieser Umbau kleiner ist, als er aussieht: Deine Schleifen, dein `len()`, deine Bewegungslogik funktionieren unverändert. Nur der Zugriff auf den einzelnen Eintrag ändert sich.

---

## Die Konzepte — Teil 11a

Beispiele aus fremden Domänen. Dein Spielcode kommt im Auftrag.

### 1. Ein Eintrag, eine Sache ⭐

Vorher, in einer Lagerverwaltung:

```python
mengen = [3, 1, 7]
namen  = ["brot", "salz", "brot"]
```

Nachher:

```python
lager = [Ware("brot", 3), Ware("salz", 1), Ware("brot", 7)]
```

**Was sich dabei ändert, ist nicht die Bequemlichkeit, sondern was überhaupt schiefgehen kann.** Erinnere dich an die zweistufige Invariante aus Etappe 6:

| Invariante | Vorher | Nachher |
|---|---|---|
| Beide Listen sind gleich lang | musste geprüft werden | **existiert nicht mehr** |
| Für jeden Index beschreiben beide denselben Gegner | war **nicht messbar** | **existiert nicht mehr** |

> **Die zweite war die gefährliche, weil man sie nicht prüfen konnte.** Zwei gleich lange Listen können trotzdem falsch zusammengehören, und kein `len()` der Welt hätte es gemerkt. **In deinem Gegnermodell ist diese Fehlerklasse ab heute gegenstandslos — nicht abgesichert, sondern weg: Es gibt keine zweite Liste mehr, die synchron gehalten werden müsste.**

⚠️ *Das ist keine Eigenschaft von Objekten an sich. Wer morgen wieder zwei parallele Listen anlegt, hat das Problem zurück. Verschwunden ist es, weil Typ und Entfernung jetzt am **selben** Objekt hängen.*

Das ist der stärkste Gewinn, den eine Datenstrukturänderung bringen kann: nicht *„der Fehler wird gefunden"*, sondern *„der Fehler kann nicht mehr entstehen"*.

### 2. Der Index war die Identität — jetzt ist es das Objekt 🧠

In Etappe 6 stand: *Der Index ist die Identität des Gegners.* Wenn du wissen wolltest, *welcher* Gegner das ist, war die Antwort „der an Stelle 2" — eine Verbindung, die nirgends geschrieben stand und sich bei jedem Entfernen verschob.

Ein Objekt ist seine eigene Identität. `Ware("brot", 3)` und `Ware("brot", 7)` sind zwei verschiedene Dinge, auch wenn beide „brot" heißen. Und deshalb funktioniert etwas wieder, das seit Etappe 6 kaputt war:

⭐ **Sag zuerst voraus, bevor du weiterliest:** In der Liste unten stehen **zwei** Waren namens „brot". Welche verschwindet — und warum genau diese?

```python
lager = [Ware("brot", 3), Ware("salz", 1), Ware("brot", 7)]
ziel = lager[2]
lager.remove(ziel)          # entfernt GENAU dieses, nicht das erste "brot"
print(lager)                # [Ware('brot', 3), Ware('salz', 1)]
```

Stimmte deine Vorhersage? Wenn du das erste „brot" erwartet hast, hast du nach dem **Wert** gedacht statt nach dem **Ding** — genau der Sprung, um den es in dieser Portion geht.

**Genau gesagt sucht `remove()` nach einem Eintrag, der mit dem übergebenen *gleich* ist.** Solange eine Klasse nicht selbst festlegt, wann zwei ihrer Objekte als gleich gelten — und deine tut das nicht —, ist jedes Objekt nur sich selbst gleich. Deshalb trifft es hier zuverlässig genau das gemeinte.

Der Umweg über `.pop(i)` und rückwärts laufende Schleifen aus Etappe 6 entfällt — nicht, weil du einen Trick gelernt hast, sondern weil das Problem nicht mehr existiert.

*(Das ist übrigens die Objektidentität aus Etappe 10, von ihrer nützlichen Seite. Dort war „zwei Namen, ein Objekt" eine Fehlerquelle. Hier ist „dieses eine Objekt" genau das, was du brauchst.)*

### 3. Die Schleifenvariable wirkt jetzt ⚠️

Das hier ist neu, und es widerspricht etwas, das du in Etappe 4 gelernt hast:

```python
zahlen = [7, 4, 2]
for z in zahlen:
    z -= 1
print(zahlen)          # [7, 4, 2]  — nichts passiert
```

Das kennst du: Die Schleifenvariable ist eine Kopie des Werts, Zuweisen daran ändert die Liste nicht. Deshalb hast du in Etappe 4 mit `range(len(...))` und Index gearbeitet.

**Bei Objekten ist es anders:**

```python
for w in lager:
    w.menge -= 1       # verändert das Objekt selbst
print(lager)           # alle Mengen sind gesunken
```

> **Der Unterschied: `z -= 1` weist der Variablen etwas Neues zu. `w.menge -= 1` verändert das Ding, auf das die Variable zeigt.**

⚠️ **Die falsche Regel, die man daraus ziehen könnte, lautet: *bei Objekten wirkt die Schleife, bei Zahlen nicht*.** Das stimmt nicht. **Die Schleifenvariable ist in beiden Fällen nur ein Name.** Entscheidend ist, was du damit tust: einen Namen auf etwas Neues zeigen zu lassen ändert die Liste nie; ein veränderbares Objekt zu verändern wirkt immer, auch außerhalb der Schleife. Das ist „Name zeigt auf Wert" aus Etappe 4, unverändert.

Das ist wieder „Name zeigt auf Wert" aus Etappe 4 — nur diesmal von der praktischen Seite. Deine Bewegungslogik wird dadurch einfacher: Aus `for i in range(len(gegner)): gegner[i] -= 1` wird `for g in gegner: g.entfernung -= 1`.

⚠️ **Was sich dabei *nicht* ändert:** Du darfst weiterhin keine Einträge entfernen, während du über die Liste läufst. Das ist derselbe `RuntimeError`-Bereich wie in Etappe 5. Lauf über eine Kopie (`.copy()` aus Etappe 4) oder sammle erst und entferne danach.

### 4. Der Zugriff auf ein Feld

Alles, was vorher über zwei Listen ging, geht jetzt über einen Punkt:

| Vorher | Nachher |
|---|---|
| `gegner[i]` | `gegner[i].entfernung` |
| `gegner_typen[i]` | `gegner[i].typ` *(wird in 11b zu `.name`)* |
| `min(gegner)` | *(braucht mehr — siehe unten)* |

⚠️ **Eine Stelle wird schwieriger, und das ist ehrlich zu sagen:** `min(gegner)` funktionierte auf einer Zahlenliste. Auf Objekten weiß Python nicht, wonach es vergleichen soll. Du brauchst dort eine kleine Schleife, die den Gegner mit der kleinsten Entfernung sucht — mit den Werkzeugen aus Etappe 3 und 4 in vier Zeilen zu bauen.

*(Es gibt dafür eine Einzeiler-Lösung mit `min(..., key=...)`. Die kommt in Etappe 23a, zusammen mit den Comprehensions. Heute baust du die Schleife — sie ist lesbarer, solange du das andere nicht kennst.)*

---

## Dein Auftrag — Teil 11a

### 1. Zieh den Beweis

```bash
python spiel.py < befehle.txt > vorher.txt
```

Ergänz `befehle.txt` um alles, was seit Etappe 10 dazugekommen ist. **Ohne diese Datei fängst du nicht an.**

---

### 2. Erweitere die `Gegner`-Klasse aus Etappe 9a

- Attribute: `typ`, `entfernung`, `trefferpunkte`, `schaden`.

*(`typ` hält, was bisher in `gegner_typen` stand: `"kriecher"`, `"speier"`. In 11b bekommt dieses Attribut einen anderen Namen — dort erfährst du, warum. Bau es heute so.)*
- Ein `__repr__`, das Typ und Entfernung zeigt. Kurz halten — du druckst gleich Listen davon.

**So prüfst du es:** In einer Wegwerf-Datei drei Gegner erzeugen und die Liste drucken. Lesbar?

---

### 3. Ersetz die zwei Listen durch eine

- Dort, wo eine Welle Gegner erzeugt, entstehen jetzt `Gegner`-Objekte.
- `gegner_typen` wird **gelöscht**, nicht auskommentiert.

**So prüfst du es:** Das Spiel startet. Ein `NameError` auf `gegner_typen` ist der freundliche Fall — er zeigt dir die nächste Stelle.

---

### 4. Zieh alle Zugriffsstellen nach

Die Fahndung aus Etappe 5, drittes Mal. Such nach `gegner` und `gegner_typen`.

- Zähl die Treffer **vorher** und schreib die Zahl auf.
- Nach jedem einzelnen ausführen.
- Achte besonders auf: Anmarschbahn, Feuern, Bewegung, Statusanzeige, Wellenende.

**So prüfst du es:** Kein `NameError`, kein `TypeError`. Die Anmarschbahn zeigt dieselben Positionen wie vorher.

---

### 5. Bau das Entfernen um

- Der erlegte Gegner wird jetzt mit `remove(objekt)` entfernt — kein Index-Abgleich, keine zweite Liste.
- Läuft das Entfernen bei dir in einer Schleife über dieselbe Liste? Dann läuft die Schleife über eine **Kopie**.

**So prüfst du es:** Erleg mehrere Gegner in einer Runde. Verschwinden genau die richtigen?

---

### 6. ⭐ Schreib auf, was jetzt unmöglich ist

Zwei Sätze in `GELERNT.md`:

- Welche **zwei** Fehlerarten aus Etappe 6 können in deinem Code jetzt nicht mehr entstehen?
- Welche der beiden war die gefährlichere, und warum?

**Das ist der wichtigste Auftragsschritt dieser Portion.** Der Umbau ist Handwerk; die Erkenntnis ist der Ertrag.

---

### 7. Beweis und Commit

```bash
python spiel.py < befehle.txt > nachher.txt
diff vorher.txt nachher.txt
```

**Kein Unterschied.** Commit: `Etappe 11a: Zwei Gegnerlisten werden eine`

> **⏸ Guter Schnitt.** Dein Spiel läuft wie vorher, und eine fünf Etappen alte Schuld ist bezahlt. 11b ist ein eigener Abend.

---

# Teil 11b — Vererbung und der Trupp

## Worum es geht

Du hast jetzt zwei Klassen, die sich verdächtig ähneln:

```python
class Marine:
    def __init__(self, ...):
        self.trefferpunkte = 100
        self.schaden = 10
        # ...

class Gegner:
    def __init__(self, ...):
        self.trefferpunkte = 20
        self.schaden = 5
        # ...
```

Beide haben Trefferpunkte. Beide haben Schaden. Beide können getroffen werden, beide können sterben. **Der Code, der einen Treffer verrechnet, sieht für beide gleich aus — und steht bei dir vermutlich zweimal da.**

> **Vererbung sagt: Das Gemeinsame wird einmal geschrieben, an einer Stelle, die beide benutzen.**

Und heute passiert noch etwas Größeres. Seit Etappe 2 wählst du eine Spielerklasse, und eine `if`/`elif`-Kette setzt Werte. **Drei der vier Klassen kamen dabei nie zur Anwendung** — sie waren Zweige, die nie liefen.

**Ab heute existieren alle vier gleichzeitig.** Vier Marines stehen nebeneinander: der, den du gewählt hast, und drei Kameraden. Das ist der **Trupp**, und er ist die Prämisse des Spiels — du bist eine Figur im Gefecht, kein Bauherr über der Karte.

---

## Die Konzepte — Teil 11b

### 5. „Ist ein" — jetzt die andere Seite ⭐

In Etappe 10 hast du gelernt: *Ein Marine **hat** ein Inventar.* Heute die Gegenprobe:

| | Frage | Beispiel |
|---|---|---|
| **Komposition** — „hat ein" | Was **besitzt** es? | Ein Fahrzeug **hat** einen Motor |
| **Vererbung** — „ist ein" | Was **ist** es? | Ein Auto **ist** ein Fahrzeug |

**Sag den Satz laut, das ist die ganze Probe.** *„Ein Auto ist ein Fahrzeug"* — stimmt. *„Ein Fahrzeug ist ein Motor"* — Unsinn.

Für dein Spiel: *„Ein Soldat ist ein Marine"* — stimmt. *„Ein Marine ist eine Einheit"* — stimmt. *„Ein Gegner ist eine Einheit"* — stimmt auch. Damit hast du deine Hierarchie.

⚠️ **Und die Gegenprobe, die du gleich brauchst:** *„Ein Inventar ist eine Ausrüstung"*? Nein. Beide sind Behälter, aber mit verschiedenen Regeln — Liste mit Obergrenze gegen feste Rollen. **Das bleibt deshalb ohne gemeinsame Basisklasse**, und es ist das Beispiel, an dem du siehst, dass Ähnlichkeit allein nicht reicht.

### 6. `class Kind(Eltern):`

Die Syntax ist ein Klammerpaar:

```python
class Fahrzeug:
    def __init__(self, name, raeder):
        self.name = name
        self.raeder = raeder
        self.km = 0

    def beschreibe(self):
        return f"{self.name} mit {self.raeder} Rädern"


class Fahrrad(Fahrzeug):        # ← Fahrrad ist ein Fahrzeug
    def __init__(self, name):
        super().__init__(name, 2)
```

Ein `Fahrrad` hat jetzt `name`, `raeder`, `km` und `beschreibe()` — **ohne dass eines davon in `Fahrrad` steht.** Es erbt sie.

**Die Begriffe, damit du fremde Erklärungen lesen kannst:** `Fahrzeug` ist die **Oberklasse** (auch: Basisklasse, Elternklasse). `Fahrrad` ist die **Unterklasse** (auch: abgeleitete Klasse, Kindklasse). Vier Wörter für zwei Dinge — such dir aus, welche du benutzt, aber erkenn alle.

### 7. `super().__init__()` — die Basis zuerst ⭐

```python
class Auto(Fahrzeug):
    def __init__(self, name, sitze):
        super().__init__(name, 4)     # zuerst: was jedes Fahrzeug braucht
        self.sitze = sitze            # dann: was nur ein Auto hat
```

**Vereinfacht gesagt:** `super()` gibt dir den nächsten Teil der Vererbungskette. In einer einfachen Hierarchie wie deiner ist das die Klasse darüber. `super().__init__(name, 4)` ruft also die `__init__` von `Fahrzeug` auf und lässt sie ihre Arbeit tun — `name`, `raeder` und `km` setzen.

**Zwei Dinge daran musst du dir merken:**

**Erstens: In diesem Projekt steht `super().__init__()` zuerst.** Das ist eine **Verabredung, keine Sprachregel** — Python erlaubt den Aufruf auch später, und du wirst fremden Code sehen, der erst etwas berechnet und dann aufruft. Wir machen es zuerst, weil danach alles da ist, worauf du aufbauen willst.

**Zweitens: Was der Konstruktor der Oberklasse setzt, wird nicht gesetzt, wenn du ihn nicht aufrufst.** Vergisst du den Aufruf, fehlen dem Objekt genau die Attribute, die dort entstanden wären:

```
AttributeError: 'Auto' object has no attribute 'name'
```

⚠️ **Das ist eine der irreführendsten Fehlermeldungen für Anfänger.** Sie zeigt auf die Stelle, an der du `name` *liest* — der Fehler steckt in `__init__`, oft dreißig Zeilen weiter oben. Genau das Muster aus Etappe 8: **Die Absturzstelle ist nicht die Fehlerstelle.**

*(Beachte auch, dass `Auto` die `4` selbst setzt. Der Aufrufer sagt nicht, wie viele Räder ein Auto hat — die Klasse weiß es. Das ist derselbe Gedanke wie „die Regel wandert zum Ding" aus Etappe 10.)*

### 8. Methoden überschreiben ⭐

Eine Unterklasse kann eine geerbte Methode ersetzen, indem sie eine mit demselben Namen definiert:

```python
class Auto(Fahrzeug):
    def __init__(self, name, sitze):
        super().__init__(name, 4)
        self.sitze = sitze

    def beschreibe(self):                        # überschreibt die geerbte
        return f"{super().beschreibe()}, {self.sitze} Sitze"
```

`super().beschreibe()` ruft die Fassung der Oberklasse auf und baut darauf auf. Du kannst sie auch ganz ignorieren und etwas völlig anderes zurückgeben — dann steht `super()` eben nicht drin.

**Und jetzt der Moment, um den es geht:**

```python
flotte = [Auto("Kombi", 5), Fahrrad("Hollandrad"), Auto("Kleinwagen", 4)]

for f in flotte:
    print(f.beschreibe())
```

```
Kombi mit 4 Rädern, 5 Sitze
Hollandrad mit 2 Rädern
Kleinwagen mit 4 Rädern, 4 Sitze
```

> **Eine Schleife, ein Methodenaufruf — und jedes Objekt tut das Richtige, ohne dass irgendwo eine Abfrage steht, was es ist.**

**Das ist der Punkt, an dem die `if`/`elif`-Kette aus Etappe 2 stirbt.** Sie hat neun Etappen lang gefragt *„welche Klasse ist das?"*. Ab heute fragt niemand mehr — jedes Objekt weiß es selbst.

### 9. Die vier Marine-Klassen — der Unterschied ist die Fähigkeit ⭐

Deine vier Spielerklassen unterscheiden sich bisher nur in Zahlen. **Ab heute unterscheiden sie sich in dem, was sie *tun*** — und das ist der eigentliche Grund, sie zu Klassen zu machen.

Jede bekommt eine Methode `faehigkeit_einsetzen()`, und jede überschreibt sie:

| Klasse | Klassengerät aus Etappe 2 | Was die Methode heute tut |
|---|---|---|
| Soldat | Sturmgewehr | gibt eine Meldung über den Granatwerfer aus |
| Heavy | Schweres MG | gibt eine Meldung über den Durchschlag aus |
| Engineer | Multiwerkzeug | gibt eine Meldung über den Geschützturm aus |
| Medic | Bio-Injektor | gibt eine Meldung über die Heilung aus |

⚠️ **Ob diese vier Unterklassen am Ende die beste Architektur sind, entscheiden wir heute noch nicht.** Du baust sie zuerst, damit du Vererbung an einem echten Problem beurteilen kannst — **die Entscheidung fällt in 11c.** Zieh daraus also nicht die Regel *„Vererbung heißt: vier Klassen bauen"*.

⚠️ **Heute gibt jede Methode nur etwas aus.** Keine Wirkung, keine Kosten, keine Abklingzeit, kein Schaden. Das ist **Etappe 18**, und dort braucht es Statuseffekte, schwere Munition und ein Freischaltraster — Stoff von sieben Etappen.

**Warum trotzdem jetzt schon eine Methode?** Weil vier Klassen, die sich nur in Zahlen unterscheiden, kein Argument für Vererbung sind. Vier Klassen, die auf denselben Aufruf verschieden reagieren, sind eines. **Ohne `faehigkeit_einsetzen()` wäre die Frage in 11c gar nicht ehrlich zu stellen.**

### 10. Held und Kamerad auf einer Basisklasse ⭐

Vier Marines stehen nebeneinander. **Einen steuerst du** — den aus Etappe 1. Die anderen drei entscheiden selbst.

> **Für die Vererbung ist das der Glücksfall: Alle vier sind Marines, alle vier haben dieselben Werte und dieselben Methoden. Der einzige Unterschied ist, *woher der Befehl kommt.***

Beim Helden aus `input()`. Bei den anderen — ab Etappe 12 — aus ihrer eigenen `update()`-Methode.

⚠️ **Heute tun die drei Kameraden noch nichts von selbst.** Sie existieren, sie stehen in der Liste, sie haben Trefferpunkte und eine Fähigkeit. Autonom werden sie in Etappe 12, wenn es einen Tick gibt, in dem sie handeln können.

**Ein Attribut reicht heute**, um sie zu unterscheiden — etwa `gesteuert = True` beim Helden. Keine eigene Unterklasse: Ein Held ist kein anderer Marine, er hat nur eine andere Befehlsquelle. *(Das ist wieder die Frage aus Etappe 9: Wem gehört dieser Wert? Er gehört der Figur, nicht ihrer Art.)*

**Und die Frage, die sich aufdrängt:** Wenn alle vier gleichzeitig da sind — wozu dann noch die Klassenwahl aus Etappe 1? **Antwort: Sie bestimmt, wer auf deinen Befehl hört.** Die Klassenwahl ist keine Auswahl aus vier Möglichkeiten mehr, sondern die Wahl deiner Rolle im Trupp.

### 11. 👀 `type(self).__name__` — der Klassenname im `__repr__`

Eine Kleinigkeit, die dir viel Tipparbeit spart. Statt in jeder Unterklasse ein eigenes `__repr__` zu schreiben:

```python
class Fahrzeug:
    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r}, km={self.km})"
```

`type(self)` ist die Klasse des Objekts, `.__name__` ihr Name als String. Ein `Auto` druckt sich damit als `Auto(...)`, ein `Fahrrad` als `Fahrrad(...)` — **eine Methode in der Oberklasse, richtige Namen in allen Unterklassen.**

Du musst das nicht benutzen. Aber du wirst es in fremdem Code sehen, und jetzt weißt du, was es tut.

---

## Dein Auftrag — Teil 11b

### 8. Bau die Klasse `Einheit`

- Attribute: `name`, `trefferpunkte`, `schaden`.
- Methode `nimm_schaden(menge)` — zieht ab und gibt zurück, ob die Einheit noch lebt.
- Ein `__repr__`.

**So prüfst du es:** In einer Wegwerf-Datei eine Einheit erzeugen, Schaden nehmen lassen, drucken.

---

### 9. Lass `Marine` und `Gegner` von `Einheit` erben

- `class Marine(Einheit):` und `class Gegner(Einheit):`
- Beide rufen `super().__init__(...)` **als erste Zeile** ihrer `__init__`.
- Lösch aus beiden alles, was jetzt in `Einheit` steht.

⚠️ **Und hier fällt eine Entscheidung, die du bewusst treffen musst: Was ist der `name` eines Gegners?**

Dein Gegner hat seit 11a ein Attribut `typ` mit Werten wie `"kriecher"`. Die Basisklasse stellt jetzt `name`. **Zwei Attribute für dasselbe wären zwei Wahrheiten über eine Sache** — die Regel aus Etappe 5, unverändert.

**Die Entscheidung für dieses Projekt: Der Typ *ist* der Name des Gegners.** Übergib ihn in `super().__init__()` als `name` und lösch `typ`. Ein Kriecher heißt „Kriecher" — er hat keinen Eigennamen, anders als deine Marines.

**Das kostet dich drei Zeilen**, weil du `typ` gerade erst gebaut hast. Genau deshalb steht es hier: **Es ist billiger, eine Entscheidung nach einem Tag zu korrigieren als nach zehn Etappen** — der Kostengedanke aus Etappe 5, an einem harmlosen Beispiel erlebt.

*(Wenn du deinen Gegnern später Eigennamen geben willst — „Kriecher #3" —, ist das ein **zusätzliches** Attribut, kein Ersatz. Heute nicht.)*

**So prüfst du es:** Das Spiel läuft unverändert. Ein `AttributeError` heißt: `super()` fehlt oder ein Attribut wurde zu früh gelöscht.

---

### 10. Bau die vier Marine-Klassen

- `class Soldat(Marine):`, `Heavy`, `Engineer`, `Medic`.
- **Jede setzt ihre eigenen Werte** — Trefferpunkte, Schaden, Panzerung, Klassengerät — im `super().__init__()`-Aufruf oder danach.
- Nimm die Zahlen aus deiner Tabelle von Etappe 2. Unverändert.

**So prüfst du es:** Erzeug alle vier in einer Wegwerf-Datei und druck sie. Stimmen die Werte mit Etappe 2 überein?

---

### 11. ⭐ Töte die `if`/`elif`-Kette

- Die Kette aus Etappe 2, die Klassenwerte setzt, wird **gelöscht**.
- An ihre Stelle tritt eine Zuordnung von Eingabe zu Klasse — ein Dictionary aus Etappe 5 leistet das in vier Zeilen.
- Die Klassenwahl erzeugt jetzt ein Objekt der passenden Klasse.

**So prüfst du es:** Wähl nacheinander alle vier Klassen. Stimmen die Startwerte jedes Mal?

⚠️ **Sie wird gelöscht, nicht auskommentiert.** Auskommentierter Code ist beim nächsten Fehler ein Verdächtiger — Etappe 8.

---

### 12. Gib jeder Klasse `faehigkeit_einsetzen()`

- In `Marine` eine Fassung, die sagt, dass diese Klasse keine Fähigkeit hat.
- In jeder der vier Unterklassen eine eigene, die **eine Meldung ausgibt** und sonst nichts.
- Bau einen Befehl `faehigkeit`, der sie beim Helden aufruft.

⚠️ **Keine Wirkung. Kein Schaden, keine Heilung, keine Kosten, keine Abklingzeit.** Etappe 18.

**So prüfst du es:** Spiel mit zwei verschiedenen Klassen und ruf `faehigkeit` auf. Kommen verschiedene Meldungen, ohne dass irgendwo eine Abfrage nach der Klasse steht?

---

### 13. ⭐ Erzeug den Trupp

- Eine Liste `trupp` mit **vier** Marine-Objekten: deiner gewählten Klasse und den drei anderen.
- Der gewählte bekommt ein Kennzeichen — etwa `gesteuert = True`.
- Erweiter die Statusanzeige, sodass alle vier mit Namen, Klasse und Trefferpunkten erscheinen.

⚠️ **Die drei anderen handeln heute nicht.** Sie stehen da. Etappe 12 gibt ihnen den Tick.

**So prüfst du es:** `status` zeigt vier Marines. Nur einer ist als gesteuert markiert.

---

### 14. Beweis und Commit

Der `diff` **darf** hier abweichen — die Statusanzeige zeigt jetzt vier Marines. Prüf stattdessen von Hand: Läuft ein voller Durchgang, feuert der Held, sinken Trefferpunkte wie vorher?

Commit: `Etappe 11b: Vererbung und der Trupp`

> **⏸ Guter Schnitt.** Vier Marines stehen im Vorposten, und die `elif`-Kette ist tot.

---

# Teil 11c — Items, Dunder und die Entscheidung

## Die Konzepte — Teil 11c

### 12. Wenn ein String zu dünn wird ⭐

In Etappe 4 hast du eine Notiz angelegt — *„hier war ein String zu dünn"*. Hol sie heraus. Die Frage darin war:

> **Du trägst zwei Medkits. Du benutzt eines. Welches?**

Damals lautete die Antwort: egal, sie sind identisch, es steht zweimal dasselbe Wort in der Liste. **Heute hört diese Antwort auf zu funktionieren.** Sobald ein Medkit halb verbraucht ist und das andere nicht, brauchst du etwas, das mehr ist als ein Wort.

```python
class Item:
    def __init__(self, kennung, name):
        self.kennung = kennung      # "medkit" — womit verglichen wird
        self.name = name            # "Medkit (klein)" — was angezeigt wird
```

**Und damit ist die Design-Entscheidung 1 aus Etappe 4 endlich sauber gelöst.** Damals musstest du dich für *eines* von beidem entscheiden — Kennung oder Anzeigename. Heute trägt ein Objekt **beides**, und die Frage war nie ein Entweder-Oder, sondern ein „noch nicht".

Die Unterklassen tragen, was nur ihre Sorte hat:

| Klasse | Was sie zusätzlich hat |
|---|---|
| `Waffe` | Schaden, Munitionsart |
| `Panzerung` | Schutzwert |
| `Modul` | worauf es wirkt |
| `Verbrauchsgut` | Anzahl der Anwendungen — **das halbe Medkit** |

⚠️ **Der Vorrat bleibt, wie er ist.** Munition und Chitinpanzer sind **Mengen** und stehen weiterhin als Zahlen im `vorrat`-Dictionary aus Etappe 5. Nur **Einzelstücke** werden Objekte. Das ist die Trennung aus Etappe 5 und 6, und sie gilt unverändert.

### 13. 👀 Dunder-Methoden — Lesestoff, keine Übung

⚠️ **Dieser Abschnitt ist ausdrücklich keine Aufgabe.** Du sollst nicht lernen, das zu schreiben. Du sollst beim Lesen fremden Codes wissen, warum dort `for x in trupp:` steht, obwohl `trupp` keine Liste ist.

```python
class Trupp:
    def __len__(self):            # entscheidet, was len(trupp) liefert
    def __contains__(self, x):    # entscheidet, was "vasquez" in trupp liefert
    def __iter__(self):           # entscheidet, was for m in trupp: durchläuft
```

Das sind dieselben Haken wie `__init__` und `__repr__` aus Etappe 9: **Python zieht daran, die Klasse hängt etwas dran.** Damit liest sich ein eigenes Objekt wie eine eingebaute Datenstruktur.

> **Ein Satz genügt: Wenn `for x in obj:` funktioniert, obwohl `obj` keine Liste ist, dann hat seine Klasse ein `__iter__`.** Wer das sagen kann, hat diesen Abschnitt erledigt.

**Wer daraus eine Übung macht, verbringt drei Abende mit Dunder-Methoden und einen mit Vererbung — und genau andersherum wäre richtig.**

### 14. 👀 `@property` — und die Klammerfalle ⚠️

Eine Methode, die sich beim Aufruf wie ein Attribut liest:

```python
class Ofen:
    def __init__(self, temperatur):
        self.temperatur = temperatur

    @property
    def ist_heiss(self):
        return self.temperatur > 200

ofen = Ofen(250)
print(ofen.ist_heiss)        # True — ohne Klammern!
```

Die Zeile `@property` darüber verändert, wie die Zeile darunter benutzt wird. *(Solche Zeilen heißen Dekoratoren; erklärt werden sie in Etappe 23b.)*

⚠️ **Und jetzt die Falle, die du im Kaputtmachen selbst auslöst — sie hat zwei Seiten:**

| | Ohne Klammern | Mit Klammern |
|---|---|---|
| **Mit `@property`** | richtig | `TypeError` — **laut, findest du sofort** |
| **Ohne `@property`** | **immer wahr — stiller Typ-3-Fehler** | richtig |

Die gefährliche Ecke ist unten links. `if gegner.am_leben:` bei einer **normalen Methode** ohne Klammern prüft nicht das Ergebnis — es prüft **die Methode selbst**, und die ist wahrheitswertig immer wahr. **Dein `if` gilt damit auch bei einem toten Gegner**, und nichts stürzt ab.

> **Das ist derselbe Fehler wie in Etappe 9, Konzept 5** — dort als Warnung, hier mit dem Werkzeug, das ihn zur Falle macht. In Etappe 16 ist er ein Hauptverdächtiger.

### 15. ⭐⭐ Die Entscheidung: brauchen wir Vererbung überhaupt?

**Das ist die wichtigste Aufgabe dieser Etappe** — wichtiger als alles, was du heute gebaut hast.

Sieh dir deine vier Marine-Klassen an. Wodurch unterscheiden sie sich?

- Durch **Zahlen** — Trefferpunkte, Schaden, Panzerung.
- Durch **eine Methode**, die je Klasse etwas anderes ausgibt.

**Zahlen sind Daten.** Man könnte sie in ein Dictionary schreiben und hätte vier Zeilen statt vier Klassen. Genau das machst du in Etappe 22 mit den Tabellen.

> **Die Frage lautet also: Wo liegt die Grenze? Wann ist ein Unterschied ein Datensatz, und wann eine Klasse?**

Es gibt keine richtige Antwort, die ich dir vorsagen könnte. **Aber die Frage zu stellen ist der Unterschied zwischen jemandem, der Syntax kann, und jemandem, der Entscheidungen trifft.**

*(Mein Hinweis, wenn du feststeckst: Schau nicht auf die Werte, schau auf das Verhalten. Ein Unterschied, der nur in `schaden` steckt, sieht nach Daten aus. Ein Unterschied, bei dem `faehigkeit_einsetzen()` grundverschiedene Dinge tut, sieht **zunächst** nach Klassen aus — lies danach unbedingt den Absatz zur Komposition weiter unten.)*

**Und eine dritte Möglichkeit, die ich hier nur benenne:** Unterschiedliches Verhalten **zwingt** nicht zu Vererbung. Man kann einem Marine auch ein Fähigkeitsobjekt mitgeben — `Marine + Heilen` statt `Medic`. Das ist **Komposition**, du hast sie in Etappe 10 gebaut, und in echtem Python ist sie häufiger als Vererbung.

**Warum du die Hierarchie trotzdem heute baust:** Nicht weil sie richtiger ist, sondern weil du Vererbung einmal von innen erlebt haben musst, um in Etappe 22 begründet gegen sie entscheiden zu können. **Eine Entscheidung gegen ein Werkzeug, das man nie benutzt hat, ist keine Entscheidung, sondern eine Vermeidung.**

> **Die Lektion dieser Etappe lautet deshalb nicht „unterschiedliches Verhalten → Vererbung", sondern: Vererbung ist eine von mehreren Modellierungsentscheidungen — nicht die automatische Folge davon, dass Objekte sich unterschiedlich verhalten.**

---

## Dein Auftrag — Teil 11c

### 15. Bau die `Item`-Hierarchie

- `Item` mit `kennung` und `name`.
- `Waffe`, `Panzerung`, `Modul`, `Verbrauchsgut` erben davon, jede mit ihren eigenen Attributen.
- `Verbrauchsgut` bekommt `anwendungen` — damit ist die Frage aus Etappe 4 beantwortet.

**So prüfst du es:** Zwei Verbrauchsgüter mit verschiedenen Restanwendungen erzeugen und drucken. Sind sie unterscheidbar?

---

### 16. Stell dein Inventar auf Objekte um

- Aus Strings in `Inventar.gegenstaende` werden `Item`-Objekte.
- Die Prüfung, ob etwas im Inventar ist, vergleicht ab jetzt **Kennungen**, nicht Objekte.
- Die Anzeige nimmt `name`, die Logik nimmt `kennung`.

⚠️ **Die Stelle, an der Alt und Neu aufeinanderprallen:** Deine Liste enthält jetzt `Item`-Objekte, aber der Spieler tippt weiterhin einen String. `"medkit" in inventar.gegenstaende` findet deshalb **nichts** — du vergleichst einen String mit Objekten. **Der Vergleich muss über `.kennung` jedes Eintrags laufen**, nicht über den Eintrag selbst. Eine Schleife aus Etappe 3 reicht dafür.

*(Das ist derselbe Fehler wie `min(gegner)` in 11a: Ein eingebautes Werkzeug, das auf Strings oder Zahlen selbstverständlich war, weiß bei deinen Objekten nicht mehr, worauf es schauen soll.)*

⚠️ **Der Vorrat bleibt unangetastet.** Munition und Material sind Mengen, keine Einzelstücke.

**So prüfst du es:** `nimm`, `ablege` und die Inventaranzeige verhalten sich wie vorher. Der Beweis mit `diff` gilt hier wieder.

---

### 17. ⭐⭐ Beantworte die Vererbungsfrage schriftlich

**Zehn Minuten, in `GELERNT.md`, als Entscheidung mit Datum und Begründung — nicht als Notiz.**

- Brauchen deine vier Marine-Klassen wirklich Vererbung, oder wären sie besser vier Zeilen in einer Tabelle?
- **Dieselbe Frage für die `Item`-Hierarchie: Was haben `Waffe`, `Panzerung`, `Modul` und `Verbrauchsgut` tatsächlich gemeinsam — außer `kennung` und `name`?** Gemeinsamer **Zustand** spricht für eine Basisklasse, gemeinsames **Verhalten** spricht stärker dafür, bloß gemeinsame **Attribute** sprechen kaum dafür. In welche der drei Lagen fällt deine?
- Woran hast du das festgemacht — an den Werten oder am Verhalten?
- Was müsste passieren, damit du deine Meinung änderst?

⚠️ **Schreib es auf, auch wenn du unsicher bist.** Du liest es in Etappe 22 wieder, wenn die Tabellen zeigen, wie gut sich Verhalten als Daten ausdrücken lässt — und noch einmal in Etappe 25, wenn du versuchst, deine Klassen nach JSON zu bringen. Dann bewertest du dieselbe Frage mit zwei Monaten Erfahrung neu.

> **Dieser Ablauf — Entscheidung → Erfahrung → Gegenprobe → Revision — ist der Kern dessen, was Softwareentwicklung von Syntaxkenntnis unterscheidet.** Er funktioniert nur, wenn die ursprüngliche Entscheidung aufgeschrieben ist. **Aus dem Gedächtnis rekonstruiert man immer die Entscheidung, die man heute treffen würde.**

---

### 18. Ein Satz zu den Dunder-Methoden

In `GELERNT.md`, ein Satz, keine Übung: *Woran erkennst du beim Lesen, dass ein Objekt iterierbar ist?*

---

### 19. Aufräumen und Commit

- Keine auskommentierte `elif`-Kette, keine `###`-Zeilen, kein `breakpoint()`.
- Commit: `Etappe 11c: Item-Hierarchie und die Vererbungsfrage`

---

## Was NICHT in diese Etappe gehört

**Keine Wirkung für Fähigkeiten.** Sie geben Meldungen aus. Etappe 18.

**Kein autonomes Handeln der drei Kameraden.** Sie stehen da. Etappe 12 gibt ihnen den Tick.

**Keine `update()`-Methode.** Auch Etappe 12.

**Keine `__len__`, `__contains__`, `__iter__` schreiben.** Erkennen genügt — siehe Konzept 13.

**Kein `@property` bauen.** Auch nur erkennen. Wer es heute einbaut, hat morgen eine Klammerfalle mehr im Code und keinen Nutzen.

**Keine gemeinsame Basisklasse für `Inventar` und `Ausruestung`.** Sie sind sich ähnlich und haben verschiedene Regeln — das Beispiel für *„Ähnlichkeit ist kein Grund"*.

**Keine Mehrfachvererbung.** Kommt im ganzen Plan nicht vor.

**Kein Umbau des Vorrats.** Mengen bleiben Zahlen.

---

## Selbsttest

**11a**
- [ ] `gegner_typen` existiert nicht mehr — auch nicht auskommentiert.
- [ ] Die Gegnerliste enthält Objekte, und das Entfernen läuft über `remove(objekt)` ohne Index-Abgleich.
- [ ] `diff vorher.txt nachher.txt` nach 11a zeigt keinen Unterschied.
- [ ] Du kannst die zwei Fehlerarten aus Etappe 6 nennen, die jetzt unmöglich sind.

**11b**
- [ ] `Marine` und `Gegner` erben von `Einheit`, und `nimm_schaden` steht **einmal**.
- [ ] Jede Unterklasse ruft `super().__init__()` als erste Zeile.
- [ ] Ein Gegner hat **entweder** `name` **oder** `typ` — nicht beides. Du kannst sagen, warum.
- [ ] Die `if`/`elif`-Kette aus Etappe 2 ist gelöscht.
- [ ] Vier Marines existieren gleichzeitig, einer ist als gesteuert markiert.
- [ ] `faehigkeit` gibt je nach Klasse Verschiedenes aus — **ohne** dass irgendwo nach der Klasse gefragt wird.

**11c**
- [ ] Das Inventar enthält `Item`-Objekte; die Logik vergleicht Kennungen, die Anzeige zeigt Namen.
- [ ] `"medkit" in inventar.gegenstaende` liefert **nicht** mehr das erwartete Ergebnis — und du weißt, warum, und was stattdessen dasteht.
- [ ] Zwei Verbrauchsgüter mit verschiedenen Restanwendungen sind unterscheidbar.
- [ ] Der `vorrat` enthält weiterhin Zahlen.
- [ ] **Die Vererbungsfrage ist schriftlich beantwortet, mit Datum und Begründung.**
- [ ] Alle drei Commits sind gesetzt.

---

## Lernziele

1. Welche zwei Fehlerarten aus Etappe 6 sind seit 11a **unmöglich**, nicht nur unwahrscheinlich?
2. Warum funktioniert `remove()` bei Objekten wieder, obwohl es bei Zahlen versagt hat?
3. Warum ändert `for g in gegner: g.entfernung -= 1` die Liste, `for z in zahlen: z -= 1` aber nicht?
4. **Was macht `super().__init__()` genau — und was passiert, wenn du es weglässt?**
5. Was heißt „Methode überschreiben"?
6. Wie kann eine Schleife über gemischte Objekte das Richtige tun, ohne nach dem Typ zu fragen?
7. Was unterscheidet den Helden von den drei Kameraden — und was gerade *nicht*?
8. Woran erkennst du beim Lesen, dass ein Objekt iterierbar ist?
9. Warum steht bei `@property` beim Aufruf keine Klammer — und welcher der beiden Klammerfehler ist der gefährliche?
10. **Wann ist Vererbung die falsche Wahl?**

**Frage 10 ist die wichtigste** und die einzige ohne richtige Antwort. **Frage 4 ist die, die dich am häufigsten Zeit kosten wird**, wenn du sie nicht beantworten kannst.

---

## Transferaufgabe (15 Minuten)

**Außerhalb des Spiels.** Ein Fuhrpark, kein Vorposten.

1. `Fahrzeug` mit `name`, `raeder`, `km` und `beschreibe()`.
2. `Auto(Fahrzeug)` mit `sitze`, `Fahrrad(Fahrzeug)` ohne Zusatz. Beide rufen `super().__init__()`.
3. `Auto.beschreibe()` überschreibt und benutzt `super().beschreibe()`.
4. Eine Liste mit drei gemischten Fahrzeugen, eine Schleife, ein Aufruf.

**Und dann der eigentliche Teil:**

5. **Nimm `super().__init__()` aus `Auto` heraus.** Sag voraus, was passiert, **bevor** du es ausführst. Wo genau knallt es — in `__init__` oder in `beschreibe()`?
6. Erklär in einem Satz, warum die Fehlermeldung auf die falsche Stelle zeigt. *(Etappe 8, Konzept 4.)*
7. **Frag dich zum Schluss:** Wäre `Fahrrad` als eigene Klasse gerechtfertigt, wenn es sich nur durch `raeder = 2` unterschiede? Zwei Sätze — dieselbe Frage wie in Konzept 15, an einem harmloseren Beispiel.

---

## Kaputtmachen

**Vor jedem: aufschreiben, was passieren wird.**

**1. ⭐ Lass `super().__init__()` weg.** Nimm es aus einer deiner vier Marine-Klassen heraus und starte. Lies den `AttributeError` genau: **Welche Zeile nennt er, und wo sitzt der Fehler wirklich?**

**2. ⭐ Die Klammerfalle, beide Richtungen.** Bau eine Methode `am_leben()`, die `self.trefferpunkte > 0` zurückgibt. Dann:
- `if gegner.am_leben():` — mit Klammern
- `if gegner.am_leben:` — ohne

Setz die Trefferpunkte auf `0` und probier beide. **Eine der beiden lügt.** Welche, und warum stürzt sie nicht ab?

**3. Vergiss das Überschreiben.** Lösch `faehigkeit_einsetzen()` aus einer Unterklasse. Was passiert beim Aufruf — Absturz oder etwas anderes?

**4. Bau die zweite Liste zurück.** Leg testweise wieder ein `gegner_typen` an und halte es *nicht* synchron. Entferne einen Gegner nur aus einer Liste. **Wie lange dauert es, bis etwas Falsches angezeigt wird?** Das ist der Schmerz, den 11a beseitigt hat.

**5. Erzeug zwei Marines derselben Klasse.** Ändere bei einem die Trefferpunkte. Ändert sich der andere mit? *(Wenn ja: Etappe 10, Konzept 6 — und dann hast du in Schritt 13 einen echten Fehler gebaut.)*

---

**Experiment 1 und 2 sind das Paar.** Beide entstehen aus einer vergessenen Kleinigkeit — einmal knallt es sofort, einmal nie. Wer nur eines macht, lernt die halbe Wahrheit.

Alles in `GELERNT.md` und ins Fehlertagebuch aus Etappe 8.

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `AttributeError: object has no attribute 'name'` | `super().__init__()` fehlt oder steht zu spät | Konzept 7 — in der `__init__` der Unterklasse |
| `TypeError: __init__() takes 2 positional arguments but 4 were given` | Die Unterklasse gibt mehr weiter, als die Oberklasse annimmt | Die Parameterliste beider `__init__` nebeneinanderlegen |
| Alle vier Marines haben dieselben Werte | Die Unterklassen setzen nichts Eigenes | Konzept 7 — was steht nach `super()`? |
| `faehigkeit` gibt immer dasselbe aus | Die Unterklassen überschreiben nicht — Tippfehler im Methodennamen | Der Name muss **exakt** übereinstimmen |
| `NameError: gegner_typen` | Eine Zugriffsstelle wurde in 11a übersehen | Auftragsschritt 4 — die Fahndung ist unvollständig |
| `TypeError: '<' not supported between instances of 'Gegner'` | `min(gegner)` auf Objekten | Konzept 4 — eine Schleife, die nach `entfernung` sucht |
| Das `if` ist immer wahr | Klammern bei einer Methode vergessen | Konzept 14 — der stille Typ-3 |
| `RuntimeError` beim Entfernen | Entfernen während der Schleife über dieselbe Liste | Konzept 3 — über eine Kopie laufen |
| Ein Marine ändert sich, alle ändern sich | Geteiltes Objekt | Etappe 10, Konzept 6 — `is` prüfen |
| Die Anmarschbahn zeigt Unsinn | Die Bahn liest noch `gegner[i]` als Zahl | `gegner[i].entfernung` |

**Der Debugging-Reflex dieser Etappe: „Wo steht diese Methode wirklich?"**

Ab heute kann ein Aufruf in drei Klassen stehen — der Unterklasse, der Oberklasse, oder deren Oberklasse. Die Frage aus Etappe 9 bekommt eine vierte Herkunft:

> **Woher kommt dieser Name?** Aus dieser Datei · aus einem `import` · von `self` · **aus einer Oberklasse.**

Im Debugger beantwortet `s` die Frage in einem Schritt: Es springt in die Methode hinein und zeigt dir, in welcher Datei und Zeile sie tatsächlich steht.

---

## Ein Blick nach vorne

**Etappe 12 ist der Tick — und die Ernte dieser Etappe.** Deine `Einheit`-Basisklasse bekommt dort eine `update()`-Methode, und der Tick läuft in einer Schleife über *alle* Einheiten: vier Marines, alle Gegner, später der Geschützturm. **Genau dafür war die gemeinsame Basis da.** Und die drei Kameraden von heute fangen dort an, selbst zu handeln.

**Etappe 13 gibt jeder Fähigkeit eine Abklingzeit.** Deine vier Methoden von heute bekommen ihren Zähler.

**Etappe 14a macht aus `entfernung` ein `(x, y)`.** Deine Gegnerobjekte sind darauf vorbereitet — ein Attribut ändern statt zwei Listen umbauen.

**Etappe 16 ist die Bug-Jagd II**, und die Klammerfalle aus Konzept 14 ist dort ein Hauptverdächtiger.

**Etappe 18 gibt den Fähigkeiten Wirkung** — Granatwerfer, Durchschlag, Minen, Heilaura, alle über `level` freigeschaltet und mit schwerer Munition bezahlt.

**Etappe 22 ist die Gegenprobe zu deiner schriftlichen Antwort.** Dort werden alle Zahlen zu Tabellen, und du siehst, wie viel deiner Klassenhierarchie sich als Daten ausdrücken lässt. **Nimm deine Antwort von heute dann heraus und lies sie, bevor du urteilst.**

**Etappe 25 ist die zweite Gegenprobe.** Objekte nach JSON zu bringen zeigt schonungslos, welche Unterschiede echtes Verhalten waren und welche nur Zahlen.

---

## Abschluss

**In `GELERNT.md`:**

- Wie viele Zugriffsstellen musste ich in 11a anfassen?
- ⭐ Welche zwei Fehlerarten aus Etappe 6 sind jetzt unmöglich?
- Was hat mich überrascht? *(Kandidaten: dass `remove()` plötzlich wieder funktioniert · dass eine Schleife das Richtige tut, ohne nach dem Typ zu fragen · wie kurz die Klassen wurden, nachdem `Einheit` da war.)*
- Wie fühlte es sich an, die `elif`-Kette aus Etappe 2 zu löschen?
- ⭐⭐ **Die Vererbungsfrage — mit Datum und Begründung.**

---

## Wenn du mehr willst

Erst bei grünem Selbsttest.

**Zähl deine Zeilen vor und nach `Einheit`.** Wie viel Code ist verschwunden, weil `nimm_schaden` nur noch einmal existiert? Die Zahl ist überzeugender als jede Erklärung, wozu Vererbung gut ist.

**Bau `type(self).__name__` in das `__repr__` der Oberklasse ein** und druck deinen Trupp. Eine Zeile, vier richtige Klassennamen.

**Schreib die Komposition-Variante auf — nur auf Papier.** Wie sähe dein Medic aus, wenn er statt einer eigenen Klasse ein `Heilen`-Fähigkeitsobjekt bekäme? Kein Code, fünf Zeilen Skizze. Du brauchst sie in Etappe 22.

**Such in fremdem Code nach `super().__init__()`** und sieh nach, ob es die erste Zeile ist. Du wirst Ausnahmen finden — und jede hat einen Grund, den du jetzt suchen kannst.

---

> **Nächste Etappe:** Etappe 12 — Der Tick · die Zeit läuft weiter, auch wenn du nichts tust, und drei Kameraden fangen an zu handeln
