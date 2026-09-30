# Etappe 18 — Fähigkeiten, Skillpunkte, Statuseffekte

*v1.1.0 · 2026-09-30*

> **Block 3: Der Vorposten reagiert** · Etappe 18 von 30 · [← Etappe 17](etappe-17-der-wellengenerator.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 19 →](etappe-19-speichern-und-laden.md)

**Neue Syntax heute:** 18a: ein Dictionary *Name → Restdauer* herunterzählen und Abgelaufenes danach löschen · ein abgeleiteter Wert als Methode · eine Tabelle, die beschreibt, *was* ein Effekt tut · 🧠 `return` in der Fassung der Oberklasse beendet nur diese Fassung — 18b: `a - b`, die Differenzmenge (hochgestuft aus Etappe 6) · ein leeres Set ist falsy · ein Set als Wert in einem Dictionary · eine Prüfkette, die einen Grund oder `None` liefert · 🧠 die `or`-Falle bei `0` — 18c: die Oberklasse ruft `self.methode()` auf, und die Fassung der Unterklasse läuft · 🧠 ein fehlendes `return` liefert `None`, und `None` sieht aus wie `False`

**Zeitaufwand:** 18a: 5–6 Sitzungen · 18b: 5–6 Sitzungen · 18c: 8–10 Sitzungen, à 20–30 Minuten. Knapp 100 Minuten davon sind Lesestoff — rund 30 in 18a (mit dem Anfang dieser Seite), gut 30 in 18b, gut 35 in 18c, die Abschnitte am Ende jeweils mitgerechnet. **Lies jeweils nur die Portion, an der du sitzt.**

⚠️ **Das ist die größte Etappe des Blocks, und sie ist ehrlich gerechnet.** Sie löst Versprechen aus fünfzehn Etappen ein: die Erfahrung aus 3c, das Klassengerät aus 2, die Freischaltungen aus 6, die Abklingzeit aus 13. **18c hat in der Mitte einen markierten Schnitt (⏸)** — dort hörst du guten Gewissens auf.

**Voraussetzung:** Etappe 17 abgeschlossen, Selbsttest grün. Du brauchst die Zählerphase und den Stufenaufstieg aus Etappe 13, das Raster, `welt.abstand()` und `welt.felder_in_reichweite()` aus 14, `FUNDE` und `welt.erkenntnisse` aus 15, deine Tick-Reihenfolge aus 16 in `GELERNT.md` — **und aus 17b `befehle17.txt` und den Schalter `SEED`.** Zwei Schritte heute sind reine Umbauten, und der Beweis dafür ist wieder `diff`.

**Die drei Portionen:**

| | Was passiert | Was danach anders ist |
|---|---|---|
| **18a** | Statuseffekte — Zustand mit Ablaufdatum | Ein Speier verätzt, eine Panzerbrut erschüttert. Beides hört von selbst wieder auf. |
| **18b** | Skillpunkte, ein zentrales Flag-Set, Voraussetzungen als Daten | Jede Stufe zahlt einen Punkt aus, und du entscheidest, wohin er geht. Die Zielhilfe aus Etappe 6 tut endlich etwas. |
| **18c** | Die vier Klassen bekommen ihre echten Fähigkeiten | Heilung, Durchschlag, Granate, Mine, Aura und ein mobiler Turm — und dein Trupp setzt sie selbst ein. |

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **18a** | Effekte mit Restdauer · die Effekttabelle · abgeleitete Werte statt gespeicherter | Zustand, der weder dauerhaft noch einmalig ist · warum man einen Grundwert nie „vorübergehend" verändert | — |
| **18b** | `welt.flags` · Skillpunkte · die Fähigkeitentabelle · `kann_lernen()` · zwei Passive | Haben gegen ausgeben · warum eine Voraussetzung nie gekauft sein darf · die `or`-Falle | `and`/`or` geben einen der Werte zurück |
| **18c** | `setze_ein()` und `wirke()` · sechs aktive Fähigkeiten · schwere Munition · die Trupp-KI, zum letzten Mal | Die Oberklasse ruft, die Unterklasse liefert · warum erst nach der Wirkung bezahlt wird · dürfen gegen wollen | — |

---

# Teil 18a — Statuseffekte

## Worum es geht

Dein Spiel kennt bisher zwei Sorten Zustand.

**Die eine bleibt für immer.** Eine Erkenntnis aus Etappe 15, eine Freischaltung aus Etappe 6 — einmal gesetzt, nie wieder weg.

**Die andere passiert genau einmal.** *„Der Turm ist gerade fertig geworden."* Etappe 13 hat dir beigebracht, sie am Übergang festzuhalten, weil sie sonst nach einem Takt verschwunden ist.

> **Heute kommt die dritte Sorte: Zustand, der eine Weile gilt und dann von selbst aufhört.**

Ein Speier trifft deinen Marine, und die Säure frisst drei Takte lang weiter. Eine Panzerbrut erwischt ihn, und er ist erschüttert — seine Schüsse treffen nur halb, bis es vorbei ist. Niemand muss den Effekt beenden. Er läuft ab.

**Das klingt nach dem Zähler aus Etappe 13, und es ist fast der Zähler aus Etappe 13.** Zwei Dinge sind anders, und an genau diesen beiden hängt die Portion:

- **Eine Einheit kann mehrere Effekte gleichzeitig haben**, und keiner weiß von den anderen. Ein Attribut pro Effekt reicht dann nicht mehr.
- **Ein Effekt verändert einen Wert, solange er läuft** — und danach muss der Wert wieder stimmen. Das ist die Stelle, an der Anfänger verlässlich einen Fehler bauen, der nie abstürzt.

---

## Der lange Bogen — was heute fällig wird

- **Der Tick aus Etappe 12** bekommt, was der Bogen ihm seit damals verspricht: Statuseffekte.
- **Das Zähler-Muster aus Etappe 13** — diesmal nicht ein Zähler an einem Objekt, sondern beliebig viele.
- **Die Regel aus Etappe 15, Konzept 2:** *„Sobald du wissen willst, wann oder wie lange … wird das Set falsch und ein Dictionary richtig."* Heute willst du genau das wissen.
- **`nachladen_noetig` aus Etappe 2 und 3c.** Zwei Werte, die dasselbe sagen — Fahndung 10 in Etappe 16 hat danach gefragt. Heute verschwindet der zweite, und du erfährst, warum er nie hätte entstehen müssen.
- **Der Generatorausfall aus Etappe 17c.** Dort stand: *„Den gespeicherten Schadenswert des Turms fasst du nicht an — du halbierst, was er austeilt."* Heute wird aus diesem Satz eine Regel für das ganze Spiel.
- **`GEGNERTYPEN` bekommt ein Feld mehr**, wie in 17a — und wieder keine neue Struktur.

---

## Eine Design-Entscheidung: Wo wohnt ein Statuseffekt? ⭐⭐

**Das Problem:** Vasquez ist verätzt, noch zwei Takte. Wo steht das? Drei Modelle, die man ernsthaft bauen könnte:

| | A — an der Einheit | B — an der Welt | C — als eigenes Objekt |
|---|---|---|---|
| Wie | Jede Einheit hat ein Dictionary *Effektname → Restdauer* | Die Welt führt eine Liste von Einträgen: *wer, welcher Effekt, wie lange noch* | Jede Einheit hat eine Liste von `Effekt`-Objekten mit Name und Restdauer |
| *Ist Vasquez verätzt?* | eine Frage mit `in` an Vasquez | die ganze Liste der Welt durchsuchen | Vasquez' Liste durchsuchen |
| Ein Gegner fällt und wird entfernt | seine Effekte gehen mit ihm | **sein Eintrag bleibt in der Liste der Welt liegen** und zeigt auf etwas, das es nicht mehr gibt | seine Effekte gehen mit ihm |
| Zweimal derselbe Effekt | unmöglich — ein Schlüssel steht höchstens einmal da | möglich, muss geprüft werden | möglich, muss geprüft werden |
| In Etappe 19 speichern | Wörter und Zahlen | Einträge, die auf Objekte zeigen | Objekte |

**Der Plan baut A**, und die Begründung ist die Besitzfrage aus Etappe 9 in ihrer schlichtesten Form: *Wem gehört die Säure?* Dem, der verätzt ist.

⚠️ **B ist nicht dumm.** Es ist der *Scheduler* aus Etappe 13 — die Welt führt Termine. In großen Simulationen mit tausend Einheiten ist das oft die bessere Bauart. Die mittlere Zeile zeigt, warum sie hier mehr kostet als sie bringt: Wer Einträge an der Welt führt, muss sie beim Entfernen einer Einheit mit aufräumen, und genau das vergisst man.

⚠️ **Und C ist nicht falsch, sondern verfrüht** — dieselbe Antwort wie in Etappe 13. Ein eigenes Objekt lohnt sich, sobald ein Effekt mehr trägt als eine Restdauer: wer ihn ausgelöst hat, wie stark er ist. **Heute trägt er genau eine Zahl.** Dafür ist ein Dictionary da.

**Schreib einen Satz in `GELERNT.md`**, welches Modell du genommen hättest und warum. Am Ende der Etappe kommt dieselbe Frage als Entwicklerfrage zurück — dann mit sechs Beispielen statt einem.

---

## Die Konzepte — Teil 18a

Alle Beispiele laufen **außerhalb** deines Spiels. Heute in einer Bäckerei und einem Café.

### 1. Die dritte Sorte Zustand ⭐

| Sorte | Beispiel aus deinem Spiel | Wie lange | Passende Struktur |
|---|---|---|---|
| **dauerhaft** | eine Erkenntnis | für immer | ein Set — *ist es da?* |
| **einmalig** | *„Turm gerade fertig"* | ein Takt | kein Speicher — ein Übergang, der erkannt wird |
| **befristet** | *„verätzt, noch 3 Takte"* | eine Weile | **ein Dictionary — *ist es da, und wie lange noch?*** |

**Die dritte Zeile hat zwei Ereignisse**, nicht eines: den Beginn und das Ende. Beide passieren genau einmal, beide lassen sich melden — und beide erkennst du mit dem, was du aus Etappe 13 kennst.

### 2. Viele Zähler an einem Objekt ⭐⭐

Ein Ofen mit mehreren Blechen. Jedes hat seine eigene Restzeit:

```python
timer = {"brot": 3, "brezel": 1}
```

**Ein Dictionary *Name → Restdauer*.** Solange ein Name drinsteht, läuft er. Steht er nicht drin, läuft er nicht. Jeder Takt zählt alle herunter.

**Sag voraus, bevor du weiterliest:** Was passiert hier?

```python
for sorte in timer:
    timer[sorte] -= 1
    if timer[sorte] == 0:
        print(f"{sorte} ist fertig.")
        del timer[sorte]
```

**Es knallt:**

```
RuntimeError: dictionary changed size during iteration
```

Du kennst die Regel aus Etappe 5: **Die Werte eines Dictionaries darfst du ändern, während du darüber läufst — seine Größe nicht.** `-= 1` ändert einen Wert, das ist erlaubt. `del` ändert die Größe. *(Und das knallt immer, auch wenn der gelöschte Eintrag der letzte war — Python merkt es beim nächsten Schleifenschritt, und den gibt es auch nach dem letzten Eintrag noch.)*

**Der Ausweg ist der aus Etappe 12, Konzept 11: erst sammeln, dann entfernen.**

```python
fertig = []
for sorte in timer:
    timer[sorte] -= 1
    if timer[sorte] == 0:
        fertig.append(sorte)

for sorte in fertig:
    del timer[sorte]
    print(f"{sorte} ist fertig.")
```

**Warum überhaupt löschen, statt die `0` stehen zu lassen?** Weil *„steht drin"* dann nicht mehr *„läuft"* heißt. `"brezel" in timer` wäre wahr, obwohl die Brezel längst draußen ist. Jede Frage müsste zusätzlich `> 0` prüfen, und die eine Stelle, an der du es vergisst, ist ein Fehler, der nicht abstürzt.

> **Die Regel für diese Sorte Dictionary: Ein Eintrag steht genau so lange drin, wie das Ding läuft.** Dann ist `in` die ganze Frage — wie beim Set.

**Und ein Nebeneffekt, den du geschenkt bekommst:** Die Meldung *„ist fertig"* kommt garantiert nur einmal. Nach dem Löschen gibt es keinen Eintrag mehr, der ein zweites Mal auf `0` stehen könnte. Das Ende ist damit ein echtes Ereignis, ohne dass du dafür etwas extra tun musst.

### 3. Zwei Sorten Wirkung ⭐

Ein Effekt kann auf zwei Arten wirken, und sie sitzen an verschiedenen Stellen im Code:

| | Pro Takt | Solange er läuft |
|---|---|---|
| Beispiel | Die Säure frisst jeden Takt 2 Trefferpunkte | Erschüttert: Schüsse treffen nur halb |
| Was es ist | **ein Ereignis**, das sich wiederholt | **ein Zustand**, nach dem gefragt wird |
| Wann es passiert | einmal in jeder Zählerphase | jedes Mal, wenn der Wert gebraucht wird |
| Wo es im Code steht | dort, wo heruntergezählt wird | dort, wo der Wert berechnet wird |

**Das ist die Prüffrage aus Etappe 13: *Soll das gelten, oder soll das passieren?*** Die Säure passiert. Die Erschütterung gilt.

### 4. Berechnen statt speichern ⭐⭐

**Das ist der wichtigste Abschnitt dieser Portion.**

Ein Café hat eine Happy Hour: Kaffee zum halben Preis, solange sie läuft. Der naheliegende Weg sieht so aus:

```python
# Beginn der Happy Hour
kaffee.preis = kaffee.preis // 2

# Ende der Happy Hour
kaffee.preis = kaffee.preis * 2
```

**Rechne nach, mit einem Preis von 5.** Halbieren: `5 // 2` ist `2`. Verdoppeln: `2 * 2` ist `4`. **Nach der Happy Hour kostet der Kaffee einen Euro weniger als vorher**, und niemand hat ihn billiger gemacht. Kein Absturz, keine Meldung.

Und das ist nur der erste von zwei Fehlern. **Der zweite:** Was, wenn die Happy Hour endet, ohne dass die Zeile *„Ende"* läuft — weil das Café früher schließt, weil jemand die Aktion von Hand löscht? Dann bleibt der Preis halbiert, für immer.

> **Wer einen Grundwert vorübergehend verändert, muss ihn später zurückverändern. Und zurückverändern geht schief — durch Rundung, durch vergessene Wege, durch zwei Effekte, die sich überlagern.**

**Der andere Weg fasst den Grundwert nie an:**

```python
class Kaffee:
    def __init__(self, preis):
        self.preis = preis
        self.aktionen = {}          # Aktion -> Restdauer

    def aktueller_preis(self):
        wert = self.preis
        if "happy_hour" in self.aktionen:
            wert = wert // 2
        return wert
```

`self.preis` bleibt `5`, immer. Wer wissen will, was der Kaffee **gerade** kostet, fragt `aktueller_preis()` — und die Methode rechnet es aus dem Grundwert und den laufenden Aktionen jedes Mal neu aus. Endet die Aktion, stimmt der Preis von selbst, weil er nie falsch war.

**Das heißt abgeleiteter Wert:** ein Wert, der sich aus anderen Werten ergibt und deshalb nicht gespeichert, sondern bei Bedarf berechnet wird. Du kennst den Gedanken seit Etappe 3c: *Was aus Zustand entsteht, wird beim Anzeigen erzeugt, nicht aufbewahrt* — damals die Länge eines Balkens. Und Etappe 17c hat ihn beim Generatorausfall schon einmal verlangt.

**Und jetzt erkennst du eine alte Stelle in deinem eigenen Programm wieder.** `nachladen_noetig` aus Etappe 3c ist ein gespeicherter Wert, der sich aus einem anderen ergibt: Ob du nachladen musst, steht bereits in deinem Magazinstand. Zwei Werte, die dasselbe sagen, können sich widersprechen — und genau das hat Fahndung 10 in Etappe 16 gesucht. **Die Krankheit ist dieselbe wie beim Kaffeepreis: eine Kopie von etwas, das man jederzeit fragen könnte.**

### 5. Die Tabelle sagt, was ein Effekt tut

Die Happy Hour oben steht mit ihrem Namen in der Methode. Beim dritten Effekt hast du drei `if`-Zweige, beim zehnten zehn. **Das ist die `if`-Kette aus Etappe 15, Konzept 4**, und dieselbe Antwort passt: Die Wirkung gehört in eine Tabelle.

```python
AKTIONEN = {
    "happy_hour":  {"halbiert": "preis"},
    "baustelle":   {"halbiert": "sitzplaetze"},
}

class Kaffee:
    def aktueller_preis(self):
        wert = self.preis
        for name in self.aktionen:
            if AKTIONEN[name]["halbiert"] == "preis":
                wert = wert // 2
        return wert
```

**Lies die Schleife als Satz:** *Für jede laufende Aktion — halbiert sie den Preis?* Die Methode fragt nie, **welche** Aktion es ist, sondern nur, **was** sie tut. Eine neue Aktion, die den Preis halbiert, ist eine Zeile in der Tabelle und keine Zeile in der Methode.

> **Der Tick fragt nie, was ein Objekt ist (Etappe 13). Die Rechnung fragt nie, wie ein Effekt heißt.** Dieselbe Idee, einmal für Objekte, einmal für Daten.

*(Die Baustelle halbiert etwas anderes — die Sitzplätze. Sie steht in derselben Tabelle und wirkt an einer anderen Stelle. Genau so wirst du heute zwei Richtungen bauen.)*

### 6. Erneuern, verlängern, stapeln

Ein Speier trifft Vasquez, der noch zwei Takte verätzt ist. **Was passiert?** Drei Antworten, und jede ist eine Spielregel:

| | Erneuern | Verlängern | Stapeln |
|---|---|---|---|
| Was passiert | die Restdauer wird wieder auf die volle Dauer gesetzt | die volle Dauer kommt zur Restdauer dazu | ein zweiter, eigener Effekt läuft daneben |
| Nach zehn Speiern | 3 Takte | 30 Takte | zehnmal Schaden pro Takt |
| Wie im Code | eine Zuweisung | `+=` | geht mit *Name → Restdauer* nicht — jeder Name bräuchte dafür mehrere Restdauern |

**Der Plan nimmt „Erneuern"** — und hier siehst du, wie eng Spielregel und Datenstruktur zusammenhängen: **Die Struktur *Name → Restdauer* kann Erneuern und Verlängern, aber kein Stapeln.** Wer stapeln will, braucht ein anderes Modell, nicht eine andere Zeile. Erneuern gibt dir das Dictionary geschenkt: Eine Zuweisung an einen Schlüssel, der schon da ist, überschreibt ihn. **Ein Schlüssel steht höchstens einmal im Dictionary** — dieselbe Zusage wie beim Set in Etappe 6, und sie ist hier die Spielregel „derselbe Effekt nie doppelt".

⚠️ **Verlängern klingt harmlos und ist es nicht.** Ohne Obergrenze wächst eine Restdauer mit jedem Treffer, und nach einer großen Welle ist ein Effekt praktisch dauerhaft. *(Kaputtmachen 5 lässt dich das sehen.)*

### 7. Wann beginnt ein Effekt, wann endet er?

**Dieselbe Frage wie in Etappe 13, Schritt 7, und diesmal ist sie gemeiner.**

Ein Effekt wird gesetzt, wenn ein Gegner trifft — in der **Gegnerphase**. Heruntergezählt wird er in der **Zählerphase**, und die steht in deinem Tick seit Etappe 13 **vor** der Truppphase. Dein Held handelt dagegen gar nicht im Tick, sondern **zwischen** zwei Ticks: Befehl, dann Tick.

**Deshalb eine harte Definition, und sie gilt für das ganze Spiel:**

> **`dauer = 3` heißt: Der Effekt steht in genau drei Zählerphasen im Dictionary.** In jeder davon wirkt, was in der Zählerphase wirkt — die Säure frisst —, und in der dritten wird er gelöscht.

**Die Dauer ist damit für jede Einheit gleich.** Verschieden ist nur, **wie oft eine Einheit handelt, während der Effekt noch dasteht** — und das hängt davon ab, wann sie handelt: Der Held handelt zwischen zwei Ticks, ein Kamerad in der Truppphase, also **nach** der Zählerphase desselben Takts. Eine Erschütterung mit Dauer 3 kann deshalb drei Schüsse des Helden halbieren und nur zwei eines Kameraden.

**Das ist kein Fehler, solange du es weißt.** Es ist einer, sobald du *„drei Takte"* sagst und *„drei Schüsse"* meinst. Auftragsschritt 5 lässt dich die Zahlen **vor** dem Ausführen aufschreiben.

---

## Dein Auftrag — Teil 18a

Nach **jedem** Schritt ausführen und einen Tick auslösen. Effekte sieht man nur in Bewegung.

---

### 1. Leg die Effekttabelle an und gib zwei Gegnertypen einen Effekt

**`EFFEKTE`**, oben bei deinen anderen festen Werten, nach Konzept 5:

| Kennung | `"dauer"` | `"pro_tick"` | `"halbiert"` | Wer ihn auslöst |
|---|---|---|---|---|
| `"veraetzt"` | 3 | 2 | `None` | der Speier, heute |
| `"erschuettert"` | 3 | 0 | `"ausgehend"` | die Panzerbrut, heute |
| `"abgeschirmt"` | 4 | 0 | `"eingehend"` | die Aura des Medic, in 18c |

`"pro_tick"` ist der Schaden in jeder Zählerphase. `"halbiert"` sagt, **welchen** Schaden der Effekt halbiert: den, den die Einheit **austeilt**, den, den sie **nimmt**, oder keinen.

⚠️ **Der dritte Effekt steht heute schon da, obwohl ihn erst 18c auslöst.** Die Tabelle soll von Anfang an zeigen, dass es drei Arten Wirkung gibt — und in Schritt 6 baust du beide Richtungen, damit die Aura in 18c nur noch eine Zeile Auslöser braucht.

**In `GEGNERTYPEN`** bekommen zwei Einträge einen neuen Schlüssel `"effekt"`: der Speier `"veraetzt"`, die Panzerbrut `"erschuettert"`. **Der Kriecher bekommt keinen** — und gelesen wird deshalb mit `.get()`, die Regel für ungleichmäßige Daten aus Etappe 5.

**So prüfst du es — in einer frisch kopierten Probedatei**, wie seit Etappe 9: `print(EFFEKTE["erschuettert"]["halbiert"])` und `print(GEGNERTYPEN["kriecher"].get("effekt"))`. Du erwartest `ausgehend` und `None`.

---

### 2. Gib jeder Einheit ein Effekt-Dictionary

- `Einheit.__init__` bekommt ein Attribut `effekte`, ein leeres Dictionary.
- Eine neue Methode `bekomme_effekt(name, welt)` in `Einheit`:
  - Steht die Einheit auf `"tot"`: sofort zurück, nichts passiert.
  - Steht der Name **noch nicht** in `self.effekte`: den Beginn melden.
  - Dann die Restdauer auf die volle Dauer aus `EFFEKTE` setzen — **erneuern**, nach Konzept 6.

⚠️ **Die Reihenfolge der beiden letzten Zeilen ist der Punkt.** Erst fragen, ob er neu ist, dann setzen. Andersherum steht er beim Fragen schon drin, und der Beginn wird nie gemeldet. Das ist *merken, neu berechnen, vergleichen* aus Etappe 13, Konzept 4, in seiner kleinsten Form.

*(Sofort melden oder in den Wellenbericht? Die Frage aus Etappe 17c: Muss der Spieler jetzt etwas tun? Beim Helden vermutlich ja, bei einem Kameraden vielleicht nicht. Deine Wahl — schreib sie auf.)*

**So prüfst du es:** In der Probedatei eine Einheit erzeugen, `bekomme_effekt("veraetzt", welt)` zweimal aufrufen, dann `print(einheit.effekte)`. **Eine Meldung, nicht zwei — und `{'veraetzt': 3}`.**

---

### 3. Lass die Gegner ihren Effekt übertragen

Such die Stelle, an der ein Gegner am Tor eine Einheit des Trupps trifft — seit Etappe 12b, und welche Einheit es trifft, hast du damals selbst entschieden.

- Direkt nach dem Schaden: den Effekt des Gegnertyps mit `.get()` aus `GEGNERTYPEN` holen. Der Gegner kennt seinen Typ über seinen `name` — seit Etappe 11b.
- Ist er nicht `None`: `bekomme_effekt()` bei **derselben** Einheit, die den Schaden genommen hat.

**So prüfst du es:** Lass die Wellenschleife testweise bei `8` beginnen, wie in 17b, und spiel, bis ein Speier oder eine Panzerbrut das Tor erreicht. Die Beginn-Meldung erscheint. *(Noch läuft der Effekt nie ab — das kommt in Schritt 4. Danach den Startwert zurück auf `1`.)*

---

### 4. ⭐⭐ Zähl die Effekte herunter

**Das ist der Auftragsschritt dieser Portion.**

Deine `Einheit.zaehler_runter(welt)` ist seit Etappe 13 ein Docstring und sonst nichts. **Ab heute tut sie etwas**, nach Konzept 2:

- Steht die Einheit auf `"tot"`: sofort zurück.
- Für jeden Effekt in `self.effekte`: den Schaden aus `"pro_tick"` über `self.nimm_schaden()` nehmen, **aber nur, wenn er größer als 0 ist**, dann die Restdauer um eins verringern. Ist sie auf `0` gekommen: den Namen in eine Liste `abgelaufen` legen.
- **Nach der Schleife:** jeden Namen aus `abgelaufen` mit `del` aus `self.effekte` löschen und das Ende melden.

*(Fällt eine Einheit dabei an ihrer Säure, ist das in Ordnung: Die Aufräumphase aus Etappe 13 kümmert sich um sie, wie um jeden anderen Ausfall.)*

⚠️ **Und jetzt der Handgriff, den kein Register beantwortet: Wer überschreibt `zaehler_runter`?** Seit Etappe 13 mindestens `Marine` — für den Ausfall, die Nachladezeit, die Abklingzeit — und dein `Basisturm` für die Bauzeit. **Jede dieser Fassungen ersetzt die aus `Einheit` vollständig.** Ohne weiteres läuft die neue Effektlogik also bei keinem einzigen Marine.

- **Such alle Klassen, die `zaehler_runter` überschreiben, und zähl sie.** Die Fahndung aus Etappe 5, diesmal nach einem Methodennamen.
- In jede davon kommt **als erste Zeile** `super().zaehler_runter(welt)` — die Form aus Etappe 11, Konzept 8.

⚠️ **Eine Stelle, die nach einem Widerspruch aussieht und keiner ist:** Die Fassung in `Einheit` steigt bei `"tot"` sofort aus. Die Fassung in `Marine` muss aber gerade bei `"tot"` weiterlaufen — der Ausfallzähler aus Etappe 13 zählt ja, während der Marine liegt. **Beides geht, weil `return` nur die Methode verlässt, in der es steht.** Der Aufruf `super().zaehler_runter(welt)` kehrt zurück, und die Marine-Fassung läuft mit ihrer nächsten Zeile weiter.

**So prüfst du es — zweimal in der Probedatei:**

1. Eine nackte `Einheit` mit 20 Trefferpunkten, `bekomme_effekt("veraetzt", welt)`, dann viermal `zaehler_runter(welt)` und nach jedem Aufruf Trefferpunkte und `effekte` ausgeben. **Schreib vorher auf, was du erwartest.**
2. Dasselbe mit einem `Marine`. **Wenn der Marine keinen Schaden nimmt und der Effekt nie endet, fehlt der `super()`-Aufruf.**

---

### 5. ⭐ Leg fest, was „drei Takte" bedeutet

**Bevor du weiterbaust, und zwar schriftlich** — die Zeitsemantik aus Etappe 13, Schritt 7, angewandt auf Konzept 7.

Bau dafür einen **Entwicklerbefehl** `test_effekt <name>`, der den Effekt deinem Helden gibt — die Erlaubnis dafür steht seit Etappe 3a: Entwicklerbefehle sind erlaubt und werden vor dem Commit entfernt. *(Ist der Name nicht in `EFFEKTE`, meldet der Befehl das, statt mit `KeyError` abzustürzen. Und er kostet keine Zeit.)*

Dann in `GELERNT.md`, **vor** dem Ausführen:

| Nach dem Befehl `test_effekt …` | Restdauer | Ätzschaden in diesem Tick? | Nächster Schuss des Helden halbiert? |
|---|---|---|---|
| Tick 1 | | | |
| Tick 2 | | | |
| Tick 3 | | | |
| Tick 4 | | | |

Füll sie zweimal aus — einmal für `veraetzt`, einmal für `erschuettert`. Zwischen den Ticks gibst du jeweils `feuern`. **Dann führ es aus und vergleich Zelle für Zelle**, wie die Tick-Tabelle aus Etappe 16.

**Und die Frage, die danach kommt:** Ein **Kamerad** handelt in der Truppphase, **nach** der Zählerphase. Wie viele seiner Schüsse wären bei `erschuettert` halbiert? **Die Dauer ist dieselbe — die Zahl der betroffenen Schüsse muss es nicht sein** (Konzept 7). Schreib auf, warum — und ob du das so lassen willst. *(Lassen ist eine gültige Antwort, wenn du den Unterschied erklären kannst.)*

⚠️ **Der Befehl setzt den Effekt außerhalb des Ticks — ein Gegner setzt ihn mitten in der Gegnerphase.** Rechne für Schritt 3 nach, ob sich an deiner Tabelle dadurch etwas verschiebt. Ein Satz dazu in `GELERNT.md`.

---

### 6. ⭐⭐ Bau die abgeleiteten Werte

Nach Konzept 4 und 5 — **zwei Richtungen**:

**Ausgehend.** `Einheit` bekommt eine Methode `aktueller_schaden()`. Sie beginnt mit `self.schaden`, läuft über die laufenden Effekte und halbiert den Wert mit `//` für jeden, dessen `"halbiert"` auf `"ausgehend"` steht. Sie gibt das Ergebnis zurück und **verändert nichts**.

**Eingehend.** In `nimm_schaden(menge)` wird die Menge **vor** dem Abziehen halbiert, für jeden laufenden Effekt mit `"eingehend"`. Auch hier: nur die Menge in diesem Aufruf, kein Attribut.

⚠️ **Und dann die Fahndung, die den Schritt ausmacht:** Such jede Stelle, an der eine Einheit **Schaden austeilt**, und zähl sie. Der Held beim `feuern` — über deine Schadensberechnung aus Etappe 7, der du den Schaden des Helden übergibst —, die Kameraden in `update()`, dein Basisturm. **An jeder dieser Stellen steht ab heute `aktueller_schaden()` statt `self.schaden`.**

⚠️ **`self.schaden` wird nach `__init__` nirgends mehr zugewiesen.** Such auch danach. Eine einzige Zuweisung irgendwo, und du hast den Kaffee aus Konzept 4 gebaut.

*(Der halbierte Turmschaden aus Etappe 17c bleibt, wo er ist. Er sitzt schon richtig — er halbiert, was ausgeteilt wird. Ob er zuerst oder nach `aktueller_schaden()` halbiert, ändert am Ergebnis übrigens nichts: Zweimal halbieren mit `//` ist in jeder Reihenfolge dasselbe.)*

**So prüfst du es:** `test_effekt erschuettert`, dann `feuern` — der Gegner verliert halb so viel. Warten, bis der Effekt abläuft, dann `feuern` — wieder voller Schaden. **Und `print(welt.held)` zeigt denselben Schadenswert wie vor dem Effekt.** Dann `test_effekt abgeschirmt` und dich treffen lassen: halber Schaden.

---

### 7. ⭐ Räum `nachladen_noetig` weg

Nach Konzept 4, letzter Absatz. **Hast du die Variable in Etappe 16 schon aufgelöst, ist dieser Schritt ein Häkchen.**

- Such jede Stelle, an der `nachladen_noetig` **gesetzt** wird, und jede, an der es **gelesen** wird. Zähl beide.
- Jede lesende Stelle fragt ab heute direkt den Wert, aus dem es sich ergibt — deinen Magazinstand. Wenn dieselbe Frage an mehr als einer Stelle steht, lohnt sich eine kleine Methode, die sie beantwortet.
- Jede setzende Stelle wird gelöscht.

⚠️ **Eine der lesenden Stellen ist alt und interessant:** die Bedingung, unter der dein Held feuern darf. Seit Etappe 2 ist sie eine verknüpfte Bedingung — damals `ziel_in_sicht and not nachladen_noetig`, seit Etappe 14b mit der Reichweite statt `ziel_in_sicht`. **Merk dir die Form.** In 18c bekommt jede Fähigkeit eine Prüfung derselben Sorte, und dort erfährst du, was ihr fehlt.

**So prüfst du es:** Das Wort `nachladen_noetig` kommt im Code nicht mehr vor. Magazin leerschießen, `feuern` — abgewiesen wie vorher. Nachladen, `feuern` — geht.

---

### 8. Mach Effekte sichtbar, und lösch sie beim Ausfall

**Anzeige.** Deine Statusanzeige zeigt bei jeder Einheit des Trupps ihre laufenden Effekte mit Restdauer — etwa `verätzt(2) erschüttert(1)`. Eine Schleife mit `.items()` aus Etappe 5. *(Ein Dictionary gibt seine Einträge in der Reihenfolge zurück, in der sie hineingekommen sind. Das Problem aus 17b mit Sets hast du hier nicht.)*

**Ausfall.** Such die Stelle in deiner Aufräumphase, an der eine gefallene Einheit des Trupps ihren Ausfallzähler bekommt — seit Etappe 13. Dort bekommt `effekte` ein neues, leeres Dictionary. **Wer wieder aufsteht, steht ohne Effekte auf.**

*(Warum das sein muss, obwohl Schritt 4 tote Einheiten überspringt: Ohne das Löschen stünde Vasquez nach dem Aufstehen noch verätzt da — mit der Restdauer von vor seinem Ausfall.)*

**So prüfst du es:** `status` mit laufendem Effekt — er steht da. Dich absichtlich fallen lassen, während du verätzt bist — nach dem Aufstehen ist `effekte` leer.

---

### 9. Prüf, dass das Alte noch läuft, und commit

- Kaufen, verkaufen, nachladen, Sektor wechseln, Fähigkeit, Turmbau, Analysieren, Wellenbericht: alles wie vorher?
- Beide Verlustbedingungen?
- **Der Entwicklerbefehl `test_effekt` ist gelöscht.** Keine `probe.py`, kein Testwert in der Wellenschleife.
- Die Abschnitte am Ende, die zu 18a gehören: **Transferaufgabe** und **Kaputtmachen 1 bis 3**.

Commit: `Etappe 18a: Statuseffekte`

---

## Selbsttest — 18a

- [ ] Ein Effekt, zweimal hintereinander gegeben, meldet seinen Beginn **einmal** und steht **einmal** im Dictionary — mit voller Restdauer.
- [ ] `veraetzt` macht genau so oft Schaden, wie deine Tabelle aus Schritt 5 sagt, und meldet danach genau einmal sein Ende.
- [ ] Nach dem Ende steht der Effektname **nicht mehr** im Dictionary.
- [ ] Jede Klasse, die `zaehler_runter` überschreibt, ruft als erste Zeile `super().zaehler_runter(welt)` — und du kennst ihre Zahl.
- [ ] Während `erschuettert` läuft, teilt der Held halben Schaden aus. **Danach wieder vollen — und `self.schaden` hat sich nie verändert.**
- [ ] `self.schaden` wird nach `__init__` nirgends zugewiesen.
- [ ] `abgeschirmt` halbiert den Schaden, den eine Einheit nimmt.
- [ ] Ein Kriecher am Tor überträgt keinen Effekt, und es gibt keinen `KeyError`.
- [ ] `nachladen_noetig` kommt im Code nicht mehr vor.
- [ ] Wer ausfällt, steht ohne Effekte wieder auf.
- [ ] Die Tabelle aus Schritt 5 steht ausgefüllt in `GELERNT.md`, mit dem Unterschied zwischen Held und Kamerad.

> **⏸ Ende von 18a.** Dein Spiel kennt jetzt drei Sorten Zustand. 18b zahlt die Erfahrung aus, die seit Etappe 3c mitzählt.

---

# Teil 18b — Skillpunkte und Voraussetzungen

## Worum es geht

Seit Etappe 3c steigt eine Zahl, wenn du einen Gegner erledigst. Seit Etappe 5 weißt du, ab wann sie welche Stufe bedeutet. Seit Etappe 13 meldet sich dein Marine, wenn er aufsteigt. **Und seit fünfzehn Etappen tut das alles nichts.**

> **Heute zahlt jede Stufe einen Skillpunkt aus, und du entscheidest, wofür.**

Dafür braucht dein Spiel drei Dinge, die es noch nicht hat: einen Ort, an dem steht, **was du weißt und besitzt** — ein zentrales Set. Eine Tabelle, in der steht, **was es zu lernen gibt und unter welchen Bedingungen**. Und eine Prüfung, die **nicht nur Nein sagt, sondern warum**.

**Und dein Klassengerät aus Etappe 2 wird zum ersten Mal abgefragt.** Sechzehn Etappen lang war es ein String, der angezeigt wurde. Ab heute entscheidet es, welche Fähigkeiten dir offenstehen.

---

## Der lange Bogen — was heute fällig wird

- **Der Fortschritt deiner Figur:** `erfahrung` aus 3c, die Stufentabelle aus 5, `level` aus 9a, der Stufenaufstieg aus 13. Heute zahlt er aus.
- **`klassengeraet` aus Etappe 2** — angezeigt seit Etappe 2, gesperrt in 4, 5, 10 und 13. Heute wird es zur Wurzel deines Fähigkeitenbaums.
- **Drei Speicher werden einer:** `freigeschaltet` aus Etappe 6, `welt.erkenntnisse` aus Etappe 15, `welt.meldung_abgesetzt` aus Etappe 2 und 17c. Etappe 6 hat versprochen, dass `freigeschaltet` der zentrale Flag-Speicher wird; Etappe 17 hat gesagt, die Funkentscheidung gehe darin auf.
- **Der Zettel aus Etappe 6:** *„Das Schnellfeuer sollte erst gehen, wenn die Zielhilfe da ist."* Etappe 6 hat dir verboten, das als `if` zu bauen, weil es in Etappe 18 ein Eintrag in den Daten wird. Hol den Zettel hervor.
- **Die Zielhilfe aus Etappe 6**, die seitdem *„kalibriert noch"* — heute bekommt sie ihre Wirkung.
- **Die Mengenoperationen aus Etappe 6.** Dort stand: *„In Etappe 18 lautet die Frage: Welche Voraussetzungen fehlen mir noch? — und die Antwort ist eine Differenzmenge."*
- **Die Umkehrtabelle aus Etappe 15** — zum dritten Mal: *Sache → Voraussetzung.*
- **Die drei Stufen aus Etappe 15** — Fundstück, Besitz, Erkenntnis — bekommen ein Gegenstück: Erfahrung, Skillpunkt, Fähigkeit.
- **Die zwei Sorten Nein aus Etappe 6, Konzept 12.** Dort stand, die zweite werde in Etappe 18 die häufigste Meldung im ganzen Spiel. Hier ist sie.
- **`and` und `or` aus Etappe 2** — als Lesestoff, und mit der Null-Falle aus Etappe 10.
- **Deine Entscheidungen zum versiegelten Weg (Etappe 5) und zum zweiten Freischalten (Etappe 6):** *fehlt* oder *markiert*, *ausblenden* oder *sichtbar lassen*. Heute stellt sich dieselbe Frage für Fähigkeiten, die du noch nicht lernen kannst.

---

## Zwei Design-Entscheidungen

### Ein Set oder drei? ⭐

**Das Problem:** Dein Spiel merkt sich an drei Stellen, dass etwas geschehen ist oder dir gehört — in drei verschiedenen Bauformen:

| | Heute | Bauform |
|---|---|---|
| Freischaltungen | `freigeschaltet` | Set aus Etappe 6 |
| Erkenntnisse | `welt.erkenntnisse` | Set aus Etappe 15 |
| Funkmeldung beim ersten Kontakt | `welt.meldung_abgesetzt` | Boolean aus Etappe 2 |

Die Frage ist bei allen dieselbe: *Ist das der Fall?* **Und ab heute wird sie gemischt gestellt** — eine Freischaltung kann eine andere voraussetzen, eine Fähigkeit eine Erkenntnis.

| | Drei Speicher | Ein Set `welt.flags` |
|---|---|---|
| *Ist X der Fall?* | erst wissen, in welchem Speicher X steht | eine Frage mit `in` |
| *Was fehlt mir für diese Fähigkeit?* | je Speicher einzeln prüfen | eine Differenzmenge |
| Etappe 19 speichert | drei Dinge | eines |
| Das Risiko | ein Wort im falschen Speicher gesucht | **zwei Quellen benutzen dasselbe Wort**, und beide Bedeutungen fallen zusammen |

**Der Plan nimmt das eine Set, `welt.flags`**, und bezahlt das Risiko in der letzten Zeile mit einer Invariante:

> **Jedes Wort in `welt.flags` hat genau eine Quelle, und keine zwei Quellen benutzen dasselbe Wort.** Erkenntnis-Wörter kommen aus `FUNDE`, Freischaltungen aus `AUSBAUTEN`, und `"meldung_abgesetzt"` steht als einziges Wort ohne Tabelle da.

Das ist die Regel aus Etappe 15, Konzept 1 — *eine Quelle definiert die Wörter* —, auf drei Quellen erweitert.

**Und was gehört in dieses Set?** Die Regel dafür: **Etwas ist geschehen oder erworben, bleibt so und braucht keine weitere Angabe.** Eine Erkenntnis, eine Freischaltung, eine Funkmeldung — ja. Ein Effekt mit Restdauer — nein, der braucht eine Zahl und ist ein Dictionary (18a). Eine Fähigkeit mit Stufe — nein, aus demselben Grund.

*(`welt.funk_gehoert` aus Etappe 17c passt nach dieser Regel auch hinein. Ob du ihn umziehst, entscheidest du — Auftragsschritt 10.)*

### Was darf eine Voraussetzung sein? ⭐⭐

Eine Fähigkeit wird freigeschaltet, wenn Bedingungen erfüllt sind. **Welche Bedingungen dürfen das sein?**

Die Regel aus *Die zwei Machtquellen* im Lehrplan beantwortet es:

> **Erfahrung entscheidet, *was* du kannst. Vaporium entscheidet, *womit* du es tust.**

| Darf eine Fähigkeit voraussetzen … | | Warum |
|---|---|---|
| eine Mindeststufe | **ja** | Das ist die Erfahrung selbst |
| das richtige Klassengerät | **ja** | Das ist deine Rolle, seit Etappe 1 |
| eine Erkenntnis | **ja** | Wissen ist verdient, nicht gekauft |
| eine Freischaltung aus `AUSBAUTEN` | **nein** | Die kostet Vaporium — dann wäre die Fähigkeit gekauft |
| genug Vaporium | **nein** | Aus demselben Grund |

**Die vierte Zeile ist die, an der die Regel verletzt wird, ohne dass man es merkt**, weil seit heute alle Wörter im selben Set stehen. `"zielhilfe" in welt.flags` sieht genauso aus wie `"schwachpunkt_kriecher" in welt.flags`. Der Unterschied steht nicht im Set, sondern in der Herkunft des Wortes — und deshalb prüfst du ihn beim Schreiben der Tabelle, nicht beim Ausführen.

⚠️ **Was eine Fähigkeit durchaus kosten darf, ist ihr *Einsatz*** — schwere Munition in 18c. Das ist das *womit*.

---

## Die Konzepte — Teil 18b

Heute in einer Tanzschule.

### 8. Haben und ausgeben ⭐

| Etappe 15 | Heute |
|---|---|
| Ein **Fundstück** liegt im Vorfeld | **Erfahrung** sammelt sich |
| Eingesammelt wird es zum **Besitz** | Beim Aufstieg wird daraus ein **Skillpunkt** |
| Analysiert wird es zur **Erkenntnis** | Ausgegeben wird er zur **Fähigkeit** |

**Der Übergang in die dritte Stufe ist wieder eine Handlung des Spielers.** Ein Skillpunkt, den du nicht ausgibst, ist ein Besitz ohne Wirkung — wie eine Probe, die du nie analysierst.

**Und der Skillpunkt ist ein Zähler, kein Set.** Du kannst zwei davon haben. Wer sie als Wahrheitswert führt (*„hat einen Punkt"*), verliert beim zweiten Aufstieg einen.

*(Zahl beim Aufstieg deshalb die **Differenz** aus, nicht einen Punkt: neue Stufe minus alte. Wer mit einem Schlag zwei Stufen steigt, bekommt zwei Punkte. Bei deinen Schwellen passiert das selten — aber „selten" ist kein Grund, es falsch zu bauen.)*

### 9. Die Voraussetzungstabelle — die Umkehrtabelle, zum dritten Mal

Eine Tanzschule legt fest, wer welchen Kurs belegen darf:

```python
KURSE = {
    "grundkurs":   {"ab_alter": 12, "braucht": set()},
    "tango":       {"ab_alter": 16, "braucht": {"grundkurs"}},
    "turnier":     {"ab_alter": 18, "braucht": {"grundkurs", "tango"}},
}
```

**Lies jede Zeile als Satz:** *Für Tango brauchst du 16 Jahre und den Grundkurs.* Das ist die Umkehrtabelle aus Etappe 15 — *Sache → Voraussetzung* —, nur dass eine Sache jetzt mehrere Voraussetzungen haben kann. **Deshalb steht dort kein Wort, sondern ein Set.**

Ein Set als Wert in einem Dictionary ist nichts Neues, nur neu zusammengesetzt: `{"grundkurs"}` kennst du aus Etappe 6, den verschachtelten Zugriff `KURSE["tango"]["braucht"]` aus Etappe 5. **Und ein Kurs ohne Voraussetzung bekommt `set()`, nicht `{}`** — `{}` wäre ein leeres Dictionary, die Falle aus Etappe 6, Konzept 2.

*(`"ab_alter"` ist übrigens dieselbe Bauart wie `"ab_welle"` aus Etappe 17a: eine Schwelle, die in den Daten steht statt in einer `if`-Kette.)*

### 10. ⭐⭐ Was fehlt noch? — die Differenzmenge

Etappe 6 hat dir drei Zeichen gezeigt und gesagt, du sollst sie nur erkennen. **Eines davon brauchst du heute zum Bauen:**

```python
braucht = {"grundkurs", "tango"}
hat     = {"grundkurs", "salsa"}

fehlend = braucht - hat
print(fehlend)             # {'tango'}
```

**`a - b` ist alles, was in `a` steht und nicht in `b`.** Die Reihenfolge der beiden Seiten zählt: `hat - braucht` wäre `{'salsa'}` — das, was du hast und niemand verlangt.

**Und die Frage *„fehlt überhaupt etwas?"* ist die Frage, ob das Ergebnis leer ist.** Ein leeres Set ist **falsy**, wie die leere Liste aus Etappe 4 und das leere Dictionary aus Etappe 17a:

```python
if fehlend:
    print("Da fehlt noch etwas.")
```

`&` und `|` bleiben 👀 — du brauchst sie heute nicht.

⚠️ **Und jetzt die Stelle, an der die Differenzmenge dich in den Fuß schießt, wenn du nicht aufpasst.** `fehlend` ist ein Set, und ein Set hat keine feste Reihenfolge — die Reihenfolge seiner Einträge kann sich **zwischen zwei Programmstarts** ändern. Das hast du in Etappe 17b, Konzept 11, gesehen, und dort stand auch, was es anrichtet: Gibst du `fehlend` direkt aus, redet `diff` beim Beweislauf, obwohl dein Seed fest ist.

**Der Ausweg ist der aus Etappe 6, Konzept 3:** Zum **Entscheiden** nimmst du das Set. Zum **Ausgeben** läufst du über eine Sammlung mit fester Reihenfolge — eine Tabelle — und fragst bei jedem Eintrag mit `in`, ob er in `fehlend` steht.

### 11. ⭐⭐ Eine Prüfkette, die sagt, was fehlt

Darf jemand am Tango-Kurs teilnehmen? Die Form aus Etappe 2 beantwortet das in einer Zeile:

```python
darf = alter >= 16 and hat_grundkurs and bezahlt
```

**Das ist eine gute Zeile, und ihr fehlt genau eine Sache:** Steht dort `False`, weißt du nicht, **welcher** Teil gescheitert ist. Etappe 2 hat das als Erkenntnis notiert. Der Tänzer am Empfang will aber nicht *„Nein"* hören, sondern *„Erst ab 16."*

**Dieselbe Frage, als Kette mit frühem `return`** — die Form aus Etappe 7, Konzept 4:

```python
def einwand(alter, hat_grundkurs, bezahlt):
    if alter < 16:
        return "Erst ab 16."
    if not hat_grundkurs:
        return "Erst den Grundkurs."
    if not bezahlt:
        return "Die Gebühr fehlt noch."
    return None
```

**Die Funktion gibt einen Grund zurück — oder `None`, wenn es keinen gibt.** Lies den Namen mit: *Einwand?* — `None` heißt *kein Einwand*.

| | `and`-Kette | Prüfkette mit Grund |
|---|---|---|
| Beantwortet | *darf er?* | *darf er — und wenn nicht, warum?* |
| Länge | eine Zeile | eine Zeile pro Bedingung |
| Wer braucht die Antwort | eine Stelle, die nur Ja oder Nein braucht | **der Spieler** |

**Und jetzt der Punkt, an dem beide zusammenkommen:** `einwand(...) is None` ist **genau dasselbe** wie `darf`. Wer nur Ja oder Nein braucht, fragt `is None` — die Prüfung aus Etappe 10. **Eine Funktion, zwei Sorten Aufrufer.** In 18c ist der eine dein Befehl, der dem Spieler den Grund zeigt, und der andere ein Kamerad, dem der Grund egal ist.

⚠️ **Zwei Regeln, ohne die die Kette lügt:**

- **Jeder Zweig endet mit einem `return`**, und am Ende steht `return None` ausdrücklich — die Regel aus Etappe 15, Konzept 5.
- **Die Reihenfolge ist die Reihenfolge der Auskunft.** Gibt es mehrere Gründe, sieht der Spieler nur den ersten. Stell den nach vorne, der ihm am meisten sagt.

### 12. 👀 `and` und `or` geben einen der Werte zurück — und die Null-Falle

**Nur erkennen, nicht bauen.** Etappe 2 hat es dir gezeigt: `and` und `or` liefern nicht unbedingt `True` oder `False`, sondern **einen ihrer beiden Werte.**

```python
name = eingabe or "Gast"
```

`or` schaut links. Ist das truthy, kommt es zurück, und **die rechte Seite wird gar nicht erst ausgewertet.** Ist es falsy, kommt die rechte Seite zurück. Tippt jemand nichts ein, ist `eingabe` der leere String — falsy —, und `name` wird `"Gast"`. Das ist die Form, die dir in fremdem Code ständig begegnet: **ein Ersatzwert in einer Zeile.**

**Und jetzt die Falle.** Ein Kurs trägt ein, wie viele Plätze er hat:

```python
plaetze = gewuenscht or 10
```

Soll ein Kurs **null** Plätze haben — etwa weil er vorübergehend ausfällt —, steht links `0`. Und `0` ist falsy. **Aus null Plätzen werden zehn**, ohne Meldung. Das ist die Null-Falle aus dem Rahmenteil des Lehrplans in ihrer gemeinsten Form, und die Frage aus Etappe 10 dahinter: **`None` und `0` sind beide falsy und bedeuten Verschiedenes.**

> **Die eine Frage, die du stellst, wenn du `x or ersatz` liest: Kann `x` legitim `0` sein?** Wenn ja, ist die Zeile falsch.

**In deinem eigenen Code schreibst du diese Form nicht.** Für einen Ersatzwert beim Nachschlagen hast du `.get(schluessel, ersatz)` aus Etappe 5 — das ersetzt nur einen *fehlenden* Schlüssel, keine `0`. Und `and` in derselben Rolle zeigt dir die Leseübung am Ende.

### 13. Passiv: eine Fähigkeit ohne Auslöser

Eine aktive Fähigkeit setzt der Spieler ein. **Ein Passiv setzt niemand ein** — es wirkt, weil eine Rechnung danach fragt. Zwei davon baust du heute, und sie zeigen die Machtquellen-Regel von beiden Seiten:

| | Zielhilfe | Standfest |
|---|---|---|
| Woher | gekauft, seit Etappe 6 — **Vaporium** | gelernt, heute — **Erfahrung** |
| Was sie deshalb darf | **eine Zahl vergrößern** | **eine Regel ändern** |
| Wirkung | die Reichweite des Helden ist um eins größer | `erschuettert` wirkt beim Heavy nicht |
| Wer fragt | die Stelle, die die Reichweite des Helden braucht | `bekomme_effekt()`, bevor ein Effekt gesetzt wird |

**Die mittlere Zeile ist der Grund, warum diese beiden nebeneinanderstehen.** Ein gekauftes Passiv, das eine neue Möglichkeit eröffnet, wäre eine gekaufte Fähigkeit. Ein gelerntes Passiv, das *„+1 Reichweite"* gibt, wäre der Skillpunkt als Zahlenbonus — genau das, was der Lehrplan verbietet: **Eine Stufe erhöht nie direkt eine Grundzahl.**

*(Und die Zielhilfe fragt nicht `self.reichweite`, sondern rechnet — der abgeleitete Wert aus 18a, Konzept 4, zum zweiten Mal.)*

---

## Dein Auftrag — Teil 18b

Nach **jedem** Schritt ausführen.

---

### 10. ⭐ Zieh drei Speicher in `welt.flags` um

**Das ist ein reiner Umbau.** Das Spiel darf sich danach um keine Zeile anders verhalten — und das beweist du wie in Etappe 7a und 12a.

**Vor dem Umbau: drei Fragen** — das Ritual seit Etappe 4:

| Frage | Antwort |
|---|---|
| **Was bleibt gleich?** | Jede Meldung, jede Zahl, jeder Kauf, jede Analyse |
| **Was ändert sich nur in der Darstellung?** | Nichts |
| **Was ändert sich wirklich am Datenmodell?** | Aus zwei Sets und einem Boolean wird **ein** Set |

**a) Der Beweis vorher.** Wellenschleife bei `8`, `SEED` auf eine feste Zahl, dann `befehle17.txt` aus Etappe 17b durchlaufen lassen und die Ausgabe in `vorher.txt` schreiben — die Zeilen aus 17b, Konzept 12. *(`vorher.txt` entsteht von selbst und wird überschrieben.)*

**b) Der Umbau.**

- `Welt.__init__` bekommt `flags`, ein leeres **Set**.
- **Fahndung:** Such jede Stelle, an der `freigeschaltet`, `erkenntnisse` oder `meldung_abgesetzt` vorkommt. Zähl sie **vorher**, getrennt nach den drei Namen.
- `.add()` auf eines der beiden alten Sets wird `.add()` auf `welt.flags`. Eine Frage mit `in` wird eine Frage an `welt.flags`.
- Das Setzen von `meldung_abgesetzt` wird `welt.flags.add("meldung_abgesetzt")`, jedes Lesen eine Frage mit `in`. *(Denk an die Nachschub-Zeile in deinem Ereignistopf aus Etappe 17c.)*
- Deine Schadensberechnung bekommt seit Etappe 15 das Erkenntnis-Set übergeben, nicht die Welt. **Das bleibt so** — sie bekommt jetzt eben `welt.flags`.
- Die drei alten Namen werden **gelöscht**, nicht auskommentiert.

⚠️ **Und eine Falle aus 17b, die hier zuschnappen kann:** Zeigt dein `__repr__` der Welt eines der alten Sets, zeigt es jetzt `welt.flags` — **ein Set, dessen Reihenfolge von Start zu Start wechseln kann.** Solange diese Zeile in einer Ausgabe steht, redet `diff`. Zeig dort stattdessen `len(self.flags)`.

**c) Der Beweis nachher.** Dieselben drei Einstellungen, Ausgabe in `nachher.txt`, dann `diff vorher.txt nachher.txt`. **Kein Unterschied.** Wellenschleife und `SEED` danach zurück. *(`vorher.txt` und `nachher.txt` vor dem Commit löschen.)*

**d) Die Invariante.** In deine Invariantenliste aus Etappe 5: *Kein Wort steht in mehr als einer Quelle — nicht als Erkenntnis in `FUNDE` und zugleich als Kennung in `AUSBAUTEN`.* Nur aufschreiben, nicht prüfen. Und prüf es einmal von Hand: Leg deine Erkenntnis-Wörter und deine Ausbau-Kennungen nebeneinander.

**e) `funk_gehoert`.** Nach der Regel aus der Design-Entscheidung passt es in das Set. **Entscheide, ob du es umziehst**, und schreib die Begründung in `GELERNT.md`. Wenn ja: derselbe Handgriff, derselbe Beweis.

**So prüfst du es:** `diff` schweigt, und die drei alten Namen kommen im Code nicht mehr vor.

---

### 11. Hol den Zettel aus Etappe 6 hervor

Eine neue Tabelle **`AUSBAU_VORAUSSETZUNG`**, Ausbau → nötige Freischaltung, genau ein Eintrag: Das Schnellfeuer braucht die Zielhilfe. **Ausbauten ohne Eintrag brauchen nichts.**

- `schalte frei` bekommt **eine** Prüfung mehr — nach *„gibt es das?"* und *„schon freigeschaltet?"*, **vor** dem Vaporium. Nachgeschlagen mit `.get()`, geprüft mit `is not None` und `in welt.flags`: die sechs Zeilen aus Etappe 15, Konzept 4.
- Die Meldung nennt, was fehlt.
- Deine Ausbautenliste aus Etappe 6 zeigt bei einem Ausbau, dessen Voraussetzung fehlt, **was** fehlt. *(Etappe 6, Entscheidung 2: sichtbar bleiben, markiert werden.)*

⚠️ **Das darf eine Freischaltung voraussetzen, eine Fähigkeit nicht.** Beide Seiten kosten Vaporium — das ist *womit*, und dort ist eine Kette aus Käufen in Ordnung.

**So prüfst du es:** `schalte frei schnellfeuer` ohne Zielhilfe — abgewiesen, und **kein** Vaporium weg. Zielhilfe freischalten, dann Schnellfeuer — geht.

---

### 12. Gib der Zielhilfe ihre Wirkung

Nach Konzept 13, linke Spalte:

- `Marine` bekommt eine Methode `aktuelle_reichweite(welt)`: der Grundwert — und beim **gesteuerten** Marine eins mehr, wenn `"zielhilfe"` in `welt.flags` steht. *(Ausbauten wirken seit Etappe 6 für den Helden — das Großmagazin hebt auch nur sein Magazin.)*
- **Fahndung:** Jede Stelle, an der ein Marine seine Reichweite liest, fragt ab heute diese Methode.
- In deiner Ausbautenliste verschwindet *„kalibriert noch"*.

*(Das ist dein dritter abgeleiteter Wert nach `aktueller_schaden()` und dem Magazinstand aus 18a — dasselbe Muster aus Konzept 4: **Speichere nicht, was du jederzeit aus dem Zustand berechnen kannst.** Die Zielhilfe verändert den Grundwert nie.)*

**So prüfst du es:** Einen Gegner genau ein Feld über die Reichweite deines Helden hinaus setzen. Ohne Zielhilfe: kein Treffer. Mit: Treffer. **Und `print(welt.held)` zeigt denselben Grundwert wie vorher.**

---

### 13. ⭐ Zahl Skillpunkte aus

- `Marine.__init__` bekommt `skillpunkte` mit `0` und `faehigkeiten`, ein leeres **Dictionary** — *Fähigkeit → Stufe*.
- An deinem Stufenaufstieg aus Etappe 13, Schritt 9 — dort, wo du die alte Stufe merkst und mit der neuen vergleichst: Ist sie gestiegen, bekommt der Marine **die Differenz** als Skillpunkte, nach Konzept 8. Die Aufstiegsmeldung nennt die neue Zahl.
- Die Statusanzeige zeigt die Skillpunkte.

⚠️ **Der Handgriff, den man übersieht: Sammeln deine Kameraden überhaupt Erfahrung?** Etappe 12 hat ihnen `abschuesse` gegeben; ob sie auch `erfahrung` bekommen, hast du vielleicht nie gebaut. **Wenn nicht, ist jetzt der Moment** — an derselben Stelle, an der `abschuesse` steigt. Sonst steigt kein Kamerad je auf, und alles in 18c, was die Kameraden betrifft, bleibt stumm.

**So prüfst du es:** In der Probedatei die Erfahrung eines Marines knapp unter eine Schwelle setzen und die Stufenberechnung auslösen, einmal knapp darunter, einmal darüber. **Genau ein Punkt beim Überschreiten, keiner beim nächsten Aufruf.** Dann dasselbe mit einem Sprung über zwei Schwellen: zwei Punkte.

---

### 14. ⭐⭐ Leg die Fähigkeitentabelle an

**`FAEHIGKEITEN`**, oben bei den festen Werten. Pro Fähigkeit ein Dictionary mit vier Schlüsseln:

| Fähigkeit | `"geraet"` | `"ab_level"` | `"passiv"` |
|---|---|---|---|
| `"heilung"` | das Gerät deines Medic | 1 | `False` |
| `"aura"` | das Gerät deines Medic | 3 | `False` |
| `"durchschlag"` | das Gerät deines Heavy | 2 | `False` |
| `"standfest"` | das Gerät deines Heavy | 2 | `True` |
| `"granate"` | das Gerät deines Soldaten | 2 | `False` |
| `"mine"` | das Gerät deines Engineer | 1 | `False` |
| `"mobiler_turm"` | das Gerät deines Engineer | 3 | `False` |

**Dazu der vierte Schlüssel `"flags"`** — ein Set der Wörter, die in `welt.flags` stehen müssen. **Bei sechs der sieben Fähigkeiten ist es `set()`.** Genau eine bekommt ein Erkenntnis-Wort aus deiner Fundtabelle: **der mobile Turm**, mit einer Erkenntnis deiner Wahl. **Kopier das Wort aus `FUNDE`, statt es abzutippen** — ein Buchstabe Unterschied ist ein Verweis ins Leere, Etappe 16, Fahndung 9.

**Und beim Standfest ein fünfter:** `"schuetzt_vor"` mit dem Wert `"erschuettert"`. Nur dort. Gelesen wird er mit `.get()` — ungleichmäßige Daten, wie beim `"effekt"` der Gegnertypen in 18a.

⚠️ **`"geraet"` ist das Klassengerät aus Etappe 2 — Zeichen für Zeichen.** Steht in deinem Code `"Schweres MG"`, steht hier `"Schweres MG"`, nicht `"schweres mg"`. **Kopier auch diese vier Strings** aus der Stelle, an der deine Marine-Klassen sie seit Etappe 11b setzen.

*(Das ist der Moment, auf den dieser String gewartet hat: Seit Etappe 2 wurde er angezeigt, heute wird er zum ersten Mal verglichen. Und du siehst dabei, dass er zu dieser Rolle taugt, gerade weil er nie etwas anderes war als Identität — kein Preis, kein Besitz, nur: wer du bist.)*

**Und leg eine feste Zahl dazu:** `MAX_FAEHIGKEITSSTUFE = 3`.

⚠️ **Die Prüfung aus der Design-Entscheidung, bevor du weitermachst:** Steht in irgendeinem `"flags"`-Set ein Wort aus `AUSBAUTEN`? Dann wäre diese Fähigkeit gekauft. **Kein einziges.**

**So prüfst du es:** In der Probedatei `print(FAEHIGKEITEN["standfest"].get("schuetzt_vor"))` und `print(FAEHIGKEITEN["heilung"].get("schuetzt_vor"))`. `erschuettert` und `None`. Dann `print(type(FAEHIGKEITEN["heilung"]["flags"]))` — **`set`, nicht `dict`.**

---

### 15. ⭐⭐ Bau `kann_lernen(name, welt)`

Eine Methode in `Marine`, nach Konzept 11: **Sie gibt einen Grund zurück, oder `None`.** Die Kette, in dieser Reihenfolge:

```
Steht der Name in FAEHIGKEITEN?                  →  nein: „Diese Fähigkeit gibt es nicht."
Passt das Gerät zu deinem Klassengerät?          →  nein: „Das kann nur, wer … trägt."
Schon auf MAX_FAEHIGKEITSSTUFE?                  →  ja:   „Das beherrschst du schon ganz."
Ist level mindestens ab_level?                   →  nein: „Erst ab Stufe …"
Fehlen Wörter aus "flags"?                       →  ja:   „Dir fehlt noch: …"
Ist mindestens ein Skillpunkt da?                →  nein: „Dir fehlt ein Skillpunkt."
── alles erfüllt ──
None
```

**Die Stufe der Fähigkeit** steht in `self.faehigkeiten` — oder gar nicht, wenn sie noch nie gelernt wurde. `.get(name, 0)` liefert dann `0`, und das ist hier gerade richtig: Eine nie gelernte Fähigkeit hat Stufe null. *(Das ist die Stelle, an der man zu `or` greifen will. Konzept 12.)*

**Die fehlenden Wörter** bekommst du mit der Differenzmenge aus Konzept 10. **Ausgeben** tust du sie nach dem Ausweg dort: Lauf über deine Fundtabelle, frag bei jedem Fund, ob sein Erkenntnis-Wort in der Differenz steht, sammle die Kennungen der passenden in einer Liste und verbinde sie mit `.join()` aus Etappe 4. *(Ein Erkenntnis-Wort, das in `FUNDE` gar nicht vorkommt, erscheint so übrigens nie in der Meldung — der Verweis ins Leere aus Etappe 16 zeigt sich als Fähigkeit, die sich nie lernen lässt, ohne dass gesagt wird, warum. Schritt 14 hat dich deshalb kopieren lassen.)*

⚠️ **Warum der Skillpunkt zuletzt kommt:** Er ist die unwichtigste Auskunft. Ein Punkt kommt mit der nächsten Stufe von selbst; eine fehlende Erkenntnis nicht. Stünde er vorne, sähe der Spieler bei jeder gesperrten Fähigkeit nur *„Dir fehlt ein Skillpunkt"* — und nie, was ihn wirklich aufhält.

**Die beiden ersten Meldungen sind die erste Sorte Nein aus Etappe 6** — *gibt es für dich nicht*. Die übrigen sind die zweite — *noch nicht*.

**So prüfst du es — in der Probedatei, mit einem Medic:** fünf Aufrufe, deren Antwort du **vorher** aufschreibst:

1. ein erfundener Name
2. `"granate"`
3. `"aura"` bei `level = 1`
4. `"heilung"` ohne Skillpunkt
5. `"heilung"` mit einem Skillpunkt

**Fünf Aufrufe, vier verschiedene Gründe und einmal `None`.** Dann einen Engineer auf Stufe 3 mit einem Skillpunkt: `"mobiler_turm"` nennt deinen fehlenden Fund. Das Wort in `welt.flags` legen — `None`.

---

### 16. ⭐ Bau `lerne` für den Helden und `lerne_selbst` für die Kameraden

**Der Befehl `lerne <fähigkeit>`:**

- `kann_lernen()` fragen. Kommt ein Grund zurück: melden, fertig.
- Sonst — **erst jetzt wird verändert** — einen Skillpunkt abziehen und die Stufe der Fähigkeit um eins erhöhen: die Zeile aus Etappe 17a, Konzept 4, `.get(name, 0) + 1`. Melden, welche Stufe sie jetzt hat.
- `lerne` allein, ohne zweites Wort: eine Meldung, kein Absturz — der Fall aus Etappe 4.

⚠️ **Das Dictionary garantiert, dass eine Fähigkeit höchstens einmal drinsteht. Es garantiert nicht, dass du für sie nur einmal bezahlst.** Der Satz aus Etappe 6, Konzept 4 — *ein Set garantiert den Zustand, nicht den Vorgang* —, gilt für Dictionaries genauso. Die Prüfung auf die Höchststufe steht deshalb in der Kette.

**Kostet `lerne` eine Runde?** Die Regel aus Etappe 3b: Auskunft nichts, Handlung schon. Entscheide und schreib es auf.

**Der Befehl `faehigkeiten`:** eine Auskunft, keine Runde. Er zeigt jede Fähigkeit aus `FAEHIGKEITEN`, **deren Gerät zu deinem passt** — mit ihrer Stufe, und bei jeder, die du gerade nicht lernen kannst, den Grund aus `kann_lernen()`. *(Sichtbar und markiert statt ausgeblendet — dieselbe Entscheidung wie beim versiegelten Weg in Etappe 5 und beim zweiten Freischalten in Etappe 6. Eine Fähigkeit, die einfach fehlt, verrät nicht, dass es sie gibt.)*

**Die Methode `lerne_selbst(welt)` für die Kameraden** — denn nur der Held wählt selbst:

- Solange noch Skillpunkte da sind: Lauf über `FAEHIGKEITEN` und lerne die **erste**, bei der `kann_lernen()` `None` liefert.
- **Hat ein Durchlauf nichts gelernt, ist Schluss** — auch wenn noch Punkte da sind.

⚠️ **Die zweite Zeile ist die, die man vergisst, und ohne sie läuft das Spiel nie weiter.** Ein Kamerad mit einem Punkt und nichts Lernbarem dreht sich für immer im Kreis. **Das ist das Budget-Ende aus Etappe 17a, Konzept 5, in anderer Kleidung:** Das Ende ist nicht *„keine Punkte mehr"*, sondern *„nichts mehr lernbar"*. Zwei gedeckte Wege dafür: `while True:` mit `break`, oder eine Zustandsvariable, die festhält, ob in diesem Durchlauf etwas gelernt wurde — beide aus Etappe 3.

**Aufgerufen wird `lerne_selbst()` direkt nach dem Auszahlen der Punkte aus Schritt 13 — nur bei Marines, die nicht gesteuert sind.**

*(Weil die Kameraden die erste lernbare Fähigkeit nehmen, ist die **Reihenfolge deiner Tabelle ihr Lernplan**. Ein Medic mit zwei Punkten steckt beide in die Heilung, bevor er die Aura auch nur ansieht. Wenn dir das nicht gefällt, ändere die Reihenfolge der Zeilen — nicht den Code.)*

**So prüfst du es:** In der Probedatei einen Kameraden-Medic auf Stufe 3 mit zwei Punkten, `lerne_selbst()`, dann `faehigkeiten` und `skillpunkte` ausgeben. Sagt vorher, was dasteht. **Dann einen Engineer auf Stufe 3 mit fünf Punkten, ohne das Wort für den mobilen Turm** — die Methode kehrt zurück, und es bleiben Punkte übrig. *(Hängt sie, brich mit `Strg + C` ab und lies im Traceback, in welcher Zeile sie war.)*

---

### 17. Lass Standfest wirken

Nach Konzept 13, rechte Spalte, und mit der Umkehrtabelle aus Etappe 15:

- In `bekomme_effekt()` — **bevor** irgendetwas gesetzt oder gemeldet wird: Hat die Einheit eine gelernte Fähigkeit, deren `"schuetzt_vor"` genau diesen Effekt nennt, passiert nichts.
- **Kein Fähigkeitsname in dieser Prüfung.** Die Methode fragt, *was* eine Fähigkeit tut, nicht, wie sie heißt — Konzept 5 aus 18a.

⚠️ **Nur Marines haben `faehigkeiten`.** Steht die Prüfung in `Einheit`, bekommt ein Basisturm einen `AttributeError`, sobald ihn ein Effekt trifft. Zwei gedeckte Wege: `Marine` überschreibt `bekomme_effekt()` und ruft danach `super()` — oder `Einheit` bekommt ein leeres `faehigkeiten` für alle. **Entscheide dich und schreib auf, warum.**

**So prüfst du es:** In der Probedatei ein Heavy mit gelerntem Standfest — `bekomme_effekt("erschuettert", welt)` ändert nichts, `bekomme_effekt("veraetzt", welt)` schon. Ein Heavy ohne Standfest bekommt beides.

---

### 18. Prüf, dass das Alte noch läuft, und commit

- Alles aus Schritt 9 noch einmal. Dazu: `schalte frei`, `analysiere`, der Wellenbericht mit seinem Ereignistopf — alle drei lesen seit heute aus `welt.flags`.
- Keine `probe.py`, keine `vorher.txt` oder `nachher.txt`, kein fester `SEED`, Wellenschleife bei `1`.
- Die Abschnitte am Ende, die zu 18b gehören: **die Leseübung** und **Kaputtmachen 6 und 7**.

Commit: `Etappe 18b: Skillpunkte und Voraussetzungen`

---

## Selbsttest — 18b

- [ ] `freigeschaltet`, `erkenntnisse` und `meldung_abgesetzt` kommen im Code nicht mehr vor, und der `diff` aus Schritt 10 war leer.
- [ ] Kein Wort steht zugleich als Erkenntnis in `FUNDE` und als Kennung in `AUSBAUTEN`.
- [ ] Das Schnellfeuer lässt sich ohne Zielhilfe nicht freischalten, und der Versuch kostet nichts.
- [ ] Mit Zielhilfe trifft der Held ein Feld weiter — sein Grundwert hat sich nicht verändert.
- [ ] Ein Aufstieg zahlt die Differenz der Stufen als Skillpunkte aus, und die Kameraden steigen ebenfalls auf.
- [ ] In keinem `"flags"`-Set der Fähigkeitentabelle steht eine Kennung aus `AUSBAUTEN`.
- [ ] `kann_lernen()` liefert für fünf Lagen vier verschiedene Gründe und einmal `None`.
- [ ] Die fehlenden Wörter erscheinen in der Meldung in der Reihenfolge deiner Fundtabelle — nicht in der eines Sets.
- [ ] `lerne` zieht erst ab, wenn alle Prüfungen bestanden sind. Eine Fähigkeit auf Höchststufe lässt sich nicht noch einmal bezahlen.
- [ ] `lerne_selbst()` kehrt zurück, auch wenn Punkte übrig sind und nichts lernbar ist.
- [ ] Ein Heavy mit Standfest wird nicht erschüttert — und kein Basisturm stürzt ab, wenn ihn ein Effekt trifft.

> **⏸ Ende von 18b.** Deine Marines können lernen — nur tun können sie noch nichts. 18c gibt ihren Fähigkeiten Wirkung.

---

# Teil 18c — Die Fähigkeiten wirken

## Worum es geht

Seit Etappe 11 hat jede Marine-Klasse eine Methode, die eine Meldung ausgibt. Seit Etappe 13 hat sie eine Abklingzeit. **Wirkung hatte sie nie.** Du konntest *„Granatwerfer!"* rufen, und nichts ist explodiert.

> **Heute explodiert etwas.** Der Medic heilt, der Heavy schießt durch eine ganze Reihe, der Soldat trifft ein Feld und seine Nachbarn, der Engineer legt Minen und stellt einen Turm auf.

**Eine aktive Fähigkeit besteht aus drei Teilen, und alle drei hast du schon:** einer Voraussetzung (18b), einer Abklingzeit (Etappe 13) und einer Wirkung (heute). Neu ist, dass sie zusammenkommen — und die Frage, **wer** sie zusammenbringt.

Und am Ende der Portion setzt dein Trupp seine Fähigkeiten selbst ein. **Danach ist die Trupp-KI fertig.** Weiter geht sie in diesem Plan nicht.

---

## Der lange Bogen — was heute fällig wird

- **`faehigkeit_einsetzen()` aus Etappe 11 und 13** — der Platzhalter mit Meldung und einer Abklingzeit — stirbt heute.
- **Die offene Frage aus Etappe 13:** Die Abklingzeit wird in der Oberklasse geprüft — *woher weiß die Unterklasse, dass abgebrochen wurde?* Heute wird die Frage umgedreht, und dann stellt sie sich nicht mehr.
- **Die Abklingzeit aus Etappe 13**, und ihr Versprechen: *„Ein eigenes Objekt lohnt sich, sobald eine Abklingzeit mehr kann als herunterzählen — das ist Etappe 18."* Sieh heute nach, ob es so weit ist.
- **Die zwei Türme aus Etappe 13.** Der Basisturm steht seit damals. Heute entsteht der zweite, und die Tabelle aus Etappe 13 wird praktisch.
- **Das Raster aus Etappe 14:** *„Minen wollen Felder — Etappe 18."* Und `felder_in_reichweite()` bekommt einen zweiten Aufrufer.
- **Das Schnellfeuer aus Etappe 6.** Der Durchschlag des Heavy klingt ähnlich und ist etwas anderes. Der Bogen verlangt, den Unterschied ausdrücklich zu benennen.
- **Der `vorrat` aus Etappe 5** bekommt einen zweiten Munitionsschlüssel.
- **Die Trupp-KI aus Etappe 12 und 14b** — Stufe 3, die letzte.
- **Das Merkattribut aus Etappe 17c:** Jede Einheit merkt sich ihren Abschussstand zu Wellenbeginn *an sich selbst*, damit eine Einheit, die mitten in der Welle entsteht, keinen `KeyError` wirft. Heute entsteht eine.
- **„Eine Strafe darf keine Belohnung sein" aus Etappe 13** — mit ihrer Kehrseite: Ein Fehlversuch darf nichts kosten.

---

## Zwei Design-Entscheidungen

### Wer bringt Voraussetzung, Abklingzeit und Wirkung zusammen? ⭐⭐

**In Etappe 13 lief es so:** Die Unterklasse ruft `super()`, die Oberklasse prüft die Abklingzeit — und steigt vielleicht aus. **Dann muss die Unterklasse irgendwie erfahren, dass sie nichts tun soll.** Etappe 13 hat dir zwei Wege gezeigt: ein Rückgabewert oder eine überschriebene Meldung.

**Heute drehst du es um:**

| | Etappe 13 | Heute |
|---|---|---|
| Wer wird zuerst aufgerufen | die Unterklasse | **die Oberklasse**, `setze_ein()` |
| Wer prüft | die Oberklasse, auf Nachfrage | die Oberklasse, von sich aus |
| Wer wirkt | die Unterklasse — wenn sie vom Abbruch erfahren hat | die Unterklasse, **nur wenn sie gerufen wird** |
| Wer bezahlt und startet die Abklingzeit | ungeklärt | die Oberklasse, **nach** der Wirkung |

> **Die Oberklasse regelt den Ablauf. Die Unterklasse liefert nur, was bei ihr anders ist: die Wirkung.**

Dann muss die Unterklasse nichts über Abbrüche wissen — sie wird gar nicht erst gerufen, wenn etwas fehlt. Und alles, was für jede Klasse gleich ist, steht **einmal** da.

### Gehört die Mine in den Trupp?

Seit Etappe 13 steht dein Basisturm in `welt.trupp`, obwohl er kein Marine ist — *„was auf meiner Seite steht und tickt"*. **Heute kommen zwei neue Dinge auf deine Seite.** Gehören sie auch dorthin?

| Im Trupp zu stehen heißt … | Mobiler Turm | Mine |
|---|---|---|
| … im Tick `update()` aufgerufen zu werden | ja, er feuert | sie handelt nicht, sie wartet |
| … Trefferpunkte zu haben und am Tor getroffen zu werden | ja | eine Mine hat keine |
| … im Wellenbericht zu sprechen | ja, mit der Stimme aus `Einheit` | *„Mine: 0 Abschüsse."* — in jeder Welle |
| … geheilt werden zu können | ja | Unsinn |

**Der Plan legt den mobilen Turm in den Trupp und die Mine nicht.** Die Mine bekommt eine eigene Liste an der Welt und eine eigene kleine Phase im Tick.

> **Wer handelt, tickt. Wer wartet, wird geprüft.**

*(Dieselbe Frage hast du in Etappe 15 schon einmal beantwortet: Ein Fundstück erbt nicht von `Einheit`, weil es nicht tickt. **Wovon etwas erbt, entscheidet, wer es benutzt.**)*

---

## Die Konzepte — Teil 18c

Heute an einem Getränkeautomaten und in einem Bürogebäude.

### 14. ⭐⭐ Die Oberklasse ruft, die Unterklasse liefert

```python
class Automat:
    def __init__(self):
        self.guthaben = 0

    def ausgeben(self, sorte, preis):
        if self.guthaben < preis:
            print("Bitte Geld einwerfen.")
            return False
        if not self.zubereiten(sorte):
            print(f"{sorte} gibt es hier nicht.")
            return False
        self.guthaben -= preis
        return True

    def zubereiten(self, sorte):
        """Ein Automat ohne Sorten kann nichts zubereiten."""
        return False


class Kaffeeautomat(Automat):
    def zubereiten(self, sorte):
        if sorte == "espresso":
            print("Espresso läuft.")
            return True
        elif sorte == "cappuccino":
            print("Milch wird aufgeschäumt.")
            return True
        return super().zubereiten(sorte)
```

**Sag voraus:** `Kaffeeautomat().ausgeben("espresso", 2)`, mit genug Guthaben. **Welche `zubereiten` läuft?**

**Die aus `Kaffeeautomat`** — obwohl der Aufruf in `Automat` steht. `self` ist in diesem Moment ein Kaffeeautomat, und `self.zubereiten(...)` sucht die Methode **bei dem Objekt**, nicht in der Klasse, in der der Aufruf zufällig steht. Das ist die Regel aus Etappe 11, Konzept 8 — *eine Schleife, ein Aufruf, jedes Objekt tut das Richtige* —, nur diesmal **von innen**: Auch die Oberklasse selbst ruft auf, und das Objekt weiß Bescheid.

**Drei Dinge, die du daraus mitnimmst:**

- **Die Fassung in `Automat` ist die Rückfallebene.** Sie gibt `False` zurück — *„kann ich nicht"*. Eine Unterklasse, die eine Sorte nicht kennt, reicht die Frage mit `super()` nach oben weiter und bekommt dasselbe `False`.
- **Bezahlt wird erst, wenn `zubereiten` `True` geliefert hat.** Kein Espresso, kein Geld. Das ist die Transaktion aus Etappe 5 — *erst alle Prüfungen, dann verändern* —, mit einer Besonderheit: Die letzte Prüfung *ist* hier das Zubereiten. Deshalb muss `zubereiten` selbst zuerst prüfen und erst dann etwas tun — und bei `False` darf es nichts verändert haben.
- **Jeder Zweig von `zubereiten` endet mit einem `return`.**

⚠️ **Der letzte Punkt ist der gefährliche.** Vergiss in einem Zweig das `return True`. Die Methode läuft bis zum Ende und liefert — wie jede Funktion ohne `return` — `None`. Und `None` ist falsy. **`not None` ist `True`.** Der Automat meldet *„gibt es hier nicht"* — **nachdem** der Espresso schon gelaufen ist, und kassiert nichts.

> **Ein fehlendes `return` sieht aus wie `False`.** Das stürzt nicht ab. Es verschenkt Espresso.

### 15. Mehrere Abklingzeiten — dasselbe Dictionary wie bei den Effekten

In Etappe 13 hatte jeder Marine **eine** Fähigkeit und **ein** Attribut `abklingzeit`. Ab heute hat ein Medic zwei Fähigkeiten, und jede läuft für sich ab.

**Das ist exakt die Form aus 18a:** ein Dictionary *Name → Restdauer*, ein Eintrag steht genau so lange drin, wie die Abklingzeit läuft, heruntergezählt in der Zählerphase, gesammelt und danach gelöscht. **Beim zweiten Mal schreibst du es schneller** — und du wirst merken, dass du denselben Block zweimal geschrieben hast.

> **Wiederholung im Muster ist ein Hinweis, kein Zufall** — der Satz aus Etappe 13. Ob daraus eine gemeinsame Struktur wird, entscheidet Etappe 22. Notier heute nur, dass es passiert ist.

**Und das Versprechen aus Etappe 13?** Dort stand, ein eigenes `Abklingzeit`-Objekt lohne sich, sobald eine Abklingzeit mehr kann als herunterzählen. **Sieh ehrlich hin: Deine Abklingzeiten zählen weiterhin nur herunter. Es sind nur mehrere.** Mehrere heißt Dictionary, nicht Objekt. Die Antwort von damals gilt noch.

### 16. Drei Formen von „wen trifft es?" ⭐

Die Wirkungen heute sehen verschieden aus und bestehen doch nur aus Werkzeugen, die du hast. **Das Neue ist die Frage, wen sie treffen:**

| Form | Fähigkeit | Womit du es baust |
|---|---|---|
| **Das beste Ziel** | Heilung | die Suche mit gemerktem Besten aus Etappe 12 und 14b — nur mit *größter Lücke* statt *kleinstem Abstand*. **Und wie dort braucht sie eine Regel für Gleichstand** — die Tie-Break-Frage aus Etappe 14a und 16 |
| **Alle, die eine Bedingung erfüllen** | Durchschlag, Aura | eine Schleife über alle, ein `if` mit verknüpfter Bedingung |
| **Alle auf bestimmten Feldern** | Granate | ein Set von Feldern aus Etappe 14b, gefragt mit `in` |

**Die zweite Zeile hat eine Falle, und sie sitzt in den Klammern.** Ein Bürogebäude: Eine Durchsage soll alle Räume erreichen, die auf demselben Stockwerk **oder** am selben Treppenhaus liegen — **und** höchstens drei Türen entfernt sind.

```python
if (raum.stockwerk == 2 or raum.treppenhaus == "B") and raum.tueren <= 3:
```

**Nimm die Klammern weg** und lies, was Python daraus macht: `and` bindet stärker als `or`, genau wie Punkt vor Strich. Ohne Klammern steht dort *„Stockwerk 2 — oder Treppenhaus B und nah"*. **Jeder Raum im zweiten Stock hört die Durchsage, egal wie weit weg.** Kein Absturz. Etappe 2, Konzept 8, hat dir die Klammern gegeben — heute brauchst du sie.

⚠️ **Und der Unterschied, den der Bogen seit Etappe 6 verlangt:**

| | Schnellfeuer — Etappe 6 | Durchschlag — heute |
|---|---|---|
| Was es ist | ein gekaufter Ausbau, passiv | eine gelernte Fähigkeit, aktiv |
| Wer es hat | der Held, egal welche Klasse | nur, wer das schwere MG trägt |
| Was passiert | zwei Schuss, zwei Ziele — die nächsten | **ein** Schuss, der alle in einer Zeile oder Spalte trifft |
| Was es kostet | nichts, nachdem es gekauft ist | schwere Munition und eine Abklingzeit |

**Das eine macht mehr vom Gleichen, das andere etwas anderes.** Das ist die Machtquellen-Regel noch einmal: Vaporium vergrößert, Erfahrung eröffnet.

### 17. Wartet oder handelt

Drei Dinge stehen ab heute auf deiner Seite des Vorfelds. Die Tabelle aus Etappe 13 bekommt eine dritte Spalte:

| | Basisturm — Etappe 13 | Mobiler Turm — heute | Mine — heute |
|---|---|---|---|
| Was er ist | ein Gebäude | eine Fähigkeit des Engineer | eine Fähigkeit des Engineer |
| Wie er entsteht | in der Werkstatt, für Vaporium, mit Bauzeit | eingesetzt, mit Aufstellzeit | eingesetzt, sofort |
| Wie lange | bis er fällt | eine feste Lebensdauer | bis jemand darauftritt |
| Wie viele | genau einer | höchstens einer | höchstens eine pro Feld |
| Im Trupp | ja | **ja** | **nein** |
| Tut was | feuert | feuert | **wartet** |

**Zwei Zähler am mobilen Turm, nacheinander:** erst die Aufstellzeit — solange tut er nichts, wie der Basisturm im Bau —, dann die Lebensdauer. Läuft sie ab, **ist das ein Ausfall**: Status `"tot"`, und die Aufräumphase entfernt ihn — **über dasselbe Attribut**, über das sie seit Etappe 13 einen gefallenen Basisturm entfernt, statt ihn wie einen Marine stehen zu lassen.

**Die Mine ist ein Ding ohne Tick.** Eine kleine Klasse mit Feld, Schaden und wem sie gehört — sie erbt von nichts. Geprüft wird sie in einer eigenen Phase **nach** den Gegnern: Steht ein Gegner auf ihrem Feld, geht sie hoch. *(Warum nach den Gegnern? Weil sie in dieser Phase ihren Schritt machen. Vorher stünde niemand auf dem Feld, der gerade darauf getreten ist.)*

### 18. Dürfen und wollen

Bei deinem Helden entscheidest du, wann eine Fähigkeit eingesetzt wird. Bei den Kameraden entscheidet der Code. **Das sind zwei verschiedene Fragen**, und sie gehören in zwei verschiedene Methoden:

| | Dürfen | Wollen |
|---|---|---|
| Die Frage | *Ist der Einsatz erlaubt?* | *Ist er jetzt klug?* |
| Beispiel | gelernt, keine Abklingzeit, genug Munition | *jemand ist unter der Hälfte seiner Trefferpunkte* |
| Gilt für | Held **und** Kameraden — dieselben Regeln | nur die Kameraden — der Held entscheidet selbst |
| Wo es steht | einmal, in `Marine` | in jeder Unterklasse, für ihre eigenen Fähigkeiten |

**Das ist der Grund, warum die Prüfung in 18b eine Funktion geworden ist und nicht ein paar `if` in deinem Befehl.** Der Befehl zeigt dem Spieler den Grund. Der Kamerad fragt nur, ob es einen gibt. **Stünde die Prüfung in deiner Befehlsverarbeitung, müsstest du sie für die Kameraden ein zweites Mal schreiben** — und die beiden Fassungen würden irgendwann auseinanderlaufen.

*(Und erinnerst du dich an deine Feuerbedingung aus 18a, Schritt 7 — `and not` und die Reichweite? **Das war die erste Dürfen-Prüfung dieses Spiels**, seit Etappe 2. Sie konnte nur nicht sagen, was fehlt.)*

---

## Dein Auftrag — Teil 18c

Nach **jedem** Schritt ausführen. **Dein Held ist nur eine der vier Klassen** — die Fähigkeiten der anderen drei prüfst du in der Probedatei, und im Spiel siehst du sie ab Schritt 29 bei den Kameraden.

---

### 19. Leg die Zahlen an und die schwere Munition ins Depot

**Zwei flache Tabellen** bei den festen Werten, beide mit den Namen der aktiven Fähigkeiten als Schlüssel:

| Fähigkeit | `ABKLINGZEITEN` | `SCHWERE_KOSTEN` |
|---|---|---|
| `"heilung"` | 5 | 0 |
| `"aura"` | 8 | 0 |
| `"durchschlag"` | 6 | 2 |
| `"granate"` | 6 | 2 |
| `"mine"` | 4 | 1 |
| `"mobiler_turm"` | 12 | 3 |

*(Standfest steht in keiner — ein Passiv hat weder Abklingzeit noch Kosten.)*

⚠️ **Das sind jetzt drei Tabellen mit fast demselben Schlüsselsatz** — `FAEHIGKEITEN`, `ABKLINGZEITEN`, `SCHWERE_KOSTEN`. **Bemerken, nicht zusammenführen.** Dasselbe Muster wie die vier Depot-Tabellen aus Etappe 5 und die drei aus Etappe 15, und derselbe Zahltag: Etappe 22. Schreib es zu den anderen in `GELERNT.md` — **und in deine Invariantenliste:** *Jede aktive Fähigkeit steht in `ABKLINGZEITEN` und `SCHWERE_KOSTEN`; kein Passiv steht dort.* Nur aufschreiben, nicht prüfen. Fehlt ein Eintrag, gibt es beim ersten Einsatz einen `KeyError` — ein Verweis ins Leere wie in Etappe 16, Fahndung 9.

**Die schwere Munition** ist ein zweiter Schlüssel im `vorrat` deines Helden — `"schwere_munition"`, Startwert `3`. Deine bisherige `"munition"` bleibt, wie sie heißt. *(Sie in „leichte Munition" umzubenennen kostet eine Fahndung und lehrt nichts.)* **Ins Depot** kommt sie mit den Einträgen, die jede Ware seit Etappe 5 braucht: ein Preis in `WAREN` — nimm `30` —, ein Eintrag in `STAPELBAR` und ein Anzeigename.

**Und der Architekturtest aus Etappe 5, zum vierten Mal:** Musstest du an deiner Kauflogik etwas ändern? Die Antwort gehört in `GELERNT.md`.

**So prüfst du es:** `kaufe schwere_munition 2` im Depot — der Vorrat steigt um zwei, das Vaporium sinkt um 60.

---

### 20. ⭐ Bau `treffe()` — ein reiner Umbau vor dem Umbau

Ab heute erledigen Fähigkeiten Gegner, nicht nur Schüsse. **Und wer einen Gegner erledigt, bekommt seit Etappe 12 einen Abschuss gutgeschrieben** — ein Marine dazu seit 3c Erfahrung und damit vielleicht einen Aufstieg. Heute stehen diese Gutschriften an den Stellen, an denen gefeuert wird. **Morgen stünden sie zusätzlich an sechs aktiven Fähigkeiten und einer Mine.**

- **Fahndung:** Such jede Stelle, an der ein Abschuss oder Erfahrung gutgeschrieben wird. Zähl sie.
- `Einheit` bekommt eine Methode `treffe(ziel, menge, welt)`: Ist das Ziel schon `"tot"`, passiert nichts. Sonst nimmt es den Schaden, und **fällt es dabei**, wird der Abschuss gutgeschrieben.
- Was nur ein Marine bekommt — Erfahrung, Stufenaufstieg, Skillpunkte —, gehört in eine Fassung von `treffe()` in `Marine`, die zuerst `super().treffe(ziel, menge, welt)` aufruft. *(Woher weiß die Marine-Fassung danach, ob das Ziel gefallen ist? Sieh dir den Status des Ziels an.)*
- Jede Stelle aus der Fahndung ruft ab heute `treffe()`.

> **Wenn mehrere Wege dieselbe Spielregel auslösen, gehört die Regel an einen Ort.** Schuss, Fähigkeit, Mine und Turm sind vier Wege — *„wer erledigt, bekommt den Abschuss"* ist eine Regel.

⚠️ **Die erste Zeile ist nicht Vorsicht, sondern Regel:** Ein Ziel, das schon liegt, wird nicht noch einmal getroffen. Sonst bekommen der Held, der einen Gegner erledigt, und die Mine, auf die der Gegner im selben Tick noch fällt, zwei Abschüsse für einen Gegner.

**Der Beweis:** wie in Schritt 10 — Wellenschleife bei `8`, fester `SEED`, `befehle17.txt`, `vorher.txt` vor dem Umbau, `nachher.txt` danach, `diff`. **Kein Unterschied.** *(Redet `diff` doch, hast du vermutlich keinen Fehler gebaut, sondern einen gefunden: eine Doppelgutschrift, die es vorher schon gab. Such die Stelle, schreib einen Dreizeiler aus Etappe 16.)*

---

### 21. ⭐ Mach aus der Abklingzeit ein Dictionary

Nach Konzept 15.

- `Marine.__init__`: Das Attribut `abklingzeit` aus Etappe 13 wird durch `abklingzeiten` ersetzt, ein leeres Dictionary.
- In `Marine.zaehler_runter()` — **nach** dem `super()`-Aufruf aus 18a — zählt der Block aus 18a, Schritt 4, jetzt auch dieses Dictionary herunter: sammeln, danach löschen, *„… wieder bereit"* melden.
- Die Statusanzeige aus Etappe 13, Schritt 8, zeigt alle laufenden Abklingzeiten.

⚠️ **Die alte Abklingzeit hängt an Stellen, die du heute ohnehin abreißt** — der Prüfung in deiner `faehigkeit_einsetzen()` und der festen Zahl `ABKLINGZEIT`. Beide verschwinden in Schritt 22. Bis dahin darf das Spiel an diesen Stellen stolpern; ein `AttributeError` zeigt dir, wo.

---

### 22. ⭐⭐ Bau `kann_einsetzen()`, `setze_ein()` und `wirke()`

**Das ist der Auftragsschritt dieser Portion.** Er baut den Ablauf, den alle sechs aktiven Fähigkeiten teilen — Standfest aus 18b ist ein Passiv und wird nie eingesetzt.

**`kann_einsetzen(name, welt)`** in `Marine`, nach Konzept 11 aus 18b — Grund oder `None`:

```
Steht der Name in self.faehigkeiten?             →  nein: „Das hast du nicht gelernt."
Ist die Fähigkeit passiv?                         →  ja:   „Das wirkt von selbst."
Läuft ihre Abklingzeit?                           →  ja:   „Noch … Takte."
Nur beim gesteuerten Marine:
  reicht die schwere Munition für SCHWERE_KOSTEN? →  nein: „Dafür fehlen dir … Schuss schwere Munition."
── alles erfüllt ──
None
```

⚠️ **Warum nur der Held zahlt:** Die Kameraden laden ihr Magazin seit Etappe 13 kostenlos über Zeit nach, während der Held aus dem Vorrat bezahlt. Für Fähigkeiten gilt dieselbe Regel — ihre Grenze ist die Abklingzeit. **Und dein Vorrat gehört dem Helden** (Etappe 11b): Ein Kamerad, der ihn leerschösse, würde über deine Munition entscheiden.

**`setze_ein(name, welt)`** in `Marine`, nach Konzept 14:

- `kann_einsetzen()` fragen. Ein Grund: melden, `False` zurück.
- `self.wirke(name, welt)` aufrufen. Liefert es nicht `True`: `False` zurück — **ohne zu zahlen und ohne Abklingzeit.**
- Erst dann: beim gesteuerten Marine die schwere Munition abziehen, und bei jedem die Abklingzeit aus `ABKLINGZEITEN` eintragen. `True` zurück.

**`wirke(name, welt)`** in `Marine`: ein Docstring, der sagt, warum diese Fassung nichts tut, und `return False`.

⚠️ **Die zweite Zeile von `setze_ein` ist die Regel aus Etappe 13, von der anderen Seite:** Eine Strafe darf keine Belohnung sein — und **ein Fehlversuch darf nichts kosten.** Heilung, wenn niemand verletzt ist; eine Granate, wenn kein Gegner in Reichweite steht: Die Fähigkeit wirkt nicht, also wird nichts bezahlt und keine Abklingzeit gestartet.

**Der Befehl `faehigkeit <name>`** ersetzt deinen alten Befehl `faehigkeit`: Er ruft `setze_ein()` beim Helden. Er kostet eine Runde, auch wenn die Fähigkeit nicht wirkt? Die Frage aus Etappe 12 zu ungültigen Eingaben — entscheide nach dem, was du dort entschieden hast.

**Und dann reißt du den Platzhalter ab:**

- `faehigkeit_einsetzen()` wird in `Marine` und in allen vier Unterklassen **gelöscht**, nicht auskommentiert. Die festen Zahl `ABKLINGZEIT` ebenso.
- **Fahndung vorher:** Zähl alle Stellen, an denen `faehigkeit_einsetzen` oder `ABKLINGZEIT` vorkommt.

**So prüfst du es:** In der Probedatei einen Medic mit gelernter Heilung. `setze_ein("heilung", welt)` — **`False`, kein Vorrat weg, keine Abklingzeit**: `wirke` gibt es noch nicht, also wirkt nichts. Genau das soll heute noch so sein. Dann `setze_ein("aura", welt)` ohne gelernte Aura — der Grund. Und im Spiel: `faehigkeit` allein, ohne Namen — eine Meldung, kein Absturz.

---

### 23. Heilung — das beste Ziel

`Medic` überschreibt `wirke(name, welt)`. **Eine `elif`-Kette über die Namen seiner eigenen Fähigkeiten**, und am Ende `return super().wirke(name, welt)` — die Rückfallebene aus Konzept 14.

*(Eine `elif`-Kette über Fähigkeitsnamen, wo du doch gerade alles in Tabellen ziehst? Ja. Sie hat zwei Zweige, sie steht in der Klasse, der die Fähigkeiten gehören, und sie fragt nicht **welche Klasse**, sondern **welche Fähigkeit**. In Etappe 23a stirbt sie durch ein Dictionary aus Funktionen — heute ist sie genau richtig.)*

**Der Zweig `"heilung"`** — Stufe `s` ist der Wert in `self.faehigkeiten`:

- Das Ziel ist die aktive Einheit des Trupps **mit der größten Lücke** zwischen Startwert und aktuellen Trefferpunkten, im Abstand höchstens `aktuelle_reichweite(welt)`. Der Medic selbst zählt mit. Den Startwert hat jede Einheit seit Etappe 13, Schritt 12.
- **Haben zwei dieselbe Lücke, gewinnt der, der in `welt.trupp` zuerst steht** — mit `>` statt `>=` beim Vergleich mit dem bisher Besten. Schreib die Regel in `GELERNT.md`, neben deine Gleichstandsregel aus Etappe 14a. *(Ohne feste Regel entscheidet sie trotzdem jemand: die Reihenfolge deiner `if`-Zeilen.)*
- Hat niemand eine Lücke: `False` — **ohne etwas zu verändern.**
- Sonst: `10 · s` Trefferpunkte dazu, **aber nie über den Startwert.** Melden, `True`.

⚠️ **Hier ist die Obergrenze richtig**, anders als beim Balken aus Etappe 3c. Dort solltest du einen Fehler sichtbar machen. Hier ist *„nie über den Startwert"* eine Spielregel.

⚠️ **Wer liegt, wird nicht geheilt.** Eine Einheit auf `"tot"` ist ausgefallen und steht nach ihrem Zähler von selbst wieder auf. Eine Heilung, die Gefallene zurückholt, wäre eine andere Fähigkeit.

**So prüfst du es:** In der Probedatei zwei Kameraden verletzen, einen schwerer. Die Heilung trifft den schwereren. Dann beide gleich schwer: Sie trifft den, der im Trupp vorne steht. Einen nur um 3 verletzten heilen — er steht danach auf seinem Startwert, nicht darüber. Niemand verletzt — `False`, keine Abklingzeit.

---

### 24. Durchschlag — alle in einer Zeile oder Spalte

`Heavy` überschreibt `wirke()`, wie in Schritt 23.

**Der Zweig `"durchschlag"`:** Jeder **aktive** Gegner, der in **derselben Zeile oder derselben Spalte** steht wie der Heavy **und** im Abstand höchstens `aktuelle_reichweite(welt) + s`, bekommt über `treffe()` den `aktueller_schaden()` des Heavy. `True`, wenn mindestens einer getroffen wurde, sonst `False`.

⚠️ **Die Klammern aus Konzept 16.** Die Bedingung hat ein `or` und ein `and`. Ohne Klammern um den `or`-Teil trifft der Durchschlag die ganze Zeile, egal wie weit weg. *(Kaputtmachen 10.)*

*(Die Stufe vergrößert hier die Reichweite der Fähigkeit, nicht den Grundschaden des Heavy. Das ist erlaubt: Eine Fähigkeit auf Stufe 3 ist dieselbe Fähigkeit mit anderen Zahlen. Verboten ist nur, dass eine Stufe den Marine selbst stärker macht.)*

**So prüfst du es:** In der Probedatei drei Gegner setzen — einer in der Zeile des Heavy, einer in seiner Spalte, einer diagonal. Zwei werden getroffen. Dann einen in der Zeile, aber weit außer Reichweite: nicht getroffen.

---

### 25. Granate — ein Feld und seine Nachbarn

`Soldat` überschreibt `wirke()`.

**Der Zweig `"granate"`:**

- Das Zielfeld ist das Feld des nächsten Gegners — `welt.naechster_gegner()` aus Etappe 14b, vom Soldaten aus. Kein Gegner, oder weiter weg als `aktuelle_reichweite(welt)`: `False`.
- Der Bereich ist `welt.felder_in_reichweite()` um das Zielfeld mit Radius `1` — fünf Felder, wie du in Etappe 14b nachgezählt hast.
- Jeder aktive Gegner, dessen `(x, y)` in diesem Set liegt, bekommt über `treffe()` `6 · s`. `True`.

⚠️ **Der eigene Trupp bekommt nichts ab**, auch wenn er im Bereich steht — du läufst nur über `welt.gegner`. Wenn du das anders willst, ist das eine Spielregel; schreib sie auf.

**So prüfst du es:** In der Probedatei drei Gegner — zwei nebeneinander, einer drei Felder daneben. Die Granate auf den ersten trifft die zwei.

> **⏸ Guter Schnitt.** Drei Fähigkeiten wirken, und alle drei waren ein Ereignis: einmal passiert, fertig. Ab Schritt 26 bleibt etwas zurück — eine Mine, ein Turm, eine Aura. Das ist die schwerere Sorte, und ein eigener Abend. *(Commit an dieser Stelle ist erlaubt: `Etappe 18c: Heilung, Durchschlag, Granate`.)*

---

### 26. ⭐ Mine — ein Ding, das wartet

Nach Konzept 17.

**Die Klasse `Mine`** — sie erbt von nichts: `x`, `y`, `schaden` und `besitzer`, der Engineer, der sie gelegt hat. Ein `__repr__` lohnt sich.

**`welt.minen`**, eine leere Liste in `Welt.__init__`.

**`Engineer` überschreibt `wirke()`, Zweig `"mine"`:** Liegt auf dem eigenen Feld schon eine Mine: `False`. Sonst eine neue mit `12 · s` Schaden auf das eigene Feld, `True`.

**Eine neue Tick-Phase „Minen"**, direkt nach den Gegnern und vor dem Aufräumen:

- Für jede Mine: Jeder aktive Gegner auf ihrem Feld bekommt ihren Schaden — über `mine.besitzer.treffe(...)`, damit der Engineer den Abschuss bekommt.
- Ist sie hochgegangen, kommt sie in eine Liste. **Nach der Schleife** werden alle hochgegangenen aus `welt.minen` entfernt — sammeln, dann entfernen, Etappe 12, Konzept 11.

⚠️ **Trag die neue Phase in deine Tick-Reihenfolge in `GELERNT.md` ein** — neben die aus Etappe 16. Und schreib einen Satz dazu, warum sie nach den Gegnern steht und vor dem Aufräumen.

**Zeichnen:** `zeichne_vorfeld()` bekommt die Minen übergeben — **die Liste, nicht die Welt**, die Reinheitsregel aus Etappe 7b — und malt sie mit einem eigenen Zeichen, **vor** den Einheiten, wie die Fundstücke aus Etappe 15.

**So prüfst du es:** In der Probedatei einen Engineer mit gelernter Mine, `setze_ein("mine", welt)`, einen Gegner direkt daneben setzen, so dass sein nächster Schritt auf die Mine führt, einen Tick auslösen. Der Gegner nimmt Schaden, `welt.minen` ist leer, der Engineer hat einen Abschuss mehr, falls der Gegner gefallen ist. **Zweite Mine auf dasselbe Feld — `False`, keine Abklingzeit.**

---

### 27. ⭐ Der mobile Turm — ein Ding, das handelt

**Die Klasse `MobilerTurm`, erbt von `Einheit`.** Eigene Werte für Trefferpunkte, Schaden und Reichweite, dazu zwei Zähler: `aufstellzeit` mit `2` und `lebensdauer` mit `4 + 2 · s` — die Stufe bekommt er beim Erzeugen übergeben.

- **`zaehler_runter()`:** zuerst `super()` — für die Effekte aus 18a. Steht er auf `"tot"`, danach nichts mehr. Sonst: Läuft die Aufstellzeit, zählt sie herunter und meldet bei null, dass er steht. **Erst danach** läuft die Lebensdauer; bei null wird er `"tot"` und meldet, dass er abgebaut ist.
- **`update()`:** Tot oder im Aufbau — sofort zurück. Sonst feuern wie dein Basisturm: nächster Gegner in Reichweite, `treffe()` mit `aktueller_schaden()`.

**`welt.mobiler_turm`** mit `None` in `Welt.__init__` — *höchstens einer*, dieselbe Form wie `welt.turm` aus Etappe 13.

**`Engineer`, Zweig `"mobiler_turm"`:** Steht schon einer: `False`. Sonst einen auf dem eigenen Feld erzeugen, an `welt.trupp` hängen, in `welt.mobiler_turm` legen, `True`.

**Aufräumphase:** Fällt der mobile Turm — ob durch Gegner oder weil seine Lebensdauer abgelaufen ist —, wird er aus dem Trupp entfernt und `welt.mobiler_turm` wieder `None`. **Über dasselbe Attribut, mit dem deine Aufräumphase seit Etappe 13 einen gefallenen Basisturm von einem gefallenen Marine unterscheidet** — keine Typabfrage.

**Eine Invariante für deine Liste**, aufgeschrieben, nicht geprüft: *Ist `welt.mobiler_turm` nicht `None`, steht genau dieses Objekt in `welt.trupp` — und ist es `None`, steht kein mobiler Turm im Trupp.* Zwei Namen für ein Objekt, Etappe 10: Wer die eine Stelle ändert und die andere vergisst, hat einen Turm, der feuert, aber nicht existiert. Etappe 19 braucht genau diesen Satz, wenn der Turm gespeichert wird.

⚠️ **Er entsteht mitten in einer Welle.** Das ist genau der Fall, für den Etappe 17c das Merkattribut für den Wellenbericht an die Einheit gelegt hat statt in ein Dictionary der Welt. Prüf, ob dein Bericht ihn ohne `KeyError` nennt.

**So prüfst du es:** In der Probedatei einsetzen, tick für tick zählen und **vorher aufschreiben**, in welchem Tick er zum ersten Mal feuert und in welchem er verschwindet — nach deiner Zählersemantik aus Etappe 13, Schritt 7. Ein zweiter Einsatz, während er steht: `False`. Nachdem er verschwunden ist: geht wieder, sobald die Abklingzeit um ist.

---

### 28. Aura — ein Effekt für viele

`Medic`, Zweig `"aura"`: Jede aktive Einheit des Trupps im Abstand höchstens `1 + s` vom Medic — ihn selbst eingeschlossen — bekommt `bekomme_effekt("abgeschirmt", welt)`. `True`.

**Das ist alles.** Die Wirkung hast du in 18a, Schritt 6, schon gebaut, die Ablaufzeit in Schritt 4. **Die Aura ist der Grund, warum die Statuseffekte vor den Fähigkeiten kamen:** Der Lehrplan nennt sie die schwerste Fähigkeit — einen Effekt mit Ablaufdatum an mehreren Einheiten gleichzeitig —, und du schreibst sie in fünf Zeilen, weil jede Einheit ihre Effekte selbst trägt.

**So prüfst du es:** Drei Kameraden, zwei nah beim Medic, einer weit weg. Aura — zwei plus der Medic sind abgeschirmt, und ein Treffer auf einen von ihnen zieht halb so viel ab. Vier Takte später ist sie vorbei.

---

### 29. ⭐⭐ Lass den Trupp seine Fähigkeiten einsetzen

Nach Konzept 18. **Die letzte Ausbaustufe der Trupp-KI.**

**`will_einsetzen(name, welt)`** — in `Marine` mit `return False`, in jeder Unterklasse überschrieben, wieder eine Kette über die eigenen Fähigkeiten:

| Fähigkeit | Ein Kamerad will sie einsetzen, wenn … |
|---|---|
| `"heilung"` | eine aktive Einheit im Abstand höchstens seiner Reichweite **weniger als die Hälfte** ihres Startwerts hat |
| `"aura"` | außer ihm selbst **mindestens zwei** aktive Einheiten im Aurabereich stehen |
| `"durchschlag"` | er damit **mindestens zwei** Gegner träfe |
| `"granate"` | im Bereich um den nächsten Gegner **mindestens zwei** Gegner stehen |
| `"mine"` | der nächste Gegner höchstens `3` Felder entfernt ist und auf seinem Feld noch keine Mine liegt |
| `"mobiler_turm"` | kein mobiler Turm steht und ein Gegner höchstens `aktuelle_reichweite(welt) + 2` entfernt ist |

**In `Marine.update()`** — nach den Prüfungen auf `gesteuert` und `"tot"`, **vor** Bewegung und Feuern:

- Für jede gelernte Fähigkeit: Darf er (`kann_einsetzen()` liefert `None`) **und** will er? Dann `setze_ein()`. Hat das geklappt, ist sein Takt verbraucht — **zurück**, ohne zu laufen oder zu feuern.
- Hat keine Fähigkeit gewirkt, geht es weiter wie bisher.

⚠️ **Der Held bekommt nie ein `will_einsetzen()`.** Seine `update()` steigt seit Etappe 12 bei `gesteuert` sofort aus, und das bleibt so. **Fähigkeiten hat jeder, aber nur der Held wählt selbst.**

⚠️ **Und jetzt eine Beobachtung, keine Anweisung.** Sieh dir den Zweig `"durchschlag"` in `wirke()` und in `will_einsetzen()` nebeneinander an. Beide suchen dieselben Gegner — einmal, um sie zu treffen, einmal, um sie zu zählen. **Dieselbe Suche zweimal geschrieben.** Das ist die Erkenntnis, auf die der Lehrplan für diese Etappe zeigt, und es gibt einen billigen Ausweg: eine kleine Methode, die die Ziele sucht und als Liste zurückgibt, und beide Stellen fragen sie. **Ob du sie heute baust oder die Doppelung notierst, entscheidest du.** Etappe 23 macht aus genau diesen Suchen Werte, die man weiterreichen kann.

**So prüfst du es:** Im Spiel, mit Kameraden auf passender Stufe — setz ihre Erfahrung zum Testen von Hand hoch, damit sie in `lerne_selbst()` etwas lernen. Eine Welle zusehen. **Mindestens eine Fähigkeit wird von einem Kameraden eingesetzt, ohne dass du etwas tust, und keine wird zweimal hintereinander eingesetzt, solange ihre Abklingzeit läuft.** Den Testwert danach zurück.

*(Wenn deine Kameraden in einem normalen Spiel kaum Stufe 2 erreichen, ist das kein Fehler von heute — es ist eine Notiz für das Balancing in Etappe 21b. Die Stufenschwellen sind seit Etappe 5 bewusst grob.)*

---

### 30. Prüf, dass das Alte noch läuft, und commit

- Alles aus Schritt 9 und 18 noch einmal.
- **Der Beweislauf aus Etappe 17b:** zwei Läufe mit festem Seed und `befehle17.txt`, Wellenschleife bei `8` — `diff` muss schweigen. **Heute ist er wichtiger als je**: Deine Kameraden lernen und entscheiden jetzt selbst. Wenn `diff` redet, gibt irgendwo eine Stelle etwas in wechselnder Reihenfolge aus — ein Set, Konzept 11 aus 17b.
- Kein fester `SEED`, Wellenschleife bei `1`, keine von Hand gesetzte Erfahrung.
- Keine `probe.py`, keine `lauf*.txt`.
- Die Abschnitte am Ende, die zu 18c gehören: **Kaputtmachen 9 und 10** und **die Entwicklerfrage**.

Commit: `Etappe 18c: Die Fähigkeiten wirken`

**Und danach: spiel.** Eine Welle, ohne Probedatei, ohne Prüfung, ohne festen Seed. Sieh zu, wie ein Kamerad heilt, eine Mine hochgeht, ein Turm aufgebaut wird und wieder verschwindet. **Seit Etappe 2 standen vier Klassengeräte als Text in deinem Programm. Ab heute kämpfen vier verschiedene Marines** — und drei davon entscheiden selbst, wann.

---

## Selbsttest — 18c

- [ ] `faehigkeit_einsetzen` und `ABKLINGZEIT` kommen im Code nicht mehr vor.
- [ ] Der `diff` aus Schritt 20 war leer — oder du hast eine Doppelgutschrift gefunden und dokumentiert.
- [ ] Ein Fehlversuch — Heilung ohne Verletzte, Granate ohne Ziel, zweite Mine auf einem Feld — kostet **weder** schwere Munition **noch** eine Abklingzeit.
- [ ] Ein gelungener Einsatz kostet beim Helden schwere Munition und startet bei jedem die Abklingzeit — bei den Kameraden ohne Munition.
- [ ] Jede der sechs aktiven Fähigkeiten hat in der Probedatei einmal gewirkt.
- [ ] Die Heilung hebt nie über den Startwert und holt niemanden zurück, der liegt.
- [ ] Der Durchschlag trifft nichts außerhalb seiner Reichweite, auch nicht in seiner eigenen Zeile.
- [ ] Die Mine steht in keiner Liste, über die der Tick `update()` aufruft — und sie geht nach der Gegnerphase hoch.
- [ ] Es gibt höchstens einen mobilen Turm. Nach seiner Lebensdauer verschwindet er aus dem Trupp, und `welt.mobiler_turm` ist wieder `None`.
- [ ] Nirgends fragt der Code, welche Klasse eine Einheit hat.
- [ ] Ein Kamerad setzt eine Fähigkeit ein, ohne dass du etwas tust — und nie, solange ihre Abklingzeit läuft.
- [ ] ⭐ **Der Beweislauf aus 17b schweigt.**

---

## Was NICHT in diese Etappe gehört

**Keine Effekte auf Gegner.** Heute tragen nur Einheiten des Trupps Effekte, weil nur für sie die Zählerphase läuft. Ein brennender Gegner ist eine Kür unter *„Wenn du mehr willst"* — mit einer Reihenfolgefrage, die du dort entscheiden musst.

**Keine Werte-Tabelle pro Fähigkeitsstufe.** Die Zahlen stehen heute als Formel — `10 · s`, `6 · s`. Sobald eine Stufe mehr ändern soll als eine Zahl, wird daraus eine Tabelle *Stufe → Werte*. Etappe 22.

**Kein Zusammenführen von `FAEHIGKEITEN`, `ABKLINGZEITEN` und `SCHWERE_KOSTEN`.** Etappe 22.

**Keine Funktionen als Werte.** Die `elif`-Ketten in `wirke()` und `will_einsetzen()` bleiben. Etappe 23a.

**Kein `Enum` für Effekt- und Flag-Wörter.** Strings, und die Disziplin aus Etappe 15. Etappe 21b.

**Keine Rekruten und Söldner.** Sie bekommen dieselben Effekte, weil Effekte an `Einheit` hängen — aber entstehen tun sie in Etappe 22.

**Kein Skillpunkt als Zahlenbonus.** Kein *„+10 Trefferpunkte"*, kein *„+2 Schaden"* für den Marine. Größere Zahlen kommen aus dem Depot.

**Keine Voraussetzung aus Vaporium.** Weder als Freischaltung noch als Betrag.

**Keine weitere Trupp-KI.** Rückzug, Fokusfeuer, Formationen, Absprachen, Ausweichen — alles reizvoll, alles ein Abend, nichts davon lehrt dich Python, das nicht schon woanders steht. Nach Etappe 27 gehört das Spiel dir.

**Keine Fallen, keine Reparatur.** Der Engineer hat Mine und Turm. Weitere Werkzeuge sind Inhalt, keine neue Technik.

**Keine Traglast und keine Gewichtsgrenze** für die schwere Munition.

**Kein Speichern.** Effekte, Abklingzeiten, Skillpunkte, Fähigkeiten, Minen, der mobile Turm und `welt.flags` — alles gehört in den Spielstand, und das ist Etappe 19.

**Keine Balance.** Die Zahlen oben sind Startwerte. Etappe 21b, auf einem eigenen Branch.

---

## Lernziele

In `GELERNT.md`, ohne nachzuschlagen — jeweils nach der Portion, zu der sie gehören.

**18a**

1. Welche drei Sorten Zustand kennt dein Spiel jetzt — mit je einem Beispiel und der Struktur, die dazu passt?
2. Warum sind die Effekte ein Dictionary und kein Set?
3. Warum darfst du in der Schleife über ein Dictionary die Werte ändern, aber keinen Eintrag löschen — und was machst du stattdessen?
4. **⭐ Warum berechnest du den aktuellen Schaden, statt ihn zu speichern? Nenn zwei Wege, auf denen ein vorübergehend veränderter Grundwert falsch bleibt.**
5. Ein Effekt mit Dauer 3 — wie viele Takte wirkt er bei deinem Helden, wie viele bei einem Kameraden, und warum?
6. Warum ist *„der Effekt läuft ab"* schwerer zu prüfen als *„der Effekt ist aktiv"*?

**18b**

7. Was gibt `a or b` zurück, wenn `a` truthy ist — und warum wird `b` dann gar nicht ausgewertet?
8. Wann ist `x or ersatz` falsch? Nenn den Wert, an dem es kippt.
9. Warum gibt `kann_lernen()` einen Grund zurück statt `True` oder `False` — und wie fragt jemand, der nur Ja oder Nein braucht?
10. Was liefert `benoetigt - vorhanden`, und warum gibst du das Ergebnis nicht direkt aus?
11. Warum darf eine Fähigkeit eine Erkenntnis voraussetzen, aber keine Freischaltung?
12. Warum ist die Reihenfolge deiner Fähigkeitentabelle der Lernplan deiner Kameraden?

**18c**

13. `setze_ein()` steht in `Marine` und ruft `self.wirke()` auf. Welche Fassung läuft, und warum?
14. Warum wird erst **nach** `wirke()` bezahlt — und was passiert, wenn in einem Zweig von `wirke()` das `return` fehlt?
15. Warum steht der mobile Turm im Trupp und die Mine nicht?
16. Was unterscheidet `kann_einsetzen()` von `will_einsetzen()` — und warum hat der Held nur eines davon?
17. Was unterscheidet das Schnellfeuer vom Durchschlag, außer dass beides mehr als einen Gegner trifft?

**Frage 4 ist die wichtigste.** Sie gilt weit über dieses Spiel hinaus: Jeder Wert, der sich aus anderen ergibt und trotzdem gespeichert wird, ist eine zweite Wahrheit, die irgendwann nicht mehr stimmt.

---

## 🧠 Die Entwicklerfrage — zu 18c

Sie hat keine Musterlösung, und niemand korrigiert sie.

> **Wo gehört Zustand hin — zur Einheit oder zur Welt?**

Du hast heute sechs Antworten gebaut, und der Plan hat jede für dich getroffen: **Effekte** an der Einheit. **Abklingzeiten, Skillpunkte, Fähigkeiten** am Marine. **`flags`** an der Welt. **Minen** an der Welt, als Liste. **Der mobile Turm** im Trupp *und* unter einem Namen an der Welt.

Nimm eine davon, von der du glaubst, dass sie auch anders ginge — und schreib auf, was dafür spräche. Ein brennender Gegner: Eigenschaft des Gegners, oder ein Eintrag in einer Liste der Welt? **Beides funktioniert.** Was kostet welches, sobald der Gegner fällt?

**Zwei bis fünf Sätze in `GELERNT.md`.** Du liest sie in Etappe 22 wieder, wenn die Zahlen zu Tabellen werden, und in Etappe 19, wenn du all das speichern musst.

---

## Transferaufgabe (15 Minuten) — zu 18a

**Außerhalb des Spiels.** Ein Gewächshaus, kein Vorposten. In einer Wegwerf-Datei.

**Teil 1.** Eine Klasse `Pflanze` mit `blaetter` (Start `10`), `wachstum` (Blätter pro Tag, Start `3`) und einem Dictionary `zustaende` *Name → Restdauer*.

- `lichtmangel` halbiert das Wachstum, solange er läuft.
- `schaedlinge` fressen jeden Tag ein Blatt.
- Eine Methode `tag()`: zuerst wachsen, dann die Schädlinge fressen lassen, dann alle Zustände herunterzählen und die abgelaufenen löschen — nach Konzept 2.
- Das Wachstum eines Tages kommt aus einer Methode `aktuelles_wachstum()` — nach Konzept 4.

Start mit `{"lichtmangel": 2, "schaedlinge": 3}`. **Schreib vorher auf**, wie viele Blätter die Pflanze nach fünf Tagen hat. Dann ausführen.

**Teil 2 — der eigentliche.** Bau die Pflanze ein zweites Mal, **falsch**: Beim Beginn des Lichtmangels wird `self.wachstum` halbiert, beim Ende verdoppelt. Lass beide Fassungen zehn Tage laufen.

- **Wie viele Blätter wachsen am Tag nach dem Lichtmangel** — in der richtigen Fassung und in der falschen?
- Mit welchem Startwert für `wachstum` wäre der Fehler **nicht** aufgefallen?

**Die zweite Frage ist der Kern.** Ein Fehler, der nur bei ungeraden Zahlen auftritt, überlebt jeden Test mit geraden. Schreib auf, was das für deine Probedatei-Prüfungen heißt.

---

## Leseübung — Stufe 3 (15 Minuten) — zu 18b

**Die Leitfrage bleibt die aus Etappe 17b: Warum ist es so gebaut?** Du tippst nichts ab und führst nichts aus.

```python
KURSE = {
    "toprope":  {"ab_alter": 8,  "braucht": set(),                   "plaetze": 10},
    "vorstieg": {"ab_alter": 14, "braucht": {"toprope"},             "plaetze": 6},
    "sturz":    {"ab_alter": 16, "braucht": {"toprope", "vorstieg"}, "plaetze": 0},
    "boulder":  {"ab_alter": 6,  "braucht": set()},
}


class Kletterhalle:
    """Nimmt Anmeldungen an — aber nur, wenn nichts dagegen spricht."""

    def __init__(self):
        self.belegt = {}            # Kurs -> Anzahl Anmeldungen

    def freie_plaetze(self, kurs):
        plaetze = KURSE[kurs].get("plaetze") or 12
        return plaetze - self.belegt.get(kurs, 0)

    def einwand(self, kurs, person):
        if kurs not in KURSE:
            return "Diesen Kurs gibt es nicht."
        if person["alter"] < KURSE[kurs]["ab_alter"]:
            return f"Erst ab {KURSE[kurs]['ab_alter']} Jahren."
        fehlend = KURSE[kurs]["braucht"] - person["scheine"]
        if fehlend:
            return "Es fehlt noch: " + ", ".join(fehlend)
        if self.freie_plaetze(kurs) <= 0:
            return "Ausgebucht."
        return None

    def anmelden(self, kurs, person):
        grund = self.einwand(kurs, person)
        if grund is not None:
            print(f"{person['name']}: {grund}")
            return False
        self.belegt[kurs] = self.belegt.get(kurs, 0) + 1
        print(f"{person['name']}: angemeldet für {kurs}.")
        return True


halle = Kletterhalle()
mia = {"name": "Mia", "alter": 15, "scheine": {"toprope"}}
ben = {"name": "Ben", "alter": 17, "scheine": set()}
ada = {"name": "Ada", "alter": 30, "scheine": {"toprope", "vorstieg"}}

halle.anmelden("vorstieg", mia)
halle.anmelden("sturz", ben)
halle.anmelden("sturz", ada)
halle.anmelden("boulder", ben)
print(halle.freie_plaetze("boulder"))

darf = mia["alter"] >= 14 and mia["scheine"]
print(darf)
```

**Die fünf Fragen, für `anmelden()`:**

1. Was kommt rein?
2. Was passiert?
3. Was verändert sich — und woran?
4. Was kommt raus?
5. Welche anderen Methoden werden dabei aufgerufen?

**Und die Stufe-3-Fragen:**

6. **Schreib alle Ausgabezeilen hin**, in der Reihenfolge, in der sie entstehen. ⚠️ Bei einer davon kannst du die Reihenfolge der Wörter nicht sicher sagen. Welche, und warum? *(18b, Konzept 10.)*
7. **⭐ Ada wird für den Sturzkurs angemeldet.** Der Kurs hat laut Tabelle `0` Plätze. **Welche Zeile lässt sie trotzdem hinein, und was hätte dort stehen müssen?** Und warum funktioniert dieselbe Zeile beim Boulderkurs richtig?
8. `einwand()` gibt einen Text oder `None` zurück, `anmelden()` gibt `True` oder `False` zurück. **Warum nicht beide dasselbe?** Wer braucht welche Antwort?
9. **Warum steht die Prüfung auf freie Plätze zuletzt in der Kette?** Was sähe Ben, wenn sie an erster Stelle stünde und der Kurs ausgebucht wäre?
10. **Was steht in der letzten Zeile der Ausgabe** — und warum ist es weder `True` noch `False`? *(18b, Konzept 12.)* Wäre `if darf:` trotzdem richtig?
11. `belegt` ist ein Dictionary, `braucht` ist ein Set. **Warum nicht umgekehrt?** *(Etappe 15, Konzept 2.)*

---

## Kaputtmachen

**Vor jedem Experiment aufschreiben, was passieren wird.** Nummer 1 bis 3, 6, 7, 9 und 10 gehören dazu, die übrigen sind Kür. **Nach jedem Experiment alles zurück.**

### Zu 18a

**1. ⭐ Lösch in der Schleife.** Nimm in deiner Effekt-Zählschleife die Liste `abgelaufen` weg und lösch direkt beim Erreichen von `0`. Lies den `RuntimeError` ganz. **Das ist ein Typ-1-Fehler — und der freundliche Fall**, weil er dir die Zeile sagt.

**2. ⭐⭐ Vergiss das Löschen.** Jetzt das Gegenteil: Lass den Effekt bei `0` einfach stehen. Gib dir `test_effekt veraetzt` *(den Entwicklerbefehl kurz zurückholen)* und spiel zehn Takte. **Was steht danach in `effekte` — und hört der Schaden auf?** Kein Absturz, und dein Marine ist für immer verätzt. Das ist der Typ-3-Fehler zu Nummer 1: Das eine knallt, das andere läuft falsch weiter.

**3. ⭐⭐ Verändere den Grundwert.** Bau `erschuettert` so, dass beim Beginn `self.schaden` halbiert und beim Ende verdoppelt wird — der Kaffee aus Konzept 4. Gib deinem Helden vorher einen **ungeraden** Schaden. Lass den Effekt ablaufen und sieh dir `self.schaden` an. **Dann noch einmal, und diesmal fällst du, während er läuft.** Mit welchem Schaden stehst du auf?

*Kür:*

**4. Nimm einen `super()`-Aufruf heraus.** Aus `Marine.zaehler_runter()`. Wer bekommt jetzt noch Ätzschaden — und bei wem läuft ein Effekt nie ab? *(Wenn dein Basisturm getroffen werden kann, ist er der Vergleich.)*

**5. Verlängern statt erneuern.** Mach aus der Zuweisung in `bekomme_effekt()` ein `+=`. Lass eine Welle mit vielen Speiern auf dich los. Wie lang ist die Restdauer am Ende?

### Zu 18b

**6. ⭐⭐ Zwei Quellen, ein Wort.** Benenn testweise einen Ausbau in `AUSBAUTEN` so um, dass er genauso heißt wie eine deiner Erkenntnisse. Analysier den passenden Fund. **Was besitzt du jetzt, ohne es gekauft zu haben?** Und in der anderen Richtung: Was weißt du, nachdem du den Ausbau gekauft hast? Kein Absturz, keine Meldung — das ist der Preis aus der Design-Entscheidung von 18b, und die Invariante aus Schritt 10 d) ist der Schutz dagegen.

**7. ⭐ Die `or`-Falle am eigenen Code.** Ersetz in `kann_lernen()` die Zeile mit `.get(name, 0)` durch `self.faehigkeiten.get(name) or 1`. Was zeigt `faehigkeiten` jetzt bei einer Fähigkeit, die du nie gelernt hast? Und lässt sich eine Fähigkeit auf Stufe 2 noch bis 3 lernen? **Schreib auf, warum die eine Zeile an der einen Stelle harmlos aussieht und an der anderen nicht.**

*Kür:*

**8. Nimm das Ende aus `lerne_selbst()`.** Lass nur die Bedingung *„solange Punkte da sind"* stehen. Gib einem Kameraden einen Punkt und nichts Lernbares. Brich mit `Strg + C` ab und lies im Traceback, wo er war.

### Zu 18c

**9. ⭐⭐ Vergiss ein `return`.** Nimm im Zweig `"granate"` das `return True` heraus. Setz die Granate dreimal hintereinander ein. **Explodiert sie? Kostet sie? Läuft eine Abklingzeit?** Und was meldet dein Spiel? Das ist Konzept 14 am eigenen Code: Ein fehlendes `return` sieht aus wie `False` — und aus einer Fähigkeit wird eine, die man ohne Grenze einsetzen kann.

**10. ⭐ Nimm die Klammern weg.** In der Bedingung des Durchschlags. Setz einen Gegner in die Zeile des Heavy, zehn Felder entfernt. Wird er getroffen? Setz einen in die Spalte, ebenso weit. Und der? **Zwei Richtungen, zwei verschiedene Antworten — aus einem Paar Klammern.**

*Kür:*

**11. Leg die Mine in den Trupp.** Mach sie testweise zu einer `Einheit` und häng sie an `welt.trupp`. Spiel eine Welle und lies den Wellenbericht. Wie viele Stellen in deinem Spiel wissen jetzt von einer Mine, ohne dass du sie dafür gebaut hast?

**12. Bezahl vor der Wirkung.** Zieh in `setze_ein()` die schwere Munition vor dem Aufruf von `wirke()` ab. Versuch die Granate ohne Gegner in Reichweite. Was hast du bezahlt, wofür?

---

**Experiment 2 und 9 sind das Paar.** Beide stürzen nie ab, beide laufen tagelang unbemerkt — das eine hält einen Zustand fest, der längst vorbei sein sollte, das andere verschenkt eine Handlung, die etwas kosten sollte. **Und beide hätte eine einzige Zeile verhindert**, die man beim Hinschreiben für selbstverständlich hält.

Alles in `GELERNT.md` und ins Fehlertagebuch aus Etappe 8: **woran du es erkannt hättest.**

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| `RuntimeError: dictionary changed size during iteration` | `del` in der Schleife über dasselbe Dictionary | 18a, Konzept 2 — sammeln, dann löschen |
| Ein Effekt endet nie, die Restdauer wird negativ | Er wird bei `0` nicht gelöscht | Schritt 4 · Kaputtmachen 2 |
| Effekte laufen beim Turm ab, bei Marines nie | `super().zaehler_runter(welt)` fehlt in einer Überschreibung | Schritt 4 — Fahndung nach allen Überschreibungen |
| Der Ausfallzähler eines Marines steht still, seit Effekte laufen | `return` für `"tot"` steht in der Marine-Fassung statt nur in der Basisfassung | Schritt 4, letzter Hinweis |
| Der Beginn eines Effekts wird nie gemeldet | Erst gesetzt, dann gefragt | Schritt 2 — Reihenfolge |
| Nach einem Effekt ist der Schaden dauerhaft kleiner | Der Grundwert wurde verändert statt berechnet | 18a, Konzept 4 · Kaputtmachen 3 |
| Erschüttert wirkt beim Kameraden einen Takt kürzer als beim Helden | Kein Fehler — Zählerphase vor Truppphase, der Held handelt zwischen den Ticks | Schritt 5 |
| `KeyError: 'effekt'` | Der Kriecher hat keinen Eintrag, und es wird mit eckigen Klammern gelesen | Schritt 1 — `.get()` |
| `AttributeError: … has no attribute 'faehigkeiten'` beim Basisturm | Die Standfest-Prüfung steht in `Einheit` | Schritt 17 |
| `diff` redet nach dem Flag-Umzug | Ein Set wird ausgegeben — oft im `__repr__` der Welt | Schritt 10 — `len()` statt des Sets |
| `AttributeError: 'Welt' object has no attribute 'erkenntnisse'` | Eine Stelle wurde beim Umzug übersehen | Schritt 10 — Fahndung, freundlicher Fall |
| Die Meldung *„Dir fehlt noch"* hat wechselnde Reihenfolge | Das Differenz-Set wird direkt ausgegeben | 18b, Konzept 10 — über `FUNDE` laufen |
| Eine Fähigkeit lässt sich nie lernen, ohne dass gesagt wird, warum | Ihr Flag-Wort steht nicht in `FUNDE` — ein Verweis ins Leere | Schritt 14 — kopieren, nicht abtippen |
| *„Das kann nur, wer … trägt"* bei der eigenen Klasse | `"geraet"` weicht von `klassengeraet` ab — Groß- und Kleinschreibung | Schritt 14 |
| Das Spiel hängt nach einem Aufstieg | `lerne_selbst()` endet nur bei null Punkten | Schritt 16 · Kaputtmachen 8 |
| Jede gesperrte Fähigkeit zeigt nur *„Dir fehlt ein Skillpunkt"* | Die Skillpunkt-Prüfung steht zu weit vorne | Schritt 15 |
| Kameraden steigen nie auf | Sie bekommen keine Erfahrung | Schritt 13 |
| Eine Fähigkeit wirkt, kostet aber nichts und ist sofort wieder bereit | Ein Zweig von `wirke()` ohne `return True` | 18c, Konzept 14 · Kaputtmachen 9 |
| Ein Fehlversuch kostet Munition oder Abklingzeit | Bezahlt vor `wirke()` | Schritt 22 · Kaputtmachen 12 |
| Abschüsse durch Fähigkeiten zählen nicht, oder doppelt | Gutschrift an der Fähigkeit vorbei — oder `treffe()` ohne Prüfung auf `"tot"` | Schritt 20 |
| Der Durchschlag trifft die ganze Zeile | Klammern um den `or`-Teil fehlen | 18c, Konzept 16 · Kaputtmachen 10 |
| Eine Mine geht nie hoch | Die Minenphase fehlt oder steht vor der Gegnerphase | Schritt 26 |
| Der mobile Turm bleibt nach seiner Lebensdauer stehen | Die Aufräumphase entfernt ihn nicht, oder `welt.mobiler_turm` bleibt gesetzt | Schritt 27 |
| `KeyError` mit dem Namen des mobilen Turms im Wellenbericht | Das Merkattribut aus 17c steht in einem Dictionary der Welt statt am Objekt | Etappe 17c, Konzept 15 |
| Ein Kamerad setzt dieselbe Fähigkeit jeden Takt ein | `will_einsetzen()` ohne `kann_einsetzen()` gefragt — oder die Abklingzeit wird nicht eingetragen | Schritt 29 · Schritt 22 |
| Der Held setzt Fähigkeiten von selbst ein | Die Prüfung auf `gesteuert` fehlt am Anfang von `update()` | Schritt 29 |

**Der Debugging-Reflex dieser Etappe: „Was steht gerade drin — und seit wann?"**

Etappe 15 fragte *steht das Wort wirklich zweimal gleich da*, 16 *in welcher Reihenfolge*, 17 *mit welchem Seed*. **Heute kommt die Zeit dazu:** Effekte und Abklingzeiten sind Dictionaries, deren Inhalt sich jeden Takt ändert.

```python
print("### TAKT", welt.zeit, einheit.name, einheit.effekte, einheit.abklingzeiten)
```

**Eine Zeile pro Takt, und du siehst, wann ein Eintrag entsteht, sinkt und verschwindet** — statt nur, dass er irgendwann nicht mehr da ist.

---

## Ein Blick nach vorne

**Etappe 19 speichert das Spiel** — und heute hast du ihm eine Menge zu speichern gegeben: `welt.flags` ist ein Set und überlebt JSON nicht, die Schuld aus Etappe 6. Effekte und Abklingzeiten sind Dictionaries aus Wörtern und Zahlen und überleben es gut. Minen zeigen auf ihren Besitzer — ein Objekt, kein Wort. **Und der mobile Turm steht an zwei Stellen**, im Trupp und unter einem Namen an der Welt. Wie sorgst du dafür, dass er nach dem Laden wieder *ein* Turm ist und nicht zwei?

**Etappe 20 macht aus Gründen Fehler.** Deine Prüfketten liefern heute einen Text oder `None`. Dort lernst du einen zweiten Weg, einen Grund durch das Programm zu tragen — und die Frage, welcher Grund dem Spieler gehört und welcher dem Entwickler.

**Etappe 21a rechnet den Kampf richtig.** Dein `aktueller_schaden()` ist dort der Eingang, und die Passiva werden von der Trefferrechnung abgefragt.

**Etappe 22 zieht die Zahlen zusammen.** `FAEHIGKEITEN`, `ABKLINGZEITEN` und `SCHWERE_KOSTEN` werden eine Tabelle, die Formeln `10 · s` vielleicht eine Tabelle pro Stufe — und dort entstehen die Rekruten, die dieselben Effekte tragen. Und die Entwicklerfrage von heute kommt zurück.

**Etappe 23a lässt die `elif`-Ketten in `wirke()` und `will_einsetzen()` sterben.** Funktionen werden Werte, und die doppelte Zielsuche aus Schritt 29 bekommt ihren Ort.

**Etappe 26 testet.** *„Ein Effekt mit Dauer 3 macht dreimal Schaden"* ist dort eine Zeile, die grün oder rot wird — und deine Tabelle aus Schritt 5 ist die Vorlage dafür.

---

## Abschluss

**In `GELERNT.md`:**

- ⭐⭐ **Die Tabelle aus Schritt 5**, ausgefüllt, und in einem Satz: was „Dauer 3" in deinem Spiel bedeutet — für den Helden und für einen Kameraden.
- ⭐ Deine Antwort auf die Design-Entscheidung aus 18a: Wo wohnt ein Effekt?
- Wie viele Stellen die Fahndungen gekostet haben: `zaehler_runter`-Überschreibungen, Schaden-Austeiler, `nachladen_noetig`, der Flag-Umzug, die Gutschriften für `treffe()`.
- Deine Entscheidung zu `funk_gehoert`.
- Die Invariante *„kein Wort in zwei Quellen"* in deiner Liste.
- Ob `lerne` eine Runde kostet — und ob ein fehlgeschlagener Fähigkeitseinsatz eine kostet.
- Wo die Standfest-Prüfung wohnt — `Marine` oder `Einheit` — und warum.
- Die neue Tick-Reihenfolge mit der Minenphase, neben der aus Etappe 16.
- Die drei Tabellen mit demselben Schlüsselsatz, notiert für Etappe 22.
- Ob du die doppelte Zielsuche aus Schritt 29 gebaut oder notiert hast.
- 🧠 Die Entwicklerfrage.
- Was hat mich überrascht? *(Kandidaten: dass ein Effekt bei Held und Kamerad verschieden lang wirkt · dass die Aura fünf Zeilen war · dass ein fehlendes `return` Espresso verschenkt · dass `or` aus null zehn macht.)*

**Vor dem Commit:** kein `test_effekt`, kein fester `SEED`, Wellenschleife bei `1`, keine von Hand gesetzte Erfahrung, keine `probe.py`, keine `vorher.txt`, `nachher.txt` oder `lauf*.txt`, kein `breakpoint()`?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest.

**Gegner bekommen Effekte.** Die Granate setzt auf jeden getroffenen Gegner `"brennend"` — ein vierter Eintrag in `EFFEKTE`, mit `"pro_tick"`. Damit er abläuft, braucht die Zählerphase auch eine Schleife über `welt.gegner`. **Und dann die Frage, die du in Etappe 16 gelernt hast zu stellen:** Wenn ein Gegner an seinem Brand fällt — in der Zählerphase, **vor** der Truppphase —, bekommt jemand den Abschuss? Wer? Schreib die Regel auf, bevor du baust.

**Eine Funktion für beide Zähl-Dictionaries.** Du zählst Effekte und Abklingzeiten mit demselben Block herunter. Eine Funktion, die ein Dictionary herunterzählt, das Abgelaufene löscht und die Liste der abgelaufenen Namen zurückgibt, spart dir den zweiten. **Dann zähl die Zeilen vorher und nachher** — und frag dich, ob sie auch in Etappe 22 noch passt, wenn Abklingzeiten mehr können sollen.

**Die Heilung im Wellenbericht.** Wie viele Trefferpunkte hat der Medic in dieser Welle geheilt? Dasselbe Merkmuster wie die Abschüsse aus 17c — und eine Zeile mehr in seiner Stimme.

**Effekte im Vorfeld zeigen.** Eine verätzte Einheit wird mit einem anderen Zeichen gemalt. `zeichne_vorfeld()` bekommt dafür nichts Neues übergeben — die Einheiten trägt sie schon. Prüf danach, ob sie noch rein ist.

**Ein eigener Lernplan pro Klasse.** Statt über die ganze Tabelle zu laufen, bekommt jede Marine-Klasse ein Tuple mit den Namen, die ihre Kameraden in dieser Reihenfolge lernen sollen. Wem gehört diese Reihenfolge — der Klasse oder der Tabelle?

---

> **Nächste Etappe:** Etappe 19 — Speichern und Laden · der Vorposten überlebt das Beenden, und ein Set lernt, dass es in einer Datei eine Liste ist
