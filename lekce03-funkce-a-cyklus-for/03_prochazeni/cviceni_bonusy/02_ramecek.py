# Bonus 2 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Rámeček. Uživatel zadá velikost N. Vnořenými cykly nakresli
#     čtverec N x N, kde okraj tvoří X a vnitřek je prázdný. Pro N=4:
#         X X X X
#         X     X
#         X     X
#         X X X X
#     Zamysli se: na kterém řádku a sloupci se kreslí X a kdy mezera?


velikost = int(input("zadej velikost "))

for radek in range(1, velikost +1):
	for sloupec in range(1, velikost +1):
		if radek == 1 or radek == velikost or sloupec ==1 or sloupec == velikost:
			print("X", end=" ")
		else:
			print(" ", end=" ")
	print()