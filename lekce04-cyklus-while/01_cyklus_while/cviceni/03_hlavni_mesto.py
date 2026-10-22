# Cvičení 3 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se uživatele "Jaké je hlavní město Česka? " tak dlouho,
#    dokud nenapíše "Praha". Pak vypiš "Správně!".


while True:
	dotaz = input("jake je hlavni mesto ceska? ")
	if dotaz =="praha" or dotaz =="Praha" or dotaz =="PRAHA":
		print("spravne!")
		break
	else:
		print("odpoved nespravna, ale nevadi, zkus to znovu")
print("sikula!")