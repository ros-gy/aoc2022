# Day 4 - gy

if __name__ == '__main__':

    file = open("d4_input.txt", "r")
    overlapping_shifts1 = 0
    overlapping_shifts2 = 0

    for x in file:
        y = x.split(',')
        shift1 = y[0].split('-')
        shift2 = y[1].split('-')

        shift1_start = int(shift1[0])
        shift1_end = int(shift1[1])
        shift2_start = int(shift2[0])
        shift2_end = int(shift2[1])

        if shift2_start >= shift1_start:
            if shift1_end >= shift2_end:
                overlapping_shifts1 += 1
            elif shift2_start <= shift1_end:
                overlapping_shifts2 += 1
        elif shift1_start >= shift2_start:
            if shift2_end >= shift1_end:
                overlapping_shifts1 += 1
            elif shift1_start <= shift2_end:
                overlapping_shifts2 += 1

    overlapping_shifts2 += overlapping_shifts1

    file.close()

    print("pt1. Number of overlapping shifts:", overlapping_shifts1)
    print("pt2. Number of overlapping shifts:", overlapping_shifts2)
