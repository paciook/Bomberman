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

def placeObject(thing):
    dimension = thing.getDimension()
    position = thing.getPosition()
    collisions = [thing, []]
    mapArray=controler.getMapArray

    for line in range(0, dimension[0]):
        for column in range(0, dimension[1]):

            if (mapArray[position[0 + line], position[1 + column]] + thing.array[line, column] > 1):
                collisions[1].append([line, collisions])
            
            mapArray[position[0 + line], position[1 + column]] += thing.array[line, column]

    controler.addCollision(collisions)
    controler.setMapArray(mapArray)



    map.setArray(array)

if __name__ == "__main__":
    arrayOf("thorman.png")