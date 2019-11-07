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
        self.availableBombs = 5 # The number of bombs Thorman can plant
        self.explodingBombsList = []
        self.enemyList=[]

    # --------- THORMAN -----------
    def createThorman(self):
        self.thorman = Thorman(self.name)
        return self.thorman

    def getThormanDirection(self):
        return self.thorman.getDirection()

    def setThormanDirection(self, direction):
        self.thorman.setDirection(direction)

    def moveThorman(self, direction):
        self.thorman.move(direction)

    def getThormanPosition(self):
        return self.thorman.getPosition()

    # --------- MJOLNIR (BOMBS) -----------
    def plantBomb(self):
        """Creates an object 'bomb' and appends it to a list"""
        theBomb = self.thorman.plantBomb()
        self.activeBombList.append(theBomb)
        self.availableBombs -= 1
        return theBomb

    def getBombs(self):
        return self.activeBombList

    def removeBombs(self):
        """Removes the first bombs of the list"""
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
        self.explodingBombsList[explotionNumber].setSpriteNumber() # Every lightning has an attribute self.spriteNumber that indicates the sprite that must be showed by visual

 # --------- HULKS (ENEMIES) -----------
    def addEnemy(self):
        enemy = self.thorman.createEnemy([100, 100])
        self.enemyList.append(enemy)
