# Metaclase hereda de type
# La función type(nombre_clase) indica el tipo de un objeto o clase (en clases siempre será type)
# __name__ en una clase contiene el nombre de la clase
# __class__ en un objeto o clase contiene información sobre la clase a la que pertenece
# __bases__ en una clase contiene información sobre la herencia directa
# __dict__ en una clase contiene métodos y atributos de clase
# __class__ y type(nombre_clase) aplicados a clases proporcionan la misma información

class Enemigo:
    pass

def atacar(self):
    print("Atacando...")

# Clase = type(name, bases, dict)
# name --> Nombre de la clase
# bases --> Tupla con la herencia directa
# dict --> Diccionario con los atributos de clase (atributos y métodos de clase)
Engendro = type('Engendro', (Enemigo,), {'atacar':atacar, 'salud':100})

engendro = Engendro()
print(Engendro.__name__)
print(Engendro.__bases__)
print(Engendro.__dict__)
engendro.atacar()
print(Engendro.salud)

def saludar(self):
    print("Hola")

# Metaclases
# (1) Agregar un atributo de instancia a los objetos de MiMetaclase
# (2) Agregar un atributo de clase a las clases de MiMetaclase
# (3) Agregar un método a una clase de MiMetaclase
class MiMetaclase(type):
    def __new__(mcs, name, bases, dictionary):
        print("En __new__")
        if ('calcular' in dictionary and callable(dictionary['calcular'])):
            print("Existe")
        else:
            raise Exception("No existe el método calcular")

        dictionary['maximo']=100 # (2)
        dictionary['di_hola']=saludar # (3)
        obj = super().__new__(mcs, name, bases, dictionary)
        return obj
    
    def __call__(cls, *args, **kwargs):
        print("En __call__")
        instancia = super().__call__(*args, **kwargs)
        instancia.altura = 10 # (1)
        return instancia

class MiClase(metaclass=MiMetaclase):
    minimo = -100
    def __init__(self) -> None:
        print("En __init__")
    
    def calcular(self):
        pass

miobjeto = MiClase()
print("Altura:", miobjeto.altura)
print(MiClase.maximo)
print(MiClase.minimo)
miobjeto.di_hola()
