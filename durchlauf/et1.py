# Etappe 1: Der Abwurf
# Namen der Variablen: durchgehend deutsch, ohne Umlaute (Entscheidung siehe GELERNT.md)
# Klasse wird als Zahl gespeichert, nicht als Name (Entscheidung siehe GELERNT.md) -
# eine Zahl in einen Namen umzuwandeln braeuchte if, das kommt erst in Etappe 2.

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
klassenwahl_text = input("Klasse (1-4): ")
klasse = int(klassenwahl_text)

print(f"Klasse gewaehlt: {klasse}")

input("Druecke Enter, um dich per Funk zu melden.")
print(f"Funkspruch gesendet. Antwort: {letzte_meldung}")
