
from visual import Visual
import thormanSpritesThread
import bombsThread
import time
import game
import pygame
import bombsExplotionThread
# import Collisions as colls
import threading
from pydispatch import dispatcher

#import Calculate Collisions as colls
CONTROLS = {'273': [0, -1], '274': [0, 1], '275': [1, 0],
            '276': [-1, 0], '32': [0, 0]}


class Controler():
    def __init__(self):
        self.activeObjects = []
        self.dimentions = (1200, 600)  # (640, 480)
        self.game = game.Game('Fran y Manu', self.dimentions)
        self.activeObjects.append(self.game.createThorman())
        self.visual = Visual(self.dimentions, self.game)
        self.loadImages()
        self.mapArray = []
        self.collisions = []
        self.activeObjects = []
        self.bombsTimeThread = bombsThread.bombTimeCounter(daemon=True)
        self.bombsThreadRun = threading.Thread(target=self.bombsTimeThread.run) 
        self.bombsThreadRun.start()
        # self.bombsExplotionThread = 
        self.mainLoop()
        self.bombs = None
        dispatcher.connect(receiver=self.explodeBomb, signal='Exploded', sender='bombsThread')

    def mainLoop(self):
        while True:
            # self.mapArray = colls.arrayOf(border)
            dispatcher.connect(receiver=self.explodeBomb, signal='Exploded', sender='bombsThread')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                # self.game.mover_bm(event.tevent_name())
                if event.type == pygame.KEYDOWN:  # alguien presionó una tecla
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_RIGHT]:
                        self.game.moveThorman(CONTROLS['275'])
                    if keys[pygame.K_LEFT]:
                        self.game.moveThorman(CONTROLS['276'])
                    if keys[pygame.K_UP]:
                        self.game.moveThorman(CONTROLS['273'])
                    if keys[pygame.K_DOWN]:
                        self.game.moveThorman(CONTROLS['274'])
                    if keys[pygame.K_SPACE]:
                        if self.game.getAvailableBombs() != 0:
                            self.activeObjects.append(self.game.plantBomb())
                            self.reloadBombsThread()

                    self.visual.reloadBackground()
                    self.visual.loadLimit(self.dimentions)
                    try:
                        self.visual.changeThormanSprite(str(event.key))
                    except Exception:
                        pass
                    print(threading.active_count())
            self.visual.reloadBombs()

            # for potencialColl in colls.closeness(self.activeObjects):
            #     colls.compare(potencialColl)

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
        # acá estamos creando una bocha de threads

        # yo haría una lista de thread
        dispatcher.send(signal='Add Bomb', sender='Controler')

    def explodeBomb(self):
        # self.game.addExplodingBombs()
        self.game.removeBombs()
        # dispatcher.send(signal='Start Changing Explotion Sprites', sender='Controler')    
    # def addCollision(coll):
    #     self.collisions.append(coll)

    def getMapArray(self):
        return self.mapArray

    def setMapArray(self, mapArray):
        self.mapArray = mapArray

    def appendActiveObject(self, newFriend):
        self.activeObjects.append(newFriend)

if __name__ == "__main__":
    controler = Controler()
