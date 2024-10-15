class Cliente:
    #Constructor con el nombre y el teléfono
    def __init__(self, nombre, telefono) -> None:
        self.nombre = nombre
        self.telefono = telefono

    #Método que le asigne el email (crea un atributo o variable de instancia)
    def asignar_mail(self, email):
        self.email = email

#Crear un objeto cliente
cliente = Cliente('Guillermo', '630112033')
#Agregar un atributo 'saldo'
cliente.saldo = 1000
#setattr(cliente,'saldo',1000)

#¿Cómo saber qué atributos de instancia tiene el objeto?
print(cliente.__dict__)