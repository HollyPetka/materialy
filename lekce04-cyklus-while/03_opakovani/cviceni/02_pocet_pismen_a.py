# Cvičení 2 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá slovo. Spočítej, kolikrát se v něm objeví
#    písmeno "a", a výsledek vypiš.


slovo = input("zadej slovo: ")
pocet = 0
for pismeno in slovo:
	if pismeno == "a" or pismeno =="A":
		pocet = pocet + 1 
print ("ve",slovo,"je",pocet,"x","pismeno a")
