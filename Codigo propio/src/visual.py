import pygame
from thormanSpritesThread import thormanSpritesThread
from PIL import Image
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
        self.thormanDirection = None
        self.thormanSpritesThread = thormanSpritesThread()
        self.fixedWall = pygame.image.load("../assets/Walls.png")
        fixedWallSize = Image.open("../assets/Walls.png")
        self.fixedWallSize = fixedWallSize.size
        self.spriteNumber = 0
        self.explotion = pygame.image.load("../assets/grasstexture.jpg")
        self.bombsThreadVisual = None
        dispatcher.connect(receiver = self.changeThormanSprite, signal = 'Change thorman sprite', sender = 'thormanSpritesThread' )
        dispatcher.connect(receiver = self.changeExplotionSprite, signal = 'Change Explotion Sprite', sender = 'bombsExplotionThread' )
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

    def changeThormanSprite(self, direction):
        self.thormanDirection = DIRECTIONS[direction]
        self.spriteNumber = self.spriteNumber + 1
        if self.spriteNumber == 4:
            self.spriteNumber = 1
        self.thorman = pygame.image.load("../assets/Thorman/Thorman" + str(self.thormanDirection) + str(self.spriteNumber) + ".png")
        self.screen.blit(self.thorman, self.game.getThormanPosition())

    def loadLimit(self, dimension):
        wallQuantity = 20
        wallWidth = int(dimension[0]/wallQuantity)
        self.fixedWall = pygame.transform.scale(self.fixedWall, (wallWidth, wallWidth))
        for ancho in range(wallQuantity):
            self.screen.blit(self.fixedWall, [ancho * wallWidth, 0])
            self.screen.blit(self.fixedWall, [ancho * wallWidth, dimension[1] - 40])

        for alto in range((wallWidth) - 1):
            self.screen.blit(self.fixedWall, [0, alto * wallWidth])
            self.screen.blit(self.fixedWall, [dimension[0] - wallWidth, alto * wallWidth])        
    # def reloadThorman(self):
    # self.screen.blit(self.thorman, self.game.getThormanPosition())

    def drawExplotionThread(self):
        self.screen.blit(self.explotion, self.game.getThormanPosition())

    def reloadBombs(self):
        self.bomb = pygame.image.load('../assets/Mjolnir.png')
        if len(self.game.getBombs()) != 0:
            for eachBomb in self.game.getBombs():
                xd = self.game.getBombs()
                self.screen.blit(self.bomb, eachBomb.getPosition())
                once = True
        else:
            if once is True:
                self.screen.blit(self.explotion, self.game.getThormanPosition())
                self.screen.blit(self.background, [0, 0])
                once = False

    def changeExplotionSprite(self):
        for i in range(len(self.game.getAvailableBombs)):
            pass
