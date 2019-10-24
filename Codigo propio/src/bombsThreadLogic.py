import threading
from pydispatch import dispatcher
import time


class bombTimeCounter(threading.Thread):
    def __init__(self, bombsList):
        super().__init__()
        self.bombs = bombsList
        self.bombTimer = [3]*len(self.bombs)

    def reloadBombs(self):
        while True:
            time.sleep(1)
            for index, i in enumerate(self.bombTimer):
                i = i - 1
                if i == 0:
                    dispatcher.send(signal='Exploded', sender='bombsThread', bomba = index)
