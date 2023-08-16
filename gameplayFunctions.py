import random

from gameParameters import *


def moveCoins():
    for row in range(ROWS - 1, 0, -1):
        for column in range(COLUMNS):
            board[row][column] = board[row - 1][column]
            

def createNewCoins(coinChance):
    for column in range(COLUMNS):
        toss = random.randint(1, 101)
        if toss < coinChance:
            board[0][column] = 1
        else:
            board[0][column] = 0
