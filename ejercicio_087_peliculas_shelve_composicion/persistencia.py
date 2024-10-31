import pickle
import shelve
import abc
import os

EXTENSION = '.movie'

class GestorPersistenciaFactory:
    @staticmethod
    def get_gestor():
        #return GestorPersistenciaPickle()
        return GestorPersistenciaShelve()

class GestorPersistencia(abc.ABC):
    @abc.abstractmethod
    def save(self, object):
        pass

    @abc.abstractmethod
    def load(self, id):
        pass

    @abc.abstractmethod
    def get_movies(self):
        pass

class GestorPersistenciaPickle(GestorPersistencia):
    def save(self, object):
        with open(f'{object.titulo.replace(" ","_")}.movie', 'wb') as file:
            pickle.dump(object, file=file)

    def load(self, id):
        with open(f'{id.replace(" ","_")}.movie', 'rb') as file:
            pelicula = pickle.load(file)
            return pelicula

    def get_movies(self):
        lista_archivos = os.listdir()
        ficheros_peliculas = [archivo.replace(' ','_') for archivo in lista_archivos if archivo.endswith(EXTENSION)]
        return ficheros_peliculas        
        

class GestorPersistenciaShelve(GestorPersistencia):
    nombre_fichero_peliculas = "peliculas.shlv"
    def save(self, object):
        shelve_obj = shelve.open(filename=GestorPersistenciaShelve.nombre_fichero_peliculas)
        shelve_obj[object.titulo.replace(" ","_")]=object
        shelve_obj.close()

    def load(self, id):
        shelve_obj = shelve.open(filename=GestorPersistenciaShelve.nombre_fichero_peliculas)
        pelicula = shelve_obj[id.replace(" ","_")]
        shelve_obj.close()
        return pelicula
    
    def get_movies(self):
        shelve_obj = shelve.open(filename=GestorPersistenciaShelve.nombre_fichero_peliculas)
        return shelve_obj.keys()
    
# if __name__=='__main__':
#    lista = GestorPersistenciaPickle().get_movies()
#    print(lista)