import threading
from pydispatch import dispatcher
import time
import sys


class bombAnimation(threading.Thread):
    def __init__(self, daemon):
        super().__init__(daemon=daemon)
        dispatcher.connect(receiver=self.addExplotion, signal='Start Changing Explotion Sprites', sender='Controler')
        self.explotions = []
        self.sprite = None

    def run(self):
        while True:
            time.sleep(0.1)
            dispatcher.send(signal = "Change Explotion Sprite", sender = "bombsExplotionThread", sprite = self.sprite)

    def addExplotion(self,explotion):
        self.explotions.append(explotion)