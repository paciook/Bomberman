import threading
from pydispatch import dispatcher
import time

class enemy(threading.Thread):
    def __init__(self, daemon):
        super().__init__(daemon=daemon)
