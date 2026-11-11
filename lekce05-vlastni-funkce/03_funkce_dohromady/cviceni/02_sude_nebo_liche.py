# Cvičení 2 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš dvě funkce:
#    je_sude(cislo) vrátí True, nebo False,
#    popis(cislo) vrátí text "4 je sudé" nebo "7 je liché" a uvnitř
#    se na je_sude zeptá.
#    Pak v cyklu for vypiš popis čísel od 1 do 6.


def je_sude_cislo (cislo):
	return cislo % 2 == 0

def popis(cislo):
	if je_sude_cislo (cislo):
		return str(cislo) + " je sudé"
	else:
		return str(cislo) + " je liché"



for cislo in range(1, 15):
    print(popis(cislo))


