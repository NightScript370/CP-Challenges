function factorial(i) {
    if (i == 1)
        return 1;

    if (i <= 0)
        throw Error('Not possible to calculate Factorial Number');

    return i * factorial(i - 1);
}

[factorial(3), factorial(2), factorial(1)]