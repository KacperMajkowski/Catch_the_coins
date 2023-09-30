import pickle
import numpy as np


import gameParameters
import qLearning
from gameplayFunctions import *
from gameParameters import *
from gameWindow import *

qTable = {}


def saveTable():
    file = open('qTable.txt', 'wb')
    pickle.dump(qLearning.qTable, file)
    file.close()


def loadTable():
    file = open('qTable.txt', 'rb')
    qLearning.qTable = pickle.load(file)
    file.close()


move = 'up'
previousBoard = gameParameters.board.copy()
learningRate = 0.75
discountRate = 0.99
targetMoves = 500000
exploreRate = 1
targetExploreRate = 0.3
exploreRateMultiplier = pow(targetExploreRate, 1/targetMoves)


def turnBoardIntoNumber(B):
    currPower = ROWS * COLUMNS - 1
    
    base = gameParameters.playerID + 1
    
    boardNumber = 0
    for row in B:
        for column in row:
            boardNumber += int(column*pow(base, currPower))
            currPower -= 1
    
    return boardNumber


def getNextMoves(oldBoard):
    boardUp = boardRight = boardDown = boardLeft = 0
    boards = [boardUp, boardRight, boardDown, boardLeft]
    moves = ['up', 'right', 'down', 'left']
    for direction in range(4):
        if (turnBoardIntoNumber(oldBoard), moves[direction]) in qTable:
            boards[direction] = qTable[(turnBoardIntoNumber(oldBoard), moves[direction])]
    
    return boards


def getBestNextMove(oldBoard):
    boardUp = boardRight = boardDown = boardLeft = 0
    boards = [boardUp, boardRight, boardDown, boardLeft]
    moves = ['up', 'right', 'down', 'left']
    for direction in range(4):
        if (turnBoardIntoNumber(oldBoard), moves[direction]) in qTable:
            boards[direction] = qTable[(turnBoardIntoNumber(oldBoard), moves[direction])]
    
    return moves[boards.index(max(boards))]


def getBestNextMoveValue(oldBoard):
    boardUp = boardRight = boardDown = boardLeft = 0
    boards = [boardUp, boardRight, boardDown, boardLeft]
    moves = ['up', 'right', 'down', 'left']
    for direction in range(4):
        if (turnBoardIntoNumber(oldBoard), moves[direction]) in qTable:
            boards[direction] = qTable[(turnBoardIntoNumber(oldBoard), moves[direction])]
            
    return max(boards)


def getPointsForTheMove():
    squareNumber = qLearning.previousBoard[gameParameters.playerY][gameParameters.playerX]
    if turnBoardIntoNumber(qLearning.previousBoard) == turnBoardIntoNumber(gameParameters.board):  # Move into a wall
        return -100000
    elif squareNumber == 0:  # Empty square
        return -1
    elif squareNumber < 10:  # Coin positive
        return 100 * qLearning.previousBoard[gameParameters.playerY][gameParameters.playerX]
    elif squareNumber < 20:  # Coin negative
        return -1000 * (qLearning.previousBoard[gameParameters.playerY][gameParameters.playerX] - 10)
    elif squareNumber == 20:  # End tile
        return 1000


def calculateNewQvalue(boardMovePair):
    bestNextMoveValue = getBestNextMoveValue(qLearning.board)
    if boardMovePair not in qTable:
        qTable[boardMovePair] = 0
    newQvalue = (1-learningRate)*qTable[boardMovePair] + learningRate*(getPointsForTheMove() + discountRate*bestNextMoveValue)
    
    return newQvalue
    
    
def updateTable():
    boardNumber = turnBoardIntoNumber(qLearning.previousBoard)
    qTable[(boardNumber, move)] = calculateNewQvalue((turnBoardIntoNumber(previousBoard), move))
    qLearning.previousBoard = gameParameters.board.copy()
    
    
def lowerExploRate():
    qLearning.exploreRate = qLearning.exploreRate * exploreRateMultiplier


def printQtable():
    for key, value in qTable.items():
        print(key, ": ", value)
        