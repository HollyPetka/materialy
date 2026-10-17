# ---------------------------------------------
#  Výřez: víc znaků najednou
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

slovo = "PyLadies"


# Dvojtečka mezi dvěma indexy vybere část textu. Druhé číslo se do výřezu
# nepočítá – stejné pravidlo jako u range:
print(slovo[0:2])
print(slovo[2:8])


# Když první číslo chybí, bere se od začátku:
print(slovo[:2])

# Když chybí druhé, jede se až do konce:
print(slovo[2:])


# Záporné indexy fungují i tady. Poslední tři znaky a všechno kromě nich:
print(slovo[-3:])
print(slovo[:-3])


# Původní text zůstává, jak byl – výřez je nový řetězec:
print(slovo)
