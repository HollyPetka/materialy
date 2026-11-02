# Cvičení 5 – Opakování
# Doplň kód pod zadání a soubor spusť (Run).

# Hra "hádej číslo":
#    - Počítač si vylosuje číslo od 1 do 20: randrange(1, 21)
#    - Uživatel hádá. Po každém tipu vypiš "Moc velké." nebo "Moc malé.".
#    - Když trefí, vypiš "Trefa!" a skonči.
#    - Když se netrefí ani na pátý pokus, prozraď číslo a skonči.
#    Nahoru na první řádek nezapomeň:  from random import randrange
from random import randrange

vylosovane_cislo = randrange (1, 21)
pokus = 0

while True:
	hadej = int(input("hadej cislo 1 až 20 "))
	pokus = pokus + 1 

	if hadej == vylosovane_cislo:
		print("trefa!")
		break

	if pokus == 5:
		print("jiz probehlo pet pokusu, hadane cislo bylo ", vylosovane_cislo)
		break

	if hadej > vylosovane_cislo:
		print("moc velke")
	else:
		print("moc male")


