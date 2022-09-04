def closestFibonacciNumber(paramNumber):
    sumOfAddition = 1
    numberAdded = sumOfAddition
    while sumOfAddition < paramNumber:
        numberAdded = sumOfAddition - numberAdded
        sumOfAddition = sumOfAddition + numberAdded

    if sumOfAddition == paramNumber:
        return [sumOfAddition]
    else:
        return [sumOfAddition - numberAdded, sumOfAddition]

def nthFibonacciNumber(paramNumber):
    assert paramNumber >= 0

    sumOfAddition = 1
    numberAdded = sumOfAddition
    for i in range(paramNumber):
        numberAdded = sumOfAddition - numberAdded
        sumOfAddition = sumOfAddition + numberAdded

    return sumOfAddition - numberAdded

print([closestFibonacciNumber(1), closestFibonacciNumber(4), closestFibonacciNumber(11), closestFibonacciNumber(21)])
print([nthFibonacciNumber(0), nthFibonacciNumber(1), nthFibonacciNumber(2), nthFibonacciNumber(7), nthFibonacciNumber(11)])