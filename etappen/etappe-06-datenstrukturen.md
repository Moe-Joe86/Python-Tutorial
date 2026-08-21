# Etappe 6 — Liste, Dictionary, Set, Tuple

> **Block 1: Fundament** · Etappe 6 von 30 · [← Etappe 5](etappe-05-vorposten-und-depot.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 7 →](etappe-07-aufraeumen.md)

**Boot.dev:** Sets, Tuples, Mengenoperationen
**Zeitaufwand:** 4–5 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 5 abgeschlossen, Selbsttest grün

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| `KLASSEN` als Tuple · zwei Sets · Freischaltungen · Bestiarium | Warum ein Set die Regel *ist* statt sie zu prüfen · die vier Fragen der Strukturwahl | Mengenoperationen (Differenz, Schnitt, Vereinigung) · warum `in` beim Set schneller ist · Sets und Tuples in JSON |

---

## Worum es geht

**Diese Etappe baut kein neues System. Sie korrigiert Wahlentscheidungen, die du getroffen hast, ohne es zu merken.**

Bis heute hattest du zwei Sammlungsarten, und du hast sie benutzt, weil es nur zwei gab. Eine Liste, wenn du mehrere Dinge brauchtest. Ein Dictionary, wenn du etwas nachschlagen wolltest. Das war keine Entscheidung, das war Verfügbarkeit.

Sieh dir drei Stellen in deinem eigenen Code an, bevor du weiterliest:

**Erstens.** In Etappe 5 hast du eine Tabelle gebaut, die nichts speichert außer Ja und Nein — welche Ware stapelbar ist. Ein Dictionary aus lauter `True` und `False`. Es funktioniert. Aber die Werte tragen keine Information; die Information ist, *dass ein Name drinsteht*.

**Zweitens.** Dein Inventar ist eine Liste. Eine Liste garantiert dir eine Reihenfolge — und die Reihenfolge deines Inventars bedeutet nichts. Du hast eine Zusage bekommen, die du nie brauchst, und bezahlst sie bei jedem `in` mit einer Suche von vorne.

**Drittens** — und das ist die interessanteste: Es gibt in deinem Spiel gerade nichts, was man nur einmal haben kann. Alles ist beliebig oft kaufbar, beliebig oft aufsammelbar. Heute kommt der erste Wert, bei dem „zweimal" keinen Sinn ergibt, und du wirst sehen, dass es dafür eine Struktur gibt, statt einer Prüfung.

**Der Satz, unter dem die ganze Etappe steht:**

> **Nicht: „welche Struktur kenne ich?" Sondern: „welche Frage stelle ich an meine Daten?"**

Vier Strukturen, vier Fragen. Am Ende der Etappe hast du eine Entscheidungshilfe, die du im ganzen Rest des Projekts benutzt — und in Etappe 25, wenn dreißig Gegnertypen aus einer Datei kommen, ist sie der Grund, warum du weißt, was davon Liste wird und was Dictionary.

**Und weil eine Etappe ohne neue Spielfunktion sich schnell nach Hausaufgabe anfühlt, bekommt dein Spiel trotzdem zwei Dinge dazu:** Freischaltungen, die man nicht doppelt kaufen kann. Und ein **Bestiarium** — die erste Sache in deinem Programm, die sich etwas über Wellen hinweg *merkt*. Bisher beschreibt jede deiner Variablen den aktuellen Zustand. Das Bestiarium beschreibt deine Geschichte.

---

## Vor dem Umbau: drei Fragen ⭐

Das Ritual seit Etappe 4. Heute betrifft es die Stapelbarkeit aus Etappe 5, Auftragsschritt 10.

| Frage | Für heute |
|---|---|
| **Was bleibt gleich?** | Der Kauf. Munition landet im `vorrat`, ein Medkit im `inventar`, die Meldungen, die Preise — alles |
| **Was ändert sich nur in der Darstellung?** | Nichts. Der Spieler merkt von diesem Umbau überhaupt nichts |
| **Was ändert sich wirklich am Datenmodell?** | Aus einem Dictionary Name → Wahrheitswert wird ein Set aus Namen |

**Die zweite Zeile ist die ungewöhnliche.** Ein Umbau, den niemand sieht, fühlt sich sinnlos an. Er ist es nicht: Danach kann eine Ware nicht mehr *widersprüchlich* eingetragen sein, weil es nichts mehr gibt, worin sie sich widersprechen könnte. Das ist die Sorte Arbeit, die dir in vier Wochen eine Stunde Fehlersuche erspart, und du wirst nie erfahren, welche.

---

## Zwei Design-Entscheidungen, die du jetzt treffen solltest

Beide haben mehr als eine vertretbare Antwort. Schreib deine Wahl **und die Begründung** in `GELERNT.md`.

### Entscheidung 1 — Wo lebt der Gegnertyp? ⭐

Dein Bestiarium soll zeigen, welchen Sorten Brut du bisher begegnet bist. Dafür muss irgendwo stehen, welcher Typ gerade anrückt — und dein Programm weiß das im Moment nirgends. Ein Gegner ist eine Zahl: die Stelle, an der er steht.

Es gibt zwei Orte, an die der Typ kann:

| | Die **Welle** kennt ihre Typen | Jeder **Gegner** kennt seinen Typ |
|---|---|---|
| In den Daten | Eine Menge Typen pro Welle, daneben unverändert `gegner = [7, 4, 2]` | Jeder Eintrag trägt Typ **und** Position |
| Die Anmarschbahn | Alle Gegner sehen gleich aus | Jeder Typ hat ein eigenes Zeichen |
| Aufwand heute | zwanzig Minuten | ein bis zwei Abende, dein Bewegungscode wird angefasst |
| In Etappe 11 | Der Typ wandert vom Wellen- ins Gegnerobjekt | Der Typ ist schon am richtigen Ort |

**Meine Empfehlung: die Welle.** Nicht weil es eleganter wäre — es ist es nicht —, sondern weil der zweite Weg dich zwingt, dir *heute* auszudenken, wie ein Gegner mit mehreren Eigenschaften aussieht. Genau diese Frage ist der Inhalt von Etappe 11, und sie wird dort mit dem richtigen Werkzeug beantwortet. Wer sie heute mit den Mitteln von Etappe 6 löst, baut eine Konstruktion, die er in fünf Etappen wieder abreißt.

**Wenn du den zweiten Weg trotzdem willst** — er ist spielerisch der bessere —, dann bau ihn so: Jeder Eintrag in `gegner` wird ein Tuple aus Typ und Position, `("kriecher", 7)`. Und dann merkst du sofort etwas, das ich dir nicht wegnehmen will: **Ein Tuple lässt sich nicht ändern.** Ein Gegner, der ein Feld vorrückt, muss also ersetzt werden statt verändert. Das ist mühsam, es ist die ehrliche Rechnung für die Struktur — und es ist die beste Begründung für Etappe 11, die du bekommen kannst. Notier, wie es sich anfühlt.

**Der Begriff dafür, und du wirst ihn ab jetzt oft brauchen:** Das hier ist eine **Modellierungsentscheidung**. Nicht die Frage, wie man etwas programmiert, sondern *woraus die Sache in deinem Programm besteht*. Sie hat selten eine richtige Antwort und immer Folgen. In Etappe 14a triffst du die nächste (benannte Orte oder Raster?), in Etappe 19 die übernächste (was ist Struktur, was ist Dateiformat?).

### Entscheidung 2 — Was passiert beim zweiten Mal?

Der Spieler schaltet den Panzerbrecher frei. Dann tippt er denselben Befehl noch einmal. Drei Reaktionen sind vertretbar:

| Variante | Was der Spieler erlebt |
|---|---|
| Meldung | „Panzerbrecher ist bereits freigeschaltet." |
| Gar nicht anbieten | Freigeschaltete Ausbauten verschwinden aus der Liste |
| Beides | Sie stehen weiter da, markiert, und der Kauf meldet |

Das klingt nach Geschmack und ist es nicht ganz. In Etappe 18 bekommen Fähigkeiten **Voraussetzungen** — eine Fähigkeit, die noch nicht kaufbar ist, weil eine andere fehlt. Wenn du heute freigeschaltete Einträge einfach ausblendest, hast du dort zwei Gründe für dasselbe Verschwinden und musst sie wieder auseinandersortieren.

**Mein Rat: die dritte Variante.** Sichtbar bleiben, markiert werden, beim Kauf melden. Sie kostet heute nichts extra und trägt bis 22.

---

## Die Konzepte

Alle Beispiele laufen **außerhalb** deines Spiels. Und wie in 4 und 5: Die Struktur kann dir selbst sagen, was sie kann.

```python
dir(set())           # alles, was ein Set kann
help(set().add)      # was eine Methode tut
```

### 1. Warum es überhaupt vier gibt

Alle vier halten mehrere Werte. Der Unterschied ist nicht, *was* drin ist, sondern **welche Zusagen die Struktur dir macht** — und jede Zusage kostet etwas.

| Struktur | Zusage | Preis |
|---|---|---|
| **Liste** | Reihenfolge bleibt, Duplikate erlaubt, Zugriff über Position | `in` sucht von vorne |
| **Dictionary** | Zu jedem Schlüssel genau ein Wert, Zugriff über den Namen | Schlüssel müssen unveränderlich sein |
| **Set** | Jeder Wert höchstens einmal, `in` ist sofort | Keine Reihenfolge, kein Index, Elemente müssen unveränderlich sein |
| **Tuple** | Ändert sich nach dem Anlegen nie | Ändert sich nach dem Anlegen nie |

**Die letzte Zeile ist kein Tippfehler.** Bei einem Tuple ist die Zusage identisch mit dem Preis — je nachdem, ob du sie brauchst oder sie dir im Weg ist.

### 2. Ein Set anlegen — und die eine Falle dabei ⚠️

```python
werkzeuge = {"hammer", "zange", "feile"}
leer = set()
```

Geschweifte Klammern wie beim Dictionary, aber ohne Doppelpunkte.

⚠️ **Und jetzt die Stelle, an der jeder einmal hängenbleibt:**

```python
a = {}          # ein leeres DICTIONARY
b = set()       # ein leeres Set
```

`{}` war zuerst da und gehört dem Dictionary. Ein leeres Set schreibt man `set()`, und es gibt keine kürzere Form. Wenn du dich vertust, merkst du es nicht sofort — beide sind falsy, beide nehmen `len()`, und der Fehler kommt erst bei `.add()`.

*(Ein Set aus einer Liste bauen geht auch: `set(["a", "b", "a"])` ergibt ein Set mit zwei Einträgen. Merk dir das für Kaputtmach-Experiment 5.)*

### 3. Keine Reihenfolge, kein Index, keine Duplikate

```python
werkzeuge = {"hammer", "zange", "hammer"}
print(werkzeuge)        # zwei Einträge, nicht drei
print(len(werkzeuge))   # 2

werkzeuge.add("feile")      # rein
werkzeuge.add("feile")      # passiert nichts. Kein Fehler.
werkzeuge.discard("saege")  # nicht drin? Egal.
werkzeuge.remove("saege")   # nicht drin? KeyError.

werkzeuge[0]            # TypeError — ein Set hat keine Positionen
```

**Drei Dinge zum Mitnehmen.** Erstens: Doppeltes Hinzufügen ist kein Fehler, es ist ein Nichts. Zweitens: `discard()` und `remove()` unterscheiden sich genau darin, ob dir das Fehlen wichtig ist — dieselbe Frage wie `.get()` gegen eckige Klammern in Etappe 5. Drittens: Die Ausgabereihenfolge kann sich zwischen zwei Programmläufen unterscheiden. **Verlass dich nie darauf.** Wenn du ein Set sortiert ausgeben willst, sortierst du beim Ausgeben — die Struktur tut es nicht für dich.

### 4. ⭐ Das Set *ist* die Regel — und was es nicht leistet

**Das ist der wichtigste Abschnitt dieser Etappe.**

Angenommen, jemand soll einen Kurs nur einmal belegen können. Mit einer Liste:

```python
# fremdes Beispiel — so nicht
if "erste_hilfe" not in belegte_kurse:
    belegte_kurse.append("erste_hilfe")
```

Das funktioniert. Und die Regel „nur einmal" lebt jetzt **in dieser einen Zeile**. An jeder anderen Stelle, an der jemals ein Kurs dazukommt, muss dieselbe Prüfung wieder stehen — und beim dritten Mal vergisst sie jemand.

Mit einem Set:

```python
belegte_kurse.add("erste_hilfe")
```

Die Regel steht nicht mehr im Code. Sie steht in der Struktur. **Es gibt keine Stelle mehr, an der man sie vergessen kann**, weil es keine Stelle mehr gibt, an der sie steht.

> **Der Unterschied zwischen „ich habe es abgefangen" und „es kann nicht passieren".**

Das ist eine der Ideen, die dich dein Programmiererleben lang begleiten, und sie ist größer als Sets. Ein Zustand, den man nicht falsch hinschreiben kann, braucht keinen Test.

⭐ **Und jetzt die Einschränkung, die genauso wichtig ist wie der Satz — sie wird fast immer weggelassen:**

> **Ein Set garantiert den Zustand, nicht den Vorgang.**

Das Set sorgt dafür, dass ein Kurs niemals doppelt drinsteht. Es sorgt **nicht** dafür, dass niemand zweimal Gebühren zahlt. Wenn dein Kaufvorgang erst abbucht und dann `add()` aufruft, hast du eine saubere Menge und einen bestohlenen Spieler — und keine Fehlermeldung, weil formal alles stimmt.

**Die Prüfung „habe ich das schon?" verschwindet also nicht. Sie wechselt nur die Aufgabe:** Vorher hat sie die Daten geschützt, jetzt schützt sie den Ablauf. Das ist die Prüfreihenfolge aus Etappe 5, Schritt 11 — und Auftragsschritt 6 verlangt sie wieder.

### 5. Was in ein Set darf — die Einlösung aus Etappe 5

In Etappe 5 stand: Ein Dictionary-Schlüssel muss **hashbar** sein, Listen sind es nicht. Für Set-Elemente gilt exakt dieselbe Regel, aus exakt demselben Grund.

```python
{"hammer", "zange"}       # geht
{(1, 2), (3, 4)}          # geht — Tuples sind unveränderlich
{["a", "b"]}              # TypeError: unhashable type: 'list'
```

**Warum:** Ein Set findet einen Wert nicht, indem es alle durchgeht, sondern indem es aus dem Wert selbst ausrechnet, wo er liegen müsste. Ändert sich der Wert nachträglich, liegt er am falschen Platz und ist verloren. Deshalb dürfen nur Dinge hinein, die sich nicht ändern können.

**Das ist derselbe Mechanismus, der `in` beim Set so schnell macht** — Konzept 6. Zusage und Preis sind hier ein und dieselbe Eigenschaft.

*(In Etappe 14b wird das konkret: Ein Geschütz deckt Felder ab, ein Feld ist ein Koordinaten-Tuple, und die abgedeckten Felder sind ein Set. Genau deshalb sind Koordinaten dort Tuples und keine Listen.)*

### 6. `in` an drei Strukturen — dreimal dasselbe Wort, dreimal etwas anderes

**Das Experiment aus dem Lehrplan. Mach es wirklich, in einer Wegwerf-Datei:**

```python
"feile" in ["hammer", "zange"]              # sucht im Inhalt, von vorne
"feile" in {"hammer", "zange"}              # sucht im Inhalt, sofort
"feile" in {"hammer": 5, "zange": 9}        # sucht im SCHLÜSSEL
```

Die dritte Zeile ist die Einlösung aus Etappe 5: `in` schaut beim Dictionary nur links vom Doppelpunkt. Wenn du nach Werten suchen willst, `in ....values()` — **und das ist wieder eine Suche von vorne**, weil `.values()` keine Menge ist, sondern eine Aufzählung.

**Und jetzt der Teil, den du fühlen sollst statt ihn zu glauben:**

```python
zahlen_liste = list(range(3_000_000))
zahlen_set   = set(zahlen_liste)

import time
start = time.perf_counter()
for _ in range(50):
    2_999_999 in zahlen_liste
print("Liste:", time.perf_counter() - start)

start = time.perf_counter()
for _ in range(50):
    2_999_999 in zahlen_set
print("Set:  ", time.perf_counter() - start)
```

Der Unterschied ist keine Prozentzahl. Die Liste geht drei Millionen Einträge durch, fünfzigmal. Das Set rechnet einmal aus, wo der Wert liegen müsste, und sieht nach.

👀 **Der Fachbegriff dafür ist Laufzeit, und mehr als diesen einen Satz brauchst du heute nicht:** Bei einer Liste wächst die Suchzeit mit der Menge, beim Set nicht. Bei zehn Einträgen ist das egal. Bei zehntausend nicht mehr.

**Ehrlich eingeordnet:** Dein Inventar hat zehn Einträge. Die Geschwindigkeit ist in deinem Spiel bis Etappe 30 vollkommen bedeutungslos. Der Grund, heute trotzdem Sets zu nehmen, ist Konzept 4 und nicht dieser Abschnitt — aber du sollst einmal gemessen haben, dass der Unterschied echt ist.

### 7. Das Tuple — die Liste, die sich festlegt

```python
wochentage = ("mo", "di", "mi", "do", "fr")
wochentage[0]           # "mo" — Index wie bei der Liste
len(wochentage)         # 5
wochentage[0] = "so"    # TypeError: 'tuple' object does not support item assignment
```

Ein Tuple ist eine Liste, die sich nach dem Anlegen nicht mehr ändern lässt. Runde Klammern statt eckiger. Alles andere — Index, `len()`, `in`, `for` — funktioniert gleich.

**Wofür ist das gut, wenn es doch nur weniger kann?** Genau dafür. Ein Tuple ist eine Zusage an dich selbst und an jeden, der den Code liest: *Hier ändert sich nichts.* Wenn du in vier Wochen liest, dass etwas ein Tuple ist, weißt du sofort, dass keine Stelle im Programm daran herumschraubt.

**Zwei typische Fälle:**
- **Eine feste Aufzählung**, die zum Spiel gehört und nicht zum Spielstand — genau das ist `KLASSEN` in Auftragsschritt 1.
- **Ein Wertepaar, das zusammengehört** — Koordinaten sind das klassische Beispiel. *Dein Spiel hat noch keine.* Ab Etappe 14a wird es das schönste Beispiel für Tuples geben, das dieser Plan zu bieten hat; heute wäre es nur eine Behauptung.

⚠️ **Und die Feinheit, die verwirrt:** Unveränderlich ist das Tuple, nicht unbedingt sein Inhalt.

```python
t = ([1, 2], "fest")
t[0].append(3)          # geht — die Liste darin ist weiter veränderlich
t[0] = [9]              # TypeError
```

**Der Merksatz:** Ein Tuple legt fest, *welche Dinge* drinliegen — nicht, wie diese Dinge aussehen. Deshalb ist `([1, 2], 3)` auch nicht hashbar und darf nicht in ein Set: eines der Dinge darin kann sich ändern.

### 8. ⭐ Die Komma-Falle

```python
a = (5)
b = (5,)
print(type(a))      # <class 'int'>
print(type(b))      # <class 'tuple'>
```

**Ein Tuple entsteht durch das Komma, nicht durch die Klammern.** Die Klammern gruppieren nur — `(5)` ist dieselbe Fünf wie ohne Klammern.

Deshalb geht das hier auch:

```python
c = 5, 7            # ein Tuple, ganz ohne Klammern
```

**Warum das mehr ist als eine Kuriosität:** In Etappe 21a gibt eine Trefferrechnung zwei Werte auf einmal zurück — `return schaden, war_kritisch`. Das ist genau diese Form. Wer die Komma-Regel nicht kennt, versteht dort nicht, warum plötzlich zwei Sachen aus einer Funktion kommen. Und wenn du das Komma an einer Stelle vergisst, an der es hingehört, bekommst du eine Zahl statt eines Paares — ohne Fehlermeldung, an einer ganz anderen Stelle im Programm.

Das ist ein Kandidat für die Bug-Jagd in Etappe 16, und du hast ihn heute gesehen.

### 9. Tuple-Unpacking — und die Enthüllung dazu

```python
paar = ("hammer", 5)
name, anzahl = paar
```

Links so viele Namen wie rechts Werte, und Python verteilt. Passt die Zahl nicht, gibt es einen Fehler — das ist gut, denn es heißt, dass Unpacking nie stillschweigend etwas Falsches tut.

**Und jetzt die Stelle, an der dir etwas aufgehen soll:** Du benutzt das seit Etappe 5.

```python
for name, daten in gewuerze.items():
    ...
```

`.items()` liefert für jeden Eintrag ein **Tuple** aus Schlüssel und Wert. Die zwei Namen links vom `in` sind Unpacking — du hast eine Tuple-Technik benutzt, bevor du wusstest, dass es Tuples gibt.

**Prüf das nach**, statt es mir zu glauben: Lass eine Schleife mit nur *einem* Namen über `.items()` laufen und gib den aus. Du siehst das Tuple.

*(In Etappe 12 läuft dieselbe Form über Einheiten und ihre Zustände. Dann ist sie dir vertraut, und das ist der Zweck von heute.)*

### 10. 👀 Mengenoperationen

```python
kann_a = {"lesen", "schreiben"}
kann_b = {"lesen", "rechnen"}

kann_a - kann_b      # {"schreiben"}   — was nur A kann
kann_a & kann_b      # {"lesen"}       — was beide können
kann_a | kann_b      # alle drei       — zusammengeworfen
```

**Drei Zeichen, drei Fragen, die man sonst mit einer Schleife beantwortet.** Das ist Stufe 👀: Du sollst sie wiedererkennen und in einem Satz sagen können, was sie tun. Du musst sie heute nicht benutzen.

**Wo sie in diesem Plan zahlen:** In Etappe 18 lautet die Frage *„welche Voraussetzungen fehlen mir noch für diese Fähigkeit?"* — und die Antwort ist `benoetigt - freigeschaltet`, eine Zeile statt einer Schleife mit Zähler.

Wenn du heute eine passende Stelle findest (Auftragsschritt 10 hat eine), benutz sie ruhig. Wenn dir die Schleife klarer ist, nimm die Schleife. Beides ist in Ordnung; nur wiedererkennen musst du die Zeichen.

### 11. ⭐ Die Entscheidungshilfe — vier Fragen, feste Reihenfolge

Das ist der Ertrag der Etappe. **Die Reihenfolge ist Teil der Regel**, weil mehrere Antworten gleichzeitig passen können und die erste passende gewinnt.

> **1. Schlage ich etwas unter einem Namen nach?** → **Dictionary**
> **2. Sollen Duplikate unmöglich sein und die Reihenfolge egal?** → **Set**
> **3. Soll sich das nach dem Anlegen nie mehr ändern?** → **Tuple**
> **4. Sonst** → **Liste**

Damit sind die drei Fragen beantwortet, die Etappe 5 offen gelassen hat — *Ist es schon enthalten? Darf es doppelt vorkommen? Ist die Reihenfolge Teil der Bedeutung?* — und zusammen mit den dreien von damals hast du sechs.

**Prüf sie an deinem eigenen Bestand nach:**

| Deine Sammlung | Frage, die zieht | Struktur |
|---|---|---|
| `sektoren` | Was gehört zu *diesem Namen*? | Dictionary |
| `waren` | Was kostet *dieser Artikel*? | Dictionary |
| `vorrat` | Wie viel habe ich von *diesem*? | Dictionary |
| `inventar` | Welche Dinge habe ich? Doppelte sind erlaubt | Liste |
| `gegner` | Welche Gegner stehen wo, in welcher Reihenfolge? | Liste |
| **Stapelbarkeit** | Ist dieser Name in einer festen Gruppe? | **Set** ← der Umbau von heute |
| **Freischaltungen** | Habe ich das? Zweimal ergibt keinen Sinn | **Set** |
| **`KLASSEN`** | Feste Aufzählung, ändert sich nie | **Tuple** |

⚠️ **Und die Gegenprobe, die wichtiger ist als die Tabelle: Wo wäre ein Set falsch?**

**Dein Inventar.** Zwei Medkits sind zwei Medkits. Ein Set würde das zweite stillschweigend schlucken — kein Fehler, keine Meldung, ein Gegenstand weg. Die Zusage „keine Duplikate" ist ein Geschenk, wenn Duplikate ein Fehler wären, und ein Datenverlust, wenn sie es nicht sind.

**Die Frage aus Etappe 4 in ihrer endgültigen Form:** *Sind zwei gleiche Einträge dasselbe oder zwei Sachen?* Bei Freischaltungen dasselbe. Bei Medkits nicht.

### 12. Zwei Sorten Nein

Dein Programm sagt inzwischen ziemlich oft nein. Und es gibt dabei **zwei grundverschiedene Gründe**, die sich für den Spieler völlig unterschiedlich anfühlen:

| Sorte | Beispiel | Was der Spieler daraus lernt |
|---|---|---|
| **Das Wort kenne ich nicht** | `bestiarium hubschrauber` | Er hat sich vertippt oder etwas erfunden |
| **Das Wort kenne ich, hier geht es nur nicht** | `bestiarium panzerbrut`, noch nie gesehen | Es gibt das — er ist nur noch nicht so weit |

**Technisch ist das die Frage nach zwei verschiedenen Mengen:** Was ist überhaupt ein gültiges Wort (dein Katalog), und was ist gerade möglich (dein Zustand). Das Depot aus Etappe 5 hatte das schon, ohne dass es benannt wurde: „Diese Ware gibt es nicht" gegen „Du bist nicht im Depot".

**Warum es heute einen eigenen Abschnitt bekommt:** In Etappe 20 wird daraus ein Prinzip für *jeden* Befehl, und in Etappe 18 wird die zweite Sorte zur häufigsten Meldung im ganzen Spiel — jede Fähigkeit, deren Voraussetzung fehlt, ist genau dieser Fall. Wer beides in einen `else`-Zweig wirft, baut ein Spiel, das nicht sagen kann, wie weit man ist.

### 13. Die Erstbegegnung — warum das Bestiarium keine Liste ist

Der erste Kriecher, den du je siehst, bekommt drei Sätze. Der zwanzigste bekommt eine Zeile.

**Das ist eine Erzähltechnik, und sie läuft über genau eine Frage:** *Ist dieser Typ schon in `gesehene_gegnertypen`?* Ein `in`, ein `add()`, fertig. Kein Zähler, keine Reihenfolge, keine Duplikate — der Lehrbuchfall für ein Set.

**Und der Nebeneffekt ist der eigentliche Gewinn:** Sobald dein Programm weiß, was du gesehen hast, weiß es auch, was du *nicht* gesehen hast. „Vier von sieben Typen erfasst" ist eine Zeile Code und die erste Stelle, an der dein Spiel dem Spieler zeigt, dass es größer ist als das, was er kennt.

**In Etappe 15 baut genau darauf das Erkenntnissystem auf:** Der Datenkern der Brut, den du in Etappe 4 aufgesammelt hast und mit dem niemand etwas anfangen konnte, wird dort zur ersten Erkenntnis über einen Typ. Das Set von heute ist die Stelle, an der solche Erkenntnisse andocken.

### 14. 👀 Was sich nicht speichern lässt

Ein Satz zum Wiedererkennen, mehr nicht:

> **Sets und Tuples überleben JSON nicht.**

JSON kennt Listen, Objekte, Zahlen, Texte, Wahrheitswerte und `null`. Ein Set gibt es dort nicht. Ein Tuple wird beim Laden zur Liste — es geht raus als Paar und kommt zurück als Liste, ohne dass jemand meckert.

**Du musst heute nichts tun.** Aber wenn du in Etappe 19 deinen Spielstand speicherst, steht dort die Entscheidung an: als Liste speichern und beim Laden wieder in ein Set verwandeln — oder die Struktur ändern. Merk dir für heute nur, dass deine zwei neuen Sets diese Frage erben.

---

## Dein Auftrag

Nach jedem Schritt ausführen — und vorher sagen, was passieren wird.

**1. Leg `KLASSEN` als Tuple an.**

Vier Einträge in dieser Reihenfolge:

```
KLASSEN:  soldat, heavy, engineer, medic
```

Als Tuple, nicht als Liste — die Schreibweise steht in Konzept 7. Großgeschrieben, weil sich das nie ändert; die Konvention aus Etappe 2 gilt weiter. Der Name gehört ganz nach oben zu deinen festen Werten, nicht in die Spiellogik.

**2. Prüf die Klasseneingabe gegen `KLASSEN`,** bevor deine `elif`-Kette aus Etappe 2 läuft. Eine ungültige Eingabe soll gemeldet werden und die Kette gar nicht erst erreichen.

**Deine Entscheidung aus Etappe 1 bestimmt, wie viel Arbeit das ist:**

- **Du speicherst die Klasse als Namen** (`"heavy"`) — dann ist die Prüfung `in KLASSEN` und du bist fertig.
- **Du speicherst sie als Zahl** — dann übersetz sie jetzt. Ein Tuple hat einen Index: `KLASSEN[eingabe - 1]` liefert den Namen. Prüf vorher, dass die Zahl zwischen 1 und `len(KLASSEN)` liegt.

**Zum Prüfen:** Starte dreimal — mit einer gültigen Wahl, mit `9`, mit `zwei`. Der zweite Fall muss jetzt sauber melden. Der dritte stürzt weiterhin ab; das ist Etappe 20.

*(Damit ist die Schuld aus Etappe 1 endgültig eingelöst: Die `9`, die dort still durchlief, hat jetzt eine Stelle, die sie abweist.)*

**Deine `elif`-Kette bleibt stehen.** Sie stirbt in Etappe 11, nicht heute.

**3. Leg zwei leere Sets an:** `freigeschaltet` und `gesehene_gegnertypen`.

**Ein leeres Set schreibt man `set()` und nicht `{}`** — Konzept 2. Prüf mit `print(type(freigeschaltet))`, dass wirklich ein Set dasteht und kein Dictionary.

**4. Bau den Katalog `AUSBAUTEN` als Dictionary** Name → Preis in Schrott:

| Kennung | Preis | Wirkung |
|---|---|---|
| `"zielhilfe"` | 60 | keine — siehe Schritt 7 |
| `"schnellladen"` | 80 | Nachladen bringt 60 Schuss statt 40 |
| `"panzerbrecher"` | 120 | Jeder Schuss macht 3 Schaden mehr |

Der Katalog ist eine Konstante wie `KLASSEN` und steht bei deinen festen Werten.

**5. Bau den Befehl `ausbauten`.**

Er listet alle Einträge aus `AUSBAUTEN` mit Preis auf und markiert, welche davon schon freigeschaltet sind — mit einer Schleife über das Dictionary und einem `in` gegen das Set. **Kein Ausbau-Name darf in der Ausgabe fest hingeschrieben sein.**

Bind den Befehl an den Sektor `"depot"`, so wie `depot` und `kaufe` in Etappe 5.

**Zum Prüfen:** Trag testweise einen vierten Ausbau in `AUSBAUTEN` ein. Er muss in der Liste erscheinen, ohne dass du die Anzeige anfasst. Danach wieder herausnehmen.

**6. Bau den Befehl `schalte frei <kennung>`.**

Die Prüfreihenfolge ist dieselbe wie beim Kauf in Etappe 5, mit einer Prüfung mehr — und jede bekommt eine eigene Meldung:

```
Gibt es die Kennung in AUSBAUTEN?      →  nein: Meldung, Ende
Steht sie schon in freigeschaltet?     →  ja:   Meldung, Ende
Reicht der Schrott?                    →  nein: Meldung, Ende
── ab hier wird verändert ──
Schrott abbuchen
Kennung ins Set aufnehmen
```

**Die zweite Prüfung ist der Punkt von Konzept 4.** Das Set verhindert den doppelten *Eintrag* von selbst — es verhindert nicht, dass du zweimal abbuchst. Genau dafür steht sie da.

**Zum Prüfen:** Schalt `zielhilfe` frei. Dann noch einmal. Der Schrott darf beim zweiten Mal nicht sinken. Dann `schalte frei tarnkappe` — Meldung, kein Absturz.

> **⏸ Hier ist ein guter Schnitt.** Freischaltungen laufen, das Bestiarium ist der zweite Abend. Wenn du teilst: Commit mit `Etappe 6: Freischaltungen als Set`.

**7. Gib zwei Freischaltungen eine Wirkung.** Je eine Zeile, die mit `in freigeschaltet` fragt:

- `"panzerbrecher"` erhöht deinen Schaden pro Schuss um 3
- `"schnellladen"` lässt `nachladen` 60 statt 40 Schuss geben

`"zielhilfe"` bekommt **absichtlich keine Wirkung** und wird in der Ausbautenliste als *„kalibriert noch"* gekennzeichnet. Sie ist ein Platzhalter wie der Datenkern aus Etappe 4 — in Etappe 18 wird eine Fähigkeit daraus.

**Zum Prüfen:** Notier deinen Schaden pro Schuss, schalt den Panzerbrecher frei, feuer noch einmal. Die Zahl muss sich ändern.

**8. Bau `GEGNERTYPEN` als verschachteltes Dictionary.** Drei Typen, jeder mit zwei Texten:

| Kennung | `"lang"` | `"kurz"` |
|---|---|---|
| `"kriecher"` | Drei bis vier Sätze in deinen Worten: wie er aussieht, wie er sich bewegt, was auffällt | Ein Halbsatz |
| `"speier"` | dasselbe | dasselbe |
| `"panzerbrut"` | dasselbe | dasselbe |

Die Verschachtelung ist die aus Etappe 5 — ein Eintrag mit mehreren Eigenschaften.

**Schreib die langen Texte wirklich.** Sie sind der einzige Ort in dieser Etappe, an dem dein Spiel Atmosphäre bekommt, und sie sind in zehn Minuten geschrieben.

**9. Bestimm zu Beginn jeder Welle deren Typen.** Ein Set, das du an einer Stelle setzt:

| Welle | Typen |
|---|---|
| 1 bis 3 | `{"kriecher"}` |
| 4 bis 7 | `{"kriecher", "speier"}` |
| ab 8 | alle drei |

Eine `if`/`elif`-Kette reicht. *(In Etappe 17 ersetzt der Wellengenerator diese Kette durch ein Budget — heute ist sie genau richtig.)*

**Zum Prüfen:** Setz `welle` testweise auf 4 und starte. Dann auf 8.

**10. Melde neue Typen ausführlich, bekannte kurz.**

Zu Wellenbeginn: Für jeden Typ dieser Welle, der **noch nicht** in `gesehene_gegnertypen` steht, gib den langen Text aus. Für die übrigen den kurzen. Danach nimm alle Typen der Welle ins Set auf.

**Reihenfolge beachten** — wer zuerst aufnimmt und dann prüft, sieht nie einen langen Text. Das ist derselbe Reihenfolgefehler wie beim Abbuchen vor dem Prüfen.

*(Hier passt eine Zeile aus Konzept 10, wenn du magst: Die neuen Typen sind `wellen_typen - gesehene_gegnertypen`. Eine Schleife mit `in` tut es genauso.)*

**Zum Prüfen:** Spiel Welle 1, dann Welle 2. Beim zweiten Mal muss der Kriecher kurz gemeldet werden.

**11. Bau den Befehl `bestiarium`.**

Er zeigt alle Typen aus `gesehene_gegnertypen` mit ihrem Kurztext und schließt mit einer Zeile ab, wie viele von wie vielen erfasst sind — beide Zahlen kommen aus `len()`, keine davon steht fest im Code.

Der Befehl ist **nicht ortsgebunden** und verbraucht keine Runde. Das ist dieselbe Regel wie bei `status` seit Etappe 3b: Nachsehen ist kein Spielzug.

**Zum Prüfen:** Ruf ihn vor der ersten Welle auf. Es muss „0 von 3" dastehen und nicht abstürzen.

**12. Bau `bestiarium <kennung>` mit zwei verschiedenen Meldungen** — die Unterscheidung aus Konzept 12:

| Eingabe | Reaktion |
|---|---|
| Kennung steht nicht in `GEGNERTYPEN` | „Diesen Typ gibt es nicht." |
| Kennung steht in `GEGNERTYPEN`, aber nicht in `gesehene_gegnertypen` | „Über diesen Typ liegen dir keine Daten vor." |
| Beides vorhanden | Der lange Text |

**Die beiden ersten Meldungen dürfen sich nicht ähneln.** Wenn du sie in vier Wochen im Spiel liest, sollst du sofort wissen, welche der beiden Mengen gefehlt hat.

**13. Ersetz `stapelbar` durch ein Set.**

Aus dem Dictionary Name → Wahrheitswert aus Etappe 5, Schritt 10 wird ein Set namens `STAPELBAR` mit genau einem Eintrag: `"munition"`. Die Einträge mit `False` fallen ersatzlos weg — sie sind jetzt die, die *nicht* drinstehen.

Pass die Stelle im Kauf an, die bisher den Wahrheitswert nachgeschlagen hat. **Beantworte vorher die drei Fragen von oben schriftlich.**

⚠️ **Und notier den Preis dieses Umbaus, denn er ist echt:** Vorher war „stapelbar?" für jede Ware ausdrücklich beantwortet, und eine fehlende Antwort fiel auf. Jetzt heißt „nicht im Set" automatisch „nicht stapelbar" — eine vergessene Ware ist stillschweigend ein Einzelstück. **Du tauschst eine Fehlerquelle gegen eine andere.** Welche schlimmer ist, hängt davon ab, wie viele Waren du hast; bei drei ist das Set klar besser, bei dreißig würde ich es neu abwägen.

**Zum Prüfen:** Kauf Munition und ein Medkit. Munition muss im `vorrat` landen, das Medkit im `inventar`. Nichts an den Meldungen darf sich geändert haben.

**14. Ergänz deine Invariantenliste aus Etappe 5** um zwei Zeilen:

- Jeder Eintrag in `freigeschaltet` steht auch als Schlüssel in `AUSBAUTEN`.
- Jeder Eintrag in `gesehene_gegnertypen` steht auch als Schlüssel in `GEGNERTYPEN`.

Nur aufschreiben, nicht prüfen. **Das ist eine neue Sorte Invariante:** Sie verbindet zwei Sammlungen miteinander — dieselbe Bauart wie der inkonsistente Datenfehler aus Etappe 5, nur zwischen Set und Dictionary. In Etappe 20 werden aus solchen Sätzen Prüfungen, in Etappe 26 Tests.

**15. Spiel drei volle Wellen — der Rückwärtsgang.** Mit Bewegung, einem Kauf, einer Freischaltung und mindestens einem Bestiariumsaufruf. Kampf, Balken, Munition, Schrott, Anmarschbahn: alles muss sich verhalten wie nach Etappe 5.

**16. Committe.**

```
git add .
git commit -m "Etappe 6: Die richtige Datenstruktur"
git push
```

---

## Was NICHT in diese Etappe gehört

- ❌ **Voraussetzungen zwischen Freischaltungen** („A braucht erst B") → Etappe 18
- ❌ **Statuseffekte mit Dauer** (brennend, geschockt) → Etappe 18
- ❌ **Ein zentraler `flags`-Speicher für alles Mögliche** → Etappe 18
- ❌ **Gegnertypen mit eigenen Werten** (Trefferpunkte, Schaden, Kosten) → Etappe 11, Kosten in 17
- ❌ **Zufällig zusammengesetzte Wellen** → Etappe 17
- ❌ **Jeder Gegner als eigenes Objekt mit Typ** → Etappe 11
- ❌ **Erkenntnisse über Gegnertypen sammeln** (der Datenkern aus Etappe 4) → Etappe 15
- ❌ **Koordinaten als Tuple** → Etappe 14a
- ❌ **Set Comprehensions** (`{x for x in ...}`) → Etappe 23a
- ❌ **Funktionen, damit `schalte frei` nicht so lang wird** → Etappe 7a
- ❌ **`frozenset`** → kommt in diesem Plan nicht vor, und das ist Absicht

**Der verlockendste Punkt ist der erste.**

Du hast jetzt drei Freischaltungen, und binnen einer Viertelstunde denkst du: *Der Panzerbrecher sollte eigentlich erst gehen, wenn die Zielhilfe da ist.* Das ist eine Zeile — `if "zielhilfe" in freigeschaltet` — und sie ist verführerisch, weil sie so klein aussieht.

**Der Gedanke ist richtig, und genau deshalb gibt es Etappe 18.** Dort ist die Voraussetzung nicht eine Bedingung im Kaufbefehl, sondern **ein Eintrag in den Daten** — und dann kannst du Voraussetzungen hinzufügen, ohne Code anzufassen. Genau derselbe Unterschied wie beim Depot in Etappe 5, nur eine Stufe komplizierter. Wer die eine Zeile heute schreibt, hat in Etappe 18 nichts zu tun als sie wieder zu löschen, und die Etappe verliert ihren Anlass.

**Notier die Idee stattdessen.** In Etappe 18 holst du den Zettel hervor.

---

## Selbsttest

Prüft den Zustand deines Programms, nicht dein Gefühl. Führ jeden Punkt tatsächlich aus.

- [ ] `print(type(freigeschaltet))` meldet ein Set, kein Dictionary
- [ ] Eine ungültige Klassenwahl wird gemeldet, bevor die `elif`-Kette läuft
- [ ] `KLASSEN[0] = "x"` in einer Wegwerf-Zeile erzeugt einen `TypeError`
- [ ] `ausbauten` zeigt alle drei Einträge mit Preis, freigeschaltete sind markiert
- [ ] ⭐ Ein vierter Eintrag in `AUSBAUTEN` erscheint in der Liste, **ohne dass du die Anzeige anfasst**
- [ ] `ausbauten` außerhalb des Depots meldet, wo das Depot ist
- [ ] `schalte frei zielhilfe` funktioniert einmal und bucht Schrott ab
- [ ] ⭐ **Beim zweiten Mal sinkt der Schrott nicht** — und `freigeschaltet` enthält den Eintrag genau einmal
- [ ] `schalte frei tarnkappe` meldet, dass es das nicht gibt, und stürzt nicht ab
- [ ] Freischalten mit zu wenig Schrott meldet das — und bucht **nichts** ab
- [ ] Der Panzerbrecher verändert deinen Schaden pro Schuss nachweisbar
- [ ] Der erste Kriecher der ersten Welle bekommt den langen Text
- [ ] ⭐ Der Kriecher der zweiten Welle bekommt den kurzen Text
- [ ] Bei `welle = 4` erscheint der Speier zum ersten Mal — mit langem Text
- [ ] `bestiarium` vor der ersten Welle zeigt „0 von 3" und stürzt nicht ab
- [ ] `bestiarium` verbraucht keine Runde
- [ ] `bestiarium hubschrauber` und `bestiarium panzerbrut` (ungesehen) melden **verschiedene** Dinge
- [ ] Kaufen von Munition landet weiterhin im `vorrat`, ein Medkit weiterhin im `inventar`
- [ ] **Drei volle Wellen** lassen sich spielen — mit Bewegung, Kauf, Freischaltung und Bestiarium — ohne Absturz

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten. Dein Mentor fragt sie ab.

1. **Was ist der Unterschied zwischen „ich prüfe, ob es schon drin ist" und „es kann nicht doppelt drin sein"?** Und was garantiert ein Set trotzdem *nicht*?
2. Nenn zwei Gründe, ein Set statt einer Liste zu nehmen. Welcher der beiden zählt in deinem Spiel wirklich?
3. Warum kann ein Set keine Listen enthalten, aber Tuples schon? *(Ein Satz.)*
4. Was genau ist an einem Tuple unveränderlich — und was nicht?
5. Was ist der Unterschied zwischen `(5)` und `(5,)`, und woran entscheidet Python das?
6. Was liefert `.items()` für jeden Eintrag zurück — und was hat das mit Tuples zu tun?
7. Nenn die vier Fragen der Entscheidungshilfe in der richtigen Reihenfolge. Warum ist die Reihenfolge nicht egal?
8. Wo wäre ein Set in deinem Spiel die **falsche** Wahl, und was würde dabei kaputtgehen?
9. Was macht `{}` — und wie schreibt man ein leeres Set?
10. Nenn die zwei Sorten Nein an einem Beispiel aus deinem eigenen Spiel.
11. Warum ist `KLASSEN` ein Tuple und nicht einfach eine Liste? *(Was gewinnst du, was verlierst du?)*

**Frage 1 ist die wichtigste.** Alles andere ist Werkzeugwissen, und Werkzeugwissen holt man nach. Der Unterschied zwischen einer Regel, die im Code steht, und einer Regel, die in der Struktur steht, ist dagegen ein Denkwerkzeug — es entscheidet, ob ein Programm mit jeder neuen Stelle unsicherer wird oder nicht. Und der zweite Halbsatz gehört dazu: Wer nur die halbe Regel gelernt hat, baut den Kaufvorgang, der zweimal abbucht.

---

## Transferaufgabe (10 Minuten)

**Außerhalb des Spiels**, in einer Wegwerf-Datei. Eine Werkstatt, kein Vorposten.

1. Bau zwei **Listen** mit Ausrüstungsteilen, die sich teilweise überschneiden — sechs Einträge pro Liste, drei davon gleich.
2. Finde **ohne Schleife** heraus, welche in beiden vorkommen. Eine Zeile, wenn du das richtige Werkzeug wählst. *(Denk daran, dass Listen das nicht können — irgendetwas musst du vorher tun.)*
3. Finde heraus, was **nur in der ersten** vorkommt.
4. Häng an die erste Liste einen Eintrag an, den sie schon enthält. Wiederhol Schritt 2. Was ändert sich am Ergebnis, und warum?
5. **Und der eigentliche Punkt:** Gib das Ergebnis aus Schritt 2 dreimal hintereinander aus, jedes Mal in einem neu gestarteten Programm. Notier, ob die Reihenfolge gleich bleibt.

Schritt 5 ist der Grund, warum diese Aufgabe existiert. Wenn du je Ausgaben aus einem Set sortiert brauchst, sortierst du beim Ausgeben — die Struktur tut es nicht.

---

## Kaputtmachen

**Vor jedem Experiment aufschreiben, was passieren wird.** Die ersten fünf gehören dazu, die letzten drei sind Kür.

**1. Schreib `freigeschaltet = {}` statt `set()`** und ruf danach `.add("zielhilfe")` auf. Lies die Fehlermeldung. Ruf dann `len({})` und `bool({})` auf und vergleich mit dem Set — an welcher Stelle hättest du den Unterschied gemerkt, und an welchen nicht?

**2. Änder `KLASSEN`.** Versuch, einen Eintrag zu überschreiben, und dann, einen anzuhängen. Zwei verschiedene Fehlermeldungen. Lies beide ganz.

**3. Lass beim Bestiarium das `add()` vor der Prüfung laufen.** Spiel Welle 1. Was siehst du — und was siehst du nie wieder?

**4. Schreib in Schritt 6 die zweite Prüfung weg** („steht sie schon in `freigeschaltet`?"). Schalt dieselbe Ausbaute dreimal frei.

⭐ **Das ist der Typ-3-Fehler dieser Etappe:** Kein Absturz, keine Meldung, `freigeschaltet` sieht danach vollkommen korrekt aus — genau ein Eintrag, wie es sein soll. Nur der Schrott ist dreimal weg. **Die Datenstruktur ist sauber und das Spiel ist kaputt.** Das ist Konzept 4 von der unangenehmen Seite, und es ist der Grund, warum dort der Zusatz steht.

**5. ⭐ Bau die Anmarschbahn einmal über ein Set.**

Statt deine Gegnerpositionen einzeln in die Bahn zu schreiben: Bau ein Set aus allen besetzten Feldern und prüf beim Zeichnen für jedes Feld mit `in`, ob es besetzt ist. Nur zum Ausprobieren, in einer Kopie.

Führ es aus und vergleich die Bahn mit der alten. Dann **stell zwei Gegner auf dasselbe Feld** und vergleich `len(gegner)` mit der Länge deines Sets.

**Beantworte danach, bevor du weiterliest:**
1. Sehen die beiden Bahnen gleich aus?
2. Welche der beiden Zahlen ist die Wahrheit über deine Welle?
3. Was wäre passiert, wenn du das Set nicht nur zum Zeichnen, sondern als *Speicher* für die Gegner benutzt hättest?

Das ist die Zusage „keine Duplikate" an einer Stelle, an der sie schadet. Antworten in `GELERNT.md`. *(In Etappe 14b kommt genau diese Bauart wieder — dort deckt ein Geschütz Felder ab, und da ist das Set richtig, weil ein Feld nur einmal abgedeckt sein kann.)*

---

Die folgenden drei sind Kür.

**6. Leg ein Set an, das ein Tuple mit einer Liste darin enthalten soll** — `{([1, 2], 3)}`. Erklär die Fehlermeldung mit Konzept 7.

**7. Lass ein Komma weg.** Bau eine Funktion, die `return 5, 7` macht, und dann eine mit `return (5)`. Pack beide Ergebnisse mit `a, b = ...` aus. Welche Fehlermeldung bekommst du, und an welcher Zeile — an der Rückgabe oder am Auspacken?

**8. Sortier ein Set.** Ruf `sorted()` darauf auf und sieh dir an, was zurückkommt. Ist das noch ein Set?

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `AttributeError: 'dict' object has no attribute 'add'` | `{}` statt `set()` beim Anlegen | Die Zeile, in der die Sammlung entsteht |
| `TypeError: 'set' object is not subscriptable` | Zugriff mit `[0]` auf ein Set | Sets haben keine Positionen — Konzept 3 |
| `TypeError: unhashable type: 'list'` | Eine Liste in ein Set gelegt oder als Dictionary-Schlüssel benutzt | Konzept 5 |
| `TypeError: 'tuple' object does not support item assignment` | Ein Tuple verändert | Entweder Liste nehmen oder neu bauen — Konzept 7 |
| `KeyError` bei `.remove()` auf einem Set | Element war nicht drin | `.discard()` nimmt es hin, `.remove()` nicht |
| Die Reihenfolge der Ausgabe ändert sich zwischen zwei Läufen | Sets haben keine Reihenfolge | Beim **Ausgeben** sortieren, nicht beim Speichern |
| Der lange Bestiariumstext erscheint nie | `add()` läuft vor der Prüfung | Auftragsschritt 10, Reihenfolge |
| Der lange Text erscheint **jedes Mal** | Der Typ wird nie ins Set aufgenommen | Dieselbe Stelle, andere Hälfte |
| Kein Fehler, aber Schrott verschwindet mehrfach | Die „schon freigeschaltet?"-Prüfung fehlt | Auftragsschritt 6 |
| `a, b = paar` scheitert mit „too many values to unpack" | Links stehen weniger Namen als rechts Werte | Was liefert die rechte Seite wirklich? |
| Zwei Gegner, aber nur einer auf der Bahn | Positionen in ein Set gelegt, Duplikat verschluckt | Kaputtmach-Experiment 5 |

**Der Debugging-Reflex dieser Etappe: „Welche Struktur ist das eigentlich?"**

Der Reflex aus Etappe 1 kommt zurück, und zwar aus einem neuen Grund: Ab heute sehen sich deine Strukturen zum ersten Mal ähnlich. `{}` ist ein Dictionary, `{"a"}` ein Set. `(5)` ist eine Zahl, `(5,)` ein Tuple. `d.keys()` sieht aus wie ein Set und ist keines.

```python
print("### TYP", type(freigeschaltet), freigeschaltet)
```

**Typ und Inhalt in einer Zeile.** Der Inhalt allein reicht nicht mehr — `{'zielhilfe'}` und `{'zielhilfe': True}` unterscheiden sich um zwei Zeichen und um alles.

**Nachsehen schlägt Vermuten** — der Grundsatz seit Etappe 1, das fünfte Werkzeug in derselben Reihe. In Etappe 8 löst der Debugger alle fünf ab.

---

## Ein Blick nach vorne

**Etappe 7a** räumt deine Befehlskette auf. Sie ist heute um zwei Befehle gewachsen, und `schalte frei` hat vier Prüfungen — beides Material für die erste Funktion, die wirklich etwas leistet.

**Etappe 11** löst deine `elif`-Kette der Klassenwerte durch vier Python-Klassen ab. `KLASSEN` überlebt das: Aus dem Tuple wird die Liste der verfügbaren Klassen, an der dein Programm prüft, was es überhaupt gibt.

**Etappe 12** lässt den Tick über deine Einheiten laufen — und die Schleifenform dabei ist das Tuple-Unpacking aus Konzept 9.

**Etappe 14b** gibt einem Geschütz Reichweite. Die abgedeckten Felder sind ein Set aus Koordinaten-Tuples: die Struktur von heute, angewandt auf Daten, die es heute noch nicht gibt. Und dort ist die Duplikatsregel richtig herum — ein Feld kann nur einmal abgedeckt sein.

**Etappe 15** baut auf `gesehene_gegnertypen` das Erkenntnissystem auf. Der Datenkern aus Etappe 4 wird dort endlich zu etwas.

**Etappe 17** ersetzt deine `if`/`elif`-Kette aus Schritt 9 durch einen Wellengenerator mit Budget. Deine Typen bekommen dort Kosten, und ab da ist jede Welle anders.

**Etappe 18** macht aus `freigeschaltet` den zentralen Flag-Speicher des Spiels — und dann weißt du, warum es ein Set ist und keine Liste. Dort kommen Voraussetzungen dazu, und die Frage *„was fehlt mir noch?"* ist die Differenzmenge aus Konzept 10.

**Etappe 19** speichert. Dann wird die Frage aus Konzept 14 fällig: Sets und Tuples überleben JSON nicht, und du musst entscheiden, was du beim Laden wieder zurückverwandelst.

**Etappe 21a** gibt zwei Werte auf einmal zurück. Das ist die Komma-Falle aus Konzept 8, dann als Werkzeug statt als Stolperstein.

---

## Abschluss

**In `GELERNT.md`:**

- Was habe ich gebaut?
- Was habe ich verstanden?
- Was hat mich überrascht? *(Kandidaten: `{}` ist ein Dictionary · `(5)` ist keine Klammer, sondern eine Zahl · `.items()` liefert seit Etappe 5 Tuples)*
- Welchen Fehler habe ich gemacht — und **wie habe ich ihn gefunden?**
- **Entscheidung 1:** Kennt die Welle die Typen oder der einzelne Gegner — und warum?
- **Entscheidung 2:** Was passiert beim zweiten Freischalten?
- **Die vier Fragen der Entscheidungshilfe**, in der richtigen Reihenfolge, aus dem Kopf
- **Wo wäre in meinem Spiel ein Set die falsche Wahl — und warum?**
- **Was ein Set garantiert und was nicht** *(der Satz aus Konzept 4, in eigenen Worten)*
- Die Antworten aus Kaputtmach-Experiment 5 (die zwei Zahlen, und welche die Wahrheit ist)
- **Zwei neue Invarianten** aus Auftragsschritt 14
- Der Preis des `STAPELBAR`-Umbaus: welche Fehlerquelle ich gegen welche getauscht habe
- Die Idee für Etappe 18, die ich heute **nicht** gebaut habe

**Commit:**

```
git add .
git commit -m "Etappe 6: Die richtige Datenstruktur"
git push
```

---

## Wenn du mehr willst

Erst bei grünem Selbsttest. Alles hier ist freiwillig.

**Die Ausbautenliste sortiert nach Preis.** `sorted()` mit dem passenden Schlüssel — und du merkst, dass ein Dictionary sich sortiert ausgeben lässt, ohne dass sich am Dictionary etwas ändert. Zwei Zeilen, und die Vorarbeit für den `lambda`-Sortierschlüssel aus Etappe 23a.

**Ein Ausbau, der Schrott zurückgibt.** Ein Eintrag, den man wieder abgeben kann: `discard()` statt `add()`, halber Preis zurück. Kostet fünf Minuten und zeigt, dass ein Set in beide Richtungen funktioniert.

**Ein Zähler neben dem Set.** Wie oft ist dir jeder Typ begegnet? Das ist ausdrücklich **kein** Set — es ist ein Dictionary Typ → Anzahl, und der Punkt der Übung ist, dass du beide nebeneinander hast und an jeder Stelle weißt, welches du gerade brauchst.

**⭐ Ein vierter Eintrag in `GEGNERTYPEN`, den keine Welle jemals ausspuckt.**

Trag einen Typ ein, der in Schritt 9 in keiner Wellenzusammenstellung vorkommt. Dein Bestiarium zählt ab sofort „2 von 4" — und der vierte Platz bleibt leer, egal wie lange man spielt.

Das ist der beste Zusatz dieser Etappe, aus demselben Grund wie der Datenkern in Etappe 4 und die Werkbank in Etappe 5: **Ein Spiel wird groß, wenn es zeigt, dass es größer ist als das, was man gesehen hat.** Der Eintrag kostet dich zwei Minuten. In Etappe 17 baust du den Wellengenerator, und dann entscheidest du, ab welcher Welle dieser Typ zum ersten Mal wirklich anrückt.

---

> **Nächste Etappe:** [Etappe 7 — Aufräumen](etappe-07-aufraeumen.md) · Funktionen, Parameter, Rückgabewerte, Scope
