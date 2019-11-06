import controlador
import intentodepacio

class Juego():
    def __init__(self, nombre_jugador, dimensiones):
        self.nombre = nombre_jugador
        self.dimensiones = dimensiones
        self.thorman = intentodepacio.Thorman(self.nombre)
        self.objetosActivos = [self.thorman]
        self.bombasActivas = 0

    def moverThor(self, direccion):
        self.thorman.mover(direccion)

    def getThorPosicion(self):
        return self.thorman.getPosition()

    def plantarBomba(self):
        if self.thorman.getBmDisp() > self.bombasActivas:
            self.objetosActivos.append(self.thorman.plantar())
            self.bombasActivas += 1
            print("Añadido a lista")
