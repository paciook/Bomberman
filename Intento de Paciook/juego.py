import controlador
import Thorman
from explosiones import explosion
from bomba import bomba
from muro import muro
import time
from celda import celda
import pygame
from pygame.locals import *
import threading
import concurrent.futures



class Juego(threading.Thread):
    def __init__(self, nombre_jugador, dimensiones):
        super().__init__(target= self.main_loop)
        self.mapArray = []
        self.nombre = nombre_jugador
        self.dimensiones = dimensiones
        self.iniciarArray()
        self.thorman = Thorman.Thorman(self.nombre)
        self.objetosActivos = [self.thorman]
        self.bombas = []
        self.serTrump()
        self.start()

    def main_loop(self):
        while True:
            if not len(self.bombas) == 0:
                self.checkBombs()
            else:
                print("cuando printeo algo funca mejor")
            # https://www.instagram.com/p/B4-sIB7nZVj/

    def moverThor(self, direccion):
        pos = list(self.thorman.getPosicion())
        self.thorman.mover(direccion)
        celThor = self.equivalenteCelda(list(self.thorman.posicion))
        celThor.reaccionar(self.thorman)

    def iniciarArray(self):
        aux = []
        respuesta = []
        for x in range(0, self.dimensiones[0], 70):
            aux = []
            for y in range(0, self.dimensiones[1], 70):
                aux.append(celda())
            respuesta.append(aux)
        self.mapArray = respuesta

    def plantarBomba(self):
        if len(self.bombas) == 0:
            pos = list(self.thorman.getPosicion())
            cel = self.equivalenteCelda(pos)
            laBomba = bomba(pos)
            self.bombas.append(laBomba)
            self.objetosActivos.append(cel.setContenido(laBomba))

    def serTrump(self):  # Era necesario poner este nombre de funcion, perdon =(

        """Esta función coloca todas las celdas correspondientes de 70x70 que pueda
        según la dimensión del juego."""

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

    def equivalenteCelda(self, posicion):
        """Recibe una posicion basada en pixeles y devuelve la celda que allí se encuentra"""

        pos = [int((posicion[0] + 35) / 70), int((posicion[1] + 35) / 70)]
        celda = self.getCelda(pos)
        pos = [pos[0] * 70 + 1, pos[1] * 70 + 1]
        return celda

    def getCelda(self, posicion):
        return self.mapArray[posicion[0]][posicion[1]]

    def getObjetos(self):
        return self.objetosActivos

    def matarObjeto(self, objeto):
        self.objetosActivos.remove(objet)

    def checkBombs(self):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            resultados = [executor.submit(bomba.explotar) for bomba in self.bombas]

            for f in concurrent.futures.as_completed(resultados):
                f.result()
                self.objetosActivos.remove(self.bombas[0])
                self.bombas.pop(0)