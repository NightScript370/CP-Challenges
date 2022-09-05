let count = 0;
let numberWithCount = 0;

function collatz(number) {
  const arrayFill = [number];
  while (number !== 1) {
    if ((number % 2) == 0) {
        number = number / 2;
    } else {
        number = number * 3 + 1;
    }
    arrayFill.push(number)
  }
  return arrayFill;
}

for (let arrayFillIndex = 1000000; arrayFillIndex > 2; arrayFillIndex--) {
  let collatzArray = collatz(arrayFillIndex);
  if (count < collatzArray.length) {
    count = collatzArray.length
    numberWithCount = collatzArray[0]
  }
}

({
  numberWithCount,
  count,
  collatzOperation: collatz(numberWithCount)
})