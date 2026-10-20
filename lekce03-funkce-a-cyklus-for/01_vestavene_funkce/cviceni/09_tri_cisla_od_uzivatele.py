# Cvičení 9 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se uživatele na tři čísla (klidně i záporná) a vypiš,
#    jak velké je to největší z nich bez ohledu na znaménko.
#    Např. z čísel -20, 5 a 12 je největší velikost 20.


a = int(input("dej mi cislo a (i zaporná)"))
b = int(input("dej mi cislo b (i zaporná)"))
c = int(input("dej mi cislo c (i zaporná)"))

print(max(abs(a), abs(b), abs(c)))