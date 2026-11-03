# Bonus 1 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Kámen, nůžky, papír – znáš z bonusu v lekci 2, kde hráli
#     dva lidé. Teď to rozšíříme: hraješ proti počítači a na víc kol.
#     - Zeptej se na svůj tah: "kamen", "nuzky" nebo "papir".
#     - Počítač si tah vylosuje: randrange(1, 4) vrátí 1, 2 nebo 3,
#       tak si to číslo přelož na tah (1 = kamen, 2 = nuzky, 3 = papir).
#     - Vypiš, co hrál počítač, a kdo kolo vyhrál.
#     - Pak se zeptej "Hrát znovu? (ano/ne) " a podle odpovědi
#       buď pokračuj, nebo skonči.
#     Kdo koho poráží: kámen tupí nůžky, nůžky stříhají papír,
#     papír balí kámen.
#     Nahoru na první řádek nezapomeň:  from random import randrange
from random import randrange

while True:
	ja = (input("zadej svuj tah - kamen, nuzky, papir: "))

	cislo = randrange(1,4)

	if cislo == 1:
		pocitac = "kamen" 
	elif cislo == 2:
		pocitac = "nuzky"
	else:
		pocitac = "papir"

	print("pocitac hral:", pocitac)

	vyhrala_kamenem = ja == "kamen" and pocitac == "nuzky"
	vyhrala_nuzkami = ja == "nuzky" and pocitac == "papir"
	vyhrala_papirem = ja == "papir" and pocitac == "kamen"

	if ja == pocitac:
		print("remiza")
	elif vyhrala_kamenem or vyhrala_nuzkami or vyhrala_papirem:
		print ("vyhrala jsi")
	else:
		print ("prohrala jsi")

	znovu = input("Hrát znovu? (ano/ne) ")
	if znovu == "ne":
		break

print("Díky za hru!")