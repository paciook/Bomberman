import pygame
from pygame.locals import *
import thorman


class Visual():

    def __init__(self, dimentions, game):
        pygame.init()
        self.game = game
        self.dimentions = dimentions
        self.background = None
        self.screen = pygame.display.set_mode(dimentions)
        self.thorman = None
 #       self.bomba = pygame.image.load('../assets/sprite.png')

        pygame.key.set_repeat(20) # para que procese eventos cuando se mantiene una tecla apretada

    def loadBackgroundImage(self, backgroundDirection):
        self.background = pygame.image.load(backgroundDirection)
        self.screen.blit(self.background, [0, 0])

    def reloadBackground(self):
        self.screen.blit(self.background, [0, 0])

    def loadThormanImage(self, sprite, pos):
        self.thorman = pygame.image.load(sprite)
        self.posThorman = pos
        self.screen.blit(self.thorman, pos)

    def reloadThorman(self):
        self.screen.blit(self.thorman, self.game.getThormanPosition()) 
    
    def drawBombs(self, sprite):
        self.bomb = pygame.image.load(sprite)
        for eachBomb in self.game.getBombs():
            self.screen.blit(self.bomb, eachBomb.getPosition())