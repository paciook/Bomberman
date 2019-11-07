import copy


class Lightning:
    def __init__(self, position):
        self.position = position
        self.spriteNumber = 0

    def getPosition(self):
        return self.position

    def setSpriteNumber(self):
        self.spriteNumber += 1

    def getSpriteNumber(self):
        return self.spriteNumber
