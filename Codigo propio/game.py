import controler
import thorman


class Game():
    def __init__(self, playerName, dimentions):
        self.name = playerName
        self.dimentions = dimentions
        self.thorman = thorman.thorman(self.nombre)

    def positionIsValid(self, direction):
        newPosition = self.thorman.get_nueva_posicion_tentativa(direccion)
        print('newPos', newPos)
        comparison = [val < self.dimensiones[i] for i, val in enumerate(newPos)]
        print(comparison[0], comparison[1], newPos[0] > 0, newPos[1] > 0)
        return comparison[0]*comparison[1]*(newPos[0] >= 0)*(newPos[1] >= 0)

    def moveThorman(self, direccion):
        self.bomberman.mover(direccion, self.es_posicion_valida(direccion))

    def getThormanPosition(self):
        return self.bomberman.get_posicion()
