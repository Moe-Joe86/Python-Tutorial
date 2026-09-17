# Etappe 16 — Bug-Jagd II

*v1.0.0 · 2026-09-16*

> **Block 2: Einheiten und Zeit** · Etappe 16 von 30 · [← Etappe 15](etappe-15-was-die-brut-hinterlaesst.md) · [Lehrplan](../Vorposten_Lehrplan.md) · Etappe 17 →

**Neue Syntax heute:** Keine. Nicht eine Zeile.

**Zeitaufwand:** 4–5 Sitzungen à 20–30 Minuten. Rund 28 Minuten Lesestoff, eine Portion. **Der Zeitaufwand liegt fast vollständig im Suchen, nicht im Lesen.**

⚠️ **Diese Etappe baut kein Feature.** Am Ende des Abends kann dein Spiel exakt so viel wie vorher — und es tut endlich, was du glaubst, dass es tut. **Das ist die letzte Etappe von Block 2, und sie ist der Grund, warum Block 3 tragfähig ist.** Wer mit vier stillen Fehlern in den Wellengenerator geht, sucht ab Etappe 17 in zwei Systemen gleichzeitig.

**Voraussetzung:** Etappen 12 bis 15 abgeschlossen. Du brauchst den Tick, die Zähler, das Raster und die Erkenntnisse — **und vor allem die vier Notizen, die du unterwegs in `GELERNT.md` geschrieben hast.** Sie sind heute dein wichtigstes Werkzeug.

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Die Tick-Tabelle von Hand · der Dreizeiler als Pflicht · die Fahndungsliste abarbeiten · eine Bisektion über vier Etappen | Reihenfolgefehler als eigene Ursachenklasse · warum „nur eine Sache auf einmal" die schwerste Regel ist · Ursache und Symptom liegen jetzt weit auseinander | — |

---

## Worum es geht

In Etappe 8 hast du gelernt, Fehler zu jagen. Damals war dein Spiel ein Programm mit Funktionen, einer Schleife und ein paar Dictionaries. **Heute ist es etwas anderes:** Es tickt, es zählt herunter, es bewegt Dinge auf einem Raster, es merkt sich etwas über Wellen hinweg, und zwölf Objekte handeln in jedem Zeitschritt ohne dein Zutun.

**Und das verändert die Sorte Fehler, die darin steckt.**

Etappe 8 hatte Abstürze, falsche Zahlen und einen Fehler in den Daten. Die waren ärgerlich, aber sie hielten still: Eine Funktion mit falschem Ergebnis hat falsche Ergebnisse, jedes Mal, reproduzierbar.

**Die Fehler, die seit Etappe 12 dazugekommen sind, sind anders.** Sie hängen nicht davon ab, *was* dein Code tut, sondern **wann**:

> **Ein Gegner, der einen Takt zu früh getroffen wird, stirbt ein Feld zu weit vorne. Ein Zähler, der in der falschen Phase läuft, ist einen Tick zu spät fertig. Eine Fähigkeit, die vor statt nach dem Aufräumen prüft, findet ein Ziel, das es nicht mehr gibt.**

**Keiner dieser Fehler stürzt ab.** Keiner produziert eine rote Zeile. Dein Spiel läuft, es spielt sich, die Zahlen sehen plausibel aus — und ab Welle zwölf hält dein Tor nicht, und du weißt nicht, warum.

**Das ist die Beute dieser Etappe.** Und der Weg dorthin ist kein Werkzeug, sondern Geduld:

> **Du schreibst einen einzigen Tick von Hand auf, Phase für Phase, Einheit für Einheit. Dann lässt du dasselbe von deinem Programm machen und vergleichst Zeile für Zeile.**

Das klingt nach Fleißarbeit. Es ist Fleißarbeit. **Und es ist die einzige Methode, die bei dieser Fehlerklasse zuverlässig funktioniert** — Lesen findet sie nicht, Herumprobieren findet sie nicht, und ein Debugger zeigt dir nur, was passiert, nicht, was hätte passieren sollen.

---

## Der lange Bogen — was heute fällig wird

Diese Etappe ist die am weitesten vorbereitete des ganzen Plans. **Neun Etappen haben Kandidaten für heute abgelegt:**

- **Etappe 3c:** Zwei Werte für dieselbe Aussage — `munition > 0` und `nachladen_noetig`.
- **Etappe 4 und 10:** Zwei Namen, ein Objekt. In Etappe 14a ist daraus `[["."] * 5] * 5` geworden.
- **Etappe 5:** Die Namensfalle — zwei Gesundheitswerte, die nie verwechselt werden dürfen.
- **Etappe 6:** Der Schmerz paralleler Listen und die Komma-Falle `(5)` gegen `(5,)`.
- **Etappe 10:** Der veränderbare Standardwert in `__init__`, der erst beim **zweiten** Objekt auffällt.
- **Etappe 11:** Eine Methode ohne Klammern im `if` ist immer wahr.
- **Etappe 12:** Sammeln und danach entfernen — und die Tick-Reihenfolge, die du dort aufgeschrieben hast.
- **Etappe 13, 14a, 14b:** Drei schriftliche Entscheidungen, die alle Off-by-one sind.
- **Etappe 15:** Ein Flag-Wort, das ins Leere verweist.

**Und die Einlösung aus Etappe 8:** Das Formular *Beobachtung → Hypothese → Experiment* war dort eine Denkform. Heute wird es Pflicht, mit einer Regel dazu, die schwerer ist, als sie klingt.

---

## Die Konzepte

### 1. Die dritte Ursachenklasse: die Reihenfolge ⭐⭐

Etappe 8 hat dir zwei Landkarten gegeben. Die eine sagt, **wann** ein Fehler auffällt — Typ 1 sofort, Typ 2 irgendwann, Typ 3 nie. Die andere sagt, **wo** er sitzt: im Code oder in den Daten.

**Heute kommt eine dritte Antwort auf die Wo-Frage dazu, und sie ist keine von beiden:**

> **Der Fehler sitzt weder im Code noch in den Daten. Er sitzt in der Reihenfolge, in der richtiger Code auf richtige Daten trifft.**

Jede einzelne Zeile ist korrekt. Jeder Wert stimmt. **Nur die Abfolge ist eine andere, als du im Kopf hattest** — und dein Kopf ist die einzige Stelle, an der die richtige Abfolge je gestanden hat.

⚠️ **Auf der Zeitachse ist das immer ein Typ-3-Fehler.** Er läuft, er stürzt nie ab, er liefert plausible Zahlen. Deshalb ist er teurer als alles, was du in Etappe 8 gejagt hast.

**Und hier ist er, in vollständiger Länge.** Ein Turm mit sechs Schaden, ein Kriecher mit zwölf Trefferpunkten, ein Feld vor dem Tor. **Derselbe Code. Zwei vertauschte Zeilen im Tick.**

```
=== Phase „Gegner zuerst"            === Phase „Trupp zuerst"
Tick 1                               Tick 1
  Turm trifft Kriecher: 12 -> 6        Turm trifft Kriecher: 12 -> 6
Tick 2                               Tick 2
  Kriecher schlägt in den Kern (95)     Turm trifft Kriecher: 6 -> 0
  Turm trifft Kriecher: 6 -> 0          Kriecher fällt auf Feld 0
  Kriecher fällt auf Feld 0
Tick 3                               Tick 3

  ERGEBNIS: Kernintegrität 95          ERGEBNIS: Kernintegrität 100
```

**Fünf Punkte Unterschied, ein Gegner, drei Ticks.** Rechne das auf zwanzig Wellen mit acht Gegnern hoch, und der Unterschied ist, ob dein Spiel gewinnbar ist.

> **Es gibt keine richtige Reihenfolge, die ich dir nennen könnte. Es gibt nur die, für die du dich entscheidest — und die dann überall gilt.**

### 2. Warum Lesen diese Fehler nicht findet 🧠

Du kannst deinen Tick zehnmal lesen und nichts bemerken. **Der Grund ist nicht Unaufmerksamkeit, sondern etwas Unangenehmeres:**

> **Beim Lesen von Code füllt dein Kopf die Lücken mit dem, was du gemeint hast. Beim Ausführen füllt Python sie mit dem, was dasteht.**

Du liest `for g in self.gegner: g.update(self)` und denkst *„dann bewegen sich die Gegner"*. Dein Kopf legt automatisch dazu, dass sie sich zum richtigen Zeitpunkt bewegen, weil du beim Schreiben wusstest, wann das sein sollte. **Dieses Wissen steht nirgends im Code. Es steht in deiner Erinnerung, und die verblasst.**

**Deshalb ist die Tick-Tabelle keine Zusatzübung, sondern das Werkzeug.** Sie zwingt dich, die Abfolge **aufzuschreiben, bevor** du sie ausführst — und damit eine Vorhersage zu treffen, die falsch sein kann. Ein Kopf, der mitliest, kann nicht falsch liegen. Ein Blatt Papier schon.

*(Das ist genau das Ritual aus dem Rahmenteil — vorhersagen, ausführen, vergleichen —, nur auf einen ganzen Zeitschritt angewendet statt auf eine Zeile.)*

### 3. Die Tick-Tabelle ⭐⭐

**So sieht sie aus.** Eine Spalte pro Einheit, eine Zeile pro Phase, und in jeder Zelle der Zustand **nach** dieser Phase:

| Phase | Gegner A | Gegner B | Turm | Marine (KI) |
|---|---|---|---|---|
| **Start** | Feld 2, 10 HP | Feld 4, 8 HP | bereit | Feld 1 |
| 1. Zeit | — | — | — | — |
| 2. Zähler | — | — | bereit | — |
| 3. Trupp handelt | 10 → 4 | 8 | bereit | Feld 2 |
| 4. Gegner handeln | Feld 1 | Feld 3 | bereit | Feld 2 |
| 5. Aufräumen | Feld 1, 4 HP | Feld 3, 8 HP | bereit | Feld 2 |

**Drei Regeln, ohne die sie nichts wert ist:**

- **Die Zeilen sind deine Phasen, nicht meine.** Schreib sie aus deiner Notiz aus Etappe 12 ab, in deiner Reihenfolge, mit der Zählerphase aus Etappe 13 und der Einsammelphase aus Etappe 15.
- **Jede Zelle wird gefüllt, auch wenn sich nichts ändert.** Ein Strich ist eine Aussage: *hier passiert nichts.* Eine leere Zelle ist keine.
- **Zuerst die ganze Tabelle, dann erst das Programm.** Wer nebenher mitlaufen lässt, schreibt ab statt vorherzusagen — und hat sich um die einzige nützliche Zeile gebracht.

⚠️ **Nimm eine kleine Lage.** Zwei Gegner, ein Marine, der Turm. Drei Ticks. **Eine Tabelle mit zwölf Einheiten füllt niemand ehrlich aus**, und eine unehrlich ausgefüllte Tabelle ist schlimmer als keine: Sie bestätigt dir, was du ohnehin geglaubt hast.

### 4. Der Dreizeiler — ab heute Pflicht ⭐

In Etappe 8 war er eine Denkform. **Ab heute schreibst du ihn hin, bevor du eine einzige Zeile Code änderst:**

```
Beobachtung:   Was siehst du? Kein Urteil, nur die Beobachtung.
Hypothese:     Was vermutest du als Ursache?
Experiment:    Was änderst du, um genau diese Vermutung zu prüfen — und nur diese?
```

**Das dritte Wort ist das schwerste: *nur diese*.**

> **Wer drei Dinge gleichzeitig ändert und danach feststellt, dass es läuft, hat den Fehler nicht gefunden, sondern begraben.**

Zwei der drei Änderungen sind jetzt unbegründet im Code. Sie tun etwas. Niemand weiß was, und beim nächsten Umbau steht jemand davor und traut sich nicht, sie anzufassen.

⚠️ **Und die härtere Hälfte derselben Regel:** *„Ich habe etwas geändert und jetzt geht es"* ist **kein Ergebnis.** Es heißt: Der Fehler ist weg, und du weißt nicht, warum — also weißt du auch nicht, ob er weg ist oder nur woandershin gewandert.

**Die Probe darauf ist billig und unbequem:** Mach deine Änderung rückgängig. Ist der Fehler wieder da? **Dann hast du ihn gefunden.** Ist er weg geblieben, hast du etwas anderes repariert und den eigentlichen noch vor dir.

### 5. Off-by-one ist eine Familie, keine Panne ⭐

Du hast in den letzten drei Etappen **drei Entscheidungen aufgeschrieben**, und alle drei sind vom selben Typ:

| Aus | Die Frage | Wenn sie falsch ist |
|---|---|---|
| **Etappe 13** | Was heißt `ABKLINGZEIT = 3` für Tick 1, 2, 3? | Alles ist einen Takt zu früh oder zu spät fertig |
| **Etappe 14a** | Welche Achse bei Gleichstand? | Gegner nehmen einen anderen Weg als erwartet |
| **Etappe 14b** | `<` oder `<=` bei der Reichweite? | Ein Feld zu früh oder zu spät geschossen |

**Der Punkt ist nicht, dass eine dieser Entscheidungen falsch wäre.** Der Punkt ist:

> **Ein Off-by-one ist nie ein Fehler im Code. Er ist ein Unterschied zwischen dem, was du aufgeschrieben hast, und dem, was du gebaut hast.**

**Und deshalb sind deine drei Notizen heute Beweismittel.** Ohne sie kannst du nur raten, was richtig gewesen wäre. Mit ihnen vergleichst du in zehn Minuten Notiz gegen Code.

⚠️ **Hast du eine der drei nicht aufgeschrieben, ist das heute die erste Aufgabe.** Nicht: nachträglich behaupten, was du gemeint hast. Sondern: **hinsehen, was der Code tut, es aufschreiben, und dann entscheiden, ob es so bleiben soll.**

### 6. Ursache und Symptom liegen jetzt weit auseinander 🧠

In Etappe 8 stand daneben, dass die Absturzstelle selten die Fehlerstelle ist. **Seit dem Tick ist der Abstand größer geworden**, und zwar in einer neuen Richtung — nicht in Zeilen, sondern in **Zeit**:

| Ursache | Symptom | Abstand |
|---|---|---|
| Zähler läuft in der falschen Phase | Fähigkeit ist einen Takt zu spät bereit | ein Tick |
| Ein Flag-Wort verweist ins Leere | Erkenntnis wirkt nie | **jede** Welle, ab immer |
| Einsammeln vor dem Aufräumen | Beute des letzten Gegners fehlt | einmal pro Welle |
| Geteilter Standardwert in `__init__` | Ein anderer Marine trägt dein Medkit | ab dem zweiten Objekt |

**Die zweite Zeile ist die unangenehmste**, weil es gar kein Symptom gibt — es passiert einfach nichts, was hätte passieren sollen. **Fehlende Wirkung ist schwerer zu bemerken als falsche Wirkung.**

> **Die Frage, die dabei hilft: „Wann hätte ich es gemerkt, wenn es funktioniert hätte?"** Wer darauf keine Antwort hat, hat eine Mechanik gebaut, die sich nicht beobachten lässt — und das ist ein eigener Fund.

### 7. Bisektion, diesmal über Etappen 🔨

Halbieren kennst du aus Etappe 8: Den Suchraum immer wieder in zwei Teile schneiden. **Heute wendest du es auf deine Git-Historie an**, und das ist der Grund, warum der Plan seit Tag eins Commits verlangt.

**Ein Fehler, von dem du nicht weißt, seit wann er da ist:**

```
Etappe 12  ← lief das hier noch?
Etappe 13
Etappe 14a ← hier prüfen
Etappe 14b
Etappe 15  ← hier ist er
```

Vier Commits, zwei Prüfungen, und du weißt, welche Etappe ihn eingebaut hat. **Das grenzt den Suchraum von „mein ganzes Programm" auf „ein Abend Arbeit" ein**, und mehr will man von einem Werkzeug nicht.

*(Git hat dafür sogar einen eigenen Befehl, der das Halbieren automatisch macht. Du brauchst ihn nicht — bei acht Commits geht es von Hand schneller, als die Bedienung nachzuschlagen.)*

### 8. Fehler in den Daten, zweite Sorte 🧠

Etappe 8 hatte einen Fehler in den Daten: falsche Werte in einer Tabelle. **Seit Etappe 15 gibt es eine zweite, gemeinere Sorte — einen Verweis ins Leere:**

```python
FUNDE = {"chitinprobe": {"erkenntnis": "schwachpunkt_kriecher"}}
SCHWACHPUNKTE = {"kriecher": "schwachpunkt_kricher"}      # ⚠️ ein Buchstabe
```

**Was passiert?** Das Set enthält `"schwachpunkt_kriecher"`. Gesucht wird `"schwachpunkt_kricher"`. **Kein Treffer, kein Fehler, keine Meldung** — die Erkenntnis wirkt einfach nie.

> **Beide Tabellen sind für sich betrachtet fehlerfrei. Falsch ist nur die Beziehung zwischen ihnen, und die prüft niemand.**

**Das ist die Kehrseite der Regel aus Etappe 15**: Eine Quelle definiert, andere verweisen — und ein Verweis ohne Ziel fällt nicht auf. *(In Etappe 21b meckert ein `Enum` darüber. Heute musst du selbst hinsehen.)*

---

## Dein Auftrag

**Heute baust du kein Feature.** Du schreibst eine Tabelle, arbeitest eine Liste ab und dokumentierst drei Funde.

⚠️ **Halt dich an die Reihenfolge.** Schritt 2 und 3 verlieren ihren Wert, wenn du vorher in deinem Code gestöbert hast.

---

### 1. Hol deine vier Notizen heraus

Aus `GELERNT.md`:

| Aus | Was dort stehen sollte |
|---|---|
| Etappe 12 | Die Tick-Reihenfolge, nummeriert |
| Etappe 13 | Was eine Zählerzahl exakt bedeutet · die Zählerphase |
| Etappe 14a | Eine Achse pro Tick · welche bei Gleichstand |
| Etappe 14b | `<` oder `<=` bei der Reichweite · die Einsammelphase aus 15 |

**Fehlt eine, ist das dein erster Fund.** Nach Konzept 5: hinsehen, was der Code tut, aufschreiben, dann entscheiden, ob es so bleiben soll — in dieser Reihenfolge.

---

### 2. ⭐⭐ Schreib die Tick-Tabelle — von Hand, vor dem Ausführen

**Das ist die Hauptübung dieser Etappe.** Plan eine ganze Sitzung dafür ein.

- Eine kleine Lage: **zwei Gegner, ein Kamerad, der Turm.** Feste Startwerte, die du dir selbst gibst.
- **Drei Ticks.**
- Eine Zeile pro Phase, aus **deiner** Notiz. Eine Spalte pro Einheit.
- Jede Zelle gefüllt, auch mit einem Strich.
- Auf Papier oder in einer Datei — **nicht im Kopf.**

⚠️ **Sieh dabei nicht in deinen Code.** Du schreibst auf, was passieren *soll*, nicht was passiert. Genau der Unterschied zwischen beidem ist heute die Beute.

---

### 3. ⭐ Lass dein Programm dasselbe tun und vergleich Zeile für Zeile

- Baue die Lage aus Schritt 2 in einer Wegwerf-Datei nach.
- Lass nach **jeder Phase** den Zustand aller Einheiten ausgeben — mit `### PHASE 3` davor, wie der Reflex aus Etappe 3.
- Drei Ticks.
- **Vergleich Zelle für Zelle, nicht Ergebnis gegen Ergebnis.**

**So prüfst du es:** Jeder Unterschied ist ein Fund. **Auch dann, wenn dein Programm recht hat** — dann war deine Vorstellung falsch, und das ist derselbe Fund von der anderen Seite.

**Schreib jeden Unterschied als Dreizeiler auf, bevor du irgendetwas änderst.**

---

### 4. ⭐ Vertausch zwei Phasen und spiel dieselbe Welle

- Zwei Zeilen im Tick tauschen — Trupp und Gegner.
- Dieselbe Welle, dieselben Startwerte.
- **Kernintegrität am Ende vergleichen.**

**So prüfst du es:** Die Zahl ist anders, und nichts ist abgestürzt. *(Konzept 1 zeigt den Fall vollständig — fünf Punkte auf einen einzigen Gegner.)*

**Dann tausch zurück.** Und schreib in `GELERNT.md`, **welche** Reihenfolge ab jetzt gilt und **warum** — ein Satz genügt, aber er muss dastehen.

---

### 5. ⭐⭐ Arbeite die Fahndungsliste ab

**Neun Etappen haben Kandidaten hinterlegt.** Geh sie einzeln durch, und schreib zu jedem Punkt eines von drei Wörtern: *geprüft* · *Fund* · *trifft nicht zu.*

| # | Kandidat | So prüfst du es |
|---|---|---|
| 1 | **Reichweite `<` gegen `<=`** | Gegner auf Abstand genau `reichweite` setzen. Wird er beschossen? Stimmt es mit deiner Notiz? |
| 2 | **Zählersemantik** | `ABKLINGZEIT = 3`, bei `zeit == 10` auslösen. Bei welchem `zeit` ist sie bereit? Stimmt es mit deiner Notiz? |
| 3 | **Gleichstand bei der Bewegung** | Gegner diagonal zum Ziel setzen, beide Abstände gleich. Welche Achse? Immer dieselbe? |
| 4 | **Zähler läuft doppelt** | Einen Zähler auf 10 setzen, **einen** Tick. Steht er auf 9 — oder auf 8? |
| 5 | **Sammeln und danach entfernen** | Vier Gegner auf `"tot"`, einmal aufräumen. Bleiben zwei übrig? |
| 6 | **Zwei Namen, ein Objekt** | `p welt.trupp[0].inventar is welt.trupp[1].inventar` — muss `False` sein |
| 7 | **Veränderbarer Standardwert** | Zwei Objekte erzeugen, dem einen etwas ins Inventar legen, beim **anderen** nachsehen |
| 8 | **Methode ohne Klammern** | Such nach `if ...am_leben:` ohne `()`. Ohne Klammern ist das **immer** wahr |
| 9 | **Verweis ins Leere** | Jedes Wort aus Schwachpunkt- und Depottabelle in der Fundtabelle nachschlagen |
| 10 | **Zwei Werte für dieselbe Aussage** | Gibt es `nachladen_noetig` **und** `munition > 0`? Können sie sich widersprechen? |
| 11 | **Namensfalle** | Zwei Gesundheitswerte — Kern und Marine. Werden sie irgendwo verwechselt? |
| 12 | **Komma-Falle** | `(5)` ist ein `int`, `(5,)` ein Tuple. Steht irgendwo eine Klammer ohne Komma? |
| 13 | **Raster geteilt** | `p welt.vorfeld[0] is welt.vorfeld[1]` — muss `False` sein |
| 14 | **Einsammeln zu früh** | Fehlt die Beute des **letzten** Gegners einer Welle? |

⚠️ **Nummer 7 und 8 sind die zwei, die am wahrscheinlichsten zuschlagen**, weil beide völlig harmlos aussehen. Bei 7 fällt nichts auf, solange du nur ein Objekt erzeugst. Bei 8 ist die Bedingung **immer** wahr — auch bei null Trefferpunkten.

**Du musst nicht alle vierzehn finden.** Du musst alle vierzehn **geprüft** haben.

---

### 6. Dokumentier drei Funde vollständig

Im Debugging-Protokoll aus Etappe 8, für **drei** deiner Funde:

- Der Dreizeiler: Beobachtung, Hypothese, Experiment.
- Was das Experiment ergeben hat — **auch wenn die Hypothese falsch war.**
- Die Rückwärtsprobe aus Konzept 4: Änderung rückgängig gemacht, Fehler wieder da?

⚠️ **Eine falsche Hypothese ist ein vollwertiger Eintrag.** Sie hat den Suchraum verkleinert, und das ist ihr Zweck. Ein Protokoll, in dem jede Hypothese stimmt, ist ein geschöntes Protokoll.

---

### 7. Übe die Bisektion an einem echten Fund

Nimm einen Fund, von dem du nicht weißt, seit wann er da ist.

- Ältere Commits auschecken, die Lage aus Schritt 2 nachstellen.
- **Halbieren**, nicht durchgehen.
- Die Etappe notieren, in der er entstanden ist.

*(Findest du keinen solchen Fehler, ist das ein gutes Zeichen. Dann bau einen: Ändere in einem Wegwerf-Zweig etwas Kleines, spiel zwei Etappen weiter, und such ihn. Die Übung ist der Zweck.)*

---

### 8. Bau einen Datenfehler und such ihn

Nach Konzept 8:

- Änder **einen Buchstaben** in einem Erkenntnis-Wort deiner Schwachpunkttabelle.
- Spiel eine Welle, analysiere, schieß.
- **Wie lange brauchst du, bis du es merkst — ohne in die Tabelle zu sehen?**

⚠️ **Die Antwort auf diese Frage ist wichtiger als der Fehler.** Wenn du es gar nicht merken kannst, fehlt deinem Spiel eine Anzeige — und das ist ein Fund.

---

### 9. Aufräumen und commit

Keine `print`-Zeilen aus Schritt 3, kein `breakpoint()`, keine Wegwerf-Dateien im Repo.

⚠️ **Und die Regel, die heute am leichtesten bricht:** Wenn du bei der Jagd etwas gefunden hast, das dir nicht gefällt, aber nicht kaputt ist — **lass es stehen.** Notier es. Heute wird repariert, was falsch ist, nicht was hässlich ist.

Commit: `Etappe 16: Bug-Jagd II — die Reihenfolge steht`

---

## Was NICHT in diese Etappe gehört

**Keine neuen Features.** Nicht eines. Wer heute nebenbei etwas einbaut, hat morgen einen Fehler, von dem er nicht weiß, ob er alt oder neu ist.

**Keine automatisierten Tests.** Die Versuchung ist heute am größten — jeder Fund schreit danach. Etappe 26, und dort ist es ein eigener Abend.

**Kein Umbau der Architektur.** Wenn dir beim Suchen auffällt, dass drei Tabellen zusammengehören: notieren. Etappe 22.

**Keine Reparatur der Kopplung.** Die Zeichnung aus Etappe 15 bleibt, wie sie ist. Etappe 23b.

**Kein `git bisect`.** Halbieren von Hand. Der Befehl ist nett und lenkt heute vom Verfahren ab.

**Kein `Enum` gegen die Verweise ins Leere.** Etappe 21b.

**Keine Optimierung.** Ein langsamer Tick ist kein Fehler.

---

## Selbsttest

- [ ] Alle vier Notizen aus Etappe 12–15 existieren — oder wurden heute nachgeholt.
- [ ] Die Tick-Tabelle wurde **vor** dem Ausführen geschrieben, drei Ticks, jede Zelle gefüllt.
- [ ] Programm und Tabelle wurden Zelle für Zelle verglichen, nicht Ergebnis gegen Ergebnis.
- [ ] Die vertauschte Reihenfolge ergibt ein **anderes** Ergebnis, und nichts stürzt ab.
- [ ] Die geltende Tick-Reihenfolge steht mit Begründung in `GELERNT.md`.
- [ ] **Alle vierzehn Punkte der Fahndungsliste sind mit einem der drei Wörter versehen.**
- [ ] Drei Funde stehen vollständig im Protokoll, mit Rückwärtsprobe.
- [ ] Mindestens ein Protokolleintrag enthält eine **falsche** Hypothese.
- [ ] Eine Bisektion wurde durchgeführt und die Etappe benannt.
- [ ] Der Datenfehler wurde gebaut, gefunden und wieder entfernt.
- [ ] Kein neues Feature im Commit.

---

## Lernziele

In `GELERNT.md`, ohne nachzuschlagen.

1. **Was ist ein Reihenfolgefehler — und warum ist er auf der Zeitachse immer ein Typ-3-Fehler?**
2. Warum findest du ihn nicht durch Lesen? Der Grund liegt nicht im Code.
3. Warum muss die Tick-Tabelle **vor** dem Ausführen entstehen?
4. Was bedeutet „nur eine Sache auf einmal ändern" — und was ist an *„ich habe etwas geändert und jetzt geht es"* falsch?
5. Wie machst du die Probe darauf, dass du wirklich **die** Ursache gefunden hast?
6. Warum ist eine falsche Hypothese ein brauchbares Ergebnis?
7. Welche drei Entscheidungen aus den Etappen 13 und 14 sind Off-by-one-Kandidaten?
8. Was ist ein Verweis ins Leere, und warum prüft ihn niemand?
9. Wie grenzt du mit Git ein, seit wann ein Fehler existiert?
10. **„Wann hätte ich es gemerkt, wenn es funktioniert hätte?" — nenn eine Stelle in deinem Spiel, bei der du darauf keine Antwort hast.**

**Frage 1 ist die wichtigste.** Sie ist die Fehlerklasse, die dich ab Etappe 17 begleitet.

**Frage 10 ist die unbequemste.** Sie findet Mechaniken, die nicht beobachtbar sind — und die kann man weder testen noch balancieren.

---

## Leseübung — Stufe 2 (15 Minuten)

**Heute liest du deinen eigenen Code.** Zum ersten Mal.

**Nimm deine `tick()`-Methode** und beantworte dieselben fünf Fragen, die du seit Etappe 12 an fremdem Code beantwortest:

1. Was kommt rein?
2. Was passiert?
3. Was verändert sich — und woran?
4. Was kommt raus?
5. Welche anderen Objekte oder Funktionen werden dabei aufgerufen?

**Und dann die drei, die heute zählen:**

6. **Schreib die Phasen in der Reihenfolge auf, in der sie im Code stehen.** Stimmt sie mit deiner Notiz aus Etappe 12 überein?
7. **Welche Phase darf man verschieben, ohne dass sich etwas ändert — und welche nicht?** Begründe für jede eine.
8. **Was ruft `tick()` alles auf, das du nicht sehen kannst, weil es in einer Unterklasse steht?** *(Das ist die Kehrseite von Etappe 11: Eine Schleife über Objekte ist lesbar und verbirgt, was tatsächlich läuft.)*

⚠️ **Frage 7 ist die eigentliche Übung.** Die meisten Phasen deines Ticks sind in ihrer Reihenfolge festgelegt, und zwar nicht durch Python, sondern durch Spielregeln, die du getroffen hast. **Wer nicht sagen kann, welche das sind, kann seinen Tick nicht gefahrlos umbauen.**

---

## Transferaufgabe (15 Minuten)

**Außerhalb des Spiels.** Eine Bankfiliale, kein Vorposten.

Ein Konto mit 100 Euro. Drei Vorgänge kommen an einem Tag an:

```
A: Zinsen gutschreiben (2 % auf den Stand)
B: Gebühr abbuchen (5 Euro)
C: Einzahlung (50 Euro)
```

1. **Rechne alle sechs möglichen Reihenfolgen von Hand aus.** Schreib sechs Endstände hin.
2. Wie viele verschiedene Ergebnisse gibt es?
3. Bau die drei Vorgänge als drei Funktionen und lass sie in allen sechs Reihenfolgen laufen. Vergleich mit deiner Rechnung.

**Und dann der eigentliche Teil:**

4. **Welche der sechs Reihenfolgen würdest du als Bank wählen? Welche als Kunde?**
5. Nimm die Zinsen heraus und rechne noch einmal. **Wie viele verschiedene Ergebnisse bleiben — und warum?**

**Schritt 5 ist der Kern.** Ohne die Zinsen ist die Reihenfolge egal, weil Addition vertauschbar ist. **Reihenfolge zählt genau dann, wenn ein Schritt vom Ergebnis eines anderen abhängt** — und in deinem Tick tut das fast jeder.

---

## Kaputtmachen

⚠️ **Heute ist das Kaputtmachen der Auftrag, nicht der Nachtisch.** Die Schritte 4, 7 und 8 sind Kaputtmach-Experimente. Diese drei kommen dazu.

**1. ⭐⭐ Zieh die Zählerphase ans Ende des Ticks.** Hinter das Aufräumen. Setz eine Abklingzeit auf `1` und beobachte, wann die Fähigkeit bereit ist. **Ein Takt Unterschied — und du hast ihn selbst herbeigeführt, also weißt du diesmal, wonach du suchst.** Genau das macht den Unterschied zu einem echten Fund aus.

**2. ⭐ Lass zwei Marines dasselbe Inventar teilen.** Setz `b.inventar = a.inventar` und spiel eine Welle. **Wann fällt es auf?** Schreib auf, nach wie vielen Aktionen — und ob es dir ohne Vorwissen aufgefallen wäre.

**3. Nimm die Klammern weg.** Änder ein `if einheit.am_leben():` zu `if einheit.am_leben:`. **Was passiert mit toten Einheiten?** *(Antwort: Sie leben. Die Methode selbst ist ein Objekt, und ein Objekt ist wahr.)*

---

**Diese drei sind bewusst Fehler, die du selbst einbaust.** Das ist der Unterschied zu Etappe 8: Dort hast du gelernt zu suchen. **Heute lernst du, wie ein Fehler aussieht, bevor du weißt, dass er da ist** — und dafür musst du ihn einmal bewusst erzeugt und dann gesucht haben.

Alles ins Fehlertagebuch: **woran du es erkannt hättest.**

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| Tabelle und Programm stimmen überein, das Spiel fühlt sich trotzdem falsch an | Die Lage war zu klein oder zu freundlich | Schritt 2 — nimm eine, in der ein Gegner das Tor erreicht |
| Nach dem Vergleich sind vier Dinge geändert und alles läuft | Mehrere Änderungen gleichzeitig | Konzept 4 — zurücknehmen, einzeln vorgehen |
| Der Fehler ist weg, kommt beim Zurücknehmen nicht wieder | Etwas anderes repariert, den eigentlichen noch offen | Konzept 4 — Rückwärtsprobe |
| Die Erkenntnis wirkt nie | Verweis ins Leere zwischen zwei Tabellen | Konzept 8, Fahndung 9 |
| Ein Zähler sinkt um zwei pro Tick | `zaehler_runter()` wird zweimal aufgerufen | Fahndung 4 — Tick **und** `update()`? |
| Alle Marines tragen dasselbe | Geteiltes Objekt oder veränderbarer Standardwert | Fahndung 6 und 7 — `is` prüfen |
| Eine tote Einheit handelt weiter | Methode ohne Klammern, oder `status`-Prüfung fehlt | Fahndung 8 |
| Die Beute des letzten Gegners fehlt | Einsammeln vor dem letzten Aufräumen | Fahndung 14 |
| Zwei Läufe mit denselben Startwerten gehen verschieden aus | Irgendwo steckt Zufall — **und der gehört ab Etappe 17 unter Kontrolle** | `random` aus Etappe 4 |
| Die Bisektion führt zu keinem klaren Ergebnis | Die Lage wurde zwischen den Commits nicht identisch nachgestellt | Schritt 7 — dieselben Startwerte |

**Der Debugging-Reflex dieser Etappe: „Schreib es auf, bevor du es ausführst."**

Etappe 12 fragte *in welchem Tick*, 13 *wie oft*, 14 *wo*, 15 *steht das Wort zweimal gleich da*. **Heute ist es keine Frage, sondern eine Reihenfolge:**

> **Erst die Vorhersage. Dann die Ausführung. Dann der Vergleich.**

Wer in der anderen Reihenfolge arbeitet, bekommt von seinem Programm immer recht.

---

## Ein Blick nach vorne

**Etappe 17a bringt Zufall ins Spiel** — und damit den ersten Fehlertyp, der sich nicht zuverlässig wiederholen lässt. **Deine Tick-Tabelle ist dann nur noch etwas wert, wenn der Zufall festgenagelt ist.**

**Etappe 17b nagelt ihn fest.** Ein Seed macht jeden Lauf reproduzierbar — und in Verbindung mit dem bedingten Breakpoint aus Etappe 8 ist das die schärfste Kombination, die dieser Plan kennt.

**Etappe 19 speichert die Welt** — und dann kommt der Fehler dazu, den du heute noch nicht haben kannst: Ein Spielstand, der beim Laden etwas anderes ergibt als beim Speichern. Deine Tick-Reihenfolge gehört dort zum Zustand.

**Etappe 21b balanciert**, und dort gilt die Regel von heute wörtlich: eine Zahl auf einmal, auf einem eigenen Branch.

**Etappe 26 schreibt Tests.** Dann wird aus dem Dreizeiler ein Ablauf: erst der Test, der den Fehler zeigt, dann der Fix. **Jeder heutige Fund ist ein Kandidat dafür** — schreib sie auf.

**Etappe 27 wendet alles von heute auf fremden Code an.** Dieselbe Geduld, dieselbe Tabelle, derselbe Dreizeiler — nur ohne die Erlaubnis, etwas zu ändern.

---

## Abschluss

**In `GELERNT.md`:**

- ⭐⭐ **Die geltende Tick-Reihenfolge**, nummeriert, mit einem Satz Begründung. **Das ist die wichtigste Zeile, die du in diesem Block schreibst.**
- ⭐ **Wie ich vorgegangen bin** — nimm einen Fund und beschreib das *Verfahren*, nicht den Fehler. Was hast du zuerst geprüft? Was hat den Suchraum am meisten verkleinert?
- Die Fahndungsliste mit ihren vierzehn Ergebnissen.
- Wie viele Funde waren Reihenfolge, wie viele etwas anderes?
- Die Antwort auf Lernziel 10: Welche Mechanik lässt sich nicht beobachten?
- Kandidaten für Etappe 26: Welche Funde sollten einen Test bekommen?
- Was hat mich überrascht? *(Kandidaten: dass die Tabelle etwas anderes sagte als der Code · dass ich einen Fehler nicht merken konnte · wie schnell die Bisektion war.)*

**Vor dem Commit:** Alle `print`-Zeilen raus? Kein neues Feature? Nichts repariert, was nur hässlich war?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest.

**Mach die Tick-Tabelle zu einer Funktion.** `welt.zustandszeile()` gibt eine Zeile aus, in der alle Einheiten mit Position und Trefferpunkten stehen. Ruf sie nach jeder Phase auf. **Dann ist die Tabelle aus Schritt 3 ein Knopfdruck**, und in Etappe 17b, wenn Zufall dazukommt, wirst du dankbar sein.

**Zähl, wie viele deiner vierzehn Kandidaten tatsächlich zutrafen.** Und dann die ehrlichere Frage: Wie viele davon hättest du ohne die Liste gefunden?

**Nimm den ältesten Commit, den du hast, und spiel eine Welle.** Fünf Minuten, und du siehst, wie weit du gekommen bist. **Das ist der Motivationsbeweis, für den die Commit-Historie seit Tag eins da ist.**

**Such in fremdem Projektcode nach `def update(` oder `def tick(`** und beantworte Frage 7 der Leseübung daran: Welche Reihenfolge ist dort festgelegt, und woran erkennt man es? **In den meisten Projekten steht es nirgends** — und das ist der Grund, warum deine Notiz etwas wert ist.

---

> **Nächste Etappe:** Etappe 17 — Der Wellengenerator · kontrollierte Unvorhersehbarkeit, und ein Seed, der sie wiederholbar macht
