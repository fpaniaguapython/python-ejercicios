'''
Clase Vehiculo
Clase Automovil(Vehiculo)
Clase Barco(Vehiculo)
Clase Anfibio(Automovil,Barco)
Todas las clases tienen un método 'arrancar'
Todas las clases tienen un método 'avanzar', excepto Anfibio
Todos los métodos escriben el texto 
    'Soy Barco y estoy arrancando...' o análogo
'''
class Vehiculo:
    def arrancar(self):
        print("Soy Vehiculo y estoy arrancando...")
    def avanzar(self):
        print("Soy Vehiculo y estoy avanzando...")
    def destruir(self):
        print("Soy Vehiculo y estoy destruyendo...")

class Automovil(Vehiculo):
    def arrancar(self):
        print("Soy Automóvil y estoy arrancando...")
    def avanzar(self):
        print("Soy Automóvil y estoy avanzando...")

class Barco(Vehiculo):
    def arrancar(self):
        print("Soy Barco y estoy arrancando...")
    def avanzar(self):
        print("Soy Barco y estoy avanzando...")
    def atracar(self):
        print("Soy Barco y estoy atracando...")
    def destruir(self):
        print("Soy Barco y estoy destruyendo...")

class Anfibio(Automovil, Barco):
    def arrancar(self):
        print("Soy Anfibio y estoy arrancando...")

# MRO - Orden de Resolución de Métodos
a = Anfibio()
a.arrancar()#Anfibio
a.avanzar()#Automovil
a.atracar()#Barco
a.destruir()#Barco

class Engendro(Vehiculo, Barco):
    def arrancar(self):
        print ("Soy Engendro y estoy arrancando...")

e = Engendro()
e.arrancar()#TypeError: Cannot create a consistent method resolution order (MRO) for bases Vehiculo, Barco