from visual import Visual
import thormanSpritesThread
import bombsThread
import time
import game
import pygame
import threading
from pydispatch import dispatcher
import Calculate Collisions as colls
CONTROLS = {'273': [0, -1], '274': [0, 1], '275': [1, 0],
            '276': [-1, 0], '32': [0, 0]}


class Controler():
    def __init__(self):
        self.dimentions = (1200, 600)  # (640, 480)
        self.game = game.Game('Fran', self.dimentions)
        self.visual = Visual(self.dimentions, self.game)
        self.bombsThread = None
        self.loadImages()
        self.mapArray = []
        self.collisions = []
        self.activeObjects = []
        self.mainLoop()
        dispatcher.connect(receiver = reloadBombs, signal='Decrease bomb time', sender = 'Controler')

    def explodeBomb(self, bomb):
        self.explotarviolento()
        self.activeBombList.pop(bomb)

    def reloadBombs(self, bomb):
        bombsList = self.game.getBombs()
        for eachBomb in bombsList:
            if eachBomb.getTime() >= 3:
                self.visual.explodeBomb[bomb]
                self.game.removeBombs()
            else:
                eachBomb.setTime(1)
            

    def mainLoop(self):
        while True:
            self.mapArray = colls.arrayOf(border)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # self.game.mover_bm(event.tevent_name())
                if event.type == pygame.KEYDOWN:  # alguien presionó una tecla
                    # print(pygame.event.event_name(event.type))
                    # print(event.key)

                        if str(event.key) == '32':
                            if self.game.getAvailableBombs != 0:
                                self.game.plantBomb()
                                self.reloadBombsThread()

                        else:
                            self.game.moveThorman(CONTROLS[str(event.key)])
                            self.visual.reloadBackground()
                            self.visual.loadLimit(self.dimentions)
                            self.visual.reloadThormanThread(str(event.key))
            
            for item in self.activeObjects:
                colls.placeObject(item)
            colls.verifyColls()


            # self.visual.drawBombs('../assets/bmsprite.png')
            pygame.display.flip()

    def loadImages(self):
        self.visual.loadBackgroundImage('../assets/Wallpaper.jpg')
        self.visual.loadThormanImage('../assets/Thorman/ThormanRight1.png',
                                     (2, 2))
        self.visual.loadLimit(self.dimentions)
        return None

    def reloadBombsThread(self):
        self.bombsThread = bombsThread.bombTimeCounter(self.game.getBombs())
        BombsThread = threading.Thread(target=self.bombsThread.reloadBombs(), daemon=True)
        BombsThread.start()

    def addCollision(coll):
        self.collisions.append(coll)

    def getMapArray(self):
        return self.mapArray

    def setMapArray(self, mapArray):
        self.mapArray = mapArray


if __name__ == "__main__":
    controler = Controler()
