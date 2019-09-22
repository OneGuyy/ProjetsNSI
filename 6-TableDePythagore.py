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

for i in range(16):
	print("")
	for j in range(16):
		if(len(deciToHex(i*j))==1):
			print("0" + deciToHex(i*j), end=" ")
		else:
			print(deciToHex(i*j), end=" ")
