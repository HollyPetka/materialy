# ---------------------------------------------
#  Hledání v textu
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

slovo = "PyLadies"


# Zápis in znáš z cyklů, kde hledal jedno písmeno. Zvládne i delší kus:
print("Ladies" in slovo)
print("ladies" in slovo)

# Velikost písmen rozhoduje. Když ti nemá vadit, převeď text na malá:
print("ladies" in slovo.lower())


# Na začátek a konec textu jsou metody:
soubor = "prezentace.pdf"

print(soubor.endswith(".pdf"))
print(soubor.startswith("prez"))


# Hodí se to v podmínce:
if soubor.endswith(".pdf"):
    print("Tohle je PDF.")
