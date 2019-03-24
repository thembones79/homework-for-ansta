# ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
# przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi


def extractNumber(postCode):
    return int(removeDash(postCode))

def removeDash(stringWithDash):
    return stringWithDash.replace("-", "")

def addZeros(number):
    if number < 10:
        return "0000"+ str(number)
    elif number < 100:
        return "000" + str(number)
    elif number < 1000:
        return "00" + str(number)
    elif number < 10000:
        return "0" + str(number)
    else:
        return str(number)

def formatToPostCode(number):
    str = addZeros(number)
    return str[:2] + "-" + str[2:]


def codeGenerator(firstCode, lastCode):
    arr = []
    i = extractNumber(firstCode)
    while i < extractNumber(lastCode)-1:
        i+=1
        arr.append(formatToPostCode(i))

    print(arr)


codeGenerator("79-900", "80-155")
