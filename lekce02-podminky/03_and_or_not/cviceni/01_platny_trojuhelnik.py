# Cvičení 1 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Platný trojúhelník. Ze tří stran jde sestavit trojúhelník jen tehdy,
#    když je součet každých dvou stran větší než ta třetí.
#    Vypiš "Platný trojúhelník." / "Takový trojúhelník nejde.".
a = 5
b = 2
c = 2


if a + b > c and b +c >a and c + a > b:
	print("platny trojuhelnik")
else:
	print("takovy trojuhelnik nejde")