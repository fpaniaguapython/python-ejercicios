
def arrancar(self):
    print(f'Arrancando {self.marca}')

def ordenar_por_precio(self, other):
    return self.precio < other.precio

def ordenar_por_consumo(self, other):
    return self.consumo < other.consumo

class Vehiculo:
    def __init__(self,marca,precio,consumo) -> None:
        self.marca = marca
        self.precio = precio
        self.consumo = consumo
    
    def __repr__(self) -> str:
        return self.marca

panda = Vehiculo("Seat",18_000_000, 44)
fabia = Vehiculo("Skoda",15_000_000, 33)

Vehiculo.arrancar = arrancar
panda.arrancar()

Vehiculo.__lt__ = ordenar_por_precio
lista = [panda, fabia]
lista.sort()
print(lista)
