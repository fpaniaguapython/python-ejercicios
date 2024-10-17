import gc

class Pelicula:
    def __init__(self, director) -> None:
        self.director = director

class Director:
    pass

director = Director()
aficionado = Director()
pelicula = Pelicula(director)
pelicula2 = Pelicula(aficionado)
pelicula3 = Pelicula(director)

lista_referencias = gc.get_referrers(director)#Obtiene las referencias al objeto
print(len(lista_referencias))#3 --> director, pelicula1 y pelicula3
