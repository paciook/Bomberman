import pygame
from thormanSpritesThread import thormanSpritesThread
from PIL import Image
from pygame.locals import *
import thorman
import threading
import time
from pydispatch import dispatcher
DIRECTIONS = {'273': "Back", '274': "Front", '275': "Right", '276': "Left", 'Standing Still': 'Still'}


class Visual():
    def __init__(self, dimentions, game):
        pygame.init()
        self.game = game
        self.dimentions = dimentions
        self.background = None
        self.screen = pygame.display.set_mode(dimentions)
        self.reloadEverythingExecuting = False
        self.reloadEverythingTimes = 0
        self.ls = None 
        self.thorman = pygame.image.load("../assets/Thorman/ThormanRight1.png")
        self.thormanSprites = {}
        self.thormanDirection = None
        self.thormanSpritesThread = thormanSpritesThread()
        self.fixedWall = pygame.image.load("../assets/Wallpaper.png")
        fixedWallSize = Image.open("../assets/Walls.png")
        self.bomb = pygame.image.load('../assets/Mjolnir.png')
        self.fixedWallSize = fixedWallSize.size
        self.spriteNumber = 0
        self.bombsThreadVisual = None
        self.lightning = None
        dispatcher.connect(receiver = self.changeThormanSprite, signal = 'Change thorman sprite', sender = 'thormanSpritesThread' )
        pygame.key.set_repeat(5)
        # para que procese eventos cuando se mantiene una tecla apretada

    def loadImages(self):
        self.background = pygame.image.load('../assets/Wallpaper.jpg')
        self.screen.blit(self.background, [0, 0])
        self.ls = []
        for i in range(3):
            self.thorman = pygame.image.load('../assets/Thorman/ThormanBack'+ str(i+1)+'.png')
            self.ls.append(self.thorman)
        self.thormanSprites['Back'] = self.ls
        self.ls.clear()
        for i in range(3):
            self.thorman = pygame.image.load('../assets/Thorman/ThormanFront'+ str(i+1)+'.png')
            self.ls.append(self.thorman)
        self.thormanSprites['Front'] = self.ls
        self.ls.clear()
        for i in range(3):
            self.thorman = pygame.image.load('../assets/Thorman/ThormanRight'+ str(i+1)+'.png')
            self.ls.append(self.thorman)
        self.thormanSprites['Right'] = self.ls
        print(len(self.thormanSprites['Right']))
        self.screen.blit(self.thorman, [2, 2])
        self.ls.clear()
        for i in range(3):
            self.thorman = pygame.image.load('../assets/Thorman/ThormanLeft'+ str(i+1) +'.png')
            self.ls.append(self.thorman)
        self.thormanSprites['Left'] = self.ls
        self.ls.clear()
        print(len(self.thormanSprites['Right']))
        for i in range(2):
            self.thorman = pygame.image.load('../assets/Thorman/ThormanStill'+ str(i+1) +'.png')
            self.ls.append(self.thorman)
        self.thormanSprites['Still'] = self.ls
        print(len(self.thormanSprites['Right']))

    def reloadBackground(self):
        self.screen.blit(self.background, [0, 0])

    def loadThormanImage(self, sprite, pos):
        self.thorman = pygame.image.load(sprite)
        self.screen.blit(self.thorman, pos)

    def changeThormanSprite(self):
        self.thormanDirection = DIRECTIONS[self.game.getThormanDirection()]
        self.spriteNumber = self.spriteNumber + 1
        if self.thormanDirection == 'Still':
            if self.spriteNumber > 2:
                self.spriteNumber = 1
            self.screen.blit(self.thormanSprites[self.thormanDirection][self.spriteNumber-1], self.game.getThormanPosition())
        else:
            if self.spriteNumber == 4:
                self.spriteNumber = 1
            print(len(self.thormanSprites['Right']))
            self.screen.blit(self.thormanSprites[self.thormanDirection][self.spriteNumber-1], self.game.getThormanPosition())


    def loadLimit(self):
        self.screen.blit(self.fixedWall, [0, 0])
        # wallQuantity = 20
        # wallWidth = int(self.dimentions[0]/wallQuantity)
        # self.fixedWall = pygame.transform.scale(self.fixedWall, (wallWidth, wallWidth))
        # for ancho in range(wallQuantity):
        #     self.screen.blit(self.fixedWall, [ancho * wallWidth, 0])
        #     self.screen.blit(self.fixedWall, [ancho * wallWidth, self.dimentions[1] - 40])

        # for alto in range((wallWidth) - 1):
        #     self.screen.blit(self.fixedWall, [0, alto * wallWidth])
        #     self.screen.blit(self.fixedWall, [self.dimentions[0] - wallWidth, alto * wallWidth])        

    def reloadBombs(self):
        if len(self.game.getBombs()) != 0:
            for eachBomb in self.game.getBombs():
                self.screen.blit(self.bomb, eachBomb.getPosition())
        else:
            pass

    def reloadExplotionSprite(self):
        if len(self.game.getExplodingBomb()) != 0:
            for eachLightning in self.game.getExplodingBomb():
                self.lightning = pygame.image.load("../assets/Lightning/Lightning" + str(eachLightning.getSpriteNumber()) + ".png")
                self.screen.blit(self.lightning, eachLightning.getPosition())

    def reloadEverything(self):        
            self.reloadEverythingTimes += 1
            if self.reloadEverythingExecuting is False:
                while self.reloadEverythingTimes >= 1:
                    self.reloadEverythingExecuting = True
                    self.reloadBackground()
                    self.reloadBombs()
                    self.changeThormanSprite()
                    self.reloadExplotionSprite()
                    self.loadLimit()
                    dispatcher.send(signal = 'Finished')
                    if self.reloadEverythingTimes > 0:
                        self.reloadEverythingTimes -= 1
                    self.reloadEverythingExecuting = False
                # pygame.display.flip()
            else:
                pass
