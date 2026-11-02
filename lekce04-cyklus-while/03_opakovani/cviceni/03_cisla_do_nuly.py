# Cvičení 3 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadává čísla tak dlouho, dokud nezadá 0. Nakonec vypiš
#    jejich součet, kolik jich bylo a jejich průměr zaokrouhlený
#    na jedno desetinné místo. (Nápověda: round(cislo, 1))

soucet = 0
pocet = 0
cislo = int(input("zadej cislo - kde zadana 0 znamena konec: "))

while cislo != 0:
	soucet =  soucet + cislo
	pocet = pocet +1
	cislo = int(input("zadej cislo - kde zadana 0 znamena konec: "))

if pocet == 0:
	print("nezadano zadne cislo")
else:
	print("soucet:", soucet)
	print("pocet:", pocet)
	print("prumer:", round(soucet/pocet, 1))
