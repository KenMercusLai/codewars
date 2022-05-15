from copy import deepcopy
from typing import List


def clockwise_rotate(grid: List[List[int]]) -> List[List[int]]:
    return list(map(list, list(zip(*grid[::-1]))))


def counter_clockwise_rotate(grid: List[List[int]]) -> List[List[int]]:
    return list(map(list, list(zip(*grid))[::-1]))


def generate_grid(size: int) -> List[List[int]]:
    return [[0 for _ in range(size)] for _ in range(size)]


def spin(grid):
    if len(grid) == 1:
        return clockwise_rotate([[1] * len(grid[0])])

    ret = [[1] * len(grid[0]), [0] * len(grid[0])]
    ret[1][-1] = 1
    if len(grid) == 2:
        return clockwise_rotate(ret)
    return clockwise_rotate(ret + spin(counter_clockwise_rotate(deepcopy(grid[2:]))))


def spiralize(size):
    grid = generate_grid(size)
    return counter_clockwise_rotate(spin(grid))


if __name__ == '__main__':
    # Test
    assert spiralize(5) == [[1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 1],
                            [1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1]]
    assert spiralize(8) == [[1, 1, 1, 1, 1, 1, 1, 1],
                            [0, 0, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 1, 0, 1],
                            [1, 0, 1, 0, 0, 1, 0, 1],
                            [1, 0, 1, 1, 1, 1, 0, 1],
                            [1, 0, 0, 0, 0, 0, 0, 1],
                            [1, 1, 1, 1, 1, 1, 1, 1]]
