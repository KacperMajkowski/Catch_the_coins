import numpy as np

TURNS = 100000000000

ROWS = 8
COLUMNS = 8

board = np.zeros((ROWS, COLUMNS))

playerX = COLUMNS - 1
playerY = ROWS - 1
playerID = 50

board[playerY][playerX] = playerID
board[0][0] = 20
board[0][ROWS - 1] = 40
board[COLUMNS - 1][0] = 10

endX = 0
endY = COLUMNS - 1
