'''
Clase abstracta:
1. Alguno de sus métodos no está implementado (método abstracto).
2. No se puede instanciar.
3. La clase que hereda de una clase abstracta debe implementar todos sus métodos o
   ser abstracta.
4. En Python, las clases abstractas heredan de abc.ABC (módulo abc)
5. En Python, los métodos abstractos se 'decoran' con @abstractmethod
6. Si una clase tiene herencia múltiple de varias clases abtractas debe implementar
   todos los métodos abstractos.
'''
from abc import ABC, abstractmethod

class Motor(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def arrancar(self):
        pass

    def mostrar_info(self):
        print("Mostrando información...")

#m = Motor()#TypeError: Can't instantiate abstract class Motor without an implementation for abstract method 'arrancar'

class MotorDiesel(Motor):
    def arrancar(self):
        print("Arrancando el motor diesel")

m = MotorDiesel()