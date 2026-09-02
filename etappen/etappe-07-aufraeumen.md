# Etappe 7 — Aufräumen

> **Block 1: Fundament** · Etappe 7 von 30 · [← Etappe 6](etappe-06-datenstrukturen.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 8 →](etappe-08-bug-jagd.md)

**Boot.dev:** Funktionen, Parameter, Rückgabewerte, Scope
**Zeitaufwand:** 7a: 3–4 Sitzungen · 7b: 2–3 Sitzungen, à 20–30 Minuten
**Voraussetzung:** Etappe 6 abgeschlossen, Selbsttest grün

**Diese Etappe ist geteilt, und diesmal aus einem inhaltlichen Grund.** 7a ist eine Programmieretappe: Du lernst Funktionen und baust dein Spiel um. 7b ist eine Denketappe: Du trennst zwei Dinge, die bisher vermischt waren. Beides an einem Abend zu *tun* geht — beides an einem Abend *ankommen* nicht.

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **7a** | Funktionen, Parameter, `return`, Standardargument, Docstring | Scope · warum sieben Parameter ein Signal sind | `global` — und warum du es nicht nimmst |
| **7b** | Zeichenfunktionen, die nur ausgeben | `return` statt `print` in der Logik | `assert` als Behauptung über einen Zustand |

⚠️ **Ein Wort zu `assert`, weil es sonst falsch ankommt:** Es steht auf Stufe *erkennen*. Du sollst **nicht** anfangen zu testen — Tests sind Etappe 26. Du sollst drei Zeilen geschrieben und einmal knallen gesehen haben. Mehr wird daraus heute nicht.

---

## Worum es geht

**Heute schreibst du kein einziges neues Spielfeature. Und das ist der Punkt.**

Öffne `spiel.py` und scroll einmal von oben nach unten. Wie lang ist die Datei inzwischen? Wie viele Zweige hat deine Befehlskette? Wie oft musst du scrollen, um von der Klassenwahl bis zum Bestiarium zu kommen?

In Etappe 5 stand die Bitte, dir zu notieren, **wann dir zum ersten Mal aufgefallen ist, dass die Datei zu lang wird.** Hol den Zettel heraus. Wenn du ihn nicht geschrieben hast, ist das auch eine Antwort — dann merkst du es heute.

**Dein Programm funktioniert. Es ist nur nicht mehr überschaubar.** Das sind zwei völlig verschiedene Eigenschaften, und bis heute war nur die erste wichtig. Ab jetzt beide.

> **Was du heute lernst, heißt Refactoring: funktionierenden Code umbauen, ohne sein Verhalten zu ändern.**

Das ist ungefähr die Hälfte dessen, was Entwickler den ganzen Tag tun. Und beim ersten Mal fühlt es sich falsch an — *es lief doch*. Genau deshalb bekommt der Umbau heute einen **Beweis** statt einer Hoffnung.

**Und es gibt einen zweiten Grund, warum diese Etappe genau hier steht.** Deine Funktionen werden gleich ständig dieselben sechs Werte brauchen und sie durch drei Ebenen durchreichen. Das ist unangenehm — und Absicht. In Etappe 9 verschwindet dieser Schmerz, und dann verstehst du, wozu `self` da ist. Wer ihn nicht hatte, hält Klassen für Zeremonie.

---

## Vor dem Umbau: drei Fragen ⭐

Das Ritual seit Etappe 4 — und heute ist es wichtiger als je zuvor, weil du **nur** umbaust:

| Frage | Antwort |
|---|---|
| **Was bleibt gleich?** | Alles. Jede Ausgabe, jede Meldung, jede Zahl, jedes Verhalten |
| **Was ändert sich nur in der Darstellung?** | Nichts. Der Spieler darf von dieser Etappe nicht das Geringste merken |
| **Was ändert sich wirklich am Datenmodell?** | Nichts. Es wandert nur anderswohin |

**Das ist der Sonderfall unter allen Umbauten dieses Plans: Alle drei Antworten heißen „nichts".** Und genau deshalb ist er so gut prüfbar — jede Abweichung ist ein Fehler, es gibt keine Grauzone.

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

### Wie kommt Zustand in deine Funktionen? ⭐

Deine Funktionen brauchen Werte, die außerhalb von ihnen liegen — Munition, Schrott, Kernintegrität, die Gegnerliste. Es gibt drei Wege, und du musst dich heute entscheiden.

| | Alles als Parameter | `global` | Ein Dictionary „Spielzustand" |
|---|---|---|---|
| Wie | Jede Funktion bekommt, was sie braucht | Funktionen greifen direkt auf äußere Namen zu | Alle Werte in **einem** Dictionary, das herumgereicht wird |
| Aufwand heute | hoch — lange Parameterlisten | fast null | mittel |
| Man sieht der Funktion an, was sie anfasst | **ja** | nein | teilweise |
| Wird in Etappe 9 abgelöst durch | `self` | — die Krücke bleibt eine Krücke | `self` |

**Nimm den ersten Weg.** Alles als Parameter, auch wenn die Listen lang werden. Und zwar aus einem Grund, der nichts mit Eleganz zu tun hat:

> **Eine lange Parameterliste ist unbequem und *sichtbar*. `global` ist bequem und *unsichtbar*.**

Bei einer Funktion mit sechs Parametern siehst du in der ersten Zeile, was sie anfasst. Bei `global` musst du den ganzen Körper lesen — und in vier Wochen weißt du nicht mehr, welche Funktion welchen Wert heimlich verändert.

👀 **Zu `global` selbst, ein Satz zum Wiedererkennen:** Es erlaubt einer Funktion, eine äußere Variable nicht nur zu lesen, sondern zu **verändern**. Es funktioniert, es ist kürzer, und es deckt genau das Problem zu, das Etappe 9 löst. Du wirst es in fremdem Code sehen. **Bau es heute nicht ein.**

*(Der dritte Weg — ein Zustands-Dictionary — ist übrigens keine schlechte Idee, und manche Projekte machen das dauerhaft so. Für dich lohnt er sich nicht, weil Etappe 9 in zwei Wochen kommt und `self` dasselbe Problem sauberer löst. Wenn du ihn trotzdem reizvoll findest: notieren, nicht bauen.)*

**Schreib deine Entscheidung und die Begründung in `GELERNT.md`.** In Etappe 9 liest du sie wieder.

---

## Die Konzepte — Teil 7a

Alle Beispiele laufen **außerhalb** deines Spiels. Was in `spiel.py` entsteht, schreibst du selbst.

### 1. Was eine Funktion ist — und was sie nicht ist

```python
def begruesse(name):
    print(f"Hallo, {name}.")

begruesse("Anna")
begruesse("Bo")
```

**Drei Teile:** `def` und ein Name, die Klammern mit den **Parametern**, und der eingerückte Block darunter.

**Und der Teil, den fast alle beim ersten Mal übersehen:** Die Zeilen unter `def` laufen nicht, wenn Python die Datei liest. Sie laufen **erst beim Aufruf**. `def` legt etwas an, es tut nichts.

```python
def sag_hallo():
    print("Hallo!")

print("Zeile 1")
sag_hallo()
print("Zeile 3")
```

**Sag die Ausgabe vorher, bevor du es ausführst.** Vier Zeilen Code, drei Zeilen Ausgabe — in welcher Reihenfolge?

### 2. Parameter und Argument — zwei Wörter, ein Missverständnis

```python
def begruesse(name):       # name ist der PARAMETER
    print(f"Hallo, {name}.")

begruesse("Anna")          # "Anna" ist das ARGUMENT
```

Der **Parameter** steht in der Definition und ist ein Platzhalter. Das **Argument** ist der echte Wert beim Aufruf.

Das klingt nach Wortklauberei und wird gleich wichtig: Wenn eine Fehlermeldung von *„missing 1 required positional argument"* spricht, meint sie den Aufruf, nicht die Definition.

### 3. `return` — der Unterschied, an dem alles hängt ⭐

```python
def verdopple_und_zeige(zahl):
    print(zahl * 2)              # gibt aus

def verdopple(zahl):
    return zahl * 2              # gibt zurück
```

Beide „machen dasselbe" — bis du damit weiterarbeiten willst:

```python
a = verdopple_und_zeige(5)       # was steht jetzt in a?
b = verdopple(5)                 # und hier?

print(verdopple(5) + verdopple(3))   # geht
print(verdopple_und_zeige(5) + 1)    # geht nicht
```

**Sag alle vier Zeilen vorher, dann führ sie aus.**

> **Eine Funktion mit `print` erzählt dir etwas. Eine Funktion mit `return` gibt dir etwas.**

Nur mit dem zweiten kannst du rechnen, vergleichen, speichern, weiterreichen.

**Und wenn kein `return` dasteht?** Dann gibt die Funktion `None` zurück — genau wie `append()` in Etappe 4. Das ist dieselbe Falle, nur diesmal in deinem eigenen Code:

```python
werte = verdopple_und_zeige(5)
print(werte + 1)      # TypeError — None kann man nicht addieren
```

**Diese Unterscheidung ist die wichtigste dieser Etappe.** Sie kommt in 7b als Design-Entscheidung wieder und entscheidet in Etappe 28, ob Pygame draufpasst oder nicht.

### 4. `return` beendet die Funktion sofort

```python
def erster_langer_name(namen):
    for name in namen:
        if len(name) > 5:
            return name          # hier ist Schluss — der Rest läuft nicht
    return "keiner gefunden"
```

`return` gibt nicht nur zurück, es **verlässt die Funktion**. Auch mitten aus einer Schleife heraus. Das ist derselbe Sprung wie `break` aus Etappe 3a, nur eine Ebene höher: `break` verlässt die Schleife, `return` die ganze Funktion.

**Nützlich für die frühe Abfahrt:** Wenn eine Prüfung scheitert, kannst du sofort zurück, statt den Rest in ein `else` zu schachteln.

```python
def hole_preis(name, katalog):
    if name not in katalog:
        return None              # raus, bevor es kompliziert wird
    return katalog[name]
```

Merk dir die Form — deine Prüfketten aus Etappe 5 und 6 lassen sich damit deutlich flacher schreiben.

### 5. Scope — die Beobachtung aus Etappe 3 bekommt einen Namen ⭐

In Etappe 3a stand: *Wo du eine Variable erzeugst, entscheidet darüber, wann sie neu gesetzt wird.* Damals ging es um Schleifenebenen. Heute bekommt dieselbe Sache ihren Fachbegriff — und eine zweite, härtere Regel.

```python
vorrat = 100

def verbrauche():
    vorrat = 50               # das ist eine NEUE Variable, nur in der Funktion
    print("drinnen:", vorrat)

verbrauche()
print("draußen:", vorrat)     # Was steht hier? Vorher sagen!
```

**Der Bereich, in dem ein Name gilt, heißt Scope.** Und die Regel dazu:

> **Eine Funktion darf äußere Werte *lesen*. Zuweisen erzeugt eine neue, eigene Variable — die äußere bleibt unberührt.**

```python
def zeige():
    print(vorrat)             # geht: nur lesen

def aendere():
    vorrat = 50               # erzeugt eine lokale Variable
```

**Warum das gut ist**, auch wenn es sich gerade nach Schikane anfühlt: Eine Funktion kann deine Werte nicht versehentlich zerstören. Was drinnen passiert, bleibt drinnen — es sei denn, du gibst es mit `return` heraus.

**Und daraus folgt die Arbeitsweise dieser Etappe:** Werte kommen als Parameter **hinein** und mit `return` wieder **hinaus**. Beides sichtbar, beides in der ersten Zeile ablesbar.

⚠️ **Die Ausnahme, die keine ist:** Bei einer **Liste** oder einem **Dictionary** kannst du den Inhalt sehr wohl von innen verändern — `liste.append(...)` funktioniert, ohne dass du zuweist. Das ist kein Widerspruch, sondern *mutable* aus Etappe 4: Der Name bleibt derselbe, das Objekt ändert sich. Merk dir das, es wird dich einmal überraschen.

### 6. Standardargumente — erweitern, ohne alte Aufrufe zu brechen

```python
def zeige_bestand(menge, einheit="Stück"):
    print(f"{menge} {einheit}")

zeige_bestand(5)                 # 5 Stück
zeige_bestand(3, "Liter")        # 3 Liter
```

Ein Parameter mit einem Standardwert darf beim Aufruf weggelassen werden.

**Warum das mehr ist als Bequemlichkeit:** Du kannst eine Funktion **erweitern, ohne einen einzigen bestehenden Aufruf anzufassen**. Das ist das häufigste Muster für rückwärtskompatible Änderungen, das es gibt.

Genau dafür brauchst du es heute: `zeige_status(marine, ausfuehrlich=False)`. Alle alten Aufrufe funktionieren weiter, der neue kann mehr.

⚠️ **Standardwerte stehen immer hinten.** `def f(a=1, b)` ist ein `SyntaxError` — Python muss wissen, welches Argument wohin gehört.

*(Und es gibt eine berühmte Falle mit Standardwerten, die Listen sind. Die hebe ich für Etappe 10 auf, weil sie erst mit Objekten richtig weh tut.)*

### 7. Sieben Parameter sind ein Signal ⭐

```python
def berechne_schaden(waffe, ziel, panzerung, klasse, boni, munition, entfernung):
```

Das funktioniert. Und es ist ein **Signal**, kein Erfolg.

Zwei Fragen, wenn eine Parameterliste so lang wird:

1. **Gehören diese Werte eigentlich zusammen?** `panzerung`, `klasse` und `boni` beschreiben alle dasselbe Ding — den Marine. Vielleicht ist das *ein* Ding, das man übergibt, und nicht drei Werte.
2. **Macht die Funktion mehr als eine Sache?** Sieben Eingaben deuten oft auf drei Aufgaben in einem Körper hin.

**Und jetzt der Teil, den du heute aushalten sollst:** Die erste Frage hat eine Antwort, und sie heißt Etappe 9. Ein `Marine`-Objekt trägt seine Panzerung, seine Klasse und seine Boni mit sich, und aus sieben Parametern werden zwei.

> **Heute baust du die lange Liste absichtlich. Damit du in Etappe 9 nicht lernst, was `self` ist, sondern warum es das gibt.**

Notier in `GELERNT.md`, welche deiner Funktionen die längste Parameterliste hat und welche Werte darin immer gemeinsam auftreten. Das ist deine Vorarbeit für Etappe 9.

### 8. „Eine Funktion, ein Zweck" — und die Gegenwarnung ⚠️

Die übliche Regel lautet: Eine Funktion tut **eine** Sache und hat einen Namen, der sagt welche.

**Die Prüffrage dazu ist nicht „kann man das auslagern?", sondern:**

> **Hat dieses Stück einen Namen, den ich aussprechen kann?**

`berechne_schaden` — ja. `mach_den_kram_nach_dem_feuern` — nein, das sind zwei Sachen.

⚠️ **Und jetzt die Gegenwarnung, damit die Etappe nicht ins Gegenteil kippt: Mehr Funktionen sind nicht besser.**

Eine Funktion, die einmal aufgerufen wird und drei Zeilen hat, macht deinen Code nicht klarer — sie verteilt ihn. Statt einer Stelle liest du jetzt zwei und springst dazwischen.

**Zerlegen hat einen Preis, und der heißt Sprünge.** Der Gewinn muss größer sein als dieser Preis. Bei deiner 200-Zeilen-Befehlskette ist er das mit Sicherheit. Bei drei Zeilen fast nie.

*(In Etappe 24 stellt sich dieselbe Frage noch einmal, dann für Dateien statt Funktionen. Der Preis ist derselbe, nur größer.)*

### 9. Docstrings — was die Funktion verspricht

```python
def berechne_trinkgeld(betrag, prozent=10):
    """Berechnet das Trinkgeld. Gibt eine Zahl zurück, nie negativ."""
    return betrag * prozent / 100
```

Ein String direkt unter der `def`-Zeile, in dreifachen Anführungszeichen. Python speichert ihn — `help(berechne_trinkgeld)` zeigt ihn an. Das ist dasselbe `help()`, mit dem du in Etappe 4 `.join()` gefunden hast; die Texte, die es zeigt, sind Docstrings von jemand anderem.

**Schreib in einen Docstring, was der Name nicht schon sagt:** was zurückkommt, was vorausgesetzt wird, was auf keinen Fall passiert. Nicht: *„Diese Funktion berechnet das Trinkgeld."* Das steht schon im Namen.

*(In Etappe 23b kommen Typannotationen dazu — dann sagt die Signatur selbst, was rein- und rausgeht.)*

### 10. Refactoring: die Methode ⭐

**Die eine Regel, die Umbauen erträglich macht:**

> **Eine Funktion herauslösen. Ausführen. Prüfen. Dann die nächste.**

Nicht fünf auf einmal. Wenn danach etwas nicht stimmt, hast du bei fünf Änderungen fünf Verdächtige und bei einer genau einen.

Das ist dasselbe Verfahren wie das dreischrittige Bauen der Anmarschbahn in Etappe 4 — und es taucht in Etappe 8 als **Halbieren statt Durchsuchen** wieder auf.

⚠️ **Und die zweite Regel, die noch wichtiger ist:**

> **Niemals Refactoring und neue Funktionen im selben Schritt.**

Wenn du beim Auslagern merkst, dass `kaufe()` eigentlich auch eine Mengenprüfung bräuchte — **notier es, bau es nicht.** Sonst weißt du hinterher nicht, ob der neue Fehler vom Umbau kommt oder vom neuen Feature. Das ist die häufigste Art, sich einen Abend zu ruinieren.

### 11. Der Verhaltens-Beweis ⭐

**Der Umbau bekommt einen Beweis, keine Hoffnung.**

Bevor du irgendetwas anfasst, schreib eine Befehlsfolge von fünfzehn bis zwanzig Zeilen auf, die dein Spiel gründlich durchgeht. **Gerade die Fälle, die schiefgehen, gehören dazu** — leere Eingabe, unbekannter Befehl, Kauf ohne Schrott, `nimm` ohne zweites Wort.

Dann:

```bash
python spiel.py < befehle.txt > vorher.txt
# ... umbauen ...
python spiel.py < befehle.txt > nachher.txt
diff vorher.txt nachher.txt
```

Die erste Zeile füttert dein Programm mit der Datei statt mit der Tastatur und schreibt die Ausgabe in eine zweite Datei. `diff` zeigt die Unterschiede zwischen beiden Läufen. **Bei einem gelungenen Refactoring gibt `diff` gar nichts aus.**

**Das heißt Charakterisierungstest:** Man friert das aktuelle Verhalten ein, um es beim Umbau nicht zu verlieren — auch das Verhalten, das man selbst nicht ganz versteht. Es ist gängige Praxis, und es ist der direkte Vorläufer von Etappe 26, wo `pytest` genau das automatisch tut.

*(Falls `diff` bei dir nicht verfügbar ist: Die beiden Dateien im Editor nebeneinander öffnen tut es auch. Der Punkt ist der Vergleich, nicht das Werkzeug.)*

---

## Die Konzepte — Teil 7b

### 12. Die Linie: rechnen oder ausgeben ⭐

**Heute schreibst du fast keinen neuen Code. Du ziehst eine Linie.**

Auf der einen Seite steht alles, was **rechnet und entscheidet**. Auf der anderen alles, was **ausgibt**. Bisher lagen beide Sorten durcheinander in denselben Funktionen — das war völlig in Ordnung, bis heute.

```python
# vermischt: rechnet UND gibt aus
def berechne_und_zeige(betrag, prozent):
    trinkgeld = betrag * prozent / 100
    print(f"Trinkgeld: {trinkgeld:.2f} Euro")

# getrennt
def berechne_trinkgeld(betrag, prozent):
    return betrag * prozent / 100

def zeige_trinkgeld(trinkgeld):
    print(f"Trinkgeld: {trinkgeld:.2f} Euro")
```

**Die untere Fassung ist länger. Sie ist trotzdem besser, und zwar aus vier Gründen**, von denen dich heute nur der erste betrifft:

| Was du gewinnst | Wo es zahlt |
|---|---|
| Du kannst mit dem Ergebnis weiterrechnen | sofort |
| Du kannst dieselbe Rechnung anders anzeigen | Etappe 14a — Bahn *und* Raster |
| Du kannst die Rechnung prüfen, ohne den Bildschirm zu lesen | Etappe 26 — Tests |
| Du kannst die Anzeige austauschen, ohne die Rechnung anzufassen | Etappe 28 — Pygame |

> **Deine Logikfunktionen geben Werte zurück. Sie geben nichts aus.**

Das ist die Design-Entscheidung mit der längsten Wirkung in diesem ganzen Tutorial. Sie fühlt sich heute umständlich an. In Etappe 28 ist sie der Unterschied zwischen *„Pygame draufsetzen"* und *„alles neu schreiben"*.

### 13. Die Darstellung wird eine eigene Schicht

Was seit Etappe 1 gewachsen ist — der ASCII-Kopf, die Balken aus 3c, die Anmarschbahn aus 4, der Grundriss aus 5 — wandert heute in Funktionen, die **nur zeichnen**.

**Die Regel dafür ist streng, und sie ist der ganze Punkt:**

> **Eine Zeichenfunktion bekommt fertige Werte und gibt Zeichen aus. Sie rechnet nichts und entscheidet nichts.**

Das heißt konkret: `zeichne_balken(wert, maximum)` bekommt zwei Zahlen. Sie fragt nicht nach der Kernintegrität, sie kennt kein `vorrat`, sie weiß nicht, was sie zeichnet. Sie kann Balken.

**Und genau deshalb kannst du sie zweimal benutzen** — für Kern und für Munition — statt zwei fast gleiche Blöcke zu haben.

**Hier zahlt eine Erkenntnis aus Etappe 3c aus:** Dort stand, dass die Balkenlänge beim *Anzeigen* berechnet wird und nicht beim Programmstart. Heute bekommt dieser Gedanke seinen Platz im Code — die Rechnung wohnt in der Zeichenfunktion, weil sie dorthin gehört.

*(In Etappe 14a kommt `zeichne_vorfeld()` dazu, in Etappe 28 werden dieselben Funktionen ausgetauscht statt umgeschrieben, in Etappe 29 zeichnen sie Kacheln statt Zeichen. Dass das geht, entscheidest du heute.)*

### 14. Zwei Werte auf einmal zurückgeben

```python
def teile_mit_rest(a, b):
    return a // b, a % b         # zwei Werte, durch Komma getrennt

ganz, rest = teile_mit_rest(17, 5)
```

Das Komma macht daraus ein **Tuple** — die Komma-Falle aus Etappe 6, jetzt von der nützlichen Seite. Und das Auspacken links vom `=` ist das Tuple-Unpacking aus derselben Etappe.

**Wofür du das brauchst:** Eine Funktion, die nur den Schaden zurückgibt, zwingt den Aufrufer zum Raten — *war die 0 ein Fehlschlag oder ein Treffer auf schwere Panzerung?* Zwei Rückgabewerte beantworten das, ohne dass irgendwo ein `print` stehen muss.

*(In Etappe 21a wird genau das gebraucht: `schaden, ergebnis = berechne_treffer(...)`.)*

### 15. 👀 `assert` — eine Behauptung, die knallt

```python
assert trinkgeld >= 0
```

**Eine Assertion ist eine Behauptung über einen Zustand, von der dein Programm sagt: das muss wahr sein, sonst stimmt etwas nicht.** Stimmt sie, passiert nichts. Stimmt sie nicht, knallt es **sofort** — an der Stelle, wo die Annahme gebrochen wurde, und nicht drei Funktionen später, wo das falsche Ergebnis auffällt.

> **Damit verwandelst du einen Fehler vom Typ 3 in einen vom Typ 1.** Das ist fast immer ein guter Tausch.

**Drei Zeilen, dann ist das Thema für heute erledigt.** Du fängst jetzt nicht an zu testen. Du hast einmal gesehen, dass man eine Annahme hinschreiben kann und dass sie bricht.

**Was bleibt, ist eine Lesefrage** — und die ist ab heute eines deiner besten Werkzeuge bei fremdem Code:

> **Welche Annahmen macht diese Funktion — und prüft sie eine davon?**

*(In Etappe 13 schreibst du Zähler-Invarianten so auf, in Etappe 20 lernst du den Unterschied zwischen prüfen und fangen, und in Etappe 26 ist `pytest` nichts anderes als dieselben `assert`-Zeilen in einer eigenen Datei. Kein neues Konzept — nur ein Rahmen drumherum.)*

---

## Dein Auftrag

**Der schwerste Teil dieser Etappe ist nicht das Tippen, sondern das Aushalten.** Du baust stundenlang um und hast am Ende ein Spiel, das sich exakt wie vorher verhält. Das fühlt sich nach nichts an — und ist die Arbeit, die Etappe 9 bis 28 überhaupt erst möglich macht.

Nach **jeder einzelnen** herausgelösten Funktion ausführen. Nicht nach fünf.

---

### 1. Schreib die Befehlsfolge für den Beweis

- Eine Textdatei `befehle.txt` mit fünfzehn bis zwanzig Zeilen, eine Eingabe pro Zeile.
- Deck alles ab: gültige Befehle, Kauf, Freischaltung, Bewegung, Bestiarium — **und die Fehlerfälle**: leere Zeile, unbekannter Befehl, `nimm` ohne Ziel, Kauf ohne Schrott.
- Am Ende `beenden`.

```bash
python spiel.py < befehle.txt > vorher.txt
```

**So prüfst du es:** Öffne `vorher.txt`. Steht dort ein vollständiger Spieldurchlauf? Wenn das Programm vorher abbricht, fehlt eine Eingabe — ergänz sie.

⚠️ **Ohne diese Datei fängst du nicht an.** Sie ist der einzige Beweis, den du heute bekommst.

---

### 2. Lös die erste Funktion heraus: `zeige_status()`

- Nimm den Block aus deinem `status`-Zweig und pack ihn in eine Funktion.
- Sie bekommt alles, was sie braucht, **als Parameter** — nach deiner Design-Entscheidung.
- Der `status`-Zweig in der Befehlskette besteht danach aus einem einzigen Aufruf.

**So prüfst du es:** Programm ausführen, `status` tippen. Die Ausgabe muss **zeichengenau** dieselbe sein wie vorher.

*(Fang mit dieser an, weil sie nichts verändert — sie gibt nur aus. Wenn hier etwas schiefgeht, liegt es am Umbau und nicht an der Logik.)*

---

### 3. Lös `berechne_schaden()` heraus

- Die Platzhalterformel aus Etappe 3c, plus der Panzerbrecher-Bonus aus Etappe 6.
- **Sie gibt eine Zahl zurück. Sie gibt nichts aus.**

**So prüfst du es:** Feuern. Die Schadenszahl muss dieselbe sein wie vorher — mit und ohne freigeschalteten Panzerbrecher.

*(Diese Funktion wird in Etappe 21a zur echten Trefferrechnung und in Etappe 26 dein erster Test. Sie ist ab heute Produktivcode.)*

---

### 4. Lös die Prüfketten heraus: `kaufe()` und `schalte_frei()`

- Die vier Prüfungen aus Etappe 5 und die fünf aus Etappe 6, jeweils in eine eigene Funktion.
- Die Reihenfolge bleibt exakt wie sie war: **erst alle Prüfungen, dann verändern.**
- Nutz die frühe Abfahrt aus Konzept 4, wenn es die Verschachtelung flacher macht.

**So prüfst du es:** Kauf mit zu wenig Schrott, Kauf bei vollem Inventar, `kaufe hubschrauber`, doppeltes Freischalten. Alle vier Meldungen müssen wortgleich sein.

---

### 5. Lös `wechsle_sektor()` heraus

- Die drei Fälle aus Etappe 5: Richtung existiert, existiert nicht, kein zweites Wort.
- Gibt den neuen Sektornamen **zurück** — sie setzt `aktueller_sektor` nicht selbst.

⚠️ *Hier merkst du zum ersten Mal, warum das lästig ist. Merk dir das Gefühl; es ist der Grund für Etappe 9.*

---

### 6. Lös `verarbeite_befehl()` heraus

- Die gesamte `if`/`elif`-Kette wandert in **eine** Funktion.
- Auch die Eingabeaufbereitung aus Etappe 4 — `.strip()`, `.lower()`, `.split()`, die Längenprüfung.
- Deine Hauptschleife besteht danach fast nur noch aus: Eingabe holen, Funktion aufrufen.

**So prüfst du es:** Alle Befehle durchprobieren, auch die Fehlerfälle. Deine `while`-Schleife sollte jetzt in einen Bildschirm passen.

*(Damit ist die Schuld aus Etappe 3b eingelöst — die Kette, die seit vier Etappen wächst, hat endlich einen eigenen Ort. Sie stirbt in Etappe 23a ganz.)*

---

### 7. Zieh den Beweis

```bash
python spiel.py < befehle.txt > nachher.txt
diff vorher.txt nachher.txt
```

**`diff` muss schweigen.** Gibt es Unterschiede, hast du beim Umbauen etwas verändert — such es, bevor du weitermachst.

⚠️ **Nicht „das ist bestimmt egal".** Ein Unterschied ist ein Verhaltensunterschied, und heute darf es keinen geben.

---

### 8. Bau ein Standardargument ein

- Gib `zeige_status()` einen Parameter `ausfuehrlich=False`.
- Bei `True` zeigt sie zusätzlich etwas an — was, ist dir überlassen: Gegnerpositionen, freigeschaltete Ausbauten, den Rundenzähler.
- **Alle bestehenden Aufrufe bleiben unverändert.**

**So prüfst du es:** Der normale `status`-Befehl verhält sich exakt wie vorher. Ein zweiter Befehl oder ein zweites Wort löst die ausführliche Fassung aus.

---

### 9. Schreib drei Docstrings

- Für `berechne_schaden()`, `kaufe()` und eine dritte deiner Wahl.
- Jeweils **ein Satz**: was kommt zurück, was wird vorausgesetzt.
- Nicht wiederholen, was der Name schon sagt.

**So prüfst du es:** `help(berechne_schaden)` im Terminal aufrufen.

---

### 10. Committen

```
git add .
git commit -m "Etappe 7a: Refactoring in Funktionen"
```

> **⏸ Hier ist der Schnitt.** 7a ist getan. Die Trennung von Logik und Darstellung ist ein eigener Abend.

---

### 11. Lös die Zeichenfunktionen heraus

Vier Funktionen, die **nur ausgeben**:

| Funktion | Bekommt | Herkunft |
|---|---|---|
| `zeichne_kopf()` | nichts | Etappe 1 |
| `zeichne_balken(wert, maximum)` | zwei Zahlen | Etappe 3c |
| `zeichne_bahn(gegner, gegner_typen)` | zwei Listen | Etappe 4 und 6 |
| `zeichne_grundriss(aktueller_sektor)` | einen Namen | Etappe 5 |

**Die Balkenfunktion ersetzt beide Balken** — Kern und Munition. Wenn du zwei fast gleiche Blöcke hattest, verschwindet einer davon.

**So prüfst du es:** `diff` erneut ziehen. Wieder muss er schweigen.

---

### 12. Prüf die Zeichenfunktionen auf Reinheit

Geh jede der vier durch und beantworte:

- Rechnet sie etwas aus, das nicht mit dem Zeichnen zu tun hat?
- Entscheidet sie etwas — greift sie auf `welle`, `kern_integritaet` oder `freigeschaltet` zu?
- Braucht sie mehr, als man ihr übergibt?

**Dreimal nein, oder du hast noch Arbeit.** Eine Zeichenfunktion, die die Welt kennt, lässt sich in Etappe 28 nicht austauschen.

---

### 13. Zieh die Linie durch die Logik

Geh deine Funktionen aus 7a durch und such nach `print`.

- `berechne_schaden()` darf keines haben.
- `kaufe()` und `schalte_frei()` dürfen melden — sie sprechen mit dem Spieler. **Aber die Rechnung darin nicht.**
- Wo eine Logikfunktion etwas mitteilen will: **Rückgabewert statt Ausgabe.** Der Aufrufer entscheidet, ob und wie es angezeigt wird.

**So prüfst du es:** Kannst du `berechne_schaden()` im Terminal aufrufen und mit dem Ergebnis rechnen, ohne dass etwas auf dem Bildschirm erscheint?

---

### 14. Die Transferaufgabe zuerst — dann drei `assert`-Zeilen

- Mach die Transferaufgabe weiter unten (`berechne_trinkgeld`) **in einer Wegwerf-Datei**.
- Schreib dort drei `assert`-Zeilen für das, was immer gelten muss.
- Brich eine davon absichtlich und sieh dir die Fehlermeldung an.

**Danach genau eine Zeile in dein Spiel:** ein `assert` in `berechne_schaden()`, das sicherstellt, dass der Schaden nie negativ wird.

⚠️ **Mehr nicht.** Du fängst nicht an zu testen. Eine Zeile, dann ist Schluss bis Etappe 26.

---

### 15. Der Rückwärtsgang

Spiel drei volle Wellen — mit Kauf, Freischaltung, Bewegung, Bestiarium und mindestens einem Fehlerfall.

**Alles muss sich verhalten wie nach Etappe 6.** Kein neues Feature, keine neue Meldung, keine andere Zahl.

---

### 16. Committen

```
git add .
git commit -m "Etappe 7b: Logik und Darstellung getrennt"
git push
```

---

## Was NICHT in diese Etappe gehört

- ❌ **Klassen und Objekte** → Etappe 9
- ❌ **`global`, um die Parameterlisten loszuwerden** → gar nicht; Etappe 9 löst das Problem richtig
- ❌ **Ein Befehls-Dictionary statt der `elif`-Kette** → Etappe 23a
- ❌ **Mehrere Dateien** → Etappe 24
- ❌ **`pytest` oder eine Testdatei** → Etappe 26
- ❌ **Typannotationen** → Etappe 23b
- ❌ **Neue Spielfunktionen jeder Art** → nächste Etappe, in der sie hingehören
- ❌ **Die Kampfformel „bei der Gelegenheit" verbessern** → Etappe 21a

**Der verlockendste Punkt ist der vorletzte, und er wird dich heute mehrfach anspringen.**

Beim Auslagern von `kaufe()` siehst du, dass eine Mengenprüfung fehlt. Beim Auslagern von `zeige_status()` fällt dir auf, dass die Anzeige hübscher sein könnte. Beim Auslagern der Befehlskette denkst du: *ein Dictionary wäre hier viel eleganter.*

**Alles richtig. Bau trotzdem nichts davon.**

Der Grund ist nicht Disziplin, sondern Diagnostik: Wenn dein `diff` in Schritt 7 Unterschiede zeigt, willst du wissen, dass sie vom Umbau kommen. Hast du gleichzeitig ein Feature eingebaut, hast du zwei Verdächtige und keinen Anhaltspunkt.

> **Notier jeden dieser Einfälle in `GELERNT.md`. Bau keinen einzigen davon heute.**

Die Liste ist mehr wert, als du gerade denkst — sie ist deine Vorlage für Etappe 21a und 23a, und sie beweist dir in vier Wochen, dass du beim Umbauen mitgedacht hast.

---

## Selbsttest

Prüft den Zustand deines Programms, nicht dein Gefühl. Führ jeden Punkt tatsächlich aus.

- [ ] ⭐ **`diff vorher.txt nachher.txt` gibt nichts aus**
- [ ] `befehle.txt` enthält mindestens vier Fehlerfälle
- [ ] Deine `while`-Hauptschleife passt auf einen Bildschirm
- [ ] Der `status`-Zweig in der Befehlskette ist ein einziger Aufruf
- [ ] `berechne_schaden()` enthält kein `print` — du kannst mit dem Rückgabewert rechnen
- [ ] `zeige_status()` funktioniert mit **und** ohne das Standardargument
- [ ] `help(berechne_schaden)` zeigt deinen Docstring
- [ ] ⭐ **Keine deiner Zeichenfunktionen greift auf eine äußere Variable zu** — sie bekommen alles übergeben
- [ ] Ein Balken wird von **einer** Funktion gezeichnet, nicht von zwei fast gleichen Blöcken
- [ ] Es gibt kein `global` in deiner Datei
- [ ] Drei volle Wellen verhalten sich wie nach Etappe 6 — inklusive aller Meldungen
- [ ] In `GELERNT.md` steht, welche Funktion die längste Parameterliste hat
- [ ] In `GELERNT.md` steht die Liste der Einfälle, die du **nicht** gebaut hast

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten.

1. Was ist der Unterschied zwischen `return` und `print`? Nenn eine Sache, die nur mit `return` geht.
2. Was gibt eine Funktion ohne `return` zurück — und woher kennst du diese Falle schon?
3. Was ist Scope? Warum kann eine Funktion eine äußere Zahl lesen, aber nicht überschreiben?
4. **Warum kann eine Funktion eine äußere Liste trotzdem verändern?** *(Das ist kein Widerspruch — welches Konzept aus Etappe 4 erklärt es?)*
5. Unterschied Parameter ↔ Argument?
6. Was ist ein Standardargument, und warum ist es rückwärtskompatibel?
7. **Warum ist eine Funktion mit sieben Parametern ein Signal und kein Erfolg?** Welche zwei Fragen stellst du dann?
8. Was macht `return` mit dem Rest der Funktion?
9. Was ist ein Charakterisierungstest, und was beweist er — was beweist er **nicht**?
10. Warum sind mehr Funktionen nicht automatisch besser? Nenn den Preis.
11. Was darf eine Zeichenfunktion nicht tun?

**Frage 7 ist die wichtigste.** Alles andere ist Werkzeugwissen, und Werkzeugwissen holt man nach. Frage 7 ist die Brücke zu Etappe 9: Wer versteht, dass eine lange Parameterliste auf zusammengehörige Daten hindeutet, lernt dort nicht *was* `self` ist, sondern *warum* es das gibt.

**Frage 4 ist die kniffligste** und deckt ein Missverständnis auf, das sonst monatelang unbemerkt bleibt.

---

## Transferaufgabe (10 Minuten)

**Außerhalb des Spiels**, in einer Wegwerf-Datei. Ein Restaurant, kein Vorposten.

1. Schreib `berechne_trinkgeld(betrag, prozent)`. Sie gibt eine Zahl **zurück**.
2. Gib dem zweiten Parameter einen Standardwert von 10.
3. Ruf sie dreimal auf — mit zwei Argumenten, mit einem, und mit `prozent=0`.
4. Schreib einen Docstring, der sagt, was zurückkommt.

**Und jetzt der eigentliche Punkt — noch ohne Testframework:**

5. **Was muss immer gelten?** Schreib drei Sätze auf. Kandidaten: Nie negativ. Bei 0 Prozent genau null. Bei doppeltem Betrag doppeltes Trinkgeld.
6. Schreib jeden dieser drei Sätze als `assert`-Zeile.
7. **Brich einen absichtlich** — ändere die Formel so, dass er nicht mehr stimmt. Lies die Fehlermeldung.

Das ist Testdenken, lange bevor du `pytest` anfasst. Und es ist der Grund, warum die Aufgabe außerhalb des Spiels läuft: `berechne_schaden()` ist ab heute Produktivcode, keine Übung mehr.

---

## Kaputtmachen

**Vor jedem Experiment aufschreiben, was passieren wird.** Die ersten vier gehören dazu, die letzten drei sind Kür.

**1. Vergiss das `return`.** Nimm es aus `berechne_schaden()` heraus und feuer einmal. Was steht in der Schadensvariablen, und wo genau knallt es?

**2. Weis einer äußeren Variablen in einer Funktion etwas zu.** Setz in `berechne_schaden()` die Zeile `munition = 0` ein, ruf sie auf und prüf danach draußen die Munition. Was ist passiert — und was nicht?

**3. Und jetzt die Gegenprobe zu Experiment 2.** Häng in derselben Funktion `gegner.append(99)` an die Gegnerliste an. Prüf danach draußen.

**Beantworte, bevor du weiterliest:** Warum wirkt das eine nach außen und das andere nicht? Die Antwort steht in Etappe 4, nicht in dieser Etappe.

**4. ⭐ Bau ein Feature ein, während du umbaust.** Lös eine Funktion heraus und verbessere dabei „nur schnell" eine Meldung. Zieh danach den `diff`.

Er zeigt jetzt einen Unterschied — und du weißt, dass er von dir kommt. **Stell dir vor, du wüsstest es nicht.** Genau dafür gibt es die Regel aus Konzept 10. Danach zurückbauen.

---

Die folgenden drei sind Kür.

**5. Setz einen Standardwert nach vorn:** `def f(a=1, b)`. Lies die Fehlermeldung und überleg, warum Python das nicht zulassen kann.

**6. Bau `global` ein.** Nimm es in einer Funktion, um `schrott` direkt zu verändern, und lösch den entsprechenden Parameter. Es funktioniert — und ist kürzer.

**Und jetzt die Frage, um die es geht:** Wie viele Zeilen musst du lesen, um herauszufinden, welche Funktionen deinen Schrott verändern? Vorher stand es in jeder Signatur. Danach zurückbauen.

**7. Ruf eine Funktion auf, bevor sie definiert ist.** Schieb einen Aufruf über die `def`-Zeile. Lies die Fehlermeldung — sie erklärt dir, was `def` eigentlich tut.

---

**Experiment 2 und 3 sind das Paar, auf das es ankommt.** Sie zeigen dieselbe Regel von zwei Seiten, und wer nur eines von beiden macht, lernt die halbe Wahrheit.

**Experiment 4 ist das unangenehmste** und das, an das du dich in Etappe 8 erinnern wirst.

Alles in `GELERNT.md`, mit einem Satz dazu: **woran du es erkannt hättest.**

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `NameError: name 'x' is not defined` in einer Funktion | Der Wert wird nicht übergeben | Die Signatur — steht `x` in den Klammern? |
| `TypeError: f() missing 1 required positional argument` | Beim Aufruf fehlt ein Argument | Die **Aufruf**stelle, nicht die Definition |
| `TypeError: unsupported operand type(s) for +: 'NoneType'` | Die Funktion hat kein `return` | Konzept 3 — dieselbe Falle wie `append()` in Etappe 4 |
| Die Funktion rechnet richtig, draußen ändert sich nichts | Zuweisung an eine äußere Variable — Scope | Konzept 5. Rückgabewert benutzen |
| Eine äußere Liste ändert sich, obwohl du das nicht wolltest | *mutable* — der Inhalt lässt sich von innen ändern | Konzept 5, Warnkasten |
| `SyntaxError: non-default argument follows default argument` | Standardwert steht vor einem Parameter ohne | Standardwerte nach hinten |
| `IndentationError` direkt nach `def` | Der Körper ist nicht eingerückt | Die Zeile unter `def` |
| Nichts passiert beim Ausführen | Die Funktion ist definiert, aber nie aufgerufen | `def` legt an, es tut nichts |
| `diff` zeigt Unterschiede, obwohl du nur verschoben hast | Beim Verschieben eine Zeile verändert oder verloren | Die zuletzt herausgelöste Funktion — nur die |
| `diff` zeigt Unterschiede in Leerzeilen | Ein `print()` zu viel oder zu wenig beim Verschieben | Zeichengenau vergleichen, nicht ungefähr |

**Der Debugging-Reflex dieser Etappe: „Was geht rein, was kommt raus?"**

In Etappe 1 war es *welchen Typ hat dieser Wert?*, in 2 *welcher Zweig läuft?*, in 3 *wie oft läuft das?*, in 4 *was steht da wirklich drin?*, in 5 *unter welchem Namen?*. Heute:

```python
def berechne_schaden(waffe, ziel):
    print("### REIN ", waffe, ziel)
    ergebnis = ...
    print("### RAUS ", ergebnis)
    return ergebnis
```

Zwei Zeilen an den **Grenzen** der Funktion. Damit findest du in einer Minute heraus, ob eine Funktion falsch rechnet oder falsch gefüttert wird — und das sind zwei völlig verschiedene Fehler an zwei völlig verschiedenen Stellen.

**Nachsehen schlägt Vermuten**, seit Etappe 1. In Etappe 8 löst der Debugger alle sechs `print`-Reflexe ab.

*(Und vor dem Commit: alle `###`-Zeilen raus.)*

---

## Ein Blick nach vorne

**Etappe 8 ist die Bug-Jagd**, und sie kommt genau jetzt, weil dein Code zum ersten Mal aus Teilen besteht, die man einzeln verdächtigen kann. Der `print`-Reflex an den Funktionsgrenzen wird dort vom Debugger abgelöst, und das Halbieren aus Konzept 10 bekommt seinen Namen.

**Etappe 9 ist der Zahltag für den Schmerz von heute.** Deine lange Parameterliste wird zu `self`:

```
heute:   berechne_schaden(waffe, ziel, panzerung, klasse, boni, munition)
später:  marine.berechne_schaden(ziel)
```

Die Werte, die immer gemeinsam auftreten, gehören dann zusammen — als Objekt. **Deine Notiz aus Auftragsschritt 7 ist die Begründung dafür**, und sie ist überzeugender als alles, was ein Guide behaupten kann.

**Etappe 10** bringt die Falle mit veränderbaren Standardwerten — die eine Sache, die ich heute bewusst weggelassen habe, weil sie erst mit Objekten wirklich weh tut.

**Etappe 14a** setzt `zeichne_vorfeld()` neben deine Zeichenfunktionen. Dass das ohne Umbau geht, entscheidest du heute in Schritt 12.

**Etappe 20** validiert an Funktionsgrenzen — genau an den Stellen, die du heute geschaffen hast. Ein Wert wird geprüft, wo er hereinkommt, nicht in der Mitte einer Rechnung.

**Etappe 21a** macht aus `berechne_schaden()` die echte Trefferrechnung mit zwei Rückgabewerten. Deine Liste der nicht gebauten Einfälle ist dort die Vorlage.

**Etappe 23a** tötet `verarbeite_befehl()` in seiner heutigen Form — die `elif`-Kette wird ein Dictionary aus Funktionen. Dass Funktionen Werte sind, die man in ein Dictionary legen kann, wird dort weniger überraschen, wenn du heute mit ihnen gearbeitet hast.

**Etappe 26** verwandelt deinen Charakterisierungstest in `pytest`. Kein neues Konzept — nur ein Rahmen um dieselben Zeilen.

**Etappe 28** tauscht deine Zeichenfunktionen gegen Pygame aus, ohne die Logik anzufassen. **Ob das geht, entscheidest du heute in Schritt 13.** Das ist keine Übertreibung: Ein einziges `print` in `berechne_schaden()` macht dort den Unterschied zwischen einem Nachmittag und einer Neuschreibung.

---

## Abschluss

**In `GELERNT.md`:**

- Was habe ich gebaut? *(Ehrliche Antwort: nichts Neues. Und trotzdem war es die anstrengendste Etappe bisher.)*
- Was habe ich verstanden?
- Was hat mich überrascht? *(Kandidaten: `return` gegen `print`, Experiment 2 gegen 3, wie lang die Datei wirklich war)*
- Welchen Fehler habe ich gemacht — und **wie habe ich ihn gefunden?**
- **Die Design-Entscheidung:** Wie kommt Zustand in meine Funktionen — und warum so?
- ⭐ **Welche Funktion hat die längste Parameterliste, und welche Werte treten darin immer gemeinsam auf?** *(Das ist deine Vorarbeit für Etappe 9.)*
- ⭐ **Die Liste der Einfälle, die ich nicht gebaut habe.**
- Wie hat es sich angefühlt, einen ganzen Abend umzubauen, ohne dass der Spieler etwas merkt?

**Vor dem Commit:** Sind alle `###`-Debugzeilen raus? Gibt es kein `global`?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest. Alles freiwillig.

**Eine zweite Befehlsdatei für den Härtefall.** `befehle_chaos.txt` — nur Unsinn: leere Zeilen, Zahlen, Sonderzeichen, zwanzigmal derselbe Befehl. Lauf sie durch und schau, ob dein Spiel überlebt. Was du dabei findest, ist die Vorlage für Etappe 20.

**Eine Funktion, die eine Funktion aufruft, die eine Funktion aufruft.** Bau `verarbeite_befehl()` → `kaufe()` → `berechne_gesamtpreis()`. Setz an jede Grenze eine `### REIN`-Zeile und schau dir die Reihenfolge an. Du siehst zum ersten Mal einen **Aufrufstapel** — in Etappe 8 liest du genau den in jedem Traceback.

**Zähl deine Zeilen.** `wc -l spiel.py` vor und nach der Etappe. Die Zahl wird größer sein, nicht kleiner — Funktionen kosten Zeilen. **Zähl stattdessen, wie viele Zeilen die längste zusammenhängende Sache in deiner Datei hat.** Diese Zahl ist deutlich kleiner geworden, und sie ist die, auf die es ankommt.

**Ein Docstring für jede Funktion.** Nicht drei, sondern alle. Danach `help()` auf jede einzelne. Das ist stumpfe Arbeit und die beste Art zu merken, welche deiner Funktionen eigentlich zwei Dinge tut — denn die lassen sich nicht in einem Satz beschreiben.

Das ist der beste Zusatz hier, weil er dir eine Antwort auf Frage 10 der Lernziele gibt, die du dir nicht ausdenken musst.

---

> **Nächste Etappe:** [Etappe 8 — Bug-Jagd I](etappe-08-bug-jagd.md) · Debugger, Traceback, Fehlertypen, Halbieren
