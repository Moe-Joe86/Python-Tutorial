# Etappe 9 — Alles wird zum Objekt

> **Block 2: Objekte und Zeit** · Etappe 9 von 30 · [← Etappe 8](etappe-08-bug-jagd.md) · [Lehrplan](../RPG_Lehrplan.md) · [Etappe 10 →](etappe-10-komposition.md)

**Boot.dev:** Klassen, `__init__`, Methoden, Attribute
**Zeitaufwand:** 6–8 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 8 abgeschlossen, Spiel läuft in Funktionen

---

## Worum es geht

Am Ende von Etappe 7 hast du eine Zahl in `GELERNT.md` geschrieben: wie viele Parameter deine größte Funktion braucht. **Schlag sie jetzt nach, bevor du weiterliest.**

Bei den meisten steht dort etwas zwischen sechs und zehn. So sieht das aus:

```python
def verarbeite_befehl(befehl, orte, aktueller_ort, inventar,
                      besuchte_orte, gesehene, runden, laeuft):
```

Acht Dinge, die alle zusammengehören — sie beschreiben gemeinsam den Zustand deiner Welt. Und sie wandern durch jede einzelne Funktion, weil es keinen Ort gibt, an dem sie wohnen könnten.

**Heute bekommen sie einen.**

```python
def verarbeite_befehl(self, befehl):
```

`self` ist der Behälter. Ein einziger Parameter, an dem alles hängt.

**Das ist der Grund, warum diese Etappe erst jetzt kommt.** Man kann Klassen an Tag drei unterrichten. Dann sind sie eine Regel, die man befolgt: *Schreib `class`, schreib `self`, frag nicht warum.* Nach Etappe 7 sind sie etwas anderes — die Antwort auf ein Problem, das dich echte Zeit gekostet hat.

Wenn dir in Etappe 7 die Parameterlisten nicht auf die Nerven gegangen sind, geh zurück und bau eine weitere Funktion mit Zustand. Ohne den Schmerz bleibt `self` eine willkürliche Python-Eigenheit.

**Und noch etwas ändert sich heute.** Bis jetzt hattest du Daten auf der einen Seite (Listen, Dictionaries, Sets) und Funktionen auf der anderen. Ab heute gehören sie zusammen: Ein Objekt ist etwas, das **weiß** und **kann**. Ein Spieler weiß, wo er ist und was er trägt — und er kann sich bewegen und etwas aufheben. Diese Zusammengehörigkeit ist der ganze Inhalt der objektorientierten Programmierung, und alles andere ist Beiwerk.

---

## Der lange Bogen

| Was du heute baust | Wo es wieder auftaucht |
|---|---|
| `Player`-Klasse | **Etappe 10** — bekommt Inventar und Ausrüstung als eigene Objekte |
| `World`-Klasse | **Etappe 12** — bekommt `tick()` und damit ein Eigenleben |
| `self` als Zustandsbehälter | **Etappe 12** — `self.zeit += 1` ist die Uhr deiner Welt |
| `__init__` | **Etappe 10** — dort lauert die Falle mit veränderbaren Standardwerten |
| `__repr__` | **Etappe 11** — bekommt Gesellschaft von `__eq__`, `__len__`, `__iter__` |
| Methoden statt freier Funktionen | **Etappe 11** — Vererbung teilt Methoden zwischen Klassen |
| `player.ort` statt `aktueller_ort` | **Etappe 19** — die Objektstruktur bestimmt den Speicherstand |
| Objekte im Debugger aufklappen | **Etappe 12** — den Tick beobachten; **Etappe 16** — Bug-Jagd mit Objekten |
| Die erste echte Leseübung | **Etappe 23** — Code aus echten Projekten; **Etappe 27** — ein ganzes Repo |

**Zehn Schulden werden heute eingelöst** — mehr als in jeder anderen Etappe des Tutorials:

Aus **Etappe 2**: die Punkt-Schreibweise. Du benutzt `.lower()` und `.append()` seit Wochen, ohne zu wissen, warum dort ein Punkt steht. Heute erfährst du es.

Aus **Etappe 2** außerdem: der Name der Figur, den du optional in einer Variable abgelegt hast. Er wird zu `npc.name`.

Aus **Etappe 7**: die Funktionen, die zu Methoden werden. Die Zuschnitt-Entscheidung, die du damals begründet hast — Themen oder Befehle. Das Prinzip „Abhängigkeiten sichtbar machen", das durch `self` eine neue Wendung nimmt. Der `global`-Verzicht, der sich heute auszahlt. Und vor allem **die Parameterliste**.

Aus **Etappe 8**: der Debugger, der ab heute Objekte aufklappen kann. Und die Leseübung, die dort eine Vorstufe war und jetzt zur festen Übungsform wird.

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

### Frage 1: Wo wohnt der Zustand?

Der Spieler steht an einem Ort. Ist das eine Eigenschaft des **Spielers** oder der **Welt**?

```python
spieler.ort = "wiese"           # A — der Spieler weiß, wo er ist
world.spielerposition = "wiese"  # B — die Welt weiß, wo der Spieler ist
```

Beide Antworten sind vertretbar, und Spiele-Engines gibt es in beiden Sorten.

**A liest sich natürlicher.** `spieler.ort` klingt wie Deutsch, und wenn du in Etappe 19 den Spielstand speicherst, ist der Spieler ein abgeschlossenes Ding mit allem, was zu ihm gehört.

**B hat einen Vorteil, den du erst in Etappe 12 merkst:** Wenn NPCs sich bewegen, muss jemand wissen, wer wo ist. Steht die Position bei jeder Figur, muss die Welt alle Figuren durchgehen, um zu beantworten „wer ist hier?"

**Meine Empfehlung: A.** Der Lehrplan geht davon aus, und es passt zur Denkweise, um die es heute geht — ein Objekt weiß Dinge über sich selbst. Aber triff die Entscheidung bewusst und schreib sie mit einem Satz Begründung in `GELERNT.md`.

**Und eine Regel, die dir Ärger erspart:** Was auch immer du wählst, es gibt danach **eine** Wahrheit. Nicht `spieler.ort` *und* `aktueller_ort` nebeneinander, die man beide pflegen muss. Zwei Quellen für dieselbe Information sind eine Fehlerfabrik — und zwar für Fehler vom Typ 3.

### Frage 2: Was wird Methode, was bleibt Funktion?

Nicht alles gehört zu einem Objekt.

```python
spieler.nimm("brot")                    # gehört klar zum Spieler
berechne_schaden(angriff, ruestung)     # gehört zu niemandem
```

`berechne_schaden` bekommt Zahlen und gibt eine Zahl zurück. Sie braucht keinen Zustand, sie kennt keinen Spieler, sie funktioniert allein. **So etwas zur Methode zu machen ist eine Verschlechterung** — es täuscht eine Zugehörigkeit vor, die es nicht gibt.

Die Frage, die trägt:

> **Braucht diese Funktion den Zustand eines bestimmten Dings? Dann Methode. Sonst Funktion.**

Das ist die Fortsetzung der Warnung aus Etappe 7 („mehr Funktionen sind nicht besser"), eine Ebene höher. Und du wirst sie in Etappe 11 wieder brauchen, wenn die Frage lautet, ob etwas eine eigene Klasse verdient.

---

### Frage 3: Wem gehört welche Information?

Bevor du irgendetwas baust, mach diese Übung auf Papier. Zehn Minuten, kein Code.

Schreib alle Variablen auf, die dein Spiel gerade hat — `spielername`, `hp`, `aktueller_ort`, `inventar`, `orte`, `besuchte_orte`, `runden`, `wetter`, `geruch`, `laeuft`, und was du sonst hast. Dann ordne jede genau einer Spalte zu:

| Variable | Player | World | gehört nirgends hin |
|---|:---:|:---:|:---:|
| `spielername` | ✓ | | |
| `orte` | | ✓ | |
| `berechne_schaden` | | | ✓ |
| … | | | |

**Die dritte Spalte ist die interessante.** Nicht alles gehört zu einem Objekt. `geruch` aus Etappe 1 ist Atmosphäre — er beschreibt weder den Spieler noch die Weltmechanik. Solche Werte dürfen lose bleiben oder als Konstanten oben stehen.

**Und ein Fall, über den du stolpern wirst:** Wohin gehört `wetter`? Zur Welt, wenn es das ganze Dorf betrifft. Zum Ort, wenn es pro Ort verschieden ist. Die Antwort hängt davon ab, was du damit vorhast — und genau solche Fragen sind der Inhalt dieser Etappe.

> **Objektorientiertes Denken ist nicht „Syntax mit `class`". Es ist die Frage: Wem gehört diese Information?**

Diese Übung bekommt in Etappe 10 eine Fortsetzung (*was ist ein eigenes Ding, was nur ein Attribut?*) und in Etappe 24 noch eine (*was gehört in welche Datei?*). Es ist jedes Mal dieselbe Frage, eine Ebene größer.

---

## Die Konzepte

### 1. Klasse und Objekt — Bauplan und Ding

```python
class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100

spieler = Player("Mara")        # jetzt existiert etwas
```

Die **Klasse** ist der Bauplan. Sie beschreibt, was ein Spieler hat und kann — aber sie ist selbst kein Spieler, so wie ein Bauplan kein Haus ist.

Das **Objekt** entsteht, wenn du die Klasse aufrufst: `Player("Mara")`. Aus einem Bauplan kann man beliebig viele bauen, und jedes hat seine eigenen Werte:

```python
mara = Player("Mara")
jorin = Player("Jorin")

mara.hp = 40
print(jorin.hp)      # 100 — Jorin ist davon unberührt
```

**Konvention:** Klassennamen groß und in Einzahl — `Player`, nicht `player` oder `Players`. Python erzwingt das nicht, aber jeder Leser erwartet es, und es hilft dir selbst, Klasse und Objekt auseinanderzuhalten.

**Und ein Detail, das dich sonst verwirrt:** Es gibt kein `new` und kein Sternchen. `Player("Mara")` sieht aus wie ein Funktionsaufruf, weil es einer ist — die Klasse ist selbst aufrufbar, und der Aufruf liefert ein neues Objekt zurück.

### 2. `__init__` — der Moment der Entstehung

```python
class Player:
    def __init__(self, name, ort="dorfplatz"):
        self.name = name
        self.hp = 100
        self.ort = ort
```

`__init__` läuft **automatisch**, sobald ein Objekt entsteht. Du rufst sie nie selbst auf — `Player("Mara")` genügt, und Python erledigt den Rest.

Ihre Aufgabe ist, das Objekt in einen brauchbaren Anfangszustand zu bringen. Alles, was ein Spieler von Anfang an haben soll, wird hier gesetzt.

**Der Standardwert `ort="dorfplatz"`** ist genau das Muster aus Etappe 7: Du kannst `Player("Mara")` schreiben oder `Player("Mara", "wiese")`, ohne zwei Klassen zu brauchen.

> ⚠️ **Die Warnung aus Etappe 7 gilt hier verschärft:** Niemals eine Liste, ein Dictionary oder ein Set als Standardwert — also nie `def __init__(self, items=[])`. Das verhält sich anders, als jeder erwartet. In Etappe 10 baust du den Fehler absichtlich nach und verstehst, warum.

**Was `__init__` nicht ist:** Sie erzeugt das Objekt nicht — das tut Python. Sie *richtet es ein*. Deshalb hat sie auch kein `return`; alles, was sie tut, ist `self.irgendwas = ...`.

**Und daraus folgt ein Prinzip, das über diese Etappe hinausreicht:**

> **Ein Objekt sollte nach seiner Erzeugung einen sinnvollen Zustand haben — nie halb fertig sein.**

Kein `Player()`, den man danach von Hand mit Namen, Lebenspunkten und Ort bestücken muss. Denn wer das einmal vergisst, hat ein Objekt, das aussieht wie ein Spieler und keiner ist — und der Fehler taucht irgendwo ganz woanders auf.

Das klingt selbstverständlich und ist es nicht: In Etappe 25 lädst du Objekte aus JSON-Dateien, die jemand von Hand bearbeitet hat. Dann ist genau diese Frage — *ist dieses Ding vollständig?* — der Grund für die Prüffunktion, die du dort schreibst.

### 3. `self` — der wichtigste Abschnitt dieser Etappe

Hier ist der Punkt, an dem viele Anfänger aussteigen, weil `self` wie eine sinnlose Formalität wirkt. Ist es nicht, und die Erklärung ist kürzer, als du denkst.

**Wenn du das schreibst:**

```python
spieler.zeige_inventar()
```

**passiert in Wahrheit das:**

```python
Player.zeige_inventar(spieler)
```

Python nimmt das Objekt vor dem Punkt und schiebt es als **erstes Argument** in die Methode. Das ist alles. `self` ist nur der Name, den man diesem ersten Parameter üblicherweise gibt.

Deshalb steht `self` in jeder Methodendefinition, aber nie beim Aufruf — es wird automatisch mitgeliefert.

**Und deshalb ist `self` die Antwort auf dein Problem aus Etappe 7.** Vergleich:

```python
# Etappe 7 — jede Funktion bekommt alles einzeln gereicht
def verarbeite_befehl(befehl, orte, aktueller_ort, inventar,
                      besuchte_orte, gesehene, runden, laeuft):

# Etappe 9 — ein Behälter, an dem alles hängt
def verarbeite_befehl(self, befehl):
```

Sieben Parameter sind verschwunden. Sie sind nicht weg — sie stecken in `self` und heißen jetzt `self.orte`, `self.inventar`, `self.runden`. Aber sie werden nicht mehr durchgereicht, sondern **liegen dort, wo sie hingehören**.

**Ein Bild, das hilft:**

```text
spieler
   │
   ▼
┌──────────────────────────┐
│ Player-Objekt            │
│                          │
│  name  → "Mara"          │
│  hp    → 100             │
│  ort   → "dorfplatz"     │
└──────────────────────────┘
        ▲
        │
      self          (innerhalb jeder Methode dieses Objekts)
```

`spieler` und `self` zeigen auf dasselbe Kästchen — nur von außen und von innen. Deshalb ist `spieler.hp` außerhalb genau dasselbe wie `self.hp` innerhalb einer Methode.

Und wenn du ein zweites Objekt erzeugst, gibt es ein zweites Kästchen mit eigenen Werten. `self` zeigt dann während eines Methodenaufrufs auf *dieses* Kästchen. Welches, entscheidet sich beim Aufruf: `mara.nimm(...)` gegen `jorin.nimm(...)`.

**Der Name ist frei wählbar.** Du könntest `def zeige(ich):` schreiben, und es würde funktionieren. Tu es nicht: Jeder Python-Programmierer der Welt liest `self`, und Abweichung kostet Verständlichkeit ohne Gegenwert.

**Der Reflex, den du dir jetzt angewöhnst:** Wann immer du in einer Methode auf etwas zugreifst, das dem Objekt gehört, schreibst du `self.` davor. Vergisst du es, sucht Python nach einer lokalen Variable — und findet meistens keine. Das ist der häufigste Fehler dieser Etappe.

### 4. Attribute — was das Objekt weiß

```python
class Player:
    def __init__(self, name):
        self.name = name        # Attribut — überlebt die Methode
        zaehler = 0             # lokale Variable — verschwindet sofort
```

Der Unterschied ist genau der Scope aus Etappe 7, nur an einem neuen Ort. Eine lokale Variable in einer Methode existiert, solange die Methode läuft. Ein Attribut hängt am Objekt und existiert, solange das Objekt existiert.

**Und jetzt die Zeile, die fast jeden einmal verwirrt:**

```python
def __init__(self, name):
    self.name = name
```

Links und rechts steht dasselbe Wort, und trotzdem sind es zwei völlig verschiedene Dinge.

**Rechts** steht der **Parameter** `name` — der Wert, der beim Aufruf hereingereicht wurde. Er existiert nur, solange `__init__` läuft, und ist danach weg.

**Links** steht das **Attribut** `self.name` — der Platz am Objekt, an dem der Wert bleiben soll. Die Zeile liest sich also: *„Nimm den Wert, der hereinkam, und leg ihn dauerhaft an diesem Objekt ab."*

Dass beide gleich heißen, ist Konvention und Bequemlichkeit, keine Notwendigkeit. Das hier ist völlig gleichwertig:

```python
def __init__(self, uebergebener_name):
    self.name = uebergebener_name
```

Nur schreibt das niemand, weil der gleiche Name klarmacht, dass es um dieselbe Sache geht. **Wichtig ist nur, dass du weißt, welche Seite welche ist** — sonst wirkt `self.` wie eine überflüssige Verzierung, die man eben hinschreibt.

Attribute kann man auch von außen lesen und setzen:

```python
print(spieler.hp)
spieler.hp = 40
spieler.mana = 20        # legt spontan ein neues Attribut an!
```

**Die letzte Zeile ist eine Falle.** Python beschwert sich nicht, wenn du ein Attribut anlegst, das es in `__init__` nicht gibt — es entsteht einfach. Ein Tippfehler wie `spieler.hpp = 40` wirft keinen Fehler und setzt stillschweigend etwas Neues. Fehler vom Typ 3, und er steht unten in den Experimenten.

**Deshalb die Regel:** Alle Attribute, die ein Objekt haben soll, werden in `__init__` gesetzt. Auch die, die anfangs `None` oder `0` sind. Dann steht an einer Stelle, was zu diesem Ding gehört — und du hast eine Liste, gegen die du Tippfehler prüfen kannst.

### 5. Methoden — was das Objekt kann

```python
class Player:
    def __init__(self, name):
        self.name = name
        self.inventar = []

    def nimm(self, gegenstand):
        if len(self.inventar) >= 10:
            return False, "Du kannst nichts mehr tragen."
        self.inventar.append(gegenstand)
        return True, f"Du nimmst {gegenstand}."
```

Eine Methode ist eine Funktion, die zu einer Klasse gehört. Alles aus Etappe 7 gilt weiter: Parameter, Rückgabewerte, `return` statt `print`, mehrere Rückgabewerte als Tuple, ein Zweck pro Methode.

**Der einzige Unterschied:** Sie hat Zugriff auf den Zustand ihres Objekts, ohne dass man ihn hineinreichen muss.

**Und hier zahlt deine Zuschnitt-Entscheidung aus Etappe 7.** Wenn du damals nach Themen geschnitten hast — `inventar_hinzufuegen`, `bewege_spieler`, `beschreibe_ort` —, dann fällt heute fast von selbst auf, welche Methode zu welcher Klasse gehört. Wenn du nach Befehlen geschnitten hast — `befehl_nimm`, `befehl_gehe` —, musst du jetzt einmal sortieren. Beides geht; das eine ist heute mehr Arbeit.

### 6. Die Punkt-Schreibweise — die Schuld aus Etappe 2

Seit Etappe 2 schreibst du `eingabe.lower()`. Seit Etappe 4 `inventar.append("brot")`. Damals stand da nur: *„ruf diese Funktion auf diesem Wert auf."* Das war richtig, aber es war nicht die ganze Wahrheit.

**Die ganze Wahrheit ist: In Python ist alles ein Objekt.**

Ein String ist ein Objekt der Klasse `str`, und `.lower()` ist eine Methode dieser Klasse. Eine Liste ist ein Objekt der Klasse `list`, und `.append()` ist eine ihrer Methoden. Wenn du `inventar.append("brot")` schreibst, passiert genau dasselbe wie bei `spieler.nimm("brot")` — nur dass jemand anderes die Klasse geschrieben hat.

```python
print(type("hallo"))        # <class 'str'>
print(type([1, 2]))         # <class 'list'>
print(type(spieler))        # <class '__main__.Player'>
```

Dreimal dasselbe Muster. **Du hast heute nicht ein neues Konzept gelernt, sondern erfahren, wie das funktioniert, was du seit sieben Etappen benutzt.**

Das ist übrigens eine der besten Nachrichten dieses Tutorials: Ab jetzt ist jede fremde Bibliothek, die du siehst, aus denselben Bauteilen gemacht wie dein Spiel.

### 7. `__repr__` — Haken, an denen Python zieht

```python
spieler = Player("Mara")
print(spieler)
# <__main__.Player object at 0x7f3a2c1d5e50>
```

Das ist die nutzloseste Ausgabe, die Python zu bieten hat. Es sagt dir: „hier ist ein Player, und er liegt an dieser Speicheradresse." Beides interessiert dich nicht.

```python
class Player:
    def __repr__(self):
        return f"Player(name={self.name!r}, hp={self.hp}, ort={self.ort!r})"
```

Jetzt:

```python
print(spieler)
# Player(name='Mara', hp=100, ort='dorfplatz')
```

**Du rufst `__repr__` nie selbst auf.** Python ruft sie, wenn ein Objekt angezeigt werden soll — bei `print()`, in einer Liste, im Debugger, in einer Fehlermeldung. Genau wie `__init__` beim Erzeugen läuft, ohne dass du sie aufrufst.

**Das ist das Muster, das du dir merken sollst:** Methoden mit doppelten Unterstrichen sind **Haken**. Python zieht daran, wenn eine bestimmte Situation eintritt. Du schreibst die Methode, Python entscheidet, wann sie läuft.

In Etappe 11 lernst du weitere: `__eq__` läuft bei `==`, `__len__` bei `len()`, `__iter__` bei `for x in obj`. Wenn du in fremdem Code jemals gerätselt hast, warum `len(irgendetwas)` funktioniert, obwohl nirgends eine `len`-Funktion definiert ist — das ist die Antwort.

**Ein praktischer Rat:** Schreib `__repr__` so, dass die Ausgabe aussieht wie der Aufruf, mit dem man das Objekt erzeugen könnte. `Player(name='Mara', hp=100)` ist besser als `Spieler Mara mit 100 HP`, weil du beim Debuggen sofort siehst, welche Attribute es gibt. Und `!r` sorgt dafür, dass Strings in Anführungszeichen erscheinen — sonst siehst du das verirrte Leerzeichen wieder nicht.

### 8. Objekte im Debugger — die Schuld aus Etappe 8

Jetzt zahlt Etappe 8 zurück, und zwar deutlich.

Setz einen Breakpoint in einer Methode und starte mit F5. Im Variablen-Bereich steht `self` — **und du kannst es aufklappen.** Darunter alle Attribute mit ihren aktuellen Werten, und die kannst du wieder aufklappen: das Inventar als Liste, die Orte als Dictionary, alles auf einmal.

**Das ist der Einblick, den `print()` mühsam nachbaut.** Vorher hättest du fünf Ausgaben gebraucht, um dasselbe zu sehen. Jetzt ein Breakpoint und ein Klick.

Und `__repr__` macht es noch besser: Steht ein Objekt in einer Liste, zeigt der Debugger nicht `<Player object at 0x...>`, sondern deinen lesbaren Text. Bei zehn NPCs in einer Liste ist das der Unterschied zwischen brauchbar und wertlos.

### 9. Was heute *nicht* zur Klasse wird

Der häufigste Fehler nach dieser Etappe ist, alles in Klassen zu stecken.

```python
class Schadensrechner:                      # nein
    def berechne(self, angriff, ruestung):
        return max(0, angriff - ruestung)
```

Diese Klasse hat keinen Zustand. Sie ist eine Funktion mit Zeremonie drumherum — man muss erst ein Objekt erzeugen, um sie zu benutzen, und das Objekt weiß nichts.

**Der Prüfstein:** Wenn `__init__` leer wäre oder nur `pass` enthielte, brauchst du keine Klasse.

Was also Funktion bleibt: `berechne_schaden()`, Hilfsfunktionen zum Formatieren von Text, alles, was Eingaben in Ausgaben verwandelt, ohne sich etwas zu merken. Diese Funktionen sind nicht schlechter als Methoden — sie sind für ihre Aufgabe besser, weil man sie einzeln aufrufen und testen kann.

### 10. Zwei Klassen, nicht eine

Heute entstehen **zwei** Klassen, und die Aufteilung ist selbst ein Lehrinhalt.

```python
class Player:
    """Was der Spieler ist und kann."""
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.ort = "dorfplatz"
        self.inventar = []

class World:
    """Die Welt und alles, was in ihr gilt."""
    def __init__(self, orte, spieler):
        self.orte = orte
        self.spieler = spieler
        self.besuchte_orte = set()
        self.runden = 0
        self.laeuft = True
```

**Beachte die letzte Zeile von `World.__init__`:** Die Welt *hat* einen Spieler. Ein Objekt kann ein anderes Objekt als Attribut halten — das ist die halbe Etappe 10, und du benutzt es heute schon, ohne dass es einen Namen braucht.

**Warum nicht alles in eine Klasse?** Weil dann nichts gewonnen wäre. Eine Klasse mit fünfzehn Attributen und zwanzig Methoden ist dieselbe Unübersichtlichkeit wie vorher, nur mit `self.` davor. Die Frage ist immer dieselbe wie in Etappe 7: **Was gehört zusammen?**

**Und was ist mit den Orten?** Die bleiben ein Dictionary. Aus jedem Ort eine `Ort`-Klasse zu machen wäre möglich, und in Etappe 11 wirst du dich fragen, ob du es tun solltest. Heute nicht — eine Sache nach der anderen.

### 11. Was `self` mit „Abhängigkeiten sichtbar machen" macht

In Etappe 7 stand das Prinzip: *Der Kopf einer Funktion ist ein Vertrag. Was nicht in den Klammern steht, braucht sie nicht.*

**Klassen weichen dieses Prinzip auf, und das solltest du wissen.**

```python
def bewege(orte, ort, richtung):     # sieht man alles
def bewege(self, richtung):          # was steckt in self?
```

Die zweite Form ist kürzer und angenehmer. Aber sie verbirgt, worauf sie zugreift — `self` kann alles Mögliche enthalten, und man muss in die Klasse schauen, um es zu erfahren.

**Ist das schlimm?** Nein, es ist ein Tausch. Man gewinnt Lesbarkeit an den Aufrufstellen und verliert Sichtbarkeit in der Signatur. Der Tausch lohnt sich, solange eine Klasse **einen klaren Zweck** hat: Wenn `World` die Welt ist, überrascht es niemanden, dass eine `World`-Methode auf `self.orte` zugreift.

Er lohnt sich **nicht** mehr, wenn eine Klasse zur Abstellkammer wird. Dann bedeutet `self` „irgendwas aus einem Haufen von zwanzig Dingen", und niemand kann mehr sagen, was eine Methode anfasst.

Das ist der Grund, warum die Frage „was gehört zusammen?" wichtiger ist als jede Syntax dieser Etappe.

---

## Dein Auftrag

Diese Etappe ist ein großer Umbau. **Der Verhaltens-Beweis aus Etappe 7 gilt wieder:** Befehlsfolge durchspielen, Ausgabe sichern, umbauen, vergleichen. Ohne ihn weißt du am Ende nicht, ob du etwas zerstört hast.

**Schritt 1 — Die Zahl nachschlagen**
Öffne `GELERNT.md` und such die Parameterzahl deiner größten Funktion aus Etappe 7. Schreib sie oben auf ein Blatt. Am Ende dieser Etappe vergleichst du.

**Schritt 2 — `Player` als Übungsstück**
Fang klein an: eine Klasse mit `name`, `hp`, `ort`. Erzeug ein Objekt, gib die Attribute aus, ändere eines, gib es nochmal aus.

Noch ohne Anschluss an dein Spiel. Du lernst hier die Mechanik an etwas, wo nichts kaputtgehen kann.

**Schritt 3 — `__repr__`**
Einbauen, dann `print(spieler)` — vorher und nachher. Zwei Minuten, und du siehst den Unterschied, der dir in den nächsten zwanzig Etappen Zeit spart.

**Schritt 4 — Die ersten Methoden**
Zwei oder drei Methoden, die zum Spieler gehören. `nimm()`, `ablege()`, `zeige_inventar()` sind die naheliegenden.

Nimm den Code aus deinen Etappe-7-Funktionen und **verschieb** ihn. Nicht neu schreiben — verschieben und `self.` ergänzen. Das ist Refactoring, kein Neubau.

**Schritt 5 — Der Anschluss**
Jetzt ersetzt du die losen Variablen im Spiel durch das Objekt. `inventar` wird `spieler.inventar`, `aktueller_ort` wird `spieler.ort`.

Nach diesem Schritt **muss dein Spiel wieder vollständig laufen.** Prüf gegen den Verhaltens-Beweis, bevor du weitermachst. Wenn du erst `World` baust und dann feststellst, dass schon `Player` etwas kaputtgemacht hat, suchst du an zwei Stellen gleichzeitig.

**Schritt 6 — `World`**
Dieselbe Übung, größeres Objekt. Alles, was zur Welt gehört und nicht zum Spieler: die Ortstabelle, die besuchten Orte, der Rundenzähler, die Laufen-Flagge — und der Spieler selbst.

**Schritt 7 — Die Funktionen werden Methoden**
`verarbeite_befehl()`, `bewege_spieler()`, `zeige_ort()` wandern in `World`. Aus jedem Parameter, der Weltzustand war, wird ein `self.`-Zugriff.

Einzeln umziehen, nach jeder prüfen. Bei sechs Funktionen auf einmal suchst du eine Stunde.

**Schritt 8 — Was Funktion bleibt**
Geh deine Funktionen durch und entscheide für jede: Braucht sie den Zustand eines bestimmten Dings?

Mindestens eine sollte Funktion bleiben — `berechne_schaden()` ist der offensichtliche Kandidat. Schreib in `GELERNT.md`, welche und warum.

**Schritt 9 — Der Debugger**
Setz einen Breakpoint in einer Methode. Klapp `self` im Variablen-Bereich auf. Schau dir an, was dein Objekt in diesem Moment tatsächlich enthält.

Das ist keine Pflichtübung, sondern eine Gewohnheit, die du dir jetzt anlegen sollst. Ab Etappe 12 ist sie die schnellste Art, deine Welt zu verstehen.

**Schritt 10 — Der Vergleich**
Verhaltens-Beweis prüfen. Dann die Parameterzahl deiner größten Methode zählen und mit der Zahl von Schritt 1 vergleichen.

Schreib beide Zahlen in `GELERNT.md`. Das ist der Messwert dieser Etappe.

---

## Was NICHT in diese Etappe gehört

- ❌ Vererbung, `super()`, Unterklassen → **Etappe 11**
- ❌ Eigene `Item`- oder `Ort`-Klassen → **Etappe 11**
- ❌ `Inventory` als eigene Klasse → **Etappe 10**
- ❌ `tick()` und Weltzeit → **Etappe 12**
- ❌ `@dataclass` → **Etappe 23**
- ❌ `@property`, `__eq__`, `__len__`, `__iter__` → **Etappe 11**
- ❌ Klassen in eigene Dateien aufteilen → **Etappe 24**
- ❌ Neue Spielfunktionen jeder Art

**Besonders verlockend wird die `Item`-Klasse.** Sobald `Player` steht, sieht ein Gegenstand als bloßer String armselig aus. Das Gefühl ist richtig — und Etappe 11 ist dafür da. Heute würdest du zwei neue Konzepte gleichzeitig lernen und bei einem Fehler nicht wissen, welches schuld ist.

**Und `tick()`.** Wenn `World` erst mal existiert, ist die Versuchung groß, ihr sofort ein Eigenleben zu geben. Widersteh: Etappe 12 ist eine der wichtigsten des ganzen Tutorials, und sie funktioniert nur, wenn `World` vorher sauber steht.

---

## Selbsttest

- [ ] Der Verhaltens-Beweis wurde **vor** dem Umbau angelegt
- [ ] Die Ausgabe nach dem Umbau ist mit der davor identisch
- [ ] `Player` und `World` existieren als Klassen
- [ ] Alle Attribute werden in `__init__` gesetzt, keines entsteht spontan woanders
- [ ] `print(spieler)` zeigt lesbaren Text, keine Speicheradresse
- [ ] `__repr__` zeigt die Attribute in einer Form, die dem Erzeugungsaufruf ähnelt
- [ ] Mindestens drei Methoden sind aus Etappe-7-Funktionen entstanden
- [ ] Mindestens eine Funktion ist bewusst **keine** Methode geworden, mit Begründung in `GELERNT.md`
- [ ] Es gibt genau eine Wahrheit über den Spielerort — keine zweite Variable daneben
- [ ] Nirgends steht `global`
- [ ] Kein Standardwert in `__init__` ist eine Liste, ein Dictionary oder ein Set
- [ ] Du hast `self` im Debugger aufgeklappt und den Inhalt gelesen
- [ ] Experiment 1 und 3 hast du **verstanden**, nicht nur repariert — du kannst beide Fehlermeldungen erklären
- [ ] Die Zuordnungstabelle aus Frage 3 ist ausgefüllt, inklusive der dritten Spalte
- [ ] Die Parameterzahl vorher und nachher steht in `GELERNT.md`
- [ ] Ein Kommentar verweist auf Etappe 12 (`World` bekommt dort `tick()`)

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten:

1. **Was ist `self` — und warum steht es überall?** Was passiert bei `spieler.nimm("brot")` tatsächlich?
2. **Unterschied Klasse ↔ Objekt?** Nenn ein Bild dafür, das nicht „Bauplan und Haus" ist.
3. **Wann wird `__init__` aufgerufen?** Warum rufst du sie nie selbst auf?
4. **Unterschied Attribut ↔ lokale Variable in einer Methode?** Wie lange lebt jedes?
5. **Wer ruft `__repr__` auf, und warum rufst *du* es nie selbst?**
6. **Warum funktioniert `inventar.append("brot")`?** Was hat das mit deiner `Player`-Klasse zu tun?
7. **Woran erkennst du, dass etwas eine Funktion bleiben sollte statt Methode zu werden?**
8. **Was passiert bei `spieler.hpp = 40`, wenn das Attribut `hp` heißt?**
9. **Was gewinnst du durch `self` — und was verlierst du gegenüber der Parameterliste aus Etappe 7?**
10. **Warum sind zwei Klassen besser als eine große?**

**Frage 1 ist die wichtigste**, und die vollständige Antwort hat zwei Teile: was Python technisch tut (das Objekt wird als erstes Argument übergeben) und wozu das gut ist (der Zustand muss nicht mehr durchgereicht werden). Wer nur den ersten Teil kann, hat die Syntax verstanden. Wer beide kann, weiß, warum es Klassen gibt.

---

## Leseübung (10 Minuten)

Ab dieser Etappe ersetzt regelmäßig eine Leseübung die Transferaufgabe. **Du schreibst nichts.** Du liest und erklärst.

Für dein eigentliches Ziel ist das die wichtigere Fähigkeit — sie wird nirgends geübt, weil Kurse einen immer schreiben lassen.

**Teil 1 — Ein fremdes Objekt lesen**

```python
class Villager:
    def __init__(self, name, trust=0):
        self.name = name
        self.trust = trust
        self._gesagt = []

    def speak(self, satz):
        self._gesagt.append(satz)
        print(f"{self.name}: {satz}")

    def kennt(self, satz):
        return satz in self._gesagt


npc = Villager("Mara")

if npc.trust > 5:
    npc.speak("Ich glaube dir.")
else:
    npc.speak("Ich kenne dich kaum.")
```

Beantworte, ohne auszuführen:

1. Was ist `npc`, und was ist `Villager`?
2. Woher kommt `trust`, und welchen Wert hat es hier?
3. Was macht der Punkt in `npc.speak(...)` — was passiert dabei mit `npc`?
4. Wie viele Argumente bekommt `speak` beim Aufruf, und wie viele stehen in der Definition? Warum ist das kein Widerspruch?
5. Welcher der beiden Sätze wird ausgegeben? Was passiert, wenn `trust` genau 5 wäre?
6. Was bewirkt der Unterstrich vor `_gesagt`? *(Python erzwingt nichts — es ist ein Signal an den Leser. Welches?)*
7. Was gäbe `npc.kennt("Ich glaube dir.")` nach diesem Ablauf zurück?

**Frage 6 ist die interessanteste.** Der führende Unterstrich ist eine Konvention, die dir in fremdem Code überall begegnet — sie sagt: *das ist Innenleben, fass es von außen nicht an.* Python hindert dich nicht daran, aber wer es trotzdem tut, hat keinen Anspruch darauf, dass es beim nächsten Update noch funktioniert. Diese Unterscheidung zwischen öffentlich und intern brauchst du in Etappe 27, wenn du ein ganzes fremdes Repo einschätzen sollst.

**Teil 2 — Der Unterschied, der zählt (5 Minuten)**

```python
a = Villager("Mara")
b = Villager("Mara")
c = a

print(a is b)
print(a is c)

c.trust = 10
print(a.trust)
```

Sag jede der drei Ausgaben voraus, **bevor** du es ausführst. Dann führ es aus.

Wenn dich das Ergebnis überrascht: Das ist das Aliasing aus Etappe 4, nur mit Objekten statt Listen. Zwei Namen, ein Ding. Und es ist die Vorbereitung auf den Stolperstein, der dich in Etappe 10 erwartet.

---

## Kaputtmachen

Nach jedem Experiment rückgängig machen.

**Experiment 1 — `self` weglassen**
```python
class Player:
    def zeige_namen():
        print("Hallo")

spieler = Player()
spieler.zeige_namen()
```
`TypeError: zeige_namen() takes 0 positional arguments but 1 was given`.

**Lies diese Meldung genau** — sie ist der beste Beweis für Konzept 3. Du hast null Argumente übergeben, Python behauptet, es sei eines gewesen. Welches?

**Experiment 2 — `self.` beim Zugriff vergessen**
```python
def nimm(self, gegenstand):
    inventar.append(gegenstand)     # ohne self.
```
`NameError`. Python sucht eine lokale Variable oder eine globale — und dein Attribut ist weder das eine noch das andere.

**Experiment 3 — Das Attribut, das nie gesetzt wurde**
Lösch `self.hp = 100` aus `__init__` und greif später auf `spieler.hp` zu.

`AttributeError: 'Player' object has no attribute 'hp'`. Vergleich die Meldung mit der aus Experiment 2. Beide sagen „gibt's nicht", aber auf verschiedene Weise — was ist der Unterschied?

**Experiment 4 — Der Tippfehler, der nichts sagt**
```python
spieler.hpp = 40
print(spieler.hp)
```
Kein Fehler. Kein Hinweis. Der Spieler hat jetzt zwei Attribute, eines davon nutzlos, und seine Lebenspunkte sind unverändert.

**Das ist der gefährlichste Fehler dieser Etappe**, weil er sich als „die Zuweisung wirkt nicht" tarnt. Prüf mit `print(spieler.__dict__)`, was das Objekt tatsächlich enthält.

**Experiment 5 — Klasse statt Objekt**
```python
print(Player.name)
```
Du greifst auf den Bauplan zu statt auf ein Ding. Was sagt Python? Und warum ist das ein sinnvoller Fehler?

**Experiment 6 — Zwei Objekte, ein Zustand**
```python
a = Player("Mara")
b = Player("Jorin")
a.hp = 10
print(b.hp)
```
Hier passiert das *Richtige* — jedes Objekt hat eigene Attribute. Führ es aus, damit du es gesehen hast. In Etappe 10 baust du den Fall, in dem es schiefgeht.

**Experiment 7 — Die leere Klasse**
```python
class Schadensrechner:
    def berechne(self, angriff, ruestung):
        return max(0, angriff - ruestung)

r = Schadensrechner()
print(r.berechne(10, 3))
```
Es funktioniert. Zähl trotzdem: Wie viele Zeilen und wie viele Schritte brauchst du gegenüber einer schlichten Funktion? Was ist der Gewinn?

**Experiment 8 — `__repr__` entfernen**
Nimm sie heraus und leg drei Spieler in eine Liste. `print(liste)`. Setz sie wieder ein und wiederhol es.

**Das ist das Experiment, das dich überzeugt**, `__repr__` in jede Klasse zu schreiben, die du in den nächsten zwanzig Etappen baust.

**Experiment 9 — Zwei Wahrheiten**
Lass versehentlich das alte `aktueller_ort` stehen und pfleg gleichzeitig `spieler.ort`. Bewege dich, und lass beide ausgeben.

Sie laufen auseinander. **Genau davor warnt die Design-Entscheidung** — und genau so entstehen die Fehler, die man tagelang sucht.

---

## Häufige Stolpersteine

| Fehlermeldung / Symptom | Was dahintersteckt | Wo du suchst |
|---|---|---|
| `TypeError: f() takes 0 positional arguments but 1 was given` | `self` in der Definition vergessen | Die Methodendefinition |
| `NameError: name 'inventar' is not defined` | `self.` beim Zugriff vergessen | Innerhalb der Methode |
| `AttributeError: 'Player' object has no attribute 'x'` | Attribut nie in `__init__` gesetzt — oder Tippfehler | `__init__` durchsehen |
| Eine Zuweisung wirkt nicht | Tippfehler legt ein neues Attribut an | `print(objekt.__dict__)` |
| `TypeError: __init__() missing 1 required positional argument` | Beim Erzeugen ein Argument vergessen | `Player()` gegen `Player("Mara")` |
| `<__main__.Player object at 0x...>` | `__repr__` fehlt | Die Klasse |
| Zwei Objekte ändern sich gemeinsam | Beide Namen zeigen auf dasselbe Objekt | Aliasing aus Etappe 4 — war es Absicht? |
| Der Ort stimmt manchmal nicht | Zwei Quellen für dieselbe Information | Alte Variable neben dem Attribut? |
| Das Verhalten hat sich verändert | Beim Umbau ist etwas verrutscht | Verhaltens-Beweis, kleinschrittig zurück |
| `AttributeError: type object 'Player' has no attribute 'name'` | Zugriff auf die Klasse statt auf ein Objekt | Wurde das Objekt erzeugt? |

**Der Debugging-Reflex dieser Etappe** ist neu und ersetzt eine Handvoll `print()`-Zeilen:

```python
print(spieler.__dict__)
```

Das zeigt dir **alle** Attribute eines Objekts mit ihren Werten, auf einen Schlag. Kein Raten, welches Attribut man ausgeben soll — und Tippfehler-Attribute fallen sofort auf, weil sie unerwartet in der Liste stehen.

Im Debugger brauchst du das nicht, dort klappst du `self` auf. Aber wenn du über zwanzig Durchläufe beobachten willst, wie sich ein Objekt verändert, ist diese eine Zeile das richtige Werkzeug.

---

## Ein Blick nach vorne

Deine `World` ist heute ein Behälter mit Methoden. Sie tut nur etwas, wenn du sie fragst.

In **Etappe 10** bekommen Spieler und Welt echte Bestandteile: `Inventory`, `Equipment`. Ein Objekt, das andere Objekte besitzt — das ist **Komposition**, und es ist wichtiger als die Vererbung, die alle für den Kern der Objektorientierung halten. Dort lauert auch der berühmteste Python-Stolperstein überhaupt, und du wirst ihn nur verstehen, weil Etappe 4 und die Leseübung von heute saßen.

In **Etappe 11** bekommen deine Gegenstände eigene Klassen, und `__repr__` bekommt Gesellschaft: `__eq__`, `__len__`, `__iter__`. Danach liest sich dein Inventar wie eine eingebaute Datenstruktur.

In **Etappe 12** wird aus deiner `World` etwas, das lebt:

```python
class World:
    def tick(self):
        self.zeit += 1
        for npc in self.npcs:
            npc.update(self)
```

Drei Zeilen — und das gesamte Dorf beginnt, sich ohne dich zu bewegen. Diese drei Zeilen sind nur deshalb so kurz, weil du heute den Behälter gebaut hast, an dem alles hängt.

In **Etappe 19** stellst du fest, dass deine Klassenstruktur bestimmt, wie der Spielstand aussieht. Was heute zu `Player` gehört und was zu `World`, entscheidet dort über die Form der JSON-Datei. Design-Entscheidungen haben lange Schatten.

---

## Abschluss

**`GELERNT.md`:**
Zwei bis drei Sätze. Zusätzlich diesmal:

- Deine Entscheidung, wo der Zustand wohnt — mit Begründung
- Welche Funktion **keine** Methode geworden ist und warum
- Die Parameterzahl vorher und nachher
- Und die Frage dieser Etappe: **Was hat `self` für dich geklärt, das vorher unklar war?**

Der letzte Punkt lohnt sich. Für die meisten ist es der Moment, in dem `.append()` und `.lower()` rückwirkend Sinn ergeben — sieben Etappen lang benutzt, ohne zu wissen, was der Punkt bedeutet.

**Die sechs Begriffe dieser Etappe**, zum Selbstprüfen. Deck die rechte Spalte ab und erklär jeden in einem Satz:

| Begriff | In einem Satz |
|---|---|
| **Klasse** | Der Bauplan — beschreibt, was ein Ding hat und kann |
| **Objekt** | Ein konkretes Ding nach diesem Bauplan, mit eigenen Werten |
| **Attribut** | Was das Objekt weiß — überlebt den Methodenaufruf |
| **Methode** | Was das Objekt kann — eine Funktion, die zu ihm gehört |
| **`__init__`** | Läuft beim Erzeugen und bringt das Objekt in einen brauchbaren Anfangszustand |
| **`self`** | Das Objekt selbst, von innen betrachtet — Python reicht es automatisch als erstes Argument |

Wenn eine Erklärung stockt, ist das keine Schande — es ist die Stelle, die du nochmal ansehen solltest.

**Commit:**
```bash
git add .
git commit -m "Etappe 9: Player und World als Objekte"
git push
```

Schau dir `git show --stat` an. Bei einem gelungenen Umbau sind ungefähr so viele Zeilen verschwunden wie dazugekommen — der Code ist nicht länger geworden, sondern anders geordnet.

---

## Wenn du mehr willst

Optional, erst bei grünem Selbsttest.

**Ein `status`-Befehl.** Gibt aus, was der Spieler gerade ist: Name, Lebenspunkte, Ort, Anzahl Gegenstände. Drei Zeilen, wenn `Player` sauber steht — und ein guter Test dafür, ob es das tut.

**Die NPCs als Objekte.** Deine drei Überlebenden sind bisher vermutlich Strings oder Dictionary-Einträge. Eine `Villager`-Klasse mit `name`, `ort` und einer `spricht()`-Methode ist genau die Übung von heute, nur ein zweites Mal.

**Mach es, wenn du Zeit hast** — nicht weil es heute nötig wäre, sondern weil Etappe 12 sie ohnehin braucht. Dort bekommen sie `update()` und einen Tagesablauf, und dann ist die Klasse schon da.

**Eine Klasse für etwas völlig anderes.** Zehn Minuten, Wegwerf-Datei, und bewusst *kein* Spielthema: `Buch`, `Fahrkarte`, `Kaffeemaschine`. Zwei Attribute, ein sinnvoller Anfangszustand, eine Methode. Dann zwei Objekte erzeugen und bei einem etwas ändern.

**Der Prüfstein:** Wenn du dabei merkst, dass du eigentlich nur `Player` umbenennst — Name, Lebenspunkte, Ort mit anderen Wörtern —, hast du die Übung nicht gemacht. Eine Fahrkarte hat keine Lebenspunkte. Sie hat einen Zielbahnhof, eine Gültigkeit und vielleicht eine Methode `entwerten()`, die einen Zustand kippt.

Das ist die Probe darauf, ob du das Konzept außerhalb deines Spiels anwenden kannst — dieselbe Idee wie bei den Transferaufgaben der letzten Etappen, nur diesmal freiwillig.

**Eine Methode, die eine andere ruft.** In `World`: eine Methode `beschreibe_aktuellen_ort()`, die intern `self.spieler.ort` benutzt und die Ortstabelle befragt.

Klingt banal, ist aber der erste Fall, in dem ein Objekt ein anderes Objekt nach etwas fragt — `self.spieler.ort` sind zwei Punkte hintereinander. Genau so sieht der Code aus, den du in Etappe 27 in fremden Projekten liest.

**`print(spieler.__dict__)` gegen `print(spieler)`.** Bau beides ein und vergleich. Das eine zeigt alles roh, das andere zeigt, was du für wichtig hältst. Beide haben ihren Platz — und die Entscheidung, was in `__repr__` gehört, ist eine Form von Rücksicht auf dein zukünftiges Ich.

---

> **Nächste Etappe:** [Etappe 10 — Komposition](etappe-10-komposition.md) · Objekte in Objekten
> Dort bekommt dein Spieler ein Inventar, das selbst ein Objekt ist. Und du triffst den berühmtesten Stolperstein, den Python zu bieten hat.
