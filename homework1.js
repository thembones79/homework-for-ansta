//ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
//przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi

let removeDash = stringWithDash => stringWithDash.replace("-", "");

let extractNumber = postCode => parseInt(removeDash(postCode));

let addZeros = number => {
  if (number < 10) {
    return "0000" + number;
  } else if (number < 100) {
    return "000" + number;
  } else if (number < 1000) {
    return "00" + number;
  } else if (number < 10000) {
    return "0" + number;
  } else {
    let str = number.toString();
    return str;
  }
};

let formatToPostCode = number => {
  let str = addZeros(number);
  return str.slice(0, 2) + "-" + str.slice(2);
};

let codeGenerator = (firstCode, lastCode) => {
  let arr = [];
  let i = extractNumber(firstCode);
  while (i < extractNumber(lastCode) - 1) {
    i++;
    arr.push(formatToPostCode(i));
  }
  return arr;
};

console.log(codeGenerator("00-005", "00-155"));
