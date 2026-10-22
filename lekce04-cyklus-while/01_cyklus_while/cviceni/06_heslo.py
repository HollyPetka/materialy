# Cvičení 6 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se na heslo. Když uživatel zadá "pyladies", vypiš "Vítej!"
#    a skonči. Když se splete třikrát, vypiš "Zablokováno." a skonči taky.
#    Z cyklu se v obou případech dostaneš příkazem break.



pokus = 0
while True:
	zadej_heslo = input("zadej heslo ")
	pokus = pokus + 1
	if zadej_heslo == "pyladies":
		print("vitej")
		break
	if pokus == 3:
		print("zablokovano")
		break
	print("spatne zkus to znovu")
	
