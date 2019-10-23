import threading
import pygame
from pydispatch import dispatcher
import time
DIRECTIONS = {'273': "Back", '274': "Front", '275': "Right", '276': "Left"}


class thormanSpritesThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def reloadThorman(self):
        # time.sleep(0.004)
        dispatcher.send(signal = 'Change thorman sprite', sender = 'thormanSpritesThread')