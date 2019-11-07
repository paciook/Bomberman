from visual import Visual
import bombsThread
import time
import game
import pygame
import bombsExplotionThread
import Collisions as colls
import threading
from pydispatch import dispatcher
import thormanStandingThread


CONTROLS = {'273': [0, -1], '274': [0, 1], '275': [1, 0],
            '276': [-1, 0], 'Standing Still': [100, 100]}


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
        self.thormanMoving = True
        self.firstFlip = True

        # --------- THREADS -----------
        self.bombsTimeThread = bombsThread.bombTimeCounter(daemon=True)
        self.bombsThreadRun = threading.Thread(target=self.bombsTimeThread.run)
        self.bombsThreadRun.start()
        self.explotionNumber = 0
        self.bombsExplotionThreadList = []
        self.thormanStandingThreadRun = thormanStandingThread.standingStill(daemon=True)
        self.thormanStandingThreadRun.start()
        self.thormanStandingThreadStarted = False
        # -----------------------------
        dispatcher.connect(receiver=self.explodeBomb, signal='Exploded', sender='bombsThread')
        dispatcher.connect(receiver = self.reloadExplotionSprite, signal = 'Change Explotion Sprite', sender = 'bombsExplotionThread' )
        dispatcher.connect(receiver = self.delExplotionSprite, signal = "Delete Explotion", sender = 'bombsExplotionThread' )
        dispatcher.connect(receiver = self.reloadThorman, signal = "Stand Still", sender = 'thormanStandingThread' )
        dispatcher.connect(receiver=self.flip, signal = 'Finished')
        self.mainLoop()
        self.bombs = None

    def mainLoop(self):
        """Main loop that recognizes whenever an event (key pressed or not)
        in pygame is executed"""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit(0)
                if event.type == pygame.KEYDOWN:  # alguien presionó una tecla
                    if self.thormanMoving == False:
                        dispatcher.send(signal = "Moving", sender = 'Controler')
                        self.thormanMoving = True
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
                            # self.game.plantBomb()
                            self.activeObjects.append(self.game.plantBomb())
                            self.reloadBombsThread()
                    else:
                        self.game.setThormanDirection(str(event.key))
                    self.visual.reloadEverything()
                else:
                    self.game.setThormanDirection('Standing Still')
                    if self.thormanMoving == True:
                        dispatcher.send(signal = "Not Moving", sender = 'Controler')
                        self.thormanMoving = False
            if self.firstFlip == True: # Does the first visual flip
                pygame.display.flip()
                self.firstFlip = False

    # --------- LIGHTNINGS(EXPLOTIONS) -----------
    def reloadExplotionSprite(self, explotionNumber):
        """Send to game the order to change the sprite of the explotion"""
        self.visual.reloadEverything()
        if explotionNumber == 3:
            pass
        else:
            self.game.setExplotionSprite(explotionNumber)

    def delExplotionSprite(self, explotionNumber):
        """Once the explotion time is finished,
        deletes the lightning from the list"""
        self.explotionNumber -= 1
        self.game.delExplodingBomb(explotionNumber)
        self.visual.reloadEverything()

    # --------- MJOLNIR(BOMBS) -----------
    def reloadBombsThread(self):
        """Sends the message to the thread to count a new bomb"""
        dispatcher.send(signal='Add Bomb', sender='Controler')

    def explodeBomb(self):
        """Creates a new thread for the lightning every time a bombs finishes its time"""
        dispatcher.send(signal='Start Changing Explotion Sprites', sender='Controler')
        bombsExplotionThreadRun = bombsExplotionThread.bombAnimation(daemon=True, explotionNumber=self.explotionNumber)
        self.bombsExplotionThreadList.append(bombsExplotionThreadRun)
        bombsExplotionThreadRun.start()
        self.explotionNumber += 1
        self.game.addExplodingBombs()
        self.game.removeBombs()
        self.visual.reloadEverything()

    # --------- THORMAN(BOMBERMAN) -----------
    def reloadThorman(self):
        """Reloads the visual every time it is called"""
        self.visual.reloadEverything()

    # --------- OTHERS -----------
    def flip(self):
        """Flips every time it is called"""
        pygame.display.flip()

    def loadImages(self):
        """Loads the first background and Thor image"""
        self.visual.loadBackgroundImage('../assets/Wallpaper.jpg')
        self.visual.loadThormanImage('../assets/Thorman/ThormanRight1.png',
                                     (2, 2))
        self.visual.loadLimit()
        return None

    def appendActiveObject(self, newFriend):
        """"""
        self.activeObjects.append(newFriend)

if __name__ == "__main__":
    controler = Controler()
