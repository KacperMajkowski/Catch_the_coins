import numpy as np

TURNS = 10

ROWS = 4
COLUMNS = 3

board = np.zeros((ROWS, COLUMNS))

playerPos = round(COLUMNS/2)
playerID = 100

board[ROWS - 1][playerPos] = playerID
