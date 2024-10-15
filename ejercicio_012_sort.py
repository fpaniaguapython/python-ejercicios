class Pelicula:
    def __init__(self,titulo,presupuesto,numero_participantes,duracion) -> None:
        self.titulo = titulo
        self.presupuesto = presupuesto
        self.numero_participantes = numero_participantes
        self.duracion = duracion

    def __repr__(self):
        return self.titulo

    def __lt__(self, other):
        return self.duracion < other.duracion

p1 = Pelicula("El resplandor", 140_000_000, 12, 150)
p2 = Pelicula("Alien", 80_000_000, 8, 93)
p3 = Pelicula("Batman", 200_000_000, 28, 130)

peliculas = [p1,p2,p3]
#peliculas.sort()
peliculas = sorted(peliculas)
print(peliculas)