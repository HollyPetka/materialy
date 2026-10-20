# Bonus 4 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Teplotní skok. Uživatel postupně zadá sedm denních teplot
#     (klidně i záporných). Najdi a vypiš největší skok mezi dvěma
#     sousedními dny – tedy největší rozdíl teplot ze dne na den
#     (bez ohledu na to, jestli teplota stoupla, nebo klesla).


predchozi = int(input("Zadej teplotu: "))
nejvetsi_skok = 0


for den in range(6):
	teplota = int(input("Zadej teplotu: "))
	skok = abs(teplota - predchozi)
	if skok > nejvetsi_skok:
		nejvetsi_skok = skok
	predchozi = teplota
print("nejvetsi skok:", nejvetsi_skok)