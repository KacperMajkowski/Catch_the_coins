import time
import numpy as np

from gameplayFunctions import *
from gameParameters import *
from gameWindow import *
from qLearning import *

updateWindow()
print(board)
print("----------------")
for turn in range(TURNS):
    time.sleep(0.0001)
    clearPlayer()
    changePlayerPos()
    movePlayer()
    updateTable()
    print(board)
    qLearning.printQtable()
    print("----------------")
    maybeRestart()
    updateWindow()
