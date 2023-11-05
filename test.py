import gameParameters
import gameWindow
import gameplayFunctions
import qLearning
import test

import time
import matplotlib.pyplot as plt

currentPoints = 0
pointsTable = []


def finishRun():
    test.finishedTest = True
    if currentPoints > -80000:
        # print(currentPoints)
        pointsTable.append(currentPoints)
    test.currentPoints = 0
    
    
def avg(table):
    return sum(table)/len(table)
    
    
def graphScores():
    smoothness = 100
    smoothPointsTable = []
    print(pointsTable)
    for i in range(smoothness, len(pointsTable[smoothness:])):
        smoothPointsTable.append(avg(pointsTable[i-smoothness:i]))
    plt.plot(smoothPointsTable)
    plt.show()
    
    
def getBestRun():
    if len(pointsTable) > 0:
        return max(pointsTable)
    else:
        return None
    
    
def addPoints(value):
    test.currentPoints += value
    