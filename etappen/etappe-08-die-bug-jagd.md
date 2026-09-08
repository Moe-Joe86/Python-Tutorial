# Etappe 8 — Die Bug-Jagd I

*v1.1.0 · 2026-09-07*

> **Block 1: Fundament** · Etappe 8 von 30 · [← Etappe 7](etappe-07-aufraeumen.md) · [Lehrplan](../Vorposten_Lehrplan.md) · Etappe 9 →

**Neue Syntax heute:** `breakpoint()` · die Debugger-Befehle `n` `s` `r` `c` `p` `l` `q` · der bedingte Breakpoint `if bedingung: breakpoint()` · `f"{wert!r}"` — die `!r`-Form im f-String · 👀 `repr()` als Funktion

**Zeitaufwand:** 4–5 Sitzungen à 20–30 Minuten. Rund 40 Minuten davon sind Lesestoff — diese Etappe ist mehr Lesen als Tippen, und das ist Absicht. Der Debugger will einmal in Ruhe verstanden werden, bevor er hilft.

**Voraussetzung:** Etappe 7 abgeschlossen, Selbsttest grün. Dein Spiel läuft und besteht seit Etappe 7 aus Funktionen, die man einzeln verdächtigen kann.

**Heute baust du kein Spielfeature.** Du baust eine Fähigkeit — und zwei Dokumente, die dich den Rest des Projekts begleiten.

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **Werkzeuge** | Debugger (`breakpoint()`, Schrittbefehle), bedingter Breakpoint, `!r` im f-String, `git diff` als Suchhilfe | Traceback von unten lesen · Ursache ≠ Symptom · Halbieren statt Durchsuchen | `repr()` als Funktion · der Aufrufstapel als Begriff |
| **Denken** | Die drei Fehlertypen als Raster · das Formular *Beobachtung → Hypothese → Experiment* · den Fehler in vier Zeilen beschreiben | Warum Typ 3 der teuerste ist · warum die Absturzstelle selten die Fehlerstelle ist | Debugging ist nicht Fehlerbehandlung (das kommt in Etappe 20) |

⚠️ **Ein Wort vorweg, damit die Etappe nicht ausufert:** Das Ziel ist nicht, dein Spiel fehlerfrei zu machen. Das Ziel ist, dass du am Ende ein **Verfahren** hast, mit dem du jeden künftigen Fehler angehst — und zwei Dateien, in denen dieses Verfahren wohnt. Wenn die stehen, bist du fertig.

---

## Worum es geht

Bis heute hattest du eine einzige Methode, einen Fehler zu finden: Code lesen und hoffen, dass er dir ins Auge springt. Das hat funktioniert, weil deine Fehler klein und dein Programm kurz war. Beides ist vorbei.

Dein Spiel läuft inzwischen über zwanzig Wellen mit Hunderten von Runden, verteilt auf ein Dutzend Funktionen. Wenn in Welle 9 ein Gegner zu viel Schaden nimmt, hilft dir Lesen nicht mehr — du weißt nicht einmal, **welche** der Funktionen schuld ist. Du brauchst ein Werkzeug, das dir zeigt, was gerade wirklich passiert, statt dass du es dir zusammenreimst.

> **Der Satz, um den es in dieser Etappe geht: Nachsehen schlägt Vermuten.**

Den kennst du schon. Seit Etappe 1 hast du in jeder Fundament-Etappe einen kleinen Nachseh-Reflex gelernt — erst `print(type(x))`, dann die Zweig-Marker, dann den Rundenzähler, dann `### VOR`/`### NACH` mit `len()`, dann `.keys()`, zuletzt die zwei `print`-Zeilen an den Funktionsgrenzen. Jeder davon war dieselbe Idee in klein: **Rate nicht, was drinsteht — druck es aus.**

Heute bekommst du das Werkzeug, das alle diese `print`-Reflexe auf einmal ablöst: den **Debugger**. Er hält dein Programm an jeder Stelle an, die du willst, und lässt dich hineinschauen — jede Variable, jeden Wert, Zeile für Zeile, ohne eine einzige `print`-Zeile einzufügen und danach wieder herauszusuchen. Der Reflex bleibt. Nur das Instrument wird schärfer.

**Und du bekommst ein Denkraster.** Denn die gefährlichsten Fehler sind nicht die, bei denen Python abstürzt und dir eine rote Meldung hinwirft. Die gefährlichsten sind die, bei denen alles ruhig weiterläuft und einfach das Falsche herauskommt. Die zu jagen ist eine eigene Kunst, und sie hat heute Saison.

---

## Der lange Bogen — was heute fällig wird

Diese Etappe ist eine **Sammelstelle**. Sechs frühere Etappen haben etwas hinterlegt, das genau hier eingelöst wird. Ich nenne sie beim Namen, damit du siehst, dass es kein Zufall ist:

- **Der `print`-Reflex aus Etappe 1 bis 7** wird heute zum Debugger. Er war immer nur der Notbehelf für das eigentliche Werkzeug.
- **Das `Strg + C` aus Etappe 3a** — der Notausgang, den du einmal absichtlich benutzt hast — gehört ab heute in den Werkzeugkasten. Ein hängendes Programm ist selbst ein Fund.
- **Die Entwicklerbefehle aus Etappe 3, die du am Ende jeder Etappe entfernst,** bekommen heute ihren tieferen Grund: Bei der Fehlersuche wäre jeder von ihnen ein Verdächtiger. Ein Programm, in dem man `gott`-Befehle stehen lässt, debuggt man doppelt so lange.
- **Der Balken aus Etappe 3c, der 110 % und negative Werte zeigt, statt sie zu kappen** — heute erntest du diese Entscheidung. Ein Balken, der Unsinn *anzeigt*, ist ein Fehlermelder. Einer, der Unsinn *versteckt*, ist ein Komplize.
- **Die Anmarschbahn aus Etappe 4** wird heute ausdrücklich zum Messgerät. Ein Listenfehler, der in einer Zahlenkolonne unsichtbar bliebe, springt auf der Bahn ins Auge.
- **Die Baureihenfolge aus Etappe 4** — ein Gegner, dann mehrere, dann entfernen, in drei Schritten statt einem — war schon das Suchverfahren dieser Etappe. Es heißt **Halbieren**, und heute bekommt es seinen Namen.
- **Der Aufrufstapel aus Etappe 7a** (die Kür-Übung mit den verschachtelten Funktionen) ist genau das, was du gleich in jedem Traceback von unten nach oben liest.

Wenn dir eine dieser Stellen nichts mehr sagt, ist das in Ordnung — du brauchst sie nicht auswendig. Wichtig ist nur, dass du siehst: **Das Projekt hat auf diese Etappe hingearbeitet.**

---

## Eine Design-Entscheidung: Wann Debugger, wann `print()`? ⭐

Du hast ab heute zwei Werkzeuge, die dasselbe können — nachsehen, was drinsteht. Sie schließen sich nicht aus, aber sie sind für verschiedene Lagen gemacht, und wer das eine für alles nimmt, verschwendet Zeit.

| | `print()` mit Präfix | Der Debugger |
|---|---|---|
| Stärke | Zeigt einen Verlauf über viele Durchläufe auf einen Blick | Zeigt **einen** Moment in voller Tiefe |
| Kostet | Zeilen einfügen und danach wieder heraussuchen | Einen Klick oder eine Zeile, keine Aufräumarbeit im Code |
| Ideal, wenn | du wissen willst *„wie entwickelt sich dieser Wert über 20 Runden?"* | du wissen willst *„was steht in diesem einen Moment in **allen** Variablen?"* |
| Schwäche | Verstopft die Ausgabe, du musst hinterher aufräumen | Zeigt immer nur den Halt, in dem du gerade stehst |

**Die Faustregel, die du dir merkst:**

> **Ein Wert über viele Runden → `print`. Viele Werte in einem Moment → Debugger.**

Der Debugger ist mächtiger, aber `print` verschwindet nicht. Bei einer Zahl, die über zwanzig Wellen langsam abdriftet, ist eine `print`-Zeile mit `### RUNDE` schneller als zwanzigmal auf *Weiter* zu klicken. **Schreib diese Faustregel und deine eigene Erfahrung damit in `GELERNT.md`** — welches der beiden du in welcher Lage genommen hast und ob es die richtige Wahl war.

---

## Die Konzepte

Alle Beispiele laufen **außerhalb** deines Spiels — Bäckerei, Kaffeebar, Lager, Restaurant. Deinen eigenen Code fasst du im Auftragsteil an. Das ist heute besonders wichtig: Bei der Bug-Jagd ist dein Spielcode das Jagdrevier, kein Anschauungsmaterial.

### 1. Zwei Landkarten desselben Geländes ⭐

Es gibt zwei gängige Arten, Fehler einzuteilen, und beide sind nützlich. Du brauchst sie für Verschiedenes.

**Die erste Landkarte — die klassische — sagt, *was* schiefgeht.** So reden Bücher, Fehlermeldungen und fremde Erklärungen:

| Name | Was passiert |
|---|---|
| **Syntaxfehler** | Python kann den Code nicht einmal lesen. Er läuft gar nicht erst los. |
| **Laufzeitfehler** | Der Code läuft und stößt beim Ausführen auf etwas Unmögliches — durch null teilen, einen Schlüssel lesen, den es nicht gibt. |
| **Logischer Fehler** | Der Code läuft sauber durch. Das Ergebnis ist trotzdem falsch. |

**Die zweite Landkarte — die dieses Projekts — sagt, *wann* der Fehler auffällt.** Das ist die interessantere Frage, denn *wann* entscheidet, wie teuer der Fehler ist:

| Typ | Wann er auffällt | Beispiel aus einer Bäckerei |
|---|---|---|
| **Typ 1** | Sofort. Das Programm startet nicht oder stürzt in der ersten Sekunde ab. | Ein Tippfehler im Rezept-Code, Python meldet ihn beim Start. |
| **Typ 2** | Irgendwann. Es läuft — bis eine bestimmte Bedingung eintritt. | Erst wenn ein Kunde *null* Brötchen bestellt, teilt der Code durch null. |
| **Typ 3** | Nie. Es läuft immer, liefert aber das Falsche. | Der Preis wird immer um zwei Cent zu niedrig gerechnet. Niemand merkt es. |

**Die beiden Landkarten decken sich nicht eins zu eins, und das ist der Witz:**

- Ein **Syntaxfehler** ist immer **Typ 1** — Python liest ihn ja gar nicht erst.
- Ein **logischer Fehler** ist immer **Typ 3** — er läuft ja durch.
- Ein **Laufzeitfehler** kann **Typ 1 oder Typ 2** sein, je nachdem, ob er sofort oder nur unter Bedingungen zuschlägt.

Du brauchst beide Landkarten: die klassische, um fremde Erklärungen und Fehlermeldungen zu verstehen, die eigene, um einzuschätzen, wie gefährlich ein Fehler ist.

### 2. Warum Typ 3 der teuerste ist ⭐

> **Die schädlichste Überzeugung, die ein Anfänger haben kann: „Wenn Python keinen Fehler zeigt, ist mein Programm richtig."**

Typ 1 und Typ 2 sind laut. Sie werfen dir eine rote Meldung hin, oft mit der Zeilennummer. Unangenehm, aber ehrlich — du weißt, dass etwas kaputt ist.

Typ 3 ist still. Dein Programm läuft, gibt Zahlen aus, das Spiel spielt sich. Und trotzdem rechnet irgendwo etwas falsch, seit Wochen, und du hast es nie bemerkt, weil nichts *knallt*. Wenn du ihn findest, dann meist zufällig — und dann fragst du dich, seit wann er drin ist und was er alles verdorben hat.

**Deshalb ist Typ 3 die eigentliche Beute dieser Etappe.** Ihn zu jagen ist die Fähigkeit, die dich von jemandem unterscheidet, der Code nur schreibt, von jemandem, der ihm auch traut — mit Recht.

### 3. Den Traceback von unten nach oben lesen 🧠

Wenn ein Typ-1- oder Typ-2-Fehler zuschlägt, druckt Python einen **Traceback** — den Stapel roter Zeilen, den du seit Etappe 1 kennst und bisher vielleicht überflogen hast. Heute liest du ihn richtig, und das heißt: **von unten nach oben.**

Schau dir diesen an. Ein Kassenprogramm im Restaurant, das durch null teilt:

```python
def teile(a, b):
    return a / b

def rechne_pro_gast(rechnung, gaeste):
    return teile(rechnung, gaeste)

print(rechne_pro_gast(80, 0))
```

Python meldet:

```
Traceback (most recent call last):
  File "kasse.py", line 7, in <module>
    print(rechne_pro_gast(80, 0))
  File "kasse.py", line 5, in rechne_pro_gast
    return teile(rechnung, gaeste)
  File "kasse.py", line 2, in teile
    return a / b
ZeroDivisionError: float division by zero
```

**So liest du das:**

- **Die unterste Zeile** ist die Diagnose: `ZeroDivisionError: float division by zero`. Sie sagt dir, *was* passiert ist. Fang hier an.
- **Die Zeile direkt darüber** ist der Tatort: `return a / b` in `teile`, Zeile 2. Dort ist es passiert.
- **Alles darüber ist der Weg dorthin** — von unten nach oben: `teile` wurde von `rechne_pro_gast` gerufen, das wurde ganz oben aufgerufen. Diese Kette heißt **Aufrufstapel**, und du hast sie in Etappe 7a schon einmal von Hand gesehen.

> **Der wichtigste Satz zum Traceback: Die unterste Zeile sagt dir, *was*. Die zweitunterste sagt dir, *wo*. Der Rest sagt dir, *wie du dorthin gekommen bist*.**

Warum von unten? Weil oben die allgemeine Ursache steht (*„irgendwas beim Ausdrucken"*) und unten die konkrete (*„Teilung durch null in `teile`"*). Du willst zuerst das Konkrete.

### 4. Die Absturzstelle ist selten die Fehlerstelle 🧠

Und jetzt die Falle, die Anfänger zuverlässig eine Stunde kostet: **Wo es knallt, ist nicht, wo der Fehler sitzt.**

Im Beispiel oben knallt es in `teile`, Zeile 2, bei `a / b`. Aber `teile` ist völlig in Ordnung — Teilen ist erlaubt. Der Fehler ist, dass jemand **null Gäste** hereingereicht hat. Der eigentliche Fehler sitzt an der Stelle, wo `gaeste` auf null gesetzt wurde — und die kann drei Funktionen weiter oben liegen.

> **Symptom ist nicht Ursache. Der Absturz ist das Symptom. Die Ursache liegt dort, wo der falsche Wert entstanden ist.**

Deshalb ist der Aufrufstapel Gold wert: Er ist die Spur vom Symptom zurück zur Ursache. Du gehst ihn Zeile für Zeile nach oben und fragst bei jeder: *War der Wert hier schon falsch?* Die erste Zeile, bei der die Antwort *ja* lautet, ist deine Ursache — oder liegt knapp davor.

### 5. Der `print`-Reflex, geschärft: Präfix und `!r`

Bevor der Debugger kommt, ein letzter Schliff an deinem alten Werkzeug. Zwei Kleinigkeiten machen `print`-Debugging deutlich schärfer.

**Erstens ein Präfix**, damit du deine Debug-Zeilen in der Ausgabe wiederfindest und hinterher sicher löschst:

```python
print("### schrott jetzt:", schrott)
```

Das `###` kennst du aus den letzten Etappen. Es hat einen zweiten Zweck: Vor dem Commit suchst du nach `###` und weißt, dass **jede** solche Zeile raus muss.

**Zweitens `!r`.** Schau dir diese zwei Ausgaben an:

```python
wert = "5"
print(f"wert ist {wert}")     # wert ist 5
print(f"wert ist {wert!r}")   # wert ist '5'
```

Die erste Zeile lügt dich nicht an, aber sie verschweigt etwas: Du siehst `5` und denkst *Zahl*. Die zweite mit `!r` zeigt `'5'` — **mit Anführungszeichen**. Jetzt siehst du sofort: Das ist ein **String**, keine Zahl. Genau dieser Unterschied — `"5"` gegen `5` — ist in Etappe 1 dein erster Fehler überhaupt gewesen (das vergessene `int()`), und `!r` macht ihn auf einen Blick sichtbar.

Das `!r` steht **im** Ausdruck, direkt hinter dem Wert, vor der schließenden Klammer. Es zeigt die **repr-Form** eines Werts — die Darstellung, die Anführungszeichen und Struktur mitzeigt.

👀 **Zum Wiedererkennen:** Dasselbe gibt es als Funktion, `repr(wert)`. `f"{wert!r}"` und `f"{repr(wert)}"` sind dasselbe. Du wirst `repr()` in fremdem Code sehen; du selbst nimmst die kürzere Form mit `!r`.

### 6. Der Debugger — anhalten und hineinschauen ⭐

Jetzt das Hauptwerkzeug. Ein Debugger hält dein Programm an einer Stelle deiner Wahl an und lässt dich in aller Ruhe umsehen: jede Variable ansehen, Zeile für Zeile weitergehen, in Funktionen hinein- oder über sie hinwegspringen.

**Die editor-unabhängige Art, die überall funktioniert**, ist eine einzige Zeile:

```python
breakpoint()
```

Wo du sie einfügst, hält das Programm an, sobald es dort ankommt, und du landest in einer Eingabezeile, die mit `(Pdb)` beginnt. Von dort steuerst du mit einzelnen Buchstaben:

| Befehl | Kurz für | Was er tut |
|---|---|---|
| `p name` | *print* | Druckt den Wert einer Variablen. `p schrott` |
| `n` | *next* | Führt die aktuelle Zeile aus und geht zur nächsten — **über** Funktionsaufrufe hinweg |
| `s` | *step* | Wie `n`, aber springt **in** einen Funktionsaufruf hinein |
| `r` | *return* | Läuft bis zum Ende der aktuellen Funktion und hält dort |
| `c` | *continue* | Läuft weiter bis zum nächsten Halt (oder bis zum Ende) |
| `l` | *list* | Zeigt die Zeilen rund um die aktuelle Stelle |
| `q` | *quit* | Bricht ab |

**Ein Detail zu `p`, das dir sonst entgeht:** Es druckt Werte immer in der **repr-Form** aus Konzept 5 — mit Anführungszeichen. `p menge` zeigt dir `'5'`, wenn es ein String ist, und `5`, wenn es eine Zahl ist. Du bekommst das `!r` im Debugger also geschenkt; du musst nichts dazutun.

Die drei Schrittbefehle sind das Herz. `n` (**darüber**) und `s` (**hinein**) sind das Paar, auf das es ankommt:

- Steht der Debugger auf einer Zeile mit einem Funktionsaufruf und du drückst `n`, läuft die ganze Funktion durch und du landest auf der Zeile danach.
- Drückst du stattdessen `s`, steigst du **in** die Funktion hinein und siehst jede ihrer Zeilen einzeln.

**Die Regel dahinter:** Vertraust du der Funktion, geh mit `n` darüber. Verdächtigst du sie, steig mit `s` hinein.

👀 **Wenn dein Editor einen grafischen Debugger hat** — VS Code, PyCharm und Thonny haben einen — dann kannst du dasselbe mit Mausklick: Ein Klick neben die Zeilennummer setzt einen roten Punkt (das ist der Breakpoint), und Knöpfe mit den Namen *Step Over* (= `n`), *Step Into* (= `s`), *Step Out* (= `r`) und *Continue* (= `c`) tun genau das, was die Buchstaben tun. Es ist dasselbe Werkzeug mit einer Oberfläche. Lern ruhig beide — die `breakpoint()`-Zeile läuft überall, auch auf einem fremden Rechner ohne deinen Editor.

⚠️ **Und wie `print`-Zeilen: Ein `breakpoint()` muss vor dem Commit wieder raus.** Ein committetes `breakpoint()` hält das Programm bei jedem an, der es startet.

### 7. Der bedingte Breakpoint — der schärfste Griff ⭐

Hier zahlt sich das Setting aus. Dein Spiel läuft über Hunderte von Runden. Ein einfaches `breakpoint()` in der Hauptschleife würde bei **jeder** Runde anhalten — du drückst dich mit `c` durch hundert Halte, bevor du bei Welle 7 bist, wo der Fehler steckt.

Die Lösung braucht kein neues Werkzeug, nur das `if`, das du seit Etappe 2 kennst:

```python
if welle == 7:
    breakpoint()
```

Jetzt hält das Programm **nur** an, wenn `welle` genau 7 ist, und rauscht durch alle anderen durch. Du kannst die Bedingung so scharf machen, wie du willst:

```python
if welle == 7 and gegner_trefferpunkte < 0:
    breakpoint()
```

*(Warum ausgerechnet „unter null"? Weil das ein Wert ist, den es **nicht geben dürfte** — und genau deshalb ein guter Aufhänger. Dein Balken aus Etappe 3c kappt bewusst nicht, sondern zeigt negative Werte an. Ein bedingter Breakpoint auf einen unmöglichen Zustand ist die schärfste Falle, die es gibt: Er hält genau in dem Moment, in dem etwas kaputtgegangen ist, und in keinem anderen. Suchst du dagegen einen normalen Zustand, nimm einen normalen — `munition == 0` etwa.)*

> **Der bedingte Breakpoint ist der Unterschied zwischen zwei Minuten und einer halben Stunde.** Er ist das schärfste einzelne Werkzeug dieser Etappe.

*(Grafische Debugger können das auch: Rechtsklick auf den roten Punkt, dann eine Bedingung eintippen. Wieder dasselbe Werkzeug, andere Oberfläche.)*

### 8. Halbieren statt Durchsuchen ⭐

Angenommen, irgendwo in einer Kette von acht Schritten schleicht sich ein falscher Wert ein. Du könntest alle acht der Reihe nach durchlesen. Oder du machst es klug:

> **Setz einen `print` oder einen Breakpoint in die *Mitte*. War der Wert dort schon falsch, liegt der Fehler in der ersten Hälfte. War er noch richtig, in der zweiten. Wiederhole. Nach drei Halbierungen hast du aus acht Schritten einen einzigen gemacht.**

Das ist **Halbieren**, und du hast es in Etappe 4 schon gebaut, ohne dass es einen Namen hatte: Dort hast du erst *einen* Gegner zum Laufen gebracht, dann *mehrere*, dann das *Entfernen* — in drei Schritten, nach jedem ausgeführt. Der Grund war genau dieser: Wer alle drei auf einmal baut und dann einen Fehler hat, hat drei Verdächtige. Wer einzeln baut, weiß immer, welcher es war — der letzte.

Halbieren ist dasselbe Verfahren, rückwärts angewandt auf fertigen Code. **Es funktioniert an fast jedem Fehler**, und es ist die Technik, die dich am zuverlässigsten schneller macht. In Etappe 24 halbierst du damit ganze Dateien: *In welchem Modul steckt es?*

### 9. Git als Zeitmaschine 🔨

Du committest seit Etappe 0 nach jeder Etappe. Diese Historie ist nicht nur ein Motivationsbeweis — sie ist ein Debugging-Werkzeug.

Wenn etwas heute kaputt ist, das gestern noch lief, dann liegt der Fehler in dem, was sich seitdem geändert hat. Und das kannst du dir zeigen lassen:

```bash
git diff              # was habe ich seit dem letzten Commit geändert?
git log --oneline     # die Liste meiner Commits, einzeilig
```

`git diff` zeigt dir die Änderungen, die du seit deinem letzten Commit **noch nicht festgeschrieben** hast — grün für neu, rot für entfernt. Wenn der Fehler seit dem letzten Commit entstanden ist, steht seine Ursache mit hoher Wahrscheinlichkeit in diesem `diff`. Das ist Halbieren auf der Zeitachse: Statt den ganzen Code zu verdächtigen, verdächtigst du nur das, was neu ist.

Das ist derselbe `diff`, mit dem du in Etappe 7 bewiesen hast, dass dein Umbau nichts verändert hat. Damals war „keine Änderung" das gute Ergebnis. Heute ist die **angezeigte** Änderung deine erste Spur.

### 10. Wenn der Fehler nicht im Code sitzt — sondern in den Daten 🧠

Nicht jeder Fehler ist eine falsche Zeile Code. Manche sind falsche **Daten**, und die sind besonders heimtückisch, weil der Code völlig korrekt aussieht.

Ein Lager-Beispiel. Diese Funktion ist fehlerfrei:

```python
def nachbar_von(sektor, karte):
    return karte[sektor]

karte = {"nord": "wald", "sued": "see"}
print(nachbar_von("ost", karte))
```

Die Funktion ist fehlerfrei — **solange ihre Annahme stimmt**, dass sie einen Schlüssel bekommt, den es in der Karte gibt. Hier stimmt sie nicht: `"ost"` existiert nicht, und es gibt einen `KeyError`, den du aus Etappe 5 kennst. Die Ursache liegt also nicht in der Zeile, in der es knallt, sondern eine Ebene davor — entweder in den Daten (die Karte ist unvollständig) oder beim Aufrufer (er fragt nach einer Himmelsrichtung, die es nicht gibt). Welches von beiden es ist, musst du entscheiden.

> **Wenn es knallt, prüf nicht nur die Zeile, sondern auch die Annahme, mit der sie aufgerufen wurde.** Das ist Konzept 4 noch einmal, aus einem anderen Winkel.

Und noch subtiler ist die stille Variante aus Etappe 5: Ein Tippfehler **links** vom `=` stürzt nicht ab. `vorrat["srott"] = 40` legt klammheimlich einen neuen Eintrag `"srott"` an, während dein `"schrott"` unverändert bei null bleibt. Kein Traceback, keine Meldung — ein lupenreiner **Typ 3**.

> **Wenn der Code stimmt und trotzdem etwas schiefgeht, verdächtige die Daten.** Diese Fehlerklasse kommt in Etappe 25 groß zurück, wenn deine Daten aus fremden Dateien stammen, die du beim Schreiben nicht im Blick hattest.

### 11. Die Darstellung als Fehleranzeiger 🧠

Dein Balken aus Etappe 3c und deine Anmarschbahn aus Etappe 4 waren immer mehr als Deko. Heute erntest du das.

Ein Balken, der `110 %` oder einen negativen Wert anzeigt, statt bei 100 zu kappen, ist ein **Alarm**: Er macht einen Rechenfehler sichtbar, der in einer nackten Zahl untergegangen wäre. Ein Balken, der brav kappt, hätte den Fehler versteckt. Genau deshalb sollte er in Etappe 3c ausdrücklich **nicht** begrenzen.

Die Anmarschbahn kann noch mehr: Der Fehler „eine Liste verändern, während man über sie läuft" ist in einer Textausgabe unsichtbar — auf der Bahn springt er ins Auge, weil plötzlich ein Gegner zwei Felder weiter steht oder einer verschwindet, den niemand getroffen hat.

> **Deine Darstellung ist Teil des Debugging-Werkzeugkastens. Ein Bild zeigt dir Fehler, die eine Zahl verschweigt.**

### 12. Das Formular: Beobachtung → Hypothese → Experiment ⭐

Zum Schluss das Wichtigste — nicht ein Werkzeug, sondern eine **Denkform**. Sie verhindert die schlechteste aller Debugging-Gewohnheiten: wild etwas ändern, bis es zufällig geht, ohne zu verstehen, warum.

Das Ritual aus dem Rahmenteil — *vorhersagen → ausführen → vergleichen → erklären* — gilt für Code, den du **neu schreibst**. Für Code, der sich **falsch verhält**, gilt sein Gegenstück:

> **Beobachtung → Hypothese → Experiment**
>
> 1. **Beobachtung:** Was genau passiert? Nicht *„es geht nicht"*, sondern *„der Preis ist bei drei Brötchen um sechs Cent zu niedrig"*.
> 2. **Hypothese:** Was könnte die Ursache sein? Eine konkrete, prüfbare Vermutung.
> 3. **Experiment:** Was tust du, um die Hypothese zu prüfen? Ein Breakpoint, ein `print`, ein Testaufruf — und was du dabei erwartest zu sehen.

Der Unterschied zu „rumprobieren" ist das Wort **Hypothese**. Wer eine Hypothese aufschreibt, *bevor* er etwas ändert, lernt bei jedem Experiment etwas — auch wenn die Hypothese falsch war, weiß er danach mehr. Wer nur ändert und guckt, weiß am Ende nur, *dass* es geht, nicht *warum*.

> **„Ich habe etwas geändert und jetzt geht es" ist ein schlechtes Ergebnis.** Es heißt: Der Fehler ist weg, aber du weißt nicht, warum — also weißt du auch nicht, ob er wirklich weg ist oder nur woandershin gewandert.

**Und der eng verwandte Griff, den Fehler zu beschreiben.** Bevor du irgendjemanden — einen Mentor, einen Kollegen, ein Forum — fragst, schreib vier Zeilen:

| Zeile | Frage |
|---|---|
| **Was ich wollte** | Was sollte passieren? |
| **Was passiert** | Was passiert stattdessen — konkret? |
| **Was ich ausgeschlossen habe** | Was habe ich schon geprüft und für unschuldig befunden? |
| **Was ich vermute** | Meine beste Hypothese. |

Der Nutzen liegt in der dritten Zeile. Beim Schreiben merkst du oft, dass du noch **nichts** ausgeschlossen hast — und prüfst es, statt zu fragen. Ein erschreckender Anteil aller Fehler löst sich, während man sie beschreibt. Der Name dafür ist **Rubber-Duck-Debugging**: Man erklärt das Problem einer Gummiente auf dem Schreibtisch, und beim Erklären fällt einem die Lösung ein. In Etappe 3 ist dir diese Form schon einmal kurz begegnet; heute wird sie zum festen Griff, und in Etappe 16 zum verbindlichen Dreizeiler.

---

## Dein Auftrag

Anders als sonst baust du heute kein Spielfeature. Du legst **zwei Dokumente** an und **übst jedes Werkzeug einmal** — teils an eigens gebauten kleinen Fehlern, teils an deinem echten Spiel. Durchlaufende Nummerierung, nach jedem Schritt das tun, was dransteht.

⚠️ **Das hier ist die vollständige Liste. Wenn diese Schritte stehen, bist du fertig** — auch wenn dein Spiel danach nicht „fehlerfrei" ist. Fehlerfreiheit ist nicht das Ziel; ein Verfahren ist das Ziel.

### 1. Leg das Fehlertagebuch an

- Erstell im Repo eine Datei `FEHLERTAGEBUCH.md`.
- Jeder Eintrag ist **eine Zeile aus zwei Teilen**: das Symptom, dann — und das ist der wichtige Teil — **wie du den Fehler gefunden hast**. Etwa: *„Schrott blieb nach dem Kauf unverändert — mit `p schrott` vor und nach dem Kauf gefunden."*
- Schreib als ersten Eintrag den letzten echten Fehler hinein, an den du dich aus einer früheren Etappe erinnerst.

*(Warum der Fundweg der wichtige Teil ist: Der Fehler selbst kommt nie wieder. Das Verfahren, mit dem du ihn gefunden hast, schon. Das Symptom steht nur deshalb daneben, weil du in Etappe 26 aus jedem dieser Einträge einen Test baust — und dafür musst du wissen, **was** falsch war, nicht nur wie du es gemerkt hast. Zwei knappe Halbsätze reichen; das hier soll kein Fehlerbericht werden.)*

### 2. Leg das Format fürs Debugging-Protokoll fest

- Halt in `GELERNT.md` (oder einer eigenen Notiz) das Vier-Zeilen-Formular aus Konzept 12 fest: *was ich wollte · was passiert · was ich ausgeschlossen habe · was ich vermute*.
- Das ist die Vorlage, die du ab jetzt bei jedem echten Fehler ausfüllst, bevor du fragst.

### 3. Übe den Traceback an drei selbst gebauten Abstürzen

Bau in einer **Wegwerf-Datei** (nicht in `spiel.py`) nacheinander drei Abstürze und lies jeden Traceback von unten nach oben:

- **Einen Syntaxfehler:** Lass irgendwo eine Klammer weg. Was meldet Python, und läuft überhaupt eine Zeile?
- **Einen Laufzeitfehler mit Aufrufstapel:** Schreib zwei Funktionen, von denen die eine die andere ruft, und lös in der inneren eine Teilung durch null oder ein `int("abc")` aus. Lies den Stapel: Welche Zeile ist die Diagnose, welche der Tatort, welche der Weg?
- **Einen logischen Fehler:** Schreib eine Funktion, die einen Rabatt abziehen soll, aber ihn addiert. Sie läuft sauber. Woran merkst du, dass sie falsch ist?

Ordne jeden der drei **beiden** Landkarten zu (klassisch **und** Typ 1/2/3).

### 4. Setz deinen ersten `breakpoint()` in dein echtes Spiel

- Setz ein `breakpoint()` an eine Stelle in deiner Hauptschleife, an der eine Runde abgehandelt wird.
- Starte das Spiel. Wenn `(Pdb)` erscheint, tipp zuerst `l` — wo genau stehst du gerade?
- Sieh dir mit `p` drei Variablen an — etwa `p schrott`, `p munition`, und was bei dir gerade interessant ist. **Achte darauf, bei welchen davon Anführungszeichen erscheinen.** Das ist die repr-Form aus Konzept 5, und sie sagt dir auf einen Blick, was ein String ist und was eine Zahl.
- Geh mit `n` ein paar Zeilen weiter. Steig mit `s` einmal **in** eine deiner Funktionen hinein und mit `r` wieder heraus.
- Beende mit `c` oder `q`. **Nimm das `breakpoint()` danach wieder heraus.**

### 5. Setz einen bedingten Breakpoint

- Setz `breakpoint()` so, dass es **nur** in einer bestimmten Welle hält — `if welle == 7:` davor (nimm eine Wellennummer, die dein Spiel erreicht).
- Starte und prüf: Rauscht das Spiel durch die Wellen davor und hält erst bei der richtigen?
- Sieh dir im Halt an, was du sonst nur vermutet hättest. `breakpoint()` danach raus.

### 6. Übe Halbieren an einem eigenen Fehler

- Bau in einer Wegwerf-Datei eine Kette von sechs bis acht Rechenschritten, bei der am Ende ein falscher Wert herauskommt (bau den Fehler absichtlich in die Mitte ein).
- Finde ihn **nicht** durch Lesen, sondern durch Halbieren: einen `print` in die Mitte, dann in die Mitte der schuldigen Hälfte, und so weiter.
- **Schreib jede dieser `print`-Zeilen mit `###`-Präfix und mit `!r`**, so: `print(f"### nach Schritt 4: {zwischenwert!r}")`. Am Ende suchst du nach `###` und weißt, dass alle raus müssen.
- Notier im Fehlertagebuch, nach wie vielen Halbierungen du ihn hattest.

### 7. Die Bug-Jagd — an deinem echten Spiel

Jetzt die eigentliche Jagd. **Sie ist die große Knobelstelle dieser Etappe** — das Problem wird gestellt, nicht das Verfahren. Hängenbleiben ist hier kein Zeichen von Unverständnis, sondern der Sinn der Übung.

- **Wenn du einen KI-Mentor hast:** Bitte ihn, dir deinen Code mit eingebauten Fehlern zurückzugeben — ohne zu sagen, wie viele und wo. Jag sie mit den Werkzeugen dieser Etappe. Für jeden gefundenen Fehler ein Eintrag im Fehlertagebuch (*wie gefunden*).
- **Wenn du keinen Mentor hast, nimm die Zeitversatz-Methode:** Schreib jetzt eine Liste von **zehn Sabotagen**, die man an deinem Spiel anrichten könnte — je eine pro Fehlertyp, dazu die Kandidaten aus dem Kaputtmachen unten. Leg sie weg. **Warte zwei Tage.** Dann misch die Liste, bau **die obersten drei** ein und jag sie.

⚠️ **Zwei Dinge zur Zeitversatz-Methode, damit sie funktioniert.**

**Erstens: Die Wartezeit ist der ganze Mechanismus, nicht Zierde.** Zufällig auswählen reicht nicht — du hast die zehn Sabotagen selbst geschrieben und weißt bei jeder sofort, wo sie sitzt. Erst der Abstand von ein paar Tagen macht dich wieder blind. **Das blockiert die Etappe nicht:** Mach alle anderen Schritte heute fertig, committe, und hol Schritt 7 in zwei Tagen nach.

**Zweitens — und das gilt für beide Varianten:** ⚠️ **Zieh während der Jagd kein `git diff`.** Wenn du manipulierten Code über deine committete Datei legst, zeigt dir `diff` alle eingebauten Fehler auf einen Schlag, und die Übung ist vorbei. Das ist kein Mangel des Werkzeugs, sondern der Beweis, wie stark es ist — heb es dir für Schritt 9 auf.

### 8. Fehler beschreiben — der Vierzeiler auf einen echten Fund

- Nimm einen der Fehler aus Schritt 7 und füll das Vier-Zeilen-Formular aus Konzept 12 vollständig aus, **bevor** du ihn behebst.
- Achte auf die dritte Zeile. Wenn dort *„nichts"* steht, hast du noch nichts ausgeschlossen — dann schließ zuerst etwas aus.

### 9. Aufräumen und committen

- **Führ zuerst `git diff` aus, bevor du irgendetwas aufräumst.** Was du dort grün siehst, ist alles, was du in dieser Etappe angefasst hast — jedes `breakpoint()`, jede `###`-Zeile. Das ist der Beweis, dass `diff` dein Suchraum ist: Statt die ganze Datei zu durchsuchen, liest du nur, was neu ist.
- Führ danach einmal `git log --oneline` aus. Wie viele Commits stehen da inzwischen?
- Durchsuch dein Spiel nach `###`-Zeilen und nach `breakpoint()`. **Jede** muss raus.
- Prüf, dass keine Entwicklerbefehle (`gott`, `+munition` und dergleichen aus Etappe 3) im Spielcode stehen geblieben sind — bei der nächsten Jagd wären sie Verdächtige.
- Führ das Spiel ein letztes Mal ganz durch. Läuft es wie vorher?
- Commit: `Etappe 8: Bug-Jagd bestanden`

---

## Was NICHT in diese Etappe gehört

⚠️ **Debugging ist nicht Fehlerbehandlung. Verwechsle die beiden nie.**

Es ist verlockend, jetzt überall `try`/`except` einzubauen, damit nichts mehr abstürzt. **Tu das nicht.** Das ist ein anderes Thema und kommt in Etappe 20. Der Unterschied ist grundlegend:

| | Debugging (heute) | Fehlerbehandlung (Etappe 20) |
|---|---|---|
| Frage | *Warum* verhält sich das Programm falsch? | Wie bleibt es stehen, statt abzustürzen? |
| Wann | Während du entwickelst | Wenn der Spieler Unsinn eingibt |
| Ergebnis | Du findest und behebst die Ursache | Das Programm fängt den Fehler ab und macht weiter |

Ein Absturz beim Entwickeln ist **hilfreich** — er zeigt dir, wo es hakt. Ihn mit `except` zu verschlucken, bevor du ihn verstanden hast, verwandelt einen ehrlichen Typ 1 in einen stillen Typ 3. Das ist genau der Fehler, den Etappe 20 dir zeigt.

**Ebenfalls nicht heute:** Tests schreiben. Das schriftliche Protokoll und das Fehlertagebuch sind Vorarbeit dafür — in Etappe 26 wird jeder Tagebucheintrag ein Testkandidat. Aber `pytest` fasst du erst dort an.

**Und nicht:** dein Spiel „absichern", bis es wasserdicht ist. Du hast heute ein Verfahren gelernt, keine Pflicht zur Perfektion.

---

## Selbsttest

Diese prüfen einen **Zustand**, nicht dein Selbstbild. Wenn du bei einem nein sagen musst, geh zurück.

- [ ] Es gibt eine Datei `FEHLERTAGEBUCH.md` mit mindestens einem Eintrag, und der Eintrag sagt, **wie** der Fehler gefunden wurde.
- [ ] Du hast in einer Wegwerf-Datei drei Abstürze erzeugt und kannst zu jedem sagen, welche Traceback-Zeile die Diagnose und welche der Tatort war.
- [ ] Du hast in deinem echten Spiel ein `breakpoint()` gesetzt, mindestens drei Variablen mit `p` angesehen, und es danach wieder entfernt.
- [ ] Du hast einen bedingten Breakpoint gesetzt, der nur in einer bestimmten Welle hielt.
- [ ] Du hast beim Halbieren `print`-Zeilen mit `###`-Präfix **und** `!r` benutzt und kannst sagen, was `!r` dir gezeigt hat.
- [ ] Du hast `git diff` einmal ausgeführt und weißt, was es anzeigt und was nicht.
- [ ] In `spiel.py` steht **kein** `breakpoint()`, **keine** `###`-Zeile und **kein** Entwicklerbefehl mehr.
- [ ] Das Spiel läuft nach der Etappe genauso wie vorher — die Bug-Jagd hat es nicht dauerhaft verändert (außer bei echten Fehlern, die du behoben hast).
- [ ] Der Commit `Etappe 8: Bug-Jagd bestanden` ist gesetzt.

---

## Lernziele

Als Fragen. Beantworte sie in `GELERNT.md`, ohne nachzuschlagen.

1. Was sind die drei Fehlertypen, und woran unterscheiden sie sich?
2. **Warum ist Typ 3 der gefährlichste?** Welche Anfängerüberzeugung zerstört er?
3. In welcher Richtung liest man einen Traceback, und was sagt die unterste Zeile, was die zweitunterste?
4. Warum ist die Absturzstelle selten die Fehlerstelle?
5. Wann nimmst du den Debugger, wann `print()`?
6. Was macht `s` anders als `n` im Debugger?
7. Warum ist ein bedingter Breakpoint in diesem Spiel besonders wertvoll?
8. Was ist Halbieren, und warum ist es schneller als Durchlesen?
9. Welche vier Angaben gehören in eine gute Fehlerbeschreibung — und welche der vier ist die nützlichste?
10. Warum ist „ich habe etwas geändert und jetzt geht es" ein schlechtes Ergebnis?
11. Was ist der Unterschied zwischen Debugging und Fehlerbehandlung?

**Frage 2 ist die wichtigste.** Alles andere ist Werkzeug; Frage 2 ist die Haltung, ohne die die Werkzeuge nichts nützen. Wer Typ 3 ernst nimmt, traut seinem eigenen Code nicht blind — und das ist der Anfang von allem.

**Frage 4 ist die kniffligste** und deckt das Missverständnis auf, das die meiste Debugging-Zeit kostet.

---

## Transferaufgabe (10–15 Minuten)

**Außerhalb des Spiels**, in einer Wegwerf-Datei. Ein Wartezimmer, kein Vorposten.

Hier ist ein fremdes Programm mit einem **Typ-3-Fehler**. Es läuft, stürzt nicht ab — und **bricht trotzdem das Versprechen, das sein Docstring gibt**. Lies den Docstring zuerst und merk dir, was er zusagt:

```python
def naechster_dran(schlange, neuankunft):
    """Gibt den Namen zurueck, der als Naechstes drankommt,
    ohne die uebergebene Warteliste zu veraendern."""
    schlange.append(neuankunft)
    return schlange[0]

warteliste = ["Ada", "Bo"]
print("dran:", naechster_dran(warteliste, "Cleo"))
print("Warteliste danach:", warteliste)
```

1. **Sag voraus**, was die zweite `print`-Zeile ausgibt, **bevor** du es ausführst. Schreib die Vorhersage auf.
2. Führ es aus. Stimmt deine Vorhersage?
3. **Finde mit dem Debugger heraus, an welcher Zeile sich `warteliste` verändert.** Setz ein `breakpoint()` und sieh dir die Liste vor und nach jeder Zeile an.
4. **Erklär in einem Satz, warum das passiert.** Der Grund steht nicht in dieser Etappe, sondern in Etappe 4 — und du hast ihn in Etappe 7, Experiment 2 und 3, von zwei Seiten gesehen.
5. **Repariere es**, ohne den Docstring zu ändern. Die Funktion darf die übergebene Liste nicht mehr anfassen. *(Ein Werkzeug aus Etappe 4 macht dir eine unabhängige Kopie.)*

Diese Aufgabe verbindet die veränderbaren Objekte aus Etappe 4 mit dem, was du heute gelernt hast: einen stillen Fehler sichtbar machen. **Und sie ist die Sorte, die in Etappe 15 wiederkommt** — eine fremde Funktion mit einer stillen Annahme.

---

## Kaputtmachen

Bau die folgenden Fehler **absichtlich** in dein Spiel ein, jag sie mit den heutigen Werkzeugen und bau sie danach zurück. **Vor jedem: aufschreiben, was passieren wird.** Für jeden: ein Eintrag im Fehlertagebuch, *wie gefunden*.

Acht Trainingsbugs — einer je Fehlertyp, dazu die klassischen Fallen:

**1. Ein Syntaxfehler (Typ 1).** Lass irgendwo eine Klammer oder einen Doppelpunkt weg. Startet das Programm? Was meldet Python, und in welcher Zeile?

**2. Ein Laufzeitfehler unter Bedingung (Typ 2).** Sorg dafür, dass irgendwo durch eine Variable geteilt wird, die *manchmal* null ist. Bei welcher Eingabe knallt es, bei welcher nicht?

**3. Ein logischer Fehler (Typ 3).** Ändere in einer Rechnung ein `+` zu `-` oder ein `>` zu `<`. Das Spiel läuft weiter — **woran** merkst du überhaupt, dass etwas falsch ist? (Das ist die schwerste und wichtigste Übung.)

**4. Der fast richtige Vergleich.** Ändere die Wellen-Abbruchbedingung von `>` auf `>=` (oder umgekehrt). Läuft eine Welle zu viel oder zu wenig? Das ist ein **Off-by-One** — die eigene Fehlerkategorie für alles, was um genau eins danebenliegt, weil der Mensch ab 1 zählt und Python ab 0.

**5. Das vergessene `return`.** Nimm aus deiner Schadensrechnung das `return` heraus. Was steht danach in der Variablen, die das Ergebnis aufnehmen sollte — und wo genau knallt es? *(Dieselbe Falle wie das `None` von `append()` in Etappe 4.)*

**6. Der Fehler in den Daten, nicht im Code.** Frag einen Nachbar-Sektor ab, den es nicht gibt — einen Namen, der in deiner Karte fehlt. Der Code ist korrekt, der `KeyError` kommt trotzdem. Woran erkennst du, dass die Ursache in den Daten liegt und nicht in der Funktion?

**7. Der stille Tippfehler links vom `=`.** Verschreib dich beim Anlegen eines Vorrats-Schlüssels (`vorrat["srott"]` statt `"schrott"`). Kein Absturz. Was passiert stattdessen mit deinem echten Schrott, und wie findest du es? *(Reiner Typ 3, aus Etappe 5.)*

**8. Zwei Fehler gleichzeitig.** Bau zwei der obigen zusammen ein. Jetzt zählt das Halbieren: Kannst du sie **einzeln** einkreisen, statt beide auf einmal zu suchen?

---

**Der Off-by-One (Nr. 4) und der stille Tippfehler (Nr. 7) sind das Paar, auf das es ankommt** — beide liegen um genau eine Kleinigkeit daneben, beide stürzen nicht sofort ab, und beide findest du nur, indem du **nachsiehst**, statt zu vermuten.

Alles in `GELERNT.md` und ins Fehlertagebuch, mit dem einen Satz: **woran du es erkannt hast.**

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `(Pdb)` erscheint, aber die Buchstaben tun nichts Erwartetes | Ein Wort statt eines Befehls getippt, oder eine Variable heißt wie ein Befehl | Nur `p name` druckt; `n s r c l q` sind die Schritte |
| Das Programm hält bei **jeder** Runde an | Ein `breakpoint()` ohne Bedingung in der Schleife | Konzept 7 — ein `if welle == …` davor |
| Nach dem Commit hält das Spiel bei jedem an | Ein `breakpoint()` blieb im Code | Vor dem Commit nach `breakpoint` **und** `###` suchen |
| Der Traceback ist lang und unübersichtlich | Von oben gelesen | Von **unten** anfangen — die letzte Zeile zuerst |
| „Es knallt in `teile`, aber `teile` ist doch richtig" | Symptom mit Ursache verwechselt | Konzept 4 — den Aufrufstapel nach oben gehen |
| `f"{wert!r}"` zeigt Anführungszeichen, `f"{wert}"` nicht | Genau der Zweck von `!r` — es zeigt die repr-Form | Konzept 5 — Anführungszeichen heißt: String |
| Der Debugger findet den Fehler nicht | Der Fehler ist ein Typ 3 — es knallt nirgends | Nicht den Absturz suchen, sondern den **falschen Wert** — Halbieren |
| `git diff` zeigt nichts | Alles ist schon committet | Der Fehler ist älter als der letzte Commit — `git log --oneline` |
| Ein `except` „behebt" den Fehler | Es verschluckt ihn nur | Das ist Etappe 20, nicht heute — Fehler erst verstehen |

**Der Debugging-Reflex dieser Etappe löst alle früheren ab: „Halt an und sieh nach."**

In Etappe 1 war es *welchen Typ hat dieser Wert?*, in 2 *welcher Zweig?*, in 3 *wie oft?*, in 4 *was steht drin?*, in 5 *unter welchem Namen?*, in 6 *welche Struktur?*, in 7 *was geht rein, was raus?*. Jeder davon war ein `print`. Heute ersetzt **ein** `breakpoint()` sie alle:

```python
breakpoint()   # und dann: p wert, p type(wert), n, s, ...
```

**Nachsehen schlägt Vermuten**, seit Etappe 1. Der Debugger ist nur die schärfste Art nachzusehen — der Reflex bleibt derselbe.

---

## Ein Blick nach vorne

**Etappe 9 macht deinen Code zu Objekten.** Und dein neuer Debugger bekommt dort sofort einen zweiten Zahn: Ohne Zutun zeigt `print(marine)` etwas wie `<__main__.Marine object at 0x7f3a…>` — die nutzloseste Ausgabe der Sprache. Mit `__repr__` (Etappe 9b) siehst du im Debugger stattdessen auf einen Blick, was im Objekt steckt. Das `!r` von heute ist die kleine Vorschau darauf.

**Etappe 12 — der Tick — ist der erste Ort, an dem der bedingte Breakpoint richtig glänzt.** *„Halt an, wenn `welle == 7`"* zusammen mit dem beobachteten Tick ist das schärfste Debugging-Werkzeug des ganzen Plans.

**Etappe 16 ist die Bug-Jagd II.** Dort liegen Ursache und Symptom weiter auseinander als heute — und dort wird aus deinem Formular *Beobachtung → Hypothese → Experiment* ein verbindlicher Dreizeiler. Dein Fehlertagebuch von heute ist das Übungsobjekt.

**Etappe 20 ist die Fehler*behandlung*** — das Gegenstück, das du heute bewusst weggelassen hast. Dort lernst du, warum ein nacktes `except:` einen ehrlichen Typ 1 in einen stillen Typ 3 verwandelt.

**Etappe 24 halbiert ganze Dateien.** Dasselbe Verfahren wie heute, eine Ebene höher: nicht *welche Zeile*, sondern *welches Modul*. Und `git diff` bekommt dort Branches als Nachbarn.

**Etappe 25 bringt den Datenfehler groß zurück.** Der stille Tippfehler von heute wird dort zum Normalfall, weil deine Daten aus fremden Dateien kommen, die du beim Schreiben nicht gesehen hast.

**Etappe 26 verwandelt dein Fehlertagebuch in Tests.** Jeder Eintrag — *wie gefunden* — ist ein Kandidat für einen Test, der sicherstellt, dass genau dieser Fehler nie wiederkommt.

**Etappe 27 ist die Prüfung:** ein ganzes fremdes Repo, ohne Hilfe. Der Debugger mit einem Breakpoint an der ersten Zeile ist dort dein erstes Werkzeug, und das Formular wendest du an, ohne etwas ändern zu dürfen.

---

## Abschluss

**In `GELERNT.md`:**

- Was habe ich gebaut? *(Ehrliche Antwort: kein Feature — ein Verfahren und zwei Dateien.)*
- Was habe ich verstanden?
- Was hat mich überrascht? *(Kandidaten: dass Typ 3 nie knallt · dass die Absturzstelle nicht die Fehlerstelle ist · wie viel schneller Halbieren war.)*
- Welchen Fehler habe ich in der Bug-Jagd am schwersten gefunden — und **wie** habe ich ihn schließlich gefunden?
- **Die Design-Entscheidung:** Wann nehme ich den Debugger, wann `print()`? Und was war meine Erfahrung damit?
- Wie hat es sich angefühlt, einen Fehler zu jagen, den ich nicht sehen konnte, weil nichts abgestürzt ist?

**Vor dem Commit:** Sind alle `breakpoint()` und alle `###`-Zeilen raus? Stehen keine Entwicklerbefehle mehr im Spielcode?

**Damit ist Block 1 abgeschlossen.** Du hast ein Fundament: Werte, Bedingungen, Schleifen, Datenstrukturen, Funktionen — und jetzt die Fähigkeit, herauszufinden, warum sie sich falsch verhalten. Ab Etappe 9 kommen Objekte, und mit ihnen die Leseübungen.

---

## Wenn du mehr willst

Erst bei grünem Selbsttest. Alles freiwillig.

**Lies einen deiner alten Tracebacks noch einmal — den ganzen Stapel.** Nimm einen Absturz aus einer früheren Etappe (oder bau einen tief verschachtelten nach) und schreib zu **jeder** Zeile des Stapels dazu, was sie bedeutet: Diagnose, Tatort, Weg. Du wirst merken, dass du sie vorher nur überflogen hast.

**Bau den `git bisect`-Gedanken von Hand nach.** Du hast einen Fehler, der vor fünf Commits noch nicht da war. Statt alle fünf zu lesen, spring per `git log --oneline` in die Mitte, prüf dort, und halbier weiter. Das ist Halbieren auf der Zeitachse — und genau das automatisiert Etappe 24.

**Schreib die zehn Sabotagen aus Auftrag 7 zu Ende, auch wenn du nur drei gebraucht hast.** Die Liste ist Gold für später: In Etappe 16 und 26 hast du damit sofort Übungsmaterial, das du dir nicht neu ausdenken musst. Leg sie unter `sabotagen.md` ab.

**Erklär einen deiner Fehler laut einer Gummiente** (oder der Wand, oder dem Hund). Vollständig, von vorn, ohne abzukürzen. Zähl mit, wie oft dir die Lösung mitten im Satz einfällt. Das ist keine Spielerei — es ist die billigste Debugging-Technik, die es gibt.

---

> **Nächste Etappe:** Etappe 9 — Alles wird zum Objekt · Klassen, `__init__`, Methoden, und der Debugger lernt, in deine Objekte zu schauen
