import threading
from pydispatch import dispatcher
import time
import sys


class bombAnimation(threading.Thread):
    def __init__(self, daemon):
        super().__init__(daemon=daemon)
        dispatcher.connect(receiver=self.addExplotion, signal='Start Changing Explotion Sprites', sender='Controler')
        self.explotions = []

    def run(self):
        while True:
            for index, i in enumerate(self.explotions):
                time.sleep(0.1)
                self.explotions[index] = self.explotions[index] + 1
                if self.explotions[index] >= 4:
                    self.explotions.pop(0)
                else:
                    dispatcher.send(signal = "Change Explotion Sprite", sender = "bombsExplotionThread", spritenum = (self.explotions[index], index))
                
    def addExplotion(self):
        self.explotions.append(0)