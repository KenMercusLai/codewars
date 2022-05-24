from functools import reduce


def reduce_exp(exp, base):
    return base ** (exp if exp < 4 else exp % 4 + 4)


def last_digit(lst):
    if not lst:
        return 1
    return reduce(reduce_exp, lst[::-1], 1) % 10


if __name__ == '__main__':
    test_data = [
        ([], 1),
        ([0, 0], 1),
        ([0, 0, 0], 0),
        ([1, 2], 1),
        ([3, 4, 5], 1),
        ([4, 3, 6], 4),
        ([7, 6, 21], 1),
        ([12, 30, 21], 6),
        ([2, 2, 2, 0], 4),
        ([937640, 767456, 981242], 0),
        ([123232, 694022, 140249], 6),
        ([499942, 898102, 846073], 6)
    ]
    for test in test_data:
        print(test[0], test[1])
        assert last_digit(test[0]) == test[1]
