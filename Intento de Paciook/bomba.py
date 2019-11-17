from thing import thing
import pygame
import time

class bomba(thing):
    def imagenInicial(self):
        self.image = pygame.image.load('Mjolnir.png')

    def reaccionar(self, objecto):
        pass

    def explotar(self):
        time.sleep(4)
        print("boom")