#Version basique d'une horloge binaire !
import time

def convert(x):
        compteur = 0 #Le compteur pour 2^y
        puissanceDeux = 1
        while(x > puissanceDeux): #Tant que x est plus petit que la fonction 2^y, la boucle tourne
            puissanceDeux *= 2    #2^(y+1)
            if(x < puissanceDeux):  #2ème vérification pour éviter que le compteur compte trop
                puissanceDeux /= 2
                break               #Si x est plus petit que la fonction, alors on arrête la boucle
            compteur += 1         #On ajoute 1 au compteur, celui ci servira pour calculer le nombre en binaire
        resultat = 0 #Variable qui stockera la valeur convertie
        ajout = puissanceDeux
        while(compteur != 0):
            if(x >= puissanceDeux):
                resultat += 10**compteur
            else:
                puissanceDeux -= ajout
            ajout = ajout/2
            puissanceDeux += ajout
            compteur -= 1
        if(x%2==1):
            return resultat+1
        return resultat

while(True):
	print(str(convert(time.localtime().tm_hour)) + ":" + str(convert(time.localtime().tm_min)) + ":" + str(convert(time.localtime().tm_sec)), end="\r")
	time.sleep(1)