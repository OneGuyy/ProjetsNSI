def decomposition(x):
	resultat = str(x) + " = " #Variables uniques de la fonction
	p2 = 1

	while(x >= p2): #Boucle pour compter les puissances de 2
		p2 *= 2
		#print("x = " + str(x) + " p2 = " + str(p2))
	
	p2 = int(p2 / 2) #Pour que x soit toujours >= p2
	print(p2)
	x -= p2 #Comme on sait que x >= p2, on peut le soustraire !
	resultat += str(p2) #On ajoute p2 au résultat

	while(x > 0): #Boucle de calcul
		#print("x = " + str(x) + " p2 = " + str(p2)) 
		if((x - p2/2) >= 0):
			x -= p2/2
			resultat += " + " + str(int(p2/2))
		p2 = int(p2/2)

	return resultat
	

print("\n" + decomposition(10))
