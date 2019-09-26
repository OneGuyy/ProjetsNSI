#Version basique d'une horloge binaire !
import time

def convert(x, resultat = ''):
    if x == 0: return "0b" + resultat[::-1]
    else: return convert(x//2, resultat + str(x%2)) 

while(True):
	print(str(convert(time.localtime().tm_hour)) + ":" + str(convert(time.localtime().tm_min)) + ":" + str(convert(time.localtime().tm_sec)), end="\r")
	time.sleep(1)
