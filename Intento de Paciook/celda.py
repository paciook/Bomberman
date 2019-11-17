class celda():
    def __init__(self):
        self.contenido = None

    def getContenido(self):
        return self.contenido

    def setContenido(self, contenido):
        self.contenido = contenido
        return contenido

    def reaccionar(self, objeto):
        if not self.contenido is None:
            self.contenido.reaccionar(objeto)