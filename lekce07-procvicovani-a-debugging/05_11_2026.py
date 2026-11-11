def je_platny(tah):
    return je_kamen(tah) or je_nuzky(tah) or tah == "papir"

def kdo_vyhral(tvuj, pocitacuv):
    if tvuj == pocitacuv:
        return "remiza"
    vyhrala_kamenem = tvuj == KAMEN and pocitacuv == NUZKY
    vyhrala_nuzkami = tvuj == NUZKY and pocitacuv == PAPIR
    vyhrala_papirem = tvuj == PAPIR and pocitacuv == KAMEN
    if vyhrala_kamenem or vyhrala_nuzkami or vyhrala_papirem:
        return "vyhra"
    else:
        return "prohra"


tvuj_tah = uklid_vstupu(input(OTAZKA_PRO_UZIVATELE))

if not je_platny(tvuj_tah):
    print("Takový tah neznám.")
else:
    pocitacuv_tah = tah_pocitace()
    print(f"Ty hraješ: {tvuj_tah}")
    print(f"Počítač hrál: {pocitacuv_tah}")

    vysledek = kdo_vyhral(tvuj_tah, pocitacuv_tah)
    if vysledek == "vyhra":
        print("Vyhrála jsi!")
    elif vysledek == "remiza":
        print("Remíza.")
    else:
        print("Prohrála jsi.")