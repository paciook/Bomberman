class thing:
    def __init__(self, position=[0, 0]):
        self.posicion = position
        self.hitbox = [0, 0]

    def getPosicion(self):
        return self.posicion

    def setPosicion(self, position):
        self.posicion = position

    def hitBy(self, obstacle):
        self.hp = self.hp - obstacle.getDamage()
        if self.hp < 1:
            self.kill()
        print("capooo")

    def kill(self):
        pass

    def getHitbox(self):
        return self.hitbox

    def getPosicion(self):
        return self.posicion
