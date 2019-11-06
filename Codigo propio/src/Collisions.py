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
    potentialColls = []
    for activeObject1 in activeObjects:
        for activeObject2 in activeObjects:
            if activeObject1 == activeObject2:
                pass     
            else:
                
                object1 = [activeObject1.getPosition()[0] + activeObject1.getHitbox()[0], 
                activeObject1.getPosition()[1] + activeObject1.getHitbox()[1]]
                object2 = [activeObject2.getPosition()[0] + activeObject2.getHitbox()[0],
                activeObject2.getPosition()[1] + activeObject2.getHitbox()[1]]
                
                if activeObject1.getPosition()[0] < activeObject2.getPosition()[0] and object1[0] < activeObject2.getPosition()[0]:
                    if activeObject1.getPosition()[1] < activeObject2.getPosition()[1] and object1[1] < activeObject2.getPosition()[1]:

                        activeObject2.hitBy(activeObject1)
                        activeObject1.hitBy(activeObject2)                    
                        print("Hay colisiones")


def compare(case):
    for x in range(case[0].getPosition()[1], case[1].getPosition()[1] + case[1].getHitbox()[1]):
        aux = []
        for y in range(case[0].getPosition()[0], case[1].getPosition()[0] + case[1].getHitbox()[0]):
            aux.append(0)
        table.append(aux)
    
    for item in case:
        spriteArray = arrayOf(item.getSprite())
        for line in range(item.getPosition[0] - case[0].getPosition()[0], item.getHitbox()[1]):
            for column in range(item.getPosition[1]- case[0].getPosition()[1], item.getHitbox[0]):
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