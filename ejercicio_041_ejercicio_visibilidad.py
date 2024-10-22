'''
(x) Crear una clase factura.
(x) El valor del IVA es común a todas las facturas y es privado.
(x) El constructor recibe una lista de Items.
(x) Se verifica en el constructor que todos los elementos de la lista son Items.
(x) Existe un método privado que calcula el importe por cada item (sin IVA).
(x) Existe un método público que proporciona el importe total de la factura.

(x) Clase Item - Nombre producto, numero de unidades y precio unitario.
'''
import functools

class Item:
    def __init__(self, nombre, numero_unidades, precio_unitario):
        self.nombre = nombre
        self.numero_unidades = numero_unidades
        self.precio_unitario = precio_unitario

class Factura:
    __iva = 0.21

    def __init__(self, items):
        self.items = items
        for item in self.items:
            if (not isinstance(item, Item)):
                raise TypeError("Los elementos de la lista deben ser instancias de Item")

    def __get_item_value(self, item):
        value = item.numero_unidades * item.precio_unitario
        return value

    def get_bill_value(self):
        value = 0
        for item in self.items:
            value = value + (self.__get_item_value(item) * (1 + Factura.__iva))
        return value
    
    #Misma solución, utilizando la función reduce (módulo functools) y lambdas
    def get_bill_value_reduce(self):
        value = functools.reduce(lambda a,b : 
                         (self.__get_item_value(a) * (1 + Factura.__iva)) + 
                         (self.__get_item_value(b) * (1 + Factura.__iva)),
                         self.items)
        return value
               
item1 = Item("Cuaderno",2,10)
item2 = Item("Bolígrafo",4,20)
items = [item1, item2]
factura = Factura(items=items)
print(factura.get_bill_value())
print(factura.get_bill_value_reduce())