import numpy as np

TURNS = 100000000000

ROWS = 8
COLUMNS = 8

board = np.zeros((ROWS, COLUMNS))

playerX = COLUMNS - 1
playerY = ROWS - 1
playerID = 100

endX = 4
endY = 4


def setUpBoard():
    board[playerY][playerX] = playerID
    board[endY][endX] = 20
    board[0][0] = 9
    board[1][0] = 19
    board[1][1] = 19
    board[1][2] = 9
    board[2][3] = 9
    board[3][3] = 19
    board[4][2] = 9
    board[4][3] = 19
    board[6][5] = 19
    board[6][6] = 19
    board[6][7] = 9
    board[7][0] = 19
    board[0][7] = 9
    board[5][7] = 19
    board[2][2] = 9
    board[3][0] = 9
    board[6][4] = 9
    board[1][3] = 19
    board[4][5] = 9
    
    
setUpBoard()

