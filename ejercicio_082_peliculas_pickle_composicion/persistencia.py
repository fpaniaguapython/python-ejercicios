import pickle
import abc

class GestorPersistenciaFactory:
    @staticmethod
    def get_gestor():
        return GestorPersistenciaPickle()

class GestorPersistencia(abc.ABC):
    @abc.abstractmethod
    def save(self, object):
        pass

    @abc.abstractmethod
    def load(self, id):
        pass

class GestorPersistenciaPickle(GestorPersistencia):
    def save(self, object):
        with open(f'{object.titulo.replace(" ","_")}.movie', 'wb') as file:
            pickle.dump(object, file=file)

    def load(self, id):
        with open(f'{id.replace(" ","_")}.movie', 'rb') as file:
            pelicula = pickle.load(file)
            return pelicula