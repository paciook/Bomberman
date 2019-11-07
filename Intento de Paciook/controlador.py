import vista
import juego
import pygame
import sys
from muro import muro
import time


CONTROLES = {'273': [0, -1], '274': [0, 1], '275': [1, 0], '276': [-1, 0]}

class Controlador:
    def __init__(self):
        # El controlador inicializa el juego
        # y la vista.
        self.dimensiones = (1260, 700)
        self.juego = juego.Juego('Fede', self.dimensiones)
        self.vista = vista.Vista(self.dimensiones, self.juego)
        self.sleep = 0.005

        self.vista.loadSprites()
        self.vista.carga_imagen_fondo()
        self.vista.cargar_imagen_bomberman([50, 50])
        self.flipearAll()
        self.main_loop()

    

    def main_loop(self):
        contador = 0
        while True:
            for event in pygame.event.get():
               
                if event.type == pygame.QUIT: sys.exit()
                #self.juego.mover_bm(event.tevent_name())
               
                if event.type==pygame.KEYDOWN: # alguien presionó una tecla
                    #print(pygame.event.event_name(event.type))
                    #print(event.key)
                    if str(event.key)=='32':

                        self.juego.plantarBomba()

                    else:
                        if str(event.key) in CONTROLES:
                            self.juego.moverThor(CONTROLES[str(event.key)])
                            
                        else:
                            print(str(event.key))
            
                    # self.vista.recargarFondo()
                    # self.vista.recargarThor()
            
            # self.vista.cargarBombas(self.juego.getBombas())
            # pygame.display.flip()
            
            if len(self.juego.getBombas()) != 0:
                contador += 1
                # print(contador)
                print(self.juego.getBombas()[0].getPosicion())
            
            if contador == 200:
                contador += 1
                self.juego.explotarBomba()

            if contador == 300:
                contador = 0
                self.juego.apagarExplosion()
            
            if len(self.juego.getExplosiones()) != 0: contador += 1
            print(contador)
            
            self.flipearAll()


            time.sleep(self.sleep)


    def flipearAll(self):
        self.vista.recargarFondo()
        self.vista.cargarBombas(self.juego.getBombas())
        self.vista.cargarExplosiones(self.juego.getExplosiones())
        self.vista.recargarThor()
        self.vista.cargarMuros(self.juego.getMuros())
        pygame.display.flip()





if __name__=="__main__":
    controlador = Controlador()

# Dale Luna aprobanos lo empecé el 11/6 porque con el otro no ibamos a llegar a ningún lado