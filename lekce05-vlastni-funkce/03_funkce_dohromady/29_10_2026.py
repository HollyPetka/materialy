""""
def je_heslo_dlouhe(heslo):
	if len(heslo) > 8:
		return True
	else:
		return False

	

def zeptej_se_na_jmeno():
	jmeno = input("zadej jmeno")
	return jmeno

def zeptej_se_na_heslo():
	return input("zadej heslo")
	
		

def prihlaseni():
	jmeno = zeptej_se_na_jmeno
	heslo = zeptej_se_na_heslo
	if je_heslo_dlouhe(heslo):
		print("vitej", jmeno)
	else:
		print("heslo neni dlouhe")

	"""



def email():
		return input("zadej email").lower()


jmeno = "adam"
print(jmeno)
velke_jmeno = jmeno.upper()
print(velke_jmeno)





