from thing import thing
import pygame


class explosion(thing):
    def imagenInicial(self):
        self.image = pygame.image.load('explosion.png')

    def getDaño (self):
        return self.daño
