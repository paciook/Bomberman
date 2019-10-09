from controler import *
from thorman import Thorman


class Game():
    def __init__(self, playerName, dimentions):
        self.name = playerName
        self.dimentions = dimentions
        self.thorman = Thorman(self.name)
        self.lista_de_bombas_activas = []

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

    def poner_bomba(self):
        self.lista_de_bombas_activas.append(thorman.poner_bomba())
    
    def get_bombas(self):
        return self.lista_de_bombas_activas