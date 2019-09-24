def maximum(x, y): #Retourne le plus grand entre x et y
	if x > y: return x
	else: return y



#CONVERTIONS

#HEXADECIMAL
def hexToDeci(num):
	dictToDeci = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A':10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
	resultat = 0
	num = num[::-1]
	for i in range(len(num)):
		resultat += dictToDeci.get(num[i])*16**i
	return resultat

def deciToHex(digit):
	dictHex = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10:'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
	quotien, reste = -1, 0
	resultat = ''
	while(quotien != 0):
		reste = digit % 16
		quotien = digit // 16
		digit = quotien
		resultat += dictHex.get(reste)
		#print("digit = " + str(digit), "quotien = " + str(quotien), "reste = " + str(reste), "resultat(inversé) = " + resultat[::-1])

	return resultat[::-1]

#BINAIRE
def deciToBin(x):
	quotien, reste = -1, 0
	resultat = ''

	while(quotien != 0):
		reste = x % 2
		quotien = x // 2
		x = quotien
		resultat += str(reste)
	return '0b' + resultat[::-1]


def binToDeci(num):
	for i in str(num):
		if(i != "0" and i != "1"):
			print("Ce n'est pas un nombre binaire !")
			return None
	if (num <= 0):
		return 0
	else:
		numString = list(str(num))
		count = 0
		result = 0
		for i in reversed(numString):
			if(i == "1"):
				result += 2**count
			count += 1
		return result

def formaterChaine(c1, c2): #Ex : c1 = 21 et c2 = 4810 alors retourne 0021
	c1 = str(c1)
	c2 = str(c2) 
	if len(c2) > len(c1):
		c1 = c1[::-1]
		while(len(c2) > len(c1)):
			c1 += '0'
		return c1[::-1]
	else:
		return c1

#FONCTION ADDITION ETRANGE
def additionEtrange(x, y):
	x = str(x)
	y = str(y)
	resultat = ''
	
	if(x[0:2] == "0b" and y[0:2] == "0b"):
		x = x[2:]
		y = y[2:]

		x = str(binToDeci(int(x)))
		y = str(binToDeci(int(y)))
	
		x = formaterChaine(x, y)
		y = formaterChaine(y, x)

		resultat = ''
		for i in range(len(x)):
			resultat += str(maximum(x[i], y[i]))
		return deciToBin(int(resultat))
	
	elif(x[0:2] == "0x" and y[0:2] == "0x"):
		x = x[2:]
		y = y[2:]
		x = str(hexToDeci(x))
		y = str(hexToDeci(y))

		x = formaterChaine(str(x), str(y))
		y = formaterChaine(str(y), str(x))

		resultat = ''
		for i in range(len(x)):
			resultat += str(maximum(x[i], y[i]))
		return "0x" + deciToHex(int(resultat))
	
	else:
		x = formaterChaine(str(x), str(y))
		y = formaterChaine(str(y), str(x))
		resultat = ''

		for i in range(len(x)):
			resultat += str(maximum(x[i], y[i]))
		return resultat


#Binaire
print(additionEtrange("0b1010", "0b1010"))
#Hexadecimal
print(additionEtrange("0x7E3", "0x1A"))
#Decimal
print(additionEtrange(1999, 2000))
