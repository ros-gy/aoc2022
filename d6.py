# Day 6 - gy

def compare(a1, a2, a3, a4):
    if a1 != a2 and a1 != a3 and a1 != a4:
        if a2 != a3 and a2 != a4:
            if a3 != a4:
                print(a1, a2, a3, a4)
                return True
    return False

def compare_big(a):
    found = True
    for i in range(14):
        if a.count(a[i]) != 1:
            found = False

    return found

if __name__ == '__main__':

    file = open("d6_input.txt", "r")

    x = file.readline()
    length = len(x)
    buffer = ["", "", "", ""]

    found_buffer = False

    # manually get the first four
    buffer[0] = x[0]
    buffer[1] = x[1]
    buffer[2] = x[2]
    buffer[3] = x[3]
    i = 0

    while not found_buffer:
        if compare(buffer[0], buffer[1], buffer[2], buffer[3]):
            found_buffer = True
        else:
            buffer[0] = buffer[1]
            buffer[1] = buffer[2]
            buffer[2] = buffer[3]
            buffer[3] = x[i+4]
            i += 1

    j = i+4  # assuming msg-start comes after packet-start
    found_msg = False
    msg_start = [""]*14
    while not found_msg:
        for k in range(14):
            msg_start[k] = x[j+k]
        if compare_big(msg_start):
            found_msg = True
        j += 1

    file.close()

    print("pt1. Position of packet: ", i+4)
    print("pt2. Position of msg:", j+13)
