import random

import gameParameters
import qLearning
import test
from gameParameters import *
from qLearning import *
    
     
def changePlayerPos():
    oldPlayerX = gameParameters.playerX
    oldPlayerY = gameParameters.playerY
    shouldExplore = random.randint(1, 101)
    if shouldExplore < qLearning.exploreRate*100:
        toss = random.randint(1, 100)
        # while illegalMove(toss):
        #    toss = random.randint(1, 100)
        if toss <= 25:
            gameParameters.playerY = max(0, gameParameters.playerY - 1)  # Move up
            qLearning.move = 'up'
        elif toss <= 50:
            gameParameters.playerX = min(gameParameters.COLUMNS - 1, gameParameters.playerX + 1)  # Move right
            qLearning.move = 'right'
        elif toss <= 75:
            gameParameters.playerY = min(gameParameters.ROWS - 1, gameParameters.playerY + 1)  # Move down
            qLearning.move = 'down'
        elif toss <= 100:
            gameParameters.playerX = max(0, gameParameters.playerX - 1)  # Move left
            qLearning.move = 'left'
        else:
            print("ERROR toss =", toss)
    else:
        bestMove = qLearning.getBestNextMove(board)
        if bestMove == 'up':
            gameParameters.playerY = max(0, gameParameters.playerY - 1)  # Move up
            qLearning.move = 'up'
        elif bestMove == 'right':
            gameParameters.playerX = min(gameParameters.COLUMNS - 1, gameParameters.playerX + 1)  # Move right
            qLearning.move = 'right'
        elif bestMove == 'down':
            gameParameters.playerY = min(gameParameters.ROWS - 1, gameParameters.playerY + 1)  # Move down
            qLearning.move = 'down'
        elif bestMove == 'left':
            gameParameters.playerX = max(0, gameParameters.playerX - 1)  # Move left
            qLearning.move = 'left'
        else:
            print("ERROR bestMove=", bestMove)
            
    board[oldPlayerY][oldPlayerX] = 0
    
    
def illegalMove(toss):
    if toss <= 25 and gameParameters.playerY == 0:
        return True
    elif 25 < toss <= 50 and gameParameters.playerX == gameParameters.COLUMNS - 1:
        return True
    elif 50 < toss <= 75 and gameParameters.playerY == gameParameters.ROWS - 1:
        return True
    elif 75 < toss <= 100 and gameParameters.playerX == 0:
        return True
    else:
        return False
    
        
def movePlayer():
    qLearning.pointsGottenForTheMove = board[gameParameters.playerY][gameParameters.playerX]
    effectsOfTheMove(gameParameters.playerY, gameParameters.playerX)
    board[gameParameters.playerY][gameParameters.playerX] = gameParameters.playerID
    
    
def effectsOfTheMove(y, x):
    if 20 < gameParameters.board[y][x] < 30:
        for col in range(len(gameParameters.board)):
            for row in range(len(gameParameters.board[col])):
                if gameParameters.board[col][row] == gameParameters.board[y][x] + 10:
                    gameParameters.board[col][row] = 0
    
    
def maybeRestart():
    if gameParameters.playerY == gameParameters.endY and gameParameters.playerX == gameParameters.endX:
        qLearning.updateTable()
        restartBoard()
        test.finishRun()
    
    
def restartBoard():
    gameParameters.board[gameParameters.playerY][gameParameters.playerX] = 0
    
    gameParameters.playerX = COLUMNS - 1
    gameParameters.playerY = ROWS - 1

    setUpBoard()
    
    qLearning.previousBoard = gameParameters.board.copy()
    

