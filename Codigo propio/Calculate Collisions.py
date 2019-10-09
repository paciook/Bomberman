def collisions(thing):
    dimension = thing.getDimension()
    position = thing.getPosition()

    for line in range(0, dimension[0]): # suponiendo que 0 son las lineas
        for column in range(0, dimension[1]): # suponiendo que 1 son las columnas
            if (map.dimension[position[0] + line][position[1] + column] > 1):
                return True

def calculateCollisions(thing):
    dimension = thing.getDimension()
    position = thing.getPosition()

    for line in range(0, dimension[0]):
        for column in range(0, dimension[1]):
            array = map.getArray()

            if (array[position[0 + line], position[1 + column]] += thing.array[line, column] > 1):
                control.collision()
            
            array[position[0 + line], position[1 + column]] += thing.array[line, column]


    map.setArray(array)