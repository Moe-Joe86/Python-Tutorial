---
name: rpg-tutorial-etappe
description: Schreibt und erweitert Etappen-Guides für das Python-RPG-Tutorial (Dorfspiel, 30 Etappen, BOGEN.md/RPG_Lehrplan.md/MENTOR.md). Nutze diesen Skill immer, wenn jemand eine neue Etappe schreiben, eine bestehende überarbeiten, den Bogen pflegen oder das Tutorial erweitern will — auch wenn nur beiläufig von "Etappe", "Lehrplan", "Bogen", "Dorfspiel" oder "das Tutorial" die Rede ist. Ebenso bei Konsistenzprüfungen über mehrere Etappen und beim Zusammenführen von Entwürfen aus anderen Modellen.
---

# Etappen-Guides für das RPG-Tutorial schreiben

Dieser Skill beschreibt, wie man dem Python-Tutorial „Dorf-RPG" eine Etappe hinzufügt, ohne seine Struktur zu beschädigen.

**Das Tutorial in einem Satz:** Ein Anfänger lernt Python, indem er über 30 Etappen ein textbasiertes Rollenspiel baut — begleitet von einer KI, der ausdrücklich verboten ist, ihm den Code zu schreiben.

**Deine Rolle hier ist eine andere als die in `MENTOR.md`.** Dort geht es darum, einen Lernenden zu begleiten. Hier geht es darum, Unterrichtsmaterial zu verfassen. Verwechsle die beiden nicht: Beim Schreiben eines Guides darfst und musst du Code zeigen — nur eben nie den Code, den der Lernende selbst schreiben soll.

---

## Zuerst: den Bogen lesen

**Ohne diesen Schritt darfst du nicht anfangen.**

`BOGEN.md` ist das Register aller Vorausverweise zwischen Etappen. Frühe Etappen legen Dinge an, die späte einlösen — eine Variable aus Etappe 1 wird in Etappe 17 gebraucht, eine Datenstruktur aus Etappe 6 zahlt in Etappe 14 und 18. Diese Verweise sind der Grund, warum sich das Tutorial wie ein Bogen anfühlt und nicht wie dreißig Übungsaufgaben.

**Rekonstruiere sie niemals aus dem Gedächtnis.** Über dreißig Etappen ist plausibel Erfundenes schlimmer als Nachgeschlagenes.

Vor dem Schreiben von Etappe N:

1. **`BOGEN.md`, Teil A** — was pflanzt Etappe N selbst? (Der Abschnitt kann fehlen; dann legst du ihn später an.)
2. **`BOGEN.md`, Teil A quer** — welche früheren Etappen zeigen mit `**N**` auf diese Etappe? Das sind die Schulden, die du einlösen musst.
3. **`BOGEN.md`, Teil B** — was erwartet Etappe N laut Register aus früheren Etappen?
4. **`RPG_Lehrplan.md`** — der Kurzabschnitt zu Etappe N: Boot.dev-Thema, was gebaut wird, Lernziele, Transferaufgabe, Kaputtmachen.
5. **Die Guides N−1 und N−2** — was wurde dort wörtlich für diese Etappe versprochen? Suche nach „Etappe N".

Praktisch:

```bash
grep -n "\*\*N\*\*" BOGEN.md                  # Schulden an Etappe N
grep -hn "Etappe N" de/etappe-*.md            # wörtliche Versprechen
```

**Jede gefundene Schuld muss im Guide sichtbar eingelöst werden** — nicht nebenbei erfüllt, sondern benannt: *„Die Schuld aus Etappe 2 wird heute eingelöst."* Der Lernende soll den Bogen bemerken.

---

## Das Schema

Jeder Guide hat dieselben Abschnitte in dieser Reihenfolge. Abweichungen brauchen einen Grund.

```markdown
# Etappe N — Titel

> **Block X: Name** · Etappe N von 30 · [← Etappe N-1](...) · [Lehrplan](../RPG_Lehrplan.md) · [Etappe N+1 →](...)

**Boot.dev:** Themen
**Zeitaufwand:** X–Y Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe N-1 abgeschlossen, Selbsttest grün

## Worum es geht
## Der lange Bogen
## Eine Design-Entscheidung, die du jetzt treffen solltest
## Die Konzepte
## Dein Auftrag
## Was NICHT in diese Etappe gehört
## Selbsttest
## Lernziele
## Transferaufgabe (X Minuten)
## Kaputtmachen
## Häufige Stolpersteine
## Ein Blick nach vorne
## Abschluss
## Wenn du mehr willst

> **Nächste Etappe:** [...] · Themen
```

### Was in jeden Abschnitt gehört

**Worum es geht** — Warum diese Etappe existiert, nicht was sie behandelt. Der beste Einstieg benennt ein Problem, das der Lernende gerade *hat*. Bei Etappen ohne neues Feature (Refactoring, Datenstrukturen) ist das besonders wichtig: Mach die Leere zum Thema, statt sie zu kaschieren.

**Der lange Bogen** — Eine Tabelle: was heute gebaut wird, wo es wieder auftaucht. Darunter ein Absatz zu den Schulden, die eingelöst werden, mit Nennung der Quell-Etappe. Diese Tabelle muss zum Bogen-Eintrag passen.

**Eine Design-Entscheidung** — Eine oder zwei Fragen, die der Lernende bewusst beantworten muss und die **später Folgen haben**. Keine Geschmacksfragen. Gute Beispiele aus dem Bestand: gesperrter Weg — Ausgang fehlt oder ist markiert (bestimmt Etappe 13); `return` statt `print` in der Logik (bestimmt, ob Etappe 28 funktioniert). Die Entscheidung gehört in `GELERNT.md`.

**Die Konzepte** — Nummerierte `###`-Abschnitte, meist 8 bis 14. Hier wird gelehrt. Regeln dazu siehe unten.

**Dein Auftrag** — Nummerierte Schritte, nach jedem ausführen. Beschreibt, *was* entstehen soll, nie *wie es aussieht*. Mindestens ein Schritt sollte prüfen, dass Bestehendes noch funktioniert.

**Was NICHT in diese Etappe gehört** — Liste mit ❌ und Verweis auf die zuständige Etappe. Danach ein Absatz zum verlockendsten Punkt: Warum das Gefühl richtig ist und trotzdem warten muss. Dieser Abschnitt verhindert, dass spätere Höhepunkte verbrannt werden.

**Selbsttest** — Checkboxen, die den **Programmzustand** prüfen, nicht das Selbstbild. *„`nimm brot` ein zweites Mal meldet, dass hier nichts mehr liegt"* ist prüfbar; *„Ich kann `append()` erklären"* ist es nicht — das gehört zu den Lernzielen.

**Lernziele** — 8 bis 10 Fragen, ohne Nachschlagen in eigenen Worten zu beantworten. Eine davon als wichtigste markieren, mit Begründung. Der Mentor fragt sie ab.

**Transferaufgabe** — 5 bis 15 Minuten, ausdrücklich **außerhalb** des Spiels, in einer Wegwerf-Datei. Wer eine Liste nur im eigenen Inventar bedienen kann, kann keine Listen. Ab Etappe 9 kann stattdessen eine **Leseübung** stehen — fremder Code, den der Lernende erklärt, ohne zu tippen.

**Kaputtmachen** — Nummerierte Experimente, absichtlich zerstören und beobachten. Mindestens eines sollte einen Fehler vom Typ 3 zeigen (läuft durch, liefert das Falsche). Wo möglich: erst aufschreiben, was man erwartet, dann ausführen.

**Häufige Stolpersteine** — Tabelle: Symptom, Ursache, wo man sucht. Echte Fehlermeldungen wörtlich. Danach der **Debugging-Reflex** dieser Etappe — die eine Frage, die hier am schnellsten zum Ziel führt.

**Ein Blick nach vorne** — Wo das Gebaute wieder auftaucht, mit Etappennummern. Der Ort für den großen Zusammenhang.

**Abschluss** — `GELERNT.md`-Einträge (immer inklusive der Design-Entscheidung) und der Commit-Befehl mit passender Message.

**Wenn du mehr willst** — Optionale Erweiterungen, erst bei grünem Selbsttest. Die beste steht zuletzt und ist meist die, die erzählerisch am meisten bringt.

---

## Regeln für Codebeispiele

**Die wichtigste Regel:** Zeige nie den Code, den der Lernende schreiben soll.

Konkret heißt das: Alle Beispiele in **Die Konzepte** laufen in einem **fremden Kontext** — Kaffeetassen, Einkaufslisten, Dorfbewohner-Alter, Türsteher. Nie am Inventar, nie an der Ortstabelle, nie an der Game-Loop.

```python
# richtig — Syntax an fremdem Beispiel
tassen = 3
while tassen > 0:
    print(f"Noch {tassen} Tassen.")
    tassen -= 1

# falsch — das ist seine Aufgabe
while laeuft:
    befehl = input("> ").lower().strip()
    if befehl == "beenden":
        laeuft = False
```

**Erlaubte Ausnahmen:**
- **Strukturskizzen ohne Inhalt** — `class World:` mit `def tick(self):` und einer Schleife darin, wenn die Struktur selbst der Lehrinhalt ist.
- **Datenformate** — die Form eines Ortsdictionaries zu zeigen ist nötig, weil die Verschachtelung der Lehrinhalt ist.
- **Gegenbeispiele** — Code, den er *nicht* schreiben soll, etwa die `elif`-Kette, die durch ein Dictionary abgelöst wird.

Wenn du unsicher bist: Könnte der Lernende das abtippen und hätte damit die Aufgabe erledigt? Dann umschreiben.

---

## Qualitätsmaßstäbe

**Jede Etappe braucht ein „warum das zählt".** Nicht „Listen sind wichtig", sondern was der Lernende danach kann, was vorher nicht ging — und wo es später zahlt.

**Sei ehrlich, wenn etwas dünn ist.** Etappe 1 ist als Programmierübung mager; der Guide sagt das und erklärt, worin der eigentliche Wert liegt. Ein Guide, der jede Etappe für gleich bedeutend erklärt, ist unglaubwürdig.

**Benenne Einschränkungen.** Wenn eine Lösung nur bis Etappe 20 trägt, schreib das hin: *„Ehrlich eingeordnet: gut genug für heute, nicht endgültig."* Das erspart dem Lernenden das Gefühl, etwas Falsches gelernt zu haben.

**Markiere die wichtigen Etappen mit ⭐** — sparsam. Zwei Sterne nur für die tragenden (der Tick, die Bug-Jagd, das Lesen fremden Codes).

**Schreib dicht.** Kurze Absätze, aber nicht ein Satz pro Absatz. Der Guide wird beim Programmieren nebenher gelesen; Luftigkeit macht ihn länger, nicht verständlicher.

**Kein Wissen aus einem Chatverlauf voraussetzen.** Das Tutorial ist ein eigenständiges Produkt. Ein Fremder lädt es herunter und gibt es irgendeiner KI. „Ich" im Text meint immer die begleitende KI, nie eine bestimmte Person oder Sitzung.

---

## Nach dem Schreiben: den Bogen pflegen

**Ohne diesen Schritt ist die Etappe nicht fertig.**

Beim Ausformulieren entstehen fast immer neue Vorausverweise, die vorher niemand geplant hatte. Sie gehen verloren, wenn sie nicht sofort eingetragen werden.

1. **Teil A** — Abschnitt für Etappe N anlegen oder ergänzen. Jede Zeile: was angelegt wird, wo es eingelöst wird (mit `**Nummer**`), Status.
2. **Teil B** — wenn Etappe N für spätere Etappen zur Voraussetzung wird, dort eine Zeile ergänzen.
3. **Teil C** — wenn ein durchgehender Faden betroffen ist (Bug-Jagd, Fehlertypen, Git, Schreiben→Lesen), dort nachziehen.
4. **Status setzen** — Schulden, die dieser Guide einlöst, von `offen` auf `**eingelöst** ✓`. Der Status beschreibt den Zustand des *Tutorials*, nicht den des Lernercodes.

Zur Kontrolle:

```bash
grep -n "Etappe [0-9]" de/etappe-NN-*.md    # alle Verweise des neuen Guides
```

Jeder Verweis auf eine spätere Etappe muss im Bogen stehen — außer er stammt aus der „Was NICHT"-Liste oder der Navigation. Das sind Abgrenzungen, keine Schulden.

**Und den Lehrplan prüfen:** Wenn der Guide Themen behandelt, die im Kurzabschnitt fehlen, ergänze sie dort knapp. Der Lehrplan bleibt die Landkarte — er beschreibt, er lehrt nicht.

---

## Entwürfe anderer Modelle zusammenführen

Ein häufiger Ablauf: Es liegt bereits ein Entwurf derselben Etappe von einem anderen Modell vor, und die guten Teile sollen übernommen werden.

**So geht das:**

1. **Kurzes Urteil zuerst** — wo ist der fremde Entwurf besser, wo schwächer. Zwei, drei Sätze, keine Diplomatie.
2. **Schulden prüfen** — fremde Entwürfe übersehen sie regelmäßig, weil sie den Bogen nicht kennen. Das ist meist der größte Unterschied.
3. **Übernehmen, was besser ist.** Typischerweise gute Erklärbilder, Experimente, die etwas erfahrbar statt erklärbar machen, und zugespitzte Formulierungen.
4. **Formatierung nie übernehmen.** Das Schema oben gilt. Insbesondere: keine Selbsttests im „Ich kann…"-Format, keine fünfzehn Lernziele, keine doppelten Aufgabenblöcke.
5. **Ablehnungen begründen.** Wenn ein Vorschlag einen späteren Höhepunkt verbrennt oder ein Werkzeug vorwegnimmt, sag warum.
6. **Bogen nachziehen**, wenn die Übernahmen neue Verweise erzeugt haben.

---

## Was das Tutorial kaputtmachen würde

- **Ein Werkzeug vorwegnehmen, das eine spätere Etappe braucht.** Crafting gehört zu Etappe 22, `random` zu 17, der Tagesablauf zu 12. Wer sie früher einbaut, nimmt der zuständigen Etappe ihren Sinn.
- **Fertigen Spielcode zeigen.** Auch in Lehrplan und Bogen, nicht nur im Guide — die Dateien werden der begleitenden KI übergeben.
- **Den Bogen nicht pflegen.** Ein Register, das nicht gepflegt wird, ist nach drei Monaten Fiktion.
- **Die Prämisse ändern.** Das leere Dorf, die drei Verbliebenen, die Mine und die Wiese sind gesetzt. Namen, Texte und Atmosphäre gehören dem Lernenden; die Struktur nicht.
- **Etappen aufblähen.** Bei 20–30 Minuten am Tag ist die größte Gefahr nicht zu wenig Übung, sondern dass der Plan zur Bürokratie wird und der Lernende aufhört.

---

## Kurzcheck vor dem Abgeben

- [ ] Alle Schulden aus dem Bogen sind eingelöst und benannt
- [ ] Alle Versprechen aus den Guides N−1 und N−2 sind erfüllt
- [ ] Kein Codebeispiel zeigt Code, den der Lernende schreiben soll
- [ ] Alle vierzehn Abschnitte sind vorhanden, in der richtigen Reihenfolge
- [ ] Die Navigationszeile stimmt, „von 30" ist korrekt
- [ ] Der Selbsttest prüft Programmzustand, nicht Selbstbild
- [ ] Mindestens ein Kaputtmach-Experiment zeigt einen Typ-3-Fehler
- [ ] Der Bogen ist um die neuen Verweise ergänzt
- [ ] Eingelöste Schulden stehen auf `**eingelöst** ✓`
- [ ] Der Lehrplan-Abschnitt passt zum Guide
