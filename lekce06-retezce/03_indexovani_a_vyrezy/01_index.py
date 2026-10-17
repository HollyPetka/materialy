# ---------------------------------------------
#  Index: jeden znak z textu
# ---------------------------------------------
# Spusť soubor. Na konci schválně spadne – tu chybu si přečti.

slovo = "PyLadies"


# Každý znak má svoje pořadové číslo, kterému se říká index.
# Počítá se od nuly, takže první písmeno má index 0:
print(slovo[0])
print(slovo[1])
print(slovo[2])


# Poslední index je proto o jedna menší než délka:
print(len(slovo))
print(slovo[7])


# Od konce se dá počítat záporně a je to kratší:
print(slovo[-1])
print(slovo[-2])


# Index, který v textu není, skončí chybou IndexError:
print(slovo[8])
