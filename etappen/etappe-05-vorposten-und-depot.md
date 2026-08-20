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
| Reihenfolge | trägt Bedeutung | trägt keine |

Eine Liste ist eine Reihe. Ein Dictionary ist ein Nachschlagewerk. Und Nachschlagewerke schlägt man nicht der Reihe nach auf.

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

⚠️ **Und dieselbe Falle wie bei Listen:** Ein Dictionary nicht verändern, während man darüber läuft. Bei einem Dictionary ist Python sogar strenger als bei einer Liste — es stürzt mit `RuntimeError: dictionary changed size during iteration` ab, statt still das Falsche zu tun. Das ist ein Geschenk.

### 7. Schlüssel müssen unveränderlich sein 👀

```python
d = {["a", "b"]: 1}      # TypeError: unhashable type: 'list'
```

Eine Liste kann kein Schlüssel sein. Ein String, eine Zahl oder ein Tuple schon.

**Der Grund in einem Satz:** Python merkt sich, *wo* ein Schlüssel abgelegt wurde — und das kann es nur, wenn der Schlüssel sich danach nicht mehr ändert. Das hängt direkt an *mutable* und *immutable* aus Etappe 4.

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

> **Eine neue Ware ist dann eine Zeile in den Daten und keine Zeile im Code.**

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

Zwölf Eier sind ein Eintrag, nicht zwölf. Und der entscheidende Vorteil ist derselbe wie in Konzept 8: Der Code, der etwas hinzufügt, muss nicht wissen, **was** er hinzufügt.

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

⚠️ **Und die Kehrseite:** Was sich zur Laufzeit ändert, muss in Etappe 19 gespeichert werden. Was sich nie ändert, nicht. Behalt beim Bauen im Hinterkopf, welche deiner Werte zur ersten und welche zur zweiten Sorte gehören — du musst heute nichts tun, aber in Etappe 19 wirst du gefragt.

### 12. Wenn ein Nachbar ins Leere zeigt

Deine Sektoren verweisen aufeinander: `nordtor` hat einen Nachbarn `kern`, `kern` hat einen Nachbarn `depot`.

**Was passiert, wenn du einen Sektor umbenennst und den Verweis vergisst?**

Der Spieler geht nach Süden. Dein Code schlägt `sektoren["kern"]` nach. `KeyError` — mitten im Spiel, an einer Stelle, die mit dem Umbenennen nichts zu tun hat.

**Das ist eine eigene Fehlerklasse, und sie hat einen Namen:** *inkonsistente Daten*. Der Code ist richtig. Die Daten widersprechen sich. Kein Test der Kauflogik und kein Blick auf die Bewegungslogik findet das je.

Heute reicht es, sie einmal erzeugt zu haben — im Kaputtmach-Teil tust du das absichtlich. In Etappe 25 wird daraus ein eigenes Thema, weil Content aus einer Datei genau diese Fehler produziert, und in Etappe 26 schreibst du einen Test, der die Karte auf sich selbst prüft.

### 13. Die Darstellung: ein Grundriss mit Markierung

Zehn Minuten, ganz am Schluss.

Ein grober Grundriss deines Vorpostens als fester ASCII-Block — genau wie der Kopf aus Etappe 1, den du längst gebaut hast. Der aktuelle Sektor wird darin markiert, etwa mit eckigen Klammern oder einem Pfeil.

**Und hier ausdrücklich der Riegel:** Der Grundriss ist **handgezeichnet und statisch**. Erzeug ihn nicht aus `sektoren`. Das wäre eine hübsche Übung, sie hat mit Dictionaries nichts zu tun, und sie kostet dich zwei Abende — die Karte müsste dann wissen, wo oben ist.

Was aus den Daten kommt, ist nur die **Markierung**: welcher Sektor gerade dran ist, plus eine Zeile mit den Ausgängen. Mehr nicht.

*(In Etappe 7b wandert der Grundriss in eine Zeichenfunktion. In Etappe 29 wird er zur Kulisse hinter der Grafik. Deine handgezeichnete Version von heute überlebt beides.)*

---

## Dein Auftrag

Nach jedem Schritt ausführen — und vorher sagen, was passieren wird. Das Ritual aus Etappe 3 gilt weiter.

**1. Bau die Sektorenkarte.**

Leg ein verschachteltes Dictionary namens `sektoren` an. Sechs Sektoren:

| Schlüssel | Rolle |
|---|---|
| `"nordtor"` | Hier stehst du zu Beginn |
| `"osttor"` | Zweiter Zugang |
| `"kern"` | Die Anlage, die du verteidigst |
| `"depot"` | Hier wird gekauft |
| `"werkstatt"` | Ab Etappe 13 wird hier gebaut |
| `"landeplattform"` | Nicht erreichbar |

Jeder Sektor bekommt drei Eigenschaften: `"beschreibung"` (ein bis zwei Sätze in deinen Worten), `"integritaet"` (eine Zahl, 100 zu Beginn) und `"nachbarn"`.

`"nachbarn"` ist selbst ein Dictionary: **Richtung → Sektorname**, etwa `{"sueden": "kern", "osten": "osttor"}`. Damit hast du zwei Verschachtelungsebenen — sieh dir an, wie sich das im Editor liest, und rück ordentlich ein.

Verbind die Sektoren so, dass man von jedem aus jeden erreichen kann. **Außer der Landeplattform** — die bleibt abgeschnitten, nach deiner Entscheidung 1.

**Zum Prüfen:** Gib `sektoren["nordtor"]["nachbarn"]` aus. Es muss ein Dictionary erscheinen, kein Text.

**2. Leg `aktueller_sektor` an** und setz ihn auf `"nordtor"`. Eine einzelne Variable, kein Dictionary-Eintrag — sie beschreibt nicht die Karte, sondern *dich*.

*(In Etappe 9 wird daraus `marine.sektor`, in Etappe 19 Teil des Spielstands.)*

**3. Bau den Befehl `umsehen`.**

Er gibt die Beschreibung des aktuellen Sektors aus, seine Integrität, und eine Zeile mit den möglichen Richtungen. Die Richtungen liest du aus `nachbarn` — schreib sie **nicht** von Hand hin, sonst stimmen sie ab Etappe 13 nicht mehr.

**Zum Prüfen:** Ändere eine Richtung in deinen Daten und ruf `umsehen` auf. Die Ausgabe muss sich mitändern, ohne dass du die Ausgabe angefasst hast.

**4. Bau den Befehl `gehe <richtung>`.**

Er soll drei Fälle sauber behandeln:

| Fall | Reaktion |
|---|---|
| Die Richtung existiert | `aktueller_sektor` ändert sich, danach `umsehen` |
| Die Richtung existiert nicht | Meldung, welche Richtungen es gibt |
| Kein zweites Wort (`gehe` allein) | Meldung, kein Absturz |

Das `.split()` aus Etappe 4 trägt das schon — du erweiterst nur deine Befehlskette.

**Zum Prüfen:** Lauf einmal durch alle sechs Sektoren und wieder zurück. Wenn du irgendwo steckenbleibst, sind deine `nachbarn` nicht in beide Richtungen eingetragen.

**5. Bau den versiegelten Weg** nach deiner Entscheidung 1. Ruf am Osttor `umsehen` auf und geh dann Richtung Landeplattform. Der Spieler muss verstehen, *warum* es nicht geht — „unbekannte Richtung" reicht nicht, wenn du den markierten Weg gewählt hast.

**6. Bau das Depot als flaches Dictionary.**

```
waren: medkit → 40, munition → 15, panzerplatte → 90
```

Preise in Schrott. Bau den Befehl `depot`, der alle Waren mit Preisen auflistet — mit einer Schleife über das Dictionary, nicht mit drei `print`-Zeilen. **Wenn du eine vierte Ware einträgst, muss sie ohne weitere Arbeit in der Liste erscheinen.**

**7. Prüf deine Kennungen gegen Etappe 4.** Ruf `depot` auf, dann `inventar`. Vergleich die Schreibweisen: Steht ein Medkit in beiden Listen unter demselben Wort?

Wenn nicht, hast du die Lage aus Konzept 9 — entscheide dich für einen Weg und schreib die Entscheidung in `GELERNT.md`.

**Mach das jetzt und nicht in Schritt 10.** Sobald `kaufe` gebaut ist, gibt es eine dritte Stelle mit denselben Namen, und dann ist die Umstellung dreimal so groß.

**8. Sperr das Depot auf den richtigen Sektor.** `depot` und `kaufe` sollen nur funktionieren, wenn `aktueller_sektor` auf `"depot"` steht. Sonst: eine Meldung, wo das Depot ist.

Das ist eine Zeile und der erste Fall, in dem ein Befehl vom **Ort** abhängt statt nur von Werten.

**9. Bau den Vorrat als Dictionary.**

Deine losen Zahlen für Schrott und Munition wandern in ein Dictionary `vorrat`, Name → Anzahl:

```
vorrat: schrott → 0, munition → 40
```

Pass alle Stellen an, die bisher `schrott` oder `ammo` direkt benutzt haben — Statusanzeige, Feuern, Aufsammeln.

**Warum der Umbau sich lohnt:** Danach kann eine Funktion Vorrat erhöhen, ohne zu wissen, *was* sie erhöht. Genau das brauchst du in Schritt 10.

**Zum Prüfen:** Feuern muss weiterhin Munition senken, und der Balken aus Etappe 3c muss weiterhin stimmen.

> **⏸ Hier ist der Schnitt.** Nach Schritt 9 hast du eine begehbare Karte und ein sichtbares Depot. Das ist ein guter Abend und ein eigener Commit (`Etappe 5: Sektorenkarte und Depot`). Die Schritte 10 bis 16 sind der zweite.

**10. Bau `kaufe <ware>`.**

Drei Bedingungen, alle drei mit eigener Meldung:

1. Gibt es die Ware überhaupt? *(Hier gehört `.get()` oder `in` hin — der Spieler tippt, also ist Fehlen der Normalfall.)*
2. Reicht der Schrott?
3. Ist Platz im Inventar? *(Die Obergrenze von zehn aus Etappe 4 gilt weiter — aber nur für Einzelstücke.)*

Erst wenn alle drei stimmen, wird abgebucht und eingebucht. **Denk an Konzept 10 aus Etappe 4: erst prüfen, dann anfassen.** Sonst zahlt der Spieler für ein volles Inventar.

**Und die eigentliche Anforderung:** In deiner Kauflogik darf **kein Warenname vorkommen**. Kein `if ware == "medkit"`. Der Preis wird nachgeschlagen.

**Zum Prüfen — das ist der Selbsttest dieser Etappe:** Trag eine vierte Ware in `waren` ein, zum Beispiel `"reparaturkit"` für 60. Sie muss kaufbar sein, ohne dass du eine einzige Zeile Logik anfasst. Wenn das nicht klappt, steckt irgendwo noch ein Warenname im Code.

**11. Entscheide, wohin die Ware wandert.**

Stapelbares (Munition) erhöht den `vorrat`. Einzelstücke (Medkit, Panzerplatte) kommen in die `inventar`-Liste aus Etappe 4.

Woran dein Code das unterscheidet, ist deine Entscheidung. Ein zusätzlicher Eintrag in den Warendaten wäre ein Weg — dann bleibt die Kauflogik weiterhin ohne Warennamen. Schreib in `GELERNT.md`, wie du es gelöst hast.

**12. Frag beim Kauf nach der Menge.**

Bei stapelbaren Waren fragst du nach: *„Wie viele?"*. Die Antwort kommt als Text aus `input()` — **hier fällt die Schuld aus Etappe 1 an.** Der Dreisatz: Text rein, `int()` drauf, dann rechnen.

Multiplizier den Preis mit der Menge, bevor du prüfst, ob der Schrott reicht.

**Zum Prüfen:** Tippe `drei` statt `3`. Es stürzt ab — das ist heute in Ordnung und wird in Etappe 20 abgefangen. Notier den Fehlernamen in `GELERNT.md`.

**13. Verknüpf Schrott mit dem Kampf.** Gefallene Gegner hinterlassen Schrott. Wenn du in Etappe 4 eine Beuteliste gebaut hast, erhöht das Aufsammeln jetzt den `vorrat`.

Damit läuft zum ersten Mal ein Kreislauf: Gegner fallen → Schrott → Munition → Gegner fallen.

**14. Der Rückwärtsgang.** Spiel drei volle Wellen. Feuern, nachladen, Status, Balken, Wellenende, Gegner auf der Bahn — funktioniert alles noch genau wie nach Etappe 4? Der `vorrat`-Umbau aus Schritt 9 hat viele Stellen angefasst.

**15. Der Grundriss — zehn Minuten, Wecker stellen.**

Zeichne einen groben ASCII-Grundriss von Hand, wie den Kopf aus Etappe 1. Markier darin den aktuellen Sektor. Der Grundriss ist statisch; **nur die Markierung kommt aus `aktueller_sektor`.**

Wenn du nach zehn Minuten etwas hast, in dem man sechs Räume erkennt, ist der Schritt erledigt.

**16. Committen.**

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
- ❌ **Den Grundriss aus den Daten erzeugen** → gar nicht, siehe Konzept 13
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
- [ ] `depot` außerhalb des Depots meldet, wo das Depot ist
- [ ] ⭐ **Eine vierte Ware ins `waren`-Dictionary eintragen, mehr nicht — sie erscheint in der Liste und ist kaufbar.** Wenn du dafür Code ändern musstest, steckt noch ein Warenname in der Logik
- [ ] Kaufen mit zu wenig Schrott sagt, dass der Schrott nicht reicht — und der Schrott wird **nicht** abgebucht
- [ ] Kaufen bei vollem Inventar sagt das — und der Schrott wird **nicht** abgebucht
- [ ] `kaufe hubschrauber` meldet, dass es die Ware nicht gibt
- [ ] Gekaufte Munition erhöht den Vorrat, ein gekauftes Medkit landet im Inventar
- [ ] Feuern senkt weiterhin die Munition, der Balken aus Etappe 3c stimmt weiterhin
- [ ] Eine volle Welle lässt sich von Anfang bis Ende spielen, ohne dass etwas abstürzt
- [ ] Im Grundriss ist der aktuelle Sektor markiert und wandert beim Gehen mit

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten. Dein Mentor fragt sie ab.

1. Was ist der Unterschied zwischen einer Liste und einem Dictionary — **nicht** in der Schreibweise, sondern in der Frage, die man stellt?
2. Wie kommst du an einen verschachtelten Wert, und was liefert der erste Schlüssel dabei zurück?
3. Was passiert bei einem Schlüssel, den es nicht gibt? Was macht `.get()` anders, und wann willst du welches von beiden?
4. **Was prüft `"medkit" in waren` — den Schlüssel oder den Wert?** Und wie fragst du nach dem anderen?
5. Was bekommst du, wenn du direkt über ein Dictionary iterierst? Und was liefert `.items()`?
6. Warum ist `sektoren` verschachtelt und `waren` flach? Nenn die Frage, mit der du das entscheidest.
7. Warum kann eine Liste kein Dictionary-Schlüssel sein? *(Ein Satz genügt — 👀.)*
8. **Warum kommt in deiner Kauflogik kein einziger Warenname vor — und was wäre der Preis dafür, wenn doch?**
9. Warum ist Schrott jetzt ein Dictionary-Eintrag und ein Medkit weiterhin ein Listeneintrag?
10. Was wird in deinem Programm verglichen und was angezeigt — und warum sollten das nicht dieselben Wörter sein?
11. Was ist ein *inkonsistenter Datenfehler*, und warum findet ihn kein Blick in die Bewegungslogik?
12. Welche deiner Werte ändern sich zur Laufzeit und welche nie? *(Die Frage kommt in Etappe 19 wieder.)*

**Frage 8 ist die wichtigste.** Die anderen sind Werkzeugwissen, und Werkzeugwissen holt man nach. Frage 8 ist der Übergang von *„ich schreibe Code, der Werte kennt"* zu *„ich schreibe Code, der Werte nachschlägt"* — und das ist der Gedanke, aus dem Etappe 22 und Etappe 25 vollständig bestehen. Wer ihn heute an drei Waren begriffen hat, versteht dort in zehn Minuten, warum dreißig Gegnertypen in eine Textdatei gehören.

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

**Vor jedem Experiment aufschreiben, was passieren wird.**

1. **Greif auf einen Schlüssel zu, den es nicht gibt.** Lies die Fehlermeldung ganz. Was genau steht in den Anführungszeichen?

2. **Verschreib dich absichtlich beim Zuweisen:** setz `sektoren["nordtorr"]["integritaet"] = 50` — oder, wenn das knallt, leg einen ganzen Sektor unter einem falschen Namen an. Ruf danach `umsehen` auf. **Kommt eine Fehlermeldung? Und wo ist der Wert hin, den du gesetzt hast?**

3. **Mach aus `nachbarn` eine Liste** statt eines Dictionaries: `["kern", "osttor"]`. Versuch, `gehe sueden` zu bauen. Woran genau scheitert es — und was sagt dir das darüber, was ein Dictionary eigentlich leistet?

4. **Lösch einen Sektor, auf den ein Nachbar zeigt.** Geh dann dorthin. Das ist der *inkonsistente Datenfehler* aus Konzept 12 — merk dir, an welcher Stelle er auffällt und wie weit die von der Ursache entfernt ist.

5. ⭐ **Schreib beim Kaufen `vorrat["schrott"] - preis` statt `-= preis`.** Kauf dreimal hintereinander dasselbe. **Das ist der Typ-3-Fehler dieser Etappe:** keine Fehlermeldung, kein Absturz — nur ein Spieler, der unendlich viel Geld hat. Der Ausdruck wird berechnet und weggeworfen.

6. **Buch den Schrott ab, bevor du prüfst, ob Platz im Inventar ist.** Kauf bei vollem Inventar. Wo ist der Schrott hin?

7. **Verändere ein Dictionary, während du darüber läufst** — lösch in einer `for`-Schleife über `waren` einen Eintrag. Vergleich die Fehlermeldung mit dem, was dieselbe Sache bei einer Liste in Etappe 4 gemacht hat. **Welches Verhalten ist dir lieber, und warum?**

8. **Versuch, eine Liste als Schlüssel zu benutzen.** Lies die Fehlermeldung. Das Wort `unhashable` musst du heute nicht verstehen — merk dir nur, dass es mit *unveränderlich* zu tun hat.

**Experiment 5 ist das wichtigste** und Experiment 7 das lehrreichste: Bei einer Liste läuft derselbe Fehler still durch, beim Dictionary knallt es. Dass eine Sprache manchmal streng ist, damit man nicht in Ruhe Unsinn machen kann, ist ein Gedanke, der dir bis Etappe 26 begegnet.

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

**Etappe 6** stellt Liste, Dictionary, Set und Tuple nebeneinander und beantwortet endgültig die Frage, die dich seit Etappe 4 begleitet: welche Struktur für welches Problem? Du wirst dort rückblickend sehen, dass du heute an zwei Stellen ein Dictionary benutzt hast, wo etwas anderes gepasst hätte.

**Etappe 7a** räumt deine Befehlskette auf. Der Kaufvorgang wird zur ersten Funktion, die wirklich etwas leistet — und du wirst merken, dass er nur deshalb so leicht auszulagern ist, weil er heute schon keine Warennamen kennt.

**Etappe 9** macht aus `aktueller_sektor` ein Attribut deines Marine. Aus einer losen Variablen wird `marine.sektor`.

**Etappe 13** räumt den Osttunnel frei. Ob das eine Zeile ist oder ein Umbau, entscheidet deine heutige Entscheidung 1.

**Etappe 14a** legt ein Raster neben deine Karte — und dann hast du beide Strukturen im selben Programm und kannst vergleichen, wofür jede taugt. Wenige benannte Orte mit Eigenschaften gegen viele gleichartige Zellen, auf denen gerechnet wird.

**Etappe 19** speichert deinen Spielstand. Dann wird die Frage aus Konzept 11 fällig: Was hat sich zur Laufzeit geändert und muss mit? Deine Sektorintegrität ja, deine Beschreibungen nein.

**Etappe 22** macht aus den Warendaten Baupläne mit Kosten, Bauzeit und Voraussetzungen. Deine flache Preistabelle bekommt Ebenen — und deine Entscheidung 2 von heute entscheidet, wie viel Arbeit das ist.

**Etappe 25** ist der große Zahltag: Die Sektorenkarte und die Warentabelle wandern in JSON-Dateien, ohne dass sich am Code etwas ändert. Dass das überhaupt möglich ist, liegt daran, dass du heute Daten von Logik getrennt hast.

---

## Abschluss

**In `GELERNT.md`:**

- Was habe ich gebaut?
- Was habe ich verstanden?
- Was hat mich überrascht? *(Kandidaten: `in` prüft Schlüssel · der Tippfehler, der einen neuen Eintrag anlegt · `x - y` statt `x -= y`)*
- Welchen Fehler habe ich gemacht — und **wie habe ich ihn gefunden?**
- **Entscheidung 1:** Fehlt der versiegelte Weg oder ist er markiert — und warum?
- **Entscheidung 2:** Hat das Depot einen Bestand — und warum (nicht)?
- **Wie unterscheidet mein Code stapelbare Waren von Einzelstücken?**
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
