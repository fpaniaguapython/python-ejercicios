class Enemigo(object):
    #No se pueden tener múltiples constructores (__init__)
    def __init__(self, nombre, salud = 100):
        self.nombre = nombre
        self.salud = salud
   
e = Enemigo(nombre="Fernando",salud=95)

