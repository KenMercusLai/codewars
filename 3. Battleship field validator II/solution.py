def validate_battlefield(battlefield):
    ship_counts = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
    }  # 1: submarines, 2: destroyers, 3: cruisers, 4: battleship
    visited = [[False] * 10 for _ in range(10)]

    def check_ship(y, x):
        if (
            x < 0
            or x >= 10
            or y < 0
            or y >= 10
            or battlefield[y][x] == 0
            or visited[y][x]
        ):
            return 0
        visited[y][x] = True
        size = 1
        # Check horizontally
        if x + 1 < 10 and battlefield[y][x + 1] == 1:
            while x + 1 < 10 and battlefield[y][x + 1] == 1:
                size += 1
                x += 1
                visited[y][x] = True
        # Check vertically
        elif y + 1 < 10 and battlefield[y + 1][x] == 1:
            while y + 1 < 10 and battlefield[y + 1][x] == 1:
                size += 1
                y += 1
                visited[y][x] = True
        return size

    for y in range(10):
        for x in range(10):
            if battlefield[y][x] == 1 and not visited[y][x]:
                ship_size = check_ship(y, x)
                print(y, x, ship_size)
                print(ship_counts)
                if ship_size in ship_counts:
                    ship_counts[ship_size] += 1
                else:
                    return False

    return (
        ship_counts[4] == 1
        and ship_counts[3] == 2
        and ship_counts[2] == 3
        and ship_counts[1] == 4
    )


validate_battlefield(
    [
        [1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
)
