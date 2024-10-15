'''
Clase Automovil, con los atributos Marca, Precio, Consumo y Velocidad
Crear una lista de automóviles ordenada por precio (mejor el más 
barato) y consumo (mejor el más económico)
(varios automóviles tienen el mismo precio)
'''
class Automovil:
    def __init__(self, marca, precio, consumo, velocidad):
        self.marca = marca
        self.precio = precio
        self.consumo = consumo
        self.velocidad = velocidad

    '''
    def __lt__(self, other):
        if (self.precio != other.precio):
            return self.precio < other.precio
        return self.consumo < other.consumo
    '''

    def __lt__(self, other):
        return self.precio < other.precio if self.precio != other.precio else self.consumo < other.consumo


    def __repr__(self) -> str:
        return self.marca


a1 = Automovil("Seat",10_000, 9.8, 100) 
a2 = Automovil("Skoda",8_000, 9.3, 100) 
a3 = Automovil("Ferrari",8_000, 15, 100) 

automoviles = [a1,a2,a3]
automoviles.sort()
print(automoviles)