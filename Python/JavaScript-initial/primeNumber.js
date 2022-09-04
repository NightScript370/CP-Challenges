function isPrime(number) {
    // 1 is neither prime nor composite number
    // 0 and below is taboo
    if (number < 2) {
        return false;
    }

    let primeNum = true;
    // looping through 2 through half number. Originally done through one less, but the skipped over values would always be two.
    const loopingPoint = number / 2 + 1;
    for (let i = 2; i < loopingPoint; i++) {
        if (number % i == 0) {
            primeNum = false;
            break;
        }
    }

    return primeNum;
}

[isPrime(3), isPrime(4), isPrime(16), isPrime(17)]