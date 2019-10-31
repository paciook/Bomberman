class powerUp:
    def __init__(self, power, duration):
        self.power = (power, duration)

    def consume(self):
        return self.power
