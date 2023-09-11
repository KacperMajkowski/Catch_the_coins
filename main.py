import time
import numpy as np

from gameplayFunctions import *
from gameParameters import *
from gameWindow import *
from qLearning import *

updateWindow()
for turn in range(TURNS):
    clearPlayer()
    changePlayerPos()
    movePlayer()
    updateTable()
    print(qLearning.pointsGottenForTheMove)
    print(board)
    print(turnBoardIntoNumber())
    print(qLearning.qTable)
    updateWindow()
    time.sleep(0.001)
    
print(len(qLearning.qTable))
