import random

import gameParameters
import qLearning
from gameParameters import *
from qLearning import *


def clearPlayer():
    board[gameParameters.playerY][gameParameters.playerX] = 0
    
     
def changePlayerPos():
    toss = random.randint(1, 101)
    if toss < 25:
        gameParameters.playerY = max(0, gameParameters.playerY - 1)  # Move up
        qLearning.move = 'up'
    elif toss < 50:
        gameParameters.playerX = min(gameParameters.COLUMNS - 1, gameParameters.playerX + 1)  # Move right
        qLearning.move = 'right'
    elif toss < 75:
        gameParameters.playerY = min(gameParameters.ROWS - 1, gameParameters.playerY + 1)  # Move down
        qLearning.move = 'down'
    else:
        gameParameters.playerX = max(0, gameParameters.playerX - 1)  # Move left
        qLearning.move = 'left'
    
        
def movePlayer():
    qLearning.pointsGottenForTheMove = board[gameParameters.playerY][gameParameters.playerX]
    board[gameParameters.playerY][gameParameters.playerX] = gameParameters.playerID
    
    
def maybeRestart():
    if gameParameters.playerY == gameParameters.endY and gameParameters.playerX == gameParameters.endX:
        restartBoard()
    
    
def restartBoard():
    gameParameters.playerX = COLUMNS - 1
    gameParameters.playerY = ROWS - 1
    
    board[playerY][playerX] = playerID
    board[0][0] = 1
    
    qLearning.previousBoard = board
    

