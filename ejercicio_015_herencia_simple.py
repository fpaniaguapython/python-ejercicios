class Enemigo(object):
    def __init__(self, nombre, salud):
        self.nombre = nombre
        self.salud = salud

    def atacar(self):
        print("Atacando...")

class EnemigoMovil(Enemigo):
    def __init__(self, nombre, salud, velocidad):
        super().__init__(nombre, salud)
        self.velocidad = velocidad
        

#enemigo_movil = EnemigoMovil() #ERROR
enemigo_movil = EnemigoMovil('Orco',100,10)

