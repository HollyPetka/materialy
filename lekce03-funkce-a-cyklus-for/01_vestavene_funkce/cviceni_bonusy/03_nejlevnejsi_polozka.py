# Bonus 3 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Cíl a rozpočet. Uživatel zadá cenu tří položek. Vypiš nejlevnější
#     a nejdražší z nich a jestli se všechny tři vejdou do rozpočtu 1000 Kč.


cena1 = int(input("zadej cenu prvni polozky "))
cena2 = int(input("zadej cenu druhe polozky "))
cena3 = int(input("zadej cenu treti polozky "))

cena_prumer = (cena1 + cena2 + cena3) / 3
print (round(cena_prumer))


print("nejdrazsi: ", max(cena1, cena2, cena3))
print("nejlevnejsi:" , min(cena1, cena2, cena3))


if (cena1 + cena2 + cena3) <= 1000:
	print("rozpocet ok")
else:
	print("pozor - rozpocet nok")
