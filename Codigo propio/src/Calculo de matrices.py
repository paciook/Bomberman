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

if __name__ == "__main__":
    arrayOf("thorman.png")