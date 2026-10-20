# Cvičení 5 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá číslo. Cyklem vypiš jeho malou násobilku –
#    tedy cislo * 1 až cislo * 10, každý řádek třeba "7 * 3 = 21".


ciselko = int(input("zadej cislo z male nasobilky "))

for nasobilka in range(1, 11):
	print(nasobilka, "*", ciselko, "=", ciselko * nasobilka  )
	
