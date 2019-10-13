import pygame
from pygame.locals import *
import thorman
import threading
import time
from pydispatch import dispatcher
DIRECTIONS = {'273': "Back", '274': "Front", '275': "Right", '276': "Left"}



class Visual():
    def __init__(self, dimentions, game):
        pygame.init()
        self.game = game
        self.dimentions = dimentions
        self.background = None
        self.screen = pygame.display.set_mode(dimentions)
        self.thorman = None
        self.spriteNumber = 0
        dispatcher.connect(self.finallyChangeSprite, signal="Change Sprite", sender="changeThormanSprite")


        pygame.key.set_repeat(20)
        # para que procese eventos cuando se mantiene una tecla apretada

    def loadBackgroundImage(self, backgroundDirection):
        self.background = pygame.image.load(backgroundDirection)
        self.screen.blit(self.background, [0, 0])

    def reloadBackground(self):
        self.screen.blit(self.background, [0, 0])

    def loadThormanImage(self, sprite, pos):
        self.thorman = pygame.image.load(sprite)
        self.screen.blit(self.thorman, pos)
    
    def loadBomb(self, sprite, pos):
        self.bomba = pygame.image.load('../assets/sprite.png')

    def changeThormanSprite(self, direction):
        self.spriteNumber = self.spriteNumber + 1
        if self.spriteNumber == 4: self.spriteNumber = 1
        self.thorman = pygame.image.load("../assets/Thorman/Thorman" + str(DIRECTIONS[direction]) + str(self.spriteNumber) + ".png")
        time.sleep(0.08)
        dispatcher.send(signal="Change Sprite", sender="changeThormanSprite")

    def finallyChangeSprite(self):
        self.screen.blit(self.thorman, self.game.getThormanPosition())

    def reloadThorman(self, direction):
        changeThormanSpriteThread = threading.Thread(target=self.changeThormanSprite(direction), args=(direction), daemon=True)
        changeThormanSpriteThread.start()

    # def reloadThorman(self):
    # self.screen.blit(self.thorman, self.game.getThormanPosition())

    # def drawBombs(self, sprite):
    #     self.bomb = pygame.image.load(sprite)
    #     for eachBomb in self.game.getBombs():
    #         self.screen.blit(self.bomb, eachBomb.getPosition())
