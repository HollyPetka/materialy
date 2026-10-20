# Bonus 1 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá celkovou cenu útraty a počet lidí. Vypiš, kolik
#     zaplatí každý, zaokrouhleno na dvě desetinná místa.


utrata_cena = int(input("zadej cenu utraty "))
pocet_lidi = int(input("zadej pocet lidi "))

print(round(utrata_cena / pocet_lidi))