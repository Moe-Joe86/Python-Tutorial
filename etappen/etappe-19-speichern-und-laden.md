# Etappe 19 — Speichern und Laden

*v1.1.2 · 2026-09-30*

> **Block 3: Der Vorposten reagiert** · Etappe 19 von 30 · [← Etappe 18](etappe-18-faehigkeiten-und-statuseffekte.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 20 →](etappe-20-wenn-der-spieler-unsinn-eingibt.md)

**Neue Syntax heute:** 19a: `import json` und `from pathlib import Path` als Gebrauchsanweisung · `Path("ordner") / "datei.json"` · `.exists()` und `.mkdir(exist_ok=True)` · 🧠 ein relativer Pfad meint den Ordner des Terminals · `with open(pfad, "w", encoding="utf-8") as f:` und dasselbe mit `"r"` · `json.dump(daten, f, ensure_ascii=False, indent=2)` und `json.load(f)` · `sorted(sammlung)` · 🧠 die sechs Dinge, die JSON kennt, und was unterwegs verloren geht — auch dass `[3, 2] == (3, 2)` falsch ist · 🧠 `FileNotFoundError`, `FileExistsError`, `TypeError: Object of type set is not JSON serializable`, `JSONDecodeError` — 19b: `tuple(liste)` · eine Methode, die ein Objekt als Dictionary beschreibt, und ihr Gegenstück, das es daraus wieder füllt · ein Verweis als Stelle in einer Liste · 🧠 das Erzeugen ist die eine Stelle, an der nach dem Typ gefragt werden muss — 19c: `pfad.unlink()` · 🧠 was ein Seed nach dem Laden kann und was nicht · 🧠 ein Wert, der für einen Übergang gemerkt wird, ist Zustand · 🧠 ein halb geschriebener Spielstand · 👀 atomares Schreiben

**Zeitaufwand:** 19a: 5–6 Sitzungen · 19b: 6–7 Sitzungen · 19c: 5–6 Sitzungen, à 20–30 Minuten. Knapp 90 Minuten davon sind Lesestoff — gut 30 in 19a (mit dem Anfang dieser Seite), gut 25 in 19b und gut 30 in 19c, die Abschnitte am Ende jeweils mitgerechnet. **Lies jeweils nur die Portion, an der du sitzt.**

**Voraussetzung:** Etappe 18 abgeschlossen, Selbsttest grün. Du brauchst `welt.flags` und `welt.minen` aus 18, den Befehl `beenden` aus Etappe 3, das Standardargument aus Etappe 7 und 17c, `.index()` aus Etappe 6, `is` aus Etappe 10, das Dictionary *Kennung → Klasse* aus Etappe 11 — **und aus 17b `befehle17.txt`, den Schalter `SEED` und den Beweislauf mit `diff`.**

**Die drei Portionen:**

| | Was passiert | Was danach anders ist |
|---|---|---|
| **19a** | Dateien, JSON und die Zustandsinventur | Eine Datei `saves/spielstand.json` hält die Werte, die es pro Spiel einmal gibt. Du weißt, was sonst noch hineingehört — und was ausdrücklich nicht. |
| **19b** | Objekte werden Daten | Der ganze Trupp, alle Gegner, Minen und Fundstücke stehen im Spielstand — und nach dem Laden ist dein Held wieder *ein* Held und nicht zwei. |
| **19c** | Das Spiel überlebt das Beenden | `beenden` speichert, der nächste Start fragt, ob du weiterspielen willst. Und ein Beweislauf zeigt, dass es nach dem Laden genauso weitergeht, als wäre nichts gewesen. |

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **19a** | `json`, `pathlib`, `with open` · die Welt-Werte speichern und laden · eine Versionsnummer | Serialisierung ist eine Abbildung — und sie verliert etwas · Zustand gegen Inhalt gegen Bild | `pickle` als Alternative |
| **19b** | `als_daten()` und `aus_daten()` an jeder Klasse · Verweise als Stelle · die Rundreise | Warum man ein Objekt nicht zweimal speichern darf · was der Konstruktor wiederherstellt, speichert man nicht | — |
| **19c** | Laden beim Start, weitermachen mitten in der Welle · `beenden` speichert · neu säen beim Speichern · der Beweislauf | Zustand wird gespeichert, Ereignisse nicht · reicht der Seed? · ein halb geschriebener Spielstand | atomares Schreiben |

---

# Teil 19a — Dateien und JSON

## Worum es geht

Starte dein Spiel, spiel bis Welle 12, tipp `beenden`. **Alles ist weg.** Die zwölf Wellen, deine Skillpunkte, die Mine vor dem Nordtor, der halb gebaute Turm.

Das liegt nicht an deinem Code. Es liegt daran, wo Werte wohnen: **Jede Variable, jedes Objekt, jede Liste lebt im laufenden Programm** — im Arbeitsspeicher, solange Python läuft. Endet das Programm, gibt Python den Speicher zurück, und nichts davon bleibt übrig. **Was überdauern soll, muss in eine Datei.**

Das klingt nach einem Handgriff — Datei auf, Werte rein, Datei zu. **Der Handgriff ist tatsächlich klein.** Er ist in 19a in drei Konzepten erledigt. Der Rest dieser Etappe steckt in zwei Fragen, die dir kein Werkzeug abnimmt:

- **Was gehört überhaupt in die Datei?** Nicht alles, was dein Programm kennt, ist Spielzustand.
- **Kommt beim Laden heraus, was du hineingesteckt hast?** Die ehrliche Antwort ist: nein — nicht von selbst.

---

## Der lange Bogen — was heute fällig wird

Diese Etappe hat mehr offene Posten als jede andere vor ihr. **Das ist kein Zufall:** Seit Etappe 1 hat fast jede Etappe irgendwo gesagt *„und das muss später gespeichert werden"*. Heute wird es gespeichert. Die wichtigsten Einlösungen, nach Portion:

**In 19a:**
- **Etappe 1:** *Weltzustand wird gespeichert, nicht nur ausgegeben.* Heute im wörtlichen Sinn.
- **Etappe 4 und 14a:** *Ist die Bahn der Zustand oder nur sein Bild?* Du hast dich damals für Positionen entschieden. Heute zahlt sich das aus: **Nur Zustand wird gespeichert, das Bild nicht.**
- **Etappe 5:** *Ein Dictionary ist eine Zuordnung Schlüssel → Wert — und ein Dictionary im Dictionary ist genau die Form, in der JSON denkt.*
- **Etappe 6:** *Sets und Tuples überleben JSON nicht.* Ein Set kommt gar nicht erst hinein, ein Tuple kommt als Liste zurück. Heute passiert es, und du löst es.
- **Etappe 0:** In `.gitignore` gehört seit dem ersten Abend eine Zeile `saves/`. Heute entsteht der Ordner, den sie meint.

**In 19b:**
- **Etappe 10:** *Zwei Namen, ein Objekt.* Dein Held steht in `welt.trupp` **und** in `welt.held`. Was passiert, wenn man ihn zweimal speichert — und zweimal lädt?
- **Etappe 10:** `None` als bewusster Leerwert — in JSON heißt er `null`. Und: *`.copy()` kopiert nur eine Ebene tief.*
- **Etappe 11:** Das Dictionary *Kennung → Klasse*. Beim Laden baut es deine Objekte aus Wörtern wieder auf.
- **Etappe 18:** Effekte, Abklingzeiten, Skillpunkte, `welt.flags`, die Minen und der mobile Turm, der an zwei Stellen steht.

**In 19c:**
- **Etappe 3:** Der Befehl `beenden` — *„dort wird vor dem Beenden gespeichert"*.
- **Etappe 13:** *„Ist fertig" gegen „wurde gerade fertig".* Welche von beiden Sorten kommt in einen Spielstand?
- **Etappe 17b:** *Reicht es, den Seed zu speichern, um nach dem Laden denselben Zufall zu bekommen?* Deine Antwort steht seit 17b in Konzept 11 bereit.
- **Etappe 5:** *Der Kauf als Transaktion — erst alle Prüfungen, dann verändern.* Beim Speichern heißt die Frage: Was ist mit einer Datei, die mittendrin abbricht?

---

## Eine Design-Entscheidung: Wie wird aus dem Spiel eine Datei? ⭐

**Das Problem:** Dein Spiel besteht aus Objekten, die aufeinander zeigen. Eine Datei ist eine Folge von Zeichen. Irgendwer muss übersetzen. Drei Wege, die in echten Programmen alle vorkommen:

| | A — JSON, von Hand übersetzt | B — `pickle` | C — ein eigenes Textformat |
|---|---|---|---|
| Wie | Jedes Objekt beschreibt sich als Dictionary aus einfachen Werten; das Dictionary wird als JSON-Text geschrieben | Ein Modul, das Python mitbringt, schreibt ganze Objekte samt Verweisen in eine Datei — in einer Zeile | Du erfindest Zeilen wie `held;Soldat;5;5;30` und zerlegst sie beim Laden mit `.split()` |
| Arbeit | viel — jede Klasse braucht zwei Methoden | fast keine | viel, und das Zerlegen ist fehleranfällig |
| Die Datei lesen | im Editor, wie ein Formular | Binärdaten, unlesbar | lesbar, aber nur für dich |
| Du benennst eine Klasse um | der alte Spielstand lädt nicht mehr — **bis du eine Zeile ergänzt**, die das alte Wort auf die neue Klasse abbildet (19b, Konzept 9). Du siehst in der Datei, was fehlt | **der alte Spielstand lädt nicht mehr**, und in die Datei hineinsehen kannst du nicht | wie A |
| Eine fremde Datei laden | harmlos — JSON kann nur Werte enthalten | **gefährlich** — beim Laden kann beliebiger Code laufen | harmlos |

**Der Plan baut A.** Die Begründung steht in der dritten und vierten Zeile: **Ein Spielstand soll dein Programm überdauern** — auch das Programm, das du in drei Wochen umgebaut hast. **Automatisch zukunftssicher ist JSON dabei nicht** — die vierte Zeile zeigt es —, aber es bricht so, dass du siehst, wo, und es mit einer Zeile reparieren kannst. Und du sollst ihn lesen können: Eine JSON-Datei ist ab heute das beste Messgerät deines Spiels, der ganze Zustand auf einen Blick.

👀 **`pickle` sollst du nur erkennen.** Wenn du in fremdem Code `pickle.load(...)` liest, weißt du: Hier werden ganze Objekte geladen — bequem, und nie für Dateien, deren Herkunft man nicht kennt.

⚠️ **Der Preis von A ist die Arbeit, und die ist der Lernstoff.** Wer jede Klasse selbst übersetzen muss, muss für jedes Attribut entscheiden, ob es in den Spielstand gehört. Genau diese Entscheidung ist das, was von dieser Etappe bleibt.

**Schreib einen Satz in `GELERNT.md`**, welchen Weg du ohne diese Tabelle gewählt hättest.

---

## Die Konzepte — Teil 19a

### 1. Zustand, Inhalt, Bild ⭐

Dein Programm kennt drei Sorten Werte, und nur eine davon gehört in einen Spielstand:

| Sorte | Beispiele | Woher kommt es nach dem Neustart? | Speichern? |
|---|---|---|---|
| **Zustand** | Trefferpunkte, Positionen, die Welle, dein Vaporium, die gesetzten Flags | Nur aus dem Spielstand | **ja** |
| **Inhalt** | `GEGNERTYPEN`, `WAREN`, `FAEHIGKEITEN`, die Beschreibungen der Sektoren, das Gelände des Vorfelds | Aus dem Code — er steht dort und wird bei jedem Start neu gelesen | nein |
| **Bild** | das gezeichnete Vorfeld, die Balken, die Statusanzeige | Wird beim Zeichnen aus dem Zustand erzeugt | nein |

**Die dritte Zeile ist der Zahltag für eine Entscheidung aus Etappe 4.** Damals hast du gewählt: Ein Gegner hat eine Position, und das `K` auf der Bahn wird daraus jedes Mal neu gezeichnet. Wäre das `K` der Gegner gewesen, müsstest du heute ein Bild speichern und daraus Gegner zurückrechnen. **So speicherst du Positionen, und das Bild entsteht beim nächsten Zeichnen von selbst.**

**Und die zweite Zeile ist die, an der man sich am leichtesten verschätzt.** Die Versuchung ist groß, einfach alles zu speichern, was im Sektoren-Dictionary steht — Beschreibungen inklusive. Dann steht der alte Beschreibungstext im Spielstand, und wenn du ihn nächste Woche im Code verbesserst, **zeigt jeder alte Spielstand weiter die alte Fassung.** Nichts stürzt ab. Deine Verbesserung wirkt nur nicht. **Inhalt, der im Spielstand steht, überschreibt den Code.**

> **Gespeichert wird Zustand. Inhalt steht im Code. Das Bild entsteht beim Zeichnen.**

### 2. Zwei Werkzeugkästen: `json` und `pathlib`

Für diese Etappe holst du zwei Werkzeugkästen, die Python mitbringt — wie `random` in Etappe 17a. **Und wie dort ist das heute eine Gebrauchsanweisung.** Was `import` genau tut, erklärt Etappe 24.

```python
import random
import json
from pathlib import Path
```

**Die zweite Zeile kennst du vom Muster her:** Danach heißen die Werkzeuge `json.dump`, `json.load` — Kastenname, Punkt, Werkzeug.

**Die dritte Zeile ist eine neue Form.** Aus dem Werkzeugkasten `pathlib` wird nur **ein** Name geholt, `Path`, und der steht danach **ohne** Kastennamen davor im Programm. Du schreibst `Path(...)`, nicht `pathlib.Path(...)`. Mehr musst du dazu heute nicht wissen.

⚠️ **Wohin die Zeilen gehören:** ganz oben in `spiel.py`, alle drei untereinander, vor den festen Werten. Das `import random` aus 17a steht schon dort.

### 3. ⭐ Ein Pfad ist kein String

Ein Ort für eine Datei — ein **Pfad** — sieht aus wie Text mit Schrägstrichen. Er ist aber mehr: Er weiß, ob es ihn gibt, er kann einen Ordner anlegen, und er setzt die Trennzeichen so, wie dein Betriebssystem sie will. Unter Windows ist das ein `\`, sonst ein `/`.

```python
from pathlib import Path

ORDNER = Path("rezepte")
DATEI = ORDNER / "suppen.json"

print(DATEI)              # rezepte/suppen.json   (unter Windows: rezepte\suppen.json)
print(DATEI.exists())     # False, solange es die Datei nicht gibt
ORDNER.mkdir(exist_ok=True)
```

**Drei Dinge daran sind neu:**

- **`Path("rezepte")`** macht aus dem Text einen Pfad. Wie `int("3")` aus Text eine Zahl macht — nur dass hier ein Pfad herauskommt.
- **`/` zwischen einem Pfad und einem Text** hängt ein Stück an. Das ist dasselbe Zeichen wie beim Teilen, und hier bedeutet es etwas anderes, weil links ein Pfad steht. *(`"rezepte" / "suppen.json"` mit zwei Texten gibt `TypeError` — links muss der Pfad stehen.)*
- **`.exists()`** fragt, ob es die Datei oder den Ordner gibt: `True` oder `False`. **`.mkdir(exist_ok=True)`** legt den Ordner an. Ohne `exist_ok=True` gibt es beim zweiten Mal einen `FileExistsError` — der Ordner steht ja schon. Mit `exist_ok=True` heißt es: *„Leg ihn an, und wenn er schon da ist, ist das auch in Ordnung."* Das ist ein Argument mit Namen — dieselbe Form wie `melde(text, sofort=True)` in Etappe 17c, nur an einem fremden Werkzeug.

⚠️ **Und die Frage aus Etappe 7: relativ zu *was*?** `Path("rezepte")` meint den Ordner `rezepte` **dort, wo dein Terminal gerade steht** — nicht dort, wo die `.py`-Datei liegt. Startest du dein Spiel aus einem anderen Ordner, entsteht dort ein zweiter `saves`-Ordner, und dein Spiel findet den alten Spielstand nicht. Das ist der Ortsfehler aus Etappe 7, Konzept 11, nur ohne Fehlermeldung. **Starte das Spiel immer aus dem Projektordner.**

**Warum nicht einfach Text zusammenkleben** — `"rezepte/" + name + ".json"`? Es funktioniert, bis es nicht mehr funktioniert: ein vergessener Schrägstrich, ein doppelter, der falsche unter Windows. Ein Pfad kennt seine eigenen Regeln. **Dieselbe Einsicht wie bei `"40"` gegen `40` in Etappe 1:** Ein Wert, der wie Text aussieht, ist nicht deshalb Text.

### 4. ⭐⭐ Eine Datei öffnen, schreiben, lesen

```python
import json
from pathlib import Path

rezept = {"name": "Linsensuppe", "portionen": 4, "vegan": True, "tipp": None}

with open(Path("suppe.json"), "w", encoding="utf-8") as f:
    json.dump(rezept, f, ensure_ascii=False, indent=2)

with open(Path("suppe.json"), "r", encoding="utf-8") as f:
    geladen = json.load(f)

print(geladen)
print(geladen == rezept)
```

**Lies das von außen nach innen.**

**`with open(pfad, "w", encoding="utf-8") as f:`** öffnet die Datei und gibt dir unter dem Namen `f` einen Griff daran. Alles, was eingerückt darunter steht, darf mit `f` arbeiten. **Wenn der eingerückte Block zu Ende ist, schließt Python die Datei von selbst** — auch dann, wenn darin ein Fehler auftritt. Genau dafür ist `with` da: Du kannst das Schließen nicht vergessen. ⚠️ **Geschlossen heißt nicht vollständig.** Bricht das Schreiben mittendrin ab, schließt `with` eine halbe Datei — ordentlich, aber halb. Das wird in 19c wichtig.

- **`"w"`** heißt *schreiben*. Die Datei wird angelegt, wenn es sie nicht gibt — und **vollständig überschrieben**, wenn es sie gibt. Das kennst du: `> vorher.txt` aus Etappe 7 tut dasselbe.
- **`"r"`** heißt *lesen*. Gibt es die Datei nicht, kommt ein `FileNotFoundError` — ein Typ 1, sofort und ehrlich. Deshalb fragt man vorher mit `.exists()`.
- **`encoding="utf-8"`** legt fest, wie Buchstaben in Bytes übersetzt werden. **Schreib es immer hin**, beim Schreiben und beim Lesen. Ohne die Angabe nimmt Python, was dein Betriebssystem gerade für richtig hält — und unter Windows ist das oft eine andere Übersetzung. Dann schreibt der eine Rechner *„Säuredrüse"* und der andere liest *„SÃ¤uredrÃ¼se"*.

**`json.dump(daten, f, ...)`** schreibt ein Dictionary als JSON-Text in die Datei. Die zwei Angaben mit Namen:

- **`ensure_ascii=False`** — Umlaute bleiben Umlaute. Ohne diese Angabe steht in der Datei `"Säuredrüse"`. Das lädt genauso richtig, ist aber nicht mehr lesbar.
- **`indent=2`** — jeder Eintrag bekommt eine eigene Zeile, eingerückt um zwei Leerzeichen. Ohne diese Angabe steht der ganze Spielstand in **einer** Zeile. Für Python ist das egal. **Für dich nicht:** Mit einer Zeile pro Wert kann `diff` dir in 19b genau sagen, *welcher* Wert sich unterscheidet.

**`json.load(f)`** liest den Text und baut daraus wieder Python-Werte.

**Und so sieht die Datei aus:**

```json
{
  "name": "Linsensuppe",
  "portionen": 4,
  "vegan": true,
  "tipp": null
}
```

Fast Python — aber nur fast. `True` heißt hier `true`, `None` heißt `null`, und alle Texte stehen in doppelten Anführungszeichen. **Die Datei ist kein Python-Code.** Sie ist ein Format, das jede Programmiersprache lesen kann.

### 5. ⭐⭐ Was JSON kennt — und was unterwegs verloren geht

**JSON kennt genau sechs Dinge** — sechs *Werttypen*:

| JSON | Wird beim Laden in Python zu | Kommt her von |
|---|---|---|
| Objekt `{...}` | Dictionary | Dictionary |
| Liste `[...]` | **Liste** | Liste — **und Tuple** |
| Text `"..."` | `str` | `str` |
| Zahl | `int` oder `float` | `int`, `float` |
| `true` / `false` | `True` / `False` | `True` / `False` |
| `null` | `None` | `None` |

**Sieh dir die rechte Spalte genau an. Drei Dinge aus deinem Spiel kommen darin nicht so vor, wie sie hineingegangen sind:**

**Ein Tuple kommt als Liste zurück.** `(3, 2)` wird zu `[3, 2]`. JSON hat keine eigene Form für „unveränderliche Liste". Und das fällt nicht sofort auf — Tuple-Unpacking `a, b = wert` funktioniert mit einer Liste genauso. **Aber:**

```python
print([3, 2] == (3, 2))       # False
```

**Eine Liste ist nie gleich einem Tuple**, auch mit denselben Zahlen darin. Wer eine geladene Adresse mit einem Tuple vergleicht, bekommt `False` — still, ohne Fehler, ein Typ 3. Und in einem Set als Eintrag wird eine Liste gar nicht erst angenommen: `TypeError: unhashable type: 'list'`, Etappe 6, Konzept 5.

**Ein Set kommt gar nicht erst an.** JSON kennt keine Sets, und `json.dump` weigert sich:

```
TypeError: Object of type set is not JSON serializable
```

*serializable* heißt: *in eine Folge von Zeichen übersetzbar*. Das ist der Fachbegriff für das, was du heute baust — **Serialisierung**. Ein Set musst du vor dem Speichern selbst in eine Liste verwandeln, und nach dem Laden wieder zurück — mit `set(liste)` aus Etappe 6.

**Und ein Zahlenschlüssel kommt als Text zurück:**

```python
kapitel = {1: "Vorwort", 2: "Suppen"}
# gespeichert und geladen:
# {"1": "Vorwort", "2": "Suppen"}
```

**JSON-Objekte haben nur Text als Schlüssel.** Aus `1` wird `"1"`, ohne Warnung. Danach findet `kapitel[1]` nichts mehr — `KeyError` —, und `kapitel.get(1)` liefert still `None`. Deine Stufentabelle aus Etappe 5 hat Zahlen als Schlüssel. **Sie ist Inhalt und wird nicht gespeichert** — aber wenn du je ein Dictionary mit Zahlenschlüsseln speicherst, weißt du jetzt, was zurückkommt.

**Und eigene Objekte?** Dieselbe Weigerung wie beim Set: `TypeError: Object of type Marine is not JSON serializable`. Das ist das Thema von 19b.

> **Beim Laden ist nichts automatisch das, was du gespeichert hast.** Was hineingeht, übersetzt du. Was herauskommt, übersetzt du zurück.

**Das ist die Regel aus Etappe 1 eine Ebene höher:** *Woher ein Wert kommt, bestimmt, was du mit ihm tun musst, bevor du ihn benutzt.* Aus `input()` kommt immer Text, und du brauchst `int()`. Aus `json.load` kommt nie ein Set, nie ein Tuple, nie ein Zahlenschlüssel — und du brauchst den Rückweg.

**Der Begriff dahinter ist eine Abbildung mit vier Stationen:**

```
Python-Objekt  →  einfache Werte  →  JSON-Text  →  einfache Werte  →  Python-Objekt
      ↑                                                                    ↓
      └───────────────── Kommt unten an, was oben losging? ────────────────┘
```

Heißt die Antwort *ja*, ist die Abbildung **verlustfrei**. Von selbst ist sie es nicht. **Deine Aufgabe in dieser Etappe ist, sie verlustfrei zu machen** — und in 19b zu beweisen, dass sie es ist.

### 6. `sorted()` — eine Menge bekommt eine Reihenfolge

Ein Set in eine Liste zu verwandeln, geht mit einer Schleife und `.append()`. Es gibt einen kürzeren Weg, und er löst nebenbei ein Problem, das du aus Etappe 17b kennst:

```python
zutaten = {"Salz", "Linsen", "Zwiebel"}
liste = sorted(zutaten)
print(liste)              # ['Linsen', 'Salz', 'Zwiebel']
```

**`sorted(sammlung)`** nimmt eine Sammlung — Liste, Set, die Schlüssel eines Dictionaries — und gibt **eine neue Liste** zurück, sortiert. Texte alphabetisch, Zahlen der Größe nach, Tuples erst nach ihrem ersten Eintrag, bei Gleichstand nach dem zweiten. Die Sammlung selbst bleibt, wie sie war.

**Warum sortiert und nicht irgendwie?** Aus Etappe 17b, Konzept 11: **Die Reihenfolge eines Sets aus Texten kann sich zwischen zwei Programmstarts ändern.** Schreibst du dein Set ungeordnet in die Datei, steht es beim nächsten Speichern vielleicht in anderer Reihenfolge da — derselbe Inhalt, andere Zeilen. **Dann redet `diff`, obwohl sich nichts geändert hat**, und dein Beweis in 19b ist wertlos. Sortiert steht es jedes Mal gleich da.

*(`sorted()` kann noch mehr — nach einer selbst gewählten Regel sortieren. Das ist Etappe 23a. Heute brauchst du die schlichte Form.)*

### 7. ⭐⭐ Die Zustandsinventur

**Das ist das Herzstück von 19a, und es ist kein Code.** Die Frage dahinter ist eine einzige: **Was muss morgen noch genauso sein — und was stellt dein Code beim Start von selbst wieder her?** Bevor du eine Zeile speicherst, gehst du jede Klasse und die Welt durch und stellst zu **jedem Attribut** drei Fragen, in dieser Reihenfolge:

| # | Frage | Wenn ja |
|---|---|---|
| **1** | **Zeigt es auf ein anderes Objekt deines Spiels?** | → **Verweis.** Es wird nicht als Objekt gespeichert, sondern als *Stelle* — das ist 19b. |
| **2** | **Kann es sich im Spiel ändern?** | → **Zustand.** Es muss in den Spielstand. |
| **3** | **Stellt der Konstruktor es beim Erzeugen wieder richtig her?** | → **Inhalt.** Es muss nicht hinein — der Code macht es neu. |

Und ein Rest, der in keine der drei passt: **Was nur zum Anzeigen gesammelt wird und beim nächsten Zeichnen neu entsteht**, ist Bild.

**Der Fall, an dem man sich irrt, ist Frage 2 gegen Frage 3.** Ein Beispiel aus einer Musikschule: Jede Gitarre bekommt im Konstruktor `saiten = 6`. Das stellt der Konstruktor wieder her, also muss es nicht in die Datei — **solange niemand im Laufe des Spiels eine Zwölfsaitige daraus macht.** Sobald irgendwo `gitarre.saiten = 12` steht, hat sich die Antwort auf Frage 2 geändert, und der Wert gehört hinein. Sonst hat die Gitarre nach dem Laden wieder sechs Saiten — und nichts meldet einen Fehler.

> **In den Spielstand gehört jeder Wert, der sich von dem unterscheiden kann, was der Konstruktor hinstellt.**

⚠️ **Und das Gegenstück, weil es genauso teuer ist:** Ein Wert, den du speicherst, obwohl der Konstruktor ihn setzt, schadet zuerst nicht. **Er friert ihn nur ein.** Ändert sich im Code der Startwert, bleibt jeder alte Spielstand beim alten. Das ist Konzept 1 von der anderen Seite.

---

## Dein Auftrag — Teil 19a

Nach **jedem** Schritt ausführen. Deine Spielstand-Datei kannst du dir jederzeit im Editor ansehen — **tu das**. Sie ist ab heute dein Messgerät.

---

### 1. Prüf `.gitignore`

Öffne `.gitignore` aus Etappe 0. **Steht dort `saves/`?** Wenn nicht, trag es ein, in einer eigenen Zeile.

*(Spielstände sind deine persönlichen Daten, keine Programmteile. Wer dein Repo klont, soll ein frisches Spiel bekommen, nicht deinen Lauf bis Welle 12. Dasselbe gilt für `.venv/` und `__pycache__/`, die dort seit dem ersten Abend stehen.)*

**So prüfst du es:** Nach Schritt 7 gibt es einen Ordner `saves`. `git status` darf ihn nicht als neue Datei anbieten.

---

### 2. Probier JSON in einer Wegwerf-Datei aus

**`json_probe.py`**, im Projektordner. Oben die zwei Importzeilen aus Konzept 2 (ohne `random`).

- Bau ein Dictionary über etwas, das nichts mit deinem Spiel zu tun hat — ein Bücherregal, einen Garten, eine Playlist — mit **genau diesen sechs Einträgen**: einem Text mit Umlaut, einer Zahl, einem Wahrheitswert, `None`, einem Tuple aus zwei Zahlen und einem Dictionary mit Zahlen als Schlüsseln.
- Schreib es mit `json.dump` in eine Datei `probe.json`, **mit** `ensure_ascii=False` und `indent=2`. Sieh dir die Datei im Editor an.
- Lies sie mit `json.load` zurück, in einen neuen Namen. **Für jeden der sechs Einträge:** `print(type(...))` — für den geladenen und für den ursprünglichen Wert. Und einmal `print(original == geladen)` für das ganze Dictionary.

**Schreib vorher auf, was du erwartest**, dann ausführen. Das Ritual aus dem Rahmenteil: Vorhersagen, Ausführen, Vergleichen, Erklären.

- **Dann ein siebter Eintrag: ein Set.** Noch einmal speichern. Lies die Fehlermeldung **und sieh danach in `probe.json` nach.** Was steht jetzt darin?

Die letzte Beobachtung brauchst du in 19c. Schreib in `GELERNT.md`, **welche Einträge verändert zurückkamen und was mit der Datei beim Set passiert ist.**

*(`json_probe.py` und `probe.json` sind Wegwerf-Dateien — vor dem Commit löschen.)*

---

### 3. ⭐⭐ Mach die Zustandsinventur

**In `GELERNT.md`, unter der Überschrift *Zustandsinventur*.** Geh jede Klasse deines Spiels durch — `Welt`, `Einheit`, `Marine` und seine vier Unterklassen, `Gegner`, dein Basisturm, `MobilerTurm`, `Mine`, `Item` und seine Unterklassen, `Fundstueck`, `Inventar`, `Ausruestung` — und **jedes Attribut, das in einem `__init__` gesetzt wird**. Pro Attribut eine Zeile mit den drei Fragen aus Konzept 7. **Du musst dafür nicht noch einmal verstehen, wie jedes Attribut funktioniert** — nur, ob es nach einem Neustart noch dieselbe Information tragen muss.

| Klasse | Attribut | Verweis? | Ändert sich? | Stellt der Konstruktor es her? | → |
|---|---|---|---|---|---|
| `Welt` | `seed` | nein | ja — ab 19c bei jedem Speichern | nein | **speichern** |
| `Welt` | `trupp` | ja — Liste von Objekten | ja | nein | **19b** |
| `Gegner` | `schaden` | nein | nein | ja, aus `GEGNERTYPEN` | **nicht** |
| … | … | | | | |

**Diese drei Zeilen sind als Beispiel da.** Den Rest füllst du selbst aus — und bei zwei Sorten Attribut lohnt es sich, genauer hinzusehen:

- ⚠️ **Die Fahndung nach heimlichen Änderungen.** Jeder Kauf aus Etappe 6, jede Erkenntnis aus Etappe 15, jeder Ausbau: **Welches Attribut hat er verändert?** Such die Stellen, an denen ein Attribut **nach** dem `__init__` einen neuen Wert bekommt. Ein Wert, den der Konstruktor setzt und ein Kauf später verändert, ist Zustand — auch wenn er auf den ersten Blick wie Inhalt aussieht.
- ⚠️ **Die Fahndung nach veränderten Tabellen.** Schreibt dein Spiel irgendwo zur Laufzeit in eine GROSS geschriebene Tabelle — etwa, weil eine Erkenntnis eine neue Ware in `WAREN` einträgt? Dann ist dieser Teil der Tabelle Zustand geworden. Zwei gedeckte Wege: den Eintrag beim Laden aus den Flags neu ableiten, oder festhalten, was hinzugekommen ist. **Schreib auf, welchen du nimmst.**

**Und drei Einträge, bei denen die Antwort von deinem Spiel abhängt:**

- **`welt.bericht`** — eine Liste aus Texten, JSON-tauglich. Gespeichert wird in 19c **mitten in einer Welle**. Kann in deinem Spiel mitten in einer Welle schon etwas im Bericht stehen? *(Welche Meldungen hast du in 17c, Schritt 16, dorthin verlegt?)*
- **Der Rundenzähler aus Etappe 3b** — lebt er an der Welt oder als Variable in der Wellenschleife? Wird er angezeigt? Dann wird der Beweislauf in 19c merken, wenn er nach dem Laden wieder bei 1 anfängt.
- **Die Karte `sektoren`** — nach Konzept 1 sind die Beschreibungen Inhalt. Aber seit Etappe 13 kann sich die Karte ändern: Der Osttunnel wird freigeräumt, und wenn du in Etappe 5 die Kür gebaut hast, sinkt die `integritaet` eines Sektors. **Welche Teile eines Sektors können sich bei dir ändern?**

*(Hast du die Kür aus 14b gebaut, gehört `erkundete_felder` in die Liste — ein Set aus Tuples, also gleich zweimal Konzept 5. Hast du 14c gebaut: Wo steht die Barrikade, und hat sie Trefferpunkte?)*

**So prüfst du es:** Jede Klasse aus der Liste oben hat mindestens eine Zeile. Die Spalte ganz rechts ist bei jeder Zeile ausgefüllt: **speichern**, **nicht** oder **19b**. Und du kannst für mindestens ein Attribut sagen, das der Konstruktor setzt und das trotzdem gespeichert werden muss — mit Grund.

*(Das ist der längste Schritt der Portion und vielleicht eine ganze Sitzung. Er ist es wert: Ab Schritt 5 schreibst du nur noch ab, was hier steht.)*

---

### 4. Leg die Grundlagen an

**Ganz oben**, zu `import random`: die Zeilen `import json` und `from pathlib import Path`.

**Bei den festen Werten:**

| Name | Wert |
|---|---|
| `SPEICHERORDNER` | ein Pfad zum Ordner `saves` |
| `SPIELSTAND` | ein Pfad zur Datei `spielstand.json` **im** `SPEICHERORDNER` |
| `SPIELSTAND_VERSION` | `1` |

**Die Versionsnummer ist heute überflüssig — du hast genau ein Format.** Sie steht trotzdem da, und Schritt 7 erklärt, wofür.

---

### 5. ⭐ Bau `Welt.als_daten()`

**Eine Methode der Welt, die ein Dictionary zurückgibt** — die Welt als einfache Werte. Heute nur die Werte, die es pro Spiel einmal gibt; Trupp, Gegner, Minen und Fundstücke kommen in 19b.

- Der erste Eintrag: `"spielstand_version"` mit `SPIELSTAND_VERSION`.
- Dann jedes Attribut der Welt, das deine Inventur mit **speichern** markiert hat und das **kein** Objekt ist. Mindestens: `seed`, `welle`, `zeit`, `kern_integritaet`, `letzte_meldung`, `generatorausfall`, `flags`, `gesehene_gegnertypen` — und `funk_gehoert`, wenn du es in 18b nicht ins Flag-Set umgezogen hast. **`bericht` nur, wenn deine Inventur es so entschieden hat** — eine Liste aus Texten geht, wie sie ist. *(Entschieden hast du danach, ob in deinem Spiel mitten in einer Welle schon etwas darin stehen kann. Der Beweislauf in 19c prüft deine Entscheidung.)*
- **Jedes Set als sortierte Liste**, nach Konzept 6.
- **Die Schlüssel heißen wie die Attribute.** Das ist keine Pflicht, aber es erspart dir ein Wörterbuch im Kopf.

**Und die Karte**, nach deiner Inventur aus Schritt 3: **Ein Eintrag `"sektoren"` mit einem Dictionary *Sektorname → das, was sich an diesem Sektor ändern kann*** — nicht der ganze Sektor. Die Beschreibung bleibt draußen. Welche Teile genau, steht in deiner Inventur. *(Der Sektor `"kern"` hat seit Etappe 5 keine `integritaet` — frag vorher mit `in`, ob der Schlüssel da ist. Und wenn sich bei dir `nachbarn` ändern kann, ist das ein flaches Dictionary aus Texten — JSON-tauglich, so wie es ist.)*

⚠️ **Gib Dictionaries, die in der Welt weiterleben, als `.copy()` hinein**, nicht direkt. Sonst zeigen das Spielstand-Dictionary und die Welt auf dasselbe Dictionary — Etappe 10. Für heute ist das harmlos, weil das Dictionary sofort in die Datei wandert. In 19b nicht mehr. *(`.copy()` gibt es am Dictionary genauso wie an der Liste.)*

**So prüfst du es:** Im Spiel, an einer beliebigen Stelle mitten in einer Welle, vorübergehend `print(welt.als_daten())`. Jedes Set steht als Liste da, alphabetisch. **Kein** `{...}` ohne Doppelpunkt darin — das wäre ein Set, das durchgerutscht ist.

---

### 6. ⭐ Bau `speichere_spiel(welt, pfad=SPIELSTAND)`

**Eine Funktion**, oben bei deinen anderen Funktionen — nicht im Hauptprogramm, nicht in der Welt:

- Den Ordner anlegen, nach Konzept 3.
- **Zuerst** das Dictionary bauen, mit `welt.als_daten()`, und unter einem Namen ablegen.
- **Danach** die Datei öffnen und schreiben, nach Konzept 4, mit beiden Angaben.
- Über `welt.melde()` Bescheid geben, dass gespeichert wurde.

**Warum ein Standardargument für den Pfad?** Weil du in 19b in eine **andere** Datei speichern willst, ohne einen einzigen Aufruf von heute anzufassen — Etappe 7, Konzept 6.

⚠️ **Warum erst das Dictionary und dann die Datei?** Deine Beobachtung aus Schritt 2, letzter Punkt. Schreib die Antwort in einem Satz in `GELERNT.md`. In 19c kommt sie wieder.

*(Die Funktion wohnt außerhalb der Welt, weil sie mit einer Datei redet und die Welt nicht. Deine Welt weiß, was sie ist — wohin sie geschrieben wird, entscheidet jemand anderes. Dieselbe Trennung wie zwischen Logik und Darstellung aus Etappe 7b.)*

---

### 7. ⭐ Bau `lade_daten(pfad=SPIELSTAND)`

**Eine Funktion, die das geladene Dictionary zurückgibt — oder `None`.** Drei Fälle, und für jeden steht fest, was zurückkommt:

| Fall | Meldung | Rückgabe |
|---|---|---|
| Die Datei gibt es nicht | *Kein Spielstand gefunden.* | `None` |
| Die Datei gibt es, aber ihre `"spielstand_version"` ist nicht `SPIELSTAND_VERSION` | eine, die beide Zahlen nennt | `None` |
| Alles in Ordnung | keine | das Dictionary |

**Die Meldungen hier mit `print()`** — `lade_daten` kennt keine Welt, weil beim Laden noch keine fertige da ist.

**Das ist der Grund für die Versionsnummer.** In Etappe 22 ziehst du deine Tabellen zusammen, in 25 kommt Inhalt aus Dateien — und irgendwann passt ein Spielstand von letzter Woche nicht mehr zu deinem Programm von heute. **Ohne Versionsnummer** bekommst du dann mitten im Laden einen `KeyError` und weißt nicht, ob dein Code kaputt ist oder die Datei alt. **Mit ihr** sagt dein Spiel: *„Dieser Spielstand ist Version 1, ich verstehe Version 2."* Sobald sich das Format deines Spielstands ändert, erhöhst du `SPIELSTAND_VERSION` um eins.

*(Eine kaputte Datei — ein fehlendes Komma, ein abgeschnittenes Ende — gibt beim `json.load` einen `JSONDecodeError`, und dein Spiel stürzt ab. **Das ist heute in Ordnung.** Einen Absturz sauber abzufangen ist Etappe 20. Heute ist er ein ehrlicher Typ 1.)*

**So prüfst du es:** in einer Probedatei. `lade_daten()` ohne Spielstand — `None` und die Meldung. Dann nach Schritt 9 noch einmal, mit Datei.

---

### 8. ⭐ Bau `Welt.aus_daten(daten)`

**Das Gegenstück zu `als_daten()`:** Eine Methode, die eine **bestehende** Welt mit den Werten aus einem geladenen Dictionary überschreibt. Sie gibt nichts zurück.

- Für jeden Eintrag, den `als_daten()` schreibt, eine Zeile, die ihn zurückholt — **außer** `"spielstand_version"`, die hat `lade_daten` schon geprüft.
- **Jede Liste, die ein Set war, wird wieder ein Set** — Etappe 6.
- **Die Karte:** Für jeden gespeicherten Sektor die gespeicherten Teile zurück in **den bestehenden** Sektor schreiben. Die Beschreibung hat der Konstruktor der Welt schon hingestellt, und sie bleibt.

⚠️ **Warum *eine bestehende Welt überschreiben* und nicht *eine neue bauen*?** Weil der Konstruktor der Welt all das hinstellt, was Inhalt ist — Gelände, Sektorbeschreibungen, die leere `bericht`-Liste. `aus_daten` legt nur den Zustand darüber. **Erst erzeugen, dann überschreiben** — und in 19b gilt dasselbe für jede Einheit.

---

### 9. ⭐ Mach die erste Rundreise und bau den Befehl `speichern`

**Der Befehl `speichern`** ruft `speichere_spiel(welt)` auf. **Er kostet keine Runde** — er ändert nichts am Spiel, die Unterscheidung aus Etappe 3b. *(Ab 19c stimmt der zweite Halbsatz nicht mehr ganz. Warum, steht dort in der Design-Entscheidung.)* *(Einen Spielstand laden kann dein Spiel erst in 19c. Heute schreibst du ihn nur — und er ist noch unvollständig, das ist Absicht.)*

**Dann die Rundreise, in einer Probedatei** — `spiel.py` als `probe.py` kopiert, das Hauptprogramm durch Prüfzeilen ersetzt, wie seit Etappe 9:

- Eine Welt anlegen, einige Werte von Hand setzen: eine Welle, einen Kern unter 100, zwei Wörter in `flags`, einen Generatorausfall.
- Speichern. Die Datei im Editor ansehen.
- **Eine zweite, frische Welt** anlegen, mit `lade_daten()` und `aus_daten()` füllen.
- Für jeden gespeicherten Wert: `print(alt == neu)`.

**Jede Zeile `True`.** Auch bei den Flags, obwohl die Datei eine Liste enthält — denn beim Laden ist es wieder ein Set, und zwei Sets sind gleich, wenn sie dieselben Einträge haben, egal in welcher Reihenfolge.

**Dann von Hand kaputtmachen:** In `saves/spielstand.json` die Versionsnummer auf `0` setzen, speichern, laden. **Die Meldung aus Schritt 7, keine Welt.** Danach wieder auf `1`.

---

### 10. Prüf, dass das Alte noch läuft, und commit

- Ein Spiel über zwei Wellen, einmal `speichern` mittendrin: Das Spiel läuft danach normal weiter, **keine Runde vergeht**, und die Datei steht in `saves`.
- `git status` bietet `saves` nicht an.
- Keine `json_probe.py`, keine `probe.json`, keine `probe.py`.
- Die Abschnitte am Ende, die zu 19a gehören: **Transferaufgabe** und **Kaputtmachen 1 bis 3**.

Commit: `Etappe 19a: Dateien und JSON`

---

## Selbsttest — 19a

- [ ] `saves/spielstand.json` lässt sich im Editor lesen: eine Zeile pro Wert, Umlaute als Umlaute.
- [ ] Kein Set steht als Set im Dictionary von `als_daten()`, und jede Liste, die aus einem Set entstand, ist alphabetisch.
- [ ] Die Beschreibungen der Sektoren stehen **nicht** in der Datei.
- [ ] Die Rundreise aus Schritt 9 ergibt für jeden Wert `True`.
- [ ] `lade_daten()` gibt ohne Datei `None` zurück, mit falscher Version ebenfalls — und beide Male eine Meldung.
- [ ] Der Befehl `speichern` kostet keine Runde.
- [ ] Deine Zustandsinventur steht in `GELERNT.md`, jede Zeile mit einer Entscheidung.
- [ ] Du kannst ein Attribut nennen, das der Konstruktor setzt und das trotzdem in den Spielstand muss.

> **⏸ Ende von 19a.** Deine Welt weiß, was sie ist, und kann es aufschreiben. Ihre Bewohner noch nicht — das ist 19b.

---

# Teil 19b — Objekte werden Daten

## Worum es geht

Probier es aus, bevor du weiterliest — zwei Zeilen, vorübergehend, irgendwo mitten in einer Welle:

```python
with open(Path("x.json"), "w", encoding="utf-8") as f:
    json.dump(welt.trupp, f)
```

```
TypeError: Object of type Soldat is not JSON serializable
```

*(Dein Klassenname steht da. Lösch die Zeile und die Datei `x.json` danach wieder.)*

**JSON kennt sechs Dinge, und dein Marine ist keines davon.** Er ist ein Objekt: ein Bündel aus Werten, dazu ein Bauplan — seine Klasse mit ihren Methoden —, dazu Verweise auf andere Objekte, ein Inventar, vielleicht eine Mine, die ihm gehört. Von diesen drei Dingen kann eine Datei nur das erste aufnehmen.

**Heute bringst du jedem Objekt bei, sich selbst als Dictionary zu beschreiben** — und aus einem Dictionary wieder zu werden, was es war. Das sind zwei kleine Methoden pro Klasse. Die eigentliche Arbeit steckt woanders: **in den Verweisen.** Dein Held steht an zwei Stellen, der mobile Turm auch, und jede Mine zeigt auf ihren Engineer. Wer das naiv speichert, lädt ein Spiel, in dem es deinen Helden zweimal gibt — und merkt es erst, wenn er Schaden nimmt, den die Anzeige nicht zeigt.

---

## Der lange Bogen — was heute fällig wird

- **Etappe 10, der Kern dieser Portion:** *Zwei Namen, ein Objekt.* Damals ein Fehler, den man vermeiden sollte. Heute eine Eigenschaft deines Spiels, die ein Spielstand **erhalten** muss.
- **Etappe 10:** `None` als bewusster Leerwert. Der leere Ausrüstungsplatz, `welt.mobiler_turm` ohne Turm — in der Datei heißt er `null`, und er kommt als `None` zurück.
- **Etappe 10:** *`.copy()` kopiert nur eine Ebene tief.* Heute der Moment, an dem das zählt.
- **Etappe 11b:** das Dictionary *Kennung → Klasse* und `type(self).__name__`. Beim Speichern schreibt jedes Objekt seinen Klassennamen auf, beim Laden wird daraus wieder eine Klasse.
- **Etappe 11c und 15:** *Wo entstehen `Item`s?* Heute an einer Stelle mehr — und die Antwort ist: auf demselben Weg wie immer.
- **Etappe 12:** *Die Aufräumphase — nur Aufgeräumtes wird gespeichert.* Gespeichert wird zwischen zwei Takten, nie mitten in einem. Ein Gegner mit `status = "tot"` steht deshalb nie im Spielstand.
- **Etappe 13 und 18:** jeder laufende Zähler — Ausfall, Nachladen, Bauzeit, Aufstellzeit, Lebensdauer, Abklingzeiten, Effekte.
- **Etappe 14a:** Position als `x` und `y`, Tuples für Adressen — und die Zone aus 14b ist ein Tuple.
- **Etappe 15:** `welt.fundstuecke` — was liegen geblieben ist, liegt nach dem Laden noch da.

---

## Eine Design-Entscheidung: Wie zeigt ein gespeichertes Objekt auf ein anderes? ⭐⭐

**Das Problem:** Dein Held steht in `welt.trupp`, und `welt.held` zeigt auf **dasselbe Objekt**. Eine Mine hat einen `besitzer`, und das ist einer der Marines aus `welt.trupp`. Im Speicher ist das *ein* Objekt mit mehreren Namen. In einer Datei gibt es keine Namen, die auf etwas zeigen — nur Text.

| | A — das Objekt noch einmal speichern | B — die Stelle speichern | C — einen Namen speichern |
|---|---|---|---|
| Was in der Datei steht | `"held": {"klasse": "Soldat", "name": "Du", …}` — der ganze Held, ein zweites Mal | `"held": 0` — *der Held ist der erste im Trupp* | `"held": "Du"` — *der Held ist der, der „Du" heißt* |
| Nach dem Laden | **zwei** Helden: einer im Trupp, einer unter `welt.held` | ein Held, zwei Namen — wie vorher | ein Held, zwei Namen — wenn der Name eindeutig ist |
| Was schiefgehen kann | Schaden trifft den einen, angezeigt wird der andere. **Stürzt nie ab.** | Die Reihenfolge des Trupps ändert sich zwischen Speichern und Laden | Zwei Einheiten heißen gleich — zwei Basistürme, zwei Kameraden gleichen Namens |

**Der Plan baut B.** Die Reihenfolge des Trupps ändert sich zwischen Speichern und Laden nicht, weil du selbst in derselben Reihenfolge speicherst und lädst. Die Stelle eines Werts in einer Liste findest du mit `.index()` aus Etappe 6, und zurück kommst du mit `liste[stelle]`. **Das ist alles, was B braucht.**

**C ist nicht falsch** — in Etappe 25 wirst du Inhalte über Kennungen verbinden, und dort ist es genau richtig, weil eine Kennung eindeutig *gemacht* wird. **Die Namen deiner Einheiten sind es nicht:** Niemand hat je geprüft, ob zwei gleich heißen.

**A ist falsch, und genau deshalb steht es da.** Es ist die Lösung, die sich von selbst ergibt, wenn man jedes Objekt einfach als Dictionary hinschreibt. **Kaputtmachen 5 lässt dich sie einmal bauen.**

---

## Die Konzepte — Teil 19b

### 8. ⭐⭐ Ein Objekt beschreibt sich selbst

Jede Klasse bekommt zwei Methoden, die zusammengehören wie `speichere_spiel` und `lade_daten`:

- **`als_daten(self)`** gibt ein Dictionary zurück — das Objekt als einfache Werte.
- **`aus_daten(self, d)`** nimmt ein solches Dictionary und **überschreibt** damit die Attribute eines schon erzeugten Objekts.

Ein fremdes Beispiel, eine Musikschule:

```python
class Instrument:
    def __init__(self, name):
        self.name = name
        self.gestimmt = False
        self.ausleihen = 0

    def als_daten(self):
        return {"klasse": type(self).__name__, "name": self.name,
                "gestimmt": self.gestimmt, "ausleihen": self.ausleihen}

    def aus_daten(self, d):
        self.gestimmt = d["gestimmt"]
        self.ausleihen = d["ausleihen"]


class Gitarre(Instrument):
    def __init__(self, name):
        super().__init__(name)
        self.saiten = 6
        self.kapodaster = None

    def als_daten(self):
        d = super().als_daten()
        d["saiten"] = self.saiten
        d["kapodaster"] = self.kapodaster
        return d

    def aus_daten(self, d):
        super().aus_daten(d)
        self.saiten = d["saiten"]
        self.kapodaster = d["kapodaster"]
```

**Drei Dinge daran sind der Lernstoff:**

- **Die Unterklasse ruft zuerst die Fassung der Oberklasse** — mit `super()`, Etappe 11, Konzept 8 — und legt danach nur dazu, was bei ihr anders ist. `als_daten` bekommt das Dictionary der Oberklasse zurück und ergänzt es, `aus_daten` lässt die Oberklasse ihren Teil holen und holt dann den eigenen. **Kein Attribut steht an zwei Stellen.**
- **`name` steht in `als_daten`, aber nicht in `aus_daten`.** Warum? Weil der Name schon beim Erzeugen gebraucht wird — `Gitarre(d["name"])` —, und danach ist er da. Konzept 9 sagt, wo das Erzeugen passiert.
- **Die beiden Methoden sind Spiegelbilder.** Jeder Schlüssel, den `als_daten` schreibt, wird in `aus_daten` gelesen — außer denen, die das Erzeugen schon verbraucht hat. Fehlt einer auf einer Seite, merkst du es: Fehlt er beim Lesen, bleibt der Konstruktorwert stehen. Fehlt er beim Schreiben, gibt es beim Laden einen `KeyError`.

⚠️ **Die Falle, die keiner merkt: Fehlt ein Attribut auf *beiden* Seiten, merkst du nichts.** Die Datei ist vollständig in sich, das Laden läuft durch — nur hat das Objekt nach dem Laden wieder seinen Konstruktorwert. Dagegen hilft keine Methode, nur die Inventur aus 19a. Und der Beweislauf in 19c.

### 9. Das Wort für die Klasse — und die eine Stelle, an der man nach dem Typ fragt

**Beim Speichern** schreibt jedes Objekt seinen Klassennamen auf: `type(self).__name__`, Etappe 11. Das steht einmal in der Oberklasse und gilt für alle Unterklassen — eine Gitarre schreibt `"Gitarre"`, obwohl die Zeile in `Instrument` steht.

**Beim Laden** muss aus dem Wort wieder eine Klasse werden. Das Werkzeug dafür kennst du aus Etappe 11b — eine Klasse als Wert in einem Dictionary:

```python
INSTRUMENTE = {"Gitarre": Gitarre, "Geige": Geige, "Trommel": Trommel}

for d in geladen["instrumente"]:
    neu = INSTRUMENTE[d["klasse"]](d["name"])
    neu.aus_daten(d)
    schule.instrumente.append(neu)
```

**Erst erzeugen, mit dem, was der Konstruktor braucht. Dann überschreiben.** Dieselbe Reihenfolge wie bei der Welt in 19a, Schritt 8.

⚠️ **Wohin das Dictionary gehört:** **unter** die letzte Klasse, die darin vorkommt. Steht es darüber, gibt es beim Start einen `NameError` — die Klasse gibt es an dieser Stelle noch nicht. Dieselbe Regel wie für `def` aus Etappe 7, Konzept 1.

🧠 **Und eine Beobachtung, die sich anfühlt wie ein Widerspruch.** Seit Etappe 11 fragt dein Programm nie, *welche Klasse* ein Objekt hat — es ruft auf, und das Objekt weiß Bescheid. **Hier fragst du doch.** Das ist kein Rückfall: **Beim Erzeugen gibt es noch kein Objekt, das man fragen könnte.** Es gibt nur ein Wort in einer Datei. Die Frage *„was soll ich bauen?"* muss jemand beantworten, und das ist die einzige Stelle im Programm, an der die Antwort in den Daten steht statt im Objekt.

**Brauchen deine Klassen verschiedene Argumente** — die Marines einen Namen, der mobile Turm dazu eine Position und eine Stufe —, dann funktioniert ein einziger Aufruf `KLASSEN[...](d["name"])` nicht für alle. **Zwei gedeckte Wege:** ein Dictionary für die Klassen, die gleich erzeugt werden, und ein `if`/`elif` über `d["klasse"]` für die übrigen — oder für jede Sorte ein eigener Zweig. **An genau dieser Stelle ist eine Kette über Klassennamen in Ordnung.** Sie steht einmal, beim Erzeugen, und nirgends sonst.

⚠️ **Der Klassenname ist heute auch die Kennung im Spielstand.** Das ist einfach und hat einen Preis: Benennst du `Soldat` in `Frontsoldat` um, findet das Dictionary das alte Wort nicht mehr, und jeder alte Spielstand bricht mit `KeyError`. Die Reparatur ist eine Zeile — das alte Wort zeigt zusätzlich auf die neue Klasse. **In größerer Software trennt man die beiden meist von Anfang an:** ein festes Wort für die Datei, ein frei änderbarer Name für die Klasse. Für heute reicht, dass du weißt, dass es zwei Dinge sind.

### 10. ⭐⭐ Ein Verweis wird eine Stelle

Eine Bibliothek, wieder fremd: Ein Buch ist an einen Leser ausgeliehen, und `buch.ausgeliehen_an` zeigt auf dieses Leser-Objekt. Derselbe Leser steht in `bibliothek.leser`.

**Speichern:** Statt des Lesers steht im Buch seine Stelle in der Leserliste.

```python
{"titel": "Moby Dick", "ausgeliehen_an": bibliothek.leser.index(buch.ausgeliehen_an)}
```

Ist das Buch nicht ausgeliehen, steht dort `None` — in der Datei `null`. **Sag für diesen Fall ausdrücklich, was hineinkommt**, sonst ruft `.index(None)` nach einem Leser, den es nicht gibt, und du bekommst `ValueError: None is not in list`. Etappe 6.

**Laden, in zwei Durchgängen:**

1. **Erst alle Leser erzeugen**, in der gespeicherten Reihenfolge, und in die Liste hängen.
2. **Dann die Bücher** — und jedes bekommt seinen Leser über `bibliothek.leser[stelle]` zurück, oder `None`, wenn `null` gespeichert war.

**Die Reihenfolge der Durchgänge ist nicht verhandelbar.** Wer ein Buch laden will, bevor es Leser gibt, zeigt auf eine leere Liste — `IndexError`.

**Und der Beweis, dass es geklappt hat,** ist das Werkzeug aus Etappe 10:

```python
print(buch.ausgeliehen_an is bibliothek.leser[2])     # True
```

`is` fragt, ob es **dasselbe Objekt** ist — nicht, ob zwei Objekte gleiche Werte haben. Zwei getrennt geladene Leser mit demselben Namen sind `==` vielleicht, aber nie `is`. **Genau diesen Unterschied soll dein Spielstand erhalten.**

### 11. Was der Konstruktor weiß, speichert man nicht

Ein `Item` hat eine Kennung und einen Anzeigenamen. Der Anzeigename kommt seit Etappe 11c aus `ANZEIGENAMEN` — **er ist Inhalt.** Speicherst du ihn mit, steht in jedem alten Spielstand der alte Name, auch wenn du ihn im Code längst verbessert hast. Konzept 1, am kleinsten Beispiel.

**Also speicherst du von einem Item nur die Kennung** — und beim Laden entsteht es **auf demselben Weg wie beim Kaufen**: Kennung rein, fertiges Item raus, mit Namen und richtiger Klasse. In der Musikschule hieße das: Die Noten eines Schülers stehen im Spielstand als `["mondscheinsonate", "fuer_elise"]`, und beim Laden baut dieselbe Funktion daraus die Notenblätter, die sie auch beim Kauf gebaut hätte.

> **Speicher, was sich nicht herleiten lässt. Erzeug alles andere auf dem Weg, auf dem es immer entsteht.**

**Der Gewinn ist größer, als er aussieht:** Gibt es nur **einen** Weg, auf dem ein Item entsteht, kann es auch nur einen Fehler dabei geben — und den findest du beim Kaufen genauso wie beim Laden.

### 12. Drei Kleinigkeiten: `null`, `.copy()` und `tuple()`

**`None` wird `null` und kommt als `None` zurück** — die einzige Übersetzung, die ohne Verlust klappt. Ein leerer Ausrüstungsplatz aus Etappe 10 bleibt leer, und `if platz is None:` funktioniert nach dem Laden wie vorher.

**`.copy()` kopiert eine Ebene.** Gibst du in `als_daten` ein Dictionary wie `self.effekte` als `.copy()` hinein, hat das Spielstand-Dictionary ein eigenes. **Für flache Dictionaries reicht das** — Name → Zahl, Richtung → Ziel. Bei einem Dictionary aus Dictionaries — wie deiner Karte — kopiert `.copy()` nur die äußere Hülle; die inneren Dictionaries sind danach weiterhin geteilt. **Deshalb hast du in 19a aus der Karte nur die veränderlichen Teile herausgezogen**, statt sie zu kopieren.

*(Beim Laden ist es umgekehrt harmlos: Was `json.load` liefert, ist frisch gebaut und gehört niemandem sonst. Das geladene Dictionary darfst du direkt übernehmen.)*

**Und der Rückweg für ein Tuple:**

```python
fach = tuple([3, 2])
print(fach)              # (3, 2)
```

**`tuple(liste)`** macht aus einer Liste ein Tuple — dasselbe wie `set(liste)` aus Etappe 6, nur mit anderem Ergebnis. Deine Zone aus Etappe 14b ist ein Tuple, und nach dem Laden ist sie eine Liste. Tuple-Unpacking funktioniert mit beiden. **Ein Vergleich mit `==` gegen ein Tuple nicht** — Konzept 5.

---

## Dein Auftrag — Teil 19b

Nimm deine Zustandsinventur aus Schritt 3 daneben. **Ab hier schreibst du ab, was dort steht.** Wo du beim Bauen merkst, dass die Inventur falsch war: erst die Inventur verbessern, dann den Code.

---

### 11. ⭐⭐ Bau `als_daten()` und `aus_daten(d)` in `Einheit`

Nach Konzept 8.

- **`als_daten()`** gibt ein Dictionary zurück. Der erste Eintrag: `"klasse"` mit dem Klassennamen. Dann jedes Attribut von `Einheit`, das deine Inventur mit **speichern** markiert hat.
- **`aus_daten(d)`** überschreibt jedes dieser Attribute mit dem gespeicherten Wert — **außer** denen, die der Konstruktor beim Erzeugen braucht und die Konzept 9 deshalb schon übergibt.
- **Das Effekt-Dictionary aus 18a als `.copy()`**, nach Konzept 12.

⚠️ **Welche Attribute mindestens dabei sind**, weil jede Einheit sie seit Etappe 12 bis 18 hat: Position, Trefferpunkte, Status, Effekte, Abschüsse — und `abschuesse_bei_wellenbeginn` aus 17c. Gespeichert wird in 19c mitten in einer Welle, und dein Wellenbericht rechnet mit diesem Wert.

**So prüfst du es:** In der Probedatei eine Einheit erzeugen, ein paar Werte ändern — Position, Trefferpunkte, einen Effekt —, `als_daten()` ausgeben. **Dann eine zweite, frische Einheit derselben Klasse erzeugen, `aus_daten()` mit dem Dictionary der ersten aufrufen und beide mit `print()` ausgeben.** Dasselbe `__repr__`, zweimal.

---

### 12. ⭐ Überschreib beide in `Marine`

Nach Konzept 8, das Gitarren-Muster: `super()` zuerst, dann dazu, was nur ein Marine hat.

Deine Inventur sagt, was das ist. **Eine Checkliste, gegen die du sie prüfst:**

| Seit Etappe | Attribut | Achtung |
|---|---|---|
| 3c, 9a | Erfahrung, Stufe | **Beide** — warum auch die Stufe, obwohl sie aus der Erfahrung folgt, klärt 19c |
| 5, 13 | der Vorrat, das Magazin | Ein Dictionary — `.copy()` |
| 5, 9 | der Sektor, in dem er steht | |
| 6 | alles, was ein Kauf verändert hat | Deine Fahndung aus Schritt 3 |
| 10 | Inventar, Ausrüstung | **Schritt 14** — hier nur ein Platzhalter |
| 11 | ob er gesteuert wird | |
| 13 | Ausfall, Nachladen | laufende Zähler |
| 14b | seine Zone | **Ein Tuple** — beim Laden mit `tuple()` zurück |
| 18 | Skillpunkte, Fähigkeiten, Abklingzeiten | Zwei Dictionaries — `.copy()` |

*(Deine vier Unterklassen `Soldat`, `Heavy`, `Engineer`, `Medic` haben vermutlich keine eigenen Attribute, die sich ändern — dann brauchen sie keine eigene Fassung. Der Klassenname steht trotzdem richtig im Dictionary, Konzept 9.)*

**So prüfst du es:** wie in Schritt 11, mit einem Marine. **Und ein Wert mehr:** Setz vor dem Speichern die Zone auf ein anderes Tuple und prüf nach dem Laden `print(neu.zone == alt.zone)`. `True` — nur mit `tuple()`.

---

### 13. Gib den übrigen Einheiten ihre Fassung

**Jede Unterklasse von `Einheit`, die eigene veränderliche Attribute hat**, überschreibt beide Methoden nach demselben Muster:

- **`Gegner`** — hat er etwas, das sich ändert und nicht in `Einheit` steht? *(Sein Schaden kommt aus `GEGNERTYPEN` und ändert sich nicht — deine Inventur.)*
- **Dein Basisturm aus Etappe 13** — Bauzeit, ob er schon aktiv ist.
- **`MobilerTurm` aus 18c** — Aufstellzeit und Lebensdauer.

**Kein Attribut wird zweimal geschrieben:** Was `Einheit` schon schreibt, schreibt die Unterklasse nicht noch einmal.

---

### 14. ⭐ Bring Inventar und Ausrüstung in den Spielstand

Nach Konzept 11.

**a) Ein Weg, auf dem Items entstehen.** Such die Stellen, an denen in deinem Spiel ein `Item` erzeugt wird — `kaufe`, `nimm`, die Einsammelphase. **Steht das Erzeugen dort jeweils ausgeschrieben** — Kennung nachschlagen, Klasse aus dem Dictionary aus Etappe 11c, Namen aus `ANZEIGENAMEN` —, dann zieh es jetzt in **eine** Funktion, die eine Kennung bekommt und das fertige Item zurückgibt, und lass alle Stellen sie aufrufen. **Das ist ein reiner Umbau:** Danach tut `kaufe` genau dasselbe wie vorher.

**b) Das Inventar-Objekt aus Etappe 10** bekommt `als_daten()`, das **eine Liste der Kennungen** zurückgibt, und `aus_daten(liste)`, das für jede Kennung über deine Funktion aus a) ein Item erzeugt und einfügt.

*(Liegen in deinem Inventar auch Fundstücke aus Etappe 15, und weiß deine Funktion aus a) nicht, wie man eines erzeugt? Dann speicher für ein solches Item zusätzlich, was deine Funktion nicht aus der Kennung herleiten kann — und lass dem Laden einen Zweig dafür. Das ist dieselbe Regel, nur zweimal angewandt.)*

**c) `Ausruestung` aus Etappe 10** — die Plätze sind seit Etappe 10 leer, weil es keinen Befehl gibt, der sie füllt. **Ein Dictionary aus `None`-Werten ist JSON-tauglich, so wie es ist** — `.copy()` hinein, beim Laden übernehmen. *(Steht bei dir doch ein Item in einem Platz, gilt die Regel aus b): nur die Kennung.)*

**d) In `Marine`**: Inventar und Ausrüstung über ihre eigenen Methoden in das Dictionary, und beim Laden zurück. **`Marine` weiß nicht, wie ein Inventar gespeichert wird — das Inventar weiß es.**

**So prüfst du es:** In der Probedatei zwei Items ins Inventar eines Marines, speichern, laden. Beide sind da, mit **Anzeigenamen**, obwohl der Name nicht in der Datei steht — sieh nach.

---

### 15. ⭐⭐ Erweitere `Welt.als_daten()` um die Bewohner

Nach Konzept 10 und der Design-Entscheidung. **Sieben neue Einträge:**

| Eintrag | Was darin steht |
|---|---|
| `"trupp"` | eine Liste: für jede Einheit in `welt.trupp` ihr `als_daten()`, **in der Reihenfolge der Liste** |
| `"held"` | die **Stelle** des Helden in `welt.trupp` |
| `"turm"` | die Stelle deines Basisturms im Trupp — oder `None`, wenn es keinen gibt *(heißt dein Attribut anders, nimm deinen Namen)* |
| `"mobiler_turm"` | dasselbe für den mobilen Turm aus 18c |
| `"gegner"` | eine Liste: für jeden Gegner sein `als_daten()` |
| `"fundstuecke"` | eine Liste: für jedes Fundstück in `welt.fundstuecke` Kennung und Position |
| `"minen"` | eine Liste: für jede Mine Position, Schaden — **und die Stelle ihres Besitzers im Trupp** |

⚠️ **Für jeden Verweis, der `None` sein kann: erst fragen, dann `.index()`.** Konzept 10, der Satz über `ValueError`.

⚠️ **Steht dein Basisturm noch nicht im Trupp, solange er gebaut wird?** Dann hat er in dieser Zeit keine Stelle, und du speicherst ihn als eigenes Dictionary unter `"turm"` — er steht ja nur an **einer** Stelle, `welt.turm`. **Die Stelle braucht nur, was an zwei Stellen steht.** Prüf, was bei dir gilt, und schreib es in die Inventur.

*(Die Mine ist keine `Einheit` und kennt den Trupp nicht. Ob sie ihr eigenes `als_daten` bekommt, dem du die Stelle des Besitzers übergibst, oder ob die Welt ihre drei Werte selbst zusammenstellt, entscheidest du. **Wer die Liste kennt, schreibt die Stelle** — das ist in beiden Fällen die Welt.)*

---

### 16. ⭐⭐ Erweitere `Welt.aus_daten()` um die Bewohner

Nach Konzept 9 und 10. **In genau dieser Reihenfolge:**

1. **Der Trupp.** `welt.trupp` wird eine neue leere Liste. Für jedes gespeicherte Dictionary: die Klasse bestimmen, erzeugen, `aus_daten()`, anhängen. Das Dictionary *Klassenname → Klasse* steht **unter** deiner letzten Klasse — Konzept 9.
2. **Die Verweise in den Trupp:** `welt.held`, dein Basisturm, `welt.mobiler_turm` — über die Stelle, oder `None`.
3. **Die Gegner**, wie der Trupp, in eine neue leere Liste.
4. **Die Fundstücke**, auf dem Weg, auf dem sie in Etappe 15 entstehen.
5. **Die Minen** — zuletzt, weil ihr Besitzer aus dem fertigen Trupp kommt.

⚠️ **„Eine neue leere Liste", nicht die alte leeren.** Der Konstruktor deiner Welt hat vielleicht schon etwas hineingelegt — und selbst wenn nicht, ist eine neue Zuweisung eindeutig. Etappe 17c, Schritt 17, hat dasselbe mit `self.bericht` gemacht.

**So prüfst du es:** in der Probedatei, nach dem Laden, drei Zeilen:

- `print(welt.held is welt.trupp[...])` — mit der Stelle, die im Spielstand steht.
- Dasselbe für eine Mine und ihren Besitzer, wenn du eine hast.
- `print(len(welt.trupp))` — **genau so viele wie vorher.** Einer mehr heißt: Irgendwo wurde ein Objekt zweimal geladen.

---

### 17. ⭐⭐ Mach die Rundreise — und frag, was sie beweist

**Ein Entwicklerbefehl `rundreise`** — erlaubt seit Etappe 3a, vor dem Commit wieder weg. Er kostet keine Runde und tut vier Dinge:

1. Die laufende Welt speichern — **nach `saves/vorher.json`**, über das Standardargument aus Schritt 6.
2. Eine **frische** Welt anlegen und mit `lade_daten(...)` aus `saves/vorher.json` und `aus_daten()` füllen.
3. Diese frische Welt speichern — **nach `saves/nachher.json`**.
4. Ausgeben, ob der Held der frischen Welt `is` der Einheit an seiner Stelle im Trupp ist.

**Dann, mitten in einer Welle — mit Gegnern auf dem Feld, möglichst einer Mine, einem laufenden Effekt, einem mobilen Turm:** `rundreise` eintippen. Das Spiel beenden, im Projektordner:

```
diff saves/vorher.json saves/nachher.json
```

**`diff` muss schweigen.** Beide Dateien sind aus demselben Spiel entstanden — einmal direkt, einmal nach Speichern und Laden. Jede Zeile, in der sie sich unterscheiden, ist ein Wert, den dein Laden anders hinstellt, als dein Speichern ihn aufgeschrieben hat. *(Unter Windows in der klassischen Eingabeaufforderung: `fc`. Beide Dateien entstehen von selbst und werden bei jedem `rundreise` überschrieben.)*

**Redet `diff`, lies die Zeile:** Sie nennt den Schlüssel, der sich unterscheidet. Meist ist es eine der drei Sorten: ein Wert, den `aus_daten` vergisst zu lesen; eine Liste, die beim Laden kein Set wurde und beim zweiten Speichern ohne Sortierung herauskommt; ein Tuple, das als Liste zurückkam.

⚠️⭐ **Und dann die wichtigste Frage dieser Portion, schriftlich in `GELERNT.md`: Was beweist die Rundreise *nicht*?**

*(Nimm ein Attribut aus beiden Methoden heraus — aus `als_daten` **und** aus `aus_daten` — und mach die Rundreise noch einmal. Kaputtmachen 7. Danach wieder hinein.)*

Die Antwort ist der Grund, warum es 19c gibt.

---

### 18. Prüf, dass das Alte noch läuft, und commit

- Kaufen, einsammeln, Fähigkeit einsetzen, eine Welle beenden: alles wie vorher? **Der Umbau aus Schritt 14 a) darf nichts verändert haben.**
- `speichern` schreibt jetzt den ganzen Spielstand. Sieh dir die Datei einmal ganz an — es ist dein ganzes Spiel, auf ein paar hundert Zeilen.
- **Der Entwicklerbefehl `rundreise` ist gelöscht**, `saves/vorher.json` und `saves/nachher.json` auch. Keine `probe.py`.
- Die Abschnitte am Ende, die zu 19b gehören: **die Leseübung** und **Kaputtmachen 4 bis 7**.

Commit: `Etappe 19b: Objekte werden Daten`

---

## Selbsttest — 19b

- [ ] Jede Klasse, die eigene veränderliche Attribute hat, überschreibt `als_daten` und `aus_daten` — und ruft in beiden zuerst `super()`.
- [ ] Kein Attribut wird in zwei Fassungen derselben Methode geschrieben.
- [ ] Nach dem Laden ist `welt.held is welt.trupp[stelle]` wahr — ebenso für den mobilen Turm und jede Mine mit ihrem Besitzer.
- [ ] `len(welt.trupp)` ist nach dem Laden so groß wie vorher.
- [ ] Im Spielstand steht von einem Item nur die Kennung — und nach dem Laden hat es seinen Anzeigenamen.
- [ ] Es gibt **eine** Funktion, die aus einer Kennung ein Item macht, und `kaufe` benutzt sie.
- [ ] Die Zone ist nach dem Laden ein Tuple.
- [ ] ⭐ Die Rundreise mitten in einer Welle: `diff` schweigt.
- [ ] Du kannst sagen, was die Rundreise nicht beweist.

> **⏸ Ende von 19b.** Dein ganzes Spiel passt in eine Datei, und es kommt heraus, wie es hineinging — soweit du es hineingetan hast. 19c macht es spielbar und beweist den Rest.

---

# Teil 19c — Das Spiel überlebt das Beenden

## Worum es geht

Dein Spiel kann sich aufschreiben. **Es kann sich noch nicht wieder aufnehmen** — und das ist mehr als ein Aufruf von `aus_daten()` an der richtigen Stelle.

Denk an das, was beim Laden alles *nicht* passieren darf: Die Klassenwahl darf nicht noch einmal kommen. Das Briefing aus Etappe 1 nicht. Die Welle, mitten in der du gespeichert hast, darf nicht neu erzeugt werden — dann stünden die alten Gegner und eine frische Welle gleichzeitig auf dem Feld. Und dein Marine darf beim nächsten Abschuss nicht noch einmal alle Skillpunkte bekommen, die er schon ausgegeben hat.

**Und dann die Frage, auf die 19b hingearbeitet hat:** Die Rundreise hat bewiesen, dass Speichern und Laden zueinander passen. Sie hat nicht bewiesen, dass sie **vollständig** sind. Dafür gibt es nur einen Beweis: **Das Spiel nach dem Laden muss genau so weitergehen wie ohne.** Zug um Zug, Würfelwurf um Würfelwurf. Und damit steht die Frage aus Etappe 17b auf dem Tisch: *Reicht der Seed dafür?*

---

## Der lange Bogen — was heute fällig wird

- **Etappe 3a und 3b:** der Befehl `beenden` und die Knobelstelle *Abbruch von innen nach außen*. Heute wird vorher gespeichert.
- **Etappe 13, Konzept 2:** Die Meldung steht **innerhalb** des `> 0`-Blocks, damit aus einem Zustand ein Ereignis wird. Heute zahlt sich das doppelt aus — beim Laden.
- **Etappe 13:** *„Ist fertig" gegen „wurde gerade fertig".* Das eine kommt in den Spielstand, das andere nicht.
- **Etappe 16:** die Tick-Reihenfolge in `GELERNT.md`. Sie steht nicht im Spielstand — und genau deshalb wird nur zwischen zwei Takten gespeichert.
- **Etappe 17b, Konzept 11:** *Der Seed legt die Folge fest, nicht, wer wann eine Zahl daraus nimmt.* Heute die Antwort auf *„Reicht der Seed?"*
- **Etappe 17b:** der Beweislauf mit `diff`. Heute in seiner schärfsten Form: ein Lauf mit Pause gegen einen Lauf ohne.
- **Etappe 17c:** *Deine Zufallsregeln* in `GELERNT.md` — *„die Liste holst du in Etappe 19 wieder hervor."* Eine Regel darin ändert sich heute.
- **Etappe 5:** *Der Kauf als Transaktion.* Beim Speichern heißt sie: erst alle Daten, dann die Datei.

---

## Eine Design-Entscheidung: Reicht der Seed? ⭐⭐

**Das Problem, an einem Beispiel:** Du spielst mit Seed 48173 bis Welle 9, Zug 4, und speicherst. Bis dahin hat dein Spiel 212 Zahlen aus der Folge genommen — für Wellen, Beute, Ereignisse. **Nach dem Laden setzt du `random.seed(48173)`.** Welche Zahl kommt als nächste?

**Die erste der Folge. Nicht die 213.** Konzept 11 aus 17b: Der Seed legt fest, wo die Folge *beginnt* — nicht, wo du gerade in ihr stehst. Nach dem Laden würfelt dein Spiel also Zahlen, die es in Welle 1 schon einmal gewürfelt hat. Das stürzt nicht ab und fühlt sich nicht falsch an. **Aber es ist nicht der Lauf, den du ohne Speichern gehabt hättest** — und damit kann kein Beweis zeigen, dass dein Spielstand vollständig ist.

Drei Wege:

| | A — hinnehmen | B — die Stelle in der Folge speichern | C — beim Speichern neu säen |
|---|---|---|---|
| Wie | Nach dem Laden mit dem gespeicherten Seed säen und damit leben, dass es anders weitergeht | `random` kann seinen inneren Zustand herausgeben — einen Wert, aus dem sich genau die Stelle in der Folge wiederherstellen lässt | Beim Speichern einen **neuen** Seed ziehen, ihn sofort setzen und speichern. Beim Laden genau diesen setzen |
| Nach dem Laden | ein anderer Lauf | derselbe Lauf | derselbe Lauf **ab dem Speichern** |
| Preis | Kein Beweis möglich | Der Zustand ist ein Tuple mit über sechshundert Zahlen darin — Konzept 5 lässt grüßen — und ein Werkzeug, das dieser Plan nicht einführt | Eine Regel aus 17b muss neu gefasst werden |

**Der Plan baut C.** Der Trick daran: **Speichern wird zu einem neuen Anfang der Folge**, und dieser Anfang steht in der Datei. Ob du nach dem Speichern weiterspielst oder das Spiel beendest und morgen lädst — beide Male wird ab derselben Stelle mit derselben Folge weitergewürfelt.

> **Du speicherst damit nicht den Zustand des Zufalls. Du entscheidest, dass beim Speichern ein neuer Zufallsabschnitt beginnt.**

**Und das hat eine Folge, die man leicht übersieht:** Wer speichert, würfelt danach anders, als er ohne Speichern gewürfelt hätte. `speichern` ändert also doch etwas am Spiel — nicht den Zustand, den du siehst, aber die Zukunft des Zufalls. Das ist für dieses Spiel in Ordnung und ein Grund mehr, dass ein Beweislauf immer beide Läufe *mit* derselben Speicherstelle vergleicht.

⚠️ **Und die Regel aus 17b, Konzept 10?** Dort stand: *„`random.seed()` einmal, am Anfang, und nie wieder."* Der Grund war: **Nie auf einen Anfang zurücksetzen, den es schon gab** — sonst beginnt jede Welle mit denselben Würfen. **Weg C setzt nicht zurück, sondern auf einen neuen Anfang**, der selbst gewürfelt ist und im Spielstand steht. Die Regel heißt ab heute genauer:

> **Gesät wird am Anfang eines Spiels, beim Speichern und beim Laden — jedes Mal mit einem Seed, der im Spielstand steht oder gleich hineinkommt. Nie mitten im Lauf auf einen alten.**

👀 *(Weg B existiert und ist in manchen Programmen genau richtig. Wenn du in fremdem Code `random.getstate()` liest, weißt du, was dort gespeichert wird.)*

---

## Die Konzepte — Teil 19c

### 13. ⭐⭐ Zustand wird gespeichert, Ereignisse nicht

Etappe 13 hat dir zwei Sorten beigebracht: **Zustand** gilt, solange er gilt — `aktiv = True`, `lebensdauer = 3`. **Ereignisse** passieren einmal, am Übergang — *„der Turm steht"*, *„Stufe 3 erreicht"*.

**Ein Spielstand ist ein Foto. Auf einem Foto gibt es nur Zustand.** Ein Ereignis ist auf keinem Foto zu sehen — es ist die Veränderung *zwischen* zwei Fotos. Das hat zwei Folgen, und beide musst du kennen:

**Erstens — was dich schützt:** Deine Zähler aus Etappe 13 melden sich **innerhalb** des `> 0`-Blocks. Ein gespeicherter Zähler, der auf `0` steht, meldet sich deshalb nach dem Laden nicht noch einmal — er ist ja nicht mehr größer als null. **Hättest du die Meldung damals eine Ebene weiter links geschrieben**, würde jeder fertige Turm nach dem Laden noch einmal *„fertig!"* rufen. Etappe 13, Kaputtmachen, noch einmal — diesmal mit einem Grund mehr.

**Zweitens — was dich erwischt:** Manche Ereignisse erkennt dein Programm, indem es **einen gemerkten Zustand mit einem neu berechneten vergleicht.** Etappe 13, Konzept 4: *merken, neu berechnen, vergleichen.* Dein Stufenaufstieg funktioniert so: alte Stufe merken, aus der Erfahrung die neue berechnen, und ist sie höher, gibt es Skillpunkte. **Der gemerkte Wert ist Zustand, auch wenn er sich aus einem anderen herleiten lässt.** Eine Musikschule, fremd:

```
Gespeichert:   übungsstunden = 60          (die Urkunde für 50 Stunden hat er schon)
Nicht gespeichert: urkunden = 1
Nach dem Laden: urkunden = 0   (Konstruktor)
Nächste Stunde: 61 Stunden, Urkunden laut Rechnung: 1, gemerkt: 0  →  Urkunde!  Noch einmal.
```

**Ein abgeleiteter Wert, der für einen Übergang gemerkt wird, gehört in den Spielstand** — sonst wiederholt sich nach dem Laden ein Ereignis, das schon passiert ist. Das ist die Antwort auf die Klammer in Schritt 12 der Checkliste.

**Und eine Frage aus dem Lehrplan, die hierher gehört:** Speicherst du von einem Zähler den **Rest** (*„noch 23 Takte"*) oder den **Fortschritt** (*„seit 17 Takten"*)? Deine Zähler aus Etappe 13 zählen herunter, also steht der Rest da. Das hat eine Folge, die du erst in Etappe 22 spürst: **Änderst du dort eine Bauzeit, läuft ein gespeicherter Bau mit seinem alten Rest weiter.** Mit Fortschritt würde er sich an die neue Bauzeit anpassen. Keins von beiden ist falsch — aber du sollst wissen, welches du hast.

**Und warum nur zwischen zwei Takten gespeichert wird:** Die Reihenfolge deines Ticks aus Etappe 16 steht im Code, nicht im Spielstand. **Mitten in einem Takt** gespeichert, wüsste niemand, welche Phasen schon gelaufen sind — nach dem Laden liefen sie noch einmal. Deine Befehle kommen immer zwischen zwei Takten, und deshalb ist der Befehl `speichern` von selbst an der richtigen Stelle. Genau deshalb steht auch nie ein Gegner mit `status = "tot"` im Spielstand: Die Aufräumphase ist immer schon gelaufen.

### 14. ⭐ Zwei Wege ins Spiel, ein Weg hindurch

Bis heute beginnt dein Spiel immer gleich: Briefing, Klassenwahl, Trupp aufstellen, Welt anlegen, Seed, Wellenschleife ab Welle 1. **Ab heute gibt es einen zweiten Anfang**, und die beiden müssen sich an einer Stelle treffen:

```
Start
 │
 ├─ Neues Spiel:  Briefing → Klassenwahl → Trupp → Welt → Seed ziehen und setzen ─┐
 │                                                                                  ├──→  Wellenschleife ab der Startwelle
 └─ Geladen:      Welt anlegen → aus_daten() → Seed aus dem Spielstand setzen ─────┘
```

**Treffpunkt ist die Wellenschleife**, und sie braucht eine Angabe, die bisher fest war: **bei welcher Welle sie anfängt.** Beim neuen Spiel bei `1`, nach dem Laden bei der gespeicherten Welle. Dass die Startzahl einer Schleife ein Wert sein kann statt einer festen Zahl, weißt du seit 17b — dort hast du sie für den Beweislauf auf `8` gestellt.

⚠️ **Die gespeicherte Welle läuft schon.** Gespeichert wird mitten in einer Welle, und beim Laden stehen ihre Gegner schon auf dem Feld. **Also darf der Wellenstart für diese eine Welle nicht alles tun, was er sonst tut.** Welche der vier Dinge aus 17c, Schritt 20 — Debug-Zeile, Welle erzeugen, Abschüsse merken, Ankündigung — noch einmal passieren dürfen, entscheidest du in Schritt 22 nach einer einzigen Frage: **Verändert es den Zustand, oder zeigt es ihn nur?**

**Und woran erkennt der Wellenstart, dass er mitten in eine Welle geraten ist?** Nicht an einer neuen Variable. **Am Zustand selbst:** Zu Beginn einer frischen Welle ist das Feld leer — die letzte Welle endete, weil kein Gegner mehr da war. Stehen beim Wellenstart Gegner auf dem Feld, wurde geladen.

### 15. 🧠 Ein halb geschriebener Spielstand

Deine Beobachtung aus Schritt 2 in 19a: `json.dump` hat angefangen zu schreiben, ist am Set gescheitert — **und die Datei war danach halb.** Die alte Datei war schon weg, denn `"w"` leert die Datei beim Öffnen. Die neue war nie fertig.

**Ein halber Spielstand ist schlimmer als keiner.** Keiner heißt: neues Spiel. Ein halber heißt: `JSONDecodeError` beim nächsten Start — und zwölf Wellen sind verloren, obwohl du gespeichert hast.

**Die erste Verteidigung hast du in 19a, Schritt 6, schon gebaut:** erst das ganze Dictionary, dann die Datei. Scheitert `als_daten()` — ein Attribut, das es nicht gibt, ein Tippfehler in einem Namen —, ist die Datei noch nicht angefasst, und der alte Spielstand steht unversehrt da. **Das ist der Kauf als Transaktion aus Etappe 5:** erst alle Prüfungen, dann verändern.

**Gegen ein Set, das durchrutscht, hilft es nicht.** `als_daten()` baut das Dictionary klaglos — ein Set darf in einem Dictionary stehen. Erst `json.dump` merkt es, und da ist die Datei schon offen und geleert. Kaputtmachen 3 lässt dich das erleben.

**Gegen eines hilft das nicht:** Stromausfall, Absturz des Rechners, ein `kill` genau während der Millisekunden, in denen geschrieben wird. Auch dann bleibt eine halbe Datei zurück.

👀 **Die übliche Lösung heißt *atomares Schreiben*, und sie ist zwei Handgriffe lang:** erst in eine **andere** Datei schreiben — etwa `spielstand.tmp` —, und wenn die fertig ist, sie über die alte **umbenennen**. Umbenennen ist für das Betriebssystem ein einziger, unteilbarer Schritt: Danach steht entweder die alte Datei da oder die neue, nie eine halbe. **Du baust das heute nicht** — es steht unter *Wenn du mehr willst*. Du sollst es wiedererkennen, wenn du in fremdem Code eine `.tmp`-Datei und ein Umbenennen direkt hintereinander siehst.

*(In Etappe 20 lernst du `finally` — einen Block, der auch bei einem Fehler noch läuft. **Er hilft gegen Programmfehler, nicht gegen einen Stromausfall.** Deshalb bleibt atomares Schreiben nötig, auch wenn du `finally` kennst.)*

---

## Dein Auftrag — Teil 19c

**Vor dem ersten Schritt:** Nimm `befehle17.txt` aus Etappe 17b zur Hand. Ab Schritt 20 stellt dein Spiel eine Frage mehr, ganz am Anfang — und jede Befehlsdatei braucht dafür eine Zeile mehr.

---

### 19. ⭐⭐ Säe beim Speichern neu

Nach der Design-Entscheidung, Weg C. **In `speichere_spiel()`, als Erstes — vor `als_daten()`:**

- Einen neuen Seed ziehen, eine Zahl von 1 bis 99999, wie in 17b, Schritt 11.
- Ihn in `welt.seed` ablegen.
- `random.seed()` damit aufrufen.

**Erst danach** wird das Dictionary gebaut — damit der neue Seed darin steht.

**So prüfst du es:** Mitten in einer Welle `speichern`. **Die Debug-Zeile der nächsten Welle zeigt einen anderen Seed als die letzte** — und in der Datei steht genau dieser.

---

### 20. ⭐ Frag beim Start, ob geladen werden soll

**Die allererste Eingabe deines Spiels**, noch vor dem Briefing: *Spielstand laden? (j/n)*. **Immer** — auch wenn es keinen Spielstand gibt. *(Warum immer? Dann beginnt jede Befehlsdatei mit derselben Zeile, egal ob gerade eine Datei in `saves` liegt. Eine Frage, die mal kommt und mal nicht, verschiebt jede Zeile deiner Befehlsdatei um eins.)*

**Bei `j`:** `lade_daten()`. Kommt ein Dictionary zurück:

- Eine Welt anlegen — so, wie dein Hauptprogramm es heute tut — und mit `aus_daten()` überschreiben.
- `random.seed()` mit dem Seed **aus dem Spielstand**. Der feste Wert `SEED` spielt beim Laden keine Rolle.
- Eine Meldung, dass geladen wurde, mit Welle und Kern.

**Bei jeder anderen Antwort — oder wenn `lade_daten()` `None` zurückgibt:** alles wie bisher, Briefing, Klassenwahl, Trupp, Welt, Seed.

⚠️ **Der Handgriff, den kein Register beantwortet: Wie bekommt dein Hauptprogramm zwei Anfänge?** Such die Zeilen, die heute ein neues Spiel aufbauen — vom Briefing bis zum Setzen des Seeds. **Genau diese Zeilen stehen ab jetzt in einem Zweig**, der nur läuft, wenn nicht geladen wurde. Ob du dafür einen Wahrheitswert setzt oder mit `is None` fragst, ob schon eine Welt da ist, ist deine Wahl — beide Wege sind gedeckt. **Und: Die Zeilen rücken dafür eine Ebene nach rechts.** Blockweise, wie in Etappe 7, Auftrag 2.

**Und sofort danach: `befehle17.txt` bekommt eine neue erste Zeile, `n`.** Sonst liest die Frage deine Klassenwahl als Antwort, und der Beweislauf aus 17b stimmt nicht mehr.

**So prüfst du es:** Spielen, `speichern`, mit `beenden` raus — *(`beenden` speichert erst ab Schritt 23, deshalb vorher `speichern`)* —, neu starten, `j`. **Keine Klassenwahl.** Dann `n`: alles wie früher. Dann den Ordner `saves` umbenennen und `j`: *Kein Spielstand gefunden*, und ein neues Spiel beginnt. Danach wieder zurückbenennen.

---

### 21. ⭐ Lass die Wellenschleife bei der richtigen Welle beginnen

Nach Konzept 14.

- **Ein Name für die Startwelle**, gesetzt in beiden Zweigen aus Schritt 20: `1` beim neuen Spiel, die geladene Welle nach dem Laden.
- **Die Wellenschleife beginnt bei diesem Wert** statt bei der festen `1`.

*(Hast du für Beweisläufe bisher die `1` von Hand auf `8` gestellt, wie in 17b? Dann stellst du jetzt die `1` im Zweig des neuen Spiels um. Derselbe Handgriff an einer anderen Stelle.)*

**So prüfst du es:** In Welle 3 speichern, beenden, laden. **Die Debug-Zeile sagt Welle 3**, nicht Welle 1.

---

### 22. ⭐⭐ Mach mitten in der Welle weiter

Nach Konzept 14, letzter Absatz. Nach Schritt 21 hat dein Spiel einen Fehler, und du hast ihn vielleicht schon gesehen: **Nach dem Laden wird die gespeicherte Welle ein zweites Mal erzeugt.** Je nachdem, ob dein Wellenstart die Gegnerliste ersetzt oder erweitert, sind die geladenen Gegner danach verschwunden — oder eine frische Welle steht zusätzlich auf dem Feld.

**Der Wellenstart fragt ab heute, ob schon Gegner auf dem Feld stehen.** Geh die Schritte deines Wellenstarts durch — die Liste aus 17c, Schritt 20 — und entscheide für jeden nach der Frage aus Konzept 14: **Verändert er den Zustand, oder zeigt er ihn nur?** Was den Zustand verändert, läuft nur bei leerem Feld. Was nur zeigt, darf in beiden Fällen laufen.

**Schreib deine vier Entscheidungen in `GELERNT.md`**, neben die Reihenfolge der Pause aus 17c. Zwei davon sind schnell entschieden. Bei einem hilft die Frage: *Was stünde im Wellenbericht, wenn er nach dem Laden noch einmal liefe?*

**So prüfst du es:** Mitten in einer Welle mit drei Gegnern speichern, beenden, laden. **Drei Gegner**, an denselben Stellen mit denselben Trefferpunkten. Die Welle zu Ende spielen: Der Wellenbericht nennt für jeden Marine die Abschüsse **der ganzen Welle**, auch die vor dem Speichern.

---

### 23. ⭐ Lass `beenden` speichern

An der Stelle, an der dein Spiel `beenden` erkennt — seit der Knobelstelle aus Etappe 3a —, **vor dem Aussteigen** `speichere_spiel(welt)`.

**Und eine Entscheidung für das Spielende**, das nicht über `beenden` kommt: Der Kern fällt, oder die letzte Welle ist geschafft. **Dann liegt in `saves` noch der letzte Spielstand — von vor dem Ende.** Wer verloren hat, kann ihn laden und es noch einmal versuchen. Soll das gehen? **Zwei gedeckte Wege — wähl einen und schreib ihn mit Grund in `GELERNT.md`:**

| | Was passiert |
|---|---|
| **a)** | Nichts. Der letzte Spielstand ist ein Rücksetzpunkt, zu dem man nach einer Niederlage zurückkehren darf. |
| **b)** | Am Spielende — Sieg oder Niederlage — wird der Spielstand gelöscht. Ein Spiel ist dann vorbei, wenn es vorbei ist. |

**Für b) brauchst du ein Werkzeug:** `pfad.unlink()` löscht die Datei, auf die der Pfad zeigt. Gibt es sie nicht, kommt ein `FileNotFoundError` — **frag also vorher mit `.exists()`.** *(Gelöscht ist gelöscht: kein Papierkorb. Probier `unlink()` zuerst an einer Wegwerf-Datei aus.)*

**So prüfst du es:** Ein Spiel starten, zwei Züge, `beenden`. Neu starten, `j` — du stehst, wo du warst.

---

### 24. ⭐⭐ Mach den Beweislauf

**Der Beweis, den die Rundreise nicht führen kann.** Zwei Läufe mit demselben festen Seed:

| Lauf | Befehlsdatei | Was passiert |
|---|---|---|
| **A** | `befehle19a.txt` | Ein neues Spiel, ein paar Züge, **`speichern`**, und danach weitere Züge — alles in einem Durchgang |
| **B** | `befehle19b.txt` | Laden — und **genau die Züge, die in A nach `speichern` kamen** |

**Wenn dein Spielstand vollständig ist, gibt B ab dem Laden dieselben Zeilen aus wie A ab dem Speichern.** Jeder Wert, der nicht gespeichert wurde, fällt hier auf — sobald er irgendetwas verändert, das ausgegeben wird.

**a) Die zwei Befehlsdateien.** Format wie seit Etappe 7: eine Zeile pro `input()`, in der Reihenfolge, in der dein Spiel fragt.

- **`befehle19a.txt`:** `n`, die Klassenwahl, die Züge der ersten Hälfte, **`speichern`**, die Züge der zweiten Hälfte.
- **`befehle19b.txt`:** `j`, dann **wörtlich** die Züge der zweiten Hälfte aus `befehle19a.txt`.
- **Die zweite Hälfte ist lang genug**, dass mindestens eine Welle zu Ende geht — mit Einsammeln, Bericht und Ereignis — und die nächste beginnt. **Die erste Hälfte ist kurz**, gespeichert wird mitten in der ersten Welle, mit Gegnern auf dem Feld. Wenn du kannst: eine Mine liegt, ein Effekt läuft.
- **Keine Befehle, die ein Set ausgeben** — `bestiarium` etwa. Zwei Läufe sind zwei Programmstarts, und die Reihenfolge eines Sets kann sich dazwischen ändern — 17b, Konzept 11.

**Bevor du startest, schreib zwei Vorhersagen auf** — das Ritual aus dem Rahmenteil: Was zeigt `diff`, **wenn alles vollständig gespeichert ist**? Und wo taucht der erste Unterschied auf, **wenn genau die Stufe eines Marines fehlt**?

**b) Die Läufe.** `SEED` auf eine feste Zahl, die Startwelle des neuen Spiels auf `8`. Im Projektordner, **erst A, dann B** — A schreibt den Spielstand, den B lädt:

```
python spiel.py < befehle19a.txt > lauf_a.txt
python spiel.py < befehle19b.txt > lauf_b.txt
diff lauf_a.txt lauf_b.txt
```

Beide Ausgabedateien entstehen von selbst. Am Ende jeder Befehlsdatei kommt der `EOFError` aus Etappe 7 — erwartet.

**c) Lies den `diff`.** Er wird **nicht** schweigen, und er soll es nicht: Lauf A hat eine erste Hälfte, die in B nicht vorkommt, und beide haben verschiedene Meldungen beim Speichern und beim Laden. **Das ist ein einziger Unterschied, ganz oben.** `diff` meldet ihn mit einer Zeile, die mit Zahlen beginnt — etwa `1,41c1,2` —, darunter die Zeilen aus A mit `<`, dann `---`, dann die aus B mit `>`.

*(Mit `fc` unter Windows sieht die Ausgabe anders aus: Jeder Unterschied steht als eigener Block, eingerahmt von Zeilen mit `*****` und den Dateinamen. Dann zählst du Blöcke statt Ziffernzeilen — erwartet ist genau einer, ganz oben. Wenn dir das zu unübersichtlich wird: beide Dateien im Editor nebeneinander, wie in 17b.)*

**Zähl die Zeilen in der `diff`-Ausgabe, die mit einer Ziffer beginnen. Genau eine.** Dann sind beide Läufe ab dem Speichern Zeile für Zeile gleich — über das Wellenende, den Bericht, das Ereignis und die nächste, zufällig erzeugte Welle hinweg. **Genau genommen beweist `diff` damit nicht, dass zwei Welten gleich sind — sondern, dass sie sich in diesem Versuch gleich verhalten.** Ein fehlender Wert, der in deinen Zügen nie etwas bewirkt, bleibt unentdeckt. Deshalb gehört die Inventur daneben, und deshalb kommen in Etappe 26 weitere Versuche dazu.

**Ist es mehr als eine**, dann zeigt die zweite, wo die Läufe auseinandergehen. **Davor ist alles gleich** — der Wert, der fehlt, wirkt zum ersten Mal zwischen der letzten gleichen und der ersten verschiedenen Zeile. Die üblichen Verdächtigen:

| Die erste Abweichung steht … | Verdächtig |
|---|---|
| in der ersten Statusanzeige nach dem Laden | ein Wert, der angezeigt wird und nicht gespeichert ist — der Rundenzähler? |
| beim ersten Abschuss nach dem Laden | Erfahrung, Stufe, Skillpunkte — Konzept 13 |
| im Wellenbericht | `abschuesse_bei_wellenbeginn` — oder `welt.bericht` |
| bei der nächsten Welle, aber nicht vorher | der Seed — hast du in Schritt 19 neu gesät, **und** beim Laden mit dem gespeicherten gesetzt? |
| bei einem Kauf oder Schuss | etwas, das ein Kauf verändert hat — deine Fahndung aus Schritt 3 |

**Jeden Fund zuerst in der Inventur verbessern, dann im Code.** Danach wieder A und B.

**d) Schreib in `GELERNT.md`**, was dein erster Beweislauf gefunden hat — oder dass er nichts gefunden hat, und warum du ihm glaubst.

*(`lauf_a.txt` und `lauf_b.txt` sind Wegwerf-Dateien. `befehle19a.txt` und `befehle19b.txt` darfst du behalten — in Etappe 26 werden sie zu einem Test.)*

---

### 25. Prüf, dass das Alte noch läuft, und commit

- **Der Beweislauf aus 17b** mit `befehle17.txt` — jetzt mit `n` in der ersten Zeile —, fester Seed, zwei Läufe: **`diff` schweigt weiterhin.** *(Er enthält kein `speichern`, also wird nie neu gesät.)*
- Ein neues Spiel ohne Laden: Briefing, Klassenwahl, alles wie früher.
- **Deine *Zufallsregeln* aus 17c:** Die Regel über `random.seed()` heißt ab heute so, wie sie in der Design-Entscheidung steht — in deinen Worten.
- `SEED` auf `None`, Startwelle des neuen Spiels auf `1`, keine `lauf*.txt`, keine `probe.py`, kein `breakpoint()`.
- Die Abschnitte am Ende, die zu 19c gehören: **Kaputtmachen 8 bis 11** und **die Entwicklerfrage**.

Commit: `Etappe 19c: Das Spiel überlebt das Beenden`

---

## Selbsttest — 19c

- [ ] Die erste Frage deines Spiels ist immer *Spielstand laden?* — auch ohne Spielstand.
- [ ] Nach dem Laden: keine Klassenwahl, kein Briefing, die richtige Welle, dieselben Gegner an denselben Stellen.
- [ ] Nach dem Laden kommt die gespeicherte Welle **nicht** ein zweites Mal.
- [ ] `beenden` speichert.
- [ ] Nach `speichern` zeigt die nächste Debug-Zeile einen neuen Seed, und er steht in der Datei.
- [ ] Ein Marine, der vor dem Speichern aufgestiegen ist, bekommt nach dem Laden beim nächsten Abschuss **keine** Skillpunkte dafür noch einmal.
- [ ] ⭐⭐ **Der Beweislauf: `diff` meldet genau einen Unterschied, ganz oben.**
- [ ] Der Beweislauf aus 17b schweigt weiterhin.
- [ ] Deine Zufallsregeln nennen alle drei Stellen, an denen gesät wird.

---

## Was NICHT in diese Etappe gehört

**Kein `try`/`except`.** Eine kaputte Datei lässt dein Spiel mit `JSONDecodeError` abstürzen, ein manipulierter Wert vielleicht erst drei Züge später. Das ist heute gewollt: Ein Absturz beim Entwickeln ist ein Fund. **Fehler abfangen ist Etappe 20.**

**Kein `pickle`.** Es steht in der Design-Entscheidung von 19a, damit du es erkennst — und nirgends im Auftrag.

**Kein Laden mitten im Spiel.** Geladen wird beim Start. Ein Befehl `laden` während einer laufenden Welle müsste die ganze Welt austauschen, während die Wellenschleife auf ihr läuft. Das ist machbar und ein eigener Abend.

**Keine mehreren Spielstände, kein Autosave nach jeder Welle.** Beides steht unter *Wenn du mehr willst*.

**Kein Umrechnen alter Spielstände.** Deine Versionsnummer weist einen fremden Stand ab. Ihn in das neue Format umzurechnen — eine *Migration* — ist erst sinnvoll, wenn es einen alten gibt, den du behalten willst.

**Kein atomares Schreiben im Auftrag.** Konzept 15 — erkennen, nicht bauen.

**Kein Inhalt in Dateien.** `GEGNERTYPEN`, `WAREN`, `FAEHIGKEITEN` bleiben im Code. Dass Inhalt aus JSON kommt, ist Etappe 25 — und dort brauchst du alles, was du heute gelernt hast, noch einmal, mit dem Unterschied, dass du die Dateien nicht selbst geschrieben hast.

**Kein `Enum`.** Deine Zustände `"aktiv"` und `"tot"` sind Texte und landen als Texte im Spielstand. Wenn sie in Etappe 21b ein `Enum` werden, ist der Spielstand die erste Stelle, an der du übersetzen musst.

---

## Lernziele

**Zu 19a:**

1. Welche drei Sorten Werte kennt dein Programm, und welche davon gehört in einen Spielstand?
2. Warum schadet es, Inhalt mitzuspeichern, obwohl beim Laden alles richtig dasteht?
3. Was tut `with` — und was passiert mit der Datei, wenn innerhalb des Blocks ein Fehler auftritt?
4. Was unterscheidet `"w"` von `"r"`, und welches von beiden kann eine bestehende Datei zerstören?
5. Welche sechs Dinge kennt JSON — und was wird aus einem Tuple, einem Set und einem Zahlenschlüssel?
6. Warum ist `[3, 2] == (3, 2)` falsch, und warum ist das gefährlicher als ein Absturz?
7. Warum sortierst du ein Set, bevor es in die Datei geht?
8. **Woran erkennst du, ob ein Attribut in den Spielstand gehört?** ← die wichtigste

**Zu 19b:**

9. Warum ruft `als_daten` einer Unterklasse zuerst die Fassung der Oberklasse auf?
10. Was passiert, wenn ein Objekt, das an zwei Stellen steht, zweimal gespeichert wird — und woran merkst du es?
11. Warum werden beim Laden erst alle Einheiten erzeugt und danach die Verweise gesetzt?
12. Warum speicherst du von einem Item nur die Kennung?
13. Warum darfst du beim Laden nach dem Klassennamen fragen, obwohl dein Programm das seit Etappe 11 nirgends sonst tut?
14. Was beweist die Rundreise, und was beweist sie nicht?

**Zu 19c:**

15. Warum reicht es nicht, den Seed vom Spielbeginn zu speichern?
16. Warum muss die Stufe gespeichert werden, obwohl sie aus der Erfahrung folgt?
17. Woran erkennt dein Wellenstart, dass er in eine laufende Welle geraten ist?
18. Warum ist ein halb geschriebener Spielstand schlimmer als keiner — und was hilft dagegen, was nicht?

---

## 🧠 Die Entwicklerfrage — zu 19c

> **Was muss ein Spielstand garantieren?**

Drei mögliche Antworten, und jede verlangt mehr als die vorige:

- **Dass er lädt.** Ohne Absturz, ohne Fehlermeldung.
- **Dass er *denselben* Zustand ergibt.** Dein Beweislauf aus Schritt 24 prüft genau das.
- **Dass er in drei Monaten noch lädt** — wenn dein Code sich verändert hat, Tabellen zusammengezogen, Klassen umbenannt, Zustände zu `Enum` geworden sind.

Welche davon muss **dein** Spielstand garantieren, und welche nicht? Und was kostet dich die dritte — heute schon, mit einer Versionsnummer, die nur abweist? Zwei bis fünf Sätze in `GELERNT.md`. Du liest sie in Etappe 22 wieder, wenn du zum ersten Mal `SPIELSTAND_VERSION` erhöhst.

---

## Transferaufgabe (15 Minuten) — zu 19a

**Außerhalb des Spiels**, in einer Wegwerf-Datei. Ein Gartenbeet:

```python
beet = {"name": "Kräuterecke", "lage": (4, 7), "pflanzen": {"Salbei", "Thymian", "Minze"},
        "gegossen_am": {12: True, 13: False}, "zuletzt_gedüngt": None}
```

Schreib zwei Funktionen:

- **`speichere_beet(beet, pfad)`** — schreibt das Beet als JSON. Sie darf das Dictionary, das sie bekommt, **nicht** verändern.
- **`lade_beet(pfad)`** — gibt ein Beet zurück, das **`==` dem ursprünglichen ist.** Nicht ähnlich — gleich.

Am Ende eine Zeile: `print(lade_beet(pfad) == beet)`. **`True`.**

**Und eine Frage zum Schluss, ohne Code:** Angenommen, es gäbe einen Katalog, der zu jedem Beetnamen Lage und Pflanzen kennt. **Welche Einträge müsstest du dann überhaupt noch speichern?** Ein Satz — und er ist Konzept 1 in klein.

*(Drei Einträge brauchen einen Rückweg. Einer davon ist der, an dem die meisten zuerst vorbeisehen — prüf mit `type()` jeden einzelnen, bevor du glaubst, fertig zu sein. Ein Tuple aus zwei Zahlen baust du so, wie du es seit Etappe 6 kennst, aus den beiden Einträgen der Liste. Und prüf nach dem Speichern, ob `beet` noch dasselbe ist wie vorher.)*

---

## Leseübung — Stufe 3 (15 Minuten) — zu 19b

**Nicht ausführen.** Lesen, beantworten, dann erst — wenn du willst — ausprobieren.

```python
import json
from pathlib import Path

KATALOG = {"A-17": "Moby Dick", "B-03": "Faust", "C-44": "Momo"}


class Leser:
    def __init__(self, ausweis, name):
        self.ausweis = ausweis
        self.name = name
        self.gebuehren = 0


class Buch:
    def __init__(self, signatur):
        self.signatur = signatur
        self.titel = KATALOG[signatur]
        self.ausgeliehen_an = None
        self.faellig_in = 0


class Bibliothek:
    def __init__(self):
        self.leser = {}
        self.buecher = []

    def speichere(self, pfad):
        daten = {"version": 2, "leser": [], "buecher": []}
        for ausweis in self.leser:
            l = self.leser[ausweis]
            daten["leser"].append({"ausweis": l.ausweis, "name": l.name,
                                   "gebuehren": l.gebuehren})
        for b in self.buecher:
            an = None
            if b.ausgeliehen_an is not None:
                an = b.ausgeliehen_an.ausweis
            daten["buecher"].append({"signatur": b.signatur, "an": an,
                                     "faellig_in": b.faellig_in})
        with open(pfad, "w", encoding="utf-8") as f:
            json.dump(daten, f, ensure_ascii=False, indent=2)

    def lade(self, pfad):
        with open(pfad, "r", encoding="utf-8") as f:
            daten = json.load(f)
        self.leser = {}
        for d in daten["leser"]:
            l = Leser(d["ausweis"], d["name"])
            l.gebuehren = d["gebuehren"]
            self.leser[l.ausweis] = l
        self.buecher = []
        for d in daten["buecher"]:
            b = Buch(d["signatur"])
            b.faellig_in = d["faellig_in"]
            if d["an"] is not None:
                b.ausgeliehen_an = self.leser[d["an"]]
            self.buecher.append(b)
```

*(Die Ausweise sind Zahlen, etwa `1041`.)*

**Die fünf Fragen**, für `speichere` und für `lade`:

1. Was kommt rein?
2. Was passiert?
3. Was verändert sich — und woran?
4. Was kommt raus?
5. Welche anderen Objekte oder Funktionen werden dabei aufgerufen?

**Und die Leitfrage von Stufe 3 — warum ist es so gebaut?**

6. Die Bibliothek hält ihre Leser in einem **Dictionary** *Ausweis → Leser*. In der Datei stehen sie als **Liste**. Warum? *(Konzept 5. Was stünde in der Datei, wenn man das Dictionary direkt hineinschriebe — und was fände `self.leser[d["an"]]` danach?)*
7. Warum steht der Titel eines Buches nicht in der Datei?
8. Welcher der drei Wege aus der Design-Entscheidung von 19b ist das? Warum geht es hier **ohne** die Stelle in einer Liste — und was müsste für jeden Leser gelten, damit das trägt?
9. Warum lädt `lade` erst alle Leser und dann alle Bücher? Was passierte in umgekehrter Reihenfolge?
10. In der Datei steht `"version": 2`. **Was fehlt?**
11. Jemand löscht in der Datei von Hand einen Leser, der noch ein Buch hat. **Wann** stürzt das Programm ab — beim Laden, beim Speichern, oder nie? Welcher der drei Fehlertypen ist das?

---

## Kaputtmachen

Jedes Experiment nach dem Ritual: **erst aufschreiben, was passieren wird**, dann ausführen, vergleichen, erklären. Danach wieder reparieren.

**Pflicht:** 3, 5, 7, 8 und 11. Die übrigen, wenn du Zeit hast.

### Zu 19a

**1. Starte vom falschen Ort.** Wechsle im Terminal in den Ordner **über** deinem Projekt und starte dein Spiel von dort, mit dem Pfad davor. Spielen, `speichern`. **Wo ist der Ordner `saves` jetzt?** Und was sagt dein Spiel, wenn du es danach wieder aus dem Projektordner startest und laden willst? *(Danach den falschen `saves`-Ordner löschen.)*

**2. Nimm `indent=2` und `ensure_ascii=False` heraus.** Speichern, die Datei ansehen. Lädt sie noch? Würde `diff` dir damit noch sagen, *welcher* Wert sich unterscheidet?

**3. ⭐⭐ Vergiss ein `sorted()`.** In `Welt.als_daten()` bei `flags`. Speichere mitten in einer Welle — mit einem Spielstand, der schon in `saves` liegt. **Was sagt Python — und was steht danach in `saves/spielstand.json`?** Versuch zu laden. Wo ist dein Spiel von vorhin? *(Das ist Konzept 15 am eigenen Leib. Und die Frage dazu: Hätte es geholfen, dass `als_daten()` vor dem Öffnen läuft?)*

### Zu 19b

**4. Stell das Dictionary *Klassenname → Klasse* über deine Klassen.** Starten. Was sagt Python, und wann — beim Start oder erst beim Laden?

**5. ⭐⭐ Bau Weg A aus der Design-Entscheidung.** Speichere unter `"held"` nicht die Stelle, sondern `welt.held.als_daten()`, und lade daraus ein **eigenes** Objekt für `welt.held`. Speichern, laden, einen Gegner an dich heranlassen. **Wessen Trefferpunkte sinken — und wessen zeigt die Statusanzeige?** Und `print(len(welt.trupp))`? *(Ein Typ 3, der nie abstürzt: Das Spiel läuft, nur stimmt das Bild nicht mehr mit dem Kampf überein.)*

**6. Nimm ein `.copy()` heraus.** Bei den Effekten in `Einheit.als_daten()`. In der Probedatei: `d = einheit.als_daten()`, dann der Einheit einen neuen Effekt geben, dann `print(d)`. **Was steht in `d` — und wann wäre das ein Problem?**

**7. ⭐⭐ Lass ein Attribut auf beiden Seiten weg.** Die Stufe eines Marines — aus `als_daten` **und** aus `aus_daten`. Die Rundreise aus Schritt 17. **Schweigt `diff`?** Warum? *(Danach wieder hinein. Die Antwort ist die auf Lernziel 14.)*

### Zu 19c

**8. ⭐⭐ Lass die Stufe wieder weg — und spiel weiter.** Nur aus beiden Methoden, wie in 7. Einen Marine auf Stufe 2 bringen, `beenden`, laden, den nächsten Gegner erledigen. **Wie viele Skillpunkte hat er jetzt?** Konzept 13 — und sieh dir an, ob der Beweislauf aus Schritt 24 es gefunden hätte.

**9. Säe beim Speichern nicht neu.** Die drei Zeilen aus Schritt 19 auskommentieren. Den Beweislauf wiederholen. **Wo redet `diff` zum zweiten Mal — und warum erst dort?** *(Wann wird nach dem Speichern zum ersten Mal gewürfelt?)*

**10. Überspring den Wellenstart nicht.** Die Frage aus Schritt 22 herausnehmen. Mitten in einer Welle speichern, laden. **Wie viele Gegner stehen auf dem Feld?** Und was sagt die Ankündigung?

**11. ⭐ Manipulier deinen Spielstand.** Vier Versuche, jeder an einer frischen Kopie deiner Datei. **Vorher jedes Mal aufschreiben: Stürzt es ab — und wenn ja, wann?**

- a) Setz `"kern_integritaet"` auf `"viel"` — mit Anführungszeichen.
- b) Lösch irgendwo ein Komma.
- c) Setz beim Helden `"klasse"` auf `"Pilot"`.
- d) Setz `"held"` auf die Stelle eines **Kameraden**.

**Welche knallt beim Laden, welche später, welche nie?** Ordne jede einem der drei Fehlertypen aus Etappe 8 zu. *(Das ist der Fehler in den Daten, den Etappe 16 dir noch nicht geben konnte: Der Code ist völlig richtig, und das Spiel tut trotzdem Unsinn. In Etappe 20 fängst du b) und c) ab. a) und d) nicht — beide knallen nicht beim Laden, sondern später oder nie, und in Etappe 25 erfährst du, warum sie schwerer zu erkennen sind.)*

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo nachsehen |
|---|---|---|
| `TypeError: Object of type set is not JSON serializable` | Ein Set steht direkt im Dictionary | Konzept 5 und 6 — `sorted()` |
| `TypeError: Object of type Soldat is not JSON serializable` | Ein Objekt statt seines `als_daten()` — oft ein Verweis | Konzept 10 |
| `TypeError: unsupported operand type(s) for /: 'str' and 'str'` | Zwei Texte mit `/` verbunden — links muss ein Pfad stehen | Konzept 3 |
| `FileNotFoundError` beim Laden | Die Datei gibt es nicht — oder das Terminal steht woanders | Schritt 7, Konzept 3 |
| `FileExistsError` beim Speichern | `mkdir()` ohne `exist_ok=True` | Konzept 3 |
| `NameError: name 'Soldat' is not defined` beim Start | Das Dictionary *Klassenname → Klasse* steht über den Klassen | Konzept 9 |
| `KeyError` in `aus_daten` | Ein Schlüssel wird gelesen, den `als_daten` nicht schreibt — oder anders schreibt | Konzept 8, Spiegelbilder |
| `ValueError: None is not in list` beim Speichern | `.index()` für einen Verweis, der gerade `None` ist | Konzept 10 |
| `JSONDecodeError` beim Start | Die Datei ist kaputt — halb geschrieben oder von Hand bearbeitet | Konzept 15, Kaputtmachen 3 und 11 |
| Umlaute als `ü` in der Datei | `ensure_ascii=False` fehlt | Konzept 4 |
| Der ganze Spielstand steht in einer Zeile | `indent=2` fehlt | Konzept 4 |
| Nach dem Laden gibt es einen Marine mehr | Ein Objekt wurde zweimal geladen — meist der Held | Design-Entscheidung 19b, Kaputtmachen 5 |
| Der Held nimmt Schaden, die Anzeige bleibt gleich | `welt.held` ist nicht dasselbe Objekt wie im Trupp | Konzept 10, der `is`-Test |
| Die Rundreise redet bei `flags` | Beim Laden kein `set()` — oder beim Speichern kein `sorted()` | Konzept 5, 6 |
| Eine geladene Position findet nichts mehr, Vergleiche sind immer falsch | Ein Tuple kam als Liste zurück | Konzept 5, 12 — `tuple()` |
| Nach dem Laden gibt es Skillpunkte, die es schon gab | Die Stufe wird nicht gespeichert | Konzept 13 |
| Nach dem Laden kommt die gespeicherte Welle noch einmal | Der Wellenstart fragt nicht, ob schon Gegner da sind | Schritt 22 |
| Der Wellenbericht nach dem Laden zählt nur die Abschüsse seit dem Laden | `abschuesse_bei_wellenbeginn` fehlt — oder der Wellenstart setzt es neu | Schritt 11, Schritt 22 |
| Ein Kauf aus Etappe 6 ist nach dem Laden wirkungslos | Er hat ein Attribut verändert, das nicht gespeichert wird | Schritt 3, die Fahndung |
| Die Beschreibung eines Sektors ändert sich im Code, im Spiel aber nicht | Die Beschreibungen stehen im Spielstand | Konzept 1 |
| Der Beweislauf redet erst ab der nächsten Welle | Beim Speichern oder beim Laden wird nicht mit dem gespeicherten Seed gesät | Schritt 19, 20 |
| Der Beweislauf aus 17b stimmt nicht mehr | `befehle17.txt` hat keine erste Zeile `n` | Schritt 20 |

---

## Ein Blick nach vorne

**Etappe 20 fängt ab, was heute abstürzt.** Eine kaputte Datei, ein fehlender Schlüssel, ein manipulierter Wert — deine Kaputtmach-Versuche aus 11 sind dort die Liste dessen, was dein Spiel dem Spieler erklären soll, statt zu sterben. Und `finally` wird dir einen automatischen Spielstand beim Absturz anbieten; Konzept 15 sagt dir heute schon, wo seine Grenze liegt.

**Etappe 21b macht aus `"aktiv"` und `"tot"` ein `Enum`.** Dann steht in deinem Spielstand ein Text und in deinem Programm etwas anderes — die erste Stelle, an der `aus_daten` übersetzen muss, obwohl sich im Spiel nichts geändert hat.

**Etappe 22 zieht deine Tabellen zusammen und bringt die Rekruten.** Beides ändert, was ein Spielstand enthält — **der erste Moment, an dem du `SPIELSTAND_VERSION` erhöhst.** Und deine Entwicklerfrage von heute liegt dann daneben.

**Etappe 25 lädt Inhalt aus JSON.** Dieselben Werkzeuge, derselbe Rückweg für Sets und Tuples — mit einem Unterschied, der alles ändert: Die Dateien hast du nicht selbst geschrieben. *„Beim Laden ist nichts automatisch das, was du gespeichert hast"* wird dort zu *„… was du erwartest"*.

**Etappe 26 testet.** Die Rundreise ist dort ein Test, der eine Welt speichert, lädt und vergleicht — in einem Wegwerf-Ordner, den das Testwerkzeug dir gibt. Und deine zwei Befehlsdateien aus Schritt 24 werden der erste Test, der ein ganzes Spiel prüft.

---

## Abschluss

**In `GELERNT.md`:**

- ⭐⭐ **Deine Zustandsinventur**, so, wie sie nach dem Beweislauf aussieht — mit jedem Fund, den er gemacht hat.
- ⭐ Was die Rundreise beweist und was nicht, in zwei Sätzen.
- ⭐ Was dein erster Beweislauf gefunden hat.
- Deine vier Entscheidungen zum Wellenstart nach dem Laden.
- Deine Entscheidung zum Spielende aus Schritt 23, mit Grund.
- Welcher Weg aus der Design-Entscheidung von 19a dir ohne Tabelle eingefallen wäre.
- Warum `speichere_spiel` erst das Dictionary baut und dann die Datei öffnet.
- **Deine Zufallsregeln aus 17c, mit der neu gefassten Regel über das Säen.**
- Ob dein Basisturm im Bau eine Stelle im Trupp hat oder nicht — und wie du ihn deshalb speicherst.
- 🧠 Die Entwicklerfrage.
- Was hat mich überrascht? *(Kandidaten: dass `diff` zwischen zwei ganzen Spielen genau eine Stelle findet · dass eine Liste nie gleich einem Tuple ist · wie viel eine Datei verrät, die man einmal ganz liest.)*

**Vor dem Commit:** `SEED` auf `None`? Startwelle bei `1`? Keine `probe.py`, `json_probe.py`, `probe.json`, `lauf_*.txt`, `vorher.json`, `nachher.json`, kein Entwicklerbefehl `rundreise`, kein `breakpoint()`? `saves` steht nicht in `git status`?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest.

**Atomares Schreiben — bauen statt erkennen.** Ein Pfad hat eine Methode `.replace(ziel)`, die die Datei umbenennt und dabei eine bestehende Datei am Ziel ersetzt — in einem unteilbaren Schritt:

```python
entwurf = Path("notizen.tmp")
with open(entwurf, "w", encoding="utf-8") as f:
    json.dump(notizen, f, ensure_ascii=False, indent=2)
entwurf.replace(Path("notizen.json"))
```

Bau das in `speichere_spiel()` ein. Dann Kaputtmachen 3 noch einmal: **Was steht jetzt in `spielstand.json`?** *(Und was bleibt im Ordner liegen?)*

**Drei Spielstände.** `speichern 2` schreibt nach `saves/spielstand_2.json`. Ein Pfad lässt sich mit einem f-String zusammensetzen: `SPEICHERORDNER / f"spielstand_{nummer}.json"`. Die Startfrage fragt dann, welcher. Denk an die Befehlsdateien: Sie brauchen danach wieder eine Zeile mehr.

**Autosave nach jeder Welle.** Klingt nach einer Zeile — und ist eine Knobelstelle. Nach der Welle ist das Feld leer, und dein Wellenstart aus Schritt 22 hält einen leeren Stand für *„neue Welle"*. **Welche Welle steht im Spielstand, und welche muss nach dem Laden beginnen?** Und was ist mit Bericht und Ereignis, die in der Pause schon gelaufen sind?

**Ein Befehl `spielstand`**, der ohne zu laden anzeigt, was in der Datei steht: Welle, Kern, Stufe des Helden, wann zuletzt gespeichert. *(Für „wann" brauchst du eine Uhrzeit, und die hast du noch nicht. Die Welle reicht.)*
