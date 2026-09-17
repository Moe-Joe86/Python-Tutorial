# Fehlertagebuch

Format: Symptom — wie gefunden.

- **Etappe 2:** Bei ungültiger Klassenwahl (`9`) stürzte das Programm nach der freundlichen Fehlermeldung trotzdem mit `NameError: name 'schaden' is not defined` ab, weil die Anzeige der Klassenwerte direkt im Anschluss an die `if`/`elif`/`else`-Kette stand, ohne zu prüfen, ob überhaupt ein gültiger Zweig gelaufen war — gefunden durch tatsächliches Ausführen mit der Testeingabe `9`, wie es der Auftrag selbst verlangt (nicht durch Lesen).
- **Etappe 4:** Bei mehrfachem `nachladen` ohne `feuern` wanderten Gegnerpositionen über das Ende der Anmarschbahn hinaus; ohne Schutz hätte das einen `IndexError` beim Zeichnen der Bahn ausgelöst — gefunden durch gezieltes Ausprobieren des Grenzfalls (viele `nachladen` hintereinander), nicht durch Lesen des Codes.
- **Etappe 7 (Fund 1):** `zeige_status()` zeigte nach dem Umbau in eine Funktion dauerhaft „Kern [..........] 0%", weil `kern_integritaet` und `trefferpunkte` beim Herauslösen als Parameter vergessen wurden — ein reiner Typ-3-Fehler, kein Absturz. Gefunden durch stichprobenartiges Ausführen von `status` nach dem Umbau (`p`-Äquivalent: einfaches Hinsehen auf die Ausgabe).
- **Etappe 7 (Fund 2, der wichtigere):** Nach dem Umbau erschien bei jeder leeren Eingabe zusätzlich eine Zeile mit der Anmarschbahn, die vorher nicht da war — ein Verhaltensunterschied, unsichtbar beim normalen Durchspielen. **Gefunden ausschließlich durch den vorgeschriebenen Charakterisierungstest** (`python et6.py < befehle.txt > vorher.txt`, Umbau, `python et7.py < befehle.txt > nachher.txt`, `diff vorher.txt nachher.txt`) — die Methode aus Etappe 7 hat hier tatsächlich einen Fehler gefunden, den kein manuelles Durchspielen gefunden hätte.

## Bug-Jagd, Etappe 8: zwei injizierte Fehler

Zwei Sabotagen wurden absichtlich in eine Kopie von `et7.py` eingebaut und mit `diff` gegen das Original plus gezieltem Testen aufgespürt (Details siehe `BERICHT.md`, Etappe 8):

- **Sabotage A (Off-by-One, Typ 3):** In `wechsle_sektor()` wurde `if richtung not in sektor["nachbarn"]:` zu `if richtung in sektor["nachbarn"]:` verdreht (Bedingung invertiert) — die Bewegung meldete danach bei jeder gültigen Richtung „Dort geht es nicht lang" und bei jeder ungültigen einen `KeyError` beim Zugriff auf `sektor["nachbarn"][richtung]`. Gefunden durch Testen von `gehe <gültige Richtung>` und Lesen des Tracebacks von unten nach oben (Tatort: die Zeile mit dem Zugriff, nicht die Bedingung selbst — genau die "Absturzstelle ist selten die Fehlerstelle"-Falle aus Konzept 4).
- **Sabotage B (Tippfehler beim Schlüssel, aber NICHT still — Korrektur einer eigenen Fehlannahme):** In `kaufe()` wurde `vorrat["vaporium"] -= gesamtpreis` zu `vorrat["vaporum"] -= gesamtpreis` verschrieben. Erwartet war (nach Etappe 5, Konzept 2) ein stiller Typ-3-Fehler, der klammheimlich einen neuen Schlüssel anlegt. **Tatsächlich stürzte das Programm beim ersten Kauf sofort mit `KeyError: 'vaporum'` ab.** Grund: `-=` ist eine Abkürzung für `vorrat["vaporum"] = vorrat["vaporum"] - gesamtpreis` — die rechte Seite **liest** den Schlüssel zuerst, und Lesen eines nicht existierenden Schlüssels stürzt ab (Etappe 5, Konzept 2), im Gegensatz zur reinen Zuweisung `vorrat["vaporum"] = 40`, die anlegt statt zu lesen. Gefunden durch Ausführen und Lesen des Tracebacks von unten nach oben — die eigene Vorhersage war falsch, und genau das Ritual (vorhersagen → ausführen → vergleichen → erklären) hat das aufgedeckt.

## Bug-Jagd II, Etappe 16: drei vollständig dokumentierte Funde

**Fund 1 — `nachladen_noetig`, ein seit Etappe 7 totes, aber harmloses Flag (Fahndungsliste #10).**
- *Beobachtung:* `marine.nachladen_noetig` wird gesetzt und zurückgesetzt, aber im aktuellen Code (`et16.py`) nirgends gelesen.
- *Hypothese:* Beim Funktions-Refactor in Etappe 7 ist eine Prüfung verlorengegangen.
- *Experiment (Bisektion über die eigenen Etappen-Snapshots statt `git bisect`):* `et3.py` bis `et11.py` nacheinander nach `nachladen_noetig` durchsucht. Ergebnis: `et3.py`–`et6.py` enthalten noch `if munition > 0 and not nachladen_noetig:`; ab `et7.py` lautet dieselbe Stelle nur noch `if geladen > 0 and len(gegner) > 0:` — die Prüfung verschwand exakt beim großen Umbau in Etappe 7.
- *Zweite Hypothese, geprüft:* War das ein echter Verhaltensfehler, den der Etappe-7-`diff`-Beweis hätte finden müssen? **Nein** — `nachladen_noetig` ist durch seine eigene Pflege (`True` genau dann, wenn `geladen == 0`; `False` genau dann, wenn danach nachgeladen wird) mit `geladen > 0` immer deckungsgleich. Der Wert war seit seiner Einführung redundant, sein Verschwinden ist folgenlos.
- *Rückwärtsprobe:* Die alte Prüfung (`... and not marine.nachladen_noetig`) probeweise wieder in `et16.py` eingebaut und mit identischen Startwerten getestet — identisches Ergebnis (`Treffer: kriecher. Geladen: 39, Gegner uebrig: 0`). Bestätigt: keine Verhaltensänderung, nur ein totes Attribut. Bleibt unangetastet stehen (heute wird nicht repariert, was nicht kaputt ist).

**Fund 2 — Schadensbonus aus Etappe 15 ist im laufenden Spiel nicht beobachtbar (Auftragsschritt 8).**
- *Beobachtung:* `feuern` meldet nach einem Treffer nur „Treffer: <Typ>", nie eine Schadenszahl. Companions' automatisches Feuern meldet ebenfalls keinen Wert.
- *Hypothese:* Ein Tippfehler in `SCHWACHPUNKTE` (z. B. `"chitin_analysiret"` statt `"chitin_analysiert"`) würde deshalb unbemerkt bleiben.
- *Experiment:* `SCHWACHPUNKTE["kriecher"]` probeweise auf den falschen Schlüssel gesetzt, `berechne_schaden()` einmal mit der korrekten Erkenntnis im Set aufgerufen. Ergebnis: `10` — identisch zum Aufruf ganz ohne jede Erkenntnis (ebenfalls `10`, erwartet worden wäre `15`).
- *Rückwärtsprobe:* Tippfehler korrigiert, derselbe Aufruf liefert `15`. Der Unterschied existiert also nur im Rückgabewert der Funktion, nie in einer für den Spieler sichtbaren Ausgabe.
- *Schluss (wichtiger als der Tippfehler selbst):* „Die Wirkung dieser Mechanik ist im laufenden Spiel nicht beobachtbar." Weder ein korrekter noch ein falscher Schwachpunkt-Eintrag würde einem Spieler je auffallen, weil nirgends ein Schadenswert angezeigt wird.

**Fund 3 (Kontrollbefund, keine echte Abweichung) — Phasenreihenfolge des Ticks.**
- *Beobachtung:* Zwei Phasen im Tick (Trupp/Gegner) vertauscht, dieselbe Startlage (ein Kriecher bereits am Tor, 12 TP, Kamerad+Turm mit insgesamt 14 Schaden) zwei Ticks laufen lassen.
- *Hypothese:* Bei „Gegner zuerst" schlägt der Gegner im ersten Tick zu, bevor er stirbt — die Kernintegrität muss niedriger sein als bei „Trupp zuerst".
- *Experiment:* Beide Reihenfolgen mit identischem Code und identischen Startwerten ausgeführt.
- *Ergebnis:* „Trupp zuerst" (die tatsächlich gebaute Reihenfolge): Kernintegrität `95`. „Gegner zuerst": Kernintegrität `90`. Die Hypothese war richtig — und bestätigt exakt das Zahlenbeispiel aus der Etappe selbst (Konzept 1).
- *Rückwärtsprobe:* Reihenfolge zurückgetauscht, Ergebnis wieder `95`. Kein Fehler im eigentlichen Sinn (beide Reihenfolgen sind laut Guide vertretbar), aber der Beweis, dass die Wahl der Reihenfolge eine echte, messbare Spielkonsequenz hat.
