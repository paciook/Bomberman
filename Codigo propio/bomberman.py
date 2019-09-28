import thing

class Thorman(thing):
        def __init__(self, nombre, pos=[0,0]):
        self.position = pos
        self.name= name
        self.step_size = 5

    def mover(self,direccion):
        for index,item in enumerate(self.position):
            self.position[index] = item+self.step_size*direccion[index]

    def get_stepsize(self):
        return self.step_size
    
    def set_stepsize(self, NewStep):
        self.step_size = NewStep
    
    def get_nueva_posicion_tentativa(self, direccion):
        print('direccion',direccion)
        lista_aux = []
        for index,item in enumerate(self.posicion_actual):
            lista_aux.append(item+self.step_size*direccion[index])
        return lista_aux

    def get_position(self):
        return self.position