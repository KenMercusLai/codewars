CONNECTIONS = {'a1': {'c2', 'b3'}, 'c2': {'b4', 'a3', 'd4', 'a1', 'e1', 'e3'},
               'b3': {'a5', 'd4', 'c5', 'a1', 'd2', 'c1'}, 'b1': {'c3', 'd2', 'a3'},
               'd2': {'e4', 'f1', 'b3', 'f3', 'b1', 'c4'}, 'a3': {'b1', 'b5', 'c4', 'c2'},
               'c3': {'e4', 'a2', 'b5', 'd5', 'e2', 'a4', 'b1', 'd1'}, 'c1': {'a2', 'b3', 'e2', 'd3'},
               'a2': {'c1', 'c3', 'b4'}, 'e2': {'g1', 'g3', 'f4', 'd4', 'c3', 'c1'},
               'd3': {'b2', 'b4', 'f4', 'c5', 'e1', 'e5', 'f2', 'c1'}, 'd1': {'b2', 'c3', 'e3', 'f2'},
               'b2': {'a4', 'd1', 'c4', 'd3'}, 'f2': {'e4', 'h3', 'd3', 'g4', 'h1', 'd1'},
               'e3': {'f1', 'd5', 'g2', 'c2', 'g4', 'f5', 'd1', 'c4'}, 'e1': {'c2', 'f3', 'g2', 'd3'},
               'g2': {'f4', 'e3', 'h4', 'e1'}, 'f3': {'g1', 'g5', 'd4', 'h4', 'e1', 'd2', 'e5', 'h2'},
               'f1': {'e3', 'd2', 'h2', 'g3'}, 'h2': {'f1', 'f3', 'g4'}, 'g3': {'e4', 'f1', 'f5', 'e2', 'h1', 'h5'},
               'g1': {'f3', 'e2', 'h3'}, 'h3': {'f4', 'g1', 'g5', 'f2'}, 'h1': {'g3', 'f2'},
               'b4': {'d3', 'a2', 'd5', 'c2', 'c6', 'a6'}, 'a4': {'b6', 'b2', 'c3', 'c5'},
               'c4': {'b2', 'a3', 'd6', 'a5', 'b6', 'd2', 'e5', 'e3'},
               'd4': {'b5', 'b3', 'e2', 'c2', 'c6', 'e6', 'f3', 'f5'},
               'e4': {'g5', 'g3', 'c5', 'd2', 'f6', 'c3', 'f2', 'd6'},
               'f4': {'h3', 'd3', 'd5', 'g2', 'e2', 'e6', 'g6', 'h5'}, 'g4': {'f6', 'h6', 'e5', 'f2', 'e3', 'h2'},
               'h4': {'f5', 'f3', 'g2', 'g6'}, 'b5': {'a3', 'd4', 'c3', 'c7', 'd6', 'a7'},
               'a5': {'c6', 'c4', 'b7', 'b3'}, 'c5': {'e4', 'd3', 'b3', 'a4', 'e6', 'd7', 'a6', 'b7'},
               'd5': {'b4', 'f4', 'b6', 'e7', 'f6', 'c3', 'c7', 'e3'},
               'e5': {'d3', 'g4', 'c6', 'd7', 'f3', 'g6', 'c4', 'f7'},
               'f5': {'g3', 'd6', 'd4', 'h4', 'e7', 'g7', 'h6', 'e3'}, 'g5': {'e4', 'h3', 'h7', 'e6', 'f3', 'f7'},
               'h5': {'f4', 'g7', 'g3', 'f6'}, 'b6': {'d5', 'a4', 'd7', 'a8', 'c8', 'c4'},
               'a6': {'c7', 'b4', 'c5', 'b8'}, 'c6': {'b4', 'a5', 'd4', 'e7', 'd8', 'e5', 'b8', 'a7'},
               'd6': {'e4', 'b5', 'c8', 'b7', 'f5', 'c4', 'e8', 'f7'},
               'e6': {'g5', 'f4', 'd4', 'c5', 'd8', 'f8', 'g7', 'c7'},
               'f6': {'e4', 'h7', 'd5', 'g4', 'd7', 'g8', 'e8', 'h5'}, 'g6': {'f4', 'e7', 'h4', 'f8', 'e5', 'h8'},
               'h6': {'g4', 'f5', 'g8', 'f7'}, 'b7': {'a5', 'd6', 'c5', 'd8'}, 'a7': {'c6', 'b5', 'c8'},
               'c7': {'b5', 'd5', 'e6', 'a8', 'a6', 'e8'}, 'd7': {'b6', 'c5', 'f8', 'f6', 'e5', 'b8'},
               'e7': {'d5', 'c6', 'g6', 'c8', 'f5', 'g8'}, 'f7': {'g5', 'd8', 'h6', 'e5', 'd6', 'h8'},
               'g7': {'e6', 'f5', 'e8', 'h5'}, 'h7': {'g5', 'f8', 'f6'}, 'b8': {'c6', 'd7', 'a6'}, 'a8': {'b6', 'c7'},
               'c8': {'b6', 'd6', 'a7', 'e7'}, 'd8': {'c6', 'f7', 'b7', 'e6'}, 'e8': {'g7', 'd6', 'c7', 'f6'},
               'f8': {'e6', 'd7', 'h7', 'g6'}, 'g8': {'e7', 'h6', 'f6'}, 'h8': {'g6', 'f7'}}


def find_path(start, end, visited=[]) -> int:
    if end in CONNECTIONS[start]:
        return 1
    return 1 + min([999] + [find_path(i, end, visited + [start]) for i in CONNECTIONS[start] if i not in visited])


def init(p1):
    ret = {i: 999 for i in CONNECTIONS.keys()}
    ret[p1] = 0
    return ret


def knight(p1, p2):
    distances = init(p1)
    queue = [p1]
    visited = []
    while queue:
        next_hop = queue.pop(0)
        visited.append(next_hop)

        for i in CONNECTIONS[next_hop]:
            distances[i] = min(distances[i], distances[next_hop] + 1)
            if distances[i] >= distances[p2]:
                continue
            if i not in visited:
                queue.append(i)
    return distances[p2]


if __name__ == '__main__':
    arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]
    for x in arr:
        z = knight(x[0], x[1])
        assert z == x[2], "{} to {}: expected {}, got {}".format(x[0], x[1], x[2], z)
