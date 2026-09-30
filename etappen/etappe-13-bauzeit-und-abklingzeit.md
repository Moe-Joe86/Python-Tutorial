# Etappe 13 — Bauzeit und Abklingzeit

*v2.0.1 · 2026-09-16*

> **Block 2: Einheiten und Zeit** · Etappe 13 von 30 · [← Etappe 12](etappe-12-der-tick.md) · [Lehrplan](../Vorposten_Lehrplan.md) · [Etappe 14 →](etappe-14-das-vorfeld.md)

**Neue Syntax heute:** Der Zähler als Bauform · ein Zähler am Objekt · `welt.melde(text)` als einziger Ausgabeort · einen Wert merken, neu berechnen, vergleichen · `d[a][b] = wert` — schreibend in ein verschachteltes Dictionary · `del d[key]` (hochgestuft aus Etappe 5, **nur für eine der beiden Varianten aus Konzept 10**) · 👀 der Begriff *Scheduler*

**Zeitaufwand:** 13a: 3–4 Sitzungen · 13b: 4–5 Sitzungen, à 20–30 Minuten. Knapp 50 Minuten davon sind Lesestoff, rund 25 je Portion — lies jeweils nur die Portion, an der du sitzt.

⚠️ **Der Lehrplan nennt diese Etappe „klein und freundlich". Das stimmt für jedes einzelne Stück und nicht für die Summe.** Eine Abklingzeit ist tatsächlich ein Zähler, ein `if` und eine Meldung — fünfzehn Minuten. Heute baust du dieselben fünfzehn Minuten **fünfmal**, an fünf verschiedenen Objekten. Nichts davon ist schwer. Es ist nur mehr, als der Satz vermuten lässt.

⚠️ **Und 13b ist konzeptionell schwerer als 13a, nicht nur länger.** In 13a beschreibt ein Zähler eine Eigenschaft deines Marines. In 13b beschreibt er zum ersten Mal einen Zustand, der ein anderes Objekt ins Spiel bringt oder zurückholt — und der die Karte verändert. Das ist derselbe Code und ein größerer Schritt.

*(Diese Etappe hat keine Leseübung. Die Leseleiter steht seit Etappe 12 auf Stufe 2 und geht in Etappe 14 weiter — heute steckt die Zeit im Bauen.)*

**Voraussetzung:** Etappe 12 abgeschlossen, Selbsttest grün. Dein Tick läuft, deine Kameraden feuern von selbst, `welt.zeit` zählt hoch. **Ohne einen laufenden Tick hat diese Etappe keinen Gegenstand** — ein Zähler, der nicht heruntergezählt wird, ist eine Zahl.

**Die zwei Portionen:**

| | Was passiert | Was danach anders ist |
|---|---|---|
| **13a** | Das Zähler-Muster, einmal gebaut und einmal verstanden | Deine Fähigkeit aus Etappe 11 hat eine Abklingzeit, und dein Marine steigt hörbar auf |
| **13b** | Dasselbe Muster viermal weiter — Ausfall, Nachladen, Basisturm, Karte | Du kannst fallen, ohne dass das Spiel endet. Der Vorposten hat einen Turm. Und die Landeplattform wird erreichbar. |

| | 🔨 Bauen | 🧠 Verstehen | 👀 Nur erkennen |
|---|---|---|---|
| **13a** | Abklingzeit · Zählerphase im Tick · `welt.melde()` · Stufenaufstieg als Ereignis | **Zustand ist nicht Ereignis** · „ist fertig" ↔ „wurde gerade fertig" | *Scheduler* als zweite Bauart |
| **13b** | Respawn · Ausfallzeit · Bauzeit · Nachladezeit · `welt.raeume_frei()` | Derselbe Zähler, zwei Spielgefühle · warum Karten Zustand sind | Kopplung, zum zweiten Mal — die Frage, nicht die Lösung |

---

## Worum es geht

In Etappe 11 hast du deinen vier Marine-Klassen je eine Fähigkeit gegeben. Sie geben eine Meldung aus. Du kannst sie zwanzigmal hintereinander auslösen, und zwanzigmal passiert dasselbe.

In Etappe 12 hast du einen Tick gebaut. Er zählt `welt.zeit` hoch, und außer den Gegnern interessiert das bisher niemanden.

> **Heute treffen sich die beiden, und dabei entsteht das erste Mal so etwas wie Spannung.**

Du setzt die Fähigkeit ein. Sie ist weg. Du kämpfst weiter, du kaufst etwas, du vergisst sie — und sechs Takte später meldet sie sich von selbst zurück. **Zwischen dem Auslösen und der Rückmeldung hast du nichts getan, was damit zu tun hatte.** Das ist der einfachste mögliche Beweis, dass dein Tick-System wirklich läuft, und es ist ein Spielmoment, den man nicht vergisst.

**Technisch ist das lächerlich wenig.** Drei Zeilen:

```
Zähler größer als null?  →  eins abziehen
Ist er dabei auf null gekommen?  →  etwas melden
```

**Und genau deshalb steht diese Etappe hier.** Nicht weil sie schwer ist, sondern weil dasselbe Muster ab heute an fünf Stellen deines Spiels sitzt und du es beim fünften Mal blind hinschreibst. Das ist der Unterschied zwischen einem Werkzeug, das man kennt, und einem, das man hat.

---

## Der lange Bogen — was heute fällig wird

- **Die zweite Verlustbedingung aus Etappe 1** wird heute erträglich. Seit der ersten Etappe kann dein Marine fallen, und seit Etappe 3a beendet das den Lauf. **Ab heute nicht mehr:** Du fällst, du wartest, du stehst wieder da. Das ist die größte Änderung am Spielgefühl seit dem Tick.
- **Der versiegelte Weg aus Etappe 5.** Du hast damals entschieden, ob der Osttunnel in deiner Karte fehlt oder markiert ist, und der Guide hat dir gesagt, dass wir heute nachschlagen. **Heute schlagen wir nach**, und deine Entscheidung von damals entscheidet, ob Auftragsschritt 17 eine Zeile ist oder drei.
- **Der Erfahrungszähler aus Etappe 3c.** Er steigt seit zehn Etappen und tut nichts. Heute tut er zum ersten Mal etwas — nicht viel, aber hörbar.
- **Die Fähigkeiten aus Etappe 11** bekommen ihre Abklingzeit. Wirkung bekommen sie immer noch nicht; das bleibt Etappe 18.
- **Die Werkbank aus Etappe 5**, an der bisher nichts ging, bekommt heute ihren Zweck: Hier wird der Basisturm in Auftrag gegeben. Damit hat die Werkstatt ihren ortsgebundenen Befehl — wie das Depot seit Etappe 5.
- **Der Satz aus Etappe 12**, dass die Truppliste Fremdkörper aufnimmt, wird heute wahr: Der Turm steht in `welt.trupp` und tickt mit, obwohl er kein Marine ist.
- **Der offene Posten aus Etappe 12:** Deine Kameraden feuern ohne Munitionsverbrauch. Heute wird er fällig, und zwar mit demselben Zähler wie alles andere.
- **`assert` aus Etappe 7b** bekommt heute seinen zweiten Anwendungsfall — als aufgeschriebene Invariante, noch nicht als Prüfung.

---

## Eine Design-Entscheidung, die du jetzt treffen musst

### Wo läuft der Zähler? ⭐

Drei Bauarten, und du entscheidest dich heute für eine:

| | Am Objekt | Als eigenes Zähler-Objekt | 👀 Die Welt führt Termine |
|---|---|---|---|
| Wie | Der Marine hat ein Attribut `abklingzeit` | Ein `Abklingzeit`-Objekt hängt am Marine | Die Welt merkt sich: *bei Tick 148 passiert X* |
| Aufwand heute | am kleinsten | mittel | am größten |
| Wer zählt herunter | das Objekt selbst im Tick | das Zähler-Objekt | die Welt, an einer Stelle |
| Bei zwanzig Zählern | zwanzig Attribute, verstreut | zwanzig Objekte, gleich gebaut | eine Liste, sortiert |

**Nimm den ersten Weg.** Ein Attribut am Objekt, dem der Zähler gehört. Die Begründung ist dieselbe wie bei jeder Besitzfrage in diesem Plan, und du kennst sie seit Etappe 9:

> **Die Abklingzeit gehört dem Marine, der die Fähigkeit hat. Die Bauzeit gehört dem Turm, der sich aufbaut. Die Räumzeit gehört der Welt, weil der Tunnel niemandem sonst gehört.**

👀 **Der dritte Weg hat einen Namen, und den sollst du kennen, nicht bauen: Scheduler.** Statt dass jedes Objekt seinen eigenen Zähler mitschleppt, führt die Welt eine Liste von Terminen — *„bei Tick 148: Geschütz aktivieren"* — und arbeitet sie ab. In großen Simulationen ist das oft die bessere Struktur, weil man bei zehntausend Objekten nicht zehntausend Zähler herunterzählen will. **Für dein Spiel mit vier Marines ist der Zähler im Objekt einfacher.** Merk dir nur, dass es beide Bauarten gibt, damit du die andere in fremdem Code nicht für einen Fehler hältst.

⚠️ **Und der zweite Weg ist kein schlechter, sondern ein verfrühter.** Ein eigenes `Abklingzeit`-Objekt lohnt sich, sobald eine Abklingzeit mehr kann als herunterzählen — sich verlängern lassen, unterbrochen werden, gestapelt werden. Das ist Etappe 18. Heute wäre es eine Klasse mit einem Attribut.

**Schreib deine Entscheidung in `GELERNT.md`.** In Etappe 22 kommt sie zurück, wenn alle Zahlen zu Tabellen werden.

---

### Und die zweite Entscheidung: Tick-Zeit oder Echtzeit?

Sie ist schnell erklärt und leicht falsch getroffen.

| | Tick-Zeit | Echtzeit (`time.time()`) |
|---|---|---|
| Wächst | pro Spieleraktion | während du weg bist |
| Kaffee kochen | ändert nichts | ändert alles |
| In Etappe 28 | **ein Tick wird ein Bild**, `bauzeit = 180` sind drei Sekunden | müsste neu gedacht werden |

**Nimm Tick-Zeit, und zwar nicht als Kompromiss.** In Etappe 28 läuft deine Schleife sechzigmal pro Sekunde. Dann *ist* ein Tick eine Zeiteinheit, und jede Zahl, die du heute hinschreibst, bedeutet plötzlich Sekunden — ohne dass sich eine Zeile Zähler-Logik ändert. **Das ist der Grund, warum diese Etappe direkt hinter dem Tick steht und nicht hinter einer Uhr.**

---

# Teil 13a — Der Zähler

## Die Konzepte — Teil 13a

Alle Beispiele laufen **außerhalb** deines Spiels. Heute in einem Waschsalon.

### 1. Das Zähler-Muster ⭐

Ein Waschgang dauert. Solange er läuft, ist die Maschine belegt:

```python
class Maschine:
    def __init__(self, name):
        self.name = name
        self.restzeit = 0

    def starten(self, salon):
        if self.restzeit > 0:
            salon.melde(f"{self.name} läuft noch {self.restzeit} Minuten.")
            return
        self.restzeit = 30
        salon.melde(f"{self.name} gestartet.")
```

Und im Takt des Salons läuft sie herunter:

```python
    def zaehler_runter(self, salon):
        if self.restzeit > 0:
            self.restzeit -= 1
            if self.restzeit == 0:
                salon.melde(f"{self.name} ist fertig.")
```

**Das ist alles.** Drei Zeilen im Takt, drei Zeilen beim Starten. Merk dir die Form, sie kommt heute noch viermal:

> **Ist der Zähler größer als null? → Eins abziehen. Ist er dabei auf null gekommen? → Etwas melden.**

⚠️ **Die äußere Prüfung `> 0` ist nicht Zierde.** Ohne sie läuft der Zähler ins Negative, und `== 0` trifft nie wieder — die Maschine wäre für immer belegt. Genau das probierst du im Kaputtmachen aus.

### 2. Zustand ist nicht Ereignis ⭐⭐

**Das ist der Begriff, der aus dieser Etappe hängen bleiben soll**, und er entscheidet über die Einrückung von genau einer Zeile.

```
maschine.restzeit == 0          ← Zustand.   Gilt, solange er gilt. Beliebig oft abfragbar.
„Maschine ist gerade fertig"    ← Ereignis.  Passiert genau einmal, in genau einem Takt.
```

**Sag voraus, bevor du weiterliest.** Hier ist dieselbe Methode, aber die Meldung ist eine Ebene weiter links:

```python
    def zaehler_runter(self, salon):
        if self.restzeit > 0:
            self.restzeit -= 1
        if self.restzeit == 0:
            salon.melde(f"{self.name} ist fertig.")
```

Eine Maschine startet mit `restzeit = 3`. Wie viele Meldungen kommen in sechs Takten?

Die Antwort ist **vier**. Ab Takt 3 ist `restzeit == 0` wahr, und sie bleibt es — der Zustand gilt ja weiter. Die Maschine schreit in jedem folgenden Takt, dass sie fertig geworden ist.

> **Ein Ereignis entsteht am Übergang von einem Zustand in den nächsten. Wenn du diesen Übergang nicht in dem Moment festhältst, in dem er passiert, ist er nach einem Takt weg.**

**Die eingerückte Fassung hält ihn fest**, weil sie nur in dem Takt läuft, in dem tatsächlich abgezogen wurde. Der Unterschied ist eine Ebene Einrückung, und er ist der ganze Abschnitt.

**Das klingt nach Wortklauberei und ist es nicht.** Alles, was später einmalig auf etwas reagieren soll, hängt daran: eine Meldung, ein Eintrag im Protokoll, ein Ton, eine Animation, ein Speicherpunkt. In Etappe 28 wird daraus die Frage, wann du etwas **zeichnest** und wann du etwas **aufblitzen** lässt.

> **Deine Prüffrage ab heute: Soll das gelten, oder soll das passieren?**

### 3. „Ist fertig" und „wurde gerade fertig" — beides wird gebraucht

Aus Konzept 2 könnte man die falsche Regel ziehen, Zustände seien schlechter als Ereignisse. Sie sind es nicht. **Du brauchst beide, für verschiedene Fragen:**

| Frage | Antwort kommt aus |
|---|---|
| *Darf ich die Maschine jetzt starten?* | dem **Zustand** `restzeit == 0` — beliebig oft abfragbar |
| *Soll ich jetzt piepen?* | dem **Ereignis** — genau einmal |

Wer nur Zustände hat, piept ununterbrochen. Wer nur Ereignisse hat, kann nach dem Piepen nicht mehr sagen, ob die Maschine frei ist.

**Im Zweifel gilt: Der Zustand ist der Zähler selbst. Das Ereignis ist der Takt, in dem er null wurde.**

### 4. Ein Wert merken, neu rechnen, vergleichen ⭐

Nicht jedes Ereignis hat einen Zähler davor. Manchmal willst du wissen, ob sich etwas geändert hat, das jemand anders ausgerechnet hat:

```python
    def pruefe_tarif(self, salon):
        alter = self.tarif
        self.tarif = salon.tarif_fuer(self.waschgaenge)
        if self.tarif != alter:
            salon.melde(f"{self.name}: neuer Tarif {self.tarif}.")
```

**Drei Zeilen, immer dieselben:** alten Wert in eine lokale Variable, neu berechnen, vergleichen.

> **Wenn du einen Übergang erkennen willst, brauchst du beide Seiten davon. Der alte Wert existiert nach dem Überschreiben nicht mehr — also merk ihn dir vorher.**

*(Die Berechnung selbst fasst du dabei nicht an. Du legst nur zwei Zeilen darum.)*

### 6. `welt.melde()` — ein Ort für alles, was gesagt wird

Deine Zähler melden sich aus dem Inneren von Objekten heraus. Ein Geschütz, das mitten im Tick `print()` aufruft, ist genau die Vermischung, gegen die du in Etappe 7b eine Linie gezogen hast.

**Die kleinstmögliche Lösung ist eine Methode am Salon:**

```python
class Salon:
    def melde(self, text):
        print(text)
```

Das sieht albern aus — eine Methode, die nichts tut außer weiterreichen. **Sie ist es nicht**, und der Grund steht in Etappe 7b: Ab jetzt gibt es **eine** Stelle, an der entschieden wird, wie eine Meldung erscheint. Willst du morgen ein `>` davor, eine Uhrzeit, oder die letzten fünf Meldungen gesammelt statt einzeln — du änderst eine Methode statt dreißig `print`-Aufrufe.

*(In Etappe 17 wird genau daraus die Meldungsliste zwischen den Wellen. Heute ist es ein `print`, und mehr soll es nicht sein.)*

### 7. Der Zähler, der nach oben läuft

Deine Erfahrung steigt seit Etappe 3c und tut nichts. Deine Stufenberechnung steht seit Etappe 9a im Marine. **Beides bleibt, wie es ist** — und trotzdem ist das derselbe Fall wie alles andere heute:

| | Abklingzeit | Erfahrung |
|---|---|---|
| Läuft | nach unten, bis null | nach oben, bis zur Schwelle |
| Der Zustand | „ist bereit" | „ist Stufe 3" |
| Das Ereignis | „wurde gerade bereit" | „ist gerade aufgestiegen" |

**Die Richtung ist egal. Was zählt, ist der Übergang** — und den erkennst du mit den drei Zeilen aus Konzept 4, nicht mit einem Zähler.

⚠️ **Eine Stufe gibt heute nichts.** Keine Skillpunkte, keine besseren Werte, keine freigeschaltete Fähigkeit. Nur eine Meldung. **Das Freischaltraster ist Etappe 18**, und wer es hier vorwegnimmt, baut es zweimal.

---

## Dein Auftrag — Teil 13a

Nach **jedem** Schritt ausführen und einen Tick auslösen. Zähler-Fehler sieht man nur in Bewegung.

---

### 1. Bau `welt.melde()`

- Eine Methode der `Welt` mit einem Parameter `text`.
- Sie gibt ihn aus. Mehr nicht.

**So prüfst du es:** In einer Wegwerf-Datei `welt.melde("Test")` aufrufen.

---

### 2. Leg die Zahlen als feste Werte an

Oben in der Datei, GROSS geschrieben, nach der Verabredung aus Etappe 1:

| Name | Startwert | Wofür |
|---|---|---|
| `ABKLINGZEIT` | `6` | Fähigkeit wieder bereit |
| `RESPAWNZEIT` | `5` | dein eigener Ausfall (13b) |
| `AUSFALLZEIT` | `4` | ein Kamerad (13b) |
| `TURM_BAUZEIT` | `8` | der Basisturm wird fertig (13b) |
| `TURM_KOSTEN` | `100` | Vaporium für den Bauauftrag (13b) |
| `NACHLADEZEIT` | `2` | Kameraden (13b) |
| `MAGAZIN_GROESSE` | `3` | Schüsse pro Magazin (13b) |

⚠️ **Leg alle sieben heute an, auch die für 13b.** Sie an einer Stelle zu sehen ist der halbe Lernstoff dieser Etappe — sechs Zahlen, die alle dasselbe bedeuten: *so viele Ticks*.

**Und widersteh der Versuchung, sie jetzt auszubalancieren.** Die Zahlen oben sind Startwerte, keine Empfehlung. Balancing ist Etappe 21b, und der Deckel aus Etappe 3c gilt weiter: **fünfzehn Minuten, dann Notizliste.**

---

### 3. Gib `Einheit` eine Methode `zaehler_runter(welt)`

- Parameter: `self` und `welt` — wie `update()` aus Etappe 12.
- Körper: ein Docstring, der sagt, warum hier nichts steht.

*(Dieselbe Bauform wie `update()`. Die Basis tut nichts, die Unterklassen überschreiben.)*

**So prüfst du es:** Eine nackte `Einheit` erzeugen und die Methode aufrufen. Kein Fehler, keine Ausgabe.

---

### 4. Bau die Zählerphase in den Tick

Dein Tick aus Etappe 12 bekommt **eine** Phase dazu, an **zweiter** Stelle:

| | Phase |
|---|---|
| 1 | `self.zeit += 1` |
| **2** | **Über `self.trupp` laufen und `zaehler_runter(self)` aufrufen** |
| 3 | Trupp handelt |
| 4 | Gegner handeln |
| 5 | Aufräumen |

⚠️ **Zweite Stelle, nicht letzte — und das ist eine Entscheidung, keine Vorgabe.** So wird eine Fähigkeit in dem Takt wieder bereit, in dem der Zähler abläuft, und nicht erst im nächsten. Stell sie ans Ende, und alles ist einen Takt später fertig. **Trag die neue Phase in deine Reihenfolge-Notiz aus Etappe 12, Schritt 17 ein.**

**So prüfst du es:** Noch passiert nichts — keine Einheit hat einen Zähler. Das Spiel muss trotzdem unverändert laufen.

---

### 5. Gib `Marine` eine Abklingzeit

- Attribut `abklingzeit` mit Startwert `0`, in `__init__`.
- `Marine.zaehler_runter()` überschreibt die geerbte Fassung und zählt sie nach dem Muster aus Konzept 1 herunter.
- Beim Erreichen von null: eine Meldung über `welt.melde()`.

**So prüfst du es:** Setz `abklingzeit` in einer Wegwerf-Datei von Hand auf `3` und tick viermal. **Genau eine** Meldung.

---

### 6. ⭐ Bau `faehigkeit_einsetzen()` um

Deine Methode aus Etappe 11 gibt bisher nur eine Meldung aus. Ab heute:

- Ist `abklingzeit` größer als null: melden, wie lange noch, und **sofort zurück** — ohne dass etwas passiert.
- Sonst: die Meldung der Unterklasse ausgeben und `abklingzeit` auf `ABKLINGZEIT` setzen.
- Die Methode bekommt `welt` als Parameter, damit sie melden kann.

⚠️ **Die Prüfung gehört in die Fassung der Oberklasse `Marine`, nicht in jede der vier Unterklassen.** Sonst schreibst du sie viermal, und beim nächsten Umbau änderst du drei davon. *(Die Unterklassen rufen sie mit `super()` auf — Etappe 11, Konzept 8.)*

⚠️ **Die Methode ändert dabei ihre Signatur** — aus `faehigkeit_einsetzen()` wird `faehigkeit_einsetzen(welt)`. **Such vorher alle Aufrufstellen** und schreib ihre Zahl auf, wie bei jeder Fahndung seit Etappe 5. Es sind wenige; darum geht es nicht. Es geht darum, dass eine geänderte Signatur **immer** alle Aufrufer kostet — der Kostengedanke aus Etappe 5 an einem billigen Beispiel.

⚠️ **Immer noch keine Wirkung, keine Kosten, kein Schaden.** Etappe 18. **Und weiterhin keine Klassenbindung:** Die vier Meldungen aus Etappe 11 bleiben Meldungen. Was der Engineer wirklich kann — Minen, Fallen, ein mobiler Geschützturm —, ist Etappe 18 und hat mit dem Basisturm aus 13b nichts zu tun.

**So prüfst du es:** Fähigkeit einsetzen, sofort noch einmal einsetzen. Beim zweiten Mal kommt die Restzeit-Meldung und **nicht** die Fähigkeitsmeldung. Dann sechsmal einen zeitkostenden Befehl geben: Sie meldet sich von selbst zurück.

---

### 7. ⭐ Leg fest, was eine Zählerzahl genau bedeutet

**Bevor du weiterbaust, und zwar schriftlich.** Setz `ABKLINGZEIT` testweise auf `3` und beantworte in `GELERNT.md`:

- Du setzt die Fähigkeit bei `welt.zeit == 10` ein. **Bei welchem `welt.zeit` ist sie wieder bereit?**
- Schreib den Ablauf für die drei folgenden Ticks einzeln auf: Welchen Wert hat der Zähler nach Tick 11, nach 12, nach 13? In welchem davon kommt die Meldung?

**Dann führ es aus und vergleich.** Stimmt es nicht mit deiner Vorhersage überein, ist nicht zwingend der Code falsch — vielleicht war deine Erwartung eine andere. **Entscheide dich für eine der beiden Bedeutungen und schreib sie auf:**

> `ABKLINGZEIT = 3` heißt entweder *„drei Ticks lang gesperrt"* oder *„beim dritten Tick wieder frei"*. Beides ist vertretbar. Nur eines darf gelten.

⚠️ **Das ist der Auftragsschritt, der sich am wenigsten nach Arbeit anfühlt und am meisten spart.** Jeder Zähler heute — Ausfall, Nachladen, Bauzeit, Räumzeit — benutzt dieselbe Bedeutung. Wer sie einmal festlegt, hat sie fünfmal richtig. Wer sie nicht festlegt, baut fünf Zähler mit drei verschiedenen Bedeutungen und sucht in Etappe 16, welcher der Falsche war.

*(Das ist der Beobachtbarkeitsfaden des Lehrplans in seiner reinsten Form: Nicht daran erkennen, dass es irgendwann feuert — sondern mitzählen und vergleichen.)*

---

### 8. Zeig die Abklingzeit im Status an

Eine Zeile in deiner Statusanzeige: bereit, oder noch so viele Takte.

**Warum das kein Komfort ist:** Ein Zähler, den man nicht sieht, ist beim Fehlersuchen unsichtbar. Du brauchst diese Zeile heute noch, wenn in 13b fünf Zähler gleichzeitig laufen.

---

### 9. ⭐ Mach den Stufenaufstieg zu einem Ereignis

Deine Stufenberechnung aus Etappe 9a bleibt **unverändert**. Du legst nur zwei Zeilen darum, nach Konzept 4:

- Vor der Berechnung die aktuelle Stufe in einer lokalen Variablen merken.
- Nach der Berechnung vergleichen.
- Ist sie gestiegen: `welt.melde()`.

**So prüfst du es:** Setz die Erfahrung von Hand knapp unter eine Schwelle und erleg einen Gegner. Genau eine Aufstiegsmeldung — und beim nächsten Abschuss keine zweite.

---

### 10. Schreib die Invariante auf

In `GELERNT.md`, zwei Zeilen, keine Prüfung — und die beiden tun Verschiedenes:

> **Die Invariante, prüfbar:** Ein Zähler ist nie kleiner als `0`.
>
> **Der Merksatz, nicht prüfbar:** Ein Zähler kann nicht gleichzeitig laufen und abgelaufen sein.

**Der Unterschied ist der Punkt.** Die erste Zeile ist eine Behauptung über eine Zahl — sie ließe sich in einem `assert` hinschreiben, und in Etappe 26 wird genau das daraus. Die zweite ist ein Bild im Kopf, das dir beim Lesen deines eigenen Codes hilft und das keine Maschine prüfen kann.

Formulier zu beiden: Was genau müsste in deinem Code passieren, damit sie brechen? *(Das ist dieselbe Übung wie die drei `assert`-Zeilen aus Etappe 7b. In Etappe 20 wird daraus eine Prüfung, in Etappe 26 ein Test. **Heute wird sie nur hingeschrieben.**)*

---

### 11. Commit

Commit: `Etappe 13a: Die Fähigkeit meldet sich zurück`

> **⏸ Guter Schnitt.** Ein Zähler läuft, und dein Spiel sagt dir von selbst Bescheid. 13b ist viermal dasselbe — und trotzdem ein eigener Abend.

---

# Teil 13b — Ausfall, der Basisturm und die Karte

## Worum es geht

Das Muster steht. Ab hier wird es angewandt, und der Lernstoff verschiebt sich: **Nicht mehr, wie ein Zähler gebaut wird, sondern was derselbe Zähler an verschiedenen Stellen bedeutet.**

Vier Bauarbeiten, alle nach demselben Rezept:

| Wo der Zähler wohnt | Läuft ab | Am Ende passiert |
|---|---|---|
| Bei deinem Marine | `ausfallzeit` | Du stehst wieder da — **mit Restmunition** |
| Bei jedem Kameraden | `ausfallzeit` | Er steht wieder auf, und das Spiel hat nie gewartet |
| Bei jedem Kameraden | `nachladezeit` | Das Magazin ist wieder voll |
| Beim **Basisturm** | `bauzeit` | Er wird fertig und fängt an zu feuern |
| **Bei der Welt** | `raeumzeit` | Der Osttunnel ist frei |

**Die letzte Zeile ist die interessante.** Sie zeigt, dass das Muster nichts mit Einheiten zu tun hat. Der Tunnel gehört keinem Marine — also zählt die Welt.

---

## Die Konzepte — Teil 13b

### 7. Derselbe Zähler, zwei Spielgefühle ⭐

Ein Kamerad fällt. Sein `ausfallzeit` läuft, vier Takte später steht er wieder. **Du hast in der Zwischenzeit weitergespielt** — zu dritt statt zu viert, etwas mühsamer, aber ununterbrochen.

Du fällst. Dein `ausfallzeit` läuft, fünf Takte später stehst du wieder. **Und in der Zwischenzeit wartest du**, weil dein Marine der einzige ist, der auf Befehle hört.

> **Identischer Code, identischer Zähler — und zwei völlig verschiedene Erfahrungen. Der Unterschied liegt nicht in der Technik, sondern darin, wer auf das Objekt angewiesen ist.**

Das ist die Unterscheidung *gesteuert ↔ autonom* aus Etappe 12, zum ersten Mal spürbar statt nur erklärt. Und es ist derselbe Grund, warum der Held **keine eigene Unterklasse** ist: Was ihn unterscheidet, ist ein Attribut, kein Verhalten.

⚠️ **Deshalb entscheidet das Attribut `gesteuert`, welcher Startwert gesetzt wird** — nicht ein Vergleich, welches Objekt der Held ist:

```python
if einheit.gesteuert:
    einheit.ausfallzeit = RESPAWNZEIT
else:
    einheit.ausfallzeit = AUSFALLZEIT
```

*(Die Versuchung, hier `is` zu benutzen und mit dem Helden zu vergleichen, ist groß. Lass es. Das Attribut sagt, was gemeint ist; ein Objektvergleich sagt nur, welches Ding es zufällig ist.)*

### 8. Mit Restmunition zurück — eine Entscheidung, keine Nebensache

Wenn du wieder aufstehst, bekommst du deine Trefferpunkte zurück. **Deinen Vorrat nicht.**

**Das ist eine bewusste Spielentscheidung, und sie ist wichtiger, als sie aussieht.** Wer mit vollem Vorrat zurückkommt, für den ist Fallen ein kostenloses Nachfüllen — und ab einem gewissen Punkt die *beste* verfügbare Handlung. Eine Mechanik, die Scheitern belohnt, zerlegt jedes Ressourcensystem leise von innen.

> **Prüf jede Strafe daraufhin, ob sie versehentlich eine Belohnung ist.** Das ist dieselbe Frage wie beim ungültigen Befehl in Etappe 12 — Unsinn tippen darf kein Zeitstopp sein.

⚠️ **Und der Wert, den du zum Aufstehen brauchst, muss irgendwo stehen.** Um die Trefferpunkte zurückzusetzen, brauchst du den Startwert — und der ist seit Etappe 11 überschrieben, sobald der erste Treffer sitzt. Also merk ihn dir in `__init__` als zweites Attribut. *(Deine Balkenanzeige aus Etappe 3c braucht dasselbe Maximum. Wenn es dort schon steht: eine Zahl, ein Name, kein zweiter.)*

### 9. Der Basisturm — ein Fremdkörper im Trupp ⭐

Der Vorposten bekommt ein Geschütz. **Es ist kein Marine**, und trotzdem kommt es in `welt.trupp`.

Der Satz klingt falsch und ist der Punkt. `trupp` heißt nicht *„Liste der Marines"*, sondern *„was auf meiner Seite steht und tickt"*. Und weil der Turm von `Einheit` erbt, hat er alles, was der Tick von ihm verlangt: `update()`, `zaehler_runter()`, `trefferpunkte`, `status`.

> **Der Tick fragt nie, was etwas ist. Er ruft auf, und das Objekt weiß Bescheid.** Das ist Etappe 11, angewandt auf etwas, das es damals noch nicht gab.

**Zwei Zustände, ein Zähler:**

```
bauzeit > 0   →  im Bau, tut nichts
bauzeit == 0  →  feuert wie ein Kamerad
```

⚠️ **Genau einer, und das ist eine Prämisse, keine Sparmaßnahme.** Dieses Spiel ist ein Hero-Survival: Du bist eine Figur im Gefecht, kein Bauherr über der Karte. **Beliebig viele Geschütze aufstellen zu können, wäre ein anderes Spiel** — und zwar eines, in dem deine eigene Figur schnell nebensächlich wird. Der Turm ist eine Beigabe, keine Mechanik. In Etappe 22 bekommt er dafür **Ausbaustufen**: fünf Zeilen in einer Tabelle, die denselben Turm beschreiben, nicht fünf Türme.

**Und dafür brauchst du keine Typprüfung.** Die Welt merkt sich den Turm unter einem eigenen Namen:

```python
self.turm = None
```

Steht dort `None`, darf gebaut werden. Steht dort ein Objekt, nicht. Das ist `is None` aus Etappe 10 und die zwei Namen für ein Objekt aus Etappe 12, Konzept 4 — der Turm steht in `trupp` **und** unter `turm`.

⚠️ **Verwechsle ihn nicht mit dem Geschützturm des Engineer.** Das sind zwei verschiedene Dinge, und sie gehören in verschiedene Etappen:

| | Der Basisturm — **heute** | Der Geschützturm des Engineer — **Etappe 18** |
|---|---|---|
| Was er ist | ein **Gebäude** im Vorposten | eine **Klassenfähigkeit** |
| Wie er entsteht | in der Werkstatt in Auftrag gegeben, kostet Vaporium | eingesetzt, kostet eine Abklingzeit |
| Wer ihn hat | jeder, unabhängig von der Klassenwahl | nur der Engineer |
| Wie lange | dauerhaft | mobil, vorübergehend |

**Die dritte Zeile ist die wichtige.** Die Klassenwahl aus Etappe 1 bestimmt, *wen du steuerst* — nicht, was im Vorposten verfügbar ist. Ein Turm, den nur der Engineer bauen könnte, würde aus einer Rollenwahl eine Fähigkeitswahl machen. *(Deshalb bleibt deine Fähigkeit aus 13a auch heute eine erfundene mit einer Meldung. Die echten Klassenfähigkeiten sind Etappe 18, und dazu gehört auch der mobile Turm.)*

**🚨 KI-Code-Warnsignal — die Frage, nicht die Lösung:**

Dein Turm bekommt die ganze Welt übergeben, um ein Ziel zu finden. In Etappe 12 stand dazu der Begriff **Kopplung**, und heute fällt er zum zweiten Mal an — bei einem Objekt, das mit fast nichts in der Welt etwas zu tun hat.

> **Stell die Frage ruhig: Warum muss dieses Ding alles kennen, nur um einen Gegner zu finden?**

**Und dann lass sie stehen.** Du reparierst heute nichts. Ab Etappe 13 lernst du nicht mehr Python, um eine Übungsaufgabe zu lösen, sondern weil *dein* Programm ein Problem hat — das ist die stärkste Form des Lernens in diesem Projekt, und sie funktioniert nur, wenn die Frage länger offen bleibt, als bequem ist. In Etappe 15 zeichnest du sie auf, in 23b bekommst du Antworten.

### 10. Die Karte ändert sich zur Laufzeit ⭐

Deine `sektoren` aus Etappe 5 waren bisher **Daten**: einmal hingeschrieben, nur gelesen. Ab heute sind sie **Zustand**.

```python
salon.geraete["trockner"]["stockwerk"] = 2
```

Ein verschachtelter Zugriff, aber diesmal auf der linken Seite des Gleichheitszeichens. Lesend kennst du das seit Etappe 5, Konzept 5. **Schreibend gilt dasselbe:** Erst die äußere Klammer, dann die innere, dann die Zuweisung. Ist der innere Schlüssel schon da, wird er überschrieben; ist er es nicht, entsteht er.

**Und genau daran hängt deine Entscheidung aus Etappe 5.** Der Guide hat damals gesagt, dass wir heute nachschlagen — hol die Notiz heraus:

| Deine Entscheidung damals | Was Freiräumen heute heißt |
|---|---|
| **Der Weg fehlt** (die Empfehlung) | Einen Eintrag **erzeugen**: `sektoren["osttor"]["nachbarn"]["osten"] = "landeplattform"` — eine Zeile |
| **Der Weg ist markiert** | Den Eintrag aus `blockiert` **entfernen** — dafür brauchst du `del` |

**Beide Wege sind richtig, und du hast damals aufgeschrieben, welchen du gegangen bist.** Das ist der ganze Zweck der Notiz: Eine Entscheidung, die vor acht Etappen getroffen wurde, kostet dich heute eine Zeile statt einer halben Stunde Suchen.

**`del` entfernt einen Eintrag aus einem Dictionary:**

```python
del salon.geraete["trockner"]["stockwerk"]
```

Du hast es in Etappe 5 einmal als Gegenbeispiel gesehen — dort ging es darum, dass man ein Dictionary nicht verkleinern darf, **während man darüber läuft**. Hier läufst du nicht darüber, also ist es genau das richtige Werkzeug. ⚠️ **Ein Schlüssel, den es nicht gibt, ergibt einen `KeyError`** — dieselbe Meldung wie beim Lesen.

> **Und die Folge für später, in einem Satz: Was sich zur Laufzeit ändert, muss in Etappe 19 gespeichert werden.** Die Beschreibungen deiner Sektoren nicht — die stehen im Code. Der freigeräumte Tunnel schon.

### 11. Wann räumt man, und wie lange?

Freiräumen ist eine Handlung, die dauert — also ist es auch ein Zähler. Aber er wohnt anders als die anderen:

| | Wo der Zähler wohnt | Warum |
|---|---|---|
| Abklingzeit | am Marine | die Fähigkeit gehört ihm |
| Bauzeit | am Basisturm | er baut sich selbst auf |
| **Räumzeit** | **an der Welt** | der Tunnel gehört niemandem |

**Die Besitzfrage aus Etappe 9 beantwortet das ohne Diskussion:** *Gäbe es diesen Wert pro Figur oder pro Spiel?* Den Tunnel gibt es einmal.

⚠️ **Und der Befehl ist ortsgebunden** — wie `kaufe` nur im Depot seit Etappe 5. Räumen kannst du nur, wo der Schutt liegt. *(In Etappe 14b wird Reichweite dieselbe Art Bedingung: Etwas geht nur, wenn du am richtigen Ort bist.)*

---

## Dein Auftrag — Teil 13b

---

### 12. Merk dir den Startwert der Trefferpunkte

- In `Einheit.__init__` ein zweites Attribut, das die Anfangs-Trefferpunkte festhält.
- Benutzt du in deiner Balkenanzeige aus Etappe 3c schon einen Maximalwert, dann ist das **derselbe** — kein zweiter Name für dieselbe Zahl. *(Die Regel aus Etappe 5, unverändert.)*

**So prüfst du es:** Einen Marine Schaden nehmen lassen. Der Startwert steht noch da.

---

### 13. ⭐ Bau den Ausfall mit Zähler

- `Einheit` bekommt `ausfallzeit` mit Startwert `0`.
- **In der Aufräumphase** deines Ticks: Steht eine Einheit des Trupps auf `"tot"` und ihre `ausfallzeit` ist `0`, setz sie — nach Konzept 7, über `gesteuert`.
- **In `zaehler_runter()`:** Zähler herunter, und bei null zurück auf `"aktiv"`, Trefferpunkte auf den Startwert, Meldung.
- Der Vorrat bleibt unangetastet.

⚠️ **Eine ausgefallene Einheit bleibt im `trupp` stehen.** Sie wird nicht entfernt — sonst hat der Zähler kein Zuhause mehr. Nur Gegner verschwinden aus ihrer Liste.

**So prüfst du es:** Setz deine eigenen Trefferpunkte von Hand auf `1` und lass dich treffen. Fünf Takte später stehst du wieder, mit vollen Trefferpunkten und **derselben** Munition wie vorher.

---

### 14. ⭐ Sorg dafür, dass das Spiel nicht mehr endet, wenn du fällst

Deine Abbruchbedingung aus Etappe 3a prüft `trefferpunkte <= 0` und beendet den Lauf. **Die muss heute weg** — für deinen Marine, nicht für den Kern.

- Solange dein Marine auf `"tot"` steht, wird jeder Befehl abgewiesen: eine Meldung mit der Restzeit.
- **Der Tick läuft trotzdem.** Sonst wartest du unendlich lange, und der Zähler kommt nie an.
- `kern_integritaet` auf `0` beendet das Spiel weiterhin.

⚠️ **Das ist die Stelle, an der man sich einsperrt.** Wer den Befehl abweist *und* den Tick überspringt, hat ein Spiel gebaut, das sich nicht mehr bewegt. Probier es absichtlich aus, bevor du es richtig baust — es ist lehrreicher als die Warnung.

**So prüfst du es:** Fallen, fünfmal irgendetwas tippen, wieder aufstehen. Von den zwei Verlustbedingungen beendet ab heute **nur noch eine** das Spiel — und du kannst sagen, welche und warum.

---

### 15. Gib den Kameraden Munition

Der offene Posten aus Etappe 12, mit demselben Muster:

- `Marine` bekommt `magazin` mit Startwert `MAGAZIN_GROESSE` und `nachladezeit` mit `0`.
- Beim Feuern in `update()`: `magazin` um eins verringern. Bei `0`: `nachladezeit` auf `NACHLADEZEIT` setzen.
- Wer nachlädt oder ein leeres Magazin hat, feuert nicht.
- In `zaehler_runter()`: Zähler herunter, bei null `magazin` wieder voll.

⚠️ **Nur die Kameraden.** Dein Held lädt weiterhin mit dem Befehl aus Etappe 3b nach und bezahlt aus dem `vorrat` — das ist seit Etappe 5 sein Wirtschaftskreislauf, und der wird heute nicht angetastet.

**So prüfst du es:** Eine Welle zusehen. Die Kameraden feuern in Schüben statt ununterbrochen.

---

### 16. Bau die Klasse `Basisturm`

- Erbt von `Einheit`. Eigene Werte für Trefferpunkte und Schaden.
- Attribut `bauzeit` mit Startwert `TURM_BAUZEIT`, gesetzt in `__init__` — er entsteht als Baustelle, nicht als fertiger Turm.
- `zaehler_runter()`: Zähler herunter, bei null eine Meldung.
- `update()`: Solange die Bauzeit läuft, sofort `return`. Danach feuern wie ein Kamerad.

**So prüfst du es:** In einer Wegwerf-Datei erzeugen und `zaehler_runter()` so oft aufrufen, wie deine Antwort aus Schritt 7 es vorhersagt. **Genau eine Meldung, und zwar in genau dem Takt, den du aufgeschrieben hast.** Kommt sie einen Takt früher oder später, hast du entweder den Turm falsch gebaut oder Schritt 7 falsch beantwortet — beide Möglichkeiten sind wertvoll.

---

### 17. ⭐ Bau den Bauauftrag in der Werkstatt

**Hier bekommt die Werkbank aus Etappe 5 endlich ihren Zweck.** Sie war acht Etappen lang ein Möbelstück mit einer Beschreibung; ab heute wird an ihr gearbeitet.

- `welt.turm` mit Startwert `None`.
- Ein Befehl `baue turm`, **nur im Sektor Werkstatt** verfügbar — gebunden wie `kaufe` ans Depot seit Etappe 5.
- Die Prüfkette in derselben Reihenfolge wie beim Kauf in Etappe 5 und beim Freischalten in Etappe 6:

```
Bist du in der Werkstatt?        →  nein: Meldung, Ende
Steht schon ein Turm?            →  ja:   Meldung, Ende
Reicht das Vaporium?             →  nein: Meldung, Ende
── ab hier wird verändert ──
Vaporium abbuchen
Turm erzeugen, in welt.turm legen und an welt.trupp hängen
```

- Fällt der Turm, wird `welt.turm` wieder `None` — und ein neuer darf gebaut werden.

⚠️ **Erst alle Prüfungen, dann verändern.** Das ist die Regel aus Etappe 5, und sie ist hier kein Formalismus: Wer das Vaporium abbucht und danach merkt, dass schon ein Turm steht, hat dem Spieler hundert Vaporium für nichts genommen. **Eine Fehlmeldung darf nie etwas kosten** — derselbe Gedanke wie beim ungültigen Befehl in Etappe 12.

⚠️ **Der Turm gehört keiner Klasse.** Jeder kann ihn bauen, egal welche Klasse du in Etappe 1 gewählt hast. Die Klassenwahl bestimmt, wen du steuerst — nicht, was im Vorposten verfügbar ist.

**So prüfst du es:** `baue turm` im Depot — Meldung, nichts passiert, kein Vaporium weg. Dann in der Werkstatt mit zu wenig Vaporium — Meldung, nichts passiert. Dann mit genug: Der Turm steht als Baustelle. `baue turm` noch einmal — Meldung, **kein zweiter Turm und kein zweites Mal Vaporium.** Und `TURM_BAUZEIT` Takte später feuert er.

---

### 18. ⭐ Bau `welt.raeume_frei()`

- **Hol zuerst deine Notiz aus Etappe 5 heraus**, Entscheidung 1. Sie sagt dir, welchen der beiden Wege aus Konzept 10 du gehst.
- Die Methode ändert die Karte und meldet es.
- Danach ist die Landeplattform über `gehe osten` erreichbar.

**So prüfst du es:** Vor dem Freiräumen `gehe osten` am Osttor — es geht nicht. Danach — es geht. **Und `umsehen` am Osttor zeigt den neuen Ausgang**, ohne dass du die Anzeige angefasst hast. *(Wenn nicht, liest deine Anzeige nicht aus `sektoren`, sondern hat den Text irgendwo doppelt. Das ist ein Fund, kein Ärgernis.)*

---

### 19. Mach das Räumen zu einer Handlung mit Dauer

- `welt.raeumzeit` mit Startwert `0`.
- Ein Befehl `raeume`, **nur am Osttor** verfügbar, setzt ihn auf einen Wert deiner Wahl.
- Die Zählerphase zählt ihn herunter und ruft bei null `raeume_frei()` auf.
- Läuft er schon oder ist der Tunnel schon frei: melden und nichts tun.

**So prüfst du es:** `raeume` tippen, dann anderswo weiterspielen. Der Tunnel öffnet sich, während du etwas anderes tust. **Das ist der zweite Beweis, dass dein Tick trägt** — und diesmal einer, der nichts mit Kampf zu tun hat.

---

### 20. Prüf, dass das Alte noch läuft

Von Hand, ohne `diff` — das Verhalten hat sich absichtlich geändert.

- Kaufen, nachladen, Sektor wechseln, Fähigkeit, Bestiarium: alles wie vorher?
- Sinkt die Kernintegrität noch, wenn ein Gegner ankommt, und beendet `0` das Spiel?
- Feuern deine Kameraden noch, und stimmen ihre Abschusszahlen aus Etappe 12?
- Läuft ein voller Wellendurchgang ohne Absturz?

---

### 21. Aufräumen und Commit

Keine von Hand gesetzten Zähler-Werte mehr im Code, kein `breakpoint()`.

Commit: `Etappe 13b: Ausfall, Nachladen und der Basisturm`

---

## Was NICHT in diese Etappe gehört

**Keine Wirkung für Fähigkeiten.** Sie haben jetzt eine Abklingzeit und weiterhin keinen Effekt. Etappe 18.

**Keine Kosten, keine Voraussetzungen, kein Freischaltraster.** Auch Etappe 18. Eine Stufe gibt heute eine Meldung und sonst nichts.

**Kein zweiter Turm und keine Ausbaustufen.** Genau einer in der Basis — das ist die Prämisse, nicht eine Vereinfachung. Seine fünf Ausbaustufen sind **Etappe 22**, und sie sind eine Tabelle, kein zweiter Turm.

**Kein freies Bauen beliebig vieler Geschütze.** Das wäre ein Tower Defense. Dieses Spiel ist ein Hero-Survival, und der Riegel gilt bis zum Ende des Plans.

**Kein Geschützturm des Engineer.** Der ist eine Klassenfähigkeit und etwas anderes als der Basisturm — Konzept 9, Tabelle. **Etappe 18**, zusammen mit Granatwerfer, Minen und Heilaura.

**Keine Bewegung und keine Reichweitenrechnung für den Turm.** Er feuert auf den Nächsten. Etappe 14b.

**Keine Rekruten und keine Söldner.** Ein Rekrut ist eine **gekaufte Stelle**, die nach ihrem Nachschubzähler neu besetzt wird — etwas anderes als ein ausgefallener Kamerad, der wieder aufsteht. Das ist eine eigene Modellierungsfrage und gehört zu **Etappe 22**, wo die Kauf- und Vertragstabellen entstehen.

**Kein `Faehigkeit`-Objekt und keine gemeinsame Zähler-Basisklasse.** Die Design-Entscheidung ist gefallen; beides lohnt sich erst, wenn ein Zähler mehr kann als herunterzählen.

**Kein `assert` für die Invariante aus Schritt 10.** Aufschreiben, nicht prüfen. Etappe 20.

**Keine Echtzeit.** Ticks. Etappe 28.

**Kein Anschluss des `klassengeraet` aus Etappe 2.** Es bleibt ein String. Die Versuchung ist heute am größten, weil es nach einem Schritt aussieht — es sind fünf.

---

## Selbsttest

**13a**
- [ ] `welt.melde()` existiert, und kein Zähler ruft mehr direkt `print()` auf.
- [ ] Eine Fähigkeit, zweimal hintereinander eingesetzt, löst beim zweiten Mal **nichts** aus.
- [ ] Sie meldet sich **genau einmal** zurück, nicht in jedem folgenden Takt.
- [ ] Die Abklingzeit steht im Status.
- [ ] Ein Stufenaufstieg meldet sich einmal, ein weiterer Abschuss danach nicht.
- [ ] Die Zählerphase steht an zweiter Stelle, und die neue Reihenfolge steht in `GELERNT.md`.
- [ ] **Du kannst sagen, was `ABKLINGZEIT = 3` in deinem Code exakt bedeutet** — und die Meldung kommt in genau dem Takt, den du in Schritt 7 aufgeschrieben hast.
- [ ] Invariante und Merksatz sind beide aufgeschrieben, und du kannst sagen, welcher von beiden prüfbar ist.

**13b**
- [ ] Dein Marine kann fallen, ohne dass das Spiel endet — und steht von selbst wieder auf.
- [ ] Er kommt mit **Restmunition** zurück, nicht mit voller.
- [ ] Während du ausgefallen bist, läuft der Tick weiter. Du kannst dich nicht einsperren.
- [ ] `kern_integritaet` auf `0` beendet das Spiel weiterhin.
- [ ] Ein gefallener Kamerad steht nach seinem Zähler wieder auf, und das Spiel hat nie gewartet.
- [ ] Kameraden feuern in Schüben und laden nach.
- [ ] **Ein Turm mit `TURM_BAUZEIT = 3` feuert nach genau drei Ticks — nicht nach zwei, nicht nach vier.** Du hast mitgezählt, nicht geschätzt.
- [ ] `baue turm` geht nur in der Werkstatt, und zwei Bauaufträge erzeugen **einen** Turm.
- [ ] Ein abgewiesener Bauauftrag kostet **kein** Vaporium.
- [ ] Der Turm lässt sich mit jeder der vier Klassen bauen.
- [ ] Nach `raeume` öffnet sich der Tunnel, während du etwas anderes tust.
- [ ] `umsehen` am Osttor zeigt den neuen Ausgang, ohne dass du die Anzeige angefasst hast.
- [ ] Nirgends fragt der Code, welche Klasse eine Einheit hat.
- [ ] Beide Commits sind gesetzt.

---

## Lernziele

In `GELERNT.md`, ohne nachzuschlagen.

1. **Was ist der Unterschied zwischen „ist fertig" und „wurde gerade fertig" — und warum brauchst du beides?**
2. Welche Zeile im Zähler-Muster macht aus einem Zustand ein Ereignis? Beschreib sie über ihre Einrückung.
3. Warum steht in der ersten Zeile `> 0` und nicht `!= 0`? Was passiert ohne die Prüfung?
4. Was spricht dafür, dass das Objekt selbst zählt — und was dafür, dass die Welt eine Liste von Terminen führt?
5. Warum darf `zaehler_runter()` nur einmal pro Tick laufen?
6. Warum wohnt die Räumzeit an der Welt und die Bauzeit am Turm?
7. Warum kommt dein Marine **nicht** mit vollem Vorrat zurück?
8. Was unterscheidet den Ausfall des Helden vom Ausfall eines Kameraden — technisch und im Spielgefühl?
9. Warum steht der Turm im `trupp`, obwohl er kein Marine ist?
10. **Was unterscheidet den Basisturm vom Geschützturm des Engineer — und warum darf der eine nicht an eine Klasse gebunden sein?**
11. Welche Teile deiner `sektoren` sind ab heute Zustand, und welche sind weiterhin Daten?

**Frage 1 ist die wichtigste.** Alles, was in Etappe 17, 19 und 28 einmalig reagieren soll, hängt daran.

**Frage 11 ist die, die in Etappe 19 Geld wert ist.** Wer sie beantworten kann, weiß dort in fünf Minuten, was in den Spielstand gehört.

---

## Transferaufgabe (15 Minuten)

**Außerhalb des Spiels.** Eine Ampel, kein Vorposten.

1. Klasse `Ampel` mit `phase` (`"rot"`, `"gruen"`, `"gelb"`) und `restzeit`.
2. `tick()`: Restzeit herunterzählen. Bei null zur nächsten Phase wechseln und deren Dauer setzen — rot 8, grün 6, gelb 2.
3. Ruf `tick()` fünfzig Mal auf und druck bei **jedem Phasenwechsel** eine Zeile. Rechne vorher aus, wie viele Wechsel es geben muss.

**Und dann der eigentliche Teil:**

4. **Bau einen Knopf für Fußgänger.** `anfordern()` setzt die Restzeit von Grün auf höchstens 2 herunter — aber nur, wenn gerade Grün ist und nicht schon angefordert wurde.
5. **Sag voraus**, was passiert, wenn du die Bedingung „nicht schon angefordert" weglässt und in jedem Takt drückst. Führ es dann aus.

**Schritt 6 ist der Kern.** Es ist dieselbe Unterscheidung wie in Konzept 2, nur von der anderen Seite: Diesmal ist das *Drücken* das Ereignis, und wer es als Zustand behandelt, hält die Ampel für immer auf Grün mit Restzeit 2.

---

## Kaputtmachen

**Vor jedem Experiment aufschreiben, was passieren wird.** Die ersten vier gehören dazu, die letzten zwei sind Kür.

**1. ⭐⭐ Rück die Meldung eine Ebene nach links.** Nimm die Meldezeile aus dem `if restzeit > 0:`-Block heraus, sodass sie direkt in der Methode steht. Setz eine Abklingzeit und tick zehnmal. **Zähl die Meldungen.** Das ist Konzept 2, an deinem eigenen Code — und es ist ein Typ-3-Fehler, weil nichts abstürzt und das Spiel trotzdem unbrauchbar wird.

**2. ⭐ Nimm die Prüfung `> 0` weg.** Nur noch abziehen, ohne Bedingung. Tick zwanzigmal und sieh dir den Wert an. Was steht dort — und was passiert beim nächsten Fähigkeitseinsatz? **Lies dann die Antwort auf Lernziel 3 noch einmal.**

**3. Setz eine Zähler-Zeit auf `0`.** `TURM_BAUZEIT = 0`. Ist der Turm sofort fertig, oder wird er es nie? **Das hängt davon ab, wie du Konzept 1 gebaut hast** — und beide Antworten sind vertretbar. Welche hast du, und passt sie zu dem, was du in Schritt 7 aufgeschrieben hast?

**4. Sperr dich ein.** Weis bei ausgefallenem Marine jeden Befehl ab **und** überspring den Tick. Tipp dreimal etwas. Kommst du wieder heraus? *(Schritt 14 warnt davor. Mach es trotzdem einmal — eine erlebte Sackgasse merkt man sich besser als eine gelesene.)*

---

Die folgenden zwei sind Kür.

**5. Stell die Zählerphase ans Ende des Ticks.** Hinter das Aufräumen. Setz eine Abklingzeit von `1` und beobachte, wann die Fähigkeit wieder bereit ist. Ein Takt Unterschied — **und in Etappe 16 suchst du genau solche Unterschiede.**

**6. Buch das Vaporium vor der Prüfung ab.** Zieh `TURM_KOSTEN` ab, **bevor** du prüfst, ob schon ein Turm steht. Gib dann zweimal `baue turm`. Wie viel Vaporium hast du für wie viele Türme bezahlt — und hättest du es gemerkt, wenn es nur zehn statt hundert wären?

---

**Experiment 1 und 2 sind das Paar.** Beide sitzen in denselben drei Zeilen, beide stürzen nicht ab, und beide machen das Spiel kaputt — das eine durch Lärm, das andere durch Stille. Wer nur eines macht, hat das Muster halb verstanden.

Alles in `GELERNT.md` und ins Fehlertagebuch aus Etappe 8: **woran du es erkannt hättest.**

---

## Häufige Stolpersteine

| Symptom | Ursache | Wo du suchst |
|---|---|---|
| Die Meldung kommt in jedem Takt | Sie steht außerhalb des `> 0`-Blocks | Konzept 2 — eine Ebene Einrückung |
| Die Fähigkeit wird nie wieder bereit | Der Zähler läuft ins Negative, `== 0` trifft nie | Konzept 1 — die Prüfung `> 0` fehlt |
| Der Zähler sinkt um zwei pro Befehl | `zaehler_runter()` wird zweimal aufgerufen | Steht es im Tick **und** in `update()`? |
| Der Zähler des Helden läuft nie | Er steht in `update()`, und die steigt bei `gesteuert` sofort aus | Schritt 4 — Zähler gehören in die eigene Phase |
| Nach dem Aufstehen ist der Vorrat voll | Der Respawn setzt mehr zurück als die Trefferpunkte | Schritt 13 — nur ein Attribut anfassen |
| `AttributeError: 'Marine' object has no attribute 'ausfallzeit'` | Attribut fehlt in `__init__` oder `super().__init__()` steht nicht zuerst | Etappe 11, Konzept 7 |
| Das Spiel bewegt sich nicht mehr, nachdem du gefallen bist | Befehl abgewiesen **und** Tick übersprungen | Schritt 14 — der Tick läuft immer |
| Zwei Türme stehen da | `welt.turm` wird nicht geprüft oder nicht gesetzt | Schritt 17 — `is None` |
| Der abgewiesene Bauauftrag kostet Vaporium | Abgebucht, bevor geprüft wurde | Schritt 17 — erst alle Prüfungen, dann verändern |
| `baue turm` geht überall | Die Ortsprüfung fehlt | Schritt 17 — gebunden wie `kaufe` ans Depot |
| `KeyError` beim Freiräumen | `del` auf einen Schlüssel, den es nicht gibt | Konzept 10 — welche Variante hast du in Etappe 5 gebaut? |
| `gehe osten` geht auch nach dem Räumen nicht | Die Bewegung liest eine andere Stelle als die, die du geändert hast | Konzept 10 — ein Sektor, eine Wahrheit |
| Der Turm feuert schon im Bau | Der `return` bei laufender Bauzeit fehlt | Schritt 16 — erste Zeile von `update()` |
| Der Turm ist einen Takt zu früh oder zu spät fertig | Zähler-Semantik nicht festgelegt | Schritt 7 — was heißt deine Zahl? |

**Der Debugging-Reflex dieser Etappe: „Wie oft lief das?"**

Etappe 12 fragte *in welchem Tick war das*. Heute kommt die Häufigkeit dazu, und sie ist bei Zählern die entscheidende Frage. Der bedingte Breakpoint aus Etappe 8 beantwortet sie in einem Schritt:

```python
if self.abklingzeit == 1:
    breakpoint()
```

**Hält an in dem Takt, bevor es interessant wird.** Dann `n` drücken und zusehen, wie die Meldung entsteht — oder eben nicht.

---

## Ein Blick nach vorne

**Etappe 14 gibt dem Vorfeld ein Raster.** Aus `entfernung` wird `(x, y)`, und dein Turm bekommt in 14b einen Standort und eine echte Reichweite. Die Kameraden fangen an zu laufen.

**Etappe 15 zeichnet deine Kopplung auf.** Fünf Minuten Papier, nichts wird repariert — und die Frage aus Konzept 9 bekommt zum ersten Mal ein Bild.

**Etappe 16 ist die Bug-Jagd II**, und die Zählerphase ist dort ein Hauptverdächtiger. Ein Zähler, der einen Takt zu früh abläuft, stürzt nie ab.

**Etappe 17 macht aus `welt.melde()` eine Liste.** Die Meldungen sammeln sich während einer Welle und werden am Ende zusammen gezeigt — zusammen mit den Abschusszahlen aus Etappe 12.

**Etappe 18 gibt den Fähigkeiten endlich Wirkung.** Deine Abklingzeit von heute ist einer von drei Teilen: Voraussetzung, Abklingzeit, Wirkung. Dort bekommt jede Klasse ihre echte Fähigkeit — und der Engineer seinen **mobilen** Geschützturm, der mit dem Basisturm von heute nichts zu tun hat. Der Stufenaufstieg zahlt dort Skillpunkte aus.

**Etappe 19 speichert alles Halbfertige.** Jeder Zähler, der gerade läuft, gehört in den Spielstand — sonst steht dein Turm nach dem Laden für immer im Bau. Deine Antwort auf Lernziel 11 ist dort die halbe Arbeit.

**Etappe 22 zieht alle Zahlen aus Schritt 2 in Tabellen** — und gibt dem Turm seine fünf **Ausbaustufen**: derselbe Turm, fünf Zeilen, kein zweiter. Dort entstehen auch die **Rekruten und Söldner**, die eine gekaufte Stelle besetzen statt auszufallen und wieder aufzustehen.

**Etappe 28 macht aus Takten Sekunden.** `TURM_BAUZEIT = 180` sind dann drei Sekunden, ohne dass sich eine Zeile Zähler-Logik ändert.

---

## Abschluss

**In `GELERNT.md`:**

- ⭐⭐ **„Soll das gelten, oder soll das passieren?"** — schreib den Satz auf und ein Beispiel aus deinem Code für jede der beiden Seiten.
- ⭐ Die neue Tick-Reihenfolge mit der Zählerphase.
- Meine Entscheidung: Wo laufen die Zähler, und warum?
- Meine Entscheidung aus Etappe 5 — hat sie sich heute ausgezahlt oder gerächt?
- Die Invariante aus Schritt 10.
- Was hat mich überrascht? *(Kandidaten: dass sich eine Fähigkeit meldet, während man etwas anderes tut · wie anders sich der eigene Ausfall anfühlt als der eines Kameraden · dass dieselben drei Zeilen fünfmal passten.)*
- ⭐ **Was bedeutet eine Zählerzahl in meinem Code?** Die Antwort aus Schritt 7, in einem Satz — sie gilt ab heute für alle fünf Zähler.
- Offener Posten, falls du ihn hast: Was fehlt dem Turm noch, bevor er sich richtig anfühlt?

**Vor dem Commit:** Beide Verlustbedingungen geprüft? Kein direktes `print()` mehr in den Zählern? Keine von Hand gesetzten Testwerte im Code?

---

## Wenn du mehr willst

Erst bei grünem Selbsttest.

**Zähl, wie oft du heute dieselben drei Zeilen geschrieben hast.** Schreib die Stellen untereinander auf und sieh dir an, worin sie sich unterscheiden — es sind zwei Dinge: der Name des Zählers und die Meldung. **Das ist die Vorarbeit für die Entscheidung in Etappe 22**, ob daraus eine gemeinsame Struktur werden soll. Heute nur aufschreiben.

**Gib der Welt eine Methode `zaehler_uebersicht()`**, die alle laufenden Zähler untereinander ausgibt. Fünf Zeilen, und bei der nächsten Fehlersuche siehst du in einem Blick, was gerade tickt.

**Lass den Osttunnel wieder zufallen.** Nach zwanzig Takten verschüttet er erneut. Kein Feature, das bleiben muss — aber es zwingt dich, dieselbe Änderung rückwärts zu schreiben, und dabei merkst du, ob deine Karte wirklich nur eine Wahrheit hat.

**Such in fremdem Spielcode nach `cooldown` oder `timer`.** Du wirst beide Bauarten finden — Zähler im Objekt und Terminlisten. Jetzt kannst du sagen, welche es ist und warum jemand sie gewählt haben könnte.

---

> **Nächste Etappe:** [Etappe 14 — Das Vorfeld](etappe-14-das-vorfeld.md) · aus einer Entfernung wird ein Ort, und dein Trupp fängt an zu laufen
