import numpy as np

from gameplayFunctions import *
from gameParameters import *
from gameWindow import *

qTable = np.zeros((pow(2, ROWS*COLUMNS), COLUMNS, 3))
pointsGottenForTheMove = 0


def turnBoardIntoNumber():
    currPower = (ROWS - 1) * COLUMNS - 1
    
    boardNumber = 0
    for row in board[:-1]:
        for column in row:
            boardNumber += column*pow(2, currPower)
            currPower -= 1
            
    boardNumber *= pow(10, 1 + COLUMNS // 10)
    boardNumber += gameParameters.playerPos
    
    return boardNumber
    