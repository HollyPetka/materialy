# Cvičení 5 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Sleva na vstupné. Slevu mají děti (do 18 let) a senioři (65 a víc).
#    Navíc mají v pondělí slevu úplně všichni.
#    Zeptej se na věk a na den a vypiš "Máš slevu." / "Plné vstupné.".


vek = int(input("kolik ti je let? "))
den = input("den? ")

if vek < 18 or vek >= 65 or den == "pondeli":
	print("mas slevu")
else:
	print("plne vstupne")