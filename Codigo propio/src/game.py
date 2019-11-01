from controler import *
from thorman import Thorman


class Game():
    def __init__(self, playerName, dimentions):
        self.name = playerName
        self.dimentions = dimentions
        self.thorman = None
        self.activeBombList = []
        self.availableBombs = 5
        self.explodingBombsList = []

    def addExplodingBombs(self):
        self.explodingBombsList.append([self.activeBombList[0].getPosition, 0])        

    def getExplodingBombsList(self):
        pass

    def createThorman(self):
        self.thorman = Thorman(self.name)
        return self.thorman

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
        theBomb = self.thorman.plantBomb()
        self.activeBombList.append(theBomb)
        self.availableBombs -= 1
        return theBomb

    def getBombs(self):
        return self.activeBombList

    def removeBombs(self):
        self.activeBombList.pop(0)
        self.availableBombs += 1

    def getAvailableBombs(self):
        return self.availableBombs
        