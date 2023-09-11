import numpy as np

TURNS = 1000

ROWS = 8
COLUMNS = 8

board = np.zeros((ROWS, COLUMNS))

playerX = round(COLUMNS/2)
playerY = round(COLUMNS/2)
playerID = 4

board[playerY][playerX] = playerID
