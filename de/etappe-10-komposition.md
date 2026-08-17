# Etappe 10 — Komposition

> **Block 2: Objekte und Zeit** · Etappe 10 von 30 · [← Etappe 9](etappe-09-alles-wird-zum-objekt.md) · [Lehrplan](../RPG_Lehrplan.md) · [Etappe 11 →](etappe-11-vererbung.md)

**Boot.dev:** Objekte in Objekten, Komposition
**Zeitaufwand:** 5–7 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 9 abgeschlossen, `Player` und `World` laufen

---

## Worum es geht

Dein Spieler hat seit gestern Attribute: einen Namen, Lebenspunkte, einen Ort. Und eine Liste.

```python
self.inventar = []
```

Diese Liste ist der Bruch in deinem Entwurf. Alles andere am Spieler ist ein einzelner Wert — aber das Inventar ist ein *Ding mit eigenen Regeln*. Es hat eine Obergrenze von zehn. Es weiß, ob etwas darin ist. Es kann voll sein. Diese Regeln stehen gerade verstreut in deinen Methoden, weil eine nackte Liste sie nicht kennt.

**Heute bekommt es einen eigenen Bauplan.**

```python
class Player:
    def __init__(self, name):
        self.name = name
        self.inventar = Inventory()
        self.ausruestung = Equipment()
```

Ein Objekt, das andere Objekte besitzt. Das heißt **Komposition**, und es ist der wichtigste Baustein der objektorientierten Programmierung — wichtiger als die Vererbung, die alle dafür halten.

**Warum ausgerechnet vorher?** Fast jede Einführung beginnt mit Vererbung, weil sie spektakulär wirkt: Klassen, die von Klassen abstammen, ein Stammbaum, ein großes Wort. In echtem Python-Code ist Komposition dagegen der Normalfall. Sie ist einfacher zu verstehen, leichter zu debuggen und flexibler. **Wenn du nur eines von beiden wirklich beherrschst, soll es dieses sein** — deshalb kommt es zuerst.

**Und noch etwas erwartet dich heute.** Am Ende dieser Etappe steht der berühmteste Stolperstein, den Python zu bieten hat. Er ist zwei Zeilen lang, sieht völlig harmlos aus, und er wird dich verblüffen. Du kannst ihn nur verstehen, weil du Etappe 4 hinter dir hast — und wenn du ihn verstanden hast, gehörst du zu einer Minderheit unter den Python-Anfängern.

---

## Der lange Bogen

| Was du heute baust | Wo es wieder auftaucht |
|---|---|
| `Inventory` als eigene Klasse | **Etappe 11** — nimmt `Item`-Objekte statt Strings auf |
| `Equipment` mit Slots | **Etappe 21** — Waffe und Rüstung wirken im Kampf |
| `None` als „bewusst nichts" | **Etappe 19** — wird zu `null` in JSON; **Etappe 20** — Rückgabewert bei Fehlschlag |
| `is None` statt `== None` | **Etappe 11** — dort erfährst du, warum `==` unzuverlässig sein kann |
| `self.position` als Tuple | **Etappe 14** — Bewegung durch das Minenraster |
| Delegation (`player.nimm` ruft `inventory.hinzufuegen`) | **Etappe 12** — `World.tick()` delegiert an jeden NPC |
| Der Stolperstein mit Standardwerten | **Etappe 16** — Bug-Jagd mit versehentlich geteilten Objekten |
| `None` als Wächter für Standardwerte | **Etappe 23** — `field(default_factory=list)` löst dasselbe Problem |
| Entscheidung: eigenes Ding oder Attribut | **Etappe 11** — verdient es eine eigene Klasse?; **Etappe 24** — eine eigene Datei? |
| Entscheidung: wer erzeugt die Bestandteile | **Etappe 26** — bestimmt, wie leicht sich das testen lässt |

**Zwölf Schulden werden heute eingelöst** — der bisherige Rekord:

Aus **Etappe 4** das Herzstück: mutable und immutable. Damals war es ein Experiment mit zwei Listen. Heute ist es die Erklärung für einen Fehler, den du sonst nie verstehen würdest. Dazu `.copy()`, das dort nur erwähnt wurde.

Aus **Etappe 6**: das Tuple für Koordinaten und die Unterscheidung zwischen *das Objekt ändern* und *den Namen neu zuweisen*.

Aus **Etappe 7 und 9**: Standardwerte in Parameterlisten — mit der Warnung, die dort zweimal stand und heute ihren Grund bekommt.

Aus **Etappe 9**: die `Player`-Klasse, die echte Bestandteile bekommt. Die Frage „wem gehört diese Information?", jetzt eine Ebene tiefer. Das Prinzip vom nicht halb fertigen Objekt. Und das Aliasing aus der Leseübung — zwei Namen, ein Ding —, das gleich zum Hauptdarsteller wird.

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

### Frage 1: Was ist ein eigenes Ding, was nur ein Attribut?

Die Fortsetzung der Zuordnungsübung aus Etappe 9, eine Ebene tiefer. Damals ging es darum, wem eine Information gehört. Jetzt: **Verdient sie einen eigenen Bauplan?**

```python
self.hp = 100                    # ein Wert
self.inventar = Inventory()      # ein Ding
```

Was spricht für ein eigenes Ding? Wenn es **eigene Regeln** hat. Ein Inventar kann voll sein, es hat eine Obergrenze, es kennt sich selbst. Lebenspunkte sind eine Zahl, die man vergleicht — mehr nicht.

Geh deinen Spieler und deine Welt durch und entscheide für jedes Attribut:

| Attribut | Eigene Klasse? | Warum |
|---|:---:|---|
| `name` | nein | Ein String mit keinen eigenen Regeln |
| `inventar` | **ja** | Obergrenze, Prüfungen, eigenes Verhalten |
| `ausruestung` | **ja** | Feste Slots, Regeln, was wohin darf |
| `hp` | nein | Eine Zahl — vorerst |
| `orte` | ? | Deine Entscheidung |

**Die Zeile mit `orte` ist die interessante.** Ein Dictionary von Orten hat durchaus Regeln — es könnte prüfen, ob ein Ausgang ins Leere zeigt. Aber es ist auch reine Daten, die in Etappe 25 in eine Datei wandern. Beide Antworten sind vertretbar; entscheide bewusst und schreib die Begründung in `GELERNT.md`.

**Und die Warnung, die zu jeder Etappe dieses Blocks gehört:** Nicht alles verdient eine Klasse. Ein Objekt, dessen einzige Aufgabe es ist, eine Zahl aufzubewahren, ist eine Zahl mit Zeremonie.

### Frage 2: Wer erzeugt die Bestandteile?

```python
# A — der Spieler besorgt sich sein Inventar selbst
class Player:
    def __init__(self, name):
        self.inventar = Inventory()

# B — der Spieler bekommt es gereicht
class Player:
    def __init__(self, name, inventar):
        self.inventar = inventar
```

**A ist bequemer.** `Player("Mara")` genügt, und niemand kann vergessen, ein Inventar mitzugeben.

**B ist flexibler.** Du kannst einem Spieler ein vorbereitetes Inventar geben — eines mit besonderer Größe, eines aus einem Spielstand, oder beim Testen ein Attrappen-Inventar, das mitzählt, was hineingelegt wurde.

**Meine Empfehlung für heute: A**, weil es zum Prinzip aus Etappe 9 passt (kein halb fertiges Objekt) und weil du bei B eine Sache mehr richtig machen musst.

**Aber merk dir die Frage.** Sie hat einen Namen und eine ausgewachsene Antwort, und du wirst ihr in echtem Code ständig begegnen. In Etappe 26 merkst du den Unterschied zum ersten Mal praktisch: Ein Objekt, das sich seine Bestandteile selbst besorgt, lässt sich schwerer testen als eines, dem man sie geben kann. **Schwer testbarer Code ist fast immer ein Hinweis auf zu enge Verbindungen** — der Test ist die Rückmeldung, nicht das Problem.

---

## Die Konzepte

### 1. „hat ein" — das Muster hinter allem

Es gibt zwei Arten, wie Klassen zueinander stehen können:

> **„ist ein"** — ein Schwert *ist ein* Gegenstand. Das ist **Vererbung**, und die kommt in Etappe 11.
> **„hat ein"** — ein Spieler *hat ein* Inventar. Das ist **Komposition**, und darum geht es heute.

Der Test ist einfach: Setz die beiden Klassen in einen Satz und schau, welches Wort passt.

```text
Ein Spieler ist ein Inventar.     ← Unsinn
Ein Spieler hat ein Inventar.     ← richtig
```

**Und du hast das gestern schon gebaut, ohne dass es einen Namen hatte.** In Etappe 9 stand in `World.__init__` die Zeile `self.spieler = spieler`. Die Welt *hat* einen Spieler. Das war bereits Komposition — heute machst du es bewusst und gibst den Bestandteilen eigene Regeln.

### 2. Ein Objekt als Attribut

Technisch ist daran nichts Neues. Ein Attribut kann jeden Wert halten — eine Zahl, einen String, eine Liste. Und eben auch ein Objekt.

```python
class Inventory:
    def __init__(self, kapazitaet=10):
        self.items = []
        self.kapazitaet = kapazitaet

    def hinzufuegen(self, gegenstand):
        if len(self.items) >= self.kapazitaet:
            return False, "Du kannst nichts mehr tragen."
        self.items.append(gegenstand)
        return True, f"Du nimmst {gegenstand}."


class Player:
    def __init__(self, name):
        self.name = name
        self.inventar = Inventory()
```

Beim Erzeugen eines Spielers wird jetzt automatisch ein Inventar miterzeugt. `Player("Mara")` löst `Inventory()` aus, ohne dass man es hinschreibt.

**Was du dabei gewonnen hast:** Die Regel „maximal zehn Gegenstände" stand vorher in einer `Player`-Methode. Jetzt steht sie dort, wo sie hingehört — im Inventar selbst. Wenn du sie ändern willst, gibt es genau eine Stelle.

### 3. Die Punktkette — und wo sie aufhört

Ein Objekt in einem Objekt bedeutet: mehrere Punkte hintereinander.

```python
spieler.inventar.kapazitaet          # zwei Punkte, in Ordnung
spieler.inventar.items.append("brot")  # drei — und hier fängt es an, weh zu tun
```

Die zweite Zeile ist technisch einwandfrei und trotzdem ein schlechtes Zeichen. Sie greift durch zwei Objekte hindurch bis auf die Liste ganz unten — und umgeht damit die Regeln, die das Inventar gerade bekommen hat. Die Obergrenze? Wird nicht geprüft. Die Rückmeldung? Gibt es nicht.

**Die Faustregel, die dir das erspart:**

> **Rede mit deinen Nachbarn, nicht mit den Nachbarn deiner Nachbarn.**

Statt durchzugreifen, fragst du das Objekt, dem die Sache gehört:

```python
erfolg, meldung = spieler.inventar.hinzufuegen("brot")
```

Und meistens noch eine Stufe kürzer, indem der Spieler weiterreicht:

```python
class Player:
    def nimm(self, gegenstand):
        return self.inventar.hinzufuegen(gegenstand)
```

Das heißt **Delegation** — der Spieler tut nicht selbst, was das Inventar besser kann, sondern gibt es weiter. Der Rest deines Spiels sagt `spieler.nimm("brot")` und muss nicht wissen, dass es intern ein Inventar gibt.

**Merk dir das Muster.** In Etappe 12 macht `World.tick()` genau dasselbe: Sie tickt nicht selbst herum, sondern ruft bei jedem NPC dessen `update()` auf. Delegation ist der Grund, warum diese Methode nur drei Zeilen lang ist.

### 4. `None` — bewusst nichts

Du kennst `None` seit Etappe 7 als das, was eine Funktion ohne `return` zurückgibt. Heute bekommt es eine aktive Rolle.

```python
slots = {"hand": None, "kopf": None, "koerper": None}
```

`None` heißt: **hier ist bewusst nichts.** Und das ist etwas völlig anderes als:

| Wert | Bedeutet |
|---|---|
| `None` | Hier ist nichts, und das ist ein gültiger Zustand |
| `0` | Hier ist eine Zahl, und sie ist null |
| `""` | Hier ist ein Text, und er ist leer |
| `False` | Hier ist ein Wahrheitswert, und er ist falsch |
| `[]` | Hier ist eine Liste, und sie ist leer |

**Der Unterschied ist praktisch, nicht philosophisch.** Ein Slot mit `None` ist frei. Ein Slot mit `0` enthält einen Gegenstand namens Null. Wenn du beides gleich behandelst, weil beide in einem `if` als falsch gelten, hast du einen Fehler, den du lange suchst.

Genau davor warnt die Truthy-Liste aus Etappe 2: `None`, `0`, `""`, `[]` gelten alle als falsch. `if slot:` unterscheidet sie nicht. `if slot is None:` schon.

**Weitere Stellen, an denen `None` heute richtig ist:** kein aktives Ziel, kein laufender Dialog, kein Gegenstand in der Hand. Überall dort, wo „noch nichts" ein normaler Zustand ist und kein Fehler.

### 5. `is None` gegen `== None`

```python
if waffe is None:      # richtig
if waffe == None:      # funktioniert meistens, ist aber falsch
```

Das ist kein Stilstreit, und der Grund ist konkret.

**`==` fragt: haben diese beiden denselben *Wert*?**
**`is` fragt: sind das *dasselbe Ding*?**

Bei `None` ist die zweite Frage die richtige, weil es in einem laufenden Python-Programm **genau ein einziges `None` gibt**. Nicht viele gleiche — eines. Wenn etwas `None` ist, dann ist es dieses eine. Identität ist hier die genauere Prüfung.

**Und der praktische Grund, der dich betrifft:** `==` lässt sich von einer Klasse überschreiben. In Etappe 11 lernst du `__eq__` kennen — eine Methode, mit der du selbst bestimmst, was `==` bedeutet. Eine Klasse mit ungeschickt geschriebenem `__eq__` kann sich bei `== None` unerwartet verhalten. `is` lässt sich nicht überschreiben und sagt immer die Wahrheit.

Nebenbei ist `is` auch schneller, aber das ist bei deinem Spiel egal. Nimm es, weil es korrekt ist.

**Dieselbe Regel gilt für `is not None`** — und nicht `!= None`.

### 6. `Equipment` und die Slots

```python
class Equipment:
    def __init__(self):
        self.slots = {"hand": None, "kopf": None, "koerper": None}

    def anlegen(self, slot, gegenstand):
        if slot not in self.slots:
            return False, f"Es gibt keinen Platz namens {slot}."
        if self.slots[slot] is not None:
            return False, f"Dort trägst du schon {self.slots[slot]}."
        self.slots[slot] = gegenstand
        return True, f"Du legst {gegenstand} an."
```

Ein Dictionary mit festen Schlüsseln und `None` als „frei". Die Schlüssel stehen fest, die Werte wechseln — genau die Struktur aus Etappe 5, nur kleiner.

**Was heute noch nicht geht:** Zu prüfen, ob ein Gegenstand *überhaupt* in die Hand gehört. Dafür müsste ein Gegenstand wissen, was er ist — und Gegenstände sind bei dir immer noch Strings. Das kommt in Etappe 11, wenn aus `"schwert"` ein `Weapon`-Objekt wird.

Heute reicht es, dass jeder Slot höchstens eines aufnimmt.

### 7. Die Position als Tuple

```python
self.position = (0, 0)
```

Die Schuld aus Etappe 6. Dein Spieler bekommt neben `ort` (dem Namen des Ortes) eine Position aus zwei Zahlen. Im Dorf braucht er sie nicht — in Etappe 14, in der Mine, ist sie das Fundament der Bewegung.

**Und hier zahlt die Unterscheidung aus Etappe 6:**

```python
self.position[0] = 5             # TypeError — Tuples ändern sich nicht
self.position = (5, 7)           # so geht es
```

Das Tuple ist unveränderlich, der Name nicht. Bei jedem Schritt ersetzt du das ganze Tuple, statt eine Zahl darin auszutauschen. Genau so wird es in Etappe 14 laufen.

**Warum überhaupt jetzt schon?** Weil sie zum Spieler gehört und du sie sonst später nachrüsten musst. Ein Attribut, das heute `(0, 0)` ist und niemanden stört, ist billiger als ein Umbau in vier Wochen.

### 8. Der Stolperstein ⭐

Jetzt kommt er. Lies langsam — es sind vier Zeilen.

```python
class Player:
    def __init__(self, name, inventar=Inventory()):
        self.name = name
        self.inventar = inventar
```

Das sieht vernünftig aus: *Wenn niemand ein Inventar mitgibt, nimm ein neues.* Genau das tut es nicht.

```python
mara = Player("Mara")
jorin = Player("Jorin")

mara.inventar.hinzufuegen("brot")
print(jorin.inventar.items)      # ['brot']
```

**Jorin hat Maras Brot.**

Kein Absturz. Keine Meldung. Zwei Spieler, die sich ein Inventar teilen, ohne dass irgendwo steht, dass sie das tun. Fehler vom Typ 3 in seiner reinsten Form — und einer, den man ohne Erklärung stundenlang sucht.

**Deine erste Reaktion darf falsch sein.** Die meisten denken an dieser Stelle: *„Aber ich habe doch nur bei Mara etwas hinzugefügt!"* Genau das sollst du denken — der Gedanke ist der Beweis, dass dein Modell von der Sache noch nicht stimmt.

Und die Frage, mit der du weitermachst, lautet **nicht** „welche Zeile muss ich ändern?", sondern:

> **Wie oft wurde `Inventory()` eigentlich ausgeführt?**

Wer die Zeile repariert, ohne diese Frage beantwortet zu haben, baut denselben Fehler in vier Wochen wieder — nur an einer Stelle, wo er schwerer zu sehen ist.

### 9. Warum das passiert

Die Erklärung ist kurz, und du hast alle Teile davon seit Etappe 4.

> **Der Standardwert wird genau einmal ausgewertet — nämlich dann, wenn Python die `def`-Zeile liest. Nicht bei jedem Aufruf.**

Das heißt: In dem Moment, in dem deine Klasse definiert wird, läuft `Inventory()` einmal. Es entsteht **ein** Inventar. Dieses eine wird ab dann jedem Spieler zugewiesen, der keines mitbekommt.

Und weil ein Inventory **mutable** ist — veränderbar, wie die Liste aus Etappe 4 —, wirkt jede Änderung bei allen. Es sind nicht viele gleiche Inventare. Es ist eines mit vielen Namen.

```python
a = [1, 2]
b = a
b.append(3)
print(a)          # [1, 2, 3]   ← Etappe 4
```

**Es ist derselbe Mechanismus.** Damals waren es zwei Variablennamen, heute sind es zwei Objekte, die auf dasselbe Ding zeigen.

**So sieht es aus, wenn es richtig ist:**

```text
mara ──→ Player ──→ Inventory ──→ ['brot']

jorin ─→ Player ──→ Inventory ──→ []
```

**Und so, wenn der Standardwert zuschlägt:**

```text
mara ──→ Player ──┐
                  ├──→ Inventory ──→ ['brot']
jorin ─→ Player ──┘
```

**Beachte, wie weit das reicht.** Geteilt wird nicht nur das `Inventory` — sondern alles, was daran hängt. Die Liste darin gehört beiden. Ein Gewicht, ein Zähler, alles.

> **Wenn zwei Objekte sich einen Bestandteil teilen, teilen sie automatisch auch dessen Bestandteile.**

Das Teilen pflanzt sich nach unten fort, durch beliebig viele Ebenen. Deshalb ist ein versehentlich geteiltes Objekt so unangenehm: Der Schaden zeigt sich oft ganz woanders, tief in einer Struktur, in die niemand geschaut hat. In Etappe 16 wartet genau so ein Fall auf dich, und in Etappe 19 wirst du beim Speichern wieder daran denken müssen. Wenn dir das Experiment aus Etappe 4 im Gedächtnis geblieben ist, hast du diesen Fehler gerade verstanden — und die meisten Python-Anfänger haben das nicht.

**Und deshalb gilt die Regel aus Etappe 7 und 9 unverändert:** Standardwerte nur mit Zahlen, Strings, `True`/`False`, Tuples oder `None`. Also nur mit **unveränderlichen** Werten. Bei denen kann nichts passieren, weil sich nichts ändern lässt.

### 10. Die Lösung — und warum `None` sie ist

```python
class Player:
    def __init__(self, name, inventar=None):
        self.name = name
        self.inventar = inventar if inventar is not None else Inventory()
```

Der Standardwert ist jetzt `None` — unveränderlich, harmlos, einmal ausgewertet ohne Folgen. Und **innerhalb** der Methode, also bei jedem Aufruf neu, entsteht ein frisches Inventar.

Man schreibt es oft auch so, was dasselbe bedeutet:

```python
def __init__(self, name, inventar=None):
    if inventar is None:
        inventar = Inventory()
    self.inventar = inventar
```

**Hier schließt sich der Kreis dieser Etappe.** `None` war in Konzept 4 „bewusst nichts". Jetzt ist es das Werkzeug, das den Stolperstein entschärft: Es steht für *„es wurde nichts mitgegeben"* — und genau das musst du erkennen können, um dann selbst etwas zu erzeugen.

Deshalb ist es auch der Moment für `is None` und nicht `== None`. Was, wenn jemand ein leeres Inventar mitgibt? Bei `if not inventar:` würdest du es wegwerfen und ein neues bauen, weil ein leeres Inventar in einem `if` als falsch gilt. `is None` unterscheidet sauber zwischen *„nichts mitgegeben"* und *„etwas Leeres mitgegeben"*.

**Merk dir dieses Muster.** Es heißt *Wächter* oder *Sentinel* und begegnet dir in fremdem Code ständig. In Etappe 23 siehst du die moderne Kurzform dafür: `field(default_factory=list)` löst genau dasselbe Problem, nur mit einer Zeile.

### 11. `.copy()` — wenn du wirklich eine Kopie willst

Die Schuld aus Etappe 4, jetzt mit Anwendung.

```python
neues = Inventory()
neues.items = altes.items.copy()      # eigene Liste, gleiche Inhalte
```

Manchmal *willst* du zwei Objekte, die dasselbe enthalten, aber unabhängig sind — beim Laden eines Spielstands, beim Duplizieren einer Ausrüstung.

**Eine Warnung, die du heute nur zur Kenntnis nimmst:** `.copy()` kopiert eine Ebene. Enthält deine Liste selbst Objekte, zeigen beide Kopien danach auf **dieselben** Objekte. Das nennt man eine flache Kopie. Für heute reicht das; in Etappe 19 beim Speichern und Laden wird es nochmal Thema.

### 12. Warum Komposition vor Vererbung

Zum Schluss die Einordnung, die dir Etappe 11 erleichtert.

Vererbung wirkt mächtiger. Man baut Stammbäume, spart Code, und das Wort klingt nach richtiger Informatik. Aber sie hat einen Preis: Eine Unterklasse ist **fest** an ihre Oberklasse gebunden. Ändert sich oben etwas, ändert es sich unten mit — auch dort, wo du es nicht wolltest.

Komposition ist lockerer. Ein Spieler *hat* ein Inventar; man könnte ihm ein anderes geben, ohne dass die `Player`-Klasse davon etwas merkt.

**Die Faustregel, die sich in der Praxis durchgesetzt hat:**

> **Bevorzuge Komposition gegenüber Vererbung.**

Das heißt nicht „nie vererben" — in Etappe 11 baust du einen Fall, wo Vererbung genau richtig ist. Es heißt: Wenn beides ginge, nimm Komposition. Sie ist leichter zu ändern, leichter zu testen und leichter zu lesen.

Und du hast jetzt eine Vergleichsgrundlage. Wenn Etappe 11 fragt *„brauchen wir hier Vererbung überhaupt?"*, kannst du die Frage beantworten — weil du die Alternative gebaut hast.

---

## Dein Auftrag

**Der Verhaltens-Beweis aus Etappe 7 gilt wieder.** Befehlsfolge durchspielen, Ausgabe sichern, umbauen, vergleichen.

**Schritt 1 — Die Zuordnung**
Die Tabelle aus Frage 1 ausfüllen. Zehn Minuten, kein Code. Du weißt danach, was heute zu tun ist.

**Schritt 2 — `Inventory`**
Eine Klasse mit `items`, `kapazitaet` und den Methoden, die es braucht: hinzufügen, entfernen, prüfen ob etwas drin ist, anzeigen.

**Und hier eine Auflage:** Die Obergrenze von zehn Gegenständen gehört ab jetzt **ins Inventar**, nicht in eine `Player`-Methode. Wenn die Regel danach noch an zwei Stellen steht, ist sie an einer zu viel.

Vergiss `__repr__` nicht. Aus Etappe 9 weißt du, warum.

**Schritt 3 — Der Spieler bekommt es**
`self.inventar = Inventory()` in `Player.__init__`. Dann alle Stellen anpassen, an denen bisher direkt auf die Liste zugegriffen wurde.

Danach muss das Spiel wieder vollständig laufen. **Prüf gegen den Verhaltens-Beweis, bevor du weitermachst.**

**Schritt 4 — Delegation**
`spieler.nimm(...)` und `spieler.ablege(...)` reichen an das Inventar weiter, statt selbst zu arbeiten.

Der Rest deines Spiels soll danach nicht mehr wissen, dass es ein `Inventory`-Objekt gibt. Wenn irgendwo noch `spieler.inventar.items` steht, ist die Delegation nicht fertig.

**Schritt 5 — `Equipment`**
Drei Slots, `None` als frei, eine `anlegen()`- und eine `ablegen()`-Methode.

Bau einen Befehl dazu — `lege an schwert` oder wie deine Befehlssprache aus Etappe 3 es vorsieht. Was angelegt ist, soll nicht mehr im Inventar liegen; es wandert von einem Ding ins andere, genau wie in Etappe 4 zwischen zwei Listen.

**Schritt 6 — Die Position**
`self.position = (0, 0)` im Spieler. Sie tut heute nichts. Setz einen Kommentar auf Etappe 14.

**Schritt 7 — Den Stolperstein bauen** ⭐
Jetzt absichtlich der Fehler aus Konzept 8. Schreib `inventar=Inventory()` in die Parameterliste, erzeug zwei Spieler, gib einem etwas, schau beim anderen nach.

**Führ das wirklich aus.** Nicht lesen und nicken — ausführen und sich wundern. Es ist der Fehler, den du in Etappe 16 bei jemand anderem wiedererkennen sollst.

Dann repariere ihn mit dem Wächter aus Konzept 10.

**Schritt 8 — Der Durchgang**
Verhaltens-Beweis prüfen. Alle Befehle aus Etappe 3 bis 5 einzeln durchgehen.

Und der Test dieser Etappe: **Ändere die Inventar-Obergrenze von 10 auf 5.** Wie viele Stellen musst du anfassen? Wenn die Antwort „eine" ist, hast du es richtig gebaut.

---

## Was NICHT in diese Etappe gehört

- ❌ Vererbung, `super()`, Unterklassen → **Etappe 11**
- ❌ `Item`-Klassen mit Gewicht und Schaden → **Etappe 11**
- ❌ `__eq__`, `__len__`, `__contains__`, `@property` → **Etappe 11**
- ❌ Prüfen, ob ein Gegenstand in einen bestimmten Slot *darf* → **Etappe 11**
- ❌ `tick()` und Weltzeit → **Etappe 12**
- ❌ `@dataclass` → **Etappe 23**
- ❌ Klassen in eigene Dateien → **Etappe 24**
- ❌ Neue Spielfunktionen jeder Art

**Besonders verlockend wird die Slot-Prüfung.** Sobald `Equipment` steht, willst du verhindern, dass ein Brot auf den Kopf kommt. Dafür müsste ein Gegenstand wissen, was er ist — und das geht erst, wenn er ein Objekt ist. Etappe 11.

**Und `__len__`.** Wenn `Inventory` erst mal existiert, ist `len(spieler.inventar)` das Naheliegende. Es geht noch nicht, und das ist Absicht: Warum es geht und wie man es einschaltet, ist eine der Kernfragen von Etappe 11.

---

## Selbsttest

- [ ] Der Verhaltens-Beweis wurde **vor** dem Umbau angelegt
- [ ] Die Ausgabe nach dem Umbau ist mit der davor identisch
- [ ] `Inventory` und `Equipment` existieren als eigene Klassen
- [ ] Die Obergrenze steht an genau einer Stelle — im Inventar
- [ ] Beide neuen Klassen haben ein `__repr__`
- [ ] `spieler.nimm()` delegiert, statt selbst zu arbeiten
- [ ] Nirgends im Spiel steht `spieler.inventar.items`
- [ ] Freie Slots enthalten `None`, nicht `""` oder `0`
- [ ] Alle Prüfungen auf leere Slots benutzen `is None` oder `is not None`
- [ ] `self.position` ist ein Tuple
- [ ] Du hast den Stolperstein selbst gebaut, ausgeführt und gesehen
- [ ] Kein Standardwert ist ein veränderbares Objekt
- [ ] Der Wächter mit `None` ist eingebaut
- [ ] Die Obergrenze von 10 auf 5 zu ändern kostet genau eine Zeile
- [ ] Die Zuordnungstabelle aus Frage 1 steht in `GELERNT.md`

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten:

1. **Unterschied „ist ein" ↔ „hat ein"?** Nenn je ein Beispiel aus deinem Spiel.
2. **Warum `is None` statt `== None`?** Nenn den Grund, der mit Etappe 11 zu tun hat.
3. **Was passiert, wenn zwei Spieler versehentlich dasselbe Inventory-Objekt teilen?** Und woran merkt man es?
4. **Warum ist `def __init__(self, inv=Inventory())` falsch?** Wann genau wird der Standardwert ausgewertet?
5. **Warum löst `None` als Standardwert das Problem?**
6. **Was ist Delegation, und was gewinnst du dadurch?**
7. **Warum ist `spieler.inventar.items.append("brot")` ein schlechtes Zeichen**, obwohl es funktioniert?
8. **Wann verdient ein Attribut eine eigene Klasse?**
9. **Was heißt „bevorzuge Komposition gegenüber Vererbung"** — und heißt es „nie vererben"?
10. **Warum ist `None` etwas anderes als `0`, `""` und `[]`?** Nenn einen Fall aus deinem Spiel, wo der Unterschied zählt.

11. **Werden Standardwerte wie `name="Mara"` auch geteilt?** Wenn ja — warum merkt man es nie?

**Frage 4 ist die wichtigste dieser Etappe**, und die vollständige Antwort besteht aus zwei Teilen: *wann* der Standardwert ausgewertet wird (einmal, beim Lesen der `def`-Zeile) und *warum* das nur bei veränderbaren Werten schadet. Wer beides erklären kann, hat den berühmtesten Stolperstein von Python verstanden — und hat gleichzeitig bewiesen, dass Etappe 4 saß.

---

## Transferaufgabe (15 Minuten)

**Neue Datei, außerhalb des Spiels.** `uebung_10.py`.

**Teil 1 — Zwei Klassen, eine Beziehung**

> Klasse `Rucksack` mit einer Kapazität und einer Methode `hinzufuegen(ding)`, die `True` oder `False` zurückgibt.
> Klasse `Wanderer`, die einen Rucksack besitzt und eine Methode `packe(ding)` hat, die weiterreicht.

Bewusst kein Spielthema. Wenn du merkst, dass du nur `Player` und `Inventory` umbenennst, hast du recht — es *ist* dasselbe Muster. Der Punkt ist, dass du es an etwas anderem wiedererkennst.

**Teil 2 — Der Stolperstein außerhalb des Spiels**

> Bau `Wanderer` einmal absichtlich mit `def __init__(self, name, rucksack=Rucksack())`.
> Erzeug zwei Wanderer. Pack bei einem etwas ein. Schau beim anderen nach.

Sag vorher, was du erwartest. Dann führ es aus.

**Teil 3 — Die drei Fassungen vergleichen**

Schreib `__init__` in drei Varianten und probier jede mit zwei Wanderern:

```python
def __init__(self, name, rucksack=Rucksack()):        # A
def __init__(self, name):                              # B
    self.rucksack = Rucksack()
def __init__(self, name, rucksack=None):               # C
    self.rucksack = rucksack if rucksack is not None else Rucksack()
```

**Welche verhalten sich gleich, welche nicht?** B und C tun bei zwei Wanderern dasselbe — aber nur C erlaubt es, einem Wanderer einen vorbereiteten Rucksack mitzugeben.

Das ist die Design-Entscheidung aus Frage 2, jetzt als Code nebeneinander. Und es ist der Grund, warum C die Fassung ist, die du in fremdem Python am häufigsten siehst.

---

## Kaputtmachen

Nach jedem Experiment rückgängig machen.

**Experiment 1 — Der geteilte Standardwert** ⭐
```python
class Inventory:
    def __init__(self):
        self.items = []

class Player:
    def __init__(self, name, inv=Inventory()):
        self.name = name
        self.inv = inv

a = Player("Mara")
b = Player("Jorin")
a.inv.items.append("brot")
print(b.inv.items)
```

Sag vorher, was du erwartest. Dann führ es aus.

**Danach die entscheidende Zusatzfrage:** Prüf mit `print(a.inv is b.inv)`, ob es wirklich dasselbe Objekt ist. Das ist derselbe `is`-Vergleich wie bei `None` — und hier siehst du, wofür er sonst noch gut ist.

**Experiment 2 — Derselbe Fehler mit einer Liste**
```python
def sammle(ding, korb=[]):
    korb.append(ding)
    return korb

print(sammle("apfel"))
print(sammle("birne"))
```
Zwei Aufrufe, und der zweite Korb enthält den Apfel. **Ohne jede Klasse** — das ist der Beweis, dass es nicht an Objekten liegt, sondern an veränderbaren Standardwerten.

**Experiment 3 — Wann wird der Standardwert ausgewertet?**
```python
def zeit_test(t=print("Das läuft JETZT")):
    pass

print("--- Definition ist durch ---")
zeit_test()
zeit_test()
```
Die Ausgabe kommt **vor** der Trennlinie und nur **einmal**. Damit hast du Konzept 9 selbst nachgewiesen, statt es zu glauben.

**Experiment 4 — Warum fällt es bei einem String nicht auf?** ⭐
```python
def begruesse(name="Mara"):
    print(id(name), name)

begruesse()
begruesse()
```

Zweimal dieselbe Zahl. **Der String wird genauso geteilt wie das Inventar** — es ist buchstäblich derselbe String bei beiden Aufrufen.

Und trotzdem hat es dich noch nie gestört. Warum?

Die Antwort ist die Pointe der ganzen Etappe:

> **Unveränderliche Standardwerte werden genauso geteilt. Es macht nur nichts aus, weil man sie nicht verändern kann.**

Es ist also nicht so, dass Zahlen und Strings „sicher" wären, weil Python sie anders behandelt. Python behandelt alle Standardwerte gleich — nur bei den unveränderlichen kann das Teilen keinen Schaden anrichten.

`id()` zeigt dir übrigens, welches Ding hinter einem Namen steckt. Probier es auch bei dem geteilten Inventar aus Experiment 1: Dort stehen ebenfalls zweimal dieselbe Zahl, und das ist der Beweis.

**Experiment 5 — `== None` gegen `is None`**
```python
class Komisch:
    def __eq__(self, other):
        return True

k = Komisch()
print(k == None)      # True (!)
print(k is None)      # False
```
Ein Objekt, das behauptet, alles zu sein. Absurd — aber es zeigt, warum `is` die verlässlichere Frage ist. In Etappe 11 schreibst du selbst ein `__eq__` und merkst, wie leicht so etwas passiert.

**Experiment 6 — Leer gegen nicht vorhanden**
```python
def __init__(self, name, inventar=None):
    self.inventar = inventar if inventar else Inventory()    # nicht "is not None"!
```
Gib einem Spieler ein **leeres** vorbereitetes Inventar mit. Es wird stillschweigend weggeworfen und durch ein neues ersetzt.

**Fehler vom Typ 3**, und er entsteht daraus, dass ein leeres Inventar in einem `if` als falsch gilt — die Truthy-Regel aus Etappe 2.

**Experiment 7 — Durchgreifen statt fragen**
```python
for i in range(20):
    spieler.inventar.items.append("stein")
print(len(spieler.inventar.items))
```
Zwanzig Steine, obwohl die Obergrenze zehn ist. Die Regel wurde nicht verletzt — sie wurde **umgangen**. Genau davor schützt Delegation.

**Experiment 8 — Das Tuple ändern**
```python
spieler.position[0] = 5
```
`TypeError`. Kennst du aus Etappe 6. Ersetz das Tuple stattdessen ganz — und beobachte, dass das funktioniert.

**Experiment 9 — Der falsche Wächter**
Ersetz `if inventar is None:` durch `if not inventar:` und dann durch `if inventar == None:`. Probier jeweils: kein Inventar mitgeben, ein volles mitgeben, ein leeres mitgeben.

Drei Fassungen, drei verschiedene Verhalten bei drei Fällen. Nur eine ist in allen richtig.

**Experiment 10 — `.copy()` und seine Grenze**
```python
a = Inventory()
a.items.append("brot")
b = Inventory()
b.items = a.items          # ohne copy
b.items.append("seil")
print(a.items)
```
Dann mit `.copy()` wiederholen. Das ist Etappe 4, nur mit Objekten drumherum.

---

## Häufige Stolpersteine

| Fehlermeldung / Symptom | Was dahintersteckt | Wo du suchst |
|---|---|---|
| Zwei Objekte teilen sich einen Bestandteil | Veränderbarer Standardwert in `__init__` | Die Parameterliste — steht dort `=[]` oder `=Klasse()`? |
| Ein mitgegebenes leeres Objekt verschwindet | `if not x:` statt `if x is None:` | Der Wächter |
| `AttributeError: 'Inventory' object has no attribute 'append'` | Du behandelst das Objekt wie die Liste darin | `.items.append()` oder besser eine Methode |
| Die Obergrenze wird nicht eingehalten | Irgendwo wird durchgegriffen | Nach `.items` suchen |
| `TypeError: 'tuple' object does not support item assignment` | Position im Tuple ändern wollen | Ganzes Tuple ersetzen |
| `<Inventory object at 0x...>` in der Ausgabe | `__repr__` fehlt in der neuen Klasse | Die Klasse |
| Ein freier Slot verhält sich wie ein belegter | `0` oder `""` statt `None` als „frei" | Die Slot-Initialisierung |
| Die Regel steht an zwei Stellen | Beim Umbau nicht entfernt | Alte `Player`-Methode durchsehen |
| `TypeError: __init__() missing 1 required positional argument` | Variante B gewählt, aber Aufruf nicht angepasst | Alle `Player(...)`-Aufrufe |

**Der Debugging-Reflex dieser Etappe** ist neu und beantwortet genau die Frage dieser Etappe:

```python
print(a.inventar is b.inventar)
```

Wenn sich zwei Objekte unerklärlich gemeinsam verändern, ist das die erste Prüfung. `is` beantwortet *„ist das dasselbe Ding?"* — und bei geteilten Bestandteilen lautet die Antwort `True`, wo du `False` erwartet hast.

Im Debugger geht es noch schneller: Klapp beide Objekte auf und vergleich die Speicheradressen hinter den Attributen. Stehen dort dieselben Zahlen, teilen sie sich das Ding.

---

## Ein Blick nach vorne

Dein Spieler ist jetzt aus Teilen zusammengesetzt. Aber die Teile enthalten immer noch Strings.

In **Etappe 11** wird aus `"schwert"` ein `Weapon`-Objekt mit Schaden, aus `"hacke"` ein `Tool` mit Haltbarkeit. Dann kann `Equipment` endlich prüfen, ob etwas in die Hand gehört — und `Inventory` bekommt `__len__`, `__contains__` und `__iter__`, sodass sich `len(spieler.inventar)` und `"brot" in spieler.inventar` schreiben lassen wie bei einer eingebauten Datenstruktur.

Dort stellt sich auch die Frage, die du heute vorbereitet hast: *Brauchen wir Vererbung überhaupt?* Du kannst sie jetzt beantworten, weil du die Alternative gebaut hast.

In **Etappe 12** wird Delegation zum Prinzip. `World.tick()` ruft bei jedem NPC `update()` auf — die Welt tickt nicht selbst, sie lässt ticken. Drei Zeilen, und das Dorf lebt. Diese drei Zeilen sind nur deshalb so kurz, weil du heute gelernt hast, Arbeit weiterzureichen.

In **Etappe 16** kommt die Bug-Jagd II, und dort wartet ein versehentlich geteiltes Objekt auf dich. Es wird nicht in einer Parameterliste stehen, sondern besser versteckt. Du wirst es finden, weil du heute `is` als Werkzeug kennengelernt hast.

In **Etappe 19** wird `None` zu `null`, wenn dein Spielstand in eine JSON-Datei wandert — eines der sechs Dinge, die JSON überhaupt kennt. Und deine Objektstruktur von heute bestimmt, wie diese Datei aussieht.

---

## Abschluss

**`GELERNT.md`:**
Zwei bis drei Sätze. Zusätzlich diesmal:

- Deine Zuordnungstabelle: was eigene Klasse, was nur Attribut, und warum
- Deine Antwort auf Frage 2: wer erzeugt die Bestandteile
- Und die Frage dieser Etappe: **Beschreib den Stolperstein in eigenen Worten, so als würdest du ihn jemandem erklären, der ihn noch nie gesehen hat.**

Der letzte Punkt ist mehr als eine Übung. Es ist einer der Fehler, die in fast jedem größeren Python-Projekt einmal vorkommen — und wer ihn erklären kann, findet ihn später bei anderen.

**Commit:**
```bash
git add .
git commit -m "Etappe 10: Spieler aus Bestandteilen"
git push
```

---

## Wenn du mehr willst

Optional, erst bei grünem Selbsttest.

**Ein Gesamtgewicht.** Gib den Gegenständen ein Gewicht — heute noch als Dictionary daneben, `{"brot": 1, "schwert": 5}` — und lass das Inventar es aufsummieren. Dann begrenzt du nicht die Anzahl, sondern das Gewicht.

Das ist eine kleine Änderung mit einer schönen Folge: Dein Spieler kann drei Brote tragen oder ein Schwert, und plötzlich ist Packen eine Entscheidung. In Etappe 11 wandert das Gewicht in den Gegenstand selbst, und in Etappe 23 wird `gesamtgewicht` zu einer `@property`, die sich wie ein Attribut liest.

**Die NPCs bekommen Bestandteile.** Wenn du in Etappe 9 schon eine `Villager`-Klasse gebaut hast: Gib ihr ein eigenes Inventar. Dann kann die Versorgerin wirklich etwas haben, das der Spieler bekommen kann.

Und dann tausch etwas zwischen beiden aus — ein Gegenstand wandert aus einem `Inventory` in ein anderes. Das ist derselbe Vorgang wie in Etappe 4 zwischen zwei Listen, nur dass jetzt beide Seiten ihre eigenen Regeln prüfen. **Der erste Handel deines Spiels**, und er kostet dich fast nichts, weil die Struktur schon steht.

**Ein `ausruestung`-Befehl.** Zeigt an, was in welchem Slot steckt — und was frei ist. Fünf Zeilen, und du siehst zum ersten Mal, wofür `None` gut ist: Ein freier Slot lässt sich sauber als *„— leer —"* anzeigen, ohne dass man raten muss, ob dort vielleicht ein Gegenstand namens leerer String liegt.

---

> **Nächste Etappe:** [Etappe 11 — Vererbung](etappe-11-vererbung.md) · Vererbung, `super()`, Methoden überschreiben, Dunder-Methoden
> Dort werden aus deinen Gegenständen echte Objekte. Und du beantwortest schriftlich die Frage, die heute vorbereitet wurde: Braucht man Vererbung überhaupt?
