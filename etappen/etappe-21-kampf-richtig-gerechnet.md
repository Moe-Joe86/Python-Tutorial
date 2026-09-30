# Etappe 21 — Kampf, richtig gerechnet

*v1.1.0 · 2026-09-30*

> **Block 3: Der Vorposten reagiert** · Etappe 21 von 30 · [← Etappe 20](etappe-20-wenn-der-spieler-unsinn-eingibt.md) · [Lehrplan](../Vorposten_Lehrplan.md) · Etappe 22 →

**Neue Syntax heute:** 21a: `max(a, b)` und `min(a, b)` mit Zahlen · Schlüsselwortargumente beim Aufruf — `f(schaden=10, wurf=3)` · 🧠 zwei Werte statt zweimal einen · 🧠 `return a, b` liefert ein Tuple · 🧠 der Zufall als Parameter · 🧠 abziehen gegen Anteil nehmen — 21b: `from enum import Enum` · `class Name(Enum):` mit seinen Mitgliedern im Klassenkörper · `Name.MITGLIED` · `.value` · `Name(wert)` — der Rückweg · `type(x) == Name` · `git branch` · `git checkout -b name` · 🧠 ein Mitglied ist nie gleich seinem Wert · 🧠 Tippfehler: `AttributeError` beim Mitglied, `ValueError` beim Rückweg, `TypeError` bei `json.dump` · 🧠 wann ein `Enum` lohnt · 🧠 nicht Committetes wandert beim Wechsel mit · 👀 `.name` · 👀 `is` bei Mitgliedern · 👀 `git switch` · 👀 Schadenstypen und Widerstände

**Zeitaufwand:** 21a: 5–6 Sitzungen · 21b: 4–5 Sitzungen, à 20–30 Minuten. Rund 65 Minuten davon sind Lesestoff — gut 35 in 21a (mit dem Anfang dieser Seite), gut 30 in 21b, die Abschnitte am Ende jeweils mitgerechnet. **Lies jeweils nur die Portion, an der du sitzt.**

**Voraussetzung:** Etappe 20 abgeschlossen, Selbsttest grün. Du brauchst deine Schadensberechnung aus Etappe 7a (seit Etappe 15 mit dem Zuschlag für Erkenntnisse), `aktueller_schaden()` und `aktuelle_reichweite()` aus 18, `treffe()` aus 18c, `pruefe_tabellen()` und `pruefe_zustand()` aus 20c, den festen `SEED` und `befehle17.txt` aus 17b — und für 21b `als_daten()`, `aus_daten()` und deine Zustandsinventur aus 19. **Aus `GELERNT.md` brauchst du zwei alte Zettel:** die Notizliste aus Etappe 3c und die Liste der Einfälle aus Etappe 7a.

**Die zwei Portionen:**

| | Was passiert | Was danach anders ist |
|---|---|---|
| **21a** | Die Rechnung | Ein Schuss kann danebengehen, und Panzerung schluckt Schaden. Eine Funktion rechnet das für jeden Schützen — und sagt, **was** passiert ist. |
| **21b** | Was darauf aufbaut | `"tot"` mit Tippfehler knallt, statt still durchzurutschen. Und du drehst an Zahlen, ohne dein Spiel zu riskieren — auf einem Branch. |

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **21a** | Eine Trefferrechnung mit zwei Rückgabewerten · `schiesse()` für alle Schützen · eine Untergrenze mit `max()` · `pruefe_trefferrechnung()` | Warum zwei Werte statt zweimal einen · der Zufall kommt von außen · abziehen gegen Anteil nehmen | — |
| **21b** | Ein `Enum` für die Zustände deiner Einheiten · der Spielstand übersetzt · ein Branch fürs Balancing | Wann ein `Enum` lohnt und wann nicht · Balancing ist ein Experiment | `.name` · `is` bei Mitgliedern · `git switch` · Schadenstypen und Widerstände |

---

# Teil 21a — Die Rechnung

## Worum es geht

Seit Etappe 3c trifft jeder Schuss. Du tippst `feuern`, der Gegner verliert Trefferpunkte, immer gleich viele. Ein Kriecher und eine Panzerbrut unterscheiden sich darin nur durch ihre Trefferpunkte — die Panzerbrut hält länger durch, aber jeder Schuss wirkt auf sie genau wie auf alles andere.

**Das war Absicht.** Etappe 3c hat es *„absichtlich primitiv"* genannt und die richtige Formel hierher verschoben. Heute kommt sie, und sie besteht aus drei Dingen, nicht aus acht:

| | Frage | Wem gehört die Zahl |
|---|---|---|
| **Trefferchance** | Trifft der Schuss überhaupt? | dem Schützen |
| **Schaden** | Wie viel richtet er an? | dem Schützen — so, wie du ihn seit 18 abgeleitet berechnest |
| **Panzerung** | Wie viel davon kommt an? | dem Ziel |

Drei Zahlen, und dein Spiel fühlt sich danach anders an. **Ein Fehlschuss kostet Munition** — also wird Nachladen, seit Etappe 3b eine Runde wert, zu einer echten Entscheidung, und die Munition, die du seit Etappe 5 kaufst, reicht nicht mehr für jeden Gegner genau einmal. **Und die Panzerbrut wird etwas anderes als ein dicker Kriecher:** Gegen sie zählen starke Treffer mehr als viele schwache.

**Der eigentliche Lernstoff steckt aber nicht in der Formel.** Er steckt in einer Frage, die dir die Formel stellt: *Wie sagt eine Funktion ihrem Aufrufer, was passiert ist?* Ein Schuss, der `0` Schaden macht, kann danebengegangen sein — oder getroffen haben und abgeprallt sein. **Eine Zahl allein kann das nicht unterscheiden.** Heute gibt deine Funktion zwei Werte zurück, und du wirst sehen, warum das mehr ist als eine Bequemlichkeit.

---

## Der lange Bogen — was heute fällig wird

**In 21a:**
- **Etappe 3c:** *Die Platzhalter-Kampfformel — die richtige kommt in 21a.* Und deine **Notizliste** *„was fühlt sich falsch an"*, auf der seit damals steht, was dich beim Spielen gestört hat.
- **Etappe 6:** *Die Komma-Falle.* Dort stand als Beispiel `return schaden, war_kritisch`. Die Form kommt heute — mit der Trefferart als zweitem Wert statt eines kritischen Treffers. *(Kritische Treffer baut der Plan nicht; drei Dinge, nicht acht. Sie stehen unter „Wenn du mehr willst".)*
- **Etappe 7a:** *`berechne_schaden()` wird zur echten Kampfformel.* Und die **Liste der Einfälle, die du nicht gebaut hast** — heute die Vorlage.
- **Etappe 7b:** *`return` statt `print` in der Logik.* Heute ist das der Grund, warum eine Funktion zwei Werte zurückgibt statt eine Meldung. Und *„Was muss immer gelten?"* — drei `assert`-Zeilen zur Schadensformel.
- **Etappe 11b:** *Die Klassentabelle mit dem Soldaten als Bezugsfall.* Heute bekommt der Soldat eine Trefferchance, und die anderen drei werden an ihm gemessen.
- **Etappe 14b:** *`<` gegen `<=` bei der Reichweite.* Die Entscheidung bleibt — und wird zur ersten von zwei Fragen, die ein Schuss beantworten muss.
- **Etappe 15b:** *Wer profitiert vom Zuschlag — nur du, oder jeder, der schießt?* Heute rechnen alle Schützen über dieselbe Stelle. Deine Entscheidung von damals muss das überstehen.
- **Etappe 18:** *`aktueller_schaden()` ist der Eingang, die Passiva werden abgefragt, `treffe()` ist der Ort, an dem Schaden ankommt.*
- **Etappe 20c:** *Deine Invarianten als `assert`* — heute kommen drei über die Rechnung dazu.

**In 21b:**
- **Etappe 12:** *`"aktiv"` und `"tot"` sind Strings — „ein Tippfehler in `"aktvi"` erzeugt keinen Fehler, sondern einen Zustand, in dem nichts mehr passt. Etappe 21b löst das ab."* Dazu der Begriff **Zustandsautomat**, damals ohne benannte Werte.
- **Etappe 16 und 18:** *Ein `Enum` gegen Verweise ins Leere* und *kein `Enum` für Effekt- und Flag-Wörter — Etappe 21b.* Heute fällt die Entscheidung.
- **Etappe 19:** *Wenn die Zustände ein `Enum` werden, ist der Spielstand die erste Stelle, an der du übersetzen musst.* Und deine **Zustandsinventur**.
- **Etappe 3c, 13, 17a, 18, 19c:** *Balancing ist Etappe 21b, auf einem eigenen Branch* — die Zahlen, die überall als *„Startwerte, keine Empfehlung"* stehen.

---

## Eine Design-Entscheidung: Kann Panzerung einen Treffer ganz schlucken? ⭐

**Das Problem:** Ein Kamerad, der gerade erschüttert ist, schießt mit halbem Schaden — sagen wir `3`. Er trifft eine Panzerbrut mit Panzerung `4`. **Was kommt an?**

Rechnerisch minus eins. Das darf es nicht geben — ein Schuss, der heilt, ist der Klassiker unter den stillen Fehlern in Kampfsystemen, und du baust ihn dir im Kaputtmachen absichtlich. **Eine Untergrenze muss also her. Die Frage ist nur, welche:**

| | **a) Jeder Treffer zählt** | **b) Panzerung kann alles schlucken** |
|---|---|---|
| Regel | Ein Treffer macht **mindestens 1** Schaden | Bleibt nach der Panzerung nichts übrig, macht er **0** |
| Mögliche Ergebnisse | `"treffer"` · `"verfehlt"` | `"treffer"` · `"verfehlt"` · `"abgeprallt"` |
| Schwache Schützen gegen die Panzerbrut | kratzen langsam — aber sie kratzen | richten nichts aus |
| Was das Spiel dem Spieler beibringt | Masse hilft immer ein bisschen | Gegen Panzer braucht es Wucht — oder eine Fähigkeit |

**Beide Varianten sind vertretbar**, und der Plan empfiehlt keine. **Wähl eine und schreib sie mit einem Satz Begründung in `GELERNT.md`** — in Auftragsschritt 2 baust du danach.

*(Bei b) siehst du den Grund für diese ganze Portion am deutlichsten: `"verfehlt"` und `"abgeprallt"` machen beide `0` Schaden. Ohne einen zweiten Rückgabewert könnte niemand sie auseinanderhalten.)*

---

## Die Konzepte — Teil 21a

Heute auf einem Jahrmarkt.

### 1. Drei Dinge — und zwei Fragen, die vorher schon beantwortet sind

Ein Schuss beantwortet in deinem Spiel **zwei** Fragen, und nur die zweite ist heute neu:

| Frage | Wer beantwortet sie | Seit |
|---|---|---|
| **Darf ich überhaupt schießen?** Ist ein Ziel da, ist es in Reichweite, ist Munition im Magazin? | die Stelle, die schießt — mit `aktuelle_reichweite()` und deiner Entscheidung `<=` | Etappe 12, 14b, 18 |
| **Was richtet der Schuss an?** Trifft er, wie viel, wie viel kommt an? | **die Trefferrechnung** | heute |

**Die Trennung ist der Punkt.** Die Trefferrechnung prüft keine Reichweite und zählt keine Munition. Sie bekommt einen Schuss, der stattfindet, und rechnet aus, was er bewirkt. Alles, was vorher entschieden wird, bleibt, wo es ist.

**Und drei Dinge bleiben ausdrücklich draußen**, als Regeln dieses Spiels:

- **Fähigkeiten würfeln nicht und ignorieren Panzerung.** Eine Granate, eine Mine, der Durchschlag des Heavy: Sie treffen, was sie treffen, mit dem Schaden aus ihrer Tabelle. Das macht Fähigkeiten gegen die Panzerbrut wertvoll — und genau das ist gewollt.
- **Gegner würfeln nicht.** Wer das Tor erreicht, trifft, wie seit Etappe 12.
- **Säure und andere Effekte fressen durch jede Panzerung.** Sie laufen über `nimm_schaden()`, nicht über die Rechnung.

*(Ob diese Regeln gut sind, ist eine Balancing-Frage, und die gehört nach 21b.)*

### 2. ⭐⭐ Zwei Werte statt zweimal einen

Am Getränkestand gibt man Pfandbecher zurück. Ein Automat prüft jeden Becher:

```python
def pruefe_becher(code, sauber):
    """Gibt das Pfand in Cent und den Grund zurück."""
    if code not in PFANDCODES:
        return 0, "fremder Becher"
    if not sauber:
        return 0, "nicht gespült"
    return PFANDCODES[code], "angenommen"
```

**Der Automat liefert zwei Dinge: wie viel es gibt, und warum.** Der Aufrufer bekommt beide auf einmal und macht daraus, was er braucht:

```python
betrag, grund = pruefe_becher("J24", True)
print(f"{grund}: {betrag} Cent")
```

**Warum nicht einfacher?** Es gibt vier naheliegende Alternativen, und jede hat einen Haken:

| Statt zwei Rückgabewerten … | Der Haken |
|---|---|
| **Nur den Betrag zurückgeben** | `0` kann *„fremder Becher"* heißen oder *„nicht gespült"*. Der Aufrufer muss raten. |
| **Die Funktion gibt die Meldung selbst aus** | Dann meldet sie auch, wenn niemand fragt — und in Etappe 26 kannst du sie nicht prüfen, ohne den Bildschirm zu lesen. Das ist die Linie aus Etappe 7b. |
| **Zwei Funktionen: eine für den Betrag, eine für den Grund** | Beide müssen dieselbe Prüfung machen, zweimal. Und sobald Zufall im Spiel ist, wird es falsch — mehr dazu gleich. |
| **Den Grund in ein Attribut schreiben** (`automat.letzter_grund`) | Ein versteckter Zustand, den jemand im richtigen Moment lesen muss. Einen Aufruf später steht dort schon etwas anderes. |

**Die dritte Zeile ist bei dir die entscheidende.** Deine Trefferrechnung würfelt. Rufst du für den Schaden eine Funktion auf und für die Trefferart eine zweite, würfelt jede für sich — und dann kann ein Schuss laut der einen treffen und laut der anderen danebengehen. **Was zusammen entschieden wird, muss zusammen zurückkommen.**

> **Eine Funktion, die einen Vorgang auswertet, gibt das Ergebnis und seine Art zusammen zurück. Was der Aufrufer damit tut — melden, zählen, ignorieren —, entscheidet der Aufrufer.**

### 3. `return a, b` — die Form aus Etappe 7, von der anderen Seite

`return a, b` kennst du seit Etappe 7a. Heute der Blick darauf, **was dabei eigentlich zurückkommt:**

```python
ergebnis = pruefe_becher("J24", True)
print(ergebnis)          # (25, 'angenommen')
print(type(ergebnis))    # <class 'tuple'>
```

**Es kommt ein einziges Ding zurück: ein Tuple.** Das Komma in `return 25, "angenommen"` baut es — genau die Regel aus Etappe 6, Konzept 8: *Ein Tuple entsteht durch das Komma, nicht durch die Klammern.* `return (25, "angenommen")` ist dasselbe. Und `betrag, grund = …` ist Tuple-Unpacking, auch aus Etappe 6.

**Daraus folgen drei Fehlerbilder, die du heute sehen wirst:**

| Du schreibst | Was passiert |
|---|---|
| `betrag = pruefe_becher(...)` — **ein** Name | Kein Fehler. `betrag` ist das ganze Tuple. Es knallt erst, wenn du damit rechnest oder vergleichst — `TypeError: … 'tuple' and 'int'` — **eine oder viele Zeilen später** |
| `a, b, c = pruefe_becher(...)` — drei Namen | `ValueError: not enough values to unpack (expected 3, got 2)` — sofort, in der Zeile |
| Ein Zweig endet mit `return 0` statt `return 0, "…"` | Auspacken scheitert — aber nur, wenn genau dieser Zweig läuft: `TypeError: cannot unpack non-iterable int object` |

**Die erste Zeile ist die gefährliche**, weil sie nicht dort knallt, wo sie entsteht. **Die dritte ist die heimtückische**, weil sie in einem seltenen Zweig sitzt. Daraus die Regel, die in Auftragsschritt 2 gilt:

> **Jeder Zweig einer Funktion, die zwei Werte zurückgibt, gibt zwei Werte zurück.** Auch der, in dem nichts passiert.

### 4. ⭐ Der Zufall kommt von außen

An der Losbude zieht man ein Los. Die Gewinnquote hängt aus: 30 von 100 Losen gewinnen. So sieht die Auswertung aus, wenn der Zufall **innen** entsteht:

```python
def ist_gewinn(gewinnquote):
    wurf = random.randint(1, 100)
    return wurf <= gewinnquote
```

Und so, wenn er **von außen** kommt:

```python
def ist_gewinn(gewinnquote, wurf):
    return wurf <= gewinnquote

gewonnen = ist_gewinn(30, random.randint(1, 100))
```

**Eine Zeile verschoben. Und die zweite Fassung kann etwas, das die erste nie können wird:** Du kannst sie prüfen, ohne zu würfeln.

```python
assert ist_gewinn(30, 30), "Die Grenze selbst muss gewinnen"
assert not ist_gewinn(30, 31), "Eins über der Grenze darf nicht gewinnen"
assert not ist_gewinn(0, 1), "Eine Quote von 0 gewinnt nie"
```

**Drei Zeilen, jede beantwortet eine Frage mit Ja oder Nein, bei jedem Lauf gleich.** Mit dem Würfel innen müsstest du tausendmal ziehen und hoffen, dass der Grenzfall dabei ist — oder den Seed aus Etappe 17b festsetzen und dir merken, welche Zahl als Nächstes kommt.

> **Eine Funktion, die nur rechnet, bekommt alles, was sie braucht, als Parameter — auch den Zufall.** Dann liefert sie für dieselben Eingaben immer dasselbe, und genau das kann man prüfen.

*(In Etappe 26 heißt so eine Funktion **testbar**, und die drei Zeilen oben werden fast unverändert Tests. Heute sind sie Behauptungen beim Start — die Form aus Etappe 20c.)*

### 5. Eine Chance in Prozent — `randint` und `<=`

Seit Etappe 17a kennst du `random.randint(a, b)` mit **beiden Enden eingeschlossen**. Für eine Chance in Prozent:

```python
wurf = random.randint(1, 100)
if wurf <= 30:
    ...                  # in 30 von 100 Fällen
```

**Die Zahlen 1 bis 30 sind genau 30 von 100.** Die Grenze und der Wurfbereich gehören zusammen — die Regel aus Etappe 17a, Konzept 3:

| Wurfbereich | Vergleich | Anteil bei Quote 30 |
|---|---|---|
| `randint(1, 100)` | `wurf <= 30` | **30 %** ✓ |
| `randint(1, 100)` | `wurf < 30` | 29 % — still falsch |
| `randint(0, 100)` | `wurf <= 30` | 31 von 101 — still falsch |

**Und die zwei Ränder, die jede Quote haben muss:** Bei `0` gewinnt nie etwas, bei `100` immer. Prüf beide, wenn du eine solche Zeile baust — sie sind die zwei Fälle, an denen ein `<` statt `<=` sofort auffällt.

**Prüfen, ob es stimmt, geht nur durch Zählen** — dein Werkzeug aus Etappe 17a, Konzept 4: zehntausend Würfe, Treffer zählen, durch zehntausend teilen. Bei `75` erwartest du ungefähr 7500, nicht genau.

### 6. ⭐ Abziehen oder einen Anteil nehmen?

An der Kasse des Jahrmarkts gibt es zwei Sorten Rabatt. **Vier Euro weniger** oder **dreißig Prozent weniger**. Für drei Einkäufe:

| Einkauf | 4 € weniger | 30 % weniger (`preis * 70 // 100`) |
|---|---|---|
| 10 € | **6 €** — 40 % gespart | 7 € |
| 20 € | 16 € — 20 % gespart | 14 € |
| 40 € | 36 € — nur 10 % gespart | **28 €** |

**Der feste Betrag trifft kleine Einkäufe hart und große kaum. Der Anteil trifft alle gleich — immer 30 %.** Irgendwo zwischen 10 und 20 € sparen beide gleich viel, und genau deshalb merkt man den Unterschied nicht, solange man nur mit einem mittleren Betrag ausprobiert.

**Übertragen auf Panzerung — die Frage aus dem Lehrplan:** Eine Panzerung, die **abzieht**, macht schwache Schüsse fast wertlos und starke kaum schwächer. Eine, die einen **Anteil** nimmt, schwächt alle gleich. **Dieser Plan zieht ab**, weil es die Panzerbrut zu dem macht, was sie sein soll: ein Gegner, gegen den Wucht zählt. Der Preis dafür steht in der Design-Entscheidung oben — der schwache Schuss, der unter null rutscht.

**Beim Balancing heißt das:** Wer bei einer abziehenden Formel den Schaden erhöht, macht einen Schützen gegen gepanzerte Gegner **überproportional** stärker. Bei einer Formel mit Anteil nicht. *(Das ist eine der Fragen, die in 21b auf dich warten.)*

**Und die Untergrenze dazu, mit einem neuen Werkzeug:**

```python
kassenstand = max(0, kassenstand - auszahlung)     # nie unter null
fuellstand = min(100, fuellstand + nachschub)       # nie über hundert
```

**`max(a, b)` gibt die größere von zwei Zahlen zurück, `min(a, b)` die kleinere.** Gelesen klingt es verkehrt herum, deshalb der Merksatz: **`max` setzt eine Untergrenze, `min` eine Obergrenze.** `max(0, -3)` ist `0`, `max(0, 5)` ist `5`. Es geht auch mit einem `if` — `max` sagt dasselbe in einer Zeile, und man sieht der Zeile an, dass sie begrenzt.

*(`max()` und `min()` können mehr, auch über ganze Listen und mit einem Schlüssel. Das ist Etappe 23a. Heute zwei Zahlen.)*

### 7. Namen beim Aufruf — wenn vier Zahlen nebeneinanderstehen

An der Zuckerwattemaschine:

```python
def spinne(zucker, farbe, dauer):
    ...

spinne(40, "rosa", 12)
spinne(zucker=40, farbe="rosa", dauer=12)
spinne(dauer=12, zucker=40, farbe="rosa")
```

**Alle drei Aufrufe tun dasselbe.** Im zweiten und dritten steht vor jedem Wert der Name des Parameters, und dann ist die **Reihenfolge egal** — Python ordnet nach Namen zu. Das heißt **Schlüsselwortargument**.

**Wozu, wenn es länger ist?** Seit Etappe 7a weißt du: *Beim Aufruf wird die Reihenfolge nicht geprüft.* Das ist harmlos, solange die Werte verschieden aussehen. Bei deiner Trefferrechnung stehen **vier Zahlen** nebeneinander — Schaden, Trefferchance, Panzerung, Wurf. `berechne_treffer(12, 4, 75, 30)` ist falsch und stürzt nicht ab: Panzerung und Trefferchance sind vertauscht. Der Schütze trifft jetzt mit 4 Prozent, fast jeder Schuss geht daneben — und das Spiel fühlt sich einfach schwer an. **Ein Typ 3.**

Mit Namen kann das nicht passieren — und Tippfehler im Namen knallen:

| Du schreibst | Was passiert |
|---|---|
| `spinne(zucker=40, farbe="rosa", dauer=12)` | läuft |
| `spinne(zuker=40, farbe="rosa", dauer=12)` | `TypeError: spinne() got an unexpected keyword argument 'zuker'` — neuere Python-Versionen fragen dazu: *Did you mean 'zucker'?* |
| `spinne(40, zucker=40, farbe="rosa")` | `TypeError: spinne() got multiple values for argument 'zucker'` |

**Die Regel für heute:** Wo ein Aufruf mehrere Zahlen übergibt, die man verwechseln kann, schreibst du die Namen dazu. In deinen `assert`-Zeilen immer — dort soll man beim Lesen sehen, was geprüft wird. *(Mischen geht auch — erst ohne Namen, dann mit. Umgekehrt nicht. Du brauchst es heute nicht.)*

### 8. Rechnen mit Zahlen, Objekte am Rand

Auf dem Jahrmarkt gibt es einen Stand, an dem man Ringe wirft. Der Betreiber hat zwei Aufgaben: ausrechnen, was ein Wurf bringt, und das Ergebnis im Stand eintragen.

**Die Rechnung selbst braucht keinen Stand.** Sie braucht Zahlen. **Das Eintragen braucht den Stand**, aber keine Rechnung. Also zwei Stücke:

```
reine Rechnung:   Zahlen rein  →  Zahlen raus          (prüfbar, ohne irgendetwas aufzubauen)
Methode am Stand: Objekte lesen → Rechnung aufrufen → Ergebnis eintragen
```

**Das ist die Kopplungsfrage aus Etappe 12 und 15, zum ersten Mal mit einer billigen Antwort in die andere Richtung:** Die Rechnung bekommt nicht die Welt, nicht den Schützen, nicht das Ziel — nur die vier Zahlen, die sie braucht. Die Methode drumherum kennt die Objekte, liest die Zahlen heraus und schreibt das Ergebnis zurück.

**Und wo kommen die Zahlen her?** Nicht aus Attributen, sondern aus deinen abgeleiteten Werten aus Etappe 18:

> **Die Rechnung fragt die Methode, nicht das Attribut.**

`aktueller_schaden()` kennt die Effekte. `aktuelle_reichweite()` kennt die Zielhilfe. Standfest schützt davor, dass `aktueller_schaden()` halbiert. **Die Trefferrechnung fragt keine einzige Fähigkeit direkt ab — und berücksichtigt trotzdem alle**, weil sie ihre Eingaben von Methoden bekommt, die das schon erledigt haben. Das ist die Einlösung aus Etappe 18: *Die Trefferrechnung fragt die Passiva ab* — über den Weg, den du dort gebaut hast.

---

## Dein Auftrag — Teil 21a

---

### 1. Hol die zwei alten Zettel heraus

In `GELERNT.md` stehen seit Etappe 3c deine Notizliste *„was fühlt sich falsch an"* und seit Etappe 7a die Liste der Einfälle, die du nicht gebaut hast.

- **Sortier jeden Eintrag in eine von drei Spalten:** *gehört in die Rechnung von heute* · *eine Zahl zum Drehen — 21b* · *gehört nicht in dieses Spiel, oder nicht jetzt*.
- **Streich, was sich erledigt hat.** Einiges davon haben Etappen seit 3c schon gebaut.

*(Die mittlere Spalte ist dein Material für den Branch in 21b. Die rechte ist genauso wertvoll: Sie ist der Beweis, dass du Einfällen widerstanden hast.)*

---

### 2. ⭐ Bau `berechne_treffer()`

Eine **Funktion**, keine Methode — zu deinen anderen Funktionen, über das Hauptprogramm (Etappe 7a, Konzept 1).

| Parameter | Bedeutung |
|---|---|
| `schaden` | der Schaden, den der Schuss mitbringt |
| `treffsicherheit` | die Trefferchance des Schützen in Prozent, `0` bis `100` |
| `panzerung` | die Panzerung des Ziels |
| `wurf` | eine Zahl von `1` bis `100`, gewürfelt **außerhalb** |

**Rückgabe: zwei Werte** — der Schaden, der ankommt, und die Trefferart als Text. Welche Trefferarten es gibt, hängt an deiner Design-Entscheidung: `"treffer"` und `"verfehlt"`, bei b) zusätzlich `"abgeprallt"`.

- **Verfehlt:** `0` Schaden. Ob verfehlt, entscheidet der Vergleich aus Konzept 5.
- **Getroffen:** Schaden minus Panzerung, mit der Untergrenze aus deiner Design-Entscheidung — bei a) mit `max()`, bei b) mit einem `if`, das den dritten Fall erkennt.
- **Jeder Zweig gibt zwei Werte zurück.** Konzept 3.
- **Kein `print`, kein `random`, keine Objekte.** Nur die vier Zahlen rein, zwei Werte raus. Konzept 4 und 8.

Ein Docstring, der sagt, was zurückkommt — beide Werte.

**So prüfst du es:** In einer frisch kopierten Probedatei, wie seit Etappe 9. Rechne **vorher** aus, was herauskommen muss, und ruf dann auf: Schaden `12`, Treffsicherheit `75`, Panzerung `4`, Wurf `75`. Dann derselbe Schuss mit Wurf `76`. Dann Schaden `3`, Treffsicherheit `75`, Panzerung `4`, Wurf `1`. **Drei Ergebnisse, jedes mit zwei Werten, und keines ist negativ.**

---

### 3. ⭐ Schreib auf, was immer gelten muss — und lass es beim Start prüfen

Die Frage aus Etappe 7b, heute mit Antwort: **Was muss bei deiner Trefferrechnung immer gelten?**

- **Eine Funktion `pruefe_trefferrechnung()`** — neben `pruefe_tabellen()` aus 20c, und genau wie diese **einmal beim Start** aufgerufen, bevor die erste Welle beginnt.
- **Mindestens drei `assert`-Zeilen**, jede mit Text. Zwei Anregungen aus dem Lehrplan: *Ist der Schaden je negativ? Kommt ohne Panzerung der volle Schaden an?* Die dritte findest du selbst — vielleicht an einem Rand aus Konzept 5. **Mindestens eine Behauptung prüft einen Schuss, dessen Schaden kleiner ist als die Panzerung** — sonst merkt keine, wenn die Untergrenze fehlt.
- **Jeder Aufruf darin mit Schlüsselwortargumenten** (Konzept 7) und mit einem **festen** Wurf. Konzept 4 ist der Grund, warum das überhaupt geht.

**Und eine Zeile mehr in `pruefe_zustand(welt)` aus 20c:** Keine Einheit hat mehr Trefferpunkte als ihren Startwert aus Etappe 13, Schritt 12. *(Warum gerade diese Zeile hierher gehört, zeigt dir Kaputtmachen 1.)*

**So prüfst du es:** Bau vorübergehend einen Fehler in `berechne_treffer()` — nimm die Untergrenze heraus, oder dreh den Vergleich aus Konzept 5 um. Starte das Spiel. **Es muss beim Start knallen, mit deinem Text**, bevor die erste Welle läuft. Danach zurück.

---

### 4. Leg die Werte an — vorerst neutral

**Zuerst der Beweis**, wie in Etappe 17b: `SEED` fest, dann im Projektordner

```
python spiel.py < befehle17.txt > vorher.txt
```

`vorher.txt` entsteht von selbst und wird bei jedem Lauf überschrieben.

**Dann zwei neue Werte, beide so gewählt, dass sich noch nichts ändert:**

- **`treffsicherheit = 100`** in `__init__` jeder Klasse, die schießt: deine Marines, dein Basisturm, der mobile Turm des Engineer. *(Wo genau, hängt davon ab, wo bei dir die anderen Werte je Klasse stehen — seit Etappe 11b. Dort auch.)*
- **`"panzerung": 0`** in **jedem** Eintrag von `GEGNERTYPEN`, und jeder `Gegner` übernimmt den Wert beim Erzeugen als `self.panzerung`. *(Der Gegner kennt seinen Typ über seinen `name`, seit 11b. Und weil **jeder** Eintrag den Schlüssel hat, liest du mit eckigen Klammern, nicht mit `.get()` — die Regel für gleichmäßige Daten aus Etappe 5.)*

**So prüfst du es:** Das Spiel läuft wie vorher. Und die Tabellenprüfung aus 20c: Fehlt einem Gegnertyp der neue Schlüssel, soll `pruefe_tabellen()` das beim Start sagen — ergänz eine Zeile, wenn sie es nicht tut.

---

### 5. ⭐⭐ Bau `schiesse()` — ein reiner Umbau vor dem Umbau

Das Muster aus Etappe 18c, Schritt 20, diesmal als Regel:

> **Erst die Struktur ändern, dann das Verhalten.** Nie beides im selben Schritt — sonst beweist `diff` nichts mehr.

- **`Einheit` bekommt eine Methode `schiesse(ziel, schaden, welt)`.** Sie legt den Wurf fest, ruft `berechne_treffer()` auf, lässt den angekommenen Schaden über `treffe()` wirken — **nur wenn er größer als `0` ist** — und gibt beide Werte zurück.
- **Der Wurf ist heute noch fest: `wurf = 1`**, mit einem Kommentar, dass er in Schritt 6 zum Würfel wird. Warum nicht gleich würfeln, zeigt dir Kaputtmachen 5.
- **Die Fahndung:** Such jede Stelle, an der ein **Schuss** über `treffe()` wirkt, und zähl sie. Der Held beim `feuern` — beim Schnellfeuer zweimal —, die Kameraden in `update()`, dein Basisturm, der mobile Turm. **An jeder dieser Stellen steht ab heute `schiesse()` statt `treffe()`.**
- **Der Schaden, den du übergibst, ist derselbe wie bisher** — beim Helden aus deiner Schadensberechnung mit dem Zuschlag aus Etappe 15, bei den anderen, wie du es damals entschieden hast, beim Basisturm mit der Halbierung aus 17c. **Nichts davon zieht in `schiesse()` um.**
- **Fähigkeiten und Minen rufen weiterhin `treffe()` direkt** — Konzept 1.

⚠️ **Die Meldungen bleiben heute, wie sie sind.** Wo bisher nach dem Schuss etwas gemeldet wurde, wird weiter dasselbe gemeldet — mit dem Schaden, den `schiesse()` zurückgibt. Neue Meldungen sind Schritt 7.

**So prüfst du es:**

```
python spiel.py < befehle17.txt > nachher.txt
diff vorher.txt nachher.txt
```

**Kein Unterschied.** Mit Trefferchance `100`, Panzerung `0` und Wurf `1` trifft jeder Schuss mit vollem Schaden — genau wie gestern. *(Redet `diff` an einer Stelle, an der ein Schuss vorher `0` Schaden machte, dann ist das deine Untergrenze aus Variante a) — kein Fehler, sondern der erste Fall, in dem sie greift. Jede andere Stelle ist ein Fund.)*

---

### 6. ⭐ Schalt die Rechnung ein

Jetzt ändert sich dein Spiel.

- **Der Wurf wird ein Würfel:** `random.randint(1, 100)` in `schiesse()` — nirgendwo sonst.
- **Trefferchance nach Klasse** — der Soldat ist der Bezugsfall seit Etappe 11b, die anderen stehen relativ zu ihm:

| Schütze | `treffsicherheit` |
|---|---|
| Soldat | `75` — der Bezugsfall |
| Heavy | `65` |
| Engineer | `70` |
| Medic | `70` |
| Basisturm | `80` |
| mobiler Turm | `70` |

- **Panzerung nach Gegnertyp:**

| Gegnertyp | `"panzerung"` |
|---|---|
| `"kriecher"` | `0` |
| `"speier"` | `1` |
| `"panzerbrut"` | `4` |

*(Hast du einen vierten Typ, bekommt er eine Zahl deiner Wahl. Alle Zahlen hier sind Startwerte für 21b, keine Empfehlung.)*

- **Die Frage aus Etappe 15b, noch einmal:** Alle Schützen rechnen jetzt über dieselbe Stelle. **Trägt deine Entscheidung, wer vom Zuschlag profitiert, noch?** Ein Satz in `GELERNT.md` — ändern darfst du sie, musst du nicht.

⚠️ **Ein Fehlschuss kostet einen Schuss.** Prüf an jeder Stelle aus der Fahndung: Wird die Munition verbraucht, **bevor** gewürfelt wird — oder nur, wenn getroffen wurde? Nur das Erste ist richtig. Ein Schütze, der beim Danebenschießen nichts verbraucht, schießt umsonst — und in 21b erfährst du, warum das die gefährlichste Sorte Balancing-Fehler ist.

**So prüfst du es — zweimal:**

1. **In der Probedatei, nach Konzept 5:** zehntausendmal `berechne_treffer()` mit einem echten Wurf aufrufen — Schaden `12`, Treffsicherheit `75`, Panzerung `0` — und die Trefferarten zählen, wie in Etappe 17a. **Ungefähr 7500 Treffer.** Dann mit `0` und mit `100` — **genau 0 und genau 10 000.**
2. **Im Spiel:** Eine Panzerbrut nimmt vom selben Schuss weniger Schaden als ein Kriecher. Und dein Magazin leert sich schneller als gestern.

---

### 7. Gib dem Spieler Rückmeldung

Deine Funktion gibt aus gutem Grund nichts aus. **Jetzt entscheidet der Aufrufer.**

- **Beim Helden:** eine Meldung je Trefferart — nach der Trefferart gefragt, nicht nach dem Schaden. *„Daneben."* ist etwas anderes als *„Abgeprallt — die Panzerung hält."*, auch wenn beide `0` sind.
- **Bei den Kameraden und den Türmen:** Entscheide, was gemeldet wird. Jeder Fehlschuss von drei Kameraden und zwei Türmen ist eine Menge Text. *(Die Frage aus Etappe 17c: Muss der Spieler jetzt etwas tun? Dein Wellenbericht kann zählen, statt zu melden.)*

**So prüfst du es:** Eine Welle spielen. **Du kannst an der Ausgabe erkennen, ob dein Held getroffen hat, danebengeschossen hat oder abgeprallt ist** — ohne eine Zahl lesen zu müssen.

---

### 8. Prüf, dass das Alte noch läuft, und commit

- **`pruefe_trefferrechnung()` und `pruefe_zustand()` schweigen** über eine ganze Welle, mit allen Fähigkeiten.
- **Der Beweislauf aus 17b:** fester Seed, `befehle17.txt`, **zwei** Läufe hintereinander, `diff` — schweigt. Dein Spiel würfelt jetzt öfter, aber immer noch dieselben Zahlen bei demselben Seed.
- **Der Beweislauf aus 19c** mit `befehle19a.txt` und `befehle19b.txt`: weiterhin genau ein Unterschied, ganz oben.
- **Die Chaos-Datei aus 20a** — keine Behauptung knallt.
- Keine Probedatei, kein fester Wurf mehr, kein vorübergehender Fehler. `vorher.txt` und `nachher.txt` weg.
- Die Abschnitte am Ende, die zu 21a gehören: **Transferaufgabe** und **Kaputtmachen 1 bis 5**.

Commit: `Etappe 21a: Der Kampf rechnet richtig`

---

## Selbsttest — 21a

- [ ] `berechne_treffer()` enthält kein `print`, kein `random` und bekommt kein Objekt — nur vier Zahlen.
- [ ] Jeder Zweig darin gibt zwei Werte zurück.
- [ ] `pruefe_trefferrechnung()` läuft beim Start, hat mindestens drei Behauptungen mit Text, und jede ruft mit Schlüsselwortargumenten und festem Wurf auf.
- [ ] Ein vorübergehend eingebauter Fehler in der Rechnung knallt **beim Start**, nicht mitten in einer Welle.
- [ ] Zehntausend Würfe mit Treffsicherheit `75` ergeben ungefähr 7500 Treffer; `0` ergibt keinen, `100` jeden.
- [ ] Kein Schuss richtet negativen Schaden an — auch ein erschütterter Kamerad nicht gegen eine Panzerbrut.
- [ ] Jeder Schütze schießt über `schiesse()`; Fähigkeiten und Minen rufen `treffe()` direkt.
- [ ] Ein Fehlschuss verbraucht Munition.
- [ ] Der Beweislauf aus 17b schweigt bei zwei Läufen mit demselben Seed.

> **⏸ Ende von 21a.** Dein Kampf rechnet, und eine Funktion sagt, was passiert ist, ohne selbst etwas zu sagen. 21b gibt deinen Zuständen einen Namen, der Tippfehler nicht verzeiht — und dir einen Ort, an dem du an Zahlen drehen darfst, ohne etwas zu riskieren.

---

# Teil 21b — Was darauf aufbaut

## Worum es geht

**Tipp in deinem Code einmal `"tto"` statt `"tot"`** — an einer einzigen Stelle, etwa dort, wo ein Gegner stirbt. Starte das Spiel. **Nichts passiert.** Kein Traceback, keine Warnung. Der Gegner hat jetzt einen Zustand, den keine Zeile deines Programms kennt. Er ist nicht `"tot"`, also räumt ihn niemand weg, und deine Kameraden beschießen ihn weiter — ob er selbst weiter handelt, hängt davon ab, wie deine Vergleiche gebaut sind. Die Welle endet nicht mehr.

Etappe 12 hat das vorausgesagt: *„Ein Tippfehler in `"aktvi"` erzeugt keinen Fehler, sondern einen Zustand, in dem nichts mehr passt. Etappe 21b löst das ab."* **Heute wird aus diesem stillen Typ 3 ein lauter Typ 1** — mit einem Werkzeug, das die Menge der erlaubten Wörter festschreibt.

**Und dann kommt der Teil, vor dem der Plan seit Etappe 3c warnt.** Deine Trefferrechnung läuft, und sie hat Zahlen: 75, 65, 4, 1. Jede davon ist eine Einladung, daran zu drehen. **Heute darfst du** — aber nicht in deinem Spiel, sondern daneben, auf einem Branch. Und nicht nach Gefühl, sondern als Experiment mit einer Messung.

**Drei Dinge heute, und jedes hat einen Satz:**

| | Wozu |
|---|---|
| **Das `Enum`** | Fehler bei einer festen Menge von Zuständen früh sichtbar machen |
| **Der Branch** | Experimente vom Spiel trennen, das läuft |
| **Das Balancing** | Änderungen messbar und wiederholbar machen |

Alles andere in dieser Portion dient einem der drei.

---

## Die Konzepte — Teil 21b

Heute an einer Ampel — der aus deiner Transferaufgabe in Etappe 13.

### 9. ⭐⭐ Ein `Enum` — die Liste der erlaubten Namen

Deine Ampel hatte in Etappe 13 eine Phase als String: `"rot"`, `"gruen"`, `"gelb"`. So sieht sie mit einem `Enum` aus:

```python
from enum import Enum


class Phase(Enum):
    ROT = "rot"
    GRUEN = "gruen"
    GELB = "gelb"


ampel_phase = Phase.ROT
if ampel_phase == Phase.ROT:
    print("Stehen bleiben.")
```

**Drei Dinge sind neu:**

- **`from enum import Enum`** — dieselbe Gebrauchsanweisung wie `from pathlib import Path` in Etappe 19: Aus dem Werkzeugkasten `enum` wird der Name `Enum` geholt. Die Zeile steht oben, bei deinen anderen `import`-Zeilen.
- **`class Phase(Enum):`** — eine Klasse, die von `Enum` erbt, Vererbung aus Etappe 11. **Aber ihr Körper sieht anders aus als jeder, den du kennst:** Dort stehen keine Methoden, sondern Zuweisungen. **Bei einem `Enum` ist jede Zeile im Klassenkörper ein erlaubter Wert** — ein **Mitglied**. Links der Name, groß geschrieben, weil er sich nie ändert (die Verabredung aus Etappe 1). Rechts ein Wert, dazu gleich mehr.
- **`Phase.ROT`** — so benutzt man ein Mitglied: Klassenname, Punkt, Name. Du erzeugst kein Objekt mit Klammern. Die drei Mitglieder gibt es genau einmal, und jede Zeile, die `Phase.ROT` schreibt, meint dasselbe.

**Und jetzt der Grund für den ganzen Aufwand:**

| Du vertippst dich | Mit Strings | Mit dem `Enum` |
|---|---|---|
| `ampel_phase = "rto"` / `Phase.RTO` | läuft — die Ampel hat jetzt eine vierte Phase, die niemand kennt | `AttributeError` mit dem Namen `RTO` — **in genau der Zeile** |
| `if ampel_phase == "rto":` / `== Phase.RTO` | läuft — die Bedingung ist einfach nie wahr | ebenso |

*(Wie die Meldung genau lautet, hängt an deiner Python-Version — `AttributeError: RTO` oder `… has no attribute 'RTO'`. Beide nennen den falschen Namen.)*

> **Ein `Enum` schreibt fest, welche Wörter es gibt. Ein Wort, das nicht darin steht, existiert nicht — und Python sagt es dir sofort.**

Das ist dieselbe Richtung wie Etappe 20: **aus einem stillen Fehler einen lauten machen.** Dort hast du es mit `assert` selbst getan. Hier tut es die Sprache.

*(Ein Mitglied lässt sich übrigens nicht überschreiben: `Phase.ROT = 5` gibt einen `AttributeError` — je nach Version `cannot reassign member 'ROT'` oder `Cannot reassign members.` Die Zusage „ändert sich nie" hält.)*

### 10. ⭐ Vergleichen — und die stille Falle beim Umbau

```python
print(Phase.ROT == Phase.ROT)      # True
print(Phase.ROT == "rot")          # False — immer, ohne Fehler
```

**Die zweite Zeile ist die, die dich heute erwischen kann.** Ein Mitglied ist **nie** gleich seinem Wert. Kein Fehler, keine Warnung — einfach `False`.

**Warum das beim Umbau gefährlich ist:** Du ziehst deine Zustände von Strings auf ein `Enum` um. An zwanzig Stellen. Vergisst du eine einzige Zeile `if self.status == "tot":`, ist diese Bedingung ab sofort **nie mehr wahr** — ein toter Gegner, der nicht als tot erkannt wird. **Das Werkzeug, das Tippfehler laut macht, macht einen vergessenen Umbau still.** Genau deshalb ist Auftragsschritt 11 eine Fahndung mit Zählen, und genau deshalb gibt es danach eine Suche, die dir beweist, dass du fertig bist.

**Eine zweite Stelle, an der sich etwas ändert, ist die Ausgabe:**

```python
print(Phase.ROT)                   # Phase.ROT
print(f"Phase: {Phase.ROT}")       # Phase: Phase.ROT
print(Phase.ROT.value)             # rot
```

Wo bisher ein Zustand im Text stand, steht nach dem Umbau `Phase.ROT` — es sei denn, du fragst mit **`.value`** nach dem Wert rechts vom Gleichheitszeichen.

**Und eine Prüfung, die sagt, ob ein Wert überhaupt ein Mitglied ist:**

```python
print(type(ampel_phase) == Phase)  # True
print(type("rot") == Phase)        # False
```

`type()` kennst du seit Etappe 1 — es sagt, von welcher Sorte ein Wert ist. **Neu ist nur, das Ergebnis mit einem Klassennamen zu vergleichen.** In einer `assert`-Zeile wird daraus eine Invariante: *Jeder Zustand ist ein Mitglied, kein String.* *(Die Form taugt hier, weil ein `Enum` keine Unterklassen hat. Bei deinen Marines taugt sie nicht: `type()` eines Soldaten ist `Soldat`, nicht `Marine`. Python hat für solche Fragen ein eigenes Werkzeug; dieser Plan braucht es nicht.)*

👀 **In fremdem Code wirst du `is` sehen:** `if ampel_phase is Phase.ROT:`. Weil es jedes Mitglied genau einmal gibt, ist `is` hier dasselbe wie `==`. Dieses Tutorial bleibt bei `==`.

👀 **Und `.name`:** `Phase.ROT.name` ist der Text `"ROT"` — der Name links vom Gleichheitszeichen. Du brauchst ihn heute nicht; manche Programme speichern ihn statt des Werts.

### 11. Hin und zurück — ein `Enum` im Spielstand

JSON kennt sechs Dinge, Etappe 19, Konzept 5. **Ein `Enum` ist keines davon:**

```
TypeError: Object of type Phase is not JSON serializable
```

— dieselbe Meldung wie beim Set, und sie kommt erst bei `json.dump`, nicht vorher. **Also übersetzt du an der Grenze**, genau wie beim Set:

```python
daten = {"phase": ampel_phase.value}       # Hinweg: das Mitglied wird Text
ampel_phase = Phase(daten["phase"])        # Rückweg: der Text wird ein Mitglied
```

**`Phase("rot")` sucht das Mitglied mit diesem Wert** und liefert `Phase.ROT`. Gibt es keines:

```
ValueError: 'rto' is not a valid Phase
```

**Und jetzt der Grund, warum die Werte rechts Texte sind und keine Zahlen.** Das `Enum` aus dem Lehrplan hat `1`, `2`, `3` — das geht auch. Aber sieh dir an, was mit deinem Spielstand passiert:

| Werte im `Enum` | Was im Spielstand steht | Alte Spielstände |
|---|---|---|
| `AKTIV = "aktiv"`, `TOT = "tot"` | `"aktiv"`, `"tot"` — **genau wie bisher** | laden weiter |
| `AKTIV = 1`, `TOT = 2` | `1`, `2` | brechen mit `ValueError` |

**Mit den alten Wörtern als Werten ändert sich an deiner Datei nichts.** Der Umbau passiert komplett in deinem Programm; der Spielstand merkt ihn nicht. Das ist die Regel aus Etappe 19 in einer neuen Form: **Das Programm darf sich ändern. Die Datei, die schon auf der Festplatte liegt, soll es nicht müssen.**

⚠️ **Und eine Stelle, an der das `Enum` dir sogar hilft:** Stand bisher in einem Spielstand `"status": "untot"`, hat `aus_daten()` das klaglos übernommen — ein Zustand, den niemand kennt, ein stiller Typ 3 **Züge später**. Mit `Zustand(...)` knallt es **beim Laden**, in der Zeile, die das Wort liest. Das ist ein Stück der Prüfung an der Grenze, die Etappe 25 vollständig baut.

### 12. ⭐ Wann lohnt ein `Enum` — und wann nicht?

**Ein `Enum` ist nicht automatisch besser als ein String**, und der Reflex *„Strings sind schlecht"* wäre die falsche Lehre aus diesem Abschnitt. Es lohnt sich unter **zwei** Bedingungen, und beide müssen gelten:

1. **Die Menge der Werte ist abgeschlossen.** Es gibt genau diese und keine weiteren — und das bleibt so, solange das Programm lebt.
2. **Ein Tippfehler soll knallen, statt durchzurutschen.**

**Die erste Bedingung ist die, an der die meisten Kandidaten scheitern.** Eine Ampel hat drei Phasen, heute und in zehn Jahren. Die Gegnertypen deines Spiels dagegen sind **Inhalt**: Heute drei, nächste Woche vier, und in Etappe 25 kommen sie aus einer Datei, die jemand anderes schreibt. Ein `Enum` dafür müsstest du bei jedem neuen Gegner im Code erweitern — und beim Laden jedes Wort aus der Datei zurückübersetzen.

**Die Kandidaten aus deinem Spiel:**

| Wörter | Abgeschlossen? | Und außerdem | Urteil |
|---|---|---|---|
| **Zustand einer Einheit** — `"aktiv"`, `"tot"` | ja — eine Einheit lebt oder nicht | an vielen Stellen verglichen — du zählst sie in Schritt 11 | **heute** |
| **Trefferart** — `"treffer"`, `"verfehlt"` … | ja — die Rechnung kennt genau diese | frisch gebaut, wenige Stellen | würde passen — Kür |
| **Gegnertypen** | nein — Inhalt, wächst | kommen in 25 aus JSON | String |
| **Effekt-Wörter** — `"veraetzt"` … | nein — Inhalt, eine Tabelle | `EFFEKTE` ist die eine Quelle | String |
| **Flag-Wörter** — `"schwachpunkt_kriecher"` … | nein — Inhalt | die Prüfung gibt es schon | String |
| **Befehlswörter** — `"feuern"`, `"kaufe"` … | ja, eigentlich | kommen als Text von `input()` und werden sofort verzweigt | String — bis 23a |

**Die Flag-Wörter verdienen einen zweiten Blick**, weil zwei frühere Etappen hierher verwiesen haben: Etappe 16 wollte *„ein `Enum` gegen Verweise ins Leere"*, Etappe 18 *„kein `Enum` für Flag-Wörter — Etappe 21b"*. **Die Entscheidung: Sie bleiben Strings.** Nicht aus Bequemlichkeit, sondern weil der Schutz, den ein `Enum` hier bringen würde, schon da ist: **`pruefe_tabellen()` aus Etappe 20c** findet jeden Verweis ins Leere beim Start. Ein `Enum` wäre eine zweite Buchführung über dieselben Wörter — und eine, die in Etappe 25 beim Laden aus JSON wieder abgebaut werden müsste.

**Und „abgeschlossen" ist selbst eine Entscheidung, keine Naturtatsache.** Eine Einheit könnte auch *verwundet*, *bewusstlos* oder *zurückgezogen* sein. Dein Spiel hat das anders gelöst: Alles, was vorübergeht, ist seit Etappe 18 ein **Effekt** mit Dauer in `effekte` — erschüttert, verätzt. **Der Zustand beantwortet nur die eine Frage, ob eine Einheit mitspielt.** Solange das so bleibt, bleibt die Menge abgeschlossen. Käme ein dritter Zustand dazu, wäre das eine Zeile im `Enum` und eine Fahndung wie in Schritt 11 — bewusst, nicht nebenbei.

> **Ein `Enum` ist eine Zusage darüber, dass sich die Liste nicht ändert. Mach sie nur dort, wo du sie halten willst.**

### 13. 👀 Schadenstypen und Widerstände

**Nur erkennen, kein Auftrag.** Eine Idee, die in vielen Spielen steckt: Jede Waffe richtet eine **Sorte** Schaden an, und jeder Gegner hält verschiedene Sorten verschieden gut aus.

| | gegen Chitin | gegen Panzerplatten |
|---|---|---|
| **Plasma** | × 1,5 | × 0,5 |
| **Panzerbrecher** | × 0,5 | × 1,5 |

**Technisch ist das ein Dictionary aus Faktoren** — die Umkehrtabelle aus Etappe 15, eine Ebene tiefer. Und du hast die Vorstufe schon gebaut: **Dein Zuschlag aus Etappe 15b** ist genau so eine Zeile, *„diese Erkenntnis macht gegen diesen Typ mehr Schaden"*. Mit Schadenstypen würde aus der Waffenwahl eine Entscheidung statt einer Zahl.

**Reizvoll, und heute nicht.** Es wäre der vierte Eingang in eine Rechnung, die gerade mit dreien stabil läuft. Und es lässt sich in Etappe 25 bequemer als **Daten** nachrüsten als heute als Code. *(Wer es trotzdem will: „Wenn du mehr willst".)*

### 14. ⭐ Ein Branch — ein Versuch, den man wegwerfen darf

Bis heute hatte dein Repo **eine** Linie von Commits. Jeder neue setzte auf den letzten, und `git log --oneline` zeigte sie untereinander.

**Ein Branch ist eine zweite Linie**, die an einem Commit abzweigt. Auf ihr kannst du committen, so viel du willst — die erste Linie merkt davon nichts. Gefällt dir das Ergebnis nicht, wechselst du zurück, und alles ist, wie es war.

```
git status                   # sauber? Das ist die Bedingung für alles Weitere
git branch                   # zeigt die Branches, der aktuelle mit *
git checkout -b versuch      # legt den Branch "versuch" an UND wechselt hinein
```

**`git branch`** listet deine Branches. Bis heute steht dort genau einer, mit einem Stern davor — **dein Hauptzweig, `main` oder `master`**, je nachdem, wie dein Git eingestellt ist. Merk dir den Namen; du brauchst ihn zum Zurückwechseln.

**`git checkout -b versuch`** macht zwei Dinge auf einmal: Es legt den neuen Branch an, genau am aktuellen Commit, und wechselt hinein. Ab jetzt landet jeder Commit auf `versuch`.

**Zurück geht es mit dem Befehl aus Etappe 16:** `git checkout main` (oder `master`). Dort hast du bisher einen alten Commit angesehen — heute wechselst du damit zwischen zwei Linien. **Nach dem Wechsel sieht deine Datei aus wie auf der Linie, auf der du jetzt stehst.** Wechselst du zurück zu `versuch`, sind deine Versuche wieder da.

⚠️ **Die eine Regel, an der Anfänger mit Branches scheitern:**

> **Was nicht committet ist, gehört keinem Branch.**

Was dann beim Wechsel passiert, hängt an der Datei:

- **Sieht die Datei auf beiden Branches gleich aus**, nimmt Git deine Änderung einfach mit. Hast du direkt nach `git checkout -b versuch` eine Zahl geändert, **ohne** zu committen, und wechselst zurück, steht die Änderung jetzt auf dem Hauptzweig in deiner Datei. Committest du dort, landet sie genau da, wo sie nie hin sollte.
- **Unterscheidet sich die Datei zwischen den Branches**, weil auf einem schon ein Commit liegt, würde der Wechsel deine Änderung überschreiben — und Git weigert sich:

```
error: Your local changes to the following files would be overwritten by checkout:
	spiel.py
Please commit your changes or stash them before you switch branches.
Aborting
```

**Beides vermeidest du mit einer Gewohnheit: vor jedem Wechsel `git status`.** Steht dort eine geänderte Datei, erst committen — auf dem Branch, auf dem du gerade bist — oder die Änderung von Hand zurücknehmen. *(Dateien, die Git noch nie gesehen hat — eine Ausgabedatei etwa —, stehen dort unter „Untracked files". Sie stören den Wechsel nicht, aber sie gehören nicht in einen Commit. Lösch sie, wenn du sie nicht mehr brauchst.)*

⚠️ **Und `git push` auf einem neuen Branch** endet mit `fatal: The current branch versuch has no upstream branch.` Das ist kein Fehler in deinem Repo: Der Branch existiert nur bei dir. **Heute lässt du ihn dort.** Hochladen, zusammenführen und wegwerfen sind Etappe 24.

👀 **In neueren Anleitungen steht statt `checkout` oft `git switch`** — `git switch -c versuch` zum Anlegen, `git switch main` zum Wechseln. Dasselbe, nur mit einem Befehl, der nichts anderes kann. Dieses Tutorial bleibt bei `checkout`, das du seit 16 kennst.

### 15. ⭐ Balancing ist ein Experiment

**Die Falle, vor der der Plan seit Etappe 3c warnt:** Du spielst eine Welle, sie fühlt sich zu leicht an, du drehst an drei Zahlen, spielst noch eine, sie fühlt sich zu schwer an, du drehst an zwei anderen. Nach zwei Stunden hast du ein Spiel, das sich anders anfühlt, und weißt nicht, warum.

**Das ist kein Balancing. Das ist Würfeln mit dem eigenen Spiel.** Der Ausweg besteht aus vier Regeln, und alle vier kennst du einzeln schon:

| Regel | Warum | Seit |
|---|---|---|
| **Eine Stellschraube pro Versuch** | Änderst du zwei, weißt du nicht, welche gewirkt hat | Etappe 16 — *eine Sache auf einmal ändern* |
| **Fester Seed, dieselbe Befehlsdatei** | Nur dann ist der Unterschied deine Änderung und nicht der Zufall | Etappe 17b |
| **Eine Messzahl, vorher festgelegt** | Was du nicht messen kannst, kannst du nicht balancieren | Etappe 16 — *wann hätte ich es gemerkt?* |
| **Fünfzehn Minuten** | Dann aufschreiben und aufhören, egal wie nah es sich anfühlt | Etappe 3c |

**Ein Seed ist eine Stichprobe von eins.** Mit einem Seed kann eine Änderung zufällig gut aussehen. Nimm **drei** Seeds, vorher und nachher — dieselben drei.

**Und die Prüffrage aus Etappe 13, die an jede Stellschraube gehört:**

> **Ist eine Strafe versehentlich eine Belohnung?**

Ein Fehlschuss, der keine Munition kostet. Ein Rücksetzpunkt, der nach dem Spielende mehr zurückgibt, als verloren ging. Eine Fähigkeit, die gegen Panzerung so gut wirkt, dass Schießen sinnlos wird. **Solche Fehler fühlt man beim Spielen nicht — man sieht sie nur an den Zahlen.**

**Die Stellschrauben deines Spiels** — alle aus früheren Etappen, alle mit dem Vermerk *„Startwert, keine Empfehlung"*:

| Stellschraube | Seit | Worauf sie wirkt |
|---|---|---|
| Trefferchance je Klasse, Panzerung je Typ | 21a | Munitionsverbrauch, Dauer einer Welle |
| Munitionspreis, Preis der schweren Munition | 5, 18c | der Kreislauf Brut → Material → Vaporium → Munition |
| Stufenschwellen | 5 | wann Skillpunkte kommen |
| Abklingzeiten | 13, 18c | wie oft Fähigkeiten den Kampf entscheiden |
| Trefferpunkte je Gegnertyp | 11b | alles |
| Magazingröße — vielleicht je Klasse | 2, 13 | Nachladen als Entscheidung |
| Größe der Zonen | 14b, 15 | wer kämpft, was eingesammelt wird |
| Tempo der Gegner — ein Feld pro Tick, oder seltener | 14a | wie viel Zeit bis zum Tor bleibt |
| Preis und Trefferpunkte der Barrikade — wenn du die Kür aus 14c gebaut hast | 14c | ob sich Stellung lohnt |
| Wellenbudget | 17a | wie viele und welche Gegner kommen |
| Was beim Spielende übrig bleibt | 19c | wie viel ein Rücksetzpunkt verzeiht |

**Heute drehst du an genau einer.**

---

## Dein Auftrag — Teil 21b

---

### 9. Füll die Kandidatentabelle aus

In `GELERNT.md`: die Tabelle aus Konzept 12, **mit deinen eigenen Wörtern.** Hast du Zustände oder Wörter, die dort nicht stehen — eine Kür, einen Befehl, den du dazugebaut hast —, kommen sie dazu.

- Für jede Zeile: abgeschlossen oder nicht? Und dein Urteil.
- **Gebaut wird heute genau eines: die Zustände deiner Einheiten.** Alles andere bleibt, wie es ist.

---

### 10. Leg das `Enum` an

- **`from enum import Enum`** zu deinen anderen `import`-Zeilen, ganz oben.
- **Eine Klasse `Zustand`**, die von `Enum` erbt, mit zwei Mitgliedern: `AKTIV` mit dem Wert `"aktiv"`, `TOT` mit dem Wert `"tot"`. *(Die alten Wörter als Werte — Konzept 11 sagt, warum.)*
- **Wohin:** zu deinen festen Werten, über deine erste Klasse. `Einheit.__init__` wird das `Enum` gleich benutzen, und die Klasse muss gelaufen sein, bevor die erste Einheit entsteht — dieselbe Regel wie für `def` seit Etappe 7a. Oben bei den festen Werten ist das garantiert.

**So prüfst du es:** In der Probedatei `print(Zustand.TOT.value)` und `print(Zustand("aktiv"))`. Du erwartest `tot` und `Zustand.AKTIV`.

---

### 11. ⭐⭐ Zieh die Zustände um

**Zuerst zwei Sicherungen.** Der Beweis, wie in Schritt 4: fester Seed, `python spiel.py < befehle17.txt > vorher.txt`. Das ist ein **reiner Umbau** — der Spieler darf nichts merken. **Und eine Kopie deines Spielstands** aus `saves/`, wie in 20a, Schritt 4 — du brauchst sie in Schritt 12.

**Dann die Fahndung**, zum wievielten Mal seit Etappe 5 — du zählst sie selbst:

- **Such nach `"aktiv"` und nach `"tot"`, beide mit Anführungszeichen**, und schreib die Zahl der Treffer auf, **bevor** du etwas änderst.
- **Jede Zuweisung** wird ein Mitglied: `Zustand.AKTIV` oder `Zustand.TOT`.
- **Jeder Vergleich** vergleicht mit einem Mitglied. Konzept 10, erste Hälfte — ein vergessener ist kein Fehler, sondern ein Typ 3.
- **Jede Ausgabe**, in der ein Zustand im Text steht, bekommt `.value`. Konzept 10, zweite Hälfte.
- **`als_daten()` und `aus_daten()` fasst du noch nicht an.** Das ist Schritt 12 — und bis dahin kannst du weder speichern noch laden: Das eine scheitert an JSON, das andere an deiner neuen Behauptung. Konzept 11. **Also bis Schritt 12 kein `speichern` und kein `beenden`** — ein abgebrochenes Speichern hinterlässt eine halb geschriebene Datei, die Etappe 19 kennt.

⚠️ **Deine Meldungstexte bleiben.** *„Vasquez ist tot."* ist kein Zustand, sondern ein Satz. Die Suche mit Anführungszeichen findet nur das alleinstehende Wort — und genau das willst du.

**Und eine Zeile mehr in `pruefe_zustand(welt)`:** Der Zustand jeder Einheit ist ein Mitglied von `Zustand` — die Prüfung mit `type()` aus Konzept 10.

**So prüfst du es — dreimal:**

1. **Die Suche nach `"aktiv"` und `"tot"` findet genau zwei Stellen: die zwei Werte in deinem `Enum`.** Vergleich mit der Zahl, die du vorher aufgeschrieben hast. *(Findet sie mehr, hast du eine Stelle übersehen — und jede übersehene ist ein Typ 3.)*
2. **`diff vorher.txt nachher.txt`: kein Unterschied.** Redet es, steht in der Ausgabe irgendwo `Zustand.TOT` — eine Ausgabe ohne `.value`.
3. **Eine ganze Welle ohne knallende Behauptung** — und die Welle endet.

---

### 12. ⭐ Übersetz den Spielstand

Die Stelle, die Etappe 19 angekündigt hat: *„Dann steht in deinem Spielstand ein Text und in deinem Programm etwas anderes."*

- **In `als_daten()`:** Der Zustand geht als `.value` ins Dictionary.
- **In `aus_daten()`:** Der Text wird mit `Zustand(...)` zum Mitglied.
- **In deiner Zustandsinventur aus 19a:** Die Zeile für den Zustand bekommt einen Vermerk — *wird beim Speichern übersetzt*, wie die Sets.

**Und eine Entscheidung, die aus Etappe 20 kommt:** Ein Spielstand mit `"status": "untot"` knallt ab heute beim Laden, mit `ValueError` — Konzept 11. In 20a, Schritt 4, hast du gewählt, ob ein kaputter Spielstand mit `KeyError` gefangen wird oder abstürzt. **Gehört `ValueError` dazu?** Entscheide nach denselben Gründen wie damals, und schreib einen Satz dazu in `GELERNT.md`. *(Fängst du ihn, dann eng — nach Konzept 3 aus 20a.)*

**So prüfst du es:**

- **Deine Kopie aus Schritt 11 lädt** — ein Spielstand von vor dem Umbau. Konzept 11, erste Zeile der Tabelle.
- **Speicher, kopier die Datei, lade, speicher noch einmal**, und vergleich Kopie und neue Datei mit `diff`. **Genau ein Unterschied: der Seed** — seit 19c zieht jedes Speichern einen neuen. Und schau hinein: **Dort steht `"tot"` oder `"aktiv"`, nicht `Zustand.TOT`.**

---

### 13. Gib dem Wellenende eine Messzeile, und commit

Für Schritt 14 brauchst du eine Zahl, die du vergleichen kannst. **Leg sie fest, bevor du an irgendetwas drehst** — Konzept 15, dritte Regel.

- **Am Ende jeder Welle eine Zeile über `welt.debug()`** aus 20c, mit drei Zahlen: die Nummer der Welle, **wie viele Ticks sie gedauert hat**, und `welt.kern_integritaet`.
- **Die Dauer steht nirgends** — `welt.zeit` zählt seit Spielbeginn. Merk dir bei Wellenbeginn `welt.zeit` in einem Attribut der Welt und zieh es am Ende ab: *merken, neu berechnen, vergleichen* aus Etappe 13, Konzept 4.

*(Mehr brauchst du heute nicht. Willst du zusätzlich Schüsse und Treffer zählen: zwei Zähler an der Welt, erhöht in `schiesse()`, zurückgesetzt bei Wellenbeginn.)*

**So prüfst du es:** `DEBUG` auf `True`, eine Welle spielen — am Ende steht deine Messzeile.

- Der Beweislauf aus 17b schweigt wie immer, der aus 19c zeigt den einen Unterschied.
- Die Abschnitte am Ende, die zum `Enum` gehören: **die Leseübung** und **Kaputtmachen 6 bis 9**.

Commit **auf deinem Hauptzweig**: `Etappe 21b: Zustände als Enum`

---

### 14. ⭐ Mach genau ein Balancing-Experiment — auf einem Branch

**Auf deinem Hauptzweig — Vorbereitung und Ausgangsmessung:**

1. **Wähl eine Stellschraube** aus der Tabelle in Konzept 15 — oder aus der mittleren Spalte deiner Zettel aus Schritt 1. **Genau eine.**
2. **Schreib in `GELERNT.md`, was du erwartest**, bevor du etwas änderst: *Wenn ich die Panzerung der Panzerbrut von 4 auf 6 setze, verliert der Kern in späten Wellen mehr.* Eine Vorhersage, keine Hoffnung. **Und leg dabei fest, welche Zahl der Messzeile deine Messzahl ist** — Konzept 15, dritte Regel. Die anderen notierst du mit, aber sie entscheiden nichts. Sonst dauert eine Welle länger und kostet weniger, und du weißt nicht, ob das gut ist.
3. **Miss den Ausgangszustand.** Drei Seeds deiner Wahl. Für jeden: `SEED` darauf setzen, dann `python spiel.py < befehle17.txt > messung.txt`, und in `messung.txt` die Messzeilen ansehen. **Entscheide dich für eine Wellennummer, die in allen drei Läufen eine Messzeile hat**, und trag diese drei Zeilen in eine Tabelle in `GELERNT.md` ein.
4. **Aufräumen und sichern:** `SEED` zurück auf deinen alten Wert, `messung.txt` löschen. Commit: `Balancing-Versuch 1: Vorhersage und Ausgangsmessung`.

**Auf dem Branch — der Versuch:**

5. `git status` — keine geänderte Datei. `git branch` — schreib auf, wie dein Hauptzweig heißt. Dann `git checkout -b balancing`.
6. **Dreh an der einen Zahl.** Miss mit denselben drei Seeds und derselben Wellennummer noch einmal. **Die drei neuen Zeilen notierst du auf einem Zettel**, nicht in `GELERNT.md` — was du auf dem Branch in `GELERNT.md` schreibst, wäre nach dem Wechsel zurück nicht mehr da. *(Kommt die Welle in einem Lauf gar nicht mehr zu Ende, ist das selbst ein Messergebnis. Schreib es auf.)*
7. **Aufräumen:** `SEED` zurück, `messung.txt` löschen. `git status` zeigt jetzt genau eine geänderte Datei, `spiel.py`, mit genau einer geänderten Zahl. Commit auf `balancing`, die Nachricht nennt Stellschraube, alten und neuen Wert: `Balancing: Panzerung Panzerbrut 4 -> 6`.

**Fünfzehn Minuten für die Schritte 6 und 7.** Dann ist Schluss, auch wenn du gerade eine Idee hast — sie kommt auf den Zettel und ist der nächste Versuch an einem anderen Abend.

**Zurück auf den Hauptzweig:**

8. `git status` — sauber? Dann `git checkout` mit dem Namen deines Hauptzweigs.
9. **Sieh nach:** Die Zahl in `spiel.py` steht wieder auf dem alten Wert. `git log --oneline` zeigt deinen Balancing-Commit **nicht**. Wechsel einmal zu `balancing` — die Zahl ist wieder die neue. Und zurück.
10. **Übertrag den Zettel** in deine Tabelle in `GELERNT.md` und schreib zwei Sätze darunter: Was ist passiert, und hat es dich überrascht? **Und sieh auf die drei Seeds einzeln:** Zeigen sie alle in dieselbe Richtung? Wenn nicht, hättest du mit nur einem je nach Seed das Gegenteil geschlossen — der Grund für die zweite Regel aus Konzept 15. Commit: `Balancing-Versuch 1: Ergebnis`.

⚠️ **Der Branch bleibt, wie er ist.** Nicht zusammenführen, nicht löschen, nicht hochladen. In Etappe 24 ist er das Übungsobjekt — dort entscheidest du, ob seine Zahl in dein Spiel kommt.

**So prüfst du es:** Auf deinem Hauptzweig läuft das Spiel mit den Zahlen aus 21a. `git branch` zeigt zwei Branches, der Stern steht beim Hauptzweig. **Und in `GELERNT.md` stehen eine Vorhersage, sechs Messzeilen und zwei Sätze.**

---

## Selbsttest — 21b

- [ ] Die Suche nach `"aktiv"` und `"tot"` mit Anführungszeichen findet nur noch die zwei Werte im `Enum`.
- [ ] `pruefe_zustand()` prüft, dass jeder Zustand ein Mitglied von `Zustand` ist.
- [ ] Der Beweislauf nach dem Umbau zeigt keinen Unterschied — nirgends steht `Zustand.` in der Ausgabe.
- [ ] Ein alter Spielstand lädt; im neuen steht weiterhin `"tot"` als Text.
- [ ] Ein Spielstand mit einem unbekannten Zustand knallt beim Laden — oder wird so behandelt, wie du es in Schritt 12 entschieden hast.
- [ ] Am Ende jeder Welle steht deine Messzeile, wenn `DEBUG` an ist.
- [ ] `git branch` zeigt zwei Branches; auf dem Hauptzweig steht nichts vom Experiment.
- [ ] Auf dem Hauptzweig, in `GELERNT.md`: die Kandidatentabelle, eine Vorhersage, sechs Messzeilen, zwei Sätze.

---

## Was NICHT in diese Etappe gehört

**Keine kritischen Treffer.** Drei Dinge, nicht acht. Eine vierte Trefferart wäre die Kür unten.

**Keine Trefferchance, die von der Entfernung abhängt.** Die Reichweite entscheidet, *ob* geschossen wird — Konzept 1. Wer sie auch noch in die Chance rechnet, hat einen fünften Eingang. Kür.

**Keine Trefferchance für Gegner, kein Würfeln bei Fähigkeiten, keine Panzerung gegen Säure.** Konzept 1, drei Regeln dieses Spiels.

**Keine eigene Formel je Marine-Klasse.** Vier Klassen, **eine** Formel, vier Sätze Zahlen. Ob diese Zahlen eigentlich Daten sind und in eine Tabelle gehören, ist die Frage von Etappe 22.

**Kein zweites `Enum`** — außer als Kür für die Trefferart. Keine `Enum` für Gegnertypen, Effekt-, Flag- oder Befehlswörter: Konzept 12.

**Keine Schadenstypen im Auftrag.** Konzept 13 ist 👀.

**Kein Balancing auf dem Hauptzweig**, und keine zweite Stellschraube im selben Versuch.

**Kein Zusammenführen, Löschen oder Hochladen des Branches.** Etappe 24.

---

## Lernziele

**Zu 21a:**

1. **Warum gibt `berechne_treffer()` zwei Werte zurück statt zweimal einen — und was ginge schief, wenn es zwei Funktionen wären?** ← die wichtigste
2. Was kommt bei `return a, b` tatsächlich zurück, und was passiert, wenn du es in **einen** Namen steckst?
3. Warum wird der Wurf außerhalb von `berechne_treffer()` gewürfelt?
4. Warum ist eine Panzerung, die abzieht, anders zu balancieren als eine, die einen Anteil nimmt?
5. Was setzt `max(0, x)` — eine Unter- oder eine Obergrenze?
6. Wozu schreibst du beim Aufruf die Namen der Parameter dazu?
7. Welche zwei Fragen beantwortet ein Schuss, und welche davon beantwortet die Trefferrechnung?
8. Woher weiß die Trefferrechnung von Standfest und Zielhilfe, obwohl sie keine Fähigkeit abfragt?

**Zu 21b:**

9. Was passiert bei einem Tippfehler im Namen eines Mitglieds — und was bei einem Tippfehler in einem String?
10. Warum ist `Zustand.TOT == "tot"` gefährlich, obwohl es nie abstürzt?
11. Warum sind die Werte in deinem `Enum` die alten Wörter und keine Zahlen?
12. Unter welchen zwei Bedingungen lohnt ein `Enum` — und warum bleiben die Flag-Wörter Strings?
13. Was passiert mit einer Änderung, die du nicht committet hast, wenn du den Branch wechselst?
14. Warum reicht **ein** Seed nicht, um zu entscheiden, ob eine Änderung besser ist?

---

## 🧠 Die Entwicklerfrage — zu 21b

> **Welche Werte gehören wirklich zum Kampfsystem?**

Die Trefferchance steht bei dir seit heute am **Schützen**. Sie könnte auch der **Waffe** gehören — deine `Item`-Klasse aus Etappe 11c kennt Waffen. Oder der **Entfernung**: Ein Schuss auf ein Feld ist sicherer als einer über fünf.

**Wo du sie hinschreibst, entscheidet darüber, was du später noch verändern kannst.** Gehört sie dem Schützen, trifft ein Medic mit jedem Gewehr gleich. Gehört sie der Waffe, trifft jeder mit demselben Gewehr gleich. Gehört sie der Entfernung, ist Stellung plötzlich wichtiger als Klasse.

Zwei bis fünf Sätze in `GELERNT.md`. In Etappe 22 kommt die Frage zurück, wenn deine Zahlen in Tabellen wandern — und dort heißt sie: *Was davon ist Daten, was ist Verhalten?*

---

## Transferaufgabe (15 Minuten) — zu 21a

**Außerhalb des Spiels**, in einer Wegwerf-Datei. Ein Parkhaus:

- Eine Funktion **`berechne_gebuehr(minuten, rabatt)`** gibt **zwei Werte** zurück: den Betrag in Cent und den Tarif als Text.
- Die ersten 15 Minuten sind frei — Tarif `"kostenlos"`, Betrag `0`.
- Ab der 16. Minute kostet jede angefangene halbe Stunde der **gesamten** Parkzeit 150 Cent — Tarif `"normal"`. 40 Minuten sind also zwei halbe Stunden. *(Angefangen: Etappe 3c, `//` und ein Schritt mehr.)*
- Ein Rabatt in Cent wird abgezogen, aber **der Betrag fällt nie unter 100 Cent**, sobald nicht kostenlos geparkt wurde. Greift diese Untergrenze, ist der Tarif `"mindestgebuehr"`.
- **Kein `print` in der Funktion.**

**Dann `pruefe_gebuehr()`** mit mindestens drei `assert`-Zeilen, jede mit Schlüsselwortargumenten. Mindestens eine davon prüft einen Rand: genau 15 Minuten, genau 16.

**Und die eigentliche Frage:** Welche deiner drei Behauptungen hätte einen Fehler gefunden, den die anderen beiden übersehen? Wenn keine — schreib eine vierte.

---

## Leseübung — Stufe 3 (15 Minuten) — zu 21b

**Nicht ausführen.** Lesen, beantworten.

```python
from enum import Enum


class Lage(Enum):
    BEREIT = "bereit"
    HEIZT = "heizt"
    STOERUNG = "stoerung"


class Kaffeemaschine:
    def __init__(self):
        self.lage = Lage.HEIZT
        self.temperatur = 20
        self.tassen = 0

    def takt(self):
        if self.lage == Lage.HEIZT:
            self.temperatur += 30
            if self.temperatur >= 90:
                self.lage = Lage.BEREIT

    def bruehe(self, anzahl):
        if self.lage != Lage.BEREIT:
            return 0, f"Maschine ist {self.lage.value}"
        if anzahl > 4:
            self.lage = Lage.STOERUNG
            return 0, "zu viele Tassen auf einmal"
        self.tassen += anzahl
        return anzahl, "gebrüht"

    def ist_gestoert(self):
        return self.lage == "stoerung"

    def als_daten(self):
        return {"lage": self.lage.value, "temperatur": self.temperatur, "tassen": self.tassen}

    def aus_daten(self, daten):
        self.lage = Lage(daten["lage"])
        self.temperatur = daten["temperatur"]
        self.tassen = daten["tassen"]


m = Kaffeemaschine()
for i in range(3):
    m.takt()
anzahl, grund = m.bruehe(6)
print(grund, m.ist_gestoert())
print(m.als_daten())
```

**Die fünf Fragen**, für `bruehe` und für `aus_daten`:

1. Was kommt rein?
2. Was passiert?
3. Was verändert sich — und woran?
4. Was kommt raus?
5. Welche anderen Objekte oder Funktionen werden dabei aufgerufen?

**Und die Leitfrage von Stufe 3 — warum ist es so gebaut, und was kostet es?**

6. Welche Temperatur hat die Maschine nach den drei Takten, und in welcher Lage ist sie?
7. **Was druckt die vorletzte Zeile?** Beide Werte. *(Lies `ist_gestoert` Zeile für Zeile. Ganz genau.)* **Warum sieht `ist_gestoert` für einen Menschen richtig aus und ist für Python falsch?** Welche Sorte Fehler ist das?
8. Was druckt die letzte Zeile?
9. Jemand lädt eine Datei mit `"lage": "Heizt"`. Was passiert, und in welcher Zeile?
10. `bruehe` gibt bei einer Störung `0` zurück — und auch, wenn die Maschine noch heizt. **Woran erkennt der Aufrufer den Unterschied?** Was würde fehlen, wenn `bruehe` nur die Zahl zurückgäbe?
11. Die Maschine hat drei Lagen. Würdest du daraus ein `Enum` machen? Prüf beide Bedingungen aus Konzept 12.

---

## Kaputtmachen

Jedes Experiment nach dem Ritual: **erst aufschreiben, was passieren wird**, dann ausführen, vergleichen, erklären. Danach wieder reparieren.

**Pflicht:** 1, 3, 6 und 10. Die übrigen, wenn du Zeit hast.

### Zu 21a

**1. ⭐⭐ Nimm die Untergrenze weg — in zwei Stufen.** Vorher: Nimm die Behauptung aus `pruefe_trefferrechnung()` heraus, die einen Schuss mit zu wenig Schaden prüft, sonst verrät sie alles beim Start. **Stufe A:** In `berechne_treffer()` kein `max()`, kein `if` — nur Schaden minus Panzerung. Lass einen erschütterten Kameraden auf eine Panzerbrut schießen *(oder ruf in der Probedatei `schiesse()` mit Schaden 3 auf)*. **Was passiert mit ihren Trefferpunkten — und welche Zeile deines Programms hat den Fehler verdeckt?** **Stufe B:** Nimm zusätzlich in `schiesse()` die Bedingung weg, dass nur bei Schaden über `0` getroffen wird. Noch einmal. **Jetzt?** *(Das ist der Klassiker unter den stillen Fehlern. Dass er in Stufe B trotzdem knallt, verdankst du einer Zeile aus Schritt 3 — ohne sie wäre es ein Typ 3. Danach alles zurück.)*

**2. Pack mit einem Namen aus.** In `schiesse()`: `schaden = berechne_treffer(...)` statt zwei Namen. Einen Schuss abgeben. **Wo knallt es, mit welcher Meldung — und in welcher Zeile steht der eigentliche Fehler?** Wie weit liegen die beiden auseinander? *(Konzept 3, erste Zeile der Tabelle. In `schiesse()` ist es eine Zeile, weil gleich danach verglichen wird. Stünde der Vergleich woanders, wären es viele.)*

**3. ⭐ Vertausch zwei Argumente.** In `schiesse()`: Rufe `berechne_treffer()` **ohne** Namen auf und tausch Panzerung und Trefferchance. Spiel eine Welle. **Was siehst du — und woran würdest du es merken, wenn du nicht wüsstest, was du getan hast?** Dann denselben vertauschten Aufruf mit Namen. **Was ändert sich?** *(Konzept 7. Und: Hat `pruefe_trefferrechnung()` etwas gemerkt? Warum nicht?)*

**4. Mach aus `<=` ein `<`.** Im Vergleich aus Konzept 5. Zähl zehntausend Würfe bei `75`. **Findest du den Unterschied an der Zahl?** Dann mit Treffsicherheit `100`. **Welche deiner Behauptungen hätte es gefunden — oder keine?**

**5. Würfel im reinen Umbau.** Kopier `spiel.py` als Probedatei und setz dort den Stand von Schritt 5 her: alle Trefferchancen auf `100`, alle Panzerungen auf `0`, `wurf = 1`. Fester Seed, `befehle17.txt`, Ausgabe in `probe_a.txt`. Dann nur `wurf = 1` gegen `random.randint(1, 100)` tauschen — kein Schuss kann danebengehen —, Ausgabe in `probe_b.txt`, `diff`. **Schweigt es?** Wenn nicht: Was hat sich geändert, obwohl jeder Schuss trifft? *(Etappe 17b, Konzept 11: Jeder Zufallsaufruf verbraucht die nächste Zahl der Folge. Danach Probedatei und beide Ausgaben löschen.)*

### Zu 21b

**6. ⭐⭐ Lass ein `"tot"` stehen.** Setz nach dem Umbau an **einer** Stelle den alten Vergleich zurück — in der Aufräumphase, dort, wo gefallene Gegner gesammelt werden. Spiel eine Welle. **Was passiert mit den Gegnern, die fallen?** Stürzt etwas ab? Findet `pruefe_zustand()` es? Findet die Suche aus Schritt 11 es? *(Konzept 10: Das Werkzeug, das Tippfehler laut macht, macht einen vergessenen Umbau still.)*

**7. Vertipp dich zweimal.** Einmal `self.status = "ttot"` — ein String, wie früher —, einmal `self.status = Zustand.TTOT`. **Wann knallt jeder der beiden, und wer bemerkt den ersten?** *(Tipp für den ersten: Es gibt seit Schritt 11 eine Zeile, die genau das prüft.)*

**8. Vergiss `.value` beim Speichern.** Erst eine Kopie deines Spielstands. Dann in `als_daten()` das `.value` weglassen und speichern. **Wann knallt es — beim Bauen des Dictionaries oder beim Schreiben der Datei?** Kommt dir die Meldung bekannt vor? **Und was steht danach in der Spielstand-Datei?** *(Etappe 19, der halb geschriebene Spielstand. Danach die Kopie zurück.)*

**9. Manipulier den Spielstand.** Setz in der gespeicherten Datei bei einer Einheit `"status": "untot"`. Laden. **Was passiert — und was wäre vor Schritt 12 passiert?** *(Konzept 11, letzter Absatz. Vor dem Laden die Datei sichern und danach zurückholen.)*

**10. ⭐ Wechsel mit ungesicherten Änderungen — zweimal.** Auf deinem Hauptzweig, nach Schritt 14. **a)** Häng an `befehle17.txt` eine Zeile an, **ohne** zu committen, und wechsel zu `balancing`. `git status`: Wo ist die Zeile? **b)** Zurück auf den Hauptzweig, die Zeile wieder heraus. Jetzt ändere in `spiel.py` die Zahl, die du auf `balancing` gedreht hast — ohne Commit — und versuch zu wechseln. **Was sagt Git — und warum ist die Zeile in `befehle17.txt` mitgekommen, die Zahl in `spiel.py` aber nicht?** *(Tipp: Welche der beiden Dateien sieht auf beiden Branches gleich aus?)* *(Konzept 14. Danach die Zahl von Hand zurück; `git status` muss wieder sauber sein.)*

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo nachsehen |
|---|---|---|
| `TypeError: '>' not supported between instances of 'tuple' and 'int'` — oder eine ähnliche Meldung mit `'tuple'` | Das Ergebnis von `berechne_treffer()` in **einen** Namen gepackt | Konzept 3, Kaputtmachen 2 |
| `TypeError: cannot unpack non-iterable int object` — nur manchmal | Ein Zweig gibt nur einen Wert zurück | Konzept 3, Schritt 2 |
| `ValueError: not enough values to unpack (expected 3, got 2)` | Drei Namen links, zwei Werte rechts | Konzept 3 |
| Ein Gegner gewinnt Trefferpunkte, wenn er getroffen wird — oder `pruefe_zustand()` meldet es | Keine Untergrenze, und der Schaden erreicht trotzdem `treffe()` | Design-Entscheidung, Kaputtmachen 1 |
| Fast jeder Schuss geht daneben | Zwei Argumente vertauscht — oft Panzerung und Trefferchance | Konzept 7, Kaputtmachen 3 |
| `TypeError: … got an unexpected keyword argument …` | Tippfehler im Parameternamen beim Aufruf | Konzept 7 |
| Deine Trefferquote liegt einen Prozentpunkt zu tief | `<` statt `<=` — oder der Wurf beginnt bei 0 | Konzept 5 |
| Ein Schütze trifft nie oder immer | Treffsicherheit noch auf `100` aus Schritt 4 — oder auf `0` | Schritt 6 |
| Die Munition reicht plötzlich ewig | Munition wird nur bei einem Treffer verbraucht | Schritt 6 |
| `diff` redet nach Schritt 5, obwohl alles trifft | Der Wurf wird schon gewürfelt | Kaputtmachen 5 |
| Beim Start knallt eine Behauptung aus `pruefe_trefferrechnung()` | Genau das soll sie — lies ihren Text | Schritt 3 |
| `AttributeError` mit dem Namen `TTOT` | Tippfehler im Namen eines Mitglieds | Konzept 9 |
| `NameError: name 'Zustand' is not defined` beim Start | Das `Enum` steht unter der Stelle, die die erste Einheit erzeugt | Schritt 10 |
| Gefallene Gegner verschwinden nicht, die Welle endet nie | Ein Vergleich mit `"tot"` ist übrig geblieben | Konzept 10, Kaputtmachen 6 |
| In der Ausgabe steht `Zustand.AKTIV` | `.value` fehlt | Konzept 10 |
| `TypeError: Object of type Zustand is not JSON serializable` | `.value` fehlt in `als_daten()` | Konzept 11 |
| `ValueError: '…' is not a valid Zustand` beim Laden | Ein unbekanntes Wort im Spielstand — oder ein Tippfehler in einem Wert des `Enum` | Konzept 11, Schritt 12 |
| `error: Your local changes … would be overwritten by checkout` | Nicht committet vor dem Wechsel | Konzept 14 |
| Eine Balancing-Änderung steht plötzlich auf dem Hauptzweig | Vor dem ersten Commit auf dem Branch gewechselt, mitgenommen und dort committet | Konzept 14, Kaputtmachen 10 |
| `fatal: The current branch balancing has no upstream branch.` | `git push` auf einem Branch, der nur bei dir existiert | Konzept 14 — heute nicht hochladen |
| `error: pathspec 'main' did not match any file(s) known to git` | Dein Hauptzweig heißt `master` | `git branch` |

---

## Ein Blick nach vorne

**Etappe 22 zieht deine Zahlen in Tabellen.** Trefferchance, Panzerung, Schaden, Abklingzeiten — was heute in `__init__` und in `GEGNERTYPEN` verstreut steht, wandert an einen Ort. Und dort stellt sich die Frage aus der Entwicklerfrage neu: Sind vier Klassen mit vier Sätzen Zahlen eigentlich vier Klassen — oder eine Klasse und eine Tabelle?

**Etappe 24 nimmt sich deinen Balancing-Branch vor.** Zusammenführen, einen Konflikt absichtlich herbeiführen, ihn auflösen — oder den Branch wegwerfen. Dein Experiment von heute ist das Übungsobjekt.

**Etappe 25 lädt Inhalt aus Dateien.** Gegnertypen mit ihrer Panzerung kommen aus JSON, und dort zeigt sich, warum sie Strings geblieben sind. Schadenstypen lassen sich dort als Daten nachrüsten statt als Code.

**Etappe 26 testet.** `pruefe_trefferrechnung()` wird dort fast unverändert eine Testdatei — und das geht nur, weil der Wurf von außen kommt. Deine Rechnung ist ab heute die erste Funktion deines Spiels, die man prüfen kann, ohne eine Welt zu bauen.

**Etappe 28 zeichnet.** Die Trefferart entscheidet dort, ob ein Treffer aufblitzt, ein Fehlschuss vorbeizischt oder ein Abpraller Funken schlägt — und die Zustände als `Enum` werden die Modi deines Spiels.

---

## Abschluss

**In `GELERNT.md`:**

- ⭐⭐ **Deine Design-Entscheidung** — a) oder b) — und ob sie sich beim Spielen bewährt hat.
- ⭐ Die sortierten Zettel aus Schritt 1, mit der mittleren Spalte als Liste für künftige Balancing-Versuche.
- Deine Antwort auf die Frage aus 15b — wer profitiert vom Zuschlag, jetzt, wo alle über `schiesse()` schießen?
- Die Kandidatentabelle aus Schritt 9.
- Wie viele Stellen die Fahndung in Schritt 11 gefunden hat — und ob die Zahl nach dem Umbau zur Suche passte.
- Deine Entscheidung zu `ValueError` beim Laden, aus Schritt 12.
- ⭐ **Dein Balancing-Experiment:** Vorhersage, sechs Messzeilen, zwei Sätze — schon da, seit Schritt 14.
- 🧠 Die Entwicklerfrage.
- Was hat mich überrascht? *(Kandidaten: wie viel ein Prozentpunkt ausmacht, den man nicht sieht · dass ein Umbau von zwei Wörtern eine ganze Welle lahmlegen kann · dass die Zahl nach dem Branch-Wechsel einfach wieder die alte war.)*

**Zum Schluss, auf deinem Hauptzweig:** Keine Probedatei, kein fester Wurf, kein vorübergehender Fehler? Kein `"tot"` außerhalb des `Enum`? `DEBUG` auf `True`?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest.

**Die Trefferart als zweites `Enum`.** Sie besteht die beiden Bedingungen aus Konzept 12. Bau es, und zähl, wie viele Stellen du anfassen musstest — im Vergleich zu den Zuständen. *(Dieselbe Frage wie beim Erweiterungstest aus Etappe 15: Was kostet eine Entscheidung, je nachdem, wann man sie trifft?)*

**Kritische Treffer.** Ein zweiter Wurf, nur nach einem Treffer: bei `10` oder weniger doppelter Schaden, Trefferart `"kritisch"`. **Wo würfelst du den zweiten Wurf** — und was heißt Konzept 4 für ihn? *(Dein `pruefe_trefferrechnung()` bekommt dafür eine vierte Behauptung.)*

**Entfernung zählt.** Pro Feld Abstand fünf Prozentpunkte weniger Trefferchance, nie unter `10`. Ein fünfter Eingang in die Rechnung — und eine Antwort auf die Entwicklerfrage, die du vorher aufgeschrieben haben solltest.

**Schadenstypen, klein.** Zwei Typen, ein Dictionary aus Faktoren nach Konzept 13, gerechnet vor der Panzerung. **Bau es auf einem zweiten Branch** — `git checkout -b schadenstypen`, abgezweigt von deinem Hauptzweig. Dann hast du zwei Versuche nebeneinander, und Etappe 24 hat mehr zu tun.

**Ein zweites Balancing-Experiment**, mit einer anderen Stellschraube, auf demselben Branch. **Und die Frage danach:** Hätte die Reihenfolge der beiden Experimente das Ergebnis des zweiten verändert?

---

> **Nächste Etappe:** Etappe 22 — Ausbaustufen und Tabellen · deine Zahlen ziehen an einen Ort, und der Basisturm bekommt seine fünf Stufen
