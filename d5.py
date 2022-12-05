# Day 5 - gy

def get_top(stacks, number):
    return number

if __name__ == '__main__':

    file = open("d5_input.txt", "r")

    stacks = []
    commands = []
    data_ready = False
    for x in file:
        temp = []
        temp_commands = []

        if not data_ready:
            for i in range(9):
                if x[i*4+1] == "1":
                    data_ready = True
                    break

                temp.append(x[i * 4 + 1])

        if not data_ready:
            stacks.append(temp)

        y = x.split(" ")
        if y[0] == "move":
            temp_commands = [y[1], y[3], y[5].strip()]
            commands.append(temp_commands)

    stacks.reverse()

    cols = []
    for i in range(9):
        temp2 = []
        for j in range(8):
            if stacks[j][i] != " ":
                temp2.append(stacks[j][i])
        cols.append(temp2)

    for z in commands:
        number = int(z[0])
        source = int(z[1])-1
        destination = int(z[2])-1

        temp_hold = []
        for k in range(number):
            t_copy = cols[source].pop(-1)
            temp_hold.append(t_copy)
            # cols[destination].append(t_copy)

        for u in range(len(temp_hold)):
            cols[destination].append(temp_hold.pop(-1))

    file.close()

    top_items1 = ""
    top_items2 = ""
    for p in range(9):
        top_items1 += cols[p][-1]
        top_items2 += cols[p][-1]

    print("pt1. List of top items:", top_items1)
    print("pt2. List of top items:", top_items2)
