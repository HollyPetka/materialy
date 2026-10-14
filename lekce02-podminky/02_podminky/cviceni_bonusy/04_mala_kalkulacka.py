# Bonus 4 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Malá kalkulačka.
#     Zeptej se na dvě čísla a na znaménko (+, -, *, /).
#     Podle znaménka vypiš výsledek správné operace.
#     Bonus v bonusu: ošetři dělení nulou vlastní hláškou.


a = int(input("dej mi prvni cislo "))
b = int(input("dej mi druhe cislo ")) 
znak = input("dej mi znamenko ((+, -, *, /) ") 

if znak == "+":
	print(a+b)
elif znak == "-":
	print(a-b)
elif znak == "*":
	print(a*b)
elif znak == "/":
	print(a/b)
else:
	print("nelze delit nulou")


