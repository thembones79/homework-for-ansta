# ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.


def generateList():
    i = 2.0
    arr = []
    while i <= 5.5:
        arr.append(i)
        i += 0.5
    print(arr)

generateList()
