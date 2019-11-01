import threading
from pydispatch import dispatcher
import time
import sys


class bombAnimation(threading.Thread):
    def __init__(self, daemon):
        super().__init__(daemon=daemon)
        dispatcher.connect(receiver=self., signal='Start Changing Explotion Sprites', sender='Controler')
        

    def run(self):
        while True:
            time.sleep(0.1)
            dispatcher.send(signal = "Change Explotion Sprite", sender = "bombsExplotionThread", bomb)
