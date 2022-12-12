# Day 12 - gy

def h(letter):
    return ord(letter)


def compare(l, n):
    ll = h(l)
    nn = h(n)
    if l == 'S':
        ll = 96
    if n == 'E':
        nn = 123
    if nn-ll < 2:
        return True
    else:
        return False


# lifted from https://onestepcode.com/graph-shortest-path-python/
def shortest_path(graph, node1, node2):
    path_list = [[node1]]
    path_index = 0
    # To keep track of previously visited nodes
    previous_nodes = {node1}
    if node1 == node2:
        return path_list[0]

    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = graph[last_node]
        # Search goal node
        if node2 in next_nodes:
            current_path.append(node2)
            return current_path
        # Add new paths
        for next_node in next_nodes:
            if not next_node in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                # To avoid backtracking
                previous_nodes.add(next_node)
        # Continue to next path in list
        path_index += 1
    # No path is found
    return []


def makestring(x, y):
    return str(x) + " " + str(y)


if __name__ == '__main__':

    file = open("d12_input.txt", "r")

    num_cols = len(file.readline().strip())
    file.seek(0)
    num_rows = sum(1 for line in file)

    # print(num_cols, num_rows)
    startx = 0
    starty = 0
    endx = 0
    endy = 0

    elevation_as = []

    file.seek(0)
    elmap = []
    for x in file:
        temp_row = []
        for i in range(num_cols):
            temp_row.append(x[i])
        elmap.append(temp_row)

    file.close()

    for a in range(num_rows):
        for b in range(num_cols):
            if elmap[a][b] == 'a':
                elevation_as.append(makestring(b, a))
            elif elmap[a][b] == "E":
                endx = b
                endy = a

    print(startx, starty)
    print(endx, endy)

    for a in range(num_rows):
        print("".join(elmap[a]))

    graph = {}

    # create dictionary
    for a in range(num_rows):
        for b in range(num_cols):
            name = makestring(b, a)
            paths = []
            if a != 0 and b != 0 and a != num_rows-1 and b != num_cols-1:
                if compare(elmap[a][b], elmap[a-1][b]):
                    paths.append(makestring(b, a-1))
                if compare(elmap[a][b], elmap[a+1][b]):
                    paths.append(makestring(b, a+1))
                if compare(elmap[a][b], elmap[a][b-1]):
                    paths.append(makestring(b-1, a))
                if compare(elmap[a][b], elmap[a][b+1]):
                    paths.append(makestring(b+1, a))
            elif a != 0 and b != 0 and a != num_rows-1:
                if compare(elmap[a][b], elmap[a - 1][b]):
                    paths.append(makestring(b, a - 1))
                if compare(elmap[a][b], elmap[a + 1][b]):
                    paths.append(makestring(b, a + 1))
                if compare(elmap[a][b], elmap[a][b - 1]):
                    paths.append(makestring(b - 1, a))
            elif a != 0 and b != 0 and b != num_cols-1:
                if compare(elmap[a][b], elmap[a - 1][b]):
                    paths.append(makestring(b, a - 1))
                if compare(elmap[a][b], elmap[a][b - 1]):
                    paths.append(makestring(b - 1, a))
                if compare(elmap[a][b], elmap[a][b + 1]):
                    paths.append(makestring(b + 1, a))
            elif a != 0 and a != num_rows-1 and b != num_cols-1:
                if compare(elmap[a][b], elmap[a-1][b]):
                    paths.append(makestring(b, a-1))
                if compare(elmap[a][b], elmap[a+1][b]):
                    paths.append(makestring(b, a+1))
                if compare(elmap[a][b], elmap[a][b+1]):
                    paths.append(makestring(b+1, a))
            elif b != 0 and a != num_rows-1 and b != num_cols-1:
                if compare(elmap[a][b], elmap[a+1][b]):
                    paths.append(makestring(b, a+1))
                if compare(elmap[a][b], elmap[a][b-1]):
                    paths.append(makestring(b-1, a))
                if compare(elmap[a][b], elmap[a][b+1]):
                    paths.append(makestring(b+1, a))
            elif a == 0 and b == 0:
                if compare(elmap[a][b], elmap[a+1][b]):
                    paths.append(makestring(b, a+1))
                if compare(elmap[a][b], elmap[a][b+1]):
                    paths.append(makestring(b+1, a))
            elif a == 0 and b == num_cols-1:
                if compare(elmap[a][b], elmap[a+1][b]):
                    paths.append(makestring(b, a+1))
                if compare(elmap[a][b], elmap[a][b-1]):
                    paths.append(makestring(b-1, a))
            elif a == num_rows-1 and b == 0:
                if compare(elmap[a][b], elmap[a-1][b]):
                    paths.append(makestring(b, a-1))
                if compare(elmap[a][b], elmap[a][b+1]):
                    paths.append(makestring(b+1, a))
            elif a == num_rows-1 and b == num_cols-1:
                if compare(elmap[a][b], elmap[a-1][b]):
                    paths.append(makestring(b, a-1))
                if compare(elmap[a][b], elmap[a][b-1]):
                    paths.append(makestring(b-1, a))
            graph.update({name: paths})

    print(elevation_as)
    # print(graph)
    short_scenic_path_lengths = []
    for spots in elevation_as:
        stops = len(shortest_path(graph, spots, makestring(endx, endy)))-1
        if stops > 0:
            short_scenic_path_lengths.append(stops)

    short_scenic_path_lengths.sort()
    print(short_scenic_path_lengths)
    print(short_scenic_path_lengths[0])
