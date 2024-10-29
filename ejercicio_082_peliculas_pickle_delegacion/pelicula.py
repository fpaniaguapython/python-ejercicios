class Pelicula():
    def __init__(self, titulo, duracion=0) -> None:
        self.titulo = titulo
        self.duracion = duracion

    def __str__(self) -> str:
        return f'Título:{self.titulo}. Duración:{self.duracion}'
    
    def __repr__(self) -> str:
        return f'Título:{self.titulo}. Duración:{self.duracion}'
        
