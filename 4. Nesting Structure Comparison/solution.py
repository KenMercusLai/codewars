from itertools import zip_longest


def same_structure_as(original, other):
    if isinstance(original, list) != isinstance(other, list):
        return False
    elif (original is None or other is None) and original != other:
        return False
    
    if isinstance(original, list):
        return all(map(lambda x: same_structure_as(x[0], x[1]), zip_longest(original, other)))
    else:
        return True


if __name__ == '__main__':
    assert same_structure_as([1, [1, 1]], [2, [2, 2]]) is True
    assert same_structure_as([1, [1, 1]], [[2, 2], 2]) is False
