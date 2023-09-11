import numpy as np

import gameParameters
from gameplayFunctions import *
from gameParameters import *
from gameWindow import *

qTable = {}
pointsGottenForTheMove = 0


def turnBoardIntoNumber():
    currPower = ROWS * COLUMNS - 1
    
    base = gameParameters.playerID + 1
    
    boardNumber = 0
    for row in board:
        for column in row:
            boardNumber += int(column*pow(base, currPower))
            currPower -= 1
    
    return boardNumber
    
    
def updateTable():
    boardNumber = turnBoardIntoNumber()
    if boardNumber not in qTable:
        qTable[boardNumber] = pointsGottenForTheMove
        