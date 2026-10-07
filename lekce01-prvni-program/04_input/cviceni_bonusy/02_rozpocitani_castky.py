# Bonus 2 – Vstup od uživatelky
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na částku a na počet lidí.
#     Vypiš, kolik zaplatí každý a kolik korun zbyde.


castka = int(input("Kolik to stojí? "))
lidi = int(input("Kolik je lidí? "))
print("Každý zaplatí", castka // lidi, "zbyde", castka % lidi)