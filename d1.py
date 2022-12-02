# Day 1 - gy
if __name__ == '__main__':
    calorie_list = []
    file = open("d1_input.txt", "r")
    temp_cal = 0
    for x in file:
        if x.strip() != "":
            temp_cal += int(x)
        else:
            calorie_list.append(temp_cal)
            temp_cal = 0

    greatest = 0
    for y in calorie_list:
        if y > greatest:
            greatest = y

    print("Elf with most calories is carrying:", greatest, "calories.")

    calorie_list.sort(reverse=True)
    top3 = 0
    for i in range(3):
        top3 += calorie_list[i]
    print("Top 3 elves are carrying:", top3, "calories.")
