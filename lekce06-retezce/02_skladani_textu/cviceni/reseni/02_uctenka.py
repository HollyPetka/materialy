# Řešení cvičení 2 – Skládání textu
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# V proměnných je cena jednoho kusu a počet kusů. Vypiš řádek účtenky
#     se dvěma desetinnými místy, například:  3 x 24.90 = 74.70

cena = 24.9
pocet = 3

print(f"{pocet} x {cena:.2f} = {cena * pocet:.2f}")

# Bez .2f by se vypsalo 74.69999999999999.
