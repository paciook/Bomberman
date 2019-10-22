import threading.Thread

class bombTimeCounter(threading.Thread):
    def __init__(self):
        super().__init__()
        