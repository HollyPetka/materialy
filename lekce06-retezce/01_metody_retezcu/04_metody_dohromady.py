# ---------------------------------------------
#  Metody za sebou
# ---------------------------------------------
# Spusť soubor a zkus různé odpovědi: ano, ANO, nebo ano s mezerou.
#
# V lekcích 2 a 4 jsi odpověď porovnávala přímo:
#   if odpoved == "ano":
# Taková podmínka projde jen u přesně napsaného "ano". "ANO" ani " ano "
# už neprojdou, i když uživatelka myslela to samé.

odpoved = input("Chceš pokračovat? (ano/ne) ")

upravena = odpoved.strip().lower()
print("[" + upravena + "]")

if upravena == "ano":
    print("Pokračujeme.")
else:
    print("Končíme.")


# Dvě metody se dají napsat za sebe na jeden řádek. Vyhodnocuje se to
# zleva doprava:
#   odpoved.strip()    nejdřív zmizí mezery na krajích
#   .lower()           z toho výsledku pak vzniknou malá písmena
#
# Totéž po krocích, kdyby to bylo přehlednější:
bez_mezer = odpoved.strip()
mala = bez_mezer.lower()
print(mala)
