def convert(strNum):
    for i in strNum:
        if(i != "0" and i != "1"):
            print("Ce n'est pas un nombre binaire !")
            return None
    intNum = int(strNum)
    if (intNum <= 0):
        return 0
    else:
        numString = list(strNum)
        count = 0
        result = 0
        for i in reversed(numString):
            if(i == "1"):
                result += 2**count
            count += 1
        return str(result)

def inversion(binStr):
   print(convert(str(binStr)))
   print(convert(str(binStr)[::-1]))

inversion(10111)