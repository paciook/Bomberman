import threading
from pydispatch import dispatcher
import time
import sys

class bombAnimation(threading.Thread):
    def __init__(self, daemon, explotionNumber):
        super().__init__(daemon=daemon)
        self.explotionNumber = explotionNumber # ID of each living explotion
        dispatcher.connect(receiver = self.decreaseExplotionNumber, signal = "Delete Explotion", sender = 'bombsExplotionThread')
        self.doesntApplyForMe = False

    def run(self):
        """Controls the life time of the lightning and sends
        a message when it must changes the sprite and when it
        finishes"""
        for i in range(3):
            time.sleep(0.5)
            dispatcher.send(signal = "Change Explotion Sprite", sender = "bombsExplotionThread", explotionNumber = self.explotionNumber)
            if i == 2:
                time.sleep(0.5)
                self.doesntApplyForMe = True
                dispatcher.send(signal = "Delete Explotion", sender = "bombsExplotionThread", explotionNumber = self.explotionNumber)
        return

    def decreaseExplotionNumber(self):
        """Decreases the explotion ID if another lightning dies"""
        if self.doesntApplyForMe is False:
            self.explotionNumber = self.explotionNumber - 1
