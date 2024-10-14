class Enemigo(object):
    def __init__(self, nombre, salud, danyo):
        #Atributos
        self.nombre = nombre
        self.salud = salud
        self.danyo = danyo
        self.vivo = True
        self.posicion = [0,0,0]
    
    #Métodos
    def caminar(self, dx, dy, dz):
        self.posicion = [
            self.posicion[0] + dx,
            self.posicion[1] + dy,
            self.posicion[2] + dz
        ]
    
    def atacar(self, fuerza):
        pass

    def __str__(self):
        #return self.nombre + ":" + str(self.posicion)
        return f'{self.nombre}:{self.posicion}'
    
enemigo = Enemigo("Orco",100, 50)
enemigo.caminar(1,0,-1)
print(enemigo)