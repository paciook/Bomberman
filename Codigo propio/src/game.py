from controler import *
from thorman import Thorman


class Game():
    def __init__(self, playerName, dimentions):
        self.name = playerName
        self.dimentions = dimentions
        self.thorman = Thorman(self.name)
        self.activeBombList = []
        self.availableBombs = 1

    def positionIsValid(self, direction):
        newPos = self.thorman.getNewTentativePosition(direction)
        print('newPos', newPos)
        comparison = [val < self.dimentions[i] for i, val in enumerate(newPos)]
        print(comparison[0], comparison[1], newPos[0] > 0, newPos[1] > 0)
        return comparison[0]*comparison[1]*(newPos[0] >= 0)*(newPos[1] >= 0)

    def moveThorman(self, direction):
        self.thorman.move(direction)

    def getThormanPosition(self):
        return self.thorman.getPosition()

    def plantBomb(self):
        self.activeBombList.append(self.thorman.plantBomb())

    def getBombs(self):
        return self.activeBombList

    def removeBombs(self):
        self.activeBombList.pop()
        self.availableBombs += 1

    def getAvailableBombs(self):
        return self.availableBombs
