from persistencia import GestorPersistenciaFactory, GestorPersistenciaPickle, GestorPersistencia

class Pelicula():
    def __init__(self, titulo, duracion=0) -> None:
        self.titulo = titulo
        self.duracion = duracion
        self.gestor_persistencia = GestorPersistenciaFactory.get_gestor()

    def save(self):
        self.gestor_persistencia.save(self)

    def load(self):
        pelicula = self.gestor_persistencia.load(self.titulo)
        self.duracion = pelicula.duracion

    def __str__(self) -> str:
        return f'Título:{self.titulo}. Duración:{self.duracion}'
    
    def __repr__(self) -> str:
        return f'Título:{self.titulo}. Duración:{self.duracion}'
        
