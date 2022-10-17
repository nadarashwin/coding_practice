# Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
#
# Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).
#
# Example 1:
# Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
# Output: 2
#
# Example 2:
# Input: board = [["."]]
# Output: 0


def countBattleships(data):
    if len(data) < 1:
        return 0
    m = len(data)
    n = len(data[0])
    counter = 0

    for i in range(m):
        for j in range(n):
            if (
                # Once we found a top-left 'X', we found a battleship
                (data[i][j] == 'X') and
                # column based lookup -> one above
                (i == 0 or data[i-1][j] == '.') and
                # row based lookup -> one on the left
                (j == 0 or data[i][j-1] == '.')
            ):
                counter += 1
    return counter


print(countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
print(countBattleships([["X","X",".","X"],["X","X",".","X"],["X","X",".","X"]]))


# ["X",".",".","X"]
# [".",".",".","X"]
# [".",".",".","X"]


# ["X",".",".","X"]
# ["X","X",".","X"]
# ["X","X",".","X"]
