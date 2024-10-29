import pickle
import os

EXTENSION = '.movie'

class GestorPersistencia:
    def save_movie(self, movie):
        with open(f'{movie.titulo.replace(" ","_")}.movie', 'wb') as file:
            pickle.dump(movie, file=file)

    def load_movie(self, titulo):
        with open(f'{titulo.replace(" ","_")}.movie', 'rb') as file:
            pelicula = pickle.load(file)
            return pelicula
        
    def get_movies(self):
        file_list = os.listdir()
        movies_list = [file_name for file_name in file_list if file_name.endswith(EXTENSION)]
        return movies_list