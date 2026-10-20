# Bonus 5 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Palindrom. Uživatel zadá slovo. Zjisti, jestli se čte stejně
#     zepředu i zezadu (třeba "kajak" nebo "radar").
#     Zamysli se, jak si slovo poskládáš pozpátku a jak obě verze porovnáš.


slovo = input("zadej slovo " )
pozpatku = ""



for znak in slovo:
	pozpatku = znak + pozpatku
	print(pozpatku)
if slovo == pozpatku:
	print("palindrom")
else:
	print("neni palindrom")





