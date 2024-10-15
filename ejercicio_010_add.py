class Pelicula:
    def __init__(self,titulo,presupuesto,numero_participantes,duracion) -> None:
        self.titulo = titulo
        self.presupuesto = presupuesto
        self.numero_participantes = numero_participantes
        self.duracion = duracion

    def __add__(self, other):
        return self.duracion + other.duracion

p1 = Pelicula("El resplandor", 140_000_000, 12, 98)
p2 = Pelicula("Alien", 80_000_000, 8, 93)

print(p1 + p2)
