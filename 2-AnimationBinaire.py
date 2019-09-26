def convert(x, resultat = ''):
    if x == 0: return "0b" + resultat[::-1]
    else: return convert(x//2, resultat + str(x%2)) 

def countdown(x):
	listValues = []
	for i in range(x+1):
		listValues.append(i)
	listValues.reverse()
	for val in listValues:
		print(convert(val), end=" ; ")

def countdown2(x):
    for i in range(x, -1, -1):
        print(convert(i), end=" ; ")

countdown(10)
print("")
countdown2(10)


input("")
