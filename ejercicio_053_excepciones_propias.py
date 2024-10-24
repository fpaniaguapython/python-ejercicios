# Aplicación de Gestión de Facturas de Jorge

'''
#Solución con una excepción existente
class Factura:
    def __init__(self, nombre_cliente, importe):
        if (len(nombre_cliente)<10):
            raise ValueError("Longitud insuficiente") #Error creado por nosotros
        self.nombre_cliente = nombre_cliente
        self.importe = importe

try:
    f = Factura("Pep",10_000)
except ValueError as ve:
    print(ve)
'''

#Solución con una excepción propia
class LongitudInsuficienteError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
    def mostrar_solucion(self):
        print("Esto no tiene arreglo")

class Factura:
    def __init__(self, nombre_cliente, importe):
        if (len(nombre_cliente)<10):
            raise LongitudInsuficienteError("Longitud insuficiente") #Error creado por nosotros
        self.nombre_cliente = nombre_cliente
        self.importe = importe

try:
    f = Factura("Pep",10_000)
except LongitudInsuficienteError as lie:
    print(lie)
    lie.mostrar_solucion()