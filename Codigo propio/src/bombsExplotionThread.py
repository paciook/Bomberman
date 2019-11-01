import threading
from pydispatch import dispatcher
import time
import sys


class bombAnimation(threading.Thread):
    def __init__(self, daemon):
        super().__init__(daemon=daemon)
        dispatcher.connect(receiver=self.addExplotion, signal='Start Changing Explotion Sprites', sender='Controler')
        self.explotions = []
        self.spritenum = None

    def run(self):
        while True:
            for index, i in enumerate(self.explotions)
                time.sleep(0.1)
                self.explotions[index] = self.explotions[index] + 1
                if self.explotions == 4:
                    self.explotions.pop(0)
                dispatcher.send(signal = "Change Explotion Sprite", sender = "bombsExplotionThread", sprite = (self.spritenum, index))
                
    def addExplotion(self,explotion):
        self.explotions.append(explotion)