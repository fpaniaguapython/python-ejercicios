#Métodos de instancia, de clase y estáticos
class Enemigo:
    numero_maximo_enemigos = 0 #Atributo de clase
    numero_enemigos = 0 #Atributo de clase

    def __init__(self, nombre, vida):
        self.nombre = nombre #Atributo de instancia
        self.vida = vida #Atributo de instancia
        Enemigo.numero_enemigos = Enemigo.numero_enemigos + 1

    def destruir(self):#Método de instancia
        print(f'Destruyendo {self.nombre}')
        Enemigo.numero_enemigos = Enemigo.numero_enemigos - 1

    @classmethod
    def set_numero_maximo_enemigos(cls, numero):
        cls.numero_maximo_enemigos = numero

    @staticmethod
    def mostrar_informacion(nombre):
        print("Información:", nombre)

e1 = Enemigo("Enemigo 1", 100)
e2 = Enemigo("Enemigo 2", 100)
Enemigo.set_numero_maximo_enemigos(10)

print(Enemigo.numero_maximo_enemigos)#10
print(e1.numero_maximo_enemigos)#10
print(e2.numero_maximo_enemigos)#10

Enemigo.mostrar_informacion("Prueba")#Información
e1.mostrar_informacion("Prueba")#Información
e2.mostrar_informacion("Prueba")#Información