import threading
from pydispatch import dispatcher
import time
import sys

class standingStill(threading.Thread):
    def __init__(self, daemon):
        super().__init__(daemon=daemon)
        threading.Thread.__init__(self)
        dispatcher.connect(receiver = self.moving, signal = "Moving", sender = 'Controler')
        dispatcher.connect(receiver = self.notMoving, signal = "Not Moving", sender = 'Controler')
        self.moving = False

    def run(self):
        while True:
            if self.moving == True:
                pass
            else:
                time.sleep(0.5)
                dispatcher.send(signal = 'Stand Still', sender='thormanStandingThread')
        return

    def moving(self):
        self.moving = True

    def notMoving(self):
        self.moving = False
