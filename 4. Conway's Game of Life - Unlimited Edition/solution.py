from typing import List


def neighbors(cells: List[List[int]], row: int, col: int) -> int:
    surroundings = [[-1, 1], [-1, 0], [-1, -1], [0, 1], [0, -1], [1, -1], [1, 0], [1, 1]]
    ret = []
    for i, j in surroundings:
        y = row + i
        x = col + j
        if x < 0 or y < 0 or x >= len(cells[0]) or y >= len(cells):
            continue
        ret.append(cells[y][x])
    return sum(ret)


def empty_grid(cells):
    return [[0 for _ in range(len(cells[0]) + 2)] for _ in range(len(cells) + 2)]


def extend_grid(cells):
    grid = empty_grid(cells)
    for i in range(1, len(cells) + 1):
        for j in range(1, len(cells[0]) + 1):
            grid[i][j] = cells[i - 1][j - 1]
    return grid


def calc_next_gen(cells):
    extended_cells = extend_grid(cells)
    next_generation = empty_grid(cells)
    for row in range(len(extended_cells)):
        for col in range(len(extended_cells[0])):
            ret = neighbors(extended_cells, row, col)
            if extended_cells[row][col] == 1 and ret in [2, 3]:
                next_generation[row][col] = 1
            elif extended_cells[row][col] == 0 and ret == 3:
                next_generation[row][col] = 1
            else:
                next_generation[row][col] = 0
    ret = remove_empties(next_generation)
    return ret


def remove_empty_rows(cells):
    while sum(cells[0]) == 0:
        cells.pop(0)
    while sum(cells[-1]) == 0:
        cells.pop()
    return cells


def rotate_cells(param):
    return list(map(list, list(zip(*param[::-1]))))


def counter_rotate_cells(cells):
    return list(map(list, list(zip(*cells[::]))[::-1]))


def remove_empties(cells):
    return counter_rotate_cells(remove_empty_rows(rotate_cells(remove_empty_rows(cells))))


def get_generation(cells, generations):
    for _ in range(generations):
        cells = calc_next_gen(cells)
    return cells


if __name__ == '__main__':
    start = [[1, 0, 0], [0, 1, 1], [1, 1, 0]]
    end = [[0, 1, 0], [0, 0, 1], [1, 1, 1]]
    assert get_generation(start, 1) == end
