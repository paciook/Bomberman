import controlador
import Thorman
from explosiones import explosion
from bomba import bomba
from muro import muro
import time
from celda import celda
import pygame
from pygame.locals import *



class Juego():
    def __init__(self, nombre_jugador, dimensiones):
        self.mapArray = []
        self.nombre = nombre_jugador
        self.dimensiones = dimensiones
        self.iniciarArray()
        self.thorman = Thorman.Thorman(self.nombre)
        
        self.objetosActivos = [self.thorman]
        self.bombasActivas = []
        self.muros = []
        self.serTrump()
        self.explosionesActivas = []

        self.clock = pygame.time.Clock()
        self.tiempoTrans = 0

    def moverThor(self, direccion):
        pos = list(self.thorman.getPosicion())
        self.thorman.mover(direccion)
        if self.puedoPonerEn(self.thorman.getPosicion()) is False:
            self.thorman.setPosicion(pos)

    def iniciarArray(self):
        aux = []
        respuesta = []
        for x in range(0, self.dimensiones[0], 70):
            aux = []
            for y in range(0, self.dimensiones[1], 70):
                aux.append(celda())
            respuesta.append(aux)
        self.setMapArray(respuesta)

    def getThorPosicion(self):
        return self.thorman.getPosicion()

    def plantarBomba(self):
        if self.thorman.getBmDisp() > len(self.bombasActivas):
            # self.bombasActivas.append(self.thorman.plantar())
            # self.bombasActivas.append(bomba(list(self.getThorPosicion())))
            print("Añadido a lista")

            pos = list(self.thorman.getPosicion())
            cel = self.equivalenteCelda(pos)

            self.objetosActivos.append(cel[0].setContenido(bomba(cel[1])))
            self.clock.tick()
            


    def explotarBomba(self):
        # pos = list(self.bombasActivas[0].getPosicion())
        # cel = self.equivalenteCelda(pos)
# ACA HAY QUE METER MANO
        # self.objetosActivos.append(cel[0].setContenido(explosion(cel[1])))

        # self.explosionesActivas.append(explosion(list(self.bombasActivas[0].getPosicion())))
        # self.bombasActivas.pop(0)
        pass

    # def getMuros(self):
    #     return self.muros

    def serTrump(self):
        aux = self.mapArray
        for x in range(len(aux)):
            for y in range(len(aux[x])):
                if x == 0 or y == 0:

                    aux[x][y].setContenido(muro([x * 70, y * 70]))
                    self.objetosActivos.append(aux[x][y].getContenido())
                elif x > 1 and y > 1 and x % 2 == 0 and y % 2 == 0:

                    aux[x][y].setContenido(muro([x * 70, y * 70]))
                    self.objetosActivos.append(aux[x][y].getContenido())
                elif x == self.dimensiones[0]/70 - 1 or \
                        y == self.dimensiones[1]/70 - 1:

                    aux[x][y].setContenido(muro([x * 70, y * 70]))
                    self.objetosActivos.append(aux[x][y].getContenido())

        self.mapArray = aux

    # def getExplosiones(self):
    #     return self.explosionesActivas

    def apagarExplosion(self):
        # pos = list(self.explosionesActivas[0].getPosicion())
        # celdaActual = self.equivalenteCelda(pos)

        # celdaActual[0].setContenido = None

        # self.explosionesActivas.pop(0)
        pass

    def getMapArray(self):
        return self.mapArray

    def setMapArray(self, mapArray):
        self.mapArray = mapArray

    # def appendMuro(self, muro):
    #     self.objetosActivos.append(muro)

    def equivalenteCelda(self, posicion):

        pos = [int((posicion[0] + 35) / 70), int((posicion[1] + 35) / 70)]
        celda = self.getCelda(pos)
        pos = [pos[0] * 70 + 1, pos[1] * 70 + 1]
        respuesta = [celda, pos]

        return respuesta

    def getCelda(self, posicion):
        return self.mapArray[posicion[0]][posicion[1]]

    def puedoPonerEn(self, posicion):
        # return True
        if self.equivalenteCelda(posicion)[0].getContenido() is None:
            return True
        else:
            return False

    def getObjetos(self):
        return self.objetosActivos

    def printearTiempo(self):
        self.clock.tick()
        self.tiempoTrans += self.clock.get_time()
        print(self.tiempoTrans)