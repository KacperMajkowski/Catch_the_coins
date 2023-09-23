import numpy as np

TURNS = 100000000000

ROWS = 8
COLUMNS = 8

board = np.zeros((ROWS, COLUMNS))

playerX = COLUMNS - 1
playerY = ROWS - 1
playerID = 100


def setUpBoard():
    board[playerY][playerX] = playerID
    board[0][0] = 9
    board[1][0] = 19
    board[1][1] = 19
    board[1][2] = 19
    board[4][2] = 19
    board[4][3] = 19
    board[4][4] = 19
    board[6][5] = 19
    board[6][6] = 19
    board[6][7] = 19
    
    
setUpBoard()
endX = 0
endY = 0
