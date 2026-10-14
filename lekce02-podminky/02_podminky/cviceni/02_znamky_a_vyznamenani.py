# Cvičení 2 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Vrať se ke studentce se třemi známkami. Spočítej průměr a vypiš
#    "Máš vyznamenání!", když je průměr menší nebo rovný 2,
#    jinak vypiš "Bez vyznamenání.".
znamka1 = 1
znamka2 = 3
znamka3 = 2


prumer = ((znamka1 + znamka2 + znamka3)/3)
print(prumer)

if prumer <= 2:
	print("mas vyznamenani")
else:
	print("bez vyznamenani")	