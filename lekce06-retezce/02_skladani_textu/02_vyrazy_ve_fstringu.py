# ---------------------------------------------
#  Co může být ve složených závorkách
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

cena = 100
jmeno = "anna"
slovo = "PyLadies"


# Nejen proměnná. Do závorek jde i výpočet:
print(f"Cena s DPH: {cena * 1.21}")

# Metoda z minulé složky:
print(f"Velkými písmeny: {jmeno.upper()}")

# Vestavěná funkce:
print(f"Počet písmen: {len(slovo)}")

# Nebo porovnání, které vrátí True/False:
print(f"Je to nad pět stovek? {cena > 500}")


# Do textu se doplní výsledek, ne ten zápis ze závorek.
