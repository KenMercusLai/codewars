from typing import Tuple, List


def flatten(heightmap):
    return [j for i in heightmap for j in i]


def find_location(heightmap, start_level) -> List[Tuple[int, int]]:
    locations = []
    for i in range(len(heightmap)):
        for j in range(len(heightmap[0])):
            if heightmap[i][j] == start_level:
                locations.append((i, j))
    return locations


def is_neighbor(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
    # print(a, b)
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) == 1


def group_locations(locations: List[Tuple[int, int]]):
    ret, *candidate = sorted(locations)
    ret = [[ret]]
    print('ret: ', ret, 'candidate: ', candidate)
    while candidate:
        candidates_updated = True
        while candidates_updated:
            candidates_updated = False
            for i in range(len(candidate)):
                # print('i: ', i, 'candidate[i]: ', candidate[i])
                for j in range(len(ret)):
                    if any([True if is_neighbor(candidate[i], k) else False for k in ret[j]]):
                        ret[j].append(candidate[i])
                        candidates_updated = True
                        break
                if candidates_updated:
                    candidate.pop(i)
                    break
        if candidate:
            ret.append([candidate.pop()])

        print('ret: ', ret)
    return ret


def raise_water(heightmap, groups):
    raised = 0
    for i in groups:
        for j in i:
            heightmap[j[0]][j[1]] += 1
            raised += 1
    return heightmap, raised


def not_at_border(heightmap, i, j):
    return 0 < i < len(heightmap) - 1 and 0 < j < len(heightmap[0]) - 1


def is_lower(heightmap, i, j, start_level):
    neighbors = [heightmap[i + 1][j], heightmap[i - 1][j], heightmap[i][j + 1], heightmap[i][j - 1]]
    return all([heightmap[i][j] < neighbor for neighbor in neighbors if neighbor != start_level] + [True])


def check_leakage(heightmap, groups, start_level):
    ret = []
    for i in groups:
        if all([True if not_at_border(heightmap, j[0], j[1]) and is_lower(heightmap, j[0], j[1], start_level) else False
                for j in i]):
            ret.append(i)
    return ret


def fill_water(heightmap, start_level):
    filled_water = 0
    raised = 1
    while raised:
        locations = find_location(heightmap, start_level)
        groups = group_locations(locations)
        print(groups)
        groups = check_leakage(heightmap, groups, start_level)
        print(groups)
        heightmap, raised = raise_water(heightmap, groups)
        filled_water += raised
        start_level += 1
        print(heightmap, raised, filled_water, start_level)
        # input()
    return filled_water


def volume(heightmap):
    print(heightmap)
    if len(heightmap) < 3 or len(heightmap[0]) < 3:
        return 0
    start_level = min(flatten(heightmap))
    print('start with: ', start_level)
    return fill_water(heightmap, start_level)


if __name__ == '__main__':
    def pretty_print(heightmap):
        size = max(len(str(v)) for r in heightmap for v in r)
        return '\n'.join(' '.join(f'{v: >{size}}' for v in r) for r in heightmap)


    def pretty_test(heightmap, expected):
        testval = volume([r[:] for r in heightmap])
        assert testval == expected, 'Test for this heightmap failed!\n{0}\n'.format(pretty_print(heightmap))


    pretty_test([[0]], 0)
    pretty_test([[22]], 0)
    pretty_test([[2, 1, 2],
                 [1, 0, 1],
                 [2, 1, 2]], 1)
    pretty_test([[1, 1, 1],
                 [1, 8, 1],
                 [1, 1, 1]], 0)
    pretty_test([[9, 9, 9, 9],
                 [9, 0, 0, 9],
                 [9, 0, 0, 9],
                 [9, 9, 9, 9]], 36)
    pretty_test([[9, 9, 9, 9, 9],
                 [9, 0, 1, 2, 9],
                 [9, 7, 8, 3, 9],
                 [9, 6, 5, 4, 9],
                 [9, 9, 9, 9, 9]], 45)
    pretty_test([[8, 8, 8, 8, 6, 6, 6, 6],
                 [8, 0, 0, 8, 6, 0, 0, 6],
                 [8, 0, 0, 8, 6, 0, 0, 6],
                 [8, 8, 8, 8, 6, 6, 6, 0]], 56)
    pretty_test([[0, 10, 0, 20, 0],
                 [20, 0, 30, 0, 40],
                 [0, 40, 0, 50, 0],
                 [50, 0, 60, 0, 70],
                 [0, 60, 0, 70, 0]], 150)
    pretty_test([[3, 3, 3, 3, 3],
                 [3, 0, 0, 0, 3],
                 [3, 3, 3, 0, 3],
                 [3, 0, 0, 0, 3],
                 [3, 0, 3, 3, 3],
                 [3, 0, 0, 0, 3],
                 [3, 3, 3, 0, 3]], 0)
    pretty_test([[3, 3, 3, 3, 3],
                 [3, 2, 2, 2, 3],
                 [3, 3, 3, 2, 3],
                 [3, 1, 1, 1, 3],
                 [3, 1, 3, 3, 3],
                 [3, 0, 0, 0, 3],
                 [3, 3, 3, 0, 3]], 0)
    f = lambda: [[3, 3, 3, 3, 3],
                 [3, 0, 0, 0, 3],
                 [3, 3, 3, 0, 3],
                 [3, 0, 0, 0, 3],
                 [3, 0, 3, 3, 3],
                 [3, 0, 0, 0, 3],
                 [3, 3, 3, 1, 3]]
    pretty_test(f(), 11)
    pretty_test(f()[::-1], 11)
    pretty_test([r[::-1] for r in f()], 11)
    pretty_test([r[::-1] for r in reversed(f())], 11)
