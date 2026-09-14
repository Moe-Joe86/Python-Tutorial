# Etappe 10 — Komposition

*v1.1.0 · 2026-09-08*

> **Block 2: Einheiten und Zeit** · Etappe 10 von 30 · [← Etappe 9](etappe-09-alles-wird-zum-objekt.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 11 →](etappe-11-vererbung.md)

**Neue Syntax heute:** Objekte als Attribute anderer Objekte · `None` als bewusster Leerwert · `is None` und `is not None` · `self.position` als Tuple · 👀 `is` gegen `==` · 👀 Komposition als Begriff

**Zeitaufwand:** 4–5 Sitzungen à 20–30 Minuten. Rund 30 Minuten davon sind Lesestoff. **Die Etappe ist kleiner als 9** — der Umbau ist überschaubar, und die Zeit steckt im Kaputtmachen, wo sie hingehört.

**Voraussetzung:** Etappe 9 abgeschlossen, Selbsttest grün. Dein Marine ist ein Objekt mit Attributen und Methoden.

⚠️ **Der wichtigste Teil dieser Etappe steht nicht im Auftrag.** Was du baust, sind zwei kleine Klassen — eine Stunde Arbeit. Was du *lernst*, ist die Antwort auf die Frage, warum sich manchmal zwei Dinge gleichzeitig ändern, die du nie zusammen angefasst hast. Das ist der Stoff, der dich in Etappe 16 einen Fehler in zehn Minuten statt in zwei Stunden finden lässt.

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **Werkzeuge** | `Inventar` und `Ausruestung` als eigene Klassen · Slots mit `None` · `is None` · `self.position` als Tuple | **Zwei Namen, ein Objekt** · `None` ≠ `0` · wo `Inventar()` steht, entscheidet alles | `is` gegen `==` · Komposition als Begriff |
| **Denken** | „hat ein" gegen „ist ein" · der Reflex *„sind das überhaupt zwei Dinge?"* | Warum Komposition vor Vererbung kommt | Warum diese Fehler nie abstürzen |

---

## Worum es geht

Dein Marine hat seit Etappe 9 eine Liste als Inventar:

```python
self.inventar = ["medkit", "datenkern"]
```

Das funktioniert, und heute reißt du es trotzdem auseinander. Der Grund steht in deinem eigenen Code, und du hast ihn in Etappe 4 schon einmal notiert.

**Frag dich:** Was passiert, wenn dein Inventar voll ist? Irgendwo in deinem Programm steht eine Zeile wie `if len(marine.inventar) < 10`. Die Zahl 10 steht dort, wo das Inventar **benutzt** wird — nicht dort, wo es **wohnt**. Und wenn du morgen einen Rucksack einführst, der zwölf Plätze hat, musst du jede dieser Stellen suchen.

> **Das ist der Kern: Eine Liste weiß nichts über sich selbst. Sie kennt ihre eigene Obergrenze nicht, ihre eigenen Regeln nicht, ihren eigenen Namen nicht.**

Ein `Inventar`-Objekt weiß das alles. Es kennt seine Kapazität, es kann selbst entscheiden, ob noch etwas hineinpasst, und es kann `False` zurückgeben, wenn nicht. Die Regel wandert dorthin, wo die Daten sind.

**Das heißt Komposition, und der Satz dazu lautet:**

> **Ein Marine *hat* ein Inventar. Er *ist* kein Inventar.**

Das klingt selbstverständlich. In Etappe 11 wirst du sehen, dass es das nicht ist — dort stellst du dieselbe Frage für Soldat und Marine, und dort lautet die Antwort anders.

**Und der eigentliche Stoff kommt als Nebenwirkung.** Sobald deine Objekte andere Objekte enthalten, kann derselbe Gegenstand an zwei Stellen hängen — und dann verändert sich etwas an einer Stelle, die du nie angefasst hast. Das ist kein exotischer Sonderfall, sondern der häufigste schwer findbare Fehler in objektorientiertem Python.

---

## Der lange Bogen — was heute fällig wird

- **Das Aliasing aus Etappe 4** — `b = a`, und beide ändern sich — kommt heute an eigenen Objekten zurück und bekommt seinen Namen: **Objektidentität**. Damals war es eine Kuriosität an einer Liste. Heute ist es die Ursache eines Fehlers, der dein Spiel kaputt macht, ohne abzustürzen.
- **`.copy()` aus Etappe 4** wird heute vom Werkzeug zur Schutzmaßnahme.
- **Truthy und Falsy aus Etappe 4** — besonders die `0` — bekommen heute ihre gefährliche Seite: `None` und `0` sind beide „falsch", aber sie bedeuten Gegenteiliges.
- **Die Standardwerte aus Etappe 7** treffen heute auf veränderbare Objekte, und daraus entsteht der berühmteste Stolperstein der Sprache.
- **Das Tuple aus Etappe 6** wird heute zur Position — die erste Stelle, an der du eines wirklich brauchst.
- **Die Notiz aus Etappe 4** (*„hier war ein String zu dünn"*) wird heute zur Hälfte eingelöst. Die andere Hälfte ist Etappe 11.
- **Die `__repr__` aus 9b** zeigt heute, was sie wert ist: Ein Objekt, das ein Objekt enthält, ist ohne sie im Debugger unlesbar.

---

## Vor dem Umbau: drei Fragen ⭐

| Frage | Antwort |
|---|---|
| **Was bleibt gleich?** | Jede Zahl, jede Meldung, jedes Verhalten. Der Spieler merkt nichts. |
| **Was ändert sich nur in der Darstellung?** | Nichts. |
| **Was ändert sich wirklich am Datenmodell?** | Zwei Attribute werden von einfachen Werten zu **Objekten**. Die Regeln, die bisher verstreut im Code standen, ziehen zu ihnen um. |

**Das ist der dritte reine Umbau des Plans**, nach 7 und 9. Also gilt wieder: `befehle.txt`, `diff`, und jede Abweichung ist ein Fehler.

---

## Die Konzepte

Alle Beispiele laufen **außerhalb** deines Spiels — eine Bäckerei, eine Werkstatt.

### 1. „Hat ein" gegen „ist ein" ⭐

Zwei Arten, wie Klassen zusammenhängen können. Heute baust du die eine, in Etappe 11 vergleichst du sie mit der anderen:

| | Frage | Beispiel |
|---|---|---|
| **Komposition** — „hat ein" | Was **besitzt** dieses Ding? | Ein Bäcker **hat** ein Regal |
| **Vererbung** — „ist ein" | Was **ist** dieses Ding? | Ein Konditor **ist** ein Bäcker |

**Die Probe ist der Satz selbst.** Sag ihn laut: *„Ein Marine ist ein Inventar"* klingt falsch, weil es falsch ist. *„Ein Marine hat ein Inventar"* klingt richtig. Dein Sprachgefühl entscheidet hier zuverlässiger als jede Regel.

⚠️ **Und die Reihenfolge im Plan ist Absicht.** Die meisten Einführungen beginnen mit Vererbung, weil sie sich spektakulär anfühlt. In echtem Python ist Komposition häufiger, einfacher zu debuggen und flexibler. **Wenn du nur eines von beiden wirklich beherrschst, sollte es dieses sein** — und deshalb steht Etappe 11 danach und stellt dort ausdrücklich die Frage, ob Vererbung überhaupt gebraucht wird.

### 2. Ein Objekt als Attribut

Technisch ist das nichts Neues. Ein Attribut kann jeden Wert halten — eine Zahl, einen String, ein Dictionary. Und eben auch ein Objekt:

```python
class Regal:
    def __init__(self, faecher):
        self.faecher = faecher
        self.inhalt = []

class Baecker:
    def __init__(self, name):
        self.name = name
        self.regal = Regal(3)      # hier entsteht ein neues Regal
```

`Regal(3)` in der `__init__` des Bäckers heißt: **Jedes Mal, wenn ein Bäcker entsteht, entsteht auch ein Regal.** Sein eigenes.

Der Zugriff ist zwei Punkte statt einem:

```python
ada = Baecker("Ada")
print(ada.regal.faecher)        # 3
ada.regal.inhalt.append("brot")
```

**Lies das von links nach rechts:** `ada` ist ein Bäcker, `.regal` holt sein Regal heraus, `.faecher` holt dessen Kapazität. Jeder Punkt geht eine Ebene tiefer.

### 3. Die Regel zieht zum Ding ⭐

Das ist der Gewinn, um den es geht. Vorher stand die Kapazitätsprüfung dort, wo eingeräumt wurde:

```python
if len(ada.regal.inhalt) < 3:      # die 3 steht im falschen Haus
    ada.regal.inhalt.append("brot")
```

Nachher steht sie im Regal selbst:

```python
class Regal:
    def __init__(self, faecher):
        self.faecher = faecher
        self.inhalt = []

    def einraeumen(self, ware):
        """Legt eine Ware ins Regal. Gibt False zurück, wenn kein Platz ist."""
        if len(self.inhalt) >= self.faecher:
            return False
        self.inhalt.append(ware)
        return True
```

Und der Aufruf wird zu einer Zeile, die keine Zahl mehr kennt:

```python
if not ada.regal.einraeumen("brot"):
    print("Kein Platz mehr.")
```

> **Wer die Kapazität ändern will, ändert eine Zahl an einer Stelle. Vorher waren es alle Stellen, an denen eingeräumt wird.**

Das ist derselbe Gedanke wie *nachschlagen statt abfragen* aus Etappe 5 und wie der Architekturtest dort: **Die Logik soll die konkreten Werte nicht kennen.** Nur diesmal wandern nicht die Daten in eine Tabelle, sondern die Regel zu den Daten.

**Und beachte den Rückgabewert.** `einraeumen` gibt `True` oder `False` zurück, statt selbst etwas auszugeben. Das ist die Trennung aus Etappe 7b: Das Regal entscheidet, der Aufrufer redet. Ein Regal, das `print` sagt, funktioniert nicht mehr, sobald du dieselbe Prüfung stumm brauchst.

### 4. `None` — bewusst nichts ⭐

Bisher hattest du für „nichts" immer irgendeinen Ersatzwert: eine leere Liste, eine `0`, einen leeren String. `None` ist etwas anderes:

> **`None` heißt: hier ist bewusst nichts. Nicht null, nicht leer — nichts.**

Ein Werkzeugplatz ohne Werkzeug ist `None`. Ein Bäcker ohne aktuellen Auftrag hat `None`. Der Unterschied zu `0` ist in deinem Spiel besonders scharf:

| Wert | Bedeutung |
|---|---|
| `munition = 0` | **Es gibt eine Waffe.** Sie ist leer. |
| `waffe = None` | **Es gibt keine Waffe.** |

Das sind zwei völlig verschiedene Zustände, und sie brauchen verschiedene Meldungen: *„Nachladen!"* gegen *„Du hast keine Waffe."* Wer beides gleich behandelt, baut einen **Typ-3-Fehler** aus Etappe 8 — das Programm läuft und sagt etwas Falsches.

⚠️ **Und jetzt die Falle, wegen der das gefährlich ist.** Erinnerst du dich an Truthy und Falsy aus Etappe 4? Beide Werte sind „falsch":

```python
if not waffe:          # wahr bei None UND bei 0 UND bei "" UND bei []
```

Dieses `if` kann die beiden Fälle **nicht unterscheiden**. Es sieht bei einer leeren Waffe und bei einer fehlenden Waffe dasselbe. Deshalb:

```python
if waffe is None:      # fragt genau eines: ist da nichts?
```

**Nimm `is None`, wenn du wirklich `None` meinst.** Nimm `if not x`, wenn dir „leer oder nichts" tatsächlich reicht. Der Unterschied kostet dich heute nichts und in Etappe 18 einen Abend, wenn eine Fähigkeit mit Kosten `0` sich verhält wie eine ohne Kosten.

### 5. 👀 `is` gegen `==`

Zwei Vergleiche, die fast immer dasselbe Ergebnis liefern und Verschiedenes fragen:

| | Fragt | Antwort bei zwei gleichen Listen |
|---|---|---|
| `==` | Haben die beiden **denselben Wert**? | `True` |
| `is` | Sind die beiden **dasselbe Objekt**? | `False` |

```python
a = [1, 2]
b = [1, 2]
c = a

print(a == b)    # True  — gleicher Inhalt
print(a is b)    # False — zwei verschiedene Listen
print(a is c)    # True  — ein Objekt, zwei Namen
```

**Merk dir nur: `is` fragt nach dem Ding, `==` nach dem Wert.** Du benutzt `is` heute an genau einer Stelle — bei `None` — und in Konzept 6, um dir etwas zu beweisen. Für alles andere nimmst du weiterhin `==`.

*(Warum ausgerechnet bei `None` die Identitätsfrage die richtige ist: Es gibt in einem laufenden Python-Programm nur ein einziges `None`. Die Frage „ist das dieses eine Nichts?" ist deshalb genau die richtige — und sie ist die Schreibweise, die jeder Python-Code benutzt.)*

### 6. Zwei Namen, ein Objekt ⭐⭐

**Das ist der Kern dieser Etappe.** Nicht die Klassen, die du baust — das hier.

Du kennst es aus Etappe 4, damals an einer Liste:

```python
a = [1, 2]
b = a          # kein zweiter Behälter — ein zweiter Name für denselben
b.append(3)
print(a)       # [1, 2, 3]  — a hat sich auch geändert
```

Damals war das eine Kuriosität. Heute wird es zu einem Fehler, den du bauen kannst, ohne es zu merken.

**Bau dafür eine zweite Fassung des Bäckers** — eine, die ihr Regal nicht selbst erzeugt, sondern übergeben bekommt:

```python
class Baecker:                       # Variante: das Regal kommt von außen
    def __init__(self, name, regal):
        self.name = name
        self.regal = regal           # kein Regal(3) — es wird nur entgegengenommen
```

Und jetzt der Unterschied:

```python
gemeinsames_regal = Regal(3)

ada = Baecker("Ada", gemeinsames_regal)
bo  = Baecker("Bo",  gemeinsames_regal)

ada.regal.einraeumen("brot")
print(bo.regal.inhalt)      # ['brot']  — Bo hat Adas Brot
```

**Zwei Bäcker, ein Regal.** Nicht zwei Regale mit gleichem Inhalt — **ein** Regal mit zwei Namen. Was der eine hineinlegt, sieht der andere.

> **Die Frage, an der alles hängt: Wo steht `Regal(3)`?**

| Wo es steht | Was passiert |
|---|---|
| **In `__init__`** | Bei jeder Erzeugung entsteht ein **neues** Regal. Jeder hat sein eigenes. |
| **Außerhalb, einmal, und dann übergeben** | Alle bekommen **dasselbe**. |

⚠️ **Und das ist die Sorte Fehler, die nie abstürzt.** Zwei Marines mit demselben Rucksack sind ein völlig funktionsfähiges Programm — nur eben nicht deines. Ein lupenreiner **Typ 3** aus Etappe 8.

> **Der Reflex, den du daraus mitnimmst — und den du in Etappe 16 brauchen wirst:**
>
> **Wenn sich zwei Dinge unerklärlich gemeinsam verändern, frag nicht *„wo wird das falsch gesetzt?"*, sondern *„sind das überhaupt zwei Dinge?"***

Der erste Reflex schickt dich auf die Suche nach einer Zuweisung, die es nicht gibt. Der zweite findet die Ursache in einer Minute — mit `is`, das dir Konzept 5 gerade gegeben hat:

```python
print(ada.regal is bo.regal)      # True → dasselbe Objekt, hier ist der Fehler
```

### 7. Der berühmteste Stolperstein ⚠️⭐

Jetzt die Variante, die dich wirklich erwischt — weil sie aussieht wie normaler Code.

Du kennst Standardwerte aus Etappe 7: `def gruesse(name, anrede="Hallo")`. Das ist bequem. Und mit einem veränderbaren Objekt wird es zur Falle:

```python
class Regal:
    def __init__(self, inhalt=[]):        # ← sieht harmlos aus
        self.inhalt = inhalt

a = Regal()
b = Regal()
a.inhalt.append("brot")
print(b.inhalt)          # ['brot']  ← b hat nie etwas bekommen
```

**Was passiert:** Der Standardwert `[]` wird **einmal** ausgewertet — beim Definieren der Funktion, nicht bei jedem Aufruf. Es gibt also genau **eine** Liste, und jedes Regal ohne eigenes Argument bekommt dieselbe.

⚠️ **Diese Falle ist besonders gemein, weil sie beim ersten Objekt nicht auffällt.** Solange du nur einen Bäcker hast, ist alles in Ordnung. Der Fehler entsteht in dem Moment, in dem du den zweiten erzeugst — und das kann Wochen später sein, in einer ganz anderen Etappe.

**Die Lösung ist eine Zeile:**

```python
class Regal:
    def __init__(self, inhalt=None):      # None als Standardwert
        if inhalt is None:
            inhalt = []                   # frische Liste bei jedem Aufruf
        self.inhalt = inhalt
```

**Warum das hilft, genau gesagt:** `None` ist kein Behälter, den sich zwei Objekte teilen könnten — es ist nur ein **Signal**, das heißt *„es wurde nichts übergeben"*. Die eigentliche Liste entsteht erst danach, in der Zeile `inhalt = []`, und zwar bei **jedem** Aufruf neu. Nicht die Unveränderlichkeit von `None` rettet dich, sondern dass die Liste an einer Stelle entsteht, die jedes Mal ausgeführt wird. Und das `is None` aus Konzept 4 bekommt hier seinen zweiten echten Anlass.

> **Die Regel, kurz: Als Standardwert nie eine Liste, ein Dictionary oder ein Objekt. Immer `None`, und die echte Sache in der ersten Zeile erzeugen.**

### 8. `.copy()` als bewusste Kopie

Manchmal willst du eine Liste von außen entgegennehmen und daraus eine **eigene** machen — damit spätere Änderungen an der ursprünglichen Liste dein Objekt nicht mehr betreffen. Dafür gibt es `.copy()` aus Etappe 4:

```python
class Regal:
    def __init__(self, inhalt):
        self.inhalt = inhalt.copy()       # eigene Liste, nicht die des Aufrufers
```

```python
liste = ["brot"]
r1 = Regal(liste)
r2 = Regal(liste)
r1.inhalt.append("salz")

print(r1.inhalt)      # ['brot', 'salz']
print(r2.inhalt)      # ['brot']
print(liste)          # ['brot']   — unangetastet
```

**Damit hast du drei Werkzeuge gegen geteilte Objekte:** in `__init__` neu erzeugen, `None` als Standardwert, oder eine Kopie ziehen. Welches passt, hängt davon ab, ob das Ding von außen kommen soll.

⚠️ `.copy()` kopiert **eine Ebene tief.** Enthält deine Liste selbst Objekte, teilen sich Original und Kopie diese weiterhin. Das ist heute kein Problem, weil deine Inventareinträge Strings sind. Merk es dir; in Etappe 19 wird es eines.

### 9. Slots — ein Dictionary mit festen Plätzen

Deine Ausrüstung ist kein Stapel, sondern eine feste Zahl von Plätzen:

```python
class Werkbank:
    def __init__(self):
        self.plaetze = {"links": None, "mitte": None, "rechts": None}

    def belegen(self, platz, geraet):
        """Stellt ein Gerät auf einen Platz. False, wenn der Platz besetzt ist."""
        if self.plaetze[platz] is not None:
            return False
        self.plaetze[platz] = geraet
        return True
```

Drei Dinge daran sind der Punkt:

**Die Schlüssel stehen von Anfang an fest**, die Werte sind `None`. Ein leerer Platz ist ein Eintrag mit `None`, kein fehlender Eintrag — dadurch kannst du die Plätze auflisten, auch wenn nichts darauf steht.

**`is not None`** ist die Gegenrichtung zu `is None`. Liest sich wie ein Satz: *ist da etwas?*

⭐ **Und jetzt die Invariante, die diese Klasse zusammenhält.** Seit Etappe 4 schreibst du solche Sätze auf — Bedingungen, die in deinen Daten **immer** wahr sein müssen. Für die Werkbank lautet sie:

> **Jeder Platz existiert immer. Ein belegter Platz enthält ein Gerät, ein leerer enthält `None`. Ein Platz wird nie gelöscht.**

⚠️ **Der Unterschied klingt nach Wortklauberei und ist keiner.** Wenn du gleich `ablegen()` baust, gibt es zwei Wege, einen Platz zu leeren:

```python
self.plaetze["links"] = None      # richtig — der Platz bleibt, er ist leer
del self.plaetze["links"]         # falsch — der Platz existiert nicht mehr
```

Der zweite bricht die Invariante, und zwar **still**. Alles läuft weiter — bis irgendwann `self.plaetze["links"]` einen `KeyError` wirft oder deine Anzeige einen Platz verschweigt, den es geben müsste. **Ein leerer Platz und ein fehlender Platz sind zwei verschiedene Dinge**, genau wie `0` und `None` in Konzept 4.

*(Schreib die Invariante in `GELERNT.md`. Geprüft wird sie nicht — das ist Etappe 20, wo aus solchen Sätzen Prüfungen werden, und Etappe 26, wo daraus Tests werden. Heute genügt, dass sie dasteht.)*

**Der Unterschied zum Inventar** ist der eigentliche Lernstoff: Das Inventar ist eine Liste mit Obergrenze — beliebige Dinge, begrenzte Zahl. Die Werkbank ist ein Dictionary mit festen Rollen — bestimmte Dinge, feste Plätze. **Dieselbe Frage wie in Etappe 6**, nur an eigenen Klassen: Welche Struktur passt zu welcher Art von Sammlung?

### 10. Ein Tuple als Position

```python
self.standort = (0, 0)
```

Zwei Zahlen, die zusammengehören und sich nur gemeinsam ändern — das ist genau der Fall, für den du in Etappe 6 das Tuple kennengelernt hast. Heute brauchst du zum ersten Mal eines.

⚠️ **Es tut heute nichts.** Es wird gesetzt, angezeigt und sonst nirgends abgefragt. **Das ist Absicht** — dieselbe Sorte geplanter Leerlauf wie beim Erfahrungszähler und beim Klassengerät. Das Raster, auf dem eine Position Bedeutung bekommt, ist Etappe 14a. Wer heute Bewegung einbaut, braucht Grenzen, Kollisionen und eine Zeichenfunktion — den Stoff von vier Etappen auf einmal.

*(Warum ein Tuple und keine Liste: Eine Position wird nicht bearbeitet, sondern ersetzt. `(3, 4)` wird zu `(3, 5)`, nicht „an Stelle 1 eine 5 schreiben". Das Tuple sagt genau das — und weil eine Position hier aus zwei Zahlen besteht, kann sie nicht versehentlich geteilt kaputtgehen, anders als alles andere in dieser Etappe.)*

### 11. `__repr__` bei verschachtelten Objekten 🧠

Deine `__repr__` aus 9b bekommt heute eine Bewährungsprobe. Enthält ein Objekt ein anderes, greift die Darstellung des äußeren auf die des inneren zu:

```
Baecker(name='Ada', regal=Regal(faecher=3, inhalt=['brot']), standort=(0, 0))
```

Das funktioniert von selbst — **wenn** die innere Klasse ein `__repr__` hat. Fehlt es, steht mitten in deiner sauberen Zeile plötzlich `<__main__.Regal object at 0x7f3a…>`.

> **Faustregel: Soll ein Objekt in der Darstellung eines anderen lesbar auftauchen, dann lohnt sich für seine Klasse ein eigenes `__repr__`.** Nötig ist es nicht — ohne reißt die innere Klasse nur ein Loch in die Zeile der äußeren.

⚠️ **Und halt sie kurz.** Wenn dein Marine drei Objekte enthält und jedes davon acht Attribute zeigt, ist die Zeile im Debugger unlesbar — und damit wertlos. Zeig im inneren `__repr__` nur, was du beim Fehlersuchen wirklich brauchst.

---

## Dein Auftrag

Nach jedem Schritt ausführen. Nicht nach fünf.

⚠️ **Das hier ist die vollständige Liste.** Zwei kleine Klassen, ein Umbau, ein Beweis. Wenn dir beim Bauen einfällt, dass eine `Waffe` auch ein Objekt sein könnte — schreib es in `GELERNT.md` und lass es. Das ist Etappe 11.

---

### 1. Zieh den Beweis, bevor du etwas anfasst

```bash
python spiel.py < befehle.txt > vorher.txt
```

Ergänz `befehle.txt` um alles, was seit Etappe 9 dazugekommen ist — vor allem `kaufe`, `verkaufe`, `nimm`, `inventar`.

⚠️ **Ohne diese Datei fängst du nicht an.**

---

### 2. Bau die Klasse `Inventar`

- Attribute: `plaetze` (die Obergrenze, bisher deine 10) und `gegenstaende` (die Liste).
- Methode `hinzufuegen(gegenstand)` — gibt `False` zurück, wenn kein Platz ist, sonst `True`.
- Methode `entfernen(gegenstand)` — gibt `False` zurück, wenn der Gegenstand nicht da ist.
- **Keine `print`-Zeile in der Klasse.** Sie entscheidet, der Aufrufer redet.

**So prüfst du es:** Leg in einer Wegwerf-Datei ein `Inventar(2)` an, füll es mit drei Gegenständen. Der dritte muss `False` liefern.

---

### 3. Bau die Klasse `Ausruestung`

- Ein Dictionary `plaetze` mit festen Schlüsseln und `None` als Startwert — etwa `"waffe"`, `"panzerung"`, `"modul"`.
- Methode `anlegen(platz, teil)` — `False`, wenn der Platz besetzt ist.
- Methode `ablegen(platz)` — gibt das Teil zurück und **setzt den Platz auf `None`**. Ist der Platz leer, gib `None` zurück.

⚠️ **Kein `del`.** Der Platz bleibt, er wird nur leer — siehe die Invariante in Konzept 9. Schreib sie in `GELERNT.md`, bevor du die Methode baust.

⚠️ **Das Klassengerät aus Etappe 2 belegt keinen Slot.** Der Medic legt seinen Bio-Injektor nicht ab, um eine Panzerplatte anzuziehen. `klassengeraet` bleibt ein eigenes Attribut am Marine, unverändert seit Etappe 2.

**So prüfst du es:** Leg zweimal hintereinander etwas auf denselben Platz. Der zweite Versuch muss `False` liefern.

---

### 4. Gib beiden Klassen ein `__repr__`

Kurz halten. Beim `Inventar` reichen Belegung und Kapazität, bei der `Ausruestung` die belegten Plätze.

**So prüfst du es:** `print()` auf beide. Steht dort eine lesbare Zeile?

---

### 5. Bau sie in den Marine ein

- In `Marine.__init__`: `self.inventar = Inventar(10)` und `self.ausruestung = Ausruestung()`.
- **Beide werden *in* `__init__` erzeugt** — nicht davor, nicht als Standardwert. Konzept 6 und 7 sagen, warum.
- Dazu `self.position = (0, 0)`.

⚠️ **Die alte Liste muss weg.** Solange `self.inventar` gleichzeitig eine Liste und ein Objekt sein kann, hast du zwei Wahrheiten über dieselbe Sache — dieselbe Regel wie beim Vorrat in Etappe 5.

**So prüfst du es:** `print(marine)` — steht die verschachtelte Darstellung aus Konzept 11 da?

---

### 6. Zieh alle Zugriffsstellen nach

Jetzt die Fahndung, die du aus Etappe 5 kennst. Such nach `inventar` im ganzen File:

- `marine.inventar.append(x)` wird zu `marine.inventar.hinzufuegen(x)`.
- `len(marine.inventar) < 10` verschwindet ersatzlos — die Prüfung steckt jetzt in der Methode.
- `x in marine.inventar` wird zu `x in marine.inventar.gegenstaende`.

**Zähl die Treffer, bevor du anfängst, und schreib die Zahl auf.** Nach jedem einzelnen ausführen.

**So prüfst du es:** Kein `NameError`, kein `AttributeError`, und `nimm` verhält sich bei vollem Inventar wie vorher.

---

### 7. ⭐ Beweis dir die Objektidentität

**In einer Wegwerf-Datei, nicht im Spiel.**

- Erzeug zwei Marines.
- **Schreib zuerst auf, was du erwartest, und begründe es in einem Satz** — bevor du Python startest. Dann erst prüf mit `is`, ob ihre Inventare dasselbe Objekt sind.
- Stimmte deine Vorhersage? Wenn nicht: Was hast du über den Ort der Erzeugung angenommen, das nicht stimmte?
- Leg bei einem etwas ins Inventar und sieh beim anderen nach.
- **Bau es dann absichtlich kaputt:** Erzeug *ein* `Inventar` außerhalb und gib es beiden mit. Prüf noch einmal mit `is`.

**Schreib beide Ergebnisse in `GELERNT.md`.** Das ist die Übung, auf die es heute ankommt.

---

### 8. Zieh den Beweis

```bash
python spiel.py < befehle.txt > nachher.txt
diff vorher.txt nachher.txt
```

**Kein Unterschied.** Wenn doch: halbieren — welche Zugriffsstelle hast du zuletzt geändert?

---

### 9. Aufräumen und committen

- Keine `###`-Zeilen, kein `breakpoint()`, keine Wegwerf-Zeilen in `spiel.py`.
- Steht irgendwo noch eine nackte `10` für die Inventargröße?
- Commit: `Etappe 10: Komposition`

---

## Was NICHT in diese Etappe gehört

**Keine Vererbung.** Nicht andeutungsweise. Etappe 11 stellt die Frage, *ob* du sie brauchst — und die ist wertlos, wenn du sie vorher unbesehen beantwortet hast.

**Keine `Waffe`- und `Gegenstand`-Klassen.** Es ist verlockend, jetzt jeden String zu einem Objekt zu machen. **Deine Inventareinträge bleiben Strings.** Der Moment, in dem ein String zu dünn wird, ist ausdrücklich Etappe 11 — und deine Notiz aus Etappe 4 ist die Begründung dafür.

**Kein zweiter Marine im Spiel.** Du erzeugst heute zwei in einer Wegwerf-Datei, um dir die Objektidentität zu beweisen. Der Trupp ist Etappe 11.

**Keine Bewegung.** `position` wird gesetzt und angezeigt, sonst nichts. Etappe 14a.

**Kein `@property`, keine Getter und Setter.** Attribute liest und schreibst du direkt. Das ist in Python normal und bleibt es.

**Keine Vererbung zwischen `Inventar` und `Ausruestung`**, auch wenn beide „Behälter" sind. Sie haben verschiedene Regeln — und das ist genau das Beispiel, an dem Etappe 11 zeigt, wann Vererbung *nicht* passt.

---

## Selbsttest

- [ ] `diff vorher.txt nachher.txt` zeigt keinen Unterschied.
- [ ] `Inventar` und `Ausruestung` sind eigene Klassen mit eigenen `__repr__`.
- [ ] Die **Prüfung**, ob noch etwas hineinpasst, steht ausschließlich in `Inventar` — im übrigen Code wird nirgends mehr gegen eine Zahl verglichen. *(Dass `Marine` beim Erzeugen `Inventar(10)` sagt, ist richtig: Der Marine gibt die Kapazität vor, das Inventar setzt sie durch.)*
- [ ] Keine der beiden Klassen enthält ein `print`.
- [ ] `Inventar()` und `Ausruestung()` werden **in** `Marine.__init__` erzeugt, nicht davor und nicht als Standardwert.
- [ ] Zwei Marines haben nachweislich verschiedene Inventare — du hast es mit `is` geprüft, nicht angenommen.
- [ ] Ein leerer Ausrüstungsplatz enthält `None`, und du prüfst ihn mit `is None`.
- [ ] `ablegen()` setzt den Platz auf `None` — es benutzt **kein** `del`, und die Invariante steht in `GELERNT.md`.
- [ ] `klassengeraet` ist **kein** Ausrüstungsplatz.
- [ ] `print(marine)` zeigt die inneren Objekte lesbar, nicht als Speicheradresse.
- [ ] Commit ist gesetzt.

---

## Lernziele

In `GELERNT.md`, ohne nachzuschlagen.

1. Was ist der Unterschied zwischen „ist ein" und „hat ein"?
2. Warum kommt Komposition in diesem Plan **vor** Vererbung?
3. **Was passiert, wenn zwei Marines versehentlich dasselbe `Inventar`-Objekt teilen — und woran merkst du es?**
4. Wann ist `0` die richtige Antwort und wann `None`?
5. Warum `is None` statt `== None` oder `if not x`?
6. Was ist der Unterschied zwischen `is` und `==`?
7. **Warum ist `def __init__(self, inhalt=[])` gefährlich, und warum fällt es beim ersten Objekt nicht auf?**
8. Was hat sich für den Spieler geändert?
9. Warum braucht eine Klasse, die in einer anderen steckt, ihre eigene `__repr__`?

**Frage 3 ist die wichtigste** — sie ist der Reflex, den Etappe 16 abfragt.

**Frage 7 ist die kniffligste.** Wer sie beantworten kann, ohne „das ist halt so" zu sagen, hat verstanden, wann Python etwas auswertet.

---

## Transferaufgabe (15 Minuten)

**Außerhalb des Spiels.** Eine Wanderung, kein Vorposten.

1. Schreib eine Klasse `Rucksack` mit `kapazitaet` und `inhalt`. Methode `hinzufuegen(ding)` gibt `True`/`False` zurück.
2. Schreib eine Klasse `Wanderer`, die einen Rucksack **hat** — erzeugt in `__init__`.
3. Gib beiden ein `__repr__`.
4. Erzeug zwei Wanderer, pack bei einem etwas ein, druck beide.

**Und jetzt der eigentliche Teil:**

5. **Sag voraus**, was passiert, wenn du `Rucksack` so änderst: `def __init__(self, kapazitaet, inhalt=[])`. Schreib die Vorhersage auf, **bevor** du es ausführst.
6. Führ es aus. Erzeug **drei** Wanderer und pack bei jedem etwas anderes ein. Was steht am Ende in jedem Rucksack?
7. **Repariere es** mit `None` als Standardwert.
8. Beweis die Reparatur mit `is`: Sind die drei Rucksäcke jetzt drei Objekte?

**Schritt 6 ist der Kern.** Mit zwei Objekten ist der Fehler seltsam, mit drei ist er offensichtlich — und genau deshalb entdeckt man ihn im echten Projekt oft erst spät.

---

## Kaputtmachen

**Vor jedem Experiment aufschreiben, was passieren wird.** Die ersten vier gehören dazu, die letzten zwei sind Kür.

**1. ⭐ Der veränderbare Standardwert.** Schreib `def __init__(self, gegenstaende=[])` in dein `Inventar` und erzeug zwei Marines. Leg bei einem etwas hinein, sieh beim anderen nach.

**Das ist der berühmteste Stolperstein der Sprache.** Beantworte danach: Wie viele Listen gibt es hier, und wann genau ist sie entstanden?

**2. Das geteilte Objekt.** Erzeug ein `Inventar` außerhalb und gib es beiden Marines mit. Vergleich das Verhalten mit Experiment 1 — es sieht gleich aus. **Ist die Ursache dieselbe?**

**3. `None` gegen `0`.** Setz einen Ausrüstungsplatz auf `0` statt `None` und prüf ihn mit `if not platz:`. Dann mit `is None`. Welche der beiden Prüfungen merkt den Unterschied?

**4. `__repr__` im inneren Objekt entfernen.** Nimm die `__repr__` aus `Inventar` heraus und druck den Marine. Was steht jetzt mitten in der Zeile?

---

Die folgenden zwei sind Kür.

**5. Vertausch `is` und `==`.** Schreib `if platz == None:` statt `is None`. Es funktioniert. Warum ist es trotzdem die schlechtere Schreibweise? *(Tipp: Was könnte eine Klasse tun, damit `==` lügt?)*

**6. Setz das Tuple.** Versuch `marine.position[0] = 5`. Lies die Fehlermeldung. Wie änderst du stattdessen die Position — und warum ist das für eine Position sogar richtig?

---

**Experiment 1 und 2 sind das Paar, auf das es ankommt.** Beide erzeugen dasselbe Symptom aus verschiedenen Ursachen. Wer nur eines macht, hält den Standardwert für den einzigen Weg, sich ein geteiltes Objekt einzufangen.

Alles in `GELERNT.md` und ins Fehlertagebuch aus Etappe 8: **woran du es erkannt hättest.**

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `AttributeError: 'list' object has no attribute 'hinzufuegen'` | Eine Stelle benutzt noch die alte Liste | Schritt 6 — die Fahndung ist unvollständig |
| `TypeError: 'Inventar' object is not iterable` | `for x in marine.inventar` statt `.gegenstaende` | Das Objekt ist keine Liste; es *hat* eine |
| Zwei Marines teilen sich alles | `Inventar()` steht nicht in `__init__` | Konzept 6 — wo steht die Erzeugung? |
| Der zweite Marine erbt die Sachen des ersten | Veränderbarer Standardwert | Konzept 7 — `None` als Standardwert |
| `if not platz` reagiert auf leere **und** fehlende Ausrüstung | `0`, `""`, `[]` und `None` sind alle falsy | Konzept 4 — `is None` |
| Mitten in `print(marine)` steht eine Speicheradresse | Der inneren Klasse fehlt `__repr__` | Konzept 11 |
| `TypeError: 'tuple' object does not support item assignment` | Position im Tuple ändern wollen | Konzept 10 — ersetzen statt bearbeiten |
| Das Inventar nimmt mehr als erlaubt | Der Aufrufer prüft nicht den Rückgabewert | Die Methode gibt `False` — jemand muss hinsehen |
| `KeyError` beim Anlegen von Ausrüstung | Ein Platz, den es im Dictionary nicht gibt | Die Schlüssel stehen in `__init__` fest |

**Der Debugging-Reflex dieser Etappe: „Sind das überhaupt zwei Dinge?"**

Etappe 9 fragte *wem gehört dieser Wert*. Heute kommt die Frage davor:

```
(Pdb) p a.inventar is b.inventar     → True heißt: ein Objekt, zwei Namen
```

**Eine Zeile, die eine Fehlersuche beendet, bevor sie anfängt.**

---

## Ein Blick nach vorne

**Etappe 11 ist die Ernte des ganzen Blocks.** Dort steht die Frage, ob du Vererbung überhaupt brauchst — und dein `Inventar` von heute ist die Vergleichsgrundlage: Zwei Behälterklassen, die sich ähneln und *nicht* voneinander erben sollten. Dort wird auch aus deinen Inventar-Strings endlich das, was deine Notiz aus Etappe 4 gefordert hat.

**Etappe 12 gibt die `Welt`.** Was heute noch lose herumliegt — `kern_integritaet`, die Gegner, die Wellennummer — bekommt seinen Besitzer. Und dort zeigt sich, ob deine Antwort auf die Design-Entscheidung aus Etappe 9 trug.

**Etappe 14a macht die Position wirklich.** Aus `(0, 0)` wird eine Stelle auf einem Raster — und dort trifft dich die Objektidentität ein zweites Mal, in ihrer bösesten Form: `[["."] * 5] * 5` erzeugt fünf Namen für **dieselbe** Zeile.

**Etappe 16 ist die Bug-Jagd II**, und geteilte Objekte sind dort ein Hauptkandidat. Der Reflex aus Konzept 6 ist das Werkzeug, mit dem du sie findest.

**Etappe 18 zeigt die `None`-gegen-`0`-Falle in ihrer teuersten Form**, wenn eine Fähigkeit mit Kosten `0` sich verhält wie eine ohne Kosten.

**Etappe 19 speichert deine Objekte** — und dort wird aus `None` ein `null`, und aus der Frage „was ist beim Laden ein neues Objekt und was dasselbe" ein echtes Problem.

**Etappe 22 nennt Komposition als dritten Weg** neben Vererbung und Daten, wenn du entscheidest, was überhaupt eine Klasse sein muss.

---

## Abschluss

**In `GELERNT.md`:**

- Was habe ich gebaut? *(Zwei Klassen — und wieder kein neues Feature.)*
- Was hat mich überrascht? *(Kandidaten: dass der Standardwert nur einmal ausgewertet wird · dass zwei Marines ein Inventar teilen können, ohne dass etwas abstürzt.)*
- **Wie viele Zugriffsstellen musste ich in Schritt 6 anfassen?**
- ⭐ **Das Ergebnis aus Schritt 7:** Was hat `is` gezeigt — vorher und nachdem du es kaputt gebaut hast?
- Welche Regel ist heute vom Code ins Objekt gewandert, und was hat das gespart?

**Vor dem Commit:** `diff` leer? Keine nackte `10` mehr? Kein `print` in den neuen Klassen?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest.

**Gib `Inventar` eine Methode `ist_voll()`.** Eine Zeile, und sie macht deine Aufrufstellen lesbarer. Frag dich danach: Ist das besser als `len(...) >= kapazitaet` an der Aufrufstelle — und warum?

**Bau die Kapazität abhängig von der Spielerklasse.** Der Heavy trägt mehr als der Medic. Zwei Zeilen, und du siehst, wie leicht das jetzt ist, wo die Zahl nur an einer Stelle steht. *(Keine neue Klasse — nur ein anderer Wert beim Erzeugen.)*

**Zeichne dein Objekt auf Papier.** Ein Kasten „Marine", darin zwei kleinere Kästen. Dann zeichne die kaputte Variante: zwei Marine-Kästen, ein Pfeil von beiden auf **denselben** Inventar-Kasten. Das Bild erklärt Konzept 6 besser als jeder Text — und du wirst es in Etappe 14a wiedererkennen.

**Such in fremdem Python-Code nach `=None` in Parameterlisten.** Du wirst es überall finden. Jetzt weißt du, warum.

---

> **Nächste Etappe:** [Etappe 11 — Vererbung, und die Frage, ob wir sie brauchen](etappe-11-vererbung.md) · vier Klassen, der Trupp, und zwei Listen werden eine
