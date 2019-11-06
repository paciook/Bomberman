import threading
from pydispatch import dispatcher
import time

class ticker(threading.Thread):
    def __init__(self, daemon):
        super().__init__(daemon=daemon)

    def run(self):
        while True:
            time.sleep(0.05)
            dispatcher.send(signal='Tick')
