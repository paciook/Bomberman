import controlador
import intentodepacio
from explosiones import explosion
from bomba import bomba
from muro import muro
import time


class Juego():
    def __init__(self, nombre_jugador, dimensiones):
        self.nombre = nombre_jugador
        self.dimensiones = dimensiones
        self.thorman = intentodepacio.Thorman(self.nombre)
        self.objetosActivos = [self.thorman]
        self.bombasActivas = []
        self.muros = []
        self.explosionesActivas = []

    def moverThor(self, direccion):
        self.thorman.mover(direccion)

    def getThorPosicion(self):
        return self.thorman.getPosicion()

    def plantarBomba(self):
        if self.thorman.getBmDisp() > len(self.bombasActivas):
            # self.bombasActivas.append(self.thorman.plantar())  
            self.bombasActivas.append(bomba(list(self.getThorPosicion())))
            print("Añadido a lista")

    def getBombas(self):
        return self.bombasActivas

    def explotarBomba(self):
        self.explosionesActivas.append(explosion(list(self.bombasActivas[0].getPosicion())))
        self.bombasActivas.pop(0)


    def getMuros(self):
        return self.muros

    def serTrump(self):
        for x in range(50, 1200, 200):
            for y in range(50, 720, 200):
                self.muros.append(muro([x,y]))

    def getExplosiones(self):
        return self.explosionesActivas

    def BOCAYOTEAMO(self):
        self.explosionesActivas.pop(0)