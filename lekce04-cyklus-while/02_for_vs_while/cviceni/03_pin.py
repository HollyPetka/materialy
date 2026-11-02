# Cvičení 3 – For versus while
# Nejdřív rozhodni for/while a napiš si do komentáře proč, pak úlohu naprogramuj.

# Ptej se na PIN tak dlouho, dokud uživatel nezadá "1234".
#    Pak vypiš "Odemčeno!".

pin = input("zadej pin: ")
while pin != "1234":
	print("spatny pin")
	pin = input("zadej pin: ")
print("odemceno!")
