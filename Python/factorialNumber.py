def factoralNumber(number):
    assert number > 0
    out = 1
    while (number):
        out *= number
        number -= 1

    return out


print([factoralNumber(5), factoralNumber(4), factoralNumber(3)])