// ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL.

let generateList = () => {
    let arr = [];
    for (let i=2.0; i<=5.5; i=i+0.5){
        arr.push(i);
    }
    return arr;
}

console.log(generateList());