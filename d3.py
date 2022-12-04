# Day 3 - gy

def lookup_priority(item):
    if item.isupper():
        priority = ord(item) - 38
    else:
        priority = ord(item) - 96
    return priority

def get_badge_priority(elf_group):
    badge = ""
    badge_found = False
    for i in range(len(elf_group[0])):
        if not badge_found:
            for j in range(len(elf_group[1])):
                if elf_group[0][i] == elf_group[1][j]:
                    if not badge_found:
                        for k in range(len(elf_group[2])):
                            if elf_group[0][i] == elf_group[2][k]:
                                badge = elf_group[0][i]
                                badge_found = True
                                break

    return lookup_priority(badge)


if __name__ == '__main__':

    file = open("d3_input.txt", "r")

    line_grouper = 0
    group = ["", "", ""]

    priority_score1 = 0
    priority_score2 = 0

    for x in file:
        length = len(x)
        first, second = x[:length//2], x[length//2:]

        found = False
        for i in range(len(first)):
            if not found:
                for j in range(len(second)):
                    if first[i] == second[j]:
                        priority_score1 += lookup_priority(first[i])
                        found = True
                        break

        line_grouper += 1
        group[line_grouper-1] = x.strip()

        if line_grouper == 3:
            priority_score2 += get_badge_priority(group)
            group = ["", "", ""]
            line_grouper = 0

    file.close()

    print("pt1. Sum of priority of misplaced items:", priority_score1)
    print("pt2. Sum of priority of group badges:", priority_score2)
