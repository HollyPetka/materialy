# Cvičení 2 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci je_plnoleta(vek), která vrátí True, nebo False.
#    Zeptej se uživatele na věk a podle výsledku vypiš
#    "Můžeš dál." nebo "Ještě ne.".


def je_plnoleta (vek):
	return vek >= 18

tvuj_vek = int(input("jaky je tvuj vek - kolik ti je let?: "))
if je_plnoleta (tvuj_vek):
	print("muzes dal")
else:
	print("jeste ne")