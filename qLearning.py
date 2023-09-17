import numpy as np

import gameParameters
import qLearning
from gameplayFunctions import *
from gameParameters import *
from gameWindow import *

qTable = {}
move = 'up'
previousBoard = gameParameters.board.copy()
pointsGottenForTheMove = -1.0
learningRate = 0.9
discountRate = 0.9


def turnBoardIntoNumber(B):
    currPower = ROWS * COLUMNS - 1
    
    base = gameParameters.playerID + 1
    
    boardNumber = 0
    for row in B:
        for column in row:
            boardNumber += int(column*pow(base, currPower))
            currPower -= 1
    
    return boardNumber


def getBestNextMove(oldBoard):
    boardUp = boardRight = boardDown = boardLeft = 0
    boards = [boardUp, boardRight, boardDown, boardLeft]
    moves = ['up', 'right', 'down', 'left']
    for direction in range(4):
        if (turnBoardIntoNumber(oldBoard), moves[direction]) in qTable:
            boards[direction] = qTable[(turnBoardIntoNumber(oldBoard), moves[direction])]
    
    return max(boards)


def getPointsForTheMove():
    if qLearning.previousBoard[gameParameters.playerY][gameParameters.playerX] == 0 or turnBoardIntoNumber(qLearning.previousBoard) == turnBoardIntoNumber(gameParameters.board):
        return -1
    else:
        return qLearning.previousBoard[gameParameters.playerY][gameParameters.playerX]


def calculateNewQvalue(boardMovePair):
    bestNextMoveValue = getBestNextMove(qLearning.board)
    if boardMovePair not in qTable:
        qTable[boardMovePair] = 0
    newQvalue = (1-learningRate)*qTable[boardMovePair] + learningRate*(getPointsForTheMove() + discountRate*bestNextMoveValue)
    
    return newQvalue
    
    
def updateTable():
    boardNumber = turnBoardIntoNumber(qLearning.previousBoard)
    qTable[(boardNumber, move)] = calculateNewQvalue((turnBoardIntoNumber(previousBoard), move))
    qLearning.previousBoard = gameParameters.board.copy()


def printQtable():
    for key, value in qTable.items():
        if value > -0.5:
            print(key, ": ", value)
        