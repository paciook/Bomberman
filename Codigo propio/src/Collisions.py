import controler
from PIL import Image

def arrayOf(pathOfFile):
    
    # I open the image and generate a pixel map of it
    im = Image.open(pathOfFile)
    pixels = im.load()

    array = []

    # Checking each pixel's color value and storing them into an array
    for line in range (0, im.size[0]):
        width = []
        for column in range (0, im.size[1]):
            
            aux = 0

            for value in pixels[column, line]:
                aux += value
            
            if (aux != 0):
                width.append(1)
                print(1, end='')
            else:
                width.append(0)
                print(' ', end='')
        array.append(width)
        print('/t')
    return array



""" def collisions(thing):
    dimension = thing.getDimension()
    position = thing.getPosition()

    for line in range(0, dimension[0]): # suponiendo que 0 son las lineas
        for column in range(0, dimension[1]): # suponiendo que 1 son las columnas
            if (map.dimension[position[0] + line][position[1] + column] > 1):
                return True """

def closeness(activeObjects):
    for item1 in range(0, activeObjects[__len__]):
        for item2 in range(0, activeObjects[__len__]):
            if item1 == item2:
                pass     
            else:
                if activeObjects[item2].getPosition()[0] > activeObjects[item1].getPosition()[0] and activeObjects[item2].getPosition()[0] < activeObjects[item1].getPosition()[0] + activeObjects[item1].getWidth():
                    potentialColls.append([item1, item2])
    return potentialColls


def compare(case):
    for x in range(case[0].getPosition()[1], case[1].getPosition()[1] + case[1].getHeight()):
        aux = []
        for y in range(case[0].getPosition()[0], case[1].getPosition()[0] + case[1].getWidth()):
            aux.append(0)
        table.append(aux)
    
    for item in case:
        spriteArray = arrayOf(item.getSprite)
        for line in range(item.getPosition[0] - case[0].getPosition()[0], item.getHeight):
            for column in range(item.getPosition[1]- case[0].getPosition()[1], item.getWidth):
                if spriteArray[line - item.getPosition[0] - case[0].getPosition()[0]][column - item.getPosition[1]- case[0].getPosition()[1]] == 1:
                    table[line][column] += 1
        
        for line in table:
            if 2 in line:
                case[0].hitBy(case[1])
                case[1].hitBy(case[0])
                return True
        return False

if __name__ == "__main__":
    arrayOf("thorman.png")