# Gelernt

Kurzfassung, zwei bis vier Sätze pro Etappe, mit Begründung. Rückwirkend aus `BERICHT.md`
und `FEHLERTAGEBUCH.md` zusammengezogen ab Etappe 11 (siehe dortige Anfängerperspektive) —
ab Etappe 11 fortlaufend während des Bauens geführt.

## Etappe 1

- **Design-Entscheidung `klasse` als Zahl, nicht als Name.** Mit den Werkzeugen von Etappe 1
  (Variablen, `input()`, `int()`, f-Strings, kein `if`) lässt sich eine eingetippte Zahl nicht
  in einen Namen wie `"heavy"` übersetzen — das bräuchte eine Fallunterscheidung, die erst
  Etappe 2 bringt. Die Zahl ist die einzige mit heutigem Werkzeug baubare Option.
- **`letzte_meldung` wortwörtlich notiert**, weil sie in Etappe 17 zitiert wird — Wortlaut
  fett im Code-Kommentar, nicht nur sinngemäß im Kopf behalten.
- **Ungültige Eingabe stürzt ab** (`ValueError` bei `int("zwei")`) — bewusst nicht abgefangen,
  wird erst in Etappe 2 (Fallunterscheidung) bzw. Etappe 20 (`try`) behandelt.
- **Typ-3-Fehler aus der Übung** (Experiment 5 und 7): beide liefen fehlerfrei durch und
  lieferten Unsinn (falscher Wert bzw. erfundene Klasse ohne Fehlermeldung) — gefährlicher als
  ein Absturz, weil sie das falsche Vertrauen erzeugen „kein Fehler heißt richtiges Programm".

## Etappe 2

- **Bug gefunden durch den vom Auftrag selbst geforderten Test (Eingabe `9`):** Nach der
  freundlichen Meldung „Diese Klasse gibt es nicht." stürzt das Programm trotzdem mit
  `NameError: name 'schaden' is not defined` ab, weil die Werteanzeige direkt im Anschluss an
  die `if`/`elif`/`else`-Kette steht, ohne zu prüfen, ob ein gültiger Zweig gelaufen ist.
  Mit heutigem Werkzeug behoben durch einen Schutz-Boolean `klasse_gueltig`.
- **Die wichtigere Lehre daraus:** „Läuft ohne Fehlermeldung" und „ist korrekt" sind zwei
  verschiedene Dinge — dieselbe Lektion wie Etappe 1, hier aber am eigenen Code erlebt statt
  nur an einer Übungsaufgabe.

## Etappe 3

- **Spielende „von innen nach außen"**: ein Boolean `spiel_laeuft`, in der inneren Schleife
  gesetzt, in der äußeren geprüft — ließ sich aus den vorher gelernten Bausteinen (Boolean,
  `break`, `while`) tatsächlich selbst herleiten, ohne fremde Lösung.
- **`ziel_in_sicht` bleibt ab hier ungenutzt liegen** (Etappe 3c baut die Feuerbedingung neu,
  ohne die Variable) — bewusst nicht mehr mitgeführt, zahlt laut `BOGEN.md` erst in Etappe 12/18.

## Etappe 4

- **Randfall ohne Vorgabe: Gegner erreicht das Bahnende.** Die naive Umsetzung stürzt mit
  `IndexError` ab, sobald eine Position über `FELDER` hinausläuft (reproduziert durch
  wiederholtes `nachladen` ohne `feuern`). Eigene Entscheidung: Position nur zeichnen, wenn
  sie im gültigen Bereich liegt — behebt den Absturz, macht den Gegner aber unsichtbar,
  während er weiter Schaden meldet. Bekannte, nicht vom Guide behandelte Lücke.
- **`nimm`/`ablege` kosten keine Runde** — eigene Interpretation (Auskunft/Handlung außerhalb
  des Kampfgeschehens), vom Guide nicht ausdrücklich festgelegt.

## Etappe 5

- **Chitinpanzer/Organe landen automatisch am Wellenende in `vorrat`**, nicht über einen
  `nimm`-Befehl — eigene Lesart einer vom Guide nur behaupteten, nicht gezeigten Mechanik.
- **Drei Wörter, die nicht durcheinandergeraten dürfen:** Depot (Ort) / Vorrat (Material,
  Marine-gebunden) / Inventar (Gegenstände, Platz-begrenzt) — als feste Gedächtnisstütze
  übernommen, wird ab hier durchgehend so verwendet.

## Etappe 6

- **`magazin_groesse` rückwirkend auf 40 korrigiert.** Etappe 5 ließ den Startwert offen,
  `et5.py` wählte 8; Etappe 6 setzt „von 40 auf 60" voraus. Eigene Entscheidung: 40 nachträglich
  als Startwert übernommen, mit Kommentar — sonst wäre der Ausbau-Text falsch.
- **`schalte frei <kennung>` ist ein Drei-Wort-Befehl** in einer sonst auf zwei Wörter
  (Verb + Ziel) festgelegten Grammatik — drittes Token eingeführt, nur für diesen Befehl.
- **Invariante `len(gegner) == len(gegner_typen)`** nach jeder Änderung explizit aufgeschrieben
  und bei jeder Änderungsstelle im Kopf mitgeführt — verhindert das parallele Auseinanderlaufen
  der beiden Listen, das in Etappe 11a ohnehin verschwindet.

## Etappe 7

- **Zwei echte, stille Regressionen ausschließlich durch den vorgeschriebenen `diff`-Beweis
  gefunden**, nicht durch Durchspielen: (1) `zeige_status()` ohne `kern_integritaet`/
  `trefferpunkte` als Parameter (Typ-3-Fehler, falsche Anzeige, kein Absturz), (2) verlorenes
  Kurzschluss-Verhalten bei leerer Eingabe (eine zusätzliche Bahn-Zeile). Beide behoben, danach
  ist `diff vorher.txt nachher.txt` still.
- **Die gefährlichere der beiden war (1)**, nicht (2): ein Absturz (oder eine sichtbar falsche
  Zeile bei jedem Aufruf) wäre schnell aufgefallen — die falsche 0%-Anzeige hätte sich dagegen
  unbemerkt als „normales" Verhalten festsetzen können, wäre sie nicht durch den systematischen
  Test aufgefallen.
- **GROSS geschriebene Konstanten (`WAREN`, `AUSBAUTEN`, …) werden nicht als Parameter
  durchgereicht** — eigene, vom Guide nicht ausdrücklich entschiedene Abgrenzung von „alles als
  Parameter".

## Etappe 8

- **Eigene Fehlannahme korrigiert:** Erwartet war ein stiller Fehler beim vertippten
  Vorrats-Schlüssel (`vorrat["vaporum"]`), wie Etappe 5 es lehrt. Tatsächlich stürzt das
  Programm sofort mit `KeyError` ab, weil die Zeile `-=` verwendet — das liest den Schlüssel
  zuerst, bevor es schreibt, anders als eine reine Zuweisung.
- **Regel geschärft:** Ein Tippfehler im Schlüssel bleibt nur bei reiner Zuweisung (`=`) still;
  bei `+=`/`-=` stürzt er meistens laut ab, weil zuerst gelesen wird.
- Simulationsgrenze ehrlich notiert: Die „Zeitversatz"-Methode (zwei Tage warten, um die
  eigene Sabotage zu vergessen) ließ sich in einem durchgehenden Lauf nicht echt nachbilden.

## Etappe 9

- **Dritter echter, stiller Fund durch `diff` in Folge:** Nach vollständigem Umzug von
  `trefferpunkte` in `Marine` verschwand die Briefing-Zeile „Trefferpunkte: 100", weil dieses
  Briefing **vor** der Klassenwahl steht, das `Marine`-Objekt aber erst danach entstehen kann.
  Behoben mit einer eigens benannten Anzeige-Variablen nur für diese eine Zeile.
- **Eigene Erweiterung der Attributtabelle:** `geladen`/`magazin_groesse`/`nachladen_noetig`
  stehen nicht in der Vorlage des Guides, gehören aber nach dessen eigenem Test („hätte ein
  zweiter Marine seinen eigenen Wert?") eindeutig in die Klasse.

## Etappe 10

- **Scheinbare Regression war keine:** vertauschte Reihenfolge zweier Gegnertyp-Zeilen im
  `diff`, obwohl an der vermeintlich betroffenen Stelle nichts geändert wurde. Ursache:
  `wellen_typen` ist ein **Set** seit Etappe 6, dessen Iterationsreihenfolge bei jedem
  Prozessstart neu von Pythons Hash-Randomisierung bestimmt wird — verifiziert durch
  wiederholte Läufe von `et9.py` **gegen sich selbst** (MD5-Vergleich, `PYTHONHASHSEED` fix
  vs. nicht fix).
- **Konsequenz für die eigene Methodik:** Beweisläufe (`vorher.txt`/`nachher.txt`) ab jetzt mit
  `PYTHONHASHSEED=0` fixiert, sonst ist ein „Unterschied" nicht zwangsläufig ein Fehler.

## Etappe 11

**11a, Auftragsschritt 6 — welche zwei Fehlerarten aus Etappe 6 sind jetzt unmöglich?**
Etappe 6 kannte zwei Arten, wie `gegner`/`gegner_typen` auseinanderlaufen konnten: **Stufe A**
(die Längen selbst laufen auseinander, z. B. weil ein Entfernen nur eine der beiden Listen
trifft — Typ 2, der Absturz kommt erst Runden später bei einem Indexzugriff ins Leere) und
**Stufe B** (die Längen bleiben gleich, aber Position und Typ gehören nicht mehr zum selben
Gegner, weil aus beiden Listen an unterschiedlichen Stellen entfernt wurde — Typ 3, nie
sichtbar außer durch genaues Hinsehen). Mit einer einzigen Liste von `Gegner`-Objekten und
`remove(objekt)` kann **keine** der beiden Situationen mehr entstehen — es gibt nur noch eine
Länge und eine Zuordnung, die sich nicht mehr trennen lassen.

**Die gefährlichere war Stufe B**, nicht Stufe A: Ein `IndexError` (Stufe A) stoppt das
Programm und zeigt unmissverständlich, dass etwas nicht stimmt — unangenehm, aber ehrlich.
Stufe B dagegen erzeugt einen **plausibel falschen Zustand**, der nie abstürzt und keine
Prüfung je auslöst (ein Speier steht da, wo ein Kriecher stehen müsste) — genau die
Fehlerklasse, die laut Etappe 1 am gefährlichsten ist, weil sie das Vertrauen „kein Fehler
heißt richtiges Programm" bestätigt, obwohl es falsch ist.

**11b, Auftragsschritt 11 — Vererbungsfrage für `Soldat`/`Heavy`/`Engineer`/`Medic`, 17.09.2026:**
Die vier Klassen brauchen echte Vererbung, keine vier Tabellenzeilen. Grund: Es ist nicht nur
gemeinsamer **Zustand** (Trefferpunkte, Schaden, Panzerung — das allein spräche für eine
Tabelle plus Dictionary), sondern gemeinsames **Verhalten mit Überschreibung** —
`faehigkeit_einsetzen()` muss bei gleichem Aufruf (`marine.faehigkeit_einsetzen()`, ohne
Typabfrage) vier verschiedene Dinge tun. Eine Tabelle liefert Werte, aber keinen
überschreibbaren Methodenaufruf ohne `if`-Kette an der Aufrufstelle — genau die `if`/`elif`-
Kette, die Auftragsschritt 11 gerade abschafft. Meinung würde sich ändern, wenn
`faehigkeit_einsetzen()` bei allen vier identisch bliebe (dann Tabelle) oder wenn eine fünfte
Klasse käme, deren Fähigkeit sich nicht als einfache Methodenüberschreibung, sondern nur als
Sonderfall mit vielen Ausnahmen ausdrücken ließe (dann Komposition statt Vererbung, wie bei
`Inventar`/`Ausruestung`).

**11c, Auftragsschritt 17 — dieselbe Frage für `Item`/`Waffe`/`Panzerung`/`Modul`/`Verbrauchsgut`:**
Hier ist die Antwort schwächer begründet als bei den Marine-Klassen — die vier Unterklassen
haben **keine** gemeinsame überschriebene Methode (nur `__repr__`, das ist reine Anzeige, kein
Spielverhalten). Was sie gemeinsam haben, ist im Wesentlichen `kennung` und `name` plus je
eigene, sich nicht überschneidende Zusatzattribute — das fällt eher in die dritte, schwächste
Kategorie „bloß gemeinsame Attribute". Vertretbar ist die Hierarchie trotzdem, weil
`erzeuge_item()` an einer Stelle über den Rückgabetyp entscheidet und `isinstance()`-Prüfungen
(z. B. für einen späteren Ausrüstungs-Slot-Check) an genau diese Struktur anknüpfen können —
aber ehrlich zugegeben: Eine einzige `Item`-Klasse mit einem `art`-String-Feld hätte hier
ebenso funktioniert, und die Grenze ist dünner als bei den Marine-Klassen. Würde die Meinung
ändern, wenn sich zeigt, dass keine der vier Unterklassen in späteren Etappen (22: Speicherung,
25: JSON) je eigenes Verhalten bekommt — dann wäre die Attribut-Hierarchie im Rückblick
Overengineering gewesen.

**11c, Auftragsschritt 18 — woran erkennt man beim Lesen, dass ein Objekt iterierbar ist?**
Wenn die Klasse `__iter__` (oder ersatzweise `__getitem__`) definiert, oder wenn sie von einer
eingebauten iterierbaren Klasse erbt (`list`, `dict`, `set`, …). Ohne eine dieser beiden
Voraussetzungen bricht `for x in objekt:` mit `TypeError: 'X' object is not iterable` ab —
keine der eigenen Klassen in diesem Projekt (`Marine`, `Gegner`, `Item`, `Inventar`, …)
definiert `__iter__`, sie sind also alle nicht direkt iterierbar, nur ihre Attribute
(`inventar.gegenstaende` als Liste) sind es.
