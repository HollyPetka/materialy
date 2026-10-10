# Řešení bonusu 1 – Metody řetězců
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Tři jména přišla z formuláře rozbitá – mezery na krajích a náhodná
#    velikost písmen. Uklid každé tak, aby vyšlo například
#    "Anna Nováková", a vypiš ho.

jmeno1 = "  anna NOVÁKOVÁ  "
jmeno2 = "PETRA svobodová"
jmeno3 = " tereza Dvořáková   "

print(jmeno1.strip().title())
print(jmeno2.strip().title())
print(jmeno3.strip().title())

# title() udělá velké první písmeno každého slova a zbytek malý,
# takže srovná i NOVÁKOVÁ na Nováková.
