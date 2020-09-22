from thing import thing
import pygame

class muro(thing):
    def imagenInicial(self):
        self.image = pygame.image.load('muro.png')
