import numpy as np

TURNS = 100000

ROWS = 8
COLUMNS = 8

board = np.zeros((ROWS, COLUMNS))

playerX = COLUMNS - 1
playerY = ROWS - 1
playerID = 4

board[playerY][playerX] = playerID
board[0][0] = 1

endX = 0
endY = 0
