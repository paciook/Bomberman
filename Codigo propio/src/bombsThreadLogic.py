import threading
from pydispatch import dispatcher
import time
import sys


class bombTimeCounter(threading.Thread):
    def __init__(self):
        super().__init__()
        dispatcher.connect(receiver=self.setBombsList, signal='Add Bomb', sender='Controler')
        self.bombsTimer = []
        self.run()

    def run(self):
        while True:
            time.sleep(1)
            try:
                for index, i in enumerate(self.bombTimer):
                    self.bombTimer[index] = self.bombTimer[index] - 1
                    print(i)
                    if self.bombTimer[index] == 0:
                        dispatcher.send(signal='Exploded', sender='bombsThread', bomba = index)
            except Exception:
                pass

    def setBombsList(self):
        self.bombTimer.append(3)
