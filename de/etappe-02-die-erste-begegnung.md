# Etappe 2 — Die erste Begegnung

> **Block 1: Fundament** · Etappe 2 von 29 · [← Etappe 1](etappe-01-der-erste-morgen.md) · [Lehrplan](../RPG_Lehrplan.md) · [Etappe 3 →](etappe-03-die-game-loop.md)

**Boot.dev:** `if` / `elif` / `else`, Vergleiche, Booleans, `and` / `or` / `not`
**Zeitaufwand:** 3–5 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 1 abgeschlossen, Selbsttest grün

---

## Worum es geht

Der Spieler ist nicht allein. Einer der drei Verbliebenen findet ihn — und stellt die erste Frage, die eine Antwort verlangt.

Zwei Möglichkeiten: Der Spieler erzählt, was er gesehen hat. Oder er behält es für sich. Beides ist eine legitime Entscheidung, und beide haben Folgen — nicht heute, aber in vier Monaten.

Technisch ist diese Etappe ein größerer Sprung als Etappe 1. Zum ersten Mal trifft dein Programm eine **Entscheidung**, und zum ersten Mal schreibst du einen **Block** — Code, der eingerückt unter einer Bedingung steht. Diese Einrückung ist in Python keine Formatierung, sondern Bedeutung. Das ist der Punkt, an dem viele Anfänger die ersten wirklich verwirrenden Fehlermeldungen sehen.

**Und es ist die Etappe, in der dein Spiel anfängt, sich etwas zu merken.**

---

## Der lange Bogen

Dieser Abschnitt steht ab jetzt in jeder Etappe. Er sagt dir, was du heute anlegst und wo es später eingelöst wird — damit du beim Schreiben weißt, dass nichts davon Wegwerfarbeit ist.

| Was du heute baust | Wo es wieder auftaucht |
|---|---|
| `vertrauen = True/False` | **Etappe 18** — wird zum vollen Vertrauens- und Flag-System |
| Verknüpfte Bedingungen (`and`/`or`/`not`) | **Etappe 18** — Dialoge prüfen mehrere Flags gleichzeitig |
| Eingaben vergleichbar machen (`.lower()`, `.strip()`) | **Etappe 3 & 5** — wird zum Befehlsparser des ganzen Spiels |
| Der `else`-Zweig für Unerwartetes | **Etappe 20** — wird zu echter Fehlerbehandlung |
| Die Wahl zwischen Erzählen und Schweigen | **Etappe 17** — beeinflusst mit, wer als Nächstes verschwindet |
| Der NPC, der dich findet | **Etappe 12** — bekommt einen Tagesablauf und ein Gedächtnis |

Eine einzige Boolean-Variable wirkt heute lächerlich klein. Sie ist der Keim deines gesamten Konsequenzsystems. Bei drei NPCs kannst du dieses System noch vollständig im Kopf behalten — genau deshalb sind es drei.

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

**Wer von den dreien findet den Spieler?**

Das klingt nach reiner Erzählung, hat aber mechanische Folgen. Wer den Spieler zuerst findet, hat den ersten Zugriff auf seine Version der Ereignisse — und wird damit automatisch zur Bezugsfigur. In Etappe 18 wirst du merken, dass der Spieler dieser Figur eher glaubt als den anderen beiden.

Wenn es der Fremde ist, der ihn findet, ist das etwas völlig anderes, als wenn es die Versorgerin ist.

Notier deine Entscheidung mit einem Satz Begründung in `GELERNT.md`. Nicht weil es Pflicht ist, sondern weil du in Etappe 17 wissen willst, warum du es so gemacht hast.

---

## Die Konzepte

### 1. Booleans

Ein Wahrheitswert. Es gibt genau zwei davon:

```python
tuer_offen = True
regnet = False
```

**Achtung:** Groß geschrieben, ohne Anführungszeichen. `True` ist ein Wahrheitswert, `"True"` ist ein Text mit vier Buchstaben. Das ist derselbe Unterschied wie `12` und `"12"` aus Etappe 1 — und er wird dich mindestens einmal beißen.

### 2. Vergleichsoperatoren

Ein Vergleich ist ein Ausdruck, der zu `True` oder `False` wird:

```python
alter = 34

alter == 34    # True   — gleich
alter != 34    # False  — ungleich
alter > 18     # True
alter <= 30    # False
```

Probier das aus, indem du einen Vergleich direkt in ein `print()` steckst:

```python
print(alter > 18)
```

Das ist ein Werkzeug, kein Endprodukt — genau wie `type()` in Etappe 1. Wenn du dir bei einer Bedingung unsicher bist, gib sie aus, statt zu raten.

### 3. `=` gegen `==`

**Das hier kostet jeden Programmierer einmal eine halbe Stunde. Auch dich. Es ist keine Schande.**

```python
alter = 34      # ZUWEISUNG:  alter bekommt den Wert 34
alter == 34     # VERGLEICH:  ist alter gleich 34?
```

In Etappe 1 hast du dir angewöhnt, `=` als „bekommt den Wert" zu lesen. Genau dafür war das gut. `==` liest sich als „ist gleich".

Schreibst du versehentlich `if alter = 34:`, bekommst du einen `SyntaxError`. Python fängt das ab — in anderen Sprachen tut es das nicht, und dort ist derselbe Tippfehler ein Fehler vom Typ 3: kein Absturz, einfach das Falsche.

### 4. `if`, `elif`, `else` — und die Einrückung

```python
temperatur = 4

if temperatur < 0:
    print("Es friert.")
elif temperatur < 10:
    print("Es ist kalt.")
else:
    print("Erträglich.")
```

Drei Dinge, die alle drei wichtig sind:

**Der Doppelpunkt** am Ende der Bedingungszeile. Vergisst du ihn, kommt ein `SyntaxError`.

**Die Einrückung** — vier Leerzeichen. In Python ist Einrückung keine Kosmetik, sondern **Syntax**. Sie entscheidet, was zum Block gehört und was nicht:

```python
if temperatur < 0:
    print("Es friert.")        # gehört zum if
print("Guten Morgen.")         # läuft IMMER
```

Das ist der häufigste Anfänger-Bug dieser Etappe, und er ist typischerweise Typ 3: kein Absturz, nur eine Zeile, die immer läuft statt manchmal.

Stell VS Code so ein, dass Tab vier Leerzeichen einfügt, und misch niemals Tabs und Leerzeichen. Python beschwert sich darüber mit einem `IndentationError` oder — schlimmer — verhält sich einfach anders als gedacht.

**`elif` ist nicht dasselbe wie mehrere `if`.** Das ist ein echter Unterschied, keine Stilfrage:

```python
# Version A — es läuft GENAU EIN Zweig
if punkte > 100:
    print("Gold")
elif punkte > 50:
    print("Silber")

# Version B — es werden ALLE Bedingungen geprüft
if punkte > 100:
    print("Gold")
if punkte > 50:
    print("Silber")
```

Bei `punkte = 150` gibt Version A **Gold** aus. Version B gibt **Gold und Silber** aus. Probier beides aus, bevor du weiterliest. Diese Unterscheidung wird dich in Etappe 17 im Ereignissystem wieder einholen, wenn mehrere Ereignisse gleichzeitig zutreffen könnten.

### 5. `and`, `or`, `not`

Bedingungen lassen sich verknüpfen:

```python
if alter >= 18 and hat_ausweis:
    print("Einlass.")

if regnet or schneit:
    print("Nimm eine Jacke.")

if not tuer_offen:
    print("Du musst erst aufschließen.")
```

- **`and`** — beide Seiten müssen wahr sein
- **`or`** — mindestens eine Seite muss wahr sein
- **`not`** — dreht um

**Reihenfolge der Auswertung:** `not` zuerst, dann `and`, dann `or`. Das heißt, `a or b and c` bedeutet `a or (b and c)` — nicht das, was viele beim Lesen erwarten.

**Setz im Zweifel Klammern.** Nicht weil Python sie braucht, sondern weil du in drei Monaten deinen eigenen Code liest.

**Eine Falle, die du selbst ausprobieren solltest:** Was ist der Unterschied zwischen

```python
not (a and b)
not a and not b
```

Nimm dir zwei Minuten und probier alle vier Kombinationen von `a` und `b` durch. Das ist eine der Lernzielfragen unten, und sie lässt sich nicht durch Nachdenken allein sauber beantworten — nur durch Ausprobieren.

**Wichtig für später:** In Etappe 18 lernst du, dass `and` und `or` nicht nur `True`/`False` zurückgeben, sondern etwas Nützlicheres. Heute reicht die einfache Sicht.

### 6. Truthy und Falsy

Ein `if` verlangt nicht zwingend einen Wahrheitswert. Python macht aus jedem Wert einen:

```python
if name:
    print("Ein Name ist da.")
```

**Als falsch gelten:** `False`, `0`, `""` (leerer String), `[]` (leere Liste), `{}` (leeres Dictionary), `None`.
**Alles andere gilt als wahr** — auch `"False"`, auch `-1`, auch `0.1`.

Das ist praktisch und wird dir in Etappe 4 (`if inventar:` statt `if len(inventar) > 0:`) das Leben leichter machen. Es ist gleichzeitig eine Fehlerquelle, weil `0` und `""` als falsch durchgehen, obwohl sie gültige Werte sein können. Merk dir die Liste — sie kommt in Etappe 18 nochmal zur Sprache, dann als echte Gefahr.

### 7. Strings vergleichen — und warum das heute wichtig wird

```python
"ja" == "Ja"      # False!
"ja" == "ja "     # False!
```

Groß- und Kleinschreibung zählen. Ein versehentliches Leerzeichen zählt. Wenn du den Spieler etwas eingeben lässt und dann `== "ja"` prüfst, scheitert das an jedem, der `Ja` tippt — und das sind fast alle.

Zwei String-Methoden lösen das:

```python
eingabe = input("Weiter? ")
antwort = eingabe.lower().strip()
```

- `.lower()` macht alles klein
- `.strip()` entfernt Leerzeichen am Anfang und Ende

Der Punkt hinter der Variable heißt: „ruf diese Funktion auf diesem Wert auf". Das ist dieselbe Schreibweise, die dir in Etappe 9 bei Objekten wiederbegegnet — dort ist sie dann `npc.speak()`. Gewöhn dich schon mal an sie.

**Und das ist der eigentliche Grund, warum das hierhergehört:** Diese zwei Zeilen sind der Ursprung deines Befehlsparsers. In Etappe 3 wird daraus die Verarbeitung von `umsehen` und `reden`, in Etappe 5 die von `gehe norden`, in Etappe 7 die Funktion `verarbeite_befehl()`. Du schreibst hier zum ersten Mal etwas, das bis zum Schluss im Spiel bleibt.

---

## Dein Auftrag

Wieder schrittweise, wieder nach jedem Schritt ausführen.

**Schritt 1 — Die Begegnung**
Nach dem Ruf aus Etappe 1: Jemand antwortet doch. Beschreib, wie diese Person auftaucht — und lass offen, ob das eine Erleichterung ist.

**Schritt 2 — Die Frage**
Die Figur fragt den Spieler, ob er etwas gesehen hat. Der Spieler antwortet per `input()`.

**Schritt 3 — Die Eingabe brauchbar machen**
Wandle die Eingabe so um, dass `Ja`, `ja` und ` JA ` alle dasselbe bedeuten. Zwei Methoden, eine Zeile.

**Schritt 4 — Die Verzweigung**
`if` / `elif` / `else`. Mindestens drei Zweige:
- Der Spieler erzählt, was er gesehen hat
- Der Spieler behält es für sich
- Der Spieler tippt etwas völlig anderes

Der dritte Zweig ist keine Pflichtübung, sondern eine Erkenntnis: Benutzer tun nie das, was man erwartet. Heute fängst du das mit `else` ab. In Etappe 20 machst du es richtig.

**Schritt 5 — Das Spiel merkt sich die Entscheidung**
Leg `vertrauen` an und setz es je nach Antwort. Kommentier, dass diese Variable in Etappe 18 zum Vertrauenssystem wird — dein Zukunfts-Ich wird dankbar sein.

**Schritt 6 — Die Reaktion**
Die Figur reagiert unterschiedlich. Und hier eine Auflage als Autor: **Die freundlichere Antwort darf nicht offensichtlich die bessere sein.** Wer sofort alles erzählt, macht sich angreifbar. Wer schweigt, wirkt verdächtig. Ein Spiel, in dem eine Option erkennbar richtig ist, hat keine Entscheidungen — nur eine Prüfung.

**Schritt 7 — Eine verknüpfte Bedingung**
Irgendwo im Ablauf brauchst du mindestens eine Bedingung mit `and`, `or` oder `not`. Zum Beispiel: Die Figur reagiert nur dann besonders, wenn der Spieler erzählt hat **und** eine bestimmte Bedingung aus dem Morgen zutrifft. Deine Variablen aus Etappe 1 stehen dafür bereit.

---

## Was NICHT in diese Etappe gehört

- ❌ Eine Schleife, die die Frage wiederholt, bis eine gültige Antwort kommt → **Etappe 3**
- ❌ Gegenstände einsammeln → **Etappe 4**
- ❌ Ein Dialogsystem mit mehreren Ebenen → **Etappe 18**
- ❌ Ein Zahlenwert für Vertrauen statt `True`/`False` → **Etappe 18**
- ❌ `try` / `except` für ungültige Eingaben → **Etappe 20**

Besonders der Punkt mit dem Zahlenwert wird verlockend sein. Widersteh. Der Sinn dieser Etappe ist, dass du Booleans wirklich verstehst, bevor du etwas Komplizierteres baust. Wenn du direkt zu Zahlen springst, überspringst du das Fundament — und in Etappe 18 fehlt es dir.

---

## Selbsttest

- [ ] Das Programm läuft von Etappe 1 durch bis zur neuen Szene
- [ ] Groß-/Kleinschreibung bei der Antwort spielt keine Rolle
- [ ] Ein Leerzeichen vor oder nach der Eingabe bricht nichts
- [ ] Es gibt mindestens drei Zweige, inklusive `else`
- [ ] `vertrauen` wird in beiden Hauptfällen gesetzt — nicht nur in einem
- [ ] Mindestens eine Bedingung benutzt `and`, `or` oder `not`
- [ ] Die Einrückung ist überall vier Leerzeichen, keine Tabs
- [ ] Du hast beide Antworten durchgespielt und beide Texte gelesen
- [ ] Keine der beiden Optionen ist erkennbar die „richtige"
- [ ] Ein Kommentar verweist auf Etappe 18

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten:

1. **Wann `elif`, wann mehrere separate `if`?** Nenn einen Fall, in dem beide dasselbe tun, und einen, in dem sie sich unterscheiden.
2. **Was ergibt `"5" == 5`? Warum?** Und was ergibt `"5" == "5.0"`?
3. **Was heißt „truthy"?** Nenn drei Werte, die als falsch gelten, ohne `False` zu sein.
4. **Was ist der Unterschied zwischen `not (a and b)` und `not a and not b`?** Beleg deine Antwort mit einer Kombination von `a` und `b`, bei der sich die beiden unterscheiden.
5. **Warum ist die Einrückung in Python keine Formatierung?** Was passiert, wenn du eine Zeile eine Ebene zu weit links schreibst?
6. **Warum reicht `== "ja"` nicht aus, um die Antwort eines Spielers zu prüfen?**

Wenn du bei Frage 4 nicht sicher bist: Das ist der Normalfall. Sie ist nicht durch Nachdenken zu lösen, sondern durch vier Zeilen Code.

---

## Transferaufgabe (10 Minuten)

**Neue Datei, außerhalb des Spiels.** `uebung_02.py`.

> Ein Türsteher. Frag nach dem Alter und danach, ob die Person auf der Gästeliste steht. Entscheide dann mit **einer** verknüpften Bedingung, ob sie hineindarf.
>
> Regel: Einlass ab 18 **und** nur mit Gästeliste. Ab 25 auch ohne Liste.

Zwei Auflagen, die den ganzen Lerneffekt ausmachen:

**Keine verschachtelten `if` im `if`.** Löse es mit `and`, `or`, `not` und `elif`. Wenn du merkst, dass du ein `if` in ein `if` schreiben willst, halt an und überleg, wie sich beide Bedingungen zu einer verbinden lassen.

**Denk an Etappe 1.** Was gibt `input()` beim Alter zurück, und was musst du damit tun, bevor du `>= 18` prüfen kannst? Wenn du diesen Fehler heute nochmal machst, ist das genau der beabsichtigte Effekt — Wiederholung ist der Punkt.

**Danach:** Schreib die Lösung ein zweites Mal, diesmal mit verschachtelten `if`. Vergleich die beiden Fassungen. Welche würdest du in vier Monaten lieber lesen?

---

## Kaputtmachen

**Experiment 1 — Die Einrückung verschieben**
Nimm eine Zeile aus einem `if`-Block und rück sie eine Ebene nach links. Kein Absturz. Aber wann läuft sie jetzt? Führ das Programm zweimal aus, mit beiden Antworten. **Das ist der wichtigste Fehler dieser Etappe** — kein Absturz, nur falsches Verhalten.

**Experiment 2 — `elif` zu `if` machen**
Ersetz alle `elif` durch `if`. Was ändert sich? Gib eine Antwort ein, die auf mehrere Bedingungen passt.

**Experiment 3 — Der Zuweisungs-Klassiker**
Schreib `if vertrauen = True:`. Lies die Fehlermeldung. Python weist dich freundlich darauf hin — nicht alle Sprachen tun das.

**Experiment 4 — Der String, der wahr ist**
```python
if "False":
    print("Das läuft tatsächlich.")
```
Warum? Was sagt dir das über den Unterschied zwischen `False` und `"False"`?

**Experiment 5 — `.lower()` entfernen**
Nimm die Umwandlung raus und tipp `Ja` mit großem J. Beobachte, in welchem Zweig du landest. Genau das würde jedem Spieler passieren, der dein Spiel zum ersten Mal startet.

**Experiment 6 — Klammern setzen und weglassen**
```python
print(True or False and False)
print((True or False) and False)
```
Zwei verschiedene Ergebnisse. Warum?

---

## Häufige Stolpersteine

| Fehlermeldung / Symptom | Was dahintersteckt | Wo du suchst |
|---|---|---|
| `IndentationError: expected an indented block` | Nach dem Doppelpunkt fehlt der eingerückte Block | Die Zeile unter dem `if` |
| `IndentationError: unindent does not match...` | Tabs und Leerzeichen gemischt | Editor-Einstellung, ganzer Block |
| `SyntaxError: invalid syntax` bei einem `if` | Doppelpunkt vergessen — oder `=` statt `==` | Die Bedingungszeile |
| `SyntaxError: cannot assign to literal` | Vergleichsrichtung verdreht (`if 5 = alter`) | Die Bedingungszeile |
| Ein Zweig läuft nie | Bedingung zu eng, oder `elif` deckt sie schon ab | Reihenfolge der Zweige |
| Eine Zeile läuft immer | Sie ist nicht eingerückt | Einrückung prüfen |
| Antwort wird nicht erkannt | Groß-/Kleinschreibung oder Leerzeichen | `.lower()` und `.strip()` |
| `TypeError: '>=' not supported between 'str' and 'int'` | Du vergleichst eine Eingabe mit einer Zahl | `int()` fehlt |

**Der wichtigste Reflex dieser Etappe:** Wenn ein Zweig sich falsch verhält, gib die Bedingung aus, bevor du sie prüfst.

```python
print(f"DEBUG: antwort ist '{antwort}'")
```

Die Anführungszeichen im Debug-Text sind kein Zufall — nur so siehst du ein verirrtes Leerzeichen. Diese Technik ist die primitivste Form von Debugging, und sie wird dich bis Etappe 29 begleiten. In Etappe 8 lernst du die bessere Variante.

---

## Abschluss

**`GELERNT.md`:**
Zwei bis drei Sätze. Und diesmal zusätzlich: Wer hat den Spieler gefunden, und warum diese Figur?

**Commit:**
```bash
git add .
git commit -m "Etappe 2: Die erste Begegnung"
git push
```

---

## Wenn du mehr willst

Optional, erst bei grünem Selbsttest.

**Eine dritte Option.** Der Spieler kann lügen — etwas erzählen, das nicht stimmt. Das braucht keine neue Technik, nur einen weiteren `elif`. Aber es legt etwas an: In Etappe 18 ist der Fremde eine unzuverlässige Informationsquelle. Wenn der Spieler das ebenfalls sein kann, wird die Symmetrie zum Thema des Spiels.

**Der Name der Figur.** Bisher hast du eine Rolle, keinen Namen. Ein Name in einer Variable ist eine Zeile — und ab Etappe 9 wird daraus ein Attribut eines Objekts. Was du heute als `versorgerin_name` anlegst, heißt dort `npc.name`.

**Die Uhrzeit als Bedingung.** Deine `tageszeit` aus Etappe 1 liegt ungenutzt herum. Lass die Figur anders reagieren, je nachdem, wie früh es ist. Das ist deine erste Bedingung, die auf gespeichertem Weltzustand beruht statt auf einer Eingabe — und genau dieses Muster trägt ab Etappe 12 das ganze Spiel.

---

> **Nächste Etappe:** [Etappe 3 — Die Game-Loop](etappe-03-die-game-loop.md) · `while`, `for`, `range()`, `break`, `continue`
> Dort hört dein Programm auf, einmal durchzulaufen. Es fängt an zu warten.
