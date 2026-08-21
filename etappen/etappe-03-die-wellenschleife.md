# Etappe 3 — Die Wellenschleife ⭐

> **Block 1: Fundament** · Etappe 3 von 30 · [← Etappe 2](etappe-02-der-erste-kontakt.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 4 →](etappe-04-ausruestung-und-beute.md)

**Boot.dev:** `while`, `for`, `range()`, `break`, `continue`
**Zeitaufwand:** 3a: 2 Sitzungen · 3b: 2 Sitzungen · 3c: 2 Sitzungen, à 20–30 Minuten
**Voraussetzung:** Etappe 2 abgeschlossen, Selbsttest grün

**Diese Etappe hat drei Portionen** — die einzige im ganzen Plan, die so weit aufgeteilt ist. Hier wird aus einem Skript ein Spiel, und dabei kommt mehr zusammen, als an einem Abend ankommt. Nach jeder Portion steht ein Commit.

| | Thema | 🔨 Bauen | 👀 Nur erkennen |
|---|---|---|---|
| **3a** | Die Schleife | `for` außen, `while` innen, `range()`, `break`, **wo Variablen leben** | `continue`, `_` |
| **3b** | Die Befehle | Befehlskette, `.lower()`, Rundenzähler | — |
| **3c** | Kampf und Anzeige | Gegner, Feuern, Nachladen, Balken | Formatangaben im f-String |

**Nach 3a wartet dein Programm auf dich. Nach 3b kannst du mit ihm reden. Nach 3c kannst du verlieren.**

---

## Worum es geht

Dein Programm läuft einmal durch und ist fertig. Der Spieler wählt eine Klasse, sieht seine Werte, feuert genau einen Schuss — das war es. Wer noch einmal spielen will, startet neu.

Heute endet das.

> **Eine Schleife ist der Unterschied zwischen einem Programm, das etwas anzeigt, und einem, das auf dich wartet.**

Das ist der erste Meilenstein dieses Tutorials. Du wirst es merken: Du fängst an, dein Programm zu *spielen*, statt es auszuführen.

**Dafür brauchst du zwei verschiedene Schleifen**, denn dein Spiel hat zwei Ebenen:

```
Welle 1 ──┬── Runde 1 ── Runde 2 ── Runde 3 ── ...
          │
Welle 2 ──┼── Runde 1 ── Runde 2 ── ...
          │
   ...    │
Welle 20 ─┘
```

Außen zwanzig Wellen — eine Zahl, die feststeht. Innen die Runden einer Welle — so viele, bis die Welle vorbei ist. **Zwei Ebenen, zwei Schleifenarten. Die Unterscheidung dazwischen ist der ganze Lernstoff von 3a.**

---

## Das Ritual — ab heute bei jedem Schritt

Der Lehrplan nennt es das Ritual, und ab dieser Etappe wird es zur Gewohnheit. Vier Schritte, jedes Mal:

> **Vorhersagen → Ausführen → Vergleichen → Erklären**

Bevor du auf „Ausführen" drückst, sag dir, was passieren wird. Wie viele Zeilen? In welcher Reihenfolge? Welcher Wert steht am Ende in welcher Variable?

**Der Punkt ist nicht, richtig zu liegen.** Der Punkt ist, dass du überhaupt eine Erwartung hast — denn nur dann kannst du überrascht werden, und Überraschung ist die einzige Stelle, an der Lernen wirklich stattfindet. Wer ohne Vorhersage ausführt, sieht ein Ergebnis und nickt. Wer mit Vorhersage ausführt, sieht einen Unterschied und fragt warum.

Bei Schleifen zahlt das ab heute doppelt: Der häufigste Schleifenfehler ist nicht „stürzt ab", sondern „läuft einmal zu oft".

---

## Der lange Bogen

**Lies das einmal und vergiss es dann.** Es ist Buchführung, keine Hausaufgabe.

**Was aus Etappe 1 und 2 heute eingelöst wird:**

| Schuld | Woher | Wie sie beglichen wird |
|---|---|---|
| `wellen_bis_evakuierung = 20` lag ungenutzt herum | **1** | Steuert die äußere Schleife |
| `kern_integritaet = 100` hatte keine Wirkung | **1** | Wird zur Abbruchbedingung |
| Der ASCII-Kopf war reine Kulisse | **1** | Der `status`-Befehl bekommt Balken |
| `f"{anteil:.0%}"` als Vorgeschmack | **1**, optional | Wird für die Prozentanzeige gebraucht |
| Ungültige Eingabe beendete das Programm | **2** | Führt jetzt zu einer neuen Frage |
| `.lower()` wurde vertagt | **2** | Jetzt tippt der Spieler Wörter |
| Feuern ging genau einmal | **2** | Wird zu einem Befehl unter mehreren |

**Sieben Schulden auf einmal.** Kein Zufall: Etappe 1 und 2 haben absichtlich Dinge angelegt, die ohne Schleife sinnlos sind. Wenn dir dort etwas willkürlich vorkam — zwanzig Wellen, ohne dass irgendwo zwanzigmal etwas passiert —, war das der Grund.

**Was heute entsteht und später wiederkommt:**

| Was entsteht | Wo es wiederkommt |
|---|---|
| **Die Hauptschleife selbst** | **12** — jeder Durchlauf löst einen Tick aus · **28** — sie wird zur Pygame-Loop |
| **Die `elif`-Kette der Befehle** | **7a** — wandert in eine Funktion · **23a** — stirbt durch ein Befehls-Dictionary |
| **Deine Befehlssprache** | **4** — `nimm schrott` · **5** — `kaufe medkit` |
| **Die Platzhalter-Kampfformel** | **21a** — wird zur echten Trefferrechnung |

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

**Wie sprechen deine Befehle?**

**A — ein Wort:** `feuern`, `status`, `nachladen`, `beenden`. Der Vergleich ist ein simples `==`, genau wie in Etappe 2.

**B — Verb und Ziel:** `feuern nordtor`, `nimm schrott`, `kaufe medkit`. Braucht ein Werkzeug, das die Eingabe zerlegt — das ist Etappe 4.

**Bau heute A.** Und schreib in `GELERNT.md`:

> *„Meine Befehle sind einwortig. Ab Etappe 4 brauche ich Verb + Ziel und muss umbauen."*

Du wirst B brauchen — spätestens, wenn es mehrere Waren zu kaufen gibt und `kaufe` allein nicht sagt, *was*. Der Umbau kostet zehn Minuten.

**Warum nicht gleich richtig:** Weil diese zehn Minuten dir etwas beibringen, das keine Erklärung leisten kann — wie es sich anfühlt, wenn eine frühe Entscheidung später Arbeit macht. Diese Erfahrung ist hier billig zu haben.

**Zweite Frage, kürzer:** Wie heißt dein Beenden-Befehl? Entscheide dich und bleib dabei — in Etappe 19 hängt das Speichern daran.

---

# Portion 3a — Die Schleife

## Die Konzepte

### 1. `while` — wiederholen, bis etwas eintritt

```python
tassen = 3
while tassen > 0:
    print(f"Noch {tassen} Tassen auf dem Tresen.")
    tassen -= 1
print("Tresen leer.")
```

**Die Struktur kennst du vom `if`** — Bedingung, Doppelpunkt, eingerückter Block. Und genau das ist die Falle: Sie sehen fast gleich aus und tun etwas völlig Verschiedenes.

```python
if tassen > 0:
    print("Noch Tassen da.")      # läuft höchstens einmal

while tassen > 0:
    print("Noch Tassen da.")      # läuft, bis die Bedingung falsch wird
```

> **`if`** — *wenn das gerade stimmt, mach es.* Einmal. Dann weiter.
> **`while`** — *solange das stimmt, mach es immer wieder.*

**Ein Wort Unterschied, zwei völlig verschiedene Programme.**

Daraus folgt die wichtigste Eigenschaft: **Irgendetwas im Block muss die Bedingung irgendwann falsch machen.** Hier ist es `tassen -= 1`.

Nimm die Zeile weg, und `tassen` bleibt für immer 3. Das ist die **Endlosschleife**, und du wirst sie heute bauen. Sie ist kein Drama:

> **`Strg + C` im Terminal bricht ab.** Merk dir das jetzt, nicht erst, wenn du es brauchst.

### 2. `for` und `range()` — wiederholen, wie oft du sagst

```python
for nummer in range(3):
    print(f"Durchgang {nummer}")
```

**Sag die Ausgabe vorher, bevor du weiterliest.** Dann führ es aus.

**Zwei Dinge überraschen hier fast jeden.**

**`range(3)` zählt 0, 1, 2** — drei Zahlen, aber ab null. Das ist keine Schrulle, sondern zieht sich durch die ganze Sprache: In Etappe 4 wirst du sehen, dass auch der erste Listeneintrag die Nummer 0 hat.

**`nummer` musst du nirgends anlegen.** `for` erzeugt die Variable selbst und füllt sie bei jedem Durchlauf neu.

**Die drei Formen:**

| Aufruf | Ergibt |
|---|---|
| `range(5)` | 0, 1, 2, 3, 4 |
| `range(1, 5)` | 1, 2, 3, 4 |
| `range(2, 11, 3)` | 2, 5, 8 |

**Die zweite Zahl ist immer ausgeschlossen.** Rechne selbst nach, welche Zahlen `range(1, 21)` liefert — und ob das zu deinen zwanzig Wellen passt.

*(Diese Sorte Fehler hat einen Namen — Off-by-One — und begegnet dir in Etappe 8 als eigene Kategorie wieder.)*

### 3. Die eigentliche Frage: `for` oder `while`?

Das ist der Kern von 3a, und die Antwort ist kurz:

> **`for`, wenn du beim Start weißt, wie oft.**
> **`while`, wenn du nur weißt, wann Schluss ist.**

Zwei Beispiele aus einer Bäckerei:

```python
# Ich weiß: zwölf Bleche. → for
for blech in range(12):
    backe(blech)

# Ich weiß nicht, wie viele Kunden kommen. Nur: bis 18 Uhr. → while
while uhrzeit < 18:
    bediene_kunden()
```

**Und warum das keine Geschmacksfrage ist:** Ein `while` mit fester Anzahl braucht einen Zähler, den du selbst anlegst, hochzählst und prüfst. Drei Stellen, an denen etwas schiefgehen kann. `for` hat sie gar nicht erst.

### 4. Schleife in Schleife

```python
for durchgang in range(3):
    vorrat = 2
    while vorrat > 0:
        print(f"Durchgang {durchgang}, Vorrat {vorrat}")
        vorrat -= 1
```

**Sag vorher, wie viele Ausgabezeilen das gibt und in welcher Reihenfolge.** Dann ausführen. Wenn du danebenlagst, hast du gerade das Wichtigste dieser Portion gelernt.

Die innere Schleife läuft **vollständig durch**, bevor die äußere weiterrückt.

⚠️ **Die Einrückung trägt jetzt zwei Ebenen.** Acht Leerzeichen heißt „innen", vier heißt „außen". Eine Zeile um vier Leerzeichen zu verrutschen, verschiebt sie zwischen den Ebenen — ohne Fehlermeldung.

### 5. Wo lebt welche Variable? ⭐

**Das ist die Frage, die verschachtelte Schleifen dir stellen — und du brauchst sie schon in Auftragsschritt 3.**

Sobald es zwei Ebenen gibt, gibt es drei Plätze für eine Variable, und jeder bedeutet etwas anderes:

```python
vorrat = 100                  # (1) VOR den Schleifen
for durchgang in range(3):
    portion = 10              # (2) pro Durchgang neu
    while portion > 0:
        rest = portion - 1    # (3) pro Runde neu
        portion -= 1
```

| Ebene | Wann wird sie gesetzt | Wofür |
|---|---|---|
| **(1) vor den Schleifen** | genau einmal, beim Start | Werte, die das ganze Spiel überdauern |
| **(2) in der äußeren Schleife** | zu Beginn jedes Durchgangs neu | Werte, die pro Durchgang frisch anfangen |
| **(3) in der inneren Schleife** | in jeder Runde neu | Zwischenergebnisse, die niemand behalten muss |

**Für dein Spiel heißt das konkret. Schreib dir das ab, bevor du tippst:**

| Variable | Ebene | Warum |
|---|---|---|
| `kern_integritaet` | **1** | Der Schaden aus Welle 3 ist in Welle 4 noch da |
| `munition` | **1** | Verbrauchtes bleibt verbraucht |
| `wellen_bis_evakuierung` | **1** | Ändert sich nie |
| Die Gegnerzahl | **2** | Jede Welle bringt neue Gegner mit |
| Die Eingabe des Spielers | **3** | Interessiert nur, solange sie verarbeitet wird |

> **Wo du eine Variable erzeugst, entscheidet darüber, wann sie neu gesetzt wird.**

**Und der Grund, warum das keine Formalie ist: Beide Varianten laufen ohne Fehlermeldung.** Eine Gegnerzahl auf Ebene 1 wird nie zurückgesetzt — Welle 2 beginnt dann mit den Resten von Welle 1 oder mit gar keinen Gegnern, und das Spiel läuft klaglos weiter. Kein Absturz, nur ein Spiel, das nicht funktioniert.

**Den Rundenzähler lasse ich hier bewusst weg.** Er kann auf Ebene 1 *oder* 2 stehen, beides ergibt ein sinnvolles Spiel — das ist deine Entscheidung, und sie kommt in 3b (Konzept 11).

*(In Etappe 7a bekommt dieses Verhalten einen Fachbegriff und ein paar zusätzliche Regeln. Heute brauchst du den Begriff nicht — du brauchst die Tabelle.)*

### 6. `break` — vorzeitig raus

```python
for kunde in range(50):
    if brote_uebrig == 0:
        print("Ausverkauft.")
        break
    verkaufe_brot()
```

`break` verlässt die Schleife sofort — auch mitten im Durchlauf.

**Und die eine Regel, die du dir merken musst:**

> **`break` verlässt immer nur die Schleife, in der es direkt steht.**

Bei zwei Ebenen heißt das: Ein `break` in der inneren Schleife beendet den inneren Durchlauf. Die äußere macht weiter. Heute noch harmlos — in Auftragsschritt 6 wird daraus die Knobelstelle.

### 7. 👀 `continue` und `_`

Zwei Kleinigkeiten, die du **erkennen** sollst und heute nicht baust.

```python
for zahl in range(6):
    if zahl == 3:
        continue
    print(zahl)
```

`continue` überspringt den **Rest des aktuellen Durchlaufs**. `break` beendet die ganze Schleife, `continue` nur eine Runde. Probier es einmal in `uebung.py` aus — und bau es dann **nicht** in dein Spiel ein. Deine Schleife braucht es nicht, und eine Schleife mit `continue` ist schwerer zu lesen als eine mit einer sauberen Bedingung.

```python
for _ in range(3):
    print("Ping")
```

Ein Unterstrich statt eines Namens sagt: *Ich brauche die Zählnummer nicht.* Eine Verabredung unter Python-Programmierern, keine Regel. **Du musst es lesen können, nicht schreiben.**

## Dein Auftrag — 3a

Nach jedem Schritt: **vorhersagen, ausführen, vergleichen.**

**0. Räum auf, bevor du anfängst.**

Dein Programm aus Etappe 2 läuft einmal von oben nach unten. Zwei Dinge daran musst du heute einordnen, sonst verwirren sie dich den ganzen Abend:

- **Der einzelne Schuss am Ende** — die `if`-Bedingung mit `and`, die genau einmal feuert. Sie wandert in 3c als Befehl `feuern` in die Schleife. **Kommentier sie vorerst aus, statt sie zu löschen** — du willst sie dort wieder ansehen.
- **Die Erzählung davor** — Klassenwahl, Briefing, Funkspruch. Die bleibt, wo sie ist: **vor** der Schleife, damit sie genau einmal läuft.

**Und eine Entscheidung, die jetzt fällig ist:** In Etappe 2 hast du `trefferpunkte` (dein Marine) und `kern_integritaet` (die Anlage) getrennt. Heute brauchst du eine Abbruchbedingung für das Spiel — **und das ist die Kernintegrität, nicht dein Marine.** Die Gegner greifen die Anlage an. Dass dein Marine ausfallen kann, ohne dass das Spiel vorbei ist, wird erst in Etappe 13 zum Thema.

Falls bei dir beides noch dieselbe Variable ist: Trenn sie jetzt. Später sind es zehn Stellen statt zwei.

**1. Bau die äußere Schleife.** Schreib eine `for`-Schleife, die für jede der zwanzig Wellen eine Zeile ausgibt:

```
--- Welle 1 von 20 ---
```

Benutz dafür `wellen_bis_evakuierung` aus Etappe 1. Finde selbst heraus, welche `range()`-Form genau die Zahlen 1 bis 20 liefert — Konzept 2 hat die Tabelle dazu.

**2. Bau die innere Schleife.** Schreib eine `while`-Schleife **innerhalb** der äußeren. Sie soll eine Eingabe abfragen und laufen, solange die Welle nicht vorbei ist.

Implementiere zunächst nur den Befehl `beenden` — er beendet die Welle. Jede andere Eingabe soll eine Meldung ausgeben und erneut fragen. Die übrigen Befehle kommen in 3b.

*(Damit ist die Schuld aus Etappe 1 und 2 eingelöst: Eine ungültige Eingabe beendet das Programm nicht mehr.)*

**3. Lass die Welle von selbst enden.** Leg eine Variable für die Gegnerzahl an — **auf Ebene 2 aus Konzept 5**, also innerhalb der `for`-Schleife und vor der `while`-Schleife. Heute reicht eine feste Zahl wie 3.

Beende die innere Schleife mit `break`, sobald sie auf 0 steht.

**Zum Prüfen:** Gib die Gegnerzahl zu Wellenbeginn aus. Bei jeder Welle muss dieselbe Zahl erscheinen. Steht dort beim zweiten Mal eine 0 oder ein Rest, liegt die Variable auf der falschen Ebene.

**Zum Testen brauchst du außerdem einen Weg, Gegner loszuwerden, bevor `feuern` existiert.** Bau einen Befehl `test`, der die Gegnerzahl um 1 senkt.

Solche Entwicklerbefehle sind erlaubt und nützlich — **und sie müssen am Ende wieder raus.** Schreib gleich beim Bauen einen Kommentar dazu (`# Entwicklerbefehl, raus am Ende von 3c`). In 3c gibt es einen eigenen Schritt dafür.

**4. Prüf, ob Etappe 2 noch funktioniert.** Führ das Programm aus und zähl mit, wie oft Klassenwahl und Lagebriefing erscheinen. Es muss genau einmal sein. Wenn sie in jeder Welle kommen, verschieb sie **vor** die `for`-Zeile.

**5. Bau absichtlich eine Endlosschleife.** Entfern die Zeile, die deine `while`-Bedingung verändert, führ aus und brich mit `Strg + C` ab. Danach zurückbauen.

Du sollst den Notausgang einmal benutzt haben, bevor du ihn brauchst.

**6. ⭐ Knobelstelle: beende das Spiel von innen heraus.**

Sorge dafür, dass das Spiel endet, wenn `kern_integritaet` auf 0 oder darunter fällt — **auch mitten in Welle 7**.

Zum Testen: Setz `kern_integritaet = 5` und lass sie in jeder Runde um 2 sinken.

Du weißt aus Konzept 6, dass `break` nur die innere Schleife verlässt. Die äußere läuft weiter, und Welle 8 beginnt trotzdem.

> **Finde selbst einen Weg, das Ende auch der äußeren Schleife mitzuteilen.** Es gibt mehrere Lösungen, und alle benutzen nur Dinge, die du schon kennst. Du musst heute nicht wissen, welche davon später die sauberste ist.

**Wenn du hier hängst, hast du nichts falsch verstanden.** Das ist die erste Stelle in diesem Tutorial, an der du ein Problem lösen sollst, für das dir niemand das Verfahren gezeigt hat — nur die Bausteine. Nimm dir Zeit. Wenn es nach zwanzig Minuten nicht klappt, frag deinen Mentor nach einem *Hinweis*, nicht nach der Lösung.

**Und wenn du fragst, frag in dieser Form — vier Zeilen:**

```
Was ich will:            Das Spiel soll enden, wenn die Kernintegrität 0 erreicht.
Was passiert:            Die Welle endet, aber die nächste beginnt trotzdem.
Was ich ausgeschlossen habe:  Die Bedingung stimmt — ich habe sie mit print geprüft.
Was ich vermute:         Das break beendet nur die innere Schleife.
```

**Der Nutzen ist nicht, dass man dir besser helfen kann.** Es ist die dritte Zeile: Beim Schreiben merkst du oft, dass du noch gar nichts ausgeschlossen hast — und gehst es prüfen, statt zu fragen. Ein erschreckender Anteil aller Fehler löst sich beim Beschreiben.

*(Das hat einen Namen: **Rubber-Duck-Debugging**. Man erklärt das Problem laut einer Gummiente. Klingt albern, funktioniert, weil Erklären dich zwingt, Lücken zu benennen, über die du beim Denken hinweggerutscht bist. In Etappe 8 wird daraus ein eigener Abschnitt.)*

**7. Committen.**

```
git add .
git commit -m "Etappe 3a: Die Wellenschleife läuft"
```

## Selbsttest — 3a

- [ ] Das Spiel läuft zwanzig Wellen durch, wenn du nichts tust, um es zu beenden
- [ ] Innerhalb einer Welle kannst du beliebig viele Eingaben machen
- [ ] Eine unbekannte Eingabe beendet nichts — es kommt eine Meldung und die nächste Frage
- [ ] Klassenwahl und Lagebriefing erscheinen **einmal**, nicht pro Welle
- [ ] Eine Welle endet von selbst, wenn kein Gegner mehr steht
- [ ] Bei `kern_integritaet = 0` endet das **ganze** Spiel, auch mitten in einer Welle
- [ ] `Strg + C` bricht dein Programm ab, ohne dass du das Terminal schließen musst

---

# Portion 3b — Die Befehle

## Die Konzepte

### 8. `.lower()` — jetzt wird sie gebraucht

In Etappe 2 hast du `.strip()` gelernt, und `.lower()` wurde vertagt, weil du Zahlen eingegeben hast. Ab jetzt tippt der Spieler Wörter:

```python
eingabe = input("> ").strip().lower()
```

Für Python sind `Status`, `STATUS` und `status` drei verschiedene Texte. `.lower()` macht alles klein, sodass du nur eine Schreibweise vergleichen musst.

**Beide Methoden hintereinander** — das geht, weil `.strip()` einen Text zurückgibt, auf dem man wieder eine Textmethode aufrufen kann. Lies von links nach rechts: *nimm die Eingabe, entferne Leerzeichen, mach das Ergebnis klein.*

Und die Falle aus Etappe 2 gilt weiter: Beide **geben etwas zurück**, sie verändern nichts. Ohne `eingabe =` davor passiert nichts.

### 9. Die Befehlskette — und warum sie hässlich sein darf

Innerhalb der Runden-Schleife fragst du, was der Spieler tun will, und verzweigst mit `if`/`elif`/`else` — dieselbe Kette wie in Etappe 2, nur mit Befehlen statt Klassennummern. Der `else`-Zweig fängt Unbekanntes ab.

**Diese Kette wächst.** In Etappe 4 kommt Aufsammeln dazu, in Etappe 5 Kaufen und Bewegen, in Etappe 13 Bauen. Irgendwann sind es zwölf Zweige.

**Das ist eingeplant.** In Etappe 7a wandert sie in eine eigene Funktion, in Etappe 23a stirbt sie durch ein Befehls-Dictionary. Schreib in `GELERNT.md`: *„Die Befehlskette wächst. Termin: Etappe 7a und 23a."* Dann ist es ein Termin und kein Mangel.

### 10. Welcher Befehl kostet Zeit?

**Eine Frage, die dein Spiel entscheidet, und sie fällt einem erst beim Spielen auf.**

Wenn dein Rundenzähler am Ende jedes Schleifendurchlaufs hochzählt, kostet **jeder** Befehl eine Runde. Auch `status`. Der Spieler schaut auf seine Munition — und die Gegner rücken auf.

Das ist fast immer nicht gewollt. Nachschauen ist keine Handlung.

**Also teil deine Befehle in zwei Sorten:**

| Sorte | Beispiele | Wirkung |
|---|---|---|
| **Kosten eine Runde** | feuern, nachladen | Zeit vergeht, Gegner handeln |
| **Kosten nichts** | status, später: Karte, Inventar, Hilfe | Reine Auskunft |

Technisch ist das ein `if` — der Zähler wird nicht mehr bedingungslos erhöht, sondern nur bei Befehlen der ersten Sorte. Du brauchst dafür kein neues Werkzeug.

**Und das ist mehr als eine Bequemlichkeit für den Spieler.** Erst wenn Nachschauen kostenlos ist, wird „nachladen kostet eine Runde" zu einer echten Entscheidung. Wenn ohnehin alles Zeit kostet, kostet nichts wirklich etwas.

*(In Etappe 12 kommt genau diese Frage wieder, dann unter anderem Namen: Welche Spieleraktion löst einen Tick aus? Deine heutige Antwort ist die erste Fassung davon.)*

### 11. 👀 Zwei Bauformen für Schleifen — welche hast du gebaut?

**Erst weiterlesen, wenn die Knobelstelle aus 3a gelöst ist.** Hier bekommt das, was du dort selbst gefunden hast, seinen Namen.

Es gibt zwei verbreitete Formen, eine Schleife zu beenden. Beide sind richtig, du solltest beide erkennen:

```python
# Variante A — mit einer Zustandsvariablen
laeuft = True
while laeuft:
    befehl = input("> ")
    if befehl == "beenden":
        laeuft = False

# Variante B — mit break
while True:
    befehl = input("> ")
    if befehl == "beenden":
        break
```

**A** liest sich selbsterklärend — die Bedingung oben sagt, worum es geht — und die Variable lässt sich von überall setzen, auch aus einer inneren Schleife heraus. **B** ist kürzer und macht den Ausstieg an genau einer Stelle sichtbar.

**Welche hast du in 3a gebaut?** Wenn du für den Abbruch von innen nach außen eine Variable angelegt hast, war es A. Wenn du es anders gelöst hast, ist das auch in Ordnung — sag nur, wie.

*(Für dieses Projekt passt A etwas besser, weil eine Zustandsvariable genau das Muster ist, das ab Etappe 12 dein ganzes Spiel trägt. Bau deswegen aber nichts um, was funktioniert.)*

### 12. Der Rundenzähler — die Entscheidung aus Konzept 5

Du brauchst einen Zähler für die Runden. Eine Zeile beim Anlegen, eine zum Hochzählen. Trivial — bis auf die Frage, die du aus Konzept 5 schon kennst: **wo legst du ihn an?**

```python
# Variante A — Ebene 2
for durchgang in range(3):
    schritt = 1
    while ...:
        schritt += 1

# Variante B — Ebene 1
schritt = 1
for durchgang in range(3):
    while ...:
        schritt += 1
```

**Sag vorher, was bei Durchgang 3 jeweils in `schritt` steht.** Dann bau beide Varianten und sieh nach.

Beide laufen. Keine erzeugt eine Fehlermeldung. **Nur eine ist das, was du wolltest** — und welche das ist, hängt davon ab, was du meinst: „Runde 3 dieser Welle" oder „insgesamt 40 Runden gespielt".

*(Und du kannst beides haben: einen Zähler pro Welle und einen fürs ganze Spiel. Zwei Variablen an zwei Stellen sind keine Verschwendung, sondern zwei verschiedene Fragen.)*

## Dein Auftrag — 3b

**8. Räum die Eingabe auf.** Häng `.strip().lower()` an dein `input()` und weis das Ergebnis einer Variablen zu.

Führ aus und tippe ` BEENDEN ` — mit Leerzeichen davor und dahinter, in Großbuchstaben. Es muss funktionieren.

**9. Bau die Befehlskette.** Erweiter deine Eingabeverarbeitung zu einer `if`/`elif`/`else`-Kette mit vier Befehlen:

| Befehl | Was er heute tut | Kostet eine Runde? |
|---|---|---|
| `status` | Gibt Kernintegrität, Munition und Schrott aus — die Zahlen, die du seit Etappe 1 hast | **nein** |
| `feuern` | Gibt vorerst nur eine Meldung aus | ja |
| `nachladen` | Gibt vorerst nur eine Meldung aus | ja |
| `beenden` | Beendet die Welle (hast du in 3a gebaut) | — |
| alles andere | `else`-Zweig: Meldung, dass der Befehl unbekannt ist | nein |

Die Wirkung von `feuern` und `nachladen` kommt in 3c. Heute geht es nur darum, dass die Kette steht.

Wirf den `test`-Befehl aus Schritt 3 noch nicht weg — du brauchst ihn, bis `feuern` in 3c echte Wirkung hat.

**10. Bau den Rundenzähler.** Leg eine Variable `runde` an und erhöh sie um 1 — aber **nur bei Befehlen, die eine Runde kosten** (siehe Tabelle in Schritt 9 und Konzept 10).

Zum Prüfen: Ruf zehnmal hintereinander `status` auf. Die Rundenzahl muss dabei stehen bleiben.

**Entscheide außerdem bewusst, ob du `runde` innerhalb oder außerhalb der Wellenschleife anlegst.** Schreib beide Entscheidungen mit Begründung in `GELERNT.md`.

**11. Probier die andere Variante aus.** Verschieb die Zeile `runde = 1` an die jeweils andere Stelle, spiel bis Welle 3 und lies den Rundenzähler ab. Vergleich mit deiner Vorhersage aus Konzept 12.

Danach zurück auf die Variante, die du haben willst.

**12. Zeig Welle und Runde an.** Bau beide Werte in deine Eingabeaufforderung ein, damit du beim Spielen siehst, wo du bist. Zwei Variablen in einem f-String — das kannst du seit Etappe 1.

**13. Committen.**

```
git add .
git commit -m "Etappe 3b: Befehle und Runden"
```

## Selbsttest — 3b

- [ ] ` FEUERN ` mit Leerzeichen und in Großbuchstaben wird erkannt
- [ ] Alle vier Befehle tun etwas Sichtbares, unbekannte Eingaben erzeugen eine Meldung
- [ ] Zehnmal `status` hintereinander lässt den Rundenzähler unverändert
- [ ] Die Eingabeaufforderung zeigt Welle und Runde
- [ ] Du kannst zeigen, in welcher Zeile dein Rundenzähler angelegt wird, und begründen warum
- [ ] Du hast die andere Variante ausprobiert und kannst den Unterschied benennen

---

# Portion 3c — Kampf und Anzeige

## Die Konzepte

### 13. Kampf, absichtlich primitiv

Ein Schuss trifft. Fester Schaden. Munition sinkt. Fertig.

Keine Trefferchance, keine Panzerung, keine kritischen Treffer. **Das ist kein Provisorium aus Faulheit, sondern Terminplanung:** Die richtige Formel ist Etappe 21a und braucht Werkzeuge, die du noch nicht hast.

**Ehrlich eingeordnet:** Was du heute baust, trägt bis Etappe 21 und ist nicht endgültig. Ein Spiel, das mit einer schlechten Formel läuft, ist unendlich viel mehr wert als eine gute Formel ohne Spiel.

**Zur Gegneranzahl entscheidest du selbst.** Sie soll mit der Wellennummer wachsen — Welle 1 hat mindestens einen, spätere haben mehr. Wie genau, ist deine Sache; eine einfache Rechnung mit der Schleifenvariable genügt vollkommen. Probier zwei Varianten aus und schau, welche sich beim Spielen besser anfühlt.

⚠️ **Hier lauert die Balancing-Falle aus dem Lehrplan zum ersten Mal.** Sobald das läuft, willst du an den Zahlen drehen. Es fühlt sich nach Arbeit an und ist keine.

> **Setz dir fünfzehn Minuten. Eine langweilige Welle, die läuft, schlägt eine spannende, die abstürzt.**

Was sich falsch anfühlt, wird **notiert statt geändert**. Die Liste ist deine Grundlage für Etappe 21a.

### 14. Die Balken

Dein `status`-Befehl zeigt Zahlen. Ab heute zusätzlich einen Balken:

```
Kern     [#######···] 70%
Munition [####······] 40%
```

**Das sieht nach mehr aus, als es ist.** Ein Balken ist ein Text aus zwei Teilen: ein paar volle Zeichen, ein paar leere.

**Das Werkzeug — Text mal Zahl:**

```python
print("#" * 7)             # #######
print("#" * 7 + "·" * 3)   # #######···
```

Ein Text mal einer Zahl ergibt den Text so oft hintereinander. Zwei Texte mit `+` ergeben einen längeren. Mehr Technik steckt nicht dahinter.

*(Ist dir `·` unbequem zu tippen? Nimm `-`, `.` oder ein Leerzeichen.)*

⚠️ **Bevor du rechnest, die wichtigste Frage: Wann wird gerechnet?**

Es ist verlockend, die Balkenlänge einmal oben bei den anderen Variablen auszurechnen. **Das funktioniert nicht** — und es stürzt auch nicht ab. Es zeigt einfach für immer denselben Balken, egal was mit der Kernintegrität passiert.

Der Grund steht in Konzept 5: Eine Zeile ganz oben läuft **einmal**. Sie rechnet mit dem Wert vom Programmstart und danach nie wieder.

> **Die Balkenlänge ist nichts, was man speichert. Sie wird jedes Mal neu ausgerechnet, wenn der Balken angezeigt wird.**

Die Rechnung gehört also dorthin, wo `status` ausgeführt wird. Merk dir die Form: **Was aus Zustand entsteht, wird beim Anzeigen erzeugt, nicht aufbewahrt.** In Etappe 4 gilt dasselbe für die Anmarschbahn, in Etappe 7b bekommt der Gedanke seinen Platz im Code.

**Und jetzt die Rechnung — die machst du selbst.** Sie hat drei Schritte, und du kennst jedes einzelne Werkzeug dafür:

1. **Wie voll ist es?** Eine Zahl zwischen 0 und 1. Bei einem Kaffeetank, der 500 ml fasst und 350 ml enthält, wäre das `350 / 500`. **Welche beiden Zahlen sind das bei deiner Kernintegrität?**
2. **Wie viele Zeichen sind voll?** Der Balken soll zehn Zeichen breit sein. Welche Rechnung macht aus einem Anteil eine Anzahl?
3. **Wie viele sind leer?** Der Rest.

Bau das **zuerst in `uebung.py`** mit festen Zahlen, nicht im Spiel.

⚠️ **Ein Hinweis, damit du an der richtigen Stelle stutzt:** Bei Schritt 2 bekommst du eine Kommazahl heraus, und `"#" * 7.0` funktioniert nicht — Python kann einen Text nicht siebenkommanull-mal wiederholen. Die Fehlermeldung sagt dir das auch.

Es gibt **zwei** Werkzeuge, die aus einer Kommazahl eine Ganzzahl machen, und sie tun nicht dasselbe. Eines kennst du aus Etappe 1, Abschnitt 8; das andere rundet kaufmännisch. Probier beide mit `7.6` und mit `9.9` aus und entscheide dich bewusst.

*(Die Entscheidungsfrage: Was soll dein Balken bei 99 % zeigen — zehn volle Zeichen oder neun? Beides ist vertretbar. Nur nicht beides gleichzeitig an verschiedenen Stellen.)*

**Die Prozentzahl daneben** — hier zahlt der optionale Vorgeschmack aus Etappe 1:

```python
anteil = 0.7
print(f"{anteil:.0%}")     # 70%
```

Der Doppelpunkt im f-String leitet eine Formatanweisung ein. `.0%` heißt: *als Prozent, ohne Nachkommastellen*. Das erspart dir die Multiplikation mit 100 — und die Sorge, ob dabei `70.00000000000001` herauskommt. Wichtig: `anteil` muss die Zahl zwischen 0 und 1 sein, nicht die bereits ausgerechneten 70.

👀 **Mehr Formatierung brauchst du heute nicht.** Es gibt viel davon (`:.2f`, `:>8`, `:,`), und du wirst sie in fremdem Code sehen. Ein Satz reicht: *nach dem Doppelpunkt steht, wie der Wert aussehen soll.*

### 15. Warum der Balken kein Schmuck ist

Ein Balken bei 110 Prozent läuft aus dem Rahmen. Ein Balken bei minus 20 sieht unmöglich aus.

**Beides fällt dir sofort auf. In einer Zahlenkolonne hättest du es überlesen.**

Deine Anzeige ist ab heute ein Messgerät. Das ist der Anfang des Fadens, der im Lehrplan **Beobachtbarkeit** heißt: die Frage *woher weißt du, dass dein Programm das Richtige tut?* Die Antwort ist nie „es läuft", sondern immer „welche Beobachtung beweist es?".

**Und ausdrücklich:** Dass dein Balken bei 150 % über den Rahmen hinausläuft, ist **kein Fehler, den du heute beheben sollst.** Die Versuchung, ihn zu begrenzen, ist groß und führt zu Werkzeugen, die hier nichts verloren haben. Der Balken soll ungültige Werte *zeigen*, nicht verstecken. Genau darin liegt sein Wert.

*(Es gilt die Zehn-Minuten-Regel. Der Balken ist fertig, wenn man ihn lesen kann — nicht, wenn er hübsch ist. In Etappe 7b wandert er in eine eigene Zeichenfunktion.)*

## Dein Auftrag — 3c

**14. Lass die Gegnerzahl mit der Welle wachsen.** Ersetz die feste Zahl aus Schritt 3 durch eine Rechnung, die die Wellennummer benutzt.

**Die Formel wählst du selbst.** Bedingung: Welle 1 hat mindestens einen Gegner, spätere Wellen haben mehr. Probier zwei Varianten aus und behalte die, die sich beim Spielen besser anfühlt.

**15. Gib `feuern` Wirkung.** Hol dir die auskommentierte Feuerbedingung aus Schritt 0 zurück und bau sie in die Befehlskette ein. Der Befehl soll `munition` um 1 senken und die Gegnerzahl um 1 senken. Ist keine Munition da, kommt eine Meldung und **kein** Schuss.

Die Bedingung dafür schreibst du wie in Etappe 2 — eine Prüfung vor der Aktion. Danach kannst du den `test`-Befehl aus Schritt 3 löschen.

**16. Gib `nachladen` Wirkung.** Der Befehl soll `munition` auf den Startwert 40 zurücksetzen — und dabei eine Runde kosten, wie in Schritt 10 festgelegt.

**Und hier fällt eine Schuld aus Etappe 2 an:** Dort hast du `nachladen_noetig` angelegt, und es stand nie auf `True`. Setz es jetzt, sobald die Munition auf 0 fällt, und beim Nachladen zurück auf `False`. Deine Feuerbedingung aus Etappe 2 prüft es bereits — sie funktioniert ab heute zum ersten Mal vollständig.

*(Wenn dir das doppelt vorkommt — `munition > 0` **und** `nachladen_noetig` —, hast du recht. Zwei Werte, die dasselbe sagen, sind eine Fehlerquelle: Vergisst du einmal, den Boolean mitzusetzen, widersprechen sie sich. Notier die Beobachtung in `GELERNT.md`; in Etappe 18 ist genau das ein eigenes Thema.)*

**Genau hier zahlt sich die Unterscheidung aus Konzept 10 aus:** Weil `status` nichts kostet und `nachladen` schon, steht der Spieler zum ersten Mal vor einer echten Wahl.

**17. Lass die Gegner zurückschlagen.** Senk `kern_integritaet` um einen festen Wert, solange noch Gegner stehen.

⚠️ **Und hier passiert der häufigste Fehler dieser ganzen Etappe.** Die naheliegende Stelle für diese Zeile ist das Ende des Schleifenkörpers — unterhalb der ganzen `if`/`elif`-Kette, auf Höhe der `while`-Schleife eingerückt. Dort läuft sie bei **jedem** Durchlauf.

Auch bei `status`. Der Spieler schaut auf seine Munition und bezahlt mit Kernintegrität.

> **Der Schaden gehört genau dorthin, wo auch der Rundenzähler hochzählt** — an dieselbe Bedingung gebunden, nicht ans Ende des Blocks.

**Zum Prüfen:** Ruf zehnmal hintereinander `status` auf. Kernintegrität **und** Rundenzähler müssen danach unverändert sein. Stimmt nur eines von beidem, steht die Zeile falsch.

Kein Absturz, keine Fehlermeldung — nur ein Spiel, das den Spieler fürs Hinsehen bestraft.

**Ab jetzt ist es ein Spiel, das man verlieren kann.** Prüf, ob dein Abbruch aus Schritt 6 auch wirklich greift.

**18. Spiel drei volle Wellen.** Nicht testen — spielen. Schreib auf, was sich falsch anfühlt: zu leicht, zu schnell vorbei, zu wenig Munition.

**Nur notieren, nichts ändern.** Die Liste ist deine Grundlage für Etappe 21a.

**19. Bau die Balken — zehn Minuten, Wecker stellen.**

Arbeite in dieser Reihenfolge:

1. **Zuerst in `uebung.py`**, mit festen Zahlen statt Variablen. Die drei Rechenschritte stehen als Fragen in Konzept 14.
   *(Und beachte den Warnkasten dort: Die Rechnung gehört später **in** den `status`-Befehl, nicht an den Programmanfang.)*
2. **Prüf ihn mit drei Werten:** voll, halb, leer. Sieht er bei allen dreien richtig aus?
3. **Dann ins Spiel übernehmen**, in den `status`-Befehl. Zweimal: für Kernintegrität (Obergrenze 100) und Munition (Obergrenze 40).
4. **Den ASCII-Kopf aus Etappe 1 nicht anfassen.** Die Balken gehören zum Status.

**20. Der Test, der zeigt, wofür der Balken da ist.** Setz `kern_integritaet = 150`, ruf `status` auf und sieh dir den Balken an. Dann dasselbe mit `-20`.

Beides sind Werte, die dein Spiel nie erzeugen sollte. Wenn dein Balken sie auffällig falsch darstellt, hast du ab heute eine Anzeige, die dich warnt. **Reparier ihn nicht** — siehe Konzept 15.

**21. Räum auf, bevor du committest.**

Drei Sorten Zeilen sollen jetzt raus oder markiert sein:

- **Entwicklerbefehle** — `test` und alles, was du sonst zum Testen gebaut hast. Ihre Arbeit ist getan, `feuern` macht das jetzt.
- **Debugzeilen** — alles mit `###`.
- **Toter Code aus Etappe 2** — der auskommentierte Einzelschuss aus Schritt 0, falls er noch dasteht.

**Das ist kein Ordnungsfimmel.** Ein Entwicklerbefehl, der versehentlich stehen bleibt, ist in Etappe 8 ein Verdächtiger bei jeder Fehlersuche — und du wirst dich in vier Wochen nicht erinnern, wofür er da war.

*(Das größere Aufräumen — Funktionen, doppelten Code zusammenfassen — ist Etappe 7a. Heute geht es nur um Zeilen, die nichts mehr tun.)*

**22. Committen und spielen.**

```
git add .
git commit -m "Etappe 3c: Der Vorposten hält"
git push
```

Danach: einmal von vorne durchspielen, zwanzig Wellen, ohne zu debuggen. Das ist kein Test — das ist der Moment, für den die letzten drei Wochen waren.

## Selbsttest — 3c

- [ ] Feuern senkt Munition und Gegnerzahl, bei leerer Munition kommt eine Meldung
- [ ] Nachladen kostet eine Runde, in der die Gegner Schaden machen
- [ ] Zehnmal `status` hintereinander kostet **keine** Kernintegrität und **keine** Runde
- [ ] Der Balken verändert sich, wenn die Kernintegrität sinkt — er zeigt nicht dauerhaft den Startwert
- [ ] Nach dem Aufräumen gibt es keinen `test`-Befehl mehr und keine `###`-Zeilen
- [ ] Du kannst das Spiel verlieren — und es endet dann tatsächlich
- [ ] Spätere Wellen haben mehr Gegner als frühe
- [ ] Beide Balken sehen bei vollem, halbem und leerem Stand richtig aus
- [ ] Der Balken bei `kern_integritaet = 150` sieht auffällig falsch aus — und du kannst sagen, warum

---

## Was NICHT in diese Etappe gehört

- ❌ **Eine Liste für die Gegner** → Etappe 4. Heute ist es eine Zahl.
- ❌ **Zweiteilige Befehle zerlegen** → Etappe 4
- ❌ **Gegner mit eigenen Trefferpunkten und Positionen** → Etappe 9 und 14
- ❌ **Trefferchance, Panzerung, kritische Treffer** → Etappe 21a
- ❌ **Zufällige Wellenzusammensetzung** → Etappe 17a
- ❌ **Funktionen, damit die Befehlskette kürzer wird** → Etappe 7a
- ❌ **Den Balken bei Werten über 100 % begrenzen** → gar nicht; er soll warnen
- ❌ **`try`/`except` für merkwürdige Eingaben** → Etappe 20
- ❌ **Speichern beim Beenden** → Etappe 19

**Der verlockendste Punkt ist der erste, und er wird dir in 3c begegnen.**

Irgendwann denkst du: *Eine Zahl als Gegneranzahl ist albern. Die Gegner müssten einzeln existieren — mit eigenen Trefferpunkten, damit man sie einzeln abschießen kann.*

**Der Gedanke ist völlig richtig, und genau das ist Etappe 4.** Dort wird aus der Zahl eine Liste, und du machst dabei einen der berühmtesten Anfängerfehler — an einer Stelle, wo er dich zehn Minuten kostet statt eines Abends.

Warum nicht heute: Du lernst gerade Schleifen. Eine Schleife über eine Zahl ist einfach zu überblicken. Eine Schleife über eine Liste, aus der Elemente verschwinden, ist es nicht. Wer beides gleichzeitig angeht, kann hinterher weder das eine noch das andere sicher.

**Ein Satz in `GELERNT.md`:** *„Gegner sind heute eine Zahl. Ab Etappe 4 eine Liste."*

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten.

1. Wann nimmst du `for`, wann `while`? Nenn je ein Beispiel aus deinem eigenen Spiel.
2. Welche Zahlen ergibt `range(5)`? Und `range(1, 21)`?
3. Was ist der Unterschied zwischen `break` und `continue`?
4. Wenn ein `break` in der inneren von zwei Schleifen steht — was genau wird beendet, und was läuft weiter?
5. Wie entsteht eine Endlosschleife, und wie kommst du wieder heraus?
6. **Was passiert mit deinem Rundenzähler, wenn er innerhalb statt außerhalb der Wellenschleife angelegt wird?**
7. Was bewirkt `"#" * 7`, und warum funktioniert `"#" * 7.0` nicht?
8. Warum brauchst du jetzt `.lower()`, obwohl Etappe 2 ohne auskam?
9. Welche deiner Befehle kosten eine Runde und welche nicht — und was wäre kaputt, wenn alle eine kosten würden?

**Frage 6 ist die wichtigste.** Sie sieht nach einer Detailfrage aus und ist der Kern dieser Etappe: Beide Varianten laufen fehlerfrei, nur eine tut das Richtige. Wer sie beantworten kann, hat verstanden, dass die *Position* von Code eine Entscheidung ist — und ist auf Etappe 7a und 12 vorbereitet.

**Frage 1 ist die zweitwichtigste**, weil sie die einzige ist, bei der man mit „ist doch egal" danebenliegt.

---

## Transferaufgabe (10 Minuten)

**Außerhalb des Spiels**, in `uebung.py`.

**Teil 1 — Zahlenraten.** Das Programm hat eine Zahl zwischen 1 und 100 (schreib sie heute fest hin — `random` ist Etappe 17a). Der Spieler rät, bis er sie hat. Nach jedem Versuch: „zu hoch" oder „zu niedrig". Zähl die Versuche mit.

Beantworte danach: **Warum ist das ein `while` und kein `for`?**

**Teil 2 — Zwei Wege zum selben Ergebnis.** Gib alle geraden Zahlen von 0 bis 20 aus. Einmal mit der Schrittweite von `range()`, einmal mit einer Bedingung im Schleifenkörper.

Beide funktionieren. Schreib in einem Satz auf, welche Variante du beim Lesen fremden Codes lieber sehen würdest — und warum.

*(Das ist keine Fleißaufgabe. „Es funktioniert" gegen „es liest sich gut" ist der Unterschied, um den es ab Etappe 23 die ganze Zeit geht.)*

---

## Kaputtmachen

**Erst aufschreiben, was du erwartest. Dann ausführen.** Dasselbe Ritual wie beim Bauen — nur dass du diesmal absichtlich etwas zerstörst.

1. **Entfern die Zeile, die deine `while`-Bedingung verändert.** Wie brichst du ab?
2. **Entfern das `break` am Wellenende.** Was passiert, wenn keine Gegner mehr da sind?
3. **Verschieb das `input()` aus der inneren Schleife heraus**, direkt darüber. Beobachte genau, was das Programm mit deiner Eingabe macht.
4. **Setz den Rundenzähler an die andere Stelle.** Spiel bis Welle 3 und lies ab.
5. **Rück eine Zeile aus der inneren Schleife um vier Leerzeichen nach links.** Läuft es? Was passiert jetzt wann?
6. **Setz `kern_integritaet = 150`** und lass dir den Balken anzeigen.

**Die eigentlichen sind 3, 4 und 5** — alle drei laufen ohne eine einzige Fehlermeldung durch und tun das Falsche:

- **3** fragt einmal und wiederholt dann ewig dieselbe Eingabe. Das Programm sieht beschäftigt aus und reagiert nicht mehr auf dich.
- **4** liefert bei Welle 3 eine völlig andere Rundenzahl — und keine der beiden ist „ein Fehler", eine ist nur nicht das, was du wolltest.
- **5** verschiebt eine Zeile zwischen den Ebenen. Vielleicht werden deine Gegner nur einmal pro Welle statt pro Runde gezählt, und du merkst es erst, wenn die Zahlen nicht aufgehen.

Alle drei in `GELERNT.md`, mit einem Satz dazu: **woran du sie erkannt hättest.**

*(Das Muster **bauen → kaputtmachen → beobachten → erklären** wiederholt sich in jeder Etappe dieses Tutorials. Es ist kein Spaßelement: „So schreibt man es" ist Auswendiglernen, „warum muss es so sein" ist Verstehen — und der verlässliche Weg dorthin führt über die Fehlermeldung.)*

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| Programm reagiert nicht mehr, Cursor blinkt | Endlosschleife | `Strg + C`, dann: was verändert die Bedingung? |
| `IndentationError: unexpected indent` | Zeile eine Ebene zu weit rechts | Genannte Zeile, vier Leerzeichen zurück |
| `SyntaxError: expected ':'` | Doppelpunkt nach `while` oder `for` vergessen | Genannte Zeile |
| Lagebriefing erscheint in jeder Welle | Steht innerhalb der Schleife | Alles vor die `for`-Zeile ziehen |
| Schleife läuft 20-mal statt 21 (oder umgekehrt) | Off-by-One in `range()` | Zweite Zahl ist ausgeschlossen |
| Nach dem Wellenende läuft die nächste trotzdem | `break` beendet nur die innere Schleife | Knobelstelle, Auftragsschritt 6 |
| Immer dieselbe Eingabe wird verarbeitet | `input()` steht außerhalb der Schleife | Ins Innere der `while`-Schleife |
| `NameError: name 'runde' is not defined` | Variable erst in der Schleife angelegt, außerhalb gelesen | Konzept 5 |
| `TypeError: can't multiply sequence by non-int of type 'float'` | `"#" * 7.0` — die Anzahl ist eine Kommazahl | Etappe 1, Abschnitt 8 |
| Balken ist immer leer | Ganzzahldivision `//` statt `/` | Die Anteilsrechnung |
| **Balken zeigt immer denselben Stand** | Die Länge wird einmal oben berechnet statt beim Anzeigen | Konzept 14, Warnkasten — die Rechnung gehört in `status` |
| Kernintegrität sinkt auch bei `status` | Die Schadenszeile steht am Ende des Schleifenkörpers statt in den zeitkostenden Zweigen | Auftragsschritt 17 |
| Prozentzahl zeigt `7000%` | `anteil` war schon mit 100 multipliziert | `:.0%` erwartet die Zahl zwischen 0 und 1 |
| Munition wird negativ | Vor dem Feuern nicht geprüft | Die Bedingung aus Etappe 2 |

**Dein Debugging-Reflex für diese Etappe:**

> **Wie oft läuft das hier eigentlich?**

In Etappe 1 hast du gefragt: *welchen Typ hat dieser Wert?* In Etappe 2: *welcher Zweig läuft gerade?* Heute kommt die dritte Frage dazu — und sie ist die, die bei Schleifenfehlern fast immer trifft.

Das Werkzeug ist dasselbe wie in Etappe 2: eine `print()`-Zeile am Anfang jedes Durchlaufs, die Welle, Runde und Gegnerzahl ausgibt. Sie beantwortet auf einen Blick, ob es zu oft, zu selten oder mit den falschen Werten läuft. **Nachsehen schlägt Vermuten** — der Grundsatz aus Etappe 2, eine Ebene höher.

*(Markier solche Zeilen mit `###`, dann findest du sie vor dem Commit wieder.)*

---

## Ein Blick nach vorne

**Etappe 4** macht aus deiner Gegnerzahl eine Liste. Jeder Gegner bekommt eine eigene Existenz — und du machst den Fehler, eine Liste zu verändern, während du über sie läufst. Deine Anmarschbahn entsteht dort: `S..K...K....@`, eine Zeile, in der du siehst, wie die Brut aufrückt.

**Etappe 7a** nimmt deine gewachsene Befehlskette und steckt sie in eine Funktion. Dort bekommt auch die Beobachtung aus Konzept 5 ihren Fachbegriff.

**Etappe 12** ist der Punkt, an dem deine Schleife erwachsen wird. Jeder Durchlauf löst dann einen *Tick* aus: Die Welt bewegt sich, auch wenn du nichts tust. Deine heutige Schleife ist das Gerüst dafür.

**Etappe 28** tauscht die Schleife aus, ohne den Inhalt anzufassen. Sie läuft dann 60-mal pro Sekunde statt einmal pro Eingabe.

---

## Abschluss

**In `GELERNT.md`:**

- Was neu war: `while`, `for`, `range()`, `break`, verschachtelte Schleifen
- Was gehakt hat, mit Fehlermeldung
- **Die Design-Entscheidung zur Befehlssprache** — mit dem Satz, dass Etappe 4 den Umbau erzwingt
- **Wo dein Rundenzähler steht und warum**
- **Welche Befehle bei dir eine Runde kosten** — und welche nicht
- **Wie du die Knobelstelle gelöst hast** (Auftragsschritt 6) — und was du zuerst probiert hast
- Die drei stillen Fehler aus dem Kaputtmachen, mit *woran du sie erkannt hättest*
- Deine Liste aus Auftragsschritt 14: was sich beim Spielen falsch angefühlt hat
- Der Satz: *„Gegner sind heute eine Zahl. Ab Etappe 4 eine Liste."*

Vor jedem Commit: Sind alle `###`-Debugzeilen raus?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest. Alle drei sind optional.

- **Ein Wellen-Zwischenbericht.** Nach jeder Welle eine Zeile: wie viele Runden, wie viel Munition verbraucht, Kern bei wie viel Prozent. Fünf Minuten, macht den Fortschritt spürbar.

- **Eine Bestätigungsabfrage beim Beenden.** *„Wirklich beenden? (j/n)"* — eine kleine Schleife in der Schleife. Zwingt dich, über die Ebenen nachzudenken, und festigt 3a.

- **Der Munitionsengpass als Spielgefühl.** Vierzig Schuss auf zwanzig Wellen sind zwei pro Welle. Wenn Nachladen eine Runde kostet und die Gegner in dieser Runde weiter Schaden machen, wird aus einer Zahl eine echte Entscheidung: schießen oder nachladen? **Das ist die beste Erweiterung hier**, weil sie keinen einzigen neuen Python-Begriff braucht und aus deinem Spiel zum ersten Mal eines mit einem Dilemma macht.

---

> **Nächste Etappe:** [Etappe 4 — Ausrüstung und Beute](etappe-04-ausruestung-und-beute.md) · Listen, `append()`, `remove()`, `len()`, Indexing
