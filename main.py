import time
import numpy as np

from gameplayFunctions import *
from gameParameters import *

for turn in range(TURNS):
    moveCoins()
    createNewCoins(50)
    print(board)
    time.sleep(1)
    