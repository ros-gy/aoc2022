# Day 2 - gy

def get_score1(opponent, play):
    if opponent == 'A':
        if play == 'X':
            result = 3
        elif play == 'Y':
            result = 6
        elif play == 'Z':
            result = 0

    if opponent == 'B':
        if play == 'X':
            result = 0
        elif play == 'Y':
            result = 3
        elif play == 'Z':
            result = 6

    if opponent == 'C':
        if play == 'X':
            result = 6
        elif play == 'Y':
            result = 0
        elif play == 'Z':
            result = 3

    if play == 'X':
        p = 1
    elif play == 'Y':
        p = 2
    elif play == 'Z':
        p = 3

    return result + p


def get_play_score(opponent, result):
    if result == 'X':  # Lose
        score_a = 0
        if opponent == 'A':
            play = 'C'
        elif opponent == 'B':
            play = 'A'
        elif opponent == 'C':
            play = 'B'

    if result == 'Y':  # Draw
        score_a = 3
        play = opponent

    if result == 'Z':  # Win
        score_a = 6
        if opponent == 'A':
            play = 'B'
        elif opponent == 'B':
            play = 'C'
        elif opponent == 'C':
            play = 'A'

    if play == 'A':
        score_b = 1
    elif play == 'B':
        score_b = 2
    elif play == 'C':
        score_b = 3

    return score_a + score_b


if __name__ == '__main__':
    score1 = 0
    score2 = 0
    file = open("d2_input.txt", "r")
    for x in file:
        a = x.split()
        score1 += get_score1(a[0], a[1])
        score2 += get_play_score(a[0], a[1])

    file.close()

    print("pt1. Using the guide, score would be:", score1, "points.")
    print("pt2. Using the guide, score would be:", score2, "points.")
