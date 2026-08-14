# Etappe 7 — Aufräumen

> **Block 1: Fundament** · Etappe 7 von 29 · [← Etappe 6](etappe-06-liste-dict-set-tuple.md) · [Lehrplan](../RPG_Lehrplan.md) · [Etappe 8 →](etappe-08-bug-jagd.md)

**Boot.dev:** Funktionen, Parameter, Rückgabewerte, Scope
**Zeitaufwand:** 5–7 Sitzungen à 20–30 Minuten
**Voraussetzung:** Etappe 6 abgeschlossen, Selbsttest grün

---

## Worum es geht

Diese Etappe baut nichts. Sie baut um.

Deine `spiel.py` ist inzwischen ein paar hundert Zeilen lang, und das meiste davon steckt in einer einzigen `while`-Schleife. Wenn du eine Kleinigkeit an der Bewegung ändern willst, scrollst du. Wenn du wissen willst, was `nimm` eigentlich tut, scrollst du. Und irgendwo dazwischen steht eine `elif`-Kette, die seit Etappe 3 wächst.

**Das war Absicht.** In Etappe 3 stand: *Heute darf die Kette lang sein. Sie zu spüren ist der Grund, warum du in Etappe 7 verstehst, wozu die Werkzeuge gut sind.* In Etappe 5 stand: *Die Befehls-Kette stirbt erst in Etappe 7.* In Etappe 6 stand: *Du sollst Funktionen nicht lernen, weil ein Lehrbuch sagt, dass sie wichtig sind, sondern weil dein eigener Code ein Problem bekommen hat.*

Heute ist das Problem groß genug. Sieben Guides haben auf diesen Tag verwiesen — mehr als auf jede andere Etappe des Blocks.

**Und dabei lernst du zwei Dinge, die verschieden sind:**

Das eine ist **Syntax**: `def`, Parameter, `return`, Scope. Das ist an einem Nachmittag gelernt.

Das andere ist **Refactoring** — bestehenden, funktionierenden Code umbauen, ohne sein Verhalten zu ändern. Das ist ungefähr die Hälfte dessen, was Softwareentwickler den ganzen Tag tun, es wird in kaum einem Kurs geübt, und beim ersten Mal fühlt es sich falsch an. *Es lief doch.*

Genau deshalb steht es hier. Wenn du das erste Mal etwas umbaust, das funktioniert, brauchst du eine Methode — sonst baust du hinterher stundenlang Fehler zurück, die du selbst hineingetragen hast. Diese Methode ist der eigentliche Inhalt der Etappe.

---

## Der lange Bogen

| Was du heute baust | Wo es wieder auftaucht |
|---|---|
| Funktionen als Bausteine | **Etappe 9** — dieselben Funktionen werden zu Methoden einer Klasse |
| Zustand als Parameter übergeben | **Etappe 9** — der Schmerz daraus ist die Begründung für `self` |
| `return` statt `print` in der Logik | **Etappe 27** — nur so lässt sich dieselbe Logik grafisch anzeigen |
| „Was muss immer gelten?" | **Etappe 26** — dieselben Fragen, dann als `pytest` |
| `berechne_schaden()` | **Etappe 21** — wird zur echten Kampfformel mit Waffe und Rüstung |
| Der Verhaltens-Beweis vor dem Umbau | **Etappe 27** — derselbe Beweis, wenn Pygame dazukommt |
| Standardwerte für Parameter | **Etappe 10** — dort lauert die berühmteste Falle dabei |
| Mehrere Rückgabewerte als Tuple | **Etappe 21** — Schaden und Treffermeldung in einem |
| Eine Funktion, ein Zweck | **Etappe 24** — dasselbe Prinzip eine Ebene höher, bei Modulen |
| Docstrings | **Etappe 23** — bekommen dort mit Typannotationen Gesellschaft |

**Fünf Schulden werden heute eingelöst:**

Aus **Etappe 2** die Normalisierung mit `.lower()` und `.strip()`, aus **Etappe 4** das `.split()` — beide wandern dorthin, wo sie hingehören: in `verarbeite_befehl()`.

Aus **Etappe 3** die Befehlsverarbeitung, die seit fünf Etappen in der Hauptschleife wohnt. Aus **Etappe 5** die `elif`-Kette, die dort ausdrücklich für heute vertagt wurde.

Und aus **Etappe 4** die unangenehmste: die *versteckten Annahmen*. Du solltest damals in `GELERNT.md` schreiben, was deine Befehlsverarbeitung stillschweigend voraussetzt. Beim Zerlegen in Funktionen werden diese Annahmen sichtbar — weil du für jede Funktion sagen musst, was sie bekommt und was sie zurückgibt.

---

## Eine Design-Entscheidung, die du jetzt treffen solltest

### Frage 1: Wer gibt aus — die Funktion oder ihr Aufrufer?

Das ist die folgenreichste Entscheidung, die du in diesem ganzen Block triffst. Sie sieht harmlos aus.

```python
# Variante A — die Funktion druckt selbst
def zeige_ort(orte, ort):
    print(orte[ort]["beschreibung"])

# Variante B — die Funktion liefert Text, der Aufrufer druckt
def beschreibe_ort(orte, ort):
    return orte[ort]["beschreibung"]

print(beschreibe_ort(orte, aktueller_ort))
```

**A ist bequemer.** Ein Aufruf, fertig, keine zweite Zeile.

**B ist wiederverwendbar.** Der Text lässt sich in eine Datei schreiben, in einem Test prüfen, an anderer Stelle einbauen — oder, in Etappe 27, in ein Pygame-Fenster zeichnen statt ins Terminal.

**Und hier ist der Punkt, an dem es ernst wird.** Im Lehrplan steht bei Etappe 27: *Deine gesamte Logik bleibt unverändert. Wenn du sauber gearbeitet hast, fasst du `world.py` fast nicht an.* Dieses Versprechen hängt an genau dieser Entscheidung. Eine Funktion, die `print()` aufruft, kann in einem Grafikfenster nichts anzeigen. Sie müsste umgeschrieben werden — jede einzelne.

**Meine Empfehlung, und sie ist ein Kompromiss:** Trenne nach Art der Funktion.

- Funktionen, die **etwas berechnen oder entscheiden** (`berechne_schaden`, `finde_ausgang`, `kann_aufnehmen`) → immer `return`, niemals `print`.
- Funktionen, deren **einziger Zweck die Darstellung** ist (`zeige_inventar`) → dürfen drucken.

So bleibt der Kern deiner Logik austauschbar, und du erstickst nicht an Rückgabewerten für jede Kleinigkeit. In Etappe 24 wirst du merken, dass diese Trennung auch bestimmt, welche Datei was enthält.

### Frage 2: Wie schneidest du zu?

Zwei vertretbare Wege, deine Befehle in Funktionen zu zerlegen:

*Nach Befehl* — `befehl_nimm()`, `befehl_gehe()`, `befehl_umsehen()`. Man findet alles sofort, und jeder Befehl ist ein Ort.

*Nach Thema* — `inventar_hinzufuegen()`, `bewege_spieler()`, `beschreibe_ort()`. Näher an dem, was in Etappe 9 zu Klassen wird, weil Thema und Objekt oft dasselbe sind.

**Empfehlung: nach Thema**, mit `verarbeite_befehl()` als Verteiler davor. Deine `Player`- und `Item`-Klassen aus Etappe 9 und 11 entstehen dann fast von selbst aus den Themen. Aber wenn dir der andere Schnitt einleuchtender ist, nimm ihn — und schreib die Begründung in `GELERNT.md`, damit du in Etappe 9 weißt, warum du es so gemacht hast.

---

## Die Konzepte

### 1. Eine Funktion definieren und aufrufen

```python
def begruesse(name):
    print(f"Willkommen, {name}.")

begruesse("Mara")
```

`def`, der Name, Klammern mit Parametern, Doppelpunkt — und darunter der eingerückte Block. Aufbau wie bei `if` und `while` aus den Etappen 2 und 3.

**Zwei Dinge, die getrennt sind und oft verwechselt werden:** Die Definition sagt nur, *was passieren würde*. Erst der Aufruf lässt es passieren. Eine Datei kann voller Funktionsdefinitionen sein und beim Ausführen gar nichts tun.

**Die Klammern beim Aufruf sind nicht optional:**

```python
begruesse          # das ist die Funktion selbst
begruesse("Mara")  # das ruft sie auf
```

Die erste Zeile stürzt nicht ab, tut aber auch nichts. Fehler vom Typ 3 — er steht unten in den Experimenten, weil du ihn produzieren wirst.

### 2. Parameter und Argument

Zwei Wörter für zwei Seiten derselben Sache:

```python
def begruesse(name):     # "name" ist ein PARAMETER
    ...

begruesse("Mara")        # "Mara" ist ein ARGUMENT
```

Der **Parameter** steht in der Definition — ein Platzhalter, den du selbst benennst. Das **Argument** ist der konkrete Wert beim Aufruf.

Es ist kein Zufall, dass beides verschiedene Namen hat: Der Parameter gehört der Funktion, das Argument dem Aufrufer. Eine Funktion soll funktionieren, ohne zu wissen, wer sie ruft.

**Mehrere Parameter werden der Reihe nach zugeordnet:**

```python
def berechne_schaden(angriff, ruestung):
    return angriff - ruestung

berechne_schaden(10, 3)     # angriff=10, ruestung=3
berechne_schaden(3, 10)     # vertauscht — kein Fehler, falsches Ergebnis
```

Die zweite Zeile ist wieder Typ 3: kein Absturz, nur Unsinn. Wenn du sicher gehen willst, kannst du beim Aufruf benennen:

```python
berechne_schaden(ruestung=3, angriff=10)     # Reihenfolge egal
```

Das ist bei zwei Parametern übertrieben. Ab vier lohnt es sich, und in fremdem Code wirst du es ständig sehen.

### 3. `return` gegen `print` — der wichtigste Unterschied dieser Etappe

Beide bringen etwas aus einer Funktion heraus. Nur eines davon ist brauchbar.

```python
def addiere_druckend(a, b):
    print(a + b)

def addiere_rueckgebend(a, b):
    return a + b

ergebnis = addiere_druckend(2, 3)      # zeigt 5 an, ergebnis ist None
ergebnis = addiere_rueckgebend(2, 3)   # zeigt nichts, ergebnis ist 5
```

`print()` schickt etwas auf den Bildschirm — und weg ist es. Kein Programmteil kann damit weiterarbeiten.
`return` gibt einen Wert an den Aufrufer zurück, der ihn speichern, weiterreichen oder prüfen kann.

**Die Merkregel:** `print` redet mit dem Menschen. `return` redet mit dem Rest deines Programms.

**Und noch etwas:** `return` beendet die Funktion sofort. Alles danach läuft nicht mehr:

```python
def pruefe(zahl):
    if zahl < 0:
        return "negativ"
    return "positiv oder null"      # wird nur erreicht, wenn oben nicht returnt wurde
```

Das ist praktisch — man kann früh aussteigen, statt alles in verschachtelte `else` zu packen.

### 4. Ohne `return` kommt `None` zurück

```python
def zeige_inventar(inventar):
    for g in inventar:
        print(g)

x = zeige_inventar(["brot"])
print(x)      # None
```

Jede Funktion gibt etwas zurück. Wenn du nichts angibst, ist es `None` — das „hier ist bewusst nichts", das dir in Etappe 10 wieder begegnet.

**Erinnerst du dich an Etappe 4?** Dort war `inventar = inventar.append("lampe")` ein Klassiker, weil `append()` nichts zurückgibt. Genau derselbe Mechanismus, jetzt in deinen eigenen Funktionen. Ab heute kannst du diesen Fehler auch selbst bauen.

### 5. Scope — was die Funktion sieht und was nicht

```python
zaehler = 0

def erhoehe():
    zaehler = zaehler + 1       # UnboundLocalError

erhoehe()
```

Eine Funktion hat ihren eigenen Raum. Variablen, die du darin anlegst, existieren nur während des Aufrufs und sind danach weg. Das heißt **lokaler Scope**.

Von außen lesen kann eine Funktion oft:

```python
name = "Mara"

def gruesse():
    print(name)      # funktioniert
```

Aber **zuweisen** macht die Variable automatisch lokal — und dann ist die äußere unerreichbar, auch beim Lesen. Das ist die Ursache des `UnboundLocalError` oben, und die Fehlermeldung ist eine der verwirrendsten in Python. Merk dir das Muster: Wenn irgendwo in der Funktion eine Zuweisung an den Namen steht, ist er in der *ganzen* Funktion lokal.

**Warum das eine gute Eigenschaft ist:** Zwei Funktionen können beide eine Variable `i` benutzen, ohne sich zu stören. Ohne Scope müsstest du dir bei jedem neuen Namen überlegen, ob er woanders schon vergeben ist.

### 6. `global` — geht, und trotzdem nicht

Es gibt ein Schlüsselwort, das den Scope aufhebt:

```python
def erhoehe():
    global zaehler
    zaehler += 1
```

Das funktioniert. Und du solltest es in diesem Projekt nicht benutzen.

**Der Grund ist praktisch, nicht dogmatisch:** Eine Funktion mit `global` verändert etwas außerhalb, ohne dass man es am Aufruf sieht. `erhoehe()` sieht harmlos aus — was danach kaputt ist, findest du nur, indem du die Funktion liest. Bei drei Funktionen geht das. Bei fünfzehn suchst du eine Stunde.

Nimm stattdessen Parameter und `return`:

```python
def erhoehe(zaehler):
    return zaehler + 1

runden = erhoehe(runden)
```

Jetzt steht am Aufruf, dass sich `runden` ändert. **Es gibt eine legitime Ausnahme:** Konstanten wie `RICHTUNGEN` aus Etappe 6, die nur gelesen werden. Die dürfen oben stehen und überall sichtbar sein — sie ändern sich ja nie.

### 7. Zustand übergeben — und der Schmerz, der daraus entsteht

Jetzt kommt der Punkt, an dem diese Etappe über sich hinauszeigt.

Deine Funktionen brauchen Daten. Also übergibst du sie:

```python
def zeige_ort(orte, aktueller_ort, besuchte_orte):
    ...

def nimm_gegenstand(orte, aktueller_ort, inventar, gesehene):
    ...

def verarbeite_befehl(befehl, orte, aktueller_ort, inventar, besuchte_orte, gesehene, runden, laeuft):
    ...
```

Die letzte Zeile ist keine Übertreibung. Genau dort landest du heute, und es wird sich falsch anfühlen. **Das ist richtig so — es *ist* falsch.**

Aber es ist nicht dein Fehler. Du hast einen Haufen zusammengehöriger Daten, und die einzige Möglichkeit, sie durchzureichen, ist eine immer längere Parameterliste. Was fehlt, ist ein Behälter, der sie zusammenhält.

**Genau deshalb gibt es Etappe 9.** Dort wird aus diesen sieben Parametern ein Objekt, und der Aufruf sieht so aus:

```python
def verarbeite_befehl(self, befehl):
```

`self` ist der Behälter. Alle Daten hängen daran. **Wenn du heute den Schmerz nicht spürst, wirkt `self` in Etappe 9 wie eine willkürliche Python-Regel, die man eben schreiben muss.** Wenn du ihn spürst, wirkt es wie eine Erlösung.

Also: Reich die Parameter durch, auch wenn es lang wird. Zähl nach, wie viele es bei deiner größten Funktion sind, und schreib die Zahl in `GELERNT.md`. In Etappe 9 schaust du nach.

### 8. Abhängigkeiten sichtbar machen

Das ist der Gedanke hinter Konzept 5 bis 7, und er verdient einen eigenen Namen. Vergleich die beiden:

```python
def zeige_ort():                                    # A
    print(orte[aktueller_ort]["beschreibung"])

def zeige_ort(orte, ort):                           # B
    print(orte[ort]["beschreibung"])
```

**A funktioniert** — solange irgendwo im Programm zufällig zwei Variablen mit genau diesen Namen existieren. Du erfährst das erst, wenn es kracht.

**B sagt, was sie braucht.** Der Kopf der Funktion ist ein Vertrag: *Gib mir eine Ortstabelle und einen Ortsnamen, dann zeige ich ihn dir an.* Was nicht in den Klammern steht, braucht sie nicht.

> **Die Kernidee des Refactorings ist nicht „kürzer", sondern: Abhängigkeiten sichtbar machen.**

Und das hat drei praktische Folgen, die du heute selbst merkst:

- Du kannst die Funktion **einzeln aufrufen und testen**, ohne das ganze Spiel zu starten.
- Du kannst sie **verschieben**, ohne dass sie kaputtgeht — das brauchst du in Etappe 24.
- Beim Lesen weißt du sofort, **was sie anfassen kann** und was nicht.

Der Preis dafür ist die lange Parameterliste aus dem nächsten Konzept. Das ist ein guter Tausch — bis er es nicht mehr ist, und dann kommt Etappe 9.

### 9. Mehrere Werte zurückgeben

```python
def bewege(orte, ort, richtung):
    if richtung not in orte[ort]["ausgaenge"]:
        return ort, "Da ist kein Weg."
    ziel = orte[ort]["ausgaenge"][richtung]
    return ziel, f"Du gehst nach {richtung}."

aktueller_ort, meldung = bewege(orte, aktueller_ort, "norden")
print(meldung)
```

Das Komma hinter `return` macht daraus ein **Tuple** — dasselbe, das du in Etappe 6 gelernt hast. Und links vom `=` packst du es wieder aus, genau wie beim Unpacking damals.

Dieses Muster — *neuer Zustand plus Meldung* — ist außerordentlich nützlich. Die Funktion entscheidet, was passiert und was der Spieler liest; wer sie aufruft, entscheidet, wohin der Text geht. Das ist Variante B aus der Design-Entscheidung in ihrer praktischsten Form, und in Etappe 21 gibt `berechne_schaden()` genauso Schaden und Trefferbeschreibung zurück.

**Zurückhalten solltest du dich ab drei Rückgabewerten.** Dann fehlt wieder ein Behälter — und das ist erneut ein Fingerzeig auf Etappe 9.

### 10. Standardwerte

```python
def zeige_ort(orte, ort, ausfuehrlich=False):
    ...

zeige_ort(orte, "wiese")                     # ausfuehrlich ist False
zeige_ort(orte, "wiese", ausfuehrlich=True)
```

Parameter mit Standardwert dürfen beim Aufruf weggelassen werden. Sie müssen nach den normalen Parametern stehen.

Das passt perfekt zu deiner ersten-Besuch-Logik aus Etappe 6.

> ⚠️ **Eine Warnung, die du heute nur zur Kenntnis nimmst:** Benutz als Standardwert **niemals** eine Liste, ein Dictionary oder ein Set — also `def f(x=[])`. Das verhält sich anders, als jeder erwartet, und ist einer der berühmtesten Python-Stolpersteine überhaupt.
>
> Warum, verstehst du in Etappe 10 — dort baust du den Fehler absichtlich nach, und die Erklärung hängt an dem mutable/immutable aus Etappe 4. Heute reicht die Regel: **Standardwerte nur mit Zahlen, Strings, `True`/`False` oder `None`.**

### 11. Docstrings

```python
def berechne_schaden(angriff, ruestung):
    """Gibt den tatsächlichen Schaden zurück, nie kleiner als 0."""
    return max(0, angriff - ruestung)
```

Ein String direkt unter der `def`-Zeile ist ein **Docstring**. Er ist kein Kommentar, sondern gehört zur Funktion — `help(berechne_schaden)` zeigt ihn an.

**Schreib einen Satz, und schreib den richtigen.** Nicht *was* die Funktion tut (das steht drunter), sondern was sie **zusichert**: was reingeht, was rauskommt, was garantiert gilt. Der Docstring oben verspricht, dass der Schaden nie negativ wird — und genau solche Zusicherungen prüfst du in Etappe 26 mit `pytest`.

### 12. Eine Funktion, ein Zweck

Die einzige Faustregel für den Zuschnitt, die wirklich trägt:

> **Wenn du zur Beschreibung deiner Funktion „und" brauchst, sind es zwei.**

*„Bewegt den Spieler und zeigt den neuen Ort und fügt ihn zu den besuchten hinzu"* — das sind drei.

Zwei praktische Nebenregeln: Wenn eine Funktion nicht auf einen Bildschirm passt, ist sie zu groß. Und wenn du keinen guten Namen findest, tut sie meistens zu viel — das schlechte Namensgefühl ist ein zuverlässigeres Warnsignal als jede Zeilenzahl.

In Etappe 24 begegnet dir dasselbe Prinzip eine Ebene höher: eine Datei, ein Thema.

### 13. Mehr Funktionen sind nicht besser

Der häufigste Fehler nach dieser Etappe ist nicht, zu wenige Funktionen zu bauen. Es ist, zu viele zu bauen.

```python
def drucke_dorfplatz_text():
    print("Der Brunnen steht trocken.")
```

Das ist keine Abstraktion, sondern ein Umweg mit Namen. Die Funktion tut genau eine Sache, wird an genau einer Stelle gerufen und macht den Code länger statt klarer.

> Die Frage ist nicht „kann man das auslagern?" — sondern: **„Verdient diese zusammengehörige Aufgabe einen eigenen Namen?"**

Ein guter Prüfstein: Wenn dir kein Name einfällt, der besser ist als eine Beschreibung des Codeinhalts, brauchst du keine Funktion. `drucke_dorfplatz_text` sagt nichts, was der `print()` darunter nicht schon sagt. `bewege_spieler` dagegen fasst eine Entscheidung zusammen, die man sonst erklären müsste.

**Und ein zweiter Punkt, damit du nicht zu weit gehst:** Deine Hauptschleife aus Etappe 3 bleibt. Sie soll schrumpfen, nicht verschwinden. Sie ist seit fünf Etappen das Herz deines Spiels, und in Etappe 12 wird jeder ihrer Durchläufe zu einem Tick der Welt. Wer sie heute wegrefactort, muss sie dort neu bauen.

### 14. Refactoring — die Methode

Und jetzt der eigentliche Inhalt der Etappe.

**Refactoring heißt: Struktur ändern, Verhalten nicht.** Nach dem Umbau muss dein Spiel sich exakt so verhalten wie vorher. Nicht ähnlich — exakt.

Das Problem: Woher weißt du das? Nach vierzig Umbauzeilen und drei Tagen kannst du dich nicht mehr erinnern, wie es vorher war.

**Deshalb machst du vorher einen Verhaltens-Beweis.** Bevor du irgendetwas anfasst:

1. Schreib eine Befehlsfolge auf, die dein Spiel gründlich durchgeht — fünfzehn bis zwanzig Zeilen. `umsehen`, `gehe norden`, `nimm brot`, `inventar`, `gehe banane`, `nimm`, `karte`, `beenden` und was du sonst hast. **Gerade die Fälle, die schiefgehen, gehören dazu.**
2. Spiel sie durch und speicher die komplette Ausgabe in einer Datei.
3. Bau um.
4. Spiel dieselbe Folge nochmal durch und vergleiche.

Unter Linux und macOS geht das direkt:

```bash
python spiel.py < befehle.txt > vorher.txt
# ... umbauen ...
python spiel.py < befehle.txt > nachher.txt
diff vorher.txt nachher.txt
```

Unter Windows in der PowerShell entsprechend mit `Get-Content` und `Compare-Object`. Und wenn dir das zu viel ist: Ausgabe in eine Textdatei kopieren und von Hand vergleichen. Der Punkt ist nicht das Werkzeug, sondern dass du **eine Wahrheit von vorher hast**.

**Das ist keine Schulübung, sondern gängige Praxis.** So etwas heißt in der Softwareentwicklung ein *Charakterisierungstest*: Man friert das aktuelle Verhalten ein, damit man es beim Umbau nicht verliert. Und es ist der direkte Vorläufer von Etappe 26 — dort schreibst du dasselbe als `pytest`, nur automatisch.

**Die zweite Regel: in kleinen Schritten.** Eine Funktion herauslösen, ausführen, prüfen. Nicht fünf auf einmal. Wenn nach einem Schritt etwas kaputt ist, weißt du genau, wo — nach fünf suchst du.

---

## Dein Auftrag

**Schritt 1 — Der Verhaltens-Beweis**
Bevor du irgendetwas umbaust: Befehlsfolge aufschreiben, durchspielen, Ausgabe sichern. Fünfzehn bis zwanzig Befehle, Fehlerfälle eingeschlossen.

Das ist der wichtigste Schritt der Etappe, und es ist verlockend, ihn zu überspringen. Tu es nicht — ohne ihn kannst du am Ende nicht wissen, ob dein Umbau geglückt ist.

**Schritt 2 — Die erste Funktion**
Nur eine: die Ortsbeschreibung. Herauslösen, Parameter überlegen, aufrufen. Dann ausführen und die Ausgabe vergleichen.

Wenn das stimmt, hast du das Verfahren einmal komplett durchlaufen. Alles Weitere ist Wiederholung.

**Schritt 3 — Die Anzeigefunktionen**
Inventar und Karte. Beide dürfen drucken — es sind reine Darstellungsfunktionen. Nach jeder einzeln prüfen.

**Schritt 4 — Die Bewegung**
`bewege_spieler()` oder wie du sie nennst. Diese Funktion **entscheidet** etwas, also gibt sie zurück statt zu drucken: den neuen Ort und eine Meldung.

Das ist deine erste Funktion mit zwei Rückgabewerten. Achte darauf, dass sie auch den Fehlerfall zurückgibt — „Da ist kein Weg" ist ein Ergebnis, kein Ausnahmezustand.

**Schritt 5 — Das Inventar**
Aufnehmen und Ablegen. Auch hier: Die Funktion entscheidet, ob es geht (liegt es hier? ist Platz? ist es tragbar?), und gibt das Ergebnis zurück.

Hier merkst du zum ersten Mal, wie viele Daten eine einzige Funktion braucht. Das ist der Schmerz aus Konzept 7. Nicht ausweichen, nicht mit `global` abkürzen.

**Schritt 6 — `verarbeite_befehl()`**
Die große. Sie bekommt die Eingabe, normalisiert sie (`.lower()`, `.strip()`, `.split()` aus Etappe 2 und 4 wandern hierher) und ruft die passende Funktion auf.

**Und hier wird eine alte Schuld sichtbar.** In Etappe 4 solltest du aufschreiben: *„Meine Befehlsverarbeitung nimmt momentan an, dass …"* Lies den Satz jetzt nach. Beim Herauslösen musst du für jeden Fall entscheiden, was passiert — und dabei fallen die Annahmen auf, die bisher nur zufällig gehalten haben.

Was du **nicht** musst: alle auflösen. Das ist Etappe 20. Sichtbar machen reicht.

**Schritt 7 — Die Hauptschleife schrumpft**
Wenn alles gewandert ist, sollte von deiner `while`-Schleife wenig übrig sein: Eingabe holen, `verarbeite_befehl()` rufen, Zähler erhöhen, Abbruchbedingung prüfen. Ein Dutzend Zeilen.

Schau dir diesen Moment an. Deine Datei ist genauso lang wie vorher, aber du kannst sie zum ersten Mal überfliegen und verstehen, was passiert.

**Schritt 7b — Zähl die gelöschten Zeilen**
Nach dem Commit sagt dir `git show --stat` , wie viele Zeilen dazugekommen und wie viele verschwunden sind. Schreib beide Zahlen auf.

Wenn mehr verschwunden als dazugekommen sind, hast du heute etwas geschafft, das den meisten schwerfällt. **Anfänger löschen ungern Code, der funktioniert hat** — er fühlt sich wie Besitz an, und ihn wegzuwerfen wie Verschwendung. Er ist keine. Jede Zeile, die es nicht mehr gibt, kann nicht mehr kaputtgehen, muss nicht mehr gelesen und nie wieder verstanden werden.

Das ist keine Motivationsfloskel: In der Praxis gehört „diese dreißig Zeilen brauchen wir nicht" zu den wertvollsten Beiträgen, die jemand zu einem Projekt leisten kann.

**Schritt 8 — Der Beweis**
Befehlsfolge aus Schritt 1 nochmal durchspielen, Ausgaben vergleichen. **Jeder Unterschied ist ein Fehler, den du selbst eingebaut hast** — auch ein fehlendes Leerzeichen.

Wenn etwas abweicht, such es jetzt. Ein Refactoring, das das Verhalten verändert hat, ist kein Refactoring, sondern ein unbemerkter Umbau.

**Schritt 9 — Die Zählung**
Zähl die Parameter deiner größten Funktion. Schreib die Zahl in `GELERNT.md`. In Etappe 9 kommst du darauf zurück.

---

## Was NICHT in diese Etappe gehört

- ❌ Klassen und Objekte → **Etappe 9**
- ❌ Ein Dictionary, das Befehle auf Funktionen abbildet → **Etappe 25**
- ❌ Mehrere Dateien / Module → **Etappe 24**
- ❌ `try` / `except` in den Funktionen → **Etappe 20**
- ❌ `pytest` → **Etappe 26**
- ❌ Typannotationen (`def f(x: str) -> bool`) → **Etappe 23**
- ❌ `global` — heute und später nicht
- ❌ Neue Spielfunktionen jeder Art

**Der letzte Punkt ist der schwerste.** Beim Umbauen wirst du zwanzig Ideen haben, was man jetzt leicht ergänzen könnte. Schreib sie auf, bau sie nicht ein. **Refactoring und neue Funktionen mischt man nicht** — sonst weißt du bei einem Fehler nicht, ob der Umbau oder die Neuerung schuld ist. Das ist eine Regel, an die sich auch Berufsentwickler halten, und sie hat genau diesen Grund.

**Und das Befehls-Dictionary** wird verlockend sein, sobald `verarbeite_befehl()` selbst zur `elif`-Kette wird. Das ist eine gute Beobachtung — aber diese Kette ist kurz, gut sichtbar und stört nicht. Sie stirbt in Etappe 25, wenn Befehle zu Daten werden.

---

## Selbsttest

- [ ] Der Verhaltens-Beweis existiert als Datei, angelegt **vor** dem Umbau
- [ ] Die Ausgabe nach dem Umbau ist mit der davor identisch — auch bei Fehleingaben
- [ ] Die Hauptschleife ist unter zwanzig Zeilen lang
- [ ] Es gibt mindestens fünf Funktionen
- [ ] Jede Funktion lässt sich in einem Satz ohne „und" beschreiben
- [ ] Keine Funktion ist länger als ein Bildschirm
- [ ] Funktionen, die etwas entscheiden, benutzen `return` statt `print`
- [ ] Mindestens eine Funktion gibt zwei Werte zurück
- [ ] `.lower()`, `.strip()` und `.split()` stehen an genau einer Stelle
- [ ] Nirgends steht `global`
- [ ] Kein Standardwert ist eine Liste, ein Dictionary oder ein Set
- [ ] Mindestens drei Funktionen haben einen Docstring
- [ ] Du hast keine einzige neue Spielfunktion eingebaut
- [ ] Es gibt keine Funktion, die an nur einer Stelle gerufen wird und nur ein `print()` enthält
- [ ] Die Hauptschleife existiert noch — sie ist geschrumpft, nicht verschwunden
- [ ] Die Parameterzahl deiner größten Funktion steht in `GELERNT.md`

---

## Lernziele

Ohne Nachschlagen, in eigenen Worten:

1. **Unterschied `return` ↔ `print`?** Was kann man mit dem einen tun, was mit dem anderen nicht?
2. **Was ist Scope — warum kennt eine Funktion deine äußeren Variablen nicht immer?** Warum ist Lesen oft möglich und Zuweisen nicht?
3. **Was passiert, wenn eine Funktion kein `return` hat?** Was steht dann in `x = meine_funktion()`?
4. **Unterschied Parameter ↔ Argument?**
5. **Was macht `return` außer einen Wert zurückzugeben?**
6. **Warum ist `global` erlaubt und trotzdem eine schlechte Idee?** Nenn den praktischen Grund, nicht „das macht man nicht".
7. **Was ist Refactoring — und woran erkennst du, dass es geglückt ist?**
8. **Warum darf man Refactoring und neue Funktionen nicht mischen?**
9. **Was passiert bei `zeige_ort` ohne Klammern?** Warum kommt keine Fehlermeldung?
10. **Wie gibt eine Funktion zwei Werte zurück, und was ist das technisch?** (Rückblick auf Etappe 6.)

**Frage 7 ist die wichtigste**, und sie hat zwei Teile. Der zweite ist der schwierigere: „Es läuft noch" ist keine ausreichende Antwort. Wenn du sagen kannst, *woher du weißt*, dass sich nichts geändert hat, hast du verstanden, worum es in dieser Etappe ging.

---

## Transferaufgabe (10–15 Minuten)

**Neue Datei, außerhalb des Spiels.** `uebung_07.py`.

**Teil 0 — Erkennen statt Tippen (5 Minuten, kein Code)**

Hier ist ein Stück Befehlsverarbeitung, wie sie in vielen Textadventures aussieht:

```python
if befehl == "inventar":
    if inventar:
        print("Du trägst:")
        for gegenstand in inventar:
            print(f"- {gegenstand}")
    else:
        print("Dein Inventar ist leer.")

elif befehl == "karte":
    print("Du warst bereits hier:")
    for ort in sorted(besuchte_orte):
        print(f"- {ort}")

elif befehl == "umsehen":
    print(orte[aktueller_ort]["beschreibung"])
    for richtung in orte[aktueller_ort]["ausgaenge"]:
        print(f"  {richtung}")
```

**Schreib keinen Code.** Beantworte nur zwei Fragen für jeden Block:

1. Welche *eine* Aufgabe steckt hier drin?
2. Wie würde die Funktion heißen, und was müsste sie als Parameter bekommen?

Fünf Minuten, ein Blatt Papier. Und achte auf den dritten Block — steckt darin wirklich nur eine Aufgabe, oder sind es zwei?

Das ist eine andere Fähigkeit als Programmieren: **Struktur in fremdem Code erkennen.** Genau die brauchst du, wenn du später Code liest, den du nicht selbst geschrieben hast. Ab Etappe 9 wird daraus eine feste Übungsform.

**Teil 1 — Die Funktion**

> Schreib `berechne_schaden(angriff, ruestung)`. Sie gibt den tatsächlichen Schaden zurück.

Vier Zeilen. Der Rest der Aufgabe ist wichtiger.

**Teil 2 — Was muss immer gelten?**

Bevor du weiterschreibst, beantworte diese Fragen schriftlich:

- Kann der Schaden negativ werden? Soll er das dürfen?
- Was passiert bei `ruestung = 0`?
- Was passiert, wenn die Rüstung größer ist als der Angriff?
- Soll ein Treffer mindestens 1 Schaden machen, oder darf er wirkungslos sein?

Das sind keine Programmierfragen, sondern **Spieldesign-Fragen**. Und sie zeigen etwas Wichtiges: Bevor du entscheidest, was der Code tun soll, musst du entscheiden, was das Spiel tun soll.

**Teil 3 — Von Hand prüfen**

Schreib drei bis fünf Fälle auf — Eingaben und das Ergebnis, das du erwartest:

```text
berechne_schaden(10, 3)  ->  erwartet: 7
berechne_schaden(3, 10)  ->  erwartet: ?
berechne_schaden(5, 5)   ->  erwartet: ?
```

Erst aufschreiben, dann ausführen, dann vergleichen. Wo du danebenlagst, hast du entweder einen Fehler im Code oder eine unklare Regel im Kopf — beides ist wertvoll.

**Das ist Testdenken, lange bevor du ein Testframework anfasst.** In Etappe 26 schreibst du genau diese Fälle als `pytest`, und dann prüft der Rechner sie bei jeder Änderung. Und in Etappe 21 wird aus dieser Funktion die Kampfformel deines Spiels — mit Waffen, Rüstung und Trefferchance, aber demselben Kern.

---

## Kaputtmachen

Nach jedem Experiment rückgängig machen.

**Experiment 1 — Die lokale Variable**
```python
zaehler = 0

def erhoehe():
    zaehler = zaehler + 1

erhoehe()
```
`UnboundLocalError`. Lies ihn genau: Python behauptet, `zaehler` sei nicht zugewiesen — obwohl er oben steht. Warum?

Nimm dann die Zuweisung heraus und lies nur (`print(zaehler)`). Jetzt geht es. Was sagt dir das über den Zeitpunkt, an dem Python entscheidet, ob ein Name lokal ist?

**Experiment 2 — Die Klammern vergessen**
```python
def zeige():
    print("Hallo")

zeige
zeige()
```
Die erste Zeile tut nichts und meldet nichts. Fehler vom Typ 3. Lass dir mit `print(zeige)` anzeigen, was der Name ohne Klammern eigentlich ist.

**Experiment 3 — `print` statt `return`**
Bau eine deiner Entscheidungsfunktionen so um, dass sie druckt statt zurückzugeben. Versuch dann, das Ergebnis in einer Variable zu speichern und damit weiterzuarbeiten.

Was steht in der Variable? **Das ist derselbe Fehler wie `inventar = inventar.append(...)` aus Etappe 4** — nur diesmal in deinem eigenen Code.

**Experiment 4 — Argumente vertauschen**
```python
berechne_schaden(3, 10)
```
Kein Absturz. Nur ein Ergebnis, das keinen Sinn ergibt. Ruf sie dann mit Namen auf und beobachte, dass die Reihenfolge egal wird.

**Experiment 5 — `return` in der Mitte**
```python
def test():
    print("eins")
    return "zwei"
    print("drei")

print(test())
```
„drei" erscheint nie. Manche Editoren markieren die Zeile sogar als unerreichbar.

**Experiment 6 — `global` bauen und bereuen**
Bau eine Funktion mit `global`, die deinen Rundenzähler erhöht. Ruf sie an drei verschiedenen Stellen auf. Setz den Zähler dann absichtlich auf einen falschen Wert und such, welcher Aufruf schuld ist.

Danach dasselbe mit Parameter und `return`. Wo war die Suche kürzer?

**Experiment 7 — Zwei Funktionen, ein Name**
```python
def gruss():
    print("Erste")

def gruss():
    print("Zweite")

gruss()
```
Kein Fehler, keine Warnung. Die zweite überschreibt die erste stillschweigend. In einer 400-Zeilen-Datei ist das eine sehr unangenehme halbe Stunde.

**Experiment 8 — Zu viele Parameter**
Nimm deine größte Funktion und häng zwei weitere Parameter an, die sie eigentlich nicht braucht. Ruf sie an allen Stellen auf.

Das ist kein Fehler-Experiment, sondern ein Gefühls-Experiment. **Merk dir, wie sich das anfühlt** — Etappe 9 löst genau dieses Problem.

**Experiment 9 — Die vier Eingabeformen**
Deine `verarbeite_befehl()` steht. Jetzt tipp der Reihe nach:

```text
gehe norden
gehe
gehe norden extra
   GEHE    NORDEN
```

Vier Eingaben, die alle dasselbe meinen könnten. Welche funktionieren? Welche stürzen ab? Welche tun stillschweigend etwas Falsches?

Du musst heute nichts davon reparieren — das ist Etappe 20. **Aber schreib die Antwort auf**, denn sie ist die konkrete Fassung des Satzes, den du in Etappe 4 in `GELERNT.md` begonnen hast: *„Meine Befehlsverarbeitung nimmt momentan an, dass …"*

Und beachte, wie viel leichter diese Frage jetzt zu beantworten ist als vor dem Umbau. Vorher steckte die Annahme irgendwo in einer 300-Zeilen-Schleife. Jetzt steht sie in einer Funktion, deren Kopf dir sagt, was sie erwartet.

**Experiment 10 — Dein eigenes Refactoring sabotieren**
Nimm eine deiner neuen Funktionen und ändere genau **eine** Kleinigkeit, ohne aufzuschreiben welche:

- ein Argument beim Aufruf weglassen
- ein `return` entfernen
- zwei Parameter vertauschen
- einen Funktionsaufruf löschen

Dann starte das Spiel und **finde den Fehler selbst**, bevor du irgendwo nachschaust. Stoppe die Zeit.

Das ist die Generalprobe für Etappe 8. Und du wirst dabei etwas bemerken, das den ganzen Aufwand von heute rechtfertigt: In einer einzigen großen Schleife hättest du den Fehler überall suchen müssen. Jetzt lautet die Frage nur noch **„welcher Baustein verhält sich falsch?"** — und danach hast du zwanzig Zeilen statt dreihundert.

**Experiment 11 — Der zerstörte Beweis**
Ändere in einer deiner Ausgaben ein einziges Zeichen — ein Leerzeichen, einen Punkt. Lass den Verhaltens-Beweis nochmal laufen.

Der Vergleich findet es sofort. **Das ist der Beweis, dass dein Beweis funktioniert.** Ein Prüfverfahren, das nie anschlägt, ist wertlos — und du solltest einmal gesehen haben, dass deines anschlägt.

---

## Häufige Stolpersteine

| Fehlermeldung / Symptom | Was dahintersteckt | Wo du suchst |
|---|---|---|
| `UnboundLocalError: local variable 'x' referenced before assignment` | Irgendwo in der Funktion steht eine Zuweisung an `x` | Parameter und `return` statt Zuweisung an Äußeres |
| `NameError: name 'x' is not defined` | Variable existiert nur in einer anderen Funktion | Als Parameter übergeben |
| `TypeError: f() missing 1 required positional argument` | Zu wenige Argumente beim Aufruf | Definition und Aufruf vergleichen |
| `TypeError: f() takes 2 positional arguments but 3 were given` | Zu viele Argumente | Dasselbe von der anderen Seite |
| Die Variable enthält `None` | Funktion hat kein `return` | Steht dort `print` statt `return`? |
| Die Funktion tut nichts | Klammern beim Aufruf vergessen | `f` gegen `f()` |
| Ein Teil der Funktion läuft nie | `return` steht davor | Alles nach `return` ist tot |
| Das Verhalten hat sich verändert | Beim Umbau ist etwas verrutscht | Verhaltens-Beweis vergleichen, kleinschrittig zurück |
| `SyntaxError: non-default argument follows default argument` | Parameter mit Standardwert steht zu früh | Standardwerte ans Ende |
| Zwei Funktionen verhalten sich wie eine | Gleicher Name, die zweite gewinnt | Nach doppelten `def`-Zeilen suchen |
| Änderungen wirken nicht | Alte Version der Funktion wird gerufen | Datei gespeichert? Richtige Datei? |

**Der Debugging-Reflex dieser Etappe** ist ein neuer, und er ist besser als alles, was du bisher hattest: Wenn eine Funktion sich falsch verhält, ruf sie **einzeln** auf.

```python
print(berechne_schaden(10, 3))
```

Das ist der eigentliche Gewinn von Funktionen fürs Debugging. Vorher musstest du das ganze Spiel starten und dich zu der Stelle durchspielen. Jetzt prüfst du ein Stück Logik in einer Zeile, ohne das Drumherum.

In Etappe 8 lernst du dazu den Debugger — und in Etappe 26 lässt du diese Einzelaufrufe automatisch laufen. Beides baut auf dem auf, was du heute gebaut hast.

---

## Ein Blick nach vorne

Heute hast du deine Logik in Bausteine zerlegt. Aber du hast dabei ein neues Problem erzeugt, und das ist kein Versehen — es ist der Plan.

Deine größte Funktion sieht ungefähr so aus:

```python
def verarbeite_befehl(befehl, orte, aktueller_ort, inventar,
                      besuchte_orte, gesehene, runden, laeuft):
```

Acht Parameter, die alle zum selben Ding gehören: dem Zustand deiner Spielwelt. Sie wandern gemeinsam durch jede Funktion, und jede neue Datenstruktur macht die Liste länger.

In **Etappe 9** bekommen sie einen Behälter:

```python
class World:
    def verarbeite_befehl(self, befehl):
```

`self` *ist* dieser Haufen. Ein einziger Parameter, an dem alles hängt. Wenn du heute genug gelitten hast, ist das der Moment, in dem Klassen einleuchten statt nur vorzukommen.

In **Etappe 10** werden aus einzelnen Werten zusammengesetzte Objekte — ein Spieler, der ein Inventar *hat*. Und dort lauert die Standardwert-Falle, vor der oben gewarnt wurde.

**Und ein praktischer Gewinn, der ab heute jeden Tag zählt:** Vor dem Umbau musstest du deinem Mentor die ganze Datei zeigen, wenn etwas nicht ging. Ab jetzt reicht die eine Funktion plus ein Satz dazu, was der Zustand gerade ist.

Das ist wichtiger, als es klingt. Dein Spiel wird ab Etappe 12 mehrere hundert Zeilen haben, und eine KI, die jedes Mal alles lesen muss, wird unzuverlässiger — sie verliert dann eher ihre Anweisungen aus `MENTOR.md` aus dem Blick und schreibt dir doch die Lösung hin. **Gezielt fragen schützt also nicht nur ihre Zeit, sondern deinen Lernerfolg.**

In **Etappe 20** löst du die versteckten Annahmen auf, die dir heute aufgefallen sind. Deine Funktionen haben klare Grenzen bekommen; jetzt kannst du an diesen Grenzen prüfen, was hereinkommt.

In **Etappe 26** wird aus deinem Verhaltens-Beweis ein automatischer Test. Was du heute von Hand vergleichst, prüft dann der Rechner bei jeder Änderung — und deine „Was muss immer gelten?"-Fragen aus der Transferaufgabe werden zu Testfällen.

Und in **Etappe 27** zahlt sich die Design-Entscheidung von heute aus. Der Lehrplan verspricht dort, dass deine Logik beim Wechsel zu Pygame fast unverändert bleibt. Ob dieses Versprechen hält, hast du **heute** entschieden — an jeder Stelle, an der du `return` statt `print` geschrieben hast.

---

## Abschluss

**`GELERNT.md`:**
Zwei bis drei Sätze. Zusätzlich diesmal:

- Die Parameterzahl deiner größten Funktion
- Deine Entscheidung zu `print` gegen `return` und zum Zuschnitt, jeweils mit einem Satz Begründung
- Und die Frage dieser Etappe: **Was war beim Umbau schwierig?**

Bei der letzten Frage gilt eine Auflage: **„Nichts" ist keine zulässige Antwort.** Wenn wirklich alles glattlief, schreib das ausdrücklich hin — aber such vorher ehrlich. Die Stelle, an der plötzlich eine Variable nicht mehr gefunden wurde, ist genau der Ort, an dem dein Verständnis eine Lücke hatte. Diese Lücken zu notieren ist wertvoller als die Liste dessen, was funktioniert hat.

Fast jeder entdeckt beim ersten Refactoring etwas über den eigenen Code, das er vorher nicht wusste — meistens, dass zwei Stellen fast dasselbe tun.

**Commit:**
```bash
git add .
git commit -m "Etappe 7: Refactoring in Funktionen"
git push
```

Ein Commit, bei dem sich am Verhalten nichts ändert, wirkt sinnlos. Er ist das Gegenteil. Wenn in vier Wochen etwas kaputtgeht, willst du genau diesen Punkt in der Historie finden können.

---

## Wenn du mehr willst

Optional, erst bei grünem Selbsttest.

**Doppelten Code zusammenlegen.** Beim Umbauen ist dir wahrscheinlich aufgefallen, dass `nimm` und `ablege` sich sehr ähneln. Beide prüfen etwas, bewegen einen Gegenstand von einer Liste in eine andere und geben eine Meldung zurück.

Ob sich das zu einer Funktion zusammenfassen lässt, ist eine echte Abwägung — manchmal wird der gemeinsame Code so verschachtelt, dass zwei getrennte Funktionen ehrlicher sind. Nimm dir zehn Minuten und entscheide bewusst.

**Ein `hilfe`-Befehl aus einer Datenstruktur.** Statt fester `print()`-Zeilen ein Dictionary aus Befehl und Erklärung, das die Hilfe-Funktion durchläuft. Das ist derselbe Gedanke wie bei der Karte in Etappe 5: Inhalt sind Daten, nicht Code. Und es ist ein kleiner Vorgriff auf Etappe 25.

**Eine `ARCHITEKTUR.md`.** Eine halbe Seite, die das Skelett deines Spiels beschreibt: welche Datenstrukturen es gibt, welche Funktionen, wer wen ruft. Kein Code — nur die Landkarte.

```text
Zustand:  orte (dict), inventar (liste), besuchte_orte (set),
          aktueller_ort (str), runden (int)
Ablauf:   Hauptschleife -> verarbeite_befehl() -> zeige_ort()
                                               -> bewege_spieler()
                                               -> zeige_inventar()
```

Zehn Minuten Arbeit, zwei Nutzen. Erstens merkst du beim Schreiben, ob du deine eigene Struktur erklären kannst — wenn nicht, ist sie unklar. Zweitens kannst du diese Datei deinem Mentor geben, statt dreihundert Zeilen Code: Er versteht dann, worüber ihr redet, ohne alles lesen zu müssen.

Halte sie kurz und aktualisier sie beim Weiterbauen. Eine veraltete Architekturbeschreibung ist schlimmer als keine.

**Die Funktion, die dir am wenigsten gefällt.** Such die eine Funktion in deinem Code, bei der du beim Lesen zögerst. Schreib in einem Satz auf, was dich stört — zu lang, unklarer Name, tut zwei Dinge, zu viele Parameter.

Du musst sie nicht reparieren. Aber dieses Zögern beim Lesen ist ein Signal, das Berufsentwickler ernst nehmen, und es zu bemerken ist eine Fähigkeit für sich.

---

> **Nächste Etappe:** [Etappe 8 — Bug-Jagd I](etappe-08-bug-jagd.md) · Kein neues Python — eine eigenständige Fähigkeit
> Dort bekommst du deinen eigenen Code mit eingebauten Fehlern zurück. Einer stürzt sofort ab, einer manchmal, einer nie. Der dritte ist der wichtige.
