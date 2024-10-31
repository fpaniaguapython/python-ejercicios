from persistencia import GestorPersistenciaFactory

from pelicula import Pelicula


def crear():
    titulo = input("Título:")
    duracion = int(input("Duración:"))
    pelicula = Pelicula(titulo, duracion)    
    pelicula.save()

def leer():
    gestor_persistencia = GestorPersistenciaFactory.get_gestor()
    ficheros = gestor_persistencia.get_movies()
    for fichero in ficheros:
        print(fichero)
    titulo = input("Título:")
    pelicula = Pelicula(titulo)
    pelicula.load()
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