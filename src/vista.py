import pygame
from pygame.locals import *
from Thorman import Thorman
import time
import threading
from metaclase import Singleton
# La vista conoce al modelo, pero el modelo no a la vista.
# Vista sólo puede "consultar" al modelo, no debe hacer que ejecute acciones.


class Vista(threading.Thread):

    def __init__(self, dimensiones, juego):
        """Esto debería ser implementado como un Singleton.
        Por ahora, ignoramos eso."""
        super().__init__(target=self.main_loop)
        pygame.init()  # Inicializo.
        self.juego = juego
        self.dimensiones = dimensiones
        self.fondo = pygame.image.load("Wallpaper.jpg")
        self.screen = pygame.display.set_mode(dimensiones)
        self.start()

        pygame.key.set_repeat(4)  # Procesar teclas mantenidas

    def main_loop(self):
        while True:  
            self.carga_imagen_fondo()   # Dibujamos la pantalla constantemente
            self.dibujarObjetos()

    def carga_imagen_fondo(self):
        self.screen.blit(self.fondo, [0, 0])

    def dibujarObjetos(self):
        for objeto in self.juego.getObjetos():
            self.screen.blit(objeto.getImage(), objeto.getPosicion())   # Preguntamos a juego sus
        pygame.display.flip()                                      # objetos y los dibujamos

    

