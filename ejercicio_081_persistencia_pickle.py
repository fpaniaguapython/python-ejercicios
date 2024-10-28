import pickle

class Pelicula:
    def __init__(self, titulo, duracion):
        self.titulo = titulo
        self.duracion = duracion

# pelicula = Pelicula("Título 1", 100)

#Serialización y almacenamiento
'''
with open('pelicula.pckl', 'wb') as fichero:
    pickle.dump(pelicula, file=fichero)
'''

#Lectura y deserialización
with open('pelicula.pckl', 'rb') as fichero:
    pelicula = pickle.load(file=fichero)

print(pelicula.titulo)
print(pelicula.duracion)