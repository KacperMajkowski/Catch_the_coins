import time
import numpy as np

from gameplayFunctions import *
from gameParameters import *
from gameWindow import *
from qLearning import *

for turn in range(TURNS):
    changePlayerPos()
    movePlayer()
    updateTable()
    lowerExploRate()
    if turn % 1000 == 0:
        print(turn)
        print("Explo rate:", qLearning.exploreRate)
    if turn > 100000:
        qLearning.exploreRate = 0
        time.sleep(0.1)
        print(board)
        print(qLearning.getBestNextMoveValue(board))
        print("Explo rate:", qLearning.exploreRate)
        print("Move:", qLearning.move)
        # qLearning.printQtable()
        print("----------------")
    updateWindow()
    maybeRestart()
    
    
    
