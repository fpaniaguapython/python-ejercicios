class Cosa:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
    
    def saludar(self):
        print("Hola")

cosa = Cosa("cosa")

print(Cosa.__class__) #<class 'type'>
print(cosa.__class__) #<class '__main__.Cosa'>
print(cosa.nombre.__class__) #<class 'str'>
print(cosa.saludar.__class__) #<class 'method'>