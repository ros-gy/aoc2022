# Day 11 - gy
# import numpy as np # import numpy package
import sys
sys.set_int_max_str_digits(1000000)

m0_items = [79, 98]
m1_items = [54, 65, 75, 74]
m2_items = [79, 60, 97]
m3_items = [74]

m0_inspections = 0
m1_inspections = 0
m2_inspections = 0
m3_inspections = 0


def divisible23(num):
    print()

def divisible19(num):
    print()

def divisible13(num):
    print()

def divisible17(num):
    print()




def operation(m_id, worry):
    if m_id == 0:
        return worry * 19
    elif m_id == 1:
        return worry + 6
    elif m_id == 2:
        return worry * worry
    elif m_id == 3:
        return worry + 3


def test_worry(m_id, worry):
    str_worry = str(worry)
    if m_id == 0:
        if divisible(str_worry, 23):
            return True
        else:
            return False
    elif m_id == 1:
        if divisible(str_worry, 19):
            return True
        else:
            return False
    elif m_id == 2:
        if divisible(str_worry, 13):
            return True
        else:
            return False
    elif m_id == 3:
        if divisible(str_worry, 17):
            return True
        else:
            return False


def inspect(m_id):
    global m0_items
    global m1_items
    global m2_items
    global m3_items
    global m0_inspections
    global m1_inspections
    global m2_inspections
    global m3_inspections

    if m_id == 0:
        for item in m0_items:
            m0_inspections += 1
            temp = relief(operation(m_id, item))
            if test_worry(m_id, temp):
                m2_items.append(temp)
            else:
                m3_items.append(temp)
        m0_items.clear()
    elif m_id == 1:
        for item in m1_items:
            m1_inspections += 1
            temp = relief(operation(m_id, item))
            if test_worry(m_id, temp):
                m2_items.append(temp)
            else:
                m0_items.append(temp)
        m1_items.clear()
    elif m_id == 2:
        for item in m2_items:
            m2_inspections += 1
            temp = relief(operation(m_id, item))
            if test_worry(m_id, temp):
                m1_items.append(temp)
            else:
                m3_items.append(temp)
        m2_items.clear()
    elif m_id == 3:
        for item in m3_items:
            m3_inspections += 1
            temp = relief(operation(m_id, item))
            if test_worry(m_id, temp):
                m0_items.append(temp)
            else:
                m1_items.append(temp)
        m3_items.clear()


def relief(worry):
    return worry
    # return int(worry/3)


if __name__ == '__main__':

    for i in range(1000):
        print(i)
        for k in range(4):
            inspect(k)

    # print(m0_items)
    # print(m1_items)
    # print(m2_items)
    # print(m3_items)

    print(m0_inspections, m1_inspections, m2_inspections, m3_inspections)

