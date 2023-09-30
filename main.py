import time
import numpy as np
import pickle

import qLearning
from gameplayFunctions import *
from gameParameters import *
from gameWindow import *
from qLearning import *


def run():
    for turn in range(TURNS):
        updateWindow()
        changePlayerPos()
        movePlayer()
        updateTable()
        lowerExploRate()
        # time.sleep(0.1)
        if turn % 1000 == 0:
            print(turn)
            print("Explo rate:", qLearning.exploreRate)
        if turn == qLearning.targetMoves:
            restartBoard()
            qLearning.exploreRate = 0
            qLearning.saveTable()
        if turn > qLearning.targetMoves:
            time.sleep(0.1)
            print("Move made:", qLearning.move)
            print(gameParameters.board)
            print(qLearning.getBestNextMoveValue(gameParameters.board))
            print("Explo rate:", qLearning.exploreRate)
            print("Move values:", getNextMoves(gameParameters.board))
            # qLearning.printQtable()
            print("----------------")
        maybeRestart()
        
        
# qLearning.loadTable()
run()
    
    
    
