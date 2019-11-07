from thing import thing
import juego
from bomba import bomba


class Thorman(thing):
    def __init__(self, name, pos=[50, 50]):
        self.posicion = pos
        self.name = name
        self.stepSize = 4
        self.direction = '275'
        self.hitbox = [128, 128] #widht, height
        self.hp = 1
        self.damage = 0
        self.BmDisp = 1

    def mover(self, direction):
        for index, item in enumerate(self.posicion):
            self.posicion[index] = item + self.stepSize*direction[index]

    def getStepsize(self):
        return self.stepSize

    def setStepsize(self, NewStep):
        self.stepSize = NewStep
    
    # def plantar(self):
    #     pos = self.posicion
    #     labomba = bomba(pos)
    #     print("Bomb has been planted")
    #     return labomba

    def getBmDisp(self):
        return self.BmDisp