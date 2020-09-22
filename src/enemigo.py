import thing


class Enemigo(thing):
    def imagenInicial(self):
        self.image = pygame.image.load('enemy.png') # ¿Qué mejor que un JPG camuflado en PNG?