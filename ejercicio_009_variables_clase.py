class Cliente:
    margen_confianza = 10 #Variable de clase
    def __init__(self, nombre, telefono) -> None:
        self.nombre = nombre
        self.telefono = telefono

    def asignar_mail(self, email):
        self.email = email

cliente = Cliente('Guillermo', '630112033')
cliente.saldo = 1000


print(Cliente.margen_confianza)#10
print(cliente.margen_confianza)#10
Cliente.margen_confianza=20
print(Cliente.margen_confianza)#20
print(cliente.margen_confianza)#20

#OJO, ESTAMOS CREANDO UN NUEVO ATRIBUTO DE INSTANCIA
cliente.margen_confianza=30
print(Cliente.margen_confianza)#20
print(cliente.margen_confianza)#30


Cliente.tiempo_espera = 20 #Agregando un atributo de clase
#print(cliente.tiempo_espera)

#¿Cómo saber qué atributos de clase tiene la clase?
#print(Cliente.__dict__)
