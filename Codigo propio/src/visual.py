import pygame
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
        self.spriteNumber = 0
        self.fixedWall = pygame.image.load("../assets/Wall hard.jpg")
        fixedWallSize = Image.open("../assets/Wall hard.jpg")
        self.fixedWallSize = fixedWallSize.size
        
        dispatcher.connect(receiver = self.drawExplotionThread, signal = 'Explode bomb', sender = 'Controler' )
        dispatcher.connect(receiver = self.reloadBomb, signal = 'Change bomb sprite', sender = 'Controler' )

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

    def reloadThorman(self, direction):
        self.spriteNumber = self.spriteNumber + 1
        if self.spriteNumber == 4:
            self.spriteNumber = 1
        self.thorman = pygame.image.load("../assets/Thorman/Thorman" + str(DIRECTIONS[direction]) + str(self.spriteNumber) + ".png")
        # time.sleep(0.004)
        self.screen.blit(self.thorman, self.game.getThormanPosition())

    def reloadThormanThread(self, direction):
        reloadThormanThread = threading.Thread(target=self.reloadThorman(direction), args=(direction), daemon=True)
        reloadThormanThread.start()

    def loadLimit(self, dimension):
        wallQuantity = 30
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
        pass
    
    def reloadBomb(self):
        self.bomb = pygame.image.load('../assets/Mjolnir.png')
        for eachBomb in self.game.getBombs():
            self.screen.blit(self.bomb, eachBomb.getPosition())

    def drawExplotion(self):
        pass