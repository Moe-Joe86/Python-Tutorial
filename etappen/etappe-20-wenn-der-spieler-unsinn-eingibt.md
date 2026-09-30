# Etappe 20 — Wenn der Spieler Unsinn eingibt

*v1.1.0 · 2026-09-30*

> **Block 3: Der Vorposten reagiert** · Etappe 20 von 30 · [← Etappe 19](etappe-19-speichern-und-laden.md) · [Lehrplan](../Vorposten_Lehrplan.md) · Etappe 21 →

**Neue Syntax heute:** 20a: `try:` / `except Fehlerklasse:` · `except Fehlerklasse as e:` und die Nachricht in `e` · mehrere `except` untereinander · `except json.JSONDecodeError:` · 🧠 eng fangen: nur die erwartete Fehlerklasse, nur um die eine Zeile · 🧠 prüfen oder fangen? · 🧠 `except Exception` und nacktes `except:` machen aus Typ 1 einen Typ 3 · 👀 Fehlerklassen haben Oberklassen — `JSONDecodeError` ist ein `ValueError` — 20b: `class SpielFehler(Exception):` mit einem Docstring als Körper · `raise SpielFehler("…")` · `else:` beim `try` · 🧠 ein Fehler wandert die Aufrufkette hinauf bis zum ersten passenden `except` · 🧠 `return` statt `raise` wirft nichts · 🧠 Grund-oder-`None` gegen Exception · 🧠 wem gehört ein Fehler — Spieler oder Entwickler? — 20c: `assert bedingung, "Text"` (hochgestuft aus Etappe 7) · 🧠 eine Behauptung wird nie gefangen — und `python -O` schaltet sie ab · 👀 `finally` · 👀 `raise` ohne Fehler dahinter · 👀 `logging` und seine Stufen

**Zeitaufwand:** 20a: 4–5 Sitzungen · 20b: 5–6 Sitzungen · 20c: 3–4 Sitzungen, à 20–30 Minuten. Knapp 60 Minuten davon sind Lesestoff — gut 20 in 20a (mit dem Anfang dieser Seite), knapp 20 in 20b und gut 15 in 20c, die Abschnitte am Ende jeweils mitgerechnet. **Lies jeweils nur die Portion, an der du sitzt.**

**Voraussetzung:** Etappe 19 abgeschlossen, Selbsttest grün. Du brauchst den Aufrufstapel aus Etappe 7a, die drei Fehlertypen und den Traceback aus Etappe 8, die Vererbung aus 11, die Prüfketten mit Grund aus 18b — und aus 19 `lade_daten()`, `aus_daten()` und deine Kaputtmach-Versuche mit dem manipulierten Spielstand. **Deine Invariantenliste aus `GELERNT.md`** brauchst du in 20c.

**Die drei Portionen:**

| | Was passiert | Was danach anders ist |
|---|---|---|
| **20a** | Fangen | `drei` statt `3` bringt dein Spiel nicht mehr zum Absturz, eine kaputte Spielstand-Datei auch nicht. Und du weißt, warum man **nicht** alles fängt. |
| **20b** | Werfen | Jeder Befehl, der gerade nicht geht, sagt dem Spieler warum — über **einen** Weg, an **einer** Stelle, und er kostet keine Runde. |
| **20c** | Prüfen und trennen | Deine Invarianten seit Etappe 5 werden geprüft, bei jedem Takt. Und was für dich als Entwickler gedacht ist, hat einen eigenen Weg mit Schalter. |

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **20a** | `try`/`except` um genau die Zeilen, die in der Welt scheitern dürfen · die Chaos-Datei | Fehlerbehandlung ist nicht Debugging · eng fangen · prüfen oder fangen | Fehlerklassen haben Oberklassen |
| **20b** | Eine eigene Fehlerklasse · `raise` · **eine** Stelle, die dem Spieler Fehler zeigt · `else` beim `try` | Ein Fehler wandert nach oben · wann ein Grund, wann eine Exception · wem ein Fehler gehört | — |
| **20c** | Invarianten als `assert` · ein Debug-Weg mit Schalter | Behauptung gegen Behandlung | `finally` · `logging` |

---

# Teil 20a — Fangen

## Worum es geht

Gib bei der Klassenwahl `zwei` ein. Seit Etappe 3a steht im Guide: *„stürzt weiterhin ab, mit `ValueError` aus `int()`. Das fängt erst Etappe 20."* **Heute ist Etappe 20.**

Und es ist nicht die einzige Stelle. Seit Etappe 1 bist du durch dieses Programm gegangen und hast an jeder Ecke einen Satz gelesen wie *„das stürzt ab — und das ist heute in Ordnung"*. Die Mengenabfrage beim Kaufen. Ein Befehl ohne zweites Wort. Eine Spielstand-Datei mit einem fehlenden Komma. **Neunzehn Etappen lang war ein Absturz beim Entwickeln ein Fund, kein Ärgernis** — so steht es in Etappe 8.

**Ab heute trennst du zwei Dinge, die bisher gleich aussahen:**

- **Ein Fehler in deinem Programm.** Ein Tippfehler im Namen, eine vergessene Klammer, ein Index, der nicht passt. Den sollst du **sehen**, so laut wie möglich — er gehört dir, und du musst ihn beheben.
- **Ein Fehler in der Welt.** Der Spieler tippt `drei`. Die Datei ist beschädigt. Dein Programm ist völlig richtig — und trotzdem geht es gerade nicht weiter. Diesen Fehler kannst du nicht beheben, nur **behandeln**.

> **Fehlerbehandlung ist für Fehler, die passieren dürfen.** Alles andere ist Debugging, und das kennst du seit Etappe 8.

Das klingt nach einer Selbstverständlichkeit. Der Rest dieser Etappe besteht darin, sie durchzuhalten — gegen das Werkzeug, das du heute lernst. Denn `try`/`except` kann beides fangen, und genau das ist seine Gefahr.

---

## Der lange Bogen — was heute fällig wird

**In 20a:**
- **Etappe 1:** *`int()` kann mit `ValueError` scheitern.* Die Klassenwahl, die Mengen beim Kaufen und Verkaufen aus Etappe 5 — dreimal dieselbe Zeile, dreimal dieselbe Antwort.
- **Etappe 3a:** *`zwei` stürzt weiterhin ab. Das fängt erst Etappe 20.*
- **Etappe 5:** *`.get()` — die leichtere Alternative zu `try`/`except`.* Heute siehst du beide nebeneinander und entscheidest, wann welche.
- **Etappe 7a:** *Die Chaos-Datei findet Validierungslücken.* Heute schreibst du sie.
- **Etappe 8:** *Der bewusste Verzicht auf `try`/`except`* — und die Warnung, dass nacktes `except:` aus einem Typ 1 einen Typ 3 macht.
- **Etappe 19:** `JSONDecodeError` beim Laden, die Klasse `"Pilot"` im Spielstand — deine Kaputtmach-Versuche b) und c).

**In 20b:**
- **Etappe 2:** *Eine verknüpfte Bedingung sagt nicht, welcher Teil scheiterte* — und *der `else`-Zweig für Unerwartetes*.
- **Etappe 4:** *Befehl ohne zweites Wort*, *Inventar voll*, *`remove()` ohne Element*, *erst prüfen, dann anfassen.*
- **Etappe 5:** *Der Kaufvorgang prüft drei Bedingungen — drei Bedingungen werden drei Fehler.*
- **Etappe 6:** *„Kein gültiges Wort" gegen „hier nicht möglich".*
- **Etappe 12:** *Ein Tick pro Befehl — auch bei ungültigem Befehl?*
- **Etappe 18b:** *`kann_lernen()` liefert einen Grund oder `None`* — und die Ankündigung: *In Etappe 20 lernst du einen zweiten Weg, einen Grund durch das Programm zu tragen.*

**In 20c:**
- **Etappe 5, 10, 13, 18:** deine Invariantenliste. *Bis 20 werden sie nur aufgeschrieben, nicht geprüft.*
- **Etappe 7b:** `assert` — seit damals auf 👀. Heute wird er gebaut.
- **Etappe 17b und 17c:** *Deine Debug-Zeile und dein Wellenbericht sind zwei Sorten Meldung mit zwei Adressaten — in Etappe 20 bekommen sie getrennte Wege.*
- **Etappe 19:** *`finally` hilft gegen Programmfehler, nicht gegen einen Stromausfall.*

---

## Die Konzepte — Teil 20a

Heute in einer Pizzeria mit Bestellautomat.

### 1. Ein Fehler, der passieren darf

```python
anzahl = int(input("Wie viele Pizzen? "))
print(f"{anzahl} Pizzen kommen.")
```

Tippt jemand `zwei`, siehst du, was du seit Etappe 1 kennst:

```
ValueError: invalid literal for int() with base 10: 'zwei'
```

**Dein Programm ist nicht kaputt.** Es tut genau das, was es soll: Es verlangt eine Zahl und bekommt keine. Der Fehler liegt draußen, beim Menschen an der Tastatur — und er **wird** passieren, bei jedem, der den Automaten benutzt. Ein Programm, das deshalb stirbt, ist wie ein Automat, der bei einem falschen Knopfdruck den Strom abschaltet.

**Was du stattdessen willst:** *Versuch es. Und wenn es nicht klappt, sag es und frag noch einmal.*

### 2. ⭐⭐ `try` und `except`

```python
anzahl = None
while anzahl is None:
    eingabe = input("Wie viele Pizzen? ")
    try:
        anzahl = int(eingabe)
    except ValueError:
        print("Bitte eine Zahl, zum Beispiel 2.")
print(f"{anzahl} Pizzen kommen.")
```

**Lies `try` und `except` wie ein Versuch mit Notfallplan:**

- **`try:`** — *Versuch, was eingerückt darunter steht.* Klappt alles, läuft das Programm nach dem ganzen `try`-`except`-Block weiter, als stünde das `try` gar nicht da.
- **`except ValueError:`** — *Wenn beim Versuch ein `ValueError` auftritt, mach stattdessen das hier.* Python **springt** in dem Moment, in dem der Fehler auftritt, aus dem `try`-Block heraus in den `except`-Block. Was im `try`-Block **nach** der scheiternden Zeile stand, läuft nicht mehr.
- **Danach** geht es nach dem ganzen Block weiter — der Fehler ist *behandelt*, das Programm lebt.

**Zwei Dinge sieht man an dem Beispiel, wenn man genau hinschaut:**

- **`anzahl` bekommt beim Scheitern keinen neuen Wert.** Die Zuweisung `anzahl = int(eingabe)` passiert ja nicht — `int()` scheitert, bevor links etwas ankommt. Deshalb bleibt `anzahl` bei `None`, und die Schleife fragt noch einmal. Das ist die Form aus Etappe 10: `None` als *„noch nichts da"*, geprüft mit `is None`.
- **Hinter `except` steht eine Fehlerklasse.** `ValueError` ist der Name, der auch ganz unten im Traceback steht. **`except` fängt nur diese eine Sorte.** Ein anderer Fehler im `try`-Block — ein `NameError`, weil du dich vertippt hast — fliegt einfach weiter, wie ohne `try`.

### 3. ⭐⭐ Eng fangen — die wichtigste Regel dieser Etappe

Die zweite Beobachtung aus Konzept 2 ist keine Nebensache. Sie ist **der** Grund, warum `except` eine Fehlerklasse verlangt:

> **Fang nur den Fehler, den du erwartest — und nur um die Zeile, an der du ihn erwartest.**

**Was passiert, wenn man es nicht tut:**

```python
try:
    anzahl = int(eingabe)
    preis = anzahl * PIZZAPRIES          # Tippfehler: PIZZAPRIES statt PIZZAPREIS
    print(f"Das macht {preis} Euro.")
except Exception:
    print("Bitte eine Zahl, zum Beispiel 2.")
```

`Exception` ist die Oberklasse fast aller Fehlerklassen — `except Exception` fängt also **jeden Fehler, den dein Programm machen kann**. Der Kunde tippt `2`, `int()` klappt, die nächste Zeile stolpert über den Tippfehler: `NameError`. **Und `except Exception` fängt ihn.** Der Automat sagt *„Bitte eine Zahl"* — zu einer Zahl. Dein Traceback, der dir seit Etappe 1 in einer Zeile gesagt hätte, wo der Tippfehler steht, ist weg.

**Das ist die Verwandlung, vor der Etappe 8 gewarnt hat:** Ein Fehler vom Typ 1 — sofort, ehrlich, mit Zeilennummer — wird zu einem vom Typ 3: Das Programm läuft und sagt etwas Falsches.

Zwei Dinge schützen dich davor, und du brauchst beide:

| | Was | Warum |
|---|---|---|
| **Eng in der Klasse** | `except ValueError`, nicht `except Exception` | Fehler, mit denen du nicht gerechnet hast, fliegen weiter |
| **Eng im Block** | nur die Zeile, die scheitern darf, in den `try` | Was danach kommt, ist dein Code — dessen Fehler willst du sehen |

**🚨 KI-Code-Warnsignal — das häufigste von allen:**

```python
try:
    irgendwas()
except Exception as e:
    print("Fehler")
```

Sieht verantwortungsvoll aus und überlebt jeden Test. **Die Frage daran ist nicht *„ist das schlimm?"*, sondern: Welchen Fehler wollte der Autor eigentlich abfangen — und warum steht er nicht da?** Und die Steigerung davon ist `except:` ganz ohne Klasse. Das fängt sogar `Strg + C`. Wer das in eine Schleife schreibt, bekommt ein Programm, das sich nicht mehr abbrechen lässt.

*(`except Exception` ist kein verbotenes Python. Es gibt Stellen, an denen es richtig ist — ganz oben in einem Programm, das nie stehen bleiben darf, etwa einem Server, und dann mit dem vollständigen Traceback in einer Protokolldatei statt mit „Fehler". Dein Spiel hat keine solche Stelle. **Die Regel „kein `except Exception`" in den Selbsttests gilt für deinen Code in diesem Tutorial** — in fremdem Code ist sie eine Frage an den Autor, kein Urteil.)*

### 4. Die Nachricht mitnehmen: `as e`

```python
try:
    anzahl = int(eingabe)
except ValueError as e:
    print(f"Das war keine Zahl ({e}).")
```

**`as e`** gibt dem gefangenen Fehler einen Namen — dieselbe Form wie `as f` bei `with open` aus Etappe 19. In `e` steckt ein Objekt, und `print(e)` oder ein f-String zeigt **seine Nachricht** — dieselbe, die sonst unten im Traceback stünde, ohne den Klassennamen davor: `invalid literal for int() with base 10: 'zwei'`.

**Für den Spieler ist diese Nachricht meist nichts** — *„invalid literal"* sagt einem Pizzakunden nichts. **Für dich als Entwickler ist sie Gold**, wenn du wissen willst, *was* genau schiefging. Wer sie zeigt und wem, klärt 20b und 20c.

*(Eine Eigenheit, die dich einmal verwirren wird: Bei einem `KeyError` ist die Nachricht der fehlende Schlüssel **mit Anführungszeichen** — `'klasse'`. Das ist kein Fehler in deinem f-String.)*

### 5. ⭐ Prüfen oder fangen?

Du kennst schon Werkzeuge, die einen Fehler **verhindern**, bevor er passiert:

| Frage | Prüfen — seit … | Fangen — seit heute |
|---|---|---|
| Gibt es den Schlüssel? | `in` oder `.get()`, Etappe 5 | `try` … `except KeyError` |
| Gibt es die Datei? | `.exists()`, Etappe 19 | `try` … `except FileNotFoundError` |
| Steht der Wert in der Liste? | `in`, Etappe 4 | `try` … `except ValueError` bei `remove()` |
| Ist dieser Text eine Zahl? | **—** | `try` … `except ValueError` bei `int()` |
| Ist diese Datei gültiges JSON? | **—** | `try` … `except json.JSONDecodeError` |

**Sieh dir die letzten zwei Zeilen an.** Für diese Fragen gibt es keine Prüfung vorher, die du kennst — **man erfährt es nur, indem man es versucht.** Ob `"12"`, `" 12 "`, `"-3"` oder `"1e3"` eine Zahl ist, weiß am zuverlässigsten `int()` selbst. Ob eine Datei gültiges JSON ist, weiß `json.load()`.

**Daraus eine Faustregel:**

> **Prüf vorher, wenn die Frage einfach ist und ihre Antwort bis zur nächsten Zeile gilt. Fang hinterher, wenn erst der Versuch selbst zeigt, ob es klappt.**

**Die ersten drei Zeilen prüfst du weiterhin**, wie seit Etappe 4, 5 und 19. `in` und `.get()` sagen beim Lesen sofort, was du erwartest; ein `try` um einen Dictionary-Zugriff zwingt den Leser, erst den `except`-Zweig zu suchen. *(In fremdem Code wirst du beide Stile sehen. Es gibt Programmierer, die grundsätzlich lieber fangen — das ist eine Stilfrage mit guten Argumenten auf beiden Seiten. In diesem Tutorial gilt die Faustregel.)*

*(„Bis zur nächsten Zeile" ist bei der Datei-Zeile nicht ganz selbstverständlich: `.exists()` fragt die Festplatte, und die gehört nicht deinem Programm. Zwischen der Prüfung und dem Öffnen könnte ein anderes Programm die Datei löschen. Bei deinem Spielstand, den nur dein Spiel anfasst, ist das kein Thema; in Programmen, in denen viele gleichzeitig auf dieselben Dateien zugreifen, fängt man deshalb eher. Bei deinen eigenen Dictionaries und Listen kann dir niemand dazwischenfunken — dort gilt die Antwort von `in` sicher bis zur nächsten Zeile.)*

⚠️ **Und das, was keine der beiden Spalten kann:** `int("-3")` klappt. Keine Exception, kein Grund zu fangen — **und trotzdem kann niemand minus drei Pizzen bestellen.** Dass etwas nicht abstürzt, heißt nicht, dass es gültig ist. **Nach dem Fangen kommt oft noch ein Prüfen** — mit einem ganz gewöhnlichen `if`.

### 6. Mehrere `except` — und eine Familie hinter den Namen

Ein Versuch kann auf mehr als eine Art scheitern. Dann stehen mehrere `except` untereinander, und **der erste passende gewinnt**:

```python
try:
    with open(pfad, "r", encoding="utf-8") as f:
        bestellung = json.load(f)
except FileNotFoundError:
    print("Keine gespeicherte Bestellung.")
except json.JSONDecodeError:
    print("Die gespeicherte Bestellung ist beschädigt.")
```

**`json.JSONDecodeError`** ist die Fehlerklasse aus Etappe 19, Kaputtmachen 3 und 11 — sie wohnt im Werkzeugkasten `json`, deshalb steht der Kastenname davor, wie bei `json.load`.

👀 **Fehlerklassen sind Klassen — und haben Oberklassen**, wie deine Marines seit Etappe 11. `JSONDecodeError` ist eine Unterklasse von `ValueError`. Deshalb fängt `except ValueError` auch einen `JSONDecodeError`. **Stünde `except ValueError` oben, käme `except json.JSONDecodeError` darunter nie zum Zug** — der erste passende gewinnt. In Bibliotheken ist das Absicht: Wer nur *„irgendein Wertfehler"* wissen will, fängt die Oberklasse; wer es genau wissen will, die Unterklasse. **Bauen musst du heute keine solche Familie** — erkennen, wenn du `except json.JSONDecodeError` in fremdem Code siehst, dass es ein Mitglied einer größeren ist.

---

## Dein Auftrag — Teil 20a

---

### 1. ⭐ Schreib die Chaos-Datei — und führ Buch

**`chaos.txt`**, eine Befehlsdatei im Format seit Etappe 7: eine Zeile pro `input()`, in der Reihenfolge, in der dein Spiel fragt — **von der Startfrage aus 19c an**.

Dreißig bis fünfzig Zeilen, **absichtlich falsch**. Du bist ab jetzt nicht der Spieler, sondern jemand, der dein Spiel kaputt machen will. Ein paar Anregungen, keine Vollständigkeit:

- Wörter statt Zahlen, Zahlen statt Wörter, leere Zeilen, Leerzeichen, Großbuchstaben
- Negative Zahlen und riesige Zahlen, wo Mengen erwartet werden
- Befehle ohne zweites Wort, mit drei Wörtern, mit einem Wort, das es nicht gibt
- `kaufe` außerhalb des Depots, `nimm` ohne dass etwas liegt, `lerne` einer Fähigkeit, die es nicht gibt, `gehe` in eine Richtung ohne Ausgang
- Bei der Startfrage etwas anderes als `j` oder `n`

**Dann, im Projektordner:**

```
python spiel.py < chaos.txt > chaos_lauf.txt
```

`chaos_lauf.txt` entsteht von selbst. **Stürzt es ab, steht der Traceback im Terminal**, nicht in der Datei — Etappe 7b, die zwei Ausgabekanäle.

**Führ Buch in `GELERNT.md`, unter *Chaos-Liste*:** Jeder Absturz eine Zeile — welche Eingabe, welche Fehlerklasse, in welcher Funktion. **Dann nimm die Zeile, die den Absturz ausgelöst hat, aus `chaos.txt` heraus** (oder schreib sie weiter hinten noch einmal hin) und lass die Datei erneut laufen, bis sie zum `EOFError` am Ende durchkommt.

*(Der `EOFError` am Dateiende ist weiterhin kein Fund — Etappe 7. Er bleibt, und du fängst ihn nicht.)*

**Und eine zweite Spalte, die wichtiger ist als die erste:** Eingaben, die **nicht** abgestürzt sind, aber etwas Falsches getan haben — ein Kauf mit negativer Menge, ein Befehl, der still gar nichts tut. **Die findet kein Traceback.** Du findest sie nur, wenn du `chaos_lauf.txt` liest.

*(Die Liste ist dein Arbeitsplan für diese Etappe. Ihre Zeilen verschwinden in 20a und 20b eine nach der anderen.)*

---

### 2. Frag bei der Klassenwahl nach, statt abzustürzen

Seit Etappe 3a steht die Klassenwahl in einer Schleife, die bei ungültiger Nummer neu fragt — nur `int()` selbst stürzt noch ab.

- **Leg ein `try` um genau die Zeile mit `int()`**, nach Konzept 2 und 3. Nicht um die ganze Kette.
- **Im `except ValueError`:** eine Meldung in deinen Worten, und es wird neu gefragt.
- **Der Punkt, an dem man hängt:** Nach dem `except` darf deine `if`/`elif`-Kette nicht laufen — sie setzt eine Zahl voraus. **Der gedeckte Weg ist die Form aus Konzept 2:** eine kleine Schleife *nur für die Zahl*, die fragt, bis `int()` klappt — und erst danach, außerhalb dieser kleinen Schleife, deine Kette aus 3a, unverändert. Zwei Schleifen: die kleine sorgt für *eine Zahl*, die große aus 3a für *eine gültige Klasse*.

**So prüfst du es:** `zwei`, dann `9`, dann `2`. Zwei Meldungen, zwei neue Fragen, dann das Briefing. **Und kein anderer Fehler wurde verschluckt:** Bau vorübergehend einen Tippfehler in die Zeile **nach** dem `int()` und gib `2` ein — der `NameError` muss laut kommen. Danach zurück.

---

### 3. ⭐ Mach die Mengen sicher — kaufen und verkaufen

Dieselbe Zeile wie in Schritt 2, **zweimal**: bei der Mengenabfrage in `kaufe` und in `verkaufe` aus Etappe 5.

- `try` um das `int()`, `except ValueError`. Was danach passiert — noch einmal fragen oder den Kauf abbrechen —, entscheidest du. **Abbrechen heißt: nichts verändert, kein Vaporium weg.** Die Transaktion aus Etappe 5.
- **Und danach, mit einem gewöhnlichen `if`, nach Konzept 5, letzter Absatz:** Eine Menge von `0` oder darunter wird abgewiesen, **bevor** gerechnet wird.

⚠️ **Die zweite Zeile ist die wichtigere.** Kauf mit `-3` einmal aus, **bevor** du sie baust, und sieh auf dein Vaporium. Stand das in deiner Chaos-Liste, zweite Spalte? Wenn nicht: Das ist der Grund, warum man die Ausgabe liest.

*(Kaufen und Verkaufen haben jetzt fast dieselben sechs Zeilen. Wenn dich das stört, gehört die Mengenabfrage in eine kleine Funktion, die eine gültige Menge zurückgibt — oder `None`, wenn der Spieler abbricht. **Sag für beide Fälle, was zurückkommt**, und prüf beim Aufrufer mit `is None`. Ob du das heute baust oder in `GELERNT.md` notierst, entscheidest du.)*

**So prüfst du es:** `kaufe medkit`, dann `drei`, dann `-3`, dann `0`, dann `2`. Nur der letzte Kauf kostet etwas.

---

### 4. ⭐ Lade robust — eine kaputte Datei ist kein Absturz

In `lade_daten()` aus 19a steht `json.load(f)`. **Seit Etappe 19, Kaputtmachen 11 b), weißt du, was ein fehlendes Komma daraus macht.**

- **`try` um das Öffnen und Lesen**, nach Konzept 6: `except json.JSONDecodeError` — eine Meldung, dass der Spielstand beschädigt ist, und `None` zurück, wie in den anderen zwei Fällen aus 19a, Schritt 7.
- **Ist `FileNotFoundError` jetzt auch ein Fall für `except`?** Du prüfst seit 19a vorher mit `.exists()`. Konzept 5 sagt, was du davon behältst. **Schreib einen Satz in `GELERNT.md`.**

**Und der zweite Fall aus Etappe 19, c): die Klasse `"Pilot"`.** Er knallt nicht in `lade_daten()`, sondern später — in `aus_daten()`, wenn das Dictionary *Klassenname → Klasse* das Wort nicht findet. `KeyError`.

⚠️ **Hier wird Konzept 3 ernst.** Ein `try` um `welt.aus_daten(daten)` mit `except KeyError` fängt den Pilot. **Er fängt aber auch jeden `KeyError`, der aus einem Tippfehler in deinem eigenen `aus_daten()` kommt** — und der sieht für `except` genauso aus. Zwei Fälle, eine Fehlerklasse, und nur einer davon gehört dem Spielstand.

**Zwei gedeckte Wege — wähl einen und schreib ihn in `GELERNT.md`:**

| | Was du baust | Was es kostet |
|---|---|---|
| **a)** | `try` um `aus_daten()`, `except KeyError as e`: Meldung **mit der Nachricht aus `e`** — *„Spielstand unlesbar, fehlt: 'Pilot'"* — und ein neues Spiel, auf demselben Weg wie in 19c, Schritt 20, wenn `lade_daten()` `None` liefert | Ein Tippfehler in `aus_daten()` sieht danach aus wie ein kaputter Spielstand. **Die Nachricht aus `e` ist dein Schutz:** Sie nennt den Schlüssel, und du erkennst deinen eigenen. |
| **b)** | Nichts fangen. Ein Spielstand, der `aus_daten()` scheitern lässt, lässt das Spiel abstürzen | Ehrlich, laut — und für einen Spieler ohne Programmierkenntnis das Ende. |

⚠️ **Bei a): Die Welt, die `aus_daten()` halb gefüllt hat, darf danach nicht weiterleben.** `aus_daten()` ist mitten in der Arbeit abgebrochen — der Trupp vielleicht schon geladen, die Minen nicht. Sorg dafür, dass dein Hauptprogramm danach den Zweig für ein **neues** Spiel nimmt, mit einer frischen Welt. Wie das geht, hängt davon ab, woran dein Hauptprogramm seit 19c, Schritt 20, erkennt, ob geladen wurde — sieh nach.

*(Es gibt einen dritten, saubereren Weg: jeden Schlüssel **vorher** prüfen, bevor `aus_daten()` ihn benutzt — die *strukturelle* Prüfung. Das ist Etappe 25, und dort lernst du, warum er mehr Arbeit ist, als er aussieht.)*

⚠️ **Und Kaputtmachen 11 a) aus Etappe 19** — `"kern_integritaet": "viel"` — fängst du heute **nicht**. Er knallt nicht beim Laden, sondern Züge später beim ersten Vergleich, weit weg von jedem `try`. Einen falschen Wert **beim Laden** zu erkennen, braucht dieselbe Vorab-Prüfung wie oben: Etappe 25.

**So prüfst du es:** Drei Kopien deines Spielstands, jede anders beschädigt — ein fehlendes Komma, eine Klasse `"Pilot"`, eine leere Datei. **Jede startet ein neues Spiel mit einer verständlichen Meldung**, keine stürzt ab. *(Danach den echten Spielstand zurück.)*

---

### 5. Lass die Chaos-Datei noch einmal laufen, und commit

- `python spiel.py < chaos.txt > chaos_lauf.txt` — **mit der vollständigen Datei**, auch den Zeilen, die du in Schritt 1 herausgenommen hast. **Welche Zeilen der Chaos-Liste sind jetzt erledigt?** Streich sie durch — in beiden Spalten.
- Was übrig bleibt, sind Befehle, die mit einer Meldung abbrechen oder still nichts tun. **Das ist die Liste für 20b.**
- Keine vorübergehenden Tippfehler mehr im Code. `chaos.txt` darfst du behalten, `chaos_lauf.txt` nicht.
- Die Abschnitte am Ende, die zu 20a gehören: **Transferaufgabe** und **Kaputtmachen 1 bis 3**.

Commit: `Etappe 20a: Fangen`

---

## Selbsttest — 20a

- [ ] `zwei` bei der Klassenwahl: eine Meldung und eine neue Frage.
- [ ] Ein vorübergehender Tippfehler direkt **nach** einem deiner `int()` bringt einen lauten `NameError` — dein `try` fängt ihn nicht.
- [ ] Kein `except` in deinem Programm ohne Fehlerklasse, keines mit `Exception`.
- [ ] Jeder `try`-Block umschließt nur die Zeilen, die in der Welt scheitern dürfen.
- [ ] Eine Menge von `-3` oder `0` kauft nichts und verkauft nichts.
- [ ] Eine Spielstand-Datei mit fehlendem Komma startet ein neues Spiel mit Meldung.
- [ ] Deine Chaos-Liste hat zwei Spalten, und in der zweiten steht mindestens eine Eingabe, die nie abgestürzt ist.

> **⏸ Ende von 20a.** Dein Spiel stürzt an den Stellen nicht mehr ab, an denen die Welt schuld ist. 20b kümmert sich um die Stellen, an denen es gar nicht abstürzt — sondern nur nicht sagt, warum etwas nicht geht.

---

# Teil 20b — Werfen

## Worum es geht

Nach 20a stürzt dein Spiel an den Stellen nicht mehr ab, an denen die Welt schuld ist. **Übrig geblieben ist die zweite Spalte deiner Chaos-Liste** — Befehle, die nicht abstürzen, sondern irgendwie enden: mit einer Meldung, mit einem `return`, manchmal mit gar nichts.

Sieh dir an, wie viele Arten dein Spiel inzwischen hat, *„das geht jetzt nicht"* zu sagen:

- `kaufe` meldet und steigt mit `return` aus — an drei Stellen, für drei Gründe.
- `lerne` fragt `kann_lernen()`, bekommt einen Grund und meldet ihn.
- `nimm` ohne zweites Wort meldet etwas — oder stürzt mit `IndexError` ab, je nachdem, was du in Etappe 4 gebaut hast.
- Ein unbekannter Befehl landet im `else` der Befehlskette.
- **Und kostet eines davon eine Runde?** Etappe 12 hat die Frage gestellt: *Ein Tick pro Befehl — auch bei ungültigem Befehl?* Die ehrliche Antwort ist bei den meisten: *kommt drauf an, wo das `return` steht.*

**Heute bekommen alle diese Fälle einen gemeinsamen Weg.** Wo immer ein Befehl merkt, dass er nicht ausgeführt werden kann, **wirft** er einen Fehler — mit dem Grund darin. Und an **genau einer** Stelle wird er gefangen, dem Spieler gezeigt, und es vergeht keine Zeit.

Das Werkzeug dafür ist `try`/`except` von der anderen Seite: nicht einen Fehler fangen, den Python wirft, sondern **selbst einen werfen**.

---

## Eine Design-Entscheidung: Wer darf einen Fehler werfen? ⭐

**Das Problem:** Ab heute kann jede Funktion einen `SpielFehler` werfen, und er wandert nach oben, bis ihn jemand fängt. **Gefangen wird er an einer einzigen Stelle: dort, wo die Befehle des Spielers ausgeführt werden.** Was passiert mit einem Fehler, der auf einem Weg geworfen wird, auf dem gar kein Befehl des Spielers läuft?

| Weg | Wer ruft auf | Wer fängt einen `SpielFehler` |
|---|---|---|
| Befehl `lerne`, `kaufe`, `setze` … | der Spieler, über deine Befehlsverarbeitung | **die eine Stelle** — Meldung, keine Runde |
| `lerne_selbst()`, `will_einsetzen()`, `setze_ein()` durch einen Kameraden | der Tick | **niemand** — das Spiel stürzt ab |
| die Einsammelphase, der Wellenbericht, ein Ereignis | die Pause zwischen den Wellen | **niemand** |

**Die Regel, die der Plan daraus macht — eine Regel für dieses Spiel, keine von Python:**

> **Ein `SpielFehler` wird nur auf Wegen geworfen, die ein Befehl des Spielers ausgelöst hat.**

Das klingt nach einer Einschränkung und ist eine Klärung: **Ein Fehler, den der Spieler verursacht hat, braucht einen Spieler, dem man ihn zeigt.** Ein Kamerad, der nichts lernen kann, hat keinen Fehler gemacht — er lernt einfach nichts. Deshalb fragen die Kameraden seit Etappe 18 *vorher* (`kann_lernen()`, `kann_einsetzen()`), und deshalb bleiben diese Fragen, wie sie sind: **Sie liefern einen Grund oder `None`, sie werfen nicht.** Konzept 9 sagt, wann welcher Weg passt.

**Schreib die Regel in `GELERNT.md`.** In Schritt 8 entscheidest du an jeder Stelle danach.

---

## Die Konzepte — Teil 20b

Heute an einem Fahrkartenautomaten.

### 7. ⭐⭐ Selbst werfen: `raise` und eine eigene Fehlerklasse

```python
class AutomatFehler(Exception):
    """Ein Fehler, den der Kunde verursacht hat — nicht der Automat."""


def pruefe_ziel(ziel):
    if ziel not in TARIFE:
        raise AutomatFehler(f"Nach {ziel} fährt von hier kein Zug.")
```

**Zwei neue Dinge:**

- **Eine eigene Fehlerklasse** — eine Klasse, die von `Exception` erbt, der Oberklasse fast aller Fehler aus Konzept 3. Vererbung aus Etappe 11, nichts sonst. **Ihr Körper ist nur ein Docstring**, wie die leere Methode aus Etappe 12, Konzept 7 — sie braucht nichts Eigenes, sie erbt alles, was ein Fehler können muss. Ihr einziger Zweck ist ihr **Name**: Ab jetzt gibt es eine Sorte Fehler, die nur deinem Programm gehört, und `except AutomatFehler` fängt genau diese Sorte und keine andere.
- **`raise`** wirft einen Fehler. Dahinter steht ein Fehler-Objekt, erzeugt wie jedes Objekt: Klassenname, Klammern, und darin die Nachricht. **Ab dieser Zeile passiert in der Funktion nichts mehr** — wie bei `return`, nur dass nichts zurückgegeben wird, sondern der Fehler losfliegt.

⚠️ **Die Falle, in die man genau einmal tritt:** `return AutomatFehler("…")` statt `raise`. Das stürzt nicht ab — es **gibt ein Fehler-Objekt zurück**, und der Aufrufer, der den Rückgabewert nicht beachtet, macht einfach weiter. Der Kunde bekommt eine Fahrkarte nach nirgendwo. *(Kaputtmachen 7.)*

### 8. ⭐⭐ Der Fehler wandert — bis ihn jemand fängt

```python
def verkaufe(ziel, geld):
    pruefe_ziel(ziel)
    preis = TARIFE[ziel]
    if geld < preis:
        raise AutomatFehler(f"Es fehlen {preis - geld} Euro.")
    drucke_fahrkarte(ziel)


while True:
    ziel = input("Wohin? ")
    try:
        verkaufe(ziel, 5)
    except AutomatFehler as e:
        print(e)
```

**Verfolge `Mondstadt` durch das Programm**, eine Zeile nach der anderen:

1. Die Schleife ruft `verkaufe()` auf — **innerhalb** des `try`.
2. `verkaufe()` ruft `pruefe_ziel()` auf.
3. `pruefe_ziel()` findet `Mondstadt` nicht und wirft.
4. **`pruefe_ziel()` ist sofort zu Ende.** Der Fehler fliegt zurück zu dem, der aufgerufen hat — `verkaufe()`.
5. `verkaufe()` hat kein `try`. **Also ist auch `verkaufe()` sofort zu Ende**, mitten in seiner ersten Zeile. `preis = …` läuft nie.
6. Der Fehler fliegt weiter zur Schleife. **Die hat ein `try` mit einem passenden `except`** — dort landet er, `print(e)` zeigt die Nachricht, und die Schleife fragt weiter.

**Das ist der Aufrufstapel aus Etappe 7a, rückwärts gelesen.** Ein Fehler steigt so lange Stufe um Stufe nach oben, bis er auf ein `except` trifft, das zu ihm passt. **Findet er keines, bis ganz oben**, stürzt das Programm ab — und der Traceback, den du seit Etappe 8 von unten nach oben liest, **ist genau dieser Weg**, aufgeschrieben.

**Und der Gewinn:** `verkaufe()` muss von dem Fehler aus `pruefe_ziel()` nichts wissen. Es muss nichts zurückgeben, nichts prüfen, nichts durchreichen. **Die Stufen dazwischen bleiben still.** Das ist der Unterschied zu allem, was du bisher hattest.

### 9. ⭐ Grund oder Exception?

Seit Etappe 18b kennst du den anderen Weg, einen Grund durch das Programm zu tragen:

```python
def einwand(ziel, geld):
    if ziel not in TARIFE:
        return f"Nach {ziel} fährt von hier kein Zug."
    if geld < TARIFE[ziel]:
        return "Das Geld reicht nicht."
    return None
```

**Beide Wege tragen denselben Satz.** Sie unterscheiden sich darin, **wer ihn bekommt und was er damit tun muss**:

| | Grund oder `None` — seit 18b | Exception — seit heute |
|---|---|---|
| Der Aufrufer … | **fragt**, ob etwas geht | **verlangt**, dass etwas passiert |
| Wer den Grund bekommt | der direkte Aufrufer — und nur der | der erste passende `except`, egal wie weit oben |
| Die Stufen dazwischen | müssen prüfen und weiterreichen | bleiben still |
| Wer ihn vergisst zu prüfen | macht still weiter — Typ 3 | fliegt laut bis oben — Typ 1 |
| Passt, wenn … | *„Nein"* eine normale Antwort ist | *„Nein"* den ganzen Vorgang abbricht |

**Die erste Zeile ist die Entscheidung.** Ein Kamerad **fragt**, ob er eine Fähigkeit einsetzen kann — und ein *„Nein"* ist für ihn völlig normal, er tut dann etwas anderes. Der Spieler **verlangt** es mit einem Befehl — und ein *„Nein"* bricht seinen Befehl ab.

**Deshalb verbinden sich beide Wege an genau einer Stelle:** Der Befehl des Spielers fragt die Funktion, die einen Grund liefert, und **macht aus dem Grund einen Fehler**, wenn einer kommt. Zwei Zeilen — und du kennst jedes Werkzeug darin.

### 10. `else` beim `try` — was nur nach dem Erfolg passieren darf

```python
try:
    verkaufe(ziel, geld)
except AutomatFehler as e:
    print(e)
else:
    zaehler_heute += 1
```

**`else` beim `try` läuft nur, wenn im `try` kein Fehler aufgetreten ist.** Dasselbe Wort wie beim `if`, eine verwandte Bedeutung: *sonst* — also, wenn der `except` nicht zum Zug kam.

**Warum nicht einfach die Zeile mit in den `try`?** Konzept 3: Der `try` soll nur umschließen, was scheitern darf. Stünde `zaehler_heute += 1` im `try`, und würfe irgendwann eine Zeile darin einen `AutomatFehler`, den du dort nicht erwartest — würde er gefangen und als Kundenfehler gemeldet. **Im `else` steht, was nach dem Erfolg passiert, außerhalb des Fangbereichs.**

**Bei dir ist das der Tick.** Ein Befehl, der mit einem `SpielFehler` endet, ist nicht passiert — also vergeht auch keine Zeit. *(Zwei gedeckte Wege dafür: `else`, oder ein Wahrheitswert, den der `except` setzt und nach dem ganzen Block geprüft wird. `else` ist kürzer und sagt, was es meint.)*

### 11. ⭐ Wem gehört ein Fehler?

Du hast ab heute drei Sorten Fehler in deinem Programm, und jede hat einen anderen Adressaten:

| Sorte | Beispiel | Adressat | Was passiert |
|---|---|---|---|
| **Der Spieler hat etwas verlangt, das nicht geht** | *„Dafür reicht dein Vaporium nicht."* | der **Spieler** | `SpielFehler`, an der einen Stelle gefangen, gemeldet, keine Runde |
| **Die Welt hat nicht mitgespielt** | eine kaputte Datei, `drei` statt `3` | der Spieler — *und* du | gefangen, **so eng wie möglich**, mit einer Meldung (20a) |
| **Dein Programm hat einen Fehler** | ein `KeyError` in der Wellenlogik, ein Tippfehler | **du** | **nicht gefangen.** Absturz, Traceback, Fund |

**Die dritte Zeile ist die, an der die meisten Programme falsch werden.** Die Versuchung ist groß, auch dort etwas zu fangen — damit der Spieler nichts Hässliches sieht. **Tu es nicht.** Ein `KeyError` in deiner Wellenlogik ist kein Fehler des Spielers, und eine Meldung wie *„Etwas ist schiefgegangen"* hilft weder ihm noch dir. Er gehört dir, und du findest ihn nur, wenn er laut ist.

**Die Entwicklerfrage dieser Etappe hängt genau hier** — sie steht am Ende.

---

## Dein Auftrag — Teil 20b

---

### 6. Leg `SpielFehler` an

**Eine Klasse `SpielFehler`**, nach Konzept 7: erbt von `Exception`, der Körper ist ein Docstring, der in einem Satz sagt, wofür sie da ist.

**Wohin:** zu deinen anderen Klassen, **vor** die erste. Sie wird überall gebraucht und braucht selbst nichts.

---

### 7. ⭐⭐ Bau die eine Stelle, die fängt

**Such die Stelle in deinem Hauptprogramm, an der ein Befehl des Spielers ausgeführt wird** — seit Etappe 7a ruft sie `verarbeite_befehl()` auf — und die danach entscheidet, ob ein Tick läuft.

- **Leg ein `try` um den Aufruf**, der den Befehl ausführt — nur um ihn.
- **`except SpielFehler as e`:** die Nachricht über `welt.melde()` ausgeben. **Sonst nichts.** Kein Tick, keine Runde.
- **Der Tick** — und alles, was bei dir nur nach einem Befehl passiert, der Zeit kostet — **kommt nach Konzept 10 dorthin, wo er nur nach einem Erfolg läuft.**

⚠️ **Deine Unterscheidung aus Etappe 3b bleibt:** Nicht jeder gelungene Befehl kostet eine Runde — `status` zum Beispiel nicht. Das `else` sagt nur *„der Befehl ist gelungen"*. Ob danach getickt wird, entscheidest du weiter so, wie du es seit Etappe 12 tust.

**So prüfst du es:** Vorübergehend, im Befehl `status`, als erste Zeile `raise SpielFehler("Test")`. Dreimal `status`: dreimal *Test*, **die Rundenzahl bleibt stehen**, kein Absturz. Dann die Zeile wieder weg.

---

### 8. ⭐⭐ Mach aus jedem Abbruch einen Fehler — die Fahndung

**Geh jeden Befehl deiner Befehlsverarbeitung durch** — und die Funktionen, die er aufruft. **Such jede Stelle, an der ein Befehl abbricht, weil etwas gerade nicht geht:** eine Meldung und danach ein `return`, ein `if`, das den Rest überspringt, ein Zweig, der still nichts tut.

**An jeder dieser Stellen: `raise SpielFehler(...)` mit dem Satz, den der Spieler lesen soll.** Die Meldung und das `return` dahinter fallen weg — beides erledigt ab jetzt die Stelle aus Schritt 7.

**Die Stellen, die dein Spiel seit langem mit sich trägt — geh sie mindestens durch:**

| Befehl | Was nicht geht | Seit |
|---|---|---|
| `nimm`, `ablege`, `kaufe`, `lerne` … **ohne zweites Wort** | Das Wort fehlt. *(Prüfen mit `len()`, bevor du auf das zweite Wort zugreifst — Konzept 5.)* | 4 |
| `nimm` | Das Inventar ist voll | 4 |
| `ablege` | Das Ding ist nicht im Inventar. *(Prüfen mit `in` statt `remove()` scheitern lassen.)* | 4 |
| `kaufe` | **Drei** Gründe: keine solche Ware, nicht im Depot, zu wenig Vaporium — **drei verschiedene Sätze** | 5 |
| `verkaufe` | Nichts davon im Vorrat · die Menge aus 20a, Schritt 3 | 5 |
| `gehe` | Keine Richtung angegeben · kein Ausgang in diese Richtung | 5 |
| `schalte frei` | Gibt es nicht · schon freigeschaltet · Voraussetzung fehlt · Vaporium fehlt | 6, 18b |
| `analysiere` | Kein solches Fundstück · schon analysiert | 15 |
| `lerne` | **Der Grund aus `kann_lernen()`** — nach Konzept 9, letzter Absatz | 18b |
| deine Fähigkeit einsetzen | **Der Grund aus `kann_einsetzen()`** — ebenso | 18c |
| ein Wort, das kein Befehl ist | *„Kein gültiger Befehl"* — **ein anderer Satz** als *„geht hier gerade nicht"*, der Unterschied aus Etappe 6 | 3b, 6 |

*(Heißen deine Befehle anders, oder hast du einen dazugebaut, der hier fehlt: Deine Befehlskette ist die Liste, nicht diese Tabelle.)*

⚠️ **Die Regel aus der Design-Entscheidung, an zwei Stellen scharf:**

- **`lerne` und das Einsetzen einer Fähigkeit** werfen im **Befehl** — nachdem sie `kann_lernen()` oder `kann_einsetzen()` gefragt haben. **Nicht** in `lerne()`, `setze_ein()` oder `lerne_selbst()` selbst, wenn die auch von Kameraden aufgerufen werden. Die fragen vorher und bekommen nie einen Fehler zu sehen.
- **`setze_ein()` gibt weiterhin `False` zurück, wenn die Wirkung scheitert** — kein Ziel für die Heilung, keine Mine auf besetztem Feld. Ob dein Befehl daraus einen `SpielFehler` macht, entscheidest du. *(Die Frage dazu: Hat der Spieler etwas verlangt, das nicht ging?)*

⚠️ **Und eine Stelle, an der ein Abbruch kein Fehler ist:** Wo dein Befehl seit Etappe 5 erst **alle** Prüfungen macht und dann erst verändert — die Transaktion —, bleibt das so. **Jedes `raise` steht vor der ersten Veränderung.** Ein Fehler, der nach dem Abbuchen fliegt, hinterlässt einen halben Kauf.

**So prüfst du es:** Zähl vorher, wie viele Stellen du findest. Danach gibt es in deiner Befehlsverarbeitung **keine Zeile mehr, die eine Absage meldet und dann mit `return` aussteigt** — such mit der Suchfunktion deines Editors nach `return` und sieh dir jede Fundstelle an.

**Und einmal den Weg aus Konzept 8, in deinem eigenen Code:** Schreib für `kaufe` ohne Vaporium in `GELERNT.md` auf, welche Funktionen der `SpielFehler` hinaufsteigt, bis er die Stelle aus Schritt 7 erreicht — und welche davon mitten in ihrer Arbeit enden. **Dann prüf deine Vorhersage:** das `try` aus Schritt 7 kurz auskommentieren, `kaufe` ohne Vaporium, den Traceback von unten nach oben lesen. Er muss dieselben Stufen zeigen. Danach das `try` zurück.

---

### 9. Lass die Chaos-Datei noch einmal laufen — und zähl die Runden

- `python spiel.py < chaos.txt > chaos_lauf.txt`. **Die zweite Spalte deiner Chaos-Liste** — was ist davon übrig?
- **Und die Frage aus Etappe 12:** Schreib in `chaos.txt` fünf ungültige Befehle hintereinander, direkt vor einem `status`. **Steht die Rundenzahl danach, wo sie vorher stand?**

*(Das ist die Antwort auf *„ein Tick pro Befehl — auch bei ungültigem Befehl?"*. Etappe 12 hat dich gefragt, ob man sich mit Unsinn Zeit erkaufen kann. In einem Spiel, das nur auf Befehle tickt, erkauft man mit einem Befehl, der nicht passiert, gar nichts — es passiert einfach nichts.)*

---

### 10. Prüf, dass das Alte noch läuft, und commit

- **Der Beweislauf aus 17b** mit `befehle17.txt`, fester Seed, zwei Läufe: `diff` schweigt. **Und ein Blick auf die Ausgabe:** Stehen dort Absagen an Stellen, an denen früher andere standen? Eine andere Formulierung ist kein Fehler — **eine Absage, wo früher ein Befehl gelang, schon.**
- Kaufen, verkaufen, lernen, eine Fähigkeit einsetzen, eine Welle beenden: alles wie vorher, wenn es gelingt.
- **Kein `SpielFehler` wird außerhalb der Befehle des Spielers geworfen.** Such nach `raise` und prüf für jede Stelle: Kann ein Kamerad, ein Tick oder die Pause hierher kommen?
- Keine vorübergehenden `raise`-Zeilen, `chaos_lauf.txt` gelöscht.
- Die Abschnitte am Ende, die zu 20b gehören: **die Leseübung**, **Kaputtmachen 4 bis 7** und **die Entwicklerfrage**.

Commit: `Etappe 20b: Werfen`

---

## Selbsttest — 20b

- [ ] `SpielFehler` erbt von `Exception`, und es gibt genau **eine** Stelle, die ihn fängt.
- [ ] Ein Befehl, der mit einem `SpielFehler` endet, kostet keine Runde.
- [ ] `kaufe` sagt drei verschiedene Sätze für drei verschiedene Gründe.
- [ ] `lerne` zeigt dem Spieler den Grund aus `kann_lernen()` — über einen `SpielFehler`.
- [ ] `lerne_selbst()` und die Kameraden-KI werfen nie.
- [ ] Ein unbekanntes Wort und ein *„geht hier nicht"* ergeben zwei verschiedene Sätze.
- [ ] Jedes `raise` in einem Befehl, der etwas verändert, steht vor der ersten Veränderung.
- [ ] Die Chaos-Liste hat keine offene Zeile mehr — oder jede offene hat einen Satz, warum sie offen bleibt.

> **⏸ Ende von 20b.** Dein Spiel sagt jetzt, was nicht geht, und warum — an einer Stelle, auf einem Weg. 20c schaut in die andere Richtung: auf Fehler, die niemand sehen soll außer dir.

---

# Teil 20c — Prüfen und trennen

## Worum es geht

**20a und 20b handeln von Fehlern, die passieren dürfen.** Diese Portion handelt von denen, die nie passieren dürften — und trotzdem passieren.

Seit Etappe 5 führst du eine Liste. *Munition wird beim Nachladen nie mehr. Jeder Ausrüstungsplatz existiert immer. Jeder gesehene Gegnertyp steht in `GEGNERTYPEN`. Ist `welt.mobiler_turm` nicht `None`, steht er im Trupp.* Und bei jedem Eintrag stand derselbe Nachsatz: **aufgeschrieben, nicht geprüft.** *„Bis Etappe 20"*, sagt der Lehrplan.

Heute werden sie geprüft — bei jedem Takt. Nicht, um dem Spieler etwas zu erklären, sondern um **dir** in dem Moment Bescheid zu sagen, in dem dein Programm etwas tut, was es nach deinen eigenen Regeln nie tun dürfte. Und weil du damit zum ersten Mal eine Sorte Ausgabe hast, die **nur** für dich gedacht ist, bekommt sie einen eigenen Weg — zusammen mit der Debug-Zeile aus Etappe 17b, die seit damals darauf wartet.

---

## Die Konzepte — Teil 20c

Heute in einem Aquarium.

### 12. ⭐⭐ `assert` — eine Behauptung, die nie gefangen wird

```python
def fuettern(becken, menge):
    becken.futter -= menge
    assert becken.futter >= 0, f"Futter negativ: {becken.futter}"
```

`assert` kennst du seit Etappe 7b vom Sehen. **Heute baust du damit.** Die Zeile sagt: *Das hier ist an dieser Stelle wahr — und wenn nicht, ist mein Programm kaputt.* Stimmt die Bedingung, passiert nichts. Stimmt sie nicht, fliegt ein `AssertionError` mit dem Text nach dem Komma.

**Und jetzt der Unterschied zu allem aus 20a und 20b:**

| | `raise SpielFehler(...)` | `assert ...` |
|---|---|---|
| Sagt | *Der Spieler hat etwas verlangt, das nicht geht.* | *Mein Programm hat etwas getan, das nie passieren darf.* |
| Adressat | der Spieler | **du** |
| Wird gefangen | ja, an der einen Stelle | **nie** |
| Wenn es auslöst | Meldung, weiter geht's | Absturz, Traceback, **Fund** |

**Ein `AssertionError` wird nie gefangen.** Er ist kein Fehler, den man behandeln kann — er ist der Beweis, dass irgendwo vorher etwas falsch gerechnet wurde. Wer ihn fängt, hat eine Behauptung, die nichts mehr behauptet.

⚠️ **Und eine Grenze, die du einmal gehört haben musst:** Python kann Behauptungen abschalten — mit `python -O spiel.py` laufen sie gar nicht erst. **Deshalb prüft ein `assert` nie eine Eingabe des Spielers.** Ob `drei` eine Zahl ist, prüft `int()` mit `try`; ob der Spieler genug Vaporium hat, prüft ein `if` mit `raise`. `assert` prüft nur, **was dein eigenes Programm garantieren sollte.**

**Welche deiner Invarianten dafür taugen**, sagt eine Notiz aus Etappe 13: *Invariante und Merksatz getrennt.* „Nie kleiner als `0`" lässt sich prüfen. „Läuft oder ist abgelaufen" nicht. **Nur die prüfbaren werden heute Zeilen.**

### 13. Zwei Sorten Invarianten, zwei Zeitpunkte

**Eine Invariante ist eine Bedingung, die an einer bestimmten Stelle im Programm immer gelten muss.** Das *„an einer bestimmten Stelle"* ist kein Beiwerk: Zwischen den zwei Zeilen, die beim Nachladen Munition vom Lager ins Magazin schieben, stimmt die Summe kurz nicht mit vorher überein — nach der zweiten Zeile wieder. Eine Prüfung genau dazwischen würde einen Fehler melden, den es nicht gibt. **Wo du prüfst, gehört deshalb zur Behauptung dazu.**

Deine Liste enthält zwei Sorten, und sie brauchen verschiedene Stellen:

| Sorte | Beispiel aus deiner Liste | Kann sich ändern, während das Spiel läuft? | Geprüft wird |
|---|---|---|---|
| **Über Tabellen** | Kein Wort steht in `FUNDE` **und** in `AUSBAUTEN` (18b) · jede aktive Fähigkeit steht in `ABKLINGZEITEN` (18c) | nein — Tabellen stehen im Code | **einmal, beim Start** |
| **Über Zustand** | Kein Zähler unter `0` · ein mobiler Turm steht auch im Trupp · jeder gesehene Typ steht in `GEGNERTYPEN` | ja | **nach jedem Tick** |

**Eine Tabellen-Invariante nach jedem Tick zu prüfen, schadet nicht — sie findet nur nie etwas**, weil sich die Tabellen nicht ändern. Beim Start geprüft, fällt ein Tippfehler in einer Tabelle **sofort** auf, bevor die erste Welle kommt. Das ist der Verweis ins Leere aus Etappe 16, Fahndung 9 — ab heute findet ihn dein Programm selbst.

*(Eine Behauptung über **mehrere** Einträge — „jeder gesehene Typ steht in `GEGNERTYPEN`" — ist eine Schleife mit einem `assert` darin. Mehr braucht es nicht.)*

### 14. ⭐ Zwei Adressaten, zwei Wege

Dein Spiel gibt inzwischen zwei Sorten Text aus, und sie haben verschiedene Leser:

| | Beispiel | Für wen | Soll der Spieler es sehen? |
|---|---|---|---|
| **Meldungen** | *„Vasquez: veraetzt vorbei."* · der Wellenbericht | den Spieler | ja |
| **Entwicklerausgaben** | `[ Debug ] Seed: 48173 Welle: 14` · eine vorübergehende Zeile, was im Tick passiert | **dich** | nein — jedenfalls nicht immer |

**Bisher laufen beide über denselben Weg**, `welt.melde()` oder `print()`. Wer die Entwicklerausgaben loswerden will, muss sie suchen und löschen — und wenn er sie wieder braucht, neu schreiben.

**Der übliche Ausweg ist ein Schalter.** Eine Musikschule mit Übungsprotokoll, fremd:

```python
PROTOKOLL = True

def protokolliere(text):
    if PROTOKOLL:
        print(f"[ Protokoll ] {text}")
```

Alle Entwicklerzeilen gehen durch **eine** Funktion. Ein fester Wert oben entscheidet, ob sie erscheinen. **Abschalten heißt eine Zeile ändern, nicht zwanzig suchen.** Und die Zeilen dürfen im Code bleiben — sie sind ab jetzt Werkzeug, nicht Aufräumarbeit.

👀 **Das Werkzeug, das es dafür fertig gibt, heißt `logging`.** In fremdem Code stehen Zeilen wie `logger.warning(...)`, und du sollst sie lesen können:

| Stufe | Heißt | Beispiel bei dir |
|---|---|---|
| `debug` | für Entwickler, im Normalbetrieb aus | *„Gegner 3 rückt auf Feld (4, 2)"* |
| `info` | normaler Ablauf | *„Welle 7 beginnt"* |
| `warning` | ungewöhnlich, läuft aber weiter | *„Spielstand beschädigt, neues Spiel"* |
| `error` | etwas ist fehlgeschlagen | *„Spielstand nicht lesbar"* |

**Der Unterschied zu deinem Schalter ist nur die Zahl der Schalter:** `logging` hat einen pro Stufe, kann in eine Datei schreiben statt auf den Bildschirm und lässt sich einstellen, ohne den Code zu ändern. **Wenn dir ein fremdes Programm scheinbar nichts sagt, sagt es oft etwas — auf einer Stufe, die gerade ausgeschaltet ist.** Das zu wissen erspart dir einmal eine unnötige Fehlersuche.

### 15. 👀 `finally` — und `raise` ohne Fehler dahinter

Zwei Formen, die du in fremdem Code sehen wirst und heute nicht baust.

**`finally`** ist der vierte Teil der Familie:

```python
try:
    bediene_kunden()
finally:
    schliesse_kasse()
```

| Schlüsselwort | Läuft … |
|---|---|
| `try` | als Versuch |
| `except` | wenn der Versuch mit einem passenden Fehler scheitert |
| `else` | wenn der Versuch gelingt |
| `finally` | **danach, in jedem Fall** — nach Erfolg, nach Fehler, sogar nach `return` |

Ein naheliegender Einsatz bei dir wäre ein automatischer Spielstand, wenn das Spiel abstürzt. **Aber sieh dir an, was „in jedem Fall" genau heißt:**

| `finally` läuft | `finally` läuft nicht |
|---|---|
| bei einem Fehler in deinem Programm | wenn jemand das Programm hart beendet — Task-Manager, `kill` |
| bei `return`, `break` | bei Stromausfall oder Systemabsturz |
| bei `Strg + C` | wenn Python selbst abstürzt |

**Die rechte Spalte ist der Grund, warum das atomare Schreiben aus 19c, Konzept 15, nötig bleibt.** `finally` schützt dich vor Fehlern in deinem Programm, nicht vor der Welt. Und ein Autosave, der nach einem Programmfehler läuft, speichert womöglich genau den kaputten Zustand, der den Fehler ausgelöst hat.

> **Eine Zusage gilt unter Bedingungen. Die Frage ist nie *„was verspricht es?"*, sondern *„unter welchen Umständen bricht das Versprechen?"***

**`raise` allein**, ohne Fehler dahinter, in einem `except`-Block, wirft den gerade gefangenen Fehler **weiter** — nachdem man etwas erledigt hat. So sieht fremder Code aus, der einen Fehler nicht verschlucken, aber vorher aufräumen will. Ein Satz, den du sagen können sollst: *„Hier wird gefangen, aufgeräumt und weitergeworfen."*

---

## Dein Auftrag — Teil 20c

---

### 11. ⭐⭐ Prüf deine Invarianten

**Hol deine Invariantenliste aus `GELERNT.md`** — sie ist seit Etappe 5 gewachsen, zuletzt in 18b und 18c. **Streich, was ein Merksatz ist**, nach Konzept 12, letzter Absatz. Was übrig bleibt, teilst du nach Konzept 13 in zwei Gruppen.

**a) `pruefe_tabellen()`** — eine Funktion, **einmal beim Start** aufgerufen, bevor die erste Welle beginnt. Mindestens:

- **Kein Wort in zwei Quellen** — die Invariante aus 18b: Kein Erkenntnis-Wort aus `FUNDE` ist zugleich eine Kennung in `AUSBAUTEN`.
- **Jede aktive Fähigkeit hat ihre Zahlen, kein Passiv hat welche** — aus 18c.

**b) `pruefe_zustand(welt)`** — eine Funktion, **am Ende jedes Ticks** aufgerufen: als letzte Zeile von `Welt.tick()`, nach dem Aufräumen. Mindestens drei aus deiner Liste, zum Beispiel:

- Kein laufender Zähler ist kleiner als `0` — Bauzeit, Ausfall, Abklingzeiten, Effekte.
- Ist `welt.mobiler_turm` nicht `None`, steht er in `welt.trupp` — und umgekehrt steht kein mobiler Turm im Trupp, wenn `welt.mobiler_turm` `None` ist. *(18c)*
- Jeder gesehene Gegnertyp steht in `GEGNERTYPEN`. *(Etappe 6)*
- Jeder Ausrüstungsplatz existiert. *(Etappe 10 — ein Platz ist leer, nie gelöscht.)*

**Jedes `assert` bekommt einen Text**, der im Fall der Fälle sagt, **was** nicht stimmt und **bei wem** — den Namen der Einheit, den Wert. Ein `AssertionError` ohne Text sagt dir nur die Zeile.

⚠️ **Die Invariante aus Etappe 5 — *die Summe aus geladener und gelagerter Munition steigt beim Nachladen nie* — passt in keine der beiden Funktionen.** Sie vergleicht ein Vorher mit einem Nachher, und das gibt es nur **im** Nachladen. Dort gehört sie hin: die Summe vor dem Verschieben merken, danach vergleichen — *merken, neu berechnen, vergleichen* aus Etappe 13, diesmal als Behauptung.

**So prüfst du es:** in der Probedatei. Für jede Invariante: eine Welt so von Hand kaputt machen, dass genau diese Behauptung bricht — einen Zähler auf `-1`, einen mobilen Turm nur in `welt.mobiler_turm` —, die Prüfung aufrufen. **Jede Behauptung knallt mit ihrem eigenen Text.** Und eine unversehrte Welt: keine.

---

### 12. ⭐ Gib den Entwicklerausgaben einen eigenen Weg

Nach Konzept 14.

- **Ein fester Wert `DEBUG`** bei den anderen oben, `True`.
- **Eine Methode `welt.debug(text)`**, die nur ausgibt, wenn `DEBUG` wahr ist — mit einer Vorsilbe, an der man die Zeile sofort erkennt.
- **Die Debug-Zeile aus 17b, Schritt 12** — Seed und Welle — geht ab jetzt über `welt.debug()`.
- **Such nach weiteren Zeilen, die nur für dich da sind** — vorübergehende `print`-Zeilen, die du stehen gelassen hast, `###`-Marker. Was du behalten willst, geht über `welt.debug()`; der Rest fliegt raus.

**`DEBUG` bleibt bei dir auf `True`.** Du bist der Entwickler dieses Spiels, und die Seed-Zeile ist dein Werkzeug seit 17b. Der Punkt ist nicht, sie heute abzuschalten — sondern, dass **eine** Zeile genügt, wenn du es willst.

**So prüfst du es:** `DEBUG = False`, eine Welle spielen: keine Debug-Zeile, alles andere unverändert. Zurück auf `True`.

---

### 13. Prüf, dass das Alte noch läuft, und commit

- **Eine ganze Welle mit allen Fähigkeiten, ohne dass eine Behauptung knallt.** Knallt eine, ist das kein Fehler in 20c — **es ist ein Fund in deinem Spiel**, vielleicht aus einer Etappe, die Wochen zurückliegt. Schreib einen Dreizeiler aus Etappe 16 und such.
- **Der Beweislauf aus 17b** mit `befehle17.txt`: `diff` schweigt — mit `DEBUG` auf `True`, wie bisher.
- **Der Beweislauf aus 19c** mit `befehle19a.txt` und `befehle19b.txt`: weiterhin genau ein Unterschied, ganz oben.
- **Die Chaos-Datei ein letztes Mal**, jetzt mit allen Behauptungen: `python spiel.py < chaos.txt > chaos_lauf.txt`. Knallt eine, hat eine Eingabe aus 20a etwas kaputt gemacht, das dir bisher niemand gesagt hat — **ein Fund, keine Störung.** Trag ihn in die Chaos-Liste ein, als letzte Zeile.
- Keine Probedatei, kein kaputt gemachter Zustand, `chaos.txt` bleibt, `chaos_lauf.txt` nicht.
- Die Abschnitte am Ende, die zu 20c gehören: **Kaputtmachen 8 bis 10**.

Commit: `Etappe 20c: Prüfen und trennen`

---

## Selbsttest — 20c

- [ ] `pruefe_tabellen()` läuft beim Start, `pruefe_zustand(welt)` nach jedem Tick.
- [ ] Jede Behauptung hat einen Text, der sagt, was und bei wem.
- [ ] Nirgends wird ein `AssertionError` gefangen.
- [ ] Kein `assert` prüft eine Eingabe des Spielers.
- [ ] Die Munitions-Invariante aus Etappe 5 steht im Nachladen.
- [ ] Mit `DEBUG = False` erscheint keine Debug-Zeile, und sonst ändert sich nichts.
- [ ] Beide Beweisläufe verhalten sich wie vorher.

---

## Was NICHT in diese Etappe gehört

**Keine Familie eigener Fehlerklassen.** Eine — `SpielFehler` — genügt. Unterklassen wie `ZuWenigVaporium` erkennst du in fremdem Code (Konzept 6); bauen würdest du sie, wenn eine Stelle im Programm **verschiedene** Spielerfehler verschieden behandeln müsste. Deine eine Stelle zeigt sie alle gleich.

**Kein `finally` im Auftrag, kein automatischer Spielstand beim Absturz.** Konzept 15 sagt, warum das weniger schützt, als es aussieht.

**Kein `logging`.** Dein Schalter aus Schritt 12 tut, was du brauchst. `logging` ist das Werkzeug für Programme mit vielen Modulen — Etappe 24.

**Keine Prüfung von Spielstand-Werten beim Laden.** Ob `"kern_integritaet"` eine Zahl ist, prüft Etappe 25 — die *strukturelle* Gültigkeit.

**Kein `try` um den Tick.** Was im Tick schiefgeht, ist dein Fehler, nicht der des Spielers. Er soll laut sein.

---

## Lernziele

**Zu 20a:**

1. Was unterscheidet einen Fehler in deinem Programm von einem Fehler in der Welt — und welcher davon wird behandelt?
2. Was passiert mit den Zeilen im `try`-Block, die **nach** der scheiternden Zeile stehen?
3. **Warum ist `except Exception` gefährlicher als gar kein `except`?** ← die wichtigste
4. Warum gehört nur die eine Zeile in den `try`, die scheitern darf?
5. Wann prüfst du vorher, wann fängst du hinterher — und warum gibt es für *„ist das eine Zahl?"* keine Prüfung vorher?
6. Warum fängt `except ValueError` auch einen `JSONDecodeError`?

**Zu 20b:**

7. Was passiert mit den Funktionen zwischen `raise` und dem passenden `except`?
8. Was ist der Unterschied zwischen `raise SpielFehler(...)` und `return SpielFehler(...)`?
9. Wann liefert eine Funktion einen Grund, wann wirft sie einen Fehler?
10. Warum wirft `lerne_selbst()` nie einen `SpielFehler`?
11. Wozu ist `else` beim `try` da, und warum steht der Tick dort?
12. Warum steht jedes `raise` in einem Befehl vor der ersten Veränderung?

**Zu 20c:**

13. Was unterscheidet `assert` von `raise SpielFehler(...)` — in Adressat, Zweck und darin, ob es gefangen wird?
14. Warum prüft ein `assert` nie eine Eingabe des Spielers?
15. Warum wird eine Tabellen-Invariante beim Start geprüft und nicht nach jedem Tick?
16. Wann läuft `finally` nicht?

---

## 🧠 Die Entwicklerfrage — zu 20b

> **Welchen Fehler zeige ich dem Spieler, welchen dem Entwickler?**

*„Dafür reicht dein Vaporium nicht"* gehört ins Spiel. Ein `KeyError` in der Wellenlogik gehört nicht ins Spiel — **aber verschwinden darf er auch nicht.** Wohin damit?

Und die Fälle dazwischen: Ein Spielstand, der nicht lädt — wessen Fehler ist das? Des Spielers, der die Datei bearbeitet hat? Deiner, weil `aus_daten()` einen Tippfehler hat? Du hast in 20a, Schritt 4, einen Weg gewählt. **Zeigt dein Spiel dem Spieler jetzt etwas, das eigentlich dir gehört — oder dir etwas, das dem Spieler gehört?**

Zwei bis fünf Sätze in `GELERNT.md`. In Etappe 25 kommt dieselbe Frage zurück, für Inhalte, die gar nicht von dir stammen.

---

## Transferaufgabe (15 Minuten) — zu 20a

**Außerhalb des Spiels**, in einer Wegwerf-Datei. Ein Pizza-Bestellautomat, der nie abstürzt:

- Er fragt nach der **Anzahl** — eine ganze Zahl von 1 bis 10.
- Dann nach der **Größe** — `klein`, `mittel` oder `gross`, Groß- und Kleinschreibung egal.
- Dann nach einem **Gutscheincode**, der in einem Dictionary *Code → Rabatt in Prozent* nachgeschlagen wird. Leer heißt: kein Gutschein.
- Am Ende der Preis. Die Preise je Größe stehen in einem zweiten Dictionary.

**Jede ungültige Antwort führt zu einer verständlichen Meldung und derselben Frage noch einmal.**

**Die eigentliche Aufgabe steht darunter:** Schreib neben jede Stelle, an der etwas schiefgehen kann, als Kommentar **„geprüft"** oder **„gefangen"** — und warum. Es sollten beide vorkommen. Und wenn du irgendwo `try` um einen Dictionary-Zugriff geschrieben hast: Hätte `in` es auch getan?

---

## Leseübung — Stufe 3 (15 Minuten) — zu 20b

**Nicht ausführen.** Lesen, beantworten.

```python
TARIFE = {"Nordhafen": 4, "Altstadt": 3, "Flughafen": 9}
RABATTE = {"schueler": 50, "senior": 30}


class AutomatFehler(Exception):
    """Ein Fehler, den der Kunde verursacht hat."""


class Automat:
    def __init__(self):
        self.kasse = 0
        self.verkauft = 0

    def preis(self, ziel, rabatt):
        if ziel not in TARIFE:
            raise AutomatFehler(f"Nach {ziel} fährt von hier kein Zug.")
        grundpreis = TARIFE[ziel]
        if rabatt == "":
            return grundpreis
        return grundpreis * (100 - RABATTE[rabat]) // 100

    def verkaufe(self, ziel, rabatt, geld):
        betrag = self.preis(ziel, rabatt)
        if geld < betrag:
            raise AutomatFehler(f"Es fehlen {betrag - geld} Euro.")
        self.kasse += betrag
        self.verkauft += 1
        return geld - betrag

    def bedienen(self):
        while True:
            ziel = input("Wohin? ").strip()
            rabatt = input("Ermäßigung? ").strip().lower()
            try:
                geld = int(input("Eingeworfen: "))
                rueckgeld = self.verkaufe(ziel, rabatt, geld)
                print(f"Gute Fahrt! Rückgeld: {rueckgeld} Euro.")
            except Exception as e:
                print(f"Fehler: {e}")
```

**Die fünf Fragen**, für `verkaufe` und für `bedienen`:

1. Was kommt rein?
2. Was passiert?
3. Was verändert sich — und woran?
4. Was kommt raus?
5. Welche anderen Objekte oder Funktionen werden dabei aufgerufen?

**Und die Leitfrage von Stufe 3 — warum ist es so gebaut, und was kostet es?**

6. Ein Kunde will nach `Mondstadt`. **Was steht auf dem Bildschirm, und welche Zeilen sind dafür gelaufen?** Zähl die Stufen, die der Fehler hinaufsteigt.
7. Ein Kunde will nach `Altstadt`, **ohne** Ermäßigung, und wirft `2` Euro ein. Was steht auf dem Bildschirm? Hat sich `self.kasse` verändert?
8. **Ein Kunde will nach `Altstadt` mit `schueler`.** Was steht auf dem Bildschirm? *(Lies `preis` Zeile für Zeile. Ganz genau.)* Welche der drei Sorten Fehler aus Konzept 11 ist das — und wem wird er gezeigt?
9. Ein Kunde gibt die Ermäßigung `student` ein. Was steht auf dem Bildschirm, und ist das eine Meldung, die ein Kunde verstehen kann?
10. **Bau `bedienen` im Kopf um**, so, wie Konzept 3 und 11 es verlangen: Welche `except` stehen dort, und für welche Fehlerklassen? Welcher der Fehler aus 8 und 9 soll danach noch laut sein?
11. `rueckgeld` wird gedruckt, obwohl es im `try` berechnet wird. Welche Zeile würdest du nach Konzept 10 woandershin stellen — und wohin?

---

## Kaputtmachen

Jedes Experiment nach dem Ritual: **erst aufschreiben, was passieren wird**, dann ausführen, vergleichen, erklären. Danach wieder reparieren.

**Pflicht:** 1, 4, 7 und 8. Die übrigen, wenn du Zeit hast.

### Zu 20a

**1. ⭐⭐ Fang alles.** Leg um den Aufruf, der einen Befehl ausführt, ein `except Exception as e:` mit `print("Das geht nicht.")`. Bau dann **einen Tippfehler** in einen Befehl — einen Namen, den es nicht gibt. Führ den Befehl aus. **Was siehst du, und was hättest du ohne das `except` gesehen?** Wie lange hättest du gesucht? *(Das ist die Verwandlung aus Etappe 8: Typ 1 wird Typ 3. Danach beides zurück.)*

**2. Mach den `try` zu groß.** In `kaufe`: das `try` nicht nur um das `int()`, sondern um den ganzen Kauf, `except ValueError`. Und dann eine Stelle im Kauf, die selbst einen `ValueError` wirft — ein `remove()` auf etwas, das nicht da ist. **Welche Meldung bekommt der Spieler?**

**3. Vertausch die Reihenfolge.** In `lade_daten()`: ein `except ValueError` **über** dem `except json.JSONDecodeError`, mit einer anderen Meldung. Eine kaputte Datei laden. **Welche Meldung kommt — und warum die?** *(Konzept 6.)*

### Zu 20b

**4. ⭐⭐ Wirf, wo niemand fängt.** In `lerne_selbst()` — da, wo ein Kamerad nichts Lernbares findet — vorübergehend `raise SpielFehler("Nichts zu lernen.")`. Einen Kameraden aufsteigen lassen. **Wo landet der Fehler, und was steht im Traceback?** Lies ihn von unten nach oben — er zeigt den Weg aus Konzept 8. *(Die Design-Entscheidung von 20b, am eigenen Leib.)*

**5. Nimm die eine Stelle weg.** Das `try` um den Befehlsaufruf aus Schritt 7 auskommentieren. `kaufe` ohne Vaporium. **Was passiert?** Und wie viele Stufen hat der Traceback?

**6. Stell den Tick in den `try`.** Statt in den `else`. Dann vorübergehend in das `update()` eines Gegners ein `raise SpielFehler("Test")`. Einen Befehl geben, der Zeit kostet. **Was sieht der Spieler — und wie viel vom Tick ist gelaufen?** *(Das ist Konzept 10. Danach zurück.)*

**7. ⭐ `return` statt `raise`.** In einem der Gründe von `kaufe`: `return SpielFehler("Dafür reicht dein Vaporium nicht.")`. Ohne Vaporium kaufen. **Was passiert — und was passiert mit deinem Vaporium?** Welcher Fehlertyp ist das?

### Zu 20c

**8. ⭐⭐ Fang eine Behauptung.** Leg ein `try` um `pruefe_zustand(welt)`, `except AssertionError:` mit einer Meldung. Dann einen Zähler absichtlich unter `0` rutschen lassen. **Was tut dein Spiel — und was wäre drei Wellen später?** *(Eine Behauptung, die gefangen wird, behauptet nichts mehr.)*

**9. Setz Klammern.** Schreib eine deiner Behauptungen als `assert (bedingung, "Text")` — mit Klammern um beides. Starten. **Was sagt Python beim Start — und was tut diese Zeile danach, auch wenn die Bedingung falsch ist?** *(Ein Tuple mit zwei Einträgen ist truthy — Etappe 2 und 6.)*

**10. Schalte die Behauptungen ab.** `python -O spiel.py`, und in der Probedatei eine Welt mit einem Zähler auf `-1` prüfen. **Was passiert?** Das ist der Grund für Konzept 12, letzter Absatz.

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo nachsehen |
|---|---|---|
| Ein Tippfehler im Code meldet sich als *„Bitte eine Zahl"* | `except` zu breit oder `try` zu groß | Konzept 3 |
| Der Spieler kann das Spiel mit `Strg + C` nicht mehr beenden | Ein nacktes `except:` in einer Schleife | Konzept 3 |
| `except json.JSONDecodeError` kommt nie zum Zug | Ein `except ValueError` steht darüber | Konzept 6 |
| `NameError: name 'SpielFehler' is not defined` | Die Klasse steht unter der Stelle, die beim Start läuft | Schritt 6 |
| Ein ungültiger Befehl kostet trotzdem eine Runde | Der Tick steht nicht im `else` — oder nicht hinter dem Wahrheitswert | Konzept 10, Schritt 7 |
| Ein Befehl, der nicht geht, tut still gar nichts | `return SpielFehler(...)` statt `raise` | Konzept 7, Kaputtmachen 7 |
| Traceback mit `SpielFehler` mitten im Tick | Ein `raise` auf einem Weg, den ein Kamerad oder der Tick nimmt | Design-Entscheidung 20b |
| Nach einer Absage ist trotzdem etwas abgebucht | Das `raise` steht nach der ersten Veränderung | Schritt 8 |
| `IndexError` bei `nimm` ohne zweites Wort | Zugriff auf das zweite Wort vor der Prüfung mit `len()` | Schritt 8 |
| Eine Menge von `-3` wird angenommen | Nach dem Fangen fehlt das Prüfen | Konzept 5, Schritt 3 |
| `SyntaxWarning: assertion is always true` | Klammern um Bedingung und Text | Kaputtmachen 9 |
| `AssertionError` ohne Text | Das Komma und der Text fehlen | Schritt 11 |
| Eine Behauptung knallt nach einer ganz normalen Welle | **Kein Fehler in 20c** — ein Fund in deinem Spiel | Schritt 13, Dreizeiler aus Etappe 16 |
| Die Seed-Zeile ist verschwunden | `DEBUG` steht auf `False` | Schritt 12 |

---

## Ein Blick nach vorne

**Etappe 21a rechnet den Kampf richtig.** Dort kommt eine Formel mit Trefferchance und Panzerung — und drei `assert`-Zeilen, die sagen, was an ihr immer gelten muss. Heute hast du gelernt, wo solche Zeilen hingehören.

**Etappe 21b macht aus deinen Zustandsstrings ein `Enum`.** `"weele"` statt `"welle"` ist heute ein stiller Typ 3. Ein `Enum` macht daraus einen lauten Typ 1 — dieselbe Richtung wie heute, von der Sprache selbst.

**Etappe 24 teilt dein Spiel in Module.** Dort bekommt `SpielFehler` eine eigene Datei, und `logging` wird zum ersten Mal sinnvoller als dein Schalter.

**Etappe 25 lädt Inhalt aus Dateien, die du nicht selbst geschrieben hast.** Heute hast du einen kaputten Spielstand abgefangen. Dort lernst du, einen **gültigen, aber unsinnigen** zu erkennen — `"kern_integritaet": "viel"` aus 19, bevor er drei Züge später knallt.

**Etappe 26 testet.** Deine Chaos-Datei ist dort eine Liste von Testfällen, und ein Test kann sogar prüfen, **dass** ein Fehler fliegt — dass `kaufe` ohne Vaporium einen `SpielFehler` wirft und nichts abbucht.

---

## Abschluss

**In `GELERNT.md`:**

- ⭐⭐ **Deine Chaos-Liste**, mit beiden Spalten und was aus jeder Zeile geworden ist.
- ⭐ Die Regel aus der Design-Entscheidung von 20b: *Ein `SpielFehler` wird nur auf Wegen geworfen, die ein Befehl des Spielers ausgelöst hat.*
- Deine Wahl aus 20a, Schritt 4 — a) oder b) — und ein Satz, warum.
- Ob `FileNotFoundError` bei dir gefangen wird oder vorher geprüft, und warum.
- Wie viele Stellen die Fahndung in Schritt 8 gefunden hat.
- **Deine Invariantenliste**, jetzt mit drei Markierungen: *geprüft beim Start*, *geprüft nach jedem Tick*, *Merksatz*.
- 🧠 Die Entwicklerfrage.
- Was hat mich überrascht? *(Kandidaten: dass eine Menge von `-3` nie abgestürzt ist · wie viele Befehle still gar nichts getan haben · dass eine Behauptung nach Wochen etwas gefunden hat.)*

**Vor dem Commit:** Keine vorübergehenden `raise`- oder Tippfehler-Zeilen? Kein `except Exception`, kein nacktes `except:`? Keine `chaos_lauf.txt`, keine Probedatei? `DEBUG` auf `True`?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest.

**Eine Hilfe, die aus Fehlern lernt.** Führ in der Welt einen Zähler, wie oft hintereinander ein `SpielFehler` kam. Nach dem dritten zeigt dein Spiel von selbst die Liste der Befehle. *(Wo zählst du hoch, und wo setzt du zurück? Die eine Stelle aus Schritt 7 kennt beide Fälle.)*

**Ein Spielstand vor dem Absturz — ehrlich gebaut.** Wer `finally` trotz Konzept 15 ausprobieren will: um die ganze Wellenschleife, und darin ein Speichern in eine **eigene** Datei, `saves/notfall.json` — nie über den echten Spielstand. Dann einen Programmfehler einbauen und nachsehen: **Was steht im Notfall-Spielstand, und würdest du ihn laden wollen?**

**Zwei Fehlerklassen statt einer.** `SpielFehler` für Absagen und eine Unterklasse davon für *„unbekannter Befehl"*, bei der dein Spiel zusätzlich die Liste der Befehle zeigt. Die eine Stelle aus Schritt 7 bekommt dann zwei `except` — **in welcher Reihenfolge?** Konzept 6.
