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

*(wird je Etappe ergänzt)*

---

## Teil 3 — Gesamtbericht

*(wird nach Abschluss aller Etappen ergänzt)*
