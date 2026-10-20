# Bonus 3 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá počáteční částku na spořicím účtu. Úrok je 5 % ročně.
#     Spočítej cyklem, kolik na účtu bude po deseti letech
#     (každý rok se částka vynásobí 1.05), a výsledek vypiš.


castka = int(input("zadej castku na sporicim ucte "))
urok = 1.05

for rok in range(10):
	castka = castka * urok 
print(round(castka, 2))