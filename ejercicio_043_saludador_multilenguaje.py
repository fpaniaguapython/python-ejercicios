import abc

class Saludador(abc.ABC):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def saludar(self):
        pass

class SaludadorCastellano(Saludador):
    def saludar(self):
        print(f'Hola {self.name}')

class SaludadorIngles(Saludador):
    def saludar(self):
        print(f'Hello {self.name}')        

def get_saludador(nombre):
    opcion = int(input("Seleccion idioma (0-Castellano, 1-Inglés):"))      
    if (opcion==0):
        return SaludadorCastellano(nombre)
    elif (opcion==1):
        return SaludadorIngles(nombre)

if __name__=='__main__':
    nombre = input('Introduce tu nombre:')
    saludador = get_saludador(nombre)
    if (isinstance(saludador, Saludador)):
        saludador.saludar()
    else:
        print("Error")
    