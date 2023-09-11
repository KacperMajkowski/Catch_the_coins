import random

import gameParameters
import qLearning
from gameParameters import *
from qLearning import *


def moveCoins():
    for row in range(ROWS - 1, 0, -1):
        for column in range(COLUMNS):
            board[row][column] = board[row - 1][column]
            
     
def changePlayerPos():
    toss = random.randint(1, 101)
    if toss < 40:
        gameParameters.playerPos = max(0, gameParameters.playerPos - 1)  # Move left
    elif toss > 60:
        gameParameters.playerPos = min(gameParameters.COLUMNS - 1, gameParameters.playerPos + 1)  # Move right
        
        
def movePlayer():
    qLearning.pointsGottenForTheMove = board[ROWS - 1][gameParameters.playerPos]
    board[ROWS - 1][gameParameters.playerPos] = 100
            

def createNewCoins(coinChance):
    for column in range(COLUMNS):
        toss = random.randint(1, 101)
        if toss < coinChance:
            board[0][column] = 1
        else:
            board[0][column] = 0
