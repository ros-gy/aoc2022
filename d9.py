# Day 9 - gy

h_x = 0
h_y = 0

h_x_last = 0
h_y_last = 0

t_x = 0
t_y = 0

tail_visited = ["x=0 y=0"]


def step_head(direction, value):
    global h_x
    global h_y
    global h_x_last
    global h_y_last
    # print(direction, value, " - ", h_x, h_y)
    # print("Step head", direction, value)

    if direction == "U":
        for steps in range(int(value)):
            h_y_last = h_y
            h_y += 1
            step_tail(direction, h_y, h_y_last)
    elif direction == "D":
        for steps in range(int(value)):
            h_y_last = h_y
            h_y += -1
            step_tail(direction, h_y, h_y_last)
    elif direction == "L":
        for steps in range(int(value)):
            h_x_last = h_x
            h_x += -1
            step_tail(direction, h_x, h_x_last)
    elif direction == "R":
        for steps in range(int(value)):
            h_x_last = h_x
            h_x += 1
            step_tail(direction, h_x, h_x_last)


def step_tail(direction, value, last_value):
    global t_x
    global t_y
    global tail_visited

    # hard part
    # check if we need to make a move
    if abs(h_x-t_x) > 1 or abs(h_y-t_y) > 1:
        # compare row and column
        if t_x == h_x:
            # check which direction to move
            if h_y > t_y:
                t_y += 1
            else:
                t_y += -1
        elif t_y == h_y:
            if h_x > t_x:
                t_x += 1
            else:
                t_x += -1
        else:
            if direction == "U":
                t_x = h_x
                t_y += 1
            elif direction == "D":
                t_x = h_x
                t_y += -1
            elif direction == "L":
                t_y = h_y
                t_x += -1
            elif direction == "R":
                t_y = h_y
                t_x += 1

    tail_visited.append("x=" + str(t_x) + " y=" + str(t_y))  # non-unique list

    # print("Step tail", direction, value, last_value)


if __name__ == '__main__':

    file = open("d9_input.txt", "r")

    for x in file:
        y = (x.strip()).split()
        step_head(y[0], y[1])
        # print(y)

    file.close()

    # print("Final head position", h_x, h_y)
    # print("Final tail position", t_x, t_y)

    unique_visited = set(tail_visited)
    print(len(tail_visited))
    print(unique_visited)

    # remove dup
    count = []
    for x in tail_visited:
        if x not in count:
            count.append(x)

    print(len(count))
    print("pt1. Unique locations: ", len(unique_visited))
