# Cvičení 6 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# V nádrži je 45 litrů vody a každou minutu z ní uteče 3 litry.
#    Po každé minutě vypiš, kolik vody zbývá, a nakonec vypiš,
#    po kolika minutách je nádrž prázdná.


voda = 45
cas = 0

while voda > 0:
	voda = voda - 3
	cas = cas + 1
	print("Po", cas, "minutách zbývá", voda, "litrů.")
print ("nadrz je prazdná po", cas ,"minutách")