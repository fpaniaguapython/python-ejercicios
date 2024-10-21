'''
Crear un decorador de clases que verifique ante cualquier
set de un atributo de tipo entero que no es par.
Si es par, lanza un ValueError.
'''
def setattr_decorator(clase):
    clase.setattribute = clase.__setattr__
    
    def wrapper(self, name, value):
        self.setattribute(name, value) #Haciendo el set del atributo
        if (isinstance(value, int) and (value%2==0)):
            raise ValueError("Esta clase no admite pares")
    
    clase.__setattr__ = wrapper
    return clase

@setattr_decorator
class Maths:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

try:
    Maths(3,4)
except ValueError as ve:
    print(ve)