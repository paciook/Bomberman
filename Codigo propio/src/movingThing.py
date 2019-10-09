import thing


class movingThing(thing):
        def move(self, direction, stepSize):
            for index, item in enumerate(self.position):
                self.position[index] = item+self.stepSize*direction[index]

        def getStepSize():
            return self.stepSize

        def setStepSize(newStepSize):
            self.stepSize = newStepSize
