# ---------------------------------------------
#  Co už s textem umíme
# ---------------------------------------------
# Spusť soubor a porovnej výsledky.
#
# Textu se v Pythonu odborně říká řetězec (anglicky string) – řetěz znaků
# navázaných za sebou. Pracuješ s ním od první lekce. Tohle už znáš:

print("Ahoj" + " " + "PyLadies!")   # spojení plusem        (lekce 1)
print("=" * 20)                     # opakování hvězdičkou  (lekce 1)
print(len("Ahoj"))                  # 4 – délka             (lekce 3)
print("o" in "Ahoj")                # True – hledání znaku  (lekce 3)

for pismeno in "Ahoj":              # průchod po znacích    (lekce 3)
    print(pismeno)


# Z lekce 1 taky víš, že input() vrací text a int() z něj udělá číslo.
# Opačný směr má na starosti funkce str():
vek = 30
print("Je mi " + str(vek) + " let")
# Plus spojuje text s textem. Bez str() by na tom řádku program spadl.
# (Ve druhé složce téhle lekce tenhle zápis nahradíme čitelnějším.)


# ---------------------------------------------
#  Metoda: co umí text sám
# ---------------------------------------------
# Všechny příklady nahoře pracují s textem zvenčí – len() si ho vezme
# a změří. Řetězec umí věci i sám o sobě. Zapisuje se to tečkou:

jmeno = "pyladies"
print(jmeno.upper())      # PYLADIES

# Čte se to takhle:
#   jmeno     hodnota, na které metodu voláme
#   .         tečka – „na téhle hodnotě"
#   upper()   metoda, tedy funkce, která k řetězci patří
#
# Kulaté závorky jsou povinné, stejně jako u len() nebo u tvých funkcí
# z lekce 5. Bez nich se metoda nezavolá.
