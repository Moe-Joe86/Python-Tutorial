# Etappe 3: Die Wellenschleife (3a, 3b, 3c)
# Namen der Variablen: durchgehend deutsch, ohne Umlaute
# Klasse wird als Zahl gespeichert
# Befehle sind einwortig (Design-Entscheidung, Umbau auf Verb+Ziel folgt in Etappe 4)
# Beenden-Befehl heisst "beenden"
# runde liegt auf Ebene 1 (ganzes Spiel), nicht pro Welle - so zaehlt sie insgesamt gespielte Runden

kopf = """
  /------------\\
 |  VORPOSTEN   |
 ----------------
"""
print(kopf)

name = input("Wie heisst du, Marine? ")
print(f"Willkommen, {name}.")

kern_integritaet = 100
trefferpunkte = 100
munition = 40
vaporium = 0
rekruten_verfuegbar = 0
wellen_bis_evakuierung = 20

print(f"Kernintegritaet: {kern_integritaet}%")
print(f"Trefferpunkte: {trefferpunkte}")
print(f"Munition: {munition} Schuss")
print(f"Vaporium: {vaporium}")
print(f"Rekruten verfuegbar: {rekruten_verfuegbar}")
print(f"Wellen bis Evakuierung: {wellen_bis_evakuierung}")

letzte_meldung = "Hier Aussenposten Sieben. Bitte um Bestaetigung, over."
print(f"Aufgezeichnete Durchsage: {letzte_meldung}")

print("Waehle deine Klasse:")
print("1 Soldat")
print("2 Heavy")
print("3 Engineer")
print("4 Medic")
klassenwahl_text = input("Klasse (1-4): ").strip()
klasse = int(klassenwahl_text)

klasse_gueltig = False
if klasse == 1:
    trefferpunkte = 100
    schaden = 10
    panzerung = 5
    klassengeraet = "Sturmgewehr"
    klasse_gueltig = True
elif klasse == 2:
    trefferpunkte = 140
    schaden = 14
    panzerung = 10
    klassengeraet = "Schweres MG"
    klasse_gueltig = True
elif klasse == 3:
    trefferpunkte = 90
    schaden = 7
    panzerung = 4
    klassengeraet = "Multiwerkzeug"
    klasse_gueltig = True
elif klasse == 4:
    trefferpunkte = 80
    schaden = 6
    panzerung = 3
    klassengeraet = "Bio-Injektor"
    klasse_gueltig = True
else:
    print("Diese Klasse gibt es nicht.")

if klasse_gueltig:
    print(f"Klasse:        {klasse}")
    print(f"Trefferpunkte: {trefferpunkte}")
    print(f"Schaden:       {schaden}")
    print(f"Panzerung:     {panzerung}")

print("Auf dem Radar bewegt sich etwas, das dort nicht hingehoert.")
funk_antwort = input("Melden? (ja/nein) ").strip()
meldung_abgesetzt = funk_antwort == "ja"
print(f"Meldung abgesetzt: {meldung_abgesetzt}")

# Der einzelne Schuss aus Etappe 2 wandert ab jetzt in den Befehl "feuern" weiter unten.

nachladen_noetig = False
erfahrung = 0
runde = 1
spiel_laeuft = True

for welle in range(1, wellen_bis_evakuierung + 1):
    if not spiel_laeuft:
        break

    print(f"--- Welle {welle} von {wellen_bis_evakuierung} ---")
    gegner = welle

    while True:
        eingabe = input(f"Welle {welle}, Runde {runde} > ").strip().lower()

        rundenkosten = False

        if eingabe == "status":
            anteil_kern = kern_integritaet / 100
            voll_kern = int(anteil_kern * 10)
            leer_kern = 10 - voll_kern
            balken_kern = "#" * voll_kern + "." * leer_kern

            anteil_marine = trefferpunkte / 100
            voll_marine = int(anteil_marine * 10)
            leer_marine = 10 - voll_marine
            balken_marine = "#" * voll_marine + "." * leer_marine

            anteil_munition = munition / 40
            voll_munition = int(anteil_munition * 10)
            leer_munition = 10 - voll_munition
            balken_munition = "#" * voll_munition + "." * leer_munition

            print(f"Kern     [{balken_kern}] {anteil_kern:.0%}")
            print(f"Marine   [{balken_marine}] {anteil_marine:.0%}")
            print(f"Munition [{balken_munition}] {anteil_munition:.0%}")
            print(f"Erfahrung: {erfahrung}")
        elif eingabe == "feuern":
            if munition > 0 and not nachladen_noetig:
                munition -= 1
                gegner -= 1
                erfahrung += 10
                print(f"Geschossen. Munition uebrig: {munition}, Gegner uebrig: {gegner}")
                if munition == 0:
                    nachladen_noetig = True
            else:
                print("Keine Munition mehr. Erst nachladen.")
            rundenkosten = True
        elif eingabe == "nachladen":
            munition = 40
            nachladen_noetig = False
            print("Nachgeladen.")
            rundenkosten = True
        elif eingabe == "beenden":
            print("Welle wird abgebrochen.")
            break
        else:
            print("Unbekannter Befehl.")

        if rundenkosten:
            runde += 1
            if gegner > 0:
                kern_integritaet -= 5
                trefferpunkte -= 2
                print("Die Brut schlaegt zurueck.")

        if kern_integritaet <= 0:
            print("Die Kernintegritaet ist auf 0 gefallen. Der Vorposten ist verloren.")
            spiel_laeuft = False
            break

        if trefferpunkte <= 0:
            print("Du bist gefallen. Der Lauf ist zu Ende.")
            spiel_laeuft = False
            break

        if gegner <= 0:
            print("Welle geschafft.")
            break

print("Programmende.")
