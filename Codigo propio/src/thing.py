class thing:
    def __init__(self, position=[0, 0]):
        self.position = position
        self.hitbox = [0, 0]

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position

    def hitBy(self, obstacle):
        self.hp = self.hp - obstacle.getDamage()
        if self.hp < 1:
            self.kill()
        print("capooo")
        
    def kill(self):
        pass

    def getDamage(self):
        return self.damage

    def getHitbox(self):
        return self.hitbox
