# ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1 - n.NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
# 1 - n = [1, 2, 3, 4, 5, ..., 10]
# np.n = 10
# wejście: [2, 3, 7, 4, 9], 10
# wyjście: [1, 5, 6, 8, 10]


def search(tab, element):
    i = 0
    for o in tab:  # o przyjmuje wartości każdego kolejnego elementu tablicy
        if o == element:  # jeśli znajdzie, zwraca i
            return i
        i += 1  # dodaje do i 1
    return -1  # jeśli nie znajdzie, zwraca -1


def findMissing(arr, max):
    resultArr = []
    for i in range(1, max):
        if search(arr, i) < 0:
            resultArr.append(i)

    print(resultArr)


findMissing([2, 3, 7, 4, 9], 10)
