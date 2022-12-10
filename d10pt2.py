# Day 10 - gy

x = 1
tick = 0
log = []
sprite_position = [0, 1, 2]
image = []

def get_pixel():
    a = sprite_position[0]
    b = sprite_position[1]
    c = sprite_position[2]
    if tick % 40 == a or tick % 40 == b or tick % 40 == c:
        return "#"
    else:
        return "."


def draw():

    l1 = image[0:40]
    l2 = image[40:80]
    l3 = image[80:120]
    l4 = image[120:160]
    l5 = image[160:200]
    l6 = image[200:240]
    print("".join(l1))
    print("".join(l2))
    print("".join(l3))
    print("".join(l4))
    print("".join(l5))
    print("".join(l6))


if __name__ == '__main__':

    file = open("d10_input.txt", "r")
    image.append(get_pixel())
    for f in file:
        y = (f.strip()).split()
        if y[0] == "noop":
            tick += 1
            log.append(x)
            image.append(get_pixel())
        elif y[0] == "addx":
            tick += 1
            log.append(x)
            image.append(get_pixel())
            tick += 1
            x += int(y[1])
            sprite_position = [x-1, x, x+1]
            log.append(x)
            image.append(get_pixel())

    file.close()

    # 20th, 60th, 100th, 140th, 180th, and 220th
    # print(log[18], log[58], log[98], log[138], log[178], log[218])
    # print(log)

    # print("pt1: ", int(log[18])*20 + int(log[58])*60 + int(log[98])*100 + int(log[138])*140 + int(log[178])*180 + int(log[218])*220)

    draw()

    print(image)
    # print(log)

    # print(0%40, 1%40, 36%40)
    # print(40%40, 41%40, 76%40)