# Cvičení 6 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Vypočítej 2 na desátou tak, že v cyklu desetkrát vynásobíš dvěma.
#    Výsledek vypiš (má vyjít 1024).


vypocet = 1
for nasobeno in range (10):
	vypocet = vypocet *2
	print("kolo", nasobeno + 1 ,":" , vypocet)
print("vysledek ", vypocet)
