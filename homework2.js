// ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1 - n.NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
// 1 - n =[1, 2, 3, 4, 5, ..., 10]
// np.n = 10
// wejście: [2, 3, 7, 4, 9], 10
// wyjście: [1, 5, 6, 8, 10]

const findMissing = (arr, max) => {
    let resultArr =[];
    for(let i=1;i<=max;i++){
        if(!arr.find(x => x===i)){
            resultArr.push(i);
        }
    }
    return resultArr;
}


console.log(findMissing([2, 3, 7, 4, 9], 10));