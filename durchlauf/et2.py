# Etappe 2: Der erste Kontakt
# Namen der Variablen: durchgehend deutsch, ohne Umlaute (Entscheidung siehe GELERNT.md)
# Klasse wird als Zahl gespeichert (Entscheidung siehe GELERNT.md, Etappe 1)
# Bezugsfall der Klassenwerte: Soldat (aus dem Guide uebernommen)

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

if klasse == 1:
    trefferpunkte = 100
    schaden = 10
    panzerung = 5
    klassengeraet = "Sturmgewehr"
elif klasse == 2:
    trefferpunkte = 140
    schaden = 14
    panzerung = 10
    klassengeraet = "Schweres MG"
elif klasse == 3:
    trefferpunkte = 90
    schaden = 7
    panzerung = 4
    klassengeraet = "Multiwerkzeug"
elif klasse == 4:
    trefferpunkte = 80
    schaden = 6
    panzerung = 3
    klassengeraet = "Bio-Injektor"
else:
    print("Diese Klasse gibt es nicht.")

print(f"Klasse:        {klasse}")
print(f"Trefferpunkte: {trefferpunkte}")
print(f"Schaden:       {schaden}")
print(f"Panzerung:     {panzerung}")

nachladen_noetig = False
ziel_in_sicht = True

if munition > 0 and not nachladen_noetig and ziel_in_sicht:
    munition = munition - 1
    print(f"Geschossen. Munition uebrig: {munition}")
else:
    print("Feuern nicht moeglich.")

print("Auf dem Radar bewegt sich etwas, das dort nicht hingehoert.")
funk_antwort = input("Melden? (ja/nein) ").strip()
meldung_abgesetzt = funk_antwort == "ja"
print(f"Meldung abgesetzt: {meldung_abgesetzt}")
