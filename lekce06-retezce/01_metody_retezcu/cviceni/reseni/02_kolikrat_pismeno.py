# Řešení cvičení 2 – Metody řetězců
# Tvoje řešení může vypadat jinak, a to je v pořádku.

# Zeptej se na slovo a vypiš, kolikrát je v něm písmeno "a".
#    V lekci 3 jsi počítala samohlásky cyklem, tady stačí jedna metoda.

slovo = input("Napiš slovo: ")
print("Písmeno a je ve slově", slovo.count("a"), "krát.")

# Velké "A" se takhle nepočítá. Kdybys chtěla obojí, převeď slovo
# nejdřív na malá písmena:  slovo.lower().count("a")
