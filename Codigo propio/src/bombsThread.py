import threading
from pydispatch import dispatcher
import time
import sys


class bombTimeCounter(threading.Thread):
    def __init__(self, daemon):
        super().__init__(daemon=daemon)
        dispatcher.connect(receiver=self.setBombsList, signal='Add Bomb', sender='Controler')
        self.bombsTimer = []

    def run(self):
        while True:
            time.sleep(1)
            try:
                for index, i in enumerate(self.bombsTimer):
                    self.bombsTimer[index] = self.bombsTimer[index] - 1
                    if self.bombsTimer[index] == 0:
                        dispatcher.send(signal='Exploded', sender='bombsThread')
                        self.bombsTimer.pop(index)
            except Exception:
                pass

    def setBombsList(self):
        self.bombsTimer.append(3)
