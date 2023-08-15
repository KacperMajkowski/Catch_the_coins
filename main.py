import time
import numpy as np

TURNS = 5

ROWS = 6
COLUMNS = 5

board = np.zeros((ROWS, COLUMNS))

board[0][3] = 1

for turn in range(TURNS):
    for row in range(ROWS - 1, 0, -1):
        for column in range(COLUMNS):
            board[row][column] = board[row - 1][column]
        
    for column in range(COLUMNS):
        board[0][column] = 0
        
    print(board)
    time.sleep(1)
    