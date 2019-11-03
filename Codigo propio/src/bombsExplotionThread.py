import threading
from pydispatch import dispatcher
import time
import sys

class bombAnimation(threading.Thread):
    def __init__(self, daemon, explotionNumber):
        super().__init__(daemon=daemon)
        # dispatcher.connect(receiver=self.addExplotion, signal='Start Changing Explotion Sprites', sender='Controler')
        self.explotionNumber = explotionNumber
        dispatcher.connect(receiver = self.decreaseExplotionNumber, signal = "Delete Explotion", sender = 'bombsExplotionThread')

    def run(self):
        for i in range(4):
            time.sleep(0.5)
            dispatcher.send(signal = "Change Explotion Sprite", sender = "bombsExplotionThread", explotionNumber = (self.explotionNumber, i))
            if i == 3:
                time.sleep(0.5)
                dispatcher.send(signal = "Delete Explotion", sender = "bombsExplotionThread", explotionNumber = (self.explotionNumber))
        return

    def decreaseExplotionNumber(self):
        self.explotionNumber -= 1











        
# class bombAnimation(threading.Thread):
#     def __init__(self, daemon):
#         super().__init__(daemon=daemon)
#         dispatcher.connect(receiver=self.addExplotion, signal='Start Changing Explotion Sprites', sender='Controler')
#         self.explotions = []

#     def run(self):
#         while True:
#             for index, i in enumerate(self.explotions):
#                 time.sleep(0.0001)
#                 self.explotions[index] = self.explotions[index] + 1
#                 if self.explotions[index] >= 4:
#                     self.explotions.pop(index)
#                 else:
#                     dispatcher.send(signal = "Change Explotion Sprite", sender = "bombsExplotionThread", spritenum = (index))
                
#     def addExplotion(self):
#         self.explotions.append(0)


