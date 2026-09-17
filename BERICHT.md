# Bericht: Tutorial-Prüfung „Vorposten"

Dieser Bericht dokumentiert einen vollständigen Anfängerdurchlauf und eine professionelle Prüfung des Tutorials, Stand der 16 vorhandenen Etappen-Guides (Etappe 1–16). Geprüft wurden `Vorposten_Lehrplan.md`, `SYNTAX.md`, `BOGEN.md` und jede Etappe einzeln — jeweils aus drei Blickwinkeln: als absoluter Python-Anfänger, der die Aufgaben tatsächlich löst; als Fachprüfung der Etappe gegen die drei Register; und als Abgleich zwischen dem, was das Spiel verspricht, und dem, was tatsächlich gebaut wird.

Der zu jeder Etappe entstandene Code liegt unter `durchlauf/et1.py` … `durchlauf/et16.py` — jede Datei ist der vollständige Programmstand nach Abschluss der jeweiligen Etappe, geschrieben ausschließlich mit den Werkzeugen, die laut `SYNTAX.md` bis zu diesem Zeitpunkt zur Verfügung standen.

---

## Teil 1 — Grundlagenprüfung: Lehrplan, SYNTAX.md, BOGEN.md

### Methodik

Alle drei Dateien wurden vollständig gelesen: der Lehrplan komplett (Rahmenteil plus alle 31 Etappenabschnitte, Block 0–4), `SYNTAX.md` komplett (Etappe 0–16, „Offene Lücken", Pflegeregeln), `BOGEN.md` komplett (Teil A für Etappe 0–6 im Detail, Teil A für Etappe 6 ff. stichprobenartig, Teil B und Teil C vollständig). Geprüft wurde erstens jede Datei für sich (Vollständigkeit, innere Widersprüche, Reihenfolge), zweitens das Zusammenspiel der drei Dateien untereinander, drittens der Abgleich gegen die tatsächlichen Etappen-Guides (Kopfzeilen, „Neue Syntax heute").

### 1.1 Befund: Widerspruch zwischen BOGEN.md und Lehrplan bei der Portionierung

**Das ist der schwerwiegendste Einzelfund der Grundlagenprüfung.**

`BOGEN.md`, Zeile 29, behauptet:

> „**1. Sieben Etappen sind in Portionen geteilt** — 3, 7, 9, 14, 17, 21, 23."

Der Lehrplan selbst (`Vorposten_Lehrplan.md`, Abschnitt „Arbeitsregeln", Tabelle „Geteilt / Portionen") listet dagegen **elf** geteilte Etappen: 3a/b/c, 7a/b, 9a/b, **11a/b/c**, **12a/b**, **13a/b**, 14a/b/c, **15a/b**, 17a/b, 21a/b, 23a/b. Diese Zahl ist auch die einzige, die mit der eigenen Rechnung des Lehrplans aufgeht: „30 Etappen — gerechnet in Portionen sind es 44". Rechnet man nach: 3 zusätzliche Portionen bei 3/11/14 (je +2) und 1 zusätzliche bei den übrigen acht (7,9,12,13,15,17,21,23, je +1) ergibt 30 + 2+2+2+8 = 44. Stimmt nur mit der Elf-Etappen-Liste.

Die tatsächlich vorhandenen Etappen-Dateien bestätigen die Lehrplan-Version, nicht die BOGEN-Version: `etappe-11-vererbung.md` hat die Portionen 11a/11b/11c, `etappe-12-der-tick.md` hat 12a/12b, `etappe-13-bauzeit-und-abklingzeit.md` hat 13a/13b, `etappe-15-was-die-brut-hinterlaesst.md` hat 15a/15b — alle vier fehlen in der BOGEN-Liste der „sieben Etappen". `BOGEN.md` selbst benutzt an Dutzenden Stellen im Fließtext Bezeichnungen wie „11a", „12b", „13a", „15a" — der einleitende Satz widerspricht damit sogar dem eigenen Dateiinhalt.

**Auswirkung:** Gering für den Lernenden selbst (die Guides sind korrekt geteilt), aber die Aussage ist die Art Fehler, vor der `MENTOR.md` ausdrücklich warnt — ein Mentor, der sich auf diese eine Zeile verlässt, unterschätzt systematisch, wie viele Etappen halbiert sind, und könnte einem Lernenden fälschlich sagen, Etappe 11 oder 13 sei „eigentlich nicht geteilt vorgesehen".

**Verbesserung:** Die Zeile in `BOGEN.md` auf „Elf Etappen sind in Portionen geteilt — 3, 7, 9, 11, 12, 13, 14, 15, 17, 21, 23" korrigieren.

### 1.2 SYNTAX.md — Vollständigkeit und Konsistenz

`SYNTAX.md` ist das jüngste und am saubersten geführte der drei Register. Die Selbstauskunft „Für die Etappen 1 bis 16: keine [offenen Lücken]" wurde beim Anfängerdurchlauf stichprobenartig geprüft (siehe Teil 2 je Etappe) und hielt in den meisten Fällen stand; die wenigen Ausnahmen, die der Anfängerdurchlauf tatsächlich fand, stehen bei der jeweiligen Etappe unter „B – Professionelle Perspektive".

Die Kopfzeilen „Neue Syntax heute" der 16 vorhandenen Guides wurden gegen die jeweilige `SYNTAX.md`-Tabelle abgeglichen (siehe Einzelbefunde je Etappe). In der großen Mehrheit deckungsgleich; Abweichungen sind unter den jeweiligen Etappen vermerkt.

Ein struktureller Pluspunkt: Der Abschnitt „Offene Lücken" in `SYNTAX.md` dokumentiert drei bereits geschlossene Lücken (`.clear()`, nacktes `return`, f-String-Dictionary-Zugriff in Etappe 5) transparent mit Herkunft — das ist genau die Art Selbstkorrektur-Spur, die `skills/SKILL.md` für den Fließtext der Etappen verbietet („keine Entwicklungsgeschichte im Text"), aber für die Register-Dateien ausdrücklich sinnvoll ist, weil sie zukünftige Autoren vor denselben Fehlern warnt. Kein Widerspruch, aber erwähnenswert als gutes Beispiel.

### 1.3 BOGEN.md — Vollständigkeit und Konsistenz (über 1.1 hinaus)

- **Statusspalte grundsätzlich plausibel.** Stichproben (Etappe 1, 4, 5, 6, 9, 10, 11, 12, 13, 14) zeigen, dass als „eingelöst ✓" markierte Einträge tatsächlich in den genannten Ziel-Etappen erscheinen (z. B. Objektidentität in Etappe 10, Tick-Prinzip in Etappe 12). Die Statuspflege wirkt ernsthaft betrieben, nicht wie eine Attrappe.
- **Teil B und Teil C sind vollständig und intern konsistent** mit der Etappen-Nummerierung und den Portionen-Kürzeln (11a/b/c, 12a/b usw.) — sie verwenden korrekt die Elf-Etappen-Zählung aus dem Lehrplan, was den Fehler in 1.1 zusätzlich als isolierten Ausrutscher in der Einleitungszeile bestätigt, nicht als durchgängiges Problem.
- **Ein doppelter Tabelleneintrag**, kein Widerspruch, aber ein Ordnungsfehler: In Etappe 5 (Teil A) steht der Eintrag zur Stufentabelle (`{1: 0, 2: 120, 3: 300}`) durch eine Leerzeile und eine zweite Markdown-Tabelle vom Rest der Etappe-5-Tabelle getrennt (Zeilen 235–236 im Vergleich zum Rest 180–233) — inhaltlich zugehörig, aber technisch eine zweite Tabelle mit eigenem Header direkt im Anschluss ohne Zwischenüberschrift. Kosmetisch, aber beim Queren mit `grep -n "\*\*N\*\*"` (wie die eigene Pflegeanleitung es vorschreibt) leicht zu übersehen, weil man eine einzelne durchgehende Tabelle erwartet.

### 1.4 Reihenfolge und Aufbau

Die Reihenfolge Lehrplan → Rahmenregeln → Block 0–4 → Etappen 0–30 ist stringent und didaktisch klar begründet (Drei-Anspruchsstufen-Prinzip vor den Etappen, Balancing-Falle vor Etappe 3, wo sie zuerst akut wird, usw.). Keine Reihenfolge-Fehler gefunden. Die Cross-Referenzierung (Lehrplan verweist auf BOGEN und SYNTAX, beide verweisen zurück) ist geschlossen und ohne erkennbare Zirkelverweise, die sich widersprechen.

### 1.5 Passen die drei Dokumente zu den tatsächlichen Etappen?

Grundsätzlich ja — mit den unter 1.1 genannten Einschränkung und den Einzelbefunden je Etappe in Teil 2. Auffällig positiv: Die Etappen-Guides sind an vielen Stellen **detaillierter und vorsichtiger** als ihre Kurzfassung im Lehrplan (z. B. Etappe 5 im Lehrplan vs. im eigenen Guide — der Guide baut zusätzliche Sicherungen gegen die dort beschriebenen Fallstricke ein). Das ist kein Widerspruch, sondern die vom Lehrplan selbst verlangte Arbeitsteilung („Landkarte, kein Lehrbuch").

---

## Teil 2 — Etappen-Durchlauf

### Etappe 1 — Der Abwurf

**Code:** `durchlauf/et1.py`

**A – Anfängerperspektive.** Die Umsetzung war fast durchgehend problemlos — die Etappe ist sehr kleinschrittig geführt, jeder Schritt hat ein konkretes Ziel und ein Beispiel in fremdem Kontext. Ein echter Stolperstein trat aber auf: Bei der „Design-Entscheidung, die du jetzt treffen solltest" werden zwei gleichwertig klingende Optionen für die Speicherung der Klassenwahl angeboten — **die Zahl** oder **der Name** (`klasse = "heavy"`). Mit den Werkzeugen, die bis zu diesem Punkt eingeführt sind (nur Variablen, Zuweisung, `input()`, `int()`/`float()`/`str()`, Rechnen, f-Strings — **kein** `if`, keine Liste, kein Dictionary), lässt sich eine eingetippte Zahl wie `2` aber gar nicht in einen Namen wie `"heavy"` übersetzen. Das bräuchte zwingend eine Fallunterscheidung, und `if` kommt laut `SYNTAX.md` erst in Etappe 2. Als Anfänger, der sich strikt an „nur bereits Gelerntes" hält, bleibt real nur die Option „Zahl" — die zweite Option ist an dieser Stelle eine Behauptung ohne Werkzeug dahinter. `durchlauf/et1.py` speichert deshalb `klasse` als Zahl, mit einem Kommentar, der das begründet.

**B – Professionelle Perspektive.**
- **Fachlicher Fehler (klein, aber real):** Im Selbsttest steht *„Alle fünf Lagewerte existieren als Variablen mit den vorgegebenen Startwerten"* — Auftragsschritt 3 listet aber **sechs** Werte (`kern_integritaet`, `trefferpunkte`, `munition`, `vaporium`, `rekruten_verfuegbar`, `wellen_bis_evakuierung`). Auch wenn man `kern_integritaet`/`trefferpunkte` abzieht, weil sie einen eigenen Selbsttest-Punkt bekommen, bleiben vier, nicht fünf. Wirkt wie ein stehengebliebener Zähler aus einer früheren Fassung (vermutlich vor Einführung von `rekruten_verfuegbar`) — genau die Art Zahlenfehler, vor der der Lehrplan selbst warnt.
- **Design-Lücke:** siehe A — die „Name"-Option der Design-Entscheidung ist in Etappe 1 mit den vorhandenen Werkzeugen nicht baubar. Entweder gehört ein Satz dazu, der sagt *„Die Umsetzung als Name folgt technisch erst in Etappe 2 — leg heute nur die Entscheidung fest, nicht den Code"*, oder die Formulierung „eine Umwandlung mehr heute" muss weg, weil sie das Gegenteil suggeriert.
- **„Neue Syntax heute"-Kopfzeile vs. `SYNTAX.md`:** deckungsgleich für alles, was tatsächlich Sprachsyntax ist. Einträge wie „GROSS geschriebene Namen" oder „`trefferpunkte` als zweiter Gesundheitswert" fehlen in der Kopfzeile, gehören dort aber nicht hin — es sind Konventionen bzw. Inhalte, keine Syntax. Kein Fehler.
- **Didaktisch stark:** Die Etappe ist ungewöhnlich ehrlich über ihren eigenen geringen Neuheitswert („Als Programmierübung ist das mager") und begründet den Sinn sofort nachvollziehbar. Die explizite Liste „Was NICHT in diese Etappe gehört" nimmt Druck raus und verhindert genau das Vorgreifen, das an anderer Stelle (siehe A) fast provoziert würde.
- **Code gegen Etappe geprüft:** `et1.py` erfüllt alle Punkte des Selbsttests bis auf die numerische Unstimmigkeit oben, die sich nicht eindeutig erfüllen lässt.

**C – Inhalt gegen Anspruch.** Etappe 1 verspricht selbst noch kein Spielfeature, sondern legt Variablen für später an (`letzte_meldung`, `kern_integritaet`, `wellen_bis_evakuierung`). Das ist transparent kommuniziert („Der lange Bogen"-Tabelle nennt explizit, wo jeder Wert wieder auftaucht) und wird, soweit die vorhandenen Etappen das zeigen, auch eingelöst (siehe Etappe 3, 9, 11, 13 unten). Keine Diskrepanz feststellbar — diese Etappe ist bewusst ein Versprechen, kein Feature.

---

### Etappe 2 — Der erste Kontakt

**Code:** `durchlauf/et2.py`

**A – Anfängerperspektive.** Bis auf einen Punkt reibungslos — `if`/`elif`/`else`, `and`, die verknüpfte Feuerbedingung, alles ließ sich mit den bis hierhin gelernten Werkzeugen direkt umsetzen, und die Beispiele in fremdem Kontext (Bäckerei, Türsteher) waren beim Übertragen wirklich hilfreich. **Ein Punkt hat aber tatsächlich zum Absturz geführt, und zwar genau der von der Etappe selbst verlangte Test:** Auftragsschritt 5 fordert ausdrücklich, alle fünf Fälle durchzuspielen, darunter `9`. Mit dem `else`-Zweig aus Schritt 3 (der nur eine Meldung ausgibt) und der Werteanzeige aus Schritt 4 (die direkt im Anschluss `schaden`, `panzerung` und `klassengeraet` ausgibt) stürzt das Programm bei Eingabe `9` mit `NameError: name 'schaden' is not defined` ab — **nachdem** die freundliche Meldung „Diese Klasse gibt es nicht." bereits erschienen ist. Reproduziert in `durchlauf/et2.py` (siehe Testlauf unten). Als Anfänger, der nur das in dieser Etappe Gezeigte kennt, gibt es keinen erkennbaren Ausweg: Funktionen, `return`, `try`/`except` oder gar `sys.exit()` sind alle nicht verfügbar (die ersten beiden erst Etappe 7, `try` erst Etappe 20). Die einzige Lösung mit heutigem Werkzeug wäre, die Anzeige mit einem eigenen Boolean (`klasse_gueltig`) zu schützen — das ist technisch machbar, aber der Guide erwähnt diese Notwendigkeit an keiner Stelle.

**B – Professionelle Perspektive.**
- **Fachlicher/didaktischer Fehler (der wichtigste Fund dieser Etappe):** Die eigene Zusage im Abschnitt „Worum es geht" — *„Eingabe `9` lief stillschweigend durch — der `else`-Zweig fängt sie ab"* — stimmt nur für den `else`-Zweig selbst, nicht für das Programm als Ganzes. Der Selbsttest-Punkt *„Eingabe `9` erzeugt eine verständliche Meldung statt einer erfundenen Klasse"* wird im Effekt erfüllt (die Meldung erscheint), verschweigt aber, dass direkt danach ein unbehandelter Absturz folgt, wenn Schritt 4 wie beschrieben direkt im Anschluss an die Kette steht. Das ist exakt die Fehlerklasse, vor der die eigene Lösungsprobe-Methodik (siehe `skills/SKILL.md`, Abschnitt 3) schützen soll: Jeder Auftragsschritt selbst lösen und ausführen — hier hätte das den Fehler sofort gezeigt.
  **Verbesserungsvorschlag:** Ein Satz in Schritt 4 oder ein kleiner Kasten, der auf einen Schutz-Boolean hinweist (`klasse_gueltig = False`, in jedem Zweig auf `True` gesetzt, Anzeige nur `if klasse_gueltig:`) — mit den Werkzeugen aus Konzept 6 vollständig lösbar, ohne irgendetwas vorzugreifen.
- **„Neue Syntax heute" vs. `SYNTAX.md`:** deckungsgleich; alle 👀-Einträge (Punkt-Schreibweise, `and`/`or` als Wertgeber) korrekt aus der Kopfzeile ausgespart.
- **Didaktisch bemerkenswert stark:** Der Abschnitt „Was NICHT in diese Etappe gehört" nimmt die naheliegende Kritik („das wäre doch ein Dictionary") selbst vorweg und begründet sie überzeugend mit dem späteren Ertrag in Etappe 11 — genau die Art Transparenz, die Frust vermeidet, weil sie zeigt, dass die hässliche Lösung heute Absicht ist statt Unwissen des Autors.
- **Sauber:** Die Trennung `kern_integritaet` (Anlage) / `trefferpunkte` (Marine) wird ein zweites Mal explizit mit Tabelle und Warnkasten geschärft — konsistent mit Etappe 1 und mit `BOGEN.md`s Eintrag zur „Namensfalle".

**C – Inhalt gegen Anspruch.** Die Etappe verspricht „Der Heavy hält aus, was den Medic umwirft" — das wird durch unterschiedliche `trefferpunkte`/`schaden`/`panzerung` je Klasse tatsächlich eingelöst, spaltenweise wie in `GELERNT.md` gefordert nachvollziehbar. Die Zukunftsversprechen zum Klassengerät (Granatwerfer, Durchschlag usw. ab Etappe 18) sind explizit als „nichts davon heute" markiert — keine Diskrepanz. Die einzige Lücke zwischen Anspruch und Umsetzung ist die unter A/B beschriebene: Der Anspruch „ungültige Eingabe wird sauber behandelt" wird nicht vollständig eingelöst.

---

### Etappe 3 — Die Wellenschleife (3a/3b/3c)

**Code:** `durchlauf/et3.py` (Endstand nach 3c, komplett getestet: 20-Wellen-Durchlauf, `status`/`feuern`/`nachladen`/ungültiger Befehl, Game-Over über `kern_integritaet`)

**A – Anfängerperspektive.** Trotz des Umfangs (drei Portionen) die bisher angenehmste Etappe. Besonders bemerkenswert: Die „Knobelstelle" in Schritt 6 (Spielende von innen nach außen mitteilen) ließ sich tatsächlich ohne fremde Hilfe lösen — mit einem Boolean `spiel_laeuft`, der in der inneren Schleife gesetzt und in der äußeren geprüft wird. Genau dieses Muster wird danach in Konzept 11 („Variante A") explizit bestätigt und benannt. Das ist gute Didaktik: Die Bausteine für die eigene Lösung waren tatsächlich alle vorher vorhanden (Boolean aus Etappe 2, `break` und `while` aus 3a) — anders als im Vorfall aus Etappe 1/2, wo eine angebotene Lösung Werkzeuge voraussetzte, die es noch nicht gab. Der explizite Warnkasten zu Auftragsschritt 17 („Schaden gehört genau dorthin, wo auch der Rundenzähler hochzählt") hat den naheliegenden Fehler (Schaden am Blockende statt an die Rundenkosten-Bedingung gebunden) proaktiv verhindert, bevor ich ihn machen konnte.

**B – Professionelle Perspektive.**
- **Kleine Konsistenzlücke:** `ziel_in_sicht` wird in Etappe 2 als dritter, gleichberechtigter Teil der Feuerbedingung eingeführt (`munition > 0 and not nachladen_noetig and ziel_in_sicht`). Etappe 3c, Auftragsschritt 15, baut die Feuerbedingung neu auf und erwähnt nur noch „ist keine Munition da" — `ziel_in_sicht` taucht im ganzen Rest der Etappe nicht mehr auf. `BOGEN.md` bestätigt das: Der Eintrag zu `ziel_in_sicht`/`nachladen_noetig` steht weiterhin auf „offen", Zieletappe 12/18. Für einen Lernenden, der `ziel_in_sicht` aus Etappe 2 übernommen hat, bleibt unklar, ob die Variable weiter in die Bedingung gehört oder bewusst herausfällt — ein Satz („`ziel_in_sicht` bleibt heute ungenutzt liegen, sie zahlt erst in Etappe 12") würde die Lücke schließen. In `durchlauf/et3.py` wurde sie entsprechend der Auftragsschritt-15-Anleitung konsequent weggelassen.
- **Kleiner Redaktionsfehler:** Die Lernziele-Nummerierung springt von „7." direkt zu „7b.", „7c.", „7d.", „7e." und dann zu „8." — eine „7a." fehlt. Rein kosmetisch, aber ein Beleg dafür, dass die Liste nachträglich erweitert wurde, ohne die Nummerierung zu prüfen.
- **„Neue Syntax heute" vs. `SYNTAX.md`:** vollständig deckungsgleich für alle drei Portionen.
- **Besonders stark:** Die explizite Vier-Zeilen-Frageform für Hilfegesuche („Was ich will / Was passiert / Was ich ausgeschlossen habe / Was ich vermute") vor der Knobelstelle ist ein didaktisch kluger Kompromiss zwischen „allein lassen" und „im Stich lassen".
- **Code gegen Etappe geprüft:** Alle Selbsttest-Punkte aus 3a/3b/3c wurden gegen `et3.py` verifiziert (siehe Testläufe) und bestehen, einschließlich der Sonderfälle „zehnmal `status`" (keine Wirkung auf Runde/Integrität) und „`kern_integritaet = 150`" (Balken läuft sichtbar aus dem Rahmen, unkorrigiert wie gefordert).

**C – Inhalt gegen Anspruch.** Die drei zentralen Versprechen der Etappe — „Nach 3a wartet dein Programm auf dich. Nach 3b kannst du mit ihm reden. Nach 3c kannst du verlieren." — sind alle drei verifiziert eingelöst. „Spätere Wellen haben mehr Gegner als frühe" ist mit der gewählten Formel (`gegner = welle`) erfüllt. Die Prämisse aus dem Lehrplan („alle vier Marines stehen immer auf dem Feld") gilt hier erwartungsgemäß noch nicht — das ist im Lehrplan selbst ausdrücklich erst ab Etappe 11 vorgesehen und wird in dieser Etappe an keiner Stelle fälschlich behauptet. Keine Diskrepanz.

---

### Etappe 4 — Ausrüstung und Beute

**Code:** `durchlauf/et4.py` (getestet: Inventar/Vorfeld-Mechanik, Befehlsumbau auf zwei Wörter, 20-Wellen-Lauf, gezielter Test auf Positions-Überlauf der Anmarschbahn)

**A – Anfängerperspektive.** Schritt 2 (Befehlsumbau auf zwei Wörter) war tatsächlich der schwerste Punkt, wie angekündigt — das Muster aus Konzept 12 (leere Eingabe zuerst abfangen, dann `wort1`/`wort2` mit Vorbelegung) war aber präzise genug beschrieben, dass sich die Umsetzung ohne Umwege ergab. Ein handfester Fund beim tatsächlichen Durchspielen (nicht nur beim Abhaken des Selbsttests): **Die Etappe sagt nirgends, was passiert, wenn ein Gegner das Ende der Anmarschbahn erreicht oder überschreitet.** Die naive, direkt aus Konzept 3b/14 folgende Umsetzung (`bahn_felder[pos] = "K"` für jede Position in `gegner`) stürzt mit `IndexError: list assignment index out of range` ab, sobald ein Gegner weiter vorrückt, als die Bahn lang ist — reproduzierbar z. B. durch mehrfaches `nachladen`, während Gegner stehen bleiben (siehe Testlauf: Welle 15, elftes `nachladen` in Folge). Ein Schutz vor dem Absturz (Position nur zeichnen, wenn sie im gültigen Bereich liegt) behebt den Crash, erzeugt aber ein neues, stilles Problem: Der betroffene Gegner wird unsichtbar, meldet sich aber weiterhin mit „Die Brut schlägt zurück." — der Spieler sieht eine leere Bahn und nimmt trotzdem Schaden. Als Anfänger, der nur dieser Etappe folgt, gibt es keinen Hinweis darauf, dass dieser Fall existiert oder wie er behandelt werden soll.

**B – Professionelle Perspektive.**
- **Wichtigster Fund:** Die unter A beschriebene Lücke ist kein Rand­fall, sondern eine direkte Folge der in dieser Etappe selbst geforderten Vollständigkeit — Auftragsschritt 10 verlangt ausdrücklich, „eine ganze Welle" zu spielen, und die Formel für die Gegnerzahl wächst mit der Wellennummer, sodass spätere, längere Wellen den Fall zwangsläufig provozieren. Die Etappe legt weder eine Bahnlänge fest noch eine Regel für „Gegner erreicht das Tor", obwohl genau diese Randprüfung in Etappe 14a (`raster[y][x]`, „die Randprüfung … vor jedem Zugriff") als zentrales Konzept eingeführt wird — hier in der eindimensionalen Vorstufe fehlt ihr Gegenstück komplett. Eine Zeile wie *„Was passiert, wenn ein Gegner das Tor erreicht? Notier es dir — die Antwort ist erst ab Etappe 13/14 dran"* würde die Lücke wenigstens benennen, so wie es die Etappe an vielen anderen Stellen vorbildlich für andere offene Fragen tut.
- **Kleinere Ambiguität:** Ob `nimm`/`ablege` eine Runde kosten, wird nirgends festgelegt — anders als bei `status`/`feuern`/`nachladen`/`beenden` in Etappe 3b, wo es eine eigene Tabelle dafür gibt. `durchlauf/et4.py` behandelt sie als kostenlos (Auskunft/Handlung außerhalb des Kampfgeschehens), das ist aber eine eigene Interpretation, keine vom Guide vorgegebene.
- **„Neue Syntax heute" vs. `SYNTAX.md`:** deckungsgleich.
- **Besonders stark:** Die Tabelle „Wo *ist* ein Gegner?" (Design-Entscheidung 2) ist eine der klarsten Gegenüberstellungen im ganzen bisherigen Material — sie macht eine abstrakte Modellierungsfrage an fünf sehr konkreten Zeilen greifbar. Ebenso stark: das dreiteilige „Vor dem Umbau"-Ritual, das hier zum ersten Mal explizit eingeführt wird und für den Rest des Plans angekündigt ist.
- **Code gegen Etappe geprüft:** Alle Selbsttest-Punkte bestehen; der oben beschriebene Grenzfall liegt außerhalb dessen, was der Selbsttest explizit prüft (er verlangt nur „korrekt gezählt", nicht „bei jeder erreichbaren Spiellänge korrekt").

**C – Inhalt gegen Anspruch.** Das zentrale Versprechen der Etappe — „die Darstellung ist ab heute ein Debugging-Werkzeug … ein Fehler, den man sieht, ist ein Fehler, den man findet" (Konzept 15, im Bogen wiederholt) — wird durch den unter A/B beschriebenen Fall ausgerechnet unterlaufen: Hier *versteckt* die notwendig gewordene Absturzsicherung einen Fehlerzustand, statt ihn zu zeigen. Das ist keine böswillige Absicht der Etappe, sondern eine Lücke an der Grenze ihres eigenen Anspruchs. Alle übrigen Versprechen — Inventar, Vorfeld, `gegner` als reine Positionsliste ohne Zeichen, Anmarschbahn als Bild statt Zustand — sind sauber eingelöst und im Test verifiziert.

---

### Etappe 5 — Der Vorposten und das Depot

**Code:** `durchlauf/et5.py` (getestet: Sektorenkarte/Bewegung, Depot mit Kauf/Verkauf, Vorrat/Magazin-Trennung, Stufentabelle, Grundriss)

**A – Anfängerperspektive.** Die größte Etappe bisher, aber die Aufteilung in „Schritt 1–9" und „Schritt 10–17" mit explizitem Commit-Punkt dazwischen hat sich beim Bauen tatsächlich wie zwei separate, gut verdauliche Abende angefühlt — genau wie angekündigt. Schritt 1 (zwei Verschachtelungsebenen: `sektoren → nachbarn`) und Schritt 11 (`kaufe` mit vier Prüfungen) waren wirklich die aufwendigsten Stellen. Eine echte Unklarheit beim Bauen: Auftragsschritt 14 sagt, „Chitinpanzer und Organe erhöhen jetzt `vorrat`, nicht das Inventar", zeigt aber anders als an praktisch jeder anderen Stelle dieser Etappe **keinen Codeausschnitt**, der zeigt, *wie* dieser Übergang mechanisch passiert — bleibt `nimm chitinpanzer` als Befehl bestehen und schreibt jetzt in `vorrat` statt in `inventar`, oder landet das Material beim Wellenende automatisch im Vorrat, ganz ohne `nimm`? Beide Lesarten sind mit dem bisher Gelernten baubar, sie unterscheiden sich aber deutlich im Spielgefühl. `durchlauf/et5.py` entscheidet sich für „automatisch beim Wellenende", weil das die sauberere Lösung ist und näher an „Aus der Brut fällt nichts, was ein Mensch anlegen kann" liegt — aber es ist eine eigene Interpretation, keine vom Guide vorgegebene.

**B – Professionelle Perspektive.**
- **Bestätigter/verstärkter Fund aus Etappe 4:** Auch hier bleibt für alle neu eingeführten Befehle (`umsehen`, `gehe`, `depot`, `kaufe`, `verkaufe`) offen, ob sie eine Runde kosten. Die Tabelle aus Etappe 3b deckt nur die ursprünglichen vier Befehle ab. Da es sich jetzt um die zweite Etappe in Folge handelt, in der dieselbe Frage unbeantwortet bleibt, ist das kein Einzelfall mehr, sondern eine Lücke, die sich mit jeder neuen Etappe potenziell wiederholt — ein Satz wie „alle Befehle, die nicht in dieser Tabelle stehen, kosten ebenfalls keine Runde, solange nichts anderes gesagt wird" würde das für den Rest des Tutorials ein für alle Mal klären.
- **Kleinere Unschärfe** wie unter A beschrieben: Der Mechanismus, wie Material von „Gegner fällt" zu `vorrat["chitinpanzer"]` wird, ist textlich behauptet, aber nicht gezeigt — ungewöhnlich für einen ansonsten sehr code-nahen Guide.
- **„Neue Syntax heute" vs. `SYNTAX.md`:** deckungsgleich.
- **Besonders stark:** Der Abschnitt „Drei Wörter, die heute nicht durcheinandergeraten dürfen" (Depot/Vorrat/Inventar) plus die „Gesamtübersicht"-Tabelle sind die klarste Modellierungs-Referenz im gesamten bisherigen Material. Ebenso die offene Selbstkritik an den vier parallelen Tabellen (`WAREN`/`VERKAUFSWERTE`/`STAPELBAR`/`ANZEIGENAMEN`) als „geplante Not" mit festem Rückzahlungstermin (Etappe 11c/22) — das nimmt dem Lernenden die berechtigte Sorge, hier schlampig zu bauen.
- **Code gegen Etappe geprüft:** Alle geprüften Selbsttest-Punkte bestehen (Kern ohne `integritaet` stürzt bei `umsehen` nicht ab, `kaufe`/`verkaufe` mit allen drei Fehlerfällen, Architektur-Erweiterbarkeit durch reines Datenwörterbuch, Nachlade-Invariante „Summe steigt nie" hält).

**C – Inhalt gegen Anspruch.** Das zentrale Versprechen — „eine neue Ware ins Depot legen, ohne die Kauflogik anzufassen" — ist strukturell eingelöst: `kaufe` enthält keinen einzigen Warennamen, alles läuft über `WAREN`/`STAPELBAR`. Der Wirtschaftskreislauf „Brut fällt → Material → verkaufen → Vaporium → kaufen → Munition" wurde im Test tatsächlich einmal vollständig durchlaufen (siehe Testlauf: Chitinpanzer verkauft, Vaporium gestiegen). Die explizit versprochene „Sperre" — `klassengeraet` gehört nicht ins Depot — wird eingehalten. Keine Diskrepanz zwischen Anspruch und Umsetzung gefunden.

---

### Etappe 6 — Liste, Dictionary, Set, Tuple

**Code:** `durchlauf/et6.py` (getestet: KLASSEN-Validierung, Gegnertypen mit parallelen Listen, `feuern` mit `.index()`-Zielsuche, Schnellfeuer, Ausbauten/Freischaltungen, Bestiarium mit allen drei Meldungsfällen)

**A – Anfängerperspektive.** Schritt 9b/9c (Gegner bekommen einen Typ, paralleles Entfernen) waren tatsächlich die schwersten Stellen, aber die Warnungen im Guide (Invariante aufschreiben, Debugzeilen bis Schritt 15 stehen lassen) haben genau die Fehler verhindert, vor denen gewarnt wurde. Zwei konkrete Funde beim tatsächlichen Bauen:

1. **`magazin_groesse` — ein Wert, der zwischen zwei Etappen nicht zusammenpasst.** Etappe 5, Schritt 12b, lässt den Startwert bewusst offen („`magazin_groesse` als festen Wert" — keine Zahl genannt). `durchlauf/et5.py` hat sich für 8 entschieden. Etappe 6, Schritt 7, sagt dann aber: „`grossmagazin` setzt `magazin_groesse` **von 40 auf 60**" — als wäre 40 der Wert, den Etappe 5 vorgegeben hätte. Das ist sie nicht. Wer in Etappe 5 einen anderen Wert gewählt hat als 40 (und es gab keinen Grund, gerade 40 zu wählen), liest hier einen Satz, der nicht zum eigenen Programm passt. `durchlauf/et6.py` korrigiert den Wert deshalb rückwirkend auf 40, mit Kommentar — genau die Art Stille-Korrektur, vor der die Tutorial-eigene Philosophie („zwei Wahrheiten über dieselbe Sache") warnt, hier aber selbst passiert.
2. **`schalte frei <kennung>` ist ein Drei-Wort-Befehl** in einem Befehlssystem, das Etappe 4 ausdrücklich als „Verb + Ziel", also **zwei** Wörter, festgelegt hat (`kaufe medkit`, `nimm vaporium`). „schalte frei grossmagazin" hat drei Token. Das lässt sich lösen (z. B. `ziel` fest auf `"frei"` prüfen und ein drittes Token für die Kennung einführen, wie in `et6.py` umgesetzt), aber die Etappe erwähnt an keiner Stelle, dass sie hier von der eigenen, vorher fest etablierten Befehlsgrammatik abweicht.

**B – Professionelle Perspektive.**
- **Wichtigster Fund:** siehe A.1 — ein cross-etappen-Zahlenkonflikt, der bei sorgfältiger Lösungsprobe (Etappe 5 tatsächlich bauen, dann Etappe 6 lesen) sofort auffällt. Behebbar mit einer Zeile in Etappe 5: „Nimm als Startwert **40**" statt „einen festen Wert".
- **Zweiter Fund:** siehe A.2 — die Drei-Wort-Form von `schalte frei` bricht mit der in Etappe 4 als verbindlich dargestellten Zwei-Wort-Grammatik, ohne dass die Etappe das kommentiert. Für einen Lernenden, der seine Befehlsverarbeitung strikt nach dem Muster aus Etappe 4 (`befehl`, `ziel` aus genau zwei Token) gebaut hat, ist das ein echter Stolperstein, der eine dritte Zerlegung erfordert.
- **„Neue Syntax heute" vs. `SYNTAX.md`:** deckungsgleich.
- **Besonders stark:** Die „Entscheidungshilfe — vier Fragen, feste Reihenfolge" ist der bislang beste Syntheseabschnitt des gesamten Tutorials; sie bündelt sechs Etappen Modellierungswissen in vier Zeilen und wird sofort an eigenen Daten nachgeprüft. Ebenso stark: Entscheidung 1 (paralleles Entfernen) wird bewusst **ohne** Empfehlung präsentiert — ungewöhnlich für diesen Guide, der sonst gerne rät, und hier genau richtig, weil beide Varianten wirklich gleichwertig sind (entspricht der eigenen Regel aus `MENTOR.md` für Design-Fragen).
- **Code gegen Etappe geprüft:** Die Invariante „`len(gegner)` == `len(gegner_typen)` nach jeder Änderung" hält im Test über mehrere Wellen und Schnellfeuer-Doppelschüsse. Alle drei Bestiarium-Meldungsfälle (unbekannt / gesehen, aber keine Daten / vollständig) wurden einzeln verifiziert.

**C – Inhalt gegen Anspruch.** Das Bestiarium wird wie versprochen zur „ersten Sache, die sich über Wellen hinweg merkt" — `gesehene_gegnertypen` überlebt den Wellenwechsel im Test korrekt, Erstbegegnung liefert den langen Text, jede weitere den kurzen. Die Anmarschbahn zeigt wie versprochen unterschiedliche Zeichen je Typ. Das Set als „Regel statt Prüfung" bei Freischaltungen ist strukturell korrekt (ein zweiter `schalte frei`-Versuch kann nicht doppelt abbuchen, weil die Prüfung `ziel in freigeschaltet` vor der Abbuchung steht). Keine Diskrepanz zwischen Anspruch und Umsetzung über die unter A/B genannten Punkte hinaus.

---

### Etappe 7 — Aufräumen

*(folgt)*

---

## Teil 3 — Gesamtbericht

*(wird nach Abschluss aller Etappen ergänzt)*
