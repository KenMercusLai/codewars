def padovan(n):
    if n in [0, 1, 2]:
        return 1

    first, second, third = 1, 1, 1
    while n > 2:
        first, second, third = second, third, first + second
        n -= 1
    return third
