import time
import numpy as np

from gameplayFunctions import *
from gameParameters import *
from gameWindow import *
from qLearning import *

updateWindow()
for turn in range(TURNS):
    moveCoins()
    changePlayerPos()
    movePlayer()
    print(qLearning.pointsGottenForTheMove)
    createNewCoins(20)
    print(board)
    updateWindow()
    time.sleep(0.1)
    