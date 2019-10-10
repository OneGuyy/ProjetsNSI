def formaterChaine(c1, c2): #Ex : c1 = 21 et c2 = 4810 alors retourne 0021
	c1, c2 = str(c1), str(c2)
	if len(c2) > len(c1):
		while(len(c2) > len(c1)):
			c1 = '0' + c1
	return c1

		
#FONCTION ADDITION ETRANGE
def additionEtrange(x, y):
	resultat = ''
	#Nombre en base 10
	if x[0:2].isdigit() and y[0:2].isdigit():
		x = formaterChaine(str(x), str(y))
		y = formaterChaine(str(y), str(x))
		for i in range(len(x)):
			resultat += str(max(x[i], y[i]))
		return resultat

	#Nombre binaire/hexadécimaux
	elif x[0:2] in ["0b", "0x"] and y[0:2] == x[0:2]:
		nType = x[:2]
		x = x[2:]
		y = y[2:]

		if(nType == '0b'): #Si c'est du Binaire
			return bin(int(additionEtrange(str(int(x, 2)), str(int(y, 2)))))

		else:
			return hex(int(additionEtrange(str(int(x, 16)), str(int(y, 16)))))




##TESTS

print(additionEtrange(str(1999), str(2018)))
print(additionEtrange("0b11", "0b1110"))
print(additionEtrange("0x7e3", "0x1a"))
