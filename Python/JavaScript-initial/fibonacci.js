function closestFibonacciNumber (paramNumber) {
    if (paramNumber == Infinity)
        throw Error('Number cannot lead system into Infinite Loop. Try again');

    let sumOfAddition = 1;
    let numberAdded = sumOfAddition;
    while (sumOfAddition < paramNumber) {
        numberAdded = sumOfAddition - numberAdded;
        sumOfAddition = sumOfAddition + numberAdded;
    }

    if (sumOfAddition == paramNumber)
        return [sumOfAddition];
    else
        return [sumOfAddition - numberAdded, sumOfAddition];
}

function nThFibonacciNumber (paramNumber) {
    if (paramNumber == Infinity || paramNumber < 0)
        throw Error('Number cannot lead system into Infinite Loop. Try again');

    let sumOfAddition = 1;
    let numberAdded = sumOfAddition;
    for (i = 0; i < paramNumber; i++) {
        numberAdded = sumOfAddition - numberAdded;
        sumOfAddition = sumOfAddition + numberAdded;
    }

    return sumOfAddition;
}

({
  closest: [closestFibonacciNumber(1), closestFibonacciNumber(4), closestFibonacciNumber(11), closestFibonacciNumber(21)],
  nth: [nThFibonacciNumber(1), nThFibonacciNumber(7), nThFibonacciNumber(11)]
})