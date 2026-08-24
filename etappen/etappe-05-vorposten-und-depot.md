# Etappe 5 — Der Vorposten und das Depot

> **Block 1: Fundament** · Etappe 5 von 30 · [← Etappe 4](etappe-04-ausruestung-und-beute.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 6 →](etappe-06-datenstrukturen.md)

**Boot.dev:** Dictionaries, verschachtelte Dictionaries, `.keys()` / `.values()` / `.items()`
**Zeitaufwand:** 4–6 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 4 abgeschlossen, Selbsttest grün

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Sektorenkarte, Bewegung, Depot, Kaufvorgang, Vorrat | Flach oder verschachtelt? · `.get()` gegen eckige Klammern · warum der Kauf keine Warennamen kennt | `.keys()` / `.values()` als eigene Objekte · warum Schlüssel unveränderlich sein müssen |

**Diese Etappe ist groß.** Sie ist nicht offiziell geteilt, aber es gibt einen sauberen Schnitt in der Mitte — er steht im Auftrag zwischen Schritt 8 und 9. Nimm ihn, wenn dir die Luft ausgeht.

---

## Worum es geht

Dein Vorposten hat seit Etappe 3 zwanzig Wellen und seit Etappe 4 ein Inventar. Was er nicht hat, ist ein **Ort**.

Alles passiert nirgendwo. Du feuerst, du nimmst Schrott auf, du siehst eine Anmarschbahn — aber es gibt keine Stelle, an der du stehst, keine, an der du nicht stehst, und nichts, wohin du gehen könntest. Ein Vorposten ohne Räume ist eine Zahlenkolonne mit Atmosphäre.

Und daneben liegt ein zweites Problem, das du selbst mitgebracht hast. In Etappe 4 hast du Schrott aufgesammelt. Zwei Stück Schrott stehen zweimal als `"schrott"` in deiner Liste. Bei fünfzig Stück wird das lächerlich — und du hast damals gemerkt, dass dir hier etwas fehlt.

**Beides braucht dasselbe Werkzeug, und es ist eines der wichtigsten in Python:**

> **Ein Dictionary ordnet einem Schlüssel einen Wert zu.**

Mehr ist es nicht. Und daraus wird heute eine Karte, eine Wirtschaft, und der erste Moment, in dem dein Programm etwas kann, was du nicht hineinprogrammiert hast: **eine neue Ware ins Depot legen, ohne die Kauflogik anzufassen.**

**Warum das der eigentliche Punkt der Etappe ist:** Bis heute hast du Code geschrieben, der Werte kennt. Ab heute schreibst du Code, der Werte *nachschlägt*. Der Unterschied klingt akademisch und ist der Grund, warum in Etappe 25 dreißig Gegnertypen in einer Textdatei stehen können, ohne dass eine Zeile Python dazukommt.

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

Zwei Fragen. Beide haben mehr als eine vertretbare Antwort, beide haben Folgen, die du erst in Monaten siehst. Schreib deine Wahl **und die Begründung** in `GELERNT.md`.

### Entscheidung 1 — Der versiegelte Weg ⭐

Die Landeplattform ist nicht erreichbar. Der Osttunnel ist verschüttet, und das bleibt er, bis du ihn in Etappe 13 freiräumst.

Wie steht das in deiner Karte?

| | Der Weg fehlt einfach | Der Weg existiert und ist markiert |
|---|---|---|
| In den Daten | Bei `osttor` steht kein Eintrag Richtung Plattform | Der Eintrag ist da, aber gekennzeichnet |
| Der Spieler sieht | nichts | „Nach Osten: verschüttet" |
| Freiräumen heißt | einen Eintrag **erzeugen** | einen Wert **ändern** |
| Erzählerisch | Es gibt dort nichts | Es gibt dort etwas, und du kommst nicht ran |

**Die Frage dahinter:** Ist ein blockierter Weg eine Abwesenheit oder ein Zustand?

Ein sichtbar blockierter Weg ist ein Versprechen an den Spieler — er weiß, dass da etwas ist, und will hin. Ein fehlender Weg ist nichts; wenn er in Etappe 13 plötzlich auftaucht, wirkt er nicht wie ein Durchbruch, sondern wie ein Fehler.

Technisch hängt daran, ob das Freiräumen in Etappe 13 eine Zeile ist oder ein Umbau. **Ich sage dir nicht, welche Variante du nehmen sollst** — aber schreib auf, welche du genommen hast, denn in Etappe 13 schlagen wir hier nach.

**Meine Empfehlung für heute: Lass den Weg fehlen.** Die Landeplattform bleibt außerhalb des erreichbaren Kartenteils, und der Spieler erfährt von ihr durch die Beschreibung des Osttors, nicht durch einen Ausgang. Das ist die kleinere Aufgabe, und du hast heute genug vor.

**Wenn du die markierte Variante trotzdem willst** — sie ist erzählerisch die bessere —, dann bau sie so und nicht anders:

Ein Eintrag `"osten": "landeplattform"` sagt nur, *wohin* es geht, nicht dass es nicht geht. Die Blockade braucht also einen eigenen Platz. **Nimm dafür ein zweites, flaches Dictionary im Sektor** — Richtung → Grund:

```
"nachbarn":  {"osten": "landeplattform"}
"blockiert": {"osten": "Der Osttunnel ist verschüttet."}
```

Zwei Tabellen, jede beantwortet eine Frage. Deine Bewegung hat dann drei Fälle statt zwei:

```
Richtung gibt es nicht      →  „Da ist keine Tür."
Richtung gibt es, blockiert →  der Grund aus der zweiten Tabelle
Richtung gibt es, frei      →  gehen
```

**Bau den Nachbarwert nicht selbst zu einem Dictionary aus.** Das wäre eine dritte Verschachtelungsebene, und die brauchst du heute nirgends. Zwei flache Tabellen nebeneinander sind hier die einfachere Lösung — und in Etappe 22 siehst du, wann es sich lohnt, sie zu einer zusammenzuziehen.

### Entscheidung 2 — Hat das Depot einen Bestand?

Bisher ist das Depot ein Katalog: Ware → Preis. Du kannst unendlich oft dasselbe kaufen.

**Willst du das?** Wenn nein, brauchst du pro Ware einen zweiten Wert — und damit wird aus dem flachen Dictionary ein verschachteltes:

```
ohne Bestand:  ware → preis
mit Bestand:   ware → { preis, bestand }
```

Das ist kein kleiner Unterschied. Jeder Zugriff bekommt eine Ebene mehr, und jede Stelle, die den Preis liest, muss angepasst werden. **Genau deshalb steht die Frage hier und nicht in drei Wochen.**

Und wenn du dich für Bestand entscheidest, kommt eine zweite Frage hinterher: Was passiert bei Bestand 0? Fliegt die Ware aus dem Dictionary, oder bleibt sie mit einer Null drin und wird als ausverkauft angezeigt? Das entscheidet, wie leicht Etappe 22 wird, wenn Waren Voraussetzungen und Ausbaustufen bekommen.

**Mein Rat, und es ist nur einer:** Bau heute ohne Bestand. Du hast genug vor. Notier die Frage, und wenn sie dich in zwei Wochen noch juckt, ist der Umbau eine gute Übung.

---

## Die Konzepte

Alle Beispiele hier laufen absichtlich **außerhalb** deines Spiels. Und wie in Etappe 4 gilt: Ein Dictionary ist ein Objekt, du kannst es fragen, was es kann.

```python
dir({})              # alles, was ein Dictionary kann
help({}.get)         # was eine bestimmte Methode tut
```

### 0. Drei Wörter, die heute nicht durcheinandergeraten dürfen

Du baust heute drei Sammlungen, die alle mit Gegenständen zu tun haben. Wenn du sie verwechselst, verwechselst du sie den Rest des Projekts:

| Wort | Was es ist | Wem es gehört | Struktur |
|---|---|---|---|
| **Depot** (`waren`) | Der Katalog: was man kaufen *kann*, und was es kostet | dem Vorposten | Dictionary Ware → Preis |
| **Vorrat** (`vorrat`) | Gezählte Ressourcen: Schrott, Munition | dem Spieler | Dictionary Name → Anzahl |
| **Inventar** (`inventar`) | Einzelne Gegenstände, die man trägt | dem Spieler | Liste (aus Etappe 4) |

**Das Depot hat keinen Bestand** — es ist eine Preisliste, kein Lager. Wenn später von „Bestand" die Rede ist, ist immer der Vorrat des Spielers gemeint.

⚠️ **Und eine Entscheidung, die heute fällt und die du sauber durchziehen musst:**

> **Ab heute ist Schrott kein Inventargegenstand mehr. Er ist eine Ressource.**

In Etappe 4 lag Schrott in deiner `inventar`-Liste, weil du nichts Besseres hattest — und zweimal `"schrott"` untereinander war der Grund, warum diese Etappe existiert. Ab heute wird er **gezählt** statt gelegt: Aufsammeln erhöht `vorrat["schrott"]`, und in der Inventarliste taucht er nicht mehr auf.

**Prüf das ausdrücklich, wenn du Schritt 9 gebaut hast.** Wenn Schrott gleichzeitig in `inventar` und in `vorrat` steht, hast du ihn zweimal — und irgendwann verkaufst oder verbrauchst du eines von beidem, und der Rest bleibt stehen. Das ist keine Kleinigkeit, sondern zwei Wahrheiten über dieselbe Sache.

Dieselbe Frage stellt sich für Munition. Für Medkit und Panzerplatte nicht — die bleiben Einzelstücke.

Diese drei Wörter benutzt der Guide ab hier konsequent. Benutz sie in deinem Code genauso.

### 1. Schlüssel und Wert

```python
farben = {"rot": "#ff0000", "blau": "#0000ff"}
telefonbuch = {"mueller": "0211 55512", "sahin": "0211 55588"}
```

Links vom Doppelpunkt der **Schlüssel**, rechts der **Wert**. Geschweifte Klammern statt eckiger.

**Der Unterschied zur Liste ist nicht die Klammer, sondern die Frage, die man stellt.**

| | Liste | Dictionary |
|---|---|---|
| Zugriff über | Position (`werkzeuge[0]`) | Name (`farben["rot"]`) |
| Die Frage | „Was ist das dritte?" | „Was gehört zu *rot*?" |
| Reihenfolge | **ist** der Zugriffsweg | ist **nicht** der Zugriffsweg |

Eine Liste ist eine Reihe. Ein Dictionary ist ein Nachschlagewerk. Und Nachschlagewerke schlägt man nicht der Reihe nach auf.

*(Genauer, weil es sonst später irritiert: Ein Dictionary **merkt** sich seit Python 3.7 durchaus, in welcher Reihenfolge du Einträge angelegt hast — beim Durchlaufen kommen sie so heraus. Nur **adressieren** kannst du darüber nichts. `waren[0]` gibt es nicht.)*

Ein leeres Dictionary ist `{}`. Genau wie die leere Liste ist es falsy — die Regel aus Etappe 2 gilt weiter.

### 2. Zugriff, und der Fehler dabei

```python
farben["rot"]        # "#ff0000"
farben["gruen"]      # KeyError: 'gruen'
```

`KeyError` heißt: Diesen Schlüssel gibt es nicht. Das ist wie der `IndexError` aus Etappe 4 — ein **angenehmer** Fehler, weil er sofort abstürzt und genau sagt, was fehlte.

Neue Einträge entstehen durch schlichtes Zuweisen:

```python
farben["gruen"] = "#00ff00"      # legt an
farben["rot"] = "#cc0000"        # überschreibt
```

⚠️ **Und hier eine Falle, die es bei Listen nicht gibt:** Beide Zeilen sehen identisch aus. Die eine legt an, die andere überschreibt — und Python sagt dir nicht, welche von beiden gerade passiert ist. Ein Tippfehler im Schlüssel erzeugt keinen Fehler, sondern **einen neuen Eintrag**, den niemand je liest.

Das ist ein Fehler vom Typ 3, und du wirst ihn heute mindestens einmal bauen.

### 3. `.get()` — fragen, ohne abzustürzen

```python
farben.get("gruen")              # None
farben.get("gruen", "#000000")   # "#000000"
```

`.get()` liefert `None` statt eines Fehlers — oder einen Ersatzwert, wenn du einen mitgibst.

**Wann nimmst du was?** Die Frage ist nicht Geschmack:

> **Eckige Klammern, wenn ein fehlender Schlüssel ein Fehler wäre. `.get()`, wenn er ein normaler Fall ist.**

Beim Nachschlagen eines Sektors, den dein eigener Code eingetragen hat, wäre ein fehlender Schlüssel ein Bug — da willst du den Absturz. Bei der Eingabe eines Spielers, der `kaufe hubschrauber` tippt, ist Fehlen der Normalfall — da willst du eine Meldung.

*(In Etappe 20 lernst du die dritte Bauweise: es versuchen und den Fehler auffangen. Dann verstehst du auch, warum `.get()` oft die freundlichere Lösung ist.)*

### 4. `in` prüft den **Schlüssel** ⭐

```python
"rot" in farben          # True
"#ff0000" in farben      # False  ← obwohl die Farbe drin ist
```

Über diesen Stolperstein fällt fast jeder einmal. `in` schaut bei einem Dictionary **nur links vom Doppelpunkt**. Der Wert interessiert es nicht.

Wenn du wirklich nach Werten suchen willst: `in farben.values()`. Merk dir, dass das eine andere Frage ist — und in Etappe 6 lernst du, warum sie auch anders teuer ist.

### 5. Verschachtelung — ein Dictionary im Dictionary

```python
gewuerze = {
    "kreuzkuemmel": {"regal": 2, "menge_g": 40, "gemahlen": True},
    "safran":       {"regal": 1, "menge_g": 2,  "gemahlen": False},
}
```

Zugriff Schritt für Schritt:

```python
gewuerze["safran"]                # das innere Dictionary
gewuerze["safran"]["menge_g"]     # 2
```

**Lies von links nach rechts:** Der erste Schlüssel liefert ein Dictionary, der zweite greift darin zu. Nicht mehr Magie als das.

**Und jetzt die Frage, um die es eigentlich geht — wann verschachtelt man?**

> **Wie viele Eigenschaften hat ein Eintrag? Eine → flach. Mehrere → verschachtelt.**

Ein Preis ist eine Zahl. `{"medkit": 40}` reicht. Ein Sektor hat eine Beschreibung, eine Integrität und Nachbarn — da reicht es nicht.

**Verschachtelung ist kein Qualitätsmerkmal.** Sie ist die Antwort auf eine Frage, und wenn die Frage nicht gestellt wurde, ist sie nur eine Ebene, durch die man sich jedes Mal durchtippt. Du baust heute beide Formen nebeneinander, damit du den Unterschied an deinem eigenen Code siehst.

### 6. Iterieren — und was du dabei bekommst

```python
for name in gewuerze:                        # nur die Schlüssel
for name, daten in gewuerze.items():         # Schlüssel und Wert
```

**Die erste Form überrascht viele:** Läuft man direkt über ein Dictionary, bekommt man die **Schlüssel**, nicht die Werte und nicht beides.

`.items()` liefert beides auf einmal. Das ist die zweite der drei Schleifenformen aus Etappe 4 — dort standen sie als 👀-Vorschau, heute baust du sie.

👀 **`.keys()` und `.values()`** liefern dasselbe einzeln. Du brauchst sie selten (`for name in gewuerze` tut schon dasselbe wie `.keys()`), aber du wirst sie in fremdem Code sehen. Ein Satz reicht.

⚠️ **Und die Falle von Etappe 4, präziser gefasst:** Verändere während einer Schleife nicht die **Größe** des Dictionaries — also keine Einträge anlegen oder löschen.

Die **Werte** zu ändern ist dagegen erlaubt:

```python
for name in gewuerze:
    gewuerze[name]["menge_g"] += 10      # in Ordnung
    del gewuerze[name]                    # nicht in Ordnung
```

Bei einem Dictionary ist Python dabei strenger als bei einer Liste: Es bricht mit `RuntimeError: dictionary changed size during iteration` ab. Eine Liste lässt dich gewähren und liefert danach ein falsches Ergebnis.

**Der Abbruch ist ein Geschenk**, auch wenn er sich nicht so anfühlt — du vergleichst beides im Kaputtmach-Teil.

### 7. Nicht alles darf Schlüssel sein 👀

```python
d = {["a", "b"]: 1}      # TypeError: unhashable type: 'list'
```

**Die Regel für heute:** Strings, Zahlen und Tuples funktionieren als Schlüssel. Listen nicht.

Der Fachbegriff steht in der Fehlermeldung: ein Schlüssel muss **hashbar** sein. Das hängt eng mit *mutable* und *immutable* aus Etappe 4 zusammen — was sich ändern kann, taugt schlecht als Adresse. Ganz deckungsgleich sind die beiden Begriffe aber nicht, und für heute musst du den Unterschied nicht kennen.

*(Eine Feinheit, falls du sie ausprobierst: Ein Tuple funktioniert nur, solange **alles darin** ebenfalls hashbar ist. `(1, 2)` geht, `([1, 2], 3)` nicht.)*

Mehr brauchst du heute nicht. In Etappe 6 wird daraus die Frage, warum ein Set keine Listen aufnimmt, und in Etappe 14a ist es der Grund, warum Koordinaten Tuples sind.

### 8. Der Kauf, der keine Warennamen kennt ⭐

**Das ist der wichtigste Abschnitt dieser Etappe.**

Ohne Dictionary sähe dein Depot so aus:

```python
# so nicht — nur zum Anschauen
if ware == "medkit":
    preis = 40
elif ware == "munition":
    preis = 15
elif ware == "panzerplatte":
    preis = 90
```

Das funktioniert. Und jede neue Ware ist ein neuer Zweig — also eine Änderung an deinem Code, ein Test, ein Commit.

Mit einem Dictionary schlägst du den Preis nach, statt ihn abzufragen. Die Kauflogik enthält danach **kein einziges Warenwort mehr**. Sie kennt nur noch: den Namen, den der Spieler getippt hat, und die Tabelle, in der sie nachschlägt.

> **Eine neue Ware ist dann eine Änderung an den Daten und keine Änderung an der Logik.**

*(Nicht „eine Zeile" — in Etappe 22 hat eine Ware Kosten, Bauzeit und Voraussetzungen, dann sind es mehrere. Der Satz bleibt trotzdem wahr, und darauf kommt es an.)*

⭐ **Und jetzt die Einschränkung, die wichtiger ist als der Satz selbst.** Sie gilt nur unter einer Bedingung:

> **Eine neue Ware kommt nur dann ohne Logikänderung aus, wenn *alles*, was die Logik über sie wissen muss, in den Daten steht.**

Sobald deine Kauflogik etwas braucht, das nirgends hinterlegt ist — ob eine Ware stapelbar ist, zum Beispiel —, fällt sie auf eine Fallunterscheidung zurück, und der Vorteil ist weg.

**Das ist der Grund, warum in Auftragsschritt 10 die Stapelbarkeit *vor* dem Kauf hinterlegt wird.** Und es ist die Frage, die dich bis Etappe 25 begleitet: Nicht *„sind meine Daten in einem Dictionary?"*, sondern **„steht dort alles, was mein Code fragen wird?"**

Probier es aus, sobald dein Kauf läuft: Füge eine vierte Ware hinzu, ohne die Kauffunktion anzufassen. Wenn das klappt, hast du heute das Prinzip verstanden, um das es in Etappe 22 und 25 vollständig geht — und du hast es nicht gelesen, sondern gebaut.

**Ehrlich eingeordnet:** Die `elif`-Kette ist nicht *falsch*. Bei drei Waren, die sich nie ändern, ist sie völlig in Ordnung und sogar leichter zu lesen. Der Unterschied entsteht durch Wachstum. Merk dir die Frage, nicht das Verdikt: **Ändert sich diese Liste? Dann sind es Daten.**

### 9. Kennung und Anzeigename — die zweite Einlösung aus Etappe 4

In Etappe 4 hast du entschieden, ob in deinem Inventar `"munitionskasten"` steht oder `"Munitionskasten (halbvoll)"`. Damals stand dabei: *Wer sich für die Kennung entscheidet, braucht irgendwo eine zweite Stelle, an der steht, wie eine Kennung schön heißt.*

**Diese zweite Stelle ist heute da.** Ein Dictionary ist genau das: eine Übersetzungstabelle.

```python
# fremdes Beispiel
anzeige = {"kreuzkuemmel": "Kreuzkümmel, gemahlen", "safran": "Safranfäden"}
print(anzeige["safran"])
```

Der Schlüssel ist knapp, kleingeschrieben und wird verglichen. Der Wert ist schön und wird angezeigt. **Zwei Aufgaben, zwei Werte** — und die eine Regel dazu lautet:

> **Verglichen wird immer die Kennung. Angezeigt wird immer der Anzeigename.**

⚠️ **Und jetzt prüf deine Entscheidung aus Etappe 4 nach**, denn hier kann sie dir auf die Füße fallen:

- **Du hast Kennungen gewählt.** Gut. Deine Warentabelle benutzt dieselben Kennungen, `kaufe medkit` funktioniert direkt, und die Anzeigenamen sind eine Tabelle mehr — oder du lässt sie ganz weg und lebst mit karger Ausgabe.
- **Du hast Anzeigenamen gewählt.** Dann steht in deinem Inventar `"Medkit (klein)"`, und der Spieler tippt `kaufe medkit`. Das passt nicht zusammen, und du merkst es heute zum ersten Mal.

**Wenn du in der zweiten Lage bist: Das ist kein Fehler von dir, sondern die Rechnung für eine Entscheidung.** Genau das war der Sinn der Übung. Du hast zwei Wege — auf Kennungen umstellen (zwanzig Minuten) oder die Eingabe des Spielers auf den Anzeigenamen übersetzen (mühsamer, und es wird mit jedem Gegenstand mühsamer).

Notier, wofür du dich entscheidest. In Etappe 11 bekommt jeder Gegenstand **beides** — `item.id` und `item.name` —, und dann ist die Frage endgültig erledigt. In Etappe 25 wird aus der Kennung der JSON-Schlüssel.

### 10. Mengen — die dritte Einlösung aus Etappe 4

In Etappe 4 stand ein Satz, der damals wie eine Randnotiz aussah: *Zwei Stück Schrott zweimal als `"schrott"` einzutragen funktioniert und wird bei fünfzig Stück lächerlich.*

Heute hast du das Werkzeug dafür. **Ein Dictionary aus Name → Anzahl:**

```python
# fremdes Beispiel: was in der Vorratskammer steht
vorrat = {"mehl_kg": 3, "eier": 12, "zucker_kg": 1}
vorrat["eier"] -= 2
```

Zwölf Eier sind ein Eintrag, nicht zwölf. Und der entscheidende Vorteil ist derselbe wie in Konzept 8: **Der Code, der etwas hinzufügt, muss den konkreten Namen nicht kennen.**

*(Die Struktur kennt er sehr wohl — er weiß, dass es ein Dictionary aus Namen und Anzahlen ist. Das ist der Unterschied zwischen „datengetrieben" und „weiß von nichts", und er ist wichtig: Datengetrieben heißt nicht ahnungslos, sondern **nicht auf einzelne Werte festgelegt**.)*

**Und damit trennt sich dein Inventar in zwei Hälften** — genau entlang der Frage aus Etappe 4:

| | Menge | Einzelnes Ding |
|---|---|---|
| Beispiele | Schrott, Munition | Medkit, Panzerplatte, Datenkern |
| Frage, die man stellt | „wie viel?" | „welches?" |
| Struktur | Dictionary Name → Anzahl | Liste (aus Etappe 4) |

**Achtung, hier ist eine echte Design-Falle:** Es ist verlockend, jetzt *alles* ins Dictionary zu schieben, weil es so ordentlich aussieht. Tu das nicht. Sobald zwei Medkits sich unterscheiden können — eines halb verbraucht, eines abgelaufen —, brauchst du wieder einzelne Dinge. Deine Liste aus Etappe 4 bleibt, und in Etappe 11 wird sie zur Liste von Objekten.

### 11. Die Karte ändert sich zur Laufzeit

```python
gewuerze["safran"]["menge_g"] = 0
```

Eine Zuweisung, und die Daten sind andere. Kein Neuanlegen, kein Kopieren.

Das klingt banal und ist der Grund, warum eine Sektorenkarte etwas anderes ist als ein Text. Ein Sektor, dessen Integrität von 100 auf 60 fällt, ist derselbe Sektor mit einem anderen Wert. In Etappe 13 räumst du damit den Osttunnel frei — **eine Zeile**, wenn du in Entscheidung 1 den markierten Weg gewählt hast.

⚠️ **Und die Kehrseite:** In Etappe 19 wird gespeichert — und dann gilt die Frage:

> **Was sich zur Laufzeit ändert *und nach dem Laden noch so sein soll*, muss in den Spielstand.**

Der zweite Halbsatz ist wichtig. Deine Eingabe ändert sich ständig und gehört nirgendwohin. Der Schaden einer einzelnen Attacke auch nicht. Aber die Integrität eines Sektors schon — sonst ist der Vorposten nach dem Laden wieder heil.

Du musst heute nichts tun. Behalt nur im Hinterkopf, welche deiner Werte zu welcher Sorte gehören.

### 12. Richtung, Ziel und Standort sind drei Dinge ⭐

Der Spieler tippt `gehe osten`. Was danach in deinem Programm passiert, sind drei Schritte — und drei verschiedene Werte:

```
"osten"          ← die Richtung. Was der Spieler getippt hat.
"landeplattform" ← das Ziel. Steht als Wert in nachbarn.
sektoren[...]    ← der Sektor selbst. Das Dictionary dahinter.
```

**`"osten"` ist kein Sektorname.** Das klingt banal, und trotzdem entsteht daraus ein Fehler, den fast jeder einmal baut:

```python
aktueller_sektor = "osten"      # ← die Himmelsrichtung als Standort
```

Danach schlägt `sektoren["osten"]` fehl — und der `KeyError` erscheint an einer ganz anderen Stelle als die Zeile, die ihn verursacht hat.

**Der Reflex dazu:** Wenn du einen Wert weiterreichst, frag dich, *welche der drei Sorten* er ist. Diese Unterscheidung — Adresse, Inhalt, und der Weg dazwischen — begegnet dir in Etappe 14a als Koordinate gegen Feldinhalt wieder und in Etappe 9, wenn ein Objekt seinen eigenen Standort kennt.

### 13. Wenn ein Nachbar ins Leere zeigt

Deine Sektoren verweisen aufeinander: `nordtor` hat einen Nachbarn `kern`, `kern` hat einen Nachbarn `depot`.

**Was passiert, wenn du einen Sektor umbenennst und den Verweis vergisst?**

Der Spieler geht nach Süden. Dein Code schlägt `sektoren["kern"]` nach. `KeyError` — mitten im Spiel, an einer Stelle, die mit dem Umbenennen nichts zu tun hat.

**Das ist eine eigene Fehlerklasse, und sie hat einen Namen:** *inkonsistente Daten*. Der Code ist richtig. Die Daten widersprechen sich. Kein Test der Kauflogik und kein Blick auf die Bewegungslogik findet das je.

**Es gibt davon zwei Sorten, und die eine ist deutlich unangenehmer als die andere.** Welche das ist und woran man es merkt, findest du im Kaputtmach-Teil selbst heraus — Experiment 5. Lies hier nicht weiter nach; der Unterschied ist in zwei Minuten erlebt und in zwei Sätzen nicht zu ersetzen.

**Was du dagegen jetzt schon mitnehmen sollst, ist eine Frage, die du dir heute zum ersten Mal stellen sollst:**

> **Welche Bedingungen müssen bei meinen Sektordaten *immer* stimmen?**

Zum Beispiel: Jeder Sektor hat eine Beschreibung. Jeder hat eine Integrität. Jeder Nachbarname existiert auch wirklich als Sektor. Solche Sätze heißen **Invarianten**, und sie sind der Unterschied zwischen „Python akzeptiert meine Daten" und „meine Daten ergeben Sinn".

**Schreib deine drei bis vier Invarianten in `GELERNT.md` — mehr nicht.** Du baust heute keinen Prüfer dafür. Aber in Etappe 25 kommt Content aus einer Datei, die du nicht selbst getippt hast, und in Etappe 26 schreibst du einen Test, der genau diese Sätze prüft. Dann holst du die Liste wieder hervor.

### 14. Die Darstellung: ein Grundriss mit Markierung

Zehn Minuten, ganz am Schluss.

Ein grober Grundriss deines Vorpostens als fester ASCII-Block — genau wie der Kopf aus Etappe 1, den du längst gebaut hast. Der aktuelle Sektor wird darin markiert, etwa mit eckigen Klammern oder einem Pfeil.

**Und hier ausdrücklich der Riegel:** Der Grundriss ist **handgezeichnet und statisch**. Erzeug ihn nicht aus `sektoren`. Das wäre eine hübsche Übung, sie hat mit Dictionaries nichts zu tun, und sie kostet dich zwei Abende — die Karte müsste dann wissen, wo oben ist.

Was aus den Daten kommt, ist nur die **Markierung**: welcher Sektor gerade dran ist, plus eine Zeile mit den Ausgängen. Mehr nicht.

*(In Etappe 7b wandert der Grundriss in eine Zeichenfunktion. In Etappe 29 wird er zur Kulisse hinter der Grafik. Deine handgezeichnete Version von heute überlebt beides.)*

---

## Dein Auftrag

**Diese Etappe ist groß.** Schritt 1 und Schritt 11 sind die aufwendigsten — bei Schritt 1 entstehen zwei Verschachtelungsebenen auf einmal, bei Schritt 11 vier Prüfungen in der richtigen Reihenfolge. Beide dürfen dich länger beschäftigen als der Rest zusammen.

Nach jedem Schritt ausführen, vorher sagen, was passieren wird.

---

### 1. Bau die Sektorenkarte

- Leg ein verschachteltes Dictionary `sektoren` an, mit sechs Einträgen:

  | Schlüssel | Rolle |
  |---|---|
  | `"nordtor"` | Hier stehst du zu Beginn |
  | `"osttor"` | Zweiter Zugang |
  | `"kern"` | Die Anlage, die du verteidigst |
  | `"depot"` | Hier wird gekauft |
  | `"werkstatt"` | Ab Etappe 13 wird hier gebaut |
  | `"landeplattform"` | Nicht erreichbar |

- Jeder Sektor bekommt drei Eigenschaften: `"beschreibung"` (ein bis zwei eigene Sätze), `"integritaet"` (Zahl, 100 zu Beginn), `"nachbarn"`.
- `"nachbarn"` ist selbst ein Dictionary — **Richtung → Sektorname**, etwa `{"sueden": "kern", "osten": "osttor"}`.
- Verbind die **erreichbaren** Sektoren so, dass man von jedem aus jeden erreichen kann.
- Die Landeplattform behandelst du nach Entscheidung 1 — entweder gar nicht angebunden, oder angebunden und blockiert.

**So prüfst du es:** `sektoren["nordtor"]["nachbarn"]` ausgeben. Es muss ein Dictionary erscheinen, kein Text.

---

### 2. Leg deine Position an

- Eine einzelne Variable `aktueller_sektor`, Startwert `"nordtor"`.
- **Kein** Dictionary-Eintrag — sie beschreibt nicht die Karte, sondern dich.

*(In Etappe 9 wird daraus `marine.sektor`, in Etappe 19 Teil des Spielstands.)*

---

### 3. Bau den Befehl `umsehen`

- Gibt aus: die Beschreibung des aktuellen Sektors, seine Integrität, die möglichen Richtungen.
- Die Richtungen liest du aus `nachbarn` — **schreib sie nicht von Hand hin**, sonst stimmen sie ab Etappe 13 nicht mehr.

**So prüfst du es:** Ändere eine Richtung in deinen Daten, ruf `umsehen` auf. Die Ausgabe muss sich mitändern, ohne dass du die Ausgabe selbst anfasst.

---

### 4. Bau den Befehl `gehe <richtung>`

Drei Fälle, sauber getrennt:

| Fall | Reaktion |
|---|---|
| Richtung existiert | `aktueller_sektor` ändert sich, danach `umsehen` |
| Richtung existiert nicht | Meldung, welche Richtungen es gibt |
| Kein zweites Wort (`gehe` allein) | Meldung, kein Absturz |

Das `.split()` aus Etappe 4 trägt das schon — du erweiterst nur deine Befehlskette.

**So prüfst du es:** Einmal durch alle erreichbaren Sektoren laufen und zurück. Bleibst du irgendwo stecken, sind die `nachbarn` nicht in beide Richtungen eingetragen.

---

### 5. Bau den versiegelten Weg

- Nach Entscheidung 1.
- Ruf am Osttor `umsehen` auf, geh dann Richtung Landeplattform.
- **Der Spieler muss verstehen, warum es nicht geht.** „Unbekannte Richtung" reicht nicht, wenn du die markierte Variante gewählt hast.

---

### 6. Bau das Depot als flaches Dictionary

```
waren: medkit → 40, munition → 15, panzerplatte → 90
```

- Preise in Schrott.
- Befehl `depot`, der alle Waren mit Preisen auflistet — **mit einer Schleife über das Dictionary**, nicht mit drei `print`-Zeilen.
- Trägst du eine vierte Ware ein, muss sie ohne weitere Arbeit in der Liste erscheinen.

**Zum Nachdenken, bevor du weitergehst:** Öffne `inventar` und `waren` nebeneinander. Beides sind Sammlungen von Gegenständen — eine Liste, ein Dictionary. Was wäre unsinnig daran, das Inventar wie `waren` aufzubauen? Ein, zwei Sätze in `GELERNT.md`. Die vollständige Antwort gibt Etappe 6.

---

### 7. Prüf deine Kennungen gegen Etappe 4

- Ruf `depot` auf, dann `inventar`.
- Steht ein Medkit in beiden unter demselben Wort?

Wenn nicht: du hast die Lage aus Konzept 9. Entscheide dich für einen Weg, schreib die Entscheidung in `GELERNT.md`.

⚠️ **Mach das jetzt, nicht in Schritt 11.** Sobald `kaufe` steht, gibt es eine dritte Stelle mit denselben Namen — dann ist die Umstellung dreimal so groß.

---

### 8. Sperr das Depot auf den richtigen Sektor

- `depot` und `kaufe` funktionieren nur, wenn `aktueller_sektor` auf `"depot"` steht.
- Sonst: Meldung, wo das Depot ist.

*(Eine Zeile — und der erste Befehl, der vom Ort abhängt statt nur von Werten.)*

---

### 9. Bau den Vorrat als Dictionary

```
vorrat: schrott → 0, munition → 40
```

- Deine losen Zahlen für Schrott und Munition wandern hinein.
- Pass **alle** Stellen an, die bisher direkt darauf zugegriffen haben — Statusanzeige, Feuern, Aufsammeln.

**So prüfst du es:** Feuern muss weiterhin Munition senken, der Balken aus Etappe 3c muss weiterhin stimmen.

> **⏸ Guter Schnitt.** Nach Schritt 9 steht eine begehbare Karte mit sichtbarem Depot. Commit: `Etappe 5: Sektorenkarte und Depot`. Die Schritte 10 bis 17 sind ein eigener Abend.

---

### 10. Hinterleg, welche Waren stapelbar sind

- Munition ist stapelbar, Medkit und Panzerplatte sind Einzelstücke.
- **Dein Code muss das aus den Daten lesen, nicht aus einer `if`-Kette.**
- Bau dafür ein zweites, flaches Dictionary:

  ```
  stapelbar: medkit → False, munition → True, panzerplatte → False
  ```

⚠️ *Was du nicht tun solltest: die Stapelbarkeit daran ablesen, ob der Name schon im `vorrat` steht. Das sieht aus, als würde es funktionieren, beantwortet aber eine andere Frage — nämlich ob der Spieler die Ressource gerade besitzt.*

**Der Preis dieser Bauweise:** Eine neue Ware braucht ab jetzt zwei Einträge. Vergisst du den zweiten, ist das der inkonsistente Datenfehler aus Konzept 13 — nur diesmal in deinen Warendaten.

---

### 11. Bau `kaufe <ware>`

**Schreib den Ablauf erst auf Papier, dann tippe.** Vier Prüfungen, danach zwei Änderungen:

```
Gibt es die Ware?          →  nein: Meldung, Ende
Reicht der Schrott?        →  nein: Meldung, Ende
Ist Platz im Inventar?     →  nein: Meldung, Ende
                              (nur bei Einzelstücken)
── ab hier wird verändert ──
Schrott abbuchen
Ware einbuchen
```

- **Erst wenn alle vier Prüfungen bestanden sind, wird etwas verändert.**
- Jede Prüfung bekommt eine **eigene** Meldung — „Kauf nicht möglich" sagt dem Spieler nichts.
- **In deiner Kauflogik darf kein Warenname vorkommen.** Kein `if ware == "medkit"`. Preis und Stapelbarkeit werden nachgeschlagen.

*(Der Grund für die Reihenfolge steht in Konzept 8 — derselbe Gedanke wie beim Umzug zwischen zwei Listen in Etappe 4.)*

---

### 12. Frag bei stapelbaren Waren nach der Menge

- *„Wie viele?"* — nur bei Stapelware, ein Einzelstück kauft man einzeln.
- Text rein, `int()` drauf, dann rechnen — der Dreisatz aus Etappe 1.
- Multiplizier den Preis mit der Menge, **bevor** du prüfst, ob der Schrott reicht.

**So prüfst du es:** Tippe `drei` statt `3` — es stürzt ab, das ist heute in Ordnung. Notier den Fehlernamen. Tippe dann `0` und `-5`. Was passiert?

---

### 13. ⭐ Der Architekturtest — nur Daten anfassen

Vier Änderungen, **keine einzige Zeile Logik darf dabei angefasst werden:**

| Änderung | Was passieren muss |
|---|---|
| Ware hinzufügen — `"reparaturkit"`, Preis 60, mit allen nötigen Daten | Erscheint im Depot, ist kaufbar |
| Ware löschen — nimm `"panzerplatte"` heraus | Verschwindet aus dem Depot, `kaufe panzerplatte` meldet sauber |
| Preis ändern — Medkit auf 25 | Depot zeigt 25, Kauf bucht 25 ab |
| Ausgang entfernen — lösch eine Richtung | `umsehen` zeigt sie nicht mehr |

Danach alles zurücksetzen.

*(Das Löschen ist die schärfere Hälfte — dabei fällt jeder fest verdrahtete Warenname auf.)*

---

### 14. Verknüpf Schrott mit dem Kampf

- Gefallene Gegner hinterlassen Schrott.
- Aus Etappe 4: Das Aufsammeln erhöht jetzt den `vorrat`.

Damit läuft zum ersten Mal ein Kreislauf: Gegner fallen → Schrott → Munition → Gegner fallen.

---

### 15. Der Rückwärtsgang

Spiel drei volle Wellen. Prüf der Reihe nach: Feuern, Nachladen, Status, Balken, Wellenende, Gegner auf der Bahn.

*(Der `vorrat`-Umbau aus Schritt 9 hat viele Stellen angefasst.)*

---

### 16. Der Grundriss

- Zeichne einen groben ASCII-Grundriss von Hand, wie den Kopf aus Etappe 1.
- Markier darin den aktuellen Sektor.
- Der Grundriss selbst ist statisch — **nur die Markierung kommt aus `aktueller_sektor`.**

**Zehn Minuten, Wecker stellen.** Wenn man sechs Räume erkennt, ist der Schritt erledigt.

---

### 17. Committen

```
git add .
git commit -m "Etappe 5: Vorposten, Depot und Wirtschaft"
git push
```

---

## Was NICHT in diese Etappe gehört

- ❌ **Funktionen, damit `kaufe` nicht so lang wird** → Etappe 7a
- ❌ **Gegenstände als Objekte mit Eigenschaften** → Etappe 11
- ❌ **`try` / `except` für die Mengeneingabe** → Etappe 20
- ❌ **Waren mit Voraussetzungen und Ausbaustufen** → Etappe 22
- ❌ **Die Karte aus einer JSON-Datei laden** → Etappe 25
- ❌ **Gegner, die in einzelnen Sektoren stehen** → Etappe 14a
- ❌ **Sektoren, die einzeln fallen können** → Etappe 17b
- ❌ **Den Grundriss aus den Daten erzeugen** → gar nicht, siehe Konzept 14
- ❌ **Verkaufen** → wenn du willst, aber es bringt heute nichts Neues
- ❌ **Balancing** (Preise, Schrott pro Gegner) → notieren, Etappe 21a

**Der verlockendste Punkt ist der erste, und du wirst ihn heute spüren.**

Deine Kauflogik hat drei Prüfungen, zwei Meldungen pro Prüfung und danach die Buchung. Das sind schnell fünfundzwanzig Zeilen mitten in deiner Befehlskette, und die Befehlskette hatte schon vorher sechs Zweige. Irgendwann heute denkst du: *das gehört ausgelagert.*

**Der Gedanke ist völlig richtig, und genau deshalb kommt Etappe 7a.** Dort räumst du auf — und der Grund, warum du dort verstehst, wozu Funktionen gut sind, ist der Zustand, in dem deine Datei heute Abend ist. Wer aufräumt, bevor es unordentlich war, lernt eine Syntax. Wer es aushält, lernt ein Werkzeug.

**Notier den Moment.** Eine Zeile in `GELERNT.md`, wann dir zum ersten Mal aufgefallen ist, dass die Datei zu lang wird. In Etappe 7a liest du sie wieder.

---

## Selbsttest

Prüft den Zustand deines Programms, nicht dein Gefühl. Führ jeden Punkt tatsächlich aus.

- [ ] `umsehen` zeigt Beschreibung, Integrität und die Ausgänge des aktuellen Sektors
- [ ] Änderst du eine Richtung in `sektoren`, ändert sich die Ausgabe von `umsehen` mit — ohne dass du die Ausgabe angefasst hast
- [ ] Du kannst alle erreichbaren Sektoren ablaufen und zurückkommen
- [ ] `gehe norden` an einer Stelle ohne Norden meldet, welche Richtungen es gibt
- [ ] `gehe` ohne zweites Wort stürzt nicht ab
- [ ] Die Landeplattform ist nicht erreichbar, und der Spieler erfährt, warum
- [ ] *(Bei Variante „markiert")* Eine blockierte Richtung meldet etwas anderes als eine Richtung, die es gar nicht gibt
- [ ] `depot` außerhalb des Depots meldet, wo das Depot ist
- [ ] ⭐ **Ware hinzufügen:** `"reparaturkit"` mit allen Daten eintragen, **keine Zeile Logik anfassen** — sie erscheint im Depot, ist kaufbar und landet an der richtigen Stelle
- [ ] ⭐ **Ware löschen:** `"panzerplatte"` aus den Daten entfernen — sie verschwindet aus dem Depot, `kaufe panzerplatte` meldet sauber, nichts stürzt ab
- [ ] Preis einer Ware ändern — Depot **und** Abbuchung zeigen den neuen Wert
- [ ] Einen Ausgang aus einem Sektor löschen — `umsehen` zeigt ihn nicht mehr, `gehe` dorthin meldet die vorhandenen Richtungen
- [ ] Kaufen mit zu wenig Schrott sagt, dass der Schrott nicht reicht — und der Schrott wird **nicht** abgebucht
- [ ] Kaufen bei vollem Inventar sagt das — und der Schrott wird **nicht** abgebucht
- [ ] `kaufe hubschrauber` meldet, dass es die Ware nicht gibt
- [ ] Gekaufte Munition erhöht den Vorrat, ein gekauftes Medkit landet im Inventar
- [ ] ⭐ **Schrott steht nur an einer Stelle** — im `vorrat`, nicht mehr in der `inventar`-Liste. Sammel welchen auf und prüf beide
- [ ] Feuern senkt weiterhin die Munition, der Balken aus Etappe 3c stimmt weiterhin
- [ ] **Drei volle Wellen** lassen sich spielen — inklusive mindestens eines Kaufs und eines aufgesammelten Schrotts — ohne dass etwas abstürzt
- [ ] Im Grundriss ist der aktuelle Sektor markiert und wandert beim Gehen mit

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten. Dein Mentor fragt sie ab.

1. Was ist der Unterschied zwischen einer Liste und einem Dictionary — **nicht** in der Schreibweise, sondern in der Frage, die man stellt?
2. Wie kommst du an einen verschachtelten Wert, und was liefert der erste Schlüssel dabei zurück?
3. Was passiert bei einem Schlüssel, den es nicht gibt? Was macht `.get()` anders, und wann willst du welches von beiden?
4. **Was prüft `"medkit" in waren` — den Schlüssel oder den Wert?** Und wie fragst du nach dem anderen?
5. Der Spieler tippt `gehe osten`. Welche drei verschiedenen Werte entstehen dabei — und warum ist `"osten"` keiner davon, den du in `aktueller_sektor` schreiben darfst?
6. Was bekommst du, wenn du direkt über ein Dictionary iterierst? Und was liefert `.items()`?
7. Warum ist `sektoren` verschachtelt und `waren` flach? Nenn die Frage, mit der du das entscheidest.
8. Warum kann eine Liste kein Dictionary-Schlüssel sein? *(Ein Satz genügt — 👀.)*
9. **Warum kommt in deiner Kauflogik kein einziger Warenname vor — und was wäre der Preis dafür, wenn doch?**
10. Warum ist Schrott jetzt ein Dictionary-Eintrag und ein Medkit weiterhin ein Listeneintrag?
11. Was wird in deinem Programm verglichen und was angezeigt — und warum sollten das nicht dieselben Wörter sein?
12. Was ist ein *inkonsistenter Datenfehler*, und warum findet ihn kein Blick in die Bewegungslogik?
13. Welche deiner Werte ändern sich zur Laufzeit **und sollen nach dem Laden noch so sein**? *(Die Frage kommt in Etappe 19 wieder.)*
14. Nenn drei Bedingungen, die bei deinen Sektordaten immer stimmen müssen. *(Deine Invarianten aus Konzept 13.)*

**Frage 9 ist die wichtigste.** Die anderen sind Werkzeugwissen, und Werkzeugwissen holt man nach. Frage 8 ist der Übergang von *„ich schreibe Code, der Werte kennt"* zu *„ich schreibe Code, der Werte nachschlägt"* — und das ist der Gedanke, aus dem Etappe 22 und Etappe 25 vollständig bestehen. Wer ihn heute an drei Waren begriffen hat, versteht dort in zehn Minuten, warum dreißig Gegnertypen in eine Textdatei gehören.

---

## Transferaufgabe (15 Minuten)

**Außerhalb des Spiels**, in einer Wegwerf-Datei. Ein Gewürzregal, kein Depot.

1. Bau ein flaches Dictionary: drei Gewürze mit ihrem Preis.
2. Frag per `input()` nach einem Namen und gib den Preis aus. Reagier sauber, wenn es das Gewürz nicht gibt — **einmal mit eckigen Klammern, einmal mit `.get()`.** Schreib in einem Satz auf, welche der beiden Varianten du im Spiel benutzen würdest und warum.
3. Bau dasselbe Regal verschachtelt: jedes Gewürz mit Preis, Menge und Regalnummer.
4. Gib alle Gewürze aus, die weniger als 50 Gramm haben — mit `.items()`.
5. **Und jetzt der eigentliche Punkt:** Füge ein viertes Gewürz hinzu und führ Schritt 4 erneut aus, ohne die Schleife anzufassen.

Wenn Schritt 5 ohne jede Änderung funktioniert, hast du Konzept 8 verstanden. Wenn nicht, steht in deiner Schleife irgendwo ein Gewürzname — und genau der wäre in deinem Depot ein Warenname.

---

## Kaputtmachen

**Vor jedem Experiment aufschreiben, was passieren wird.** Die ersten fünf gehören dazu, die letzten vier sind Kür.

**1. Greif auf einen Schlüssel zu, den es nicht gibt.** Lies die Fehlermeldung ganz. Was genau steht in den Anführungszeichen?

**2. Der Tippfehler beim Zuweisen — und warum er zweimal etwas anderes tut.**

Probier beides und vergleich:

```python
waren["repraturkit"] = 60                   # ← Tippfehler
sektoren["nordtorr"]["integritaet"] = 50    # ← Tippfehler
```

Das erste läuft **still durch** und legt einen Eintrag an, den nie jemand liest. Das zweite **knallt sofort** mit `KeyError`.

**Warum der Unterschied?** Beim ersten legst du einen Schlüssel *an* — das ist erlaubt, dafür gibt es keine Rechtschreibprüfung. Beim zweiten musst du erst einen Schlüssel *lesen*, um an das innere Dictionary zu kommen, und den gibt es nicht.

**Die Regel dahinter ist wichtiger als das Beispiel:** Ein Tippfehler links vom `=` ist gefährlich. Ein Tippfehler beim Lesen ist harmlos, weil er abstürzt. Ruf danach `waren` auf und sieh dir an, was da jetzt drinsteht.

**3. Schreib beim Kaufen `vorrat["schrott"] - preis` statt `-= preis`.** Kauf dreimal hintereinander dasselbe.

⭐ **Das ist der Typ-3-Fehler dieser Etappe:** keine Fehlermeldung, kein Absturz — nur ein Spieler, der unendlich viel Geld hat. Der Ausdruck wird berechnet und weggeworfen.

**4. Buch den Schrott ab, bevor du prüfst, ob Platz im Inventar ist.** Kauf bei vollem Inventar. Wo ist der Schrott hin? Das ist die Gegenprobe zu Auftragsschritt 11.

**5. Zwei Sorten kaputter Karte — und sie fühlen sich verschieden an.**

Erst: Lösch eine Richtung aus einem Sektor und geh dorthin. Dann: Lass die Richtung stehen, aber **verschreib dich im Zielnamen** (`"sueden": "ker"`) und geh dorthin.

**Beantworte danach drei Fragen, bevor du weiterliest:**

1. Bei welchem der beiden greift deine eigene Prüfung — und bei welchem nicht?
2. Bei welchem stürzt das Programm ab, **obwohl** die Prüfung durchgelaufen ist?
3. Warum ist der zweite Fall der gemeinere, wenn du ihn in vier Wochen suchen musst?

Das ist der inkonsistente Datenfehler aus Konzept 13, und du hast ihn dir gerade selbst gebaut. Die Antworten in `GELERNT.md`.

---

Die folgenden vier sind Kür. Wenn dir die Zeit fehlt, nimm mindestens Nummer 6.

**6. ⭐ Der Umbenennungstest.** Benenne `"werkstatt"` in `"schmiede"` um — nur den Schlüssel, sonst nichts. Führ das Spiel aus und such alle Stellen, die dadurch kaputtgehen.

Es werden mehr sein, als du denkst: Nachbarn anderer Sektoren, vielleicht dein Grundriss, vielleicht eine Ortsprüfung. **Und Python hat dich bei keiner einzigen davon gewarnt.**

Das ist der Satz, um den es geht: **Daten sind nicht konsistent, nur weil Python sie akzeptiert.** Danach zurückbenennen.

**7. Mach aus `nachbarn` eine Liste** statt eines Dictionaries: `["kern", "osttor"]`. Versuch, `gehe sueden` zu bauen. Woran genau scheitert es — und was sagt dir das darüber, was ein Dictionary eigentlich leistet?

**8. Lösch einen Eintrag, während du über das Dictionary läufst.** Vergleich die Fehlermeldung mit dem, was dieselbe Sache bei einer Liste in Etappe 4 gemacht hat. **Welches Verhalten ist dir lieber, und warum?**

**9. Versuch, eine Liste als Schlüssel zu benutzen.** Lies die Fehlermeldung. Das Wort `unhashable` musst du heute nicht verstehen — merk dir nur, dass es mit *veränderlich* zu tun hat.

---

**Experiment 3 ist das wichtigste**, Experiment 6 das lehrreichste und Experiment 8 das überraschendste: Beim Dictionary bricht Python ab. Bei einer Liste kann das Programm weiterlaufen und trotzdem ein falsches Ergebnis liefern — es überspringt Einträge, wie du in Etappe 4 gesehen hast.

Dass eine Sprache manchmal streng ist, damit man nicht in Ruhe Unsinn machen kann, ist ein Gedanke, der dir bis Etappe 26 begegnet.

Alle Typ-3-Fehler in `GELERNT.md`, mit einem Satz dazu: **woran du sie erkannt hättest.**

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `KeyError: 'kern'` | Schlüssel existiert nicht — Tippfehler oder Verweis ins Leere | Die Stelle, an der der Schlüssel *entsteht*, nicht die, an der er gelesen wird |
| `TypeError: string indices must be integers` | Du greifst mit einem Namen auf einen String zu | Eine Verschachtelungsebene zu tief — was liefert der erste Schlüssel wirklich? |
| `TypeError: unhashable type: 'list'` | Eine Liste als Schlüssel benutzt | Konzept 7 |
| `RuntimeError: dictionary changed size during iteration` | Eintrag gelöscht, während die Schleife lief | Erst sammeln, dann löschen — wie in Etappe 4 |
| Kein Fehler, aber der Wert ist nicht angekommen | Tippfehler im Schlüssel beim **Zuweisen** — es entstand ein neuer Eintrag | `print(sektoren.keys())` und nachsehen, was wirklich drinsteht |
| Kein Fehler, aber Schrott wird nie weniger | `x - y` statt `x -= y` | Die Zeile mit der Abbuchung |
| Schrott ist weg, Ware nicht da | Abgebucht, bevor alle Prüfungen durch waren | Konzept 10 aus Etappe 4 |
| `gehe` funktioniert in eine Richtung, aber nicht zurück | Nachbar nur einseitig eingetragen | Beide Sektoren prüfen |
| `KeyError` beim Gehen, **obwohl** die Richtung geprüft wurde | Der Zielname existiert nicht — inkonsistente Daten | Nicht die Prüfung, sondern den **Wert** hinter der Richtung |
| `KeyError: 'osten'` nach dem Gehen | Die Himmelsrichtung wurde als Standort gespeichert | Konzept 12 — Richtung ist nicht Ziel |
| Neue Ware erscheint nicht im Depot | Die Anzeige ist von Hand geschrieben statt aus den Daten | Auftragsschritt 6 |
| `in` findet die Ware nicht, obwohl sie da ist | Du suchst nach dem Wert statt nach dem Schlüssel | Konzept 4 |

**Der Debugging-Reflex dieser Etappe: „Was steht wirklich drin — und unter welchem Namen?"**

In Etappe 4 war es *was steht da gerade wirklich drin?*. Bei Dictionaries kommt die zweite Hälfte dazu, denn ein falscher Schlüssel ist unsichtbar:

```python
print("### KEYS", sektoren.keys())
print("### WERT", sektoren.get(aktueller_sektor))
```

`.keys()` ist hier ausdrücklich nützlich, obwohl du es sonst selten brauchst: Es zeigt dir auf einen Blick, ob dein Schlüssel `"nordtor"`, `"Nordtor"` oder `"nordtorr"` heißt. Und `.get()` statt eckiger Klammern, damit die Debugzeile nicht selbst abstürzt.

**Nachsehen schlägt Vermuten** — der Grundsatz gilt seit Etappe 1, das Werkzeug wächst mit. In Etappe 8 löst der Debugger diese Zeilen ab.

---

## Ein Blick nach vorne

**Etappe 6** stellt Liste, Dictionary, Set und Tuple nebeneinander. Damit du dort nicht bei „Liste = mehrere Dinge, Dictionary = mehrere Daten" landest, hier dein Zwischenstand — **drei Fragen, drei Antworten**, alle schon gebaut:

| Frage an die Daten | Antwort |
|---|---|
| *Welche Dinge habe ich?* | **Liste** (`inventar`) |
| *Was gehört zu diesem Namen?* | **Dictionary** (`sektoren`, `waren`) |
| *Wie viel habe ich?* | **Zahl** — oder ein Dictionary aus Namen und Anzahlen (`vorrat`) |

**Etappe 6 ergänzt die drei fehlenden Fragen:**

> *Ist es schon enthalten?* · *Darf es doppelt vorkommen?* · *Ist die Reihenfolge Teil der Bedeutung?*

Und dann wirst du rückblickend sehen, dass du heute an ein bis zwei Stellen ein Dictionary benutzt hast, wo etwas anderes besser gepasst hätte.

**Etappe 7a** räumt deine Befehlskette auf. Der Kaufvorgang wird zur ersten Funktion, die wirklich etwas leistet — und du wirst merken, dass er nur deshalb so leicht auszulagern ist, weil er heute schon keine Warennamen kennt.

**Etappe 9** macht aus `aktueller_sektor` ein Attribut deines Marine. Aus einer losen Variablen wird `marine.sektor`.

**Etappe 13** räumt den Osttunnel frei. Ob das eine Zeile ist oder ein Umbau, entscheidet deine heutige Entscheidung 1.

**Etappe 14a** legt ein Raster neben deine Karte — und dann hast du beide Strukturen im selben Programm und kannst vergleichen, wofür jede taugt. Wenige benannte Orte mit Eigenschaften gegen viele gleichartige Zellen, auf denen gerechnet wird.

**Etappe 19** speichert deinen Spielstand. Dann wird die Frage aus Konzept 11 fällig: Was hat sich zur Laufzeit geändert und muss mit? Deine Sektorintegrität ja, deine Beschreibungen nein.

**Etappe 22** macht aus den Warendaten Baupläne mit Kosten, Bauzeit und Voraussetzungen. Deine flache Preistabelle bekommt Ebenen — und deine Entscheidung 2 von heute entscheidet, wie viel Arbeit das ist.

**Etappe 25** ist der große Zahltag: Die Sektorenkarte und die Warentabelle wandern in JSON-Dateien, ohne dass sich am Code etwas ändert. Dass das überhaupt möglich ist, liegt daran, dass du heute Daten von Logik getrennt hast.

---

## Abschluss

**⭐ Und einmal, weil es sich lohnt: Schreib eine Zustandsübersicht.**

Dein Spiel hat inzwischen viele Werte, die verstreut ganz oben in der Datei stehen. Sortier sie einmal auf einem Blatt — nicht im Code, nur als Liste:

```
SPIELER      Name, Klasse, Trefferpunkte, Schaden, Panzerung
RESSOURCEN   vorrat (Schrott, Munition)
BESITZ       inventar
VORPOSTEN    kern_integritaet, sektoren
POSITION     aktueller_sektor
WELLE        welle, runde, gegner
```

**Das ist keine neue Technik, sondern eine Bestandsaufnahme** — und der Moment, in dem die meisten zum ersten Mal denken: *Mein Spiel hat einen Zustand.*

Du brauchst diese Liste vier Mal wieder: in **Etappe 7a**, wenn Funktionen Zustand übergeben bekommen; in **Etappe 9**, wenn ein Teil davon in den Marine wandert; in **Etappe 12**, wenn ein anderer Teil zur Welt gehört; und in **Etappe 19**, wenn du entscheiden musst, was gespeichert wird. Heb sie auf.

**In `GELERNT.md`:**

- Was habe ich gebaut?
- Was habe ich verstanden?
- Was hat mich überrascht? *(Kandidaten: `in` prüft Schlüssel · der Tippfehler, der einen neuen Eintrag anlegt · `x - y` statt `x -= y`)*
- Welchen Fehler habe ich gemacht — und **wie habe ich ihn gefunden?**
- **Entscheidung 1:** Fehlt der versiegelte Weg oder ist er markiert — und warum?
- **Entscheidung 2:** Hat das Depot einen Bestand — und warum (nicht)?
- **Wie unterscheidet mein Code stapelbare Waren von Einzelstücken?**
- **Meine drei bis vier Invarianten:** Was muss bei den Sektordaten immer stimmen?
- Was beim Umbenennungstest kaputtging — und wie viele Stellen es waren
- Warum `inventar` eine Liste ist und `vorrat` ein Dictionary
- Die Zeile aus dem „Was NICHT"-Abschnitt: **wann ist mir zuerst aufgefallen, dass die Datei zu lang wird?**

---

## Wenn du mehr willst

Erst bei grünem Selbsttest. Alles hier ist freiwillig.

**Sektoren nehmen Schaden.** Die Gegner greifen nicht die Anlage allgemein an, sondern den Sektor, in dem du gerade nicht bist. `sektoren[...]["integritaet"]` sinkt. Das ist eine Zeile und macht aus deiner Karte zum ersten Mal eine taktische Entscheidung: Wo stehst du, wenn du nicht überall sein kannst? *(In Etappe 17b kann ein Sektor dadurch endgültig fallen.)*

**Reparieren.** `repariere` kostet Schrott und hebt die Integrität des aktuellen Sektors. Nutzt alles, was du heute gebaut hast, und schließt den Wirtschaftskreislauf.

**Eine Ware, die es nicht immer gibt.** Ein Eintrag, der erst ab Welle 5 im Depot auftaucht. Zwei Zeilen, und deine Warentabelle bekommt zum ersten Mal eine Eigenschaft, die *keine Zahl* ist — die Vorstufe zu den Voraussetzungen aus Etappe 22.

**Der Grundriss zeigt Schäden.** Ein Sektor unter 50 Prozent wird anders dargestellt. Kostet nichts und macht den Grundriss von Kulisse zu Information.

**Die Werkstatt hat eine Werkbank, an der nichts geht.** `untersuche werkbank` gibt eine Zeile aus: halb fertige Halterungen, ein Werkzeug, das jemand liegen gelassen hat, als es schnell gehen musste. Kein Befehl greift darauf zu.

Das ist der beste Zusatz dieser Etappe, und aus demselben Grund wie der Datenkern in Etappe 4: Es ist ein Versprechen, das du erst in Etappe 13 einlöst, wenn dort gebaut wird. Ein Ort, der nach etwas aussieht, was noch nicht geht, zieht mehr als jede Ankündigung.

---

> **Nächste Etappe:** [Etappe 6 — Liste, Dictionary, Set, Tuple](etappe-06-datenstrukturen.md) · Sets, Tuples, Mengenoperationen
