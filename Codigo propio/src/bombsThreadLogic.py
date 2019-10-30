import threading
from pydispatch import dispatcher
import time
import sys


class bombTimeCounter(threading.Thread):
    def __init__(self, bombsList):
        super().__init__()
        # self.bombs = [0]
        # self.bombs[0] = 3
        # self.bombTimer = [3]*len(self.bombs)
        self.bombsTimer = []

    def run(self):
        while True:
            time.sleep(1)
            for index, i in enumerate(self.bombTimer):
                self.bombTimer[index] = self.bombTimer[index] - 1
                if self.bombTimer[index] == 0:
                    dispatcher.send(signal='Exploded', sender='bombsThread', bomba = index)

    def setBombsList(self, bombs):
        self.bombTimer.append(bombs[-1].getTime)