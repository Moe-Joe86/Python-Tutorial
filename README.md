# Python lernen, indem ein Spiel wächst

**Ein Tutorial in 30 Etappen. Du baust ein textbasiertes Survival-Spiel — und eine KI begleitet dich dabei als Mentor, der dir nicht die Lösung verrät.**

> 🇬🇧 **English:** This is a German-language Python curriculum. You learn Python by building a text-based survival game over 30 stages, guided by an AI mentor that is explicitly instructed never to write the code for you. All materials are in German — an English version does not exist yet.

**Status:** **In Arbeit.** Der Lehrplan steht vollständig, die ausführlichen Guides entstehen noch Etappe für Etappe.


---

## Was das hier ist und warum es das hier gibt

Ich habe schon häufiger versucht Python zu lernen, aber mein innerer Schweinehund hat mich jedes mal besiegt. Alle Lernportale oder Bücher die ich gefunden habe, haben neue Python-Werkzeuge an trockenen Übungen gezeigt, welche selten einen Zusammenhang hatten oder geschweige denn ein übergeortnetes großes Ziel verfolgt hätten. Und am Ende war ich immer noch nicht in der Lage diese Werkzeuge gemeinsam zu benutzen, um damit selbst etwas zu bauen. 
Dazu kam, dass man bis vor wenigen Jahren jede Information/Frage oft mühselig im Internet recherchieren musste. Dadurch habe ich zur Klärung einfacher Sachverhalte manchmal viel Zeit vergeudet, was die Motivation zusätztlich geschmälert hat. Mittlerweile kann man mit KI jedoch flexibel über seinen Code sprechen, Fragen stellen und bekommt innerhalb von Sekunden präzise Antworten. Genau hier setzt dieser Kurs an.

Die meisten Python-Kurse lassen dich Übungsaufgaben lösen, die du nach zwei Wochen vergessen hast. Dieses Tutorial macht etwas anderes: **Jede gelernte Fähigkeit landet sofort in einem Spiel, das dir gehört und das jeden Tag ein Stück größer wird.**

Du lernst Listen und baust ein Inventar. Du lernst Dictionaries und baust ein Depot. Du lernst Klassen und deine Mitstreiter bekommen ein Eigenleben. Schon früh kannst du mit deinem eigenen Spiel etwas ausprobieren und sehen, was dein neuer Code bewirkt und über die Monate wächst daraus Schritt für Schritt ein echtes System.

Und vor allem: **Du arbeitest nicht allein, sondern mit einer KI als Mentor.** Die KI bekommt eine Anweisungsdatei, die ihr ausdrücklich verbietet, dir den Code zu schreiben. Sie stellt Rückfragen, gibt Hinweise, prüft dein Verständnis und lässt dich jede Zeile selbst tippen.

---

## Für wen das gedacht ist

**Gut geeignet, wenn du…**
- Python lernen willst, aber bei abstrakten Übungsaufgaben die Motivation verlierst
- mit KI-generiertem Code arbeitest möchtest und aufhören willst, ihm blind zu vertrauen
- 20–30 Minuten am Tag hast und einen langen Atem
- Freude daran hast, wenn ein System vor deinen Augen wächst

**Nicht geeignet, wenn du…**
- in zwei Wochen einen Job als Entwickler brauchst
- eine reine Syntax-Referenz suchst (das hier ist die *Anwendung*, nicht die Einführung)
- schnell ein fertiges Spiel willst — dann nimm eine Engine, nicht dieses Tutorial

Das Tutorial behandelt dich nicht wie einen Computer-Anfänger. Dinge wie die Einrichtung und Nutzung von Python, IDE(VS Code) und Github werden in Grundzügen vorausgesetzt.

---

## Die Prämisse

Ein Vorposten auf einem Mond, den niemand mehr besucht. Der Reaktorkern hält die Kuppel. Das Evakuierungsschiff kommt in **zwanzig Wellen** — so lange musst du durchhalten.

Draußen ist die Brut. Sie kommt in Wellen, und sie wird jedes Mal größer.

Du steuerst einen von vier Marines — Soldat, Heavy, Engineer, Medic —, während drei weitere programmgesteuert mitkämpfen. Dazwischen: Wellen überstehen, Material bergen und verkaufen, im Depot ausrüsten, den Kern halten. Jede Klasse ist technisch an einem anderen Konzept verankert, und alle vier existieren im Code von Anfang an — auch die, die du gerade nicht spielst.

Das Setting ist bewusst schlank gehalten: wenig Weltenbau nötig, dafür maximaler Raum für das, worum es eigentlich geht: Python-Werkzeuge und Syntax.

---

## Wie es funktioniert

Das hier ist der Kern, und er unterscheidet dieses Tutorial von allen anderem.

**1. Du gibst einer KI die Mentor-Anweisung.**

Lade das Repo herunter und gib der KI deiner Wahl (Claude, ChatGPT, Gemini …) diese vier Dateien:

- `MENTOR.md` — die Regeln, nach denen sie dich begleitet
- `Vorposten_Lehrplan.md` — der Überblick über alle 30 Etappen
- `BOGEN.md` — das Register aller Querverweise
- `SYNTAX.md` — das Register, welches Sprachwerkzeug wann eingeführt wurde

Bei Claude legst du sie als Projektdateien ab, bei anderen Anbietern als Anweisung oder angehängtes Dokument. Dann schreibst du einfach:

> „Begleite mich durch dieses Tutorial. Ich fange bei Etappe 0 an."

**2. Die KI hält sich zurück — und das ist Absicht.**

`MENTOR.md` verbietet ihr, Code für dein Spiel zu schreiben. Stattdessen arbeitet sie eine Hinweis-Leiter ab: erst Rückfragen, dann auf die Stelle zeigen, dann das Konzept an einem *fremden* Beispiel erklären. Die Lösung bekommst du nicht.

Das ist unbequem. Es ist auch der einzige Weg, auf dem etwas hängen bleibt.

**3. Du arbeitest Etappe für Etappe.**

Jede Etappe hat denselben Aufbau: ein Konzept lernen, es im Spiel anwenden, eine kleine Übung außerhalb des Spiels, absichtlich etwas kaputtmachen — und am Ende erklären, was du verstanden hast. Erst dann gilt sie als abgeschlossen.

**4. Die KI prüft dich.**

Wenn du sagst „fertig", stellt sie dir die Lernziel-Fragen der Etappe. Nicht als Prüfung — das Erklären *ist* der Lernvorgang. Wer eine Sache in eigenen Worten erklären kann, hat sie verstanden. Wer sie nur benutzen kann, erinnert sich an seinen eigenen Code.

---

## Schnellstart

```bash
git clone https://github.com/Moe-Joe86/Python-Tutorial.git
```

1. **Lies** `Vorposten_Lehrplan.md` — einmal ganz, damit du den Bogen kennst.
2. **Übergib** `MENTOR.md`, `Vorposten_Lehrplan.md`, `BOGEN.md` und `SYNTAX.md` an deine KI.
3. **Leg dein eigenes Repo an** — das Spiel gehört dir, nicht hierher.
4. **Starte mit Etappe 0.** Ein Abend, kein Python: Repo, `README.md`, `GELERNT.md`, `.gitignore`, virtuelle Umgebung.
5. **Dann Etappe 1.** Am Ende des Abends existiert dein Spiel.

Die ausführlichen Etappen-Guides gibst du der KI einzeln dazu, wenn du sie erreichst. Das hält den Kontext schlank.

---

## Was du brauchst

| | |
|---|---|
| **Python 3.10+** | Installiert und im Terminal aufrufbar |
| **Ein Editor** | VS Code (+Python-Plugin) empfohlen, aber beliebig |
| **Git & GitHub** | Ein kostenloses Konto reicht |
| **Eine KI** | Claude, ChatGPT, Gemini o. ä. |
| **Zeit** | 20–30 Minuten am Tag, über Monate |

**Empfohlen zusätzlich:** eine strukturierte Syntax-Quelle. Der Lehrplan ist auf [Boot.dev](https://boot.dev) abgestimmt, funktioniert aber mit jeder Quelle, die dieselben Themen in ähnlicher Reihenfolge behandelt — auch mit kostenlosen wie freeCodeCamp. Dieses Tutorial ersetzt keine Syntax-Einführung. Es ist die Anwendung dazu.

---

## Die Grundsätze

**Kein Vibe Coding.** Du schreibst jede Zeile selbst. Wenn du feststeckst, formulierst du es so: *„Ich will X, habe Y probiert, es passiert Z — woran könnte es liegen?"* Nicht: *„Schreib mir das."*

**Erst kaputt machen, dann fragen.** Wenn etwas funktioniert, änderst du absichtlich etwas und schaust zu. „So schreibt man es" ist Auswendiglernen. „Warum muss es so sein" ist Verstehen.

**Das Spiel läuft ab Etappe 1.** Erst hässlich und textbasiert, aber spielbar. Jede Etappe macht es größer, nicht hübscher.

**Grafik kommt zum Schluss.** Wellenlogik, Ökonomie, Fortschritt — alles reine Logik, kein Pixel nötig. Wer mit Sprites anfängt, kämpft ein halbes Jahr mit Kollisionsabfragen und baut nie das, was ihn eigentlich interessiert hat. Grafik kommt ab Etappe 28.

**Erweitern, ohne zu zerstören.** Spätestens ab Block 2 der Maßstab für alles. Programmieren heißt nicht nur, neuen Code zu schreiben — sondern bestehenden zu verstehen und vorsichtig zu verändern.

---

## Zeitrahmen — ehrlich

| Block | Etappen | Dauer |
|---|---|---|
| Werkzeug | 0 | 1 Abend |
| Fundament | 1–8 | 9–12 Wochen |
| Einheiten und Zeit | 9–16 | 10–13 Wochen |
| Der Vorposten reagiert | 17–27 | 14–18 Wochen |
| Grafik (optional) | 28–30 | offen |

Bei 20–30 Minuten am Tag. Das ist kein Wochenendprojekt.

---

## Was am Ende dasteht

Ein spielbares Survival-Spiel: ein Vorposten, der zwanzig Wellen einer immer größer werdenden Bedrohung übersteht, eine Ökonomie aus Beute, Depot und Ausbau, ein Trupp mit eigenem Verhalten — und ein System, das du komplett selbst gebaut und mehrfach umgebaut hast.

Dazu ein öffentliches Repo mit hunderten Commits über Monate. Das ist ein besserer Nachweis für Durchhaltevermögen als jedes Kurszertifikat.

Und der eigentliche Punkt: **Du wirst fremden Python-Code lesen und beurteilen können, statt ihm zu vertrauen.**

---

## Ehrliche Einschränkungen

**Es ist noch nicht fertig.** Der Lehrplan steht, die ausführlichen Etappen-Guides entstehen nach und nach. Bis dahin trägt der Lehrplan die späteren Etappen — knapper, aber vollständig.

**Es hängt an der KI.** Die Qualität der Begleitung schwankt je nach Modell. `MENTOR.md` ist so geschrieben, dass es robust sein sollte, aber keine KI hält sich perfekt an Anweisungen. Wenn deine KI anfängt, dir Lösungen hinzuschreiben, erinnere sie an `MENTOR.md`.

**Es ersetzt keinen Kurs.** Die Syntax lernst du woanders. Hier lernst du, sie zu benutzen.

**Es ist ein Lernprojekt, kein Spieleentwicklungs-Tutorial.** Wenn du ein kommerzielles Spiel bauen willst, ist eine Engine der schnellere Weg.

---

## Mitwirken

Wenn du das Tutorial durchläufst und über eine unklare Stelle stolperst, ist ein Issue hilfreich. Besonders wertvoll: Stellen, an denen du feststeckst und der Guide dir nicht weiterhilft — das sind die Lücken, die man von innen nicht sieht.

---

## Lizenz

MIT — siehe [LICENSE](LICENSE). Nutz es, verändere es, gib es weiter.
