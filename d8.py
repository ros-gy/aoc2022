# Day 8 - gy
import numpy


if __name__ == '__main__':

    file = open("d8_input.txt", "r")

    num_cols = len(file.readline().strip())
    file.seek(0)
    num_rows = sum(1 for line in file)

    # print(num_cols, num_rows)

    file.seek(0)
    trees = []
    for x in file:
        temp_row = []
        for i in range(num_cols):
            temp_row.append(x[i])
        trees.append(temp_row)

    file.close()

    # print(trees)
    # print(trees[1][0])

    num_visible = num_cols*2 + (num_rows-2)*2
    scenic_score = []

    for a in range(num_rows-2):
        for b in range(num_cols-2):
            visible_up = True
            visible_down = True
            visible_left = True
            visible_right = True

            loc_row = a+1
            loc_col = b+1

            tree_height = trees[loc_row][loc_col]
            # print(tree_height, loc_row, loc_col)

            # check up
            buffer_up = []
            c = loc_row - 1
            while c >= 0:
                if trees[c][loc_col] >= tree_height:
                    visible_up = False
                buffer_up.append(trees[c][loc_col])
                c += -1

            # check down
            buffer_down = []
            c = loc_row + 1
            while c < num_rows:
                if trees[c][loc_col] >= tree_height:
                    # print(trees[c][loc_col], tree_height)
                    visible_down = False
                buffer_down.append(trees[c][loc_col])
                c += 1

            # check left
            buffer_left = []
            d = loc_col - 1
            while d >= 0:
                if trees[loc_row][d] >= tree_height:
                    visible_left = False
                buffer_left.append(trees[loc_row][d])
                d += -1

            # check right
            buffer_right = []
            d = loc_col + 1
            while d < num_cols:
                if trees[loc_row][d] >= tree_height:
                    visible_right = False
                buffer_right.append(trees[loc_row][d])
                d += 1

            # print(loc_row, loc_col, visible_up, visible_down, visible_left, visible_right)
            if visible_up or visible_down or visible_left or visible_right:
                num_visible += 1
                # print("hidden: ", loc_row, loc_col)

            score_up = 0
            score_down = 0
            score_left = 0
            score_right = 0

            for i in range(len(buffer_up)):
                if int(buffer_up[i]) < int(tree_height):
                    score_up += 1
                else:
                    score_up += 1
                    break

            for i in range(len(buffer_down)):
                if int(buffer_down[i]) < int(tree_height):
                    score_down += 1
                else:
                    score_down += 1
                    break

            for i in range(len(buffer_left)):
                if int(buffer_left[i]) < int(tree_height):
                    score_left += 1
                else:
                    score_left += 1
                    break

            for i in range(len(buffer_right)):
                if int(buffer_right[i]) < int(tree_height):
                    score_right += 1
                else:
                    score_right += 1
                    break

            # print(score_up, score_down, score_left, score_right)
            scenic_score.append(score_up*score_down*score_left*score_right)

    print(num_visible)
    scenic_score.sort(reverse=True)
    print(scenic_score[0])


