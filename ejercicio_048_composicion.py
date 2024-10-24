# Herencia
class Motor:
    def arrancar(self):
        pass

class Coche(Motor):
    pass

coche = Coche()
coche.arrancar()

# Composición
class Engine:
    def arrancar(self):
        pass

class Car:
    def __init__(self, engine):
        self.engine = engine

coche = Car(Engine)
coche.engine.arrancar()
