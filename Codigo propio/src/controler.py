from visual import Visual
import thormanSpritesThread
import bombsThreadLogic
import time
import game
import pygame
import Collisions as colls
import threading
from pydispatch import dispatcher

#import Calculate Collisions as colls
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
        dispatcher.connect(receiver = self.explodeBomb, signal='Exploded', sender = 'bombsThread')

    def mainLoop(self):
        while True:
            # self.mapArray = colls.arrayOf(border)
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
                        print("xd")
            self.visual.reloadBombs()

            for potencialColl in colls.closeness(self.activeObjects):
                colls.compare(potencialColl)

            # for item in self.activeObjects:
            #     colls.placeObject(item)
            # colls.verifyColls()


            # self.visual.drawBombs('../assets/bmsprite.png')
            pygame.display.flip()

    def loadImages(self):
        self.visual.loadBackgroundImage('../assets/Wallpaper.jpg')
        self.visual.loadThormanImage('../assets/Thorman/ThormanRight1.png',
                                     (2, 2))
        self.visual.loadLimit(self.dimentions)
        return None

    def reloadBombsThread(self):
        self.bombsThread = bombsThreadLogic.bombTimeCounter(self.game.getBombs())
        BombsThread = threading.Thread(target=self.bombsThread.reloadBombs(), args=(None,), daemon=True)
        BombsThread.start()

    def explodeBomb(self, bomb):
        self.game.removeBombs(bomb)

    # def addCollision(coll):
    #     self.collisions.append(coll)

    def getMapArray(self):
        return self.mapArray

    def setMapArray(self, mapArray):
        self.mapArray = mapArray


if __name__ == "__main__":
    controler = Controler()
