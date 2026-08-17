# Etappe 6 — Liste, Dictionary, Set, Tuple

> **Block 1: Fundament** · Etappe 6 von 30 · [← Etappe 5](etappe-05-die-karte.md) · [Lehrplan](../RPG_Lehrplan.md) · [Etappe 7 →](etappe-07-aufraeumen.md)

**Boot.dev:** Sets, Tuples, Mengenoperationen
**Zeitaufwand:** 4–6 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 5 abgeschlossen, Selbsttest grün

---

## Worum es geht

Diese Etappe baut fast kein neues Feature. Sie tauscht Werkzeuge aus.

Das klingt nach einem schlechten Geschäft — bisher wurde dein Spiel in jeder Etappe größer, heute wird es hauptsächlich *richtiger*. Aber überleg, was du inzwischen mit dir herumträgst: eine Liste für das Inventar, eine für die Gegenstände am Ort, ein Dictionary für die Karte, ein Dictionary für die Ausgänge. Vier Sammlungen, zwei Werkzeuge.

Und drei Probleme, die du bisher nicht lösen konntest:

- Der `karte`-Befehl aus Etappe 5 zeigt **alle** Orte, auch die, wo der Spieler nie war.
- Die lange Ortsbeschreibung erscheint bei jedem Betreten wieder, auch beim zwanzigsten Mal.
- Wenn du „schon gesehen" mit einer Liste speicherst, steht der Dorfplatz nach fünf Besuchen fünfmal drin.

Alle drei haben dieselbe Ursache: **Du hast für ein Mengen-Problem eine Reihenfolge-Struktur benutzt.**

Heute lernst du die zwei fehlenden Werkzeuge kennen — **Set** und **Tuple** — und damit vier statt zwei. Und du lernst die Frage, die davor steht und die dich bis Etappe 29 begleiten wird:

> **Was für eine Art von Sammlung ist das eigentlich?**

Die meisten Anfänger benutzen jahrelang Listen für alles. Es funktioniert ja. Der Unterschied zwischen „funktioniert" und „passt" ist eine der Fähigkeiten, die diese Etappe dir beibringt — und sie zahlt sich in Etappe 14 und 18 in barer Münze aus.

---

## Der lange Bogen

| Was du heute baust | Wo es wieder auftaucht |
|---|---|
| Set für besuchte Orte | **Etappe 14** — `besuchte_felder` in der Mine; **Etappe 18** — der zentrale `flags`-Speicher |
| Tuple für Unveränderliches | **Etappe 10** — `self.position`; **Etappe 14** — Koordinaten `(x, y)` |
| Tuple als Dictionary-Schlüssel | **Etappe 14** — Positionen als Schlüssel nachschlagen |
| Tuple-Unpacking (`for a, b in ...`) | **Etappe 12** — über NPCs und ihre Zustände laufen |
| Sets lassen sich nicht als JSON speichern | **Etappe 19** — eine Design-Entscheidung beim Speicherstand |
| Mengenoperationen (`&`, `|`, `-`) | **Etappe 18** — welche Flags hat der Spieler, welche fehlen |
| Die Frage „welche Struktur passt hier?" | **Etappe 14** — Dorf als Dictionary, Mine als Raster; **Etappe 22** — Rezepte als Daten |
| `RICHTUNGEN` als feste Sammlung | **Etappe 20** — Eingabevalidierung vor der Verarbeitung |

**Acht Schulden werden heute eingelöst** — das ist der Rekord dieses Blocks:

Aus **Etappe 4**: die angekündigte Gegenüberstellung von `in` bei Liste, Set und Dictionary. Und das Set für „schon gesehen", das dort ausdrücklich vertagt wurde.

Aus **Etappe 5**: warum `{}` ein leeres Dictionary ist und wie man ein leeres Set schreibt. Warum ein Dictionary-Schlüssel unveränderbar sein muss — und warum aus demselben Grund keine Liste in ein Set passt. Der `TypeError: unhashable type` aus Experiment 6. Der `karte`-Befehl, der zu viel verrät. Und die Ortsbeschreibung, die beim zweiten Besuch kürzer sein sollte.

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

### Frage 1: Nimm dein eigenes Spiel auseinander

Bevor du irgendetwas Neues lernst, mach eine Bestandsaufnahme. Geh deinen Code durch und trag jede Sammlung ein, die du hast:

| Was | Aktuell | Reihenfolge wichtig? | Duplikate möglich? | Ändert sich? | Sollte sein |
|---|---|---|---|---|---|
| `inventar` | Liste | ? | ? | ? | ? |
| Gegenstände am Ort | Liste | ? | ? | ? | ? |
| `orte` | Dictionary | ? | ? | ? | ? |
| `ausgaenge` | Dictionary | ? | ? | ? | ? |

Füll die Fragezeichen aus, **bevor** du weiterliest. Die letzte Spalte lässt du erstmal frei — nach den Konzepten unten füllst du sie aus.

Das ist keine Fleißaufgabe. Es ist die Übung, um die es in dieser Etappe geht. Und du wirst feststellen, dass manches richtig ist, wie es ist — nicht alles muss ein Set werden.

**Ein Hinweis vorab, damit du nicht überkorrigierst:** Dein Inventar bleibt eine Liste. Die Reihenfolge, in der du Dinge aufgehoben hast, ist eine sinnvolle Information, und zwei Brote sollen zwei Brote bleiben. Ein Set wäre hier die falsche Wahl.

### Frage 2: Was heißt „besucht"?

Klingt trivial, ist es nicht. Zählt ein Ort als besucht, wenn der Spieler ihn **betritt** — oder erst, wenn er sich dort **umsieht**?

Beide Antworten sind vertretbar, und sie erzeugen unterschiedliche Spiele. Wer beim Durchqueren automatisch alles kartiert, bewegt sich schneller. Wer sich umsehen muss, wird zum Erkunden gezwungen.

Die Entscheidung wirkt bis Etappe 14: Dort baust du Nebel des Krieges in der Mine, und dieselbe Frage stellt sich noch einmal — nur dass sie dort über Spannung entscheidet.

Schreib beide Entscheidungen in `GELERNT.md`.

---

## Die Konzepte

### 1. Vier Werkzeuge im Überblick

Bevor die Details kommen, die Landkarte:

| | Liste `[]` | Dictionary `{k: v}` | Set `{}` | Tuple `()` |
|---|---|---|---|---|
| **Wofür** | Reihe von Dingen | Nachschlagen | Menge ohne Duplikate | Feste Zusammenstellung |
| **Reihenfolge** | ja | nach Einfügung | **keine** | ja |
| **Duplikate** | ja | Schlüssel nein | **nein** | ja |
| **Änderbar** | ja | ja | ja | **nein** |
| **`in` sucht** | im Inhalt | im **Schlüssel** | im Inhalt | im Inhalt |
| **`in` ist** | langsam | schnell | **schnell** | langsam |

Zwei Zeilen davon sind fett, weil sie die eigentlichen Unterscheidungsmerkmale sind: Ein Set hat keine Duplikate und keine Reihenfolge. Ein Tuple lässt sich nicht ändern.

**Aber die Tabelle ist nur die halbe Wahrheit.** Eine Datenstruktur ist kein Behälter, den man nimmt, weil er gerade passt. Sie ist eine **Aussage darüber, was an diesen Daten wichtig ist** — und wer deinen Code liest, liest diese Aussage mit:

> Eine **Liste** sagt: *Hier gibt es eine Reihenfolge, und Dinge dürfen mehrfach vorkommen.*
> Ein **Dictionary** sagt: *Hier schlage ich etwas unter einem Namen nach.*
> Ein **Set** sagt: *Hier geht es nur um Zugehörigkeit — ohne Duplikate, ohne Reihenfolge.*
> Ein **Tuple** sagt: *Diese Werte gehören zusammen und ändern sich nicht.*

Deshalb ist die Frage „welche Struktur nehme ich?" keine Syntaxfrage. Es ist eine **Modellierungsentscheidung**: Du entscheidest, was du über deine Daten behauptest. Merk dir das Wort — es beschreibt einen großen Teil dessen, was Programmieren jenseits der Syntax ausmacht.

### 2. Das Set — eine Menge

```python
besuchte_orte = {"dorfplatz", "wiese"}
```

Geschweifte Klammern wie beim Dictionary, aber ohne Doppelpunkte — nur Werte.

**Zwei Eigenschaften, und beide sind der Punkt:**

```python
besuchte_orte = {"dorfplatz", "wiese", "dorfplatz", "dorfplatz"}
print(besuchte_orte)      # {'dorfplatz', 'wiese'}
```

Duplikate verschwinden. Nicht mit einer Fehlermeldung, sondern lautlos — das ist erwünscht. Du musst nie prüfen, ob etwas schon drin ist, bevor du es hinzufügst.

```python
print(besuchte_orte)      # die Reihenfolge kann bei jedem Lauf anders sein
```

Ein Set hat **keine Reihenfolge**. Es gibt kein `set[0]`. Wenn du eine geordnete Ausgabe willst, sagst du das ausdrücklich:

```python
for ort in sorted(besuchte_orte):
    print(ort)
```

Das ist wichtig für deinen `karte`-Befehl: Ohne `sorted()` steht dein Dorf bei jedem Aufruf in einer anderen Reihenfolge da, und das sieht kaputt aus, obwohl es korrekt ist.

### 3. Das leere Set — die Schuld aus Etappe 5

In Etappe 5 stand: *`{}` ist ein leeres Dictionary, nicht ein leeres Set.* Hier ist die Auflösung.

```python
leeres_dict = {}          # Dictionary
leeres_set = set()        # Set
```

Die geschweiften Klammern waren zuerst für Dictionaries vergeben, also brauchte das leere Set eine eigene Schreibweise. Sobald Werte drinstehen, ist es eindeutig: `{"a"}` ist ein Set, `{"a": 1}` ein Dictionary.

**Und genau hier passiert ein Fehler, den du einmal machen wirst:**

```python
besuchte_orte = {}                    # das ist ein DICTIONARY
besuchte_orte.add("dorfplatz")        # AttributeError
```

Die Fehlermeldung sagt dir dann, dass ein Dictionary kein `add()` kennt — und du wunderst dich, warum, weil du doch ein Set gebaut hast. Hast du nicht.

### 4. Hinzufügen und Entfernen

```python
besuchte_orte.add("schmiede")        # hinzufügen
besuchte_orte.discard("schmiede")    # entfernen, egal ob drin oder nicht
besuchte_orte.remove("schmiede")     # entfernen, KeyError wenn nicht drin
```

`add()` statt `append()` — weil nichts angehängt wird, es gibt ja keine Reihenfolge.

**Der Unterschied zwischen `discard()` und `remove()` ist eine Design-Entscheidung im Kleinen**, dieselbe wie bei `[]` und `.get()` in Etappe 5: Ist das Fehlen ein Fehler oder ein Normalfall? Bei einer Liste hattest du diese Wahl nicht — dort stürzt `remove()` immer ab, und du musstest mit `in` vorbauen.

Und das Beste: `add()` mit etwas, das schon drin ist, tut einfach nichts. Kein Fehler, keine Prüfung nötig. Vergleich das mit dem, was du für dieselbe Sache mit einer Liste schreiben müsstest:

```python
if ort not in besuchte_orte:      # Liste: Prüfung nötig
    besuchte_orte.append(ort)

besuchte_orte.add(ort)            # Set: fertig
```

### 5. Das `in`-Experiment — die Schuld aus Etappe 4 und 5

Mach das wirklich. Es sind sechs Zeilen und der Kern der Etappe.

```python
meine_liste = ["schwert", "brot"]
mein_set    = {"schwert", "brot"}
mein_dict   = {"schwert": 5, "brot": 1}

print("schwert" in meine_liste)    # True — sucht im Inhalt
print("schwert" in mein_set)       # True — sucht im Inhalt
print("schwert" in mein_dict)      # True — sucht im SCHLÜSSEL
print(5 in mein_dict)              # False — 5 ist ein Wert!
```

Dreimal dasselbe Wort, dreimal etwas leicht anderes. Bei Liste und Set sucht `in` im Inhalt. Beim Dictionary **nur in den Schlüsseln** — dass es hier trotzdem `True` ergibt, liegt daran, dass `"schwert"` zufällig ein Schlüssel ist.

Die vierte Zeile ist die wichtige: `5` steht sichtbar im Dictionary, und `in` findet es trotzdem nicht. Willst du in den Werten suchen, musst du das sagen: `5 in mein_dict.values()`.

**Genau solche Kleinigkeiten trennen „ich habe es abgeschrieben" von „ich weiß, was da steht."**

### 6. Warum `in` bei einem Set schneller ist

Bei einer Liste muss Python jedes Element einzeln vergleichen. Bei tausend Einträgen bis zu tausend Vergleiche.

Ein Set macht das anders: Es berechnet aus dem Wert selbst eine Art Adresse und schaut direkt dort nach. **Ein Zugriff, egal ob zehn oder eine Million Einträge.** Dasselbe Verfahren nutzt ein Dictionary für seine Schlüssel — deshalb sind beide bei `in` schnell.

Für dein Dorf mit acht Orten ist das völlig egal. Merk es dir trotzdem: In Etappe 14 prüfst du bei jedem Schritt, ob ein Feld schon besucht wurde, und in Etappe 18 fragst du bei jedem Dialog mehrere Flags ab. Da summiert es sich.

**Ehrlich eingeordnet:** Das ist der Grund, den Programmierer als ersten nennen. Für dich ist der andere wichtiger — dass ein Set schlicht *ausdrückt*, worum es geht: eine Menge ohne Duplikate.

### 7. Warum ein Set keine Listen aufnehmen kann — die Schuld aus Etappe 5

```python
kaputt = {["a", "b"]}     # TypeError: unhashable type: 'list'
geht = {("a", "b")}       # Tuple funktioniert
```

Denselben Fehler hast du in Etappe 5 gesehen, als du eine Liste als Dictionary-Schlüssel benutzen wolltest. **Es ist derselbe Grund**, und jetzt kannst du ihn erklären:

Set und Dictionary berechnen aus dem Wert eine Adresse. Würde sich der Wert nachträglich ändern — und Listen sind veränderbar —, läge der Eintrag an der falschen Stelle und wäre unauffindbar. Also lässt Python nur **immutable** Werte zu: Strings, Zahlen, Booleans, Tuples.

Das Wort in der Fehlermeldung ist *unhashable*. Wenn du es siehst, weißt du ab jetzt: Da war etwas Veränderbares an einer Stelle, die Unveränderliches braucht.

### 8. Mengenoperationen

Sets können rechnen. Das ist ihre zweite Stärke und der Grund, warum die Transferaufgabe unten eine Zeile lang ist.

```python
a = {"brot", "seil", "lampe"}
b = {"seil", "lampe", "axt"}

a & b      # {'seil', 'lampe'}          Schnittmenge — was in beiden ist
a | b      # {'brot','seil','lampe','axt'}  Vereinigung — alles zusammen
a - b      # {'brot'}                   Differenz — was nur in a ist
a ^ b      # {'brot', 'axt'}            was in genau einem von beiden ist
```

Es gibt auch ausgeschriebene Namen: `a.intersection(b)`, `a.union(b)`, `a.difference(b)`. Die Zeichen sind kürzer, die Namen lesbarer — nimm, was du in vier Monaten besser verstehst.

**Wozu das in deinem Spiel gut ist:** In Etappe 18 hast du einen Satz Flags, die der Spieler gesammelt hat, und ein Ereignis, das bestimmte Flags voraussetzt. Die Frage „hat er alles, was nötig ist?" ist dann eine Zeile:

```python
if benoetigt - spieler_flags:      # es fehlt noch etwas
```

Heute kannst du damit sofort etwas anfangen: Welche Orte hat der Spieler noch **nicht** besucht? `set(orte) - besuchte_orte`.

Beachte dabei: `set(orte)` macht aus deinem Karten-Dictionary ein Set seiner **Schlüssel**. Dieselbe Regel wie bei `in`.

### 9. Das Tuple — was sich nicht ändern soll

```python
position = (4, 7)
richtungen = ("norden", "sueden", "osten", "westen")
```

Runde Klammern. Ansonsten verhält es sich wie eine Liste: Reihenfolge, Index ab 0, Duplikate erlaubt, `in` sucht im Inhalt.

**Der einzige Unterschied, und er ist der ganze Punkt:**

```python
position[0] = 5      # TypeError: 'tuple' object does not support item assignment
```

Ein Tuple lässt sich nach dem Anlegen nicht mehr verändern. Kein `append()`, kein `remove()`, keine Zuweisung an eine Position.

**Und jetzt die Unterscheidung, über die fast jeder stolpert:**

```python
position = (4, 7)

position[0] = 5      # TypeError — geht nicht
position = (5, 7)    # funktioniert einwandfrei
```

Wie kann das zweite erlaubt sein, wenn ein Tuple doch unveränderlich ist?

Weil zwei verschiedene Dinge gemeint sind. **Unveränderlich ist das Tuple, nicht der Name.** Die erste Zeile versucht, *im vorhandenen Tuple* etwas auszutauschen — das verweigert Python. Die zweite Zeile baut ein völlig neues Tuple und hängt das Schild `position` daran um. Das alte wird einfach nicht mehr gebraucht.

Erinnerst du dich an Etappe 1? Dort stand: *Eine Variable ist kein Behälter, sondern ein Schild, das auf einen Wert zeigt.* Hier ist der Fall, in dem dieser Unterschied plötzlich sichtbar wird. Das Schild darf umgehängt werden. Der Wert selbst nicht.

**Praktisch heißt das:** Die Position deiner Spielfigur darf sich jederzeit ändern — du ersetzt dann das ganze Tuple, statt eine Zahl darin zu tauschen. In Etappe 14 wirst du genau das bei jedem Schritt durch die Mine tun.

**Warum sollte man Unveränderlichkeit wollen?** Drei Gründe, und der erste ist der wichtigste:

*Es sagt etwas.* Wenn jemand — auch du in vier Monaten — ein Tuple sieht, weiß er sofort: Das ändert sich nicht. Das ist Dokumentation, die nicht veralten kann.

*Es schützt vor Versehen.* Was du nicht ändern kannst, kannst du nicht versehentlich ändern. Erinnerst du dich an das Aliasing aus Etappe 4 — zwei Namen, eine Liste? Bei einem Tuple kann das nicht passieren.

*Es darf in Sets und als Dictionary-Schlüssel stehen.* Siehe oben.

### 10. Tuple-Unpacking — das kennst du schon

```python
position = (4, 7)
x, y = position          # x ist 4, y ist 7
```

Zwei Variablen links, ein Tuple rechts, und Python verteilt. Das nennt sich **Unpacking**.

Und du benutzt es seit Etappe 5, ohne dass es einen Namen hatte:

```python
for name, daten in orte.items():
```

`.items()` liefert nämlich Tuples — jedes Paar aus Schlüssel und Wert ist eines. Die zwei Variablen vor dem `in` packen es aus. Was dir damals wie eine Sonderregel für Dictionaries vorkam, ist eine allgemeine Eigenschaft von Tuples.

**Prüf das selbst:**

```python
for paar in orte.items():
    print(type(paar), paar)
```

In Etappe 12 wirst du diese Form ständig benutzen, wenn du über NPCs und ihre Zustände läufst.

### 11. Die Klammer-Falle bei einem Element

```python
kein_tuple = (5)      # das ist einfach die Zahl 5
echtes_tuple = (5,)   # DAS ist ein Tuple mit einem Element
```

Das Komma macht das Tuple, nicht die Klammern. Bei einem Element muss man es hinschreiben, sonst sind die Klammern nur eine Rechenklammer wie in `(3 + 4) * 2`.

Kurios, aber du wirst darüber stolpern. Und `len((5))` gibt dir dann einen `TypeError` statt einer 1.

### 12. Tuples als Dictionary-Schlüssel — ein Blick auf Etappe 14

Weil Tuples unveränderbar sind, dürfen sie als Schlüssel dienen. Das öffnet eine Möglichkeit, die du in Etappe 14 brauchen wirst:

```python
felder = {
    (0, 0): "wand",
    (1, 0): "gang",
    (1, 1): "gang",
}

print(felder[(1, 0)])     # "gang"
```

Eine Karte, die nach Koordinaten nachschlägt. Mit einer Liste als Schlüssel ginge das nicht — jetzt weißt du warum.

Du brauchst das heute nicht. Aber wenn du es in Etappe 14 siehst, soll es kein neues Konzept sein, sondern ein Wiedersehen.

### 13. Dieselbe Klammer, drei Bedeutungen

Dir ist inzwischen etwas untergekommen, das verwirrend ist, weil es gleich aussieht:

```python
inventar[0]              # Position — das erste Element
orte["dorfplatz"]        # Schlüssel — der Eintrag mit diesem Namen
besuchte_orte[0]         # TypeError — ein Set hat keine Positionen
```

Dreimal eckige Klammern, dreimal etwas anderes. Bei der Liste ist der Inhalt eine **Position**, beim Dictionary ein **Schlüssel**, und beim Set geht es gar nicht.

**Das ist typisch für Programmiersprachen und ein Grund, warum Syntax allein nicht reicht:** Was eine Zeile bedeutet, hängt davon ab, welcher Datentyp dahintersteht. Wer beim Lesen von Code nur auf die Zeichen schaut, versteht ihn nicht — man muss wissen, worauf der Name zeigt.

Das ist übrigens auch der Grund für den Debugging-Reflex weiter unten: Bei einem seltsamen Verhalten ist `type()` oft die schnellere Frage als „was steht drin".

### 14. Die Entscheidungshilfe

Vier Fragen, in dieser Reihenfolge, und du hast die richtige Struktur:

> **1. Schlage ich etwas unter einem Namen nach?** → Dictionary
> **2. Sollen Duplikate unmöglich sein und die Reihenfolge egal?** → Set
> **3. Soll sich das nach dem Anlegen nicht mehr ändern?** → Tuple
> **4. Sonst** → Liste

Angewandt auf dein Spiel: Die Karte schlägt nach — Dictionary. Besuchte Orte sind eine Menge — Set. Die vier Himmelsrichtungen ändern sich nie — Tuple. Das Inventar ist eine Reihe von Dingen mit Reihenfolge und möglichen Duplikaten — Liste.

Jetzt füll die letzte Spalte deiner Tabelle von oben aus.

---

## Dein Auftrag

Schrittweise, nach jedem Schritt ausführen.

**Schritt 1 — Die Bestandsaufnahme**
Falls noch nicht geschehen: die Tabelle aus der Design-Entscheidung ausfüllen, jetzt mit der letzten Spalte. Zwei Minuten, und du weißt, was heute zu tun ist.

**Schritt 2 — `besuchte_orte` als Set**
Ein leeres Set vor der Hauptschleife. Achte auf die Schreibweise — `{}` wäre ein Dictionary.

Beim Betreten eines Ortes: `add()`. Ohne vorherige Prüfung, denn genau das musst du beim Set nicht.

Den Startort nicht vergessen — der wird nie „betreten", der Spieler ist schon da.

**Schritt 3 — Der `karte`-Befehl**
Zeigt jetzt nur, wo der Spieler war. Nicht mehr die ganze Welt.

Benutz `sorted()`, sonst wechselt die Reihenfolge bei jedem Aufruf.

**Und der Zusatz, der es interessant macht:** Zeig auch, wie viele Orte es insgesamt gibt. `3 von 8 erkundet` ist eine Zeile Code und verändert, wie der Spieler dein Dorf sieht — aus einer Ansammlung von Räumen wird etwas, das man vollständig machen kann.

**Schritt 4 — Die zweite Beschreibung ist kürzer**
Die Schuld aus Etappe 5. Beim ersten Betreten der ausführliche Text, danach eine knappe Zeile.

Du hast dafür jetzt genau das richtige Werkzeug: `if ort in besuchte_orte` — geprüft **bevor** du hinzufügst. Die Reihenfolge dieser zwei Zeilen entscheidet über alles; wenn du zuerst hinzufügst, ist jeder Ort sofort „schon bekannt".

Das ist übrigens eine Konvention fast aller Textadventures, und sie macht wiederholtes Durchqueren erträglich.

**Schritt 5 — `RICHTUNGEN` als Tuple**
Eine feste Sammlung der gültigen Himmelsrichtungen, ganz oben im Code:

```python
RICHTUNGEN = ("norden", "sueden", "osten", "westen")
```

Großschreibung ist Konvention für Werte, die sich nie ändern. Python erzwingt das nicht — das Tuple schon.

**Und jetzt der Nutzen**, denn das ist keine Fingerübung: Damit kannst du zwei Fälle unterscheiden, die dein Spiel bisher gleich behandelt hat.

- `gehe banane` → *„Das ist keine Richtung."*
- `gehe norden`, wo kein Weg ist → *„Da ist kein Weg."*

Der Spieler erfährt damit, ob er sich im Wort geirrt hat oder in der Welt. Das ist ein spürbarer Unterschied, und er kostet dich eine Prüfung gegen `RICHTUNGEN`.

**Schritt 6 — Gesehene Gegenstände**
Ein zweites Set: Was hat der Spieler schon einmal aufgehoben oder untersucht? Anders als das Inventar leert sich das nie.

Damit kannst du beim wiederholten Aufnehmen einen anderen Text zeigen — *„Du kennst dieses Brot bereits"* statt der vollen Beschreibung. Kleine Sache, dieselbe Wirkung wie Schritt 4.

Kommentier das Set: In Etappe 18 wird aus derselben Idee der zentrale Flag-Speicher deines Spiels.

**Schritt 7 — Mengenrechnung im Spiel**
Bau eine Zeile ein, die Mengenoperationen benutzt. Naheliegend: die noch unbesuchten Orte.

```python
set(orte) - besuchte_orte
```

Ob du das dem Spieler zeigst, ist deine Entscheidung — als Hinweis („Zwei Wege hast du noch nicht genommen") oder nur als Debug-Ausgabe für dich. Gebaut haben sollst du es.

**Schritt 8 — Der Durchgang**
Alle Befehle aus Etappe 3, 4 und 5 einzeln durchgehen. Danach der Test dieser Etappe: Lauf zweimal durch dasselbe Dorf. Beim zweiten Mal muss sich das Spiel anders anfühlen — kürzere Texte, eine gefüllte Karte, ein Fortschrittsstand.

Ohne dass du eine einzige neue Spielmechanik gebaut hast.

---

## Was NICHT in diese Etappe gehört

- ❌ Funktionen wie `zeige_karte()` → **Etappe 7**
- ❌ Ein Koordinatensystem für das Dorf → **Etappe 14** (und dort für die Mine, nicht das Dorf)
- ❌ Klassen für Orte oder Gegenstände → **Etappe 9 und 11**
- ❌ Ein vollständiges Flag-System → **Etappe 18**
- ❌ Das Speichern der Sets in einer Datei → **Etappe 19**
- ❌ `frozenset`, `defaultdict`, `Counter` und andere Spezialstrukturen → nicht in diesem Lehrplan
- ❌ Comprehensions (`{x for x in ...}`) → **Etappe 23**

**Besonders verlockend wird das Umbauen von allem.** Wenn man Sets frisch gelernt hat, sieht plötzlich jede Liste falsch aus. Dein Inventar ist keine.

Und **`frozenset` und Konsorten** wirst du beim Nachschlagen finden. Lass sie liegen. Vier Strukturen sicher zu beherrschen ist mehr wert als acht zu kennen.

---

## Selbsttest

- [ ] `besuchte_orte` ist ein Set und wird mit `set()` angelegt
- [ ] Der Startort steht von Anfang an drin
- [ ] Beim Betreten wird ohne vorherige Prüfung `add()` aufgerufen
- [ ] `karte` zeigt nur besuchte Orte, alphabetisch sortiert
- [ ] `karte` zeigt, wie viele von wie vielen Orten erkundet sind
- [ ] Die zweite Beschreibung eines Ortes ist kürzer als die erste
- [ ] Der Startort zeigt beim allerersten Mal die lange Beschreibung
- [ ] `RICHTUNGEN` ist ein Tuple
- [ ] `gehe banane` und `gehe norden` ohne Weg erzeugen verschiedene Meldungen
- [ ] Ein zweites Set merkt sich gesehene Gegenstände
- [ ] Irgendwo im Code steht eine Mengenoperation
- [ ] Du hast das `in`-Experiment mit allen drei Strukturen ausgeführt
- [ ] Du hast versucht, eine Liste in ein Set zu legen, und die Meldung gelesen
- [ ] Du hast versucht, ein Tuple zu ändern, und die Meldung gelesen
- [ ] Deine Bestandsaufnahme-Tabelle ist vollständig ausgefüllt
- [ ] Alle Befehle aus Etappe 3, 4 und 5 funktionieren unverändert
- [ ] Ein Kommentar verweist auf Etappe 18 (Flags) und 19 (Sets speichern)

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten:

1. **Wann Set statt Liste?** Nenn die zwei Gründe.
2. **Warum kann ein Set keine Listen enthalten, aber Tuples schon?** Und was hat das mit Dictionary-Schlüsseln aus Etappe 5 zu tun?
3. **Was ist an einem Tuple unveränderlich?** Was geht damit nicht mehr, was mit einer Liste ginge?
4. **Warum eignen sich Koordinaten besonders für Tuples?** Nenn zwei Gründe.
5. **Was ergibt `"a" in x`** — bei einer Liste, einem Set und einem Dictionary? Wo ist der Unterschied?
6. **Wie legst du ein leeres Set an, und warum nicht mit `{}`?**
7. **Was macht `a - b` bei zwei Sets?** Und wozu könntest du das in deinem Spiel gebrauchen?
8. **Warum ist `add()` bequemer als `append()` mit vorheriger Prüfung?**
9. **Was passiert bei `x = (5)` — und was wolltest du wahrscheinlich?**
10. **Was liefert `.items()` eigentlich zurück?** Warum funktionieren dort zwei Variablen vor dem `in`?

**Frage 2 ist die wichtigste.** Sie verbindet drei Etappen: das Aliasing aus Etappe 4, die Dictionary-Schlüssel aus Etappe 5 und die Set-Regel von heute. Es ist derselbe Grund, dreimal. Wer das erklären kann, hat verstanden, warum Python zwischen veränderbar und unveränderbar unterscheidet.

---

## Transferaufgabe (10–15 Minuten)

**Neue Datei, außerhalb des Spiels.** `uebung_06.py`.

**Teil 1 — Die Einzeiler**

> ```python
> dorf_bewohner = ["Mara", "Jorin", "Tobias", "Anne"]
> minenarbeiter = ["Jorin", "Karl", "Tobias", "Hannes"]
> ```
>
> Finde heraus, wer zu **beiden** Gruppen gehört — ohne Schleife.

Wenn du dabei eine Schleife schreibst, hast du das falsche Werkzeug gewählt. Mit dem richtigen ist es eine Zeile.

**Der Haken, der die eigentliche Übung ist:** Das sind Listen, und Listen können nicht rechnen. Du musst sie erst umwandeln. Genau dieser Zwischenschritt ist der Punkt — du entscheidest bewusst, dass die Daten für *diese Frage* als Menge behandelt werden sollen, obwohl sie als Liste ankommen.

Das ist eine sehr häufige Situation: Daten kommen in einer Form, die für ihre Herkunft sinnvoll ist, und du wandelst sie für deine Frage um.

Danach, ebenfalls je eine Zeile:

- Welche Dorfbewohner arbeiten **nicht** in der Mine?
- Wer kommt in **mindestens einer** Gruppe vor?
- Wie viele **verschiedene** Personen sind es insgesamt?

Der Zweck ist nicht die Lösung, sondern die Beobachtung: Wie viel Code entfällt, wenn die Struktur zum Problem passt.

**Teil 2 — Das Tuple**

> Leg eine Position als Tuple an. Pack sie in zwei Variablen aus.
> Versuch, eine der beiden Zahlen im Tuple zu ändern. Lies die Meldung.
> Bau dann ein Dictionary, das Positionen auf Beschreibungen abbildet, und schlag eine Position nach.

Das ist ein Vorgriff auf Etappe 14 — dort ist es das Fundament der Mine. Heute reichen drei Positionen.

**Teil 3 — Der Vergleich**

> Leg dieselben zehn Werte einmal als Liste und einmal als Set an, jeweils mit Duplikaten.
> Gib beide aus und vergleich die Längen.

Zwei Zeilen, und der Unterschied ist sichtbar statt behauptet.

---

## Kaputtmachen

Nach jedem Experiment rückgängig machen.

**Experiment 1 — Eine Liste in ein Set legen**
```python
kaputt = {["norden", "sueden"]}
```
`TypeError: unhashable type: 'list'`. Dieselbe Meldung wie in Etappe 5, Experiment 6 — dort war es ein Dictionary-Schlüssel. Kannst du jetzt erklären, warum es derselbe Fehler ist?

Danach mit einem Tuple statt der Liste. Warum geht das?

**Experiment 2 — Ein Tuple ändern**
```python
richtungen = ("norden", "sueden")
richtungen[0] = "westen"
richtungen.append("osten")
```
Zwei verschiedene Fehlermeldungen. Lies beide — die zweite sagt dir, dass es die Methode überhaupt nicht gibt.

**Experiment 3 — Das falsche leere Ding**
```python
besucht = {}
besucht.add("dorfplatz")
```
`AttributeError`. Was hast du tatsächlich angelegt? Prüf es mit `type()`.

**Experiment 4 — Duplikate verschwinden lassen**
```python
liste = ["brot", "brot", "brot"]
menge = set(liste)
print(len(liste), len(menge))
```
Drei gegen eins. **Bau das in dein Inventar ein** — mach `inventar` versehentlich zu einem Set und heb zweimal Brot auf. Was passiert mit dem zweiten?

Das ist der Grund, warum dein Inventar eine Liste bleibt. Fehler vom Typ 3 in Reinform: kein Absturz, nur ein Brot, das lautlos verschwindet.

**Experiment 5 — Dasselbe mit einer Liste**
Der umgekehrte Weg zu Experiment 4, und der überzeugendere. Bau `besuchte_orte` in deinem Spiel zur Liste um: `set()` wird `[]`, `add()` wird `append()`.

Jetzt lauf fünfmal zwischen zwei Orten hin und her und ruf `karte` auf.

Kein Absturz. Aber deine Karte behauptet, du hättest zehn Orte besucht, und dein Fortschrittsstand ist Unsinn. Um dasselbe mit einer Liste zu erreichen, bräuchtest du die `in`-Prüfung vor jedem `append()` — die du beim Set nicht brauchst.

**Das ist die Etappe in einem Experiment:** Beide Strukturen funktionieren. Nur eine passt.

**Experiment 6 — Die Reihenfolge, die keine ist**
```python
s = {"zeta", "alpha", "mu", "omega"}
print(s)
```
Führ das mehrmals aus, am besten in getrennten Programmläufen. Steht es immer gleich da?

Nimm dann `sorted()` aus deinem `karte`-Befehl heraus und schau, was der Spieler sieht.

**Experiment 7 — Zugriff über den Index**
```python
s = {"a", "b", "c"}
print(s[0])
```
`TypeError: 'set' object is not subscriptable`. Warum kann es keinen Index geben? Die Antwort steht in der Zeile darüber.

**Experiment 8 — Das Ein-Element-Tuple**
```python
a = (5)
b = (5,)
print(type(a), type(b))
print(len(b))
print(len(a))
```
Die letzte Zeile stürzt ab. Was ist `a` wirklich?

**Experiment 9 — Die Reihenfolge zweier Zeilen**
In Schritt 4 prüfst du `if ort in besuchte_orte` und rufst danach `add()` auf. Dreh die beiden Zeilen um.

Kein Absturz. Aber welche Beschreibung siehst du jetzt beim ersten Betreten — und warum? **Das ist der Fehler, den du in dieser Etappe wirklich produzieren wirst.**

**Experiment 10 — Mengenrechnung schiefherum**
```python
set(orte) - besuchte_orte
besuchte_orte - set(orte)
```
Das zweite ergibt fast immer ein leeres Set. Warum? Und was würde ein nicht-leeres Ergebnis über deine Daten aussagen?

Die Antwort ist interessanter, als sie klingt: Es hieße, der Spieler hätte einen Ort besucht, den es in deiner Karte nicht gibt. Genau die inkonsistenten Daten aus Etappe 5 — nur dass du sie jetzt in einer Zeile aufspüren kannst.

---

## Häufige Stolpersteine

| Fehlermeldung / Symptom | Was dahintersteckt | Wo du suchst |
|---|---|---|
| `AttributeError: 'dict' object has no attribute 'add'` | `{}` statt `set()` benutzt | Die Zeile, wo du es angelegt hast |
| `TypeError: unhashable type: 'list'` | Liste in ein Set oder als Dict-Schlüssel | Tuple statt Liste nehmen |
| `TypeError: 'set' object is not subscriptable` | Zugriff mit `[0]` auf ein Set | Sets haben keine Reihenfolge |
| `TypeError: 'tuple' object does not support item assignment` | Tuple verändern wollen | War Unveränderlichkeit hier richtig? |
| `AttributeError: 'tuple' object has no attribute 'append'` | Dasselbe von der anderen Seite | Liste nehmen, wenn es sich ändern soll |
| Die Ausgabe steht jedes Mal anders da | Sets haben keine Reihenfolge | `sorted()` beim Ausgeben |
| Die erste Beschreibung erscheint nie | `add()` steht vor der `in`-Prüfung | Die Reihenfolge der zwei Zeilen |
| Die erste Beschreibung erscheint immer | Der Besuch wird gar nicht gespeichert | Wird `add()` überhaupt erreicht? |
| Gegenstände verschwinden lautlos | Eine Liste wurde zum Set gemacht | Duplikate waren erwünscht |
| `TypeError: object of type 'int' has no len()` | `(5)` ist kein Tuple | Komma nicht vergessen: `(5,)` |
| Ein Set-Vergleich liefert nichts | Operanden vertauscht | `a - b` ist nicht `b - a` |

**Der Debugging-Reflex dieser Etappe:** Wenn eine Sammlung sich seltsam verhält, frag nicht als Erstes nach dem Inhalt, sondern nach dem **Typ**.

```python
print(type(besuchte_orte), len(besuchte_orte), besuchte_orte)
```

`type()` kennst du aus Etappe 1. Hier bekommt es seine eigentliche Bedeutung: Die Hälfte der Fehler dieser Etappe sind Strukturen, die etwas anderes sind, als du denkst. `{}` sieht aus wie ein Set und ist ein Dictionary. `(5)` sieht aus wie ein Tuple und ist eine Zahl.

---

## Ein Blick nach vorne

Heute hast du kein Feature gebaut, sondern ein Urteil geschärft. Das zahlt sich mehrfach aus:

In **Etappe 7** räumst du deine Befehlsverarbeitung in Funktionen auf. Dabei wirst du merken, dass gut gewählte Datenstrukturen sich viel leichter in Funktionen zerlegen lassen — weil eine Funktion, die ein Set entgegennimmt, sofort klar hat, was sie damit tun darf.

In **Etappe 14** kommt beides zusammen, was du in Etappe 5 und heute gelernt hast:

```python
besuchte_felder = set()          # das Set von heute
position = (x, y)                # das Tuple von heute
karte[y][x]                      # verschachtelte Listen — neu
```

Der Nebel des Krieges in der Mine ist genau dein `besuchte_orte`, nur mit Koordinaten statt Namen. Du wirst das dort nicht neu lernen, sondern wiedererkennen.

In **Etappe 18** wird aus deinem Set gesehener Gegenstände der zentrale **Flag-Speicher**. Jede Entscheidung, jeder Fund, jedes Gespräch hinterlässt eine Markierung, und Dialoge fragen sie ab. Und dann brauchst du die Mengenoperationen von heute wirklich: *Hat der Spieler alles, was dieses Ereignis voraussetzt?* ist eine Zeile mit `-`.

In **Etappe 19** stößt du auf eine unangenehme Überraschung: **Ein Set lässt sich nicht direkt als JSON speichern.** JSON kennt Listen, aber keine Mengen. Du wirst also beim Speichern umwandeln und beim Laden zurückwandeln müssen — und dabei zum ersten Mal merken, dass deine Datenstrukturen und dein Dateiformat zwei verschiedene Dinge sind.

Das ist kein Fehler in deinem Entwurf. Es ist die Sorte Problem, die entsteht, wenn Programme mit der Außenwelt reden.

---

## Abschluss

**`GELERNT.md`:**
Zwei bis drei Sätze. Zusätzlich diesmal:

- Deine ausgefüllte Bestandsaufnahme-Tabelle
- Was heißt bei dir „besucht" — betreten oder umgesehen?
- Und die Frage, die diese Etappe zusammenfasst: **Welche deiner bisherigen Datenstrukturen war falsch gewählt, und woran hättest du das früher merken können?**

Wenn die ehrliche Antwort „keine" lautet, ist das auch ein Ergebnis. Nicht jede Etappe muss etwas umwerfen.

**Commit:**
```bash
git add .
git commit -m "Etappe 6: Liste, Dictionary, Set, Tuple"
git push
```

Damit ist Block 1 fast durch. Ein Blick auf `git log --oneline` lohnt sich: sieben Commits, und dein Spiel hat eine Welt, ein Inventar, eine Karte und ein Gedächtnis.

---

## Wenn du mehr willst

Optional, erst bei grünem Selbsttest.

**Der Fortschrittsbalken.** Aus `3 von 8 erkundet` lässt sich mit ein paar Zeichen ein Balken bauen: `[███░░░░░]`. Du brauchst dafür nur `len()` und String-Multiplikation — `"█" * 3`. Kostet fünf Minuten und verändert, wie sich Erkunden anfühlt.

**Sackgassen erkennen.** Ein Ort, von dem aus alle Ausgänge zu bereits besuchten Orten führen, ist erschöpft. Mit Mengenoperationen ist das eine Zeile: Sind alle Ziele der Ausgänge in `besuchte_orte`? Der Spieler bekommt dann einen Hinweis, dass es hier nichts mehr zu holen gibt.

Das ist gleichzeitig die erste Stelle, an der dein Spiel etwas über seine eigene Struktur *weiß*, statt es nur abzubilden.

**Ein zweites Gedächtnis für die NPCs.** Mit wem hat der Spieler schon gesprochen? Ein Set, drei Zeilen — und die Figur aus Etappe 2 kann beim zweiten Gespräch anders reagieren als beim ersten.

Das ist der direkteste Vorgeschmack auf Etappe 18, den du heute bauen kannst. Und in einem leeren Dorf mit drei Menschen wirkt es stärker als jede Mechanik: Sie erinnern sich an dich.

---

> **Nächste Etappe:** [Etappe 7 — Aufräumen](etappe-07-aufraeumen.md) · Funktionen, Parameter, Rückgabewerte, Scope
> Dort baust du wieder nichts Neues — du zerlegst, was du hast. Und merkst zum ersten Mal, warum Funktionen nicht aus einem Lehrbuch kommen, sondern aus Notwendigkeit.
