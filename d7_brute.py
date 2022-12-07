# Day 7 - gy

file_r = open("d7_input.txt", "r")
temp_file = file_r.readlines()
file_r.close()


def getstringpath(cur_list):
    path_string = ""
    for k in cur_list:
        if k == "/":
            path_string += k
        else:
            path_string += k + "/"
    return path_string


def get_size(name, path):
    getting_data = False
    count = 0
    temp_size = 0
    cur_dir2 = []

    # print("get size of", name, "at", path)

    # find beginning of data
    for x in temp_file:
        path_string = ""
        count += 1

        y = (x.strip()).split()
        if y[0] == "$":
            if y[1] == "cd":
                if y[2] != "..":
                    cur_dir2.append(y[2])
                    if y[2] == name and getstringpath(cur_dir2) == path:
                        # print("!!match", path, " = ", getstringpath(cur_dir2))
                        path_string = getstringpath(cur_dir2)
                        getting_data = True
                        break
                else:
                    cur_dir2.pop(-1)

    i = 1
    while getting_data:
        # print("COUNT IS ", count)
        z = ((temp_file[count + i]).strip()).split()
        i += 1
        # print(z)
        if z[0] == "dir":
            if z[1] != name:
                temp_size += get_size(z[1], path_string+z[1]+"/")
            else:
                temp_size += get_size(z[1], path_string+z[1]+"/")
        elif z[0] == "$":
            if z[1] != "ls":
                getting_data = False
        else:
            temp_size += int(z[0])

    # print(name, temp_size)
    if temp_size == 0:
        print("error size zero for ", path, "line", count)
    return temp_size


if __name__ == '__main__':
    # global a, b
    file = open("d7_input.txt", "r")

    temp_names = ["/"]
    temp_path = ["/"]
    cur_dir = []
    # discover all directories
    for x in file:
        y = (x.strip()).split()
        if y[0] == "$":
            if y[1] == "cd":
                if y[2] != "..":
                    cur_dir.append(y[2])
                else:
                    cur_dir.pop(-1)
        if y[0] == "dir":
            path_string = getstringpath(cur_dir)

            # print("found_directory: ", y[1], "at ", path_string)
            temp_names.append(y[1])
            temp_path.append(path_string+y[1]+"/")

    file.close()

    # print(len(temp_names), len(temp_path))
    # print(temp_path)
    # print(temp_names)
    # print(temp_names[0], temp_path[0])

    size_info = []
    # print(temp_path[temp_names.index("vsztsjfh")])

    for i in range(len(temp_names)):
        size_info.append(get_size(temp_names[i], temp_path[i]))

    used_space = size_info[0]

    part1 = 0
    for p in size_info:
        if p == 0:
            print("ERROR")
        if p <= 100000:
            part1 += p

    print("part 1:", part1)

    free_space = 70000000-used_space
    free_up = 30000000-free_space

    delete_options = []
    for u in size_info:
        if u > free_up:
            delete_options.append(u)

    delete_options.sort()
    print("part 2:", delete_options[0])


