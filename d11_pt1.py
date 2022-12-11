# Day 11 - gy

m0_items = [54, 82, 90, 88, 86, 54]
m1_items = [91, 65]
m2_items = [62, 54, 57, 92, 83, 63, 63]
m3_items = [67, 72, 68]
m4_items = [68, 89, 90, 86, 84, 57, 72, 84]
m5_items = [79, 83, 64, 58]
m6_items = [96, 72, 89, 70, 88]
m7_items = [79]

divider = [11, 5, 7, 2, 17, 13, 3, 19]
inspections = [0, 0, 0, 0, 0, 0, 0, 0]


def operation(m_id, worry):
    if m_id == 0:
        return worry * 7
    elif m_id == 1:
        return worry * 13
    elif m_id == 2:
        return worry + 1
    elif m_id == 3:
        return worry * worry
    elif m_id == 4:
        return worry + 7
    elif m_id == 5:
        return worry + 6
    elif m_id == 6:
        return worry + 4
    elif m_id == 7:
        return worry + 8


def test_worry(m_id, worry):
    if m_id == 0:
        if worry % divider[m_id] == 0:
            return True
        else:
            return False
    elif m_id == 1:
        if worry % divider[m_id] == 0:
            return True
        else:
            return False
    elif m_id == 2:
        if worry % divider[m_id] == 0:
            return True
        else:
            return False
    elif m_id == 3:
        if worry % divider[m_id] == 0:
            return True
        else:
            return False
    elif m_id == 4:
        if worry % divider[m_id] == 0:
            return True
        else:
            return False
    elif m_id == 5:
        if worry % divider[m_id] == 0:
            return True
        else:
            return False
    elif m_id == 6:
        if worry % divider[m_id] == 0:
            return True
        else:
            return False
    elif m_id == 7:
        if worry % divider[m_id] == 0:
            return True
        else:
            return False


def inspect(m_id):
    global m0_items
    global m1_items
    global m2_items
    global m3_items
    global m4_items
    global m5_items
    global m6_items
    global m7_items
    global inspections

    if m_id == 0:
        for item in m0_items:
            inspections[m_id] += 1
            temp = relief(operation(m_id, item))
            if test_worry(m_id, temp):
                m2_items.append(temp)
            else:
                m6_items.append(temp)
        m0_items.clear()
    elif m_id == 1:
        for item in m1_items:
            inspections[m_id] += 1
            temp = relief(operation(m_id, item))
            if test_worry(m_id, temp):
                m7_items.append(temp)
            else:
                m4_items.append(temp)
        m1_items.clear()
    elif m_id == 2:
        for item in m2_items:
            inspections[m_id] += 1
            temp = relief(operation(m_id, item))
            if test_worry(m_id, temp):
                m1_items.append(temp)
            else:
                m7_items.append(temp)
        m2_items.clear()
    elif m_id == 3:
        for item in m3_items:
            inspections[m_id] += 1
            temp = relief(operation(m_id, item))
            if test_worry(m_id, temp):
                m0_items.append(temp)
            else:
                m6_items.append(temp)
        m3_items.clear()
    elif m_id == 4:
        for item in m4_items:
            inspections[m_id] += 1
            temp = relief(operation(m_id, item))
            if test_worry(m_id, temp):
                m3_items.append(temp)
            else:
                m5_items.append(temp)
        m4_items.clear()
    elif m_id == 5:
        for item in m5_items:
            inspections[m_id] += 1
            temp = relief(operation(m_id, item))
            if test_worry(m_id, temp):
                m3_items.append(temp)
            else:
                m0_items.append(temp)
        m5_items.clear()
    elif m_id == 6:
        for item in m6_items:
            inspections[m_id] += 1
            temp = relief(operation(m_id, item))
            if test_worry(m_id, temp):
                m1_items.append(temp)
            else:
                m2_items.append(temp)
        m6_items.clear()
    elif m_id == 7:
        for item in m7_items:
            inspections[m_id] += 1
            temp = relief(operation(m_id, item))
            if test_worry(m_id, temp):
                m4_items.append(temp)
            else:
                m5_items.append(temp)
        m7_items.clear()


def relief(worry):
    return int(worry / 3)


if __name__ == '__main__':

    for i in range(20):
        for k in range(8):
            inspect(k)

    # print(m0_items)
    # print(m1_items)
    # print(m2_items)
    # print(m3_items)

    print(inspections)

    inspections.sort(reverse=True)
    print(inspections[0], inspections[1])
    print("monkey business", inspections[0]*inspections[1])

