import json

class Pelicula:
    def __init__(self, titulo):
        self.titulo = titulo

p = Pelicula('Rambo')
print(p.__dict__)