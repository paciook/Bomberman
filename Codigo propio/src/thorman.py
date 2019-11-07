from thing import thing
from bomb import Bomb
from lightning import Lightning
from enemy import Enemy
class Thorman(thing):
    def __init__(self, name, pos=[0, 0]):
        self.position = pos
        self.name = name
        self.stepSize = 5 # The distance it moves when the key is pressed
        self.direction = '275'
        self.hitbox = [128, 128] #widht, height
        self.hp = 1
        self.damage = 0

    # --------- THORMAN -----------
    def getDirection(self):
        return self.direction

    def setDirection(self, direction):
        self.direction = direction

    def move(self, direction):
        """Moves the Thorman"""
        for index, item in enumerate(self.position):
            self.position[index] = item + self.stepSize*direction[index]

    def getStepsize(self):
        return self.stepSize
    
    def getThormanPosition(self):
        return self.getPosition

    def getPosition(self):
        return self.position

    # --------- LIGHTNINGS(EXPLOTIONS) -----------
    def createLightning(self, position):
        lightning = Lightning(position)
        return lightning

    # --------- MJOLNIR(BOMBS) -----------
    def plantBomb(self):
        theBomb = Bomb(self.position)
        return theBomb

    # --------- HULK(ENEMY) -----------
    def createEnemy(self, position):
        enemy = Enemy(position)
        return enemy