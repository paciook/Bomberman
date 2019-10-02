import thing


class Thorman(thing):
        def __init__(self, name, pos=[0,0]):
        self.position = pos
        self.name= name
        self.stepSize = 5

    def move(self,direction):
        for index,item in enumerate(self.position):
            self.position[index] = item+self.stepSize*direction[index]

    def getStepsize(self):
        return self.stepSize
    
    def setStepsize(self, NewStep):
        self.stepSize = NewStep
    
    def getNewTentativePosition(self, direction):
        print('direction',direction)
        auxList = []
        for index, item in enumerate(self.actualPosition):
            auxList.append(item+self.stepSize*direction[index])
        return auxList

    def getPosition(self):
        return self.position