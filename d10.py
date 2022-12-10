# Day 10 - gy

x = 1
tick = 0
log = []

if __name__ == '__main__':

    file = open("d10_input.txt", "r")

    for f in file:
        y = (f.strip()).split()
        if y[0] == "noop":
            tick += 1
            log.append(x)
        elif y[0] == "addx":
            tick += 1
            log.append(x)
            tick += 1
            x += int(y[1])
            log.append(x)

    file.close()

    # 20th, 60th, 100th, 140th, 180th, and 220th
    print(log[18], log[58], log[98], log[138], log[178], log[218])

    print("pt1: ", int(log[18])*20 + int(log[58])*60 + int(log[98])*100 + int(log[138])*140 + int(log[178])*180 + int(log[218])*220)