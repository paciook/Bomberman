from visual import Visual
import game
import pygame
from pydispatch import dispatcher
CONTROLS = {'273': [0, -1], '274': [0, 1], '275': [1, 0],
            '276': [-1, 0], '32': [0, 0]}


class Controler():
    def __init__(self):
        self.dimentions = (1200, 600)  # (640, 480)
        self.game = game.Game('Fede', self.dimentions)
        self.visual = Visual(self.dimentions, self.game)
        self.loadImages()
        self.mainLoop()

    def mainLoop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # self.game.mover_bm(event.tevent_name())
                if event.type == pygame.KEYDOWN:  # alguien presionó una tecla
                    # print(pygame.event.event_name(event.type))
                    # print(event.key)
                    try:
                        self.game.moveThorman(CONTROLS[str(event.key)])
                        # self.game.plantBomb(CONTROLS[str(event.key)])
                        self.visual.reloadBackground()
                        self.visual.loadLimit(self.dimentions)
                        self.visual.reloadThorman(str(event.key))
                    except Exception:
                        pass

            # self.visual.drawBombs('../assets/bmsprite.png')
            pygame.display.flip()

    def loadImages(self):
        self.visual.loadBackgroundImage('../assets/Wallpaper.jpg')
        self.visual.loadThormanImage('../assets/Thorman/ThormanRight1.png',
                                     (2, 2))
        self.visual.loadLimit(self.dimentions)
        return None


if __name__ == "__main__":
    controler = Controler()
