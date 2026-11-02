# Cvičení 5 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# Načítej od uživatele čísla tak dlouho, dokud nezadá záporné číslo.
#    Pak vypiš, kolik čísel stihl zadat.

kolik = 0
cislo = int(input("zadej cislo:" ))
while cislo >=0:
	kolik = kolik +1
	cislo = int(input("zadej cislo:" ))
print("pocet zadaných čísel před minusovým cislem je:", kolik)