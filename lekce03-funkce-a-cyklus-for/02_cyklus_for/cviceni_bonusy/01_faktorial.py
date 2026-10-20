# Bonus 1 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá číslo N. Spočítej cyklem jeho faktoriál –
#     tedy 1 * 2 * 3 * ... * N – a výsledek vypiš.
#     (Faktoriál z 5 je 120.)


n = int(input("zadej cislo "))
faktorial = 1

for cislo in range(1, n +1):
	faktorial = faktorial * cislo
	print("kolo", cislo ,":" , faktorial)
print(faktorial)