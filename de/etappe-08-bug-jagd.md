# Etappe 8 — Bug-Jagd I ⭐

> **Block 1: Fundament** · Etappe 8 von 29 · [← Etappe 7](etappe-07-aufraeumen.md) · [Lehrplan](../RPG_Lehrplan.md) · [Etappe 9 →](etappe-09-alles-wird-zum-objekt.md)

**Boot.dev:** Kein neues Thema. Eine eigenständige Fähigkeit.
**Zeitaufwand:** 3–5 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 7 abgeschlossen, Spiel läuft in Funktionen

---

## Worum es geht

Bisher waren Fehler etwas, das dir passiert ist. Heute werden sie zu etwas, das du **jagst**.

Das ist keine Wortspielerei, sondern ein anderer Umgang mit derselben Sache. Wenn ein Fehler dir passiert, wartest du auf eine Fehlermeldung und hoffst, dass sie dir sagt, was los ist. Wenn du ihn jagst, hast du eine Methode: Du grenzt ein, stellst Hypothesen auf, prüfst sie, und der Suchraum wird mit jedem Schritt kleiner.

**Warum das eine eigene Etappe verdient:** Debugging wird in fast keinem Kurs unterrichtet. Man lernt, wie man Code schreibt, und geht stillschweigend davon aus, dass Fehlersuche sich dabei nebenbei einstellt. Tut sie nicht. Es ist eine eigenständige Fähigkeit mit eigenen Werkzeugen und einer eigenen Denkweise, und wer sie nicht bewusst lernt, verbringt Jahre damit, `print()` an zufällige Stellen zu streuen.

**Und für dein eigentliches Ziel ist sie die wichtigste Etappe des ersten Blocks.** Wenn dir irgendwann vierhundert Zeilen Code vorliegen, die du nicht selbst geschrieben hast, und irgendetwas daran funktioniert nicht — dann nützt dir kein auswendig gelerntes Syntaxdetail. Dann brauchst du genau das hier: **eingrenzen und präzise beschreiben können.**

Heute lernst du also kein Python. Du lernst, was man mit Python tut, wenn es nicht tut, was es soll.

**Eine Sache noch:** Diese Etappe ist die erste, in der du deinen Code jemand anderem gibst, damit er ihn kaputtmacht. Das fühlt sich unangenehm an. Es ist auch das erste Mal, dass du erlebst, wie ein Fehler aussieht, den *nicht du* gemacht hast — und das ist ein wichtiger Unterschied. Bei eigenen Fehlern hilft die Erinnerung. Bei fremden hilft nur die Methode.

---

## Der lange Bogen

| Was du heute baust | Wo es wieder auftaucht |
|---|---|
| Die drei Fehlertypen als Denkraster | **Etappe 20** — `except:` verwandelt Typ 1 in Typ 3; **Etappe 21** — `"kamfp"` gegen `GameState.KAMFP` |
| Tracebacks von unten nach oben lesen | durchgehend — bis Etappe 29 dein häufigstes Werkzeug |
| Der Debugger | **Etappe 12** — den Tick Schritt für Schritt beobachten; **Etappe 14** — Bewegung im Raster |
| Ursache und Symptom trennen | **Etappe 16** — dort liegen sie noch weiter auseinander |
| Halbieren als Suchverfahren | **Etappe 24** — welches Modul ist schuld |
| Dein schriftliches Debugging-Protokoll | **Etappe 16** — du liest es nach und schärfst es |
| Einen Fehler präzise beschreiben | **Etappe 23** — dieselbe Fähigkeit bei fremdem Code |
| Das Fehlertagebuch | **Etappe 26** — jeder Eintrag ist ein möglicher Testfall |
| `git diff` als Werkzeug | **Etappe 24** — dort mit Branches |
| Funktionen einzeln aufrufen | **Etappe 26** — dasselbe, dann automatisch |

**Zwei Schulden werden heute eingelöst:**

Aus **Etappe 2**: dort stand, `print()`-Debugging sei *die primitivste Form* und in Etappe 8 lernst du die bessere. Hier ist sie — und du lernst gleichzeitig, wann die primitive trotzdem die richtige ist.

Aus **Etappe 7**: das Einzelaufrufen von Funktionen. Damals war es ein Nebeneffekt des Refactorings. Heute wird es zum Verfahren.

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

Diese Etappe baut kein Spielfeature. Was du heute anlegst, ist ein **Dokument** — und wie es aussieht, entscheidest du.

### Frage 1: Wo führst du dein Fehlertagebuch?

Ab heute notierst du Fehler, die dich mehr als zehn Minuten gekostet haben. Nicht alle — nur die, bei denen du dich geärgert hast.

Zwei Möglichkeiten: ein eigener Abschnitt in `GELERNT.md`, oder eine eigene Datei `FEHLER.md` im Repo. Bei einem Projekt über sechs Monate wird der Abschnitt lang; eine eigene Datei bleibt übersichtlicher.

**Und was hineinkommt, ist wichtiger als wo.** Pro Eintrag drei Zeilen:

```text
Symptom:  Was habe ich gesehen?
Ursache:  Was war tatsächlich falsch?
Gefunden: Wie bin ich draufgekommen?
```

**Die dritte Zeile ist die entscheidende.** Was der Fehler war, vergisst du und brauchst es nie wieder. Wie du ihn gefunden hast, ist übertragbar — und nach zwanzig Einträgen siehst du dein eigenes Muster: welche Verfahren bei dir funktionieren und an welcher Stelle du regelmäßig zu lange herumrätst.

In Etappe 26 hat das noch einen zweiten Nutzen: Jeder Eintrag im Tagebuch ist ein Kandidat für einen Test.

### Frage 2: Debugger oder Terminal?

Du wirst heute beides lernen. Aber du wirst dich mit der Zeit für einen Arbeitsstil entscheiden, und beide sind legitim.

Manche arbeiten fast ausschließlich im Debugger und setzen Breakpoints, sobald etwas hakt. Andere bleiben beim Terminal und schreiben gezielte Ausgaben. Es gibt hier keine richtige Antwort — nur eine falsche, nämlich das Werkzeug gar nicht zu kennen und deshalb immer dasselbe zu benutzen.

Probier heute beide ehrlich aus. Notier am Ende in `GELERNT.md`, welches dir lag und warum.

---

## Die Konzepte

### 1. Die drei Fehlertypen

Alles, was schiefgehen kann, fällt in eine von drei Klassen. Die Reihenfolge ist nach Schwierigkeit sortiert.

**Typ 1 — stürzt sofort ab.**
Du startest, es knallt, du bekommst einen Traceback mit Zeilennummer. Unangenehm, aber ehrlich: Python sagt dir, wo es aufgehört hat.

**Typ 2 — stürzt manchmal ab.**
Läuft meistens. Aber wenn der Spieler `gehe` ohne Richtung tippt, oder wenn das Inventar leer ist, oder beim zwölften Durchlauf — dann knallt es. Schwerer, weil du erst die Bedingung finden musst, unter der es passiert.

**Typ 3 — stürzt nie ab und liefert das Falsche.**
Keine Fehlermeldung. Keine Zeilennummer. Das Programm läuft freundlich weiter und tut etwas anderes, als du wolltest. Der Rundenzähler steht immer auf 1. Die erste Ortsbeschreibung erscheint nie. Ein Gegenstand ist plötzlich an zwei Orten.

**Typ 3 ist die gefährlichste Sorte**, und zwar aus einem Grund, der über Programmieren hinausgeht: Er zerstört die schädlichste Überzeugung, die Anfänger haben —

> *„Wenn Python keinen Fehler zeigt, ist mein Programm richtig."*

Das ist schlicht falsch. Python prüft, ob dein Code **ausführbar** ist, nicht ob er **richtig** ist. Diese beiden Fragen haben fast nichts miteinander zu tun.

Du kennst Typ 3 längst, auch wenn er keinen Namen hatte. Das fehlende `f` vor dem String in Etappe 1. Die falsch eingerückte Zeile in Etappe 2. Der Zähler, der in der Schleife zurückgesetzt wird, aus Etappe 3. `inventar = inventar.append(...)` aus Etappe 4. Der stille Tippfehler beim Dictionary-Schlüssel aus Etappe 5.

Jedes Mal lief das Programm. Jedes Mal war es falsch.

### 2. Den Traceback lesen

Ein Traceback sieht abschreckend aus und ist eine der hilfreichsten Ausgaben, die Python macht. Man muss ihn nur richtig herum lesen.

```text
Traceback (most recent call last):
  File "spiel.py", line 214, in <module>
    verarbeite_befehl(eingabe, orte, aktueller_ort, inventar)
  File "spiel.py", line 156, in verarbeite_befehl
    return bewege_spieler(orte, ort, teile[1])
  File "spiel.py", line 98, in bewege_spieler
    ziel = orte[ort]["ausgaenge"][richtung]
KeyError: 'westen'
```

**Von unten nach oben:**

Die **letzte Zeile** sagt, *was* passiert ist: ein `KeyError`, und der gesuchte Schlüssel war `'westen'`.

Die **Zeile direkt darüber** sagt, *wo* es passiert ist: Zeile 98, in `bewege_spieler`, bei genau diesem Zugriff.

Alles **darüber** ist der Weg dorthin — wer wen gerufen hat. Von unten nach oben gelesen: `bewege_spieler` wurde von `verarbeite_befehl` gerufen, und das von der Hauptschleife.

**Der Satz oben ist wörtlich gemeint:** *most recent call last* — der jüngste Aufruf steht unten. Deshalb liest man von unten.

**Und der Weg nach oben ist nicht überflüssig.** Wenn `bewege_spieler` sauber aussieht, ist die interessante Frage: Wer hat sie mit `'westen'` gerufen und warum? Der Traceback zeigt dir die Antwort — seit Etappe 7 hast du überhaupt erst mehrere Ebenen, in denen das sichtbar wird.

**Ein praktischer Hinweis:** Bei einem `SyntaxError` zeigt Python oft auf die Zeile *nach* dem Fehler. Eine vergessene Klammer in Zeile 40 meldet sich in Zeile 41 — weil Python erst dort merkt, dass etwas nicht aufgeht. Wenn die genannte Zeile einwandfrei aussieht, schau eine höher.

### 3. Ursache und Symptom sind nicht dasselbe

Das ist die wichtigste Unterscheidung dieser Etappe.

> **Wo es knallt, ist selten, wo es kaputt ist.**

Im Traceback oben knallt es in Zeile 98, weil `richtung` den Wert `'westen'` hat und der Ort keinen Westausgang. Aber ist Zeile 98 falsch? Vielleicht ist die echte Ursache:

- Die Prüfung mit `in` fehlt, bevor zugegriffen wird → dann ist Zeile 98 die Ursache.
- Der Spieler steht am falschen Ort, weil eine Bewegung vorher nicht sauber war → die Ursache liegt hunderte Zeilen entfernt.
- Deine Ortstabelle hat einen Ausgang, der auf einen Ort ohne Rückweg zeigt → die Ursache steht in den Daten, nicht im Code.

**Die Frage lautet deshalb nie „welche Zeile ist falsch?", sondern:** *Woher kam der Wert, der hier Ärger macht?*

Bei Typ-3-Fehlern gibt es gar keine Absturzstelle, und dann bleibt nur diese Frage. Du arbeitest dich rückwärts: Was hätte hier stehen müssen? Wo wurde es zuletzt gesetzt? Stimmte es dort schon nicht?

### 4. Die Methode: raten ist kein Verfahren

Der häufigste Anfängerfehler beim Debuggen ist **Herumprobieren**: Man ändert etwas, startet, ändert etwas anderes, startet. Manchmal geht es dann. Man weiß nicht warum, und beim nächsten Mal geht es wieder nicht.

Es gibt ein besseres Verfahren, und es ist dasselbe wie in den Naturwissenschaften:

> **1. Beobachten** — was passiert genau? Nicht „es geht nicht", sondern der exakte Ablauf.
> **2. Hypothese** — was könnte die Ursache sein? Eine, nicht fünf.
> **3. Vorhersage** — *wenn* meine Hypothese stimmt, dann müsste bei diesem Test genau das herauskommen.
> **4. Prüfen** — Test ausführen.
> **5. Auswerten** — Vorhersage getroffen? Hypothese hält. Nicht getroffen? Verwerfen und die nächste.

**Punkt 3 ist der, den alle überspringen**, und er ist der wertvollste. Wer vorher aufschreibt, was er erwartet, lernt aus jedem Test — auch aus den fehlgeschlagenen. Wer nur ausprobiert und schaut, lernt nur aus den erfolgreichen.

Du kennst das Verfahren schon: Genau so waren die Kaputtmach-Experimente der letzten Etappen gebaut. *Sag vorher, was du erwartest, dann führ aus.* Das war kein didaktisches Ritual — es war Training für heute.

### 5. Halbieren — der wichtigste Suchtrick

Dein Spiel hat vielleicht vierhundert Zeilen. Irgendwo darin sitzt ein Fehler. Wenn du sie einzeln durchgehst, brauchst du im Schnitt zweihundert Schritte.

**Halbierst du stattdessen, brauchst du neun.**

Das Verfahren: Finde eine Stelle in der Mitte des Ablaufs und prüfe, ob dort noch alles stimmt. Ist es in Ordnung, liegt der Fehler dahinter. Ist es schon falsch, liegt er davor. Dann halbierst du die verbleibende Hälfte. Und so weiter.

```python
# irgendwo in der Mitte
print(f"HALB: ort={aktueller_ort} inventar={inventar}")
```

Praktisch heißt das: Nicht zwanzig `print()` auf einmal einstreuen, sondern **eines in der Mitte**. Danach weißt du, welche Hälfte du vergessen kannst.

**Dasselbe funktioniert mit der Zeit statt mit dem Ort.** Wann lief es zuletzt richtig? Vor drei Commits? Dann liegt die Ursache in dem, was seither dazugekommen ist — und das ist überschaubar, wenn du dich an die Commit-Disziplin aus Etappe 0 gehalten hast.

Das Halbieren ist auch der Grund, warum Etappe 7 sich heute auszahlt. Deine Funktionen sind natürliche Halbierungspunkte: Statt „wo in vierhundert Zeilen" fragst du „welcher Baustein verhält sich falsch" — und hast danach zwanzig Zeilen statt vierhundert.

### 6. `print()`-Debugging richtig gemacht

`print()` ist nicht schlecht. Es ist nur meistens schlecht *benutzt*.

**Schlecht:**
```python
print(x)
print("hier")
print("hier2")
```
Nach zehn Minuten weißt du nicht mehr, welche Ausgabe woher kam.

**Gut:**
```python
print(f"[bewege] ort={aktueller_ort!r} richtung={richtung!r} ausgaenge={ausgaenge}")
```

Drei Dinge machen den Unterschied:

**Ein Präfix**, das sagt, woher die Zeile kommt. Wenn du fertig bist, findest du damit alle wieder — `[bewege]` ist leichter zu suchen als `print(`.

**Namen dazu.** `ort=` statt nur der Wert. Sonst rätst du bei drei Ausgaben, welche welche ist.

**`!r` statt nichts.** Das ist neu: Es zeigt den Wert so an, wie Python ihn schreiben würde — mit Anführungszeichen bei Strings. `ort=westen` und `ort=' westen '` sehen ohne `!r` gleich aus, und das verirrte Leerzeichen bleibt unsichtbar. Genau deshalb standen in den letzten Etappen immer Anführungszeichen in den Debug-Beispielen; `!r` macht das automatisch und zuverlässiger.

**Und räum sie hinterher weg.** Debug-Ausgaben, die im Code bleiben, sind der Grund, warum Spieler irgendwann `[bewege] ort='wiese'` zu sehen bekommen.

### 7. Der Debugger — die bessere Variante

Die Schuld aus Etappe 2. `print()` zeigt dir einen Wert an einer Stelle. Der Debugger hält das Programm an und zeigt dir **alles**.

**In VS Code, einmalig:**

1. Setz einen **Breakpoint**: Klick links neben eine Zeilennummer, ein roter Punkt erscheint.
2. Starte mit **F5** statt mit dem normalen Ausführen.
3. Das Programm läuft bis zum Breakpoint und hält an.

**Und jetzt siehst du, was `print()` dir nie zeigen kann:**

Links im Bereich **Variablen** stehen alle Namen, die gerade existieren, mit ihren Werten. Nicht der eine, den du dir ausgegeben hast — alle. Du kannst Listen und Dictionaries aufklappen und hineinschauen.

Darunter steht der **Aufrufstapel**: welche Funktion gerade läuft und wer sie gerufen hat. Das ist dasselbe wie ein Traceback, nur live und anklickbar.

**Die vier Knöpfe, mehr brauchst du nicht:**

| Knopf | Taste | Was er tut |
|---|---|---|
| Step Over | F10 | Nächste Zeile, Funktionsaufrufe werden komplett ausgeführt |
| Step Into | F11 | Nächste Zeile, aber in die aufgerufene Funktion hinein |
| Step Out | Shift+F11 | Aktuelle Funktion zu Ende laufen lassen und zurück |
| Continue | F5 | Weiter bis zum nächsten Breakpoint |

**Die praktische Regel:** *Step Over*, bis du an der interessanten Stelle bist. Dann *Step Into*, um zu sehen, was die Funktion tut. Wenn du merkst, dass du zu tief bist, *Step Out*.

**Ein Trick, der viel Zeit spart:** Man kann Breakpoints an Bedingungen knüpfen. Rechtsklick auf den roten Punkt, „Edit Breakpoint", und du gibst zum Beispiel `runden > 10` ein. Das Programm hält dann nur an, wenn die Bedingung stimmt. Bei einem Fehler, der erst beim zwölften Durchlauf auftritt, ist das der Unterschied zwischen zwei Minuten und zwanzig.

**Ohne VS Code:** Python bringt einen Debugger mit. `python -m pdb spiel.py` startet ihn, die Befehle sind `n` (next), `s` (step), `c` (continue), `p variable` (print), `q` (quit). Weniger bequem, überall verfügbar.

### 8. Wann Debugger, wann `print()`

Beides hat seinen Platz, und die Wahl ist nicht Geschmackssache.

**Debugger, wenn du nicht weißt, wo du suchst.** Er zeigt dir den ganzen Zustand auf einmal. Wenn du erst herausfinden musst, was überhaupt schiefläuft, ist er unschlagbar.

**`print()`, wenn du weißt, was du beobachten willst** — besonders über viele Durchläufe hinweg. Ein Wert, der sich über dreißig Runden verändert, ist als Liste von Zeilen leichter zu überblicken als dreißigmal Anhalten. Genau das brauchst du in Etappe 12, wenn NPCs sich bei jedem Tick bewegen.

**Der Debugger hat einen weiteren Vorteil, der oft übersehen wird:** Er verändert deinen Code nicht. Ein `print()`, das du vergisst, bleibt drin.

### 9. Funktionen einzeln aufrufen — der Zahltag aus Etappe 7

Vor dem Refactoring musstest du das ganze Spiel starten und dich zu der Stelle durchspielen, um eine Berechnung zu prüfen. Jetzt:

```python
print(berechne_schaden(10, 3))
print(berechne_schaden(3, 10))
```

Zwei Zeilen, kein Spiel, kein Durchspielen. **Das ist die schnellste Art zu prüfen, ob ein Baustein für sich genommen richtig ist** — und wenn er es ist, kannst du ihn beim Suchen ausschließen.

Genau das machst du in Etappe 26 automatisch, und dann heißen diese Zeilen Tests.

### 10. Git als Debugging-Werkzeug

Seit Etappe 0 committest du nach jeder Etappe. Heute zahlt es sich zum ersten Mal aus.

```bash
git diff              # was habe ich seit dem letzten Commit geändert?
git log --oneline     # wann lief es zuletzt sicher?
git stash             # Änderungen kurz beiseitelegen und testen
```

**`git diff` ist bei echten Fehlern das erste, was du tun solltest.** Wenn es gestern noch lief und heute nicht, steht die Ursache mit hoher Wahrscheinlichkeit in dem, was der Befehl dir anzeigt. Das reduziert den Suchraum von vierhundert Zeilen auf vielleicht dreißig — noch bevor du überhaupt angefangen hast zu suchen.

> ⚠️ **Aber heute nicht.** Wenn dein Mentor dir manipulierten Code zurückgibt, würde `git diff` die Bug-Jagd in fünf Sekunden beenden — und du hättest nichts gelernt. Behandle den Code als frischen Stand und such mit den Werkzeugen von oben.
>
> Die Versuchung ist real. Ihr zu widerstehen gehört zur Übung, denn draußen gibt es die Abkürzung nicht: Bei fremdem Code weißt du nicht, welche Zeile neu ist.

### 11. Den Fehler beschreiben

Das ist das Lernziel, das der Lehrplan für diese Etappe nennt, und es ist mehr als Höflichkeit.

Eine gute Fehlerbeschreibung hat vier Teile:

> **Was ich wollte:** Der Spieler soll nach `gehe norden` in der Schmiede stehen.
> **Was passiert:** Er bleibt auf dem Dorfplatz, aber die Meldung sagt „Du gehst nach norden."
> **Was ich ausgeschlossen habe:** Die Ortstabelle stimmt — `orte["dorfplatz"]["ausgaenge"]["norden"]` gibt `"schmiede"`. `bewege_spieler` gibt einzeln aufgerufen auch `"schmiede"` zurück.
> **Was ich vermute:** Der Rückgabewert wird beim Aufruf nicht übernommen.

Vergleich das mit *„gehe funktioniert nicht"*.

**Der eigentliche Nutzen ist aber nicht, dass andere dir besser helfen können.** Es ist, dass du beim Schreiben der dritten Zeile — *was ich ausgeschlossen habe* — merkst, dass du noch gar nichts ausgeschlossen hast. Und dann gehst du es prüfen, statt zu fragen.

Es gibt dafür einen Namen: **Rubber-Duck-Debugging.** Die Idee ist, das Problem laut einer Gummiente zu erklären. Klingt albern, funktioniert aber, weil Erklären dich zwingt, Lücken zu benennen, über die du beim Denken hinweggerutscht bist. Ein erschreckender Anteil aller Fehler löst sich während der Beschreibung — bevor jemand geantwortet hat.

**Für dieses Projekt heißt das:** Wenn du feststeckst, formulier es in dieser Form, bevor du fragst. In `MENTOR.md` steht ohnehin, dass die erste Rückfrage lauten wird: *Was hast du probiert, was hast du erwartet, was ist passiert?* Wenn du das schon mitlieferst, spart ihr euch eine Runde.

---

## Dein Auftrag

Diese Etappe hat eine ungewöhnliche Reihenfolge: **Erst die Werkzeuge, dann die Jagd.** Wer den Debugger zum ersten Mal öffnet, während er unter Druck einen Fehler sucht, benutzt ihn nicht.

**Schritt 1 — Den Debugger einrichten**
Setz einen Breakpoint in deiner Hauptschleife und starte mit F5. Lass das Spiel anhalten, sieh dir die Variablen an, klapp `orte` auf, geh drei Schritte weiter.

Noch ist nichts kaputt. Das ist der Punkt: Du lernst das Werkzeug an einem funktionierenden Programm kennen.

**Schritt 2 — Alle vier Schritt-Arten ausprobieren**
Setz einen Breakpoint vor einem Funktionsaufruf. Einmal mit **Step Over** drüber, einmal mit **Step Into** hinein. Aus der Funktion mit **Step Out** wieder heraus.

Danach solltest du erklären können, was der Unterschied ist. Es sind zwei Minuten und der Unterschied zwischen „ich habe einen Debugger" und „ich kann ihn benutzen".

**Schritt 3 — Einen bedingten Breakpoint setzen**
Rechtsklick auf einen Breakpoint, Bedingung `runden > 5` eintragen. Spiel, bis er auslöst.

Genau das brauchst du bei Typ-2-Fehlern, die erst nach einer Weile auftreten.

**Schritt 4 — Die Trainingsbugs**
Jetzt baust du selbst Fehler ein — einer von jedem Typ, und du weißt jeweils, welchen. Es geht nicht ums Finden, sondern darum, zu sehen, wie jeder Typ sich **anfühlt**.

Vorschläge unten im Abschnitt *Kaputtmachen*. Nach jedem: Wie hättest du ihn gefunden, wenn du nicht wüsstest, was du getan hast?

**Schritt 5 — Das Protokoll schreiben**
Bevor die echte Jagd beginnt: Schreib in `GELERNT.md` oder `FEHLER.md` **deine eigene Vorgehensweise** auf. Fünf bis acht Schritte, in deinen Worten, in der Reihenfolge, in der du sie abarbeiten willst.

Das ist der eigentliche Ertrag dieser Etappe. Nicht abschreiben — formulieren. In Etappe 16 liest du es nach und änderst, was sich nicht bewährt hat.

**Schritt 6 — Die Bug-Jagd**
Jetzt gibst du deinen Code an deinen Mentor und forderst die Jagd an:

```text
Ich will eine Runde Bug-Jagd. Bau Fehler in meinen Code ein und gib ihn
zurück, ohne mir zu sagen wie viele oder wo. Mindestens einer soll nicht
abstürzen, sondern nur das Falsche liefern.
```

**Während der Jagd: kein `git diff`.** Und führ Protokoll — welche Hypothese, welche Vorhersage, was kam heraus.

**Schritt 7 — Beschreiben statt fragen**
Wenn du bei einem Fehler feststeckst, schreib die Vier-Punkte-Beschreibung aus Konzept 11 auf, bevor du deinen Mentor fragst.

Achte darauf, wie oft du sie am Ende gar nicht abschickst.

**Schritt 8 — Das Fehlertagebuch anlegen**
Trag jeden gefundenen Fehler ein: Symptom, Ursache, wie gefunden. Auch die aus früheren Etappen, an die du dich noch erinnerst.

---

## Wenn du keinen Mentor hast

Die Bug-Jagd braucht jemanden, der Fehler einbaut, ohne dir zu sagen welche. Wenn du das Tutorial allein durcharbeitest, gibt es eine Variante, die überraschend gut funktioniert: **Zeitversatz.**

1. Schreib heute zehn Sabotagen in eine Datei `sabotage.txt` — je eine Zeile, verteilt über deinen Code. *„In `bewege_spieler` das `return` entfernen."* *„Bei der Inventarprüfung `>=` zu `>` machen."* *„Im Zähler die Initialisierung in die Schleife schieben."*
2. Committe deinen sauberen Stand.
3. **Warte mindestens zwei Tage.** Nicht schummeln — die Wartezeit ist das Verfahren.
4. Dann würfle oder lass dir drei Zahlen zwischen 1 und 10 geben, wende die entsprechenden Sabotagen an, **ohne die anderen Zeilen zu lesen**, und schließ die Datei.
5. Jetzt jage.

Nach zwei Tagen erinnerst du dich an die Liste, aber nicht an die Details — und das reicht. Ein Fehler, den du selbst eingebaut und vergessen hast, verhält sich beim Suchen fast wie ein fremder.

Der Vorteil gegenüber der Mentor-Variante: Du kannst hinterher exakt nachlesen, was du getan hast, und vergleichen, wie du es gefunden hast. Der Nachteil: Die Sabotagen sind aus deinem Kopf, also treffen sie deine blinden Flecken nicht.

---

## Was NICHT in diese Etappe gehört

- ❌ `try` / `except`, um Abstürze zu verhindern → **Etappe 20**
- ❌ `pytest` oder ein anderes Testframework → **Etappe 26**
- ❌ `logging` statt `print()` → nicht in diesem Lehrplan
- ❌ Neue Spielfunktionen jeder Art
- ❌ Den Code „bei der Gelegenheit" schöner machen

**Die Verwechslung von Fehlerbehandlung und Debugging ist hier die wichtigste Abgrenzung.** Beide klingen nach „mit Fehlern umgehen" und sind gegensätzlich:

> **Debugging** heißt herausfinden, *warum* sich das Programm falsch verhält.
> **Fehlerbehandlung** heißt dafür sorgen, dass es bei absehbaren Problemen sauber weiterläuft statt abzustürzen.

Ein `except` an der falschen Stelle **verschlimmert** Debugging: Es verwandelt einen Typ-1-Fehler, der dir laut sagt, wo es klemmt, in einen Typ-3-Fehler, der stillschweigend das Falsche tut. In Etappe 20 kommst du darauf zurück, und dann wirst du verstehen, warum ein nacktes `except:` so gefährlich ist.

---

## Selbsttest

- [ ] Du hast einen Breakpoint gesetzt und das Programm damit angehalten
- [ ] Du kannst Step Over, Step Into und Step Out unterscheiden und hast alle drei benutzt
- [ ] Du hast im Variablen-Bereich ein Dictionary aufgeklappt und hineingeschaut
- [ ] Du hast einen bedingten Breakpoint gesetzt, der ausgelöst hat
- [ ] Du hast alle drei Fehlertypen selbst eingebaut und beobachtet
- [ ] Du kannst in deinem eigenen Traceback zeigen, welche Zeile *was* sagt und welche *wo*
- [ ] Dein Debugging-Protokoll steht schriftlich im Repo
- [ ] Das Fehlertagebuch existiert und hat mindestens drei Einträge
- [ ] Jeder Eintrag hat die Zeile „wie gefunden"
- [ ] Du hast die Bug-Jagd durchlaufen und alle Fehler gefunden
- [ ] Du hast während der Jagd kein `git diff` benutzt
- [ ] Du hast mindestens eine Vier-Punkte-Fehlerbeschreibung geschrieben
- [ ] Alle Debug-Ausgaben sind wieder aus dem Code entfernt
- [ ] Dein Spiel läuft am Ende wieder wie vor der Jagd

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten:

1. **Nenn die drei Fehlertypen und je ein Beispiel aus deinem eigenen Spiel.** Welcher ist der gefährlichste und warum?
2. **In welcher Richtung liest man einen Traceback?** Welche Zeile sagt *was*, welche sagt *wo*, wozu ist der Rest da?
3. **Warum ist die Stelle, an der ein Programm abstürzt, oft nicht die Stelle, an der es kaputt ist?** Nenn ein Beispiel.
4. **Was ist der Unterschied zwischen Debugging und Fehlerbehandlung?**
5. **Beschreib das Halbierungs-Verfahren.** Warum sind neun Schritte besser als zweihundert?
6. **Wann benutzt du den Debugger, wann `print()`?** Nenn für beides eine Situation, in der es das bessere Werkzeug ist.
7. **Was macht `!r` in einem f-String, und wann brauchst du es?**
8. **Was ist der Unterschied zwischen Step Over und Step Into?**
9. **Welche vier Angaben gehören in eine gute Fehlerbeschreibung?**
10. **Warum ist „ich habe etwas geändert und jetzt geht es" ein schlechtes Ergebnis?**

**Frage 10 ist die wichtigste**, und sie ist unbequem. Ein Fehler, der verschwunden ist, ohne dass du weißt warum, ist nicht behoben — er ist nur gerade unsichtbar. Wenn du erklären kannst, warum das ein Problem ist, hast du verstanden, worum es in dieser Etappe ging.

---

## Transferaufgabe (10–15 Minuten)

**Neue Datei, außerhalb des Spiels.** `uebung_08.py`.

Hier ist ein kleines Programm, das die Durchschnittsnote berechnet — einmal roh, einmal ohne die beste und schlechteste Note. Tipp es ab oder kopier es:

```python
def durchschnitt(werte):
    summe = 0
    for w in werte:
        summe += w
    return summe / len(werte)

def bereinige(werte):
    """Entfernt die beste und die schlechteste Note."""
    werte.remove(max(werte))
    werte.remove(min(werte))
    return werte

noten = [4, 1, 2, 3, 5]

print("Roh:          ", durchschnitt(noten))
print("Bereinigt:    ", durchschnitt(bereinige(noten)))
print("Roh nochmal:  ", durchschnitt(noten))
```

**Bevor du es ausführst:** Schreib auf, was in den drei Zeilen stehen müsste. Zeile 1 und Zeile 3 berechnen dasselbe aus derselben Liste.

Dann ausführen.

**Jetzt die Aufgaben:**

1. Welcher Fehlertyp ist das? Warum ist er besonders unangenehm?
2. Finde die Ursache — mit dem Debugger, nicht durch Nachdenken. Setz einen Breakpoint und beobachte `noten` vor und nach dem Aufruf von `bereinige`.
3. Erklär in einem Satz, warum es passiert. Der Grund steht in Etappe 4.
4. Repariere es, ohne die drei `print()`-Zeilen zu ändern.
5. Und die eigentliche Frage: **Ist der Docstring von `bereinige` gelogen?**

Punkt 5 ist der interessanteste. Die Funktion tut, was dort steht — und noch etwas anderes, das nicht dort steht. Eine Funktion, die nebenbei etwas verändert, ohne dass ihr Name oder ihre Beschreibung es ankündigt, ist eine der ergiebigsten Fehlerquellen überhaupt.

Das verbindet drei Etappen: mutable Objekte aus Etappe 4, das Prinzip „Abhängigkeiten sichtbar machen" aus Etappe 7 und die Fehlersuche von heute.

---

## Kaputtmachen

Heute ist das Kaputtmachen die Vorbereitung, nicht der Abschluss. Bau jeden dieser Fehler ein, beobachte ihn, mach ihn rückgängig.

**Trainingsbug 1 — Typ 1, sofortiger Absturz**
Entferne in einer Funktion einen Parameter aus der Definition, lass die Aufrufe unverändert. Starte.

Lies den Traceback vollständig. Zeig auf die Zeile, die sagt *was*, und auf die, die sagt *wo*. Wie viele Ebenen zeigt der Aufrufweg?

**Trainingsbug 2 — Typ 2, bedingter Absturz**
Nimm bei `gehe` die Prüfung heraus, ob überhaupt eine Richtung angegeben wurde. Starte und spiel normal — es läuft. Dann tipp `gehe` allein.

**Das ist die Lektion:** Der Fehler war die ganze Zeit da. Er ist nur nie ausgelöst worden. Wie viele solcher Fehler stecken gerade in deinem Spiel, ohne dass du es weißt?

**Trainingsbug 3 — Typ 3, still und falsch**
Verschieb die Initialisierung deines Rundenzählers in die Schleife hinein.

Kein Absturz, keine Meldung. Der Zähler steht immer auf 1. Wie lange hättest du gebraucht, das zu bemerken, wenn du es nicht selbst getan hättest?

**Trainingsbug 4 — Der Vergleich, der fast stimmt**
Ändere in deiner Inventar-Obergrenze `>=` zu `>` (oder umgekehrt). Jetzt passen elf Gegenstände hinein statt zehn.

Ein Zeichen. Kein Absturz. Und es fällt nur auf, wenn jemand genau nachzählt. **Diese Sorte Fehler ist der Grund, warum Etappe 26 existiert.**

**Trainingsbug 5 — Das vergessene `return`**
Entferne in einer Funktion, die etwas berechnet, das `return`. Ruf sie auf und arbeite mit dem Ergebnis weiter.

Was steht in der Variable? Wo knallt es — in der Funktion oder viel später? **Das ist Ursache gegen Symptom in Reinform.**

**Trainingsbug 6 — Die Reihenfolge zweier Zeilen**
Vertausch bei den besuchten Orten die `in`-Prüfung und das `add()`.

Kennst du aus Etappe 6. Diesmal ist die Frage nicht, was passiert, sondern: **Wie würdest du es finden, wenn du es nicht wüsstest?** Welchen Breakpoint würdest du wo setzen?

**Trainingsbug 7 — Der Fehler in den Daten**
Ändere in deiner Ortstabelle einen Zielort auf einen Namen, den es nicht gibt. Geh in diese Richtung.

Der Code ist einwandfrei. Der Fehler steht in den Daten. **Für einen Anfänger ist das der verwirrendste Fall überhaupt**, weil man reflexhaft im Code sucht. Merk dir das Gefühl — ab Etappe 25 liegen deine Daten in Dateien, und dann ist diese Fehlersorte häufiger als jede andere.

**Trainingsbug 8 — Zwei auf einmal**
Bau zwei Fehler gleichzeitig ein. Repariere einen und starte.

Es geht immer noch nicht. **Die Falle:** Man denkt, die Reparatur war falsch, und macht sie rückgängig. Dann hat man zwei Fehler und eine falsche Überzeugung.

Deshalb: Nach jeder Reparatur prüfen, **ob sich das Symptom verändert hat** — nicht nur, ob es weg ist. Ein anderes Symptom heißt Fortschritt.

---

## Häufige Stolpersteine

| Symptom | Was dahintersteckt | Was du tust |
|---|---|---|
| Der Traceback zeigt auf eine Zeile, die richtig aussieht | Bei `SyntaxError` oft die Zeile davor | Eine Zeile höher schauen, Klammern zählen |
| „Es geht einfach nicht" | Das Symptom ist nicht genau genug beobachtet | Exakt aufschreiben, was passiert statt was fehlt |
| Zwanzig `print()` und keine Erkenntnis | Gestreut statt halbiert | Alle raus, eines in die Mitte |
| Der Fehler verschwindet beim Debuggen | Meist ein Beobachtungsfehler, selten ein Timing-Problem | Zustand ausgeben statt sich zu erinnern |
| Nach der Reparatur geht es immer noch nicht | Zwei Fehler gleichzeitig | Hat sich das Symptom *verändert*? |
| Der Debugger hält nicht an | Breakpoint in nie ausgeführtem Code, oder normal gestartet statt F5 | Breakpoint an eine Stelle, die sicher läuft |
| „Ich habe was geändert, jetzt geht's" | Fehler unsichtbar, nicht behoben | Änderung rückgängig, Fehler reproduzieren, dann gezielt beheben |
| Debug-Ausgaben tauchen im Spiel auf | Vergessen zu entfernen | Nach dem Präfix suchen |
| Die Fehlermeldung sagt nichts | Sie sagt fast immer etwas | Die letzte Zeile wörtlich lesen, Wort für Wort |

**Der wichtigste Reflex dieser Etappe** ist keine Technik, sondern eine Reihenfolge:

> **Erst beobachten, dann vermuten, dann ändern.**

Die meisten Anfänger machen es umgekehrt: ändern, schauen, dann vermuten. Das fühlt sich schneller an und dauert länger — weil man nach zehn Änderungen nicht mehr weiß, welche davon etwas bewirkt hat.

---

## Ein Blick nach vorne

Diese Etappe hat einen ungewöhnlichen Status: Sie ist die einzige, die nie ganz endet.

**Ab morgen läuft die Bug-Jagd unregelmäßig weiter.** Dein Mentor wird manchmal Fehler einbauen und es dazusagen, manchmal ein normales Review geben, manchmal dich bitten, einen selbst eingebauten Fehler zu suchen. Du weißt nicht, wann.

Das ist Absicht. Wenn du wüsstest „nach jedem Block kommen drei Bugs", wäre es eine Schulaufgabe. So bleibt es eine Fähigkeit.

**Eine Zusage dazu**, die auch in `MENTOR.md` steht und die du einfordern darfst: Dein Mentor behauptet nie, dein Code sei fehlerfrei, wenn er einen Fehler sieht. Und nie, er hätte etwas eingebaut, wenn er es nicht getan hat. Fragst du direkt, bekommst du eine ehrliche Antwort. Unvorhersehbar ist nur, *ob* manipuliert wird — nie die Wahrheit über deinen Code.

**In Etappe 9** bekommt dein Debugger neue Bedeutung. Objekte haben Zustand, und im Variablen-Bereich kannst du sie aufklappen und sehen, was ein `Player` in diesem Moment tatsächlich enthält. Das ist die Art von Einblick, die `print()` mühsam nachbaut.

**In Etappe 12** wird er unverzichtbar. Der Tick verändert bei jedem Durchlauf mehrere NPCs gleichzeitig, und die Frage „warum steht die Bäckerin plötzlich am Minenpfad" ist mit einem bedingten Breakpoint in fünf Minuten beantwortet und mit `print()` in einer Stunde.

**In Etappe 16** kommt die Bug-Jagd II — dieselben Werkzeuge, ein größeres System, subtilere Fehler. Dort liest du dein Protokoll von heute nach und schärfst es.

**Und in Etappe 26** dreht sich das Verhältnis um. Statt Fehler zu finden, nachdem sie passiert sind, schreibst du Tests, die sie melden, bevor du sie bemerkst. Dein Fehlertagebuch ist dann eine Liste von Testkandidaten — jeder Eintrag beschreibt etwas, das schon einmal kaputt war und deshalb wieder kaputtgehen kann.

---

## Abschluss

**`GELERNT.md`:**
Zwei bis drei Sätze. Zusätzlich diesmal:

- Dein Debugging-Protokoll, wenn es nicht in einer eigenen Datei steht
- Debugger oder Terminal — was lag dir besser, und warum?
- Und die Frage dieser Etappe: **Welchen Fehler hast du am längsten gesucht, und woran lag es, dass es so lange gedauert hat?**

Bei der letzten Frage geht es nicht um den Fehler, sondern um dich. War die Hypothese zu breit? Hast du an der falschen Stelle gesucht? Hast du geändert, bevor du beobachtet hast? Das ist die Information, aus der in Etappe 16 ein besseres Protokoll wird.

**Commit:**
```bash
git add .
git commit -m "Etappe 8: Bug-Jagd bestanden"
git push
```

Damit ist **Block 1 abgeschlossen.** Acht Etappen, und dein Spiel hat eine Welt, ein Inventar, eine Karte, ein Gedächtnis, saubere Bausteine — und du hast eine Methode, wenn etwas davon nicht tut, was es soll.

Schau dir `git log --oneline` an. Das ist keine Zeremonie: Diese Liste ist der Beleg dafür, dass du seit Wochen dranbleibst, und in Block 2 wird der Stoff schwerer.

---

## Wenn du mehr willst

Optional, erst bei grünem Selbsttest.

**Ein Debug-Befehl im Spiel.** Ein Befehl `debug`, der den kompletten Zustand ausgibt: Ort, Inventar, besuchte Orte, Rundenzahl, Flags. Fünf Zeilen, und du sparst dir bei jeder künftigen Fehlersuche den ersten Schritt.

Bau ihn so, dass er sich abschalten lässt — eine Konstante `DEBUG = True` ganz oben, und der Befehl reagiert nur, wenn sie gesetzt ist. Damit hast du nebenbei das Muster kennengelernt, mit dem echte Programme ihren Entwicklermodus steuern.

**Die eigene Fehlermeldung.** Wenn `bewege_spieler` einen Ort bekommt, den es nicht gibt, ist die Standardmeldung `KeyError: 'schmide'`. Hilfreicher wäre: *„Der Ausgang nach norden zeigt auf 'schmide', aber diesen Ort gibt es nicht."*

Du brauchst dafür noch kein `try`/`except` — eine Prüfung und ein `print()` reichen. Und du merkst dabei etwas Wichtiges: Eine gute Fehlermeldung ist eine, die dir sagt, **was du als Nächstes tun sollst**.

**Farbe im Terminal.** Block 1 ist geschafft — das darf man sehen. Dein Terminal kann Farben, und du brauchst dafür kein Modul, nur ein paar Konstanten:

```python
ROT   = "\033[91m"
GRUEN = "\033[92m"
GELB  = "\033[93m"
GRAU  = "\033[90m"
RESET = "\033[0m"

print(f"{GELB}Die Versorgerin sieht dich an.{RESET}")
```

Diese Zeichenfolgen sind Steuerbefehle an das Terminal: Farbe an, Farbe aus. Vergiss das `RESET` nicht, sonst bleibt alles Folgende eingefärbt.

Ein sinnvolles Schema: Gegenstände grün, Figuren gelb, Fehlermeldungen rot, Ortsbeschreibungen normal, Debug-Ausgaben grau. Nach zehn Minuten sieht dein Spiel aus wie eine echte Konsolenanwendung statt wie ein Übungsskript — und das nach einer Etappe, in der du nichts gebaut, sondern nur repariert hast.

**Zur Verträglichkeit:** Auf Linux, macOS und im modernen Windows Terminal funktioniert das ohne Weiteres. In der alten `cmd.exe` bleiben die Codes unter Umständen als Zeichensalat stehen — dann entweder Windows Terminal benutzen oder die Farben über eine Konstante `FARBEN = False` abschaltbar machen. Letzteres ist ohnehin die bessere Übung.

**Die Konsistenzprüfung.** Schreib eine Funktion, die deine Ortstabelle einmal komplett durchgeht und meldet, wenn ein Ausgang auf einen Ort zeigt, den es nicht gibt. Ruf sie beim Start auf.

Zehn Zeilen, und Trainingsbug 7 kann dir nie wieder passieren. Das ist der Gedanke, aus dem in Etappe 26 die Tests entstehen — nur dass du ihn hier von Hand baust, für ein Problem, das dich heute geärgert hat.

---

> **Nächste Etappe:** [Etappe 9 — Alles wird zum Objekt](etappe-09-alles-wird-zum-objekt.md) · Klassen, `__init__`, Methoden, Attribute
> Block 2 beginnt. Und die acht Parameter, die du in Etappe 7 durch jede Funktion geschleppt hast, bekommen endlich einen Behälter.
