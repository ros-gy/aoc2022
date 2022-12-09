# Day 9 - gy

r_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
r_y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

tail_visited = ["x=0 y=0"]


def step_head(direction, value):
    global r_x
    global r_y
    # print(direction, value, " - ", r_x[knot-1], r_y[knot-1])
    # print("Step head", direction, value)

    if direction == "U":
        for steps in range(int(value)):
            r_y[0] += 1
            step_tail(direction, 1)
    elif direction == "D":
        for steps in range(int(value)):
            r_y[0] += -1
            step_tail(direction, 1)
    elif direction == "L":
        for steps in range(int(value)):
            r_x[0] += -1
            step_tail(direction, 1)
    elif direction == "R":
        for steps in range(int(value)):
            r_x[0] += 1
            step_tail(direction, 1)


def step_tail(direction, knot):
    global r_x
    global r_y
    global tail_visited

    # hard part
    # check if we need to make a move
    if abs(r_x[knot-1]-r_x[knot]) > 1 or abs(r_y[knot-1]-r_y[knot]) > 1:
        # compare row and column
        if r_x[knot] == r_x[knot-1]:
            # check which direction to move
            if r_y[knot-1] > r_y[knot]:
                r_y[knot] += 1
            else:
                r_y[knot] += -1
        elif r_y[knot] == r_y[knot-1]:
            if r_x[knot-1] > r_x[knot]:
                r_x[knot] += 1
            else:
                r_x[knot] += -1
        else:
            if direction == "U":
                r_x[knot] = r_x[knot-1]
                r_y[knot] += 1
            elif direction == "D":
                r_x[knot] = r_x[knot-1]
                r_y[knot] += -1
            elif direction == "L":
                r_y[knot] = r_y[knot-1]
                r_x[knot] += -1
            elif direction == "R":
                r_y[knot] = r_y[knot-1]
                r_x[knot] += 1
    if knot < 9:
        step_tail(direction, knot+1)
    if knot == 9:
        tail_visited.append("x=" + str(r_x[knot]) + " y=" + str(r_y[knot]))  # non-unique list

    # print("Step tail", direction, value, last_value)


if __name__ == '__main__':

    file = open("d9_test.txt", "r")

    for x in file:
        y = (x.strip()).split()
        step_head(y[0], y[1])

    file.close()

    print("Final head position", r_x[0], r_y[0])
    print("Final tail position", r_x[9], r_y[9])

    unique_visited = set(tail_visited)

    print("pt1. Unique locations: ", len(unique_visited))
