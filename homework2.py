# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA itemY O WARTOŚCIACH 1 - n.NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH itemÓW BRAKUJE
# 1 - n = [1, 2, 3, 4, 5, ..., 10]
# np.n = 10
# wejście: [2, 3, 7, 4, 9], 10
# wyjście: [1, 5, 6, 8, 10]


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
