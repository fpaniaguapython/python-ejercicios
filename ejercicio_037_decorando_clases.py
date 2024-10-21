#Método 'externo' que agregamos a la clase
def saludar(self):
    print("Hola", self.matricula)

#Decorador de clase
def saludador(clase):
    clase.saludar = saludar
    return clase

#Decorador de clase
def contador(clase):
    clase.atributos = clase.__getattribute__

    def detector(self, name):
        if name=='kilometros':
            print("Ha accedido al kilometraje")
        return clase.atributos(self, name)
    
    clase.__getattribute__ = detector
    return clase

#@saludador
@contador
class Coche:
    def __init__(self, matricula):
        self.kilometros = 0
        self.matricula = matricula

coche = Coche('4458-KLM')
print(f'El coche tiene {coche.kilometros} kilómetros')#Ha accedido al kilometraje
print(f'El coche tiene la matrícula {coche.matricula}')
#coche.saludar()