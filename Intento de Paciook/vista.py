import pygame
from pygame.locals import *
from Thorman import Thorman

# La vista conoce al modelo, pero el modelo no a la vista.
# Vista sólo puede "consultar" al modelo, no debe hacer que ejecute acciones.


class Vista():

    def __init__(self, dimensiones, juego):
        """Esto debería ser implementado como un Singleton.
        Por ahora, ignoramos eso."""
        pygame.init()  # Inicializo.
        self.juego = juego
        self.dimensiones = dimensiones
        self.fondo = pygame.image.load("Wallpaper.jpg")
        self.screen = pygame.display.set_mode(dimensiones)
        self.thorman = None
        self.bomba = None
        self.muro = None
        self.explosion = None

        pygame.key.set_repeat(20)  # Procesar teclas mantenidas

    def carga_imagen_fondo(self):
        self.screen.blit(self.fondo, [0, 0])

    # def recargarFondo(self):
    #     self.screen.blit(self.fondo, [0, 0])

    # def cargar_imagen_bomberman(self, pos):
    #     self.pos_bomberman = pos
    #     self.screen.blit(self.thorman, pos)

    # def recargarThor(self):
    #     self.screen.blit(self.thorman, self.juego.getThorPosicion())

    # def loadSprites(self):
    #     self.fondo = pygame.image.load('Wallpaper.jpg')
    #     self.thorman = pygame.image.load('bmsprite.png')
    #     self.bomba = pygame.image.load('Mjolnir.png')
    #     self.muro = pygame.image.load('muro.png')
    #     self.explosion = pygame.image.load('explosion.png')

    # def cargarBombas(self, listaBombas):

    #     for bomba in listaBombas:
    #         self.mostrarBomba(bomba.getPosicion())

    def dibujarObjetos(self):
        for objeto in self.juego.getObjetos():
            self.screen.blit(objeto.getImage(), objeto.getPosicion())
        pygame.display.flip()

    # def mostrarBomba(self, posicion):
    #     self.screen.blit(self.bomba, posicion)
    #     # print(posicion)

    # def cargarExplosiones(self, listaExplosiones):

    #     for explosion in listaExplosiones:
    #         self.mostrarExplosion(explosion.getPosicion())

    # def mostrarExplosion(self, posicion):
    #     self.screen.blit(self.explosion, posicion)
    #     # print(posicion)

    # def cargarMuros(self, muros):
    #     for muro in muros:
    #         self.screen.blit(self.muro, muro.getPosicion())
    

