class thing:
    def __init__(self, position=[0, 0]):
        self.position = position
        self.sprite = 'path/to/sprite'

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def hitBy(self, obstacle):
        self.hp = self.hp - obstacle.getDamage()
        if self.hp > 1:
            self.kill()
        print("capooo")
        
    def kill(self):
        pass
