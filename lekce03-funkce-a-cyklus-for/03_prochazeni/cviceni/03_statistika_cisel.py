# Cvičení 3 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Statistika čísel. Uživatel zadá, kolik čísel bude zadávat, a pak
#    ta čísla postupně napíše. V jednom průchodu cyklem spočítej a vypiš
#    jejich součet, průměr, největší a nejmenší číslo.
#    Nepoužívej funkce sum, max ani min – spočítej vše sama cyklem.


pocet_cisel = int(input("kolik cisel zadas? "))
pocet = int(input("zadej cislo: "))

soucet = pocet
nejmensi = pocet
nejvetsi = pocet

for i in range(pocet_cisel -1):
	cislo = int(input("zadej cislo: "))
	soucet = soucet + cislo
	if cislo > nejvetsi:
		nejvetsi = cislo
	if cislo < nejmensi:
		nejmensi = cislo
print("soucet: ", soucet)
print("prumer: ", soucet/pocet_cisel)
print("nejvetsi: ",nejvetsi)
print("nejmensi: ", nejmensi)

