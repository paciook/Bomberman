import time


class Bomba:
    def __init__(self, position, explotionRange):
        self.explotionTime = 2  # segundos

        self.plantar(position, explotionRange)

    def plantar(self, position, explotionRange, explotionTime):

        self.setPosition(position)
        self.setExplotionRange(explotionRange)
        self.setExplotionTime(explotionTime)

        time.sleep(self.getExplotionTime())

        self.explode()

    def setPosition(pos):
        self.position = pos

    def getPosition():
        return self.position

    def setExplotionRange(exprng):
        self.explotionRange = exprng

    def getExplotionRange():
        return self.explotionRange

    def setExplotionTime(exptm):
        self.explotionTime = exptm

    def getExplotionTime():
        return self.explotionTime

    def explode():
        
