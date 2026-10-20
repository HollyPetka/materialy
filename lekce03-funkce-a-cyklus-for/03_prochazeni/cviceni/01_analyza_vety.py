# Cvičení 1 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Analýza věty. Uživatel zadá větu. Projdi ji znak po znaku a vypiš
#    počet znaků, počet samohlásek, počet mezer a počet slov ve větě.
#    (Počet slov = počet mezer + 1.)


veta = input("zadej vetu: ")

pocet_samohlasek = 0
pocet_mezer = 0
pocet_souhlasek = 0


for pismeno in veta:
	if pismeno == " ":
		pocet_mezer = pocet_mezer + 1
	if pismeno in "aeiouyAEIOUY":
		pocet_samohlasek = pocet_samohlasek + 1
	if pismeno not in "aeiouyAEIOUY .,?!":
		pocet_souhlasek = pocet_souhlasek + 1
print("pocet samohlasek: ", pocet_samohlasek)
print("pocet souhlasek: ", pocet_souhlasek)
print("pocet mezer: ", pocet_mezer)
print("pocet slov: ", pocet_mezer + 1)
print("pocet znaku: ", len(veta))


