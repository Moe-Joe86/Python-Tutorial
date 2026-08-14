# Etappe 3 — Die Game-Loop

> **Block 1: Fundament** · Etappe 3 von 29 · [← Etappe 2](etappe-02-die-erste-begegnung.md) · [Lehrplan](../RPG_Lehrplan.md) · [Etappe 4 →](etappe-04-das-inventar.md)

**Boot.dev:** `while`, `for`, `range()`, `break`, `continue`
**Zeitaufwand:** 4–6 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 2 abgeschlossen, Selbsttest grün

---

## Worum es geht

Bis jetzt läuft dein Programm genau einmal von oben nach unten. Der Spieler wacht auf, ruft, jemand findet ihn, er antwortet, die Figur reagiert — Schluss.

**Ab heute wartet dein Spiel auf den Spieler.**

Die Grundidee ist erstaunlich klein:

```text
frage nach einem Befehl
→ verarbeite ihn
→ reagiere
→ frage wieder
→ ...
```

Das ist die **Game-Loop**. Zwanzig Zeilen ungefähr — und das Skelett, an dem bis Etappe 29 alles andere hängt.

Der Sprung ist größer, als die Syntax vermuten lässt. Dein Programm bekommt zum ersten Mal einen **Zustand, der zwischen den Durchläufen bestehen bleibt**. Es merkt sich etwas über die Zeit. Es fragt, hört zu, reagiert, fragt wieder.

Das ist die Definition eines Spiels. **Feier den Tag, an dem das läuft.**

---

## Der lange Bogen

| Was du heute baust | Wo es wieder auftaucht |
|---|---|
| Die Hauptschleife | **Etappe 12** — jeder Durchlauf löst einen Tick der Weltzeit aus |
| Die Schleifen-Struktur selbst | **Etappe 27** — wird zur Pygame-Loop mit 60 Bildern pro Sekunde |
| Befehle lesen und unterscheiden | **Etappe 7** — wandert in die Funktion `verarbeite_befehl()` |
| `range()` | **Etappe 14** — jede einzelne Schleife über das Minenraster |
| `range()` zählt ab 0 | **Etappe 4** — derselbe Grund, warum der erste Listenindex 0 ist |
| Ein Zähler mit `+=` | **Etappe 12** — wird zu `self.zeit += 1`, der Weltzeit |
| Die Wiederholung bei ungültiger Eingabe | **Etappe 20** — wird zu echter Validierung mit `try`/`except` |
| Der Befehl `beenden` | **Etappe 19** — dort wird vorher gespeichert |
| Der `else`-Zweig für unbekannte Befehle | **Etappe 5** — wächst mit jedem neuen Befehl mit |
| Die lange `elif`-Kette (bewusst ertragen) | **Etappe 5** — das Dictionary löst sie ab |

**Und eine Schuld aus Etappe 2 wird heute eingelöst:** Dort hast du `.lower()` und `.strip()` auf eine einzelne Antwort angewendet. Heute wird daraus der Befehlsparser, durch den ab jetzt *jede* Eingabe läuft. Das war kein Zufall — es war Vorbereitung.

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

**Wie spricht der Spieler mit deinem Spiel?**

Das klingt nach Kosmetik und ist eine Architekturfrage. Was du heute festlegst, tippt dein Spieler hunderte Male.

**Frage 1: Ein Wort oder zwei?**
Heute reichen Ein-Wort-Befehle: `umsehen`, `reden`, `beenden`. Aber in Etappe 4 kommt `nimm brot`, in Etappe 5 `gehe norden`. Wenn du heute etwas baust, das nur ein einzelnes Wort verarbeiten kann, baust du es dort um.

Du musst zwei Wörter heute **nicht** umsetzen — dir fehlt das Werkzeug, es kommt in Etappe 4. Aber entscheide jetzt, wohin die Reise geht, und schreib es auf.

**Frage 2: Wie streng ist dein Spiel?**
Nur `umsehen`? Oder auch `schau`, `umschauen`, `u`? Jedes Synonym kostet ein `or` und erspart dem Spieler Frust. Ein Spiel, das die richtige Absicht wegen des falschen Wortes ablehnt, fühlt sich feindselig an.

**Frage 3: Befehlsform oder Grundform?**
`umsehen` oder `sieh dich um`? `nimm` oder `nehmen`? Beides geht — aber misch es nicht. Du selbst wirst dich in Etappe 5 nicht mehr erinnern, was du gewählt hattest.

**Was du heute nicht tust:** zwanzig Befehle erfinden. `inventar`, `schlafen`, `untersuchen` — dafür gibt es noch keine Mechanik. Du baust heute die *Struktur*, in die solche Befehle später hineinkommen. Schreib die Wunschliste in `GELERNT.md` und arbeite weiter.

---

## Die Konzepte

### 1. `while` — wiederholen, solange etwas gilt

```python
tassen = 3

while tassen > 0:
    print(f"Noch {tassen} Tassen.")
    tassen = tassen - 1

print("Kanne leer.")
```

Python prüft die Bedingung **vor jedem Durchlauf**. Ist sie `True`, läuft der Block, danach springt es zurück nach oben. Ist sie `False`, geht es hinter der Schleife weiter.

Aufbau wie beim `if` aus Etappe 2: Doppelpunkt, eingerückter Block. Die Einrückung entscheidet auch hier, was zur Schleife gehört.

**Das Entscheidende:** Irgendetwas *innerhalb* der Schleife muss dafür sorgen können, dass die Bedingung irgendwann falsch wird. Sonst läuft sie ewig.

### 2. `while` gegen `if` — der Unterschied, der oft untergeht

Beide sehen fast gleich aus. Sie tun etwas völlig Verschiedenes.

```python
if hunger:
    print("Du hast Hunger.")      # läuft höchstens einmal

while hunger:
    print("Du hast Hunger.")      # läuft, bis hunger falsch wird
```

> **`if`** — *wenn das gerade stimmt, mach es.* Einmal. Dann weiter.
> **`while`** — *solange das stimmt, mach es immer wieder.*

Wird `hunger` im Block nie verändert, läuft die zweite Fassung für immer. Der Unterschied ist ein Wort und zwei völlig verschiedene Programme.

### 3. `+=` — der Zähler

Die Zeile `tassen = tassen - 1` liest sich merkwürdig, wenn man `=` als Gleichheit missversteht. Als „bekommt den Wert" gelesen — deine Gewohnheit aus Etappe 1 — ergibt sie Sinn: *tassen bekommt den Wert, den tassen gerade hat, minus eins.*

Kürzer geht es so:

```python
zaehler = 0
zaehler += 1      # dasselbe wie: zaehler = zaehler + 1
zaehler -= 1
```

**Ein Zähler braucht zwei Dinge, und die Reihenfolge ist entscheidend:**

```python
runden = 0            # VOR der Schleife anlegen
while True:
    runden += 1       # IN der Schleife hochzählen
```

Steht `runden = 0` versehentlich *innerhalb* der Schleife, wird der Zähler bei jedem Durchlauf zurückgesetzt und steht ewig auf 1. Kein Absturz, keine Fehlermeldung — Fehler vom Typ 3. Er kommt unten als Experiment, weil du ihn einmal gesehen haben musst.

**Der lange Bogen:** In Etappe 12 heißt diese Zeile `self.zeit += 1` und ist die Uhr deiner Spielwelt. Derselbe Gedanke, anderer Ort.

### 4. Die Endlosschleife — und wie du rauskommst

```python
while True:
    print("Hilfe.")
```

`True` ist immer wahr, also endet das nie.

> **`Strg` + `C` bricht ein laufendes Python-Programm ab.** Auf dem Mac ebenfalls `Ctrl+C`, nicht `Cmd`.

Merk dir das jetzt, nicht wenn du es brauchst. **Bau eine Endlosschleife absichtlich, führ sie aus, brich sie ab.** Zwei Minuten, und die Panik ist für immer weg. Eine Endlosschleife ist kein Schaden — nur ein Programm, das genau das tut, was du geschrieben hast.

### 5. `break` und `continue`

```python
while True:
    eingabe = input("> ")
    if eingabe == "stop":
        break        # raus aus der Schleife, sofort
    if eingabe == "":
        continue     # zurück nach oben, Rest überspringen
    print(f"Du hast '{eingabe}' getippt.")
```

> **`break`** beendet die Schleife.
> **`continue`** beendet nur diesen Durchlauf.

Nach `break` macht Python mit dem Code **unterhalb** der Schleife weiter. Nach `continue` springt es zurück zur Bedingung.

**Beide wirken immer auf die innerste Schleife**, in der sie stehen. Heute egal, in Etappe 14 wichtig, wenn zwei Schleifen ineinander liegen.

Das heißt auch: `while True` ist nicht „unendlich und unkontrollierbar". Du baust dir bewusst einen Ausgang ein.

### 6. Zwei Arten, die Game-Loop zu bauen

Eine echte Wahl, keine Stilfrage. Beide Formen sind verbreitet, du solltest beide erkennen.

**Variante A — mit einer Flagge:**
```python
laeuft = True

while laeuft:
    befehl = input("> ")
    if befehl == "beenden":
        laeuft = False
```

**Variante B — mit `break`:**
```python
while True:
    befehl = input("> ")
    if befehl == "beenden":
        break
```

**A** liest sich selbsterklärend — die Bedingung oben sagt, worum es geht. Und du kannst die Flagge von mehreren Stellen setzen, auch aus tief verschachteltem Code.

**B** ist kürzer und macht den Ausstieg an genau einer Stelle sichtbar.

Nimm eine und zieh sie durch. Wenn du unsicher bist: **Variante A** passt besser zu diesem Projekt, weil `laeuft` eine Zustandsvariable ist — und Zustandsvariablen sind das Muster, das ab Etappe 12 dein ganzes Spiel trägt.

### 7. `for` — für jedes Element aus etwas

```python
for buchstabe in "Dorf":
    print(buchstabe)
```

Vier Zeilen: `D`, `o`, `r`, `f`. Die Variable bekommt bei jedem Durchlauf den nächsten Wert — du musst nichts hochzählen und nichts abbrechen.

In Etappe 4 wirst du `for` über Listen laufen lassen, und dort wird es richtig nützlich. Heute reicht ein String oder `range()`.

**Der Unterschied zu `while` in einem Satz:**

> `for` benutzt du, wenn du **weißt, wie oft** oder **worüber** du läufst. `while`, wenn du es **nicht** weißt.

Deine Game-Loop ist ein `while`, weil niemand weiß, wie lange jemand spielt. Drei Echos sind ein `for`, weil es genau drei sind.

### 8. `range()` — Zahlen zum Durchlaufen

```python
for i in range(5):
    print(i)
```

Ausgabe: `0 1 2 3 4`

**Zwei Dinge, über die jeder einmal stolpert:** `range(5)` beginnt bei **0**, nicht bei 1. Und endet bei **4** — die obere Zahl ist ausgeschlossen.

Das wirkt willkürlich, hat aber einen Grund: `range(5)` liefert genau fünf Werte, und sie passen exakt auf die Positionen einer Sammlung mit fünf Einträgen. In Etappe 4 lernst du, dass die Zählung bei Listen bei 0 beginnt. `range()` ist darauf abgestimmt. Ab Etappe 14 wirst du dankbar sein.

**Die Formen:**

```python
range(5)           # 0, 1, 2, 3, 4
range(2, 10)       # 2 … 9                    — Start, Ende
range(2, 10, 3)    # 2, 5, 8                  — Start, Ende, Schrittweite
range(10, 0, -1)   # 10, 9, 8 … 1             — rückwärts
```

Bei `range(2, 10, 3)`: 2, dann +3 = 5, dann +3 = 8, dann wäre 11 — jenseits von 10, also Schluss.

**Die Schleifenvariable ist keine Deko.** Du darfst `i` im Block benutzen, und meistens solltest du:

```python
for i in range(3):
    print(f"Durchgang {i + 1} von 3")
```

Brauchst du den Wert wirklich nicht, ist ein Unterstrich üblich: `for _ in range(3):`. Das ist ein Signal an den Leser — „läuft dreimal, die Zahl ist egal". Du wirst es in fremdem Code sehen.

**Der lange Bogen:** In Etappe 14 sieht deine Minenkarte so aus:

```python
for y in range(len(karte)):
    for x in range(len(karte[y])):
```

Zwei Schleifen ineinander, beide über `range()`, und daran hängt der ganze Dungeon.

### 9. Die Eingabe-Schleife — die Schuld aus Etappe 2

In Etappe 2 stand: *„Eine Schleife, die die Frage wiederholt, bis eine gültige Antwort kommt → Etappe 3."* Hier ist sie.

Beachte, dass `input()` **innerhalb** der Schleife steht:

```python
while True:
    antwort = input("Ja oder nein? ").lower().strip()
    if antwort == "ja" or antwort == "nein":
        break
    print("Bitte antworte mit ja oder nein.")
```

Solange die Antwort nicht passt, wird erneut gefragt. Erst eine gültige Antwort bricht aus.

**Warum `input()` in der Schleife stehen muss:** Steht es davor, wird einmal gefragt, und die Schleife prüft danach ewig denselben Wert. Das ist die häufigste Endlosschleife von Anfängern und steht unten als Experiment.

**Ehrlich eingeordnet:** Gut genug für heute und trägt lange. Nicht endgültig — in Etappe 20 lernst du `try`/`except` und fängst damit Fälle ab, die sich mit `if` gar nicht prüfen lassen.

---

## Dein Auftrag

Schrittweise. Nach jedem Schritt ausführen. Die Schleife ist der erste Ort, an dem ein Tippfehler dein Programm nicht abstürzen, sondern *hängen* lässt — umso wichtiger, klein zu arbeiten.

**Schritt 1 — Die nackte Schleife**
Nach der Szene aus Etappe 2: eine Schleife, die `> ` fragt, die Eingabe entgegennimmt und bei `beenden` abbricht. Sonst nichts. Ausführen, ein paar Wörter tippen, sauber beenden.

Eine Handvoll Zeilen — und der wichtigste Schritt der Etappe.

**Schritt 2 — Die Eingabe brauchbar machen**
`.lower()` und `.strip()` aus Etappe 2, jetzt auf jede Eingabe. Ab hier sind `BEENDEN`, `beenden` und ` Beenden ` dasselbe.

**Schritt 3 — Drei Befehle**
`umsehen`, `reden`, `beenden`.

`umsehen` beschreibt den Ort — benutz deine Variablen aus Etappe 1: Tageszeit, Wetter, Geruch, Dorfname. Kein Kartensystem, das kommt in Etappe 5.

`reden` spricht die Figur aus Etappe 2 an. **Und hier zahlt deine Entscheidung von damals:** Die Figur reagiert unterschiedlich, je nachdem, ob `vertrauen` gesetzt ist. Ein `if` innerhalb der Schleife, mehr braucht es nicht.

Damit passiert etwas Bemerkenswertes: Eine Szene, die bisher einmalig war, ist jetzt wiederholbar — und trägt trotzdem das Gedächtnis der letzten Etappe.

**Schritt 4 — Unbekannte Befehle**
Ein `else`-Zweig. Die entscheidende Auflage: **Das Spiel läuft weiter.** Es stürzt nicht ab, beendet sich nicht, beschimpft niemanden.

Schreib den Text so, dass er hilft: „Das kenne ich nicht. Versuch `umsehen`, `reden` oder `beenden`." Ein Spiel, das nur „Unbekannter Befehl" sagt, lässt den Spieler raten.

**Schritt 5 — Der Zähler**
Eine Variable vor der Schleife, die mitzählt, wie viele Befehle eingegeben wurden. Innerhalb hochzählen.

Benutz sie für etwas Sichtbares — beim `beenden` ausgeben, wie viele Runden vergangen sind. Ein Zähler, den niemand sieht, ist nicht überprüfbar.

Kommentar dazu: In Etappe 12 wird daraus die Weltzeit.

**Schritt 6 — Eine `for`-Schleife mit `range()`**
Irgendwo, wo sie erzählerisch passt. Naheliegend ist der Ruf aus Etappe 1: Das Echo verhallt in mehreren Stufen.

**Auflage:** Benutz die Schleifenvariable im Text. Nicht dreimal dasselbe ausgeben — lass die Ausgabe sich mit `i` verändern. Ein Echo, das leiser wird, ist eine Zeile mehr und ein anderer Effekt.

**Schritt 7 — Die Eingabe-Wiederholung**
An einer Stelle deiner Wahl: eine Frage, die wiederholt wird, bis eine gültige Antwort kommt. Naheliegend ist die Frage aus Etappe 2 — die kannst du jetzt nachrüsten, ohne dass ein `else` die falsche Antwort schluckt.

Das ist zugleich deine erste Übung im übergreifenden Prinzip: **Etwas verbessern, ohne das Bestehende kaputtzumachen.** Danach müssen beide Antwortwege noch genauso funktionieren wie vorher.

**Schritt 8 — Alles zusammen**
So soll es sich anfühlen:

```text
[deine Szene aus Etappe 1 und 2]

> umsehen
[Umgebung]

> reden
[Reaktion — abhängig von vertrauen]

> fisch
[Das kenne ich nicht. Versuch ...]

> beenden
[Abschluss, mit Rundenzahl]
```

---

## Was NICHT in diese Etappe gehört

- ❌ Gegenstände aufheben (`nimm brot`) → **Etappe 4**
- ❌ Mehrere Orte und `gehe norden` → **Etappe 5**
- ❌ Befehle in einer Liste oder einem Dictionary sammeln → **Etappe 5 und 7**
- ❌ Die Schleife in eine Funktion packen → **Etappe 7**
- ❌ `try` / `except` → **Etappe 20**
- ❌ Ein Tick-System, bei dem NPCs sich bewegen → **Etappe 12**
- ❌ Zufällige Ereignisse pro Runde → **Etappe 17**

**Besonders verlockend wird das Dictionary sein**, sobald du den vierten Befehl schreibst und die `elif`-Kette länger wird. Du wirst irgendwann denken: *„Das wird unübersichtlich, das gehört in eine Funktion."*

**Genau.** Und das ist kein Problem, das du heute löst — es ist die Aufgabe von Etappe 7. Heute darf die Kette lang sein. Sie zu *spüren* ist der Grund, warum du in Etappe 5 und 7 verstehst, wozu die Werkzeuge gut sind, statt sie nur abzuschreiben.

---

## Selbsttest

- [ ] Das Spiel läuft von Etappe 1 über Etappe 2 in die Schleife hinein
- [ ] Mindestens drei Befehle funktionieren
- [ ] `beenden` beendet sauber — kein Absturz, kein `Strg+C` nötig
- [ ] Unbekannte Befehle werden abgefangen, und das Spiel läuft weiter
- [ ] `Umsehen`, `UMSEHEN` und ` umsehen ` werden gleich behandelt
- [ ] `reden` berücksichtigt `vertrauen` aus Etappe 2
- [ ] Es gibt genau einen klaren Weg aus der Hauptschleife
- [ ] Ein Zähler wird vor der Schleife angelegt und darin hochgezählt
- [ ] Der Zähler ist irgendwo sichtbar
- [ ] Eine `for`-Schleife mit `range()` ist im Einsatz
- [ ] Die Schleifenvariable wird im Block tatsächlich benutzt
- [ ] Mindestens eine Eingabe wird wiederholt, bis sie gültig ist
- [ ] Du hast `continue` mindestens einmal ausprobiert
- [ ] Du hast absichtlich eine Endlosschleife gebaut und mit `Strg+C` beendet
- [ ] Ein Kommentar verweist auf Etappe 12

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten:

1. **Wann `while`, wann `for`?** Je ein Beispiel aus deinem eigenen Spiel.
2. **Was ist der Unterschied zwischen `if` und `while`?** Was passiert, wenn du in einer `while`-Bedingung nie etwas veränderst?
3. **Was ergibt `range(5)` genau?** Welche Zahlen, und warum ist die letzte nicht dabei?
4. **Was ergibt `range(2, 10, 3)`?** Schreib die Zahlen auf, *bevor* du es ausprobierst.
5. **Unterschied zwischen `break` und `continue`?** Beschreib ihn, ohne die Wörter nur zu wiederholen. Was passiert jeweils mit dem Rest des Durchlaufs?
6. **Wie entsteht eine Endlosschleife — und wie kommst du raus?**
7. **Warum muss `input()` innerhalb der Schleife stehen?** Was passiert, wenn es davorsteht?
8. **Was ist der Unterschied zwischen `while laeuft:` mit Flagge und `while True:` mit `break`?** Welche hast du gewählt und warum?
9. **Warum muss ein Zähler vor der Schleife angelegt werden?**

Frage 7 und 9 beschreiben dieselbe Fehlerklasse aus zwei Richtungen: eine Zeile auf der falschen Seite der Einrückung. Wer beide sauber erklären kann, hat verstanden, was eine Schleife tut.

Und wenn du unsicher bist: **nicht nachschlagen, sondern den Code verändern und zusehen.** Gerade bei Schleifen ist Ausprobieren schneller als jede Erklärung.

---

## Transferaufgabe (10–15 Minuten)

**Neue Datei, außerhalb des Spiels.** `uebung_03.py`.

### Teil 1 — Zahlenraten

> Das Programm legt eine Zahl zwischen 1 und 100 fest. Der Spieler rät. Nach jedem Versuch: „zu hoch" oder „zu niedrig". Bei Treffer: Glückwunsch und die Anzahl der Versuche.

Die Zahl darfst du fest hineinschreiben — Zufall kommt in Etappe 17. Wenn du `random` heute schon nachschlagen willst, ist das eine gute Übung im Selbernachschlagen, aber keine Pflicht.

Darin stecken drei Dinge: eine Schleife mit unbekannter Länge, ein Zähler, und die Umwandlung von `input()` in eine Zahl. Der letzte Punkt ist der Rückfall aus Etappe 1 — wenn du ihn nochmal machst, ist das der beabsichtigte Effekt.

**Danach, die eigentliche Übung:** Schreib es ein zweites Mal mit der jeweils anderen Loop-Variante. Hattest du `while True:` mit `break`, nimm jetzt eine Flagge — oder umgekehrt. Vergleich die beiden Fassungen. Welche liest sich besser?

### Teil 2 — `range()` gegen Bedingung

> Gib alle geraden Zahlen von 0 bis 20 aus. Einmal mit der Schrittweite von `range()`. Einmal mit `range()` über alle Zahlen und einer Bedingung im Block.

Beide sind vier Zeilen. Beide richtig. Lies sie nebeneinander und entscheide, welche du in vier Monaten lieber vorfinden würdest.

Keine Fangfrage — es gibt keine falsche Antwort. Der Zweck ist, dass du anfängst, Code nach **Lesbarkeit** zu beurteilen und nicht nur danach, ob er läuft. Diese Gewohnheit ist ab Etappe 23 dein eigentliches Ziel.

---

## Kaputtmachen

Nach jedem Experiment rückgängig machen. Du wirst `Strg+C` brauchen — das ist Absicht.

**Experiment 1 — `break` entfernen**
Nimm das `break` (oder `laeuft = False`) heraus. Was passiert bei `beenden`? Wie kommst du raus? **Schreib deine Erklärung auf, bevor du repariert.**

**Experiment 2 — `input()` vor die Schleife ziehen**
Verschieb die `input()`-Zeile direkt vor das `while`. Ausführen. Was passiert, und warum?

**Das ist die häufigste Endlosschleife überhaupt.** Und die Lektion dahinter ist größer als der Fehler: Eine Schleife wiederholt zwar etwas — aber wenn sich die Daten darin nicht ändern, wiederholt sie immer wieder dasselbe.

**Experiment 3 — Der Zähler an der falschen Stelle**
Verschieb `runden = 0` in die Schleife hinein. Kein Absturz. Aber was zeigt der Zähler jetzt an, egal wie lange du spielst? Fehler vom Typ 3, sauber vorgeführt.

**Experiment 4 — `break` gegen `continue`**
Ersetz das `break` bei `beenden` durch `continue`. Was ändert sich? Warum kannst du das Spiel nicht mehr verlassen?

**Experiment 5 — Die Grenzen von `range()`**
Schreib **erst auf, welche Zahlen du erwartest**, dann führ aus:
```python
range(5)
range(1, 5)
range(1, 6)
range(0, 21, 2)
range(10, 0, -1)
```
Bei welcher lagst du falsch? Das ist die, die du dir merken musst.

**Experiment 6 — Die Bedingung, die nie falsch wird**
```python
tassen = 3
while tassen > 0:
    print(tassen)
```
Was fehlt? `Strg+C`. Frag dich danach: **Welche Information hätte sich innerhalb der Schleife verändern müssen?**

**Experiment 7 — Einrückung eine Ebene zu weit links**
Nimm eine Zeile aus der Schleife und rück sie auf die Ebene des `while`. Läuft sie noch? Wann? Derselbe Fehler wie in Etappe 2 — in einer Schleife fühlt er sich völlig anders an.

---

## Häufige Stolpersteine

| Fehlermeldung / Symptom | Was dahintersteckt | Wo du suchst |
|---|---|---|
| Programm hängt, nichts passiert | Endlosschleife | `Strg+C`, dann: Was ändert die Bedingung? |
| Dieselbe Ausgabe rast endlos durch | `input()` steht außerhalb der Schleife | Die Einrückung von `input()` |
| Die Schleife läuft nur einmal | `break` nicht eingerückt oder zu früh | Der Block unter `while` |
| `beenden` beendet nicht | `break` wird nie erreicht | Bedingung und Einrückung |
| `IndentationError: expected an indented block` | Nach dem Doppelpunkt fehlt der Block | Die Zeile unter `while` / `for` |
| `SyntaxError: invalid syntax` | Doppelpunkt vergessen | Die `while`- oder `for`-Zeile |
| `NameError: name 'runden' is not defined` | Zähler nicht vor der Schleife angelegt | Über der Schleife |
| Der Zähler steht immer auf 1 | Initialisierung steht in der Schleife | Einrückung von `runden = 0` |
| `TypeError: 'int' object is not iterable` | `for i in 5:` statt `for i in range(5):` | Die `for`-Zeile |
| Der letzte Wert fehlt | `range()` schließt die obere Grenze aus | Ist das Absicht oder ein Fehler? |
| `Umsehen` wird nicht erkannt | Eingabe nicht normalisiert | `.lower()` |
| ` umsehen ` wird nicht erkannt | Leerzeichen blieben stehen | `.strip()` |

**Der wichtigste neue Debugging-Reflex dieser Etappe.** Bei einer Schleife fragst du nicht zuerst:

> „Welche Zeile ist falsch?"

Sondern:

> **„Was ist der Zustand am Anfang dieses Durchlaufs — und was ist er am Ende?"**

Bei Schleifen liegt der Fehler fast nie in einer einzelnen Zeile, sondern in dem, was sich von Durchlauf zu Durchlauf *nicht* verändert. Und wenn du das nicht weißt, gibst du es aus:

```python
print(f"DEBUG: Runde {runden}, befehl = '{befehl}'")
```

Diese eine Zeile beantwortet fast jede Schleifenfrage: Läuft sie überhaupt? Wie oft? Was steht wirklich drin? Die Anführungszeichen sind wieder wichtig — nur so siehst du ein verirrtes Leerzeichen.

---

## Ein Blick nach vorne

Heute ist deine Schleife noch schlicht:

```text
Befehl → Reaktion → Befehl → Reaktion
```

In **Etappe 4** bekommt der Spieler ein Inventar. Aus `umsehen` wird `nimm schlüssel`, und die Schleife bekommt eine echte Aufgabe: Sie wartet nicht mehr auf Text, sondern **verändert den Zustand deiner Welt**.

In **Etappe 5** kommt die Karte, und `gehe norden` bewegt dich wirklich.

In **Etappe 7** wird die immer länger werdende Befehlsverarbeitung in Funktionen zerlegt.

Und in **Etappe 12** passiert der entscheidende Schritt — jeder Durchlauf wird zu einem Tick der Welt:

```text
Befehl entgegennehmen
→ den Spieler handeln lassen
→ die Zeit weiterstellen
→ NPCs aktualisieren
→ Pflanzen wachsen lassen
→ Ereignisse prüfen
→ die Welt darstellen
→ wieder von vorn
```

Ab dann lebt dein Dorf, ob der Spieler etwas tut oder nicht.

Du baust heute also nicht nur eine Schleife. Du baust das **Rückgrat deines Spiels** — und alles, was noch kommt, hängt sich in diese sieben Zeilen ein.

---

## Abschluss

**`GELERNT.md`:**
Zwei bis drei Sätze. Zusätzlich diesmal drei Dinge:

- Deine Befehlssprache als Liste
- Flagge oder `break` — und warum
- Was sich für dich verändert hat, seit dein Programm nicht mehr nach der Szene aus Etappe 2 endet

**Commit:**
```bash
git add .
git commit -m "Etappe 3: Das Spiel läuft"
git push
```

Schau danach einmal `git log --oneline` an. Vier Commits, und dein Spiel wartet auf Eingaben. Das ist mehr, als die meisten je erreichen, die „mal Programmieren lernen" wollten.

---

## Wenn du mehr willst

Optional, erst bei grünem Selbsttest.

**Ein `hilfe`-Befehl.** Listet auf, was möglich ist. Fünf Minuten, und dein Spiel wird für Fremde benutzbar. In Etappe 25 wird daraus ein Eintrag in einer Datei — heute sind es ein paar `print()`.

**Synonyme.** `schau` und `umsehen` machen dasselbe. Ein `or` in der Bedingung. Achte darauf, wie schnell die Bedingungen unübersichtlich werden — merk dir das Gefühl für Etappe 5.

**Die leere Eingabe.** Was passiert, wenn jemand nur Enter drückt? Erkenn den Fall und überspring ihn mit `continue`. Kleine, aber echte Anwendung.

**Ein Zähler, der die Erzählung verändert.** Beim ersten `umsehen` beschreibst du das Dorf. Beim dritten fällt dem Spieler etwas auf, das vorher nicht da war. Beim fünften wird die Stille unangenehm.

Gebaut mit `if` und einem Zähler, keine neue Technik.

Wenn du es *regelmäßig* wiederkehren lassen willst — jede fünfte Runde ein Geräusch —, brauchst du einen Operator, den du noch nicht kennst: `%` liefert den Rest einer Division.

```python
if runden % 5 == 0:
    print("Irgendwo fällt etwas um.")
```

`17 % 5` ergibt 2, `20 % 5` ergibt 0. Immer wenn der Rest 0 ist, ist die Rundenzahl glatt durch 5 teilbar. Das ist die übliche Art, in Programmen etwas zyklisch passieren zu lassen, und du wirst sie überall wiedersehen — in Etappe 12 steuert genau dieses Muster den Tagesablauf deiner Welt.

Aber es ist das erste Mal, dass dein Spiel **auf verstrichene Zeit reagiert** statt auf eine Eingabe — und genau dieses Muster ist ab Etappe 12 das Rückgrat deines lebendigen Dorfes. Wenn du eine Sache aus diesem Abschnitt mitnimmst, dann diese.

**Eine Pause zwischen den Echos.** Wenn du in Etappe 1 schon `time.sleep()` nachgeschlagen hast, kombinier es mit der `for`-Schleife. Ein Echo, das in Abständen verhallt, wirkt völlig anders als drei Zeilen auf einmal.

---

> **Nächste Etappe:** [Etappe 4 — Das Inventar](etappe-04-das-inventar.md) · Listen, `append()`, `remove()`, `len()`, Indexing
> Dort bekommt dein Spieler zum ersten Mal etwas in die Hand. Und du lernst den Unterschied kennen, der später die meisten unverständlichen Fehler erklärt.
