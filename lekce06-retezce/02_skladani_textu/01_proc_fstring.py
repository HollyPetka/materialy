# ---------------------------------------------
#  Proč f-string
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.

jmeno = "Anna"
vek = 30


# Takhle se text skládal doteď – plusem:
print("Je mi " + str(vek) + " let")

# Číslo musí projít přes str(), jinak řádek spadne na TypeError.
# A mezery si hlídáš sama:
print("Ahoj" + jmeno)


# f-string: před uvozovky napiš f a proměnnou dej do složených závorek.
print(f"Je mi {vek} let")
print(f"Ahoj {jmeno}")

# Python si hodnotu ze závorek doplní do textu. Číslo si převede sám
# a mezery jsou tam, kde je napíšeš.


# Stejná věta dvakrát:
print("Ahoj " + jmeno + ", je ti " + str(vek) + " let.")
print(f"Ahoj {jmeno}, je ti {vek} let.")
