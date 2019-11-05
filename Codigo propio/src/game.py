from controler import *
from thorman import Thorman
from lightning import Lightning
import time

class Game():
    def __init__(self, playerName, dimentions):
        self.name = playerName
        self.dimentions = dimentions
        self.thorman = None
        self.activeBombList = []
        self.availableBombs = 5
        self.explodingBombsList = []


    # --------- THORMAN -----------

    def createThorman(self):
        self.thorman = Thorman(self.name)
        return self.thorman

    def getThormanDirection(self):
        return self.thorman.getDirection()

    def setThormanDirection(self, direction):
        self.thorman.setDirection(direction)

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


    # -------------------------------------


    # --------- MJOLNIR (BOMBS) -----------

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



 # --------- LIGHNINGS (EXPLOTIONS) -----------
    def addExplodingBombs(self):
        lightning = self.thorman.createLightning(self.activeBombList[0].getPosition())
        self.explodingBombsList.append(lightning)

    def getExplodingBomb(self):
        return self.explodingBombsList

    def delExplodingBomb(self, explotionNumber):
        self.explodingBombsList.pop(0)

    def setExplotionSprite(self, explotionNumber):
        self.explodingBombsList[explotionNumber - 1].setSpriteNumber()
