class Pelicula:
    def __init__(self, titulo, director, anyo):
        self.titulo = titulo
        self.director = director
        self.anyo = anyo
    
    def mostrar_ficha(self):
        ficha = f'{self.titulo}:{self.director}:{self.anyo}'
        print(ficha)

peliculas = [Pelicula("P1","D1",1901),Pelicula("P2","D2",1902),Pelicula("P3","D3",1903)]

p1 = Pelicula("P1","D1",1901)
p2 = Pelicula("P2","D2",1902)
p3 = Pelicula("P3","D3",1903)
peliculas = [p1,p2,p3]

peliculas = []
peliculas.append(p1)
peliculas.append(p2)
peliculas.append(p3)

for pelicula in peliculas:
    pelicula.mostrar_ficha()