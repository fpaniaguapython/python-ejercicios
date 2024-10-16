'''
Crear la clase Animal
Crear la clase Mamífero (hereda de Animal)
Crear la clase Cuadrúpedo (hereda de Mamífero)
Crear la clase Reptil (hereda de Animal)
Crear una lista con objetos vaca, serpiente, perro, gato y humano
Recorrer la lista e indicar qué objetos son cuadrúpedos (isinstance)
'''
class Animal:
    pass

class Mamifero(Animal):
    pass

class Cuadrupedo(Mamifero):
    pass

class Reptil(Animal):
    pass

vaca = Cuadrupedo()
serpiente = Reptil()
perro = Cuadrupedo()
gato = Cuadrupedo()
humano = Mamifero()

bichos = (vaca, serpiente, perro, gato, humano)

for bicho in bichos:
    if isinstance(bicho, Cuadrupedo):#Probar con Mamifero y Animal
        print("Es un cuadrúpedo")
