from thing import thing
from bomb import Bomb
from lightning import Lightning

class Thorman(thing):
    def __init__(self, name, pos=[0, 0]):
        self.position = pos
        self.name = name
        self.stepSize = 5
        self.direction = '275'
        self.hitbox = [128, 128] #widht, height
        self.hp = 1
        self.damage = 0
    
    def getDirection(self):
        return self.direction

    def setDirection(self, direction):
        self.direction = direction

    def createLightning(self, position):
        lightning = Lightning(position)
        return lightning

    def move(self, direction):
        for index, item in enumerate(self.position):
            self.position[index] = item + self.stepSize*direction[index]

    def getStepsize(self):
        return self.stepSize

    def setStepsize(self, NewStep):
        self.stepSize = NewStep

    def getNewTentativePosition(self, direction):
        print('direction', direction)
        auxList = []
        for index, item in enumerate(self.position):
            auxList.append(item+self.stepSize * direction[index])
        return auxList

    def plantBomb(self):
        theBomb = Bomb(self.position)
        return theBomb

    def getThormanPosition(self):
        return self.getPosition
    
    def getHitbox(self):
        return self.hitbox

    def getPosition(self):
        return self.position