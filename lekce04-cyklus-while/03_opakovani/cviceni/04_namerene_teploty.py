# Cvičení 4 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadává naměřené teploty. Po každé se zeptej
#    "Další? (ano/ne) ". Až odpoví "ne", vypiš nejvyšší teplotu.


otazka_teplota = int(input("zadej namerenou teplotu: "))

while True:
	nasledujici = input("dalsi?  ano/ne ")
	if nasledujici == "ne":
		break
	teplota = int(input("zadej teplotu "))
	if teplota > otazka_teplota:
		otazka_teplota = teplota

print ("nejvetsi teplota byla:", otazka_teplota)