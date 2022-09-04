function factoralNumber (number) {
    if (number <= 0)
        throw Error('Not possible to calculate Factorial Number')

    let out = 1
    while (number) {
        out *= number
        number -= 1
    }

    return out
}

[factoralNumber(5), factoralNumber(4), factoralNumber(3)]