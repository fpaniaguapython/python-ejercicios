import sqlite3

# 1. Abrir la conexión (se abre con un nombre de fichero)
# 10. Cerrar la conexión
class Pelicula:
    def __init__(self, id, titulo, duracion):
        self.id = id
        self.titulo = titulo
        self.duracion = duracion

class DBManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.connection = sqlite3.connect(file_name)
        self.__create_model()

    def __create_model(self):
        cursor = self.connection.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS peliculas 
                       (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       titulo TEXT NOT NULL, duracion INTEGER NOT NULL)""")
        cursor.close()

    def insert_movie(self, movie):
        cursor = self.connection.cursor()
        cursor.execute(f"INSERT INTO peliculas (titulo, duracion) VALUES ('{movie.titulo}',{movie.duracion})")
        self.connection.commit()
        cursor.close()

    def __del__(self):
        self.connection.close()

DB_NAME = "movies.db"

pelicula = Pelicula(0, 'Batman', 100)
DBManager(DB_NAME).insert_movie(pelicula)
