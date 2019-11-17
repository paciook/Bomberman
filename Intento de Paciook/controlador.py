import vista
import juego
import pygame
import sys
from muro import muro
import time


CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}


class Controlador:
    def __init__(self):
        # El controlador inicializa el juego
        # y la vista.
        self.dimensiones = (1260, 700)
        self.juego = juego.Juego('Fran', self.dimensiones)
        self.vista = vista.Vista(self.dimensiones, self.juego)
        # self.sleep = 0.005

        # self.vista.loadSprites()
        self.vista.carga_imagen_fondo()
        # self.vista.cargar_imagen_bomberman([50, 50])
        # self.flipearAll()
        self.main_loop()

    def main_loop(self):
        # Se recorre constantemente una serie de controles

        contador = 0
        while True:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:  # Alguien apretó CERRAR
                    sys.exit()

                if event.type == pygame.KEYDOWN:  # Alguien presionó una tecla

                    if str(event.key) == '32':  # Espacio

                        self.juego.plantarBomba()

                    else:
                        if str(event.key) in CONTROLES:  # Direccionamiento
                            self.juego.moverThor(CONTROLES[str(event.key)])

                        else:
                            print(str(event.key))

            # if len(self.juego.getBombas()) != 0:  # Hay bombas?
            #     contador += 1
            #     print(self.juego.getBombas()[0].getPosicion())

            # if contador == 200:  # Hora de explotar
            #     contador += 1
            #     self.juego.explotarBomba()

            # if contador == 300:  # Llegaron los bomberos
            #     contador = 0
            #     self.juego.apagarExplosion()

            # if len(self.juego.getExplosiones()) != 0:  # No pasa nada
            #     contador += 1
            # print(contador)
            self.vista.carga_imagen_fondo()
            self.vista.dibujarObjetos()
            self.juego.printearTiempo()
            # self.flipearAll()
            # time.sleep(self.sleep)

    # def flipearAll(self):  # Dibujamos la situacion actual
    #     self.vista.recargarFondo()
    #     self.vista.cargarBombas(self.juego.getBombas())
    #     self.vista.cargarExplosiones(self.juego.getExplosiones())
    #     self.vista.recargarThor()
    #     self.vista.cargarMuros(self.juego.getMuros())
    #     pygame.display.flip()

if __name__ == "__main__":
    controlador = Controlador()

# Dale Luna aprobanos lo empecé el 11/6 porque con el
# otro no ibamos a llegar a ningún lado
