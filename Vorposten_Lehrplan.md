# Projekt-Lehrplan: Vorposten

**Begleitend zu Boot.dev — Python lernen, indem die Verteidigung wächst**
*Fassung 3 — 30 Etappen in 38 Portionen. Portiert aus dem Dorf-RPG-Lehrplan (Fassung 5); alle Python-Themen sind 1:1 erhalten.*

---

## Bevor du weiterliest

Diese Datei ist lang. **Du musst sie nicht lesen.** Sie ist eine Landkarte, kein Lehrbuch — man schlägt darin nach, man arbeitet sie nicht durch.

**Für heute reichen drei Abschnitte:** [Die Prämisse](#die-prämisse), [Das Ritual](#das-ritual-vorhersagen--ausführen--vergleichen--erklären) und [Etappe 0](#etappe-0--das-repo). Das sind vier Seiten. Alles andere liest du in dem Moment, in dem es dich betrifft — der Rahmenteil erklärt Werkzeuge, die erst ab Etappe 8 auftauchen, und wer sie vorher liest, merkt sie sich nicht.

**Die kleinste gültige Sitzung sind fünfzehn Minuten.** Nicht als Notlösung: Ein Projekt über sechs Monate scheitert nicht an zu kurzen Sitzungen, sondern an ausgelassenen. Eine Etappe darf sich über acht Abende ziehen. Zwei Etappen an einem Wochenende durchzuziehen und dann drei Wochen nichts zu tun, ist der schlechtere Weg — auch wenn er sich besser anfühlt.

**Und eine Zusage vorweg:** Nichts in diesem Plan setzt voraus, dass du vorher programmiert hast. Wo etwas schwer ist, steht dabei, dass es schwer ist. Wo etwas dünn ist, steht das auch.

---

## Die Prämisse

Ein Vorposten auf einem Mond, den niemand mehr besucht. Der Reaktorkern hält die Kuppel. Das Evakuierungsschiff kommt in **zwanzig Wellen**. So lange musst du den Kern halten.

Draußen ist die Brut. Sie kommt in Wellen, sie kommt immer wieder, und sie wird jedes Mal größer.

Du bist einer von vier Marines.

| Klasse | Spielerisch | Technisch verankert an |
|---|---|---|
| **Soldat** | Ausgewogen, billige Munition | Der Basisfall — die Zahlen, gegen die alles verglichen wird |
| **Heavy** | Viel Panzerung, viel Schaden, langsam | Abklingzeiten, Nachladen, Zahlenlogik |
| **Engineer** | Baut Geschütze, repariert Sektoren | Objekte mit Bauzeit, Weltzustand zur Laufzeit ändern |
| **Medic** | Heilt, hält Rekruten am Leben | Statuseffekte, Werte über Zeit |

**Und alle vier stehen immer auf dem Feld.** Du steuerst einen. Die anderen drei kämpfen programmgesteuert mit — sie laufen zum nächsten Gegner, bis sie in Reichweite sind, und feuern. Mehr nicht, jedenfalls am Anfang.

Das ist keine Bequemlichkeit, sondern die tragende Konstruktion dieses Plans:

**Eine Regel, die alles trägt: Die Klassenwahl bestimmt, wen du steuerst — nicht, was verfügbar ist.** Der Engineer baut Geschütze, ob du ihn spielst oder nicht. Der Medic heilt so oder so. Wenn du je in die Lage kommst, dass eine Etappe eine bestimmte Klassenwahl *voraussetzt*, ist das ein Konstruktionsfehler und keine Spielregel.

**Was der Trupp didaktisch leistet** — und das ist der eigentliche Grund, warum er existiert:

| | Ohne Trupp | Mit Trupp |
|---|---|---|
| **Etappe 11** (Vererbung) | Drei der vier Klassen sind toter Code, den du nie laufen siehst | Vier Objekte in einer Liste, vier verschiedene `faehigkeit_einsetzen()`, alle sichtbar |
| **Etappe 12** (Tick) | Nur Gegner ticken | Jede Einheit tickt — der Unterschied „gesteuert" ↔ „autonom" wird greifbar |
| **Etappe 14** (Raster) | Abstände braucht nur das Geschütz | Vier Einheiten suchen den nächsten Gegner — dieselbe Rechnung, vier Aufrufer |
| **Etappe 23** (Funktionen als Werte) | Zielauswahl betrifft Geschütze | Zielauswahl betrifft Geschütze *und* Marines — die Auslagerung wird zwingend statt hübsch |

**Die Trupp-KI ist absichtlich dumm** und bleibt es bis Etappe 18. Nächsten Gegner suchen, hinlaufen, schießen — das ist alles. Sie ist ein Rabbit Hole wie Balancing, und es gilt dieselbe Regel: Wer drei Sitzungen lang nur an der KI schraubt, hat kein Python gelernt.

Im Code existieren ab Etappe 11 alle vier Klassen gleichzeitig.

**Die Zusatzregel dazu:** Fällt ein Trupp-Marine, ist er nicht tot, sondern *ausgefallen* — und kommt nach einem Zähler zurück, genau wie ein Rekrut. Fällt **dein** Marine, ist das Spiel vorbei. Der Unterschied ist die ganze Spannung.

**Was du dazwischen tust:** Wellen überstehen, Schrott einsammeln, im Depot kaufen — Waffen, Module, Fähigkeiten, Geschütze. Und **Rekruten**. Ein Rekrut hält ein Tor, das du gerade nicht halten kannst. Wenn er fällt, läuft ein Nachschubzähler; irgendwann steht ein neuer da. Du kaufst dir also kein Leben, sondern eine **Stelle**, die dauerhaft besetzt wird. Genau diese Unterscheidung ist später eine der schöneren Modellierungsfragen im Code.

**Namen sind deine Baustelle.** Vorposten, Kern, Brut, Rekrut — das sind Platzhalter. Wie deine Gegner heißen und wie deine Klassen heißen, entscheidest du. Die Struktur nicht.

---

## Warum dieses Setting — ehrlich eingeordnet

Dieser Plan ist die Portierung eines Dorf-RPGs. Der Grund für den Umzug war nicht, dass das RPG schlecht war, sondern dass es **Schreibarbeit erzwang**: Dialoge, Ortsbeschreibungen, Motive, ein Rätsel, das aufgehen muss. Wer 25 Minuten am Tag hat, verbringt davon schnell fünfzehn mit Prosa und zehn mit Python.

**Was du gewinnst:**

- **Zahlen statt Prosa.** Ein Gegnertyp ist ein Tabelleneintrag, kein Charakter mit Motiv. Ab Etappe 6 hat er zwei Beschreibungstexte, ab 17a Kosten, ab 21b Widerstände — aber nie eine Vorgeschichte. Der Inhalt deines Spiels ist eine Tabelle.
- **Die Schleife ist von selbst da.** Ein Wellenspiel *ist* eine Schleife mit Zähler. `range()` hat ab Etappe 3 einen echten Zweck statt bis Etappe 14 zu warten.
- **Der Tick ist unvermeidlich.** In einem RPG muss man begründen, warum die Welt tickt. Hier fällt das Spiel ohne Tick auseinander: Gegner rücken vor, Abklingzeiten laufen, Geschütze bauen sich, Rekruten kommen nach.
- **Fehler vom Typ 3 werden greifbar.** Wo gerechnet wird, kann etwas leise falsch sein. Eine Schadensformel, die nie abstürzt und trotzdem Unsinn liefert, ist der beste Lehrmeister, den dieser Plan hat.
- **Tests haben Ziele.** Schadensformel, Wellenbudget, Kaufvorgang, Nachschubzähler — alles prüfbar, alles ohne Verrenkung.

**Was du verlierst — und das steht hier, damit du es vorher weißt:**

- **Das Rätsel.** Das RPG hatte einen Sog: *Warum sind alle weg?* Ein Verteidigungsspiel hat einen anderen Sog: *Schaffe ich Welle 14?* Wenn dich Geschichten mehr ziehen als Systeme, ist das ein echter Verlust. Wenn dich Systeme mehr ziehen, ist es ein Gewinn.
- **Dialogbäume.** Im RPG waren Dialoge das Vehikel für Booleans, Flags und datengetriebenes Design. Hier tragen dieselben Themen auf anderen Systemen (Fähigkeiten, Freischaltungen, Statuseffekte). Kein Python-Thema fällt weg — nur das Vehikel wechselt.
- **Die Ortserkundung.** Zwischen Toren wechseln ist taktisch, nicht neugierig. Das Dorf hatte Räume zum Entdecken, der Vorposten hat Stellungen zum Wählen.

**Und eine Gefahr, die das RPG nicht hatte:** Balancing. Dazu unten ein eigener Abschnitt. Nimm ihn ernst — er ist der wahrscheinlichste Grund, warum dieses Projekt scheitern könnte.

---

## Die zwei Fähigkeiten

Es gibt zwei Arten, ein Projekt abzuschließen:

**„Mein Inventar funktioniert."** — Du erinnerst dich an deinen eigenen Code.
**„Ich kann mit Listen umgehen."** — Du beherrschst das Konzept.

Der erste Zustand fühlt sich wie der zweite an. Er ist es nicht.

Und es gibt zwei Fähigkeiten, die ebenfalls nicht dasselbe sind:

**Python schreiben** — du bringst deine Absicht in Code.
**Python lesen** — du verstehst Code, den jemand anders geschrieben hat.

Für dein eigentliches Ziel ist die zweite die wichtigere. Sie wird in keinem Kurs unterrichtet, weil Kurse dich immer schreiben lassen. Deshalb steht sie ab Etappe 9 fest im Plan.

---

## Die Leseleiter ⭐

Die Leseübungen sind kein Beiwerk, sondern der Weg zum eigentlichen Ziel. Deshalb wachsen sie in vier Stufen, und jede Stufe hat einen anderen Anspruch:

| Stufe | Etappen | Umfang | Die Leitfrage |
|---|---|---|---|
| 1 | 9–11 | 5–10 Zeilen | **Was passiert hier?** Was ist Objekt, was Attribut, was Aufruf? |
| 2 | 12–16 | 15–30 Zeilen | **Was verändert sich — und wer verändert es?** |
| 3 | 17–22 | 30–60 Zeilen | **Warum ist es so gebaut?** Welche Design-Entscheidung steckt dahinter? |
| 4 | 23–27 | ganze Dateien | **Was könnte schiefgehen — und taugt der Code?** Echter KI-Code aus deinen Projekten. |

Die Leitfragen sind die eigentliche Progression. Stufe 1 fragt nach dem *Was*, Stufe 2 nach dem *Wer*, Stufe 3 nach dem *Warum*, Stufe 4 nach dem *Urteil*. Wer bei Stufe 4 anfängt, rät.

**Auf den Stufen 1 bis 3 sind es immer dieselben fünf Fragen.** Die Wiederholung ist der Punkt — nach zehn Malen stellst du sie dir automatisch, auch wenn niemand sie stellt:

> 1. Was kommt rein?
> 2. Was passiert?
> 3. Was verändert sich — und woran?
> 4. Was kommt raus?
> 5. Welche anderen Objekte oder Funktionen werden dabei aufgerufen?

**Auf Stufe 4 kommt die sechste dazu, und sie ist die eigentliche:**

> 6. Was hältst du hier für die schwächste Stelle?

Frage 1 bis 5 kann man mit genug Geduld immer beantworten. Frage 6 verlangt ein Urteil, und ein Urteil setzt voraus, dass du Alternativen kennst. Deshalb steht sie erst am Ende — und deshalb ist Etappe 27 die Prüfung dieses ganzen Lehrplans und nicht bloß seine letzte Etappe.

**Die Regel dabei: Du tippst nichts ab.** Leseübungen werden gelesen und beantwortet, nicht ausgeführt. Wer den Code laufen lässt, lässt das Programm die Frage beantworten statt sich selbst.

---

## Wiederkehrende Lesemuster

Drei Dinge tauchen in fremdem Python so oft auf, dass sie eigene Aufmerksamkeit verdienen. Sie sind kein Stoff für eine Etappe, sondern ein Faden, der durch alle läuft — und in jeder Etappe steht, wo er gerade zahlt.

**1. Die Null-Falle.** `if munition:` und `if munition is not None:` bedeuten etwas anderes, sobald `0` ein gültiger Wert sein kann. In diesem Spiel ist `0` überall: leere Magazine, abgelaufene Zähler, Index 0, Panzerung 0, ein Gegner auf Feld 0. Das ist die häufigste stille Fehlerquelle, die dir begegnen wird — in fremdem Code wie in deinem. Aufgebaut in Etappe 2 (truthy/falsy), verschärft in 10 (`None` ≠ `0`), zur Falle in 18 (`or`), nach JSON übersetzt in 19 (`null`).

**2. Die drei Schleifenformen.** Du musst sie beim Lesen sofort auseinanderhalten:

```python
for x in dinge:                   # nur der Wert
for k, v in daten.items():        # Schlüssel und Wert
for i, x in enumerate(dinge):     # Index und Wert
```

Angelegt in Etappe 3 und 5, geübt als Erkennungsdrill in Etappe 14.

**3. Die Importzeile ist das Inhaltsverzeichnis.** Lange bevor du selbst Module schreibst (Etappe 24), begegnen sie dir beim Lesen. Ab Etappe 9 gehört deshalb zu jeder Leseübung die Frage: *Woher kommt dieser Name?* Aus dieser Datei, aus einem Import, oder aus `self`? Wer das nicht trennen kann, hält jeden unbekannten Namen für Magie.

---

## Drei Kompetenzen, nicht eine

Der Plan misst nicht „wie viel Python kannst du". Er entwickelt drei Fähigkeiten nebeneinander, und ihr Verhältnis verschiebt sich absichtlich:

| | Frage | Woran du es übst |
|---|---|---|
| **A — Bauen** | Kann ich es selbst schreiben? | Auftrag, Transferaufgabe |
| **B — Lesen** | Kann ich fremden Code nachvollziehen? | Leseleiter, Bug-Jagd |
| **C — Beurteilen** | Kann ich sagen, ob dieser Code taugt? | Design-Entscheidungen, „Warum nicht?", KI-Warnsignale |

```
Block 1 (1–8)     A ██████████   B ██         C ░
Block 2 (9–16)    A ████████     B ██████     C ███
Block 3 (17–27)   A ██████       B █████████  C █████████
```

Fast jeder Kurs trainiert nur A. Dein Ziel liegt aber bei B und C — und die kommen nicht von allein, wenn man lange genug baut. Deshalb stehen sie hier als eigene Elemente im Plan und nicht als Nebenwirkung.

---

## Das Ritual: Vorhersagen → Ausführen → Vergleichen → Erklären

Gilt ab Etappe 1 für **jedes** Kaputtmach-Experiment und jeden neuen Code, den du zum ersten Mal laufen lässt:

> 1. **Vorhersagen.** Schreib auf, was passieren wird. Vor dem Ausführen. Ein Satz genügt.
> 2. **Ausführen.**
> 3. **Vergleichen.** Was war anders?
> 4. **Erklären.** Warum war deine Vorhersage falsch?

Punkt 1 ist der ganze Trick, und er ist der, den alle überspringen. Ohne Vorhersage ist Ausführen nur Zuschauen — du siehst ein Ergebnis und rationalisierst es hinterher als „ja klar, logisch". Mit Vorhersage stellst du fest, wo dein inneres Modell des Programms von der Wirklichkeit abweicht. **Genau dieses innere Modell ist das, was dir beim Lesen von KI-Code fehlt.**

Und wenn deine Vorhersage stimmt: auch gut. Dann hast du in fünf Sekunden bestätigt, dass du verstanden hast, statt es zu hoffen.

---

## Die Struktur jeder Etappe

1. **Boot.dev** — was du dort lernst
2. **Was du baust** — die Anwendung im Spiel
3. **Lernziele** — was du danach *ohne Hilfe erklären* können musst
4. **Entweder Transferaufgabe oder Leseübung** — 5–15 Minuten
5. **Kaputtmach-Experiment** — absichtlich zerstören und beobachten
6. **Commit**

**Ab Etappe 17 kommt ein siebter Punkt dazu: die Entwicklerfrage.** Zwei bis fünf Sätze, keine Musterlösung. Sie steht weiter unten in einem eigenen Abschnitt.

**Punkt 4 ist ein Entweder-oder, kein Und.** Bei 20–30 Minuten am Tag ist die größte Gefahr nicht, zu wenig zu üben — sondern dass der Plan zur Bürokratie wird und du aufhörst. Sechs Pflichtelemente pro Etappe wären genau das.

**Und was hier bewusst *nicht* steht: eine Liste „Am Ende kannst du…".** Sie wäre schnell geschrieben und würde nichts prüfen. Ein Häkchen hinter *„Ich kann Zustandsautomaten erklären"* setzt man aus dem Gefühl heraus, und das Gefühl täuscht — Wiedererkennen fühlt sich an wie Wissen. Deshalb sind die Lernziele hier **Fragen** und keine Behauptungen: Eine Frage kann man beantworten oder eben nicht, und der Unterschied fällt sofort auf. Das ist der ganze Grund, warum sie diese Form haben.

**Transferaufgabe:** Bewusst *außerhalb* des Spiels, in einer Wegwerf-Datei. Wenn du eine Liste nur im Kontext deines Inventars bedienen kannst, kannst du keine Listen. Obergrenze 15 Minuten.

**Leseübung:** Ich zeige dir fremden Code, du erklärst ihn — Umfang und Anspruch nach der Leseleiter oben, Fragen immer dieselben fünf. Nicht „schreib das", sondern: erklären, ohne auszuführen.

**Kaputtmachen:** Kein Spaßelement. „So schreibt man es" ist Auswendiglernen. „Warum muss es so sein" ist Verstehen. Der einzige verlässliche Weg dorthin führt über die Fehlermeldung.

---

## Die drei Anspruchsstufen ⭐

**Das ist die wichtigste Regel dieses Plans, und sie steht bewusst weit vorne.**

Ab Etappe 2 beginnt fast jede Etappe mit einer kleinen Tabelle, die den Stoff in drei Stufen einteilt. Diese Einteilung ist keine Deko, sondern das Mittel gegen den einen Fehler, an dem Selbstlern-Projekte reihenweise scheitern: **alles gleich wichtig zu nehmen.**

| Stufe | Heißt | Woran du merkst, dass du fertig bist |
|---|---|---|
| 🔨 **Bauen** | Du schreibst es selbst, in dein Spiel | Es läuft, der Selbsttest ist grün |
| 🧠 **Verstehen** | Du kannst erklären, warum es so ist und was die Alternative wäre | Du beantwortest die Lernzielfrage in eigenen Worten |
| 👀 **Nur erkennen** | Du siehst es in fremdem Code und weißt in einem Satz, was es tut | Du sagst den einen Satz — und gehst weiter |

**Die dritte Stufe ist die, die dich rettet.** Es ist völlig in Ordnung, nach Etappe 23 zu sagen: *„Ich weiß ungefähr, was ein Dekorator ist. Schreiben könnte ich noch keinen."* Das ist kein Rückstand, sondern die richtige Stufe — für dein Ziel sogar die produktivste. Wer aus jedem Konzept eine Übung macht, kommt bei Etappe 14 zum Stehen und hat dann viel gelernt und nichts gebaut.

**Und umgekehrt:** Was auf Stufe 1 steht, wird gebaut. Da gibt es kein Überfliegen. Eine Etappe ist fertig, wenn Stufe 1 läuft — nicht, wenn Stufe 3 vollständig verstanden ist.

---

## Vorausverweise sind Buchhaltung, keine Hausaufgabe

Dieser Plan sagt oft Sätze wie *„das zahlt in Etappe 22"* oder *„hier wird die Schuld aus Etappe 4 eingelöst"*. Das ist Absicht — es ist der Grund, warum sich das Projekt wie ein Bogen anfühlt und nicht wie dreißig Übungsaufgaben.

**Aber es ist nicht deine Aufgabe, diesen Bogen im Kopf zu tragen.**

Wenn du bei Etappe 6 liest, dass Sets in Etappe 14 wichtig werden, ist die richtige Reaktion: *„aha, gut"* — und weiter. Nicht: *„ich muss jetzt schon verstehen, wofür."* Du löst heute ein Problem, das dein Spiel heute hat. Der Rückblick kommt von selbst, und er kommt als der befriedigendste Satz dieses ganzen Projekts:

> *„Ach — DESHALB haben wir das damals so gebaut."*

Der Bogen ist meine Buchführung. Deine ist `GELERNT.md`.

---

## Das übergreifende Prinzip

> **Neue Funktionalität hinzufügen, ohne bestehende kaputtzumachen.**

Das ist keine Etappe, sondern der Maßstab für alles ab Block 2. Anfänger denken: Programmieren = neuen Code schreiben. In Wirklichkeit besteht der Beruf zum großen Teil daraus, bestehenden Code zu verstehen und vorsichtig zu verändern.

Deshalb tauchen im Plan immer wieder Aufgaben dieser Form auf: *„Füge einen neuen Gegnertyp hinzu, ohne die Wellenlogik anzufassen."* Wenn das nicht geht, ist das eine Erkenntnis über deinen Code — nicht über dein Können.

---

## Die Balancing-Falle ⚠️

Ein Verteidigungsspiel ist eine Maschine mit Stellschrauben. Sobald sie läuft, willst du drehen. Das ist der angenehmste Zeitfresser, den dieses Projekt zu bieten hat: Es fühlt sich wie Arbeit an, du lernst dabei aber kein Python.

**Drei Regeln, ab Etappe 3 gültig:**

1. **Balancing hat ein Zeitlimit.** Fünfzehn Minuten, dann Schluss. Aufschreiben, was dir aufgefallen ist, und beim nächsten Mal weitermachen.
2. **Balancing findet auf einem Branch statt** — spätestens ab Etappe 21, wo du Branches sowieso lernst. Vorher: separater Commit, den du zur Not wegwirfst.
3. **Eine langweilige Welle, die läuft, schlägt eine spannende Welle, die abstürzt.** Balance ist die letzte Schicht, nicht die erste.

**Der Test, ob du in der Falle sitzt:** Wenn du bei der letzten Sitzung nur Zahlen geändert hast und keine Zeile Struktur — dreimal hintereinander — dann steckst du fest. Das ist keine Schande, sondern ein Signal: Weiter zur nächsten Etappe, die Zahlen laufen dir nicht weg.

---

## Die Darstellung — ASCII von Anfang an

Grundsatz 2 sagt: Grafik kommt zum Schluss. Das gilt weiter und ohne Ausnahme. Aber **ASCII ist keine Grafik.** Ein Raster aus Zeichen ins Terminal zu schreiben ist eine Schleife und ein `print()` — also genau der Stoff, den du in der jeweiligen Etappe ohnehin lernst.

Deshalb wächst die Darstellung von Etappe 1 an mit:

| Etappe | Was du siehst | Wovon es lebt |
|---|---|---|
| 1 | Ein fester Kopf mit der Lage | mehrzeiliger String, f-Strings |
| 3 | Balken statt Zahlen: `Kern [#######...]` | `"#" * anzahl` |
| **4** | **Die Anmarschbahn als eine Zeile:** `S..K...K....@` | Liste, Index, `len()`, `remove()` |
| 5 | Grundriss des Vorpostens, aktueller Sektor markiert | Dictionary |
| 14 | Aus der einen Zeile werden mehrere | verschachtelte Listen |
| 29 | Aus Zeichen werden Kacheln | Pygame |

**Etappe 4 ist der Durchbruch.** Eine einzelne Zeile, in der Gegner aufrücken und verschwinden, ist der Moment, in dem dein Spiel aufhört, eine Zahlenkolonne zu sein. Und sie ist kein Zugeständnis an die Optik: Der berüchtigte Fehler „eine Liste verändern, während man über sie läuft" ist im Text unsichtbar und auf der Bahn sofort erkennbar — ein Gegner überspringt einen Schritt. Die Darstellung ist hier ein Debugging-Werkzeug.

**Zwei Riegel, sonst frisst dich das:**

1. **Die Darstellung ist immer der letzte Schritt einer Etappe.** Erst wenn der Selbsttest grün ist. Sonst verbringst du Etappe 4 mit Rahmenzeichen statt mit Listen.
2. **Zehn Minuten, dann Schluss.** Es gilt dieselbe Regel wie beim Balancing, und aus demselben Grund: Es fühlt sich wie Arbeit an.

Ab Etappe 7 lebt die Darstellung in eigenen Funktionen, die nur zeichnen und nichts entscheiden. Ab da gilt die Trennung, die in Etappe 28 alles rettet: **Die Logik rechnet und gibt zurück. Die Darstellung gibt aus.** Wer beides vermischt, schreibt sein Spiel für Pygame neu.

---

## 🚨 KI-Code-Warnsignale

Ab Etappe 8 tauchen in den Guides kleine Kästen mit diesem Zeichen auf. Sie zeigen ein Muster, das in KI-generiertem Python auffällig oft vorkommt — zusammen mit der Frage, die du daran stellst.

Ein Warnsignal ist **kein Fehler**. Jedes dieser Muster ist manchmal genau richtig. Ein Warnsignal heißt: *Hier lohnt sich eine Frage, bevor du weitergehst.* Genau das ist der Unterschied zwischen „ich lasse den Code laufen" und „ich beurteile ihn".

Ein Vorgeschmack, damit klar ist, was gemeint ist:

| Was du siehst | Was du fragst |
|---|---|
| `except Exception:` oder `except:` | Welcher Fehler wird hier eigentlich verschluckt? |
| `def update(self, welt):` | Warum braucht diese Klasse die *ganze* Welt? |
| Eine `elif`-Kette aus zwölf fast gleichen Zweigen | Sind das nicht eigentlich Daten? |
| `def verarbeite_alles(...)` mit acht Parametern | Wie viele Dinge tut diese Funktion? |
| `if x:` bei einem Zahlenwert | Kann `x` legitim `0` sein? |
| Kein einziger Test, keine einzige Prüfung | Woran erkennt man hier, dass es funktioniert? |

Die Sammlung wächst mit dem Plan. Am Ende ist sie das Werkzeug, mit dem du in Etappe 27 fremden Code beurteilst.

---

## Beobachtbarkeit — die Frage, die ab Etappe 8 immer mitläuft

> **Woher weißt du, dass dein Programm das Richtige tut?**

„Es läuft" ist keine Antwort. „Es stürzt nicht ab" auch nicht. Die Frage verlangt eine **Beobachtung**, die es beweist.

Beispiel aus Etappe 13: Dein Geschütz hat `bauzeit = 8`. Woran erkennst du, dass es nach genau acht Ticks aktiv wird und nicht nach sieben oder neun? Nicht daran, dass es irgendwann feuert — sondern daran, dass du den Zähler sichtbar machst, mitzählst und vergleichst.

Diese eine Frage verbindet fast alle späteren Werkzeuge des Plans miteinander:

| Werkzeug | Etappe | Macht beobachtbar |
|---|---|---|
| Der Balken statt der Zahl | 3 | Werte außerhalb des gültigen Bereichs |
| Die Anmarschbahn | 4 | Einheiten, die übersprungen werden |
| `assert` | 7 | Eine gebrochene Annahme, an der Stelle wo sie bricht |
| Der Debugger | 8 | Jeden Zwischenzustand |
| `__repr__` | 9 | Was wirklich im Objekt steht |
| Fester Seed | 17 | Reproduzierbarkeit trotz Zufall |
| Speicherstand | 19 | Den kompletten Zustand als Text |
| Logging | 20 | Abläufe, ohne den Code zu ändern |
| Tests | 26 | Alle Annahmen auf einmal |

Wer diese Frage bei jedem Feature stellt, baut nebenbei ein Programm, das sich debuggen lässt. Wer sie nie stellt, baut eines, das nur funktioniert, solange es funktioniert.

---

## „Warum nicht die naheliegende Alternative?"

Zu fast jeder Design-Entscheidung im Plan gehört eine Gegenfrage. Sie steht in den Guides ausdrücklich dabei, weil eine Begründung ohne Alternative keine Begründung ist:

| Etappe | Die Wahl | Die Gegenfrage |
|---|---|---|
| 6 | Set für Freischaltungen | Warum keine Liste mit Prüfung? |
| 11 | Vier Klassen | Warum nicht vier Dictionaries? |
| 12 | Die Welt tickt | Warum tickt nicht jede Einheit selbst? |
| 14 | Raster fürs Vorfeld | Warum kein Dictionary wie bei den Sektoren? |
| 19 | `pathlib` | Warum nicht einfach Strings zusammenbauen? |
| 22 | Baupläne als Daten | Wann wäre eine Klasse besser? |
| 23 | Funktionen im Dictionary | Warum nicht weiter `if`/`elif`? |
| 24 | Mehrere Module | Warum nicht alles in einer Datei? |
| 25 | JSON als Content | Warum nicht Python-Dateien mit Daten? |

**Die Antwort „weil man das so macht" gilt nicht.** Wenn dir zu einer Zeile keine Alternative einfällt, hast du sie nicht verstanden, sondern abgeschrieben.

**Und deshalb steht in diesem Plan fast nirgends „X ist besser als Y".** Wo es doch so klingt, ist immer *„für dieses Problem, an dieser Stelle, aus diesem Grund"* gemeint. Werkzeuge sind Entscheidungen, keine Religion. Ein Lehrplan, der dir feste Architekturregeln beibringt, produziert jemanden, der Dogmen nachspricht — und du sollst am Ende jemand sein, der zwei mögliche Lösungen sieht und ihre Nachteile benennen kann. Wenn dir eine Formulierung hier zu absolut vorkommt: Das ist eine berechtigte Rückfrage, keine Störung.

---

## Vor jedem Umbau: drei Fragen — ab Etappe 4

Dieser Plan lässt dich mehrfach etwas umbauen, das schon funktioniert: die Gegnerzahl wird eine Liste (4), die Munition wandert ins Dictionary (5), alles wandert in Funktionen (7a) und dann in Objekte (9). Jedes Mal fühlt es sich falsch an — da läuft etwas, und du reißt es auseinander.

**Deshalb steht ab Etappe 4 vor jedem Umbau dasselbe kleine Ritual:**

> **Was bleibt gleich? Was ändert sich nur in der Darstellung? Was ändert sich wirklich am Datenmodell?**

Die dritte Zeile ist immer die kürzeste. Alles andere ist Beweislast — und dafür gibt es in jedem betroffenen Guide einen eigenen Auftragsschritt, der prüft, dass das Bestehende noch tut, was es tat.

**Der Ertrag ist ein Reflex, der weit über dieses Projekt hinausreicht:**

> **Umbauen heißt nicht „alles neu". Es heißt: eine Sache ändert sich, alles andere beweist, dass es noch funktioniert.**

**Und die Migrationen selbst sind festgelegt, nicht dem Zufall überlassen** — welcher Wert ab wann wo lebt, steht in `BOGEN.md` in einer eigenen Tabelle. Das ist wichtiger, als es klingt: Ohne diese Festlegung entstehen zwei Wahrheiten über dieselbe Sache, und das ist die Fehlerquelle, die am längsten unentdeckt bleibt.

---

## 🧠 Die Entwicklerfrage — ab Etappe 17

Ab Block 3 gehört zu jeder Etappe eine Frage, die **kein Lernziel und keine Aufgabe** ist. Sie hat keine Musterlösung, und ich habe sie auch nicht. Sie ist die Sorte Frage, über die in echten Projekten in Besprechungen gestritten wird:

| Etappe | Die Entwicklerfrage |
|---|---|
| 17 | Wie viel Zufall ist noch fair? |
| 18 | Wo gehört Zustand hin — zur Einheit oder zur Welt? |
| 19 | Was muss ein Spielstand garantieren? |
| 20 | Welchen Fehler zeige ich dem Spieler, welchen dem Entwickler? |
| 21 | Welche Werte gehören wirklich zum Kampfsystem — und welche nur zur Waffe? |
| 22 | Was ist Inhalt, und was ist Verhalten? |
| 23 | Wer muss wen kennen? |
| 24 | Wann macht Aufteilung Code besser, und wann nur komplizierter? |
| 25 | Wem vertraue ich — meinem Code, meinen Daten oder keinem von beiden? |
| 26 | Was beweist ein grüner Test eigentlich? |
| 27 | Woran erkennst du, dass jemand über seinen Code nachgedacht hat? |

**Zwei bis fünf Sätze in `GELERNT.md`, mehr nicht.** Der Wert liegt nicht in der Antwort, sondern darin, dass du sie in vier Wochen wiederliest und merkst, dass du inzwischen anders denkst. Genau das ist der Unterschied zwischen „ich kann Python" und „ich kann Software entwickeln".

---

## Nie erklären, was du selbst herausfinden kannst

Eine Regel für dich und für deinen Mentor gleichermaßen. Wenn eine Frage durch Lesen, Ausprobieren oder Debuggen zu beantworten ist, kommt die Antwort **nicht** sofort.

Auf *„was macht `foo()`?"* lautet die erste Antwort nicht „`foo()` macht X", sondern: **wie würdest du es herausfinden?** `print(foo)`, `help(foo)`, `dir(objekt)`, F12 im Editor, ein Breakpoint. Erst wenn das nicht trägt, kommt die Erklärung.

Der Grund ist unangenehm konkret: Eine Erklärung *wiederzuerkennen* fühlt sich genauso an wie sie zu *wissen*. Es ist aber nicht dasselbe, und der Unterschied fällt erst auf, wenn niemand mehr da ist, den man fragen kann. Genau dieser Zustand ist der, aus dem dich dieses Projekt herausholen soll.

---

## `GELERNT.md` — ein festes Format

Zwei Sätze pro Etappe reichen nicht ganz. Nimm dieses Gerüst; es kostet drei Minuten:

```markdown
# Etappe 12

## Was habe ich gebaut?
## Was habe ich verstanden?
## Was hat mich überrascht?
## Welchen Fehler habe ich gemacht?
## Wie habe ich ihn gefunden?     ← der wichtigste Punkt
## Welche Entscheidung habe ich getroffen, und warum?
```

**Die vorletzte Zeile ist die, für die sich das Ganze lohnt.** *Was* der Fehler war, ist in vier Wochen wertlos — du machst dann andere. *Wie du ihn gefunden hast*, ist übertragbar, und es ist genau die Fähigkeit, die du beim Debuggen von fremdem Code brauchst.

Nach drei Monaten ist diese Datei außerdem der einzige verlässliche Beweis dafür, wie weit du gekommen bist.

---

## Die Bug-Jagd

Fehlerbehandlung und Debugging sind **nicht dasselbe**. `try/except` verhindert Abstürze. Debugging heißt herausfinden, *warum* etwas nicht tut, was es soll.

**Drei Sorten Fehler, nach Schwierigkeit:**

1. Stürzt sofort ab — unangenehm, aber ehrlich
2. Stürzt manchmal ab — schwerer, weil er von Bedingungen abhängt
3. **Stürzt nie ab und liefert einfach das Falsche** — die gefährlichste Sorte

Der dritte Typ ist der wichtigste, weil er eine der schädlichsten Überzeugungen zerstört, die Anfänger haben: *„Wenn Python keinen Fehler anzeigt, ist mein Programm richtig."*

**Und dazu eine zweite Achse — nicht das Symptom, sondern die Ursache.** Die drei Typen oben beschreiben, *wie sich ein Fehler zeigt*. Diese vier beschreiben, *woher er kommt*, und sie sind die eigentliche Suchhilfe:

| Ursache | Die Frage | Typisch in diesem Spiel |
|---|---|---|
| **Syntax / Typ** | Warum stürzt es ab? | Text statt Zahl aus `input()` |
| **Logik** | Warum rechnet es falsch? | `>=` statt `>`, Formel falsch geklammert |
| **Zustand** | Warum *bleibt* etwas falsch? | Ein Zähler wird nie zurückgesetzt |
| **Reihenfolge** | Warum hängt das Ergebnis davon ab, *wann* etwas passiert? | Gegner bewegen sich, bevor Geschütze feuern |

**Die vierte Zeile ist die, die es in einem RPG kaum gibt und hier überall.** Sobald mehrere Systeme im selben Tick laufen — Gegner, Geschütze, vier Marines, Zähler, Statuseffekte — hängt das Ergebnis an ihrer Reihenfolge. Solche Fehler findest du nicht durch Lesen. Du findest sie, indem du einen Tick von Hand auf Papier mitschreibst. Genau das ist die Übung in Etappe 16.

**Deine Regel ab Etappe 8:** Jede neue Funktion wird mindestens einmal absichtlich kaputtgemacht — und zwar nach Möglichkeit in mehr als einer der vier Ursachen.

**Und das Formular, mit dem du ab Etappe 8 jeden echten Bug angehst.** Das Ritual aus dem Rahmenteil (vorhersagen → ausführen → vergleichen → erklären) gilt für Code, den du *neu* schreibst. Für Code, der sich falsch verhält, gilt sein Gegenstück:

```
Beobachtung:   Der Gegner stirbt manchmal ein Feld zu früh.
Hypothese:     Die Geschütze feuern vor der Bewegung.
Experiment:    Zwei Zeilen im Tick vertauschen, dieselbe Welle mit demselben Seed laufen lassen.
Ergebnis:      ...
```

Drei Zeilen, bevor du irgendetwas änderst. Der Punkt ist die **Hypothese**: Ohne sie änderst du Dinge, bis es zufällig geht, und weißt hinterher nicht, warum. Genau das meint der Satz *„ich habe etwas geändert und jetzt läuft es"* — und er ist kein Erfolg, sondern eine unbezahlte Rechnung. Ein Experiment ohne Hypothese ist Herumprobieren mit besserem Namen.

**In diesem Setting ist Typ 3 überall.** Eine Schadensformel, die bei Panzerung 0 das Doppelte rechnet. Ein Wellenzähler, der eine Welle überspringt. Ein Nachschubzähler, der bei jedem Tick zweimal heruntergezählt wird. Nichts davon stürzt ab. Alles davon macht dein Spiel kaputt — und du merkst es erst, wenn du misstrauisch wirst.

**Wie wir es machen — bewusst unvorhersehbar.** Wenn du weißt „nach jedem Block versteckt der Mentor drei Bugs", wird daraus eine Schulaufgabe. Also läuft es zufällig ab. Manchmal ein normales Review. Manchmal manipulierter Code. Manchmal: „Irgendwo in deinem eigenen Code ist ein Fehler — such ihn."

**Eine Zusage dazu:** Ich behaupte nie, dein Code sei fehlerfrei, wenn ich einen Fehler sehe. Und ich behaupte nie, ich hätte einen Fehler eingebaut, wenn ich es nicht getan habe. Die Unvorhersehbarkeit betrifft nur, *ob* manipuliert wird — nie die Wahrheit über deinen eigenen Code.

**Was du dabei lernst:** Tracebacks von unten nach oben lesen. Den Debugger (Breakpoint, Variablen inspizieren). Gezielte `print()`-Ausgaben statt Herumraten. Und die Unterscheidung, auf die alles ankommt: *Wo es knallt, ist selten, wo es kaputt ist.*

---

## Git und GitHub — bewusst rationiert

Git ist ein Fass ohne Boden, und es ist kein Python.

**Minimalset für die ersten Monate:**

```
git init / git status / git add . / git commit -m "..." / git push
git log --oneline        # deine Motivationskurve
```

Drei Dateien im Repo: `README.md` (dein Schaufenster), `GELERNT.md` (zwei Sätze pro Etappe), `.gitignore` (`__pycache__/`, `saves/`, `.venv/`).

**Aufgeschoben, und zwar in zwei Schritten:**

- **Etappe 21 — der erste Branch.** Ein Branch ergibt Sinn, wenn du Wellenbalancing ausprobieren und das Ergebnis notfalls wegwerfen willst. Genau dieser Fall tritt dort zum ersten Mal ein, und keinen Tag früher.
- **Etappe 24 — Merge und Konflikt.** Zusammenführen, einen Konflikt absichtlich herbeiführen, ihn auflösen, etwas rückgängig machen. Übungsobjekt ist dein Balancing-Branch von Etappe 21.

**Pull Requests bleiben optional.** Wer allein an einem Repo arbeitet, stellt sich mit einem PR einen Briefkasten in die eigene Wohnung. Das Verfahren ist in fünfzehn Minuten gelernt, sobald es einen zweiten Menschen gibt — vorher ist es Zeremonie. Rebase und Cherry-Pick stehen aus demselben Grund gar nicht im Plan.

---

## Arbeitsregeln

**Kein Vibe Coding in diesem Projekt.** Du schreibst jede Zeile selbst. Wenn du feststeckst: „Ich will X, habe Y probiert, es passiert Z — woran könnte es liegen?"

**Etappen dürfen halbiert werden — und sieben sind es bereits.** Der Plan ist ein Vorschlag, kein Vertrag.

Sieben Etappen tragen so viel Stoff, dass sie an einem Stück nur halb ankommen. Die sind ausdrücklich geteilt, mit einem eigenen Commit dazwischen:

| Geteilt | Erste Hälfte | Zweite Hälfte |
|---|---|---|
| **3a / 3b / 3c** ⭐ | siehe unten — als einzige **drei**geteilt | |
| **7a / 7b** | Funktionen, Parameter, `return`, Scope | Darstellung als eigene Schicht, `assert` |
| **9a / 9b** | Klasse, `__init__`, `self`, Methoden | `__repr__` fürs Debugging |
| **14a / 14b** | Das Raster, `[y][x]`, Bewegung, Ränder | Reichweite, Sensorabdeckung, Trupp-Bewegung |
| **17a / 17b** | Zufall und das Wellenbudget | Ereignisse und der Seed als Werkzeug |
| **21a / 21b** | Trefferrechnung und Rückgabewerte | Schadenstypen, `Enum`, Balancing-Branch |
| **23a / 23b** | Python lesen | Python modellieren |

**Etappe 3 ist die einzige mit drei Portionen:** 3a die Schleife, 3b die Befehle, 3c Kampf und Anzeige. Hier wird aus einem Skript ein Spiel, und das ist der dichteste Punkt des ganzen Fundaments.

**Die Nummer bleibt, weil das Thema eines ist.** Es bleiben 30 Etappen — gerechnet in Portionen sind es 38, dazu Etappe 0. Und wenn dir eine ungeteilte Etappe zu groß vorkommt, teil sie selbst. Das ist keine Kapitulation, sondern die Anwendung derselben Regel.

**Umwege haben Vorrang.** Wenn dein eigenes Programm eine Frage erzeugt, ist diese Frage die nächste Lektion — auch wenn sie hier nicht steht.

---

## Zeitrahmen

Bei 20–30 Minuten am Tag, Übungen eingerechnet — und mit den geteilten Etappen als getrennte Portionen gerechnet:

| Block | Etappen | Portionen | Dauer |
|---|---|---|---|
| Werkzeug | 0 | 1 | 1 Abend |
| Fundament | 1–8 | 11 | 9–12 Wochen |
| Einheiten und Zeit | 9–16 | 10 | 10–13 Wochen |
| Der Vorposten reagiert | 17–27 | 14 | 14–18 Wochen |
| Grafik (optional) | 28–30 | 3 | offen |

Eine Portion sind zwei bis vier Sitzungen. Wenn du bei sechs bist, ist das kein Rückstand — die Zahlen hier sind Erfahrungswerte, keine Vorgaben.

Der Punkt, an dem sich das eigentliche Ziel einlöst, ist Etappe 27.

### Die Meilensteine — sechs Abende, an denen es klick macht

Ein halbes Jahr ist lang, und Fortschritt fühlt sich in der Mitte nach nichts an. Deshalb hier vorab die Abende, an denen etwas passiert, das du *siehst*:

| Etappe | Was passiert | Warum es sich anders anfühlt |
|---|---|---|
| **3a** | Das Programm wartet auf dich | Ab hier ist es ein Spiel und kein Skript |
| **4** | `S..K...K....@` — Gegner rücken sichtbar auf | Dein Spiel hat ein Bild, aus einer Liste gebaut |
| **12** | Die Welt tickt, auch wenn du nichts tust | Der Motor läuft, nicht mehr nur die Anzeige |
| **13** | Hinter dir feuert ein Geschütz, das du vor fünf Runden bestellt hast | Der Beweis, dass der Tick echt ist — der schönste Moment des ganzen Plans |
| **14a** | Ein Raster, auf dem sich etwas bewegt | Dein Spiel hat eine Karte |
| **17a** | Welle 14 ist jedes Mal anders und trotzdem fair | Dein Spiel erzeugt Inhalt, statt ihn abzuspielen |
| **25** | Ein neuer Gegnertyp sind vier Zeilen in einer Textdatei | Du entwirfst, ohne zu programmieren |
| **27** | Du liest fremden Code und hast eine Meinung dazu | Das war von Anfang an das Ziel |

**Ausdrucken, an den Bildschirm hängen, abhaken.** Das klingt albern und wirkt trotzdem.

### An Tagen, an denen nichts geht

Das kommt. Bei sechs Monaten ist es keine Frage, ob, sondern wann. Drei Auswege, alle gültig:

1. **`GELERNT.md` öffnen und die letzten drei Einträge lesen.** Das zählt als Sitzung. Du wirst überrascht sein, was du vor vier Wochen noch nicht konntest.
2. **`git log --oneline` laufen lassen.** Vierzig Commits sind vierzig Abende, an denen du es doch gemacht hast.
3. **Eine Etappe halbieren.** Sieben sind es schon; bei den übrigen darfst du es selbst tun. Der Plan ist ein Vorschlag.

**Was du nicht tun solltest: eine Etappe überspringen, weil sie langweilig aussieht.** Etappe 6 (Datenstrukturen) und Etappe 7 (Aufräumen) sehen beide nach nichts aus und sind beide der Grund, warum die nächsten fünf Etappen funktionieren.

**Und was du ebenfalls nicht tun solltest: die Spalte „nur erkennen" zur Pflicht machen.** Sie ist dafür da, dass du weitergehen kannst. Wer sie ernster nimmt als vorgesehen, bleibt bei Etappe 14 stehen — mit sehr viel Wissen und einem halben Spiel.

---

# BLOCK 0 — Werkzeug

## Etappe 0 — Das Repo

Ein Abend, kein Python. Repo auf GitHub, lokal klonen, `README.md`, `GELERNT.md`, `.gitignore`, virtuelle Umgebung (`python -m venv .venv`), erster Commit, erster Push.

**Klein ergänzt, weil es später gebraucht wird:** Aktivier die venv, installier irgendein Paket (`pip install requests`), schau mit `pip list` nach und halt es mit `pip freeze > requirements.txt` fest. Du musst heute nicht verstehen, warum — nur einmal gesehen haben, dass eine venv ein *Ort für Pakete* ist und die Paketliste zum Projekt gehört. Spätestens in Etappe 28 brauchst du das für Pygame.

`requirements.txt` reicht dir lange. In Etappe 24 lernst du ihr Gegenstück `pyproject.toml` kennen — und warum beide nebeneinander existieren dürfen.

**Lernziele:** Was ist ein Commit? Warum existiert `.gitignore`? Wozu eine virtuelle Umgebung — und warum steht `.venv/` in `.gitignore`, `requirements.txt` aber nicht?

**Commit:** `Etappe 0: Projektstart`

---

# BLOCK 1 — Fundament

*Boot.dev: „Learn to Code in Python", erste Kapitel*

## Etappe 1 — Der Abwurf

**Boot.dev:** Variablen, Strings, f-Strings, `print()`, `input()`, Typumwandlung

**Was du baust:**
`spiel.py`. Der Spieler gibt seinen Namen ein und wählt per Zahl eine der vier Klassen. Variablen für `kern_integritaet`, `schrott`, `munition`, `wellen_bis_evakuierung`, `letzte_meldung` — und mindestens drei f-Strings, die daraus ein Lagebriefing bauen. Dann meldest du dich per Funk. Die Antwort ist eine Wiederholung derselben aufgezeichneten Durchsage.

**Auflage als Autor: Nirgends darf wörtlich stehen, dass die Lage aussichtslos ist. Die Zahlen zeigen es.** Rekruten verfügbar: 0. Verstärkung in: 20 Wellen. Munition: 40. Das ist die ganze Atmosphäre, die du brauchst — und sie kostet dich vier Zeilen statt vier Absätzen. Merk dir dieses Verhältnis; es ist der Grund, warum dieses Setting existiert.

**Hier kommt sofort ein echtes Problem, und es besteht aus genau drei Sätzen:**

1. `input()` gibt **immer** Text zurück. Immer. Auch wenn der Spieler `2` tippt.
2. `int()` macht daraus eine Zahl.
3. Erst mit dieser Zahl kannst du rechnen oder vergleichen.

Mehr ist es nicht, und es ist trotzdem der erste Kontakt mit dem Thema, das dich Monate begleiten wird: **Ein Wert hat einen Typ, und der Typ entscheidet, was mit ihm geht.** Vergiss Schritt 2, und dein Programm sieht völlig richtig aus, rechnet aber Unsinn — oder stürzt ab.

*(Die Klassenwahl ist heute nur die Stelle, an der du das übst. Was die gewählte Zahl **bewirkt**, ist Etappe 2. Heute merkst du sie dir nur.)*

Deine übrigen Werte — `kern_integritaet`, `munition`, `schrott` — schreibst du direkt als Zahlen hin. Die kommen nicht aus `input()` und brauchen kein `int()`. Genau dieser Unterschied ist der Lernstoff: **Woher ein Wert kommt, bestimmt, was du mit ihm tun musst, bevor du ihn benutzt.**

**Und schon heute siehst du etwas.** Ein mehrzeiliger String als Kopf — eine grobe Skizze der Kuppel, darunter die Lagewerte per f-String. Das ist `print()` mit `"""` und sonst nichts. Zehn Minuten, ganz am Schluss, wenn der Rest steht. Es ist die erste Zeile einer Darstellung, die bis Etappe 29 wächst.

`letzte_meldung` hebst du auf. In Etappe 17 schreibst du: *„Die Aufzeichnung läuft immer noch. Sie ist von vor achtzehn Tagen."*

**Ehrlich eingeordnet:** Kaum eine Programmier-Übung. Aber sie baut eine Gewohnheit an, die technisch zählt: **Weltzustand wird gespeichert, nicht nur ausgegeben.** Alles, was du heute nur ausgibst, musst du in Etappe 12 nachrüsten.

**Lernziele:**
- Unterschied zwischen einer Variable und ihrem Wert?
- Was macht das `f` vor dem String genau?
- Warum ist `munition = "40"` etwas anderes als `munition = 40`?
- Was gibt `input()` zurück — in welchem Datentyp?
- Was passiert bei `int("drei")`, und was bei `int("3 ")`?

**Transferaufgabe (5 Min):** Frag nach dem Geburtsjahr, berechne das Alter. Achte darauf, was mit dem Rückgabewert von `input()` passieren muss.

**Kaputtmachen:** Lass das `f` weg. Rechne mit `input()`, ohne umzuwandeln. Gib bei der Klassenwahl `zwei` statt `2` ein. `TypeError` und `ValueError` werden deine häufigsten Fehler der nächsten Monate.

**Commit:** `Etappe 1: Der Abwurf`

---

## Etappe 2 — Der erste Kontakt

**Boot.dev:** `if` / `elif` / `else`, Vergleiche, Booleans, `and` / `or` / `not`

**Was du baust:**
Zwei Dinge, die zusammengehören.

Erstens: Die Klassenwahl aus Etappe 1 bekommt Folgen. Je nach Klasse andere Startwerte — Panzerung, Schaden, Trefferpunkte, Startausrüstung. Das ist eine `if`/`elif`-Kette, und sie ist an dieser Stelle genau richtig, auch wenn sie hässlich wird. Sie stirbt in Etappe 11.

Zweitens: Der erste Schuss. Ob du feuern kannst, hängt an mehr als einer Sache — und **genau so soll es aussehen**, nicht als Turm aus verschachtelten `if`:

```python
# fremdes Beispiel, damit die Form klar ist:
if hat_ticket and not gesperrt and alter >= 18:
    print("Einlass.")
```

Eine verknüpfte Bedingung statt drei Ebenen. Das ist die Form, die dir in Etappe 18 als vollständiges Freischaltsystem wiederbegegnet.

**Und ausdrücklich nur die gewählte Klasse.** Ein Spieler, vier mögliche Klassen, **ein** Satz Werte am Ende. Die anderen drei Marines aus der Prämisse existieren heute noch nicht im Code — sie kommen in Etappe 11, wenn du Klassen hast, in denen sie sinnvoll wohnen können.

Das ist wichtig genug für einen eigenen Absatz, weil die Versuchung groß ist: Vier Wertesätze in einer `if`/`elif`-Kette anzulegen wäre technisch möglich und wäre trotzdem falsch. Du würdest heute Daten erzeugen, die dein Spiel nicht benutzt, und dabei genau das lernen, was du nicht lernen sollst. **Eine `if`/`elif`-Kette wählt genau einen Zweig aus. Das ist ihr ganzer Sinn, und den sollst du heute sehen.**

Dazu ein Boolean, der sich etwas merkt: Beim ersten Kontakt siehst du etwas — eine Spur, ein Geräusch, einen Gegner, der sich anders verhält als die anderen. Du meldest es per Funk oder du behältst es für dich. `meldung_abgesetzt = True/False`. Diese Entscheidung wirkt in Etappe 17 mit.

**Lernziele:**
- Wann `elif`, wann mehrere separate `if`? (Echter Unterschied, keine Stilfrage.)
- Was ergibt `"5" == 5`? Warum?
- Was ist „truthy"? Welche Werte sind falsch, ohne `False` zu sein? (`0` ist einer davon — merk ihn dir, er wird dir bei Munition und Abklingzeiten noch wehtun.)
- Was ergibt `not (a and b)` im Vergleich zu `not a and not b`?
- Warum reicht ein Boolean nicht, um „Munition" darzustellen?

**Transferaufgabe (10 Min):** Türsteher. Frag nach Alter und Gästelisten-Status, entscheide mit **einer** verknüpften Bedingung über den Einlass — nicht mit verschachtelten `if`. (Noch ohne Funktion; die kommt in Etappe 7.)

**Kaputtmachen:** Schreib `if am_leben = True:`. Der Klassiker, der jeden einmal eine halbe Stunde kostet. Danach: Rück einen Zweig deiner `elif`-Kette eine Ebene falsch ein und schau, welche Klasse plötzlich welche Werte bekommt — das ist ein Fehler vom Typ 3, mitten in Etappe 2.

**Commit:** `Etappe 2: Der erste Kontakt`

---

## Etappe 3 — Die Wellenschleife ⭐

**Boot.dev:** `while`, `for`, `range()`, `break`, `continue`

**Die einzige Etappe mit drei Portionen.** Hier wird aus einem Skript ein Spiel — und dabei kommt mehr zusammen, als an einem Abend ankommt. Nach jeder Portion ein Commit.

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **3a** | `for` außen, `while` innen, `range()`, `break` | Wann `for`, wann `while` — und warum das keine Geschmacksfrage ist | `continue`, `_` |
| **3b** | Befehlskette, `.lower()`, Rundenzähler | Wo eine Variable angelegt wird, entscheidet, wann sie neu gesetzt wird | — |
| **3c** | Gegner, Feuern, Nachladen, Balken | Warum die Anzeige ein Messgerät ist | Formatangaben im f-String |

**Nach 3a wartet das Programm auf den Spieler. Nach 3b kann er mit ihm reden. Nach 3c kann er verlieren.**

---

### 3a — Die Schleife

Zwei Ebenen, zwei Schleifenarten:

- **außen** die Wellen, eine feste Anzahl → `for` mit `range()`
- **innen** die Runden innerhalb einer Welle, unbestimmt lang → `while`

**Genau diese Gegenüberstellung ist der Lernstoff, und heute nichts anderes.** `for` wenn du weißt, wie oft. `while` wenn du weißt, *wann Schluss ist*, aber nicht, nach wie vielen Durchläufen. Die innere Schleife braucht heute genau einen Befehl, um zu funktionieren: `beenden`. Die Welle endet zusätzlich, wenn keine Gegner mehr da sind (`break`).

**⭐ Und ein Konzept gehört ausdrücklich in 3a und nicht später: Wo lebt welche Variable?** Verschachtelte Schleifen erzeugen drei Ebenen — vor den Schleifen, pro Welle, pro Runde —, und die Zuordnung ist schon für die Gegnerzahl in 3a nötig. Der Guide gibt dafür eine Tabelle mit den konkreten Spielvariablen.

**Zwei Altlasten aus Etappe 2 werden hier eingeordnet:** Der Einzelschuss vom Ende wird ausgeklammert und kehrt in 3c als Befehl zurück. Und die Abbruchbedingung ist **`kern_integritaet`, nicht `trefferpunkte`** — die Gegner greifen die Anlage an, nicht den Marine.

**Dazu zwei Kleinigkeiten, die hier zum ersten Mal gebraucht werden:** `Strg + C` als Notausgang aus der Endlosschleife — einmal absichtlich herbeiführen — und die Regel, dass `break` immer nur *eine* Schleife verlässt.

⭐ **Die Knobelstelle:** Fällt die Kernintegrität auf null, muss auch die äußere Schleife enden. `break` allein reicht dafür nicht. Der Lernende soll das selbst lösen; alle Bausteine sind vorhanden. **Das ist die erste Stelle im Tutorial, an der ein Problem gestellt wird, ohne dass das Verfahren gezeigt wurde** — und sie ist ausdrücklich als solche markiert, damit niemand denkt, er habe etwas Grundlegendes nicht verstanden.

👀 **Nur erkennen: `continue` und `_`.** Beide einmal in einem Wegwerf-Skript sehen, dann weitergehen. Im Spiel wird keines von beiden gebraucht, und `continue` macht eine Schleife schwerer lesbar als eine saubere Bedingung.

---

### 3b — Die Befehle

Befehle: `feuern`, `status`, `nachladen`, `beenden`, plus `else` für Unbekanntes. Die `if`/`elif`-Kette aus Etappe 2, nur mit Wörtern statt Zahlen — und **jetzt** wird `.lower()` gebraucht, das in Etappe 2 bewusst vertagt wurde.

**Die Design-Entscheidung dieser Etappe ist die Befehlssprache.** Ein Wort pro Befehl (`feuern`) oder Verb plus Ziel (`nimm schrott`)? Heute wird bewusst einwortig gebaut; Etappe 4 erzwingt den Umbau. Der kostet zehn Minuten und lehrt, wie sich eine frühe Entscheidung anfühlt, die später Arbeit macht — hier ist diese Erfahrung billig zu haben.

**Dazu eine zweite Design-Entscheidung, die erst beim Spielen auffällt: Welche Befehle kosten eine Runde?** Wenn der Zähler bei jedem Schleifendurchlauf hochzählt, kostet auch `status` Zeit — der Spieler schaut auf seine Munition, und die Gegner rücken auf. Auskunft sollte nichts kosten, Handlung schon. Technisch ein `if`, didaktisch die erste Fassung der Frage, die in Etappe 12 lautet: Welche Spieleraktion löst einen Tick aus?

**Der eigentliche Lernstoff steckt im Rundenzähler**, und er ist unscheinbar: Wo `runde = 1` steht, entscheidet, ob Welle 5 bei Runde 1 oder bei Runde 40 anfängt. Innerhalb der Wellenschleife heißt „pro Welle neu", außerhalb heißt „läuft durch". Beides läuft ohne Fehlermeldung. Nur eines ist das, was gemeint war.

> **Wo du eine Variable erzeugst, entscheidet darüber, wann sie neu gesetzt wird.**

Mehr als diese Beobachtung braucht es heute nicht. **Der Fachbegriff — Scope — kommt in Etappe 7a**, und zwar bewusst später: erst das Verhalten, dann der Name.

---

### 3c — Kampf und Anzeige

**Kampf ist absichtlich primitiv.** Ein Schuss trifft, macht festen Schaden, fertig. Keine Trefferchance, keine Panzerung, keine Kritischen. Kein Provisorium aus Faulheit, sondern Terminplanung: Die richtige Formel kommt in Etappe 21a.

**Die Gegnerzahl wächst mit der Wellennummer — nach einer Formel, die der Lernende selbst wählt.** Vorgegeben ist nur die Bedingung: Welle 1 hat mindestens einen Gegner, spätere haben mehr. Damit bekommt `range()` einen Zweck und wartet nicht bis Etappe 14.

**Nachladen kostet eine Runde**, in der die Gegner weiter Schaden machen — Nachschauen dagegen nicht. Erst durch diese Asymmetrie entsteht ohne eine Zeile neuen Python die erste echte Spielentscheidung: schießen oder nachladen?

⚠️ **Hier wird die Balancing-Falle zum ersten Mal akut.** Sobald das Spiel läuft, will man an den Zahlen drehen. Deckel: fünfzehn Minuten — und was sich falsch anfühlt, wird **notiert statt geändert**. Die Notizliste ist die Grundlage für Etappe 21a.

**Zur Darstellung, zehn Minuten ganz am Ende:** Der Befehl `status` zeigt Kernintegrität und Munition als Balken — `Kern [#######···] 70%`. Das ist Stringmultiplikation und eine Division. Der Rechenweg wird nicht vorgegeben, nur die drei Fragen dazu.

⚠️ **Die Stelle, an der hier fast jeder hängenbleibt, ist nicht die Rechnung, sondern ihr Zeitpunkt:** Wer die Balkenlänge einmal oben bei den Startwerten ausrechnet, bekommt einen Balken, der sich nie ändert — ohne Fehlermeldung. Die Rechnung gehört in den `status`-Befehl. Derselbe Gedanke trägt in Etappe 4 die Anmarschbahn: **Was aus Zustand entsteht, wird beim Anzeigen erzeugt, nicht aufbewahrt.**

**Nachladen schließt eine Schuld aus Etappe 2:** `nachladen_noetig` bekommt hier zum ersten Mal einen Wert — und die Beobachtung, dass zwei Variablen dasselbe aussagen können, wird als Vorgriff auf Etappe 18 notiert.

**3c endet mit einem Aufräumschritt:** Entwicklerbefehle raus, Debugzeilen raus, toter Code aus Etappe 2 raus. Das große Aufräumen — Funktionen — bleibt Etappe 7a.

**Der Nebeneffekt ist der eigentliche Gewinn:** Ein Balken, der bei 110 Prozent aus dem Rahmen läuft, zeigt Rechenfehler, die in einer Zahlenkolonne unsichtbar bleiben. **Und er soll das tun** — den Balken zu begrenzen ist ausdrücklich nicht die Aufgabe. Hier beginnt der Faden *Beobachtbarkeit*.

---

**Lernziele:**
- Wann `while`, wann `for`?
- Was ergibt `range(5)` genau — und `range(1, 21)`?
- Unterschied `break` ↔ `continue`?
- Wenn `break` in der inneren von zwei Schleifen steht — was genau wird beendet?
- Wie entsteht eine Endlosschleife — und wie kommst du raus?
- **Was passiert mit dem Rundenzähler, wenn er *innerhalb* statt außerhalb der Wellenschleife angelegt wird?** ← die wichtigste
- Was bewirkt `"#" * 7` — und warum funktioniert `"#" * 7.0` nicht?
- Warum wird jetzt `.lower()` gebraucht, obwohl Etappe 2 ohne auskam?

**Transferaufgabe (10 Min):** Zahlenraten mit „zu hoch"/„zu niedrig", mit Versuchszähler. Danach: alle geraden Zahlen von 0 bis 20 — einmal über die Schrittweite, einmal über eine Bedingung. Welche Variante liest sich besser?

**Kaputtmachen:** Entferne das `break` am Wellenende. Verschieb `input()` aus der inneren Schleife heraus. Setz den Rundenzähler an die andere Stelle. Rück eine Zeile um vier Leerzeichen aus der inneren in die äußere Schleife. Setz die Kernintegrität auf 150 und sieh dir den Balken an. **Die mittleren drei laufen ohne Fehlermeldung durch und tun das Falsche.**

**Commits:** `Etappe 3a: Die Wellenschleife läuft` · `Etappe 3b: Befehle und Runden` · `Etappe 3c: Der Vorposten hält`

---

## Etappe 4 — Ausrüstung und Beute

**Boot.dev:** Listen, `append()`, `remove()`, `len()`, Indexing

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Inventar, Gegnerliste, `.split()`, die Anmarschbahn | Warum `append()` nichts zurückgibt · zwei Namen, ein Objekt · Menge oder mehrere Dinge? | *mutable* · `dir()` und `help()` |

**Das Thema der Etappe in zwei Worten: Dinge statt Zahlen.** Die Gegner sind eine Anzahl — eine Anzahl hat keine Position, keinen Zustand, keine Reihenfolge. Die Beute wären Einzelvariablen, und beim vierten Fundstück müsste man wieder Code anfassen. Beides ist dasselbe Problem, und Listen sind die Antwort darauf.

**Was du baust:**
`inventar = []`. Befehle `nimm <ding>` und `inventar`. Maximal 10 Gegenstände.

Dazu `ablege <ding>` und eine zweite Liste mit dem, was nach einer Welle im Vorfeld liegt — ein Gegenstand wandert von der einen in die andere. Und `.split()`, damit Zwei-Wort-Befehle überhaupt möglich werden; in Etappe 5 trägt dasselbe Werkzeug `kaufe medkit`.

**Erste Fundstücke:** Schrott (deine Währung), ein Munitionskasten, eine verbeulte Panzerplatte, ein Datenkern der Brut, mit dem heute noch niemand etwas anfangen kann. Der Datenkern ist der Köder Richtung Etappe 15.

**⚠️ Und der wichtigste Riegel: Nicht alles wird eine Liste.** Munition bleibt eine Zahl. Vierzig Schuss als Liste aus vierzig gleichen Einträgen wäre technisch möglich und wäre falsch — man kann sie nicht unterscheiden, man tut nichts an einem einzelnen, und die einzige Frage lautet „wie viele noch?".

Die Frage dahinter — **Menge oder mehrere unterscheidbare Dinge?** — ist die erste Modellierungsfrage des Plans und die, um die es in Etappe 6 vollständig geht. Wer nach dieser Etappe alles zu Listen macht, hat Listen gelernt und Modellieren verlernt.

**Die zweite Liste ist wichtiger, als sie aussieht:** die Gegner der laufenden Welle. Sie kommen per `append()` dazu und verschwinden per `remove()`, wenn sie fallen. Damit stehst du sofort vor einem der berühmtesten Anfängerfehler: **eine Liste verändern, während man über sie läuft.** Probier es aus. Es stürzt nicht ab. Es überspringt einfach Gegner. Merk dir das Gefühl — in Etappe 12 kommt es als echtes Problem zurück.

**Zwei Design-Entscheidungen, beide mit Folgen:**

**1. Kennung oder Anzeigename?** Steht `"munitionskasten"` in der Liste oder `"Munitionskasten (halbvoll)"`? Die Kennung braucht eine zweite Stelle, an der steht, wie sie schön heißt — und die wird in Etappe 5 das Depot und in Etappe 25 eine JSON-Datei. Der Anzeigename spart das heute und kostet es in Etappe 11.

**2. Ist die Anmarschbahn der Zustand oder nur sein Bild?** ⭐ Das ist die wichtigere und die unauffälligere. Ein `"K"` an Stelle 7 *ist* der Gegner — oder jeder Gegner hat eine Zahl, und die Bahn wird daraus jedes Mal neu gebaut. Der zweite Weg ist etwas mehr Arbeit und der, den dieser Plan meint:

> **Ein Zustand und seine Darstellung sind zwei Dinge. Wer sie zu einem macht, kann sie später nicht trennen.**

Ein Gegner, der nur als Zeichen in einer Anzeigezeile existiert, hat nichts, was man in Etappe 12 ticken oder in Etappe 19 speichern könnte.

**Und hier wird dein Spiel zum ersten Mal sichtbar: die Anmarschbahn.**

Eine Liste fester Länge, ein Zeichen pro Feld — der Spawnpunkt links, dein Tor rechts, dazwischen die Gegner:

```
S..K...K....@
```

**Der Weg von der Zeichenliste zur Zeile wird nicht vorgegeben.** Es gibt eine eingebaute String-Methode, die genau das tut, und sie soll selbst gefunden werden — mit `dir("")` und `help()`. *Woher weiß ich, was dieses Objekt kann?* ist eine der Fähigkeiten, um die es im ganzen Projekt geht; in Etappe 27 stehen genau diese zwei Werkzeuge vor einem fremden Repo.

**Und der Riegel, der diese Etappe machbar hält: bau in drei Schritten, nicht in einem.**

1. **Ein** Gegner bewegt sich pro Runde ein Feld.
2. Mehrere Gegner aus einer Liste bewegen sich.
3. Getroffene Gegner verschwinden — und genau hier schnappt die Falle von oben zu.

Nach jedem Schritt ausführen. Wer alle drei auf einmal baut und dann einen Fehler hat, hat drei Verdächtige. Wer sie einzeln baut, weiß immer, welcher es war — der letzte. Das ist kein Anfängertrick, sondern das Suchverfahren, das in Etappe 8 **Halbieren statt Durchsuchen** heißt.

**Warum die Bahn mehr als Deko ist:** Der Fehler „eine Liste verändern, während man über sie läuft" ist in einer Textausgabe unsichtbar. Auf der Bahn ist er offensichtlich — ein Gegner steht plötzlich zwei Felder weiter, oder einer verschwindet, den niemand getroffen hat. Deine Darstellung ist ab heute ein Debugging-Werkzeug, und in Etappe 8 wird genau darauf zurückgegriffen.

**Die Etappe darf geteilt werden**, auch wenn sie offiziell nicht geteilt ist: Nach dem Inventar und dem Befehlsumbau steht ein sauberer Schnitt. Die Gegnerliste und die Anmarschbahn sind ein eigener Abend.

**Lernziele:**
- Warum ist der erste Index 0? Was hat das mit `range()` aus Etappe 3a zu tun?
- Was macht `liste[-1]`?
- Was passiert bei `liste[99]`, wenn die Liste 3 Einträge hat — und warum ist dieser Fehler ein *angenehmer*?
- **Was verändert `append()` — die Liste selbst, oder gibt es eine neue zurück?**
- Unterschied zwischen `b = a` und `b = a.copy()`?
- Warum überspringt eine Schleife Einträge, wenn man während des Durchlaufs entfernt?
- **Wie kommst du von „Gegner hat Position 4" zu „an Stelle 4 der Bahn steht ein `K`" — und warum sind das zwei getrennte Dinge?** ← die wichtigste
- Was liefert `"nimm".split()`, und was passiert beim Zugriff auf das zweite Element?
- **Warum ist Munition keine Liste geworden, das Inventar aber schon?**
- Was hat sich an `for` geändert seit Etappe 3 — und was nicht?

Die vorletzte Frage ist der Einstieg in **mutable vs. immutable** — Ursache vieler Bugs, die man nicht versteht:

```python
a = [1, 2]
b = a
b.append(3)
print(a)      # Was steht hier? Warum?

x = "hallo"
y = x
y += " welt"
print(x)      # Und hier? Warum anders?
```

Wenn du diese beiden Blöcke wirklich verstehst, hast du dir Wochen Fehlersuche gespart.

**Transferaufgabe (10 Min):** Liste mit drei Namen. Gib den zweiten aus, dann den letzten ohne `len()`. Häng einen an, entferne den ersten. Dann der eigentliche Punkt: Weis die Liste einer zweiten Variable zu, entferne über die zweite jemanden und gib die erste aus — erst die Vorhersage aufschreiben. Danach dasselbe mit `.copy()`. (Noch ohne Funktion; die kommt in Etappe 7a.)

**Kaputtmachen:** `remove()` mit etwas, das nicht drin ist. `inventar = inventar.append("medkit")` und schauen, was danach in `inventar` steht. Gegner mitten im Durchlauf entfernen, während die Bahn läuft — **der Typ-3-Fehler dieser Etappe, ohne jede Fehlermeldung.** Die Bahn zeichnen, *bevor* sich die Gegner bewegen statt danach: die erste Begegnung mit der Frage nach der Reihenfolge innerhalb einer Runde, aus der in Etappe 16 eine eigene Bug-Jagd wird. Und Munition testweise als Liste bauen — eine Struktur versteht man auch dadurch, dass man sie einmal am falschen Problem benutzt hat.

**Commit:** `Etappe 4: Ausrüstung, Beute und die Anmarschbahn`

---

## Etappe 5 — Der Vorposten und das Depot

**Boot.dev:** Dictionaries, verschachtelte Dictionaries, `keys()` / `values()` / `items()`

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Sektorenkarte, Bewegung, Depot, Kaufvorgang, Vorrat | Flach oder verschachtelt? · `.get()` gegen eckige Klammern · warum der Kauf keine Warennamen kennt | `.keys()` / `.values()` als eigene Objekte · warum Schlüssel unveränderlich sein müssen |

**Die Etappe ist groß und darf in der Mitte geteilt werden** — Karte und Depot am ersten Abend, Kaufvorgang und Vorrat am zweiten.

**Zuerst das Konzept, und zwar an etwas, das mit deinem Spiel nichts zu tun hat:**

```python
farben = {"rot": "#ff0000", "blau": "#0000ff"}
tage   = {"mo": "Montag", "di": "Dienstag"}
```

**Ein Dictionary ist eine Zuordnung: Schlüssel → Wert.** Nichts weiter. Es ist kein Inventar-Werkzeug und kein Shop-Werkzeug — es ist das Werkzeug für jede Frage der Form *„zu diesem Namen gehört welcher Wert?"*. Halt das eine Minute lang fest, bevor du weiterliest, denn gleich siehst du zwei Dictionaries voller Spielinhalt, und dann sieht es schnell so aus, als wären Preise und Räume das Thema.

**Was du baust:** Zwei Dictionaries, absichtlich unterschiedlich tief.

**Der Vorposten** — verschachtelt, weil jeder Sektor mehrere Eigenschaften hat:

```python
sektoren = {
    "nordtor": {
        "beschreibung": "...",
        "integritaet": 100,
        "nachbarn": {"sueden": "kern", "osten": "osttor"}
    },
}
```

Fünf bis sechs Sektoren: Nordtor, Osttor, Kern, Depot, Werkstatt, Landeplattform. Dazu `aktueller_sektor` als Zustandsvariable (wird in Etappe 9 zu `marine.sektor`).

**Das Depot** — flach, weil ein Preis nur eine Zahl ist:

```python
waren = {"medkit": 40, "munition": 15, "panzerplatte": 90}
```

Zwei Formen desselben Werkzeugs in einer Etappe. Das ist Absicht: Verschachtelung ist kein Qualitätsmerkmal, sondern eine Antwort auf eine Frage. *Wie viele Eigenschaften hat ein Eintrag?* Eine → flach. Mehrere → verschachtelt.

Dazu **Bewegung**: `umsehen` liest Beschreibung und Ausgänge aus den Daten, `gehe <richtung>` schlägt in `nachbarn` nach. Und `kaufe` funktioniert nur im Depot — der erste Befehl, der vom **Ort** abhängt statt nur von Werten.

Damit läuft ab heute die Wirtschaft: Gegner fallen → Schrott → `kaufe <ware>`. Der Kaufvorgang prüft drei Dinge (gibt es die Ware, reicht der Schrott, ist Platz im Inventar) und ist damit dein erstes Stück Logik, das mehr als eine Bedingung braucht. Die Mengenabfrage (*„wie viele?"*) löst dabei die `int()`-Schuld aus Etappe 1 ein.

**⭐ Und hier steckt der eigentliche Ertrag der Etappe, nicht bei den Dictionaries selbst:** In der Kauflogik darf **kein Warenname vorkommen**. Der Preis wird nachgeschlagen, nicht abgefragt. Eine vierte Ware ist dann eine Zeile in den Daten und keine Zeile im Code — und genau das ist die Prüfung, die im Selbsttest steht.

Das ist der Anfang des Fadens, aus dem Etappe 22 und 25 vollständig bestehen. Die Frage dazu lautet nicht „Dictionary oder `elif`?", sondern: **Ändert sich diese Liste? Dann sind es Daten.**

**Der Architekturtest dazu hat zwei Hälften, und die zweite ist die schärfere:** eine Ware hinzufügen *und eine löschen*. Hinzufügen kann auch klappen, wenn irgendwo noch ein fest verdrahteter Warenname steht — beim Löschen fällt er auf.

⭐ **Und die Einschränkung dazu ist wichtiger als der Satz selbst:** Eine neue Ware kommt nur dann ohne Logikänderung aus, wenn **alles in den Daten steht, was die Logik über sie fragt**. Sobald etwas fehlt — ob eine Ware stapelbar ist, zum Beispiel —, fällt der Code auf eine Fallunterscheidung zurück, und der Vorteil ist weg. Deshalb wird die Stapelbarkeit als zweite flache Tabelle hinterlegt, bevor der Kauf gebaut wird.

**Drei Wörter müssen dabei sauber getrennt bleiben:** das **Depot** ist der Katalog (Ware → Preis, kein Bestand), der **Vorrat** sind gezählte Ressourcen des Spielers (Name → Anzahl), das **Inventar** sind einzelne Gegenstände in einer Liste. Wer sie vermischt, vermischt sie den Rest des Projekts.

**Und drei kleinere Dinge, die hier zum ersten Mal auftauchen und weit tragen:** die Unterscheidung *Richtung ≠ Ziel ≠ Standort* (sonst landet `"osten"` in `aktueller_sektor`); der Kauf als **Transaktion** — erst alle Prüfungen, dann verändern; und die Frage nach **Invarianten**: Welche Bedingungen müssen bei den Sektordaten immer stimmen? Aufgeschrieben, nicht geprüft — der Prüfer kommt in Etappe 26.

**Zwei Einlösungen aus Etappe 4 kommen hier an.** Erstens die **Mengen**: Schrott und Munition wandern in ein `vorrat`-Dictionary (Name → Anzahl), Einzelstücke bleiben in der Liste — die Frage *Menge oder mehrere Dinge?* bekommt ihre zweite Struktur. Zweitens **Kennung oder Anzeigename**: Das Depot ist die zweite Stelle, von der in Etappe 4 die Rede war, und wer sich damals für Anzeigenamen entschieden hat, merkt hier zum ersten Mal, was das kostet.

**Zwei Design-Entscheidungen, die weit tragen:**

1. **Der versiegelte Sektor.** Die Landeplattform ist nicht erreichbar — der Osttunnel ist verschüttet. Fehlt der Eintrag in `nachbarn` einfach, oder existiert er und ist markiert? Ein sichtbar blockierter Weg ist ein Versprechen; ein fehlender Weg ist nichts. Davon hängt ab, ob das Freiräumen in Etappe 13 eine Zeile oder ein Umbau ist. **Empfohlen ist heute „fehlt einfach"** — das ist die kleinere Aufgabe. Wer „markiert" wählt, braucht dafür ein zweites flaches Dictionary im Sektor (Richtung → Grund), und `gehe` bekommt drei Fälle statt zwei. Den Nachbarwert selbst zu einem Dictionary auszubauen wäre eine dritte Verschachtelungsebene und ist hier ausdrücklich nicht gemeint.
2. **Ausverkaufte Ware.** Fliegt sie aus dem Dictionary, oder bleibt sie mit Bestand 0 drin? Auch das entscheidet, wie leicht Etappe 22 wird, wenn Waren Voraussetzungen und Ausbaustufen bekommen.

Beide Entscheidungen kommen in `GELERNT.md`.

**Zur Darstellung, zehn Minuten am Ende:** Ein grober Grundriss des Vorpostens als fester ASCII-Block, in dem der aktuelle Sektor markiert ist. Der Grundriss selbst darf handgezeichnet und statisch sein — nur die Markierung kommt aus `aktueller_sektor`. Widersteh der Versuchung, ihn aus den Daten zu erzeugen; das wäre eine hübsche Übung und hat mit Dictionaries nichts zu tun.

**Warum das zählt:** Erster Moment, in dem *Daten* und *Code* auseinanderfallen. Eine neue Ware kostet dich eine Zeile und keinen Gedanken an die Kauflogik. Merk dir das Gefühl — es kommt in Etappe 25 in voller Größe zurück.

**Lernziele:**
- Warum ist ein Dictionary hier besser als eine Liste?
- Wie kommst du an einen verschachtelten Wert?
- Was passiert bei einem Schlüssel, den es nicht gibt — und was macht `.get()` anders?
- **Was prüft `"medkit" in waren` — Schlüssel oder Wert?** (Stolperstein, über den fast jeder einmal fällt.)
- Was bekommst du beim Iterieren über ein Dictionary?
- Warum ist das eine Dictionary verschachtelt und das andere nicht?
- **Warum kommt in deiner Kauflogik kein einziger Warenname vor — und was wäre der Preis dafür, wenn doch?** ← die wichtigste
- Warum ist Schrott jetzt ein Dictionary-Eintrag und ein Medkit weiterhin ein Listeneintrag?
- Was wird verglichen und was angezeigt — und warum sollten das nicht dieselben Wörter sein?
- Was ist ein *inkonsistenter Datenfehler* (ein Nachbar zeigt ins Leere), und warum findet ihn kein Blick in die Bewegungslogik?

**Transferaufgabe (15 Min):** Dictionary mit drei Waren und Preisen. Frag einen Namen per `input()` ab und gib den Preis aus — und reagier sauber, wenn es die Ware nicht gibt. Probier beide Wege: eckige Klammern und `.get()`. (Noch ohne Funktion; die kommt in Etappe 7.)

**Kaputtmachen:** Mach aus `nachbarn` eine Liste. Lösch einen Sektor, auf den ein Nachbar zeigt. Schreib beim Kaufen `schrott - preis` statt `schrott -= preis` und kauf dreimal hintereinander dasselbe — **der Typ-3-Fehler dieser Etappe: unendlich Geld ohne jede Meldung.** Verschreib dich beim Zuweisen eines Schlüssels und sieh nach, wo der Wert gelandet ist. Und lösch einen Eintrag, während du über das Dictionary läufst: Python knallt hier, wo es bei einer Liste in Etappe 4 still das Falsche tat.

**Commit:** `Etappe 5: Vorposten, Depot und Wirtschaft`

---

## Etappe 6 — Liste, Dictionary, Set, Tuple

**Boot.dev:** Sets, Tuples, Mengenoperationen

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| `KLASSEN` als Tuple · Freischaltungen als Set · **Gegnertypen und die zweite Gegnerliste** · Bestiarium | Warum ein Set eine Regel *ist* statt sie zu prüfen · **warum zwei parallele Listen unangenehm sind** · die vier Fragen der Strukturwahl | Mengenoperationen (`-`, `&`) · warum `in` beim Set schneller ist |

**Was du baust:**
Keine neue Funktion — eine bessere Wahl der Werkzeuge.

```python
KLASSEN = ("soldat", "heavy", "engineer", "medic")   # Tuple: unveränderlich
freigeschaltet = {"panzerbrecher", "schnellladen"}    # Set: keine Duplikate
```

**Das Set ist hier keine Optimierung, sondern eine Spielregel.** Eine Fähigkeit zweimal zu kaufen darf nicht gehen. Mit einer Liste musst du das prüfen. Mit einem Set ist es strukturell unmöglich — die Datenstruktur *ist* die Regel. Das ist der Unterschied zwischen „ich habe es abgefangen" und „es kann nicht passieren", und er wird dich dein Programmiererleben lang begleiten.

---

**⭐ Und hier führt der Plan die Gegnertypen ein. Das ist die eigentliche Neuerung dieser Etappe.**

Bis Etappe 5 ist ein Gegner eine Positionszahl, und alle sehen gleich aus — `gegner = [7, 4, 2]`, drei Zeichen `K` auf der Bahn. Ab heute hat jeder einen **Typ**: Kriecher, Speier, Panzerbrut. Die Typen selbst stehen in einem verschachtelten Dictionary mit je einem langen und einem kurzen Beschreibungstext.

**Und jetzt der Teil, der bewusst unbequem ist.** Der Typ bekommt keine eigene Klasse und kein Tuple — er bekommt eine **zweite Liste neben der ersten**:

```
gegner       = [7, 4, 2]
gegner_typen = ["kriecher", "kriecher", "speier"]
```

Zwei Listen, über den **Index** verbunden. Der Gegner an Stelle 1 steht auf Feld 4 und ist ein Kriecher.

**Warum das so und nicht besser:**

Beim Anlegen ist es harmlos. Beim **Entfernen** wird es unangenehm — ein gefallener Gegner muss aus beiden Listen an derselben Stelle verschwinden, und `remove()` nach Wert trägt nicht mehr, weil zwei Gegner denselben Typ haben können. Der Lernende muss über den **Index** entfernen und dabei aufpassen, dass die Listen synchron bleiben.

> **Zwei Sammlungen, die immer gleich lang sein müssen, sind eine Sammlung, die noch nicht gebaut wurde.**

**Das ist absichtliches technisches Schuldenmachen mit festem Rückzahlungstermin.** In Etappe 11 kollabieren beide Listen zu einer Liste von Objekten, und der Schmerz endet. Wer ihn nicht erlebt hat, hält Objekte dort für Zeremonie. Wer ihn erlebt hat, versteht sie in der ersten Minute.

*(Deshalb steht im Guide auch ausdrücklich: nicht heute schon Objekte bauen, nicht heute schon ein Tuple aus Typ und Position basteln. Beides wäre eine Konstruktion, die in fünf Etappen wieder abgerissen wird.)*

**Der sichtbare Gewinn:** Die Anmarschbahn zeigt zum ersten Mal verschiedene Zeichen — `S..k...S....@`. Damit liest die Darstellung erstmals aus zwei Quellen, und die Zuordnung Typ → Zeichen ist dieselbe, die in Etappe 14a im Raster und in Etappe 29 bei den Kacheln wieder auftaucht.

**Welche Typen in welcher Welle vorkommen, entscheidet eine `if`/`elif`-Kette über die Wellennummer.** Sie ist hässlich und heute genau richtig — in Etappe 17a ersetzt der Budget-Generator sie.

---

**Dazu ein zweites Set: `gesehene_gegnertypen`.** Der Befehl `bestiarium` zeigt, was dir bisher begegnet ist — und damit auch, wie viel du noch nicht kennst. Die erste Begegnung mit einem Typ bekommt den langen Text, jede spätere den kurzen.

**Das ist die erste Sache im Programm, die sich etwas über Wellen hinweg merkt.** Bisher beschreibt jede Variable den aktuellen Zustand; das Bestiarium beschreibt die Geschichte des Spielers. Und es ist der Lehrbuchfall für ein Set: keine Reihenfolge, keine Duplikate, eine einzige Frage — *war der schon mal da?*

`bestiarium` kostet **keine Runde** — Anwendung der Unterscheidung aus 3b zwischen Auskunft und Handlung.

**Das Tuple bleibt heute bei `KLASSEN`, und das hat einen Grund.** Die übliche Tuple-Begründung lautet „gut für Koordinaten" — nur hat dein Spiel noch keine, und über etwas zu reden, das man nicht braucht, erzeugt keine Einsicht, sondern eine offene Frage. `KLASSEN` dagegen hat sofort Nutzen: Damit unterscheidet dein Programm „das ist keine Klasse" von „diese Klasse hast du nicht gewählt". Und es ist eine Liste, die sich nie ändern darf — genau dafür ist ein Tuple da.

**Mengenoperationen, und zwar mit Zweck:**

```python
# fremdes Beispiel
kann_a = {"lesen", "schreiben"}
kann_b = {"lesen", "rechnen"}
kann_a - kann_b      # was nur A kann
kann_a & kann_b      # was beide können
```

Bei dir: Welche Fähigkeiten fehlen dir noch für eine bestimmte Freischaltung? Das ist eine Differenzmenge und keine Schleife.

**Die Etappe endet mit einer Entscheidungshilfe** — vier Fragen in dieser Reihenfolge, und die Struktur steht fest:

> **1. Schlage ich etwas unter einem Namen nach?** → Dictionary
> **2. Sollen Duplikate unmöglich sein und die Reihenfolge egal?** → Set
> **3. Soll sich das nach dem Anlegen nicht mehr ändern?** → Tuple
> **4. Sonst** → Liste

Damit werden auch die drei Fragen beantwortet, die Etappe 5 offen gelassen hat: *Ist es schon enthalten? Darf es doppelt vorkommen? Ist die Reihenfolge Teil der Bedeutung?*

**Das `in`-Experiment — mach es wirklich:**

```python
"medkit" in meine_liste    # sucht im Inhalt
"medkit" in mein_set       # sucht im Inhalt, aber viel schneller
"medkit" in mein_dict      # sucht im SCHLÜSSEL, nicht im Wert
```

Dreimal dasselbe Wort, dreimal etwas anderes.

**Lernziele:**
- Wann Set statt Liste? (Zwei Gründe: Duplikate und Geschwindigkeit bei `in`.)
- Warum kann ein Set keine Listen enthalten, aber Tuples schon?
- Was ist an einem Tuple unveränderlich?
- Wofür eignet sich ein Tuple besser als eine Liste — und woran erkennst du solche Fälle? *(Koordinaten werden ab Etappe 14 das schönste Beispiel dafür sein. Heute brauchst du sie noch nicht.)*
- Was ist der Unterschied zwischen „ich prüfe, ob es schon drin ist" und „es kann nicht doppelt drin sein"?

**Transferaufgabe (10 Min):** Zwei Listen mit Ausrüstungsteilen. Finde ohne Schleife heraus, welche in beiden vorkommen. (Eine Zeile, wenn du das richtige Werkzeug wählst.)

**Kaputtmachen:** Leg eine Liste in ein Set. Ändere ein Tuple. Schreib `(5)` und `(5,)` und lass dir mit `type()` sagen, was das jeweils ist. **Und der wichtigste Versuch: Entfern einen gefallenen Gegner nur aus `gegner` und vergiss `gegner_typen`.** Spiel danach eine Welle. Das läuft ohne Fehlermeldung, bis die Listen so weit auseinanderlaufen, dass ein Index ins Leere greift — ein Typ-2-Fehler, der genau dann kommt, wenn man ihn am wenigsten erwartet.

**Commit:** `Etappe 6: Die richtige Datenstruktur`

---

## Etappe 7 — Aufräumen

**Boot.dev:** Funktionen, Parameter, Rückgabewerte, Scope

**Geteilt, und diesmal aus einem inhaltlichen Grund.** 7a ist eine Programmieretappe: Du lernst Funktionen und baust dein Spiel um. 7b ist eine Denketappe: Du trennst zwei Dinge voneinander, die bisher vermischt waren. Beides an einem Abend geht — beides an einem Abend *ankommen* nicht.

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **7a** | Funktionen, Parameter, `return`, Standardargument | Scope · warum sieben Parameter ein Signal sind | `global` — und warum du es nicht nimmst |
| **7b** | Zeichenfunktionen, die nur ausgeben | `return` statt `print` in der Logik | `assert` als Behauptung über einen Zustand |

**Ein Wort zu `assert`, weil es sonst falsch ankommt:** Es steht heute auf Stufe *erkennen*. Du sollst nicht anfangen zu testen — Tests sind Etappe 26. Du sollst drei Zeilen geschrieben und einmal knallen gesehen haben. Mehr wird daraus heute nicht.

---

### 7a — Funktionen

**Was du baust:**
Nichts Neues. Du zerlegst die unübersichtliche Datei: `zeige_status()`, `wechsle_sektor()`, `kaufe()`, `berechne_schaden()`, `verarbeite_befehl()`.

**Warum das zählt:** Refactoring — funktionierenden Code umbauen, ohne sein Verhalten zu ändern. Ungefähr die Hälfte dessen, was Entwickler den ganzen Tag tun. Beim ersten Mal fühlt es sich falsch an („es lief doch!").

**Prüfung:** Nach dem Umbau muss sich das Spiel *exakt* wie vorher verhalten. Schreib vorher auf, was bei Welle 3 mit fünf Schüssen passiert. Nachher muss dasselbe passieren. Das ist ein Charakterisierungstest, und in Etappe 26 wird `pytest` daraus.

**Der Schmerz, den du hier fühlen sollst:** Deine Funktionen brauchen ständig dieselben sechs Werte. `berechne_schaden(waffe, ziel, panzerung, klasse, boni, munition)` — und du reichst sie durch drei Ebenen. Das ist unangenehm, und es ist Absicht. In Etappe 9 verschwindet dieser Schmerz, und dann verstehst du, wozu `self` da ist. Wer diesen Schmerz nicht hatte, hält Klassen für Zeremonie.

**Die Abkürzung, die du nicht nimmst:** `global`. Sie funktioniert, sie ist zwei Zeichen kürzer, und sie deckt genau das Problem zu, das Etappe 9 löst. Wenn du in Versuchung kommst, frag mich — ich erkläre dir, warum sie hier falsch ist.

**Ein Standardargument nimmst du mit:** `def zeige_status(marine, ausfuehrlich=False)`. Damit erweiterst du eine Funktion, ohne einen einzigen bestehenden Aufruf anzufassen — das häufigste Muster für rückwärtskompatible Änderungen überhaupt.

**Und der Umbau bekommt einen Beweis, keine Hoffnung.** Bevor irgendetwas angefasst wird: eine Befehlsfolge von fünfzehn bis zwanzig Zeilen aufschreiben, die das Spiel gründlich durchgeht — **gerade die Fälle, die schiefgehen, gehören dazu**. Einmal durchspielen, Ausgabe in eine Datei. Umbauen. Dieselbe Folge nochmal, Ausgaben vergleichen.

```bash
python spiel.py < befehle.txt > vorher.txt
# ... umbauen ...
python spiel.py < befehle.txt > nachher.txt
diff vorher.txt nachher.txt
```

Das heißt **Charakterisierungstest**: Man friert das aktuelle Verhalten ein, um es beim Umbau nicht zu verlieren. Es ist gängige Praxis und der direkte Vorläufer von Etappe 26 — dort wird dasselbe zu `pytest`, nur automatisch.

**Dazu die Regel, die Refactoring erträglich macht:** in kleinen Schritten. Eine Funktion herauslösen, ausführen, prüfen. Nicht fünf auf einmal — sonst suchst du hinterher.

⚠️ **Und eine Gegenwarnung, damit die Etappe nicht ins Gegenteil kippt:** *Mehr Funktionen sind nicht besser.* Eine Funktion, die einmal aufgerufen wird und drei Zeilen hat, macht den Code nicht klarer, sondern verteilt ihn. Die Prüffrage lautet nicht „kann man das auslagern?", sondern **„hat dieses Stück einen Namen, den ich aussprechen kann?"**

**Commit dazwischen:** `Etappe 7a: Refactoring in Funktionen`

---

### 7b — Die Trennung

**Heute schreibst du fast keinen neuen Code. Du ziehst eine Linie.**

Auf der einen Seite steht alles, was *rechnet und entscheidet*. Auf der anderen alles, was *ausgibt*. Bisher lagen beide Sorten durcheinander in denselben Funktionen, und das war völlig in Ordnung — bis heute.

**Die Darstellung wird zur eigenen Schicht.** Was seit Etappe 1 gewachsen ist — Kopf, Balken, Anmarschbahn, Grundriss — wandert in Funktionen, die nur zeichnen: `zeichne_bahn(gegner)`, `zeichne_balken(wert, maximum)`. Sie rechnen nichts und entscheiden nichts. Sie bekommen fertige Werte und geben Zeichen aus.

Das ist die wichtigste Trennung dieser Etappe, und sie ist dieselbe wie die nächste:

**Eine Entscheidung mit langer Wirkung:** Deine Logikfunktionen geben Werte **zurück**, sie geben nicht selbst aus. `berechne_schaden()` liefert eine Zahl, keine Zeile Text. Das fühlt sich heute umständlich an. In Etappe 28 ist es der Unterschied zwischen „Pygame draufsetzen" und „alles neu schreiben".

**Lernziele:**
- Unterschied `return` ↔ `print`?
- Was ist ein Standardargument, und warum ist es rückwärtskompatibel?
- Was ist Scope — warum kennt eine Funktion deine äußeren Variablen nicht?
- Was passiert, wenn eine Funktion kein `return` hat?
- Unterschied Parameter ↔ Argument?
- Warum ist eine Funktion mit sieben Parametern ein Signal und kein Erfolg?

**Transferaufgabe (10 Min):** Funktion `berechne_trinkgeld(betrag, prozent)`. Danach die entscheidende Frage — noch ohne Testframework: **Was muss immer gelten?** Nie negativ? Bei 0 Prozent genau der Betrag? Schreib drei Fälle auf und prüf sie von Hand. Das ist Testdenken, lange bevor du `pytest` anfasst.

*(Bewusst außerhalb des Spiels: `berechne_schaden()` ist ab heute dein Produktivcode, keine Übung mehr.)*

👀 **Und dann schreibst du deine Antworten hin — als Code.** Nicht als Kommentar:

```python
assert trinkgeld >= 0
```

**Eine Assertion ist eine Behauptung über einen Zustand, von der dein Programm sagt: das muss wahr sein, sonst stimmt etwas nicht.** Stimmt sie, passiert nichts. Stimmt sie nicht, knallt es sofort — an der Stelle, wo die Annahme gebrochen wurde, und nicht drei Funktionen später, wo das falsche Ergebnis auffällt. Damit verwandelst du einen Fehler vom Typ 3 in einen vom Typ 1, und das ist fast immer ein guter Tausch.

**Drei Zeilen, mehr nicht — und dann ist das Thema für heute erledigt.** Du fängst jetzt nicht an zu testen. Du hast einmal gesehen, dass man eine Annahme hinschreiben kann und dass sie knallt, wenn sie bricht. Beim Lesen fremden Codes hast du ab jetzt eine Frage, die fast alles über eine Funktion verrät: **Welche Annahmen macht sie eigentlich — und prüft sie eine davon?** Alles Weitere wartet bis Etappe 26.

**Kaputtmachen:** Ändere eine Variable in einer Funktion und lies sie draußen aus. Bau ein `return` in eine Funktion ein, das mitten in einer Schleife steht.

**Commit:** `Etappe 7b: Logik und Darstellung getrennt`

---

## Etappe 8 — Bug-Jagd I ⭐

**Kein neues Boot.dev-Thema. Eine eigenständige Fähigkeit.**

**Was du baust:**
Kein Spielfeature, sondern zwei Dokumente: dein eigenes **Debugging-Protokoll** und ein **Fehlertagebuch** mit der wichtigsten Zeile — *wie gefunden*, nicht *was war*.

Davor die Werkzeuge, in dieser Reihenfolge: die drei Fehlertypen als Denkraster, Tracebacks von unten nach oben lesen, Ursache von Symptom trennen, Halbieren statt Durchsuchen, `print()` mit Präfix und `!r`, und der **Debugger** — Breakpoints, Step Over/Into/Out, Variablen-Ansicht, bedingte Breakpoints. Dazu `git diff` als Suchraum-Verkleinerer.

**Warum bedingte Breakpoints hier besonders zahlen:** Dein Spiel läuft zwanzig Wellen mit hunderten Runden. „Halt an, wenn `welle == 7` und `gegner.hp < 0`" ist der Unterschied zwischen zwei Minuten und einer halben Stunde.

Erst wenn die Werkzeuge sitzen, kommt die Jagd: Der Mentor gibt manipulierten Code zurück, ohne zu sagen wie viele Fehler und wo. Ab hier läuft sie unregelmäßig weiter. **Ohne Mentor** funktioniert die Zeitversatz-Variante: zehn Sabotagen aufschreiben, zwei Tage warten, drei davon blind anwenden.

**Warum das zählt:** Debugging wird in fast keinem Kurs unterrichtet, ist aber die Fähigkeit, die bei fremdem Code als einzige trägt. Und Typ 3 zerstört die schädlichste Anfängerüberzeugung: *„Wenn Python keinen Fehler zeigt, ist mein Programm richtig."*

**Wichtige Abgrenzung:** Debugging ist nicht Fehlerbehandlung. Das eine heißt herausfinden, *warum* sich das Programm falsch verhält; das andere kommt in Etappe 20.

**Lernziele:**
- Die drei Fehlertypen — und warum Typ 3 der gefährlichste ist?
- In welcher Richtung liest man einen Traceback, und welche Zeile sagt was?
- Warum ist die Absturzstelle selten die Fehlerstelle?
- Wann Debugger, wann `print()`?
- Welche vier Angaben gehören in eine gute Fehlerbeschreibung?
- Warum ist „ich habe etwas geändert und jetzt geht es" ein schlechtes Ergebnis?

**Transferaufgabe (10–15 Min):** Ein fremdes Programm mit einem Typ-3-Fehler — eine Funktion verändert die übergebene Liste, obwohl ihr Docstring das nicht ankündigt. Mit dem Debugger finden, erklären, reparieren. Verbindet mutable Objekte aus Etappe 4 mit „Abhängigkeiten sichtbar machen" aus Etappe 7.

**Kaputtmachen:** Acht Trainingsbugs, selbst eingebaut — einer je Fehlertyp, dazu der fast richtige Vergleich (`>=` statt `>` beim Wellenende), das vergessene `return` in `berechne_schaden()`, der Fehler in den *Daten* statt im Code (ein Nachbar-Sektor, den es nicht gibt), und zwei Fehler gleichzeitig.

**Die Fehlertypen bekommen hier ihre zweite Benennung.** Neben den Typen 1/2/3 dieses Plans (die sagen, *wann* ein Fehler auffällt) stehen die klassischen Begriffe, die überall sonst benutzt werden und sagen, *was* schiefgeht: **Syntaxfehler** (Python kann den Code nicht lesen), **Laufzeitfehler** (stößt beim Ausführen auf etwas Unmögliches), **logischer Fehler** (läuft, Ergebnis falsch). Ein Syntaxfehler ist immer Typ 1, ein logischer Fehler immer Typ 3, ein Laufzeitfehler kann beides sein. Beide Einteilungen werden gebraucht: die klassische, um fremde Erklärungen zu lesen, die eigene, um die Gefährlichkeit einzuschätzen.

**Und ein eigener Abschnitt: den Fehler beschreiben.** Vier Zeilen — *was ich wollte · was passiert · was ich ausgeschlossen habe · was ich vermute*. Der Nutzen liegt in der dritten: Beim Schreiben merkt man, dass man noch nichts ausgeschlossen hat, und prüft es, statt zu fragen. Der Name dafür ist **Rubber-Duck-Debugging**; ein erschreckender Anteil aller Fehler löst sich während der Beschreibung. In Etappe 3 wird die Form schon einmal kurz vorgestellt.

**Commit:** `Etappe 8: Bug-Jagd bestanden`

Damit ist Block 1 abgeschlossen.

---

# BLOCK 2 — Einheiten und Zeit

*Boot.dev: „Learn Object Oriented Programming in Python"*
*Ab hier kommen Leseübungen dazu.*

## Etappe 9 — Alles wird zum Objekt

**Boot.dev:** Klassen, `__init__`, Methoden, Attribute

**Die erste OOP-Etappe, und deshalb geteilt.** `self` ist der Begriff, an dem die meisten Anfänger zum ersten Mal wirklich hängenbleiben — nicht weil er schwer ist, sondern weil er überall steht. Der bekommt 9a für sich allein.

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **9a** | `Marine` und `Gegner` als Klassen, Methoden statt Funktionen mit sieben Parametern | Was `self` ist · Klasse gegen Objekt | — |
| **9b** | `__repr__` | Warum das dein Debugging verändert | `__str__` und wann es statt `__repr__` läuft |

---

### 9a — Klassen

**Was du baust:**
Klasse `Marine` mit `name`, `hp`, `panzerung`, `schaden`, `sektor`, `munition`. Deine losen Variablen wandern hinein — und die siebenstellige Parameterliste aus Etappe 7 schrumpft auf `self`.

Dazu `Gegner` mit `hp`, `schaden`, `entfernung`. Zwei Klassen, nicht eine — weil du in Etappe 11 die Frage stellen wirst, was sie gemeinsam haben.

**Commit dazwischen:** `Etappe 9a: Alles wird zum Objekt`

---

### 9b — Objekte, die sich zeigen

**Eine Methode nimmst du sofort mit, weil sie jede spätere Fehlersuche erleichtert:**

```python
def __repr__(self):
    return f"Marine(name={self.name!r}, hp={self.hp}, sektor={self.sektor!r})"
```

Ohne sie zeigt `print(marine)` etwas wie `<__main__.Marine object at 0x7f3a...>` — die nutzloseste Ausgabe der Sprache. Mit ihr siehst du im Debugger aus Etappe 8 sofort, was im Objekt steckt. Und ab Etappe 12, wenn zwanzig Gegner gleichzeitig existieren, ist eine lesbare Liste von Objekten kein Komfort mehr, sondern Voraussetzung.

Merk dir das Muster: **Methoden mit doppelten Unterstrichen sind Haken, an denen Python selbst zieht.** `__init__` beim Erzeugen, `__repr__` beim Anzeigen. Mehr davon in Etappe 11.

👀 **Nur erkennen — es gibt zwei Darstellungen, nicht eine:**

| | Gedacht für | Ausgelöst durch |
|---|---|---|
| `__repr__` | dich, beim Debuggen — eindeutig und vollständig | `repr(x)`, die Konsole, Listenausgabe |
| `__str__` | den Spieler — lesbar und kurz | `str(x)`, `print(x)`, `f"{x}"` |

**Schreib heute nur `__repr__`.** Ohne `__str__` springt Python darauf zurück, deshalb reicht eines von beiden vollkommen. Der Kasten steht hier aus einem einzigen Grund: Wenn du in fremdem Code auf `f"{einheit}"` triffst, sollst du nicht rätseln, woher der Text kommt. Er kommt aus einer dieser beiden Methoden, und welche es ist, steht in der Klasse — nicht in der f-String-Zeile. Ein Satz, den du sagen kannst, reicht. Eine zweite Implementierung brauchst du nicht.

**Leseübung, Stufe 1 der Leseleiter — und eine neue Frage dazu:** Ab heute gehört zu jeder Leseübung *Woher kommt dieser Name?* Steht er in dieser Datei, kommt er aus einem `import`, oder hängt er an `self`? Drei völlig verschiedene Herkünfte, die beim Lesen gleich aussehen. Wer sie nicht trennt, hält jeden unbekannten Namen für Magie — und genau das ist der Zustand, aus dem dieses Projekt dich herausholen soll. Module baust du erst in Etappe 24; erkennen musst du sie ab jetzt.

**Lernziele:**
- Was ist `self` — und warum steht es überall?
- Wer ruft `__repr__` auf, und warum rufst *du* es nie selbst?
- Unterschied Klasse ↔ Objekt?
- Wann wird `__init__` aufgerufen?
- Unterschied Attribut ↔ lokale Variable in einer Methode?
- Was hat sich an deinen Funktionen aus Etappe 7 geändert, und was nicht?
- Wann läuft `__str__`, wann `__repr__` — und was passiert, wenn nur eines davon existiert?
- Woran erkennst du beim Lesen, ob ein Name aus dieser Datei, aus einem Import oder von `self` kommt?

**Leseübung (5 Min):** Ich gebe dir etwas in dieser Form:

```python
einheit = Rekrut("Vasquez")

if einheit.moral > 5:
    einheit.melde("Position gehalten.")
else:
    einheit.melde("Ich brauche Ablösung.")
```

Du schreibst nichts. Du beantwortest: Was ist `einheit`? Woher kommt `moral`? Was macht der Punkt? Wann läuft `melde()`? Was passiert, wenn `moral` genau 5 ist?

**Kaputtmachen:** Lass `self` bei einer Methode weg. Setz `self.munition` nicht in `__init__` und greif später darauf zu.

**Commit:** `Etappe 9b: Objekte zeigen, was in ihnen steckt`

---

## Etappe 10 — Komposition

**Boot.dev:** Objekte in Objekten, Komposition

**Was du baust:**
Nicht Vererbung — **Komposition.** Ein Marine *hat* Dinge:

```python
class Marine:
    def __init__(self, name):
        self.name = name
        self.inventar = Inventar()
        self.ausruestung = Ausruestung()
        self.position = (0, 0)
```

`Ausruestung` verwaltet die Slots: `{"waffe": None, "panzerung": None, "modul": None}`

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| `Inventar` und `Ausruestung` als eigene Klassen, ein Marine besitzt sie | `None` gegen `0` · zwei Namen können auf **ein** Objekt zeigen | `is` gegen `==` |

**Und der eigentliche Kern dieser Etappe steht in der mittleren Spalte, nicht in der linken: Zwei Variablen können auf dasselbe Objekt zeigen.**

Du hast das in Etappe 4 schon einmal gesehen, damals an einer Liste:

```python
a = [1, 2]
b = a          # kein zweiter Behälter — ein zweiter Name für denselben
b.append(3)    # a hat sich jetzt auch geändert
```

Heute ist es dasselbe, nur mit deinen eigenen Objekten. Und die Frage lautet:

> **Haben zwei Marines jeweils ein eigenes Inventar — oder teilen sie sich eines?**

Die Antwort hängt daran, **wo** `Inventar()` steht. Steht es in `__init__`, bekommt jeder Marine bei seiner Erzeugung ein frisches. Steht es an einer Stelle, die nur einmal ausgeführt wird, teilen sich alle dasselbe — und dann heilt ein Medkit, das der eine wegnimmt, plötzlich beim anderen nicht mehr.

**Das ist die Ursache des berühmtesten Stolpersteins der Sprache**, dem du unten beim Kaputtmachen begegnest. Und es ist die Sorte Fehler, die nicht abstürzt: Zwei Marines mit demselben Rucksack sind ein völlig funktionsfähiges Programm. Nur eben nicht deines.

**Der Reflex, den du daraus mitnimmst:** Wenn sich zwei Dinge unerklärlich gemeinsam verändern, frag nicht *„wo wird das falsch gesetzt?"*, sondern **„sind das überhaupt zwei Dinge?"**

**Hier lernst du `None` richtig.** `None` heißt „hier ist bewusst nichts" — etwas völlig anderes als `0`, `""` oder `False`. Leerer Slot, kein aktuelles Ziel, kein laufender Bauauftrag: alles `None`. Und der Unterschied ist in diesem Spiel besonders scharf: `munition = 0` heißt „Waffe da, leer". `waffe = None` heißt „keine Waffe". Wer beides gleich behandelt, baut sich einen Fehler vom Typ 3.

Und `if waffe is None:` — nicht `== None`. Kein Stil, echter Unterschied; frag mich danach.

**Warum Komposition vor Vererbung:** Die meisten Einführungen stürzen sich auf Vererbung, weil sie sich spektakulär anfühlt. In echtem Python ist Komposition häufiger, einfacher zu debuggen, flexibler. Wenn du nur eins von beiden wirklich beherrschst, sollte es dieses sein.

**Lernziele:**
- Unterschied „ist ein" ↔ „hat ein"?
- Warum `is None` statt `== None`?
- Was passiert, wenn zwei Marines versehentlich dasselbe `Inventar`-Objekt teilen?
- Wann ist `0` die richtige Antwort und wann `None`?

**Transferaufgabe (15 Min):** Klasse `Rucksack` mit Kapazität und `hinzufuegen()`, die `True`/`False` zurückgibt. Klasse `Wanderer`, die einen Rucksack besitzt.

**Kaputtmachen:** Gib `Inventar()` als Standardwert in die Parameterliste (`def __init__(self, inv=Inventar())`). Erzeug zwei Marines. Beobachte. Einer der berühmtesten Python-Stolpersteine — und du verstehst ihn nur, wenn Etappe 4 saß.

**Commit:** `Etappe 10: Komposition`

---

## Etappe 11 — Vererbung — und die Frage, ob wir sie brauchen

**Boot.dev:** Vererbung, `super()`, Methoden überschreiben

**Diese Etappe ist voll, deshalb vorab die Gewichtung:**

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Die Hierarchien, `super()`, `faehigkeit_einsetzen()` überschreiben | Wann Vererbung passt und wann nicht — schriftlich beantwortet | `__len__`, `__contains__`, `__iter__`, `@property` |

**Die dritte Spalte ist ausdrücklich keine Aufgabe.** Keine Implementierung, keine Transferübung, keine Prüfung außer einer einzigen Verständnisfrage. Du sollst nicht lernen, `__iter__` zu schreiben — du sollst beim Lesen fremden Codes wissen, *warum* dort `for x in trupp:` steht, obwohl `trupp` keine Liste ist. Ein Satz dazu, und die Spalte ist erledigt.

Wer daraus eine Übung macht, verbringt drei Abende mit Dunder-Methoden und einen mit Vererbung — und genau andersherum wäre richtig.

**⭐ Und hier wird die Schuld aus Etappe 6 zurückgezahlt.** Seit dort trägt der Lernende zwei parallele Listen mit sich herum:

```
gegner       = [7, 4, 2]
gegner_typen = ["kriecher", "kriecher", "speier"]
```

Zwei Sammlungen, die über den Index zusammenhängen, immer gleich lang sein müssen und beim Entfernen doppelte Sorgfalt verlangen. **Heute kollabieren sie zu einer:**

```
gegner = [Gegner("kriecher", 7), Gegner("kriecher", 4), Gegner("speier", 2)]
```

Ein Eintrag, eine Sache. Kein Index-Abgleich mehr, kein Synchronhalten, kein „ich habe vergessen, es aus der zweiten Liste zu löschen".

**Das ist der stärkste Moment, den diese Etappe zu bieten hat, und er funktioniert nur, weil der Schmerz echt war.** Der Guide soll ausdrücklich darauf zurückkommen: erst die alten zwei Listen zeigen, dann die neue eine, dann die Frage, welche der beiden Fehlermöglichkeiten aus Etappe 6 jetzt gar nicht mehr existieren kann.

Es gilt weiter die Migrationsregel: **Die Liste bleibt — nur was ein Eintrag bedeutet, wird reicher.** Schleifen, `len()` und die Bewegungslogik funktionieren unverändert.

**Was du baust:**
- `Einheit` → `Marine`, `Rekrut`, `Geschuetz`, `Gegner` — alles, was Trefferpunkte hat und Schaden nehmen kann
- `Marine` → `Soldat`, `Heavy`, `Engineer`, `Medic`
- `Item` → `Waffe`, `Panzerung`, `Modul`, `Verbrauchsgut`

Hier stirbt die `if`/`elif`-Kette aus Etappe 2. Die Klassenwerte stehen nicht mehr in einer Verzweigung, sondern in der jeweiligen Klasse. Und jede Klasse überschreibt `faehigkeit_einsetzen()` — der Medic heilt, der Engineer baut, der Heavy feuert eine Salve.

**Die zweite Aufgabe ist die wichtigere:**

> Zehn Minuten, schriftlich: *Brauchen wir hier Vererbung überhaupt?*

Und in diesem Setting hat die Frage besonders scharfe Zähne. Deine vier Marine-Klassen unterscheiden sich vor allem durch **Zahlen**. Zahlen sind Daten. Man könnte sie in ein Dictionary schreiben und hätte vier Zeilen statt vier Klassen — genau das machst du in Etappe 22 mit den Bauplänen.

Also: Wo liegt die Grenze? Wann ist ein Unterschied ein Datensatz und wann eine Klasse? Es gibt keine richtige Antwort, die ich dir vorsagen könnte. Aber die Frage zu stellen ist der Unterschied zwischen jemandem, der Syntax kann, und jemandem, der Entscheidungen trifft.

*(Mein Hinweis, wenn du feststeckst: Schau nicht auf die Werte, schau auf das Verhalten. Ein Unterschied, der nur in `schaden` steckt, sieht nach Daten aus. Ein Unterschied, bei dem `faehigkeit_einsetzen()` grundverschiedene Dinge tut, sieht nach Klassen aus.)*

**Und eine dritte Möglichkeit, die ich hier nur benenne und nicht erkläre:** Unterschiedliches Verhalten *zwingt* nicht zu Vererbung. Man kann einem Marine auch ein Fähigkeitsobjekt mitgeben — `Marine + Heilen + Zielstrategie „Schwächster"`, zusammengesetzt statt abgeleitet. Das heißt **Komposition**, du hast es in Etappe 10 bereits gebaut, ohne dass es so genannt wurde, und es ist in echtem Python häufiger als Vererbung.

**Trotzdem baust du heute die Hierarchie.** Nicht weil sie richtiger ist, sondern weil du Vererbung einmal von innen erlebt haben musst, um in Etappe 22 begründet gegen sie entscheiden zu können. Eine Entscheidung gegen ein Werkzeug, das man nie benutzt hat, ist keine Entscheidung, sondern eine Vermeidung.

Die eigentliche Lektion dieser Etappe lautet deshalb nicht *„unterschiedliches Verhalten → Vererbung"*, sondern: **Vererbung ist eine von mehreren Modellierungsentscheidungen — nicht die automatische Folge davon, dass Objekte sich unterschiedlich verhalten.**

**Schreib deine Antwort in `GELERNT.md` — als Entscheidung mit Datum und Begründung, nicht als Notiz.** Du liest sie in Etappe 22 wieder, wenn Baupläne zeigen, wie gut sich Verhalten als Daten ausdrücken lässt, und noch einmal in Etappe 25, wenn du versuchst, deine Klassen nach JSON zu bringen. Dann bewertest du dieselbe Frage mit zwei Monaten Erfahrung neu.

Dieser Ablauf — **Entscheidung → Erfahrung → Gegenprobe → Revision** — ist der Kern dessen, was Softwareentwicklung von Syntaxkenntnis unterscheidet. Er funktioniert nur, wenn die ursprüngliche Entscheidung aufgeschrieben ist. Aus dem Gedächtnis rekonstruiert man immer die Entscheidung, die man heute treffen würde.

**Und hier wird der Trupp zum ersten Mal sichtbar.** Bis gestern waren drei deiner vier Klassen Werte in einer Verzweigung, die nie zur Anwendung kamen. Heute sind sie vier Objekte in einer Liste — alle vier existieren, alle vier haben `faehigkeit_einsetzen()`, und du kannst sie ausgeben und vergleichen. Ohne den Trupp wäre Vererbung hier eine Behauptung; mit ihm ist sie eine Beobachtung.

**Die Gegenfrage dazu, weil sie sich aufdrängt:** Wenn alle vier gleichzeitig da sind — wozu dann noch die Klassenwahl? Antwort: Sie bestimmt, wer auf deinen Befehl hört. Die anderen drei tun ab Etappe 12, was ihre `update()`-Methode sagt.

👀 **Dritter Teil — Lesestoff, keine Übung.** Die weiteren Haken, an denen Python zieht. Einmal ansehen, einen Satz dazu sagen können, weitergehen:

```python
class Trupp:
    def __len__(self):           # was passiert bei len(trupp)
    def __contains__(self, x):   # was passiert bei "vasquez" in trupp
    def __iter__(self):          # was passiert bei "for e in trupp"
```

Damit liest sich dein Trupp plötzlich wie eine eingebaute Datenstruktur.

Dazu `@property` — eine Methode, die sich wie ein Attribut liest:

```python
@property
def am_leben(self):
    return self.hp > 0

# Aufruf: gegner.am_leben   (ohne Klammern!)
```

**Warum das hier steht:** Wenn du in fremdem Code `for x in obj:` liest und dich fragst, wo diese Schleife herkommt — das hier ist die Antwort. Es ist eine Dunder-Methode der Klasse.

**Lernziele:**
- Was macht `super().__init__()` genau?
- Woran erkennst du beim Lesen, dass ein Objekt iterierbar ist?
- Warum steht bei `@property` beim Aufruf keine Klammer?
- Was passiert, wenn du sie vergisst — und warum ist `if gegner.am_leben:` ohne Klammern *immer* wahr, wenn du sie falsch schreibst?
- Was heißt „Methode überschreiben"?
- Wann ist Vererbung die falsche Wahl?

**Transferaufgabe (15 Min):** `Fahrzeug` → `Auto`, `Fahrrad`, jeweils mit `beschreibe()` und `super()`.

**Kaputtmachen:** Lass `super().__init__()` weg. Lies den `AttributeError` und überleg, was er dir eigentlich sagt. Danach: Schreib `if gegner.am_leben():` mit Klammern und dann `if gegner.am_leben:` ohne — bei einer der beiden Varianten ist einer davon ein stiller Typ-3-Fehler.

**Commit:** `Etappe 11: Einheiten- und Item-Hierarchie`

---

## Etappe 12 — DER TICK ⭐

**Boot.dev:** Objekte in Schleifen, Zustand über Zeit

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| `Welt.tick()`, `update()` an jeder Einheit, dümmste Trupp-KI | Gesteuert gegen autonom · warum man Listen nicht beim Durchlaufen verändert | Tick-Reihenfolge · der Begriff *Zustandsautomat* |

```python
class Welt:
    def tick(self):
        self.zeit += 1
        for einheit in self.einheiten:
            einheit.update(self)
```

**Warum diese Etappe in diesem Setting der Angelpunkt ist:** Ein RPG kann ohne Tick existieren — dann ist es eben statisch. Dein Spiel kann das nicht. Ohne Tick rücken keine Gegner vor, laufen keine Abklingzeiten ab, baut sich kein Geschütz, kommt kein Rekrut nach. Der Tick ist hier nicht ein Feature, sondern der Motor.

Ein Tick läuft bei jedem Spielerbefehl. Und in ihm passiert alles gleichzeitig: Gegner nähern sich, Geschütze feuern, Verbände heilen, Zähler zählen.

💡 **Nur merken — der Tick hat eine Reihenfolge, und die ist eine Entscheidung.**

Dein Computer tut nichts gleichzeitig. Er arbeitet eine Reihenfolge ab: erst die Zähler, dann die Einheiten, dann das Aufräumen — oder eben anders herum. **Du musst heute keine perfekte Reihenfolge entwerfen.** Schreib nur auf, welche du gebaut hast, und leg sie in `GELERNT.md`.

Der Grund steht in Etappe 16: Dort schreibst du einen Tick von Hand mit und stellst fest, dass ein Gegner, der sich vor dem Feuern bewegt, ein Feld weiter vorne stirbt. Nichts davon stürzt ab. Wenn du dann nachschlagen kannst, welche Reihenfolge du gewählt hattest, ist der Fehler in zehn Minuten gefunden. Wenn nicht, in zwei Stunden.

**Der Fehler, der hier fast garantiert passiert** — und du kennst ihn seit Etappe 4: Ein Gegner fällt *während* du über die Gegnerliste läufst. Jetzt ist es kein Übungsfall mehr, sondern dein Spiel. Sammle, was entfernt werden soll, und entferne es danach.

**Und hier fängt die Trupp-KI an — in ihrer allerdümmsten Form.**

Die drei nicht gesteuerten Marines bekommen `update()` wie jede andere Einheit. Sie tun genau eine Sache: *Wenn ein Gegner in Reichweite ist, feuere.* Kein Laufen, keine Zielwahl, keine Fähigkeiten. Bewegen können sie sich erst ab Etappe 14, weil es davor keine Positionen gibt, auf denen man laufen könnte.

**Warum das hier fast nichts kostet und viel bringt:** Du schreibst keine neue Mechanik, sondern gibst einer bestehenden Klasse eine `update()`-Methode. Der Tick läuft ohnehin über alle Einheiten. Was du dafür bekommst, ist der Begriff, um den es in dieser Etappe eigentlich geht:

> **Eine gesteuerte Einheit wartet auf einen Befehl. Eine autonome Einheit entscheidet im Tick selbst.**

Dein Marine und die drei anderen sind derselbe Typ, unterscheiden sich aber genau in diesem einen Punkt. Wenn du das an vier fast identischen Objekten siehst, hast du verstanden, wofür der Tick da ist — besser als jede Erklärung es könnte.

**🚨 KI-Code-Warnsignal — nur bemerken, nichts reparieren:** `def update(self, welt)` — deine Einheiten bekommen die ganze Welt übergeben, nur um ein Ziel zu finden. Das ist bequem, und es hat einen Namen: **Kopplung**. Für dein Spiel ist es heute völlig richtig so. Merk dir nur die Frage — *muss dieses Ding wirklich alles kennen?* — denn in fremdem Code ist sie eine der nützlichsten, die du stellen kannst.

**Erweiterung:** Einheiten merken sich, wo sie waren. „Rekrut Vasquez hat das Nordtor zwei Wellen lang allein gehalten." Billig zu bauen, große Wirkung. Grundlage für Etappe 17.

**Lernziele:**
- Warum bekommt `update()` die Welt übergeben?
- Was ist ein Zustandsautomat — und wo steckt einer in deinem Gegner? *(Ein Satz reicht.)*
- Was passiert, wenn du beim Iterieren über `self.einheiten` eine Einheit entfernst?
- Warum tickt die Welt und nicht jede Einheit für sich?
- Was passiert, wenn zwei Systeme im selben Tick auf dieselbe Einheit zugreifen — und in welcher Reihenfolge laufen sie eigentlich?

**Leseübung, Stufe 2 (10 Min):** Ab hier wird der fremde Code länger — 15 bis 30 Zeilen, eine Schleife über Objekte, die dabei Zustand verändert. Du beantwortest die fünf Fragen und zusätzlich diese: *Wie sieht die Liste nach dem dritten Durchlauf aus?* Nicht ausführen. Auf Papier verfolgen. Genau das ist die Fähigkeit, die dir in Etappe 16 bei den Reihenfolgefehlern das Leben rettet.

**Transferaufgabe (10 Min, alternativ):** Klasse `Uhr` mit `tick()`, die Minuten zählt und bei 60 auf die nächste Stunde springt.

**Kaputtmachen:** Ruf `tick()` zweimal pro Befehl auf. Dann gar nicht. Dann nur, wenn der Befehl gültig war — und schau, ob du dir damit unendlich Zeit erkaufen kannst, indem du Unsinn eingibst. Das ist ein Typ-3-Fehler, der wie eine Spielmechanik aussieht.

**Commit:** `Etappe 12: Der Vorposten tickt`

---

## Etappe 13 — Bauzeit und Nachschub ⭐

**Boot.dev:** Objektzustand über Zeit, Weltzustand zur Laufzeit ändern

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Bauzeit, Nachschubzähler, Räumzeit — dreimal dasselbe Muster | Zustand gegen Ereignis: *soll das gelten oder soll das passieren?* | Der Begriff *Scheduler* |

**Das ist eine kleine, freundliche Etappe** — ein Zähler, ein `if`, und ein Spielmoment, den du nicht mehr vergisst. Genau deshalb steht sie direkt hinter dem Tick.

```python
class Geschuetz:
    def update(self, welt):
        self.alter += 1
        if self.alter >= self.bauzeit and not self.aktiv:
            self.aktiv = True
            welt.melde(f"{self.name} ist online.")
```

Du gibst den Bauauftrag, gehst zum anderen Tor, kämpfst — und irgendwann feuert hinter dir etwas, das vorher nicht da war. Der einfachste mögliche Beweis, dass dein Tick-System funktioniert.

**Drei Systeme, ein Muster.** Das ist der eigentliche Lernstoff dieser Etappe:

| System | Zähler läuft | Am Ende passiert |
|---|---|---|
| Geschütz im Bau | `bauzeit` | Es wird aktiv |
| Gefallener Rekrut | `nachschubzaehler` | Ein neuer steht da |
| Verschütteter Osttunnel | `raeumzeit` | Der Sektor wird erreichbar |
| **Ausgefallener Trupp-Marine** | `ausfallzeit` | Er steht wieder auf |

Viermal derselbe Ablauf mit anderen Namen. Wenn du das siehst, hast du den wichtigsten Reflex dieser Etappe: **Wiederholung im Muster ist ein Hinweis, kein Zufall.** Ob du daraus schon eine gemeinsame Basisklasse machst oder erst später, ist deine Entscheidung — aber du sollst sie bewusst treffen.

💡 **Nur merken:** Man könnte das auch anders bauen — die Welt führt eine Liste von Terminen (*„bei Tick 148: MG-Turm aktivieren"*), statt dass jedes Objekt seinen eigenen Zähler mitschleppt. Das heißt **Scheduler**, es ist in großen Simulationen oft die bessere Struktur, und für dein Spiel ist der Zähler im Objekt momentan einfacher. Mehr musst du dazu heute nicht wissen — nur, dass es beide Bauarten gibt, damit du die andere in fremdem Code nicht für einen Fehler hältst.

Und das Dritte in der Tabelle ist besonders: `welt.raeume_frei("osttunnel")` ändert dein `sektoren`-Dictionary **zur Laufzeit**. Deine Karte aus Etappe 5 war statische Daten. Jetzt ist sie lebendiger Zustand. Und hier zahlt die Design-Entscheidung von damals: Wenn du den blockierten Weg markiert hast, ist das eine Zeile. Wenn er fehlte, ist es ein Umbau.

**Und jetzt der Begriff, der aus dieser Etappe hängen bleiben soll: Zustand ist nicht Ereignis.**

```
aktiv = True                    ← Zustand.   Gilt, solange er gilt. Beliebig oft abfragbar.
"Geschütz wurde gerade fertig"  ← Ereignis.  Passiert genau einmal, in genau einem Tick.
```

Der Unterschied klingt nach Wortklauberei und ist der Grund, warum die `not self.aktiv`-Prüfung im Beispiel oben dasteht. Ohne sie meldet dein Geschütz bei *jedem* Tick, dass es fertig geworden ist — der Zustand ist ja weiterhin wahr. Ein Ereignis entsteht erst am **Übergang** von einem Zustand in den nächsten, und wenn du diesen Übergang nicht festhältst, ist er nach einem Tick weg.

Das ist keine Spielerei mit Begriffen. Alles, was später einmalig auf etwas reagieren soll, hängt daran: eine Meldung, ein Eintrag im Protokoll, ein Ton, eine Animation, ein freigeschalteter Bauplan, ein Speicherpunkt. In Etappe 28 wird daraus die Frage, wann du etwas zeichnest und wann du etwas *aufblitzen* lässt.

**Deine Prüffrage ab heute:** Soll das gelten, oder soll das passieren?

**⚠️ Hier ist ein Umweg ausdrücklich erwünscht:**

Irgendwann wirst du fragen: *Warum muss das Geschütz eigentlich die ganze Welt kennen, nur um ein Ziel zu finden?* Ausgezeichnete Frage, sie hat einen Namen (**Kopplung**), und sie steht nicht im Lehrplan.

**Stell sie trotzdem.** Ab hier lernst du nicht mehr Python, um eine Übungsaufgabe zu lösen — du lernst Python, weil *dein* Programm ein Problem hat. Das ist die stärkste Form des Lernens, die dieses Projekt zu bieten hat.

**Zur Zeitrechnung — Tick oder Echtzeit?**

- **Tick-Zeit** — wächst pro Spieleraktion. Passt zum Textspiel: Kaffee kochen ändert nichts.
- **Echtzeit** (`time.time()`) — wächst, während du weg bist.

**Empfehlung: jetzt Tick-Zeit.** Nicht als Kompromiss — in Etappe 28 läuft die Loop mit 60 Bildern pro Sekunde. Dann *ist* ein Tick eine Zeiteinheit, und `bauzeit = 180` sind exakt drei Sekunden. Ohne eine Zeile neue Bau-Logik. *(Und wenn dich Echtzeit wirklich reizt: dafür gibt es die `advanced/`-Reihe. Nicht jetzt.)*

**Lernziele:**
- Was spricht dafür, dass das Objekt selbst zählt — und was dafür, dass die Welt eine Liste von Terminen führt?
- Was ist der Unterschied zwischen „ist fertig" und „wurde gerade fertig" — und warum brauchst du beides?
- Warum darf `update()` nur einmal pro Tick laufen?

**Kaputtmachen:** Lass die `not self.aktiv`-Prüfung weg und schau, was ein fertiges Geschütz bei jedem weiteren Tick meldet. Setz `bauzeit = 0`.

**Commit:** `Etappe 13: Das erste Geschütz`

---

## Etappe 14 — Das Vorfeld ⭐

**Boot.dev:** Verschachtelte Listen, 2D-Raster, `range()` über Koordinaten

**Die am stärksten geteilte Etappe des Plans — und sie war vorher die überladenste.** 14a ist reine Python-Arbeit an einer Datenstruktur. 14b baut darauf Spielmechanik. Wer beides mischt, lernt weder das eine noch das andere.

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **14a** | Das Raster, `vorfeld[y][x]`, Gegnerbewegung, Randprüfung | Warum hier ein Raster passt und bei den Sektoren ein Dictionary | `enumerate()` |
| **14b** | Reichweite als Set von Feldern, Sensorabdeckung, Trupp-Bewegung | Warum ein Set und keine Liste | — |

**Wenn dir 14b zu viel wird: lass die Sensorabdeckung weg.** Sie ist Spielmechanik, kein Python-Lernziel, und sie kann jederzeit nachkommen. Die Reichweite dagegen brauchst du in Etappe 21.

---

### 14a — Das Raster

```python
vorfeld = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", ".", ".", "@", "#"],
    ["#", "S", "#", "#", "#"],
]
```

**Hier wird die Schuld aus Etappe 4 eingelöst.** Deine Anmarschbahn war eine Zeile. Heute wird sie ein Feld. Der einzige wirklich neue Gedanke ist die zweite Ebene — eine Liste, deren Elemente selbst Listen sind, und ein zweiter Index. Das Zeichnen kannst du längst; du machst es jetzt in einer Schleife statt einmal.

Das Gelände vor dem Tor: Wände, offene Felder, der Spawnpunkt der Brut (`S`), dein Tor (`@`). Positionen als Tuple `(x, y)` — und jetzt ist auch klar, wofür das Tuple aus Etappe 6 gut war. Gegner bewegen sich Feld für Feld auf dein Tor zu.

**Der Star dieser Portion ist eine einzige Zeile:**

```python
vorfeld[y][x]
```

Erst die Zeile, dann die Spalte. Das verwechselt jeder mindestens einmal, und deshalb steht es hier so groß.

**Hier zahlt `range()` aus Etappe 3:**

```python
for y in range(len(vorfeld)):
    for x in range(len(vorfeld[y])):
```

**Dazu die Randprüfung:** Liegt `(x, y)` überhaupt auf dem Raster? Ein Gegner, der bei `x = -1` landet, greift in Python auf das *letzte* Element zu, statt abzustürzen — einer der schönsten Typ-3-Fehler der Sprache, und du kannst ihn heute selbst herbeiführen.

**⚠️ Der wichtigste Riegel dieser Etappe: Heute gibt es keine Wegfindung.** Kein A\*, kein Dijkstra, keine Breitensuche. Deine Gegner gehen den direkten Weg — ein Schritt in x, ein Schritt in y, und wenn eine Wand im Weg steht, gilt eine simple Regel (an ihr entlang, oder gar nicht erst Wände dorthin bauen).

Der Reflex „Wände plus Bewegung, also brauche ich jetzt A\*" ist verständlich und die teuerste Abzweigung in diesem ganzen Plan. Wegfindung ist ein schönes Thema, es ist Informatik statt Python, und es kostet dich zwei Wochen an einer Stelle, an der du gerade verschachtelte Listen lernen wolltest. **Notier es in `GELERNT.md` als Idee für nach Etappe 27.** Dann gehört das Spiel dir, und dann ist es ein wunderbares Wochenendprojekt.

**Warum ein Raster und nicht ein Dictionary wie bei den Sektoren?**

Diese Frage gehört zu jeder Design-Entscheidung, und hier ist sie besonders lehrreich, weil dieselbe Welt beide Strukturen enthält:

| | Sektoren (Etappe 5) | Vorfeld (heute) |
|---|---|---|
| Wie viele? | Eine Handvoll | Hunderte Felder |
| Wie benannt? | `"nordtor"` — jedes hat Charakter | `(4, 2)` — reine Adresse |
| Was macht man damit? | Nachschlagen, was dort ist | Rechnen: Abstände, Wege, Reichweiten |
| Passende Struktur | Dictionary | Raster |

**Die Regel dahinter:** Wenige benannte Dinge mit Eigenschaften → Dictionary. Viele gleichartige Zellen, auf denen gerechnet wird → Raster. Wer das Vorfeld als Dictionary baut, kann keinen Abstand ausrechnen, ohne die Schlüssel zu zerlegen. Wer die Sektoren als Raster baut, hat ein Feld namens `(0,3)`, dem man nicht ansieht, dass es das Depot ist. **Zu wissen, wann welche Struktur passt, trennt Anfänger von Fortgeschrittenen** — und du hast jetzt beide im selben Programm und kannst sie vergleichen.

👀 **Nur erkennen: `enumerate()`.** Wenn du Index *und* Wert brauchst, ist das die übliche Form — `for y, zeile in enumerate(vorfeld):`. Beim 2D-Raster ist `range(len(...))` völlig in Ordnung, und du musst heute nichts umschreiben. Sag dir nur zu jeder dieser drei Zeilen einen Satz, was in den Schleifenvariablen steht:

```python
for zeile in vorfeld:                    # ?
for y, zeile in enumerate(vorfeld):      # ?
for name, wert in daten.items():         # ?
```

Diese drei Formen machen einen erheblichen Teil aller Schleifen aus, die dir je in fremdem Python begegnen — und wer sie verwechselt, liest ein Programm falsch, ohne es zu merken. Zwei Minuten, kein Umbau.

**Der spätere Zahltag:** Genau dieses Raster ist das Format, in dem Pygame Tilemaps zeichnet. Dein Vorfeld wird in Etappe 29 zur ersten grafischen Karte — ohne Umbau.

**Transferaufgabe (15 Min):** 3×3-Raster aus Zahlen. Berechne die Summe einer Zeile, dann die einer Spalte.

**Kaputtmachen:** Vertausch `x` und `y`. Erzeug das Raster mit `[["."] * 5] * 5` und ändere ein Feld — das hängt direkt mit Etappe 4 und 10 zusammen und ist derselbe Gedanke: ein Objekt, viele Namen. Lass die Randprüfung weg und schick einen Gegner auf `x = -1`.

**Commit dazwischen:** `Etappe 14a: Das Vorfeld ist ein Raster`

---

### 14b — Was auf dem Raster passiert

Jetzt wird das Raster benutzt.

**Reichweite.** Geschütze stehen auf Feldern und decken einen Bereich ab. Welche Felder deckt ein Geschütz auf `(2, 3)` mit Reichweite 2 ab? Das ist eine Doppelschleife über Koordinaten, ein Abstandsvergleich und am Ende ein **Set von Tuples**.

Hier zahlt Etappe 6 zum ersten Mal richtig: Ein Feld kann nicht zweimal abgedeckt sein, und die Frage „liegt dieser Gegner im Feuerbereich?" ist ein `in` auf einem Set. Mit einer Liste müsstest du prüfen, ob schon etwas doppelt drinsteht. Mit einem Set kann es nicht passieren.

**Und jetzt lernt der Trupp laufen.**

Die drei autonomen Marines bekommen zwei Regeln, mehr nicht:

1. Such den **nächsten** Gegner. Das ist ein Durchlauf über die Gegnerliste mit einem Abstandsvergleich und einem gemerkten Minimum — der klassischste aller Suchalgorithmen, und du schreibst ihn heute zum ersten Mal.
2. Geh ein Feld auf ihn zu, solange du außer Reichweite bist. Aber **verlasse deine Zone nicht.**

Die Zone ist der Punkt, an dem das eine Spielmechanik wird statt einer Spielerei: Jeder Marine hat einen Bereich, den er hält. Damit rennt dir nicht der ganze Trupp hinter einem einzelnen Krabbler her, während am anderen Tor die Wand fällt.

Technisch ist die Zone dieselbe Randprüfung wie die des Rasters, nur mit anderen Grenzen. Du schreibst dieselbe Art Bedingung zweimal an einem Tag und siehst dabei, dass „liegt das noch drauf?" und „darf der da hin?" dieselbe Form haben.

**Warum die Trupp-KI genau hier und nicht früher:** Vorher gab es keine Positionen. „Geh zum nächsten Gegner" setzt voraus, dass es ein *nächster* sein kann — und das setzt Abstände voraus, also Koordinaten.

**Und die Bremse dazu:** Mehr als diese zwei Regeln bekommt die KI heute nicht. Kein Ausweichen, kein Zurückziehen, kein Fokusfeuer, keine Absprache. Das sind reizvolle Probleme, sie kosten alle einen Abend, und keines davon lehrt dich Python. Notier sie in `GELERNT.md` als Ideen und geh weiter.

**Optional — die Sensorabdeckung.** Du siehst nicht das ganze Vorfeld, sondern nur, was in Reichweite deiner Sensoren liegt oder schon einmal lag. `erkundete_felder` ist ein zweites Set von Koordinaten und wächst, während du dich bewegst und Geschütze baust. Der Rest wird als `?` gezeichnet. Zwei Zeilen Aufwand, große Wirkung — aber ausdrücklich Kür. Wenn 14b sich zieht, kommt das später.

*Die Design-Entscheidung dazu, falls du es baust:* Was heißt „erkundet"? Einmal gesehen und für immer bekannt, oder nur solange ein Sensor hinschaut? Das erste ist ein wachsendes Set, das zweite ein bei jedem Tick neu berechnetes. Beides ist vertretbar — aber nur das erste musst du speichern, und das merkst du in Etappe 19.

**Lernziele:**
- Bei `vorfeld[y][x]` — welcher Index ist Zeile, welcher Spalte? Warum verwechselt das jeder mindestens einmal?
- Wie prüfst du, ob eine Koordinate überhaupt auf dem Raster liegt?
- Warum ist ein Set für abgedeckte Felder besser als eine Liste?
- Warum kann ein Tuple ein Set-Element sein, eine Liste aber nicht?
- Was steht bei den drei Schleifenformen jeweils in den Schleifenvariablen?
- Wann passt ein Raster, wann ein Dictionary?

**Kaputtmachen:** Setz die Reichweitenprüfung auf `<=` statt `<` und schau, ob ein Gegner ein Feld zu früh beschossen wird. Das läuft durch, und es ist genau die Sorte Fehler, die dich in Etappe 16 beschäftigen wird.

**Commit:** `Etappe 14b: Reichweite und Bewegung`

---

## Etappe 15 — Was die Brut hinterlässt

**Boot.dev:** Suchen in Datenstrukturen, Zustandsverwaltung

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Fundstücke, `erkenntnisse` als Set, Wirkung auf Depot und Kampf | Ein Ereignis verändert den Spielzustand **dauerhaft** | Der Begriff *Kopplung* |

**Das Muster dieser Etappe in vier Zeilen** — und es ist eines der nützlichsten, die es in Python überhaupt gibt:

```python
erkenntnisse = set()
erkenntnisse.add("chitinprobe")

if "chitinprobe" in erkenntnisse:
    ...
```

Etwas passiert einmal. Es wird gemerkt. Es wird später abgefragt. Damit hat dein Spiel zum ersten Mal ein Gedächtnis, das über eine Welle hinausreicht.

Gefallene Gegner hinterlassen mehr als Schrott: Chitinproben, einen halb geschmolzenen Datenkern, Sporen, die auf etwas hindeuten, das noch nicht gekommen ist. Jeder Fund setzt ein Flag in `erkenntnisse`.

**Und Erkenntnisse tun etwas.** Wer die Chitinprobe analysiert hat, sieht in der Gegnerübersicht den Schwachpunkt und macht mehr Schaden. Wer den Datenkern hat, bekommt im Depot eine Ware angeboten, die vorher nicht im Sortiment war. Wer die Sporen gefunden hat, weiß, welcher Typ in Welle 12 kommt — und kann vorbauen.

**Erste echte Verzahnung** von Ort, Gegenstand, Wirtschaft und Kampf. Deine Systeme reden miteinander, und das ist der Moment, in dem aus vier Bausteinen ein Spiel wird.

**Erweitern ohne zu zerstören:** Füge einen vierten Fund hinzu, **ohne** die Depot-Logik oder die Schadensberechnung anzufassen. Wenn das nicht geht, ist das eine Erkenntnis über deinen Code — nicht über dein Können. Und es ist genau die Erkenntnis, die Etappe 22 vorbereitet.

**Und jetzt fünf Minuten mit einem Blatt Papier: Wer muss von wem wissen?**

Heute treffen zum ersten Mal vier Systeme aufeinander, die bisher nichts voneinander wussten — Fundstück, Erkenntnis, Depot, Kampf. Zeichne die Pfeile, mehr nicht:

```
Fundstück  →  Erkenntnis
Erkenntnis →  Depot?
Erkenntnis →  Schadensberechnung?
```

🚨 **Nur bemerken, nichts reparieren:** Wenn irgendwo eine Zeile wie `fundstueck.analysiere(welt.depot.spieler.einheiten[0])` entsteht, weiß diese Funktion sehr viel über andere Teile deines Spiels. Sie funktioniert. Sie ist nur schwer zu ändern, weil jede dieser Ebenen sie brechen kann.

Das ist alles, was du heute damit tun musst: es sehen. Der Begriff heißt **Kopplung**, sein Werkzeug kommt in Etappe 23. Heb die Zeichnung auf — dort machst du sie ein zweites Mal und vergleichst.

**Lernziele:**
- Wo speicherst du eine Erkenntnis — beim Fundstück, beim Gegnertyp, oder zentral? Was spricht wofür?
- Wie findest du in einer Liste von Objekten das erste, das eine Bedingung erfüllt?
- Warum ist „Erkenntnis vorhanden" ein Set und kein Dictionary aus Booleans?

**Leseübung (10 Min):** Ich zeige dir eine fremde Funktion, die eine Sammlung durchsucht und dabei stillschweigend annimmt, dass sie nie leer ist. Du sagst mir, unter welcher Bedingung sie abstürzt — ohne sie auszuführen.

**Commit:** `Etappe 15: Was die Brut hinterlässt`

---

## Etappe 16 — Bug-Jagd II

Gleiches Ritual, größeres System, subtilere Fehler: ein Geschütz, das ein Feld zu weit trifft; ein Nachschubzähler, der bei bestimmten Klassen doppelt läuft; eine Erkenntnis, die zu früh gesetzt wird; ein Objekt, das versehentlich geteilt wird.

**Der Fehlertyp, der in diesem Spiel neu ist:** Reihenfolgefehler im Tick. Wenn Gegner sich bewegen, *bevor* Geschütze feuern, sieht das Ergebnis anders aus als umgekehrt — und beides läuft ohne Fehlermeldung durch. Solche Bugs findest du nicht durch Lesen, sondern indem du einen Tick von Hand mitschreibst.

**Die Hauptübung dieser Etappe ist keine Fehlersuche, sondern eine Tabelle.**

Nimm einen einzigen Tick und schreib ihn von Hand mit. Nicht im Kopf — auf Papier oder in einer Datei, Phase für Phase, mit allen Einheiten nebeneinander:

| Phase | Gegner A | Gegner B | MG-Turm | Marine (KI) | Rekrut |
|---|---|---|---|---|---|
| Start | Feld 2, 10 HP | Feld 4, 8 HP | aktiv | Feld 1 | aktiv |
| Gegner bewegen sich | Feld 3 | Feld 5 | aktiv | Feld 1 | aktiv |
| Marines bewegen sich | Feld 3 | Feld 5 | aktiv | Feld 2 | aktiv |
| Es wird gefeuert | 10 → 0 | 8 → 4 | aktiv | Feld 2 | aktiv |
| Aufräumen | **tot** | Feld 5, 4 HP | aktiv | Feld 2 | aktiv |

Dann führ dasselbe mit deinem Programm aus und vergleich Zeile für Zeile. Das ist das Ritual aus dem Rahmenteil, angewendet auf das komplizierteste System, das du bisher hast.

**Und danach die eigentliche Frage:**

> Was wäre anders, wenn gefeuert wird, *bevor* sich die Gegner bewegen?

Probier es aus — vertausch zwei Zeilen in deinem Tick und lass dieselbe Welle laufen. Das Ergebnis ist anders, und **nichts davon stürzt ab**. Ein Gegner, der ein Feld zu weit vorne getroffen wird, ist ein Gegner, der ein Feld zu weit vorne stirbt, und ab Welle 12 entscheidet das darüber, ob dein Tor hält.

Damit hast du den vierten Fehlertyp aus dem Rahmenteil am eigenen Programm erlebt: **Reihenfolgefehler.** Es gibt keine richtige Reihenfolge, die ich dir nennen könnte — es gibt nur die, für die du dich entscheidest, und die dann überall gilt. Schreib sie in `GELERNT.md`.

**Und ab heute schreibst du jede Fehlersuche als drei Zeilen auf, bevor du eine Zeile Code änderst:**

```
Beobachtung:   Was siehst du? (kein Urteil, nur die Beobachtung)
Hypothese:     Was vermutest du als Ursache?
Experiment:    Was änderst du, um genau diese Vermutung zu prüfen — und nur diese?
```

Das dritte Wort ist das schwerste: **nur diese.** Wer drei Dinge gleichzeitig ändert und danach feststellt, dass es läuft, hat den Fehler nicht gefunden, sondern begraben. Zwei der drei Änderungen sind jetzt unbegründet im Code und warten.

**Merk dir das Formular. Es ist das, was du in Etappe 27 auf fremden Code anwendest** — dort in der Form: *„Ich verstehe diese Stelle nicht. Was vermute ich? Wie prüfe ich das?"* Das ist derselbe Vorgang, nur ohne die Erlaubnis, etwas zu ändern.

**Zusatzaufgabe:** Nimm einen der Fehler und schreib in `GELERNT.md`, *wie du vorgegangen bist* — nicht, was der Fehler war.

**Commit:** `Etappe 16: Bug-Jagd II — die Reihenfolge steht`

---

# BLOCK 3 — Der Vorposten reagiert

*Ab hier wird der Plan bewusst gröber, und der Ton wechselt.*

*Bis Etappe 16 hieß es: „Jetzt lernst du X." Ab hier heißt es: **„Hier ist ein Problem. Welche Lösung würdest du wählen?"** Das ist keine Nachlässigkeit, sondern der Übergang vom Programmierenlernen zur Softwareentwicklung — und der besteht genau darin, dass niemand mehr sagt, welche Datenstruktur die richtige ist.*

*Das Verfahren dafür steht ab jetzt bei jeder größeren Entscheidung: **Problem beschreiben → drei Modelle überlegen → Vor- und Nachteile → entscheiden → bauen → später neu bewerten.** Deine Entscheidungen kommen in `GELERNT.md`, weil du mehrere davon in Etappe 22 und 25 wieder auf den Tisch bekommst.*

*Und: Dein Spiel wird Fragen erzeugen, die heute niemand kennt. Die haben Vorrang.*

## Etappe 17 — Der Wellengenerator ⭐

**Boot.dev:** `random`, gewichtete Wahrscheinlichkeiten

**Geteilt.** 17a ist Zufall — ein handliches, sofort belohnendes Thema. 17b ist alles, was der Zufall nach sich zieht, und das ist mehr, als es aussieht.

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **17a** | `random`, ein Wellenbudget, erzeugte Wellen | Warum Budget besser steuert als Anzahl | Gewichtete Auswahl (`random.choices`) |
| **17b** | Seed als sichtbares Werkzeug, Ereignisse zwischen den Wellen | Zufall macht ein Programm untestbar — außer man fixiert ihn | — |

---

### 17a — Zufall

Bis heute waren deine Wellen von Hand geschrieben. Ab heute werden sie **erzeugt**.

**Fang mit dem Handwerkszeug an, in einer Wegwerf-Datei:**

```python
random.choice(liste)      # eines davon
random.randint(1, 6)      # eine Zahl dazwischen
random.random()           # eine Kommazahl zwischen 0 und 1
```

Fünf Minuten, dreimal laufen lassen, dreimal etwas anderes sehen. Dann ins Spiel.

**Die Gegnertypen gibt es seit Etappe 6 — hier bekommen sie Zahlen.** Zu den Beschreibungstexten kommen Kosten und optional ein Gewicht. Das ist ein Dateneintrag mehr pro Typ, keine neue Struktur.

**Jede Welle bekommt ein Budget**, das mit der Wellennummer wächst. Jeder Gegnertyp hat Kosten. Der Generator kauft ein, bis das Budget leer ist. Damit ist Welle 14 jedes Mal anders und trotzdem ungefähr gleich schwer.

**Und die `if`/`elif`-Kette aus Etappe 6 stirbt hier** — die, die festlegte, welche Typen in welcher Welle vorkommen. Sie war dort genau richtig und ist es ab jetzt nicht mehr. Der Guide soll den Vergleich zeigen: vorher eine Kette mit drei Zweigen, nachher eine Rechnung, die mit dreißig Typen genauso funktioniert.

**Der schwierige Teil ist nicht `random`, sondern das Wort davor.**

`random.choice(liste)` ist eine Zeile. Die eigentliche Aufgabe steht nirgends in der Dokumentation:

> Wie erzeugt man **kontrollierte** Unvorhersehbarkeit?

Deine Welle 14 soll jedes Mal anders sein — aber nicht mal spielbar und mal unmöglich. Sie soll überraschen — aber nicht unfair sein.

Deshalb das Budget. Es trennt zwei Dinge, die Anfänger meist vermischen: **Wie schwer ist die Welle** (Budget, wächst planbar) und **woraus besteht sie** (Zufall, innerhalb des Budgets). Das erste kontrollierst du, das zweite überlässt du dem Würfel. Das ist der ganze Trick, und er ist derselbe, den echte Spiele verwenden.

**Warum nicht einfach `anzahl = welle * 2`?** Weil dann jede Welle gleich aussieht, nur länger. Und warum nicht rein zufällig? Weil Welle 3 dann irgendwann drei Brecher enthält und du ohne Chance verlierst.

👀 **Nur erkennen: Gewichte.** Mit `random.choices(typen, weights=gewichte)` kommen manche Gegner häufiger als andere. Eine Zeile, sofort einsetzbar — aber wenn dich die Frage „Gewicht gegen Wahrscheinlichkeit" gerade nicht interessiert, bau sie einfach ein und geh weiter. Sie funktioniert auch ohne Theorie.

**Kaputtmachen:** Setz alle Gewichte gleich und spiel fünf Wellen. Dann setz ein Gewicht auf das Hundertfache. Beobachte, ob dein Budget-System das abfängt oder ob Welle 3 unspielbar wird.

**Commit dazwischen:** `Etappe 17a: Wellen werden erzeugt`

---

### 17b — Was der Zufall nach sich zieht

**Der wichtigste Satz dieser Etappe:** Sobald Zufall im Spiel ist, ist dein Spiel nicht mehr reproduzierbar — und damit auch nicht mehr debuggbar. Zwei identische Durchläufe gibt es nicht mehr, also lässt sich ein Fehler nicht mehr vorführen.

```python
random.seed(42)
```

Eine Zeile. **Derselbe Seed → derselbe Zufall → derselbe Fehler, jedes Mal.**

**Und dann bleibt der Seed nicht in dieser Zeile stehen, sondern wird sichtbar:**

```
[ Debug ]  Seed: 48173   Welle: 14
```

Der Seed wird beim Start gezogen und *angezeigt*, landet in Etappe 19 im Spielstand und lässt sich beim Start wieder vorgeben. Damit wird aus *„manchmal stirbt ein Gegner zu früh"* der Satz **„bei Seed 48173 in Welle 14 stirbt der zweite Brecher ein Feld zu früh"** — und das ist der Unterschied zwischen einem Bug, den man jagt, und einem, den man vorführt.

Diese eine Anzeige verbindet vier Etappen: Zufall (17) → Debugging (16) → Spielstand (19) → Tests (26).

**Dazu Ereignisse zwischen den Wellen** — jetzt, wo der Generator steht: ein Versorgungsabwurf, ein Generatorausfall, der deine Geschütze für zwei Wellen halbiert, ein Riss in der Kuppel, Funkkontakt mit jemandem, der nicht antwortet. Technisch ist das dieselbe gewichtete Auswahl wie bei den Gegnern, nur mit anderen Folgen.

**Hier zahlt Etappe 1 aus:**

> *„Die Aufzeichnung läuft immer noch. Sie ist von vor achtzehn Tagen."*

Die Variable, die du am ersten Tag angelegt und nie benutzt hast, bekommt heute ihren Auftritt. Das war der Sinn der Übung.

**Optional, und ausdrücklich Kür:** Ein Sektor, der endgültig fällt, wenn du zu langsam warst — ausgelöst davon, wie oft er beschädigt wurde und was du in Etappe 15 herausgefunden hast. Er kommt nicht zurück. Das ist Spieldesign, kein Python-Lernziel, und es gehört an den Schluss der Etappe oder gar nicht.

**Lernziele:**
- Unterschied `random.choice` / `random.random` / `random.randint`?
- Was macht ein Seed, und warum ist er beim Testen Gold wert?
- Warum ist „Budget" eine bessere Steuerung als „Anzahl"?
- Was kannst du an einem Fehler *nicht* mehr feststellen, wenn dein Programm bei jedem Lauf andere Zahlen zieht?

**🧠 Entwicklerfrage:** *Wie viel Zufall ist noch fair?* Wo genau liegt für dich die Grenze zwischen „überraschend" und „verloren, ohne dass ich etwas falsch gemacht habe"? Zwei bis fünf Sätze in `GELERNT.md`.

**Commit:** `Etappe 17b: Reproduzierbarer Zufall und Ereignisse`

---

## Etappe 18 — Fähigkeiten, Freischaltungen, Statuseffekte

**Boot.dev:** Zustandsverwaltung, Sets, komplexere Boolean-Logik

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Statuseffekte mit Dauer · Voraussetzungen für Fähigkeiten | Zustand, der weder dauerhaft noch einmalig ist | `and`/`or` als Rückgabewerte |

**Die Reihenfolge ist nicht beliebig:** Erst die Statuseffekte — das ist der eigentliche Stoff und die schwerste Sorte Zustand. Dann die Voraussetzungen. Die dritte Spalte ist Lesestoff und darf ausfallen.

Ein zentraler `flags`-Speicher (ein Set — jetzt weißt du, warum). Fähigkeiten haben Voraussetzungen: eine bestimmte Freischaltung, eine Mindestwellennummer, genug Schrott, die richtige Klasse. Das ist eine verknüpfte Bedingung, und sie ist erwachsen geworden seit Etappe 2.

Dazu **Statuseffekte** mit Dauer: brennend, geschockt, überladen, abgeschirmt. Sie hängen an Einheiten, sie zählen im Tick herunter, sie verändern Werte, solange sie laufen. Damit hast du zum ersten Mal Zustand, der weder dauerhaft noch einmalig ist — die Sorte, die am schwersten sauber zu modellieren ist.

👀 **Nur erkennen: `and` und `or` geben nicht `True`/`False` zurück, sondern einen der beiden Werte.**

```python
ziel = gewaehltes_ziel or standardziel
```

**Schreib das heute nicht.** In deinem eigenen Code ist `if ziel is not None:` klarer, und Klarheit schlägt Kürze. Aber du wirst diese Form in fremdem Code ständig sehen, und dann soll sie nicht mystisch wirken.

**Und wenn du sie siehst, stell genau eine Frage:** Kann die linke Seite legitim `0` sein? Denn `0` ist falsy — dann greift die rechte Seite, obwohl links ein gültiger Wert stand. In einem Spiel voller Zähler, Indizes und Munitionsstände ist das kein Sonderfall, sondern der Normalfall. Das ist die Null-Falle aus dem Rahmenteil, in ihrer gemeinsten Form.

**Und jetzt wird der Trupp klug — genau einmal und dann nicht mehr.**

Bisher laufen deine drei Marines zum nächsten Gegner und schießen. Ab heute setzen sie auch ihre Fähigkeit ein, sobald deren Voraussetzungen erfüllt sind: Der Medic heilt, wenn jemand unter der Hälfte ist. Der Engineer repariert, wenn ein Sektor beschädigt ist. Der Heavy feuert seine Salve, wenn genug Ziele in Reichweite stehen.

**Das ist dieselbe verknüpfte Bedingung wie beim Spieler — nur ohne Spieler.** Und genau daran zeigt sich, ob dein Fähigkeitensystem sauber gebaut ist: Wenn „darf diese Fähigkeit jetzt eingesetzt werden?" eine Funktion ist, die einen Wahrheitswert liefert, dann kann sie jeder aufrufen — dein Befehl genauso wie eine `update()`-Methode. Wenn die Prüfung dagegen in deiner Befehlsverarbeitung verstreut liegt, musst du sie für die KI ein zweites Mal schreiben.

**Das ist eine Beobachtung, keine Anweisung.** Wenn du merkst, dass du dieselbe Bedingung zweimal geschrieben hast, ist das die Erkenntnis dieser Etappe — und der Grund, warum in Etappe 23 Funktionen zu Werten werden.

**Und damit ist die Trupp-KI fertig.** Weiter geht sie in diesem Plan nicht. Rückzug, Fokusfeuer, Formationen, Absprachen — alles reizvoll, alles ein Abend, nichts davon lehrt dich Python, das nicht schon woanders steht. Nach Etappe 27 gehört das Spiel dir; dann kannst du daran bauen, so lange du willst.

**Lernziele:**
- Was gibt `a or b` zurück, wenn `a` truthy ist?
- Warum wird der rechte Teil manchmal gar nicht ausgewertet?
- Wo ist das gefährlich (wenn `0` ein gültiger Wert ist)?
- Wo speicherst du einen Statuseffekt — bei der Einheit oder bei der Welt? Was spricht wofür?
- Warum ist „Effekt läuft ab" schwerer zu testen als „Effekt ist aktiv"?

**🧠 Entwicklerfrage:** *Wo gehört Zustand hin?* Ein brennender Gegner — ist das eine Eigenschaft des Gegners oder ein Eintrag in einer Effektliste der Welt? Beides funktioniert. Entscheide dich, schreib die Begründung auf, und schau in Etappe 22 nach, ob sie noch trägt.

**Commit:** `Etappe 18: Fähigkeiten und Statuseffekte`

---

## Etappe 19 — Speichern und Laden

**Boot.dev:** Datei-I/O, `json`, `pathlib`

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Speichern und Laden mit `json`, `pathlib`, `with` · `save_version` | Warum Set und Tuple beim Laden nicht mehr da sind | Atomares Schreiben über eine temporäre Datei |

Kompletter Weltzustand in eine Datei und zurück — inklusive halb fertig gebauter Geschütze, laufender Nachschubzähler, Statuseffekte mit Restdauer, freigeschalteter Fähigkeiten, erkundeter Vorfeldfelder.

**Die wichtigste Einsicht dieser Etappe — und sie ist präziser, als sie klingt:**

JSON ist **nicht** „Python-Objekte in anderer Form". JSON kennt genau sechs Dinge: Text, Zahl, Wahrheitswert, `null`, Liste, Objekt (≈ Dictionary). Deine `Marine`-Instanz ist nichts davon. Ein Set auch nicht. Ein Tuple auch nicht — und deine Positionen sind Tuples.

Du musst also selbst **entscheiden, wie sich dein Objekt als solche Daten darstellen lässt** — und wie du es daraus wieder herstellst. Das ist eine Design-Entscheidung, keine Übersetzung.

**Der Begriff dafür ist Serialisierung, und er ist eine Abbildung mit vier Stationen:**

```
Python-Objekt  →  einfache Daten  →  JSON-Text  →  einfache Daten  →  Python-Objekt
     ↑                                                                      ↓
     └──────────────── Kommt hier dasselbe an wie oben? ────────────────────┘
```

**Die Frage, an der alles hängt: Ist diese Abbildung verlustfrei?** Und die Antwort ist nein, wenn du nicht aufpasst:

```
(4, 2)        →  [4, 2]      →  beim Laden eine Liste, kein Tuple
{"a", "b"}    →  ["a", "b"]  →  beim Laden eine Liste, kein Set — Duplikate wieder möglich
```

Python weiß beim Laden nicht mehr, dass da mal ein Tuple stand. Das ist keine Schwäche von JSON, sondern der Preis dafür, dass die Datei auch von etwas gelesen werden kann, das kein Python ist. **Du musst den Verlust also selbst rückgängig machen** — und dafür musst du wissen, welche deiner Werte betroffen sind. Deine Positionen sind Tuples. Deine Freischaltungen sind ein Set. Deine erkundeten Felder sind ein Set aus Tuples, also gleich doppelt.

**Der Reflex, den du daraus mitnimmst:** Beim Laden ist nichts, was du bekommst, automatisch das, was du gespeichert hast. Genau diese Skepsis brauchst du in Etappe 25 noch einmal — dort gegenüber Dateien, die du gar nicht selbst geschrieben hast.

**Der Fall, an dem du es merkst:** Ein Geschütz, das bei `bauzeit = 40` gerade bei `alter = 17` steht. Speicherst du „im Bau" oder „noch 23 Ticks"? Beides funktioniert. Nur eines überlebt es, wenn du in Etappe 22 die Bauzeit änderst.

**Und eine Zeile, die du heute schreibst und in zwei Monaten feierst:**

```python
{"save_version": 1, ...}
```

Eine Versionsnummer im Spielstand. Heute völlig überflüssig — du hast genau ein Format.

In Etappe 22 änderst du deine Baupläne, in 25 kommt der Content aus JSON, und plötzlich passt ein Spielstand von letzter Woche nicht mehr zum Programm von heute. Ohne Versionsnummer bekommst du dann einen `KeyError` mitten im Laden und weißt nicht, ob dein Code kaputt ist oder die Datei alt. Mit Versionsnummer bekommst du: *„Dieser Spielstand ist Version 1, ich verstehe Version 2."*

Das ist kein Lehrbuchproblem. **Das ist das häufigste Problem, das Software mit gespeicherten Daten überhaupt hat**, und du löst es heute mit einer Zeile. Ob du später auch migrierst — alte Stände umrechnen statt abweisen — kannst du dann entscheiden. Erkennen musst du das Problem, bevor es dich trifft.

**Warum `pathlib` und nicht einfach Strings?** Weil `"saves/" + name + ".json"` auf Windows mit Backslashes bricht, bei doppelten Schrägstrichen still das Falsche tut und dir kein `mkdir`, kein `.exists()` und kein `.stem` gibt. Ein Pfad ist kein Text, der zufällig Schrägstriche enthält — er ist ein eigener Datentyp mit eigenen Operationen. Dieselbe Einsicht wie bei `"40"` gegen `40` in Etappe 1, nur eine Ebene höher.

**Neu dabei: `pathlib`.** Pfade sind kein String-Basteln:

```python
from pathlib import Path
SAVE_DIR = Path("saves")
SAVE_DIR.mkdir(exist_ok=True)
```

**Neu dabei: `with`.** Ab hier öffnest du Dateien nie wieder anders:

```python
with open(pfad, "w", encoding="utf-8") as f:
    json.dump(daten, f, ensure_ascii=False, indent=2)
```

`with` sorgt dafür, dass die Datei **auch dann geschlossen wird, wenn mittendrin ein Fehler auftritt**. Und `encoding="utf-8"` schreibst du *immer* hin.

👀 **Nur erkennen — Bonus, wenn der Rest steht:** Was passiert, wenn beim Speichern der Strom ausfällt? Dann steht eine halb geschriebene Datei da, und der Spielstand ist unrettbar — schlimmer als gar keiner. Die übliche Lösung ist zwei Zeilen lang: erst in eine temporäre Datei schreiben, dann umbenennen. **Umbenennen ist unteilbar, Schreiben nicht.**

Das heißt *atomares Schreiben*, es steckt in jedem ernsthaften Programm, das Dateien anfasst, und du musst es heute nicht einbauen. Wissen, dass es das Problem gibt, reicht vollkommen — sonst lernst du an einem Abend JSON, Serialisierung, Dateizugriff und Absturzsicherheit gleichzeitig.

**Erweitern ohne zu zerstören:** Erweitere das Speichern so, dass Statuseffekte mitgesichert werden — ohne die bestehende Speicherlogik umzuschreiben.

**Lernziele:**
- Welche sechs Datentypen kennt JSON?
- Wie stellst du ein Set in JSON dar — und wie machst du es beim Laden rückgängig?
- Was wird aus deinen Positions-Tuples, wenn du sie speicherst und wieder lädst?
- Was macht `with` genau, und was passiert ohne?
- Warum ist ein halb geschriebener Spielstand schlimmer als gar keiner?

**🧠 Entwicklerfrage:** *Was muss ein Spielstand garantieren?* Dass er lädt? Dass er *denselben* Spielzustand ergibt? Dass er auch in drei Monaten noch lädt, wenn dein Code sich verändert hat? Die drei Antworten führen zu drei verschiedenen Dateiformaten.

**Commit:** `Etappe 19: Der Vorposten überlebt das Beenden`

---

## Etappe 20 — Wenn der Spieler Unsinn eingibt

**Boot.dev:** `try` / `except`, eigene Exceptions, Validierung

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| `try`/`except` an den richtigen Stellen · **eine** eigene Exception-Klasse | Wann prüfen (`if`), wann fangen (`try`) | Exception-Hierarchien · `finally` · `logging` |

Kein Absturz mehr. Unbekannte Befehle, zu wenig Schrott, volles Inventar, ein Bauplatz, auf dem schon etwas steht, ein Sektor, der nicht mehr existiert — alles wird abgefangen und erklärt.

**Wichtige Abgrenzung:** Das hier ist Fehler*behandlung*. Debugging (Etappe 8, 16) ist etwas anderes. Fehlerbehandlung heißt: das Programm bleibt stehen statt abzustürzen. Debugging heißt: du findest heraus, warum es sich falsch verhält. Verwechsle die beiden nie.

**Eine eigene Exception, und die ist erstaunlich billig:**

```python
class SpielFehler(Exception):
    pass
```

Drei Wörter, und du hast einen Fehlertyp, der nur dir gehört. `raise SpielFehler("Dafür reicht dein Schrott nicht")` an der Stelle, wo es auffällt — `except SpielFehler` an der Stelle, wo du damit umgehen willst. Dazwischen darf beliebig viel Code liegen, und du musst keinen Rückgabewert durchreichen.

👀 **Nur erkennen — Hierarchien.** Man kann davon Unterklassen bilden (`class NichtGenugSchrott(SpielFehler)`) und dann wahlweise einen einzelnen Fall oder die ganze Familie fangen. Jede ernsthafte Bibliothek macht das, und es ist der Grund, warum du in fremdem Code `except json.JSONDecodeError` liest. **Bauen musst du heute genau eine Klasse.** Wenn dein Spiel später mehr Unterscheidung braucht, merkst du das — und dann kostet es zwei Zeilen.

👀 **Nur erkennen: `finally`.** Du sollst es nicht einbauen — du sollst wissen, was es tut, wenn es dir begegnet:

```python
try:
    spiele()
finally:
    speichere_automatisch()     # läuft IMMER — auch bei Absturz, auch bei return
```

Die vier Schlüsselwörter in einer Zeile: `try` = versuche · `except` = falls Fehler · `else` = falls kein Fehler · `finally` = danach in jedem Fall.

Ein naheliegender Einsatz wäre der automatische Spielstand beim Beenden — nach zwölf überstandenen Wellen soll ein Absturz nicht alles kosten.

**Und jetzt die Präzisierung, die den Unterschied zwischen „gelesen" und „verstanden" ausmacht.** Der Kommentar oben sagt „läuft IMMER", und das ist die übliche Kurzfassung. Sie stimmt nicht ganz:

| `finally` läuft | `finally` läuft nicht |
|---|---|
| bei einer Python-Ausnahme | bei `kill -9` oder Task-Manager |
| bei `return`, `break`, `continue` | bei Stromausfall oder Systemabsturz |
| bei `Strg+C` (`KeyboardInterrupt`) | bei `os._exit()` |
| beim normalen Ende des Blocks | wenn der Python-Prozess selbst abstürzt |

**Die rechte Spalte ist der Grund, warum die temporäre Datei aus dem Abschnitt oben trotzdem nötig ist.** `finally` schützt dich vor Programmfehlern, nicht vor der Welt. Wer das verwechselt, baut sich eine Sicherheit, die er nicht hat — und das ist gefährlicher als gar keine, weil man aufhört, weiter nachzudenken.

**Merk dir die Form dieser Erkenntnis, sie kommt noch oft:** Eine Zusage in der Dokumentation gilt unter Bedingungen. Die Frage ist nie „was verspricht es?", sondern „unter welchen Umständen bricht das Versprechen?"

**🚨 KI-Code-Warnsignal — und zwar das häufigste von allen:**

```python
try:
    irgendwas()
except Exception as e:
    print("Fehler")
```

Sieht verantwortungsvoll aus. Ist es nicht. **Frag dich: Was ist hier gerade verloren gegangen?**

Die Antwort: die Information, *welcher* Fehler aufgetreten ist und *wo*. Ein Tippfehler im Variablennamen, eine kaputte Datei und ein Programmierfehler in einer ganz anderen Funktion — alle drei landen in derselben Zeile und erzeugen dieselbe nichtssagende Meldung. Der Traceback, an dem du seit Etappe 1 alles ablesen konntest, ist weg.

Damit hast du einen Fehler vom Typ 1 in einen vom Typ 3 verwandelt: Das Programm stürzt nicht mehr ab und tut trotzdem das Falsche, nur eben leise.

KI-generierter Code produziert dieses Muster besonders gern, weil es defensiv wirkt und jeden Test überlebt. Wenn du es siehst, ist die Frage nie „ist das schlimm?", sondern immer: **Welchen Fehler wollte der Autor hier eigentlich abfangen — und warum steht das nicht da?**

Ein sauberes `except` nennt seinen Fehler. Wenn du wirklich alles fangen musst, dann gib wenigstens `e` mit aus, oder lös den Fehler mit `raise` wieder aus, nachdem du dein Aufräumen erledigt hast.

**Die Unterscheidung, die dieses Spiel besonders braucht:** „Das ist kein Befehl" ist etwas anderes als „Das geht hier gerade nicht". `baue geschuetz` ist ein gültiger Befehl — nur nicht mitten in einer Welle und nicht ohne Schrott und nicht auf einem besetzten Feld. Drei verschiedene Fehler, drei verschiedene Meldungen. Wer sie zusammenwirft, baut ein Spiel, das der Spieler nicht versteht.

**Zehn Minuten Leseeinheit: `print()` gegen `logging`.** Du baust heute kein Logging-System — du sollst nur eines lesen können. In fremdem Code stehen Zeilen wie `logger.warning(...)`, und die Frage ist nicht, wie man das schreibt, sondern was es bedeutet:

| Stufe | Heißt | Beispiel bei dir |
|---|---|---|
| `debug` | für Entwickler, im Normalbetrieb aus | „Gegner 3 rückt auf Feld (4,2)" |
| `info` | normaler Ablauf | „Welle 7 beginnt" |
| `warning` | ungewöhnlich, läuft aber weiter | „Bauauftrag ohne Platz" |
| `error` | etwas ist fehlgeschlagen | „Speicherstand nicht lesbar" |

Der Unterschied zu `print()` ist der Schalter: Ein Log lässt sich **abstellen, filtern und in eine Datei umleiten**, ohne dass jemand Code ändert. Deshalb steht in ernsthaften Projekten kein `print()`. Wenn du eines Tages ein Programm bekommst, das nichts sagt — dann sagt es vermutlich etwas, nur auf einer Stufe, die gerade ausgeschaltet ist. Das zu wissen erspart dir eine unnötige Fehlersuche.

**Lernziele:**
- Unterschied `except Exception` ↔ `except:`?
- Wann läuft `finally`, wann `else` beim `try`?
- Warum eine eigene Exception-Klasse statt `raise Exception("...")`?
- Wann prüfst du vorher (`if`), wann fängst du hinterher (`try`)?
- Was kann ein Log, was `print()` nicht kann?

**Kaputtmachen:** Fang alles mit `except:` ab. Merke, warum das eine schlechte Idee ist — es verwandelt Fehler vom Typ 1 in Fehler vom Typ 3.

**🧠 Entwicklerfrage:** *Welchen Fehler zeige ich dem Spieler, und welchen dem Entwickler?* „Dafür reicht dein Schrott nicht" gehört ins Spiel. Ein `KeyError` in der Wellenlogik gehört nicht ins Spiel — aber verschwinden darf er auch nicht. Wohin damit?

**Commit:** `Etappe 20: Kein Absturz mehr`

---

## Etappe 21 — Kampf, richtig gerechnet

**Boot.dev:** Mehrere Rückgabewerte, Zahlenlogik — plus `Enum`

**Geteilt, und zwar an einer klaren Naht.** 21a ist die Rechnung. 21b ist alles, was man auf eine funktionierende Rechnung obendrauf setzen kann — und obendrauf heißt: erst wenn sie funktioniert.

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **21a** | Trefferchance, Schaden, Panzerung · zwei Rückgabewerte | Warum eine Funktion zwei Werte liefert statt zweimal einen | — |
| **21b** | Ein `Enum` für deine Spielzustände · Balancing auf einem Branch | Wann `Enum` lohnt und wann nicht | Schadenstypen und Widerstände |

---

### 21a — Die Rechnung

Seit Etappe 3 kämpfst du mit einer Platzhalterformel. Heute wird sie eine richtige: **Trefferchance, Schaden, Panzerung.** Drei Dinge, nicht acht.

**Mehrere Rückgabewerte, weil du sie hier wirklich brauchst:** `berechne_treffer()` liefert nicht nur den Schaden, sondern auch, *was passiert ist* — getroffen oder verfehlt. Ein Tuple aus zwei Werten:

```python
schaden, ergebnis = berechne_treffer(...)
```

Und jetzt weißt du auch, warum `(5)` und `(5,)` in Etappe 6 unterschiedliche Dinge waren.

**Warum das mehr ist als eine Bequemlichkeit:** Eine Funktion, die nur den Schaden zurückgibt, zwingt den Aufrufer zum Raten — *war 0 ein Fehlschlag oder ein Treffer auf schwere Panzerung?* Zwei Rückgabewerte beantworten das, ohne dass irgendwo `print()` stehen muss. Das ist dieselbe Entscheidung wie in Etappe 7b: **Die Logik rechnet und gibt zurück, die Darstellung gibt aus.**

**Und hier zahlt Etappe 7b zum ersten Mal richtig:** Wenn deine Kampffunktion nichts ausgibt, kannst du sie in Etappe 26 testen. Wenn sie `print()` enthält, kannst du das nicht.

**Lernziele:**
- Warum gibt eine Funktion zwei Werte zurück statt zweimal einen?
- Warum ist eine Formel mit Multiplikation anders zu balancieren als eine mit Subtraktion?
- Was muss bei deiner Schadensformel *immer* gelten? (Nie negativ? Bei Panzerung 0 der volle Schaden?) Schreib drei `assert`-Zeilen dazu — die Form kennst du aus Etappe 7b.

**Kaputtmachen:** Setz die Panzerung auf einen Wert größer als der Schaden und schau, ob dein Gegner geheilt wird. Das ist der Klassiker unter den Typ-3-Fehlern in Kampfsystemen, und er läuft völlig geräuschlos durch.

**Commit dazwischen:** `Etappe 21a: Der Kampf rechnet richtig`

---

### 21b — Was darauf aufbaut

**Neu: Zustände sauber modellieren.** Deine Zustandsstrings aus Etappe 12 bekommen ein Zuhause:

```python
from enum import Enum

class Spielzustand(Enum):
    VORBEREITUNG = 1
    WELLE = 2
    DEPOT = 3
```

`Spielzustand.WEELE` knallt sofort. `"weele"` schleicht sich durch — genau die Sorte Fehler vom Typ 3, die dich in Etappe 16 gekostet hat.

**Ein einziges `Enum` reicht für heute.** Nimm deine Spielzustände, sonst nichts. Du musst nicht jeden String in deinem Programm ersetzen — und du sollst auch keine eigenen `Enum`-Hierarchien entwerfen.

**Denn `Enum` ist nicht automatisch besser als ein String**, und der Reflex „Strings sind schlecht" wäre die falsche Lehre. Es lohnt sich unter zwei Bedingungen:

1. **Die Menge der gültigen Werte ist abgeschlossen** — es gibt genau diese Zustände und keine weiteren. Bei Spielzuständen stimmt das. Bei Einheitennamen, Gegenstandsbezeichnungen oder Sektorschlüsseln stimmt es nicht.
2. **Ein Tippfehler soll knallen statt durchzurutschen.**

Wo das nicht gilt, kostet `Enum` dich nur Umwandlungsarbeit — spätestens in Etappe 25, wenn dieselben Werte aus einer JSON-Datei kommen und wieder Strings sind. Ein `Enum` ist eine Zusage darüber, dass sich die Liste nicht ändert. Mach sie nur da, wo du sie halten willst.

👀 **Nur erkennen — Schadenstypen und Widerstände.** Der Plasmawerfer ist gegen Chitin gut und gegen Panzerung schlecht; der Panzerbrecher umgekehrt. Damit wird deine Waffenwahl eine Entscheidung statt einer Zahl, und technisch ist es ein Dictionary aus Faktoren. **Reizvoll, aber Kür.** Wenn 21a und das `Enum` stehen, ist die Etappe erfüllt. Schadenstypen kannst du jederzeit nachrüsten — sie lassen sich in Etappe 25 sogar bequemer als Daten hinzufügen als heute als Code.

**⚠️ Und jetzt die Warnung, die diese Etappe wirklich braucht:** Kampfbalancing ist ein Loch, in das man wochenlang fällt. Sobald die Formel läuft, willst du an ihr drehen, und es fühlt sich wie Arbeit an.

**Setz dir fünfzehn Minuten — und mach es auf einem Branch.**

```bash
git checkout -b balancing
```

Das ist der erste Moment in diesem ganzen Projekt, in dem ein Branch einen echten Zweck hat: Du probierst etwas aus, das du wegwerfen können willst. Wenn die Zahlen nach zwei Sitzungen nicht besser sind, `git checkout main`, und du hast nichts verloren. Genau dafür gibt es das.

*(Merges und Konflikte kommen in Etappe 24. Heute reicht: Branch anlegen, darauf arbeiten, zurückwechseln.)*

**Lernziele:**
- Was ist der Vorteil von `Enum` gegenüber Strings — und was gegenüber Zahlen?
- Wann lohnt sich ein `Enum`, und wann ist ein String die ehrlichere Wahl?
- Wozu ist ein Branch da, und was passiert mit deinen Änderungen, wenn du auf `main` zurückwechselst?

**🧠 Entwicklerfrage:** *Welche Werte gehören wirklich zum Kampfsystem?* Trefferchance — Eigenschaft der Waffe, des Schützen oder der Entfernung? Wo du sie hinschreibst, entscheidet darüber, was du später überhaupt noch verändern kannst.

**Commit:** `Etappe 21b: Zustände und Balancing`

---

## Etappe 22 — Baupläne und Ausbaustufen

**Boot.dev:** Datengetriebenes Design, Listen von Dictionaries

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Baupläne als Dictionary, neuer Geschütztyp ohne Logikänderung | Was Daten sind und was Verhalten ist | Komposition als dritter Weg |

```python
baupläne = {
    "mg_turm": {"kosten": {"schrott": 120}, "bauzeit": 8, "voraussetzung": None},
    "plasmaturm": {"kosten": {"schrott": 300}, "bauzeit": 20, "voraussetzung": "energiezelle"},
}
```

Geschütztypen, Waffen, Module, Fähigkeiten — alles bekommt Kosten, Bauzeit und Voraussetzungen. Und die Voraussetzung ist einfach ein Eintrag:

> *Der Plasmaturm braucht die Energiezelle. Also darf er erst gebaut werden, wenn die Energiezelle freigeschaltet ist.*

Ein Feld im Dictionary, eine Prüfung beim Bauen. Das ist alles — und es ist trotzdem der Moment, in dem dein Spiel einen Ausbaubaum bekommt, ohne dass du einen programmiert hättest.

**Fast geschenkt:** Bauzeiten, Nachschubzähler, Statuseffekte und Ereignisse laufen alle auf demselben Takt aus Etappe 12.

**Erweitern ohne zu zerstören:** Neuen Geschütztyp hinzufügen, ohne eine einzige Zeile Logik zu ändern. Wenn das klappt, hast du datengetriebenes Design verstanden. Wenn nicht, siehst du genau, an welcher Stelle deine Logik etwas über ihre Daten weiß, das sie nicht wissen sollte.

**Warum Daten und nicht Klassen — und wann wäre eine Klasse besser?**

Hol deine Antwort aus Etappe 11 hervor, bevor du weiterliest. Die Gegenprobe lautet:

| | Als Daten | Als Vererbung | Als Komposition |
|---|---|---|---|
| Unterscheiden sich nur **Werte** | ✅ eine Zeile pro Variante | ❌ vier fast identische Klassen | ➖ überflüssiger Aufwand |
| Unterscheidet sich das **Verhalten** | ❌ du landest bei `if typ == ...` | ✅ jede überschreibt ihre Methode | ✅ das Verhalten wird beigelegt |
| Soll es von **außen** änderbar sein | ✅ JSON, kein Code-Commit | ❌ nur mit Programmieren | ➖ teils: die Zusammensetzung ja, die Bausteine nein |
| Braucht es **eigenen Zustand** über Zeit | ❌ Daten sind stumm | ✅ das Objekt zählt selbst | ✅ das Objekt zählt selbst |
| Soll sich Verhalten **frei kombinieren** lassen | ❌ | ❌ Mehrfachvererbung wird schnell unübersichtlich | ✅ genau dafür ist es da |

Ein Bauplan hat andere Kosten und eine andere Bauzeit — reine Werte, also Daten. Ein *gebautes* Geschütz zählt seine Bauzeit herunter, sucht Ziele und feuert — eigener Zustand und eigenes Verhalten, also Objekt.

👀 **Nur erkennen — die dritte Spalte.** In Einführungen fehlt sie fast immer, und du sollst heute nichts damit bauen:

```
Marine
  + Fähigkeit:       Heilen
  + Zielstrategie:   Schwächster zuerst
```

Kein `Medic` als Unterklasse — ein Marine, dem ein Fähigkeitsobjekt beiliegt. Das heißt **Komposition**, du hast die Bauart in Etappe 10 schon benutzt, ohne dass sie so genannt wurde. Der Unterschied wird spürbar, sobald jemand einen Heavy will, der auch heilen kann: Bei Vererbung brauchst du eine fünfte Klasse, bei Komposition tauschst du einen Baustein.

**Du musst heute nichts umbauen.** Du sollst die Spalte nur kennen, damit deine Antwort auf die Frage aus Etappe 11 zwischen drei Möglichkeiten wählt statt zwischen zwei.

**Das ist die Trennung, die dir heute klar wird und die viele nie sauber sehen:** Der Bauplan ist das Rezept, das Geschütz ist der Kuchen. Beide beschreiben dasselbe Ding und gehören trotzdem in verschiedene Strukturen.

**Und jetzt kommt die Frage aus Etappe 11 zurück:** Deine vier Marine-Klassen unterscheiden sich durch Zahlen. Baupläne sind Zahlen. Könntest du die Klassen genauso behandeln? Solltest du? Das ist keine rhetorische Frage — beantworte sie schriftlich, und vergleich sie mit dem, was du in Etappe 11 aufgeschrieben hast.

**Und wenn deine beiden Antworten sich widersprechen, hast du alles richtig gemacht.** Der Widerspruch ist nicht peinlich, sondern der Beleg dafür, dass zwischen den beiden Einträgen echte Erfahrung liegt. Genau dieser Ablauf — **Entscheidung → Erfahrung → Gegenprobe → Revision** — ist das, was in keinem Kurs vorkommt, weil Kurse zu kurz dafür sind.

**🧠 Entwicklerfrage:** *Was ist Inhalt, und was ist Verhalten?* Ziehe an deinem eigenen Spiel eine Linie: Auf der einen Seite alles, was jemand ändern könnte, ohne Python zu können. Auf der anderen alles Übrige. Wo die Linie krumm wird, wirst du in Etappe 25 arbeiten.

**Commit:** `Etappe 22: Inhalt wird zu Daten`

---

## Etappe 23 — Python wird pythonisch ⭐

**Boot.dev:** Comprehensions, `dataclass`, Typannotationen

Keine neue Spielfunktion. **Und trotzdem die Etappe, die deinem eigentlichen Ziel am direktesten dient.**

Bis hierher lautete die Frage: *Wie schreibe ich etwas?* Ab hier: *Wie lese ich Code, den jemand anders geschrieben hat?*

**Diese Etappe ist die vollste im ganzen Plan, und das ist ein Problem.** Zehn Konzepte, von denen mehrere ein eigenes Denkmodell verlangen. Sie an einem Stück durchzuziehen bedeutet, sechs Dinge halb zu können.

**Deshalb ist sie in zwei Hälften geteilt, und dazwischen steht ein Commit.** Sie behält eine Nummer, weil sie ein Thema hat — aber behandle sie wie zwei Etappen, mit zwei bis drei Sitzungen je Hälfte:

### 23a — Python lesen

> Comprehensions · Funktionen als Werte · Callback · `lambda` · `*args` / `**kwargs`

**Das verbindende Thema: Code, in dem etwas anderes als eine Zahl herumgereicht wird.** Eine Liste, die aus einer Liste entsteht. Eine Funktion, die in einem Dictionary liegt. Ein Argument, das erst beim Aufruf ausgepackt wird. Alle fünf Punkte sind Formen, die dich beim Lesen fremden Codes stolpern lassen, wenn du sie nicht sofort erkennst.

**Commit dazwischen:** `Etappe 23a: Funktionen sind Werte`

### 23b — Python modellieren

> `dataclass` · Typannotationen · Dekoratoren erkennen · Kopplung zeichnen

**Das verbindende Thema: Code, der über sich selbst Auskunft gibt.** Eine Signatur, die sagt, was rein- und rausgeht. Eine Klasse, die als reiner Wertetyp gekennzeichnet ist. Ein `@`, das etwas mit der Funktion darunter macht. Und am Ende die Frage, die alles zusammenhält: *Wer kennt hier eigentlich wen?*

**Und die Anspruchsstufen gelten quer über beide Hälften:**

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Comprehensions, Funktionen im Dictionary, `lambda` als Sortierschlüssel, `dataclass`, Typannotationen | Callback als Muster · Kopplung als Frage | Dekoratoren, `*args`, `**kwargs` |

Die letzte Spalte schreibst du in diesem Projekt nie selbst. Du liest sie in jedem fremden Repo. Wenn dir dazu ein Satz einfällt („das faltet ein Dictionary in benannte Argumente auf"), reicht das vollkommen — geh weiter, statt eine Übung daraus zu machen.

**Comprehensions:**
```python
lebende = [g for g in self.gegner if g.hp > 0]
nach_typ = {g.typ: g for g in self.gegner}
```
*Warnung:* Eine Ebene, nie verschachtelt. Wenn die Comprehension schwerer zu lesen ist als die Schleife, hast du verloren.

**Funktionen sind Werte ⭐ — die wichtigste Einzelheit dieser Etappe.** Eine Funktion ist ein ganz normales Ding, das man in eine Variable legen, in ein Dictionary stecken und weiterreichen kann:

```python
befehle = {
    "status": zeige_status,     # kein Aufruf! Keine Klammern!
    "kaufe": kaufe,
}

befehle["status"](marine)       # HIER wird aufgerufen
```

Damit stirbt die letzte `elif`-Kette deines Spiels — die in `verarbeite_befehl()`, die seit Etappe 3 gewachsen ist.

**Und dann der Fall, für den dieses Setting gemacht ist: Zielauswahl.** Ein Geschütz muss entscheiden, worauf es feuert — der nächste Gegner, der stärkste, der schwächste, der mit dem meisten Schaden. Vier Strategien. Vier Funktionen. Ein Dictionary. Und plötzlich ist „Zielpriorität einstellen" eine Spielmechanik, die dich eine Zeile kostet:

```python
strategien = {"naechster": ..., "staerkster": ...}
ziel = strategien[self.modus](gegner_in_reichweite)
```

Das ist dasselbe Muster, mit dem jede grafische Oberfläche der Welt arbeitet: *„ruf DAS hier auf, wenn geklickt wird."* Das heißt **Callback**, und ohne dieses Konzept ist fremder Oberflächen-Code Magie.

Dazu die Kurzform für Wegwerf-Funktionen — und auch die hat hier einen echten Zweck:

```python
sortiert = sorted(gegner, key=lambda g: g.entfernung)
```

**Was `@` eigentlich bedeutet.** Ein Dekorator ist eine Funktion, die eine Funktion nimmt und eine veränderte zurückgibt. Die Syntax ist nur eine Abkürzung:

```python
@irgendwas
def f(): ...

# ist exakt dasselbe wie:
def f(): ...
f = irgendwas(f)
```

Du wirst wenige eigene schreiben und tausende lesen — `@dataclass`, `@property`, `@pytest.fixture`.

**dataclass:**
```python
from dataclasses import dataclass

@dataclass
class Gegnertyp:
    name: str
    hp: int
    schaden: int
    kosten: int
```
Die Brücke zwischen „ich verstehe Klassen" und „ich verstehe, wie professioneller Python-Code aussieht". Und für reine Wertetypen wie Gegnerdaten ist es genau das richtige Werkzeug.

**Typannotationen:**
```python
def finde_ziel(self, gegner: list[Gegner]) -> Gegner | None:
```
**Ehrliche Einordnung:** Python *prüft* das zur Laufzeit nicht. Es ist Dokumentation, die dein Editor lesen kann — keine Typsicherheit. Genau deshalb ist es für dich wichtig: Die Signatur sagt dir sofort, was rein- und rausgeht. Und `| None` ist die Zeile, an der du in fremdem Code erkennst, dass du eine Prüfung brauchst.

**`*args` und `**kwargs`, jetzt richtig.** Du brauchst sie zum Lesen, nicht zum Schreiben:

```python
def protokoll(nachricht, *args, **kwargs):
    print(nachricht, args, kwargs)

protokoll("Treffer", 12, stufe="warnung")   # args=(12,)  kwargs={"stufe":"warnung"}
```

Und die Form, die dir am häufigsten begegnet — das Durchreichen: `fremde_funktion(**config)` faltet ein Dictionary in benannte Argumente auf.

**Und ein Lesekriterium, das ab hier zu jeder Leseübung gehört: Was hängt wovon ab?**

Den Begriff kennst du seit Etappe 13 — dort war es die Frage, warum das Geschütz die ganze Welt kennen muss. Jetzt wird daraus ein Werkzeug. Zeichne bei jedem größeren Stück Code auf, wer wen kennt:

```
Welt → Einheit
Einheit → Welt        ← beide Richtungen? das ist ein Signal
Geschuetz → Welt
```

Du brauchst dafür keine Architekturtheorie. Du brauchst nur die Fähigkeit, irgendwann zu sagen: *„Diese Klasse weiß zu viel über die Welt."* Das ist der Satz, der dich vom Konsumenten zum Beurteiler macht — und es ist die Vorstufe zu Frage 6 der Leseleiter, die in Etappe 27 zählt.

**Leseübung, Stufe 4 (15 Min):** Ich gebe dir ein Stück Code aus einem echten Projekt — ab hier ausdrücklich auch KI-generierten Code aus deinen eigenen. Du erklärst, was es tut, und beantwortest zum ersten Mal die sechste Frage: Wo ist die schwächste Stelle? Das ist der eigentliche Test dieses ganzen Lehrplans.

**🧠 Entwicklerfrage:** *Wer muss wen kennen?* Hol die Zeichnung aus Etappe 15 hervor und mach sie noch einmal — für dein heutiges Programm, mit allem, was seitdem dazugekommen ist. Vergleich die beiden. Was ist gewachsen, was hättest du anders gebaut, wenn du es damals gewusst hättest?

**Commit:** `Etappe 23b: Python wird pythonisch`

---

## Etappe 24 — Das Projekt wird zum Projekt (Code + Git)

**Boot.dev:** Module, Imports, Paketstruktur

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Aufteilung in Module, `import`, `if __name__ == "__main__"` · Branch mergen | Warum zirkuläre Importe ein Signal sind | `pyproject.toml`, Versionsangaben, semantische Versionierung |

**Der Satz, um den es heute geht, ist erstaunlich schlicht:**

> *Mein Programm ist nicht kaputt. Es ist einfach zu groß für eine Datei geworden.*

Das ist keine Architekturlektion, sondern eine Erfahrung. Eine Python-Datei kann ein *Teil* deines Programms sein — mehr musst du heute nicht mitnehmen.

Aufteilung in mehrere Dateien, zum Beispiel `welt.py`, `einheiten.py`, `wellen.py`, `depot.py`, `vorfeld.py`, `befehle.py`, `main.py`.

**Ausdrücklich: Das ist ein Vorschlag, kein Standard.** Deine Struktur darf anders aussehen, solange du **begründen kannst, warum**:

> Ich teile ein Programm in Module auf, wenn es dadurch verständlicher und wartbarer wird.

Wenn du beim Aufteilen merkst, dass zwei Dateien ständig voneinander importieren, ist das ein Signal. **Und wenn es knallt, heißt der Fehler `ImportError: ... (most likely due to a circular import)`.** Diesen Satz solltest du einmal gesehen haben, bevor er dich in fremdem Code trifft — und in diesem Projekt wirst du ihn sehen, weil `welt` die Einheiten kennt und die Einheiten die Welt.

**Zwei Dinge, die zur Struktur gehören:**

```python
if __name__ == "__main__":
    main()
```

Eine Datei hat zwei Rollen: gestartet werden *oder* importiert werden. Ohne diese Zeile läuft dein Spiel los, sobald jemand `import main` schreibt — zum Beispiel dein Testframework in Etappe 26.

Dazu der Unterschied zwischen `from .welt import Welt` (relativ) und `from vorposten.welt import Welt` (absolut).

**Und die Datei, die sagt „das hier ist ein Projekt": `pyproject.toml`.**

```toml
[project]
name = "vorposten"
version = "0.1.0"
requires-python = ">=3.11"
dependencies = ["pygame>=2.5"]

[project.scripts]
vorposten = "vorposten.main:main"
```

Mit der letzten Zeile wird aus `python -m vorposten.main` ein Befehl namens `vorposten`.

**Die Unterscheidung, die fast überall falsch erklärt wird:** Die beiden Dateien sind **keine Konkurrenten**.

| | Sagt | Beispiel |
|---|---|---|
| `pyproject.toml` | Was mein Projekt **braucht** — als Bereich | `pygame>=2.5` |
| `requirements.txt` | Was genau **installiert war** — exakt | `pygame==2.5.2` |

Das erste ist die Absicht, das zweite die Momentaufnahme.

**Versionsangaben lesen können** ist wichtiger als sie schreiben zu können: `>=2.5` heißt „mindestens", `==2.5.2` „genau diese", `~=2.5` „2.5 und Korrekturen, aber nicht 3.0". Dahinter steht **semantische Versionierung**.

**Und jetzt die Gegenprobe: eine fremde Bibliothek lesen, bevor du sie benutzt.** ⭐

Bis hierher hast du deine eigenen Module gebaut. Heute schaust du in fremde. Nimm eine einzige Zeile, die dir in Etappe 28 begegnen wird:

```python
bildschirm = pygame.display.set_mode((800, 600))
```

Und beantworte, ohne Pygame je benutzt zu haben:

1. Was ist `pygame` — Datei, Ordner, Paket?
2. Was ist `display`, und wo liegt es auf der Festplatte?
3. Was ist `set_mode` — Funktion, Methode, Klasse? Woran erkennst du das?
4. Was wird übergeben — wie viele Argumente sind das eigentlich?
5. Was kommt zurück, und woran hast du das festgestellt?

**Frage 4 ist die Falle**, und sie ist mit Absicht gestellt: Es sieht aus wie zwei Argumente und ist eines, ein Tuple. Die Komma-Falle aus Etappe 6, zwei Blöcke später und im fremden Code.

**Warum das hierher gehört und nicht in Etappe 28:** Dein späteres Problem wird nicht sein „kann ich Python schreiben", sondern *„eine KI hat hier `pygame.sprite.Group()` benutzt — was ist das?"* Genau diese Situation übst du heute, mit deinem frischen Modulwissen und den Werkzeugen aus Etappe 8: `print(pygame.__file__)`, F12 im Editor, `help()` und `dir()`. Du darfst in fremden Code hineinschauen. Er liegt auf deiner Festplatte.

**Warum überhaupt aufteilen — warum nicht alles in einer Datei?**

Eine einzelne Datei hat echte Vorteile: nichts zu importieren, keine zirkulären Abhängigkeiten, alles mit einer Suche auffindbar. Bei zweihundert Zeilen ist sie die richtige Wahl, und wer dort schon Module baut, macht sich das Leben ohne Gegenwert schwer.

Die Grenze liegt nicht bei einer Zeilenzahl, sondern hier: **Wenn du beim Suchen einer Stelle scrollst statt springst, und wenn du beim Ändern einer Sache Angst um eine andere hast.** Beides hast du inzwischen. Genau deshalb steht diese Etappe hier und nicht bei Etappe 12.

---

**Der Git-Teil — nimm ihn als eigene Sitzung.** Diese Etappe ist auch ohne ihn schon voll, und Git ist kein Python. Mach erst die Struktur fertig, committe, und fang danach neu an.

Branches, Merges, Merge-Konflikte — und wie man einen absichtlich herbeiführt, um zu sehen, wie er aussieht. Erst jetzt, weil du erst jetzt einen Grund hast. **Dein Balancing-Branch aus Etappe 21 ist das Übungsobjekt.**

**Pull Requests lässt du aus, solange du allein arbeitest.** Ein PR ist ein Verfahren, um jemand anderen um Durchsicht zu bitten — allein am eigenen Repo ist er Zeremonie ohne Gegenüber. Wenn eines Tages ein zweiter Mensch dazukommt, lernst du ihn in einer Viertelstunde. Was du heute stattdessen üben solltest, ist das, was dich wirklich rettet: einen Merge rückgängig machen und einen Commit finden, der drei Tage zurückliegt.

**Lernziele:**
- Wozu `if __name__ == "__main__"` — was passiert ohne?
- Was ist der Unterschied zwischen einem Modul und einem Paket?
- Was sagt `pyproject.toml`, was `requirements.txt` — und warum ist das kein Widerspruch?
- Woran erkennst du an einer Versionsnummer, dass ein Update gefährlich sein könnte?
- Was ist ein zirkulärer Import, und was sagt er über deine Aufteilung?
- Wie findest du heraus, was eine fremde Funktion zurückgibt, wenn die Doku schweigt?

**🧠 Entwicklerfrage:** *Wann macht Aufteilung Code besser, und wann nur komplizierter?* Du hast heute beides erlebt — die Datei, bei der die Trennung sofort einleuchtete, und die, bei der du zweimal umsortiert hast. Was war der Unterschied?

**Commit:** `Etappe 24: Das Projekt wird zum Projekt`

---

## Etappe 25 — Inhalt raus aus dem Code ⭐

**Boot.dev:** JSON als Content-Format, Laden zur Laufzeit

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| `content/`-Ordner, Laden beim Start, eine Prüffunktion | Drei Stufen von „gültig" · warum Daten von außen nie vertrauenswürdig sind | Schema-Validierung als eigenes Werkzeug |

**Der Erfolg, an dem du diese Etappe misst — und er ist ein großer:**

> *Füge einen neuen Gegnertyp hinzu, ohne eine einzige Zeile Python anzufassen.*

Wenn das klappt, hast du datengetriebenes Design nicht nur verstanden, sondern es benutzt.

Gegnertypen, Wellenrezepte, Waren, Baupläne, Fähigkeiten, Ereignisse, Vorfeld-Karten — alles wandert nach `content/`. Der Code lädt es beim Start.

**Neu und wichtig: Daten von außen sind nie vertrauenswürdig.** Ein Tippfehler in deinem JSON darf keinen unverständlichen Traceback erzeugen, sondern eine klare Meldung: *„content/gegner.json, Eintrag 3: Feld 'hp' fehlt."* Schreib eine kleine Prüffunktion, die die geladenen Daten kontrolliert, bevor das Spiel startet.

Das ist dieselbe Fehlerklasse wie in Etappe 8 — der Fehler steckt in den Daten, nicht im Code. Nur dass er jetzt aus einer Datei kommt, die du beim Schreiben nicht im Blick hattest.

**Und hier lernst du die Unterscheidung, die den ganzen Abschnitt trägt: „gültig" hat drei Stufen, und dein Spiel braucht alle drei.**

```
Datei laden
   ↓
1. syntaktisch gültig?   Ist das überhaupt JSON?          →  json.JSONDecodeError
   ↓
2. strukturell gültig?   Sind die erwarteten Felder da,   →  deine Prüfung
                         mit den erwarteten Typen?
   ↓
3. inhaltlich gültig?    Ergeben die Werte einen Sinn?    →  deine Prüfung
   ↓
Spiel starten
```

Der Fall, an dem der Unterschied kippt:

```json
{ "name": "Brecher", "hp": "sehr viel", "kosten": -30 }
```

**Das ist einwandfreies JSON.** Stufe 1 ist zufrieden. Stufe 2 findet den ersten Fehler: `hp` sollte eine Zahl sein und ist Text. Stufe 3 findet den zweiten: `kosten` ist zwar eine Zahl, aber eine negative — und ein Gegner, der dem Wellenbudget Geld *zurückgibt*, erzeugt in Etappe 17 eine Welle aus tausend Krabblern.

**Und genau das ist deine Fehlertypen-Skala von Etappe 8, eine Ebene höher gespiegelt:** Stufe 1 knallt sofort (Typ 1). Stufe 2 knallt irgendwann, an einer ganz anderen Stelle (Typ 2). Stufe 3 knallt nie und macht dein Spiel kaputt (Typ 3). **Je später die Stufe, desto teurer der Fehler** — und desto wichtiger, dass die Prüfung stattfindet, bevor das Spiel startet, und nicht mitten in Welle 9.

**Warum das für dich besonders zählt:** Ab hier kannst du an deinem Spiel *entwerfen*, ohne zu programmieren. Ein neuer Gegnertyp ist vier Zeilen JSON. Eine neue Welle ist eine Zeile. Eine neue Vorfeld-Karte ist ein Textblock.

**Das ist der Moment, in dem sich die Prämisse einlöst.** Ein Verteidigungsspiel lebt von Vielfalt, und Vielfalt war bis heute Arbeit im Code. Ab heute ist sie Arbeit in einer Textdatei — und dein Spiel kann von fünf Gegnertypen auf dreißig wachsen, ohne dass du die Spiellogik anfasst.

**Warum JSON und nicht einfach Python-Dateien mit Daten?** Eine Datei `gegner.py` mit einem großen Dictionary darin wäre kürzer zu laden — ein `import`, fertig, keine Umwandlung, Kommentare erlaubt. Der Preis: Wer den Inhalt bearbeitet, bearbeitet **ausführbaren Code**. Ein Tippfehler kann dann nicht nur falsche Werte erzeugen, sondern beliebiges Verhalten. Und niemand außer Python kann die Datei lesen — kein Editor, kein Werkzeug, keine andere Sprache. JSON ist dümmer, und genau das ist sein Vorteil: Daten, die nichts tun können.

**Und daraus ergibt sich direkt die nächste Etappe.** Deine Prüffunktion von heute ist selbst Code, der falsch sein kann — und sie ist die Stelle, an der du am wenigsten merkst, wenn sie es ist. Eine Validierung, die nichts findet, sieht genauso aus wie eine, die nicht funktioniert.

Damit hast du den Kreislauf, um den es in Etappe 26 geht:

```
Daten  →  Validierung  →  Fehler gefunden  →  Test dafür geschrieben
                              ↑                        ↓
                          Änderung  ←──────────  Test läuft wieder
```

Notier dir beim Bauen jeden Fall, den deine Prüfung abfangen soll — fehlendes Feld, falscher Typ, negative Zahl, unbekannter Verweis. Das ist keine Fleißarbeit: Es ist die Testliste für Etappe 26, und du schreibst sie zu dem Zeitpunkt, an dem dir die Fälle noch präsent sind.

**🧠 Entwicklerfrage:** *Wem vertraue ich — meinem Code, meinen Daten oder keinem von beiden?* Und die unbequeme Anschlussfrage: Deine Content-Dateien schreibst du selbst. Ändert das etwas? (Der Fehler, den du in vier Wochen in `gegner.json` machst, ist genauso fremd wie einer von jemand anderem. Du wirst dich nicht erinnern.)

**Commit:** `Etappe 25: Der Inhalt verlässt den Code`

**Und der ehrliche Zusatz:** Genau hier merkst du, ob Etappe 11 und 22 gut entschieden waren. Wenn deine Marine-Klassen sich in JSON beschreiben lassen, waren sie Daten. Wenn nicht, waren sie zu Recht Klassen. Diese Antwort bekommst du erst jetzt — und sie ist wertvoller als jede, die ich dir in Etappe 11 hätte geben können.

---

## Etappe 26 — Tests

**Boot.dev:** `pytest`

| 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|
| Tests für Schaden, Wellenbudget, Kaufvorgang, Speichern | Warum Zufall ohne Seed untestbar ist | `parametrize` und Fixtures |

**Und die gute Nachricht vorweg:** Das hier ist kein neues Konzept. Du sollst nicht „eine professionelle Test-Suite bauen". Du sollst deinem Programm eine Frage stellen und es sich selbst überprüfen lassen — mit genau den `assert`-Zeilen, die du seit Etappe 7b kennst. Neu ist nur der Rahmen: eine eigene Datei und ein Befehl, der alle Prüfungen auf einmal laufen lässt.

Jetzt formalisierst du, was du seit Etappe 7 nebenbei gemacht hast. Tests für das, was stillschweigend kaputtgeht: Schadensberechnung, Wellenbudget, Kaufvorgang bei zu wenig Schrott, Inventar-Obergrenze, Nachschubzähler, Speichern/Laden, Reichweitenberechnung.

**Zwei Werkzeuge, die du gleich mitnimmst:**

```python
@pytest.mark.parametrize("angriff,panzerung,erwartet", [
    (10, 0, 10), (10, 5, 5), (1, 99, 0),
])
def test_schaden(angriff, panzerung, erwartet):
    assert berechne_schaden(angriff, panzerung) == erwartet

def test_speichern(tmp_path):      # tmp_path ist eine Fixture: ein Wegwerf-Ordner
    ...
```

**Und die gute Nachricht zuerst: Du kennst das schon.** Ein pytest-Test ist eine Funktion mit einem `assert` darin — genau den `assert`-Zeilen, die du seit Etappe 7 schreibst. Neu ist nicht das Prüfen, neu ist nur der Rahmen: eine eigene Datei, ein Befehl, der alle Prüfungen auf einmal laufen lässt, und eine Ausgabe, die dir sagt, welche gebrochen ist. Wer Etappe 7 ernst genommen hat, lernt hier ein Werkzeug und kein Konzept.

`parametrize` ersetzt zehn fast gleiche Tests durch einen — genau der Fall deiner Schadensformel. **Fixtures** sind vorbereitete Zutaten, die pytest deinem Test übergibt; `tmp_path` ist die nützlichste davon.

**Und hier zahlt Etappe 17:** Ein Wellengenerator mit Zufall ist untestbar — außer du setzt den Seed. `random.seed(42)` am Testanfang macht aus „irgendwas mit ungefähr dem richtigen Budget" eine prüfbare Aussage. Das ist der Grund, warum der Seed damals im Lehrplan stand.

**Und hier schließt sich der Kreis zum übergreifenden Prinzip:** Tests sind das, was „erweitern ohne zu zerstören" von einer Hoffnung in eine Gewissheit verwandelt. Beim ersten Test, der einen Fehler findet, den du nicht bemerkt hattest, verstehst du das körperlich.

**Bug-Jagd III, umgekehrt:** Ich baue einen Fehler ein, und du schreibst zuerst einen Test, der ihn *nachweist*, bevor du ihn behebst.

**🧠 Entwicklerfrage:** *Was beweist ein grüner Test eigentlich?* Deine Prüffunktion aus Etappe 25 hat einen Test, und der ist grün. Heißt das, die Prüfung funktioniert — oder nur, dass sie bei diesem einen Fall funktioniert? Eine Validierung, die nichts findet, sieht genauso aus wie eine, die nicht läuft. Wie unterscheidest du die beiden?

**Commit:** `Etappe 26: Tests`

---

## Etappe 27 — Fremden Code lesen ⭐⭐

**Kein neues Python. Der Zweck des ganzen Lehrplans.**

Bis hierher hast du ein Spiel gebaut. Das war der Köder. Das eigentliche Ziel stand auf der ersten Seite: **fremden Python-Code lesen und beurteilen können, statt ihm zu vertrauen.** Diese Etappe ist die Probe darauf.

**Was du baust:** Kein Code. Ein Dokument.

Such dir ein echtes, veröffentlichtes Python-Repository — nicht zu groß, ein paar tausend Zeilen. Eine kleine Spielebibliothek, ein Werkzeug, das du benutzt, oder eines deiner eigenen KI-generierten Projekte, das du nie verstanden hast. Und dann schreib **ohne Hilfe** eine Architekturbeschreibung:

1. Was tut dieses Projekt, in drei Sätzen?
2. Wo ist der Einstiegspunkt? Was passiert beim Start, der Reihe nach?
3. Welche fünf Dateien sind die wichtigsten, und warum?
4. Welche Objekte gibt es zur Laufzeit, und wer besitzt wen?
5. Welche externen Abhängigkeiten gibt es?
6. Wo würdest du eine neue Funktion einbauen, und warum genau dort?
7. **Was hältst du für die schwächste Stelle?**

**Frage 7 ist die eigentliche.** Bis hierher warst du Konsument von Code. Sie zu beantworten heißt, ein Urteil zu haben.

Und sie ist nicht neu: Es ist Frage 6 der Leseleiter, seit Etappe 23 geübt, jetzt auf ein ganzes Repository angewendet. Dein Werkzeug dafür ist das Kopplungs-Bild aus Etappe 23 — wer kennt wen, und wo geht das in beide Richtungen. Die schwächste Stelle eines Projekts liegt fast nie in einer einzelnen Funktion, sondern zwischen zweien, die zu viel voneinander wissen.

**Fang bei `pyproject.toml` an.** Das ist der schnellste Einstieg in ein unbekanntes Repo: Projektname, Python-Version, sämtliche Abhängigkeiten — und unter `[project.scripts]` oft direkt den Einstiegspunkt. Drei Minuten Lesen ersparen dir zehn Minuten Suchen.

Was du daraus schon ablesen kannst, bevor du eine Zeile Code siehst: Hängt das Projekt am Netz (`requests`, `httpx`)? Rechnet es viel (`numpy`)? Hat es eine Oberfläche (`pygame`, `flask`)? Die Abhängigkeitsliste ist eine Inhaltsangabe.

**Dein Werkzeugkasten — alles längst gelernt:**
- `print(paket.__file__)` zeigt dir, wo ein installiertes Paket liegt
- F12 im Editor springt in fremden Code hinein („Go to Definition")
- `help(objekt)` und `dir(objekt)` fragen ein Objekt, was es kann
- `git log --oneline` verrät, was zuletzt angefasst wurde
- Der Debugger aus Etappe 8 mit einem Breakpoint an der ersten Zeile
- Die Importe von oben nach unten lesen — sie sind das Inhaltsverzeichnis
- `pyproject.toml` oder `requirements.txt` als Inhaltsangabe

**Die Erkenntnis, auf die es ankommt:** Fremder Code ist kein Zauber und keine Blackbox. Es ist Python, von Menschen geschrieben, meistens schlechter dokumentiert als deiner. Du darfst da hineinschauen — und du kannst es jetzt.

**Lernziele:**
- Wie findest du in einem unbekannten Projekt den Einstiegspunkt?
- Woran erkennst du, was öffentlich gemeint ist und was interner Kram? (Stichwort: führender Unterstrich)
- Wie findest du heraus, welche Argumente eine Funktion erwartet, wenn die Doku schweigt?
- Was sagt dir die Ordnerstruktur eines Projekts, bevor du eine Zeile liest?

---

### Der zweite Teil — die eigentliche Prüfung

Wenn die Architekturbeschreibung steht, kommt der Test, für den dieser ganze Plan gebaut wurde. Dein Mentor gibt dir **etwa fünfhundert Zeilen KI-generierten Python-Code** — am besten aus einem deiner eigenen Projekte, das du nie verstanden hast.

Fünf Schritte, in dieser Reihenfolge:

1. **Beschreib die Architektur.** Was tut das, wer besitzt wen, wo ist der Einstieg?
2. **Nenn drei Risiken.** Wo ist Kopplung? Wo werden Fehler verschluckt? Wo steckt eine Annahme, die niemand hingeschrieben hat? Nutz die Warnsignale.
3. **Markier drei Stellen, die du nicht verstehst.** Ehrlich. Das ist der wertvollste Teil, und der, den man am liebsten überspringt.
4. **Wähl eine davon** und beschreib, *wie* du sie untersuchen würdest — welches Werkzeug, welcher Breakpoint, welche Ausgabe.
5. **Erst jetzt darfst du den Code ausführen.** Und dann vergleichst du, was du vermutet hast, mit dem, was passiert.

**Schritt 5 kommt zuletzt, und das ist kein Schikane.** Ausführen ist der bequemste Weg zu einem Ergebnis und der schlechteste zu einem Verständnis: Man sieht, *was* passiert, und hält das für eine Erklärung, *warum*. Wer erst liest und dann ausführt, prüft sein Modell. Wer erst ausführt, baut nie eines.

Das ist dasselbe Ritual wie in Etappe 1 beim Kaputtmachen — Vorhersagen, Ausführen, Vergleichen, Erklären. Nur dass es hier auf fünfhundert Zeilen fremden Code angewendet wird, die du vor sechs Monaten nicht einmal geöffnet hättest.

---

**Dann sprechen wir darüber.** Nicht als Prüfung — sondern weil das ab hier die Form ist, in der über Code geredet wird. Du bringst eine Lesart mit, dein Mentor widerspricht, wo er anderer Meinung ist.

**Und ab hier gilt eine neue Arbeitsregel:** Wenn du beim Vibe Coding Code bekommst, den du nicht verstehst, ist das ab sofort ein Problem der Erklärung und nicht deines Könnens. Frag nach. Du hast jetzt die Begriffe dafür.

**🧠 Die letzte Entwicklerfrage:** *Woran erkennst du, dass jemand über seinen Code nachgedacht hat?* Nicht ob er gut ist — ob jemand nachgedacht hat. Deine Antwort auf diese Frage ist die Summe von allem, was in diesem Plan stand, und sie ist der Grund, warum du ihn durchgezogen hast.

**Commit:** `Etappe 27: Ich kann fremden Code lesen`

Damit ist das Kernprogramm abgeschlossen.

---

# BLOCK 4 — Grafik

*Optional. Erst starten, wenn Block 1–3 stehen — aber dann mit gutem Gewissen: Das hier ist der Nachtisch. Und in diesem Setting ist es ein besonders naheliegender, weil ein Verteidigungsspiel gesehen werden will.*

## Etappe 28 — Das Spiel läuft von selbst

Fenster, Spielschleife mit Bildrate, ein Rechteck mit Pfeiltasten.

**Der eigentliche Umbruch ist nicht die Grafik, sondern der Kontrollfluss.** Bisher wartete dein Spiel auf dich: Du gibst einen Befehl, es tickt einmal, es zeigt dir das Ergebnis. Ab heute läuft es weiter, ob du etwas tust oder nicht:

```
Spielschleife
    ↓
Eingabe entgegennehmen
    ↓
Tick
    ↓
zeichnen
    ↓
von vorn, 60-mal pro Sekunde
```

**Und genau hier bekommt eine Entscheidung aus Etappe 13 ihren Zahltag.** Damals hast du Tick-Zeit statt Echtzeit gewählt und es fühlte sich nach einem Kompromiss an. Jetzt *ist* ein Tick eine Zeiteinheit: `bauzeit = 180` sind exakt drei Sekunden. Ohne eine Zeile neue Bau-Logik.

**Entscheidend:** Deine gesamte Logik bleibt unverändert. Pygame ist nur eine neue *Darstellung*. Wenn du sauber gearbeitet hast — insbesondere bei der `return`-statt-`print`-Entscheidung aus Etappe 7 — fasst du `welt.py` fast nicht an. Das ist der Beweis, dass die Architektur stimmt.

Wenn du an dieser Stelle merkst, dass du `welt.py` kaum anfassen musst, ist das der beste Beweis für die Qualität deiner Arbeit, den dieses Projekt zu bieten hat.

## Etappe 29 — Kacheln, Sprites, Kamera

Aus Zeichen werden Kacheln. Und weil deine Darstellung seit Etappe 7 eine eigene Schicht ist, tauschst du hier eine Schicht aus und schreibst kein Spiel neu: Wo `zeichne_vorfeld()` bisher `#` und `.` ausgegeben hat, zeichnet sie jetzt Bilder. Die Logik darunter merkt davon nichts.

Tilemap für das Vorfeld, animierte Einheiten, eine Kamera, die dem Geschehen folgt. Dein Vorfeld aus Etappe 14 ist bereits im richtigen Format — genau dafür wurde es damals als Raster und nicht als Dictionary gebaut.

## Etappe 30 — Isometrie

Umrechnung von Raster- auf Bildschirmkoordinaten, Zeichenreihenfolge nach Tiefe. Mathematisch der anspruchsvollste Teil — und die Ansicht, für die dieses Spiel von Anfang an gedacht war. Zu diesem Zeitpunkt bist du ein anderer Programmierer als heute.

---

## Was bewusst nicht drinsteht

Ein Lehrplan wird nicht dadurch besser, dass mehr darin steht. Diese Themen fehlen mit Absicht:

**Generatoren und `yield`, `async`/`await`, Metaklassen, Deskriptoren, funktionale Programmierung, Design Patterns als Theorieblock.** Alle sind echtes Python, keines davon brauchst du für dieses Spiel, und jedes würde bei 20–30 Minuten am Tag eine Woche kosten. *(`async` und Nebenläufigkeit stehen in der `advanced/`-Reihe — dort, wo dein Spiel sie tatsächlich braucht, und nicht vorher.)*

**Ausnahme, und die nenne ich, weil sie sonst wie ein Versehen aussieht: Dekoratoren bleiben drin** (Etappe 23), obwohl sie in dieselbe Liste gehören würden. Der Grund ist, dass sie nicht optional sind: `@dataclass`, `@property` und `@pytest.fixture` stehen in deinem eigenen Code, und zwar in genau diesem Plan. Du sollst keine schreiben. Du sollst wissen, dass die Zeile darunter durch die Zeile darüber hindurchgereicht wird — mehr nicht.

**Und tiefere Git-Theorie** — Rebase, Cherry-Pick, Reflog. Das ist kein Python, und es lernt sich in dem Moment am besten, in dem man es das erste Mal wirklich braucht.

---

## Warum hier Schluss ist

Der Bogen steht: Grundlagen → Datenstrukturen → Funktionen → Debugging → OOP → Komposition → Vererbung → Zeit und Zustand → Dateien → Fehlerbehandlung → Zustandsmodellierung → datengetriebenes Design → modernes Python → Module → Tests → **fremden Code lesen** → Grafik.

Weitere Themen hineinzupressen würde den Plan verbessern und das Projekt verschlechtern. Ab Etappe 17 ist er bewusst grob — und das ist keine Lücke, sondern die eigentliche Absicht.

Denn wenn du an diesem Punkt sagst:

> *„Ich glaube, meine Datenstruktur ist falsch."*
> *„Warum brauche ich diese Klasse eigentlich?"*
> *„Hier hängt zu viel voneinander ab."*

…dann ist dieses Problem selbst die nächste Lektion. Und dann brauchst du keinen Lehrplan mehr.

---

## Was du am Ende hast

Ein spielbares Verteidigungsspiel: vier Klassen, ein Vorposten mit Sektoren, ein Depot, Geschütze mit Bauzeit, Rekruten, die nachkommen, zwanzig erzeugte Wellen, Ereignisse, Statuseffekte, Speicherstände — und ein Kern, der fällt, wenn du zu langsam bist.

Dazu ein öffentliches Repo mit hunderten Commits. Und der eigentliche Punkt: Du wirst fremden Python-Code lesen und beurteilen können, statt ihm zu vertrauen.

---

## So arbeiten wir

Bring mir pro Etappe:
1. Was du bauen willst, in eigenen Worten
2. Deinen Code
3. Was nicht klappt

Ich gebe Hinweise, Erklärungen, Reviews. Wenn du nach fertigem Code fragst, frage ich zurück, was du schon probiert hast.

**Ich nehme die Lernziele ernst.** Wenn du sagst „Etappe 5 ist fertig", frage ich dich die Fragen. Nicht als Prüfung — das Erklären *ist* der Lernvorgang. Du lernst am besten, wenn du etwas selbst machen und wiederholen musst: Die Transferaufgaben sind das Machen, die Lernziele das Wiederholen, die Leseübungen das, was am Ende zählt.

An Tagen ohne Energie: `GELERNT.md` öffnen, die letzten drei Einträge lesen. Das zählt auch.

---

## Was sich in Fassung 3 geändert hat

Keine Etappe wurde hinzugefügt, keine gestrichen, keine umnummeriert — die Themenliste und alle Verweise sind unverändert. Geändert wurde die **Belastungssteuerung**.

**Das neue tragende Prinzip: die drei Anspruchsstufen.** 🔨 Bauen · 🧠 Verstehen · 👀 Nur erkennen. Fast jede Etappe beginnt jetzt mit dieser Tabelle. Sie ist das Mittel gegen den einen Fehler, an dem Selbstlernprojekte scheitern: alles gleich wichtig zu nehmen.

**Sieben Etappen sind geteilt**, mit Commit dazwischen — 3, 7, 9, 14, 17, 21, 23. **Etappe 3 dreifach** (Schleife / Befehle / Kampf und Anzeige), die übrigen zweifach. Aus 30 Etappen werden 38 Portionen, ohne dass eine einzige Nummer sich verschiebt.

**Herabgestuft auf „nur erkennen":** `continue` (3a) · `__str__` (9b) · Dunder-Methoden und `@property` (11) · der Begriff *Zustandsautomat* und die Tick-Reihenfolge (12) · *Scheduler* (13) · `enumerate()` (14a) · *Kopplung* (15) · `and`/`or` als Rückgabewerte (18) · atomares Schreiben (19) · Exception-Hierarchien und `finally` (20) · Schadenstypen (21b) · Komposition (22).

**Entlastet und neu geordnet:**

| Was | Wo |
|---|---|
| `int()` als Dreisatz statt als Klassen-Stats-Kopplung | 1 |
| Nur noch die **gewählte** Klasse wird gesetzt — der Trupp kommt in 11 | 2 |
| Anmarschbahn in drei Schritten: ein Gegner → mehrere → entfernen | 4 |
| Dictionary zuerst an einem Nicht-Spiel-Beispiel erklärt | 5 |
| Tuple ohne Koordinaten-Vorgriff begründet | 6 |
| `assert` ist Ausblick, nicht Testeinstieg | 7b |
| Objektidentität („zwei Namen, ein Objekt") explizit gemacht | 10 |
| Zustandsautomat auf zwei Zeilen mit String reduziert | 12 |
| Wegfindung ausdrücklich ausgeschlossen | 14a |
| Sensorabdeckung als Kür markiert | 14b |
| Set-Muster (merken → abfragen) als Kern herausgestellt | 15 |
| Ereignisse und Seed von der Zufallsmechanik getrennt | 17b |
| Eine Exception-Klasse statt einer Hierarchie | 20 |
| Ausbaubaum als Voraussetzungsfeld statt als „Graph" | 22 |
| Die Spielschleife als eigentlicher Umbruch, nicht die Grafik | 28 |

**Nicht übernommen:** eine Umnummerierung von 24–30 (bricht sämtliche Vorausverweise, den Bogen und alle bestehenden Guides, ohne didaktischen Gewinn — die a/b-Teilung leistet dasselbe) und jede Form von zusätzlichem Python-Stoff. Der Plan sollte lernbarer werden, nicht länger.

---

## Was sich in Fassung 2 geändert hat

Für alle, die Fassung 1 kennen. Keine Etappe wurde hinzugefügt, keine gestrichen, keine umnummeriert — die Themenliste ist unverändert. Geändert wurde die Didaktik:

| Neu | Wo |
|---|---|
| Lesehinweis und Mindestsitzung | ganz vorne |
| Meilensteine und „an Tagen, an denen nichts geht" | Zeitrahmen |
| 🧠 Die Entwicklerfrage — eine echte Entscheidungsfrage je Etappe | Rahmenteil, eingelöst in 17–27 |
| Beobachtung → Hypothese → Experiment als Debugging-Formular | Bug-Jagd, angewandt in 16 |
| Anspruchsstufen für überladene Etappen | 11, 18, 23 |
| Etappe 23 in zwei Hälften (23a lesen / 23b modellieren) mit Commit dazwischen | 23 |
| Tick-Reihenfolge als bewusste Entscheidung, nicht als Zufall | 12, eingelöst in 16 |
| Komposition als dritte Option neben Daten und Vererbung | 11 angekündigt, 22 ausgeführt |
| Riegel gegen Wegfindung | 14 |
| Kopplungs-Zeichnung als eigene Übung | 15, wiederholt in 23 |
| Seed als sichtbare Entwicklerfunktion | 17 |
| Serialisierung als Abbildung — und die Frage, ob sie verlustfrei ist | 19 |
| Drei Stufen der Gültigkeit (syntaktisch / strukturell / inhaltlich) | 25 |
| Commit-Zeile für jede Etappe | durchgehend |

**Entschärft** wurden absolute Formulierungen an sechs Stellen — beim Objektzähler gegen Scheduler (13), bei Vererbung gegen Komposition (11), bei `Enum` gegen String (21) und bei `finally` (20), das eben *nicht* immer läuft. **Gestrichen** wurden Pull Requests als Pflichtstoff (24).

**Was bewusst nicht übernommen wurde:** eine Rubrik „Am Ende kannst du…" je Etappe (Selbstbild statt Prüfung — siehe *Die Struktur jeder Etappe*) und jede Form von zusätzlichem Python-Stoff. Der Plan sollte tiefer werden, nicht länger.
