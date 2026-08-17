# Etappe 5 — Die Karte

> **Block 1: Fundament** · Etappe 5 von 30 · [← Etappe 4](etappe-04-das-inventar.md) · [Lehrplan](../RPG_Lehrplan.md) · [Etappe 6 →](etappe-06-liste-dict-set-tuple.md)

**Boot.dev:** Dictionaries, verschachtelte Dictionaries, `keys()` / `values()` / `items()`
**Zeitaufwand:** 5–7 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 4 abgeschlossen, Selbsttest grün

---

## Worum es geht

Dein Dorf besteht bisher aus einem einzigen Ort. Der Spieler sieht sich um, hebt etwas auf, redet — aber er kann nirgendwo hingehen. Das Dorf ist ein Raum, kein Ort.

Heute bekommt es eine Ausdehnung. Fünf bis sechs Orte, dazu die **Wiese** vor dem Dorf und der **Minenpfad**. Der Spieler tippt `gehe norden` und steht woanders.

Und am Ende des Pfades liegt der Mineneingang. Verschlossen. Dein erster gesperrter Weg — und die erste Stelle, an der dein Spiel dem Spieler etwas zeigt, das er noch nicht haben kann.

**Technisch ist das die wichtigste Etappe des ersten Blocks.**

Nicht wegen der Syntax — Dictionaries sind schnell gelernt. Sondern wegen dem, was danach anders ist: Zum ersten Mal fallen **Daten und Code auseinander**. Bisher war jede Ortsbeschreibung eine `print()`-Zeile mitten in deinem Programm. Ab heute ist sie ein Eintrag in einer Tabelle, und dein Programm liest sie nur noch aus.

Der Unterschied klingt akademisch. Er ist der Grund, warum du in Etappe 25 an deinem Spiel *schreiben* kannst, ohne zu programmieren. Merk dir das Gefühl, wenn du heute den siebten Ort hinzufügst und keine einzige Zeile Logik anfassen musst.

---

## Der lange Bogen

| Was du heute baust | Wo es wieder auftaucht |
|---|---|
| `orte` als verschachteltes Dictionary | **Etappe 13** — `world.oeffne_weg()` verändert es zur Laufzeit |
| Trennung von Daten und Code | **Etappe 25** — der gesamte Inhalt wandert nach `content/` |
| Die verschachtelte Struktur selbst | **Etappe 19** — genau diese Form ist JSON |
| Der verschlossene Mineneingang | **Etappe 14** — die Mine öffnet sich |
| Die Wiese vor dem Dorf | **Etappe 13** — dort wächst der magische Samen |
| `in` prüft beim Dictionary den **Schlüssel** | **Etappe 6** — die Gegenüberstellung Liste / Set / Dictionary |
| Schlüssel müssen unveränderbar sein | **Etappe 6** — warum ein Set keine Listen enthalten kann |
| `aktueller_ort` als Zustandsvariable | **Etappe 10** — wird zu `player.ort`; **Etappe 19** — Teil des Speicherstands |
| `.get()` für sicheren Zugriff | **Etappe 20** — die Alternative zu `try` / `except` |
| Über ein Dictionary iterieren | **Etappe 12** — über alle NPCs laufen |
| Gegenstände pro Ort | **Etappe 13** — Pflanzen gehören zur Wiese, nicht zum Spieler |

**Sieben Schulden werden heute eingelöst** — so viele wie in keiner Etappe zuvor:

Aus **Etappe 3**: die lange `elif`-Kette, die du damals ertragen solltest. Aus Etappe 3 auch die Befehlssprache, die du festgelegt hast — heute kommt `gehe norden` dazu und muss zu deiner Entscheidung passen. Und der `else`-Zweig für unbekannte Befehle wächst mit.

Aus **Etappe 4**: `.split()` bekommt seinen zweiten Anwendungsfall. Die Gegenstände verteilen sich auf die Orte. Das Werkzeug für Kennung und Anzeigename, das dir dort angekündigt wurde, ist genau das Dictionary. Und das Zählen von Gegenständen, das mit einer Liste so umständlich war, wird hier zur Nebensache.

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

Zwei Fragen, und beide haben Folgen bis Etappe 13.

### Frage 1: Sind Wege beidseitig?

Wenn vom Dorfplatz ein Weg nach Norden zur Schmiede führt — führt dann von der Schmiede automatisch einer nach Süden zurück?

**Python macht das nicht für dich.** Du schreibst beide Einträge von Hand, oder es gibt den Rückweg nicht. Bei sechs Orten sind das schnell ein Dutzend Einträge, die zusammenpassen müssen, und ein Tippfehler bedeutet einen Spieler, der irgendwo festsitzt.

Die einfache Lösung: **Diszipliniert beide Richtungen eintragen, jedes Mal.** Das ist unelegant und völlig ausreichend. Es gibt Wege, das automatisch zu machen — du hast das Werkzeug dafür noch nicht, und du brauchst es bei sechs Orten auch nicht.

**Aber:** Eine Einbahnstraße ist ein Gestaltungsmittel. Ein Abhang, den man hinunterrutscht und nicht wieder hinaufkommt. Ein Fallgatter, das hinter dir zufällt. Wenn du das einsetzt, dann **bewusst und selten** — sonst hältst du deine eigenen Tippfehler für Absicht.

### Frage 2: Wie stellst du einen gesperrten Weg dar?

Das ist die wichtigere Frage, und der Mineneingang zwingt dich zur Antwort.

*Möglichkeit A — der Ausgang existiert nicht.* Am Minenpfad gibt es einfach keinen Eintrag nach Westen. Der Spieler tippt `gehe westen` und bekommt „Da ist kein Weg." Einfach zu bauen.

*Möglichkeit B — der Ausgang existiert und ist gesperrt.* Der Eintrag ist da, hat aber eine Markierung. Der Spieler bekommt „Die Tür ist verschlossen." Aufwändiger.

**Der Unterschied ist nicht technisch, sondern erzählerisch.** Eine Tür, die du siehst und nicht öffnen kannst, ist ein Versprechen. Eine Tür, die es nicht gibt, ist gar nichts. Der Spieler soll wissen, dass da etwas ist, und soll sich fragen, wie er hineinkommt.

**Meine Empfehlung: Möglichkeit B.** Nicht nur wegen der Erzählung — in Etappe 13 öffnet ein magischer Samen einen Weg, der vorher nicht begehbar war. Wenn Wege grundsätzlich existieren und nur einen Zustand haben, ist das dort eine Zeile. Wenn Wege erst entstehen müssen, ist es Umbau.

Schreib deine Entscheidung mit einem Satz Begründung in `GELERNT.md`.

---

## Die Konzepte

### 1. Das Dictionary — Nachschlagen statt Abzählen

Eine Liste ordnet Werte nach **Position**. Ein Dictionary ordnet sie nach **Namen**.

```python
alter = {"mara": 34, "jorin": 51}
```

Die geschweiften Klammern machen das Dictionary. Vor dem Doppelpunkt steht der **Schlüssel**, dahinter der **Wert**. Getrennt werden die Paare durch Kommas.

```python
alter["mara"]      # 34
```

Statt „gib mir Position 0" sagst du „gib mir den Eintrag `mara`". Und genau das brauchst du für Orte: Du willst nicht wissen, welcher Ort der dritte ist. Du willst wissen, was am Dorfplatz ist.

**Ein leeres Dictionary:**

```python
leer = {}
```

Achtung, kleine Gemeinheit: `{}` ist ein leeres Dictionary, nicht ein leeres Set. Das Set kommt in Etappe 6 und muss anders geschrieben werden.

### 2. Warum hier ein Dictionary und keine Liste

Stell dir deine Karte als Liste vor:

```python
orte = ["dorfplatz", "schmiede", "brunnen", "wiese"]
```

Und jetzt: Wo ist der Spieler? Position 2. Wohin führt der Weg nach Norden? Zu Position 1. Dein Code wäre voller Zahlen, die nichts bedeuten, und beim Einfügen eines neuen Ortes verschieben sich alle.

Mit einem Dictionary heißt der Ort `"dorfplatz"`, und er heißt so, egal wie viele Orte du noch hinzufügst.

**Die Faustregel für den Rest deines Programmiererlebens:**

> Wenn die **Reihenfolge** zählt und du die Dinge durchgehst: **Liste.**
> Wenn du etwas **unter einem Namen nachschlägst**: **Dictionary.**

Dein Inventar bleibt eine Liste — dort zählt, was du hast, nicht wie es heißt. Deine Karte wird ein Dictionary.

### 3. Verschachtelung — Dictionary im Dictionary

Ein Ort hat mehr als eine Eigenschaft. Er hat eine Beschreibung *und* Ausgänge. Also ist der Wert zu jedem Ortsnamen selbst wieder ein Dictionary:

```python
orte = {
    "dorfplatz": {
        "beschreibung": "Der Brunnen steht trocken. Niemand hat heute Wasser geholt.",
        "ausgaenge": {"norden": "schmiede", "sueden": "wiese"}
    },
    "wiese": {
        "beschreibung": "Hohes Gras, ungemäht. Dahinter beginnt der Pfad.",
        "ausgaenge": {"norden": "dorfplatz", "westen": "minenpfad"}
    },
}
```

Drei Ebenen: `orte` → ein Ort → seine `ausgaenge`. Und die Ausgänge sind wieder ein Dictionary, weil du nach `"norden"` nachschlagen willst.

**Die Struktur als Baum gelesen:**

```text
orte
└── dorfplatz
    ├── beschreibung
    └── ausgaenge
        ├── norden → schmiede
        └── sueden → wiese
```

Wenn dir die Klammern zu viel werden, zeichne dir den Baum auf. Nicht die Schreibweise ist das Schwierige, sondern das Lesen der Ebenen — und ein Baum auf Papier beantwortet die Frage „auf welcher Ebene bin ich gerade?" schneller als jedes Nachzählen.

**Der Zugriff staffelt sich:**

```python
orte["dorfplatz"]                            # das ganze Ortsdictionary
orte["dorfplatz"]["beschreibung"]            # der Text
orte["dorfplatz"]["ausgaenge"]               # alle Ausgänge
orte["dorfplatz"]["ausgaenge"]["norden"]     # "schmiede"
```

Von links nach rechts gelesen: nimm `orte`, hol den Eintrag `dorfplatz`, hol daraus `ausgaenge`, hol daraus `norden`.

**Formatierung ist hier keine Kosmetik.** Schreib jeden Ort auf mehrere Zeilen, wie oben. In einer einzigen langen Zeile findest du deine eigene fehlende Klammer nie wieder. Das abschließende Komma nach dem letzten Eintrag ist erlaubt und praktisch — dann kannst du unten anfügen, ohne die Zeile darüber zu ändern.

**Und ein Blick weit nach vorn:** Was du hier schreibst, ist strukturell exakt das, was in Etappe 19 in einer JSON-Datei stehen wird. Verschachtelte Zuordnungen von Namen auf Werte sind das Format, in dem praktisch alle Konfigurationsdateien und Web-Schnittstellen der Welt arbeiten. Du lernst heute nicht nur ein Python-Detail.

### 4. Der Schlüssel, den es nicht gibt

```python
orte["taverne"]      # KeyError: 'taverne'
```

Ein Absturz, Fehler vom Typ 1. Das Gegenstück zum `IndexError` aus Etappe 4 — dieselbe Situation, andere Datenstruktur.

**Und hier ist die Falle, die dich in deinem Spiel erwischen wird:** Nicht der Ortsname ist das Problem, sondern die *Richtung*. Der Spieler tippt `gehe westen`, wo es keinen Westen gibt, und dein Programm stürzt ab. Ein `KeyError` ist die häufigste Art, wie ein Textadventure stirbt.

### 5. `.get()` — der sanfte Zugriff

```python
orte["taverne"]              # Absturz
orte.get("taverne")          # None — kein Absturz
orte.get("taverne", "nix")   # "nix" — dein eigener Ersatzwert
```

`.get()` liefert `None` statt zu knallen, und mit einem zweiten Argument bestimmst du selbst, was zurückkommt.

**Wann welches?** Das ist eine echte Entscheidung, keine Geschmackssache:

- **Eckige Klammern**, wenn der Schlüssel *da sein muss*. Wenn `orte[aktueller_ort]` fehlschlägt, ist dein Spielzustand kaputt, und ein lauter Absturz ist besser als stilles Weiterlaufen.
- **`.get()`**, wenn das Fehlen ein normaler Fall ist. Der Spieler tippt eine Richtung, die es nicht gibt — das ist kein Fehler, das ist Dienstag.

Diese Unterscheidung — *darf das fehlen oder nicht?* — ist eine der nützlichsten Gewohnheiten, die du dir in diesem Projekt aneignen kannst. In Etappe 20 bekommst du mit `try`/`except` das schwerere Werkzeug für dieselbe Frage.

### 6. `in` prüft den Schlüssel — nicht den Wert

Über diesen Stolperstein fällt fast jeder einmal.

```python
alter = {"mara": 34, "jorin": 51}

"mara" in alter      # True  — mara ist ein Schlüssel
34 in alter          # False — 34 ist ein WERT, kein Schlüssel
```

Bei einer Liste sucht `in` im Inhalt. Bei einem Dictionary sucht es **nur in den Schlüsseln**. Das ist kein Versehen der Sprachdesigner, sondern der Punkt: Ein Dictionary ist zum Nachschlagen gebaut, und nachgeschlagen wird über den Schlüssel.

Willst du wirklich in den Werten suchen, musst du das sagen: `34 in alter.values()`.

**Praktisch ist das dein Schutz vor dem `KeyError`:**

```python
if richtung in orte[aktueller_ort]["ausgaenge"]:
    # es gibt einen Weg
```

In Etappe 6 stellst du `in` bei Liste, Set und Dictionary direkt nebeneinander. Heute merk dir: **Dictionary heißt Schlüssel.**

### 7. Schlüssel müssen unveränderbar sein

```python
falsch = {["a", "b"]: "wert"}     # TypeError: unhashable type: 'list'
```

Eine Liste darf kein Schlüssel sein. Ein String, eine Zahl oder ein Tupel schon.

Der Grund hängt direkt an dem, was du in Etappe 4 gelernt hast: Ein Dictionary findet seine Einträge, indem es aus dem Schlüssel eine Art Adresse berechnet. Würde sich der Schlüssel nachträglich ändern — und Listen sind ja veränderbar —, wäre der Eintrag unauffindbar. Deshalb erlaubt Python nur **immutable** Werte als Schlüssel.

Für dich heute ohne Folgen, alle deine Schlüssel sind Strings. Aber merk dir die Regel: In Etappe 6 begegnet sie dir wieder, wenn ein Set aus demselben Grund keine Listen aufnehmen kann.

### 8. Iterieren — und was du dabei bekommst

```python
for x in orte:
    print(x)
```

Was wird ausgegeben? **Die Schlüssel.** Nicht die Werte. Das ist die zweite Stelle, an der Anfänger stolpern.

Drei Methoden geben dir, was du brauchst:

```python
orte.keys()      # alle Schlüssel
orte.values()    # alle Werte
orte.items()     # beides als Paare
```

Am nützlichsten ist `.items()`, weil du beides gleichzeitig bekommst:

```python
for name, daten in orte.items():
    print(name, "-", daten["beschreibung"])
```

Die zwei Variablen vor dem `in` verteilen das Paar auf Name und Wert. Das ist neu und wird dir überall begegnen.

**Für dein Spiel brauchst du das heute kaum** — du schlägst einzelne Orte nach, statt alle durchzugehen. Aber in Etappe 12 läuft genau diese Form über alle NPCs, und dort trägt sie den Tick.

### 9. Hinzufügen und Ändern zur Laufzeit

```python
orte["taverne"] = {"beschreibung": "...", "ausgaenge": {}}     # neuer Eintrag
orte["dorfplatz"]["beschreibung"] = "Der Brunnen ist jetzt..."  # geändert
```

Dieselbe Schreibweise für beides: Gibt es den Schlüssel, wird überschrieben. Gibt es ihn nicht, entsteht er.

Das ist bequem und gleichzeitig eine Fehlerquelle — ein Tippfehler beim Schlüssel legt stillschweigend einen neuen Eintrag an, statt zu meckern. Fehler vom Typ 3.

**Und hier der wichtigste Vorausverweis dieser Etappe:** In Etappe 13 lässt du einen magischen Samen wachsen, und wenn er reif ist, öffnet sich ein Weg, den es vorher nicht gab. Der Code dafür ist genau diese Zeile — ein Eintrag im `ausgaenge`-Dictionary, verändert, während das Spiel läuft. Deine Karte ist ab heute nicht mehr fest, sondern Zustand.

### 10. Die `elif`-Kette, die du nicht schreiben musst

In Etappe 3 stand: *Die Kette darf lang sein. Sie zu spüren ist der Grund, warum du in Etappe 5 verstehst, wozu die Werkzeuge gut sind.* Hier ist die Einlösung.

So sähe deine Karte ohne Dictionary aus:

```python
if aktueller_ort == "dorfplatz":
    print("Der Brunnen steht trocken...")
    if richtung == "norden":
        aktueller_ort = "schmiede"
    elif richtung == "sueden":
        aktueller_ort = "wiese"
elif aktueller_ort == "schmiede":
    print("Die Esse ist kalt...")
    if richtung == "sueden":
        aktueller_ort = "dorfplatz"
    ...
```

Sechs Orte, sechs Blöcke, jeder mit eigener Beschreibung und eigener Bewegungslogik. Ein siebter Ort bedeutet einen siebten Block. Und wenn du an der Bewegung etwas ändern willst, änderst du es sechsmal.

Mit dem Dictionary hast du **sechs Dateneinträge und genau eine Bewegungslogik**. Ein siebter Ort ist ein Eintrag mehr und keine Zeile Code.

**Die Form deines Programms ändert sich damit grundlegend:**

```text
VORHER                          NACHHER

Code                            Daten
├── wenn Dorfplatz ...          └── orte
├── wenn Schmiede ...               ├── dorfplatz
├── wenn Wiese ...                  ├── schmiede
└── wenn Minenpfad ...              ├── wiese
                                    └── minenpfad

                                Code
                                └── eine allgemeine Regel
                                    ├── Ort lesen
                                    ├── Beschreibung zeigen
                                    └── Ausgang wählen
```

Links wächst der Code mit der Welt. Rechts wächst nur die Welt.

**Das ist der Moment, den du dir merken sollst.** Nicht die Syntax — das Gefühl, dass Hinzufügen plötzlich billig geworden ist.

**Ehrlich dazu, damit keine falsche Erwartung entsteht:** Deine Befehls-Kette — `umsehen`, `reden`, `nimm`, `gehe`, `beenden` — bleibt eine `elif`-Kette. Die stirbt erst in Etappe 7, wenn du Funktionen hast. Heute stirbt nur die Ortskette, die du nie schreiben musstest.

### 11. Das Dictionary als Nachschlagetabelle

Nebenbei löst dieselbe Struktur zwei Probleme, die dich in Etappe 4 geärgert haben.

**Kennung und Anzeigename** — dort hast du entschieden, Gegenstände als kurze Kennung zu speichern, und der schöne Text stand von Hand im Code:

```python
namen = {
    "schluessel": "ein alter, schwerer Schlüssel",
    "brot": "ein halb gegessenes Brot",
}

print(f"Du nimmst {namen['schluessel']}.")
```

**Mengen** — mit einer Liste war „zwei Brote" umständlich:

```python
vorrat = {"brot": 2, "seil": 1}
vorrat["brot"] += 1
```

Beides musst du heute nicht einbauen; deine Karte ist Arbeit genug. Aber du sollst gesehen haben, dass es dasselbe Werkzeug ist. Ein Dictionary ist nicht „die Karte" — es ist *Nachschlagen*, und das brauchst du überall.

---

## Dein Auftrag

Schrittweise, nach jedem Schritt ausführen. Diese Etappe ist größer als die vorigen — teil sie ruhig auf mehrere Tage auf.

**Schritt 1 — Die Ortstabelle**
Leg `orte` als verschachteltes Dictionary an, vor der Hauptschleife. Fünf bis sechs Orte im Dorf, dazu **Wiese** und **Minenpfad**.

Fang mit **zwei** Orten an und einem Weg dazwischen. Bring das zum Laufen, bevor du die anderen schreibst. Eine Karte mit acht Orten und einem Klammerfehler ist eine unangenehme halbe Stunde.

Denk beim Schreiben an deine Entscheidung von oben: beide Richtungen eintragen.

**Schritt 2 — Wo der Spieler steht**
Eine Variable `aktueller_ort` mit dem Startort. Das ist ab heute eine der wichtigsten Variablen deines Spiels — sie sagt, wo alles stattfindet.

Kommentier sie: In Etappe 10 wird daraus `player.ort`, in Etappe 19 Teil des Speicherstands.

**Schritt 3 — `umsehen` liest aus der Tabelle**
Dein `umsehen` gibt gerade feste Texte aus. Jetzt holt es die Beschreibung aus dem Dictionary.

**Das ist ein Refactoring, kein neues Feature.** Nach dem Umbau muss sich `umsehen` am Startort genauso verhalten wie vorher. Wenn nicht, hast du beim Umbau etwas zerstört — such es, bevor du weitermachst.

Gib zusätzlich aus, welche Ausgänge es gibt. Der Spieler soll nicht raten müssen, wohin er kann.

**Schritt 4 — `gehe <richtung>`**
Deine `.split()`-Verarbeitung aus Etappe 4 kann das schon. Vier Fälle:

- Die Richtung existiert → `aktueller_ort` ändern, neuen Ort beschreiben
- Die Richtung existiert nicht → „Da ist kein Weg." Kein Absturz.
- Der Weg ist gesperrt → deine Entscheidung von oben
- Es wurde keine Richtung genannt (`gehe` allein) → nachfragen

Der zweite Fall ist der wichtige. **Prüf mit `in`, bevor du zugreifst** — sonst hast du einen `KeyError`, sobald jemand in eine Wand läuft.

**Schritt 5 — Gegenstände gehören zum Ort**
In Etappe 4 lag alles an einem Ort. Jetzt verteilt es sich.

Du hast zwei Möglichkeiten, und beide sind vertretbar:

```python
# A — die Gegenstände wohnen im Ort
orte["dorfplatz"]["gegenstaende"] = ["brot"]

# B — eine eigene Tabelle daneben
gegenstaende = {"dorfplatz": ["brot"], "wiese": []}
```

**Empfehlung: A.** Alles, was einen Ort ausmacht, steht dann an einer Stelle — und in Etappe 25, wenn die Karte in eine Datei wandert, wandern die Gegenstände von allein mit.

Beachte: Der Wert ist eine **Liste in einem Dictionary**. Deine `nimm`- und `ablege`-Befehle aus Etappe 4 arbeiten weiter mit Listen, sie holen sich die Liste jetzt nur woanders her.

**Schritt 6 — Der Schlüssel liegt nicht mehr vor deiner Nase**
Verteil die Fundstücke sinnvoll. Der Schlüssel gehört nicht auf den Dorfplatz — leg ihn irgendwohin, wo man ihn suchen muss.

Und lass ihn weiter nichts öffnen. Das ist Absicht, und es ist ein Gestaltungsprinzip, das du dir merken solltest:

> **Ein Gegenstand darf Bedeutung bekommen, bevor der Spieler seine Bedeutung versteht.**

Wer den Schlüssel findet und erst zwei Stunden später begreift, wozu er gehört, erlebt einen anderen Moment als jemand, dem das Spiel es sofort sagt.

**Schritt 7 — Der Minenpfad und die verschlossene Tür**
Am Ende des Pfades der Mineneingang. Der Spieler sieht ihn. Er kommt nicht hinein.

Schreib den Text so, dass klar wird: Das ist nicht Dekoration, da geht es weiter. Setz einen Kommentar auf Etappe 14.

**Schritt 8 — Die Wiese**
Vor dem Dorf, erreichbar, und heute passiert dort nichts. Sie ist bewusst leer.

In Etappe 13 pflanzt der Spieler dort einen Samen, der über Ticks wächst und einen neuen Weg öffnet. Beschreib sie so, dass sie sich nach einer Möglichkeit anfühlt, nicht nach einer Lücke — hoher Boden, ungemähtes Gras, jemand hat hier mal etwas angebaut.

**Schritt 9 — Der Durchgang**
Alles aus Etappe 3 und 4 muss noch funktionieren: `umsehen`, `reden`, `nimm`, `ablege`, `inventar`, `beenden`, unbekannte Befehle. Geh jeden einzeln durch.

Und dann der Test, der dieser Etappe ihren Sinn gibt: **Füge einen siebten Ort hinzu.** Wie viele Zeilen Logik musst du anfassen? Wenn die Antwort „keine" ist, hast du es richtig gebaut.

---

## Was NICHT in diese Etappe gehört

- ❌ Ein Set für besuchte Orte → **Etappe 6**
- ❌ Die Mine selbst als begehbarer Bereich → **Etappe 14**
- ❌ Funktionen wie `zeige_ort()` oder `bewege_spieler()` → **Etappe 7**
- ❌ Eine `Ort`-Klasse → **Etappe 11**
- ❌ NPCs, die sich zwischen Orten bewegen → **Etappe 12**
- ❌ Wege, die sich im Spiel öffnen → **Etappe 13**
- ❌ Die Karte in eine externe Datei auslagern → **Etappe 25**
- ❌ `try` / `except` beim Zugriff → **Etappe 20**

**Besonders verlockend wird die eigene Datei sein.** Sobald deine Ortstabelle vierzig Zeilen lang ist, willst du sie aus `spiel.py` heraushaben. Das Gefühl ist absolut richtig — und es ist genau das Gefühl, das Etappe 25 begründet. Heute darf die Tabelle im Code stehen.

**Und die Klasse.** Ein Ort mit Beschreibung, Ausgängen, Gegenständen — das schreit nach einem Objekt. Auch richtig. Auch Etappe 11. Wenn du heute eine Klasse baust, lernst du nicht, was ein Dictionary kann.

---

## Selbsttest

- [ ] `orte` enthält mindestens sechs Orte, plus Wiese und Minenpfad
- [ ] Jeder Ort hat eine Beschreibung und Ausgänge
- [ ] `gehe <richtung>` bewegt den Spieler tatsächlich
- [ ] Eine Richtung, die es nicht gibt, stürzt nicht ab
- [ ] `gehe` ohne Richtung stürzt nicht ab
- [ ] Jeder Weg funktioniert in beide Richtungen — oder die Einbahnstraße ist Absicht und dokumentiert
- [ ] `umsehen` holt den Text aus dem Dictionary, nicht aus einem festen `print()`
- [ ] `umsehen` zeigt auch die möglichen Ausgänge
- [ ] Gegenstände liegen an verschiedenen Orten
- [ ] `nimm` findet nur, was am aktuellen Ort liegt
- [ ] Der Mineneingang ist sichtbar und nicht begehbar
- [ ] Die Wiese ist erreichbar
- [ ] Vor jedem Zugriff auf eine Richtung steht eine Prüfung mit `in` oder ein `.get()`
- [ ] Alle Befehle aus Etappe 3 und 4 funktionieren unverändert
- [ ] Du hast einen siebten Ort hinzugefügt, ohne Logik anzufassen
- [ ] Ein Kommentar verweist auf Etappe 13 (Wiese), 14 (Mine) und 19 (`aktueller_ort` im Speicherstand)

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten:

1. **Warum ist ein Dictionary für die Karte besser als eine Liste?** Nenn zwei Gründe.
2. **Wie kommst du an einen verschachtelten Wert?** Erklär `orte["wiese"]["ausgaenge"]["westen"]` Schritt für Schritt.
3. **Was passiert bei einem Schlüssel, den es nicht gibt — und was macht `.get()` anders?** Wann nimmst du welches?
4. **Was prüft `"dorfplatz" in orte` — Schlüssel oder Wert?** Und wie prüfst du einen Wert?
5. **Was bekommst du bei `for x in orte:`?** Wie kommst du an die Werte, wie an beides?
6. **Warum darf eine Liste kein Dictionary-Schlüssel sein?** Was hat das mit Etappe 4 zu tun?
7. **Warum ist deine Ortsbeschreibung jetzt ein Datum und kein Code?** Was hast du dadurch gewonnen?
8. **Was passiert bei `orte["dorfplat"] = ...` mit einem Tippfehler?** Warum ist das gefährlicher als ein `KeyError`?

**Frage 7 ist die wichtigste dieser Etappe.** Sie ist keine Syntaxfrage. Wenn du sie in eigenen Worten beantworten kannst, hast du das Prinzip verstanden, auf dem Etappe 25 und der halbe Rest deines Programmiererlebens beruht.

---

## Transferaufgabe (15 Minuten)

**Neue Datei, außerhalb des Spiels.** `uebung_05.py`.

**Teil 1 — Nachschlagen**

> Leg ein Dictionary mit drei Dorfbewohnern und ihrem Alter an.
> Frag per `input()` nach einem Namen und gib das Alter aus.
> Reagier sauber, wenn es den Namen nicht gibt.

Bau es **zweimal**: einmal mit eckigen Klammern und einer `in`-Prüfung davor, einmal mit `.get()`.

Vergleich die beiden Fassungen. Welche liest sich besser? Und die eigentliche Frage: In welcher Situation wäre der Absturz sogar die bessere Reaktion?

**Teil 2 — Verschachteln**

> Erweiter jeden Bewohner zu einem eigenen Dictionary mit Alter *und* Beruf.
> Gib zu einem eingegebenen Namen beides aus.
> Dann: Gib mit einer Schleife alle Namen und Berufe aus.

Für den letzten Teil brauchst du `.items()`. Das ist die Form, die in Etappe 12 über deine NPCs läuft — üb sie hier, wo noch nichts davon abhängt.

---

## Kaputtmachen

Nach jedem Experiment rückgängig machen.

**Experiment 1 — Ausgänge als Liste**
Mach aus `{"norden": "schmiede"}` eine Liste: `["norden", "schmiede"]`. Versuch, damit die Bewegung zu bauen.

Es geht — aber schau dir an, was du dafür tun musst. Genau diese Umständlichkeit ist die Antwort auf Lernziel 1.

**Experiment 2 — Der Ort, der ins Leere zeigt**
Lösch einen Ort aus `orte`, auf den noch ein Ausgang zeigt. Geh in diese Richtung.

Wo genau knallt es — beim Bewegen oder erst beim `umsehen` danach? **Das ist der Unterschied zwischen der Stelle, an der es kaputtgeht, und der Stelle, an der es knallt.** Genau die Unterscheidung, um die es bei der Bug-Jagd geht.

**Und hier lernst du eine neue Fehlerklasse kennen.** Deine Syntax ist einwandfrei. Deine Logik ist einwandfrei. Trotzdem stimmt etwas nicht:

> Der Ausgang behauptet, dass es einen Ort gibt.
> Die Ortstabelle behauptet, dass es ihn nicht gibt.

**Deine Daten widersprechen sich.** Das ist etwas anderes als ein Programmierfehler, und es wird dich ab jetzt begleiten — je mehr Inhalt du in Daten auslagerst, desto mehr Möglichkeiten gibt es, dass zwei Einträge nicht zusammenpassen. In Etappe 25, wenn alles in Dateien liegt, ist das die häufigste Fehlerart überhaupt.

**Experiment 3 — `KeyError` provozieren**
Nimm die `in`-Prüfung bei `gehe` heraus und lauf in eine Wand. Lies die Fehlermeldung: Sie nennt dir den Schlüssel, den sie nicht gefunden hat. Fehlermeldungen sind Hilfe.

**Experiment 4 — Die drei Sichten nebeneinander**
Sag **vorher**, was du erwartest, dann führ aus:

```python
print(ausgaenge.keys())
print(ausgaenge.values())
print(ausgaenge.items())

for x in ausgaenge:
    print(x)

for richtung, ziel in ausgaenge.items():
    print(richtung, "→", ziel)
```

Fünf Ausgaben, drei verschiedene Antworten auf dieselbe Frage. Die vierte ist die, über die Anfänger stolpern: Direktes Iterieren gibt dir die **Schlüssel**, nicht die Werte.

**Experiment 5 — `in` auf einen Wert**
```python
orte = {"dorfplatz": {...}, "wiese": {...}}
print("dorfplatz" in orte)
print(orte["dorfplatz"] in orte)
```
Die zweite Zeile ist `False`, obwohl der Wert offensichtlich drinsteht. Warum?

**Experiment 6 — Eine Liste als Schlüssel**
```python
kaputt = {["norden"]: "schmiede"}
```
Lies den `TypeError`. Das Wort *unhashable* ist der Hinweis. Merk es dir für Etappe 6.

**Experiment 7 — Der stille Tippfehler**
```python
orte["dorfplat"]["beschreibung"] = "Neuer Text"
```
Kein `KeyError` beim Schreiben — aber führ es aus und schau nach, was jetzt in `orte` steht. Warum ist das schlimmer als ein Absturz?

**Experiment 8 — Während der Iteration verändern**
```python
for name in orte:
    orte["neuer_ort"] = {}
```
`RuntimeError: dictionary changed size during iteration`. Dasselbe Prinzip wie das Löschen in der Schleife aus Etappe 4 — nur meldet sich Python hier ausdrücklich. Diese Regel kommt in Etappe 12 wieder.

**Experiment 9 — Die `elif`-Welt wachsen lassen**
Bau in einer Wegwerf-Datei die Bewegung noch einmal ohne Dictionary:

```python
if richtung == "norden":
    ziel = "schmiede"
elif richtung == "sueden":
    ziel = "wiese"
```

Jetzt füg drei weitere Richtungen hinzu. Dann noch drei. Zähl die Zeilen.

Daneben:

```python
ziel = ausgaenge.get(richtung)
```

Füg auch hier sechs Richtungen hinzu. Zähl die Zeilen **Code** — nicht die Daten.

**Das ist der wichtigste Versuch dieser Etappe**, weil er eine Frage beantwortet, die dir dein Leben lang begegnen wird:

> Sind das wirklich verschiedene **Regeln** — oder nur verschiedene **Daten**?

Verschiedene Regeln gehören in Code. Verschiedene Daten gehören in eine Datenstruktur. Wer das verwechselt, schreibt Programme, die mit jedem Inhalt mitwachsen.

**Experiment 10 — Die halbe Verbindung**
Bau einen Ausgang, der nur in eine Richtung existiert. Geh hin, versuch zurück.

Kein Fehler, kein Absturz — der Spieler sitzt fest. **Fehler vom Typ 3, und zwar der, den du in dieser Etappe wirklich produzieren wirst.**

---

## Häufige Stolpersteine

| Fehlermeldung / Symptom | Was dahintersteckt | Wo du suchst |
|---|---|---|
| `KeyError: 'westen'` | Richtung existiert nicht, ungeprüft zugegriffen | `in`-Prüfung oder `.get()` vor dem Zugriff |
| `KeyError: 'schmiede'` beim `umsehen` | Ein Ausgang zeigt auf einen Ort, den es nicht gibt | Tippfehler im Zielnamen |
| `TypeError: unhashable type: 'list'` | Liste als Schlüssel benutzt | Die geschweiften Klammern durchsehen |
| `TypeError: string indices must be integers` | Eine Ebene zu tief oder zu flach zugegriffen | Was ist `orte["x"]` — Dictionary oder String? |
| Iterieren gibt nur Namen, keine Daten | `for x in dict` liefert Schlüssel | `.items()` benutzen |
| `in` findet den Wert nicht | Bei Dictionaries sucht `in` im Schlüssel | `.values()` — oder war die Frage falsch? |
| Der Spieler sitzt fest | Rückweg fehlt | Beide Richtungen prüfen |
| Ein neuer Ort taucht aus dem Nichts auf | Tippfehler beim Zuweisen legt ihn an | Alle Schlüssel ausgeben |
| `SyntaxError` irgendwo in der Karte | Komma oder Klammer fehlt | Zeile für Zeile, von der ersten Ortsdefinition an |
| `nimm` findet nichts mehr | Gegenstandsliste zeigt noch auf die alte Variable | Wo holt `nimm` die Liste her? |

**Der Debugging-Reflex dieser Etappe:** Wenn Bewegung sich falsch verhält, gib den Ort **und** seine Ausgänge aus.

```python
print(f"DEBUG: ort={aktueller_ort}  ausgaenge={orte[aktueller_ort]['ausgaenge']}")
```

Beachte die einfachen Anführungszeichen innerhalb des f-Strings — die doppelten sind schon vergeben. Fast jeder Bewegungsfehler ist ein Ausgang, der anders heißt, als du denkst.

**Und ein Werkzeug, das dir eine halbe Stunde spart:** Wenn deine Karte unübersichtlich wird, gib sie einmal komplett aus.

```python
for name, daten in orte.items():
    print(name, "->", daten["ausgaenge"])
```

Vier Zeilen, und du siehst alle Verbindungen auf einen Blick. Fehlende Rückwege springen dir sofort ins Auge.

---

## Ein Blick nach vorne

Deine Karte ist heute eine Tabelle im Code:

```python
orte = {"dorfplatz": {"beschreibung": "...", "ausgaenge": {...}}}
```

In **Etappe 7** räumst du deine Befehlsverarbeitung auf, die heute noch einmal gewachsen ist. Und das ist der eigentliche Grund für die Reihenfolge in diesem Lehrplan:

> Du sollst Funktionen nicht lernen, weil ein Lehrbuch sagt, dass Funktionen wichtig sind. Du sollst sie lernen, weil **dein eigener Code ein Problem bekommen hat**.

In **Etappe 6** lernst du das Set — und deine besuchten Orte bekommen die Datenstruktur, die wirklich zu ihnen passt. Ein Ort, den du zweimal betrittst, soll nicht zweimal in der Liste stehen.

In **Etappe 13** verändert sich diese Tabelle zum ersten Mal, während das Spiel läuft. Ein Samen wächst auf der Wiese, und ein Ausgang entsteht, den es beim Start nicht gab:

```python
world.oeffne_weg("wiese", "osten", "schlucht")
```

Das ist genau die Zuweisung aus Konzept 9 — nur an einem Ort im Code, der weiß, wann es soweit ist.

In **Etappe 14** öffnet sich die Mine. Und dort wirst du etwas Überraschendes tun: Die Mine bekommt **kein** Dictionary. Sie wird ein Raster aus verschachtelten Listen, weil ein Dungeon andere Eigenschaften hat als ein Dorf — größer, verzweigter, vielleicht zufällig erzeugt. Zu wissen, wann welche Struktur passt, ist die Fähigkeit, die diese beiden Etappen zusammen dir beibringen.

In **Etappe 19** speicherst du deinen Spielstand. Und dann fällt dir auf, dass deine Ortstabelle bereits fast JSON ist — verschachtelte Zuordnungen von Namen auf Werte. Der Weg von hier dorthin ist kürzer, als du heute glaubst.

In **Etappe 25** verlässt die Karte den Code endgültig. Sie liegt dann in `content/orte.json`, und du erweiterst dein Dorf, ohne Python anzufassen.

Das Prinzip dahinter hast du heute gebaut. Alles Weitere ist Ausbau.

---

## Abschluss

**`GELERNT.md`:**
Zwei bis drei Sätze. Zusätzlich diesmal:

- Deine Entscheidung zu gesperrten Wegen (Ausgang fehlt oder Ausgang gesperrt) — mit Begründung
- Ob du Einbahnstraßen zulässt
- Wie viele Zeilen Logik du für den siebten Ort anfassen musstest

Der letzte Punkt ist der Messwert dieser Etappe. Und er hat nur zwei mögliche Antworten:

> *„Ich müsste einen neuen `elif`-Block schreiben."* → Das Ziel dieser Etappe ist noch nicht erreicht. Geh zurück zu Konzept 10 und Experiment 9.
>
> *„Ich füge einen Eintrag zu `orte` hinzu, die Logik bleibt unverändert."* → Du hast verstanden, warum es diese Etappe gibt.

**Commit:**
```bash
git add .
git commit -m "Etappe 5: Die Karte"
git push
```

---

## Wenn du mehr willst

Optional, erst bei grünem Selbsttest.

**Anzeigenamen für Gegenstände.** Die Schuld aus Etappe 4, jetzt einlösbar: ein Dictionary, das Kennungen auf schöne Namen abbildet. `nimm schluessel` funktioniert weiter, aber der Spieler liest „Du nimmst einen alten, schweren Schlüssel." Zwei Zeilen, und dein Spiel klingt sofort erwachsener.

**Ein `karte`-Befehl.** Zeigt alle bekannten Verbindungen. Heute zeigt er notgedrungen *alle* Orte — auch die, wo der Spieler nie war. Merk dir das Problem: In Etappe 6 bekommst du mit dem Set genau das Werkzeug, um „schon besucht" zu speichern.

**Die erste Beschreibung ist länger.** Beim ersten Betreten der ausführliche Text, danach eine knappe Zeile. Das ist die Konvention fast aller Textadventures, und sie macht wiederholtes Durchqueren erträglich.

Du brauchst dafür eine Markierung pro Ort — heute geht das mit einem zusätzlichen Eintrag im Ortsdictionary. In Etappe 6 machst du es eleganter.

**Ein Bild für jeden Ort.** Ein Ort im Dictionary kann mehr Einträge haben als Beschreibung und Ausgänge. Zum Beispiel ein kleines Bild aus Textzeichen:

```python
"minenpfad": {
    "bild": """
        /\      /\
       /  \____/  \
      |   [    ]   |
      |   |    |   |
    """,
    "beschreibung": "...",
    "ausgaenge": {...}
}
```

Die dreifachen Anführungszeichen sind neu: Sie erlauben einen String über mehrere Zeilen, mit allen Zeilenumbrüchen genau so, wie du sie tippst. Ausgegeben wird er wie jeder andere.

**Warum das mehr ist als Dekoration:** Dein Spiel sieht nach fünf Minuten Arbeit plötzlich nicht mehr aus wie ein Skript. Und didaktisch ist es genau der richtige Ort — das Bild ist ein weiterer *Dateneintrag*, kein Code. Du hast gerade bewiesen, dass deine Struktur erweiterbar ist, ohne dass die Logik davon etwas mitbekommt.

Zwei Warnungen: Rückwärtsschrägstriche in ASCII-Bildern muss man verdoppeln (`\\`), sonst hält Python sie für Steuerzeichen. Und mach es für zwei, drei markante Orte, nicht für alle acht — sonst sitzt du den Abend an Bildchen statt an Python.

**Ein Ort, der sich beim zweiten Besuch verändert hat.** Etwas steht offen, das vorher zu war. Etwas fehlt. Erzählerisch ist das dein stärkstes Mittel in einem leeren Dorf: Der Spieler merkt, dass er nicht allein ist, ohne dass jemand auftaucht.

Technisch brauchst du nichts Neues — nur die Zuweisung aus Konzept 9. Und du hast dabei vorweggenommen, worum es in Etappe 13 geht.

---

> **Nächste Etappe:** [Etappe 6 — Liste, Dictionary, Set, Tuple](etappe-06-liste-dict-set-tuple.md) · Sets, Tuples, Mengenoperationen
> Dort baust du kein neues Feature. Du lernst, für jedes Problem die richtige Datenstruktur zu wählen — und merkst, dass du zwei davon schon die ganze Zeit brauchst.
