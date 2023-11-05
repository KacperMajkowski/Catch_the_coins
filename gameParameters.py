import numpy as np

TURNS = 100000000000

ROWS = 8
COLUMNS = 8

board = np.zeros((ROWS, COLUMNS))

playerX = COLUMNS - 1
playerY = ROWS - 1
playerID = 100

endX = 0
endY = 0


def setUpBoard():
    board[playerY][playerX] = playerID
    board[endY][endX] = 20
    board[2][5] = 9
    
setUpBoard()

