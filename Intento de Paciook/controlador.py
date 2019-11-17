import vista
import juego
import pygame
import sys
from muro import muro
import threading


CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}


class Controlador:
    def __init__(self):
        self.dimensiones = (1260, 700)

        self.juego = juego.Juego('Fran', self.dimensiones)      # El controlador incializa
        self.vista = vista.Vista(self.dimensiones, self.juego)  # la vista y el modelo.

        self.main_loop()

    def main_loop(self):
        # Se recorre constantemente una serie de controles
        while True:
            for event in pygame.event.get(): # Recorro cola de eventos

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

if __name__ == "__main__":
    controlador = Controlador()

# Dale Luna aprobame lo empecé el 11/6 porque con el
# otro no ibamos a llegar a ningún lado
