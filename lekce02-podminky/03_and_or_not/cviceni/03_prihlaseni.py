# Cvičení 3 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Přihlášení. Správné jméno je "anna" a správné heslo je "tajne".
#    Zeptej se na jméno i heslo a vypiš "Vítej!", jen když sedí obojí.
#    Jinak vypiš "Špatné údaje.".


jmeno = input("tvoje jmeno? ")
heslo = input("tvoje heslo? ")


if jmeno == "anna" and heslo == "tajne":
	print("vitej!")
else:
	print("spatne udaje")