# ---------------------------------------------
#  Zaokrouhlení ve f-stringu
# ---------------------------------------------
# Spusť soubor a podívej se na první řádek výpisu.

cena = 249
s_dph = cena * 1.21


# S desetinnými čísly počítá Python s drobnou nepřesností a na ceně
# je to vidět:
print(f"Cena s DPH: {s_dph}")


# Dvojtečka a .2f za výrazem říkají: zaokrouhli na dvě desetinná místa.
print(f"Cena s DPH: {s_dph:.2f}")


# Zaokrouhlovat umí i funkce round(), kterou znáš z vestavěných funkcí.
# Liší se u částek, kterým druhé desetinné místo chybí:
zaloha = 200 * 1.21
print(round(zaloha, 2))
print(f"{zaloha:.2f}")


# U cen se proto hodí .2f. Dvě desetinná místa drží i u kulatých částek.
