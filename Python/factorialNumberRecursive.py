def factorial(i):
    if i == 1:
        return 1
    assert i > 0
    return i * factorial(i - 1)


print([factorial(3), factorial(2), factorial(1)])