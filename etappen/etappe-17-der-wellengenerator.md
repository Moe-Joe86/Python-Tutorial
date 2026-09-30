# Etappe 17 — Der Wellengenerator

*v2.2.0 · 2026-09-30*

> **Block 3: Der Vorposten reagiert** · Etappe 17 von 30 · [← Etappe 16](etappe-16-bug-jagd-ii.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 18 →](etappe-18-faehigkeiten-und-statuseffekte.md)

**Neue Syntax heute:** 17a: `import random` als erste Zeile und `random.choice(liste)` — beide aus der Kür von Etappe 4, ab heute im Auftrag · `random.randint(a, b)` · gewichtete Auswahl von Hand · Zufall prüfen durch Zählen mit `d[k] = d.get(k, 0) + 1` · `if not d:` beim Dictionary · das Budget-Muster · 🧠 `random.random()` · 🧠 Gewicht gegen Wahrscheinlichkeit, Wurfbereich und Grenze · 🧠 `ValueError: empty range` und die verdeckende `random.py` · 👀 `random.choices(..., weights=...)` — 17b: `random.seed(n)` · `SEED = None` als Schalter · 🧠 was ein Seed nicht festnagelt — Eingaben und Sets · 🧠 der Debugger liest aus derselben Eingabe wie `input()` — 17c: ein Standardargument an einer bestehenden Methode nachrüsten · einzelne `if` füllen einen Topf, eine `elif`-Kette führt das Gezogene aus · ein Zähler in Wellen statt in Takten

**Zeitaufwand:** 17a: 7–9 Sitzungen · 17b: 4–5 Sitzungen · 17c: 6–7 Sitzungen, à 20–30 Minuten, ohne die Kür in Schritt 22. Rund 95 Minuten davon sind Lesestoff — gut 40 in 17a (mit dem Anfang dieser Seite), knapp 20 in 17b und gut 30 in 17c, die Abschnitte am Ende jeweils mitgerechnet. **Lies jeweils nur die Portion, an der du sitzt.** Die Abschnitte am Ende sind nach Portionen markiert.

⚠️ **Das ist mehr als die Faustregel aus dem Lehrplan, zwei bis vier Sitzungen pro Portion, und es ist ehrlich gerechnet.** Allein Schritt 2 und Schritt 6 sind je ein Abend, der Beweislauf in Schritt 13 ebenfalls. 17a und 17c haben deshalb in der Mitte einen markierten Schnitt (⏸), an dem du guten Gewissens aufhörst.

⚠️ **17a ist die freundlichste Portion.** Zufall ist sofort sichtbar und sofort belohnend: Du startest das Spiel zweimal und siehst zwei verschiedene Wellen. **17b ist das, was der Zufall nach sich zieht** — ab dort ist dein Spiel zum ersten Mal ein Programm, dessen Fehler man nicht mehr einfach nachspielen kann, und du baust das Werkzeug, das das wieder möglich macht. **17c nutzt den Zufall, den du dann im Griff hast:** Zwischen den Wellen passiert etwas.

**Voraussetzung:** Etappe 16 abgeschlossen, Selbsttest grün. Du brauchst `GEGNERTYPEN` aus Etappe 6, die Klasse `Gegner` aus Etappe 9 und 11, die vier Marine-Klassen aus Etappe 11, den Tick und `welt.melde()` aus Etappe 12 und 13, die Fundstücke, die Fundtabelle und das Vorwissen aus Etappe 15 — **und die Tick-Reihenfolge aus Etappe 16 in `GELERNT.md`.** In 17c schreibst du eine zweite Reihenfolge daneben: die der Pause zwischen den Wellen.

**Die drei Portionen:**

| | Was passiert | Was danach anders ist |
|---|---|---|
| **17a** | Zufall, gewichtete Auswahl, ein Budget | Jede Welle ist anders und trotzdem ungefähr gleich schwer. Die `if`/`elif`-Kette aus Etappe 6 ist weg. Seltene Beute ist selten — auch der Datenkern. |
| **17b** | Ein Seed, sichtbar und bewiesen | Ein Fehler lässt sich wieder vorführen: derselbe Seed, dieselben Eingaben, derselbe Lauf. |
| **17c** | Ein Wellenbericht und Ereignisse zwischen den Wellen | Deine Kameraden melden sich zu Wort, jeder mit eigener Stimme. Und die Aufzeichnung vom ersten Tag läuft noch. |

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **17a** | `random.randint` · `random.choice` · eine eigene gewichtete Auswahl · ein Wellenbudget · erzeugte Wellen · typgebundene, gewichtete Beute | Gewicht gegen Wahrscheinlichkeit · warum ein Budget besser steuert als eine Anzahl · `random.random()` | `random.choices(..., weights=...)` |
| **17b** | `random.seed` als sichtbares Werkzeug · ein Beweislauf mit festem Seed | Zufall macht ein Programm unvorführbar — außer man fixiert ihn · was ein Seed *nicht* festnagelt | — |
| **17c** | der Wellenbericht mit Stimmen · Ereignisse zwischen den Wellen · die Reihenfolge der Pause | Sofort oder gesammelt? · welche Bedingungen einen Topf füllen und welche eine Kette brauchen | — |

---

## Ab hier: Block 3

**Mit dieser Etappe beginnt der letzte große Block, und der Ton ändert sich.**

Bis Etappe 16 hieß es meistens: *„Jetzt lernst du X. So sieht es aus. Bau es ein."* Ab hier heißt es öfter:

> **Hier ist ein Problem. Welche Lösung würdest du wählen?**

Das ist keine Nachlässigkeit, sondern der Übergang vom Programmierenlernen zur Softwareentwicklung. Bei jeder größeren Entscheidung dieses Blocks gehst du denselben Weg: **Problem beschreiben → Modelle nebeneinanderstellen → Vor- und Nachteile → entscheiden → bauen → später neu bewerten.** Heute passiert das zweimal: bei der Frage, woraus eine Welle besteht (17a), und bei der Frage, wie eine Meldung wartet, bis die Welle vorbei ist (17c).

⚠️ **Was sich nicht ändert:** Jedes Werkzeug, das ein Auftragsschritt braucht, wird weiterhin vorher erklärt. „Du entscheidest" heißt nie „such dir das Werkzeug selbst".

**Und zwei Dinge kommen ab heute dazu:**

- **Die Leseleiter steigt auf Stufe 3.** Die fünf Fragen bleiben, der fremde Code wird länger — 30 bis 60 Zeilen —, und die Leitfrage heißt jetzt: **Warum ist es so gebaut?** Die erste Übung gehört zu 17b.
- **Die Entwicklerfrage.** Am Ende jeder Etappe steht ab heute eine Frage ohne Musterlösung — eine, über die in echten Projekten gestritten wird. Zwei bis fünf Sätze in `GELERNT.md`, und niemand korrigiert sie. Du liest sie in ein paar Wochen wieder. Die erste gehört zu 17c.

---

# Teil 17a — Zufall

## Worum es geht

Bis heute hast du jede Welle selbst geschrieben. Nicht Gegner für Gegner, aber fast: Eine `if`/`elif`-Kette aus Etappe 6 legt fest, welche Typen ab welcher Welle kommen, und eine feste Regel sagt, der wievielte Gegner ein Speier ist. **Welle 9 sieht bei jedem Spiel genau gleich aus.** Wer sie einmal überlebt hat, überlebt sie wieder.

> **Ab heute werden deine Wellen erzeugt.**

Das klingt nach einer Zeile — `random` ist in Python tatsächlich schnell benutzt. **Der schwierige Teil ist nicht `random`, sondern das Wort davor:**

> **Wie erzeugt man *kontrollierte* Unvorhersehbarkeit?**

Deine Welle 14 soll jedes Mal anders sein — aber nicht mal spielbar und mal unmöglich. Sie soll überraschen, aber nicht unfair sein. **Diese Frage steht in keiner Dokumentation**, und sie ist der eigentliche Stoff dieser Portion. Die Antwort hat einen Namen: **Budget.**

Dazu löst du heute eine Frage ein, die du seit Etappe 4 mit dir herumträgst: **Warum fällt ein seltenes Ding genauso oft wie ein häufiges — und wie ändert man das?**

---

## Der lange Bogen — was heute fällig wird

- **Die `if`/`elif`-Kette aus Etappe 6, Schritt 9** — und die feste Verteilung aus Schritt 9b. Beide sterben heute. Etappe 6 hat es zweimal angekündigt; heute ist es so weit.
- **Die Anzahlformel aus Etappe 3c.** Du hast damals selbst entschieden, wie viele Gegner eine Welle hat. Heute wird daraus ein Budget.
- **`GEGNERTYPEN` bekommt Zahlen.** Etappe 6 hat versprochen: *„ein Feld mehr im selben Dictionary, keine neue Struktur."* Es werden drei Felder, und die Struktur bleibt dieselbe.
- **Die vierte Menge aus Etappe 6, Konzept 12b.** Neben *was existiert*, *was kann kommen* und *was kenne ich* kommt heute eine vierte Frage: *was kann sich der Generator gerade leisten?*
- **Die Beutefrage aus Etappe 4:** *Warum fällt ein Datenkern so oft wie ein Chitinpanzer?* Sie steht seit dreizehn Etappen in deiner `GELERNT.md`. Heute bekommt sie ihre Antwort.
- **Die Säuredrüse aus Etappe 4**, die ein Speier seitdem hinterlassen soll. Beute wird heute typgebunden und gewichtet — und die Tabelle *Gegnertyp → Fundkennung* aus Etappe 15 geht darin auf.
- **Das Vorwissen aus Etappe 15.** Solange die Wellen fest waren, war es eine nette Zeile. Ab heute ist es ein echter Vorteil.
- **`wellen_bis_evakuierung` aus Etappe 1.** Der Generator weiß ab heute, welche Welle die letzte ist.
- **Die Transferaufgabe aus Etappe 3.** Dein Zahlenraten hatte eine fest hingeschriebene Zahl, *„`random` ist Etappe 17a"*. Heute ist Etappe 17a.

---

## Eine Design-Entscheidung: Wie entsteht eine Welle? ⭐⭐

**Das Problem:** Zwanzig Wellen. Jede soll schwerer sein als die davor, jede soll sich anders anfühlen, und keine soll unfair sein. Drei Modelle, die man ernsthaft bauen könnte:

| | A — Feste Anzahl, fester Typ | B — Rein zufällig | C — Budget |
|---|---|---|---|
| Wie | `anzahl` aus der Wellennummer, die Typen nach Regel — so, wie dein Spiel es heute tut | Für jeden Gegner würfeln, welcher Typ es wird | Jede Welle bekommt eine Summe; jeder Typ kostet etwas; der Generator kauft zufällig ein, bis nichts mehr bezahlbar ist |
| Welle 14 beim zweiten Spiel | genau wie beim ersten | irgendwas | anders, aber ungefähr gleich schwer |
| Was schiefgeht | Nach dem dritten Spiel kennst du jede Welle auswendig | Welle 3 besteht irgendwann aus drei Panzerbruten, und du verlierst, ohne etwas falsch gemacht zu haben | Ein Typ, der nichts kostet — dazu Konzept 5 |
| Ein neuer Gegnertyp | eine neue Regel in der Kette | eine Zeile — aber er kommt genauso oft wie alle anderen | eine Zeile **mit Preis** |

**Welches würdest du wählen?** Entscheide, bevor du weiterliest, und schreib einen Satz in `GELERNT.md`, warum.

Der Plan baut C, und die Begründung ist ein einziger Gedanke. **Das Budget trennt zwei Fragen, die Anfänger fast immer vermischen:**

> **Wie schwer ist die Welle?** — Das entscheidest du. Das Budget wächst planbar mit der Wellennummer.
> **Woraus besteht sie?** — Das entscheidet der Würfel, aber nur innerhalb des Budgets.

Das erste kontrollierst du, das zweite überlässt du dem Zufall. **Das ist der ganze Trick**, und er ist derselbe, mit dem echte Spiele ihre Gegnerwellen, Beutetruhen und Kartenstapel bauen. B vermischt beide Fragen — wie schwer eine Welle wird, entscheidet dort der Würfel mit. A trennt sie gar nicht, weil es keinen Zufall hat.

⚠️ **Modell A ist nicht dumm.** Für eine handgemachte Kampagne mit zehn sorgfältig gebauten Leveln ist es genau richtig — dort soll Welle 7 jedes Mal dieselbe sein. Es passt nur nicht zu einem Spiel, das man zwanzigmal durchspielen soll. **Hast du anders gewählt als der Plan, streich deine Antwort nicht durch.** Schreib daneben, was dich überzeugt hat oder nicht. In Etappe 22 und 25, wenn Kosten und Wellenrezepte zu Daten werden, holst du sie wieder hervor.

---

## Die Konzepte — Teil 17a

### 1. `import random` — ein Werkzeugkasten, den Python mitbringt

Alles, was du bisher benutzt hast — `print`, `len`, `range`, `input` —, war einfach da. **Zufall ist nicht einfach da.** Er liegt in einem Werkzeugkasten, den Python mitbringt, aber erst auf Anfrage aufmacht. Die Anfrage ist eine Zeile:

```python
import random
```

**Wie das genau funktioniert, erklärt Etappe 24.** Bis dahin ist das hier eine Gebrauchsanweisung, und sie hat drei Regeln:

1. **Die Zeile steht ganz oben in der Datei**, als allererste Zeile, noch vor deinen festen Werten. Dort sucht jeder Leser zuerst nach der Antwort auf *„woher kommt dieser Name?"*.
2. **Danach schreibst du `random.` vor jedes Werkzeug aus dem Kasten** — `random.randint(...)`, `random.choice(...)`. Der Punkt ist dieselbe Schreibweise wie bei `wert.methode()`: erst, wo es herkommt, dann, was es tut.
3. ⚠️ **Nenn keine eigene Datei `random.py`.** Klingt harmlos für eine Wegwerf-Datei, in der du Zufall ausprobierst — und ist der häufigste Fehler dieser Etappe. Python sucht beim `import` zuerst im Ordner, in dem dein Programm liegt. Findet es dort eine `random.py`, nimmt es **deine** Datei statt des Werkzeugkastens. Je nachdem, was in dieser Datei steht, bekommst du eine von zwei Meldungen:

```
AttributeError: partially initialized module 'random' has no attribute 'randint' (most likely due to a circular import)
AttributeError: module 'random' has no attribute 'randint'
```

Die erste kommt, wenn deine Wegwerf-Datei selbst `random.py` heißt und `import random` enthält — sie importiert sich dann selbst. Die zweite, wenn eine andere Datei eine `random.py` im selben Ordner findet. **Beide heißen dasselbe: umbenennen.** *(Je nach Python-Version steht noch ein Hinweis dahinter, der genau das sagt.)*

### 2. Drei Würfel

**`random.randint(a, b)` — eine ganze Zahl von `a` bis `b`.**

```python
wurf = random.randint(1, 6)     # 1, 2, 3, 4, 5 oder 6
```

⚠️ **Beide Enden sind eingeschlossen.** Das ist anders als bei `range(1, 6)`, das bei 5 aufhört. `randint(1, 6)` kann eine 6 liefern. Zwei Werkzeuge, zwei Regeln — und genau an dieser Stelle entsteht der Off-by-one-Fehler dieser Etappe.

**`random.choice(liste)` — ein Eintrag aus einer Liste**, jeder gleich wahrscheinlich:

```python
suppen = ["Linsen", "Tomate", "Kürbis"]
heute = random.choice(suppen)
```

Wer in Etappe 4 die Kür gebaut hat, kennt es schon. Ab heute darf es im Auftrag stehen. **Eine leere Liste mag `choice` nicht** — du bekommst `IndexError: Cannot choose from an empty sequence`, weil es nichts gibt, das es herausgeben könnte.

🧠 **`random.random()` — eine Kommazahl, mindestens 0, aber immer unter 1.** Zum Beispiel `0.7263...`. Du brauchst sie heute nicht zum Bauen, sollst aber wissen, wofür man sie nimmt: **als Prozentchance.**

```python
if random.random() < 0.3:
    print("Es regnet.")      # in etwa drei von zehn Fällen
```

*(Alle drei ziehen aus derselben Quelle — einer langen Zahlenfolge, die Python für dich ausrechnet. Was es mit dieser Folge auf sich hat, ist Thema von 17b.)*

### 3. ⭐⭐ Gewicht gegen Wahrscheinlichkeit

`random.choice` behandelt alles gleich. **Ein Datenkern so oft wie ein Chitinpanzer** — das war die Beobachtung aus der Kür von Etappe 4, und sie ist das Problem, das du heute löst.

**Ein Gewicht ist keine Wahrscheinlichkeit.** Es ist eine Zahl, die nur im Vergleich mit den anderen etwas bedeutet. Stell dir ein Glücksrad auf dem Jahrmarkt vor, mit drei Farben:

| Farbe | Gewicht |
|---|---|
| rot | 5 |
| blau | 3 |
| grün | 2 |

Zusammen sind das **10**. Rot bekommt 5 von 10 Teilen des Rades, also die Hälfte. Blau 3 von 10, grün 2 von 10. **Der Anteil ist Gewicht durch Summe** — und deshalb ändert sich nichts, wenn du alle Gewichte verdoppelst. 10, 6, 4 ist dasselbe Rad.

**Und jetzt der Gedanke, aus dem du gleich eine Funktion baust.** Leg die drei Stücke hintereinander auf eine Strecke von 1 bis 10:

```
 1   2   3   4   5 | 6   7   8 | 9   10
 ——————— rot ————— | —— blau — | — grün —
```

Wirf eine Zahl von 1 bis 10 — jede gleich wahrscheinlich, das kann `randint`. **Wo sie landet, das ist die Farbe.** Weil rot die längste Strecke hat, landet dort am meisten.

Wie findet ein Programm heraus, in welchem Stück der Wurf liegt? **Es läuft die Stücke der Reihe nach ab und zieht jedes vom Wurf ab.** Für den Wurf 7:

| Schritt | Stück | Rechnung | Rest |
|---|---|---|---|
| 1 | rot, 5 | 7 − 5 | 2 — noch übrig, also nicht rot |
| 2 | blau, 3 | 2 − 3 | −1 — **aufgebraucht: blau** |

Rot hat den Wurf nicht verbraucht, blau schon. **Das Stück, bei dem der Rest aufgebraucht ist, ist das gezogene.**

**Und jetzt rechne selbst, bevor du baust:** Was kommt bei Wurf 5 heraus? Bei Wurf 6? Bei Wurf 10? **Bei zweien dieser drei hängt die Antwort davon ab, ob „aufgebraucht" `< 0` oder `<= 0` heißt** — und bei einem davon kommt mit der falschen Bedingung gar keine Farbe heraus. Welche der beiden Bedingungen passt zur Strecke oben — auf der die 5 noch zu rot gehört? Schreib deine Antwort auf, bevor du Schritt 2 anfängst. *(Das ist die eine Stelle der Etappe, an der sich Nachdenken mehr lohnt als Ausprobieren. Eine falsche Grenze stürzt nicht ab — sie verschiebt nur still die Anteile.)*

**Was du daraus baust, ist eine Funktion mit zwei Schleifen über dasselbe Dictionary:**

1. Die erste zählt die Gewichte zusammen.
2. Dazwischen ein Wurf von 1 bis zur Summe.
3. Die zweite läuft die Stücke ab und gibt das zurück, bei dem der Rest aufgebraucht ist.

Die zweite Schleife ist deine Suchschleife aus Etappe 15, Konzept 5: **`return` mitten in der Schleife, sobald es passt.** Und wie dort gehört ein `return None` ans Ende — falls die Schleife durchläuft, ohne etwas zu finden.

⚠️ **Und der Fehlerzweig, bevor du ihn im Spiel findest:** Was, wenn das Dictionary leer ist, oder alle Gewichte `0` sind? Dann ist die Summe `0`, und `random.randint(1, 0)` gibt es nicht:

```
ValueError: empty range for randrange() (1, 1, 0)
```

*(Der Wortlaut hinter `empty range` hängt von der Python-Version ab. Er nennt `randrange`, weil `randint` intern daran weitergibt.)* **Deshalb prüft deine Funktion die Summe, bevor sie würfelt, und gibt bei `0` sofort `None` zurück.** Wer sie aufruft, muss mit `None` rechnen — die Regel aus Etappe 15, Konzept 5.

**Zum Mitnehmen:** Deine Funktion kennt weder Gegner noch Beute noch Glücksräder. Sie bekommt ein Dictionary *Name → Gewicht* und gibt einen Namen zurück. **Deshalb kannst du sie für alles benutzen, was in dieser Etappe gewichtet wird** — und das sind drei verschiedene Dinge: Gegner und Beute in 17a, Ereignisse in 17c.

### 4. Wie prüft man etwas, das jedes Mal anders ausgeht?

Bisher war die Prüfung einfach: ausführen, hinsehen, stimmt es? **Bei Zufall trägt das nicht mehr.** Ein Wurf, der „blau" liefert, beweist gar nichts — blau darf ja kommen.

**Was du prüfen kannst, ist die Verteilung.** Lass die Funktion zehntausendmal ziehen und zähl mit, wie oft jedes Ergebnis kam. Bei einem richtigen Rad landest du ungefähr bei 5000, 3000, 2000 — nicht genau, aber nah dran. Bei einer falschen Grenze aus Konzept 3 siehst du es sofort.

**Aber Zählen beweist nicht, dass deine Funktion stimmt.** Es macht grobe Fehler sichtbar — eine Grenze, die ein Gewicht verdoppelt, springt dir entgegen. Ein Fehler, der nur jeden tausendsten Zug betrifft, geht in den Schwankungen unter. *(Was eine bestandene Prüfung überhaupt beweist, fragt Etappe 26.)*

Zum Zählen brauchst du ein Muster, das aus zwei bekannten Teilen besteht: `.get()` mit Ersatzwert aus Etappe 5 und das Schreiben in ein Dictionary. **Fremdes Beispiel — Wörter in einer Einkaufsliste zählen:**

```python
einkauf = ["Brot", "Milch", "Brot", "Eier", "Brot"]
anzahl = {}
for ding in einkauf:
    anzahl[ding] = anzahl.get(ding, 0) + 1
print(anzahl)     # {'Brot': 3, 'Milch': 1, 'Eier': 1}
```

Beim ersten „Brot" gibt es den Schlüssel noch nicht, `.get()` liefert `0`, und `0 + 1` wird eingetragen. Beim zweiten liefert es `1`. **Eine Zeile, und kein `if` für den ersten Fall.**

### 5. ⭐⭐ Das Budget-Muster

Stell dir vor, du stehst mit **10 Münzen** auf dem Jahrmarkt und willst sie zufällig ausgeben:

| Stand | kostet | wie gern (Gewicht) |
|---|---|---|
| Los | 1 | 5 |
| Zuckerwatte | 3 | 3 |
| Karussell | 4 | 2 |

**Eine Runde geht so:** Schau, was du dir **jetzt** noch leisten kannst. Zieh daraus gewichtet eines. Bezahl es. Nächste Runde. **Wenn nichts mehr bezahlbar ist, bist du fertig.**

Ein Durchlauf könnte so aussehen:

| Runde | Münzen vorher | bezahlbar | gezogen | Münzen nachher |
|---|---|---|---|---|
| 1 | 10 | Los, Zuckerwatte, Karussell | Karussell | 6 |
| 2 | 6 | Los, Zuckerwatte, Karussell | Zuckerwatte | 3 |
| 3 | 3 | Los, Zuckerwatte | Los | 2 |
| 4 | 2 | Los | Los | 1 |
| 5 | 1 | Los | Los | 0 |
| 6 | 0 | — | — | **fertig** |

Drei Dinge fallen auf, und alle drei gehören in deinen Generator:

**Erstens: Die Liste des Bezahlbaren wird in jeder Runde neu gebaut.** In Runde 3 ist das Karussell herausgefallen, weil nur noch drei Münzen da waren. Wer sie einmal vor der Schleife baut, kauft ein Karussell für Geld, das er nicht mehr hat. **Das ist die vierte Menge aus Etappe 6** — *was ist gerade leistbar* —, und sie ändert sich mit jedem Kauf.

**Zweitens: Die Liste des Bezahlbaren trägt die Gewichte gleich mit.** Du baust sie als Dictionary *Name → Gewicht*, und zwar genau in der Form, die deine Funktion aus Konzept 3 erwartet. Dann ist der Zug eine Zeile.

**Drittens, und das ist der Fehler, den fast jeder beim ersten Mal baut:** **Das Ende ist nicht „Budget ist 0".** Hätte das billigste Ding 2 Münzen gekostet, wäre in Runde 5 eine Münze übrig und nichts mehr bezahlbar. Eine Schleife `while budget > 0:` liefe dann für immer weiter — sie kann nichts kaufen, also sinkt das Budget nie. **Das richtige Ende ist: *nichts mehr bezahlbar*.** Das schließt „Budget ist 0" mit ein.

Wie du das Ende baust, entscheidest du. Zwei Wege sind gedeckt: **`while True:` mit `break`** aus Etappe 3, sobald das Bezahlbare leer ist — oder eine Zustandsvariable als Schleifenbedingung, ebenfalls aus Etappe 3. Für „ist leer?" gilt beim Dictionary dasselbe wie bei der Liste aus Etappe 4: **Ein leeres Dictionary ist falsy.** `if not bezahlbar:` liest sich wie der Satz, den es prüft.

### 6. Die Kette stirbt — vorher und nachher

So ungefähr sieht deine Kette aus Etappe 6 heute aus, nur mit deinen Namen:

```
wenn welle höchstens 3:   erlaubt ist nur kriecher
sonst wenn höchstens 7:   kriecher und speier
sonst:                    alle drei
```

**Das ist Logik, die eigentlich eine Angabe ist.** *„Die Panzerbrut kommt ab Welle 8"* ist ein Satz über die Panzerbrut — er gehört zu ihr, nicht in eine Kette, die über alle Typen gleichzeitig entscheidet.

Ab heute steht er dort. Jeder Typ in `GEGNERTYPEN` bekommt ein Feld `"ab_welle"`, und die Kette wird zu **einer Bedingung**, die für jeden Typ gleich lautet: *Ist die aktuelle Welle mindestens seine `ab_welle`?*

| | Vorher | Nachher |
|---|---|---|
| Wo steht, ab wann ein Typ kommt? | in der Kette, für alle Typen gemischt | beim Typ selbst |
| Ein vierter Typ | ein neuer Zweig, und die anderen Zweige ändern sich mit | eine Zeile in `GEGNERTYPEN` |
| Mit dreißig Typen | eine Kette mit dreißig Zweigen | dieselbe Bedingung |

**Das ist der Faden „Daten statt Code" aus Etappe 5** — der Kauf schlug damals Preise nach, statt sie abzufragen. Heute schlägt die Welle nach, statt zu entscheiden. Und in Etappe 25 wandern genau diese Zahlen in eine Datei außerhalb deines Programms.

### 7. 👀 `random.choices` — die eine Zeile, die es auch kann

Python bringt eine gewichtete Auswahl fertig mit:

```python
farbe = random.choices(["rot", "blau", "grün"], weights=[5, 3, 2])[0]
```

**Nur erkennen, nicht bauen.** Drei Dinge sollst du daran sehen können:

- **Namen und Gewichte stehen in zwei getrennten Listen**, zusammengehalten nur über die Stelle — genau die unsichtbare Verbindung, die du in Etappe 6 mit `gegner` und `gegner_typen` hattest und in Etappe 11 losgeworden bist.
- **`choices` mit s liefert eine Liste**, auch wenn du nur eines willst. Daher das `[0]` am Ende. Ohne es hast du `['blau']` statt `'blau'` — und ein `if farbe == "blau":` ist dann still falsch.
- **Sie tut dasselbe wie deine Funktion aus Konzept 3.** Nicht ungefähr dasselbe — dasselbe Prinzip, die Strecke. Sie läuft sie nur geschickter ab als Stück für Stück.

**Warum dann selbst bauen?** Weil Etappe 4 dir eine Frage gestellt und ausdrücklich nicht beantwortet hat, und die Antwort ist nicht diese Zeile, sondern das Bild von der Strecke. **Wer die Zeile kennt, kann gewichten. Wer die Strecke kennt, kann erklären, warum ein Gewicht von 0 nie gezogen wird, warum Verdoppeln nichts ändert und wo eine Grenze falsch sitzt.** Nach dieser Etappe darfst du `random.choices` benutzen, wo du willst — deine Funktion bleibt aber im Spiel, weil sie mit Dictionaries arbeitet und nicht mit zwei Listen.

### 8. ⭐ Beute mit Gewicht — die Antwort auf Etappe 4

Seit Etappe 15 entscheiden bei dir **zwei Stellen**, was ein Gefallener hinterlässt: die Regel für sein Material aus Etappe 5 — oder, wenn du in Etappe 4 die Kür gebaut hast, `random.choice` über eine Beuteliste — und die Tabelle *Gegnertyp → Fundkennung* aus Etappe 15, Schritt 3. **Beide sind entweder fest oder gleichverteilt.** Jeder Speier hinterlässt seinen Fund, jedes Mal. Und in der Kür von Etappe 4 fällt ein Datenkern so oft wie ein Chitinpanzer.

**Das ist die Frage, die du in Etappe 4 in `GELERNT.md` geschrieben und stehen gelassen hast.** Die Antwort ist das Glücksrad aus Konzept 3: **Selten heißt, ein kleines Stück der Strecke zu bekommen.** Ab heute zieht jeder Typ aus **einer** Tabelle, in der Material, Fund und „nichts" nebeneinanderstehen, jedes mit seinem Gewicht:

```
kriecher   →  chitinpanzer: 60   organ: 20   nichts: 17   sein Fund: 3
```

Der Fund bekommt 3 von 100 Teilen des Rades. **Er kommt — aber selten.** Und weil es eine Tabelle ist und nicht zwei, gibt es auch nur noch eine Tabelle, die festlegt, was ein Typ fallen lassen kann und wie oft. Ein Gefallener hinterlässt ab heute **höchstens ein** Fundstück.

**Drei Entscheidungen stecken darin, und alle drei sind Absicht:**

**„nichts" steht in der Tabelle wie jedes andere Ergebnis.** Dann entscheidet dasselbe Gewicht, wie oft ein Gegner leer ausgeht, und du musst dafür keine zweite Würfelregel erfinden. **Der Preis:** `"nichts"` ist ein ganz normaler String. Wer nach dem Ziehen nicht fragt, ob `"nichts"` herauskam, legt ein `Fundstueck` namens `nichts` ins Vorfeld — und dein Einsammeln trägt es brav ein, als Einzelstück in dein Inventar. **Kein Absturz, nur ein Fehler, den man lange nicht bemerkt.** *(Deshalb muss das Wort eine Kennung sein, die es sonst nirgends gibt.)*

**Die Funde aus Etappe 15 stehen mit kleinen Gewichten mit drin.** Sie sind die seltenste Beute des Spiels — und damit das, was ein Fund sein soll. Ein Fund, der bei jedem Speier liegt, ist nach der dritten Welle keiner mehr.

**Seltene Beute bleibt Brut.** Der Grundsatz aus Etappe 4 und 5 gilt auch für das Wertvollste: Aus der Brut fällt nichts, was ein Mensch anlegen kann — keine Munition, kein Vaporium, keine Panzerplatte, **auch nicht als seltener Glücksfall.**

---

## Dein Auftrag — Teil 17a

Nach **jedem** Schritt ausführen. Ab Schritt 7 dazu eine Welle spielen — **und das Spiel zweimal starten**, denn ab dort ist jeder Lauf anders.

---

### 1. Wirf ein paar Würfel in einer Wegwerf-Datei

Leg neben `spiel.py` eine Datei `wuerfeln.py` an — **nicht `random.py`**, Konzept 1.

- Erste Zeile: `import random`.
- Eine `for`-Schleife, die zehnmal `random.randint(1, 6)` ausgibt.
- Eine Liste mit drei, vier Dingen deiner Wahl und fünfmal `random.choice()` daraus.
- Einmal `random.random()` ausgeben.

**Führ die Datei dreimal hintereinander aus.**

**So prüfst du es:** Dreimal verschiedene Zahlen. Über die dreißig Würfe der drei Läufe taucht so gut wie sicher eine 6 auf, aber nie eine 0 oder eine 7. *(Keine 6 dabei? Noch zwei Läufe. Kommt nie eine 6, egal wie oft? Dann steht da `randint(1, 5)`.)*

---

### 2. ⭐⭐ Bau `gewichtete_wahl()` in der Wegwerf-Datei

**In `wuerfeln.py`, noch nicht im Spiel.** Hier kannst du sie prüfen, ohne dass zwanzig andere Dinge mitlaufen.

| | |
|---|---|
| Name | `gewichtete_wahl` |
| Parameter | eines: ein Dictionary *Name → Gewicht*, die Gewichte ganze Zahlen ab 0 |
| Rückgabe | einer der Namen — nach Gewicht gezogen |
| Wenn das Dictionary leer ist oder alle Gewichte 0 sind | `None`, **ohne** zu würfeln |
| Am Ende der Funktion, falls die zweite Schleife nichts zurückgegeben hat | `None` |

Bau sie nach Konzept 3: erste Schleife summiert, dann Summe prüfen, dann ein Wurf von 1 bis zur Summe, zweite Schleife läuft ab. **Die Grenze `< 0` oder `<= 0` hast du vorher auf Papier entschieden** — Konzept 3, letzte Frage.

⚠️ **Die `def`-Zeile steht über dem Code, der sie aufruft** — wie in Etappe 7. In der Wegwerf-Datei heißt das: erst `import`, dann die Funktion, dann die Prüfungen unten.

**So prüfst du es — drei Prüfungen, unten in `wuerfeln.py`:**

1. **Die Verteilung.** Das Glücksrad aus Konzept 3 als Dictionary, zehntausendmal ziehen, mitzählen nach Konzept 4, Ergebnis ausgeben. Du erwartest ungefähr 5000 rot, 3000 blau, 2000 grün.
2. **Die Grenze.** Ein Rad mit zwei Farben, beide Gewicht 1. Du erwartest ungefähr halbe-halbe. **Wenn eine Farbe doppelt so oft kommt wie die andere, oder `None` auftaucht, sitzt deine Grenze falsch** — zurück zu Konzept 3.
3. **Die Fehlerzweige.** `print(gewichtete_wahl({}))` und `print(gewichtete_wahl({"x": 0}))`. Beide müssen `None` ausgeben, nicht abstürzen.

*(Behalte `wuerfeln.py` bis zur Transferaufgabe am Ende des Guides. Mach die **vor** dem Commit in Schritt 10 und lösch die Datei danach — sonst nimmt `git add .` sie mit.)*

---

### 3. Hol die Funktion ins Spiel

- **`import random` wird die erste Zeile von `spiel.py`**, noch über deinen festen Werten. *(Steht sie schon irgendwo, weil du in Etappe 4 die Kür gebaut hast? Dann nicht doppelt — nur nach ganz oben damit.)*
- `gewichtete_wahl` kommt **zu deinen anderen Funktionen** über dem Hauptprogramm. Kopieren, nicht neu schreiben — sie ist geprüft.

**So prüfst du es:** Das Spiel startet und läuft wie vorher. Noch benutzt niemand die Funktion; es geht nur darum, dass nichts kaputt ist.

---

### 4. Gib jedem Gegnertyp drei Zahlen

Jeder Eintrag in `GEGNERTYPEN` bekommt zu `"lang"` und `"kurz"` drei neue Schlüssel:

| Kennung | `"kosten"` | `"gewicht"` | `"ab_welle"` |
|---|---|---|---|
| `"kriecher"` | 1 | 6 | 1 |
| `"speier"` | 3 | 3 | 4 |
| `"panzerbrut"` | 6 | 1 | 8 |

**Zwei Regeln für diese Zahlen:** `"gewicht"` ist 0 oder größer — 0 heißt „kommt nie". `"kosten"` ist **mindestens 1.** Warum hier eine 0 verboten ist, obwohl sie beim Gewicht erlaubt ist, zeigt dir Kaputtmachen 3. Schreib beide Regeln zu deinen Invarianten aus Etappe 5.

**Die `"ab_welle"`-Werte sind dieselben Grenzen wie in deiner Kette aus Etappe 6** — Welle 4 für den Speier, Welle 8 für die Panzerbrut. Du verschiebst die Entscheidung, du änderst sie nicht.

⚠️ **Hast du in Etappe 6 den vierten Typ eingetragen, den keine Welle ausspuckt?** Dann braucht auch er alle drei Schlüssel, sonst gibt es in Schritt 6 einen `KeyError: 'kosten'`. Etappe 6 hat versprochen, dass du heute entscheidest, ab welcher Welle er kommt. **Das ist jetzt eine einzige Zahl.** Soll er nie kommen: eine `"ab_welle"` über `wellen_bis_evakuierung`.

**So prüfst du es — in einer frischen Probedatei**, angelegt wie in Etappe 9: `spiel.py` als `probe.py` kopieren, den Teil löschen, der das Spiel startet, Prüfzeilen unten anfügen. Eine alte Kopie kennt die neuen Schlüssel nicht. Prüfzeile: `print(GEGNERTYPEN["speier"]["kosten"])` — du erwartest `3`.

---

### 5. Leg das Budget als feste Werte an

Bei deinen anderen festen Werten, GROSS geschrieben:

| Name | Wert | Bedeutung |
|---|---|---|
| `BUDGET_START` | `3` | Grundbudget jeder Welle |
| `BUDGET_PRO_WELLE` | `2` | kommt pro Wellennummer dazu |

**Das Budget einer Welle ist `BUDGET_START + BUDGET_PRO_WELLE * welle`.** Welle 1 hat also 5, Welle 10 hat 23. **Die letzte Welle bekommt das doppelte Budget** — sie ist die, vor der die Evakuierung kommt, und sie soll sich so anfühlen.

⚠️ **Die Balancing-Falle aus Etappe 3c gilt wieder.** Du wirst an diesen zwei Zahlen drehen wollen. Tu es — aber **erst nach Schritt 10**, mit einem Deckel von fünfzehn Minuten, und schreib jede Änderung mit Begründung in deine Notizliste. Eine langweilige Welle, die läuft, schlägt eine spannende, die abstürzt.

---

### 6. ⭐⭐ Bau den Generator `erzeuge_welle()`

**Eine Funktion, die eine Liste von Typnamen zurückgibt.** Nicht Gegner-Objekte — nur die Namen, zum Beispiel `["kriecher", "speier", "kriecher", "kriecher"]`. Aus Namen Objekte zu machen kann dein Spiel seit Etappe 11; das bleibt, wo es ist.

| | |
|---|---|
| Name | `erzeuge_welle` |
| Parameter | `welle` (die Nummer der Welle) und `letzte_welle` (die Nummer der letzten Welle — beim Aufruf übergibst du dein `wellen_bis_evakuierung` aus Etappe 1) |
| Rückgabe | eine Liste von Kennungen aus `GEGNERTYPEN` |
| Wo | bei deinen anderen Funktionen, **unter** `gewichtete_wahl` |

**Was sie tut, nach Konzept 5:**

- Budget ausrechnen, nach der Formel aus Schritt 5. Letzte Welle: verdoppeln.
- Eine leere Namensliste anlegen.
- **In jeder Runde:**
  - Ein neues, leeres Dictionary *bezahlbar* anlegen.
  - Über `GEGNERTYPEN` laufen. Ein Typ kommt hinein, wenn **beides** stimmt: Seine `"ab_welle"` ist höchstens die aktuelle Welle, **und** seine `"kosten"` sind höchstens das Restbudget. Eingetragen wird sein Name mit seinem `"gewicht"`.
  - Ist *bezahlbar* leer: fertig, raus aus der Schleife.
  - Sonst mit `gewichtete_wahl` einen Namen ziehen, an die Namensliste hängen, seine Kosten vom Budget abziehen.
- Die Namensliste zurückgeben.

⚠️ **Kann `gewichtete_wahl` hier `None` liefern?** Nur, wenn alle bezahlbaren Typen das Gewicht 0 haben. Mit deinen Zahlen passiert das nicht — **prüf es trotzdem** und behandle `None` wie „nichts bezahlbar". Die Regel aus Etappe 15 fragt nicht, ob es gerade vorkommt. *(Wer es auslässt und irgendwann alle bezahlbaren Typen auf Gewicht 0 stellt, bekommt einen `KeyError: None` eine Zeile später — beim Abziehen der Kosten.)*

*(Warum läuft die Schleife über `GEGNERTYPEN` und nicht über ein Set der erlaubten Typen? Weil ein Dictionary seine Schlüssel in der Reihenfolge liefert, in der du sie hingeschrieben hast. Ein Set tut das nicht, Etappe 6, Konzept 3. Heute ist dir das egal — in 17b wird es wichtig.)*

**So prüfst du es — in der Probedatei, nicht im Spiel.** Kopier sie **frisch**, wie in Schritt 4 — die von dort kennt den Generator noch nicht. *(Das gilt für jede Probedatei heute: Sie ist eine Momentaufnahme von `spiel.py`, und nach jeder Änderung ist sie alt.)*

- `print(erzeuge_welle(1, 20))` dreimal hintereinander. Du erwartest fünf Kriecher, jedes Mal. **Warum ist Welle 1 nicht zufällig?** Die Antwort steht in deiner Tabelle aus Schritt 4.
- `print(erzeuge_welle(5, 20))` dreimal. Jetzt unterscheiden sich die Listen.
- `print(erzeuge_welle(19, 20))` und `print(erzeuge_welle(20, 20))`. Welle 20 ist deutlich länger.
- **Rechne für eine der Listen nach:** Summe der Kosten aller Namen. Mit deinen Zahlen ist sie **genau** das Budget — der Kriecher kostet 1 und passt immer noch hinein. *(Wäre der billigste Typ 2 wert, bliebe manchmal eine 1 übrig. Das ist in Ordnung und genau der Fall aus Konzept 5.)*

> **⏸ Guter Schnitt.** Der Generator steht und ist geprüft, aber noch nicht eingebaut. Dein Spiel läuft unverändert — ein sicherer Stand zum Aufhören. *(Die Probedatei vor dem Aufhören löschen oder nicht committen.)*

---

### 7. ⭐ Bau den Generator ein — und lösch die Kette

Such die Stelle am Anfang jeder Welle, an der heute drei Dinge passieren:

| Was dort heute steht | Was daraus wird |
|---|---|
| Deine Anzahlformel aus Etappe 3c | **fällt weg** — das Budget entscheidet über die Menge |
| Die `if`/`elif`-Kette aus Etappe 6, Schritt 9, die `wellen_typen` setzt | **fällt weg** — `"ab_welle"` entscheidet |
| Die feste Verteilung aus Etappe 6, Schritt 9b (*„der erste ist Speier …"*) | **fällt weg** — der Generator entscheidet |
| Der Code, der für jeden Gegner ein `Gegner`-Objekt auf dem Spawnpunkt erzeugt | **bleibt** — nur woher der Name kommt, ändert sich |

**Ruf `erzeuge_welle` einmal pro Welle auf — mit der aktuellen Wellennummer und deinem `wellen_bis_evakuierung` — und merk dir die Liste unter einem Namen.** Dann erzeug für jeden Namen darin einen Gegner, genau so, wie dein Code es heute schon tut.

⚠️ **`wellen_typen` darf nicht einfach verschwinden.** Deine Wellenankündigung aus Etappe 6, Schritt 10, fragt mit `in wellen_typen`, welche Typen in dieser Welle vorkommen — für den langen oder kurzen Text. **Bau das Set ab heute aus der Namensliste:** ein leeres Set, und für jeden Namen ein `.add()`. Doppelte fallen von selbst weg, das ist Etappe 6, Konzept 3. Die Ankündigung selbst fasst du nicht an.

**Und bevor du löschst:** Zähl die Zeilen, die wegfallen, und die, die dazukommen. **Beide Zahlen in `GELERNT.md`.** Das ist der Vorher-Nachher-Vergleich aus Konzept 6, an deinem eigenen Code.

**So prüfst du es:**
- Spiel startet, Welle 1 kommt, die Ankündigung nennt die Kriecher.
- Lass deine Wellenschleife testweise bei `8` beginnen statt bei `1` und **starte das Spiel zweimal.** Zwei verschiedene Wellen, und die Ankündigung nennt jedes Mal genau die Typen, die tatsächlich im Vorfeld stehen.
- Den Startwert der Wellenschleife wieder auf `1` setzen.

---

### 8. Stell das Vorwissen um

Dein Vorwissen aus Etappe 15, Schritt 12, liest die Kette — und die gibt es nicht mehr. **Ab heute liest es die Namensliste der Welle.** Die Bedingung bleibt dieselbe: nur, wer die passende Erkenntnis in `welt.erkenntnisse` hat.

**Und jetzt kann es mehr als vorher, weil es mehr zu wissen gibt.** Ohne Vorwissen erfährt der Spieler, **wie viele** Gegner kommen. Mit Vorwissen erfährt er **die Zusammensetzung**: wie viele von jedem Typ.

```
Welle 11 — 14 Kontakte.
Die Sporen verraten mehr:  10 kriecher · 3 speier · 1 panzerbrut
```

**Wie du zählst, entscheidest du.** Zwei Wege sind gedeckt: das Zählmuster aus Konzept 4 über die Namensliste, oder zwei verschachtelte Schleifen aus Etappe 3 — außen über `GEGNERTYPEN`, innen über die Namen, mit einem Zähler. Der zweite Weg liefert die Typen gleich in fester Reihenfolge.

**So prüfst du es:** Einmal mit und einmal ohne die Erkenntnis in `welt.erkenntnisse` eine Welle beginnen. Die Zahlen in der Zusammensetzung ergeben zusammen die Gesamtzahl.

*(Etappe 15 hat versprochen, dass der Generator das Vorwissen wertvoll macht. Hier ist der Grund: Solange Welle 11 immer gleich war, konntest du sie dir merken. Jetzt nicht mehr.)*

---

### 9. ⭐ Mach die Beute typgebunden und gewichtet — in einer Tabelle

**Eine neue Tabelle, oben bei den anderen:** `BEUTE`, Gegnertyp → Dictionary *Kennung → Gewicht*.

| Typ | Einträge |
|---|---|
| `"kriecher"` | `"chitinpanzer"`: 60 · `"organ"`: 20 · `"nichts"`: 17 · sein Fund: 3 |
| `"speier"` | `"saeuredruese"`: 50 · `"organ"`: 30 · `"nichts"`: 16 · sein Fund: 4 |
| `"panzerbrut"` | `"chitinpanzer"`: 55 · `"organ"`: 35 · sein Fund: 10 |

**„Sein Fund"** ist die Kennung, die dieser Typ in deiner Tabelle *Gegnertyp → Fundkennung* aus Etappe 15, Schritt 3, hat — **genau so geschrieben wie dort und in `FUNDE`.** Hat ein Typ dort keinen Eintrag, lässt du den Eintrag weg und schlägst sein Gewicht auf `"nichts"`. *(Steht ein Datenkern unter deinen Funden, hast du jetzt die Antwort auf Etappe 4 in Zahlen.)* Die Zahlen darfst du ändern; die Form nicht.

⚠️ **Verweis ins Leere, wie in Etappe 15, Konzept 1:** Ein Buchstabe Unterschied zwischen der Kennung in `BEUTE` und der in `FUNDE`, und die Probe fällt, lässt sich einsammeln und bringt beim Analysieren nie eine Erkenntnis. Kein Absturz. **Kopier jede Fundkennung aus `FUNDE`, statt sie abzutippen.**

**In deiner Aufräumphase** — dort, wo seit Etappe 15 ein Gefallener etwas als `Fundstueck` auf sein Feld legt:

- Mit `.get()` über seinen `name` die Tabelle seines Typs holen. `None`? Dann lässt dieser Typ nichts fallen — kein Sonderfall, die Regel aus Etappe 15.
- Sonst mit `gewichtete_wahl` ziehen.
- Ist das Ergebnis `"nichts"` **oder `None`**: **kein** `Fundstueck`. Sonst **eines** mit der gezogenen Kennung, an seiner Koordinate, wie bisher. *(`None` kommt nur, wenn alle Gewichte einer Tabelle 0 sind — die Regel aus Etappe 15 fragt trotzdem.)*
- **Die Tabelle *Gegnertyp → Fundkennung* aus Etappe 15 und die Regel, die das Material bestimmt, fallen weg** — `BEUTE` ersetzt beide. Hast du in Etappe 4 die Kür gebaut, fallen auch die Beuteliste und ihr `random.choice` weg. **Zwei Tabellen, die festlegen, was fällt, wären zwei Wahrheiten.**
- **`FUNDE` bleibt, wie es ist.** Dort steht, was ein Fund *bedeutet*. `BEUTE` sagt nur, *wie oft* er fällt.

⚠️ **Ein Material ist neu:** die Säuredrüse, die Etappe 4 dem Speier versprochen hat. Sie braucht die drei Einträge, die Etappe 5 für neue Beute genannt hat:

| Wo | Eintrag |
|---|---|
| `vorrat`, dort wo er seine Startwerte bekommt | `"saeuredruese"` mit `0` |
| `VERKAUFSWERTE` | `"saeuredruese"` — eigene Wahl, mehr als ein Organ |
| `ANZEIGENAMEN` | `"saeuredruese"` → `"Säuredrüse"` |

**Und jetzt der Test aus Etappe 5 und 15, zum dritten Mal:** Musst du irgendwo in deiner **Logik** einen Materialnamen eintippen, damit die Säuredrüse eingesammelt, gezählt und verkauft wird? Wenn deine Einsammelphase nach `kennung in vorrat` entscheidet, lautet die Antwort *nein* — **ein neues Material sind drei Dateneinträge und keine Zeile Logik.** Schreib die Antwort in `GELERNT.md`.

**So prüfst du es — zuerst gezählt, dann gespielt:**

- **In einer frisch kopierten Probedatei** die Zählprobe aus Konzept 4 mit `BEUTE["kriecher"]`, zehntausend Züge. Etwa 300 davon sind sein Fund — nicht ein Viertel, wie es bei vier gleich häufigen Ergebnissen wäre.
- **Im Spiel** ein paar Wellen, mit einer vorübergehenden Prüfzeile `print(welt.fundstuecke)` vor dem Einsammeln und dem `vorrat` danach. *(Die Prüfzeile danach wieder löschen.)* Kriecher lassen manchmal nichts liegen. Speier hinterlassen Säuredrüsen. **Nirgends liegt ein Fundstück mit der Kennung `nichts`.** Ein Fund ist selten — wenn du ihn in fünf Wellen nicht siehst, ist das kein Fehler, sondern sein Gewicht.

**Und schreib die Antwort auf die Frage aus Etappe 4 unter die Frage in `GELERNT.md`** — in deinen Worten, mit dem Glücksrad.

---

### 10. Prüf, dass das Alte noch läuft, und commit

- Kaufen, verkaufen, nachladen, Sektor wechseln, Fähigkeit, Bestiarium, Turmbau, Räumen, Analysieren: alles wie vorher?
- **Das Bestiarium:** Zeigt es neue Typen weiterhin ausführlich und bekannte kurz? *(Es liest `gesehene_gegnertypen`, das du heute nicht angefasst hast — aber die Ankündigung, die es füllt, hat eine neue Quelle.)*
- **Das Analysieren:** Ein eingesammelter Fund lässt sich analysieren und bringt seine Erkenntnis — er kommt jetzt nur seltener.
- Beide Verlustbedingungen?
- Zwanzig Wellen ohne Absturz — oder, wenn dir das zu lange dauert, die Wellenschleife testweise bei `19` beginnen lassen und die letzten zwei spielen. **Welle 20 muss deutlich voller sein.** Danach den Startwert zurück auf `1`.
- Die Abschnitte am Ende, die zu 17a gehören: **Transferaufgabe** und **Kaputtmachen 1 bis 3**. Danach `wuerfeln.py` löschen. Keine `probe.py`, kein Testwert in der Wellenschleife.

Commit: `Etappe 17a: Wellen werden erzeugt`

---

## Selbsttest — 17a

- [ ] `gewichtete_wahl` liefert beim Glücksrad 5 : 3 : 2 nach zehntausend Zügen ungefähr 5000 : 3000 : 2000 — und bei zwei gleichen Gewichten ungefähr halbe-halbe.
- [ ] `gewichtete_wahl({})` und `gewichtete_wahl({"x": 0})` geben `None` zurück, ohne abzustürzen.
- [ ] Jeder Eintrag in `GEGNERTYPEN` hat `"kosten"`, `"gewicht"` und `"ab_welle"` — auch ein vierter, falls du ihn hast.
- [ ] `erzeuge_welle(1, 20)` liefert jedes Mal fünf Kriecher. **Du kannst sagen, warum.**
- [ ] Die Kosten einer erzeugten Welle ergeben zusammen genau ihr Budget. Welle 20 hat das doppelte.
- [ ] **Die `if`/`elif`-Kette aus Etappe 6 und die feste Verteilung aus Etappe 6, Schritt 9b, stehen nicht mehr in deinem Code.** Die Zeilenzahlen vorher und nachher stehen in `GELERNT.md`.
- [ ] Die Wellenankündigung nennt genau die Typen, die tatsächlich kommen.
- [ ] Mit Vorwissen siehst du die Zusammensetzung, ohne Vorwissen nur die Anzahl.
- [ ] Es gibt nur noch **eine** Tabelle, die festlegt, was ein Gegnertyp fallen lassen kann und wie oft: `BEUTE`. Die Tabelle *Gegnertyp → Fundkennung* ist weg.
- [ ] Die Zählprobe mit `BEUTE["kriecher"]` liefert seinen Fund in etwa 3 von 100 Zügen.
- [ ] Kein `Fundstueck` mit der Kennung `nichts`, nirgends.
- [ ] Die Säuredrüse wird eingesammelt, gezählt und verkauft, **ohne** dass ihr Name in deiner Logik steht.
- [ ] Unter deiner Frage aus Etappe 4 steht in `GELERNT.md` jetzt eine Antwort.

> **⏸ Ende von 17a.** Dein Spiel würfelt, und zwar kontrolliert. 17b beschäftigt sich mit der Frage, die sich daraus ergibt — und die du vielleicht schon gemerkt hast, als du in Schritt 7 zweimal gestartet hast: **Wie jagst du einen Fehler, der beim zweiten Start nicht mehr da ist?**

---

# Teil 17b — Der Seed

## Worum es geht

In Etappe 16 hast du Fehler gejagt, indem du dieselbe Lage immer wieder durchgespielt und mit einer Tabelle verglichen hast. **Das ging, weil dein Spiel bei denselben Eingaben immer dasselbe tat.**

Seit 17a stimmt das nicht mehr. Wenn dir in Welle 14 ein Speier seltsam vorkommt, startest du neu — und in Welle 14 gibt es keinen Speier. Der Fehler ist nicht weg. **Er ist nur nicht mehr vorführbar.**

> **Sobald Zufall im Spiel ist, lässt sich ein Fehler nicht mehr zweimal zeigen — außer man nagelt den Zufall fest.**

Das Werkzeug dafür ist eine Zeile, und der größte Teil dieser Portion ist trotzdem nicht diese Zeile. Er ist das, was du daraus machst: **ein Seed, den dein Spiel sichtbar anzeigt**, ein Beweislauf, der zeigt, dass zwei Spiele wirklich gleich sind — und die Erkenntnis, was ein Seed *nicht* festnagelt.

**Das ist die kürzeste Portion dieser Etappe.** Der Beweislauf in Schritt 13 ist trotzdem ein voller Abend.

---

## Der lange Bogen — was heute fällig wird

- **Die Tick-Tabelle aus Etappe 16** und der **bedingte Breakpoint aus Etappe 8.** Beide sind seit 17a nur noch etwas wert, wenn der Zufall festgenagelt ist. Heute ist er es.
- **`befehle.txt` und `diff` aus Etappe 7.** Der Beweis, dass zwei Läufe gleich sind, ist derselbe wie beim Refactoring.
- **Die Welt aus Etappe 12** bekommt ihr erstes neues Attribut dieser Etappe: den Seed. In Etappe 19 steht er als Erstes im Spielstand.

---

## Die Konzepte — Teil 17b

### 9. Der Fehler, der beim zweiten Mal nicht kommt

Deine Fehlersuche aus Etappe 8 und 16 hat eine stillschweigende Voraussetzung: **Wenn du dasselbe tust, passiert dasselbe.** Nur dann kannst du einen Fehler auslösen, eine Änderung machen und prüfen, ob er weg ist. Die Rückwärtsprobe aus Etappe 16 — *Änderung zurücknehmen, ist der Fehler wieder da?* — setzt voraus, dass er beim ersten Mal nicht zufällig da war.

**Zufall nimmt dir genau diese Voraussetzung.** Drei Dinge gehen verloren:

| Werkzeug | Warum es mit Zufall nicht mehr trägt |
|---|---|
| Die Tick-Tabelle aus 16 | Du rechnest eine Lage vor, und das Programm spielt eine andere |
| Die Rückwärtsprobe aus 16 | Ist der Fehler weg, weil du ihn behoben hast, oder weil diesmal kein Speier kam? |
| `diff` aus 7 | Zwei Läufe unterscheiden sich immer, auch ohne Fehler |

### 10. ⭐⭐ Der Seed

**Der Zufall in deinem Computer ist nicht zufällig.** `random` rechnet eine lange Folge von Zahlen aus, die zufällig *aussehen* — aber jede folgt aus der vorigen. Wo die Folge beginnt, entscheidet eine einzige Startzahl: der **Seed**.

Normalerweise nimmt Python eine Startzahl, die bei jedem Programmstart anders ist. **Mit `random.seed()` bestimmst du sie selbst:**

```python
import random

random.seed(7)
for i in range(5):
    print(random.randint(1, 6))
```

Diese fünf Würfe sind **bei jedem Start dieselben** — bei `seed(7)` sind es 3, 2, 4, 6, 1. Mit `seed(8)` sind es fünf andere, und auch die wieder jedes Mal. **Derselbe Seed, dieselbe Folge.** Ob daraus auch derselbe Lauf wird, klärt Konzept 11.

**Drei Regeln, und jede davon hat einen eigenen Fehler, wenn man sie bricht:**

1. **Einmal, am Anfang.** Bevor das Spiel zum ersten Mal für sich würfelt, und nie wieder. *(Die Zahl, die du übergibst, darf selbst gewürfelt sein — das ist Regel 3.)* Wer den Seed in die Wellenschleife schreibt, setzt die Folge vor jeder Welle auf denselben Anfang zurück — dann beginnt jede Welle mit denselben Würfen. Das stürzt nicht ab und fühlt sich nur seltsam an. *(Kaputtmachen 6.)* *(In Etappe 19 wird diese Regel genauer gefasst: Beim Speichern und beim Laden wird noch einmal gesät — mit einem neuen Seed, der im Spielstand steht, nie mit einem alten. Bis dahin gilt sie wörtlich.)*
2. **Ein fester Seed ist kein Spiel mehr.** Mit `random.seed(42)` im Code ist jedes Spiel gleich, für immer. Das ist zum Jagen eines Fehlers Gold und zum Spielen wertlos.
3. **Deshalb wird der Seed gezogen und angezeigt.** Normalerweise würfelt dein Spiel beim Start eine Startzahl, merkt sie sich, übergibt sie an `random.seed()` — und **zeigt sie an.** Siehst du einen Fehler, schreibst du die Zahl ab, trägst sie oben in deine Datei ein, und das Spiel läuft genauso noch einmal.

Die dritte Regel ist der eigentliche Gewinn. Aus *„manchmal stirbt ein Gegner zu früh"* wird: **„Bei Seed 48173 in Welle 14 stirbt der zweite Speier einen Takt zu früh."** Das ist der Unterschied zwischen einem Fehler, den man jagt, und einem, den man vorführt.

**Für den Schalter oben in der Datei brauchst du nichts Neues:** einen festen Wert, der entweder eine Zahl ist oder `None`. `None` heißt *„keine Vorgabe, zieh selbst"* — das ist `None` als bewusster Leerwert aus Etappe 10, geprüft mit `is None`.

### 11. 🧠 Was der Seed *nicht* festnagelt

**Der Seed legt die Folge fest. Nicht, wer wann eine Zahl daraus nimmt.**

**Stell dir den Zufall in deinem Spiel als Strom von Zahlen vor.** Jeder Zufallsaufruf nimmt die nächste. Zwei Läufe mit demselben Seed, im zweiten fällt ein Gegner weniger:

```
Folge aus Seed 48173:   Zahl 1 … Zahl 12   Zahl 13   Zahl 14   Zahl 15 …
Lauf A:                 Welle 8 erzeugen   Beute     Beute     Welle 9 erzeugen …
Lauf B:                 Welle 8 erzeugen   Beute     Welle 9 erzeugen …
```

In Lauf B beginnt Welle 9 eine Zahl früher — und ist deshalb eine andere Welle. Dieselbe Folge, anders verteilt. *(Wie viele Zahlen eine Welle verbraucht, hängt von ihrer Größe ab; die 12 ist nur ein Beispiel.)*

**Erstens: deine Eingaben.** Jeder Aufruf von `randint`, `choice` oder deiner `gewichtete_wahl` verbraucht die nächste Zahl der Folge. Deine Beute wird gezogen, wenn ein Gegner fällt — und **welcher Gegner wann fällt**, hängt davon ab, was du eintippst. Tippst du anders, fallen die Gegner in anderer Reihenfolge, und dieselben Zahlen der Folge landen bei **anderen** Gegnern: Die Beute liegt woanders, und vielleicht außerhalb deiner Zonen.

**Und wenn sich ändert, *wie viele* Zahlen verbraucht werden** — ein Gegner fällt gar nicht, eine Beute mehr wird gezogen —, dann verschiebt sich ab dieser Stelle **alles**: jede Beute danach, die Zusammensetzung der nächsten Welle — und ab 17c das Ereignis in der Pause. Ob das bei dir passieren kann, hängt davon ab, wie deine Wellen enden. **Die Faustregel, die immer gilt: Entscheidend ist nicht, was du tust, sondern wie viele Zahlen bis zu einer Stelle schon gezogen wurden.**

> **Derselbe Seed und dieselben Eingaben ergeben denselben Lauf. Derselbe Seed allein nicht.**

**Zweitens: Sets.** Die Reihenfolge, in der ein Set aus Strings seine Einträge herausgibt, kann sich **zwischen zwei Programmstarts** ändern — und der Seed ändert daran nichts, denn `random` hat damit nichts zu tun. Fremdes Beispiel:

```python
print({"Apfel", "Birne", "Kirsche"})
```

Dreimal gestartet, kann das dreimal in verschiedener Reihenfolge herauskommen. **Solange du über ein Set nur mit `in` fragst, ist das egal** — so ist es seit Etappe 15 Regel. **Gefährlich wird es, wenn du über ein Set läufst und dabei würfelst oder ausgibst — oder ein Set als Ganzes ausgibst**, etwa `welt.erkenntnisse` in deinem `__repr__`. Dann steht dein Lauf trotz festem Seed jedes Mal anders da. **Der Ausweg ist der aus Etappe 6, Schritt 10:** über etwas mit fester Reihenfolge laufen — eine Tabelle, ein Dictionary — und beim Set nur mit `in` fragen. Das ist auch der Grund für die Klammer in Schritt 6: Dein Generator läuft über `GEGNERTYPEN`, ein Dictionary — dessen Reihenfolge ist die, in der du es hingeschrieben hast.

*(Ein Verwandter aus derselben Familie: Ein Objekt ohne eigenes `__repr__` gibt sich als `<Fundstueck object at 0x7f…>` aus, und die Zahl hinter `0x` ist bei jedem Start eine andere. Wer so etwas ausgibt, bekommt ebenfalls einen redenden `diff`. Abhilfe: ein `__repr__`, Etappe 9.)*

### 12. Der Beweislauf — und warum der Debugger nicht mitspielt

**Wie beweist du, dass zwei Läufe gleich sind?** Mit dem Werkzeug aus Etappe 7: Eingaben aus einer Datei, Ausgabe in eine Datei, zwei Ausgabedateien vergleichen.

```
python spiel.py < befehle17.txt > lauf1.txt
python spiel.py < befehle17.txt > lauf2.txt
diff lauf1.txt lauf2.txt
```

Alles wie damals: Das Terminal steht im Projektordner. `lauf1.txt` und `lauf2.txt` **entstehen von selbst** und werden bei jedem Aufruf überschrieben. Am Ende der Befehlsdatei kommt ein `EOFError` im Terminal — **erwartet**, er landet nicht in der Ausgabedatei. Und wenn `diff` nichts ausgibt, sind die Läufe gleich. *(Unter Windows in der klassischen Eingabeaufforderung heißt das Werkzeug `fc`. Oder du legst beide Dateien im Editor nebeneinander.)*

**Mit festem Seed muss `diff` schweigen. Ohne Seed redet er.** Das ist der Beweis, dass dein Seed alles erfasst — und wenn `diff` trotz festem Seed redet, hast du einen Zufall gefunden, der an `random` vorbeiläuft. Konzept 11, zweiter Teil.

⚠️ **Und hier die Falle beim Kombinieren mit dem Breakpoint aus Etappe 8:** Der Debugger liest seine Befehle von derselben Stelle wie `input()`. Startest du mit `< befehle17.txt` und läuft das Programm in ein `breakpoint()`, **frisst der Debugger die nächsten Zeilen deiner Befehlsdatei** als Debugger-Befehle. Nichts stürzt ab — dein Lauf ist nur still ein anderer. **Bedingte Breakpoints also nie zusammen mit `<`.** Schritt 14 zeigt, wo die Kombination Seed plus Breakpoint trotzdem ihre volle Kraft hat.

---

## Dein Auftrag — Teil 17b

Nach **jedem** Schritt ausführen. Ab Schritt 11 ist dein Spiel wieder wiederholbar — **nutz das**: Wenn etwas seltsam aussieht, schreib den Seed ab.

---

### 11. ⭐ Zieh einen Seed und setz ihn

- **Ein fester Wert oben bei den anderen:** `SEED = None`. Ein Kommentar dahinter: `None` heißt, bei jedem Start einen neuen ziehen.
- **Die Welt bekommt ein Attribut `seed`**, Startwert `None`. Ein Wert, den es pro Spiel einmal gibt — und in Etappe 19 gehört er in den Spielstand.
- **Im Hauptprogramm, direkt nachdem die Welt angelegt ist und bevor die Wellenschleife beginnt:**
  - Ist `SEED` `None`? Dann einen ziehen, eine Zahl von 1 bis 99999. Sonst `SEED` nehmen.
  - Das Ergebnis in `welt.seed` ablegen.
  - `random.seed()` damit aufrufen. **Genau einmal im ganzen Programm** — gemeint ist der Aufruf, nicht der Zufall davor.

*(Einen Seed mit `random` zu ziehen, bevor `random.seed()` aufgerufen ist, ist kein Widerspruch: Bis dahin würfelt Python mit seiner eigenen, jedes Mal anderen Startzahl. Genau die willst du für die Wahl des Seeds.)*

**So prüfst du es:** Eine vorübergehende Zeile `print(welt.seed)` direkt danach, zweimal starten — zwei verschiedene Zahlen. Dann `SEED = 48173`, zweimal starten — zweimal 48173. **Danach `SEED` wieder auf `None` und die Prüfzeile weg** — Schritt 12 zeigt den Seed ab jetzt dauerhaft.

---

### 12. Zeig den Seed an

Am Anfang jeder Welle, vor der Ankündigung, eine Zeile:

```
[ Debug ]  Seed: 48173   Welle: 14
```

Der Wortlaut ist deiner, aber **Seed und Wellennummer stehen in derselben Zeile** — das sind die zwei Angaben, mit denen du eine Stelle im Spiel wiederfindest.

*(Das ist die erste Zeile deines Spiels, die ausdrücklich für den Entwickler da ist und nicht für den Spieler. In Etappe 20 bekommt diese Sorte Ausgabe einen eigenen Ort.)*

---

### 13. ⭐⭐ Mach den Beweislauf

**a) Leg eine neue Befehlsdatei `befehle17.txt` an.** Die aus Etappe 7 passt nicht mehr — dein Spiel stellt inzwischen andere Fragen und kennt andere Befehle. Das Format ist dasselbe: eine Zeile pro `input()`, in der Reihenfolge, in der dein Spiel fragt, von der Klassenwahl an. **Dreißig bis fünfzig Zeilen**, gemischt aus Befehlen, die Zeit kosten — so viele, dass mindestens eine Welle zu Ende geht.

*(Lass die Wellenschleife für den Beweislauf bei `8` beginnen. Ab dort ist schon die erste Welle zufällig zusammengesetzt, und du musst nicht sieben Wellen lang Befehle schreiben. **Schreib dir auf, dass sie auf `8` steht** — nach Schritt 13 kommt sie zurück auf `1`, und in Schritt 21 brauchst du die `8` noch einmal.)*

**b) Fester Seed, zwei Läufe.** `SEED` auf eine Zahl deiner Wahl, dann die drei Zeilen aus Konzept 12. **`diff` muss schweigen.**

Redet er, such die erste Zeile, in der die Dateien auseinandergehen. **Davor ist alles gleich, also steckt der Zufall, der an deinem Seed vorbeiläuft, zwischen der letzten gleichen und der ersten verschiedenen Zeile.** Verdächtig ist alles, was über ein Set läuft oder ein Set ausgibt, und jede Ausgabe mit `0x…` darin — Konzept 11, mit dem Ausweg dort.

**c) Ohne Seed, zwei Läufe.** `SEED = None`, dieselben Befehle, noch einmal zwei Läufe. `diff` redet — schon in der Debug-Zeile, aber sieh weiter: **Wo unterscheidet sich das Spiel selbst zum ersten Mal?**

**d) Fester Seed, eine Eingabe anders.** Denselben Seed wie in b), aber in `befehle17.txt` einen Schuss in der ersten Welle gegen einen anderen Befehl tauschen, der ebenfalls Zeit kostet. Ein Lauf in `lauf3.txt`, `diff` gegen `lauf1.txt`. **Drei Fragen:** Ab wo unterscheiden sich die Läufe? Liegt die Beute noch da, wo sie im ersten Lauf lag? **Und ist die nächste Welle gleich zusammengesetzt oder nicht — und warum?** Die Antwort auf die letzte Frage steht in Konzept 11, zweiter Absatz: Zähl, wie viele Beutezüge bis zum Wellenende in beiden Läufen stattgefunden haben. *(Ist im Spielgeschehen gar nichts anders, hat der fehlende Schuss keinen Gegner früher oder später fallen lassen. Tausch einen, der getroffen hat.)*

**Schreib in `GELERNT.md`, was b), c) und d) ergeben haben.** Ein Satz pro Lauf.

*(`lauf1.txt`, `lauf2.txt` und so weiter sind Wegwerf-Dateien — vor dem Commit löschen. `befehle17.txt` darfst du behalten.)*

---

### 14. ⭐ Führ eine Welle vor — mit Seed und bedingtem Breakpoint

**a) In der Probedatei** — frisch kopiert, wie in Schritt 4. Dort gibt es keine Eingaben, die dem Debugger in die Quere kommen.

- Ganz unten: `random.seed()` mit einer festen Zahl deiner Wahl.
- Darunter eine Schleife über die Wellen 1 bis 20, die für jede Welle `erzeuge_welle()` aufruft und die Liste unter einem Namen ablegt. Als letzte Welle übergibst du `20` — dein `wellen_bis_evakuierung` ist beim Kopieren vielleicht mit dem Hauptprogramm verschwunden.
- Direkt unter dieser Zeile, noch in der Schleife, der bedingte Breakpoint aus Etappe 8: anhalten, **wenn die Welle 14 ist.**

Starten. Am Debugger-Prompt die Liste mit `p` ansehen, dann mit `c` weiterlaufen lassen. **Zweimal starten — zweimal dieselbe Welle 14.** Dann den Seed ändern: eine andere Welle 14, und auch die jedes Mal.

**Das ist die Kombination, die Etappe 8 und 16 versprochen haben:** Du springst direkt in die Welle, in der etwas nicht stimmt, und sie ist jedes Mal dieselbe.

⚠️ **Eine ehrliche Einschränkung, die du verstehen sollst:** Die Welle 14 aus deiner Probedatei ist **nicht** die Welle 14 aus deinem Spiel mit demselben Seed. Das Spiel zieht zwischen den Wellen noch Beute — ab 17c auch Ereignisse — und verbraucht damit Zahlen der Folge, die Probedatei nicht. **Wiederholbar ist, was mit demselben Seed denselben Weg nimmt** — Konzept 11. Schreib den Satz in `GELERNT.md`, mit deinen eigenen Worten.

**b) Im Spiel — von Hand.** Jetzt dieselbe Kombination dort, wo die Fehler wirklich passieren:

- `SEED` auf eine feste Zahl, die Wellenschleife testweise bei `13` beginnen lassen.
- Am Anfang jeder Welle, direkt nach dem Erzeugen, der bedingte Breakpoint: anhalten, wenn `welt.welle` 14 ist.
- **Ohne `<` starten** — Konzept 12 — und Welle 13 von Hand durchspielen. Am Breakpoint die Namensliste mit `p` ansehen.
- Noch einmal, mit denselben Befehlen. **Steht dieselbe Welle 14 da?** Wenn ja: Du kannst ab jetzt jede Welle, in der dir etwas auffällt, gezielt wieder ansteuern. Wenn nein: Zähl mit Konzept 11 nach, ob in beiden Durchgängen gleich viele Zahlen gezogen wurden.

**c) Aufräumen und commit.**

- Breakpoint raus, `SEED` auf `None`, Wellenschleife beginnt wieder bei `1`.
- Keine `probe.py`, keine `lauf*.txt` im Ordner. `befehle17.txt` bleibt — du brauchst sie in 17c noch einmal.
- Die Abschnitte am Ende, die zu 17b gehören: **die Leseübung** und **Kaputtmachen 6**.

Commit: `Etappe 17b: Reproduzierbarer Zufall`

---

## Selbsttest — 17b

- [ ] Zwei Starts mit `SEED = None` zeigen zwei verschiedene Seeds in der Debug-Zeile.
- [ ] `random.seed()` steht **genau einmal** in `spiel.py`.
- [ ] ⭐ **Zwei Beweisläufe mit festem Seed und derselben Befehlsdatei: `diff` schweigt.**
- [ ] Du kannst sagen, was Lauf d) aus Schritt 13 gezeigt hat — und warum.
- [ ] In der Probedatei hält der bedingte Breakpoint zweimal hintereinander bei derselben Welle 14.
- [ ] Der Satz aus Schritt 14 a) steht in deinen Worten in `GELERNT.md`.

> **⏸ Ende von 17b.** Dein Zufall ist festgenagelt, sichtbar und bewiesen. 17c nutzt ihn für das, was zwischen zwei Wellen passiert.

---

# Teil 17c — Zwischen den Wellen

## Worum es geht

Dein Spiel würfelt, und du kannst den Würfel festhalten. Jetzt nutzt du ihn.

**Zwischen den Wellen passiert etwas:** Nachschub, ein Generatorausfall, ein Riss in der Kuppel. Deine Kameraden melden sich mit dem, was sie in der Welle geschafft haben — jeder auf seine Art. Und einmal im Spiel kommt Funkkontakt, mit einer Aufzeichnung, die du am ersten Tag geschrieben hast.

Technisch ist wenig davon neu. Das Ziehen kann `gewichtete_wahl` seit 17a, das Zählen kennst du aus Etappe 13, die Stimmen sind Vererbung aus Etappe 11. **Neu sind zwei Fragen:** Welche Meldung muss sofort auf den Bildschirm, und welche darf warten? Und in welcher Form stellt man Bedingungen, wenn mehrere gleichzeitig stimmen können? Dazu kommt, dass zwischen zwei Wellen plötzlich so viel passiert, dass die **Reihenfolge** eine Entscheidung wird — wie beim Tick in Etappe 16.

---

## Der lange Bogen — was heute fällig wird

- ⭐⭐ **`letzte_meldung` aus Etappe 1.** Du hast sie am ersten Tag angelegt, als Satz in einer Variable, und sie hat vier Monate lang nichts getan. **Heute bekommt sie ihren Auftritt.** Etappe 1 hat dir den Satz schon verraten, der dazugehört: *„Die Aufzeichnung läuft immer noch. Sie ist von vor achtzehn Tagen."*
- **`meldung_abgesetzt` aus Etappe 2.** Deine Funkentscheidung beim ersten Kontakt wirkt ab heute mit: Wer gemeldet hat, bekommt häufiger Nachschub.
- **`elif` gegen mehrere `if` aus Etappe 2, Konzept 4.** Damals hieß es: *„Diese Unterscheidung kommt in Etappe 17 zurück, wenn mehrere Ereignisse gleichzeitig zutreffen können. Wer dort eine Kette baut, verliert Ereignisse."* Heute brauchst du beide Formen an zwei aufeinanderfolgenden Stellen.
- **`kern_integritaet` aus Etappe 1** wird zum ersten Mal mit ihrem Startwert verglichen.
- **`welt.melde()` aus Etappe 13.** Dort stand: *„In Etappe 17 wird genau daraus die Meldungsliste zwischen den Wellen."* Heute.
- **`abschuesse` aus Etappe 12.** Ein Zähler ohne Wirkung, seit fünf Etappen. Heute wird daraus ein Satz, den ein Kamerad sagt — jeder mit der Stimme seiner Klasse aus Etappe 11.
- **Zustand gegen Ereignis aus Etappe 13** — diesmal nicht in einem Takt, sondern zwischen zwei Wellen.
- **Zwei offene Fragen aus Etappe 13:** Was tut der Trupp, während du ausgefallen bist? Und kann ein Kamerad endgültig fallen? Beide werden heute entschieden — siehe unten.
- **Die Landeplattform aus Etappe 13.** Seit sie freigeräumt ist, wartet sie auf etwas. Heute landet dort das Evakuierungsschiff.

---

## Zwei Design-Entscheidungen, die der Plan für dich trifft

### Was tut der Trupp, während du ausgefallen bist?

**Er kämpft weiter.** Das tut er seit Etappe 13 ohnehin — der Tick läuft, die Kameraden handeln. Was fehlt, ist, dass du es erfährst. **Ab heute steht es im Wellenbericht:** Wer in dieser Welle wie viele Gegner erledigt hat. Wenn du zwölf Takte ausgefallen warst und Vasquez in der Zeit vier Kriecher geschafft hat, liest du das am Ende der Welle — und merkst zum ersten Mal, dass dein Trupp dich gerade getragen hat.

### Kann ein Kamerad endgültig fallen?

**Nein — heute nicht.** Ein Kamerad fällt aus und steht nach seinem Zähler wieder auf, wie seit Etappe 13. Der Grund ist kein technischer: **Mit zufälligen Wellen kann eine einzige schlechte Welle einen Kameraden kosten, ohne dass du etwas falsch gemacht hast.** Das ist genau die Grenze, nach der die Entwicklerfrage dieser Etappe fragt. Endgültiger Verlust gehört zu einer Stelle, die man **neu besetzen** kann — den Rekruten und Söldnern aus Etappe 22.

---

## Die Konzepte — Teil 17c

### 13. ⭐ Sofort oder gesammelt?

Seit Etappe 13 gibt es in deinem Spiel **einen** Ort, an dem entschieden wird, wie eine Meldung erscheint: `welt.melde()`. Dort stand: *„Willst du morgen … die letzten fünf Meldungen gesammelt statt einzeln — du änderst eine Methode statt dreißig `print`-Aufrufe."* **Heute ist morgen.**

**Nicht jede Meldung gehört sofort auf den Bildschirm.** Die Frage, die entscheidet:

> **Muss der Spieler jetzt etwas tun?**

| Sofort | Gesammelt, für den Wellenbericht |
|---|---|
| *„Fähigkeit wieder bereit."* — du willst sie einsetzen | *„Vasquez ist aufgestiegen."* — schön, aber du tust deshalb nichts anders |
| *„Du bist ausgefallen."* | *„Turm hat einen Speier erledigt."* |
| *„Ein Gegner hat das Tor erreicht."* | |

Gesammelt wird in einer Liste an der Welt. Am Ende der Welle wird sie ausgegeben — **und danach geleert.** Wer das Leeren vergisst, liest in Welle 10 die Meldungen aus neun Wellen noch einmal.

**Offen ist nur noch, wie eine Meldung in diese Liste kommt — und hier entscheidest du.** Zwei Wege, beide mit Werkzeugen, die du hast:

| | A — eine zweite Methode | B — ein Standardargument |
|---|---|---|
| Wie | Die Welt bekommt neben `melde(text)` eine Methode `notiere(text)`, die nur sammelt | `melde` bekommt einen zweiten Parameter mit Standardwert — das „erweitern, ohne alte Aufrufe zu brechen" aus Etappe 7, Konzept 6 |
| Ein Aufruf, der sammelt | `welt.notiere("…")` | `welt.melde("…", False)` |
| Was man beim Lesen sieht | sofort, dass gesammelt wird — der Name sagt es | ein nacktes `False`, dessen Bedeutung man in `melde` nachschlagen muss |
| Bestehende Aufrufe | bleiben, wie sie sind | bleiben, wie sie sind — sie bekommen den Standardwert |
| Kommt eine dritte Sorte dazu, etwa „nur für den Entwickler" | eine dritte Methode | ein Parameter, der mehr als zwei Werte kennen muss |

**Beide sind richtig**, und Schritt 16 beschreibt beide. Wähl einen und schreib in `GELERNT.md`, warum. In Etappe 20 bekommen Meldungen getrennte Wege — dann siehst du, welche Bauart sich leichter erweitern ließ.

### 14. ⭐⭐ Viele Bedingungen, ein Ereignis

Zwischen zwei Wellen soll **ein** Ereignis passieren, gezogen nach Gewicht. Aber nicht jedes Ereignis ist immer möglich: Ein Generatorausfall ohne Turm hat nichts auszufallen. Funkkontakt soll nur einmal im Spiel kommen.

**Das sind zwei verschiedene Fragen, und jede braucht eine andere Form:**

**Welche Ereignisse sind möglich?** Das prüfst du für jedes Ereignis **unabhängig**. Es kann gleichzeitig ein Turm stehen **und** der Kern unter der Hälfte sein **und** Funkkontakt noch ausstehen. Alle drei gehören dann in den Topf. **Das sind einzelne `if`.**

**Was passiert beim gezogenen Ereignis?** Gezogen ist genau eines. Die Fälle schließen sich aus. **Das ist eine `elif`-Kette.**

Genau das ist die Frage aus Etappe 2, Konzept 4 — *„Schließen sich diese Fälle gegenseitig aus?"* —, und die Antwort ist hier zweimal verschieden, in zwei Blöcken direkt hintereinander.

> **Beim Füllen des Topfes darf nichts verloren gehen. Beim Ausführen gewinnt genau eines.**

**Fremdes Beispiel, falsch gebaut.** Ein Planer für den Sonntagnachmittag:

```python
moeglich = {"Spaziergang": 5}
if sonne:
    moeglich["Freibad"] = 4
elif flohmarkt_offen:
    moeglich["Flohmarkt"] = 3
```

Sonniger Sonntag, Flohmarkt offen — was steht im Topf? **Der Flohmarkt fehlt.** Kein Fehler, keine Meldung, nur ein Ausflug, der an sonnigen Tagen nie gezogen werden kann. Du merkst es erst nach Wochen, wenn überhaupt. **Das ist der verlorene Fall, vor dem Etappe 2 gewarnt hat.**

*(Der Topf ist übrigens dasselbe wie das Bezahlbare aus Konzept 5: ein Dictionary Name → Gewicht, das vor jedem Zug frisch gebaut wird und dann an `gewichtete_wahl` geht. Dritte Anwendung, dieselbe Funktion.)*

### 15. Einheiten bekommen eine Stimme

Seit Etappe 12 zählt jede Einheit ihre `abschuesse`. **Für den Wellenbericht brauchst du aber nicht die Summe seit Spielbeginn, sondern die dieser Welle.**

Das ist das Muster aus Etappe 13, Konzept 4: **merken, neu berechnen, vergleichen.** Zu Beginn der Welle merkt sich jede Einheit ihren Stand. Am Ende ist die Differenz das, was sie in dieser Welle geschafft hat.

**Wo merkt sie es sich?** An sich selbst, als Attribut mit Startwert 0 in `Einheit`. Das hat einen Vorteil, der sich erst zeigt, wenn etwas schiefgeht: **Eine Einheit, die mitten in der Welle neu entsteht** — ein neu gebauter Turm —, hat ihren Merkwert von Geburt an, und die Differenz stimmt trotzdem. Ein Dictionary *Name → Stand*, einmal zu Wellenbeginn gefüllt, kennt sie nicht und wirft dir einen `KeyError`.

**Und dann bekommen die Zahlen eine Stimme — und zwar nicht eine für alle.** Ein Heavy klingt anders als ein Medic, und ein Turm klingt nach gar nichts. Wie macht man das, ohne dass der Bericht fragt, wer gerade spricht?

**Mit dem Werkzeug aus Etappe 11, Konzept 8: eine Methode in der Basisklasse, überschrieben in den Kindern.**

- `Einheit` bekommt eine Methode, die zu einer Anzahl einen nüchternen Satz **zurückgibt** — Name und Zahl. Das ist die Stimme für alles, was keine eigene hat.
- Jede Marine-Klasse überschreibt sie mit eigenen Sätzen.
- Der Bericht läuft über den Trupp und ruft bei jeder Einheit dieselbe Methode auf. **Wer antwortet, entscheidet das Objekt** — der Satz aus Etappe 13, Konzept 9: *Der Tick fragt nie, was etwas ist. Er ruft auf, und das Objekt weiß Bescheid.* Heute gilt er für den Bericht.

**Innerhalb einer Stimme** unterscheiden sich die Sätze nach der Zahl. Drei Fälle, die sich ausschließen — eine `elif`-Kette:

| Abschüsse in der Welle | Zum Beispiel, für einen Heavy |
|---|---|
| 0 | *„Vasquez: 0. Das MG ist nicht mal warm geworden."* |
| 1 oder 2 | *„Vasquez: 2. Hätten mehr sein können."* |
| 3 oder mehr | *„Vasquez: 4. Das Nordtor hält."* |

**Die Methode gibt den Satz zurück, sie gibt ihn nicht aus.** Ausgegeben wird er im Bericht, über `melde` — so bleibt `melde` der eine Ort, an dem dein Spiel spricht.

**Schreib deine eigenen Sätze** — und zwar so, dass du nach zehn Wellen an einem Satz erkennst, wer ihn gesagt hat, auch ohne den Namen davor. Das ist die zweite Stelle nach den langen Gegnertexten in Etappe 6, an der dein Spiel billig Atmosphäre bekommt — und nach zehn Wellen ist Vasquez keine Zeile mehr, sondern jemand.

### 16. Ein Zähler, der in Wellen zählt

Der Generatorausfall soll deinen Turm **für zwei Wellen** schwächen. Das ist das Zähler-Muster aus Etappe 13, Konzept 1, unverändert — **mit einer anderen Uhr.** Es zählt nicht pro Takt herunter, sondern einmal pro Wellenende.

**Und damit stellt sich die Frage aus Etappe 13, Schritt 7, noch einmal:** Was bedeutet die Zahl 2 genau? Welche Wellen sind betroffen — die nächsten zwei, oder die laufende und die nächste? **Das hängt davon ab, an welcher Stelle zwischen den Wellen der Zähler heruntergezählt wird** und an welcher der Ausfall gesetzt wird. Leg es fest, bevor du baust, und prüf es nachher.

**Und wieder Zustand gegen Ereignis, Etappe 13, Konzept 2:**

| | Wo es steht | Wer es liest |
|---|---|---|
| **Zustand:** *„Der Generator ist aus."* | der Zähler ist größer als 0 | der Turm, bei jedem Schuss |
| **Ereignis:** *„Der Generator fällt aus."* | das gezogene Ereignis | eine Meldung, einmal |
| **Ereignis:** *„Der Generator läuft wieder."* | der Zähler ist **gerade** auf 0 gekommen | eine Meldung, einmal — innerhalb des `> 0`-Blocks |

---

## Dein Auftrag — Teil 17c

Nach **jedem** Schritt ausführen und eine Welle spielen. Wenn dir dabei etwas seltsam vorkommt: Seed aus der Debug-Zeile abschreiben — seit 17b kannst du die Stelle wieder ansteuern.

---

### 15. Zieh die Werte vom ersten Tag in die Welt

Ereignisse brauchen gleich Werte, die bisher lose in deinem Programm liegen. **Was es pro Spiel einmal gibt, gehört in die Welt** — die Regel aus Etappe 12. Die `Welt` bekommt in ihrem `__init__` diese Attribute:

| Attribut | Startwert | Was drinsteht |
|---|---|---|
| `letzte_meldung` | `""` | der Text aus Etappe 1 |
| `meldung_abgesetzt` | `False` | die Funkentscheidung aus Etappe 2 |
| `funk_gehoert` | `False` | ob der Funkkontakt schon kam |
| `generatorausfall` | `0` | wie viele Wellen der Ausfall noch dauert |
| `bericht` | `[]` | die gesammelten Meldungen der laufenden Welle |

*(`seed` hat die Welt seit Schritt 11.)*

**Und jetzt der Handgriff, den kein Register beantwortet: Wann bekommen die ersten beiden ihre echten Werte?** Such in deinem Programm die Stellen, an denen `letzte_meldung` und `meldung_abgesetzt` entstehen, und vergleich sie mit der Stelle, an der die Welt angelegt wird:

| Die lose Variable entsteht … | Dann |
|---|---|
| **vor** der Welt — das Briefing aus Etappe 1 läuft, bevor es eine Welt gibt | Direkt nachdem die Welt angelegt ist, den Wert ans Attribut übergeben. Die lose Variable bleibt für das, was **vor** der Welt passiert; danach liest niemand mehr sie. |
| **nach** der Welt — etwa, wenn die Funkentscheidung erst beim ersten Kontakt in Welle 1 fällt | Die Antwort **direkt** in das Attribut schreiben, und die lose Variable löschen. |
| **schon an der Welt** — weil du sie in Etappe 12, Schritt 3, mit den anderen Werten pro Spiel umgezogen hast | Nur prüfen, dass Name und Startwert zur Tabelle oben passen. |

**So prüfst du es:** `print(welt)` aus Etappe 12 zu Beginn von Welle 2. Beide Werte stehen darin — wenn dein `__repr__` sie zeigt. Tut er es nicht, ist das der Moment, ihn zu ergänzen.

---

### 16. ⭐ Bring der Welt das Sammeln bei

Nach deiner Wahl aus Konzept 13:

| | Was du baust |
|---|---|
| **Weg A** | Eine neue Methode der Welt, `notiere(text)`, die den Text an `self.bericht` anhängt. `melde` bleibt, wie sie ist. |
| **Weg B** | `melde` bekommt einen zweiten Parameter, `sofort`, mit dem Standardwert `True`. Ist `sofort` wahr: ausgeben wie bisher. Sonst: den Text an `self.bericht` anhängen. |

**In beiden Fällen wird kein bestehender Aufruf angefasst** — außer denen, die du gleich bewusst umstellst.

Dann entscheide nach Konzept 13, **welche deiner bestehenden Meldungen in den Bericht gehören.** Mindestens zwei, und eine davon steht fest: **die Meldung aus der Einsammelphase, wie viel liegen blieb** (Etappe 15, Schritt 5). Sie ist die typische Berichtszeile — wichtig, aber nichts, worauf du jetzt reagieren musst. Diese Aufrufe werden zu `welt.notiere(...)` (Weg A) oder bekommen `False` als zweites Argument (Weg B). Schreib in `GELERNT.md`, welche es sind und nach welcher Frage du entschieden hast.

*(Und falls deine Einsammelphase noch mit `print()` statt `welt.melde()` meldet: Das ist jetzt der Moment, sie umzustellen.)*

**So prüfst du es:** Eine Welle spielen, in der eine der umgestellten Meldungen fällig wird. Sie erscheint **nicht** mitten im Kampf — und `print(welt.bericht)` nach der Welle zeigt sie. *(Ausgegeben wird der Bericht erst in Schritt 17.)*

---

### 17. ⭐⭐ Bau den Wellenbericht — mit Stimmen

**Eine Methode der Welt, `wellenbericht()`**, aufgerufen einmal nach jeder Welle, **direkt nach dem Einsammeln.** Warum genau dort, fragt Schritt 20. Sie gibt alles über `self.melde()` aus, wie jede andere Meldung, die sofort erscheinen soll.

**Zuerst die Abschüsse der Welle, nach Konzept 15:**

- `Einheit` bekommt ein Attribut `abschuesse_bei_wellenbeginn`, Startwert `0`.
- **Am Anfang jeder Welle**, im Hauptprogramm: Für jede Einheit in `welt.trupp` den aktuellen Stand von `abschuesse` in dieses Attribut übernehmen.

**Dann die Stimmen:**

- `Einheit` bekommt eine Methode `funkspruch(anzahl)`, die einen **String zurückgibt**: Name und Zahl, nüchtern, etwa *„Basisturm: 2 Abschüsse."* Ein Satz für alle Fälle reicht hier. Das ist die Stimme des Basisturms — und von allem, was keine eigene hat.
- **Jede der vier Marine-Klassen aus Etappe 11 — `Soldat`, `Heavy`, `Engineer`, `Medic` — überschreibt `funkspruch`** mit eigenen Sätzen, nach den drei Fällen aus Konzept 15. Die Zahl steht im f-String mit drin. **Jeder Zweig endet mit einem `return`** — ein Zweig ohne gibt `None` zurück, und im Bericht steht dann `None`.
- **Im Bericht:** Für jede Einheit in `welt.trupp` die Differenz ausrechnen, `funkspruch()` damit aufrufen und das Ergebnis über `self.melde()` ausgeben. **Keine Typabfrage, wer spricht.** Der Bericht ruft auf, das Objekt weiß Bescheid.

**Dann alles, was in dieser Welle gesammelt wurde:** jeder Eintrag aus `self.bericht`, einer pro Zeile. **Danach die Liste leeren** — mit einer Zuweisung einer neuen, leeren Liste an `self.bericht`, **nach** der Schleife. Einträge einzeln herauszulöschen, während du darüber läufst, überspringt jeden zweiten — Etappe 12, Konzept 11.

**Dann die Lage.** Mehrere dieser Zeilen können gleichzeitig zutreffen — Konzept 14, also einzelne `if`:

- **Immer:** der Kern in Prozent seines Startwerts. Dafür braucht der Startwert einen Namen: `KERN_START = 100` zu deinen festen Werten, und `Welt.__init__` benutzt ihn statt der nackten `100`. **Steht die `100` auch noch als Obergrenze in deinem Kern-Balken aus Etappe 3c, ersetz sie dort ebenfalls** — sonst gibt es zwei Wahrheiten über dieselbe Zahl. Die Prozentzahl bekommst du mit `*` und `//` aus Etappe 3c.
- **Wenn der Kern unter der Hälfte ist:** eine Warnung in deinen Worten.
- **Für jede Einheit, die gerade ausgefallen ist:** eine Zeile, wie viele Takte ihr noch fehlen. `status` und `ausfallzeit` hat jede Einheit seit Etappe 12 und 13.

```
—— Bericht nach Welle 6 ——
Du: 5. Hier kommt keiner durch.
Vasquez: 3. Das Nordtor hält.
Okafor: 0. Hab verbunden, nicht geschossen.
Basisturm: 2 Abschüsse.
Zwei Fundstücke außerhalb der Zonen zurückgelassen.
Vasquez ist auf Stufe 3 aufgestiegen.
Kern: 64 %.
Okafor liegt noch — 4 Takte.
```

*(Das Beispiel zeigt nur die Form. Deine Sätze, deine Reihenfolge — aber jede der drei Sorten muss vorkommen.)*

**So prüfst du es:** Eine Welle spielen, in der du selbst ausfällst. **Die Abschüsse deiner Kameraden aus der Zeit, in der du lagst, stehen im Bericht.** Mindestens zwei Kameraden klingen verschieden. Danach eine zweite Welle: Der Bericht zeigt nur die Abschüsse **dieser** Welle, nicht die Summe. Und kein Eintrag aus der ersten Welle taucht noch einmal auf.

> **⏸ Guter Schnitt.** Der Bericht steht, dein Trupp hat Stimmen. Die Ereignisse sind ein eigener Abend.

---

### 18. ⭐⭐ Bau den Ereignistopf

**Eine Methode der Welt, `moegliche_ereignisse()`**, die ein Dictionary *Kennung → Gewicht* zurückgibt — gebaut nach Konzept 14, **mit einzelnen `if`**:

| Kennung | Gewicht | Kommt in den Topf, wenn … |
|---|---|---|
| `"ruhe"` | 30 | immer |
| `"nachschub"` | 20 — **40**, wenn `meldung_abgesetzt` wahr ist | immer |
| `"generatorausfall"` | 15 | ein Turm steht **und** kein Ausfall mehr läuft |
| `"riss"` | 20 | der Kern unter der Hälfte von `KERN_START` ist |
| `"funkkontakt"` | 15 | er noch nicht kam **und** die Welle mindestens 5 ist |

*(Die Nachschub-Zeile ist die Wirkung deiner Funkentscheidung aus Etappe 2: Wer das Ungewöhnliche gemeldet hat, ist beim Kommando auf dem Schirm. Eine Zahl, und eine Entscheidung vom ersten Abend hat Folgen.)*

**So prüfst du es:** In einer frisch kopierten Probedatei eine Welt mit einem Marine anlegen, wie du es seit Etappe 12 kennst, Werte von Hand setzen und `print(welt.moegliche_ereignisse())`. **Drei Lagen:** ohne Turm bei vollem Kern · mit Turm, Kern bei 40 · mit Turm, Kern bei 40, Welle 6, Funk noch ausstehend. **In der dritten Lage stehen alle fünf im Topf.** Fehlt einer, hast du irgendwo ein `elif`. **Und die Grenze, wie in Etappe 16:** Kern bei **genau** der Hälfte von `KERN_START` — dann steht kein Riss im Topf, denn „unter der Hälfte" heißt `<`. Die Warnung im Bericht aus Schritt 17 muss dieselbe Grenze haben.

---

### 19. ⭐⭐ Bau die Ereignisse

**Eine Methode der Welt, `ereignis()`:** holt den Topf, zieht mit `gewichtete_wahl`, führt das Gezogene aus — **mit einer `elif`-Kette**, denn gezogen ist genau eines. Jedes Ereignis meldet sich über `self.melde()`, sofort.

*(Und der Fehlerzweig? `gewichtete_wahl` liefert hier nur `None`, wenn jedes Gewicht im Topf 0 ist — mit `"ruhe"` bei 30 passiert das nie. Wenn doch, passt kein Zweig der Kette, und es passiert nichts. Genau das Richtige, ohne eine Zeile dafür.)*

| Kennung | Was passiert |
|---|---|
| `"ruhe"` | Eine Zeile Stimmung, sonst nichts. *„Draußen ist es still. Zu still."* — Hast du in der Kür von Etappe 1 Sinnesvariablen angelegt, Temperatur, Geräusch, Notbeleuchtung: Hier ist ihr Ort. |
| `"nachschub"` | Ein Versorgungsabwurf: 20 Schuss in `vorrat["munition"]` deines Helden |
| `"generatorausfall"` | `generatorausfall` auf `2`. Dein Turm schießt ab jetzt mit halbem Schaden |
| `"riss"` | Die Kuppel reißt weiter: `kern_integritaet` sinkt um 5 — prüf, dass deine Verlustbedingung auch greift, wenn der Kern **zwischen** zwei Wellen auf 0 fällt |
| `"funkkontakt"` | siehe unten |

**Der Funkkontakt ist der Grund für diesen Schritt.** Er spielt zuerst deine `letzte_meldung` ab — die aus Etappe 1, unverändert, so wie sie in `GELERNT.md` steht. Dann einen Moment Stille, etwa als Zeile mit drei Punkten. *(Kein `input()` als Pause: Jede zusätzliche Eingabe verschiebt deine `befehle17.txt` um eine Zeile.)* Dann:

> *„Die Aufzeichnung läuft immer noch. Sie ist von vor achtzehn Tagen."*

Dieser Satz ist gesetzt; was du davor und danach schreibst, ist deins. **Und danach `funk_gehoert` auf `True`**, sonst kommt die Aufzeichnung in der nächsten Pause wieder und verliert alles, was sie beim ersten Mal hatte.

**Der halbe Schaden des Turms:** Such die Stelle, an der dein `Basisturm` seinen Schaden bestimmt — seit Etappe 13 in seiner Methode, die den Tick mitmacht, oder in deiner Schadensberechnung, je nachdem, wie du Etappe 15, Schritt 9, entschieden hast. Ist `generatorausfall` der Welt größer als 0, wird der Schaden mit `//` halbiert. **Den gespeicherten Schadenswert des Turms fasst du dabei nicht an** — du halbierst, was er in diesem Schuss austeilt. Sonst ist der Turm nach dem Ausfall für immer halb so stark.

**Und das Ende des Ausfalls, nach Konzept 16:** Direkt nach dem Wellenbericht zählt eine Stelle `generatorausfall` nach dem Zähler-Muster herunter und meldet, wenn er **gerade** auf 0 gekommen ist: *„Der Generator läuft wieder."* **Erst danach** kommt der Aufruf von `ereignis()`. **Sag voraus, wie viele Wellen der Turm mit dieser Reihenfolge halbiert schießt — mit einer kleinen Tabelle in `GELERNT.md`, wie die Tick-Tabelle aus Etappe 16.** Angenommen, der Ausfall wird in der Pause nach Welle 5 gezogen:

| Pause nach Welle | `generatorausfall` vorher | Was in dieser Pause passiert | `generatorausfall` danach | Nächste Welle halbiert? |
|---|---|---|---|---|
| 5 | 0 | | | |
| 6 | | | | |
| 7 | | | | |

Füll sie aus, bevor du spielst. Schritt 20 fragt, warum die Reihenfolge das Ergebnis bestimmt.

**So prüfst du es:** Setz in `moegliche_ereignisse()` testweise alle Gewichte außer einem auf 0 und spiel, bis das Ereignis kommt — für jedes der fünf einmal. *(Ein Gewicht von 0 wird nie gezogen. Warum, ist Lernziel 2.)* Für den Generatorausfall: **Zähl die Wellen, in denen der Turm halbiert schießt.** Es müssen genau so viele sein, wie du vorausgesagt hast. Danach alle Gewichte zurück.

---

### 20. ⭐ Ordne die Pause zwischen den Wellen

Du hast heute vier neue Dinge, die zwischen zwei Wellen passieren. **Ihre Reihenfolge ist eine Entscheidung, keine Nebensache** — die Lehre aus Etappe 16. Der Plan legt sie so fest:

```
… letzter Tick der Welle: Zähler → Trupp → Gegner → Aufräumen
Welle vorbei
→ Einsammeln                          (Etappe 15)
→ Wellenbericht                       (Schritt 17)
→ Generatorausfall herunterzählen     (Schritt 19)
→ Ereignis ziehen und ausführen       (Schritt 19)
nächste Welle
→ Debug-Zeile                         (Schritt 12)
→ Welle erzeugen                      (Schritt 7)
→ Abschüsse merken                    (Schritt 17)
→ Ankündigung mit Vorwissen           (Schritt 8)
```

**Vergleich die Liste mit deinem Code** — die ersten vier Punkte nach der Welle hast du in den Schritten 17 und 19 schon so gebaut. **Dann zwei Fragen, schriftlich:**

1. Warum steht der Bericht **nach** dem Einsammeln? *(Wo landet sonst die Meldung, wie viel liegen blieb — die aus Schritt 16?)*
2. Warum wird der Ausfall **vor** dem Ereignis heruntergezählt? *(Was passiert mit einem Ausfall, der gerade gezogen wurde, wenn es umgekehrt ist?)*

**Nach der letzten Welle kein Ereignis mehr.** Dann kommt die Evakuierung — und dein Spielende nennt ab heute den Ort, an dem sie passiert: **Das Schiff landet auf der Landeplattform**, die du in Etappe 13 freigeräumt hast. Ein Satz in deiner Siegmeldung.

**Trag die neue Reihenfolge in `GELERNT.md` ein**, neben die Tick-Reihenfolge aus Etappe 16.

**So prüfst du es:** Drei Wellen spielen und die Ausgabe zwischen zwei Wellen mit der Liste oben vergleichen, Zeile für Zeile — wie die Tick-Tabelle aus Etappe 16.

---

### 21. Prüf, dass das Alte noch läuft, und commit

- Alles aus Schritt 10 noch einmal.
- **Der Beweislauf aus Schritt 13 b) noch einmal**, mit allem, was seitdem dazugekommen ist — Wellenschleife dafür wieder bei `8`, fester Seed. **`diff` muss weiterhin schweigen.** Wenn nicht: In 17c ist etwas dazugekommen, das an deinem Seed vorbeiläuft — Konzept 11 sagt, wo du suchst.
- `SEED` steht auf `None`, die Wellenschleife beginnt wieder bei `1`, alle Ereignisgewichte stehen auf ihren Werten aus Schritt 18.
- Keine `lauf*.txt`, keine `probe.py`, kein `breakpoint()` im Ordner.
- Die Abschnitte am Ende, die zu 17c gehören: **Kaputtmachen 7** und **die Entwicklerfrage**.

Commit: `Etappe 17c: Bericht und Ereignisse zwischen den Wellen`

---

### 22. ⭐ Kür: Ein Sektor fällt endgültig

**Nur, wenn du in Etappe 5 die Kür gebaut hast, in der Sektoren einzeln Schaden nehmen.** Ohne sie gibt es nichts, was fallen könnte — dann überspring diesen Schritt ohne schlechtes Gewissen.

**Und ein Deckel, wie bei der Balancing-Falle:** höchstens zwei Sitzungen. Merkst du beim ersten Punkt, dass dir Grundlagen fehlen, die die Kür aus Etappe 5 nicht gebaut hat, dann hör auf und schreib nur das Design in `GELERNT.md` — was fällt, wann, wer es vorher merkt. Auch das ist eine erledigte Kür.

Die Idee: **Sinkt die `integritaet` eines Sektors auf 0, fällt er — und kommt nicht zurück.** Er ist danach nicht mehr betretbar; wer dort steht, wird in den Nachbarsektor zurückgedrängt. Das ist deine Karte aus Etappe 13, Konzept 10, rückwärts: Dort öffnete sich ein Weg zur Laufzeit, hier schließt sich einer.

Zwei Dinge, die du schon hast, sollen dabei mitreden:

- **`meldung_abgesetzt`:** Wer beim ersten Kontakt gemeldet hat, bekommt **einmal im Spiel** Hilfe — der erste Sektor, der fallen würde, hält mit einem Rest.
- **Eine Erkenntnis aus Etappe 15:** Wer eine bestimmte davon hat, bekommt im Wellenbericht eine Warnung, **bevor** ein Sektor fällt.

Welche Erkenntnis, wie viel Rest, welche Sätze — das entscheidest du. **Das ist Spieldesign, kein neues Python.** Alles, was du dafür brauchst, hast du: Zähler, Topf, Bericht, Karte.

---

## Selbsttest — 17c

- [ ] Eine umgestellte Meldung erscheint nicht im Kampf, sondern im Bericht — und in der nächsten Welle nicht noch einmal.
- [ ] Der Bericht zeigt die Abschüsse **dieser** Welle, auch die, die entstanden sind, während du ausgefallen warst.
- [ ] Mindestens zwei Kameraden klingen im Bericht verschieden, der Basisturm spricht mit der Stimme aus `Einheit` — und im Bericht fragt keine Zeile, welche Klasse eine Einheit hat.
- [ ] Kein `None` im Bericht, bei keiner Abschusszahl.
- [ ] In einer Lage mit Turm, Kern unter der Hälfte, Welle 5 oder später und ausstehendem Funk stehen alle fünf Ereignisse im Topf.
- [ ] Der Funkkontakt kommt höchstens einmal pro Spiel und spielt deine `letzte_meldung` wörtlich ab.
- [ ] Ein Generatorausfall halbiert den Turmschaden für genau die Wellen, die du in `GELERNT.md` festgelegt hast — und danach schießt der Turm wieder voll.
- [ ] Nach der letzten Welle kommt kein Ereignis, und das Schiff landet auf der Landeplattform.
- [ ] ⭐ **Der Beweislauf aus Schritt 13 b), wiederholt in Schritt 21: `diff` schweigt weiterhin.**
- [ ] Alle drei Commits sind gesetzt, `SEED` steht auf `None`.

---

## Was NICHT in diese Etappe gehört

**Kein `random.choices` im Auftrag.** Du darfst es ab jetzt kennen und in eigenen Experimenten benutzen. Im Spiel bleibt `gewichtete_wahl`, weil sie mit deinen Dictionaries arbeitet.

**Kein `random.shuffle`, kein `random.sample`.** Gibt es, brauchst du nicht. Die Leseübung zeigt, wie man ohne sie mischt.

**Keine Schwierigkeit, die sich an den Spieler anpasst.** Wellen, die leichter werden, wenn du schlecht spielst, sind eine eigene Design-Frage mit eigenen Tücken. Das Budget wächst heute stur mit der Wellennummer.

**Keine Wellenrezepte oder Ereignisse in Dateien.** `GEGNERTYPEN`, `BEUTE` und die Ereignisgewichte bleiben heute im Code. Etappe 25 zieht sie nach `content/`.

**Kein Spielstand.** Der Seed ist heute sichtbar und einstellbar, aber nicht gespeichert. Das ist Etappe 19 — und dort steht er als Erstes drin.

**Keine automatisierten Tests für den Generator.** Deine Prüfungen heute sind Zählen und `diff`. Etappe 26 macht daraus Tests, und ohne den Seed von heute ginge das nicht.

**Kein endgültiger Tod für Kameraden, keine Rekruten.** Siehe die Design-Entscheidung oben. Etappe 22.

**Keine Wirkung für Fähigkeiten, kein Flag-Set.** `meldung_abgesetzt` wirkt heute auf eine Zahl im Ereignistopf. In Etappe 18 geht es mit den Erkenntnissen in einem gemeinsamen Set auf.

**Kein Logging.** Der Wellenbericht ist für den Spieler, die Debug-Zeile für dich. Wo Entwickler-Ausgaben eigentlich hingehören, ist Etappe 20.

---

## Lernziele

In `GELERNT.md`, ohne nachzuschlagen — jeweils nach der Portion, zu der sie gehören.

**17a**

1. Was ist der Unterschied zwischen `random.randint`, `random.choice` und `random.random`? Und welches Ende ist bei `randint(1, 6)` eingeschlossen, das bei `range(1, 6)` fehlt?
2. Warum ändert sich nichts, wenn du alle Gewichte verdoppelst — und was genau bedeutet ein Gewicht von 0?
3. Deine `gewichtete_wahl` würfelt von 1 bis zur Summe. Welche Vergleichsgrenze gehört dazu, und was passiert mit den Anteilen, wenn man die andere nimmt?
4. **⭐ Warum steuert ein Budget besser als eine Anzahl?** Was davon entscheidest du, und was der Würfel?
5. Warum ist das Ende des Generators *„nichts mehr bezahlbar"* und nicht *„Budget ist 0"*?
6. Warum wird das Bezahlbare in jeder Runde neu gebaut und nicht einmal vor der Schleife?
7. Warum fällt ein Fund jetzt selten — und warum steht er in derselben Tabelle wie das Material, statt in einer eigenen?

**17b**

8. Was macht ein Seed — und warum ist er beim Fehlersuchen Gold wert?
9. **⭐ Was kannst du an einem Fehler nicht mehr feststellen, wenn dein Programm bei jedem Lauf andere Zahlen zieht?**
10. Derselbe Seed, und trotzdem ein anderer Lauf. Nenn zwei Gründe.

**17c**

11. Warum wird der Topf der möglichen Ereignisse mit einzelnen `if` gebaut, und das gezogene Ereignis mit `elif` ausgeführt?
12. Warum merkt sich jede Einheit ihren Stand zu Wellenbeginn selbst, statt dass die Welt ein Dictionary führt?
13. Der Bericht fragt nie, wer spricht, und trotzdem klingt der Heavy anders als der Turm. Wo steht die Entscheidung, wer wie klingt?

**Frage 9 ist die wichtigste.** Sie ist der Grund, warum der Seed ab heute zu deinem Spiel gehört und in Etappe 19 und 26 wiederkommt.

---

## 🧠 Die Entwicklerfrage — zu 17c

Sie hat keine Musterlösung, und niemand korrigiert sie.

> **Wie viel Zufall ist noch fair?**

Wo genau liegt für dich die Grenze zwischen *„überraschend"* und *„verloren, ohne dass ich etwas falsch gemacht habe"*? Du hast heute Material dafür: Ist ein Riss in der Kuppel fair, der **nur** kommt, wenn es dir ohnehin schlecht geht? Ist eine Welle 20 fair, deren Stärke du kennst, deren Zusammensetzung aber nicht? Ist ein Fund fair, der in zehn Wellen nicht fällt? Wäre ein Kamerad, der endgültig fällt, weil eine Welle ungünstig gewürfelt war, fair?

**Zwei bis fünf Sätze in `GELERNT.md`.** Nicht mehr. Der Wert liegt darin, dass du sie in Etappe 22 und 26 wiederliest.

---

## Transferaufgabe (15 Minuten) — zu 17a

In `wuerfeln.py`, ohne Spiel.

**Teil 1 — das Zahlenraten aus Etappe 3.** Dort stand: *„schreib sie heute fest hin — `random` ist Etappe 17a."* Hol es aus deiner Übungsdatei von damals, kopier es nach `wuerfeln.py` und ersetz die feste Zahl durch eine gewürfelte von 1 bis 100. Zwei Minuten, und ein Spiel aus Etappe 3 ist zum ersten Mal ein Spiel.

**Teil 2 — zwei Würfel.** Wirf zehntausendmal **zwei** Würfel und zähl mit, wie oft jede **Summe** vorkommt, von 2 bis 12. Gib die Summen der Reihe nach aus, jede mit ihrer Anzahl.

**Dann die eigentliche Frage:** Jeder einzelne Würfel ist gleichverteilt — jede Zahl gleich oft. **Warum ist die Summe 7 trotzdem etwa sechsmal so häufig wie die 2?**

*(Und was das mit deinem Spiel zu tun hat: Die Beute nach einer Welle ist die Summe aus vielen einzelnen Zügen. Ein einzelner Kriecher lässt in vier von zehn Fällen nichts fallen — zwanzig Kriecher lassen fast immer um die zwölf Chitinpanzer zurück, kaum je fünf oder zwanzig. **Viele kleine Zufälle zusammen schwanken weniger als einer allein.** Das ist derselbe Gedanke, der hinter dem Budget steckt: Die Stärke der Welle legst du fest, und der Zufall darf nur noch in vielen kleinen Entscheidungen darin wirken. Schreib ihn in eigenen Worten auf.)*

---

## Leseübung — Stufe 3 (15 Minuten) — zu 17b

**Ab heute steht die Leseleiter auf Stufe 3.** Die fünf Fragen bleiben dieselben. **Neu ist die Leitfrage darüber: Warum ist es so gebaut?** Nicht nur, was der Code tut — sondern welche Entscheidung dahintersteckt und welche Alternative es gegeben hätte.

**Die Regel dabei: Du tippst nichts ab und führst nichts aus.** Beantworte die Fragen allein aus dem Lesen.

```python
import random


class Musikbox:
    """Spielt Lieder in zufälliger Reihenfolge — aber gerecht verteilt."""

    def __init__(self, lieder, seed=None):
        self.lieder = lieder        # Titel -> wie oft pro Durchgang
        self.beutel = []
        self.zuletzt = None
        self.durchgaenge = 0
        if seed is not None:
            random.seed(seed)

    def fuelle_beutel(self):
        for titel in self.lieder:
            for _ in range(self.lieder[titel]):
                self.beutel.append(titel)
        self.durchgaenge += 1

    def naechstes(self):
        if not self.beutel:
            self.fuelle_beutel()
        titel = random.choice(self.beutel)
        if titel == self.zuletzt and len(self.beutel) > 1:
            titel = random.choice(self.beutel)
        self.beutel.remove(titel)
        self.zuletzt = titel
        return titel

    def __repr__(self):
        return f"Musikbox({len(self.beutel)} im Beutel, Durchgang {self.durchgaenge})"


LIEDER = {
    "Hafenlied": 3,
    "Nordwind": 2,
    "Kesselflicker": 1,
}

box = Musikbox(LIEDER, seed=7)
abend = []
for _ in range(12):
    abend.append(box.naechstes())

print(", ".join(abend))
print(box)
```

**Die fünf Fragen, für `naechstes()`:**

1. Was kommt rein?
2. Was passiert?
3. Was verändert sich — und woran?
4. Was kommt raus?
5. Welche anderen Objekte oder Funktionen werden dabei aufgerufen?

**Und die Stufe-3-Fragen — warum ist es so gebaut?**

6. **⭐ Die Box zieht nicht jedes Mal neu nach Gewicht, wie deine `gewichtete_wahl`, sondern füllt einen Beutel und nimmt heraus.** Wie oft ist „Hafenlied" nach den ersten sechs Liedern gelaufen — sicher, nicht ungefähr? Wie oft hätte es bei deiner `gewichtete_wahl` nach sechs Zügen höchstens laufen können? **Welche Bauart ist fairer, und welche überraschender?**
7. Wird ein Lied, das gerade lief, **nie** direkt wiederholt? Such einen Fall, in dem es doch passiert. *(Tipp: Was liegt kurz vor dem Neufüllen noch im Beutel?)*
8. Warum wird nur **einmal** neu gezogen, und nicht in einer Schleife, bis ein anderes Lied kommt? Was würde diese Schleife tun, wenn im Beutel nur noch zweimal „Nordwind" liegt?
9. Wozu dient `len(self.beutel) > 1` — was passiert ohne die Bedingung, wenn nur noch ein Lied im Beutel ist?
10. **Der Seed wird im `__init__` der Musikbox gesetzt.** Stell dir ein Programm vor, das neben der Musikbox auch noch würfelt — eine Tombola, sagen wir. **Was macht dieser eine Aufruf mit dem Zufall der Tombola?** Wo hättest du den Seed hingeschrieben, und warum? *(Das ist dieselbe Regel wie in Schritt 11 — genau einmal, an einer Stelle —, gesehen von der anderen Seite.)*
11. **Der `__init__` legt `lieder` so ab, wie es übergeben wird — keine Kopie.** Nach den zwölf Liedern setzt das Programm `LIEDER["Kesselflicker"] = 4`. Merkt die Box das — sofort, beim nächsten Neufüllen des Beutels, oder nie? Und wäre es anders, wenn der `__init__` mit `.copy()` eine Kopie ablegte? *(Etappe 4, Konzept 9, und Etappe 10, Konzept 6: zwei Namen, ein Objekt.)*

---

## Kaputtmachen

**Vor jedem Experiment aufschreiben, was passieren wird.** Nummer 1 bis 3, 6 und 7 gehören dazu, die übrigen sind Kür. **Nach jedem Experiment alles zurück** — auch den Startwert der Wellenschleife, wenn du ihn verstellt hast.

### Zu 17a

**1. ⭐⭐ Verschieb die Grenze.** Lass `gewichtete_wahl` von **0** bis zur Summe würfeln statt von 1, und lass den Vergleich, wie er ist. Dann die Prüfung aus Schritt 2 mit zwei gleichen Gewichten. **Wie ist das Verhältnis jetzt?** Nichts stürzt ab, jede Farbe kommt vor, und trotzdem ist es falsch — ein Typ-3-Fehler, den man nur durch Zählen findet. Nimm die Änderung zurück und prüf, dass wieder halbe-halbe herauskommt: die Rückwärtsprobe aus Etappe 16.

**2. ⭐ Spiel mit den Gewichten.** Setz alle drei Gegner-Gewichte gleich und spiel ab Welle 8 fünf Wellen. Dann setz das Gewicht der Panzerbrut auf das Hundertfache. **Fängt das Budget es ab, oder wird Welle 8 unspielbar?** Rechne nach, wie viele Panzerbruten in das Budget von Welle 8 passen, bevor du startest.

**3. Mach einen Gegner kostenlos.** `"kosten": 0` beim Kriecher, starten. Was passiert — und warum hört es nicht auf? **Brich mit `Strg + C` ab und lies den Traceback:** Er zeigt dir, in welcher Zeile dein Programm war, als du abgebrochen hast. *(Und was hat der Kriecher mit Konzept 5 zu tun, obwohl dort vom umgekehrten Fall die Rede war?)*

*Kür:*

**4. Vergiss „nichts".** Nimm die Prüfung auf `"nichts"` aus deiner Aufräumphase heraus. Spiel zwei Wellen mit vielen Kriechern und sieh dir nach dem Einsammeln deinen `vorrat` **und** dein Inventar an. Wo ist das Nichts gelandet — und warum gerade dort?

**5. Leg eine `random.py` an.** Eine leere Datei mit diesem Namen neben `spiel.py`, dann starten. Lies die Fehlermeldung ganz — und lösch die Datei wieder.

### Zu 17b

**6. ⭐ Setz den Seed in die Wellenschleife.** Verschieb `random.seed()` an den Anfang jeder Welle, mit einem festen Seed. Spiel ab Welle 8 drei Wellen und vergleich, womit die Wellen beginnen. **Was ist dir aufgefallen, und warum?** Konzept 10, Regel 1.

### Zu 17c

**7. ⭐⭐ Bau den Topf mit `elif`.** Mach aus den einzelnen `if` in `moegliche_ereignisse()` eine Kette. Dann die dritte Lage aus Schritt 18 in der Probedatei. **Was fehlt im Topf?** Und wie lange hättest du spielen müssen, um zu merken, dass der Funkkontakt nie kommt, solange ein Turm steht? *(Was genau fehlt, hängt davon ab, in welcher Reihenfolge deine `if` stehen — und in welcher Lage. Such dir eine, in der mindestens zwei Bedingungen gleichzeitig stimmen.)* Das ist die Warnung aus Etappe 2, Konzept 4, an deinem eigenen Code.

*Kür:*

**8. Vergiss das Leeren.** Nimm die Zeile heraus, die `self.bericht` am Ende des Berichts leert. Spiel drei Wellen. Wie lang ist der dritte Bericht?

**9. Nimm einer Stimme ihr `return`.** Ersetz in einem Zweig von `funkspruch()` bei einer Marine-Klasse das `return` durch ein `print`. Spiel eine Welle, in der dieser Zweig dran ist. Was steht im Bericht — und in welcher Reihenfolge?

---

**Experiment 1 und 7 sind das Paar.** Beide stürzen nicht ab, beide liefern plausible Ergebnisse, und beide sind falsch. Das eine verschiebt Wahrscheinlichkeiten, das andere löscht Möglichkeiten. **Nirgends verstecken sich Typ-3-Fehler so gut wie im Zufall** — weil „kommt selten" und „kommt nie" beim Spielen gleich aussehen.

Alles in `GELERNT.md` und ins Fehlertagebuch aus Etappe 8: **woran du es erkannt hättest.**

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `AttributeError: … module 'random' has no attribute 'randint'` — mit oder ohne *partially initialized* | Eine eigene Datei heißt `random.py` | Konzept 1 — umbenennen |
| `NameError: name 'random' is not defined` | `import random` fehlt oder steht nur in der Wegwerf-Datei | Schritt 3 — erste Zeile von `spiel.py` |
| `ValueError: empty range …` | `randint(1, 0)` — die Summe war 0 | Konzept 3 — Summe prüfen, bevor gewürfelt wird |
| `IndexError: Cannot choose from an empty sequence` | `random.choice()` auf eine leere Liste | Konzept 2 |
| Das Programm hängt beim Wellenbeginn | Der Generator endet nie: ein Typ kostet 0, oder das Ende heißt „Budget ist 0" | Konzept 5 — `Strg + C`, Traceback lesen |
| `KeyError: 'kosten'` | Ein Eintrag in `GEGNERTYPEN` ohne die neuen Schlüssel — oft der vierte Typ | Schritt 4 |
| `KeyError: None` beim Abziehen der Kosten | `gewichtete_wahl` gab `None` zurück, und niemand hat gefragt | Schritt 6 — `None` wie „nichts bezahlbar" |
| Eine Farbe kommt doppelt so oft, oder `None` taucht auf | Wurfbereich und Vergleichsgrenze passen nicht zusammen | Konzept 3 · Kaputtmachen 1 |
| Die Ankündigung nennt Typen, die nicht kommen, oder keine | `wellen_typen` wird noch aus der alten Kette gebaut — oder gar nicht mehr | Schritt 7 |
| Im Vorfeld liegt ein Fundstück `nichts` | Das Ziehergebnis wird nicht geprüft | Schritt 9 |
| Ein Gefallener hinterlässt zwei Dinge, und der Fund kommt bei jedem | Die Tabelle *Gegnertyp → Fundkennung* aus Etappe 15 legt noch zusätzlich ab | Schritt 9 — `BEUTE` ist die einzige Beutetabelle |
| Ein Fund lässt sich einsammeln, bringt beim Analysieren aber nie eine Erkenntnis | Die Kennung in `BEUTE` ist anders geschrieben als in `FUNDE` — ein Verweis ins Leere | Schritt 9 — kopieren statt abtippen |
| `diff` redet trotz festem Seed | Irgendwo wird über ein Set gelaufen und dabei gewürfelt oder ausgegeben — oder `random.seed()` steht an zwei Stellen | Konzept 11 · Schritt 11 |
| Mit Breakpoint und `< befehle17.txt` läuft das Spiel anders als ohne | Der Debugger liest Zeilen aus der Befehlsdatei | Konzept 12 — Breakpoints nur ohne `<` |
| Alle Wellen fangen gleich an | `random.seed()` steht in der Wellenschleife | Konzept 10, Regel 1 |
| Der Bericht wiederholt Meldungen aus früheren Wellen | `self.bericht` wird nicht geleert | Schritt 17 |
| `KeyError` mit einem Einheitennamen im Bericht | Der Stand zu Wellenbeginn steht in einem Dictionary, und die Einheit ist neu | Konzept 15 — ans Objekt |
| Im Bericht steht `None` statt eines Satzes | Ein Zweig von `funkspruch()` gibt nichts zurück — `print` statt `return`, oder ein Zweig ohne `return` | Schritt 17 · Kaputtmachen 9 |
| Der Bericht zeigt die Summe seit Spielbeginn | Der Stand wird nicht zu Beginn jeder Welle übernommen | Schritt 17 |
| Funkkontakt kommt nie | `elif` im Topf, oder die Welle-5-Bedingung falsch herum | Schritt 18 · Kaputtmachen 7 |
| Funkkontakt kommt jede Pause | `funk_gehoert` wird nicht gesetzt | Schritt 19 |
| Der Turm schießt nach dem Ausfall dauerhaft halb | Der gespeicherte Schaden wurde halbiert statt des ausgeteilten | Schritt 19 |
| Der Ausfall dauert eine Welle zu kurz oder zu lang | Herunterzählen und Setzen in der falschen Reihenfolge | Konzept 16 · Schritt 20, Frage 2 |

---

## Ein Blick nach vorne

**Etappe 18 gibt den Fähigkeiten Wirkung** und baut das zentrale Flag-Set. `meldung_abgesetzt` und `welt.erkenntnisse` gehen dort darin auf — deine Funkentscheidung wird ein Eintrag neben den anderen.

**Etappe 19 speichert das Spiel.** Der Seed steht dort als Erstes im Spielstand, zusammen mit `funk_gehoert` und einem laufenden `generatorausfall`. **Und dort stellt sich eine Frage, die heute schon angelegt ist:** Reicht es, den Seed zu speichern, um nach dem Laden denselben Zufall zu bekommen? *(Konzept 11 kennt die Antwort.)* Dort wird auch die Regel „einmal, am Anfang“ aus Konzept 10 genauer gefasst.

**Etappe 20 trennt Ausgaben.** Deine Debug-Zeile und dein Wellenbericht sind zwei Sorten Meldung mit zwei Adressaten — dort bekommen sie getrennte Wege.

**Etappe 22 stellt die Datenfrage.** Kosten, Gewichte und Ereignisse stehen dann neben Fähigkeiten, Turmstufen und Söldnern — und dort kommt die Frage zurück, ob ein Kamerad endgültig fallen darf.

**Etappe 25 zieht `GEGNERTYPEN`, `BEUTE` und die Ereignisgewichte in Dateien.** Dann ist eine neue Welle kein Code mehr, sondern Inhalt.

**Etappe 26 testet den Generator.** *„Welle 14 bei Seed 48173 kostet genau ihr Budget"* ist dort eine Zeile, die grün oder rot wird. Ohne Seed wäre sie nicht schreibbar — und deine Zufallsregeln aus `GELERNT.md` sind dort die Liste dessen, was ein Test prüfen soll.

---

## Abschluss

**In `GELERNT.md`:**

- ⭐⭐ **Deine Zufallsregeln** — eine kleine Liste unter der Überschrift *Zufallsregeln meines Spiels*, drei bis sechs Sätze. Der erste steht fest: *„Derselbe Seed und dieselben Eingaben ergeben denselben Lauf."* Die übrigen schreibst du selbst: wo der Seed gesetzt und angezeigt wird, was der Zufall entscheiden darf und was nicht — und **mindestens eine Stelle in deinem Spiel, an der du den Zufall bewusst begrenzt**, mit Grund. Darunter, was deine Läufe b), c) und d) aus Schritt 13 gezeigt haben. *(Die Liste holst du in Etappe 19 und 26 wieder hervor.)*
- ⭐ Die Reihenfolge der Pause zwischen den Wellen, mit deinen Antworten auf die zwei Fragen aus Schritt 20.
- Deine Antwort aus Konzept 3: `< 0` oder `<= 0`, und warum.
- Deine Wahl aus der Design-Entscheidung von 17a — und was du vom Budget hältst, nachdem du es gebaut hast.
- Die Zeilenzahlen vor und nach dem Generator aus Schritt 7.
- ⭐ Die Antwort auf deine Frage aus Etappe 4, unter der Frage.
- Die Säuredrüse: Wie viele Stellen in der Logik musstest du anfassen?
- Weg A oder B für das Sammeln — und welche Meldungen du in den Bericht verlegt hast, nach welcher Frage.
- Was „2" beim Generatorausfall genau bedeutet.
- 🧠 Die Entwicklerfrage.
- Was hat mich überrascht? *(Kandidaten: dass Welle 1 bis 3 gar nicht zufällig sind · dass eine falsche Grenze nicht abstürzt · wie sich der Funkkontakt angefühlt hat.)*

**Vor dem Commit:** `SEED` auf `None`? `random.seed()` genau einmal? Wellenschleife beginnt bei `1`? Keine `probe.py`, keine `wuerfeln.py`, keine `lauf*.txt`, kein `breakpoint()`, keine Testgewichte auf 0, keine vorübergehenden `print`-Zeilen?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest.

**Ein perfekt erhaltener Chitinpanzer.** Ein weiterer, seltener Eintrag in der Beute des Kriechers, Gewicht 1, eins weniger bei `"nichts"` — ein neues Material nach Schritt 9, drei Dateneinträge. Was man daraus herstellen könnte, ist eine Frage für die Werkstatt. **Heute nur: Er fällt, er ist selten, und du hast keine Zeile Logik geschrieben.**

**Einheiten merken sich, wo sie waren.** Jede Einheit zählt mit, in wie vielen Takten sie in welchem Sektor stand. Im Bericht: *„Vasquez hat das Nordtor zwei Wellen lang allein gehalten."* Billig gebaut — ein Dictionary am Objekt und das Zählmuster aus Konzept 4 —, und Vasquez bekommt eine Geschichte.

**Eine Vorschau über zwei Wellen.** Erzeug die nächste Welle schon am Ende der laufenden und zeig sie mit Vorwissen vorab an. **Prüf danach mit dem Beweislauf, ob dein Seed das noch trägt** — du hast die Reihenfolge verändert, in der Zahlen aus der Folge genommen werden.

**Ein Ereignis, das nicht zweimal hintereinander kommt.** Der Trick aus der Leseübung, angewandt auf deinen Topf. Welcher der beiden Wege — Beutel oder Neuziehen — passt besser zu Ereignissen?

**Die Zustandszeile aus der Kür von Etappe 16**, falls du sie noch nicht hast. Jetzt, mit Zufall, ist sie das Werkzeug, das dir beim Beweislauf die erste abweichende Zeile am schnellsten zeigt.

---

> **Nächste Etappe:** Etappe 18 — Fähigkeiten, Skillpunkte, Statuseffekte · aus der Abklingzeit wird eine Wirkung, und aus deinen Flags wird ein Set

