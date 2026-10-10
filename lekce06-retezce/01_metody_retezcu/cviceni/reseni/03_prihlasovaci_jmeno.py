# Řešení cvičení 3 – Metody řetězců
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na přihlašovací jméno. Ulož ho malými písmeny a bez mezer
#    na krajích a vypiš, jak bude uložené. Obal výpis hranatými
#    závorkami, ať je vidět, že tam mezery nezůstaly.

jmeno = input("Přihlašovací jméno: ")
ulozene = jmeno.strip().lower()
print("[" + ulozene + "]")
