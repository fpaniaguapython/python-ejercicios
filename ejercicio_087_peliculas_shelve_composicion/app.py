import os

from pelicula import Pelicula

EXTENSION = '.movie'

def crear():
    titulo = input("Título:")
    duracion = int(input("Duración:"))
    pelicula = Pelicula(titulo, duracion)    
    pelicula.save()

def leer():
    '''
    lista_archivos = os.listdir()
    for archivo in lista_archivos:
        if (archivo.endswith(EXTENSION)):
            print(archivo)
    '''
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