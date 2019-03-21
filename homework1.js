//ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
//przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi

let noDash = stringWithDash => stringWithDash.replace("-", "");
let extractNumber = postCode => parseInt(noDash(postCode));
let addDash = number => {
  str = number.toString();
  return str.slice(0, 2) + "-" + str.slice(2);
};

let codeGenerator = (firstCode, lastCode) => {
  let arr = [];
  let i = extractNumber(firstCode);
  while (i < extractNumber(lastCode)-1) {
    i++;
    arr.push(addDash(i));
  }
  return arr;
};

console.log(codeGenerator("79-900", "80-155"));
