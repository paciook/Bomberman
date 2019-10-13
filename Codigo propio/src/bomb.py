import time


class Bomb:
    def __init__(self, position):
        self.explotionTime = 4  # seconds
        self.explotionRange = explotionRange
        self.position = position

    def setPosition(self, pos):
        self.position = pos

    def getPosition(self):
        return self.position

    def setExplotionRange(self, exprng):
        self.explotionRange = exprng

    def getExplotionRange(self,):
        return self.explotionRange

    def setExplotionTime(self, exptm):
        self.explotionTime = exptm

    def getExplotionTime(self):
        return self.explotionTime

    def explode(self,):
        pass
