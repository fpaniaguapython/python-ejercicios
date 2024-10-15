class Cosa: #Definición del nombre de la clase
    def __init__(self, nombre : str) -> None: #Constructor?
        self.nombre = nombre #Atributo

    def saludar(self): #Método?
        self.edad = 15 #Agregando un nuevo atributo al objeto que ejecuta saludar
        print("Hola")

cosa = Cosa("Mando")
print(cosa.nombre) #'Mando'
#print(cosa.edad) #AttributeError
cosa.saludar()
print(cosa.edad) #15
cosa.altura = 150
#cosa.despedir()#AttributeError

print(callable(cosa.nombre)) #False
print(callable(cosa.saludar)) #True

#Función hasattr (nos indica si un OBJETO tiene una ATRIBUTO), 
if (not hasattr(cosa, "despedir")):
    print("No tengo esa funcionalidad")
if (hasattr(cosa, "saludar")):
    cosa.saludar()

#Función getattr (proporciona el valor de un atributo de un objeto)
print(getattr(cosa, "nombre")) #Mando
print(getattr(cosa,"velocidad",180)) #180

#Función setattr
setattr(cosa, "altura", 215) 
print(cosa.altura) #215
setattr(cosa, "ciudad", "Zaragoza")
print(cosa.ciudad) #Zaragoza




