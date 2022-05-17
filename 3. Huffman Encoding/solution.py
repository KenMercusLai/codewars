def group_cells(field):
    ret = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                for group_index in range(len(ret)):
                    if ((i + 1, j) in ret[group_index] or
                            (i - 1, j) in ret[group_index] or
                            (i, j + 1) in ret[group_index] or
                            (i, j - 1) in ret[group_index]):
                        ret[group_index].append((i, j))
                        break
                else:
                    ret.append([(i, j)])
    return ret


def straight(cells):
    rows = map(lambda x: x[0], cells)
    cols = map(lambda x: x[1], cells)
    return len(set(list(rows))) == 1 or len(set(list(cols))) == 1


def validate_groups(groups):
    lengths = list(map(len, groups))
    return len(groups) == 10 and all(map(straight, groups)) and lengths.count(1) == 4 and lengths.count(
        2) == 3 and lengths.count(3) == 2 and lengths.count(4) == 1


def contact(field):
    for i in range(len(field) - 1):
        for j in range(len(field[i]) - 1):
            if field[i][j:j + 2] == [1, 0] and field[i + 1][j:j + 2] == [0, 1]:
                return False
            elif field[i][j:j + 2] == [0, 1] and field[i + 1][j:j + 2] == [1, 0]:
                return False
    return True


def validate_battlefield(field):
    groups = group_cells(field)
    return validate_groups(groups) and contact(field)


if __name__ == '__main__':
    battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                   [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                   [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                   [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    assert validate_battlefield(battleField) == True
