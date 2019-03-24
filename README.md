# Homework for Ansta | Smart Solutions

### ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
### przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi


## SOLUTION 1



```Python

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
```

### ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA itemY O WARTOŚCIACH 1 - n.NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH itemÓW BRAKUJE
### 1 - n = [1, 2, 3, 4, 5, ..., 10]
### np.n = 10
### wejście: [2, 3, 7, 4, 9], 10
### wyjście: [1, 5, 6, 8, 10]


## SOLUTION 2



```Python

def search(arr, item):
    i = 0
    for x in arr:
        if x == item:
            return i
        i += 1
    return -1


def findMissing(arr, max):
    resultArr = []
    for i in range(1, max):
        if search(arr, i) < 0:
            resultArr.append(i)

    print(resultArr)


findMissing([2, 3, 7, 4, 9], 10)
```

### ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.


## SOLUTION 3



```Python

def generateList():
    i = 2.0
    arr = []
    while i <= 5.5:
        arr.append(i)
        i += 0.5
    print(arr)

generateList()
```
