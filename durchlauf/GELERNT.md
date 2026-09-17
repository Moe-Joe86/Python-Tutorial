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

## Etappe 12

**12a, Auftragsschritt 2 — hat die Etappe-9-Antwort getragen?** Ja, fast vollständig. Die
Regel „gäbe es diesen Wert pro Figur oder pro Spiel?" hat für jeden der acht Welt-Werte sofort
eine eindeutige Antwort geliefert. Einzige Korrektur: `sektoren` stand in Etappe 9 nicht zur
Debatte (es gab noch keine `Welt`), aber nach derselben Regel angewendet gehört die Karte
eindeutig der Welt (es gibt sie einmal pro Spiel), nicht dem Marine.

**Design-Entscheidung „eine Liste oder zwei?" — zwei Listen, wie vom Plan vorgegeben.**
`welt.trupp` und `welt.gegner` bleiben getrennt, weil die Anmarschbahn (braucht `entfernung`)
und die Statusanzeige (braucht keine) sonst bei jedem Zugriff erst fragen müssten, was ein
Eintrag überhaupt ist — genau die Frage, die Etappe 11 gerade abgeschafft hat. Zusätzlicher,
selbst erlebter Grund: Die feste Reihenfolge „Trupp vor Gegner" im Tick ist nur sichtbar
und entscheidbar, weil es zwei Schleifen sind, keine gemeinsam sortierte Liste.

**12a — Anzahl der Zugriffsstellen:** Die Fahndung nach `kern_integritaet`/`gegner`/`trupp`/
`welle`/`sektoren` als losen Namen traf 22 Stellen (verteilt auf `verarbeite_befehl()` und das
Hauptprogramm); nach dem Umbau bekommt keine Funktion mehr mehr als zwei dieser Werte einzeln
— die meisten bekommen `welt` als Ganzes oder gar nichts davon.

**12b, Auftragsschritt 17 — die eigene Tick-Reihenfolge, mit Datum:**
1. `self.zeit += 1`
2. `welt.trupp` handelt (Kameraden feuern autonom)
3. `welt.gegner` handelt (rückt vor oder trifft den Kern)
4. Aufräumen (tote Gegner entfernen)

**Was wäre bei vertauschten Phasen 2/3 anders?** Ein Gegner, den ein Kamerad in Phase 2 mit dem
letzten nötigen Treffer erledigt, kann in der jetzigen Reihenfolge in Phase 3 desselben Ticks
nicht mehr vorrücken oder zuschlagen — er ist zu diesem Zeitpunkt schon `"tot"`. Mit
vertauschten Phasen würde derselbe Gegner in Phase 3 (jetzt zuerst) noch normal handeln, bevor
er in Phase 2 (jetzt danach) fällt — er bekäme also einen „letzten" Vorstoß, den er in der
gebauten Reihenfolge nie bekommt. Die gebaute Reihenfolge begünstigt damit leicht die
Verteidigung; die umgekehrte macht jeden Gegner einen Tick lang gefährlicher, bevor er fällt.

**Eigene Entscheidung: Eine ungültige Eingabe kostet keinen Tick.** Begründung: „Unbekannter
Befehl." ist reine Auskunft über die Eingabe, keine gescheiterte Handlung — dieselbe Logik wie
bei `status`/`umsehen` seit Etappe 3b. **Bewusst in Kauf genommene Kehrseite, per Kaputtmachen
1 verifiziert:** Damit lässt sich unendlich Zeit erkaufen, ohne dass sich am Spielzustand
etwas ändert (100 Unsinn-Eingaben hintereinander: `welt.zeit` bleibt `0`, kein Gegner rückt
vor) — ein Typ-3-„Fehler", der wie eine Spielmechanik aussieht, genau wie die Etappe vorhersagt.
Würde ich in einem echten Release anders entscheiden (ungültige Eingabe kostet doch einen Tick),
für diesen Lerndurchlauf aber bewusst so gelassen, weil beide Fassungen laut Guide vertretbar
sind und die aktuelle die tippfehlerfreundlichere ist.

**Offener Posten:** Die Kameraden feuern ohne Munitionsverbrauch (wie von der Etappe
ausdrücklich als Auslassung markiert, Etappe 13 wird das nachholen).

**Eigener, über die Etappe hinausgehender Fund — siehe BERICHT.md, Perspektive B/C:** Mit
`Gegner.update()` exakt wie in Auftragsschritt 12 spezifiziert (nur `welt.kern_integritaet`
nimmt Schaden) wird die zweite, seit Etappe 3c geforderte Verlustbedingung
(`marine.trefferpunkte <= 0`, „Du bist gefallen.") praktisch unerreichbar — nichts im neuen
Tick-Modell reduziert mehr die Trefferpunkte des eigenen Marines. Auftragsschritt 19 verlangt
aber ausdrücklich, weiterhin **beide** Verlustbedingungen zu prüfen. Für diesen Durchlauf
wurde die Spezifikation trotzdem wörtlich umgesetzt (kein eigener Schadensmechanismus
hinzuerfunden), weil die Etappe an keiner Stelle einen Ersatz dafür nennt — das ist also eine
Lücke im Guide, keine eigene Lücke in der Umsetzung.

**Was mich überrascht hat:** Wie stark sich die Funktionssignaturen verkürzt haben — aus
`verarbeite_befehl(eingabe, marine, trupp, kern_integritaet, gegner, sektoren, vorfeld,
freigeschaltet, gesehene_gegnertypen)` (neun Parameter, Etappe 11) wurde
`verarbeite_befehl(eingabe, welt, freigeschaltet, gesehene_gegnertypen)` (vier). Ebenso
überraschend: dass ein Kamerad tatsächlich ganz ohne eigenes Zutun einen Gegner erledigt —
verifiziert per Testlauf (siehe `BERICHT.md`).

## Etappe 13

**Design-Entscheidung „Wo läuft der Zähler?" — am Objekt, wie vom Plan vorgegeben.**
`abklingzeit`/`magazin`/`nachladezeit` gehören dem Marine, `bauzeit` dem Turm, `raeumzeit` der
Welt (der Tunnel gehört niemandem) — jeweils nach der Etappe-9-Regel „gäbe es diesen Wert pro
Figur oder pro Spiel?" entschieden. Ein eigenes `Abklingzeit`-Objekt oder ein Scheduler an der
Welt wären für vier Marines und einen Turm reiner Mehraufwand ohne Gegenwert — lohnt sich laut
Guide erst, wenn ein Zähler mehr kann als zählen (Etappe 18).

**Auftragsschritt 7 — was bedeutet `ABKLINGZEIT = 3` exakt?** Eingesetzt bei `welt.zeit == 10`:
Nach Tick 11 steht der Zähler auf 2, nach Tick 12 auf 1, nach Tick 13 auf 0 **und meldet sich
in genau diesem Tick**. „Wieder bereit" heißt also `welt.zeit == 13` — drei Ticks lang gesperrt
(11, 12, 13), danach frei. Verifiziert per Testlauf, stimmt mit der Vorhersage überein. Diese
Bedeutung gilt ab heute für alle fünf Zähler (Abklingzeit, Ausfallzeit, Nachladezeit, Bauzeit,
Räumzeit) — dieselbe `zaehler_runter()`-Form wird überall identisch verwendet.

**Neue Tick-Reihenfolge, mit Zählerphase an zweiter Stelle:**
1. `self.zeit += 1`
2. Zählerphase: `zaehler_runter(self)` an jedem Trupp-Mitglied, danach `welt.raeumzeit`
3. Trupp handelt (`update()`)
4. Gegner handeln (`update()`)
5. Aufräumen (tote Gegner entfernen, Ausfallzeit bei frisch gefallenen Trupp-Mitgliedern setzen)

**„Soll das gelten, oder soll das passieren?"** Zustand-Beispiel aus dem eigenen Code:
`marine.status == "tot"` — beliebig oft abfragbar, entscheidet z. B. in `verarbeite_befehl()`,
ob ein Befehl abgewiesen wird. Ereignis-Beispiel: die Zeile `if self.abklingzeit == 0:
welt.melde(...)` **innerhalb** des `if self.abklingzeit > 0:`-Blocks in `zaehler_runter()` —
sie läuft nur in dem einen Tick, in dem der Zähler tatsächlich von 1 auf 0 fällt, nicht in
jedem folgenden. Genau dieselbe Unterscheidung entscheidet, ob ein Stufenaufstieg einmal oder
in jeder Statuszeile erneut gemeldet wird (gelöst über „alte Stufe merken, neu berechnen,
vergleichen" — Konzept 4).

**Invariante und Merksatz (Auftragsschritt 10):**
- **Prüfbar:** Kein Zähler (`abklingzeit`, `ausfallzeit`, `nachladezeit`, `bauzeit`,
  `raeumzeit`) ist jemals kleiner als 0. Würde brechen, wenn irgendwo `zaehler_runter()` ohne
  die äußere `> 0`-Prüfung stünde (Kaputtmachen 2) — dann liefe der Zähler ins Negative und
  `== 0` träfe nie wieder.
- **Merksatz, nicht prüfbar:** Ein Zähler kann nicht gleichzeitig laufen und abgelaufen sein
  — z. B. kann `marine.status` nicht gleichzeitig `"tot"` (Ausfallzeit läuft) und `"aktiv"`
  sein. Würde brechen, wenn zwei Codepfade unabhängig voneinander über denselben Status
  entscheiden, ohne sich gegenseitig zu kennen — bisher nicht der Fall, aber keine Maschine
  könnte das automatisch prüfen.

**Meine Entscheidung aus Etappe 5 — ausgezahlt.** „Der Weg fehlt einfach" bedeutete heute genau
eine Zeile (`sektoren["osttor"]["nachbarn"]["osten"] = "landeplattform"`) statt der `del`-
Variante mit ihrer `KeyError`-Falle bei doppeltem Aufruf. Die damalige Notiz hat die
angekündigte halbe Stunde Suchen tatsächlich gespart.

**Gefundener, seit Etappe 3c/9 mitgeführter Bug (siehe BERICHT.md):** Der Marine-Balken in
`zeige_status()` verglich immer gegen die feste Zahl `100`, obwohl die vier Klassen seit
Etappe 2 unterschiedliche Start-Trefferpunkte haben (80–140) — für Heavy (140 TP) hätte der
Balken bei vollem Leben über 100 % angezeigt, für Medic (80 TP) nie ganz voll. Mit dem heute
geforderten `max_trefferpunkte`-Attribut (Auftragsschritt 12: „ist das schon derselbe Wert wie
in der Balkenanzeige? Dann kein zweiter Name") behoben.

**Was mich überrascht hat:** Wie klar der Unterschied zwischen dem eigenen Ausfall und dem
eines Kameraden tatsächlich spürbar war, obwohl es exakt derselbe Code ist (nur `gesteuert`
entscheidet Wartezeit und Konsequenz) — beim Kameraden spielt man einfach zu dritt weiter, beim
eigenen Ausfall steht das Spiel für den Spieler still, auch wenn der Tick technisch weiterläuft.
Ebenso überraschend: wie oft dieselben drei Zeilen (Zähler abfragen, abziehen, bei 0 melden)
heute tatsächlich wortgleich wiederkehrten — fünfmal, mit nur zwei Unterschieden (Name des
Zählers, Text der Meldung).

**Offener Posten:** Was dem Turm noch fehlt, bevor er sich richtig anfühlt — eine sichtbare
Reichweitenbegrenzung (er feuert aktuell wie ein Kamerad ohne eigene Munition oder Position,
Etappe 14b bringt echte Positionen und damit eine echte Reichweitenrechnung).
