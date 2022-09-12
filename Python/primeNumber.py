def isPrime(number):
    # 1 is neither prime nor composite number
    # 0 and below is taboo
    if (number < 2): return False

    primeNum = True;
    # looping through 2 to number-1
    for i in range(2, number//2+1):
        if number % i == 0:
            primeNum = False
            break;

    return primeNum;

print([isPrime(3), isPrime(4), isPrime(16), isPrime(17)])