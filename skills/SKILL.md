---
name: rpg-tutorial-etappe
description: Schreibt und erweitert Etappen-Guides für das selbsttragende Python-Tutorial „Vorposten" (30 Etappen; Register-Dateien BOGEN.md, SYNTAX.md, Vorposten_Lehrplan.md, MENTOR.md). Nutze diesen Skill immer, wenn jemand eine Etappe schreiben oder überarbeiten, Bogen, Syntaxregister oder Lehrplan pflegen, das Tutorial prüfen oder erweitern will — auch bei beiläufiger Erwähnung von „Etappe", „Lehrplan", „Bogen", „Syntaxregister" oder „das Tutorial". Ebenso bei Konsistenzprüfungen über mehrere Etappen, beim Zusammenführen fremder Entwürfe und bei jeder Änderung an einer Tutorial-Datei, weil dabei die Dateiversion nachzuziehen ist.
---

# Etappen-Guides schreiben

Ein Anfänger lernt Python, indem er über 30 Etappen ein textbasiertes Spiel baut — begleitet von einer KI, der verboten ist, ihm den Code zu schreiben.

**Das Spiel ist ein Hero-Survival, kein Tower Defense.** Diese Unterscheidung ist keine Geschmacksfrage, sondern die Prämisse, an der mehrere Etappen hängen:

- **Der Spieler steuert genau eine Figur.** Drei weitere Marines kämpfen ab Etappe 11 mit, entscheiden aber selbst. Daran hängt, warum Etappe 11 zwei Steuerungsquellen auf einer Basisklasse braucht.
- **Es gibt zwei Verlustbedingungen:** `kern_integritaet` (die Anlage) und `trefferpunkte` (die eigene Figur). Beide ab Etappe 1 angelegt, beide ab 3a wirksam.
- **Fortschritt läuft über Erfahrung und Stufen**, nicht nur über Währung. Der Faden beginnt in 3c als Zähler ohne Wirkung und zahlt erst in 18 Skillpunkte aus.
- **Es gibt genau einen Turm in der Basis, dafür mit Ausbaustufen.** Freies Bauen beliebig vieler Geschütze gehört nicht in dieses Spiel. Der Engineer-Turret ist eine *Fähigkeit* mit Abklingzeit, kein Gebäude, und höchstens einer gleichzeitig.
- **Ein ausbaubarer Stützpunkt ist bewusst zurückgestellt.** Die Entscheidung samt natürlichem Ort steht im Bogen.

Vorbild ist die Warcraft-3-Funmap *Marine Hero Survival*, Anleihen kommen aus DotA und LoL. **Vorschläge, die das Spiel Richtung Tower Defense schieben, werden abgelehnt** — auch wenn sie didaktisch bequem wären.

**Deine Rolle hier ist Unterrichtsmaterial verfassen, nicht mentorieren** (das steht in `MENTOR.md`). Du darfst Code zeigen — nur nie den, den der Lernende schreiben soll.

---

## 0. Die zwei Grundsätze, aus denen alles Übrige folgt

### Das Tutorial ist selbsttragend

**Es setzt keine zweite Lernquelle voraus.** Kein Boot.dev, kein Buch, kein Kurs, kein Vorwissen über Python. Wer Terminal, Editor und Dateisystem bedienen kann, muss allein durchkommen.

Daraus folgt hart: **Jedes Zeichen, jedes Schlüsselwort und jeder Aufruf, den ein Auftragsschritt braucht, muss vorher in einem Guide erklärt worden sein.** Nicht erwähnt — erklärt, mit Syntax und Beispiel. Ein Werkzeug in einer Tabellenzelle zu nennen (*„Werkzeug: `pop(i)` oder `del`"*) ist keine Erklärung. Ein Werkzeug beim Namen zu nennen und die Anwendung offenzulassen, ist keine Erklärung.

Die Kopfzeile jeder Etappe nennt deshalb **„Neue Syntax heute"**, nicht ein Kapitel einer fremden Plattform. Wenn dir in einem Bestandsguide noch eine `Boot.dev:`-Zeile begegnet, ersetz sie.

### Das Tutorial ist ein Produkt, keine Werkstatt

Der Leser ist ein Fremder. Ihn interessiert nicht, wie das Material entstanden ist.

**Nicht ins Tutorial gehören:** Fassungsnummern im Fließtext, Abschnitte wie „Was sich in Fassung 3 geändert hat", Vermerke wie „nachgezogen auf Fassung 3", „portiert aus dem Dorf-RPG-Lehrplan", „diese Zeile ist neu", „Zum Stand dieser Fassung", Hinweise auf verworfene Entwürfe, Anreden an bestimmte Personen, Verweise auf Chatverläufe oder auf das Modell, das etwas vorgeschlagen hat.

**Diese Passagen werden ersatzlos gestrichen, nicht umgezogen.** Es gibt keine Changelog-Datei und soll keine geben — das hier ist Unterrichtsmaterial, keine Softwareentwicklung. Wer wissen will, was sich wann geändert hat, liest `git log`. Das ist genau die Commit-Historie, die der Lernende ohnehin ab Etappe 0 als Motivationsbeweis führt.

**Die einzige zulässige Spur der Entstehung** ist der Versionskopf jeder Datei (Abschnitt 8). Eine Zeile, direkt unter der Überschrift, sonst nichts.

Wenn du eine Bestandsdatei aus einem anderen Grund anfasst und dabei Entwicklungsgeschichte im Text findest: raus damit, in denselben Arbeitsgang. Sie wächst sonst nach.

---

## 1. Pflichtlektüre vor dem Schreiben

**Vorausverweise und Werkzeugstände nie aus dem Gedächtnis rekonstruieren.** Plausibel Erfundenes ist schlimmer als Nachgeschlagenes.

Vor Etappe N:

1. **`BOGEN.md` Teil A** — was pflanzt N selbst?
2. **`BOGEN.md` quer** — welche Schulden zeigen auf N? `grep -n "\*\*N\*\*" BOGEN.md`
3. **`BOGEN.md` Teil B/C** — was setzt N voraus, welche Fäden laufen durch?
4. **`SYNTAX.md`** — welche Werkzeuge stehen dem Lernenden bei Etappe N zur Verfügung? Das ist die Liste, gegen die du in Abschnitt 3 prüfst.
5. **`Vorposten_Lehrplan.md`** — der Kurzabschnitt zu N.
6. **Die Guides N−1 und N−2** — wörtliche Versprechen: `grep -hn "Etappe N" etappen/etappe-*.md`

**Jede gefundene Schuld wird im Guide sichtbar eingelöst** — benannt, nicht nebenbei erfüllt.

---

## 2. Die drei Register

Das Tutorial führt drei Buchhaltungen. Sie überschneiden sich nicht.

| Datei | Führt Buch über | Frage, die sie beantwortet |
|---|---|---|
| `BOGEN.md` | Vorausverweise zwischen Etappen | *Was hat Etappe 2 versprochen, das Etappe 17 einlösen muss?* |
| `SYNTAX.md` | Werkzeuge und ihre Einführung | *Darf ich `pop()` in Etappe 6 benutzen — kennt der Lernende es?* |
| `Vorposten_Lehrplan.md` | Der Überblick über alle 30 Etappen | *Worum geht es in Etappe 14 überhaupt?* |

`SYNTAX.md` ist das jüngste der drei und existiert, weil ohne es systematisch Löcher entstehen. Aufbau:

```markdown
| Werkzeug | Eingeführt in | Erklärt in Konzept | Stufe |
|---|---|---|---|
| `=` Zuweisung            | 1  | 2  | 🔨 |
| `int()` / `str()`        | 1  | 8  | 🔨 |
| `==` `!=` `<` `>`        | 2  | 3  | 🔨 |
| `+=` `-=`                | 3a | 1b | 🔨 |
| `while True:`            | 3a | 6b | 🔨 |
| `liste[i]` lesend        | 4  | 3  | 🔨 |
| `liste[i] = wert`        | 4  | 3b | 🔨 |
| `%` Modulo               | 4  | 4b | 🧠 |
| `.pop(i)`                | 6  | 2b | 🔨 |
| Slicing `liste[a:b]`     | 4  | 8b | 👀 |
```

Eine Zeile pro Werkzeug, chronologisch nach Einführungsetappe. Die Stufenspalte trägt dieselbe Bedeutung wie in den Guides: 👀 heißt, der Lernende erkennt es nur — dann darf **kein Auftragsschritt** es verlangen.

---

## 3. Die Lösungsprobe — der Pflichtschritt gegen Werkzeuglücken

**Das ist der wichtigste Abschnitt dieses Skills.** Er verhindert die einzige Fehlerklasse, die einen Lernenden ohne Zweitquelle wirklich blockiert.

Der Fehler entsteht nicht dadurch, dass ein unbekanntes Werkzeug im Guide *steht*. Er entsteht dadurch, dass die **Lösung** eines Auftragsschritts ein Werkzeug braucht, das im Guide nirgends vorkommt — auch nicht als Lücke, weil niemand die Lösung aufgeschrieben hat.

### Das Verfahren

**Für jeden einzelnen Auftragsschritt, ohne Ausnahme:**

1. **Löse ihn selbst.** Schreib die Lösung tatsächlich hin, in einer Wegwerf-Datei, und lass sie laufen. Nicht im Kopf. Nicht „das ist offensichtlich".
2. **Inventarisier, was die Lösung braucht.** Jedes Zeichen, jeden Aufruf, jede Konstruktion. Auch das Kleine: `+=`, `%`, `//`, `[i] =`, `[-1]`, `["."] * n`, `while True:`, `.pop()`, `del`, `enumerate()`, f-String-Formatangaben.
3. **Prüf jeden Eintrag gegen `SYNTAX.md`.** Drei mögliche Ausgänge:
   - **Steht mit Etappe ≤ N drin** → in Ordnung, weiter.
   - **Steht nicht drin und gehört hierher** → Konzeptabschnitt schreiben, danach in `SYNTAX.md` eintragen.
   - **Gehört in eine spätere Etappe** → Auftragsschritt umbauen, bis er ohne auskommt. Nicht das Werkzeug vorziehen.
4. **Gibt es mehr als einen gangbaren Lösungsweg?** Dann muss **mindestens einer davon vollständig gedeckt** sein. Es reicht nicht, dass Weg A gedeckt wäre, wenn der Guide an anderer Stelle von Weg A abrät.

### Zusätzlich zu prüfende Fundstellen

Werkzeuge schleichen sich außerhalb von Codeblöcken ein. Diese vier Orte immer mitprüfen:

- **Die Stolpersteine-Tabelle.** Sie nennt Fehlerursachen — und damit Werkzeuge. Einen Fehler zu beschreiben, den der Lernende gar nicht verursachen kann, weil er das Zeichen nicht kennt, verwirrt nur.
- **Die Kaputtmach-Experimente.**
- **Der Selbsttest.**
- **Klammerbemerkungen und Tabellenzellen.** Genau dort ist historisch das meiste durchgerutscht.

### Zwei Regeln für Hinweise

**Ein Hinweis, der nur sagt, was nicht funktioniert, ist kein Hinweis.** Steht im Guide *„die Schleifenvariable zu ändern reicht nicht"*, dann muss an derselben oder einer verlinkten Stelle stehen, was stattdessen geht. Sonst bleibt der Lernende mit einer Verneinung und ohne Werkzeug zurück.

**Ein Guide darf ein Werkzeug suchen lassen oder es nennen, nicht beides.** *„Such die passende String-Methode"* und im selben Satz `help("".join)` — das ist keine Suche, das ist eine Inszenierung. Entscheide dich. Und wenn du suchen lässt: erklär vorher, wie man die Ausgabe des Suchwerkzeugs liest. `dir("")` liefert 81 Einträge, 34 davon Dunder-Methoden, und gibt in einem Skript ohne `print()` überhaupt nichts aus.

### Der Fehlerkatalog, gegen den geprüft wird

Diese sieben Lücken sind real aufgetreten. Sie sind der Grund für diesen Abschnitt und dienen als Musterfälle:

| Lücke | Wie sie entstand |
|---|---|
| `+=` / `-=` | Im ersten `while`-Beispiel benutzt, nie erklärt — zu klein für ein eigenes Konzept, zu neu zum Voraussetzen |
| `liste[i] = wert` | Nur lesender Indexzugriff gezeigt; der Auftrag verlangte schreibenden |
| `%` Modulo | In einem Kaputtmach-Beispiel benutzt |
| `//` | Nur in der Stolpersteine-Tabelle als Fehlerursache genannt |
| `.pop(i)` / `del` | In einer Tabellenzelle als „Werkzeug" benannt, Syntax nirgends |
| `while True:` | Vom Auftrag verlangt, die Bauform erst eine Portion später erklärt |
| Funktionsaufrufe (`backe(blech)`) | Als lesbarer Pseudocode in Beispielen, vier Etappen bevor Funktionen drankommen |

Die letzte Zeile ist eine eigene Regel wert: **Beispiele dürfen keine Konstruktion enthalten, die der Lernende noch nicht kennt — auch nicht als Kulisse.** Wenn ein Beispiel eine Handlung braucht, nimm `print()`.

---

## 4. Schema

**Kopfzeile:** Block, „Etappe N von 30", Navigation (← N−1 · Lehrplan · N+1 →), **Neue Syntax heute**, Zeitaufwand, Voraussetzung, Stufentabelle (🔨 Bauen · 🧠 Verstehen · 👀 Nur erkennen).

**Abschnitte:** `Worum es geht` · `Der lange Bogen`\* · `Eine Design-Entscheidung` · `Die Konzepte` · `Dein Auftrag` · `Was NICHT in diese Etappe gehört` · `Selbsttest` · `Lernziele` · `Transferaufgabe` · `Kaputtmachen` · `Häufige Stolpersteine` · `Ein Blick nach vorne` · `Abschluss` · `Wenn du mehr willst`

\* *Optional. Entfällt er, müssen die Schulden trotzdem im Text benannt werden.*

**„Neue Syntax heute" listet vollständig auf, was in `SYNTAX.md` mit dieser Etappe dazukommt.** Diese Zeile und das Register müssen identisch sein — sie ist die Zusage an den Lernenden, dass er nichts anderes braucht.

**Selbsttest prüft Programmzustand, nie Selbstbild.** Lernziele sind Fragen, eine als wichtigste markiert. Mindestens ein Kaputtmach-Experiment zeigt einen Typ-3-Fehler.

---

## 5. Codebeispiele

**Zeige nie den Code, den der Lernende schreiben soll.** Alle Beispiele in „Die Konzepte" laufen in fremdem Kontext — Kaffeetassen, Bäckerei, Gewürzregal, Parkbuchten.

Erlaubt: Strukturskizzen ohne Inhalt, Datenformate, Gegenbeispiele.

**Prüffrage: Könnte er das abtippen und hätte die Aufgabe erledigt? Dann umschreiben.** Das gilt auch für durchgerechnete Beispiele, die sich 1:1 übertragen lassen — dort einen Rechenschritt als Frage offenlassen.

**Und die Gegenprobe aus Abschnitt 3:** Enthält das Beispiel nur Werkzeuge, die laut `SYNTAX.md` schon eingeführt sind?

Diese zwei Regeln ziehen in verschiedene Richtungen. Die Auflösung ist immer dieselbe: **Wechsle die Domäne, nicht das Werkzeug.** Ein Beispiel mit einem Gewürzregal darf dieselbe Syntax benutzen wie die Lösung — es darf nur nicht dieselbe Aufgabe sein.

---

## 6. Auftragsschritte

- **Jeder Schritt beginnt mit einem Verb im Imperativ.** *„Bau die innere Schleife"*, nicht *„Die innere Schleife"*.
- **Anweisung vorn, Begründung hinten.** Bogen-Verweise in Klammern ans Ende. Mehr Zeilen Einordnung als Handlung = falsch aufgebaut.
- **Alle Werte nennen** — Startwerte, Obergrenzen, Variablennamen. Mehr als drei zusammengehörige: Tabelle.
- **Variablennamen sind durchgehend deutsch** (`trefferpunkte`, nicht `hp`; `kern_integritaet`, nicht `core_integrity`). Etappe 1 stellt diese Entscheidung ausdrücklich auf; ein einzelner englischer Name irgendwo im Plan macht sie unglaubwürdig. Prüf das bei jeder neuen Etappe mit — es rutscht leicht durch, weil englische Fachbegriffe schneller zur Hand sind.
- **Testanweisung**, wo das Ergebnis nicht sofort sichtbar ist.
- **Wegwerfcode erlauben**, wenn etwas erst später richtig gebaut wird.
- **Durchlaufende Nummerierung** über alle Portionen.
- Mindestens ein Schritt prüft, dass Bestehendes noch funktioniert.
- **Kein Schritt verlangt ein Werkzeug der Stufe 👀.**
- **Jeder Schritt hat die Lösungsprobe aus Abschnitt 3 bestanden.**

---

## 7. Zeitangaben ehrlich rechnen

Zu niedrige Schätzungen sind respektlos und werden zuverlässig bemerkt.

**Die Lesezeit zählt mit.** Sie ist bei diesen Guides kein Randposten: Bei dichtem deutschem Fachtext rechnest du mit **180 Wörtern pro Minute**. Ein Guide mit 9.000 Wörtern kostet 50 Minuten, bevor eine Zeile getippt ist — also ein bis zwei komplette Sitzungen.

```bash
wc -w etappen/etappe-NN-*.md     # geteilt durch 180 = Lesezeit in Minuten
```

**Rechne die Angabe zusammen aus:** Lesezeit + Auftragsschritte + Transferaufgabe + Kaputtmachen + Selbsttest. Wenn der Guide im Fließtext schreibt *„eine Stunde nur für Schritt 2 ist normal"*, muss diese Stunde in der Kopfzeile enthalten sein. Widersprüche zwischen Kopfzeile und Fließtext sind ein häufiger und peinlicher Fehler.

**Ab etwa 45 Minuten reiner Lesezeit gehört die Etappe geteilt**, nicht optimistischer geschätzt.

---

## 8. Versionierung — jede Datei, ausnahmslos

**Jede Datei des Tutorials trägt einen Versionskopf.** Ohne Ausnahme: Guides, `BOGEN.md`, `SYNTAX.md`, `Vorposten_Lehrplan.md`, `MENTOR.md`, `README.md`, jede weitere, die dazukommt.

Format: kursiv, direkt unter der Überschrift, Version und Datum:

```markdown
# Etappe 4 — Ausrüstung und Beute

*v1.2.0 · 2026-09-02*
```

Bei Dateien ohne Überschrift steht dieselbe Zeile ganz oben als HTML-Kommentar.

**Die Ziffern bedeuten:**

| Stelle | Wird erhöht bei |
|---|---|
| **MAJOR** | Struktur ändert sich — Etappen umnummeriert, Prämisse geändert, Register umgebaut |
| **MINOR** | Inhalt kommt dazu — neuer Konzeptabschnitt, neuer Auftragsschritt, neue Registerzeile |
| **PATCH** | Korrektur ohne neuen Inhalt — Tippfehler, toter Link, Statusspalte, Zeitangabe geeicht |

Jede Datei zählt für sich; die Nummern laufen unabhängig voneinander. Eine neu angelegte Datei startet bei `v1.0.0`.

**Bei jeder Änderung, ausnahmslos, zwei Handgriffe:**

1. Version im Kopf **jeder** geänderten Datei erhöhen — auch wenn nur eine Statusspalte im Bogen gekippt wurde. Eine Änderung ohne Versionssprung ist eine unsichtbare Änderung.
2. Ein Commit, dessen Nachricht die Etappe oder Datei nennt. Die Commit-Nachricht trägt das Warum, das sonst in einem Changelog stünde: `Etappe 4 v1.2.0: schreibender Indexzugriff ergänzt (war in Auftrag 9.2 nötig, aber nirgends erklärt)`.

**Eine Changelog-Datei gibt es nicht.** Wer die Geschichte braucht, liest `git log`. Sich zwei Buchführungen über dieselbe Sache zu leisten, führt zuverlässig dazu, dass eine davon falsch wird.

---

## 9. Nach dem Schreiben — drei Register, keines davon optional

**Der Lehrplan wird regelmäßig vergessen. Das Syntaxregister ist neu und wird deshalb erst recht vergessen.**

**`SYNTAX.md`:** Jedes in dieser Etappe neu eingeführte Werkzeug eintragen, mit Etappe, Konzeptnummer und Stufe. Muss mit der Kopfzeile „Neue Syntax heute" übereinstimmen.

**`BOGEN.md`:** Teil A ergänzen, Teil B bei neuen Voraussetzungen, Teil C bei betroffenen Fäden. Eingelöste Schulden auf `**eingelöst** ✓`. Migrationen (welcher Wert lebt ab wann wo) in die Migrationstabelle.

**`Vorposten_Lehrplan.md`:** fehlende Themen ergänzen, Widersprüche zum Guide beheben, kein fertiger Spielcode, keine Aufgabe mit Werkzeug aus späterer Etappe, Zeitrahmen eichen.

**Danach: Versionen.** Jede in diesem Arbeitsgang berührte Datei bekommt ihren Versionssprung nach Abschnitt 8 — typischerweise vier auf einmal, wenn eine neue Etappe entsteht.

```bash
grep -n "Etappe [0-9]" etappen/etappe-NN-*.md   # jeder Verweis muss im Bogen stehen
```

*(Ausgenommen: Verweise aus „Was NICHT" und der Navigation — das sind Abgrenzungen, keine Schulden.)*

**Tote Links prüfen.** Guides verlinken gern auf Etappen, die es noch nicht gibt. Entweder die Datei anlegen oder den Link zu reinem Text machen:

```bash
grep -rhoP '\]\(\.{0,2}[^)#]*\.md' --include="*.md" . | sed 's/](//' | sort -u
```

---

## 10. Das Repo für Fremde

Diese Punkte gelten unabhängig von einzelnen Etappen und werden bei jeder größeren Änderung mitgeprüft:

- **`README.md` im Wurzelverzeichnis.** Was das ist, für wen, wie man anfängt, welche Dateien man der KI gibt. Ohne das findet niemand den Einstieg. Es beschreibt das aktuelle Tutorial — nicht ein Vorgängerprojekt.
- **Keine Verweise auf verworfene Vorgängerfassungen** in Text oder Verlinkung. Altbestand gehört in ein deutlich benanntes Archivverzeichnis oder aus dem Repo.
- **Keine Datei behauptet, eine Zweitquelle sei nötig.** Das gilt auch für `MENTOR.md` und `README.md`.
- **Alle Kopiervorlagen für die KI sind vollständig aufgeführt:** `MENTOR.md`, `Vorposten_Lehrplan.md`, `BOGEN.md`, `SYNTAX.md`.
- **Jede Datei trägt einen Versionskopf.** Fehlt einer, nachrüsten — auch bei Dateien, die du sonst nicht anfasst.

---

## 10b. Wo eine neue Sitzung nachsieht

**Diese Datei hält keinen Fortschrittsstand fest — der würde beim nächsten Guide sofort veralten und dieselbe Art Lüge produzieren, die eine ungepflegte `SYNTAX.md` schon einmal war.**

Für *„was ist schon geschrieben"* und *„was kommt als Nächstes"*: `BOGEN.md` und `Vorposten_Lehrplan.md` nachsehen — Status-Spalte im Bogen, vorhandene Etappen-Dateien im Verzeichnis. Für *„welches Werkzeug kennt der Lernende schon"*: `SYNTAX.md`, Abschnitt *Offene Lücken*. Diese drei sind die Quelle der Wahrheit; eine Kopie ihres Inhalts hier wäre die zweite Buchführung, die Abschnitt 8 ausdrücklich verbietet.

**Drei Entscheidungen bleiben hier vermerkt, weil sie sich nicht aus dem Fortschritt ablesen lassen und leicht vergessen werden:**

- **Etappe 4 liegt über der Teilungsgrenze aus Abschnitt 7.** Ein Schnitt nach Auftragsschritt 6 ist im Guide markiert, aber nicht vollzogen.
- **Es gibt kein Root-`README.md`.** Wer das Repo findet, hat keinen Einstieg.
- **Ein ausbaubarer Stützpunkt ist zurückgestellt**, nicht vergessen. Begründung und natürlicher Ort stehen im Bogen bei Etappe 22.

---

## 11. Kurzcheck

- [ ] Alle Schulden aus dem Bogen eingelöst **und benannt**
- [ ] Versprechen aus N−1 und N−2 erfüllt
- [ ] **Jeder Auftragsschritt selbst gelöst und ausgeführt; alle benötigten Werkzeuge gegen `SYNTAX.md` geprüft**
- [ ] **Kein Beispiel und keine Tabelle nennt ein Werkzeug, das der Lernende noch nicht kennt**
- [ ] **Jeder „so geht es nicht"-Hinweis hat ein gedecktes „so geht es"**
- [ ] Kein Auftragsschritt verlangt ein 👀-Werkzeug
- [ ] Kein Codebeispiel zeigt die Aufgabe des Lernenden
- [ ] Jeder Auftragsschritt: Imperativ, Anweisung vor Begründung, alle Werte genannt
- [ ] Selbsttest prüft Zustand; ein Kaputtmachen zeigt Typ 3
- [ ] **Zeitangabe enthält die Lesezeit und widerspricht dem Fließtext nicht**
- [ ] **Kopfzeile „Neue Syntax heute" ist vollständig und deckt sich mit `SYNTAX.md`**
- [ ] **Keine Entwicklungsgeschichte im Text — Fassungsvermerke, „neu in dieser Version", Herkunftshinweise sind raus**
- [ ] **Variablennamen durchgehend deutsch**
- [ ] **Nichts schiebt das Spiel Richtung Tower Defense** — ein Held, ein Basisturm, zwei Verlustbedingungen
- [ ] **Geschlossene Lücken sind aus „Offene Lücken" in `SYNTAX.md` verschwunden**
- [ ] `SYNTAX.md`, `BOGEN.md`, `Vorposten_Lehrplan.md` nachgezogen
- [ ] **Version in jeder berührten Datei erhöht, committet mit sprechender Nachricht**
- [ ] „Etappe N von 30", Navigation und alle Links stimmen

---

## Fremde Entwürfe und fremde Vorschlagslisten

Kurzes Urteil zuerst. Schulden prüfen — fremde Entwürfe übersehen sie, weil sie den Bogen nicht kennen. **Lösungsprobe ebenfalls durchführen** — sie setzen typischerweise Werkzeuge voraus, die es im Register noch nicht gibt, weil sie von einem allgemein gebildeten Python-Leser ausgehen statt vom Stand dieser Etappe. **Formatierung nie übernehmen.** Ablehnungen begründen. Register nachziehen.

### Die Prüffrage, die zählt

**Nicht:** *„Trägt dieser Vorschlag etwas bei?"* — das bejahen fast alle, und deshalb ist die Frage wertlos.

**Sondern, in dieser Reihenfolge:**

1. **Steht das schon im Guide?** Der häufigste Fund. Ein Vorschlag beschreibt eine Regel, die zwei Bildschirme weiter oben bereits steht, nur anders formuliert. Dann ist die richtige Antwort, die vorhandene Stelle zu schärfen — nicht, eine zweite danebenzustellen.
2. **Kollidiert es mit einer Schuld im Bogen?** Besonders bei Kürzungsvorschlägen: Ein Abschnitt, der überladen wirkt, trägt oft drei Vorausverweise, die anderswo eingelöst werden.
3. **Was kostet es?** Jede Ergänzung ist Lesezeit, und Lesezeit ist bei diesen Guides der knappste Posten.
4. **Braucht die Ergänzung einen Abgrenzungshinweis?** Wenn du dabei bist zu schreiben *„verwechsle das nicht mit dem Abschnitt weiter oben"*, ist die Ergänzung fast immer die falsche. Zwei ähnliche Rituale sind schlechter als eines.

### Die Menge ist selbst ein Warnsignal

Kommt eine Liste mit zwölf oder sechzehn Vorschlägen, ist die Trefferquote erfahrungsgemäß **unter der Hälfte** — auch wenn die Liste selbst mit *„ich würde nicht mehr Stoff hinzufügen"* beginnt. Einzeln geprüft bestehen fast alle; in Summe wächst der Guide um ein Viertel.

**Deshalb: erst alle Vorschläge sichten, dann sortieren, dann übernehmen.** Nicht der Reihe nach abarbeiten. Und wenn eine Etappe schon an der Teilungsgrenze steht, muss für jede Aufnahme etwas anderes weichen.

**Beim Bericht ehrlich zählen.** „Fünfzehn von sechzehn übernommen" ist keine Qualitätsaussage, wenn vier davon Wiederholungen waren und einer ein Lob für bestehenden Text. Sag, was gut war, was marginal, was abgelehnt — und warum.
