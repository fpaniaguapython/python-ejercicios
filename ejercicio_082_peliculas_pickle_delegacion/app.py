from pelicula import Pelicula
from persistencia import GestorPersistencia

EXTENSION = '.movie'

gestor_persistencia = GestorPersistencia()

def crear():
    titulo = input("Título:")
    duracion = int(input("Duración:"))
    pelicula = Pelicula(titulo, duracion)    
    gestor_persistencia.save_movie(pelicula)

def leer():
    lista_archivos_peliculas = gestor_persistencia.get_movies()
    for archivo_pelicula in lista_archivos_peliculas:
        print(archivo_pelicula)
    titulo = input("Título:")
    pelicula = gestor_persistencia.load_movie(titulo)
    print(pelicula)

if __name__=='__main__':
    while (True):
        opcion_principal = int(input("(1)Crear (2)Leer (3)Salir:")) 
        if (opcion_principal==1):
            crear()
        elif (opcion_principal==2):
            leer()
        elif (opcion_principal==3):
            break
        else:
            print("Opción errónea")