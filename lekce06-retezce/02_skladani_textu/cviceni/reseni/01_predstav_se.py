# Řešení cvičení 1 – Skládání textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na jméno a na věk a jednou větou oboje vypiš.
#     Použij f-string.

jmeno = input("Jak se jmenuješ? ")
vek = input("Kolik ti je let? ")

print(f"Ahoj {jmeno}, je ti {vek} let.")

# Věk sem přišel z input() jako text a f-stringu to nevadí.
# Kdybys s ním chtěla počítat, převedeš ho na číslo pomocí int().
